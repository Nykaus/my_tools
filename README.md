# Mes outils perso pour sublime-text 

Petit outils perso sur sublime-text


##Sommaire



* [Numerotation par mutli-selection](#numerotation) 
* [Nettoyeur de la console de Sublime-Text](#clean_console) 
* [Switcher de 2 selections](#switch) 
* [La décrémentation ou l'augmentation d'un chiffre selectionné](#compteur) 
* [Affichage du path du fichier](#path) 
* [Affichage de l'heure  MM:HH](#stampHour) 
* [Différence entre 2 heure  MM:HH - MM:HH ](#diffheure) 
* [Additionner plusieurs heures](#sumheure) 
* [Supprimer la multi selection par le clavier](#suppselections) 
* [Afficher un calendrier](#calendar) 



## <a id="numerotation"></a> [ctrl+alt+c] Numerotation par mutli-selection

Avec l'outil multi-selection et la commande ctrl+alt+c, vous avec une numérotation aligner

		1
		2
		3
		4


## <a id="clean_console"></a> [ctrl+alt+v] Nettoyeur de la console de Sublime-Text

Ajout des lignes dans la console de sublime text pour séparer les informations

## <a id="switch"></a> [ctrl+alt+espace] Switcher de 2 selections
En selectionnant 2 elements et en utilisant la commande ctrl+alt+espace les elements s'intervertissent.

## <a id="compteur"></a> [ctrl+alt+keypad_minus or keypad_plus] La décrémentation ou l'augmentation d'un chiffre selectionné

Vous pouvez incrémenter ou décrémenter un chiffre selectionner


## <a id="path"></a> [ctrl+alt+f] Affichage du path du fichier
Cette commande utiliser dans un fichier, donnera le path du fichier.

## <a id="stampHour"></a> [ctrl+alt+x] Affichage de l'heure  MM:HH
Cette commande colle l'heure actuel à la selection

## utiliser pour la gestion de ticket:
avec le snipet "ticket" je creer une ligne pour ajouter un commentaire

			2:02	09:00 - 11:02	"Ajouter l'information de ma tache 1"
	= 3:0	0:58	11:02 - 12:00	"Tache 2"

	Grace à la différence du temps me donne le tps de la tache
	et l'addition du tps des tache me donne la durée total. très rapide!!

### <a id="diffheure"></a> [ctrl+alt+keypad_divide] Différence entre 2 heure  MM:HH - MM:HH
En selection une soustraction d'heure (MM:HH - MM:HH) le resultat s'affichera a gauche
ex:		4:10	10:12 - 14:22

### <a id="sumheure"></a> [ctrl+alt+keypad_multiply] Additionner plusieurs heures
4:10	10:12 - 14:22

## <a id="suppselections"></a> [ctrl+alt+s] Supprimer la multi selection par le clavier
Après que j'ajoute la multi-selection avec mon clavier, au lieu d'utiliser ma souris pour l'unifier, j'utilise ma commande ctrl+alt+s

## <a id="calendar"></a> [ctrl+alt+k] Afficher un calendrier

Affichage d'un calendrier 
ctrl+alt+k : affiche le calendrier du mois actuel
sinon si vous selectionner mois-années (MM-YYYY) ex: 5-2017

		------------------------------------
		|             Mai 2017             |
		------------------------------------
		| Lu | Ma | Me | Je | Ve | Sa | Di |
		------------------------------------
		| 01 | 02 | 03 | 04 | 05 | 06 | 07 |
		------------------------------------
		| 08 | 09 | 10 | 11 | 12 | 13 | 14 |
		------------------------------------
		| 15 | 16 | 17 | 18 | 19 | 20 | 21 |
		------------------------------------
		| 22 | 23 | 24 | 25 | 26 | 27 | 28 |
		------------------------------------
		| 29 | 30 | 31                     |
		------------------------------------
