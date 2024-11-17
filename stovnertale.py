import pygame
import time
from math import pi
import math
from random import randint
import os
import ast
import sys
dir = str(os.path.dirname(os.path.abspath(sys.argv[0]))) + '/Data/'
pygame.init()
cl = pygame.time.Clock()
skj = pygame.display.set_mode((1000,700))
pygame.display.set_caption("StovnerTale")

pygame.display.set_icon(pygame.image.load(dir+"weedsymbol.png"))
undertalefont = pygame.font.Font(dir+"font/PixelOperatorHB.ttf" ,70)
undertalefont2 = pygame.font.Font(dir+"font/PixelOperatorMonoHB8.ttf",30)
undertalefont3 = pygame.font.Font(dir+"font/PixelOperator.ttf",60)
undertalefont4 = pygame.font.Font(dir+"font/PixelOperator.ttf",30)
undertalefont5 = pygame.font.Font(dir+"font/PixelOperatorMonoHB8.ttf",35)
undertalefont6 = pygame.font.Font(dir+"font/PixelOperatorMonoHB8.ttf",10)
undertalefont7 = pygame.font.Font(dir+"font/PixelOperator.ttf",50)
undertaleorange = (255,127,39)
undertaleyellow = (255,255,0)
undertalelightpurple = (185,100,185)
undertalepurple = (133,53,126)
bak_col = (0,0,0)
collision_col = (255,255,255)

image1 = pygame.transform.scale((pygame.image.load(dir+"player1.png")),(64,94))
image2 = pygame.transform.scale((pygame.image.load(dir+"player2.png")),(64,94))
image3 = image1
image4 = pygame.transform.scale((pygame.image.load(dir+"player4.png")),(64,94))
image5 = pygame.transform.scale((pygame.image.load(dir+"player5.png")),(64,94))
image6 = pygame.transform.scale((pygame.image.load(dir+"player6.png")),(64,94))
image7 = image5
image8 = pygame.transform.scale((pygame.image.load(dir+"player8.png")),(64,94))
image9 = pygame.transform.scale((pygame.image.load(dir+"player9.png")),(64,94))
image10 = pygame.transform.scale((pygame.image.load(dir+"player10.png")),(64,94))
image11 = image9
image12 = pygame.transform.scale((pygame.image.load(dir+"player12.png")),(64,94))
image13 = pygame.transform.flip(image5,True,False)
image14 = pygame.transform.flip(image6,True,False)
image15 = image13
image16 = pygame.transform.flip(image8,True,False)
pat = pygame.transform.scale((pygame.image.load(dir+"pat.png")),(74,123))
pat2 = pygame.transform.scale((pygame.image.load(dir+"pat.png")),(221,369))
muj = pygame.transform.scale((pygame.image.load(dir+"mujaffa.png")),(274,314)) #68 78
muj2 = pygame.transform.scale((pygame.image.load(dir+"mujaffa.png")),(136,156)) #68 78
mujaffabil = pygame.transform.scale((pygame.image.load(dir+"mujaffabil.png")),(200,130))
mujaffabil2 = pygame.transform.scale((pygame.image.load(dir+"mujaffabil2.png")),(225,225)) #90 90
er09 = pygame.transform.scale((pygame.image.load(dir+"09-er.png")),(186,144))#31 24
stojent = pygame.transform.scale((pygame.image.load(dir+"stovnerjenter.png")),(525,375)) # 70 50
foxtrotkids=  pygame.transform.scale((pygame.image.load(dir+"foxtrotkids.png")),(420,350)) #70 50
foxtrotkids2 = pygame.transform.scale((pygame.image.load(dir+"foxtrotkidsa.png")),(280,249)) #70 63
foxtrotguy=  pygame.transform.scale((pygame.image.load(dir+"foxtrotguy.png")),(70,123)) #70 123
foxtrotguy2 = pygame.transform.scale((pygame.image.load(dir+"foxtrotguy2.png")),(245,350)) #70 100
gun = pygame.transform.scale((pygame.image.load(dir+"gun2.png")),(29,29))# 58 40   
gun2 = pygame.transform.scale((pygame.image.load(dir+"gun2.png")),(232,230))# 58 40  #232 160
poster = pygame.transform.scale((pygame.image.load(dir+"posters.png")),(38,75))# 50 100
elsparkesykkel = pygame.transform.scale((pygame.image.load(dir+"sykkel.png")),(100,118))# 100 118
weed = pygame.transform.scale((pygame.image.load(dir+"weedsymbol.png")),(20,20))# 20 20
jonna = pygame.transform.scale((pygame.image.load(dir+"jonna.png")),(140,240))# 700 1200
jonna2 = pygame.transform.scale((pygame.image.load(dir+"jonna.png")),(210,432))# 700 1200
shelves = pygame.transform.scale((pygame.image.load(dir+"bunkerstorage.png")),(196,120))# 192 120
ak47 = pygame.transform.scale((pygame.image.load(dir+"ak47.png")),(270,124))# 1350 620
doomshotgun = pygame.transform.scale((pygame.image.load(dir+"doomshotgun.png")),(270,64))# 1350 322
tankbody = pygame.transform.scale((pygame.image.load(dir+"tankbody.png")),(209,123))# 261 154
tankhead = pygame.transform.scale((pygame.image.load(dir+"tankhead.png")),(360,360))#450 450
nuke = pygame.transform.scale((pygame.image.load(dir+"mininuke.png")),(100,50))#100 50
sunset = pygame.transform.scale((pygame.image.load(dir+"sunset.png")),(402,400))#201 200
star1 = pygame.transform.scale((pygame.image.load(dir+"star1.png")),(64,64))#32 32
star2 = pygame.transform.scale((pygame.image.load(dir+"star2.png")),(64,64))#32 32
logo = pygame.transform.scale((pygame.image.load(dir+"logo.jpg")),(812,84))#203 21


px = 500
py = 300
savepx = 500
savepy = 300
lvl = 0
exp = 0
rank = "Weed Amateur"
brukskonto = 0
inventory = []
pdamage = 4 + lvl
talkstun = False
playername = None#"TEST"
HPmax = 20 +(lvl*2)
HP = HPmax
enemy = ""
encountered_09 = False
globalangle = 0
AntiMoonwalkProcedure = False
room = 1
walkanim = 1
walkani = 1
mujanim = 650
mujani = 0
jonna_x = 0
jonna_y = 0
jonna_ani = 0
lightswitch = 0
enc_muj = False
enc_gang = False
enc_boss = False
enc_jonna = False
image = image1
is_dead = False
ismoving = False
hasbunkerkey = False
encounter_cooldown = 120
traderlimit = 4
temptalk1 = ""
temptalk2 = ""
tempplacement = 0
spa = "up"
is_combat = False
is_combatmenu = False
is_roaming = False 
is_intro = False
is_outro = False
is_startmenu = True
for event in pygame.event.get():pass
if not os.path.exists(dir+"Data.txt"):
    o = open(dir+"Data.txt","a")
    o.write("0")
    o.close()
with open(dir+"Data.txt","r") as o:
    load = o.read()
    o.flush()
def savedata():
    global load,playername,px,py,lvl,exp,inventory,mujani,encountered_09,enc_muj,jonna_ani,enc_gang,enc_boss,enc_jonna,room,rank,lightswitch,hasbunkerkey
    playerdata = [playername,px,py,lvl,exp,inventory,room,rank]
    progressdata = [mujani,encountered_09,enc_muj,jonna_ani,enc_gang,enc_boss,lightswitch,enc_jonna,hasbunkerkey]
    itemts = [playerdata,progressdata]
    with open(dir+"Data.txt","w") as o:
        o.write(str(itemts))
        o.flush()
    with open(dir+"Data.txt","r") as o:
        load = o.read()
        o.flush()
def loaddata():
    global load,playername,px,py,lvl,exp,inventory,room,mujani,encountered_09,enc_muj,jonna_ani,enc_gang,enc_boss,enc_jonna,room,rank,lightswitch,savepx,savepy,hasbunkerkey
    with open(dir+"Data.txt","r") as o:
        load = o.read()
        o.flush()
    if load!="0":
        load = ast.literal_eval(load)
        playername=load[0][0]
        px=load[0][1]
        py=load[0][2]
        lvl=load[0][3]
        exp=load[0][4]
        inventory=load[0][5]
        room=load[0][6]
        rank=load[0][7]
        mujani=load[1][0]
        encountered_09=load[1][1]
        enc_muj=load[1][2]
        jonna_ani=load[1][3]
        enc_gang=load[1][4]
        enc_boss=load[1][5]
        lightswitch=load[1][6]    
        enc_jonna=load[1][7]    
        hasbunkerkey=load[1][8]    
        savepx=load[0][1]
        savepy=load[0][2]
def savingmenu():
    global savemenu,talkstun,menu_select,spa,load
    if load!="0":
        with open(dir+"Data.txt","r") as o:
            tempload =ast.literal_eval(o.read())
            o.flush()
        displayname = tempload[0][0]
        displaylvl = tempload[0][3]
    else:
        displayname = "NONE"
        displaylvl = "NaN"
    pygame.draw.rect(skj,(0,0,0),(150,300,700,200))
    pygame.draw.rect(skj,(255,255,255),(150,300,700,200),6)    
    skj.blit(undertalefont2.render(f"{displayname}   NIVÅ {displaylvl}",False,(255,255,255)),(180,330))
    if menu_select==1:skj.blit(undertalefont3.render("* Save",False,(undertaleyellow)),(180,430))
    else:skj.blit(undertalefont3.render("Save",False,(255,255,255)),(180,430))
    if load!="0":temp = "Load"
    else:temp = "---"
    if menu_select==2:skj.blit(undertalefont3.render(f"* {temp}",False,(undertaleyellow)),(400,430))
    else:skj.blit(undertalefont3.render(temp,False,(255,255,255)),(400,430))
    if menu_select==3:skj.blit(undertalefont3.render("* Tilbake",False,(undertaleyellow)),(600,430))
    else:skj.blit(undertalefont3.render("Tilbake",False,(255,255,255)),(600,430))
    if menu_select==1 and spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
        savedata()
        spa = "up"
        talkstun = False
        savemenu = False
    if menu_select==2 and spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
        loaddata()
        talkstun = False
        savemenu = False
        spa = "up"
    if menu_select==3 and spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
        talkstun = False
        savemenu = False
        spa = "up"

def ps(ang):
    global px,py,psize
    vec = pygame.math.Vector2(0,-int(psize/2)).rotate(ang)
    ptx,pty= px+vec.x,py+vec.y
    return str(skj.get_at((int(ptx),int(pty))))[0:-6]+")"
def ps2(c):
    check = False
    for i in range(36):
        if ps(i*10)==c: check = True
    return check
def playermovement():
    global px,py,psize,pspeed,bak_col,collision_col,ismoving,globalangle,AntiMoonwalkProcedure
    ke = pygame.key.get_pressed()
    dx = 0
    dy = 0
    ismoving = False
    AntiMoonwalkProcedure = False
    c = str(collision_col)
    if ke[pygame.K_w]or ke[pygame.K_a]or ke[pygame.K_s]or ke[pygame.K_d]or ke[pygame.K_UP]or ke[pygame.K_LEFT]or ke[pygame.K_DOWN]or ke[pygame.K_RIGHT]:
        ismoving = True
        if ke[pygame.K_a]or ke[pygame.K_LEFT]:
            dx += -1
        if ke[pygame.K_d]or ke[pygame.K_RIGHT]:
            dx += 1
        if ke[pygame.K_w]or ke[pygame.K_UP]:
            dy += -1
        if ke[pygame.K_s]or ke[pygame.K_DOWN]:  
            dy += 1
        ang = (math.atan2(dy, dx) * (180 / pi )) 
        if globalangle==None:globalangle =int(ang+90)
        else:
            if not (int(ang+90)>globalangle-50 and int(ang+90)<globalangle+50) and not (dx == 0 and dy == 0):             
                globalangle = int(ang+90)
            elif (dx == 0 and dy == 0):
                AntiMoonwalkProcedure = True
            if (dx == 0 and dy == -1): globalangle = int(ang+90)
            if (dx==-1 and dy==-1):AntiMoonwalkProcedure=False
        if globalangle == -45: globalangle = 315
        if not math.radians(ang) == 0.0:
            px += pspeed * math.sin(math.radians(ang+90))
            if ps2(c):
                px -= pspeed * math.sin(math.radians(ang+90))
            py -= pspeed * math.cos(math.radians(ang+90))
            if ps2(c):
                py += pspeed * math.cos(math.radians(ang+90))
        else:       
            if (ke[pygame.K_d]or ke[pygame.K_RIGHT]) and not (ke[pygame.K_w]or ke[pygame.K_a]or ke[pygame.K_s]or ke[pygame.K_UP]or ke[pygame.K_LEFT]or ke[pygame.K_DOWN]):
                px += pspeed * math.sin(math.radians(ang+90))
                if ps2(c):
                    px -= pspeed* math.sin(math.radians(ang+90))
    else: globalangle = None
def playeranimation():
    global ke,walkani,walkanim,playerect,image,talkstun,globalangle,AntiMoonwalkProcedure
    if (ke[pygame.K_w]or ke[pygame.K_a]or ke[pygame.K_s]or ke[pygame.K_d]or ke[pygame.K_UP]or ke[pygame.K_LEFT]or ke[pygame.K_DOWN]or ke[pygame.K_RIGHT]) and talkstun == False:
        if walkanim >10:
            walkani+=1
            walkanim = 1
        if walkani>4: walkani = 1
        if globalangle>=0 and globalangle<45 or globalangle>=315 and globalangle<=0:
            if walkani ==1: image = image9
            if walkani ==2: image = image10
            if walkani ==3: image = image11
            if walkani ==4: image = image12
            if AntiMoonwalkProcedure==True: image=image9
        if globalangle>=45 and globalangle<135:
            if walkani ==1: image = image5
            if walkani ==2: image = image6
            if walkani ==3: image = image7
            if walkani ==4: image = image8
            if AntiMoonwalkProcedure==True: image=image5
        if globalangle>=135 and globalangle<225:
            if walkani ==1: image = image1
            if walkani ==2: image = image2
            if walkani ==3: image = image3
            if walkani ==4: image = image4
            if AntiMoonwalkProcedure==True: image=image1
        if globalangle>=225 and globalangle<=315:
            if walkani ==1: image = image13
            if walkani ==2: image = image14
            if walkani ==3: image = image15
            if walkani ==4: image = image16
            if AntiMoonwalkProcedure==True: image=image13
        playerect = image.get_rect(topleft = (px-32,py-62))
        walkanim+=1
    else:
        playerect = image1.get_rect(topleft = (px-32,py-62))
        walkani = 1
def orangebutton(x,y,dcol,text,symbol,dis):
    global bak_col
    pygame.draw.rect(skj,dcol,(x,y,173,70),3,1)
    if symbol == "sword":
        pygame.draw.line(skj,dcol,(x+18,y+58),(x+27,y+20),4)
        pygame.draw.line(skj,dcol,(x+20,y+56),(x+32,y+20),5)
        pygame.draw.lines(skj,dcol,False,[(x+27,y+20),(x+30,y+12),(x+32,y+20)],3)
        pygame.draw.line(skj,dcol,(x+15,y+39),(x+35,y+47),3)
        pygame.draw.line(skj,dcol,(x+17,y+40),(x+32,y+47),5)
    if symbol == "act":
        pygame.draw.lines(skj,dcol,False,[(x+19,y+29),(x+20,y+30),(x+20,y+40),(x+19,y+41)],3)
        pygame.draw.lines(skj,dcol,False,[(x+24,y+23),(x+26,y+25),(x+26,y+45),(x+24,y+47)],3)
        pygame.draw.lines(skj,dcol,False,[(x+29,y+17),(x+32,y+20),(x+32,y+50),(x+29,y+53)],4)
    if symbol == "item":
        pygame.draw.line(skj,dcol,(x+28,y+18),(x+18,y+55),8)
        pygame.draw.circle(skj,bak_col,(x+19,y+58),7)
        pygame.draw.circle(skj,dcol,(x+19,y+58),5)
    if symbol == "mercy":
        pygame.draw.line(skj,dcol,(x+15,y+18),(x+40,y+54),5)
        pygame.draw.line(skj,dcol,(x+35,y+19),(x+18,y+55),5)
        pass
    skj.blit(undertalefont.render((text),False,dcol),(x+42+dis,y-2))
def buttonkey(x,y,text,col):
    if text!="BACKSPACE" and text!="CONFIRM":
        pygame.draw.rect(skj,(col),(x,y,80,80),3,5)
        skj.blit(undertalefont.render(str(text),False,(col)),(x+25,y+5))
    if text=="BACKSPACE":
        pygame.draw.rect(skj,(col),(x,y,160,80),3,5)
        pygame.draw.line(skj,(col),(x+60,y+40),(x+120,y+40),6)
        pygame.draw.polygon(skj,(col),[(x+60,y+20),(x+60,y+60),(x+30,y+40)])
    if text =="CONFIRM":
        pygame.draw.rect(skj,(col),(x,y,290,80),3,5)
        skj.blit(undertalefont.render("CONFIRM",False,(col)),(x+25,y+5))
def dialogue(y,text1,text2,text3):
    pygame.draw.rect(skj,(0,0,0),(50,y,900,200))
    pygame.draw.rect(skj,(255,255,255),(50,y,900,200),10)
    skj.blit(undertalefont3.render(text1,False,(255,255,255)),(80,y+10))
    skj.blit(undertalefont3.render(text2,False,(255,255,255)),(80,y+70))
    skj.blit(undertalefont3.render(text3,False,(255,255,255)),(80,y+130))
def talkbubble(x,y,len,hei,point,text1,text2,text3):
    pygame.draw.rect(skj,(255,255,255),(x,y,len,hei),0,25)
    if point ==1: pygame.draw.polygon(skj,(255,255,255),[(x,y+50),(x,y+70),(x-50,y+60)])
    if point ==2: pygame.draw.polygon(skj,(255,255,255),[(x+len,y+hei/3),(x+len,y+hei/3+20),(x+len+50,y+hei/3+10)])
    skj.blit(undertalefont4.render(text1,False,(0,0,0)),(x+20,y+20))
    skj.blit(undertalefont4.render(text2,False,(0,0,0)),(x+20,y+50))
    skj.blit(undertalefont4.render(text3,False,(0,0,0)),(x+20,y+80))
