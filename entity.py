import random
import pygame
import math
import os
import asyncio
import random
pygame.font.init()
textFont0 = pygame.font.SysFont("arial",30)
textFont = pygame.font.SysFont("arial",25)
textFont1 = pygame.font.SysFont("arial",15)
textFont40 = pygame.font.SysFont("arial",40)
textFont25 = pygame.font.SysFont("arial",25)


diceSize = (125,125)
cube1 = pygame.transform.scale(pygame.image.load(os.path.join("assets","cube1.png")),diceSize)
cube2 = pygame.transform.scale(pygame.image.load(os.path.join("assets","cube2.png")),diceSize)
cube3 = pygame.transform.scale(pygame.image.load(os.path.join("assets","cube3.png")),diceSize)
cube4 = pygame.transform.scale(pygame.image.load(os.path.join("assets","cube4.png")),diceSize)
cube5 = pygame.transform.scale(pygame.image.load(os.path.join("assets","cube5.png")),diceSize)
cube6 = pygame.transform.scale(pygame.image.load(os.path.join("assets","cube6.png")),diceSize)

radiusFact = (30,30)
factPicture = pygame.transform.scale(pygame.image.load( os.path.join("assets","fact.png")) ,radiusFact )
factPicture1 = pygame.image.load( os.path.join("assets","fact.png"))
questionPicture = pygame.image.load( os.path.join("assets","question.png") )
gamblePicture = pygame.image.load( os.path.join( "assets","gamble.png" ) )

def winnerMessage(players,initialBank):
    nameWinner =""
    stat = []
    points = 0
    for player in players:
        if not player.isFieldAlive():
            continue
        avgH = (player.healthA + player.healthR + player.healthF)/3*0.7
        avgC = (player.bank)/initialBank*0.3
        mess = f"{player.id}    Health Points:{round(avgH,2)}    Bank Points:{round(avgC,2)}  Total:{round(avgH+avgC,2)}"
        stat.append(mess)
        if avgC+avgH >=points:
            nameWinner = player.id
            points = avgC+avgH

    message0 = f"Winner is: {nameWinner}"
    stat.insert(0,message0)
    return stat

def drawWinner(window,stat):
    w = 1000
    mM = setButton(stat,window.get_width()/2-w/2,200,w,400)
    mM.draw(window)

def checkVertices(x,y,w,h):
    vertices = []
    vertices.append( [x,y+h*2/3] )
    vertices.append( [x+w/3,y+h*3/3] )
    vertices.append( [x+w*3/3,y+h*1/3] )
    vertices.append( [x+w*5/6,y+h*1/6] )
    vertices.append( [x+w*1/3,y+h*2/3] )
    vertices.append( [x+w/6,y+h/2] )
    return vertices

def drawText(surface, text,size, x, y, max_width,):
        font = pygame.font.SysFont("arial",size)
        LINE_SPACING = 1.2 
        FONT_SIZE = font.get_linesize()
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = " ".join([current_line, word]).strip()
            width, _ = font.size(test_line)
            
            if width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        
        lines.append(current_line)
        
        for line in lines:
            text_surface = font.render(line, True, (255,255,255))
            surface.blit(text_surface, (x, y))
            y += int(FONT_SIZE * LINE_SPACING)

def backGroundPolygon(window,color,cordinates,list,edge,angleOffset = 0):
    backG = 0
    for i in list:
        backG+=i

    i = len(list) - 1
    while i>=0:
        pygame.draw.polygon(window,color[i+1],polygon([cordinates[0],cordinates[1]],cordinates[2]+backG,edge,angleOffset))
        backG -= list[i]
        i -= 1
    pygame.draw.polygon(window,color[0],polygon([cordinates[0],cordinates[1]],cordinates[2],edge,angleOffset))

def backText(window,text,size,color,cordinates,list):
    backG = size
    for i in list:
        backG+=i

    i = len(list) - 1
    while i>=0:
        font = pygame.font.SysFont("arial",backG)
        textL = font.render(text,1,color[i+1])
        window.blit(textL,(cordinates[0]-textL.get_width()/2,cordinates[1]-textL.get_height()/2))
        backG -= list[i]
        i -= 1
    font = pygame.font.SysFont("arial",backG)
    textL = font.render(text,1,color[i+1])
    window.blit(textL,(cordinates[0]-textL.get_width()/2,cordinates[1]-textL.get_height()/2))

def backGround(window,color,cordinates,list):
    backG = 0
    for i in list:
        backG+=i

    i = len(list) - 1
    while i>=0:
        pygame.draw.rect(window,color[i+1],(cordinates[0]-backG,cordinates[1]-backG,cordinates[2]+2*backG,cordinates[3]+2*backG))
        backG -= list[i]
        i -= 1
    pygame.draw.rect(window,color[0],cordinates)

def polygon(center,r,edge,angleOffset = 0):
    angle = 2*math.pi / edge
    offset = angleOffset*math.pi/180
    vertice = []

    for i in range(edge):
        angleTmp = i*angle + offset
        dot = [center[0],center[1]]
        dot[0] += r*math.cos(angleTmp)
        dot[1] += r*math.sin(angleTmp)
        vertice.append(dot)
    return vertice

def star(center,rB,rS,edge,angleOffset = 0):
    edge = 2*edge
    angle = 2*math.pi / edge
    r = rS
    small = True
    offset = angleOffset*math.pi/180
    vertice = []
    for i in range(edge):
        angleTmp = i*angle + offset
        dot = [center[0],center[1]]
        dot[0] += r*math.cos(angleTmp)
        dot[1] += r*math.sin(angleTmp)
        vertice.append(dot)
        if small:
            small = False
            r = rB
        else:
            small = True
            r = rS
    return vertice

def starBackground(window,color,cANDr,edge,list,angleOffset = 0):
    backG = 0
    for i in list:
        backG+=i

    i = len(list) - 1
    while i>=0:
        star2 = star((cANDr[0],cANDr[1]),backG+cANDr[2],backG+cANDr[3],edge,angleOffset)
        pygame.draw.polygon(window,color[i+1],star2)
        backG -= list[i]
        i -= 1
    star1 = star((cANDr[0],cANDr[1]),cANDr[2],cANDr[3],edge,angleOffset)
    pygame.draw.polygon(window,color[0],star1)

