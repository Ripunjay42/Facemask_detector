echo "BUILD START"

# Install dependencies
Pip install -r requirements.txt

# Collect static files
Python3.8 manage.py collectstatic --noinput --clear

echo "BUILD END"