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
		self.pic=image.load(name+"/"+name+"ball.png")
		self.pic2=image.load(name+"/"+name+"ball2.png")
		self.seq=0
		
		file=open(name+"/"+name+".dat")
		for i in range(11):
			line1=file.readline().split()
		line2=file.readline().split()
		self.ball=[int(line1[0]),int(line1[1]),int(line1[2]),int(line1[3]),int(line2[0]),int(line2[1]),int(line2[2]),int(line2[3])]
		line1=file.readline().split()
		line2=file.readline().split()
		line3=file.readline().split()
		self.at= int(line3[1])
		
	def go(self,p):
		if self.orient=="right":
			self.x=self.x+self.v
			self.rect=Rect(self.x,self.y,50,50)

		if self.orient=="left":
			self.x=self.x-self.v
			self.rect=Rect(self.x,self.y,50,50)		
		
		if self.rect.colliderect(p.rect):
			p.hp=p.hp-self.at
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
			window.blit(self.pic,(self.x-50,self.y-30),(self.ball[2]*self.seq+self.ball[0],self.ball[1],self.ball[2],self.ball[3]))

		if self.orient=="left":
			window.blit(self.pic2,(self.x-50,self.y-30),(self.ball[6]*self.seq+self.ball[4],self.ball[5],self.ball[6],self.ball[7]))

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
		self.pic=image.load(name+"/"+name+".png")
		self.pic2=image.load(name+"/"+name+"2.png")
		self.pic3=image.load(name+"/"+name+"3.png")
		self.pic4=image.load(name+"/"+name+"4.png")
		
		file=open(name+"/"+name+".dat")
		line1=file.readline().split()
		line2=file.readline().split()
		self.stand=[int(line1[0]),int(line1[1]),int(line1[2]),int(line1[3]),int(line2[0]),int(line2[1]),int(line2[2]),int(line2[3])]
		line1=file.readline().split()
		line2=file.readline().split()
		self.go=[int(line1[0]),int(line1[1]),int(line1[2]),int(line1[3]),int(line2[0]),int(line2[1]),int(line2[2]),int(line2[3])]		
		line1=file.readline().split()
		line2=file.readline().split()
		self.at1=[int(line1[0]),int(line1[1]),int(line1[2]),int(line1[3]),int(line2[0]),int(line2[1]),int(line2[2]),int(line2[3])]
		line1=file.readline().split()
		line2=file.readline().split()
		self.at2=[int(line1[0]),int(line1[1]),int(line1[2]),int(line1[3]),int(line2[0]),int(line2[1]),int(line2[2]),int(line2[3])]
		line1=file.readline().split()
		line2=file.readline().split()
		self.at3=[int(line1[0]),int(line1[1]),int(line1[2]),int(line1[3]),int(line2[0]),int(line2[1]),int(line2[2]),int(line2[3])]
		line1=file.readline().split()
		line1=file.readline().split()
		line1=file.readline().split()
		line2=file.readline().split()
		line3=file.readline().split()
		self.at=[int(line1[0]),int(line1[1]),int(line2[0]),int(line2[1]),int(line3[0]),int(line3[1])]
		
		file.close()
		
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
		if self.rect.colliderect(p.rect) and p.hp>0 and self.mp>self.at[1]:
			p.hp=p.hp-self.at[0]
		if self.mp>self.at[1]:
			self.mp=self.mp-self.at[1]
		else:
			self.mode="stand"
			
	def attack2(self,p):
		self.mode="attack2"
		if self.rect.colliderect(p.rect) and p.hp>0 and self.mp>self.at[3]:
			p.hp=p.hp-self.at[2]
		if self.mp>self.at[3]:
			self.mp=self.mp-self.at[3]
		else:
			self.mode="stand"
			
	def attack3(self,b):
		if self.mp>self.at[5] and b.orient=="stop":
			self.mode="attack3"
			if self.orient=="left":
				b.orient="left"
				b.x=self.x-80
			else:
				b.orient="right"
				b.x=self.x+40
			b.y=self.y+40
			self.mp=self.mp-self.at[5]
		

			
	def draw(self):
		#draw.rect(window,white,self.rect,1)
		#draw.rect(window,white,Rect(self.x+0,self.y+self.size[1],50,100),1)
		
		if self.mode=="stand":
			if self.orient=="right":
				window.blit(self.pic,(self.x-40,self.y+3),(self.stand[2]*self.seq+self.stand[0],self.stand[1],self.stand[2],self.stand[3]))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(self.stand[6]*self.seq+self.stand[4],self.stand[5],self.stand[6],self.stand[7]))
		if self.mode=="go":
			if self.orient=="right":
				window.blit(self.pic,(self.x-40,self.y+3),(self.go[2]*self.seq+self.go[0],self.go[1],self.go[2],self.go[3]))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(self.go[6]*self.seq+self.go[4],self.go[5],self.go[6],self.go[7]))
		if self.mode=="attack1":
			if self.orient=="right":
				window.blit(self.pic,(self.x-40,self.y+3),(self.at1[2]*self.seq+self.at1[0],self.at1[1],self.at1[2],self.at1[3]))
			else:
				window.blit(self.pic2,(self.x-40,self.y+3),(self.at1[6]*self.seq+self.at1[4],self.at1[5],self.at1[6],self.at1[7]))
		if self.mode=="attack2":
			if self.orient=="right":
				window.blit(self.pic3,(self.x-40,self.y+3),(self.at2[2]*self.seq+self.at2[0],self.at2[1],self.at2[2],self.at2[3]))
			else:
				window.blit(self.pic4,(self.x-40,self.y+3),(self.at2[6]*self.seq+self.at2[4],self.at2[5],self.at2[6],self.at2[7]))
		if self.mode=="attack3":
			if self.orient=="right":
				window.blit(self.pic3,(self.x-40,self.y+3),(self.at3[2]*self.seq+self.at3[0],self.at3[1],self.at3[2],self.at3[3]))
			else:
				window.blit(self.pic4,(self.x-40,self.y+3),(self.at3[6]*self.seq+self.at3[4],self.at3[5],self.at3[6],self.at3[7]))
		self.seq=(self.seq+1)%4
		self.mode="stand"
		if self.mp<100 and self.seq==0:
			self.mp=self.mp+1
	
