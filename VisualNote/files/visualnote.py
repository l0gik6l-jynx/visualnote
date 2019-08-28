from graphics import *
import pygame
from pygame import *
import time
import random
from math import *

from config import *


pygame.mixer.init(8000, -16, 2, 64)

win = GraphWin("My Circle", 500, 500)
''' c = Circle(Point(250,250),150) '''
reset = Circle(Point(250,250),75)
zero = Point(250,100)
one = Point(325,120)
two = Point(380,175)
three = Point(400,250)
four = Point(380,325)
five = Point(325,380)
six = Point(250,400)
seven = Point(175,380)
eight = Point(120,325)
nine = Point(100,250)
ten = Point(120,175)
eleven = Point(175,120)
twelve = Point(310,25)
thirteen =  Point(415,85)
fourteen =  Point(475,188)
fifteen = Point(475,310)
sixteen = Point(415,415)
seventeen = Point(310,475)
eighteen = Point(190,475)
nineteen = Point(85,415)
twenty = Point(25,310)
twentyone = Point(25,190)
twentytwo = Point(85,85)
twentythree = Point(190,25)

zeroCircle = Circle(zero,35)
oneCircle = Circle(one,35)
twoCircle = Circle(two,35)
threeCircle = Circle(three,35)
fourCircle = Circle(four,35)
fiveCircle = Circle(five,35)
sixCircle = Circle(six,35)
sevenCircle = Circle(seven,35)
eightCircle = Circle(eight,35)
nineCircle = Circle(nine,35)
tenCircle = Circle(ten,35)
elevenCircle = Circle(eleven,35)

twelveCircle = Circle(Point(310,25),50)#
thirteenCircle = Circle(Point(415,85),50)#
fourteenCircle = Circle(Point(475,188),50)#
fifteenCircle = Circle(Point(475,310),50)#
sixteenCircle = Circle(Point(415,415),50)#
seventeenCircle = Circle(Point(310,475),50)#
eighteenCircle = Circle(Point(190,475),50)#
nineteenCircle = Circle(Point(85,415),50)
twentyCircle = Circle(Point(25,310),50)
twentyoneCircle = Circle(Point(25,190),50)#
twentytwoCircle = Circle(Point(85,85),50)#
twentythreeCircle = Circle(Point(190,25),50)#

button1 = Rectangle(Point(500,500),Point(450,480))
text1 = Text(Point(475,490),"Play")

button1.draw(win)
text1.draw(win)
reset.draw(win)
twelveCircle.draw(win)
thirteenCircle.draw(win)
fourteenCircle.draw(win)
fifteenCircle.draw(win)
sixteenCircle.draw(win)
seventeenCircle.draw(win)
eighteenCircle.draw(win)
nineteenCircle.draw(win)
twentyCircle.draw(win)
twentyoneCircle.draw(win)
twentytwoCircle.draw(win)
twentythreeCircle.draw(win)
zeroCircle.draw(win)
oneCircle.draw(win)
twoCircle.draw(win)
threeCircle.draw(win)
fourCircle.draw(win)
fiveCircle.draw(win)
sixCircle.draw(win)
sevenCircle.draw(win)
eightCircle.draw(win)
nineCircle.draw(win)
tenCircle.draw(win)
elevenCircle.draw(win)

text0 = Text(zero,"C")
text1 = Text(one,"Db")
text2 = Text(two,"D")
text3 = Text(three,"Eb")
text4 = Text(four,"E")
text5 = Text(five,"F")
text6 = Text(six,"Gb")
text7 = Text(seven,"G")
text8 = Text(eight,"Ab")
text9 = Text(nine,"A")
text10 = Text(ten,"Bb")
text11= Text(eleven,"B")
text12 = Text(twelve,"C")
text13 = Text(thirteen,"Db")
text14 = Text(fourteen,"D")
text15 = Text(fifteen,"Eb")
text16 = Text(sixteen,"E")
text17 = Text(seventeen,"F")
text18 = Text(eighteen,"Gb")
text19 = Text(nineteen,"G")
text20 = Text(twenty,"Ab")
text21 = Text(twentyone,"A")
text22 = Text(twentytwo,"Bb")
text23 = Text(twentythree,"B")






for text in [text0,text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20,text21,text22,text23]:
    text.draw(win)

win.setBackground("black")
reset.setFill("gray")
button1.setFill("gray")

true = 1
playlist = []
play = []

def num2color(number):
    color = ''
    if number == 0 or number == 12 :
        color = "green"
    if number == 1 or number == 13 :
        color = "blue"
    if number == 2 or number == 14 :
        color = "purple"
    if number == 3 or number == 15 :
        color = "red"
    if number == 4 or number == 16 :
        color = "orange"
    if number == 5 or number == 17 :
        color = "yellow"
    if number == 6 or number == 18 :
        color = "green"
    if number == 7 or number == 19 :
        color = "blue"
    if number == 8 or number == 20 :
        color = "purple"
    if number == 9 or number == 21 :
        color = "red"
    if number == 10 or number == 22 :
        color = "orange"
    if number == 11 or number == 23 :
        color = "yellow"
    return color
