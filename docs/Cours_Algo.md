## Notion de variable
- Donnée : valeur introduite pendant l'exécution du programme
- Constante : valeur fixe utilisée par le programme
- Variable : valeur susceptible de changer au cours de l'exécution du programme

## Types de données
- Booléen : vrai ou faux (0 ou 1) --> sur 1 bit
- Caractère : à retrouver dans la table ASCII
- Entier : nombre sans virgule, positif ou négatif
- Réel

!!! tip "Etapes d'écriture d'un algorithme :"
    1. Compréhension de l'énoncé
    2. Distinctions des entrées, sorties, contraints et moyens d'action
    3. Création d'un algorithme général puis précis

## Instructions de base
### - Affectation
Attribution de la valeur d'une expression à une variable : 
    
    U <-- V
### - Lecture
Demande d'une valeur :
    
    lire(V1,V2,...,Vn)
### - Ecriture
Affichage d'une valeur :

    afficher(V1,V2,...,Vn)
### - Choix simple
Test : 

    si ... alors : 
    
    (sinon :)

## Boucles
**Boucles = structure itérative** :
: Sont destinées à être exécutées plusieurs fois (Itération : passage dans la boucle)
    **- Boucles à bornes définies** :
    : Incrémentation automatique du min au max

            pour i variant de x à y faire :
                <instruction>
        ??? attention
            - La variable de boucle doit être scalaire (entier, énuméré, intervalle ou caractère)
            - <instruction> peut être un bloc de plusieurs instructions
            - Si x > y , il n'y aura pas d'exécution

    **-Boucles à bornes indéfinies** :
    : Au moins un passage

            tant que <expression> faire :
                <instruction>
            fin tant que

            répéter
                <instruction>
            jusqu'à <expression>
        ??? attention
            Bien vérifier la condition de sortie pour éviter une boucle infinie
            
## Tableaux
Une collection ^^ordonnée^^ d'éléments de même type. On accède à chaque élémet à l'aide d'un indice (2 indices pour un tableau à 2 dimensions).

    <identificateur> = Tableau[type-index] de type-éléments

## Chaîne de caractères
Suite de caracères regroupés dans une même variable. Le type `string` en python avec 255 caractères max permet de manipuler des chaînes de longueur variable.

### Fonctions sur les chaînes

- ORDRE : `ORDRE(caractère)` renvoie un entier correspondant au code ASCII du caractère
- CARACTERE : `CARACTERE(entier)` renvoie le caractère correspondant à l'entier dans la table ASCII
- Comparaison de chaînes de caractère :

        s1 <--- "Dupont"
        s2 <--- "Dupond"  #s2 < s1
        s3 <--- "Du pont" #s3 < s1 (compare les caractères 1 à 1 et *espace*<"p")
        s4 <--- "du Pont" #s4 > s1

??? example "Exemple : conversion minuscule-majuscule"
    
        Soit c une variable de type car
        si (c >= "a") et (c <= "z") alors
            c <--- CARACTERE(ORDRE(c)-ORDRE("a")+ORDRE("A"))
- Concaténation : opération accolant 2 ou plusieurs chaînes de caractères

        s1 <--- "du"
        s2 <--- "pont"
        s3 <--- s1 + s2        #s3 vaut "dupont"
        s4 <--- s1 + " " + s2  #s4 vaut "du pont"

- LONGUEUR : `LONGUEUR("chaîne")` renvoie un entier représentant la longueur de la chaîne
- POSITION : `POSITION("sous-chaîne","chaîne")` renvoie la position d'une sous-chaîne dans une chaîne
- COPIE : `COPIE("chaîne source", début, longueur)` renvoie une sous-chaîne de longueur donnée à partir d'une position donnée

    

