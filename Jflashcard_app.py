import random

# Dictionary of Japanese words and their meanings.
flashcards = {
    "猫": "cat",
    "犬": "dog",
    "水": "water",
    "火": "fire",
    "山": "mountain",
    "空": "sky",
    "先生": "teacher",
    "友達": "friend",
    "本": "book",
    "日本": "japan"
}

print("👋 Welcome to the Japanese Flashcard App!")
print("Type the English meaning of the word. Type 'exit' to quit.\n")

# Game loop
while True:
    word = random.choice(list(flashcards.keys()))
    answer = input(f"What is the meaning of '{word}'? ").strip().lower()

    if answer == 'exit':
        print("Thanks for playing! またね！👋")
        break

    if answer == flashcards[word]:
        print("✅ Correct!\n")
    else:
        print(f"❌ Incorrect. The correct answer is '{flashcards[word]}'.\n")
