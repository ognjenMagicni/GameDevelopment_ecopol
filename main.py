import pygame
from proba1 import Player
import proba1
import random
import asyncio
import os
pygame.init()

#Screenpython
WIDTH = 1200
HEIGHT = 800
WIN = pygame.display.set_mode( (WIDTH,HEIGHT) )
WIN.fill( (230,230,230) )
pygame.display.set_caption("Ecopol")

#music sound
pygame.mixer.init()
dice1 = pygame.mixer.Sound( os.path.join("assets","dice1.ogg") )
dice2 = pygame.mixer.Sound( os.path.join("assets","dice2.ogg") )
diceS = [dice1,dice2]
jump1 = pygame.mixer.Sound( os.path.join("assets","jump1.ogg") )
jump2 = pygame.mixer.Sound( os.path.join("assets","jump2.ogg") )
jump3 = pygame.mixer.Sound( os.path.join("assets","jump3.ogg") )
jumpS = [jump1,jump2,jump3]
clickS = pygame.mixer.Sound( os.path.join("assets","buttonClick2.ogg") )


#Refresh rate
clock = pygame.time.Clock()
FPS = 60

#font
pygame.font.init()
textFont60 = pygame.font.SysFont("arial",60)

#pictures
shopImage1 = pygame.image.load( os.path.join("assets","factory.png") )
shopImage2 = pygame.image.load( os.path.join("assets","industry1.png"))
shopImage3 = pygame.image.load( os.path.join("assets","industry2.png"))
shopImage4 = pygame.image.load( os.path.join("assets","greenF1.png"))
shopImage5 = pygame.image.load( os.path.join("assets","greenF2.png"))
shopImage6 = pygame.image.load( os.path.join("assets","greenF3.png"))
squirrelLogo = pygame.image.load(os.path.join("assets","logo.png"))
tutorial01 = pygame.image.load(os.path.join("assets","tutorial01.png"))
tutorial02 = pygame.image.load(os.path.join("assets","tutorial02.png"))
tutorial03 = pygame.image.load(os.path.join("assets","tutorial03.png"))
tutorial13 = pygame.image.load(os.path.join("assets","tutorial13.png"))
tutorial04 = pygame.image.load(os.path.join("assets","tutorial04.png"))
tutorial14 = pygame.image.load(os.path.join("assets","tutorial14.png"))
tutorial05 = pygame.image.load(os.path.join("assets","tutorial05.png"))
tutorial06 = pygame.image.load(os.path.join("assets","tutorial06.png"))
tutorial07 = pygame.image.load(os.path.join("assets","tutorial07.png"))

#proba
p1 = Player("Player1",0,0,0,30,30,(120,120,200))
p2 = Player("Player2",7,0,0,970,30,(120,200,120))
p3 = Player("Player3",14,0,0,970,470,(200,120,120))
p4 = Player("Player4",21,0,0,30,470,(200,60,200))

players = [p1,p2,p3,p4]
numOfPlayers = len(players)

#shop
fac1 = proba1.Factory("Fabrika1",False,3,5,3,100,50,shopImage1)
fac2 = proba1.Factory("Fabrika2",False,5,3,3,100,50,shopImage2)
fac3 = proba1.Factory("Fabrika3",False,3,3,5,100,50,shopImage3)
fac4 = proba1.Factory("Fabrika4",True,0,0,1,150,50,shopImage4)
fac5 = proba1.Factory("Fabrika5",True,0,1,0,150,50,shopImage5)
fac6 = proba1.Factory("Fabrika6",True,1,0,0,150,50,shopImage6)
shopList = [fac1,fac2,fac3,fac4,fac5,fac6]

shop = proba1.Shop(shopList,WIDTH,HEIGHT)

