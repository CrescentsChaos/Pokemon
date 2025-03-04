import discord
from pokemon import *
from moves import *
async def switch_if_needed(ctx, bot, x, y, tr1, tr2, field, turn):
    if len(tr1.pokemons) > 1 or (x.hp < x.maxhp / 2 and x.use == "Shed Tail"):
        return await switch(ctx, bot, x, y, tr1, tr2, field, turn)
async def stance(ctx,x,y,turn,field,used,em):    
    x.showability=True
    if used not in typemoves.statusmove and x.ability=="Stance Change" and x.sword!=True:
        x.shield=False
        x.sword=True
        em.add_field(name=f"{x.icon} {x.name}'s Stance Change!",value="Aegislash changed to it's blade forme.")
        per=x.hp/x.maxhp
        x.weight=116.84
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/aegislash-blade.gif"
        if x.shiny=="Yes":
            x.sprite="http://play.pokemonshowdown.com/sprites/ani-shiny/aegislash-blade.gif"
        x.hp=60
        x.atk=140
        x.defense=50
        x.spatk=140
        x.spdef=50
        x.speed=60
        calcst(x)
        x.hp=x.maxhp*per
    if used in typemoves.statusmove and x.ability=="Stance Change" and x.shield!=True:
        x.shield=True
        x.sword=False
        em.add_field(name=f"{x.icon} {x.name}'s Stance Change!",value="Aegislash changed to it's shield forme.")
        per=x.hp/x.maxhp
        x.hp=60
        x.sprite="http://play.pokemonshowdown.com/sprites/ani/aegislash.gif"
        if x.shiny=="Yes":
            x.sprite="http://play.pokemonshowdown.com/sprites/ani-shiny/aegislash.gif"
        x.atk=50
        x.defense=140
        x.spatk=50
        x.spdef=140
        x.speed=60
        calcst(x)
        x.hp=x.maxhp*per
async def preattack(ctx,x,y,tr1,tr2,used,choice2,field,turn):
    if y.ability=="Stench" and x.ability!="Long Reach":
        ch=random.randint(1,100)  
        if ch>90:
            x.flinched=True   
    if x.item in ["Kings Rock","Razor Fang"]:
        ch=random.randint(1,100)
        if ch>90 and y.ability not in ["Inner Focus"]:
            if used in typemoves.premove and x.precharge==False:
                pass
            if used in typemoves.premove and x.precharge==True:
                y.flinched=True
            else:
                y.flinched=True
async def accheck(x,y,used,field,em):
    if x.use!="Assist":
        used=x.use
    accuracy=100
    eff=1
    if y.evasion<40:
        y.evasion=40
    if y.evasion>160:
        y.evasion=160
    if x.accuracy<40:
        x.accuracy=40
    if x.accuracy>160:
        x.accuracy=160
    if x.use in typemoves.acc30:
        accuracy=30
    if x.use in typemoves.acc95:
        accuracy=95
    if x.use in typemoves.acc80:
        accuracy=80
    if x.use in typemoves.acc50:
        accuracy=50
    if x.use in typemoves.acc70:
        accuracy=70
    if y.ability=="Wonder Skin" and x.use in typemoves.statusmove and x.use not in typemoves.buffmove:
        eff*=0.5  
    if field.weather in ["Sunny","Sandstorm","Extreme Sunlight"] and x.use in ["Blizzard","Thunder","Hurricane"]:
        accuracy=50
    if field.weather in ["Rainy","Heavy Rain"] and x.use in ["Thunder","Hurricane"]:
        accuracy=100
    if field.weather in ["Hail","Snowstorm"] and x.use=="Blizzard":
        accuracy=100
    if x.use in typemoves.acc90:
        accuracy=90
    if x.item=="Zoom Lens" and x.speed<y.speed:
        eff*=1.2
    if x.ability=="Victory Star":
        eff*=1.1
    if x.item=="Wide Lens":
        eff*=1.1
    if y.item in ["Bright Powder","Lax Incense"]:
        eff*=0.9
    if y.ability=="Tangled Feet" and y.confused==True and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and x.use not in typemoves.abilityigmoves:
        eff*=0.5
    if x.ability=="Hustle":
        eff*=0.8
    if y.ability not in ["Air Lock","Cloud Nine"] and x.ability not in ["Air Lock","Cloud Nine"] and field.weather=="Fog":
        eff*=0.6
    if y.ability=="Snow Cloak" and x.ability not in ["Air Lock","Cloud Nine"] and field.weather in ["Snowstorm","Hail"] and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and x.use not in typemoves.abilityigmoves:
        eff*=0.75
    if y.ability=="Sand Veil" and x.ability not in ["Air Lock","Cloud Nine"] and field.weather=="Sandstorm"and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and x.use not in typemoves.abilityigmoves:
        eff*=0.75
    if x.ability in ["Compound Eyes","Illuminate"]:
        eff*=1.3
    eff*=(y.evasion/100)
    eff*=(x.accuracy/100)
    accuracy=accuracy*eff
    if y.lockon==True:
        accuracy=100    
    if x.use in typemoves.noaccuracy:
        accuracy=100
    if y.use in ["Phantom Force","Shadow Force","Sky Attack","Bounce","Dig","Fly","Dive"] and y.precharge==True and used not in typemoves.buffmove and used!="None" and used not in typemoves.protectmoves:
        accuracy=0
        if y.use in ["Bounce","Fly","Sky Attack"] and x.use in ["Thunder","Hurricane","Sky Uppercut"]:
            accuracy=1
        if "Dig" in y.use and x.use in ["Earthquake","Magnitude"]:
            accuracy=1
            x.atk*=2
    if x.use in typemoves.premove and x.precharge==False and "Power Herb" not in x.item:
        accuracy=100    
    if x.ability in ["No Guard","Deadeye","Space Control"] or y.ability=="No Guard":
        accuracy=100            
    ch=random.randint(1, 100)
    if accuracy<100 and ch>accuracy and x.recharge==False and x.use!="None":
        x.precharge=False
        em.add_field(name=f"Move:",value=f"{x.name} used {x.use}!\n{y.name} avoided the attack!")  
        used="None"
        if x.use in ["High Jump Kick","Axe Kick","Supercell Slam"]:
            a=b=c=r=al=1
            dmg=await physical(x,x.level,x.atk,y.defense,130,a,b,c,r,al)
            x.hp-=dmg/2
            em.add_field(name=f"Recoil:",value=f"{x.name} was hurt by recoil!") 
    return used           
####    
async def moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they):
    if y.shelltrap==True and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
        await shelltrap(ctx,x,y,tr1,em,field,turn)
    if yhp==y.maxhp and y.hp<=0:
        if y.item=="Focus Sash" and used not in typemoves.multimove:
            y.showitem=True
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name} hung on using Focus Sash!")
            y.hp=1
            y.item+="[Used]"
        elif y.ability in ["Sturdy","Nine Lives"] and y.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and used not in typemoves.abilityigmoves and used not in typemoves.multimove:
            y.showability=True
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"{y.name} hung on using {y.ability}!")
            y.hp=1
    if y.item=="Focus Band" and used not in typemoves.multimove and y.hp<=0:
        y.showitem=True
        ch=random.randint(1,10)
        if ch==1:
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name} hung on using Focus Band.!")
            y.hp=1
    if y.item=="Rocky Helmet" and x.ability!="Magic Guard" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            y.showitem=True
            me.hp-=round(me.maxhp/6)
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{x.name} was hurt by {y.icon} {y.name}'s Rocky Helmet!")
            if me.hp<0:
                me.hp=0      
    if y.ability in ["Gooey","Tangling Hair"] and me.ability not in ["Clear Body","Good as Gold"] and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"] and y.hp!=yhp:
        y.showability=True
        await speedchange(em,me,y,-1)        
    elif y.ability=="Flame Body" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"] and y.hp!=yhp:
        ch=random.randint(1,10)
        if ch<3:
            em.add_field(name=f"{y.name}'s {y.ability}!",value="It may burn in contact!")
            await burn(em,x,y,100)      
            y.showability=True
    elif y.ability=="Seed Sower" and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"] and field.terrain!="Grassy" and y.hp!=yhp:
        em.add_field(name=f"{y.name}'s {y.ability}!",value="It may seed grasses in contact!")
        y.showability=True
        em.add_field(name="Grassy Terrain",value="Grass grew to cover the battlefield!")
        field.terrain="Grassy"
        field.grassturn=turn
        field.grassend(x,y)  
    elif y.ability=="Toxic Debris" and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"] and y.hp!=yhp:
        y.showability=True
        if tr1.hazard.count("Toxic Spikes")<3:
            tr1.hazard.append("Toxic Spikes")
            em.add_field(name="Toxic Spikes:",value="Poison spikes were scattered all around the ally team!")     
    elif y.ability in ["Mummy","Lingering Aroma","Wandering Spirit"] and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads","Ability Shield"] and y.hp!=yhp and x.ability not in ["Mummy","Lingering Aroma","Wandering Spirit"]:     
        y.showability=True
        em.add_field(name=f"{y.name}'s {y.ability}!",value="It may infect in contact!")
        x.ability=y.ability    
    elif y.ability=="Cute Charm" and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"] and y.hp!=yhp and x.infatuated is False:
        y.showability=True
        x.infatuated=True
        em.add_field(name=f"{y.name}'s {y.ability}!",value=f"{x.name} is infatuated!")
    elif y.ability=="Perish Body" and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"] and y.hp!=yhp and 0 in (x.perishturn,y.perishturn):   
        y.showability=True
        em.add_field(name=f"{y.name}'s {y.ability}!",value="It may perish in contact!")  
        if x.perishturn==0:
            x.perishturn=4
        if y.perishturn==0:
            y.perishturn=4 
    elif y.ability=="Effect Spore" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"] and y.hp!=yhp:    
        ll=random.randint(1,3)
        if ll==1 and x.status=="Alive":
            ch=random.randint(1,10)
            if ch<=3:
                em.add_field(name=f"{y.name}'s {y.ability}!",value="It may status in contact!")
                await poison(em,y,x,100)
                y.showability=True
        elif ll==2 and x.status=="Alive":
            ch=random.randint(1,10)
            if ch<=3:
                em.add_field(name=f"{y.name}'s {y.ability}!",value="It may status in contact!")
                await sleep(em,y,x,100)
                y.showability=True
        elif ll==3 and x.status=="Alive": 
            ch=random.randint(1,10)
            if ch<=3:
                em.add_field(name=f"{y.name}'s {y.ability}!",value="It may status in contact!")
                await paralyze(em,y,x,100)
                y.showability=True
    elif y.ability=="Static" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"] and y.hp!=yhp:
        ch=random.randint(1,10)
        if ch<=3:
            em.add_field(name=f"{y.name}'s {y.ability}!",value="It may paralyze in contact!")
            await paralyze(em,y,x,100)
            y.showability=True
    elif y.ability=="Poison Point" and me.status=="Alive" and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
        ch=random.randint(1,10)
        if ch<=3:
            em.add_field(name=f"{y.name}'s {y.ability}!",value="It may poison in contact!")
            await poison(em,y,x,100)
            y.showability=True
    elif y.ability=="Magical Dust" and me.ability!="Long Reach" and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
        em.add_field(name=f"{y.name}'s {y.ability}!",value="It may cause magic in contact!")    
        y.showability=True    
        x.primaryType,x.secondaryType="Psychic","???"
    if ((x.ability in ["Poison Touch","Toxic Fangs","Toxic Drain"] and used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]) or (x.ability=="Toxic Chain" and used not in typemoves.statusmove)) and me==x:
        ch=random.randint(1,10)
        if ch<=3:
            em.add_field(name=f"{x.name}'s {x.ability}!",value="It may poison the target!")
            await poison(em,y,x,100)
            y.showability=True       
