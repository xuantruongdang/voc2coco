import os 
import random
random.sample(range(100), 10)

all_files = os.listdir("vehicles/xml_files")
all_files.sort()

# split train test
train_files = all_files.copy()
val_files = random.sample(all_files, 100)
for item in  val_files:
    train_files.remove(item)
train_files.sort()
val_files.sort()
print("train_files: ",len(train_files))
print("val_files: ", len(val_files))

file = open(os.path.join('vehicles/img_ids', 'train.txt'), "w")
for item in train_files:
    item = item.rstrip(".xml")
    if item == train_files[-1].rstrip(".xml"):
        file.writelines(item)
    else:
        file.writelines([item, "\n"])
file.close()

file = open(os.path.join('vehicles/img_ids', 'val.txt'), "w")
for item in val_files:
    item = item.rstrip(".xml")
    if item == val_files[-1].rstrip(".xml"):
        file.writelines(item)
    else:
        file.writelines([item, "\n"])
file.close()