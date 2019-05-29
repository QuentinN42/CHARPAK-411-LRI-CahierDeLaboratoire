#!/usr/bin/env bash
cp -rf ../Stage/data/ ./sources/
rm $(lr | grep "\.json")
rm $(lr | grep "\.prejson")
