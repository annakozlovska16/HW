import random 

words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
print("Welcome to Worlde!")

def give_hint(secret_word, guessed_letters):
    for i in range(len(secret_word)):
        if secret_word[i] not in guessed_letters:
            print(f"Hint: The letter at position {i + 1} is {secret_word[i].upper()}")
            break

play = "yes"
while play == "yes":
    word = random.choice(words)
    tries = 6
    length = len(word)
    print("Guess the",length,"-letter word. You have", tries, "tries.")
    guessed_letters = set()

    hint_used = False

    while tries > 0:
        guess = input("Enter the word: ")

        if len(guess) != length:
            print("Wrong length. Expected length", length)
            continue 
        if not guess.isalpha():
            print("Please enter letters only.")
            continue

        guessed_letters.update(guess)
        
        if guess == word:
            print("You won!")
            break

        result = []
        for i in range(length):
            if guess[i] == word[i]:
                result.append(" " + guess[i].upper() + " ")
            elif guess[i] in word:
                result.append("*" + guess[i] + " ")
            else: 
                result.append(" " + guess[i] + " ")
                
        print("Result: ", " ".join(result))
        tries = tries - 1
        print("Tries left: ", tries)
        
        if tries == 3 and not hint_used:
            give_hint(word, guessed_letters)
            hint_used = True

    if guess != word:
        print("You lost:(. The word was: ", word.upper())

    play = input("Do you want to play again? yes or no: ").lower()

print("Thanks for playing!")


# Після рефакторингу код стає більш читабельним завдяки змінні назви змінних на більш зрозумілі, 
# покращенню обробки помилок, які виникають через неправильні ведення користувача, підтримці кількох раундів без
# перезапуску програми та додаванню функції підказок.
# Також для покращення можна додати кольори виводу для підсвічування правильних та неправильних літер 
# та зберігання історії спроб.