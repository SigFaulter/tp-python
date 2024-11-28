def fusionner_dicts(dic1, dic2):
    dict = {}
    for key, val in dic1.items():
        if(key in dic2.keys()):
            dict[key] = val + dic2[key]
        else:
            dict[key] = val
    for key, val in dic2.items():
        if(key not in dict.keys()):
            dict[key] = val;
    return dict

dic1 = {"num": 2, "a": 3 }
dic2 = {"num": 4, "b": 0 }

print(fusionner_dicts(dic1, dic2))
