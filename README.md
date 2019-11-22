**Tesi Mattia Polticchia**
---
---

Presentazione
---
Git fatto per tenere conto della mia tesi.
L'argomento della tesi è la creazione di un'intelligenza artificiale che tramite il reinforcement learning impari a giocare a tetris.
Il punto focale è riuscire a farle imparare a giocare dandole delle limitate informazioni sull'ambiente.
L'ambiente utilizzato è sviluppato tramite OpenAI e si chiama gym-tetris
a cui sono state applicate alcune modifiche per aumentare la compatibilità con l'AI. 
L'AI è stata implementata in Keras-rl libreria sviluppata tramite Keras contentente i principali algoritmi di apprendimento per RL.

I dati che vengono passati all'AI sono:
* current piece
* number of lines
* score
* next piece
* board height


Bug e problemi
---
Abbiamo dei problemi di: 
`[Tensorflow 2.0] AttributeError: Tensor.op is meaningless when eager execution is enabled`
Una possibile soluzione è questo `train_interval=4` messo nella creazione dell' DQNAgent.

Possibile step, creare una funzione che crei dei grafici coi dati dei vari train. Potrebbe essere interessante da mostrare nella tesi.

---

> A quanto pare c'è una montagna di roba nelle pull e nelle issue di github che va accuratamente osservata.

Modifiche nel tempo
---
* Cambiata la policy dopo una selezione fatta seguendo un articolo su un sito 
specialistico. Ritrovare il sito ( controllare telegram )

* Rimossi alcuni parametri nella creazione del DQNAgent perché superflui in quanto già presenti nella dichiarazione dalla classe. Ha senso metterli solo  se si vogliono diversi valori rispetto agli standard.

---
Rete neurale
* Aggiunto il valore di dropout per evitare l'overfitting. Questo ha effettivamente portato a dei miglioramenti in tempo e in quantità di punti.
>_Paper di 30 pagine da leggere - Inserire il titolo_
* Modificata la struttura dei nodi e la dichiarazione dell'attivatore

from :
```
agent.add(Dense(16))
agent.add(Activation('relu'))
```
to : 

 `model.add(Dense(16, activation='relu'))`


---
Link vari
* Creare un piccolo file log delle modifiche della gym-tetris che sta subendo sporadiche modifiche nel tempo ma non vengono segnalate quasi da nessuna parte.

> Controllare i tetris_env i return.
> Il dict che era nelle info è stato commentato -> spiegare perché

* Aggiungere da qualche parte tutta la miriade di link che sono su telegram in modo da averli pronti per la bibliografia e le note
