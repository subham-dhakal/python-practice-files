st=input("Enter here ")
d={}
def fun(st):
	for word in st.split(" "):
		d[word]=d.get(word,0)+1

	print(d)
	
fun(st)