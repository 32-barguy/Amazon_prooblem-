'''
Thinking that I have 4 items from amazon and flipkart prices different

They are :
Keyboard = 2190
Mouse = 1912            ---- Prices in amazon
CPU = 19020


Keyboard = 2999
Mouse = 2142            ---- Prices in flipkart
CPU = 19990

I want to compare  which one of them is bigger One by one 

Lets assign some simple codes to each one

Keyboard_amazon  MEans keyboard from amazon

Keyboard_flipkart means keyboard from flipkart 


Let's turn them into some data  type 

first Let's try a dict data type


amazon_prices = {"keyboard" : 2190


    
    }






'''


amazon_prices = {
    "keyboard_amazon" : 2190,
    "mouse_amazon" : 1912,
    "CPU_amazon" : 19020
}

flipkart_prices = {
    1 : 2999,
    2 : 2142,
    3 : 19990
}
print(flipkart_prices[3])

flipkart_list = []
amazon_list = []
for items,item in flipkart_prices and amazon_prices:
    flipkart_list.append(items)
    amazon_list.append(item)

print(flipkart_list)
print(flipkart_list)




# compared = {}

# def comparer(first,second):
#     global compared
#     if first>second:
#         resul = first
#         compared.update({"okay" : resul})
#         return compared
#     elif second>first:
#         resul = second
#         compared.update({"okay_no" : resul}) 
#         return compared


# CPU = Amazon_things_Priced.
# print(comparer(,))

# Amazon_things_Priced = {"CPU_1" : 12}
# CPU = Amazon_things_Priced.
