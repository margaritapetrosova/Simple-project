word1 = 'Smth'
featureVector1 = []
for letter in word1:
    featureVector1.append(ord(letter))
print(featureVector1)

word2 = 'Smth'
featureVector2 = []
for letter in word1:
    featureVector2.append(ord(letter))
print(featureVector2)

sum = 0
for num in range(len(word1)):
    res = (featureVector2[num] - featureVector1[num]) ** 2
    sum = res + sum
euc = (sum) ** 0.5

print(euc)