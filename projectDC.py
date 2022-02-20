"""
   This program save user course in dictionary using add_course(course) function, add score
   of a course using add_score(cours) function, removes course by using 
   remove_course(course) function, and lastly displays user score, score date and
   course by using display_gradebook(course) function. All of the functions will be
   functioning by the user choice in main() function.
   
   Author: Dongseok Cho (Danny Cho)
"""
import pickle
course = {}
import datetime #importing datetime
from graphics import *

def add_course(course):
    """
       This function prompts user a course name, the activity names in the course,
       and weight of an activity. If the user enters existing course name or a 
       empty string the program will give error message and will keep prompt till enter
       correctly. For activity name user can enter any type or words. If the activity
       is empty then the function will stop prompting activity. Weight will only except
       numbers. At the end all data will be saved in course{} dictionary.
       
       Parameter:
       course:dictionary
              empty dictionary to save prompted values
       
       Return:
       None
    """
    course_name = input("Course name: ") # prompt user for course name
    course_name = add_course_error_name(course_name,course) # check if the name is in dictionary or it is empty
    print("Evaluation:") #print out 'Evaluation'
    activity_weight = {} #empty dictionary for activity
    
    get_activity(activity_weight)

    course[course_name] = activity_weight #adding course and activities to course dictionary
    return



#-------------------------------------------------------------------------------
def add_course_error_name(course_name,course):
    """
       This function check if the course_name inputed already exist in course{}
       dictionary and if it is empty. If it is empty and already exist in the 
       dictionary will keep prompt user for a new course_name.
       
       Parameter:
       course_name:str
                  initial user input for course_name
       course:dictionary
             saved dictionary with course information
       
       Return:
       str
          the name of a course that is not in dictionary
    """
    while (True): # loop till break
        if course_name in list(course.keys()):# checking if course name is in coures keys
            print("Error: the course name already exists")#if so print error message
        elif course_name == "":#checking if course name is empty
            print("Error: the course name cannot be empty")#if so print error message
        else:
            break# break loop none of above 
        course_name = input("Course name: ") # reprompting if error
    
    return course_name # returning correct course_name





#-------------------------------------------------------------------------------

def get_activity(activity_weight):
    """
       This function input user for a name of an activity in the course. If user
       enter empty string, the program loop back to beginning. If the activity
       already exist, then will give a error message and reprompt the user.
       At the end activity and weight will be saved in a dictionary.
       
       Parameter:
       activity_weight:dict
                 Empty dicionary
       
       Return:
       None
    """
    while (True): # loop till break
        activity = input("  Activity: ") # prompt user for activity name
        weight_date_percent = {} #empty dictionary for weight, date, and score percent
        
        if activity in activity_weight.keys():# check if activity is in activity_keys()
            print("  Error: the activity name already exists")# if does giving error message
        
        elif activity != "":# checking if activity is not empty
            weight = get_weight()
            
            weight_date_percent["Weight"] = weight
    
            activity_weight[activity] = weight_date_percent            
        
        elif activity == "": # checking if activity is empty
            break #if so stop    

#-------------------------------------------------------------------------------

def get_weight():
    """
       This function input user for a weight of an activity. If weight is invalid
       the function will keep prompt the user for weight. 
       
       Parameter:
       None
       
       Return:
       float:
            the weight input
    """
    weight = input("  Weight: ") # Prompt user for weight

    try:
        weight = float(weight)
    except:
        print("  Error: the provided weight is invalid")
        weight = get_weight()
    
    return weight

#-------------------------------------------------------------------------------



def add_score(course):
    """
       This function prompts user for course activity score and the completion date.
       If the user enters "?" when prompted for course name. The function will 
       give a list of course in course{} dictionary. If a user enters "/" when 
       prompted for activity. The function will give a list of activity in the
       course that user chose. For course name and activity name if user entered
       name that is not existing in the dictionary, then the function will keep
       prompt user. At the end the score and the completion date will be saved
       in dictionary under the activity user chosen. If user enters empty course
       or empty activity. Break out of the function and go back to the menu.
       
       Parameter:
       course:dictionary
              saved dictionary with course information
       Return:
       none
    """
    course_lst = list(course.keys()) #list of course name
    course_lst.sort()#sorting course name
    name_course = input("Course (? for list): ")#prompting course name
    name_course = score_course_error(name_course,course_lst)# error checking course name
    
    if name_course in course_lst:#checking if name_course is in course_lst
            activity_lst = list(course[name_course].keys()) #list of activity
            activity_lst.sort()#sorting activity list
            
            activity = get_score_activity(activity_lst)
            
            if activity != "":#if activity is not empty prompt date and score. add date and score to dictionary
                
                complete_date = date_completion()
                
                score = get_score()
            
                course[name_course][activity]["Score"] = float(score)
                course[name_course][activity]["Date"]= complete_date
    return
