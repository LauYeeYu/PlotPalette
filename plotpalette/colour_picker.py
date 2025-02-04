"""This module provides functions to pick colours from the palette."""

__all__ = ['pick_colours_in_one_family', 'pick_colours']

from .colours import name, main_palette, palette

def pick_colours_in_one_family(
        num_sub_colours: int,
        main_colour: str,
) -> list[str]:
    """ Pick colours in one family.

    Args:
        num_sub_colours (int): The number of sub colours to pick.
        main_colour (str): The main colour to pick. You may use the name
                           of colour in the main palette (e.g., silverstone)
                           or the colour (e.g., yellow).

    Returns:
        list: A list of colours.
    """
    match num_sub_colours:
        case 1:
            return [palette[main_colour]]
        case 2:
            return [
                palette[f'{main_colour}-bright'],
                palette[f'{main_colour}-dark'],
                ]
        case 3:
            return [
                palette[f'{main_colour}-light'],
                palette[f'{main_colour}-regular'],
                palette[f'{main_colour}-darker'],
            ]
        case 4:
            return [
                palette[f'{main_colour}-light'],
                palette[f'{main_colour}-bright'],
                palette[f'{main_colour}-regular'],
                palette[f'{main_colour}-darker'],
            ]
        case 5:
            return [
                palette[f'{main_colour}-light'],
                palette[f'{main_colour}-bright'],
                palette[f'{main_colour}-regular'],
                palette[f'{main_colour}-dark'],
                palette[f'{main_colour}-darker'],
            ]
        case _:
            raise ValueError('The number of colours to pick must be between '
                             '1 and 5.')


def pick_colours(
        num_colour_family: int,
        num_sub_colours: int | list[int],
        main_colour: str,
) -> list[list[str]]:
    """Pick colours from the palette.

    Args:
        num_colour_family (int): The number of colour families to pick.
        num_sub_colours (int | list[int]): The number of sub colours in each
                                           colour families to pick.
        main_colour (str): The main colour to pick. You may use the name
                           of colour in the main palette (e.g., silverstone)
                           or the colour (e.g., yellow).


    Returns:
        list: A list of colour families, each of which is a list of colours.

    Example:
        pick_colours(2, 2, 'monza')

        Output: [['#f46255', '#b32414'], ['#ff9900', '#de6000']]
    """
    if main_colour in name:
        main_colour = name[main_colour]
    elif main_colour not in palette:
        raise ValueError('The main colour is not in the palette.')

    if num_colour_family < 1:
        raise ValueError('The number of colour families to pick must be at '
                         'least 1.')
    elif num_colour_family > len(main_palette):
        raise ValueError('The number of colour families to pick must be at '
                         'most the number of main colours.')

    # Handle the colour families
    colour_families = [main_colour]
    for i in main_palette.keys():
        if len(colour_families) >= num_colour_family:
            break
        if i == main_colour:
            continue
        colour_families.append(i)

    if isinstance(num_sub_colours, int):
        return [pick_colours_in_one_family(num_sub_colours, colour)
                for colour in colour_families]
    elif isinstance(num_sub_colours, list):
        return [pick_colours_in_one_family(num_sub_colours[i], colour)
                for i, colour in enumerate(colour_families)]
    else:
        raise ValueError('The number of sub colours must be an integer or a '
                         'list of integers.')

