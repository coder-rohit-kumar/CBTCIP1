# CBTCIP1import os
def screen_clear():
    if os.name== "Pasin":
        _=os.system('clear')
    else:
        _=os.system('cls')
import time
print("\t\t\t\t*@@@ QUIZ GAME @@@@ ***")
print("\t\t\t\t\t\t\t****Level:-1****\n")
time.sleep(1)
name=input("Enter yours name")
print("\t\n\t\n\t\n\t\n\t\t!!!!Are you ready !!!!!\t\n\t\n\t\n\t\t\t",name)
time.sleep(1)
input("PLEASE PREES ANY KEY")
time.sleep(1)
print("\n\t\n\t\n\t\n\t\t!!!!!!!!!!!!Let's Play!!!!!!!!!!\n\t\n\t\n\t")
time.sleep(2)
screen_clear()


score1 = 0
score2 = 0

Ques1= input("Question 1... Which of the following option leads to the portability & security of java? \n a.Byte is executed by JVM. \t b.The applet makes the Java code secure & portable. \n c.Use of exception handling. \t d.Dynamic binding between objects.")
if Ques1== "a":
    score1 += 1
    print ("Correct!")
    print ("Score:", score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
else:
    print ("Incorrect ! \n The answer is a.")
    print (" Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()


Ques2= input("Question 2.... Which of the following in not a Java features? \n a.Dynamic. \t b.Architecture Neutral. \n c.Use of Pointer. \t d.Object Oriented.")
if Ques2=="c":
    score1 += 1
    print ("Correct!")
    print ("Score:", score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
else:
    print ("Incorrect ! \n The answer is c.")
    print ("Score:", score1)
    print ("\n")
    time.sleep(2)
    screen_clear()


Ques3= input("Question 3.... The \u0021 article reffered to as a? \n a.Unicode escape sequence. \t b.Octal escape. \n c.Hexa decimal. \t d.Line feed.")
if Ques3=="a":
    score1 += 1
    print ("Correct!")
    print ("Score:", score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
else:
    print ("Incorrect ! \n The answer is a.")
    print ("Score:", score1)
    print ("\n")
    time.sleep(2)
    screen_clear()

Ques4= input("Question 4.... ________ is used to find & fix bugs in the Java program? \n a.JVM. \t b.JRE. \n c.JDK. \t d.JDB.")
if Ques4=="d":
    score1+= 1
    print ("Correct!")
    print ("Score:", score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
else:
    print ("Incorrect ! \n The answer is d.")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear(   )

Ques5= input("Question 5.... Which allows the removal of element from a collection? \n a.Enumeration. \t b.Iterator. \n c.Both. \t d.None of the above.")
if Ques5=="d":
    score1+= 1
    print ("Correct")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
else:
    print (" Incorrect ! \n The answer is d.")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()

Ques6= input("Question 6.... What is the return type of the hash code () method in the object class? \n a.Object. \t b.Int. \n c.Long. \t d.Void.")
if Ques6=="b":
    score1+= 1
    print ("Correct")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()

else:
    print ("Incorrect ! \n The answer is b.")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()

Ques7= input("Question 7.... Which of the following is a valid long literal? \n a.ABH8097. \t b.L00923. \n c.904423. \t d. OXnf029L.")
if Ques7=="d":
    score1+= 1
    print ("Correct")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
else:
    print ("Incorrect ! \n The answer is d.")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()

Ques8= input("Question 8.... What does the expression float a=35/0 return? \n a.0. \t b.Not a number. \n c.Infinity. \t d.Run time exception.")
if Ques8=="c":
    score1+= 1
    print ("Correct")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
else:
    print ("Incorrect ! \n The answer is c.")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()

Ques9= input ("Question 9.... Evaluate the following Java expression, if x=3,y=5,&,z=10:   \n\t\n ++z+y-y+z+x++.... \n a.24. \t b.23. \n c.20. \t d.25.")
if Ques9=="a":
    score1+= 1
    print ("Correct")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
else:
    print ("Incorrect ! \n The answer is a.")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()

Ques10= input("Question 10.... Which of the following creates a lists of 3 visible items & multiple selection abled? \n a. New list(false,3). \t b.New lists(3,true). \n c.New lists(true,3). \t d.New lists(3,false).")
if Ques10=="b":
    score1+= 1
    print ("Correct")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
else:
    print ("Incorrect ! \n The answer is b.")
    print ("Score:",score1)
    print ("\n")
    time.sleep(2)
    screen_clear()
oldscoreg=score1
oldscoren=10-score1
reportcard(oldscoreg,oldscoren)

if score1>=7:
    print ("!!!!!!!!!! CONGRATULATION !!!!! You are qualified for First level")
    print ("welcome to second level")


    
    Ques1= input("Question 1.... PHP stands for? \n a.PHP Hypertex Processor. \t b.PHP Hypertex Markup Processor. \n c.PHP Hypertex Markup Preprocessor. \t d.PHP Hypertex Preprocessor.")
    if Ques1=="d":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is d.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques2= input("Question 2.... PHP is an example __________ scripting language? \n a.Server-side. \t b.Client-side. \n c.Browser-side. \t d.In-side.")
    if Ques2=="a":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is a.")
        print ("Score:",score)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques3= input("Question 3.... Which of the following is not true? \n a.PHP can be used to develop web application. \t b.PHP makes a website dynamic. \n c.PHP application can not be compile. \t d.PHP can not be embedded into html.")
    if Ques3=="d":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is d.")
        print ("Score:",score1)
        print("\n")
        time.sleep(2)
        screen_clear()

    Ques4= input("Question 4.... who is known as the father of PHP? \n a. Rasmus Lerdorf. \t b.Willam Makepiece. \n c.Derk Kolkevi. \t d.Lists Barely.")
    if Ques4=="a":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is a.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques5= input("Question 5.... PHP scripts are enclosed within ________? \n a.<php>....</php>. \t b.<?php>....?>. \n c.?php....?php. \t d.<p>....</p>.")
    if Ques5=="b":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is b.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques6= input("Question 6.... Which of the following varibles is not a predefined variable? \n a.$get. \t b.$ask. \n c.$request. \t d.$post.")
    if Ques6=="b":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is b.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques7= input("Question 7.... When you need to obtain the ASCII value of a character which of the following function you apply in PHP? \n a.chr();. \t b.asc();. \n c.ord();. \t d.val();.")
    if Ques7=="c":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is c.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques8= input ("Question 8.... Which of the following methods sends input to a script via a URL? \n a.Get. \t b.Post. \n c.Both. \t d.None.")
    if Ques8=="a":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is a.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques9= input ("Question 9.... Which of the following function returns a text in title case from a variable? \n a.ucwords($var). \t b.upper($var). \n c.toupper($var). \t d.ucword($var).")
    if Ques9=="a":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is a.")
        print  ("Score:",score1)
        print("\n")
        time.sleep(2)
        screen_clear()

    Ques10= input ("Question 10.... Which of the following function returns the number of characters in a string variable? \n a.count($variable). \t b.len($variable). \n c.strcount($variable). \t d.strlen($variable).")
    if Ques10=="d":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is d.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()


if score1>=7:
    print ("!!!!!!!!CONGRATULATION!!!!!!!!! You are qualified for Second level")
    print ("Welcome To Third Level")


    Ques1= input ("Question 1.... HTML is what type of language? \n a.Scripting Language. \t b.Markup Language. \n c.Programming Language. \t d.Network Protocal.")
    if Ques1=="b":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is b.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques2= input ("Question 2.... HTML uses? \n a.User defind tags. \t b.Pre-specified tags. \n c.Fixed tags defined by the language. \t d.Tags only for linking.")
    if Ques2=="c":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is c.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques3= input ("Question 3.... The year in which HTML was first proposed? \n a.1990. \t b.1980. \n c.2000. \t d.1995.")
    if Ques3=="a":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! \n The answer is a.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques4= input ("Question 4.... Fundamental HTML Block is known as __________ . \n a.HTML Body. \t b.HTML Tag. \n c.HTML Attribute. \t d.HTML Element.")
    if Ques4=="b":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is b.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques5= input ("Question 5.... Apart from <b> tag, what other tag makes text bold ? \n a.<fat>. \t b.<stong>. \n c.<black>. \t d.<emp>.")
    if Ques5=="b":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! the answer is b.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques6= input ("Question 6.... What is the full form of HTML? \n a.HyperText Markup Language. \t b.Hyper Tech Markup Language. \n c.Hyper Teach Markup Language. \t d.none of these.")
    if Ques6=="a":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    else:
        print ("Incorrect ! The answer is a.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques7= input ("Question 7.... Who is known as the father of World Wide Web (WWW)? \n a.Robert Cailliau. \t b.Tim Thompson. \n c.Charles Darwin. \t d.Tim Berners-Lee.")
    if Ques7=="d":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is d.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques8= input ("Question 8.... What should be the first tag in any HTML document? \n a.<head>. \t b.<title>. \n c.<html> \t d.<document>.")
    if Ques8=="c":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is c.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques9= input ("Question 9.... How can you make a bulleted lists with number? \n a.<dl>. \t b.<ol>. \n c.<list>. \t d.<ul>.")
    if Ques9=="b":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is b.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques10= input ("Question 10.... What tag is used to display a picture in a HTML page? \n a.picture. \t b.image. \n c.img. \t d.src.")
    if Ques10=="c":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is c.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

if score1>=7:
    print ("!!!!!!CONGRATULATION!!!!!! You are qualified for fourth level")
    print ("Welcome To Fourth Level")



    Ques1= input ("Question 1.... One of the fault base testing techniques is ______. \n a.unit testing. \t b.beta testing. \n c.stress testing. \t d.mutation testing.")
    if Ques1=="d":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is d.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques2= input ("Question 2.... ER model shows the _____ . \n a.static view. \t b.functional view. \n c.dynamic view. \t d.all of the above.")
    if Ques2=="a":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is a.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques3= input ("Question 3.... The level at which the software uses scarce resoures is ____ . \n a.Reliability. \t b.Efficiency. \n c.Portability. \t d.All of the above.")
    if Ques3=="b":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print (" Incorrect ! The answer is b.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques4= input ("Question 4.... Which is not a step of requirement Engineering? \n a.Requirement elicitation. \t b.Requirement analysis. \n c.Requirement design. \t d.Requirement documentataion. ")
    if Ques4=="c":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is c.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques5= input ("Question 5.... Which is the most important feature of spiral model? \n a.Quality management. \t b.Risk management. \n c.Performance management. \t d.Efficiency management. ")
    if Ques5=="b":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is b.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques6= input ("Question 6.... What is the simplest model of software development paradigram? \n a.Spiral model. \t b.Big Bang model. \n c.V-model. \t d.Waterfall model. ")
    if Ques6=="d":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is d.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques7= input ("Question 7.... Software project management comprises of a number of activities which contain ____ . \n a.Project planning. \t b.Scope management. \n c.Project estimation. \t d.All of the above. ")
    if Ques7=="d":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is d.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques8= input ("Question 8.... Compilers, Editors software come under which type of software \n a.System software. \t b. Application software. \n c.Scientific software. \t d.None of the above. ")
    if Ques8=="a":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is a.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques9= input ("Question 9.... The worst type of coupling is. \n a.Data coupling. \t b.control coupling. \n c. stamp coupling. \t d.content coupling. ")
    if Ques9=="d":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is d.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()

    Ques10= input ("Question 10.... Mention any two indirect measures of product. \n a.quality. \t b.efficiency. \n c.accuracy. \t d.both A and B. ")
    if Ques10=="d":
        score1+=1
        print ("Correct")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
    else:
        print ("Incorrect ! The answer is d.")
        print ("Score:",score1)
        print ("\n")
        time.sleep(2)
        screen_clear()
else:
    exit
print ("\t\n\t\n****THANK YOU FOR PLAYING THIS GAME****\n\t\n\t")

def reportcard(sc,oldy,oldn):
    if(sc>=7):
        return
    else:
        print(name,"You are not qualified for next round\n")
        
    
    
    



