# Colors

The `cmap.Color` type is used to represent an individual color.

## ColorLike

A variety of objects can be interpreted as a color, `cmap` refers
to these objects collectively as `ColorLike`.

The following objects can be interpreted as a color:

1. A string containing a color name. All CSS color names are supported, case is
   ignored along with spaces, underscores and dashes  (see complete list below.)

    - `'red'`
    - `'slategray'`

1. A string containing a 3, 6, or 8-digit [hexadecimal color
   code](https://w3c.github.io/csswg-drafts/css-color/#hex-notation):

    - `'#0F5'`     (RGB)
    - `'#00FF55'`   (RRGGBB)
    - `'#00FF55FF'`  (RRGGBBAA)

1. A string containing a valid css
   [`rgb(a)`](https://w3c.github.io/csswg-drafts/css-color/#rgb-functions) or
   [`hsl(a)`](https://w3c.github.io/csswg-drafts/css-color/#the-hsl-notation)
   color:
    - `'rgb(255, 0, 0)'`
    - `'rgb(100%, 0%, 0%)'`
    - `'rgba(255, 0, 0, 0.5)'`
    - `'rgba(255, 0, 0)'`  (it's ok to use `rgba` without an alpha value)
    - `'rgba(100%, 0%, 0%, 0.5)'`
    - `'hsl(180, 100%, 50%)'`
    - `'hsla(180, 100%, 50%, 0.5)'`
    - `'hsla(180, 100%, 50%)'` (it's ok to use `hsla` without an alpha value)

1. A `tuple` containing 3 `int` values between 0-255 (for RGB), or 3 int values and a `float` alpha value from 0-1 (for RGBA). (Note: the alpha value is *always* a float between 0-1).
    - `(0, 128, 255)`
    - `(0, 128, 255, 0.5)`

1. A `tuple` containing 3 or 4 `float` values (see note on ambiguity below):
    - `(0.0, 0.5, 1.0)`
    - `(0.0, 0.5, 1.0, 0.5)`

!!! note
    In all cases, numeric values are clipped to their valid range, so `(0, 300,
    0, 2.0)` is equivalent to `(0, 255, 0, 1.0)`, and `(0.0, 1.5, 0.0, -0.5)` is
    equivalent to `(0.0, 1.0, 0.0, 0)`.

!!!warning "Ambiguities"

    While it's nice to support both the 8-bit and float inputs, there is amgiguity in the case of a tuple of integers containing only zeros and ones (e.g. `(0, 0, 1)`).  The convention in `cmap` is to treat a tuple of *all* integers as 8-bit RGB values, and a tuple with *any* floats as float RGB values, so 
    
    - `(0, 0, 1) == (0, 0, 1/255) == '#000001'`
    - `(0, 0, 1.) == (0, 0, 255) == '#0000FF'`

    To avoid ambiguity, it's best to always prefer float values.

## Recognized Color Names

{{ COLOR_LIST }}
