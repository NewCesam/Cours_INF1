=== "TD 8"
    ## 1. 
    Trouver une définition récursive du PGCD de deux entiers et écrire l’algorithme correspondant.

        
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
    
    __

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



                
