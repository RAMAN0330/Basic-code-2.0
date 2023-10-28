exis_data = open("file1.txt","r")
gener_data = open("file2.txt","w")

file1 = exis_data.read().split("\n")
for i in range(len(file1)):
    file1[i]= file1[i].split(".")

data = []
for sen in file1:
    for j in range(len(sen)):
        data.append(sen[j])
        
savable = []
for i in data:
    if "but" in i or "But" in i:
        if "butter" in i or "Butter" in i:
            pass
        else:
            print(i)
            savable.append(i)
            
savable = ".".join(savable)

gener_data.write(savable)

exis_data.close()
gener_data.close()