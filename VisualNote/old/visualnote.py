from graphics import *
from winsound import *
import winsound
import pygame
from pygame import *
import time
import random
from math import *

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

phrygian = [0,1,3,5,7,8,10,0,5]
phrygian2 = [12,13,15,17,19,20,22,12,17]
locrian = [0,1,2,3,5,6,8,10,0,3]
pentatonic = [1,3,6,8,10,1,8]
pentatonic2 = [13,15,18,20,22,13,20]
fsmaj = [2,4,7,9,11,2,9]
fsmaj2 = [14,16,19,21,23,14,21]

button1 = Rectangle(Point(500,500),Point(450,480))
text1 = Text(Point(475,490),"term")

button1.draw(win)
text1.draw(win)
#c.draw(win)
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
text0 = Text(zero,"0")
text1 = Text(one,"1")
text2 = Text(two,"2")
text3 = Text(three,"3")
text4 = Text(four,"4")
text5 = Text(five,"5")
text6 = Text(six,"6")
text7 = Text(seven,"7")
text8 = Text(eight,"8")
text9 = Text(nine,"9")
text10 = Text(ten,"10")
text11= Text(eleven,"11")
text0.draw(win)
text1.draw(win)
text2.draw(win)
text3.draw(win)
text4.draw(win)
text5.draw(win)
text6.draw(win)
text7.draw(win)
text8.draw(win)
text9.draw(win)
text10.draw(win)
text11.draw(win)
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
    if circle == zeroCircle :
        output = 0
    if circle == oneCircle :
        output = 1
    if circle == twoCircle :
        output = 2
    if circle == threeCircle :
        output = 3
    if circle == fourCircle :
        output = 4
    if circle == fiveCircle :
        output = 5
    if circle == sixCircle :
        output = 6
    if circle == sevenCircle :
        output = 7
    if circle == eightCircle :
        output = 8
    if circle == nineCircle :
        output = 9
    if circle == tenCircle :
        output = 10
    if circle == elevenCircle :
        output = 11
    if circle == twelveCircle :
        output = 12
    if circle == thirteenCircle :
        output = 13
    if circle == fourteenCircle :
        output = 14
    if circle == fifteenCircle :
        output = 15
    if circle == sixteenCircle :
        output = 16
    if circle == seventeenCircle :
        output = 17
    if circle == eighteenCircle :
        output = 18
    if circle == nineteenCircle :
        output = 19
    if circle == twentyCircle :
        output = 20
    if circle == twentyoneCircle :
        output = 21
    if circle == twentytwoCircle :
        output = 22
    if circle == twentythreeCircle :
        output = 23
    return output
def word2num(word):
    if word == zero :
        output = 0
    if word == one :
        output = 1
    if word == two :
        output = 2
    if word == three :
        output = 3
    if word == four :
        output = 4
    if word == five :
        output = 5
    if word == six :
        output = 6
    if word == seven :
        output = 7
    if word == eight :
        output = 8
    if word == nine :
        output = 9
    if word == ten :
        output = 10
    if word == eleven :
        output = 11
    if word == twelve :
        output = 12
    if word == thirteen :
        output = 13
    if word == fourteen :
        output = 14
    if word == fifteen :
        output = 15
    if word == sixteen :
        output = 16
    if word == seventeen :
        output = 17
    if word == eighteen :
        output = 18
    if word == nineteen :
        output = 19
    if word == twenty :
        output = 20
    if word == twentyone :
        output = 21
    if word == twentytwo :
        output = 22
    if word == twentythree :
        output = 23
    return output

def play(one,two,three):
    pygame.mixer.Sound( '{}.wav'.format(word2num(one))).play()
    pygame.mixer.Sound( '{}.wav'.format(word2num(two))).play()
    pygame.mixer.Sound( '{}.wav'.format(word2num(three))).play()
def stop():
    true
    pygame.mixer.stop()
def randomFastRest():
    quarternote = .15
    halfnote = quarternote * 2
    wholenote = quarternote * 4
    eightnote = quarternote / 2
    time.sleep(random.choice([quarternote,halfnote,wholenote,eightnote]))
def randomRest():
    quarternote = .40
    halfnote = quarternote * 2
    wholenote = quarternote * 4
    eightnote = quarternote / 2
    time.sleep(random.choice([quarternote,halfnote,wholenote,eightnote]))
