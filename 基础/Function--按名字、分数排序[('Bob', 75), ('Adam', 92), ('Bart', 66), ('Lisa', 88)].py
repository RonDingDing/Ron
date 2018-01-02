l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(l):
    return l[0].lower()

def by_score(l):
    return l[1]


sorted(l, key=by_score, reverse=True)
    

 
