a = "Kebijaksanaan"

def myfunc():
    print("Filsafat adalah ilmu tentang " + a)

myfunc()

b = "pohon"

def myfunc():
    b = "Masa lalu"
    print("Sejarah adalah ilmu yang mempelajari tentang " + b)

myfunc()

print("Sejarah berasal dari bahasa Arab yang artinya " + b)

def myfunc():
    global c
    c = "Manusia"

myfunc()

print("Antropologi adalah ilmu tentang " + c)

d = "menggali"

def myfunc():
    global d
    d = "yang telah berlalu"

myfunc()

print("Arkeologi adalah ilmu yang mempelajari hasil kebendaan " + d)