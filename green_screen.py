# @author: Xavier Collantes

from PIL import Image
from PIL import ImageColor
import os, arrow

def greenScreen(bg, gs):
	# This operation takes a while, let's keep track with a timer 
	
	# Use Tableau to find green threshold value to be used below 
	p = 'green_values.csv'
	file = open(p, 'w+')
	file.write("Red, Green, Blue\n")
	
	# Establish counter for green screen image 
	WIDTH = gs.size[0] - 1
	HEIGHT = gs.size[1] - 1
	pos = (0, 0)
	try:
		# Stop when smallest dimension is reached on green screen image 
		while pos[0] <= WIDTH:
		
			while pos[1] <= HEIGHT:
				print("processing pixel: ", pos)

				if gs.getpixel(pos)[1] > 150:  # If pixel on green screen image is somewhat green 
					print("change pixel: ", pos)
					
					frontColor = bg.getpixel(pos)  # Get corresponding pixel color of the same coordinates 
					gs.putpixel(pos, frontColor)
				else:
					pass
				
				try:
					o = str(gs.getpixel(pos)[0]) + ", " + str(gs.getpixel(pos)[1]) + ", " + str(gs.getpixel(pos)[2]) + "\n"
					file.write(o)  # Output RGB values for analysis 
				except IOError as ioe:
					print("Error with file output %s" %ioe)
					
				pos = (pos[0], pos[1] + 1)  # Increment height by 1

			pos = (pos[0], 0)
			pos = (pos[0] + 1, pos[1])  # Increment width by 1
	except Exception as e:
		print("Iteration issue %s" %e)
		pass
	
	file.close()
	gs.save(arrow.now('US/Pacific').format('DD-MMM-YY_HH-mm-SS') + '.png')
	
if __name__=='__main__':
	os.chdir('lib/')
	
	back = Image.open('transpose_horizontal.png')
	shia = Image.open('shia.jpg')
	
	greenScreen(back, shia)
	