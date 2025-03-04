async def action(bot, ctx, tr1, tr2, x, y):
    if tr1.ai:
        new=[]
        for i in tr1.pokemons:
            new.append(i.tera)
        if "m-Z" in x.item and tr1.canz==True and x.zuse==True:
            return 5
        elif x.item not in megastones and tr1.canmax and x.tera == "Max" and x.teraType=="???" and "m-Z" not in x.item:
           x.tera=random.choice([x.primaryType,x.secondaryType])
           return 8
        elif x.item not in megastones and tr1.canmax and x.teraType == "???" and "m-Z" not in x.item and "Max" not in new:
            maxch = random.randint(1, 6)
            return 8 if maxch == 1 else 1
        elif x.item in megastones and tr1.canmega:
            return random.choices([1, 6], weights=[1, 10], k=1)[0]
        elif x.tera not in ["???","Max"] and x.tera not in (x.primaryType, x.secondaryType) and tr1.cantera==True and tr1.canmega!=True:
            return 9
        else:
            move=random.choices([1, 2], weights=[10, 1], k=1)[0]
            if y.trap==True:
                return 1
            elif y.ability=="Magnet Pull" and "Steel" in (x.primaryType ,x.secondaryType ,x.teraType ):
                return 1
            else:
                return move
    else:
        inaction = None
        while True:
            des = "#1 💥 Fight\n#2 🔁 Switch\n#3 🚫 Forfeit\n"
            if "m-Z" in x.item and tr1.canz and x.zuse:
                des+="#5 <:zmove:1140788256577949717> Z-Move\n"
            elif tr1.canmega and not x.dmax and (x.item in megastones or "Dragon Ascent" in x.moves) and x.teraType == "???":
                des += "#6 <:megaevolve:1104646688951500850> Mega Evolve\n"
            elif not x.dmax and x.item == "Ultranecrozium-Z" and "Ultra" not in x.name:
                des += "#7 Ultra Burst\n"
            elif tr1.canmax and not x.dmax and x.item not in megastones and x.teraType == "???" and "m-Z" not in x.item:
                des += "#8 <:dynamax:1104646304904257647> Dynamax/Gigantamax\n"
            if tr1.cantera and not x.dmax and x.item not in megastones and x.teraType == "???" and "m-Z" not in x.item and x.tera!="Max":
                des += f"#9 {await teraicon(x.tera)} Terastallize\n"
            em = discord.Embed(title=f"{tr1.name}, what do you wanna do?", description=des)
            em.set_footer(text="Wait a few seconds before entering your action. Re-enter action if it's not working.")
            if tr2.ai==True:
                await ctx.send(embed=em)
                inaction = await bot.wait_for('message', check=lambda msg: msg.author == ctx.author)
            else:
                await tr1.member.send(embed=em)
                inaction = await bot.wait_for('message', check=lambda msg: isinstance(msg.channel, discord.DMChannel) and msg.author == tr1.member)
            inaction = int(inaction.content)    
            await ctx.channel.purge(limit=10,check=lambda msg:msg.author==ctx.author)
            if inaction==2:
                if y.trap==True:
                    return 1
                elif y.ability=="Magnet Pull" and "Steel" in (x.primaryType ,x.secondaryType ,x.teraType ):
                    return 1
                else:
                    return 2
            else:
                return inaction
async def score(ctx, x, y, tr1, tr2, turn, bg):
    team=" ".join(tr1.party)
    tr1.sparty=await spartyup(tr1,x)
    steam=" ".join(tr1.sparty)
    hpbar = "<:HP:1107296292243255356>" + "<:GREY:1107331848360689747>" * 10 + "<:END:1107296362988580907>"
    status_mapping = {
        "Frostbite": "<:FBT:1107340620097404948>",
        "Frozen": "<:FZN:1107340597980827668>",
        "Sleep": "<:SLP:1107340641882603601>",
        "Drowsy": "<:SLP:1107340641882603601>",
        "Paralyzed": "<:YELLOW:1107331825929556111>",
        "Burned": "<:BRN:1107340533518573671>",
        "Poisoned": "<:PSN:1107340504762437723>",
        "Badly Poisoned":"<:PSN:1107340504762437723>"
    }
    if x.dmax==True:
        hpbar = "<:HP:1107296292243255356>" + "<:dynamax:1141227784958652547>"* int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    elif x.status in status_mapping:
        hpbar = "<:HP:1107296292243255356>" + status_mapping[x.status] * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    elif x.status == "Alive":
        if 0.6 < (x.hp / x.maxhp) <= 1:
            hpbar = "<:HP:1107296292243255356>" + "<:GREEN:1107296335780139113>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        elif 0.3 < (x.hp / x.maxhp) <= 0.6:
            hpbar = "<:HP:1107296292243255356>" + "<:YELLOW:1107331825929556111>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        elif 0 < (x.hp / x.maxhp) <= 0.3:
            hpbar = "<:HP:1107296292243255356>" + "<:RED:1107331787480379543>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    rflct=""
    if tr1.reflect==True:
        rflct=f"\n<:reflect:1142009182095163422> Reflect"
    ls=""
    if tr1.lightscreen==True:
        rflct=f"\n<:lightscreen:1142009225741082657> Light Screen"     
    av=""          
    if tr1.auroraveil==True:
        av=f"\n<:auroraveil:1142009279705006102> Aurora Veil"
    tw=""          
    if tr1.tailwind==True:
        av=f"\n<:tailwind:1142043322064572446> Tailwind"               
    em = discord.Embed(
        title=f"{tr1.name}:",
        description=f"{team}\n{steam}",
        color=bg,
    )
    em.add_field(name="Stats:", value=f"**{x.nickname}** Lv. {x.level}\n**HP:** {round(x.hp)}/{x.maxhp} ({round((x.hp/x.maxhp)*100,2)}%)\n**ATK:** {await bufficon(x.atkb)} **DEF:** {await bufficon(x.defb)} **SPA:** {await bufficon(x.spatkb)} **SPD:** {await bufficon(x.spdefb)} **SPE:** {await bufficon(x.speedb)}{rflct}{ls}{av}{tw}")
    em.add_field(name="HP Bar:", value=f"{hpbar}{await statusicon(x.status)}")
    em.set_image(url=x.sprite)
    em.set_footer(text=f"ATK: {x.atkb} DEF: {x.defb} SPA: {x.spatkb} SPD: {x.spdefb} SPE: {x.speedb}")
    if tr1.sub!="None":
        em.set_image(url="https://play.pokemonshowdown.com/sprites/substitutes/gen5/substitute.png")
    if x.gsprite != "None":
        em.set_image(url=x.gsprite)
    await ctx.send(embed=em)
