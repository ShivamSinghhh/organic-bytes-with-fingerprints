from random import choice

from art import logo


def select_card():
    """Returns a random selected card value"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def compare_score(u_score, b_score):
    if u_score == b_score:
        return "Draw 🙃"
    elif b_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over 21You lose 😭"
    elif b_score > 21:
        return "Opponent went over 21. You win 😁"
    elif u_score > b_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def calculate_score(scores):
    """Calculates the final score and if it is above 21, replacing ace(value-11) with 1"""
    if 11 in scores and 10 in scores and len(scores) == 2:
        return 0
    if 11 in scores and sum(scores) > 21:
        scores.remove(11)
        scores.append(1)
    return sum(scores)


def play_game():
    print(logo)
    user_choice: list[int] = []
    user_score = -1
    bot_score = -1
    bot_choice: list[int] = []
    is_game_over = False

    for _ in range(2):
        user_choice.append(select_card())
        bot_choice.append(select_card())

    while not is_game_over:
        user_score = calculate_score(user_choice)
        bot_score = calculate_score(bot_choice)
        print(
            f"Your choices are {user_choice} and your score is: {calculate_score(user_choice)}"
        )
        print(f"Bot first card is {bot_choice[0]} ")

        if user_score == 0 or bot_score == 0 or user_score >= 21 or bot_score >= 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to take cards ? (y/n): ").lower()
            if user_should_deal == "y":
                user_choice.append(select_card())
            else:
                is_game_over = True

    while bot_score != 0 and bot_score < 17:
        bot_choice.append(select_card())
        bot_score = calculate_score(bot_choice)

    print(f"Bot choices are {bot_choice} and their final score is: {bot_score}")
    print(f"user choices are {user_choice} and their final score is: {user_score}")
    print(compare_score(user_score, bot_score))


while input("Do you want to play Blackjack? (y/n): ").lower() == "y":
    print("/n" * 20)
    play_game()