#-------------------------------------------------------------------------------
def score_course_error(name_course,course_lst):
    """
       This function check if name of the course is in the course_lst. If the 
       name is not in the course_lst, then print out the list of courses and 
       reprompt user. If enter '?', then print out the list of courses and repormpt
       user. If user enter empty. Break out of function.
       
       Parameter:
       name_course:str
                   user inputed course name
       course_lst:list
                 list of courses in dictionary
                 
       Return:
       str
          name of course in dictionary
    """
    while(True):
        if name_course == "?":
            print(f"  Courses: {', '.join(course_lst)}")
        elif name_course not in course_lst:
            if name_course != "":
                print("  Courses:", ", ".join(course_lst))
        else:
            break
        if name_course == "":
            break
        
        name_course = input("Course (? for list): ")
    
    return name_course

#-------------------------------------------------------------------------------


def get_score_activity(activity_lst):
    """
       This function prompts user for an activity name. Wrong name will print a 
       error message and will reprompt the user.
       
       Parameter:
       activity_lst: list
                   list of activity in a course
       
       Return:
       str:
          a name of activity.
    """
    while(True):#loop till break
        activity = input("Activity (? for list): ")#prompting user for activity
        if activity == "?":#checking if activity is '?'
            print("  Activities:", ", ".join(activity_lst))# if so print list of activities
        elif activity not in activity_lst:#checking if input is in activity_lst
            if activity != "":#checking if activity is not empty
                print("  Activities:", ", ".join(activity_lst))#if so print out list of activities.
        else:
            break#break out of loop
        if activity == "":#if activity is empty break out of loop
            break
    return activity

#-------------------------------------------------------------------------------
def date_completion():
    """
       This function prompt user for completion date of a course and turn it in 
       to date time object.
       
       Parameter:
       None
       
       Return:
       date time:
                the completion date for a course
    """
    input_date = input("Completed date (YYYY-MM-DD): ")
    
    complete_date = date_time(input_date) 
    
    return complete_date

#-------------------------------------------------------------------------------

def date_time(input_date):
    """
       This function changes the user inputed date vaule to Python's datetime
       libarry.
       
       Parameter:
       input_date:str
                  user inputed completion date
       Return:
       datetime
               completion date in datetime 
    """
    lst_date = input_date.split("-")
    try:
        complete_date = datetime.date(int(lst_date[0]),int(lst_date[1]),int(lst_date[2]))
    except:
        print("Error: the provided date is invalid")
        complete_date = date_completion()
    
    return complete_date


#-------------------------------------------------------------------------------

def get_score():
    """
       This function prompt user for obtained score of a course. Wrong value will
       print out error message and reprompt the user.
       
       Parameter:
       None
       
       Return:
       float:
             percent of score in float
    """
    score = input("Score (%): ")
    try:
        score = float(score)
    except:
        print("Error: the provided score is invalid")
        score = get_score()

    return score

#-------------------------------------------------------------------------------


def remove_course(course):
    """
       This function removes a course in course{} dictionary. If user input '?'
       or wrong course the function will give out the list of courses in 
       dictionary. If user enters empty string, then will be break out of function
       and go back to the menu option. If user enter correct course name. The course
       will be removed.
       
       Parameter:
       course:dictionary
              saved dictionary with course information
       
       Return:
       None
    """
    while(True):
        remove_course = input("Course (? for list): ")
        
        if remove_course == "?":
            print("  Courses:", ", ".join(list(course.keys())))
        
        elif remove_course not in course.keys():
            if remove_course != "":
                print("  Courses:", ", ".join(list(course.keys())))
        
        elif remove_course in course.keys():
            course.pop(remove_course)
            break
        
        if remove_course == "":
            break
    return
    



#-------------------------------------------------------------------------------




