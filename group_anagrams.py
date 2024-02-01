
from collections import defaultdict
Input= ["eat", "tea", "tan", "ate", "nat", "bat"]
print("The original list : " + str(Input))
temp=defaultdict(list)
for i in Input:
	temp[str(sorted(i))].append(i)
Output = list(temp.values())
print("The grouped Anagrams : " + str(Output))




 