def celcius():
    print("===========Celcius==========")
    inputCelcius = float(input("Masukkan suhu: "))
    outputReamur = (4/5) * inputCelcius
    outputFahrenheit = (9/5) * inputCelcius + 32
    outputKelvin = inputCelcius + 273
    print(f"Reamur      : {outputReamur}°R")
    print(f"Fahrenheit  : {outputFahrenheit}°F")
    print(f"Kelvin      : {outputKelvin}°K")
    print()
    lanjut = input("Lanjut? [y/n]: ")
    while lanjut == "y" or lanjut == "Y":
        main()
    else:
        exit()

def reamur():
    print("===========Reamur==========")
    inputReamur = float(input("Masukkan suhu: "))
    outputCelcius = (5/4) * inputReamur
    outputFahrenheit = (9/4) * inputReamur + 32
    outputKelvin = (5/4) * inputReamur + 273
    print(f"Celcius      : {outputCelcius}°C")
    print(f"Fahrenheit  : {outputFahrenheit}°F")
    print(f"Kelvin      : {outputKelvin}°K")
    print()
    lanjut = input("Lanjut? [y/n]: ")
    while lanjut == "y" or lanjut == "Y":
        main()
    else:
        exit()

def fahrenheit():
    print("===========Fahrenheit==========")
    inputFahrenheit = float(input("Masukkan suhu: "))
    outputCelcius = 5/9 * (inputFahrenheit - 32)
    outputReamur = 4/9 * (inputFahrenheit - 32)
    outputKelvin = 5/9 * (inputFahrenheit - 32) + 273
    print(f"Celcius     : {outputCelcius}°C")
    print(f"Fahrenheit  : {outputReamur}°F")
    print(f"Kelvin      : {outputKelvin}°K")
    print()
    lanjut = input("Lanjut? [y/n]: ")
    while lanjut == "y" or lanjut == "Y":
        main()
    else:
        exit()

def kelvin():
    print("===========Kelvin==========")
    inputKelvin = float(input("Masukkan suhu: "))
    outputCelcius = inputKelvin - 273
    outputReamur = 4/5 * (inputKelvin - 273)
    outputFahrenheit = 9/5 * (inputKelvin - 273) + 32
    print(f"Celcius     : {outputCelcius}°C")
    print(f"Reamur      : {outputReamur}°R")
    print(f"Fahrenheit  : {outputFahrenheit}°F")
    print()
    lanjut = input("Lanjut? [y/n]: ")
    while lanjut == "y" or lanjut == "Y":
        main()
    else:
        exit()

def main():
    print("===========Temperature Converter==========")
    print("1. Celcius")
    print("2. Reamur")
    print("3. Fahrenheit")
    print("4. Kelvin")
    pilihan = int(input("Pilih tipe suhu (1/2/3/4): "))

    while pilihan == 1:
        celcius()
    while pilihan == 2:
        reamur()
    while pilihan == 3:
        fahrenheit()
    while pilihan == 4:
        kelvin()
    else:
        print("Pilihan tidak tersedia")
        exit()

main()