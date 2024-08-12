# Temperature-Converter


temperature = int(input("please enter the temperature : "))

conversion_unit = int(
    input(
        "please specify the unit you want to convert: 1 . Celsius to Fahrenheit , 2 . Fahrenheit to Celsius, 3. Celsius to Kelvin , 4. Kelvin to Celsius, 5. Fahrenheit to Kelvin, 6. Kelvin to Fahrenheit : "
    )
)


def Temp_convert(temp, unit):
    try:

        if unit == 1:

            Fahrenheit = (temp * 9 / 5) + 32

            return f"the temp conversion from  Celsius to fahrenheit is  {Fahrenheit}F"

        elif unit == 2:

            Celsius = (temp - 32) * 5 / 9

            return f"the temp conversion from fahrenheit to Celsius  is  {Celsius}c"

        elif unit == 3:

            Kelvin = temp + 273.15

            return f"the temp conversion from Celsius to Kelvin is  {Kelvin}k"

        elif unit == 4:

            Celsius = temp - 273.15

            return f"the temp conversion from Kelvin to  Celsius is  {Celsius}c"

        elif unit == 5:

            Kelvin = (temp - 32) * 5 / 9 + 273.15

            return f"the temp conversion from fahrenheit to Kelvin  is  {Kelvin}k"

        elif unit == 6:

            Fahrenheit = (temp - 273.15) * 9 / 5 + 32

            return f"the temp conversion from Kelvin to fahrenheit is  {Fahrenheit}k"

        else:
            print("please enter a valid value ")

    except ValueError:
        print("please enter proper value for temperature conversion")


output = Temp_convert(temperature, conversion_unit)


print(output)
