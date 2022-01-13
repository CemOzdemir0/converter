INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"


def fix_text(mystr):
    words = mystr.split(' ')
    fixed= ''
    for n in words:
        if(n[0]== '('):
            if(n[1] != '('):
                fixed += ' ' + n.replace("(", "").replace(")", "")
            else:
                fixed += ' (' + n.replace("(", "").replace(")", "")
        else:
            fixed += ' ' +n[::-1]


    return fixed[1:]

if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
    print(fix_text(INPUT))