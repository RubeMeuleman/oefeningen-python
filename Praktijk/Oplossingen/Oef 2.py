def word_breaker(word, word_list):
    for i in range(1, len(word)):
        first_part = word[:i].strip()
        second_part = word[i:].strip()
        if first_part in word_list and second_part in word_list:
            return True
    return False


def bertje_zijn_boodschappenlijst(given_list):
    # Maak een gesorteerde lijst
    sorted_list = [given_list[0]] if len(given_list) > 0 else []
    # Start met de loop van de lijst
    if sorted_list:
        for i in range(1, len(given_list)):
            item_placed = False
            # Loop door de gesorteerde lijst
            for j in range(len(sorted_list)):
                # Controlleer of het huidige item kleiner is als het huidige item in de gesorteerde lijst
                if len(given_list[i]) < len(sorted_list[j]):
                    # Voeg het item in de gesorteerde lijst
                    sorted_list.insert(j, given_list[i])
                    item_placed = True
                    break
            # Als het item niet kleiner is als al de andere items, dan plaatsen we deze op het einde van de gesorteerde lijst
            if not item_placed:
                sorted_list.append(given_list[i])
    return sorted_list
