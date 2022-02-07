def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig')as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None     # creating "person" to avoid when the chat doesn't start with a person
	new = []
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:     #if personn has a value, the next line runs
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open('filename', 'w') as f: 
		for line in lines:
			f.write(line + '\n')

def main():
	lines =  read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()

