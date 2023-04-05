SMS gateway avec une partie client et une autre serveur

Côté client, le projet provient de ce dépot https://github.com/juancresc/SMSHub

Côté serveur, c'est un script en Python qui tourne en permanence sur une machine dédiée, le serveur attend une éventuelle requête du client. Dès la réception d'un nouveau sms, il le stocke dans un fichier JSON. Le contenu de ce fichier est affiché via une simple page HTML. le script de base a été inspiré de ce morceau de code https://gist.github.com/hawkins/36b7d781d8fa5277d4cb29b6906abe57

La communication doit se faire sur le même LAN, il existe toutefois une solution pour que le serveur soit accessible depuis l'extérieur en utilisant par exemple ngrok calibré sur le même port d'écoute que le serveur
