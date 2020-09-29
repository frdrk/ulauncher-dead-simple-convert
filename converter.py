# unit name : UI description
dict = { 
    # Weight
    "grams":                "grams (g)",
    "kilos":                "kilos (kg)",
    "metric-tonnes":        "metric tonnes (t)",
    "ounces":               "ounces (oz)",
    "pounds":               "pounds (lb)",
    "short-ton":            "short ton (shton)",
    "long-ton":             "long ton (Lton)",

    # Length
    "inches":               "inches (in)",
    "feet":                 "feet (ft)",
    "yards":                "yards (yd)",
    "miles":                "miles (mi)",
    "millimeters":          "millimeters (mm)",
    "centimeters":          "centimeters (cm)",
    "meters":               "meters (m)",
    "kilometers":           "kilometers (km)",

    # Volume
    "teaspoon-metric":      "teaspoons (tsp - metric)",
    "tablespoon-metric":    "tablespoons (tbsp - metric)",
    "floz-us":              "fluid onces (fl oz - US)",
    "floz-imp":             "fluid ounces (fl oz - Imperial)",
    "cups-us" :             "cups (US)",
    "cups-imp":             "cups (Imperial)",
    "milliliter":           "milliliters (ml)",
    "liter":                "liters",
    "m3":                   "cubic meters (m3)",
    "in3" :                 "cubic inches (in3)",
    "ft3" :                 "cubic feet (ft3)",
    "pint-us" :             "pints (pt - US)",
    "pint-imp":             "pints (pt - Imperial)",
    "quart-us":             "quarts (qt - US)",
    "quart-imp":            "quarts (qt - Imperial)",
    "gallon-us":            "gallons (gal - US)",
    "gallon-imp":           "gallons (gal - Imperial)",
}


