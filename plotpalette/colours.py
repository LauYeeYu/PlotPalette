
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

If pick 4 colours, the darker one will be omitted.
If pick 3 colours, the medium and darker ones will be omitted.
If pick 2 colours, the regular and dark ones will be taken.

Therefore, the light, regular and dark will be more important.
"""
palette_darkness = {
    'light': 0,
    'regular': 1,
    'medium': 2,
    'dark': 3,
    'darker': 4,
}

palette = main_palette | {
    # Monza (Red)
    'monza-light': '#ec5649',
    'monza-regular': '#e13f2d',
    'monza-medium': '#cf3527',
    'monza-dark': '#b32414',  # 'monza' colour
    'monza-darker': '#8e2207',

    # Zandvoort (Orange)
    'zandvoort-light': '#ff7a14',
    'zandvoort-regular': '#f48217',
    'zandvoort-medium': '#eb7317',
    'zandvoort-dark': '#de6000',  # 'zandvoort' colour
    'zandvoort-darker': '#d44601',

    # Silverstone (Yellow)
    'silverstone-light': '#faf377',
    'silverstone-regular': '#f9ed48',
    'silverstone-medium': '#f1d126',
    'silverstone-dark': '#e4c315',  # 'silverstone' colour
    'silverstone-darker': '#c5a400',
}
