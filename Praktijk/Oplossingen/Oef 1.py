def full_name(first_name, surname):
    # If there is no surname given, then the space between the first and surname shouldn't be given
    return first_name + (" " + surname if surname != "" else "")


def word_counter(sentence):
    # "" will return 1. Check if the sentence isn't empty -> return 0!
    return len(str(sentence).strip().split(" ")) if str(sentence).strip() != "" else 0


def average_number(numbers):
    return sum(numbers) // len(numbers)

    # OR

    # average = 0
    # for number in numbers:
    #     average += number
    # return average // len(numbers)
