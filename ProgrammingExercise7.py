import re


def main():
    # Have the user enter a paragraph
    paragraph = input("Enter a paragraph:\n")

    # Split paragraph into sentences
    sentences = re.split(r'(?<=[.!?])\s+', paragraph)

    # Remove any empty strings
    sentences = [sentence for sentence in sentences if sentence]

    # Display each sentence
    print("\nIndividual Sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")

    # Display the total number of sentences
    print(f"\nTotal number of sentences: {len(sentences)}")


# Run the program
main()