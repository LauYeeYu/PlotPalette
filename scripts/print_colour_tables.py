"""Print the main colours and all colours in tables with Markdown format."""

import plotpalette

palette_darkness = ['light', 'bright', 'regular', 'dark', 'darker']

def print_main_colours():
    """Print the main colours in tables."""
    print('Main colours:')
    print('| Colour | Name | Value |')
    print('|:------:|:----:|:-----:|')
    for colour, name in plotpalette.name.items():
        print(f'| {colour.capitalize()} | {name.capitalize()} | {plotpalette.main_palette[name]} |')
    print()


def print_all_colours():
    """Print all the colours in tables."""
    print('All colours:')
    print('| Colour | Name | Light | Bright | Regular | Dark | Darker |')
    print('|:------:|:----:|:-----:|:------:|:-------:|:----:|:------:|')
    for colour, name in plotpalette.name.items():
        print(f'| {colour.capitalize()} | {name.capitalize()} |', end=' ')
        for darkness in palette_darkness:
            print(plotpalette.palette[f'{name}-{darkness}'], end=' | ')
        print()


if __name__ == '__main__':
    print_main_colours()
    print_all_colours()