def randomLongRest():
    quarternote = .80
    halfnote = quarternote * 2
    wholenote = quarternote * 4
    eightnote = quarternote / 2
    time.sleep(random.choice([quarternote,halfnote,eightnote]))
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
            chord(playlist)
            clearCircles()
            playlist = []
        if  450 < click.getX()  < 500 and 480 < click.getY() < 500:#terminal button
            Godsong()
def rest():
    time.sleep(.44)
def halfRest():
    time.sleep(.22)

def clearCircles():
    zeroCircle.setFill("gray")
    oneCircle.setFill("gray")
    twoCircle.setFill("gray")
    threeCircle.setFill("gray")
    fourCircle.setFill("gray")
    fiveCircle.setFill("gray")
    sixCircle.setFill("gray")
    sevenCircle.setFill("gray")
    eightCircle.setFill("gray")
    nineCircle.setFill("gray")
    tenCircle.setFill("gray")
    elevenCircle.setFill("gray")
    twelveCircle.setFill("gray")
    thirteenCircle.setFill("gray")
    fourteenCircle.setFill("gray")
    fifteenCircle.setFill("gray")
    sixteenCircle.setFill("gray")
    seventeenCircle.setFill("gray")
    eighteenCircle.setFill("gray")
    nineteenCircle.setFill("gray")
    twentyCircle.setFill("gray")
    twentyoneCircle.setFill("gray")
    twentytwoCircle.setFill("gray")
    twentythreeCircle.setFill("gray")
def markNote(note):
    for i in range(24):
        if note == i :
            num2circle(i).setFill(num2color(i))
def note(note):
    for i in range(24):
        if note == i:
            clearCircles()
            stop()
            print("{}".format(i))
            pygame.mixer.Sound( '{}.wav'.format(i)).play()
            markNote(i)
def testing():
    for i in range(25):
        time.sleep(.2)
        clearCircles()
        note(random.choice(range(24)))
    clearCircles()
def chord(play):
    clearCircles()
    print(play)
    stop()
    for i in play:
        pygame.mixer.Sound("{}.wav".format(i)).play()
        markNote(i)
def appreg(play):
    clearCircles()
    print(play)
    stop()
    for i in play:
        pygame.mixer.Sound("{}.wav".format(i)).play()
        markNote(i)
        time.sleep(.12)
def checkCircles(mouse):
    for circle in [zeroCircle,oneCircle,twoCircle,threeCircle,fourCircle,fiveCircle,sixCircle,sevenCircle,eightCircle,nineCircle,tenCircle,elevenCircle,twelveCircle,thirteenCircle,fourteenCircle,fifteenCircle,sixteenCircle,seventeenCircle,eighteenCircle,nineteenCircle,twentyCircle,twentyoneCircle,twentytwoCircle,twentythreeCircle]:
        center = circle.getCenter()
        distance =  sqrt(((mouse.getX() - center.getX()) ** 2) + ((mouse.getY() - center.getY()) ** 2))
        if distance < 50:
            playlist.extend([circle2num(circle)])
            print(playlist)
            output = circle2num(circle)
        #is i within range of click
        if  175 < mouse.getX()  < 325 and 175 < mouse.getY() < 325:#centercircle
            chord(playlist)
            clearCircles()
def terminal():
    print("\n"*25)
    print('Welcome to the Terminal!')
    loop = 1
    while loop == 1:
        cmd = input("cmd> ")
        if cmd == str("exit"):
            print("Use Alt+Tab to switch back to visualizer")
            loop = 0
        if cmd == str("exit()"):
            exit()
        if cmd == str("phrygian"):
            for i in phrygian:
                note(i)
                time.sleep(.3)
            clearCircles()
        if cmd == str("locrian"):
            for i in locrian:
                note(i)
                time.sleep(.3)
            clearCircles()
        if cmd == str("pentatonic"):
            for i in pentatonic:
                note(i)
                time.sleep(.3)
        if cmd == str("phrygian random"):
            word = random.choice([1,2,3,4])
            def phChord():
                for i in range(3):
                    note(random.choice(phrygian))
            phChord()
            def loChord():
                for i in range(3):
                    note(random.choice(locrian))
            phChord()
            def peChord():
                for i in range(3):
                    note(random.choice(pentatonic))
            phChord()
        if cmd == str("locrian random"):
            word = random.choice([1,2,3,4])
            def phChord():
                for i in range(3):
                    note(random.choice(phrygian))
            phChord()
        if cmd == str("Godsong"):
            Godsong()

