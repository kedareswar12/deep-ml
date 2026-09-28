def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	
	if not a or not b or len(a[0]) != len(b):
		return -1

	vector_length = len(b)

	for row in a:
		if len(row) != vector_length :
			return -1

	result = []

	for row in a :
		row_sum =0
		for i in range(vector_length):
			row_sum += row[i] * b[i]

		result.append(row_sum)
	return result

	
	