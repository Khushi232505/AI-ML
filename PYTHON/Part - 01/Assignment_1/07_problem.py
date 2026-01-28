celcius = input("Enter the temprature in celcius : ")

CelciusTemp = float(celcius)
print(CelciusTemp, type(CelciusTemp))

FahrenheitTemp = (CelciusTemp * (9/5)) + 32

print("Temprature in Fahrenhiet :", FahrenheitTemp )
