heights=[96,106, 156, 148]   #list with heights of customers in inches
print("heights of customers in inches is",heights)  #printimg them in inches
newlist=[each_value_in_list*2.54 for each_value_in_list in heights]  #for each value in heights list , converting inches to centimetres using formula
print("height of customers in centimetres is ",newlist)  #printing ne list in centimetres