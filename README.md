# Recommender Systems
## Overview
This is a recommendation system that implements both collaborative and content based models. The dataset used is from LightFM. 4 different loss functions were used to see the difference in results 
## Results
### Warp  
User 3  
&nbsp;&nbsp;&nbsp;&nbsp;Known Positives:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Seven (Se7en) (1995)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contact (1997)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Starship Troopers (1997)  
    Recommended:  
        Scream (1996)  
        Starship Troopers (1997)  
        Game, The (1997)  
User 25  
    Known Positives:  
        Dead Man Walking (1995)  
        Star Wars (1977)  
        Fargo (1996)  
    Recommended:  
        English Patient, The (1996)  
        L.A. Confidential (1997)  
        Titanic (1997)  
User 450  
    Known Positives:  
        Contact (1997)  
        George of the Jungle (1997)  
        Event Horizon (1997)  
    Recommended:  
        Dante's Peak (1997)  
        Conspiracy Theory (1997)  
        Devil's Advocate, The (1997)
### Logistic
User 3  
    Known Positives:  
        Seven (Se7en) (1995)  
        Contact (1997)  
        Starship Troopers (1997)  
    Recommended:  
        Star Wars (1977)  
        Fargo (1996)  
        Return of the Jedi (1983)  
User 25
    Known Positives:
        Dead Man Walking (1995)
        Star Wars (1977)
        Fargo (1996)
    Recommended:
        Star Wars (1977)
        Fargo (1996)
        Return of the Jedi (1983)
User 450
    Known Positives:
        Contact (1997)
        George of the Jungle (1997)
        Event Horizon (1997)
    Recommended:
        Star Wars (1977)
        Fargo (1996)
        Return of the Jedi (1983)
### BPR
User 3
    Known Positives:
        Seven (Se7en) (1995)
        Contact (1997)
        Starship Troopers (1997)
    Recommended:
        Air Force One (1997)
        G.I. Jane (1997)
        Conspiracy Theory (1997)
User 25
    Known Positives:
        Dead Man Walking (1995)
        Star Wars (1977)
        Fargo (1996)
    Recommended:
        L.A. Confidential (1997)
        English Patient, The (1996)
        Chasing Amy (1997)
User 450
    Known Positives:
        Contact (1997)
        George of the Jungle (1997)
        Event Horizon (1997)
    Recommended:
        Conspiracy Theory (1997)
        G.I. Jane (1997)
        Air Force One (1997)
### Warp-Kos
User 3
    Known Positives:
        Seven (Se7en) (1995)
        Contact (1997)
        Starship Troopers (1997)
    Recommended:
        L.A. Confidential (1997)
        English Patient, The (1996)
        Cop Land (1997)
User 25
    Known Positives:
        Dead Man Walking (1995)
        Star Wars (1977)
        Fargo (1996)
    Recommended:
        Contact (1997)
        English Patient, The (1996)
        L.A. Confidential (1997)
User 450
    Known Positives:
        Contact (1997)
        George of the Jungle (1997)
        Event Horizon (1997)
    Recommended:
        Dante's Peak (1997)
        Peacemaker, The (1997)
        Cop Land (1997)
## Dependencies
Numpy - To install Numpy run sudo pip3 install numpy or sudo pip install numpy
## Usage
Run using python3 <path_to_repository>/movie_recommender.py or python <path_to_repository>/movie_recommender.py
## Credits
The credits for most of the code goes to Siraj Raval (||Source||)
