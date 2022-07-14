import colorama
colorama.init()

class ColorPrint:
	def __init__(self):
		pass

	def __getitem__(self, color: str):
		print(getattr(colorama.Fore, color.upper()), sep="", end="")
		return print
	
	def reset(self):
		print(colorama.Style.RESET_ALL)

ColorPrint.__call__ = print

crint = ColorPrint()

# class Building(object):
# 	def __init__(self, floors):
# 		self._floors = [None]*floors
# 	def __setitem__(self, floor_number, data):
# 		self._floors[floor_number] = data
# 	def __getitem__(self, floor_number):
# 		return self._floors[floor_number]

# building1 = Building(4) # Construct a building with 4 floors
# building1[0] = 'Reception'
# building1[1] = 'ABC Corp'
# building1[2] = 'DEF Inc'
# print( building1[2] )