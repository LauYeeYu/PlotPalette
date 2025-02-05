"""Pick the colours."""

import plotpalette

import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Create a list of all the main colours
    picked_colours = plotpalette.pick_colours(2, 3, 'monza')
    colours = [colour for colour_family in picked_colours for colour in colour_family]
    names = [str(i) for i in range(len(colours))]
    print(colours)
    x_pos = range(len(names))
    height = [1] * len(names)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(15,5))
    ax.bar(x_pos, height, color=colours, hatch='', edgecolor='white')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(names)
    ax.set_yticks([])

    # Show the plot
    plt.tight_layout()
    plt.show()

