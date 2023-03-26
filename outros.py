import random
from pokemonbase2 import *
def outro(tr,sr,mon,field):
    mons=[]
    mmons=[]
    trname=tr.name.split(" ")[-1]
    for k in sr.pokemons:
        mmons.append(k.name)
    for i in tr.pokemons:
        mons.append(i.name)
    srname=sr.name.split(" ")[-1]
    print("===================================================================================")
    if "Katy" in sr.name:
        print(random.choice([f" {sr.name}: All of my sweet little Pokémon dropped like flies!\n",f" {sr.name}: Your strength rose during our battle like a nice bread in the oven.\n"]))
    if "Kofu" in sr.name:
        print(random.choice([f" {sr.name}: Vaultin’ Veluza! Yer a lively one, aren’t ya! A little TOO lively, if I do say so myself!\n",f" {sr.name}: Gahaha! A loss as refreshing as the air at the morning market!\n"]))
    if "Brassius" in sr.name:
        print(random.choice([f" {sr.name}: Oh! What artistic tactics you employ!\n",f" {sr.name}: Avant-garde!\n"]))
    if "Iono" in sr.name:
        print(random.choice([f" {sr.name}: Our challenger came out victorious! Well done, {trname}!\n",f" {sr.name}: I hate to say it, but I lost! Thanks for cheerin’ me on anywho, my loyal fans!\n"]))
    if "Tucker" in tr.name:
        print(random.choice([f" {tr.name}: Ahahaha! Aren't you embarrassed? Everyone's watching!\n",f" {tr.name}: My Dome Ace title isn't just for show!\n"]))
    if "Tucker" in sr.name:
        print(random.choice([f" {sr.name}: Grr... What the...\n",f" {sr.name}: Ahahaha! You're inspiring!\n"]))
    if "Pyramid" in sr.name:
        print(random.choice([f" {sr.name}: That's it! You’ve done great! You've worked hard for this!\n",f" {sr.name}: That's it! You've done it! You kept working for this!\n"]))
    if "Pyramid" in tr.name:
        print(random.choice([f" {tr.name}: Hey! Don't give up now! Get up! Don't lose faith in yourself!\n",f" {tr.name}: Hey! What's wrong with you! Let's see some effort! Get up!\n"]))
    if "Spenser" in sr.name:
        print(random.choice([f" {sr.name}: Ah... Now this is something else...\n",f" {sr.name}: Well, that was some display! Even fully unleashed, my brethren could not overpower you. You team spirit is truly admirable! Here! Bring me that thing, will you?\n"]))
    if "Spenser" in tr.name:
        print(random.choice([f" {tr.name}: Your Pokémon are wimpy because you're wimpy as a Trainer!\n",f" {tr.name}: Gwahahaha! My brethren, we have nothing to fear!\n"]))
    if "Greta" in tr.name:
        print(random.choice([f" {tr.name}: Heheh! What did you expect?\n"]))
    if "Greta" in sr.name:
        print(random.choice([f" {sr.name}: No way! Good job!\n",f" {sr.name}: It's going to be fun the next time! I'm looking forward to it!\n",f" {sr.name}: Huh? Are you serious?!\n",f" {sr.name}: Arrrgh! This is so infuriating! If we ever battle again, I won't lose! Don't you forget it! Bye-bye!\n"]))
    if "Aaron" in sr.name:
        print(random.choice([f" {sr.name}: I will now concede defeat. But I think you came to see how great Bug-type Pokémon can be. I hope you also realized why you're up against in the Pokémon League. Battling is a deep and complex affair...\n",f" {sr.name}: Guess I was still one step behind... You've won.\n"]))
    if "Klara" in sr.name:
        print(random.choice([f" {sr.name}: Not good... Not good at all, man... How'd this kid get so strong?!\n"]))
    if "Avery" in sr.name:
        print(random.choice([f" {sr.name}: Ahem! You have potential. Why, you made me use a whole three percent of my strength! Still... How should I put this...\n"]))
    if "Wake" in sr.name:
        print(random.choice([f" {sr.name}: Hunwah! It's gone and ended! How will I say this... I want more! I wanted to battle a lot more!\n"]))
    if "Wake" in tr.name:
        print(random.choice([f" {tr.name}: I won, but I want more! I wanted to battle a lot more!\n"]))
    if "Bugsy" in tr.name:
        print(random.choice([f" {tr.name}: Thanks! Thanks to our battle, I was also able to make progress in my research!\n"]))
    if "Blaine" in tr.name:
        print(random.choice([f" {tr.name}: Whoa hey! I'll power up my Pokémon with the heat from this victorious battle!\n"]))
    if "Koga" in tr.name:
        print(random.choice([f" {tr.name}: You expect to battle the Elite Four with your current skills?\n",f" {sr.name}: Have you learned to fear the techniques of the ninja?\n"]))
    if "Sabrina" in sr.name:
        print(random.choice([f" {sr.name}: Your power... It far exceeds what I foresaw... Maybe it isn't possible to fully predict what the future holds...\n",f" {sr.name}: This loss shocks me!\n But a loss is a loss.\n"]))
    if "Sabrina" in tr.name:
        print(random.choice([f" {tr.name}: This victory... It's exactly as I foresaw three years ago!\n"]))
    if "Erika" in tr.name:
        print(random.choice([f" {tr.name}: I feel inspired by my win. Fighting alongside your beloved Pokémon and winning. This is the joy of being a Pokémon Trainer.\n"]))
    if "Surge" in sr.name:
        print(random.choice([f" {sr.name}: Even my electric tricks lost. You're excellent! Keep goin' like lightning!\n"]))
    if "Surge" in tr.name:
        print(random.choice([f" {tr.name}: Oh yeah! When it comes to Electric-type Pokémon, I'm number one in the world!\n"]))
    if "Misty" in sr.name:
        print(random.choice([f" {sr.name}: Know what? My dream was to go on a journey and battle powerful Trainers... I made my dream come true, and now... my next dream is to defeat you!\n"]))
    if "Misty" in tr.name:
        print(random.choice([f" {tr.name}: Know what? My dream was to go on a journey and battle powerful Trainers... Now, that dream has come true!\n"]))
    if "Brock" in tr.name:
        print(random.choice([f" {tr.name}: I really enjoyed the battle with you. I guess my rock-hard defense works in top-level competition as well!\n"]))
    elif "Brock" in sr.name:
        print(random.choice([f" {sr.name}: I really enjoyed the battle with you. Still, the world is huge! I can't believe you got past my rock-hard defense.\n",f" {sr.name}: I knew you were strong, but this...\n",f" {sr.name}: Awesome... That was a really great battle. I compliment you on your victory!\n"]))
    if "Lucy" in tr.name:
        print(random.choice([f" {tr.name}: Humph...\n"]))
    elif "Lucy" in sr.name:
        print(random.choice([f" {sr.name}: ... ... ... ... ... ... Show me your Frontier Pass...\n",f" {sr.name}: Urk...\n",f" {sr.name}: ...That's all there is... Disappear already...\n"]))
    if "Shauntal" in sr.name:
        print(random.choice([f" {sr.name}: Wow. I'm dumbstruck! I know a lot of words, but right now I can't figure out how to say this. Perhaps, if the feeling I'm having now is put into words, it will be trapped there. So let me say this... My feeling is you're a great Trainer!\n",f" {sr.name}: S-sorry! First, I must apologize to my Pokémon... I'm really sorry you had a bad experience because of me! Oh! It's not your fault! This is how battles always are. Even in light of that, I'm still one of the Elite Four!\n",f" {sr.name}: Challenger, if you defeat the entire Elite Four of the Pokémon League, you can go on to challenge the Champion. And you have earned that right. Return to the plaza in the center and check the statue.\n"]))
    if "Blaine" in sr.name:
        print(random.choice([f" {sr.name}: I have burned down to nothing!\n Not even ashes remain!\n",f" {sr.name}: Awesome. I have burned out... But the fire inside me is only going to get stronger! Let's battle again sometime!\n"]))
    if "ner May" in sr.name:
        print(random.choice([f" {sr.name}: Woah, that was great!\n You lived up to the hype!\n"]))
    if "Jasmine" in sr.name:
        print(random.choice([f" {sr.name}: Well done...\n"]))
    if "Tonoy" in tr.name:
        print(f" {tr.name}: Thanks for playing the game! 😶‍🌫️\n")
    if "Lance" in tr.name:
        print(f" {tr.name}: I never give up, no matter what. You must be the same?\n")
    if "Iris" in tr.name:
        print(random.choice([f" {tr.name}: Do you ever feel that way too, {srname}?\n",f" {tr.name}: {mon.name} is amazing , right? I've trained him well..\n"]))
    if "Brendan" in sr.name:
        print(random.choice([f" {sr.name}: Drat, wasted yet again...\n",f" {sr.name}: Oof, I'm missing something...\n",f" {sr.name}: Not sure what I was expecting...\n",f" {sr.name}: Heh... not bad...\n"]))
    if "Lorelei" in sr.name:
        print(random.choice([f" {sr.name}: ... Things shouldn't be this way!\n",f" {sr.name}: You're better than I thought! Go on ahead! You only got a taste of Pokémon League power!\n",f" {sr.name}: I may have lost to you, but I'll never give up on my Ice-type Pokémon! You should aim to win using Pokémon you like best, too!\n"]))
    if "Bruno" in sr.name:
        print(random.choice([f" {sr.name}: Why? How could I lose?\n",f" {sr.name}: My job is done! Go face your next challenge!\n",f" {sr.name}: Having lost, I have no right to say anything… Go face your next challenge!\n",f" {sr.name}: If you have defeated me, then my job is done. Ugh! I may not like it, but...go! Go face your next challenge!\n", f" {sr.name}: Ugh! No! So my training is still lacking, is that it? ...Go. Do not trouble yourself on my behalf. Continue to move forward!\n",f" {sr.name}: I have regrets!\n"]))
    if "Agatha" in sr.name:
        print(random.choice([f" {sr.name}: Oh, my!\n You are something special, child!\n",f" {sr.name}: You win! I see what the old duff sees in you now. I've nothing else to say. Run along now, child!\n",f" {sr.name}: Not bad!\n",f" {sr.name}: Small wonder that old-timer's taken such an interest in you. Oak and I used to be good rivals, too, you know. Just like you and Gary. Well, what are you waiting for? Head on to the next room!\n"]))
    if "Lance" in sr.name:
        print(random.choice([f" {sr.name}: That's it! I hate to admit it, but you are a Pokémon master!\n",f" {sr.name}: …It's over. But it's an odd feeling. I'm not angry that I lost. In fact, I feel happy. Happy that I witnessed the rise of a great new Champion!\n",f" {sr.name}: …Whew. You have become truly powerful, {trname}. Your Pokémon have responded to your strong and upstanding nature. As a trainer, you will continue to grow strong with your Pokémon.\n",f" {sr.name}: I'm sure you already know this, but dragons are sacred and legendary creatures! That's why I won't lose next time!\n"]))
    if "Erika" in sr.name:
        print(random.choice([f" {sr.name}: Oh! I concede defeat... You are remarkably strong.... That was a delightful match. I felt inspired.\n"]))
    if "Chuck" in sr.name:
        print(random.choice([f" {sr.name}: Wha! I lost?!\n Incredible!\n"]))
    if "Bugsy" in sr.name:
        print(random.choice([f" {sr.name}: Gah...Now I'm not just single, I'm a frickin loser too!\n",f" {sr.name}: Whoa, amazing! You're an expert on Pokémon! My research isn't complete yet.\n"]))
    if "Koga" in sr.name:
        print(random.choice([f" {sr.name}: Humph!\n You have proven your worth!",f" {sr.name}: I subjected you to everything I could muster. But my efforts failed. I must hone my skills. Go on to the next room, and put your abilities to the test!\n"]))
    if "Karen" in sr.name:
        print(random.choice([f" {sr.name}: Well, aren't you good. I like that in a trainer.\n",f" {sr.name}: Strong Pokémon. Weak Pokémon. That is only the selfish perception of people. Truly skilled trainers should try to win with their favorites. I like your style. You understand what's important. Go on--the Champion is waiting.\n"]))
    if "Cynthia" in tr.name:
        print(random.choice([f" {tr.name}: What's necessary to become stronger? I think it's important to never lose your love of Pokémon.\n",f" {tr.name}: Even if you lose, never lose your love of Pokémon.\n"]))
    if "Falkner" in sr.name:
        print(random.choice([f" {sr.name}: Mmm... I have much to learn even before attaining the Mega Stones...\n"]))
    if "Cynthia" in sr.name:
        print(random.choice([f" {sr.name}: Just a few moments ago, you were the most powerful challenger. And just now, you became the most powerful of all the Trainers. You are now our newest Champion!\n",f" {sr.name}: My heart is pounding so hard because I had such a heated battle with you. You are a really great Trainer!!\n",f" {sr.name}: That was beyond my expectation! What an exceptional battle! You certainly bear a resemblance to that Trainer who faced Giratina... Oh, pardon me.\n",f" {sr.name}: No matter how fun the battle is, it will always end sometime...\n"]))
    if "Diantha" in sr.name:
        print(random.choice([f" {sr.name}: Witnessing the noble spirits of you and your Pokémon in battle has really touched my heart...\n"]))
    if "Diantha" in tr.name:
        print(random.choice([f" {tr.name}: Oh, fantastic! What did you think? My team was pretty cool, right? It's a bit embarrassing to show off, but I love to show their best sides!\n"]))
    if "Pryce" in sr.name:
        print(random.choice([f" {sr.name}: Impressive... It appears you've overcame many obstacles as well.\n"]))
    if "Clair" in sr.name:
        print(random.choice([f" {sr.name}: Oh, I see...\n Your skills are rather mysterious.\n"]))
    if "Archer" in sr.name:
        print(random.choice([f" {sr.name}: What a shameful blunder!\n",f" {sr.name}: Again?! This is infuriating!\n",f" {sr.name}: That's how it be...\n"]))
    if "Ariana" in sr.name:
        print(random.choice([f" {sr.name}: Heh... I'm actually impressed.\n"]))
    if "Giovanni" in tr.name:
        print(random.choice([f" {tr.name}: Ha! That was a truly intense fight!\n",f" {tr.name}: I hope we meet again...\n"]))
    if "Blue" in sr.name:
        print(random.choice([f" {sr.name}: Hey! Take it easy!\n",f" {sr.name}: Aww!\n You just lucked out!\n",f" {sr.name}: No! That can't be!\n",f" {sr.name}: What!?\n"]))
    if "Morty" in sr.name:
        print(random.choice([f" {sr.name}: I'm still not good enough yet...\n"]))
    if "Grunt" in sr.name:
        print(random.choice([f" {sr.name}: Dang!\n",f" {sr.name}: Ayaya!\n",f" {sr.name}: Stop! I give up!\n I'll leave quietly!\n",f" {sr.name}: Arrgh!\n You are good!\n",f" {sr.name}: Crushed by a kid, as usual.\n",f" {sr.name}: Must be nice being strong.\n",f" {sr.name}: Please! No more!\n",f" {sr.name}: I give up!\n"]))
    if "Giovanni" in sr.name:
        print(random.choice([f" {sr.name}: What? Me, lose?!\n",f" {sr.name}: Haarg! I lose?! There is nothing I wish to say to you!\n",f" {sr.name}: How this is possible...? The past three years have been a waste...? How can a kid like you manage to destroy my dream once again? The precious dream of Team Rocket has become little more than an illusion...\n",f" {sr.name}: ...I see you have raised your Pokémon with utmost care. It would be foolish to fight such a kid with all my might. Ha, very well.\n",f" {sr.name}: What!\n This can't be!\n",f" {sr.name}: W-what?! Impossible...\n"]))
    if "Noland" in sr.name:
        print(f" {sr.name}: Heh... You're a pretty bright spark... Next time, I'll come after you hard. No holds barred, understand? You keep up your studies!\n")
    if "Noland" in tr.name:
        print(f" {tr.name}: Way to work! That was a good lesson, eh?\n")
    if "Red" in tr.name:
        print(f" {tr.name}: .........\n")
    if "Red" in sr.name:
        print(f" {sr.name}: .........\n")
    elif "Eternatus" in mon.name:
        print(f" {sr.name}: {mon.name}! *sigh* You had to use that thing fr?😢\n")
    if tr.ai==True and sr.ai==False:
        print(random.choice([f" {tr.name}:\n Imagine losing to an AI. Bruh...Wtf are you doing with your life?🤣\n",f" {tr.name}:\n Humans this humans that...You are more worthless than something that does not exist!😒\n"]))
    else:
        pass
    print("===================================================================================")
    dedlist(tr,sr)
    statistics(tr,sr)
        #if mon.use!="None":
