def pig_it(text):
    # Split the input text into a list of words
    words = text.split()

    # Iterate through each word in the list
    for i in range(len(words)):
        word = words[i]
        # Check if the word contains only alphabetic characters
        if word.isalpha():
            # Move the first character to the end of the word and add "ay"
            words[i] = word[1:] + word[0] + "ay"
    # Join the words back into a single string with space as delimiter
    return " ".join(words)
