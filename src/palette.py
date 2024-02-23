# Palette-loading utility function, by Kevin.
# Public domain.  Have fun.

import re


def load_palette(src):
    """Loads a palette file and returns a list suitable for Surface.setpalette()

    Loads a palette file, which is anything that looks like this:

    0 0 0
    0 0  4
    0 64 8
    ...

    GIMP and Fractint palette files both match this description.
    Lines that don't match are silently ignored.
    Only recognizes decimal values, not 0xFF or #AA66FF.
    """

    with open(src) as f:
        pal = []
        rgb_re = re.compile("^(?:\s+)?(\d+)\s+(\d+)\s+(\d+)")
        for l in f.readlines():
            m = rgb_re.search(l)
            if m:
                pal.append(tuple(map(int, m.groups())))
    return pal
