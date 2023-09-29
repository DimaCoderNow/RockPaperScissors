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
    user_hand = int(input("Введите номер: "))

    print(f"Bot: {bot_hand}, You: {hands[user_hand - 1]}")

    if win_hands[bot_hand] == hands[user_hand - 1]:
        print("Bot win")
    elif bot_hand == hands[user_hand - 1]:
        print("Ничья")
    else:
        print("You win!")
    if input("Еще играем? 1-Да, 0-нет: ") == "1":
        continue
    else:
        break