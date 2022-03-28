def writeinfo():
	with open('test.jpg', 'ab') as f:
		f.write(b'hello world')
def readinfo():
	with open('test.jpg', 'rb') as f:
		content = f.read()
		offset = content.index(bytes.fromhex('FFD9'))
		f.seek(offset + 2)
		print(f.read())
	
import PIL.Image
import io

def writeimg():
	img = PIL.Image.open('programmer.png')
	byte_arr = io.BytesIO()
	img.save(byte_arr, format='PNG')
	
	with open('test2.jpg', 'ab') as f:
		f.write(byte_arr.getvalue())

def readimg():
	with open('test2.jpg', 'rb') as f:
		content = f.read()
		offset = content.index(bytes.fromhex('FFD9')) 
		
		f.seek(offset + 2)
		new_img  = PIL.Image.open(io.BytesIO(f.read()))
		new_img.save('new image.png')
		
#print('test image start..')
#a = input()
#writeimg()
#b = input()
#readimg()
#print('success..')