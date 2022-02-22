from __future__ import unicode_literals, print_function
import spacy

def read_input_file(filename):
    """
    Read input from input file into string
    :param filename: filename of input file
    :return: string containing all contents of input file
    """

    with open(filename, "r") as f:
        return f.read()


def write_sentences(filename, list):
    fp = open(filename, 'w+')
    for i in range(len(list)):
        fp.write(list[i] + '\n')

# Main program
if __name__ == "__main__":
    filename = "../nlp-project-dev-data-articles/set3/a1.txt"
    input_text = read_input_file(filename)
    nlp_better = spacy.load('en_core_web_sm')
    store = []
    for i in nlp_better(input_text).sents:
        str = i.text.strip()
        if len(str) != 0:
            store.append(str)

    output_file = "../sentences/a1.txt"
    write_sentences(output_file, store)
