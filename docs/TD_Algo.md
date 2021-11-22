=== "TD 8"
    ## 1. 
    Trouver une définition récursive du PGCD de deux entiers et écrire l’algorithme correspondant.

    ??? abstract "Réponse"

        PGCD(A,B):
            A, B : entiers
                
            début
                si A mod B = 0
                    alors
                        retourner B
                sinon
                    retourner PGCD(B,A mod B)
            fin

    ## 2. 
    Trouver un algorithme récursif permettant de calculer la puissance d’un nombre x^y. Attention : y pourra être éventuellement négatif

    (insérer image)

    ??? abstract "Réponse"

        Puissance(x,y):
            x, y : réels
               
            début
                si y=0
                    alors
                        retourner 1
                si y>0
                    alors
                        retourner x*Puissance(x,y-1)
                    sinon
                        retourner (1/x)*Puissance(x,y+1)
            fin            

    ## 3. 
    Trouver un algorithme récursif permettant d’inverser une chaîne de caractères (‘NF01’ devient ‘10FN’, ‘bonjour’ devient ‘ruojnob’…).

    ??? abstract "Réponse"

        Inversion(S):
            S : chaîne
                
            début
                si S=" "
                    alors
                        retourner S
                    sinon
                        retourner Inversion(copie(S,2,longueur(S)))+S[1]
            fin

    ## 4. 
    En déduire un algorithme permettant d’indiquer si un mot est un palindrome (identique à l’endroit et à l’envers, par exemple : ‘noyon’ ou ‘rever’).

    ??? abstract "Réponse"

        Palindrome(S):
            S : chaîne
                
            début
                si longueur(S)<=1
                    alors
                        retourner Vrai
                    sinon
                        si S[1]=S[longueur[S]]
                            alors
                                retourner Palindrome(copie(S,2,longueur(S)-1))
                            sinon
                                retourner Faux
            fin

    ## 5. 
    Ecrire une version récursive de l’algorithme de recherche dichotomique.
    ??? info "Recherche dichotomique"
        On rappelle que la recherche dichotomique est une recherche par approximations successives dans une liste ordonnée (triée par ordre croissant de ses valeurs). On compare l'élément recherché à celui situé en milieu de liste. S'il est plus grand, on recommence avec la moitié supérieure de la liste, sinon avec la moitié inférieure de la liste, jusqu'à convergence vers l'élément recherché (égalité = succès), ou jusqu'à ce qu'il n'y ait plus aucun élément à comparer (liste vide). Dans ce cas, l'élément recherché était absent de la liste. Ecrire un algorithme dichotomie permettant d'effectuer une recherche dichotomique dans un tableau de 100 entiers.
    
    ??? abstract "Réponse"

        Dicho(T,val,d,f):
            T : tableau
            val : entier
            d,f : entiers
              
            début
                si d > f
                    alors
                        retourner 0
                    sinon
                        n <--- (d+f)/2
                        si T[n] = val
                            alors
                                retourner n
                            sinon
                                si val>T[n]
                                    alors
                                        retourner Dicho(T,val,n+1,f)
                            sinon
                                retourner Dicho(T,val,d,n-1)
            fin


