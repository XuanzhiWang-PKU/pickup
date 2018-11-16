#!/usr/env/python2
# -*- encoding: UTF-8 -*-

import argparse
import sys
import time

import cv2
import numpy as np

import action
import almath
import imglib
import motion
from color_path import get_path
from naoqi import ALProxy

img_width = 320
img_height = 240
img_area = 76800

global motionProxy
global postureProxy
global camProxy
global tts
global client_name
global is_remote


def pickup(robotIP, PORT=9559):
    global camProxy
    global client_name

    pickBall = 10
    closetoballmid = 100
    closetoballbot = 210
    throwBall = 15
    closeToTarget = 1
    upCloseToTarget = 150
    downCloseToTarget = 170

    # 初始化机器人状态
    motionProxy.wakeUp()
    postureProxy.goToPosture('StandInit', 0.5)
    camProxy, client_name = imglib.init_camera(robotIP, PORT, 1)

    config = [["LeftStepHeight", 0.025],
              ["RightStepHeight", 0.03],
              ["LeftMaxStepX", 0.03],
              ["RightMaxStepX", 0.04]]

    joint_name = 'HeadPitch'
    angle_lists = 20 * almath.TO_RAD
    time_lists = 1.0
    is_absolute = True
    motionProxy.angleInterpolation(
        joint_name, angle_lists, time_lists, is_absolute)


    motionProxy.setMoveArmsEnabled(True, True)
    motionProxy.moveToward(0.6, 0, 0)
    time.sleep(3)

    # 找垃圾
    while True:
        img = imglib.get_image(camProxy, client_name)

        if is_remote:
            cv2.imshow('image', img)
            cv2.waitKey(1)
        
        yellow_pos = imglib.find_color_pos(img, get_path('laji'), display=is_remote)
        center_x = yellow_pos[0] + yellow_pos[2] / 2
        down_y = yellow_pos[1] + yellow_pos[3]

        if center_x < 0 or (130 - pickBall) < center_x < (130 + pickBall):
            print('Forward')
            motionProxy.moveToward(0.6, 0, 0)
        elif center_x < (130 - pickBall):
            print('front left')
            motionProxy.moveToward(0.3, 0, 0.07)
        elif center_x > (130 + pickBall):
            print('front right')
            motionProxy.moveToward(0.3, 0, -0.07)
        if down_y > closetoballbot:
            if (130 - pickBall) < center_x < (130 + pickBall):
                print('--------------------------------------stop-------------')
                motionProxy.moveToward(0, 0, 0)
                break
            elif center_x < (130 - pickBall):
                print('left')
                motionProxy.moveToward(0, 0.25, 0)
            elif center_x > (130 + pickBall):
                print('right')
                motionProxy.moveToward(0, -0.25, 0)

    motionProxy.setCollisionProtectionEnabled("Arms", False)
    if motionProxy.getCollosionProtectionEnabled == False:
        print('保护机制已关闭')
    # 捡垃圾
    action.pickUpBalls(motionProxy)
    
    camProxy.setActiveCamera(1)
    motionProxy.setMoveArmsEnabled(True, False)
    motionProxy.moveTo(0, 0, 0.1)
    motionProxy.moveToward(0, 0, 0)

    # 找垃圾桶
    while True:
        img = imglib.get_image(camProxy, client_name)

        dustbin_pos = imglib.find_color_pos(img, get_path('dustbin'), is_remote)
        down_y = dustbin_pos[1] + dustbin_pos[2]
        if down_y > downCloseToTarget:
            motionProxy.moveToward(0, 0, 0)
            break
        motionProxy.moveToward(0.4, 0, 0, config)
        print('Forward')

    # angle_lists = -10 * almath.TO_RAD
    motionProxy.angleInterpolation(
        joint_name, angle_lists, time_lists, is_absolute)

    # 找垃圾桶
    while True:
        img = imglib.get_image(camProxy, client_name)

        dustbin_pos = imglib.find_color_pos(img, get_path('dustbin'), is_remote)
        center_x = dustbin_pos[0] + dustbin_pos[2] / 2
        center_y = dustbin_pos[1] + dustbin_pos[3] / 2

        if center_x < 0 or (180 - throwBall) < center_x < (180 + throwBall):
            print('Forward')
            motionProxy.moveToward(0.4, 0, 0)
        elif center_x < (180 - throwBall):
            print('Forward left')
            motionProxy.moveToward(0.4, 0, 0.15, config)
        elif center_x > (180 + throwBall):
            print('Forward right')
            motionProxy.moveToward(0.4, 0, -0.15, config)
        if dustbin_pos[1] + dustbin_pos[3] > upCloseToTarget:
            if (180 - throwBall) < center_x < (180 + throwBall):
                motionProxy.moveToward(0, 0, 0)
                print('---------------------stop----------------------')
                break
            elif center_x < (180 - pickBall):
                print('left')
                motionProxy.moveToward(0, 0.5, 0)
            elif center_x > (180 + pickBall):
                print('right')
                motionProxy.moveToward(0, -0.5, 0)
    
    # 扔垃圾
    action.throwBall(motionProxy)

    postureProxy.goToPosture('StandInit', 0.5)
    motionProxy.rest()
    imglib.release_camera(camProxy, client_name)


if __name__ == "__main__":
    global is_remote
    global motionProxy
    global postureProxy
    global tts
    # global is_remote
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", '-i', type=str, default="10.0.0.11",
                        help="Robot ip address")
    parser.add_argument("--port", '-p', type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    if (args.ip == ('127.0.0.1' or 'localhost')) and args.port == 9559:
        is_remote = False
    else:
        is_remote = True
    
    try:
        motionProxy = ALProxy("ALMotion", args.ip, args.port)
        postureProxy = ALProxy("ALRobotPosture", args.ip, args.port)
        tts = ALProxy('ALTextToSpeech', args.ip, args.port)
    except:
        print("Could not create proxy")
        sys.exit(0)

    try:
        pickup(args.ip, args.port)
    except KeyboardInterrupt:
        postureProxy.goToPosture('StandInit', 0.5)
        motionProxy.rest()
