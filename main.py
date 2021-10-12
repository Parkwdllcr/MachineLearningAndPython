
import cv2
import numpy as np
import tensorflow as tf
img = cv2.imread(r"D:\picture\testpicture.jpg")    # 加载图片
cv2.namedWindow("cs")                                           # 创建一个窗口，名称cs
cv2.imshow("cs",img)                                            # 在窗口cs中显示图片
cv2.waitKey(10000)
cv2.destroyAllWindows()






