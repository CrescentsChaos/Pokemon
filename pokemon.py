import random
from movelist import *
naturelist=("Hardy","Lonely","Adamant","Naughty","Brave", "Bold",'Docile','Impish','Lax','Relaxed' ,'Modest','Mild','Bashful','Rash','Quiet' ,'Calm','Gentle','Careful','Quirky','Sassy', 'Timid','Hasty','Jolly','Naive','Serious')
def stat_calc(stat, individual_value, effort_value, level, spst="None"):
    if spst == "HP":
        new_stat = round((((2 * stat + individual_value + (effort_value * 0.25)) * level) / 100) + level + 10)
    else:
        new_stat = round((((2 * stat + individual_value + (effort_value * 0.25)) * level) / 100) + 5)
    return new_stat
def zmove(x):
    normalzmoves={
    "Normalium-Z": "Breakneck Blitz",
    "Firium-Z": "Inferno Overdrive",
    "Waterium-Z": "Hydro Vortex",
    "Electrium-Z": "Gigavolt Havoc",
    "Grassium-Z": "Bloom Doom",
    "Icium-Z": "Subzero Slammer",
    "Fightinium-Z": "All-Out Pummeling",
    "Poisonium-Z": "Acid Downpour",
    "Groundium-Z": "Tectonic Rage",
    "Flyinium-Z": "Supersonic Skystrike",
    "Psychium-Z": "Shattered Psyche",
    "Buginium-Z": "Savage Spin-Out",
    "Rockium-Z": "Continental Crush",
    "Ghostium-Z": "Never-Ending Nightmare",
    "Dragonium-Z": "Devastating Drake",
    "Darkinium-Z": "Black Hole Eclipse",
    "Steelium-Z": "Corkscrew Crash",
    "Fairium-Z": "Twinkle Tackle"
}
    specialzmoves={
    "Pikashunium-Z":"10,000,000 Volt Thunderbolt",
    "Pikanium-Z": "Catastropika",
    "Decidium-Z": "Sinister Arrow Raid",
    "Incinium-Z": "Malicious Moonsault",
    "Primarium-Z": "Oceanic Operetta",
    "Tapunium-Z": "Guardian of Alola",
    "Marshadium-Z": "Soul-Stealing 7-Star Strike",
    "Aloraichium-Z": "Stoked Sparksurfer",
    "Snorlium-Z": "Pulverizing Pancake",
    "Eevium-Z": "Extreme Evoboost",
    "Mewnium-Z": "Genesis Supernova",
    "Lycanium-Z": "Splintered Stormshards",
    "Kommonium-Z": "Clangorous Soulblaze",
    "Solganium-Z": "Searing Sunraze Smash",
    "Lunalium-Z": "Menacing Moonraze Maelstrom",
    "Ultranecrozium-Z": "Light That Burns The Sky",
    "Mimikium-Z":"Let's Snuggle Forever"}
    if x.name=="Pikachu" and x.item=="Pikashunium-Z" and "Thunderbolt" in x.moves:
        return specialzmoves[x.item]
    elif x.name=="Pikachu" and x.item=="Pikanium-Z" and "Volt Tackle" in x.moves:
        return specialzmoves[x.item]    
    elif x.name=="Decidueye" and x.item=="Decidium-Z" and "Spirit Shackle" in x.moves:
        return specialzmoves[x.item]  
    elif x.name=="Incineroar" and x.item=="Incinium-Z" and "Darkest Lariat" in x.moves:
        return specialzmoves[x.item]
    elif x.name=="Primarina" and x.item=="Primarium-Z" and "Sparkling Aria" in x.moves:
        return specialzmoves[x.item]    
    elif "Tapu " in x.name and x.item=="Tapunium-Z" and "Natures Madness" in x.moves:
        return specialzmoves[x.item]   
    elif x.name=="Marshadow" and x.item=="Marshadium-Z" and "Spectral Thief" in x.moves:
        return specialzmoves[x.item]     
    elif x.name=="Alolan Raichu" and x.item=="Aloraichium-Z" and "Thunderbolt" in x.moves:
        return specialzmoves[x.item]    
    elif x.name=="Snorlax" and x.item=="Snorlium-Z" and "Giga Impact" in x.moves:
        return specialzmoves[x.item] 
    elif ("eon" in x.name or x.name=="Eevee") and x.item=="Eevium-Z" and "Last Resort" in x.moves:
        return specialzmoves[x.item]
    elif x.name=="Mew" and x.item=="Mewnium-Z" and "Psychic" in x.moves:
        return specialzmoves[x.item]
    elif "Lycanroc" in x.name and x.item=="Lycanium-Z" and "Stone Edge" in x.moves:
        return specialzmoves[x.item]
    elif x.name=="Kommo-O" and x.item=="Kommonium-Z" and "Clanging Scales" in x.moves:
        return specialzmoves[x.item]
    elif x.name=="Solgaleo" and x.item=="Solganium-Z" and "Sunsteel Strike" in x.moves:
        return specialzmoves[x.item]
    elif x.name=="Lunala" and x.item=="Lunalium-Z" and "Moongeist Beam" in x.moves:
        return specialzmoves[x.item]
    elif "Necrozma" in x.name and x.item=="Ultranecrozium-Z" and "Photon Geyser" in x.moves:
        return specialzmoves[x.item]
    elif "Mimikyu" in x.name and x.item=="Mimikium-Z" and "Play Rough" in x.moves:
        return specialzmoves[x.item]
    elif x.item not in specialzmoves:
        if "m-Z" in x.item and "Used" not in x.item:
            return normalzmoves[x.item]    
    else:
        x.zuse=False
        return "None"
                    
