from tag import *
import stanza

def match_npvp(tree):
    tree = tree.children[0]
    if tree.label != SENTENCE:
        return False
    if len(tree.children) != 3:
        return False
    #look for np and vp structure
    if tree.children[0].label != NP:
        return False
    if tree.children[1].label != VP:
        return False
    return True

def binary_questions(doc):
    question = ""
    for word in doc.sentences[0].words:
        if word.deprel == "aux":
            return aux_binary_quesitons(doc)
        elif word.xpos == "VBP":
            question = "Do " + question
            question = question + word.lemma + " "
        elif word.xpos == "VBZ":
            question = "Does " + question
            question = question + word.lemma + " "
        elif word.xpos == "VBD":
            question = "Did " + question
            question = question + word.lemma + " "
        elif word.xpos == ".":
            break;
        else:
            question = question + word.text + " "

    return format_question(question)

def aux_binary_quesitons(doc):
    question = ""
    for word in doc.sentences[0].words:
        if word.deprel == "aux":
            question = word.text + " " + question
        elif word.xpos == ".":
            break;
        else:
            question = question + word.text + " "

    return format_question(question)


def format_question(question):
    str = question.strip()
    str = str[0].upper() + str[1:len(str)]
    str = str + "?"
    return str

# Main program
if __name__ == "__main__":
    sentences = ["John made a cake.", "Mary makes a cake.", "I make a cake.", "John has made a cake.", "I have made a cake.", "She had made a cake."]
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,constituency,lemma,depparse')
    for line in sentences:
        doc = nlp(line)
        tree = doc.sentences[0].constituency
        if match_npvp(tree):
            question = binary_questions(doc)
            print(line)
            print(question)