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
            - `<instruction>` peut être un bloc de plusieurs instructions
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

## Récursivité
Une fonction ou une procédure est dite récursive s'il est fait appel à cette fonction ou à cette procédure dans le corps d'instructions qui la définit : la fonction ^^s'appelle elle-même^^

    x ancêtre de y
    si x parent de z
    et z ancêtre de y
    ou x parent de z

??? example "Exemples"
    ??? abstract "Factorielle"
        Déf itérative :
        n! = n*(n-1)* ... *1

        Déf récursive: 
        n! = n*(n-1)!
    
            si (n>1)
                alors
                    factorielle <--- n*facrtorielle(n-1)
                sinon
                    factorielle <--- 1

    ??? abstract "Somme des n premiers nombres"
        Algorithme itératif :

            variables
                i : entier
                sum : entier long

            début
                sum <--- 0
                pour i variant de 1 à N faire
                sum <--- sum + i
            fin

        Algorithme récursif :

            si n = 0
                alors
                    somme <--- somme <--- 0
                sinon somme <--- somme(n-1) + n

            ##S(n) = S(n-1) + n
            ##S(0) = 0        ##pour la condition d'arrêt
    
    ??? abstract "Saisie de phrase"
        Algorithme récursif :

            constante
                POINT = "."
            variable
                car : caractère

            faire :
                début
                    lire(car)
                    si (car<>POINT)
                        alors
                            faire
                    afficher (car)
                fin
    
    ??? abstract "Exemple de récursivité croisée/double : les fonctions cos(x) et sin(x)"
        Principe de récursivité :
            
            sin(x) = x quand x tend vers 0
            sin(x) = 2 * sin(x/2) * cos(x/2)

            cos(x) = 1 quand x tend vers 0
            cos(x) = cos²(x/2) - sin²(x/2)
        
        Algorithme :

            sinus(x):
                début
                    si x < 0.00001
                        alors
                            sinus ← x
                        sinon
                            sinus ← 2 * sinus(x/2) * cosinus(x/2)
                fin
            
            cosinus(x):
                début
                    si x < 0.00001
                        alors
                            cosinus ← 1
                        sinon
                            cosinus ← ((cosinus(x/2))^2) - ((sinus(x/2))^2)
                fin

    ??? abstract "Tours de Hanoï"
        - But : déplacer la pile de la tour 1 à la tour 3, en ne déplaçant qu'un disque à la fois, et en s'assuant qu'aucun disque ne repose sur un disque de plus petite dimension.
        - Hypothèse : on veut déplacer la pile des n-1 premiers disques de la tour 1 à la tour 2
        - Action : Déplacer le dernier disque de la tour 1 à la tour 3
        - Ensuite : il ne reste plus qu'à déplacer les n-1 disques de la tour 2 à la tour 3
        - Condition d'arrêt : nb disques = 0

                Hanoi (nb_disques, T_orig, T_inter, T_dest : entiers) :
                    début
                        si (nb_disques > 0)
                            alors
                                Hanoi(nb_disques - 1, T_orig, T_inter, T_dest)
                                afficher("Déplacer le disque de ", T_orig, "à", T_dest)
                                Hanoi(nb_disques - 1, T_inter, T_dest, T_orig)
                    fin

## Enregistrement
Comment modéliser une entité ayant plusieurs caractéristiques ?

Une variable de type Objet(ou Classe) est une variable structurée avec plusieurs champs.
Les champs sont les attributs ou caractéristiques de l'enregistrement.

    type
        Objet Voiture
            marque : chaine
            cylindre : réel
            couleur : chaîne
                
    variable
        auto : Voiture

    auto.marque <-"Renault"

!!! attention
    Tableau : éléments de même type
    Objet : les champs peuvent être de type diff

??? example "Représenter un tableau et sa taille"

        type
            Objet Table
                elements: tableau[1..NMAX] de réels
                taille : integer;
        Variables : T:Table

        pour i variant de 1 à T.taille faire
            lire(T.elements[i]);
    
??? tips "Un champ peut-être un enregistrement"

        type
            objet LIEU
                rue: chaîne
                code_postal: chaîne
                ville: chaîne
            
            objet SITE
                nom: chaîne
                adresse : LIEU
            
            objet UNIVERSITE
                nom: chaîne
                liste_sites: tableau[1..NMAX] de SITE
        
        Variables :
            univ: UNIVERSITE

        univ.sites[1].nom                #accès au nom du premier site
        univ.liste_sites[2].adresse.rue  #accès à la rue du 2ème site

??? example "Tableau d'enregistrements"
    
        type
            Objet UN_RESULTAT
                nom, prenom: chaîne
                median, final: réel
                TP: tableau[1..MAXTP] de réel

            Resultats=tableau[1..NBMAX] de UN_RESULTAT
        Variables
            tabResult: Resultats N

        tabResult[3].median              #accès à la note du médian du troisième étudiant
        tabResult[i].TP[j]               #accès à la jème note du ième étudiant

## Ensembles

### Opérateurs

**Union** :
: Symbole `+`
??? example "Exemple"

**Intersection** :
: Symbole `*`
??? example "Exemple"

**Différence** :
: Symbole `-`
??? example "Exemple"

## Algorithmes de tri
Problème : trier un tableau d'éléments de même type, muni d'une relation d'ordre
### Tri par sélection
- On suppose qu'on connaît le nb d'éléments
- on cherche le min
- on le place en premier
- on cherche le minimum suivant
- on le place en deuxième
- ...

    8 12 5 35 21 `3`  
    3 12 `5` 35 21 8  
    3 5 12 35 21 `8`  
    ........................  

        pour i allant de 1 à n-1 faire
            min <--- T[i]
            indiceMin <--- i
            pour j allant de i+1 à n faire
                si T[j] < min
                    alors
                        min <--- T[j]
                        indiceMin <--- j
            Echanger T[i] et T[indiceMin]

Version récursive :

        Tri(i,n) :
            début
                si i<= n-1
                    alors
                        min <--- T[i]
                        indiceMin <--- i
                        pour j allant de i+1 à n faire
                            si T[j] < min
                                alors
                                    min <--- T[j]
                                    indiceMin <--- j
                        Echanger T[i] et T[indiceMin]
                        Tri(i+1,n)
            fin

### Tri par insertion

        pour i allant de 1 à n-1 faire
            début
                elt <--- T[i+1]
                k <--- i
                tant que (elt < T[k]) et (k >= 1) faire
                    T[k+1] <--- T[k]
                    k <--- k-1
                T[k+1] <--- elt
            fin

### Tri par échange (tri à bulles)
On échange les éléments 2 à 2 en les réordonnant, les éléments mal classés remontent dans la liste comme des bulles à la surface d'un liquide. L'éfficacité dépend du tableau initial, efficace si le tableau est presque trié

        nbElts <--- n
        echange <--- vrai
        tant que echange faire
            echange <--- faux
            max <--- nbElts
            pour i allant de 1 à max-1 faire
                si T[i] > T[i+1] alors
                    echanger T[i] et T[i+1]
                    echange <--- vrai
                    nbElts <--- i
        