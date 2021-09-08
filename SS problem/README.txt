Update:
- Am facut sa functioneze chat-ul, dupa trimiterea mesajului pagina isi da refresh automat.
- Acum merge si trimiterea unui fisier de orice tip.
- Am redenumit titlurile paginilor in functie de pagina respectiva.
- Am reordonat pagina de Search user.


Proiectul este creat in Python si Django.

Pornire site:
- descarcare proiect github: https://github.com/alexbnicolae/alexbnicolae.github.io/tree/main/SS%20problem
- deschidere proiect intr-un IDE
- trebuie instalat pip: https://phoenixnap.com/kb/install-pip-windows
- pentru a instala librarile din proiect: pip install -r requirements.txt
- pentru crearea de superuser (pentru a intra in baza de date la http://localhost:8000/admin) trebuie folosita comanda  python manage.py createsuperuser si apoi de completat 
superuserul cu datele cerute.
- pornire server prin comanda: python manage.py runserver 0.0.0.0:8000
- deschidere site la adresa: http://localhost:8000


Functionalitati site:
- Creare cont: deoarece am dezactivat email-ul de confirmare, dupa creare cont in Sign-up, o sa apara o eroare: SMTPAuthenticationError at /signup/, dar contul se creeaza si dupa se poate conecta cu email-ul si parola.
- In bara de search se cauta utilizatorii dupa username, nume sau prenume (nu merg 2 cuvinte sau mai mult)
- O data cautata persoana se poate aduaga la friends
- Pentru a aparea in lista de prieteni trebuie ca cealalta persoana va adauge la prieteni
- Chat-ul este creat in momentul cand ambele persoane sunt in lista fiecaruia de  prieteni
- Chat-ul functioneaza doar text, iar dupa trimiterea unui mesaj trebuie dat refresh la pagina de chat.

Informatii pentru dev:
- In fisierul UserInteraction/templates se gasesc template-urile html
- Fisierele de lucru efectiv se gasesc in feed.
feed/models.py - fisierul in care am creat tabelele
feed/views.py - fisierul in care am creat functionalitatile de pe site
feed/admin.py - fisierul de inregistrare a tabelelor in baza de date
- Pentru conectarea ca superuser trebuie creat acesta cu comanda python manage.py createsuperuser.
- Pentru logarea ca superuser trebuie mers la pagina http://localhost:8000/admin
- Cand se modifica ceva in models.py trebuie create noi migrari folosind comanda: python manage.py makemigrations.
- Pentru a aplica noile migrari trebuie folosita comanda: python manage.py migrate
