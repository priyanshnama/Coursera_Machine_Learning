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
python "Simple Linear Regression.py"
ECHO Uninstalling Packages
pip uninstall pandas
y
pip uninstall cycler
y
pip uninstall joblib
y
pip uninstall kiwisolver
y
pip uninstall pyparsing
y
pip uninstall python-dateutil
y
pip uninstall pytz
y
pip uninstall scipy
y
pip uninstall six
y
pip uninstall numpy
y
pip uninstall matplotlib
y
pip uninstall scikit-learn
y
ECHO All Done
cd..
final.bat
