import os


chap=0
inis=[1,42, 77, 114, 166,198, 218, 238, 273, 330,401,463, 506]
for ini in inis:
    fini = ini + 15
    chap+=1
    print("\rcropping chapter {}...".format(chap), end="")
    os.system(" pdftk book.pdf cat {}-{} output chap{}.pdf".format(ini,fini,chap))
