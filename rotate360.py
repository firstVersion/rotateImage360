from PIL import Image
import math
img = Image.open('image.png')

for i in range(360):
 width = img.size[0]
 height = img.size[1]
 tmp_size = width*2
 tmp = Image.new('RGBA',(tmp_size,tmp_size),(0,0,0,0))
 cx = int((tmp_size - width)/2)
 cy = int((tmp_size - height)/2)
 tmp.paste(img,(cx,cy))
 tmp = tmp.rotate(i)
 cuts = int(math.floor((width+height)/math.sqrt(2)))
 pos = int((tmp_size - cuts)/2)
 tmp = tmp.crop((pos,pos,pos+cuts,pos+cuts))
 tmp.save("./image/"+'rotate'+str(i)+'.png')
