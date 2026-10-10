## Contents

- [Task 1.5: Training](#task-15-training)
  - [Simple](#simple)
  - [Diag](#diag)
  - [Split](#split)
  - [Xor](#xor)

## Task 0.5: Visualization

Parameters: `weight_0_0 = -10.00`, `weight_1_0 = 0.05`, `bias_0 = 5.05`

![Manual classifier](images/manual_simple.png)

## Task 1.5: Training

### Simple
PTS: 150, HIDDEN: 2, RATE: 0.5, epochs: 500

![Simple](images/simple.png)

```
Epoch: 50/500, loss: 87.85243481548076, correct: 128
Epoch: 100/500, loss: 33.92893188066495, correct: 136
Epoch: 150/500, loss: 22.240405641661685, correct: 140
Epoch: 200/500, loss: 17.02661571716005, correct: 142
Epoch: 250/500, loss: 15.172817566147954, correct: 143
Epoch: 300/500, loss: 13.703393615469158, correct: 144
Epoch: 350/500, loss: 12.530247300877111, correct: 144
Epoch: 400/500, loss: 11.801990204071396, correct: 144
Epoch: 450/500, loss: 11.213035873906431, correct: 145
Epoch: 500/500, loss: 10.624253330757167, correct: 146
```

### Diag
PTS: 150, HIDDEN: 2, RATE: 0.5, epochs: 500

![Diag](images/diag.png)

```
Epoch: 50/500, loss: 27.86624859357958, correct: 140
Epoch: 100/500, loss: 7.314896280641765, correct: 150
Epoch: 150/500, loss: 4.0142539659231105, correct: 150
Epoch: 200/500, loss: 2.7827215351420502, correct: 150
Epoch: 250/500, loss: 2.1498261688578912, correct: 150
Epoch: 300/500, loss: 1.772286790620146, correct: 150
Epoch: 350/500, loss: 1.5237030605719915, correct: 150
Epoch: 400/500, loss: 1.3479470548814638, correct: 150
Epoch: 450/500, loss: 1.2166129739792795, correct: 150
Epoch: 500/500, loss: 1.1148580699633786, correct: 150
```


### Split
PTS: 150, HIDDEN: 3, RATE: 0.5, epochs: 1000

![Split](images/split.png)

```
Epoch: 50/1000, loss: 100.7568272385153, correct: 90
Epoch: 100/1000, loss: 100.63375721970303, correct: 90
Epoch: 150/1000, loss: 100.34842009055326, correct: 90
Epoch: 200/1000, loss: 99.78920257181174, correct: 90
Epoch: 250/1000, loss: 98.50894833893999, correct: 92
Epoch: 300/1000, loss: 78.31141684741638, correct: 120
Epoch: 350/1000, loss: 67.43119951458965, correct: 120
Epoch: 400/1000, loss: 62.9982997683521, correct: 116
Epoch: 450/1000, loss: 54.748352743544494, correct: 122
Epoch: 500/1000, loss: 56.94570654294341, correct: 116
Epoch: 550/1000, loss: 52.618945622375165, correct: 117
Epoch: 600/1000, loss: 45.02917152030735, correct: 125
Epoch: 650/1000, loss: 38.14378247787156, correct: 128
Epoch: 700/1000, loss: 38.47438657935344, correct: 128
Epoch: 750/1000, loss: 37.45599642603649, correct: 129
Epoch: 800/1000, loss: 29.583060997483667, correct: 135
Epoch: 850/1000, loss: 23.15337321475854, correct: 139
Epoch: 900/1000, loss: 19.962562307147287, correct: 139
Epoch: 950/1000, loss: 24.386833517211453, correct: 135
Epoch: 1000/1000, loss: 18.238902161680265, correct: 139
```


### Xor
PTS: 150, HIDDEN: 10, RATE: 0.5, epochs: 1000

![Xor](images/xor.png)

```
Epoch: 50/1000, loss: 59.68016546156006, correct: 122
Epoch: 100/1000, loss: 40.32903437614807, correct: 127
Epoch: 150/1000, loss: 39.05499572562959, correct: 134
Epoch: 200/1000, loss: 29.507884197262104, correct: 133
Epoch: 250/1000, loss: 26.528349563750325, correct: 136
Epoch: 300/1000, loss: 26.886855445415048, correct: 137
Epoch: 350/1000, loss: 20.520987821187624, correct: 140
Epoch: 400/1000, loss: 23.740820115780657, correct: 137
Epoch: 450/1000, loss: 19.217224202375373, correct: 141
Epoch: 500/1000, loss: 21.70045106595324, correct: 138
Epoch: 550/1000, loss: 22.440805555452396, correct: 137
Epoch: 600/1000, loss: 19.200101661737598, correct: 142
Epoch: 650/1000, loss: 17.684016514239108, correct: 143
Epoch: 700/1000, loss: 18.85071454755213, correct: 140
Epoch: 750/1000, loss: 22.51813442600012, correct: 138
Epoch: 800/1000, loss: 14.539553427206112, correct: 143
Epoch: 850/1000, loss: 15.232683983980474, correct: 142
Epoch: 900/1000, loss: 15.131250173443165, correct: 142
Epoch: 950/1000, loss: 11.62480764303702, correct: 148
Epoch: 1000/1000, loss: 12.087830106179059, correct: 145
```