def display_gradebook(course):
    """
       This function display courses, activities, scores, and score dates in the
       course{} dictionary.
       
       Parameter:
       course: dictionary
              saved dictionary with course information
       Return:
       None
    """
    
    course_lst = list(course.keys())
    course_lst.sort()
    
    for i in course_lst:# print out all the course
        print("\nCourse:", i)
        activity_lst = list(course[i].keys())
        activity_lst.sort()
        
        for activity in activity_lst:#print out all the activity and weight
            print("  Activity:",activity, "(Weight:", course[i][activity]["Weight"], end = "")
            print(")")
            score_lst = course[i][activity].keys()
            
            if "Score" in score_lst:# if score exists print out score and date
                print("    Score:",course[i][activity]["Score"],end=" ")
                print("(Completed:", course[i][activity]["Date"], end="")
                print(")")
        
        
        
#-------------------------------------------------------------------------------



def menu():
    """
       This function print out the options for user.
       Parameter:
       None
       Return:
       None
    """
    print("""=== Gradebook ===
(1) Add course
(2) Add score
(3) Remove course
(4) Display gradebook

(5) Calculate possible outcomes
(6) Calculate GPA

(7) Plot scores

(0) Quit""")
 


#------------------------------------------------------------------------------- 


    
def main():
    """
       This function displays menu and prompt user to choose an option. If input
       is not correct the function will prompt user till get the right input.
       What ever command user choose this function will run corresponding options.
       Lastly if user choose 0, the function will stop and not going to prompt 
       user again. So this function will repeat till user enter 0.
       
       Parameter:
       None
       
       Return:
       None
    """
    print("working")
    course = {}#empty course dictionary
    try:
        course = open_pickle("gradebook.p")
    except:
        print(f"Failed to load data from gradebook.p")
    while(True):
        print()
        menu()
        command = input("\nEnter command: ")
        command = command_error(command)#error check if command is right value
        print()
        command_operator(command,course) #command operator 1 to 7
        
        if command == "0":#if zero stop
            write_file(course)
            break
        
#------------------------------------------------------------------------------- 
        
def command_error(command):
    """
       This function check if user endtered command is in between setted range.
       If not in range and wrong value, will reprompt the user.
       
       Parameter:
       command: str
               user entered value
        
       Return:
       str:
           correct command value
    """
    while (True):# checking if user choice < 0 or choice > 4
        if command.isdigit() == False:
            command = input("Enter command: ")
        elif int(command) < 0 or int(command) > 7:
            command = input("Enter command: ")
        else:
            break
    return command
#-------------------------------------------------------------------------------
def command_operator(command,course):
    """
       This function operates user inputed command. 
       
       Parameter:
       command:int
               options choice
       course:dict
              course dictionary
       
       Return:
       None
    """
    if command == "1":
        add_course(course)
    elif command == "2":
        add_score(course)
    elif command == "3":
        remove_course(course)
    elif command == "4":
        display_gradebook(course)
    elif command == "5":
        total = 0
        name_course = course_calculate_outcome(course)
        command_five(name_course,course,total)
    elif command == "6":
        gpa(course)
    elif command == "7":
        command_seven(course)    
#-------------------------------------------------------------------------------       
def command_five(name_course,course,total):
    """
       This function help command_operate(course,command) if user command is five. 
       Displays worst, expected,and best case of course.
       
       Parameter:
       name_course: str
                name of cousre
       course: dict
              course saved in dictionary
       total: int
             initial total
       
       Return:
       None
    """
    if name_course != "":
        worst_case(name_course,course,total)
        expected_case(name_course,course,total)
        best_case(course,name_course,total)    
#-------------------------------------------------------------------------------

def command_seven(course):
    """
       This function helps command_operate(course,command) if user input is 7.
       Display chart of score and score date.
       
       Parameter
       course:dict
              dictonary of course
       
       Return:
       None
    """
    dates,name_course = list_of_date(course)
    if name_course == None:
        None
    elif dates == []:
        print("Error: course does not have graded activities")
    elif name_course != None:
        first_date(dates)
        last_date(dates)
        window(name_course,dates,course)    
