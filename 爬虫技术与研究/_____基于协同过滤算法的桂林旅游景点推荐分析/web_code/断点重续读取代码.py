with open(r"data\urls_new.txt") as f:
    url=f.read()

lis=url.replace("{","").replace("}","").replace("'","").split(sep=", ")
