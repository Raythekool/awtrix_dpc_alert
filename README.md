# AWTRIX Protezione Civile Alert 🇮🇹

Blueprint per Home Assistant che mostra gli alert meteo della Protezione Civile italiana sul tuo dispositivo AWTRIX3.

## ⚠️ Requisiti

Prima di utilizzare questo blueprint, assicurati di avere:

1. **Home Assistant** con supporto per i blueprint
2. **AWTRIX 3** dispositivo configurato e connesso tramite MQTT
3. **Integrazione DPC Alert** installata da [caiosweet/Home-Assistant-custom-components-DPC-Alert](https://github.com/caiosweet/Home-Assistant-custom-components-DPC-Alert)

## 📦 Installazione

### Metodo 1: Import automatico (consigliato)

1. Clicca sul pulsante qui sotto per importare il blueprint:

   [![Apri la tua Home Assistant e mostra il blueprint import dialog con un URL specifico pre-compilato.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FRaythekool%2Fawtrix_dpc_alert%2Fblob%2Fmain%2Fawtrix_dpc_alert.yaml)

2. Clicca su "Import Blueprint" nella tua Home Assistant
3. Il blueprint sarà disponibile nelle tue automazioni

### Metodo 2: Import manuale

1. Vai in Home Assistant → Impostazioni → Automazioni e scene → Blueprint
2. Clicca sul pulsante "Import Blueprint"
3. Inserisci questo URL:
   ```
   https://github.com/Raythekool/awtrix_dpc_alert/blob/main/awtrix_dpc_alert.yaml
   ```
4. Clicca su "Preview" e poi "Import Blueprint"

### Metodo 3: File locale

1. Scarica il file `awtrix_dpc_alert.yaml`
2. Copia il file nella cartella `blueprints/automation/` della tua configurazione Home Assistant
3. Riavvia Home Assistant o ricarica le automazioni

## 🎨 Icone consigliate

Per una migliore visualizzazione, carica queste icone sul tuo AWTRIX:

- **dpc-idraulico** (49300) - Rischio idraulico (alluvioni, esondazioni)
- **dpc-temporali** (49299) - Rischio temporali
- **dpc-idrogeologico** (2289) - Rischio idrogeologico (frane, smottamenti)
- **dpc-warning** (16754) - Icona generica per alert

Puoi trovare altre icone su [developer.lametric.com/icons](https://developer.lametric.com/icons) o crearne di personalizzate.

### 📤 Script automatico per caricare le icone

Abbiamo incluso uno script che scarica automaticamente le icone consigliate da LaMetric e le carica sul tuo dispositivo AWTRIX.

**Utilizzo rapido:**

```bash
# Carica tutte le icone consigliate per DPC alerts
./upload_icons.sh 192.168.1.100 --default-icons

# Oppure usa direttamente Python
python3 upload_icons.py 192.168.1.100 --default-icons
```

Sostituisci `192.168.1.100` con l'indirizzo IP del tuo dispositivo AWTRIX.

**Opzioni avanzate:**

```bash
# Visualizza le icone predefinite
./upload_icons.sh --list-default

# Carica icone personalizzate
./upload_icons.sh 192.168.1.100 --icon my-icon 12345 --icon another-icon 67890

# Combina icone predefinite e personalizzate
./upload_icons.sh 192.168.1.100 --default-icons --icon custom-icon 99999
```

Lo script scarica automaticamente le icone da LaMetric e le carica sul tuo AWTRIX tramite HTTP. Non è necessario installare dipendenze aggiuntive, usa solo la libreria standard di Python 3.

## 🚀 Utilizzo

1. Vai in Home Assistant → Impostazioni → Automazioni e scene
2. Clicca su "Crea automazione" → "Usa un blueprint"
3. Seleziona "AWTRIX Protezione Civile Alert 🇮🇹"
4. Configura i parametri:
   - **Dispositivo AWTRIX**: Seleziona il tuo dispositivo AWTRIX
   - **Sensori DPC Alert**: Seleziona i sensori di allerta da monitorare
   - **Livello minimo di allerta**: Imposta il livello minimo (0-4)
     - 0 = Mostra tutte le allerte
     - 1 = Verde (Ordinaria criticità)
     - 2 = Giallo (Moderata criticità)
     - 3 = Arancione (Criticità elevata)
     - 4 = Rosso (Criticità estrema)
   - **Durata messaggio**: Tempo di visualizzazione in secondi (default: 20)
   - **Icone**: Personalizza gli ID delle icone per ogni tipo di rischio
5. Salva l'automazione

## 🎯 Funzionalità

- **Monitoraggio multi-sensore**: Supporta più sensori DPC contemporaneamente
- **Filtro per criticità**: Mostra solo le allerte sopra un certo livello
- **Colori automatici**: I messaggi sono colorati in base al livello di criticità
  - Verde: Ordinaria
  - Giallo: Moderata
  - Arancione: Elevata
  - Rosso: Estrema
- **Icone personalizzabili**: Usa icone diverse per ogni tipo di rischio
- **Multi-dispositivo**: Supporta più dispositivi AWTRIX contemporaneamente
- **Auto-clear**: Rimuove automaticamente gli alert quando non sono più attivi

## 🔧 Configurazione avanzata

### Personalizzare la durata dei messaggi

Il parametro "Durata messaggio" controlla quanto tempo l'alert rimane sullo schermo:
- `0` = usa il tempo globale del dispositivo AWTRIX
- `1-300` = secondi specifici (massimo 5 minuti)

### Usare icone personalizzate

Puoi usare qualsiasi icona da LaMetric o caricarne di personalizzate sul tuo AWTRIX. Basta inserire l'ID dell'icona nei campi corrispondenti.

## 📝 Note

- Il blueprint usa il modo "restart" per evitare duplicati quando arrivano più alert
- Gli alert vengono pubblicati su MQTT nel topic `custom/dpc_alert`
- Se ci sono più alert attivi, verranno mostrati in sequenza

## 🤝 Contributi

Contributi, segnalazioni di bug e richieste di funzionalità sono benvenuti! Sentiti libero di aprire una issue o una pull request.

## 📄 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

## 🙏 Crediti

- Integrazione DPC Alert: [caiosweet](https://github.com/caiosweet/Home-Assistant-custom-components-DPC-Alert)
- AWTRIX 3: [Blueforcer](https://github.com/Blueforcer/awtrix3)