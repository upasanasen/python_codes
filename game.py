
import random

waste = ["polybags", "plastic wraps","plastic bottles", "banana peels", "egg shels", "molded breads", "tetrapacked milk boxes", "paper boxes", "egg trays", "notebooks", "tissues", "papertowels", "glass bottles", "glass jars", "broken glass windows"]
bintype = input("choose the dustbin: (hint: (1)plastic, (2)biodegradable, (3)recyclable, (4)paper, (5)glass):" )
for  step in range(10):
	N = random.randint(0, len(waste)-1)
	print(waste[N]) 

