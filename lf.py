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
	def __init__(self,name):
		self.x=-100
		self.y=-100
		self.orient="stop"
		self.v=8
		self.rect=Rect(self.x,self.y,50,50)
		self.pic=image.load(name+"ball.png")
		self.pic2=image.load(name+"ball2.png")
		self.seq=0
		
	def go(self,p):
		if self.orient=="right":
			#window.blit(self.pic,(self.x-50,self.y-30),(80*self.seq+3,0,78,80))
			self.x=self.x+self.v
			self.rect=Rect(self.x,self.y,50,50)

		if self.orient=="left":
			#window.blit(self.pic2,(self.x-5,self.y-30),(80*self.seq+3,0,78,80))
			self.x=self.x-self.v
			self.rect=Rect(self.x,self.y,50,50)		
		
		if self.rect.colliderect(p.rect):
			p.hp=p.hp-20
			if p.hp<0:
				p.hp=0
			self.x=-100
			self.y=-100
			self.orient="stop"
			self.rect=Rect(self.x,self.y,50,50)		
		
		if self.x>res[0] or self.x<-30:
			self.x=-100
			self.y=-100
			self.orient="stop"

		
		
	def draw(self):
		#draw.rect(window,white,self.rect,1)
		
		if self.orient=="stop":
			window.blit(self.pic,(self.x-30,self.y-30),(110*self.seq,100,100,95))
			
		if self.orient=="right":
			window.blit(self.pic,(self.x-50,self.y-30),(80*self.seq+3+163,0,78,80))
			#self.x=self.x+self.v
			#self.rect=Rect(self.x,self.y,50,50)

		if self.orient=="left":
			window.blit(self.pic2,(self.x-5,self.y-30),(80*self.seq+3,0,78,80))
			#self.x=self.x-self.v
			#self.rect=Rect(self.x,self.y,50,50)

		self.seq=(self.seq+1)%2

class Player(object):
	
	def __init__(self,x,y,name):
		self.x=x
		self.y=y
		self.size=(50,100)
		self.rect=Rect(self.x-0.5*self.size[0]+5,self.y+20,self.size[0]-10,self.size[1]-50)
		self.hp=100
		self.mp=100
		self.orient="right"
		self.mode = "stand"
		self.seq=0
		self.pic=image.load(name+".png")
		self.pic2=image.load(name+"2.png")
		self.pic3=image.load(name+"3.png")
		self.pic4=image.load(name+"4.png")
		
	def left(self):
		self.orient="left"
		self.mode="go"
		if self.x>0:
			self.x=self.x-5
		self.rect=Rect(self.x-0.5*self.size[0]+5,self.y+20,self.size[0]-10,self.size[1]-50)
			
	def right(self):
		self.orient="right"
		self.mode="go"
		if self.x<res[0]:
			self.x=self.x+5
		self.rect=Rect(self.x-0.5*self.size[0]+5,self.y+20,self.size[0]-10,self.size[1]-50)
			
	def up(self):
		self.mode="go"
		if self.y>horizon-self.size[1]:
			self.y=self.y-3
		self.rect=Rect(self.x-0.5*self.size[0]+5,self.y+20,self.size[0]-10,self.size[1]-50)
			
	def down(self):
		self.mode="go"
		if self.y<res[1]-100:
			self.y=self.y+3
		self.rect=Rect(self.x-0.5*self.size[0]+5,self.y+20,self.size[0]-10,self.size[1]-50)
			
			
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
		if self.mp>50 and b.orient=="stop":
			self.mode="attack3"
			if self.orient=="left":
				b.orient="left"
				b.x=self.x-80
			else:
				b.orient="right"
				b.x=self.x+40
			b.y=self.y+40
			self.mp=self.mp-50
		
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
				window.blit(self.pic,(self.x-40,self.y+3),(80*self.seq,0,80,80))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(80*self.seq+480,0,80,80))
		if self.mode=="go":
			if self.orient=="right":
				window.blit(self.pic,(self.x-40,self.y+3),(80*self.seq+240,0,80,80))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(80*self.seq+160,0,80,80))
		if self.mode=="attack1":
			if self.orient=="right":
				window.blit(self.pic,(self.x-40,self.y+3),(80*self.seq,80,80,80))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(80*self.seq+480,80,80,80))		
		if self.mode=="attack2":
			if self.orient=="right":
				window.blit(self.pic3,(self.x-40,self.y+3),(80*self.seq+480,0,75,80))
			else:
				window.blit(self.pic4,(self.x-40,self.y+3),(80*self.seq,0,75,80))	
		if self.mode=="attack3":
			if self.orient=="right":
				window.blit(self.pic3,(self.x-40,self.y+3),(80*self.seq+240,0,75,80))
			else:
				window.blit(self.pic4,(self.x-40,self.y+3),(80*self.seq+240,0,75,80))
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


frozen=image.load("frozen.bmp")
elektro=image.load("elektro.bmp")			
name1 = ""
name2 = ""
x1=-1000
x2 = -1000
y1 = -1000
y2 = -1000

end=False
while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True
	
	window.fill(black)

	draw.rect(window,blue,Rect(x1-5,y1-5,130,130),0)
	draw.rect(window,green,Rect(x2-5,y2-5,130,130),0)
	
	window.blit(frozen,(100,100))
	window.blit(frozen,(500,100))
	
	window.blit(elektro,(100,300))
	window.blit(elektro,(500,300))
	

	
	if mouse.get_pressed()[0] == 1:
		if mouse.get_pos()[0]>100 and mouse.get_pos()[0]<300 and mouse.get_pos()[1]>100 and mouse.get_pos()[1]<300:
			name1 = "frozen"
			x1 = 100
			y1 = 100
		if mouse.get_pos()[0]>500 and mouse.get_pos()[0]<700 and mouse.get_pos()[1]>100 and mouse.get_pos()[1]<200:
			name2 = "frozen"			
			x2 = 500
			y2 = 100
		if mouse.get_pos()[0]>100 and mouse.get_pos()[0]<300 and mouse.get_pos()[1]>300 and mouse.get_pos()[1]<500:
			name1 = "elektro"
			x1 = 100
			y1 = 300
		if mouse.get_pos()[0]>500 and mouse.get_pos()[0]<700 and mouse.get_pos()[1]>300 and mouse.get_pos()[1]<500:
			name2 = "elektro"
			x2 = 500
			y2 = 300
		if mouse.get_pos()[0]>320 and mouse.get_pos()[0]<420 and mouse.get_pos()[1]>300 and mouse.get_pos()[1]<330:
			end = True
	
	
	draw.rect(window,red,Rect(320,300,100,30),0)
	text = Font.render("START",True,(255,255,255))
	window.blit(text,(330,300))
	
	
	
	clock.tick(20)
	display.flip()

if name1 == "" and name2=="":
	name1 = "frozen"
	name2 = "frozen"


	
av1 = image.load(name1+".bmp")
av2 = image.load(name2+".bmp")
av1=transform.scale(av1,(80,80))
av2=transform.scale(av2,(80,80))


p2 = Player(200,100+horizon,name1)
p1 = Player(600,100+horizon,name2)
b1 = Ball(name2)
b2 = Ball(name1)
game = Game()
	
end = False 
while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True
			
	keys = key.get_pressed()
	
			
	if p1.hp>0 and p2.hp>0:
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
	b1.go(p2)
	b2.go(p1)
	game.draw()
	window.blit(av1,(10,10))
	window.blit(av2,(410,10))

	clock.tick(20)
	display.flip()
	