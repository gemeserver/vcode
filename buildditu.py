from PIL import Image
import numpy as np
import util

# 检查已存在的像素点颜色和新像素点颜色是否相同,如果相同,返回相同颜色像素点在数组中的位置,如果不同,返回-1
def replist(lpoint,point1):
    for i in range(len(lpoint)):
        if lpoint[i][0] == point1[0] and lpoint[i][1] == point1[1] and lpoint[i][2] == point1[2]:
            return i
    return -1


# 计算传入的像素点颜色数组,返回重复数最多的像素点颜色
def prosspoint(point):
    lpoint = []
    succ = 0
    # 判断每个坐标点颜色和已有坐标点颜色是否重复，如果重复则重复数加1，如果不重复则在已有颜色数组中新增该颜色
    for i in range(len(point)):
        res = replist(lpoint, point[i])
        if res == -1:
            lpoint = np.append(lpoint, np.append(point[i], 1))
            succ = succ+1
            lpoint = lpoint.reshape(succ, 4)
        else:
            lpoint[res][3] = lpoint[res][3]+1

    maxpoint = 0
    maxpointline = 0
    for i in range(len(lpoint)):
        if lpoint[i][3]>maxpoint:
            maxpoint=lpoint[i][3]
            maxpointline = i

    retpoint=[int(lpoint[maxpointline][0]), int(lpoint[maxpointline][1]), int(lpoint[maxpointline][2])]
    return retpoint


data = []
aa = util.file_name("hongye10/", ".jpg")
pinnum = len(aa)
for i in range(pinnum):
    lena = Image.open('hongye10/' + aa[i] + '.jpg')
    X_im1 = np.asarray(lena).copy()
    data = np.append(data, X_im1)

data = data.reshape(pinnum, 100*320, 3)
newpic = []
# 对读入的所有图片的所有像素点颜色进行判断，用重复数量最多的像素点颜色生成新的图像
for j in range(100*320):
    point = []
    for i in range(pinnum):
        point = np.append(point, data[i][j])

    point = point.reshape(pinnum, 3)
    point = prosspoint(point)
    newpic = np.append(newpic, point)

newpic = newpic.reshape(100, 320, 3)
new_im = util.MatrixToImage(newpic)
new_im.save('hongye10/ditu.bmp')

