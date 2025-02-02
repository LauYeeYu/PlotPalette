"""This module provides functions to pick colours from the palette."""

from .colours import name, main_palette, palette

def pick_colours(num_colour_family: int, num_sub_colours: int, main_colour: str) -> list:
    """Pick colours from the palette.

    Args:
        num_colour_family (int): The number of colour families to pick.
        num_sub_colours (int): The number of sub colours in each colour
                               families to pick.
        main_colour (str): The main colour to pick. You may use the name
                           of colour in the main palette (e.g., silverstone)
                           or the colour (e.g., yellow).


    Returns:
        list: A list of colour families, each of which is a list of colours.

    Example:
        pick_colours(2, 2, 'monza')
        # Output: [['#f46255', '#b32414'], ['#ff9900', '#de6000']]
    """
    if main_colour in name:
        main_colour = name[main_colour]
    elif main_colour not in palette:
        raise ValueError('The main colour is not in the palette.')

    if num_colour_family < 1:
        raise ValueError('The number of colour families to pick must be at least 1.')
    elif num_colour_family > len(main_palette):
        raise ValueError('The number of colour families to pick must be at most the number of main colours.')

    # Handle the colour families
    colour_families = [main_colour]
    for i in main_palette.keys():
        if len(colour_families) >= num_sub_colours:
            break
        if i == main_colour:
            continue
        colour_families.append(i)

    # Pick the colours
    match num_colour_family:
        case 1:
            return [palette[main_colour]]
        case 2:
            return [
                [
                    palette[f'{colour}-bright'],
                    palette[f'{colour}-dark'],
                ] for colour in colour_families
            ]
        case 3:
            return [
                [
                    palette[f'{colour}-light'],
                    palette[f'{colour}-regular'],
                    palette[f'{colour}-darker'],
                ] for colour in colour_families
            ]
        case 4:
            return [
                [
                    palette[f'{colour}-light'],
                    palette[f'{colour}-bright'],
                    palette[f'{colour}-regular'],
                    palette[f'{colour}-darker'],
                ] for colour in colour_families
            ]
        case 5:
            return [
                [
                    palette[f'{colour}-light'],
                    palette[f'{colour}-bright'],
                    palette[f'{colour}-regular'],
                    palette[f'{colour}-dark'],
                    palette[f'{colour}-darker'],
                ] for colour in colour_families
            ]
        case _:
            raise ValueError('The number of colours to pick must be between 1 and 5.')

