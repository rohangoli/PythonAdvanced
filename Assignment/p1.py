'''Reverse words in sentence. Input - " This is a reverse order sentence". Output - "sentence order reverse a is This"'''
x = "This is a reverse order sentence"
y=x.split()
print(' '.join(y[::-1]))
