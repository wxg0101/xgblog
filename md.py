import os
from datetime import datetime
import argparse
import time

datetime.now().strftime('%Y-%m-%d')
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name",type=str,required=True,help="文件名")
    args=parser.parse_args()
    return args

if __name__=="__main__":
    args=get_args()
    filename = datetime.now().strftime('%Y-%m-%d')+"-"+args.name+".md"
    filename = os.path.join('D:\\OneDrive365\Desktop\\xgblog\\_posts', filename)
    f =  open(filename, "w",encoding='utf-8')
    f.write(
        f"""---
layout: post                    # 使用的布局（不需要改）
title: "{args.name}"              # 标题 
subtitle: Hello World, Hello Blog #副标题
date: {datetime.now().strftime('%Y-%m-%d')}             # 时间
author: Leowxg                      # 作者
header-img: img/post-bg-2015.jpg    #这篇文章标题背景图片
catalog: true                       # 是否归档
tags:                               #标签
    - 教程
---

## Hey
>这是我的第一篇博客。

进入你的博客主页，新的文章将会出现在你的主页上.

 <!--more-->
        """
        )
    f.close()
    time.sleep(3)
    os.system('D:\\"Program Files (x86)"\Typora\\typora.exe {}'.format(
        filename))