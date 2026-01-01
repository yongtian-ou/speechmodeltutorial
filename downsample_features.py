
def downsample_features(features,story):
    """Downsample features to fMRI TRs using lanczos interpolation based on word timings.
    features: np.ndarray of shape (n_words, n_features) or (n_words,)
    story: string, name of the story to get word timings
    Returns: np.ndarray of shape (n_TRs_trimmed, n_features)
    """

    from interpdata import lanczosinterp2D
    Rstories = ['alternateithicatom', 'avatar', 'howtodraw', 'legacy', 
            'life', 'myfirstdaywiththeyankees', 'naked', 
            'odetostepfather', 'souls', 'undertheinfluence']

    # Pstories are the test (or Prediction) stories (well, story), which we will use to test our models
    Pstories = ['wheretheressmoke']

    allstories = Rstories + Pstories

    # Load TextGrids and TR files
    from stimulus_utils import load_grids_for_stories,load_generic_trfiles
    grids = load_grids_for_stories(allstories)
    trfiles = load_generic_trfiles(allstories)

    # Make word and phoneme datasequences
    from dsutils import make_word_ds
    wordseqs = make_word_ds(grids, trfiles) # dictionary of {storyname : word DataSequence}

    # check if the story is valid
    assert story in allstories, f'Story {story} not found in allstories! Stories available: {allstories}'
    
    # check if features is 1D, if so, reshape to 2D with one column
    if features.ndim == 1:
        features = features.reshape(-1, 1)
    # check if feature length matches wordseqs[story] length, if not, transpose and check again
    if features.shape[0] != len(wordseqs[story].data):
        features = features.T
        assert features.shape[0] == len(wordseqs[story].data), f'Feature length {features.shape[0]} does not match word count {len(wordseqs[story].data)} for story {story} even after transposing!'
    
    print(f'Downsampling {features.shape[1]} feature(s) for story {story}...')

    trim = 5
    downsampled_features = np.zeros((len(wordseqs[story].tr_times)-5-2*trim, features.shape[1]))  # Initialize downsampled_features with correct shape
    # loop through each feature to process
    for i in range(features.shape[1]):
        print(f'Processing feature {i+1}/{features.shape[1]}:')
        feature = features[:, i]
        # check if feature has NaN values and fill in with mean of the feature
        print(f"Number of NaN values in feature: {np.sum(np.isnan(feature))}")

        if np.any(np.isnan(feature)):
            mean_feat = np.nanmean(feature)
            feat_nonan = np.where(np.isnan(feature), mean_feat, feature)
            print(f"Filled NaN values with mean value: {mean_feat}")

        # z-score the feature
        feat_nonan_zscore = (feat_nonan - np.mean(feat_nonan))/ np.std(feat_nonan)

        # downsample the feature to fMRI TRs using lanczos interpolation
        feature_downsampled = lanczosinterp2D(feat_nonan_zscore,wordseqs[story].data_times, wordseqs[story].tr_times, window=3,cutoff_mult=0.5)

        # trim TRs and z-score
        feature_downsampled_trimmed = feature_downsampled[5+trim:-trim]
        feature_downsampled_trimmed_zscore = (feature_downsampled_trimmed - np.mean(feature_downsampled_trimmed))/ np.std(feature_downsampled_trimmed)
        # store back
        downsampled_features[:, i] = feature_downsampled_trimmed_zscore.squeeze()
    return downsampled_features