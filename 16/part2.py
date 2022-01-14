class PacketStream():
	def __init__(self, raw):
		self.string = bin(int("1" + raw, 16))[3:]
		self.offset = 0
		
	def ReadBits(self, n):
		result = int(self.string[self.offset : self.offset+n], 2)
		self.offset += n
		return result
		
	def ParsePacket(self):
		version = self.ReadBits(3)
		typeID = self.ReadBits(3)

		if (typeID == 4):
			num = ""
			more = True
			while more:
				more = self.ReadBits(1) == 1
				num += self.string[self.offset : self.offset+4]
				self.offset += 4
			return int(num, 2)
		else:
			lengthTypeID = self.ReadBits(1)
			vals = []
			if (lengthTypeID == 0): # next 15 bits represents the total length of the sub-packets
				length = self.ReadBits(15)
				length += self.offset
				while self.offset < length:
					vals.append(self.ParsePacket())
			
			else: # next 11 bits represents the number of sub-packets
				count = self.ReadBits(11)
				for _ in range(count):
					vals.append(self.ParsePacket())
					
			if (typeID == 0):
				return sum(vals)
			elif (typeID == 1):
				retval = 1
				for num in vals:
					retval *= num
				return retval
			elif (typeID == 2):
				return min(vals)
			elif (typeID == 3):
				return max(vals)
			elif (typeID == 5):
				return 1 if vals[0] > vals[1] else 0
			elif (typeID == 6):
				return 1 if vals[0] < vals[1] else 0
			elif (typeID == 7):
				return 1 if vals[0] == vals[1] else 0
			
file = open("input.txt")
stream = PacketStream(file.readline())
print("The result of evaluating the expression is:", stream.ParsePacket())