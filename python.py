def flames(person1, person2):
    person1 = person1.lower().replace(" ", "")
    person2 = person2.lower().replace(" ", "")

    unique_characters = list(set(person1 + person2))
    total_count = len(unique_characters)
    print(unique_characters)
    flames = "FLAMES"
    while len(flames) > 1:
        index = (total_count % len(flames)) - 1
        index = index if index >= 0 else len(flames) - 1 
        flames = flames[:index] + flames[index + 1:]

    return flames

def flames_game():
    person1 = input("Enter the name of Person 1: ")
    person2 = input("Enter the name of Person 2: ")

    result = flames(person1, person2)

    relationship = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Admirers',
        'M': 'Married',
        'E': 'Enemies',
        'S': 'Siblings'
    }

    print(f"The relationship between {person1} and {person2} is: {relationship[result]}")

flames_game()