def trading():
    global talkstun,hideplayer,menu_element,menu_select,spa,tradermenu,inventory,brukskonto,undertalefont3,pat2,undertaleyellow,room
    talkstun = True
    hideplayer = True
    pygame.draw.rect(skj,(0,0,0),(0,300,1000,400))
    pygame.draw.rect(skj,(255,255,255),(0,300,1000,100),10)                  
    pygame.draw.rect(skj,(255,255,255),(0,400,1000,300),10)                  
    skj.blit(pat2,pat2.get_rect(topleft = (800,400)))
    skj.blit(undertalefont3.render(str("PatPat's WeedShop            konto: ")+str(brukskonto)+"kr",False,(255,255,255)),(30,315)) 
    if menu_element == 0:
        skj.blit(undertalefont3.render("Halla drittunge!",False,(255,255,255)),(30,415))
        skj.blit(undertalefont3.render("Vil du ha litt naarkoootika?",False,(255,255,255)),(30,475))
        if event.type == pygame.KEYUP and spa == "down":
            if event.key == pygame.K_SPACE:
                menu_element = 1
                spa = "up"
    if menu_element == 1:
        if menu_select ==1:
            skj.blit(undertalefont3.render("* Tilbake",False,(undertaleyellow)),(30,415)) 
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talkstun = False
                hideplayer = False
                tradermenu = False
                spa = "up"                                     
        else:
                skj.blit(undertalefont3.render("Tilbake",False,(255,255,255)),(30,415))  
        if menu_select ==2:
            skj.blit(undertalefont3.render("* Vape (ett trekk)           25kr",False,(undertaleyellow)),(30,475))
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                if brukskonto >= 25:
                    if len(inventory)<6:
                        inventory.append("Vape")
                        brukskonto -=25
                    else:
                        menu_element = 3
                else:
                    menu_element = 2
                spa = "up"                 
        else:
                skj.blit(undertalefont3.render("Vape (ett trekk)            25kr",False,(255,255,255)),(30,475))  
        if menu_select ==3:
            skj.blit(undertalefont3.render("* Joint                            100kr",False,(undertaleyellow)),(30,525))  
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                if brukskonto >= 100:
                    if len(inventory)<6:
                        inventory.append("Joint")
                        brukskonto -=100
                    else:
                        menu_element = 3
                else:
                    menu_element = 2
                spa = "up"                                                    
        else:
                skj.blit(undertalefont3.render("Joint                             100kr",False,(255,255,255)),(30,525))  
        if menu_select ==4:
            skj.blit(undertalefont3.render("* Keef                      250kr",False,(undertaleyellow)),(30,585)) 
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                if brukskonto >= 250:
                    if len(inventory)<6:
                        inventory.append("Keef")
                        brukskonto -=250
                    else:
                        menu_element = 3
                else:
                    menu_element = 2
                spa = "up"                    
        else:
                skj.blit(undertalefont3.render("Keef                            250kr",False,(255,255,255)),(30,585))  
        if room ==9:
            if menu_select ==5:
                skj.blit(undertalefont3.render("* Svart Afghan                   500kr",False,(undertaleyellow)),(30,635)) 
                if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                    if brukskonto >= 500:
                        if len(inventory)<6:
                            inventory.append("Svart Afghan")
                            brukskonto -=500
                        else:
                            menu_element = 3
                    else:
                        menu_element = 2
                    spa = "up"                    
            else:
                    skj.blit(undertalefont3.render("Svart Afghan                    500kr",False,(255,255,255)),(30,635))  
    if menu_element ==2:
        skj.blit(undertalefont3.render("Ingen penger, Ingen narkotika!",False,(255,255,255)),(30,415))
        if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
            talkstun = False
            hideplayer = False
            tradermenu = False
            spa = "up"                 
    if menu_element ==3:
        skj.blit(undertalefont3.render("Du har ingen plass i de XXS-size ",False,(255,255,255)),(30,415))
        skj.blit(undertalefont3.render("lommene dine for å kjøpe mer ",False,(255,255,255)),(30,475))
        if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
            talkstun = False
            hideplayer = False
            tradermenu = False
            spa = "up"  
def win_screen():
    global enemy,earnedexp,earnedkr,exp,brukskonto,talk,is_roaming,is_combatmenu,spa,enc_boss,enc_jonna,enc_boss,enc_muj,enc_gang
    pygame.draw.rect(skj,(0,0,0),(50,200,900,400))
    pygame.draw.rect(skj,(255,255,255),(50,200,900,400),10)
    skj.blit(undertalefont3.render("Du gætta den rett ned bro",False,(255,255,255)),(80,300+10))
    if enemy == "09":
        earnedexp = 5
        earnedkr = 15
    if enemy == "stovnerjenter":
        earnedexp = 10
        earnedkr = 30
    if enemy == "mujaffa":
        earnedexp = 30
        earnedkr = 100
        enc_muj = True
    if enemy == "foxtrotkids":
        earnedexp = 40
        earnedkr = 100
        if room == 8: enc_gang = True
    if enemy == "foxtrotguy":
        earnedexp = 50
        earnedkr = 150
        enc_boss = True
    if enemy == "jonna":
        earnedexp = 100
        earnedkr = 250
        enc_jonna = None
    skj.blit(undertalefont3.render(str("+"+str(earnedexp)+" EXP  ("+str((exp+earnedexp))+"/"+str(((lvl+1)*5))+")"),False,(255,255,255)),(80,300+80))
    skj.blit(undertalefont3.render(str("+"+str(earnedkr)+" Kr"),False,(255,255,255)),(80,300+140))

    if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
        talk = 0
        exp += earnedexp
        brukskonto += earnedkr
        is_roaming = True
        is_combatmenu = False
        spa = "up"
def enemies():
    global enemy,spa,combat_timer,menu_element,menu_select,triedtorunlikeabitch,turn,talk,is_roaming,is_combatmenu,is_combat,menupause,encountered_09,enemyHP
    if enemy == "mujaffa":
        combat_timer = 900
        if menu_element ==0:
            if triedtorunlikeabitch == False:
                if turn == 0:
                    skj.blit(undertalefont3.render("Mujaffa står foran deg",False,(255,255,255)),(80,350))
                    skj.blit(undertalefont3.render("Mujaffas BMW durer rolig bak han",False,(255,255,255)),(80,400))
                    skj.blit(undertalefont3.render("Dette blir en hard kamp",False,(255,255,255)),(80,450))
                else:
                    skj.blit(undertalefont3.render("Mujaffa prøver å få kontakt med",False,(255,255,255)),(80,350))
                    skj.blit(undertalefont3.render("en mæbe som går på fortauet.",False,(255,255,255)),(80,400))
                    skj.blit(undertalefont3.render("Han blir ignorert..",False,(255,255,255)),(80,450))
            else:
                skj.blit(undertalefont3.render("Du kan ikke løpe fra Mujaffa..",False,(255,255,255)),(80,350))
                skj.blit(undertalefont3.render("Han har Mujaffas BMW",False,(255,255,255)),(80,400))
        if menu_element ==2:
            skj.blit(undertalefont3.render("Ingen ord du kunne sagt ville hatt",False,(255,255,255)),(80,350))
            skj.blit(undertalefont3.render("noen invirkning på Mujaffa",False,(255,255,255)),(80,400))
            if menu_select ==1:
                skj.blit(undertalefont3.render("  * tilbake",False,(undertaleyellow)),(80,450))
            else:
                skj.blit(undertalefont3.render("  tilbake",False,(255,255,255)),(80,450))
    if enemy == "09":
        combat_timer = 600
        if talk == 0:
            if menu_element ==0:
                if triedtorunlikeabitch == False or encountered_09 == False:
                    if turn == 0:
                        skj.blit(undertalefont3.render("En 09er jump-",False,(255,255,255)),(80,350))
                        skj.blit(undertalefont3.render("ehh... prøver å jumpe deg",False,(255,255,255)),(80,400))
                        skj.blit(undertalefont3.render("(Han er for lav)",False,(255,255,255)),(80,450))
                    else:
                        skj.blit(undertalefont3.render("Du er overrasket over hvordan",False,(255,255,255)),(80,350))
                        skj.blit(undertalefont3.render("drittungen fortsatt lever",False,(255,255,255)),(80,400))
                else:
                    skj.blit(undertalefont3.render("Bro prøvde å rømme fra en 09-er",False,(255,255,255)),(80,350))
                    skj.blit(undertalefont3.render("     :skull_emoji:",False,(255,255,255)),(80,400))
            if menu_element ==2:
                if menu_select ==1:
                    skj.blit(undertalefont3.render("* tilbake",False,(undertaleyellow)),(80,350))
                else:
                    skj.blit(undertalefont3.render("tilbake",False,(255,255,255)),(80,350))
                if menu_select ==2:
                    skj.blit(undertalefont3.render("* Introduser deg selv",False,(undertaleyellow)),(380,350))
                else:
                    skj.blit(undertalefont3.render("Introduser deg selv",False,(255,255,255)),(380,350))
        if talk == 1:
            skj.blit(undertalefont3.render("Du prøver å introdusere deg selv",False,(255,255,255)),(80,350))
            skj.blit(undertalefont3.render("til misfosteret..",False,(255,255,255)),(80,400))
            if event.type == pygame.KEYUP and spa == "down":
                if event.key == pygame.K_SPACE:
                    talk = 2
                    spa = "up"
        if talk == 2:
            skj.blit(undertalefont3.render("Han forstår ikke språket du snakker",False,(255,255,255)),(80,350))
            skj.blit(undertalefont3.render("og kaller deg en",False,(255,255,255)),(80,400))
            skj.blit(undertalefont3.render('"skibbidy gyatt"',False,(255,255,255)),(80,450))
            if event.type == pygame.KEYUP and spa == "down":
                if event.key == pygame.K_SPACE:
                    talk =0 
                    menupause = False
                    spa = "up"   
        if talk == -1:
                skj.blit(undertalefont3.render("Du jetter unna",False,(255,255,255)),(80,350))
                if event.type == pygame.KEYUP and spa == "down":
                    if event.key == pygame.K_SPACE:
                        is_roaming = True
                        is_combatmenu = False                        
                        talk = 0
                        menupause = False
                        spa = "up" 
    if enemy == "stovnerjenter":
        combat_timer = 600
        if talk == 0:
            if menu_element == 0:
                if turn == 0:
                    skj.blit(undertalefont3.render('To "jenter" står foran deg',False,(255,255,255)),(80,350))
                else:
                    skj.blit(undertalefont3.render("Du tåler ikke å se på dem mer.",False,(255,255,255)),(80,350))
            if menu_element == 2:
                if menu_select ==1:
                    skj.blit(undertalefont3.render("* tilbake",False,(undertaleyellow)),(80,350))
                else:
                    skj.blit(undertalefont3.render("tilbake",False,(255,255,255)),(80,350))
                if menu_select ==2:
                    skj.blit(undertalefont3.render("* Snakk om været",False,(undertaleyellow)),(380,350))
                else:
                    skj.blit(undertalefont3.render("Snakk om været",False,(255,255,255)),(380,350))
        if talk == 1:
            skj.blit(undertalefont3.render("Du prøver å slå ann en prat",False,(255,255,255)),(80,350))
            skj.blit(undertalefont3.render("om været..",False,(255,255,255)),(80,400))
            if event.type == pygame.KEYUP and spa == "down":
                if event.key == pygame.K_SPACE:
                    talk = 2
                    spa = "up"
        if talk == 2:
            skj.blit(undertalefont3.render("De ignorerer deg og spør om",False,(255,255,255)),(80,350))
            skj.blit(undertalefont3.render("du vil se kukene deres",False,(255,255,255)),(80,400))
            if event.type == pygame.KEYUP and spa == "down":
                if event.key == pygame.K_SPACE:
                    talk =0 
                    menupause = False
                    spa = "up"                
        if talk == -1:
            skj.blit(undertalefont3.render("Du jetter unna",False,(255,255,255)),(80,350))
            if event.type == pygame.KEYUP and spa == "down":
                if event.key == pygame.K_SPACE:
                    is_roaming = True
                    is_combatmenu = False                        
                    talk = 0
                    menupause = False
                    spa = "up"          
    if enemy == "foxtrotkids":
        combat_timer = 600
        if talk == 0:
            if menu_element == 0:
                if triedtorunlikeabitch == False:
                    if turn == 0:
                        skj.blit(undertalefont3.render("En gjeng med foxtrot unger står",False,(255,255,255)),(80,350))
                        skj.blit(undertalefont3.render('foran deg',False,(255,255,255)),(80,400))
                    else:
                        skj.blit(undertalefont3.render("(Dette er ikke en spøk lenger, jeg",False,(255,255,255)),(80,350))
                        skj.blit(undertalefont3.render("vet ikke hva faen de sier)",False,(255,255,255)),(80,400))
                else:
                    skj.blit(undertalefont3.render('Gjengen står i en sirkel rundt deg.',False,(255,255,255)),(80,350))
                    skj.blit(undertalefont3.render('Du kommer deg ikke unna.',False,(255,255,255)),(80,400))
            if menu_element == 2:
                if menu_select ==1:
                    skj.blit(undertalefont3.render("* tilbake",False,(undertaleyellow)),(80,350))
                else:
                    skj.blit(undertalefont3.render("tilbake",False,(255,255,255)),(80,350))
                if menu_select ==2:
                    skj.blit(undertalefont3.render("* Prøv å snakke svensk",False,(undertaleyellow)),(380,350))
                else:
                    skj.blit(undertalefont3.render("Prøv å snakke svensk",False,(255,255,255)),(380,350))

        if talk == 1:
            skj.blit(undertalefont3.render("Du gjør et ærlig forsøk på å",False,(255,255,255)),(80,350))
            skj.blit(undertalefont3.render("snakke svensk.",False,(255,255,255)),(80,400))
            if event.type == pygame.KEYUP and spa == "down":
                if event.key == pygame.K_SPACE:
                    talk = 2
                    spa = "up"
        if talk == 2:
            skj.blit(undertalefont3.render("De begynner å le av deg.",False,(255,255,255)),(80,350))
            skj.blit(undertalefont3.render("Du vet ikke hvorfor..",False,(255,255,255)),(80,400))
            if event.type == pygame.KEYUP and spa == "down":
                if event.key == pygame.K_SPACE:
                    talk =0 
                    menupause = False
                    spa = "up"                
    if enemy == "foxtrotguy": 
        combat_timer = 600
        if talk == 0:
            if menu_element == 0:
                if triedtorunlikeabitch == False:
                    if turn == 0:
                        skj.blit(undertalefont3.render("En foxtrot leder står foran deg..",False,(255,255,255)),(80,350))
                        skj.blit(undertalefont3.render('med en pistol',False,(255,255,255)),(80,400))
                    else:
                        skj.blit(undertalefont3.render("Han lader om pistolen sin og",False,(255,255,255)),(80,350))
                        skj.blit(undertalefont3.render("ser stygt på deg.",False,(255,255,255)),(80,400))
                else:
                    skj.blit(undertalefont3.render('Han har en pistol..',False,(255,255,255)),(80,350))
                    skj.blit(undertalefont3.render('Å løpe unna hadde vært dumt.',False,(255,255,255)),(80,400))
            if menu_element == 2:
                skj.blit(undertalefont3.render("Denne fyren har ingen planer",False,(255,255,255)),(80,350))
                skj.blit(undertalefont3.render("om å høre på deg yappe",False,(255,255,255)),(80,400))
                if menu_select ==1:
                    skj.blit(undertalefont3.render("* tilbake",False,(undertaleyellow)),(80,450))
                else:
                    skj.blit(undertalefont3.render("tilbake",False,(255,255,255)),(80,450))
    if enemy == "jonna":
        combat_timer = 900
        if talk == 0:
            if menu_element ==0:
                if triedtorunlikeabitch == False:
                    if enemyHP>50:
                        if turn == 0:
                            skj.blit(undertalefont3.render("Jonna står foran deg",False,(255,255,255)),(80,350))
                            skj.blit(undertalefont3.render("Han er uten sin BMW her nede",False,(255,255,255)),(80,400))
                        else:
                            skj.blit(undertalefont3.render("Jonna lader geværene, og gjør",False,(255,255,255)),(80,350))
                            skj.blit(undertalefont3.render("seg klar til å gætte deg rett ned",False,(255,255,255)),(80,400))
                    else:
                        skj.blit(undertalefont3.render("Jonna er irritert på at du ikke dør",False,(255,255,255)),(80,350))
                        skj.blit(undertalefont3.render("Forbered deg for det verste..",False,(255,255,255)),(80,400))
                else:
                    skj.blit(undertalefont3.render("Du kan ikke løpe fra Jonna..",False,(255,255,255)),(80,350))
                    skj.blit(undertalefont3.render("Du sitter fast i kjelleren hans",False,(255,255,255)),(80,400))
            if menu_element ==2:
                if menu_select ==1:
                    skj.blit(undertalefont3.render("  * tilbake",False,(undertaleyellow)),(80,350))
                else:
                    skj.blit(undertalefont3.render("  tilbake",False,(255,255,255)),(80,350))
                if menu_select ==2:
                    skj.blit(undertalefont3.render("* Gaslight",False,(undertaleyellow)),(480,350))
                else:
                    skj.blit(undertalefont3.render("Gaslight",False,(255,255,255)),(480,350))
        if talk == 1:
            skj.blit(undertalefont3.render("Du prøver å overbevise Jonna om at",False,(255,255,255)),(80,350))
            skj.blit(undertalefont3.render("Fallout musikk er overrated",False,(255,255,255)),(80,400))
            if event.type == pygame.KEYUP and spa == "down":
                if event.key == pygame.K_SPACE:
                    talk = 2
                    spa = "up"
        if talk == 2:
            skj.blit(undertalefont3.render("Han tramper mot bakken og roper",False,(255,255,255)),(80,350))
            skj.blit(undertalefont3.render("(kanskje du gikk litt for langt)",False,(255,255,255)),(80,400))
            talkbubble(600,50,250,150,1,"NEI NEI NEI NEI NEI!","NEI NEI NEI NEI NEI!","NEI NEI NEI!")
            if event.type == pygame.KEYUP and spa == "down":
                if event.key == pygame.K_SPACE:
                    talk =0 
                    menupause = False
                    spa = "up"      

