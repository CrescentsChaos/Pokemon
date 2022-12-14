from movelist import *
import random
naturelist=["Hardy","Lonely","Adamant","Naughty","Brave", "Bold",'Docile','Impish','Lax','Relaxed' ,'Modest','Mild','Bashful','Rash','Quiet' ,'Calm','Gentle','Careful','Quirky','Sassy', 'Timid','Hasty','Jolly','Naive','Serious']
class Pokemon2:
    "Pokemon2"
    def __init__(self,name="Unidentified",type1="Normal",type2=None,nature=None,level=100,happiness=0,hp=0,atk=0,defense=0,spatk=0,spdef=0,speed=0,hpiv=0,atkiv=0,defiv=0,spatkiv=0,spdefiv=0,speediv=0,maxiv="No",atktype="Normal",hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,status="Alive",atkb=1,defb=1,spatkb=1,spdefb=1,speedb=1,ability=None,moves=None,movez=None,badpoison=1,flinched=False,recharge=False,seeded=False, canfakeout=True,item="Leftovers",precharge=False, protect=False,shelltrap=False,choiced=False,choicedmove=None,owner=None,teratype=None,taunted=False,critrate=1, accuracy=100,dmax=False,maxmove=None,maxend=0,megaintro=False,primalintro=False,fsprite="graphics/fsprites/unknown.png", bsprite="graphics/bsprites/Gengar.png", priority=False,dbond=False, abilityused=False,healcount=0,confused=False,dmgtaken=0,yawn=False,m1pp=10,m2pp=10,m3pp=10,m4pp=10,mx1pp=10,mx2pp=10,mx3pp=10,mx4pp=10,pplist=None,aring=False,olock=False):
        #Name
        self.name=name
        if moves is None:
            self.moves=[]
        else:
            self.moves=moves
        self.shiny=random.randint(1,4096)
        if self.shiny==7:
            self.name=self.name+"✨"
        #Type
        self.type1=type1
        self.type2=type2
        self.aring=aring
        self.olock=olock
        self.atkby=None
        self.atktime=0
        self.m1pp=m1pp
        self.m2pp=m2pp
        self.m3pp=m3pp
        self.m4pp=m4pp
        self.mx1pp=mx1pp
        self.mx2pp=mx2pp
        self.mx3pp=mx3pp
        self.mx4pp=mx4pp
        if self.moves[0] in typemoves.pp5:
            self.m1pp=self.mx1pp=5
        if self.moves[1] in typemoves.pp5:
            self.m2pp=self.mx2pp=5
        if self.moves[2] in typemoves.pp5:
            self.m3pp=self.mx3pp=5
        if self.moves[3] in typemoves.pp5:
            self.m4pp=self.mx4pp=5
        self.pplist=[self.m1pp,self.m2pp,self.m3pp,self.m4pp]
        self.yawn=yawn
        self.dmgtaken=dmgtaken
        self.confused=confused
        self.healcount=healcount
        self.teratype=teratype
        self.item=item
        self.abilityused=abilityused
        self.dbond=dbond
        self.fsprite=fsprite
        self.bsprite=bsprite
        self.megaintro=megaintro
        self.dmax=dmax
        self.priority=priority 
        self.primalintro=primalintro 
        self.accuracy=accuracy
        self.critrate=critrate
        self.basestats=atk+defense+spdef+spatk+hp+speed
        self.owner=owner
        self.badpoison=badpoison
        self.recharge=recharge
        self.seeded=seeded
        self.flinched=flinched
        self.precharge=precharge 
        self.protect=protect
        self.shelltrap=shelltrap
        self.canfakeout=canfakeout
        self.choiced=choiced
        self.taunted=taunted 
        self.maxend=maxend
        self.choicedmove=choicedmove
        self.basename=self.name.split(" ")[-1]
        self.fsprite="graphics/fsprites/"+self.basename+".png"
        #self.bsprite="graphics/bsprites/"+self.basename+".png"
        #Nature
        self.nature=nature
        if self.nature is None:
            self.gennature()
        #Level
        self.level=level
        #Happiness
        self.happiness=happiness
        #Base Stats
        self.hp=hp
        self.atk=atk
        self.defense=defense
        self.spatk=spatk
        self.spdef=spdef
        self.speed=speed
        #IVs
        self.hpiv=hpiv
        self.atkiv=atkiv
        self.defiv=defiv
        self.spatkiv=spatkiv
        self.spdefiv=spdefiv
        self.speediv=speediv
        #IVs
        self.hpev=hpev
        self.atkev=atkev
        self.defev=defev
        self.spatkev=spatkev
        self.spdefev=spdefev
        self.speedev=speedev
        self.alpha=random.randint(1,20)
        if "Mega " not in self.name and self.alpha==7 and maxiv not in ["Yes","gmax"]:
            self.name="Alpha "+name
        self.totem=random.randint(1,20)
        if "Mega " not in self.name and "Alpha " not in name and self.totem == 7 and maxiv not in ["Yes","gmax"]:
            self.name="Totem "+name
        self.teratype=random.randint(1,50)
        if self.teratype==2 and "Mega" not in self.name and "Alpha " not in self.name and self.dmax is False and maxiv not in ["gmax","Yes"]:
            if self.type2==None:
                self.teratype=random.choices([self.type1,random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])],weights=[60,40],k=1)[0]
            if self.type2!=None:
                self.teratype=random.choices([self.type1,self.type2,random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])],weights=[40,40,20],k=1)[0]
            if self.teratype not in (self.type1,self.type2):
                self.moves[0]="Tera Blast"
            self.name+="💎"
        self.movez=movez
        if self.teratype not in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
            self.teratype=None
        if ((maxiv not in ("Yes","gmax")) or "Z-Crystal" in self.name) and "💎" not in self.name:
            self.movez=random.randint(1,2)
            if "Z-Crystal" in self.name:
                self.movez=2
        if self.movez==2 and "Mega " not in self.name and "Alpha " not in self.name:
            self.moves+=zmove(self)
            if "(Z-Crystal)" not in self.name:
                self.name+="(Z-Crystal)"
        #Command
        self.maxiv=maxiv
        #Attack Manipulation
        self.atktype=atktype
        #Boost
        self.atkb=atkb
        self.defb=defb
        self.spatkb=spatkb
        self.spdefb=spdefb
        self.speedb=speedb
        
        #stats
        self.ability=ability
        self.status=status
        mch=random.randint(1,2)
        if "💎" in self.name and self.maxiv in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]: 
            self.teratype=self.maxiv
            
        if (((("Mega " not in self.name and "Z-Crystal" not in self.name and "Zacian" not in self.name and "Zamazenta" not in self.name) and mch==1 and self.maxiv!="Yes" and "Battle Bond" not in self.ability) or self.maxiv=="gmax" ) and "💎" not in self.name):
            self.dmax=True
            rename(self)
        if self.dmax is True:
            self.maxmove=mxmove(self,typemoves)
        self.calcst()
        self.hp=self.maxhp
    def genlowiv(self):
        "Sets to Max IV"
        self.hpiv=self.atkiv=self.defiv=self.spatkiv=self.spdefiv=self.speediv=0
    def genmaxiv(self):
        "Sets to Max IV"
        self.hpiv=self.atkiv=self.defiv=self.spatkiv=self.spdefiv=self.speediv=31
#GENERATES RANDOM IV
    def geniv(self):
        "Generates Random IV"
        self.hpiv=random.randint(0,31)
        self.atkiv=random.randint(0,31)
        self.defiv=random.randint(0,31)
        self.spatkiv=random.randint(0,31)
        self.spdefiv=random.randint(0,31)
        self.speediv=random.randint(0,31)
        if self.maxiv=="Steel":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,31,30,31
        if self.maxiv=="Dark":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,31,31,31
        if self.maxiv=="Dragon":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,31,31,31,31
        if self.maxiv=="Ghost":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,30,31,30,31
        if self.maxiv=="Rock":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,30,31,30,30
        if self.maxiv=="Bug":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,31,30,30
        if self.maxiv=="Psychic":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,31,31,31,30
        if self.maxiv=="Flying":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,30,30,30
        if self.maxiv=="Poison":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,30,30,30,31
        if self.maxiv=="Electric":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,30,31,31
        if self.maxiv=="Water":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,30,31,30
        if self.maxiv=="Fighting":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,30,30,30,30
        if self.maxiv=="Ground":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,30,30,31
        if self.maxiv=="Grass":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,31,30,31,31
        if self.maxiv=="Ice":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,30,31,31,31
        if self.maxiv=="Fire":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,31,30,31,30
        if "Mega " not in self.name and self.alpha==7:
            self.hpiv=random.randint(15,31)
            self.atkiv=random.randint(15,31)
            self.defiv=random.randint(15,31)
            self.spatkiv=random.randint(15,31)
            self.spdefiv=random.randint(15,31)
            self.speediv=random.randint(15,31)
        if "Mega " not in self.name and self.totem==7:
            num=random.randint(1,50)
            if num==1:
                self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=(31,31,31,31,31,31)
            if 1>num<5:
                iv=[31,31,31,31,31,random.randint(15,31)]
                random.shuffle(iv)
                self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=tuple(iv)
            if 4<num<20:
                iv=[31,31,31,31,random.randint(15,31),random.randint(15,31)]
                random.shuffle(iv)
                self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=tuple(iv)
            else:
                iv=[31,31,31,random.randint(15,31),random.randint(15,31),random.randint(15,31)]
                random.shuffle(iv)
                self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=tuple(iv)
    def maxendturn(self,turn):
        if self.dmax is True:
            self.maxend=turn+3                    
                        
    def calcst(self):
        "Calculates Stats"
        #Generates Random IV
        if self.maxiv=="No":
            self.geniv()
        elif self.maxiv=="Low":
            self.genlowiv()
        else:
            self.genmaxiv()
        self.maxhp = stat_clac(self.hp,self.hpiv,self.hpev,self.level,"HP")
        self.maxatk = stat_clac(self.atk,self.atkiv,self.atkev,self.level)
        self.maxdef=stat_clac(self.defense,self.defiv,self.defev,self.level)
        self.maxspatk = stat_clac(self.spatk,self.spatkiv,self.spatkev,self.level)
        self.maxspdef = stat_clac(self.spdef,self.spdefiv,self.spdefev,self.level)
        self.maxspeed =stat_clac(self.speed,self.speediv,self.speedev,self.level)
        
        self.natureboost()
#        self.maxhp=self.hp
#        self.maxatk=self.atk
#        self.maxspeed=self.speed
#        self.maxspatk=self.spatk
#        self.maxspdef=self.spdef
#        self.maxdef=self.defense
        if self.dmax==True:
            self.hp*=2
            self.maxhp*=2
        if self.name=="Shedinja":
            self.hp=self.maxhp=1
        self.maxtotal=self.maxhp+self.maxatk+self.maxdef+self.maxspatk+self.maxspdef+self.maxspeed
        
#NATURE BOOST
    def natureboost(self):
        "Boosts stats according to nature"
        if self.nature in ["Bashful","Docile","Hardy","Quirky","Serious"]:
            pass
        if self.nature in ["Adamant","Brave","Lonely","Naughty"]:
            self.atk+=round(self.atk*0.1)
        if self.nature in ["Mild","Modest","Quite","Rash"]:
            self.spatk+=round(self.spatk*0.1)
        if self.nature in ["Adamant","Careful","Impish","Jolly"]:
            self.spatk-=round(self.spatk*0.1)
        if self.nature in ["Bold","Calm","Modest","Timid"]:
            self.atk-=round(self.atk*0.1)
        if self.nature in ["Bold","Relaxed","Lax","Impish"]:
            self.defense+=round(self.defense*0.1)
        if self.nature in ["Gentle","Hasty","Lonely","Mild"]:
            self.defense-=round(self.defense*0.1)
        if self.nature in ["Calm","Careful","Gentle","Sassy"]:
            self.spdef+=round(self.spdef*0.1)
        if self.nature in ["Lax","Naive","Naughty","Rash"]:
            self.spdef-=round(self.spdef*0.1)
        if self.nature in ["Jolly","Timid","Naive","Hasty"]:
            self.speed+=round(self.speed*0.1)
        if self.nature in ["Brave","Quite","Sassy","Relaxed"]:
            self.speed-=round(self.speed*0.1)
#GENERATES NATURE
    def gennature(self):
        "Generates Nature"
        self.nature=random.choice(naturelist)
        
    def ivc(self):
        "Checks IV"
        print(f"HP IV: {self.hpiv}/31")
        print(f"Attack IV: {self.atkiv}/31")
        print(f"Defence IV: {self.defiv}/31")
        print(f"Special Attack IV: {self.spatkiv}/31")
        print(f"Special Defence IV: {self.spdefiv}/31")
        print(f"Speed IV: {self.speediv}/31")
        totaliv=self.hpiv+self.atkiv+self.defiv+self.spatkiv+self.spdefiv+self.speediv
        print("=============================================")
        percentage=(totaliv/186)*100
        print(f"Total IV: {totaliv}/186")
        print(f"IV: {round(percentage,2)}%")
    
        print("=============================================")
    def info(self):
        "Shows Stats"
        print("=============================================")
        print(f"Name: {self.name}")
        if self.type2 is None:
            print(f"Type: {self.type1}")
        else:
            print(f"Type: {self.type1}/{self.type2}")
        print(f"Nature: {self.nature}")
        print(f"Ability: {self.ability}")
        print(f"Item: {self.item}")
        print(f"Level: {self.level}")
        print("=============================================")
        print("Stats:")
        print("=============================================")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.atk}")
        print(f"Defence: {self.defense}")
        print(f"Special Attack: {self.spatk}")
        print(f"Special Defence: {self.spdef}")
        print(f"Speed: {self.speed}")
        print("=============================================")
        self.ivc()
#Calculates Stats
def stat_clac(stat,individual_value,effort_value,level,spst=None):
	"Generates enhanced stats"
	if spst == "HP":
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+level+10)
	else:
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+5)
	
	return new_stat
        
#typem
def movelist(self):
    "Shows Moves"
    num=0
    print("=============================================")
    print(f" {self.name}'s available moves.")
    print("=============================================")
    if self.moves == []:
        print(" No Moves")
    if self.dmax is True:
        for i in self.maxmove:
            num+=1
            print(f" {num}. {i} ({self.pplist[self.maxmove.index(i)]})")
    if self.dmax is False:
        for i in self.moves:
            num+=1
            print(f" {num}. {i} ({self.pplist[self.moves.index(i)]})")          
#            if num==1:
#                print(f" {num}. {i} ({self.pplist[self.moves.index(i)]}/{self.mx1pp})")
#            if num==2:
#                print(f" {num}. {i} ({self.m2pp}/{self.mx2pp})")
#            if num==3:
#                print(f" {num}. {i} ({self.m3pp}/{self.mx3pp})")
#            if num==4:
#                print(f" {num}. {i} ({self.m4pp}/{self.mx4pp})")
#            if num==5:
#                print(f" {num}. {i} (1/1)")
    print("=============================================")
def moveset(moves,num=4):
    new=[]
    while len(new)!=num:
        x=random.choice(moves)
        if x not in new:
            new.append(x)
    return new        
    
def mxmove(self,typem=typemoves):
    maxmove=[]
    gm=None
    for i in self.moves:
        if i in typem.dragonmoves:
            gm="Max Wyrmwind"
            if "Duraludon" in self.name:
                gm="G-Max Depletion"
        if i in typem.normalmoves:
            gm="Max Strike"
            if "Snorlax" in self.name:
                gm="G-Max Replenish"
            if "Meowth" in self.name:
                gm="G-Max Gold Rush"
            if "Eevee" in self.name:
                gm="G-Max Cuddle"
        if i in typem.steelmoves:
            gm="Max Steelspike"
            if "Copperajah" in self.name:
                gm="G-Max Steelsurge"
            if "Melmetal" in self.name:
                gm="G-Max Meltdown"
        if i in typem.fairymoves:
            gm="Max Starfall"
            if "Hatterene" in self.name:
                gm="G-Max Smite"
            if "Alcremie" in self.name:
                gm="G-Max Finale"
        if i in typem.rockmoves:
            gm="Max Rockfall"
            if "Coalossal" in self.name:
                gm="G-Max Volcalith"
        if i in typem.groundmoves:
            gm="Max Quake"
            if "Sandaconda" in self.name:
                gm="G-Max Sandblast"
        if i in typem.ghostmoves:
            gm="Max Phantasm"
            if "Gengar" in self.name:
                gm="G-Max Terror"
        if i in typem.grassmoves:
            gm="Max Overgrowth"
            if "Venusaur" in self.name:
                gm="G-Max Vine Lash"
            if "Flapple" in self.name:
                gm="G-Max Tartness"
            if "Appletun" in self.name:
                gm="G-Max Sweetness"
            if "Rillaboom" in self.name:
                gm="G-Max Drum Solo"
        if i in typem.poisonmoves:
            gm="Max Ooze"
            if "Garbodor" in self.name:
                gm="G-Max Malodor"
        if i in typem.psychicmoves:
            gm="Max Mindstorm"
            if "Orbeetle" in self.name:
                gm="G-Max Gravitas"
        if i in typem.electricmoves:
            gm="Max Lightning"
            if "Pikachu" in self.name:
                gm="G-Max Volt Crash"
            if "Toxtricity" in self.name:
                gm="G-Max Stun Shock"
        if i in typem.fightingmoves:
            gm="Max Knuckle"
            if "Machamp" in self.name:
                gm="G-Max Chi Strike"
        if i in typem.icemoves:
            gm="Max Hailstorm"
            if "Lapras" in self.name:
                gm="G-Max Resonance"
        if i in typem.statusmove:
            gm="Max Guard"
        if i in typem.watermoves:
            gm="Max Geyser"
            if "Drednaw" in self.name:
                gm="G-Max Stonesurge"
            if "Rapid" in self.name:
                gm="G-Max Rapid Flow"
            if "Inteleon" in self.name:
                gm="G-Max Hydrosnipe"
            if "Kingler" in self.name:
                gm="G-Max Foam Burst"
            if "Blastoise" in self.name:
                gm="G-Max Cannonade"
        if i in typem.bugmoves:
            gm="Max Flutterby"
            if "Butterfree" in self.name:
                gm="G-Max Befuddle"
        if i in typem.darkmoves:
            gm="Max Darkness"
            if "Grimmsnarl" in self.name:
                gm="G-Max Snooze"
            if "Single" in self.name:
                gm="G-Max One Blow"
        if i in typem.flyingmoves:
            gm="Max Airstream"
            if "Corviknight" in self.name:
                gm="G-Max Wind Rage"
        if i in typem.firemoves:
            gm="Max Flare"
            if "Charizard" in self.name:
                gm="G-Max Wildfire"
            if "Cinderace" in self.name:
                gm="G-Max Fireball"
            if "Centiskorch" in self.name:
                gm="G-Max Centiferno"
        maxmove.append(gm)
    return maxmove
def rename(self):
    if self.dmax is True and ("Mega " not in self.name or "Z-Crystal" not in self.name):
        if self.name in ["Charizard","Blastoise","Venusaur","Pikachu","Butterfree","Snorlax","Machamp","Gengar","Kingler","Lapras","Garbodor","Melmetal","Rillaboom","Cinderace","Inteleon","Corviknight","Orbeetle","Drednaw","Coalossal","Copperajah","Flapple","Appletun","Sandaconda","Grimmsnarl","Hatterene","Toxtricity","Centiskorch","Alcremie","Duraludon","Single Strike Urshifu","Rapid Strike Urshifu","Centiskorch"]:
            self.name="Gigantamax "+self.name
        if "Toxtricity" in self.name:
            self.name="Gigantamax Toxtricity"
        if "Gigantamax " not in self.name:
            self.name="Dynamax "+self.name
def zmove(mon):
    tp=""
    ch=random.randint(1,2)
    if mon is None:
        return ["Breakneck Blitz "]
    if ch==1:
        tp=mon.type1
    if ch==2:
        if mon.type2 is None:
            tp=mon.type1
        else:
            tp=mon.type2       
    if "eon" in mon.name and "Last Resort" in mon.moves:
        mon.item="Eevium Z"
        return ["Extreme Evoboost"]
    elif "Necrozma" in mon.name and "Photon Geyser" in mon.moves:
        mon.item="Ultranecrozium Z"
        return ["Light That Burns The Sky"]
    elif "Tapu" in mon.name and "Nature's Madness" in mon.moves:
        mon.item="Tapunium Z"
        return ["Guardian of Alola"]
    elif "Solgaleo" in mon.name and "Sunsteel Strike" in mon.moves:
        mon.item="Solganium Z"
        return ["Searing Sunraze Smash"]
    elif "Primarina" in mon.name and "Sparkling Aria" in mon.moves:
        mon.item="Primarium Z"
        return ["Oceanic Operetta"]
    elif "Pikachu" in mon.name:
        if "Thunderbolt" in mon.moves:
            mon.item="Pikashunium Z"
            return ["10,000,000 Volt Thunderbolt"]
        elif "Volt Tackle" in mon.moves:
            mon.item="Pikanium Z"
            return ["Catastropika"]
    elif "Mimikyu" in mon.name and "Play Rough" in mon.moves:
        mon.item="Mimikium Z"
        return ["Let's Snuggle Forever"]
    elif "Marshadow" in mon.name and "Spectral Thief" in mon.moves:
        mon.item="Marshadium Z"
        return ["Soul-Stealing 7-Star Strike"]  
    elif "Lunala" in mon.name and "Moongeist Beam" in mon.moves:
        mon.item="Lunalium Z"
        return ["Menacing Moonraze Maelstrom"]
    elif "Kommo" in mon.name and "Clanging Scales" in mon.moves:
        mon.item="Kommonium Z"
        return ["Clangorous Soulblaze"]
    elif "Incineroar" in mon.name and "Darkest Lariat" in mon.moves:
        mon.item="Incinum Z"
        return ["Malicious Moonsault"]
    elif "Decidueye" in mon.name and "Spirit Shackle" in mon.moves:
        mon.item="Decidium Z"
        return ["Sinister Arrow Raid"]
    elif "Alolan Raichu" in mon.name and "Thunderbolt" in mon.moves:
        mon.item="Aloraichium Z"
        return ["Stoked Sparksurfer"]
    elif "Mew" in mon.name and "Psychic" in mon.moves:
        mon.item="Mewnium Z"
        return ["Genesis Supernova"]
    elif "Snorlax" in mon.name and "Giga Impact" in mon.moves:
        mon.item="Snorlium Z"
        return ["Pulverizing Pancake"]
    elif "Lycanroc" in mon.name and "Stone Edge" in mon.moves:
        mon.item="Lycanium Z"
        return ["Splintered Stromshards"]        
    elif tp=="Fire":
        mon.item="Firium Z"
        return ["Inferno Overdrive"]
    elif tp=="Water":
        mon.item="Waterium Z"
        return ["Hydro Vortex"]
    elif tp=="Poison":
        mon.item="Poisonium Z"
        return ["Acid Downpour"]
    elif tp=="Fighting":
        mon.item="Fightinium Z"
        return ["All-Out Pummeling"]
    elif tp=="Dark":
        mon.item="Darkium Z"
        return ["Black Hole Eclipse"]
    elif tp=="Grass":
        mon.item="Grassium Z"
        return ["Bloom Doom"]
    elif tp=="Normal":
        mon.item="Normalium Z"
        return ["Breakneck Blitz"]
    elif tp=="Rock":
        mon.item="Rockium Z"
        return ["Continental Crush"]
    elif tp=="Steel":
        mon.item="Steelium Z"
        return ["Corkscrew Crash"]
    elif tp=="Dragon":
        mon.item="Dragonium Z"
        return ["Devastating Drake"]
    elif tp=="Psychic":
        mon.item="Pychium Z"
        return ["Shattered Psyche"]
    elif tp=="Electric":
        mon.item="Electrium Z"
        return ["Gigavolt Havoc"]
    elif tp=="Ghost":
        mon.item="Ghostium Z"
        return ["Never-ending Nightmare"]
    elif tp=="Bug":
        mon.item="Buginium Z"
        return ["Savage Spin-Out"]
    elif tp=="Ice":
        mon.item="Icium Z"
        return ["Subzero Slammer"]
    elif tp=="Ground":
        mon.item="Groundium Z"
        return ["Tectonic Rage"]
    elif tp=="Fairy":
        mon.item="Fairium Z"
        return ["Twinkle Tackle"]
    elif tp=="Flying":
        mon.item="Flyinium Z"   
        return ["Supersonic Skystrike"]                    

        
