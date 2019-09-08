print('Hello, Django girls!')
if 3>2:
    print("To dziala!")
if 5>2: 
    print("5 jest jednak wieksze od 2")
else:
    print("5 nie jest wieksze od 2")
name = "Sonja"
if name == "ania":
    print("hej ania!")
elif name == "Sonja":
    print("Hej Sonja!")
else: print("Hej anonimie!")
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print ("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume <100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
# change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    volume = 50
    print("That´s better!")
def hi():
    print("Hej!")
    print("Jak sie masz?")
hi()
hi()
def hi(imie):
    if imie == "ania":
        print("hej ania!")
    elif imie == "Sonia":
        print("Hej Sonia!")
    else:
        print('Hej nieznajoma!')
hi("Marta")
def hi(imie):
    print("hej " + imie + "!")
dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ania']
for imie in dziewczyny:
    hi(imie)
    print("kolejna dziewczyna")
for i in range(1, 6):
    print(i)

