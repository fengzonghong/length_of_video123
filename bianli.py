import csv
import os
from os import path
import cv2

framenum=[]
fps=[]
width=[]
height=[]

listFile = []
list_of_file = []

for root,dirs,files in os.walk("Y:\【素材成品】\港台官人"):
 for dir in dirs:
  os.path.join(root,dir).encode('utf-8').decode('utf-8');
 for file in files:
  listFile.append(os.path.join(root,file).encode('utf-8').decode('utf-8')) ;
  list_of_file.append(file)

print(listFile)
for name in listFile:
    cap=cv2.VideoCapture(name)
    print(name)
    framenum.append(cap.get(7)) # 读取帧数
    fps.append(cap.get(5)) # 读取帧率
    height.append(cap.get(4)) # 读取高度
    width.append(cap.get(3)) # 读取宽度

f=open('C:\\Users\\HY-notebook-001\\Desktop\素材\\广告长度.csv','w', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['文件名','视频尺寸','广告长度'])
for i in range(len(framenum)):
  csv_writer.writerow([list_of_file[i],str(int(width[i]))+'x'+str(int(height[i])),str(int(framenum[i]/fps[i])) if fps[i]>0 else "0"])

