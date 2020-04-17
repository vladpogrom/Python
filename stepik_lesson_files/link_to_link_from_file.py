import requests

def open_new_link(filename):
    x=0
    while filename[0:2] != "We":
        x+=1
        link = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + filename, 'r')
        filename = link.text
        print(str(x) + filename)
        if filename[0:2] == "We":
            break
            print(filename)
    return

link_for = open("dataset_3378_3.txt", 'r')
line_for = link_for.readline().strip()
r_for = requests.get(line_for)
filename = r_for.text
print("1 " + filename)

if filename[0:2] != "We":
    open_new_link(filename)
else:
    print("Finish" + filename)
    
    
