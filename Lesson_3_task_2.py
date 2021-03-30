x = 'Its such a wonderful life'
z = (len(x) // 2) + (len(x) % 2)
y = x[z:] + x[:z]
print(y)

