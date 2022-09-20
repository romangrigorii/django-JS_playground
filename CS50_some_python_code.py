# how to use wrappers
# functonal programming - when functions themsevles are used as inputs
def announce(f):
    def wrapper():
        print("I am running this function")
        f()
        print("Done running the function")
    return wrapper  
@announce
def hel():
    print("hiiii")
hel()

# how to sort dictionaries based on a name
people = [
    {"name":"harry", "house":"gryffindor"},
    {"name":"cho", "house":"ravenclaw"},
    {"name":"draco", "house":"slytherin"},
]
def g(person):
    return person["name"]

people.sort(key = g)
print(people)

# how to sort dictionary based on values

adict = {"a": 3, "b":2, "c":1}
adict =dict(sorted(adict.items(), key = lambda x : x[1]))
print(adict)

# excepting based cases
def div(x,y):
    try: 
        return x/y
    except ValueError:
        return "HUH???"
    except:
        return "can't divide that"

print(div(1,"well"))