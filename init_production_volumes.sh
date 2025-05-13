#!/bin/bash

mkdir -v data/prod
chown :flask data/prod
chmod 775 data/prod
chmod g+s data/prod