async def bufficon(s,base=0):
    if s==base:
        return "<:base:1140755497323081789>"
    elif s<base:
        return "<:low:1140755454071418910>"
    elif s>base:
        return "<:high:1140755420533772389>"       
async def advscore(ctx, x, y, tr1, tr2, turn, field, bg):
    team=" ".join(tr1.party)
    tr1.sparty=await spartyup(tr1,x)
    steam=" ".join(tr1.sparty)
    hpbar = "<:HP:1107296292243255356>" + "<:GREY:1107331848360689747>" * 10 + "<:END:1107296362988580907>"
    status_mapping = {
        "Frostbite": "<:FBT:1107340620097404948>",
        "Frozen": "<:FZN:1107340597980827668>",
        "Sleep": "<:SLP:1107340641882603601>",
        "Drowsy": "<:SLP:1107340641882603601>",
        "Paralyzed": "<:YELLOW:1107331825929556111>",
        "Burned": "<:BRN:1107340533518573671>",
        "Poisoned": "<:PSN:1107340504762437723>",
        "Badly Poisoned":"<:PSN:1107340504762437723>"
    }
    if x.dmax==True:
        hpbar = "<:HP:1107296292243255356>" + "<:dynamax:1141227784958652547>"* int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    elif x.status in status_mapping:
        hpbar = "<:HP:1107296292243255356>" + status_mapping[x.status] * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    elif x.status == "Alive":
        if 0.6 < (x.hp / x.maxhp) <= 1:
            hpbar = "<:HP:1107296292243255356>" + "<:GREEN:1107296335780139113>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        if 0.3 < (x.hp / x.maxhp) <= 0.6:
            hpbar = "<:HP:1107296292243255356>" + "<:YELLOW:1107331825929556111>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
        if 0 < (x.hp / x.maxhp) <= 0.3:
            hpbar = "<:HP:1107296292243255356>" + "<:RED:1107331787480379543>" * int((x.hp / x.maxhp) * 10) + "<:GREY:1107331848360689747>" * (10 - int((x.hp / x.maxhp) * 10)) + "<:END:1107296362988580907>"
    itm=x.item
    if "Used" in itm:
        itm="None"
    rflct=""
    if tr1.reflect==True:
        rflct=f"\n<:reflect:1142009182095163422> Reflect ({tr1.rfendturn-turn} turns left)"
    ls=""
    if tr1.lightscreen==True:
        rflct=f"\n<:lightscreen:1142009225741082657> Light Screen ({tr1.screenend-turn} turns left)"     
    av=""          
    if tr1.auroraveil==True:
        av=f"\n<:auroraveil:1142009279705006102> Aurora Veil ({tr1.avendturn-turn} turns left)"
    tw=""          
    if tr1.tailwind==True:
        av=f"\n<:tailwind:1142043322064572446> Tailwind ({tr1.twendturn-turn} turns left)"        
    em = discord.Embed(
        title=f"{tr1.name}:",
        description=f"{team}\n{steam}",color=bg)
    em.add_field(name="Stats:",value=f"**{x.nickname}**{await statusicon(x.gender)} Lv. {x.level}\n**HP:** {round(x.hp)}/{x.maxhp} ({round((x.hp/x.maxhp)*100,2)}%)\n**Ability:** {x.ability}\n**Held Item:** {await itemicon(x.item)} {itm}\n**ATK:** {round(x.atk)}{await bufficon(x.atkb)} **DEF:** {round(x.defense)}{await bufficon(x.defb)} **SPA:** {round(x.spatk)}{await bufficon(x.spatkb)} **SPD:** {round(x.spdef)}{await bufficon(x.spdefb)} **SPE:** {round(x.speed)}{await bufficon(x.speedb)}{rflct}{ls}{av}{tw}")
    em.add_field(name="HP Bar:",value=f"{hpbar}{await statusicon(x.status)}")
    em.set_image(url=x.sprite)
    em.set_footer(text=f"ATK: {x.atkb} DEF: {x.defb} SPA: {x.spatkb} SPD: {x.spdefb} SPE: {x.speedb}")
    if tr1.sub!="None":
        em.set_image(url="https://cdn.discordapp.com/attachments/1102579499989745764/1139438981445062719/20230811_120335.png")
    if x.gsprite!="None":
        em.set_image(url=x.gsprite)
    if tr2.ai==False:
        await tr1.member.send(embed=em)
    if tr2.ai==True:
        await ctx.send(embed=em)                 