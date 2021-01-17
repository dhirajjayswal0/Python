def foo(name):
    return "Hi %s" % name.capitalize()

user = input("Enter your name: ")
print(foo(user))