- BACKEND

Fisierul index.js din foloderul "backend" este fisierul in care am creat cele doua rute pentru a lua datele din API-ul primit.
Pentru Backend am folosit Node.js cu Express.
Pe scurt in app.get() am facut request.post la API si asa am luat datele.

Pentru a porni backend-ul trebuie folosita comanda: npm start

- FRONTEND

Fisierul numit "social-insider-task" reprezinta fisierul de frontend de React.
In fisierul "src"/App.js am lucrat tot frontend-ul care functioneaza asa:

Pe pagina de start: localhost:3000 apar doua date-pickere pentru Data de start si Data de sfarsit.
Dupa ce sunt selectate datele atunci apare un tabel cu ID-ul profilelor si numele lor. Pentru a calcula Total Fans si Engagements am 
folosit link-uri care trimit pe alte pagini unde scrie numarul total de fans/engagements.

Pentru a porni frontend-ul trebuie folosita comanda: npm start 
