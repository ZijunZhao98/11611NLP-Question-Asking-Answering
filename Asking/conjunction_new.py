from tag import *
import re



def matched(tree):
    tree = tree.children[0]
    if tree.label != SENTENCE:
        return False
    if len(tree.children) < 3:
        return False
    np_true = False
    vp_true = False
    #look for np and vp structure
    for child in tree.children:
        if child.label == NP:
            np_true = True
        if child.label == VP:
            vp_tree = child.children
            vp_true = True
    if not np_true or not vp_true:
        return False
    #look for #VP,VP,CC,VP
              #VP,CC,VP
    check_str = "" #a string for checking
    for child in vp_tree:
        check_str = check_str + child.label
    result = re.search("VP(,VP)?CCVP", check_str)
    if result is None:
        return False

    return True

def split_apposition(tree):
    two_sentences = []
    np1 = []
    tree.children[0].children[0].visit_preorder(leaf=lambda x: np1.append(x.label))
    np2 = []
    tree.children[0].children[2].visit_preorder(leaf=lambda x: np2.append(x.label))
    vp = []
    tree.children[1].visit_preorder(leaf=lambda x: vp.append(x.label))
    two_sentences.append(combine_two_sentences(np1, vp))
    two_sentences.append(combine_two_sentences(np2, vp))
    return two_sentences

def combine_two_sentences(np, vp):
    str1 = ' '.join(np)
    str2 = ' '.join(vp)
    str = str1 + ' ' + str2
    str = str.capitalize()
    return str