# -*- coding: utf-8 -*-
"""Yolov3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T8zGQGqWBglntGimhUyBbqZBSSaac5e0
"""

!git clone https://github.com/ultralytics/yolov3
!cd yolov3;pip install -qr requirements.txt

import torch
from IPython.display import Image, clear_output  # to display images

clear_output()
print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

# Commented out IPython magic to ensure Python compatibility.
# %cd yolov3
!python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov3.pt --nosave

!cd yolov3;python detect.py --weights yolov3.pt --img 640 --conf 0.25 --source data/images

from IPython.display import Image, clear_output 

Image(filename='/content/yolov3/runs/detect/exp/memory.jpg', width=600)

!mkdir /content/data
!wget -O /content/data/beatles01.jpg https://raw.githubusercontent.com/chulminkw/DLCV/master/data/image/beatles01.jpg

# 실행 디렉토리를 고정하고, 시각화시 bounding box line 두께를 조절
!cd yolov3;python detect.py --weights yolov3.pt --img 640 --conf 0.25 --source /content/data/beatles01.jpg  \
                            --project /content/data  --name=run_image --exist-ok --line-thickness 1

# Night_Day_Chase.mp4 영상 다운로드 하기
!wget -O /content/data/Night_Day_Chase.mp4 https://github.com/chulminkw/DLCV/blob/master/data/video/Night_Day_Chase.mp4?raw=true

# --project를 /content/data/run_video 로 설정하여 Detect된 영상을 저장.  
!cd yolov3;python detect.py --weights yolov3.pt --img 640 --conf 0.25 --source /content/data/Night_Day_Chase.mp4 \
                            --project=/content/data/run_video --exist-ok --line-thickness 1