str1=input("enter string")
def string_alternative(str1):  #defining string alternative function
    final_String=(str1[::2])   #using slicing retrieving alternate characters in the string and assigning to final string
    return print(final_String)        #returning and printing final string
string_alternative(str1)  #calling function string_alternative