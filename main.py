import random

def deal_card():
    '''Функция выбора случайной карты из списка'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Расчет суммы очков у каждого игрока'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Ничья"
    elif computer_score == 0:
        return "Вы проиграли, у противника Blackjack"
    elif user_score == 0:
        return "Вы выиграли, у Вас Blackjack"
    elif user_score > 21:
        return "У Вас перебор. Вы проиграли"
    elif computer_score > 21:
        return "У противника перебор. Вы выиграли"
    elif user_score > computer_score:
        return "Вы выиграли"
    else:
        return "Вы проиграли"

def play_game():
    # Списки карт игрока и компьютера
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Раздаем по 2 карты каждому игроку
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Цикл выдает карты игроку до момента, пока игрок не наберет 21 очко или более
    while not is_game_over:
        # Считаем счет игрока и компьютера
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        # Выводим счет на экран
        print(f" Ваши карты: {user_cards}, текущий счет: {user_score}")
        print(f" Первая карта компьютера: {computer_cards[0]}")
        # Проверяем счет
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Введите 'y' чтобы взять еще карту, введите 'n' для завершения: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # Цикл выдает карты компьютеру, пока тот не наберет 21 или пока у него меньше 17 очков.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Ваши карты: {user_cards}, финальный счет: {user_score}")
    print(f" Карты компьютера: {computer_cards},  финальный счет: {computer_score}")
    print(compare(user_score, computer_score))

while input("Хотите сыграть в Blackjack? Введите 'y' или 'n': ") == "y":
    play_game()
