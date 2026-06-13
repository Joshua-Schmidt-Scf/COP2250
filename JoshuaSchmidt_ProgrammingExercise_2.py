# Joshua Schmidt Programming Exercise 2

"""Gets an email message from the user."""
def get_email():
    print("Enter an email message:")
    return input("> ")

"""Checks email for spam words and phrases and returns score and matches."""
def check_spam(email):

    spam_words = [
        "# 1",
        "100 % more",
        "100 % free",
        "100 % satisfied",
        "additional income",
        "be your own boss",
        "best price",
        "big bucks",
        "billion",
        "cash bonus",
        "cents on the dollar",
        "consolidate debt",
        "double your cash",
        "double your income",
        "earn extra cash",
        "act now",
        "apply now",
        "become a member",
        "call now",
        "click below",
        "click here",
        "get it now",
        "do it today",
        "don’t delete",
        "exclusive deal",
        "get started now",
        "important information regarding",
        "information you requested",
        "instant",
        "limited time"
    ]

    score = 0
    found_words = []

    email = email.lower()

    for word in spam_words:
        occurrences = email.count(word)

        if occurrences > 0:
            score += occurrences
            found_words.append(word)

    return score, found_words

"""Determines likelihood of spam risk."""
def spam_rating(score):

    if score == 0:
        return "Very Low Spam Risk"
    elif score <= 3:
        return "Low Spam Risk"
    elif score <= 7:
        return "Moderate Spam Risk"
    elif score <= 12:
        return "High Spam Risk"
    else:
        return "Very High Spam Risk"


def main():
    email = get_email()

    score, found_words = check_spam(email)

    print("\n--- Spam Analysis Results ---")
    print("Spam Score:", score)
    print("Likelihood:", spam_rating(score))

    if found_words:
        print("\nWords/Phrases Found:")
        for word in found_words:
            print("-", word)
    else:
        print("\nNo spam words or phrases were detected.")


main()