# Dit is geen vraagstuk of theorie. Deze file is puur om de antwoorden te controlleren!
def question(antwoorden):
    print("Bekijk de code. 1 van deze onderstaande antwoorden is juist:")
    answers_list = []
    for answer in antwoorden.keys():
        print(f"{answer}\t-\t {antwoorden[answer]}")
        answers_list.append(answer)
    print()
    mijn_antwoord = input("Kies uit de bovenstaande antwoorden (a, b, ...): ")
    while str(mijn_antwoord).lower() not in answers_list:
        mijn_antwoord = input("Kies uit de bovenstaande antwoorden (a, b, ...): ")
    return mijn_antwoord


def check_anwser(answers, result):
    guess = question(answers)
    correct_answer = None
    for answer in answers.keys():
        if answers[answer] == result:
            correct_answer = answer
    print()
    print(f"Jij koos: \t\t\t\t\t{guess} ({answers[guess]})")
    print(f"Het juiste antwoord was: \t{correct_answer} ({answers[correct_answer]})")
    print('Je had het juist!' if guess == correct_answer else 'Je had het fout!')
