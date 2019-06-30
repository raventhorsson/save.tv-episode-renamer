import os
import re
print(f"We are the rename-demons. Grateful to be of service to you.\nFirst the program will run in TestMode and shows you what it will do.")
path = input("Please, provide the path to the files we shall rename.\n")
username = input("Please, provide the your Save.TV username.\n")
username = "_" + username
path = path.replace("\\" , "/")

l = os.listdir(path)#puts filenames into the array l
t = 0
k = 0
testmode = True
length = len(l)

while k <= 1:
    while t < length:
        episodename = l[t]
        match = re.search("S[0-9][0-9]E[0-9][0-9]_", episodename)#determines if episodeinformation is supplied
        if match:
            Folge = match.group(0)#delivers the string we searched for 
            newepisodename = episodename
            newepisodename = newepisodename.replace(Folge,'') #delete "Folge"
            newepisodename = Folge + newepisodename #new episodename is created, Folge is at beginning, rest is concatenated except Folge SxxExx 
            newepisodename = newepisodename.replace(username,'') #delete User ID
            newepisodename = newepisodename.replace('Folge','') #delete "Folge"
            t += 1
            if testmode == False:
                print(f"Renaming: {episodename}")
                os.rename(path + "/" + episodename, path + "/" + newepisodename)#Files will only be renamed if the testmode is disabled
            else:
                print (f"\n{episodename}")
                print (f"{newepisodename}\n")#In testmode the result is displayed to give user the opportunity to decide if renaming works as intended
                
        else: 
            t += 1
            newepisodename = episodename
            newepisodename = newepisodename.replace(username,'') #delete User ID
            if testmode == False:
                os.rename(path + "/" + episodename, path + "/" + newepisodename)#Files will only be renamed if the testmode is disabled
            else:
                print(f"{newepisodename}")#In testmode the result is displayed to give user the opportunity to decide if renaming works as intended
                print(f"Seems no episode information is contained in filename.\n")
        
    if testmode == True:
        proceed = input("Shall we perform the renaming?(Y/N)\n")
    if proceed == "Y" or "y" or "j" or "J":
        k = k + 1
        t = 0
        testmode = False
        continue
    else:
        print(f"We are very sorry that our renaming skills didn't fullfill your requirements.")
        break
