print(__import__('functools').reduce(lambda a, b: a + b, [(__import__('re').sub('[:\n]', '', i).split(' ')[2][int(__import__('re').sub('[:\n]', '', i).split(' ')[0].split('-')[0]) - 1] == __import__('re').sub('[:\n]', '', i).split(' ')[1]) ^ (__import__('re').sub('[:\n]', '', i).split(' ')[2][int(__import__('re').sub('[:\n]', '', i).split(' ')[0].split('-')[1]) - 1] == __import__('re').sub('[:\n]', '', i).split(' ')[1]) for i in open('input.txt')]))