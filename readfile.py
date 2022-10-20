handle = open("test.txt","r")

data = handle.read()
# data = handle.readline()
# data = handle.readlines()


count = 0
for word in data.split():
    if word == 'Python':
        count += 1

# print(data)
print(count)

handle.close()

print('----------------------------------------------------------')

with open("test.txt","r") as handle:
    data = handle.read()
    print(data)

print('--------------------------------------------------------------')

text_file = "test.txt"
def read_file(text_file):
    try:
        with open(text_file,"r") as handle:

            data = handle.read()
            return data
    except FileNotFoundError: return None