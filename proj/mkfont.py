from PIL import Image


im = Image.open("font.png").convert('RGB')

font_list = [0] * 256 

for i in range(0,16*16):
    guide_x = i%16
    guide_y = i//16
    val = 0
    for y in range(0,5):
        ny = guide_y*5 + y
        for x in range(0,5):
            nx = guide_x*5 + x
            r, g, b = im.getpixel((nx, ny))
            n = (r+g+b) > 0
            val = (val << 1) + n
    font_list[i] = val


for font in font_list:
    string = ""
    for i in range(0,25):
        
        if (font//(1<<(25-i))%2) == 1:
            string+= "■"
        else:
            string+= " "
        if i%5 == 4:
            print(string)
            string = ""
    print("----")


new = ""
i = 5000
for num in font_list:
    new += "ld r0 "+ str(i) + "\n"
    new += "ld r1 "+str(num)+ "\n"
    new += "wr r0 r1\n"
    i+=1
    
file = open("fontmade.txt","w")
file.write(new)
file.close()
