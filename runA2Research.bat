@echo off
setlocal enabledelayedexpansion

set tests=1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
set algos=nn dp ga

for %%a in (%algos%)do (
    if "%%a"=="nn" set algoName=Nearest Neighbor First
    if "%%a"=="dp" set algoName=Bitmask Dynamic Programming
    if "%%a"=="ga" set algoName=Genetic Algorithm

    echo.
    echo Testing !algoName!:
    echo -------------------------------------
    for %%i in (%tests%) do (
        python research.py Research/Test/test_%%i.txt %%a
        echo.
    )
    echo -------------------------------------
    pause
)