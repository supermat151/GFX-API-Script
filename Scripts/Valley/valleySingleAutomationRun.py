#!/usr/bin/env python
#coding=utf-8

import valley_automation # type: ignore
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Run Unigine Valley benchmark with specified settings.')
parser.add_argument('--api', type=str, default='GL', help='API to use (e.g., DX9, DX11, GL)')
parser.add_argument('--fullscreen', type=int, default=1, help='Fullscreen mode (0 or 1)')
parser.add_argument('--aa', type=int, default=8, help='Anti-aliasing level; 0, 2, 4, 8')
parser.add_argument('--width', type=int, default=3840, help='Resolution width')
parser.add_argument('--height', type=int, default=2160, help='Resolution height')
parser.add_argument('--quality', type=str, default='ULTRA', help='Quality setting; low, medium, high, ultra')
parser.add_argument('--log', type=str, default='UnigineValley.csv', help='Log file name')
parser.add_argument('--log_caption', type=str, default='FPS,Resolution,AA,Video Card Info,API,Score,Quality', help='Log caption')
parser.add_argument('--log_format', type=str, default='$F,$v,$m,$g,$A,$S,$quality', help='Log format')

args = parser.parse_args()

valley_automation.run(\
    api = args.api,\
    fullscreen = args.fullscreen,\
    aa = args.aa,\
    width = args.width,\
    height = args.height,\
    quality = args.quality,\
    log = args.log,\
    log_caption = args.log_caption,\
    log_format = args.log_format\
)
