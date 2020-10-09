

c='Congratulations!!!'        #a variable that will be used for displaying congratulations message

dot=" - "

def styler(string):  #This can add a lil' bit of interactiveness to the program.
    print(string*50)

def convert_to_hundred(mark,f):   #defining a function that will convert obtained marks into range of 100 depending upon full mark for that subject too
    result=(mark/f)*100
    return result

def gpa(a):   #define a function to assign a grade point based on obtained marks(converted into 100)
    '''
    INPUT:MARKS IN EACH SUBJECT
    OUTPUT: GRADE POINT IN EACH SUBJECT
    '''
    if 100>=a>=90:
        return 4.0
    elif 90>a>=80:
        return 3.6
    elif 80>a>=70:
        return 3.2
    elif 70>a>=60:
        return 2.8
    elif 60>a>=50:
        return 2.4
    elif 50>a>=40:
        return 2.0
    elif 40>a>=30:
        return 1.6
    elif 30>a>=20:
        return 1.2
    elif 20>a>=0:
        return 0.8
    else:
        return a
        
consol='\t\t\t\twhich is too low\n\t\t\t\tsorry! you need to prepare well.'   #a var. that will be used if the user's grade/percentage is below pass marks range

def gpa_in_range(num):    #check whether the gpa obtained is within range of 0 to 4 or not, else display messgae of user input error
    if num<=4 and num>=0:
        print("\t\t\t\tYour GPA  is :-   {}".format(num))
    else:
        print()
        print(dot*50)
        print("\t\t\t\t****USER INPUT ERROR****")
        print("\t\t\t\tsorry!!!")
        print()
        print("\t\t\t\tyour obtained marks is greater than full marks\n\t\t\t\tplease, check your input")
        print()
        print(dot*50)
        print()
    


def find_grade(a):   # function  to display letter grade based on grade point
    '''input: marks
    output: grade'''
    c='congratulations!!!!!'
    if 4.0>=a>3.6:
        print("\t\t\t\t %s your grade is A+" %(c))
    elif 3.6>=a>3.2:
        print("\t\t\t\t %s your grade is A" %(c))
    elif 3.2>=a>2.8:
        print("\t\t\t\t %s your grade is B+" %(c))
    elif 2.8>=a>2.4:
        print("\t\t\t\t your grade is B")
    elif 2.4>=a>2.0:
        print("\t\t\t\t your grade is C+")
    elif 2.0>=a>=1.6:
        print("\t\t\t\t your grade is C")
    elif 1.6>=a>1.2:
        print("\t\t\t\t Your grade is 'D+' %s " %(consol))
    elif 1.2>=a>0.8:
        print("\t\t\t\t Your grade is 'D' %s" %(consol))
    elif 0.8>=a>0:
        print("\t\t\t\t Your grade is 'E' %s " %(consol))
   



        
def percentage_dialogue():   #function to display percentage 
    if PER>=40:
        styler(dot)
        print()
        print("\t\t\t\t\tCONGRATULATIONS!!!\n\t\t\tYour total obtained marks is:-\t{o}\n\t\t\tYour obtained percentage is:-\t{p}%\n".format(o=OBT,p=PER))
        print()
        styler(dot)
    else:
        styler(dot)
        print()
        print("\t\t\tYour total obtained marks is:\t{o}\n\t\t\tYour obtained percentage is:-\t{p}%\n\t\t\t\t*****Study Well*****\n".format(o=OBT,p=PER))
        styler(dot)
        print()
    print("\n")
    
program_active=True  #creating a variable that declares program being active, this will be main trick to run the proram again in same window if the user wishes to

