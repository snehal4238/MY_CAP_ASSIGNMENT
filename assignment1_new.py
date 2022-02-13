
#area of circle
r= float(input("input radius of circle :"))

f= float(3.14159*r**2)
a= print("The area of circle with radius %f is : " %r,+f)

#find the extension

f_name= str(input("input a filename :"))

# function to return the file extension
f_extension= f_name.split(".")
print("The Extension of the file is: "+ repr(f_extension[-1]))

