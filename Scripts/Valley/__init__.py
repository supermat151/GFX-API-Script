#!/usr/bin/env python
#coding=utf-8

# Copyright (C) 2013, Unigine Corp. All rights reserved.
#
# File:    __init__.py
# Desc:    Valley automation core
# Version: 1.01
# Authors: Anna Chaplinskaya <anna@unigine.com>
#          Denis Shergin <binstream@unigine.com>
#
# This file is part of the Valley benchmark Advanced/Pro
# http://unigine.com/products/valley/pro/

import os
import platform
import string

engine_project = 'Valley'

def run(\
	api = 'DX9',\
	fullscreen = 1,\
	aa = 0,\
	width = 1280,\
	height = 720,\
	quality = 'ULTRA',\
	frame_number = -1,\
	number_of_frames = 0,\
	applevel = 0,\
	driver_type = 0,\
	feature_level = 0,\
	driver_debug = 0,\
	log = '',\
	log_caption = '',\
	log_format = '',\
	temperature_log = '',\
	frequency_log = '',\
	frames_log = '',\
	step = 0\
	):
	""" Starts Valley benchmark with custom parameters.
	
	parameters:
	api: DX9, DX11, GL (case-insensitive)
	fullscreen: 0, 1
	aa: 0, 2, 4, 8
	width: integer value (in pixels)
	height: integer value (in pixels)
	quality: LOW, MEDIUM, HIGH, ULTRA (case-insensitive)
	frame_number: frame number. If not -1, benchmark run in one-frame-rendering mode
	number_of_frames: iterations number for one-frame-rendering mode
	applevel: if 1, benchmark run with AppLevel plugin
	driver_type: driver type for render mode
	feature_level: feature level for render mode
	driver_debug: Debug DX: 0, 1
	log: log file name (can contain subfolders), set to '' to omit
	log_caption: comma-separated log file caption
	log_format: see user manual for info on placeholders
	temperature_log: temperature log file name
	frequency_log: frequency log file name
	frames_log: frames log file name
	step: step for logging temperature, frequency and frames (in seconds)
	
	"""
	
	# set path to the valley binary
	system = platform.system()
	app = 'valley'
	path = '..' + os.sep + 'bin' + os.sep
	if system == 'Linux':
		old_ld_path = ''
		if os.environ.get('LD_LIBRARY_PATH') != None:
			old_ld_path = os.environ['LD_LIBRARY_PATH']
		os.environ['LD_LIBRARY_PATH'] = os.path.abspath(path) + ':' + old_ld_path
		arch = '_x86'
		if platform.architecture()[0] == '64bit':
			arch = '_x64'
		extension = ''
	elif system == 'Darwin':
		arch = '_x32'
		if platform.architecture()[0] == '64bit':
			arch = '_x64' 
		path = '..' + os.sep + 'MacOS' + os.sep
		extension = '.macos'
	elif system == 'Windows':
		arch = ''
		extension = '.exe'
	executable = path + app + arch + extension
	
	# translate script params into engine ones
	if system == 'Linux' or system == 'Darwin':
		print("OpenGL is used")
		engine_api = 'opengl'
	else:
		engine_api = api.upper()
		if api == 'GL': engine_api = 'opengl'
		elif api == 'DX11': engine_api = 'direct3d11'
		elif api == 'DX9': engine_api = 'direct3d9'
	
	engine_aa = 0
	if aa == 2: engine_aa = 1
	elif aa == 4: engine_aa = 2
	elif aa == 8: engine_aa = 3
	
	extern_plugin = '-extern_plugin "GPUMonitor"'
	
	debug_parameter = ''
	if applevel == 1:
		extern_plugin = extern_plugin + ',"AppLevel"'
		if driver_debug == 1: debug_parameter = '-debug'
	
	engine_define = '-extern_define RELEASE,VALLEY_ADV,AUTOMATION'
	
	engine_define += ',QUALITY_' + quality.upper()
	
	if frame_number > -1: engine_define = engine_define + ',FRAME'
	
	if log_caption == '': engine_log_caption = 'FPS,API,Resolution,AA,Quality,Video,CPU'
	else: engine_log_caption = log_caption
	
	if log_format == '': engine_log_format = '$F,$A,$v,$m,$quality,$g,$c'
	else: engine_log_format = log_format
	
	engine_log_format = str.replace(engine_log_format,'$quality',quality)
	
	if system == 'Linux' or system == 'Darwin':
		engine_log_format = str.replace(engine_log_format,'$','\$')
	
	deep_analysis_params = ''
	
	if temperature_log != '':
		temperature_log = full_log_path(temperature_log)
		deep_analysis_params = '-temperature ' + str(temperature_log)
	
	if frequency_log != '':
		frequency_log = full_log_path(frequency_log)
		deep_analysis_params = deep_analysis_params + ' -frequency ' + str(frequency_log)
	
	if frames_log != '':
		frames_log = full_log_path(frames_log)
		deep_analysis_params = deep_analysis_params + ' -frames ' + str(frames_log)
	
	if step != 0:
		deep_analysis_params = deep_analysis_params + ' -step ' + str(step)
	
	# console command to run
	command = executable\
			+ ' -video_app ' + engine_api\
			+ ' -sound_app openal'\
			+ ' -project_name "' + engine_project + '"'\
			+ ' -data_path ../'\
			+ ' -system_script valley/unigine.cpp'\
			+ ' -engine_config ../data/valley_1.0.cfg'\
			+ ' -video_multisample ' + str(engine_aa)\
			+ ' -video_fullscreen ' + str(fullscreen)\
			+ ' -video_mode -1'\
			+ ' -video_width ' + str(width)\
			+ ' -video_height ' + str(height)\
			+ ' -frame ' + str(frame_number)\
			+ ' -duration ' + str(number_of_frames)\
			+ ' -type ' + str(driver_type).lower()\
			+ ' -level ' + str(feature_level).lower()\
			+ ' ' + debug_parameter\
			+ ' ' + deep_analysis_params\
			+ ' ' + extern_plugin\
			+ ' ' + engine_define
	
	# create log file if requested
	if log != '':
		log = full_log_path(log)
		if not os.path.isfile(log):
			result_file = open(log,'w+')
			result_file.write(engine_log_caption + '\n')
			result_file.close()
		tmp_log = log + '.tmp'
		command = command + ' -scores "' + tmp_log + '" -format "' + engine_log_format + '"'
	
	# run the benchmark with given params
	os.system(command)
	
	# write results to the log file
	if log != '' and os.path.isfile(tmp_log):
		tmp_file = open(tmp_log,'r')
		tmp_data = tmp_file.read()
		tmp_file.close()
		result_file = open(log,'a+')
		result_file.write(tmp_data + '\n')
		result_file.close()
		os.remove(tmp_log)
	
def full_log_path(file_name = ''):
	""" Defines full path for log file """
	
	# we can write into user dir only
	path = os.path.expanduser('~') + os.sep + engine_project + os.sep + 'reports' + os.sep + file_name
	dir = os.path.dirname(path)
	if not os.path.exists(dir):
		os.makedirs(dir)
	return os.path.normpath(path)
