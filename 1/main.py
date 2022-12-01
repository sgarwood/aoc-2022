
maximum_calories = 0
with open('input.txt') as f:
  calories = 0
  contents = f.readlines()
  for line in contents:
    if line == '\n':
      if calories > maximum_calories:
        print('new max found')
        maximum_calories = calories
      calories = 0
    else:
      calories += int(line)
print('max', maximum_calories)
