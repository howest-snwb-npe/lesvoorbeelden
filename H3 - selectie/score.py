score = int(input("Geef uw score /20: "))

if score >= 16:
    print("Uitzonderlijk")
elif score >= 14:
    print("Onderscheidend")
elif score >= 12:
    print("Ruim en vlot")
elif score >= 10:
    print("Voldoende")
else:
    print("Onvoldoende")