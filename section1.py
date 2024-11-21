#program to diplay details

details = []
for i in range(1,8):
    if i==1:
        detail = input("please enter your firstname: ")
        details.append(detail)
    if i==2:
        detail = input("please enter your lastname: ")
        details.append(detail)
    if i==3:
        detail = input("please enter your address: ")
        details.append(detail)
    if i==4:
        detail = input("please enter your phone number: ")
        details.append(detail)
    if i==5:
        detail = input("please enter your email: ")
        details.append(detail)
    if i==6:
        detail = input("please enter your state: ")
        details.append(detail)
    if i==7:
        detail = input("please enter your country: ")
        details.append(detail)

print(details)
