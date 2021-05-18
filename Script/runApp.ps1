./venv/Scripts/activate                         # Activate the venv
$Env:PYTHONPATH += ";.\Source\Python";          # Add the Python root to the PYTHON path relative to project root
$Env:FLASK_ENV = "development";                 # Flask environment type
$Env:FLASK_APP = ".\Source\Python\flask_app.py" # Set the location of the root script
flask run -h 0.0.0.0 -p 9001
