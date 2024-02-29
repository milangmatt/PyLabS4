""" 
Name : Milan George Mathew
Class : S4 DS
Roll No : 39
Experiment : 5 - E-Mail verification
Date : 28 - 02 - 2024
"""

email=input("Enter E-Mail ID : ")
verified = 1
ID = email.split('@')
if not len(ID)==2 :
    verified = 0
else :
    name=ID[0]
    url=ID[1]
    if (not name.isalnum()) and '_' not in name:
        verified = 0
    else :
        domain = url.split('.')
        if len(domain) > 1:
            for i in url.split('.'):
                if not i.isalnum():
                    verified = 0
        else:
            verified=0
if verified == 1:
    print("Valid Email ID")
else :
    print("Invalid Email ID")