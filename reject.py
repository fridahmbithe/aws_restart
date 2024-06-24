def monday_greeting(name):
    return ("hello goodmorning {}, rrrreject".format(name))
    # return f"hello goodmorning, {name} rrreject"
names = ["mary", "mercy", "Fridah"]
for name in names:
    print(monday_greeting(name))

# define
def test_function(x,y):
    print(f"this is the function {x} and {y}")

# calling the function
test_function("cat","dog")