def checking_inventory():
    global inventory,menu_select,menu_element,HP,HPmax,is_combat,is_combatmenu,triedtorunlikeabitch,menupause,spa
    if len(inventory)==0:
        skj.blit(undertalefont3.render("Du har ingenting å røyke :c",False,(255,255,255)),(80,350))
        if menu_select ==1:skj.blit(undertalefont3.render("  * tilbake",False,(undertaleyellow)),(80,400))
        else:skj.blit(undertalefont3.render("  tilbake",False,(255,255,255)),(80,400))
    else:
        if menu_select ==1:
            skj.blit(undertalefont3.render("  * tilbake",False,(undertaleyellow)),(80,350))
        else: skj.blit(undertalefont3.render("  tilbake",False,(255,255,255)),(80,350))
        if menu_select ==2:
            skj.blit(undertalefont3.render(str("  * "+str(inventory[0])),False,(undertaleyellow)),(500,350))
        else:skj.blit(undertalefont3.render(str("  "+str(inventory[0])),False,(255,255,255)),(500,350))  
        if len(inventory)>1:
            if menu_select ==3:
                skj.blit(undertalefont3.render(str("  * "+str(inventory[1])),False,(undertaleyellow)),(180,400))
            else: skj.blit(undertalefont3.render(str("  "+str(inventory[1])),False,(255,255,255)),(180,400))
        if len(inventory)>2:
            if menu_select ==4:
                skj.blit(undertalefont3.render(str("  * "+str(inventory[2])),False,(undertaleyellow)),(500,400))
            else: skj.blit(undertalefont3.render(str("  "+str(inventory[2])),False,(255,255,255)),(500,400))
        if len(inventory)>3:
            if menu_select ==5:
                skj.blit(undertalefont3.render(str("  * "+str(inventory[3])),False,(undertaleyellow)),(180,450))
            else: skj.blit(undertalefont3.render(str("  "+str(inventory[3])),False,(255,255,255)),(180,450))
        if len(inventory)>4:
            if menu_select ==6:
                skj.blit(undertalefont3.render(str("  * "+str(inventory[4])),False,(undertaleyellow)),(500,450))
            else: skj.blit(undertalefont3.render(str("  "+str(inventory[4])),False,(255,255,255)),(500,450))
        if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
            if menu_select!=1:
                is_combat = True
                is_combatmenu = False
                triedtorunlikeabitch = False
                menupause = False
                if inventory[menu_select-2]=="Vape":HP+=5
                if inventory[menu_select-2]=="Joint":HP+=15
                if inventory[menu_select-2]=="Keef":HP+=30
                if inventory[menu_select-2]=="Svart Afghan":HP+=100
                if HP > HPmax:HP =HPmax
                inventory.pop(menu_select-2)
            spa = "up"
def walldraw(x1,x2,y,coll):
    i = 0
    pygame.draw.rect(skj,(coll),((x1),y+20,25,20),3)
    while (x1+(i*50))<x2:
        if (x1+(i*50))+50>x2: pygame.draw.rect(skj,(coll),((x1+(i*50)),y,50-((x1+(i*50)+50)-x2),20),3)
        else: pygame.draw.rect(skj,(coll),((x1+(i*50)),y,50,20),3)
        if (x1+(i*50))+50>x2: pygame.draw.rect(skj,(coll),((x1+(i*50)),y+40,50-((x1+(i*50)+50)-x2),20),3)
        else: pygame.draw.rect(skj,(coll),((x1+(i*50)),y+40,50,20),3)
        if (x1+(i*50))+75>x2: pygame.draw.rect(skj,(coll),((x1+(i*50))+25,y+20,50-((x1+(i*50)+75)-x2),20),3)
        else:pygame.draw.rect(skj,(coll),((x1+(i*50))+25,y+20,50,20),3)
        i+=1
