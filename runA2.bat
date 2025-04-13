@echo off
setlocal enabledelayedexpansion

set tests=1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
set algos=cus2

for %%a in (%algos%)do (
    if "%%a"=="bfs" set algoName=Breadth-First Search
    if "%%a"=="dfs" set algoName=Depth-First Search
    if "%%a"=="gbfs" set algoName=Greedy Best-First Search
    if "%%a"=="as" set algoName=A*
    if "%%a"=="cus1" set algoName=CUS1 ^(Dijkstra^)
    if "%%a"=="cus2" set algoName=CUS2 ^(Ant Colony Optimisation^)

    echo.
    echo Testing !algoName!:
    echo -------------------------------------
    for %%i in (%tests%) do (
        python search.py Test/test_%%i.txt %%a
        echo.
    )
    echo -------------------------------------
    pause
)