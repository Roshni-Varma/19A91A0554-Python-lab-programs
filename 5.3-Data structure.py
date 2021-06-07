#Implement a python script to count number of words in a string and reverse each word in a string at the same location.
s = input()
words = s.split(" ") 
newwords=[word[::-1] for word in words]
newsentence=" ".join(newwords)
print("Reversed String:") 
print(newsentence)
print(len(newwords))

"""output:Hello World
Reversed String:
olleH dlroW
2"""
