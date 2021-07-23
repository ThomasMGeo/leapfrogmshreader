# leapfrog .msh reader
A simple reader of leapfrog mesh files, without onerous installation requirements.


This was extracted from [GemGis](https://github.com/cgre-aachen/gemgis), a fantastic package. One downside to GemGIS is the installation requirements. 

This package is meant to be a lightweight, single use case, reader for leapfrog .msh files.


# Installation

!pip install leapfrogmshreader

## use:

from leapfrogmshreader import reader

data = reader.read_leapfrog_msh(path='filename.msh')