def umrezi(fieldBeg,numDir,fieldEnd,inB,inE): #ne ukljucuje inE
    fields = []
    for it in range(inB,inE):
            field = FieldInside(it)
            fields.append(field)

    fieldBeg.addDir(1,fields[0])
    fields[0].addDir(1,fieldBeg)
    fieldPrev = fields[0]
    for it in range(inE-inB-1):
        fields[it].addDir(0,fields[it+1])
        fields[it+1].addDir(1,fields[it])            #zadnj it je 0 bio xD

    fields[inE-inB-1].addDir(0,fieldEnd)
    fields[inE-inB-1].addDir(1,fields[inE-inB-2])
    fieldEnd.addDir(numDir,fields[inE-inB-1])     

def vAdd(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have the same length for addition.")
    
    result = tuple(v1 + v2 for v1, v2 in zip(tuple1, tuple2))
    return result

class button():
    def __init__(self,text,x,y,width,height,fontSize=40,color = [(140,140,200),(130,130,180),(90,90,90)]):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fontSize = fontSize
        self.color = color

    def draw(self,window):
        x = self.x
        y = self.y
        w = self.width
        h = self.height

        font = pygame.font.SysFont('arial',self.fontSize)
        backGround(window,self.color,(x,y,w,h),[5,5])
        textLabel = font.render(self.text,1,(235,235,235))
        window.blit(textLabel,(x+w/2-textLabel.get_width()/2,y+h/2-textLabel.get_height()/2))

    def isClicked(self,mouseX,mouseY):
        if self.x <= mouseX <= self.x+self.width and self.y<= mouseY <=self.y + self.height:
            return True
        return False

class setButton():
    def __init__(self,text,x,y,width,height,offset = 30,fontSize = 40):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.offset = offset
        self.buttons = []

        numOfBut = len(self.text)
        hBtn = (self.height-(numOfBut-1)*self.offset)/numOfBut
        
        for i,txt in enumerate(self.text):
            btn = button(txt,self.x,self.y+i*self.offset+i*hBtn,self.width,hBtn,fontSize)
            self.buttons.append(btn)
    
    def createButtons(self):
        numOfBut = len(self.text)
        hBtn = (self.height-(numOfBut-1)*self.offset)/numOfBut
        
        for i,txt in enumerate(self.text):
            btn = button(txt,self.x,self.y+i*self.offset+i*hBtn,self.width,hBtn)
            self.buttons.append(button)

    def draw(self,window):
        for btn in self.buttons:
            btn.draw(window)
    
    def whichClicked(self,mouseX,mouseY):
        for i,btn in enumerate(self.buttons):
            if btn.isClicked(mouseX,mouseY):
                return i

class Field:
    def __init__(self,id):
        self.id = id
        self.label = "none"
        self.fieldX = None
        self.fieldY = None
        self.radius = 25
        self.picture = None

    def draw(self,window,posx,posy,radius=25,color=(120,120,120)):
        self.fieldX = posx
        self.fieldY = posy
        pygame.draw.circle(window,color,(posx,posy),radius)
        #textLabel = textFont.render(f"{self.id}",1,(235,235,235))
        #window.blit(textLabel,(posx-radius/2,posy-radius/2))
        if self.picture!=None:
            window.blit(self.picture,(posx-self.picture.get_width()/2,posy-self.picture.get_height()/2))

    def addLabel(self,label):
        self.label = label

    def __str__(self):
        return str(self.id)
    
    def isItIn(self,mouseX,mouseY):
        rect = self.radius*1.25
        return self.fieldX-rect <= mouseX <= self.fieldX+rect and self.fieldY-rect<=mouseY<=self.fieldY+rect

class Card:
    def execute():
        value = 5

class Fact(Card):
    def __init__(self,fact):
        self.fact = fact
        self.image = pygame.transform.scale( factPicture1, (100,100) )
    
    def execute(self):
        print("Izvukli ste Fact kartu")
        print(self.fact)

    

    def draw(self,window):
        #background
        boxW = 350
        boxH = 500
        x = window.get_width()/2-boxW/2
        y = window.get_height()/2-boxH/2

        backGround(window,[(140,200,140),(130,180,130),(90,90,90)],(x,y,boxW,boxH),[5,5])

        #part for box which posesses text
        offsetX = 10
        offsetY = 10
        backGround(window,[(90,90,90),(210,210,210)],(x+offsetX,y+boxH/3+offsetY,boxW-2*offsetX,boxH*2/3-2*offsetY),[5])

        
        starBackground(window,[(200,200,80),(170,170,100),(120,120,120)],[x+boxW,y,145,100],7,[5,5])
        window.blit(pygame.transform.scale(self.image,(100,100)),(x+boxW-self.image.get_width()/2,y-self.image.get_height()/2))

        #text
        x = x+offsetX
        y = y+boxH/3+offsetY
        drawText(window,self.fact,30,x,y, boxW-2*offsetX)
       
class Destroy(Card):
    def __init__(self,text,segment,addPoints):
        self.text = text
        if segment=="A" or segment=="F" or segment=="R" or segment=="B":
            self.segment = segment
        else:
            self.segment = "B"
        self.addPoints = addPoints

    def execute(self,player):
        print("Izvukli ste Destroy kartu")
        print(self.text)
        if self.segment == "A":
            player.healthA -= self.subPoints
        if self.segment == "F":
            player.healthF -= self.subPoints
        if self.segment == "R":
            player.healthR -= self.subPoints
        if self.segment == "money":
            player.bank -= self.subPoints

    def draw(self,window):
        boxW = 350
        boxH = 500
        x = window.get_width()/2-boxW/2
        y = window.get_height()/2-boxH/2

        backGround(window,[(220,140,140),(180,130,130),(90,90,90)],(x,y,boxW,boxH),[5,5])

        #part for box which posesses text
        offsetX = 10
        offsetY = 10
        backGround(window,[(90,90,90),(210,210,210)],(x+offsetX,y+boxH/3+offsetY,boxW-2*offsetX,boxH*2/3-2*offsetY),[5])

        #text
        x = x+offsetX
        y = y+boxH/3+offsetY
        drawText(window,self.text,30,x,y, boxW-2*offsetX)

        #representative of bad card
        x = window.get_width()/2-boxW/2
        y = window.get_height()/2-boxH/2
        boxW1 = boxW/2
        boxH1 = boxW/2
        backGroundPolygon(window,[(220,100,100),(235,235,235)],[x+boxW,y,120],[12],8)
        signW = 35
        pygame.draw.rect(window,(235,235,235),(x+boxW-signW/2,y-3*signW,signW,4*signW))
        pygame.draw.rect(window,(235,235,235),(x+boxW-signW/2,y+2*signW,signW,signW))
        
class Good(Card):
    def __init__(self,text,segment,addPoints):
        self.text = text
        if segment=="A" or segment=="F" or segment=="R" or segment=="B":
            self.segment = segment
        else:
            self.segment = "B"
        self.addPoints = addPoints

    def execute(self,player):
        print("Izvukli ste Good kartu")
        print(self.text)
        if self.segment == "A":
            player.healthA += self.addPoints
        if self.segment == "F":
            player.healthF += self.addPoints
        if self.segment == "R":
            player.healthR += self.addPoints
        if self.segment == "money":
            player.bank += self.addPoints

    def draw(self,window):
        boxW = 350
        boxH = 500
        x = window.get_width()/2-boxW/2
        y = window.get_height()/2-boxH/2

        backGround(window,[(140,200,140),(130,180,130),(90,90,90)],(x,y,boxW,boxH),[5,5])

        #part for box which posesses text
        offsetX = 10
        offsetY = 10
        backGround(window,[(90,90,90),(210,210,210)],(x+offsetX,y+boxH/3+offsetY,boxW-2*offsetX,boxH*2/3-2*offsetY),[5])

        #text
        x = x+offsetX
        y = y+boxH/3+offsetY
        drawText(window,self.text,30,x,y, boxW-2*offsetX)

        #representative of good card
        x = window.get_width()/2-boxW/2
        y = window.get_height()/2-boxH/2
        boxW1 = boxW/2
        boxH1 = boxW/2
        backGround(window,[(100,220,100),(150,240,150),(235,235,235)],[x+boxW-boxW1/2,y-boxH1/2,boxW1,boxH1],[10,10])
        check = checkVertices(x+boxW-boxW1/2,y-boxH1/2,boxW1,boxH1)
        pygame.draw.polygon(window,(230,230,230),check)

class Question(Good):
    def __init__(self,text,segment,addPoints,answers,correct):    #prvo text, zatim sta povecava,sumu novac pare(A,F,R,B), koliko dodaje, ponudjeni odgovori 2-4, koji je tacan 1-4
        super().__init__(text,segment,addPoints)
        self.answers = answers
        self.correct = correct
        self.image = pygame.transform.scale(questionPicture,(100,100))
        self.answerCord = None

    def execute(self,player):
        print("Izvukli ste Question kartu")
        print(self.text)
        for a in self.answers:
            print(a)
        answer = input()        #odg sa 1,2,3,...
        if answer == self.correct:
            print("Odgovor je tacan!")
            if self.segment == "A":
                player.healthA += self.addPoints
            if self.segment == "F":
                player.healthF += self.addPoints
            if self.segment == "R":
                player.healthR += self.addPoints
            if self.segment == "money":
                player.bank += self.addPoints
        else:
            print("Netacno")

    def setAnswerCord(self):
        self.answerCord = [[305.0, 350.0, 600, 25],
                    [305.0, 415.0, 600, 25],
                    [305.0, 480.0, 600, 25],
                    [305.0, 545.0, 600, 25]
            ]

    def execute1(self,mouseX,mouseY): #1 ako je tacan, 0 ako nije, -1 nije kliknuo dje treba
        for i,coor in enumerate(self.answerCord):
            print(coor[0],coor[0]+coor[2],coor[1],coor[1]+coor[3])
            if coor[0] <= mouseX <= coor[0] +coor[2] and coor[1] <= mouseY <=coor[1] +coor[3]:
                if int(self.correct) == i+1:
                    return 1
                else :return 0
        return -1

    def draw(self,window):
        picSize = (100,100)                               #velicina logoa gornji desni ugao
        textSize = 25
        boxW = 600
        boxH = 450
        x = window.get_width()/2-boxW/2
        y = window.get_height()/2-boxH/2

        textFont1 = pygame.font.SysFont("arial",textSize)

        off = 14/13
        starBackground(window,[(200,200,80),(170,170,100),(120,120,120)],[x+boxW*off,y,120,85],7,[5,5])
        window.blit(pygame.transform.scale(self.image,picSize),(x+boxW*off-self.image.get_width()/2,y-self.image.get_height()/2))

        backGround(window,[(140,200,140),(130,180,130),(90,90,90)],(x,y,boxW,boxH),[5,5])

        #part for box which posesses text
        offsetX = 10
        offsetY = 10
        backGround(window,[(90,90,90),(210,210,210)],(x+offsetX,y+offsetY,boxW-2*offsetX,boxH/3),[5])

        
        #starBackground(window,[(200,200,80),(170,170,100),(120,120,120)],[x+boxW,y,100,65],7,[5,5])
        #window.blit(self.image,(x+boxW-self.image.get_width()/2,y-self.image.get_height()/2))
        
        x = x+offsetX
        y = y+offsetY
        drawText(window,self.text,textSize,x,y, boxW-2*offsetX)

        x = x
        y = y + boxH/3 + 2*offsetY
        answerPartH = boxH-4*offsetY - boxH/3
        offsetAnswer = answerPartH/4


        colors = [ 
            None,
            [(200,120,120),(170,90,90),(140,70,70)],
            [(120,200,120),(90,170,90),(70,140,70)],
            [(120,120,200),(90,90,170),(70,70,140)],
            [(150,80,150),(130,70,130),(120,60,120)]
         ]
        for i,answer in enumerate(self.answers):
            backGround(window,colors[i+1],(x,y+i*offsetAnswer,20,20),[2,3])
            textLabel = textFont1.render(answer,1,(255,255,255))
            backGround(window,[(120,120,120),(90,90,90)],(x+25 + offsetX,y+i*offsetAnswer-2,boxW-2*offsetX -3*offsetX,25),[3])
            window.blit(textLabel,(x+25+offsetX,y+i*offsetAnswer-4))
            print(x-5,y+i*offsetAnswer-5,boxW,14)

class Deck():
    def __init__(self,questionList,factList,destroyList,goodList):
        self.questionList = questionList
        self.factList = factList
        self.destroyList = destroyList
        self.goodList = goodList

    def giveAppropriateCard(self,type):
        if type=="question":
            limit = len(self.questionList)
            card =  self.questionList[random.randrange(0,limit)]
            return card
        if type=="fact":
            limit = len(self.factList)
            card = self.factList[random.randrange(0,limit)]
            return card
        if type=="gamble":
            slucajno = random.randrange(0,2)
            if slucajno == 0:
                limit = len(self.goodList)
                card = self.goodList[random.randrange(0,limit)]
                return card
            elif slucajno ==1:
                limit = len(self.destroyList)
                card = self.destroyList[random.randrange(0,limit)]
                return card
        
class FieldReg(Field):
    def __init__(self, id):
        super().__init__(id)
        self.dir = [None]

    def addDir(self,position,field):
        if position != 0:
            print("Error index out of bounds")
        self.dir[position] = field

class FieldTurn(Field):
    def __init__(self,id):
        Field.__init__(self,id)
        self.dir = [None,None]       #0 is straight, 1 is turn on
        self.radius = 35
        self.picture = None

    def draw(self,window,posx,posy,radius=35,color=(180,180,180)):
        self.fieldX = posx
        self.fieldY = posy
        pygame.draw.circle(window,color,(posx,posy),radius)
        #textLabel = textFont.render(f"{self.id}",1,(235,235,235))
        #window.blit(textLabel,(posx-radius/2,posy-radius/2))
        if self.picture!=None:
            window.blit(self.picture,(posx-self.picture.get_width()/2,posy-self.picture.get_height()/2))
        

    def addDir(self,position,field):
        if position>1 or position<0:
            print("Error index out of bounds")
        self.dir[position] = field

class FieldCenter(Field):
    def __init__(self, id):
        super().__init__(id)
        self.dir = [None,None,None,None]
        self.radius = 35
        self.picture = None

    def draw(self,window,posx,posy,radius=35,color=(180,180,180)):
        self.fieldX = posx
        self.fieldY = posy
        pygame.draw.circle(window,color,(posx,posy),radius)
        #textLabel = textFont.render(f"{self.id}",1,(235,235,235))
        #window.blit(textLabel,(posx-radius/2,posy-radius/2))
        if self.picture!=None:
            window.blit(self.picture,(posx-self.picture.get_width()/2,posy-self.picture.get_height()/2))
        

    def addDir(self,position,field):
        if position>3 or position<0:
            print("Error index out of bounds")
        self.dir[position] = field            #0 is path which starts in 0, 1 starts at 7, 2 at 14...

class FieldInside(Field):
    def __init__(self, id):
        super().__init__(id)
        self.dir = [None,None]
    
    def addDir(self,position,field):  #0 za ulazenje, 1 za ilazenje
        if position>1 or position<0:
            print("Error index out of bounds")
        self.dir[position] = field

def insideList(list,item):
    for i in list:
        if i==item:
            return True
    return False

class Map():
    def __init__(self,field):
        self.startingPoint = field
        self.centar = None
        self.outside = []   #od 0,1,2,..27
        self.inside = []    #100,101,...403
        self.insideA = []   #u 0 je 100,200,300 u 1 101,201,301 ovo se namesti sve nakon poziva printMap

    def setField(self):
        index = [5,10,15,20,25]
        choosen = []   

        i = 0     
        while i < 5:
            num = random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10,21,22,23,24,25,26,27,100,101,102,103,201,202,203,300,301,302,303,401,402,403,400,44])
            if not insideList(choosen,num):
                choosen.append(num)
                i += 1
                field = self.getField(num)
                field.picture = factPicture
                field.label = "fact"
            
        i = 0     
        while i < 5:
            num = random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10,21,22,23,24,25,26,27,100,101,102,103,201,202,203,300,301,302,303,401,402,403,400,44])
            if not insideList(choosen,num):
                choosen.append(num)
                i += 1
                field = self.getField(num)
                field.picture =pygame.transform.scale( questionPicture,(50,50))
                field.label = "question"
        
        i = 0     
        while i < 5:
            num = random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10,21,22,23,24,25,26,27,100,101,102,103,201,202,203,300,301,302,303,401,402,403,400,44])
            if not insideList(choosen,num):
                choosen.append(num)
                i += 1
                field = self.getField(num)
                field.picture = pygame.transform.scale(gamblePicture,(50,50))
                field.label = "gamble"

        

        #for fieldN in range(0,28): #for fieldN in index
         #   field = self.getField(fieldN)
         #   field.picture = pygame.transform.scale( questionPicture,(50,50))
          #  field.label = "question"
        #for fieldN in range(0,28): #for fieldN in index
         #   field = self.getField(fieldN)
          #  field.picture = pygame.transform.scale( gamblePicture,(50,50))
           # field.label = "gamble"

    def colorNextLoc(self,window,destinations,color):
        for fieldN in destinations:
            field = self.getField(fieldN)
            radius = field.radius
            field.draw(window,field.fieldX,field.fieldY,radius*1.25,color)

    def draw(self,window,WIDTH,HEIGHT):
        radius = 300
        center = (WIDTH/2,HEIGHT/2)
        
        pom = 2*math.pi/28
        rotationCircle = -10.5*pom

        for i in range(28):
            field = self.outside[i]
            angle = i*pom + rotationCircle
            field.draw(window,center[0]+radius*math.cos(angle),center[1]+radius*math.sin(angle))
            
        pom = 2*math.pi/4
        changeORad = 300/5
        for list in self.insideA:
            radius -= changeORad
            i = 0
            for field in list:
                angle = i*pom + rotationCircle
                field.draw(window,center[0]+radius*math.cos(angle),center[1]+radius*math.sin(angle))
                i+=1
        self.centar.draw(window,center[0],center[1])
        
    

        


    def createBasic(self):
        #Constant
        numCircle = 28

        #kreiranje mape
        arrayFiTu = [FieldTurn(0),FieldTurn(7),FieldTurn(14),FieldTurn(21)]
        index = 0
        fieldPrev = arrayFiTu[0]
        for it in range(1,numCircle):
            if it%7!=0:
                field = FieldReg(it)
                fieldPrev.addDir(0,field)
                fieldPrev = field
            else:
                index+=1
                fieldPrev.addDir(0,arrayFiTu[index])
                fieldPrev = arrayFiTu[index]
        fieldPrev.addDir(0,arrayFiTu[0])

        fieldC = FieldCenter(44)
        self.centar = fieldC
         

        umrezi(arrayFiTu[0],2,fieldC,100,104)
        umrezi(arrayFiTu[1],3,fieldC,200,204)
        umrezi(arrayFiTu[2],0,fieldC,300,304)
        umrezi(arrayFiTu[3],1,fieldC,400,404)

        arrayFiTu[0].label = "question"
        arrayFiTu[1].label = "gamble"
        arrayFiTu[2].label = "gamble"
        arrayFiTu[3].label = "fact"
        self.startingPoint = arrayFiTu[0]

    def printMap(self):
        field = self.startingPoint
        fieldTmp = self.startingPoint
        repeated = 0
        while fieldTmp != field or repeated==0:
            repeated = 1
            print(fieldTmp.id,end=" ")
            self.outside.append(fieldTmp)

            if type(fieldTmp) == FieldTurn:
                print()
                print("[",end=" ")
                if fieldTmp.dir[1] != None:
                    fieldTmp1 = fieldTmp.dir[1]

                    while type(fieldTmp1) != FieldCenter:
                        print(fieldTmp1.id,end=" ")
                        self.inside.append(fieldTmp1)
                        fieldTmp1 = fieldTmp1.dir[0]
                print("]")

            fieldTmp = fieldTmp.dir[0]
        inside0 = []
        inside1 =  []
        inside2 = []
        inside3 = []
        for i in range(4):
            inside0.append(self.inside[i*4])
            inside1.append(self.inside[i*4+1])
            inside2.append(self.inside[i*4+2])
            inside3.append(self.inside[i*4+3])
        self.insideA.append(inside0)
        self.insideA.append(inside1)
        self.insideA.append(inside2)
        self.insideA.append(inside3)


    
    def movement(self,field):
        fieldTmp = field
        while True:
            print("ID:",fieldTmp.id)
            print("Mozes da se kreces:",end=" ")
            length = len(fieldTmp.dir)
            for pos in range(length):
                print(fieldTmp.dir[pos],end=" ")
            direction = int(input())
            if direction==-1:
                break
            for pos in range(length):
                if direction==fieldTmp.dir[pos].id:
                    fieldTmp = fieldTmp.dir[pos]
                    break    
    def movement1(self,player):
        while True:
            print("ID:",player.location)
            print("Mozes da se kreces:",end=" ")
            directions = self.nextFields1(player,1)
            print(directions)
            direction = int(input())
            if direction==-1:
                break

            fieldTmp = self.getField(player.location)
            length = len(fieldTmp.dir)
            for pos in range(length):
                if direction==fieldTmp.dir[pos].id:
                    player.location = fieldTmp.dir[pos].id
                    break 
    
    def getField(self,id):
        field = self.startingPoint
        fieldTmp = self.startingPoint
        repeated = 0
        while fieldTmp != field or repeated==0:
            repeated = 1
            if fieldTmp.id==id:
                return fieldTmp

            if type(fieldTmp) == FieldTurn:
                
                if fieldTmp.dir[1] != None:
                    fieldTmp1 = fieldTmp.dir[1]

                    while type(fieldTmp1) != FieldCenter:
                        if fieldTmp1.id==id:
                            return fieldTmp1
                        fieldTmp1 = fieldTmp1.dir[0]
                    if fieldTmp1.id==id:
                        return fieldTmp1

            fieldTmp = fieldTmp.dir[0]

    def nextFields(self,fieldB,roll):
        destinations = []
        posecen = [False]*500
        posecen[fieldB.id] = True

        queue = []
        queue.append([fieldB,0])

        while queue:
            par = queue.pop(0)

            if par[1]==roll:
                destinations.append(par[0].id)
            for nextField in par[0].dir:

                if posecen[nextField.id]==False:
                    posecen[nextField.id]=True
                    queue.append([nextField,par[1]+1])

        return destinations

    def function(number):
        if number>=1 and number <=7:
            return [200,201,202,203]
        elif number>=8 and number <= 14:
            return [300,301,302,303]
        elif number>=15 and number<=21:
            return [400,401,402,403]
        elif (number>=22 and number<=27) or number == 0:
            return [100,101,102,103]

    def nextFields1(self,player,roll):
        if player.location==-1:
            return
        if player.location>=0 and player.location<=27:
            player.inside = True

        fieldB = self.getField(player.location)
        destinations = []
        posecen = [False]*500
        posecen[fieldB.id] = True

        queue = []
        queue.append([fieldB,0])

        while queue:
            par = queue.pop(0)          #par se sastoji iz polja i koliko je polje udaljeno od fieldB

            if type(par[0]) == FieldCenter:
                player.inside = False
            if par[1]==roll:
                destinations.append(par[0].id)
            
            i = 0
            n = len(par[0].dir)
            while i<n:
                if type(par[0])==FieldInside and player.inside==True and i==1:
                    i+=1
                    continue
                if type(par[0])==FieldInside and player.inside==False and i==0:
                    i+=1
                    continue
                if posecen[par[0].dir[i].id]==False and par[1]<roll:
                    posecen[par[0].dir[i].id]=True
                    queue.append([par[0].dir[i],par[1]+1])
                i+=1
        
        return destinations

