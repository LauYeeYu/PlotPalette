# PlotPalette

PlotPalette is a Python package that simplifies the process of creating colour
palettes for plots. It provides a combination of colours for plots, and a
colour picker to help select the colours.

## Colour Palette

### Main Colours
![Main Palettes](assets/main_palette.png)

### All Colours

![Colour Palettes](assets/all_palette.png)

## Installation

### Prerequisites

To install PlotPalette, you need to install python build tools. On Ubuntu,
you can do this by running:

```bash
pip3 install build installer wheel
```

On arch-based systems, you can do this by running:

```bash
sudo pacman -S python-build python-installer python-wheel --needed
```

### Build and Install

Then you can install PlotPalette using pip:

```bash
python -m build --wheel --no-isolation
sudo python -m installer dist/*.whl
```

## Features

- **Colour Palettes**: PlotPalette provides a set of colour palettes that can
  be used in plots, which is given in [colours.py](plotpalette/colours.py).
  You may use the colours in that file directly, or use the colour picker to
  select the colours.
- **Colour Picker**: PlotPalette provides colour picking tools for selecting
  colours for plots. You can use the colour picker to select colours for your
  plots, and then use the colours in your plots.
- **Simpler Plotting** (in progress).
- **Customized Fonts** (in progress).

## License

MIT License

Copyright (c) 2024-2025 Yiyu Liu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
