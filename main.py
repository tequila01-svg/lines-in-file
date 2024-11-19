#program to count number of lines in this file
#opening a file
file=open("sample.txt","r")
counter = 1

#reading the content of the file
content = file.read()
#splitting content into lines 
# and storing in list
CoList= content.split("\n")

for i in CoList:
    if i:
        counter +=1
print("this is the number of lines in the file")
print(counter)