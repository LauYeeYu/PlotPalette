"""Presets for plotpalette."""

__all__ = ['preset_font', 'use_preset']

import matplotlib
import contextlib

preset_font = {
    'usenix': 'Times New Roman',
    'acmart': 'Linux Libertine',
}


@contextlib.contextmanager
def use_preset(preset: str) -> None:
    """Use a preset.

    The font will be set to the font of the preset.

    Args:
        preset (str): The name of the preset to use.

    Example:
        with plotpalette.use_preset('usenix'):
            ...  # Your code here
    """
    if preset not in preset_font:
        raise ValueError(f'Preset {preset} is not available.')
    old_font = matplotlib.rcParams['font.family']
    matplotlib.rcParams['font.family'] = preset_font[preset]
    try:
        yield
    finally:
        matplotlib.rcParams['font.family'] = old_font