#question cards
questions = [      ["What does \"circular economy\" mean?", 'A', 400, ['A circle of money', 'Reusing resources and making less waste', 'A round table discussion about economy', 'An economy where everything costs the same'], '2'],
        ["What does \"upcycling\" mean?", 'A', 400, ['Throwing away used items', 'Reusing/recycling materials to make higher value products', 'Buying new things to replace old ones', 'Cleaning up the environment'], '2'],
        ["What is \"eco-entrepreneurship\"?", 'F', 400, ['Starting a business that helps the environment', 'Making a lot of money quickly', 'Selling only eco-friendly products', 'Starting a business that uses a lot of resources'], '1'],
        ["What's a \"green business\" idea?", 'F', 400, ['Making clothes quickly and cheaply', "Making soaps that break down and don't harm the environment", 'A business that makes plastic toys', 'Selling fast food'], '2'],
        ["How does less waste help our planet?", 'R', 400, ['It makes the world look cleaner', 'It can slow down climate change', 'It makes things smell better', "It doesn't help"], '2'],
        ["Why should a business try to be \"carbon-neutral\"?", 'R', 400, ['To save money on carbon', 'To help slow down global warming', 'To have a neutral color scheme', 'To make their products weigh less'], '2'],
        ["What's a renewable source of energy?", 'B', 400, ['Coal', 'Gasoline', 'Sunlight', 'Plastic'], '3']  , ["What does \"circular economy\" mean?", "A", 400, ["A circle of money", "Reusing resources and making less waste", "A round table discussion about economy", "An economy where everything costs the same"], "2"], ["What does \"upcycling\" mean?", "A", 400, ["Throwing away used items", "Reusing/recycling materials to make higher value products", "Buying new things to replace old ones", "Cleaning up the environment"], "2"], ["What is \"eco-entrepreneurship\"?", "F", 400, ["Starting a business that helps the environment", "Making a lot of money quickly", "Selling only eco-friendly products", "Starting a business that uses a lot of resources"], "1"], ["Circular Economy Principle: What is the main idea behind the circular economy?", "A", 400, ["Use once and dispose", "Recycle a few things and discard others", "Design products for endless reuse and recycling", "Produce more goods for growth"], "3"], ["Green Energy Source: Which of the following is NOT a renewable energy source?", "B", 400, ["Wind", "Solar", "Natural gas", "Geothermal"], "3"], ["Ecological Economics: What distinguishes ecological economics from traditional economics?", "A", 400, ["It focuses solely on maximizing profits.", "It emphasizes GDP as the only measure of progress.", "It integrates ecological principles and system constraints.", "It disregards environmental factors entirely."], "3"], ["Zero-Waste Philosophy: What does the zero-waste movement primarily promote?", "A", 400, ["Buying as much as possible.", "Only recycling plastics.", "Designing and managing products and processes to systematically avoid waste.", "Minimizing only hazardous waste."], "3"], ["Bio-Based Materials: Which of the following is NOT a bio-based material?", "B", 400, ["Polyethylene", "Mycelium leather", "Polylactic acid (PLA)", "Algal bioplastics"], "1"], ["Regenerative Design: What is the main goal of regenerative design in eco-entrepreneurship?", "F", 400, ["To restore and renew systems beyond sustainability.", "To achieve short-term economic growth.", "To maintain systems in their current state.", "To utilize as many natural resources as possible."], "1"], ["Ecosystem Services: Which of the following is NOT a type of ecosystem service?", "R", 400, ["Provisioning services (like food and water)", "Exploitation services", "Regulating services (like climate regulation)", "Cultural services (like aesthetic value)"], "2"], ["Life Cycle Assessment (LCA): What does LCA primarily evaluate?", "A", 400, ["The market value of a product.", "The environmental impacts throughout a product's entire life cycle.", "The cultural significance of a product.", "The number of consumers for a product."], "2"], ["Biomimicry: What principle does biomimicry emphasize in sustainable design?", "F", 400, ["Imitating popular culture trends.", "Copying existing technologies.", "Emulating nature's time-tested patterns and strategies.", "Modeling after high-energy processes."], "3"], ["Carbon Neutrality: What does it mean for a company to be carbon neutral?", "R", 400, ["It uses carbon-based fuels exclusively.", "It offsets its carbon emissions by investing in renewable energy or carbon sequestration.", "It has zero carbon emissions from its operations.", "It has no responsibility for carbon emissions."], "2"], ["Green Procurement: Why do companies adopt green procurement policies?", "F", 400, ["To solely reduce their operating costs.", "To purchase products and services that cause minimal environmental impacts.", "To buy products based solely on their market popularity.", "To promote non-sustainable goods."], "2"], ["Natural Resource Depletion: Which activity is a primary driver for the rapid depletion of natural resources?", "B", 400, ["Conservation efforts", "Overconsumption and inefficient resource use", "Preservation of habitats", "Promotion of renewable energy"], "2"], ["Ecological Economics: What distinguishes ecological economics from traditional economics?", "A", 400, ["It focuses solely on maximizing profits.", "It emphasizes GDP as the only measure of progress.", "It integrates ecological principles and system constraints.", "It disregards environmental factors entirely."], "3"], ["Zero-Waste Philosophy: What does the zero-waste movement primarily promote?", "A", 400, ["Buying as much as possible.", "Only recycling plastics.", "Designing and managing products and processes to systematically avoid waste.", "Minimizing only hazardous waste."], "3"], ["Bio-Based Materials: Which of the following is NOT a bio-based material?", "B", 400, ["Polyethylene", "Mycelium leather", "Polylactic acid (PLA)", "Algal bioplastics"], "1"], ["Regenerative Design: What is the main goal of regenerative design in eco-entrepreneurship?", "F", 400, ["To restore and renew systems beyond sustainability.", "To achieve short-term economic growth.", "To maintain systems in their current state.", "To utilize as many natural resources as possible."], "1"], ["Ecosystem Services: Which of the following is NOT a type of ecosystem service?", "R", 400, ["Provisioning services (like food and water)", "Exploitation services", "Regulating services (like climate regulation)", "Cultural services (like aesthetic value)"], "2"], ["Life Cycle Assessment (LCA): What does LCA primarily evaluate?", "A", 400, ["The market value of a product.", "The environmental impacts throughout a product's entire life cycle.", "The cultural significance of a product.", "The number of consumers for a product."], "2"], ["Biomimicry: What principle does biomimicry emphasize in sustainable design?", "F", 400, ["Imitating popular culture trends.", "Copying existing technologies.", "Emulating nature's time-tested patterns and strategies.", "Modeling after high-energy processes."], "3"], ["Carbon Neutrality: What does it mean for a company to be carbon neutral?", "R", 400, ["It uses carbon-based fuels exclusively.", "It offsets its carbon emissions by investing in renewable energy or carbon sequestration.", "It has zero carbon emissions from its operations.", "It has no responsibility for carbon emissions."], "2"], ["Green Procurement: Why do companies adopt green procurement policies?", "F", 400, ["To solely reduce their operating costs.", "To purchase products and services that cause minimal environmental impacts.", "To buy products based solely on their market popularity.", "To promote non-sustainable goods."], "2"], ["Natural Resource Depletion: Which activity is a primary driver for the rapid depletion of natural resources?", "B", 400, ["Conservation efforts", "Overconsumption and inefficient resource use", "Preservation of habitats", "Promotion of renewable energy"], "2"]]