class Player:
    def __init__(self,id,startingPoint,x,y,imageX,imageY,color):
        self.id = id
        self.plays = False
        self.turn = False
        self.location = -1
        self.startingPoint = startingPoint
        self.bank = 1500
        self.beforeLocation = -1
        self.inside = True

        self.x = x
        self.y = y
        self.imageX = imageX
        self.imageY = imageY
        self.color = color

        self.healthF = 100
        self.healthR = 100
        self.healthA = 100
        self.factories = [0,0,0,0,0,0]

        self.varThatHelpsForLosing = True

    def eat(self,players):
        for p in players:
            if p == self:
                continue
            if self.location == p.location:
                p.location = -1
                p.plays = False

    def draw(self,window,field=None):
        x = self.imageX
        y = self.imageY
        
        darker = (-60,-60,-60)
        if not self.plays:
            w = 80
            h = 60
            if x<600:
                x1 = x + 180
                y1 = y + 50
                pygame.draw.circle(window,vAdd(self.color,darker),(x1+w*3/5,y1+h/2),19)
                pygame.draw.circle(window,self.color,(x1+w*3/5,y1+h/2),15)
            else:
                x1 = x -60
                y1 = y +50
                pygame.draw.circle(window,vAdd(self.color,darker),(x1+w*2/5,y1+h/2),19)
                pygame.draw.circle(window,self.color,(x1+w*2/5,y1+h/2),15)
        else:
            posx = field.fieldX
            posy = field.fieldY
            pygame.draw.circle(window,vAdd(self.color,darker),(posx,posy),19)
            pygame.draw.circle(window,self.color,(posx,posy),15)

    def drawImage(self,window,shopList):
        x = self.imageX
        y = self.imageY
        whiteC = (235,235,235)

        if self.turn:
            pygame.draw.rect(window,self.color,(self.imageX-20,self.imageY-20,240,340),0,10)

        wBank = 150
        hBank = 60
        inPlayer = 20
        outsideB = 6
        outsideColor = (60,60,60)
        xPom = 3
        if y<400:
            pygame.draw.rect(window,outsideColor,(xPom+x-outsideB,y+300-inPlayer-outsideB,wBank+2*outsideB,hBank+2*outsideB),0,15)
            pygame.draw.rect(window,(120,120,120),(xPom+x,y+300-inPlayer,wBank,hBank),0,15)
            textBank = textFont0.render(f"{self.bank}",1,whiteC)
            window.blit(textBank,(xPom+x+10,y+300+5))
        else:
            pygame.draw.rect(window,outsideColor,(xPom+x-outsideB,y-hBank+inPlayer-outsideB,wBank+2*outsideB,hBank+2*outsideB),0,15)
            pygame.draw.rect(window,(120,120,120),(xPom+x,y-hBank+inPlayer,wBank,hBank),0,15)
            textBank = textFont0.render(f"{self.bank}",1,whiteC)
            window.blit(textBank,(xPom+x+10,y-hBank+inPlayer))

        if x<600:
            pygame.draw.rect(window,(120,120,120),(x+180,y+50,80,60),0,15)
        else:
            pygame.draw.rect(window,(120,120,120),(x-60,y+50,80,60),0,15)

        pygame.draw.rect(window,(200,200,80),(self.imageX-5,self.imageY-5,210,310),0,10)
        pygame.draw.rect(window,(255,255,100),(self.imageX,self.imageY,200,300),0,10)
        #if self.plays:
         #   backGround(window,[colo])
        pygame.draw.rect(window,(120,120,120),(self.imageX+15,self.imageY+15,170,40),0,3)
        textLabel = textFont.render(f"{self.id}",1,(235,235,235))
        window.blit(textLabel,(self.imageX+20,self.imageY+20))
        
        pygame.draw.rect(window,(120,120,120),(x + 15,y + 70,170,30))
        pygame.draw.rect(window,(120,120,120),(x+15,y + 105,170,30))
        pygame.draw.rect(window,(120,120,120),(x+15,y + 140,170,30))
        
        textLabel1 = textFont1.render("Air",1,(235,235,235))
        window.blit(textLabel1,(x+15,y+70))
        pygame.draw.rect(window,(180,180,240),(x+15,y+85,170*self.healthA/100,15))

        textLabel1 = textFont1.render("Forest",1,(235,235,235))
        window.blit(textLabel1,(x+15,y+105))
        pygame.draw.rect(window,(100,240,100),(x+15,y+120,170*self.healthF/100,15))

        textLabel1 = textFont1.render("River",1,(235,235,235))
        window.blit(textLabel1,(x+15,y+140))
        pygame.draw.rect(window,(100,100,240),(x+15,y+155,170*self.healthR/100,15))

        dimBox = (x+15+7,y+185,156,100)
        backGround(window,[(50,50,50),(100,100,100),(150,150,150)],dimBox,(3,4))
        
        boxW = dimBox[2]/3
        boxH = dimBox[3]/2
        sizePic = (30,30)
        con = 25
        x = dimBox[0]
        y = dimBox[1]
        i = 0
        j = 0
        while i<2:
            while j<3:
                image = pygame.transform.scale(shopList[j+i*3].image,sizePic)
                window.blit(image,(x+j*boxW+boxW/2-image.get_width()/2,y+i*boxH+boxH/2-image.get_height()/2))
                textLabel = textFont1.render(f"x{self.factories[j+i*3]}",1,(235,235,235))
                window.blit(textLabel,(x+j*boxW+boxW/2-image.get_width()/2+con,y+i*boxH+boxH/2-image.get_height()/2+con))
                j+=1
            i+=1
            j=0
            
    def damageProces(self,shopList):
        for i,factory in enumerate(shopList):
            if self.healthA - self.factories[i]*factory.damageA<=0:
                self.healthA=0
            else:
                self.healthA -= self.factories[i]*factory.damageA
            if self.healthF - self.factories[i]*factory.damageA<=0:
                self.healthF=0
            else:
                self.healthF -= self.factories[i]*factory.damageA
            if self.healthR - self.factories[i]*factory.damageA<=0:
                self.healthR=0
            else:
                self.healthR -= self.factories[i]*factory.damageA
            self.bank += self.factories[i]*factory.income
    
    def update(self,what,howMuch):
        if what == 'B':
            self.bank+=howMuch
        if what == 'A':
            if self.healthA + howMuch >= 100:
                self.healthA = 100
            else: 
                self.healthA = self.healthA + howMuch
        if what == 'F':
            if self.healthF + howMuch >= 100:
                self.healthF = 100
            else: 
                self.healthF = self.healthF + howMuch
        if what == 'R':
            if self.healthR + howMuch >= 100:
                self.healthR = 100
            else: 
                self.healthR = self.healthR + howMuch
    def isFieldAlive(self):
        if self.healthA <= 0 or self.healthF <= 0 or self.healthR <= 0 :
            return False
        return True
    
    def __str__(self):
        string  = str(self.id) + " " + str(self.location) + " "+ str(self.bank)+ " " +str(self.healthA)+ " "+str(self.healthR)+ " "+str(self.healthF)+ " "
        return string

