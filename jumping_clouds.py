"""Choose the shorter path to the end avoiding 1 position."""
ar = [0, 1, 0, 0, 0, 1, 0]


def jumping_clouds(ar):
	jump_count = 0
	end = False
	index = 0
	while not end:
		if index
		if ar(index + 2) != 1:
			index += 2
		else:
			index += 1
		jump_count += 1

	for i in range(0, len(ar), 2):
		print ar[i]

print jumping_clouds(ar)
