import base64

def image_to_base64(path):
    f=open(path,'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    f.close()
    return ls_f

def base64_to_image(str, name):
    imgdata=base64.b64decode(str)
    file=open('{}.jpg'.format(name),'wb')
    file.write(imgdata)
    file.close()


print(image_to_base64('96.UniqueBinarySearchTrees/UniqueBinarySearchTrees.png'))
