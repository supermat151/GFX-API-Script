@echo off
echo First argument: %1
cd C:\Program Files\Intel Corporation\DGDiagTool_Internal
DGDiagTool.exe -SYSTEM.UTIL.DGMonitor duration=172800 stime=1000 file=%1
