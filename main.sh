#!/bin/bash

python -m main
cd public && python3 -m http.server 8888
