#/usr/bin/bash -x

cd js
webpack
cd ../
python web.py