phrygian = [0,1,3,5,7,8,10,0,7]
phrygian2 = [12,13,15,17,19,20,22,12,17]
locrian = [0,1,3,5,6,8,10,0,6]
locrian2 = [12,13,15,17,18,20,22,12,17]
pentatonic = [1,3,6,8,10,1,10]
pentatonic2 = [13,15,18,20,22,13,22]
pentatonic3 = [6,8,11,1,6,1]
pentatonic4 = [18,20,23,13,18,13]
fsmaj = [1,3,5,6,8,10,11,1,8]
fsmaj2 = [13,15,17,18,20,22,23,13,20]
ionian = [0,2,4,5,7,9,11,1,5]
ionian2 = [12,14,16,17,19,21,13,13,17]

bullChord = [11,6,1,21,14]
harmonic = [0,5,10,14,19,12,17]
homestuck = [10, 5, 0, 20, 13, 15]
homestuckALT = [10, 0, 22, 5, 15, 20, 12]

quarternote = .35
halfnote = quarternote * 2
wholenote = quarternote * 4
eightnote = quarternote / 2

def wholeNote():
    time.sleep(wholenote)
def halfNote():
    time.sleep(halfnote)
def quarterNote():
    time.sleep(quarternote)
def eightNote():
    time.sleep(eightnote)
def rhythm(note):
    for i in range(4):
        note(note)
        wholeNote()
        note(note)
        halfNote()
        note(note)
        halfNote()