class Factory:    #damage Air,Forest,River
    def __init__(self,name,eco,damageA,damageF,damageR,price,income,image):
        self.name = name
        self.eco = eco
        self.damageA = damageA
        self.damageF = damageF
        self.damageR = damageR
        self.price = price
        self.income = income
        velicina = (50,50)
        self.image = pygame.transform.scale(image,velicina)

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Eco: {self.eco}\n"
                f"DamageA: {self.damageA}\n"
                f"DamageF: {self.damageF}\n" 
                f"DamageR: {self.damageR}\n"
                f"Price: {self.price}")

shopImg = pygame.transform.scale(pygame.image.load(os.path.join("assets","shop.png")),diceSize)

class Shop():
    def __init__(self,list,W,H):
        self.image = shopImg
        self.list = list
        self.listImg = None
        self.open = False
        self.x = W/2-self.image.get_width()/2
        self.y = H/2+2.5*H/10-self.image.get_height()/2
        div = 12
        self.shopRect = (W/div,W/div,W-2*W/div,H-2*W/div)
        self.buyPos = [(292.2222222222222, 238.0, 60, 60), (625.5555555555555, 238.0, 60, 60), (958.8888888888888, 238.0, 60, 60), (292.2222222222222, 538.0, 60, 60), (625.5555555555555, 538.0, 60, 60), (958.8888888888888, 538.0, 60, 60)]

    def isClickBuy(self,mouseX,mouseY,player):
        for i,cor in enumerate(self.buyPos):
            if cor[0]<=mouseX<=cor[0]+cor[2] and cor[1]<=mouseY<=cor[1]+cor[3]:
                if player.bank>=self.list[i].price:
                    player.bank -= self.list[i].price
                    player.factories[i]+=1
                    return i
                else:
                    return 100 #spec poruka nemas para
        return -1

    def isItIn(self,mouseX,mouseY,W,H):
        
        return  self.x <= mouseX <= self.x+self.image.get_width() and self.y<=mouseY<=self.y+self.image.get_height()

    def isItInRect(self,mouseX,mouseY):
        return self.shopRect[0]<=mouseX<=self.shopRect[0]+self.shopRect[2] and self.shopRect[1]<=mouseY<=self.shopRect[1]+self.shopRect[3]
    def draw(self,window,W,H,color1):
        color = (120,120,120,50)
        window.blit(self.image,(W/2-self.image.get_width()/2,H/2+2.5*H/10-self.image.get_height()/2))
        shopM = pygame.Surface((self.shopRect[2],self.shopRect[3]))
        shopM.fill(color)
        shopM.set_alpha(255*3/4)
        if self.open:
            x = self.shopRect[0]
            y = self.shopRect[1]
            width = self.shopRect[2]
            height = self.shopRect[3]
            window.blit(shopM,(self.shopRect[0],self.shopRect[1]))
            facX = x
            facY = y
            facW = width/3
            facH = height/2
            for j,factory in enumerate(self.list):
                
                #pygame.draw.rect(window,(random.randrange(1,100),random.randrange(1,100),random.randrange(1,100)),(facX,facY,facW,facH))

                boxW = facW*2/3
                boxH = facH*2/3
                backG = 7
                titleF = (boxW*3/5,30)
                bindTextBack = (facX+facW/2-boxW/2+10,facY+facH/2-boxH/2+30)

                pygame.draw.rect(window,(170,170,50),(facX+facW/2+-boxW/2-backG,facY+facH/2-boxH/2-backG,boxW+2*backG,boxH+2*backG),0,10)
                pygame.draw.rect(window,color1[j],(facX+facW/2-boxW/2,facY+facH/2-boxH/2,boxW,boxH),0,10)

                pygame.draw.rect(window,(120,120,120),(bindTextBack[0],bindTextBack[1],titleF[0],titleF[1]),0,3)
                textLabel = textFont.render(f"{factory.name}",1,(235,235,235))
                window.blit(textLabel,(bindTextBack[0]+5,bindTextBack[1]))

                window.blit(factory.image,(facX+facW/2-boxW/2+boxW-1.2*factory.image.get_width(),facY+facH/2-boxH/2+13))
                
                spaceBet = 5
                spaceBetIn = 3
                miss = 0
                backG3 = 2
                textBar = (bindTextBack[0],bindTextBack[1]+titleF[1]+spaceBet,titleF[0]*4/5,titleF[1]*3/5)
                for i in range(0,5):
                    if i == 3: 
                        spaceBetIn = 5
                    backGround(window,[(120,120,120)],(textBar[0],textBar[1]+i*spaceBetIn+i*textBar[3],textBar[2],textBar[3]),[])
                    #pygame.draw.rect(window,(180,180,180),(textBar[0]-backG3,textBar[1]+i*spaceBetIn+i*textBar[3]-backG3,textBar[2]+2*backG3,textBar[3]+2*backG3))
                    #pygame.draw.rect(window,(120,120,120),(textBar[0],textBar[1]+i*spaceBetIn+i*textBar[3] + miss,textBar[2],textBar[3]))
                    
                    

                textLabel1 = textFont1.render(f"Air: {factory.damageA}",1,(235,235,235))
                window.blit(textLabel1,(textBar[0],textBar[1]))
                pygame.draw.rect(window,(180,180,240),(facX,facY,30,15))

                textLabel1 = textFont1.render(f"Forest: {factory.damageF}",1,(235,235,235))
                window.blit(textLabel1,(textBar[0],textBar[1]+1*spaceBetIn+1*textBar[3]))
                pygame.draw.rect(window,(100,240,100),(facX,facY,30,15))

                textLabel1 = textFont1.render(f"River: {factory.damageF}",1,(235,235,235))
                window.blit(textLabel1,(textBar[0],textBar[1]+2*spaceBetIn+2*textBar[3]))
                pygame.draw.rect(window,(100,100,240),(facX,facY,30,15))

                textLabel1 = textFont1.render(f"Income: {factory.income}",1,(235,235,235))
                window.blit(textLabel1,(textBar[0],textBar[1]+3*spaceBetIn+3*textBar[3]))

                textLabel1 = textFont1.render(f"Price: {factory.price}",1,(235,235,235))
                window.blit(textLabel1,(textBar[0],textBar[1]+4*spaceBetIn+4*textBar[3]))

                buyS = (60,60)
                backG1 = 7
                backG2 = 4
                pygame.draw.rect(window,(120,120,120),(facX+facW*2/3-buyS[0]/2-backG1,facY+facH/2-buyS[1]*1/5-backG1,buyS[0]+2*backG1,buyS[1]+2*backG1),0,10)
                pygame.draw.rect(window,(180,180,70),(facX+facW*2/3-buyS[0]/2-backG2,facY+facH/2-buyS[1]*1/5-backG2,buyS[0]+2*backG2,buyS[1]+2*backG2),0,10)
                pygame.draw.rect(window,(255,255,150),(facX+facW*2/3-buyS[0]/2,facY+facH/2-buyS[1]*1/5,buyS[0],buyS[1]),0,10)
                
                textLabel1 = textFont40.render("Buy",1,(100,100,100))
                window.blit(textLabel1,(facX+facW*2/3-buyS[0]/2,facY+facH/2-buyS[1]*1/5+5))
                
                facX += facW
                if facX-10>=width:
                    facY+=facH
                facX %= width
            
            
                
