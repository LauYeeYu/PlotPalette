"""Make a plot of all the colours in the palette."""

import plotpalette

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def main():
    # Create a list of all the main colours
    names = list(plotpalette.palette.keys())
    x_pos = range(len(names))
    colours = list(plotpalette.palette.values())
    height = [1] * len(names)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(15,5))
    ax.bar(x_pos, height, color=colours, hatch='', edgecolor='white')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(names, rotation=45, ha='right')
    ax.set_yticks([])

    # Show the plot
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    with plotpalette.use_preset('acmart'):
        main()
