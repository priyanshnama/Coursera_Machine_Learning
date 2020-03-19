@ECHO OFF 
:: This batch file install basic requirements listed in requirements.txt
TITLE Setting up things
python --version
pip --version
ECHO Upgrading pip
python -m pip install --upgrade pip
ECHO installing Packages
pip install numpy
pip install matplotlib
pip install pandas
pip install scikit-learn
ECHO Upgrading Packages
pip install --upgrade pandas
pip install --upgrade numpy
pip install --upgrade matplotlib
pip install --upgrade scikit-learn
ECHO All Done
python "Simple Linear Regression.py"
PAUSE