quesDeck = []
for i in questions:
    i[1] = 'B'
    q = proba1.Question(i[0],i[1],i[2],i[3],i[4])
    q.setAnswerCord()
    quesDeck.append(q)

invests = [
["Green Grant: Your sustainable business model has attracted a government grant. Receive 52 for research and development.", "F", 52],
["Eco Award: Your enterprise has won an award for outstanding contributions to environmental preservation. Gain publicity and receive 87 as a prize.", "A", 87],
["Corporate Partnership: A major corporation is impressed with your waste reduction methods and wants to implement them. They pay you 52 for consultation and collaboration.", "F", 52],
["Crowdfunding Success: Your eco-project pitch went viral! Ecologically conscious individuals from around the world chip in. Collect 133 from supportive backers.", "R", 133],
["Eco-Tourism Tie-Up: A travel company wants to feature your eco-friendly establishment in their green travel itinerary. Receive 57 for a year-long collaboration.", "A", 57]
]

invDeck = []
for i in invests:
    ness = proba1.Good(i[0],i[1],i[2])
    invDeck.append(ness)

destroys = [
["Pollution Problems: An oil spill near your sustainable fishing business has affected the marine life. Pay 89 for cleanup and restoration efforts.", "A", -89],
["Equipment Failure: Your solar panels have malfunctioned due to a manufacturer defect. Pay 95 for replacements.", "R", -95],
["Natural Disaster: Heavy rain and flooding have damaged your organic farm. Pay 133 to restore and re-plant.", "A", -133],
["Supply Chain Issues: A major supplier of eco-friendly materials has gone bankrupt. Pay 105 to find and switch to a new supplier.", "B", -105],
["Pest Infestation: Harmful pests have infested your sustainable woodlot. Pay 90 for eco-friendly pest control solutions.", "B", -90]
]
destroyDeck = []
for i in destroys:
    d = proba1.Destroy(i[0],i[1],i[2])
    destroyDeck.append(d)

