"""This module contains the colour palette for the plots.

Specifically, this file provides three dictionaries:
- `name`: The mapping from colour to the name of colour family.
- `main_palette`: The main colours in the palette.
- `palette`: The full palette of colours.
"""

name = {
    'red':    'monza',        # Scuderia Ferrari
    'orange': 'zandvoort',    # House of Orange-Nassau
    'yellow': 'silverstone',  # Get in there Lewis!
    'green':  'spa',          # Green circuit with a lot of trees
    'cyan':   'miami',        # Miami Dolphins
    'blue':   'shanghai',     # Sea and sky
    'purple': 'seattle',      # Go Huskies!
    'brown':  'sakhir',       # Desert sand
}

main_palette = {
    'monza': '#b32414',        # Red
    'zandvoort': '#de6000',    # Orange
    'silverstone': '#e4c315',  # Yellow
    'spa': '#2d7830',          # Green
    'miami': '#00c5c1',        # Cyan
    'shanghai': '#4f89c4',     # Blue
    'seattle': '#5b408e',      # Purple
    'sakhir': '#580e0e',       # Brown
}


"""The palette darkness is used to create a gradient of colours.

Depending on the number of colours picked:
If pick 1 colour, we will take the colour in the main palette.
If pick 2 colours, we will take bright and dark.
If pick 3 colours, we will take light, regular and darker.
If pick 4 colours, we will take light, bright, regular and darker.

Therefore, the light, regular and dark will be more important.
"""
palette_darkness = {
    'light': 0,
    'bright': 1,
    'regular': 2,
    'dark': 3,
    'darker': 4,
}

palette = main_palette | {
    # Monza (Red)
    'monza-light': '#ff8c82',
    'monza-bright': '#f46255',
    'monza-regular': '#e13f2d',
    'monza-dark': '#b32414',  # 'monza' colour
    'monza-darker': '#8e2207',

    # Zandvoort (Orange)
    'zandvoort-light': '#ffb949',
    'zandvoort-bright': '#ff9900',
    'zandvoort-regular': '#ff7a14',
    'zandvoort-dark': '#de6000',  # 'zandvoort' colour
    'zandvoort-darker': '#d44601',

    # Silverstone (Yellow)
    'silverstone-light': '#faf377',
    'silverstone-bright': '#f9ed48',
    'silverstone-regular': '#f1d126',
    'silverstone-dark': '#e4c315',  # 'silverstone' colour
    'silverstone-darker': '#c5a400',

    # Spa (Green)
    'spa-light': '#8ae68a',
    'spa-bright': '#42ce42',
    'spa-regular': '#429b44',
    'spa-dark': '#2d7830',  # 'spa' colour
    'spa-darker': '#1b591e',

    # Miami (Cyan)
    'miami-light': '#ace6e5',
    'miami-bright': '#0de8e8',
    'miami-regular': '#00c5c1',  # 'miami' colour
    'miami-dark': '#009b92',
    'miami-darker': '#007a70',

    # Shanghai (Blue)
    'shanghai-light': '#add6ff',
    'shanghai-bright': '#69abee',
    'shanghai-regular': '#4f89c4',  # 'shanghai' colour
    'shanghai-dark': '#2c659e',
    'shanghai-darker': '#1b3a5f',

    # Seattle (Purple)
    'seattle-light': '#c2b1e1',
    'seattle-bright': '#8d7bc5',
    'seattle-regular': '#6b5ebd',
    'seattle-dark': '#5b408e',  # 'seattle' colour
    'seattle-darker': '#311a6e',

    # Sakhir (Brown)
    'sakhir-light': '#be9696',
    'sakhir-bright': '#ad5d44',
    'sakhir-regular': '#893924',
    'sakhir-dark': '#580e0e',  # 'sakhir' colour
    'sakhir-darker': '#420404',
}