def rooms():
    global room,px,py,collision_col,encountered_09,mujani,talk,talkstun,encanim,enemy,HP,HPmax,enemyHP,enemyHPmax,turn,hasbunkerkey,triedtorunlikeabitch,is_outro,is_roaming,star,star1
    global tradermenu,menu_element,menu_select,enc_muj,inventory,spa,encounter_cooldown,jonna_ani,jonna_x,jonna_y,event,enc_gang,enc_boss,lvl,lightswitch,enc_jonna,savemenu,staranim,star2
    collision_col=(undertalepurple)
    if room==9 or room==10 or room==11 or room==12:collision_col=(100,100,100)
    if room == 1:
        #room = 3 #testing
        #px = 300-(psize+20)  #testing
        #py = 340    #testing
        #lvl = 15
        #inventory = ["Vape","Joint","Keef"] #testing
        #enc_muj = True #Testing
        #enc_gang = True #Testing
        #enc_boss = True #Testing
        #enc_jonna = True
        #jonna_ani = -1 # testing
        #hasbunkerkey = True #testing
        pygame.draw.rect(skj,(undertalelightpurple),(100,190,800,310))
        pygame.draw.rect(skj,collision_col, (100,190,800,310),20)
        pygame.draw.rect(skj,(undertalelightpurple),(300,500,400,200))
        pygame.draw.rect(skj,collision_col,(300,500,400,200),20)
        pygame.draw.rect(skj,(undertalelightpurple),(320,450,360,250))
        pygame.draw.rect(skj,(150,150,150),(100,50,800,150))
        pygame.draw.rect(skj,(200,200,200),(100,0,800,50))
        pygame.draw.rect(skj,(180,180,180),(200,70,610,130))
        pygame.draw.rect(skj,(200,200,200),(475,50,50,150))
        pygame.draw.rect(skj,(50,50,50),(420,80,50,100))
        pygame.draw.rect(skj,(50,50,50),(280,80,115,110))
        pygame.draw.rect(skj,(50,50,50),(205,80,50,100))
        pygame.draw.rect(skj,(50,50,50),(755,80,50,100))
        pygame.draw.rect(skj,(50,50,50),(615,80,115,110))
        pygame.draw.rect(skj,(50,50,50),(530,80,50,100))
        pygame.draw.rect(skj,(10,10,10),(420,5,160,35))
        pygame.draw.rect(skj,(150,0,0),(455,5,35,35))
        pygame.draw.circle(skj,(255,255,255),(472,22),13)
        pygame.draw.circle(skj,(150,0,0),(472,22),11)
        skj.blit(undertalefont7.render("#",False,(255,255,255)),(425,-4))
        skj.blit(undertalefont4.render("T",False,(255,255,255)),(465,6))
        skj.blit(undertalefont4.render("Stovner",False,(255,255,255)),(490,6))
        skj.blit(star,star.get_rect(topleft=(618,318)))
        staranim+=1
        if staranim>60:
            staranim=0
            if star==star1:star=star2
            else:star=star1
        if px>600 and px<700 and py>300 and py<400:
            if spa =="down" and pygame.key.get_pressed()[pygame.K_SPACE] and savemenu == False:
                savemenu = True
                talkstun = True
                menu_select= 0
        if py<280 and talk ==0 and spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
            talk = 22
            talkstun = True
            spa = "up"
        if py >700-(psize-20):
            room = 2
            py = (psize+10)
            if px <460:px = 460
            if px >540:px =540
    if room == 2:
        pygame.draw.rect(skj,(undertalelightpurple),(0,0,1000,700))
        pygame.draw.rect(skj,(collision_col),(0,0,1000,700),20)
        pygame.draw.rect(skj,(undertalelightpurple),(425,0,150,50))
        walldraw(20,425,20,collision_col)
        walldraw(575,980,20,collision_col)
        if mujani ==-1:
            pygame.draw.rect(skj,undertalelightpurple,(0,250,50,200))
            if px < 0+(psize-20):
                room = 3
                encountered_09 = False
                px = 1000-(psize+20)
                if py <305:py = 305
                if py >385:py = 385
        if not mujani ==-1:
            if mujani == 1:
                #pygame.draw.rect(skj,(0,0,0),(mujanim-30,240,160,160))   #hitbox 
                skj.blit(muj2,muj2.get_rect(topleft = (mujanim+10-25,270-25)))
            else:
                #pygame.draw.rect(skj,(0,0,0),(630,240,160,160))     #hitbox
                skj.blit(muj2,muj2.get_rect(topleft = (660-25,270-25)))
            if px >630 and px<790 and py >240 and py<400 and talk == 0 and mujani ==0:
                if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                    talk = 4
                    talkstun = True
                    spa = "up"
        if py < 0+(psize-20):
            room = 1
            py = 700-(psize+20)   
    if room == 3:
        pygame.draw.rect(skj,(undertalelightpurple),(0,190,1000,260))
        pygame.draw.rect(skj,(collision_col),(-20,190,1040,260),20)
        pygame.draw.rect(skj,undertalelightpurple,(0,270,1000,160))
        walldraw(0,1000,210,(collision_col))
        if px > 1000-(psize-20):
            room = 2
            px = (psize+20)
        if px < 0+(psize-20):
                room = 4
                encountered_09=False
                encounter_cooldown = 300
                px = 1000-(psize+20)   
        if encountered_09 == False and px>400 and px<450:
            encountered_09 = True
            talkstun = True
            encanim = 1
            enemy = "09"
            HPmax = 20+(lvl*2)
            HP = HPmax
            enemyHP = 10
            enemyHPmax = 10
            turn = 0
    if room == 4:
        pygame.draw.rect(skj,(undertalelightpurple),(0,0,800,550))
        pygame.draw.rect(skj,(undertalelightpurple),(250,140,800,560))
        pygame.draw.rect(skj,(collision_col),(0,0,250,550),20)  
        pygame.draw.rect(skj,(collision_col),(250,0,350,700),20)  
        pygame.draw.rect(skj,(collision_col),(600,0,200,700),20)  
        pygame.draw.rect(skj,(collision_col),(800,140,200,560),20)  
        pygame.draw.rect(skj,(collision_col),(270,550,325,20))  
        pygame.draw.rect(skj,undertalelightpurple,(950,250,50,200))
        pygame.draw.rect(skj,undertalelightpurple,(50,0,150,50))
        pygame.draw.rect(skj,undertalelightpurple,(775,465,50,215))
        pygame.draw.rect(skj,undertalelightpurple,(575,20,50,205))
        pygame.draw.rect(skj,undertalelightpurple,(225,315,50,215))
        walldraw(20,50,20,collision_col)
        walldraw(200,230,20,collision_col)
        walldraw(230,270,315,collision_col)
        walldraw(270,780,20,collision_col)
        walldraw(820,980,160,collision_col)
        walldraw(780,820,465,collision_col)
        if encounter_cooldown >0: encounter_cooldown-=1
        skj.blit(pat,pat.get_rect(topleft = (400,560)))
        if enc_gang ==True:skj.blit(elsparkesykkel,elsparkesykkel.get_rect(topleft = (50,400)))
        skj.blit(star,star.get_rect(topleft=(518,418)))
        staranim+=1
        if staranim>60:
            staranim=0
            if star==star1:star=star2
            else:star=star1
        if px>500 and px<600 and py>400 and py<500:
            if spa =="down" and pygame.key.get_pressed()[pygame.K_SPACE] and savemenu == False:
                savemenu = True
                talkstun = True
                menu_select= 0
        if px>20 and px<220 and py>380 and py<520 and talk == 0:
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                if enc_gang == True:
                    talk = 21
                    menu_select = 0
                    talkstun = True
                spa = "up"
        if px > 1000-(psize-20):
            room = 3
            px = (psize+20)  
            encountered_09 = False
            if py <305:py = 305
            if py >385:py = 385    
        if py < 0+(psize-20):  
            room = 5
            py = 700-(psize+20)
            px +=670
        if ismoving == True and px>600 and px<800 or ismoving == True and py>20 and py<375 and px<800:   
            if randint(1,240) ==1 and encounter_cooldown<=0:
                if randint(1,2) ==1:
                    talkstun = True
                    encanim = 1
                    enemy = "09"
                    HPmax = 20+(lvl*2)
                    HP = HPmax
                    enemyHP = 10
                    enemyHPmax = 10
                    turn = 0
                else:
                    talkstun = True
                    encanim = 1
                    enemy = "stovnerjenter"
                    HPmax = 20+(lvl*2)
                    HP = HPmax
                    enemyHP = 15
                    enemyHPmax = 15
                    turn = 0                        
        if py>510 and px>270 and px<600 and tradermenu == False:
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                menu_element = 0
                menu_select = 0
                tradermenu = True
                spa ="up"
    if room == 5:
        pygame.draw.rect(skj,(undertalelightpurple),(600,0,400,700))
        pygame.draw.rect(skj,(50,50,50),(200,0,400,700))
        for i in range(10):pygame.draw.rect(skj,(undertaleyellow),(400,80*i,10,40))
        pygame.draw.rect(skj,(collision_col),(200,0,800,700),20)
        pygame.draw.rect(skj,(undertalelightpurple),(700,650,200,500))
        skj.blit(star,star.get_rect(topleft=(918,318)))
        staranim+=1
        if staranim>60:
            staranim=0
            if star==star1:star=star2
            else:star=star1
        if px>900 and px<1000 and py>300 and py<400:
            if spa =="down" and pygame.key.get_pressed()[pygame.K_SPACE] and savemenu == False:
                savemenu = True
                talkstun = True
                menu_select= 0
        if enc_muj == True and (jonna_ani>1 or jonna_ani==-1):
            pygame.draw.rect(skj,(undertalelightpurple),(700,0,200,20))
        if enc_muj == False:
            skj.blit(muj2,muj2.get_rect(topleft = (500,80)))
        if jonna_ani!=4:
            if jonna_ani!=-1:
                skj.blit(mujaffabil,mujaffabil.get_rect(topleft = (400,160)))
        else:
            skj.blit(mujaffabil,mujaffabil.get_rect(topleft = (jonna_x,jonna_y)))
            jonna_y-=0.1*(161-(jonna_y))      
            if jonna_y<-100:
                jonna_ani =-1
        if enc_muj == True and jonna_ani==0 and levelupscreen == False: 
            talk = 6
            talkstun = True
            jonna_ani = 1
            px = 750
            py = 330
        if jonna_ani==2:
            skj.blit(jonna,jonna.get_rect(topleft = (jonna_x,jonna_y)))
            jonna_x+=4*math.cos(math.atan2(700-550,0-160))
            jonna_y+=4*math.sin(math.atan2(700-550,0-160))
            if jonna_x <500:
                talk = 7
                jonna_ani=3
        if jonna_ani==3:
            skj.blit(jonna,jonna.get_rect(topleft = (jonna_x,jonna_y)))
        if py > 700-(psize-20): 
            room = 4
            encounter_cooldown = 300
            py = psize+20
            px -= 670
            if px<84:px=84 #50 200
            if px>166:px=166 #+34 -34
        if py < 0+(psize-20): 
            room = 6
            py = 700-(psize+20)
            px -= 300
            if px<434:px=434 
            if px>566:px=566 #+34 -34
        #pygame.draw.rect(skj,(0,0,0),(400,80,300,200))  #Hitbox
        if px >400 and px<700 and py >80 and py<280 and talk == 0 and enc_muj == False: 
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 1
                talkstun = True
                spa = "up"
    if room ==6:
        pygame.draw.rect(skj,(undertalelightpurple),(0,40,1000,360))        
        pygame.draw.rect(skj,(collision_col),(-20,40,1040,360),20)
        walldraw(0,1000,60,collision_col)
        pygame.draw.rect(skj,(undertalelightpurple),(380,400,240,400))     
        pygame.draw.rect(skj,(collision_col),(380,400,240,420),20)
        pygame.draw.rect(skj,(undertalelightpurple),(400,380,200,40)) 
        pygame.draw.rect(skj,(100,30,80),(490,50,20,120))           
        pygame.draw.polygon(skj,(undertalepurple),[(455,55),(495,55),(495,75),(455,75),(440,65)])           
        pygame.draw.polygon(skj,(undertalepurple),[(540,75),(510,75),(510,95),(540,95),(555,85)])         
        
        if px>400 and px<580 and py<230:
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE] and talk == 0:  
                talkstun = True
                talk = 9
                spa = "up"              
        if py > 700-(psize-20): 
            room = 5
            py = 0+(psize+20)
            px += 300     
        if px < 0+(psize-20):
                room = 7
                px = 1000-(psize+20) 
                py+=300
        if px > 1000-(psize-20):
                room = 8
                px = 0+(psize+20) 
                py+=300
        if encounter_cooldown >0: encounter_cooldown-=1
        if ismoving == True and px>50 and px<950 and py<650:   
            if randint(1,240) ==1 and encounter_cooldown<=0:
                if randint(1,2) ==1:
                    talkstun = True
                    encanim = 1
                    enemy = "09"
                    HPmax = 20+(lvl*2)
                    HP = HPmax
                    enemyHP = 10
                    enemyHPmax = 10
                    turn = 0
                else:
                    talkstun = True
                    encanim = 1
                    enemy = "stovnerjenter"
                    HPmax = 20+(lvl*2)
                    HP = HPmax
                    enemyHP = 15
                    enemyHPmax = 15
                    turn = 0      
    if room ==7:
        pygame.draw.rect(skj,(undertalelightpurple),(0,0,1000,700))        
        pygame.draw.rect(skj,(collision_col),(0,0,1000,700),20)  
        pygame.draw.rect(skj,(undertalelightpurple),(980,420,20,260))
        pygame.draw.circle(skj,(100,100,100),(860,350,),100) 
        pygame.draw.circle(skj,(150,150,150),(860,350,),85)
        pygame.draw.rect(skj,(100,100,100),(770,345,180,10)) 
        pygame.draw.rect(skj,(100,100,100),(855,260,10,180)) 
        pygame.draw.circle(skj,(100,100,100),(860,350,),25)
        pygame.draw.rect(skj,(collision_col),(400,0,40,500))
        pygame.draw.rect(skj,(collision_col),(20,475,400,20))
        pygame.draw.rect(skj,(collision_col),(20,275,400,20))
        pygame.draw.line(skj,(collision_col),(420,300),(500,185),20)
        pygame.draw.rect(skj,(collision_col),(490,20,20,270))
        for i in range(10): pygame.draw.rect(skj,(collision_col),(450+i*7,490-i*30,100,10))
        pygame.draw.line(skj,(collision_col),(450,500),(520,200),20)
        pygame.draw.line(skj,(collision_col),(550,500),(620,200),20)
        pygame.draw.line(skj,(collision_col),(700,500),(770,200),20)
        pygame.draw.rect(skj,(collision_col),(490,190,490,20))
        pygame.draw.rect(skj,(undertaleyellow),(20,20,380,254))
        pygame.draw.rect(skj,(undertaleyellow),(440,20,49,170))
        pygame.draw.polygon(skj,(undertaleyellow),[(440,190),(488,190),(440,260)])

        pygame.draw.rect(skj,(undertalelightpurple),(140,100,200,100))
        pygame.draw.rect(skj,(collision_col),(140,100,200,100),10)
        pygame.draw.rect(skj,(50,50,50),(50,300,300,180))
        for i in range(17): pygame.draw.rect(skj,(150,150,150),(60,310+i*10,280,5))
        skj.blit(mujaffabil,mujaffabil.get_rect(topleft = (50,500)))

        if px > 1000-(psize-20):
                room = 6
                px = 0+(psize+20) 
                py+=-300    
                if py<154:py=154 #120 380
                if py>346:py=346 #+34 -34
        if px>720 and px<980 and py<460:
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE] and talk == 0:  
                if hasbunkerkey == False:
                    talkstun = True
                    talk = 10
                if hasbunkerkey == True:
                    px = 700
                    py = 500
                    room = 12
                spa = "up"
        if px<300 and py>400:
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE] and talk == 0:  
                if enc_jonna == False:
                    talkstun = True
                    talk = 11
                if enc_jonna == True:
                    talk =26
                    talkstun = True
                    menu_select = 1
                spa = "up"
    if room ==8:
        pygame.draw.rect(skj,(undertalelightpurple),(0,0,1000,700))        
        pygame.draw.rect(skj,(collision_col),(0,0,1000,700),20)  
        pygame.draw.rect(skj,(undertalelightpurple),(0,420,20,260))
        pygame.draw.rect(skj,(50,50,50),(200,420,780,260))
        for i in range(8):pygame.draw.rect(skj,(undertaleyellow),(360+80*i,550,40,10))
        for i in range(2):pygame.draw.rect(skj,(undertaleyellow),(360,550+80*i,10,40))
        pygame.draw.rect(skj,(collision_col),(0,250,270,20))     
        pygame.draw.rect(skj,(collision_col),(450,250,550,20))     
        pygame.draw.rect(skj,(collision_col),(450,0,20,250))
        pygame.draw.rect(skj,(collision_col),(250,0,20,250))
        pygame.draw.line(skj,(collision_col),(260,269),(330,109),20)
        pygame.draw.line(skj,(collision_col),(330,109),(450,112),5)
        pygame.draw.rect(skj,(collision_col),(321,20,20,90))
        pygame.draw.rect(skj,(collision_col),(50,50,150,100),10)
        pygame.draw.rect(skj,(collision_col),(700,100,120,150),10)  
        pygame.draw.rect(skj,(collision_col),(800,100,120,150),10)
        pygame.draw.rect(skj,(255,255,255),(650,30,320,50))
        skj.blit(undertalefont5.render("K",False,(0,0,0)),(719,38))
        skj.blit(undertalefont5.render("I",False,(0,0,0)),(748,38))
        skj.blit(undertalefont5.render("W",False,(0,0,0)),(778,38))
        skj.blit(undertalefont5.render("I",False,(0,0,0)),(810,38))
        skj.blit(undertalefont2.render("KIWI",False,(0,255,0)),(720,40))
        skj.blit(undertalefont6.render("MINI",False,(0,0,0)),(850,40))
        skj.blit(undertalefont6.render("PRIS",False,(0,0,0)),(850,55))
        if enc_gang==False:skj.blit(foxtrotkids2,foxtrotkids2.get_rect(topleft = (670,120)))
        skj.blit(star,star.get_rect(topleft=(68,268)))
        staranim+=1
        if staranim>60:
            staranim=0
            if star==star1:star=star2
            else:star=star1
        if px>50 and px<150 and py>250 and py<350:
            if spa =="down" and pygame.key.get_pressed()[pygame.K_SPACE] and savemenu == False:
                savemenu = True
                talkstun = True
                menu_select= 0
        if px>650 and px<980 and py<425 and talk == 0 and enc_gang==False:
            talk = 12
            talkstun = True
        if enc_gang ==False:skj.blit(pat,pat.get_rect(topleft = (370,90)))
        if enc_gang ==True:skj.blit(elsparkesykkel,elsparkesykkel.get_rect(topleft = (350,90)))
        if px>250 and px<450 and py<250 and talk == 0:
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                if enc_gang == False:
                    talk = 13
                    talkstun = True
                if enc_gang == True:
                    talk = 21
                    menu_select = 0
                    talkstun = True
                spa = "up"
        if enc_gang==True and px>700 and px<920 and py<310:
            room = 9
            px = 500
            py = 700-(psize+20)
        if px < 0+(psize-20):
                room = 6
                px = 1000-(psize+20) 
                py-=300
                if py<154:py=154 #120 380
                if py>346:py=346 #+34 -34
    if room ==9:
        pygame.draw.rect(skj,(200,200,200),(0,-20,1000,720))
        for j in range(10):
            for i in range(10):
                pygame.draw.rect(skj,(180,180,180),(20+i*100,-20+j*100,100,100),5)
        pygame.draw.rect(skj,collision_col, (0,-20,1000,720),20)
        pygame.draw.rect(skj,(200,200,200),(400,680,200,20))
        pygame.draw.rect(skj,(collision_col),(800,250,100,300),0,10)
        pygame.draw.polygon(skj,(collision_col),[(890,549),(960,549),(890,400)])
        pygame.draw.rect(skj,(collision_col),(550,250,100,300),0,10)
        pygame.draw.polygon(skj,(collision_col),[(570,549),(500,549),(570,400)])
        pygame.draw.rect(skj,(collision_col),(350,250,100,300),0,10)
        pygame.draw.polygon(skj,(collision_col),[(430,549),(500,549),(430,400)])
        pygame.draw.rect(skj,(50,255,50),(850,255,45,100),0,1)
        pygame.draw.rect(skj,(50,50,50),(805,255,40,200),0,5)
        pygame.draw.polygon(skj,(50,50,50),[(805,510),(920,510),(805,350)])
        for i in range(31): pygame.draw.line(skj,(70,70,70),(808,255+i*5),(842,255+i*5),3)
        for i in range(20): pygame.draw.line(skj,(70,70,70),(808,410+i*5),(int(842+i*3.5),410+i*5),3)
        pygame.draw.rect(skj,(150,150,150),(802,370,50,50),0,10)
        pygame.draw.rect(skj,(50,50,50),(827,370,20,50),0,1)
        pygame.draw.rect(skj,(50,255,50),(400,255,45,100),0,1)
        pygame.draw.rect(skj,(50,50,50),(355,255,40,200),0,5)
        pygame.draw.polygon(skj,(50,50,50),[(355,510),(470,510),(355,350)])
        for i in range(31): pygame.draw.line(skj,(70,70,70),(358,255+i*5),(392,255+i*5),3)
        for i in range(20): pygame.draw.line(skj,(70,70,70),(358,410+i*5),(int(392+i*3.5),410+i*5),3)
        pygame.draw.rect(skj,(150,150,150),(352,370,50,50),0,10)
        pygame.draw.rect(skj,(50,50,50),(377,370,20,50),0,1)
        pygame.draw.rect(skj,(50,255,50),(555,255,45,100),0,1)
        pygame.draw.rect(skj,(50,50,50),(606,255,40,200),0,5)
        pygame.draw.polygon(skj,(50,50,50),[(645,510),(530,510),(645,350)])
        for i in range(31): pygame.draw.line(skj,(70,70,70),(608,255+i*5),(642,255+i*5),3)
        for i in range(20): pygame.draw.line(skj,(70,70,70),(int(608-i*3.8),410+i*5),(642,410+i*5),3)
        pygame.draw.rect(skj,(150,150,150),(598,370,50,50),0,10)
        pygame.draw.rect(skj,(50,50,50),(603,370,20,50),0,1)
        pygame.draw.line(skj,(collision_col),(900,250),(1000,230),8)
        pygame.draw.line(skj,(collision_col),(350,250),(649,250),20)
        pygame.draw.rect(skj,(collision_col),(50,300,100,100),0,10)
        pygame.draw.rect(skj,(50,255,50),(55,305,90,90),0,10)
        pygame.draw.rect(skj,(collision_col),(50,420,100,100),0,10)
        pygame.draw.rect(skj,(50,255,50),(55,425,90,90),0,10)
        pygame.draw.rect(skj,(collision_col),(950,0,50,120))
        pygame.draw.rect(skj,(50,255,50),(955,0,45,115))
        pygame.draw.line(skj,(50,50,50),(975,0),(975,116),3)
        for i in range(3):
            pygame.draw.rect(skj,(collision_col),(300+i*200,0,75,120))
            pygame.draw.rect(skj,(50,255,50),(5+300+i*200,0,65,115))
            pygame.draw.line(skj,(50,50,50),(337+i*200,0),(337+i*200,110),3)            
        pygame.draw.rect(skj,(collision_col),(0,0,50,120))
        pygame.draw.rect(skj,(50,255,50),(0,0,45,115))
        pygame.draw.line(skj,(50,50,50),(25,0),(25,116),3)
        skj.blit(star,star.get_rect(topleft=(118,568)))
        staranim+=1
        if staranim>60:
            staranim=0
            if star==star1:star=star2
            else:star=star1
        if px>100 and px<200 and py>550 and py<650:
            if spa =="down" and pygame.key.get_pressed()[pygame.K_SPACE] and savemenu == False:
                savemenu = True
                talkstun = True
                menu_select= 0
        if encounter_cooldown >0: encounter_cooldown-=1
        if enc_boss==False:
            if ismoving == True and py<500:   
                if randint(1,360) ==1 and encounter_cooldown<=0:
                    encanim = 1
                    enemy = "foxtrotkids"
                    HPmax = 20+(lvl*2)
                    HP = HPmax
                    enemyHP = 30
                    enemyHPmax = 30
                    turn = 0    
                    talk = 0            
                    talkstun = True
                    triedtorunlikeabitch = False
        if enc_boss ==True:
            skj.blit(pat,pat.get_rect(topleft=(490,300)))
            if px>400 and px<700 and py>350 and py<500 and tradermenu == False:
                if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                    tradermenu = True
                    menu_element = 0
                    menu_select = 0
                    spa = "up"
        if px>400 and px<600 and py>700-(psize-20):
            room = 8
            px = 800
            py = 340
        if py<0+(psize-20):
            room = 10
            py=700-(psize+20)
    if room==10:
        pygame.draw.rect(skj,(200,200,200),(0,0,1000,720))
        for j in range(10):
            for i in range(10):
                pygame.draw.rect(skj,(180,180,180),(20+i*100,20+j*100,100,100),5)
        pygame.draw.rect(skj,collision_col, (0,0,1000,720),20)
        pygame.draw.rect(skj,(collision_col),(950,0,50,700))
        pygame.draw.rect(skj,(50,255,50),(955,0,45,700))
        pygame.draw.line(skj,(50,50,50),(975,28),(975,700),3)
        for i in range(3):
            pygame.draw.rect(skj,(collision_col),(300+i*200,400,75,300))
            pygame.draw.rect(skj,(50,255,50),(5+300+i*200,405,65,300))
            pygame.draw.line(skj,(50,50,50),(337+i*200,400),(337+i*200,700),3)        
        pygame.draw.rect(skj,(collision_col),(0,0,50,700))
        pygame.draw.rect(skj,(50,255,50),(0,0,45,700))
        pygame.draw.line(skj,(50,50,50),(25,28),(25,700),3)
        pygame.draw.rect(skj,(collision_col),(0,0,375,50))
        pygame.draw.line(skj,(50,50,50),(28,13),(350,13),3)
        pygame.draw.rect(skj,(collision_col),(650,0,350,50))
        pygame.draw.line(skj,(50,50,50),(654,13),(976,13),3)
        pygame.draw.rect(skj,(collision_col),(150,150,650,150),0,5)
        pygame.draw.rect(skj,(200,200,200),(153,153,644,144),0,5)
        pygame.draw.rect(skj,(150,150,150),(170,160,610,50))
        pygame.draw.rect(skj,(150,150,150),(170,240,610,50))
        for i in range(5):
            pygame.draw.line(skj,(collision_col),(170+i*122,160),(170+i*122,208),4)
            pygame.draw.line(skj,(collision_col),(170+i*122,240),(170+i*122,288),4)
        pygame.draw.rect(skj,(200,200,200),(530,0,100,20))
        if enc_boss==False:
            pygame.draw.line(skj,(collision_col),(530,5),(630,5),5)
            skj.blit(foxtrotguy,foxtrotguy.get_rect(topleft = (545,5)))
        else:
            pygame.draw.line(skj,(99,99,99),(645,90),(630,5),5)
        if encounter_cooldown >0: encounter_cooldown-=1
        if enc_boss==False:
            if ismoving == True:   
                if randint(1,360) ==1 and encounter_cooldown<=0:
                    encanim = 1
                    enemy = "foxtrotkids"
                    HPmax = 20+(lvl*2)
                    HP = HPmax
                    enemyHP = 30
                    enemyHPmax = 30
                    turn = 0    
                    talk = 0            
                    talkstun = True
                    triedtorunlikeabitch = False
        if py>700-(psize-20):
            room = 9
            py=0+(psize+20)
        if py<0+(psize-20) and enc_boss==True:
            room=11
            px-=80
            py=400-(psize+20)
        if px>510 and px<650 and py<200 and talk == 0 and enc_boss ==False:
            talk = 15
            talkstun = True
            spa = "up"
    if room==11:
        pygame.draw.rect(skj,(200,200,200),(-20,0,1020,400))
        for j in range(4):
            for i in range(10):
                pygame.draw.rect(skj,(180,180,180),(20+i*100,-20+j*100,100,100),5)
        pygame.draw.rect(skj,collision_col, (-20,0,1020,400),20)  
        pygame.draw.rect(skj,(200,200,200),(450,380,100,20))
        pygame.draw.rect(skj,(50,50,50),(108,303,254,74))
        pygame.draw.rect(skj,(collision_col),(110,305,250,70))
        pygame.draw.polygon(skj,(75,25,0),[(110,330),(160,315),(180,355),(130,370)])
        pygame.draw.rect(skj,(75,25,0),(200,315,40,55))
        pygame.draw.polygon(skj,(75,25,0),[(258,320),(320,305),(330,355),(270,365)])
        pygame.draw.rect(skj,(50,50,50),(-2,303,94,74))
        pygame.draw.rect(skj,(collision_col),(0,305,90,70))
        pygame.draw.rect(skj,(75,25,0),(0,315,60,50))
        pygame.draw.rect(skj,(50,50,50),(110,50,250,40))
        pygame.draw.rect(skj,(collision_col),(112,52,246,36))
        pygame.draw.line(skj,(collision_col),(110,20),(110,100),8)
        pygame.draw.line(skj,(50,50,50),(110,20),(110,100),7)
        pygame.draw.rect(skj,(75,25,0),(280,40,60,45),0,1)
        pygame.draw.rect(skj,(75,25,0),(200,20,30,65),0,1)
        pygame.draw.rect(skj,(75,25,0),(240,45,45,35),0,1)
        pygame.draw.rect(skj,(75,25,0),(120,40,70,30),0,1)
        pygame.draw.line(skj,(collision_col),(360,20),(360,100),8)
        pygame.draw.line(skj,(50,50,50),(360,20),(360,100),7)
        pygame.draw.rect(skj,(50,50,50),(107,-10,257,40))
        pygame.draw.rect(skj,(collision_col),(109,-9,253,36))
        pygame.draw.rect(skj,(75,25,0),(150,0,40,27))
        pygame.draw.rect(skj,(75,25,0),(270,0,90,25))
        pygame.draw.rect(skj,(50,50,50),(0,50,84,40))
        pygame.draw.rect(skj,(collision_col),(0,52,82,36))
        pygame.draw.rect(skj,(75,25,0),(0,40,70,40),0,1)
        pygame.draw.line(skj,(collision_col),(80,20),(80,100),8)
        pygame.draw.line(skj,(50,50,50),(80,20),(80,100),7)
        pygame.draw.rect(skj,(50,50,50),(0,-10,84,40))
        pygame.draw.rect(skj,(collision_col),(0,-9,82,36))
        pygame.draw.line(skj,(30,30,30),(349,160),(349,40),10)
        pygame.draw.lines(skj,(30,30,30),True,[(330,70),(330,40),(369,40),(369,70),(349,90)],5)
        pygame.draw.polygon(skj,(255,200,0),[(321,160),(350,120),(380,160)])
        pygame.draw.line(skj,(255,200,0),(325,160),(325,260),20)
        pygame.draw.line(skj,(255,200,0),(375,160),(375,260),20)
        pygame.draw.rect(skj,(255,200,0),(366,230,20,40),0,255)
        pygame.draw.rect(skj,(50,50,50),(371,240,10,20),0,255)
        pygame.draw.rect(skj,(255,200,0),(316,230,20,40),0,255)
        pygame.draw.rect(skj,(50,50,50),(321,240,10,20),0,255)
        for i in range(5):
            pygame.draw.rect(skj,(collision_col),(700+i*50,0,50,130))
            pygame.draw.rect(skj,(150,150,150),(704+i*50,4,42,122))
            pygame.draw.rect(skj,(collision_col),(708+i*50,30,34,3))
            pygame.draw.rect(skj,(collision_col),(708+i*50,34,34,3))
            pygame.draw.rect(skj,(collision_col),(708+i*50,38,34,3))
        skj.blit(poster,poster.get_rect(topleft=(908,45)))
        if px>900 and px<960 and py<200:
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE] and hasbunkerkey==False and talk==0: 
                talk = 17
                talkstun = True
                spa = "up"
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE] and hasbunkerkey == True and talk==0:
                talk = 18
                talkstun = True
                spa = "up"
        if px <400:
            talk = 19
            talkstun = True
            px = 400
        if py>400-(psize-20):
            room=10
            px+=80
            py=0+(psize+20)       
    if room==12:
        pygame.draw.rect(skj,(150,150,150),(150,200,700,400))        
        pygame.draw.rect(skj,(collision_col),(150,200,700,400),20)  
        pygame.draw.rect(skj,(20,20,20),(300,0,100,220)) 
        for i in range(20):
            pygame.draw.rect(skj,(100-i*5,100-i*5,100-i*5),(280,0,20,200-i*5)) 
            pygame.draw.rect(skj,(100-i*5,100-i*5,100-i*5),(400,0,20,200-i*5)) 
        pygame.draw.circle(skj,(120,120,120),(700,500),60)
        pygame.draw.line(skj,(200,150,0),(670,500),(670,340),6)
        pygame.draw.line(skj,(200,150,0),(730,500),(730,340),6)
        for i in range(8): pygame.draw.line(skj,(200,150,0),(670,360+i*20),(730,360+i*20),4)
        pygame.draw.rect(skj,(160,120,60),(180,400,100,170))
        pygame.draw.rect(skj,(230,230,230),(184,404,92,162))
        pygame.draw.rect(skj,(160,0,0),(182,462,96,106))
        pygame.draw.rect(skj,(160,160,160),(193,410,75,32))
        skj.blit(shelves,shelves.get_rect(topleft=(640,200)))
        skj.blit(shelves,shelves.get_rect(topleft=(456,200)))
        if py<200 and px<335:px=335
        if py<200 and px>365:px=365
        if px>640 and px<750 and py>450:
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                px = 860
                py = 400
                room = 7
                spa = "up"
        skj.blit(star,star.get_rect(topleft=(188,238)))
        staranim+=1
        if staranim>60:
            staranim=0
            if star==star1:star=star2
            else:star=star1
        if px>170 and px<270 and py>230 and py<330:
            if spa =="down" and pygame.key.get_pressed()[pygame.K_SPACE] and savemenu == False:
                savemenu = True
                talkstun = True
                menu_select= 0
        if py<(psize-20):
            py = 700-(psize+20)
            px = 500
            room = 13
    if room ==13:
        if lightswitch==0:collision_col = (10,10,10)
        else:
            collision_col = (100,100,100)
            pygame.draw.rect(skj,(150,150,150),(0,0,1000,700))    
        pygame.draw.rect(skj,(collision_col),(0,0,1000,700),20)       
        if lightswitch==0 and enc_jonna==False:pygame.draw.rect(skj,(0,0,0),(450,680,100,20)) 
        else:pygame.draw.rect(skj,(150,150,150),(450,680,100,20)) 
        if lightswitch==0 and enc_jonna==False:pygame.draw.line(skj,(150,150,150),(500,400),(500,200),3)
        else:pygame.draw.line(skj,(80,80,80),(500,400),(500,200),3)
        pygame.draw.circle(skj,(200,200,0),(501,400),5)
        if lightswitch>0 and enc_jonna==False:
            skj.blit(jonna,jonna.get_rect(center=(500,100)))
            a = pygame.transform.rotate(ak47,-15)
            skj.blit(a,a.get_rect(topleft=(80,300)))
            d = pygame.transform.rotate(doomshotgun,15)
            skj.blit(d,d.get_rect(topleft=(650,300)))
            skj.blit(tankbody,tankbody.get_rect(topleft=(50,80)))
            skj.blit(tankbody,tankbody.get_rect(topleft=(750,80)))
            t1 = pygame.transform.rotate(tankhead,135)
            t2 = pygame.transform.rotate(tankhead,55)
            skj.blit(t1,t1.get_rect(center=(130,140)))
            skj.blit(t2,t2.get_rect(center=(830,140)))            
        if lightswitch>0 and enc_jonna==False: lightswitch+=1
        if lightswitch>120 and talk == 0 and encanim==0 and enc_jonna==False:
            talk = 23
        if py>400 and py<450 and px>450 and px<550 and talk == 0 and lightswitch==0 and enc_jonna==False:
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                lightswitch = 1
                talkstun = True
                spa = "up"
        if enc_jonna == None:
            talk = 25
            enc_jonna = True
        if py>700-(psize-20):
            py = (psize+20)
            px = 350
            room = 12

