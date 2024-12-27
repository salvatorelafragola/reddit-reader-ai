import json
import os
from config.settings import LIMIT_POST, LIMIT_COMMENT, REDDIT_CHANNELS, OPENAI_MODEL, PROMPT, MAIL_TO_SEND_SUMMARIES
from dotenv import load_dotenv
from src import RedditFetcher, OpenAIProcessor, Tools, EmailSender

load_dotenv()

reddit = RedditFetcher(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent="script:redditreaderAI:1.0",
    limit_posts=LIMIT_POST,
    limit_comments=LIMIT_COMMENT
)

openai_processor = OpenAIProcessor(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model=OPENAI_MODEL,
    prompt=PROMPT
)

posts = []

for channel in REDDIT_CHANNELS:
    posts.extend(reddit.get_posts_formatted_with_comments_by_channel(channel=channel))

summaries_generated = openai_processor.generate_summary(posts)

template_mail = Tools.load_template("newsletter_template.html")

final_html = Tools.replace_html_content(
    template_mail,
    "{content_placeholder}",
    summaries_generated
)


mail_sender = EmailSender(
    smtp_server=os.getenv('SMPT_SERVER'),
    port=int(os.getenv('SMTP_PORT_TLS')),
    email=os.getenv('MAIL'),
    username=os.getenv('USER_MAIL'),
    password=os.getenv('PASS_MAIL'),
)

mail_sender.send_mail(
    to=[MAIL_TO_SEND_SUMMARIES],
    subject="Reddit Daily Newsletter",
    body=final_html,
    is_html=True
)

print("END")
