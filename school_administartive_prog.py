import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","E-mail ID"])

        writer.writerow(info_list)
if __name__=='__main__':
    terms = True
    student_num = 1

    while(terms):
        student_info =input("enter sudent information for student # {} in the following format(name Age Contact_Number E-mail ID):".format(student_num))

        #split
        student_info_list=student_info.split(' ')
        
        print("\nThe entered information is :\nName: {}\nAge: {}\nContact_Number: {}\nE-mail ID : {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        
        input_check = input("is the entered information is correct(yes/no):")
        
        if input_check=="yes":
            write_into_csv(student_info_list)
            terms_check =input("enter (yes/no) if  you want to enter information for another student:")
            if terms_check == "yes":
                terms = True
                student_num = student_num + 1
            elif terms_check == "no":
                terms = False
        elif input_check == "no":
            print("\nplease re-enter the values!")

        

    

    

    
    

    

