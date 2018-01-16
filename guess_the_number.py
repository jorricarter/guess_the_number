import random
not_a_number = 'That is not a number. Please try again.'
correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'



def configure_range():
    '''Set the high and low values for the random number'''
    num_range = int(input('Enter a number to set the range of number: '))
    return 1, num_range


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    #todo varify input is a number. if not, notify user
    try:
        return int(input('Guess the secret number:\n'))
    except ValueError:
        return 'null'


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == 'null':
        return not_a_number
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    counter = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)
        print('number of guesses: ', counter)

        counter += 1
        if result == correct:
            break

if __name__ == '__main__':
    replay = "Yes"
    while replay == "Yes" or replay =="yes":
        main()
        while replay != "yes" or replay != "Yes" or replay != "No" or replay != "no":
            replay = input("Would you like to play again?\n'Yes' or 'No'?\n")
            if replay == "No" or replay == "no":
                break
            if replay != 'Yes' or replay != 'yes':
                    print("I'm sorry, I did not understand your response.")
