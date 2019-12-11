import random

def get_link(file):
    f = open(file)
    lines = f.readlines()
    filessize = len(lines)
    index = random.randint(0,filessize)
    link = lines[index]
    f.close()
    return link