def num2circle(number):
    if number == 0 :
        color = zeroCircle
    if number == 1 :
        color = oneCircle
    if number == 2 :
        color = twoCircle
    if number == 3 :
        color = threeCircle
    if number == 4 :
        color = fourCircle
    if number == 5 :
        color = fiveCircle
    if number == 6 :
        color = sixCircle
    if number == 7 :
        color = sevenCircle
    if number == 8 :
        color = eightCircle
    if number == 9 :
        color = nineCircle
    if number == 10 :
        color = tenCircle
    if number == 11 :
        color = elevenCircle
    if number == 12 :
        color = twelveCircle
    if number == 13 :
        color = thirteenCircle
    if number == 14 :
        color = fourteenCircle
    if number == 15 :
        color = fifteenCircle
    if number == 16 :
        color = sixteenCircle
    if number == 17 :
        color = seventeenCircle
    if number == 18 :
        color = eighteenCircle
    if number == 19 :
        color = nineteenCircle
    if number == 20 :
        color = twentyCircle
    if number == 21 :
        color = twentyoneCircle
    if number == 22 :
        color = twentytwoCircle
    if number == 23 :
        color = twentythreeCircle
    return color
def circle2num(circle):
    output = -1
    for i in [zeroCircle,oneCircle,twoCircle,threeCircle,fourCircle,fiveCircle,sixCircle,sevenCircle,eightCircle,nineCircle,tenCircle,elevenCircle,twelveCircle,thirteenCircle,fourteenCircle,fifteenCircle,sixteenCircle,seventeenCircle,eighteenCircle,nineteenCircle,twentyCircle,twentyoneCircle,twentytwoCircle,twentythreeCircle ]:
        output += 1
        if circle == i :
            return output
def word2num(word):
    output = -1
    for i in [zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree]:
        output += 1
        if word == i:
            return output


def clearCircles():
    for x in [zeroCircle,oneCircle,twoCircle,threeCircle,fourCircle,fiveCircle,sixCircle,sevenCircle,eightCircle,nineCircle,tenCircle,elevenCircle,twelveCircle,thirteenCircle,fourteenCircle,fifteenCircle,sixteenCircle,seventeenCircle,eighteenCircle,nineteenCircle,twentyCircle,twentyoneCircle,twentytwoCircle,twentythreeCircle ]:
        x.setFill("gray")

def play(note,length):
    print(note)
    if isinstance(note,int) :
        markNote(note)
        pygame.mixer.Sound( '{}.wav'.format(note)).play()
    if isinstance(note,list):
        for i in note:
            markNote(i)
            pygame.mixer.Sound( '{}.wav'.format(i)).play()
    rest(length)
    clearCircles()
def hit(note):
    if isinstance(note,int):
        markNote(note)
        pygame.mixer.Sound( '{}.wav'.format(note)).play()
    if isinstance(note,list):
        for i in note:
            markNote(i)
            pygame.mixer.Sound( '{}.wav'.format(i)).play()

def stop():
    true
    pygame.mixer.stop()
def rest(length):
    restLength = wholenote / length
    time.sleep(restLength)
def markNote(note):
    for i in range(24):
        if note == i :
            num2circle(i).setFill(num2color(i))

