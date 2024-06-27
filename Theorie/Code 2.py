# Dit is de code. Geef het juiste antwoord!

a = True
b = a
a = False
output = b

# =========================================================================


from Oplossingen import check
antwoorden = {
    "a": True,
    "b": False
}
check.check_anwser(antwoorden, output)
