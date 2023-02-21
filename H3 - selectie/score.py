score = int(input("Geef uw score /20: "))

match score:
    case 16 | 17 | 18 | 19 | 20:
        print("Uitzonderlijk")
    case 14 | 15:
        print("Onderscheidend")
    case 12 | 13:
        print("Ruim en vlot")
    case 10 | 11:
        print("Voldoende")
    case _:
        print("Onvoldoende")