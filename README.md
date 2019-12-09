**Tesi Mattia Polticchia**
---
---

Presentazione
---
Git fatto per il versioning dei file della tesi.
L'argomento della tesi è la creazione di un'intelligenza artificiale che tramite il reinforcement learning impari a giocare a tetris.
Il punto focale è riuscire a farle imparare a giocare dandole delle limitate informazioni sull'ambiente.
L'ambiente utilizzato è sviluppato tramite OpenAI e si chiama gym-tetris
a cui sono state applicate alcune modifiche per aumentare la compatibilità con l'AI. 
L'AI è stata implementata in Keras-rl libreria sviluppata tramite Keras contentente i principali algoritmi di apprendimento per RL.

I dati che vengono passati all'Agente dopo ogni step sono:
### *observation / state*
Semplificazione delle righe della "mappa"

### *reward*
numerical reward given after some valuable actions. Like rows. 


### *done*
Bool value that represent if the play is finished or not

### *Info*
Dict contenente : 
* current piece
* number of lines
* score
* next piece
* board height


Bug e problemi
---
### Problemi passati: 
`[Tensorflow 2.0] AttributeError: Tensor.op is meaningless when eager execution is enabled`
Una possibile soluzione è questo `train_interval=4` messo nella creazione dell' DQNAgent.

### Attuali problemi:

È stata aperta un' issue sul git della libreria [keras-rl2](https://github.com/wau/keras-rl2/issues/7).
Si verifica che l'agente con dei nodi Conv2D ( _Convoluzionali a 2 dimensioni_ ) aggiunge inspiegabilmete un layer e la rete non riconosce l'input shape.

Aggiunta:
> A quanto pare c'è una montagna di roba nelle pull e nelle issue di github che va consultata.

Modifiche nel tempo
---
* Cambiata la policy dopo una selezione fatta seguendo un articolo su un sito 
specialistico.

* Rimossi alcuni parametri nella creazione dell' oggetto DQNAgent perché superflui in quanto già presenti nella dichiarazione dalla classe. Ha senso metterli solo  se si vogliono diversi valori rispetto agli standard. 

* Si è deciso di passare ad una rete neurale così formata: //inserire immagine.
Perché probabilmente alla rete viene passata anche l'attuale disposzione dei tetrimini e quindi è più probabile che l'elaborazione migliori notevolmente. 

---
Rete neurale
* Aggiunto il valore di dropout per evitare l'overfitting. Questo ha effettivamente portato a dei miglioramenti in tempo e in quantità di punti.
I nodi sono stati attualmente omessi per il cambio dell'architettura della rete. Verranno riaggiunti appena il problema sarà risolto.

* Modificata la struttura dei nodi e la dichiarazione dell'attivatore

from :
```
agent.add(Dense(16))
agent.add(Activation('relu'))
```
to : 

 `model.add(Dense(16, activation='relu'))`

Tetris Env
---
Il tetris ENV è stato omesso da questo git per comodità di manutenzione ma i file che sono stati modificati sono presenti nella cartella Env assieme ad un piccolo file che ne spiega le modifiche.