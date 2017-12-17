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
horizon = 270
background=image.load("back07.jpg")
background=transform.scale(background,(res[0]+50,res[1]-top))

init()
window=display.set_mode(res)
clock = time.Clock()
Font=font.SysFont("arial",26)


class Ball(object):
	def __init__(self):
		self.x=-100
		self.y=-100
		self.orient="stop"
		self.v=5
		self.rect=Rect(self.x,self.y,50,50)
		self.pic=image.load("ball.png")
		self.pic2=image.load("ball2.png")
		self.seq=0
		
	def draw(self):
		#draw.rect(window,white,self.rect,1)
		
		if self.orient=="stop":
			window.blit(self.pic,(self.x-30,self.y-30),(110*self.seq,100,100,95))
			
		if self.orient=="right":
			window.blit(self.pic,(self.x-50,self.y-30),(110*self.seq,0,105,95))
			self.x=self.x+self.v
			self.rect=Rect(self.x,self.y,50,50)

		if self.orient=="left":
			window.blit(self.pic2,(self.x-5,self.y-30),(110*self.seq+225,0,105,95))
			self.x=self.x-self.v
			self.rect=Rect(self.x,self.y,50,50)

		self.seq=(self.seq+1)%2

class Player(object):
	
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.size=(50,100)
		self.rect=Rect(self.x-0.5*self.size[0],self.y+20,self.size[0],self.size[1]-50)
		self.hp=100
		self.mp=100
		self.orient="right"
		self.mode = "stand"
		self.seq=0
		self.pic=image.load("jason.png")
		self.pic2=image.load("jason2.png")
		self.pic3=image.load("jason3.png")
		self.pic4=image.load("jason4.png")
		
	def left(self):
		self.orient="left"
		self.mode="go"
		if self.x>0:
			self.x=self.x-5
			self.rect=Rect(self.x-0.5*self.size[0],self.y+20,self.size[0],self.size[1]-50)
			
	def right(self):
		self.orient="right"
		self.mode="go"
		if self.x<res[0]:
			self.x=self.x+5
			self.rect=Rect(self.x-0.5*self.size[0],self.y+20,self.size[0],self.size[1]-50)
			
	def up(self):
		self.mode="go"
		if self.y>horizon-self.size[1]:
			self.y=self.y-3
			self.rect=Rect(self.x-0.5*self.size[0],self.y+20,self.size[0],self.size[1]-50)
			
	def down(self):
		self.mode="go"
		if self.y<res[1]-100:
			self.y=self.y+3
			self.rect=Rect(self.x-0.5*self.size[0],self.y+20,self.size[0],self.size[1]-50)
			
			
	def attack1(self,p):
		self.mode="attack1"
		if self.rect.colliderect(p.rect) and p.hp>0:
			p.hp=p.hp-1
			
	def attack2(self,p):
		self.mode="attack2"
		if self.rect.colliderect(p.rect) and p.hp>0 and self.mp>5:
			p.hp=p.hp-3
		if self.mp>5:
			self.mp=self.mp-5
		else:
			self.mode="stand"
			
	def attack3(self,b):
		self.mode="attack3"
		if self.orient=="left":
			b.orient="left"
			b.x=self.x-80
		else:
			b.orient="right"
			b.x=self.x+40
		b.y=self.y+40
		
		'''
		if self.rect.colliderect(p.rect) and p.hp>0 and self.mp>5:
			p.hp=p.hp-3
		if self.mp>5:
			self.mp=self.mp-5
		'''

			
	def draw(self):
		#draw.rect(window,white,self.rect,1)
		#draw.rect(window,white,Rect(self.x+0,self.y+self.size[1],50,100),1)
		
		if self.mode=="stand":
			if self.orient=="right":
				window.blit(self.pic,(self.x-40,self.y+10),(80*self.seq,0,80,100))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(80*self.seq+480,0,80,100))
		if self.mode=="go":
			if self.orient=="right":
				window.blit(self.pic,(self.x-40,self.y+10),(80*self.seq+240,0,80,100))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(80*self.seq+160,0,80,100))
		if self.mode=="attack1":
			if self.orient=="right":
				window.blit(self.pic,(self.x-40,self.y+10),(80*self.seq+240,100,80,100))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(80*self.seq+160,100,80,100))		
		if self.mode=="attack2":
			if self.orient=="right":
				window.blit(self.pic,(self.x-40,self.y+10),(80*self.seq,200,75,100))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(80*self.seq+480,200,75,100))	
		if self.mode=="attack3":
			if self.orient=="right":
				window.blit(self.pic3,(self.x-40,self.y),(80*self.seq+400,100,75,100))
			else:
				window.blit(self.pic4,(self.x-40,self.y),(80*self.seq+80,100,75,100))
		self.seq=(self.seq+1)%4
		self.mode="stand"
		if self.mp<100 and self.seq==0:
			self.mp=self.mp+1
	
class Game(object):
	
	def __init__(self):
		pass
	
	def draw(self):
		draw.rect(window,(0,0,0),Rect(0,0,res[0],res[1]),0)
		#draw.rect(window,bluesky,Rect(0,top,res[0],res[1]),0)
		#draw.rect(window,greengrass,Rect(0,horizon,res[0],res[1]),0)
		window.blit(background,(-25,top))
		
		if p1.y>p2.y:
			p2.draw()
			p1.draw()
		else:
			p1.draw()
			p2.draw()
		
		b1.draw()
		b2.draw()
		
		draw.rect(window,bloodred,Rect(100,25,2*100,20))
		draw.rect(window,red,Rect(100,25,2*p2.hp,20))
		
		draw.rect(window,bloodred,Rect(500,25,2*100,20))
		draw.rect(window,red,Rect(500,25,2*p1.hp,20))
		
		draw.rect(window,darkblue,Rect(100,55,2*100,20))
		draw.rect(window,blue,Rect(100,55,2*p2.mp,20))
		
		draw.rect(window,darkblue,Rect(500,55,2*100,20))
		draw.rect(window,blue,Rect(500,55,2*p1.mp,20))
		
		if p1.hp<=0:
			text = Font.render("Player 2 wins",True,(255,255,255))
			window.blit(text,(res[0]/2-60,res[1]/2))
		if p2.hp<=0:
			text = Font.render("Player 1 wins",True,(255,255,255))
			window.blit(text,(res[0]/2-60,res[1]/2))


p2 = Player(200,100+horizon)
p1 = Player(600,100+horizon)
b1 = Ball()
b2 = Ball()
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
	if keys[K_KP1]:
		p1.attack1(p2)
	if keys[K_KP2]:
		p1.attack2(p2)
	if keys[K_KP3]:
		p1.attack3(b1)
	if keys[K_a]:
		p2.left()
	if keys[K_d]:
		p2.right()
	if keys[K_w]:
		p2.up()
	if keys[K_s]:
		p2.down()
	if keys[K_1]:
		p2.attack1(p1)
	if keys[K_2]:
		p2.attack2(p1)
	if keys[K_5]:
		p2.attack3(b2)
	#p1.hp=p1.hp-1	
	game.draw()
	
	clock.tick(20)
	display.flip()