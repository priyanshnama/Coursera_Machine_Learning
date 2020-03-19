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
pip uninstall cycler
pip uninstall joblib
pip uninstall kiwisolver
pip uninstall pyparsing
pip uninstall python-dateutil
pip uninstall pytz
pip uninstall scipy
pip uninstall six
pip uninstall numpy
pip uninstall matplotlib
pip uninstall scikit-learn
ECHO All Done
cd..
final.bat
