# REDDIT SECTION
REDDIT_CHANNELS = ["Python", "PHP", "OpenAI", "Symfony", "litigi", "ItaliaPersonalFinance", "ItalyInformatica"]
LIMIT_POST = 4
LIMIT_COMMENT = 3

# CHAT GPT SECTION
OPENAI_MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.2
MAX_COMPLETIONS_TOKEN = 2048
TOP_P = 1
FREQUENCE_PENALTY = 1
PRESENCE_PENALTY = 2
PROMPT = '''
Sto lavorando a un progetto in cui devo creare un report dettagliato basato su dati JSON forniti da Reddit. Vorrei una sintesi ben organizzata per una mail.
Il tuo scopo è quello di leggere il post di ogni canale, creare una breve sintesi facendo attenzione a cogliere i punti più importanti per ognuno di essi. Inoltre, leggerai anche i commenti e cercherai di capire il sentiment degli utenti in merito al post.
Voglio che la sintesi sia organizzata per canale, includendo il titolo del post, un breve riassunto , una sezione con brevi riassunti dei commenti tradotti in italiano ed infine, fai delle considerazioni sull'argomento riflettendo sul perchè mi potrebbe essere utile o meno leggerlo, e menzionando le tecnologie utilizzate con una breve spiegazione di ognuna di esse (quest'ultima solo se si tratta di un canale di programmazione).
Il risultato dovrebbe apparire in un JSON così per ogni post del canale:
{
      "canale": "Python",
      "titolo": "Sunday Daily Thread: Su cosa lavorano tutti questa settimana?",
      "url": "ttps://www.reddit.com/r/Python/comments/1hjmlmy/sunday_daily_thread_whats_everyone_working_on/",
      "sintesi_del_post": "Il thread settimanale offre ai principianti la possibilità di fare domande su Python e ricevere supporto dalla community. Vengono condivisi link utili e consigli per risorse per principianti.",
      "sintesi_dei_commenti": [
       "Un utente condivide l'entusiasmo per il debugger di Python in Visual Studio Code.",
       "Altri commenti sono meno legati a domande, ma piuttosto a condivisioni di scoperte personali riguardo a strumenti di sviluppo."
      ],
      "considerazioni": "L'argomento è interessante perchè permette il confronto di vari progetti su Python. Gli strumenti menzionati sono: Visual studio code: Editor di codice"
}
'''

# GENERAL SETTING
LANGUAGE = "Italian"
MAIL_TO_SEND_SUMMARIES = "INSERT MAIL"
