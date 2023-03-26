from attack import *
from moves import *
from intros import intro
from outros import outro
from moreoptions import *
from movelist import *
from battle3 import *
def score2(w,x,y,z,p1,p2,turn):
    xs=ys=ws=zs=colored("ALIVE","green")
    xsa=ysa=wsa=zsa="red"
    xsb=ysb=wsb=zsb="yellow"
    xsc=ysc=wsc=zsc="magenta"
    xsd=ysd=wsd=zsd="blue"
    xse=yse=wse=zse="cyan"
    xa=xb=xc=xd=xe=ya=yb=yc=yd=ye=wa=wb=wc=wd=we=za=zb=zc=zd=ze="white"
    if x.atk!=x.maxspeed:
        if x.speed>x.maxspeed:
            xe="green"
        if x.speed<x.maxspeed:
            xe="red"
    if x.spdef!=x.maxspdef:
        if x.spdef>x.maxspdef:
            xd="green"
        if x.spdef<x.maxspdef:
            xd="red"
    if x.defense!=x.maxdef:
        if x.defense>x.maxdef:
            xb="green"
        if x.defense<x.maxdef:
            xb="red"
    if x.spatk!=x.maxspatk:
        if x.spatk>x.maxspatk:
            xc="green"
        if x.spatk<x.maxspatk:
            xc="red"
    if x.atk!=x.maxatk:
        if x.atk>x.maxatk:
            xa="green"
        if x.atk<x.maxatk:
            xa="red"
    if y.atk!=y.maxspeed:
        if y.speed>y.maxspeed:
            ye="green"
        if y.speed<y.maxspeed:
            ye="red"
    if y.spdef!=y.maxspdef:
        if y.spdef>y.maxspdef:
            yd="green"
        if y.spdef<y.maxspdef:
            yd="red"
    if y.defense!=y.maxdef:
        if y.defense>y.maxdef:
            yb="green"
        if y.defense<y.maxdef:
            yb="red"
    if y.spatk!=y.maxspatk:
        if y.spatk>y.maxspatk:
            yc="green"
        if y.spatk<y.maxspatk:
            yc="red"
    if y.atk!=y.maxatk:
        if y.atk>y.maxatk:
            ya="green"
        if y.atk<y.maxatk:
            ya="red"      
    if w.atk!=w.maxspeed:
        if w.speed>w.maxspeed:
            we="green"
        if w.speed<w.maxspeed:
            we="red"
    if w.spdef!=w.maxspdef:
        if w.spdef>w.maxspdef:
            wd="green"
        if w.spdef<w.maxspdef:
            wd="red"
    if w.defense!=w.maxdef:
        if w.defense>w.maxdef:
            wb="green"
        if w.defense<w.maxdef:
            wb="red"
    if w.spatk!=w.maxspatk:
        if w.spatk>w.maxspatk:
            wc="green"
        if w.spatk<w.maxspatk:
            wc="red"
    if w.atk!=w.maxatk:
        if w.atk>w.maxatk:
            wa="green"
        if w.atk<w.maxatk:
            wa="red"
    if z.atk!=z.maxspeed:
        if z.speed>z.maxspeed:
            ze="green"
        if z.speed<z.maxspeed:
            ze="red"
    if z.spdef!=z.maxspdef:
        if z.spdef>z.maxspdef:
            zd="green"
        if z.spdef<z.maxspdef:
            zd="red"
    if z.defense!=z.maxdef:
        if z.defense>z.maxdef:
            zb="green"
        if z.defense<z.maxdef:
            zb="red"
    if z.spatk!=z.maxspatk:
        if z.spatk>z.maxspatk:
            zc="green"
        if z.spatk<z.maxspatk:
            zc="red"
    if z.atk!=z.maxatk:
        if z.atk>z.maxatk:
            za="green"
        if z.atk<z.maxatk:
            za="red"             
    if w.status=="Drowsy":
        ws=colored("DROWSY","white")
    if z.status=="Drowsy":
        zs=colored("DROWSY","white")            
    if w.status=="Sleep":
        ws=colored("SLEEP","cyan")
    if z.status=="Sleep":
        zs=colored("SLEEP","cyan")
    if w.status=="Frostbite":
        ws=colored("FROSTBITE","cyan")
    if z.status=="Frostbite":
        zs=colored("FROSTBITE","czan")
    if z.status=="Badly Poisoned":
        zs=colored("BADLY POISONED","magenta")
    if z.status=="Poisoned":
        zs=colored("POISONED","magenta")
    if z.status=="Paralyzed":
        zs=colored("PARALYZED","yellow")
    if z.status=="Burned":
        zs=colored("BURNED","red")
    if z.status=="Frozen":
        zs=colored("FROZEN","cyan")
    if w.status=="Badly Poisoned":
        ws=colored("BADLY POISONED","magenta")
    if w.status=="Poisoned":
        ws=colored("POISONED","magenta")
    if w.status=="Paralyzed":
        ws=colored("PARALYZED","yellow")
    if w.status=="Burned":
        ws=colored("BURNED","red")
    if w.status=="Frozen":
        ws=colored("FROZEN","cyan")             
    if x.status=="Drowsy":
        xs=colored("DROWSY","white")
    if y.status=="Drowsy":
        ys=colored("DROWSY","white")            
    if x.status=="Sleep":
        xs=colored("SLEEP","cyan")
    if y.status=="Sleep":
        ys=colored("SLEEP","cyan")
    if x.status=="Frostbite":
        xs=colored("FROSTBITE","cyan")
    if y.status=="Frostbite":
        ys=colored("FROSTBITE","cyan")
    if y.status=="Badly Poisoned":
        ys=colored("BADLY POISONED","magenta")
    if y.status=="Poisoned":
        ys=colored("POISONED","magenta")
    if y.status=="Paralyzed":
        ys=colored("PARALYZED","yellow")
    if y.status=="Burned":
        ys=colored("BURNED","red")
    if y.status=="Frozen":
        ys=colored("FROZEN","cyan")
    if x.status=="Badly Poisoned":
        xs=colored("BADLY POISONED","magenta")
    if x.status=="Poisoned":
        xs=colored("POISONED","magenta")
    if x.status=="Paralyzed":
        xs=colored("PARALYZED","yellow")
    if x.status=="Burned":
        xs=colored("BURNED","red")
    if x.status=="Frozen":
        xs=colored("FROZEN","cyan")            
    print("===================================================================================")
    print(f" {p1.name}:")
    if len(p1.hazard)!=0:
        print(" Hazards: ",end="")
        if "Stealth Rock" in p1.hazard:
            print("🪨 ",end="")
        if "Steel Spikes" in p1.hazard:
            print("📌 ",end="")
        if "Sticky Web" in p1.hazard:
            print("🕸️ ",end="")
        if "Spikes" in p1.hazard:
            print("✴️ "*p1.hazard.count("Toxic Spikes"),end="")
        if "Toxic Spikes" in p1.hazard:
            print("☠️ "*p1.hazard.count("Toxic Spikes"),end="")
        print("")
    if p1.tailwind==True:
        print(f" 🍃 Tailwind({p1.twendturn-turn} turns left)")                   
    if p1.reflect==True:
        print(f" 🟦 Reflect({p1.rfendturn-turn} turns left)")   
    if p1.auroraveil==True:
        print(f" ⬜ Aurora Veil({p1.avendturn-turn} turns left)")
    if p1.lightscreen==True:              
        print(f" 🟪 Light Screen({p1.screenend-turn} turns left)")        
    print(colored(f" {x.name} Lv.{x.level}","white"),f"[{xs}]")
    print(colored(f" HP: ","green")+colored(f"{round(x.hp)}/{x.maxhp}({round((x.hp/x.maxhp)*100,3)}%)","white"))
    if x.status in ["Sleep","Drowsy"]:
        print(" "+"⬜"*int((x.hp/x.maxhp)*25))
    if x.status in ["Poisoned","Badly Poisoned"]:
        print(" "+"🟪"*int((x.hp/x.maxhp)*25))
    if x.status in ["Frozen","Frostbite"]:
        print(" "+"🟦"*int((x.hp/x.maxhp)*25))
    if x.status=="Burned":
        print(" "+"🟧"*int((x.hp/x.maxhp)*25))
    if x.status=="Paralyzed":
        print(" "+"🟨"*int((x.hp/x.maxhp)*25))
    if x.status=="Alive":
        if x.dmax is True:
            print(" "+"🛑"*int((x.hp/x.maxhp)*25))
        if x.dmax is False:
            if 6<=int((x.hp/x.maxhp)*10)<=10:
                print(" "+"🟩"*int((x.hp/x.maxhp)*25))
            if 3<int((x.hp/x.maxhp)*10)<6:
                print(" "+"🟨"*int((x.hp/x.maxhp)*25))
            if int((x.hp/x.maxhp)*10)<=3:
                print(" "+"🟥"*int((x.hp/x.maxhp)*25))
    if x.encore==True:
        print(colored(" || Encore || ","white"),end="")
    if x.taunted==True:
        print(colored(" || Taunt || ","red"),end="") 
    if x.seeded==True:
        print(colored(" || Leech Seed || ","green"),end="")
    if x.salty==True:
        print(colored(" || Salt Cure || ","yellow"),end="")
    if x.flashfire==True:
        print(colored(" || Flash Fire || ","red"),end="")
    if x.grav==True:
        print(colored(" || Gravity || ","magenta"),end="")
    if x.aring==True:
        print(colored(" || Aqua Ring || ","blue"),end="")
    print(end="\n")
    #print("")
    if x.teratype !="None" and x.type2 =="None" and p2.ai is True:
        print(colored(f" Type:{x.teratype} Ability: {x.ability} Item: {x.item} Nature: {x.nature}","white"))
    if x.teratype !="None" and x.type2 !="None" and p2.ai is True:
        print(colored(f" Type:{x.teratype} Ability: {x.ability} Item: {x.item} Nature: {x.nature}","white"))
    if x.teratype =="None" and x.type2 =="None" and p2.ai is True:
        print(colored(f" Type:{x.type1} Ability: {x.ability} Item: {x.item} Nature: {x.nature}","white"))
    if x.teratype =="None" and x.type2 !="None" and p2.ai is True:
        print(colored(f" Type:{x.type1}/{x.type2} Ability: {x.ability} Item: {x.item} Nature: {x.nature}","white"))
    if p2.ai is True:        
        print(colored(f" Atk: ",xsa)+colored(f"{round(x.atk)}({round(x.atkb,3)})",xa)+colored(f" Def: ",xsb)+colored(f"{round(x.defense)}({round(x.defb,3)})",xb)+colored(f" SpA: ",xsc)+colored(f"{round(x.spatk)}({round(x.spatkb,3)})",xc)+colored(f" SpD: ",xsd)+colored(f"{round(x.spdef)}({round(x.spdefb,3)})",xd)+colored(f" Spe: ",xse)+colored(f"{round(x.speed)}({round(x.speedb,3)})",xe))     
    print(colored(f" {w.name} Lv.{w.level}","white"),f"[{ws}]")
    print(colored(f" HP: ","green")+colored(f"{round(w.hp)}/{w.maxhp}({round((w.hp/w.maxhp)*100,3)}%)","white"))
    if w.status in ["Sleep","Drowsy"]:
        print(" "+"⬜"*int((w.hp/w.maxhp)*25))
    if w.status in ["Poisoned","Badly Poisoned"]:
        print(" "+"🟪"*int((w.hp/w.maxhp)*25))
    if w.status in ["Frozen","Frostbite"]:
        print(" "+"🟦"*int((w.hp/w.maxhp)*25))
    if w.status=="Burned":
        print(" "+"🟧"*int((w.hp/w.maxhp)*25))
    if w.status=="Paralyzed":
        print(" "+"🟨"*int((w.hp/w.maxhp)*25))
    if w.status=="Alive":
        if w.dmax is True:
            print(" "+"🛑"*int((w.hp/w.maxhp)*25))
        if w.dmax is False:
            if 6<=int((w.hp/w.maxhp)*10)<=10:
                print(" "+"🟩"*int((w.hp/w.maxhp)*25))
            if 3<int((w.hp/w.maxhp)*10)<6:
                print(" "+"🟨"*int((w.hp/w.maxhp)*25))
            if int((w.hp/w.maxhp)*10)<=3:
                print(" "+"🟥"*int((w.hp/w.maxhp)*25))
    if w.encore==True:
        print(colored(" || Encore || ","white"),end="")
    if w.taunted==True:
        print(colored(" || Taunt || ","red"),end="") 
    if w.seeded==True:
        print(colored(" || Leech Seed || ","green"),end="")
    if w.salty==True:
        print(colored(" || Salt Cure || ","yellow"),end="")
    if w.flashfire==True:
        print(colored(" || Flash Fire || ","red"),end="")
    if w.grav==True:
        print(colored(" || Gravity || ","magenta"),end="")
    if w.aring==True:
        print(colored(" || Aqua Ring || ","blue"),end="")
    print(end="\n")
    #print("")
    if w.teratype !="None" and w.type2 =="None" and p2.ai is True:
        print(colored(f" Type:{w.teratype} Ability: {w.ability} Item: {w.item} Nature: {w.nature}","white"))
    if w.teratype !="None" and w.type2 !="None" and p2.ai is True:
        print(colored(f" Type:{w.teratype} Ability: {w.ability} Item: {w.item} Nature: {w.nature}","white"))
    if w.teratype =="None" and w.type2 =="None" and p2.ai is True:
        print(colored(f" Type:{w.type1} Ability: {w.ability} Item: {w.item} Nature: {w.nature}","white"))
    if w.teratype =="None" and w.type2 !="None" and p2.ai is True:
        print(colored(f" Type:{w.type1}/{w.type2} Ability: {w.ability} Item: {w.item} Nature: {w.nature}","white"))
    if p2.ai is True:        
        print(colored(f" Atk: ",wsa)+colored(f"{round(w.atk)}({round(w.atkb,3)})",wa)+colored(f" Def: ",wsb)+colored(f"{round(w.defense)}({round(w.defb,3)})",wb)+colored(f" SpA: ",wsc)+colored(f"{round(w.spatk)}({round(w.spatkb,3)})",wc)+colored(f" SpD: ",wsd)+colored(f"{round(w.spdef)}({round(w.spdefb,3)})",wd)+colored(f" Spe: ",wse)+colored(f"{round(w.speed)}({round(w.speedb,3)})",we))    
    print("===================================================================================")
    print(f" {p2.name}:")
    if len(p2.hazard)!=0:
        print(" Hazards: ",end="")
        if "Stealth Rock" in p2.hazard:
            print("🪨 ",end="")
        if "Steel Spikes" in p2.hazard:
            print("📌 ",end="")
        if "Sticky Web" in p2.hazard:
            print("🕸️ ",end="")
        if "Spikes" in p2.hazard:
            print("✴️ "*p2.hazard.count("Toxic Spikes"),end="")
        if "Toxic Spikes" in p2.hazard:
            print("☠️ "*p2.hazard.count("Toxic Spikes"),end="")
        print("")
    if p2.tailwind==True:
        print(f" 🍃 Tailwind({p2.twendturn-turn} turns left)")                
    if p2.reflect==True:
        print(f" 🟦 Reflect({p2.rfendturn-turn} turns left)")     
    if p2.auroraveil==True:
        print(f" ⬜ Aurora Veil({p2.avendturn-turn} turns left)")
    if p2.lightscreen==True:        
        print(f" 🟪 Light Screen({p2.screenend-turn} turns left)")               
    print(colored(f" {y.name} Lv.{y.level}","white"),f"[{ys}]")
    print(colored(f" HP: ","green")+colored(f"{round(y.hp)}/{y.maxhp}({round((y.hp/y.maxhp)*100,3)}%)","white"))
    if y.status in ["Sleep","Drowsy"]:
        print(" "+"⬜"*int((y.hp/y.maxhp)*25))
    if y.status in ["Poisoned","Badly Poisoned"]:
        print(" "+"🟪"*int((y.hp/y.maxhp)*25))
    if y.status in ["Frozen","Frostbite"]:
        print(" "+"🟦"*int((y.hp/y.maxhp)*25))
    if y.status=="Burned":
        print(" "+"🟧"*int((y.hp/y.maxhp)*25))
    if y.status=="Paralyzed":
        print(" "+"🟨"*int((y.hp/y.maxhp)*25))
    if y.status=="Alive":
        if y.dmax is True:
            print(" "+"🛑"*int((y.hp/y.maxhp)*25))
        if y.dmax is False:
            if int((y.hp/y.maxhp)*10)>=6:
                print(" "+"🟩"*int((y.hp/y.maxhp)*25))
            if 3<int((y.hp/y.maxhp)*10)<6:
                print(" "+"🟨"*int((y.hp/y.maxhp)*25))
            if int((y.hp/y.maxhp)*10)<=3:
                print(" "+"🟥"*int((y.hp/y.maxhp)*25))
    if y.encore==True:
        print(colored(" || Encore || ","white"),end="")
    if y.taunted==True:
        print(colored(" || Taunt || ","red"),end="") 
    if y.seeded==True:
        print(colored(" || Leech Seed || ","green"),end="")
    if y.salty==True:
        print(colored(" || Salt Cure || ","yellow"),end="")
    if y.grav==True:
        print(colored(" || Gravity || ","magenta"),end="")
    if y.flashfire==True:
        print(colored(" || Flash Fire || ","red"),end="")
    if y.aring==True:
        print(colored(" || Aqua Ring || ","blue"),end="")
    print(end="\n")                
    if y.teratype !="None" and y.type2 =="None" and p1.ai is True:
        print(colored(f" Type:{y.teratype} Ability: {y.ability} Item: {y.item} Nature: {y.nature}","white"))
    if y.teratype !="None" and y.type2 !="None" and p1.ai is True:
        print(colored(f" Type:{y.teratype} Ability: {y.ability} Item: {y.item} Nature: {y.nature}","white"))
    if y.teratype =="None" and y.type2 =="None" and p1.ai is True:
        print(colored(f" Type:{y.type1} Ability: {y.ability} Item: {y.item} Nature: {y.nature}","white"))
    if y.teratype =="None" and y.type2 !="None" and p1.ai is True:
        print(colored(f" Type:{y.type1}/{y.type2} Ability: {y.ability} Item: {y.item} Nature: {y.nature}","white"))
    if p1.ai is True:
        print(colored(f" Atk: ",ysa)+colored(f"{round(y.atk)}({round(y.atkb,3)})",ya)+colored(f" Def: ",ysb)+colored(f"{round(y.defense)}({round(y.defb,3)})",yb)+colored(f" SpA: ",ysc)+colored(f"{round(y.spatk)}({round(y.spatkb,3)})",yc)+colored(f" SpD: ",ysd)+colored(f"{round(y.spdef)}({round(y.spdefb,3)})",yd)+colored(f" Spe: ",yse)+colored(f"{round(y.speed)}({round(y.speedb,3)})",ye))                   
    print(colored(f" {z.name} Lv.{z.level}","white"),f"[{ws}]")
    print(colored(f" HP: ","green")+colored(f"{round(z.hp)}/{z.maxhp}({round((z.hp/z.maxhp)*100,3)}%)","white"))
    if z.status in ["Sleep","Drowsy"]:
        print(" "+"⬜"*int((z.hp/z.maxhp)*25))
    if z.status in ["Poisoned","Badly Poisoned"]:
        print(" "+"🟪"*int((z.hp/z.maxhp)*25))
    if z.status in ["Frozen","Frostbite"]:
        print(" "+"🟦"*int((z.hp/z.maxhp)*25))
    if z.status=="Burned":
        print(" "+"🟧"*int((z.hp/z.maxhp)*25))
    if z.status=="Paralyzed":
        print(" "+"🟨"*int((z.hp/z.maxhp)*25))
    if z.status=="Alive":
        if z.dmax is True:
            print(" "+"🛑"*int((z.hp/z.maxhp)*25))
        if z.dmax is False:
            if 6<=int((z.hp/z.maxhp)*10)<=10:
                print(" "+"🟩"*int((z.hp/z.maxhp)*25))
            if 3<int((z.hp/z.maxhp)*10)<6:
                print(" "+"🟨"*int((z.hp/z.maxhp)*25))
            if int((z.hp/z.maxhp)*10)<=3:
                print(" "+"🟥"*int((z.hp/z.maxhp)*25))
    if z.encore==True:
        print(colored(" || Encore || ","white"),end="")
    if z.taunted==True:
        print(colored(" || Taunt || ","red"),end="") 
    if z.seeded==True:
        print(colored(" || Leech Seed || ","green"),end="")
    if z.salty==True:
        print(colored(" || Salt Cure || ","yellow"),end="")
    if z.flashfire==True:
        print(colored(" || Flash Fire || ","red"),end="")
    if z.grav==True:
        print(colored(" || Gravity || ","magenta"),end="")
    if z.aring==True:
        print(colored(" || Aqua Ring || ","blue"),end="")
    print(end="\n")
    #print("")
    if z.teratype !="None" and z.type2 =="None" and p2.ai is True:
        print(colored(f" Type:{z.teratype} Ability: {z.ability} Item: {z.item} Nature: {z.nature}","white"))
    if z.teratype !="None" and z.type2 !="None" and p2.ai is True:
        print(colored(f" Type:{z.teratype} Ability: {z.ability} Item: {z.item} Nature: {z.nature}","white"))
    if z.teratype =="None" and z.type2 =="None" and p2.ai is True:
        print(colored(f" Type:{z.type1} Ability: {z.ability} Item: {z.item} Nature: {z.nature}","white"))
    if z.teratype =="None" and z.type2 !="None" and p2.ai is True:
        print(colored(f" Type:{z.type1}/{z.type2} Ability: {z.ability} Item: {z.item} Nature: {z.nature}","white"))
    if p2.ai is True:        
        print(colored(f" Atk: ",zsa)+colored(f"{round(z.atk)}({round(z.atkb,3)})",za)+colored(f" Def: ",zsb)+colored(f"{round(z.defense)}({round(z.defb,3)})",zb)+colored(f" SpA: ",zsc)+colored(f"{round(z.spatk)}({round(z.spatkb,3)})",zc)+colored(f" SpD: ",zsd)+colored(f"{round(z.spdef)}({round(z.spdefb,3)})",zd)+colored(f" Spe: ",zse)+colored(f"{round(z.speed)}({round(z.speedb,3)})",ze))

