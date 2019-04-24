"""Counting pairs of numbers in one array."""

ar = [1, 2, 1, 1, 2, 2, 3, 3, 8, 9, 9, 9, 9]


def count_pairs(ar):
	"""Count total pairs of values y ar."""
	checked_values = []
	res = 0
	for value in ar:
		if value not in checked_values:
			checked_values.append(value)
			count = ar.count(value)
			if count >= 2:
				res += count / 2
	return res

print ar
print count_pairs(ar)
