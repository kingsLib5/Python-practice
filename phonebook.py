#to add phone details to list
book = []


#function to add to the list using dictionary
def addnewuser(firstname, lastname, address, phone, email):
    k = {}
    k["firstname"] = firstname
    k["lastname"] = lastname
    k["address"] = address
    k["phone"] = phone
    k["email"] = email
    book.append(k)

#looping for the inputs
while True:
    action = int(input("please enter task to perform 1: for new user 2 : for result: "))
    if action ==1:
        firstname = input("please enter firstname: ")
        lastname = input("please enter lastname: ")    
        address = input("please enter address: ")    
        phone = input("please enter phone: ")    
        email = input("please enter email: ")   
        addnewuser(firstname, lastname, address, phone, email)
        #task
    else:      
        print(book)
        #task
