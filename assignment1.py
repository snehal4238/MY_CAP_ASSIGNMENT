#area of circle
r= float(input("input radius of circle :"))

f= float(3.14159*r**2)
a= print("The area of circle with radius %f is : " %r,+f)

#find the extension

f_name= str(input("input a filename :"))
if f_name.endswith(".py"):
    print("the extension of the file is python")
elif f_name.endswith("c"):
    print("the extension of the file is c")
elif f_name.endswith(".txt"):
    print("the extension of the file is textfile")
elif f_name.endswith(".pdf"):
    print("the extension of the file is pdf")
elif f_name.endswith(".cs"):
    print("the extension of the file is c#")
elif f_name.endswith(".java"):
    print("the extension of the file is java")
elif f_name.endswith(".html"):
    print("the extension of the file is html")
elif f_name.endswith(".css"):
    print("the extension of the file is CSS")
else:
    print("the extension of the file is image")
