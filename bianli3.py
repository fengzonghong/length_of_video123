
# -*-coding:utf-8-*-
import os
listFile = []

for root,dirs,files in os.walk("Y:\【素材成品】\港台官人\Fb&谷歌\视频"):
 for dir in dirs:
  os.path.join(root,dir).encode('utf-8').decode('utf-8');
 for file in files:
  listFile.append(os.path.join(root,file).encode('utf-8').decode('utf-8')) ;


print(listFile)