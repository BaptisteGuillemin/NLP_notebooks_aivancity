
import re





pattern = "[0\+\(][\d{1,3}]?[\)-]?\d{9}|\d{1,3}-\d{9}"


text ="""Mr. John requests that you call him at 0123456789
                The meeting is scheduled for 20-10-2022;
                contact the client at +33123456789.
                The product will be shipped for 125489655 £.
                (1)123456789 is my new phone number.
                +123123456789 is my new phone number.
                There was a missed call from 358-123456789"""

match = re.findall(pattern,text)
print(match)

    






























##UserText = input("Email: ")
##pattern = '\S+@{1}\S+\.{1}\S+'
##match = re.search(pattern,userText)
##if match:
##    print('email insrted')
##
##else:
##    print('Please enter a valid email')
