from copy import deepcopy

data0 = [1,2,3,4]
data1 = [5,6,7,8]

print(f"list biasa = {data0}")

data2D = [data0, data1]

print(f"list 2D = {data2D}")

#contoh penggunaan
peserta0 = ["ucup", 25, "laki-laki"]
peserta1 = ["otong", 10, "laki-laki"]
peserta2 = ["dede", 20, "wanita"]

listPeserta = [peserta0, peserta1, peserta2]
print(f"list peserta = {listPeserta}")


for peserta in listPeserta:
    print(f"name\t = {peserta[0]}")
    print(f"umur\t = {peserta[1]}")
    print(f"gender\t = {peserta[2]}\n")


#by default python use pass by reference on list, so use copy to pass by value
#but for nested list, when we copy the wrapper, list inside the wrapper still pass by reference
listCopy = listPeserta.copy()
print(f"list copy = {listPeserta}")


#to copy nested list include with their component, use deepcopy
listDeepCopy = deepcopy(listPeserta)