async def attack(ctx,bot,x,y,tr1,tr2,used,choice2,field,turn): 
    canatk=True   
    #Choice Item        
    if x.choiced is True and x.dmax is False and used!="None":
        if "Used" not in x.item and (x.choicedmove in x.moves and x.dmax is False) and x.status!="Sleep" and x.flinched==False and canatk is True:
            used=x.choicedmove
            x.use=used
        else:
            x.choicedmove="Struggle"
            used="Struggle"       
    c=await movecolor(used,field,x)
    em=discord.Embed(title=f"{tr1.name}:",color=c)   
    #Recharging    
    if x.recharge==True:
        if x.ability!="Time Control":
            em.add_field(name="Rechange:",value=f"{x.name} is recharging.")
            x.recharge=False
            used="None"          
        else:
            x.recharge=False   
    em.set_thumbnail(url=x.sprite) 
    me,they=x,y
    xhp=x.hp
    yhp=y.hp
    hit=1
    pp=1
    #Behind Substitute 
    subr=y
    if x.roost!=False:
        if x.roost=="T1":
            x.primaryType="Flying"
        if x.roost=="T2":
            x.secondaryType="Flying"
        if x.roost=="TR":
            x.teraType="Flying"
        x.roost=False
    if x.taunted==True and used in typemoves.statusmove:
        used="None"
        em.add_field(name="Taunt:",value="Cannot use status moves while taunted!")
        if x.choiced==True:
            used="Struggle"
    #Substitute bypass check        
    if tr2.sub!="None" and used not in typemoves.bypass:
        yhp=tr2.sub.hp
    #Substitue Bypass
    if tr2.sub!="None":
        if tr2.sub.hp>0:
            y=tr2.sub
            if used in typemoves.bypass or x.ability=="Infiltrator":
                y=subr
            if used!="None" and used not in typemoves.soundmoves and used in typemoves.statusmove and (used not in typemoves.buffmove and used not in typemoves.bypass):
                used="None"        
                em.add_field(name="Substitute:",value="Substitute is immune to statusmoves!")
    if used in typemoves.physicalmoves:
        x.atkcat="Physical"
    elif used not in (typemoves.statusmove+typemoves.physicalmoves):
        x.atkcat="Special"
    elif used in typemoves.statusmove:
        x.atkcat="Status"
    if y.ability=="Pressure":
        pp=2
    x.use=used
    if len(x.moves)==0:
        await ctx.send(f" {x.name} has no move left!")
        used="Struggle"
    if x.item=="Custap Berry[Used]" and x.priority==True and used not in typemoves.prioritymove:    
        em.add_field(name=f"{await itemicon(x.item.replace('[Used]',''))} {x.name}'s {x.item}:",value=f"{x.item.replace('[Used]','')} will let {x.name} move first!") 
    if x.status=="Sleep":
        x.sleepturn-=1
        if x.sleepturn==0 or x.ability in ["Insomnia","Vital Spirit"]:
            em.add_field(name="Sleep:",value=f"{x.name} woke up!")
            x.status="Alive"
            x.sleepturn=-1
            x.yawn=False
        else:
            em.add_field(name="Sleep:",value=f"{x.name} is fast asleep!") 
            x.recharge=x.precharge=False 
            if used=="Sleep Talk":
                em.add_field(name=f"Move:",value=f"{x.name} used Sleep Talk!")
                l=[]+x.moves
                l=list(set(l)-{"Sleep Talk"})
                used=random.choice(l)
            else:
                used="None"
    #Paralyzed        
    if x.status=="Paralyzed":
        ch=random.randint(1,100)
        if ch<=25:
            canatk=False
            used="None"
            x.precharge=False
            em.add_field(name=f"{x.name} is paralyzed!",value=f"{x.name} couldn't move because it's paralyzed!")
            x.precharge=x.recharge=False
        else:
            em.add_field(name="Paralysis:",value=f"{x.name} is paralyzed!")
            canatk=True      
    #Checks Freeze                
    elif y.status=="Frozen":
        if used in typemoves.thawmove:       
            em.add_field(name="Status:",value=f"{y.name} thawed out.")
            y.status="Alive"       
    if x.status=="Frozen":
        ch=random.randint(1,10)
        if ch<=3 or used in typemoves.thawmove:
            em.add_field(name="Status:",value=f"{x.name} thawed out.")
            x.status="Alive"
        else:
            em.add_field(name="Frozen:",value=f"{x.name} is frozen solid!")
            x.precharge=x.recharge=False
            used="None"           
    #Multi-turned force moves                   
    if x.fmove==True and x.status!="Sleep" and canatk==True and used!="None":
        used=list(set(x.moves).intersection(["Outrage","Thrash","Petal Dance","Raging Fury"]))[0]       
    if (choice2 in typemoves.buffmove or choice2=="None") and used in typemoves.protectmoves:
        em.add_field(name=f"{x.name} used {used}!",value="It failed.")
        used="None"
    #Consecutive Protect     
    if x.protect=="Pending" and used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct","Silk Trap","Burning Bulwark"]:
        em.add_field(name=f"{x.name} used {used}!",value="It failed.")
        used="None"                 
        x.protect=False   
    await preattack(ctx,x,y,tr1,tr2,used,choice2,field,turn)
    #Destiny Bond cancellation
    if used!="Destiny Bond" and "Destiny Bond" in x.moves:
        y.dbond=False
    #Disguise        
    if y.ability=="Disguise" and used not in typemoves.statusmove+typemoves.buffmove+typemoves.zmoves+typemoves.multimove+typemoves.abilityigmoves and x.ability not in ["Mold Breaker","Teravolt","Turboblaze","Propeller Tail","Stalwart"] and used!="None":
        em.add_field(name=f"{x.name} used {used}!",value=f"{y.icon} {y.name}'s {y.ability}!\n{y.icon} {y.name}'s disguise was busted!")
        y.hp-=round(y.maxhp/8)
        used="None"
        y.ability="Disguise[Used]"
        y.sprite=y.sprite.replace(".gif","-busted.gif")
    #Gigaton Hammer/Blood Moon consecutively            
    #if x.use!="None" and used in ["Gigaton Hammer","Blood Moon"] and x.use in ["Gigaton Hammer","Blood Moon"]:
