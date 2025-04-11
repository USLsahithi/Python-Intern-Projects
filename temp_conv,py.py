temp=input("Enter the temperature that you would like to convert? (like 45F,23C,56R,78K etc...): ")
degrees=int(temp[:-1])
choice=temp[-1]
if choice.upper()=='F':
    c=(degrees-32)*(5/9)
    k=c+273.15
    r=degrees+459.67
    print("The temperature in celsius is : ",c,"degrees.")
    print("The temperature in kelvin is : ",k,"degrees.")
    print("The temperature in rankine is : ",r,"degrees.")
elif choice.upper()=='C':
    f=(degrees*(9/5))+32
    k=degrees+273.15
    r=f+459.67
    print("The temperature in fahrenheit is : ",f,"degrees.")
    print("The temperature in kelvin is : ",k,"degrees.")
    print("The temperature in rankine is : ",r,"degrees.")
elif choice.upper()=='K':
    c=degrees-273.15
    f=(c*(9/5))+32
    r=f+459.67
    print("The temperature in celsius is : ",c,"degrees.")
    print("The temperature in fahrenheit is : ",f,"degrees.")
    print("The temperature in rankine is : ",r,"degrees.")
elif choice.upper()=='R':
    f=degrees-459.67
    c=(f-32)*(5/9)
    k=c+273.15
    print("The temperature in fahrenheit is : ",f,"degrees.")
    print("The temperature in celsius is : ",c,"degrees.")
    print("The temperature in kelvin is : ",k,"degrees.")
else:
    print("Enter proper value for temperature")
    quit()
    
