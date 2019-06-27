"""
Counting valleys.

A mountain is a sequence of consecutive steps above sea level,
starting with a step up from sea level and ending with a step down
to sea level.

A valley is a sequence of consecutive steps below sea level,
starting with a step down from sea level and ending with a step
up to sea level.

"""
steps = 'UDDDUDUU'


def count_valleys(steps):
	"""Sum 1 when step U. Rest 1 when step D."""
	sea_level = 0
	valley_count = 0
	for step in steps:
		if step == 'U':
			sea_level += 1
		else:
			sea_level -= 1
		if sea_level == 0 and step == 'U':
			valley_count += 1
		print 'step: {} sea level: {} valley count: {}'.format(step, sea_level, valley_count)
	return valley_count


print 'Valley count: {}'.format(count_valleys(steps))