#-------------------------------------------------------------------------------
def write_file(course):
    """
       This function saves data enter in this program with pickle. If failed
       to save dat, print out fail meassage. If data saved, print out success
       message.
       
       Parameter:
       course:dict
             course data dictionary
       Return:
       None
       
    """
    try:
        pickle_file =  open("gradebook.p", "wb")
        print(f"Data saved in gradebook.p")
    except:
        print(f"Failed to save data in gradebook.p")
        return
    
    pickle.dump(course,pickle_file)
    pickle_file.close()
    
#-------------------------------------------------------------------------------

def open_pickle(file_name):
    """
       This function loads data from saved pickle file. Successful load will
       print data is loaded.
       
       Parameter:
       file_name: str
                user entered file name
       Return:
       dict:
           course dictionary.
    """
    
    pickle_file = open(file_name,"rb")
    
    course = pickle.load(pickle_file)
    
    pickle_file.close()
    
    print(f"Data loaded from {file_name}")
    
    return course
#-------------------------------------------------------------------------------
def course_calculate_outcome(course):
    """
       This function prompt user for a name of a course to calculate outcome
       of a course percentages.
       
       Parameter:
       course:dict
             dictionary with course data
       
       Return:
       str:
           Name of course
    """
    course_lst = list(course.keys()) #list of course name
    course_lst.sort()#sorting course name
    name_course = input("Course (? for list): ")#prompting course name
    name_course = score_course_error(name_course,course_lst) 
    total = 0
    return name_course
#-------------------------------------------------------------------------------
def worst_case(name_course,course,total):    
    """
       This function calculates a worst case of a course mark.
       
       Parameter:
       name_course:str
                 name of course
       course:dict
               course data dictionary
       total: int
             initial total(0)
       
       Return:
       None
    """
    for i in course[name_course]:
        lst = list(course[name_course][i])
        if "Score" in lst:
            total += ( course[name_course][i]["Score"]* course[name_course][i]["Weight"]) / 100    
        elif "Score" not in lst:
            total += 0
    
    score = (total/100)*100    
    print(f"  Worst case:   {score: .1f} ({letter_grade(score)})")
#-------------------------------------------------------------------------------
def expected_case(name_course,course,total):    
    """
       This function calculates a expected case of a course mark.
       
       Parameter:
       name_course:str
                 name of course
       course:dict
               course data dictionary
       total: int
             initial total(0)
       
       Return:
       None 
    """
    score = average_score(name_course,course,total) #average entered score
    for i in course[name_course]:
        lst = list(course[name_course][i])
        if "Score" in lst:
            total += (course[name_course][i]["Score"] * course[name_course][i]["Weight"])/100
        else: 
            total += (score * course[name_course][i]["Weight"])/100
    
    score = total
    print(f"  Expected case:{score: .1f} ({letter_grade(score)})")
#-------------------------------------------------------------------------------
def average_score(name_course,course,total):
    """
       This function averages the entered score for the expected score.
       
       Parameter:
       name_course:str
                 name of course
       course:dict
               course data dictionary
       total: int
             initial total(0)
       
       Return:
       int:
           the average score
    """
    score = 0
    count = 0
    for i in course[name_course]:
        lst = list(course[name_course][i])
        if "Score" in lst:
            score += course[name_course][i]["Score"]
            count += 1
    if count != 0:
        score = score/count
    else:
        score = 0    
    return score
#-------------------------------------------------------------------------------
def best_case(course,name_course,total):
    """
       This function calculates a best case of a course mark.
       
       Parameter:
       name_course:str
                 name of course
       course:dict
               course data dictionary
       total: int
             initial total(0)
       
       Return:
       None
    """
    
    score = 0
    for i in course[name_course]:
        lst =list(course[name_course][i])
        if "Score" in lst:
            score += (course[name_course][i]["Score"] * course[name_course][i]["Weight"])/100
        else:
            score += course[name_course][i]["Weight"]
    score = score
    
    print(f"  Best case:    {score: .1f} ({letter_grade(score)})")     

