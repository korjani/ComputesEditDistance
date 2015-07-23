import sys

def is_vowel(c):
	return (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u') or (c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U')

res = []

def solve(str1, str2):
	len1, len2 = len(str1), len(str2)
	res.append([])
	for j in range(len2 + 1):
		res[0].append(2 * j)
	for i_ in range (len1):
		i = i_ + 1
		res.append([])
		res[i].append(3 * i)
	for i_ in range (len1):
		for j_ in range(len2):
			i = i_ + 1
			j = j_ + 1
			if str1[i - 1] == str2[j - 1]:
				res[i].append(res[i - 1][j - 1])
			else:
				temp = min(res[i - 1][j] + 3, res[i][j - 1] + 2)
				temp_sub = res[i - 1][j - 1]
				if is_vowel(str1[i - 1]) and is_vowel(str2[j -1]):
					temp_sub = temp_sub + 0.5
				else:
					temp_sub = temp_sub + 1
				res[i].append(min(temp, temp_sub))
	print 'Edit distance: ', res[len1][len2]

def print_all_seq(i, j, cur_seq, str1, str2):
	if i == 0 and j == 0:
		for move in reversed(cur_seq):
			if move[0] == 0:
				print 'Insert character ', move[2], ' at position ', move[1]
			if move[0] == 1:
				print 'Delete character ', move[2], ' at position ', move[1]
			if move[0] == 2:
				print 'Replace character from position ', move[1], ' with character ', move[2]
		print '--------'
		return
	if i == 0:
		cur_seq.append([1, j - 1, str2[j - 1]])
		print_all_seq(i, j - 1, cur_seq, str1, str2)
		cur_seq.pop()
		return
	if j == 0:
		cur_seq.append([0, 0, str1[i - 1]])
		print_all_seq(i - 1, j, cur_seq, str1, str2)
		cur_seq.pop()
		return
	if str1[i - 1] == str2[j - 1]:
		print_all_seq(i - 1, j - 1, cur_seq, str1, str2)
		return
	if res[i][j] == res[i - 1][j] + 3:
		cur_seq.append([0, j, str1[i - 1]])
		print_all_seq(i - 1, j, cur_seq, str1, str2)
		cur_seq.pop()
	if res[i][j] == res[i][j - 1] + 2:
		cur_seq.append([1, j - 1, str2[ j - 1]])
		print_all_seq(i, j - 1, cur_seq, str1, str2)
		cur_seq.pop()
	if is_vowel(str1[i - 1]) and is_vowel(str2[j -1]):
		if res[i][j] == res[i - 1][j - 1] + 0.5:
			cur_seq.append([2, j - 1, str1[i - 1]])
			print_all_seq(i - 1, j - 1, cur_seq, str1, str2)
			cur_seq.pop()
	else:
		if res[i][j] == res[i - 1][j - 1] + 1:
			cur_seq.append([2, j - 1, str1[i - 1]])
			print_all_seq(i - 1, j - 1, cur_seq, str1, str2)
			cur_seq.pop()
	return

def main():
  if len(sys.argv) != 3:
    print 'usage: ./SDL_problem1.py file'
    sys.exit(1)

  st1 = sys.argv[1]
  st2 = sys.argv[2]
  solve(st1, st2)
  print_all_seq(len(st1), len(st2), [], st1, st2)
  
if __name__ == '__main__':
  main()
