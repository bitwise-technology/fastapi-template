#!/bin/bash

cd /home/app && uvicorn app.main.main:app --host=0.0.0.0 --port=80 --reload
