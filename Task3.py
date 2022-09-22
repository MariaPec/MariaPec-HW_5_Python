
def StringComp(myString): #Функция rle сжатия
    myStringComp = ""
    count = 0
    i = 0
    item = myString[0]
    while i < len(myString):
    	if myString[i] == item:
    		count += 1
    		i += 1
    	else:
    	    myStringComp += str(count)
    	    myStringComp += item
    	    count = 0
    	    item = myString[i]
    myStringComp += str(count)
    myStringComp += item
    return(myStringComp)

#Работаем с файлами input1 и output1
with open("input1.txt", "r") as file1:
   for line in file1:
      myString = line.strip()

file2 = open('output1.txt', 'w')
file2.write(StringComp(myString))
file2.close()

#Для проверки выведу в консоль
print(myString)
print(StringComp(myString))

def StringUnp(myStringComp): #Функция rle распаковки
    myStringUnp = ""
    i = 0
    
    while i < len(myStringComp) - 1:
    	count = int(myStringComp[i])
    	item = myStringComp[i + 1]
    	myStringUnp += item * count
    	i += 2
    return(myStringUnp)

#Работаем с файлами input2 и output2
with open("input2.txt", "r") as file3:
   for line in file3:
      myString2 = line.strip()

file4 = open('output2.txt', 'w')
file4.write(StringUnp(myString2))
file4.close()

#Для проверки выведу в консоль
print(myString2)
print(StringUnp(myString2))
