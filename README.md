# Projeto-Final-EFIJOTA
## Para criar o ambiente virtual
```bash
python -m venv .venv
```
## Para entrar no ambiente virtual
 _Windows_
 ```bash
.venv\Scripts\activate
```

 _Linux/macOS_
 ```bash
source .venv/bin/activate
```
## Dentro do ambiente virtual
```bash
pip install -r requirements.txt
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
```bash
python manage.py runserver
```
```bash
acesse http://127.0.0.1:8000/admin/
```
