import random
import pygame
from pokerClass import Table
from pokerClass import Player
from pokerClass import Card 
from pokerClass import Deck 
from pokerClass import Game

pygame.init()

display_width = 1000
display_height = 650

pokerTable = pygame.image.load('images/table.png')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pygame Poker')
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
green = (51,153,51)
blue = (51,102,153)

playerBoxImg = pygame.image.load('images/playerBox.png')

playerNum = 6

betBar = pygame.image.load('images/control.png')

tableCard = pygame.image.load('images/ontablecard.png')

dChip = pygame.image.load('images/dealerChip.png')

# A list to represent the preflop, post-flop, post-turn, and post-river rounds of betting
betRounds = [1,2,3,4]







# displays the control bar on the game surface
def controlBar():
	gameDisplay.blit(betBar, (0,510))

# displays the player boxes on the game surface
def playerBox():
	
	if playerNum == 6:
		gameDisplay.blit(playerBoxImg, (100,100))
		gameDisplay.blit(playerBoxImg, (730,100))
		gameDisplay.blit(playerBoxImg, (420,70))
		gameDisplay.blit(playerBoxImg, (100,390))
		gameDisplay.blit(playerBoxImg, (730,390))
		gameDisplay.blit(playerBoxImg, (420,410))
	elif playerNum == 5:
		gameDisplay.blit(playerBoxImg, (100,100))
		gameDisplay.blit(playerBoxImg, (730,100))
		gameDisplay.blit(playerBoxImg, (100,390))
		gameDisplay.blit(playerBoxImg, (730,390))
		gameDisplay.blit(playerBoxImg, (420,410))
	elif playerNum == 4:
		gameDisplay.blit(playerBoxImg, (100,100))
		gameDisplay.blit(playerBoxImg, (730,100))
		gameDisplay.blit(playerBoxImg, (100,390))
		gameDisplay.blit(playerBoxImg, (730,390))
	elif playerNum == 3:
		gameDisplay.blit(playerBoxImg, (100,100))
		gameDisplay.blit(playerBoxImg, (730,100))
		gameDisplay.blit(playerBoxImg, (420,410))
	elif playerNum == 2:
		gameDisplay.blit(playerBoxImg, (420,70))
		gameDisplay.blit(playerBoxImg, (420,410))


def blitCardLoop():
	for p in objectList:
		if p.bust == False and p.folded == False:
			gameDisplay.blit(tableCard, (p.cardCoordT))



def dealer(table):

	if table.dealerChipPos == 0:
		gameDisplay.blit(dChip, (455,370))
	elif table.dealerChipPos == 1:
		gameDisplay.blit(dChip, (240,335))
	elif table.dealerChipPos == 2:
		gameDisplay.blit(dChip, (308,160))
	elif table.dealerChipPos == 3:
		gameDisplay.blit(dChip, (525,160))
	elif table.dealerChipPos == 4:
		gameDisplay.blit(dChip,(745,200))
	else:
		gameDisplay.blit(dChip,(675,370))




				
# forms part of betting function before the flop has been drawn				
def preFlopBetLoop(table):
	global pPreflopList
	for player in pPreflopList:
		if player.bust == False and player.folded == False and player.bet != table.roundBet:
			decision = input('Check, fold, call or raise: ')
			if decision == 'fold':
				player.folded = True
			elif decision == 'check':
				pass
			elif decision == 'call':
				if player.chips > table.roundBet:
					player.bet = table.roundBet
			elif decision == 'raise':
				y = input('raise by how much?: ')
				player.bet = player.bet + y
				pPreflopList = pPreflopList[pPreflopList.index(player)+1:]+ pPreflopList[:pPreflopList.index(player)]
				preFlopBetLoop(table)

# forms the betting functionality for after the flop has been drawn
def postFlopBetLoop(table):
	global pPostflopList
	for player in pPostflopList:
		if player.bust == False and player.folded == False and player.bet != table.roundBet:
			x = input('Check, fold, call or raise: ')
			if x == 'fold':
				player.folded = True
			elif x == 'check':
				pass
			elif x == 'call':
				if player.chips > table.roundBet:
					player.bet = table.roundBet
			elif x == 'raise':
				y = input('raise by how much?: ')
				player.bet = player.bet + y
				pPostflopList = pPostflopList[pPostflopList.index(player)+1:]+ pPostflopList[:pPostflopList.index(player)]
				postFlopBetLoop(table)
	


def betRoundLoop(table):
	for round in betRounds:
		if round == 1:
			preFlopBetLoop(table)
		else:
			postFlopBetLoop(table)




