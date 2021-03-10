#function initialisation

func = input("the function: ") # input
mainList= []
mekademim = []
hezkot = []
derivativeList = []
# transformes the string to list

for st in func:
    try:
        mainList.append(int(st))
    except:
        mainList.append(st)

flag = False
i = 0
# hezkot and mekadmim
while(flag == False):
    if mainList[i] == '^':
        hezkot.append(mainList[i+1])

    if mainList[i] == "x" or mainList[i] == "X":
            if(type(mainList[abs(i-1)]) == int):
                mekademim.append(mainList[i-1])

    i+=1
    if i == len(mainList):
        flag = True

def derivative(mainList): #finds derivative, returns the list
    derivativeList = []
    i = 0
    flag = False
    while(flag == False):
        if (i == len(mainList)):
            return derivativeList
        if mainList[i] == '^':
            if(type(mainList[abs(i-2)])!= int):
                derivativeList.append(1*mainList[i+1]) #mekadem
            else:
                derivativeList.append(mainList[i-2]*mainList[i+1]) #mekadem
            derivativeList.append('x')
            derivativeList.append('^')
            derivativeList.append(mainList[i+1]-1) #hezka
            try:
                if(mainList[i+2] == 'x' or mainList[i+3] == 'x' or mainList[i+4] == 'x' or mainList[i+1] ==  'X' or mainList[i+2] ==  'X'or mainList[i+3] ==  'X' or mainList[i+4] ==  'X'):
                    derivativeList.append(mainList[i+2]) #sign
            except:
                print("no more")


        if(mainList[i] == 'x' or mainList[i] == 'X'):
            if((i+1)>len(mainList) or (i+1) == len(mainList)): #we are in the end
                if(type(mainList[i-1])!=int):
                    derivativeList.append(1)
                else:
                    derivativeList.append(mainList[i-1])
        i+=1

derivativeList = derivative(mainList)





print("main list =")
print(mainList)
print( "^ = ")
print(hezkot)
print("||X = ")
print(mekademim)
print("Derivative = " )
print(derivativeList)

