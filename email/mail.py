#!/usr/bin/env python3
import smtplib,sys

#function to accept login details
def login():
    print("Enter your email-ID")
    email=input()
    print("Enter your password")
    password=input()
    return email,password


#function to enter details of sender and message
def send():
    print("Enter the recipients ID")
    rec=input()
    group=rec.split()
    print("Enter Subject")
    sub=input()
    print("Enter Message")
    mes=input()
    sub="Subject: {}\n".format(sub)
    mes=sub+'\n'+mes
    return group,mes

try:
    #Creating SMTP object linking to smtp server
    smtpObj=smtplib.SMTP('smtp.gmail.com',587)
    #Sending hello
    smtpObj.ehlo()
    #Enabling TLS Encryption
    smtpObj.starttls()
    print("Connection Established   ")
except Exception:
    print("Error Establishing connection")

try:
    email,password=login()
    #logging into the account
    smtpObj.login(email,password)
    print("Login successful")
except Exception:
    print("Login Failed")
    smtpObj.quit()
    sys.exit()


rec,mes=send()
#Sending the mail
smtpObj.sendmail(email,rec,mes)

#Ending the session
smtpObj.quit()

print("Mail sent successfully :)")
