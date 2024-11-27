hotels_in_Krakow = [
   {"name": "Sky", "price": 320.00},
   {"name": "Metropol", "price": 480.00},
   {"name": "New Port", "price": 420.00},
   {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
   {"name": "Focus", "price": 510.00},
   {"name": "Aqua", "price": 345.00},
   {"name": "La Boutique", "price": 390.00},
   {"name": "Marina", "price": 410.00}
]


def calculate_average(hotels):
    total_price = 0
    hotel_count = len(hotels) 
    
    for hotel in hotels:
        total_price += hotel["price"]
    
    average_price = total_price / hotel_count  
    return average_price


average_krakow = calculate_average(hotels_in_Krakow)
average_sopot = calculate_average(hotels_in_Sopot)


print(f"Average price of hotels in Krakow: {average_krakow:.2f} PLN")
print(f"Average price of hotels in Sopot: {average_sopot:.2f} PLN")

if average_krakow>average_sopot:
    print('sopots hotels are cheaper')
if average_sopot>average_krakow:
    print('krakows hotels are cheaper')
