from datetime import datetime
def overriding_1(user_name, user_number, purchased_laptop,VATAmount,Final_amount):
    '''Writes the bill for the purchased laptops in the text file '''
    date_time = datetime.now()
    with open(str(user_name)+str(user_number)+".txt","w") as file:
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\t \t \t \t \t Laptop world Bill ")
        file.write("\n")
        file.write("\t \t \t \t Birtamod,jhapa ,phone: 9817994959")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Laptop Details: ")
        file.write("\n")
        file.write("Customer name: "+str(user_name))
        file.write("\n")
        file.write("Contact Number: " +str(user_number))
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------------")
        file.write("Date and time of buying: " +str(date_time))
        file.write("------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("purchase Detail are: ")
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("Item Name  \t Total Quantity \t Unit Price \t \t  Total")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------")
        for i in purchased_laptop:
            file.write(str(i[0])+ "\t \t \t"+ str(i[1])+ "\t \t \t"+str(i[2])+ "\t \t \t"+"$"+str(i[3])+"\n")
        file.write("----------------------------------------------------------------------")
        file.write("VAT Amount : "+ str(VATAmount))
        file.write("Grand Total: $"+str(Final_amount)) 
        file.write("VAT Amount is added to grand total")



def overriding_2(user_name, user_number,date_time, purchased_laptop,shipping_price, Final_amount):
    '''Writes the bill for the purchased laptops in a text file'''
    with open(str(user_name)+str(user_number)+".txt","w") as file:
         file.write("\n")
         file.write("\n")
         file.write("\t \t \t \t Laptop Shop Bill ")
         file.write("\n")
         file.write("\t \t Kamalpokhari, Kathmandi | Phone No: 9876547 ")
         file.write("\n")
         file.write("-------------------------------------------------------------------------------")
         file.write("Laptop Details are:")
         file.write("-------------------------------------------------------------------------------")
         file.write("Name of the customer: "+str(user_name))
         file.write("Contact number: "+str(user_number))
         file.write("Date and  time of purchase: "+str(date_time))
         file.write("-------------------------------------------------------------------------------")
         file.write("\n")
         file.write("Purchase Detail are: ")
         file.write("----------------*--------------*--------------*------------*--------------------*----------------------")
         file.write("Item Name \t \t Total Quantity \t \t Unit Price \t \t \t Total")
         file.write("----------------*--------------*--------------*------------*--------------------*----------------------")
         for i in purchased_laptop:
             file.write( str (i[0])+ "\t\t\t"+ str (i[1])+ "\t\t\t"+str (i[2])+"\t\t\t"+"$"+ str (i[3])+"\n")
             file.write("-------------------------------------------------------------------------------")
         if shipping_price:

             file.write("Your shipping cost is:"+""+str( shipping_price)+"\n")
             file.write("Grand Total:"+str(Final_amount)+"\n")
             file.write("Note: Shipping cost is added to the grand total"+"\n")     
         else:
             file.write("Grand Total: $"+str(Final_amount))
    

    