def levelup_screen():
    global nextrank,nextranklevel,talkstun,levelupscreen,hideplayer,spa,ismoving
    ismoving = False
    pygame.draw.rect(skj,(0,0,0),(50,200,900,400))
    pygame.draw.rect(skj,(255,255,255),(50,200,900,400),10)
    skj.blit(undertalefont3.render("Du økte i nivå",False,(255,255,255)),(80,300-50))
    pygameisbeingafuckingbitch = (lvl-lvldif)
    skj.blit(undertalefont3.render(str("Fra nivå "+str(pygameisbeingafuckingbitch)+" til nivå "+str(lvl)+" (+"+str(lvldif)+"dmg,+"+str((lvldif*2))+"HP)"),False,(255,255,255)),(80,300+20))
    skj.blit(undertalefont3.render(str("Din rank: "+str(rank)),False,(255,255,255)),(80,300+80))  
    if rank == "Weed Amateur":
        nextrank = "Keef Enjoyer"       
        nextranklevel = 3     
    if rank == "Keef Enjoyer":
        nextrank = "Serious Addict"
        nextranklevel = 10
    if rank == "Serious Addict":
        nextrank = "død.."
        nextranklevel = 10
    skj.blit(undertalefont3.render(str(str(nextrank)+"-rank om "+str((nextranklevel-lvl))+" Nivåer"),False,(255,255,255)),(80,300+140))              
    if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
        talkstun = False
        levelupscreen = False
        hideplayer = False
        spa = "up"  
def startmenu_events():
    global event,spa,menu_element,menu_select
    if not pygame.key.get_pressed()[pygame.K_SPACE]:
        spa = "up"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spa = "down"
            if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_w or event.key == pygame.K_UP:
                menu_select -= 1
                if menu_select<1: menu_select = 2
                if menu_select>2: menu_select = 1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                menu_select += 1
                if menu_select<1: menu_select = 2
                if menu_select>2: menu_select = 1
def intro_events():
    global menu_select,menu_element,event,typing,keyboardlist,playername,is_intro,is_roaming,typing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()     
        if event.type == pygame.KEYUP:
            if menu_element == 1:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    menu_select -= 1
                    if menu_select<1: menu_select +=30
                    if menu_select>30: menu_select -=30
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    menu_select += 1
                    if menu_select<1: menu_select +=30
                    if menu_select>30: menu_select -=30
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    menu_select -= 10
                    if menu_select<1: menu_select +=30
                    if menu_select>30: menu_select -=30
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if menu_select>=21 and menu_select<=30:
                        menu_select = 31
                    else:  
                        menu_select += 10
                        if menu_select<1: menu_select +=30
                        if menu_select>30: menu_select -=30
                if event.key == pygame.K_SPACE:
                    if menu_select !=30 and menu_select !=31:
                        if len(typing)<8:
                            typing+=keyboardlist[menu_select-1]
                    if menu_select ==30:
                        if len(typing)>0:
                            typing = typing[0:-1]
                    if menu_select == 31:
                        if len(typing)>0:
                            menu_element = 2
                            menu_select = 0
            if menu_element ==2:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    menu_select -= 1
                    if typing == "MUJAFFA" or typing == "MUJAFA" or typing == "JONNA": 
                        if menu_select<1 or menu_select>1: menu_select = 1
                    else:
                        if menu_select<1: menu_select =2
                        if menu_select>2: menu_select =1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    menu_select += 1
                    if typing == "MUJAFFA" or typing == "MUJAFA" or typing == "JONNA": 
                        if menu_select<1 or menu_select>1: menu_select = 1
                    else:
                        if menu_select<1: menu_select =2
                        if menu_select>2: menu_select =1
                if event.key == pygame.K_SPACE:
                    if menu_select == 1:
                        menu_element = 1
                        menu_select = 0
                    if menu_select == 2:
                        menu_element = 3
                        playername = typing
def roaming_events():
    global spa,menu_element,menu_select,tradermenu,event
    if not pygame.key.get_pressed()[pygame.K_SPACE]:
        spa = "up" 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spa = "down" 
        if tradermenu == True:
            if room!=9: traderlimit = 4
            if room==9: traderlimit = 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_w or event.key == pygame.K_UP:
                    if menu_element == 1:
                        menu_select -= 1
                        if menu_select<1: menu_select = traderlimit
                        if menu_select>traderlimit: menu_select = 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if menu_element == 1:
                        menu_select += 1
                        if menu_select<1: menu_select = traderlimit
                        if menu_select>traderlimit: menu_select = 1
        if savemenu == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_w or event.key == pygame.K_UP:
                    menu_select -= 1
                    if menu_select<1: menu_select = 3
                    if menu_select>3: menu_select = 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    menu_select += 1
                    if menu_select<1: menu_select = 3
                    if menu_select>3: menu_select = 1
        if talk ==21 or talk==26:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_w or event.key == pygame.K_UP:
                    menu_select -= 1
                    if menu_select<1: menu_select = 2
                    if menu_select>2: menu_select = 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    menu_select += 1
                    if menu_select<1: menu_select = 2
                    if menu_select>2: menu_select = 1
def combatmenu_events():
    global spa,menupause,menu_element,menu_select,inventory,dialogue_options,attacking,triedtorunlikeabitch,enemy,talk,event
    if not pygame.key.get_pressed()[pygame.K_SPACE]:
        spa = "up" 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()    
        if event.type == pygame.KEYDOWN:
            spa = "down"
        if event.type == pygame.KEYUP:
            if menupause == False:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_w or event.key == pygame.K_UP:
                    if menu_element == 0:
                        menu_select -= 1
                        if menu_select<1: menu_select = 4
                        if menu_select>4: menu_select = 1
                    if menu_element == 2:
                        menu_select-=1
                        if menu_select<1: menu_select = dialogue_options
                        if menu_select>dialogue_options: menu_select = 1
                    if menu_element == 3:
                        menu_select-=1
                        if menu_select<1: menu_select = len(inventory)+1
                        if menu_select>len(inventory)+1: menu_select = 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if menu_element == 0:
                        menu_select += 1
                        if menu_select<1: menu_select = 4
                        if menu_select>4: menu_select = 1
                    if menu_element == 2:
                        menu_select+=1
                        if menu_select<1: menu_select = dialogue_options
                        if menu_select>dialogue_options: menu_select = 1
                    if menu_element == 3:
                        menu_select+=1
                        if menu_select<1: menu_select = len(inventory)+1
                        if menu_select>len(inventory)+1: menu_select = 1
                if event.key == pygame.K_SPACE:
                    if menu_element ==0:
                        if menu_select == 1:
                            attacking = 180
                            menupause = True
                            menu_select = 0
                        if menu_select == 2:
                            menu_element = 2
                            menu_select = 0
                        if menu_select == 3:
                            menu_element =3
                            menu_select = 0
                            spa = "up"
                        if menu_select ==4:
                            if enemy == "mujaffa"or enemy =="foxtrotkids"or enemy=="foxtrotguy"or enemy=="jonna"or enemy=="09"and encountered_09==True:
                                triedtorunlikeabitch = True
                            else:
                                talk = -1
                                menupause = True
                                spa = "up"
                    if menu_element ==2:
                        if menu_select ==2:
                            talk = 1
                            spa = "up"
                            menupause = True
                        if menu_select ==1:
                            menu_select = 2
                            menu_element = 0
                    if menu_element ==3:
                        if menu_select ==1:
                            menu_element = 0
                            menu_select = 3
                            menupause = False
                            triedtorunlikeabitch = False
                            spa = "up"
def combat_events():
    global event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()      
def dead_events():
    global menu_select,menu_element,event,is_dead,is_roaming,load
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()     
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                menu_select -= 1
                if menu_select<1: menu_select = 2
                if menu_select>2: menu_select = 1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                menu_select += 1
                if menu_select<1: menu_select = 2
                if menu_select>2: menu_select = 1
            if event.key == pygame.K_SPACE:
                if menu_select == 1:
                    if load!="0":
                        loaddata()
                        is_dead = False
                        is_roaming = True
                if menu_select == 2:
                    pygame.quit()
def outro_events():
    global event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()       
list09 = []
def attack09():
    global list09
    if randint(1,30) ==1 :
        list09.append([randint(150,850),535,randint(-45,45)])
    ca = 0
    for i in range(len(list09)):
        list09[i-ca][0] += 3*math.cos(math.radians(list09[i-ca][2]-90))
        list09[i-ca][1] += 3*math.sin(math.radians(list09[i-ca][2]-90))
        if list09[i-ca][2] < 180 and list09[i-ca][2] > -189:
            if list09[i-ca][2] <0:
                list09[i-ca][2] -=0.5
            if list09[i-ca][2] >=0:
                list09[i-ca][2] +=0.5
        pygame.draw.circle(skj,(255,0,0),(list09[i-ca][0],list09[i-ca][1]),15)
        if is_combat == False or list09[i-ca][1]>535:
            list09.pop(i-ca)
            ca +=1
stjen_pulse = 0
stjen_pulse2 = False
list_stjen = []
list2_stjen = []
def attackstjen():
    global stjen_pulse,stjen_pulse2,list_stjen,list2_stjen,px,py
    temp = (840+70*math.cos(math.atan2(py-355,px-840)) , 355+70*math.sin(math.atan2(py-355,px-840)))
    pygame.draw.line(skj,(255,0,0),(840,355),(temp),10)
    if stjen_pulse2 == False:
        stjen_pulse +=1
        if stjen_pulse>=10:
            stjen_pulse2 = True
            for i in range(18):
                radius = 75
                angle = i*20
                vec = pygame.math.Vector2(0, -radius).rotate(angle)
                xpo, ypo = int(280 + vec.x), int(355 + vec.y)
                list_stjen.append([xpo,ypo,i*20])         
    if stjen_pulse2 == True:
        stjen_pulse -=1
        if stjen_pulse<=0:
            stjen_pulse2 = False
            if randint(1,5)==1:
                temp1 = 840
                temp2 = 355
                while temp1>155 and temp1<845 and temp2>185 and temp2<525:
                    temp1 += math.cos(math.atan2(py-355,px-840))
                    temp2 += math.sin(math.atan2(py-355,px-840))
                list2_stjen.append([temp1,temp2,0,math.atan2(py-355,px-840)])
        
    pygame.draw.circle(skj,(255,0,0),(280,355),60+stjen_pulse*3)
    ca = 0
    for i in range(len(list2_stjen)):
        list2_stjen[i-ca][2]+=1
        if list2_stjen[i-ca][2] <60:
            pygame.draw.line(skj,(undertaleyellow),
                             (list2_stjen[i-ca][0],list2_stjen[i-ca][1]),
                             (840+70*math.cos(list2_stjen[i-ca][3]),355+70*math.sin(list2_stjen[i-ca][3]))
                             ,5)    
        if list2_stjen[i-ca][2] >=60:
            pygame.draw.line(skj,(255,0,0),
                             (list2_stjen[i-ca][0],list2_stjen[i-ca][1]),
                             (840+70*math.cos(list2_stjen[i-ca][3]),355+70*math.sin(list2_stjen[i-ca][3]))
                             ,5)   
        if list2_stjen[i-ca][2]>100:
            list2_stjen.pop(i-ca)
            ca +=1
    ca = 0
    for i in range(len(list_stjen)):
        list_stjen[i-ca][0] += 3*math.cos(math.radians(list_stjen[i-ca][2]-90))
        list_stjen[i-ca][1] += 3*math.sin(math.radians(list_stjen[i-ca][2]-90)) 
        pygame.draw.circle(skj,(255,0,0),(list_stjen[i-ca][0],list_stjen[i-ca][1]),5)
        if list_stjen[i-ca][0] < 160 or list_stjen[i-ca][0]>840 or list_stjen[i-ca][1]<190 or list_stjen[i-ca][1]>520:
            list_stjen.pop(i-ca)
            ca+=1
am_tile_offset = 0
am_count = 0
list1_am = []
def attackmujaffa1():
    global am_tile_offset,list1_am,am_count
    pygame.draw.rect(skj,(bak_col),(150,180,200,350))
    pygame.draw.rect(skj,(bak_col),(650,180,200,350))

    am_tile_offset +=3
    if am_tile_offset >160:am_tile_offset = 0
    for i in range(3):
        if i == 0:pygame.draw.rect(skj,(255,0,0),(490,(60-(-86+am_tile_offset))+40+am_tile_offset+160*i,10,-86+am_tile_offset))
        else:pygame.draw.rect(skj,(255,0,0),(490,40+am_tile_offset+160*i,10,60))
    am_count +=1
    if am_count > 120:
        list1_am.append([370+randint(0,1)*150,540])
        am_count = 0
    ca = 0
    for i in range(len(list1_am)):
        list1_am[i-ca][1] -=2
        if list1_am[i-ca][1] >= 400:
            pygame.draw.rect(skj,(255,0,0),(list1_am[i-ca][0],list1_am[i-ca][1],100,540-list1_am[i-ca][1]),0,15)
        elif list1_am[i-ca][1] <= 180:
            pygame.draw.rect(skj,(255,0,0),(list1_am[i-ca][0],list1_am[i-ca][1]+(+180-list1_am[i-ca][1]) ,100,-40+list1_am[i-ca][1]),0,15)
        else:
            pygame.draw.rect(skj,(255,0,0),(list1_am[i-ca][0],list1_am[i-ca][1],100,140),0,15)
        if list1_am[i-ca][1] <45:
            list1_am.pop(i-ca)
            ca +=1
    #pygame.draw.rect(skj,(255,255,0),(370,400,100,140),0,15)
    #pygame.draw.rect(skj,(255,255,0),(370,180,100,140),0,15)
    pygame.draw.rect(skj,(collision_col),(350,180,300,350),6,1)
    pygame.draw.rect(skj,(bak_col),(350,530,300,30))
    pygame.draw.rect(skj,(bak_col),(490,530,10,50))
list2_am = []
def attackmujaffa2():
    global list2_am
    pygame.draw.rect(skj,(bak_col),(150,180,200,350))
    pygame.draw.rect(skj,(collision_col),(350,180,500,350),6,1)  
    if randint(1,8) == 1:
        radius = 40
        angle = randint(1,360)
        vec = pygame.math.Vector2(0, -radius).rotate(angle)
        xpo, ypo = int(770 + vec.x), int(450 + vec.y)
        list2_am.append([xpo,ypo,randint(270,360)])  
   
    ca = 0
    for i in range (len(list2_am)):
        list2_am[i-ca][0] += 3*math.cos(math.radians(list2_am[i-ca][2]-90))
        list2_am[i-ca][1] += 3*math.sin(math.radians(list2_am[i-ca][2]-90))
        if list2_am[i-ca][2] > 180:
                list2_am[i-ca][2] -=0.5
 
        pygame.draw.circle(skj,(255,0,0),(list2_am[i-ca][0],list2_am[i-ca][1]),6)
        pygame.draw.circle(skj,(255,0,0),(list2_am[i-ca][0]+12,list2_am[i-ca][1]),6)
        pygame.draw.polygon(skj,(255,0,0),[
        (list2_am[i-ca][0]-6,list2_am[i-ca][1]),(list2_am[i-ca][0]+18,list2_am[i-ca][1]),(list2_am[i-ca][0]+6,list2_am[i-ca][1]+13)
        ])
        
    skj.blit(mujaffabil,mujaffabil.get_rect(topleft = (680+randint(-8,8),390+randint(-8,8))))    
