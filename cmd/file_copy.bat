@echo off
set source_file="C:\path\to\source.txt"
set destination_file="C:\path\to\destination.txt"
copy %source_file% %destination_file%


REM This is a comment
:: This is also a comment

@REM This is a batch script that copies the contents of a file from one location to another.

@REM The @echo off command is used to turn off the command prompt’s echoing of commands. This is done to make the output of the script cleaner and easier to read.

@REM The set command is used to set environment variables. In this case, it is used to set the source and destination file paths.

@REM The copy command is used to copy the contents of the source file to the destination file.