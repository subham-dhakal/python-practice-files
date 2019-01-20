'''
fw=open("filewrite.txt","w") #file write
fw.write("Hi i am subham")
fw.close()

fr=open("filewrite.txt","r")  #file read
print(fr.read())

fa=open("filewrite.txt","a")  #appending a file
fa.write(" and my hometown is biratchowk")
print(fa.tell())  #prints the current position of the cursor
fa.close()

with open("context_manager.txt","w") as w:
    w.write("This is the context manager in python")
  '''

l=["Hello\n","There\n"]
with open("append_from_loop.txt","w") as q:
    for i in l:
        q.write(i)

with open("append_from_loop.txt","r") as fread:    #It is not completed we should be able to print in new line
    print(fread.read())

rewrite="print('Hello world')"
with open("print.py","w") as py:
    py.write(rewrite)