class Dice:
    cubes = [cube1,cube2,cube3,cube4,cube5,cube6]
    imageX = 0
    imageY = 0
    def roll(self):
        return random.randrange(1,7)
    
    def ini(self,x,y):
        self.imageX = x
        self.imageY = y

    def draw(self,window,W,H,roll):
        cube = self.cubes[roll-1]
        window.blit(cube,(W/2-cube.get_width()/2,H/2-2.5*H/10-cube.get_height()/2))
        imageX = W/2-cube.get_width()/2
        imageY = H/2-2.5*H/10-cube.get_height()/2

    def isItIn(self,mouseX,mouseY):
        return  self.imageX <= mouseX <= self.imageX+self.cubes[0].get_width() and self.imageY<=mouseY<=self.imageY+self.cubes[0].get_height()
  

class Game:
    def __init__(self,map,players,shop,deck):
        self.map = map
        self.players = players
        self.shops = shop
        self.deck = deck

    def kupovina(self,player):
        print("Da li zelis da kupujes: ",end="")
        response = int(input())
        if response==1:
            print()
            for shop in self.shops:
                print(shop)
                print()
            while True:
                chose = input()
                if chose=='0':
                    break
                for shop in self.shops:
                    if chose==shop.name:
                        if player.bank >= shop.price:
                            player.factories.append(shop)
                            player.bank -= shop.price
                            print("Kupio si",shop.name)
                print(player)

                        
    def fieldProperty(self,player):
        field = self.map.getField(player.location)
        if field.label=="question":
            self.deck.giveAppropriateCard("question",player)
        if field.label=="fact":
            self.deck.giveAppropriateCard("fact",player)
        if field.label=="gamble":
            number = random.randrange(0,2)
            if number==1:
                self.deck.giveAppropriateCard("destroy",player)
            elif number==0:
                self.deck.giveAppropriateCard("good",player)
        print(player)

    #unos: polja, -2 izlaz, -3 kupovina
    def run(self,window,width,height):

        while True:
            
            for player in self.players:
                print("Player:",player.id)
                roll = Dice.roll(self)

                if player.plays == False:
                    player.draw(window)
                    player.damageProces()
                    if  not player.isFieldAlive():
                        print("Zao nam je ",player.id," ali tvoja zemlja je unistena")
                        self.players.remove(player)
                        continue
                    print(" Nisi u igri, moras da dobijes 6")
                    print(" Dobio si",roll )
                    if roll == 6:
                        print(" U igri si")
                        player.plays = True
                        player.location = player.startingPoint

                while player.plays: 
                    player.damageProces()
                    if  not player.isFieldAlive():
                        print("Zao nam je ",player.id," ali tvoja zemlja je unistena")
                        self.players.remove(player)
                        break
                    #player.draw()#####
                    print(" Trenutn na pozicija:",player.location,", broj para:",player.bank,player.healthA,player.healthF,player.healthR)
                    roll = Dice.roll(self)
                    print(" Dobio si:",roll)
                    print("Mozes da ides: ",self.map.nextFields1(player,roll))
                    #print(" Mozes da ides:",map.nextFields(map.getField(player.location),roll),end=" ")
                    player.beforeLocation = player.location
                    player.location = int(input())

                    #

                    if player.location == -2:
                        exit()

                    self.kupovina(player)
                    self.fieldProperty(player)
                    
                    if roll != 6:
                        break         
       