def maxmovemaker(self,typem=typemoves):
    maxmove=[]
    gm="None"
    for i in self.moves:
        if i in typem.dragonmoves:
            gm="Max Wyrmwind"
            if "Duraludon" in self.name:
                gm="G-Max Depletion"
        elif i in typem.normalmoves:
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
        elif i in typem.steelmoves:
            gm="Max Steelspike"
            if "Copperajah" in self.name:
                gm="G-Max Steelsurge"
            if "Melmetal" in self.name:
                gm="G-Max Meltdown"
        elif i in typem.fairymoves:
            gm="Max Starfall"
            if "Hatterene" in self.name:
                gm="G-Max Smite"
            if "Alcremie" in self.name:
                gm="G-Max Finale"
        elif i in typem.rockmoves:
            gm="Max Rockfall"
            if "Coalossal" in self.name:
                gm="G-Max Volcalith"
        elif i in typem.groundmoves:
            gm="Max Quake"
            if "Sandaconda" in self.name:
                gm="G-Max Sandblast"
        elif i in typem.ghostmoves:
            gm="Max Phantasm"
            if "Gengar" in self.name:
                gm="G-Max Terror"
        elif i in typem.grassmoves:
            gm="Max Overgrowth"
            if "Venusaur" in self.name:
                gm="G-Max Vine Lash"
            if "Flapple" in self.name:
                gm="G-Max Tartness"
            if "Appletun" in self.name:
                gm="G-Max Sweetness"
            if "Rillaboom" in self.name:
                gm="G-Max Drum Solo"
        elif i in typem.poisonmoves:
            gm="Max Ooze"
            if "Garbodor" in self.name:
                gm="G-Max Malodor"
        elif i in typem.psychicmoves:
            gm="Max Mindstorm"
            if "Orbeetle" in self.name:
                gm="G-Max Gravitas"
        elif i in typem.electricmoves:
            gm="Max Lightning"
            if "Pikachu" in self.name:
                gm="G-Max Volt Crash"
            if "Toxtricity" in self.name:
                gm="G-Max Stun Shock"
        elif i in typem.fightingmoves:
            gm="Max Knuckle"
            if "Machamp" in self.name:
                gm="G-Max Chi Strike"
        elif i in typem.icemoves:
            gm="Max Hailstorm"
            if "Lapras" in self.name:
                gm="G-Max Resonance"
        elif i in typem.watermoves:
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
        elif i in typem.bugmoves:
            gm="Max Flutterby"
            if "Butterfree" in self.name:
                gm="G-Max Befuddle"
        elif i in typem.darkmoves:
            gm="Max Darkness"
            if "Grimmsnarl" in self.name:
                gm="G-Max Snooze"
            if "Single" in self.name:
                gm="G-Max One Blow"
        elif i in typem.flyingmoves:
            gm="Max Airstream"
            if "Corviknight" in self.name:
                gm="G-Max Wind Rage"
        elif i in typem.firemoves:
            gm="Max Flare"
            if "Charizard" in self.name:
                gm="G-Max Wildfire"
            if "Cinderace" in self.name:
                gm="G-Max Fireball"
            if "Centiskorch" in self.name:
                gm="G-Max Centiferno"
        if i in typem.statusmove:
            gm="Max Guard"                
        maxmove.append(gm)
    return maxmove	