def doublebattle(w,x,y,z,tr1,tr2):
    turn=0
    score2(w,x,y,z,tr1,tr2,turn)         
    
def gymbattle(field):
    gym=[]
    btype="Gym Battle"
    if "Kanto" in field.location:         
        gym=[brock,misty,surge,erika,janine,sabrina,blaine,blue]
    if "Johto" in field.location:
        gym=[falkner,bugsy, whitney, chuck,morty,pryce,janine,clair]
    if "Hoenn" in field.location:
        gym=[roxanne, brawly, wattson, flannery, norman, winona, tate, liza, juan]
    if "Sinnoh" in field.location:
        gym=[roark, gardenia,fantina,wake,maylene,byron,candice,volkner]
    if "Unova" in field.location:
        gym=[random.choice([cilan,chili,cress]),cheren,lenora,roxie,burgh,elesa,clay,skyla,brycen,random.choice([marlon,drayden])]
    if "Kalos" in field.location:
        gym=[viola,grant,korrina,ramos,clemont,valerie,olympia,wulfric]
    if "Alola" in field.location:
        gym=[Lillie,mallow,lana,kiawe,Ilima,hala,olivia,acerola]
    if "Galar" in field.location:
        gym=[milo,nessa,kabu,bea,allister,random.choice([opal,bede]),gordie,melony,random.choice([piers,marnie]),raihan]
    if "Paldea" in field.location:
        gym=[katy,brassius,Iono,kofu,ryme,grusha,tulip]
    p1=players()
    p1.winner=True
    n=0
    while True:        
        if p1.winner==True:
            for i in range(8):
                n+=1
                if p1.winner==True:
                    if n<=8:
                        if n!=1:
                            heal(p1)
                        if n<8:
                            singlebattle(p1,gym[i],btype)
                        
                    if n==8:
                        print(f" 🏆 {p1.name} won all the gym challenges!!!")
                if p1.winner==False or n==8:
                    if n!=8:
                        print(f" {p1.name} couldn't get through {gym[i].name}!!")
                    break 
        if p1.winner==False or n==8:
            break        
        