#-------------------------------------------------------------------------------
def letter_grade(score):
    """
       This function score value to a letter grade.
       
       Parameter:
       score: float
       
       Return:
       str:
           letter grade
    """
    if score <= 44:
        letter= "F"
    elif score >= 45 and score < 50:
        letter= "D"
    elif score >= 50 and score < 55:
        letter= "D+"
    elif score >= 55 and score < 60:
        letter= "C-"
    elif score >= 60 and score < 65:
        letter= "C"
    elif score >= 65 and score < 70:
        letter= "C+"
    elif score >= 70 and score < 75:
        letter= "B-"
    elif score >= 75 and score < 80:
        letter= "B"
    elif score >= 80 and score < 85:
        letter= "B+"
    elif score >= 85 and score < 90:
        letter= "A-"
    elif score >= 90 and score < 95:
        letter= "A"
    elif score >= 95 and score <= 100:
        letter= "A+"
    return letter 
#-------------------------------------------------------------------------------
def gpa(course):
    """
       This function calculate the expected gpa of courses.
       
       Parameter:
       course: dict
             course data dictionary
       
       Return:
       None
    """
    course_list = list(course.keys())
    gpa = 0
    count = 0
    if course != {}:
        for name_course in course_list:
            total = 0
            score = average_score(name_course,course,total)
            for i in course[name_course]:
                lst = list(course[name_course][i])
                if "Score" in lst:
                    total += (course[name_course][i]["Score"] * course[name_course][i]["Weight"])/100
                else: 
                    total += (score * course[name_course][i]["Weight"])/100     
            grade = letter_grade(total)
            gpa += grade_to_gpa(grade)
            count += 1
        if count != 0:
            average_gpa = gpa / count
        print(f"Expected GPA:{average_gpa: .1f}")
    else:
        return
    
#-------------------------------------------------------------------------------

def grade_to_gpa(grade):
    """
       This function convert letter grade to gpa value.
       
       Parameter:
       grade:str
             letter grade
       
       Return:
       float:
             gpa
    """
    if grade == "A+":
        gpa = 4.00
    elif grade == "A":
        gpa = 4.00
    elif grade == "A-":
        gpa = 3.70
    elif grade == "B+":
        gpa = 3.33
    elif grade == "B":
        gpa = 3.00
    elif grade == "B-":
        gpa = 2.70
    elif grade == "C+":
        gpa = 2.30
    elif grade == "C":
        gpa = 2.00
    elif grade == "C-":
        gpa = 1.70
    elif grade == "D+":
        gpa = 1.30
    elif grade == "D":
        gpa = 1.00
    elif grade == "F":
        gpa = 0.00
    return gpa

#-------------------------------------------------------------------------------

def list_of_date(course):
    """
       This function makes a list of completion dates in course dictionary. Also
       prompt user for name of a course.
       
       Parameter:
       course:dict
              course data dictionary
       Return:
       list:
            list of completion date
       str:
           name of a course   
    """
    date = []
    course_list = list(course.keys())
    
    name_course = input("Course (? for list): ")
    name_course = score_course_error(name_course,course_list)
    if name_course == "":
        return None,None
    
    act_list = list(course[name_course].keys())
    for act in act_list:
        act_data = list(course[name_course][act].keys())
        if "Score" in act_data:
            date.append(course[name_course][act]["Date"])
    return date,name_course

#-------------------------------------------------------------------------------

def first_date(dates):
    """
       This function compares all the dates in course activity dictionary and
       gives earliest date.
       
       Parameter:
       dates:list
            list of completion dates in a course activity
       Return:
       datetime:
               the earliest date
    """
    first_date = datetime.date(9999,12,31)
    for i in range(0,len(dates)-1):
        if dates[i] < first_date:
            first_date = dates[i]
    if dates[len(dates)-1] < first_date:
        first_date = dates[len(dates)-1]
    return first_date
#-------------------------------------------------------------------------------
def last_date(dates):
    """
       This function compare all the dates in course activity dictionary and fives
       last completion date.
       
       Parameter:
       dates:list
             list of completion dates
       Return:
       datetime:
                the last completion date
    """
    last_date = datetime.date(1,1,1)
    for i in range(0,len(dates)-1):
        if dates[i] > last_date:
            last_date = dates[i]
    if dates[len(dates)-1] > last_date:
        last_date = dates[len(dates)-1]
    return last_date
#-------------------------------------------------------------------------------

def date_difference(date,dates):
    """
       This function calculates the date difference of two dates.
       
       Parameter:
       date:datetime
            end date
       dates:
             list of dates
       Return:
       int:
           the number of date difference
    """
    dif = date - first_date(dates)
    dif_list = str(dif).split(" ")
    if len(dif_list) > 1:
        differ = int(dif_list[0])
    else:
        differ = 0
    return differ
