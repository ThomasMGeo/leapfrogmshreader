"""
Contributor: Thomas Martin

This has been used from GemGis, more specifically the raster toolkit.

https://github.com/cgre-aachen/gemgis/blob/main/gemgis/raster.py

leapfrog_msh_reader is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


leapfrog_msh_reader is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (LICENSE) for more details.

For more information on LGPL, check out the wikipedia: https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License
"""

import numpy as np
import linecache
import pandas as pd
from typing import Union, List, Sequence, Optional, Iterable, Dict, Tuple
from pathlib import Path

dtype_conversion = {
    "Integer": np.int32,
    "Double": np.float64
}


def read_leapfrog_msh(path: Union[str, Path]) -> Dict[str, np.ndarray]:
    """Function to read Leapfrog .msh files - https://help.leapfrog3d.com/Geo/4.3/en-GB/Content/meshes/meshes.htm
    Parameters
    __________
        path : Union[str, Path]
            Path to msh file, e.g. ``path='mesh.msh'``
    Returns
    _______
        data : Dict[str, np.ndarray]
            Dict containing the mesh data
    Example
    _______
        >>> # Loading Libraries and File
        >>> import gemgis as gg
        >>> data = gg.raster.read_msh('mesh.msh')
        >>> data
        {'Tri': array([[    0,     1,     2],
        [    0,     3,     1],
        [    4,     3,     0],
        ...,
        [53677, 53672, 53680],
        [53679, 53677, 53680],
        [53673, 53672, 53677]]),
        'Location': array([[ 1.44625109e+06,  5.24854344e+06, -1.12743862e+02],
        [ 1.44624766e+06,  5.24854640e+06, -1.15102216e+02],
        [ 1.44624808e+06,  5.24854657e+06, -1.15080548e+02],
        ...,
        [ 1.44831008e+06,  5.24896679e+06, -1.24755449e+02],
        [ 1.44830385e+06,  5.24896985e+06, -1.33694397e+02],
        [ 1.44829874e+06,  5.24897215e+06, -1.42506587e+02]])}
    See Also
    ________
        read_ts : Reading a GoCAD TSurface File
        read_asc : Reading ESRI ASC files
        read_zamp : Reading Petrel ZMAP Files
    """

    # Checking that the path is of type string or a path
    if not isinstance(path, (str, Path)):
        raise TypeError('Path must be of type string')

    # Getting the absolute path
    path = os.path.abspath(path=path)

    # Checking that the file has the correct file ending
    if not path.endswith(".msh"):
        raise TypeError("The mesh must be saved as .msh file")

    # Opening the file
    with open(path, "rb") as f:

        chunk = f.read(512)
        header_end = chunk.find(b"[binary]")
        data = {}
        f.seek(header_end + 0x14)

        # Extracting data from each line
        for line in chunk[chunk.find(b"[index]") + 8:header_end].decode("utf-8").strip().split("\n"):
            name, dtype, *shape = line.strip().rstrip(";").split()
            shape = list(map(int, reversed(shape)))
            dtype = dtype_conversion[dtype]
            data[name] = np.fromfile(
                f,
                dtype,
                np.prod(shape)
            ).reshape(shape)

    return data