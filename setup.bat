@ECHO OFF 
:: This batch file install basic requirements listed in requirements.txt
TITLE Setting up things
:: Section 1: Some information.
python --version
pip --version
python -m pip install --upgrade pip
pip install numpy
pip install matplotlib
pip install pandas
pip install scikit-learn
python "Simple Linear Regression.py"
PAUSE