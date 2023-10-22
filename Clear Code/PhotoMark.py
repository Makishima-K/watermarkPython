from PIL import Image, ImageChops
#import tkinter as tk
import random


r = str(random.randint(1 , 200))
s1 = 'Watermark/'
s2 = 'Photo/'
s3 = 'PhotoWithWaterMark/'


p2 =  input('Backgraund name = ')
p1 =  input('Watermark name = ')

if p1 == '':
    p1 = 'WaterMark.png'
if p2 == '':
    p2 = 'SimpleBackground.jpg'


position1 = input('Choose position: right-top, left-top , right-Down, right-top, center, another = ')

watermark2 = Image.open(s1 + p1)
base_image2 = Image.open(s2 + p2)

a3, b3 = watermark2.size
a, b = base_image2.size

if position1 == 'center':
    b = b/2 - b3/2
    a = a/2 - a3/2
elif position1 == 'left-top':
    b = 0
    a = 0
elif position1 == 'left-Down':
    a = 0
    b = b -b3
elif position1 == 'right-Down':
    a = a - a3
    b = b - b3
elif position1 == 'right-top':
    a = a - a3
    b = 0
elif position1 == 'another':
    a = input('x = ')
    b = input('y = ')
else:
    a = 0
    b = 0  

def watermark_with_transparency(input_image_path, output_image_path,  watermark_image_path, position):

    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    
    width, height = base_image.size
   
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    watermark.putalpha(128)

    rgba = watermark.convert("RGBA") 
    datas = rgba.getdata() 
  
    newData = [] 
    for item in datas: 
        if item[0] == 0 and item[1] == 0 and item[2] == 0:  
         
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item) 
  
    rgba.putdata(newData) 
    
    watermark=rgba

    transparent.paste(watermark, position, mask=watermark)
    print(position)
    transparent.show()
    transparent.save( s3 + output_image_path)
 
watermark_with_transparency(str(s2+p2), 'PhotoWithWatermark'+ str(r) + '.png', str(s1+p1), position=(int(a),int(b)))

# --------------------------------------------------------------------------------------

#cc = 'green'

#root = tk.Tk()

#root['bg'] = 'black'

#root.title('FF')

#root.geometry('600x750')

#root.wm_attributes('-alpha', 0.9)

#canvas = Canvas(root, height=300, width=250)
#canvas.pack()

#def gg():
 #   global p1,p2,inputt,inputtt,s2,s1,s3,a,b
 #   
    
 #   
 #   p1 = inputt
#
#    p2 = inputtt
 #   watermark_with_transparency(str(s2+p2), 'PhotoWithPoppy77poppy.png', str(s1+p1), position=(int(a),int(b))) 
#    root.mainloop()

    
#frame = tk.Frame(root, bg='red')
#frame.place(relx=0.15, rely=0.15, relwidth=0.8, relheight=0.5)

#title = tk.Label(frame, text='AAAAAAAAA', bg=cc, font=90)
#title.pack()
#btn= tk.Button(frame, text='BTN', bg='red', command=gg )
#btn.pack()

#inputt= tk.Entry(frame, bg='white')
#inputt.pack()
#p1 = inputt
# 'POP.png'
#inputtt= tk.Entry(frame, bg='green')
#inputtt.pack()
#p2 = inputtt
# p2 = 'TT.jpg'


#root.mainloop()

# ---------------------------------------------------------






