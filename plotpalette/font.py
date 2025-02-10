"""Allow applications to use custom fonts in plots easily."""

__all__ = ['set_font']

import matplotlib
import contextlib

@contextlib.contextmanager
def set_font(font_name: str) -> None:
    """Set the font of the plot.

    Note: If you find the matplotlib cannot find the font, try to call
    `plotpalette.clear_cache()` to clear the cache.

    Args:
        font_name (str): The name of the font to use.

    Example:
        with plotpalette.set_font('Monospace'):
            main()
    """
    old_font = matplotlib.rcParams['font.family']
    matplotlib.rcParams['font.family'] = font_name
    try:
        yield
    finally:
        matplotlib.rcParams['font.family'] = old_font
