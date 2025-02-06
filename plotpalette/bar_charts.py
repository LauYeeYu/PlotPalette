"""Draw bar charts easily."""

__all__ = ['bar_chart']

from .colour_picker import pick_main_colours
from .colours import main_palette

import matplotlib.pyplot as plt


def bar_chart(
        bar_names: list[str],
        data: dict[str, float],
        title: str | None = None,
        colours: list[str] | list[list[str]] | None = None,
        size: tuple[int, int] = (10, 5),
        hatch: list[str] | None = None,
        edgecolor: str = 'black',
        bar_margin: int | None = None,
        value_limit: int | None = None,
        horizontal: bool = False,
        show_values: bool | list = False,
        show_bar_names: bool = False,
) -> None:
    """Draw a bar chart.

    Args:
        bar_names (alist[str]): The names of the bars.
        data (dict[str, float]): The data of the bars.
        title (str | None): The title of the bar chart. By default, it is None,
            which means no title.
        colours (list[str] | list[list[str]] | None): The colours of the bars.
            If the argument is a list of list, it will be converted to a list.
            If the argument is None, the function will pick the main colours
            from the palette. By default, it is None.
        size (tuple[int, int]): The size of the figure. By default, it is (10, 5).


    """
    num_bars = len(bar_names)
    # Handle all colours
    if colours is None:
        if 1 <= num_bars <= len(main_palette):
            colours = pick_main_colours(num_bars)
        else:
            raise ValueError('The number of bars must be between 1 and the '
                             'number of main colours.')
    elif len(colours) == 0:
        raise ValueError('The number of colours must be at least 1.')
    elif isinstance(colours[0], list):
        original_colours = colours
        colours = [colour for colour_family in original_colours
                   for colour in colour_family]

    # Set defaults
    if hatch is None: hatch = [''] * num_bars
    if bar_margin is None: bar_margin = 0.1

    # Check all bars are in the data
    if not all(bar in data for bar in bar_names):
        raise ValueError('Some bars are not in the data.')

    # Check the length
    def check_length(lst, name):
        if len(lst) != len(bar_names):
            raise ValueError(f'The number of {name} must be equal to the number '
                             'of bars.')
    check_length(colours, 'colours')
    #TODO: check hatch and show_values
