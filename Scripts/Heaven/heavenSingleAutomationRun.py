#!/usr/bin/env python
#coding=utf-8

import heaven_automation # type: ignore
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Run Unigine Heaven benchmark with specified settings.')
parser.add_argument('--api', type=str, default='GL', help='API to use (e.g., DX9, DX11, GL)')
parser.add_argument('--fullscreen', type=int, default=1, help='Fullscreen mode (0 or 1)')
parser.add_argument('--aa', type=int, default=8, help='Anti-aliasing level; 0, 2, 4, 8')
parser.add_argument('--width', type=int, default=3840, help='Resolution width')
parser.add_argument('--height', type=int, default=2160, help='Resolution height')
parser.add_argument('--quality', type=str, default='ultra', help='Quality setting; low, medium , high , ultra')
parser.add_argument('--tessellation', type=str, default='extreme', help='Tessellation setting; disabled, moderate, normal, extreme')
parser.add_argument('--log', type=str, default='UnigineHeaven.csv', help='Log file name')
parser.add_argument('--log_caption', type=str, default='FPS,Resolution,AA,Video Card Info,API,Score,Tessellation,Quality', help='Log caption')
parser.add_argument('--log_format', type=str, default='$F,$v,$m,$g,$A,$S,$tessellation,$quality', help='Log format')

args = parser.parse_args()

# set number of iterations here!
iteration_number = 1

for i in range(iteration_number):
    heaven_automation.run(\
        api = args.api,\
        fullscreen = args.fullscreen,\
        aa = args.aa,\
        width = args.width,\
        height = args.height,\
        quality = args.quality,\
        tessellation = args.tessellation,\
        log = args.log,\
        log_caption = args.log_caption,\
        log_format = args.log_format\
    )