#        used="None"
#        em.add_field(name="Consecutive use:",value=f"Cannot use {x.use} consecutively!")
    #Stance Change        
    if x.ability=="Stance Change" and used!="None":
        await stance(ctx,x,y,turn,field,used,em)  
    #Destiny Knot
    if x.item=="Destiny Knot" and y.infatuated==False and x.gender!=y.gender:
        y.infatuated=True
        em.add_field(name="Infatuation:",value=f"{y.name} is infatuated!")
    #Infatuation       
    if x.infatuated==True and y.ability=="Cute Charm":
        ch=random.randint(1,100)
        if ch<=25:
            canatk=False
            used="None"
            x.precharge=False
            em.add_field(name=f"{x.name} is infatuated!",value=f"{x.name} is immobilized by love!")
        else:
            em.add_field(name="Infatuation:",value=f"{x.name} is infatuated!")
            canatk=True
    #Checks Flinch    
    if x.flinched==True and x.dmax is False:
            x.precharge=False
            em.add_field(name="Flibch:",value=f"{x.name} flinched and couldn't move.")
            x.precharge=x.recharge=False
            x.flinched=False
            used="None"            
    #Confusion
    if x.confused is True:
        em.add_field(name="Confusion:",value=f" {x.name} is confused!")
        x.confuseendturn-=1
        if x.confuseendturn==0 or y.ability=="Oblivious":
            em.add_field(name="Confusion End!",value=f" {x.name} snapped out of confusion!")
            x.confused=False      
            x.conduseendturn=-1
        ch=random.randint(1,100)  
        if ch>67 and x.dmax==False and x.confused==True:
            canatk=False
            used="None"
            em.add_field(name="Confused!",value=f" {x.name} hurt itself in confusion.")
            r=await randroll()
            x.hp-=await physical(x,x.level,x.atk,x.defense,base=40,a=1,r=r)
            used="None"
        else:
            canatk=True
    #Assist                
    if used=="Assist" and canatk==True:
        x.use="Assist"
        pmoves=[]
        for i in tr1.pokemons:
            if i!=x:
                pmoves+=i.moves
                used=random.choice(pmoves)  
        em.add_field(name=f"{x.name} used Assist!",value=f"It will pick a random ally move! Assist turned into {used}!")          
    #Me First        
    if used=="Me First" and canatk==True:
        if choice2!="None":
            if x.speed>y.speed:
                x.atk*=1.5
                x.spatk*=1.5
                used=choice2
                em.add_field(name=f"{x.name} used Me First!",value=f"It will use opponents move first!")
            else:
                em.add_field(name=f"{x.name} used {used}!",value=f"It failed!")    
    if x.ability=="Prankster" and "Dark" in (y.primaryType,y.secondaryType,y.teraType) and used in typemoves.statusmove:
        used="None"
        em.add_field(name=f"{x.icon} {x.name}'s Prankster!",value=f"{y.name} is immune to {x.name}'s Prankster due to being partially Dark-Type!")                   
    #Good as Gold        
    if y.ability=="Good as Gold" and used in typemoves.statusmove and used not in ["Stealth Rock","Haze","Toxic Spikes","Protect","Spiky Shield","Baneful Bunker","King's Shield","Silk Trap","Burning Bulwark"]+typemoves.healingmoves+typemoves.buffmove:
        em.add_field(name=f"{x.name} used Me First!",value=f"{y.icon} {y.name}'s {y.ability} prevented {used}!")
        used="None"              
    #Encore   
    if x.encore is not False and x.dmax is False:
        if turn==x.encendturn:    
            x.encore=False
        elif x.encore in x.moves:
            used=x.encore
        else:
            used="Struggle"            
    #Safety Googles            
    if used in typemoves.powdermoves and y.item=="Safety Googles":
        em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.icon} {y.name}'s {y.item} protected it from {x.name}'s {used}!")
        used="None"  
    #Soundproof            
    if used in typemoves.soundmoves and y.ability=="Soundproof":
        em.add_field(name=f"{x.name} used {used}!",value=f"{y.icon} {y.name}'s Soundproof!")
        used="None"
    #Bulletproof        
    if used in typemoves.bulletmove and y.ability=="Bulletproof":
        em.add_field(name=f"{x.name} used {used}!",value=f"{y.icon} {y.name}'s Bulletproof!")
        used="None"
    #Fluffy        
    if used in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
        if y.ability=="Fluffy":
            x.atk/=2
    #Priority blocker            
    if (field.terrain=="Psychic" or y.ability in ["Dazzling","Queenly Majesty","Armor Tail"]) and used in typemoves.prioritymove and x.dmax is False:
        if field.terrain!="Psychic":
            em.add_field(name=f"{x.name} used {used}!",value=f"{y.icon} {y.name}'s {y.ability}!\nCannot use priority moves!")
        elif field.terrain=="Psychic":
            em.add_field(name="Psychic Terrain:",value=f"Cannot use priority moves!")
        used="None"
    #Truant
    if x.ability=="Truant" and used!="Slack Off":
        if x.truant==True:
            em.add_field(name=f"{x.icon} {x.name}'s {x.ability}!",value=f"{x.name} is loafing around!")
            used="None"
            x.truant=False
        else:
            x.truant=True
    elif x.ability=="Truant" and used=="Slack Off":
        x.truant=False         
    #Assault Vest                
    if x.item=="Assault Vest" and used in typemoves.statusmove:
        em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"Cannot use status moves while holding an Assault Vest.")
        used="None"        
    
    #Accuracy Check        
    if x.status!="Sleep" and canatk==True:
        if x.use!="Assist":
            x.use=used
        used=await accheck(x,y,used,field,em)         
    #Precharged Moves
    if x.precharge==True and len(x.moves)>0 and "Geomancy" not in x.moves and x.status not in ["Sleep","Frozen"] and canatk==True:
        l=list(set(x.moves).intersection(typemoves.premove))
        if len(l)!=0:
            used=l[0]           
    if used not in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct","Silk Trap","Max Guard","Burning Bulwark"]:
            x.protect=False          
    if y.protect==True and (y.dmax is True and used not in typemoves.buffmove and used not in ["G-Max One Blow","G-Max Rapid Flow"] and used!="None"):
            y.protect="Pending"
            em.add_field(name=f"{x.name} used {used}!",value=f"{y.name} protected itself from {x.name}'s {used}!")
            x.fmoveturn=0
            if used in typemoves.zmoves:
                x.item+="[Used]"
                #x.moves.remove(x.use)
            used="None"
            if used in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Obstruct","Silk Trap","Burning Bulwark"]:
                used="None"     
    #Protection Moves                
    if y.dmax is False and y.protect==True and used not in typemoves.buffmove and (x.ability not in ["Infiltrator","Unseen Fist"]  and used not in ["Shadow Force","Phantom Force","Hyperspace Fury","Hyper Drill","Hyperspace Hole","Mighty Cleave"] and used not in typemoves.maxmovelist and used not in typemoves.zmoves) and used!="None" :
        y.protect="Pending"
        em.add_field(name=f"{x.name} used {used}!",value=f"{y.name} protected itself from {x.name}'s {used}!")
        used="None"
        x.fmoveturn=0
        if x.use in ["Protect","Spiky Shield","King's Shield","Baneful Bunker","Max Guard","Burning Bulwark"]:
            em.add_field(name=f"{x.name} used {used}!",value=f"It failed!")   
            x.protect=False
        if "Spiky Shield" in y.use and x.use in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            x.hp-=round(x.maxhp/8)
            em.add_field(name="Spiky Shield!",value=f"{x.name} was hurt by Spiky Shield.")
        elif "Silk Trap" in y.use and x.use in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            await speedchange(em,x,y,-1)
        elif "Obstruct" in y.use and x.use in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            await spatkchange(em,x,y,-1)
        elif "King's Shield" in y.use and x.use in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            await atkchange(em,x,y,-1)
        elif "Burning Bulwark" in y.use and x.use in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            if x.status=="Alive":
                x.status="Burned"
                em.add_field(name="Burning Bulwark!",value=f"{x.name} was burned.")
        elif "Baneful Bunker" in y.use and x.use in typemoves.contactmoves and x.item not in ["Punching Glove","Protective Pads"]:
            if x.status=="Alive":
                x.status="Badly Poisoned"
                em.add_field(name="Baneful Bunker!",value=f"{x.name} was badly poisoned.")
    #Hit count            
    if used not in typemoves.statusmove and used!="None":
        y.atkby=x.name
        y.atktime+=1             
    function_map = {
    "Shadow Ball": shadowball,
    "Charge": charge,
    "Psych Up": psychup,
    "Perish Song": perishsong,
    "Sonic Slash": sonicslash,
    "Techno Blast":technoblast,
    "Triple Arrows":triplearrows,
    "Double Shock":doubleshock,
    "Burn Up":burnup,
    "Spectral Thief":spectralthief,
    "Soul Robbery":soulrobbery,
    "Jaw Lock":jawlock,
    "Acupressure": acupressure,
    "Psycho Shift": psychoshift,
    "Multi-Attack":multiattack,
    "Skull Bash":skullbash,
    "Geomancy":geomancy,
    "Mortal Spin":mortalspin,
    "G-Max Centiferno":gmaxcentiferno,
    "Tidy Up":tidyup,
    "Judgment":judgment,
    "Flail": flail,
    "Reversal": reversal,
    "Collision Course":collisioncourse,
    "Electro Drift":electrodrift,
    "Flame Charge":flamecharge,
    "Aura Wheel":aurawheel,
    "Shadow Bone":shadowbone,
    "Sky Uppercut":skyuppercut,
    "Steel Beam":steelbeam,
    "Core Enforcer":coreenforcer,
    "Thousand Waves":thousandwaves,
    "Axe Kick":axekick,
    "Aurora Beam":aurorabeam,
    "Bitter Malice":bittermalice,
    "Glaciate":glaciate,
    "Night Daze":nightdaze,
    "Meteor Assault":meteorassault,
    "Diamond Storm":diamondstorm,
    "Earthquake": earthquake,
    "Psychic": psychic,
    "Flying Press":flyingpress,
    "Egg Bomb":eggbomb,
    "Hyperspace Hole":hyperspacehole,
    "Hyperspace Fury":hyperspacefury,
    "No Retreat":noretreat,
    "Psyshield Bash":psyshieldbash,
    "Stone Edge": stoneedge,
    "Mighty Cleave":mightycleave,
    "Sleep Powder":sleeppowder,
    "Stun Spore":stunspore,
    "Sweet Kiss":sweetkiss,
    "Lovely Kiss":lovelykiss,
    "Triple Axel":tripleaxel,
    "Triple Kick":triplekick,
    "Force Palm":forcepalm,
    "Inferno":inferno,
    "Frost Breath":frostbreath,
    "Anchor Shot":anchorshot,
    "Glare":glare,
    "Black Hole Eclipse":blackholeeclipse,
    "Order Up": orderup,
    "Spirit Break": spiritbreak,
    "Pollen Puff":pollenpuff,
    "Moongeist Beam":moongeistbeam,
    "Sunsteel Strike":sunsteelstrike,
    "Apple Acid":appleacid,
    "Bleakwind Storm":bleakwindstorm,
    "Searing Sunraze Smash":sunraze,
    "Menacing Moonraze Maelstrom":moonraze,
    "Soul-Stealing 7-Star Strike":soulstealing,
    "Malicious Moonsault":moonsault,
    "G-Max Gravitas":gmaxgravitas,
    "Springtide Storm":springtidestorm,
    "Sandsear Storm":sandsearstorm,
    "Wildbolt Storm":wildboltstorm,
    "False Surrender": falsesurrender,
    "Breaking Swipe": breakingswipe,
    "Glacial Lance": glaciallance,
    "Gigaton Hammer": gigatonhammer,
    "Matcha Gotcha":matchagotcha,
    "Play Rough": playrough,
    "Synthesis":synthesis,
    "Morning Sun":morningsun,
    "Moonlight":moonlight,
    "Shore Up":shoreup,
    "Jungle Healing":junglehealing,
    "Lunar Blessing":lunarblessing,
    "Blazing Torque":blazingtorque,
    "Combat Torque":combattorque,
    "Noxious Torque":noxioustorque,
    "Magical Torque":magicaltorque,
    "Wicked Torque":wickedtorque,
    "Shell Side Arm":shellsidearm,
    "Razor Shell":razorshell,
    "Outrage":outrage,
    "Thrash":thrash,
    "Crunch": crunch,
    "Hydro Pump": hydropump,
    "Shadow Claw": shadowclaw,
    "Kowtow Cleave": kowtowcleave,
    "Body Slam": bodyslam,
    "Outrage": outrage,
    "Plasma Fists": plasmafists,
    "Mach Punch": machpunch,
    "Will-O-Wisp": willowisp,
    "Low Kick":lowkick,
    "Supercell Slam":supercellslam,
    "Genesis Supernova":genesissupernova,
    "Inferno Overdrive":infernooverdrive,
    "Hydro Vortex":hydrovortex,
    "Thunder Wave": thunderwave,
    "Icicle Crash": iciclecrash,
    "G-Max Snooze":gmaxsnooze,
    "Never-ending Nightmare":neverendingnightmare,
    "Close Combat": closecombat,
    "Ivy Cudgel":ivycudgel,
    "Syrup Bomb":syrupbomb,
    "Superpower": superpower,
    "Bullet Punch": bulletpunch,
    "Extreme Speed": extremespeed,
    "Fire Fang": firefang,
    "Defog":defog,
    "Meteor Mash": meteormash,
    "Blood Moon":bloodmoon,
    "Hydro Steam":hydrosteam,
    "Psyblade":psyblade,
    "Ice Beam": icebeam,
    "Scald": scald,
    "Recover": recover,
    "Air Slash": airslash,
    "Moonblast": moonblast,
    "Behemoth Blade":behemothblade,
    "Behemoth Bash":behemothbash,
    "Destiny Bond":destinybond,
    "Aura Sphere": aurasphere,
    "Dark Pulse": darkpulse,
    "Sludge Bomb": sludgebomb,
    "Rock Tomb": rocktomb,
    "Fire Punch": firepunch,
    "Ice Punch": icepunch,
    "Thunder Punch": thunderpunch,
    "Savage Spin-Out":savagespinout,
    "Thunder Fang": thunderfang,
    "Poison Tail": poisontail,
    "Bug Buzz": bugbuzz,
    "Venom Drench":venomdrench,
    "Toxic Thread":toxicthread,
    "Bloom Doom":bloomdoom,
    "Poison Fang": poisonfang,
    "Bolt Strike": boltstrike,
    "Ice Fang": icefang,
    "Flare Blitz": flareblitz,
    "Horn Drill":horndrill,
    "Guillotine":guillotine,
    "10,000,000 Volt Thunderbolt":tenmillionvolt,
    "Splintered Stormshards":splinteredstormshards,
    "Fissure":fissure,
    "Sheer Cold":sheercold,
    "Seed Flare":seedflare,
    "Barrier":barrier,
    "Make It Rain":makeitrain,
    "Nuzzle":nuzzle,
    "Razor Leaf":razorleaf,
    "Fake Out":fakeout,
    "Upper Hand":upperhand,
    "First Impression":firstimpression,
    "Thunderous Kick":thunderouskick,
    "Trop Kick":tropkick,
    "Smelling Salts":smellingsalts,
    "Spirit Shackle":spiritshackle,
    "Freeze Shock":freezeshock,
    "Strength":strength,
    "Light Of Ruin":lightofruin,
    "Mind Blown":mindblown,
    "Chloroblast":chloroblast,
    "Submission":submission,
    "Mountain Gale":mountaingale,
    "Supersonic Skystrike":supersonicskystrike,
    "Acid Downpour":aciddownpour,
    "All-Out Pummeling":alloutpummeling,
    "Let's Snuggle Forever":letssnuggleforever,
    "Twinkle Tackle":twinkletackle,
    "Subzero Slammer":subzeroslammer,
    "Devastating Drake":devastatingdrake,
    "Shattered Psyche":shatteredpsyche,
    "Pulverizing Pancake":pancake,
    "Breakneck Blitz":breakneckblitz,
    "Sinister Arrow Raid":arrowraid,
    "Oceanic Operetta":operetta,
    "Dig":dig,
    "Bounce":bounce,
    "Fly":fly,
    "Dive":dive,
    "Corkskrew Crash":corkscrewcrash,
    "Tectonic Rage":tectonicrage,
    "Continental Crush":continentalcrush,
    "Throat Chop":throatchop,
    "Barb Barrage":barbbarrage,
    "Beak Blast":beakblast,
    "Misty Explosion": mistyexplosion,
    "Heal Bell": healbell,
    "Aromatherapy": aromatherapy,
    "Explosion": explosion,
    "Avalanche": avalanche,
    "Needle Arm": needlearm,
    "Leaf Blade": leafblade,
    "Drill Peck": drillpeck,
    "Poison Jab": poisonjab,
    "Freeze-Dry": freezedry,
    "Power Gem": powergem,
    "Thunderbolt": thunderbolt,
    "Toxic": toxic,
    "Milk Drink": milkdrink,
    "Dark Void":darkvoid,
    "Slack Off": slackoff,
    "Quick Attack":quickattack,
    "Feint":feint,
    "Glaive Rush":glaiverush,
    "Roost": roost,
    "Heal Order": healorder,
    "Soft-Boiled": softboiled,
    "Light Screen":lightscreen,
    "Reflect":reflect,
    "Aurora Veil":auroraveil,
    "Jungle Healing": junglehealing,
    "Heat Wave": heatwave,
    "Sacred Fire": sacredfire,
    "Boomburst": boomburst,
    "Blizzard": blizzard,
    "Leaf Storm": leafstorm,
    "Make It Rain":makeitrain,
    "Extrasensory": extrasensory,
    "Draco Meteor": dracometeor,
    "Origin Pulse": originpulse,
    "Scorching Sands": scorchingsands,
    "Flamethrower": flamethrower,
    "Pain Split": painsplit,
    "Endeavor": endeavor,
    "Fire Blast": fireblast,
    "Giga Drain": gigadrain,
    "Dream Eater": dreameater,
    "Dragon Rush":dragonrush,
    "Fire Spin":firespin,
    "Whirlpool":whirlpool,
    "Sand Tomb":sandtomb,
    "Infestation":infestation,
    "Dire Claw":direclaw,
    "Shadow Punch":shadowpunch,
    "Poltergeist":poltergeist,
    "Rage Fist":ragefist,
    "Taunt":taunt,
    "Thunder": thunder,
    "Struggle":struggle,
    "Swagger":swagger,
    "Leech Seed":leechseed,
    "Strength Sap":strengthsap,
    "Defend Order":defendorder,
    "Coil":coil,
    "Hone Claws":honeclaws,
    "Mimic":mimic,
    "Captivate":captivate,
    "Autotomize":autotomize,
    "Iron Head": ironhead,
    "Grassy Glide": grassyglide,
    "Drum Beating": drumbeating,
    "Ice Hammer": icehammer,
    "Earth Power": earthpower,
    "Hammer Arm": hammerarm,
    "High Jump Kick": highjumpkick,
    "Pyro Ball": pyroball,
    "Mist Ball": mistball,
    "Luster Purge": lusterpurge,
    "Venoshock": venoshock,
    "Final Gambit": finalgambit,
    "Vine Whip":vinewhip,
    "Lash Out":lashout,
    "Double Team":doubleteam,
    "Smokescreen":smokescreen,
    "Minimize":minimize,
    "Sand-Attack":sandattack,
    "Parabolic Charge":paraboliccharge,
    "Draining Kiss":drainingkiss,
    "G-Max Befuddle":gmaxbefuddle,
    "G-Max Volt Crash":gmaxvoltcrash,
    "G-Max Gold Rush":gmaxgoldrush,
    "G-Max Chi Strike":gmaxchistrike,
    "G-Max Terror":gmaxterror,
    "G-Max Resonance":gmaxresonance,
    "G-Max Cuddle":gmaxcuddle,
    "G-Max Replenish":gmaxreplenish,
    "G-Max Malodor":gmaxmalodor,
    "G-Max Meltdown":gmaxmeltdown,
    "Bitter Blade":bitterblade,
    "Horn Leech":hornleech,
    "Smart Strike":smartstrike,
    "Head Charge":headcharge,
    "Razor Wind":razorwind,
    "X-Scissor": xscissor,
    "Gyro Ball": gyroball,
    "Zen Headbutt": zenheadbutt,
    "Megahorn": megahorn,
    "Ice Shard": iceshard,
    "Jet Punch": jetpunch,
    "Aqua Jet": aquajet,
    "Dragon Hammer": dragonhammer,
    "Ice Spinner": icespinner,
    "Iron Tail": irontail,
    "Slash": slash,
    "Cross Chop": crosschop,
    "Belly Drum":bellydrum,
    "Acid Spray":acidspray,
    "Weather Ball":weatherball,
    "Aqua Cutter": aquacutter,
    "Growth": growth,
    "Acid Armor": acidarmor,
    "Iron Defense": irondefense,
    "Thunder Cage":thundercage,
    "Shelter": shelter,
    "Agility": agility,
    "Rock Polish": rockpolish,
    "Leaf Tornado": leaftornado,
    "Cotton Guard": cottonguard,
    "Psyshock": psyshock,
    "Curse": curse,
    "Haze": haze,
    "Trick Room":trickroom,
    "Stored Power":storedpower,
    "Power Trip":powertrip,
    "Hex":hex,
    "Infernal Parade":infernalparade,
    "Snipe Shot":snipeshot,
    "Signal Beam":signalbeam,
    "Aeroblast":aeroblast,
    "Air Cutter":aircutter,
    "Aerial Ace":aerialace,
    "Fishious Rend":fishiousrend,
    "Bolt Beak":boltbeak,
    "Foul Play":foulplay,
    "Chilling Water":chillingwater,
    "Dizzy Punch":dizzypunch,
    "Confuse Ray":confuseray,
    "Drill Run":drillrun,
    "Electro Ball":electroball,
    "Zap Cannon":zapcannon,
    "Amnesia": amnesia,
    "Ancient Power":ancientpower,
    "Acrobatics": acrobatics,
    "Cross Poison": crosspoison,
    "Wave Crash": wavecrash,
    "Wood Hammer": woodhammer,
    "Brave Bird": bravebird,
    "Bulldoze": bulldoze,
    "Cosmic Power": cosmicpower,
    "Energy Ball": energyball,
    "Psystrike": psystrike,
    "Strange Steam": strangesteam,
    "Swords Dance": swordsdance,
    "Focus Energy":focusenergy,
    "Dragon Cheer":dragoncheer,
    "Rock Slide": rockslide,
    "Quiver Dance": quiverdance,
    "Crabhammer": crabhammer,
    "Tailwind":tailwind,
    "Shell Smash": shellsmash,
    "Focus Blast": focusblast,
    "Victory Dance": victorydance,
    "Calm Mind": calmmind,
    "Expanding Force": expandingforce,
    "Rising Voltage": risingvoltage,
    "Bulk Up": bulkup,
    "Freezing Glare": freezingglare,
    "Nasty Plot": nastyplot,
    "Tail Glow": tailglow,
    "Rising Voltage": risingvoltage,
    "Oblivion Wing": oblivionwing,
    "Grassy Terrain": grassyterrain,
    "Psychic Terrain": psychicterrain,
    "Misty Terrain": mistyterrain,
    "Electric Terrain": electricterrain,
    "Max Overgrowth":maxovergrowth,
    "Max Starfall":maxstarfall,
    "Max Lightning":maxlightning,
    "Max Mindstorm":maxmindstorm,
    "Max Quake":maxquake,
    "Max Steelspike":maxsteelspike,
    "Blaze Kick":blazekick,
    "Max Strike":maxstrike,
    "Max Phantasm":maxphantasm,
    "Max Darkness":maxdarkness,
    "Max Wyrmwind":maxwyrmwind,
    "Max Flutterby":maxflutterby,
    "Max Knuckle":maxknuckle,
    "Max Ooze":maxooze,
    "Max Airstream":maxairstream,
    "Max Geyser":maxgeyser,
    "Max Flare":maxflare,
    "Max Rockfall":maxrockfall,
    "Max Hailstorm":maxhailstorm,
    "Night Slash":nightslash,
    "Esper Wing":esperwing,
    "Psycho Cut":psychocut,
    "Wicked Blow":wickedblow,
    "Storm Throw":stormthrow,
    "Leech Life":leechlife,
    "Encore":encore,
    "Wish":wish,
    "Aqua Ring":aquaring,
    "G-Max Stun Shock":gmaxstunshock,
    "Gigavolt Havoc":gigavolthavoc,
    "Extreme Evoboost":evoboost,
    "Stoked Sparksurfer":sparksurf,
    "Catastropika":catastropika,
    "Guardian of Alola":guardianofalola,
    "Steel Wing":steelwing,
    "Payback":payback,
    "Assurance":assurance,
    "Attack Order":attackorder,
    "Doodle":doodle,
    "Yawn":yawn,
    "Surf":surf,
    "Muddy Water":muddywater,
    "Flash Cannon":flashcannon,
    "Fleur Cannon":fleurcannon,
    "Psycho Boost":psychoboost,
    "Spicy Extract":spicyextract,
    "Recycle":recycle,
    "Skill Swap":skillswap,
    "Trick":trick,
    "Trick-Or-Treat":trickortreat,
    "Forests Curse":forestscurse,
    "Magic Powder":magicpowder,
    "Soak":soak,
    "Tar Shot":tarshot,
    "Fusion Flare":fusionflare,
    "Searing Shot":searingshot,
    "Fiery Wrath":fierywrath,
    "V-Create":vcreate,
    "Steam Eruption":steameruption,
    "Fiery Dance":fierydance,
    "Lumina Crash":luminacrash,
    "Super Fang":superfang,
    "Ruination":ruination,
    "Natures Madness":naturesmadness,
    "Shell Trap":shelltrap,
    "Charm":charm,
    "Scary Face":scaryface,
    "Eerie Impulse":eerieimpulse,
    "G-Max Finale":gmaxfinale,
    "G-Max Smite":gmaxsmite,
    "G-Max Depletion":gmaxdepletion,
    "G-Max One Blow":gmaxoneblow,
    "G-Max Rapid Flow":gmaxrapidflow,
    "Clangorous Soul":csoul,
    "Clanging Scales":cscales,
    "Clangorous Soulblaze":csoulblaze,
    "G-Max Volcalith":gmaxvolcalith,
    "Metal Sound":metalsound,
    "Fake Tears":faketears,
    "Feather Dance":featherdance,
    "Octazooka":octazooka,
    "Fillet Away":filletaway,
    "Headlong Rush":headlongrush,
    "Armor Cannon":armorcannon,
    "Wave Crash":wavecrash,
    "Wood Hammer":woodhammer,
    "Volt Tackle":volttackle,
    "Bolt Strike":boltstrike,
    "Fusion Bolt":fusionbolt,
    "Dazzling Gleam":dazzlinggleam,
    "Lava Plume":lavaplume,
    "Hurricane":hurricane,
    "Overheat":overheat,
    "Blast Burn":blastburn,
    "Hydro Cannon":hydrocannon,
    "Giga Impact":gigaimpact,
    "Prismatic Laser":prismaticlaser,
    "Eternabeam":eternabeam,
    "Rock Wrecker":rockwrecker,
    "Frenzy Plant":frenzyplant,
    "Sparkling Aria":sparklingaria,
    "Head Smash":headsmash,
    "Last Respects":lastrespects,
    "Power Whip":powerwhip,
    "Astral Barrage":astralbarrage,
    "Alluring Voice":alluringvoice,
    "Decorate":decorate,
    "Fickle Beam":ficklebeam,
    "Knock Off":knockoff,
    "Seed Bomb":seedbomb,
    "Crush Claw":crushclaw,
    "Spin Out":spinout,
    "Meteor Beam":meteorbeam,
    "Phantom Force":phantomforce,
    "Sky Attack":skyattack,
    "Heat Crash":heatcrash,
    "Heavy Slam":heavyslam,
    "Grass Knot":grassknot,
    "Hard Press":hardpress,
    "Mystical Fire":mysticalfire,
    "Temper Flare":temperflare,
    "Return":returm,
    "Facade":facade,
    "Lunge":lunge,
    "Pounce":pounce,
    "Skitter Smack":skittersmack,
    "Photon Geyser":photongeyser,
    "Fell Stinger":fellstinger,
    "Dynamic Punch":dynamicpunch,
    "Avalanche":avalanche,
    "Zing Zap":zingzap,
    "Vaccum Wave":vaccumwave,
    "Aqua Tail":aquatail,
    "Body Press":bodypress,
    "Waterfall":waterfall,
    "Flower Trick":flowertrick,
    "Rapid Spin":rapidspin,
    "Dragon Dance":dragondance,
    "G-Max Fireball":gmaxfireball,
    "G-Max Drum Solo":gmaxdrumsolo,
    "G-Max Hydrosnipe":gmaxhydrosnipe,
    "G-Max Foam Burst":gmaxfoamburst,
    "G-Max Sandblast":gmaxsandblast,
    "Spore":spore,
    "Shadow Sneak":shadowsneak,
    "Drain Punch":drainpunch,
    "Sunny Day":sunnyday,
    "Rain Dance":raindance,
    "Sandstorm":sandstorm,
    "Snowscape":snowscape,
    "Gunk Shot":gunkshot,
    "Belch":belch,
    "Water Spout":waterspout,
    "Tera Blast":terablast,
    "Hidden Power":hiddenpower,
    "Eruption":eruption,
    "Crush Grip":crushgrip,
    "Dragon Energy":dragonenergy,
    "Stomping Tantrum":stompingtantrum,
    "Magnitude":magnitude,
    "High Horsepower":highhorsepower,
    "Fire Lash":firelash,
    "Liquidation":liquidation,
    "Mystical Power":mysticalpower,
    "Torch Song":torchsong,
    "Snarl":snarl,
    "Dark Hole":darkhole,
    "Hypnosis":hypnosis,
    "Hyper Voice":hypervoice,
    "Protect":prtect,
    "Spiky Shield":spikyshield,
    "Petal Blizzard":petalblizzard,
    "Baneful Bunker":banefulbunker,
    "Burning Bulwark":burningbulwark,
    "Tri Attack":triattack,
    "Max Guard":maxguard,
    "Obstruct":obstruct,
    "Silk Trap":silktrap,
    "Double-Edge":doubleedge,
    "Relic Song":relicsong,
    "Bubble Beam":bubblebeam,
    "Dragon Claw":dragonclaw,
    "Dragon Pulse":dragonpulse,
    "Grav Apple":gravapple,
    "Petal Dance":petaldance,
    "Shadow Force":shadowforce,
    "Substitute":substitute,
    "Sacred Sword":sacredsword,
    "Draco Barrage":dracobarrage,
    "Electroweb":electroweb,
    "Overdrive":overdrive,
    "Discharge":discharge,
    "Hyper Beam":hyperbeam,
    "Wild Charge":wildcharge,
    "Secret Sword":secretsword,
    "Darkest Lariat":darkestlariat,
    "Magma Storm":magmastorm,
    "Aqua Fang":aquafang,
    "Blue Flare":blueflare,
    "Ice Burn":iceburn,
    "Rest":rest,
    "Precipice Blades":precipiceblades,
    "Revelation Dance":revelationdance,
    "Dragon Ascent":dragonascent,
    "Solar Beam":solarbeam,
    "Electro Shot":electroshot,
    "Solar Blade":solarblade,
    "Burning Jealousy":burningjealousy,
    "Seismic Toss":seismictoss,
    "Night Shade":nightshade,
    "Icy Wind":icywind,
    "Sludge Wave":sludgewave,
    "Hyper Drill":hyperdrill,
    "Lands Wrath":landswrath,
    "Thousand Arrows":thousandarrows,
    "Trailblaze":trailblaze,
    "Aqua Step":aquastep,
    "Counter":counter,
    "Mirror Coat":mirrorcoat,
    "Dynamax Cannon":dynamaxcannon,
    "Spacial Rend":spacialrend,
    "G-Max Wildfire":gmaxwildfire,
    "G-Max Cannonade":gmaxcannonade,
    "G-Max Vine Lash":gmaxvinelash
}
    move_functions = {
    "Stealth Rock": stealthrock,
    "Stone Axe": stoneaxe,
    "G-Max Stonesurge": gmaxstonesurge,
    "Brick Break": brickbreak,
    "G-Max Wind Rage": gmaxwindrage,
    "Psychic Fangs": psychicfangs,
    "Light That Burns The Sky": skyburn,
    "Raging Bull": ragingbull,
    "G-Max Steelsurge": gmaxsteelsurge,
    "Toxic Spikes": toxicspikes,
    "Ceasless Edge": ceaslessedge,
    "Spikes": spikes,
    "Sticky Web": stickyweb
}
    if used in function_map:
        await function_map[used](ctx, x, y, tr1, em, field,turn)
        await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
    elif used in move_functions:
        await move_functions[used](ctx, x, y, tr1, tr2, em, field, turn)
        await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
    elif used=="Surging Strikes":
        hit=0
        while True:
            hit+=1
            await surgingstrikes(ctx,x,y,tr1,em,field,turn)  
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they) 
            if hit==3 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")         
    elif used=="Dual Wingbeat":
        hit=0
        while True:
            hit+=1
            await dualwingbeat(ctx,x,y,tr1,em,field,turn)  
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they) 
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")     
    elif used=="Tachyon Cutter":
        hit=0
        while True:
            hit+=1
            await tachyoncutter(ctx,x,y,tr1,em,field,turn)  
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they) 
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")                 
    elif used=="Bonemerang":
        hit=0
        while True:
            hit+=1
            await bonemerang(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")         
    elif used=="Icicle Spear":
        hitx=random.randint(2,5)
        if x.ability=="Skill Link":
            hitx=5
        elif x.item=="Loaded Dice":
            hitx=random.randint(4,5)
        hit=0
        while True:
            hit+=1
            await iciclespear(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")                
    elif used=="Arm Thrust":
        hitx=random.randint(2,5)
        if x.ability=="Skill Link":
            hitx=5
        elif x.item=="Loaded Dice":
            hitx=random.randint(4,5)
        hit=0
        while True:
            hit+=1
            await armthrust(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")    
    elif used=="Double Hit":
        hitx=random.randint(2,5)
        if x.ability=="Skill Link":
            hitx=5
        elif x.item=="Loaded Dice":
            hitx=random.randint(4,5)
        hit=0
        while True:
            hit+=1
            await doublehit(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")                        
    elif used=="Population Bomb":
        hitx=1
        hit=0
        while True:
            hit+=1
            ch=random.randint(1,10)
            await armthrust(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0 or (ch==1 and x.item!="Wide Lens"):
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")            
    elif used=="Bone Rush":
        hitx=random.randint(2,5)
        if x.ability=="Skill Link":
            hitx=5
        elif x.item=="Loaded Dice":
            hitx=random.randint(4,5)
        hit=0
        while True:
            hit+=1
            await bonerush(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")        
    elif used=="Doom Desire":
        em.add_field(name=f"Move:",value=f"{x.name} used Doom Desire!")    
        if tr2.doom!=0:
            pass
        elif tr2.doom==0:
            tr2.doom=turn+2
            em.add_field(name="Doom Desire:",value=f"{x.name} chose Doom Desire as it's Destiny!")   
            al=1
            r=await randroll()
            c=1
            a=1
            b=1
            tr2.ftmul=await special(x,x.level,x.spatk,y.spdef,140,a,b,c,r,al)   
    elif used=="Future Sight":
        em.add_field(name=f"Move:",value=f"{x.name} used Future Sight!")    
        if tr2.future!=0:
            pass
        elif tr2.future==0:
            tr2.future=turn+2
            em.add_field(name="Future Sight:",value=f"{x.name} foresaw the future!")   
            al=1
            r=await randroll()
            c=1
            a=1
            b=1
            tr2.ftmul=await special(x,x.level,x.spatk,y.spdef,120,a,b,c,r,al)                    
    elif used=="Pin Missile":
        hitx=random.randint(2,5)
        if x.ability=="Skill Link":
            hitx=5
        elif x.item=="Loaded Dice":
            hitx=random.randint(4,5)
        hit=0
        while True:
            hit+=1
            await pinmissile(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")        
    elif used=="Water Shuriken":
        hitx=random.randint(2,5)
        if x.ability=="Skill Link":
            hitx=5
        elif x.item=="Loaded Dice":
            hitx=random.randint(4,5)
        hit=0
        while True:
            hit+=1
            await watershuriken(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")        
    elif used=="Deathroll":
        hitx=random.randint(1,3)
        if x.ability=="Skill Link":
            hitx=3
        elif x.item=="Loaded Dice":
            hitx=random.randint(2,3)
        hit=0
        while True:
            hit+=1
            await deathroll(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")        
    elif used=="Rock Blast":
        hitx=random.randint(2,5)
        if x.ability=="Skill Link":
            hitx=5
        elif x.item=="Loaded Dice":
            hitx=random.randint(4,5)
        hit=0
        while True:
            hit+=1
            await rockblast(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")             
    elif used=="Bullet Seed":
        hitx=random.randint(2,5)
        if x.ability=="Skill Link":
            hitx=5
        elif x.item=="Loaded Dice":
            hitx=random.randint(4,5)
        hit=0
        while True:
            hit+=1
            await bulletseed(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")        
    elif used=="Whirlwind":
        em.add_field(name=f"Move:",value=f"{x.name} used Whirlwind!")  
        if len(tr2.pokemons)>1 and y.ability not in ["Suction Cups","Guard Dog"] and y.dmax is False:
            em.add_field(name=f"Effect:",value=f"{y.name} blew away with the wind.") 
            y.atkb=y.defb=y.spatkb=y.spdefb=y.speedb=0
            l=y
            while True:
                if tr2.sub=="None":
                    y=random.choice(tr2.pokemons)
                    tr2.party=await partyup(tr2,y)
                if tr2.sub!="None":
                    subr=random.choice(tr2.pokemons)
                    tr2.party=await partyup(tr2,subr)
                if y!=l:
                    break
            em.add_field(name="Whirlwind:",value=f"{y.name} was dragged out!")         
            await entryeff(ctx,y,x,tr2,tr1,field,turn)
        await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)            
    elif used=="Dragon Tail":
        await dragontail(ctx,x,y,tr1,em,field,turn)
        if len(tr2.pokemons)>1 and y.ability not in ["Suction Cups","Guard Dog"] and y.dmax is False and "Fairy" not in (y.primaryType ,y.secondaryType ,y.teraType):
            y.atkb=y.defb=y.spatkb=y.spdefb=y.speedb=0
            l=y
            while True:
                if tr2.sub=="None":
                    y=random.choice(tr2.pokemons)
                    tr2.party=await partyup(tr2,y)
                if tr2.sub!="None":
                    subr=random.choice(tr2.pokemons)
                    tr2.party=await partyup(tr2,subr)
                if y!=l:
                    break
            em.add_field(name="Dragon Tail:",value=f"{y.name} was dragged out!")         
            await entryeff(ctx,y,x,tr2,tr1,field,turn)       
        await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)            
    elif used=="Roar":
        em.add_field(name=f"Move:",value=f"{x.name} used Roar!")  
        if len(tr2.pokemons)>1 and y.ability not in ["Suction Cups","Guard Dog"] and y.dmax is False:
            y.atkb=y.defb=y.spatkb=y.spdefb=y.speedb=0
            l=y
            while True:
                if tr2.sub=="None":
                    y=random.choice(tr2.pokemons)
                    tr2.party=await partyup(tr2,y)
                if tr2.sub!="None":
                    subr=random.choice(tr2.pokemons)
                    tr2.party=await partyup(tr2,subr)
                if y!=l:
                    break
            em.add_field(name="Roar:",value=f"{y.name} was dragged out!")         
            await entryeff(ctx,y,x,tr2,tr1,field,turn)           
        await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)                  
    elif used=="Beat Up":
        hitx=len(tr1.pokemons)
        hit=0
        while True:
            hit+=1
            await beatup(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")        
    elif used=="Scale Shot":
        hitx=random.randint(2,5)
        if x.ability=="Skill Link":
            hitx=5
        elif x.item=="Loaded Dice":
            hitx=random.randint(4,5)
        hit=0
        while True:
            hit+=1
            await scaleshot(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==hitx or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")
        await defchange(em,x,x,-1)  
        await speedchange(em,x,x,1)  
    elif used=="Twin Beam":
        hit=0
        while True:
            hit+=1
            await twinbeam(ctx,x,y,tr1,em,field,turn) 
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)  
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")               
    elif used=="Dragon Darts":
        hit=0
        while True:
            hit+=1
            await dragondarts(ctx,x,y,tr1,em,field,turn) 
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)  
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")         
    elif used=="Dual Chop":
        hit=0
        while True:
            hit+=1
            await dualchop(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")    
    elif used=="Double Iron Bash":
        hit=0
        while True:
            hit+=1
            await ironbash(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")                    
    elif used=="Gear Grind":
        hit=0
        while True:
            hit+=1
            await geargrind(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==2 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")            
    elif used=="Triple Dive":
        hit=0
        while True:
            hit+=1
            await tripledive(ctx,x,y,tr1,em,field,turn)   
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
            if hit==3 or y.hp<=0:
                break
        em.add_field(name="Hit:",value=f"It hit {hit} time(s).")            
    elif used=="Sucker Punch":
        if choice2 in typemoves.statusmove or choice2 =="None":
            em.add_field(name=f"{x.name} used Sucker Punch!",value="It failed.")
        else:
            await suckerpunch(ctx,x,y,tr1,em,field,turn) 
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
    elif used=="Thunderclap":
        if choice2 in typemoves.statusmove or choice2 =="None":
            em.add_field(name=f"{x.name} used Thunderclap!",value="It failed.")
        else:
            await thunderclap(ctx,x,y,tr1,em,field,turn)      
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)       
    elif used in ["Parting Shot", "Flip Turn", "Volt Switch", "Chilly Reception", "Shed Tail", "U-turn"]:
        if used=="U-turn":
            await uturn(ctx, x, y, tr1, em, field, turn)
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
        else:
            await eval(used.replace(" ", "").lower())(ctx, x, y, tr1, em, field, turn)
            await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)
        x=await switch_if_needed(ctx, bot, x, y, tr1, tr2, field, turn)
    elif used=="Teleport":
        em.add_field(name=f"Move:",value=f"{x.name} used Teleport!")
        if len(tr1.pokemons)>1:
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
        await moveeff(em,ctx,bot,x,y,tr1,tr2,used,choice2,field,turn,yhp,me,they)            
    else:
        if used!="None":
            em.add_field(name="Error:",value=f"{used} is missing!")                  
    if tr2.sub!="None" and used not in typemoves.soundmoves:
        y=subr
        if tr2.sub.hp>=0 and used not in typemoves.statusmove and tr2.sub.hp!=yhp:
            em.add_field(name="Substitute:",value=f"The substitute took the damage for {subr.name}!")
        if tr2.sub.hp<=0:
            tr2.sub="None"
            em.add_field(name="Substitute:",value="The substitute faded away!")
    if tr2.sub!="None":
        y=subr            
    if y.hp>y.maxhp:
        y.hp=y.maxhp
    if x.hp>x.maxhp:
        x.hp=x.maxhp
    if y.hp<0:
        y.hp=0
    if x.hp<0:
        x.hp=0
    y.dmgtaken=yhp-y.hp
    if y.hp!=yhp and used!="None":
        x.miss=False
    if y.hp==yhp and used=="None":
        x.miss=True
        if x.item=="Blunder Policy":
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"Blunder Policy was used upon miss!")
            item+="[Used]"
            await speedchange(em,x,x,2)
    if "Gulp Missile" in y.ability and y.hp!=yhp:
        if "-" in y.ability:
            y.sprite=y.sprite.split("-")[0]+".gif"
            em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"{y.name} launched something at the target!")
            if x.ability!="Magic Guard":
                x.hp-=(x.maxhp/4)
            if "Pikachu" in y.ability:
                await paralyze(y,x,100)
                y.ability="Gulp Missile"
            if "Arrocuda" in y.ability:
                defchange(x,y,-0.5)
                y.ability="Gulp Missile"            
    if len(x.moves)>=1 and x.use==x.moves[0] and len(x.pplist)>=1:
        if x.pplist[0]==1:
            pp=1
        x.pplist[0]-=pp
    elif len(x.moves)>=2 and x.use==x.moves[1] and len(x.pplist)>=2:
        if x.pplist[1]==1:
            pp=1
        x.pplist[1]-=pp
    elif len(x.moves)>=3 and x.use==x.moves[2] and len(x.pplist)>=3:
        if x.pplist[2]==1:
            pp=1
        x.pplist[2]-=pp
    elif len(x.moves)>=4 and x.use==x.moves[3] and len(x.pplist)>=4:
        if x.pplist[2]==1:
            pp=1
        x.pplist[3]-=pp
    if x.dmax is True and canatk is True:
        if len(x.maxmoves)>=1 and used==x.maxmoves[0]:
            x.pplist[0]-=pp
        if len(x.maxmoves)>=2 and used==x.maxmoves[1]:
            x.pplist[1]-=pp
        if len(x.maxmoves)>=3 and used==x.maxmoves[2]:
            x.pplist[2]-=pp
        if len(x.maxmoves)>=4 and used==x.maxmoves[3]:
            x.pplist[3]-=pp
    per=round(((yhp-y.hp)/y.maxhp)*100,2)
    sper=round(((xhp-x.hp)/x.maxhp)*100,2)
    if xhp!=x.hp and xhp-x.hp<0 and x.ability!="Parental Bond" and x==me:
        em.add_field(name="Regeneration:",value=f"{x.name} regained {-sper}% of its health!")
    if yhp!=y.hp and yhp-y.hp>0 and x.ability!="Parental Bond" and y==they:
        em.add_field(name="Damage:",value=f"{y.name} lost {per}% of its health!")
    if x.hp!=xhp and x==me and x.hp<xhp and sper>0:
        em.add_field(name="Recoil:",value=f"Total damage received {sper}%")  
    if x.dbond is True and y.hp<=0:
        x.hp=0
        em.add_field(name="Effect:",value=f"{y.name} took away {x.name} with it!")
    if y.ability=="Illusion" and "Zoroark" not in y.name and y.hp!=yhp:
        if y.primaryType=="Dark":
            y.name=y.name="Zoroark"
            em.add_field(name=f"{y.name}'s Illusion!",value=f"{y.icon} {y.name}'s Illusion wore off!")
            if x.shiny=="No":
                y.sprite="http://play.pokemonshowdown.com/sprites/ani/zoroark.gif"
            elif x.shiny=="Yes":
                y.sprite="http://play.pokemonshowdown.com/sprites/ani-shiny/zoroark.gif"
        else:
            y.name=y.name="Hisuian Zoroark"
            em.add_field(name=f"{y.name}'s Illusion!",value=f"{y.icon} {y.name}'s Illusion wore off!")
            if x.shiny=="Yes":
                y.sprite="http://play.pokemonshowdown.com/sprites/ani/zoroark-hisui.gif"
            elif x.shiny=="No":
                y.sprite="http://play.pokemonshowdown.com/sprites/ani-shiny/zoroark-hisui.gif"      
    if used in typemoves.contactmoves and y.item=="Air Balloon" and x.item not in ["Punching Glove","Protective Pads"] and used not in typemoves.groundmoves and y.hp!=yhp:
        em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.icon} {y.name}'s Air Balloon popped off!")
        y.item+="[Used]"   
    if yhp!=y.hp and y==they:
        if used not in typemoves.statusmove:
            if y.ability in ["Rough Skin","Iron Barbs","Iron Spikes"] and used in typemoves.contactmoves and x.ability!="Long Reach" and x.item not in ["Punching Glove","Protective Pads"]:
                em.add_field(name=f"{y.name}'s {y.ability}!",value="")
                me.hp-=round((me.maxhp/16),2)
                if me.hp<0:
                    me.hp=0
        elif len(tr2.pokemons)>1 and y.item=="Eject Pack" and used in typemoves.statusmove and x.speed>y.speed:
            y.item+="[Used]"
            while y!=they:
                y=random.choice(tr2.pokemons)
                tr2.party=await partyup(tr2,y)
            await entryeff(ctx,y,x,tr2,tr1,field,turn)   
        elif len(tr1.pokemons)>1 and y.item=="Red Card":
            y.item+="[Used]"
            x=await switch(ctx,bot,x,y,tr1,tr2,field,turn)
        elif len(tr2.pokemons)>1 and y.item=="Eject Button" and x.speed>y.speed:
            y.item+="[Used]"
            while y!=they:
                y=random.choice(tr2.pokemons)
                tr2.party=await partyup(tr2,y)
            await entryeff(ctx,y,x,tr2,tr1,field,turn) 
#LIFE ORB                    
        if me.item=="Life Orb" and me.ability not in ["Magic Guard",'Sheer Force']:
            me.showitem=True
            me.hp-=round(me.maxhp/16)
            em.add_field(name=f"{await itemicon(me.item)} {me.name}'s {me.item}:",value=f"{me.name} lost some of its HP")
            if x.hp<0:
                x.hp=0                
    #Persim    
    if y.item=="Persim Berry" and y.confused==True and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} cured {y.icon} {y.name}'s confusion!")
        y.confused=False
        y.item+="[Used]"     
   #Persim   
    if x.item=="Persim Berry" and x.confused==True and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} cured {x.name}'s confusion!")
        x.confused=False
        x.item+="[Used]"        
    #Cheri        
    if x.item=="Cheri Berry" and x.status=="Paralyzed" and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} cured {x.name}'s paralysis!")
        x.status="Alive"
        x.item+="[Used]"
    #Cheri        
    if y.item=="Cheri Berry" and y.status=="Paralyzed" and y.hp>0 and y.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp*0.33)
        em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} cured {y.icon} {y.name}'s paralysis!")
        y.status="Alive"
        y.item+="[Used]"     
    #Rawst
    if x.item=="Rawst Berry" and x.status=="Burned" and x.hp>0 and x.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} cured {x.name}'s burn!")
        x.status="Alive"
        x.item+="[Used]"
    #Rawst
    if y.item=="Rawst Berry" and y.status=="Burned" and y.hp>0 and y.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp*0.33)
        em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} cured {y.icon} {y.name}'s burn!")
        y.status="Alive"
        y.item+="[Used]"        
    #Chesto 
    if x.item=="Chesto Berry" and x.status=="Sleep" and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} cured {x.name}'s sleep!")
        x.status="Alive"
        x.item+="[Used]"
   #Chesto
    if y.item=="Chesto Berry" and y.status=="Sleep" and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} cured {y.icon} {y.name}'s sleep!")
        y.status="Alive"
        y.item+="[Used]"
   #Aspear
    if x.item=="Aspear Berry" and x.status=="Frozen" and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} cured {x.name}'s freeze!")
        x.status="Alive"
        x.item+="[Used]"
    #Aspear
    if y.item=="Aspear Berry" and y.status=="Frozen" and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} cured {y.icon} {y.name}'s freeze!")
        y.status="Alive"
        y.item+="[Used]"
    #Pecha
    if x.item=="Pecha Berry" and x.status=="Badly Poisoned" and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} cured {x.name}'s poison!")
        x.status="Alive"
        x.item+="[Used]"
    #Pecha
    if y.item=="Pecha Berry" and y.status=="Badly Poisoned" and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} cured {y.icon} {y.name}'s poison!")
        y.status="Alive"
        y.item+="[Used]"
    #Lum
    if x.item=="Lum Berry" and x.status!="Alive"and x.hp>0 and y.ability not in ["Unnerve","As One"]:
        if x.ability=="Cheek Pouch" and x.hp<x.maxhp:
            x.hp+=(x.maxhp*0.33)
        em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.item} cured {x.name}'s status condition!")
        x.status="Alive"
        x.item+="[Used]"        
    #Lum
    if y.item=="Lum Berry" and y.status!="Alive" and y.hp>0 and x.ability not in ["Unnerve","As One"]:
        if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
            y.hp+=(y.maxhp/3)
        em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} cured {y.icon} {y.name}'s status condition!")
        y.status="Alive"
        y.item+="[Used]"
    #Sitrus
    if y.hp<=y.maxhp/2 and y.hp>0:
        if y.item=="Sitrus Berry" and x.ability not in ["Unnerve","As One"]:
            if y.ability=="Ripen":
                y.hp+=round(y.maxhp/2)     
            else:
                y.hp+=round(y.maxhp/4)
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name} restored Hp using its {y.item}!")
            y.item+="[Used]"                
    #Sitrus
    if x.hp<=x.maxhp/2 and x.hp>0:
        if x.item=="Sitrus Berry" and y.ability not in ["Unnerve","As One"]:    
            if x.ability=="Ripen":   
                x.hp+=round(x.maxhp/2)
            else:   
                x.hp+=round(x.maxhp/4)
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.name} restored Hp using its {x.item}!")
            x.item+="[Used]"    
    if x.hp>0:
        if x.item=="Shell Bell" and y.dmgtaken>0 and y.protect==False and x.recharge==False:
            x.hp+=(y.dmgtaken/8)
            em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"{x.name} restored a little HP using its Shell Bell!")            
    if y.hp>0:
        await berry(em,y,x,xhp,yhp,turn)     
        if y.hp<=(y.maxhp/2)  and yhp>(y.maxhp/2):
            if y.ability=="Berserk":
                em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"{y.name} went berserk!")
                await spatkchange(em,y,y,1)
            if y.ability=="Anger Shell":
                em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"{y.name} became extremely angry!")
                await atkchange(em,y,y,2)
                await spatkchange(em,y,y,2)
                await speedchange(em,y,y,2)
                await defchange(em,y,y,-1)
                await spdefchange(em,y,y,-1)
        if y.ability=="Stamina" and y.hp!=yhp and x.hp>0:
            await defchange(em,y,x,1)      
    if y.ability=="Innards Out" and y==they and y.hp<=0:
        em.add_field(name=f"{y.icon} {y.name}'s {y.ability}!",value=f"{y.name} launched a huge punch!")
        x.hp-=yhp    
    if x.item=="Throat Spray" and used in typemoves.soundmoves:
        await spatkchange(em,x,x,1)
        em.add_field(name=f"{x.icon} {x.name}'s {await itemicon(x.item)} {x.item}!",value=f"The Throat Spray raised {x.name}'s Special Attack!")
        x.item+="[Used]"           
    await ctx.send(embed=em)
    return x,y
    
        
        