facts = ["Buzzing Business! Did you know some eco-entrepreneurs start beekeeping businesses? Bees help plants grow and their honey is sweet money!",
 "Eco-Fashionista: Some eco-businesses create clothing from recycled bottles and even old fishing nets!",
 "Sneaky Sneakers: There are eco-friendly shoes made from sustainable materials like wool and can even be planted to grow flowers when worn out.",
 "Edible Cutlery: Yep, you heard it! Some entrepreneurs are making spoons and forks you can eat after using them. Tasty and waste-free!",
 "Paper from Poop: An eco-business in Sri Lanka makes paper out of elephant dung! Don't worry, it doesn't smell!",
 "Solar Surge: Solar power has become cheaper than coal in many places over the last decade.",
 "Organic Upswing: Organic farming not only avoids harmful pesticides but also absorbs carbon from the air.",
 "Water Wisdom: Nearly 30% of the global population lacks safe drinking water at home.",
 "Green Jobs: Eco-businesses often result in job creation in new, environmentally-friendly sectors.",
 "Eco Architecture: Green buildings reduce emissions and can save occupants money on utility bills."]

factsDeck = []
for i in facts:
    f = proba1.Fact(i)
    factsDeck.append(f)

deck = proba1.Deck(quesDeck,factsDeck,destroyDeck,invDeck)

game = proba1.Game(map,players,shop,deck)

dice = proba1.Dice()
dice.ini(WIDTH/2-dice.cubes[0].get_width()/2,HEIGHT/2-2.5*HEIGHT/10-dice.cubes[0].get_height()/2)

show_text = False
show_time = 120  # in milliseconds
start_time = 0
backAreYouSure = False

#buttons for Yes No, when back is clicked
btnYes = proba1.button("Yes",WIDTH/2-135,HEIGHT/2+100,90,60,color = [(200,80,80),(140,70,70),(110,60,60)])
btnNo = proba1.button("No",WIDTH/2+45,HEIGHT/2+100,90,60,color = [(200,80,80),(140,70,70),(110,60,60)])
buttonExit = False

#quick fixes
colorNzm = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]

def playSound(text):
    lenD = len(diceS)
    lenJ = len(jumpS)
    if "dice" == text:
        sound = diceS[random.randrange(0,lenD)]
        sound.play()
    if "jump" == text:
        sound = jumpS[random.randrange(0,lenJ)]
        sound.play()
    if "click" == text:
        sound = clickS
        sound.play()

def backGround(window,color,cordinates,list,num=0,num1=0):
        backG = 0
        for i in list:
            backG+=i

        i = len(list) - 1
        while i>=0:
            pygame.draw.rect(window,color[i+1],(cordinates[0]-backG,cordinates[1]-backG,cordinates[2]+2*backG,cordinates[3]+2*backG),num,num1)

            backG -= list[i]
            i -= 1
        pygame.draw.rect(window,color[0],cordinates,num,num1)
btn = proba1.button("Back",250,720,90,60)

