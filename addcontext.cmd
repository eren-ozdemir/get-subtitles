@echo off

REG ADD HKEY_CURRENT_USER\Software\Classes\Directory\Background\shell\Subtitles(Tr)\command   /d "\"C:\Program Files (x86)\Subtitles\Subtitles-tr.exe\""
REG ADD HKEY_CURRENT_USER\Software\Classes\Directory\Background\shell\Subtitles(En)\command   /d "\"C:\Program Files (x86)\Subtitles\Subtitles-en.exe\""
