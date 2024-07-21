@echo off
setlocal enabledelayedexpansion

REM Prompt user to enter the drive letter (e.g., E:) of the USB/Drive to overwrite
set /p drive_letter=Enter drive letter (e.g., E:) of the drive to overwrite: 

REM Verify that the drive letter provided exists
if not exist "%drive_letter%\" (
    echo Drive %drive_letter% does not exist or is not accessible.
    exit /b 1
)

REM Prompt user for confirmation
set /p confirm=WARNING: This will irreversibly overwrite all data on %drive_letter%. Proceed? (yes/no): 

if /i "%confirm%"=="yes" (
    echo Overwriting drive %drive_letter% with random data...

    REM Calculate size of the drive in bytes
    for /f "usebackq tokens=3" %%a in (`dir "%drive_letter%\" ^| findstr "bytes free"`) do set free_bytes=%%a
    set /a free_bytes=!free_bytes:,=!

    REM Triple pass overwriting with random data (1s and 0s)
    echo Filling %drive_letter% with random data (Pass 1)...
    for /l %%i in (1,1,1000) do (
        echo 01100110101001010101101010101101 > "%drive_letter%\pass1_%%i.txt"
    )

    echo Filling %drive_letter% with random data (Pass 2)...
    for /l %%i in (1,1,1000) do (
        echo 01100110101001010101101010101101 > "%drive_letter%\pass2_%%i.txt"
    )

    echo Filling %drive_letter% with random data (Pass 3)...
    for /l %%i in (1,1,1000) do (
        echo 01100110101001010101101010101101 > "%drive_letter%\pass3_%%i.txt"
    )

    echo Overwriting complete.

) else (
    echo Operation cancelled.
    exit /b 0
)