async def play(players,map):
    numberOfTurns = 21

    numOfPlayers = len(players)
    run = True
    FPS = 60
    players[0].turn = True
    def draw(roll,shopList,numberOfTurns,destinations=None,color = (0,0,0),message = "",colorMessage = [(200,80,80),(140,70,70),(110,60,60)],cardA=False,cardR = None,color1=colorNzm,winner = False,winnerList = [],buttonExit = False):
        
        
        WIN.fill((230,230,230))

        #WIN.blit(squirrelLogo,(WIDTH/2-squirrelLogo.get_width()/2,70))

        map.draw(WIN,WIDTH,HEIGHT)
        if destinations != None:
            map.colorNextLoc(WIN,destinations,color)
        
        for p in players:
            p.drawImage(WIN,shopList)
            p.draw(WIN,map.getField(p.location))
        dice.draw(WIN,WIDTH,HEIGHT,roll)
        shop.draw(WIN,WIDTH,HEIGHT,color1)
        

        if cardA==True:
            cardR.draw(WIN)

        btn.draw(WIN)
        btn1 = proba1.button("Rounds: "+str(numberOfTurns),750,720,180,60)
        btn1.draw(WIN)

        if buttonExit:
            w = 650
            h = 250
            offsetY = 60
            backGround(WIN,[(180,180,180),(140,140,140),(120,120,120)],[WIDTH/2-w/2,HEIGHT/2-h/2+offsetY,w,h],[5,5])
            btnYes.draw(WIN)
            btnNo.draw(WIN)

        if message!="": 
            textLabel = textFont60.render(message,1,(255,255,255))
            backGround(WIN,colorMessage,(WIDTH/2-textLabel.get_width()/2-20,HEIGHT/2-textLabel.get_height()*4/10,textLabel.get_width()+40,textLabel.get_height()*6/7),([5,6]),0,3)
            WIN.blit(textLabel,(WIDTH/2-textLabel.get_width()/2,HEIGHT/2-textLabel.get_height()/2))

        if winner==True:
            proba1.drawWinner(WIN,winnerList)


        pygame.display.update()
    
    async def mouseReaction(player,sixStage = False):
        roll = 0
        color1 = []
        for i in range(0,6):
            color = (random.randrange(1,256),random.randrange(1,256),random.randrange(1,256))
            color1.append(color)
        messExit = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX,mouseY = pygame.mouse.get_pos()

                    global backAreYouSure                               #napravi fju za ovu ranju, aktiviraj je i tokom poteza
                    if btn.isClicked(mouseX,mouseY):
                        playSound("click")
                        messExit = "Are you sure to exit"
                        buttonExit = True
                        draw(roll,shopList,numberOfTurns,message = messExit,buttonExit = buttonExit)
                        backAreYouSure = True
                    if backAreYouSure and btnYes.isClicked(mouseX,mouseY):
                        playSound("click")
                        backAreYouSure = False
                        await main_menu()
                    if backAreYouSure and btnNo.isClicked(mouseX,mouseY):
                        playSound("click")
                        messExit = ""
                        buttonExit = False
                        backAreYouSure = False
                        draw(roll,shopList,numberOfTurns) 

                    if shop.open and not shop.isItInRect(mouseX,mouseY):
                        playSound("click")
                        shop.open = False
                        mouseReaction(player)
                        draw(roll,shopList,numberOfTurns)
                    if shop.isItIn(mouseX,mouseY,WIDTH,HEIGHT) and not shop.open:
                        playSound("click")
                        shop.open = True
                        draw(roll,shopList,numberOfTurns,color1=color1)
                        print(shop.buyPos)
                    a = shop.isClickBuy(mouseX,mouseY,player)
                    if shop.open and a>=0:
                        playSound("click")
                        draw(roll,shopList,numberOfTurns,color1 = color1)
                        if a==100:
                            draw(roll,shopList,numberOfTurns,message="You do not have enough money",color1=color1)
                        #print(a)
                        else:
                            draw(roll,shopList,numberOfTurns,message=f"You have bought {shop.list[a].name}",colorMessage = [(180,180,180),(140,140,140),(120,120,120)],color1=color1)

                    if dice.isItIn(mouseX,mouseY) and not shop.open:
                        if sixStage:
                            roll = random.choice([1,2,3,4,5,6,6,6,6])
                        else:
                            roll = random.randrange(1,7)                                           ##
                    



                        
                        

            if roll!=0:
                break
            await asyncio.sleep(0)
       
        return roll
    def upgradeTurn(players):
        index = 0
        for i,player in enumerate(players):
            if player.turn == True:
                index = i
        players[index].turn=False
        index += 1
        index %= numOfPlayers
        print(index)
        players[index].turn = True
    async def cardGame(roll,shopList,label,player):
        exit = 0
        message1 = ""
        colorMessage = [(200,80,80),(140,70,70),(110,60,60)]
        card = deck.giveAppropriateCard(label)
        while True:
            draw(roll,shopList,numberOfTurns,cardA = True,cardR = card,message=message1,colorMessage = colorMessage)   ## ovde je ness bilo True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX,mouseY = pygame.mouse.get_pos()
                    if label == "fact":
                        exit = 1
                        break
                    if label == "question":
                        if exit==0:
                            result = card.execute1(mouseX,mouseY)
                            if result==0:
                                playSound("click")
                                message1 = "Your answer is not correct :("
                                exit = 2
                                break
                            elif result==1:
                                playSound("click")
                                message1 = "Your answer is correct"
                                player.update(card.segment,card.addPoints)
                                colorMessage =  [(80,200,80),(70,140,70),(60,110,60)]
                                #draw(roll,shopList,numberOfTurns,cardA = True,cardR = card,message=message1,colorMessage = [(80,200,80),(70,140,70),(60,110,60)])
                                exit = 2
                                break
                                
                        if exit==2:
                            exit = 1
                            break

                        break
                    if label == "gamble":
                        player.update(card.segment,card.addPoints)
                        exit = 1
                        break
                    

            if exit == 1:
                break

            await asyncio.sleep(0)
                    
    draw(1,shopList,numberOfTurns)
    roll1 = 1
    initialBank = 500
    while run:
        clock.tick(60)
        
        numberOfTurns -= 1
        if numberOfTurns <= 0:
            messages = proba1.winnerMessage(players,initialBank)
            draw(roll1,shopList,numberOfTurns,winnerList = messages, winner = True)
            roll = await mouseReaction(player)
            continue

        for player in players:
            player.damageProces(shopList)
            if not player.isFieldAlive():
                if player.varThatHelpsForLosing:
                    player.varThatHelpsForLosing = False
                    draw(roll1,shopList,numberOfTurns,message=f"{player.id} has lost a game")
                    roll = await mouseReaction(player)
                upgradeTurn(players)
                continue
            
            print(player.id)
            draw(roll1,shopList,numberOfTurns)                 #kad se ovo ubaci kvari se kockica
            if player.plays==False:
                roll = await mouseReaction(player,True)
                playSound("dice")
                roll1 = roll
                if roll!=6:
                    upgradeTurn(players)
                draw(roll,shopList,numberOfTurns)
                
                if roll == 6:   
                    player.plays = True
                    player.location = player.startingPoint
                    player.eat(players)
                else:
                    draw(roll,shopList,numberOfTurns)
                roll = 0
                
            
            while player.plays:
                roll = await mouseReaction(player)
                playSound("dice")
                roll1 = roll
                draw(roll,shopList,numberOfTurns)
                destinations = map.nextFields1(player,roll)
                draw(roll,shopList,numberOfTurns,destinations,player.color)

                while True:
                    exit = 0
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseX,mouseY = pygame.mouse.get_pos()           #

                            global backAreYouSure
                            if btn.isClicked(mouseX,mouseY):
                                playSound("click")
                                messExit = "Are you sure to exit"
                                buttonExit = True
                                draw(roll,shopList,numberOfTurns,destinations,player.color,message = messExit,buttonExit = buttonExit)
                                backAreYouSure = True
                                #await main_menu()
                            if backAreYouSure and btnYes.isClicked(mouseX,mouseY):
                                playSound("click")
                                backAreYouSure = False
                                await main_menu()
                            if backAreYouSure and btnNo.isClicked(mouseX,mouseY):
                                playSound("click")
                                messExit = ""
                                buttonExit = False
                                backAreYouSure = False
                                draw(roll,shopList,numberOfTurns,destinations,player.color)  
                            
                            for fieldN in destinations:
                                field = map.getField(fieldN)
                                if field.isItIn(mouseX,mouseY):
                                    playSound("jump")
                                    player.location = fieldN
                                    player.eat(players)
                                    exit = 1
                                    if field.label != "none":
                                        await cardGame(roll,shopList,field.label,player)
                                    if roll!=6:
                                        upgradeTurn(players)
                                    draw(roll,shopList,numberOfTurns) 
                            break
                    if exit==1:
                        break
                    await asyncio.sleep(0)
                
                if roll!=6:
                    break
        await asyncio.sleep(0)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
