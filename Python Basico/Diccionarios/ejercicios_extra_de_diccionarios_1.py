print("---- EJERCICIOS EXTRA DE DICCIONARIOS - 1")

sales = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Iron',
                'upc': 'ITEM-324',
                'unit_price': 32.45,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 12.54,
            },
        ],
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 5.42,
            },
        ],
    },
    {
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 3.42,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 17.54,
            },
        ],
    },
    {
            'date': '26/02/23',
            'customer_email': 'amanda@gmail.com',
            'items': [
                {
                    'name': 'Key Holder',
                    'upc': 'ITEM-23',
                    'unit_price': 3.42,
                },
                {
                    'name': 'Basketball',
                    'upc': 'ITEM-432',
                    'unit_price': 17.54,
                },
                {
                    'name': 'Phone Case',
                    'upc': 'ITEM-444',
                    'unit_price': 45.89,
                },
                {
                    'name': 'Screen',
                    'upc': 'ITEM-326',
                    'unit_price': 25.99,
                },
            ],
        },
]

total_info = {}

for i in range(len(sales)):
    for j in range(len(sales[i].get('items'))):
        if sales[i].get('items')[j].get('upc') not in total_info:
            total_info[sales[i].get('items')[j].get('upc')] = 0
        total_info[sales[i].get('items')[j].get('upc')] += sales[i].get('items')[j].get('unit_price') 

for i,j in total_info.items():
    print(f"{i}: {j}")