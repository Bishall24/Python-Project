def file_reading_mode():
    ''' This function reads the laptop.txt file and stores the given data in the dictionary and return it'''
    file = open("laptop.txt","r")
    Laptop_id = 1
    mydict = {}
    for line in file:
        line = line.replace("\n","")
        mydict.update({Laptop_id:line.split(",")})
        Laptop_id += 1
    file.close()
    return mydict
    
