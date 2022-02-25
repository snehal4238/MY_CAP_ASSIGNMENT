
#area of circle
r= float(input("input radius of circle :"))

f= float(3.14159*r**2)
a= print("The area of circle with radius %f is : " %r,+f)

#find the extension

f_name= str(input("input a filename :"))
f_extension= f_name.split(".") #split()method use to split string into a list
print("The Extension of the file is: ", f_extension[-1]) #[-1] to get the last element of list after splitting filename

