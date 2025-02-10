"""Miscellaneous functions for the plotpalette package."""

__all__ = ['clear_cache']

import matplotlib
import os

def clear_cache() -> None:
    """Clear the cache.

    This function can be very useful when there's something wrong and cannot
    be fixed by other means. For example, when the matplotlib cannot find
    a font, you can clear the cache to force it to find the font again.
    """
    cache_dir = matplotlib.get_cachedir()
    for file in os.listdir(cache_dir):
        os.remove(os.path.join(cache_dir, file))
