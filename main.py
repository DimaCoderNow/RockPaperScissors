import random


hands = ["камень", "ножницы", "бумага"]
win_hands = {"камень": "ножницы",
             "ножницы": "бумага",
             "бумага": "камень",
             }

while True:
    bot_hand = random.choice(hands)
    # Меню
    print("1 - камень")
    print("2 - ножницы")
    print("3 - бумага")
    user_hand = input("Введите номер: ")
