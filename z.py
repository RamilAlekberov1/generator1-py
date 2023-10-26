g = [
{'id':1, 'full_name': 'Алекберов Рамиль Русланович'},
{'id':2, 'full_name': 'Бобровская Анастасия Дмиьриевна'},
{'id':2, 'full_name': 'Винговатов Александр Олегович'},

]

f = [g['full_name'] for g in g if len(g['full_name'].split()[1]) > 6]

print (f)
