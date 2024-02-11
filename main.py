from datetime import datetime

from read import file_reading_mode
from operation import if_purchased,if_sold,user_name_number,validity_checkfor_ID,validity_checkfor_quantity,buying_details,for_invoice,selling_details
from write import overriding_1,overriding_2
date_time = datetime.now()


print("\n")
print("=====*=====*=====*=====*=====*=====*====*=====*=====*=====*======*======*=======*=======*=======*=====*=====*======*======*=====*=====*======*=====")
print("\n")
print("\t \t \t \t \t \t \t  Welcome to The Laptop World")
print("\t \t \t \t \t \t \t --------------------------------")
print("\n")
print("\t \t Address: Birtamod, jhapa                                                           Contact: 9817994959")
print("\n")
print("=====*=====*=====*=====*=====*=====*====*=====*=====*=====*======*======*=======*=======*=======*=====*=====*======*======*=====*=====*======*=====")
print("\n")
mydict = file_reading_mode()


continueLoop = True
while continueLoop ==True:
    
    print("\n")
    print("\n")
 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Press 1 to buy from manufacturer")
    print("Press 2 to sell to customer")
    print("Press 3 to exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    print("---------------------------------------------------------------------------------------------------------------")
    try:
        userinput = int(input("Press any number 1, 2, or 3: "))
        if userinput not in [1,2,3]:
            print("Dear user,Please input either 1,2,or 3! ")
            continue
        
    except:
        print("Dear user, please enter valid number")
        continue

    
    


    if userinput == 1:
        buying_details()
        user_name,user_number = user_name_number()
        purchased_laptop = []

        
        buy_iteration = True
        while buy_iteration == True:
            valid_id = validity_checkfor_ID()
            valid_quantity = validity_checkfor_quantity(valid_id)
            VATAmount = 0
            name_of_product = mydict[valid_id][0]
            quantity_asked = valid_quantity
            unit_price = mydict[valid_id][2]
            price_of_oneitem = mydict[valid_id][2].replace("$","")
            total_cost = int(price_of_oneitem) * int(quantity_asked)
            

            purchased_laptop.append([name_of_product,quantity_asked,unit_price,total_cost])

            purchased_more = input("Do you want to buy more laptops?(y/n):")

            if purchased_more.lower() =="y":
                buy_iteration = True


            else:
                total = 0
                VATAmount = 0
                for i in purchased_laptop:
                    total+=int(i[3])
                VATAmount = 0.13 * total
                grand_total = total + VATAmount

                for_invoice(user_name,user_number,date_time,purchased_laptop)
                if_purchased(valid_id,valid_quantity,purchased_laptop,total_cost,VATAmount,grand_total)
                overriding_1(user_name,user_number,purchased_laptop,VATAmount,grand_total)
                buy_iteration=False
    
        
        
    elif userinput==2:
        selling_details()
        user_name,user_number = user_name_number()
        purchased_laptop =[]
       
        sell_iteration = True
        while sell_iteration == True:
            valid_id = validity_checkfor_ID()
            valid_quantity = validity_checkfor_quantity(valid_id)
            shipping_price = 0
            name_of_product = mydict[valid_id][0]
            quantity_asked = valid_quantity
            unit_price = mydict[valid_id][2]
            price_of_oneitem = mydict[valid_id][2].replace("$","")
            total_cost = int(price_of_oneitem) * int(quantity_asked)

            purchased_laptop.append([name_of_product,quantity_asked,price_of_oneitem,total_cost])
            sell_more = input("Do you want to sell more?(y/n):")

            if sell_more.lower() =="y":
                sell_iteration =True

            else:

                total = 0
                shipping_price = 0
                for i in purchased_laptop:
                    total+=int(i[3])
                grand_total = total + shipping_price


                for_invoice(user_name,user_number,date_time,purchased_laptop)
                if_sold(valid_id,valid_quantity,date_time,purchased_laptop,shipping_price,grand_total)
                overriding_2(user_name, user_number,date_time, purchased_laptop,shipping_price, grand_total)
                sell_iteration = False
    elif userinput ==3:
        print("Thank you for having our service!!!")
        continueLoop = False
