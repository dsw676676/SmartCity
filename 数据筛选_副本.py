#遍历文件，获得文件名列表
import pandas as pd
import os
import glob

folder =  r"D:\学校\凉山州项目\轨迹和足迹数据"    #输入地址
datadirs = []

for root,dirs,files in os.walk(folder, topdown=True):
    for name in dirs:
        sigdir = os.path.join(root,name)
        
        pt = glob.glob(sigdir + r'\*footprints*.shp')
        datadirs.append(pt)

from itertools import chain

obj = chain.from_iterable(datadirs)
ls = list(obj)

#筛选
for a,i in enumerate(ls):
    print(i)
    track = gpd.read_file(i)
    dt = track.merge(track_zj,on = 'tripid')
    if dt.crs is None:
        dt = dt.set_crs(epsg = 4326)
    else:
        dt = dt.to_crs(epsg = 4326)
    
    dt_yucy = gpd.overlay(dt,pl_yucy,how = 'intersection',keep_geom_type=False)
    track = gpd.sjoin(dt_yucy,pl_lsz,op = 'intersects')
    track = track[['tripid', 'location', 'title', 'triptime', 'triptype', 'geometry']]
    if track.empty is True:
        continue
    else:
        track.to_file(r'D:\学校\凉山州项目\自驾车轨迹\track_zj_ '+str(a)+'.shp',encoding = 'utf-8')