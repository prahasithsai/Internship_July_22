# Find Angle MBC
AB = int(input())
BC = int(input())
import math
angle = math.atan(AB/BC)
angle_deg = round(math.degrees(angle))
print(angle_deg,chr(176),sep='')

