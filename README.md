# Wahyu Project

- Welcome to Wahyu Brand Website GitHub Project
- Wahyu Brand Main Website
- Customer Portal
- Supplier Portal
- Sales Order System
    - Connect all modules together
    wahyuproject-instance
    user: root
    pw: wahyu12345
    db: wahyu_db
    
    wahyuproject-253604:asia-southeast1:wahyuproject-instance
    
    @cmd prompt: 
    cloud_sql_proxy.exe -instances="wahyuproject-253604:asia-southeast1:wahyuproject-instance"=tcp:3306
    
    virtaulenv: pywahyu
    project: wahyuproject

    superuser: wahyu
    pw: wahyu12345

    gcloud: wahyuproject
    account: it.macronoob@gmail.com

    tulis something

- cloud sql proxy for MACOS
./cloud_sql_proxy -instances="wahyuproject-253604:asia-southeast1:wahyuproject-instance"=tcp:3306

source pywahyu/bin/activate

- How to send email using django
https://medium.com/@_christopher/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e