class scale():
    def __init__(self,name,scale):
        self.name = name
        self.scale = scale
        self.I = [scale[0],scale[2],scale[4],scale[6]]
        self.II = [scale[1],scale[3],scale[5],scale[7]]
        self.III = [scale[2],scale[4],scale[6],scale[8]]
        self.IV = [scale[3],scale[5],scale[7],scale[9]]
        self.V = [scale[4],scale[6],scale[8],scale[10]]
        self.VI = [scale[5],scale[7],scale[9],scale[11]]
        self.VII = [scale[6],scale[8],scale[10],scale[12]]
        self.chords = [self.I,self.II,self.III,self.IV,self.V,self.VI,self.VII]
        self.hand = []
        self.hand1 = [scale[0],scale[1],scale[2]]
        self.hand2 = [scale[1],scale[2],scale[3]]
        self.hand3 = [scale[2],scale[3],scale[4]]
        self.hand4 = [scale[3],scale[4],scale[5]]
        self.hand5 = [scale[4],scale[5],scale[6]]
        self.hand6 = [scale[5],scale[6],scale[7]]
        self.hand7 = [scale[6],scale[7],scale[8]]
        self.hand8 = [scale[7],scale[8],scale[9]]
        self.hand9 = [scale[8],scale[9],scale[10]]
        self.hand10 = [scale[9],scale[10],scale[11]]
        self.hand11 = [scale[10],scale[11],scale[12]]
        self.hands = [self.hand1,self.hand2,self.hand3,self.hand4,self.hand5,self.hand6,self.hand7,self.hand8,self.hand9,self.hand10,self.hand11]
    def randhand():
        return random.choice([self.hand1,self.hand2,self.hand3,self.hand4,self.hand5,self.hand6,self.hand7,self.hand8,self.hand9,self.hand10,self.hand11])
    def bar(self):
            hands = [scale.randhand,scale.randhand,scale.randhand]
            for i in range(4):
                choice = random.choice([1,3])
                self.hand = random.choice(self.hands)
                if choice == 1:
                    self.melody()
                if choice == 2:
                    play(random.choice(self.chords),random.choice([2,1]))
                if choice == 3:
                    self.randchord()
                    rest(16)
    def randchord(self):
        play(random.choice(self.chords),random.choice([2,1]))
    def melody(self):
        self.hand = random.choice(self.hands)
        note1 = random.choice(self.hand)
        note2 = random.choice(self.hand)
        note3 = random.choice(self.hand)
        rest1 = random.choice([4,8])
        rest2 = random.choice([4,8])
        rest3 = random.choice([4,8])

        note4 = random.choice(self.hand)
        note5 = random.choice(self.hand)
        note6 = random.choice(self.hand)
        rest4 = random.choice([4,8])
        rest5 = random.choice([4,8])
        rest6 = random.choice([4,8])

        note7 = random.choice(self.hand)
        note8 = random.choice(self.hand)
        note9 = random.choice(self.hand)
        rest7 = random.choice([4,8])
        rest8 = random.choice([4,8])
        rest9 = random.choice([4,8])

        def play1():
            play(note1,rest1)
            play(note2,rest2)
        def play2():
            play(note4,rest4)
            play(note5,rest5)
        def play3():
            play(note7,rest7)
            play(note8,rest8)
        def play4():
            play(note3,rest3)
            play(note6,rest6)

        for i in range(3):
            choice = random.choice([1,2,3,4])
            if choice == 1:
                play1()
            if choice == 2:
                play2()
            if choice == 3:
                play3()
            if choice == 4:
                play4()




C_major = scale("C Major",[0,2,4,5,7,9,10,12,14,16,17,19,22])
Cs_major = scale("C sharp Major",[1,3,5,6,8,10,11,13,15,17,18,20,22,23])
D_major = scale("D Major",[2,4,6,7,9,11,12,14,16,18,19,21,23,0])
Ds_major = scale("D Sharp Major",[3,5,7,8,10,12,13,15,17,19,20,22,0,1])
E_major = scale("E Major",[4,6,8,9,11,13,15,16,18,20,21,23,1,3])
F_major = scale("F Major",[5,7,9,10,12,14,16,17,19,21,22,0,2,4])
Fs_major = scale("F Sharp Major",[6,8,10,11,13,15,17,18,20,22,23,1,3,5])
G_major = scale("G Major",[7,9,11,12,14,16,18,19,21,23,0,2,4,6])

C_phrygian = scale("C Phrygian",[0,1,3,5,7,8,10,12,13,15,17,19,20,22])
C_locrian = scale("C Locrian",[0,1,3,5,6,8,10,12,13,15,17,18,20,22])
C_minor = scale("C Minor",[0,2,3,5,7,8,10,12,14,15,17,19,20,22])
C_dorian = scale("C Dorian",[0,2,3,5,7,9,10,12,14,15,17,19,21,22])
C_mixolydian = scale("C Mixolydian",[0,2,4,5,7,9,10,12,14,16,17,19,21,22])

def playall():
    print("playing all scales")
    for scale in [C_phrygian,C_major,C_locrian,D_major,C_minor,G_major,C_mixolydian,E_major,C_dorian]:
        print(scale.name)
        for play in range(7):
            scale.bar()
            print("**END BAR**")
        scale.randchord()
        print("**SCALE CHANGE**")
        time.sleep(1.5)

def test():
    for i in range(28):
        hit(random.choice(range(23)))





def PlayChords():
    playlist = []
    while true == 1:
        click = win.getMouse()
        for circle in [zeroCircle,oneCircle,twoCircle,threeCircle,fourCircle,fiveCircle,sixCircle,sevenCircle,eightCircle,nineCircle,tenCircle,elevenCircle,twelveCircle,thirteenCircle,fourteenCircle,fifteenCircle,sixteenCircle,seventeenCircle,eighteenCircle,nineteenCircle,twentyCircle,twentyoneCircle,twentytwoCircle,twentythreeCircle]:
            center = circle.getCenter()
            distance =  sqrt(((click.getX() - center.getX()) ** 2) + ((click.getY() - center.getY()) ** 2))
            if distance < 50:
                playlist.extend([circle2num(circle)])
                print(playlist)
                output = circle2num(circle)
                markNote(output)
        if  175 < click.getX()  < 325 and 175 < click.getY() < 325:#centercircle
            play(playlist,1)
            clearCircles()
            playlist = []
        if  450 < click.getX()  < 500 and 480 < click.getY() < 500:#terminal button
            playall()



for i in range(24):
    play(i,64)
    time.sleep(.015)
PlayChords()