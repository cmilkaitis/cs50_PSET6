from nltk.tokenize import sent_tokenize

def getSubs(c,n):
    subs = []
    for i in range(len(c)):
	    sub = c[i:i+n]
	    if len(sub) == n:
		    subs.append(sub)
    return subs


def lines(a, b):
    """Return lines in both a and b"""
    a = a.splitlines()
    b = b.splitlines()

    matches = list(set(a).intersection(set(b)))
    return matches


def sentences(a, b):
    """Return sentences in both a and b"""
    aList = sent_tokenize(a)
    bList = sent_tokenize(b)

    matches = list(set(aList).intersection(set(bList)))
    return matches


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    aList = getSubs(a,n)
    bList = getSubs(b,n)
    matches = list(set(aList).intersection(set(bList)))
    return matches