#Venusaur
class Venusaur(Pokemon2):
    "Venusaur"
    def __init__(self,name="Venusaur",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=82,defense=83,spatk=100,spdef=100,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Overgrow","Chlorophyll"]),item=random.choice(["Black Sludge","Life Orb","Grass Gem","Poison Gem"])):
        if move is None:
            ch=random.randint(1,2)
            if ch==1:
                moves=["Giga Drain","Earth Power","Sludge Bomb","Solar Beam","Sleep Powder","Leech Seed","Frenzy Plant","Synthesis"]
                moves=moveset(moves)
            if ch==2:
                moves=["Earthquake","Sleep Powder","Giga Drain","Sludge Bomb"]
                nature="Modest"
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
class Charizard(Pokemon2):
    "Charizard"
    def __init__(self,name="Charizard",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=84,defense=78,spatk=109,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Blaze","Solar Power"]),item=random.choice(["Heavy-Duty Boots","Life Orb","Fire Gem"]),dmax=False):
        if move is None:
            ch=random.randint(1,3)
            if ch==1:
                avmoves=["Flare Blitz","Dragon Dance","Dragon Claw","Roost","Flamethrower","Fire Blast","Blast Burn","Air Slash","Dragon Pulse","Thunder Punch","Ancient Power","Scale Shot"]
                moves=moveset(avmoves)
            if ch==2:
                moves=["Roost","Flamethrower","Airslash","Fire Blast"]
            if ch==3:
                moves=["Dragon Dance","Flare Blitz","Thunder Punch","Dragon Claw"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,dmax=dmax)
class Blastoise(Pokemon2):
    "Blastoise"
    def __init__(self,name="Blastoise",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=79,atk=83,defense=100,spatk=85,spdef=105,speed=78,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Torrent","Rain Dish"]),item=random.choice(["Sitrus Berry","Life Orb","Water Gem"])):
        if move is None:
            avmoves=["Hydro Pump","Shell Smash","Flip Turn","Hydro Cannon","Skull Bash","Rapid Spin","Aura Sphere","Water Spout","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#mBeedrill
class MBeedrill(Pokemon2):
    "Mega Beedrill"
    def __init__(self,name="Mega Beedrill",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=65,atk=150,defense=40,spatk=15,spdef=80,speed=145,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Beedrillite"):
        if move is None:
            ch=random.randint(1,2)
            if ch==1:
                moves=["Poison Jab","Knock Off","Sludge Bomb","Drill Run","Toxic Spikes","U-Turn"]
                moves=moveset(moves)
            if ch==2:
                moves=["U-Turn","Poison Jab","Drill Run","Knock Off"]
                nature="Jolly"
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Nidoqueen
class Nidoqueen(Pokemon2):
    "Nidoqueen"
    def __init__(self,name="Nidoqueen",type1="Poison",type2="Ground",nature=None,level=100,happiness=255,hp=90,atk=92,defense=87,spatk=75,spdef=85,speed=76,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Poison Touch"]),item=random.choice(["Black Sludge","Life Orb"])):
        if move is None:
            ch=random.randint(1,2)
            if ch==1:
                moves=["Ice Beam","Earth Power","Sludge Bomb","Strength","Poison Jab","Toxic Spikes","Taunt","Toxic","Stealth Rock"]
                moves=moveset(moves)
            if ch==2:
                moves=["Stealth Rock","Earth Power","Sludge Wave","Ice Beam"]
                nature="Timid"
                item="Life Orb"
                ability="Sheer Force"
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
        
        
#Nidoking
class Nidoking(Pokemon2):
    "Nidoking"
    def __init__(self,name="Nidoking",type1="Poison",type2="Ground",nature=None,level=100,happiness=255,hp=81,atk=102,defense=77,spatk=85,spdef=75,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Poison Touch"]),item=random.choice(["Black Sludge","Life Orb"])):
        if move is None:
            ch=random.randint(1,2)
            if ch==1:
                moves=["Ice Beam","Earth Power","Sludge Bomb","Strength","Poison Jab","Toxic Spikes"]
                moves=moveset(moves)
            if ch==2:
                moves=["Sludge Wave","Earth Power","Ice Beam","Taunt"]
                nature="Timid"
                item="Life Orb"
                ability="Sheer Force"
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Ninetales
class Ninetales(Pokemon2):
    "Ninetales"
    def __init__(self,name="Ninetales",type1="Fire",type2=None,    nature=None,level=100,happiness=255,hp=73,atk=76,defense=75,spatk=81,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Drought"]),item=random.choice(["Heat Rock","Life Orb","Fire Gem"])):
        if move is None:
            avmoves=["Fire Blast","Flamethrower","Solar Beam","Hidden Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Alolan Ninetales
class ANinetales(Pokemon2):
    "Alolan Ninetales"
    def __init__(self,name="Alolan Ninetales",type1="Ice",type2="Fairy",    nature=None,level=100,happiness=255,hp=73,atk=67,defense=75,spatk=81,spdef=100,speed=109,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Snow Warning","Snow Cloak","Serene Grace"]),item=random.choice(["Icy Rock","Light Clay","Ice Gem","Fairy Gem"])):
        if move is None:
            avmoves=["Ice Beam","Moonblast","Hidden Power","Dazzling Gleam","Aurora Veil"]
            moves=moveset(avmoves)
            
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Golduck
class Golduck(Pokemon2):
    "Golduck"
    def __init__(self,name="Golduck",type1="Water",type2="Psychic",    nature=None,level=100,happiness=255,hp=80,atk=82,defense=78,spatk=100,spdef=80,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Neuroforce","Swift Swim","Cloud Nine"]),item=random.choice(["Leftovers","Life Orb"])):
        if move is None:
            avmoves=["Ice Beam","Psychic","Hydro Pump","Hidden Power","Rain Dance","Nasty Plot","Power Gem","Chilling Water"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Primeape
class Primeape(Pokemon2):
    "Primeape"
    def __init__(self,name="Primeape",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=65,atk=105,defense=60,spatk=60,spdef=70,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Gorilla Tactics",item=random.choice(["Choice Scarf","Life Orb"])):
        if move is None:
            avmoves=["Hidden Power","Dynamic Punch","Close Combat","Superpower","Fire Punch","U-Turn","Cross Chop","Skull Bash","Rage Fist"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Anihilape
class Anihilape(Pokemon2):
    def __init__(self,name="Annihilape",type1="Fighting",type2="Ghost",nature=None,level=100,happiness=255,hp=110,atk=115,defense=80,spatk=50,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Defiant","Inner Focus","Vital Spirit"]),item=random.choice(["Choice Scarf","Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Drain Punch","Close Combat","Superpower","Fire Punch","U-Turn","Cross Chop","Shadow Claw","Shadow Sneak","Final Gambit","Bulk Up","Rest","Taunt"]
            moves=moveset(avmoves,3)+["Rage Fist"]
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
        
#Arcanine
class Arcanine(Pokemon2):
    "Arcanine"
    def __init__(self,name="Arcanine",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=90,atk=110,defense=80,spatk=100,spdef=80,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Flash Fire"]),item=random.choice(["Heavy-Duty Boots","Life Orb"])):
        if move is None:
            ch=random.randint(1,2)
            if ch==1:
                moves=["Hidden Power","Fire Blast","Flamethrower","Sunny Day","Solar Beam","Flare Blitz","Wild Charge","Morning Sun","Extreme Speed"]
                moves=moveset(moves)
            if ch==2:
                moves=["Flare Blitz","Wild Charge","Extreme Speed","Morning Sun"]
                nature="Jolly"
                item="Life Orb"
                ability="Flash Fire"
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
        
#Poliwrath
class Poliwrath(Pokemon2):
    "Poliwrath"
    def __init__(self,name="Poliwrath",type1="Water",type2="Fighting",nature=None,level=100,happiness=255,hp=90,atk=95,defense=95,spatk=70,spdef=90,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Water Absorb",item=random.choice(["Choice Band","Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Dynamic Punch","Thunder Punch","Rain Dance","Submission","Darkest Lariat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Pidgeot 
class MPidgeot(Pokemon2):
    "Mega Pidgeot"
    def __init__(self,name="Mega Pidgeot",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=83,atk=80,defense=80,spatk=135,spdef=80,speed=121,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="No Guard",item="Pidgeotite"):
        if move is None:
            ch=random.randint(1,2)
            if ch==1:
                moves=["Hidden Power","Hurricane","Dual Wingbeat","Brave Bird","U-Turn","Roost","Double-Edge","Heat Wave"]
                moves=moveset(moves)
            if ch==2:
                moves=["U-Turn","Hurricane","Heat Wave","Roost"]
                nature="Timid"
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Pidgeot        
class Pidgeot(Pokemon2):
    "Pidgeot"
    def __init__(self,name="Pidgeot",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=83,atk=80,defense=75,spatk=70,spdef=70,speed=101,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tangled Feet","Frisk"]),item=random.choice(["Choice Band","Life Orb","Flying Gem"])):
        if move is None:
            avmoves=["Hidden Power","Hurricane","Dual Wingbeat","Brave Bird","U-Turn","Roost","Tailwind","Heat Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Alakazam
class Alakazam(Pokemon2):
    "Alakazam"
    def __init__(self,name="Alakazam",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=55,atk=50,defense=45,spatk=135,spdef=95,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Magic Guard","Inner Focus"]),item="Focus Sash"):
        if move is None:
            avmoves=["Hidden Power","Recover","Dazzling Gleam","Shadow Ball","Nasty Plot","Dark Pulse","Focus Blast","Expanding Force","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Beheeyem
class Beheeyem(Pokemon2):
    def __init__(self,name="Beheeyem",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=95,atk=75,defense=75,spatk=125,spdef=95,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Analytic","Synchronize"]),item="Focus Sash"):
        if move is None:
            avmoves=["Hidden Power","Recover","Shadow Ball","Nasty Plot","Dark Pulse","Focus Blast","Expanding Force","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Ajjimajji
class Ajjimajji(Pokemon2):
    def __init__(self,name="Ajjimajji",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=120,atk=50,defense=45,spatk=95,spdef=135,speed=55,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Magic Guard","Levitate"]),item="Focus Sash"):
        if move is None:
            avmoves=["Hidden Power","Recover","Dazzling Gleam","Shadow Ball","Calm Mind","Dark Pulse","Focus Blast","Expanding Force","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                      
#Mega  Alakazam
class MAlakazam(Pokemon2):
    "Mega Alakazam"
    def __init__(self,name="Mega Alakazam",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=55,atk=50,defense=65,spatk=175,spdef=105,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Trace",item="Alakazite"):
        if move is None:
            ch=random.randint(1,2)
            if ch==1:
                moves=["Hidden Power","Recover","Dazzling Gleam","Shadow Ball","Nasty Plot","Dark Pulse","Focus Blast","Expanding Force","Psychic"]
                moves=moveset(moves)
            if ch==2:
                moves=["Psychic","Focus Blast","Recover","Shadow Ball"]
                nature="Timid"
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Machamp
class Machamp(Pokemon2):
    "Machamp"
    def __init__(self,name="Machamp",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=90,atk=130,defense=80,spatk=65,spdef=85,speed=55,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["No Guard","Guts"]),item=random.choice(["Choice Band","Black Belt"])):
        if move is None:
            avmoves=["Dynamic Punch","Close Combat","Superpower","Fire Punch","Cross Chop","Submission","Darkest Lariat"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Machug
class Machug(Pokemon2):
    def __init__(self,name="Machug",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=110,atk=130,defense=90,spatk=65,spdef=75,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Thick Fat","Guts"]),item=random.choice(["Choice Band","Black Belt","Sitrus Berry"])):
        if move is None:
            avmoves=["Close Combat","Superpower","Fire Punch","Cross Chop","Submission","Belly Drum"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                             
#Victreebel
class Victreebel(Pokemon2):
    "Victreebel"
    def __init__(self,name="Victreebel",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=105,defense=70,spatk=100,spdef=75,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Gluttony"]),item=random.choice(["Rocky Helmet","Black Sludge"])):
        if move is None:
            avmoves=["Power Whip","Sludge Bomb","Sleep Powder","Solar Beam","Toxic","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Bustoliv
class Bustoliv(Pokemon2):
    def __init__(self,name="Bustoliv",type1="Grass",type2="Normal",nature=None,level=100,happiness=255,hp=60,atk=45,defense=80,spatk=90,spdef=105,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Chlorophyll",item=random.choice(["Rocky Helmet","Miracle Seed"])):
        if move is None:
            avmoves=["Sleep Powder","Solar Beam","Synthesis","Sunny Day","Giga Drain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Tentacruel
class Tentacruel(Pokemon2):
    "Tentacruel"
    def __init__(self,name="Tentacruel",type1="Water",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=60,defense=80,spatk=90,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move=None, ability=random.choice(["Clear Body","Liquid Ooze","Rain Dish"]),item="Black Sludge"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Sludge Bomb","Poison Jab","Rain Dance","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Toedscruel
class Toedscruel(Pokemon2):
    def __init__(self,name="Toedscruel",type1="Grass",type2="Ground",nature=None,level=100,happiness=255,hp=80,atk=60,defense=80,spatk=90,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move=None, ability="Effect Spore",item="Black Sludge"):
        if move is None:
            avmoves=["Hidden Power","Earth Power","Giga Drain","Bulldoze","Sludge Bomb","Poison Jab","Sunny Day","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Doncrete
class Doncrete(Pokemon2):
    def __init__(self,name="Doncrete",type1="Rock",type2="Ground",nature=None,level=100,happiness=255,hp=70,atk=110,defense=120,spatk=55,spdef=75,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Rock Head","Dark Mind"]),item=random.choice(["Weakness Policy"])):
        if move is None:
            avmoves=["Stone Edge","Earthquake","Stealth Rock","Rock Blast","Night Slash","Magnitude","Bulldoze","Foul Play"]
            moves=moveset(avmoves)
        else:
            moves=move
        if "Explosion" in moves:
            ability="Sturdy"
            item="Custap Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Golem
class Golem(Pokemon2):
    "Golem"
    def __init__(self,name="Golem",type1="Rock",type2="Ground",nature=None,level=100,happiness=255,hp=80,atk=120,defense=130,spatk=55,spdef=65,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Rock Head","Sturdy"]),item=random.choice(["Weakness Policy"])):
        if move is None:
            avmoves=["Stone Edge","Earthquake","Stealth Rock","Rock Blast","Explosion","Magnitude","Bulldoze"]
            moves=moveset(avmoves)
        else:
            moves=move
        if "Explosion" in moves:
            ability="Sturdy"
            item="Custap Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Golem
class AGolem(Pokemon2):
    "Alolan Golem"
    def __init__(self,name="Alolan Golem",type1="Rock",type2="Electric",nature=None,level=100,happiness=255,hp=80,atk=120,defense=130,spatk=55,spdef=65,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Galvanize","Sturdy","Magnet Pull","Rock Head"]),item=random.choice(["Choice Scarf","Weakness Policy"])):
        if move is None:
            avmoves=["Stone Edge","Earthquake","Stealth Rock","Rock Blast","Thunderbolt","Explosion","Magnitude","Bulldoze"]
            moves=moveset(avmoves)
        else:
            moves=move
        if "Explosion" in moves:
            ability="Sturdy"
            item="Custap Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Rapidash
class Rapidash(Pokemon2):
    "Rapidash"
    def __init__(self,name="Rapidash",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=65,atk=100,defense=70,spatk=80,spdef=80,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Reckless","Blazing Soul"]),item=random.choice(["Choice Band","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Fire Blast","Flamethrower","Flare Blitz","Inferno","Morning Sun","Sunny Day","High Horsepower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Slowbro
class Slowbro(Pokemon2):
    "Slowbro"
    def __init__(self,name="Slowbro",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=75,defense=110,spatk=100,spdef=80,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item=random.choice(["Colbur Berry","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Hydro Pump","Thunderbolt","Iron Defense","Rain Dance","Rest","Expanding Force","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Slowbro
class MSlowbro(Pokemon2):
    "Mega Slowbro"
    def __init__(self,name="Mega Slowbro",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=75,defense=180,spatk=130,spdef=80,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Regenerator","Shell Armor"]),item="Slowbronite"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Hydro Pump","Thunderbolt","Iron Defense","Body Press","Rest","Expanding Force","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Dodrio
class Dodrio(Pokemon2):
    "Dodrio"
    def __init__(self,name="Dodrio",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=110,defense=70,spatk=60,spdef=60,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Rock Head","Early Bird","Tangled Feet"]),item=random.choice(["Choice Scarf","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Close Combat","Brave Bird","Roost","Sky Attack","High Jump Kick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
        
#Garbodor
class Garbodor(Pokemon2):
    def __init__(self,name="Garbodor",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=80,atk=115,defense=82,spatk=60,spdef=82,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Aftermath","Stench"]),item=random.choice(["Black Sludge","Shuca Berry","Payapa Berry"])):
        if move is None:
            avmoves=["Poison Jab","Acid Armor","Toxic","Sludge Bomb","Venoshock","Toxic Spikes","Explosion","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Muk
class Muk(Pokemon2):
    "Muk"
    def __init__(self,name="Muk",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=105,atk=105,defense=75,spatk=65,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Poison Touch","Regenerator","Sticky Hold"]),item=random.choice(["Black Sludge","Shuca Berry","Payapa Berry"])):
        if move is None:
            avmoves=["Poison Jab","Acid Armor","Toxic","Sludge Bomb","Venoshock","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
#Cloyster
class Cloyster(Pokemon2):
    "Cloyster"
    def __init__(self,name="Cloyster",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=50,atk=95,defense=180,spatk=85,spdef=45,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Skill Link","Shell Armor","Overcoat"]),item=random.choice(["Focus Sash","King's Rock"])):
        if move is None:
            avmoves=["Ice Beam","Rock Blast","Icicle Spear","Shell Smash","Hydro Pump","Pin Missile","Snowscape"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                               
#Gengar
class Gengar(Pokemon2):
    "Gengar"
    def __init__(self,name="Gengar",type1="Ghost",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=65,defense=60,spatk=130,spdef=75,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Black Sludge"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Dazzling Gleam","Psychic","Shadow Ball","Dark Pulse","Thunderbolt","Nasty Plot","Destiny Bond","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Dangal
class Dangal(Pokemon2):
    def __init__(self,name="Dangal",type1="Ghost",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=85,defense=70,spatk=110,spdef=75,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Black Glasees"):
        if move is None:
            avmoves=["Hidden Power","Shadow Ball","Dark Pulse","Nasty Plot","Destiny Bond","Night Daze","Leech Life"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
        #Mega Gengar
class MGengar(Pokemon2):
    "Mega Gengar"
    def __init__(self,name="Mega Gengar",type1="Ghost",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=65,defense=80,spatk=170,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=253,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shadow Tag",item="Gengarite"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Dazzling Gleam","Psychic","Shadow Ball","Dark Pulse","Thunderbolt","Nasty Plot","Destiny Bond","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Exeggutor
class Exeggutor(Pokemon2):
    "Exeggutor"
    def __init__(self,name="Exeggutor",type1="Grass",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=95,defense=85,spatk=125,spdef=75,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item=random.choice(["Lum Berry","Leftovers"])):
        if move is None:
            avmoves=["Hidden Power","Giga Drain","Sunny Day","Psychic","Solar Beam","Egg Bomb","Leech Seed","Morning Sun","Light Screen","Expanding Force","Weather Ball","Psyshock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Alolan Exeggutor
class AExeggutor(Pokemon2):
    "Alolan Exeggutor"
    def __init__(self,name="Alolan Exeggutor",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=95,atk=105,defense=85,spatk=125,spdef=75,speed=45,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Harvest"]),item="Leftovers"):
        if move is None:
            avmoves=["Sunny Day","Egg Bomb","Psychic","Solar Beam","Dragon Hammer","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Alolan Muk
class AMuk(Pokemon2):
    "Alolan Muk"
    def __init__(self,name="Alolan Muk",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=105,atk=105,defense=75,spatk=65,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Power of Alchemy","Poison Touch"]),item="Black Sludge"):
        if move is None:
            avmoves=["Sludge Bomb","Toxic","Poison Jab","Venoshock","Smocksceen","Toxic Spikes","Drain Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Hitmonlee
class Hitmonlee(Pokemon2):
    "Hitmonlee"
    def __init__(self,name="Hitmonlee",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=50,atk=120,defense=53,spatk=35,spdef=110,speed=87,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Reckless","Limber","Striker","Unburden"]),item=random.choice(["Choice Band","Assault Vest"])):
        if move is None:
            avmoves=["Blaze Kick","High Jump Kick","Superpower","Pyro Ball","Low Kick","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Hitmontop
class Hitmontop(Pokemon2):
    def __init__(self,name="Hitmontop",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=50,atk=95,defense=95,spatk=35,spdef=110,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Technician"]),item=random.choice(["Choice Band","Assault Vest"])):
        if move is None:
            avmoves=["Triple Kick","Sucker Punch","Superpower","Gyro Ball","Low Kick","Close Combat","Rapid Spin"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Hitmonchan
class Hitmonchan(Pokemon2):
    "Hitmonchan"
    def __init__(self,name="Hitmonchan",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=50,atk=115,defense=79,spatk=35,spdef=110,speed=76,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Iron Fist",item=random.choice(["Assault Vest","Choice Band","Punching Glove"])):
        if move is None:
            avmoves=["Ice Punch","Thunder Punch","Mach Punch","Fire Punch","Dizzy Punch","Dynamic Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Weezing
class Weezing(Pokemon2):
    "Weezing"
    def __init__(self,name="Weezing",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=65,atk=90,defense=120,spatk=85,spdef=70,speed=60,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Levitate",item=random.choice(["Black Sludge","Rocky Helmet"])):
        if move is None:
            avmoves=["Sludge Bomb","Toxic","Poison Jab","Venoshock","Explosion","Toxic Spikes","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Kangaskhan
class Kangaskhan(Pokemon2):
    "Kangaskhan"
    def __init__(self,name="Kangaskhan",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=105,atk=95,defense=80,spatk=40,spdef=80,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Scrappy",item=random.choice(["Silk Scarf","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Crunch","Body Slam","Fake Out","Power-Up Punch","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Kangaskhan
class MKangaskhan(Pokemon2):
    "Mega Kangaskhan"
    def __init__(self,name="Mega Kangaskhan",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=105,atk=125,defense=100,spatk=60,spdef=100,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Parental Bond",item="Kangaskhanite"):
        if move is None:
            avmoves=["Crunch","Body Slam","Fake Out","Power-Up Punch","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Starmie
class Starmie(Pokemon2):
    "Starmie"
    def __init__(self,name="Starmie",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=75,defense=85,spatk=100,spdef=85,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Natural Cure",item=random.choice(["Life Orb","Sitrus Berry","Mystic Water"])):
        if move is None:
            avmoves=["Meteor Beam","Hidden Power","Ice Beam","Scald","Psychic","Surf","Hydro Pump","Thunderbolt","Flip Turn","Recover","Rapid Spin"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Pinsir
class Pinsir(Pokemon2):
    "Pinsir"
    def __init__(self,name="Pinsir",type1="Bug",type2=None,nature=None,level=100,happiness=255,hp=65,atk=125,defense=100,spatk=55,spdef=70,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Moxie",item="Life Orb"):
        if move is None:
            avmoves=["Megahorn","Return","Brick Break","Close Combat","Submission"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Pinsir
class MPinsir(Pokemon2):
    "Mega Pinsir"
    def __init__(self,name="Mega Pinsir",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=155,defense=120,spatk=65,spdef=90,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Aerilate",item="Pinsirite"):
        if move is None:
            avmoves=["Double-Edge","Megahorn","Return","Brick Break","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Dubwool
class Dubwool(Pokemon2):
    def __init__(self,name="Dubwool",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=82,atk=80,defense=100,spatk=60,spdef=90,speed=88,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Fluffy","Bulletproof","Steadfast"]),item="Leftovers"):
        if move is None:
            avmoves=["Double-Edge","Strength","Earthquake","Drill Run","Head Smash","Megahorn","Rest","Head Charge","Cotton Guard"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Tauros
class Tauros(Pokemon2):
    "Tauros"
    def __init__(self,name="Tauros",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=75,atk=100,defense=95,spatk=70,spdef=70,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Sheer Force"]),item="Life Orb"):
        if move is None:
            avmoves=["Double-Edge","Strength","Earthquake","Drill Run","Head Smash","Megahorn","Rest","Head Charge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Tauros
class PTauros(Pokemon2):
    def __init__(self,name="Paldean Tauros",type1="Fighting",type2=random.choice([None,"Fire","Water"]),nature=None,level=100,happiness=255,hp=75,atk=110,defense=105,spatk=30,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Anger Point"]),item="Life Orb"):
        if move is None:
            avmoves=["Close Combat","Strength","Earthquake","Zen Headbutt","Head Smash","Megahorn","Rest","Head Charge","Drill Run","Raging Bull"]
            if type2==None:
                moves=moveset(avmoves,3)+["Doube-Edge"]
            if type2=="Fire":
                moves=moveset(avmoves,3)+["Flare Blitz"]
            if type2=="Water":
                moves=moveset(avmoves,3)+["Wave Crash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Gyarados
class Gyarados(Pokemon2):
    "Gyarados"
    def __init__(self,name="Gyarados",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=125,defense=79,spatk=60,spdef=100,speed=81,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item=random.choice(["Mystic Water","Heavy-Duty Boots","Lum Berry"])):
        if move is None:
            avmoves=["Crunch","Waterfall","Dragon Dance","Earthquake","Aqua Tail","Ice Fang","Power Whip","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Gyarados
class MGyarados(Pokemon2):
    "Mega Gyarados"
    def __init__(self,name="Mega Gyarados",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=95,atk=155,defense=109,spatk=70,spdef=130,speed=81,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mold Breaker",item="Gyaradosite"):
        if move is None:
            avmoves=["Crunch","Waterfall","Dragon Dance","Earthquake","Aqua Tail","Ice Fang","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Lapras
class Lapras(Pokemon2):
    "Lapras"
    def __init__(self,name="Lapras",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=130,atk=85,defense=80,spatk=85,spdef=95,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Water Absorb",item=random.choice(["Choice Specs","Heavy-Duty Boots"]),dmax=False):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Snowscape","Rain Dance","Aurora Veil"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,dmax=dmax)

#Omastar
class Omastar(Pokemon2):
    "Omastar"
    def __init__(self,name="Omastar",type1="Rock",type2="Water",nature=None,level=100,happiness=255,hp=70,atk=60,defense=125,spatk=115,spdef=70,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Shell Armor","Swift Swim","Weak Armor"]),item=random.choice(["Power Herb","Mystic Water"])):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Ancient Power","Rock Blast","Stealth Rock","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        if "Meteor Beam" in moves:
            item="Power Herb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Kabutops
class Kabutops(Pokemon2):
    "Kabutops"
    def __init__(self,name="Kabutops",type1="Rock",type2="Water",nature=None,level=100,happiness=255,hp=60,atk=115,defense=105,spatk=65,spdef=70,speed=80,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Swift Swim","Sharpness"]),item=random.choice(["Choice Band","Life Orb"])):
        if move is None:
            avmoves=["Protect","Liquidation","Hydro Pump","Rock Slide","Stone Edge","Flip Turn","Stealth Rock","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                  
#Aerodactyl
class Aerodactyl (Pokemon2):
    "Aerodactyl"
    def __init__(self,name="Aerodactyl",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=105,defense=65,spatk=60,spdef=75,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Rock Head",item=random.choice(["Flying Gem","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Ancient Power","Stone Edge","Rock Slide","Brave Bird","Stealth Rock","Meteor Beam","Taunt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Mega  Aerodactyl
class MAerodactyl (Pokemon2):
    "Mega Aerodactyl"
    def __init__(self,name="Mega Aerodactyl",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=135,defense=85,spatk=70,spdef=95,speed=150,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Aerodactylite"):
        if move is None:
            avmoves=["Protect","Ancient Power","Stone Edge","Rock Slide","Brave Bird","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Snorlax
class Snorlax(Pokemon2):
    "Snorlax"
    def __init__(self,name="Snorlax",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=160,atk=110,defense=65,spatk=65,spdef=110,speed=30,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Thick Fat","Immunity"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Beam","Body Slam","Thunder Punch","Double-Edge","Hyper Beam","Giga Impact","Rest","Metronome","Darkest Lariat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Articuno
class Articuno(Pokemon2):
    "Articuno"
    def __init__(self,name="Articuno",type1="Ice",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=70,defense=100,spatk=95,spdef=125,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Blizzard","Freeze-Dry","Brave Bird","Sky Attack","Roost","Tailwind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Zapdos
class Zapdos(Pokemon2):
    "Zapdos"
    def __init__(self,name="Zapdos",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=90,defense=85,spatk=125,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Drizzle","Static"]),item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Thunder","Brave Bird","Thunderbolt","Sky Attack","Roost","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Moltres
class Moltres(Pokemon2):
    "Moltres"
    def __init__(self,name="Moltres",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=100,defense=90,spatk=125,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Drought","Flame Body"]),item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Flamethrower","Hurricane","Heat Wave","Sky Attack","Brave Bird","Fire Blast","Roost","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Baxcalibur
class Baxcalibur (Pokemon2):
    def __init__(self,name="Baxcalibur",type1="Ice",type2="Dragon",nature=None,level=100,happiness=255,hp=115,atk=145,defense=92,spatk=75,spdef=86,speed=87,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Ice Body","Thermal Exchange"]),item=random.choice(["Weakness Policy","Leftovers","Choice Band","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Ice Beam","Icicle Crash","Dragon Claw","Double-Edge","Thunder Wave","Mountain Gale","Snowscape"]  
            moves=moveset(avmoves,3)+["Glaive Rush"]          
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev,ability=ability,item=item)
#Dragonite
class Dragonite(Pokemon2):
    def __init__(self,name="Dragonite",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=91,atk=134,defense=95,spatk=100,spdef=100,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Multiscale","Inner Focus"]),item=random.choice(["Weakness Policy","Leftovers","Choice Band","Heavy-Duty Boots"])):
        if move is None:
            ch=random.randint(1,2)
            if ch==1:
                avmoves=["Protect","Ice Beam","Hydro Pump","Thunderbolt","Surf","Dragon Claw","Double-Edge","Thunder Wave","Dual Wingbeat","Roost","Extreme Speed","Scale Shot","Dragon Dance"]
                moves=moveset(avmoves)
            if ch==2:
                moves=["Swords Dance","Extreme Speed","Dragon Claw","Roost"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
            
#Mewtwo
class Mewtwo(Pokemon2):
    "Mewtwo"
    def __init__(self,name="Mewtwo",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=106,atk=110,defense=90,spatk=154,spdef=90,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item=random.choice(["Expert Belt","Life Orb"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Shadow Ball","Dark Pulse","Ice Beam","Focus Blast","Expanding Force","Aura Sphere","Power Gem","Earth Power"]
            moves=moveset(avmoves,3)+["Psystrike"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
        
#Mewtwo
class MMewtwoX(Pokemon2):
    "Mewtwo"
    def __init__(self,name="Mega Mewtwo X",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=106,atk=190,defense=100,spatk=154,spdef=100,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item=random.choice(["Mewtwonite X"])):
        if move is None:
            avmoves=["Protect","Zen Headbutt","Psystrike","Shadow Claw","Night Slash","Ice Punch","Fire Punch","Poison Jab","Rock Slide","Thunder Punch","Iron Tail","Brick Break"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mew
class Mew(Pokemon2):
    "Mew"
    def __init__(self,name="Mew",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Synchronize",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Hidden Power","Transform","Psychic","Focus Blast","Aura Sphere"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Venusaur 
class MVenusaur(Pokemon2):
    "Mega Venusaur"
    def __init__(self,name="Mega Venusaur",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=100,defense=123,spatk=122,spdef=120,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat",item="Venusaurite"):
        if move is None:
            ch=random.randint(1,2)
            if ch==1:
                moves=["Giga Drain","Earth Power","Sludge Bomb","Solar Beam","Sleep Powder","Leech Seed","Frenzy Plant"]
                moves=moveset(moves)
            if ch==2:
                moves=["Earthquake","Sleep Powder","Giga Drain","Sludge Bomb"]
                nature="Modest"
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mega Blastoise
class MBlastoise(Pokemon2):
    "Mega Blastoise"
    def __init__(self,name="Mega Blastoise",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=79,atk=103,defense=120,spatk=135,spdef=115,speed=78,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mega Launcher",item="Blastoisinite"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Dark Pulse","Dragon Pulse","Aura Sphere","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Charizard X
class MCharizardX(Pokemon2):
    "Mega Charizard X"
    def __init__(self,name="Mega Charizard X",type1="Fire",type2="Dragon",nature=None,level=100,happiness=255,hp=78,atk=130,defense=111,spatk=130,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Charizardite X"):
        if move is None:
            avmoves=["Protect","Dragon Fance","Dragon Claw","Flare Blitz","Roost","Earthquake","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Mega Charizard Y
class MCharizardY(Pokemon2):
    "Mega Charizard Y"
    def __init__(self,name="Mega Charizard Y",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=104,defense=78,spatk=169,spdef=115,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought",item="Charizardite Y"):
        if move is None:
            avmoves=["Protect","Hidden Power","Fire Blast","Solar Beam","Flamethrower","Earth Power","Focus Blast","Ancient Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Meganium
class Meganium(Pokemon2):
    "Meganium"
    def __init__(self,name="Meganium",type1="Grass",type2="Fairy",nature=None,level=100,happiness=255,hp=80,atk=72,defense=100,spatk=93,spdef=100,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Triage","Overgrow"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Leaf Storm","Moonblast","Dazzling Gleam","Synthesis","Leech Seed","Solar Beam","Frenzy Plant","Light Screen","Draining Kiss","Ancient Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Typhlosion
class Typhlosion(Pokemon2):
    "Typhlosion"
    def __init__(self,name="Typhlosion",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=78,atk=84,defense=78,spatk=109,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Blaze","Blazing Soul"]),item="Choice Specs"):
        if move is None:
            avmoves=["Protect","Hidden Power","Earth Power","Fire Blast","Lava Plume","Eruption","Focus Blast","Blast Burn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Feraligatr
class Feraligatr(Pokemon2):
    "Feraligatr"
    def __init__(self,name="Feraligatr",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=85,atk=105,defense=100,spatk=79,spdef=83,speed=78,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Torrent","Strong Jaw"]),item=random.choice(["Choice Band","Life Orb"])):
        if move is None:
            avmoves=["Protect","Ice Beam","Hydro Pump","Liquidation","Dragon Claw","Hydro Cannon","Ice Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Vaporeon
class Vaporeon(Pokemon2):
    "Vaporeon"
    def __init__(self,name="Vaporeon",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=130,atk=65,defense=60,spatk=110,spdef=95,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Water Absorb",item=random.choice(["Leftovers","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Acid Armor","Surf","Rain Dance","Flip Turn","Chilling Water","Calm Mind","Aqua Ring"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Jolteon
class Jolteon(Pokemon2):
    "Jolteon"
    def __init__(self,name="Jolteon",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=65,atk=65,defense=60,spatk=110,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Volt Absorb",item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Volt Switch","Thunder","Thunderbolt","Shadow Ball","Thunder Wave","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Boltund
class Boltund(Pokemon2):
    def __init__(self,name="Boltund",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=69,atk=100,defense=60,spatk=80,spdef=60,speed=121,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Strong Jaw","Competitive"]),item=random.choice(["Choice Band","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Volt Switch","Play Rough","Thunder Fang","Wild Charge","Thunder Wave","Psychic Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Flareon
class Flareon(Pokemon2):
    "Flareon"
    def __init__(self,name="Flareon",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=65,atk=130,defense=60,spatk=95,spdef=110,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Guts"]),item=random.choice(["Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Flare Blitz","Fire Blast","Flame Charge","Last Resort","Will-O-Wisp","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Toxic Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Crobat
class Crobat(Pokemon2):
    "Crobat"
    def __init__(self,name="Crobat",type1="Poison",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=90,defense=80,spatk=90,spdef=80,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Infiltrator",item=random.choice(["Black Sludge","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Poison Jab","Cross Poison","Dual Wingbeat","Brave Bird","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Lanturn
class Lanturn(Pokemon2):
    "Lanturn"
    def __init__(self,name="Lanturn",type1="Water",type2="Electric",nature=None,level=100,happiness=255,hp=125,atk=58,defense=58,spatk=76,spdef=76,speed=67,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Volt Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Rain Dance","Flip Turn","Volt Switch","Thunder Wave"]
            moves=moveset(avmoves,3)+["Parabolic Charge"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ampharos
class Ampharos(Pokemon2):
    "Amoharos"
    def __init__(self,name="Ampharos",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=90,atk=75,defense=85,spatk=115,spdef=90,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability="Static",item=random.choice(["Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Signal Beam","Power Gem","Thunderbolt","Discharge","Thunder Wave","Focus Blast","Light Screen","Reflect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Mega Ampharos
class MAmpharos(Pokemon2):
    "Mega Amoharos"
    def __init__(self,name="Mega Ampharos",type1="Electric",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=95,defense=105,spatk=165,spdef=110,speed=45,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Mold Breaker","Thick Fat"]),item="Ampharosite"):
        if move is None:
            avmoves=["Protect","Hidden Power","Signal Beam","Power Gem","Thunderbolt","Draco Meteor","Dragon Pulse","Thunder Wave","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Azumarill
class Azumarill(Pokemon2):
    "Azumarill"
    def __init__(self,name="Azumarill",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=100,atk=50,defense=80,spatk=60,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Huge Power",item=random.choice(["Choice Specs","Sitrus Berry"])):
        if move is None:
            avmoves=["Protect","Ice Beam","Aqua Jet","Play Rough","Liquidation","Belly Drum"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Politoed
class Politoed(Pokemon2):
    "Politoed"
    def __init__(self,name="Politoed",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=90,atk=75,defense=75,spatk=90,spdef=100,speed=70,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Drizzle","Damp"]),item=random.choice(["Choice Specs","Water Gem"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Flip Turn","Focus Blast","Belly Drum","Metronome","Scald","Hypnosis"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Drizzle":
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Espeon
class Espeon(Pokemon2):
    "Espeon"
    def __init__(self,name="Espeon",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=65,atk=65,defense=60,spatk=130,spdef=95,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Magic Bounce","Synchronize"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Psychic","Shadow Ball","Dazzling Gleam","Morning Sun","Light Screen","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Meowstic
class Meowstic(Pokemon2):
    def __init__(self,name="Meowstic",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=74,atk=48,defense=76,spatk=63,spdef=81,speed=104,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Feline Prowess","Infiltrator","Prankster"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Psychic","Shadow Ball","Dazzling Gleam","Morning Sun","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Sylveon
class Sylveon (Pokemon2):
    def __init__(self,name="Sylveon",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=95,atk=65,defense=65,spatk=110,spdef=130,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Cute Charm","Pixilate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Moonblast","Hyper Voice","Dazzling Gleam","Mystical Fire","Heal Bell","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                 
#Umbreon
class Umbreon(Pokemon2):
    "Umbreon"
    def __init__(self,name="Umbreon",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=95,atk=65,defense=110,spatk=60,spdef=130,speed=65,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Inner Focus",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Foul Play","Shadow Ball","Dark Pulse","Moonlight","Toxic","Calm Mind","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Steelix
class Steelix(Pokemon2):
    "Steelix"
    def __init__(self,name="Steelix",type1="Steel",type2="Ground",nature=None,level=100,happiness=255,hp=75,atk=85,defense=200,spatk=55,spdef=65,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Tail","Gyro Ball","Earthquake","Stone Edge","Rock Slide","Toxic","Body Press","Stealth Rock","Autotomize"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Steelix
class MSteelix(Pokemon2):
    "Mega Steelix"
    def __init__(self,name="Mega Steelix",type1="Steel",type2="Ground",nature=None,level=100,happiness=255,hp=75,atk=125,defense=230,spatk=55,spdef=95,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Inner Focus","Heatproof"]),item="Steelixite"):
        if move is None:
            avmoves=["Protect","Iron Tail","Gyro Ball","Earthquake","Stone Edge","Rock Slide","Toxic","Body Press","Stealth Rock","Autotomize"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Scizor
class Scizor(Pokemon2):
    "Scizor"
    def __init__(self,name="Scizor",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=130,defense=100,spatk=55,spdef=80,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Iron Head","Bullet Punch","X-Scissor","U-Turn","Roost","Superpower","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Scizor
class MScizor(Pokemon2):
    "Mega Scizor"
    def __init__(self,name="Mega Scizor",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=150,defense=140,spatk=65,spdef=100,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Scizorite"):
        if move is None:
            avmoves=["Protect","Iron Head","Bullet Punch","X-Scissor","U-Turn","Roost","Superpower","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                   
#Heracross
class Heracross(Pokemon2):
    "Heracross"
    def __init__(self,name="Heracross",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=125,defense=75,spatk=40,spdef=95,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts",item="Flame Orb"):
        if move is None:
            avmoves=["Protect","Megahorn","Brick Break","X-Scissor","U-Turn","Close Combat","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Heracross
class MHeracross(Pokemon2):
    "Mega Heracross"
    def __init__(self,name="Mega Heracross",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=185,defense=115,spatk=40,spdef=105,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Skill Link",item="Heracronite"):
        if move is None:
            avmoves=["Protect","Megahorn","Brick Break","X-Scissor","U-Turn","Close Combat","Superpower","Pin Missile"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Skarmory
class Skarmory(Pokemon2):
    "Skarmory"
    def __init__(self,name="Skarmory",type1="Steel",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=80,defense=140,spatk=40,spdef=70,speed=70,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sturdy",item=random.choice(["Leftovers","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Roost","Brave Bird","Stealth Rock","Whirlwind","Steel Wing","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Houndoom
class Houndoom(Pokemon2):
    "Houndoom"
    def __init__(self,name="Houndoom",type1="Dark",type2="Fire",nature=None,level=100,happiness=255,hp=75,atk=90,defense=50,spatk=110,spdef=80,speed=95,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Fire Blast","Dark Pulse","Flamethrower","Inferno","Crunch","Will-O-Wisp","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Houndoom
class MHoundoom(Pokemon2):
    "Mega Houndoom"
    def __init__(self,name="Mega Houndoom",type1="Dark",type2="Fire",nature=None,level=100,happiness=255,hp=75,atk=90,defense=90,spatk=140,spdef=90,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Solar Power","Dark Aura"]),item="Houndoominite"):
        if move is None:
            avmoves=["Protect","Fire Blast","Dark Pulse","Flamethrower","Inferno","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Kingdra
class Kingdra(Pokemon2):
    "Kingdra"
    def __init__(self,name="Kingdra",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=75,atk=95,defense=95,spatk=95,spdef=95,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Swift Swim",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Dragon Pulse","Ice Beam","Surf","Thunder","Hydro Pump","Dragon Dance","Rain Dance","Flip Turn","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Tatsugiri
class Tatsugiri(Pokemon2):
    def __init__(self,name="Tatsugiri",type1="Dragon",type2="Water",nature=None,level=100,happiness=255,hp=68,atk=50,defense=60,spatk=120,spdef=95,speed=82,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Commander",item="Choice Specs"):
        if move is None:
            avmoves=["Protect","Dragon Pulse","Ice Beam","Surf","Thunder","Hydro Pump","Dragon Dance","Rain Dance","Flip Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                             
#Tyranitar
class Tyranitar(Pokemon2):
    "Tyranitar"
    def __init__(self,name="Tyranitar",type1="Rock",type2="Dark",nature=None,level=100,happiness=255,hp=100,atk=134,defense=110,spatk=95,spdef=100,speed=61,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sand Stream",item=random.choice(["Chople Berry","Weakness Policy"])):
        if move is None:
            avmoves=["Protect","Crunch","Earthquake","Stone Edge","Rock Slide","Hyper Beam","Dragon Dance","Giga Impact","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Tyranitar
class UTyranitar(Pokemon2):
    def __init__(self,name="Ultimate Tyranitar",type1="Steel",type2="Dark",nature=None,level=100,happiness=255,hp=90,atk=144,defense=120,spatk=75,spdef=110,speed=71,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Filter",item=random.choice(["Chople Berry"])):
        if move is None:
            avmoves=["Protect","Crunch","Earthquake","Stone Edge","Iron Head","Steel Beam","Dragon Dance","Iron Tail","Stealth Rock","Flamethrower","Smart Strike"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Tyranitar
class MTyranitar(Pokemon2):
    "Mega Tyranitar"
    def __init__(self,name="Mega Tyranitar",type1="Rock",type2="Dark",nature=None,level=100,happiness=255,hp=100,atk=164,defense=150,spatk=95,spdef=120,speed=71,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sand Stream",item="Tyranitarite"):
        if move is None:
            avmoves=["Protect","Crunch","Earthquake","Stone Edge","Rock Slide","Hyper Beam","Dragon Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Raikou
class Raikou(Pokemon2):
    "Raikou"
    def __init__(self,name="Raikou",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=90,atk=85,defense=75,spatk=115,spdef=100,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item=random.choice(["Leftovers","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Crunch","Thunder","Thunderbolt","Wild Charge","Hyper Beam","Rain Dance","Thunder Wave","Extreme Speed","Reflect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Entei
class Entei(Pokemon2):
    "Entei"
    def __init__(self,name="Entei",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=115,atk=115,defense=85,spatk=90,spdef=75,speed=100,hpev=0,atkev=115,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item=random.choice(["Choice Band","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Crunch","Fire Blast","Sacred Fire","Flamethrower","Hyper Beam","Flare Blitz","Eruption","Extreme Speed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Suicune
class Suicune(Pokemon2):
    "Suicune"
    def __init__(self,name="Suicune",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=75,defense=115,spatk=90,spdef=115,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance","Scald","Extreme Speed","Light Screen","Tailwind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Lugia
class Lugia(Pokemon2):
    "Lugia"
    def __init__(self,name="Lugia",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=106,atk=90,defense=130,spatk=90,spdef=154,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Multiscale","Pressure"]),item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance","Aeroblast","Psychic","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ho-Oh
class Hooh(Pokemon2):
    "Ho-Oh"
    def __init__(self,name="Ho-Oh",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=106,atk=130,defense=90,spatk=110,spdef=154,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Regenerator","Pressure"]),item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Recover","Hyper Beam","Sunny Day","Sacred Fire","Fire Blast","Flamethrower","Brave Bird","Heat Wave","Sky Attack"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Celebi
class Celebi(Pokemon2):
    "Celebi"
    def __init__(self,name="Celebi",type1="Grass",type2="Psychic",nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Psychic","Leaf Storm","Future Sight","Perish Song","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Blissey
class Blissey(Pokemon2):
    "Blissey"
    def __init__(self,name="Blissey",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=255,atk=10,defense=10,spatk=75,spdef=135,speed=55,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Soft Boiled","Toxic","Seismic Toss","Light Screen","Reflect","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Deoxys
class Deoxys(Pokemon2):
    "Deoxys"
    def __init__(self,name="Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=150,defense=50,spatk=150,spdef=50,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Kasib Berry"):
        if move is None:
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Attack Deoxys
class ADeoxys(Pokemon2):
    "Attack Deoxys"
    def __init__(self,name="Attack Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=180,defense=20,spatk=180,spdef=20,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psycho Boost","Psychic","Shadow Ball","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Speed Deoxys
class SDeoxys(Pokemon2):
    "Speed Deoxys"
    def __init__(self,name="Speed Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=95,defense=90,spatk=95,spdef=90,speed=180,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave","Toxic Spikes","Stealth Rock","Extreme Speed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Defense Deoxys
class DDeoxys(Pokemon2):
    "Defense Deoxys"
    def __init__(self,name="Defense Deoxys",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=50,atk=70,defense=160,spatk=70,spdef=160,speed=90,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=4,maxiv="No",move=None, ability="Pressure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave","Toxic Spikes","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Jirachi       
class Jirachi(Pokemon2):
    "Jirachi"
    def __init__(self,name="Jirachi",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Serene Grace",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Psychic","Doom Desire","Future Sight","Flash Cannon","Shadow Ball","Rest","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Rayquaza     
class Rayquaza(Pokemon2):
    "Rayquaza"
    def __init__(self,name="Rayquaza",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=105,atk=150,defense=90,spatk=150,spdef=90,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Air Lock",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Crunch","Hyper Beam","Dragon Ascent","Dragon Dance","Extreme Speed","Draco Meteor","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Mega Rayquaza     
class MRayquaza(Pokemon2):
    "Mega Rayquaza"
    def __init__(self,name="Mega Rayquaza",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=105,atk=180,defense=100,spatk=180,spdef=100,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Delta Stream",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Crunch","Hyper Beam","Dragon Ascent","Dragon Dance","Extreme Speed","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Arboliva
class Arboliva(Pokemon2):
    def __init__(self,name="Arboliva",type1="Grass",type2="Normal",nature=None,level=100,happiness=255,hp=78,atk=69,defense=90,spatk=125,spdef=109,speed=39,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Seed Sower",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Leaf Storm","Focus Blast","Energy Ball","Seed Bomb","Petal Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Sceptile
class Sceptile(Pokemon2):
    "Sceptile"
    def __init__(self,name="Sceptile",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=70,atk=105,defense=65,spatk=85,spdef=86,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Overgrow","Unburden"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Leaf Blade","Hyper Beam","Leaf Storm","Dragon Dance","Dragon Pulse","Draco Meteor","Focus Blast","Energy Ball","Frenzy Plant","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Mega Sceptile
class MSceptile(Pokemon2):
    "Mega Sceptile"
    def __init__(self,name="Mega Sceptile",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=70,atk=135,defense=75,spatk=110,spdef=85,speed=145,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Lightning Rod","Technician"]),item="Sceptilite"):
        if move is None:
            avmoves=["Protect","Leaf Blade","Dragon Dance","Dragon Pulse","Draco Meteor","Focus Blast", "Energy Ball","X-Scissor","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Blaziken
class Blaziken(Pokemon2):
    "Blaziken"
    def __init__(self,name="Blaziken",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=120,defense=70,spatk=110,spdef=70,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Speed Boost","Striker","Blaze"]),item=random.choice(["Life Orb","Focus Sash"])):
        if move is None:
            avmoves=["Protect","Overheat","High Jump Kick","Sky Uppercut","Blaze Kick","Brave Bird","Flare Blitz","Focus Blast","Blast Burn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Quaquaval
class Quaquaval(Pokemon2):
    def __init__(self,name="Quaquaval",type1="Water",type2="Fighting",nature=None,level=100,happiness=255,hp=85,atk=120,defense=80,spatk=85,spdef=75,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Moxie","Torrent"]),item=random.choice(["Life Orb","Focus Sash"])):
        if move is None:
            avmoves=["Protect","Hydro Pump","High Jump Kick","Aqua Jet","Brave Bird","Liquidation","Focus Blast","Hydro Cannon"]
            moves=moveset(avmoves,3)+["Aqua Step"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                    
#Mega Blaziken
class MBlaziken(Pokemon2):
    "Mega Blaziken"
    def __init__(self,name="Mega Blaziken",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=160,defense=80,spatk=130,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Speed Boost",item="Blazikenite"):
        if move is None:
            avmoves=["Protect","Overheat","High Jump Kick","Sky Uppercut","Blaze Kick","Brave Bird","Flare Blitz","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                     
#Swampert
class Swampert(Pokemon2):
    "Swampert"
    def __init__(self,name="Swampert",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=100,atk=110,defense=90,spatk=85,spdef=90,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Torrent","Damp"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Power-up Punch","Waterfall","Ice Punch","Hydro Cannon","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Swampert
class MSwampert(Pokemon2):
    "Mega Swampert"
    def __init__(self,name="Mega Swampert",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=100,atk=150,defense=110,spatk=95,spdef=110,speed=70,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item="Swampertite"):
        if move is None:
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Power-up Punch","Waterfall","Ice Punch","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                               
#Ludicolo
class Ludicolo(Pokemon2):
    "Ludicolo"
    def __init__(self,name="Ludicolo",type1="Grass",type2="Water",nature=None,level=100,happiness=255,hp=80,atk=70,defense=70,spatk=100,spdef=100,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Swift Swim","Dancer"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Ice Beam","Giga Drain","Surf","Hydro Pump","Rain Dance","Focus Blast","Energy Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Shiftry
class Shiftry(Pokemon2):
    "Shiftry"
    def __init__(self,name="Shiftry",type1="Grass",type2="Dark",nature=None,level=100,happiness=255,hp=90,atk=120,defense=60,spatk=110,spdef=60,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Infiltrator"]),item=random.choice(["Life Orb","Dark Gem"])):
        if move is None:
            avmoves=["Protect","Sunny Day","Giga Drain","Leaf Storm","Hurricane","Leaf Tornado","Leech Seed","Focus Blast","Explosion","Parting Shot","Sucker Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Swellow
class Swellow(Pokemon2):
    "Swellow"
    def __init__(self,name="Swellow",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=85,defense=60,spatk=75,spdef=50,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Guts","Aerilate"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","Flying Gem"])):
        if move is None:
            avmoves=["Protect","Roost","Brave Bird","Facade","Hurricane","Boomburst"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Pelipper
class Pelipper(Pokemon2):
    "Pelipper"
    def __init__(self,name="Pelipper",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=50,defense=100,spatk=95,spdef=70,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Drizzle",item=random.choice(["Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Roost","Surf","Ice Beam","Hurricane","Hydro Pump","Scald","Chilling Water"]
            moves=moveset(avmoves,3)+["Tailwind"]
        else:
            moves=move
        if ability=="Drizzle":
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Gardevoir
class Gardevoir(Pokemon2):
    "Gardevoir"
    def __init__(self,name="Gardevoir",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=68,atk=65,defense=65,spatk=125,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Trace",item=random.choice(["Choice Specs","Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Protect","Recover","Dazzling Gleam","Moonblast","Psychic","Shadow Ball","Focus Blast","Trick Room","Misty Terrain","Aura Sphere"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Mega Gardevoir
class MGardevoir(Pokemon2):
    "Mega Gardevoir"
    def __init__(self,name="Mega Gardevoir",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=68,atk=85,defense=65,spatk=165,spdef=135,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pixilate",item="Gardevoirite"):
        if move is None:
            avmoves=["Protect","Recover","Dazzling Gleam","Moonblast","Psychic","Shadow Ball","Focus Blast","Trick Room","Misty Terrain","Aura Sphere"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Breloom
class Breloom(Pokemon2):
    "Breloom"
    def __init__(self,name="Breloom",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=60,atk=130,defense=80,spatk=60,spdef=60,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Poison Heal",item="Toxic Orb"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Mach Punch","Spore","Sky Uppercut","Bullet Seed","Seed Bomb","Leech Seed","Superpower","Gunk Shot","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Slaking
class Slaking(Pokemon2):
    "Slaking"
    def __init__(self,name="Slaking",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=150,atk=160,defense=100,spatk=95,spdef=65,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Truant",item="Leftovers",truant=False):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Hyper Beam","Double-Edge","Sky Uppercut","Return","Slack Off","Rest","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.truant=truant
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Hariyama
class Hariyama(Pokemon2):
    "Hariyama"
    def __init__(self,name="Hariyama",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=144,atk=120,defense=60,spatk=40,spdef=60,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Guts",item="Flame Orb"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Force Palm","Sky Uppercut","Arm Thrust","Belly Drum","Knock Off","Facade","Cross Chop","Drain Punch","Headlong Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Mega Sableye
class MSableye(Pokemon2):
    "Mega Sableye"
    def __init__(self,name="Mega Sableye",type1="Dark",type2="Ghost",nature=None,level=100,happiness=255,hp=50,atk=85,defense=125,spatk=85,spdef=115,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Magic Bounce",item="Sablenite"):
        if move is None:
            avmoves=["Protect","Night Shade","Shadow Sneak","Power Gem","Zen Headbutt","Knock Off","Foul Play","Moonlight","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mega Mawile
class MMawile(Pokemon2):
    "Mega Mawile"
    def __init__(self,name="Mega Mawile",type1="Steel",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=105,defense=125,spatk=55,spdef=95,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Huge Power",item="Mawilite"):
        if move is None:
            avmoves=["Protect","Iron Head","Play Rough","Crunch","Sucker Punch","Iron Defense","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Tinkaton
class Tinkaton(Pokemon2):
    def __init__(self,name="Tinkaton",type1="Fairy",type2="Steel",nature=None,level=100,happiness=255,hp=85,atk=75,defense=77,spatk=70,spdef=105,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mold Breaker",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Head","Play Rough","Crunch","Sucker Punch","Iron Defense","Draining Kiss","Fake Out","Knock Off"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Aggron
class Aggron(Pokemon2):
    "Aggron"
    def __init__(self,name="Aggron",type1="Steel",type2="Rock",nature=None,level=100,happiness=255,hp=70,atk=110,defense=180,spatk=60,spdef=60,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Rock Head","Sturdy","Heavy Metal"]),item=random.choice(["Choice Band","Leftovers"])):
        if move is None:
            avmoves=["Protect","Iron Head","Stone Edge","Crunch","Earthquake","Iron Defense","Hyper Beam","Flash Cannon","Body Press","Stealth Rock","Autotomize","Heavy Slam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Mega Aggron
class MAggron(Pokemon2):
    "Mega Aggron"
    def __init__(self,name="Mega Aggron",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=70,atk=140,defense=230,spatk=60,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Filter",item="Aggronite"):
        if move is None:
            avmoves=["Protect","Iron Head","Stone Edge","Crunch","Earthquake","Iron Defense","Hyper Beam","Flash Cannon","Heavy Slam","Body Press","Autotomize"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mega Medicham
class MMedicham (Pokemon2):
    "Mega Medicham"
    def __init__(self,name="Mega Medicham",type1="Fighting",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=100,defense=85,spatk=80,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pure Power",item="Medichamite"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Thunder Punch","Psycho Cut","Fire Punch","Zen Headbutt","Ice Punch","High Jump Kick","Close Combat","Axe Kick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Medicham        
class Medicham (Pokemon2):
    "Medicham"
    def __init__(self,name="Medicham",type1="Fighting",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=60,defense=75,spatk=60,spdef=75,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pure Power",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dynamic Punch","Thunder Punch","Psycho Cut","Fire Punch","Zen Headbutt","Ice Punch","High Jump Kick","Close Combat","Axe Kick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Torkoal       
class Torkoal (Pokemon2):
    "Torkoal"
    def __init__(self,name="Torkoal",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=70,atk=75,defense=140,spatk=95,spdef=70,speed=20,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Drought","White Smoke","Shell Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Lava Plume","Thunder Wave","Flamethrower","Toxic","Stealth Rock","Explosion","Earth Power","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
#Mega Manectric
class MManectric(Pokemon2):
    "Mega Manectric"
    def __init__(self,name="Mega Manectric",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=70,atk=75,defense=80,spatk=135,spdef=80,speed=135,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Manectite"):
        if move is None:
            avmoves=["Protect","Volt Switch","Thunder","Crunch","Thunderbolt","Wild Charge","Hyper Beam","Thunder Wave","Flamethrower","Electric Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Sharpedo
class Sharpedo(Pokemon2):
    "Sharpedo"
    def __init__(self,name="Sharpedo",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=120,defense=40,spatk=95,spdef=40,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Speed Boost","Rough Skin"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Flip Turn","Hydro Pump","Crunch","Ice Beam","Surf","Dark Pulse","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Overqwil
class Overqwil(Pokemon2):
    "Overqwil"
    def __init__(self,name="Overqwil",type1="Dark",type2="Poison",nature=None,level=100,happiness=255,hp=85,atk=115,defense=95,spatk=65,spdef=65,speed=85,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Intimidate",item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Flip Turn","Pin Missile","Crunch","Poison Jab","Barb Barrage","Dark Pulse","Double-Edge","Toxic Spikes","Stealth Rock","Chilling Water","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Sharpedo
class MSharpedo(Pokemon2):
    "Mega Sharpedo"
    def __init__(self,name="Mega Sharpedo",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=140,defense=70,spatk=110,spdef=65,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Strong Jaw",item="Sharpedonite"):
        if move is None:
            avmoves=["Protect","Flip Turn","Thunder Fang","Crunch","Liquidation","Surf","Ice Fang","Poison Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Wailord
class Wailord(Pokemon2):
    "Wailord"
    def __init__(self,name="Wailord",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=150,atk=50,defense=80,spatk=105,spdef=80,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Blubber Defense","Pressure"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Water Spout","Hydro Pump","Blizzard","Ice Beam","Surf","Rain Dance","Heavy Slam","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Mega Camerupt
class MCamerupt(Pokemon2):
    "Mega Camerupt"
    def __init__(self,name="Mega Camerupt",type1="Fire",type2="Ground",nature=None,level=100,happiness=255,hp=90,atk=100,defense=110,spatk=145,spdef=115,speed=20,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sheer Force",item="Cameruptite"):
        if move is None:
            avmoves=["Protect","Eruption","Earth Power","Lava Plume","Earthquake","Stone Edge","Fire Blast","Stealth Rock","Magnitude","Bulldoze","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Camerupt
class Camerupt(Pokemon2):
    "Camerupt"
    def __init__(self,name="Camerupt",type1="Fire",type2="Ground",nature=None,level=100,happiness=255,hp=90,atk=100,defense=70,spatk=105,spdef=75,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Solid Rock","Anger Point","Magma Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Eruption","Earth Power","Lava Plume","Earthquake","Stone Edge","Fire Blast","Will-O-Wisp","Stealth Rock","Magnitude","Bulldoze","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Arbok
class Arbok(Pokemon2):
    "Arbok"
    def __init__(self,name="Arbok",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=75,atk=85,defense=75,spatk=65,spdef=79,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Strong Jaw","Shed Skin"]),item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Venoshock","Earth Power","Poison Fang","Crunch","Gunk Shot","Belch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Regirock
class Regirock(Pokemon2):
    "Regirock"
    def __init__(self,name="Regirock",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=80,atk=100,defense=200,spatk=50,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Clear Body","Solid Rock"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Zap Cannon","Earth Power","Hyper Beam","Earthquake","Stone Edge","Rock Slide","Explosion","Stealth Rock","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Regice
class Regice(Pokemon2):
    "Regice"
    def __init__(self,name="Regice",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=50,defense=100,spatk=100,spdef=200,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Clear Body","Filter"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Beam","Blizzard","Freeze-Dry","Hyper Beam","Zap Cannon","Snowscape","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Registeel
class Registeel(Pokemon2):
    "Registeel"
    def __init__(self,name="Registeel",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=80,atk=75,defense=150,spatk=75,spdef=150,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Clear Body","Filter"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Head","Flash Cannon","Zap Cannon","Earthquake","Hyper Beam","Curse","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Dewgong
class Dewgong(Pokemon2):
    "Dewgong"
    def __init__(self,name="Dewgong",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=50,defense=80,spatk=90,spdef=95,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Thick Fat","Ice Scales","Ice Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Snowscape","Rain Dance","Frost Breath","Aurora Veil"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Jynx
class Jynx(Pokemon2):
    "Jynx"
    def __init__(self,name="Jynx",type1="Ice",type2="Psychic",nature=None,level=100,happiness=255,hp=65,atk=50,defense=50,spatk=115,spdef=95,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Dry Skin",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Ice Beam","Psychic","Blizzard","Dark Pulse","Hail","Shadow Ball","Trick Room","Light Screen","Expanding Force","Draining Kiss"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Mamoswine
class Mamoswine(Pokemon2):
    "Mamoswine"
    def __init__(self,name="Mamoswine",type1="Ice",type2="Ground",nature=None,level=100,happiness=255,hp=110,atk=130,defense=80,spatk=70,spdef=60,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Thick Fat","Snow Cloak"]),item=random.choice(["Leftovers","Choice Scarf"])):
        if move is None:
            avmoves=["Protect","Ice Beam","Earthquake","Blizzard","Stone Edge","Hail","Icicle Crash","Stealth Rock","Snowscape"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Deigon
class Deigon(Pokemon2):
    def __init__(self,name="Deigon",type1="Ground",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=130,defense=80,spatk=90,spdef=80,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens","Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Stone Edge","Superpower","Sandstorm"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                 
#Flygon
class Flygon(Pokemon2):
    "Flygon"
    def __init__(self,name="Flygon",type1="Ground",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=100,defense=80,spatk=100,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens","Levitate","Compound Eyes"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Stone Edge","Superpower","Sandstorm","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Mega Flygon
class MFlygon(Pokemon2):
    def __init__(self,name="Mega Flygon",type1="Bug",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=130,defense=100,spatk=100,spdef=80,speed=140,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Flygonite"):
        if move is None:
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Stone Edge","Superpower","Sandstorm","Bug Buzz","Dragon Dance","X-Scissor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Altaria
class Altaria(Pokemon2):
    "Altaria"
    def __init__(self,name="Altaria",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=70,defense=90,spatk=70,spdef=105,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Natural Cure","Cloud Nine"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Brave Bird","Sky Attack","Moonblast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Mega Altaria
class MAltaria(Pokemon2):
    "Mega Altaria"
    def __init__(self,name="Mega Altaria",type1="Dragon",type2="Fairy",nature=None,level=100,happiness=255,hp=85,atk=110,defense=110,spatk=110,spdef=105,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pixilate",item="Altarianite"):
        if move is None:
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Brave Bird","Sky Attack","Moonblast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Zangoose
class Zangoose(Pokemon2):
    "Zangoose"
    def __init__(self,name="Zangoose",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=73,atk=115,defense=70,spatk=60,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Toxic Boost","Tough Claws"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Clush Claw","Slash","Crunch","X-Scissor","Facade","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Toxic Boost":
            item="Toxic Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Seviper
class Seviper(Pokemon2):
    "Seviper"
    def __init__(self,name="Seviper",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=83,atk=100,defense=83,spatk=100,spdef=83,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Shed Skin","Merciless","Fatal Precision"]),item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Poison Fang","Poison Tail","Crunch","Poison Jab","Toxic","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Exploud
class Exploud(Pokemon2):
    "Exploud"
    def __init__(self,name="Exploud",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=104,atk=81,defense=63,spatk=91,spdef=73,speed=73,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Scrappy","Punk Rock","Soundproof"]),item="Throat Spray"):
        if move is None:
            avmoves=["Protect","Boomburst","Hyper Beam","Crunch","Hyper Voice","Toxic","Double-Edge","Rest"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Lunatone
class Lunatone(Pokemon2):
    "Lunatone"
    def __init__(self,name="Lunatone",type1="Rock",type2="Psychic",nature=None,level=100,happiness=255,hp=70,atk=55,defense=65,spatk=105,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Moonblast","Stone Edge","Moonlight","Explosion","Trick Room","Stealth Rock","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Solrock
class Solrock(Pokemon2):
    "Solrock"
    def __init__(self,name="Solrock",type1="Rock",type2="Psychic",nature=None,level=100,happiness=255,hp=70,atk=105,defense=85,spatk=55,spdef=65,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Moonblast","Stone Edge","Morning Sun","Explosion","Trick Room","Solar Beam","Stealth Rock","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Whiscash
class Whiscash(Pokemon2):
    "Whiscash"
    def __init__(self,name="Whiscash",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=110,atk=78,defense=73,spatk=76,spdef=71,speed=60,hpev=0,atkev=252,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Oblivious",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Ice Beam","Surf","Power Gem","Hydro Pump","Stone Edge","Earthquake","Rest","Magnitude"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Dondozo
class Dondozo(Pokemon2):
    def __init__(self,name="Dondozo",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=150,atk=100,defense=115,spatk=65,spdef=65,speed=35,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Unaware",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Rock Slide","Earthquake","Rest","Wave Crash","Heavy Slam","Body Press","Yawn"]
            moves=moveset(avmoves,3)+["Order Up"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Crawdaunt
class Crawdaunt(Pokemon2):
    "Crawdaunt"
    def __init__(self,name="Crawdaunt",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=63,atk=120,defense=85,spatk=90,spdef=55,speed=55,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Adaptability","Shell Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Ice Beam","Surf","Power Gem","Hydro Pump","Crabhammer","Liquidation","Knock Off","Brick Break"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Claydol
class Claydol(Pokemon2):
    "Claydol"
    def __init__(self,name="Claydol",type1="Ground",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=70,defense=105,spatk=80,spdef=120,speed=75,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Earth Power","Stone Edge","Explosion","Trick Room","Stealth Rock","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Cradily
class Cradily(Pokemon2):
    "Cradily"
    def __init__(self,name="Cradily",type1="Rock",type2="Grass",nature=None,level=100,happiness=255,hp=86,atk=81,defense=97,spatk=81,spdef=107,speed=43,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Storm Drain",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","Giga Drain","Sludge Bomb","Earth Power","Leech Seed","Energy Ball","Stealth Rock","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Armaldo
class Armaldo(Pokemon2):
    "Armaldo"
    def __init__(self,name="Armaldo",type1="Rock",type2="Bug",nature=None,level=100,happiness=255,hp=75,atk=125,defense=100,spatk=70,spdef=80,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ancient Power","Hyper Beam","X-Scissor","Rock Blast","Earth Power","Crush Claw","Stealth Rock","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Milotic
class Milotic(Pokemon2):
    "Milotic"
    def __init__(self,name="Milotic",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=95,atk=60,defense=84,spatk=100,spdef=125,speed=86,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Competitive","Marvel Scale"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Ice Beam","Surf","Rain Dance","Hydro Pump","Coil","Thunderbolt","Light Screen","Scale Shot","Aqua Ring"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Marvel Scale":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Dudunsparce
class Dudunsparce (Pokemon2):
    def __init__(self,name="Dudunsparce",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=125,atk=100,defense=80,spatk=85,spdef=75,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Serene Grace",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Roost","Hypnosis","Shadow Ball","Trick Room","Light Screen","Reflect","Giga Impact","Body Slam","Yawn","Scale Shot"]
            moves=moveset(avmoves,3)+["Hyper Drill"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Cyclizar
class Cyclizar(Pokemon2):
    def __init__(self,name="Cyclizar",type1="Dragon",type2="Normal",nature=None,level=100,happiness=255,hp=70,atk=95,defense=65,spatk=85,spdef=65,speed=121,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Light Screen","Reflect","Giga Impact","Body Slam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                 
#Farigarif
class Farigarif(Pokemon2):
    "Farigarif"
    def __init__(self,name="Farigarif",type1="Normal",type2="Psychic",nature=None,level=100,happiness=255,hp=120,atk=90,defense=70,spatk=110,spdef=70,speed=85,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Armor Tail",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Psychic","Crunch","Zen Headbutt","Assurance","Hypnosis","Shadow Ball","Trick Room","Light Screen","Reflect"]
            moves=moveset(avmoves,3)+["Twin Beam"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Banette
class Banette(Pokemon2):
    "Banette"
    def __init__(self,name="Banette",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=64,atk=115,defense=65,spatk=73,spdef=63,speed=65,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Insomnia",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Phantom Force","Assurance","Hypnosis","Shadow Ball","Will-O-Wisp","Destiny Bond","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Mega Banette
class MBanette(Pokemon2):
    "Mega Banette"
    def __init__(self,name="Mega Banette",type1="Ghost",type2="Normal",nature=None,level=100,happiness=255,hp=64,atk=165,defense=75,spatk=93,spdef=83,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Prankster",item="Banettite"):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Phantom Force","Assurance","Hypnosis","Shadow Ball","Toxic","Thunder Wave","Will-O-Wisp","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Absol
class Absol(Pokemon2):
    "Absol"
    def __init__(self,name="Absol",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=75,atk=130,defense=70,spatk=85,spdef=70,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Super Luck","Justified"]),item=random.choice(["Life Orb","Choice Band","Black Glasses","Scope Lens"])):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Psycho Cut","Assurance","Night Slash","Shadow Ball","Toxic","Sucker Punch","Close Combat","Swords Dance","Play Rough","Iron Tail"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Mega Absol
class MAbsol(Pokemon2):
    "Mega Absol"
    def __init__(self,name="Mega Absol",type1="Dark",type2="Fairy",nature=None,level=100,happiness=255,hp=75,atk=150,defense=70,spatk=115,spdef=70,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Magic Bounce","Sharpness"]),item="Absolite"):
        if move is None:
            avmoves=["Protect","Recover","Knock Off","Crunch","Psycho Cut","Assurance","Night Slash","Shadow Ball","Toxic","Sucker Punch","Close Combat","Swords Dance","Play Rough"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Mega Glalie
class MGlalie(Pokemon2):
    "Mega Glalie"
    def __init__(self,name="Mega Glalie",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=135,defense=80,spatk=105,spdef=80,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Refrigerate",item="Glalite"):
        if move is None:
            avmoves=["Protect","Recover","Earthquake","Crunch","Ice Beam","Blizzard","Freeze-Dry","Ice Fang","Toxic","Snowscape","Hyper Beam","Rain Dance","Icicle Crash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
                                    
#Glalie
class Glalie(Pokemon2):
    "Glalie"
    def __init__(self,name="Glalie",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=80,spatk=100,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Inner Focus","Moody","Refrigerate"]),item="Focus Sash"):
        if move is None:
            avmoves=["Protect","Recover","Earthquake","Crunch","Ice Beam","Blizzard","Freeze-Dry","Ice Fang","Toxic","Snowscape","Hyper Beam","Rain Dance","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Walrein
class Walrein(Pokemon2):
    "Walrein"
    def __init__(self,name="Walrein",type1="Ice",type2="Water",nature=None,level=100,happiness=255,hp=90,atk=80,defense=90,spatk=95,spdef=90,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Thick Fat","Ice Body","Fur Coat"]),item=random.choice(["Leftovers","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Slack Off","Surf","Crunch","Ice Beam","Blizzard","Freeze-Dry","Ice Fang","Rest","Snowscape","Hyper Beam","Earthquake","Icicle Spear","Iron Head","Swords Dance","Liquidation"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Huntail
class Huntail(Pokemon2):
    "Huntail"
    def __init__(self,name="Huntail",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=55,atk=104,defense=105,spatk=94,spdef=75,speed=52,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Intimidate","Defiant"]),item="White Herb"):
        if move is None:
            avmoves=["Protect","Crunch","Ice Beam","Blizzard","Liquidation","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Shell Smash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Gorebyss
class Gorebyss(Pokemon2):
    "Gorebyss"
    def __init__(self,name="Gorebyss",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=55,atk=84,defense=105,spatk=104,spdef=75,speed=52,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Regenerator","Dazzling"]),item="White Herb"):
        if move is None:
            avmoves=["Protect","Dazzling Gleam","Ice Beam","Blizzard","Moonblast","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Shell Smash","Draining Kiss"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Relicanth
class Relicanth(Pokemon2):
    "Relicanth"
    def __init__(self,name="Relicanth",type1="Water",type2="Rock",nature=None,level=100,happiness=255,hp=100,atk=105,defense=130,spatk=45,spdef=65,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Ice Beam","Stone Edge","Rock Slide","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Head Smash","Stealth Rock","Meteor Beam","Skull Bash","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Salamence
class Salamence(Pokemon2):
    "Salamence"
    def __init__(self,name="Salamence",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=135,defense=80,spatk=110,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item=random.choice(["Life Orb","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Stone Edge","Dragon Claw","Flamethrower","Crunch","Zen Headbutt","Double-Edge","Hydro Pump","Earthquake","Dragon Dance","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Mega Salamence
class MSalamence(Pokemon2):
    "Mega Salamence"
    def __init__(self,name="Mega Salamence",type1="Dragon",type2="Flying",nature=None,level=100,happiness=255,hp=95,atk=145,defense=130,spatk=120,spdef=90,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Aerilate",item="Salamencite"):
        if move is None:
            avmoves=["Protect","Stone Edge","Dragon Claw","Ice Beam","Flamethrower","Crunch","Zen Headbutt","Double-Edge","Hydro Pump","Earthquake","Dragon Dance","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Metagross
class Metagross(Pokemon2):
    "Metagross"
    def __init__(self,name="Metagross",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=135,defense=130,spatk=95,spdef=90,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Clear Body",item=random.choice(["Leftovers","Choice Band"])):
        if move is None:
            avmoves=["Protect","Stone Edge","Bullet Punch","Meteor Mash","Hyper Beam","Crunch","Zen Headbutt","Double-Edge","Iron Defense","Earthquake","Hammer Arm","Flash Cannon","Stealth Rock","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                    
#MegaMetagross
class MMetagross(Pokemon2):
    "Mega Metagross"
    def __init__(self,name="Mega Metagross",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=145,defense=150,spatk=105,spdef=110,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Metagrossite"):
        if move is None:
            avmoves=["Protect","Stone Edge","Bullet Punch","Meteor Mash","Hyper Beam","Crunch","Zen Headbutt","Double-Edge","Iron Defense","Earthquake","Hammer Arm","Flash Cannon","Fire Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Latias
class Latias(Pokemon2):
    "Latias"
    def __init__(self,name="Latias",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=80,defense=90,spatk=110,spdef=130,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Mist Ball","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Latios
class Latios(Pokemon2):
    "Latios"
    def __init__(self,name="Latios",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=90,defense=80,spatk=130,spdef=110,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item=random.choice(["Choice Scarf","Choice Specs"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Luster Purge","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball","Draco Meteor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Latias
class MLatias(Pokemon2):
    "Mega Latias"
    def __init__(self,name="Mega Latias",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=100,defense=120,spatk=140,spdef=150,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Latiasite"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Mist Ball","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Latios
class MLatios(Pokemon2):
    "Mega Latios"
    def __init__(self,name="Mega Latios",type1="Dragon",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=130,defense=100,spatk=160,spdef=120,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Latiosite"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Luster Purge","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Kyogre
class Kyogre(Pokemon2):
    "Kyogre"
    def __init__(self,name="Kyogre",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=90,spatk=150,spdef=140,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drizzle",item=random.choice(["Choice Scarf","Choice Specs","Leftovers"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Origin Pulse","Thunder","Water Spout","Ancient Power","Calm Mind","Ice Beam","Thunderbolt","Rest","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Primal Kyogre
class PKyogre(Pokemon2):
    "Primal Kyogre"
    def __init__(self,name="Primal Kyogre",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=150,defense=90,spatk=180,spdef=160,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Primordial Sea",item="Blue Orb"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Origin Pulse","Thunder","Water Spout","Ancient Power","Calm Mind","Ice Beam","Thunderbolt","Rest","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Groudon
class Groudon(Pokemon2):
    "Groudon"
    def __init__(self,name="Groudon",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=100,atk=150,defense=140,spatk=100,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Drought",item=random.choice(["Choice Band","Leftovers","Lum Berry","Life Orb"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Precipice Blades","Earthquake","Eruption","Ancient Power","Swords Dance","Fire Blast","Fire Punch","Rest","Thunder Wave","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Primal Groudon
class PGroudon(Pokemon2):
    "Primal Groudon"
    def __init__(self,name="Primal Groudon",type1="Ground",type2="Fire",nature=None,level=100,happiness=255,hp=100,atk=180,defense=160,spatk=150,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Desolate Land",item="Red Orb"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Precipice Blades","Earthquake","Eruption","Ancient Power","Swords Dance","Fire Blast","Fire Punch","Rest","Thunder Wave","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Torterra
class Torterra(Pokemon2):
    "Torterra"
    def __init__(self,name="Torterra",type1="Grass",type2="Ground",nature=None,level=100,happiness=255,hp=95,atk=109,defense=105,spatk=75,spdef=85,speed=56,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Overgrow","Rock Head"]),item=random.choice(["Choice Band","Leftovers","Yache Berry"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Wood Hammer","Earthquake","Leaf Storm","Ancient Power","Swords Dance","Curse","Synthesis","Crunch","Giga Drain","Headlong Rush","Frenzy Plant","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Infernape
class Infernape(Pokemon2):
    "Infernape"
    def __init__(self,name="Infernape",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=76,atk=110,defense=71,spatk=110,spdef=71,speed=113,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Blaze","Iron Fist"]),item=random.choice(["Choice Band","Focus Sash","Expert Belt","Life Orb"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Flare Blitz","Close Combat","Fire Blast","Mach Punch","Swords Dance","Power-up Punch","Overheat","Calm Mind","Flamethrower","Blast Burn","Stealth Rock","Raging Fury","Taunt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Empoleon
class Empoleon(Pokemon2):
    "Empoleon"
    def __init__(self,name="Empoleon",type1="Water",type2="Steel",nature=None,level=100,happiness=255,hp=84,atk=86,defense=88,spatk=111,spdef=101,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Torrent","Competitive"]),item=random.choice(["Leftovers","Shuca Berry","Chople Berry"])):
        if move is None:
            avmoves=["Protect","Hyper Beam","Surf","Flash Cannon","Hydro Pump","Liquidation","Wave Crash","Ice Beam","Steel Beam","Rest","Scald","Hydro Cannon","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Staraptor
class Staraptor(Pokemon2):
    "Staraptor"
    def __init__(self,name="Staraptor",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=120,defense=70,spatk=50,spdef=60,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Reckless"]),item=random.choice(["Choice Scarf","Choice Band","Leftovers"])):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-Turn","Giga Impact","Facade"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Luxray
class Luxray(Pokemon2):
    "Luxray"
    def __init__(self,name="Luxray",type1="Electric",type2="Dark",nature=None,level=100,happiness=255,hp=80,atk=120,defense=79,spatk=95,spdef=79,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Guts"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Wild Charge","Crunch","Thunder Wave","Play Rough","Electric Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Roserade
class Roserade(Pokemon2):
    "Roserade"
    def __init__(self,name="Roserade",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=70,defense=65,spatk=125,spdef=105,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Technician","Poison Touch"]),item=random.choice(["Heavy-Duty Boots","Black Sludge","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Weather Ball","Toxic","Sunny Day","Giga Drain","Energy Ball","Toxic Spikes","Grassy Terrain","Flower Trick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Rampardos
class Rampardos(Pokemon2):
    "Rampardos"
    def __init__(self,name="Rampardos",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=97,atk=165,defense=60,spatk=65,spdef=50,speed=58,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Mold Breaker"]),item=random.choice(["Choice Scarf","Choice Band"])):
        if move is None:
            avmoves=["Protect","Head Smash","Iron Head","Crunch","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Stonjourner
class Stonjourner(Pokemon2):
    def __init__(self,name="Stonjourner",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=100,atk=125,defense=135,spatk=20,spdef=50,speed=80,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Power Spot"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Protect","Stealth Rock","Heavy Slam","Rock Slide","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Eiscue
class Eiscue(Pokemon2):
    def __init__(self,name="Eiscue",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=75,atk=100,defense=110,spatk=45,spdef=90,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Ice Face"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Protect","Ice Beam","Freeze-Dry","Weather Ball","Surf"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Bastiodon
class Bastiodon(Pokemon2):
    "Bastiodon"
    def __init__(self,name="Bastiodon",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=60,atk=52,defense=168,spatk=47,spdef=138,speed=30,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sturdy","Dauntless Shield","Soundproof"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Defense","Iron Head","Crunch","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Vespiquen
class Vespiquen(Pokemon2):
    "Vespiquen"
    def __init__(self,name="Vespiquen",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=80,defense=102,spatk=80,spdef=102,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Pressure","Queenly Majesty"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Defense Order","Attack Order","Heal Order","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                             #Gastrodon
class WGastrodon(Pokemon2):
    "Gastrodon"
    def __init__(self,name="West Sea Gastrodon",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=111,atk=83,defense=68,spatk=92,spdef=82,speed=39,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Storm Drain",item=random.choice(["Leftovers","Rindo Berry","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Earth Power","Recover","Hydro Pump","Ice Beam","Stealth Rock","Light Screen","Reflect","Chilling Water","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Gastrodon
class EGastrodon(Pokemon2):
    "Gastrodon"
    def __init__(self,name="East Sea Gastrodon",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=111,atk=83,defense=68,spatk=92,spdef=82,speed=39,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Storm Drain",item=random.choice(["Leftovers","Rindo Berry","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Earth Power","Recover","Hydro Pump","Ice Beam","Stealth Rock","Light Screen","Reflect","Chilling Water"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ambipom
class Ambipom(Pokemon2):
    "Ambipom"
    def __init__(self,name="Ambipom",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=75,atk=100,defense=66,spatk=60,spdef=66,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Skill Link",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Toxic","Double Hit","U-Turn","Return"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Drifblim
class Drifblim(Pokemon2):
    "Drifblim"
    def __init__(self,name="Drifblim",type1="Ghost",type2="Flying",nature=None,level=100,happiness=255,hp=150,atk=80,defense=44,spatk=90,spdef=54,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flare Boost",item="Flame Orb"):
        if move is None:
            avmoves=["Protect","Psychic","Shadow Ball","Calm Mind","Thunderbolt","Explosion","Destiny Bond","Tailwind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Lopunny
class MLopunny(Pokemon2):
    "Mega Lopunny"
    def __init__(self,name="Mega Lopunny",type1="Normal",type2="Fighting",nature=None,level=100,happiness=255,hp=65,atk=136,defense=94,spatk=54,spdef=96,speed=135,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Scrappy",item="Lopunnite"):
        if move is None:
            avmoves=["Protect","High Jump Kick","Return","Fake Out","Power-up Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mismagius
class Mismagius(Pokemon2):
    "Mismagius"
    def __init__(self,name="Mismagius",type1="Ghost",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=60,defense=70,spatk=105,spdef=105,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psychic","Shadow Ball","Calm Mind","Thunderbolt","Dazzling Gleam","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Purugly
class Purugly(Pokemon2):
    "Purugly"
    def __init__(self,name="Purugly",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=100,atk=82,defense=79,spatk=79,spdef=64,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Thick Fat","Defiant","Own Tempo"]),item=random.choice(["Silk Scarf","Life Orb"])):
        if move is None:
            avmoves=["Protect","Sucker Punch","Play Rough","Body Slam","Double-Edge","Bulk Up"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Skuntank
class Skuntank(Pokemon2):
    "Skuntank"
    def __init__(self,name="Skuntank",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=103,atk=93,defense=67,spatk=91,spdef=61,speed=84,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Stench",item=random.choice(["Rocky Helmet","Black Sludge","Black Glasses","Choice Band","Choice Scarf"])):
        if move is None:
            avmoves=["Protect","Dark Pulse","Shadow Ball","Flamethrower","Belch","Sludge Wave","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Honchkrow
class Honchkrow(Pokemon2):
    "Honchkrow"
    def __init__(self,name="Honchkrow",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=100,atk=125,defense=60,spatk=105,spdef=60,speed=96,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Super Luck","Moxie","Insomnia"]),item=random.choice(["Scope Lens","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Night Slash","Shadow Ball","Drill Peck","Roost","Dark Pulse","Tailwind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Spiritomb
class Spiritomb(Pokemon2):
    "Spiritomb"
    def __init__(self,name="Spiritomb",type1="Ghost",type2="Dark",nature=None,level=100,happiness=255,hp=50,atk=92,defense=108,spatk=92,spdef=108,speed=35,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Pressure","Intimidate"]),item=random.choice(["Choice Band","Leftovers"])):
        if move is None:
            avmoves=["Protect","Night Slash","Shadow Ball","Hypnosis","Nasty Plot","Dark Pulse","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Whimsicott
class Whimsicott(Pokemon2):
    def __init__(self,name="Whimsicott",type1="Grass",type2="Fairy",nature=None,level=100,happiness=255,hp=60,atk=67,defense=85,spatk=77,spdef=75,speed=115,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Protect","Cotton Guard","Hurricane","Moonblast","Energy Ball","Giga Drain"]
            moves=moveset(avmoves,3)+["Tailwind"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Garchomp
class Garchomp(Pokemon2):
    "Garchomp"
    def __init__(self,name="Garchomp",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=108,atk=130,defense=95,spatk=80,spdef=85,speed=102,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Rough Skin","Sand Veil"]),item=random.choice(["Life Orb","Yache Berry","Leftovers","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Dragon Claw","Stone Edge","Draco Meteor","Flamethrower","Stealth Rock","Dual Chop","Roar","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Mega Garchomp
class MGarchomp(Pokemon2):
    "Mega Garchomp"
    def __init__(self,name="Mega Garchomp",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=108,atk=170,defense=105,spatk=120,spdef=95,speed=102,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Force",item="Garchompite"):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Dragon Claw","Stone Edge","Draco Meteor","Flamethrower","Stealth Rock","Dual Chop","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Lucario
class Lucario(Pokemon2):
    "Lucario"
    def __init__(self,name="Lucario",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=110,defense=70,spatk=115,spdef=70,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Inner Focus",item=random.choice(["Choice Band","Life Orb"])):
        if move is None:
            avmoves=["Protect","Meteor Mash","Aura Sphere","Dragon Pulse","Close Combat","Bullet Punch","Bone Rush","Extreme Speed","Steel Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Mega Lucario
class MLucario(Pokemon2):
    "Mega Lucario"
    def __init__(self,name="Mega Lucario",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=145,defense=88,spatk=140,spdef=70,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Lucarionite"):
        if move is None:
            avmoves=["Protect","Meteor Mash","Aura Sphere","Dragon Pulse","Close Combat","Bullet Punch","Bone Rush","Extreme Speed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Hippowdon
class Hippowdon(Pokemon2):
    "Hippowdon"
    def __init__(self,name="Hippowdon",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=108,atk=112,defense=118,spatk=68,spdef=72,speed=47,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Stream",item=random.choice(["Leftovers","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Earthquake","Slack Off","Stone Edge","Knock Off","Stealth Rock","Yawn","Roar"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Drapion
class Drapion(Pokemon2):
    "Drapion"
    def __init__(self,name="Drapion",type1="Poison",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=90,defense=110,spatk=60,spdef=75,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper",item=random.choice(["Shuca Berry","Choice Band","Black Sludge"])):
        if move is None:
            avmoves=["Protect","Wicked Blow","Cross Poison","Swords Dance","Knock Off","Crunch","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Toxicroak
class Toxicroak(Pokemon2):
    "Toxicroak"
    def __init__(self,name="Toxicroak",type1="Poison",type2="Fighting",nature=None,level=100,happiness=255,hp=83,atk=106,defense=65,spatk=86,spdef=65,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper",item=random.choice(["Choice Band","Life Orb"])):
        if move is None:
            avmoves=["Protect","Close Combat","Cross Poison","Swords Dance","Knock Off","Venoshock","Poison Jab"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                       
#Abomasnow
class Abomasnow(Pokemon2):
    "Abomasnow"
    def __init__(self,name="Abomasnow",type1="Grass",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=92,defense=75,spatk=92,spdef=85,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Snow Warning","Soundproof"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Protect","Wood Hammer","Icicle Crash","Blizzard","Ice Shard","Energy Ball","Earth Power","Aurora Veil"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Snow Warning":
            item="Icy Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Mega Abomasnow
class MAbomasnow(Pokemon2):
    "Abomasnow"
    def __init__(self,name="Abomasnow",type1="Grass",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=132,defense=105,spatk=132,spdef=105,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item="Abomasite"):
        if move is None:
            avmoves=["Protect","Wood Hammer","Icicle Crash","Blizzard","Ice Shard","Energy Ball","Earth Power","Aurora Veil"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Weavile
class Weavile(Pokemon2):
    "Weavile"
    def __init__(self,name="Weavile",type1="Dark",type2="Ice",nature=None,level=100,happiness=255,hp=70,atk=120,defense=65,spatk=45,spdef=85,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Pressure","Infiltrator"]),item=random.choice(["Heavy-Duty Boots","Choice Band"])):
        if move is None:
            avmoves=["Protect","Night Slash","Icicle Crash","Ice Shard","Poison Jab","Fake Out"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       #Magnezone
class Magnezone(Pokemon2):
    "Magnezone"
    def __init__(self,name="Magnezone",type1="Electric",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=70,defense=115,spatk=130,spdef=90,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate","Sturdy","Analytic","Magnet Pull"]),item=random.choice(["Leftovers","Choice Specs"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Flash Cannon","Thunderbolt","Iron Defense","Electric Terrain","Steel Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Klinklang
class Klinklang(Pokemon2):
    def __init__(self,name="Klinklang",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=60,atk=100,defense=115,spatk=70,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Clear Body","Steelworker"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Flash Cannon","Thunderbolt","Iron Defense","Electric Terrain","Steel Beam"]
            moves=moveset(avmoves,3)+["Gear Grind"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Rhyperior
class Rhyperior(Pokemon2):
    "Rhyperior"
    def __init__(self,name="Rhyperior",type1="Ground",type2="Rock",nature=None,level=100,happiness=255,hp=115,atk=140,defense=130,spatk=55,spdef=55,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability=random.choice(["Solid Rock","Reckless"]),item=random.choice(["Leftovers","Weakness Policy"])):
        if move is None:
            avmoves=["Protect","Stone Edge","Hammer Arm","High Horsepower","Thunder Punch","Giga Impact","Stealth Rock","Meteor Beam","Rock Wrecker","Megahorn","Drill Run"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Tangrowth
class Tangrowth(Pokemon2):
    "Tangrowth"
    def __init__(self,name="Tangrowth",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=125,spatk=110,spdef=50,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=0,maxiv="No",move=None, ability=random.choice(["Regenerator","Chlorophyll"]),item=random.choice(["Assault Vest","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Giga Drain","Sleep Powder","Ancient Power","Poison Jab","Grassy Terrain","Stealth Rock","Power Whip"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Electivire
class Electivire(Pokemon2):
    "Electivire"
    def __init__(self,name="Electivire",type1="Electric",type2="Fighting",nature=None,level=100,happiness=255,hp=75,atk=113,defense=67,spatk=105,spdef=85,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Motor Drive","Iron Fists"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Plasma Fists","Close Combat","Wild Charge","Brick Break","Giga Impact","Electric Terrain","Cross Chop","Focus Blast","Reflect","Volt Tackle","Ice Punch","Fire Punch","Thunder Punch","Iron Tail","Darkest Lariat","Flamethrower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                            #Magmortar
class Magmortar(Pokemon2):
    "Magmortar"
    def __init__(self,name="Magmortar",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=75,atk=80,defense=67,spatk=125,spdef=95,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Mega Launcher","Quick Draw"]),item=random.choice(["Choice Specs","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Fire Blast","Sunny Day","Flamethrower","Toxic","Armor Cannon","Scorching Sands","Magma Storm","Steam Eruption","Dragon Pulse","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Togekiss
class Togekiss(Pokemon2):
    "Togekiss"
    def __init__(self,name="Togekiss",type1="Fairy",type2="Flying",nature=None,level=100,happiness=255,hp=85,atk=50,defense=95,spatk=120,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Serene Grace","Hustle"]),item="Heavy-Duty Boots"):
        if move is None:
            avmoves=["Protect","Roost","Nasty Plot","Air Slash","Moonblast","Extreme Speed","Metronome","Aura Sphere"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Yanmega
class Yanmega(Pokemon2):
    "Yanmega"
    def __init__(self,name="Yanmega",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=86,atk=76,defense=86,spatk=116,spdef=56,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability="Speed Boost",item=random.choice(["Choice Specs","Heavy-Duty Boots","Life Orb"])):
        if move is None:
            avmoves=["Protect","Ancient Power","Bug Buzz","Air Slash","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Gliscor
class Gliscor(Pokemon2):
    "Gliscor"
    def __init__(self,name="Gliscor",type1="Ground",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=95,defense=125,spatk=45,spdef=75,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Poison Heal","Sand Veil"]),item="Smooth Rock"):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Rock Slide","U-Turn","Sandstorm"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Poison Heal":
            item="Toxic Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                         
#Porygon-Z
class PorygonZ(Pokemon2):
    "Porygon-Z"
    def __init__(self,name="Porygon-Z",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=80,defense=70,spatk=135,spdef=75,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Adaptability","Download"]),item="Choice Scarf"):
        if move is None:
            avmoves=["Protect","Ice Beam","Calm Mind","Recover","Thunderbolt","Flamethrower","Signal Beam","Hidden Power","Psychic","Shadow Ball","Hyper Beam","Trick Room"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                          
#Gallade
class Gallade(Pokemon2):
    "Gallade"
    def __init__(self,name="Gallade",type1="Psychic",type2="Fighting",nature=None,level=100,happiness=255,hp=68,atk=125,defense=65,spatk=65,spdef=115,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Steadfast","Sharpness"]),item=random.choice(["Choice Band","Assault Vest","Life Orb"])):
        if move is None:
            avmoves=["Protect","Swords Dance","Psycho Cut","Night Slash","Close Combat","Aqua Cutter","Leaf Blade","Sacred Sword"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Mega Gallade
class MGallade(Pokemon2):
    "Mega Gallade"
    def __init__(self,name="Mega Gallade",type1="Psychic",type2="Fighting",nature=None,level=100,happiness=255,hp=68,atk=165,defense=95,spatk=65,spdef=115,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Inner Focus","Sharpness"]),item="Galladite"):
        if move is None:
            avmoves=["Protect","Swords Dance","Psycho Cut","Night Slash","Close Combat","Aqua Cutter","Leaf Blade","Sacred Sword"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                           
#Hisuian Arcanine
class HArcanine(Pokemon2):
    "Hisuian Arcanine"
    def __init__(self,name="Hisuian Arcanine",type1="Fire",type2="Rock",nature=None,level=100,happiness=255,hp=95,atk=125,defense=80,spatk=85,spdef=80,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Rock Head"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Fire Fang","Flare Blitz","Wild Charge","Head Smash","Headlong Rush","Morning Sun","Raging Fury"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Ursaluna
class Ursaluna(Pokemon2):
    "Ursaluna"
    def __init__(self,name="Ursaluna",type1="Normal",type2="Ground",nature=None,level=100,happiness=255,hp=130,atk=140,defense=105,spatk=45,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Guts","Rock Head"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Bulk Up","Double-Edge","High Horsepower","Head Smash","Headlong Rush","Moonlight"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Probopass
class Probopass(Pokemon2):
    "Probopass"
    def __init__(self,name="Probopass",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=65,atk=45,defense=145,spatk=80,spdef=150,speed=40,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Sturdy","Levitate","Magnet Pull"]),item=random.choice(["Leftovers","Air Ballon"])):
        if move is None:
            avmoves=["Protect","Iron Defense","Thunder Wave","Heavy Slam","Sandstorm","Zap Cannon","Power Gem","Rest","Rock Slide","Light Screen","Reflect","Steel Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
#Dusknoir
class Dusknoir(Pokemon2):
    "Dusknoir"
    def __init__(self,name="Dusknoir",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=45,atk=100,defense=135,spatk=65,spdef=135,speed=45,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Pressure","Levitate","Hustle"]),item=random.choice(["Choice Band","Leftovers","Chesto Berry"])):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Thunder Wave","Shadow Punch","Hex","Calm Mind","Rest","Metronome","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Froslass
class Froslass(Pokemon2):
    "Froslass"
    def __init__(self,name="Froslass",type1="Ice",type2="Ghost",nature=None,level=100,happiness=255,hp=70,atk=95,defense=70,spatk=95,spdef=70,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Snow Cloak","Levitate"]),item="Focus Sash"):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Blizzard","Shadow Punch","Hex","Calm Mind","Ice Beam","Destiny Bond","Aurora Veil"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Cryogonal
class Cryogonal(Pokemon2):
    def __init__(self,name="Cryogonal",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=70,atk=50,defense=30,spatk=110,spdef=135,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Focus Sash"):
        if move is None:
            avmoves=["Protect","Blizzard","Ice Beam","Aurora Veil","Ice Shard","Light Screen","Reflect","Ancient Power","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                
        #Wash Rotom
class WRotom(Pokemon2):
    "Wash Rotom"
    def __init__(self,name="Wash Rotom",type1="Electric",type2="Water",nature=None,level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=4,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Volt Switch","Thunder Wave","Hydro Pump","Hex","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Uxie
class Uxie(Pokemon2):
    "Uxie"
    def __init__(self,name="Uxie",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=75,atk=75,defense=130,spatk=75,spdef=130,speed=95,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunder Wave","Recover","Shadow Ball","Psychic","Calm Mind"]
            moves=moveset(avmoves,3)+["Mystical Power"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Mesprit
class Mesprit(Pokemon2):
    "Mesprit"
    def __init__(self,name="Mesprit",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=80,atk=105,defense=105,spatk=105,spdef=105,speed=80,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunder Wave","Recover","Shadow Ball","Psychic","Calm Mind"]
            moves=moveset(avmoves,3)+["Mystical Power"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Gremlid
class Gremlid(Pokemon2):
    def __init__(self,name="Gremlid",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=75,atk=110,defense=80,spatk=145,spdef=80,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunderbolt","Recover","Shadow Ball","Dark Pulse","Nasty Plot","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                            
        #Azelf
class Azelf(Pokemon2):
    "Azelf"
    def __init__(self,name="Azelf",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=75,atk=125,defense=70,spatk=125,spdef=70,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunderbolt","Recover","Shadow Ball","Psychic","Calm Mind","Ice Beam"]
            moves=moveset(avmoves,3)+["Mystical Power"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Dialga
class Dialga(Pokemon2):
    "Dialga"
    def __init__(self,name="Dialga",type1="Steel",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=120,defense=120,spatk=150,spdef=100,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Adamant Orb"):
        if move is None:
            avmoves=["Protect","Flash Cannon","Rest","Aura Sphere","Earth Power","Steel Beam"]
            moves=moveset(avmoves,3)+["Roar of Time"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Origin Dialga
class ODialga(Pokemon2):
    "Origin Dialga"
    def __init__(self,name="Origin Dialga",type1="Steel",type2="Dragon",nature=None,level=100,happiness=255,hp=100,atk=100,defense=120,spatk=150,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Adamant Orb"):
        if move is None:
            avmoves=["Protect","Flash Cannon","Rest","Aura Sphere","Earth Power","Steel Beam"]
            moves=moveset(avmoves,3)+["Roar of Time"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Palkia
class Palkia(Pokemon2):
    "Palkia"
    def __init__(self,name="Palkia",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=120,defense=100,spatk=150,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Lustrous Orb"):
        if move is None:
            avmoves=["Protect","Hydro Pump","Rest","Aura Sphere","Earth Power"]
            moves=moveset(avmoves,3)+["Spacial Rend"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Origin Palkia
class OPalkia(Pokemon2):
    "Origin Palkia"
    def __init__(self,name="Origin Palkia",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=100,defense=100,spatk=150,spdef=120,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Lustrous Orb"):
        if move is None:
            avmoves=["Protect","Hydro Pump","Rest","Aura Sphere","Earth Power"]
            moves=moveset(avmoves,3)+["Spacial Rend"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Giratina
class Giratina(Pokemon2):
    "Giratina"
    def __init__(self,name="Giratina",type1="Ghost",type2="Dragon",nature=None,level=100,happiness=255,hp=150,atk=100,defense=120,spatk=100,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Griseous Orb"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Rest","Aura Sphere","Earth Power","Dragon Claw"]
            moves=moveset(avmoves,3)+["Shadow Force"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Origin Giratina
class OGiratina(Pokemon2):
    "Origin Giratina"
    def __init__(self,name="Origin Giratina",type1="Ghost",type2="Dragon",nature=None,level=100,happiness=255,hp=150,atk=120,defense=120,spatk=100,spdef=100,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Griseous Orb"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Rest","Aura Sphere","Earth Power"]
            moves=moveset(avmoves,3)+["Shadow Force"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Heatran
class Heatran(Pokemon2):
    "Heatran"
    def __init__(self,name="Heatran",type1="Fire",type2="Steel",nature=None,level=100,happiness=255,hp=91,atk=90,defense=106,spatk=130,spdef=106,speed=77,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Flash Fire"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Fire Blast","Flash Cannon","Ancient Power","Earth Power","Steel Beam","Dark Pulse"]
            moves=moveset(avmoves,3)+["Magma Storm"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Regigigas
class Regigigas(Pokemon2):
    "Regigigas"
    def __init__(self,name="Regigigas",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=110,atk=160,defense=110,spatk=80,spdef=110,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Titan's Rage"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Giga Impact","Iron Head","Hyper Beam","Earthquake"]
            moves=moveset(avmoves,3)+["Crush Grip"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                      
#Cresselia
class Cresselia(Pokemon2):
    "Cresselia"
    def __init__(self,name="Cresselia",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=120,atk=70,defense=120,spatk=75,spdef=130,speed=85,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Moonblast","Psychic","Calm Mind","Dazzling Gleam"]
            moves=moveset(avmoves,3)+["Lunar Blessing"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Phione
class Phione(Pokemon2):
    "Phione"
    def __init__(self,name="Phione",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=80,spatk=80,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hydration"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Take Heart","Hydro Pump","Moonblast","Calm Mind","Acid Armor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Manaphy
class Manaphy(Pokemon2):
    "Manaphy"
    def __init__(self,name="Manaphy",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hydration"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hydro Pump","Tail Glow","Rain Dance","Acid Armor"]
            moves=moveset(avmoves,3)+["Heart Swap"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Darkrai
class Darkrai(Pokemon2):
    "Darkrai"
    def __init__(self,name="Darkrai",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=70,atk=90,defense=90,spatk=135,spdef=90,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Bad Dreams"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Psychic","Nasty Plot","Dark Pulse"]
            moves=moveset(avmoves,3)+["Dark Void"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Eldegoss
class Eldegoss(Pokemon2):
    def __init__(self,name="Eldegoss",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=75,atk=50,defense=90,spatk=90,spdef=120,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Regenerator"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Cotton Guard","Energy Ball","Synthesis","Leech Seed","Hidden Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Shaymin
class Shaymin(Pokemon2):
    "Shaymin"
    def __init__(self,name="Shaymin",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Natural Cure"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Energy Ball","Synthesis","Leech Seed","Hidden Power"]
            moves=moveset(avmoves,3)+["Seed Flare",]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Sky Shaymin
class SShaymin(Pokemon2):
    "Sky Shaymin"
    def __init__(self,name="Sky Shaymin",type1="Grass",type2="Flying",nature=None,level=100,happiness=255,hp=100,atk=103,defense=75,spatk=120,spdef=75,speed=127,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Natural Cure"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Energy Ball","Synthesis","Leech Seed","Hidden Power"]
            moves=moveset(avmoves,3)+["Seed Flare"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Arceus
class Arceus(Pokemon2):
    "Arceus"
    def __init__(self,name="Arceus",type1=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]),type2=None,nature=None,level=100,happiness=255,hp=120,atk=120,defense=120,spatk=120,spdef=120,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Multitype"]),item="Elemental Plates"):
        if move is None:
            avmoves=["Protect","Hyper Beam","Extreme Speed","Recover","Hidden Power","Swords Dance","Taunt"]
            moves=moveset(avmoves,3)+["Judgement"]
        else:
            moves=move
        name=name+f"({type1})"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Origin Arceus
class OArceus(Pokemon2):
    "Origin Arceus"
    def __init__(self,name="Origin Arceus",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=200,atk=200,defense=200,spatk=200,spdef=200,speed=200,hpev=252,atkev=252,defev=252,spatkev=252,spdefev=252,speedev=252,maxiv="Yes",move=None, ability=random.choice(["Typeless"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Judgement","Roar of Time","Spacial Rend","Origin Pulse","Precipice Blades","Dragon Ascent","Magma Storm","Dark Void","Lunar Blessing","Crush Grip","Shadow Force","Aeroblast","Sacred Fire","Take Heart","Heart Swap","Seed Flare","Bleakwind Storm","Wildbolt Storm","Sandsear Storm","Sacred Sword","Secret Sword","Relic Song","Techno Blast","Blue Flare","Bolt Strike","Fusion Flare","Fusion Bolt","Freeze Shock","Ice Burn"]
            moves=avmoves
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mightyena
class Mightyena(Pokemon2):
    "Mightyena"
    def __init__(self,name="Mightyena",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=70,atk=95,defense=70,spatk=60,spdef=60,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Strong Jaw","Intimidate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Fire Fang","Thunder Fang","Ice Fang","Poison Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Terryena
class Terryena(Pokemon2):
    def __init__(self,name="Terryena",type1="Dark",type2="Ground",nature=None,level=100,happiness=255,hp=85,atk=125,defense=90,spatk=50,spdef=80,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Strong Jaw","Intimidate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Fire Fang","Thunder Fang","Ice Fang","Poison Fang","Earthquake","Bulldoze","Jaw Lock","Night Slash"]
            moves=moveset(avmoves)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Bronzong
class Bronzong(Pokemon2):
    "Bronzong"
    def __init__(self,name="Bronzong",type1="Steel",type2="Psychic",nature=None,level=100,happiness=255,hp=67,atk=89,defense=116,spatk=79,spdef=116,speed=33,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate","Heatproof","Heavy Metal"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Trick Room","Extrasensory","Thunder Wave","Flash Cannon","Iron Defense","Light Screen","Reflect","Meteor Beam","Steel Beam","Heavy Slam"]
            moves=moveset(avmoves)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
                                                                                                         #Victini
class Victini(Pokemon2):
    "Victini"
    def __init__(self,name="Victini",type1="Psychic",type2="Fire",nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Victory Star",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Searing Shot","Hidden Power","V-create","Psychic","Focus Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Serperior
class Serperior(Pokemon2):
    "Serperior"
    def __init__(self,name="Serperior",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=75,atk=75,defense=95,spatk=75,spdef=95,speed=113,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Contrary",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Leaf Storm","Hidden Power","Giga Drain","Coil","Focus Blast","Leech Seed","Frenzy Plant"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Emboar
class Emboar(Pokemon2):
    "Emboar"
    def __init__(self,name="Emboar",type1="Fire",type2="Fighting",nature=None,level=100,happiness=255,hp=110,atk=123,defense=65,spatk=100,spdef=65,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Reckless",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hammer Arm","Flare Blitz","Heat Crash","Head Smash","Close Combat","Blast Burn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Samurott
class Samurott(Pokemon2):
    "Samurott"
    def __init__(self,name="Samurott",type1="Water",type2="Steel",nature=None,level=100,happiness=255,hp=95,atk=100,defense=85,spatk=108,spdef=70,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Shell Armor",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Razor Shell","Aqua Jet","Megahorn","Hydro Pump","Hydro Cannon","Aqua Cutter"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Samurott
class HSamurott(Pokemon2):
    "Hisuian Samurott"
    def __init__(self,name="Hisuian Samurott",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=90,atk=108,defense=80,spatk=100,spdef=65,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sharpness",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Razor Shell","Aqua Jet","Megahorn","Liquidation","Night Slash","Ceaseless Edge","Aqua Cutter","Sacred Sword"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Typhlosion
class HTyphlosion(Pokemon2):
    "Hisuian Typhlosion"
    def __init__(self,name="Hisuian Typhlosion",type1="Fire",type2="Ghost",nature=None,level=100,happiness=255,hp=73,atk=84,defense=78,spatk=119,spdef=85,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flash Fire",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Earth Power","Fire Blast","Lava Plume","Eruption","Focus Blast","Shadow Ball","Infernal Parade","Hex","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
 #Skeledirge
class Skeledirge(Pokemon2):
    def __init__(self,name="Skeledirge",type1="Fire",type2="Ghost",nature=None,level=100,happiness=255,hp=104,atk=75,defense=100,spatk=110,spdef=75,speed=66,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Unaware","Blaze"]),item="Throat Spray"):
        if move is None:
            avmoves=["Protect","Earth Power","Fiee Blast","Flamethrower","Eruption","Focus Blast","Shadow Ball","Hex","Destiny Bond","Will-O-Wisp","Slack Off"]
            moves=moveset(avmoves,3)+["Torch Song"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Unfezant
class Unfezant(Pokemon2):
    "Unfezant"
    def __init__(self,name="Unfezant",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=115,defense=80,spatk=65,spdef=55,speed=108,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Super Luck","Big Pecks"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-Turn","Giga Impact","Sky Attack","Air Slash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Zebstrika
class Zebstrika(Pokemon2):
    "Zebstrika"
    def __init__(self,name="Zebstrika",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=75,atk=100,defense=63,spatk=80,spdef=63,speed=116,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Motor Drive","Sap Sipper","Flare Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wild Charge","Discharge","Thunderbolt","Thunder Wave","Volt Switch"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Flare Boost":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                            #Stoutland
class Stoutland(Pokemon2):
    "Stoutland"
    def __init__(self,name="Stoutland",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=90,atk=115,defense=90,spatk=45,spdef=90,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Scrappy","Intimidate"]),item=random.choice(["Silk Scarf","Life Orb"])):
        if move is None:
            avmoves=["Protect","Giga Impact","Crunch","Play Rough","Thunder Fang","Stomping Tantrum"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Houndstone
class Houndstone(Pokemon2):
    def __init__(self,name="Houndstone",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=72,atk=101,defense=100,spatk=50,spdef=97,speed=68,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sand Rush","Fluffy"]),item=random.choice(["Spell Tag","Life Orb"])):
        if move is None:
            avmoves=["Protect","Phantom Force","Crunch","Play Rough","Thunder Fang","Stomping Tantrum","Crunch","Shadow Claw"]
            moves=moveset(avmoves,3)+["Last Respects"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                         
#Gigalith
class Gigalith(Pokemon2):
    "Gigalith"
    def __init__(self,name="Gigalith",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=85,atk=135,defense=130,spatk=60,spdef=80,speed=25,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Sturdy","Sand Force","Sand Stream"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Defense","Stone Edge","Rock Blast","Earthquake","Explosion","Rock Slide","Rest","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Excadrill
class Excadrill(Pokemon2):
    "Excadrill"
    def __init__(self,name="Excadrill",type1="Ground",type2="Steel",nature=None,level=100,happiness=255,hp=110,atk=135,defense=60,spatk=50,spdef=65,speed=88,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sand Rush","Sand Force"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Earthquake","Drill Run","Iron Head","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Conkeldurr
class Conkeldurr(Pokemon2):
    "Conkeldurr"
    def __init__(self,name="Conkeldurr",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=105,atk=140,defense=95,spatk=55,spdef=65,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Guts","Sheer Force"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Mach Punch","Drain Punch","Bulk Up","Facade","Knock Off"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Seismitoad
class Seismitoad (Pokemon2):
    "Seismitoad"
    def __init__(self,name="Seismitoad",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=105,atk=95,defense=75,spatk=85,spdef=75,speed=74,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Poison Touch","Swift Swim"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Drain Punch","Waterfall","Ice Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Leavanny
class Leavanny(Pokemon2):
    "Leavanny"
    def __init__(self,name="Leavanny",type1="Bug",type2="Grass",nature=None,level=100,happiness=255,hp=75,atk=103,defense=80,spatk=70,spdef=80,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Sharpness"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Razor Leaf","Swords Dance","X-Scissor","U-Turn","Leaf Blade","Sticky Web"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Scolipede
class Scolipede(Pokemon2):
    "Scolipede"
    def __init__(self,name="Scolipede",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=100,defense=89,spatk=55,spdef=69,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability=random.choice(["Poison Touch","Speed Boost","Swarm"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Leech Life","Megahorn","Toxic","U-Turn","X-Scissor","Poison Jab"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Basculegion
class Basculegion (Pokemon2):
    "Basculegion"
    def __init__(self,name="Basculegion",type1="Water",type2="Ghost",nature=None,level=100,happiness=255,hp=120,atk=112,defense=65,spatk=80,spdef=75,speed=78,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Adaptability","Swift Swim"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wave Crash","Crunch","Aqua Tail","Aqua Jet","Waterfall","Zen Headbutt","Destiny Bond","Last Respects"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Lilligant
class HLilligant(Pokemon2):
    "Hisuian Lilligant"
    def __init__(self,name="Hisuian Lilligant",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=70,atk=105,defense=75,spatk=50,spdef=75,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Leaf Blade","Swords Dance","Victory Dance","Close Combat","Petal Dance","Recover","Drain Punch","Sleep Powder","Ice Spinner","Solar Blade"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Krookodile
class Krookodile(Pokemon2):
    "Krookodile"
    def __init__(self,name="Krookodile",type1="Ground",type2="Dark",nature=None,level=100,happiness=255,hp=95,atk=117,defense=80,spatk=65,spdef=70,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wicked Blow","Earthquake","Stone Edge","Crunch","Foul Play","Outrage","Darkest Lariat","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Darmanitan
class Darmanitan(Pokemon2):
    "Darmanitan"
    def __init__(self,name="Darmanitan",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=105,atk=140,defense=55,spatk=30,spdef=55,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Zen Mode"]),item="Choice Scarf"):
        if move is None:
            avmoves=["Superpower","Earthquake","Stone Edge","Crunch","Flare Blitz","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Galarian Darmanitan
class GDarmanitan(Pokemon2):
    "Galarian Darmanitan"
    def __init__(self,name="Galarian Darmanitan",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=105,atk=140,defense=55,spatk=30,spdef=55,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Gorilla Tactics","Zen Mode"]),item="Choice Scarf"):
        if move is None:
            avmoves=["Superpower","Earthquake","Stone Edge","Crunch","Icicle Crash","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Scrafty
class Scrafty(Pokemon2):
    "Scrafty"
    def __init__(self,name="Scrafty",type1="Dark",type2="Fighting",nature=None,level=100,happiness=255,hp=65,atk=90,defense=115,spatk=45,spdef=115,speed=58,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Intimidate","Moxie"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Close Combat","Drain Punch","Fake Out","Crunch","Foul Play","Knock Off"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Cofagrigus
class Cofagrigus(Pokemon2):
    "Cofagrigus"
    def __init__(self,name="Cofagrigus",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=58,atk=50,defense=145,spatk=95,spdef=105,speed=30,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Mummy","Shadow Shield"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Hex","Shadow Sneak","Dark Pulse","Body Press","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Runerigus
class Runerigus(Pokemon2):
    "Runerigus"
    def __init__(self,name="Runerigus",type1="Ground",type2="Ghost",nature=None,level=100,happiness=255,hp=58,atk=95,defense=145,spatk=50,spdef=105,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Wandering Spirit","Shadow Shield"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Shadow Claw","Shadow Sneak","Earthquake","Body Press","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Carracosta
class Carracosta (Pokemon2):
    "Carracosta"
    def __init__(self,name="Carracosta",type1="Water",type2="Rock",nature=None,level=100,happiness=255,hp=74,atk=108,defense=133,spatk=83,spdef=65,speed=32,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Solid Rock",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Ancient Power","Waterfall","Shell Smash","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Archeops
class Archeops(Pokemon2):
    "Archeops"
    def __init__(self,name="Archeops",type1="Rock",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=140,defense=65,spatk=80,spdef=65,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Defeatist",item="Flying Gem"):
        if move is None:
            avmoves=["Protect","Acrobatics","Earthquake","Stone Edge","Dragon Claw","Crunch","U-Turn","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zoroark
class Zoroark(Pokemon2):
    "Zoroark"
    def __init__(self,name="Zoroark",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=60,atk=105,defense=60,spatk=120,spdef=60,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Illusion",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Dark Pulse","Flamethrower","Nasty Plot","Night Daze","Knock Off","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Zoroark
class HZoroark(Pokemon2):
    "Hisuian Zoroark"
    def __init__(self,name="Hisuian Zoroark",type1="Normal",type2="Ghost",nature=None,level=100,happiness=255,hp=55,atk=100,defense=60,spatk=125,spdef=60,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Illusion",item=random.choice(["Life Orb","Leftovers"])):
        if move is None:
            avmoves=["Protect","Shadow Ball","Flamethrower","Nasty Plot","Bitter Malice","Knock Off","U-Turn","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Gothitelle
class Gothitelle(Pokemon2):
    "Gothitelle"
    def __init__(self,name="Gothitelle",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=70,atk=55,defense=95,spatk=95,spdef=110,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Competitive",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Psychic","Calm Mind","Hypnosis","Thunder Wave","Stored Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Reuniclus
class Reuniclus(Pokemon2):
    "Reuniclus"
    def __init__(self,name="Reuniclus",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=110,atk=65,defense=75,spatk=125,spdef=85,speed=30,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Magic Guard",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Shadow Ball","Psychic","Calm Mind","Acid Armor","Thunder Wave","Stored Power","Reflect","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Swanna
class Swanna(Pokemon2):
    "Swanna"
    def __init__(self,name="Swanna",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=77,defense=63,spatk=97,spdef=63,speed=108,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None,ability=random.choice(["Hydration","No Guard"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Brave Bird","Hurricane","Rain Dance","Roost","Air Slash","Surf"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Vanilluxe
class Vanilluxe(Pokemon2):
    "Vanilluxe"
    def __init__(self,name="Vanilluxe",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=71,atk=90,defense=85,spatk=110,spdef=95,speed=84,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Snow Warning",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Blizzard","Ice Beam","Acid Armor","Icicle Spear","Freeze-Dry","Weather Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Escavalier
class Escavalier(Pokemon2):
    "Escavalier"
    def __init__(self,name="Escavalier",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=135,defense=105,spatk=60,spdef=105,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Shell Armor","Overcoat","Swarm"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Iron Head","Iron Defense","X-Scissor","U-Turn","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Mollonce
class Mollonce(Pokemon2):
    def __init__(self,name="Mollonce",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=70,atk=145,defense=115,spatk=50,spdef=85,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Shell Armor","Super Luck"]),item="Focus Sash"):
        if move is None:
            avmoves=["Protect","Iron Head","Iron Defense","X-Scissor","U-Turn","Swords Dance","Drill Run","Megahorn","Night Slash"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
                            #Jellicent
class Jellicent(Pokemon2):
    "Jellicent"
    def __init__(self,name="Jellicent",type1="Water",type2="Ghost",nature=None,level=100,happiness=255,hp=100,atk=60,defense=70,spatk=85,spdef=105,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Water Absorb","Water Bubble","Cursed Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Shade","Acid Armor","Rain Dance","Recover","Will-O-Wisp","Hex","Destiny Bond","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Galvantula
class Galvantula(Pokemon2):
    "Galvantula"
    def __init__(self,name="Galvantula",type1="Bug",type2="Electric",nature=None,level=100,happiness=255,hp=70,atk=77,defense=60,spatk=97,spdef=60,speed=108,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swarm",item=random.choice(["Life Orb","Heavy-Duty Boots"])):
        if move is None:
            avmoves=["Protect","Electoweb","Thunder Wave","Electro Ball","Sucker Punch","Discharge","Bug Buzz","Giga Drain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Ferrothorn
class Ferrothorn(Pokemon2):
    "Ferrothorn"
    def __init__(self,name="Ferrothorn",type1="Grass",type2="Steel",nature=None,level=100,happiness=255,hp=74,atk=94,defense=131,spatk=54,spdef=116,speed=20,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Iron Barbs",item=random.choice(["Leftovers","Rocky Helmet"])):
        if move is None:
            avmoves=["Protect","Gyro Ball","Iron Defense","Power Whip","Leech Seed","Curse","Heavy Slam","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Eelektross
class Eelektross(Pokemon2):
    "Eelektross"
    def __init__(self,name="Eelektross",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=85,atk=105,defense=80,spatk=115,spdef=80,speed=50,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate","Fatal Precision"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Wild Charge","Thunder Wave","Coil","Sludge Bomb","Discharge","Crunch","Crush Claw","Dragon Claw","Toxic","Thunderbolt","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Chandelure
class Chandelure(Pokemon2):
    "Chandelure"
    def __init__(self,name="Chandelure",type1="Ghost",type2="Fire",nature=None,level=100,happiness=255,hp=60,atk=55,defense=90,spatk=145,spdef=90,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Shadow Tag","Flame Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Fire Blast","Focus Blast","Shadow Ball","Infernal Parade","Hex","Will-O-Wisp","Overheat","Destiny Bond","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Haxorus
class Haxorus(Pokemon2):
    "Haxorus"
    def __init__(self,name="Haxorus",type1="Dragon",type2=None,nature=None,level=100,happiness=255,hp=76,atk=147,defense=90,spatk=60,spdef=70,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Mold Breaker",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Outrage","Swords Dance","Dual Chop","Dragon Dance","Dragon Claw","Crunch","Scale Shot","Earthquake","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Beartic
class Beartic(Pokemon2):
    "Beartic"
    def __init__(self,name="Beartic",type1="Ice",type2="Fighting",nature=None,level=100,happiness=255,hp=95,atk=140,defense=80,spatk=70,spdef=80,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Slush Rush","Swift Swim","Ice Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Outrage","Swords Dance","Ice Fang","Dragon Claw","Crunch","Hammer Arm","Superpower","Snowscape","Earthquake","Close Combat"]
            moves=moveset(avmoves,3)+["Icicle Crash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Accelgor
class Accelgor(Pokemon2):
    "Accelgor"
    def __init__(self,name="Accelgor",type1="Bug",type2=None,nature=None,level=100,happiness=255,hp=80,atk=70,defense=40,spatk=100,spdef=60,speed=145,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sticky Hold","Sheer Force","Unburden"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Toxic","Bug Buzz","Final Gambit","U-Turn","Recover","Giga Drain","Water Shuriken","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Bombeedel
class Bombeedel(Pokemon2):
    def __init__(self,name="Bombeedel",type1="Bug",type2=None,nature=None,level=100,happiness=255,hp=70,atk=70,defense=30,spatk=130,spdef=70,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Aftermath",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Toxic","Fire Blast","Final Gambit","U-Turn","Recover","Explosion","X-Scissor","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mienshao
class Mienshao(Pokemon2):
    "Mienshao"
    def __init__(self,name="Mienshao",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=65,atk=125,defense=60,spatk=95,spdef=60,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Inner Focus","Regenerator","Reckless"]),item=random.choice(["Choice Scarf","Choice Band","Life Orb"])):
        if move is None:
            avmoves=["Protect","Drain Punch","High Jump Kick","Aura Sphere","U-Turn","Fake Out","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move    
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Druddigon
class Druddigon(Pokemon2):
    "Druddigon"
    def __init__(self,name="Druddigon",type1="Dragon",type2=None,nature=None,level=100,happiness=255,hp=90,atk=120,defense=90,spatk=60,spdef=90,speed=41,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Rough Skin","Mold Breaker"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Outrage","Swords Dance","Superpower","Dragon Dance","Dragon Claw","Crunch","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      

#Golurk
class Golurk(Pokemon2):
    "Golurk"
    def __init__(self,name="Golurk",type1="Ground",type2="Ghost",nature=None,level=100,happiness=255,hp=100,atk=124,defense=90,spatk=55,spdef=90,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["No Guard","Iron Fist"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Phantom Force","Hammer Arm","Shadow Sneak","Earthquake","Dynamic Punch","Stomping Tantrum","High Horsepower","Magnitude"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Bisharp
class Bisharp(Pokemon2):
    "Bisharp"
    def __init__(self,name="Bisharp",type1="Dark",type2="Steel",nature=None,level=100,happiness=255,hp=65,atk=125,defense=100,spatk=60,spdef=70,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Defiant"]),item="Eviolite"):
        if move is None:
            avmoves=["Protect","Night Slash","Swords Dance","Iron Head","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Kingambit
class Kingambit(Pokemon2):
    def __init__(self,name="Kingambit",type1="Dark",type2="Steel",nature=None,level=100,happiness=255,hp=85,atk=145,defense=110,spatk=60,spdef=80,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Supreme Overlord","Defiant"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Night Slash","Swords Dance","Iron Head","Superpower","Sucker Punch"]
            moves=moveset(avmoves,3)+["Kowtow Cleave"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Bouffalant
class Bouffalant(Pokemon2):
    "Bouffalant"
    def __init__(self,name="Bouffalant",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=100,atk=110,defense=95,spatk=40,spdef=95,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sap Sipper","Reckless"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Megahorn","Swords Dance","Superpower","Head Charge","High Horsepower","Wild Charge","Stone Edge","Iron Head","Zen Headbutt","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Braviary
class Braviary(Pokemon2):
    "Braviary"
    def __init__(self,name="Braviary",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=100,atk=123,defense=75,spatk=57,spdef=75,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Defiant","Sheer Force"]),item="Life Orb"):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-Turn","Sky Attack","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Hisuian Braviary
class HBraviary(Pokemon2):
    "Hisuian Braviary"
    def __init__(self,name="Hisuian Braviary",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=110,atk=83,defense=70,spatk=112,spdef=70,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Tinted Lens"]),item=random.choice(["Life Orb","Choice Specs"])):
        if move is None:
            avmoves=["Protect","Roost","Esper Wing","Air Slash","Dazzling Gleam","Mystical Fire","Psychic","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Mandibuzz
class Mandibuzz(Pokemon2):
    "Mandibuzz"
    def __init__(self,name="Mandibuzz",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=110,atk=65,defense=105,spatk=55,spdef=95,speed=80,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Overcoat","Weak Armor"]),item=random.choice(["Rocky Helmet","Leftovers"])):
        if move is None:
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Iron Defense","U-Turn","Knock Off","Bone Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Heatmor
class Heatmor(Pokemon2):
    "Heatmor"
    def __init__(self,name="Heatmor",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=85,atk=90,defense=66,spatk=105,spdef=66,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Fatal Precision"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Fire Lash","Flare Blitz","Inferno","Giga Drain","U-Turn","Knock Off","Sunny Day"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Durant
class Durant(Pokemon2):
    "Durant"
    def __init__(self,name="Durant",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=58,atk=109,defense=112,spatk=48,spdef=48,speed=109,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hustle","Swarm"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Crunch","Iron Head","U-Turn","Knock Off","X-Scissor","Rock Slide","Stomping Tantrum"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Hydreigon
class Hydreigon(Pokemon2):
    "Hydreigon"
    def __init__(self,name="Hydreigon",type1="Dark",type2="Dragon",nature=None,level=100,happiness=255,hp=92,atk=105,defense=90,spatk=125,spdef=90,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Dragon Pulse","Dark Pulse","Flamethrower","U-Turn","Thunderbolt","Shadow Ball","Thunder Wave","Nasty Plot","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Volcarona
class Volcarona(Pokemon2):
    "Volcarona"
    def __init__(self,name="Volcarona",type1="Bug",type2="Fire",nature=None,level=100,happiness=255,hp=85,atk=60,defense=65,spatk=135,spdef=105,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flame Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Quiver Dance","Bug Buzz","Giga Drain","Heat Wave","Morning Sun"]
            moves=moveset(avmoves,3)+["Fiery Dance"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Cobalion
class Cobalion(Pokemon2):
    "Cobalion"
    def __init__(self,name="Cobalion",type1="Steel",type2="Fighting",nature=None,level=100,happiness=255,hp=91,atk=90,defense=129,spatk=90,spdef=72,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Justified","Sharpness"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Secred Sword","Superpower","Close Combat","Iron Head"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Terrakion
class Terrakion(Pokemon2):
    "Terrakion"
    def __init__(self,name="Terrakion",type1="Rock",type2="Fighting",nature=None,level=100,happiness=255,hp=91,atk=129,defense=90,spatk=72,spdef=90,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Justified","Sharpness"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Secred Sword","Earthquake","Close Combat","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Virizion
class Virizion(Pokemon2):
    "Virizion"
    def __init__(self,name="Virizion",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=91,atk=90,defense=72,spatk=90,spdef=129,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Justified","Sharpness"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Swords Dance","Secred Sword","Giga Drain","Close Combat","Leaf Blade"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tornadus
class Tornadus(Pokemon2):
    "Tornadus"
    def __init__(self,name="Tornadus",type1="Flying",type2=None,nature=None,level=100,happiness=255,hp=79,atk=115,defense=70,spatk=125,spdef=80,speed=111,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hurricane","Air Slash","Extrasensory"]
            moves=moveset(avmoves,2)+["Bleakwind Storm","Tailwind"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Thundurus
class Thundurus(Pokemon2):
    "Thundurus"
    def __init__(self,name="Thundurus",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=79,atk=115,defense=70,spatk=125,spdef=80,speed=111,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunder","Nasty Plot","Extrasensory","Thunder Wave"]
            moves=moveset(avmoves,3)+["Wildbolt Storm"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Malevorus
class Malevorus(Pokemon2):
    def __init__(self,name="Malvorus",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=115,defense=70,spatk=135,spdef=80,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Daze","Wildbolt Storm","Nasty Plot","Extrasensory","Springtide Storm","Sandsear Storm","Bleakwind Storm"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Malevorus
class TMalevorus(Pokemon2):
    def __init__(self,name="Therian Malvorus",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=70,atk=135,defense=80,spatk=105,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Defiant",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Daze","Crunch","Dragon Dance","Night Slash","Dark Void","Dragon Claw","Sky Attack"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                               
#Landorus
class Landorus(Pokemon2):
    "Landorus"
    def __init__(self,name="Landorus",type1="Ground",type2="Flying",nature=None,level=100,happiness=255,hp=89,atk=125,defense=90,spatk=115,spdef=80,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Earth Power","Air Slash","Extrasensory"]
            moves=moveset(avmoves,3)+["Sandsear Storm",]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Therian Tornadus
class TTornadus(Pokemon2):
    "Therian Tornadus"
    def __init__(self,name="Therian Tornadus",type1="Flying",type2=None,nature=None,level=100,happiness=255,hp=79,atk=100,defense=80,spatk=110,spdef=90,speed=121,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hurricane","Bleakwind Storm","Air Slash","Extrasensory","Tailwind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Therian Thundurus
class TThundurus(Pokemon2):
    "Therian Thundurus"
    def __init__(self,name="Therian Thundurus",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=79,atk=105,defense=70,spatk=145,spdef=80,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Volt Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Thunder","Wildbolt Storm","Nasty Plot","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Therian Landorus
class TLandorus(Pokemon2):
    "Therian Landorus"
    def __init__(self,name="Therian Landorus",type1="Ground",type2="Flying",nature=None,level=100,happiness=255,hp=89,atk=145,defense=90,spatk=105,spdef=80,speed=91,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Earthquake","Sandsear Storm","U-Turn","Stone Edge","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Reshiram
class Reshiram(Pokemon2):
    "Reshiram"
    def __init__(self,name="Reshiram",type1="Dragon",type2="Fire",nature=None,level=100,happiness=255,hp=100,atk=120,defense=100,spatk=150,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Turboblaze",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Blue Flare","Fusion Flare","Dragon Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zekrom
class Zekrom(Pokemon2):
    "Zekrom"
    def __init__(self,name="Zekrom",type1="Dragon",type2="Electric",nature=None,level=100,happiness=255,hp=100,atk=150,defense=120,spatk=120,spdef=100,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Teravolt",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Bolt Strike","Fusion Bolt","Dragon Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Kyurem
class Kyurem(Pokemon2):
    "Kyurem"
    def __init__(self,name="Kyurem",type1="Dragon",type2="Ice",nature=None,level=100,happiness=255,hp=125,atk=130,defense=90,spatk=130,spdef=90,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Refrigerate",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Outrage","Sheer Cold","Scale Shot","Ice Beam","Blizzard","Ancient Power","Dragon Pulse","Freeze-Dry","Hyper Voice"]
            moves=moveset(avmoves,3)+["Glaciate"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #White Kyurem
class WKyurem(Pokemon2):
    "White Kyurem"
    def __init__(self,name="White Kyurem",type1="Dragon",type2="Ice",nature=None,level=100,happiness=255,hp=125,atk=120,defense=90,spatk=170,spdef=100,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Turboblaze",item="Leftovers"):
        if move is None:
            avmoves=["Blue Flare","Fusion Flare","Dragon Pulse","Ice Burn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Black Kyurem 
class BKyurem(Pokemon2):
    "Black Kyurem"
    def __init__(self,name="Black Kyurem",type1="Dragon",type2="Ice",nature=None,level=100,happiness=255,hp=125,atk=170,defense=100,spatk=120,spdef=90,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Teravolt",item="Leftovers"):
        if move is None:
            avmoves=["Freeze Shock","Fusion Bolt","Dragon Claw","Bolt Strike"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Keldeo
class Keldeo(Pokemon2):
    "Keldeo"
    def __init__(self,name="Keldeo",type1="Water",type2="Fighting",nature=None,level=100,happiness=255,hp=91,atk=72,defense=90,spatk=129,spdef=90,speed=108,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Justified","Sharpness"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Sacred Sword","Hydro Pump","Close Combat"]
            moves=moveset(avmoves,3)+["Secret Sword"]
        else:
            moves=move
        if "Secret Sword" in moves:
            name="Resolute "+name
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Meloetta
class Meloetta(Pokemon2):
    "Meloetta"
    def __init__(self,name="Meloetta",type1="Normal",type2="Psychic",nature=None,level=100,happiness=255,hp=100,atk=77,defense=77,spatk=128,spdef=128,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Serene Grace",item="Leftovers"):
        if move is None:
            avmoves=["Protect","U-Turn","Psychic","Relic Song","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Pirouette Meloetta
class PMeloetta(Pokemon2):
    "Meloetta"
    def __init__(self,name="Pirouette Meloetta",type1="Normal",type2="Fighting",nature=None,level=100,happiness=255,hp=100,atk=128,defense=90,spatk=77,spdef=77,speed=128,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Serene Grace",item="Leftovers"):
        if move is None:
            avmoves=["Protect","U-Turn","Psychic","Relic Song","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Genesect
class Genesect(Pokemon2):
    "Genesect"
    def __init__(self,name="Genesect",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=71,atk=120,defense=95,spatk=120,spdef=95,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Download",item=random.choice(["Burn Drive","Chill Drive","Douse Drive","Shock Drive"])):
        if move is None:
            avmoves=["Protect","Techno Blast","Bug Buzz","Iron Head","X-Scissor","Flash Cannon"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Delphox
class Delphox(Pokemon2):
    "Delphox"
    def __init__(self,name="Delphox",type1="Fire",type2="Psychic",nature=None,level=100,happiness=255,hp=75,atk=69,defense=72,spatk=114,spdef=100,speed=104,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Blaze","Magic Guard"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Fire Blast","Flamethrower","Psychic","Mystical Fire","Shadow Ball","Blast Burn","Nasty Plot","Focus Blast","Torch Song"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Chesnaught
class Chesnaught(Pokemon2):
    "Chesnaught"
    def __init__(self,name="Chesnaught",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=88,atk=107,defense=122,spatk=74,spdef=75,speed=64,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Overgrow","Iron Barbs","Bulletproof"]),item="Leftovers"):
        if move is None:
            avmoves=["Hammer Arm","Wood Hammer","Bulk Up","Seed Bomb","Close Combat","Frenzy Plant","Spiky Shield","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Greninja
class Greninja(Pokemon2):
    "Greninja"
    def __init__(self,name="Greninja",type1="Water",type2="Dark",nature=None,level=100,happiness=255,hp=72,atk=95,defense=67,spatk=103,spdef=71,speed=122,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Protean","Battle Bond"]),item="Life Orb"):
        if move is None:
            avmoves=["Water Shuriken","Dark Pulse","Hydro Pump","Extrasensory","Grass Knot","Hydro Cannon","Poison Jab","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Meowscarada
class Meowscarada(Pokemon2):
    def __init__(self,name="Meowscarada",type1="Grass",type2="Dark",nature=None,level=100,happiness=255,hp=76,atk=110,defense=70,spatk=81,spdef=70,speed=123,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Protean","Overgrow"]),item="Life Orb"):
        if move is None:
            avmoves=["Razor Leaf","Night Slash","Extrasensory","Grass Knot","Power Whip","Poison Jab","Play Rough"]
            moves=moveset(avmoves,3)+["Flower Trick"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                
#Talonflame
class Talonflame(Pokemon2):
    "Talonflame"
    def __init__(self,name="Talonflame",type1="Fire",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=91,defense=71,spatk=74,spdef=69,speed=126,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flame Body","Gale Wings"]),item="Charti Berry"):
        if move is None:
            avmoves=["Protect","Heat Wave","Sky Attack","Brave Bird","Flare Blitz","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Pyroar
class Pyroar(Pokemon2):
    "Pyroar"
    def __init__(self,name="Pyroar",type1="Fire",type2="Normal",nature=None,level=100,happiness=255,hp=86,atk=68,defense=72,spatk=109,spdef=66,speed=106,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Moxie","Adaptability"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Heat Wave","Fire Blast","Flamethrower","Flare Blitz","Overheat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                           
#Florges
class Florges(Pokemon2):
    "Florges"
    def __init__(self,name="Florges",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=78,atk=65,defense=68,spatk=112,spdef=154,speed=75,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Misty Terrain","Natural Cure"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Moonblast","Petal Blizzard","Grass Knot","Dazzling Gleam","Synthesis","Grassy Terrain","Misty Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Eternal Floette
class EFloette(Pokemon2):
    "Floette"
    def __init__(self,name="Eternal Floette",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=74,atk=65,defense=67,spatk=125,spdef=128,speed=92,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Misty Terrain",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Moonblast","Petal Blizzard","Grass Knot","Light of Ruin","Synthesis","Grassy Terrain","Misty Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Gogoat
class Gogoat(Pokemon2):
    "Gogoat"
    def __init__(self,name="Gogoat",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=123,atk=100,defense=72,spatk=67,spdef=87,speed=74,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Sap Sipper","Grass Pelt"]),item="Leftovers"):
        if move is None:
            avmoves=["Leaf Blade","Wood Hammer","Bulk Up","Seed Bomb","Milk Drink","Horn Leech","Leech Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Pangoro
class Pangoro(Pokemon2):
    "Pangoro"
    def __init__(self,name="Pangoro",type1="Fighting",type2="Dark",nature=None,level=100,happiness=255,hp=95,atk=124,defense=78,spatk=69,spdef=71,speed=58,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Scrappy",item="Leftovers"):
        if move is None:
            avmoves=["Hammer Arm","Parting Shot","Bulk Up","Crunch","Close Combat","Night Slash","Grass Knot","Darkest Lariat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Aegislash
class Aegislash(Pokemon2):
    "Aegislash"
    def __init__(self,name="Aegislash",type1="Steel",type2="Ghost",nature=None,level=100,happiness=255,hp=60,atk=50,defense=150,spatk=50,spdef=150,speed=60,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Stance Change",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["King's Shield","Sacred Sword","Shadow Sneak","Iron Head"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Gholdengo
class Gholdengo(Pokemon2):
    def __init__(self,name="Gholdengo",type1="Steel",type2="Ghost",nature=None,level=100,happiness=255,hp=87,atk=60,defense=95,spatk=133,spdef=91,speed=84,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Good as Gold",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Focus Blast","Nasty Plot","Shadow Ball","Power Gem","Recover"]
            moves=moveset(avmoves,3)+["Make It Rain"]
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Malamar
class Malamar(Pokemon2):
    "Malamar"
    def __init__(self,name="Malamar",type1="Dark",type2="Psychic",nature=None,level=100,happiness=255,hp=86,atk=92,defense=88,spatk=68,spdef=75,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Contrary",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Superpower","Psycho Cut","Shadow Sneak","Night Slash","Hypnosis"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Barbaracle
class Barbaracle(Pokemon2):
    "Barbaracle"
    def __init__(self,name="Barbaracle",type1="Rock",type2="Water",nature=None,level=100,happiness=255,hp=72,atk=105,defense=115,spatk=54,spdef=86,speed=68,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Tough Claws","Sniper","Infiltrator"]),item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Superpower","Shell Smash","Razor Shell","Stone Edge","Cross Chop","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dragalge
class Dragalge(Pokemon2):
    "Dragalge"
    def __init__(self,name="Dragalge",type1="Poison",type2="Dragon",nature=None,level=100,happiness=255,hp=65,atk=75,defense=90,spatk=97,spdef=123,speed=44,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Poison Touch","Adaptability"]),item="Leftovers"):
        if move is None:
            avmoves=["Hydro Pump","Sludge Bomb","Outrage","Dragon Pulse","Sludge Wave","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Clawitzer
class Clawitzer(Pokemon2):
    "Clawitzer"
    def __init__(self,name="Clawitzer",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=71,atk=73,defense=88,spatk=120,spdef=89,speed=72,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Mega Launcher",item="Leftovers"):
        if move is None:
            avmoves=["Hydro Pump","Aura Sphere","Dark Pulse","Dragon Pulse","Sludge Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tyrantrum
class Tyrantrum(Pokemon2):
    "Tyrantrum"
    def __init__(self,name="Tyrantrum",type1="Rock",type2="Dragon",nature=None,level=100,happiness=255,hp=82,atk=121,defense=119,spatk=69,spdef=59,speed=71,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Rock Head","Strong Jaw"]),item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Giga Impact","Head Smash","Earthquake","Stone Edge","Dragon Claw","Meteor Beam","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Aurorus
class Aurorus(Pokemon2):
    "Aurorus"
    def __init__(self,name="Aurorus",type1="Rock",type2="Ice",nature=None,level=100,happiness=255,hp=123,atk=77,defense=72,spatk=99,spdef=92,speed=58,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Refrigerate",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Giga Impact","Blizzard","Ice Beam","Stone Edge","Freeze-Dry","Light Screen","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hawlucha
class Hawlucha(Pokemon2):
    "Hawlucha"
    def __init__(self,name="Hawlucha",type1="Fighting",type2="Flying",nature=None,level=100,happiness=255,hp=78,atk=92,defense=75,spatk=74,spdef=63,speed=118,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Limber"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Sky Attack","Roost","Brave Bird","Close Combat","U-Turn","High Jump Kick","Flying Press","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Goodra
class Goodra(Pokemon2):
    "Goodra"
    def __init__(self,name="Goodra",type1="Dragon",type2=None,nature=None,level=100,happiness=255,hp=90,atk=100,defense=70,spatk=110,spdef=150,speed=80,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sap Sipper",item="Assault Vest", shield=True,sword=False):
        if move is None:
            avmoves=["Power Whip","Body Slam","Hydro Pump","Rain Dance","Dragon Pulse","Protect"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Goodra
class HGoodra(Pokemon2):
    "Hisuian Goodra"
    def __init__(self,name="Hisuian Goodra",type1="Dragon",type2="Steel",nature=None,level=100,happiness=255,hp=80,atk=100,defense=100,spatk=110,spdef=150,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sap Sipper",item="Assault Vest", shield=True,sword=False):
        if move is None:
            avmoves=["Power Whip","Body Slam","Hydro Pump","Shelter","Dragon Pulse","Protect","Steel Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Trevenant
class Trevenant(Pokemon2):
    "Trevenant"
    def __init__(self,name="Trevenant",type1="Ghost",type2="Grass",nature=None,level=100,happiness=255,hp=85,atk=120,defense=82,spatk=65,spdef=82,speed=56,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Natural Cure","Harvest"]),item="Leftovers"):
        if move is None:
            avmoves=["Leech Seed","Wood Hammer","Shadow Claw","Will-O-Wisp","Horn Leech","Phantom Force","Forest's Curse","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                         #Gourgeist
class Gourgeist(Pokemon2):
    "Gourgeist"
    def __init__(self,name="Gourgeist",type1="Ghost",type2="Grass",nature=None,level=100,happiness=255,hp=58,atk=100,defense=122,spatk=85,spdef=75,speed=54,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Frisk","Flare Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Leech Seed","Bullet Seed","Shadow Claw","Will-O-Wisp","Razor Leaf","Phantom Force","Trick-or-Treat","Destiny Bond","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Flare Boost":
            item="Flame Orb"
        name=random.choice(["Small","Large","Super"])+" "+name
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Avalugg
class HAvalugg(Pokemon2):
    "Avalugg"
    def __init__(self,name="Hisuian Avalugg",type1="Ice",type2="Rock",nature=None,level=100,happiness=255,hp=95,atk=127,defense=184,spatk=34,spdef=36,speed=38,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sturdy",item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Mountain Gale","Ice Shard","Icicle Crash","Stone Edge","Earthquake","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Avalugg
class Avalugg(Pokemon2):
    "Avalugg"
    def __init__(self,name="Avalugg",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=95,atk=117,defense=184,spatk=44,spdef=46,speed=28,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Fliter","Sturdy","Ice Body"]),item="Leftovers", shield=True,sword=False):
        if move is None:
            avmoves=["Mountain Gale","Ice Shard","Icicle Crash","Earthquake","Iron Defense","Recover","Skull Bash","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Noivern
class Noivern(Pokemon2):
    "Noivern"
    def __init__(self,name="Noivern",type1="Flying",type2="Dragon",nature=None,level=100,happiness=255,hp=85,atk=70,defense=80,spatk=102,spdef=80,speed=123,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Infiltrator",item="Leftovers"):
        if move is None:
            avmoves=["Boomburst","Hurricane","Roost","Dragon Pulse","Air Slash","Hyper Voice"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                             
#Xerneas
class Xerneas(Pokemon2):
    "Xerneas"
    def __init__(self,name="Xerneas",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=126,atk=131,defense=95,spatk=131,spdef=98,speed=99,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Fairy Aura",item="Power Herb"):
        if move is None:
            avmoves=["Moonblast","Thunder","Flamethrower","Focus Blast"]
            moves=moveset(avmoves,3)+["Geomancy"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Yveltal
class Yveltal(Pokemon2):
    "Yveltal"
    def __init__(self,name="Yveltal",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=126,atk=131,defense=95,spatk=131,spdef=98,speed=99,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Dark Aura",item="Leftovers"):
        if move is None:
            avmoves=["Dark Pulse","Thunder","Sucker Punch","Focus Blast"]
            moves=moveset(avmoves,3)+["Oblivion Wing"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Complete Zygarde
class CZygarde(Pokemon2):
    "Zygarde"
    def __init__(self,name="Complete Zygarde",type1="Dragon",type2="Ground",nature=None,level=100,happiness=255,hp=216,atk=100,defense=121,spatk=91,spdef=95,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Power Constrict",item="Leftovers"):
        if move is None:
            avmoves=["Land's Wrath","Thousand Arrows","Core Enforcer","Earthquake","Coil","Thousand Waves"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Klefki
class Klefki(Pokemon2):
    "Klefki"
    def __init__(self,name="Klefki",type1="Steel",type2="Fairy",nature=None,level=100,happiness=255,hp=57,atk=80,defense=91,spatk=80,spdef=87,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Foul Play","Play Rough","Flash Cannon","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Diancie
class Diancie(Pokemon2):
    "Diancie"
    def __init__(self,name="Diancie",type1="Rock",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=100,defense=150,spatk=100,spdef=150,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Diamond Storm","Play Rough","Moonblast","Stealth Rock","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  

#Mega Diancie
class MDiancie(Pokemon2):
    "Mega Diancie"
    def __init__(self,name="Mega Diancie",type1="Rock",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=160,defense=110,spatk=160,spdef=110,speed=110,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Clear Body",item="Diancite"):
        if move is None:
            avmoves=["Protect","Diamond Storm","Play Rough","Moonblast","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Hoopa Unbound 
class UHoopa(Pokemon2):
    "Hoopa Unbound"
    def __init__(self,name="Hoopa Unbound",type1="Psychic",type2="Dark",nature=None,level=100,happiness=255,hp=80,atk=160,defense=60,spatk=170,spdef=130,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Magician",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hyperspace Fury","Psychic","Dark Pulse","Shadow Ball","Hyperspace Hole"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Volcanion
class Volcanion(Pokemon2):
    "Volcanion"
    def __init__(self,name="Volcanion",type1="Fire",type2="Water",nature=None,level=100,happiness=255,hp=80,atk=110,defense=120,spatk=130,spdef=90,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Water Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Steam Eruption","Flare Blitz","Overheat","Hydro Pump"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Decidueye
class Decidueye(Pokemon2):
    "Decidueye"
    def __init__(self,name="Decidueye",type1="Grass",type2="Ghost",nature=None,level=100,happiness=255,hp=78,atk=107,defense=75,spatk=95,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Overgrow","Tinted Lens","Long Reach"]),item="Leftovers"):
        if move is None:
            avmoves=["U-Turn","Shadow Claw","Brave Bird","Leaf Blade","Shadow Sneak","Sucker Punch"]
            moves=moveset(avmoves,3)+["Spirit Shackle"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Decidueye
class HDecidueye(Pokemon2):
    "Hisuian Decidueye"
    def __init__(self,name="Hisuian Decidueye",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=88,atk=112,defense=80,spatk=95,spdef=95,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Scrappy",item="Leftovers"):
        if move is None:
            avmoves=["Triple Arrows","U-Turn","Aura Sphere","Brave Bird","Leaf Blade","Close Combat","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Incineroar
class Incineroar(Pokemon2):
    "Incineroar"
    def __init__(self,name="Incineroar",type1="Fire",type2="Dark",nature=None,level=100,happiness=255,hp=95,atk=115,defense=90,spatk=80,spdef=90,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Blaze"]),item="Leftovers"):
        if move is None:
            avmoves=["Throat Chop","Flare Blitz","Parting Shot","Snarl","Cross Chop"]
            moves=moveset(avmoves,3)+["Darkest Lariat"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Primarina
class Primarina(Pokemon2):
    "Primarina"
    def __init__(self,name="Primarina",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=80,atk=74,defense=74,spatk=126,spdef=116,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Liquid Voice","Torrent"]),item="Leftovers"):
        if move is None:
            avmoves=["Moonblast","Hyper Voice","Hydro Pump","Misty Terrain","Ice Beam"]
            moves=moveset(avmoves,3)+["Sparkling Aria"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Toucannon
class Toucannon(Pokemon2):
    "Toucannon"
    def __init__(self,name="Toucannon",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=120,defense=75,spatk=75,spdef=75,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Skill Link"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Beak Blast","Roost","Brave Bird","Rock Blast","U-Turn","Bullet Seed","Drill Peck"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hisuian Electrode
class HElectrode(Pokemon2):
    "Hisuian Electrode"
    def __init__(self,name="Hisuian Electrode",type1="Electric",type2="Grass",nature=None,level=100,happiness=255,hp=60,atk=50,defense=70,spatk=80,spdef=80,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Overgrow",item="Leftovers"):
        if move is None:
            avmoves=["Chloroblast","Thunder","Thunderbolt","Thunder Wave","Energy Ball","Hyper Beam","Rest","Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Sneasler
class Sneasler(Pokemon2):
    "Sneasler"
    def __init__(self,name="Sneasler",type1="Poison",type2="Fighting",nature=None,level=100,happiness=255,hp=80,atk=130,defense=60,spatk=40,spdef=80,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Poison Touch",item="Leftovers"):
        if move is None:
            avmoves=["Dire Claw","Poison Jab","Close Combat","Swords Dance","X-Scissor","Bulk Up","Rest","Shadow Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Wyrdeer
class Wyrdeer(Pokemon2):
    "Wyrdeer"
    def __init__(self,name="Wyrdeer",type1="Normal",type2="Psychic",nature=None,level=100,happiness=255,hp=103,atk=105,defense=72,spatk=105,spdef=75,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intimidate",item="Leftovers"):
        if move is None:
            avmoves=["Psyshield Bash","Zen Headbutt","Double-Edge","Wild Charge","Megahorn","Rest","High Horsepower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Vikavolt
class Vikavolt(Pokemon2):
    "Vikavolt"
    def __init__(self,name="Vikavolt",type1="Bug",type2="Electric",nature=None,level=100,happiness=255,hp=77,atk=70,defense=90,spatk=145,spdef=75,speed=43,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Levitate",item=random.choice(["Leftovers","Occa Berry"])):
        if move is None:
            avmoves=["Protect","Thunderbolt","Thunder Wave","Zap Cannon","Energy Ball","Crunch","Bug Buzz","Thunder","Sticky Web","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Midday Lycanroc
class MDLycanroc(Pokemon2):
    "Lycanroc"
    def __init__(self,name="Midday Lycanroc",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=75,atk=115,defense=65,spatk=55,spdef=65,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sand Rush",item="Leftovers"):
        if move is None:
            avmoves=["Accelerock","Stone Edge","Crunch","Sucker Punch","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Midnight Lycanroc
class MNLycanroc(Pokemon2):
    "Lycanroc"
    def __init__(self,name="Midnight Lycanroc",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=85,atk=115,defense=75,spatk=55,spdef=75,speed=82,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="No Guard",item="Leftovers"):
        if move is None:
            avmoves=["Accelerock","Stone Edge","Crunch","Close Combat","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Dusk Lycanroc
class DLycanroc(Pokemon2):
    "Lycanroc"
    def __init__(self,name="Dusk Lycanroc",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=75,atk=117,defense=75,spatk=55,spdef=65,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tough Claws",item="Leftovers"):
        if move is None:
            avmoves=["Accelerock","Stone Edge","Crunch","Sucker Punch","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #School Wishiwashi
class SWishiwashi(Pokemon2):
    "Wishiwashi"
    def __init__(self,name="School Wishiwashi",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=55,atk=140,defense=130,spatk=140,spdef=135,speed=30,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Schooling",item="Leftovers"):
        if move is None:
            avmoves=["Hydro Pump","Water Spout","Double-Edge","Soak","Rest","Rain Dance","Scald","Ice Beam","Earth Power","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Toxapex
class Toxapex(Pokemon2):
    "Toxapex"
    def __init__(self,name="Toxapex",type1="Poison",type2="Water",nature=None,level=100,happiness=255,hp=50,atk=63,defense=152,spatk=53,spdef=142,speed=35,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Black Sludge"):
        if move is None:
            avmoves=["Baneful Bunker","Toxic","Liquidation","Toxic Spikes","Scald","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mudsdale
class Mudsdale(Pokemon2):
    "Mudsdale"
    def __init__(self,name="Mudsdale",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=100,atk=125,defense=100,spatk=55,spdef=85,speed=35,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Stamina","Tangling Hair"]),item="Leftovers"):
        if move is None:
            avmoves=["High Horsepower","Stone Edge","Earthquake","Heavy Slam","Iron Defense"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Araquanid
class Araquanid(Pokemon2):
    "Araquanid"
    def __init__(self,name="Araquanid",type1="Water",type2="Bug",nature=None,level=100,happiness=255,hp=68,atk=70,defense=92,spatk=50,spdef=132,speed=42,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Water Absorb",item="Leftovers"):
        if move is None:
            avmoves=["Leech Life","Lunge","Liquidation","Crunch","Scald","Ice Beam","X-Scissor","Sticky Web","Aqua Ring"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Salazzle
class Salazzle(Pokemon2):
    "Salazzle"
    def __init__(self,name="Salazzle",type1="Poison",type2="Fire",nature=None,level=100,happiness=255,hp=68,atk=64,defense=60,spatk=111,spdef=60,speed=117,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Corrosion",item="Black Sludge"):
        if move is None:
            avmoves=["Fire Lash","Toxic","Flamethrower","Toxic Spikes","Dragon Pulse","Nasty Plot","Sludge Bomb","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Salobber
class Salobber(Pokemon2):
    def __init__(self,name="Salobber",type1="Poison",type2="Fire",nature=None,level=100,happiness=255,hp=58,atk=111,defense=60,spatk=64,spdef=60,speed=127,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Corrosion",item="Black Sludge"):
        if move is None:
            avmoves=["Fire Lash","Toxic","Flare Blitz","Toxic Spikes","Swords Dance","Sludge Bomb","Poison Jab","Fire Fang","Cross Poison"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                
#Bewear
class Bewear(Pokemon2):
    "Bewear"
    def __init__(self,name="Bewear",type1="Normal",type2="Fighting",nature=None,level=100,happiness=255,hp=120,atk=125,defense=80,spatk=55,spdef=60,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Fluffy",item="Leftovers"):
        if move is None:
            avmoves=["Superpower","Double-Edge","Hammer Arm","Strength","High Horsepower","Zen Headbutt","Darkest Lariat","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Tsareena
class Tsareena(Pokemon2):
    "Tsareena"
    def __init__(self,name="Tsareena",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=72,atk=120,defense=98,spatk=50,spdef=98,speed=72,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Queenly Majesty","Striker"]),item="Leftovers"):
        if move is None:
            avmoves=["Trop Kick","High Jump Kick","Power Whip","Play Rough","Grass Knot","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Golisopod
class Golisopod(Pokemon2):
    "Golisopod"
    def __init__(self,name="Golisopod",type1="Bug",type2="Water",nature=None,level=100,happiness=255,hp=75,atk=125,defense=140,spatk=60,spdef=90,speed=40,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Tough Claws",item="Leftovers"):
        if move is None:
            avmoves=["Leech Life","First Impression","Liquidation","Crunch","Swords Dance","Ice Beam","X-Scissor","Razor Shell","Sucker Punch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Palossand
class Palossand(Pokemon2):
    "Palossand"
    def __init__(self,name="Palossand",type1="Ghost",type2="Ground",nature=None,level=100,happiness=255,hp=85,atk=75,defense=110,spatk=100,spdef=75,speed=35,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Water Compaction",item="Leftovers"):
        if move is None:
            avmoves=["Shore Up","Earth Power","Shadow Ball","Giga Drain","Sandstorm","Sludge Bomb","Destiny Bond"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Silvally
class Silvally(Pokemon2):
    "Silvally"
    def __init__(self,name="Silvally",type1=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]),type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["RKS System"]),item="Elemental Disks"):
        if move is None:
            avmoves=["Protect","Multi-Attack","Hyper Beam","Double-Edge","Crush Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        name=name+"-"+type1
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Turtonator
class Turtonator(Pokemon2):
    "Turtonator"
    def __init__(self,name="Turtonator",type1="Fire",type2="Dragon",nature=None,level=100,happiness=255,hp=70,atk=58,defense=135,spatk=91,spdef=85,speed=36,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Dauntless Shield","Shell Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Shell Trap","Shell Smash","Overheat","Flamethrower","Dragon Pulse","Iron Defense","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Mimikyu
class Mimikyu(Pokemon2):
    "Mimikyu"
    def __init__(self,name="Mimikyu",type1="Ghost",type2="Fairy",nature=None,level=100,happiness=255,hp=55,atk=90,defense=80,spatk=50,spdef=105,speed=96,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Disguise",item="Leftovers"):
        if move is None:
            avmoves=["Shadow Sneak","Play Rough","Shadow Claw","Wood Hammer","Swords Dance","Destiny Bond","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Drampa
class Drampa(Pokemon2):
    "Drampa"
    def __init__(self,name="Drampa",type1="Normal",type2="Dragon",nature=None,level=100,happiness=255,hp=103,atk=50,defense=85,spatk=135,spdef=91,speed=36,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Berserk","Sap Sipper","Fatal Precision"]),item="Leftovers"):
        if move is None:
            avmoves=["Hyper Voice","Dragon Pulse","Extrasensory","Hyper Beam","Hurricane","Ice Beam","Energy Ball","Focus Blast","Heat Wave","Light Screen","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dhelmise
class Dhelmise(Pokemon2):
    "Delmise"
    def __init__(self,name="Dhelmise",type1="Ghost",type2="Grass",nature=None,level=100,happiness=255,hp=70,atk=131,defense=100,spatk=86,spdef=90,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Steelworker",item="Leftovers"):
        if move is None:
            avmoves=["Power Whip","Phantom Force","Shadow Ball","Heavy Slam"]
            moves=moveset(avmoves,3)+["Anchor Shot"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Kommo-o
class Kommo(Pokemon2):
    "Kommo-o"
    def __init__(self,name="Kommo-o",type1="Dragon",type2="Fighting",nature=None,level=100,happiness=255,hp=75,atk=110,defense=125,spatk=100,spdef=105,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Overcoat","Bulletproof"]),item="Throat Spray"):
        if move is None:
            avmoves=["Hyper Voice","Dragon Pulse","Focus Blast","Aura Sphere","Flash Cannon","Scale Shot"]
            moves=moveset(avmoves,2)+["Clangorous Soul","Clanging Scales"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Tapu Koko
class Tapukoko(Pokemon2):
    "Tapu Koko"
    def __init__(self,name="Tapu Koko",type1="Electric",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=115,defense=85,spatk=95,spdef=75,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Electric Surge"]),item="Leftovers"):
        if move is None:
            avmoves=["Nature's Madness","Wild Charge","Play Rough","Brave Bird","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Tapu Lele
class Tapulele(Pokemon2):
    "Tapu Lele"
    def __init__(self,name="Tapu Lele",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=85,defense=75,spatk=130,spdef=115,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Psychic Surge"]),item="Leftovers"):
        if move is None:
            avmoves=["Nature's Madness","Extrasensory","Moonblast","Psyshock","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Tapu Bulu
class Tapubulu(Pokemon2):
    "Tapu Bulu"
    def __init__(self,name="Tapu Bulu",type1="Grass",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=130,defense=115,spatk=85,spdef=95,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Grassy Surge"]),item="Leftovers"):
        if move is None:
            avmoves=["Nature's Madness","Horn Leech","Play Rough","Wood Hammer","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                       
        #Tapu Fini
class Tapufini(Pokemon2):
    "Tapu Fini"
    def __init__(self,name="Tapu Fini",type1="Water",type2="Fairy",nature=None,level=100,happiness=255,hp=70,atk=75,defense=115,spatk=95,spdef=130,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Misty Surge"]),item="Leftovers"):
        if move is None:
            avmoves=["Nature's Madness","Hydro Pump","Moonblast","Surf"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Solgaleo
class Solgaleo(Pokemon2):
    "Solgaleo"
    def __init__(self,name="Solgaleo",type1="Psychic",type2="Steel",nature=None,level=100,happiness=255,hp=137,atk=137,defense=107,spatk=113,spdef=89,speed=97,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Full Metal Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Sunsteel Strike","Flare Blitz","Solar Beam","Wild Charge","Morning Sun","Zen Headbutt","Meteor Beam","Steel Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Radiant Sun Solgaleo
class RSSolgaleo(Pokemon2):
    "Solgaleo"
    def __init__(self,name="Radiant Sun Solgaleo",type1="Psychic",type2="Steel",nature=None,level=100,happiness=255,hp=137,atk=157,defense=107,spatk=113,spdef=89,speed=97,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Full Metal Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Sunsteel Strike","Flare Blitz","Solar Beam","Wild Charge","Morning Sun","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Lunala
class Lunala(Pokemon2):
    "Lunala"
    def __init__(self,name="Lunala",type1="Psychic",type2="Ghost",nature=None,level=100,happiness=255,hp=137,atk=113,defense=89,spatk=157,spdef=107,speed=97,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Shadow Shield"]),item="Leftovers"):
        if move is None:
            avmoves=["Moongeist Beam","Phamtom Force","Moonblast","Night Daze","Moonlight","Shadow Ball","Psychic","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Full Moon Lunala
class FMLunala(Pokemon2):
    "Lunala"
    def __init__(self,name="Full Moon Lunala",type1="Psychic",type2="Ghost",nature=None,level=100,happiness=255,hp=137,atk=113,defense=89,spatk=137,spdef=107,speed=97,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Shadow Shield"]),item="Leftovers"):
        if move is None:
            avmoves=["Moongeist Beam","Phamtom Force","Moonblast","Night Daze","Moonlight","Shadow Ball","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Dusk Mane Necrozma
class DMNecrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Dusk Mane Necrozma",type1="Psychic",type2="Steel",nature=None,level=100,happiness=255,hp=97,atk=157,defense=127,spatk=113,spdef=109,speed=77,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Prism Armor"]),item="Ultranecrozium Z"):
        if move is None:
            avmoves=["Sunsteel Strike","Flare Blitz","Solar Beam","Photon Geyser","Prismatic Laser","Morning Sun","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Dawn Wing Necrozma
class DWNecrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Dawn Wing Necrozma",type1="Psychic",type2="Ghost",nature=None,level=100,happiness=255,hp=97,atk=113,defense=109,spatk=157,spdef=127,speed=77,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Prism Armor"]),item="Ultranecrozium Z"):
        if move is None:
            avmoves=["Moongeist Beam","Shadow Ball","Moonblast","Photon Geyser","Prismatic Laser","Moonlight","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Necrozma
class Necrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Necrozma",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=97,atk=107,defense=101,spatk=127,spdef=89,speed=79,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Prism Armor"]),item="Ultranecrozium Z"):
        if move is None:
            avmoves=["Moonlight","Iron Defense","Rock Blast","Photon Geyser","Prismatic Laser","Morning Sun","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Nihilego
class Nihilego(Pokemon2):
    "Nihilego"
    def __init__(self,name="Nihilego",type1="Rock",type2="Poison",nature=None,level=100,happiness=255,hp=109,atk=53,defense=47,spatk=127,spdef=131,speed=103,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Venom Drench","Iron Defense","Toxic Spikes","Stealth Rock","Venoshock","Power Gem","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Buzzwole
class Buzzwole(Pokemon2):
    "Buzzwole"
    def __init__(self,name="Buzzwole",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=107,atk=139,defense=139,spatk=53,spdef=53,speed=79,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Lunge","Superpower","Bulk Up","Fell Stinger","Power-up Punch","Close Combat","Drain Punch","Darkest Lariat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Pheromosa
class Pheromosa(Pokemon2):
    "Pheromosa"
    def __init__(self,name="Pheromosa",type1="Rock",type2="Poison",nature=None,level=100,happiness=255,hp=71,atk=137,defense=37,spatk=137,spdef=37,speed=151,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["U-Turn","Triple Axel","High Jump Kick","Quiver Dance","Bug Buzz","Lunge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Xurkitree
class Xurkitree(Pokemon2):
    "Xurkitree"
    def __init__(self,name="Xurkitree",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=83,atk=69,defense=71,spatk=173,spdef=71,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Eerie Impulse","Thunderbolt","Electric Terrain","Power Whip","Discharge","Hypnosis"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Celesteela
class Celesteela(Pokemon2):
    "Celesteela"
    def __init__(self,name="Celesteela",type1="Steel",type2="Flying",nature=None,level=100,happiness=255,hp=97,atk=101,defense=103,spatk=107,spdef=101,speed=61,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Heavy Slam","Iron Defense","Leech Seed","Flash Cannon","Giga Drain","Meteor Beam","Flamethrower","Autotomize"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Kartana
class Kartana(Pokemon2):
    "Kartana"
    def __init__(self,name="Kartana",type1="Grass",type2="Steel",nature=None,level=100,happiness=255,hp=59,atk=181,defense=131,spatk=59,spdef=31,speed=109,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Sacred Sword","Leaf Blade","Night Slash","Smart Strike"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Guzzlord
class Guzzlord(Pokemon2):
    "Guzzlord"
    def __init__(self,name="Guzzlord",type1="Dark",type2="Dragon",nature=None,level=100,happiness=255,hp=203,atk=101,defense=73,spatk=97,spdef=73,speed=23,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Heavy Slam","Belch","Hammer Arm","Stomping Tantrum","Knock Off","Dragon Rush"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Necrozma
class UNecrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Ultra Necrozma",type1="Psychic",type2="Dragon",nature=None,level=100,happiness=255,hp=97,atk=167,defense=97,spatk=167,spdef=97,speed=129,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Neuroforce"]),item="Ultranecrozium Z"):
        if move is None:
            avmoves=["Moonlight","Iron Defense","Rock Blast","Photon Geyser","Prismatic Laser","Morning Sun"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Magearna
class Magearna(Pokemon2):
    "Magearna"
    def __init__(self,name="Magearna",type1="Steel",type2="Fairy",nature=None,level=100,happiness=255,hp=80,atk=95,defense=115,spatk=130,spdef=115,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Soul-Heart"]),item="Leftovers"):
        if move is None:
            avmoves=["Fleur Cannon","Zap Cannon","Flash Cannon","Aura Sphere"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Marshadow
class Marshadow(Pokemon2):
    "Marshadow"
    def __init__(self,name="Marshadow",type1="Fighting",type2="Ghost",nature=None,level=100,happiness=255,hp=90,atk=125,defense=80,spatk=90,spdef=90,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Technician"]),item="Leftovers"):
        if move is None:
            avmoves=["Spectral Thief","Superpower","Bulk Up","Drain Punch","Power-up Punch","Close Combat","Sucker Punch","Shadow Sneak"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Naganadel
class Naganadel (Pokemon2):
    "Naganadel"
    def __init__(self,name="Naganadel",type1="Poison",type2="Dragon",nature=None,level=100,happiness=255,hp=73,atk=73,defense=73,spatk=127,spdef=73,speed=121,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Dragon Pulse","Sludge Wave","Nasty Plot","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Stakataka
class Stakataka(Pokemon2):
    "Stakataka"
    def __init__(self,name="Stakataka",type1="Rock",type2="Steel",nature=None,level=100,happiness=255,hp=61,atk=131,defense=211,spatk=53,spdef=101,speed=13,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Iron Head","Iron Defense","Double-Edge","Stealth Rock","Heavy Slam","Rock Slide","Meteor Beam","Autotomize"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Blacephalon
class Blacephalon(Pokemon2):
    "Blacephalon"
    def __init__(self,name="Blacephalon",type1="Fire",type2="Ghost",nature=None,level=100,happiness=255,hp=53,atk=127,defense=53,spatk=151,spdef=79,speed=107,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beast Boost"]),item="Leftovers"):
        if move is None:
            avmoves=["Mind Blown","Fire Blast","Shadow Ball","Mystical Fire"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zeraora
class Zeraora(Pokemon2):
    "Zeraora"
    def __init__(self,name="Zeraora",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=88,atk=112,defense=75,spatk=102,spdef=80,speed=143,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Volt Absorb"]),item="Leftovers"):
        if move is None:
            avmoves=["Plasma Fists","Close Combat","Wild Charge","Thunder Punch","Volt Switch","Power-up Punch","Aura Sphere"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Melmetal
class Melmetal(Pokemon2):
    "Melmetal"
    def __init__(self,name="Melmetal",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=135,atk=143,defense=143,spatk=80,spdef=65,speed=34,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Iron Fist"]),item="Leftovers"):
        if move is None:
            avmoves=["Superpower","Thunder Punch","Ice Punch","Fire Punch","Iron Defense"]
            moves=moveset(avmoves,3)+["Double Iron Bash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
                                                                                    #Galarian Rapidash
class GRapidash(Pokemon2):
    "Rapidash"
    def __init__(self,name="Galarian Rapidash",type1="Fire",type2="Fairy",nature=None,level=100,happiness=255,hp=65,atk=100,defense=70,spatk=80,spdef=80,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire","Reckless"]),item="Leftovers"):
        if move is None:
            avmoves=["Megahorn","Psycho Cut","Play Rough","Drill Run","High Horsepower","Wild Charge","Flare Blitz","Expanding Force"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Slowbro
class GSlowbro(Pokemon2):
    "Slowbro"
    def __init__(self,name="Galarian Slowbro",type1="Poison",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=75,defense=105,spatk=115,spdef=70,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Regenerator","Quick Draw","Own Tempo"]),item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Sludge Bomb","Thunderbolt","Iron Defense","Rain Dance","Expanding Force","Chilling Water","Yawn"]
            moves=moveset(avmoves,3)+["Shell Side Arm "]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Weezing
class GWeezing(Pokemon2):
    "Weezing"
    def __init__(self,name="Galarian Weezing",type1="Poison",type2="Fairy",nature=None,level=100,happiness=255,hp=65,atk=90,defense=120,spatk=85,spdef=70,speed=60,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate","Misty Surge"]),item="Black Sludge"):
        if move is None:
            avmoves=["Sludge Bomb","Toxic","Venoshock","Explosion","Toxic Spikes","Strange Stream","Misty Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Medicrow
class Medicrow(Pokemon2):
    def __init__(self,name="Medicrow",type1="Fairy",type2="Poison",nature=None,level=100,happiness=255,hp=65,atk=50,defense=60,spatk=125,spdef=70,speed=90,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Levitate","Misty Surge"]),item="Black Sludge"):
        if move is None:
            avmoves=["Sludge Bomb","Toxic","Sludge Wave","Toxic Spikes","Dazzling Gleam","Moonblast","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Articuno
class GArticuno(Pokemon2):
    "Articuno"
    def __init__(self,name="Galarian Articuno",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=75,defense=95,spatk=125,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Competitive",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Psychic","Extrasensory","Brave Bird","Sky Attack","Roost","Expanding Force"]
            moves=moveset(avmoves,3)+["Freezing Glare"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Zapdos
class GZapdos(Pokemon2):
    "Zapdos"
    def __init__(self,name="Galarian Zapdos",type1="Fighting",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=125,defense=90,spatk=85,spdef=90,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Defiant",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Brave Bird","Close Combat","Sky Attack","Roost","Bulk Up"]
            moves=moveset(avmoves,3)+["Thunderous Kick"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Moltres
class GMoltres(Pokemon2):
    "Moltres"
    def __init__(self,name="Galarian Moltres",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=90,atk=85,defense=90,spatk=100,spdef=125,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Berserk",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Hidden Power","Hurricane","Nasty Plot","Sky Attack","Brave Bird","Sucker Punch","Roost","Tailwind"]
            moves=moveset(avmoves,3)+["Fiery Wrath"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Slowking
class GSlowking(Pokemon2):
    "Slowking"
    def __init__(self,name="Galarian Slowking",type1="Poison",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=65,defense=80,spatk=110,spdef=110,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Curious Medicine",item=random.choice(["Leftovers","Icy Rock"])):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Sludge Bomb","Thunderbolt","Iron Defense","Rain Dance","Eerie Spell","Toxic Spikes","Yawn"]
            moves=moveset(avmoves,3)+["Chilly Reception"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Rillaboom
class Rillaboom(Pokemon2):
    "Rillaboom"
    def __init__(self,name="Rillaboom",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=100,atk=125,defense=90,spatk=60,spdef=70,speed=85,hpev=0,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Grassy Surge","Overgrow"]),item="Choice Band"):
        if move is None:
            avmoves=["Drum Beating","Wood Hammer","Grassy Glide","Swords Dance","Knock Off","Superpower","Acrobatics","High Horsepower","Drain Punch","U-Turn","Darkest Lariat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Cinderace
class Cinderace(Pokemon2):
    "Cinderace"
    def __init__(self,name="Cinderace",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=80,atk=116,defense=75,spatk=65,spdef=75,speed=119,hpev=80,atkev=164,defev=0,spatkev=0,spdefev=48,speedev=216,maxiv="No",move=None, ability=random.choice(["Libero","Blaze"]),item="Heavy-Duty Boots"):
        if move is None:
            avmoves=["Pyro Ball","Court Change","U-Turn","Sucker Punch","Gunk Shot","Zen Headbutt","High Jump Kick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Inteleon
class Inteleon(Pokemon2):
    "Inteleon"
    def __init__(self,name="Inteleon",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=70,atk=85,defense=65,spatk=125,spdef=65,speed=120,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sniper","Torrent"]),item=random.choice(["Expert Belt","Scope Lens"])):
        if move is None:
            avmoves=["Snipe Shot","Ice Beam","Shadow Ball","U-Turn","Knock Off","Hydro Pump","Dark Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Corviknight
class Corviknight(Pokemon2):
    "Corviknight"
    def __init__(self,name="Corviknight",type1="Flying",type2="Steel",nature=None,level=100,happiness=255,hp=98,atk=87,defense=105,spatk=53,spdef=85,speed=67,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Pressure","Mirror Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Roost","Brave Bird","Defog","U-Turn","Body Press","Steel Wing"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Orbeetle
class Orbeetle(Pokemon2):
    "Orbeetle"
    def __init__(self,name="Orbeetle",type1="Bug",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=45,defense=110,spatk=80,spdef=120,speed=90,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Swarm","Frisk"]),item="Expert Belt"):
        if move is None:
            avmoves=["Reflect","Light Screen","Sticky Web","U-Turn","Body Press","Calm Mind","Extrasensory","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Rabsca
class Rabsca(Pokemon2):
    def __init__(self,name="Rabsca",type1="Bug",type2="Psychic",nature=None,level=100,happiness=255,hp=75,atk=50,defense=85,spatk=115,spdef=100,speed=45,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Synchronize"]),item="Expert Belt"):
        if move is None:
            avmoves=["Reflect","Light Screen","Sticky Web","U-Turn","Body Press","Calm Mind","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Coalossal
class Coalossal(Pokemon2):
    "Coalossal"
    def __init__(self,name="Coalossal",type1="Rock",type2="Fire",nature=None,level=100,happiness=255,hp=110,atk=80,defense=120,spatk=80,spdef=90,speed=30,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Steam Engine","Flash Fire"]),item="Heavy-Duty Boots"):
        if move is None:
            avmoves=["Stealth Rock","Rock Blast","Flamethrower","Rapid Spin","Earth Power","Body Press","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Garganacl
class Garganacl(Pokemon2):
    def __init__(self,name="Garganacl",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=100,atk=100,defense=130,spatk=45,spdef=90,speed=35,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Purifying Salt","Clear Body","Sturdy"]),item="Heavy-Duty Boots"):
        if move is None:
            avmoves=["Stealth Rock","Rock Blast","Rapid Spin","Earth Power","Body Press","Meteor Beam","Explosion","Heavy Slam","Earthquake","Recover","Hammer Arm"]
            moves=moveset(avmoves,3)+["Salt Cure"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
                               
                                                                             
#Flapple
class Flapple(Pokemon2):
    "Flapple"
    def __init__(self,name="Flapple",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=75,atk=110,defense=80,spatk=95,spdef=60,speed=70,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Ripen","Hustle"]),item="Life Orb"):
        if move is None:
            avmoves=["Grab Apple","Outrage","Sucker Punch","U-Turn","Grassy Glide","Dragon Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Appletun
class Appletun(Pokemon2):
    "Appletun"
    def __init__(self,name="Appletun",type1="Grass",type2="Dragon",nature=None,level=100,happiness=255,hp=110,atk=85,defense=80,spatk=100,spdef=80,speed=30,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Ripen","Thick Fat"]),item="Leftovers"):
        if move is None:
            avmoves=["Draco Meteor","Outrage","Apple Acid","Recover","Giga Drain","Dragon Pulse","Leech Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Sandaconda
class Sandaconda(Pokemon2):
    "Sandaconda"
    def __init__(self,name="Sandaconda",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=72,atk=107,defense=125,spatk=65,spdef=70,speed=71,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Sand Spit","Sand Veil"]),item="Leftovers"):
        if move is None:
            avmoves=["Coil","Sandstorm","Glare","Recover","Earthquake","Drill Run","Stealth Rock","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Centiskorch
class Centiskorch(Pokemon2):
    "Centiskorch"
    def __init__(self,name="Centiskorch",type1="Fire",type2="Bug",nature=None,level=100,happiness=255,hp=100,atk=115,defense=65,spatk=90,spdef=90,speed=65,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Flash Fire","Flame Body","Mountaineer"]),item="Leftovers"):
        if move is None:
            avmoves=["Lunge","Fire Lash","Coil","Crunch","Inferno","Power Whip","X-Scissor","Flare Blitz","Leech Life"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Toxtricity
class Toxtricity(Pokemon2):
    "Toxtricity"
    def __init__(self,name="Toxtricity",type1="Electric",type2="Poison",nature=random.choice(naturelist),level=100,happiness=255,hp=75,atk=98,defense=70,spatk=114,spdef=70,speed=75,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Punk Rock","Technician"]),item="Throat Spray"):
        if move is None:
            avmoves=["Boomburst","Overdrive","Sludge Wave","Hyper Voice","Volt Switch"]
            moves=moveset(avmoves)
        if nature in ['Hardy', 'Brave', 'Adamant', 'Naughty', 'Docile', 'Impish', 'Lax', 'Hasty', 'Jolly', 'Naive', 'Rash', 'Sassy','Quirky']:
            name="Amped "+name
        if nature not in ['Hardy', 'Brave', 'Adamant', 'Naughty', 'Docile', 'Impish', 'Lax', 'Hasty', 'Jolly', 'Naive', 'Rash', 'Sassy','Quirky']:
            name="Low Key "+name
        if move is not None:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Barraskewda
class Barraskewda(Pokemon2):
    "Barraskewda"
    def __init__(self,name="Barraskewda",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=61,atk=123,defense=60,spatk=60,spdef=50,speed=136,hpev=0,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Propeller Tail","Swift Swim"]),item="Leftovers"):
        if move is None:
            avmoves=["Liquidation","Double-Edge","Aqua Jet","Crunch","Psychic Fangs","Close Combat","Poison Jab","Waterfall","Ice Fang","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Grapplot
class Grapplot(Pokemon2):
    "Grapplot"
    def __init__(self,name="Grapplot",type1="Fighting",type2="Water",nature=None,level=100,happiness=255,hp=80,atk=118,defense=90,spatk=70,spdef=80,speed=42,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Technician","Limber"]),item="Leftovers"):
        if move is None:
            avmoves=["Octolock","Superpower","Topsy-Turvy","Submission","Bulk Up","Close Combat","Focus Blast","Brick Break","Octazooka"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Polteageist
class Polteageist (Pokemon2):
    "Polteageist"
    def __init__(self,name="Polteageist",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=60,atk=65,defense=65,spatk=134,spdef=114,speed=70,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Weak Armor"]),item="Focus Sash"):
        if move is None:
            avmoves=["Shell Smash","Giga Drain","Shadow Ball","Stored Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Hatterene
class Hatterene(Pokemon2):
    "Hatterene"
    def __init__(self,name="Hatterene",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=57,atk=90,defense=95,spatk=136,spdef=103,speed=29,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Magic Bounce"]),item="Leftovers"):
        if move is None:
            avmoves=["Calm Mind","Dazzling Gleam","Mystical Fire","Moonblast","Psychic","Draining Kiss","Trick Room","Expanding Force","Misty Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Grimmsnarl
class Grimmsnarl(Pokemon2):
    "Grimmsnarl"
    def __init__(self,name="Grimmsnarl",type1="Dark",type2="Fairy",nature=None,level=100,happiness=255,hp=95,atk=120,defense=65,spatk=95,spdef=75,speed=60,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Prankster"]),item="Leftovers"):
        if move is None:
            avmoves=["Light Screen","Reflect","Spirit Break","Play Rough","Dark Pulse","Sucker Punch","False Surrender","Taunt","Metronome","Darkest Lariat","Parting Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Obstagoon
class Obstagoon(Pokemon2):
    "Obstagoon"
    def __init__(self,name="Obstagoon",type1="Dark",type2="Normal",nature=None,level=100,happiness=255,hp=93,atk=90,defense=101,spatk=60,spdef=81,speed=95,hpev=0,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Guts","Defiant"]),item="Leftovers"):
        if move is None:
            avmoves=["Obstruct","Double-Edge","Close Combat","Snarl","Night Slash","Sucker Punch","Throat Chop","Cross Chop"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Kleavor
class Kleavor(Pokemon2):
    "Kealvor"
    def __init__(self,name="Kleavor",type1="Bug",type2="Rock",nature=None,level=100,happiness=255,hp=70,atk=135,defense=95,spatk=45,spdef=70,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sharpness",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Stone Axe","Stealth Rock","X-Scissor","U-Turn","Swords Dance","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Perrserker
class Perrserker(Pokemon2):
    "Perrserker"
    def __init__(self,name="Perrserker",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=90,atk=110,defense=100,spatk=30,spdef=60,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Tough Claws",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Iron Head","Slash","Iron Defense","Play Rough","Swords Dance","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Sirfetchd
class Sirfetchd(Pokemon2):
    "Sirfetchd"
    def __init__(self,name="Sirfetch'd",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=82,atk=135,defense=95,spatk=68,spdef=82,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Scrappy","Sharpness"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Sacred Sword","Leaf Blade","Night Slash","Meteor Assault","Brave Bird"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #MrRime
class MrRime(Pokemon2):
    "MrRime"
    def __init__(self,name="Mr.Rime",type1="Ice",type2="Psychic",nature=None,level=100,happiness=255,hp=80,atk=65,defense=75,spatk=110,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Ice Body","Screen Cleaner"]),item="Leftovers"):
        if move is None:
            avmoves=["Psychic","Ice Shard","Freeze-Dry","Sucker Punch","Dazzling Gleam","Grass Knot","Expanding Force"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Alcremie
class Alcremie(Pokemon2):
    "Alcremie"
    def __init__(self,name="Alcremie",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=65,atk=60,defense=75,spatk=110,spdef=121,speed=64,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sweet Veil",item="Leftovers"):
        if move is None:
            avmoves=["Misty Terrain","Freeze-Dry","Draining Kiss","Dazzling Gleam","Calm Mind","Misty Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Frosmoth
class Frosmoth(Pokemon2):
    "Frosmoth"
    def __init__(self,name="Frosmoth",type1="Ice",type2="Bug",nature=None,level=100,happiness=255,hp=70,atk=65,defense=65,spatk=125,spdef=90,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Ice Scales","Shield Dust"]),item="Leftovers"):
        if move is None:
            avmoves=["Defog","Ice Shard","Freeze-Dry","Bug Buzz","Tailwind","Quiver Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Indeedee
class Indeedee(Pokemon2):
    "Indeedee"
    def __init__(self,name="Indeedee",type1="Psychic",type2="Normal",nature=None,level=100,happiness=255,hp=60,atk=65,defense=55,spatk=105,spdef=95,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Psychic Surge",item=random.choice(["Psychic Seed","Terrain Extender"])):
        if move is None:
            avmoves=["Psychic","Expanding Force","Calm Mind","Stored Power","Metronome","Mystical Fire","Hyper Voice","Shadow Ball","Draining Kiss"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Copperajah
class Copperajah(Pokemon2):
    "Copperajah"
    def __init__(self,name="Copperajah",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=122,atk=130,defense=79,spatk=80,spdef=79,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Sheer Force","Heavy Metal"]),item="Leftovers"):
        if move is None:
            avmoves=["Heavy Slam","High Horsepower","Iron Head","Play Rough","Bulldoze"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dracozolt
class Dracozolt(Pokemon2):
    "Dracozolt"
    def __init__(self,name="Dracozolt",type1="Electric",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=100,defense=90,spatk=80,spdef=70,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sand Rush","Hustle"]),item="Leftovers"):
        if move is None:
            avmoves=["Bolt Beak","Dragon Rush","Dragon Tail","Wild Charge","Earthquake","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dracovish
class Dracovish(Pokemon2):
    "Dracovish"
    def __init__(self,name="Dracovish",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=90,atk=90,defense=100,spatk=70,spdef=80,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Strong Jaw",item="Choice Scarf"):
        if move is None:
            avmoves=["Fishious Rend","Dragon Rush","Ice Fang","Thunder Fang","Earthquake","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Duraludon
class Duraludon(Pokemon2):
    "Duraludon"
    def __init__(self,name="Duraludon",type1="Steel",type2="Dragon",nature=None,level=100,happiness=255,hp=85,atk=95,defense=115,spatk=120,spdef=50,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Stalwart","Heavy Metal"]),item="Leftovers"):
        if move is None:
            avmoves=["Draco Meteor","Steel Beam","Flash Cannon","Dark Pulse","Iron Defense","Breaking Swipe","Dark Pulse","Thunderbolt","Heavy Slam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Dragapult
class Dragapult(Pokemon2):
    "Dragapult"
    def __init__(self,name="Dragapult",type1="Dragon",type2="Ghost",nature=None,level=100,happiness=255,hp=88,atk=120,defense=75,spatk=100,spdef=75,speed=142,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Infiltrator",item="Choice Band"):
        if move is None:
            avmoves=["Dragon Darts","Draco Meteor","Phantom Force","Flamethrower","Thunderbolt","U-Turn","Shadow Ball","Dragon Pulse"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zacian
class Zacian(Pokemon2):
    "Zacian"
    def __init__(self,name="Crowned Sword Zacian",type1="Fairy",type2="Steel",nature=None,level=100,happiness=255,hp=92,atk=170,defense=115,spatk=80,spdef=115,speed=148,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Intrepid Sword",item="Rusted Sword"):
        if move is None:
            avmoves=["Behemoth Blade","Play Rough","Protect","Crunch","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Zamazenta
class Zamazenta(Pokemon2):
    "Zamazenta"
    def __init__(self,name="Crowned Shield Zamazenta",type1="Fighting",type2="Steel",nature=None,level=100,happiness=255,hp=92,atk=130,defense=145,spatk=80,spdef=145,speed=128,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Dauntless Shield",item="Rusted Shield"):
        if move is None:
            avmoves=["Behemoth Bash","Close Combat","Protect","Crunch","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Eternatus
class Eternatus(Pokemon2):
    "Eternatus"
    def __init__(self,name="Eternatus",type1="Poison",type2="Dragon",nature=None,level=100,happiness=255,hp=140,atk=85,defense=95,spatk=145,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item="Power Herb"):
        if move is None:
            avmoves=["Dynamax Cannon","Eternabeam","Flamethrower","Sludge Bomb","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Urshifu
class DUrshifu(Pokemon2):
    "Urshifu"
    def __init__(self,name="Single Strike Urshifu",type1="Fighting",type2="Dark",nature=None,level=100,happiness=255,hp=100,atk=130,defense=100,spatk=63,spdef=60,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Unseen Fist",item=random.choice(["Choice Band","Muscle Band"])):
        if move is None:
            avmoves=["Wicked Blow","Close Combat","U-Turn","Sucker Punch","Darkest Lariat","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Urshifu
class WUrshifu(Pokemon2):
    "Urshifu"
    def __init__(self,name="Rapid Strike Urshifu",type1="Fighting",type2="Water",nature=None,level=100,happiness=255,hp=100,atk=130,defense=100,spatk=63,spdef=60,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Unseen Fist",item=random.choice(["Choice Band","Muscle Band"])):
        if move is None:
            avmoves=["Surging Strikes","Close Combat","U-Turn","Aqua Jet","Swords Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Zarude
class Zarude(Pokemon2):
    "Zarude"
    def __init__(self,name="Zarude",type1="Dark",type2="Grass",nature=None,level=100,happiness=255,hp=105,atk=120,defense=105,spatk=70,spdef=95,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Leaf Guard",item=random.choice(["Heavy Duty Boots","Leftovers","Choice Scarf"])):
        if move is None:
            avmoves=["Jungle Healing","Power Whip","U-Turn","Darkest Lariat","Swords Dance","Trailblaze","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Regieleki
class Regieleki(Pokemon2):
    "Regieleki"
    def __init__(self,name="Regieleki",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=80,atk=100,defense=50,spatk=100,spdef=50,speed=200,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Transistor",item="Life Orb"):
        if move is None:
            avmoves=["Thunder Cage","Explosion","Thunderbolt","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Regidrago
class Regidrago(Pokemon2):
    "Regidrago"
    def __init__(self,name="Regidrago",type1="Dragon",type2=None,nature=None,level=100,happiness=255,hp=200,atk=100,defense=50,spatk=100,spdef=50,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Dragon's Maw",item="Leftovers"):
        if move is None:
            avmoves=["Dragon Energy","Explosion","Dragon Pulse","Hyper Beam","Earthquake","Earth Power","Fire Fang","Ice Fang","Thunder Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Glastrier
class Glastrier(Pokemon2):
    "Glastrier"
    def __init__(self,name="Glastrier",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=100,atk=145,defense=130,spatk=65,spdef=110,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Chilling Neigh",item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Icicle Crash","High Horsepower","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Spectrier
class Spectrier(Pokemon2):
    "Spectrier"
    def __init__(self,name="Spectrier",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=100,atk=65,defense=60,spatk=145,spdef=80,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Grim Neigh",item="Leftovers"):
        if move is None:
            avmoves=["Nasty Plot","Shadow Ball","Dark Pulse","Hex"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Calyrex
class ICalyrex(Pokemon2):
    "Calyrex"
    def __init__(self,name="Ice Rider Calyrex",type1="Psychic",type2="Ice",nature=None,level=100,happiness=255,hp=100,atk=165,defense=150,spatk=85,spdef=130,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="As One",item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Glacial Lance","High Horsepower","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Calyrex
class SCalyrex(Pokemon2):
    "Calyrex"
    def __init__(self,name="Shadow Rider Calyrex",type1="Psychic",type2="Ghost",nature=None,level=100,happiness=255,hp=100,atk=85,defense=80,spatk=165,spdef=100,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="As One",item="Leftovers"):
        if move is None:
            avmoves=["Nasty Plot","Astral Barrage","Dark Pulse","Hex"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Cetitan
class Cetitan(Pokemon2):
    "Cetitan"
    def __init__(self,name="Cetitan",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=170,atk=113,defense=65,spatk=45,spdef=55,speed=73,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Thick Fat","Slush Rush"]),item="Leftovers"):
        if move is None:
            avmoves=["Belly Drum","Icicle Crash","Protect","Stone Edge","Ice Spinner","Ice Shard","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Koraidon
class Koraidon(Pokemon2):
    "Koraidon"
    def __init__(self,name="Koraidon",type1="Dragon",type2="Fighting",nature=None,level=100,happiness=255,hp=100,atk=135,defense=115,spatk=85,spdef=100,speed=135,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Orichalcum Pulse"]),item=random.choice(["Choice Band","Life Orb","Leftovers","Choice Scarf"])):
        if move is None:
            avmoves=["Extreme Speed","Superpower","Close Combat","Dragon Claw","U-Turn","Heavy Slam","Flare Blitz","Swords Dance","Flame Charge","Stomping Tantrum","Outrage"]
            moves=moveset(avmoves,3)+["Collision Course"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Miraidon
class Miraidon(Pokemon2):
    "Miraidon"
    def __init__(self,name="Miraidon",type1="Dragon",type2="Electric",nature=None,level=100,happiness=255,hp=100,atk=85,defense=100,spatk=135,spdef=115,speed=135,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hadron Engine"]),item=random.choice(["Choice Specs","Choice Scarf","Heavy Duty Boots","Leftovers"])):
        if move is None:
            avmoves=["Dragon Pulse","Overheat","Thunder","Volt Switch","Draco Meteor","Parabolic Charge","U-Turn","Dazzling Gleam","Calm Mind","Taunt"]
            moves=moveset(avmoves,3)+["Electro Drift"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Enamorus
class Enamorus(Pokemon2):
    "Enamorus"
    def __init__(self,name="Enamorus",type1="Fairy",type2="Flying",nature=None,level=100,happiness=255,hp=74,atk=115,defense=70,spatk=135,spdef=80,speed=106,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Trace","Fairy Aura"]),item="Leftovers"):
        if move is None:
            avmoves=["Springtide Storm","Moonblast","Extrasensory","Focus Blast","Draining Kiss","Hurricane"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Enamorus
class TEnamorus(Pokemon2):
    "Enamorus"
    def __init__(self,name="Therian Enamorus",type1="Fairy",type2="Flying",nature=None,level=100,happiness=255,hp=74,atk=115,defense=110,spatk=135,spdef=100,speed=46,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Trace","Fairy Aura"]),item="Leftovers"):
        if move is None:
            avmoves=["Springtide Storm","Moonblast","Extrasensory","Focus Blast","Draining Kiss","Hurricane"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Butterfree
class Butterfree(Pokemon2):
    "Butterfree"
    def __init__(self,name="Butterfree",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=45,defense=60,spatk=95,spdef=90,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens","Compound Eyes"]),item="Leftovers"):
        if move is None:
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Tailwind","Psychic","Sleep Powder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Vivillon
class Vivillon(Pokemon2):
    def __init__(self,name="Vivillon",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=80,atk=52,defense=50,spatk=90,spdef=50,speed=89,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens","Compound Eyes"]),item="Leftovers"):
        if move is None:
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Tailwind","Sleep Powder","Hurricane","Light Screen","Draining Kiss"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Beedrill
class Beedrill(Pokemon2):
    "Beedrill"
    def __init__(self,name="Beedrill",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=65,atk=90,defense=40,spatk=45,spdef=80,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper",item="Black Sludge"):
        if move is None:
            avmoves=["Poison Jab","Knock Off","Sludge Bomb","Drill Run","Toxic Spikes","Endeavor"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Raticate
class Raticate(Pokemon2):
    "Raticate"
    def __init__(self,name="Raticate",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=60,atk=91,defense=60,spatk=45,spdef=70,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Guts","Hustle"]),item="Life Orb"):
        if move is None:
            avmoves=["Swords Dance","Knock Off","Crunch","Sucker Punch","Double-Edge","Super Fang","Endeavor"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Smeargle
class Smeargle(Pokemon2):
    def __init__(self,name="Smeargle",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=55,atk=20,defense=35,spatk=20,spdef=45,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Technician","Moody","Own Tempo"]),item="Focus Sash"):
        if move is None:
            avmoves=typemoves.allmove
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Gumshoos
class Gumshoos(Pokemon2):
    def __init__(self,name="Gumshoos",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=98,atk=110,defense=60,spatk=55,spdef=60,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Stakeout","Strong Jaw","Adaptability"]),item="Life Orb"):
        if move is None:
            avmoves=["Swords Dance","Knock Off","Super Fang","Sucker Punch","Double-Edge","Crunch","Rest","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#ARaticate
class ARaticate(Pokemon2):
    "Raticate"
    def __init__(self,name="Alolan Raticate",type1="Normal",type2="Dark",nature=None,level=100,happiness=255,hp=75,atk=86,defense=70,spatk=40,spdef=80,speed=77,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Thick Fat","Hustle"]),item="Sitrus Berry"):
        if move is None:
            avmoves=["Swords Dance","Knock Off","Crunch","Sucker Punch","Double-Edge","Super Fang"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Fearow
class Fearow(Pokemon2):
    "Fearow"
    def __init__(self,name="Fearow",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=100,defense=65,spatk=61,spdef=61,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Technician","Sniper","Frisk"]),item="Sharp Beak"):
        if move is None:
            avmoves=["U-Turn","Drill Peck","Drill Run","Dual Wingbeat","Brave Bird","Roost","Steel Wing"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Pikachu
class Pikachu(Pokemon2):
    "Pikachu"
    def __init__(self,name="Pikachu",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=45,atk=80,defense=50,spatk=75,spdef=60,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Static",item="Light Ball"):
        if move is None:
            avmoves=["Extreme Speed","Volt Tackle","Iron Tail","Electroweb","Electro Ball","Thunder"]
            moves=moveset(avmoves,3)+["Thunderbolt"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Emolga
class Emolga(Pokemon2):
    def __init__(self,name="Emolga",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=55,atk=55,defense=60,spatk=95,spdef=60,speed=103,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Static","Lightning Rod","Motor Drive"]),item="Electric Gem"):
        if move is None:
            avmoves=["Acrobatics","Volt Switch","Electro Ball","Thunder","Light Screen"]
            moves=moveset(avmoves,3)+["Thunderbolt"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Heliolisk
class Heliolisk(Pokemon2):
    def __init__(self,name="Heliolisk",type1="Electric",type2="Normal",nature=None,level=100,happiness=255,hp=62,atk=55,defense=52,spatk=109,spdef=94,speed=109,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Solar Beam",item="Sitrus Berry"):
        if move is None:
            avmoves=["Volt Switch","Electro Ball","Thunder","Thunderbolt","Scale Shot"]
            moves=moveset(avmoves,3)+["Parabolic Charge"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
#Raichu
class Raichu(Pokemon2):
    "Raichu"
    def __init__(self,name="Raichu",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=70,atk=100,defense=55,spatk=100,spdef=80,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Static","Lightning Rod"]),item="Leftovers"):
        if move is None:
            avmoves=["Extreme Speed","Volt Tackle","Iron Tail","Thunderbolt","Electroweb","Electro Ball","Thunder","Fake Out","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Pincurchin
class Pincurchin(Pokemon2):
    "Raichu"
    def __init__(self,name="Pincurchin",type1="Electric",type2="Water",nature=None,level=100,happiness=255,hp=68,atk=81,defense=95,spatk=91,spdef=85,speed=15,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Electric Surge",item="Electric Seed"):
        if move is None:
            avmoves=["Zing Zap","Discharge","Thunder Wave","Chilling Water","Rest","Toxic Spikes"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Gorochu
class Gorochu(Pokemon2):
    def __init__(self,name="Gorochu",type1="Electric",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=115,defense=65,spatk=120,spdef=80,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Competitive",item="Leftovers"):
        if move is None:
            avmoves=["Extreme Speed","Volt Tackle","Iron Tail","Thunderbolt","Electroweb","Electro Ball","Thunder","Fake Out","Nasty Plot","Dark Pulse","Night Slash","Crunch","Rain Dance","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                            
#ARaichu
class ARaichu(Pokemon2):
    "Raichu"
    def __init__(self,name="Alolan Raichu",type1="Electric",type2="Psychic",nature=None,level=100,happiness=255,hp=60,atk=85,defense=50,spatk=95,spdef=85,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Surge Surfer",item="Leftovers"):
        if move is None:
            avmoves=["Extreme Speed","Volt Tackle","Grass Knot","Thunderbolt","Psychic","Electro Ball","Thunder","Fake Out","Nasty Plot","Expanding Force"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Sandslash
class Sandslash(Pokemon2):
    "Sandslash"
    def __init__(self,name="Sandslash",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=75,atk=110,defense=120,spatk=25,spdef=65,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sand Rush","Sand Veil"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Crush Claw","Earthquake","Gyro Ball","Bulldoze","Rock Slide","Rapid Spin"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Cochungus
class Cochungus(Pokemon2):
    def __init__(self,name="Cochungus",type1="Normal",type2="Ground",nature=None,level=100,happiness=255,hp=125,atk=100,defense=90,spatk=25,spdef=95,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Unaware","Oblivious"]),item="Leftovers"):
        if move is None:
            avmoves=["Rest","Slack Off","Earthquake","Body Slam","Bulldoze","Rock Slide","Return"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                     
                 #Sandslash
class ASandslash(Pokemon2):
    "Sandslash"
    def __init__(self,name="Alolan Sandslash",type1="Ice",type2="Steel",nature=None,level=100,happiness=255,hp=75,atk=110,defense=120,spatk=25,spdef=65,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Slush Rush","Snow Cloak","Icicle Scales"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Spiky Shield","Icicle Crash","Gyro Ball","Ice Shard","Icicle Spear","Steel Beam","Rapid Spin"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Clefable
class Clefable(Pokemon2):
    "Clefable"
    def __init__(self,name="Clefable",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=95,atk=76,defense=73,spatk=95,spdef=90,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Magic Guard",item="Leftovers"):
        if move is None:
            avmoves=["Cosmic Power","Moonblast","Meteor Mash","Stored Power","Moonlight","Meteor Beam","Metronome","Misty Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Wigglytuff
class Wigglytuff(Pokemon2):
    def __init__(self,name="Wigglytuff",type1="Normal",type2="Fairy",nature=None,level=100,happiness=255,hp=140,atk=70,defense=45,spatk=85,spdef=50,speed=45,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Competitive","Sheer Force","Frisk"]),item="Leftovers"):
        if move is None:
            avmoves=["Body Slam","Moonblast","Rest","Play Rough","Gyro Ball","Expanding Force","Misty Explosion"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Vileplume
class Vileplume(Pokemon2):
    def __init__(self,name="Vileplume",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=85,atk=80,defense=85,spatk=110,spdef=90,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Effect Spore"]),item="Black Sludge"):
        if move is None:
            avmoves=["Grassy Terrain","Moonblast","Giga Drain","Sleep Powder","Moonlight","Sludge Bomb","Toxic","Apple Acid","Strength Sap","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Parasect
class Parasect(Pokemon2):
    def __init__(self,name="Parasect",type1="Bug",type2="Grass",nature=None,level=100,happiness=255,hp=80,atk=110,defense=100,spatk=60,spdef=80,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Dry Skin","Effect Spore","Damp"]),item="Leftovers"):
        if move is None:
            avmoves=["Spore","X-Scissor","Giga Drain","Cross Poison","Synthesis","Leaf Blade"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                                                                                                 #Venomoth
class Venomoth(Pokemon2):
    def __init__(self,name="Venomoth",type1="Bug",type2="Psychic",nature=None,level=100,happiness=255,hp=70,atk=65,defense=65,spatk=95,spdef=75,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens","Shield Dust","Wonder Skin"]),item="Black Sludge"):
        if move is None:
            avmoves=["Quiver Dance","Bug Buzz","Giga Drain","Psychic","Sleep Powder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Dugtrio
class Dugtrio(Pokemon2):
    def __init__(self,name="Dugtrio",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=45,atk=100,defense=60,spatk=50,spdef=70,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sand Force","Sand Veil"]),item="Leftovers"):
        if move is None:
            avmoves=["Sucker Punch","Earthquake","Night Slash","Bulldoze","Rock Slide","Scorching Sands","Shadow Claw","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
        #Wugtrio
class Wugtrio(Pokemon2):
    def __init__(self,name="Wugtrio",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=45,atk=100,defense=60,spatk=50,spdef=70,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Rain Dish","Water Veil"]),item="Leftovers"):
        if move is None:
            avmoves=["Sucker Punch","Hydro Pump","Night Slash","Liquidation","Ice Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                             
        #Dugtrio
class ADugtrio(Pokemon2):
    def __init__(self,name="Dugtrio",type1="Ground",type2="Steel",nature=None,level=100,happiness=255,hp=45,atk=110,defense=60,spatk=50,spdef=70,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tangling Hair","Sand Veil"]),item="Leftovers"):
        if move is None:
            avmoves=["Sucker Punch","Earthquake","Night Slash","Bulldoze","Iron Head","Steel Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Persian
class Persian(Pokemon2):
    def __init__(self,name="Persian",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=65,atk=80,defense=60,spatk=60,spdef=65,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Technician","Feline Prowess"]),item="Leftovers"):
        if move is None:
            avmoves=["Play Rough","Sucker Punch","Slash","Night Slash","Fake Out","U-Turn","Shadow Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Persian
class APersian(Pokemon2):
    def __init__(self,name="Alolan Persian",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=65,atk=60,defense=60,spatk=55,spdef=65,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Feline Prowess","Fur Coat","Technician"]),item="Leftovers"):
        if move is None:
            avmoves=["Nasty Plot","Sucker Punch","Power Gem","Dark Pulse","Fake Out","U-Turn","Shadow Ball","Taunt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Kingler
class Kingler(Pokemon2):
    def __init__(self,name="Kingler",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=65,atk=130,defense=115,spatk=50,spdef=50,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sheer Force","Shell Armor","Hyper Cutter"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Crabhammer","Razor Shell","Hammer Arm","X-Scissor","Rock Slide","Waterfall","Liquidation"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Klawf
class Klawf(Pokemon2):
    def __init__(self,name="Klawf",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=70,atk=100,defense=115,spatk=35,spdef=55,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Shell Armor","Anger Shell"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","Crabhammer","Stone Edge","Hammer Arm","X-Scissor","Rock Slide","Bulldoze"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
                                                      
        #Hypno
class Hypno(Pokemon2):
    def __init__(self,name="Hypno",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=85,atk=73,defense=70,spatk=73,spdef=115,speed=67,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Psychic Surge","Insomnia"]),item=random.choice(["Psychic Seed","Terrain Extender"])):
        if move is None:
            avmoves=["Nasty Plot","Psyshock","Psychic","Dark Pulse","Hypnosis","Thunder Wave","Shadow Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Electrode
class Electrode(Pokemon2):
    "Electrode"
    def __init__(self,name="Electrode",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=60,atk=55,defense=70,spatk=100,spdef=80,speed=140,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Static","Galvanize","Soundproof"]),item="Leftovers"):
        if move is None:
            avmoves=["Thunder","Thunderbolt","Thunder Wave","Hyper Beam","Rest","Explosion","Reflect","Light Screen"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Marowak
class Marowak(Pokemon2):
    def __init__(self,name="Marowak",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=110,spatk=30,spdef=80,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Rock Head","Bone Zone","Battle Armor"]),item="Leftovers"):
        if move is None:
            avmoves=["Bone Rush","Bonemerang","Earthquake","Stomping Tantrum","Bulldoze","Rock Slide","Swords Dance","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Marowak
class AMarowak(Pokemon2):
    def __init__(self,name="Alolan Marowak",type1="Fire",type2="Ghost",nature=None,level=100,happiness=255,hp=80,atk=80,defense=110,spatk=30,spdef=80,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Rock Head","Bone Zone"]),item="Leftovers"):
        if move is None:
            avmoves=["Bone Rush","Bonemerang","Earthquake","Will-O-Wisp","Bulldoze","Rock Slide","Swords Dance","Stealth Rock","Shadow Bone"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Rhydon
class Rhydon(Pokemon2):
    def __init__(self,name="Rhydon",type1="Ground",type2="Rock",nature=None,level=100,happiness=255,hp=105,atk=130,defense=120,spatk=45,spdef=45,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Rock Head",item=random.choice(["Eviolite"])):
        if move is None:
            avmoves=["Protect","Stone Edge","Hammer Arm","High Horsepower","Thunder Punch","Giga Impact","Stealth Rock","Horn Drill","Double-Edge","Meteor Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Chansey
class Chansey(Pokemon2):
    def __init__(self,name="Chansey",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=250,atk=5,defense=5,spatk=35,spdef=105,speed=50,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=4,speedev=0,maxiv="No",move=None, ability="Natural Cure",item="Eviolite"):
        if move is None:
            avmoves=["Protect","Soft Boiled","Toxic","Seismic Toss","Light Screen","Reflect","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Seaking
class Seaking(Pokemon2):
    def __init__(self,name="Seaking",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=80,atk=92,defense=65,spatk=65,spdef=80,speed=68,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Lightning Rod","Swift Swim","Rain Dish"]),item="Leftovers"):
        if move is None:
            avmoves=["Fishious Rend","Megahorn","Horn Drill","Poison Jab","Swords Dance","Rain Dance","Waterfall","Liquidation","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Palafin
class Palafin(Pokemon2):
    def __init__(self,name="Palafin",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=100,atk=70,defense=72,spatk=53,spdef=62,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Zero to Hero"]),item="Leftovers"):
        if move is None:
            avmoves=["Wave Crash","Aqua Tail","Acrobatics","Flip Turn","Close Combat","Iron Head"]
            moves=moveset(avmoves,3)+["Jet Punch"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                
#Mr.Mime
class MrMime(Pokemon2):
    def __init__(self,name="Mr.Mime",type1="Psychic",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=45,defense=65,spatk=100,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Psychic Surge",item=random.choice(["Psychic Seed","Terrain Extender"])):
        if move is None:
            avmoves=["Psychic","Dazzling Gleam","Sucker Punch","Encore","Light Screen","Reflect","Expanding Force","Metronome"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Scyther
class Scyther(Pokemon2):
    def __init__(self,name="Scyther",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=70,atk=110,defense=80,spatk=55,spdef=80,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Eviolite"):
        if move is None:
            avmoves=["Swords Dance","Slash","X-Scissor","U-Turn","Roost","Dual Wingbeat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
        #Ditto
class Ditto(Pokemon2):
    "Ditto"
    def __init__(self,name="Ditto",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=40,atk=40,defense=40,spatk=40,spdef=40,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Imposter",item="Choice Scarf"):
        if move is None:
            moves=["Transform","Protect","Recover","Light Screen"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Furret
class Furret(Pokemon2):
    def __init__(self,name="Furret",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=86,defense=64,spatk=45,spdef=55,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Sitrus Berry"):
        if move is None:
            avmoves=["Belly Drum","Return","Extreme Speed","Sucker Punch","Double-Edge","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Noctowl        
class Noctowl(Pokemon2):
    def __init__(self,name="Noctowl",type1="Normal",type2="Flying",nature=None,level=100,happiness=255,hp=110,atk=50,defense=50,spatk=76,spdef=96,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Tinted Lens",item=random.choice(["Choice Specs","Life Orb","Flying Gem"])):
        if move is None:
            avmoves=["Hidden Power","Hurricane","Hypnosis","Brave Bird","U-Turn","Air Slash","Moonblast","Psychic","Roost","Extrasensory","Reflect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Ledian    
class Ledian(Pokemon2):
    "Ledian"
    def __init__(self,name="Ledian",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=55,atk=90,defense=50,spatk=35,spdef=100,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Iron Fist",item=random.choice(["Choice Band","Life Orb","Bug Gem"])):
        if move is None:
            avmoves=["Power-Up Punch","Fire Punch","Ice Punch","Thunder Punch","U-Turn","Mach Punch","Victory Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        #Ariados       
class Ariados(Pokemon2):
    def __init__(self,name="Ariados",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=70,atk=95,defense=70,spatk=60,spdef=60,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Sniper",item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["Toxic Thread","Swords Dance","Sucker Punch","Poison Jab","U-Turn","Gunk Shot","Sticky Web","Cross Poison","Megahorn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                        
#Xatu
class Xatu(Pokemon2):
    def __init__(self,name="Xatu",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=75,defense=70,spatk=105,spdef=70,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Magic Bounce",item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["Air Slash","Night Shade","Stored Power","Tailwind","U-Turn","Calm Mind","Grass Knot","Psychic","Thunder Wave"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                
#Bellossom
class Bellossom(Pokemon2):
    def __init__(self,name="Bellossom",type1="Grass",type2="Fairy",nature=None,level=100,happiness=255,hp=75,atk=80,defense=95,spatk=90,spdef=100,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Chlorophyll",item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["Moonlight","Petal Dance","Grassy Terrain","Moonblast","Sleep Powder","Quiver Dance","Giga Drain","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Sudowoodo
class Sudowoodo(Pokemon2):
    def __init__(self,name="Sudowoodo",type1="Rock",type2=None,nature=None,level=100,happiness=255,hp=90,atk=100,defense=115,spatk=30,spdef=65,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Rock Head",item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["Head Smash","Double-Edge","Low Kick","Rock Slide","Sucker Punch","Wood Hammer","Stone Edge","Hammer Arm","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Jumpluff
class Jumpluff(Pokemon2):
    def __init__(self,name="Jumpluff",type1="Grass",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=85,defense=70,spatk=35,spdef=95,speed=110,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Fluffy","Aerilate"]),item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["U-Turn","Acrobatics","Leech Seed","Bullet Seed","Sleep Powder","Synthesis","Giga Drain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Sunflora
class Sunflora(Pokemon2):
    def __init__(self,name="Sunflora",type1="Grass",type2="Fire",nature=None,level=100,happiness=255,hp=95,atk=75,defense=55,spatk=135,spdef=85,speed=55,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Solar Power"]),item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["Growth","Leaf Storm","Leech Seed","Sunny Day","Solar Beam","Synthesis","Giga Drain","Flamethrower","Seed Flare"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Quagsire
class Quagsire(Pokemon2):
    def __init__(self,name="Quagsire",type1="Water",type2="Ground",nature=None,level=100,happiness=255,hp=100,atk=85,defense=90,spatk=65,spdef=65,speed=35,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Water Absorb","Damp","Unaware"]),item=random.choice(["Life Orb","Rindo Berry"])):
        if move is None:
            avmoves=["Earthquake","Toxic","Amnesia","Aqua Tail","Muddy Water","Stealth Rock","Toxic Spikes","Chilling Water","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Clodsire
class Clodsire(Pokemon2):
    def __init__(self,name="Clodsire",type1="Poison",type2="Ground",nature=None,level=100,happiness=255,hp=95,atk=85,defense=85,spatk=65,spdef=65,speed=35,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Corrosion",item=random.choice(["Life Orb","Sitrus Berry"])):
        if move is None:
            avmoves=["Earthquake","Toxic","Amnesia","Poison Tail","Chilling Water","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Slowking
class Slowking(Pokemon2):
    "Slowking"
    def __init__(self,name="Slowking",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=95,atk=65,defense=80,spatk=110,spdef=110,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Surf","Thunderbolt","Iron Defense","Rain Dance","Yawn"]
            moves=moveset(avmoves,3)+["Chilly Reception"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Wobbuffet
class Wobbuffet(Pokemon2):
    def __init__(self,name="Wobbuffet",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=190,atk=33,defense=58,spatk=33,spdef=58,speed=33,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Shadow Tag",item="Leftovers"):
        if move is None:
            avmoves=["Counter","Mirror Coat","Destiny Bond","Recover"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Forretress
class Forretress(Pokemon2):
    def __init__(self,name="Forretress",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=75,atk=90,defense=140,spatk=60,spdef=60,speed=40,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Sturdy",item="Leftovers"):
        if move is None:
            avmoves=["Iron Defense","Gyro Ball","Heavy Slam","Explosion","Stealth Rock","Reflect","Rapid Spin","Body Press"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Granbull
class Granbull(Pokemon2):
    def __init__(self,name="Grabull",type1="Fairy",type2="Fighting",nature=None,level=100,happiness=255,hp=100,atk=120,defense=75,spatk=60,spdef=60,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Intimidate","Strong Jaw"]),item="Leftovers"):
        if move is None:
            avmoves=["Play Rough","Crunch","Outrage","Fire Fang","Ice Fang","Thunder Fang","Bulk Up","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Shuckle
class Shuckle(Pokemon2):
    def __init__(self,name="Shuckle",type1="Bug",type2="Rock",nature=None,level=100,happiness=255,hp=20,atk=10,defense=230,spatk=10,spdef=230,speed=5,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Sturdy","Contrary","Solid Rock"]),item="Leftovers"):
        if move is None:
            avmoves=["Iron Defense","Gyro Ball","Heavy Slam","Explosion","Stealth Rock","Reflect","Rapid Spin","Sticky Web","Cosmic Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Ursaring
class Ursaring(Pokemon2):
    def __init__(self,name="Ursaring",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=90,atk=130,defense=75,spatk=75,spdef=75,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Intimidate","Guts"]),item="Eviolite"):
        if move is None:
            avmoves=["Facade","Hammer Arm","Rest","Slash","Strength","Return","Swords Dance","Rock Slide","Shadow Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Magcargo
class Magcargo(Pokemon2):
    def __init__(self,name="Magcargo",type1="Fire",type2="Rock",nature=None,level=100,happiness=255,hp=50,atk=50,defense=120,spatk=80,spdef=80,speed=30,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Flame Body",item="Leftovers"):
        if move is None:
            avmoves=["Shell Smash","Flamethrower","Earth Power","Recover","Body Slam","Lava Plume","Ancient Power","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Corsola
class Corsola(Pokemon2):
    def __init__(self,name="Corsola",type1="Water",type2="Rock",nature=None,level=100,happiness=255,hp=55,atk=55,defense=85,spatk=65,spdef=85,speed=35,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item="Leftovers"):
        if move is None:
            avmoves=["Ancient Power","Recover","Earth Power","Explosion","Stealth Rock","Reflect","Power Gem"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Corsola
class GCorsola(Pokemon2):
    def __init__(self,name="Galarian Corsola",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=60,atk=55,defense=100,spatk=65,spdef=100,speed=30,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Cursed Body",item="Eviolite"):
        if move is None:
            avmoves=["Ancient Power","Night Shade","Earth Power","Strength Sap","Stealth Rock","Reflect","Power Gem"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Cursola
class Cursola(Pokemon2):
    def __init__(self,name="Cursola",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=80,atk=75,defense=50,spatk=145,spdef=130,speed=55,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Weak Armor","Unburden","Perish Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Ancient Power","Night Shade","Earth Power","Strength Sap","Stealth Rock","Reflect","Power Gem"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                
#Octillery
class Octillery(Pokemon2):
    def __init__(self,name="Octillery",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=75,atk=105,defense=75,spatk=105,spdef=75,speed=75,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Moody","Sniper","Skill Link","Mega Launcher"]),item="Leftovers"):
        if move is None:
            avmoves=["Octazooka","Hydro Pump","Ice Beam","Bullet Seed","Gunk Shot","Rock Blast","Surf"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Delibird
class Delibird(Pokemon2):
    def __init__(self,name="Delibird",type1="Ice",type2="Flying",nature=None,level=100,happiness=255,hp=45,atk=100,defense=45,spatk=65,spdef=45,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hustle","Surprise"]),item="Leftovers"):
        if move is None:
            avmoves=["Drill Peck","Dual Wingbeat","Rest","Toxic","Present"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Mantine
class Mantine(Pokemon2):
    def __init__(self,name="Mantine",type1="Water",type2="Flying",nature=None,level=100,happiness=255,hp=65,atk=40,defense=70,spatk=90,spdef=140,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Water Absorb","Swift Swim"]),item="Leftovers"):
        if move is None:
            avmoves=["Air Slash","Hydro Pump","Ice Beam","Roost","Rain Dance","Scald","Surf"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Donphan
class Donphan(Pokemon2):
    def __init__(self,name="Donphan",type1="Ground",type2=None,nature=None,level=100,happiness=255,hp=90,atk=120,defense=120,spatk=60,spdef=60,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Sturdy","Technician"]),item="Leftovers"):
        if move is None:
            avmoves=["Bulldoze","Earthquake","Ice Shard","Rock Tomb","Knock Off","Assurance","Rock Slide","Rapid Spin"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Porygon2
class Porygon2(Pokemon2):
    def __init__(self,name="Porygon2",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=80,defense=90,spatk=105,spdef=95,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=0,maxiv="No",move=None, ability="Download",item="Eviolite"):
        if move is None:
            avmoves=["Protect","Ice Beam","Calm Mind","Recover","Thunderbolt","Flamethrower","Signal Beam","Hidden Power","Psychic","Shadow Ball","Hyper Beam","Trick Room"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
        #Miltank
class Miltank(Pokemon2):
    def __init__(self,name="Miltank",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=95,atk=85,defense=105,spatk=40,spdef=70,speed=100,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Thick Fat","Sap Sipper","Scrappy"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Milk Drink","Body Slam","High Horsepower","Double-Edge","Play Rough","Giga Impact","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
        #Mewtwo
class MMewtwoY(Pokemon2):
    "Mewtwo"
    def __init__(self,name="Mega Mewtwo Y",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=106,atk=150,defense=70,spatk=194,spdef=120,speed=140,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Pressure",item=random.choice(["Mewtwonite Y"])):
        if move is None:
            avmoves=["Protect","Hidden Power","Shadow Ball","Dark Pulse","Ice Beam","Focus Blast","Expanding Force","Aura Sphere","Power Gem","Earth Power"]
            moves=moveset(avmoves,3)+["Psystrike"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
        #Ceruledge
class Ceruledge(Pokemon2):
    def __init__(self,name="Ceruledge",type1="Fire",type2="Ghost",nature=None,level=100,happiness=255,hp=65,atk=115,defense=80,spatk=60,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Slash","Swords Dance","Bitter Blade","Flare Blitz","Shadow Sneak"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
        #Armarouge
class Armarouge(Pokemon2):
    def __init__(self,name="Armarouge",type1="Fire",type2="Psychic",nature=None,level=100,happiness=255,hp=65,atk=60,defense=80,spatk=115,spdef=70,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flash Fire"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psychic","Calm Mind","Armor Cannon","Fire Blast","Extrasensory"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Linoone
class Linoone(Pokemon2):
    def __init__(self,name="Linoone",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=78,atk=80,defense=61,spatk=50,spdef=61,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item="Sitrus Berry"):
        if move is None:
            avmoves=["Belly Drum","Return","Extreme Speed","Sucker Punch","Double-Edge","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Beautifly
class Beautifly(Pokemon2):
    def __init__(self,name="Beautifly",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=60,atk=70,defense=50,spatk=100,spdef=50,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens","Compound Eyes"]),item="Leftovers"):
        if move is None:
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Tailwind","Psychic","Sleep Powder","Giga Drain","Morning Sun"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Dustox
class Dustox(Pokemon2):
    def __init__(self,name="Dustox",type1="Bug",type2="Poison",nature=None,level=100,happiness=255,hp=60,atk=50,defense=70,spatk=50,spdef=90,speed=65,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Shield Dust","Compound Eyes"]),item="Leftovers"):
        if move is None:
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Toxic","Light Screen","Sleep Powder","Moonlight"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Masquerain
class Masquerain(Pokemon2):
    def __init__(self,name="Masquerain",type1="Bug",type2="Water",nature=None,level=100,happiness=255,hp=80,atk=60,defense=62,spatk=80,spdef=82,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens","Intimidate"]),item="Leftovers"):
        if move is None:
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Sticky Web","Psychic","Sleep Powder","Hurricane","Hydro Pump","Chilling Water"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Ninjask
class Ninjask(Pokemon2):
    def __init__(self,name="Ninjask",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=61,atk=100,defense=45,spatk=50,spdef=50,speed=160,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Speed Boost","Infiltrator"]),item="Leftovers"):
        if move is None:
            avmoves=["Swords Dance","U-Turn","X-Scissor","Roost","Night Slash","Final Gambit"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Shedinja
class Shedinja(Pokemon2):
    def __init__(self,name="Shedinja",type1="Bug",type2="Ghost",nature=None,level=100,happiness=255,hp=1,atk=90,defense=45,spatk=30,spdef=30,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Wonder Guard"]),item="Focus Sash"):
        if move is None:
            avmoves=["X-Scissor","Phantom Force","Shadow Ball","Shadow Sneak","Shadow Claw"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                         
#Sableye
class Sableye(Pokemon2):
    def __init__(self,name="Sableye",type1="Dark",type2="Ghost",nature=None,level=100,happiness=255,hp=50,atk=75,defense=75,spatk=65,spdef=65,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Prankster",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Shade","Shadow Sneak","Power Gem","Zen Headbutt","Knock Off","Foul Play","Moonlight","Metronome"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Grafaiai
class Grafaiai(Pokemon2):
    def __init__(self,name="Grafaiai",type1="Poison",type2="Normal",nature=None,level=100,happiness=255,hp=63,atk=95,defense=65,spatk=80,spdef=72,speed=110,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Poison Touch","Prankster"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Poison Jab","Venoshock","Toxic","Return","Doodle"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                
#Mawile
class Mawile(Pokemon2):
    def __init__(self,name="Mawile",type1="Steel",type2="Fairy",nature=None,level=100,happiness=255,hp=50,atk=85,defense=85,spatk=55,spdef=55,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Intimidate",item="Life Orb"):
        if move is None:
            avmoves=["Protect","Iron Head","Play Rough","Crunch","Sucker Punch","Iron Defense","Stealth Rock"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
        #Manectric
class Manectric(Pokemon2):
    def __init__(self,name="Manectric",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=70,atk=75,defense=60,spatk=105,spdef=60,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Intimidate","Static","Lightning Rod"]),item="Manectite"):
        if move is None:
            avmoves=["Protect","Volt Switch","Thunder","Crunch","Thunderbolt","Wild Charge","Hyper Beam","Thunder Wave","Flamethrower","Electric Terrain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Swalot
class Swalot(Pokemon2):
    def __init__(self,name="Swalot",type1="Poison",type2=None,nature=None,level=100,happiness=255,hp=100,atk=53,defense=88,spatk=93,spdef=88,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Gluttony","Liquid Ooze","Magic Guard"]),item="Black Sludge"):
        if move is None:
            avmoves=["Protect","Sludge Bomb","Gunk Shot","Body Slam","Belch","Toxic","Ice Beam","Toxic Spikes","Body Press","Swords Dance","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Grumpig
class Grumpig(Pokemon2):
    def __init__(self,name="Grumpig",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=90,atk=45,defense=65,spatk=90,spdef=110,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Thick Fat",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Psychic","Psyshock","Body Slam","Rest","Power Gem","Belch","Nasty Plot","Snarl","Dazzling Gleam","Earth Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Cacturne
class Cacturne(Pokemon2):
    def __init__(self,name="Cacturne",type1="Grass",type2="Dark",nature=None,level=100,happiness=255,hp=70,atk=120,defense=60,spatk=120,spdef=60,speed=55,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Water Absorb","Sand Rush","Sand Veil"]),item="Black Glasses"):
        if move is None:
            avmoves=["Spiky Shield","Leech Seed","Poison Jab","Assurance","Sucker Punch","Needle Arm","Energy Ball","Grass Knot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Dusclops
class Dusclops(Pokemon2):
    def __init__(self,name="Dusclops",type1="Ghost",type2=None,nature=None,level=100,happiness=255,hp=40,atk=70,defense=130,spatk=60,spdef=130,speed=25,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Pressure"]),item=random.choice(["Eviolite"])):
        if move is None:
            avmoves=["Protect","Will-O-Wisp","Thunder Wave","Shadow Punch","Hex","Calm Mind","Rest","Trick Room","Metronome","Pain Split"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Tropius
class Tropius(Pokemon2):
    def __init__(self,name="Tropius",type1="Grass",type2="Flying",nature=None,level=100,happiness=255,hp=99,atk=68,defense=83,spatk=92,spdef=87,speed=81,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Solar Power","Harvest"]),item="Leftovers"):
        if move is None:
            avmoves=["Dragon Hammer","Dragon Dance","Solar Beam","Leaf Storm","Air Slash","Body Slam","Energy Balll","Grass Knot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Bibarel
class Bibarel(Pokemon2):
    def __init__(self,name="Bibarel",type1="Normal",type2="Water",nature=None,level=100,happiness=255,hp=79,atk=85,defense=80,spatk=55,spdef=80,speed=71,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Moody","Unaware","Simple"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Aqua Jet","Super Fang","Superpower","Swords Dance","Crunch","Waterfall","Grass Knot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Kricketune
class Kricketune(Pokemon2):
    def __init__(self,name="Kricketune",type1="Bug",type2=None,nature=None,level=100,happiness=255,hp=77,atk=95,defense=71,spatk=55,spdef=71,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Technician",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Night Slash","X-Scissor","Slash","Swords Dance","Hypnosis","Sticky Web"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Wormadam
class SWormadam(Pokemon2):
    def __init__(self,name="Sandy Wormadam",type1="Bug",type2="Ground",nature=None,level=100,happiness=255,hp=60,atk=79,defense=105,spatk=59,spdef=85,speed=36,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Quiver Dance","Rock Blast","Psychic","Sucker Punch","Earthquake"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Wormadam
class Wormadam(Pokemon2):
    def __init__(self,name="Wormadam",type1="Bug",type2="Grass",nature=None,level=100,happiness=255,hp=60,atk=59,defense=85,spatk=79,spdef=105,speed=36,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Quiver Dance","Leaf Storm","Psychic","Sucker Punch","Giga Drain"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Wormadam
class TWormadam(Pokemon2):
    def __init__(self,name="Trash Wormadam",type1="Bug",type2="Steel",nature=None,level=100,happiness=255,hp=60,atk=69,defense=95,spatk=69,spdef=95,speed=36,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Natural Cure",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Quiver Dance","Iron Head","Psychic","Sucker Punch","Flash Cannon"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                      
#Mothim
class Mothim(Pokemon2):
    def __init__(self,name="Mothim",type1="Bug",type2="Flying",nature=None,level=100,happiness=255,hp=70,atk=94,defense=50,spatk=94,spdef=50,speed=66,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Tinted Lens",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Quiver Dance","Leaf Storm","Psychic","Sucker Punch","Giga Drain","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                 
#Floatzel
class Floatzel(Pokemon2):
    def __init__(self,name="Floatzel",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=85,atk=90,defense=55,spatk=95,spdef=50,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Swift Swim","Technician"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Aqua Jet","Crunch","Ice Fang","Waterfall","Aqua Tail","Hydro Pump","Flip Turn","Wave Crash","Ice Spinner"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Pachirisu
class Pachirisu(Pokemon2):
    def __init__(self,name="Pachirisu",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=75,atk=45,defense=70,spatk=45,spdef=95,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Volt Absorb","Prankster"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Volt Switch","Thunderbolt","Super Fang","Sweet Kiss","Nuzzle","Light Screen","Reflect","Charm"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Cherrim
class Cherrim(Pokemon2):
    def __init__(self,name="Cherrim",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=70,atk=100,defense=70,spatk=60,spdef=78,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Flower Gift",item="Leftovers"):
        if move is None:
            avmoves=["Protect","Petal Dance","Solar Beam","Leech Seed","Sunny Day","Morning Sun"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Lumineon
class Lumineon(Pokemon2):
    def __init__(self,name="Lumineon",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=79,atk=59,defense=76,spatk=96,spdef=69,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Storm Drain","Dazzling"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Aqua Jet","Tailwind","Ice Beam","Surf","Hydro Pump","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Lickilicky
class Lickilicky(Pokemon2):
    def __init__(self,name="Lickilicky",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=110,atk=95,defense=95,spatk=80,spdef=95,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Oblivious","Unaware","Cloud Nine"]),item="Sitrus Berry"):
        if move is None:
            avmoves=["Protect","Belly Drum","Power Whip","Body Slam","Knock Off","Return","Ice Beam","Thunderbolt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Leafeon
class Leafeon(Pokemon2):
    def __init__(self,name="Leafeon",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=65,atk=130,defense=110,spatk=60,spdef=65,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Sap Sipper"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Leaf Blade","Razor Leaf","Last Resort","Giga Drain","Synthesis","Leech Seed","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Glaceon
class Glaceon(Pokemon2):
    def __init__(self,name="Glaceon",type1="Ice",type2=None,nature=None,level=100,happiness=255,hp=80,atk=45,defense=100,spatk=130,spdef=95,speed=75,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Snow Cloak","Slush Rush","Ice Body"]),item="Leftovers"):
        if move is None:
            avmoves=["Protect","Ice Shard","Ice Beam","Last Resort","Blizzard","Freeze-Dry","Snowscape","Calm Mind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                         
#Watchog
class Watchog(Pokemon2):
    def __init__(self,name="Watchog",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=100,defense=69,spatk=60,spdef=69,speed=77,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Analytic","No Guard"]),item="Sitrus Berry"):
        if move is None:
            avmoves=["Protect","Super Fang","Hypnosis","Body Slam","Knock Off","Return","Crunch","Toxic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                
#Liepard
class Liepard(Pokemon2):
    def __init__(self,name="Liepard",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=64,atk=98,defense=55,spatk=78,spdef=55,speed=106,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Prankster","Moxie","Unburden"]),item="Sitrus Berry"):
        if move is None:
            avmoves=["Protect","Play Rough","Night Slash","Sucker Punch","Knock Off","Assurance","Fake Out","Taunt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Drednaw        
class Drednaw(Pokemon2):
    def __init__(self,name="Drednaw",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=90,atk=115,defense=90,spatk=48,spdef=68,speed=74,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Swift Swim","Strong Jaw","Shell Armor"]),item=random.choice(["Sitrus Berry","Life Orb","Water Gem"])):
        if move is None:
            avmoves=["Hydro Pump","Shell Smash","Flip Turn","Head Smash","Body Slam","Liquidation","Jaw Lock","Crunch","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Bellibolt
class Bellibolt(Pokemon2):
    def __init__(self,name="Bellibolt",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=109,atk=64,defense=91,spatk=103,spdef=83,speed=45,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Electromorphosis",item=random.choice(["Life Orb","Shuca Berry"])):
        if move is None:
            avmoves=["Thunderbolt","Hyper Voice","Volt Switch","Wild Charge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Great Tusk
class Greattusk(Pokemon2):
    def __init__(self,name="Great Tusk",type1="Ground",type2="Fighting",nature=None,level=100,happiness=255,hp=115,atk=131,defense=131,spatk=53,spdef=53,speed=87,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Protosynthesis",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Close Combat","Earthquake","Mach Punch","Stone Edge","Superpower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Brute Bonnet
class Brutebonnet(Pokemon2):
    def __init__(self,name="Brute Bonnet",type1="Grass",type2="Dark",nature=None,level=100,happiness=255,hp=111,atk=127,defense=99,spatk=79,spdef=99,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Protosynthesis",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Power Whip","Night Slash","Synthesis","Spore"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Amoongus
class Amoongus(Pokemon2):
    def __init__(self,name="Amoongus",type1="Grass",type2="Poison",nature=None,level=100,happiness=255,hp=114,atk=85,defense=70,spatk=85,spdef=80,speed=80,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Regenerator",item=random.choice(["Black Sludge","Rocky Helmet"])):
        if move is None:
            avmoves=["Giga Drain","Foul Play","Synthesis","Spore","Sludge Bomb"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                   
#Sandy Shocks
class Sandyshocks(Pokemon2):
    def __init__(self,name="Sandy Shocks",type1="Electric",type2="Ground",nature=None,level=100,happiness=255,hp=85,atk=81,defense=97,spatk=121,spdef=85,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Protosynthesis",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Thunderbolt","Earth Power","Volt Switch","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Scream Tail
class Screamtail(Pokemon2):
    def __init__(self,name="Scream Tail",type1="Fairy",type2="Psychic",nature=None,level=100,happiness=255,hp=115,atk=65,defense=99,spatk=65,spdef=115,speed=111,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability="Protosynthesis",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Psychic","Moonblast","Light Screen","Dazzling Gleam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Flutter Mane
class Fluttermane(Pokemon2):
    def __init__(self,name="Flutter Mane",type1="Ghost",type2="Fairy",nature=None,level=100,happiness=255,hp=55,atk=55,defense=55,spatk=135,spdef=135,speed=135,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Protosynthesis",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Shadow Ball","Moonblast","Will-O-Wisp","Hex"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Slither Wing
class Slitherwing(Pokemon2):
    def __init__(self,name="Slither Wing",type1="Bug",type2="Fighting",nature=None,level=100,happiness=255,hp=85,atk=135,defense=79,spatk=85,spdef=105,speed=81,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Protosynthesis",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Close Combat","Swords Dance","Mach Punch","U-Turn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Roaring Moon
class Roaringmoon(Pokemon2):
    def __init__(self,name="Roaring Moon",type1="Dragon",type2="Dark",nature=None,level=100,happiness=255,hp=105,atk=139,defense=71,spatk=55,spdef=101,speed=119,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Protosynthesis",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Dragon Claw","Night Slash","Dragon Dance","Crunch","Scale Shot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Iron Treads
class Irontreads(Pokemon2):
    def __init__(self,name="Iron Treads",type1="Ground",type2="Steel",nature=None,level=100,happiness=255,hp=90,atk=112,defense=120,spatk=72,spdef=70,speed=106,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Quark Drive",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Heavy Slam","Earthquake","Body Slam","Stone Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Iron Moth
class Ironmoth(Pokemon2):
    def __init__(self,name="Iron Moth",type1="Fire",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=70,defense=60,spatk=140,spdef=110,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Quark Drive",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Fiery Dance","Sludge Wave","Morning Sun","Will-O-Wisp","Discharge","Bug Buzz","Overheat","Hurricane","Lunge","Air Slash","Dazzling Gleam","Flash Cannon","Heat Wave","Energy Ball","Psychic","Flamethrower","Fire Blast","Solar Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Iron Hands
class Ironhands(Pokemon2):
    def __init__(self,name="Iron Hands",type1="Fighting",type2="Electric",nature=None,level=100,happiness=255,hp=154,atk=140,defense=108,spatk=50,spdef=68,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Quark Drive",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Close Combat","Thunder Punch","Mach Punch","Plasma Fists","Body Press","Belly Drum","Heavy Slam","Wild Charge","Fake Out","Earthquake","Play Rough","Iron Head","Rock Slide","Swords Dance","Rest","Stomping Tantrum","Drain Punch","Ice Punch","Fire Punch","Brick Break","Volt Switch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Iron Jugulis
class Ironjugulis(Pokemon2):
    def __init__(self,name="Iron Jugulis",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=94,atk=80,defense=86,spatk=122,spdef=80,speed=108,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Quark Drive",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Dark Pulse","Roost","Night Daze","Air Slash","Dragon Pulse","Knock Off","Hyper Voice","Snarl","Flash Cannon","Heat Wave","Flamethrower","Earth Power","Hydro Pump","Fire Blast","Focus Blast","Hyper Beam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Iron Thorns
class Ironthorns(Pokemon2):
    def __init__(self,name="Iron Thorns",type1="Rock",type2="Electric",nature=None,level=100,happiness=255,hp=100,atk=134,defense=110,spatk=70,spdef=84,speed=72,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Quark Drive",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Wild Charge","Earthquake","Dragon Dance","Stone Edge","Rock Slide","Iron Defense","Fire Fang","Ice Fang","Thunder Fang","Sandstorm","Wild Charge","Stealth Rock","Heavy Slam","Crunch","Iron Head","Swords Dance","Stomping Tantrum","Dragon Claw","Rock Blast","Dragon Tail"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Iron Bundle
class Ironbundle(Pokemon2):
    def __init__(self,name="Iron Bundle",type1="Ice",type2="Water",nature=None,level=100,happiness=255,hp=56,atk=80,defense=114,spatk=124,spdef=60,speed=136,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Quark Drive",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Ice Beam","Hydro Pump","Surf","Snowscape","Drill Peck","Freeze-Dry","Flip Turn","Aurora Veil","Blizzard","Chilling Water"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)               
#Iron Valiant
class Ironvaliant(Pokemon2):
    def __init__(self,name="Iron Valiant",type1="Fairy",type2="Fighting",nature=None,level=100,happiness=255,hp=74,atk=130,defense=90,spatk=120,spdef=60,speed=116,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Quark Drive",item=random.choice(["Booster Energy"])):
        if move is None:
            avmoves=["Close Combat","Swords Dance","Moonblast","Aura Sphere","Spirit Break","Knock Off","Leaf Blade","Night Slash","Psychic Cut","Dazzling Gleam","Shadow Sneak","Focus Blast","Thunderbolt","Psychic","Energy Ball","Shadow Ball","Aura Sphere","Liquidation","X-Scissor","Poison Jab"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Spinestial
class Spinestial(Pokemon2):
    def __init__(self,name="Spinestial",type1="Water",type2="Dragon",nature=None,level=100,happiness=255,hp=104,atk=130,defense=90,spatk=40,spdef=80,speed=100,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Swift Swim",item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["Liquidation","Dragon Dance","Dragon Claw","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)              
#Audino
class Audino(Pokemon2):
    def __init__(self,name="Audino",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=103,atk=60,defense=86,spatk=60,spdef=86,speed=50,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Regenerator",item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Misty Terrain","Double-Edge","Moonblast","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Audino
class MAudino(Pokemon2):
    def __init__(self,name="Mega Audino",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=103,atk=60,defense=126,spatk=80,spdef=126,speed=50,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability="Regenerator",item=random.choice(["Audite"])):
        if move is None:
            avmoves=["Misty Terrain","Double-Edge","Moonblast","Zen Headbutt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Delcatty
class Delcatty(Pokemon2):
    def __init__(self,name="Delcatty",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=70,atk=65,defense=65,spatk=65,spdef=55,speed=90,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move=None, ability=random.choice(["Magic Guard","Feline Prowess","Wonder Skin"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Misty Terrain","Double-Edge","Fake Out","Zen Headbutt","Hyper Voice","Play Rough"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Wo-Chien
class Wochien(Pokemon2):
    def __init__(self,name="Wo-Chien",type1="Dark",type2="Grass",nature=None,level=100,happiness=255,hp=85,atk=85,defense=100,spatk=95,spdef=135,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Tablets of Ruin"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Giga Drain","Dark Pulse","Foul Play","Grassy Terrain","Knock Off","Leaf Storm"]
            moves=moveset(avmoves,3)+["Ruination"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Chien-Pao
class Chienpao(Pokemon2):
    def __init__(self,name="Chien-Pao",type1="Dark",type2="Ice",nature=None,level=100,happiness=255,hp=80,atk=120,defense=80,spatk=90,spdef=65,speed=135,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sword of Ruin"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Icicle Crash","Night Slash","Foul Play","Snowscape","Knock Off","Swords Dance","Sucker Punch","Sacred Sword","Recover"]
            moves=moveset(avmoves,3)+["Ruination"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Ting-Lu
class Tinglu(Pokemon2):
    def __init__(self,name="Ting-Lu",type1="Dark",type2="Ground",nature=None,level=100,happiness=255,hp=155,atk=110,defense=125,spatk=55,spdef=80,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Vessel of Ruin"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Earthquake","Night Slash","Foul Play","Sandstorm","Knock Off","Stomping Tantrum"]
            moves=moveset(avmoves,3)+["Ruination"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Chi-Yu
class Chiyu(Pokemon2):
    def __init__(self,name="Chi-Yu",type1="Dark",type2="Fire",nature=None,level=100,happiness=255,hp=55,atk=80,defense=80,spatk=135,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Beads of Ruin"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Overheat","Dark Pulse","Nasty Plot","Sunny Day","Knock Off","Fire Blast"]
            moves=moveset(avmoves,3)+["Ruination"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Bombirdier
class Bombirdier(Pokemon2):
    def __init__(self,name="Bombirdier",type1="Dark",type2="Flying",nature=None,level=100,happiness=255,hp=70,atk=103,defense=85,spatk=60,spdef=85,speed=82,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Rocky Payload"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Dual Wingbeat","Dark Pulse","Rock Slide","Parting Shot","Knock Off","Roost"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Flamigo
class Flamigo(Pokemon2):
    def __init__(self,name="Flamigo",type1="Flying",type2="Fighting",nature=None,level=100,happiness=255,hp=82,atk=115,defense=74,spatk=75,spdef=64,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Scrappy","Costar"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Brave Bird","Roost","Throat Chop","Sky Attack","Knock Off","Close Combat"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Kilowattrel
class Kilowattrel(Pokemon2):
    def __init__(self,name="Kilowattrel",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=70,atk=70,defense=60,spatk=105,spdef=60,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Volt Absorb","Competitive","Wind Power"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Air Slash","Roost","Thunderbolt","Hurricane","Volt Switch","Electro Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Espathra
class Espathra(Pokemon2):
    def __init__(self,name="Espathra",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=95,atk=60,defense=60,spatk=101,spdef=60,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Speed Boost","Opportunist"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Psychic","Dazzling Gleam","Drill Peck","Extreme Speed"]
            moves=moveset(avmoves,3)+["Lumina Crash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Veluza
class Veluza(Pokemon2):
    def __init__(self,name="Veluza",type1="Water",type2="Psychic",nature=None,level=100,happiness=255,hp=90,atk=102,defense=73,spatk=78,spdef=65,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Mold Breaker","Sharpness"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Recover","Psycho Cut","Night Slash","Slash","Crunch","Fillet Away"]
            moves=moveset(avmoves,3)+["Aqua Cutter"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Glimmora
class Glimmora(Pokemon2):
    def __init__(self,name="Glimmora",type1="Rock",type2="Poison",nature=None,level=100,happiness=255,hp=83,atk=55,defense=90,spatk=130,spdef=81,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Corrosion","Toxic Debris"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Sludge Wave","Power Gem","Stealth Rock","Acid Armor","Spiky Shield","Rock Slide"]
            moves=moveset(avmoves,3)+["Mortal Spin"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Orthworm
class Orthworm(Pokemon2):
    def __init__(self,name="Orthworm",type1="Steel",type2=None,nature=None,level=100,happiness=255,hp=70,atk=85,defense=145,spatk=60,spdef=55,speed=65,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Earth Eater"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Earthquake","Iron Head","Stealth Rock","Iron Defense","Iron Tail","Heavy Slam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Lokix
class Lokix(Pokemon2):
    def __init__(self,name="Lokix",type1="Bug",type2="Dark",nature=None,level=100,happiness=255,hp=71,atk=102,defense=78,spatk=52,spdef=55,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Tinted Lens"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Sucker Punch","Throat Chop","Swords Dance","Assurance","X-Scissor"]
            moves=moveset(avmoves,3)+["Axe Kick"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Spidops
class Spidops(Pokemon2):
    def __init__(self,name="Spidops",type1="Bug",type2=None,nature=None,level=100,happiness=255,hp=60,atk=79,defense=92,spatk=52,spdef=86,speed=35,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Stakeout"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Sucker Punch","Throat Chop","Swords Dance","Assurance","X-Scissor"]
            moves=moveset(avmoves,3)+["Silk Trap"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Sigilyph
class Sigilyph(Pokemon2):
    def __init__(self,name="Sigilyph",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=72,atk=58,defense=80,spatk=103,spdef=80,speed=97,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Magic Guard","Tinted Lens"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Air Slash","Psychic","Light Screen","Reflect","Tailwind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Swoobat
class Swoobat(Pokemon2):
    def __init__(self,name="Swoobat",type1="Psychic",type2="Flying",nature=None,level=100,happiness=255,hp=75,atk=57,defense=65,spatk=77,spdef=55,speed=114,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Simple","Unaware"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Air Slash","Psychic","Light Screen","Reflect","Tailwind"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Scovillain
class Scovillain(Pokemon2):
    def __init__(self,name="Scovillain",type1="Grass",type2="Fire",nature=None,level=100,happiness=255,hp=65,atk=108,defense=65,spatk=108,spdef=65,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Moody"]),item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["Growth","Sunny Day","Solar Beam","Synthesis","Flamethrower","Fire Fang","Bullet Seed","Crunch"]
            moves=moveset(avmoves,3)+["Spicy Extract"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Revavroom
class Revavroom(Pokemon2):
    def __init__(self,name="Revavroom",type1="Steel",type2="Poison",nature=None,level=100,happiness=255,hp=80,atk=119,defense=90,spatk=54,spdef=67,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Filter"]),item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["Taunt","Iron Head","Poison Jab","Gunk Shot"]
            moves=moveset(avmoves,3)+["Spin Out"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Dachsbun
class Dachsbun(Pokemon2):
    def __init__(self,name="Dachsbun",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=57,atk=80,defense=115,spatk=50,spdef=80,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Well-Baked Body"]),item=random.choice(["Life Orb"])):
        if move is None:
            avmoves=["Crunch","Play Rough","Body Press","Stomping Tantrum"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Slurpuff
class Slurpuff(Pokemon2):
    def __init__(self,name="Slurpuff",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=82,atk=90,defense=86,spatk=75,spdef=75,speed=72,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sweet Veil","Unburden"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Energy Ball","Play Rough","Sticky Web","Draining Kiss"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Maushold
class Maushold(Pokemon2):
    def __init__(self,name="Maushold",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=74,atk=75,defense=70,spatk=65,spdef=75,speed=111,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Technician"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Protect","Play Rough","Super Fang","Bullet Seed","Crunch"]
            moves=moveset(avmoves,3)+["Population Bomb"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)            
#Mabosstiff
class Mabosstiff(Pokemon2):
    def __init__(self,name="Mabosstiff",type1="Dark",type2=None,nature=None,level=100,happiness=255,hp=80,atk=120,defense=90,spatk=60,spdef=70,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Guard Dog","Stakeout"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Double-Edge","Outrage","Jawlock","Crunch"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Pawmot
class Pawmot(Pokemon2):
    def __init__(self,name="Pawmot",type1="Electric",type2="Fighting",nature=None,level=100,happiness=255,hp=70,atk=115,defense=70,spatk=70,spdef=60,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Volt Absorb","Natural Cure","Iron Fist"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Close Combat","Thunder Wave","Wild Charge","Discharge","Nuzzle"]
            moves=moveset(avmoves,3)+["Double Shock"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)     
#Diggersby
class Diggersby(Pokemon2):
    def __init__(self,name="Diggersby",type1="Normal",type2="Ground",nature=None,level=100,happiness=255,hp=85,atk=56,defense=77,spatk=50,spdef=77,speed=78,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Huge Power",item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Earthquake","Return","Stone Edge","Body Slam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Simisage
class Simisage(Pokemon2):
    def __init__(self,name="Simisage",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=75,atk=98,defense=63,spatk=98,spdef=63,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Overgrow",item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Seed Bomb","Grass Knot","Giga Drain","Energy Ball"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Simisear
class Simisear(Pokemon2):
    def __init__(self,name="Simisear",type1="Fire",type2=None,nature=None,level=100,happiness=255,hp=75,atk=98,defense=63,spatk=98,spdef=63,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Blaze",item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Overheat","Will-O-Wisp","Fire Blast","Flamethrower"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Simipour
class Simipour(Pokemon2):
    def __init__(self,name="Simipour",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=75,atk=98,defense=63,spatk=98,spdef=63,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Torrent",item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Hydro Pump","Surf","Scald","Rain Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Musharna
class Musharna(Pokemon2):
    def __init__(self,name="Musharna",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=116,atk=55,defense=85,spatk=107,spdef=95,speed=29,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Synchronize","Unaware"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Calm Mind","Psychic","Moonblast","Hypnosis","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Throh
class Throh(Pokemon2):
    def __init__(self,name="Throh",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=120,atk=100,defense=95,spatk=30,spdef=95,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability="Guts",item=random.choice(["Flame Orb"])):
        if move is None:
            avmoves=["Superpower","Bulk Up","Grass Knot","Taunt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Throh
class Throh(Pokemon2):
    def __init__(self,name="Throh",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=120,atk=100,defense=85,spatk=30,spdef=85,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Guts","Mold Breaker","Technician"]),item=random.choice(["Leftover"])):
        if move is None:
            avmoves=["Superpower","Bulk Up","Grass Knot","Taunt"]
            moves=moveset(avmoves)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Sawk
class Sawk(Pokemon2):
    def __init__(self,name="Sawk",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=75,atk=125,defense=75,spatk=30,spdef=75,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sturdy","Inner Focus","Contrary"]),item=random.choice(["Weakness Policy"])):
        if move is None:
            avmoves=["Close Combat","Bulk Up","Grass Knot","Brick Break"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)        
#Eevee
class Eevee(Pokemon2):
    def __init__(self,name="Eevee",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=65,atk=75,defense=70,spatk=65,spdef=85,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Adaptability",item=random.choice(["Normal Gem"])):
        if move is None:
            avmoves=["Double-Edge","Extreme Speed","Last Resort","Protect"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Plusle
class Plusle(Pokemon2):
    def __init__(self,name="Plusle",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=60,atk=50,defense=40,spatk=85,spdef=75,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Plus","Transistor","Lightning Rod"]),item=random.choice(["Focus Sash"])):
        if move is None:
            avmoves=["Thunder Wave","Nasty Plot","Encore","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Minun
class Minun(Pokemon2):
    def __init__(self,name="Minun",type1="Electric",type2=None,nature=None,level=100,happiness=255,hp=60,atk=85,defense=75,spatk=50,spdef=40,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Minus","Volt Absorb","Galvanize"]),item=random.choice(["Focus Sash"])):
        if move is None:
            avmoves=["Thunder Wave","Nasty Plot","Encore","Thunder"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Volbeat
class Volbeat(Pokemon2):
    def __init__(self,name="Volbeat",type1="Bug",type2="Electric",nature=None,level=100,happiness=255,hp=85,atk=47,defense=75,spatk=90,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item=random.choice(["Focus Sash"])):
        if move is None:
            avmoves=["Play Rough","Bug Buzz","Tail Glow","Moonlight","Thunderbolt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Illumise
class Illumise(Pokemon2):
    def __init__(self,name="Illumise",type1="Bug",type2="Fairy",nature=None,level=100,happiness=255,hp=85,atk=90,defense=75,spatk=47,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Prankster",item=random.choice(["Focus Sash"])):
        if move is None:
            avmoves=["Play Rough","Bug Buzz","Tail Glow","Moonlight"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Spinda
class Spinda(Pokemon2):
    def __init__(self,name="Spinda",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=80,atk=80,defense=80,spatk=80,spdef=80,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Contrary",item=random.choice(["Focus Sash"])):
        if move is None:
            avmoves=["Sucker Punch","Drain Punch","Dizzy Punch","Rock Slide"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Castform
class Castform(Pokemon2):
    def __init__(self,name="Castform",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=70,atk=70,defense=70,spatk=70,spdef=70,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Forecast",item=random.choice(["Focus Sash"])):
        if move is None:
            avmoves=["Hydro Pump","Hurricane","Fire Blast","Blizzard","Rain Dance","Sunny Day","Snowscape"]
            moves=moveset(avmoves,3)+["Weather Ball"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Chimecho
class Chimecho(Pokemon2):
    def __init__(self,name="Chimecho",type1="Psychic",type2=None,nature=None,level=100,happiness=255,hp=90,atk=50,defense=70,spatk=95,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability="Levitate",item=random.choice(["Focus Sash"])):
        if move is None:
            avmoves=["Psychic","Extrasensory","Light Screen","Yawn"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Lilligant
class Lilligant(Pokemon2):
    def __init__(self,name="Lilligant",type1="Grass",type2=None,nature=None,level=100,happiness=255,hp=70,atk=60,defense=75,spatk=110,spdef=75,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Chlorophyll",item=random.choice(["Focus Sash"])):
        if move is None:
            avmoves=["Leaf Storm","Sleep Powder","Petal Blizzard","Energy Ball","Quiver Dance"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Crustle
class Crustle(Pokemon2):
    def __init__(self,name="Crustle",type1="Bug",type2="Rock",nature=None,level=100,happiness=255,hp=70,atk=95,defense=125,spatk=65,spdef=75,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Sturdy","Shell Armor","Weak Armor"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Rock Wrecker","Shell Smash","X-Scissor","Rock Blast"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Cinccino
class Cincinno(Pokemon2):
    def __init__(self,name="Cinccino",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=75,atk=95,defense=60,spatk=65,spdef=60,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability="Skill Link",item=random.choice(["Focus Sash"])):
        if move is None:
            avmoves=["Tail Slap","Bullet Seed","Rock Blast","Thunderbolt"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)       
#Sawsbuck
class Sawsbuck(Pokemon2):
    def __init__(self,name="Sawsbuck",type1="Normal",type2="Grass",nature=None,level=100,happiness=255,hp=80,atk=110,defense=70,spatk=60,spdef=70,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Chlorophyll","Sap Sipper","Serene Grace"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Horn Leech","Bullet Seed","Megahorn","Double-Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Alomomola
class Amomola(Pokemon2):
    def __init__(self,name="Alomomola",type1="Water",type2=None,nature=None,level=100,happiness=255,hp=165,atk=75,defense=80,spatk=40,spdef=45,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Hydration","Regenerator"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Hydro Pump","Aqua Jet","Ice Beam","Surf"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)             
#Passimian
class Passimian(Pokemon2):
    def __init__(self,name="Passimian",type1="Fighting",type2=None,nature=None,level=100,happiness=255,hp=100,atk=120,defense=90,spatk=40,spdef=75,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Defiant","Receiver"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Giga Impact","Close Combat","Bulk Up","Double-Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Lopunny
class Lopunny(Pokemon2):
    def __init__(self,name="Lopunny",type1="Normal",type2="Fighting",nature=None,level=100,happiness=255,hp=65,atk=76,defense=84,spatk=54,spdef=96,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Limber"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["High Jump Kick","Close Combat","Bulk Up","Double-Edge"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Rotom
class MRotom(Pokemon2):
    def __init__(self,name="Mow Rotom",type1="Electric",type2="Grass",nature=None,level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Volt Switch","Leaf Storm","Discharge","Trick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Rotom
class FRotom(Pokemon2):
    def __init__(self,name="Fan Rotom",type1="Electric",type2="Flying",nature=None,level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Motor Drive"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Volt Switch","Hurricane","Discharge","Trick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)
#Rotom
class HRotom(Pokemon2):
    def __init__(self,name="Heat Rotom",type1="Electric",type2="Fire",nature=None,level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Volt Switch","Flamethrower","Discharge","Will-O-Wisp"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Rotom
class FrRotom(Pokemon2):
    def __init__(self,name="Frost Rotom",type1="Electric",type2="Ice",nature=None,level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Levitate"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Volt Switch","Blizzard","Discharge","Trick"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Arctovish
class Arctovish(Pokemon2):
    def __init__(self,name="Arctovish",type1="Water",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=90,defense=100,spatk=55,spdef=90,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Water Absorb","Ice Body","Slush Rush"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Fishious Rend","Icicle Crash","Crunch","Ancient Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item) 
#Arctozolt
class Arctozolt(Pokemon2):
    def __init__(self,name="Arctozolt",type1="Electric",type2="Ice",nature=None,level=100,happiness=255,hp=90,atk=100,defense=90,spatk=90,spdef=55,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Volt Absorb","Static","Slush Rush"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Bolt Beak","Discharge","Icicle Crash","Ancient Power"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)   
#Aromatisse
class Aromatisse(Pokemon2):
    def __init__(self,name="Aromatisse",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=101,atk=62,defense=82,spatk=99,spdef=89,speed=29,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Aroma Veil","Fairy Aura"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Draining Kiss","Moonblast","Calm Mind","Psychic"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Ribombee
class Ribombee(Pokemon2):
    def __init__(self,name="Ribombee",type1="Bug",type2="Fairy",nature=None,level=100,happiness=255,hp=60,atk=55,defense=60,spatk=95,spdef=70,speed=124,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Sweet Veil","Shield Dust","Swarm"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Polen Puff","Moonblast","Quiver Dance","Draining Kiss"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)  
#Comfey
class Comfey(Pokemon2):
    def __init__(self,name="Aromatisse",type1="Fairy",type2=None,nature=None,level=100,happiness=255,hp=51,atk=52,defense=90,spatk=82,spdef=110,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Flower Veil","Triage","Natural Cure"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Draining Kiss","Moonblast","Calm Mind","Grass Knot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)         
#Lurwntis
class Lurantis(Pokemon2):
    def __init__(self,name="Lurantis",type1="Grass",type2="Fighting",nature=None,level=100,happiness=255,hp=70,atk=105,defense=90,spatk=80,spdef=90,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Contrary","Leaf Guard"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Solar Blade","Leaf Blade","Synthesis","X-Scissor","Brick Break","Sunny Day"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Shiinotic
class Shiinotic(Pokemon2):
    def __init__(self,name="Shiinotic",type1="Grass",type2="Fairy",nature=None,level=100,happiness=255,hp=75,atk=45,defense=80,spatk=90,spdef=100,speed=30,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Rain Dish","Effect Spore"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Moonblast","Spore","Synthesis","Giga Drain","Strength Sap"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Brambleghast
class Brambleghast(Pokemon2):
    def __init__(self,name="Brambleghast",type1="Grass",type2="Ghost",nature=None,level=100,happiness=255,hp=55,atk=115,defense=70,spatk=80,spdef=70,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move=None, ability=random.choice(["Wind Rider","Infiltrator"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Power Whip","Pain Split","Phantom Force","Bullet Seed"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)    
#Crabominable
class Crabominable(Pokemon2):
    def __init__(self,name="Crabominable",type1="Fighting",type2="Ice",nature=None,level=100,happiness=255,hp=97,atk=132,defense=77,spatk=62,spdef=67,speed=43,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Iron Fist","Anger Point"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Ice Hammer","Close Combat","Ice Punch","Ice Spinner"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        #Kecleon
class Kecleon(Pokemon2):
    def __init__(self,name="Kecleon",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=85,atk=100,defense=70,spatk=60,spdef=120,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Color Change","Protean"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Foul Play","Sucker Punch","Shadow Claw","Ancient Power","Psychic","Shadow Sneak"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                        
#Oranguru
class Oranguru(Pokemon2):
    def __init__(self,name="Oranguru",type1="Normal",type2="Psychic",nature=None,level=100,happiness=255,hp=90,atk=60,defense=110,spatk=90,spdef=80,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Inner Focus","Symbiosis","Sage Power"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Foul Play","Psychic","Trick Room","Nasty Plot"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)           
#Greedent
class Greedent(Pokemon2):
    def __init__(self,name="Greedent",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=120,atk=95,defense=95,spatk=55,spdef=75,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Cheek Pouch"]),item=random.choice(["Sitrus Berry"])):
        if move is None:
            avmoves=["Super Fang","Belch","Bullet Seed","Rest","Body Slam"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)      
#Oinkologne
class Oinkologne(Pokemon2):
    def __init__(self,name="Oinkologne",type1="Normal",type2=None,nature=None,level=100,happiness=255,hp=110,atk=100,defense=75,spatk=59,spdef=80,speed=65,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Lingering Aroma","Thick Fat"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["Body Slam","Double-Edge","Yawn","Play Rough"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)          
#Falinks
class Falinks(Pokemon2):
    def __init__(self,name="Falinks",type1="Fighting",type2="Bug",nature=None,level=100,happiness=255,hp=65,atk=100,defense=100,spatk=70,spdef=60,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move=None, ability=random.choice(["Battle Armor","Defiant"]),item=random.choice(["Leftovers"])):
        if move is None:
            avmoves=["No Retreat","Close Combat","Megahorn","Iron Defense","Bulk Up"]
            moves=moveset(avmoves)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item)                                                
                                                                           