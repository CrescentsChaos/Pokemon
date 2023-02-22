def zmove(mon):
    zlist=[]
    ilist=[]
    item=None
    zm=None
    ch=random.randint(1,2)
    for i in mon.moves:
        if i in typemoves.dragonmoves:
            if "Kommo" in mon.name and "Clanging Scales" in mon.moves:
                item="Kommonium Z"
                zm="Clangorous Soulblaze"
            else:
                zm="Devastating Drake"
        if i in typemoves.normalmoves:
            if "Snorlax" in mon.name and "Giga Impact" in mon.moves:
                item="Snorlium Z"
                zm="Pulverizing Pancake"
            if ("Eevee" or "eon") in mon.name and "Last Resort" in mon.moves:
                zm="Extreme Evoboost"
                item="Eevium Z"
            else:
                zm="Breakneck Blitz"
                item="Normalium Z"
        if i in typemoves.steelmoves:
            if ("Solgaleo" in mon.name or "Dusk Mane" in mon.name or "Nebby" in mon.name) and "Sunsteel Strike" in mon.moves:
                item="Solganium Z"
                zm="Searing Sunraze Smash"
            else:
                zm="Corkscrew Crash"
                item="Steelium Z"
        if i in typemoves.fairymoves:
            if "Mimikyu" in mon.name and "Play Rough" in mon.moves:
                item="Mimikium Z"
                zm="Let's Snuggle Forever"
            if "Tapu" in mon.name and "Nature's Madness" in mon.moves:
                item="Tapunium Z"
                zm="Guardian of Alola"
            else:
                zm="Twinkle Tackle"
                item="Fairium Z"
        if i in typemoves.rockmoves:
            if "Lycanroc" in mon.name and "Stone Edge" in mon.moves:
                item="Lycanium Z"
                zm="Splintered Stromshards"
            else:
                item="Rockium Z"
                zm="Continental Crash"
        if i in typemoves.groundmoves:
            zm="Techronic Rage"
            item="Groundium Z"
        if i in typemoves.ghostmoves:
            if "Decidueye" in mon.name and "Spirit Shackle" in mon.moves:
                item="Decidium Z"
                zm="Sinister Arrow Raid"
            if ("Lunala" in mon.name or "Dawn Wing" in mon.name or "Nebby" in mon.name) and "Moongeist Beam" in mon.moves:
                item="Lunalium Z"
                zm="Menacing Moonraze Maelstrom"
            if "Marshadow" in mon.name and "Spectral Thief" in mon.moves:
                item="Marshadium Z"
                zm="Soul-Stealing 7-Star Strike"
            else:
                item="Ghostium Z"
                zm="Never-ending Nightmare"
        if i in typemoves.grassmoves:
            zm="Bloom Doom"
            item="Grassium Z"
        if i in typemoves.poisonmoves:
            zm="Acid Downpour"
            item="Poisonium Z"
        if i in typemoves.psychicmoves:
            if "Mew" in mon.name and "Psychic" in mon.moves:
                item="Mewnium Z"
                zm="Genesis Supernova"
            if "Necrozma" in mon.name and "Photon Geyser" in mon.moves:
                item="Ultranecrozium Z"
                zm="Light That Burns The Sky"
            else:
                zm="Shattered Psyche"
                item="Psychium Z"
        if i in typemoves.electricmoves:
            if "Alolan Raichu" in mon.name and "Thunderbolt" in mon.moves:
                item="Aloraichium Z"
                zm="Stoked Sparksurfer"
            if "Pikachu" in mon.name:
                if "Thunderbolt" in mon.moves:
                    item="Pikashunium Z"
                    zm="10,000,000 Volt Thunderbolt"
                elif "Volt Tackle" in mon.moves:
                    item="Pikanium Z"
                    zm="Catastropika"
            else:
                zm="Gigavolt Havoc"
                item="Electrium Z"
        if i in typemoves.fightingmoves:
            zm="All-out Pummeling"
            item="Fightium Z"
        if i in typemoves.icemoves:
            zm="Subzero Slammer"
            item="Icium Z"
        if i in typemoves.statusmove:
            zm="Breakneck Blitz"
            item="Normalium Z"
        if i in typemoves.watermoves:
            if "Primarina" in mon.name and "Sparkling Aria" in mon.moves:
                item="Primarium Z"
                zm="Oceanic Operetta"
            else:
                zm="Hydro Vortex"
                item="Waterium Z"
        if i in typemoves.bugmoves:
            zm="Savage Spin-out"
        if i in typemoves.darkmoves:
            if "Incineroar" in mon.name and "Darkest Lariat" in mon.moves:
                item="Incinum Z"
                zm="Malicious Moonsault"
            else:
                item="Darkium Z"
                zm="Blackhole Eclipse"
        if i in typemoves.flyingmoves:
            zm="Supersonic Airstrike"
            item="Flyium Z"
        if i in typemoves.firemoves:
            zm="Inferno Overdrive"
            item="Firium Z"
        if zm is None:
            zm="Breakneck Blitz"
            item="Normalium Z"
        zlist.append(zm)
        ilist.append(item)
    x=random.randint(0,len(zlist)-1)
    return zlist[x]
    print(ilist)