def tournament():
    print("🏆"*40)
    print(colored(" GROUP STAGE","yellow"))
    btype="Group Stage"
    print("🏆"*40)
    win=0
    n=0
    p1=players()
    p2=players()
    singlebattle(p1,p2,btype)
    skip("None","None","None","None","None")
    while n!=4:
        n+=1
        if n==4:
            print("🏆"*40)
            print(colored(" FINAL","yellow"))
            btype="Final"
            print("🏆"*40)
        if n==3:
            print("🏆"*40)
            print(colored(" SEMI-FINAL","yellow"))
            btype="Semi Final"
            print("🏆"*40)
        if n==2:
            print("🏆"*40)
            print(colored(" QUARTER FINAL","yellow"))
            btype="Quarter Final"
            print("🏆"*40)
        if n==1:
            print("🏆"*40)
            print(colored(" ROUND OF 16","yellow"))
            btype="Round of 16"
            print("🏆"*40)
        if p2.winner==True:
            p1=players()
            heal(p2)
            singlebattle(p1,p2,btype)
            skip("None","None","None","None","None")
        if p1.winner==True:
            p2=players()
            heal(p1)
            singlebattle(p1,p2,btype)
            skip("None","None","None","None","None")
    if p1.winner==True:            
        print(colored(f" 🏆 {p1.name} won the tournament!!!!","yellow"))
    if p2.winner==True:            
        print(colored(f" 🏆 {p2.name} won the tournament!!!!","yellow"))
