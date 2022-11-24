""""

sudo apt update                            #second step 

sudo apt install python                    #install python 
sudo apt install python3-pip                 #second method step

#command for installing venv package 
pip install virtualenv                      #secnd method 
 
sudo apt install python3.10-venv


#commands for setting (making) up virtual environment at the decided path
python3 -m venv tutorial-env             


#activate venv
source tutorial-env/bin/activate

#uninstall lib 
python -m pip uninstall


#
python -m pip show              will display information about a particular package:


#
python -m pip list               will display all of the packages installed in the virtual environment:
## pip list              (working in  venv)

#
python -m pip freeze        
                            will produce a similar list of the installed packages, but the output uses the format that python -m pip install expects.
pip freeze          (working in venv)


#django install 

python -m pip install Django

# make code importable 
 python -m pip install -e django/                         # not working
 
 
 python -m django --version

$ django-admin startproject mysite



""""
