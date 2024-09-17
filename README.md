# What is it?

A multimodal german tutor is meant to be an 'experimental' dialog game which teaches you german in a gamified manner. This project should not be taken seriously since its meant to be a fun exploration into games, RL and multimodal language models.

## Example
An example scenario is where the player is asked to fulfill an objective by conversing in german:
```
Order an espresso with two packets of sugar
``` 
Then the player converses with barista person in german to accomplish the objective:
```
Barista> Hallo wie geht es dir!
Player> Alles gut! und du?
Barista> Ich Auch! was möchten sie?
Player> Ich möchte ein espresso mit zwei zucker bitte.
Barista> das ist alles
Player> Ja
Barista> perfekt
```

# Design

## Actors


### Imitator
Actor which takes up the role of someone who talks to the player. In our example above Barista lady is the Imitator.

### Player
Actor which talks to the Imitator to complete an objective. For ex: Player which talks to the barista lady to order espresso.

### Tutor
Actor which helps out Player when they are stuck. Also, they correct the mistakes and suggest improvements.



# Installation 

## Mac 

### Install Audio processing related dependencies
```
brew install portaudio
```

### Install library requirements
```
pip install -r requirements.txt
```
