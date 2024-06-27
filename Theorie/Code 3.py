# Dit is de code. Geef het juiste antwoord!

def function(text):
    result = text
    for i in range(10, 0):
        result += str(i) + " "
    return result + "done!"


output = function("Counter: ")

# =========================================================================


import check

antwoorden = {
    "a": "Counter: done!",
    "b": "Counter: 10 9 8 7 6 5 4 3 2 1 done!",
    "c": "Counter: 0 1 2 3 4 5 6 7 8 9 done!",
    "d": "Counter: 0 1 2 3 4 5 6 7 8 9 10 done!",
    "e": "Error: Index out of range!",
}
check.check_anwser(antwoorden, output)
