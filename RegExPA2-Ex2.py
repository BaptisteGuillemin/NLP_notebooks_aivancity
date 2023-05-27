
import re
valid = []
invalid = []



pattern = '([A-Za-z0-9])+([._-]?[a-zA-Z0-9]+)*@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'



#Test
EmailList = ["Jhon.doe@gmail.com","Jhondoe154@outlook.com",
             "Jhondoe154@outlook.co.uk","Jhon.doe1@aivancity.education",
             "Jhon_doe1@aivancity.education","Jhon-doe@yahoo.fr",
             "Jhon-doe@yahoo..fr","Jhon.doe@gmail.com.","Jhon;doe@gmail.com",
             "Jhondoe154@outlook-com","Jhon.doe1@@aivancity.education",
             "@yahoo.fr","Jhon.doe1@aivancity"]
for userText in EmailList:
    match = re.fullmatch(pattern,userText)
    if match:
        valid.append(userText)

    else:
        invalid.append(userText)

    
print('valid emails')
print(valid)
print('invalid emails')
print(invalid)













##UserText = input("Email: ")
##pattern = '\S+@{1}\S+\.{1}\S+'
##match = re.search(pattern,userText)
##if match:
##    print('email insrted')
##
##else:
##    print('Please enter a valid email')
