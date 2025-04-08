@echo off

echo Testing BFS:
echo -------------------------------------
for %%i in (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17) do (
    python search.py Test/test_%%i.txt bfs
    echo.
)
echo -------------------------------------
pause

echo.
echo Testing DFS:
echo -------------------------------------
for %%i in (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17) do (
    python search.py Test/test_%%i.txt dfs
    echo.
)
echo -------------------------------------
pause

echo.
echo Testing GBFS:
echo -------------------------------------
for %%i in (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17) do (
    python search.py Test/test_%%i.txt gbfs
    echo.
)
echo -------------------------------------
pause

echo.
echo Testing A*:
echo -------------------------------------
for %%i in (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17) do (
    python search.py Test/test_%%i.txt as
    echo.
)
echo -------------------------------------
pause

echo.
echo Testing CUS1 (Dijkstra):
echo -------------------------------------
for %%i in (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17) do (
    python search.py Test/test_%%i.txt cus1
    echo.
)
echo -------------------------------------
pause

echo.
echo Testing CUS2 (ACO):
echo -------------------------------------
for %%i in (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17) do (
    python search.py Test/test_%%i.txt cus2
    echo.
)
echo -------------------------------------