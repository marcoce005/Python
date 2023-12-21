## if    

anni = int(input("Inserire anni:\t"))

if anni >= 18 :                    ## if
    print ("sei maggiorenne")
elif anni <= 0 :                    ## else if
    print ("Non sei nato")
else :                              ## else
    print ("sei minorenne")


## and or not ecc...

temp = int (input ("inserire la temperatura:\t"))

if temp > 0 and temp < 30 :         ## and 
    print ("ottima temp")
elif not (temp == 100) :                ## not
    print ("non vai a fuoco")           
elif temp < 0 or temp > 30 :            ## or
    print ("Fa freddo o fa caldo??")