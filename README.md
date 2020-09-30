# ulauncher-dead-simple-convert
Offline unit converter extension for [Ulauncher](https://ulauncher.io/). Bringing a little bit of [Spotlight's](https://en.wikipedia.org/wiki/Spotlight_(software)) conversion simplicity to Linux.

![Dead Simple Convert Screenshot](docs/dsc-screenshot.png)

## Install
1. In ulauncher preferences window » extensions » add extension and paste the following url: `https://github.com/frdrk/ulauncher-dead-simple-convert`
2. Set you preferred keyword or use the default 'c'.


## Usage
In Ulauncher simply type in whatever you would like to convert from and all available conversion units will be calculated and displayed. No need to specify what you want to converty to. Use format:  
`[keyword] [number] [unit]`

#### Examples
- `c 1 cup`
- `c 16.5 inches`
- `c 68 F`
- `c 12,5 miles`
- `c .5 m2`


## Available units
See [convertable_units.py](https://github.com/frdrk/ulauncher-dead-simple-convert/blob/master/convertable_units.py) for all available units and their variants.

## Known limitations
- No support for fractions. So can't convert for example '5/16 inches'. 
- No support for double unit conversions. For example '3 ft 6 in'