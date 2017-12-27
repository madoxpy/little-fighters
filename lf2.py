from pygame import *
import numpy as np
from random import randint,random,choice

green=(0,255,0)
greengrass=(1,166,17)
black=(0,0,0)
white=(255,255,255)
bluesky=(135,206,235)
red=(255,5,5)
bloodred=(138,7,7)
blue=(0,0,255)
darkblue=(0,0,139)

res = (800,500)
top = 100
horizon = 250

init()
window=display.set_mode(res)
clock = time.Clock()
Font=font.SysFont("arial",26)
back = image.load("back07.jpg")
back=transform.scale(back,(res[0]+50,res[1]-100))

class Player(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.size=(50,100)
		self.rect=Rect(self.x-0.5*self.size[0],self.y,self.size[0],self.size[1])
		self.hp=90
		self.mp=90
		self.orient = "right"
		self.pic = self.photo =image.load("jason.png")
		self.pic2 = self.phot = image.load("jason2.png")		
		self.seq = 0
		self.mode = "stand"
	def left(self):
		self.mode = "go"
		self.orient = "left"
		if self.x>0:
			self.x=self.x-3
			self.rect=Rect(self.x-0.5*self.size[0],self.y,self.size[0],self.size[1])
	def right(self):
		self.mode = "go"
		self.orient = "right"
		if self.x<res[0]:
			self.x=self.x+3
			self.rect=Rect(self.x-0.5*self.size[0],self.y,self.size[0],self.size[1])
	def up(self):
		if self.y>horizon-self.size[1]:
			self.y=self.y-2
			self.rect=Rect(self.x-0.5*self.size[0],self.y,self.size[0],self.size[1])
	def down(self):
		if self.y<res[1]:
			self.y=self.y+2
			self.rect=Rect(self.x-0.5*self.size[0],self.y,self.size[0],self.size[1])
	def draw(self):
		#draw.rect(window,white,self.rect,1)

		if self.mode == "stand":
			if self.orient == "right":
				window.blit(self.pic,(self.x-40,self.y+10),(80*self.seq,0,80,100))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(80*self.seq+400,0,80,100))
		if self.mode == "go":
			self.mode = "stand"
			if self.orient == "right":
				window.blit(self.pic,(self.x-40,self.y+10),(80*self.seq+240,0,80,100))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(80*self.seq+160,0,80,100))
		if self.seq == 4:
			self.seq = 0
		else:
			self.seq = self.seq + 1

	
class Game(object):
	def __init__(self):
		pass
	def draw(self):
		draw.rect(window,(0,0,0),Rect(0,0,res[0],res[1]),0)
		draw.rect(window,bluesky,Rect(0,top,res[0],res[1]),0)
		draw.rect(window,greengrass,Rect(0,horizon,res[0],res[1]),0)
		window.blit(back,(-25,top))
		if p1.y>p2.y:
			p2.draw()
			p1.draw()
		else:
			p1.draw()
			p2.draw()
		draw.rect(window,bloodred,Rect(100,25,2*100,20))
		draw.rect(window,red,Rect(100,25,2*p1.hp,20))
		
		draw.rect(window,bloodred,Rect(500,25,2*100,20))
		draw.rect(window,red,Rect(500,25,2*p2.hp,20))
		
		draw.rect(window,darkblue,Rect(100,55,2*100,20))
		draw.rect(window,blue,Rect(100,55,2*p1.mp,20))
		
		draw.rect(window,darkblue,Rect(500,55,2*100,20))
		draw.rect(window,blue,Rect(500,55,2*p2.mp,20))
		
		if p1.hp<=0:
			text = Font.render("Player 2 wins",True,(255,255,255))
			window.blit(text,(res[0]/2-60,res[1]/2))
		if p2.hp<=0:
			text = Font.render("Player 1 wins",True,(255,255,255))
			window.blit(text,(res[0]/2-60,res[1]/2))


p2 = Player(200,100+horizon)
p1 = Player(600,100+horizon)
game = Game()
	
end = False 
while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True
			
	keys = key.get_pressed()
	if keys[K_LEFT]:
		p1.left()
	if keys[K_RIGHT]:
		p1.right()
	if keys[K_UP]:
		p1.up()
	if keys[K_DOWN]:
		p1.down()
	if keys[K_a]:
		p2.left()
	if keys[K_d]:
		p2.right()
	if keys[K_w]:
		p2.up()
	if keys[K_s]:
		p2.down()
	#p1.hp=p1.hp-1	
	game.draw()
	
	clock.tick(20)
	display.flip()
