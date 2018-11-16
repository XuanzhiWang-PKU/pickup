# -*- encoding: UTF-8 -*-
import cv2
import numpy as np
import vision_definitions
import argparse
import time
import almath
import motion

from naoqi import ALProxy
from naoqi import ALModule


def find_color(img, xml_name='yellow.xml'):
    '''
    通过输入的xml文件搜索指定颜色\n
    返回二值图
    '''
    svm = cv2.ml.SVM_load(xml_name)
    img_data = cv2.medianBlur(img, 15)
    img_data = np.reshape(img, (img.shape[0] * img.shape[1], 3))
    img_data = np.float32(img_data)
    result = svm.predict(img_data)[1]
    result = np.uint8(result)

    result = np.reshape(result, [img.shape[0], img.shape[1], 1])
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 17))
    result = cv2.morphologyEx(result, cv2.MORPH_ELLIPSE, element)
    result = cv2.bitwise_not(result)
    return result


def find_color_pos(img, xml_name='yellow.xml', display=False):
    '''
    通过输入的xml文件搜索指定颜色，返回面积最大的矩形\n
    矩形四个值分别为x, y, width, height\n
    若没有矩形，则返回(-1, -1, -1, -1)
    '''
    bin_img = find_color(img, xml_name)
    contours = cv2.findContours(
        bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    results = []
    for c in contours[1]:
        rect = cv2.boundingRect(c)
        # print(rect[0], rect[1], rect[2], rect[3])
        if rect[1] != 0 and (rect[0] == 0 or rect[0] + rect[2] == img.shape[1] - 5):
            # cv2.drawContours(bin_img, c, -1, (0), -1)
            continue
        if (rect[1] + rect[3] == img.shape[0] - 5) or (rect[1] > 0.9 * img.shape[0]):
            # cv2.drawContours(bin_img, c, -1, (0), -1)
            print(2)
            continue
        if rect[2] * rect[3] < 100:
            # cv2.drawContours(bin_img, c, -1, (0), -1)
            continue
        cv2.rectangle(bin_img, (rect[0], rect[1]),
                      (rect[0] + rect[2], rect[1] + rect[3]), (255))
        results.append(rect)
        # print('got')

    if display:
        cv2.imshow('image', img)
        cv2.imshow('bin', bin_img)
        cv2.waitKey(1)
    
    areas = [c[2] * c[3] for c in results]
    if areas:
        return results[areas.index(max(areas))]
    else:
        return (-1, -1, -1, -1)

def find_laji_pos(img, xml_name='yellow.xml', display=False):
    '''
    通过输入的xml文件搜索指定颜色，返回面积最大的矩形\n
    矩形四个值分别为x, y, width, height\n
    若没有矩形，则返回(-1, -1, -1, -1)
    '''
    bin_img = find_color(img, xml_name)
    contours = cv2.findContours(
        bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(bin_img, contours[1], -1, (100))
    results = []
    for c in contours[1]:
        rect = cv2.boundingRect(c)
        if rect[0] > 0.8 * img.shape[1] or rect[0] < 0.2 * img.shape[1]:
            # cv2.drawContours(bin_img, c, -1, (0), -1)
            # continue
            pass
        cv2.rectangle(bin_img, (rect[0], rect[1]),
                      (rect[0] + rect[2], rect[1] + rect[3]), (255))
        results.append(rect)

    if display:
        cv2.imshow('image', img)
        cv2.imshow('bin', bin_img)
        cv2.waitKey(1)
    
    areas = [c[2] * c[3] for c in results]
    if areas:
        return results[areas.index(max(areas))]
    else:
        return (-1, -1, -1, -1)


def init_camera(robotIP, PORT=9559, camera_idx=0):
    '''
    初始化机器人的摄像头，默认分辨率320x240，关闭自动白平衡\n
    返回camProxy, client_name
    '''
    try:
        camProxy = ALProxy("ALVideoDevice", robotIP, PORT)
    except Exception, e:
        print("could not creat proxy to ALVideoDeviceProxy")
        print("error was:", e)
    camProxy.setActiveCamera(camera_idx)
    resolution = vision_definitions.kQVGA
    colorSpace = vision_definitions.kBGRColorSpace
    client_name = camProxy.subscribe("camera", resolution, colorSpace, 10)
    camProxy.setParameter(camera_idx, 12, 0)
    return camProxy, client_name


def release_camera(camProxy, client_name):
    camProxy.unsubscribe(client_name)


def get_image(camProxy, client_name):
    '''
    从机器人摄像头获取一张BGR图像\n
    '''
    img = camProxy.getImageRemote(client_name)
    imagHeader = map(ord, img[6])
    camProxy.releaseImage(client_name)
    imagHeader = np.reshape(imagHeader, [240, 320, 3])
    return np.uint8(imagHeader)


def show_image(robotIP, PORT=9559):
    try:
        motionProxy = ALProxy("ALMotion", robotIP, PORT)
        postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    except:
        print("could not creat proxy")

    motionProxy.wakeUp()
    postureProxy.goToPosture("StandInit", 0.5)

    camProxy, client_name = init_camera(robotIP)

    index = 0
    while True:
        img = get_image(camProxy, client_name)
        cv2.imshow("capture-image", img)
        key = cv2.waitKey(1) & 255
        if key == ord('s'):
            cv2.imwrite('img{}.jpg'.format(index), img)
            index += 1
        elif key == 27:
            break

    motionProxy.stopMove()
    release_camera(camProxy, client_name)


def test_svm():
    img = cv2.imread('eight.jpg')
    result = find_color_pos(img, 'red.xml')
    cv2.imshow('result', result)
    cv2.waitKey(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot's ip address")
    parser.add_argument(
        "--port",
        type=int,
        default=9559,
        help="Robot port number"
    )
    args = parser.parse_args()

    # show_image(args.ip, args.port)
    test_svm()
