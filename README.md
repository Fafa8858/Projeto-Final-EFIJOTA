# Projeto-Final-EFIJOTA
Projeto final no curso de python na OC3

# Para a plena vizualização do projeto:

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# acesse http://127.0.0.1:8000/admin/