fokids_var = 0
list_fokids = []
def attackfoxtrotkids():
    global list_fokids ,fokids_var
    fokids_var+=1
    if fokids_var>=90:
        vinkel = randint(1,360)
        list_fokids.append([vinkel,0,"launch",400])
        fokids_var=0
    ca = 0
    for i in range(len(list_fokids)):
        rad = 300     
        vec1 = pygame.math.Vector2(0,-rad).rotate(list_fokids[i-ca][0])
        startpoint = int(500+vec1.x),int(335+vec1.y)
        if not list_fokids[i-ca][2]=="return":
            ang = list_fokids[i-ca][0]+list_fokids[i-ca][1]
        else:
            ang = list_fokids[i-ca][0]
        radians = math.radians(ang)
        cos = math.cos(radians)
        sin = math.sin(radians)
        startpoint=startpoint[0]+int(list_fokids[i-ca][3]*cos),startpoint[1]+int(list_fokids[i-ca][3]*sin)
        pygame.draw.line(skj,(255,0,0),(startpoint),(startpoint[0]+80*cos,startpoint[1]+80*sin),20)
        pygame.draw.line(skj,(255,0,0),(startpoint[0]+70*cos,startpoint[1]+70*sin),(startpoint[0]+260*cos,startpoint[1]+260*sin),30)
        cos1 = math.cos(math.radians(ang-90))
        cos2 = math.cos(math.radians(ang+90))
        sin1 = math.sin(math.radians(ang-90))
        sin2 = math.sin(math.radians(ang+90))
        pygame.draw.line(skj,(255,0,0),(startpoint[0]+70*cos+50*cos1,startpoint[1]+70*sin+50*sin1),(startpoint[0]+70*cos+50*cos2,startpoint[1]+70*sin+50*sin2),10)
        pygame.draw.polygon(skj,(255,0,0),[
            (startpoint[0]+320*cos,startpoint[1]+320*sin),
            (startpoint[0]+250*cos+(14*cos1),startpoint[1]+250*sin+(14*sin1)),
            (startpoint[0]+250*cos+(14*cos2),startpoint[1]+250*sin+(14*sin2))
            ])
            
        if list_fokids[i-ca][2]=="launch":
            list_fokids[i-ca][3]-= 0.05*(list_fokids[i-ca][3])
            if list_fokids[i-ca][3]<=10:
                list_fokids[i-ca][3]=0
                list_fokids[i-ca][2]="slash"
        if list_fokids[i-ca][2]=="slash":    
            list_fokids[i-ca][1]+=0.05*(361-list_fokids[i-ca][1])
            if list_fokids[i-ca][1]>358:
                list_fokids[i-ca][1]=360
                list_fokids[i-ca][2]="return"
                list_fokids[i-ca][3]=1
        if list_fokids[i-ca][2]=="return":
            list_fokids[i-ca][3]+=0.2*(list_fokids[i-ca][3])
            if list_fokids[i-ca][3]>=400:
                list_fokids.pop(i-ca)
                ca+=1
foguyvar = 0
list_foguy = []
def attackfoxtrotguy():
    global foguyvar,list_foguy,gun2,px,py
    pygame.draw.rect(skj,(bak_col),(150,180,150,350))
    pygame.draw.rect(skj,(bak_col),(700,180,150,350))
    pygame.draw.rect(skj,(collision_col),(300,180,400,350),6,1)
    foguyvar+=1
    if foguyvar>=60:
        vinkel = randint(1,360)
        rad = 300
        vec1 = pygame.math.Vector2(0,-rad).rotate(vinkel)
        list_foguy.append([vinkel,0,"launch",400,px,py])
        foguyvar=0
    ca = 0
    for i in range(len(list_foguy)):
        rad = 300     
        vec1 = pygame.math.Vector2(0,-rad).rotate(list_foguy[i-ca][0])
        startpoint = int(500+vec1.x),int(335+vec1.y)
        ang = list_foguy[i-ca][0]
        radians = math.radians(ang)
        cos = math.cos(radians)
        sin = math.sin(radians)
        startpoint=startpoint[0]+int(list_foguy[i-ca][3]*cos),startpoint[1]+int(list_foguy[i-ca][3]*sin)
        point = math.atan2(list_foguy[i-ca][5]-startpoint[1],list_foguy[i-ca][4]-startpoint[0])
        point2 = math.radians(math.degrees(point)+10)
        pointleft = math.radians(math.degrees(point2)-90)
        cos2 = math.cos(pointleft)
        sin2 = math.sin(pointleft)
        rotatedrect = pygame.transform.rotate(gun2,360-math.degrees(point)-10)
        if list_foguy[i-ca][2]=="shoot":
            pygame.draw.line(skj,(255,0,0),(startpoint[0]+53*cos2,startpoint[1]+53*sin2),
            (startpoint[0]+2500*math.cos(point2)+53*cos2,startpoint[1]+2500*math.sin(point2)+53*sin2),25)
        skj.blit(rotatedrect,rotatedrect.get_rect(center = (startpoint)))

        if list_foguy[i-ca][2]=="launch":
            list_foguy[i-ca][3]-= 0.1*(list_foguy[i-ca][3])
            if list_foguy[i-ca][3]<=1:
                list_foguy[i-ca][3]=0
                list_foguy[i-ca][2]="shoot"
        if list_foguy[i-ca][2]=="shoot":    
            list_foguy[i-ca][1]+=0.05*(61-list_foguy[i-ca][1])
            if list_foguy[i-ca][1]>60:
                list_foguy[i-ca][1]=0
                list_foguy[i-ca][2]="return"
                list_foguy[i-ca][3]=1
        if list_foguy[i-ca][2]=="return":
            list_foguy[i-ca][3]+=0.2*(list_foguy[i-ca][3])
            if list_foguy[i-ca][3]>=400:
                list_foguy.pop(i-ca)
                ca+=1
list_jonna = []
jonnavar = 0
def attackjonna1():
    global list_jonna, combat_timer, jonnavar
    pygame.draw.rect(skj,(bak_col),(150,180,175,350))
    pygame.draw.rect(skj,(bak_col),(675,180,175,350))
    if combat_timer>480:
        randi1 = randint(-5,5)
        randi2 = randint(-5,5)
        ak1 = pygame.transform.rotate(ak47,randint(-5,5))
        akk2 = pygame.transform.flip(ak47,True,False)
        ak2 = pygame.transform.rotate(akk2,randint(-5,5))
        skj.blit(ak1,ak1.get_rect(center = (150,355)))
        skj.blit(ak2,ak2.get_rect(center = (850,355)))
        jonnavar+=1
        if jonnavar >=15:
            vec1 = pygame.math.Vector2(0,-135).rotate(90+randi1-5)
            list_jonna.append([int(150+vec1.x),int(355+vec1.y),(randint(-30,30))])
            vec2 = pygame.math.Vector2(0,-135).rotate(-90+randi2+5)
            list_jonna.append([int(850+vec2.x),int(355+vec2.y),(-180+randint(-30,30))])
            jonnavar = 0
        ca = 0
        for i in range(len(list_jonna)):
            list_jonna[i-ca][0] += 5*math.cos(math.radians(list_jonna[i-ca][2]))
            list_jonna[i-ca][1] += 5*math.sin(math.radians(list_jonna[i-ca][2]))
            pygame.draw.circle(skj,(255,0,0),(list_jonna[i-ca][0],list_jonna[i-ca][1]),8)
            if list_jonna[i-ca][0]<0 or list_jonna[i-ca][0]>1000 or list_jonna[i-ca][1]<0 or list_jonna[i-ca][1]>700:
                list_jonna.pop(i-ca)
                ca+=1
    if combat_timer<480 and combat_timer>120:
        angle = 480-combat_timer
        ak1 = pygame.transform.rotate(ak47,-angle)
        akk2 = pygame.transform.flip(ak47,True,False)
        ak2 = pygame.transform.rotate(akk2,-angle)
        vect1 = pygame.math.Vector2(0,-350).rotate(angle-90)
        vect2 = pygame.math.Vector2(0,-350).rotate(90+angle)
        vect3 = pygame.math.Vector2(0,-220).rotate(angle-90)
        vect4 = pygame.math.Vector2(0,-220).rotate(90+angle)
        skj.blit(ak1,ak1.get_rect(center = (vect1.x+500,vect1.y+355)))
        skj.blit(ak2,ak2.get_rect(center = (vect2.x+500,vect2.y+355)))
        pygame.draw.line(skj,(255,0,0),(vect3.x+500,vect3.y+355),(vect4.x+500,vect4.y+355),15+randint(1,10))
    if combat_timer<120:
        thickness = int((120-combat_timer)*2)
        pygame.draw.line(skj,(255,0,0),(0,355),(1000,355),15+thickness+randint(1,10))
        doom2 = pygame.transform.flip(doomshotgun,True,False)
        skj.blit(doom2,doom2.get_rect(center = (150+randint(-10,10),355+randint(-10,10))))
        skj.blit(doomshotgun,doomshotgun.get_rect(center = (850+randint(-10,10),355+randint(-10,10))))
    pygame.draw.rect(skj,(collision_col),(325,180,350,350),6,1)
def attackjonna2():
    global list_jonna,px,py
    if list_jonna==[]:
        list_jonna.append(["tank",-90,120])
        list_jonna.append(["tank",90,120])
        list_jonna.append(["jet",700,130,0,0])
        list_jonna.append(["jet",300,580,180,0])
    ca = 0
    for i in range(len(list_jonna)):
        if list_jonna[i-ca][0]=="tank":
            vec = pygame.math.Vector2(0,-400).rotate(-1*(90+(list_jonna[i-ca][1])))
            tankbod = pygame.transform.rotate(tankbody,90+(list_jonna[i-ca][1]))
            skj.blit(tankbod,tankbod.get_rect(center = (vec.x+500,vec.y+335)))
            list_jonna[i-ca][1]+=0.2
            rads = math.radians(-(-90+list_jonna[i-ca][1]))
            headpoint = vec.x+500+(20*math.cos(rads)),vec.y+335+(20*math.sin(rads))
            tankhed = pygame.transform.rotate(tankhead,180+360-math.degrees(math.atan2(py-headpoint[1],px-headpoint[0])))
            skj.blit(tankhed,tankhed.get_rect(center=(headpoint)))
            list_jonna[i-ca][2]-=1
            if list_jonna[i-ca][2]<=0:
                rads2 = math.atan2(py-headpoint[1],px-headpoint[0])
                point = headpoint[0]+(180*math.cos(rads2)),headpoint[1]+(180*math.sin(rads2))
                list_jonna.append(["tankshot",point[0],point[1],(rads2)])
                list_jonna[i-ca][2]=120
        if list_jonna[i-ca][0]=="tankshot":
            p1 = list_jonna[i-ca][1]+50*math.cos(list_jonna[i-ca][3]) , list_jonna[i-ca][2]+50*math.sin(list_jonna[i-ca][3])
            pygame.draw.line(skj,(255,0,0),(list_jonna[i-ca][1],list_jonna[i-ca][2]),(p1),10)
            list_jonna[i-ca][1]+=7*math.cos(list_jonna[i-ca][3])
            list_jonna[i-ca][2]+=7*math.sin(list_jonna[i-ca][3])
        if list_jonna[i-ca][0]=="jetshot":
            list_jonna[i-ca][1]+=10*math.cos(math.radians(list_jonna[i-ca][3]))
            list_jonna[i-ca][2]+=10*math.sin(math.radians(list_jonna[i-ca][3]))            
            pygame.draw.line(skj,(255,0,0),
            (list_jonna[i-ca][1],list_jonna[i-ca][2]),
            (list_jonna[i-ca][1]+40*math.cos(math.radians(list_jonna[i-ca][3])),list_jonna[i-ca][2]+40*math.sin(math.radians(list_jonna[i-ca][3]))),2)
            if list_jonna[i-ca][1]<0 or list_jonna[i-ca][1]>1000 or list_jonna[i-ca][2]<0 or list_jonna[i-ca][2]>700: 
                list_jonna.pop(i-ca)
                ca+=1
        if list_jonna[i-ca][0]=="jet":
            playerdir = -180+180+math.degrees(math.atan2(py-list_jonna[i-ca][2],px-list_jonna[i-ca][1]))
            if playerdir<0:
                playerdir +=360
            if playerdir>360:
                playerdir -=360
            plus = 0
            if list_jonna[i-ca][3] > int(playerdir):
                plus += 360-list_jonna[i-ca][3]
                plus += int(playerdir)
            else:
                plus = int(playerdir)-list_jonna[i-ca][3]
            minus = 360-plus
            if plus<minus:
                list_jonna[i-ca][3]+=1
            if plus>minus:
                list_jonna[i-ca][3]-=1
            if list_jonna[i-ca][3]<0:
                list_jonna[i-ca][3]+=360
            if list_jonna[i-ca][3]>360:
                list_jonna[i-ca][3]-=360
            list_jonna[i-ca][4]+=1
            if plus<45 or minus<45:
                if list_jonna[i-ca][4]>30:
                    list_jonna.append(["jetshot",list_jonna[i-ca][1],list_jonna[i-ca][2],list_jonna[i-ca][3]])
                    list_jonna[i-ca][4]=0
            list_jonna[i-ca][1]+=3*math.cos(math.radians(list_jonna[i-ca][3]))
            list_jonna[i-ca][2]+=3*math.sin(math.radians(list_jonna[i-ca][3]))
            radians = math.radians(list_jonna[i-ca][3])
            radians1 = math.radians(list_jonna[i-ca][3]+135)
            radians2 = math.radians(list_jonna[i-ca][3]-135)
            radians3 = math.radians(list_jonna[i-ca][3]-160)
            radians4 = math.radians(list_jonna[i-ca][3]+160)
            pygame.draw.line(skj,(255,0,0),(list_jonna[i-ca][1],list_jonna[i-ca][2]),(list_jonna[i-ca][1]-4*math.cos(radians),list_jonna[i-ca][2]-4*math.sin(radians)),3)
            pygame.draw.polygon(skj,(255,0,0),[(list_jonna[i-ca][1]-4*math.cos(radians),list_jonna[i-ca][2]-4*math.sin(radians)),
            (list_jonna[i-ca][1]+10*math.cos(radians3)-4*math.cos(radians),list_jonna[i-ca][2]+10*math.sin(radians3)-4*math.sin(radians)),
            (list_jonna[i-ca][1]+10*math.cos(radians4)-4*math.cos(radians),list_jonna[i-ca][2]+10*math.sin(radians4)-4*math.sin(radians))])
            pygame.draw.line(skj,(255,0,0),(list_jonna[i-ca][1]-10*math.cos(radians),list_jonna[i-ca][2]-10*math.sin(radians)),
            (list_jonna[i-ca][1]-35*math.cos(radians),list_jonna[i-ca][2]-35*math.sin(radians)),8)
            pygame.draw.polygon(skj,(255,0,0),[(list_jonna[i-ca][1]-25*math.cos(radians),list_jonna[i-ca][2]-25*math.sin(radians)),
            (list_jonna[i-ca][1]-12*math.cos(radians),list_jonna[i-ca][2]-12*math.sin(radians)),
            (list_jonna[i-ca][1]-20*math.cos(radians)+22*math.cos(radians1),list_jonna[i-ca][2]-20*math.sin(radians)+22*math.sin(radians1))])
            pygame.draw.polygon(skj,(255,0,0),[(list_jonna[i-ca][1]-25*math.cos(radians),list_jonna[i-ca][2]-25*math.sin(radians)),
            (list_jonna[i-ca][1]-12*math.cos(radians),list_jonna[i-ca][2]-12*math.sin(radians)),
            (list_jonna[i-ca][1]-20*math.cos(radians)+22*math.cos(radians2),list_jonna[i-ca][2]-20*math.sin(radians)+22*math.sin(radians2))])
            pygame.draw.polygon(skj,(255,0,0),[(list_jonna[i-ca][1]-30*math.cos(radians),list_jonna[i-ca][2]-30*math.sin(radians)),
            (list_jonna[i-ca][1]-38*math.cos(radians),list_jonna[i-ca][2]-38*math.sin(radians)),
            (list_jonna[i-ca][1]-30*math.cos(radians)+15*math.cos(radians1),list_jonna[i-ca][2]-30*math.sin(radians)+15*math.sin(radians1))])
            pygame.draw.polygon(skj,(255,0,0),[(list_jonna[i-ca][1]-30*math.cos(radians),list_jonna[i-ca][2]-30*math.sin(radians)),
            (list_jonna[i-ca][1]-38*math.cos(radians),list_jonna[i-ca][2]-38*math.sin(radians)),
            (list_jonna[i-ca][1]-30*math.cos(radians)+15*math.cos(radians2),list_jonna[i-ca][2]-30*math.sin(radians)+15*math.sin(radians2))])
            #pygame.draw.line(skj,(255,255,0),(list_jonna[i-ca][1],list_jonna[i-ca][2]),(list_jonna[i-ca][1]+1000*math.cos(math.radians(list_jonna[i-ca][3])),list_jonna[i-ca][2]+1000*math.sin(math.radians(list_jonna[i-ca][3]))),1)
            #pygame.draw.line(skj,(100,100,255),(list_jonna[i-ca][1],list_jonna[i-ca][2]),(list_jonna[i-ca][1]+1000*math.cos(math.radians(playerdir)),list_jonna[i-ca][2]+1000*math.sin(math.radians(playerdir))),1)
def attackjonna3():
    global list_jonna,combat_timer
    if combat_timer==850:
        list_jonna.append(["nuke",800,0,randint(-590,-470)])
    if combat_timer==400:
        list_jonna.append(["nuke",200,0,randint(-590,-470)])
    ca = 0
    for i in range(len(list_jonna)):
        if list_jonna[i-ca][0]=="nuke":
            if list_jonna[i-ca][3]<0:
                list_jonna[i-ca][2]+=1+(list_jonna[i-ca][2]/50)
                list_jonna[i-ca][3]+=5
                rotrect = pygame.transform.rotate(nuke,-90)
                skj.blit(rotrect,rotrect.get_rect(center=(list_jonna[i-ca][1],int(list_jonna[i-ca][2]))))
            else:
                list_jonna[i-ca][3]+=1
                if int(list_jonna[i-ca][3])==30:
                    for j in range(18):
                        list_jonna.append(["ball",list_jonna[i-ca][1],list_jonna[i-ca][2],j*20])
                if int(list_jonna[i-ca][3])==60:
                    for j in range(18):
                        list_jonna.append(["ball",list_jonna[i-ca][1],list_jonna[i-ca][2],10+j*20])
                    list_jonna[i-ca][3]=0
                pygame.draw.circle(skj,(255,0,0),(list_jonna[i-ca][1],int(list_jonna[i-ca][2])),25+randint(1,10))
        if list_jonna[i-ca][0]=="ball":
            list_jonna[i-ca][1]+=2*math.cos(math.radians(list_jonna[i-ca][3]))
            list_jonna[i-ca][2]+=2*math.sin(math.radians(list_jonna[i-ca][3]))
            pygame.draw.circle(skj,(255,0,0),(list_jonna[i-ca][1],list_jonna[i-ca][2]),5)
            if list_jonna[i-ca][1]<0 or list_jonna[i-ca][1]>1000 or list_jonna[i-ca][2]<0 or list_jonna[i-ca][2]>700: 
                list_jonna.pop(i-ca)
                ca+=1
