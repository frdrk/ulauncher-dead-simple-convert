# Input match : unit match
convertableUnits = {
    "c":            "celcius",
    "celcius":      "celcius",
    "f":            "fahrenheit",
    "fahrenheit":   "fahrenheit",
    "k":            "kelvin",
    "kelvin":       "kelvin",

    "cup":          "cups",
    "cups":         "cups",
    
    "lb":           "pounds",
    "pound":        "pounds",
    "pounds":       "pounds",
    "oz":           "ounces",
    "ounce":        "ounces",
    "shton":        "short-ton",
    "short ton":    "short-ton", 
    "lhton":        "long-ton",
    "long ton":     "long-ton", 
    "g":            "grams",
    "gram":         "grams", 
    "grams":        "grams", 
    "kg":           "kilos",
    "kilo":         "kilos", 
    "kilos":        "kilos",  
    "kilogram":     "kilos",
    "tonne":        "metric-tonnes", 
    "tonnes":       "metric-tonnes",  
    "metric tonnes":"metric-tonnes",
 

    "in":           "inches",
    "inch":         "inches",
    "inches":       "inches",
    "ft":           "feet",
    "foot":         "feet",
    "feet":         "feet",
    "yd":           "yards",
    "yard":         "yards",
    "yards":        "yards",
    "mi":           "miles",
    "mile":         "miles",
    "miles":        "miles",
    "mm":           "millimeters",
    "millimeter":   "millimeters",
    "millimeters":  "millimeters",
    "cm":           "centimeters",
    "centimeter":   "centimeters",
    "centimeters":  "centimeters",
    "m":            "meters",
    "meter":        "meters",
    "meters":       "meters",
    "km":           "kilometers",
    "kilometer":    "kilometers",
    "kilometers":   "kilometers",
}

def parse_units(input_unit):
    if input_unit in convertableUnits:
        return convertableUnits.get(input_unit)
    else:
        return False