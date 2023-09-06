
status_1 = True
status_2 = True
status_3 = True

elems = [
    {"h1": True, "robots": True},
    {"h1": False, "robots": False},
    {"h1": True, "robots": True}
]


for elem in elems:

    if elem["h1"] and elem["robots"]:
        print ("todo salió bien")
    else:
        print ("algo salió mal")