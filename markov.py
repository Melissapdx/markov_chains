"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()
    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    chains = {}

    for i in range(len(words)-2):
        key = (words[i], words[i + 1])
        value = words[(i + 2)]

        if key not in chains:
            chains[key] = [value]
        else:
            chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    new_key = choice(chains.keys())
    new_value = choice(chains[new_key])

    while new_key in chains:

        #and appending to list
        words.append(new_key[1])
        # using value to name next key
        next_value = choice(chains[new_key])
        # using new key to find next value
        new_key = (new_key[1], next_value)

        #chains[new_key].get(new_key, None)



    print " ".join(words)



input_path = "green-eggs.txt"

 #Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print random_text

#print open_and_read_file('green-eggs.txt')
