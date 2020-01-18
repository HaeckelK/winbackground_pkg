@echo off
cd..

for %%f in (*.py) do (
    python -m pydoc -w %%~nf
)

move *.html %~dp0

pause