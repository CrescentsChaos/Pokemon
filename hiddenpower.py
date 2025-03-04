import math
a=26
b=16
c=31
d=29
e=30
f=30
damage=0
type=""

async def hidp(a,b,c,d,e,f):
    adbit=0
    bdbit=0
    cdbit=0
    ddbit=0
    edbit=0
    fdbit=0
    atbit=0
    btbit=0
    ctbit=0
    dtbit=0
    etbit=0
    ftbit=0
    if a%4==0:
        adbit=0
        atbit=0
    if a%4==1:
        adbit=0
        atbit=1
    if a%4==2:
        adbit=1
        atbit=0
    if a%4==3:
        adbit=1
        atbit=1
    if b%4==0:
        bdbit=0
        btbit=0
    if b%4==1:
        bdbit=0
        btbit=1
    if b%4==2:
        bdbit=1
        btbit=0
    if b%4==3:
        bdbit=1
        btbit=1
    if c%4==0:
        cdbit=0
        ctbit=0
    if c%4==1:
        cdbit=0
        ctbit=1
    if c%4==2:
        cdbit=1
        ctbit=0
    if c%4==3:
        cdbit=1
        ctbit=1
    if d%4==0:
        ddbit=0
        dtbit=0
    if d%4==1:
        ddbit=0
        dtbit=1
    if d%4==2:
        ddbit=1
        dtbit=0
    if d%4==3:
        ddbit=1
        dtbit=1
    if e%4==0:
        edbit=0
        etbit=0
    if e%4==1:
        edbit=0
        etbit=1
    if e%4==2:
        edbit=1
        etbit=0
    if e%4==3:
        edbit=1
        etbit=1
    if f%4==0:
        fdbit=0
        ftbit=0
    if f%4==1:
        fdbit=0
        ftbit=1
    if f%4==2:
        fdbit=1
        ftbit=0
    if f%4==3:
        fdbit=1
        ftbit=1
    damage=round(((1*adbit+2*bdbit+4*cdbit+8*ddbit+16*edbit+32*fdbit)*40)/63)+30
    tn=math.floor(((1*atbit+2*btbit+4*ctbit+8*dtbit+16*etbit+32*ftbit)*15)/63)
    if tn==0:
        type="Fighting"
    if tn==1:
        type="Flying"
    if tn==2:
        type="Poison"
    if tn==3:
        type="Ground"
    if tn==4:
        type="Rock"
    if tn==5:
        type="Bug"
    if tn==6:
        type="Ghost"
    if tn==7:
        type="Steel"
    if tn==8:
        type="Fire"
    if tn==9:
        type="Water"
    if tn==10:
        type="Grass"
    if tn==11:
        type="Electric"
    if tn==12:
        type="Psychic"
    if tn==13:
        type="Ice"
    if tn==14:
        type="Dragon"
    if tn==15:
        type="Dark"
    return damage,type
x=hidp(a,b,c,d,e,f)
#print("HP",x[1],x[0])