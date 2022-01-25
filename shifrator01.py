import pyperclip

def do():
    '''asks for sentence, split, replace'''
    global reversed_text

    original_text = input("\n\nwrite text to shifr : ").lower()



    reverce_txt(original_text)
    replacer(reversed_text)
    do()



def reverce_txt(txt_var):
    '''revercing words, but not changing the order'''

    global reversed_text

    splited_or_txt = txt_var.split()
    reversed_text = list(map(lambda txt: txt[::-1], splited_or_txt))
    reversed_text = " ".join(reversed_text)



def replacer(txt):
    '''takes reversed sentence, replaces letters and restarts the programm'''
# symbols starts with 0, english letters - with 1, russisan letters - with 2 or 3

    original_list = (".", "?", "!", ")", "(", ",", "-",
    "o", "u", "y", "a", "e", "i", "b", "m", "l", "h",
    "ю", "о", "у", "а", "е", "и", "я", "э", "ы",
    "т", "п")
    shifrate_list = ("01gkg", "04str", "03pwq", "02sdj", "05wxz", "05nfw", "07wtr",
    "14cnp", "15sdg", "16pvk", "11xfj", "12jdq", "13dnz", "17jrw", "18kfj", "19sxq", "10drg",
    "24cnp", "25sdg", "26pvk", "21xfj", "22jdq", "23dnz", "27wtq", "28sfz", "29kxw",
    "33wnd", "31jtj")

    global reversed_text

    reverce_txt(reversed_text)

    if reversed_text.endswith(".rvr1"):

        reversed_text = reversed_text.replace(".rvr1", "")

        for i in range(len(original_list)):
            reversed_text = reversed_text.replace(shifrate_list[i], original_list[i])
            i += 1

        print("\n{0}".format(reversed_text))

    else:
        for i in range(len(shifrate_list)):
            reversed_text = reversed_text.replace(original_list[i], shifrate_list[i])
            i += 1

        print("\n{0}.rvr1".format(reversed_text))

        copy()

def copy():
    pyperclip.copy("{0}.rvr1".format(reversed_text))
    print("\n(copied to copied to clipboard)")

'''starts code '''
do()
