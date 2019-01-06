import sqlite3

clients = [
    {
        'nom': 'a',
        'prenom': 'A',
        'birth': '111', 
        'id': 1
    },
    {
        'nom': 'b',
        'prenom': 'B',
        'birth': '222', 
        'id': 2
    },
    {
        'nom': 'c',
        'prenom': 'C',
        'birth': '333', 
        'id': 3
    }
]

goods = [
    {
        'nom' : 'a',
        'description' : 'd',
        'kind' : 'k',
        'ville' : 'v',
        'piece' : 1,
        'carac' : 'k',
        'proprietaire' : 1,
        'id': 1
    },
    {
        'nom' : 'a',
        'description' : 'd',
        'kind' : 'k',
        'ville' : 'v',
        'piece' : 1,
        'carac' : 'k',
        'proprietaire' : 2,
        'id': 2
    },
    {
        'nom' : 'a',
        'description' : 'd',
        'kind' : 'k',
        'ville' : 'v',
        'piece' : 1,
        'carac' : 'k',
        'proprietaire' : 3,
        'id': 3
    },
    {
        'nom' : 'a2',
        'description' : 'd2',
        'kind' : 'k2',
        'ville' : 'v2',
        'piece' : 1,
        'carac' : 'k2',
        'proprietaire' : 1,
        'id': 4
    },
    {
        'nom' : 'a2',
        'description' : 'd2',
        'kind' : 'k2',
        'ville' : 'v2',
        'piece' : 1,
        'carac' : 'k2',
        'proprietaire' : 2,
        'id': 5
    },
    {
        'nom' : 'a2',
        'description' : 'd2',
        'kind' : 'k2',
        'ville' : 'v2',
        'piece' : 1,
        'carac' : 'k2',
        'proprietaire' : 3,
        'id': 6
    }
]


conn = sqlite3.connect('../data/data.db')
c = conn.cursor()

c.execute('drop table if exists Users;')
c.execute("CREATE TABLE IF NOT EXISTS Users(nom, prenom, birth, id);")

for client in clients:
    row = [
        client.get('nom'),
        client.get('prenom'),
        client.get('birth'),
        client.get('id')
    ]
    c.execute("insert into Users values (?,?,?,?)", row)

c.execute('drop table if exists Goods;')
c.execute("CREATE TABLE IF NOT EXISTS Goods(nom, description, kind, ville, piece, carac, proprietaire, id);")

for good in goods:
    row = [
        good.get('nom'),
        good.get('description'),
        good.get('kind'),
        good.get('ville'),
        good.get('piece'),
        good.get('carac'),
        good.get('proprietaire'),
        good.get('id')
    ]
    c.execute("insert into Goods values (?,?,?,?,?,?,?,?)", row)
conn.commit()
#results = c.execute('select * from Goods where id = 1').fetchall()
#print(results)
conn.close()
