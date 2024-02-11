from read import file_reading_mode
from datetime import datetime


mydict = file_reading_mode()

def validity_checkfor_ID():
    '''Asks the user to to input ID of the laptop and verify if the ID is valid and returns particular ID of the laptop.'''
    print("-----------------------------------------------------------------------")
    
    valid_id = int(input("Please input ID of the Laptop for you want to buy:"))
    print("-----------------------------------------------------------------------")
    print("\n")

        #criteria for valid ID
    while valid_id <= 0 or valid_id> len(file_reading_mode()):
        print("-----------------------------------")
        print("Please provide the valid ID")
        print("-----------------------------------")
        print("\n")
        print("-----------------------------------------------------------------------")
        valid_id = int(input("Please inputID of the Laptop for you want to buy:"))
    
        print("-----------------------------------------------------------------------")
        print("\n")
    return valid_id

    #criteria for valid_quantity


def validity_checkfor_quantity(valid_id):
    '''Asks the user to input quantity of the laptop and verify if the entered quantity is valid,
    it also has valid ID as arguments and returns particular quantity'''
    print("-------------------------------------------------------------------------------")
    valid_quantity = int(input("Please provide the quantity of the laptop you want to buy"))
    print("-------------------------------------------------------------------------------")
    available_quantity = mydict[valid_id][3]
    #criteria for valid quantity
    while valid_quantity <= 0 or valid_quantity> int(available_quantity):
        print("-------------------------------------------------------------------------------------------------------------------")
        print("Dear concern, we don't have the number of laptops you are looking for in our stock.Please check out yhe list again ")
        print("-------------------------------------------------------------------------------------------------------------------")
        print("\n")
        valid_quantity = int(input("Please provide the quantity of the laptop you want to buy"))
        print("\n")
    return valid_quantity



date_time = datetime.now()




def for_invoice(user_name, user_number,date_time,purchased_laptop):
        '''It prints the bill for the purchased laptops '''
        print("\n")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("\t \t \t \t \t Laptop world Bill ")
        print("\n")
        print("\t \t \t \t Birtamod,jhapa ,phone: 9817994959")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("Laptop Details: ")
        print("\n")
        
       
        print("Customer name: "+str(user_name))
        print("\n")
        print("Contact Number: " +str(user_number))
        print("\n")
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        print("Date and time of buying: " +str(date_time))
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("purchase Detail are: ")
        print("\n")
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        print("Item Name  \t Total Quantity \t Unit Price \t \t  Total")
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        #Iterate over the the list of purchased items and display the  details of each products
        for i in purchased_laptop:
            print(i[0], "\t ", i[1], "\t \t ", i[2], "\t \t ","$",i[3])
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        


def user_name_number():
    '''It takes user input for the name and mobile number and also handles the certain exception'''
    user_name = input("Enter your name: ")
    while True:
        try:
            user_number = input("Enter your mobile number: ")
            if (len(user_number)) != 10:
                print("Dear user, please input the 10 digit number")
                continue
            else:
                break
            
        except:
            print("Invalid mobile number")
            continue

    return user_name, user_number


def buying_details():
    '''Displays the details of available laptops'''
        
    print("Thank you for buying")
    print("\n")
    print("Name and number are required to print bill")
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("ID \t Name \t \t  Brand \t  Price \t  Quantity \t  processor \t Graphic Card")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    a = 1
    file = open("laptop.txt","r")
    for line in file:
        print(a, "\t" +line.replace(",","\t"))
        a+=1
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    file.close()
    print("\n")


def if_purchased(valid_id, valid_quantity, purchased_laptop, total_cost,VATAmount, grand_total):
        
        '''It updates the stock of laptop ,calculates and prints the vat amount and grand total amount. It also 
        returns valid_id, valid_quantity, date_time, purchased_laptop, VATAmount, grand_total'''
        
         #updating text file

        mydict[valid_id][3] = int(mydict[valid_id][3]) + int(valid_quantity)
        file = open("laptop.txt", "w")
        for values in mydict.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
            file.write("\n")
        file.close()


        #getting items purchased by the user
        total = 0
        for i in purchased_laptop:
            total+=int(i[3])
        VATAmount = 0.13*total
        grand_total = total + VATAmount

        date_time = datetime.now()
        if VATAmount:
            print ("VAT Amount : ", VATAmount)
            print("Grand Total: $"+str(grand_total))
            print("-----------------------------------------------------------------------------------------------------------")
            print("\n")
            print("VAT Amount is added to grand total")

        else:
              print("Grand Total: $"+str(grand_total))    
        return valid_id, valid_quantity, date_time, purchased_laptop, VATAmount, grand_total



def selling_details():
    '''It display the selling details of the laptop'''
    print("\n")
    print("Thank you for selling")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("\t For Bill Generation you will have to enter your details first:")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("S.N\t Name \t \t  Brand \t Quantity \tPrice\t \tProcessor \t \tGraphic Card")
    print("--------------------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("laptop.txt","r")
    for line in file:
            print(a,"\t" + line.replace(",","\t"))
            a+=1
    file.close()
    print("--------------------------------------------------------------------------------------------------------------------")
    
    print("\n")



def if_sold(valid_id, valid_quantity,date_time,purchased_laptop,shipping_price,grand_total):
    '''Updates the laptop stock after the selling transaction and also calculates and displays shipping cost and total amount
    .Also returns date_time, purchased_laptop,shipping_price,grand_total,valid_id,valid_quantity'''

    quantity = mydict[valid_id][3]
    mydict[valid_id][3] = int(quantity)-int(valid_quantity)
    # Opening file in reading mode
    file = open("laptop.txt","w")

    for values in mydict.values():
         file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
         file.write("\n")
    file.close()


    #retrieving user purchased items

    date_time = datetime.now()

   

    print("----------------------------------------------------------------------------------------")
    shipping_price = input("Dear concern, Do you want your laptop to be shipped?(y/n)")

    if shipping_price.lower() =="y":
        net_total = 0
        shipping_price = 500
        for i in purchased_laptop:
            net_total+=int(i[3])
        grand_total = net_total+shipping_price
        print("Your shipping cost is:", shipping_price)
        print("Grand Total:"+str(grand_total))
        print("Shipping cost has been added to the grand total")

    else:
        print("Grand Total:"+str(grand_total))
        print("Shipping cost has not been added to the grand total")
    return date_time, purchased_laptop,shipping_price,grand_total,valid_id,valid_quantity







       
 


    
        
