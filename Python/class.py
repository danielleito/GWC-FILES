"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

class Cat():
		#Constructor Method
	def __init__(self, furColor, cHeight, cWeight):
		self.furColor = furColor
		self.cHeight = cHeight
		self.cWeight = cWeight
		#Methods
	def purr(self):
		print("Purr")
	def meow(self):
		print("Meow")
	def returnFurcolor(self):
		return self.furColor
Mittens=Cat("GREY","85","15")
Mittens.purr()
Mittens.meow()	
	def __init__(self, furColor, cHeight, cWeight):
		self.furColor = furColor
		self.cHeight = cHeight
		self.cWeight = cWeight
		#Methods
	def purr(self):
		print("Purr")
	def meow(self):
		print("Meow")
	def returnFurcolor(self):
		return self.furColor
Rags=Cat("BLACK","70","20")
Rags.purr()
Rags.meow()	