async def tutorial(players,map):
    run = True
    btn = proba1.button("Back",250,720,90,60)
    roll = [1]
    numberOfTurns = 20
    buttonExit = False
    messExit = ""
    backAreYouSure = False
    stage = [1]
    def draw(roll,shopList,numberOfTurns,destinations=None,color = (0,0,0),message = "",colorMessage = [(200,80,80),(140,70,70),(110,60,60)],cardA=False,cardR = None,color1=colorNzm,winner = False,winnerList = [],buttonExit = False,tutorial = None,tutorialCord = [0,0]):
        
        
        WIN.fill((230,230,230))

        #WIN.blit(squirrelLogo,(WIDTH/2-squirrelLogo.get_width()/2,70))

        map.draw(WIN,WIDTH,HEIGHT)
        if destinations != None:
            map.colorNextLoc(WIN,destinations,color)
        
        for p in players:
            p.drawImage(WIN,shopList)
            p.draw(WIN,map.getField(p.location))
        dice.draw(WIN,WIDTH,HEIGHT,roll)
        shop.draw(WIN,WIDTH,HEIGHT,color1)
        

        if cardA==True:
            cardR.draw(WIN)

        btn.draw(WIN)
        btn1 = proba1.button("Rounds: "+str(numberOfTurns),750,720,180,60)
        btn1.draw(WIN)

        if tutorial != None:
            WIN.blit(tutorial,tutorialCord)

        if buttonExit:
            w = 650
            h = 250
            offsetY = 60
            backGround(WIN,[(180,180,180),(140,140,140),(120,120,120)],[WIDTH/2-w/2,HEIGHT/2-h/2+offsetY,w,h],[5,5])
            btnYes.draw(WIN)
            btnNo.draw(WIN)

        if message!="": 
            textLabel = textFont60.render(message,1,(255,255,255))
            backGround(WIN,colorMessage,(WIDTH/2-textLabel.get_width()/2-20,HEIGHT/2-textLabel.get_height()*4/10,textLabel.get_width()+40,textLabel.get_height()*6/7),([5,6]),0,3)
            WIN.blit(textLabel,(WIDTH/2-textLabel.get_width()/2,HEIGHT/2-textLabel.get_height()/2))

        if winner==True:
            proba1.drawWinner(WIN,winnerList)

        


        pygame.display.update()

    def stageUpgrade(stage,mouseCord,roll):
        if stage[0] == 3:
            if shop.isItIn(mouseCord[0],mouseCord[1],WIDTH,HEIGHT):
                stage[0]+=1
        elif stage[0]==4:
            if not shop.isItInRect(mouseCord[0],mouseCord[1]):
                stage[0]+=1 
        elif stage[0] == 5:
            if dice.isItIn(mouseCord[0],mouseCord[1]):
                 roll[0] = 6
                 stage[0]+=1
        else:
            stage[0]+=1
    def stagePrep(stage):
        if stage[0]==1:
            return [tutorial01,[WIDTH/2-tutorial01.get_width()/2,HEIGHT/2 - tutorial01.get_height()/2]]
        if stage[0]==2:
            return [tutorial02,[250,100]]
        if stage[0]==3:
            return [tutorial03,[175,575]]
        if stage[0]==4:
            shop.open = True
            playSound("click")
            return [tutorial13,[WIDTH/2-tutorial13.get_width()/2,HEIGHT/2 - tutorial13.get_height()/2]]
        if stage[0]==5:
            shop.open = False
            playSound("click")
            return [tutorial14,[WIDTH/2-tutorial14.get_width()/2,25]]
        if stage[0]==6:
            playSound("dice")
            players[0].plays = True
            players[0].location = players[0].startingPoint
            return [tutorial05,[WIDTH/2-tutorial05.get_width()/2,250]]
        if stage[0]==7:
            return [tutorial07,[WIDTH/2-tutorial07.get_width()/2,HEIGHT/2 - tutorial07.get_height()/2]]
        else:
            return [tutorial06,[WIDTH/2-tutorial06.get_width()/2,HEIGHT/2 - tutorial06.get_height()/2]]

    stageP = stagePrep(stage)
    while run:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX,mouseY = pygame.mouse.get_pos()
                stageUpgrade(stage,[mouseX,mouseY],roll)
                stageP = stagePrep(stage)
                if btn.isClicked(mouseX,mouseY):
                    playSound("click")
                    messExit = "Are you sure to exit"
                    buttonExit = True
                    draw(roll[0],shopList,numberOfTurns,message = messExit,buttonExit = buttonExit)
                    backAreYouSure = True
                    #await main_menu()
                if backAreYouSure and btnYes.isClicked(mouseX,mouseY):
                    playSound("click")
                    backAreYouSure = False
                    await main_menu()
                if backAreYouSure and btnNo.isClicked(mouseX,mouseY):
                    playSound("click")
                    messExit = ""
                    buttonExit = False
                    backAreYouSure = False
                    draw(roll[0],shopList,numberOfTurns) 
        
        
        draw(roll[0],shopList,numberOfTurns,message=messExit,buttonExit = buttonExit,tutorial = stageP[0],tutorialCord = stageP[1])
        await asyncio.sleep(0)
        
            
 

