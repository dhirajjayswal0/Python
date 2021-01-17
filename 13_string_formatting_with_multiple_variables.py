name = input("Enter your name:")
surname = input("Enter your surname:")
when = "today"

message1 = "Hello %s %s" % (name, surname)
message2 = f"Hello {name} {surname} what's up {when}."
print(message1)
print(message2)