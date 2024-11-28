def analyse_texte(text):
    return {"mots": len(text.split()), "chars": len(text) - text.count(" ")}

print(analyse_texte("vcxv 12 dfsdf cvx; .!3!#["))