class Game(object):
	
	def __init__(self):
		pass
	
	def draw(self):
		draw.rect(window,(0,0,0),Rect(0,0,res[0],res[1]),0)
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



			
			
			
char=["frozen","firen","elektro","henry","deep","jan","dennis","rudolf"]
av=[]
for c in char:
	av.append(image.load(c+"/"+c+".bmp"))
	
select1=1
select2=1			

end=False
while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True
	
	window.fill(black)
	
	if select1 in [0,1,2,3]:
		draw.rect(window,blue,Rect(25,select1*125,130,130),0)
	if select1 in [4,5,6,7]:
		draw.rect(window,blue,Rect(175,(select1-4)*125,130,130),0)
	if select2 in [0,1,2,3]:
		draw.rect(window,green,Rect(445,select2*125,130,130),0)
	if select2 in [4,5,6,7]:
		draw.rect(window,green,Rect(595,(select2-4)*125,130,130),0)		
		
	for i in range(4):
		window.blit(av[i],(30,i*125+5))
		window.blit(av[i],(450,i*125+5))
		window.blit(av[i+4],(180,i*125+5))
		window.blit(av[i+4],(600,i*125+5))
	
	
	if mouse.get_pressed()[0]:
		if mouse.get_pos()[0]>320 and mouse.get_pos()[0]<420 and mouse.get_pos()[1]>300 and mouse.get_pos()[1]<330:
			end = True
		for i in range(4):
			if mouse.get_pos()[0]>30 and mouse.get_pos()[0]<150 and mouse.get_pos()[1]>i*125+5 and mouse.get_pos()[1]<i*125+125:
				select1=i
			if mouse.get_pos()[0]>180 and mouse.get_pos()[0]<300 and mouse.get_pos()[1]>i*125+5 and mouse.get_pos()[1]<i*125+125:
				select1=i+4
			if mouse.get_pos()[0]>450 and mouse.get_pos()[0]<570 and mouse.get_pos()[1]>i*125+5 and mouse.get_pos()[1]<i*125+125:
				select2=i
			if mouse.get_pos()[0]>600 and mouse.get_pos()[0]<720 and mouse.get_pos()[1]>i*125+5 and mouse.get_pos()[1]<i*125+125:
				select2=i+4
	
	
	draw.rect(window,red,Rect(320,300,100,30),0)
	text = Font.render("START",True,(255,255,255))
	window.blit(text,(330,300))
	
	
	
	clock.tick(20)
	display.flip()

	
	
	
	


	
av1 = image.load(char[select1]+"/"+char[select1]+".bmp")
av2 = image.load(char[select2]+"/"+char[select2]+".bmp")
av1=transform.scale(av1,(80,80))
av2=transform.scale(av2,(80,80))


p2 = Player(200,100+horizon,char[select1])
p1 = Player(600,100+horizon,char[select2])
b1 = Ball(char[select2])
b2 = Ball(char[select1])
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
