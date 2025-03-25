char = input("Enter frame character ==> ").strip()
print(char)
height = int(input("Height of box ==> "))
print(height)
width = int(input("Width of box ==> ").strip())
print(width,end="\n\n")
print("Box:")
w = char * width
vertical = char + " "*(width-2) + char
center_space = int((width - 2 - len(str(width)) - len(str(height)) - 1)/2)
vert_space = int((height-3)/2)
center = char + (" "*center_space) + str(width) + "x" + str(height) + " "*(center_space-1+center_space) + char


print(w)                                                        # Top
print((vertical+'\n')*vert_space,end="")                                        # First half of vertical print
print(center)                                                   # Center
print((vertical+'\n')*(vert_space-1+vert_space),end="")                                        # Second half of vertical print
print(w)                                                        # Bottom