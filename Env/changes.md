actions.py
---

Nel file  è stato aggiunto un array chiamato `TRAIN_MOVEMENT` che viene usato come lista di movimenti base per il train dell'AI.

tetris_env.py
---
Nel file è stata commentata la riga 115 e la riga 152 e sostituita con `return 0` perché il `return None` dava dei problemi di incompatibilità coi dati analizzati dalla libreria dell'intelligenza artificiale.

La riga 245 è stata commentata perché l'oggetto  `statistics=self._statistics` contiene un dict, ma essendo già dentro  dava dei problemi di incompatibilità coi dati analizzati dalla libreria dell'intelligenza artificiale.