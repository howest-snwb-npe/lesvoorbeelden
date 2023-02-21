x = int(input("Geef een getal voor x: "))
y = int(input("Geef een getal voor y: "))

if x < y:
    print("x is kleiner dan y")
else:
    if x > y:
        print("x is groter dan y")
    else:
        if x == y:
            print("x is gelijk aan y")