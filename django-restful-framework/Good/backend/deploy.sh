cp $PREFIX/etc/apt/sources.list $PREFIX/etc/apt/sources.list.bak
rm -f $PREFIX/etc/apt/sources.list 
echo -e "# The termux repository mirror from TUNA:\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux stable main" >> $PREFIX/etc/apt/sources.list
pkg upgrade
pkg install openssh python git
mkdir ~/.pip
echo -e "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.pip/pip.conf
pip install --upgrade pip 
pip install Django==2.2.9 django-filter==2.2.0 djangorestframework==3.11.0 djangorestframework-jwt==1.11.0 PyJWT==1.7.1 pytz==2019.3 restframework-datachange==0.0.2.1 sqlparse==0.3.0
git config --global http.postBuffer 5242880000
git config --global https.postBuffer 5242880000
cd ~
mkdir sale_system
cd sale_system
# git clone XXX
python manage.py makemigrations
python manage.py migrate
python manage.py deploy