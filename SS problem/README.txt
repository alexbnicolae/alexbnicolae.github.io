Pornire proiect:
- descarcare proiect github: https://github.com/alexbnicolae/alexbnicolae.github.io/tree/main/SS%20problem
- deschidere proiect intr-un IDE
- pornire server prin comanda: python manage.py runserver 0.0.0.0:8000
- deschidere site la adresa: http://localhost:8000

Functionalitati site:
- Se poate loga cu Google(recomandat) sau se poate crea cont, dar cand am urcat pe github, am dezactivat trimiterea mail-ului din fisierul settings.py
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
