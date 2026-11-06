print("---- EJERCICIOS DE DICCIONARIOS - 1")

hotel = {
    'name': 'Hotel Zeta',
    'number_of_stars': 4,
    'rooms': [
        {
            'number': 101,
            'floor': 1,
            'price_per_night': 170,
        }
        ]
}

for i,j in hotel.items():
    print(i , j)