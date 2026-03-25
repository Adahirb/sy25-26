F1 = ["F1", "VW Off Road-Bug", 185, (104,142), 6000, 0, 1886, 4]

C3 = ["C3", "VW Polo GTI", 185, (96,103), 7600, 8.0, 1600, 4]

C1 = ["C1", "Subaru Impreza WRC", 220, (221,300), 5500, 5.4, 1994, 4]
 
E2 = ["E2", "Ford Escort", 220, (220,299), 6250, 5.6, 1993, 4]

B3 = ["B3", "Toyota Corolla WRC", 210, (220,299), 5700, 5.4, 1972, 4]

B1 = ["B1", "Seat Cordoba WRC", 230, (221,300), 6000, 5.0, 1998, 4]

C2 = ["C2", "Opel Astra GSi", 235, (235,320), 6200, 5.6, 2962, 6]

D4 = ["D4", "Peugeot 206 WRC", 225, (221,300), 5600, 5.4, 1996, 4]

C4 = ["C4", "Citroen Saxo Kit-Car", 168, (161,220), 7000, 7.5, 1600, 4]


def print_car(c):
    # Set the card width
    width = 47
    border = "|" + "-" * (width - 2) + "|"

    # Prepare each line, padded to the card width
    lines = [
        f"| {c[0]} - {c[1]}".ljust(width - 1) + "|",
        f"| Top Speed: {c[2]} km/h      | 0-100 km/h: {c[5]} s".ljust(width - 1) + "|",
        f"| Power: {c[3][0]}-{c[3][1]} hp        | Year: {c[6]}".ljust(width - 1) + "|",
        f"| RPM: {c[4]}                | Cylinders: {c[7]}".ljust(width - 1) + "|"
    ]

    print(border)
    for line in lines:
        print(line)
    print(border)

cars = [F1, C3, C1, E2, B3, B1, C2, D4, C4]


i = 1
for car in cars:
    print(i, car[1])
    i += 1

choice = int(input("Card Number: "))
print_car(cars[choice -1])