def moveset(moves):
    moves=eval(moves)
    result=[]
    if len(moves)>4:
        while len(result)<4:
            x=random.choice(moves)
            if x not in result:
                result.append(x)
        return result          
    else:
        return moves          
class Pokemon:
    def __init__(self,name="MissingNo.",primaryType="???",nickname="No",secondaryType="???",teraType="???",level=100,nature="None",happiness=255,hp=0,atk=0,defense=0,spatk=0,spdef=0,speed=0,hpiv=0,atkiv=0,defiv=0,spatkiv=0,spdefiv=0,speediv=0,hpev=0,atkev=0,defev=0,spatkev=0,spdefev=0,speedev=0,ability="Unknown,Known",moves="Moves,M,N,P,U",maxiv="No",shiny="No",sprite="url",backsprite="url",item="None",gender="None",tera="???",catchdate="Unknown",weight=100,icon="<:000:1127112083792728074>",m1pp=32,m2pp=32,m3pp=32,m4pp=32,mx1pp=32,mx2pp=32,mx3pp=32,mx4pp=32,height=1.5):
        self.name=name
        self.status="Alive"
        self.primaryType=primaryType 
        self.secondaryType=secondaryType
        self.teraType=teraType
        self.tera=tera
        if self.tera=="???":
            self.tera=random.choice([self.primaryType,self.secondaryType])
            if self.tera=="???":
                self.tera=self.primaryType
        self.level=level
        self.nature=nature
        if self.nature=="None":
            self.nature=random.choice(naturelist)
        self.happiness=happiness
        self.hp=hp
        self.nickname=nickname
        self.nickname=self.nickname.replace(" <:favorite:1144122202942357534>","")
        if self.nickname=="No":
            self.nickname=self.name
        self.atk=atk
        self.defense=defense
        self.spatk=spatk
        self.shield=True
        self.sword=False
        self.spdef=spdef
        self.weight=weight
        self.maxend=-1
        self.protect=False
        self.miss=False
        self.roost=False
        self.infatuated=False
        self.salty=False
        self.speed=speed
        self.catchdate=catchdate
        self.height=height
        self.maxhp=hp
        self.maxatk=atk
        self.maxdef=defense
        self.maxspatk=spatk
        self.maxspdef=spdef
        self.speed=speed
        self.hpiv=hpiv
        self.atkiv=atkiv
        self.defiv=defiv
        self.spatkiv=spatkiv
        self.spdefiv=spdefiv
        self.speediv=speediv
        self.hpev=hpev
        self.atkev=atkev
        self.defev=defev
        self.spatkev=spatkev
        self.spdefev=spdefev
        self.speedev=speedev
        self.hpb=0
        self.atkb=0
        self.defb=0
        self.spatkb=0
        self.spdefb=0
        self.speedb=0
        self.atktime=0
        self.critrate=1
        self.fenergy=False
        self.dcheer=False
        self.lockon=False
        self.item=item
        self.dmgtaken=0
        self.confuseeendturn=-1
        self.use="None"
        self.perishturn=0
        self.evasion=100
        self.accuracy=100
        self.encore=False
        self.encendturn=0
        self.atktime=0
        self.dbond=False
        self.gsprite="None"
        self.yawn=False
        self.charged=False
        self.truant=False
        self.atkby=None
        self.fmove=False
        self.fmoveturn=0
        self.bullrush=False
        self.yawn=False
        self.flinched=False
        self.taunted=False
        self.taunturn=0
        self.canfakeout=True
        self.seeded=False
        self.precharge=False
        self.confused=False
        self.recharge=False
        self.flashfire=False
        self.tarshot=False
        self.aring=False
        self.grav=False
        self.gravendturn=-1
        self.sleepturn=-1
        self.toxicCounter=0
        self.choiced="None"
        self.syrup=False
        self.showitem=False
        self.showability=False
        self.shelltrap=False
        self.choicedmove="None"
        self.priority=False
        self.atktype="???"
        self.atkcat="???"
        self.icon=icon
        self.ability=ability
        self.moves=moves
        self.moves=moveset(self.moves)
        self.zmove="None"
        self.zuse=False
        if "m-Z" in self.item:
            self.zuse=True
            self.zmove=zmove(self)
        self.maxmoves=maxmovemaker(self,typemoves)
        #Volcalith
        self.vcdmg=False
        self.vcendturn=0
        #Vine Lash
        self.vldmg=False
        self.vlendturn=0
        #Magma Storm
        self.magmadmg=False
        self.magmaendturn=0
        #Wildfire
        self.wfdmg=False
        self.wfendturn=0
        #Cannonade
        self.cndmg=False
        self.cnendturn=0
        #gravity
        self.grav=False
        self.gravendturn=0
        #Centi
        self.cntdmg=False
        self.cntendturn=0
        self.infestation=0
        self.cursed=False
        self.trap=False
        self.sandtomb=0
        self.whirlpool=0
        self.firespin=0
        self.lostmoves=[]
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
        self.totaliv=round(((self.hpiv+self.atkiv+self.defiv+self.spatkiv+self.spdefiv+self.speediv)/186)*100,2)
        self.totalev=(self.hpev+self.atkev+self.defev+self.spatkev+self.spdefev+self.speedev)
        self.ability=(random.choice(self.ability.split(","))).strip()
        self.gender=gender
        self.gender=random.choice(self.gender.split(","))
        self.sprite=sprite
        if self.name in ["Jellicent","Pyroar","Unfezant","Meowstic","Xatu","Wobbuffet","Ambipom","Basculegion","Beautifly","Bibarel","Blaziken","Cacturne","Camerupt","Donphan","Dustox","Floatzel","Garchomp","Heracross","Hippowdon","Houndoom","Indeedee","Kricketune","Ledian","Ludicolol","Lumineon","Luxray","Mamoswine","Medicham","Meganium","Milotic","Octillery","Oinkologne","Pachirisu","Pikachu","Politoed","Quagsire","Raticate","Relicanth","Rhydon","Rhyperior","Scizor","Scyther","Shiftry","Staraptor","Steelix","Sudowoodo","Swalot","Tangrowth","Toxicroak","Ursaring","Weavile"] and self.gender=="Female":
            self.sprite=self.sprite.replace(".gif","-f.gif")
        self.backsprite="http://play.pokemonshowdown.com/sprites/ani-back/"+self.sprite.split("/")[-1]
        self.maxiv=maxiv
        self.shiny=shiny
        if maxiv=="Alpha":
            if "Alpha" not in self.nickname and self.nickname==self.name:
                self.nickname=self.nickname+" <:alpha:1127167307198758923>"
        if self.shiny=="Yes":
            self.sprite="http://play.pokemonshowdown.com/sprites/ani-shiny/"+self.sprite.split("/")[-1]
            self.backsprite="http://play.pokemonshowdown.com/sprites/ani-back-shiny/"+self.sprite.split("/")[-1]
            if "Shiny" not in self.nickname and self.nickname==self.name:
                self.nickname=self.nickname+" <:shiny:1127157664665837598>"           
        self.dmax=False
        self.typechange()
        calcst(self)
        if self.maxiv=="Yes":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=31,31,31,31,31,31
        elif self.maxiv=="Alpha":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=random.randint(15,31),random.randint(15,31),random.randint(15,31),random.randint(15,31),random.randint(15,31),random.randint(15,31)
        elif self.maxiv=="No":
            self.hpiv,self.atkiv,self.defiv,self.spatkiv,self.spdefiv,self.speediv=random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31) 
    def typechange(self):
        if self.name=="Ogerpon":
            if self.item=="Hearthflame Mask":
                self.tera="Fire"
                self.ability="Mold Breaker"
                self.secondaryType="Fire"
                self.sprite="https://cdn.discordapp.com/attachments/1102579499989745764/1151383775759056896/ezgif.com-resize_3.png"
            elif self.item=="Wellspring Mask":
                self.tera="Water"
                self.ability="Water Absorb"
                self.secondaryType="Water"
                self.sprite="https://cdn.discordapp.com/attachments/1102579499989745764/1151383766623850506/ezgif.com-resize_2.png"
            elif self.item=="Cornerstone Mask":
                self.tera="Rock"
                self.ability="Sturdy"
                self.secondaryType="Rock"
                self.sprite="https://cdn.discordapp.com/attachments/1102579499989745764/1151383783556255814/ezgif.com-resize_4.png"
            else:
                self.tera="Grass"
                self.ability="Defiant"
                self.sprite="https://cdn.discordapp.com/attachments/1102579499989745764/1151383758000365658/ezgif.com-resize_1.png"
        elif self.ability=="RKS System" and self.item!="None" and "Memory" in self.item:
            self.primaryType=self.item.split(" ")[0]
            self.sprite=f"http://play.pokemonshowdown.com/sprites/ani/silvally-{self.primaryType.lower()}.gif"
        elif self.ability=="Multitype" and self.item!="None":
            if self.item=="Zap Plate":
                self.primaryType="Electric"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-electric.gif"
            elif self.item=="Toxic Plate":
                self.primaryType="Poison"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-poison.gif"
            elif self.item=="Stone Plate":
                self.primaryType="Rock"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-rock.gif"
            elif self.item=="Spooky Plate":
                self.primaryType="Ghost"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-ghost.gif"
            elif self.item=="Splash Plate":
                self.primaryType="Water"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-water.gif"
            elif self.item=="Sky Plate":
                self.primaryType="Flying"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-flying.gif"
            elif self.item=="Pixie Plate":
                self.primaryType="Fairy"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-fairy.gif"
            elif self.item=="Mind Plate":
                self.primaryType="Psychic"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-psychic.gif"
            elif self.item=="Iron Plate":
                self.primaryType="Steel"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-steel.gif"
            elif self.item=="Insect Plate":
                self.primaryType="Bug"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-bug.gif"
            elif self.item=="Icicle Plate":
                self.primaryType="Ice"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-ice.gif"
            elif self.item=="Flame Plate":
                self.primaryType="Fire"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-fire.gif"
            elif self.item=="Fist Plate":
                self.primaryType="Fighting"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-fighting.gif"
            elif self.item=="Earth Plate":
                self.primaryType="Ground"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-ground.gif"
            elif self.item=="Dread Plate":
                self.primaryType="Dark"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-dark.gif"
            elif self.item=="Draco Plate":
                self.primaryType="Dragon"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-dragon.gif"
            elif self.item=="Meadow Plate":
                self.primaryType="Grass"
                self.sprite="http://play.pokemonshowdown.com/sprites/ani/arceus-grass.gif"
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
def calcst(self):
    "Calculates Stats"
    self.maxhp =self.hp= stat_calc(self.hp,self.hpiv,self.hpev,self.level,"HP")
    self.maxatk =self.atk= stat_calc(self.atk,self.atkiv,self.atkev,self.level)
    self.maxdef=self.defense=stat_calc(self.defense,self.defiv,self.defev,self.level)
    self.maxspatk = self.spatk=stat_calc(self.spatk,self.spatkiv,self.spatkev,self.level)
    self.maxspdef = self.spdef=stat_calc(self.spdef,self.spdefiv,self.spdefev,self.level)
    self.maxspeed=self.speed=stat_calc(self.speed,self.speediv,self.speedev,self.level)
    self.natureboost()
    self.hp=self.maxhp
    if self.name=="Shedinja":
        self.hp=self.maxhp=1
    self.maxtotal=self.maxhp+self.maxatk+self.maxdef+self.maxspatk+self.maxspdef+self.maxspeed
    muldict={1:1.5,2:2,3:2.5,4:3,5:3.5,6:4,0:1,-1:0.66,-2:0.5,-3:0.4,-4:0.33,-5:0.29,-6:0.25}
    self.atk=self.maxatk*muldict[self.atkb]
    self.defense=self.maxdef*muldict[self.defb]
    self.spatk=self.maxspatk*muldict[self.spatkb]
    self.spdef=self.maxspdef*muldict[self.spdefb]
    self.speed=self.maxspeed*muldict[self.speedb] 
    