def attackjonna4():
    global combat_timer,px,py,jonnavar
    jonnavar+=1
    if list_jonna==[]:
        list_jonna.append(["idle",450,55,270,0,"left"])
        list_jonna.append(["idle",550,55,90,0,"right"])
        py = 450
    if jonnavar>=90:
        if randint(1,2)==1:list_jonna[0][0]="swing"
        else:list_jonna[1][0]="swing"
        jonnavar=0
    for i in range(len(list_jonna)):
        if list_jonna[i][0]=="swing":
            list_jonna[i][4]+=1+int(list_jonna[i][4]/18)
            if list_jonna[i][4]>90:
                list_jonna[i][4]=90
                list_jonna[i][0]="return"
        if list_jonna[i][0]=="return":
            list_jonna[i][4]-=1+int((90-list_jonna[i][4])/18)
            if list_jonna[i][4]<0:
                list_jonna[i][4]=0
                list_jonna[i][0]="idle"
        startpoint = (list_jonna[i][1],list_jonna[i][2])
        if list_jonna[i][5]=="right":
            radians = math.radians(list_jonna[i][3]-90+list_jonna[i][4])
            radians2 = math.radians(list_jonna[i][3]+90-90+list_jonna[i][4])
            radians3 = math.radians(list_jonna[i][3]-90-90+list_jonna[i][4])
        elif list_jonna[i][5]=="left":
            radians = math.radians(list_jonna[i][3]-90-list_jonna[i][4])
            radians2 = math.radians(list_jonna[i][3]+90-90-list_jonna[i][4])
            radians3 = math.radians(list_jonna[i][3]-90-90-list_jonna[i][4])            
        cos = math.cos(radians)
        sin = math.sin(radians)
        handlepoint = (list_jonna[i][1]+300*cos,list_jonna[i][2]+300*sin)
        cos2 = math.cos(radians2)
        sin2 = math.sin(radians2)
        cos3 = math.cos(radians3)
        sin3 = math.sin(radians3)
        pygame.draw.polygon(skj,(255,0,0),[(list_jonna[i][1]+15*cos,list_jonna[i][2]+15*sin),
        (list_jonna[i][1]-30*cos+50*cos2,list_jonna[i][2]-30*sin+50*sin2),
        (list_jonna[i][1]-80*cos+50*cos2,list_jonna[i][2]-80*sin+50*sin2),
        (list_jonna[i][1]-80*cos+50*cos3,list_jonna[i][2]-80*sin+50*sin3),
        (list_jonna[i][1]-30*cos+50*cos3,list_jonna[i][2]-30*sin+50*sin3)
        ],30)
        pygame.draw.line(skj,(255,0,0),startpoint,(handlepoint),30)
        pygame.draw.polygon(skj,(255,0,0),[(handlepoint[0]+180*cos,handlepoint[1]+180*sin),
        (handlepoint[0]+70*cos2+160*cos,handlepoint[1]+70*sin2+160*sin),
        (handlepoint[0]+70*cos2,handlepoint[1]+70*sin2),
        (handlepoint[0]+70*cos3,handlepoint[1]+70*sin3),
        (handlepoint[0]+70*cos3+160*cos,handlepoint[1]+70*sin3+160*sin)
        ])
    if px<355: px=355
    if px>645: px=645
    if py<285: py=285
    if py>525: py=525

  