def gameIntro():

	gameStarted = False

	while not gameStarted:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


		gameDisplay.fill(green)
		font = pygame.font.SysFont('comicsans', 100)
		text = font.render('Pygame Poker', 1, black)
		gameDisplay.blit(text, (240,80))
		pygame.display.update()
		clock.tick(60)


def gameLoop():

	gameLoopFinished = False


	while not gameLoopFinished:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		



		gameDisplay.fill(blue)
		gameDisplay.blit(pokerTable, (180,119))
		playerBox()
		blitCardLoop()
		gameDisplay.blit(flop1.cardImg, (310,200))
		gameDisplay.blit(flop2.cardImg, (385,200))
		gameDisplay.blit(flop3.cardImg, (460,200))
		gameDisplay.blit(turn.cardImg, (535,200))
		gameDisplay.blit(river.cardImg, (610,200))
		p1.blitHand(390,400,410,400)
		p2.blitHand(70,390,90,390)
		p3.blitHand(70,60,90,60)
		p4.blitHand(390,40,410,40)
		p5.blitHand(700,60,720,60)
		p6.blitHand(700,390,720,390)
		gameDisplay.blit(p1name, (500,415))
		gameDisplay.blit(p1chips,(500,440))
		gameDisplay.blit(p2name, (180,395))
		gameDisplay.blit(p2chips,(180,420))
		gameDisplay.blit(p3name, (180,105))
		gameDisplay.blit(p3chips,(180,130))
		gameDisplay.blit(p4name, (500,75))
		gameDisplay.blit(p4chips,(500,100))
		gameDisplay.blit(p5name, (810,105))
		gameDisplay.blit(p5chips,(810,130))
		gameDisplay.blit(p6name, (810,395))
		gameDisplay.blit(p6chips,(810,420))
		dealer(table1)
		#betRoundLoop(table1)
		controlBar()
		
		
		
		pygame.display.update()
		clock.tick(60)



#Game intro assignments are below

#creates game object
game1 = Game(1500,25)

# creates a table object
table1 = Table()

#creates a deck
deck1 = Deck()
deck1.shuffle()

# assigns names to player objects
p1 = Player('mat')
p2 = Player('cal')
p3 = Player('kim')
p4 = Player('jim')
p5 = Player('sar')
p6 = Player('pat')





# adds player name to a a list of gamblers in table object
table1.gamblers.append(p1.name)
table1.gamblers.append(p2.name)
table1.gamblers.append(p3.name)
table1.gamblers.append(p4.name)
table1.gamblers.append(p5.name)
table1.gamblers.append(p6.name)




# create random position for dealer chip
table1.randomDealerChip()
print(table1.dealerChipPos)

objectList = [p1,p2,p3,p4,p5,p6]

# this creates an object list that is ordered by first turn
new1 = objectList[table1.dealerChipPos:]
new2 = objectList[:table1.dealerChipPos]
objectTurnList = new1+new2

obPreflopTurn  = objectTurnList[3:]+objectTurnList[:3]

pPreflopList  = objectTurnList[3:]+objectTurnList[:3]
pPostflopList = objectTurnList[1:]+objectTurnList[:1]

print(table1.gamblers)

# gets the coordinates for blitting each of the players hands down cards on the table
p1.getTableCoord(table1)
p2.getTableCoord(table1)
p3.getTableCoord(table1)
p4.getTableCoord(table1)
p5.getTableCoord(table1)
p6.getTableCoord(table1)


p1.drawCard(deck1)
p2.drawCard(deck1)
p3.drawCard(deck1)
p4.drawCard(deck1)
p5.drawCard(deck1)
p6.drawCard(deck1)
p1.drawCard(deck1)
p2.drawCard(deck1)
p3.drawCard(deck1)
p4.drawCard(deck1)
p5.drawCard(deck1)
p6.drawCard(deck1)

font = pygame.font.SysFont('arial', 20)

p1name = font.render(p1.name, 1, black)
p1chips = font.render(str(p1.chips),1,black)
p2name = font.render(p2.name, 1, black)
p2chips = font.render(str(p2.chips),1,black)
p3name = font.render(p3.name, 1, black)
p3chips = font.render(str(p3.chips),1,black)
p4name = font.render(p4.name, 1, black)
p4chips = font.render(str(p4.chips),1,black)
p5name = font.render(p5.name, 1, black)
p5chips = font.render(str(p5.chips),1,black)
p6name = font.render(p6.name, 1, black)
p6chips = font.render(str(p6.chips),1,black)



flop1 = deck1.drawCard()
flop2 = deck1.drawCard()
flop3 = deck1.drawCard()
turn = deck1.drawCard()
river = deck1.drawCard()	


#preFlopBetLoop(table1) 
	

gameLoop()
