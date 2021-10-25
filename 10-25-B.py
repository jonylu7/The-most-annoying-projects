e = input("Emoji")
alphabet = list(input("Alphabet"))
outarr=[]
for i in alphabet:
    j=""
    if(i=="1"):
        for _ in range(5):
            j+=e+"\n"
    elif(i=="2"):
        for i in range(5):
            j+=e
        j+="\n"
        for i in range(5):
            j+="___________"+e+"\n"
        j+="\n"
        for i in range(5):
            j+=e
        j+="\n"
        for _ in range(5):
            j+=e+"\n"
        for i in range(5):
            j+=e
    elif(i=="3"):
        for i in range(6):
            j+=e
        j+="\n"

        for i in range(5):
            j+="___________"+e+"\n"

        for i in range(6):
            j+=e
        j+="\n"

        for i in range(5):
            j+="___________"+e+"\n"
        for i in range(6):
            j+=e     
    elif(i=="4"):
        for i in range(5):
            j+=e+"__________"+e+"\n"
        for i in range(6):
            j+=e
        j+="\n"
        for i in range(5):
            j+="_____________"+e+"\n"
    elif(i=="5"):
        for i in range(6):
            j+=e
        j+="\n"

        for i in range(5):
            j+=e+"___________"+"\n"

        for i in range(6):
            j+=e
        j+="\n"

        for i in range(5):
            j+="___________"+e+"\n"
        
        for i in range(6):
            j+=e 
    elif(i=="6"):
        for i in range(6):
            j+=e
        j+="\n"

        for i in range(5):
            j+=e+"___________"+"\n"

        for i in range(6):
            j+=e
        j+="\n"

        for i in range(5):
            j+=e+"__________"+e+"\n"
        
        for i in range(6):
            j+=e 
    elif(i=="7"):
        for i in range(5):
            j+=e
        j+="\n"

        for i in range(8):
            j+="___________"+e+"\n"

    elif(i=="8"):
        for i in range(6):
            j+=e
        j+="\n"

        for i in range(5):
            j+=e+"__________"+e+"\n"
        
        for i in range(6):
            j+=e 

        j+="\n"

        for i in range(5):
            j+=e+"__________"+e+"\n"
        
        for i in range(6):
            j+=e 
    
    elif(i=="9"):
        for i in range(6):
            j+=e
        j+="\n"

        for i in range(5):
            j+=e+"__________"+e+"\n"
        
        for i in range(6):
            j+=e
        
        j+="\n"

        for i in range(8):
            j+="_____________"+e+"\n"
    elif(i=="0"):
        for i in range(6):
            j+=e
        j+="\n"

        for i in range(9):
            j+=e+"__________"+e+"\n"
        
        for i in range(6):
            j+=e 
    elif(i=="A"):
        j+="  "+e+"   "+"\n"
        j+="  "+e+" "+e+" "


    outarr.append(j)

for i in outarr:
    print("\n")
    print(i)