#RIP
def Godsong():
    song = random.choice([1,2])
    if song == 1:
        for i in range(2):
            sent = random.choice([1,2])
            if sent == 1:
                    for i in range(4):
                        word = random.choice([1,2])
                        if word == 1:
                            print("bullchord")
                            for i in range(8):
                                measure = random.choice([1,2,3,4])
                                if measure == 1:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(bullChord))
                                        randomRest()
                                if measure == 2:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(bullChord)])
                                        playlist.extend([random.choice(bullChord)])
                                        playlist.extend([random.choice(bullChord)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                if measure == 3:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(bullChord))
                                        randomRest()
                                if measure == 4:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(bullChord)])
                                        playlist.extend([random.choice(bullChord)])
                                        playlist.extend([random.choice(bullChord)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()

                        if word == 2:
                            print("random harmonic")
                            win.setBackground("black")
                            for i in range(8):
                                measure = random.choice([1,2,3,4])
                                if measure == 1:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(harmonic))
                                        randomRest()
                                        randomRest()
                                if measure == 2:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(harmonic)])
                                        playlist.extend([random.choice(harmonic)])
                                        playlist.extend([random.choice(harmonic)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        randomLongRest()
                                if measure == 3:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(harmonic))
                                        randomRest()
                                        randomRest()
                                if measure == 4:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(harmonic)])
                                        playlist.extend([random.choice(harmonic)])
                                        playlist.extend([random.choice(harmonic)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        randomLongRest()

            if sent == 2:
                    for i in range(4):
                        word = random.choice([1,2])
                        if word == 1:
                            print("f# MAJ")
                            for i in range(8):
                                measure = random.choice([1,2,3,4])
                                if measure == 1:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(fsmaj2))
                                        randomFastRest()
                                if measure == 2:
                                    #Fast rest
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(fsmaj)])
                                        playlist.extend([random.choice(fsmaj)])
                                        playlist.extend([random.choice(fsmaj2)])
                                        note(random.choice(playlist))
                                        randomFastRest()
                                        note(random.choice(playlist))
                                        randomFastRest()
                                        chord(playlist)
                                        randomRest()
                                if measure == 3:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(fsmaj))
                                        randomRest()
                                if measure == 4:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(fsmaj)])
                                        playlist.extend([random.choice(fsmaj2)])
                                        playlist.extend([random.choice(fsmaj2)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()

                        if word == 2:
                            print("homestuck alternate")
                            for i in range(8):
                                measure = random.choice([1,2,3,4])
                                if measure == 1:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(homestuckALT))
                                        randomRest()
                                        randomRest()
                                if measure == 2:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(homestuckALT)])
                                        playlist.extend([random.choice(homestuckALT)])
                                        playlist.extend([random.choice(homestuckALT)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        randomLongRest()
                                if measure == 3:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(homestuckALT))
                                        randomRest()
                                        randomRest()
                                if measure == 4:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(homestuckALT)])
                                        playlist.extend([random.choice(homestuckALT)])
                                        playlist.extend([random.choice(homestuckALT)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        randomLongRest()
    if song == 1:
        for i in range(2):
            sent = random.choice([1,2])
            if sent == 1:
                    for i in range(4):
                        word = random.choice([1,2])
                        if word == 1:
                            print("phrygian")
                            for i in range(8):
                                measure = random.choice([1,2,3,4])
                                if measure == 1:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(phrygian2))
                                        randomRest()
                                if measure == 2:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(phrygian)])
                                        playlist.extend([random.choice(phrygian)])
                                        playlist.extend([random.choice(phrygian2)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        note(random.choice(playlist))
                                        randomRest()

                                if measure == 3:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(phrygian))
                                        randomRest()
                                if measure == 4:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(phrygian)])
                                        playlist.extend([random.choice(phrygian2)])
                                        playlist.extend([random.choice(phrygian2)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        note(random.choice(playlist))
                                        randomRest()


                        if word == 2:
                            print("locrian")
                            win.setBackground("black")
                            for i in range(8):
                                measure = random.choice([1,2,3,4])
                                if measure == 1:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(locrian2))
                                        randomRest()
                                        randomRest()
                                if measure == 2:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(locrian)])
                                        playlist.extend([random.choice(locrian)])
                                        playlist.extend([random.choice(locrian2)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        randomLongRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                if measure == 3:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(locrian))
                                        randomRest()
                                        randomRest()
                                if measure == 4:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(locrian)])
                                        playlist.extend([random.choice(locrian2)])
                                        playlist.extend([random.choice(locrian2)])

                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        randomLongRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
            if sent == 2:
                    for i in range(4):
                        word = random.choice([1,2])
                        if word == 1:
                            print("pentatonic 1")
                            for i in range(8):
                                measure = random.choice([1,2,3,4])
                                if measure == 1:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(fsmaj2))
                                        randomFastRest()
                                if measure == 2:
                                    #Fast rest
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(pentatonic)])
                                        playlist.extend([random.choice(pentatonic)])
                                        playlist.extend([random.choice(fsmaj2)])
                                        note(random.choice(playlist))
                                        randomFastRest()
                                        chord(playlist)
                                        randomRest()
                                        note(random.choice(playlist))
                                        randomFastRest()

                                if measure == 3:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(pentatonic))
                                        randomRest()
                                if measure == 4:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(pentatonic)])
                                        playlist.extend([random.choice(fsmaj2)])
                                        playlist.extend([random.choice(fsmaj2)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        note(random.choice(playlist))
                                        randomRest()
                        if word == 2:
                            print("pentatonic")
                            for i in range(8):
                                measure = random.choice([1,2,3,4])
                                if measure == 1:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(pentatonic4))
                                        randomRest()
                                        randomRest()
                                if measure == 2:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(pentatonic3)])
                                        playlist.extend([random.choice(pentatonic3)])
                                        playlist.extend([random.choice(pentatonic4)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        randomLongRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                if measure == 3:
                                    for i in range(3):
                                        clearCircles()
                                        note(random.choice(pentatonic3))
                                        randomRest()
                                        randomRest()
                                if measure == 4:
                                    for i in range(1):
                                        playlist = []
                                        clearCircles()
                                        playlist.extend([random.choice(pentatonic3)])
                                        playlist.extend([random.choice(pentatonic4)])
                                        playlist.extend([random.choice(pentatonic4)])
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()
                                        chord(playlist)
                                        randomLongRest()
                                        randomLongRest()
                                        note(random.choice(playlist))
                                        randomRest()
                                        randomRest()


def csMajor():
    print('csmajor')
    csmajor = [0,2,4,5,7,9,10,12,14,16,17,19,22]
    group1 = [0,2,4,5,7]
    group2 = [2,4,5,7,9]
    group3 = [4,5,7,9,10]
    group4 = [5,7,9,10,12]
    group5 = [7,9,10,12,14]
    group6 = [9,10,12,14,16]
    group7 = [10,12,14,16,17]
    group8 = [12,14,16,17,19]
    cs1 = [0,4,7]
    cs2 = [2,5,9]
    cs3 = [4,7,10]
    cs4 = [5,9,12]
    cs5 = [7,10,14]
    cs6 = [9,12,16]
    cs7 = [10,14,17]
    cs8 = [12,16,19]
    for i in range(random.choice(range(4,8))):
        note(random.choice(group1))
        randomRest()
    chord(cs1)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(group2))
        randomRest()
    chord(cs2)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(group3))
        randomRest()
    chord(cs3)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(group4))
        randomRest()
    chord(cs4)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(group5))
        randomRest()
    chord(cs5)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(group6))
        randomRest()
    chord(cs6)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(group7))
        randomRest()
    chord(cs7)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(group8))
        randomRest()
    chord(cs8)
    randomLongRest()
    randomLongRest()

