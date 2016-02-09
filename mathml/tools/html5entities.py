#!/usr/bin/python

from utils.misc import downloadWithProgressBar

# FIXME: DownBreve, tdot, TripleDot and DotDot will no longer be prefixed with
# a space.
# See https://github.com/w3c/xml-entities/commit/59df3c0260780a5beea06d1a8f78d1ba7e22abfc
downloadWithProgressBar("https://www.w3.org/2003/entities/2007/htmlmathml.json",
                        outputDirectory="../relations/html5-tree/",
                        forceDownload=True)