while program_active:
    #main program:
    print()
    
    print()
    print()
    print()
    print()
    print()
    print("||---------------------------------------------------------------------------------------------------------------------------------------||")
    print("\n")
    print("\n")
    print("\t\t****This is simplest python program to calculate your obtained marks,perentage and grades too****")
    print("\n\t\t\t\t****DEVELOPED BY-ASHIM PAUDEL****\n")
    print("\t\t\t\t**Follow the instructions below**\n")
    print("\n")
    print("\t\t\t\t*****FIRSTLY, INPUT YOUR OBTAINED MARKS IN EACH SUBJECTS*****\n")
    print("Mathematics:")  
    math=float(eval(input()))
    print("Science:") 
    sci=float(eval(input()))
    print("English:") 
    eng=float(eval(input()))
    print("Nepali:")
    nep=float(eval(input()))
    print("Social:")
    soc=float(eval(input()))
    print("EHP:")
    ehp=float(eval(input()))
    print("Optional 1st:")
    opt1=float(eval(input()))
    print("Optional 2nd:")
    opt2=float(eval(input()))
    print("\n")
   

    styler(dot)
    print()
    print("\t\t\t\tIs full marks for all subjects same??\n\t\t\t\t(y/n)")
    com1 = input()
    com1=com1[0].upper()

    
    while com1!='Y' and com1!='N':    #for exception handling and to keep in track of user's input
        com1=input("\t\t\t\tSorry!!! couldnot recognize your command,\n\t\t\t\tyou must say (y/n)\n")
        com1=com1[0].upper()

    if com1 == 'Y':
        print("\t\t\t\twhat is that common full marks?")     #for exception handling and to keep in track of user's input
        while True:
            f=input()
            try:
                f=int(f)
                break
            except ValueError:
                print("\t\t\t\t'%s' is not an integer!\n\t\t\t\tplease, type that common full marks again." %(f))
        
        print()
        print()
        
        TOT=f*8
        OBT = float(math+soc+sci+eng+nep+ehp+opt1+opt2)
        PER=(OBT/TOT)*100
        
        percentage_dialogue()
   
        a=PER
    
    
        print()
        styler(dot)
        print()
        print("\t\t\t\tDo you want to check your grades too?\n\t\t\t\t***'say y/n'***\n\n")
        d=input()
        d=d[0].upper()
        while d!='Y' and d!='N':
            d=input("\t\t\t\tSorry!!!\n\t\t\t\tcouldnot recognize your command,\n\t\t\t\tsay (y/n)\n")    #for exception handling and to keep in track of user's input
            d=d[0].upper()
        if d=='Y':
            math1=gpa(convert_to_hundred(math,f))
            sci1=gpa(convert_to_hundred(sci,f))
            eng1=gpa(convert_to_hundred(eng,f))
            nep1=gpa(convert_to_hundred(nep,f))
            soc1=gpa(convert_to_hundred(soc,f))
            ehp1=gpa(convert_to_hundred(ehp,f))
            opt1_1=gpa(convert_to_hundred(opt1,f))
            opt2_1=gpa(convert_to_hundred(opt2,f))

            TOT_GPA=(math1+sci1+eng1+nep1+soc1+ehp1+opt1_1+opt2_1)/8
            
            gpa_in_range(TOT_GPA)
            
            find_grade(TOT_GPA)
            
        elif d=='N':
            print("\n")
        else:
            print("Sorry couldn't recognize your command '%s' sir" %(d))
            
    elif com1=='N':   #if full marks is not same for all subjects
        print()
        styler(dot)
        print("\t\t\t\t *****NOW, INPUT FULL MARKS FOR EACH SUBJECTS*****")
        styler(dot)
        print("\n")
        print("Mathematics:")  
        matha=float(eval(input()))
        print("Science:") 
        scia=float(eval(input()))
        print("English:") 
        enga=float(eval(input()))
        print("Nepali:")
        nepa=float(eval(input()))
        print("Social:")
        soca=float(eval(input()))
        print("EHP:")
        ehpa=float(eval(input()))
        print("Optional 1st:")
        opt1a=float(eval(input()))
        print("Optional 2nd:")
        opt2a=float(eval(input()))
        print("\n")
        
        OBT = float(math+soc+sci+eng+nep+ehp+opt1+opt2)
        TOT = float(matha+scia+enga+nepa+soca+ehpa+opt1a+opt2a)
        PER=(OBT/TOT)*100
        
        percentage_dialogue()

        a=PER
        
        print("\t\t\t\tDo you want to check your grades too?\n\t\t\t\t***say 'y/n'***\n\n")
        d=input()
        d=d[0].upper()
        while d!='Y' and d!='N':
            d=input("\t\t\t\tSorry!!! \n\t\t\t\tcouldnot recognize your command,\n\t\t\t\tsay (y/n)\n")
            d=d[0].upper()
            
        if d=='Y':
            math1=gpa(convert_to_hundred(math,matha))
            sci1=gpa(convert_to_hundred(sci,scia))
            eng1=gpa(convert_to_hundred(eng,enga))
            nep1=gpa(convert_to_hundred(nep,nepa))
            soc1=gpa(convert_to_hundred(soc,soca))
            ehp1=gpa(convert_to_hundred(ehp,ehpa))
            opt1_1=gpa(convert_to_hundred(opt1,opt1a))
            opt2_1=gpa(convert_to_hundred(opt2,opt2a))

            TOT_GPA=(math1+sci1+eng1+nep1+soc1+ehp1+opt1_1+opt2_1)/8
            
            gpa_in_range(TOT_GPA)
        
            find_grade(TOT_GPA)
        elif d=='N':
            print("\n")
            
            
        #program ends
        
        #restart prompt
    print()
    styler(dot)
    print()
    
    restart=input('\n\n\t\t\t\tHey ! wanna run this program again?(y/n) \n')
    while restart[0].upper()!='Y' and restart[0].upper()!='N':
        print("\t\t\t\tSorry '{}' was an invalid input. Say (y/n)".format(restart))
        restart=input()
    if restart.upper().startswith('N'):
        program_active=False    
        print("\n")
        print()
        print()
        print()
        print()
        
        
        styler(dot) 
        # feed back session
        print("\n\t\t\t\tDid you enjoy this program??:(y/n)\n")
        feedback=input()
        feedback=feedback[0].upper()
        while feedback!='Y' and feedback!='N':
            feedback=input("\t\t\tSorry!!! you must leave at least one feed back\n\t\t\t\tDid you enjoy this program??:(y/n)\n")
            feedback=feedback[0].upper()
        if feedback=='Y':
            print("\t\t\t\tThankyou for your response!!!")
        else:
            print("\t\t\t\tThankyou a lot\n\t\t\t\tWe will improve this program further.")
        print()
        styler(dot)
        
        input("\t\t\t\t\tPress any to exit\n")
