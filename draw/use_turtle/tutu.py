#Draw a rabbit with big ears
from turtle import *
speed(10)

#Bunny's face
color('pink')
pensize(5)
circle(radius=100)#face

#eye
pencolor('black')
#Left eye
pu()
goto(-45,92)
pd()
begin_fill()
color((0,0,0),(0,0,0.1))
circle(radius=15)
#Right eye
pu()
goto(45,92)
pd()
circle(radius=15)
end_fill()

#nose
pu()
goto(20,60)
color('pink')
pd()
begin_fill()
goto(-20,60)
goto(0,45)
goto(20,60)
end_fill()

#mouth
goto(0,45)
goto(0,40)
seth(-90)
circle(10,120)
pu()
goto(0,40)
seth(-90)
pd()
circle(-10,120)


#Bunny ears
#Left ear
pu()
goto(-60,180)#
seth(200)
pd()
circle(radius=350,extent=90)
goto(-98,110)
#Right ear
pu()
goto(60,180)#
seth(-20)
pd()
circle(radius=-350,extent=90)
goto(98,110)

#Bunny's body
pu()
goto(20,3)
seth(-25)
pd()
circle(radius=-250,extent=25)
circle(radius=-135,extent=260)
seth(50)
circle(radius=-250,extent=25)

##
#Left arm
pu()
seth(180)
goto(-30,-3)
pd()
#Short arm
##circle(radius=270,extent=20)
##circle(radius=20,extent=190)
circle(radius=248,extent=30)
circle(radius=29,extent=185)
#Right arm
pu()
seth(0)
goto(30,-3)
pd()
circle(radius=-248,extent=30)
circle(radius=-27,extent=184)

##
##
pu()
goto(-162,-260)#
pd()
seth(0)
circle(radius=41)
#Right foot
pu()
goto(164,-260)
pd()
circle(radius=41)

done()