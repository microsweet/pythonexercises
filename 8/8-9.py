def make_great(magic):
    i=0
    for name in magic:
        name += 'the great' 
        magic[i] = name
        i += 1

def show_magicians(magic):
    for name in magic:
        print(name)

magic = ['bob', 'tec']
make_great(magic)
show_magicians(magic)
