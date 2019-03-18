## Primary Project 1 - "Python program to create a user-interface driven 'knock Knock' jokes"
## Name - Shriram Sivaraman
## Course - Introduction to Python Programming 
## Course code - MSIT 3440
## Description - The objective of the program is to present a user-interface driven “knock knock” jokes where both the system 
##               and the user interact with each other as “person 1 and person 2” in joke format.

import random
joketot=[]
joketot.append(["yah","Noo!, Thanks I use Google"])
joketot.append(["firewall","welcome to china! Home of the great firewall"])
joketot.append(["hard drive","I had a hard drive, let me in so I can relax!!"]) ## accepting the joke's prompt and punchline
variant=["who's there","who's there?","whos there?","whos there",
         "who is there","who is there?","who there?","who dere","who dere?"]   ## list to get all types of who is there
random.shuffle(joketot)						                                   ## random.shuffle is used to shuffle the list containing jokes
print "     Welcome to the portal of Knock-Knock jokes      "
while True:
    try:
        times=int(raw_input("Enter the number of 'knock-knock' jokes you wanna hear ?? "))  ## To enroll the number of times to tell the joke
        if times in range(1,4):					    ## To check the number of jokes within the range
            break
        else:
            print '  ', times, 'is out of range'   ## To print if the given input is out of range
    except ValueError:						       ## To handle ValueError exception
        print " I am expecting a number dear !! "
    except KeyboardInterrupt:
        exit ()
print "Prepare to be amazed "
inc=0                                ## A variable which is initialized to trasverse through the list everytime for loop runs
for inc in range(times):
    text1=raw_input("knock, knock !! \n")
    if text1.lower() in variant:
        print joketot[inc][0]
    else:
	## While loop made to run until the input prompt condition is satisfied
        while True:
            text1=raw_input(" Please type Who's there? \n")
            if text1.lower() in variant:
                print joketot[inc][0]
                break
    text2=raw_input("")                                         ## user input based on the system prompt
    if "who" in text2.lower():                                  ## check made if word "who" is in the input text
        print joketot[inc][1]
    else:
	## While loop made to run until the input prompt condition is satisfied
        while True:
            print 'Please type '+(joketot[inc][0]+" who")
            text2=raw_input("")			                        ## user input based on the system prompt
            if "who" in text2.lower():
               print joketot[inc][1]
               break
    inc+=1
    if inc<times:
        print "Ha Ha!!Get ready for next joke"                  ## To alert the user to get ready for the next joke
    else:
        print "Hope you had great fun. Bye-Bye!!"               ## This message gets printed after the last joke 
        break

