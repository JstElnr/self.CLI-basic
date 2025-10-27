def celcius_to_fahrenheit(celcius):
    return (celcius*9/5)+32

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit-32)*5/9

def celcius_to_kelvin(celcius):
    return celcius+273.15

def kelvin_to_celcius(kelvin):
    return kelvin-273.15

def fahrenheit_to_kelvin(fahrenheit):
    celcius=fahrenheit_to_celcius(fahrenheit)
    return celcius_to_kelvin(celcius)

def kelvin_to_fahrenheit(kelvin):
    celcius=kelvin_to_celcius(kelvin)
    return celcius_to_kelvin(celcius)

def celcius_to_rankine(celcius):
    return (celcius+273.15)*1.8

def rankine_to_celcius(celcius):
    return (celcius-491.67)/1.8

def rankine_to_fahrenheit(rankine):
    return rankine-459.67

def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit+459.67

def rankine_to_kelvin(rankine):
    return rankine/1.8

def kelvin_to_rankine(kelvin):
    return kelvin*1.8

def reaumur_to_celcius(reaumur):
    return reaumur/0.8

def celcius_to_reaumur(celcius):
    return celcius*0.8

def reaumur_to_fahrenheit(reaumur):
    celcius=reaumur_to_celcius(reaumur)
    return celcius_to_fahrenheit(celcius)

def fahrenheit_to_reaumur(fahrenheit):
    celcius=fahrenheit_to_celcius(fahrenheit)
    return celcius_to_reaumur(celcius)

def reaumur_to_kelvin(reaumur):
    celcius=reaumur_to_celcius(reaumur)
    return celcius_to_kelvin(celcius)

def kelvin_to_reaumur(kelvin):
    celcius=kelvin_to_celcius(kelvin)
    return celcius_to_reaumur(celcius)

def reaumur_to_rankine(reaumur):
    celcius=reaumur_to_celcius(reaumur)
    return celcius_to_rankine(celcius)

def rankine_to_reaumur(rankine):
    celcius=rankine_to_celcius(rankine)
    return celcius_to_reaumur(celcius)

def main():
    print("Temperature converter")
    print("Options: ")
    print("1.Celcius to Fahrenheit")
    print("2.Fahrenheit to Celcius")
    print("3.Celcius to Kelvin")
    print("4.Kelvin to Celcius")
    print("5.Fahrenheit to Kelvin")
    print("6.Kelvin to Fahrenheit")
    print("7.Celcius to Rankine")
    print("8.Rankine to Celcius")
    print("9.Rankine to Fahrenheit")
    print("10.Fahrenheit to Rankine")
    print("11.Rankine to Kelvin")
    print("12.Kelvin to Rankine")
    print("13.Reaumur to Celcius")
    print("14.Celcius to Reaumur")
    print("15.Reaumur to Fahrenheit")
    print("16.Fahrenheit to Reaumur")
    print("17.Reaumur to Kelvin")
    print("18.Kelvin to Reaumur")
    print("19.Reaumur to Rankine")
    print("20.Rankine to Reaumur")

    print("0.Quite")

    while True:

        choice=input("Enter your choice: ")

        if choice=='0':
            print("Closing the program...")
            break
        try:
            value=float(input("Enter the temperature value: "))
        except ValueError:
            print("Wrong temperature value. Enter a number.")
            continue

        if choice=='1':
            result=celcius_to_fahrenheit(value)
            print(f"{value}C is {result:.2f}F")

        elif choice=='2':
            result=fahrenheit_to_celcius(value)
            print(f"{value}F is {result:.2f}C")

        elif choice=='3':
            result=celcius_to_kelvin(value)
            print(f"{value}C is {result:.2f}K")

        elif choice=='4':
            result=kelvin_to_celcius(value)
            print(f"{value}K is {result:.2f}C")

        elif choice=='5':
            result=fahrenheit_to_kelvin(value)
            print(f"{value}F is {result:.2f}K")

        elif choice=='6':
            result=kelvin_to_fahrenheit(value)
            print(f"{value}K is {result:.2f}F")

        elif choice=='7':
            result=celcius_to_rankine(value)
            print(f"{value}C is {result:.2f}Ra")

        elif choice=='8':
            result=rankine_to_celcius(value)
            print(f"{value}Ra is {result:.2f}C")

        elif choice=='9':
            result=rankine_to_fahrenheit(value)
            print(f"{value}Ra is {result:.2f}F")

        elif choice=='10':
            result=fahrenheit_to_rankine(value)
            print(f"{value}F is {result:.2f}Ra")

        elif choice=='11':
            result=rankine_to_kelvin(value)
            print(f"{value}Ra is {result:.2f}K")

        elif choice=='12':
            result=kelvin_to_rankine(value)
            print(f"{value}K is {result:.2f}Ra")

        elif choice=='13':
            result=reaumur_to_celcius(value)
            print(f"{value}Re is {result:.2f}C")

        elif choice=='14':
            result=celcius_to_reaumur(value)
            print(f"{value}C is {result:.2f}Re")

        elif choice=='15':
            result=reaumur_to_fahrenheit(value)
            print(f"{value}Re is {result:.2f}F")

        elif choice=='16':
            result=fahrenheit_to_reaumur(value)
            print(f"{value}F is {result:.2f}Re")

        elif choice=='17':
            result=reaumur_to_kelvin(value)
            print(f"{value}Re is {result:.2f}K")

        elif choice=='18':
            result=kelvin_to_reaumur(value)
            print(f"{value}K is {result:.2f}Re")

        elif choice=='19':
            result=reaumur_to_rankine(value)
            print(f"{value}Re is {result:.2f}Ra")

        elif choice=='20':
            result=rankine_to_reaumur(value)
            print(f"{value}Ra is {result:.2f}Re")

        else:
            print("Wrong choice.Select from 0 to 20.")

if __name__=="__main__":
    main()