#-------------------------------------------------------------------------------
def window(name_course,dates,course):
    """
       This function creates a window of a chart that displays the score percent
       and the completion date. If there is not date difference, this function
       will give an error message
       
       Parameter:
       name_course:str
                   name of a course
       dates:list
             list of dates
       
       course:dict
              course data dictionary
       
       Return:
       None
    """
    try:
        rec,win = create_window(name_course,dates)
    except:
        return print("Error: graded activities all occur on the same day")
    create_y_percent(win,dates)#display percent on Y 0 to 100%
    graph_start_end(dates,win)#print start and end date
    point(win,name_course,course,dates)#display score by point on chart
    get_percent_value(win,dates,rec)#display date and score where clicked
   
#-------------------------------------------------------------------------------
def create_window(name_course,dates):
    """
       This function creates a 1024 by 600 window. Also create a white rectangle 
       inside and set left bottom of rectangle Point(0,0). 
       
       Parameter:
       name_course:str
                   name of a course
       
       dates:list
             a list of completion dates
       
       Return:
       Rectangle:
                window rectangle
       GraphWin:
               window
    """
    win= GraphWin(name_course, 1024,600)
    date_dif = date_difference(last_date(dates),dates)
    if date_dif == 0:
        win.close()
    win.setCoords((-100/(824/date_dif)),0,(date_dif)+(100/(824/date_dif)),600)
    rec = (Rectangle(Point(0,100),Point(date_dif,500))).draw(win)
    rec.setFill("white")
    return rec,win

#-------------------------------------------------------------------------------
def create_y_percent(win,dates):
    """
       This function print out the percent 0% to 100% increasing by 10 each time
       verticaly.
       
       Parameter:
       win:GraphWin
           created window
       
       dates:list
             list of completion dates
       Return
       None
    """
    percent = 0
    half_point = (-100/(824/date_difference(last_date(dates),dates)))/2
    for i in range(100,501,40):
        (Text(Point(half_point,i),f"{percent}%")).draw(win)
        percent += 10    
#-------------------------------------------------------------------------------    
        
def graph_start_end(dates,win):
    """
       This function print the first and last completion date on start(left bottom)
       and end(right bottom) of rectangle.
       
       dates:list
             list of completion dates
       win:Graphwin
           window
    
       Return:
       None
    """
    start = Text(Point(0,50), f"{first_date(dates)}")
    start.draw(win)
    end = Text(Point(date_difference(last_date(dates),dates),50), f"{last_date(dates)}")
    end.draw(win)
 
#-------------------------------------------------------------------------------        
def point(win,name_course,course,dates):
    """
       This function plot a image point on cart that indicates the score and date.
       
       Parameter:
       win:GraphWin
           window
    
       name_course: str
                   name of a course
       
       course:dict
              course data dictionary
       
       dates:list
             list of completion dates
    
       Return:
       None
    """
    act_list = list(course[name_course].keys())
    for act in act_list:
        act_data = list(course[name_course][act].keys())
        if "Score" in act_data:
            course[name_course][act]["Score"]    
            if date_difference(course[name_course][act]["Date"],dates) == 0:
                        x_point = 0
            else:
                x_point = date_difference(course[name_course][act]["Date"],dates)
            point = Image(Point(x_point,(40*(course[name_course][act]["Score"]/10)+100)),"point.gif")
            point.draw(win)
#-------------------------------------------------------------------------------            

def get_percent_value(win,dates,rec):
    """
       This function prints out a text that shows the score and percent where
       clicked. The text will display on top middle of window.
       
       Parameter:
       
       win:GraphWin
           window
       
       dates:list
             list of completion dates
       
       rec:Rectangle
           rectangle created on window
           
       Return:
       None
    """
    text = Text(Point(date_difference(last_date(dates),dates)/2,550), "")
    text.draw(win)
    while win.isOpen():
        try:
            pin = win.getMouse()
        except:
            break
        if pin.x >= rec.p1.x and pin.x <= rec.p2.x and pin.y > rec.p1.y and pin.y < rec.p2.y:
            text.setText(f"({first_date(dates) + datetime.timedelta(int(pin.x))},{((pin.y-100)/40)*10: .1f}%)")
        else:
            text.setText(f"")
            