# Multiplier : unit name
units = {
    
    ### Weight
    "ounces" : {
        "ounces (oz) is equal to:":     1,
        dict.get("grams"):              28, 
        dict.get("kilos"):              0.02835,
        #dict.get("metric-tonnes"):     0, 
        #dict.get("ounces"):            0,
        dict.get("pounds"):             0.0625, 
        #dict.get("short-ton"):         0, 
        #dict.get("long-ton"):          0,  
    },
    "pounds" : {
        "pounds (lb) is equal to:":     1,
        dict.get("grams"):              453.59,
        dict.get("kilos"):              0.4536,
        dict.get("metric-tonnes"):      0.000454,  
        dict.get("ounces"):             16,
        #dict.get("pounds"):            0, 
        dict.get("short-ton"):          0.0005,
        dict.get("long-ton"):           0.000446,
    },
    "short-ton" : {
        "short ton (shton) is equal to:":   1,
        #dict.get("grams"):             0,
        dict.get("kilos"):              907.2,  
        dict.get("metric-tonnes"):      0.9072, 
        #dict.get("ounces"):            0, 
        dict.get("pounds"):             2000,
        #dict.get("short-ton"):         0,  
        dict.get("long-ton"):           0.892913,
    },
    "long-ton" : {
        "long ton (Lton) is equal to:": 1,
        #dict.get("grams"):             0, 
        dict.get("kilos"):              1016, 
        dict.get("metric-tonnes"):      1.016,  
        #dict.get("ounces"):            0,
        dict.get("pounds"):             2239.859,
        dict.get("short-ton"):          1.119929,
        # dict.get("long-ton"):         0,
    },
    "grams" : {
        "gram (g) is equal to:":        1,
        dict.get("ounces"):             0.035273,
        dict.get("pounds"):             0.002205,
        #dict.get("short-ton"):         0, 
        #dict.get("long-ton"):          0,
        #dict.get("grams"):             0, 
        dict.get("kilos"):              0.001,
        #dict.get("metric-tonnes"):     0,
    },
    "kilos" : {
        "kilogram (kg) is equal to:":   1,
        dict.get("ounces"):             35.27337, 
        dict.get("pounds"):             2.204586,
        dict.get("short-ton"):          0.001102, 
        dict.get("long-ton"):           0.000984,  
        dict.get("grams"):              1000, 
        #dict.get("kilos"):             0,
        dict.get("metric-tonnes"):      0.001, 
    },
    "metric-tonnes" : {
        "metric tonnes (t) is equal to:":  1,
        #dict.get("ounces"):            0,
        dict.get("pounds"):             2204.586,  
        dict.get("short-ton"):          1.102293,
        dict.get("long-ton"):           0.984252,  
        #dict.get("grams"):             0,
        dict.get("kilos"):              1000,
        #dict.get("metric-tonnes"):     0, 
    },
    
    ### Length
    "inches" : {
        "inches (in) is equal to:":     1,
        dict.get("millimeters"):        25.4,
        dict.get("centimeters"):        2.54,
        dict.get("meters"):             0.0254,
        #dict.get("kilometers"):        0,
        #dict.get("inches"):            0,
        dict.get("feet"):               0.083333,
        dict.get("yards"):              0.027778,
        dict.get("miles"):              0.000016,
    },
    "feet" : {
        "feet (ft) is equal to:":       1,
        #dict.get("millimeters"):       0,
        dict.get("centimeters"):        30.48,
        dict.get("meters"):             0.3048,
        dict.get("kilometers"):         0.000305,
        dict.get("inches"):             12,
        #dict.get("feet"):              1,
        dict.get("yards"):              0.333333,
        dict.get("miles"):              0.000189,  
    },
    "yards" : {
        "yards (yd) is equal to:":      1,
        #dict.get("millimeters"):       914.4,
        dict.get("centimeters"):        91.44,
        dict.get("meters"):             0.9144,
        dict.get("kilometers"):         0.000914,
        dict.get("inches"):             36,
        dict.get("feet"):               3,
        #dict.get("yards"):             1,
        dict.get("miles"):              0.000568, 
    },
    "miles" : {
        "miles (mi) is equal to:":      1,
        #dict.get("millimeters"):       0,
        #dict.get("centimeters"):       0,
        dict.get("meters"):             1609.344,
        dict.get("kilometers"):         1.609344,
        dict.get("inches"):             63360,
        dict.get("feet"):               5280,
        dict.get("yards"):              1760,
        #dict.get("miles"):             0,
    },
    "millimeters" : {
        "millimeters (mm) is equal to:":    1,
        dict.get("inches"):             0.03937,
        dict.get("feet"):               0.003281,
        dict.get("yards"):              0.001094,
        #dict.get("miles"):             0,
        #dict.get("millimeters"):       0,
        dict.get("centimeters"):        0.1,
        dict.get("meters"):             0.001,
        dict.get("kilometers"):         0.000001,
    },
    "centimeters" : {
        "centimeters (cm) is equal to:":    1,
        dict.get("inches"):             0.393701,
        dict.get("feet"):               0.032808,
        dict.get("yards"):              0.010936,
        #dict.get("miles"):             0,
        dict.get("millimeters"):        10,
        #dict.get("centimeters"):       1,
        dict.get("meters"):             0.01,
        dict.get("kilometers"):         0.00001,
    },
    "meters" : {
        "meters (m) is equal to:":      1,
        dict.get("inches"):             39.37008,
        dict.get("feet"):               3.28084,
        dict.get("yards"):              1.093613,
        dict.get("miles"):              0.000621,
        dict.get("millimeters"):        1000,
        dict.get("centimeters"):        100,
        #dict.get("meters"):            0,
        dict.get("kilometers"):         0.001,
    },
    "kilometers" : {
        "kilometers (km) is equal to:": 1,           
        dict.get("inches"):             39370.08,
        dict.get("feet"):               3280.84,
        dict.get("yards"):              1093.613,
        dict.get("miles"):              0.621371,
        #ict.get("millimeters"):        0,
        #dict.get("centimeters"):       0,
        dict.get("meters"):             0.0254,
        #dict.get("kilometers"):        0,
    },

    ### Volume 
    "teaspoon-metric" : {
        "teaspoons (tsp - metric) is equal to:":    1,              
        #ict.get("teaspoon-metric"):    0,
        dict.get("tablespoon-metric"):  0.3333,         
        dict.get("floz-us"):            0.1690701135,
        dict.get("floz-imp"):           0.1759753986,
        dict.get("cups-us"):            0.0211337642,
        dict.get("cups-imp"):           0.0175975399,
        dict.get("milliliter"):         5,
        dict.get("liter"):              0.005,
        #dict.get("m3"):                #0.000005, 
        dict.get("in3"):                0.3051187205,
        #dict.get("ft3"):               #0.0001765733,
        dict.get("pint-us"):            0.0105668821,
        dict.get("pint-imp"):           0.0087987699,
        dict.get("quart-us"):           0.005283441,
        dict.get("quart-imp"):          0.004399385,
        dict.get("gallon-us"):          0.0013208603,
        dict.get("gallon-imp"):         0.0010998462,
    },
    "tablespoon-metric" : {
        "tablespoons (tbsp - metric) is equal to:": 1,
        dict.get("teaspoon-metric"):    3,
        #dict.get("tablespoon-metric"): 0,           
        dict.get("floz-us"):            0.5072103405,
        dict.get("floz-imp"):           0.5279261959,
        dict.get("cups-us"):            0.0634012926,
        dict.get("cups-imp"):           0.0527926196,
        dict.get("milliliter"):         15,
        dict.get("liter"):              0.015,
        #dict.get("m3"):                0,
        dict.get("in3"):                0.9153561614,
        dict.get("ft3"):                0.00052972,
        dict.get("pint-us"):            0.0317006463,
        dict.get("pint-imp"):           0.0263963098,
        dict.get("quart-us"):           0.0158503231,
        dict.get("quart-imp"):          0.0131981549,
        dict.get("gallon-us"):          0.0039625808,
        dict.get("gallon-imp"):         0.0032995387,
    },
    "floz-us" : {
        "fluid ounces (fl oz - US) is equal to:":   1,              
        dict.get("teaspoon-metric"):    5.9147059125,
        dict.get("tablespoon-metric"):  1.9715686375,
        #dict.get("floz-us"):           0, 
        dict.get("floz-imp"):           1.0408427308, 
        dict.get("cups-us"):            0.125,
        dict.get("cups-imp"):           0.1040842731,
        dict.get("milliliter"):         29.573529562,
        dict.get("liter"):              0.0295735296,
        #dict.get("m3"):                0,
        dict.get("in3"):                1.8046875,
        dict.get("ft3"):                0.0010443793,
        dict.get("pint-us"):            0.0625,
        dict.get("pint-imp"):           0.0520421365,
        dict.get("quart-us"):           0.03125,
        dict.get("quart-imp"):          0.0260210683,
        dict.get("gallon-us"):          0.0078125,
        dict.get("gallon-imp"):         0.0065052671,
    },
    "floz-imp" : {
        "fluid ounces (fl oz - Imperial) is equal to:": 1,              
        dict.get("teaspoon-metric"):    5.6826125,     
        dict.get("tablespoon-metric"):  1.8942041667,  
        dict.get("floz-us"):            0.9607599404,   
        #dict.get("floz-imp"):          0:               
        dict.get("cups-us"):            0.1200949926,
        dict.get("cups-imp"):           0.1,           
        dict.get("milliliter"):         28.4130625,    
        dict.get("liter"):              0.0284130625, 
        #dict.get("m3"):                0,              
        dict.get("in3"):                1.7338714549,   
        dict.get("ft3"):                0.0010033978,  
        dict.get("pint-us"):            0.0600474963,    
        dict.get("pint-imp"):           0.05,           
        dict.get("quart-us"):           0.0300237481,
        dict.get("quart-imp"):          0.025,        
        dict.get("gallon-us"):          0.007505937,    
        dict.get("gallon-imp"):         0.00625,        
    },
    "cups-us" : {
        "cups (US) is equal to:":       1,
        dict.get("teaspoon-metric"):    47.3176473,
        dict.get("tablespoon-metric"):  15.7725491,
        dict.get("floz-us"):            8,
        dict.get("floz-imp"):           8.3267418463,
        #dict.get("cups-us"):           0,
        dict.get("cups-imp"):           0.8326741846,
        dict.get("milliliter"):         28.4130625,
        dict.get("liter"):              0.2365882365,
        #dict.get("m3"):                0,
        dict.get("in3"):                14.4375,
        dict.get("ft3"):                0.0083550347,
        dict.get("pint-us"):            0.5,
        dict.get("pint-imp"):           0.4163370923,
        dict.get("quart-us"):           0.25,
        dict.get("quart-imp"):          0.2081685462,
        dict.get("gallon-us"):          0.0625,
        dict.get("gallon-imp"):         0.0520421365,
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
        try:
            for key, value in units[fromUnit].items():
                convertedValue = quantity * value
                
                # Control decimals
                if convertedValue > 0.1: 
                    convertedValue = round(convertedValue, 2)

                elif convertedValue > 0.01:
                    convertedValue = round(convertedValue, 3)

                elif convertedValue > 0.001:
                    convertedValue = round(convertedValue, 4)

                elif convertedValue > 0.0001:
                    convertedValue = round(convertedValue, 5)    
                
                items.append(format(convertedValue,'n') + ' ' + key)

        except:
            print("Houston.. etc")

    return items