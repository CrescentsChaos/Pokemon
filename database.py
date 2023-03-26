import sqlite3
def showall(trainer):
    db=sqlite3.connect(f"pokémon.db")
    c=db.cursor()
    c.execute(f"SELECT rowid, * FROM [{trainer.name}]")
    items=c.fetchall()
    for i in items:
        print (i)
    db.commit()
    db.close()
def createtable(trainer):
    print(f" Adding {trainer.name} to the database...")
    db=sqlite3.connect(f"pokémon.db")
    c=db.cursor()    
    if "Z-Crystal" in trainer.pokemons[-1].name:
        trainer.pokemons[-1].name=trainer.pokemons[-1].name.split("(")[0]
    c.execute(f"""CREATE TABLE IF NOT EXISTS [{trainer.name}] (
    Name text,
    Nature text,
    Ability  text,
    Item text,
    Move1 text,
    Move2 text,
    Move3 text,
    Move4 text
     )""")
    db.commit()
    c.execute(f" SELECT * FROM [{trainer.name}]")
    items=c.fetchall()
    db.commit()
    n=0
    while True:
        if trainer.pokemons[n].name not in items:
            c.execute(f" SELECT * FROM [{trainer.name}] WHERE Name='{trainer.pokemons[n].name}'")
            check=c.fetchone()
            if check==None:
                check=[]
            db.commit()
            if trainer.pokemons[n].name in check:
                c.execute(f"""UPDATE [{trainer.name}] SET
                Name="{trainer.pokemons[n].name}",
                Nature="{trainer.pokemons[n].nature}",
                Ability="{trainer.pokemons[n].ability}",
                Item="{trainer.pokemons[n].item}",
                Move1="{trainer.pokemons[n].moves[0]}",
                Move2="{trainer.pokemons[n].moves[1]}",
                Move3="{trainer.pokemons[n].moves[2]}",
                Move4="{trainer.pokemons[n].moves[3]}" WHERE Name="{trainer.pokemons[n].name}" """)
                db.commit()
            if trainer.pokemons[n].name not in check:
                c.execute(f"""INSERT INTO [{trainer.name}] VALUES (
                "{trainer.pokemons[n].name}",
                "{trainer.pokemons[n].nature}",
                "{trainer.pokemons[n].ability}",
                "{trainer.pokemons[n].item}",
                "{trainer.pokemons[n].moves[0]}",
                "{trainer.pokemons[n].moves[1]}",
                "{trainer.pokemons[n].moves[2]}",
                "{trainer.pokemons[n].moves[3]}"
                 )""")
                db.commit()
        n+=1
        if n==6:
            break
    db.commit()
    db.close()