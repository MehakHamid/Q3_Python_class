import random
#bytes
byte_data:bytes = b"Mehak"
print(byte_data)
print(byte_data[0])
print(byte_data[1])
print(byte_data[2])
print(byte_data[3])
print(byte_data[4])

# byte array
byte_array= bytearray([77,101,104,97,107])
print(byte_array)

# join method
pak_team=["fakhar zaman","sarfaraz","saim Ayub"]
print(", ".join(pak_team))

# split
message= "Hello world"
print(message.split())
print(message.split("\n"))

# replace
print(message.replace("world","Mehak"))

#list
print(pak_team[1:3])

# if else
bobzi_run=28
if (bobzi_run>100):
    print("win")
else:
    print("loss")

# random number
babar_run=random.randint(0,150)
babar_balls=random.randint(0,150)

if (babar_run>100 and babar_balls<babar_run):
    print("win")
else:
    print("loss")

# nested if else
num=6
if num>0:
    if num %2==0:
        print("even")
    else:
        print("odd")
else:
    print("negative")

# dictionery 
user1={
    "name":"mehak",
    "age":25,
    "is_student": True
}
print(user1["name"])
print(user1["age"])
print(user1["is_student"])

# tuple
# its immutable 

pak_team1=["fakhar zaman","sarfaraz","saim Ayub","rizwan"]
print(pak_team1)

# set 
pak_team2={"fakhar zaman","rizwan","sarfaraz","saim Ayub","rizwan"}
print(pak_team2)

