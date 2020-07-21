import pygame
import random

pygame.init()

suit = ['H', 'D', 'C', 'S']
val = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

display_width = 1000
display_height = 650

pokerTable = pygame.image.load('images/table.png')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pygame Poker')
clock = pygame.time.Clock()

tableCard = pygame.image.load('images/ontablecard.png')
pos = (500,300)


class Table():
	def __init__(self):
		self.gamblers = []
		self.seats = 6
		self.dealerChipPos = 0
		self.pot = 0
		# self.roundBet should always start as big blind, 25 is a placeholder
		self.roundBet = 100

	

	def removePlayer(self, playerObject):
		for playerObject.name in self.gamblers:
			if playerObject.bust == True:
				self.gamblers.remove(playerObject)

	def randomDealerChip(self):
		self.dealerChipPos = random.randint(0, (len(self.gamblers)-1))



	
	

class Player():
	def __init__(self, name):
		self.hand = []
		self.chips = 0
		self.bet = 0
		self.turnOver = False
		self.folded = False
		self.bust = False
		self.name = name
		self.cardCoordT = ()
		self.bb = False
		self.sb = False
		self.dChip = False
		

		
	def namePlayer(self,name):
		self.name = name
		
	def drawCard(self, deck):
		self.hand.append(deck.drawCard())
		return self.hand

	def showHand(self):
		for c in self.hand:
			c.show()

	def blitHand(self,x1,y1,x2,y2):
		gameDisplay.blit(self.hand[0].cardImg, (x1,y1))
		gameDisplay.blit(self.hand[1].cardImg, (x2,y2))
		

	def checkBet(self):
		if self.turn == True:
			self.turn = False

	def raiseBet(self,x):
		if self.turn == True:
			if self.chips > x:
				self.bet = x
				self.chips = self.chips - x
				self.turn = False

	def foldBet(self):
		if self.turn == True:
			self.folded = True
			self.turn = False

	def blitTableCard(self):
		if self.folded == False and self.bust == False:
			gameDisplay.blit(tableCard, self.cardCoordT)

	def getTableCoord(self, table):
		posTableCard = table.gamblers.index(self.name)
		if posTableCard == 0:
			self.cardCoordT = (263,175)
		elif posTableCard == 1:
			self.cardCoordT = (700,175)
		elif posTableCard == 2:
			self.cardCoordT = (480,160)
		elif posTableCard == 3:
			self.cardCoordT = (263,345)
		elif posTableCard == 4:
			self.cardCoordT = (700,345)
		else:
			self.cardCoordT = (480,355)

	def addChips(self, game):
		self.chips = game.startChips


		






class Card():
	def __init__(self, suit, val):
		self.suit = suit
		self.val = val
		self.cardImg = pygame.image.load('images/'+val+suit+'.png')

	def show(self):
		print(self.val, 'of', self.suit)



class Deck():
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for i in suit:
			for j in val:
				self.cards.append(Card(i,j))

	def show(self):
		for c in self.cards:
			c.show()

	def shuffle(self):
		random.shuffle(self.cards)

	def drawCard(self):
		return self.cards.pop()



class Game():
	def __init__(self, startChips, bigBlind):
		self.startChips = startChips
		self.bigBlind = bigBlind
		self.smallBlind = bigBlind//2
		self.pot = 0
		self.sideP1 = 0
		self.sideP2 = 0
		self.sideP3 = 0
		self.sideP4 = 0

	

