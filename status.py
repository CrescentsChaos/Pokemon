import random
from movelist import *
from plugins import *
        
#Berry            
async def berry(em,y,x,xhp,yhp,turn):
    if y.hp<=(y.maxhp/4)  and yhp>(y.maxhp/4):
      if y.item=="Lansat Berry" and x.ability not in ["Unnerve","As One"]:
          if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
              y.hp+=(y.maxhp/3)
          em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s critical hit ratio!")
          n=4
          if y.ability=="Ripen":
              n=8
          y.critrate*=n
          y.item+="[Used]"
      if y.item=="Ganlon Berry" and x.ability not in ["Unnerve","As One"]:
          if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
              y.hp+=(y.maxhp/3)
          em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Special Defense!")
          n=1
          if y.ability=="Ripen":
              n=2
          await defchange(em,y,x,n)
          y.item+="[Used]"
      if y.item=="Apicot Berry" and x.ability not in ["Unnerve","As One"]:
          if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
              y.hp+=(y.maxhp/3)
          em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Special Defense!")
          n=1
          if y.ability=="Ripen":
              n=2
          await spdefchange(em,y,x,n)
          y.item+="[Used]"
    if y.item=="Maranga Berry" and y.atkcat=="Special" and x.hp!=xhp:
          if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
              y.hp+=(y.maxhp/3)
          em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Special Defense!")
          n=1
          if y.ability=="Ripen":
              n=2
          await spdefchange(em,y,x,n)
          y.item+="[Used]"
    if x.use not in typemoves.statusmove:
        if y.item=="Jaboca Berry" and y.atkcat=="Physical" and x.hp!=xhp:
            if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                y.hp+=(y.maxhp/3)
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} damaged {x.name}!")
            x.hp-=round(x.maxhp/8)
            y.item+="[Used]"
        if y.item=="Rowap Berry" and y.atkcat=="Special" and x.hp!=xhp:
            if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                y.hp+=(y.maxhp/3)
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} damaged {x.name}!")
            x.hp-=(y.maxhp/8)
            y.item+="[Used]"
        if y.item=="Kee Berry" and x.ability not in ["Unnerve","As One"]:
            if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                y.hp+=(y.maxhp/3)
            em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Defense!")
            n=1
            if y.ability=="Ripen":
                n=2
            await defchange(em,y,x,n)
            y.item+="[Used]"
    if (y.hp<=(y.maxhp/4)  and yhp>(y.maxhp/4)) or (y.ability=="Gluttony" and y.hp<=(y.maxhp/2) and yhp>(y.maxhp/2)):
        if y.item=="Liechi Berry" and x.ability not in ["Unnerve","As One"]:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Attack!")
              n=1
              if y.ability=="Ripen":
                  n=2
              await atkchange(em,y,x,n)
              y.item+="[Used]"
        if y.item=="Petaya Berry" and x.ability not in ["Unnerve","As One"]:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Special Attack!")
              n=1
              if y.ability=="Ripen":
                  n=2
              await spatkchange(em,y,x,n)
              y.item+="[Used]"
        if y.item=="Salac Berry" and x.ability not in ["Unnerve","As One"]:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Speed!")
              n=1
              if y.ability=="Ripen":
                  n=2
              await speedchange(em,y,x,n)
              y.item+="[Used]"
        if y.item=="Custap Berry" and y.speed<x.speed:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              y.priority=True
              y.item+="[Used]"
        if y.item=="Starf Berry" and x.ability not in ["Unnerve","As One"]:
              if y.ability=="Cheek Pouch" and y.hp<y.maxhp:
                  y.hp+=(y.maxhp/3)
              ss=random.randint(1,5)
              n=1
              if y.ability=="Ripen":
                  n=2
              if ss==1:
                  em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Attack!")
                  await atkchange(em,y,x,n)
              if ss==2:
                  em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Special Attack!")
                  await spatkchange(em,y,x,n)
              if ss==3:
                  em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Defense!")
                  await defchange(em,y,x,n)
              if ss==4:
                  em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Special Defense!")
                  await spdefchange(em,y,x,n)
              if ss==5:
                  em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.item} raised {y.icon} {y.name}'s Speed!")
                  await speedchange(em,y,x,n)
              y.item+="[Used]"
        if y.item in ["Aguav Berry","Figy Berry","Ipapa Berry","Mago Berry","Wiki Berry"]:
                y.hp+=round(y.maxhp/3)
                em.add_field(name=f"{y.icon} {y.name}'s {await itemicon(y.item)} {y.item}!",value=f"{y.name} consumed it's {y.item} and restored some HP!")
                if y.item=="Wiki Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Adamant","Jolly","Careful","Impish"]:
                        pass
                        #confuse(y,y,turn,100)
                if y.item=="Ipapa Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Lonely","Mild","Gentle","Hasty"]:
                        pass
                        #confuse(y,y,turn,100)
                if y.item=="Aguav Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Naughty","Naive","Rash","Lax"]:
                        pass
                        #confuse(y,y,turn,100)
                if y.item=="Mago Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Brave","Quiet","Sassy","Relaxed"]:
                        pass
                        #confuse(y,y,turn,100)
                if y.item=="Figy Berry" and x.ability not in ["Unnerve","As One"]:
                    if y.nature in ["Modest","Timid","Calm","Bold"]:
                        pass
                        #confuse(y,y,turn,100)
                y.item+="[Used]"                                                      