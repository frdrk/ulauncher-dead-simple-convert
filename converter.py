# Multiplier : unit name
units = {
    "cups" : {
        1:          "cups is equal to:",
        0.2366:     "liter",
        23.66:      "centiliter",
        0.5:        "pints",
        8:          "fluid ounces",
        16:         "tablespoons",
        48:         "teaspoons"
    },
    "pounds" : {
        1:          "pounds (lb) is equal to:",
        0.45:       "kilo",
        453.59:     "gram",
        16:         "ounces"
    },
    "inches" : {
        1:           "inches (in) is equal to:",
        25.4:        "millimeters",
        2.54:        "centimeters",
        0.0254:      "meters",
        #:           "kilometers",
        #1:          "inches",
        0.083333:    "feet",
        0.027778:    "yards",
        0.000016:    "miles",  
    },
    "feet" : {
        1:           "feet (ft) is equal to:",
        #:           "millimeters",
        30.48:       "centimeters",
        0.3048:      "meters",
        0.000305:    "kilometers",
        12:          "inches",
        #1:          "feet",
        0.333333:    "yards",
        0.000189:    "miles",  
    },
    "yards" : {
        1:           "yards (yd) is equal to:",
        #914.4:      "millimeters",
        91.44:       "centimeters",
        0.9144:      "meters",
        0.000914:    "kilometers",
        36:          "inches",
        3:           "feet",
        #1:          "yards",
        0.000568:    "miles",  
    },
    "miles" : {
        1:           "miles (mi) is equal to:",
        #:           "millimeters",
        #:           "centimeters",
        1609.344:    "meters",
        1.609344:    "kilometers",
        63360:       "inches",
        5280:        "feet",
        1760:        "yards",
        #1:          "miles",  
    },
    "millimeters" : {
        1:           "millimeters (mm) is equal to:",
        0.03937:     "inches",
        0.003281:    "feet",
        0.001094:    "yards",
        #1:          "miles", 
        #:           "millimeters",
        0.1:         "centimeters",
        0.001:       "meters",
        0.000001:    "kilometers",
    },
    "centimeters" : {
        1:           "centimeters (cm) is equal to:",
        0.393701:     "inches",
        0.032808:    "feet",
        0.010936:    "yards",
        #1:          "miles", 
        10:           "millimeters",
        #1:         "centimeters",
        0.01:       "meters",
        0.00001:    "kilometers",
    },
    "meters" : {
        1:           "meters (m) is equal to:",
        39.37008:    "inches",
        3.28084:     "feet",
        1.093613:    "yards",
        0.000621:    "miles", 
        1000:        "millimeters",
        100:         "centimeters",
        #:           "meters",
        0.001:       "kilometers",
    },
    "kilometers" : {
        1:           "kilometers (km) is equal to:",
        39370.08:    "inches",
        3280.84:     "feet",
        1093.613:    "yards",
        0.621371:    "miles", 
        #:           "millimeters",
        #:           "centimeters",
        0.0254:      "meters",
        #:           "kilometers",
    },

    
}   

def convert_from_unit(fromUnit, quantity):
    
    items = []

    if fromUnit == "fahrenheit":
        celcius = (quantity - 32) * (5 / 9)
        kelvin = (quantity + 459.67) * (5 / 9)

        items.append(format(quantity,'.2f').rstrip('0').rstrip('.') + ' degrees Fahrenheit (F) is equal to:')
        items.append(format(celcius,'.2f').rstrip('0').rstrip('.') + ' Celcius')
        items.append(format(kelvin,'.2f').rstrip('0').rstrip('.') + ' Kelvin')
    
    elif fromUnit == "celcius":
        farenheit = (quantity * (9 / 5) + 32)
        kelvin = (quantity + 273.15)

        items.append(format(quantity,'.2f').rstrip('0').rstrip('.') + ' degrees Celcius (C) is equal to:')
        items.append(format(farenheit,'.2f').rstrip('0').rstrip('.') + ' Farenheit')
        items.append(format(kelvin,'.2f').rstrip('0').rstrip('.') + ' Kelvin')

    elif fromUnit == "kelvin":
        celcius = (quantity - 273.15)
        fahrenheit = (quantity * (9 / 5) - 459.67)

        items.append(format(quantity,'.2f').rstrip('0').rstrip('.') + ' degrees Kelvin (K) is equal to:')
        items.append(format(celcius,'.2f').rstrip('0').rstrip('.') + ' Celcius')
        items.append(format(fahrenheit,'.2f').rstrip('0').rstrip('.') + ' Fahrenheit')

    else:
        for key in units[fromUnit]:
            items.append(format((quantity * key),'n') + ' ' + units[fromUnit][key])

    return items