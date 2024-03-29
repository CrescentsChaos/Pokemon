#pylint:disable=C0304
#pylint:disable=R0915
#pylint:disable=R0912
#pylint:disable=C0116
#pylint:disable=C0103
#pylint:disable=C0301
#import sys
#import time
#def print(something):
#    for character in something:
#        sys.stdout.write(character)
#        sys.stdout.flush()
#        time.sleep(0.01)
import random
from colorama import init
from termcolor import colored    
def intro (tr,sr,field):
    mons=[]
    mmons=[]
    for k in sr.pokemons:
        mmons.append(k.name)
    for i in tr.pokemons:
        mons.append(i.name)
    srname=sr.name.split(" ")[-1]
    if "Beauty" in tr.name:
        print(random.choice([colored(f" {tr.name}: This might hurt a little bit, but we'll be done quick.\n Hold still!\n","white")]))
    if "Juggler" in tr.name:
        print(random.choice([f" {tr.name}: Howdy!\n Are you a member of my fan club?\n"]))
    if "Rich Girl" in tr.name:
        print(random.choice([colored(f" {tr.name}: Hmm.. So, you're good, huh?\n","white")]))
    if "Painter" in tr.name:
        print(random.choice([colored(f" {tr.name}: Hmm.. hold still right there!\n I must paint that powerful pose!\n","white")]))
    if "Blue" in tr.name and "Bruno" in srname:
        print(random.choice([colored(f" {tr.name}: I hope you can offer me more of a challenge!\n","white")]))
    if "Blue" in tr.name and "Lorelei" in srname:
        print(random.choice([colored(f" {tr.name}: I will smash your Ice into a million pieces!\n","white")]))
    if "Scientist" in tr.name:
        print(random.choice([colored(f" {tr.name}: Charge! my Pokémon!\n Demonstrate the fruits of our experimentation!\n","white")]))
    if "Waiter" in tr.name:
        print(random.choice([colored(f" {tr.name}: May I take your order, please?\n","white")]))
    if "Waitress" in tr.name:
        print(random.choice([colored(f" {tr.name}: What I really hoped to become was a cook.\n","white")]))
    if "Dragon Tamer" in tr.name:
        print(random.choice([colored(f" {tr.name}: See it! Feel it! The ultimate power...\n Probably!\n","white")]))
    if "Black Belt" in tr.name:
        print(random.choice([colored(f" {tr.name}: A battle is deadly earnest!\n Not a moment of inattention!\n","white"),colored(f" {tr.name}: My spirit burns, my fists are steel, and my sweat cascades!\n","white")]))
    if "Rancher" in tr.name:
        print(random.choice([colored(f" {tr.name}: Smell that?\n That's the smell of hay clinging to my body.\n","white")]))
    if "Picnicker" in tr.name:
        print(random.choice([colored(f" {tr.name}: I'll teach you what's fun about battling!\n","white")]))
    if "Expert" in tr.name:
        print(random.choice([colored(f" {tr.name}: Oh, you are still a child.\n Who said you could come here?\n","white")]))
    if "Fisherman" in tr.name:
        print(random.choice([colored(f" {tr.name}: My fishing-rod handling technique is the best.\n Check it out!\n","white"),colored(f" {tr.name}: I came here from far away to fish for new Pokémon.\n","white")]))
    if "Ranger" in tr.name:
        print(random.choice([colored(f" {tr.name}: I didn't sleep while trying to come up with this new strategy!\n","white")]))
    if "Burglar" in tr.name:
        print(random.choice([colored(f" {tr.name}: I was a thief, but I went straight as a trainer. \n","white")]))
    if "Ruin Maniac" in tr.name:
        print(random.choice([colored(f" {tr.name}: I travel around in search of lost treasures.\n","white")]))
    if "Jogger" in tr.name:
        print(random.choice([colored(f" {tr.name}: I run a marathon every morning!\n It's great!\n","white"),colored(f" {tr.name}: I'll run on the spot while battling for the good of my health.\n","white")]))
    if "Tuber" in tr.name:
        print(random.choice([colored(f" {tr.name}: I ... I can swim, Really!\n I don't need my inner tube!\n","white"),colored(f" {tr.name}: I like rivers more than the sea.\n Which do you prefer?\n","white")]))
    if "Geeta" in tr.name:
        print(colored(f" {tr.name}: Welcome, {srname}.\n It gives me great joy that you’ve managed to make it all the way to the pinnacle of the Pokémon League.\n The final test is a battle against me, the Top Champion.\n","white"))
    if "Katy" in tr.name:
        print(colored(f" {tr.name}: Forgive me. Ahem. My name is Katy, and I am the Gym Leader here in Cortondo.\n","white"))
    if "Kofu" in tr.name:
        print(colored(f" {tr.name}: I am Kofu the Torrent! Ever changin'—just like water! Now come see what I'm made of!\n","white"))
    if "Brassius" in tr.name:
        print(colored(f" {tr.name}: I am Brassius—an artist specializing in Grass-type Pokémon. I am also the Gym Leader here at the Artazon Gym.\n","white"))
    if "Iono" in tr.name:
        print(colored(f" {tr.name}: Ladies and gentlemens! Are you readyyyyyy?!\n Your eyeballs are MINE—caught in my Electroweb! Whosawhatsit?\n Iono! ’Ello, ’ello, hola! Ciao and bonjour!\n It’s time for the Iono Zone, everybody!\n Today’s challenger is flyin’ high like a Wattrel! Iiit’s {srname}!\n Yayyy...How’re ya feelin’ about this battle, {srname}?\n","white"))
    if "Tucker" in tr.name:
        print(colored(f" {tr.name}: Ahahah! Do you hear it? This crowd! They're all itching to see our match! Ahahah! I bet you're twitching all over from the tension of getting to battle me! But don't worry about a thing! I'm the no. 1 star of the Battle Dome! I, Tucker the Dome Ace, will bathe you in a brilliant glow! Your strategy! Let's see it! The final match! {srname} versus the Dome Ace, Tucker! Let the battle begin!\n","white"))
    if "Spenser" in tr.name:
        print(colored(f" {tr.name}: My physical being is with Pokémon always! My heart beats as one with Pokémon always! Young one of a Trainer! Do you believe in your Pokémon? Can you believe them through and through? If your bonds of trust are frail, you will never beat my brethren! The bond you share with your Pokémon! Prove it to me here!\n","white"))
    if "Greta" in tr.name:
        print(colored(f" {tr.name}: Hey! Howdy! ...Wait, are you the challenger?\n","white"))
    if "Wake" in tr.name:
        print(colored(f" {tr.name}: Welcome! I don't get challenged very often! The glory you are now beholding is the Pastoria Gym Leader! That's right, I'm Crasher Wake! My Pokémon were toughened up by stormy white waters! They'll take everything you can throw at them and then pull you under! Victory will be ours! Come on, let's get it done!\n","white"))
    if "Bugsy" in tr.name:
        print(colored(f" {tr.name}: I never lose when it comes to Bug-type Pokémon. Let me demonstrate what I've learned from my studies.\n","white"))
    if "Blaine" in tr.name:
        print(colored(f" {tr.name}: Hah! I'm Blaine! I am the Leader of Cinnabar Gym! My fiery Pokémon will incinerate all challengers! Hah! You better have Burn Heal!\n","white"))
    if "Koga" in tr.name:
        print(colored(f" {tr.name}: Fwahahahaha! I am Koga of the Elite Four. I live in shadows--a ninja! My intricate style will confound and destroy you! Confusion, sleep, poison... Prepare to be the victim of my sinister techniques! Fwahahahaha! Pokémon are not merely about brute force--you shall see soon enough!\n","white"))
    if "Sabrina" in tr.name:
        print(colored(f" {tr.name}: Three years ago I had a vision of battling you. Since you wish it, I will show you my psychic powers!\n","white"))
    if "Brock" in tr.name:
        if sr.region=="Kanto":
            print(random.choice([colored(f" {tr.name}: I'm Brock! I'm Pewter's Gym Leader! I believe in rock hard defense and determination! That's why my Pokémon are all the Rock-type! Do you still want to challenge me? Fine then! Show me your best!\n","white")]))
        else:
            print(random.choice([colored(f" {tr.name}: Wow, it's not often that we get a challenger from {sr.region}. I'm Brock, the Pewter Gym Leader. I'm an expert on Rock-type Pokémon. My Pokémon are impervious to most physical attacks. You'll have a hard time inflicting any damage. Come on!\n","white"),colored(f" {tr.name}: I'm Brock! I'm an expert of Rock-type Pokémon. My defense is rock hard!\n","white"),colored(f" {tr.name}: I'm Brock! I'm an expert of Rock-type Pokémon. My Pokémon are impervious to most physical attacks. You'll have a hard time inflicting any damage.\n","white")]))
    if "Lucy" in tr.name:
        print(random.choice([colored(f" {tr.name}: I am Lucy... I am the law here... For I am the Pike Queen... You already know it, but to advance, you must defeat me... ...I'm not one for idle chatter. Hurry. Come on... Your luck... I hope you didn't use it all up here...\n","white"),colored(f" {tr.name}: You again... ... ... ... ... ... ... ...I've trampled flowers and braved storms to get to where I am... I don't feel any compulsion to keep losing to the same opponent... ... ... ... ... ... ... Fine... I'll do it... Now! Come on!\n","white")]))
    if "Iris" in tr.name:
        print(random.choice([colored(f" {tr.name}: Know what? I really look forward to having serious battles with strong Trainers! I mean, come on! The Trainers who make it here are Trainers who desire victory with every fiber of their being! And they are battling alongside Pokémon that have been through countless difficult battles! If I battle with people like that, not only will I get stronger, my Pokémon will, too! And we'll get to know each other even better! OK! Brace yourself! I'm Iris, the Pokémon League Champion, and I'm going to defeat you!\n","white"),colored(f" {tr.name}: The Trainers who come here are Trainers who desire victory with every fiber of their being! And they are battling alongside Pokémon that have been through countless difficult battles! If I battle with people like that, not only will I get stronger, my Pokémon will, too! And we'll get to know each other even better! OK! Brace yourself! I'm Iris, the Pokémon League Champion, and I'm going to defeat you!\n","white")]))
    if "Noland" in tr.name:
        print(random.choice([colored(f" {tr.name}: Hey, my name's Noland! I'm basically in charge of this place, which is why I'm the Factory Head! I had a look at your Battle Swap data. You seem to have the right idea, but you're still square in your head! Listen up, okay? Knowledge isn't only about reading books or doing desk work. Just doing that sort of thing... It may as well be useless! You have to experience things with your heart and your body, understand? I'll take you on under the same conditions as you. I'll be using rental Pokémon too! Shake out every last bit of your knowledge and bring it on!\n","white"),colored(f" {tr.name}: The name's Noland. I'm the Frontier Brain in charge of the Battle Factory over in Hoenn. Pleasure to meet you!\n","white")]))
    if "Pyramid" in tr.name:
        print(random.choice([colored(f" {tr.name}: Young adventurer... Wouldn't you agree that explorations are the grandest of adventures? Your own wits! Your own strength! Your own Pokémon! And, above all, only your courage to lead you through unknown worlds...\n","white"),
colored(f" {tr.name}: Aah, yes, indeed this life is grand! Grand, it is! Eh? I'm Brandon. I'm the Pyramid King, which means I'm in charge here. Most people call me the chief! You coming here means you have that much confidence in yourself, am I right? Hahahah! This should be exciting! Now, then! Bring your courage to our battle!\n","white"),colored(f" {tr.name}: ...You've finally returned, young explorer... Your love for adventure seems to come deep from within your heart... Yes... You are exactly as I was in my own youth... ... ... ...Ah... The passionate! The dangerous! The desperate! Those days of death-defying, life-affirming adventures are back..."
"Now, then! I sense my courage is off the meter! Everything you have! I'm braced for it all!\n","white")]))
    if " Turo" in tr.name:
        print(colored(f" {tr.name}: Many other Pokémon also came to this place from across the boundaries of time. But I was never able to bring over more than two specimens of Miraidon.\n","white"))
    if " Sada" in tr.name:
        print(colored(f" {tr.name}: ∧t |ɑst ⅿy drəaⅿ ıs withın reaɔh...ɑnd you’re no7 gətting ın the way!\n","white"))
    if " Rika" in tr.name:
        print(colored(f" {tr.name}: Next, I'd like to ask you a few questions, if you wouldn't mind, {srname}.\n","white"))
    if "Clemont" in tr.name:
        print(colored(f" {tr.name}: Oh! I'm glad that we got to meet yet again like this!\n","white"))
    if "Marlon" in tr.name:
        print(colored(f" {tr.name}: Oh ho, so I'm facing you! That's off the wall. How 'bout you and I make some waves and sweep the audience away? Let's leave 'em with even bigger smiles!\n","white"))
    if "Gladion" in tr.name:
        print(colored(f" {tr.name}: What does a Pokémon Trainer really need to be successful? I guess everyone might have their own answer. But for me... I want the strongest rival for myself.\n","white"))
    if "Burgh" in tr.name:
        print(colored(f" {tr.name}: If the battle brings out the beauty in Bug-type Pokémon, it will be a scene that makes my heart flutter, win or lose. My bug Pokémon are abuzz with anticipation. Let's get straight to it!\n","white"))
    if tr.name=="Brock(Hard Mode)":
        field.weather="Sandstorm"
    if tr.name=="Misty(Hard Mode)":
        field.weather="Rainy"
    if tr.name=="Blaine(Hardcore Mode)":
        print(colored(f" {tr.name}: Are you ready? Cause I'm not here to play a fair battle haahhahaha!\n","white"))
        field.weather="Desolate Land"
    if tr.name=="Erika(Hardcore Mode)":
        print(colored(f" {tr.name}: Nature is beautiful don't you think? Yeah...even if you have different opinion I'll force you haha!\n","white"))
        field.terrain="Grassy"
    if "Roark" in tr.name:
        if "Canalave City" in field.location:
            print(colored(f" {tr.name}: You came to challenge dad? But guess what! you gotta challenge me first!\n","white"))
    if "Buck" in tr.name:
        if "Heatran" in mmons:
            print(colored(f" {tr.name}: Ohhhh! Is that a Heatran? So you did catch Heatran! That's cool! But You aren't even close to my collection!\n","white"))
        else:
            print(colored(f" {tr.name}: One, there are no shortcuts in the way of Pokémon! Two... Nevermind that, let's do this!\n","white"))
    if "Falkner" in tr.name:
        if "Lugia" in mons:
            print(colored(f" {tr.name}: Oh! Lugia? Haha... Don't worry he's just a friend of mine..\n","white"))
        else:
            print(colored(f" {tr.name}: I'm Falkner, the Violet Pokémon Gym leader! People say you can clip flying-type Pokémon's wings with a jolt of electricity... I won't allow such insults to bird Pokémon! I'll show you the real power of the magnificent bird Pokémon!\n","white"))
    if "Trevor" in tr.name:
        print(colored(f" {tr.name}: I think I will follow the crowd and be your opponent as well. But this time it won't be about the Pokédex. It will be a Pokémon battle!\n","white"))
    if "Ingo" in tr.name:
        print(colored(f" {tr.name}: What a selfish outlook.These frenzies cause the Pokémon themselves such suffering! But what is it you want to do, {srname}?\n","white"))
    if "Anabel" in tr.name:
        print(colored(f" {tr.name}: Greetings... My name is Anabel. I am the Salon Maiden, and I am in charge of running the Battle Tower... I have heard several rumors about you... In all honesty, what I have heard does not seem attractive in any way... The reason I've come to see you... Well, there is but one reason... Let me see your talent in its entirety...\n","white"))
    if "Ghetsis" in tr.name:
        print(colored(f" {tr.name}: My name is Ghetsis. I am representing Team Plasma. I, too, was summoned from another world, much like the other leaders you've defeated!\n","white"))
    if "Dahlia" in tr.name:
        print(colored(f" {tr.name}: Whenever I battle someone tough, I smile. I cannot help it! How about you? What do you do? Do you laugh? Cry? Get angry?\n","white"))
    if "Ethan" in tr.name:
        print(colored(f" {tr.name}: I knew it was you, {srname}! How did you get past me? Here is your punishment for surprising me, {srname}!\n","white"))
    if "Blue" in tr.name:
        if field.location=="Indigo Plateau":
            print(colored(f" {tr.name}: Hey, {srname}! I was looking forward to seeing you, {srname}! Hahah, that is so great! My rival should be strong to keep me sharp. While working on my Pokédex, I looked all over for Pokémon. Not only that, I assembled teams that would beat any Pokémon type. And now… I am the Pokémon League Champion! {srname}! Do you know what that means? I'll tell you. I am the most powerful Trainer in the world!\n","white"))
    if "Surge" in tr.name:
        print(colored(f" {tr.name}: The name's Lt. Surge! When it comes to Electric-type Pokémon, I'm number one! You've got guts to challenge me! I'm gonna zap you!\n","white"))
    if "Misty" in tr.name:
        print(random.choice([colored(f" {tr.name}: I'm Misty! I'm a user of Water-type Pokémon, and my Water-type Pokémon are tough!\n","white"),colored(f" {tr.name}: Hi, you're a new face! What's your policy on Pokémon? What is your approach? My policy is an all-out offensive with Water-type Pokémon! Misty, the world-famous beauty, is your host! Are you ready, sweetie?\n","white")]))
    if "Silver" in tr.name:
        print(colored(f" {tr.name}: Hold it. You're going to take the Pokémon League challenge now? That's not going to happen. My super-well trained Pokémon are going to pound you. {srname}! I challenge you!\n","white"))
    if "Leon" in tr.name:
        print(colored(f" {tr.name}: A real hero, who battled alongside the Legendary Pokémon, Zacian and Zamazenta... I couldn't have dreamed of a better challenger to help increase my winning streak!\n","white"))
    if "Trainer N" in tr.name:
        print(colored(f" {tr.name}: Well, {srname}, is it? Let me hear your Pokémon's voice again!\n","white"))
    if "Tabitha" in tr.name:
        print(colored(f" {tr.name}: Hehehe... Got here already, did you? We underestimated you! But this is it! I'm a cut above the Grunts you've seen so far. I'm not stalling for time. I'm going to pulverize you!\n","white"))
    if "Brendan" in tr.name:
        print(colored(f" {tr.name}: Hey, {srname}. So this is where you were. How's it going? Have you been raising your Pokémon? I'll check for you.Oh! By checking I meant battling you get it?\n","white"))
    if "Ariana" in tr.name:
        print(colored(f" {tr.name}: I don't know or care if what I'm doing is right or wrong... I just put my faith in Giovanni and do as I am told.\n","white"))
    if "Archer" in tr.name:
        print(colored(f" {tr.name}: That's quite enough of you playing the hero, kid. Spreading lies about how Team Rocket has disbanded… It's such an obvious attempt to cause confusion in our ranks. Fortunately, we're not so ignorant to fall for the lies of a child! And now, I'll show you how scary an angry adult can be!\n","white"))
    if "Cyrus" in tr.name:
        x=random.choice([colored(f" {tr.name}: ...The shadowy Pokémon isn't here. It abandoned me here, then disappeared somewhere farther down... Was it content to merely interfere with my plan...? Incidentally, do you understand the concept of genes?\n","white"),colored(f" {tr.name}: ...My name is Cyrus. I would like to ask you one question. Is this world the new world?\n","white"),colored(f" {tr.name}: I can sense in you the strong desire to protect... something. You have a powerful spirit. ...That must mean this isn't the world I desired. I used the power of the Pokémon that control time and space to create a perfect world, where the human spirit does not exist. That was when a great shadow appeared and engulfed me... And brought me to this world.\n","white"),colored(f" {tr.name}: So we meet again, {srname}. It seems our fates have become intertwined. But here and now, I will finally break that bond!")])
        print(x)
    if "Archie" in tr.name:
        x=random.choice([colored(f" {tr.name}: I find myself thinkin'… maybe I should make this world more like my ideal while I'm here anyway! I've got the Sea Basin Pokémon, Kyogre… With its power to control the rains, I'll call down a great deluge to wash away this world's land! All life is born from the sea! If we help the ocean to expand, we're creating the cradle for future life to grow and thrive!\n","white"),colored(f" {tr.name}: The ancient power of Primal Kyogre!\n","white"),colored(f" {tr.name}: The super-ancient Pokémon…KYOGRE!!!\n","white")])
        print(x)
    if "Maxie" in tr.name:
        x=random.choice([(colored(f" {tr.name}: Groudon... Nothing could awaken you from your sleep bathed in magma... This Red Orb is what you sought. Wasn't it? I have brought you the Red Orb. Let its shine awaken you! And show me... Show me the full extent of your power!\n","white")),colored(f" {tr.name}: So the super-ancient Pokémon weren't only Groudon and Kyogre... After all our frantic scheming and fruitless efforts, that one Pokémon's simple action puts everything right again as if nothing had happened... Fu... Fuhahaha.../n")])
        print(x)
    if "Giovanni" in tr.name:
        x=random.choice([colored(f" {tr.name}: ... I don't know why you have come here. Anyway, I have to warn you that this is not a place for kids like you.\n","white"),colored(f" {tr.name}: You have a certain look... It reminds me of the kid who stood in front of me three years ago... You have the same eyes... I'm on my way to Goldenrod City to answer the call and join my team. Are you going to get in my way?\n","white"),colored(f" {tr.name}: For your insolence, you will feel a world of pain!\n","white")])
        if "Viridian City" in field.location:
            print(colored(f" {tr.name}: Fwahahaha! This is my hideout! I planned to resurrect Team Rocket here! But, you have caught me again! So be it! This time, I'm not holding back! Once more, you shall face Giovanni, the greatest trainer!\n","white"))
        else:
            print(x)
    if "Kahili" in tr.name:
        print(colored(f" {tr.name}: Alola! And alola once again! My name is Kahili. A few years ago, I was a champion of the island challenge, too. Just like you. I've been traveling the world to improve my skill as both a Trainer and as a golfer. When I heard that they'd made a Pokémon League in my own home region, I came flying back to serve Alola. Have a look at my fantastic Flying-type team!\n","white"))
    if "Acerola" in tr.name:
        print(colored(f" {tr.name}: Nanu said maybe he can't refuse a tapu choosing him to serve as kahuna... But he'd be darned if he had to serve as one of the Elite Four just because some guy asked him! So I guess I'll just have to battle hard enough to make up for his not being here!\n","white"))
    if "Olivia" in tr.name:
        print(colored(f" {tr.name}: I won't be holding back! My Rock-type Pokémon will grind you to dust! Your puny little Pokémon are going to go down in one hit! Hah!\n","white"))
    if "Molayne" in tr.name:
        print(colored(f" {tr.name}: Kukui asked me to, so I decided to be in the Elite Four. I'm looking forward to battling against you and Sophocles in the Pokémon League.\n","white"))
    if "Hala" in tr.name:
        print(colored(f" {tr.name}: Your old kahuna is now also a member of the Elite Four. Well, this time I'm holding nothing back! Time for you to see what I can really do!\n","white"))
    if "Caitlin" in tr.name:
        print(colored(f" {tr.name}: Who are you? How impudent you are to disturb my sleep. Hmf... You appear to possess a combination of strength and kindness. Very well. Make your best effort not to bore me with a yawn-inducing battle. Clear?\n","white"))
    if "Marshal" in tr.name:
        print(colored(f" {tr.name}: Greetings, challenger. My name is Marshal. In order to master the art of fighting, I'm training under my mentor, Alder. My mentor sees your potential as a Trainer and is taking an interest in you. It is my intention to test you--to take you to the limits of your strength. Kiai!\n","white"))
    if "Grimsley" in tr.name:
        print(colored(f" {tr.name}: Man oh man... What is going on today? Challengers coming one right after another. Well, no matter. I am Grimsley of the Elite Four, and I will fulfill my duty to be your opponent.\n","white"))
    if "Shauntal" in tr.name:
        x=random.choice([colored(f" {tr.name}: Eyes brimming with dark flame, this man rejected everything other than himself in order to bring about one singular justice...' That's part of a novel I'm writing. I was inspired by the challenger who was just here, and somehow I got a little sad... Excuse me. You're a challenger, right? I'm the Elite Four's Ghost-type Pokémon user, Shauntal, and I shall be your opponent.\n","white"),colored(f"'{tr.name}: Do you know Thunderbolt?' was his first greeting to me. It wasn't until after we battled that I learned his name was Volkner.' That's part of a novel I wrote. I absolutely love writing about the close bonds between the Trainers who come here and the Pokémon they train. Could I use you and your Pokémon as a subject?\n","white")])
        print(x)
    if "Karen" in tr.name:
        print(colored(f" {tr.name}: I am Karen of the Elite Four. You're {srname}? How amusing. I love dark-type Pokémon. I find their wild, tough image to be so appealing. And they're so strong. Think you can take them? Just try to entertain me. Let's go.\n","white"))
    if "Drake" in tr.name:
        print(colored(f" {tr.name}: I am the last of the Pokémon League Elite Four, Drake the Dragon master! In their natural state, Pokémon are wild living things. They are free. At times, they hinder us. At times, they help us. For us to battle with Pokémon as partners, do you know what it takes? Do you know what is needed? If you don't, then you will never prevail over me!\n","white"))
    if "Glacia" in tr.name:
        print(colored(f" {tr.name}: Welcome, my name is Glacia of the Elite Four. I've traveled from afar to Hoenn so that I may hone my icy skills. But all I have seen are challenges by weak Trainers and their Pokémon. What about you? It would please me to no end if I could go all out against you!\n","white"))
    if "Sidney" in tr.name:
        print(colored(f" {tr.name}: Welcome, challenger! I'm Sidney of the Elite Four. I like that look you're giving me. I guess you'll give me a good match. That's good! Looking real good! All right! You and me, let's enjoy a battle that can only be staged here in the Pokémon League!\n","white"))
    if "Phoebe" in tr.name:
        print(colored(f" {tr.name}: Ahahaha! I'm Phoebe of the Elite Four. I did my training on Mt. Pyre. While I trained, I gained the ability to commune with Ghost-type Pokémon. Yes, the bond I developed with Pokémon is extremely tight. So, come on, just try and see if you can even inflict damage on my Pokémon!\n","white"))
    if "Malva" in tr.name:
        print(colored(f" {tr.name}: You're the illustrious {srname}, are you? Welcome at last to the Pokémon League. I am one of the Elite Four. People know me as the Fire-type-Pokémon user, Malva. Here in the Pokémon League, you'll encounter the four of us--the Elite Four--and our Champion. If you hope to meet the Champion and challenge her here, you must first defeat the four of us. Do your best, because if you can't impress us with your real strength, you'll never get to battle her. But it should be a walk in the park for you, right? The hero/heroin who destroyed big, bad Team Flare.\n","white"))
    if "Drasna" in tr.name:
        print(colored(f" {tr.name}: Oh goodness, hello to you! Welcome, welcome, come in. You must be a strong Trainer. Yes, quite strong indeed... That's just wonderful news! Facing opponents like you and your team will make my Pokémon grow like weeds!\n","white"))
    if "Wikstrom" in tr.name:
        print(colored(f" {tr.name}: Well met, young challenger! Verily am I the Elite Four's famed blade of hardened Steel, Wikstrom! With my magnificent Pokémon at my side, I will reveal the scope of Trainer achievement! Let us both give our word that our contest shall be fair and honorable. Ready? En garde!\n","white"))
    if "Lucian" in tr.name:
        print(colored(f" {tr.name}: Ah, you timed your arrival well. I've just finished reading a book, you see. Allow me to introduce myself. I am Lucian. I am a user of the Psychic type. I must say, you've already proven yourself to be outstanding by coming this far. They say I am the toughest of the Elite Four. I'm afraid I will have to go all out against you to live up to that reputation.\n","white"))
    if "Bertha" in tr.name:
        print(colored(f" {tr.name}: Well, well. You're quite the adorable Trainer, but you've also got a spine. Ahaha! I'm Bertha. I have a preference for Ground-type Pokémon. Well, would you show this old lady how much you've learned?\n","white"))
    if "Aaron" in tr.name:
        print(colored(f" {tr.name}: Hello! Welcome to the Pokémon League! I'm Aaron of the Elite Four. It's good to meet you. Oh, I should explain, I'm a huge fan of bug Pokémon. Bug Pokémon are nasty-mean, and yet they're beautiful, too... Would you like to know why I take on challengers here, in this room? It's because I want to become perfect, just like my bug Pokémon! Ok! Let me take you on!\n","white"))
    if "Flint" in tr.name:
        print(colored(f" {tr.name}: This situation just cooks! The drama and tension sizzles! Flint, the fiery master of fire Pokémon, is going to put you to the test! Let Flint see how hot your spirit burns!\n","white"))
    if "Siebold" in tr.name:
        print(colored(f" {tr.name}: ... ... ... Yes, I see it now. This is a path with no end. To seek to be the absolute best is an absurd goal. Yet, as long as I am alive, I shall strive onward to seek the ultimate cuisine... and the strongest opponents in battle!\n","white"))
    if "Red" in tr.name:
        print(colored(f" {tr.name}: ........\n","white"))
    if "Cynthia" in tr.name:
        print(colored(f" {tr.name}: One look at you tells me many things about you. Together, you and your Pokémon overcame all the challenges you faced, however difficult. It means that you've triumphed over any personal weaknesses, too. The power you learned... I can feel it emanating from you. That's enough talking. Let's get on with why you're here. I, Cynthia, accept your challenge as the Pokémon League Champion! There won't be any letup from me!\n","white"))
    if "Tobias" in tr.name:
        print(colored(f" {tr.name}: I'm the Lily of the Valley Conference Champion. You probably heard of my Famous Darkrai and Latios. {srname}! But now I will show you my true strength. The strength of Legendary Pokémons.\n","white"))
    if "Wallace" in tr.name:
        print(colored(f" {tr.name}: You have overcome challenges and made it this far because you worked as one with your Pokémon. Show me that strength here and now!\n","white"))
    if "Steven" in tr.name:
        print(colored(f" {tr.name}: Welcome, {srname}. I was looking forward to seeing you here one day. You… What did you see on your journey with Pokémon? What did you feel, meeting so many other Trainers like you? What has awoken in you? I want you to hit me with it all! Now, bring it!\n","white"))
    if "Agatha" in tr.name and "Red" in srname:
        print(colored(f" {tr.name}: I am Agatha of the Elite Four! Oak's taken a lot of interest in you, child! That old duff was once tough and handsome! That was decades ago! Now he just wants to fiddle with his Pokédex! He's wrong! Pokémon are for fighting! {srname}! I'll show you how a real trainer fights!\n","white"))
    if "Lorelei" in tr.name:
        print(colored(f" {tr.name}: Well then, allow me to reintroduce myself. I am Lorelei of the Elite Four. No one can best me when it comes to icy Pokémon.\n Freezing moves are powerful. Your Pokémon will be at my mercy when they are frozen solid. That's because frozen Pokémon can't do a thing in battle! Hahaha!\n Are you ready?\n","red"))
        
    if "Bruno" in tr.name:
        print(random.choice([colored(f" {tr.name}: I am Bruno of the Elite Four! Through rigorous training, people and Pokémon can become stronger without limit. I've lived and trained with my fighting Pokémon! And that will never change! {srname}! We will grind you down with our superior power! Hoo hah!\n","white"),colored(f" {tr.name}: I am Bruno of the Elite Four! The Pokémon you trained. Show them to me! U-waaaah!\n","white")]))
    if "Lance" in tr.name:
        print(random.choice([colored(f" {tr.name}: I've been waiting for you. {srname}! I knew that you, with your skills, would eventually reach me here. There's no need for words now. We will battle to determine who is the stronger of the two of us. As the most powerful trainer and as the Pokémon League Champion… I, Lance the dragon master, accept your challenge!\n","white"),colored(f" {tr.name}: So I see you've come this far. Show me what you've got. Let's see how you fair against the leader of the Elite Four and my army of dragons!\n","white")]))               
