# 导入必要的库
import cv2
import paddleocr
import numpy as np


def recognize_license_plate(image):
    # 初始化车牌轮廓列表
    plate_contours = []

    # 创建中文OCR识别器实例
    ocr = paddleocr.PaddleOCR(lang="ch")

    # 图像预处理
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # 高斯模糊去噪
    edges = cv2.Canny(blurred, 50, 150)  # 边缘检测
    contours, _ = cv2.findContours(
        edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )  # 查找轮廓

    # 遍历所有轮廓，寻找可能的车牌区域
    for contour in contours:
        # 轮廓近似，简化轮廓形状
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        # 如果轮廓有4个顶点，可能是车牌
        if len(approx) == 4:
            plate_contours.append(contour)

    # 如果找到可能的车牌轮廓
    if plate_contours:
        # 选择最大的轮廓作为车牌区域
        plate_contour = max(plate_contours, key=cv2.contourArea)

        # 获取车牌区域的边界框
        x, y, w, h = cv2.boundingRect(plate_contour)
        plate_roi = image[y : y + h, x : x + w]  # 提取车牌区域图像
        result = ocr.ocr(plate_roi)  # 对车牌区域进行OCR识别

        # 提取识别结果中的文本
        for line in result:
            for item in line:
                text = item[1][0]
                return text

    # 如果未能识别出车牌，返回空值
    return None
