# Dit is de code. Geef het juiste antwoord!

output = 0
for i in range(0, 10):
    if i % 2 == 0:
        output += i

# =========================================================================


from Oplossingen import check
antwoorden = {
    "a": 15,
    "b": 20,
    "c": 25,
    "d": 30
}
check.check_anwser(antwoorden, output)
