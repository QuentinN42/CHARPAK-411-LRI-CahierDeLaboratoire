#!/usr/bin/env bash
(cd files && python3 build.py)
latex -output-format=pdf CahierDeLabo.tex
