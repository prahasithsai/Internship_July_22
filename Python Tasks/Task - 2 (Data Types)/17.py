# The Captain's Room
K = int(input())
room = input().split()
room.sort()
capt_room = set(room[0::2])^set(room[1::2])
print(capt_room.pop())