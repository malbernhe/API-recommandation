# API recommandation

Moteur de recommandation : l'orientation prédictive ! (plateforme JobIRL.com)
API flask sur docker - Moteur de recommandation basé sur le modèle RIASEC

# Modélisation RIASEC - JobIRL
Marc ALBERNHE @DataStratégie
Avril 2020

Datasource : Raw data from online personality tests https://openpsychometrics.org/_rawdata/

Contexte : la plateforme JobIRL, réseau d’orientation qui connecte les jeunes et les pros, aide les jeunes collégiens et lycéens dans leur recherche de parcours professionel, en les mettant en relation avec des professionnels. 

L'objectif de l'étude est de construire un modèle de recommendation pour orienter les jeunes dans leur recherche de filière et de métier.
Le modèle RIASEC est une théorie sur les carrières et les choix vocationnels qui s'appuie sur les types psychologiques. Il identifie 6 types de personnalités en milieu professionnel qui sont à mettre en lien avec les intérêts professionnels.

R = Réaliste
I = Investigateur
A = Artistique
S = Social
E = Entreprenant
C = Conventionnel

Les données : le dataset contient 145828 enregistrements, 93 colonnes 
Col 1-48 : le codage RIASEC se base sur 48 questions pondérées. Score de 1 à 5 = 1=Dislike, 3=Neutral, 5=Enjoy.
Col 52-62 : Ten Item Personality Inventory. Score de 1 à 7.
    TIPI1	Extraverted, enthusiastic.
    TIPI2	Critical, quarrelsome.
    TIPI3	Dependable, self-disciplined.
    TIPI4	Anxious, easily upset.
    TIPI5	Open to new experiences, complex.
    TIPI6	Reserved, quiet.
    TIPI7	Sympathetic, warm.
    TIPI8	Disorganized, careless.
    TIPI9	Calm, emotionally stable.
    TIPI10	Conventional, uncreative.

1. Extraverti(e), enthousiaste
2. Critique, agressif(ve)
3. Digne de confiance, autodiscipliné(e)
4. Anxieux(euse), facilement troublé(e)
5. Ouvert(e) à de nouvelles expériences, d’une personnalité complexe 
6. Réservé(e), tranquille
7. Sympathique, chaleureux(euse)
8. Désorganisé(e), négligent(e)
9. Calme, émotionnellement stable
10. Conventionnel(le), peu créatif(ve)

/ 30+ variables demographiques et de personalité.

# Dockerfile

