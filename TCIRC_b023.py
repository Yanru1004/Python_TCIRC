#b023 十二生肖

animal = {1:'Rat',
          2:'Ox',
          3:'Tiger',
          4:'Hare',
          5:'Dragon',
          6:'Snake',
          7:'Horse',
          8:'Sheep',
          9:'Monkey',
          10:'Rooster',
          11:'Dog',
          0:'Pig'}

while True:
    try:
        year = int(input())

        print(animal[(year-3)%12])

    except:
        break