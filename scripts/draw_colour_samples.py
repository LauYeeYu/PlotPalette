"""Draw all figures for the colour samples."""

import plotpalette

import matplotlib.pyplot as plt

palette_darkness = ['light', 'bright', 'regular', 'dark', 'darker']

def draw_main_palette():
    """Draw the main palette."""
    # Create a list of all the main colours
    names = [name.capitalize() for name in plotpalette.main_palette.keys()]
    num = (len(names) + 1) // 2
    names_1 = names[:num]
    names_2 = names[num:]
    y_pos = range(num)
    colours = list(plotpalette.main_palette.values())
    colours_1 = colours[:num]
    colours_2 = colours[num:]
    height = [1] * num
    offset = [1.1] * num
    width = 0.8

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10,5))
    bar_1 = ax.barh(y_pos, height, width, color=colours_1, hatch='')
    bar_2 = ax.barh(y_pos, height, width, offset, color=colours_2, hatch='')
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlim(-0.05, 2.15)
    ax.set_ylim(-0.5, num - 0.5)
    ax.axis('off')

    # Add the names
    def add_names(bar, names, colours, offset):
        for i, bar in enumerate(bar):
            ax.text(offset, bar.get_y() + bar.get_height() / 2,
                    f'{names[i]} ({colours[i]})',
                    ha='center', va='center', color='white',
                    fontsize=18, fontweight='bold')
    add_names(bar_1, names_1, colours_1, 0.5)
    add_names(bar_2, names_2, colours_2, 1.6)

    # Show the plot
    plt.tight_layout()
    plt.savefig('assets/main_palette.png', dpi=300)


def draw_all_palette():
    """Draw all the palettes."""
    # Create a list of all the main colours
    names = list(plotpalette.main_palette.keys())
    names_cap = [name.capitalize() for name in names]
    y_pos = range(len(names))
    colours = list(plotpalette.main_palette.values())
    height = 1
    width = 0.8

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10,10))

    def draw_one_colour(name, y_pos):
        for i, darkness in enumerate(palette_darkness):
            ax.barh(y_pos, height, width, i,
                    color=plotpalette.palette[f'{name}-{darkness}'], hatch='')
    for i, name in enumerate(names):
        draw_one_colour(name, -i)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names)
    ax.set_xticks([])
    ax.axis('off')
    ax.set_xlim(-0.05, 5.15)
    ax.set_ylim(-len(names) + 0.3, 0.8)

    # Add the names
    for i, name in enumerate(names_cap):
        ax.text(-0.6, -i, name, ha='center', va='center', color='black',
                fontsize=18, fontweight='bold')
    for i, darkness in enumerate(palette_darkness):
        ax.text(i + 0.5, 0.6, darkness.capitalize(), ha='center', va='center',
                color='black', fontsize=18, fontweight='bold')

    # Show the plot
    plt.tight_layout()
    plt.savefig('assets/all_palette.png', dpi=300)


if __name__ == '__main__':
    draw_main_palette()
    draw_all_palette()
