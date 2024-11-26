price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
for key,value in price_list.items():
    print(key,value)

count=0
for  value in price_list.values():
    count+=value
print(count)

updated={}
count1=0
for key,value in price_list.items():
   
    new_price = value * 0.9 
    updated[key] = new_price
    count1+=new_price
    print(key, "Updated Price:", new_price)
print(count1)


    
