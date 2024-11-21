username = "admin5"
password = "admin1234"

registration = []

def newregistration(firstname, lastname, address, phone, email):
    k = {}
    k["firstname"] = firstname
    k["lastname"] = lastname
    k["address"] = address
    k["phone"] = phone
    k["email"] = email
    registration.append(k)

while True:
    action = int(input("please enter task to perform 1: register 2 : login 3: registration details: "))
    if action ==1:
        firstname = input("please enter firstname: ")
        lastname = input("please enter lastname: ")    
        address = input("please enter address: ")    
        phone = input("please enter phone: ")    
        email = input("please enter email: ")   
        newregistration(firstname, lastname, address, phone, email)
        #task
    elif action == 2:      
        user = input("please enter your username: ")
        newpass = input("please enter your password: ")
        if (username==user) and (password== newpass):
            print("successful")
        else:
            print("invalid")
    else:
        print(registration)

