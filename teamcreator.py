import sqlite3
name=input("Enter name: ")
db=sqlite3.connect("pokemondata.db")
c=db.cursor()
c.execute(f"""CREATE TABLE IF NOT EXISTS [{name}] (
        Name text,
        Nickname text,
        hpev integer default 0,
        atkev integer default 0,
        defev integer default 0,
        spatkev integer default 0,
        spdefev integer default 0,
        speedev integer default 0,
        Ability text default None,
        Nature text default Bashful,
        Shiny text default No,
        Item text default None,
        gender text default Male,
        teratype text default '???',
        moves text default 'A,B,C,D'
        )""")
print("Done")
db.commit()        