#Constant
numCircle = 28

#kreiranje mape
arrayFiTu = [FieldTurn(0),FieldTurn(7),FieldTurn(14),FieldTurn(21)]
index = 0
fieldPrev = arrayFiTu[0]
for it in range(1,numCircle):
    if it%7!=0:
        field = FieldReg(it)
        fieldPrev.addDir(0,field)
        fieldPrev = field
    else:
        index+=1
        fieldPrev.addDir(0,arrayFiTu[index])
        fieldPrev = arrayFiTu[index]
fieldPrev.addDir(0,arrayFiTu[0])

fieldC = FieldCenter(44)
  

umrezi(arrayFiTu[0],2,fieldC,100,104)
umrezi(arrayFiTu[1],3,fieldC,200,204)
umrezi(arrayFiTu[2],0,fieldC,300,304)
umrezi(arrayFiTu[3],1,fieldC,400,404)

arrayFiTu[0].label = "question"
arrayFiTu[1].label = "gamble"
arrayFiTu[2].label = "gamble"
arrayFiTu[3].label = "fact"

#map = Map(arrayFiTu[0])
#map.printMap()

#for i in map.outside:
#    print(i.id)
#for i in map.inside:
#    print(i.id,end=" ")
#field = map.getField(0)  
#map.movement(field)

