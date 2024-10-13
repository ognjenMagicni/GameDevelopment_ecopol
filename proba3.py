def fun():
    a = 5
    def fun1():
        global a
        a=6
    fun1()
    print(a)
fun()

b = 5
def fun():
    global b
    b=6
fun()
print(b)