while True:
    if is_startmenu == True:
        menu_element = 0
        menu_select = 0
        if playername!=None:
            is_roaming = True
            is_startmenu = False
    while is_startmenu == True:
        skj.fill(bak_col)

        if menu_element== 0:
            skj.blit(logo,logo.get_rect(center=(500,100)))
            if menu_select==1: skj.blit(undertalefont.render("* Nytt spill",False,(undertaleyellow)),(320,350))
            else: skj.blit(undertalefont.render("  Nytt spill",False,(255,255,255)),(320,350))
            if menu_select==2: skj.blit(undertalefont.render("* Last spill",False,(undertaleyellow)),(320,450))
            else: skj.blit(undertalefont.render("  Last spill",False,(255,255,255)),(320,450))

            if menu_select==1 and spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                is_intro = True
                is_startmenu = False
                spa = "up"
            if menu_select==2 and spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                menu_select = 0
                menu_element = 1
                spa = "up"
        if menu_element ==1:
            if load!="0":
                pygame.draw.rect(skj,(0,0,0),(150,100,700,200))
                pygame.draw.rect(skj,(255,255,255),(150,100,700,200),6)    
                with open(dir+"Data.txt","r") as o:
                    tempload =ast.literal_eval(o.read())
                    o.flush()
                displayname = tempload[0][0]
                displaylvl = tempload[0][3]
                skj.blit(undertalefont.render("Lagret spill:",False,(255,255,255)),(180,130))
                skj.blit(undertalefont2.render(f"{displayname}   NIVÅ {displaylvl}",False,(255,255,255)),(180,240))
                if menu_select==1: skj.blit(undertalefont.render("* Fortsett spill",False,(undertaleyellow)),(300,500))
                else: skj.blit(undertalefont.render("  Fortsett spill",False,(255,255,255)),(300,500))
                if menu_select==1 and spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                    loaddata()

                    is_roaming = True
                    is_startmenu = False
                    spa = "up"
            else: 
                skj.blit(undertalefont.render("Det er ingen lagrede spill",False,(255,255,255)),(180,130))
                if menu_select==1: skj.blit(undertalefont.render("  -----",False,(undertaleyellow)),(300,500))
                else: skj.blit(undertalefont.render("  -----",False,(255,255,255)),(300,500))
            if menu_select==2: skj.blit(undertalefont.render("* Tilbake",False,(undertaleyellow)),(300,600))
            else: skj.blit(undertalefont.render("  Tilbake",False,(255,255,255)),(300,600))            
            if menu_select==2 and spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                menu_select = 0
                menu_element = 0
                spa = "up"
        startmenu_events()

        pygame.display.flip()
        pygame.display.update()
        cl.tick(60)
    if is_intro == True:
        menu_select = 30
        menu_element = 1
        spa = "up"
        typing = ""
        keyboardlist = ["Q","W","E","R","T","Y","U","I","O","P","Å","A","S","D","F","G","H","J","Ø","Æ","K","L","Z","X","C","V","B","N","M"] 
        introcinematic = 0
    while is_intro == True:
        skj.fill(bak_col)
        if menu_element == 1:
            pygame.draw.rect(skj,(255,255,255),(300,150,400,100),4,1)
            skj.blit(undertalefont.render(typing,False,(255,255,255)),(345,170))
            skj.blit(undertalefont3.render("Hva vil du hete? Gi deg selv et bra navn",False,(255,255,255)),(35,20))
            for i in range(10):
                if menu_select == i+1:buttonkey(60+i*90,300,keyboardlist[i],(undertaleyellow))
                else: buttonkey(60+i*90,300,keyboardlist[i],"white")
            for i in range(10):
                if menu_select == i+11: buttonkey(40+i*90,390,keyboardlist[i+10],(undertaleyellow))
                else: buttonkey(40+i*90,390,keyboardlist[i+10],"white")
            for i in range(9):
                if menu_select == i+21: buttonkey(20+i*90,480,keyboardlist[i+20],(undertaleyellow))
                else: buttonkey(20+i*90,480,keyboardlist[i+20],"white")
            if menu_select == 30: buttonkey(830,480,"BACKSPACE",(undertaleyellow))
            else: buttonkey(830,480,"BACKSPACE","white")
            if menu_select == 31: buttonkey(355,580,"CONFIRM",(undertaleyellow))
            else: buttonkey(355,580,"CONFIRM","white")
        if menu_element ==2:
            if typing == "MUJAFFA" or typing == "MUJAFA" or typing == "JONNA":
                skj.blit(undertalefont3.render("Det navnet er jævla uoriginalt!",False,(255,255,255)),(110,30))
                skj.blit(undertalefont3.render("Prøv på nytt!",False,(255,255,255)),(300,90))  
                if menu_select == 1: skj.blit(undertalefont.render("* OK",False,(undertaleyellow)),(450,300))
                else: skj.blit(undertalefont.render("OK",False,(255,255,255)),(450,300))
            else:             
                skj.blit(undertalefont3.render("Det navnet er kjedelig som faen!",False,(255,255,255)),(95,30))
                skj.blit(undertalefont3.render("Har du lyst til å beholde det likevel?",False,(255,255,255)),(60,90))
                if menu_select == 1: skj.blit(undertalefont.render("* Nei",False,(undertaleyellow)),(200,300))
                else: skj.blit(undertalefont.render("Nei",False,(255,255,255)),(200,300))
                if menu_select == 2: skj.blit(undertalefont.render("* Ja",False,(undertaleyellow)),(600,300))
                else: skj.blit(undertalefont.render("Ja",False,(255,255,255)),(600,300))
        if menu_element == 3:
            introcinematic+=0.5
            if introcinematic>=0 and introcinematic<=120:
                c1 = int((introcinematic*(255/120)))
                skj.blit(undertalefont3.render("Du er en ung og alminnelig hasjbruker",False,(c1,c1,c1)),((40,90)))
            elif introcinematic>=480 and introcinematic<600:
                c1 = 255-int(((introcinematic-480)*(255/120)))
                skj.blit(undertalefont3.render("Du er en ung og alminnelig hasjbruker",False,(c1,c1,c1)),((40,90)))
            elif introcinematic>120 and introcinematic<480:skj.blit(undertalefont3.render("Du er en ung og alminnelig hasjbruker",False,(255,255,255) ) ,((40,90)))

            if introcinematic>=120 and introcinematic<=240:
                c1 = int(((introcinematic-120)*(255/120)))
                skj.blit(undertalefont3.render("Du tar t-banen i Oslo for å hente litt keef",False,(c1,c1,c1)),((10,170)))
            elif introcinematic>=480 and introcinematic<600:
                c1 = 255-int(((introcinematic-480)*(255/120)))
                skj.blit(undertalefont3.render("Du tar t-banen i Oslo for å hente litt keef",False,(c1,c1,c1)),((10,170)))
            elif introcinematic>240 and introcinematic<480: skj.blit(undertalefont3.render("Du tar t-banen i Oslo for å hente litt keef",False,(255,255,255) ) ,((10,170)))
            
            if introcinematic>=240 and introcinematic<=360:
                c1 = int(((introcinematic-240)*(255/120)))
                skj.blit(undertalefont3.render(",men du blir vipps-ranet og kasta" ,False,(c1,c1,c1)),((20,250)))
                skj.blit(undertalefont3.render("ut på feil stasjon",False,(c1,c1,c1)),((20,290)))
            elif introcinematic>=480 and introcinematic<600:
                c1 = 255-int(((introcinematic-480)*(255/120)))
                skj.blit(undertalefont3.render(",men du blir vipps-ranet og kasta" ,False,(c1,c1,c1)),((20,250)))
                skj.blit(undertalefont3.render("ut på feil stasjon",False,(c1,c1,c1)),((20,290)))
            elif introcinematic>360 and introcinematic<480: 
                skj.blit(undertalefont3.render(",men du blir vipps-ranet og kasta" ,False,(255,255,255)),((20,250)))
                skj.blit(undertalefont3.render("ut på feil stasjon",False,(255,255,255)),((20,290)))
            
            if introcinematic>=360 and introcinematic<=480:
                c1 = int(((introcinematic-360)*(255/120)))
                skj.blit(undertalefont3.render("du ender opp i et sted du ikke kan forlate",False,(c1,c1,c1)),((20,360)))
            elif introcinematic>=480 and introcinematic<600:
                c1 = 255-int(((introcinematic-480)*(255/120)))
                skj.blit(undertalefont3.render("du ender opp i et sted du ikke kan forlate",False,(c1,c1,c1)),((20,360)))
            elif introcinematic>480 and introcinematic<480: skj.blit(undertalefont3.render("du ender opp i et sted du ikke kan forlate",False,(255,255,255) ) ,((20,360)))

            if introcinematic>=600 and introcinematic<720:
                c1 = int(((introcinematic-600)*(255/120)))
                skj.blit(undertalefont3.render("Du er nå stuck i Stovner...",False,(c1,c1,c1)),((50,300)))
            elif introcinematic>=720 and introcinematic<800:skj.blit(undertalefont3.render("Du er nå stuck i Stovner...",False,(255,255,255)),((50,300)))

            if introcinematic>=800:
                skj.blit(logo,logo.get_rect(center=(500,350)))
            if introcinematic >=920:
                is_roaming = True
                is_intro = False
            
        intro_events()

        pygame.display.flip()
        pygame.display.update()
        cl.tick(60)
    if is_roaming == True:
        px = savepx
        py = savepy
        psize = 64
        pspeed = 2
        encanim = 0
        encani = 0
        talk = 0
        lvldif = 0
        encounter_cooldown = 300
        levelupscreen = False
        hideplayer = False
        tradermenu = False
        savemenu = False
        collision_col = undertalepurple
        ismoving = False
        staranim = 0
        star = star1
    while is_roaming == True:
        skj.fill(bak_col)
        rooms()
        if talk ==1:
            dialogue(450,"Hva er greia di mann?","Du følger meg som en bikkje!","")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 2
                spa = "up"
        if talk ==2:
            dialogue(450,"Ikke fuck med Mujaffa","Mujaffa har Mujaffas BMW","")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 3
                spa = "up"
        if talk ==3:
            dialogue(450,"Wallah jeg gætter deg rett ned!","","RETT NED SA JEG!!")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                encanim = 1
                enemy = "mujaffa"
                HPmax = 20+(lvl*2)
                HP = HPmax
                enemyHP = 25
                enemyHPmax = 25
                talk = -1
                turn = 0
                spa = "up"                         
        if talk ==4:
            dialogue(450,"Wallah man mujaffa gir faen i kids","...","Jeg gir faen")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 5
                spa = "up"
        if talk ==5:
            dialogue(450,"Fuck deg man","Jeg jetter til mujaffas BMW","")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                mujani = 1
                talk = 0
                spa = "up"
                talkstun = False
        if talk ==6:
            dialogue(450,"(Du tror at du kan flykte fra ","stovner I Mujaffas BMW nå som","Mujaffa er borte)")
            if event.type == pygame.KEYUP and spa == "down" and levelupscreen == False:
                if event.key == pygame.K_SPACE:  
                    if jonna_ani ==1:
                        jonna_x = 700
                        jonna_y = 0    
                        jonna_ani = 2
                    spa = "up"     
        if talk ==7:
            dialogue(450,"Mujaffa er død, lenge leve Jonna","...","Greit om jeg tæsjer denne BMW-en?")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 8
                spa = "up" 
        if talk ==8:
            dialogue(450,"Jeg gir faen i hva du mener","","Den er min nå")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                jonna_ani = 4
                jonna_x = 400
                jonna_y = 160
                talkstun = False
                talk = 0
                spa = "up"      
        if talk ==9:
            dialogue(450,"<== Mujaffas JONNAS verksted ","","              kjedelig kiwibutikk    ==>")
            pygame.draw.line(skj,(255,255,255),(160,495),(380,495),3)
            pygame.draw.line(skj,(255,255,255),(160,485),(380,478),3)
            pygame.draw.line(skj,(255,255,255),(160,475),(380,485),3)
            pygame.draw.line(skj,(255,255,255),(160,500),(380,460),3)
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                talkstun = False
                talk = 0
                spa = "up"
        if talk ==10:
            if py>400: placedialogue=50
            else:placedialogue=450
            dialogue(placedialogue,"Dette er Jonnas bunker","Den er låst","(han har spillet for mye fallout 4)")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 0
                talkstun = False
                spa = "up" 
        if talk ==11:    
            dialogue(50,"Dette er nå Jonnas BWM.","Du må beseire den nåverende","eieren for å kunne rulle i den")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 0
                talkstun = False
                spa = "up" 
        if talk ==12:    
            dialogue(30,"Vi äger stället här nu.","Gå bort förlorare detta är foxtrot ","territorium!")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                encanim = 1
                enemy = "foxtrotkids"
                HPmax = 20+(lvl*2)
                HP = HPmax
                enemyHP = 30
                enemyHPmax = 30
                turn = 0    
                talk = 0            
                talkstun = False
                triedtorunlikeabitch = False
                spa = "up" 
        if talk ==13:    
            dialogue(450,"Halla kid! Jeg trenger litt hjelp.","Disse nye svenskebandene har","tatt over Kiwi-en her.")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 14
                spa = "up" 
        if talk ==14:    
            dialogue(450,"Hvis du kunne ha fjernet dem",",kan jeg begynne å selge ting i","dette territoriumet også!")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 0
                talkstun = False
                spa = "up" 
        if talk ==15:
            dialogue(450,"Tror du verkligen att du kan ","ta över vårt territorium?","du får mig att skratta lilla!")
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                talk = 16
                spa ="up"
        if talk ==16:
            dialogue(450,"Vad?","aldrig sett en pistol förut?","din lilla jävel")
            skj.blit(gun,gun.get_rect(topleft = (590,70)))
            if spa == "down" and pygame.key.get_pressed()[pygame.K_SPACE]:  
                spa ="up"
                encanim = 1
                enemy = "foxtrotguy"
                HPmax = 20+(lvl*2)
                HP = HPmax
                enemyHP = 40
                enemyHPmax = 40
                turn = 0    
                talk = 0            
                talkstun = False
                triedtorunlikeabitch = False
        if talk ==17:
            dialogue(450,"Skapet har en nøkkel i seg","som hører til Jonna's bunker","")
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                hasbunkerkey = True
                talkstun = False
                talk = 0
                spa = "up"
        if talk ==18:
            dialogue(450,"Jonna's skap har flere plakater av ","Jonna's favorittspill",", men ikke Stovnertale :c")
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                talk = 0
                talkstun = False
                spa = "up"    
        if talk ==19:
            dialogue(450,"Robin og Dawit har forlatt tralla","her imens de tar en puff-pause","på dass (den har vart i 2-timer)")
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                talk = 20
                spa = "up"
        if talk ==20:
            dialogue(450,"Dette gjør at du ikke kan gå lengre","forbi her på grunn av videospill-","logikk  >:)  ")
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                talk = 0
                talkstun = False
                spa = "up" 
        if talk ==21:
            if menu_select ==1: temptalk1 = "* Nei"
            else: temptalk1 = "Nei"
            if menu_select ==2: temptalk2 = " * Ja"
            else: temptalk2 = "Ja"
            if room==8:tempplacement = 450
            if room==4:tempplacement = 50
            dialogue(tempplacement,"Vil du ta sparkesykkelen?","(det er gratis fordi Stovner logic)","   "+temptalk1+"         "+temptalk2)
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                if menu_select ==1:
                    talk = 0
                    talkstun = False
                if menu_select ==2:
                    talk = 0
                    talkstun = False
                    if room ==8: 
                        room =4
                        px = 250
                        py = 450
                    elif room ==4: 
                        room =8  
                        px = 350
                        py = 280
                spa = "up"
        if talk ==22:
            dialogue(450,"Du er fanget i Stovner fordi staten","har valgt å stanse all kollektiv-","transport ut av stovner.")
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                talk = 0
                talkstun = False
                spa = "up"      
        if talk ==23:
            dialogue(480,"Makan til oppførsel!","","")   
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                talk = 24
                spa = "up"
        if talk ==24:
            dialogue(480,"Tror du virkelig at du kan tæsje","min BMW?","Ikke tro du er noe lille drittunge!")   
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                talk = 0
                encanim = 1
                enemy = "jonna"
                HPmax = 20+(lvl*2)
                HP = HPmax
                enemyHP = 100
                enemyHPmax = 100
                turn = 0          
                talkstun = False
                triedtorunlikeabitch = False                
                spa = "up"
        if talk ==25:
            dialogue(480,"Jonna er beseiret, du er nå den","verdige eieren av Mujaffas BMW..","Du kan nå forlate Stovner")   
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE] and levelupscreen == False:
                talk  = 0
                spa = "up"
        if talk ==26:
            if menu_select ==1: temptalk1 = "* Nei"
            else: temptalk1 = "Nei"
            if menu_select ==2: temptalk2 = " * Ja"
            else: temptalk2 = "Ja"
            dialogue(50,"Har du lyst til å forlate Stovner?",temptalk1+"         "+temptalk2,"")   
            if spa=="down" and pygame.key.get_pressed()[pygame.K_SPACE]:
                if menu_select==1:
                    talk = 0
                    talkstun = False
                if menu_select==2:
                    talk  = 0
                    is_roaming = False
                    is_outro = True
                spa = "up"
        if mujani ==1:
            mujanim -=4
        if mujanim <0:
            mujani = -1
            mujanim = 0

        if not encanim == 0:
            if encanim >6:
                skj.fill((0,0,0))
            if encanim >12:
                encanim = 1
                encani +=1
            if encani ==4:
                savepx = px
                savepy = py
                talkstun = False
                is_combatmenu = True 
                is_roaming = False 
            encanim +=1
        if exp >= (lvl+1)*5 and levelupscreen == False:
            exp -= (lvl+1)*5
            lvl +=1
            lvldif +=1
            if not exp >= (lvl+1)*5:
                if lvl >=3:rank = "Keef Enjoyer"
                if lvl >=10:rank = "Serious Addict"
                if lvl >=50:rank = "død.."
                levelupscreen = True
                talkstun = True
                hideplayer = True
        if levelupscreen == True:
            levelup_screen()
        if tradermenu == True:
            trading()
        if talkstun == False:
            playermovement()       
        if talkstun == True: ismoving = False         
        ke = pygame.key.get_pressed()
        if hideplayer == False:
            playeranimation()
            skj.blit(image,playerect)
        #pygame.draw.rect(skj,(0,0,0),playerrect,1)                                          #imagesize
        #pygame.draw.rect(skj,(0,255,0),(int(px-(psize/2)),int(py-(psize/2)),psize,psize))   #hitbox
        if savemenu == True:
            savingmenu()

        roaming_events()

        pygame.display.flip()
        pygame.display.update()
        cl.tick(60)     

    if is_combatmenu == True:
        pdamage = 4 + lvl
        menu_select = 1
        menu_element = 0
        menupause = False
        winscreen = False
        triedtorunlikeabitch = False
        attacking = -1
        collision_col = (255,255,255)  
        talk = 0    
        list09 = []
        am_tile_offset = 0
        am_count = 0
        list1_am = []
        list2_am = []
        stjen_pulse = 0
        stjen_pulse2 = False
        list_stjen = []
        list2_stjen = []
        fokids_var = 0
        list_fokids = []
        foguyvar = 0
        list_foguy = []
        list_jonna = []
        jonnavar = 0
        if enemy == "mujaffa":dialogue_options = 1
        if enemy == "09":dialogue_options = 2
        if enemy == "stovnerjenter":dialogue_options = 2
        if enemy == "foxtrotkids":dialogue_options = 2
        if enemy == "foxtrotguy":dialogue_options = 1
        if enemy == "jonna":dialogue_options = 2
    while is_combatmenu == True:
        skj.fill(bak_col)
        if enemy == "mujaffa":
            skj.blit(muj,muj.get_rect(topleft = (350,12)))
        if enemy == "09":
            skj.blit(er09,er09.get_rect(topleft = (380,180)))
        if enemy == "stovnerjenter":
            skj.blit(stojent,stojent.get_rect(topleft = (250,-45)))
        if enemy == "foxtrotkids":
            skj.blit(foxtrotkids,foxtrotkids.get_rect(topleft = (270,-21)))
        if enemy == "foxtrotguy":
            skj.blit(foxtrotguy2,foxtrotguy2.get_rect(topleft = (380,-21)))
        if enemy == "jonna":
            skj.blit(jonna2,jonna2.get_rect(topleft = (390,-55)))
        pygame.draw.rect(skj,collision_col,(50,330,900,200),6,1)
        skj.blit(undertalefont2.render((playername),False,(255,255,255)),(50,560))
        skj.blit(undertalefont2.render(str("NIVÅ "+str(lvl)),False,(255,255,255)) ,(300,560))
        skj.blit(undertalefont2.render(str("HP  "+str(HP)+"/"+str(HPmax)),False,(255,255,255)) ,(550,560))
        pygame.draw.rect(skj,(255,0,0),(620,560,40,30))
        pygame.draw.rect(skj,(undertaleyellow),(620,560, 40*(HP/HPmax) ,30))
        enemies()          
        if menu_element ==3:
            checking_inventory()

        if menu_select ==1 and menu_element == 0:    
            orangebutton(50,620,undertaleyellow,"KÆS","sword",0)
        else:
            orangebutton(50,620,undertaleorange,"KÆS","sword",0)
        if menu_select == 2 and menu_element == 0:
            orangebutton(290,620,undertaleyellow,"YAP","act",15)
        else:
            orangebutton(290,620,undertaleorange,"YAP","act",15)
        if menu_select == 3 and menu_element == 0:
            orangebutton(540,620,undertaleyellow,"RØYK","item",-8)
        else:
            orangebutton(540,620,undertaleorange,"RØYK","item",-8)
        if menu_select == 4 and menu_element == 0:
            orangebutton(777,620,undertaleyellow,"JET","mercy",15)
        else:
            orangebutton(777,620,undertaleorange,"JET","mercy",15)
        if attacking >0:
            pygame.draw.rect(skj,(64,64,64),(447,77,106,36))
            if attacking <135:
                skj.blit(undertalefont.render(str(pdamage),False,(255,0,0)),(475,10))
            if attacking >90:
                pygame.draw.rect(skj,(0,255,0),(450,80,100*(enemyHP/enemyHPmax),30))
            else:
                pygame.draw.rect(skj,(0,255,0),(450,80,100*((enemyHP-pdamage)/enemyHPmax),30))
            if enemyHP-pdamage <=0:
                if enemy == "09":
                    talkbubble(600,150,200,100,1,"ERM WHAT","THE SIGMA","")
                if enemy == "stovnerjenter":
                    talkbubble(700,150,200,100,1,"Cancelled!","","")
                    talkbubble(100,150,250,100,2,str("#"+str(playername)+"ISOVERPARTY"),"","")
            elif turn == 0 and enemy == "09":
                talkbubble(600,150,200,100,1,"OHIO MOMENT","","")
            elif turn == 0 and enemy == "stovnerjenter":
                talkbubble(100,150,200,100,2,"Slå meg enda","hardere!","")
            attacking-=1
        if attacking == 0:
            enemyHP -= pdamage
            if enemyHP >0:
                is_combat = True
                is_combatmenu = False
                triedtorunlikeabitch = False
                menupause = False
                attacking = -10
            if enemyHP <=0:
                triedtorunlikeabitch= False
                menupause = True
                winscreen = True
                attacking = -10
        if winscreen == True: win_screen()

            

        combatmenu_events()            
        pygame.display.flip()
        pygame.display.update()
        cl.tick(60)

    if is_combat == True:
        talk = 0
        talkcounter = 0
        px = 500
        py = 350
        if enemy == "mujaffa":
            attack_choice = randint(1,2)
            if attack_choice == 1:
                px = 450
            if attack_choice ==2:
                talk = 1
                talkstun = True
        if enemy == "jonna": attack_choice = randint(1,2)
        psize = 20
        pspeed = 2
        pimmunity = -1
        menu_select = 0
        collision_col = (255,255,255)
        talkstun = False
    while is_combat == True:
        skj.fill(bak_col)
        if enemy == "mujaffa":
            skj.blit(muj,muj.get_rect(topleft = (350,12)))
        if enemy == "09":
            skj.blit(er09,er09.get_rect(topleft = (380,30)))
        if enemy == "stovnerjenter":
            skj.blit(stojent,stojent.get_rect(topleft = (250,-45)))
        if enemy == "foxtrotkids":
            skj.blit(foxtrotkids,foxtrotkids.get_rect(topleft = (270,-91)))
        if enemy == "foxtrotguy":
            skj.blit(foxtrotguy2,foxtrotguy2.get_rect(topleft = (380,-91)))
        if enemy == "jonna":
            if attack_choice==4 and enemyHP<=50:skj.blit(jonna2,jonna2.get_rect(topleft = (390,70)))
            else: skj.blit(jonna2,jonna2.get_rect(topleft = (390,-100)))
        if not(enemy=="jonna"and attack_choice==2 and enemyHP<=50):
            pygame.draw.rect(skj,bak_col,(150,180,700,350))
            pygame.draw.rect(skj,collision_col,(150,180,700,350),6,1)
        else: 
            pygame.draw.rect(skj,bak_col,(350,350,300,180))
            pygame.draw.rect(skj,collision_col,(350,350,300,180),6,1)
        
        skj.blit(undertalefont2.render((playername),False,(255,255,255)),(50,560))
        skj.blit(undertalefont2.render(str("NIVÅ "+str(lvl)),False,(255,255,255)) ,(300,560))
        skj.blit(undertalefont2.render(str("HP  "+str(HP)+"/"+str(HPmax)),False,(255,255,255)) ,(550,560))
        pygame.draw.rect(skj,(255,0,0),(620,560,40,30))
        pygame.draw.rect(skj,(undertaleyellow),(620,560, 40*(HP/HPmax) ,30))
        orangebutton(50,620,undertaleorange,"KÆS","sword",0)
        orangebutton(290,620,undertaleorange,"YAP","act",15)
        orangebutton(540,620,undertaleorange,"RØYK","item",-8)
        orangebutton(777,620,undertaleorange,"JET","mercy",15)
        if enemy == "09":
            attack09() 
            enemydamage = 4
        if enemy == "mujaffa":
            if attack_choice ==1:
                attackmujaffa1()
                enemydamage = 6
            if attack_choice ==2:
                enemydamage = 6
                if talk == 0:
                    attackmujaffa2()
        if enemy == "stovnerjenter":
            attackstjen()
            enemydamage = 5
        if enemy == "foxtrotkids":
            attackfoxtrotkids()
            enemydamage = 6
        if enemy == "foxtrotguy":
            attackfoxtrotguy()
            enemydamage = 10
        if enemy == "jonna":
            if enemyHP>50:
                if attack_choice ==1:
                    attackjonna2()
                    enemydamage = 12
                if attack_choice ==2:
                    attackjonna3()
                    enemydamage = 10
            else:
                if attack_choice ==1:
                    attackjonna1()
                    enemydamage = 12
                if attack_choice==2:
                    attackjonna4()
                    enemydamage = 12
        if pimmunity <= 0:
            c = "(255, 0, 0)"
            if ps2(c):
                HP -=enemydamage
                pimmunity = 90
        if pimmunity >0:
            pimmunity -=1
            if int(pimmunity/10)/2 == int(int(pimmunity/10)/2):
                #pygame.draw.rect(skj,(255,255,100),(int(px-(psize/2)),int(py-(psize/2)),psize,psize))
                pygame.draw.circle(skj,(255,255,100),(px,py),psize/2)
            else:
                #pygame.draw.rect(skj,(0,150,0),(int(px-(psize/2)),int(py-(psize/2)),psize,psize))
                pygame.draw.circle(skj,(0,150,0),(px,py),psize/2)
        else:
            #pygame.draw.rect(skj,(0,255,0),(int(px-(psize/2)),int(py-(psize/2)),psize,psize))
            pygame.draw.circle(skj,(0,150,0),(px,py),psize/2)
            skj.blit(weed,weed.get_rect(topleft=(px-psize/2,py-1-psize/2)))
        if talkstun == False:
            playermovement()
        if enemy == "foxtrotguy":
            if px<(306+(psize/2)): px = 306+(psize/2)#300,180,400,350
            if px>(794-(psize/2)): px = 794-(psize/2)
            if py<(186+(psize/2)): py = 186+(psize/2)
            if py>(524-(psize/2)): py = 524-(psize/2)

        if talk ==1:
            talkbubble(600,50,250,150,1,"Halla snuppa! ","Kom inn i Mujaffas","BMW!")
            talkcounter+=1
            if talkcounter >40:
                talkbubble(700,300,200,80,2,"OK JEG KOMMER!","","")
            if talkcounter >180:
                px = 500
                py = 350    
                talkstun = False
                talkcounter = 0
                talk = 0

        if HP <=0:
            is_dead = True
            is_combat = False
            list09 = []
        if talk ==0:
            combat_timer-=1
        if combat_timer <0:
            turn +=1
            is_combatmenu = True
            is_combat = False
  
        combat_events()
        pygame.display.flip()
        pygame.display.update()
        cl.tick(60)   
    if is_dead == True:
        menu_select = 0 
    while is_dead == True:
        skj.fill(bak_col) 
        pygame.draw.rect(skj,collision_col,(225,100,550,100),6,1)
        skj.blit(undertalefont3.render("Du døde... jævla taper",False,(255,255,255)),(235,110))
        if load!="0":temp = "Load save"
        else:temp = "---"
        if menu_select ==1:
            skj.blit(undertalefont3.render(f"  * {temp}",False,(undertaleyellow)),(80,400))
        else:
            skj.blit(undertalefont3.render(f"  {temp}",False,(255,255,255)),(80,400))
        if menu_select ==2:
            skj.blit(undertalefont3.render("  * Kan jeg pliiis få en ny sjanse?",False,(undertaleyellow)),(80,500))
        else:
            skj.blit(undertalefont3.render("  Kan jeg pliiis få en ny sjanse?",False,(255,255,255)),(80,500))

        dead_events()
        pygame.display.flip()
        pygame.display.update()
        cl.tick(60)              
    if is_outro == True:
        bak_col = (0,0,0)
        fadein = 1
        creditscroll = -40
        credits = [
                    ["STOVNERTALE"],
                    ["Creator of game: Anders Mc.Western"],
                    ["game designer: Anders Mc.Western"],
                    ["art director: Anders Mc.Western"],
                    ["stealing art from online: Anders Mc.Western"],
                    ["skillfull programming:"],
                    ["programming: Anders Mc.Western"],
                    ["big dick haver: Anders Mc.Western"],
                    [""],
                    ["ROLES"],
                    ["mujaffa: mujaffa muj affason"],
                    ["mujaffas BMW: mujaffas BMW"],
                    ["jonna: Jonna michealson"],
                    ["09-eren: en unge jeg kidnappa fra gata"],
                    ['stovner"jentene": tumbler.com'],
                    ["narkoman pat pat: https://www.youtube.com/"],
                    ["                  watch?v=tIqPHTGFtes"],
                    ["foxtrot-mannen: Rawa Majid"],
                    [f"En feit liten drittsekk: {playername}"],
                    [""],
                    ["SPECIAL THANKS"],
                    ['kebabnorsk translator: Bobin"Sassmate"rolysh'],
                    ["inspirasjon: jul i svingen"],
                    ["             Osama Bin Laden"],
                    ["             200 mg anfetamin"],
                    ["personal albino: albino bakken"],
                    [""],
                    ["OBJECTS I'VE SHOVED UP MY ARSE"],
                    ["Vibrators "],
                    ["Dildos "],
                    ["Pens "],
                    ["Pencils "],
                    ["Coins "],
                    ["Pebbles "],
                    ["Broomstick Handle"],
                    ]
    while is_outro == True:
        if fadein<255:
            fadein+=0.5
            if fadein>255: fadein=255
            sunset = pygame.transform.scale((pygame.image.load(dir+"sunset.png")),(603,600))#201 200
            sunset.fill((255, 255, 255, int(fadein)), None, pygame.BLEND_RGBA_MULT)
            mujaffabil2 = pygame.transform.scale((pygame.image.load(dir+"mujaffabil2.png")),(225,225)) #90 90
            mujaffabil2.fill((255, 255, 255, fadein), None, pygame.BLEND_RGBA_MULT)
        skj.fill(bak_col)
        skj.blit(sunset,sunset.get_rect(bottomleft=(0,700)))
        skj.blit(mujaffabil2,mujaffabil2.get_rect(center=(250,640)))
        
        for i in range(len(credits)):
            skj.blit(undertalefont6.render(str(credits[i][0]),False,(255,255,255)),(520,700-int(creditscroll)+i*35))
        creditscroll+=0.75
        if creditscroll>1200:
            pygame.quit()


        outro_events()
        pygame.display.flip()
        pygame.display.update()
        cl.tick(60)