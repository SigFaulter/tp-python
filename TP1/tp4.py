def compte_occurence(list):
    dict = {}
    for mot in list:
        if(mot in dict):
            dict[mot] +=1
        else:
            dict[mot] = 1
    return dict

print(compte_occurence(["b", "b", "c", "l", "c"]))
