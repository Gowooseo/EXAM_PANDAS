#(1)open
file=open('message.txt',encoding='utf8')
print(f'file=>{type(file)},{file}')

#(2) 읽기
datas=file.readlines()

print(datas)
#(3) 닫기
file.close

