f=open("input.txt","w")  #opening file with write mode
f.write("Python Course\n")  #writing first line
f.write(" Deep Learning Course") #writing secomd line into file
f.close() #closing file after writing
f=open("input.txt","r") #opening file with read mode
print(f.read()) #reading that file
f.close()  # closing file after freading

from collections import Counter  #importing Counter from collections library
def count_words(filename):   #defining count_words function by taking file as argument
    with open(filename) as f:
        return Counter(f.read().split())  #reading the input file and split every word in file and count words

with open("output.txt","a") as f:  #opening new outputfile and sending output of returned function to output file
    print("Number of words in the file:\n", count_words("input.txt"))     #printing output