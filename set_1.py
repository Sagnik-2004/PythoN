wr= {"abc","def",45, 24.78}
print(wr)
wr.remove("def")
print(type(wr))
print(wr)
wr.add("wsr")
print(wr)
wr.remove("wsr")
print(wr)
wr.add("def")
print(wr)

qw = {"(": ")", "{": "}", "[": "]"}
print(qw," ", type(qw))
for i in range(4):
	symb = input()
	if symb in qw:
		print(symb)
