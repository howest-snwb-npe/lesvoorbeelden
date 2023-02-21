tijd = int(input("Hoe laat is het? "))

if 1 <= tijd <= 12:
    for i in range(tijd):
        print("koekoek")
else:
    print("Geef een getal tussen 1 en 12")