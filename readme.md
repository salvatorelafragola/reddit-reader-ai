# README

## Descrizione dell'Applicazione
Reddit Reader AI è un applicazione che sintetizza i contenuti di un topic Reddit di uno o più specifici canali, tramite l'Intelligenza Artificiale. Il sommario dei contenuto verrà inviato tramite mail all'utente desiderato.

Requisiti minimi: Python >= 3.11
## Configurazione dell'Applicazione

Per poter utilizzare l'applicazione, è necessario configurare i file `.env` e `settings.py` nella directory `config`.

### 1. Configurazione del file `.env`
Il file `.env` contiene le variabili di ambiente necessarie per il funzionamento dell'applicazione, come ad esempio chiavi API, credenziali di accesso e impostazioni sensibili.

#### Esempio di `.env`:
```
OPENAI_API_KEY="your_openai_api_key_here"
REDDIT_CLIENT_ID="insert_reddit_client_id"
REDDIT_CLIENT_SECRET="insert_reddit_client_secret"
SMPT_SERVER="smtp.your_email_provider.com"
MAIL="email"
USER_MAIL="your_email_username"
PASS_MAIL="your_email_password"
```
Assicurati di sostituire i valori di esempio con quelli effettivi.

### 2. Configurazione del file `settings.py`
Il file `settings.py` nella directory `config` contiene configurazioni globali per l'applicazione, come parametri di completamento OpenAI o impostazioni specifiche del progetto.

#### Esempio di `settings.py`:
```python
# Configurazioni OpenAI
# REDDIT SECTION
REDDIT_CHANNELS = ["Python", "PHP", "OpenAI", "Symfony", "litigi", "ItaliaPersonalFinance", "ItalyInformatica"] #Puoi modificare i canali Reddit qui
LIMIT_POST = 4 # Limite dei post per canale
LIMIT_COMMENT = 3 # Limite commenti per post

# CHAT GPT SECTION
OPENAI_MODEL = "gpt-3.5-turbo" 
TEMPERATURE = 0.2
MAX_COMPLETIONS_TOKEN = 2048
TOP_P = 1
FREQUENCE_PENALTY = 1
PRESENCE_PENALTY = 2
MAIL_TO_SEND_SUMMARIES = "INSERT-MAIL" #Inserisci la mail a cui inviare la newsletter
```
Modifica questi valori secondo le tue necessità.

### 3. Installazione delle dipendenze
Assicurati di avere Python installato sulla tua macchina. Per installare le dipendenze richieste, esegui il comando seguente:
```bash
pip install -r requirements.txt
```

### 4. Avvio dell'Applicazione
Una volta configurati i file necessari, puoi avviare l'applicazione eseguendo il file principale:
```bash
python reddit_reader_ai.py
```

## Test
Per eseguire i test, usa il comando seguente nella directory principale del progetto:
```bash
pytest tests/
```

Assicurati di avere `pytest` installato:
```bash
pip install pytest
```

# reddit-reader-ai
