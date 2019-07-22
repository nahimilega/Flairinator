flairs = ['Photography','Politics', 'Non-Political', 'Science/Technology','AskIndia', '[R]eddiquette', 'Policy/Economy', 'Business/Finance',  'Scheduled', 'Sports', 'Food' ]

c ='Science/Technology'

def read_file(flair):
    filename = flair[1]+ flair[-1] + 'tf'+ '.txt'
    f = open(filename, "r")
    all_p ={}
    for x in f:
        g = x.split("   ")

        all_p[g[0]] = float(g[1][:-1])

    return all_p

if __name__ == "__main__":
    mm = read_file(c)

    all_of = []
    for flair in flairs:
        all_of.append(read_file(flair))
    final = []
    for aaa in list(mm.keys()):
        cctr=0
        for kk in all_of:
            cctr += kk[aaa]
        if cctr > 9:
            final.append(aaa)

    with open('final.txt', mode='w') as f:
        for jj in final:
            f.write(jj + "\n")