from graphics import *
import pygame
from pygame import *
pygame.init()
pygame.mixer.init(22100, -16, 2, 64)
import time
import random

def main():
    win = GraphWin("My Circle", 500, 500)
    c = Circle(Point(250,250),150)
    reset = Circle(Point(250,250),75)
    reset.setFill("purple")


    note0 = pygame.mixer.Sound('0.wav')
    note1 = pygame.mixer.Sound('1.wav')
    note2 = pygame.mixer.Sound('2.wav')
    note3 = pygame.mixer.Sound('3.wav')
    note4 = pygame.mixer.Sound('4.wav')
    note5 = pygame.mixer.Sound('5.wav')
    note6 = pygame.mixer.Sound('6.wav')
    note7 = pygame.mixer.Sound('7.wav')
    note8 = pygame.mixer.Sound('8.wav')
    note9 = pygame.mixer.Sound('9.wav')
    note10 = pygame.mixer.Sound('10.wav')
    note11 = pygame.mixer.Sound('11.wav')


    notes = [note0,note1,note2,note3,note4,note5,note6,note7,note8,note9,note10,note11]
    phrygians = [note0,note1,note3,note5,note7,note8,note10,note0]
    majors = []
    minors = []
    locrian = [note0,note1,note3,note5,note6,note8,note10,note0]


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

    button1 = Rectangle(Point(500,500),Point(450,480))
    text1 = Text(Point(475,490),"random")
    button2 = Rectangle(Point(500,480),Point(450,460))
    text2 = Text(Point(475,470),"chroma")
    button3 = Rectangle(Point(500,460),Point(450,440))
    text3 = Text(Point(475,450),"penta")
    button4 = Rectangle(Point(500,440),Point(450,420))
    text4 = Text(Point(475,430),"chroma")
    button5 = Rectangle(Point(500,420),Point(450,400))
    text5 = Text(Point(475,410),"phryg")
    button6 = Rectangle(Point(500,400),Point(450,380))
    text6 = Text(Point(475,390),"locri")

    button1.draw(win)
    button2.draw(win)
    button3.draw(win)
    button4.draw(win)
    button5.draw(win)
    button6.draw(win)
    text1.draw(win)
    text2.draw(win)
    text3.draw(win)
    text4.draw(win)
    text5.draw(win)
    text6.draw(win)

    c.draw(win)
    reset.draw(win)
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

    true = 1
    playlist = []
    play = []


    while true==1:
        def stop():
            pygame.mixer.stop()
        def playChord(one,two,three):
            print(one)
            one.play()
            two.play()
            three.play()
            markNote(one)
            markNote(two)
            markNote(three)
            randomLongRest()
            clearCircles()
            stop()
        def playRand(one,two,three):
            for i in range(1,16):
                note = random.choice([one,two,three])
                markNote(note)
                note.play()
                randomRest()
                stop()
                clearCircles()
        def clearCircles():
            zeroCircle.setFill("white")
            oneCircle.setFill("white")
            twoCircle.setFill("white")
            threeCircle.setFill("white")
            fourCircle.setFill("white")
            fiveCircle.setFill("white")
            sixCircle.setFill("white")
            sevenCircle.setFill("white")
            eightCircle.setFill("white")
            nineCircle.setFill("white")
            tenCircle.setFill("white")
            elevenCircle.setFill("white")
        def markNote(note):
            for i in notes:
                if note == i :
                    num2circle(i).setFill(num2color(i))
        def playRandomSong():
            randomNote = random.choice(play)
            randomNote.play()
            clearCircles()
            pygame.mixer.stop()
            markNote(randomNote)
            randomNote.play()
            randomRest()
        def playNote():
            random.choice(notes).play()
        def pickNote():
            return random.choice(notes)
        def playPent():
            note = random.choice([note2,note4,note7,note9,note11])
            markNote(note)
            note.play()
        def playPent2():
            note = random.choice([note3,note5,note8,note10,note0])
            markNote(note)
            note.play()
        def playPent3():
            note = random.choice([note4,note6,note9,note11,note1])
            markNote(note)
            note.play()
        def catch():
            time.sleep(.1333)
        def randomRest():
            quarternote = .1
            halfnote = quarternote * 2
            wholenote = quarternote * 4
            eightnote = quarternote / 2
            time.sleep(random.choice([quarternote,halfnote,wholenote,eightnote]))
        def randomLongRest():
            quarternote = .25
            halfnote = quarternote * 2
            wholenote = quarternote * 4
            eightnote = quarternote / 2
            time.sleep(random.choice([quarternote,halfnote,wholenote,eightnote]))
        def num2color(number):
            color = ''
            if number == note0:
                color = "green"
            if number == note1:
                color = "blue"
            if number == note2:
                color = "purple"
            if number == note3:
                color = "red"
            if number == note4:
                color = "orange"
            if number == note5:
                color = "yellow"
            if number == note6:
                color = "green"
            if number == note7:
                color = "blue"
            if number == note8:
                color = "purple"
            if number == note9:
                color = "red"
            if number == note10:
                color = "orange"
            if number == note11:
                color = "yellow"
            return color
        def num2circle(number):
            if number == note0:
                color = zeroCircle
            if number == note1:
                color = oneCircle
            if number == note2:
                color = twoCircle
            if number == note3:
                color = threeCircle
            if number == note4:
                color = fourCircle
            if number == note5:
                color = fiveCircle
            if number == note6:
                color = sixCircle
            if number == note7:
                color = sevenCircle
            if number == note8:
                color = eightCircle
            if number == note9:
                color = nineCircle
            if number == note10:
                color = tenCircle
            if number == note11:
                color = elevenCircle
            return color








        click = win.getMouse()

        if 450 < click.getX() and 480 < click.getY():#random
            for i in range(60):
                pickNote().play()

        if  175 < click.getX() < 325 and 175 < click.getY() < 325:#reset
            print("reset")
            clearCircles()
            for i in playlist:
                for i in play:
                    i.play()
                    time.sleep(0.01)
                    print(num2color(i))
                playlist = []
                play = []#reset
        if 450 < click.getX() and 480 > click.getY() > 460:#chromatic
            for t in range(1,100):
                i = random.choice([1,2,3,4])
                if i == 1:
                    for i in range(1,4):
                        playNote()
                        randomRest()
                        randomRest()
                        randomRest()
                if i == 2:
                    for i in range(1,2):
                        playNote()
                if i == 3:
                    for i in range (1,3):
                        playNote()
                if i == 3:
                    for i in range (1,2):
                        playNote()
        if 450 < click.getX() and 460 > click.getY() > 440: #pentatonic
            for i in range(1,4):
                choice = random.choice([1,2,3])
                if i == 1: #sentence
                    for t in range(1,60):
                        i = random.choice([1,2,3,4])
                        if i == 1: #word
                            for i in range(1,4):
                                playPent()
                                randomRest()
                                randomRest()
                                randomRest()
                        if i == 2: #word
                            for i in range(1,2):
                                playPent()
                        if i == 3: #word
                            for i in range (1,2):
                                playPent()
                        if i == 3: #word
                            for i in range (1,3):
                                playPent()

                if i == 2: #sentence
                    for t in range(1,60):
                        i = random.choice([1,2,3,4])
                        if i == 1:
                            for i in range(1,4): #word
                                playPent2()
                                randomRest()
                                randomRest()
                                randomRest()
                        if i == 2:
                            for i in range(1,2): #word
                                playPent2()
                        if i == 3:
                            for i in range (1,2): #word
                                playPent2()
                        if i == 3:
                            for i in range (1,3): #word
                                playPent2()

                if i == 3: #sentence
                    for t in range(1,60):
                        i = random.choice([1,2,3,4])
                        if i == 1:
                            for i in range(1,4): #word
                                playPent3()
                                randomRest()
                                randomRest()
                                randomRest()
                        if i == 2:
                            for i in range(1,2): #word
                                playPent3()
                        if i == 3:
                            for i in range (1,2): #word
                                playPent3()
                        if i == 3:
                            for i in range (1,3): #word
                                playPent3()


            for t in range(1,100):
                i = random.choice([1,2,3,4])
                if i == 1:
                    for i in range(1,4):
                        playPent()
                        randomLongRest()
                if i == 2:
                    for i in range(1,2):
                        playPent()
                if i == 3:
                    for i in range (1,2):
                        playPent()
                if i == 3:
                    for i in range (1,3):
                        playPent()
        if 450 < click.getX() and 440 > click.getY() > 420:#testing

            for i in range(1,20):
                choice = random.choice(range(1,8))
                if choice == 1:
                    choice = random.choice(range(4))
                    if choice == 1:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 2:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 3:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 4:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)

                if choice == 2:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = note0
                        two = note4
                        three = note7
                        playChord(one,two,three)
                    if choice == 2:
                        one = note1
                        two = note5
                        three = note8
                        playChord(one,two,three)
                    if choice == 3:
                        one = note2
                        two = note6
                        three = note9
                        playChord(one,two,three)
                    if choice == 4:
                        one = note3
                        two = note7
                        three = note10
                        playChord(one,two,three)

                if choice == 3:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 2:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 3:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 4:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                if choice == 4:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 2:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 3:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 4:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                if choice == 5:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 2:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 3:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 4:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                if choice == 6:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 2:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 3:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                    if choice == 4:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playRand(one,two,three)
                if choice == 7:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 2:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 3:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 4:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                if choice == 8:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 2:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 3:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
                    if choice == 4:
                        one = pickNote()
                        two = pickNote()
                        three = pickNote()
                        playChord(one,two,three)
            one = pickNote()
            two = pickNote()
            three = pickNote()
            playChord(one,two,three)
        if 450 < click.getX() and 420 > click.getY() > 400: #phrygians
            for i in range(1,20):
                choice = random.choice(range(1,8))
                if choice == 1:
                    choice = random.choice(range(4))
                    if choice == 1:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)

                if choice == 2:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)

                if choice == 3:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 3:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                if choice == 4:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 2:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 4:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                if choice == 5:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 2:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 4:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                if choice == 6:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 2:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                    if choice == 4:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playRand(one,two,three)
                if choice == 7:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 3:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                if choice == 8:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 3:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(phrygians)
                        two = random.choice(phrygians)
                        three = random.choice(phrygians)
                        playChord(one,two,three)
            one = random.choice(phrygians)
            two = random.choice(phrygians)
            three = random.choice(phrygians)
            playChord(one,two,three)
        if 450 < click.getX() and 400 > click.getY() > 380: #locrian
            print("test")
            for i in range(1,100):
                print("test")
                choice = random.choice(range(1,8))
                if choice == 1:
                    choice = random.choice(range(4))
                    if choice == 1:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                if choice == 2:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                if choice == 3:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 3:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                if choice == 4:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 2:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 4:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                if choice == 5:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 2:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 4:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                if choice == 6:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 2:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 3:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                    if choice == 4:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playRand(one,two,three)
                if choice == 7:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 3:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                if choice == 8:
                    choice = random.choice(range(1,4))
                    if choice == 1:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 2:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 3:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
                    if choice == 4:
                        one = random.choice(locrian)
                        two = random.choice(locrian)
                        three = random.choice(locrian)
                        playChord(one,two,three)
            one = random.choice(locrian)
            two = random.choice(locrian)
            three = random.choice(locrian)
            playChord(one,two,three)
        if  230 < click.getX() < 270 and 80 < click.getY() < 120:#0            pygame.mixer.stop()

            zeroCircle.setFill("green")
            note0.play()
            playlist.extend([0])
            play.extend([note0])
        if  305 < click.getX() < 345 and 100 < click.getY() < 140: #1
            pygame.mixer.stop()
            oneCircle.setFill("blue")
            note1.play()
            playlist.extend([1])
            play.extend([note1])
        if  360 < click.getX() < 400 and 155 < click.getY() < 195: #2
            pygame.mixer.stop()
            twoCircle.setFill("purple")
            note2.play()
            playlist.extend([2])
            play.extend([note2])
        if  380 < click.getX() < 420 and 230 < click.getY() < 270: #3
            pygame.mixer.stop()
            threeCircle.setFill("red")
            note3.play()
            playlist.extend([3])
            play.extend([note3])
        if  360 < click.getX() < 400 and 305 < click.getY() < 345: #4
            pygame.mixer.stop()
            fourCircle.setFill("orange")
            note4.play()
            playlist.extend([4])
            play.extend([note4])
        if  305 < click.getX() < 345 and 360 < click.getY() < 400: #5
            pygame.mixer.stop()
            fiveCircle.setFill("yellow")
            note5.play()
            playlist.extend([5])
            play.extend([note5])
        if  230 < click.getX() < 270 and 380 < click.getY() < 420: #6
            pygame.mixer.stop()
            sixCircle.setFill("green")
            note6.play()
            playlist.extend([6])
            play.extend([note6])
        if  155 < click.getX() < 195 and 360 < click.getY() < 400: #7
            pygame.mixer.stop()
            sevenCircle.setFill("blue")
            note7.play()
            playlist.extend([7])
            play.extend([note7])
        if  100 < click.getX() < 140 and 305 < click.getY() < 345: #8
            pygame.mixer.stop()
            eightCircle.setFill("purple")
            note8.play()
            playlist.extend([8])
            play.extend([note8])
        if  80 < click.getX() < 120 and 230 < click.getY() < 270: #9
            pygame.mixer.stop()
            nineCircle.setFill("red")
            note9.play()
            playlist.extend([9])
            play.extend([note9])
        if  100 < click.getX() < 140 and 155 < click.getY() < 195:#10
            pygame.mixer.stop()
            tenCircle.setFill("orange")
            note10.play()
            playlist.extend([10])
            play.extend([note10])
        if  155 < click.getX() < 195 and 100 < click.getY() < 140:#11
            pygame.mixer.stop()
            elevenCircle.setFill("yellow")
            note11.play()
            playlist.extend([11])
            play.extend([note11])

        '''N3P7TSYS WAZ HERE'''
main()
