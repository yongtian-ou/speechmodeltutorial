# speechmodeltutorial forked for replication of Huth et al. (2016)

This repository was originally given as a tutorial at EACL 2014 by Alex Huth.

`Tia_replication.ipynb` uses this repository as the code base to replicate the semantic model in Huth et al. (2016) (full citation see below). Full dataset used for replication comes from [this repository](https://gin.g-node.org/gallantlab/story_listening/src/master). To fetch these data, see Installation.

In `speechmodeltutorial.ipynb` you will step through a voxel-wise modeling analysis. You will use computational models to extract semantic features from a natural speech stimulus. Then these features will be used to build linear models of fMRI data. 

#### Acknowledgements
This fMRI data used in this tutorial was collected by Alex Huth and Wendy de Heer at the University of California, Berkeley. All work was supervised by professors Jack Gallant and Frederic Theunissen of the UC Berkeley Psychology Department. Please do not redistribute the code or data used here. 

#### Citation
The analysis demonstrated in this tutorial forms the basis of this paper:
[Huth, A. G. et al., "Natural speech reveals the semantic maps that tile human cerebral cortex" (2016) _Nature_.](https://www.nature.com/articles/nature17637)

Installation
------------
1. Download [data files from tutorial](https://utexas.box.com/shared/static/4n3lemyec0wlj5rcr80991nxwflsbks9.zip) and unzip in this directory. Should create a directory called `data`.
2. Download [data files from paper](https://gin.g-node.org/gallantlab/story_listening/src/master) and copy all files into the `data` directory above.
3. (If not using Anaconda) install dependencies:
`sudo apt-get update`
`sudo apt-get install -y ipython ipython-notebook python-numpy python-scipy python-matplotlib cython python-pip python-pip python-dev python-h5py python-nibabel python-lxml python-shapely python-html5lib mayavi2 python-tables git`

    (If using Conda): `conda install python 'cython=0.29.36' pytables h5py jupyter matplotlib numpy scipy` (NOTE: some packages may be missing from this list)

4. Start a Jupyter notebook server in this directory (if you don't have one):
`jupyter notebook`
