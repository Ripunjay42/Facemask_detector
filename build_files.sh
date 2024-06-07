#!/usr/bin/env python3.8  # Specify interpreter (adjust path if needed)

echo "BUILD START"

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3.8 manage.py collectstatic --noinput --clear

echo "BUILD END"