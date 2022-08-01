import os
from js import document, window, Uint8Array, File, console

# local = window.localStorage
# console.log(local, 'aaye')
# console.log('hello world')
files = os.listdir('/home/pyodide')
for file in files:
        print(file)