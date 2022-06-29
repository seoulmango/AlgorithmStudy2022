# ord() 함수는 str을 10진수의 유니코드로 변환시켜준다.
# chr() 함수는 int을 유니코드 문자로 변환시켜준다.

print(ord('A'))
# >>> 65
print(chr(65))
# >>> A


for i in range(65, 91):
	print(chr(i))
# >>> A ~ Z까지 순차적으로 
for i in range(91, 117):
	print(chr(i))