=== "TD 9"
    ##1.
    Définir le type date permettant de représenter une date comportant le numéro du jour et le numéro du mois (14 7, 25 12, 31 12, ...).  
    Ecrire un algorithme jour_du _lendemain qui détermine la date du lendemain d’un jour donné. On supposera que l’année n’est pas bissextile.

    ??? abstract "Réponse"

        date = enregistrement
            jour : entier (1,31)
            mois : entier (1,12)
        Algorithme jour_du_lendemain
            variables : 
                d1,d2 : date
                max_j : entier
            début
                Afficher("Donnez une date : jour et mois)
                lire(d1.jour,d1.mois)
                si(d1.mois = 2)
                    alors
                        max_j <--- 28
                    sinon si (d1.mois est dans [1,3,5,7,8,10,12])
                        alors
                            max_j <--- 31
                        sinon
                            max_j <--- 30
                d2.jour <--- d1.jour + 1
                si (d2.jour > max_j)
                    alors
                        d2.jour <--- 1
                si (d2.jour = 1)
                    alors
                        d2.mois <--- d1.mois + 1
                        si (d2.mois = 13)
                            alors
                                d2.mois <--- 1
                sinon
                    d2.mois <--- d1.mois
                Afficher("Le jour suivant est", d2.jour, d2.mois)
            fin
    Il faudrait compléter l'algorithme avec une fonction de vérification de la cohérence de la date

    ##2.
    Un supermarché désire créer un tableau contenant la liste des prix de tous les articles disponibles en rayon. Ecrire un algorithme qui écrit dans un tableau la liste des articles avec leur prix (entrés au clavier). On désire ensuite calculer le prix moyen des articles en rayon. On aimerait, pour conclure, rechercher le nombre d'articles pour lesquels le prix est supérieur à un tarif entré par l'utilisateur. Par exemple, on voudrait savoir combien d'articles sont vendus à plus de 500 euros. 

    ??? abstract "Réponse"

        article = enregistrement
            nom : chaîne
            prix : réel
        Algorithme
            variables :
                i, N, Taille, nb : entier
                S, Tarif : réel
            début
                #Saisie des articles
                afficher ("Combien y a-t-il d'article ?")
                lire (N)
                T : tableau de N article           
                i <--- 0
                répéter
                    i <--- i + 1
                    afficher("Nom de l'article :")
                    lire(T[i].nom)
                    afficher("Prix de l'article :")
                    lire(T[i].prix)
                tant que (T[i].prix > 0 et i <= N)
                Taille <--- i - 1

                #Prix moyen
                pour i variant de 1 à Taille 
                    S <--- S + T[i].prix
                afficher("Le prix moyen des articles est", S/Taille)

                #Recher articles sup
                afficher ("Donnez un prix"
                lire(Tarif)
                nb <--- 0
                pour i variant de 1 à Taille
                    si(T[i].prix >= Tarif)
                        alors
                            nb <--- nb + 1
                afficher(nb, "articles dont le prix est supérieur ou égal au tarif entré")

    ##3.
    On dispose d’un tableau d’enregistrements ayant la structure suivante : nom, prénom, âge.  

    a) Ecrire un algorithme avec un MENU permettant de proposer l’ensemble des actions à réaliser (cf liste ci-dessous). Une boucle sera effectuée jusqu’à ce que l’utilisateur ait choisi 0 pour sortir. L’algorithme vérifiera que le choix de l’utilisateur est un chiffre compris entre 0 et 6. Si ce n’est pas le cas, son choix lui sera demandé à nouveau.  

    ??? abstract "Réponse"

        etudiant = enregistrement
            nom : chaîne
            prenom : chaîne
            age : entier
        
        Algorithme MENU
            variables
                choix : entier
            début
                répéter
                    afficher("Tapez 1 : Stockage des informations des étudiants dans le tableau")
                    afficher("Tapez 2 : Afficher l’ensemble du tableau (liste de tous les étudiants)")
                    afficher("Tapez 3 : Ajout d’un étudiant")
                    afficher("Tapez 4 : Recherche d’un étudiant")
                    afficher("Tapez 5 : Suppression d’un étudiant")
                    afficher("Tapez 6 : Modification d’un étudiant")
                    afficher("Tapez 0 : Quitter")
                    répéter
                        afficher("Entrez votre choix")
                        lire(choix)
                    jusqu'à (choix >= 0 et choix <= 6)
                jusqu'à choix = 0

    b) Ecrire les algorithmes pour réaliser les actions suivantes :  
     1. Stockage de l’ensemble des étudiants dans le tableau  
     2. Afficher l’ensemble du tableau (liste de tous les étudiants)  
     3. Ajout d’un étudiant  
     4. Recherche d’un étudiant  
     5. Suppression d’un étudiant  
     6. Modification d’un étudiant  

    ??? abstract "Algorithme de stockage"
            
            Algorithme STOCKAGE
                input
                    max : entier
                    T : tableau de max etudiant
                variables
                    i, nb_etu : entier

                début
                    répéter
                        afficher("Donner le nombre d'étudiants")
                        lire(nb_etu)
                    jusqu'à (nb_etu > 0 et nb_etu <= max)
                    pour i variant de 1 à nb_etu faire
                        afficher("Donnez le nom et le prénom")
                        lire(T[i].nom, T[i].prenom)
                        afficher("Donnez l'âge")
                        lire(T[i].age)
                    retourner nb_etu
                fin

    ??? abstract "Algorithme d'affichage"

            Algorithme AFFICHAGE
                input
                    max : entier
                    T : tableau de max etudiant
                    nb_etu : entier
                variables
                    i : entier
                début
                    pour i variant de 1 à nb_etu faire
                        afficher("Etudiant", i, ":", T[i].nom, T[i].prenom, T[i].age)
                fin

    ??? abstract "Algorithme d'ajout"

            Algorithme AJOUT
                input
                    max, nb_etu : entier
                    T : tableau de max etudiant
                début
                    si nb_etu < max
                        alors
                            nb_etu <--- nb_etu + 1
                            afficher("Donnez le nom et le prénom")
                            lire(T[nb_etu].nom, T[nb_etu].prenom)
                            afficher("Donnez l'âge")
                            lire(T[nb_etu].age)
                        sinon
                            afficher("Impossible d'ajouter un étudiant")
                    retourner nb_etu
                fin

    ??? abstract "Algorithme intermédiaire : RECHERCHE_indice"
            
            Algoritme RECHERCHE_indice
                input
                    max, nb_etu : entier
                    T : tableau de max etudiant
                    nom : chaîne
                    prenom : chaîne
                variables
                        i : entier
                début
                    i <--- 1
                    tant que (i <= nb_etu et (T[i].nom <> nom ou T[i].prenom <> prenom))
                        i <--- i + 1
                    fin tant que
                    retourner i
                fin

    ??? abstract "Algorithme de recherche"

            Algorithme RECHERCHE
                input
                    nb_etu, max : entier
                    T : tableau de max etudiant
                variables
                    nom, prenom : chaîne
                    i : entier
                début
                    afficher("Donnez le nom et le prénom à rechercher")
                    lire(nom, prenom)
                    i <--- RECHERCHE_indice(nb_etu, max, T, nom, prenom)
                    si(i > nb_etu)
                        alors
                            afficher("L'étudiant n'existe pas")
                        sinon
                            afficher("Nom : ", T[i].nom, "Prénom : ", T[i].prenom, "Âge : ", T[i].age)
                fin

    ??? abstract "Algorithme de Suppression"

            Algorithme SUPRESSION
                input
                    nb_etu, max : entier
                    T : tableau de max etudiant
                variables
                    nom, prenom : chaîne
                    i : entier
                début
                    afficher("Donnez le nom et le prénom à rechercher")
                    lire(nom, prenom)
                    i <--- RECHERCHE_indice(nb_etu, max, T, nom, prenom)
                    si(i > nb_etu)
                        alors
                            afficher("L'étudiant n'existe pas")
                        sinon
                            nb_etu = nb_etu - 1
                            pour j variant de i à nb_etu faire
                                T[j] <--- T[j+1]
                fin

    ??? abstract "Algorithme de Modification"

            Algorithme MODIFICATION
                input
                    nb_etu, max : entier
                    T : tableau de max etudiant
                variables
                    nom, prenom : chaîne
                    i : entier
                début
                    afficher("Donnez le nom et le prénom à rechercher")
                    lire(nom, prenom)
                    i <--- RECHERCHE_indice(nb_etu, max, T, nom, prenom)
                    si(i > nb_etu)
                        alors
                            afficher("L'étudiant n'existe pas")
                        sinon
                            afficher("Donnez le nom et le prénom")
                            lire(T[i].nom, T[i].prenom)
                            afficher("Donnez l'âge")
                            lire(T[i].age)
                fin

    ##4.
    On dispose d’un tableau dont chaque élément possède la structure suivante :

        type Objet élève
            nom : chaîne
            prenom : chaîne
            math : réel
            physique : réel
            français : réel
    
    Ecrire un algorithme qui exploite ce tableau pour afficher la liste des étudiants avec leur note en Maths, en Physique, en Français, ainsi que leur moyenne.  
    Par exemple, nous pourrions avoir les informations suivantes :  
    (insérer image)
    On supposera que le nombre d’élèves est inférieur ou égal à 100.

    ??? abstract "Réponse"

            eleve = enregistrement
                nom : chaîne
                prenom : chaîne
                math : réel
                physique : réel
                français : réel
            Algorithme Affichage
                Input
                    T : tableau de 100 eleve
                    nb_eleve : entier
                variables
                    i : entier
                    M_M,M_P,M_F,moy : réel
                début
                    M_M <--- 0
                    M_P <--- 0
                    M_F <--- 0
                    afficher("Nom   Prénom  Math    Physique    Français    Moyenne")
                    afficher("__________________________________________")
                    pour i variant de 1 à nb_eleve faire
                        afficher(T[i].nom,"    ",T[i].prenom,"    ",T[i].math,"   ",T[i].physique,"   ",T[i].français,"    ",(T[i].math + T[i].physique + T[i].français)/3)
                        M_M <--- M_M + T[i].math
                        M_P <--- M_P + T[i].physique
                        M_F <--- M_F + T[i].français
                    M_M <--- M_M/nb_eleve
                    M_P <--- M_P/nb_eleve
                    M_F <--- M_F/nb_eleve
                    moy <--- (M_M + M_P + M_F)/3
                    afficher("Moyenne    ", M_M,"    ",M_P,"    ",M_F,"    ",moy)

