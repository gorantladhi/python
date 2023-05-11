import re
#f=open("ipaddress.txt", "r")
#new=open("‪firstip1.txt","w")
#new.truncate(0)
#l=f.readlines()
#out=" "
#for i in l:
    
    #if re.findall('^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9])$',i):
        #new=open("firstip1.txt","a")
        #new.write(i)
        #new.close()

'''
f=open("phonenumbers.txt")
new=open("phnoutput.txt")
#new.truncate(0)
l=f.readlines()
for i in l:
    if re.findall('^([6-9][0-9]{9})$',i):
        new.write(i)
        new.close()
'''
f=open("gmailids.txt","r")
new=open("gmailoutput.txt","w")
new.truncate(0)
l=f.readlines()
for i in l:
    if re.findall("\w[a-zA-Z0-9\.]*@gmail\.com",i):
        new.write(i)
new.close()
