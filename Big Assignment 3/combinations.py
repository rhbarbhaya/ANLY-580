from itertools import combinations
text = '''VCI =~ inform + simil + vocab + compreh
WMI =~ digspan + arith
POI =~ piccomp + block + matrixreason
PSI =~ symbolsearch + digsym
IQ =~ inform + simil + vocab + compreh + digspan + arith + piccomp + block + matrixreason + symbolsearch + digsym'''
combo = ["digsym ~~ 0*digsym", "digspan ~~ 0*digspan", "piccomp ~~ 0*piccomp", "matrixreason ~~ 0*matrixreason", 
"block ~~ 0*block", "compreh ~~ 0*compreh", "simil ~~ 0*simil", "vocab ~~ 0*vocab", 
"inform ~~ 0*inform", "arith ~~ 0*arith", "symbolsearch ~~ 0*symbolsearch"]
res = []

# for i in range(len(combo)):
#     res.append(combinations(combo, 1))

a = (combinations(combo, 3))
for j in a:
    print(r"```{r}")
    print("bifactor = '")
    print(text)
    print(j[0])
    print(j[1])
    print(j[2])
    print("'")
    print(("bifactor.fit = cfa(bifactor, data = data2, check.gradient = F)"))
    print(r"```")
    print("")