#player = Player(5,0)
#player.location = 0
#player.inside = True
#print(map.nextFields1(player,6))
#print(map.nextFields(map.getField(44),4))
#map.movement1(player)

"""
#test factories 
print()
player = Player(5,0)
f1 = Factory(False,20,10,5,100)
f2 = Factory(False,10,10,10,100)
player.factories.append(f1)
player.factories.append(f2)
print(player)
player.damageProces()
print(player)
print(player.isFieldAlive())
player.damageProces()
player.damageProces()
player.damageProces()
print(player)
print(player.isFieldAlive())
# 
"""
# game
"""
player1 = Player("1",0)
player2 = Player("2",7)
player3 = Player("3",14)

players = [player1,player2,player3]

fac1 = Factory("Fabrika1",False,3,5,3,100)
fac2 = Factory("Fabrika2",False,5,3,3,100)
fac3 = Factory("Fabrika3",False,3,3,5,100)
fac4 = Factory("Fabrika4",True,0,0,1,150)
fac5 = Factory("Fabrika5",True,0,1,0,150)
fac6 = Factory("Fabrika6",True,1,0,0,150)
shop = [fac1,fac2,fac3,fac4,fac5,fac6]

q1 = Question("Treba li zagadjivati vazduh","A",20,["Da","Ne"],'1')
q2 = Question("Treba li bacati smece u sumi","F",20,["Da","Ne"],'1')
f1 = Fact("Treba voditi zdrav zivot")
d1 = Destroy("SPalio si sumu","F",30)
g1 = Good("Investiraju u tebe","money",200)

deck = Deck([q1,q2],[f1],[d1],[g1])

game = Game(map,players,shop,deck)
game.run()
"""
# game



#chrome preuzimanje podesavanja Francuska