def fsMajor():
    print("fsmajor")
    fsmajor = [6,8,10,11,13,15,16,18,20,22,23,1]
    melody = [1,3,4,6,8,10,13,15,18,20,21]
    group1 = [0,2,4,5,7]
    group2 = [2,4,5,7,9]
    group3 = [4,5,7,9,10]
    group4 = [5,7,9,10,12]
    group5 = [7,9,10,12,14]
    group6 = [9,10,12,14,16]
    group7 = [10,12,14,16,17]
    group8 = [12,14,16,17,19]
    fs1 = [6,10,13,16]
    fs2 = [8,11,15,18]
    fs3 = [10,13,16,20]
    fs4 = [11,15,18,22]
    fs5 = [13,16,20,23]
    fs6 = [15,18,22]
    fs7 = [16,20,23]
    fs8 = [18,0,1,2]
    chords = []
    chords.append(fs1)
    chords.append(fs2)
    chords.append(fs3)
    chords.append(fs4)
    chords.append(fs5)
    chords.append(fs6)
    chords.append(fs7)
    print(chords)
    def asdf():
        for i in chords:
            chord(i)
            rest()
        rest
        for i in range(2):
            random.shuffle(chords)
            for i in chords:
                appreg(i)

    for i in range(4):
        choice = random.choice([2,3,4])
        if choice == 1:
            for i in range(2):
                choice = random.choice([fs1,fs2,fs3,fs4,fs5,fs6,fs7])
                chord(choice)
                randomLongRest()
        if choice == 4:
            for i in range(1):
                choice = random.choice([fs1,fs2,fs3,fs4,fs5,fs6,fs7])
                chord(choice)
                randomLongRest()
        if choice == 2:
            for i in range(random.choice(range(2,3))):
                note(random.choice(melody))
                rest()
        if choice == 3:
            for i in range(8):
                choice = random.choice([fs1,fs2,fs3,fs4,fs5,fs6,fs7])
                appreg(choice)
                randomLongRest()


def csMajor2():
    print("csmajor(2)")
    csmajor = [0,2,4,5,7,9,10,12,14,16,17,19,22]
    cs1 = [0,4,7]
    cs2 = [2,5,9]
    cs3 = [4,7,10]
    cs4 = [5,9,12]
    cs5 = [7,10,14]
    cs6 = [9,12,16]
    cs7 = [10,14,17]
    cs8 = [12,16,19]

    for i in range(8):
        choice = random.choice([cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8])
        chord(choice)
        randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(csmajor))
        randomRest()
    choice = random.choice([cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8])
    chord(choice)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(csmajor))
        randomRest()
    choice = random.choice([cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8])
    chord(choice)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(csmajor))
        randomRest()
    choice = random.choice([cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8])
    chord(choice)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(csmajor))
        randomRest()
    choice = random.choice([cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8])
    chord(choice)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(csmajor))
        randomRest()
    choice = random.choice([cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8])
    chord(choice)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(csmajor))
        randomRest()
    choice = random.choice([cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8])
    chord(choice)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(csmajor))
        randomRest()
    choice = random.choice([cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8])
    chord(choice)
    randomLongRest()
    randomLongRest()
    for i in range(random.choice(range(4,8))):
        note(random.choice(csmajor))
        randomRest()
    choice = random.choice([cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8])
    chord(choice)
    randomLongRest()
    randomLongRest()



for i in range(24):
    note(i)
    time.sleep(.02)
win.getMouse()
fsMajor()
Godsong()
csMajor()
csMajor2()

PlayChords()
#n3ph7sys waz here!!!