#            print(f" {tr.name}:\n Did you feel my pain in that {mon.use} from {mon.name}!\n")
#        else:
#            print(random.choice([f" {tr.name}:\n Me and {mon.name} trained a lot! Thanks for that!\n",f" {tr.name}:\n You are a fool if you thought you could beat me and {mon.name}...fwhahahhahahaha!\n"]))
    print("===================================================================================")
def dedlist(tr,sr):
    z=tr.faintedmon
    x=[]
    y=[]
    for i in z:
        if i.owner==tr:
            x.append(i)
        if i.owner==sr:
            y.append(i)
    tr.faintedmon=x        
    sr.faintedmon=y
    for i in tr.faintedmon:
        if i not in tr.pokemons:
            tr.pokemons.append(i)
            i.hp=i.maxhp
            i.calcst()
    for i in sr.faintedmon:
        if i not in sr.pokemons:
            sr.pokemons.append(i)         
            i.hp=i.maxhp
            i.calcst()   
def statistics(tr,sr):
    trname=tr.name.split(" ")[-1]
    srname=sr.name.split(" ")[-1]
    trdmgdealt=0
    srdmgdealt=0
    trcarry=Pikachu()
    srcarry=Pikachu()
    trdmgrec=0
    srdmgrec=0
    trtank=Pikachu()
    srtank=Pikachu()
    for i in tr.pokemons:
         if trdmgdealt<i.dmgdealt:
             trdmgdealt=i.dmgdealt
             trcarry=i
    print(f" 🏅 Carry from the winning team: {trname}'s {trcarry.name} ({trdmgdealt})") 
    for i in sr.pokemons:
         if srdmgdealt<i.dmgdealt:
             srdmgdealt=i.dmgdealt
             srcarry=i
    print(f" 🥈 Carry from the losing team: {srname}'s {srcarry.name} ({srdmgdealt})") 
    for i in tr.pokemons:
         if trdmgrec<i.dmgrec:
             trdmgrec=i.dmgrec
             trtank=i
    print(f" 🏅 Tank from the winning team: {trname}'s {trtank.name} ({trdmgrec})") 
                
    for i in sr.pokemons:
         if srdmgrec<i.dmgrec:
             srdmgrec=i.dmgrec
             srtank=i
    print(f" 🥈 Tank from the losing team: {srname}'s {srtank.name} ({srdmgrec})")
    if srdmgdealt>trdmgdealt and srdmgdealt>700:
        print(f" 💯 Best Carry: {srname}'s {srcarry.name} ({srdmgdealt})") 
    if trdmgdealt>srdmgdealt and trdmgdealt>700:
        print(f" 💯 Best Carry: {trname}'s {trcarry.name} ({trdmgdealt})") 
    if srdmgrec>trdmgrec and (srdmgrec>700 or srdmgrec>srtank.maxhp*2):
        print(f" 💯 Best Tank: {srname}'s {srtank.name} ({srdmgrec})") 
    if trdmgrec>srdmgrec and (trdmgrec>700 or trdmgrec>trtank.maxhp*2):
        print(f" 💯 Best Tank: {trname}'s {trtank.name} ({trdmgrec})") 
    if trtank==trcarry and (trdmgdealt>700 and trdmgrec>700):
        print(f" 🏆 Most Valuable Pokémon: {trname}'s {trcarry.name}!")
    if srtank==srcarry and (srdmgdealt>700 and srdmgrec>700):
        print(f" 🏆 Most Valuable Pokémon: {srname}'s {srcarry.name}!")
    
     