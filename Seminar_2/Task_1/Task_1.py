n = 6
refr = ['gylfole', 'ant0n', '0000a0000n00t00000o000000n', '222anton456', 'richard', 'a1n1t1o1n1']
for i in range(n):
    if 'a' in refr[i]:
        refr[i] = refr[i][refr[i].find('a'):]
        if 'n' in refr[i]:
            refr[i] = refr[i][refr[i].find('n'):]
            if 't' in refr[i]:
                refr[i] = refr[i][refr[i].find('t'):]
                if 'o' in refr[i]:
                    refr[i] = refr[i][refr[i].find('o'):]
                    if 'n' in refr[i]:
                        print (i + 1)
