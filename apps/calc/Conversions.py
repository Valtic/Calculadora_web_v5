def fahrenheit_from_celsius(celsius):
    """ Convert Celsius to Fahrenheit degrees. """
    try:
        fahrenheit= float(celsius) * 9 /5 +32
        fahrenheit = round(fahrenheit, 3) # Round decimal part.
        return str(fahrenheit)
    except ValueError:
        return "invalid Value"

def celsius_from_fahrenheit(fahrenheit):
    """ Convert Fahrenheit to Celsius degrees. """
    try:
        celsius= (float(fahrenheit)-32)* 5 / 9
        celsius = round(celsius, 3) # Round decimal part.
        return str(celsius)
    except ValueError:
        return "invalid Value"
    
def kelvin_from_celsius(celsius):
    """ Convert Celsius to kelvin degrees. """
    try:
        kelvin= float(celsius)+273.15
        kelvin = round(kelvin, 3) # Round decimal part.
        return str(kelvin)
    except ValueError:
        return "invalid Value"
    
def celsius_from_kelvin(kelvin):
    """ Convert Celsius to kelvin degrees. """
    try:
        celsius= float(kelvin)-273.15
        celsius = round(celsius, 3) # Round decimal part.
        return str(celsius)
    except ValueError:
        return "invalid Value"

if __name__=="__main__":
    
    celsius_in = input("Celsius: ")
    print("Farenheit:{0}".format(fahrenheit_from_celsius(celsius_in)))
    print("Kelvin:{0}".format(kelvin_from_celsius(celsius_in)))
    
    fahrenheit_in = input("Fahrenheit: ")
    print("Celsius:{0}".format(celsius_from_fahrenheit(fahrenheit_in)))
    
    
    kelvin_in = input("Kelvin: ")
    print("Celsius:{0}".format(celsius_from_kelvin(kelvin_in)))
    
