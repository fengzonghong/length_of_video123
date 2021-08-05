import os
from os import path
import cv2



path='Y:\\【素材成品】\\港台官人\\Fb&谷歌\\视频\\2021年7月'
videoList = os.listdir(path)
print(videoList)
framenum=[]
fps=[]
width=[]
height=[]


for name in videoList:
    cap=cv2.VideoCapture(path+'/'+name)
    framenum.append(cap.get(7)) # 读取帧数
    fps.append(cap.get(5)) # 读取帧率
    height.append(cap.get(4)) # 读取高度
    width.append(cap.get(3)) # 读取宽度
f=open('C:\\Users\\HY-notebook-001\\Desktop\素材\\framenum.txt','w')

for i in range(len(framenum)):
  f.write('\t'+videoList[i]+'\t'+str(width[i])+'x'+str(height[i])+'\t'+str(framenum[i])+'\t'+str(fps[i])+'\n')

  ## Y:\【素材成品】\港台官人\Fb&谷歌\视频