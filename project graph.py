from graphics import *
import datetime

#dic = {"c":{"lab":{"score":45,"weight":50, "date": datetime.date(2019,1,1)},
            #"final":{"score":80,"weight":50,"date":datetime.date(2019,4,30)}}}
d1 = datetime.date(2019,1,1)
d2 = datetime.date(2019,5,30)
d3 = datetime.date(2019,4,30)

dic = {"c":{"lab":{"score":45,"weight":50, "date": d1},
                    "final":{"score":80,"weight":50,"date": d2},
                    "u":{"score":45,"weight":50, "date": d3}}}
win= GraphWin("",1024,600)

rec=Rectangle(Point(100,100),Point(924,500))
rec.draw(win)


#draw percent at the side
percent = 0
for i in range(500,99,-40):
    (Text(Point(50,i),f"{percent}%")).draw(win)
    percent += 10

#print point at the y location
text = Image(Point(100,500-((400/10)*6.25)),"point.gif")
text.draw(win)

#plot date



#find out the earlest mark
def first_date(dic):
    lst2 = list_of_date(dic)
    firstdate = datetime.date(9999,12,31)
    
    for i in range(0,len(lst2)-1):
        if lst2[i] < firstdate:
            firstdate = lst2[i]
    
    #if firstdate == 0:
    if lst2[len(lst2)-1] < firstdate:
        firstdate = lst2[len(lst2)-1]
       
            
    return firstdate


#find last date
def last_date(dic):
    lst2 = list_of_date(dic)
    
    lastdate = datetime.date(1,1,1)
    
    for i in range(0,len(lst2)-1):
        if lst2[i] > lst2[i+1]:
            lastdate = lst2[i]
    
    
    if lst2[len(lst2)-1] > lastdate:
        lastdate = lst2[len(lst2)-1]    
    
    return lastdate



# make list with date
def list_of_date(dic):
    lst = list(dic["c"].keys())
    lst2 = []
    for i in lst:
        lst3 = list(dic["c"][i].keys())
        
        if "score" in lst3:
            lst2.append(dic["c"][i]["date"])
    return lst2

#date range
def sub():
    d=last_date(dic) - first_date(dic)
    
    lst = str(d).split(" ")
    
    e = lst[0]
    return int(e)

texts = Text(Point(100,550), f"{first_date(dic)}")
test1 = Text(Point(924,550), f"{last_date(dic)}")
test1.draw(win)
texts.draw(win)

#plot potint
s = dic["c"]["lab"]["date"]-first_date(dic)
print(s)
u = str(s).split(" ")
print(u)
print(u[0])
text3 = Image(Point(100+((824/sub())*(int(u[0]))),
                   500-((400/10)*(dic["c"]["lab"]["score"]/10))),"point.gif")
text3.draw(win)

"""

If there are no scores no plot


Midterm: score 45
         Date 2019-02-15
Labs: score: 85
      date:2019-03-15
final: score : 60
     date : 2019-04-01


window 1024 x 600


-rectangle is going to be the plot area

-824*400 pixel

-percent right side of rectangle

- 100 
d1 = datatime.date(2019-01-01)
d2 = datetime.date(2019-05-01)

d1 < d2
True

lwo x lowest date to Max x highest date

"""
#d1 = datetime.date(2019,5,15)
#d2 = datetime.date(2019,4,30)
#d3 = datetime.date(2019,6,30)

#dic = {"c":{"lab":{"score":45,"weight":50, "date": d1},
            #"final":{"score":80,"weight":50,"date": d2},
            #"u":{"score":45,"weight":50, "date": d3}}}