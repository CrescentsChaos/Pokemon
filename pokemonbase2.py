from movelist import *
from pokemonintros import *
import random
naturelist=["Hardy","Lonely","Adamant","Naughty","Brave", "Bold",'Docile','Impish','Lax','Relaxed' ,'Modest','Mild','Bashful','Rash','Quiet' ,'Calm','Gentle','Careful','Quirky','Sassy', 'Timid','Hasty','Jolly','Naive','Serious']
megastones=["Gyaradosite","Venusaurite","Charizardite X","Charizardite Y","Abomasite","Absolite","Aerodactylite","Aggronite","Alakazite","Altarianite","Amoharosite","Audinite","Banettite","Beedrillite","Blastoisinite","Blazikenite","Camerupite","Diancite","Galladite","Garchompite","Gardevoirite","Gengarite","Glalitite","Heracronite","Houndoominite","Kangaskhanite","Latiasite","Latiosite","Lopunnite","Lucarionite","Manectite","Mawilite","Medichamite","Metagrossite","Mewtwonite X","Mewtwonite Y","Pidgeotite","Pinsirite","Sablenite","Salamencite","Sceptilite","Scizorite","Sharpedonite","Slowbronite","Steelixite","Seampertite","Tyranitarite"]
class Pokemon2:
    "Pokemon2"
    def __init__(self,name="Unidentified",type1="Normal",type2="None",nature="None",level=100,happiness=0,hp=0,atk=0,defense=0,spatk=0,spdef=0,speed=0,hpiv=0,atkiv=0,defiv=0,spatkiv=0,spdefiv=0,speediv=0,maxiv="No",atktype="Normal",hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,status="Alive",atkb=1,defb=1,spatkb=1,spdefb=1,speedb=1,ability="None",moves="None",movez="None",toxicCounter=1,flinched=False,recharge=False,seeded=False, canfakeout=True,item="None",precharge=False, protect=False,shelltrap=False,choiced=False,choicedmove="None",owner="None",teratype="None",taunted=False,critrate=1, accuracy=100,dmax=False,maxmove="None",maxend=0,megaintro=False,fsprite="graphics/fsprites/unknown.png", bsprite="graphics/bsprites/Gengar.png", priority=False,dbond=False, abilityused=False,healcount=0,confused=False,dmgtaken=0,yawn=False,m1pp=32,m2pp=32,m3pp=32,m4pp=32,mx1pp=32,mx2pp=32,mx3pp=32,mx4pp=32,pplist="None",aring=False,olock=False,tarshot=False,bullrush=False,atkcat="None",magmadmg=False,magmaendturn=False,wfdmg=False,wfendturn=False,cndmg=False,cnendturn=False,vldmg=False,vlendturn=False,miss=False,use="None",cntdmg=False,cntendturn=False,grav=False,gravendturn=False,weight=100,sleependturn=False,confuseendturn=False,encore=False,enendturn=False,taunturn=0,encturn=False,tera="None",dmgrec=0,dmgdealt=0,salty="None",perishturn=0,fmoveturn=0,fmove=False,roost=False,flashfire=False,focus=False,lockon=False,evasion=100,trap=False,lostmoves=[], infatuated=False, infestation=False,firespin=False,whirlpool=False,zuser=False,cursed=False,color="white"):
        #Name
        self.name=name
        if moves =="None":
            self.moves=["Tackle","Tackle","Tackle","Tackle"]
        else:
            self.moves=moves
        self.shiny=random.randint(1,4096)
        if self.shiny==7:
            self.name=self.name+"✨"
        #Type
        self.type1=type1
        self.cursed=cursed
        self.color=color
        self.trap=trap
        self.infatuated=infatuated 
        self.lostmoves=lostmoves
        self.infestation=infestation
        self.firespin=firespin
        self.whirlpool=whirlpool
        self.lockon=lockon
        self.evasion=evasion 
        self.dmgrec=dmgrec
        self.roost=roost
        self.focus=focus
        self.fmove=fmove
        self.fmoveturn=fmoveturn
        self.salty=salty
        self.flashfire=flashfire
        self.dmgdealt=dmgdealt
        self.perishturn=perishturn
        self.taunturn=taunturn
        self.encturn=encturn
        self.encore=encore
        self.enendturn=enendturn
        self.use=use
        self.weight=weight
        self.miss=miss
        self.tarshot=tarshot
        self.atkcat=atkcat
        self.type2=type2
        self.tera=tera
        if self.tera=="None":
            self.tera=random.choices([self.type1,self.type1,random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])], weights=[10,10,5],k=1)[0]
        self.aring=aring
        self.sleependturn=sleependturn
        self.confuseendturn=confuseendturn
        self.vldmg=vldmg
        self.vlendturn=vlendturn
        self.magmadmg=magmadmg
        self.magmaendturn=magmaendturn
        self.wfdmg=wfdmg
        self.wfendturn=wfendturn
        self.cndmg=cndmg
        self.cnendturn=cnendturn
        self.grav=grav
        self.gravendturn=gravendturn
        self.cntdmg=cntdmg
        self.cntendturn=cntendturn
        self.olock=olock
        self.bullrush=bullrush
        self.atkby="None"
        self.atktime=0
        self.m1pp=m1pp
        self.m2pp=m2pp
        self.m3pp=m3pp
        self.m4pp=m4pp
        self.mx1pp=mx1pp
        self.mx2pp=mx2pp
        self.mx3pp=mx3pp
        self.mx4pp=mx4pp
        if self.moves[0] in typemoves.pp15:
            self.m1pp=self.mx1pp=24
        if self.moves[0] in typemoves.pp10:
            self.m1pp=self.mx1pp=16
        if self.moves[0] in typemoves.pp5:
            self.m1pp=self.mx1pp=8
        if self.moves[1] in typemoves.pp15:
            self.m2pp=self.mx2pp=24
        if self.moves[1] in typemoves.pp10:
            self.m2pp=self.mx2pp=16
        if self.moves[1] in typemoves.pp5:
            self.m2pp=self.mx2pp=8
        if self.moves[2] in typemoves.pp15:
            self.m3pp=self.mx3pp=24
        if self.moves[2] in typemoves.pp10:
            self.m3pp=self.mx3pp=16
        if self.moves[2] in typemoves.pp5:
            self.m3pp=self.mx3pp=8
        if self.moves[3] in typemoves.pp15:
            self.m4pp=self.mx4pp=24
        if self.moves[3] in typemoves.pp10:
            self.m4pp=self.mx4pp=16
        if self.moves[3] in typemoves.pp5:
            self.m4pp=self.mx4pp=8
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
        self.accuracy=accuracy
        self.critrate=critrate
        self.basestats=atk+defense+spdef+spatk+hp+speed
        self.ability=ability
        self.owner=owner
        self.toxicCounter=toxicCounter
        self.recharge=recharge
        self.seeded=seeded
        self.flinched=flinched
        self.precharge=precharge 
        self.protect=protect
        self.shelltrap=shelltrap
        self.canfakeout=canfakeout
        self.choiced=choiced
        self.taunted=taunted 
        self.zuser=zuser
        self.maxend=maxend
        self.choicedmove=choicedmove
        self.fsprite="graphics/fsprites/"+self.name+".png"
        #self.bsprite="graphics/bsprites/"+self.basename+".png"
        #Nature
        self.nature=nature
        if self.nature =="None":
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
        self.maxmove=mxmove(self,typemoves)
        #Command
        self.maxiv=maxiv
        if self.maxiv in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
            self.tera=self.maxiv
#        if self.maxiv not in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
#            ch=random.randint(1,3)
#            if ch==2:
#                self.tera=self.type2
#            if ch==1:
#                self.tera=self.type1
#            if ch==3:
#                self.tera=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])
            xx=random.randint(1,100)    
            if xx>90 and self.zuser==False:
                self.moves[0]="Tera Blast"
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
        self.alpha=random.randint(1,100)
        if self.item not in megastones and self.alpha==7 and maxiv not in ["Yes"]:
            self.name=f"Alpha {name}"
        self.totem=random.randint(1,300)
        if self.item not in megastones and "Alpha " not in name and self.totem == 7 and maxiv not in ["Yes"]:
            self.name=f"Totem {name}"
        self.movez=movez
        if (maxiv not in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice","Yes"] and self.zuser==False) or "Z-Crystal" in self.name:
            if "Z-Crystal" in self.name:
                self.moves+=zmove(self)
            self.movez=random.randint(1,2)
            if ((self.movez==2) and self.item not in megastones):
                x=zmove(self)
                if x==None:
                    x="Breakneck Blitz"
                    self.item="Normalium-Z"
                self.moves+=x
                self.zuser=True
        #Attack Manipulation
        self.atktype=atktype
        #Boost
        self.atkb=atkb
        self.defb=defb
        self.spatkb=spatkb
        self.spdefb=spdefb
        self.speedb=speedb
        self.calcst()
        self.hp=self.maxhp
        #stats
        self.status=status
        mch=random.randint(1,2)
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
        if "Steel" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,31,30,31
        if "Dark" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,31,31,31
        if "Dragon" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,31,31,31,31
        if "Ghost" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,30,31,30,31
        if "Rock" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,30,31,30,30
        if "Bug" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,31,30,30
        if "Psychic" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,31,31,31,30
        if "Flying" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,30,30,30
        if "Poison" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,30,30,30,31
        if "Electric" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,30,31,31
        if "Water" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,30,31,30
        if "Fighting" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,30,30,30,30
        if "Ground" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,30,30,31
        if "Grass" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,31,30,31,31
        if "Ice" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,30,31,31,31
        if "Fire" in self.maxiv:
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,30,31,30,31,30
        if self.alpha==7 and self.item not in megastones:
            self.hpiv=random.randint(15,31)
            self.atkiv=random.randint(15,31)
            self.defiv=random.randint(15,31)
            self.spatkiv=random.randint(15,31)
            self.spdefiv=random.randint(15,31)
            self.speediv=random.randint(15,31)
        if self.totem==7 and self.item not in megastones:
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
        self.maxspeed=stat_clac(self.speed,self.speediv,self.speedev,self.level)
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
            self.maxatk+=round(self.maxatk*0.1)
        if self.nature in ["Mild","Modest","Quite","Rash"]:
            self.maxspatk+=round(self.maxspatk*0.1)
        if self.nature in ["Adamant","Careful","Impish","Jolly"]:
            self.maxspatk-=round(self.maxspatk*0.1)
        if self.nature in ["Bold","Calm","Modest","Timid"]:
            self.maxatk-=round(self.maxatk*0.1)
        if self.nature in ["Bold","Relaxed","Lax","Impish"]:
            self.maxdef+=round(self.maxdef*0.1)
        if self.nature in ["Gentle","Hasty","Lonely","Mild"]:
            self.maxdef-=round(self.maxdef*0.1)
        if self.nature in ["Calm","Careful","Gentle","Sassy"]:
            self.maxspdef+=round(self.maxspdef*0.1)
        if self.nature in ["Lax","Naive","Naughty","Rash"]:
            self.maxspdef-=round(self.maxspdef*0.1)
        if self.nature in ["Jolly","Timid","Naive","Hasty"]:
            self.maxspeed+=round(self.maxspeed*0.1)
        if self.nature in ["Brave","Quite","Sassy","Relaxed"]:
            self.maxspeed-=round(self.maxspeed*0.1)
#GENERATES NATURE
    def gennature(self):
        "Generates Nature"
        self.nature=random.choice(naturelist)
        
    def ivc(self):
        "Checks IV"
        print(f" HP IV: {self.hpiv}/31")
        print(f" Attack IV: {self.atkiv}/31")
        print(f" Defence IV: {self.defiv}/31")
        print(f" Sp.Attack IV: {self.spatkiv}/31")
        print(f" Sp.Defence IV: {self.spdefiv}/31")
        print(f" Speed IV: {self.speediv}/31")
        totaliv=self.hpiv+self.atkiv+self.defiv+self.spatkiv+self.spdefiv+self.speediv
        print("=============================================")
        percentage=(totaliv/186)*100
        print(f" Total IV: {totaliv}/186")
        print(f" IV: {round(percentage,2)}%")
    
        print("=============================================")
    def info(self):
        "Shows Stats"
        print("=============================================")
        print(colored(f" NAME: {self.name} Lv.{self.level}","white"))
        if self.type2 =="None":
            print(colored(f" TYPE: {self.type1}","white"))
        else:
            print(colored(f" TYPE: {self.type1}/{self.type2}","white"))
        print(colored(f" TERA-TYPE: {self.tera}","white"))
        print(colored(f" OT: {self.owner.name}","white"))
        print(colored(f" ITEM: {self.item}","white"))
        print(colored(f" {self.nature} nature.","white"))
        print(colored(f" WEIGHT: {self.weight} lbs.","white"))
        print(colored(f" Met in {random.choice(place).upper()} at Lv.{random.randint(1,self.level-1)}.","white"))
                
        print("=============================================")
        print(" Stats:")
        print("=============================================")
        print(colored(f" HP","green")+f": {round(self.hp)}")
        print(colored(f" ATTACK","red")+f": {round(self.atk)}")
        print(colored(f" DEFENSE","yellow")+f": {round(self.defense)}")
        print(colored(f" SP.ATK","magenta")+f": {round(self.spatk)}")
        print(colored(f" SP.DEF","blue")+f": {round(self.spdef)}")
        print(colored(f" SPEED","cyan")+f": {round(self.speed)}")        
        print(colored(f" ABILITY: {self.ability}","white"))
        abilitydesc(self.ability)
        print("=============================================")
        self.ivc()
#Calculates Stats
def stat_clac(stat,individual_value,effort_value,level,spst="None"):
	"Generates enhanced stats"
	if spst == "HP":
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+level+10)
	else:
	    new_stat=round((((2*stat+individual_value+(effort_value*0.25))*level)/100)+5)
	return new_stat
        
#typem
def movelist(self,other,field):
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
            cl="white"
            if i in (typemoves.watermoves):
                cl="blue"
            if i in (typemoves.psychicmoves+typemoves.ghostmoves+typemoves.poisonmoves+typemoves.fairymoves):
                cl="magenta"
            if i in (typemoves.flyingmoves+typemoves.icemoves):
                cl="cyan"
            if i in (typemoves.grassmoves+typemoves.bugmoves):
                cl="green"
            if i in (typemoves.electricmoves+typemoves.rockmoves+typemoves.groundmoves):
                cl="yellow"
            if i in (typemoves.firemoves+typemoves.darkmoves+typemoves.fightingmoves+typemoves.dragonmoves):
                cl="red"
            print(colored(f" {num}. {i} ({self.pplist[self.maxmove.index(i)]})",cl))
    if self.dmax is False:
        x="None"
        if (self.item!="None" or "Used" not in self.item) and "m-Z" in self.item:
            x=4
        if "Used" in self.item or "m-Z" not in self.item:
            x=len(self.moves)
        for i in range(x):
            num+=1
            cl="white"
            if self.moves[i] in (typemoves.watermoves):
                cl="blue"
            if self.moves[i] in (typemoves.psychicmoves+typemoves.ghostmoves+typemoves.poisonmoves+typemoves.fairymoves):
                cl="magenta"
            if self.moves[i] in (typemoves.flyingmoves+typemoves.icemoves):
                cl="cyan"
            if self.moves[i] in (typemoves.grassmoves+typemoves.bugmoves):
                cl="green"
            if self.moves[i] in (typemoves.electricmoves+typemoves.rockmoves+typemoves.groundmoves):
                cl="yellow"
            if self.moves[i] in (typemoves.firemoves+typemoves.darkmoves+typemoves.fightingmoves+typemoves.dragonmoves):
                cl="red"
            if ((self.ability=="Prankster" and self.moves[i] not in typemoves.statusmove and "Dark" in (other.type1,other.type2,other.teratype)) or (other.ability in ["Armor Tail","Queenly Majesty","Dazzling"] or field.terrain=="Psychic") and self.moves[i] not in typemoves.prioritymove) or (self.precharge==True and self.moves[i] in typemoves.premove) or (self.taunted==True and self.moves[i] not in typemoves.statusmove) or ((self.choiced==True or self.encore==True) and self.moves[i]==self.choicedmove) or (self.taunted==False and self.choiced==False and self.precharge==False):
                if "Hidden Power" not in self.moves[i]:
                    print(colored(f" {num}. {self.moves[i]} ({self.pplist[self.moves.index(self.moves[i])]})",cl))
                if "Hidden Power" in self.moves[i]:
                    if self.maxiv not in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
                        x=hidp(self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv)
                        print(colored(f" {num}. {self.moves[i]}-{x[1]} ({self.pplist[self.moves.index(self.moves[i])]})",cl))
                    if self.maxiv in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
                        print(colored(f" {num}. {self.moves[i]}-{self.maxiv} ({self.pplist[self.moves.index(self.moves[i])]})",cl))
    if "Used" not in self.item and "m-Z" in self.item:
        print(f" {num+1}. {self.moves[-1]} (1)") 
        #print(" Press 5 to unlish your Z-move!")
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
    
def mxmove(self,typem=typemoves):
    maxmove=[]
    gm="None"
    for i in self.moves:
        if i in typem.dragonmoves:
            gm="Max Wyrmwind"
            if "Duraludon" in self.name:
                gm="G-Max Depletion"
        if i in typem.normalmoves:
            gm="Max Strike"
            if self.ability=="Galvanize":
                gm="Max Lightning"
            if self.ability=="Aerilate":
                gm="Max Airstream"
            if self.ability=="Refrigerate":
                gm="Max Hailstorm"
            if self.ability=="Pixilate":
                gm="Max Starfall"
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

def zmove(mon):
    tp="U-turn"
    if mon.maxiv not in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
        ch=1
        if ch==1:
            tp=mon.type1
        if ch==2:
            if mon.type2 =="None":
                tp=mon.type1
            else:
                tp=mon.type2       
        if ch==3:
            tp=random.choice(["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"])                
    if mon.maxiv in ["Rock","Fire","Water","Grass","Electric","Ground","Flying","Fighting","Fairy","Dragon","Steel","Poison","Dark","Ghost","Normal","Bug","Ice"]:
        tp=mon.maxiv
    if ("Eevee"in mon.name or "eon" in mon.name) and "Last Resort" in mon.moves:
        mon.item="Eevium-Z"
        return ["Extreme Evoboost"]
    elif "Necrozma" in mon.name and "Photon Geyser" in mon.moves:
        mon.item="Ultranecrozium-Z"
        return ["Light That Burns The Sky"]
    elif "Tapu" in mon.name and "Nature's Madness" in mon.moves:
        mon.item="Tapunium-Z"
        return ["Guardian of Alola"]
    elif ("Solgaleo" in mon.name or "Dusk Mane" in mon.name or "Nebby" in mon.name) and "Sunsteel Strike" in mon.moves:
        mon.item="Solganium-Z"
        return ["Searing Sunraze Smash"]
    elif "Primarina" in mon.name and "Sparkling Aria" in mon.moves:
        mon.item="Primarium-Z"
        return ["Oceanic Operetta"]
    elif "Pikachu" in mon.name:
        if "Thunderbolt" in mon.moves:
            mon.item="Pikashunium-Z"
            return ["10,000,000 Volt Thunderbolt"]
        elif "Volt Tackle" in mon.moves:
            mon.item="Pikanium-Z"
            return ["Catastropika"]
    elif "Mimikyu" in mon.name and "Play Rough" in mon.moves:
        mon.item="Mimikium-Z"
        return ["Let's Snuggle Forever"]
    elif "Marshadow" in mon.name and "Spectral Thief" in mon.moves:
        mon.item="Marshadium-Z"
        return ["Soul-Stealing 7-Star Strike"]  
    elif ("Lunala" in mon.name or "Dawn Wing" in mon.name or "Nebby" in mon.name) and "Moongeist Beam" in mon.moves:
        mon.item="Lunalium-Z"
        return ["Menacing Moonraze Maelstrom"]
    elif "Kommo" in mon.name and "Clanging Scales" in mon.moves:
        mon.item="Kommonium-Z"
        return ["Clangorous Soulblaze"]
    elif "Incineroar" in mon.name and "Darkest Lariat" in mon.moves:
        mon.item="Incinum-Z"
        return ["Malicious Moonsault"]
    elif "Decidueye" in mon.name and "Spirit Shackle" in mon.moves:
        mon.item="Decidium-Z"
        return ["Sinister Arrow Raid"]
    elif "Alolan Raichu" in mon.name and "Thunderbolt" in mon.moves:
        mon.item="Aloraichium-Z"
        return ["Stoked Sparksurfer"]
    elif "Mew" in mon.name and "Psychic" in mon.moves:
        mon.item="Mewnium-Z"
        return ["Genesis Supernova"]
    elif "Snorlax" in mon.name and "Giga Impact" in mon.moves:
        mon.item="Snorlium-Z"
        return ["Pulverizing Pancake"]
    elif "Lycanroc" in mon.name and "Stone Edge" in mon.moves:
        mon.item="Lycanium-Z"
        return ["Splintered Stormshards"]        
    elif tp=="Fire":
        mon.item="Firium-Z"
        return ["Inferno Overdrive"]
    elif tp=="Water":
        mon.item="Waterium-Z"
        return ["Hydro Vortex"]
    elif tp=="Poison":
        mon.item="Poisonium-Z"
        return ["Acid Downpour"]
    elif tp=="Fighting":
        mon.item="Fightinium-Z"
        return ["All-Out Pummeling"]
    elif tp=="Dark":
        mon.item="Darkium-Z"
        return ["Black Hole Eclipse"]
    elif tp=="Grass":
        mon.item="Grassium-Z"
        return ["Bloom Doom"]
    elif tp=="Normal":
        mon.item="Normalium-Z"
        return ["Breakneck Blitz"]
    elif tp=="Rock":
        mon.item="Rockium-Z"
        return ["Continental Crush"]
    elif tp=="Steel":
        mon.item="Steelium-Z"
        return ["Corkscrew Crash"]
    elif tp=="Dragon":
        mon.item="Dragonium-Z"
        return ["Devastating Drake"]
    elif tp=="Psychic":
        mon.item="Pychium-Z"
        return ["Shattered Psyche"]
    elif tp=="Electric":
        mon.item="Electrium-Z"
        return ["Gigavolt Havoc"]
    elif tp=="Ghost":
        mon.item="Ghostium-Z"
        return ["Never-ending Nightmare"]
    elif tp=="Bug":
        mon.item="Buginium-Z"
        return ["Savage Spin-Out"]
    elif tp=="Ice":
        mon.item="Icium-Z"
        return ["Subzero Slammer"]
    elif tp=="Ground":
        mon.item="Groundium-Z"
        return ["Tectonic Rage"]
    elif tp=="Fairy":
        mon.item="Fairium-Z"
        return ["Twinkle Tackle"]
    elif tp=="Flying":
        mon.item="Flyinium-Z"   
        return ["Supersonic Skystrike"]   
    
    
         
#Venusaur
class Venusaur(Pokemon2):
    "Venusaur"
    def __init__(self,name="Venusaur",type1="Grass",type2="Poison",nature="None",level=100,happiness=255,hp=80,atk=82,defense=93,spatk=110,spdef=100,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Overgrow","Chlorophyll","Thick Fat"]),item=random.choice(["Black Sludge","Life Orb","Grass Gem","Poison Gem","Venusaurite","Sitrus Berry","Expert Belt","White Herb","Quick Claw","Lum Berry","Shell Bell","Focus Band","Scope Lens"]),weight=220.46):
        if move =="None":
            moves=["Giga Drain","Earth Power","Sludge Bomb","Solar Beam","Sleep Powder","Leech Seed","Frenzy Plant","Synthesis","Sunny Day","Weather Ball","Toxic","Chloroblast","Leaf Storm","Petal Blizzard","Petal Dance","Growth","Razor Leaf","Toxic","Seed Bomb","Double-Edge","Roar","Bullet Seed","Sunny Day","Hyper Beam","Light Screen","Protect","Earthquake","Double Team","Rest","Energy Ball","Giga Impact","Bulldoze","Grass Knot","Substitute","Amnesia","Charm","Grassy Terrain","Leaf Storm","Power Whip","Skull Bash","Hidden Power","Ancient Power","Razor Wind"]
            moves=moveset(type1,type2,moves)
        else:
            moves=move        
        if "OU" in maxiv:
            nature="Modest"
            item="Black Sludge"
            ability="Chlorophyll"
            moves=["Earth Power","Sleep Powder","Giga Drain","Sludge Bomb"]  
        if "Skull Bash" in moves:
            item="Power Herb"         
        color="green"    
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
class Charizard(Pokemon2):
    "Charizard"
    def __init__(self,name="Charizard",type1="Fire",type2="Flying",nature="None",level=100,happiness=255,hp=78,atk=84,defense=78,spatk=110,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Blaze","Solar Power","Flash Fire"]),item=random.choice(["Heavy-Duty Boots","Life Orb","Fire Gem","Choice Specs","Charizardite X","Charizardite Y","Lum Berry","Charti Berry","Salac Berry","Dragon Gem","Focus Sash","King's Rock","Bright Powder"]),weight=199.52):
        color="red"
        if move =="None":
            ch=1
            if item=="Charizardite X":
                spatkev=0
                atkev=252
                avmoves=["Dragon Dance","Dragon Claw","Roost","Thunder Punch","Scale Shot","Night Slash","Dual Wingbeat","Slash"]
                moves=moveset(type1,type2,avmoves,3,name=name)+["Flare Blitz"]
            if item=="Charizardite Y":
                avmoves=["Roost","Flamethrower","Fire Blast","Blast Burn","Air Slash","Dragon Pulse","Ancient Power","Hurricane","Focus Blast","Hidden Power","Heat Wave"]
                moves=moveset(type1,type2,avmoves,name=name)
            else:
                avmoves=["Flare Blitz","Dragon Dance","Dragon Claw","Roost","Flamethrower","Fire Blast","Blast Burn","Air Slash","Dragon Pulse","Thunder Punch","Ancient Power","Scale Shot","Hurricane","Focus Blast","Heat Wave","Fire Fang","Slash","Inferno","Protect","Acrobatics","Aerial Ace","Bulldoze","Rock Tomb","Flame Charge","Dragon Tail","Sunny Day","Brick Break","Shadow Claw","Body Slam","Fire Punch","Rest","Rock Slide","Swords Dance","Substitute","Will-O-Wisp","Crunch","Dragon Pulse","Earthquake","Giga Impact","Outrage","Overheat","Hyper Beam","Belly Drum","Dragon Rush","Iron Tail","Fly"]
                moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if name=="Charizard":
            ch=random.randint(1,5)
            if ch==5:
                name+=" the Unrivaled"
                ability="Solar Power"
                moves=["Dragon Pulse","Fire Blast","Hurricane","Focus Blast"]
                maxiv="Dragon"
        if "OU" in maxiv:
            maxiv="Grass"
            nature="Timid"
            item="Charizardite Y"
            ability="Blaze"
            moves=["Hidden Power","Air Slash","Fire Blast","Focus Blast"] 
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight, color=color)
class Blastoise(Pokemon2):
    "Blastoise"
    def __init__(self,name="Blastoise",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=84,atk=73,defense=100,spatk=95,spdef=105,speed=78,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Torrent","Rain Dish","Shell Armor"]),item=random.choice(["Sitrus Berry","Life Orb","Water Gem","Blastoisinite","Salac Berry","Choice Scarf","Quick Claw","Mystic Water","Lum Berry"]),weight=188.50):
        color="blue"
        if move =="None":
            avmoves=["Hydro Pump","Shell Smash","Flip Turn","Hydro Cannon","Skull Bash","Rapid Spin","Aura Sphere","Water Spout","Dark Pulse","Flash Cannon","Protect","Rain Dance","Aqua Tail","Iron Defense","Focus Punch","Roar","Blizzard","Hyper Beam","Iron Tail","Earthquake","Brick Break","Double Team","Rock Tomb","Rest","Scald","Focus Blast","Dragon Pulse","Giga Impact","Avalanche","Gyro Ball","Rock Slide","Swagger","Bulldoze","Substitute","Surf","Waterfall","Aqua Jet","Aqua Ring","Fake Out","Muddy Water","Yawn","Outrage","Mirror Coat","Yawn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "OU" in maxiv:
            nature="Timid"
            item="Blastoisinite"
            ability="Rain Dish"
            moves=["Rapid Spin","Dark Pulse","Aura Sphere","Ice Beam"] 
        if "Gyro Ball" in moves:
            item="Iron Ball"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)

#Nidoqueen
class Nidoqueen(Pokemon2):
    "Nidoqueen"
    def __init__(self,name="Nidoqueen",type1="Poison",type2="Ground",nature="None",level=100,happiness=255,hp=90,atk=75,defense=87,spatk=87,spdef=85,speed=76,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sheer Force","Poison Touch"]),item=random.choice(["Black Sludge","Life Orb","Passho Berry","Bright Powder"]),weight=132.28):
        color="blue"
        if move =="None":
            moves=["Ice Beam","Earth Power","Sludge Bomb","Strength","Poison Jab","Toxic Spikes","Taunt","Toxic","Stealth Rock","Superpower","Thunder"]
            moves=moveset(type1,type2,moves)
        else:
            moves=move
        if "OU" in maxiv:
            nature="Timid"
            item="Life Orb"
            ability="Sheer Force"
            moves=["Stealth Rock","Earth Power",random.choice(["Sludge Wave","Ice Beam"]),random.choice(["Taunt","Toxic"])] 
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
        
        
#Nidoking
class Nidoking(Pokemon2):
    "Nidoking"
    def __init__(self,name="Nidoking",type1="Poison",type2="Ground",nature="None",level=100,happiness=255,hp=81,atk=102,defense=77,spatk=85,spdef=75,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sheer Force","Poison Touch"]),item=random.choice(["Black Sludge","Life Orb","Shuca Berry","Choice Specs","Bright Powder"]),weight=136.69):
        color="magenta"
        if move =="None":
            ch=1
            if ch==1:
                moves=["Ice Beam","Earth Power","Sludge Bomb","Strength","Poison Jab","Toxic Spikes","Head Smash","Blizzard","Megahorn","Flamethrower","Thrash"]
                moves=moveset(type1,type2,moves)
            if ch==2:
                moves=["Sludge Wave","Earth Power","Ice Beam","Taunt"]
                nature="Timid"
                item="Life Orb"
                ability="Sheer Force"
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Ninetales
class Ninetales(Pokemon2):
    "Ninetales"
    def __init__(self,name="Ninetales",type1="Fire",type2="None",    nature="None",level=100,happiness=255,hp=73,atk=66,defense=75,spatk=96,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Drought"]),item=random.choice(["Heat Rock","Life Orb","Fire Gem","Air Balloon","Charti Berry","Passho Berry"]),weight=43.87):
        color="yellow"
        if move =="None":
            avmoves=["Fire Blast","Flamethrower","Solar Beam","Hidden Power","Weather Ball","Heat Wave","Scorching Sands","Psyshock","Dark Pulse","Fire Spin"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "OU" in maxiv:
            maxiv="Ice"
            name="Ninetales"
            nature="Timid"
            item="Firium-Z"
            ability="Drought"
            moves=["Hidden Power","Nasty Plot","Fire Blast","Solar Beam"] 
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Alolan Ninetales
class ANinetales(Pokemon2):
    "Alolan Ninetales"
    def __init__(self,name="Alolan Ninetales",type1="Ice",type2="Fairy",    nature="None",level=100,happiness=255,hp=73,atk=67,defense=75,spatk=81,spdef=100,speed=109,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Snow Warning","Snow Cloak","Serene Grace"]),item=random.choice(["Icy Rock","Light Clay","Ice Gem","Fairy Gem","Choice Specs"]),weight=43.87):
        color="cyan"
        if move =="None":
            avmoves=["Ice Beam","Moonblast","Hidden Power","Dazzling Gleam","Aurora Veil","Triple Axel","Weather Ball","Freeze-Dry","Blizzard","Energy Ball"]
            moves=moveset(type1,type2,avmoves,name=name)            
        else:
            moves=move
        if "OU" in maxiv:
            nature="Timid"
            item="Light Clay"
            ability="Snow Warning"
            moves=["Aurora Veil","Freeze-Dry","Hypnosis","Snowscape"] 
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Golduck
class Golduck(Pokemon2):
    "Golduck"
    def __init__(self,name="Golduck",type1="Water",type2="Psychic",    nature="None",level=100,happiness=255,hp=80,atk=72,defense=78,spatk=105,spdef=80,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Neuroforce","Swift Swim","Cloud Nine"]),item=random.choice(["Leftovers","Life Orb","Petaya Berry","Water Gem","Pecha Berry"]),weight=168.87):
        color="cyan"
        if move =="None":
            avmoves=["Ice Beam","Psychic","Hydro Pump","Hidden Power","Rain Dance","Nasty Plot","Power Gem","Chilling Water","Future Sight","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "OU" in maxiv:
            maxiv="Grass"
            nature="Modest"
            item="Life Orb"
            ability="Swift Swim"
            moves=["Rain Dance","Ice Beam","Hidden Power",random.choice(["Hydro Pump","Surf"])]
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Primeape
class Primeape(Pokemon2):
    "Primeape"
    def __init__(self,name="Primeape",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=65,atk=105,defense=60,spatk=60,spdef=70,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Gorilla Tactics","Defiant","Vital Spirit","Anger Point"]),item=random.choice(["Choice Scarf","Life Orb","Eviolite","Liechi Berry"]),weight=70.55):
        color="red"
        if move =="None":
            avmoves=["Hidden Power","Dynamic Punch","Close Combat","Superpower","Fire Punch","U-turn","Cross Chop","Skull Bash","Rage Fist","Outrage","Stone Edge","Thrash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Annihilape
class Annihilape(Pokemon2):
    def __init__(self,name="Annihilape",type1="Fighting",type2="Ghost",nature="None",level=100,happiness=255,hp=110,atk=115,defense=80,spatk=50,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Defiant","Inner Focus","Vital Spirit"]),item=random.choice(["Choice Scarf","Life Orb","Leftovers"]),weight=123.46):
        color="cyan"
        if move =="None":
            avmoves=["Drain Punch","Close Combat","Superpower","Fire Punch","U-turn","Cross Chop","Shadow Claw","Shadow Sneak","Final Gambit","Bulk Up","Rest","Taunt"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Rage Fist"]
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        if "Final Gambit" in moves:
            hpev=252
            atkev=0
        if "OU" in maxiv:
            hpev=240
            spdefev=252
            speedev=16
            atkev=0
            maxiv=random.choice(["Water","Fairy"])
            nature="Careful"
            item="Leftovers"
            ability="Defiant"
            moves=["Bulk Up","Rage Fist","Drain Punch",random.choice(["Rest","Taunt"])] 
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
        
#Arcanine
class Arcanine(Pokemon2):
    "Arcanine"
    def __init__(self,name="Arcanine",type1="Fire",type2="None",nature="None",level=100,happiness=255,hp=90,atk=110,defense=80,spatk=100,spdef=80,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Flash Fire","Justified"]),item=random.choice(["Heavy-Duty Boots","Life Orb","Sitrus Berry","Safety Googles","Weakness Policy","Liechi Berry","Focus Sash","Expert Belt","Lum Berry"]),weight=341.72):
        color="red"
        if move =="None":
            moves=["Snarl","Fire Blast","Flamethrower","Sunny Day","Solar Beam","Flare Blitz","Wild Charge","Morning Sun","Extreme Speed","Will-O-Wisp","Protect","Close Combat","Play Rough","Dragon Pulse","Bulldoze"]
            moves=moveset(type1,type2,moves)
        else:
            moves=move
        if "Dragon Pulse" in moves:
            item="Dragon Gem"
        if "OU" in maxiv:
            hpev=252
            defev=236
            speedev=20
            atkev=0
            nature="Impish"
            item="Heavy-Duty Boots"
            ability="Intimidate"
            moves=["Flare Blitz","Will-O-Wisp","Morning Sun","Roar"]
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
        
#Poliwrath
class Poliwrath(Pokemon2):
    "Poliwrath"
    def __init__(self,name="Poliwrath",type1="Water",type2="Fighting",nature="None",level=100,happiness=255,hp=90,atk=115,defense=95,spatk=70,spdef=90,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Water Absorb","Swift Swim","Damp"]),item=random.choice(["Choice Band","Life Orb","Leftovers","Salac Berry","Water Gem","Sitrus Berry","Quick Claw"]),weight=119.05):
        color="blue"
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Dynamic Punch","Thunder Punch","Rain Dance","Submission","Darkest Lariat","Surging Strikes","Hypnosis","Belly Drum","Waterfall","Rock Slide","Focus Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "OU" in maxiv:
            ch=random.randint(1,2)
            if ch==2:
                hpev=252
                speedev=96
                defev=160
                nature="Bold"
                item="Leftovers"
                ability="Water Absorb"
                moves=["Surging Strikes","Scald","Rest","Sleep Talk"]
            if ch==1:
                spdefev=4
                speedev=252
                atkev=252
                nature="Adamant"
                item="Choice Band"
                ability="Water Absorb"
                moves=["Liquidation","Close Combat","Darkest Lariat",random.choice(["Earthquake","Poison Jab"])]
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)

#Pidgeot        
class Pidgeot(Pokemon2):
    "Pidgeot"
    def __init__(self,name="Pidgeot",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=83,atk=60,defense=75,spatk=115,spdef=70,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Quick Feet","Frisk","No Guard"]),item=random.choice(["Choice Band","Life Orb","Flying Gem","Pidgeotite","Sitrus Berry"]),weight=87.08):
        color="yellow"
        if move =="None":
            avmoves=["Hidden Power","Hurricane","Dual Wingbeat","Brave Bird","U-turn","Roost","Tailwind","Heat Wave","Focus Blast","Hyper Voice","Sand-Attack","Quick Attack","Whirlwind","Feather Dance","Agility","Air Slash","Hyper Beam","Protect","Double Team","Steel Wing","Substitute","Defog","Swagger","Return","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "OU" in maxiv:
            nature="Timid"
            item="Pidgeotite"
            ability="Big Pecks"
            moves=["Hurricane","Heat Wave","Morning Sun","Whirlwind"]
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Alakazam
class Alakazam(Pokemon2):
    "Alakazam"
    def __init__(self,name="Alakazam",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=55,atk=50,defense=45,spatk=135,spdef=95,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Magic Guard","Inner Focus","Synchronize"]),item=random.choice(["Focus Sash","Choice Specs","Life Orb","Leftovers","Alakazite","Twisted Spoon","Colbur Berry"]),weight=105.82):
        color="yellow"
        if move =="None":
            avmoves=["Hidden Power","Recover","Dazzling Gleam","Shadow Ball","Nasty Plot","Dark Pulse","Focus Blast","Expanding Force","Trick","Signal Beam","Grass Knot","Calm Mind","Psyshock","Thunder Wave"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Psychic"]
        else:
            moves=move
        if "OU" in maxiv:
            nature="Timid"
            item="Life Orb"
            ability="Magic Guard"
            moves=["Focus Blast","Psychic","Nasty Plot","Shadow Ball"]
        if " Magic Guard" in ability and "Trick" in moves:
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Beheeyem
class Beheeyem(Pokemon2):
    def __init__(self,name="Beheeyem",type1="Psychic",type2="Steel",nature="None",level=100,happiness=255,hp=95,atk=75,defense=75,spatk=125,spdef=95,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Analytic","Synchronize"]),item="Focus Sash",weight=76.06):
        color="red"
        if move =="None":
            avmoves=["Hidden Power","Recover","Shadow Ball","Nasty Plot","Dark Pulse","Focus Blast","Expanding Force","Psychic","Flash Cannon"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Ajjimajji
class Ajjimajji(Pokemon2):
    def __init__(self,name="Ajjimajji",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=120,atk=50,defense=45,spatk=95,spdef=135,speed=55,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Magic Guard","Levitate"]),item="Focus Sash",weight=100):
        if move =="None":
            avmoves=["Hidden Power","Recover","Dazzling Gleam","Shadow Ball","Calm Mind","Dark Pulse","Focus Blast","Expanding Force","Light Screen"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                      

#Machamp
class Machamp(Pokemon2):
    "Machamp"
    def __init__(self,name="Machamp",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=90,atk=130,defense=80,spatk=65,spdef=85,speed=55,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["No Guard","Guts"]),item=random.choice(["Choice Band","Black Belt","Expert Belt","Payapa Berry","Lum Berry","Sitrus Berry","Scope Lens","White Herb","Focus Sash","Choice Scarf"]),weight=286.60):
        color="cyan"
        if move =="None":
            avmoves=["Dynamic Punch","Close Combat","Superpower","Fire Punch","Cross Chop","Submission","Darkest Lariat","Drain Punch","Mach Punch","Rock Slide","Bulldoze","Dual Chop","Bulk Up","Earthquake","Stone Edge","Ice Punch","Knock Off","Encore"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Machug
class Machug(Pokemon2):
    def __init__(self,name="Machug",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=110,atk=130,defense=90,spatk=65,spdef=75,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Thick Fat","Guts"]),item=random.choice(["Choice Band","Black Belt","Sitrus Berry"]),weight=400):
        if move =="None":
            avmoves=["Close Combat","Superpower","Fire Punch","Cross Chop","Submission","Belly Drum"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                             
#Victreebel
class Victreebel(Pokemon2):
    "Victreebel"
    def __init__(self,name="Victreebel",type1="Grass",type2="Poison",nature="None",level=100,happiness=255,hp=80,atk=105,defense=85,spatk=80,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Gluttony"]),item=random.choice(["Rocky Helmet","Black Sludge","Life Orb","Salac Berry","Wide Lens","Power Herb"]),weight=34.17):
        color="yellow"
        if move =="None":
            avmoves=["Power Whip","Sludge Bomb","Sleep Powder","Solar Beam","Toxic","Toxic Spikes","Solar Blade","Giga Drain","Weather Ball","Knock Off","Gunk Shot","Sucker Punch","Reflect","Swords Dance"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Bustoliv
class Bustoliv(Pokemon2):
    def __init__(self,name="Bustoliv",type1="Grass",type2="Normal",nature="None",level=100,happiness=255,hp=60,atk=45,defense=80,spatk=90,spdef=105,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Chlorophyll",item=random.choice(["Rocky Helmet","Miracle Seed"]),weight=100):
        if move =="None":
            avmoves=["Sleep Powder","Solar Beam","Synthesis","Sunny Day","Giga Drain"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)        
#Tentacruel
class Tentacruel(Pokemon2):
    "Tentacruel"
    def __init__(self,name="Tentacruel",type1="Water",type2="Poison",nature="None",level=100,happiness=255,hp=80,atk=60,defense=75,spatk=95,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move="None", ability=random.choice(["Clear Body","Liquid Ooze","Rain Dish"]),item=random.choice(["Black Sludge","Apicot Berry","Scope Lens","Focus Sash"]),weight=121.25):
        color="cyan"
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Sludge Bomb","Poison Jab","Rain Dance","Toxic Spikes","Sludge Wave","Giga Drain","Scald","Rest","Aurora Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry "
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Toedscruel
class Toedscruel(Pokemon2):
    def __init__(self,name="Toedscruel",type1="Grass",type2="Ground",nature="None",level=100,happiness=255,hp=80,atk=60,defense=80,spatk=90,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move="None", ability=random.choice(["Effect Spore","Mycelium Might"]),item="Leftovers",weight=127.87):
        color="yellow"
        if move =="None":
            avmoves=["Hidden Power","Earth Power","Giga Drain","Bulldoze","Sludge Bomb","Poison Jab","Sunny Day","Stealth Rock","Spore"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Doncrete
class Doncrete(Pokemon2):
    def __init__(self,name="Doncrete",type1="Rock",type2="Ground",nature="None",level=100,happiness=255,hp=70,atk=110,defense=120,spatk=55,spdef=75,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Rock Head","Dark Mind"]),item=random.choice(["Weakness Policy"]),weight=100):
        if move =="None":
            avmoves=["Stone Edge","Earthquake","Stealth Rock","Rock Blast","Night Slash","Magnitude","Bulldoze","Foul Play"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Explosion" in moves:
            ability="Sturdy"
            item="Custap Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)        
#Golem
class Golem(Pokemon2):
    "Golem"
    def __init__(self,name="Golem",type1="Rock",type2="Ground",nature="None",level=100,happiness=255,hp=80,atk=120,defense=130,spatk=55,spdef=65,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Rock Head","Sturdy","Sand Veil"]),item=random.choice(["Weakness Policy","Rindo Berry","Salac Berry","Passho Berry","Lum Berry","Ground Gem","Choice Band"]),weight=661.39):
        color="yellow"
        if move =="None":
            avmoves=["Stone Edge","Stealth Rock","Rock Blast","Explosion","Magnitude","Bulldoze","Head Smash","Headlong Rush","Body Press","Heat Crash","Sucker Punch","Iron Defense","Roar","Iron Head","Rock Polish","Curse","Gyro Ball","Fire Punch","Protect"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Earthquake"]
        else:
            moves=move
        if "Sucker Punch" in moves:
            item="Dark Gem"
        if "Explosion" in moves:
            ability="Sturdy"
            item="Custap Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Golem
class AGolem(Pokemon2):
    "Alolan Golem"
    def __init__(self,name="Alolan Golem",type1="Rock",type2="Electric",nature="None",level=100,happiness=255,hp=80,atk=120,defense=130,spatk=55,spdef=65,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Galvanize","Sturdy","Magnet Pull","Rock Head"]),item=random.choice(["Choice Scarf","Weakness Policy","Air Balloon"]),weight=696.66):
        color="yellow"
        if move =="None":
            avmoves=["Stone Edge","Earthquake","Stealth Rock","Rock Blast","Thunderbolt","Explosion","Magnitude","Bulldoze","Volt Tackle","Headlong Rush","Body Press","Heat Crash","Rock Polish"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Explosion" in moves:
            ability="Sturdy"
            item="Custap Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            #Rapidash
class Rapidash(Pokemon2):
    "Rapidash"
    def __init__(self,name="Rapidash",type1="Fire",type2="None",nature="None",level=100,happiness=255,hp=65,atk=100,defense=70,spatk=80,spdef=80,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Reckless","Blazing Soul","Flame Body"]),item=random.choice(["Choice Band","Heavy-Duty Boots","Shuca Berry"]),weight=209.44):
        color="yellow"
        if move =="None":
            avmoves=["Fire Blast","Flamethrower","Flare Blitz","Inferno","Morning Sun","Sunny Day","High Horsepower","Bounce","Rest","Protect","Toxic","Fire Spin"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)

#Dodrio
class Dodrio(Pokemon2):
    "Dodrio"
    def __init__(self,name="Dodrio",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=60,atk=130,defense=70,spatk=60,spdef=60,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Rock Head","Early Bird","Quick Feet","Defiant","Tangled Feet"]),item=random.choice(["Choice Scarf","Heavy-Duty Boots","Wacan Berry"]),weight=187.83):
        color="red"
        if move =="None":
            avmoves=["Close Combat","Brave Bird","Roost","Sky Attack","High Jump Kick","U-turn","Double-Edge","Tri Attack","Drill Peck","Acupressure","Thrash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
        
#Garbodor
class Garbodor(Pokemon2):
    def __init__(self,name="Garbodor",type1="Poison",type2="None",nature="None",level=100,happiness=255,hp=80,atk=105,defense=92,spatk=60,spdef=92,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Aftermath","Stench","Unburden","Weak Armor"]),item=random.choice(["Black Sludge","Shuca Berry","Payapa Berry","Salac Berry","Expert Belt"]),weight=236.56):
        color="magenta"
        if move =="None":
            avmoves=["Poison Jab","Acid Armor","Toxic","Sludge Bomb","Venoshock","Toxic Spikes","Explosion","Pain Split","Gunk Shot","Rock Blast","Thunderbolt","Focus Blast","Psychic"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Muk
class Muk(Pokemon2):
    "Muk"
    def __init__(self,name="Muk",type1="Poison",type2="None",nature="None",level=100,happiness=255,hp=105,atk=110,defense=75,spatk=65,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Poison Touch","Regenerator","Sticky Hold","Stench"]),item=random.choice(["Black Sludge","Shuca Berry","Payapa Berry","Quick Claw","Aguav Berry"]),weight=66.14):
        color="magenta"
        if move =="None":
            avmoves=["Poison Jab","Acid Armor","Toxic","Sludge Bomb","Venoshock","Toxic Spikes","Gunk Shot","Knock Off","Shadow Sneak","Minimize","Curse","Rock Slide"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                       
#Cloyster
class Cloyster(Pokemon2):
    "Cloyster"
    def __init__(self,name="Cloyster",type1="Water",type2="Ice",nature="None",level=100,happiness=255,hp=50,atk=95,defense=180,spatk=85,spdef=45,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Skill Link","Shell Armor","Overcoat"]),item=random.choice(["Focus Sash","King's Rock","Salac Berry"]),weight=292.11):
        color="cyan"
        if move =="None":
            avmoves=["Ice Beam","Rock Blast","Icicle Spear","Shell Smash","Hydro Pump","Pin Missile","Snowscape","Liquidation","Razor Shell","Explosion","Aurora Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                               
#Gengar
class Gengar(Pokemon2):
    "Gengar"
    def __init__(self,name="Gengar",type1="Ghost",type2="Poison",nature="None",level=100,happiness=255,hp=60,atk=65,defense=60,spatk=130,spdef=75,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate","Shadow Tag","Cursed Body"]),item=random.choice(["Black Sludge","Gengarite","Petaya Berry","Wide Lens","Focus Sash","Scope Lens","Life Orb","Payapa Berry"]),weight=89.29):
        color="magenta"
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Dazzling Gleam","Psychic","Shadow Ball","Dark Pulse","Thunderbolt","Nasty Plot","Destiny Bond","Sludge Bomb","Perish Song","Skitter Smack","Substitute","Focus Blast","Hypnosis","Giga Drain","Skill Swap"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Dangal
class Dangal(Pokemon2):
    def __init__(self,name="Dangal",type1="Ghost",type2="Dark",nature="None",level=100,happiness=255,hp=70,atk=85,defense=70,spatk=110,spdef=75,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Levitate",item="Black Glasees",weight=100):
        if move =="None":
            avmoves=["Hidden Power","Shadow Ball","Dark Pulse","Nasty Plot","Destiny Bond","Night Daze","Leech Life"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
  #Exeggutor
class Exeggutor(Pokemon2):
    "Exeggutor"
    def __init__(self,name="Exeggutor",type1="Grass",type2="Psychic",nature="None",level=100,happiness=255,hp=95,atk=75,defense=100,spatk=125,spdef=95,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Harvest"]),item=random.choice(["Lum Berry","Leftovers","Petaya Berry","Tanga Berry","Life Orb","Focus Sash","Miracle Seed","Expert Belt"]),weight=264.55):
        color="green"
        if move =="None":
            avmoves=["Hidden Power","Giga Drain","Sunny Day","Psychic","Solar Beam","Egg Bomb","Leech Seed","Morning Sun","Light Screen","Expanding Force","Weather Ball","Psyshock","Future Sight","Zen Headbutt","Wood Hammer","Explosion"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)             
#Alolan Exeggutor
class AExeggutor(Pokemon2):
    "Alolan Exeggutor"
    def __init__(self,name="Alolan Exeggutor",type1="Grass",type2="Dragon",nature="None",level=100,happiness=255,hp=95,atk=105,defense=85,spatk=125,spdef=75,speed=45,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Harvest"]),item="Leftovers",weight=916.24):
        color="green"
        if move =="None":
            avmoves=["Sunny Day","Egg Bomb","Psychic","Solar Beam","Dragon Hammer","Zen Headbutt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            
 #Alolan Muk
class AMuk(Pokemon2):
    "Alolan Muk"
    def __init__(self,name="Alolan Muk",type1="Poison",type2="Dark",nature="None",level=100,happiness=255,hp=105,atk=105,defense=75,spatk=65,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Power of Alchemy","Poison Touch"]),item=random.choice(["Black Sludge","Assault Vest"]),weight=114.64):
        color="magenta"
        if move =="None":
            avmoves=["Sludge Bomb","Toxic","Poison Jab","Venoshock","Toxic Spikes","Drain Punch","Fire Punch","Poison Fang","Knock Off","Ice Punch","Parting Shot","Sucker Punch","Minimize"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Hitmonlee
class Hitmonlee(Pokemon2):
    "Hitmonlee"
    def __init__(self,name="Hitmonlee",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=50,atk=120,defense=68,spatk=35,spdef=110,speed=87,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Reckless","Limber","Striker","Unburden"]),item=random.choice(["Choice Band","Assault Vest","Electric Seed","Black Belt","Salac Berry","Life Orb"]),weight=109.79):
        color="red"
        if move =="None":
            avmoves=["Blaze Kick","High Jump Kick","Superpower","Pyro Ball","Low Kick","Close Combat","Brick Break","Head Smash","Bulk Up","Sucker Punch","Bulldoze","Fake Out","Stone Edge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Hitmontop
class Hitmontop(Pokemon2):
    def __init__(self,name="Hitmontop",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=60,atk=100,defense=95,spatk=35,spdef=110,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Technician"]),item=random.choice(["Choice Band","Assault Vest","Liechi Berry","Wide Lens","Sitrus Berry"]),weight=105.82):
        color="blue"
        if move =="None":
            avmoves=["Triple Kick","Sucker Punch","Superpower","Gyro Ball","Low Kick","Close Combat","Rapid Spin","Triple Axel","Dig","Drill Run","Bulk Up","Bullet Punch","Mach Punch","Fake Out"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Drill Run" in moves:
            item="Ground Gem"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Hitmonchan
class Hitmonchan(Pokemon2):
    "Hitmonchan"
    def __init__(self,name="Hitmonchan",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=65,atk=115,defense=79,spatk=35,spdef=110,speed=76,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Iron Fist",item=random.choice(["Assault Vest","Choice Band","Punching Glove","Black Belt","Leftovers"]),weight=110.67):
        color="red"
        if move =="None":
            avmoves=["Ice Punch","Thunder Punch","Mach Punch","Fire Punch","Dizzy Punch","Dynamic Punch","Close Combat","Double Team","Drain Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Ice Punch" in moves:
            ch=random.randint(1,2)
            if ch==1:
                item="Ice Gem"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            #Weezing
class Weezing(Pokemon2):
    "Weezing"
    def __init__(self,name="Weezing",type1="Poison",type2="None",nature="None",level=100,happiness=255,hp=65,atk=90,defense=120,spatk=85,spdef=70,speed=60,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Levitate",item=random.choice(["Black Sludge","Rocky Helmet"]),weight=20.94):
        color="magenta"
        if move =="None":
            avmoves=["Sludge Bomb","Toxic","Poison Jab","Venoshock","Explosion","Toxic Spikes","Pain Split","Fire Blast","Shadow Ball","Thunderbolt","Will-O-Wisp","Flamethrower"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Fire Blast" in moves:
            item="Fire Gem"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
#Kangaskhan
class Kangaskhan(Pokemon2):
    "Kangaskhan"
    def __init__(self,name="Kangaskhan",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=105,atk=95,defense=80,spatk=40,spdef=80,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Scrappy",item=random.choice(["Silk Scarf","Heavy-Duty Boots","Kangaskhanite","Chople Berry","Pecha Berry"]),weight=176.37):
        color="yellow"
        if move =="None":
            avmoves=["Crunch","Body Slam","Fake Out","Power-up Punch","Earthquake","Ice Punch","Sucker Punch","Hammer Arm"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Komala
class Komala(Pokemon2):
    def __init__(self,name="Komala",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=75,atk=115,defense=65,spatk=75,spdef=95,speed=65,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Comatose",item=random.choice(["Silk Scarf","Leftovers","Quick Claw"]),weight=43.87):
        color="cyan"
        if move =="None":
            avmoves=["Last Resort","Body Slam","Sucker Punch","Wood Hammer","Zen Headbutt","Outrage","Aqua Tail","Hammer Arm","Thrash","Yawn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Eevee
class Eevee(Pokemon2):
    "Eevee"
    def __init__(self,name="Eevee",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=65,atk=75,defense=70,spatk=65,spdef=85,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Adaptability",item=random.choice(["Silk Scarf","Heavy-Duty Boots","Chople Berry"]),weight=14.33):
        if move =="None":
            avmoves=["Double-Edge","Body Slam","Quick Attack","Shadow Ball","Last Resort"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                         
   
#Starmie
class Starmie(Pokemon2):
    "Starmie"
    def __init__(self,name="Starmie",type1="Water",type2="Psychic",nature="None",level=100,happiness=255,hp=60,atk=75,defense=85,spatk=100,spdef=85,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Natural Cure","Analytic"]),item=random.choice(["Life Orb","Sitrus Berry","Mystic Water","Ganlon Berry","Petaya Berry","Choice Scarf","Choice Specs","Focus Sash","Expert Belt","Wide Lens","Lum Berry"]),weight=176.37):
        color="magenta"
        if move =="None":
            avmoves=["Meteor Beam","Hidden Power","Ice Beam","Scald","Psychic","Surf","Hydro Pump","Thunderbolt","Flip Turn","Recover","Rapid Spin","Minimize","Recover","Cosmic Power","Psyshock","Grass Knot","Reflect","Light Screen","Thunder","Blizzard","Rain Dance","Aurora Beam","Substitute","Thunder Wave","Hidden Power"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rain Dance" in moves:
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Pinsir
class Pinsir(Pokemon2):
    "Pinsir"
    def __init__(self,name="Pinsir",type1="Bug",type2="None",nature="None",level=100,happiness=255,hp=65,atk=125,defense=100,spatk=55,spdef=70,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Moxie","Mold Breaker"]),item=random.choice(["Life Orb","Pinsirite","Liechi Berry","Choice Scarf","Salac Berry","Scope Lens"]),weight=121.25):
        color="red"
        if move =="None":
            avmoves=["Megahorn","Return","Brick Break","Close Combat","Submission","Guillotine","Swords Dance","Superpower","Bulk Up","Earthquake","Bulldoze","X-Scissor","Facade","Storm Throw"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Facade" in moves:
            item="Toxic Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)

#Dubwool
class Dubwool(Pokemon2):
    def __init__(self,name="Dubwool",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=82,atk=80,defense=100,spatk=60,spdef=90,speed=88,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Fluffy","Bulletproof","Steadfast"]),item="Leftovers",weight=94.8):
        if move =="None":
            avmoves=["Double-Edge","Strength","Earthquake","Drill Run","Head Smash","Megahorn","Rest","Head Charge","Cotton Guard","Counter"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)        
#Tauros
class Tauros(Pokemon2):
    "Tauros"
    def __init__(self,name="Tauros",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=75,atk=100,defense=95,spatk=70,spdef=70,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Sheer Force","Anger Point"]),item=random.choice(["Life Orb","Lum Berry"]),weight=194.89):
        color="red"
        if move =="None":
            avmoves=["Double-Edge","Strength","Earthquake","Drill Run","Head Smash","Megahorn","Rest","Head Charge","Will-O-Wisp","Iron Head","Body Slam","Outrage","Thrash","Return","Zen Headbutt","Giga Impact"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Tauros
class PTauros(Pokemon2):
    def __init__(self,name="Paldean Tauros",type1="Fighting",type2=random.choice(["None","Fire","Water"]),nature="None",level=100,happiness=255,hp=75,atk=110,defense=105,spatk=30,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Anger Point","Cud Chew"]),item="Life Orb",weight=100):
        if move =="None":
            avmoves=["Close Combat","Strength","Earthquake","Zen Headbutt","Head Smash","Megahorn","Rest","Head Charge","Drill Run","Raging Bull"]
            if type2=="None":
                moves=moveset(type1,type2,avmoves,3,name=name)+["Double-Edge"]
                weight=253.53
                color="red"
            if type2=="Fire":
                name+="(Blaze Breed)"
                moves=moveset(type1,type2,avmoves,3,name=name)+["Flare Blitz"]
                color="red"
                weight=187.39
            if type2=="Water":
                name+="(Aqua Breed)"
                moves=moveset(type1,type2,avmoves,3,name=name)+["Wave Crash"]
                color="blue"
                weight=242.51
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Gyarados
class Gyarados(Pokemon2):
    "Gyarados"
    def __init__(self,name="Gyarados",type1="Water",type2="Flying",nature="None",level=100,happiness=255,hp=95,atk=125,defense=79,spatk=60,spdef=100,speed=81,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Moxie"]),item=random.choice(["Mystic Water","Heavy-Duty Boots","Lum Berry","Gyaradosite","Muscle Band","Wacan Berry","Leftovers","King's Rock"]),weight=518.09):
        color="cyan"
        if move =="None":
            avmoves=["Crunch","Waterfall","Earthquake","Aqua Tail","Ice Fang","Power Whip","Scale Shot","Stone Edge","Outrage","Substitute","Rest","Aqua Fang"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Dragon Dance"]
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)

#Lapras
class Lapras(Pokemon2):
    "Lapras"
    def __init__(self,name="Lapras",type1="Water",type2="Dragon",nature="None",level=100,happiness=255,hp=130,atk=75,defense=90,spatk=95,spdef=95,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Water Absorb","Liquid Voice","Shell Armor"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","Ganlon Berry","Petaya Berry","Zoom Lens","Sitrus Berry","Lum Berry"]),weight=485.02):
        color="cyan"
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Snowscape","Rain Dance","Aurora Veil","Boomburst","Sparkling Aria","Perish Song","Future Sight","Dragon Pulse","Ice Shard","Recover","Psychic","Ice Shard","Sheer Cold","Rest"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)

#Omastar
class Omastar(Pokemon2):
    "Omastar"
    def __init__(self,name="Omastar",type1="Rock",type2="Water",nature="None",level=100,happiness=255,hp=70,atk=60,defense=125,spatk=115,spdef=70,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Shell Armor","Swift Swim","Weak Armor"]),item=random.choice(["White Herb","Mystic Water","Rindo Berry"]),weight=77.16):
        color="cyan"
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Hydro Pump","Ancient Power","Rock Blast","Stealth Rock","Meteor Beam","Shell Smash","Earth Power","Power Gem","Hydro Cannon"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Meteor Beam" in moves:
            item="Power Herb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)             
#Kabutops
class Kabutops(Pokemon2):
    "Kabutops"
    def __init__(self,name="Kabutops",type1="Rock",type2="Water",nature="None",level=100,happiness=255,hp=60,atk=140,defense=105,spatk=65,spdef=70,speed=80,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Swift Swim","Sharpness","Battle Armor"]),item=random.choice(["Choice Band","Life Orb","Salac Berry","Liechi Berry","Focus Sash"]),weight=89.29):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Liquidation","Hydro Pump","Rock Slide","Stone Edge","Flip Turn","Stealth Rock","Meteor Beam","Stone Axe","Earthquake","Rock Wrecker","Dig","Swords Dance","Superpower","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                  
#Aerodactyl
class Aerodactyl (Pokemon2):
    "Aerodactyl"
    def __init__(self,name="Aerodactyl",type1="Rock",type2="Flying",nature="None",level=100,happiness=255,hp=80,atk=105,defense=65,spatk=60,spdef=75,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Rock Head","Pressure","Unnerve"]),item=random.choice(["Flying Gem","Heavy-Duty Boots","Aerodactylite","Passho Berry","Charti Berry","Choice Scarf","Focus Sash","Choice Band","Yache Berry","King's Rock"]),weight=130.07):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Ancient Power","Stone Edge","Rock Slide","Brave Bird","Stealth Rock","Meteor Beam","Taunt","Substitute","Thunder Fang","Tailwind","Earthquake","Ice Fang","Swagger","Iron Head","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
 
#Snorlax
class Snorlax(Pokemon2):
    "Snorlax"
    def __init__(self,name="Snorlax",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=160,atk=110,defense=65,spatk=65,spdef=110,speed=30,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Thick Fat","Immunity"]),item=random.choice(["Leftovers","Sitrus Berry","Quick Claw","Zoom Lens"]),weight=1014.13):
        color="blue"
        if move =="None":
            avmoves=["Protect","Ice Beam","Body Slam","Thunder Punch","Double-Edge","Hyper Beam","Giga Impact","Rest","Metronome","Darkest Lariat","Substitute","Sleep Talk","Belly Drum","Earthquake","Return"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves and "Sleep Talk" not in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Articuno
class Articuno(Pokemon2):
    "Articuno"
    def __init__(self,name="Articuno",type1="Ice",type2="Flying",nature="None",level=100,happiness=255,hp=90,atk=70,defense=100,spatk=95,spdef=125,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Snow Warning","Pressure","Snow Cloak"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","Bright Powder","Wacan Berry"]),weight=122.14):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Hidden Power","Ice Beam","Blizzard","Freeze-Dry","Brave Bird","Sky Attack","Roost","Tailwind","Triple Axel","Hurricane","Extrasensory","Rest","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Zapdos
class Zapdos(Pokemon2):
    "Zapdos"
    def __init__(self,name="Zapdos",type1="Electric",type2="Flying",nature="None",level=100,happiness=255,hp=90,atk=90,defense=85,spatk=125,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Lightning Rod","Static","Pressure","Defiant"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","Life Orb","Focus Band","Bright Powder","King's Rock","Sharp Beak","Choice Scarf"]),weight=115.96):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Hidden Power","Thunder","Brave Bird","Thunderbolt","Sky Attack","Roost","Thunder Wave","Bolt Beak","Razor Wind","Heat Wave","Tailwind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)             
#Moltres
class Moltres(Pokemon2):
    "Moltres"
    def __init__(self,name="Moltres",type1="Fire",type2="Flying",nature="None",level=100,happiness=255,hp=90,atk=100,defense=90,spatk=125,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flame Body","Pressure"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","King's Rock","Bright Powder"]),weight=132.28):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Hidden Power","Flamethrower","Hurricane","Heat Wave","Sky Attack","Brave Bird","Fire Blast","Roost","Solar Beam","Will-O-Wisp","Scorching Sands","Mystical Fire","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Baxcalibur
class Baxcalibur (Pokemon2):
    def __init__(self,name="Baxcalibur",type1="Ice",type2="Dragon",nature="None",level=100,happiness=255,hp=115,atk=145,defense=92,spatk=75,spdef=86,speed=87,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Ice Body","Thermal Exchange"]),item=random.choice(["Weakness Policy","Leftovers","Choice Band","Heavy-Duty Boots"]),weight=462.97):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Ice Beam","Icicle Crash","Dragon Claw","Double-Edge","Thunder Wave","Mountain Gale","Snowscape","Icicle Spear","Dragon Dance","Earthquake","Ice Shard"]  
            moves=moveset(type1,type2,avmoves,3,name=name)+["Glaive Rush"]          
        else:
            moves=move
        if "Icicle Spear" in moves:
            item="Loaded Dice"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev,ability=ability,item=item,weight=weight,color=color)
#Dragonite
class Dragonite(Pokemon2):
    def __init__(self,name="Dragonite",type1="Dragon",type2="Flying",nature="None",level=100,happiness=255,hp=91,atk=134,defense=95,spatk=100,spdef=100,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Multiscale","Inner Focus"]),item=random.choice(["Weakness Policy","Leftovers","Choice Band","Heavy-Duty Boots","Yache Berry","Lum Berry","Liechi Berry","Focus Sash","Bright Powder"]),weight=462.97):
        color="yellow"
        if move =="None":
            ch=1
            if ch==1:
                avmoves=["Protect","Ice Beam","Hydro Pump","Thunderbolt","Surf","Dragon Claw","Double-Edge","Thunder Wave","Dual Wingbeat","Roost","Extreme Speed","Scale Shot","Dragon Dance","Dragon Hammer","Hurricane","Dragon Rush","Stone Edge","Ice Punch","Fire Punch","Draco Meteor","Outrage","Razor Wind"]
                moves=moveset(type1,type2,avmoves,name=name)
            if ch==2:
                moves=["Swords Dance","Extreme Speed","Dragon Claw","Roost"]
        else:
            moves=move
        if "Outrage" in moves:
            item="Persim Berry"
        if "Dragon Rush" in moves:
            item="Wide Lens"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
            
#Mewtwo
class Mewtwo(Pokemon2):
    "Mewtwo"
    def __init__(self,name="Mewtwo",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=106,atk=110,defense=90,spatk=154,spdef=90,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Pressure","Unnerve"]),item=random.choice(["Expert Belt","Life Orb","Mewtwonite X","Mewtwonite Y","Berserk Gene"]),weight=268.96):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Hidden Power","Shadow Ball","Dark Pulse","Ice Beam","Focus Blast","Expanding Force","Aura Sphere","Power Gem","Earth Power","Future Sight"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Psystrike"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
        

#Mew
class Mew(Pokemon2):
    "Mew"
    def __init__(self,name="Mew",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Synchronize",item="Leftovers",weight=8.82):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Shadow Ball","Hidden Power","Transform","Psychic","Focus Blast","Aura Sphere","Swords Dance","Zen Headbutt","Sucker Punch","Ice Punch","Razor Wind","Dark Pulse"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)


#Meganium
class Meganium(Pokemon2):
    "Meganium"
    def __init__(self,name="Meganium",type1="Grass",type2="Fairy",nature="None",level=100,happiness=255,hp=80,atk=62,defense=110,spatk=93,spdef=110,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Triage","Overgrow","Filter"]),item=random.choice(["Leftovers"]),weight=221.56):
        color="green"
        if move =="None":
            avmoves=["Protect","Hidden Power","Leaf Storm","Moonblast","Dazzling Gleam","Synthesis","Leech Seed","Solar Beam","Frenzy Plant","Light Screen","Draining Kiss","Ancient Power","Toxic"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Giga Drain"]
        else:
            moves=move
        if "Light Screen" in moves:
            item="Light Clay"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Typhlosion
class Typhlosion(Pokemon2):
    "Typhlosion"
    def __init__(self,name="Typhlosion",type1="Fire",type2="None",nature="None",level=100,happiness=255,hp=78,atk=79,defense=73,spatk=124,spdef=80,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Blaze","Blazing Soul","Adaptability"]),item=random.choice(["Choice Specs","Charcoal","Wide Lens","Shuca Berry"]),weight=175.27):
        color="blue"
        if move =="None":
            avmoves=["Protect","Hidden Power","Earth Power","Fire Blast","Lava Plume","Eruption","Focus Blast","Blast Burn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Feraligatr
class Feraligatr(Pokemon2):
    "Feraligatr"
    def __init__(self,name="Feraligatr",type1="Water",type2="Dark",nature="None",level=100,happiness=255,hp=85,atk=110,defense=100,spatk=79,spdef=83,speed=78,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sheer Force","Torrent","Strong Jaw","Intimidate"]),item=random.choice(["Choice Band","Life Orb","King's Rock","Wacan Berry"]),weight=195.77):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Ice Beam","Hydro Pump","Liquidation","Dragon Claw","Hydro Cannon","Ice Fang","Jaw Lock","Dragon Dance","Swords Dance","Scale Shot","Power-up Punch","Substitute","Razor Wind","Aqua Fang"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Vaporeon
class Vaporeon(Pokemon2):
    "Vaporeon"
    def __init__(self,name="Vaporeon",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=130,atk=65,defense=60,spatk=110,spdef=95,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move="None", ability="Water Absorb",item=random.choice(["Leftovers","Heavy-Duty Boots","Rindo Berry"]),weight=63.93):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Acid Armor","Surf","Rain Dance","Flip Turn","Chilling Water","Calm Mind","Aqua Ring","Rain Dance","Aurora Beam","Heal Bell","Scald"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rain Dance" in moves:
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                   
#Jolteon
class Jolteon(Pokemon2):
    "Jolteon"
    def __init__(self,name="Jolteon",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=65,atk=65,defense=60,spatk=110,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Volt Absorb","Quick Feet"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","Air Balloon","Shuca Berry","Sitrus Berry","Razor Claw","Bright Powder"]),weight=54.01):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Hidden Power","Volt Switch","Thunder","Thunderbolt","Shadow Ball","Thunder Wave","Calm Mind","Substitute","Signal Beam","Wish","Yawn","Iron Tail"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Boltund
class Boltund(Pokemon2):
    def __init__(self,name="Boltund",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=69,atk=100,defense=60,spatk=80,spdef=60,speed=121,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Strong Jaw","Competitive"]),item=random.choice(["Choice Band","Heavy-Duty Boots","Expert Belt"]),weight=75):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Volt Switch","Play Rough","Thunder Fang","Wild Charge","Thunder Wave","Psychic Fangs","Crunch","Bolt Strike"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)               
#Flareon
class Flareon(Pokemon2):
    "Flareon"
    def __init__(self,name="Flareon",type1="Fire",type2="None",nature="None",level=100,happiness=255,hp=65,atk=130,defense=65,spatk=60,spdef=95,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Guts"]),item=random.choice(["Heavy-Duty Boots","Salac Berry","Quick Claw","Charcoal"]),weight=55.12):
        color="red"
        if move =="None":
            avmoves=["Protect","Flare Blitz","Fire Blast","Flame Charge","Last Resort","Will-O-Wisp","Calm Mind","Sacred Fire","Gunk Shot","Flail","Yawn","Superpower","Overheat","Fire Spin"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Overheat" in moves:
            item="White Herb"
        if ability=="Guts":
            item="Toxic Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Crobat
class Crobat(Pokemon2):
    "Crobat"
    def __init__(self,name="Crobat",type1="Poison",type2="Flying",nature="None",level=100,happiness=255,hp=75,atk=110,defense=75,spatk=90,spdef=75,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Infiltrator","Sniper","Inner Focus"]),item=random.choice(["Black Sludge","Heavy-Duty Boots","Payapa Berry","Sitrus Berry","Red Card","King's Rock","Sharp Beak"]),weight=165.35):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Poison Jab","Cross Poison","Dual Wingbeat","Brave Bird","U-turn","Poison Fang","Acrobatics","Tailwind","Heat Wave","Super Fang","Toxic","Taunt","Zen Headbutt","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Zen Headbutt" in moves:
            item="Psychic Gem"
        if ability=="Sniper":
            item="Scope Lens"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
#Lanturn
class Lanturn(Pokemon2):
    "Lanturn"
    def __init__(self,name="Lanturn",type1="Water",type2="Electric",nature="None",level=100,happiness=255,hp=125,atk=58,defense=88,spatk=76,spdef=106,speed=67,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Volt Absorb","Water Absorb"]),item=random.choice(["Leftovers","Sitrus Berry","Wide Lens","Rindo Berry","Quick Claw"]),weight=49.60):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Rain Dance","Flip Turn","Volt Switch","Thunder Wave","Toxic","Scald"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Parabolic Charge"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Ampharos
class Ampharos(Pokemon2):
    "Amoharos"
    def __init__(self,name="Ampharos",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=90,atk=75,defense=85,spatk=115,spdef=90,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move="None", ability="Static",item=random.choice(["Life Orb","Leftovers","Ampharosite","Sitrus Berry","Shuca Berry","Petaya Berry","Expert Belt","Zoom Lens"]),weight=135.58):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Hidden Power","Signal Beam","Power Gem","Thunderbolt","Discharge","Thunder Wave","Focus Blast","Light Screen","Reflect","Dragon Pulse","Cotton Guard","Fire Punch","Thunder Punch","Brick Break","Bulldoze","Thunder","Rest"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Reflect" in moves:
            item="Light Clay"
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)               
      
#Azumarill
class Azumarill(Pokemon2):
    "Azumarill"
    def __init__(self,name="Azumarill",type1="Water",type2="Fairy",nature="None",level=100,happiness=255,hp=110,atk=80,defense=80,spatk=80,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Huge Power","Thick Fat"]),item=random.choice(["Choice Band","Sitrus Berry","Assault Vest"]),weight=62.83):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Ice Beam","Play Rough","Liquidation","Belly Drum","Superpower","Ice Spinner","Chilling Water","Ice Punch","Perish Song","Substitute","Brick Break","Aqua Tail","Superpower"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Aqua Jet"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Politoed
class Politoed(Pokemon2):
    "Politoed"
    def __init__(self,name="Politoed",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=90,atk=75,defense=75,spatk=90,spdef=100,speed=70,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Drizzle","Damp","Water Absorb"]),item=random.choice(["Choice Specs","Water Gem","Wide Lens","Quick Claw","Bright Powder","Lax Incense"]),weight=74.74):
        color="green"
        if move =="None":
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Flip Turn","Focus Blast","Metronome","Scald","Hypnosis","Perish Song","Bounce"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Drizzle":
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
#Espeon
class Espeon(Pokemon2):
    "Espeon"
    def __init__(self,name="Espeon",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=70,atk=65,defense=60,spatk=130,spdef=95,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Magic Bounce","Synchronize"]),item=random.choice(["Leftovers","Petaya Berry","Lum Berry","Bright Powder"]),weight=58.42):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Hidden Power","Shadow Ball","Dazzling Gleam","Morning Sun","Light Screen","Calm Mind","Fiery Dance","Future Sight","Substitute","Yawn","Reflect","Signal Beam"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Psychic"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Meowstic
class Meowstic(Pokemon2):
    def __init__(self,name="Meowstic",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=74,atk=48,defense=76,spatk=63,spdef=81,speed=104,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Feline Prowess","Infiltrator","Prankster"]),item="Leftovers",weight=18.74):
        color="blue"
        if move =="None":
            avmoves=["Protect","Hidden Power","Psychic","Shadow Ball","Dazzling Gleam","Morning Sun","Light Screen","Future Sight"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Sylveon
class Sylveon (Pokemon2):
    def __init__(self,name="Sylveon",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=95,atk=65,defense=65,spatk=110,spdef=130,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Cute Charm","Pixilate"]),item=random.choice(["Leftovers","Pixie Plate"]),weight=51.81):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Hidden Power","Moonblast","Hyper Voice","Dazzling Gleam","Mystical Fire","Heal Bell","Calm Mind","Psyshock","Misty Explosion","Hyper Beam","Wish","Shadow Ball"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Hyper Voice" in moves:
            item="Throat Spray"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                 
#Umbreon
class Umbreon(Pokemon2):
    "Umbreon"
    def __init__(self,name="Umbreon",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=95,atk=70,defense=110,spatk=70,spdef=130,speed=55,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability="Inner Focus",item=random.choice(["Leftovers","Bright Powder","Scope Lens"]),weight=59.52):
        color="Yellow"
        if move =="None":
            avmoves=["Protect","Hidden Power","Foul Play","Shadow Ball","Dark Pulse","Moonlight","Toxic","Calm Mind","Thunder Wave","Wish"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Steelix
class Steelix(Pokemon2):
    "Steelix"
    def __init__(self,name="Steelix",type1="Steel",type2="Ground",nature="None",level=100,happiness=255,hp=75,atk=85,defense=200,spatk=55,spdef=65,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Rock Head",item=random.choice(["Leftovers","Steelixite","Occa Berry","Passho Berry","Salac Berry","Steel Gem","Rindo Berry","Rocky Helmet","Quick Claw","Metal Coat"]),weight=881.85):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Iron Tail","Gyro Ball","Earthquake","Stone Edge","Rock Slide","Toxic","Body Press","Stealth Rock","Autotomize","Head Smash","Dig","Sandstorm","Curse","Roar"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
     
#Scizor
class Scizor(Pokemon2):
    "Scizor"
    def __init__(self,name="Scizor",type1="Bug",type2="Steel",nature="None",level=100,happiness=255,hp=70,atk=130,defense=100,spatk=55,spdef=80,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Technician","Swarm","Light Metal"]),item=random.choice(["Life Orb","Assault Vest","Leftovers","Scizorite","Occa Berry","Sitrus Berry","Shell Bell","Bright Powder"]),weight=260.15):
        color="red"
        if move =="None":
            avmoves=["Protect","Iron Head","Bullet Punch","X-Scissor","U-turn","Roost","Superpower","Swords Dance","Double Team","Aerial Ace","Acrobatics","Razor Wind","Trailblaze"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
                               
#Heracross
class Heracross(Pokemon2):
    "Heracross"
    def __init__(self,name="Heracross",type1="Bug",type2="Fighting",nature="None",level=100,happiness=255,hp=80,atk=125,defense=75,spatk=40,spdef=95,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Guts","Moxie","Swarm"]),item=random.choice(["Coba Berry","Heracronite","Salac Berry","Choice Band","Choice Scarf","Focus Band","Leftovers","Bug Gem"]),weight=119.05):
        color="blue"
        if move =="None":
            avmoves=["Protect","Brick Break","X-Scissor","U-turn","Close Combat","Superpower","Substitute","Stone Edge","Swords Dance","Aerial Ace","Shadow Claw","Focus Punch","Curse","Rest","Seismic Toss","Rock Slide","Facade","Night Slash","Feint","Pin Missile","Rock Blast","Spikes"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Megahorn"]
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                                   
#Skarmory
class Skarmory(Pokemon2):
    "Skarmory"
    def __init__(self,name="Skarmory",type1="Steel",type2="Flying",nature="None",level=100,happiness=255,hp=65,atk=80,defense=140,spatk=40,spdef=70,speed=70,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sturdy","Weak Armor"]),item=random.choice(["Leftovers","Rocky Helmet","Salac Berry","Wacan Berry","Life Orb"]),weight=111.33):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Roost","Brave Bird","Stealth Rock","Whirlwind","Steel Wing","Body Press","Spikes","Toxic","Swords Dance","Curse","Aerial Ace","Roar"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            #Houndoom
class Houndoom(Pokemon2):
    "Houndoom"
    def __init__(self,name="Houndoom",type1="Dark",type2="Fire",nature="None",level=100,happiness=255,hp=75,atk=95,defense=50,spatk=110,spdef=80,speed=105,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Intimidate","Unnerve"]),item=random.choice(["Life Orb","Houndoominite","Passho Berry","Petaya Berry","Focus Sash"]),weight=77.16):
        color="red"
        if move =="None":
            avmoves=["Protect","Fire Blast","Dark Pulse","Flamethrower","Inferno","Crunch","Will-O-Wisp","Nasty Plot","Fiery Wrath","Overheat","Sucker Punch","Counter","Roar","Thunder Fang"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Overheat" in moves:
            item="White Herb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                                  
#Kingdra
class Kingdra(Pokemon2):
    "Kingdra"
    def __init__(self,name="Kingdra",type1="Water",type2="Dragon",nature="None",level=100,happiness=255,hp=75,atk=85,defense=95,spatk=105,spdef=95,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Swift Swim","Sniper","Damp"]),item=random.choice(["Life Orb","Haban Berry","Scope Lens","Lum Berry","Wide Lens"]),weight=335.10):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Dragon Pulse","Ice Beam","Surf","Thunder","Hydro Pump","Dragon Dance","Rain Dance","Flip Turn","Scale Shot","Snipe Shot","Yawn","Agility","Rest","Flash Cannon","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Tatsugiri
class Tatsugiri(Pokemon2):
    def __init__(self,name="Tatsugiri",type1="Dragon",type2="Water",nature="None",level=100,happiness=255,hp=68,atk=50,defense=60,spatk=120,spdef=95,speed=82,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Commander","Storm Drain"]),item=random.choice(["Choice Specs","Leftovers"]),weight=17.64):
        color=random.choice(["red","magenta","yellow"])
        if move =="None":
            avmoves=["Protect","Dragon Pulse","Ice Beam","Surf","Thunder","Hydro Pump","Dragon Dance","Rain Dance","Flip Turn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                             
#Tyranitar
class Tyranitar(Pokemon2):
    "Tyranitar"
    def __init__(self,name="Tyranitar",type1="Rock",type2="Dark",nature="None",level=100,happiness=255,hp=100,atk=134,defense=110,spatk=95,spdef=100,speed=61,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sand Stream","Battle Armor","Unnerve"]),item=random.choice(["Chople Berry","Weakness Policy","Tyranitarite","Passho Berry","King's Rock","Expert Belt","Quick Claw","Focus Sash"]),weight=445.33):
        color="green"
        if move =="None":
            avmoves=["Protect","Crunch","Earthquake","Stone Edge","Rock Slide","Hyper Beam","Dragon Dance","Giga Impact","Stealth Rock","Substitute"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if name=="Tyranitar":
            ch=random.randint(1,5)
            if ch==5:
                moves=["Earthquake","Stone Edge","Crunch","Ice Punch"]
                maxiv="Ghost"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Tyranitar
class UTyranitar(Pokemon2):
    def __init__(self,name="Ultimate Tyranitar",type1="Steel",type2="Dark",nature="None",level=100,happiness=255,hp=90,atk=144,defense=120,spatk=75,spdef=110,speed=71,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Filter",item=random.choice(["Chople Berry"]),weight=100):
        if move =="None":
            avmoves=["Protect","Crunch","Earthquake","Stone Edge","Iron Head","Steel Beam","Dragon Dance","Iron Tail","Stealth Rock","Flamethrower","Smart Strike"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)        
     
#Raikou
class Raikou(Pokemon2):
    "Raikou"
    def __init__(self,name="Raikou",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=90,atk=85,defense=75,spatk=115,spdef=100,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Inner Focus","Pressure"]),item=random.choice(["Leftovers","Heavy-Duty Boots","Air Balloon","Shuca Berry","Magnet","Lax Incense","Wise Glasses"]),weight=392.42):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Crunch","Thunder","Thunderbolt","Wild Charge","Hyper Beam","Rain Dance","Thunder Wave","Extreme Speed","Reflect","Weather Ball","Hidden Power","Calm Mind","Aura Sphere"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Entei
class Entei(Pokemon2):
    "Entei"
    def __init__(self,name="Entei",type1="Fire",type2="None",nature="None",level=100,happiness=255,hp=115,atk=115,defense=85,spatk=90,spdef=75,speed=100,hpev=0,atkev=115,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Inner Focus","Pressure"]),item=random.choice(["Choice Band","Heavy-Duty Boots","Wise Glasses","Leftovers"]),weight=436.52):
        color="red"
        if move =="None":
            avmoves=["Protect","Crunch","Fire Blast","Sacred Fire","Flamethrower","Hyper Beam","Flare Blitz","Eruption","Extreme Speed","Sunny Day","Extrasensory"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sunny Day" in moves:
            item="Heat Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Suicune
class Suicune(Pokemon2):
    "Suicune"
    def __init__(self,name="Suicune",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=100,atk=75,defense=115,spatk=90,spdef=115,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Inner Focus","Pressure"]),item=random.choice(["Leftovers","Wacan Berry","Never Melt Ice"]),weight=412.26):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance","Scald","Extreme Speed","Light Screen","Tailwind","Rest","Ice Beam","Blizzard","Extrasensory","Aurora Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Lugia
class Lugia(Pokemon2):
    "Lugia"
    def __init__(self,name="Lugia",type1="Psychic",type2="Flying",nature="None",level=100,happiness=255,hp=106,atk=90,defense=130,spatk=90,spdef=154,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Multiscale","Pressure"]),item=random.choice(["Choice Specs","Heavy-Duty Boots"]),weight=476.20):
        if move =="None":
            avmoves=["Protect","Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance","Aeroblast","Psychic","Extrasensory","Esper Wing","Future Sight"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)            
#Ho-Oh
class Hooh(Pokemon2):
    "Ho-Oh"
    def __init__(self,name="Ho-Oh",type1="Fire",type2="Flying",nature="None",level=100,happiness=255,hp=106,atk=130,defense=90,spatk=110,spdef=154,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Regenerator","Pressure","Phoenix Down"]),item=random.choice(["Choice Specs","Heavy-Duty Boots"]),weight=438.72):
        color="red"
        if move =="None":
            avmoves=["Protect","Recover","Hyper Beam","Sunny Day","Sacred Fire","Fire Blast","Flamethrower","Brave Bird","Heat Wave","Sky Attack","Future Sight"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                     
#Celebi
class Celebi(Pokemon2):
    "Celebi"
    def __init__(self,name="Celebi",type1="Grass",type2="Psychic",nature="None",level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Natural Cure",item=random.choice(["Leftovers","Occa Berry"]),weight=11.02):
        color="green"
        if move =="None":
            avmoves=["Protect","Recover","Psychic","Leaf Storm","Future Sight","Perish Song","Shadow Ball"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Blissey
class Blissey(Pokemon2):
    "Blissey"
    def __init__(self,name="Blissey",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=255,atk=10,defense=10,spatk=75,spdef=135,speed=55,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=4,speedev=0,maxiv="No",move="None", ability="Natural Cure",item="Leftovers",weight=103.18):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Soft-Boiled","Toxic","Seismic Toss","Light Screen","Reflect","Stealth Rock","Minimize","Flamethrower","Grass Knot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Deoxys
class Deoxys(Pokemon2):
    "Deoxys"
    def __init__(self,name="Deoxys",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=50,atk=150,defense=50,spatk=150,spdef=50,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Pressure",item="Kasib Berry",weight=134.04):
        color="red"
        if move =="None":
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Ice Beam","Fire Punch","Low Kick","Reflect","Light Screen","Knock Off","Extreme Speed","Superpower"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Reflect" in moves or "Light Screen" in moves:
            item="Light Clay"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Attack Deoxys
class ADeoxys(Pokemon2):
    "Attack Deoxys"
    def __init__(self,name="Attack Deoxys",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=50,atk=180,defense=20,spatk=180,spdef=20,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Pressure",item=random.choice(["Life Orb","Focus Sash"]),weight=134.04):
        color="red"
        if move =="None":
            avmoves=["Protect","Psycho Boost","Psychic","Shadow Ball","Dark Pulse","Ice Beam","Superpower","Thunder","Extreme Speed","Hidden Power","Spikes","Stealth Rock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Speed Deoxys
class SDeoxys(Pokemon2):
    "Speed Deoxys"
    def __init__(self,name="Speed Deoxys",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=50,atk=95,defense=90,spatk=95,spdef=90,speed=180,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Pressure",item=random.choice(["Leftovers","Lum Berry","Focus Sash","Colbur Berry","Choice Scarf","Expert Belt","Rocky Helmet"]),weight=134.04):
        color="red"
        if move =="None":
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave","Toxic Spikes","Stealth Rock","Extreme Speed","Double Team","Hidden Power","Superpower","Trick","Taunt","Thunderbolt","Reflect","Mirror Coat","Light Screen","Low Kick","Skill Swap"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Reflect" in moves or "Light Screen" in moves:
            item="Light Clay"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
#Defense Deoxys
class DDeoxys(Pokemon2):
    "Defense Deoxys"
    def __init__(self,name="Defense Deoxys",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=50,atk=70,defense=160,spatk=70,spdef=160,speed=90,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=4,maxiv="No",move="None", ability="Pressure",item=random.choice(["Leftovers","Rocky Helmet"]),weight=134.04):
        color="red"
        if move =="None":
            avmoves=["Protect","Psycho Boost","Toxic","Psychic","Shadow Ball","Dark Pulse","Recover","Thunder Wave","Toxic Spikes","Stealth Rock","Spikes","Taunt","Ice Beam","Night Shade","Thunder","Knock Off","Skill Swap"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Thunder" in moves:
            item="Electric Gem"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            
#Jirachi       
class Jirachi(Pokemon2):
    "Jirachi"
    def __init__(self,name="Jirachi",type1="Steel",type2="Psychic",nature="None",level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Serene Grace",item="Leftovers",weight=2.43):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Recover","Psychic","Future Sight","Flash Cannon","Shadow Ball","Rest","Meteor Beam","Meteor Mash","Future Sight","Substitute","Wish"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Doom Desire"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Rayquaza     
class Rayquaza(Pokemon2):
    "Rayquaza"
    def __init__(self,name="Rayquaza",type1="Dragon",type2="Flying",nature="None",level=100,happiness=255,hp=105,atk=150,defense=90,spatk=150,spdef=90,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Air Lock",item=random.choice(["Life Orb","Charti Berry"]),weight=455.25):
        color="green"
        if move =="None":
            avmoves=["Protect","Crunch","Hyper Beam","Dragon Dance","Extreme Speed","Draco Meteor","Meteor Beam"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Dragon Ascent"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
          
#Arboliva
class Arboliva(Pokemon2):
    def __init__(self,name="Arboliva",type1="Grass",type2="Normal",nature="None",level=100,happiness=255,hp=78,atk=69,defense=90,spatk=125,spdef=109,speed=39,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Seed Sower","Harvest"]),item=random.choice(["Life Orb","Occa Berry","Sitrus Berry"]),weight=106.26):
        color="green"
        if move =="None":
            avmoves=["Protect","Leaf Storm","Focus Blast","Energy Ball","Seed Bomb","Petal Dance","Leech Seed","Dazzling Gleam","Strength Sap"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
        
#Sceptile
class Sceptile(Pokemon2):
    "Sceptile"
    def __init__(self,name="Sceptile",type1="Grass",type2="Dragon",nature="None",level=100,happiness=255,hp=70,atk=105,defense=65,spatk=85,spdef=86,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Overgrow","Unburden"]),item=random.choice(["Life Orb","Sceptile","Occa Berry","Scope Lens"]),weight=115.08):
        color="green"
        if move =="None":
            avmoves=["Protect","Leaf Blade","Hyper Beam","Leaf Storm","Dragon Dance","Dragon Pulse","Draco Meteor","Focus Blast","Energy Ball","Frenzy Plant","Scale Shot","Substitute","Double Team","Razor Wind","Night Slash","Earthquake","Swords Dance"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
      
#Blaziken
class Blaziken(Pokemon2):
    "Blaziken"
    def __init__(self,name="Blaziken",type1="Fire",type2="Fighting",nature="None",level=100,happiness=255,hp=80,atk=130,defense=70,spatk=100,spdef=70,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Speed Boost","Striker","Blaze","Sheer Force"]),item=random.choice(["Life Orb","Focus Sash","Blazikenite","Salac Berry","Air Balloon","Shell Bell","Passho Berry"]),weight=114.64):
        color="red"
        if move =="None":
            avmoves=["Protect","Overheat","High Jump Kick","Sky Uppercut","Blaze Kick","Brave Bird","Flare Blitz","Focus Blast","Blast Burn","Triple Arrows","Bulk Up","Sky Uppercut","Stone Edge","Flame Charge","Earthquake"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Quaquaval
class Quaquaval(Pokemon2):
    def __init__(self,name="Quaquaval",type1="Water",type2="Fighting",nature="None",level=100,happiness=255,hp=85,atk=120,defense=80,spatk=85,spdef=75,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Moxie","Torrent"]),item=random.choice(["Life Orb","Focus Sash"]),weight=136.47):
        color="blue"
        if move =="None":
            avmoves=["Protect","Hydro Pump","High Jump Kick","Aqua Jet","Brave Bird","Liquidation","Focus Blast","Hydro Cannon"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Aqua Step"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                    
                                   
#Swampert
class Swampert(Pokemon2):
    "Swampert"
    def __init__(self,name="Swampert",type1="Water",type2="Ground",nature="None",level=100,happiness=255,hp=100,atk=110,defense=90,spatk=85,spdef=90,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Torrent","Damp","Swift Swim"]),item=random.choice(["Leftovers","Swampertite","Rindo Berry","Quick Claw","Expert Belt","Shell Bell"]),weight=180.56):
        color="blue"
        if move =="None":
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Power-up Punch","Waterfall","Ice Punch","Hydro Cannon","Stealth Rock","Focus Blast","Muddy Water","Earth Power","Ice Beam","Ancient Power"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                                                     
#Ludicolo
class Ludicolo(Pokemon2):
    "Ludicolo"
    def __init__(self,name="Ludicolo",type1="Grass",type2="Water",nature="None",level=100,happiness=255,hp=80,atk=70,defense=90,spatk=110,spdef=100,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Swift Swim","Dancer","Rain Dish"]),item=random.choice(["Life Orb","Leftovers","Lum Berry"]),weight=121.25):
        color="green"
        if move =="None":
            avmoves=["Protect","Ice Beam","Giga Drain","Surf","Hydro Pump","Rain Dance","Focus Blast","Energy Ball","Weather Ball","Aurora Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            
        #Shiftry
class Shiftry(Pokemon2):
    "Shiftry"
    def __init__(self,name="Shiftry",type1="Grass",type2="Dark",nature="None",level=100,happiness=255,hp=90,atk=100,defense=60,spatk=110,spdef=60,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Infiltrator","Flare Boost"]),item=random.choice(["Life Orb","Dark Gem"]),weight=131.4):
        color="red"
        if move =="None":
            avmoves=["Protect","Sunny Day","Giga Drain","Leaf Storm","Hurricane","Leaf Tornado","Leech Seed","Focus Blast","Explosion","Parting Shot","Sucker Punch","Weather Ball","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Flare Boost":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            #Swellow
class Swellow(Pokemon2):
    "Swellow"
    def __init__(self,name="Swellow",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=60,atk=85,defense=70,spatk=100,spdef=65,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Guts","Aerilate","Scrappy"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","Flying Gem","Liechi Berry"]),weight=43.65):
        color="blue"
        if move =="None":
            avmoves=["Protect","Roost","Brave Bird","Facade","Hurricane","Boomburst","Double Team","Endeavor","Aerial Ace","Heat Wave","U-turn","Air Slash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
#Pelipper
class Pelipper(Pokemon2):
    "Pelipper"
    def __init__(self,name="Pelipper",type1="Water",type2="Flying",nature="None",level=100,happiness=255,hp=65,atk=35,defense=100,spatk=100,spdef=80,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Drizzle",item=random.choice(["Heavy-Duty Boots","Damp Rock","Petaya Berry"]),weight=61.73):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Roost","Surf","Ice Beam","Hurricane","Hydro Pump","Scald","Chilling Water","Air Slash","Weather Ball","Tailwind","U-turn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Drizzle":
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Gardevoir
class Gardevoir(Pokemon2):
    "Gardevoir"
    def __init__(self,name="Gardevoir",type1="Psychic",type2="Fairy",nature="None",level=100,happiness=255,hp=68,atk=65,defense=65,spatk=125,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Trace","Telepathy","Synchronize"]),item=random.choice(["Choice Specs","Life Orb","Leftovers","Choice Scarf","Gardevoirite","Lum Berry","Bright Powder"]),weight=106.70):
        color="green"
        if move =="None":
            avmoves=["Protect","Recover","Dazzling Gleam","Moonblast","Shadow Ball","Focus Blast","Trick Room","Misty Terrain","Aura Sphere","Thunderbolt","Calm Mind","Will-O-Wisp","Destiny Bond","Heal Bell","Pain Split","Protect","Signal Beam","Psyshock","Trick","Hyper Voice","Mystical Fire","Light Screen","Future Sight","Double Team","Rest"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Psychic"]
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
          
#Breloom
class Breloom(Pokemon2):
    "Breloom"
    def __init__(self,name="Breloom",type1="Grass",type2="Fighting",nature="None",level=100,happiness=255,hp=60,atk=130,defense=80,spatk=60,spdef=60,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Poison Heal",item=random.choice(["Toxic Orb","Coba Berry","Focus Sash","Shell Bell","Life Orb"]),weight=86.42):
        color="green"
        if move =="None":
            avmoves=["Protect","Dynamic Punch","Mach Punch","Spore","Sky Uppercut","Bullet Seed","Seed Bomb","Leech Seed","Superpower","Gunk Shot","Close Combat","Substitute","Focus Punch","Stone Edge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)            
#Slaking
class Slaking(Pokemon2):
    "Slaking"
    def __init__(self,name="Slaking",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=150,atk=160,defense=100,spatk=95,spdef=65,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Truant",item=random.choice(["Leftovers","Sitrus Berry","Eject Button","Choice Band"]),truant=False,weight=287.70):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Dynamic Punch","Hyper Beam","Double-Edge","Sky Uppercut","Return","Slack Off","Rest","Yawn","Body Slam","Play Rough","Earthquake","Hammer Arm","Giga Impact","Night Slash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        self.truant=truant
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Vigoroth
class Vigoroth(Pokemon2):
    def __init__(self,name="Vigoroth",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=80,atk=80,defense=80,spatk=55,spdef=55,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Vital Spirit",item="Eviolite",weight=102.51):
        color="red"
        if move =="None":
            avmoves=["Protect","Double-Edge","Sky Uppercut","Return","Slack Off","Rest","Yawn","Slash","Throat Chop","Play Rough","Body Slam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                 
#Hariyama
class Hariyama(Pokemon2):
    "Hariyama"
    def __init__(self,name="Hariyama",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=144,atk=120,defense=80,spatk=40,spdef=80,speed=50,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Guts","Thick Fat","Sheer Force"]),item=random.choice(["Sitrus Berry","Bright Powder","Leftovers","Salac Berry","Quick Claw"]),weight=559.53):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Dynamic Punch","Force Palm","Sky Uppercut","Arm Thrust","Belly Drum","Knock Off","Facade","Cross Chop","Drain Punch","Headlong Rush","Smelling Salts","Earthquake","Bulk Up","Bullet Punch","Rest","Stone Edge","Sand-Attack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
  
#Tinkaton
class Tinkaton(Pokemon2):
    def __init__(self,name="Tinkaton",type1="Fairy",type2="Steel",nature="None",level=100,happiness=255,hp=85,atk=75,defense=77,spatk=70,spdef=105,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Mold Breaker",item=random.choice(["Leftovers","Air Balloon"]),weight=248.68):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Iron Head","Play Rough","Crunch","Sucker Punch","Iron Defense","Draining Kiss","Fake Out","Knock Off","Skitter Smack"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Gigaton Hammer"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                
        
#Aggron
class Aggron(Pokemon2):
    "Aggron"
    def __init__(self,name="Aggron",type1="Steel",type2="Rock",nature="None",level=100,happiness=255,hp=70,atk=110,defense=180,spatk=60,spdef=60,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Rock Head","Sturdy","Heavy Metal"]),item=random.choice(["Choice Band","Leftovers","Aggronite","Custap Berry","Chople Berry","Focus Sash","Air Balloon","Quick Claw"]),weight=793.66):
        if move =="None":
            avmoves=["Protect","Iron Head","Stone Edge","Crunch","Earthquake","Iron Defense","Hyper Beam","Flash Cannon","Body Press","Stealth Rock","Autotomize","Heavy Slam","Outrage","Thunder Wave","Avalanche","Dragon Rush","Fire Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    

#Medicham        
class Medicham (Pokemon2):
    "Medicham"
    def __init__(self,name="Medicham",type1="Fighting",type2="Psychic",nature="None",level=100,happiness=255,hp=60,atk=80,defense=75,spatk=60,spdef=75,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Pure Power",item=random.choice(["Leftovers","Medichamite","Psychic Gem","Kasib Berry""Choice Scarf","Focus Band","Bright Powder"]),weight=69.45):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Dynamic Punch","Thunder Punch","Psycho Cut","Fire Punch","Zen Headbutt","Ice Punch","High Jump Kick","Close Combat","Axe Kick","Bullet Punch","Bulk Up","Brick Break","Trailblaze"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Torkoal       
class Torkoal (Pokemon2):
    "Torkoal"
    def __init__(self,name="Torkoal",type1="Fire",type2="None",nature="None",level=100,happiness=255,hp=90,atk=75,defense=140,spatk=95,spdef=80,speed=20,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Drought","White Smoke","Shell Armor"]),item=random.choice(["Leftovers","Heat Rock","Fire Gem"]),weight=177.25):
        color="red"
        if move =="None":
            avmoves=["Protect","Lava Plume","Thunder Wave","Flamethrower","Toxic","Stealth Rock","Explosion","Earth Power","Yawn","Shell Smash","Heat Wave","Solar Beam","Gyro Ball","Fire Spin"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                       
       
#Sharpedo
class Sharpedo(Pokemon2):
    "Sharpedo"
    def __init__(self,name="Sharpedo",type1="Water",type2="Dark",nature="None",level=100,happiness=255,hp=70,atk=120,defense=40,spatk=95,spdef=40,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Speed Boost","Rough Skin"]),item=random.choice(["Life Orb","Sharpedonite","Focus Sash"]),weight=195.77):
        color="blue"
        if move =="None":
            avmoves=["Protect","Flip Turn","Hydro Pump","Crunch","Ice Beam","Surf","Dark Pulse","Scale Shot","Zen Headbutt","Aqua Jet","Aqua Fang","Night Slash","Ice Fang","Psychic Fangs","Waterfall"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
#Overqwil
class Overqwil(Pokemon2):
    "Overqwil"
    def __init__(self,name="Overqwil",type1="Dark",type2="Poison",nature="None",level=100,happiness=255,hp=85,atk=115,defense=95,spatk=65,spdef=65,speed=85,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Intimidate","Swift Swim","Poison Point"]),item="Black Sludge",weight=133.4):
        color="blue"
        if move =="None":
            avmoves=["Protect","Flip Turn","Pin Missile","Crunch","Poison Jab","Dark Pulse","Double-Edge","Toxic Spikes","Stealth Rock","Chilling Water","Scale Shot","Minimize","Explosion"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Barb Barrage"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
         
#Wailord
class Wailord(Pokemon2):
    "Wailord"
    def __init__(self,name="Wailord",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=170,atk=90,defense=70,spatk=105,spdef=100,speed=30,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Blubber Defense","Oblivious","Pressure","Regenerator"]),item=random.choice(["Leftovers","Sitrus Berry","Choice Scarf","Wacan Berry","Quick Claw","Mystic Water"]),weight=877.44):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Water Spout","Hydro Pump","Blizzard","Ice Beam","Surf","Rain Dance","Heavy Slam","Rest","Explosion","Hydro Cannon","Aqua Ring","Avalanche","Amnesia","Bounce","Fissure","Soak","Whirlpool"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                

#Camerupt
class Camerupt(Pokemon2):
    "Camerupt"
    def __init__(self,name="Camerupt",type1="Fire",type2="Ground",nature="None",level=100,happiness=255,hp=90,atk=100,defense=70,spatk=105,spdef=75,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Solid Rock","Anger Point","Magma Armor"]),item=random.choice(["Leftovers","Camerupite","Passho Berry","Shuca Berry"]),weight=485.02):
        color="red"
        if move =="None":
            avmoves=["Protect","Eruption","Earth Power","Lava Plume","Earthquake","Stone Edge","Fire Blast","Will-O-Wisp","Stealth Rock","Magnitude","Bulldoze","Yawn","Magma Storm","Steam Eruption","Fissure","Explosion"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Arbok
class Arbok(Pokemon2):
    "Arbok"
    def __init__(self,name="Arbok",type1="Poison",type2="Dark",nature="None",level=100,happiness=255,hp=75,atk=105,defense=75,spatk=65,spdef=80,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Strong Jaw","Shed Skin","Unnerve"]),item=random.choice(["Black Sludge","Shuca Berry"]),weight=143.3):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Venoshock","Earth Power","Poison Fang","Crunch","Gunk Shot","Belch","Jaw Lock","Glare","Sucker Punch","Poison Jab","Thunder Fang","Ice Fang","Fire Fang","Acid Spray","Coil","Haze","Iron Tail","Dig","Earthquake","Double Team","Rock Tomb","Dark Pulse","Rock Slide","Bulldoze","Shed Tail","Dragon Tail"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Regirock
class Regirock(Pokemon2):
    "Regirock"
    def __init__(self,name="Regirock",type1="Rock",type2="None",nature="None",level=100,happiness=255,hp=80,atk=100,defense=200,spatk=50,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Clear Body","Solid Rock","Lithogen","Sturdy"]),item=random.choice(["Leftovers","Passho Berry","Quick Claw"]),weight=507.06):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Zap Cannon","Earth Power","Hyper Beam","Earthquake","Stone Edge","Rock Slide","Explosion","Stealth Rock","Meteor Beam","Iron Defense","Superpower","Lock-On","Ancient Power","Strength","Brick Break","Sandstorm"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sandstorm" in moves:
            item="Smooth Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)      
#Regice
class Regice(Pokemon2):
    "Regice"
    def __init__(self,name="Regice",type1="Ice",type2="None",nature="None",level=100,happiness=255,hp=80,atk=50,defense=100,spatk=100,spdef=200,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Clear Body","Thermal Exchange","Ice Body"]),item=random.choice(["Leftovers","Shell Bell","Ganlon Berry"]),weight=385.81):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Ice Beam","Blizzard","Freeze-Dry","Hyper Beam","Zap Cannon","Snowscape","Explosion","Focus Blast","Thunderbolt","Amnesia","Icy Wind","Lock-On","Rock Polish","Focus Blast","Giga Impact","Rest"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Registeel
class Registeel(Pokemon2):
    "Registeel"
    def __init__(self,name="Registeel",type1="Steel",type2="None",nature="None",level=100,happiness=255,hp=80,atk=75,defense=150,spatk=75,spdef=150,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Clear Body","Filter","Steely Spirit","Light Metal"]),item=random.choice(["Leftovers","Occa Berry","Quick Claw"]),weight=451.95):
        if move =="None":
            avmoves=["Protect","Iron Head","Flash Cannon","Zap Cannon","Earthquake","Hyper Beam","Curse","Explosion","Double Iron Bash","Rest","Lock-On","Substitute","Focus Blast","Toxic","Thunder","Stealth Rock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)   
#Dewgong
class Dewgong(Pokemon2):
    "Dewgong"
    def __init__(self,name="Dewgong",type1="Water",type2="Ice",nature="None",level=100,happiness=255,hp=105,atk=50,defense=90,spatk=100,spdef=105,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Thick Fat","Ice Scales","Ice Body"]),item=random.choice(["Leftovers","Wacan Berry","Sitrus Berry","Lum Berry","Life Orb","Razor Fang"]),weight=264.55):
        if move =="None":
            avmoves=["Protect","Hidden Power","Ice Beam","Hydro Pump","Thunderbolt","Surf","Snowscape","Rain Dance","Frost Breath","Aurora Veil","Ice Shard","Sheer Cold","Signal Beam","Frost Breath","Perish Song","Fake Out","Drill Run","Aqua Jet","Rest","Aurora Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)       
#Jynx
class Jynx(Pokemon2):
    "Jynx"
    def __init__(self,name="Jynx",type1="Ice",type2="Psychic",nature="None",level=100,happiness=255,hp=75,atk=40,defense=35,spatk=125,spdef=95,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Dry Skin","Hydration","Anticipation"]),item=random.choice(["Leftovers","Salac Berry","Psychic Gem","Bright Powder","Wise Glasses"]),weight=89.51):
        color="red"
        if move =="None":
            avmoves=["Protect","Hidden Power","Ice Beam","Psychic","Blizzard","Dark Pulse","Hail","Shadow Ball","Trick Room","Light Screen","Expanding Force","Draining Kiss","Triple Axel","Freezing Glare","Psycho Boost","Psystrike","Avalanche","Lovely Kiss","Perish Song","Future Sight","Frost Breath","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Mamoswine
class Mamoswine(Pokemon2):
    "Mamoswine"
    def __init__(self,name="Mamoswine",type1="Ice",type2="Ground",nature="None",level=100,happiness=255,hp=110,atk=130,defense=80,spatk=70,spdef=60,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Thick Fat","Snow Cloak","Oblivious"]),item=random.choice(["Leftovers","Choice Scarf","Ice Gem","Liechi Berry","Focus Sash","Salac Berry","Bright Powder"]),weight=641.55):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Ice Beam","Earthquake","Blizzard","Stone Edge","Hail","Icicle Crash","Stealth Rock","Snowscape","Headlong Rush","Mountain Gale","Ice Shard","Double-Edge","Bulldoze","Rock Tomb","Superpower","Endeavor","Icicle Spear","Fissure"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#
#Flygon
class Flygon(Pokemon2):
    "Flygon"
    def __init__(self,name="Flygon",type1="Ground",type2="Dragon",nature="None",level=100,happiness=255,hp=90,atk=110,defense=85,spatk=130,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Tinted Lens","Levitate","Compound Eyes"]),item=random.choice(["Leftovers","Lum Berry","Yache Berry","Liechi Berry","Wide Lens","Power Herb","Soft Sand"]),weight=180.78):
        color="green"
        if move =="None":
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Stone Edge","Superpower","Sandstorm","Scale Shot","First Impression","Headlong Rush","Bug Buzz","Earth Power","Dragon Pulse","Dig","Outrage","Flamethrower","Fire Blast","Draco Meteor","U-turn","Solar Beam","Sunny Day"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sunny Day" in moves:
            item="Heat Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   

#Altaria
class Altaria(Pokemon2):
    "Altaria"
    def __init__(self,name="Altaria",type1="Dragon",type2="Flying",nature="None",level=100,happiness=255,hp=75,atk=85,defense=90,spatk=90,spdef=105,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Natural Cure","Cloud Nine"]),item=random.choice(["Leftovers","Altarianite","Apicot Berry","Power Herb","Petaya Berry","Dragon Fang"]),weight=45.42):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Dragon Claw","Earthquake","Crunch","Brave Bird","Sky Attack","Moonblast","Perish Song","Air Slash","Dragon Pulse","Cotton Guard","Outrage","Fire Blast","Perish Song","Dragon Dance","Draco Meteor"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Fire Blast" in moves:
            item="Fire Gem"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
                  
#Zangoose
class Zangoose(Pokemon2):
    "Zangoose"
    def __init__(self,name="Zangoose",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=73,atk=115,defense=70,spatk=60,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Toxic Boost","Tough Claws","Immunity"]),item=random.choice(["Life Orb","Salac Berry","Chople Berry","Liechi Berry"]),weight=88.85):
        if move =="None":
            avmoves=["Protect","Crush Claw","Slash","Crunch","X-Scissor","Facade","Close Combat","Swords Dance","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Toxic Boost":
            item="Toxic Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)          
#Seviper
class Seviper(Pokemon2):
    "Seviper"
    def __init__(self,name="Seviper",type1="Poison",type2="Dark",nature="None",level=100,happiness=255,hp=73,atk=110,defense=83,spatk=90,spdef=83,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Shed Skin","Merciless","Fatal Precision","Intimidate"]),item=random.choice(["Black Sludge","Shuca Berry"]),weight=115.74):
        color="blue"
        if move =="None":
            avmoves=["Protect","Poison Fang","Poison Tail","Crunch","Poison Jab","Toxic","Sludge Bomb","Gunk Shot","Sucker Punch","Night Slash","Dragon Tail","Sludge Wave","Glare","Dark Pulse"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Exploud
class Exploud(Pokemon2):
    "Exploud"
    def __init__(self,name="Exploud",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=104,atk=70,defense=63,spatk=120,spdef=63,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Scrappy","Punk Rock","Soundproof"]),item=random.choice(["Throat Spray","Petaya Berry","Expert Belt","Focus Band","Quick Claw"]),weight=185.19):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Boomburst","Hyper Beam","Crunch","Hyper Voice","Toxic","Double-Edge","Rest","Overdrive","Fire Blast","Focus Blast","Ice Beam","Blizzard"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            #Lunatone
class Lunatone(Pokemon2):
    "Lunatone"
    def __init__(self,name="Lunatone",type1="Rock",type2="Ghost",nature="None",level=100,happiness=255,hp=90,atk=55,defense=95,spatk=95,spdef=115,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Levitate",item=random.choice(["Leftovers","Petaya Berry","Expert Belt"]),weight=370.38):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Moonblast","Stone Edge","Moonlight","Explosion","Trick Room","Stealth Rock","Meteor Beam","Photon Geyser","Future Sight","Ice Beam","Signal Beam","Grass Knot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Solrock
class Solrock(Pokemon2):
    "Solrock"
    def __init__(self,name="Solrock",type1="Rock",type2="Fire",nature="None",level=100,happiness=255,hp=70,atk=45,defense=65,spatk=150,spdef=65,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Levitate",item=random.choice(["Leftovers","Liechi Berry","Passho Berry"]),weight=339.51):
        color="red"
        if move =="None":
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Moonblast","Stone Edge","Morning Sun","Explosion","Trick Room","Solar Beam","Stealth Rock","Meteor Beam","Blast Burn","Fire Blast","Flamethrower","Zen Headbutt","Fire Spin"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
#Whiscash
class Whiscash(Pokemon2):
    "Whiscash"
    def __init__(self,name="Whiscash",type1="Water",type2="Ground",nature="None",level=100,happiness=255,hp=115,atk=85,defense=73,spatk=80,spdef=71,speed=60,hpev=0,atkev=252,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Oblivious","Anticipation","Adaptability"]),item=random.choice(["Leftovers","Rindo Berry","Zoom Lens"]),weight=52.03):
        color="blue"
        if move =="None":
            avmoves=["Protect","Ancient Power","Ice Beam","Surf","Power Gem","Hydro Pump","Stone Edge","Earthquake","Rest","Magnitude","Future Sight","Fissure","Dragon Dance","Discharge","Waterfall","Blizzard","Rain Dance","Icy Wind","Muddy Water","Whirlpool"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        if "Rain Dance" in moves:
            item="Damp Rock "
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Dondozo
class Dondozo(Pokemon2):
    def __init__(self,name="Dondozo",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=150,atk=100,defense=115,spatk=65,spdef=65,speed=35,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Unaware","Oblivious"]),item=random.choice(["Leftovers","Heavy-Duty Boots","Rocky Helmet"]),weight=485.02):
        color="blue"
        if move =="None":
            avmoves=["Protect","Rock Slide","Earthquake","Rest","Wave Crash","Heavy Slam","Body Press","Yawn","Curse","Liquidation"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Order Up"]
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Crawdaunt
class Crawdaunt(Pokemon2):
    "Crawdaunt"
    def __init__(self,name="Crawdaunt",type1="Water",type2="Dark",nature="None",level=100,happiness=255,hp=83,atk=120,defense=95,spatk=90,spdef=80,speed=55,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Adaptability","Shell Armor"]),item=random.choice(["Leftovers","Focus Sash","Wacan Berry","Life Orb","Choice Scarf"]),weight=72.31):
        color="red"
        if move =="None":
            avmoves=["Protect","Ancient Power","Ice Beam","Surf","Power Gem","Hydro Pump","Crabhammer","Liquidation","Knock Off","Brick Break","Superpower","Dragon Dance","Guillotine","Night Slash","Crunch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)               
#Claydol
class Claydol(Pokemon2):
    "Claydol"
    def __init__(self,name="Claydol",type1="Ground",type2="Psychic",nature="None",level=100,happiness=255,hp=70,atk=70,defense=105,spatk=90,spdef=120,speed=75,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Levitate",item=random.choice(["Leftovers","Ganlon Berry","Sitrus Berry","Kasib Berry","Hard Stone","Wise Glasses","Quick Claw"]),weight=238.10):
        color="red"
        if move =="None":
            avmoves=["Protect","Ancient Power","Hyper Beam","Psychic","Power Gem","Earth Power","Stone Edge","Explosion","Trick Room","Stealth Rock","Light Screen","Shore Up","Cosmic Power","Ice Beam","Rock Slide"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Cradily
class Cradily(Pokemon2):
    "Cradily"
    def __init__(self,name="Cradily",type1="Rock",type2="Grass",nature="None",level=100,happiness=255,hp=111,atk=61,defense=107,spatk=91,spdef=107,speed=43,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Storm Drain",item=random.choice(["Leftovers","Sitrus Berry","Expert Belt","Lum Berry"]),weight=133.16):
        color="green"
        if move =="None":
            avmoves=["Protect","Ancient Power","Hyper Beam","Giga Drain","Sludge Bomb","Earth Power","Leech Seed","Energy Ball","Stealth Rock","Meteor Beam","Hidden Power","Power Gem","Amnesia","Toxic","Rock Slide","Earthquake"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Armaldo
class Armaldo(Pokemon2):
    "Armaldo"
    def __init__(self,name="Armaldo",type1="Rock",type2="Bug",nature="None",level=100,happiness=255,hp=75,atk=125,defense=100,spatk=70,spdef=80,speed=70,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Swift Swim","Battle Armor"]),item=random.choice(["Leftovers","Liechi Berry","Quick Claw","Lum Berry","White Herb","Wide Lens"]),weight=150.36):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Ancient Power","Hyper Beam","X-Scissor","Rock Blast","Earth Power","Crush Claw","Stealth Rock","Meteor Beam","Curse","Aqua Tail","Swords Dance","Earthquake","Stone Edge","Rock Polish","Toxic"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Milotic
class Milotic(Pokemon2):
    "Milotic"
    def __init__(self,name="Milotic",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=95,atk=60,defense=84,spatk=100,spdef=125,speed=86,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Competitive","Marvel Scale","Cute Charm","Filter"]),item=random.choice(["Leftovers","Lum Berry","Rocky Helmet","Salac Berry","Shell Bell"]),weight=357.15):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Recover","Ice Beam","Surf","Rain Dance","Hydro Pump","Coil","Thunderbolt","Light Screen","Scale Shot","Aqua Ring","Icy Wind","Rest","Scald"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Marvel Scale":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Dudunsparce
class Dudunsparce (Pokemon2):
    def __init__(self,name="Dudunsparce",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=125,atk=100,defense=80,spatk=85,spdef=75,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Serene Grace","Rattled"]),item=random.choice(["Leftovers","Apicot Berry"]),weight=86.42):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Roost","Hypnosis","Shadow Ball","Trick Room","Light Screen","Reflect","Giga Impact","Body Slam","Yawn","Scale Shot","Glare","Skitter Smack","Dig","Rock Slide","Coil"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Hyper Drill"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Cyclizar
class Cyclizar(Pokemon2):
    def __init__(self,name="Cyclizar",type1="Dragon",type2="Normal",nature="None",level=100,happiness=255,hp=70,atk=95,defense=65,spatk=85,spdef=65,speed=121,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Regenerator","Shed Skin"]),item="Leftovers",weight=138.89):
        color="green"
        if move =="None":
            avmoves=["Protect","Shadow Ball","Light Screen","Reflect","Giga Impact","Body Slam"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Shed Tail"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                 
#Farigarif
class Farigiraf(Pokemon2):
    "Farigarif"
    def __init__(self,name="Farigiraf",type1="Normal",type2="Psychic",nature="None",level=100,happiness=255,hp=120,atk=90,defense=70,spatk=110,spdef=70,speed=85,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Armor Tail",item=random.choice(["Leftovers","Safety Googles","Sitrus Berry","Colbur Berry"]),weight=352.74):
        color="red"
        if move =="None":
            avmoves=["Protect","Recover","Psychic","Crunch","Zen Headbutt","Assurance","Hypnosis","Shadow Ball","Trick Room","Light Screen","Reflect","Hyper Voice","Psyshock","Dazzling Gleam","Boomburst","Future Sight","Razor Wind"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Twin Beam"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Banette
class Banette(Pokemon2):
    "Banette"
    def __init__(self,name="Banette",type1="Ghost",type2="None",nature="None",level=100,happiness=255,hp=64,atk=115,defense=65,spatk=73,spdef=63,speed=65,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Insomnia","Frisk","Cursed Body"]),item=random.choice(["Leftovers","Banettite","Liechi Berry","Ghost Gem","Sticky Barb"]),weight=27.56):
        if move =="None":
            avmoves=["Protect","Recover","Knock Off","Crunch","Phantom Force","Assurance","Hypnosis","Shadow Ball","Toxic","Thunder Wave","Will-O-Wisp","Destiny Bond","Double-Edge","Shadow Sneak","Shadow Claw","Gunk Shot","Destiny Bond","Sucker Punch","Trick","Curse","Sucker Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)          
  
#Absol
class Absol(Pokemon2):
    "Absol"
    def __init__(self,name="Absol",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=75,atk=130,defense=70,spatk=85,spdef=70,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Super Luck","Justified","Pressure"]),item=random.choice(["Life Orb","Choice Band","Black Glasses","Scope Lens","Dread Plate","Absolite","Salac Berry","Bright Powder","Lum Berry"]),weight=103.62):
        color="blue"
        if move =="None":
            avmoves=["Protect","Recover","Knock Off","Crunch","Psycho Cut","Assurance","Shadow Ball","Toxic","Sucker Punch","Close Combat","Swords Dance","Play Rough","Iron Tail","Perish Song","Future Sight","Double Team","Substitute","Aerial Ace"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Night Slash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         

                                    
#Glalie
class Glalie(Pokemon2):
    "Glalie"
    def __init__(self,name="Glalie",type1="Ice",type2="Rock",nature="None",level=100,happiness=255,hp=80,atk=80,defense=80,spatk=100,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Inner Focus","Moody","Refrigerate"]),item=random.choice(["Focus Sash","Glalitite","Scope Lens"]),weight=565.49):
        if move =="None":
            avmoves=["Protect","Recover","Earthquake","Crunch","Ice Beam","Blizzard","Freeze-Dry","Ice Fang","Toxic","Snowscape","Hyper Beam","Rain Dance","Shadow Ball","Double Team","Rock Blast","Gyro Ball"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Gyro Ball" in moves:
            item="Iron Ball"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
        #Walrein
class Walrein(Pokemon2):
    "Walrein"
    def __init__(self,name="Walrein",type1="Ice",type2="Water",nature="None",level=100,happiness=255,hp=110,atk=80,defense=95,spatk=105,spdef=95,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Thick Fat","Ice Body","Fur Coat","Regenerator"]),item=random.choice(["Leftovers","Heavy-Duty Boots","Salac Berry","Sitrus Berry","Expert Belt","Quick Claw","Bright Powder"]),weight=332.02):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Slack Off","Surf","Crunch","Ice Beam","Blizzard","Freeze-Dry","Ice Fang","Rest","Snowscape","Hyper Beam","Earthquake","Icicle Spear","Iron Head","Swords Dance","Liquidation","Frost Breath","Yawn","Super Fang","Aqua Ring","Sheer Cold","Toxic","Aurora Beam","Roar"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Huntail
class Huntail(Pokemon2):
    "Huntail"
    def __init__(self,name="Huntail",type1="Water",type2="Dark",nature="None",level=100,happiness=255,hp=95,atk=114,defense=105,spatk=94,spdef=75,speed=52,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Intimidate","Defiant","Moxie","Water Veil"]),item=random.choice(["Leftovers","White Herb","Liechi Berry"]),weight=59.52):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Crunch","Ice Beam","Blizzard","Liquidation","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Aqua Fang","Scald","Confuse Ray"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Shell Smash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Gorebyss
class Gorebyss(Pokemon2):
    "Gorebyss"
    def __init__(self,name="Gorebyss",type1="Water",type2="Fairy",nature="None",level=100,happiness=255,hp=55,atk=84,defense=105,spatk=114,spdef=75,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Regenerator","Dazzling","Swift Swim","Water Absorb"]),item=random.choice(["Leftovers","White Herb","Petaya Berry"]),weight=49.82):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Dazzling Gleam","Ice Beam","Blizzard","Moonblast","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Draining Kiss","Psychic","Icy Wind"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Shell Smash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Relicanth
class Relicanth(Pokemon2):
    "Relicanth"
    def __init__(self,name="Relicanth",type1="Water",type2="Rock",nature="None",level=100,happiness=255,hp=100,atk=105,defense=130,spatk=45,spdef=65,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Rock Head",item=random.choice(["Leftovers","Rock Gem","Rindo Berry","Ganlon Berry","Liechi Berry"]),weight=51.59):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Liquidation","Ice Beam","Stone Edge","Rock Slide","Ice Fang","Waterfall","Hydro Pump","Rain Dance","Head Smash","Stealth Rock","Meteor Beam","Skull Bash","Scale Shot","Yawn","Rock Polish","Amnesia"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rain Dance" in moves:
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Salamence
class Salamence(Pokemon2):
    "Salamence"
    def __init__(self,name="Salamence",type1="Dragon",type2="Flying",nature="None",level=100,happiness=255,hp=95,atk=135,defense=80,spatk=110,spdef=80,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Moxie"]),item=random.choice(["Life Orb","Heavy-Duty Boots","Salamencite","Yache Berry","Petaya Berry","Dragon Gem","White Herb","Expert Belt","Cheri Berry","King's Rock"]),weight=226.19):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Stone Edge","Dragon Claw","Flamethrower","Crunch","Zen Headbutt","Double-Edge","Fire Blast","Earthquake","Dragon Dance","Roost","Thunder Fang","Hydro Pump","Heat Wave","Draco Meteor","Outrage","Rock Slide","Tailwind","Hyper Voice"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if name=="Salamence":
            ch=random.randint(1,5)
            if ch==5:
                moves=["Dragon Claw","Hurricane","Dual Wingbeat","Earthquake"]
                maxiv="Steel"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Metagross
class Metagross(Pokemon2):
    "Metagross"
    def __init__(self,name="Metagross",type1="Steel",type2="Psychic",nature="None",level=100,happiness=255,hp=80,atk=135,defense=130,spatk=95,spdef=90,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Clear Body","Light Metal"]),item=random.choice(["Leftovers","Choice Band","Metagrossite","Occa Berry","Liechi Berry","Expert Belt","Air Balloon","Quick Claw"]),weight=1212.54):
        color="blue"
        if move =="None":
            avmoves=["Protect","Stone Edge","Bullet Punch","Meteor Mash","Hyper Beam","Crunch","Zen Headbutt","Double-Edge","Iron Defense","Earthquake","Hammer Arm","Flash Cannon","Stealth Rock","Meteor Beam","Psyshield Bash","Explosion"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Latias
class Latias(Pokemon2):
    "Latias"
    def __init__(self,name="Latias",type1="Dragon",type2="Psychic",nature="None",level=100,happiness=255,hp=80,atk=80,defense=90,spatk=110,spdef=130,speed=110,hpev=252,atkev=0,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Levitate",item=random.choice(["Soul Dew","Leftovers","Choice Specs","Choice Scarf","Latiasite","Yache Berry","Colbur Berry","Lum Berry","Bright Powder"]),weight=88.18):
        color="red"
        if move =="None":
            avmoves=["Protect","Hyper Beam","Mist Ball","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball","Psyshock","Roost","Thunder","Thunder Wave","Reflect","Light Screen","Draco Meteor","Energy Ball","Recover"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Reflect" in moves or "Light Screen" in moves:
            item="Light Clay"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Latios
class Latios(Pokemon2):
    "Latios"
    def __init__(self,name="Latios",type1="Dragon",type2="Psychic",nature="None",level=100,happiness=255,hp=80,atk=90,defense=80,spatk=130,spdef=110,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Levitate",item=random.choice(["Choice Scarf","Choice Specs","Soul Dew","Latiosite","Lum Berry","Expert Belt","Haban Berry"]),weight=132.28):
        color="blue"
        if move =="None":
            avmoves=["Protect","Hyper Beam","Luster Purge","Zen Headbutt","Dragon Pulse","Psychic","Calm Mind","Ice Beam","Thunderbolt","Shadow Ball","Draco Meteor","Dragon Dance","Recover","Dragon Claw","Shadow Claw","Tailwind","Psyshock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Draco Meteor" in moves:
            item="White Herb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
    
#Kyogre
class Kyogre(Pokemon2):
    "Kyogre"
    def __init__(self,name="Kyogre",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=100,atk=100,defense=90,spatk=150,spdef=140,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Drizzle",item=random.choice(["Choice Scarf","Choice Specs","Leftovers","Blue Orb"]),weight=776.03):
        color="blue"
        if move =="None":
            avmoves=["Protect","Hyper Beam","Origin Pulse","Thunder","Water Spout","Ancient Power","Calm Mind","Ice Beam","Thunderbolt","Rest","Thunder Wave"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                         
#Groudon
class Groudon(Pokemon2):
    "Groudon"
    def __init__(self,name="Groudon",type1="Ground",type2="None",nature="None",level=100,happiness=255,hp=100,atk=150,defense=140,spatk=100,spdef=90,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Drought",item=random.choice(["Choice Band","Leftovers","Lum Berry","Life Orb","Red Orb","Salac Berry"]),weight=2094.39):
        color="red"
        if move =="None":
            avmoves=["Protect","Hyper Beam","Precipice Blades","Earthquake","Eruption","Ancient Power","Swords Dance","Fire Blast","Fire Punch","Rest","Thunder Wave","Solar Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Torterra
class Torterra(Pokemon2):
    "Torterra"
    def __init__(self,name="Torterra",type1="Grass",type2="Ground",nature="None",level=100,happiness=255,hp=95,atk=109,defense=105,spatk=75,spdef=85,speed=56,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Overgrow","Rock Head","Shell Armor"]),item=random.choice(["Choice Band","Leftovers","Yache Berry","Bright Powder"]),weight=683.43):
        color="green"
        if move =="None":
            avmoves=["Protect","Hyper Beam","Wood Hammer","Earthquake","Leaf Storm","Ancient Power","Swords Dance","Curse","Synthesis","Crunch","Giga Drain","Headlong Rush","Frenzy Plant","Stealth Rock","Head Smash","Outrage","Stone Edge","Sunny Day"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sunny Day" in moves:
            item="Heat Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
#Infernape
class Infernape(Pokemon2):
    "Infernape"
    def __init__(self,name="Infernape",type1="Fire",type2="Fighting",nature="None",level=100,happiness=255,hp=76,atk=110,defense=71,spatk=110,spdef=71,speed=113,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Blaze","Iron Fist"]),item=random.choice(["Choice Band","Focus Sash","Expert Belt","Life Orb","Fire Gem","Coba Berry","Wise Glasses"]),weight=121.25):
        color="red"
        if move =="None":
            avmoves=["Protect","Hyper Beam","Flare Blitz","Close Combat","Fire Blast","Mach Punch","Swords Dance","Power-up Punch","Overheat","Calm Mind","Flamethrower","Blast Burn","Stealth Rock","Raging Fury","Taunt","Slack Off","Thunder Punch","Pyro Ball","Dig","Bulk Up","Fire Punch","Fake Out"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Empoleon
class Empoleon(Pokemon2):
    "Empoleon"
    def __init__(self,name="Empoleon",type1="Water",type2="Steel",nature="None",level=100,happiness=255,hp=84,atk=86,defense=88,spatk=111,spdef=101,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Torrent","Competitive","Adaptability"]),item=random.choice(["Leftovers","Shuca Berry","Chople Berry","Petaya Berry"]),weight=186.29):
        color="blue"
        if move =="None":
            avmoves=["Protect","Hyper Beam","Surf","Flash Cannon","Hydro Pump","Liquidation","Wave Crash","Ice Beam","Steel Beam","Rest","Scald","Hydro Cannon","Stealth Rock","Substitute","Grass Knot","Feather Dance","Blizzard","Double Team"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Staraptor
class Staraptor(Pokemon2):
    "Staraptor"
    def __init__(self,name="Staraptor",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=85,atk=120,defense=70,spatk=50,spdef=60,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Reckless"]),item=random.choice(["Choice Scarf","Choice Band","Leftovers","King's Rock","Muscle Band","Eject Pack"]),weight=54.9):
        color="red"
        if move =="None":
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-turn","Giga Impact","Facade","Double-Edge","Double Team","Quick Attack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Final Gambit" in moves:
            hpev=252
            atkev=0
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Luxray
class Luxray(Pokemon2):
    "Luxray"
    def __init__(self,name="Luxray",type1="Electric",type2="Dark",nature="None",level=100,happiness=255,hp=80,atk=120,defense=79,spatk=95,spdef=79,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Guts"]),item=random.choice(["Life Orb","Shuca Berry","Liechi Berry","Expert Belt","Muscle Band"]),weight=92.59):
        color="blue"
        if move =="None":
            avmoves=["Protect","Wild Charge","Crunch","Thunder Wave","Play Rough","Electric Terrain","Sucker Punch","Volt Tackle","Zing Zap","Superpower","Fire Fang","Ice Fang","Quick Attack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Roserade
class Roserade(Pokemon2):
    "Roserade"
    def __init__(self,name="Roserade",type1="Grass",type2="Poison",nature="None",level=100,happiness=255,hp=60,atk=70,defense=65,spatk=125,spdef=105,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Technician","Poison Touch","Natural Cure"]),item=random.choice(["Heavy-Duty Boots","Black Sludge","Rocky Helmet","Lum Berry","Leftovers","Choice Scarf","White Herb","Big Root","Rose Incense","Miracle Seed"]),weight=31.97):
        color="green"
        if move =="None":
            avmoves=["Protect","Weather Ball","Toxic","Sunny Day","Giga Drain","Energy Ball","Toxic Spikes","Grassy Terrain","Flower Trick","Shadow Ball","Petal Dance","Substitute"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Rampardos
class Rampardos(Pokemon2):
    "Rampardos"
    def __init__(self,name="Rampardos",type1="Rock",type2="Dragon",nature="None",level=100,happiness=255,hp=97,atk=165,defense=40,spatk=65,spdef=40,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sheer Force","Mold Breaker","Rock Head"]),item=random.choice(["Choice Scarf","Choice Band","Life Orb","Salac Berry","Focus Sash","Persim Berry"]),weight=225.97):
        color="blue"
        if move =="None":
            avmoves=["Protect","Head Smash","Iron Head","Crunch","Stone Edge","Accelerock","Superpower","Zen Headbutt","Outrage","Earthquake","Avalanche","Dragon Rush","Thrash","Giga Impact"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
                                      
#Stonjourner
class Stonjourner(Pokemon2):
    def __init__(self,name="Stonjourner",type1="Rock",type2="None",nature="None",level=100,happiness=255,hp=100,atk=125,defense=135,spatk=20,spdef=50,speed=80,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Power Spot","Solid Rock"]),item=random.choice(["Leftovers","Choice Band","Hard Stone"]),weight=1146.4):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Stealth Rock","Heavy Slam","Rock Slide","Stone Edge","Rock Polish","Body Slam","Low Kick","Bulldoze","Heat Crash","Explosion","Earthquake"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Eiscue
class Eiscue(Pokemon2):
    def __init__(self,name="Eiscue",type1="Ice",type2="None",nature="None",level=100,happiness=255,hp=75,atk=100,defense=110,spatk=45,spdef=90,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Ice Face"]),item=random.choice(["Leftovers","Salac Berry"]),weight=196.2):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Ice Beam","Freeze-Dry","Weather Ball","Surf","Head Smash","Icy Wind","Amnesia"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                   
        
#Bastiodon
class Bastiodon(Pokemon2):
    "Bastiodon"
    def __init__(self,name="Bastiodon",type1="Rock",type2="Steel",nature="None",level=100,happiness=255,hp=70,atk=78,defense=168,spatk=47,spdef=138,speed=30,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sturdy","Dauntless Shield","Bulletproof","Solid Rock"]),item=random.choice(["Leftovers","Shuca Berry","Air Balloon","Muscle Band","Weakness Policy"]),weight=329.59):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Iron Defense","Iron Head","Crunch","Stone Edge","Heavy Slam","Fire Blast","Stealth Rock","Fire Blast","Behemoth Bash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            #Vespiquen
class Vespiquen(Pokemon2):
    "Vespiquen"
    def __init__(self,name="Vespiquen",type1="Bug",type2="Flying",nature="None",level=100,happiness=255,hp=85,atk=80,defense=102,spatk=80,spdef=102,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Pressure","Queenly Majesty","Intimidate"]),item=random.choice(["Leftovers","Apicot Berry","Wise Glasses"]),weight=84.88):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Defend Order","Attack Order","Heal Order","Toxic","Swagger","Power Gem","Destiny Bond","Pollen Puff","Roost"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Gastrodon
class Gastrodon(Pokemon2):
    "Gastrodon"
    def __init__(self,name="Gastrodon",type1="Water",type2="Ground",nature="None",level=100,happiness=255,hp=111,atk=83,defense=68,spatk=92,spdef=82,speed=39,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Storm Drain","Sand Force"]),item=random.choice(["Leftovers","Rindo Berry","Heavy-Duty Boots","Apicot Berry","Wiki Berry"]),weight=65.92):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Earth Power","Recover","Hydro Pump","Ice Beam","Stealth Rock","Light Screen","Reflect","Chilling Water","Yawn","Sludge Wave","Counter","Icy Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        name=random.choice(["East Sea ","West Sea "])+name
        if "East" in name:
            color="green"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Ambipom
class Ambipom(Pokemon2):
    "Ambipom"
    def __init__(self,name="Ambipom",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=75,atk=100,defense=66,spatk=60,spdef=66,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Skill Link","Technician"]),item=random.choice(["Leftovers","Life Orb","Flying Gem","Focus Sash","Normal Gem","Bright Powder"]),weight=44.75):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Toxic","Double Hit","U-turn","Return","Fake Out","Knock Off","Brick Break","Double-Edge","Acrobatics","Facade","Low Kick","Ice Punch","Fire Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                            
        #Drifblim
class Drifblim(Pokemon2):
    "Drifblim"
    def __init__(self,name="Drifblim",type1="Ghost",type2="Flying",nature="None",level=100,happiness=255,hp=150,atk=80,defense=44,spatk=90,spdef=54,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flare Boost","Unburden","Aftermath"]),item=random.choice(["Ghost Gem","Expert Belt","Wise Glasses"]),weight=33.07):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Psychic","Shadow Ball","Calm Mind","Thunderbolt","Explosion","Destiny Bond","Tailwind","Minimize","Acrobatics","Thunder","Sucker Punch","Icy Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Acrobatics" in moves:
            ability="Unburden"
            item="Flying Gem"
        if ability=="Flare Boost":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                                
#Mismagius
class Mismagius(Pokemon2):
    "Mismagius"
    def __init__(self,name="Mismagius",type1="Ghost",type2="Fairy",nature="None",level=100,happiness=255,hp=70,atk=65,defense=70,spatk=110,spdef=110,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Levitate",item=random.choice(["Leftovers","Kasib Berry","Salac Berry","Sitrus Berry","Colbur Berry","Spell Tag"]),weight=9.7):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Psychic","Shadow Ball","Calm Mind","Thunderbolt","Dazzling Gleam","Destiny Bond","Perish Song","Dark Pulse","Pain Split","Power Gem","Pain Split"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Purugly
class Purugly(Pokemon2):
    "Purugly"
    def __init__(self,name="Purugly",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=90,atk=102,defense=79,spatk=64,spdef=64,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Thick Fat","Defiant","Own Tempo"]),item=random.choice(["Silk Scarf","Life Orb"]),weight=96.56):
        if move =="None":
            avmoves=["Protect","Sucker Punch","Play Rough","Body Slam","Double-Edge","Bulk Up","Slack Off"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight) 
#Glameow
class Glameow(Pokemon2):
    def __init__(self,name="Glameow",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=49,atk=55,defense=42,spatk=42,spdef=37,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Thick Fat","Defiant","Own Tempo"]),item=random.choice(["Silk Scarf","Life Orb"]),weight=8.60):
        if move =="None":
            avmoves=["Protect","Sucker Punch","Play Rough","Body Slam","Double-Edge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)            
#Skuntank
class Skuntank(Pokemon2):
    "Skuntank"
    def __init__(self,name="Skuntank",type1="Poison",type2="Dark",nature="None",level=100,happiness=255,hp=103,atk=103,defense=67,spatk=91,spdef=61,speed=84,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Stench","Aftermath","Poison Touch"]),item=random.choice(["Rocky Helmet","Black Sludge","Black Glasses","Choice Band","Choice Scarf","Shuca Berry","Bright Powder"]),weight=83.78):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Dark Pulse","Shadow Ball","Flamethrower","Belch","Sludge Wave","Sludge Bomb","Nasty Plot","Fire Blast","Acid Spray"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Honchkrow
class Honchkrow(Pokemon2):
    "Honchkrow"
    def __init__(self,name="Honchkrow",type1="Dark",type2="Flying",nature="None",level=100,happiness=255,hp=100,atk=125,defense=60,spatk=105,spdef=60,speed=96,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Super Luck","Moxie","Insomnia","Prankster"]),item=random.choice(["Scope Lens","Heavy-Duty Boots","Salac Berry","Charti Berry","Choice Scarf","Dark Gem","Expert Belt","Sharp Beak"]),weight=60.19):
        color="blue"
        if move =="None":
            avmoves=["Protect","Night Slash","Shadow Ball","Drill Peck","Roost","Dark Pulse","Tailwind","Heat Wave","Sucker Punch","Perish Song","Icy Wind","Nasty Plot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Spiritomb
class Spiritomb(Pokemon2):
    "Spiritomb"
    def __init__(self,name="Spiritomb",type1="Ghost",type2="Dark",nature="None",level=100,happiness=255,hp=100,atk=92,defense=108,spatk=92,spdef=108,speed=35,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Pressure","Intimidate"]),item=random.choice(["Choice Band","Leftovers","Sitrus Berry","Rocky Helmet"]),weight=238.10):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Night Slash","Shadow Ball","Hypnosis","Nasty Plot","Dark Pulse","Destiny Bond","Calm Mind","Will-O-Wisp","Pain Split","Sucker Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Whimsicott
class Whimsicott(Pokemon2):
    def __init__(self,name="Whimsicott",type1="Grass",type2="Fairy",nature="None",level=100,happiness=255,hp=60,atk=67,defense=85,spatk=77,spdef=75,speed=115,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Prankster",item=random.choice(["Leftovers","Occa Berry","Mental Herb"]),weight=14.55):
        color="green"
        if move =="None":
            avmoves=["Protect","Cotton Guard","Hurricane","Moonblast","Energy Ball","Giga Drain","Tailwind","Encore","Substitute"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Tailwind"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
#Garchomp
class Garchomp(Pokemon2):
    "Garchomp"
    def __init__(self,name="Garchomp",type1="Dragon",type2="Ground",nature="None",level=100,happiness=255,hp=108,atk=130,defense=95,spatk=80,spdef=85,speed=102,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Rough Skin","Sand Veil"]),item=random.choice(["Life Orb","Yache Berry","Leftovers","Rocky Helmet","Garchompite","Salac Berry","Choice Scarf","Focus Sash","Bright Powder"]),weight=209.44):
        color="blue"
        if move =="None":
            avmoves=["Protect","Swords Dance","Earthquake","Dragon Claw","Stone Edge","Draco Meteor","Flamethrower","Stealth Rock","Dual Chop","Roar","Scale Shot","Fire Blast","Dig","Aqua Tail","Brick Break","Outrage","Rock Slide","Fire Fang"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
#Lucario
class Lucario(Pokemon2):
    "Lucario"
    def __init__(self,name="Lucario",type1="Fighting",type2="Steel",nature="None",level=100,happiness=255,hp=70,atk=110,defense=70,spatk=115,spdef=70,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Inner Focus","Steadfast"]),item=random.choice(["Choice Band","Life Orb","Lucarionite","Liechi Berry","Focus Sash","Bright Powder","Scope Lens","Razor Fang","Salac Berry"]),weight=119.05):
        color="blue"
        if move =="None":
            avmoves=["Protect","Meteor Mash","Aura Sphere","Dragon Pulse","Close Combat","Bullet Punch","Bone Rush","Extreme Speed","Steel Beam","Cross Chop","Swords Dance","Crunch","Ice Punch","Dark Pulse","Psychic"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Hippowdon
class Hippowdon(Pokemon2):
    "Hippowdon"
    def __init__(self,name="Hippowdon",type1="Ground",type2="None",nature="None",level=100,happiness=255,hp=108,atk=112,defense=118,spatk=68,spdef=72,speed=47,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Sand Stream",item=random.choice(["Leftovers","Rocky Helmet","Passho Berry","Quick Claw"]),weight=661.39):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Earthquake","Slack Off","Stone Edge","Knock Off","Stealth Rock","Yawn","Roar","Dig","Ice Fang"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Drapion
class Drapion(Pokemon2):
    "Drapion"
    def __init__(self,name="Drapion",type1="Poison",type2="Dark",nature="None",level=100,happiness=255,hp=70,atk=100,defense=110,spatk=60,spdef=75,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Sniper",item=random.choice(["Shuca Berry","Choice Band","Black Sludge","Sitrus Berry","Scope Lens","Rawst Berry"]),weight=135.58):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Wicked Blow","Cross Poison","Swords Dance","Knock Off","Crunch","Toxic Spikes","Fire Fang","Acupressure","Night Slash","Ice Fang"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Toxicroak
class Toxicroak(Pokemon2):
    "Toxicroak"
    def __init__(self,name="Toxicroak",type1="Poison",type2="Fighting",nature="None",level=100,happiness=255,hp=83,atk=106,defense=65,spatk=86,spdef=65,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Dry Skin","Poison Touch","Swift Swim","Anticipation"]),item=random.choice(["Choice Band","Life Orb","Payapa Berry","Focus Sash","Scope Lens"]),weight=97.89):
        color="blue"
        if move =="None":
            avmoves=["Protect","Close Combat","Cross Poison","Swords Dance","Knock Off","Venoshock","Poison Jab","Sucker Punch","Drain Punch","Bulk Up","Substitute","X-Scissor","Giga Impact","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                       
#Abomasnow
class Abomasnow(Pokemon2):
    "Abomasnow"
    def __init__(self,name="Abomasnow",type1="Grass",type2="Ice",nature="None",level=100,happiness=255,hp=90,atk=92,defense=75,spatk=92,spdef=85,speed=60,hpev=220,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=36,maxiv="No",move="None", ability=random.choice(["Snow Warning","Soundproof"]),item=random.choice(["Leftovers","Focus Sash","Babiri Berry","Icy Rock","Abomasite","Occa Berry","Scope Lens","Zoom Lens"]),weight=298.73):
        if move =="None":
            a=random.randint(1,2)
            if a==1:
                avmoves=["Protect","Wood Hammer","Icicle Crash","Blizzard","Ice Shard","Energy Ball","Earth Power","Aurora Veil","Substitute","Grass Knot","Earthquake","Brick Break","Aurora Beam"]
                moves=moveset(type1,type2,avmoves,name=name)
            if a==2:
                nature="Modest"
                ability="Snow Warning"
                moves=["Blizzard","Protect","Aurora Veil",random.choice(["Earth Power","Giga Drain"])]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)       
#Weavile
class Weavile(Pokemon2):
    "Weavile"
    def __init__(self,name="Weavile",type1="Dark",type2="Ice",nature="None",level=100,happiness=255,hp=70,atk=120,defense=65,spatk=45,spdef=85,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Pressure","Infiltrator"]),item=random.choice(["Heavy-Duty Boots","Choice Band","Chople Berry","Dark Gem","Ice Gem","Focus Sash","Razor Claw"]),weight=74.96):
        color="red"
        if move =="None":
            avmoves=["Protect","Night Slash","Icicle Crash","Ice Shard","Poison Jab","Fake Out","Triple Axel","Low Kick","Shadow Claw","Ice Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
        #Magnezone
class Magnezone(Pokemon2):
    "Magnezone"
    def __init__(self,name="Magnezone",type1="Electric",type2="Steel",nature="None",level=100,happiness=255,hp=70,atk=70,defense=115,spatk=130,spdef=90,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sturdy","Analytic","Magnet Pull","Levitate"]),item=random.choice(["Leftovers","Choice Specs","Air Balloon","Focus Sash","Shuca Berry","Quick Claw","Bright Powder"]),weight=396.83):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Hidden Power","Flash Cannon","Thunderbolt","Iron Defense","Electric Terrain","Steel Beam","Signal Beam","Discharge","Zap Cannon","Lock-On","Thunder Wave","Mirror Coat","Toxic","Explosion","Reflect","Metal Sound"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Klinklang
class Klinklang(Pokemon2):
    def __init__(self,name="Klinklang",type1="Steel",type2="Electric",nature="None",level=100,happiness=255,hp=60,atk=110,defense=115,spatk=70,spdef=85,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Clear Body","Steelworker","Levitate"]),item=random.choice(["Leftovers","Occa Berry","Steel Gem","Shuca Berry"]),weight=178.57):
        if move =="None":
            avmoves=["Protect","Hidden Power","Flash Cannon","Thunderbolt","Iron Defense","Electric Terrain","Steel Beam","Volt Tackle","Superpower","Volt Switch","Metal Sound"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Gear Grind"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)        
#Rhyperior
class Rhyperior(Pokemon2):
    "Rhyperior"
    def __init__(self,name="Rhyperior",type1="Ground",type2="Rock",nature="None",level=100,happiness=255,hp=115,atk=140,defense=130,spatk=55,spdef=55,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=0,maxiv="No",move="None", ability=random.choice(["Solid Rock","Reckless"]),item=random.choice(["Leftovers","Weakness Policy","Hard Stone","Liechi Berry","Expert Belt","Life Orb","Zoom Lens","Sitrus Berry"]),weight=623.47):
        color="red"
        if move =="None":
            avmoves=["Protect","Stone Edge","Hammer Arm","High Horsepower","Thunder Punch","Giga Impact","Stealth Rock","Meteor Beam","Rock Wrecker","Megahorn","Drill Run","Rock Blast","Ice Punch","Earthquake","Dragon Rush","Avalanche"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Tangrowth
class Tangrowth(Pokemon2):
    "Tangrowth"
    def __init__(self,name="Tangrowth",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=100,atk=100,defense=125,spatk=110,spdef=50,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=0,maxiv="No",move="None", ability=random.choice(["Regenerator","Chlorophyll"]),item=random.choice(["Assault Vest","Rocky Helmet","Liechi Berry","Salac Berry","Power Herb","Expert Belt"]),weight=283.51):
        color="blue"
        if move =="None":
            avmoves=["Protect","Giga Drain","Sleep Powder","Ancient Power","Poison Jab","Grassy Terrain","Stealth Rock","Power Whip","Swords Dance","Rock Slide","Earthquake","Solar Beam","Focus Blast","Synthesis"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
#Electivire
class Electivire(Pokemon2):
    "Electivire"
    def __init__(self,name="Electivire",type1="Electric",type2="Fighting",nature="None",level=100,happiness=255,hp=75,atk=123,defense=67,spatk=105,spdef=85,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Motor Drive","Iron Fists"]),item=random.choice(["Life Orb","Air Balloon","Liechi Berry","Salac Berry","Expert Belt","Cheri Berry","Wide Lens"]),weight=305.56):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Plasma Fists","Close Combat","Wild Charge","Brick Break","Giga Impact","Electric Terrain","Cross Chop","Focus Blast","Reflect","Volt Tackle","Ice Punch","Fire Punch","Thunder Punch","Iron Tail","Darkest Lariat","Flamethrower","Low Kick","Rock Tomb","Thunder","Dynamic Punch","Iron Tail","Rock Slide"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Magmortar
class Magmortar(Pokemon2):
    "Magmortar"
    def __init__(self,name="Magmortar",type1="Fire",type2="None",nature="None",level=100,happiness=255,hp=75,atk=95,defense=67,spatk=125,spdef=95,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Mega Launcher","Quick Draw","Flame Body"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","Life Orb","Petaya Berry","Liechi Berry","Choice Scarf","Shuca Berry","Sitrus Berry"]),weight=149.91):
        color="red"
        if move =="None":
            avmoves=["Protect","Fire Blast","Sunny Day","Flamethrower","Toxic","Armor Cannon","Scorching Sands","Magma Storm","Steam Eruption","Dragon Pulse","Dark Pulse","Aura Sphere","Psychic","Thunderbolt","Cross Chop","Rock Slide","Thunder Punch","Flame Charge","Overheat"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Overheat" in moves:
            item="White Herb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                     
#Togekiss
class Togekiss(Pokemon2):
    "Togekiss"
    def __init__(self,name="Togekiss",type1="Fairy",type2="Flying",nature="None",level=100,happiness=255,hp=85,atk=50,defense=95,spatk=120,spdef=115,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Serene Grace","Hustle","Super Luck"]),item=random.choice(["Heavy-Duty Boots","Charti Berry","Leftovers","Yache Berry"]),weight=83.78):
        if move =="None":
            avmoves=["Protect","Roost","Nasty Plot","Air Slash","Moonblast","Extreme Speed","Metronome","Aura Sphere","Aeroblast","Shadow Ball","Grass Knot","Aerial Ace","Steel Wing","Sky Attack","Drain Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sky Attack" in moves:
            item="Power Herb"
        if ability=="Hustle":
            item="Wide Lens"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                
#Yanmega
class Yanmega(Pokemon2):
    "Yanmega"
    def __init__(self,name="Yanmega",type1="Bug",type2="Flying",nature="None",level=100,happiness=255,hp=86,atk=76,defense=86,spatk=116,spdef=56,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Speed Boost","Tinted Lens"]),item=random.choice(["Choice Specs","Heavy-Duty Boots","Life Orb","Charti Berry","Focus Sash","Bright Powder","Liechi Berry"]),weight=113.54):
        color="green"
        if move =="None":
            avmoves=["Protect","Ancient Power","Bug Buzz","Air Slash","U-turn","Double Team","Psychic","Hypnosis","Giga Drain","Night Slash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
#Gliscor
class Gliscor(Pokemon2):
    "Gliscor"
    def __init__(self,name="Gliscor",type1="Ground",type2="Flying",nature="None",level=100,happiness=255,hp=75,atk=95,defense=125,spatk=45,spdef=75,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Poison Heal","Sand Veil","Hyper Cutter"]),item=random.choice(["Smooth Rock","Quick Claw","Soft Sand","Focus Sash"]),weight=93.7):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Swords Dance","Earthquake","Rock Slide","U-turn","Sandstorm","Acrobatics","Tailwind","Fire Fang","Sandstorm","Counter","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sandstorm" in moves:
            item="Smooth Rock"
        if "Acrobatics" in moves:
            item="Flying Gem"
        if ability=="Poison Heal":
            item="Toxic Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                         
#Porygon-Z
class PorygonZ(Pokemon2):
    "Porygon-Z"
    def __init__(self,name="Porygon-Z",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=85,atk=80,defense=70,spatk=135,spdef=75,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Adaptability","Download"]),item=random.choice(["Choice Scarf","Life Orb","Chople Berry","Sitrus Berry","Expert Belt","Bright Powder"]),weight=74.96):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Ice Beam","Calm Mind","Recover","Thunderbolt","Flamethrower","Signal Beam","Hidden Power","Psychic","Shadow Ball","Hyper Beam","Trick Room","Tri Attack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                          
#Gallade
class Gallade(Pokemon2):
    "Gallade"
    def __init__(self,name="Gallade",type1="Psychic",type2="Fighting",nature="None",level=100,happiness=255,hp=68,atk=125,defense=65,spatk=65,spdef=115,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Steadfast","Sharpness","Justified"]),item=random.choice(["Choice Band","Assault Vest","Life Orb","Galladite","Lum Berry","Kasib Berry","Coba Berry","Scope Lens","King's Rock"]),weight=114.64):
        color="green"
        if move =="None":
            avmoves=["Protect","Swords Dance","Psycho Cut","Night Slash","Close Combat","Aqua Cutter","Leaf Blade","Sacred Sword","Triple Axel","Future Sight","Double Team","Stone Edge","Bulk Up","Slash","Ice Punch","Trick Room"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Trick Room" in moves:
            item="Iron Ball"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
                     
#Hisuian Arcanine
class HArcanine(Pokemon2):
    "Hisuian Arcanine"
    def __init__(self,name="Hisuian Arcanine",type1="Fire",type2="Rock",nature="None",level=100,happiness=255,hp=95,atk=125,defense=80,spatk=85,spdef=80,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Rock Head"]),item=random.choice(["Leftovers","Choice Band"]),weight=370.4) :
        color="red"
        if move =="None":
            avmoves=["Protect","Fire Fang","Flare Blitz","Wild Charge","Head Smash","Headlong Rush","Morning Sun","Raging Fury","Accelerock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
#Ursaluna
class Ursaluna(Pokemon2):
    "Ursaluna"
    def __init__(self,name="Ursaluna",type1="Normal",type2="Ground",nature="None",level=100,happiness=255,hp=130,atk=140,defense=105,spatk=45,spdef=80,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Guts","Rock Head","Unnerve","Bulletproof"]),item=random.choice(["Leftovers","Assault Vest"]),weight=639.3):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Bulk Up","Double-Edge","High Horsepower","Head Smash","Headlong Rush","Moonlight","Thrash","Ice Punch","Facade","Gunk Shot","Facade","Taunt","Belly Drum","Shadow Claw","Drain Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Probopass
class Probopass(Pokemon2):
    "Probopass"
    def __init__(self,name="Probopass",type1="Rock",type2="Steel",nature="None",level=100,happiness=255,hp=70,atk=55,defense=145,spatk=95,spdef=150,speed=40,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Sturdy","Levitate","Magnet Pull"]),item=random.choice(["Leftovers","Air Balloon","Shuca Berry","Chople Berry","Rock Incense","King's Rock"]),weight=749.57):
        color="blue"
        if move =="None":
            avmoves=["Protect","Iron Defense","Thunder Wave","Heavy Slam","Sandstorm","Zap Cannon","Power Gem","Rest","Rock Slide","Light Screen","Reflect","Steel Beam","Flash Cannon","Hidden Power","Taunt","Stealth Rock","Tri Attack","Pain Split"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                       
#Dusknoir
class Dusknoir(Pokemon2):
    "Dusknoir"
    def __init__(self,name="Dusknoir",type1="Ghost",type2="None",nature="None",level=100,happiness=255,hp=60,atk=110,defense=135,spatk=65,spdef=135,speed=45,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Pressure","Levitate","Hustle"]),item=random.choice(["Choice Band","Leftovers","Chesto Berry","Sitrus Berry","Ganlon Berry","Lum Berry","Apicot Berry","Muscle Band","Bright Powder"]),weight=235.01):
        if move =="None":
            avmoves=["Protect","Will-O-Wisp","Thunder Wave","Shadow Punch","Hex","Calm Mind","Rest","Metronome","Destiny Bond","Future Sight","Bulldoze","Pain Split","Thunder Punch","Poltergeist"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Froslass
class Froslass(Pokemon2):
    "Froslass"
    def __init__(self,name="Froslass",type1="Ice",type2="Ghost",nature="None",level=100,happiness=255,hp=70,atk=60,defense=70,spatk=110,spdef=70,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Snow Cloak","Levitate"]),item=random.choice(["Focus Sash","Ice Gem","Petaya Berry","Lax Incense"]),weight=58.64):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Will-O-Wisp","Blizzard","Shadow Punch","Hex","Calm Mind","Ice Beam","Destiny Bond","Aurora Veil","Bitter Malice","Double Team","Thunderbolt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Cryogonal
class Cryogonal(Pokemon2):
    def __init__(self,name="Cryogonal",type1="Ice",type2="Ghost",nature="None",level=100,happiness=255,hp=70,atk=50,defense=30,spatk=125,spdef=135,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Focus Sash","Heavy-Duty Boots","Petaya Berry","Wide Lens","Occa Berry"]),weight=326.28):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Blizzard","Ice Beam","Aurora Veil","Ice Shard","Light Screen","Reflect","Ancient Power","Explosion","Shadow Ball","Recover","Double Team","Flash Cannon","Sheer Cold","Aurora Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                
        #Wash Rotom
class WRotom(Pokemon2):
    "Wash Rotom"
    def __init__(self,name="Wash Rotom",type1="Electric",type2="Water",nature="None",level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=4,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Leftovers","Wide Lens"]),weight=0.66):
        color="blue"
        if move =="None":
            avmoves=["Protect","Volt Switch","Thunder Wave","Hydro Pump","Hex","Ice Beam","Will-O-Wisp","Trick","Thunder"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Trick" in moves:
            item="Choice Scarf"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
#Uxie
class Uxie(Pokemon2):
    "Uxie"
    def __init__(self,name="Uxie",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=75,atk=75,defense=130,spatk=75,spdef=130,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Leftovers","Colbur Berry"]),weight=0.66):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Thunder Wave","Recover","Shadow Ball","Psychic","Calm Mind","U-turn","Knock Off","Stealth Rock","Future Sight"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Mystical Power"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Mesprit
class Mesprit(Pokemon2):
    "Mesprit"
    def __init__(self,name="Mesprit",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=80,atk=105,defense=105,spatk=105,spdef=105,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Leftovers","Choice Scarf","Colbur Berry","Life Orb","Choice Specs"]),weight=0.66):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Thunder Wave","Recover","Shadow Ball","Psychic","Calm Mind","U-turn","Trick","Dazzling Gleam","Nasty Plot","Thunderbolt","Stealth Rock","Future Sight"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Mystical Power"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Gremlid
class Gremlid(Pokemon2):
    def __init__(self,name="Gremlid",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=75,atk=110,defense=80,spatk=145,spdef=80,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate"]),item="Leftovers",weight=100):
        if move =="None":
            avmoves=["Protect","Thunderbolt","Recover","Shadow Ball","Dark Pulse","Nasty Plot","Ice Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                            
        #Azelf
class Azelf(Pokemon2):
    "Azelf"
    def __init__(self,name="Azelf",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=75,atk=125,defense=70,spatk=125,spdef=70,speed=115,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Leftovers","Heavy-Duty Boots","Expert Belt","Life Orb"]),weight=0.66):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Thunderbolt","Recover","Shadow Ball","Psychic","Calm Mind","Ice Beam","Knock Off","Flamethrower","U-turn","Nasty Plot","Fire Blast","Psyshock","Energy Ball","Dazzling Gleam","Future Sight"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Mystical Power"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Dialga
class Dialga(Pokemon2):
    "Dialga"
    def __init__(self,name="Dialga",type1="Steel",type2="Dragon",nature="None",level=100,happiness=255,hp=100,atk=120,defense=120,spatk=150,spdef=100,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Pressure"]),item=random.choice(["Adamant Orb","Adamant Crystal","Shuca Berry"]),weight=1505.76):
        color="blue"
        if move =="None":
            avmoves=["Protect","Flash Cannon","Rest","Aura Sphere","Earth Power","Steel Beam","Power Gem","Ancient Power","Iron Head","Iron Defense","Dragon Pulse","Heavy Slam","Focus Blast","Overheat","Hyper Beam","Draco Meteor"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Roar of Time"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
       
#Palkia
class Palkia(Pokemon2):
    "Palkia"
    def __init__(self,name="Palkia",type1="Water",type2="Dragon",nature="None",level=100,happiness=255,hp=90,atk=120,defense=100,spatk=150,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Pressure"]),item=random.choice(["Lustrous Orb","Lustrous Globe"]),weight=740.75):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Hydro Pump","Rest","Aura Sphere","Earth Power","Thunder","Ancient Power","Power Gem","Aqua Tail","Draco Meteor","Focus Blast","Stone Edge","Blizzard","Fire Blast","Ice Beam","Hyper Beam"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Spacial Rend"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
     
#Giratina
class Giratina(Pokemon2):
    "Giratina"
    def __init__(self,name="Giratina",type1="Ghost",type2="Dragon",nature="None",level=100,happiness=255,hp=150,atk=100,defense=120,spatk=100,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Pressure"]),item=random.choice(["Griseous Orb","Griseous Core"]),weight=1653.47):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Shadow Ball","Rest","Aura Sphere","Earth Power","Dragon Claw","Shadow Sneak","Ancient Power","Draco Meteor","Hyper Beam","Phantom Force"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Shadow Force"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
 
#Heatran
class Heatran(Pokemon2):
    "Heatran"
    def __init__(self,name="Heatran",type1="Fire",type2="Steel",nature="None",level=100,happiness=255,hp=91,atk=90,defense=106,spatk=130,spdef=106,speed=77,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Flash Fire"]),item=random.choice(["Leftovers","Air Balloon","Passho Berry","Shuca Berry","Focus Sash","Quick Claw","Bught Powder"]),weight=947.99):
        color="red"
        if move =="None":
            avmoves=["Protect","Fire Blast","Flash Cannon","Ancient Power","Earth Power","Steel Beam","Dark Pulse","Solar Beam","Substitute","Fire Fang","Earthquake","Crunch","Stone Edge","Dragon Pulse","Metal Sound"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Magma Storm"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Regigigas
class Regigigas(Pokemon2):
    "Regigigas"
    def __init__(self,name="Regigigas",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=110,atk=160,defense=110,spatk=80,spdef=110,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Slow Start"]),item=random.choice(["Leftovers","Bright Powder","Shell Bell","Chople Berry","Life Orb"]),weight=925.94):
        if move =="None":
            avmoves=["Protect","Giga Impact","Iron Head","Hyper Beam","Earthquake","Substitute","Double Team","Thunder Wave","Return","Ice Punch","Stone Edge","Thunderbolt","Focus Blast","Drain Punch","Swagger"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Crush Grip"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                      
#Cresselia
class Cresselia(Pokemon2):
    "Cresselia"
    def __init__(self,name="Cresselia",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=120,atk=70,defense=120,spatk=75,spdef=130,speed=85,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Leftovers","Focus Band","Lum Berry","Wise Glasses","Sitrus Berry"]),weight=188.72):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Moonblast","Psychic","Calm Mind","Dazzling Gleam","Future Sight","Double Team","Shadow Ball","Ice Beam","Energy Ball","Toxic","Aurora Beam"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Lunar Blessing"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
#Phione
class Phione(Pokemon2):
    "Phione"
    def __init__(self,name="Phione",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=80,atk=80,defense=80,spatk=80,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Hydration"]),item="Leftovers",weight=6.83):
        color="blue"
        if move =="None":
            avmoves=["Protect","Take Heart","Hydro Pump","Moonblast","Calm Mind","Acid Armor"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Manaphy
class Manaphy(Pokemon2):
    "Manaphy"
    def __init__(self,name="Manaphy",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Hydration"]),item="Leftovers",weight=3.09):
        color="blue"
        if move =="None":
            avmoves=["Protect","Hydro Pump","Tail Glow","Rain Dance","Acid Armor"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Heart Swap"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Darkrai
class Darkrai(Pokemon2):
    "Darkrai"
    def __init__(self,name="Darkrai",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=70,atk=90,defense=90,spatk=135,spdef=90,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Bad Dreams"]),item=random.choice(["Leftovers","Salac Berry","Life Orb"]),weight=111.33):
        color="red"
        if move =="None":
            avmoves=["Protect","Shadow Ball","Psychic","Nasty Plot","Dark Pulse","Dark Hole","Double Team","Taunt"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Dark Void"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
#Eldegoss
class Eldegoss(Pokemon2):
    def __init__(self,name="Eldegoss",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=75,atk=50,defense=90,spatk=90,spdef=120,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Regenerator","Cotton Down"]),item="Leftovers",weight=5.5):
        color="green"
        if move =="None":
            avmoves=["Protect","Cotton Guard","Energy Ball","Synthesis","Leech Seed","Hidden Power","Pollen Puff"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Shaymin
class Shaymin(Pokemon2):
    "Shaymin"
    def __init__(self,name="Shaymin",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Natural Cure"]),item="Leftovers",weight=4.63):
        color="green"
        if move =="None":
            avmoves=["Protect","Energy Ball","Synthesis","Leech Seed","Hidden Power"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Seed Flare",]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Sky Shaymin
class SShaymin(Pokemon2):
    "Sky Shaymin"
    def __init__(self,name="Sky Shaymin",type1="Grass",type2="Flying",nature="None",level=100,happiness=255,hp=100,atk=103,defense=75,spatk=120,spdef=75,speed=127,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Serene Grace"]),item="Leftovers",weight=11.46):
        color="red"
        if move =="None":
            avmoves=["Protect","Energy Ball","Synthesis","Leech Seed","Hidden Power"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Seed Flare"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
                             
#Arceus
class Arceus(Pokemon2):
    "Arceus"
    def __init__(self,name="Arceus",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=120,atk=120,defense=120,spatk=120,spdef=120,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Multitype"]),item=random.choice(["Draco Plate","Dread Plate","Earth Plate","Fist Plate","Flame Plate","Icicle Plate","Insect Plate","Iron Plate","Meadow Plate","Mind Plate","Pixie Plate","Sky Plate","Splash Plate","Spooky Plate","Stone Plate","Toxic Plate","Zap Plate","Life Orb","Silk Scarf","Choice Scarf"]),weight=705.48):
        if move =="None":
            avmoves=["Protect","Hyper Beam","Extreme Speed","Recover","Hidden Power","Swords Dance","Taunt","Perish Song"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Judgement"]
        else:
            moves=move
        if item=="Draco Plate":
            type1="Dragon"
        if item=="Dread Plate":
            type1="Dark"
        if item=="Earth Plate":
            type1="Ground"    
        if item=="Fist Plate":
            type1="Fighting"    
        if item=="Flame Plate":
            type1="Fire"    
        if item=="Icicle Plate":
            type1="Ice"     
        if item=="Insect Plate":
            type1="Bug"    
        if item=="Iron Plate":
            type1="Steel"    
        if item=="Meadow Plate":
            type1="Grass"     
        if item=="Mind Plate":
            type1="Psychic"
        if item=="Pixie Plate":
            type1="Fairy"  
        if item=="Sky Plate":
            type1="Flying"          
        if item=="Splash Plate":
            type1="Water"    
        if item=="Spooky Plate":
            type1="Ghost"
        if item=="Stone Plate":
            type1="Rock"    
        if item=="Toxic Plate":
            type1="Poison"    
        if item=="Zap Plate":
            type1="Electric"         
        if type1!="Normal":
            name=name+f"({type1})"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
        #Origin Arceus
class OArceus(Pokemon2):
    "Origin Arceus"
    def __init__(self,name="Origin Arceus",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=200,atk=200,defense=200,spatk=200,spdef=200,speed=200,hpev=252,atkev=252,defev=252,spatkev=252,spdefev=252,speedev=252,maxiv="Yes",move="None", ability=random.choice(["Typeless"]),item="Leftovers",weight=100):
        if move =="None":
            avmoves=["Protect","Judgement","Roar of Time","Spacial Rend","Origin Pulse","Precipice Blades","Dragon Ascent","Magma Storm","Dark Void","Lunar Blessing","Crush Grip","Shadow Force","Aeroblast","Sacred Fire","Take Heart","Heart Swap","Seed Flare","Bleakwind Storm","Wildbolt Storm","Sandsear Storm","Sacred Sword","Secret Sword","Relic Song","Techno Blast","Blue Flare","Bolt Strike","Fusion Flare","Fusion Bolt","Freeze Shock","Ice Burn"]
            moves=avmoves
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Mightyena
class Mightyena(Pokemon2):
    "Mightyena"
    def __init__(self,name="Mightyena",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=70,atk=100,defense=70,spatk=60,spdef=70,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Strong Jaw","Intimidate","Quick Feet","Moxie"]),item="Leftovers",weight=81.57):
        color="red"
        if move =="None":
            avmoves=["Protect","Crunch","Fire Fang","Thunder Fang","Ice Fang","Poison Fang","Jaw Lock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Terryena
class Terryena(Pokemon2):
    def __init__(self,name="Terryena",type1="Dark",type2="Ground",nature="None",level=100,happiness=255,hp=85,atk=125,defense=90,spatk=50,spdef=80,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Strong Jaw","Intimidate"]),item="Leftovers",weight=100):
        if move =="None":
            avmoves=["Protect","Crunch","Fire Fang","Thunder Fang","Ice Fang","Poison Fang","Earthquake","Bulldoze","Jaw Lock","Night Slash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)         
#Bronzong
class Bronzong(Pokemon2):
    "Bronzong"
    def __init__(self,name="Bronzong",type1="Steel",type2="Psychic",nature="None",level=100,happiness=255,hp=67,atk=89,defense=116,spatk=79,spdef=116,speed=33,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Levitate","Heatproof","Heavy Metal"]),item=random.choice(["Leftovers","Occa Berry","Sitrus Berry","Lum Berry","Rocky Helmet","Iron Ball","Twisted Spoon"]),weight=412.26):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Trick Room","Extrasensory","Thunder Wave","Flash Cannon","Iron Defense","Light Screen","Reflect","Meteor Beam","Steel Beam","Heavy Slam","Psyshield Bash","Future Sight","Earthquake","Zen Headbutt","Gyro Ball"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Victini
class Victini(Pokemon2):
    "Victini"
    def __init__(self,name="Victini",type1="Psychic",type2="Fire",nature="None",level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Victory Star",item="Leftovers",weight=8.82):
        color="red"
        if move =="None":
            avmoves=["Protect","Searing Shot","Hidden Power","V-create","Psychic","Focus Blast","Blue Flare"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Serperior
class Serperior(Pokemon2):
    "Serperior"
    def __init__(self,name="Serperior",type1="Grass",type2="Dragon",nature="None",level=100,happiness=255,hp=75,atk=85,defense=95,spatk=85,spdef=95,speed=113,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Contrary","Overgrow","Chlorophyll"]),item="Leftovers",weight=138.89):
        color="green"
        if move =="None":
            avmoves=["Protect","Leaf Storm","Hidden Power","Giga Drain","Coil","Focus Blast","Leech Seed","Frenzy Plant","Leaf Blade","Aerial Ace"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
#Emboar
class Emboar(Pokemon2):
    "Emboar"
    def __init__(self,name="Emboar",type1="Fire",type2="Fighting",nature="None",level=100,happiness=255,hp=110,atk=133,defense=85,spatk=90,spdef=65,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Reckless","Blaze","Bull Rush","Rock Head"]),item=random.choice(["Leftovers","Expert Belt"]),weight=330.69):
        color="red"
        if move =="None":
            avmoves=["Protect","Hammer Arm","Flare Blitz","Heat Crash","Head Smash","Close Combat","Blast Burn","Wild Charge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Samurott
class Samurott(Pokemon2):
    "Samurott"
    def __init__(self,name="Samurott",type1="Water",type2="Steel",nature="None",level=100,happiness=255,hp=95,atk=118,defense=85,spatk=98,spdef=70,speed=82,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Shell Armor","Torrent","Defiant"]),item="Leftovers",weight=208.56):
        color="blue"
        if move =="None":
            avmoves=["Protect","Swords Dance","Razor Shell","Aqua Jet","Megahorn","Hydro Pump","Hydro Cannon","Aqua Cutter","Smart Strike"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Hisuian Samurott
class HSamurott(Pokemon2):
    "Hisuian Samurott"
    def __init__(self,name="Hisuian Samurott",type1="Water",type2="Dark",nature="None",level=100,happiness=255,hp=90,atk=108,defense=80,spatk=100,spdef=65,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Sharpness",item="Leftovers",weight=128.3):
        color="blue"
        if move =="None":
            avmoves=["Protect","Swords Dance","Razor Shell","Aqua Jet","Megahorn","Liquidation","Night Slash","Ceaseless Edge","Aqua Cutter","Sacred Sword"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Hisuian Typhlosion
class HTyphlosion(Pokemon2):
    "Hisuian Typhlosion"
    def __init__(self,name="Hisuian Typhlosion",type1="Fire",type2="Ghost",nature="None",level=100,happiness=255,hp=73,atk=84,defense=78,spatk=119,spdef=85,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Blaze"]),item=random.choice(["Leftovers","Heavy-Duty Boots"]),weight=153.9):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Hidden Power","Earth Power","Fire Blast","Lava Plume","Eruption","Focus Blast","Shadow Ball","Destiny Bond","Calm Mind","Will-O-Wisp"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Infernal Parade"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
 #Skeledirge
class Skeledirge(Pokemon2):
    def __init__(self,name="Skeledirge",type1="Fire",type2="Ghost",nature="None",level=100,happiness=255,hp=104,atk=75,defense=100,spatk=110,spdef=75,speed=66,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Unaware","Blaze"]),item=random.choice(["Throat Spray","Air Balloon"]),weight=719.81):
        color="red"
        if move =="None":
            avmoves=["Protect","Earth Power","Fire Blast","Flamethrower","Eruption","Focus Blast","Shadow Ball","Hex","Destiny Bond","Will-O-Wisp","Slack Off"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Torch Song"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
#Unfezant
class Unfezant(Pokemon2):
    "Unfezant"
    def __init__(self,name="Unfezant",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=80,atk=65,defense=80,spatk=145,spdef=55,speed=113,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Super Luck","Big Pecks","Scrappy"]),item=random.choice(["Leftovers","Liechi Berry"]),weight=63.93):
        if move =="None":
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-turn","Giga Impact","Sky Attack","Air Slash","Aura Sphere","Tailwind","Heat Wave","Hypnosis","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Final Gambit" in moves:
            hpev=252
            atkev=0
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                                                                                                                 #Zebstrika
class Zebstrika(Pokemon2):
    "Zebstrika"
    def __init__(self,name="Zebstrika",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=75,atk=110,defense=63,spatk=80,spdef=63,speed=116,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Motor Drive","Sap Sipper","Flare Boost"]),item=random.choice(["Leftovers","Air Balloon","Liechi Berry","Life Orb"]),weight=175.27):
        if move =="None":
            avmoves=["Protect","Wild Charge","Discharge","Thunderbolt","Thunder Wave","Volt Switch","Bolt Strike","Me First","Flame Charge","Overheat","Return","Quick Attack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Flare Boost":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Stoutland
class Stoutland(Pokemon2):
    "Stoutland"
    def __init__(self,name="Stoutland",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=85,atk=110,defense=90,spatk=45,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Scrappy","Intimidate"]),item=random.choice(["Silk Scarf","Life Orb","Salac Berry","Focus Sash"]),weight=134.48):
        if move =="None":
            avmoves=["Protect","Giga Impact","Crunch","Play Rough","Thunder Fang","Stomping Tantrum","Reversal","Wild Charge","Ice Fang","Return"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight) 
#Houndstone
class Houndstone(Pokemon2):
    def __init__(self,name="Houndstone",type1="Ghost",type2="None",nature="None",level=100,happiness=255,hp=72,atk=101,defense=100,spatk=50,spdef=97,speed=68,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sand Rush","Fluffy"]),item=random.choice(["Spell Tag","Life Orb"]),weight=33.07):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Phantom Force","Crunch","Play Rough","Thunder Fang","Stomping Tantrum","Crunch","Shadow Claw"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Last Respects"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                         
#Gigalith
class Gigalith(Pokemon2):
    "Gigalith"
    def __init__(self,name="Gigalith",type1="Rock",type2="None",nature="None",level=100,happiness=255,hp=85,atk=135,defense=130,spatk=60,spdef=80,speed=25,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Sturdy","Sand Force","Sand Stream"]),item=random.choice(["Leftovers","Hard Stone"]),weight=573.2):
        color="blue"
        if move =="None":
            avmoves=["Protect","Iron Defense","Stone Edge","Rock Blast","Earthquake","Explosion","Rock Slide","Rest","Meteor Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Excadrill
class Excadrill(Pokemon2):
    "Excadrill"
    def __init__(self,name="Excadrill",type1="Ground",type2="Steel",nature="None",level=100,happiness=255,hp=110,atk=135,defense=60,spatk=50,spdef=65,speed=88,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sand Rush","Sand Force","Mold Breaker"]),item=random.choice(["Leftovers","Air Balloon","Life Orb","Liechi Berry","Focus Sash","Chople Berry"]),weight=89.07):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Swords Dance","Earthquake","Drill Run","Iron Head","Rock Slide","Dig","Submission","X-Scissor"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Conkeldurr
class Conkeldurr(Pokemon2):
    "Conkeldurr"
    def __init__(self,name="Conkeldurr",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=105,atk=140,defense=95,spatk=55,spdef=65,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Guts","Sheer Force","Iron Fist"]),item=random.choice(["Life Orb","Fighting Gem"]),weight=191.80):
        color="red"
        if move =="None":
            avmoves=["Protect","Mach Punch","Drain Punch","Bulk Up","Facade","Knock Off"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Seismitoad
class Seismitoad (Pokemon2):
    "Seismitoad"
    def __init__(self,name="Seismitoad",type1="Water",type2="Ground",nature="None",level=100,happiness=255,hp=105,atk=95,defense=75,spatk=85,spdef=75,speed=74,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Poison Touch","Swift Swim","Drizzle"]),item=random.choice(["Leftovers","Salac Berry","Rindo Berry","Life Orb"]),weight=136.69):
        color="blue"
        if move =="None":
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Drain Punch","Waterfall","Ice Punch","Muddy Water","Earth Power","Poison Jab","Rain Dance","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Leavanny
class Leavanny(Pokemon2):
    "Leavanny"
    def __init__(self,name="Leavanny",type1="Bug",type2="Grass",nature="None",level=100,happiness=255,hp=75,atk=103,defense=80,spatk=70,spdef=80,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Sharpness","Poison Heal"]),item=random.choice(["Leftovers","Coba Berry","Focus Sash"]),weight=45.19):
        color="green"
        if move =="None":
            avmoves=["Protect","Razor Leaf","Swords Dance","X-Scissor","U-turn","Leaf Blade","Sticky Web","Aerial Ace","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Poison Heal":
            item="Toxic Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Scolipede
class Scolipede(Pokemon2):
    "Scolipede"
    def __init__(self,name="Scolipede",type1="Bug",type2="Poison",nature="None",level=100,happiness=255,hp=60,atk=100,defense=89,spatk=55,spdef=69,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Poison Touch","Speed Boost","Swarm"]),item=random.choice(["Leftovers","Salac Berry","Liechi Berry","Choice Scarf"]),weight=442.03):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Leech Life","Megahorn","Toxic","U-turn","X-Scissor","Poison Jab","Earthquake","Rock Slide","Toxic Spikes"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Basculegion
class Basculegion (Pokemon2):
    "Basculegion"
    def __init__(self,name="Basculegion",type1="Water",type2="Ghost",nature="None",level=100,happiness=255,hp=120,atk=112,defense=65,spatk=80,spdef=75,speed=78,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Adaptability","Swift Swim","Mold Breaker","Rattled"]),item=random.choice(["Leftovers","Salac Berry"]),weight=242.5):
        color="green"
        if move =="None":
            avmoves=["Protect","Wave Crash","Crunch","Aqua Tail","Aqua Jet","Waterfall","Zen Headbutt","Destiny Bond","Last Respects","Flail","Double-Edge","Aqua Fang"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Hisuian Lilligant
class HLilligant(Pokemon2):
    "Hisuian Lilligant"
    def __init__(self,name="Hisuian Lilligant",type1="Grass",type2="Fighting",nature="None",level=100,happiness=255,hp=70,atk=105,defense=75,spatk=50,spdef=75,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Hustle"]),item="Leftovers",weight=42.3):
        color="green"
        if move =="None":
            avmoves=["Protect","Leaf Blade","Swords Dance","Victory Dance","Close Combat","Petal Dance","Recover","Drain Punch","Sleep Powder","Ice Spinner","Solar Blade"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Krookodile
class Krookodile(Pokemon2):
    "Krookodile"
    def __init__(self,name="Krookodile",type1="Ground",type2="Dark",nature="None",level=100,happiness=255,hp=95,atk=117,defense=80,spatk=65,spdef=70,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Moxie","Anger Point"]),item=random.choice(["Leftovers","Chople Berry","Black Glasses","Expert Belt","Choice Band","Liechi Berry","Assault Vest"]),weight=212.31):
        color="red"
        if move =="None":
            avmoves=["Protect","Wicked Blow","Earthquake","Stone Edge","Crunch","Foul Play","Outrage","Darkest Lariat","Scale Shot","Dig","Fire Fang","Aqua Tail","High Horsepower","Rock Slide","Close Combat","Power Trip"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Darmanitan
class Darmanitan(Pokemon2):
    "Darmanitan"
    def __init__(self,name="Darmanitan",type1="Fire",type2="Fighting",nature="None",level=100,happiness=255,hp=105,atk=140,defense=55,spatk=30,spdef=55,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sheer Force","Zen Mode"]),item=random.choice(["Choice Scarf","Fighting Gem","Liechi Berry"]),weight=204.81):
        color="red"
        if move =="None":
            avmoves=["Superpower","Earthquake","Stone Edge","Crunch","Flare Blitz","U-turn","Hammer Arm"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Galarian Darmanitan
class GDarmanitan(Pokemon2):
    "Galarian Darmanitan"
    def __init__(self,name="Galarian Darmanitan",type1="Ice",type2="None",nature="None",level=100,happiness=255,hp=105,atk=140,defense=55,spatk=30,spdef=55,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Gorilla Tactics","Zen Mode"]),item=random.choice(["Choice Scarf","Salac Berry"]),weight=264.6):
        color="cyan"
        if move =="None":
            if ability!="Zen Mode":
                avmoves=["Superpower","Earthquake","Stone Edge","Crunch","Icicle Crash","U-turn","Ice Hammer","Avalanche"]
            if ability=="Zen Mode":
                avmoves=["Superpower","Heat Crash","Flare Blitz","Crunch","Icicle Crash","U-turn","Ice Hammer","Avalanche","Flamethrower"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Scrafty
class Scrafty(Pokemon2):
    "Scrafty"
    def __init__(self,name="Scrafty",type1="Dark",type2="Fighting",nature="None",level=100,happiness=255,hp=65,atk=90,defense=115,spatk=45,spdef=115,speed=58,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Intimidate","Moxie","Shed Skin"]),item=random.choice(["Leftovers"]),weight=66.14):
        color="red"
        if move =="None":
            avmoves=["Protect","Close Combat","Drain Punch","Fake Out","Crunch","Foul Play","Knock Off","Head Smash","Dragon Tail","Bulk Up","Amnesia"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Cofagrigus
class Cofagrigus(Pokemon2):
    "Cofagrigus"
    def __init__(self,name="Cofagrigus",type1="Ghost",type2="None",nature="None",level=100,happiness=255,hp=58,atk=50,defense=145,spatk=95,spdef=105,speed=30,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Mummy","Shadow Shield","Cursed Body"]),item="Leftovers",weight=168.65):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Will-O-Wisp","Hex","Shadow Sneak","Dark Pulse","Body Press","Destiny Bond","Rest","Night Shade"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Runerigus
class Runerigus(Pokemon2):
    "Runerigus"
    def __init__(self,name="Runerigus",type1="Ground",type2="Ghost",nature="None",level=100,happiness=255,hp=58,atk=95,defense=145,spatk=50,spdef=105,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Wandering Spirit","Shadow Shield","Sand Veil"]),item="Leftovers",weight=146.8):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Will-O-Wisp","Shadow Claw","Shadow Sneak","Earthquake","Body Press","Destiny Bond","Poltergeist"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Carracosta
class Carracosta (Pokemon2):
    "Carracosta"
    def __init__(self,name="Carracosta",type1="Water",type2="Rock",nature="None",level=100,happiness=255,hp=74,atk=108,defense=133,spatk=83,spdef=105,speed=32,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Solid Rock","Sturdy","Swift Swim"]),item=random.choice(["Leftovers","White Herb","Liechi Berry","Water Gem","Lum Berry"]),weight=178.57):
        color="blue"
        if move =="None":
            avmoves=["Protect","Liquidation","Earthquake","Stone Edge","Ancient Power","Waterfall","Shell Smash","Meteor Beam","Rock Wrecker","Hydro Pump","Aqua Jet","Rock Slide"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Archeops
class Archeops(Pokemon2):
    "Archeops"
    def __init__(self,name="Archeops",type1="Rock",type2="Flying",nature="None",level=100,happiness=255,hp=75,atk=150,defense=55,spatk=122,spdef=55,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Defeatist","Intimidate"]),item=random.choice(["Flying Gem","Life Orb","Sitrus Berry","Enigma Berry","Choice Band"]),weight=70.55):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Acrobatics","Earthquake","Stone Edge","Dragon Claw","Crunch","U-turn","Meteor Beam","Head Smash","Rock Wrecker","Double Team","Quick Attack","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Zoroark
class Zoroark(Pokemon2):
    "Zoroark"
    def __init__(self,name="Zoroark",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=60,atk=105,defense=60,spatk=120,spdef=60,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Illusion",item="Life Orb",weight=178.79):
        color="red"
        if move =="None":
            avmoves=["Protect","Dark Pulse","Flamethrower","Nasty Plot","Night Daze","Knock Off","U-turn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Hisuian Zoroark
class HZoroark(Pokemon2):
    "Hisuian Zoroark"
    def __init__(self,name="Hisuian Zoroark",type1="Normal",type2="Ghost",nature="None",level=100,happiness=255,hp=55,atk=100,defense=60,spatk=125,spdef=60,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Illusion",item=random.choice(["Life Orb","Leftovers","Focus Sash"]),weight=160.9):
        if move =="None":
            avmoves=["Protect","Shadow Ball","Flamethrower","Nasty Plot","Bitter Malice","Knock Off","U-turn","Destiny Bond","Poltergeist","Return","Swords Dance","Low Kick"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)        
#Gothitelle
class Gothitelle(Pokemon2):
    "Gothitelle"
    def __init__(self,name="Gothitelle",type1="Psychic",type2="Dark",nature="None",level=100,happiness=255,hp=70,atk=55,defense=95,spatk=95,spdef=110,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Competitive","Shadow Tag","Frisk"]),item=random.choice(["Leftovers","Sitrus Berry","Choice Scarf"]),weight=97):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Shadow Ball","Psychic","Calm Mind","Hypnosis","Thunder Wave","Stored Power","Psycho Boost","Future Sight","Dark Pulse","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Reuniclus
class Reuniclus(Pokemon2):
    "Reuniclus"
    def __init__(self,name="Reuniclus",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=110,atk=65,defense=75,spatk=125,spdef=85,speed=30,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Magic Guard",item=random.choice(["Leftovers","Life Orb","Colbur Berry","Toxic Orb"]),weight=44.31):
        color="green"
        if move =="None":
            avmoves=["Protect","Shadow Ball","Psychic","Calm Mind","Acid Armor","Thunder Wave","Stored Power","Reflect","Pain Split","Future Sight","Toxic","Light Screen"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Toxic Orb" in item and "Trick" not in moves:
            moves[3]="Trick"
            ability="Magic Guard"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                   
        #Swanna
class Swanna(Pokemon2):
    "Swanna"
    def __init__(self,name="Swanna",type1="Water",type2="Flying",nature="None",level=100,happiness=255,hp=75,atk=107,defense=63,spatk=107,spdef=63,speed=108,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None",ability=random.choice(["Hydration","No Guard","Drizzle"]),item=random.choice(["Leftovers","Wacan Berry","Focus Sash"]),weight=53.35):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Brave Bird","Hurricane","Rain Dance","Roost","Air Slash","Surf","Feather Dance","Tailwind","Ice Beam","Scald"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Drizzle":
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
class Cramorant(Pokemon2):
    def __init__(self,name="Cramorant",type1="Flying",type2="Water",nature="None",level=100,happiness=255,hp=70,atk=85,defense=55,spatk=85,spdef=95,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None",ability=random.choice(["Gulp Missile"]),item="Leftovers",weight=39.7):
        color="blue"
        if move =="None":
            avmoves=["Protect","Brave Bird","Hurricane","Rain Dance","Roost","Air Slash","Belch","Drill Peck","Amnesia"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Surf"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                
#Vanilluxe
class Vanilluxe(Pokemon2):
    "Vanilluxe"
    def __init__(self,name="Vanilluxe",type1="Ice",type2="None",nature="None",level=100,happiness=255,hp=71,atk=65,defense=75,spatk=130,spdef=85,speed=109,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Snow Warning",item=random.choice(["Leftovers","Occa Berry","Sitrus Berry"]),weight=126.77):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Blizzard","Ice Beam","Acid Armor","Icicle Spear","Freeze-Dry","Weather Ball","Avalanche","Flash Cannon"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Escavalier
class Escavalier(Pokemon2):
    "Escavalier"
    def __init__(self,name="Escavalier",type1="Bug",type2="Steel",nature="None",level=100,happiness=255,hp=70,atk=135,defense=105,spatk=60,spdef=105,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Shell Armor","Overcoat","Swarm","Filter"]),item=random.choice(["Leftovers","Occa Berry","Quick Claw"]),weight=72.75):
        color="green"
        if move =="None":
            avmoves=["Protect","Iron Head","Iron Defense","X-Scissor","U-turn","Swords Dance","Double Iron Bash","Substitute","Megahorn","Knock Off"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
#Mollonce
class Mollonce(Pokemon2):
    def __init__(self,name="Mollonce",type1="Bug",type2="Steel",nature="None",level=100,happiness=255,hp=70,atk=145,defense=115,spatk=50,spdef=85,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Shell Armor","Super Luck"]),item="Focus Sash",weight=100):
        if move =="None":
            avmoves=["Protect","Iron Head","Iron Defense","X-Scissor","U-turn","Swords Dance","Drill Run","Megahorn","Night Slash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)          
                            #Jellicent
class Jellicent(Pokemon2):
    "Jellicent"
    def __init__(self,name="Jellicent",type1="Water",type2="Ghost",nature="None",level=100,happiness=255,hp=100,atk=60,defense=70,spatk=100,spdef=105,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Water Absorb","Water Bubble","Cursed Body"]),item=random.choice(["Leftovers","Rindo Berry","Ghost Gem","Expert Belt"]),weight=297.62):
        color=random.choice(["cyan","magenta"])
        if move =="None":
            avmoves=["Protect","Night Shade","Acid Armor","Rain Dance","Recover","Will-O-Wisp","Hex","Destiny Bond","Pain Split","Water Spout","Hydro Pump","Surf","Scald","Psychic","Whirlpool"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
#Galvantula
class Galvantula(Pokemon2):
    "Galvantula"
    def __init__(self,name="Galvantula",type1="Bug",type2="Electric",nature="None",level=100,happiness=255,hp=70,atk=77,defense=60,spatk=107,spdef=60,speed=108,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Swarm","Compound Eyes","Unnerve"]),item=random.choice(["Life Orb","Heavy-Duty Boots","Petaya Berry","Sitrus Berry","Scope Lens"]),weight=31.53):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Electroweb","Thunder Wave","Electro Ball","Sucker Punch","Discharge","Bug Buzz","Giga Drain","Thunderbolt","Cross Poison"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Ferrothorn
class Ferrothorn(Pokemon2):
    "Ferrothorn"
    def __init__(self,name="Ferrothorn",type1="Grass",type2="Steel",nature="None",level=100,happiness=255,hp=74,atk=94,defense=131,spatk=54,spdef=116,speed=20,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Iron Barbs","Anticipation","Shell Armor"]),item=random.choice(["Leftovers","Rocky Helmet","Occa Berry","Apicot Berry","Choice Band"]),weight=242.51):
        color="green"
        if move =="None":
            avmoves=["Protect","Gyro Ball","Iron Defense","Power Whip","Leech Seed","Curse","Heavy Slam","Body Press","Spikes","Explosion","Bulldoze","Rest"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Eelektross
class Eelektross(Pokemon2):
    "Eelektross"
    def __init__(self,name="Eelektross",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=95,atk=115,defense=80,spatk=115,spdef=80,speed=50,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Levitate","Fatal Precision"]),item=random.choice(["Leftovers","Assault Vest","Salac Berry","Choice Band","Magnet"]),weight=177.47):
        color="blue"
        if move =="None":
            avmoves=["Protect","Wild Charge","Thunder Wave","Coil","Sludge Bomb","Discharge","Crunch","Crush Claw","Dragon Claw","Toxic","Thunderbolt","Thunder","Giga Drain","Flamethrower","Zap Cannon","Thunder Punch","Fire Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Chandelure
class Chandelure(Pokemon2):
    "Chandelure"
    def __init__(self,name="Chandelure",type1="Ghost",type2="Fire",nature="None",level=100,happiness=255,hp=60,atk=55,defense=90,spatk=145,spdef=90,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Shadow Tag","Flame Body","Levitate"]),item=random.choice(["Leftovers","Choice Scarf","Life Orb","Focus Sash","White Herb"]),weight=75.62):
        color="blue"
        if move =="None":
            avmoves=["Protect","Hidden Power","Fire Blast","Focus Blast","Shadow Ball","Infernal Parade","Hex","Will-O-Wisp","Overheat","Destiny Bond","Pain Split","Trick","Solar Beam","Energy Ball","Calm Mind","Minimize","Psychic","Rest"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Haxorus
class Haxorus(Pokemon2):
    "Haxorus"
    def __init__(self,name="Haxorus",type1="Dragon",type2="Steel",nature="None",level=100,happiness=255,hp=76,atk=147,defense=90,spatk=60,spdef=70,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Mold Breaker","Sheer Force","Unnerve"]),item=random.choice(["Leftovers","Dragon Gem","Focus Sash","Choice Scarf","Yache Berry","Persim Berry"]),weight=232.59):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Outrage","Swords Dance","Dual Chop","Dragon Dance","Dragon Claw","Crunch","Scale Shot","Earthquake","Close Combat","First Impression","Iron Head","Brick Break","Razor Wind","Rock Slide"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Beartic
class Beartic(Pokemon2):
    "Beartic"
    def __init__(self,name="Beartic",type1="Ice",type2="Fighting",nature="None",level=100,happiness=255,hp=95,atk=140,defense=80,spatk=70,spdef=80,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Slush Rush","Swift Swim","Ice Body","Snow Cloak"]),item=random.choice(["Leftovers","Focus Sash","Charti Berry","Liechi Berry","Bright Powder","Sitrus Berry","Lax Incense"]),weight=573.2):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Outrage","Swords Dance","Ice Fang","Dragon Claw","Crunch","Hammer Arm","Superpower","Snowscape","Earthquake","Close Combat","Ice Hammer","Liquidation"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Icicle Crash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Accelgor
class Accelgor(Pokemon2):
    "Accelgor"
    def __init__(self,name="Accelgor",type1="Bug",type2="Dark",nature="None",level=100,happiness=255,hp=80,atk=70,defense=40,spatk=110,spdef=60,speed=145,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sticky Hold","Sheer Force","Unburden","Adaptability"]),item=random.choice(["Leftovers","Petaya Berry","Bright Powder"]),weight=55.78):
        color="red"
        if move =="None":
            avmoves=["Protect","Toxic","Bug Buzz","Final Gambit","U-turn","Recover","Giga Drain","Water Shuriken","Sludge Bomb","Skitter Smack","Dark Pulse","Double Team","Spikes"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Final Gambit" in moves:
            hpev=252
            atkev=0
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  

#Mienshao
class Mienshao(Pokemon2):
    "Mienshao"
    def __init__(self,name="Mienshao",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=65,atk=125,defense=60,spatk=95,spdef=60,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Inner Focus","Regenerator","Reckless"]),item=random.choice(["Choice Scarf","Choice Band","Life Orb","King's Rock","Muscle Band","Focus Sash"]),weight=78.26):
        color="red"
        if move =="None":
            avmoves=["Protect","Drain Punch","High Jump Kick","Aura Sphere","U-turn","Fake Out","Rock Slide","Smelling Salts","Aerial Ace"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move    
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                
#Druddigon
class Druddigon(Pokemon2):
    "Druddigon"
    def __init__(self,name="Druddigon",type1="Dragon",type2="Rock",nature="None",level=100,happiness=255,hp=90,atk=120,defense=90,spatk=60,spdef=90,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sheer Force","Rough Skin","Mold Breaker"]),item=random.choice(["Life Orb","Yache Berry","Salac Berry","Rocky Helmet"]),weight=306.44):
        color="blue"
        if move =="None":
            avmoves=["Protect","Outrage","Swords Dance","Superpower","Dragon Dance","Dragon Claw","Crunch","Scale Shot","Dragon Hammer","Toxic","Dragon Tail","Head Smash","Rock Slide","Sucker Punch","Glare","Fire Fang"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      

#Golurk
class Golurk(Pokemon2):
    "Golurk"
    def __init__(self,name="Golurk",type1="Ground",type2="Ghost",nature="None",level=100,happiness=255,hp=100,atk=124,defense=90,spatk=55,spdef=90,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["No Guard","Iron Fist"]),item=random.choice(["Leftovers","Assault Vest","Ghost Gem","Lum Berry"]),weight=727.53):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Phantom Force","Hammer Arm","Shadow Sneak","Earthquake","Dynamic Punch","Stomping Tantrum","High Horsepower","Magnitude","Headlong Rush","Substitute","Poltergeist"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Bisharp
class Bisharp(Pokemon2):
    "Bisharp"
    def __init__(self,name="Bisharp",type1="Dark",type2="Steel",nature="None",level=100,happiness=255,hp=65,atk=125,defense=100,spatk=60,spdef=70,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Defiant","Pressure"]),item=random.choice(["Eviolite","Chople Berry"]),weight=154.32):
        color="red"
        if move =="None":
            avmoves=["Protect","Night Slash","Swords Dance","Iron Head","Superpower","Sucker Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
#Kingambit
class Kingambit(Pokemon2):
    def __init__(self,name="Kingambit",type1="Dark",type2="Steel",nature="None",level=100,happiness=255,hp=85,atk=145,defense=110,spatk=60,spdef=80,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Supreme Overlord","Defiant","Pressure"]),item=random.choice(["Life Orb","Black Glasses","Leftovers"]),weight=264.55):
        color="red"
        if move =="None":
            avmoves=["Protect","Night Slash","Swords Dance","Iron Head","Superpower","Sucker Punch"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Kowtow Cleave"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Bouffalant
class Bouffalant(Pokemon2):
    "Bouffalant"
    def __init__(self,name="Bouffalant",type1="Normal",type2="Ground",nature="None",level=100,happiness=255,hp=95,atk=110,defense=95,spatk=40,spdef=95,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sap Sipper","Reckless","Bull Rush"]),item=random.choice(["Leftovers","Normal Gem","Life Orb","Sitrus Berry"]),weight=208.56):
        if move =="None":
            avmoves=["Protect","Megahorn","Swords Dance","Superpower","Head Charge","High Horsepower","Wild Charge","Stone Edge","Iron Head","Zen Headbutt","Close Combat","Headlong Rush","Slack Off","Earthquake","Thrash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)  
#Braviary
class Braviary(Pokemon2):
    "Braviary"
    def __init__(self,name="Braviary",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=100,atk=123,defense=75,spatk=57,spdef=75,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Defiant","Sheer Force"]),item=random.choice(["Life Orb","Fighting Gem","Normal Gem","White Herb","Choice Band","Persim Berry","Wacan Berry"]),weight=90.39):
        if move =="None":
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Close Combat","U-turn","Sky Attack","Rock Slide","Superpower","Bulk Up","Crush Claw","Thrash","Tailwind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Final Gambit" in moves:
            hpev=252
            atkev=0
        if "Sky Attack" in moves:
            item="Power Herb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Hisuian Braviary
class HBraviary(Pokemon2):
    "Hisuian Braviary"
    def __init__(self,name="Hisuian Braviary",type1="Psychic",type2="Flying",nature="None",level=100,happiness=255,hp=110,atk=83,defense=70,spatk=112,spdef=70,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sheer Force","Tinted Lens","Defiant"]),item=random.choice(["Life Orb","Choice Specs"]),weight=95.7):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Roost","Esper Wing","Air Slash","Dazzling Gleam","Mystical Fire","Psychic","U-turn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
        
#Mandibuzz
class Mandibuzz(Pokemon2):
    "Mandibuzz"
    def __init__(self,name="Mandibuzz",type1="Dark",type2="Flying",nature="None",level=100,happiness=255,hp=110,atk=65,defense=105,spatk=55,spdef=105,speed=80,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Overcoat","Weak Armor","Intimidate","Big Pecks"]),item=random.choice(["Rocky Helmet","Leftovers","Apicot Berry","Salac Berry","Wacan Berry","Sitrus Berry"]),weight=87.08):
        color="red"
        if move =="None":
            avmoves=["Protect","Final Gambit","Roost","Brave Bird","Iron Defense","U-turn","Knock Off","Bone Rush","Toxic","Double Team","Air Slash","Dark Pulse","Taunt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Final Gambit" in moves:
            hpev=252
            atkev=0
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Heatmor
class Heatmor(Pokemon2):
    "Heatmor"
    def __init__(self,name="Heatmor",type1="Fire",type2="Dragon",nature="None",level=100,happiness=255,hp=100,atk=77,defense=86,spatk=135,spdef=86,speed=45,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Flash Fire","Fatal Precision","Berserk"]),item=random.choice(["Leftovers","Salac Berry","Focus Sash"]),weight=127.87):
        color="red"
        if move =="None":
            avmoves=["Protect","Fire Lash","Flare Blitz","Inferno","Giga Drain","U-turn","Knock Off","Sunny Day","Draco Meteor","Dragon Pulse","Focus Blast","Sucker Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Durant
class Durant(Pokemon2):
    "Durant"
    def __init__(self,name="Durant",type1="Bug",type2="Steel",nature="None",level=100,happiness=255,hp=58,atk=119,defense=117,spatk=48,spdef=68,speed=119,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Hustle","Swarm","Battle Armor"]),item=random.choice(["Leftovers","Liechi Berry","Wide Lens","Power Herb","Focus Sash"]),weight=72.75):
        if move =="None":
            avmoves=["Protect","Crunch","Iron Head","U-turn","Knock Off","X-Scissor","Rock Slide","Stomping Tantrum","First Impression","Skitter Smack","Dig","Guillotine","Stone Edge","Agility","Iron Defense","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)        
#Hydreigon
class Hydreigon(Pokemon2):
    "Hydreigon"
    def __init__(self,name="Hydreigon",type1="Dark",type2="Dragon",nature="None",level=100,happiness=255,hp=92,atk=105,defense=90,spatk=125,spdef=90,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Leftovers","Roseli Berry","Petaya Berry","Choice Specs","White Herb","Choice Scarf"]),weight=352.74):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Dragon Pulse","Dark Pulse","Flamethrower","U-turn","Thunderbolt","Shadow Ball","Thunder Wave","Nasty Plot","Scale Shot","Tri Attack","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if name=="Hydreigon":
            ch=random.randint(1,5)
            if ch==5:
                moves=["Draco Meteor","Dark Pulse","Nasty Plot","Flash Cannon"]
                maxiv="Steel"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Volcarona
class Volcarona(Pokemon2):
    "Volcarona"
    def __init__(self,name="Volcarona",type1="Bug",type2="Fire",nature="None",level=100,happiness=255,hp=85,atk=60,defense=65,spatk=135,spdef=105,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flame Body","Swarm","Solar Power"]),item=random.choice(["Leftovers","Heavy-Duty Boots","Charti Berry"]),weight=101.41):
        color="red"
        if move =="None":
            avmoves=["Protect","Quiver Dance","Bug Buzz","Giga Drain","Heat Wave","Morning Sun","Skitter Smack"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Fiery Dance"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Cobalion
class Cobalion(Pokemon2):
    "Cobalion"
    def __init__(self,name="Cobalion",type1="Steel",type2="Fighting",nature="None",level=100,happiness=255,hp=91,atk=90,defense=129,spatk=90,spdef=72,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Justified","Sharpness"]),item=random.choice(["Leftovers"]),weight=551.16):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Swords Dance","Sacred Sword","Superpower","Close Combat","Iron Head"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Terrakion
class Terrakion(Pokemon2):
    "Terrakion"
    def __init__(self,name="Terrakion",type1="Rock",type2="Fighting",nature="None",level=100,happiness=255,hp=91,atk=129,defense=90,spatk=72,spdef=90,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Justified","Sharpness"]),item=random.choice(["Leftovers","Salac Berry"]),weight=573.2):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Swords Dance","Sacred Sword","Earthquake","Close Combat","Stone Edge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Virizion
class Virizion(Pokemon2):
    "Virizion"
    def __init__(self,name="Virizion",type1="Grass",type2="Fighting",nature="None",level=100,happiness=255,hp=91,atk=90,defense=72,spatk=90,spdef=129,speed=108,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Justified","Sharpness"]),item="Leftovers",weight=440.92):
        color="green"
        if move =="None":
            avmoves=["Protect","Swords Dance","Sacred Sword","Giga Drain","Close Combat","Leaf Blade","Solar Blade"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Tornadus
class Tornadus(Pokemon2):
    "Tornadus"
    def __init__(self,name="Tornadus",type1="Flying",type2="None",nature="None",level=100,happiness=255,hp=79,atk=115,defense=70,spatk=125,spdef=80,speed=111,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Prankster","Defiant"]),item="Leftovers",weight=138.89):
        color="green"
        if move =="None":
            avmoves=["Protect","Hurricane","Air Slash","Extrasensory"]
            moves=moveset(type1,type2,avmoves,2,name=name)+["Bleakwind Storm","Tailwind"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        #Thundurus
class Thundurus(Pokemon2):
    "Thundurus"
    def __init__(self,name="Thundurus",type1="Electric",type2="Flying",nature="None",level=100,happiness=255,hp=79,atk=115,defense=70,spatk=125,spdef=80,speed=111,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Prankster","Defiant"]),item="Leftovers",weight=134.48):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Thunder","Nasty Plot","Extrasensory","Thunder Wave"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Wildbolt Storm"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Malevorus
class Malevorus(Pokemon2):
    def __init__(self,name="Malvorus",type1="Dark",type2="Flying",nature="None",level=100,happiness=255,hp=80,atk=115,defense=70,spatk=135,spdef=80,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Prankster",item="Leftovers",weight=100):
        if move =="None":
            avmoves=["Protect","Night Daze","Wildbolt Storm","Nasty Plot","Extrasensory","Springtide Storm","Sandsear Storm","Bleakwind Storm"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)             
#Malevorus
class TMalevorus(Pokemon2):
    def __init__(self,name="Therian Malvorus",type1="Dark",type2="Flying",nature="None",level=100,happiness=255,hp=70,atk=135,defense=80,spatk=105,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Defiant",item="Leftovers",weight=100):
        if move =="None":
            avmoves=["Protect","Night Daze","Crunch","Dragon Dance","Night Slash","Dark Void","Dragon Claw","Sky Attack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                               
#Landorus
class Landorus(Pokemon2):
    "Landorus"
    def __init__(self,name="Landorus",type1="Ground",type2="Flying",nature="None",level=100,happiness=255,hp=89,atk=125,defense=90,spatk=115,spdef=80,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sand Force","Sheer Force"]),item=random.choice(["Leftovers"]),weight=149.91):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Earth Power","Air Slash","Extrasensory"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Sandsear Storm",]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Therian Tornadus
class TTornadus(Pokemon2):
    "Therian Tornadus"
    def __init__(self,name="Therian Tornadus",type1="Flying",type2="None",nature="None",level=100,happiness=255,hp=79,atk=100,defense=80,spatk=110,spdef=90,speed=121,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Regenerator",item="Leftovers",weight=138.89):
        color="green"
        if move =="None":
            avmoves=["Protect","Hurricane","Bleakwind Storm","Air Slash","Extrasensory","Tailwind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                   
#Therian Thundurus
class TThundurus(Pokemon2):
    "Therian Thundurus"
    def __init__(self,name="Therian Thundurus",type1="Electric",type2="Flying",nature="None",level=100,happiness=255,hp=79,atk=105,defense=70,spatk=145,spdef=80,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Volt Absorb",item=random.choice(["Leftovers","Life Orb","Assault Vest"]),weight=134.48):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Thunder","Wildbolt Storm","Nasty Plot","Extrasensory","Hidden Power","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Therian Landorus
class TLandorus(Pokemon2):
    "Therian Landorus"
    def __init__(self,name="Therian Landorus",type1="Ground",type2="Flying",nature="None",level=100,happiness=255,hp=89,atk=145,defense=90,spatk=105,spdef=80,speed=91,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Intimidate",item=random.choice(["Leftovers","Choice Scarf","Focus Sash","Earth Plate","Lum Berry","Yache Berry"]),weight=149.91):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Earthquake","Sandsear Storm","U-turn","Stone Edge","Swords Dance","Stealth Rock","Hidden Power","Explosion"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Reshiram
class Reshiram(Pokemon2):
    "Reshiram"
    def __init__(self,name="Reshiram",type1="Dragon",type2="Fire",nature="None",level=100,happiness=255,hp=100,atk=120,defense=100,spatk=150,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Turboblaze",item="Leftovers",weight=727.53):
        color="red"
        if move =="None":
            avmoves=["Protect","Blue Flare","Fusion Flare","Dragon Pulse"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Zekrom
class Zekrom(Pokemon2):
    "Zekrom"
    def __init__(self,name="Zekrom",type1="Dragon",type2="Electric",nature="None",level=100,happiness=255,hp=100,atk=150,defense=120,spatk=120,spdef=100,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Teravolt",item=random.choice(["Leftovers","Lum Berry","Shuca Berry"]),weight=760.59):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Bolt Strike","Fusion Bolt","Dragon Claw"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Kyurem
class Kyurem(Pokemon2):
    "Kyurem"
    def __init__(self,name="Kyurem",type1="Dragon",type2="Ice",nature="None",level=100,happiness=255,hp=125,atk=130,defense=90,spatk=130,spdef=90,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Refrigerate","Absolute Zero","Pressure"]),item="Leftovers",weight=716.5):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Outrage","Sheer Cold","Scale Shot","Ice Beam","Blizzard","Ancient Power","Dragon Pulse","Freeze-Dry","Hyper Voice"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Glaciate"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #White Kyurem
class WKyurem(Pokemon2):
    "White Kyurem"
    def __init__(self,name="White Kyurem",type1="Dragon",type2="Ice",nature="None",level=100,happiness=255,hp=125,atk=120,defense=90,spatk=170,spdef=100,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Turboblaze",item="Leftovers",weight=716.5):
        if move =="None":
            avmoves=["Blue Flare","Fusion Flare","Dragon Pulse","Ice Burn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
        #Black Kyurem 
class BKyurem(Pokemon2):
    "Black Kyurem"
    def __init__(self,name="Black Kyurem",type1="Dragon",type2="Ice",nature="None",level=100,happiness=255,hp=125,atk=170,defense=100,spatk=120,spdef=90,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Teravolt",item="Leftovers",weight=716.5):
        if move =="None":
            avmoves=["Freeze Shock","Fusion Bolt","Dragon Claw","Bolt Strike"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
        #Keldeo
class Keldeo(Pokemon2):
    "Keldeo"
    def __init__(self,name="Keldeo",type1="Water",type2="Fighting",nature="None",level=100,happiness=255,hp=91,atk=72,defense=90,spatk=129,spdef=90,speed=108,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Justified","Sharpness"]),item="Leftovers",weight=106.92):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Sacred Sword","Hydro Pump","Close Combat"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Secret Sword"]
        else:
            moves=move
        if "Secret Sword" in moves:
            name="Resolute "+name
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                       
        #Meloetta
class Meloetta(Pokemon2):
    "Meloetta"
    def __init__(self,name="Meloetta",type1="Normal",type2="Psychic",nature="None",level=100,happiness=255,hp=100,atk=77,defense=77,spatk=128,spdef=128,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Serene Grace",item="Leftovers",weight=14.33):
        color="green"
        if move =="None":
            avmoves=["Protect","U-turn","Psychic","Relic Song","Close Combat","Perish Song"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Pirouette Meloetta
class PMeloetta(Pokemon2):
    "Meloetta"
    def __init__(self,name="Pirouette Meloetta",type1="Normal",type2="Fighting",nature="None",level=100,happiness=255,hp=100,atk=128,defense=90,spatk=77,spdef=77,speed=128,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Serene Grace",item="Leftovers",weight=14.33):
        color="red"
        if move =="None":
            avmoves=["Protect","U-turn","Psychic","Relic Song","Close Combat"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Genesect
class Genesect(Pokemon2):
    "Genesect"
    def __init__(self,name="Genesect",type1="Bug",type2="Steel",nature="None",level=100,happiness=255,hp=71,atk=120,defense=95,spatk=120,spdef=95,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Download",item=random.choice(["Burn Drive","Chill Drive","Douse Drive","Shock Drive","Choice Scarf"]),weight=181.88):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Bug Buzz","Iron Head","X-Scissor","Flash Cannon","Metal Sound"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Techno Blast"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Delphox
class Delphox(Pokemon2):
    "Delphox"
    def __init__(self,name="Delphox",type1="Fire",type2="Psychic",nature="None",level=100,happiness=255,hp=75,atk=69,defense=72,spatk=114,spdef=100,speed=104,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Blaze","Magic Guard","Magician"]),item=random.choice(["Leftovers","Salac Berry"]),weight=85.98):
        color="red"
        if move =="None":
            avmoves=["Protect","Fire Blast","Flamethrower","Psychic","Mystical Fire","Shadow Ball","Blast Burn","Nasty Plot","Focus Blast","Torch Song","Future Sight"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Chesnaught
class Chesnaught(Pokemon2):
    "Chesnaught"
    def __init__(self,name="Chesnaught",type1="Grass",type2="Fighting",nature="None",level=100,happiness=255,hp=88,atk=107,defense=122,spatk=74,spdef=75,speed=64,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Overgrow","Iron Barbs","Bulletproof"]),item=random.choice(["Leftovers","Rocky Helmet","Salac Berry","Expert Belt"]),weight=198.42):
        color="green"
        if move =="None":
            avmoves=["Hammer Arm","Wood Hammer","Bulk Up","Seed Bomb","Close Combat","Frenzy Plant","Spiky Shield","Body Press","Belly Drum","Needle Arm","Drain Punch","Leech Seed","Spikes","Roar","Taunt","Synthesis","Superpower","Stone Edge","Substitute"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Greninja
class Greninja(Pokemon2):
    "Greninja"
    def __init__(self,name="Greninja",type1="Water",type2="Dark",nature="None",level=100,happiness=255,hp=72,atk=95,defense=67,spatk=103,spdef=71,speed=122,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Protean","Battle Bond","Torrent"]),item=random.choice(["Life Orb","Choice Specs"]),weight=88.18):
        color="blue"
        if move =="None":
            avmoves=["Water Shuriken","Dark Pulse","Hydro Pump","Extrasensory","Grass Knot","Hydro Cannon","Poison Jab","Ice Beam","Double Team"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if name=="Greninja":
            ch=random.randint(1,5)
            if ch==5:
                name+=" the Unrivaled"
                ability="Torrent"
                moves=["Toxic Spikes","Double Team","Hydro Pump","Night Slash"]
                maxiv="Poison"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Meowscarada
class Meowscarada(Pokemon2):
    def __init__(self,name="Meowscarada",type1="Grass",type2="Dark",nature="None",level=100,happiness=255,hp=76,atk=110,defense=70,spatk=81,spdef=70,speed=123,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Protean","Overgrow"]),item=random.choice(["Life Orb","Expert Belt"]),weight=68.78):
        color="green"
        if move =="None":
            avmoves=["Razor Leaf","Night Slash","Extrasensory","Grass Knot","Power Whip","Poison Jab","Play Rough","Double Team","Pollen Puff","Knock Off","U-turn","Spikes"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Flower Trick"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                
#Talonflame
class Talonflame(Pokemon2):
    "Talonflame"
    def __init__(self,name="Talonflame",type1="Fire",type2="Flying",nature="None",level=100,happiness=255,hp=78,atk=91,defense=71,spatk=74,spdef=69,speed=126,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flame Body","Gale Wings"]),item="Charti Berry",weight=54.01):
        color="red"
        if move =="None":
            avmoves=["Protect","Heat Wave","Sky Attack","Brave Bird","Flare Blitz","Roost","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Pyroar
class Pyroar(Pokemon2):
    "Pyroar"
    def __init__(self,name="Pyroar",type1="Fire",type2="Normal",nature="None",level=100,happiness=255,hp=86,atk=68,defense=72,spatk=109,spdef=66,speed=106,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Moxie","Adaptability","Unnerve"]),item=random.choice(["Leftovers","Choice Specs"]),weight=179.68):
        color="red"
        if move =="None":
            avmoves=["Protect","Heat Wave","Fire Blast","Flamethrower","Flare Blitz","Overheat","Hyper Voice","Hidden Power","Scorching Sands","Dark Pulse"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                                                                                           
#Florges
class Florges(Pokemon2):
    "Florges"
    def __init__(self,name="Florges",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=78,atk=65,defense=68,spatk=112,spdef=154,speed=75,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Misty Surge","Natural Cure"]),item="Leftovers",weight=22.05):
        color=random.choice(["white","cyan","blue","red","yellow","magenta"])
        if move =="None":
            avmoves=["Protect","Moonblast","Petal Blizzard","Grass Knot","Dazzling Gleam","Synthesis","Grassy Terrain","Misty Terrain","Pollen Puff"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Eternal Floette
class EFloette(Pokemon2):
    "Floette"
    def __init__(self,name="Eternal Floette",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=74,atk=65,defense=67,spatk=125,spdef=128,speed=92,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Misty Terrain",item="Leftovers",weight=1.98):
        color="red"
        if move =="None":
            avmoves=["Protect","Moonblast","Petal Blizzard","Grass Knot","Light of Ruin","Synthesis","Grassy Terrain","Misty Terrain"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
        #Gogoat
class Gogoat(Pokemon2):
    "Gogoat"
    def __init__(self,name="Gogoat",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=123,atk=100,defense=72,spatk=67,spdef=87,speed=74,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sap Sipper","Grass Pelt","Grassy Surge"]),item="Leftovers",weight=200.62):
        color="green"
        if move =="None":
            avmoves=["Leaf Blade","Wood Hammer","Bulk Up","Seed Bomb","Milk Drink","Horn Leech","Leech Seed","Grassy Glide","Toxic"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Pangoro
class Pangoro(Pokemon2):
    "Pangoro"
    def __init__(self,name="Pangoro",type1="Fighting",type2="Dark",nature="None",level=100,happiness=255,hp=95,atk=124,defense=78,spatk=69,spdef=71,speed=58,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Scrappy","Mold Breaker","Iron Fist"]),item="Leftovers",weight=299.83):
        color="red"
        if move =="None":
            avmoves=["Hammer Arm","Parting Shot","Bulk Up","Crunch","Close Combat","Night Slash","Grass Knot","Darkest Lariat","Wicked Blow","Storm Throw"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Aegislash
class Aegislash(Pokemon2):
    "Aegislash"
    def __init__(self,name="Aegislash",type1="Steel",type2="Ghost",nature="None",level=100,happiness=255,hp=60,atk=50,defense=140,spatk=50,spdef=140,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Stance Change",item="Leftovers", shield=True,sword=False,weight=116.84):
        if move =="None":
            avmoves=["King's Shield","Sacred Sword","Shadow Sneak","Iron Head"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        self.shield=shield
        self.sword=sword
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Gholdengo
class Gholdengo(Pokemon2):
    def __init__(self,name="Gholdengo",type1="Steel",type2="Ghost",nature="None",level=100,happiness=255,hp=87,atk=60,defense=95,spatk=133,spdef=91,speed=84,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Good as Gold",item=random.choice(["Leftovers","Choice Specs","Covert Cloak","Air Balloon"]),weight=66.14):
        color="yellow"
        if move =="None":
            avmoves=["Focus Blast","Nasty Plot","Shadow Ball","Power Gem","Recover"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Make It Rain"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Malamar
class Malamar(Pokemon2):
    "Malamar"
    def __init__(self,name="Malamar",type1="Dark",type2="Psychic",nature="None",level=100,happiness=255,hp=86,atk=92,defense=88,spatk=68,spdef=75,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Contrary","Infiltrator","Suction Cups"]),item="Leftovers",weight=103.62):
        color="magenta"
        if move =="None":
            avmoves=["Superpower","Psycho Cut","Shadow Sneak","Night Slash","Hypnosis","Psycho Boost","Destiny Bond","Payback"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Barbaracle
class Barbaracle(Pokemon2):
    "Barbaracle"
    def __init__(self,name="Barbaracle",type1="Rock",type2="Water",nature="None",level=100,happiness=255,hp=72,atk=105,defense=115,spatk=54,spdef=86,speed=68,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Tough Claws","Sniper","Infiltrator"]),item=random.choice(["Leftovers","Shuca Berry"]),weight=211.64):
        color="yellow"
        if move =="None":
            avmoves=["Superpower","Shell Smash","Razor Shell","Stone Edge","Cross Chop","Meteor Beam","Accelerock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Dragalge
class Dragalge(Pokemon2):
    "Dragalge"
    def __init__(self,name="Dragalge",type1="Poison",type2="Dragon",nature="None",level=100,happiness=255,hp=65,atk=75,defense=90,spatk=97,spdef=123,speed=44,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Poison Touch","Adaptability"]),item=random.choice(["Leftovers","Black Sludge","Safety Googles"]),weight=179.68):
        color="magenta"
        if move =="None":
            avmoves=["Hydro Pump","Sludge Bomb","Outrage","Dragon Pulse","Sludge Wave","Scale Shot","Double Team","Draco Meteor","Toxic Spikes"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Clawitzer
class Clawitzer(Pokemon2):
    "Clawitzer"
    def __init__(self,name="Clawitzer",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=71,atk=73,defense=88,spatk=120,spdef=89,speed=72,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Mega Launcher","Shell Armor"]),item="Leftovers",weight=77.82):
        color="blue"
        if move =="None":
            avmoves=["Hydro Pump","Aura Sphere","Dark Pulse","Dragon Pulse","Sludge Wave","Origin Pulse","Snipe Shot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Tyrantrum
class Tyrantrum(Pokemon2):
    "Tyrantrum"
    def __init__(self,name="Tyrantrum",type1="Rock",type2="Dragon",nature="None",level=100,happiness=255,hp=82,atk=121,defense=119,spatk=69,spdef=59,speed=71,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Rock Head","Strong Jaw"]),item=random.choice(["Leftovers","Lum Berry"]),weight=595.25):
        color="red"
        if move =="None":
            avmoves=["Giga Impact","Head Smash","Earthquake","Stone Edge","Dragon Claw","Meteor Beam","Scale Shot","Accelerock","Crunch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Aurorus
class Aurorus(Pokemon2):
    "Aurorus"
    def __init__(self,name="Aurorus",type1="Rock",type2="Ice",nature="None",level=100,happiness=255,hp=123,atk=77,defense=72,spatk=99,spdef=92,speed=58,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Refrigerate","Snow Warning"]),item="Leftovers",weight=496.04):
        color="cyan"
        if move =="None":
            avmoves=["Giga Impact","Blizzard","Ice Beam","Stone Edge","Freeze-Dry","Light Screen","Meteor Beam","Diamond Storm","Boomburst","Avalanche","Aurora Veil"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Hawlucha
class Hawlucha(Pokemon2):
    "Hawlucha"
    def __init__(self,name="Hawlucha",type1="Fighting",type2="Flying",nature="None",level=100,happiness=255,hp=78,atk=92,defense=75,spatk=74,spdef=63,speed=118,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Limber","Mold Breaker","Unburden"]),item=random.choice(["Leftovers","Flying Gem","Fighting Gem","Rocky Helmet"]),weight=47.4):
        color="red"
        if move =="None":
            avmoves=["Protect","Sky Attack","Roost","Brave Bird","Close Combat","U-turn","High Jump Kick","Flying Press","Swords Dance","Taunt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Goodra
class Goodra(Pokemon2):
    "Goodra"
    def __init__(self,name="Goodra",type1="Dragon",type2="None",nature="None",level=100,happiness=255,hp=90,atk=100,defense=70,spatk=110,spdef=150,speed=80,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sap Sipper","Gooey"]),item=random.choice(["Assault Vest","Leftovers"]),weight=331.8):
        color="magenta"
        if move =="None":
            avmoves=["Power Whip","Body Slam","Hydro Pump","Rain Dance","Dragon Pulse","Protect","Dragon Hammer","Draco Barrage"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Hisuian Goodra
class HGoodra(Pokemon2):
    "Hisuian Goodra"
    def __init__(self,name="Hisuian Goodra",type1="Dragon",type2="Steel",nature="None",level=100,happiness=255,hp=80,atk=100,defense=100,spatk=110,spdef=150,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sap Sipper","Gooey","Shell Armor"]),item=random.choice(["Assault Vest","Leftovers","Choice Specs"]),weight=736.6):
        color="magenta"
        if move =="None":
            avmoves=["Power Whip","Body Slam","Hydro Pump","Shelter","Dragon Pulse","Protect","Steel Beam","Draco Meteor","Flash Cannon","Flamethrower","Fire Blast","Drahon Tail","Body Press"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Trevenant
class Trevenant(Pokemon2):
    "Trevenant"
    def __init__(self,name="Trevenant",type1="Ghost",type2="Grass",nature="None",level=100,happiness=255,hp=85,atk=120,defense=82,spatk=65,spdef=82,speed=56,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Natural Cure","Harvest"]),item=random.choice(["Leftovers","Sitrus Berry"]),weight=156.53):
        color="green"
        if move =="None":
            avmoves=["Leech Seed","Wood Hammer","Shadow Claw","Will-O-Wisp","Horn Leech","Phantom Force","Forest's Curse","Destiny Bond","Poltergeist"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                         
        #Gourgeist
class Gourgeist(Pokemon2):
    "Gourgeist"
    def __init__(self,name="Gourgeist",type1="Ghost",type2="Grass",nature="None",level=100,happiness=255,hp=58,atk=100,defense=122,spatk=85,spdef=75,speed=54,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Frisk","Flare Boost"]),item="Leftovers",weight=27.56):
        color="yellow"
        if move =="None":
            avmoves=["Leech Seed","Bullet Seed","Shadow Claw","Will-O-Wisp","Razor Leaf","Phantom Force","Trick-or-Treat","Destiny Bond","Pain Split","Poltergeist"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Flare Boost":
            item="Flame Orb"
        name=random.choice(["Small","Large","Super"])+" "+name
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Hisuian Avalugg
class HAvalugg(Pokemon2):
    "Avalugg"
    def __init__(self,name="Hisuian Avalugg",type1="Ice",type2="Rock",nature="None",level=100,happiness=255,hp=95,atk=127,defense=184,spatk=34,spdef=36,speed=38,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sturdy","Strong Jaw","Ice Body"]),item="Leftovers", weight=578.5):
        color="cyan"
        if move =="None":
            avmoves=["Mountain Gale","Ice Shard","Icicle Crash","Stone Edge","Earthquake","Iron Defense","Accelerock","Avalanche","Crunch","Ice Fang"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Avalugg
class Avalugg(Pokemon2):
    "Avalugg"
    def __init__(self,name="Avalugg",type1="Ice",type2="None",nature="None",level=100,happiness=255,hp=95,atk=117,defense=184,spatk=44,spdef=46,speed=28,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Fliter","Sturdy","Ice Body"]),item=random.choice(["Leftovers","Heavy-Duty Boots"]),weight=1113.33):
        color="cyan"
        if move =="None":
            avmoves=["Mountain Gale","Ice Shard","Icicle Crash","Earthquake","Iron Defense","Recover","Skull Bash","Body Press","Rapid Spin","Avalanche"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Noivern
class Noivern(Pokemon2):
    "Noivern"
    def __init__(self,name="Noivern",type1="Flying",type2="Dragon",nature="None",level=100,happiness=255,hp=85,atk=70,defense=80,spatk=102,spdef=80,speed=123,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Infiltrator","Frisk","Aerilate"]),item=random.choice(["Leftovers","Choice Scarf"]),weight=187.39):
        color="blue"
        if move =="None":
            avmoves=["Boomburst","Hurricane","Roost","Dragon Pulse","Air Slash","Hyper Voice","Flamethrower","U-turn","Draco Meteor","Aeroblast","Taunt","Double Team","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                                             
#Xerneas
class Xerneas(Pokemon2):
    "Xerneas"
    def __init__(self,name="Xerneas",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=126,atk=131,defense=95,spatk=131,spdef=98,speed=99,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Fairy Aura",item="Power Herb",weight=473.99):
        color="blue"
        if move =="None":
            avmoves=["Moonblast","Thunder","Flamethrower","Focus Blast"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Geomancy"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Yveltal
class Yveltal(Pokemon2):
    "Yveltal"
    def __init__(self,name="Yveltal",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=126,atk=131,defense=95,spatk=131,spdef=98,speed=99,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Dark Aura",item=random.choice(["Leftovers","Lum Berry","Charti Berry"]),weight=447.54):
        color="red"
        if move =="None":
            avmoves=["Dark Pulse","Thunder","Sucker Punch","Focus Blast","Dark Hole","Razor Wind"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Oblivion Wing"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Complete Zygarde
class CZygarde(Pokemon2):
    "Zygarde"
    def __init__(self,name="Zygarde",type1="Dragon",type2="Ground",nature="None",level=100,happiness=255,hp=108,atk=100,defense=121,spatk=81,spdef=95,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Power Construct","Aura Break"]),item="Leftovers",weight=672.41):
        color="green"
        if move =="None":
            avmoves=["Land's Wrath","Thousand Arrows","Core Enforcer","Earthquake","Coil","Thousand Waves","Outrage","Crunch","Dragon Dance","Dragon Tail","Glare","Toxic","Rest"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Klefki
class Klefki(Pokemon2):
    "Klefki"
    def __init__(self,name="Klefki",type1="Steel",type2="Fairy",nature="None",level=100,happiness=255,hp=57,atk=80,defense=91,spatk=80,spdef=87,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Prankster",item="Leftovers",weight=6.61):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Foul Play","Play Rough","Flash Cannon","Toxic","Spikes","Metal Sound"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Diancie
class Diancie(Pokemon2):
    "Diancie"
    def __init__(self,name="Diancie",type1="Rock",type2="Fairy",nature="None",level=100,happiness=255,hp=50,atk=100,defense=150,spatk=100,spdef=150,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Clear Body",item=random.choice(["Leftovers","Diancite"]),weight=19.4):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Play Rough","Moonblast","Stealth Rock","Meteor Beam","Earth Power"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Diamond Storm"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  

                   
#Hoopa Unbound 
class UHoopa(Pokemon2):
    "Hoopa Unbound"
    def __init__(self,name="Hoopa Unbound",type1="Psychic",type2="Dark",nature="None",level=100,happiness=255,hp=80,atk=160,defense=60,spatk=170,spdef=130,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Magician",item=random.choice(["Leftovers","Salac Berry"]),weight=1080.27):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Hyperspace Fury","Psychic","Dark Pulse","Shadow Ball","Hyperspace Hole","Dark Hole","Drain Punch","Knock Off"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Volcanion
class Volcanion(Pokemon2):
    "Volcanion"
    def __init__(self,name="Volcanion",type1="Fire",type2="Water",nature="None",level=100,happiness=255,hp=80,atk=110,defense=120,spatk=130,spdef=90,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Water Absorb","Steam Engine"]),item=random.choice(["Leftovers","Shuca Berry"]),weight=429.9):
        color="red"
        if move =="None":
            avmoves=["Protect","Steam Eruption","Flare Blitz","Overheat","Hydro Pump","Heat Wave","Earth Power","Fire Spin"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                       
         #Decidueye
class Decidueye(Pokemon2):
    "Decidueye"
    def __init__(self,name="Decidueye",type1="Grass",type2="Ghost",nature="None",level=100,happiness=255,hp=78,atk=107,defense=75,spatk=95,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Overgrow","Tinted Lens","Long Reach"]),item="Leftovers",weight=80.69):
        color="green"
        if move =="None":
            avmoves=["U-turn","Shadow Claw","Brave Bird","Leaf Blade","Shadow Sneak","Sucker Punch","Poltergeist"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Spirit Shackle"]
        else:
            moves=move
        if name=="Decidueye":
            ch=random.randint(1,5)
            if ch==5:
                name+=" the Unrivaled"
                ability="Long Reach"
                moves=["Brave Bird","Low Kick","Spirit Shackle","Leaf Blade"]
                maxiv="Flying"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Hisuian Decidueye
class HDecidueye(Pokemon2):
    "Hisuian Decidueye"
    def __init__(self,name="Hisuian Decidueye",type1="Grass",type2="Fighting",nature="None",level=100,happiness=255,hp=88,atk=112,defense=80,spatk=95,spdef=95,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Scrappy","Overgrow","Quill Rush","Long Reach"]),item="Leftovers",weight=81.6):
        color="red"
        if move =="None":
            avmoves=["Triple Arrows","U-turn","Aura Sphere","Brave Bird","Leaf Blade","Close Combat","Roost"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Incineroar
class Incineroar(Pokemon2):
    "Incineroar"
    def __init__(self,name="Incineroar",type1="Fire",type2="Dark",nature="None",level=100,happiness=255,hp=95,atk=115,defense=90,spatk=80,spdef=90,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Blaze"]),item="Leftovers",weight=182.98):
        color="red"
        if move =="None":
            avmoves=["Throat Chop","Flare Blitz","Parting Shot","Snarl","Cross Chop"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Darkest Lariat"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Primarina
class Primarina(Pokemon2):
    "Primarina"
    def __init__(self,name="Primarina",type1="Water",type2="Fairy",nature="None",level=100,happiness=255,hp=80,atk=74,defense=74,spatk=126,spdef=116,speed=60,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Liquid Voice","Torrent"]),item="Leftovers",weight=97):
        color="blue"
        if move =="None":
            avmoves=["Moonblast","Hyper Voice","Hydro Pump","Misty Terrain","Ice Beam","Perish Song"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Sparkling Aria"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Toucannon
class Toucannon(Pokemon2):
    "Toucannon"
    def __init__(self,name="Toucannon",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=90,atk=120,defense=75,spatk=75,spdef=75,speed=60,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sheer Force","Skill Link"]),item=random.choice(["Leftovers","Focus Sash"]),weight=56.32):
        if move =="None":
            avmoves=["Protect","Beak Blast","Roost","Brave Bird","Rock Blast","U-turn","Bullet Seed","Drill Peck","Boomburst","Swagger","Tailwind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Hisuian Electrode
class HElectrode(Pokemon2):
    "Hisuian Electrode"
    def __init__(self,name="Hisuian Electrode",type1="Electric",type2="Grass",nature="None",level=100,happiness=255,hp=60,atk=50,defense=70,spatk=80,spdef=80,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Static","Soundproof","Aftermath"]),item="Leftovers",weight=156.5):
        color="yellow"
        if move =="None":
            avmoves=["Chloroblast","Thunder","Thunderbolt","Thunder Wave","Energy Ball","Hyper Beam","Rest","Explosion"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Sneasler
class Sneasler(Pokemon2):
    "Sneasler"
    def __init__(self,name="Sneasler",type1="Poison",type2="Fighting",nature="None",level=100,happiness=255,hp=80,atk=130,defense=60,spatk=40,spdef=80,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Poison Touch","Pressure"]),item=random.choice(["Leftovers","Life Orb","Choice Band"]),weight=94.8):
        color="magenta"
        if move =="None":
            avmoves=["Dire Claw","Poison Jab","Close Combat","Swords Dance","X-Scissor","Bulk Up","Rest","Shadow Claw","Gunk Shot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Wyrdeer
class Wyrdeer(Pokemon2):
    "Wyrdeer"
    def __init__(self,name="Wyrdeer",type1="Normal",type2="Psychic",nature="None",level=100,happiness=255,hp=103,atk=105,defense=72,spatk=105,spdef=75,speed=65,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Intimidate","Fur Coat","Sap Sipper","Frisk"]),item=random.choice(["Leftovers","Normal Gem"]),weight=209.7):
        if move =="None":
            avmoves=["Psyshield Bash","Zen Headbutt","Double-Edge","Wild Charge","Megahorn","Rest","High Horsepower","Hyper Voice","Mystical Fire","Calm Mind","Psychic","Thrash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Vikavolt
class Vikavolt(Pokemon2):
    "Vikavolt"
    def __init__(self,name="Vikavolt",type1="Bug",type2="Electric",nature="None",level=100,happiness=255,hp=77,atk=70,defense=90,spatk=145,spdef=75,speed=43,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Levitate",item=random.choice(["Leftovers","Occa Berry"]),weight=99.21):
        color="blue"
        if move =="None":
            avmoves=["Protect","Thunderbolt","Thunder Wave","Zap Cannon","Energy Ball","Crunch","Bug Buzz","Thunder","Sticky Web","Roost","Skitter Smack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Midday Lycanroc
class MDLycanroc(Pokemon2):
    "Lycanroc"
    def __init__(self,name="Midday Lycanroc",type1="Rock",type2="None",nature="None",level=100,happiness=255,hp=75,atk=115,defense=65,spatk=55,spdef=65,speed=112,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sand Rush","Steadfast","Frisk"]),item=random.choice(["Leftovers","Shuca Berry","Life Orb","Choice Band"]),weight=55.12):
        if move =="None":
            avmoves=["Accelerock","Stone Edge","Crunch","Sucker Punch","Stealth Rock","Headlong Rush","Brick Break","Fire Fang","Swords Dance","Toxic","Psychic Fangs","Close Combat","Double Team","Drill Run"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Midnight Lycanroc
class MNLycanroc(Pokemon2):
    "Lycanroc"
    def __init__(self,name="Midnight Lycanroc",type1="Rock",type2="None",nature="None",level=100,happiness=255,hp=85,atk=115,defense=75,spatk=55,spdef=75,speed=82,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["No Guard","Frisk","Vital Spirit"]),item=random.choice(["Leftovers","Shuca Berry","Life Orb","Choice Scarf"]),weight=55.12):
        color="red"
        if move =="None":
            avmoves=["Accelerock","Stone Edge","Crunch","Close Combat","Stealth Rock","Precipice Blades","Head Smash","Rock Polish","Swords Dance","Play Rough","Stomping Tantrum","Fire Punch","Toxic","Sucker Punch","Double Team"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Dusk Lycanroc
class DLycanroc(Pokemon2):
    "Lycanroc"
    def __init__(self,name="Dusk Lycanroc",type1="Rock",type2="None",nature="None",level=100,happiness=255,hp=75,atk=117,defense=75,spatk=55,spdef=65,speed=110,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=252,maxiv="No",move="None", ability="Tough Claws",item=random.choice(["Leftovers","Choice Band","Life Orb"]),weight=55.12):
        color="yellow"
        if move =="None":
            avmoves=["Accelerock","Stone Edge","Crunch","Sucker Punch","Stealth Rock","Drill Run","Fire Fang","Swords Dance","Psychic Fangs","Close Combat","Play Rough","Double Team"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #School Wishiwashi
class SWishiwashi(Pokemon2):
    "Wishiwashi"
    def __init__(self,name="Wishiwashi",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=55,atk=20,defense=20,spatk=25,spdef=25,speed=40,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Schooling",item="Leftovers",weight=0.66):
        color="cyan"
        if move =="None":
            avmoves=["Hydro Pump","Water Spout","Double-Edge","Soak","Rest","Rain Dance","Scald","Ice Beam","Earth Power","Scale Shot","Whirlpool"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Toxapex
class Toxapex(Pokemon2):
    "Toxapex"
    def __init__(self,name="Toxapex",type1="Poison",type2="Water",nature="None",level=100,happiness=255,hp=50,atk=63,defense=152,spatk=53,spdef=142,speed=35,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Regenerator","Merciless","Limber"]),item=random.choice(["Black Sludge","Rocky Helmet"]),weight=31.97):
        color="cyan"
        if move =="None":
            avmoves=["Baneful Bunker","Toxic","Liquidation","Toxic Spikes","Scald","Ice Beam","Recover","Chilling Water","Knock Off","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Mudsdale
class Mudsdale(Pokemon2):
    "Mudsdale"
    def __init__(self,name="Mudsdale",type1="Ground",type2="None",nature="None",level=100,happiness=255,hp=100,atk=125,defense=100,spatk=55,spdef=85,speed=35,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Stamina","Tangling Hair","Striker"]),item="Leftovers",weight=2028.25):
        color="red"
        if move =="None":
            avmoves=["High Horsepower","Stone Edge","Earthquake","Heavy Slam","Iron Defense","Slack Off"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Araquanid
class Araquanid(Pokemon2):
    "Araquanid"
    def __init__(self,name="Araquanid",type1="Water",type2="Bug",nature="None",level=100,happiness=255,hp=68,atk=70,defense=92,spatk=50,spdef=132,speed=42,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Water Absorb","Water Bubble"]),item="Leftovers",weight=180.78):
        color="green"
        if move =="None":
            avmoves=["Leech Life","Lunge","Liquidation","Crunch","Scald","Ice Beam","X-Scissor","Sticky Web","Aqua Ring","Skitter Smack","Aurora Beam","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Salazzle
class Salazzle(Pokemon2):
    "Salazzle"
    def __init__(self,name="Salazzle",type1="Poison",type2="Fire",nature="None",level=100,happiness=255,hp=68,atk=64,defense=60,spatk=111,spdef=60,speed=117,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Corrosion","Oblivious"]),item="Black Sludge",weight=48.94):
        color="magenta"
        if move =="None":
            avmoves=["Fire Lash","Toxic","Flamethrower","Toxic Spikes","Dragon Pulse","Nasty Plot","Sludge Bomb","Scale Shot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Salobber
class Salobber(Pokemon2):
    def __init__(self,name="Salobber",type1="Poison",type2="Fire",nature="None",level=100,happiness=255,hp=58,atk=111,defense=60,spatk=64,spdef=60,speed=127,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Corrosion",item="Black Sludge",weight=100):
        if move =="None":
            avmoves=["Fire Lash","Toxic","Flare Blitz","Toxic Spikes","Swords Dance","Sludge Bomb","Poison Jab","Fire Fang","Cross Poison"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                
#Bewear
class Bewear(Pokemon2):
    "Bewear"
    def __init__(self,name="Bewear",type1="Normal",type2="Fighting",nature="None",level=100,happiness=255,hp=120,atk=125,defense=80,spatk=55,spdef=60,speed=60,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Fluffy","Unnerve"]),item=random.choice(["Leftovers","Normal Gem"]),weight=297.62):
        color="magenta"
        if move =="None":
            avmoves=["Superpower","Double-Edge","Hammer Arm","Strength","High Horsepower","Zen Headbutt","Darkest Lariat","Pain Split","Thrash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Tsareena
class Tsareena(Pokemon2):
    "Tsareena"
    def __init__(self,name="Tsareena",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=72,atk=120,defense=98,spatk=50,spdef=98,speed=72,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Queenly Majesty","Striker"]),item="Leftovers",weight=47.18):
        color="magenta"
        if move =="None":
            avmoves=["Trop Kick","High Jump Kick","Power Whip","Play Rough","Grass Knot","U-turn","Triple Axel","Grav Apple"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Golisopod
class Golisopod(Pokemon2):
    "Golisopod"
    def __init__(self,name="Golisopod",type1="Bug",type2="Water",nature="None",level=100,happiness=255,hp=75,atk=125,defense=140,spatk=60,spdef=90,speed=40,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability="Tough Claws",item="Leftovers",weight=238.1):
        if move =="None":
            avmoves=["Leech Life","First Impression","Liquidation","Crunch","Swords Dance","Ice Beam","X-Scissor","Razor Shell","Sucker Punch","Skitter Smack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Palossand
class Palossand(Pokemon2):
    "Palossand"
    def __init__(self,name="Palossand",type1="Ghost",type2="Ground",nature="None",level=100,happiness=255,hp=85,atk=75,defense=110,spatk=100,spdef=75,speed=35,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability="Water Compaction",item=random.choice(["Leftovers","Sitrus Berry"]),weight=551.16):
        color="yellow"
        if move =="None":
            avmoves=["Shore Up","Earth Power","Shadow Ball","Giga Drain","Sandstorm","Sludge Bomb","Destiny Bond","Curse","Toxic","Scorching Sands","Stealth Rock","Strength Sap"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Silvally
class Silvally(Pokemon2):
    "Silvally"
    def __init__(self,name="Silvally",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=100,atk=100,defense=100,spatk=100,spdef=100,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["RKS System"]),item=random.choice(["Rock Memory","Fire Memory","Water Memory","Grass Memory","Electric Memory","Ground Memory","Flying Memory","Fighting Memory","Fairy Memory","Dragon Memory","Steel Memory","Poison Memory","Dark Memory","Ghost Memory","Normal Memory","Bug Memory","Ice Memory","Life Orb","Choice Band","Choice Scarf"]),weight=221.56):
        if move =="None":
            avmoves=["Protect","Hyper Beam","Double-Edge","Crush Claw","Parting Shot","Explosion","Thunder Wave","Swords Dance","Razor Wind"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Multi-Attack"]
        else:
            moves=move
        if "Memory" in item:
            type1=item.split(" ")[0]
        if type1!="Normal":
            name=name+f"({type1})"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Turtonator
class Turtonator(Pokemon2):
    "Turtonator"
    def __init__(self,name="Turtonator",type1="Fire",type2="Dragon",nature="None",level=100,happiness=255,hp=70,atk=58,defense=135,spatk=91,spdef=85,speed=36,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Dauntless Shield","Shell Armor"]),item=random.choice(["Leftovers","White Herb"]),weight=467.38):
        color="red"
        if move =="None":
            avmoves=["Shell Trap","Shell Smash","Overheat","Flamethrower","Dragon Pulse","Iron Defense","Scale Shot","Head Smash","Fire Spin"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Mimikyu
class Mimikyu(Pokemon2):
    "Mimikyu"
    def __init__(self,name="Mimikyu",type1="Ghost",type2="Fairy",nature="None",level=100,happiness=255,hp=55,atk=90,defense=80,spatk=50,spdef=105,speed=96,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Disguise",item=random.choice(["Leftovers","Lum Berry"]),weight=1.54):
        color="yellow"
        if move =="None":
            avmoves=["Shadow Sneak","Play Rough","Shadow Claw","Wood Hammer","Swords Dance","Destiny Bond","Pain Split","Double Team"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Drampa
class Drampa(Pokemon2):
    "Drampa"
    def __init__(self,name="Drampa",type1="Normal",type2="Dragon",nature="None",level=100,happiness=255,hp=103,atk=50,defense=85,spatk=135,spdef=91,speed=36,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Berserk","Sap Sipper","Fatal Precision"]),item="Leftovers",weight=407.86):
        color="yellow"
        if move =="None":
            avmoves=["Hyper Voice","Dragon Pulse","Extrasensory","Hyper Beam","Hurricane","Ice Beam","Energy Ball","Focus Blast","Heat Wave","Light Screen","Scale Shot","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Dhelmise
class Dhelmise(Pokemon2):
    "Delmise"
    def __init__(self,name="Dhelmise",type1="Ghost",type2="Grass",nature="None",level=100,happiness=255,hp=70,atk=131,defense=100,spatk=86,spdef=90,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Steelworker",item="Leftovers",weight=462.97):
        color="green"
        if move =="None":
            avmoves=["Power Whip","Phantom Force","Shadow Ball","Heavy Slam","Poltergeist"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Anchor Shot"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Kommo-o
class Kommo(Pokemon2):
    "Kommo-o"
    def __init__(self,name="Kommo-o",type1="Dragon",type2="Fighting",nature="None",level=100,happiness=255,hp=75,atk=110,defense=125,spatk=100,spdef=105,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Overcoat","Bulletproof","Soundproof"]),item=random.choice(["Throat Spray","Yache Berry","Salac Berry"]),weight=172.4):
        color="yellow"
        if move =="None":
            avmoves=["Hyper Voice","Dragon Pulse","Focus Blast","Aura Sphere","Flash Cannon","Scale Shot"]
            moves=moveset(type1,type2,avmoves,2,name=name)+["Clangorous Soul","Clanging Scales"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Tapu Koko
class Tapukoko(Pokemon2):
    "Tapu Koko"
    def __init__(self,name="Tapu Koko",type1="Electric",type2="Fairy",nature="None",level=100,happiness=255,hp=70,atk=115,defense=85,spatk=95,spdef=75,speed=130,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Electric Surge"]),item=random.choice(["Leftovers","Shuca Berry"]),weight=45.19):
        color="yellow"
        if move =="None":
            avmoves=["Nature's Madness","Wild Charge","Play Rough","Brave Bird","Thunder","Rising Voltage","Grass Knot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Tapu Lele
class Tapulele(Pokemon2):
    "Tapu Lele"
    def __init__(self,name="Tapu Lele",type1="Psychic",type2="Fairy",nature="None",level=100,happiness=255,hp=70,atk=85,defense=75,spatk=130,spdef=115,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Psychic Surge"]),item=random.choice(["Leftovers","Twisted Spoon"]),weight=41.01):
        color="magenta"
        if move =="None":
            avmoves=["Nature's Madness","Extrasensory","Moonblast","Psyshock","Psychic","Focus Blast","Hidden Power","Taunt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Tapu Bulu
class Tapubulu(Pokemon2):
    "Tapu Bulu"
    def __init__(self,name="Tapu Bulu",type1="Grass",type2="Fairy",nature="None",level=100,happiness=255,hp=70,atk=130,defense=115,spatk=85,spdef=95,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Grassy Surge"]),item=random.choice(["Leftovers","Life Orb"]),weight=100.31):
        color="red"
        if move =="None":
            avmoves=["Nature's Madness","Horn Leech","Play Rough","Wood Hammer","Zen Headbutt","Grassy Glide","Close Combat","Swords Dance"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                       
        #Tapu Fini
class Tapufini(Pokemon2):
    "Tapu Fini"
    def __init__(self,name="Tapu Fini",type1="Water",type2="Fairy",nature="None",level=100,happiness=255,hp=70,atk=75,defense=115,spatk=95,spdef=130,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Misty Surge"]),item=random.choice(["Leftovers","Focus Sash"]),weight=46.74):
        color="blue"
        if move =="None":
            avmoves=["Nature's Madness","Hydro Pump","Moonblast","Surf","Muddy Water","Misty Explosion","Flip Turn","Blizzard","Calm Mind","Ice Beam","Draining Kiss"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Solgaleo
class Solgaleo(Pokemon2):
    "Solgaleo"
    def __init__(self,name="Solgaleo",type1="Psychic",type2="Steel",nature="None",level=100,happiness=255,hp=137,atk=137,defense=107,spatk=113,spdef=89,speed=97,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Full Metal Body"]),item="Leftovers",weight=507.06):
        color="yellow"
        if move =="None":
            avmoves=["Sunsteel Strike","Flare Blitz","Solar Beam","Wild Charge","Morning Sun","Zen Headbutt","Meteor Beam","Steel Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Radiant Sun Solgaleo
class RSSolgaleo(Pokemon2):
    "Solgaleo"
    def __init__(self,name="Radiant Sun Solgaleo",type1="Psychic",type2="Steel",nature="None",level=100,happiness=255,hp=137,atk=157,defense=107,spatk=113,spdef=89,speed=97,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Full Metal Body"]),item="Leftovers",weight=100):
        color="yellow"
        if move =="None":
            avmoves=["Sunsteel Strike","Flare Blitz","Solar Beam","Wild Charge","Morning Sun","Zen Headbutt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Lunala
class Lunala(Pokemon2):
    "Lunala"
    def __init__(self,name="Lunala",type1="Psychic",type2="Ghost",nature="None",level=100,happiness=255,hp=137,atk=113,defense=89,spatk=157,spdef=107,speed=97,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Shadow Shield"]),item="Leftovers",weight=264.55):
        color="blue"
        if move =="None":
            avmoves=["Moongeist Beam","Phantom Force","Moonblast","Night Daze","Moonlight","Shadow Ball","Psychic","Meteor Beam","Esper Wing"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Full Moon Lunala
class FMLunala(Pokemon2):
    "Lunala"
    def __init__(self,name="Full Moon Lunala",type1="Psychic",type2="Ghost",nature="None",level=100,happiness=255,hp=137,atk=113,defense=89,spatk=137,spdef=107,speed=97,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Shadow Shield"]),item="Leftovers",weight=100):
        if move =="None":
            avmoves=["Moongeist Beam","Phantom Force","Moonblast","Night Daze","Moonlight","Shadow Ball","Psychic"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
        #Dusk Mane Necrozma
class DMNecrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Dusk Mane Necrozma",type1="Psychic",type2="Steel",nature="None",level=100,happiness=255,hp=97,atk=157,defense=127,spatk=113,spdef=109,speed=77,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Prism Armor"]),item="Weakness Policy",weight=1014.13):
        color="yellow"
        if move =="None":
            avmoves=["Sunsteel Strike","Flare Blitz","Solar Beam","Photon Geyser","Prismatic Laser","Morning Sun","Zen Headbutt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Dawn Wing Necrozma
class DWNecrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Dawn Wing Necrozma",type1="Psychic",type2="Ghost",nature="None",level=100,happiness=255,hp=97,atk=113,defense=109,spatk=157,spdef=127,speed=77,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Prism Armor"]),item="Weakness Policy",weight=771.62):
        color="cyan"
        if move =="None":
            avmoves=["Moongeist Beam","Shadow Ball","Moonblast","Photon Geyser","Prismatic Laser","Moonlight","Psychic"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Necrozma
class Necrozma(Pokemon2):
    "Necrozma"
    def __init__(self,name="Necrozma",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=97,atk=107,defense=101,spatk=127,spdef=89,speed=79,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Prism Armor"]),item="Weakness Policy",weight=507.06):
        color="red"
        if move =="None":
            avmoves=["Moonlight","Iron Defense","Rock Blast","Photon Geyser","Prismatic Laser","Morning Sun","Meteor Beam","Heat Wave","Psyshock","Stealth Rock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Meteor Beam" in moves:
            item="Power Herb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Nihilego
class Nihilego(Pokemon2):
    "Nihilego"
    def __init__(self,name="Nihilego",type1="Rock",type2="Poison",nature="None",level=100,happiness=255,hp=109,atk=53,defense=47,spatk=127,spdef=131,speed=103,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item="Leftovers",weight=122.36):
        color="cyan"
        if move =="None":
            avmoves=["Venom Drench","Iron Defense","Toxic Spikes","Stealth Rock","Venoshock","Power Gem","Meteor Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Buzzwole
class Buzzwole(Pokemon2):
    "Buzzwole"
    def __init__(self,name="Buzzwole",type1="Bug",type2="Fighting",nature="None",level=100,happiness=255,hp=107,atk=139,defense=139,spatk=53,spdef=53,speed=79,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item=random.choice(["Leftovers","Occa Berry"]),weight=735.46):
        color="red"
        if move =="None":
            avmoves=["Lunge","Superpower","Bulk Up","Fell Stinger","Power-up Punch","Close Combat","Drain Punch","Darkest Lariat"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Pheromosa
class Pheromosa(Pokemon2):
    "Pheromosa"
    def __init__(self,name="Pheromosa",type1="Rock",type2="Poison",nature="None",level=100,happiness=255,hp=71,atk=137,defense=37,spatk=137,spdef=37,speed=151,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item="Leftovers",weight=55.12):
        color="yellow"
        if move =="None":
            avmoves=["U-turn","Triple Axel","High Jump Kick","Quiver Dance","Bug Buzz","Lunge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                                                                                                                 #Xurkitree
class Xurkitree(Pokemon2):
    "Xurkitree"
    def __init__(self,name="Xurkitree",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=83,atk=69,defense=71,spatk=173,spdef=71,speed=98,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item=random.choice(["Leftovers","Life Orb","Air Balloon","Heavy-Duty Boots","Choice Scarf","Shuca Berry"]),weight=220.46):
        if move =="None":
            avmoves=["Eerie Impulse","Electric Terrain","Power Whip","Discharge","Hypnosis","Energy Ball","Dazzling Gleam","Volt Switch","Grass Knot","Hidden Power","Tail Glow"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Thunderbolt"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Celesteela
class Celesteela(Pokemon2):
    "Celesteela"
    def __init__(self,name="Celesteela",type1="Steel",type2="Flying",nature="None",level=100,happiness=255,hp=97,atk=101,defense=103,spatk=107,spdef=101,speed=61,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item=random.choice(["Leftovers","Weakness Policy","Occa Berry"]),weight=2204.4):
        color="green"
        if move =="None":
            avmoves=["Heavy Slam","Iron Defense","Leech Seed","Flash Cannon","Giga Drain","Meteor Beam","Flamethrower","Autotomize","Toxic","Air Slash","Fire Blast","Protect","Metal Sound"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Meteor Beam" in moves:
            item="Power Herb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Kartana
class Kartana(Pokemon2):
    "Kartana"
    def __init__(self,name="Kartana",type1="Grass",type2="Steel",nature="None",level=100,happiness=255,hp=59,atk=181,defense=131,spatk=59,spdef=31,speed=109,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item=random.choice(["Leftovers","Life Orb","Choice Band","Choice Scarf"]),weight=0.22):
        color="yellow"
        if move =="None":
            avmoves=["Swords Dance","Sacred Sword","Night Slash","Smart Strike","Knock Off","Defog"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Leaf Blade"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Guzzlord
class Guzzlord(Pokemon2):
    "Guzzlord"
    def __init__(self,name="Guzzlord",type1="Dark",type2="Dragon",nature="None",level=100,happiness=255,hp=203,atk=101,defense=73,spatk=97,spdef=73,speed=23,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item=random.choice(["Leftovers","Choice Band"]),weight=1957.70):
        color="red"
        if move =="None":
            avmoves=["Heavy Slam","Belch","Hammer Arm","Stomping Tantrum","Dragon Rush","Earthquake","Toxic","Protect","Dragon Tail","Rest","Heat Crash","Outrage","Draco Barrage"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Knock Off"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                       
#Magearna
class Magearna(Pokemon2):
    "Magearna"
    def __init__(self,name="Magearna",type1="Steel",type2="Fairy",nature="None",level=100,happiness=255,hp=80,atk=95,defense=115,spatk=130,spdef=115,speed=65,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Soul-Heart"]),item="Leftovers",weight=177.47):
        color="magenta"
        if move =="None":
            avmoves=["Pain Split","Zap Cannon","Flash Cannon","Aura Sphere","Steel Beam","Focus Blast","Ice Beam","Thunderbolt","Psychic","Energy Ball","Shadow Ball"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Fleur Cannon"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                                                                                                                 #Marshadow
class Marshadow(Pokemon2):
    "Marshadow"
    def __init__(self,name="Marshadow",type1="Fighting",type2="Ghost",nature="None",level=100,happiness=255,hp=90,atk=125,defense=80,spatk=90,spdef=90,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Technician"]),item=random.choice(["Leftovers","Life Orb","Spell Tag","Choice Band"]),weight=48.94):
        color="red"
        if move =="None":
            avmoves=["Superpower","Bulk Up","Drain Punch","Power-up Punch","Close Combat","Sucker Punch","Ice Punch","Rock Tomb","Poltergeist"]
            moves=moveset(type1,type2,avmoves,2,name=name)+["Spectral Thief","Shadow Sneak"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Naganadel
class Naganadel (Pokemon2):
    "Naganadel"
    def __init__(self,name="Naganadel",type1="Poison",type2="Dragon",nature="None",level=100,happiness=255,hp=73,atk=73,defense=73,spatk=127,spdef=73,speed=121,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item=random.choice(["Leftovers","Life Orb","Lum Berry"]),weight=330.69):
        color="magenta"
        if move =="None":
            avmoves=["Dragon Pulse","Nasty Plot","Dark Pulse","Venoshock","Heat Wave","Air Slash","Sludge Bomb","Hyper Beam","Draco Meteor","Fire Blast"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Sludge Wave"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
        #Stakataka
class Stakataka(Pokemon2):
    "Stakataka"
    def __init__(self,name="Stakataka",type1="Rock",type2="Steel",nature="None",level=100,happiness=255,hp=61,atk=131,defense=211,spatk=53,spdef=101,speed=13,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item=random.choice(["Leftovers","Shuca Berry"]),weight=1807.79):
        color="yellow"
        if move =="None":
            avmoves=["Iron Head","Iron Defense","Double-Edge","Stealth Rock","Heavy Slam","Rock Slide","Meteor Beam","Autotomize","Body Press","Heat Crash","Superpower"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Blacephalon
class Blacephalon(Pokemon2):
    "Blacephalon"
    def __init__(self,name="Blacephalon",type1="Fire",type2="Ghost",nature="None",level=100,happiness=255,hp=53,atk=127,defense=53,spatk=151,spdef=79,speed=107,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Beast Boost"]),item=random.choice(["Leftovers","Choice Specs"]),weight=28.66):
        if move =="None":
            avmoves=["Will-O-Wisp","Fire Blast","Shadow Ball","Mystical Fire","Light Screen","Solar Beam","Dark Pulse","Overheat","Calm Mind","Heat Wave","Psyshock","Psychic","Flamethrower","Hyper Beam","Hidden Power","Trick","Calm Mind"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Mind Blown"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Zeraora
class Zeraora(Pokemon2):
    "Zeraora"
    def __init__(self,name="Zeraora",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=88,atk=112,defense=75,spatk=102,spdef=80,speed=143,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Volt Absorb"]),item=random.choice(["Leftovers","Heavy-Duty Boots","Life Orb","Expert Belt","Shuca Berry","Air Balloon"]),weight=98.11):
        color="yellow"
        if move =="None":
            avmoves=["Close Combat","Wild Charge","Thunder Punch","Volt Switch","Power-up Punch","Aura Sphere","Bulk Up","Knock Off","Toxic","Grass Knot","Giga Impact"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Plasma Fists"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Melmetal
class Melmetal(Pokemon2):
    "Melmetal"
    def __init__(self,name="Melmetal",type1="Steel",type2="None",nature="None",level=100,happiness=255,hp=135,atk=143,defense=143,spatk=80,spdef=65,speed=34,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Iron Fist"]),item=random.choice(["Leftovers","Protective Pads","Choice Band","Assault Vest"]),weight=1763.7):
        if move =="None":
            avmoves=["Superpower","Thunder Punch","Ice Punch","Fire Punch","Iron Defense","Toxic","Earthquake"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Double Iron Bash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
                                                                                    #Galarian Rapidash
class GRapidash(Pokemon2):
    "Rapidash"
    def __init__(self,name="Galarian Rapidash",type1="Psychic",type2="Fairy",nature="None",level=100,happiness=255,hp=65,atk=100,defense=70,spatk=80,spdef=80,speed=125,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Reckless","Pastel Veil","Anticipation"]),item=random.choice(["Leftovers","Electric Seed","Kee Berry","Choice Band"]),weight=176.4):
        color="magenta"
        if move =="None":
            avmoves=["Megahorn","Psycho Cut","Play Rough","Drill Run","High Horsepower","Wild Charge","Flare Blitz","Expanding Force","Mystical Fire","Morning Sun","Stored Power","Calm Mind","Swords Dance","Future Sight"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
#Slowbro
class Slowbro(Pokemon2):
    "Slowbro"
    def __init__(self,name="Slowbro",type1="Water",type2="Psychic",nature="None",level=100,happiness=255,hp=95,atk=75,defense=110,spatk=100,spdef=80,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Regenerator","Own Tempo"]),item=random.choice(["Colbur Berry","Heavy-Duty Boots","Slowbronite","Apicot Berry","Shell Bell"]),weight=173.06):
        color="magenta"
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Hydro Pump","Thunderbolt","Iron Defense","Rain Dance","Rest","Expanding Force","Yawn","Future Sight","Psyshock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Slowbro
class GSlowbro(Pokemon2):
    "Slowbro"
    def __init__(self,name="Galarian Slowbro",type1="Poison",type2="Psychic",nature="None",level=100,happiness=255,hp=95,atk=75,defense=105,spatk=115,spdef=70,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Regenerator","Quick Draw","Own Tempo"]),item="Leftovers",weight=155.4):
        color="magenta"
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Sludge Bomb","Thunderbolt","Iron Defense","Rain Dance","Expanding Force","Chilling Water","Yawn","Future Sight"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Shell Side Arm"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Weezing
class GWeezing(Pokemon2):
    "Weezing"
    def __init__(self,name="Galarian Weezing",type1="Poison",type2="Fairy",nature="None",level=100,happiness=255,hp=65,atk=90,defense=120,spatk=85,spdef=70,speed=60,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Levitate","Misty Surge","Neutralizing Gas"]),item="Black Sludge",weight=35.3):
        color="green"
        if move =="None":
            avmoves=["Sludge Bomb","Toxic","Venoshock","Explosion","Toxic Spikes","Strange Steam","Misty Explosion","Pain Split","Will-O-Wisp"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)             
#Medicrow
class Medicrow(Pokemon2):
    def __init__(self,name="Medicrow",type1="Fairy",type2="Poison",nature="None",level=100,happiness=255,hp=65,atk=50,defense=60,spatk=125,spdef=70,speed=90,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Levitate","Misty Surge"]),item="Black Sludge",weight=100):
        if move =="None":
            avmoves=["Sludge Bomb","Toxic","Sludge Wave","Toxic Spikes","Dazzling Gleam","Moonblast","Roost"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                     
#Articuno
class GArticuno(Pokemon2):
    "Articuno"
    def __init__(self,name="Galarian Articuno",type1="Psychic",type2="Flying",nature="None",level=100,happiness=255,hp=90,atk=75,defense=95,spatk=125,spdef=100,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Competitive",item=random.choice(["Leftovers","Heavy-Duty Boots","Choice Specs"]),weight=112.2):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Hidden Power","Psychic","Extrasensory","Brave Bird","Sky Attack","Roost","Expanding Force","Aura Sphere","Hurricane","Recover","U-turn","Shadow Ball","Psyshock","Future Sight","Double Team","Snowscape"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Freezing Glare"]
        else:
            moves=move
        if "Snowscape" in moves:
            item="Icy Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Zapdos
class GZapdos(Pokemon2):
    "Zapdos"
    def __init__(self,name="Galarian Zapdos",type1="Fighting",type2="Flying",nature="None",level=100,happiness=255,hp=90,atk=125,defense=90,spatk=85,spdef=90,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Defiant","Striker","Tough Claws"]),item=random.choice(["Leftovers","Choice Band","Choice Scarf","Lum Berry","Charti Berry","Bright Powder"]),weight=128.3):
        color="red"
        if move =="None":
            avmoves=["Protect","Hidden Power","Brave Bird","Close Combat","Sky Attack","Roost","Bulk Up","Stomping Tantrum","U-turn","Blaze Kick"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Thunderous Kick"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)             
#Moltres
class GMoltres(Pokemon2):
    "Moltres"
    def __init__(self,name="Galarian Moltres",type1="Dark",type2="Flying",nature="None",level=100,happiness=255,hp=90,atk=85,defense=90,spatk=100,spdef=125,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Berserk",item=random.choice(["Leftovers","Weakness Policy","Life Orb","Lum Berry"]),weight=145.5):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Hidden Power","Hurricane","Nasty Plot","Sky Attack","Brave Bird","Sucker Punch","Roost","Tailwind","Rest","Air Slash","Agility","Rest","Scorching Sands","Sunny Day"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Fiery Wrath"]
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        if "Sunny Day" in moves:
            item="Heat Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Slowking
class GSlowking(Pokemon2):
    "Slowking"
    def __init__(self,name="Galarian Slowking",type1="Poison",type2="Psychic",nature="None",level=100,happiness=255,hp=95,atk=65,defense=80,spatk=110,spdef=110,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Curious Medicine",item=random.choice(["Leftovers","Icy Rock","Assault Vest"]),weight=175.3):
        color="magenta"
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Sludge Bomb","Thunderbolt","Iron Defense","Rain Dance","Toxic Spikes","Yawn","Future Sight"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Chilly Reception"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Rillaboom
class Rillaboom(Pokemon2):
    "Rillaboom"
    def __init__(self,name="Rillaboom",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=100,atk=125,defense=90,spatk=60,spdef=70,speed=85,hpev=0,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Grassy Surge","Overgrow"]),item=random.choice(["Choice Band","Life Orb","Grassy Seed"]),weight=198.4):
        color="green"
        if move =="None":
            avmoves=["Drum Beating","Wood Hammer","Grassy Glide","Swords Dance","Knock Off","Superpower","Acrobatics","High Horsepower","Drain Punch","U-turn","Darkest Lariat","Boomburst"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Cinderace
class Cinderace(Pokemon2):
    "Cinderace"
    def __init__(self,name="Cinderace",type1="Fire",type2="None",nature="None",level=100,happiness=255,hp=80,atk=116,defense=75,spatk=65,spdef=75,speed=119,hpev=80,atkev=164,defev=0,spatkev=0,spdefev=48,speedev=216,maxiv="No",move="None", ability=random.choice(["Libero","Blaze"]),item=random.choice(["Heavy-Duty Boots","Charcoal","Life Orb"]),weight=72.8):
        color="red"
        if move =="None":
            avmoves=["Court Change","U-turn","Sucker Punch","Gunk Shot","Zen Headbutt","High Jump Kick","Scorching Sands","Bounce"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Pyro Ball"]
        else:
            moves=move
        if name=="Cinderace":
            ch=random.randint(1,5)
            if ch==5:
                name+=" the Unrivaled"
                ability="Protean"
                moves=["High Jump Kick","Pyro Ball","Acrobatics","Iron Head"]
                maxiv="Fighting"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Inteleon
class Inteleon(Pokemon2):
    "Inteleon"
    def __init__(self,name="Inteleon",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=70,atk=85,defense=65,spatk=125,spdef=65,speed=120,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sniper","Torrent"]),item=random.choice(["Expert Belt","Scope Lens","Choice Specs","Life Orb"]),weight=99.6):
        color="blue"
        if move =="None":
            avmoves=["Snipe Shot","Ice Beam","Shadow Ball","U-turn","Knock Off","Hydro Pump","Dark Pulse","Double Team"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Corviknight
class Corviknight(Pokemon2):
    "Corviknight"
    def __init__(self,name="Corviknight",type1="Flying",type2="Steel",nature="None",level=100,happiness=255,hp=98,atk=87,defense=105,spatk=53,spdef=85,speed=67,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Pressure","Mirror Armor","Unnerve"]),item=random.choice(["Leftovers","Rocky Helmet","Lum Berry","Occa Berry"]),weight=165.3):
        color="blue"
        if move =="None":
            avmoves=["Roost","Brave Bird","Defog","U-turn","Body Press","Steel Wing"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Orbeetle
class Orbeetle(Pokemon2):
    "Orbeetle"
    def __init__(self,name="Orbeetle",type1="Bug",type2="Psychic",nature="None",level=100,happiness=255,hp=60,atk=45,defense=110,spatk=80,spdef=120,speed=90,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Swarm","Frisk"]),item="Expert Belt",weight=89.9):
        color="red"
        if move =="None":
            avmoves=["Reflect","Light Screen","Sticky Web","U-turn","Body Press","Calm Mind","Psychic","Infestation"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Extrasensory"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Rabsca
class Rabsca(Pokemon2):
    def __init__(self,name="Rabsca",type1="Bug",type2="Psychic",nature="None",level=100,happiness=255,hp=75,atk=50,defense=85,spatk=115,spdef=100,speed=45,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Synchronize"]),item="Expert Belt",weight=7.72):
        color="magenta"
        if move =="None":
            avmoves=["Reflect","Light Screen","Sticky Web","U-turn","Body Press","Calm Mind","Extrasensory"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Coalossal
class Coalossal(Pokemon2):
    "Coalossal"
    def __init__(self,name="Coalossal",type1="Rock",type2="Fire",nature="None",level=100,happiness=255,hp=110,atk=80,defense=120,spatk=80,spdef=90,speed=30,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Steam Engine","Flash Fire"]),item=random.choice(["Heavy-Duty Boots","Weakness Policy"]),weight=684.5):
        color="red"
        if move =="None":
            avmoves=["Stealth Rock","Rock Blast","Flamethrower","Rapid Spin","Earth Power","Body Press","Meteor Beam","Tar Shot","Stone Edge","Heat Crash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Garganacl
class Garganacl(Pokemon2):
    def __init__(self,name="Garganacl",type1="Rock",type2="None",nature="None",level=100,happiness=255,hp=100,atk=100,defense=130,spatk=45,spdef=90,speed=35,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Purifying Salt","Clear Body","Sturdy"]),item=random.choice(["Heavy-Duty Boots","Leftovers","Figy Berry"]),weight=529.11):
        color="yellow"
        if move =="None":
            avmoves=["Stealth Rock","Rock Blast","Rapid Spin","Earth Power","Body Press","Meteor Beam","Explosion","Heavy Slam","Earthquake","Recover","Hammer Arm","Iron Defense","Protect","Stealth Rock"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Salt Cure"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Flapple
class Flapple(Pokemon2):
    "Flapple"
    def __init__(self,name="Flapple",type1="Grass",type2="Dragon",nature="None",level=100,happiness=255,hp=75,atk=110,defense=80,spatk=95,spdef=60,speed=70,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Ripen","Hustle"]),item="Life Orb",weight=2.2):
        color="red"
        if move =="None":
            avmoves=["Grav Apple","Outrage","Sucker Punch","U-turn","Grassy Glide","Dragon Pulse","Dragon Energy"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Appletun
class Appletun(Pokemon2):
    "Appletun"
    def __init__(self,name="Appletun",type1="Grass",type2="Dragon",nature="None",level=100,happiness=255,hp=110,atk=85,defense=80,spatk=100,spdef=80,speed=30,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Ripen","Thick Fat"]),item="Leftovers",weight=28.7):
        color="green"
        if move =="None":
            avmoves=["Draco Meteor","Outrage","Apple Acid","Recover","Giga Drain","Dragon Pulse","Leech Seed"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Sandaconda
class Sandaconda(Pokemon2):
    "Sandaconda"
    def __init__(self,name="Sandaconda",type1="Ground",type2="None",nature="None",level=100,happiness=255,hp=72,atk=107,defense=125,spatk=65,spdef=70,speed=71,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sand Spit","Sand Veil","Shed Skin"]),item=random.choice(["Leftovers","Rocky Helmet"]),weight=144.4):
        color="yellow"
        if move =="None":
            avmoves=["Coil","Sandstorm","Glare","Recover","Earthquake","Drill Run","Stealth Rock","Scale Shot","Rest","Rock Slide","Minimize","Dig"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
        #Centiskorch
class Centiskorch(Pokemon2):
    "Centiskorch"
    def __init__(self,name="Centiskorch",type1="Fire",type2="Bug",nature="None",level=100,happiness=255,hp=100,atk=115,defense=65,spatk=90,spdef=90,speed=65,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Flash Fire","Flame Body","Mountaineer"]),item=random.choice(["Leftovers","Heavy-Duty Boots"]),weight=264.6):
        color="red"
        if move =="None":
            avmoves=["Lunge","Fire Lash","Coil","Crunch","Inferno","Power Whip","X-Scissor","Flare Blitz","Leech Life","Knock Off","Skitter Smack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Toxtricity
class Toxtricity(Pokemon2):
    "Toxtricity"
    def __init__(self,name="Toxtricity",type1="Electric",type2="Poison",nature=random.choice(naturelist),level=100,happiness=255,hp=75,atk=98,defense=70,spatk=114,spdef=70,speed=75,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Punk Rock","Technician"]),item=random.choice(["Throat Spray","Life Orb","Choice Specs","Air Balloon"]),weight=88.2):
        color="yellow"
        if move =="None":
            avmoves=["Boomburst","Sludge Wave","Hyper Voice","Volt Switch","Venoshock","Snarl"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Overdrive"]
        if nature in ['Hardy', 'Brave', 'Adamant', 'Naughty', 'Docile', 'Impish', 'Lax', 'Hasty', 'Jolly', 'Naive', 'Rash', 'Sassy','Quirky']:
            name="Amped "+name
            color="cyan"
        if nature not in ['Hardy', 'Brave', 'Adamant', 'Naughty', 'Docile', 'Impish', 'Lax', 'Hasty', 'Jolly', 'Naive', 'Rash', 'Sassy','Quirky']:
            name="Low Key "+name
        if move !="None":
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Barraskewda
class Barraskewda(Pokemon2):
    "Barraskewda"
    def __init__(self,name="Barraskewda",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=61,atk=123,defense=60,spatk=60,spdef=50,speed=136,hpev=0,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Propeller Tail","Swift Swim"]),item=random.choice(["Leftovers","Choice Band","Expert Belt"]),weight=66.1):
        color="yellow"
        if move =="None":
            avmoves=["Liquidation","Double-Edge","Aqua Jet","Crunch","Psychic Fangs","Close Combat","Poison Jab","Waterfall","Ice Fang","Scale Shot","Drill Run"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Grapplot
class Grapploct(Pokemon2):
    "Grapplot"
    def __init__(self,name="Grapploct",type1="Fighting",type2="Water",nature="None",level=100,happiness=255,hp=80,atk=118,defense=90,spatk=70,spdef=80,speed=42,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Technician","Limber"]),item="Leftovers",weight=86):
        color="blue"
        if move =="None":
            avmoves=["Octolock","Superpower","Submission","Bulk Up","Close Combat","Focus Blast","Brick Break","Octazooka","Drain Punch","Ice Punch","Power-Up Punch","Aqua Jet"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Polteageist
class Polteageist (Pokemon2):
    "Polteageist"
    def __init__(self,name="Polteageist",type1="Ghost",type2="None",nature="None",level=100,happiness=255,hp=60,atk=65,defense=65,spatk=134,spdef=114,speed=70,hpev=0,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Weak Armor"]),item=random.choice(["Focus Sash","White Herb"]),weight=0.9):
        color="magenta"
        if move =="None":
            avmoves=["Shell Smash","Giga Drain","Shadow Ball","Stored Power"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Hatterene
class Hatterene(Pokemon2):
    "Hatterene"
    def __init__(self,name="Hatterene",type1="Psychic",type2="Fairy",nature="None",level=100,happiness=255,hp=57,atk=90,defense=95,spatk=136,spdef=103,speed=29,hpev=252,atkev=0,defev=4,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Magic Bounce","Anticipation"]),item=random.choice(["Leftovers","Life Orb"]),weight=11):
        color="magenta"
        if move =="None":
            avmoves=["Calm Mind","Dazzling Gleam","Mystical Fire","Moonblast","Psychic","Draining Kiss","Trick Room","Expanding Force","Misty Explosion","Nuzzle"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Grimmsnarl
class Grimmsnarl(Pokemon2):
    "Grimmsnarl"
    def __init__(self,name="Grimmsnarl",type1="Dark",type2="Fairy",nature="None",level=100,happiness=255,hp=95,atk=120,defense=65,spatk=95,spdef=75,speed=60,hpev=252,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Prankster","Frisk"]),item=random.choice(["Leftovers","Light Clay","Figy Berry"]),weight=134.5):
        color="blue"
        if move =="None":
            avmoves=["Light Screen","Reflect","Spirit Break","Play Rough","Dark Pulse","Sucker Punch","False Surrender","Taunt","Metronome","Darkest Lariat","Parting Shot","Bulk Up","Drain Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Obstagoon
class Obstagoon(Pokemon2):
    "Obstagoon"
    def __init__(self,name="Obstagoon",type1="Dark",type2="Normal",nature="None",level=100,happiness=255,hp=93,atk=90,defense=101,spatk=60,spdef=81,speed=95,hpev=0,atkev=252,defev=4,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Guts","Defiant"]),item="Leftovers",weight=101.4):
        if move =="None":
            avmoves=["Obstruct","Double-Edge","Close Combat","Snarl","Night Slash","Sucker Punch","Throat Chop","Cross Chop"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
        #Kleavor
class Kleavor(Pokemon2):
    "Kealvor"
    def __init__(self,name="Kleavor",type1="Bug",type2="Rock",nature="None",level=100,happiness=255,hp=70,atk=135,defense=95,spatk=45,spdef=70,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sharpness","Sheer Force","Swarm","Steadfast"]),item="Life Orb",weight=196.2):
        color="yellow"
        if move =="None":
            avmoves=["Protect","Stone Axe","Stealth Rock","X-Scissor","U-turn","Swords Dance","Close Combat","Accelerock","Double Team"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Perrserker
class Perrserker(Pokemon2):
    "Perrserker"
    def __init__(self,name="Perrserker",type1="Steel",type2="None",nature="None",level=100,happiness=255,hp=90,atk=110,defense=100,spatk=30,spdef=60,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Tough Claws","Steely Spirit"]),item="Life Orb",weight=61.7):
        if move =="None":
            avmoves=["Protect","Iron Head","Slash","Iron Defense","Play Rough","Swords Dance","Close Combat"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Sirfetchd
class Sirfetchd(Pokemon2):
    "Sirfetchd"
    def __init__(self,name="Sirfetch`d",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=82,atk=135,defense=95,spatk=68,spdef=82,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Scrappy","Sharpness"]),item="Leftovers",weight=257.9):
        if move =="None":
            avmoves=["Swords Dance","Sacred Sword","Leaf Blade","Night Slash","Meteor Assault","Brave Bird","First Impression"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #MrRime
class MrRime(Pokemon2):
    "MrRime"
    def __init__(self,name="Mr.Rime",type1="Ice",type2="Psychic",nature="None",level=100,happiness=255,hp=80,atk=65,defense=75,spatk=110,spdef=90,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Ice Body","Screen Cleaner"]),item="Leftovers",weight=128.3):
        color="blue"
        if move =="None":
            avmoves=["Psychic","Ice Shard","Freeze-Dry","Sucker Punch","Dazzling Gleam","Grass Knot","Expanding Force","Triple Axel","Thunder","Hypnosis"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Alcremie
class Alcremie(Pokemon2):
    "Alcremie"
    def __init__(self,name="Alcremie",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=65,atk=60,defense=75,spatk=110,spdef=121,speed=64,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Sweet Veil",item="Leftovers",weight=1.1):
        color="magenta"
        if move =="None":
            avmoves=["Misty Terrain","Freeze-Dry","Draining Kiss","Dazzling Gleam","Calm Mind","Misty Explosion"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Frosmoth
class Frosmoth(Pokemon2):
    "Frosmoth"
    def __init__(self,name="Frosmoth",type1="Ice",type2="Bug",nature="None",level=100,happiness=255,hp=70,atk=65,defense=65,spatk=125,spdef=90,speed=65,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Ice Scales","Shield Dust"]),item="Leftovers",weight=92.6):
        color="cyan"
        if move =="None":
            avmoves=["Defog","Ice Shard","Freeze-Dry","Bug Buzz","Tailwind","Quiver Dance","Skitter Smack","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Indeedee
class Indeedee(Pokemon2):
    "Indeedee"
    def __init__(self,name="Indeedee",type1="Psychic",type2="Normal",nature="None",level=100,happiness=255,hp=60,atk=65,defense=55,spatk=105,spdef=95,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Psychic Surge",item=random.choice(["Psychic Seed","Terrain Extender"]),weight=61.7):
        color="blue"
        if move =="None":
            avmoves=["Psychic","Expanding Force","Calm Mind","Stored Power","Metronome","Mystical Fire","Hyper Voice","Shadow Ball","Draining Kiss"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Copperajah
class Copperajah(Pokemon2):
    "Copperajah"
    def __init__(self,name="Copperajah",type1="Steel",type2="None",nature="None",level=100,happiness=255,hp=122,atk=130,defense=79,spatk=80,spdef=79,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sheer Force","Heavy Metal"]),item="Leftovers",weight=1433):
        color="green"
        if move =="None":
            avmoves=["Heavy Slam","High Horsepower","Iron Head","Play Rough","Bulldoze","Double Iron Bash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Dracozolt
class Dracozolt(Pokemon2):
    "Dracozolt"
    def __init__(self,name="Dracozolt",type1="Electric",type2="Dragon",nature="None",level=100,happiness=255,hp=90,atk=100,defense=90,spatk=80,spdef=70,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sand Rush","Hustle"]),item=random.choice(["Leftovers","Choice Scarf","Life Orb"]),weight=418.9):
        color="yellow"
        if move =="None":
            avmoves=["Bolt Beak","Dragon Rush","Dragon Tail","Wild Charge","Earthquake","Meteor Beam","Outrage","Aerial Ace","Dragon Claw","Flamethrower","Stone Edge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Dracovish
class Dracovish(Pokemon2):
    "Dracovish"
    def __init__(self,name="Dracovish",type1="Water",type2="Dragon",nature="None",level=100,happiness=255,hp=90,atk=90,defense=100,spatk=70,spdef=80,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Strong Jaw",item="Choice Scarf",weight=474):
        color="blue"
        if move =="None":
            avmoves=["Fishious Rend","Dragon Rush","Ice Fang","Thunder Fang","Earthquake","Meteor Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Duraludon
class Duraludon(Pokemon2):
    "Duraludon"
    def __init__(self,name="Duraludon",type1="Steel",type2="Dragon",nature="None",level=100,happiness=255,hp=85,atk=95,defense=115,spatk=120,spdef=50,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Stalwart","Heavy Metal"]),item=random.choice(["Leftovers","Blunder Policy"]),weight=88.2):
        if move =="None":
            avmoves=["Draco Meteor","Steel Beam","Flash Cannon","Dark Pulse","Iron Defense","Breaking Swipe","Dark Pulse","Thunderbolt","Heavy Slam","Thunder","Substitute"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Dragapult
class Dragapult(Pokemon2):
    "Dragapult"
    def __init__(self,name="Dragapult",type1="Dragon",type2="Ghost",nature="None",level=100,happiness=255,hp=88,atk=120,defense=75,spatk=100,spdef=75,speed=142,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Infiltrator",item=random.choice(["Choice Band","Life Orb","Choice Specs","Lum Berry"]),weight=110.2):
        color="green"
        if move =="None":
            avmoves=["Dragon Darts","Draco Meteor","Phantom Force","Flamethrower","Thunderbolt","U-turn","Shadow Ball","Dragon Pulse","Sucker Punch","Shadow Sneak","Double Team","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                       
         #Zacian
class Zacian(Pokemon2):
    "Zacian"
    def __init__(self,name="Crowned Sword Zacian",type1="Fairy",type2="Steel",nature="None",level=100,happiness=255,hp=92,atk=170,defense=115,spatk=80,spdef=115,speed=148,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Intrepid Sword",item="Rusted Sword",weight=782.6):
        color="cyan"
        if move =="None":
            avmoves=["Behemoth Blade","Play Rough","Protect","Crunch","Swords Dance"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Zamazenta
class Zamazenta(Pokemon2):
    "Zamazenta"
    def __init__(self,name="Crowned Shield Zamazenta",type1="Fighting",type2="Steel",nature="None",level=100,happiness=255,hp=92,atk=130,defense=145,spatk=80,spdef=145,speed=128,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Dauntless Shield",item="Rusted Shield",weight=1730.6):
        color="magenta"
        if move =="None":
            avmoves=["Behemoth Bash","Close Combat","Protect","Crunch","Swords Dance"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                                                                                                                 #Eternatus
class Eternatus(Pokemon2):
    "Eternatus"
    def __init__(self,name="Eternatus",type1="Poison",type2="Dragon",nature="None",level=100,happiness=255,hp=140,atk=85,defense=95,spatk=145,spdef=95,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Pressure",item=random.choice(["Power Herb","Lum Berry"]),weight=2094.4):
        color="blue"
        if move =="None":
            avmoves=["Dynamax Cannon","Eternabeam","Flamethrower","Sludge Bomb","Meteor Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
     #Eternatus
class EEternatus(Pokemon2):
    "Eternatus"
    def __init__(self,name="Eternamax Eternatus",type1="Poison",type2="Dragon",nature="None",level=100,happiness=255,hp=255,atk=115,defense=250,spatk=125,spdef=250,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Pressure",item="Power Herb",weight=100):
        if move =="None":
            avmoves=["Dynamax Cannon","Eternabeam","Flamethrower","Sludge Bomb","Meteor Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                
        #Urshifu
class DUrshifu(Pokemon2):
    "Urshifu"
    def __init__(self,name="Single Strike Urshifu",type1="Fighting",type2="Dark",nature="None",level=100,happiness=255,hp=100,atk=130,defense=100,spatk=63,spdef=60,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Unseen Fist",item=random.choice(["Choice Band","Muscle Band","Life Orb"]),weight=213.5):
        color="red"
        if move =="None":
            avmoves=["Close Combat","U-turn","Sucker Punch","Darkest Lariat","Swords Dance","Poison Jab","Drain Punch"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Wicked Blow"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Urshifu
class WUrshifu(Pokemon2):
    "Urshifu"
    def __init__(self,name="Rapid Strike Urshifu",type1="Fighting",type2="Water",nature="None",level=100,happiness=255,hp=100,atk=130,defense=100,spatk=63,spdef=60,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Unseen Fist",item=random.choice(["Choice Band","Muscle Band","Life Orb"]),weight=213.5):
        color="blue"
        if move =="None":
            avmoves=["Close Combat","U-turn","Aqua Jet","Swords Dance","Drain Punch","Bulk Up"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Surging Strikes"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Zarude
class Zarude(Pokemon2):
    "Zarude"
    def __init__(self,name="Zarude",type1="Dark",type2="Grass",nature="None",level=100,happiness=255,hp=105,atk=120,defense=105,spatk=70,spdef=95,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Leaf Guard",item=random.choice(["Heavy Duty Boots","Leftovers","Choice Scarf"]),weight=154.3):
        color="green"
        if move =="None":
            avmoves=["Jungle Healing","Power Whip","U-turn","Darkest Lariat","Swords Dance","Trailblaze","Close Combat"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Regieleki
class Regieleki(Pokemon2):
    "Regieleki"
    def __init__(self,name="Regieleki",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=80,atk=100,defense=50,spatk=100,spdef=50,speed=200,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Transistor",item="Life Orb",weight=319.7):
        color="yellow"
        if move =="None":
            avmoves=["Thunder Cage","Explosion","Thunderbolt","Thunder","Zap Cannon","Lock-On","Extreme Speed","Acrobatics","Reflect","Light Screen","Thunder Wave","Substitute","Rest"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Regidrago
class Regidrago(Pokemon2):
    "Regidrago"
    def __init__(self,name="Regidrago",type1="Dragon",type2="None",nature="None",level=100,happiness=255,hp=200,atk=100,defense=50,spatk=100,spdef=50,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Dragon's Maw",item="Leftovers",weight=440.9):
        color="red"
        if move =="None":
            avmoves=["Dragon Energy","Explosion","Dragon Pulse","Hyper Beam","Earthquake","Earth Power","Fire Fang","Ice Fang","Thunder Fang","Draco Meteor","Outrage"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Glastrier
class Glastrier(Pokemon2):
    "Glastrier"
    def __init__(self,name="Glastrier",type1="Ice",type2="None",nature="None",level=100,happiness=255,hp=100,atk=145,defense=130,spatk=65,spdef=110,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Chilling Neigh",item=random.choice(["Leftovers","Iapapa Berry","Lum Berry"]),weight=1763.7):
        color="cyan"
        if move =="None":
            avmoves=["Swords Dance","Icicle Crash","High Horsepower","Close Combat","Ice Hammer","Avalanche"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Spectrier
class Spectrier(Pokemon2):
    "Spectrier"
    def __init__(self,name="Spectrier",type1="Ghost",type2="None",nature="None",level=100,happiness=255,hp=100,atk=65,defense=60,spatk=145,spdef=80,speed=130,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Grim Neigh",item=random.choice(["Leftovers","Lum Berry","Choice Specs"]),weight=98.1):
        color="blue"
        if move =="None":
            avmoves=["Nasty Plot","Shadow Ball","Dark Pulse","Hex","Will-O-Wisp"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Calyrex
class ICalyrex(Pokemon2):
    "Calyrex"
    def __init__(self,name="Ice Rider Calyrex",type1="Psychic",type2="Ice",nature="None",level=100,happiness=255,hp=100,atk=165,defense=150,spatk=85,spdef=130,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="As One",item=random.choice(["Leftovers","Heavy-Duty Boots","Choice Band","Life Orb","Weakness Policy","Lum Berry"]),weight=1783.7):
        color="cyan"
        if move =="None":
            avmoves=["Swords Dance","High Horsepower","Close Combat","Leech Seed","Trick","Psyshock","Avalanche"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Glacial Lance"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Calyrex
class SCalyrex(Pokemon2):
    "Calyrex"
    def __init__(self,name="Shadow Rider Calyrex",type1="Psychic",type2="Ghost",nature="None",level=100,happiness=255,hp=100,atk=85,defense=80,spatk=165,spdef=100,speed=150,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="As One",item=random.choice(["Leftovers","Choice Specs","Choice Scarf","Focus Sash","Mental Herb","Heavy-Duty Boots","Life Orb"]),weight=118.1):
        color="blue"
        if move =="None":
            avmoves=["Nasty Plot","Dark Pulse","Hex","Trick","Psyshock","Leech Seed","Draining Kiss","Future Sight"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Astral Barrage"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
#Cetitan
class Cetitan(Pokemon2):
    "Cetitan"
    def __init__(self,name="Cetitan",type1="Ice",type2="None",nature="None",level=100,happiness=255,hp=170,atk=113,defense=65,spatk=45,spdef=55,speed=73,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Thick Fat","Slush Rush","Sheer Force"]),item=random.choice(["Leftovers","Sitrus Berry","Heavy-Duty Boots"]),weight=1543.24):
        color="cyan"
        if move =="None":
            avmoves=["Belly Drum","Icicle Crash","Protect","Stone Edge","Ice Spinner","Ice Shard","Yawn","Earthquake","Play Rough","Heavy Slam","Avalanche"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Koraidon
class Koraidon(Pokemon2):
    "Koraidon"
    def __init__(self,name="Koraidon",type1="Dragon",type2="Fighting",nature="None",level=100,happiness=255,hp=100,atk=135,defense=115,spatk=85,spdef=100,speed=135,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Orichalcum Pulse"]),item=random.choice(["Choice Band","Life Orb","Leftovers","Choice Scarf","Heat Rock"]),weight=668):
        color="red"
        if move =="None":
            avmoves=["Extreme Speed","Superpower","Close Combat","Dragon Claw","U-turn","Heavy Slam","Flare Blitz","Swords Dance","Flame Charge","Stomping Tantrum","Outrage"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Collision Course"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Miraidon
class Miraidon(Pokemon2):
    "Miraidon"
    def __init__(self,name="Miraidon",type1="Dragon",type2="Electric",nature="None",level=100,happiness=255,hp=100,atk=85,defense=100,spatk=135,spdef=115,speed=135,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Hadron Engine"]),item=random.choice(["Choice Specs","Choice Scarf","Heavy Duty Boots","Leftovers","Terrain Extender"]),weight=529.11):
        color="blue"
        if move =="None":
            avmoves=["Dragon Pulse","Overheat","Thunder","Volt Switch","Draco Meteor","Parabolic Charge","U-turn","Dazzling Gleam","Calm Mind","Taunt"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Electro Drift"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Enamorus
class Enamorus(Pokemon2):
    "Enamorus"
    def __init__(self,name="Enamorus",type1="Fairy",type2="Flying",nature="None",level=100,happiness=255,hp=74,atk=115,defense=70,spatk=135,spdef=80,speed=106,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Trace","Fairy Aura"]),item="Leftovers",weight=105.8):
        color="magenta"
        if move =="None":
            avmoves=["Springtide Storm","Moonblast","Extrasensory","Focus Blast","Draining Kiss","Hurricane"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Enamorus
class TEnamorus(Pokemon2):
    "Enamorus"
    def __init__(self,name="Therian Enamorus",type1="Fairy",type2="Flying",nature="None",level=100,happiness=255,hp=74,atk=115,defense=110,spatk=135,spdef=100,speed=46,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Trace","Fairy Aura"]),item="Leftovers",weight=105.8):
        color="magenta"
        if move =="None":
            avmoves=["Springtide Storm","Moonblast","Extrasensory","Focus Blast","Draining Kiss","Hurricane"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Butterfree
class Butterfree(Pokemon2):
    "Butterfree"
    def __init__(self,name="Butterfree",type1="Bug",type2="Flying",nature="None",level=100,happiness=255,hp=60,atk=45,defense=45,spatk=110,spdef=95,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Tinted Lens","Compound Eyes"]),item=random.choice(["Leftovers","Silver Powder","Choice Specs"]),weight=70.55):
        color="blue"
        if move =="None":
            avmoves=["Quiver Dance","Air Slash","Tailwind","Psychic","Sleep Powder","Giga Drain","Hurricane","Whirlwind","Pollen Puff","Protect","Shadow Ball","Double Team","Roost","Energy Ball","U-turn","Razor Wind"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Bug Buzz"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Vivillon
class Vivillon(Pokemon2):
    def __init__(self,name="Vivillon",type1="Bug",type2="Flying",nature="None",level=100,happiness=255,hp=80,atk=52,defense=50,spatk=90,spdef=50,speed=89,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Tinted Lens","Compound Eyes"]),item="Leftovers",weight=37.48):
        color="green"
        if move =="None":
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Tailwind","Sleep Powder","Hurricane","Light Screen","Draining Kiss","Pollen Puff"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Beedrill
class Beedrill(Pokemon2):
    "Beedrill"
    def __init__(self,name="Beedrill",type1="Bug",type2="Poison",nature="None",level=100,happiness=255,hp=65,atk=115,defense=40,spatk=40,spdef=80,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sniper","Swarm","Adaptability"]),item=random.choice(["Black Sludge","Silver Powder","Beedrillite","Salac Berry"]),weight=65.04):
        color="yellow"
        if move =="None":
            avmoves=["Poison Jab","Knock Off","Sludge Bomb","Drill Run","Toxic Spikes","Endeavor","Brick Break","Megahorn","Gunk Shot","Venoshock","Assurance","Pin Missile","Agility","Brick Break","Double Team","Facade","Aerial Ace","Roost","X-Scissor","Swords Dance","U-turn","Substitute"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Raticate
class Raticate(Pokemon2):
    def __init__(self,name="Raticate",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=60,atk=91,defense=70,spatk=45,spdef=70,speed=107,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Guts","Hustle","Adaptability"]),item=random.choice(["Life Orb","Silk Scarf","Focus Sash"]),weight=40.79):
        if move =="None":
            avmoves=["Swords Dance","Knock Off","Crunch","Sucker Punch","Double-Edge","Super Fang","Endeavor","Stomping Tantrum","Thudner Wave","Shadow Ball","Quick Attack","Assurance","Roar","Taunt","Protect","Iron Tail","Dig","Double Team","Facade","Giga Impact","Thunder Wave","Swagger","Substitute","Strength","Final Gambit"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Smeargle
class Smeargle(Pokemon2):
    def __init__(self,name="Smeargle",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=55,atk=20,defense=35,spatk=20,spdef=45,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Technician","Moody","Own Tempo"]),item="Focus Sash",weight=127.87):
        if move =="None":
            avmoves=typemoves.allmove
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)              
#Gumshoos
class Gumshoos(Pokemon2):
    def __init__(self,name="Gumshoos",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=98,atk=110,defense=60,spatk=55,spdef=60,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Stakeout","Strong Jaw","Adaptability"]),item=random.choice(["Life Orb","Choice Band"]),weight=31.31):
        color="yellow"
        if move =="None":
            avmoves=["Swords Dance","Knock Off","Super Fang","Sucker Punch","Double-Edge","Crunch","Rest","Yawn","Thrash","Earthquake"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#ARaticate
class ARaticate(Pokemon2):
    "Raticate"
    def __init__(self,name="Alolan Raticate",type1="Normal",type2="Dark",nature="None",level=100,happiness=255,hp=75,atk=86,defense=70,spatk=40,spdef=80,speed=77,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Thick Fat","Hustle"]),item="Sitrus Berry",weight=56.22):
        if move =="None":
            avmoves=avmoves=["Swords Dance","Knock Off","Crunch","Sucker Punch","Double-Edge","Super Fang","Endeavor","Stomping Tantrum","Thudner Wave","Shadow Ball","Quick Attack","Assurance","Roar","Taunt","Protect","Iron Tail","Dig","Double Team","Facade","Giga Impact","Thunder Wave","Swagger","Substitute","Strength","Final Gambit"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
#Fearow
class Fearow(Pokemon2):
    "Fearow"
    def __init__(self,name="Fearow",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=65,atk=110,defense=65,spatk=61,spdef=61,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Technician","Sniper","Frisk","Intimidate"]),item=random.choice(["Sharp Beak","Liechi Berry"]),weight=83.78):
        if move =="None":
            avmoves=["U-turn","Drill Peck","Drill Run","Dual Wingbeat","Brave Bird","Roost","Steel Wing","Assurance","Aerial Ace","Double Team","Steel Wing","Giga Impact","Defog","Fly","Feather Dance","Quick Attack","Sky Attack","Tri Attack","Whirlwind","Heat Wave","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Pikachu
class Pikachu(Pokemon2):
    "Pikachu"
    def __init__(self,name="Pikachu",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=45,atk=80,defense=50,spatk=75,spdef=60,speed=120,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Static","Lightning Rod"]),item="Light Ball",weight=13.23):
        color="yellow"
        if move =="None":
            avmoves=["Extreme Speed","Volt Tackle","Iron Tail","Electroweb","Electro Ball","Thunder","Double Team","Wish","Brick Break","Fake Out"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Thunderbolt"]
        else:
            moves=move
        if name=="Pikachu":
            ch=random.randint(1,5)
            if ch==5:
                name+=" the Unrivaled"
                ability="Lightning Rod"
                moves=["Play Rough","Iron Tail","Surf","Thunder"]
                maxiv="Water"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
#Emolga
class Emolga(Pokemon2):
    def __init__(self,name="Emolga",type1="Electric",type2="Flying",nature="None",level=100,happiness=255,hp=55,atk=95,defense=60,spatk=105,spdef=60,speed=103,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Static","Lightning Rod","Motor Drive"]),item=random.choice(["Electric Gem","Flying Gem"]),weight=11.02):
        color="yellow"
        if move =="None":
            avmoves=["Acrobatics","Volt Switch","Electro Ball","Thunder","Light Screen","Double Team","Thunder Wave","U-turn","Charm"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Thunderbolt"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
#Heliolisk
class Heliolisk(Pokemon2):
    def __init__(self,name="Heliolisk",type1="Electric",type2="Normal",nature="None",level=100,happiness=255,hp=62,atk=55,defense=52,spatk=109,spdef=94,speed=109,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Solar Power",item=random.choice(["Sitrus Berry","Air Balloon"]),weight=46.3):
        color="yellow"
        if move =="None":
            avmoves=["Volt Switch","Electro Ball","Thunder","Thunderbolt","Scale Shot","Boomburst","Razor Wind"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Parabolic Charge"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                     
#Raichu
class Raichu(Pokemon2):
    "Raichu"
    def __init__(self,name="Raichu",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=70,atk=100,defense=55,spatk=110,spdef=80,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Static","Lightning Rod"]),item=random.choice(["Leftovers","Air Balloon","Salac Berry","Electric Gem","Liechi Berry","Life Orb","Focus Sash"]),weight=66.14):
        color="yellow"
        if move =="None":
            avmoves=["Extreme Speed","Volt Tackle","Iron Tail","Thunderbolt","Electroweb","Electro Ball","Thunder","Fake Out","Calm Mind","Double Team","Signal Beam","Focus Blast","Thunder Wave","Brick Break","Knock Off","Return","Grass Knot","Swagger","Feint"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Grass Knot" in moves:
            item="Grass Gem"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
#Pincurchin
class Pincurchin(Pokemon2):
    "Raichu"
    def __init__(self,name="Pincurchin",type1="Electric",type2="Water",nature="None",level=100,happiness=255,hp=68,atk=81,defense=95,spatk=91,spdef=85,speed=15,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Electric Surge",item="Electric Seed",weight=2.2):
        color="blue"
        if move =="None":
            avmoves=["Zing Zap","Discharge","Thunder Wave","Chilling Water","Rest","Toxic Spikes","Rising Voltage"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Gorochu
class Gorochu(Pokemon2):
    def __init__(self,name="Gorochu",type1="Electric",type2="Dark",nature="None",level=100,happiness=255,hp=70,atk=115,defense=65,spatk=120,spdef=80,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Competitive",item="Leftovers",weight=100):
        if move =="None":
            avmoves=["Extreme Speed","Volt Tackle","Iron Tail","Thunderbolt","Electroweb","Electro Ball","Thunder","Fake Out","Nasty Plot","Dark Pulse","Night Slash","Crunch","Rain Dance","Thunder"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                            
#ARaichu
class ARaichu(Pokemon2):
    "Raichu"
    def __init__(self,name="Alolan Raichu",type1="Electric",type2="Psychic",nature="None",level=100,happiness=255,hp=60,atk=85,defense=50,spatk=95,spdef=85,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Surge Surfer",item="Leftovers",weight=46.3):
        color="yellow"
        if move =="None":
            avmoves=["Extreme Speed","Volt Tackle","Grass Knot","Thunderbolt","Psychic","Electro Ball","Thunder","Fake Out","Nasty Plot","Expanding Force","Future Sight","Double Team","Electric Terrain","Rising Voltage","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Electric Terrain" in moves:
            item="Terrain Extender"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
#Sandslash
class Sandslash(Pokemon2):
    "Sandslash"
    def __init__(self,name="Sandslash",type1="Ground",type2="None",nature="None",level=100,happiness=255,hp=75,atk=100,defense=110,spatk=25,spdef=55,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sand Rush","Sand Veil","Sand Force"]),item=random.choice(["Leftovers","Salac Berry"]),weight=65.04):
        color="yellow"
        if move =="None":
            avmoves=["Swords Dance","Crush Claw","Earthquake","Gyro Ball","Bulldoze","Rock Slide","Rapid Spin","Spiky Shield","Dig","Brick Break","Sandstorm"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
#Cochungus
class Cochungus(Pokemon2):
    def __init__(self,name="Cochungus",type1="Normal",type2="Ground",nature="None",level=100,happiness=255,hp=125,atk=100,defense=90,spatk=25,spdef=95,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Unaware","Oblivious"]),item="Leftovers",weight=100):
        if move =="None":
            avmoves=["Rest","Slack Off","Earthquake","Body Slam","Bulldoze","Rock Slide","Return"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                     
                 #Sandslash
class ASandslash(Pokemon2):
    "Sandslash"
    def __init__(self,name="Alolan Sandslash",type1="Ice",type2="Steel",nature="None",level=100,happiness=255,hp=75,atk=110,defense=120,spatk=25,spdef=65,speed=65,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Slush Rush","Snow Cloak","Icicle Scales"]),item=random.choice(["Leftovers","Shuca Berry"]),weight=121.25):
        color="cyan"
        if move =="None":
            avmoves=["Swords Dance","Spiky Shield","Icicle Crash","Gyro Ball","Ice Shard","Icicle Spear","Steel Beam","Rapid Spin","Triple Axel"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        #Clefable
class Clefable(Pokemon2):
    "Clefable"
    def __init__(self,name="Clefable",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=95,atk=76,defense=73,spatk=95,spdef=90,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Magic Guard","Cute Charm"]),item=random.choice(["Leftovers","Life Orb","Unaware","Steel Gem","Sitrus Berry"]),weight=88.18):
        color="magenta"
        if move =="None":
            avmoves=["Cosmic Power","Moonblast","Meteor Mash","Stored Power","Moonlight","Meteor Beam","Metronome","Misty Explosion","Light of Ruin","Soft-Boiled","Mystical Fire","Draining Kiss","Minimize","Wish","Thunder Punch","Ice Beam","Thunderbolt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                       
        #Wigglytuff
class Wigglytuff(Pokemon2):
    def __init__(self,name="Wigglytuff",type1="Normal",type2="Fairy",nature="None",level=100,happiness=255,hp=140,atk=50,defense=85,spatk=95,spdef=80,speed=45,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Competitive","Sheer Force","Frisk","Magic Guard","Cute Charm"]),item=random.choice(["Leftovers","Life Orb","Normal Gem"]),weight=26.46):
        color="magenta"
        if move =="None":
            avmoves=["Body Slam","Moonblast","Rest","Play Rough","Gyro Ball","Expanding Force","Misty Explosion","Flamethrower","Thunderbolt","Ice Beam","Perish Song","Minimize","Blizzard","Fire Blast","Hyper Voice"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Vileplume
class Vileplume(Pokemon2):
    def __init__(self,name="Vileplume",type1="Grass",type2="Poison",nature="None",level=100,happiness=255,hp=75,atk=80,defense=85,spatk=100,spdef=90,speed=100,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Effect Spore"]),item=random.choice(["Black Sludge","Grass Gem","Quick Claw"]),weight=41.01):
        color="red"
        if move =="None":
            avmoves=["Grassy Terrain","Moonblast","Giga Drain","Sleep Powder","Moonlight","Sludge Bomb","Toxic","Apple Acid","Strength Sap","Solar Beam","Petal Dance","Earth Power","Pollen Puff"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Parasect
class Parasect(Pokemon2):
    def __init__(self,name="Parasect",type1="Bug",type2="Grass",nature="None",level=100,happiness=255,hp=70,atk=115,defense=100,spatk=55,spdef=90,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Dry Skin","Effect Spore","Damp"]),item="Leftovers",weight=65.04):
        color="red"
        if move =="None":
            avmoves=["Spore","X-Scissor","Giga Drain","Cross Poison","Synthesis","Leaf Blade","Crabhammer"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
        #Venomoth
class Venomoth(Pokemon2):
    def __init__(self,name="Venomoth",type1="Bug",type2="Psychic",nature="None",level=100,happiness=255,hp=70,atk=55,defense=65,spatk=100,spdef=75,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Tinted Lens","Shield Dust","Wonder Skin"]),item=random.choice(["Black Sludge","Petaya Berry","Wide Lens"]),weight=27.56):
        color="magenta"
        if move =="None":
            avmoves=["Quiver Dance","Bug Buzz","Giga Drain","Psychic","Sleep Powder","Sludge Bomb","Sleep Powder","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Dugtrio
class Dugtrio(Pokemon2):
    def __init__(self,name="Dugtrio",type1="Ground",type2="None",nature="None",level=100,happiness=255,hp=35,atk=152,defense=50,spatk=50,spdef=70,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sand Force","Sand Veil"]),item=random.choice(["Leftovers","Razor Claw"]),weight=73.41):
        color="yellow"
        if move =="None":
            avmoves=["Sucker Punch","Earthquake","Night Slash","Bulldoze","Rock Slide","Scorching Sands","Shadow Claw","Stone Edge","Tri Attack","Dig"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
        #Wugtrio
class Wugtrio(Pokemon2):
    def __init__(self,name="Wugtrio",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=45,atk=100,defense=60,spatk=50,spdef=70,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Rain Dish","Water Veil","Gooey"]),item="Leftovers",weight=11.9):
        color="red"
        if move =="None":
            avmoves=["Sucker Punch","Hydro Pump","Night Slash","Liquidation","Ice Beam","Tri Attack","Dig"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Triple Dive"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                             
        #Dugtrio
class ADugtrio(Pokemon2):
    def __init__(self,name="Alolan Dugtrio",type1="Ground",type2="Steel",nature="None",level=100,happiness=255,hp=45,atk=110,defense=60,spatk=50,spdef=70,speed=120,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Tangling Hair","Sand Veil"]),item="Leftovers",weight=146.83):
        color="yellow"
        if move =="None":
            avmoves=["Sucker Punch","Earthquake","Night Slash","Bulldoze","Iron Head","Steel Beam","Tri Attack","Dig"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Persian
class Persian(Pokemon2):
    def __init__(self,name="Persian",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=65,atk=100,defense=60,spatk=60,spdef=65,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Technician","Feline Prowess","Limber","Unnerve","Nine Lives"]),item=random.choice(["Leftovers","Wide Lens"]),weight=70.55):
        color="yellow"
        if move =="None":
            avmoves=["Play Rough","Sucker Punch","Slash","Night Slash","Fake Out","U-turn","Shadow Claw","Hyper Voice","Taunt","Nasty Plot","Knock Off","Hypnosis","Swagger"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                   
        #Persian
class Meowth(Pokemon2):
    def __init__(self,name="Meowth",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=40,atk=45,defense=35,spatk=40,spdef=40,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Technician","Feline Prowess"]),item="Leftovers",weight=9.26):
        color="yellow"
        if move =="None":
            avmoves=["Play Rough","Sucker Punch","Slash","Night Slash","Fake Out","U-turn","Shadow Claw"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                     
        #Persian
class APersian(Pokemon2):
    def __init__(self,name="Alolan Persian",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=65,atk=60,defense=60,spatk=55,spdef=65,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Feline Prowess","Fur Coat","Technician"]),item="Leftovers",weight=72.75):
        color="cyan"
        if move =="None":
            avmoves=["Nasty Plot","Sucker Punch","Power Gem","Dark Pulse","Fake Out","U-turn","Shadow Ball","Taunt","Skitter Smack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Kingler
class Kingler(Pokemon2):
    def __init__(self,name="Kingler",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=65,atk=130,defense=115,spatk=50,spdef=90,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sheer Force","Shell Armor","Hyper Cutter"]),item=random.choice(["Leftovers","Salac Berry"]),weight=132.28):
        color="red"
        if move =="None":
            avmoves=["Swords Dance","Crabhammer","Razor Shell","Hammer Arm","X-Scissor","Rock Slide","Waterfall","Liquidation","Ice Hammer"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Klawf
class Klawf(Pokemon2):
    def __init__(self,name="Klawf",type1="Rock",type2="None",nature="None",level=100,happiness=255,hp=70,atk=100,defense=115,spatk=35,spdef=55,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Shell Armor","Anger Shell","Regenerator"]),item="Leftovers",weight=174.17):
        color="yellow"
        if move =="None":
            avmoves=["Swords Dance","Crabhammer","Stone Edge","Hammer Arm","X-Scissor","Rock Slide","Bulldoze"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)              
        #Hypno
class Hypno(Pokemon2):
    def __init__(self,name="Hypno",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=100,atk=53,defense=70,spatk=113,spdef=120,speed=67,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Psychic Surge","Magic Bounce","Bad Dreams"]),item=random.choice(["Psychic Seed","Terrain Extender","Sitrus Berry"]),weight=166.67):
        color="yellow"
        if move =="None":
            avmoves=["Nasty Plot","Psyshock","Psychic","Dark Pulse","Hypnosis","Thunder Wave","Shadow Ball","Future Sight","Psycho Boost","Recover","Dream Eater","Trick","Wish","Foul Play"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Trick" in moves:
            item="Lagging Tail"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                      
          #Electrode
class Electrode(Pokemon2):
    "Electrode"
    def __init__(self,name="Electrode",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=60,atk=130,defense=50,spatk=130,spdef=50,speed=140,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Static","Galvanize","Soundproof","Aftermath"]),item=random.choice(["Leftovers","Lum Berry","Shuca Berry","Electric Gem","Focus Sash","Air Balloon"]),weight=146.83):
        color="red"
        if move =="None":
            avmoves=["Thunder","Thunderbolt","Thunder Wave","Hyper Beam","Rest","Explosion","Reflect","Light Screen","Mirror Coat","Signal Beam","Double Team","Electro Ball","Taunt","Swagger","Rain Dance"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rain Dance" in moves:
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Marowak
class Marowak(Pokemon2):
    def __init__(self,name="Marowak",type1="Ground",type2="None",nature="None",level=100,happiness=255,hp=70,atk=100,defense=110,spatk=50,spdef=80,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Rock Head","Bone Zone","Battle Armor"]),item=random.choice(["Leftovers","Yache Berry"]),weight=99.21):
        color="yellow"
        if move =="None":
            avmoves=["Bone Rush","Bonemerang","Earthquake","Stomping Tantrum","Bulldoze","Rock Slide","Swords Dance","Stealth Rock","Head Smash","Perish Song","Outrage","Thunder Punch","Stone Edge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Marowak
class AMarowak(Pokemon2):
    def __init__(self,name="Alolan Marowak",type1="Fire",type2="Ghost",nature="None",level=100,happiness=255,hp=80,atk=80,defense=110,spatk=30,spdef=80,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Rock Head","Bone Zone","Skill Link"]),item="Leftovers",weight=74.96):
        color="cyan"
        if move =="None":
            avmoves=["Bone Rush","Bonemerang","Earthquake","Will-O-Wisp","Bulldoze","Rock Slide","Swords Dance","Stealth Rock","Shadow Bone"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                       
         #Rhydon
class Rhydon(Pokemon2):
    def __init__(self,name="Rhydon",type1="Ground",type2="Rock",nature="None",level=100,happiness=255,hp=105,atk=130,defense=120,spatk=45,spdef=45,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=4,speedev=0,maxiv="No",move="None", ability="Rock Head",item=random.choice(["Eviolite"]),weight=264.55):
        if move =="None":
            avmoves=["Protect","Stone Edge","Hammer Arm","High Horsepower","Thunder Punch","Giga Impact","Stealth Rock","Horn Drill","Double-Edge","Meteor Beam","Curse"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Chansey
class Chansey(Pokemon2):
    def __init__(self,name="Chansey",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=250,atk=5,defense=5,spatk=35,spdef=105,speed=50,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=4,speedev=0,maxiv="No",move="None", ability="Natural Cure",item="Eviolite",weight=76.28):
        color="magenta"
        if move =="None":
            avmoves=["Protect","Soft-Boiled","Toxic","Seismic Toss","Light Screen","Reflect","Stealth Rock","Teleport","Minimize"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                        
        #Seaking
class Seaking(Pokemon2):
    def __init__(self,name="Seaking",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=80,atk=112,defense=80,spatk=45,spdef=80,speed=98,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Lightning Rod","Swift Swim","Rain Dish"]),item=random.choice(["Leftovers","Wacan Berry"]),weight=85.98):
        color="red"
        if move =="None":
            avmoves=["Fishious Rend","Megahorn","Horn Drill","Poison Jab","Swords Dance","Rain Dance","Waterfall","Liquidation","Scale Shot","Agility"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Palafin
class Palafin(Pokemon2):
    def __init__(self,name="Palafin",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=100,atk=70,defense=72,spatk=53,spdef=62,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Zero to Hero"]),item=random.choice(["Leftovers","Assault Vest","Choice Band"]),weight=132.72):
        color="cyan"
        if move =="None":
            avmoves=["Wave Crash","Aqua Tail","Acrobatics","Close Combat","Iron Head","Bounce","Drain Punch","Bulk Up"]
            moves=moveset(type1,type2,avmoves,2,name=name)+["Flip Turn","Jet Punch"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                
#Mr.Mime
class MrMime(Pokemon2):
    def __init__(self,name="Mr.Mime",type1="Psychic",type2="Fairy",nature="None",level=100,happiness=255,hp=40,atk=35,defense=100,spatk=100,spdef=120,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Psychic Surge","Filter","Technician","Soundproof"]),item=random.choice(["Psychic Seed","Terrain Extender","Kasib Berry","Colbur Berry"]),weight=120.15):
        if move =="None":
            avmoves=["Psychic","Dazzling Gleam","Sucker Punch","Encore","Light Screen","Reflect","Expanding Force","Metronome","Psycho Boost","Future Sight","Icy Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ("Reflect" or "Light Screen") in moves:
            item="Light Clay"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
        #Scyther
class Scyther(Pokemon2):
    def __init__(self,name="Scyther",type1="Bug",type2="Flying",nature="None",level=100,happiness=255,hp=70,atk=110,defense=80,spatk=55,spdef=80,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Technician",item="Eviolite",weight=123.46):
        if move =="None":
            avmoves=["Swords Dance","Slash","X-Scissor","U-turn","Roost","Dual Wingbeat","Double Team","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
        #Ditto
class Ditto(Pokemon2):
    "Ditto"
    def __init__(self,name="Ditto",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=40,atk=40,defense=40,spatk=40,spdef=40,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Imposter",item="Choice Scarf",weight=8.82):
        if move =="None":
            moves=["Transform","Protect","Recover","Light Screen"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
#Furret
class Furret(Pokemon2):
    def __init__(self,name="Furret",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=95,atk=86,defense=95,spatk=45,spdef=95,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Adaptability","Scrappy"]),item="Sitrus Berry",weight=71.65):
        if move =="None":
            avmoves=["Belly Drum","Return","Extreme Speed","Sucker Punch","Double-Edge","U-turn","Zen Headbutt","Body Slam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Noctowl        
class Noctowl(Pokemon2):
    def __init__(self,name="Noctowl",type1="Normal",type2="Flying",nature="None",level=100,happiness=255,hp=110,atk=40,defense=80,spatk=96,spdef=106,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Tinted Lens","Insomnia"]),item=random.choice(["Choice Specs","Life Orb","Flying Gem","Ganlon Berry"]),weight=89.95):
        if move =="None":
            avmoves=["Hidden Power","Hurricane","Hypnosis","Brave Bird","U-turn","Air Slash","Moonblast","Psychic","Roost","Extrasensory","Reflect","Esper Wing","Oblivion Wing","Future Sight","Dream Eater"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
#Ledian    
class Ledian(Pokemon2):
    "Ledian"
    def __init__(self,name="Ledian",type1="Bug",type2="Fighting",nature="None",level=100,happiness=255,hp=55,atk=90,defense=50,spatk=35,spdef=100,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Iron Fist",item=random.choice(["Choice Band","Life Orb","Bug Gem"]),weight=78.48):
        if move =="None":
            avmoves=["Power-up Punch","Fire Punch","Ice Punch","Thunder Punch","U-turn","Mach Punch","Victory Dance"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        #Ariados       
class Ariados(Pokemon2):
    def __init__(self,name="Ariados",type1="Bug",type2="Poison",nature="None",level=100,happiness=255,hp=70,atk=90,defense=80,spatk=60,spdef=80,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sniper","Huge Power"]),item=random.choice(["Life Orb","Poison Barb","Payapa Berry"]),weight=73.85):
        if move =="None":
            avmoves=["Toxic Thread","Swords Dance","Sucker Punch","Poison Jab","U-turn","Gunk Shot","Sticky Web","Cross Poison","Megahorn","Signal Beam","Sludge Bomb","Psychic","Electroweb","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                        
#Xatu
class Xatu(Pokemon2):
    def __init__(self,name="Xatu",type1="Psychic",type2="Flying",nature="None",level=100,happiness=255,hp=95,atk=75,defense=80,spatk=105,spdef=80,speed=95,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Magic Bounce","Synchronize"]),item=random.choice(["Life Orb","Petaya Berry","Wacan Berry","Charti Berry","Leftovers","Focus Sash"]),weight=33.07):
        if move =="None":
            avmoves=["Air Slash","Night Shade","Stored Power","Tailwind","U-turn","Calm Mind","Grass Knot","Psychic","Thunder Wave","Esper Wing","Future Sight","Heat Wave","Shadow Ball","Feather Dance","Stored Power","Light Screen"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                
#Bellossom
class Bellossom(Pokemon2):
    def __init__(self,name="Bellossom",type1="Grass",type2="Fairy",nature="None",level=100,happiness=255,hp=75,atk=80,defense=85,spatk=90,spdef=100,speed=100,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Triage"]),item=random.choice(["Life Orb"]),weight=12.79):
        if move =="None":
            avmoves=["Moonlight","Petal Dance","Grassy Terrain","Moonblast","Sleep Powder","Quiver Dance","Giga Drain","Toxic","Fiery Dance","Earth Power","Drain Punch","Leaf Blade"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Sudowoodo
class Sudowoodo(Pokemon2):
    def __init__(self,name="Sudowoodo",type1="Rock",type2="Grass",nature="None",level=100,happiness=255,hp=90,atk=100,defense=115,spatk=30,spdef=65,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Rock Head","Sturdy"]),item=random.choice(["Life Orb","Liechi Berry"]),weight=83.78):
        if move =="None":
            avmoves=["Head Smash","Double-Edge","Low Kick","Rock Slide","Sucker Punch","Wood Hammer","Stone Edge","Hammer Arm","Earthquake","Head Smash","Foul Play","Toxic","Stealth Rock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Jumpluff
class Jumpluff(Pokemon2):
    def __init__(self,name="Jumpluff",type1="Grass",type2="Flying",nature="None",level=100,happiness=255,hp=75,atk=85,defense=70,spatk=35,spdef=95,speed=110,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Fluffy","Aerilate"]),item=random.choice(["Life Orb","Yache Berry","Focus Sash"]),weight=6.61):
        if move =="None":
            avmoves=["U-turn","Acrobatics","Leech Seed","Bullet Seed","Sleep Powder","Synthesis","Giga Drain","Swords Dance","Double-Edge","Strength Sap","Seed Bomb","Pollen Puff"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Acrobatics" in moves:
            item="Flying Gem"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Sunflora
class Sunflora(Pokemon2):
    def __init__(self,name="Sunflora",type1="Grass",type2="Fire",nature="None",level=100,happiness=255,hp=95,atk=75,defense=55,spatk=135,spdef=85,speed=55,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Solar Power","Flash Fire"]),item=random.choice(["Life Orb"]),weight=18.74):
        if move =="None":
            avmoves=["Growth","Leaf Storm","Leech Seed","Sunny Day","Solar Beam","Synthesis","Giga Drain","Flamethrower","Seed Flare","Fiery Dance","Sludge Bomb","Earth Power"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sunny Day" in moves:
            item="Heat Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Quagsire
class Quagsire(Pokemon2):
    def __init__(self,name="Quagsire",type1="Water",type2="Ground",nature="None",level=100,happiness=255,hp=95,atk=95,defense=95,spatk=55,spdef=75,speed=35,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Water Absorb","Damp","Unaware"]),item=random.choice(["Life Orb","Rindo Berry","Focus Sash","Quick Claw"]),weight=165.35):
        if move =="None":
            avmoves=["Earthquake","Toxic","Amnesia","Aqua Tail","Muddy Water","Stealth Rock","Toxic Spikes","Chilling Water","Yawn","Waterfall","Recover","Curse","Rain Dance"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)            
#Clodsire
class Clodsire(Pokemon2):
    def __init__(self,name="Clodsire",type1="Poison",type2="Ground",nature="None",level=100,happiness=255,hp=130,atk=75,defense=60,spatk=45,spdef=100,speed=20,hpev=252,atkev=0,defev=4,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Poison Point","Unaware","Water Absorb"]),item=random.choice(["Life Orb","Sitrus Berry","Heavy-Duty Boots","Black Sludge","Covert Cloak"]),weight=491.63):
        if move =="None":
            avmoves=["Earthquake","Toxic","Amnesia","Poison Tail","Chilling Water","Yawn","Stealth Rock","Recover","Haze","Poison Jab","Toxic Spikes","Spikes"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)         
#Slowking
class Slowking(Pokemon2):
    "Slowking"
    def __init__(self,name="Slowking",type1="Water",type2="Psychic",nature="None",level=100,happiness=255,hp=95,atk=65,defense=80,spatk=110,spdef=110,speed=30,hpev=0,atkev=0,defev=252,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Regenerator","Own Tempo"]),item=random.choice(["Leftovers","Lum Berry","Choice Specs","Expert Belt","Wise Glasses","Bright Powder"]),weight=175.27):
        if move =="None":
            avmoves=["Hidden Power","Ice Beam","Slack Off","Psychic","Flamethrower","Surf","Thunderbolt","Iron Defense","Rain Dance","Yawn","Future Sight","Shadow Ball","Focus Blast","Scald","Nasty Plot","Blizzard","Dragon Tail","Fire Blast","Psyshock"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Chilly Reception"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Wobbuffet
class Wobbuffet(Pokemon2):
    def __init__(self,name="Wobbuffet",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=200,atk=1,defense=90,spatk=1,spdef=90,speed=1,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Shadow Tag",item="Leftovers",weight=62.83):
        if move =="None":
            avmoves=["Counter","Mirror Coat","Destiny Bond","Recover","Encore"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Forretress
class Forretress(Pokemon2):
    def __init__(self,name="Forretress",type1="Bug",type2="Steel",nature="None",level=100,happiness=255,hp=75,atk=90,defense=140,spatk=90,spdef=70,speed=20,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Sturdy",item=random.choice(["Leftovers","Apicot Berry","Occa Berry","Iron Ball","Rocky Helmet"]),weight=277.34):
        if move =="None":
            avmoves=["Iron Defense","Gyro Ball","Heavy Slam","Explosion","Stealth Rock","Reflect","Rapid Spin","Body Press","Spikes","Bug Buzz","Pain Split","Zap Cannon","Earthquake","Light Screen","Toxic","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Reflect" in moves:
            item="Light Clay"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Granbull
class Granbull(Pokemon2):
    def __init__(self,name="Grabull",type1="Fairy",type2="Fighting",nature="None",level=100,happiness=255,hp=90,atk=120,defense=75,spatk=60,spdef=60,speed=85,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Intimidate","Strong Jaw","Bull Rush","Quick Feet"]),item=random.choice(["Leftovers","Quick Claw"]),weight=107.37):
        if move =="None":
            avmoves=["Play Rough","Crunch","Outrage","Fire Fang","Ice Fang","Thunder Fang","Bulk Up","Close Combat","Jaw Lock"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Shuckle
class Shuckle(Pokemon2):
    def __init__(self,name="Shuckle",type1="Bug",type2="Rock",nature="None",level=100,happiness=255,hp=50,atk=10,defense=230,spatk=10,spdef=230,speed=5,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sturdy","Contrary","Solid Rock"]),item=random.choice(["Leftovers","Sitrus Berry","Rocky Helmet","Bright Powder"]),weight=45.19):
        if move =="None":
            avmoves=["Iron Defense","Gyro Ball","Heavy Slam","Explosion","Stealth Rock","Reflect","Rapid Spin","Sticky Web","Cosmic Power","Skitter Smack","Substitute","Toxic","Stone Edge","Earthquake","Rest","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Ursaring
class Ursaring(Pokemon2):
    def __init__(self,name="Ursaring",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=90,atk=130,defense=75,spatk=75,spdef=75,speed=90,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Intimidate","Guts","Quick Feet","Unnerve"]),item=random.choice(["Eviolite","Chople Berry","Liechi Berry","Quick Claw"]),weight=277.34):
        if move =="None":
            avmoves=["Facade","Hammer Arm","Rest","Slash","Strength","Return","Swords Dance","Rock Slide","Shadow Claw","Bulk Up","Thunder Punch","Thrash","Crunch","Avalanche","Counter","Rest"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Magcargo
class Magcargo(Pokemon2):
    def __init__(self,name="Magcargo",type1="Fire",type2="Rock",nature="None",level=100,happiness=255,hp=100,atk=30,defense=120,spatk=100,spdef=110,speed=20,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Flame Body","Simple","Flash Fire"]),item="Leftovers",weight=121.25):
        if move =="None":
            avmoves=["Shell Smash","Flamethrower","Earth Power","Recover","Body Slam","Lava Plume","Ancient Power","Yawn","No Retreat"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Corsola
class Corsola(Pokemon2):
    def __init__(self,name="Corsola",type1="Water",type2="Rock",nature="None",level=100,happiness=255,hp=55,atk=55,defense=100,spatk=65,spdef=100,speed=35,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Regenerator",item="Leftovers",weight=0.9):
        if move =="None":
            avmoves=["Ancient Power","Recover","Earth Power","Explosion","Stealth Rock","Reflect","Power Gem"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Corsola
class GCorsola(Pokemon2):
    def __init__(self,name="Galarian Corsola",type1="Ghost",type2="None",nature="None",level=100,happiness=255,hp=60,atk=55,defense=100,spatk=65,spdef=100,speed=30,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Cursed Body","Weak Armor"]),item="Eviolite",weight=1.1):
        if move =="None":
            avmoves=["Ancient Power","Night Shade","Earth Power","Strength Sap","Stealth Rock","Reflect","Power Gem"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Cursola
class Cursola(Pokemon2):
    def __init__(self,name="Cursola",type1="Water",type2="Rock",nature="None",level=100,happiness=255,hp=80,atk=75,defense=50,spatk=145,spdef=130,speed=55,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Hustle","Natural Cure","Regenerator"]),item="Leftovers",weight=11.02):
        if move =="None":
            avmoves=["Ancient Power","Mirror Coat","Earth Power","Recover","Stealth Rock","Reflect","Power Gem","Ancient Power","Aqua Ring"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                                
#Octillery
class Octillery(Pokemon2):
    def __init__(self,name="Octillery",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=75,atk=105,defense=75,spatk=105,spdef=75,speed=75,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Moody","Sniper","Skill Link","Mega Launcher"]),item="Leftovers",weight=62.83):
        if move =="None":
            avmoves=["Hydro Pump","Ice Beam","Bullet Seed","Gunk Shot","Rock Blast","Surf","Snipe Shot","Water Spout","Skitter Smack","Aurora Beam"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Octazooka"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Delibird
class Delibird(Pokemon2):
    def __init__(self,name="Delibird",type1="Ice",type2="Flying",nature="None",level=100,happiness=255,hp=50,atk=100,defense=50,spatk=90,spdef=50,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Hustle","Surprise"]),item="Leftovers",weight=35.27):
        if move =="None":
            avmoves=["Drill Peck","Dual Wingbeat","Rest","Toxic","Present","Aurora Beam","Surf","Hydro Pump","Freeze-Dry","Ice Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Mantine
class Mantine(Pokemon2):
    def __init__(self,name="Mantine",type1="Water",type2="Flying",nature="None",level=100,happiness=255,hp=80,atk=40,defense=80,spatk=90,spdef=140,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Water Absorb","Swift Swim"]),item=random.choice(["Leftovers","Wacan Berry","Petaya Berry"]),weight=485.02):
        if move =="None":
            avmoves=["Air Slash","Hydro Pump","Ice Beam","Roost","Rain Dance","Scald","Surf","Hidden Power","Hurricane","Signal Beam","Agility"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Donphan
class Donphan(Pokemon2):
    def __init__(self,name="Donphan",type1="Ground",type2="None",nature="None",level=100,happiness=255,hp=90,atk=120,defense=120,spatk=60,spdef=70,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sturdy","Technician","Battle Armor"]),item=random.choice(["Leftovers","Lum Berry","Quick Claw","Bright Powder","Focus Band","Razor Claw"]),weight=264.55):
        if move =="None":
            avmoves=["Bulldoze","Earthquake","Ice Shard","Rock Tomb","Knock Off","Assurance","Rock Slide","Rapid Spin","Head Smash","Double Team","Rock Polish","Counter"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Porygon2
class Porygon2(Pokemon2):
    def __init__(self,name="Porygon2",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=85,atk=80,defense=90,spatk=105,spdef=95,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=4,speedev=0,maxiv="No",move="None", ability="Download",item="Eviolite",weight=71.65):
        if move =="None":
            avmoves=["Protect","Ice Beam","Calm Mind","Recover","Thunderbolt","Flamethrower","Signal Beam","Hidden Power","Psychic","Shadow Ball","Hyper Beam","Trick Room","Tri Attack"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
        #Miltank
class Miltank(Pokemon2):
    def __init__(self,name="Miltank",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=95,atk=90,defense=105,spatk=40,spdef=70,speed=100,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Thick Fat","Sap Sipper","Scrappy"]),item=random.choice(["Leftovers","Liechi Berry","Lum Berry"]),weight=166.45):
        if move =="None":
            avmoves=["Protect","Milk Drink","Body Slam","High Horsepower","Double-Edge","Play Rough","Giga Impact","Zen Headbutt","Brick Break","Return"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
                                 
        #Ceruledge
class Ceruledge(Pokemon2):
    def __init__(self,name="Ceruledge",type1="Fire",type2="Ghost",nature="None",level=100,happiness=255,hp=65,atk=115,defense=80,spatk=60,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire","Weak Armor"]),item=random.choice(["Leftovers","Heavy-Duty Boots","Life Orb"]),weight=136.69):
        if move =="None":
            avmoves=["Protect","Night Slash","Swords Dance","Flare Blitz","Shadow Sneak","Close Combat","Bulk Up"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Bitter Blade"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
        #Armarouge
class Armarouge(Pokemon2):
    def __init__(self,name="Armarouge",type1="Fire",type2="Psychic",nature="None",level=100,happiness=255,hp=65,atk=60,defense=80,spatk=115,spdef=70,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flash Fire"]),item=random.choice(["Charcoal","Weakness Policy","Life Orb","Safety Googles"]),weight=187.39):
        if move =="None":
            avmoves=["Protect","Psychic","Calm Mind","Fire Blast","Extrasensory","Flamethrower","Psyshock","Aura Sphere","Focus Blast","Iron Defense","Heat Wave","Trick Room","Energy Ball"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Armor Cannon"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Linoone
class Linoone(Pokemon2):
    def __init__(self,name="Linoone",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=78,atk=115,defense=70,spatk=80,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Adaptability",item="Sitrus Berry",weight=71.65):
        if move =="None":
            avmoves=["Belly Drum","Return","Extreme Speed","Sucker Punch","Double-Edge","U-turn","Substitute"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Beautifly
class Beautifly(Pokemon2):
    def __init__(self,name="Beautifly",type1="Bug",type2="Flying",nature="None",level=100,happiness=255,hp=60,atk=70,defense=70,spatk=110,spdef=70,speed=75,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Tinted Lens","Compound Eyes","Swarm"]),item=random.choice(["Leftovers","Life Orb","Bright Powder","Focus Sash","Choice Specs","Choice Scarf"]),weight=62.61):
        if move =="None":
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Tailwind","Psychic","Sleep Powder","Giga Drain","Morning Sun","Hidden Power","Roost","U-turn","Sleep Powder"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Dustox
class Dustox(Pokemon2):
    def __init__(self,name="Dustox",type1="Bug",type2="Poison",nature="None",level=100,happiness=255,hp=60,atk=65,defense=100,spatk=65,spdef=100,speed=70,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Shield Dust","Compound Eyes","Multiscale"]),item=random.choice(["Leftovers","Black Sludge","Life Orb"]),weight=69.67):
        if move =="None":
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Toxic","Light Screen","Sleep Powder","Moonlight","Roost","Iron Defense"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Masquerain
class Masquerain(Pokemon2):
    def __init__(self,name="Masquerain",type1="Bug",type2="Water",nature="None",level=100,happiness=255,hp=70,atk=60,defense=73,spatk=100,spdef=82,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Tinted Lens","Intimidate","Unnerve"]),item=random.choice(["Leftovers","Focus Sash"]),weight=7.94):
        if move =="None":
            avmoves=["Quiver Dance","Air Slash","Bug Buzz","Sticky Web","Psychic","Sleep Powder","Hurricane","Hydro Pump","Chilling Water","Ice Beam","Roost"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Ninjask
class Ninjask(Pokemon2):
    def __init__(self,name="Ninjask",type1="Bug",type2="Flying",nature="None",level=100,happiness=255,hp=61,atk=125,defense=45,spatk=50,spdef=50,speed=160,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Speed Boost","Infiltrator"]),item=random.choice(["Leftovers","Insect Plate"]),weight=26.46):
        if move =="None":
            avmoves=["Swords Dance","U-turn","X-Scissor","Roost","Night Slash","Final Gambit","Sonic Slash","Acrobatics","Protect","Leech Life","Hidden Power","Skitter Smack","Double Team","Dig"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Final Gambit" in moves:
            hpev=252
            atkev=0
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Shedinja
class Shedinja(Pokemon2):
    def __init__(self,name="Shedinja",type1="Bug",type2="Ghost",nature="None",level=100,happiness=255,hp=1,atk=135,defense=30,spatk=135,spdef=30,speed=40,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Wonder Guard"]),item=random.choice(["Focus Sash","Lum Berry","Quick Claw","Scope Lens","Heavy-Duty Boots","Safety Googles","Lax Incense"]),weight=2.65):
        if move =="None":
            avmoves=["X-Scissor","Phantom Force","Shadow Ball","Shadow Sneak","Shadow Claw","Hidden Power","Sucker Punch","Will-O-Wisp","Swords Dance","Toxic","Skitter Smack","Shadow Force","Dig"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                         
#Sableye
class Sableye(Pokemon2):
    def __init__(self,name="Sableye",type1="Dark",type2="Ghost",nature="None",level=100,happiness=255,hp=50,atk=75,defense=100,spatk=65,spdef=100,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Prankster"]),item=random.choice(["Leftovers","Sablenite","Ganlon Berry"]),weight=24.25):
        if move =="None":
            avmoves=["Protect","Night Shade","Shadow Sneak","Power Gem","Zen Headbutt","Knock Off","Foul Play","Moonlight","Metronome","Recover","Seismic Toss","Shadow Ball","Will-O-Wisp","Toxic","Taunt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)             
#Grafaiai
class Grafaiai(Pokemon2):
    def __init__(self,name="Grafaiai",type1="Poison",type2="Normal",nature="None",level=100,happiness=255,hp=63,atk=95,defense=65,spatk=80,spdef=72,speed=110,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Poison Touch","Prankster"]),item=random.choice(["Leftovers","Heavy-Duty Boots","Black Sludge"]),weight=59.97):
        if move =="None":
            avmoves=["Protect","Poison Jab","Venoshock","Toxic","Return","Doodle","Knock Off","Gunk Shot","U-turn","Parting Shot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                                
#Mawile
class Mawile(Pokemon2):
    def __init__(self,name="Mawile",type1="Steel",type2="Fairy",nature="None",level=100,happiness=255,hp=50,atk=85,defense=85,spatk=55,spdef=55,speed=90,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Intimidate",item=random.choice(["Life Orb","Leftovers","Mawilite"]),weight=25.35):
        if move =="None":
            avmoves=["Protect","Iron Head","Play Rough","Crunch","Sucker Punch","Iron Defense","Stealth Rock","Double Iron Bash","Hidden Power","Swords Dance","Toxic","Iron Head"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sucker Punch" in moves:
            x=random.randint(1,2)
            if x==1:
                item="Dark Gem"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
        #Manectric
class Manectric(Pokemon2):
    def __init__(self,name="Manectric",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=70,atk=75,defense=60,spatk=115,spdef=60,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Intimidate","Static","Lightning Rod"]),item=random.choice(["Manectite","Life Orb","Petaya Berry","Magnet"]),weight=88.63):
        if move =="None":
            avmoves=["Protect","Volt Switch","Thunder","Crunch","Thunderbolt","Wild Charge","Hyper Beam","Thunder Wave","Flamethrower","Electric Terrain","Double Team","Rain Dance","Overheat","Hidden Power"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rain Dance" in moves:
            item="Damp Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Swalot
class Swalot(Pokemon2):
    def __init__(self,name="Swalot",type1="Poison",type2="None",nature="None",level=100,happiness=255,hp=100,atk=90,defense=83,spatk=90,spdef=83,speed=55,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Gluttony","Liquid Ooze","Magic Guard"]),item=random.choice(["Black Sludge","Life Orb"]),weight=176.37):
        if move =="None":
            avmoves=["Protect","Sludge Bomb","Gunk Shot","Body Slam","Belch","Toxic","Ice Beam","Toxic Spikes","Body Press","Swords Dance","Pain Split","Earth Power","Giga Drain"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Grumpig
class Grumpig(Pokemon2):
    def __init__(self,name="Grumpig",type1="Psychic",type2="Dark",nature="None",level=100,happiness=255,hp=100,atk=50,defense=75,spatk=115,spdef=120,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Thick Fat","Magic Guard","Own Tempo"]),item=random.choice(["Leftovers","Colbur Berry","Ganlon Berry","Salac Berry"]),weight=157.63):
        if move =="None":
            avmoves=["Protect","Psychic","Psyshock","Body Slam","Rest","Power Gem","Belch","Nasty Plot","Snarl","Dazzling Gleam","Earth Power","Thunder Wave","Toxic","Calm Mind","Shadow Ball","Focus Blast"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Cacturne
class Cacturne(Pokemon2):
    def __init__(self,name="Cacturne",type1="Grass",type2="Dark",nature="None",level=100,happiness=255,hp=70,atk=120,defense=60,spatk=120,spdef=60,speed=75,hpev=0,atkev=252,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Water Absorb","Sand Rush","Sand Veil"]),item=random.choice(["Black Glasses","Life Orb","Focus Sash","Salac Berry"]),weight=170.64):
        if move =="None":
            avmoves=["Spiky Shield","Leech Seed","Poison Jab","Assurance","Sucker Punch","Needle Arm","Energy Ball","Grass Knot","Focus Blast","Dark Pulse","Superpower","Seed Bomb","Giga Drain","Swords Dance","Destiny Bond","Spikes"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)               
#Cacturne
class Carnivine(Pokemon2):
    def __init__(self,name="Carnivine",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=89,atk=100,defense=82,spatk=55,spdef=82,speed=46,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Miracle Seed","Life Orb","Focus Sash","Liechi Berry"]),weight=59.52):
        if move =="None":
            avmoves=["Leech Seed","Poison Jab","Sucker Punch","Needle Arm","Energy Ball","Grass Knot","Superpower","Seed Bomb","Swords Dance","Crunch","Power Whip"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Cacturne
class Maractus(Pokemon2):
    def __init__(self,name="Maractus",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=85,atk=116,defense=67,spatk=86,spdef=67,speed=70,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Water Absorb","Chlorophyll","Grassy Surge","Prankster"]),item=random.choice(["Miracle Seed","Life Orb","Focus Sash","Lum Berry"]),weight=61.73):
        if move =="None":
            avmoves=["Leech Seed","Poison Jab","Sucker Punch","Needle Arm","Energy Ball","Grass Knot","Superpower","Seed Bomb","Swords Dance","Spiky Shield","Petal Dance","Cotton Guard","Synthesis"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                          
#Dusclops
class Dusclops(Pokemon2):
    def __init__(self,name="Dusclops",type1="Ghost",type2="None",nature="None",level=100,happiness=255,hp=40,atk=70,defense=130,spatk=60,spdef=130,speed=25,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Pressure","Frisk"]),item=random.choice(["Eviolite"]),weight=67.46):
        if move =="None":
            avmoves=["Protect","Will-O-Wisp","Thunder Wave","Shadow Punch","Hex","Calm Mind","Rest","Trick Room","Metronome","Pain Split","Skitter Smack","Future Sight","Poltergeist"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Tropius
class Tropius(Pokemon2):
    def __init__(self,name="Tropius",type1="Grass",type2="Dragon",nature="None",level=100,happiness=255,hp=109,atk=58,defense=90,spatk=92,spdef=97,speed=61,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Solar Power","Harvest"]),item=random.choice(["Leftovers","Sitrus Berry","Yache Berry"]),weight=220.46):
        if move =="None":
            avmoves=["Dragon Hammer","Dragon Dance","Solar Beam","Leaf Storm","Air Slash","Body Slam","Energy Ball","Grass Knot","Leech Seed","Dragon Pulse","Hurricane","Substitute","Roost","Sunny Day","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sunny Day" in moves:
            item="Heat Rock"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)     
#Bibarel
class Bibarel(Pokemon2):
    def __init__(self,name="Bibarel",type1="Normal",type2="Water",nature="None",level=100,happiness=255,hp=79,atk=85,defense=80,spatk=55,spdef=80,speed=71,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Moody","Unaware","Simple","Torrent"]),item="Leftovers",weight=69.45):
        if move =="None":
            avmoves=["Protect","Aqua Jet","Super Fang","Superpower","Swords Dance","Crunch","Waterfall","Grass Knot","Curse"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Kricketune
class Kricketune(Pokemon2):
    def __init__(self,name="Kricketune",type1="Bug",type2="None",nature="None",level=100,happiness=255,hp=77,atk=105,defense=51,spatk=105,spdef=51,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Technician","Swarm"]),item="Leftovers",weight=56.22):
        if move =="None":
            avmoves=["Protect","Night Slash","X-Scissor","Slash","Swords Dance","Hypnosis","Sticky Web","Perish Song"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Wormadam
class SWormadam(Pokemon2):
    def __init__(self,name="Sandy Wormadam",type1="Bug",type2="Ground",nature="None",level=100,happiness=255,hp=100,atk=79,defense=105,spatk=59,spdef=85,speed=36,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Natural Cure","Anticipation"]),item="Leftovers",weight=14.33):
        if move =="None":
            avmoves=["Protect","Quiver Dance","Rock Blast","Psychic","Sucker Punch","Earthquake","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)      
#Wormadam
class Wormadam(Pokemon2):
    def __init__(self,name="Wormadam",type1="Bug",type2="Grass",nature="None",level=100,happiness=255,hp=100,atk=59,defense=85,spatk=79,spdef=105,speed=36,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Natural Cure","Anticipation"]),item="Leftovers",weight=14.33):
        if move =="None":
            avmoves=["Protect","Quiver Dance","Leaf Storm","Psychic","Sucker Punch","Giga Drain","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)              
#Wormadam
class TWormadam(Pokemon2):
    def __init__(self,name="Trash Wormadam",type1="Bug",type2="Steel",nature="None",level=100,happiness=255,hp=100,atk=69,defense=95,spatk=69,spdef=95,speed=36,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Natural Cure","Anticipation"]),item="Leftovers",weight=14.33):
        if move =="None":
            avmoves=["Protect","Quiver Dance","Iron Head","Psychic","Sucker Punch","Flash Cannon","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                      
#Mothim
class Mothim(Pokemon2):
    def __init__(self,name="Mothim",type1="Bug",type2="Flying",nature="None",level=100,happiness=255,hp=70,atk=94,defense=50,spatk=134,spdef=50,speed=66,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Tinted Lens","Swarm"]),item="Leftovers",weight=51.37):
        if move =="None":
            avmoves=["Protect","Quiver Dance","Leaf Storm","Psychic","Sucker Punch","Giga Drain","Roost","Air Slash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                 
#Floatzel
class Floatzel(Pokemon2):
    def __init__(self,name="Floatzel",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=85,atk=90,defense=55,spatk=95,spdef=50,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Swift Swim","Technician"]),item=random.choice(["Leftovers","Choice Band","Mystic Water","Liechi Berry","Life Orb","Destiny Knot","Bright Powder"]),weight=73.85):
        if move =="None":
            avmoves=["Protect","Aqua Jet","Crunch","Ice Fang","Waterfall","Aqua Tail","Hydro Pump","Flip Turn","Wave Crash","Ice Spinner","Surging Strikes","Brick Break","Bulk Up","Ice Punch","Focus Blast","Razor Wind"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                   
#Pachirisu
class Pachirisu(Pokemon2):
    def __init__(self,name="Pachirisu",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=75,atk=45,defense=70,spatk=45,spdef=95,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Volt Absorb","Prankster"]),item="Leftovers",weight=8.6):
        if move =="None":
            avmoves=["Protect","Volt Switch","Thunderbolt","Super Fang","Sweet Kiss","Nuzzle","Light Screen","Reflect","Charm"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Cherrim
class Cherrim(Pokemon2):
    def __init__(self,name="Cherrim",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=70,atk=100,defense=70,spatk=60,spdef=78,speed=85,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Flower Gift",item=random.choice(["Leftovers","Miracle Seed","Grass Gem"]),weight=20.5):
        if move =="None":
            avmoves=["Protect","Petal Dance","Solar Beam","Leech Seed","Sunny Day","Morning Sun","Grav Apple","Solar Blade","Weather Ball","X-Scissor","Return","Pollen Puff","Substitute"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        
#Lumineon
class Lumineon(Pokemon2):
    def __init__(self,name="Lumineon",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=79,atk=69,defense=76,spatk=129,spdef=69,speed=91,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Storm Drain","Dazzling","Swift Swim"]),item=random.choice(["Leftovers"]),weight=52.91):
        if move =="None":
            avmoves=["Protect","Aqua Jet","Tailwind","Ice Beam","Surf","Hydro Pump","U-turn","Bug Buzz","Hurricane","Icy Wind","Blizzard","Rain Dance","Aurora Beam","Whirlpool"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)     
#Lickilicky
class Lickilicky(Pokemon2):
    def __init__(self,name="Lickilicky",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=110,atk=95,defense=100,spatk=80,spdef=100,speed=30,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Oblivious","Unaware","Cloud Nine","Regenerator"]),item=random.choice(["Sitrus Berry","Expert Belt","Quick Claw"]),weight=308.65):
        if move =="None":
            avmoves=["Protect","Belly Drum","Power Whip","Body Slam","Knock Off","Return","Ice Beam","Thunderbolt","Explosion","Gyro Ball","Thrash","Surf","Flamethrower","Rest","Earthquake"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)        
#Leafeon
class Leafeon(Pokemon2):
    def __init__(self,name="Leafeon",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=65,atk=130,defense=110,spatk=60,spdef=65,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Sap Sipper"]),item=random.choice(["Leftovers","Occa Berry","Yache Berry","Quick Claw","Wide Lens"]),weight=56.22):
        if move =="None":
            avmoves=["Protect","Leaf Blade","Razor Leaf","Last Resort","Giga Drain","Synthesis","Leech Seed","Swords Dance","Quick Attack","X-Scissor"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)         
#Glaceon
class Glaceon(Pokemon2):
    def __init__(self,name="Glaceon",type1="Ice",type2="None",nature="None",level=100,happiness=255,hp=80,atk=45,defense=100,spatk=130,spdef=95,speed=75,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Snow Cloak","Slush Rush","Ice Body"]),item=random.choice(["Leftovers","Salac Berry","Life Orb","Choice Scarf","Wise Glasses","Bright Powder"]),weight=57.1):
        if move =="None":
            avmoves=["Protect","Ice Shard","Ice Beam","Last Resort","Blizzard","Freeze-Dry","Snowscape","Calm Mind","Triple Axel","Icy Wind","Shadow Ball","Yawn","Signal Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                         
#Watchog
class Watchog(Pokemon2):
    def __init__(self,name="Watchog",type1="Normal",type2="Psychic",nature="None",level=100,happiness=255,hp=60,atk=115,defense=69,spatk=60,spdef=69,speed=107,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Analytic","No Guard","Intimidate"]),item=random.choice(["Sitrus Berry","Salac Berry","Focus Sash"]),weight=59.52):
        if move =="None":
            avmoves=["Protect","Super Fang","Hypnosis","Body Slam","Knock Off","Return","Crunch","Toxic","Psychic Fangs","Psycho Cut","Zen Headbutt","Low Kick","Flail"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                
#Liepard
class Liepard(Pokemon2):
    def __init__(self,name="Liepard",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=64,atk=108,defense=55,spatk=78,spdef=55,speed=116,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Prankster","Moxie","Unburden"]),item=random.choice(["Sitrus Berry","Choice Band"]),weight=82.67):
        if move =="None":
            avmoves=["Protect","Play Rough","Night Slash","Sucker Punch","Knock Off","Assurance","Fake Out","Taunt","Skitter Smack","Double Team","U-turn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Drednaw        
class Drednaw(Pokemon2):
    def __init__(self,name="Drednaw",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=90,atk=115,defense=90,spatk=48,spdef=68,speed=74,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Swift Swim","Strong Jaw","Shell Armor"]),item=random.choice(["Sitrus Berry","Life Orb","Water Gem","Air Balloon","Lum Berry"]),weight=254.6):
        if move =="None":
            avmoves=["Hydro Pump","Shell Smash","Flip Turn","Head Smash","Body Slam","Liquidation","Jaw Lock","Crunch","Scale Shot","Aqua Fang"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)      
#Bellibolt
class Bellibolt(Pokemon2):
    def __init__(self,name="Bellibolt",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=109,atk=64,defense=91,spatk=103,spdef=83,speed=45,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Electromorphosis","Damp","Static"]),item=random.choice(["Life Orb","Shuca Berry","Leftovers","Sitrus Berry","Rocky Helmet","Assault Vest","Choice Specs"]),weight=249.12):
        if move =="None":
            avmoves=["Thunderbolt","Hyper Voice","Volt Switch","Wild Charge","Thunder Wave","Discharge","Parabolic Charge","Slack Off","Soak","Chilling Water","Muddy Water","Sucker Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                                        #Great Tusk
class Greattusk(Pokemon2):
    def __init__(self,name="Great Tusk",type1="Ground",type2="Fighting",nature="None",level=100,happiness=255,hp=115,atk=131,defense=131,spatk=53,spdef=53,speed=87,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Protosynthesis",item=random.choice(["Booster Energy","Focus Sash","Passho Berry","Payapa Berry","Rindo Berry","Choice Band"]),weight=705.48):
        if move =="None":
            avmoves=["Close Combat","Earthquake","Mach Punch","Stone Edge","Superpower","Headlong Rush","Knock Off","Ice Spinner","Bulk Up","Stealth Rock","Rapid Spin"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)      
#Brute Bonnet
class Brutebonnet(Pokemon2):
    def __init__(self,name="Brute Bonnet",type1="Grass",type2="Dark",nature="None",level=100,happiness=255,hp=111,atk=127,defense=99,spatk=79,spdef=99,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Protosynthesis",item=random.choice(["Booster Energy","Loaded Dice","Life Orb"]),weight=46.30):
        if move =="None":
            avmoves=["Power Whip","Night Slash","Synthesis","Spore","Close Combat","Crunch","Bullet Seed","Growth","Sucker Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)      
#Amoongus
class Amoongus(Pokemon2):
    def __init__(self,name="Amoongus",type1="Grass",type2="Poison",nature="None",level=100,happiness=255,hp=114,atk=85,defense=70,spatk=85,spdef=80,speed=80,hpev=252,atkev=0,defev=172,spatkev=0,spdefev=84,speedev=0,maxiv="No",move="None", ability="Regenerator",item=random.choice(["Black Sludge","Rocky Helmet","Wiki Berry","Occa Berry","Ganlon Berry"]),weight=23.15):
        if move =="None":
            avmoves=["Giga Drain","Foul Play","Synthesis","Sludge Bomb","Pollen Puff","Substitute","Toxic"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Spore"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)                   
#Sandy Shocks
class Sandyshocks(Pokemon2):
    def __init__(self,name="Sandy Shocks",type1="Electric",type2="Ground",nature="None",level=100,happiness=255,hp=85,atk=81,defense=97,spatk=121,spdef=85,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Protosynthesis",item=random.choice(["Booster Energy"]),weight=132.28):
        if move =="None":
            avmoves=["Thunderbolt","Earth Power","Volt Switch","Stone Edge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)           
#Scream Tail
class Screamtail(Pokemon2):
    def __init__(self,name="Scream Tail",type1="Fairy",type2="Psychic",nature="None",level=100,happiness=255,hp=115,atk=65,defense=99,spatk=65,spdef=115,speed=111,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Protosynthesis",item=random.choice(["Booster Energy","Leftovers","Covert Cloak"]),weight=17.64):
        if move =="None":
            avmoves=["Psychic","Moonblast","Light Screen","Dazzling Gleam","Perish Song","Reflect","Wish"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight) 
#Flutter Mane
class Fluttermane(Pokemon2):
    def __init__(self,name="Flutter Mane",type1="Ghost",type2="Fairy",nature="None",level=100,happiness=255,hp=55,atk=55,defense=55,spatk=135,spdef=135,speed=135,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Protosynthesis",item=random.choice(["Booster Energy","Wiki Berry"]),weight=8.82):
        if move =="None":
            avmoves=["Shadow Ball","Moonblast","Will-O-Wisp","Hex","Perish Song"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)   
#Slither Wing
class Slitherwing(Pokemon2):
    def __init__(self,name="Slither Wing",type1="Bug",type2="Fighting",nature="None",level=100,happiness=255,hp=85,atk=135,defense=79,spatk=85,spdef=105,speed=81,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Protosynthesis",item=random.choice(["Booster Energy"]),weight=202.83):
        if move =="None":
            avmoves=["Close Combat","Swords Dance","Mach Punch","U-turn","First Impression","Morning Sun","Leech Life","Superpower","Flare Blitz","Earthquake","Wild Charge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)      
#Roaring Moon
class Roaringmoon(Pokemon2):
    def __init__(self,name="Roaring Moon",type1="Dragon",type2="Dark",nature="None",level=100,happiness=255,hp=105,atk=139,defense=71,spatk=55,spdef=101,speed=119,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Protosynthesis",item=random.choice(["Booster Energy","Choice Band"]),weight=837.76):
        if move =="None":
            avmoves=["Dragon Claw","Night Slash","Dragon Dance","Crunch","Scale Shot","Jaw Lock","Taunt","Acrobatics","Earthquake"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Iron Treads
class Irontreads(Pokemon2):
    def __init__(self,name="Iron Treads",type1="Ground",type2="Steel",nature="None",level=100,happiness=255,hp=90,atk=112,defense=120,spatk=72,spdef=70,speed=106,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Quark Drive",item=random.choice(["Booster Energy"]),weight=529.11):
        if move =="None":
            avmoves=["Heavy Slam","Earthquake","Body Slam","Stone Edge","Knock Off","Stealth Rock","Rapid Spin","Volt Switch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)       
#Iron Moth
class Ironmoth(Pokemon2):
    def __init__(self,name="Iron Moth",type1="Fire",type2="Poison",nature="None",level=100,happiness=255,hp=80,atk=70,defense=60,spatk=140,spdef=110,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Quark Drive",item=random.choice(["Booster Energy","Choice Scarf"]),weight=79.37):
        if move =="None":
            avmoves=["Fiery Dance","Sludge Wave","Morning Sun","Will-O-Wisp","Discharge","Bug Buzz","Overheat","Hurricane","Lunge","Air Slash","Dazzling Gleam","Flash Cannon","Heat Wave","Energy Ball","Psychic","Flamethrower","Fire Blast","Solar Beam","U-turn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)     
#Iron Hands
class Ironhands(Pokemon2):
    def __init__(self,name="Iron Hands",type1="Fighting",type2="Electric",nature="None",level=100,happiness=255,hp=154,atk=140,defense=108,spatk=50,spdef=68,speed=50,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Quark Drive",item=random.choice(["Booster Energy"]),weight=839.3):
        if move =="None":
            avmoves=["Close Combat","Thunder Punch","Mach Punch","Plasma Fists","Body Press","Belly Drum","Heavy Slam","Wild Charge","Fake Out","Earthquake","Play Rough","Iron Head","Rock Slide","Swords Dance","Rest","Stomping Tantrum","Drain Punch","Ice Punch","Fire Punch","Brick Break","Volt Switch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)         
#Iron Jugulis
class Ironjugulis(Pokemon2):
    def __init__(self,name="Iron Jugulis",type1="Dark",type2="Flying",nature="None",level=100,happiness=255,hp=94,atk=80,defense=86,spatk=122,spdef=80,speed=108,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Quark Drive",item=random.choice(["Booster Energy"]),weight=244.71):
        if move =="None":
            avmoves=["Dark Pulse","Roost","Night Daze","Air Slash","Dragon Pulse","Knock Off","Hyper Voice","Snarl","Flash Cannon","Heat Wave","Flamethrower","Earth Power","Hydro Pump","Fire Blast","Focus Blast","Hyper Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Iron Thorns
class Ironthorns(Pokemon2):
    def __init__(self,name="Iron Thorns",type1="Rock",type2="Electric",nature="None",level=100,happiness=255,hp=100,atk=134,defense=110,spatk=70,spdef=84,speed=72,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Quark Drive",item=random.choice(["Booster Energy","Air Balloon"]),weight=668):
        if move =="None":
            avmoves=["Wild Charge","Earthquake","Dragon Dance","Stone Edge","Rock Slide","Iron Defense","Fire Fang","Ice Fang","Thunder Fang","Sandstorm","Wild Charge","Stealth Rock","Heavy Slam","Crunch","Iron Head","Swords Dance","Stomping Tantrum","Dragon Claw","Rock Blast","Dragon Tail"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Iron Bundle
class Ironbundle(Pokemon2):
    def __init__(self,name="Iron Bundle",type1="Ice",type2="Water",nature="None",level=100,happiness=255,hp=56,atk=80,defense=114,spatk=124,spdef=60,speed=136,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Quark Drive",item=random.choice(["Booster Energy"]),weight=24.25):
        if move =="None":
            avmoves=["Ice Beam","Hydro Pump","Surf","Snowscape","Drill Peck","Freeze-Dry","Flip Turn","Aurora Veil","Blizzard","Chilling Water"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)               
#Iron Valiant
class Ironvaliant(Pokemon2):
    def __init__(self,name="Iron Valiant",type1="Fairy",type2="Fighting",nature="None",level=100,happiness=255,hp=74,atk=130,defense=90,spatk=120,spdef=60,speed=116,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Quark Drive",item=random.choice(["Booster Energy","Life Orb"]),weight=77.16):
        if move =="None":
            avmoves=["Close Combat","Swords Dance","Moonblast","Aura Sphere","Spirit Break","Knock Off","Leaf Blade","Night Slash","Psycho Cut","Dazzling Gleam","Shadow Sneak","Focus Blast","Thunderbolt","Psychic","Energy Ball","Shadow Ball","Aura Sphere","Liquidation","X-Scissor","Poison Jab","Psyshock","Future Sight","Double Team"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)        
#Spinestial
class Spinestial(Pokemon2):
    def __init__(self,name="Spinestial",type1="Water",type2="Dragon",nature="None",level=100,happiness=255,hp=104,atk=130,defense=90,spatk=40,spdef=80,speed=100,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Swift Swim",item=random.choice(["Life Orb"]),weight=100):
        if move =="None":
            avmoves=["Liquidation","Dragon Dance","Dragon Claw","Crunch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)              
#Audino
class Audino(Pokemon2):
    def __init__(self,name="Audino",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=103,atk=60,defense=86,spatk=60,spdef=86,speed=50,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability="Regenerator",item=random.choice(["Leftovers","Audinite","Sitrus Berry","Shell Bell"]),weight=68.34):
        if move =="None":
            avmoves=["Misty Terrain","Double-Edge","Moonblast","Zen Headbutt","Blizzard","Fire Blast","Thunder","Calm Mind","Wish","Heal Bell","Dazzling Gleam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)  

#Delcatty
class Delcatty(Pokemon2):
    def __init__(self,name="Delcatty",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=70,atk=95,defense=95,spatk=65,spdef=85,speed=90,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Magic Guard","Feline Prowess","Wonder Skin","Cute Charm","Normalize"]),item=random.choice(["Leftovers","Focus Sash"]),weight=71.87):
        if move =="None":
            avmoves=["Misty Terrain","Double-Edge","Fake Out","Zen Headbutt","Hyper Voice","Play Rough","Thunder Wave","Tickle"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)           
#Wo-Chien
class Wochien(Pokemon2):
    def __init__(self,name="Wo-Chien",type1="Dark",type2="Grass",nature="None",level=100,happiness=255,hp=85,atk=85,defense=100,spatk=95,spdef=135,speed=70,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Tablets of Ruin"]),item=random.choice(["Leftovers"]),weight=163.58):
        if move =="None":
            avmoves=["Giga Drain","Dark Pulse","Foul Play","Grassy Terrain","Knock Off","Leaf Storm","Leech Seed","Protect"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Ruination"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Chien-Pao
class Chienpao(Pokemon2):
    def __init__(self,name="Chien-Pao",type1="Dark",type2="Ice",nature="None",level=100,happiness=255,hp=80,atk=120,defense=80,spatk=90,spdef=65,speed=135,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sword of Ruin"]),item=random.choice(["Life Orb","Choice Band","Heavy-Duty Boots","Focus Sash","Black Glasses"]),weight=335.54):
        if move =="None":
            avmoves=["Icicle Crash","Night Slash","Foul Play","Snowscape","Knock Off","Swords Dance","Sucker Punch","Sacred Sword","Recover","Crunch","Ice Shard","Ice Spinner","Throat Chop","Night Slash"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Ruination"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)     
#Ting-Lu
class Tinglu(Pokemon2):
    def __init__(self,name="Ting-Lu",type1="Dark",type2="Ground",nature="None",level=100,happiness=255,hp=155,atk=110,defense=125,spatk=55,spdef=80,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Vessel of Ruin"]),item=random.choice(["Leftovers"]),weight=1542.57):
        if move =="None":
            avmoves=["Earthquake","Night Slash","Foul Play","Sandstorm","Knock Off","Stomping Tantrum","Whirlwind"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Ruination"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)      
#Chi-Yu
class Chiyu(Pokemon2):
    def __init__(self,name="Chi-Yu",type1="Dark",type2="Fire",nature="None",level=100,happiness=255,hp=55,atk=80,defense=80,spatk=135,spdef=120,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Beads of Ruin"]),item=random.choice(["Choice Specs","Choice Scarf","Life Orb"]),weight=10.8):
        if move =="None":
            avmoves=["Overheat","Dark Pulse","Nasty Plot","Sunny Day","Knock Off","Fire Blast","Flamethrower","Psychic","Snarl","Heat Wave","Protect"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Ruination"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)      
#Bombirdier
class Bombirdier(Pokemon2):
    def __init__(self,name="Bombirdier",type1="Dark",type2="Flying",nature="None",level=100,happiness=255,hp=70,atk=103,defense=85,spatk=60,spdef=85,speed=82,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Rocky Payload","Big Pecks"]),item=random.choice(["Leftovers"]),weight=94.58):
        if move =="None":
            avmoves=["Dual Wingbeat","Dark Pulse","Rock Slide","Parting Shot","Knock Off","Roost"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)          
#Flamigo
class Flamigo(Pokemon2):
    def __init__(self,name="Flamigo",type1="Flying",type2="Fighting",nature="None",level=100,happiness=255,hp=82,atk=115,defense=74,spatk=75,spdef=64,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Scrappy","Costar","Tangled Feet"]),item=random.choice(["Leftovers","Choice Band","Choice Scarf"]),weight=81.57):
        if move =="None":
            avmoves=["Brave Bird","Roost","Throat Chop","Sky Attack","Knock Off","Close Combat","U-turn","Tailwind","Throat Chop","Double Team"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)             
#Kilowattrel
class Kilowattrel(Pokemon2):
    def __init__(self,name="Kilowattrel",type1="Electric",type2="Flying",nature="None",level=100,happiness=255,hp=70,atk=70,defense=60,spatk=105,spdef=60,speed=125,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Volt Absorb","Competitive","Wind Power"]),item=random.choice(["Leftovers"]),weight=85.1):
        if move =="None":
            avmoves=["Air Slash","Roost","Thunderbolt","Hurricane","Volt Switch","Electro Ball"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)   
#Espathra
class Espathra(Pokemon2):
    def __init__(self,name="Espathra",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=95,atk=60,defense=60,spatk=101,spdef=60,speed=105,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Speed Boost","Opportunist","Frisk"]),item=random.choice(["Leftovers","Expert Belt"]),weight=198.42):
        if move =="None":
            avmoves=["Psychic","Dazzling Gleam","Drill Peck","Extreme Speed","Calm Mind","Roost","Stored Power","Shadow Ball","Protect"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Lumina Crash"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)         
#Veluza
class Veluza(Pokemon2):
    def __init__(self,name="Veluza",type1="Water",type2="Psychic",nature="None",level=100,happiness=255,hp=90,atk=102,defense=73,spatk=78,spdef=65,speed=70,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Mold Breaker","Sharpness"]),item=random.choice(["Leftovers","Sitrus Berry"]),weight=198.42):
        if move =="None":
            avmoves=["Recover","Psycho Cut","Night Slash","Slash","Crunch","Fillet Away"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Aqua Cutter"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)  
#Glimmora
class Glimmora(Pokemon2):
    def __init__(self,name="Glimmora",type1="Rock",type2="Poison",nature="None",level=100,happiness=255,hp=83,atk=55,defense=90,spatk=130,spdef=81,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Corrosion","Toxic Debris"]),item=random.choice(["Leftovers","Focus Sash","Air Balloon"]),weight=99.21):
        if move =="None":
            avmoves=["Sludge Wave","Power Gem","Stealth Rock","Acid Armor","Spiky Shield","Rock Slide","Earth Power","Dazzling Gleam","Spikes"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Mortal Spin"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)           
#Orthworm
class Orthworm(Pokemon2):
    def __init__(self,name="Orthworm",type1="Steel",type2="None",nature="None",level=100,happiness=255,hp=70,atk=85,defense=145,spatk=60,spdef=55,speed=65,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Earth Eater"]),item=random.choice(["Leftovers"]),weight=683.43):
        if move =="None":
            avmoves=["Earthquake","Iron Head","Stealth Rock","Iron Defense","Iron Tail","Heavy Slam","Rest","Shed Tail","Dig"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Lokix
class Lokix(Pokemon2):
    def __init__(self,name="Lokix",type1="Bug",type2="Dark",nature="None",level=100,happiness=255,hp=71,atk=102,defense=78,spatk=52,spdef=55,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Tinted Lens","Swarm"]),item=random.choice(["Leftovers","Choice Band"]),weight=38.58):
        if move =="None":
            avmoves=["Sucker Punch","Throat Chop","Swords Dance","Assurance","X-Scissor","First Impression","Lunge","Leech Life","U-turn","Brick Break","Skitter Smack"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Axe Kick"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)     
#Spidops
class Spidops(Pokemon2):
    def __init__(self,name="Spidops",type1="Bug",type2="None",nature="None",level=100,happiness=255,hp=60,atk=79,defense=92,spatk=52,spdef=86,speed=35,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Stakeout"]),item=random.choice(["Leftovers","Focus Sash"]),weight=36.38):
        if move =="None":
            avmoves=["Sucker Punch","Throat Chop","Swords Dance","Assurance","X-Scissor","First Impression","Skitter Smack","Spikes","Sticky Web","Toxic Spikes","U-turn"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Silk Trap"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)   
#Sigilyph
class Sigilyph(Pokemon2):
    def __init__(self,name="Sigilyph",type1="Psychic",type2="Flying",nature="None",level=100,happiness=255,hp=72,atk=58,defense=80,spatk=113,spdef=80,speed=117,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Magic Guard","Tinted Lens"]),item=random.choice(["Leftovers","Life Orb","Expert Belt"]),weight=30.86):
        if move =="None":
            avmoves=["Air Slash","Psychic","Light Screen","Reflect","Tailwind","Esper Wing","Hurricane","Psycho Boost","Cosmic Power","Ice Beam","Ancient Power","Energy Ball","Heat Wave","Stored Power","Roost"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Swoobat
class Swoobat(Pokemon2):
    def __init__(self,name="Swoobat",type1="Psychic",type2="Flying",nature="None",level=100,happiness=255,hp=75,atk=57,defense=65,spatk=117,spdef=55,speed=114,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Simple","Unaware","Unburden"]),item=random.choice(["Leftovers","Flying Gem","Salac Berry"]),weight=23.15):
        if move =="None":
            avmoves=["Air Slash","Psychic","Light Screen","Reflect","Tailwind","Esper Wing","Future Sight"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)            
#Scovillain
class Scovillain(Pokemon2):
    def __init__(self,name="Scovillain",type1="Grass",type2="Fire",nature="None",level=100,happiness=255,hp=65,atk=108,defense=65,spatk=108,spdef=65,speed=75,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Moody"]),item=random.choice(["Life Orb"]),weight=33.07):
        if move =="None":
            avmoves=["Growth","Sunny Day","Solar Beam","Synthesis","Flamethrower","Fire Fang","Bullet Seed","Crunch"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Spicy Extract"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)      
#Revavroom
class Revavroom(Pokemon2):
    def __init__(self,name="Revavroom",type1="Steel",type2="Poison",nature="None",level=100,happiness=255,hp=80,atk=119,defense=90,spatk=54,spdef=67,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Filter"]),item=random.choice(["Life Orb","Air Balloon"]),weight=264.55):
        if move =="None":
            avmoves=["Taunt","Iron Head","Poison Jab","Gunk Shot"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Spin Out"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Dachsbun
class Dachsbun(Pokemon2):
    def __init__(self,name="Dachsbun",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=57,atk=80,defense=115,spatk=50,spdef=80,speed=95,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Well-Baked Body"]),item=random.choice(["Life Orb","Leftovers"]),weight=32.85):
        if move =="None":
            avmoves=["Crunch","Play Rough","Body Press","Stomping Tantrum","Charm","Protect"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)          
#Slurpuff
class Slurpuff(Pokemon2):
    def __init__(self,name="Slurpuff",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=82,atk=90,defense=86,spatk=75,spdef=75,speed=72,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sweet Veil","Unburden"]),item=random.choice(["Leftovers","Focus Sash"]),weight=11.02):
        if move =="None":
            avmoves=["Energy Ball","Play Rough","Sticky Web","Draining Kiss","Misty Explosion","Fire Blast","Thunderbolt","Dazzling Gleam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Maushold
class Maushold(Pokemon2):
    def __init__(self,name="Maushold",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=74,atk=75,defense=70,spatk=65,spdef=75,speed=111,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Technician","Cheek Pouch"]),item=random.choice(["Leftovers"]),weight=5.07):
        if move =="None":
            avmoves=["Protect","Play Rough","Super Fang","Bullet Seed","Crunch","Tidy Up"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Population Bomb"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)            
#Mabosstiff
class Mabosstiff(Pokemon2):
    def __init__(self,name="Mabosstiff",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=80,atk=120,defense=90,spatk=60,spdef=70,speed=85,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Guard Dog","Stakeout","Intimidate"]),item=random.choice(["Leftovers"]),weight=134.48):
        if move =="None":
            avmoves=["Double-Edge","Outrage","Jawlock","Crunch","Swagger","Roar","Snarl"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight) 
#Pawmot
class Pawmot(Pokemon2):
    def __init__(self,name="Pawmot",type1="Electric",type2="Fighting",nature="None",level=100,happiness=255,hp=70,atk=115,defense=70,spatk=70,spdef=60,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Volt Absorb","Natural Cure","Iron Fist"]),item=random.choice(["Leftovers"]),weight=90.39):
        if move =="None":
            avmoves=["Close Combat","Thunder Wave","Wild Charge","Discharge","Nuzzle","Dig"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Double Shock"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)     
#Diggersby
class Diggersby(Pokemon2):
    def __init__(self,name="Diggersby",type1="Normal",type2="Ground",nature="None",level=100,happiness=255,hp=85,atk=56,defense=77,spatk=50,spdef=77,speed=78,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Huge Power","Cheek Pouch"]),item=random.choice(["Leftovers"]),weight=93.48):
        if move =="None":
            avmoves=["Earthquake","Return","Stone Edge","Body Slam","Dig","High Horsepower","Wild Charge","Foul Play","Stone Edge","Iron Head","Low Kick"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Simisage
class Simisage(Pokemon2):
    def __init__(self,name="Simisage",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=75,atk=98,defense=63,spatk=98,spdef=63,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Overgrow",item=random.choice(["Leftovers","Salac Berry","Grass Gem"]),weight=67.24):
        color="green"
        if move =="None":
            avmoves=["Seed Bomb","Grass Knot","Giga Drain","Energy Ball","Spiky Shield","Low Kick","Acrobatics"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Simisear
class Simisear(Pokemon2):
    def __init__(self,name="Simisear",type1="Fire",type2="None",nature="None",level=100,happiness=255,hp=75,atk=98,defense=63,spatk=98,spdef=63,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Blaze",item=random.choice(["Leftovers","Salac Berry","Fire Gem"]),weight=61.73):
        color="red"
        if move =="None":
            avmoves=["Overheat","Will-O-Wisp","Fire Blast","Flamethrower","Low Kick","Heat Wave","Rock Slide"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Simipour
class Simipour(Pokemon2):
    def __init__(self,name="Simipour",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=75,atk=98,defense=63,spatk=98,spdef=63,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Torrent",item=random.choice(["Leftovers","Salac Berry","Water Gem"]),weight=63.93):
        color="cyan"
        if move =="None":
            avmoves=["Hydro Pump","Surf","Scald","Rain Dance","Toxic","Hidden Power","Taunt","Grass Knot","Acrobatics"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)        
#Musharna
class Musharna(Pokemon2):
    def __init__(self,name="Musharna",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=116,atk=55,defense=85,spatk=107,spdef=95,speed=29,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Synchronize","Unaware"]),item=random.choice(["Leftovers"]),weight=133.38):
        color="magenta"
        if move =="None":
            avmoves=["Calm Mind","Psychic","Moonblast","Hypnosis","Yawn","Future Sight"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Throh
class Throh(Pokemon2):
    def __init__(self,name="Throh",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=120,atk=100,defense=95,spatk=30,spdef=95,speed=45,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Guts","Mold Breaker","Inner Focus"]),item=random.choice(["Flame Orb","Payapa Berry"]),weight=122.36):
        color="red"
        if move =="None":
            avmoves=["Superpower","Bulk Up","Grass Knot","Taunt","Recover","Facade","Knock Off","Storm Throw"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ability=="Guts":
            item="Flame Orb"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Sawk
class Sawk(Pokemon2):
    def __init__(self,name="Sawk",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=75,atk=135,defense=75,spatk=30,spdef=75,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sturdy","Inner Focus","Contrary","Mold Breaker"]),item=random.choice(["Weakness Policy","Focus Sash","Expert Belt","Life Orb"]),weight=112.44):
        color="blue"
        if move =="None":
            avmoves=["Close Combat","Bulk Up","Grass Knot","Brick Break"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
#Plusle
class Plusle(Pokemon2):
    def __init__(self,name="Plusle",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=60,atk=50,defense=40,spatk=85,spdef=75,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Plus","Transistor","Lightning Rod","Prankster"]),item=random.choice(["Focus Sash","Shuca Berry","Magnet","Salac Berry"]),weight=9.26):
        color="red"
        if move =="None":
            avmoves=["Thunder Wave","Nasty Plot","Encore","Thunder","Nuzzle","Grass Knot","Hidden Power","Agility","Discharge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Minun
class Minun(Pokemon2):
    def __init__(self,name="Minun",type1="Electric",type2="None",nature="None",level=100,happiness=255,hp=60,atk=85,defense=75,spatk=50,spdef=40,speed=110,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Electric Surge","Volt Absorb","Galvanize","Prankster"]),item=random.choice(["Focus Sash","Electric Gem","Life Orb"]),weight=9.26):
        color="blue"
        if move =="None":
            avmoves=["Thunder Wave","Nasty Plot","Encore","Thunder","Nuzzle","Rising Voltage","Grass Knot","Hidden Power"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Volbeat
class Volbeat(Pokemon2):
    def __init__(self,name="Volbeat",type1="Bug",type2="Electric",nature="None",level=100,happiness=255,hp=85,atk=47,defense=75,spatk=90,spdef=85,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Prankster","Illuminate","Swam"]),item=random.choice(["Focus Sash"]),weight=39.02):
        color="red"
        if move =="None":
            avmoves=["Play Rough","Bug Buzz","Tail Glow","Moonlight","Thunderbolt","Double Team","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Illumise
class Illumise(Pokemon2):
    def __init__(self,name="Illumise",type1="Bug",type2="Fairy",nature="None",level=100,happiness=255,hp=85,atk=90,defense=75,spatk=47,spdef=85,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Prankster","Tinted Lens","Oblivious"]),item=random.choice(["Focus Sash"]),weight=39.02):
        color="blue"
        if move =="None":
            avmoves=["Play Rough","Bug Buzz","Tail Glow","Moonlight","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Spinda
class Spinda(Pokemon2):
    def __init__(self,name="Spinda",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=80,atk=80,defense=80,spatk=80,spdef=80,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Contrary","Own Tempo","Tangled Feet"]),item=random.choice(["Focus Sash","Salac Berry"]),weight=11.02):
        color="yellow"
        if move =="None":
            avmoves=["Sucker Punch","Drain Punch","Dizzy Punch","Rock Slide","Hyper Voice","Crush Claw","Double-Edge","Superpower","Assist","Thrash"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Sucker Punch" in moves:
            item="Dark Gem"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Castform
class Castform(Pokemon2):
    def __init__(self,name="Castform",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=70,atk=70,defense=70,spatk=70,spdef=70,speed=70,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Forecast",item=random.choice(["Focus Sash","Heat Rock","Icy Rock","Smooth Rock","Damp Rock","Life Orb","Expert Belt","Petaya Berry","Lum Berry"]),weight=1.76):
        if move =="None":
            avmoves=["Hydro Pump","Hurricane","Fire Blast","Blizzard","Rain Dance","Sunny Day","Snowscape","Ice Beam","Flamethrower","Thunder","Thunderbolt","Shadow Ball","Energy Ball","Thunder Wave"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Weather Ball"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)    
#Chimecho
class Chimecho(Pokemon2):
    def __init__(self,name="Chimecho",type1="Psychic",type2="None",nature="None",level=100,happiness=255,hp=90,atk=50,defense=70,spatk=95,spdef=80,speed=80,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Levitate",item=random.choice(["Focus Sash","Colbur Berry"]),weight=2.20):
        color="magenta"
        if move =="None":
            avmoves=["Psychic","Extrasensory","Light Screen","Yawn","Perish Song","Recover","Healing Wish","Energy Ball","Trick Room"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Lilligant
class Lilligant(Pokemon2):
    def __init__(self,name="Lilligant",type1="Grass",type2="None",nature="None",level=100,happiness=255,hp=70,atk=60,defense=75,spatk=110,spdef=75,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Own Tempo"]),item=random.choice(["Focus Sash","Petaya Berry","Miracle Seed","Big Root"]),weight=35.94):
        color="green"
        if move =="None":
            avmoves=["Leaf Storm","Sleep Powder","Petal Blizzard","Energy Ball","Quiver Dance","Seed Flare","Pollen Puff"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Crustle
class Crustle(Pokemon2):
    def __init__(self,name="Crustle",type1="Bug",type2="Rock",nature="None",level=100,happiness=255,hp=70,atk=95,defense=125,spatk=65,spdef=75,speed=55,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Sturdy","Shell Armor","Weak Armor"]),item=random.choice(["Leftovers","White Herb","Lum Berry","Salac Berry","Power Herb","Rocky Helmet"]),weight=440.92):
        color="yellow"
        if move =="None":
            avmoves=["Rock Wrecker","Shell Smash","X-Scissor","Rock Blast","Skitter Smack","Earthquake","Rock Slide","Solar Beam","Flail"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Cinccino
class Cinccino(Pokemon2):
    def __init__(self,name="Cinccino",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=75,atk=95,defense=60,spatk=65,spdef=60,speed=115,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Skill Link","Technician","Cute Charm"]),item=random.choice(["Focus Sash","Rawst Berry","Life Orb","King's Rock"]),weight=16.53):
        if move =="None":
            avmoves=["Tail Slap","Bullet Seed","Rock Blast","Thunderbolt","U-turn","Focus Blast","Grass Knot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)       
#Sawsbuck
class Sawsbuck(Pokemon2):
    def __init__(self,name="Sawsbuck",type1="Fighting",type2="Grass",nature="None",level=100,happiness=255,hp=80,atk=120,defense=70,spatk=60,spdef=70,speed=100,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Chlorophyll","Sap Sipper","Serene Grace"]),item=random.choice(["Leftovers","Liechi Berry","Choice Scarf"]),weight=203.93):
        color=random.choice(["green","magenta","cyan","red"])
        if move =="None":
            avmoves=["Horn Leech","Bullet Seed","Megahorn","Double-Edge","Close Combat","Superpower","Wild Charge","High Jump Kick","Rest","Swords Dance","Return"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if "Rest" in moves:
            item="Chesto Berry"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Alomomola
class Alomomola(Pokemon2):
    def __init__(self,name="Alomomola",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=165,atk=75,defense=80,spatk=40,spdef=45,speed=65,hpev=166,atkev=0,defev=252,spatkev=0,spdefev=92,speedev=0,maxiv="No",move="None", ability=random.choice(["Hydration","Regenerator"]),item=random.choice(["Leftovers","Heavy-Duty Boots","Rocky Helmet","Apicot Berry","Weakness Policy"]),weight=69.67):
        color="magenta"
        if move =="None":
            avmoves=["Hydro Pump","Aqua Jet","Ice Beam","Surf","Play Rough","Protect","Chilling Water","Toxic","Scald","Knock Off","Wish","Mirror Coat","Calm Mind","Dive","Whirlpool"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)             
#Passimian
class Passimian(Pokemon2):
    def __init__(self,name="Passimian",type1="Fighting",type2="None",nature="None",level=100,happiness=255,hp=100,atk=120,defense=90,spatk=40,spdef=75,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Defiant","Receiver"]),item=random.choice(["Leftovers"]),weight=182.54):
        if move =="None":
            avmoves=["Giga Impact","Close Combat","Bulk Up","Double-Edge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Lopunny
class Lopunny(Pokemon2):
    def __init__(self,name="Lopunny",type1="Normal",type2="Fighting",nature="None",level=100,happiness=255,hp=65,atk=76,defense=84,spatk=54,spdef=96,speed=105,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Limber","Cute Charm"]),item=random.choice(["Leftovers","Lopunnite","Liechi Berry","Chople Berry","Bright Powder","Focus Band"]),weight=73.41):
        color="yellow"
        if move =="None":
            avmoves=["High Jump Kick","Close Combat","Bulk Up","Double-Edge","Ice Punch","Dizzy Punch","Encore","Return","Low Kick","Sweet Kiss","Thunder Wave","Focus Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Rotom
class MRotom(Pokemon2):
    def __init__(self,name="Mow Rotom",type1="Electric",type2="Grass",nature="None",level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Leftovers"]),weight=0.66):
        color="green"
        if move =="None":
            avmoves=["Volt Switch","Leaf Storm","Discharge","Trick"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Rotom
class FRotom(Pokemon2):
    def __init__(self,name="Fan Rotom",type1="Electric",type2="Flying",nature="None",level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Motor Drive"]),item=random.choice(["Leftovers","King's Rock"]),weight=0.66):
        color="yellow"
        if move =="None":
            avmoves=["Volt Switch","Hurricane","Discharge","Trick","Air Slash","Pain Split","Substitute"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Rotom
class HRotom(Pokemon2):
    def __init__(self,name="Heat Rotom",type1="Electric",type2="Fire",nature="None",level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Leftovers","Flame Orb"]),weight=0.66):
        color="red"
        if move =="None":
            avmoves=["Volt Switch","Flamethrower","Discharge","Will-O-Wisp","Trick","Overheat","Pain Split","Thunderbolt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Rotom
class FrRotom(Pokemon2):
    def __init__(self,name="Frost Rotom",type1="Electric",type2="Ice",nature="None",level=100,happiness=255,hp=50,atk=65,defense=107,spatk=105,spdef=107,speed=86,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Levitate"]),item=random.choice(["Leftovers"]),weight=0.66):
        color="cyan"
        if move =="None":
            avmoves=["Volt Switch","Blizzard","Discharge","Trick","Hidden Power","Ice Beam","Freeze-Dry","Thunderbolt","Frost Breath"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Arctovish
class Arctovish(Pokemon2):
    def __init__(self,name="Arctovish",type1="Water",type2="Ice",nature="None",level=100,happiness=255,hp=90,atk=90,defense=100,spatk=55,spdef=90,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Water Absorb","Ice Body","Slush Rush"]),item=random.choice(["Leftovers","Water Gem"]),weight=385.8):
        color="cyan"
        if move =="None":
            avmoves=["Fishious Rend","Icicle Crash","Crunch","Ancient Power","Freeze-Dry","Psychic Fangs"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color) 
#Arctozolt
class Arctozolt(Pokemon2):
    def __init__(self,name="Arctozolt",type1="Electric",type2="Ice",nature="None",level=100,happiness=255,hp=90,atk=100,defense=90,spatk=90,spdef=55,speed=80,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Volt Absorb","Static","Slush Rush"]),item=random.choice(["Leftovers"]),weight=330.7):
        color="cyan"
        if move =="None":
            avmoves=["Bolt Beak","Discharge","Icicle Crash","Ancient Power","Avalanche"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)   
#Aromatisse
class Aromatisse(Pokemon2):
    def __init__(self,name="Aromatisse",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=101,atk=62,defense=82,spatk=99,spdef=89,speed=29,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Aroma Veil","Fairy Aura"]),item=random.choice(["Leftovers"]),weight=34.17):
        color="magenta"
        if move =="None":
            avmoves=["Draining Kiss","Moonblast","Calm Mind","Psychic"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Ribombee
class Ribombee(Pokemon2):
    def __init__(self,name="Ribombee",type1="Bug",type2="Fairy",nature="None",level=100,happiness=255,hp=60,atk=55,defense=60,spatk=95,spdef=70,speed=124,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Sweet Veil","Shield Dust","Swarm"]),item=random.choice(["Leftovers"]),weight=1.1):
        color="yellow"
        if move =="None":
            avmoves=["Pollen Puff","Moonblast","Quiver Dance","Draining Kiss"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)  
#Comfey
class Comfey(Pokemon2):
    def __init__(self,name="Comfey",type1="Fairy",type2="None",nature="None",level=100,happiness=255,hp=51,atk=52,defense=90,spatk=82,spdef=110,speed=100,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Flower Veil","Triage","Natural Cure"]),item=random.choice(["Leftovers"]),weight=0.66):
        color="magenta"
        if move =="None":
            avmoves=["Draining Kiss","Moonblast","Calm Mind","Grass Knot","Giga Drain"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
#Lurwntis
class Lurantis(Pokemon2):
    def __init__(self,name="Lurantis",type1="Grass",type2="Fighting",nature="None",level=100,happiness=255,hp=70,atk=105,defense=90,spatk=80,spdef=90,speed=45,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Contrary","Leaf Guard"]),item=random.choice(["Leftovers"]),weight=40.79):
        color="magenta"
        if move =="None":
            avmoves=["Solar Blade","Leaf Blade","Synthesis","X-Scissor","Brick Break","Sunny Day","Pollen Puff","Petal Blizzard","Growth","Night Slash","Seed Bomb","Poison Jab","Swords Dance","Substitute","Defog"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Shiinotic
class Shiinotic(Pokemon2):
    def __init__(self,name="Shiinotic",type1="Grass",type2="Fairy",nature="None",level=100,happiness=255,hp=75,atk=45,defense=80,spatk=90,spdef=100,speed=30,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Rain Dish","Effect Spore"]),item=random.choice(["Leftovers"]),weight=25.35):
        color="magenta"
        if move =="None":
            avmoves=["Moonblast","Spore","Synthesis","Giga Drain","Strength Sap","Pollen Puff"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)           
#Brambleghast
class Brambleghast(Pokemon2):
    def __init__(self,name="Brambleghast",type1="Grass",type2="Ghost",nature="None",level=100,happiness=255,hp=55,atk=115,defense=70,spatk=80,spdef=70,speed=90,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Wind Rider","Infiltrator"]),item=random.choice(["Leftovers"]),weight=13.23):
        color="yellow"
        if move =="None":
            avmoves=["Power Whip","Pain Split","Phantom Force","Bullet Seed","Infestation"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)    
#Crabominable
class Crabominable(Pokemon2):
    def __init__(self,name="Crabominable",type1="Fighting",type2="Ice",nature="None",level=100,happiness=255,hp=97,atk=132,defense=77,spatk=62,spdef=67,speed=43,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Iron Fist","Anger Point"]),item=random.choice(["Leftovers"]),weight=396.83):
        color="cyan"
        if move =="None":
            avmoves=["Ice Hammer","Close Combat","Ice Punch","Ice Spinner","Avalanche","Superpower","Dynamic Punch","Iron Defense","Brick Break"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                        
        #Kecleon
class Kecleon(Pokemon2):
    def __init__(self,name="Kecleon",type1="Normal",type2="Ghost",nature="None",level=100,happiness=255,hp=85,atk=110,defense=90,spatk=60,spdef=120,speed=40,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Color Change","Protean","Adaptability"]),item=random.choice(["Leftovers","Ganlon Berry"]),weight=48.5):
        color="green"
        if move =="None":
            avmoves=["Foul Play","Sucker Punch","Shadow Claw","Ancient Power","Psychic","Shadow Sneak","Substitute","Crush Claw","Shadow Claw","Shadow Force","Recover","Fake Out"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                        
#Oranguru
class Oranguru(Pokemon2):
    def __init__(self,name="Oranguru",type1="Normal",type2="Psychic",nature="None",level=100,happiness=255,hp=90,atk=60,defense=110,spatk=90,spdef=80,speed=60,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Inner Focus","Symbiosis","Sage Power"]),item=random.choice(["Leftovers"]),weight=167.55):
        if move =="None":
            avmoves=["Foul Play","Psychic","Trick Room","Nasty Plot","Future Sight","Reflect","Light Screen","Yawn"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        if ("Reflect" or "Light Screen") in moves:
            item="Light Clay "
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)           
#Greedent
class Greedent(Pokemon2):
    def __init__(self,name="Greedent",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=120,atk=95,defense=95,spatk=55,spdef=75,speed=20,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Cheek Pouch"]),item=random.choice(["Sitrus Berry"]),weight=13.2):
        color="red"
        if move =="None":
            avmoves=["Super Fang","Belch","Bullet Seed","Rest","Body Slam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)      
#Oinkologne
class Oinkologne(Pokemon2):
    def __init__(self,name="Oinkologne",type1="Normal",type2="None",nature="None",level=100,happiness=255,hp=110,atk=100,defense=75,spatk=59,spdef=80,speed=65,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Lingering Aroma","Thick Fat","Aroma Veil","Gluttony"]),item=random.choice(["Leftovers"]),weight=264.55):
        color="magenta"
        if move =="None":
            avmoves=["Body Slam","Double-Edge","Yawn","Play Rough"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)          
#Falinks
class Falinks(Pokemon2):
    def __init__(self,name="Falinks",type1="Fighting",type2="Bug",nature="None",level=100,happiness=255,hp=65,atk=100,defense=100,spatk=70,spdef=60,speed=75,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Battle Armor","Defiant"]),item=random.choice(["Leftovers","Salac Berry"]),weight=136.7):
        color="yellow"
        if move =="None":
            avmoves=["No Retreat","Close Combat","Megahorn","Iron Defense","Bulk Up","First Impression","Reversal","Throat Chop"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                                        
#Oricorio
class Oricorio(Pokemon2):
    def __init__(self,name="Oricorio",type1=random.choice(["Fire","Electric","Psychic","Ghost"]),type2="Flying",nature="None",level=100,happiness=255,hp=75,atk=70,defense=70,spatk=98,spdef=70,speed=93,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Dancer"]),item=random.choice(["Focus Sash"]),weight=7.5):
        color="red"
        if move =="None":
            avmoves=["Hurricane","Air Slash","Roost","Acrobatics","Calm Mind","Tailwind","U-turn","Hidden Power"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Revelation Dance"]
        else:
            moves=move
        if type1=="Ghost":
            name="Sensu Oricorio"
            color="blue"
        if type1=="Psychic":
            name="Pa'u Oricorio"
            color="magenta"
        if type1=="Electric":
            name="Pom Pom Oricorio"
            color="yellow"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)                          
#Thievul
class Thievul(Pokemon2):
    def __init__(self,name="Thievul",type1="Dark",type2="None",nature="None",level=100,happiness=255,hp=70,atk=58,defense=58,spatk=87,spdef=92,speed=90,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Stakeout","Unburden"]),item=random.choice(["Leftovers"]),weight=43.9):
        color="red"
        if move =="None":
            avmoves=["Parting Shot","Foul Play","Night Slash","Sucker Punch","Nasty Plot","Snarl","Assurance","Dark Pulse","Shadow Ball","Psychic","Hyper Beam"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)

#Dedenne
class Dedenne(Pokemon2):
    def __init__(self,name="Dedenne",type1="Electric",type2="Fairy",nature="None",level=100,happiness=255,hp=67,atk=58,defense=57,spatk=91,spdef=67,speed=101,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Cheek Pouch","Electric Surge"]),item=random.choice(["Leftovers"]),weight=4.85):
        color="yellow"
        if move =="None":
            avmoves=["Parabolic Charge","Nuzzle","Volt Switch","Play Rough","Thunder","Dazzling Gleam","Draining Kiss","Grass Knot","Hidden Power","Rising Voltage","U-turn","Toxic"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)            
        
#Togedemaru
class Togedemaru(Pokemon2):
    def __init__(self,name="Togedemaru",type1="Electric",type2="Steel",nature="None",level=100,happiness=255,hp=65,atk=108,defense=63,spatk=40,spdef=73,speed=96,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Iron Barbs","Motor Drive","Sturdy","Lightning Rod"]),item=random.choice(["Leftovers","Rocky Helmet"]),weight=7.28):
        if move =="None":
            avmoves=["Zing Zap","Nuzzle","Volt Switch","Play Rough","Wild Charge","Dazzling Gleam","Draining Kiss","Grass Knot","Hidden Power","Rising Voltage","U-turn","Toxic","Spiky Shield","Iron Head"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
#Stunfisk
class Stunfisk(Pokemon2):
    def __init__(self,name="Stunfisk",type1="Ground",type2="Electric",nature="None",level=100,happiness=255,hp=109,atk=66,defense=84,spatk=81,spdef=99,speed=32,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Static","Water Absorb","Sand Veil","Sand Stream"]),item=random.choice(["Leftovers","Rocky Helmet","Passho Berry","Petaya Berry"]),weight=24.25):
        color="yellow"
        if move =="None":
            avmoves=["Volt Switch","Toxic","Earth Power","Stomping Tantrum","Foul Play","Surf","Scald","Flail","Muddy Water","Discharge","Stone Edge"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Stunfisk
class GStunfisk(Pokemon2):
    def __init__(self,name="Galarian Stunfisk",type1="Ground",type2="Steel",nature="None",level=100,happiness=255,hp=109,atk=81,defense=99,spatk=66,spdef=84,speed=32,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Iron Barbs","Filter"]),item=random.choice(["Leftovers","Rocky Helmet"]),weight=45.2):
        color="green"
        if move =="None":
            avmoves=["Iron Defense","Toxic","Earth Power","Stomping Tantrum","Foul Play","Surf","Scald","Sucker Punch"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)       
#Iron Leaves
class Ironleaves(Pokemon2):
    def __init__(self,name="Iron Leaves",type1="Grass",type2="Psychic",nature="None",level=100,happiness=255,hp=90,atk=130,defense=88,spatk=70,spdef=108,speed=104,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability="Quark Drive",item=random.choice(["Booster Energy","Life Orb"]),weight=275.6):
        color="green"
        if move =="None":
            avmoves=["Close Combat","Swords Dance","Sacred Sword","Leaf Blade","Night Slash","Psycho Cut","X-Scissor","Poison Jab","Megahorn","Solar Blade"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Psyblade"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)         
        
class Walkingwake(Pokemon2):
    def __init__(self,name="Walking Wake",type1="Water",type2="Dragon",nature="None",level=100,happiness=255,hp=99,atk=83,defense=91,spatk=125,spdef=83,speed=109,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability="Protosynthesis",item=random.choice(["Booster Energy","Choice Specs"]),weight=617.3):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Crunch","Surf","Hydro Pump","Recover","Hyper Beam","Rain Dance","Scald","Extreme Speed","Light Screen","Tailwind","Calm Mind","Draco Meteor","Dragon Pulse","Aqua Jet","Flamethrower","Snarl","Hurricane","Agility"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Hydro Steam"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)     
        
class Terapagos(Pokemon2):
    def __init__(self,name="Terapagos",type1="Water",type2="Ground",nature="None",level=100,happiness=255,hp=115,atk=55,defense=100,spatk=130,spdef=120,speed=50,hpev=252,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=0,maxiv="No",move="None", ability="Prism Armor",item=random.choice(["Leftovers"]),weight=100):
        color="cyan"
        if move =="None":
            avmoves=["Power Gem","Ice Shard","Iron Defense","Diamond Storm","Scald","Body Press","Heavy Slam","Chilling Water"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
        
class Ogrepon(Pokemon2):
    def __init__(self,name="Ogrepon",type1="Fairy",type2="Grass",nature="None",level=100,happiness=255,hp=70,atk=140,defense=80,spatk=55,spdef=80,speed=145,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability="Prankster",item=random.choice(["Focus Sash"]),weight=100):
        color="green"
        if move =="None":
            avmoves=["Knock Off","Play Rough","Night Slash","Leaf Blade","Taunt","Shadow Sneak","Grass Knot"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Okidogi
class Okidogi(Pokemon2):
    def __init__(self,name="Okidogi",type1="Ground",type2="None",nature="None",level=100,happiness=255,hp=95,atk=124,defense=78,spatk=69,spdef=71,speed=58,hpev=252,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability="Scrappy",item="Leftovers",weight=100):
        color="green"
        if move =="None":
            avmoves=["Hammer Arm","Parting Shot","Bulk Up","Crunch","Close Combat","Night Slash","Grass Knot","Darkest Lariat"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Pyukumuku
class Pyukumuku(Pokemon2):
    def __init__(self,name="Pyukumuku",type1="Water",type2="None",nature="None",level=100,happiness=255,hp=55,atk=60,defense=130,spatk=30,spdef=130,speed=5,hpev=252,atkev=0,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Innards Out","Unaware"]),item="Leftovers",weight=2.65):
        color="magenta"
        if move =="None":
            avmoves=["Toxic","Pain Split","Curse","Recover","Counter","Light Screen","Reflect","Rain Dance","Taunt"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Luvdisc
class Luvdisc(Pokemon2):
    def __init__(self,name="Luvdisc",type1="Water",type2="Fairy",nature="None",level=100,happiness=255,hp=43,atk=30,defense=55,spatk=100,spdef=65,speed=97,hpev=0,atkev=0,defev=0,spatkev=252,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Soul-Heart","Swift Swim"]),item="Leftovers",weight=19.18):
        color="magenta"
        if move =="None":
            avmoves=["Blizzard","Hydro Pump","Draining Kiss","Dazzling Gleam","Flip Turn","Hidden Power","Ice Beam","Rain Dance","Scald","Wish"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Carbink
class Carbink(Pokemon2):
    def __init__(self,name="Carbink",type1="Rock",type2="Fairy",nature="None",level=100,happiness=255,hp=50,atk=50,defense=150,spatk=50,spdef=150,speed=50,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Clear Body","Sturdy"]),item=random.choice(["Leftovers"]),weight=12.57):
        color="cyan"
        if move =="None":
            avmoves=["Protect","Play Rough","Moonblast","Stealth Rock","Meteor Beam","Earth Power","Recover","Stone Edge","Gyro Ball"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Body Press"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Bruxish
class Bruxish(Pokemon2):
    def __init__(self,name="Bruxish",type1="Water",type2="Psychic",nature="None",level=100,happiness=255,hp=68,atk=105,defense=70,spatk=70,spdef=70,speed=92,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=252,speedev=0,maxiv="No",move="None", ability=random.choice(["Dazzling","Strong Jaw","Wonder Skin"]),item="Leftovers",weight=41.89):
        color="magenta"
        if move =="None":
            avmoves=["Toxic","Crunch","Wave Crash","Aqua Jet","Psychic Fangs","Aqua Tail","Reflect","Rain Dance","Taunt","Aqua Fang","Swords Dance"]
            moves=moveset(type1,type2,avmoves,name=name)
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight,color=color)
#Minior
class Minior(Pokemon2):
    def __init__(self,name="Minior",type1="Rock",type2="Flying",nature="None",level=100,happiness=255,hp=60,atk=60,defense=100,spatk=60,spdef=100,speed=60,hpev=252,atkev=0,defev=252,spatkev=0,spdefev=0,speedev=0,maxiv="No",move="None", ability=random.choice(["Shield Down"]),item=random.choice(["Leftovers"]),weight=88.18):
        if move =="None":
            avmoves=["Protect","Play Rough","Moonblast","Stealth Rock","Meteor Beam","Earth Power","Recover","Stone Edge","Gyro Ball","Reflect","Light Screen","U-turn","Rock Tomb"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Shell Smash"]
        else:
            moves=move
        if ("Reflect" or "Light Screen") in moves:
            item="Light Clay"
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)     
#Minior
class Morpeko(Pokemon2):
    def __init__(self,name="Full Belly Morpeko",type1="Electric",type2="Dark",nature="None",level=100,happiness=255,hp=55,atk=110,defense=58,spatk=70,spdef=58,speed=97,hpev=0,atkev=252,defev=0,spatkev=0,spdefev=0,speedev=252,maxiv="No",move="None", ability=random.choice(["Hunger Switch"]),item=random.choice(["Leftovers"]),weight=6.6):
        if move =="None":
            avmoves=["Protect","Thunderbolt","Quick Attack","Agility","Bullet Seed","Crunch","Rest","Thunder Wave","Brick Break"]
            moves=moveset(type1,type2,avmoves,3,name=name)+["Aura Wheel"]
        else:
            moves=move
        super().__init__(name,type1,type2,nature,level,happiness,hp,atk,defense,spatk,spdef,speed,maxiv=maxiv,moves=moves,hpev=hpev,atkev=atkev,defev=defev,spatkev=spatkev,spdefev=spdefev,speedev=speedev, ability=ability,item=item,weight=weight)
class regimon:
    def __init__(self):
        #List of Kanto Pokemon 
        self.kantomon=[Venusaur, Charizard, Blastoise, Butterfree,Beedrill,Pidgeot,Raticate,Fearow,Arbok,Pikachu,Raichu,Sandslash, Nidoqueen, Nidoking, Clefable, Ninetales, Wigglytuff, Vileplume, Parasect, Venomoth, Dugtrio,Meowth,Persian,Golduck, Primeape, Arcanine, Poliwrath, Alakazam, Machamp, Victreebel, Tentacruel,Golem,Rapidash, Slowbro,Dodrio, Dewgong,Muk, Cloyster, Gengar,Hypno,Kingler, Electrode, Exeggutor,Marowak, Hitmonlee, Hitmonchan, Weezing, Rhydon, Chansey, Kangaskhan,Seaking, Starmie,MrMime, Scyther,Jynx,Pinsir,Tauros, Gyarados,Lapras,Ditto,Eevee, Vaporeon, Jolteon, Flareon, Omastar, Kabutops, Aerodactyl, Snorlax, Articuno, Zapdos,Moltres, Dragonite, Mewtwo,Mew]
        #List of Johto Pokemon
        self.johtomon=[Meganium, Typhlosion,Feraligatr,Furret, Noctowl,Ledian,Ariados,Crobat, Lanturn,Xatu, Ampharos, Bellossom, Azumarill, Sudowoodo, Politoed, Jumpluff,Sunflora, Quagsire, Espeon,Umbreon, Slowking, Wobbuffet, Forretress, Steelix, Granbull, Scizor,Shuckle, Heracross, Ursaring, Magcargo, Corsola, Octillery, Delibird, Mantine, Skarmory, Houndoom,Kingdra, Donphan, Porygon2, Smeargle, Hitmontop,Miltank, Blissey,Raikou,Entei,Suicune, Tyranitar,Lugia,Hooh,Celebi]
        self.hoennmon=[]
        self.sinnohmon=[]
        self.unovamon=[]
        self.kalosmon=[]
        self.alolamon=[]
        self.galarmon=[]
        self.hisuimon=[]
        self.paldeamon=[]
regmon=regimon()        