async def main_menu():
    backAreYouSure = False
    run = True
    mMW = 250
    mMH = 250
    mainMenu = proba1.setButton(["Two Players","Three Players","Four Players","How to play"],WIDTH/2-mMW/2,400,mMW,mMH)
    p1 = Player("Player1",0,0,0,30,30,(120,120,200))
    p2 = Player("Player2",7,0,0,970,30,(120,200,120))
    p3 = Player("Player3",14,0,0,970,470,(200,120,120))
    p4 = Player("Player4",21,0,0,30,470,(200,60,200))

    players = [p1,p2,p3,p4]

    textLabel = textFont60.render("Ecopol",1,(255,255,255))

    map = proba1.Map(0)
    map.createBasic()
    map.printMap()
    print(map.outside[20].label)
    map.setField()

    def draw():
        WIN.fill((200,200,200))
        WIN.blit(squirrelLogo,(WIDTH/2-squirrelLogo.get_width()/2,-120))
        #proba1.backText(WIN,"Ecopol",60,[(140,200,140),(130,180,130),(90,90,90)],(WIDTH/2,mainMenu.y+mainMenu.height+30),[50,50])
        WIN.blit(textLabel,(WIDTH/2-textLabel.get_width()/2,mainMenu.y+mainMenu.height+30))
        mainMenu.draw(WIN)
        pygame.display.update()
    while run:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX,mouseY = pygame.mouse.get_pos()
                numOfBtn = mainMenu.whichClicked(mouseX,mouseY)
                if numOfBtn == 0:
                    playSound("click")
                    await play(players[:2],map)
                elif numOfBtn == 1:
                    playSound("click")
                    await play(players[:3],map)
                elif numOfBtn ==2:
                    playSound("click")
                    await play(players,map)
                elif numOfBtn == 3:
                    playSound("click")
                    await tutorial(players,map)
        await asyncio.sleep(0)
                
                              
asyncio.run(main_menu())
pygame.quit()

