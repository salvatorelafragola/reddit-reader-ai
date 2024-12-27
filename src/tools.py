import json
import os
from typing import List


class Tools:
    @staticmethod
    def load_template(template_name):
        template_path = os.path.join("templates", template_name)
        with open(template_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def replace_html_content(template: str, placeholder: str, posts: list):
        content = ""
        for post in posts:
            post_deserialized = json.loads(post)
            # Genera i commenti
            comments = ""
            for comment in post_deserialized["sintesi_dei_commenti"]:
                comments += f"<li>{comment}</li>"

            # I contenuti dei post verranno aggiunti al template mail
            content += f"""
            <div class="post">
                <h2>{post_deserialized["canale"]}</h2>
                <div class="section">
                    <strong>Titolo:</strong>
                    <div class="title">{post_deserialized["titolo"]}</div>
                </div>
                <div class="section">
                    <strong>URL:</strong>
                    <a class="url" href="{post_deserialized["url"]}" target="_blank">{post_deserialized["url"]}</a>
                </div>
                <div class="section">
                    <strong>Sintesi del Post:</strong>
                    <div class="sintesi_del_post">{post_deserialized["sintesi_del_post"]}</div>
                </div>
                <div class="section">
                    <strong>Commenti:</strong>
                    <div class="sintesi_dei_comment">
                        <ul>
                            {comments}
                        </ul>
                    </div>
                </div>
                <div class="section">
                    <strong>Considerazioni:</strong>
                    <div class="considerazioni">{post_deserialized["considerazioni"]}</div>
                </div>
            </div>
            """

        return template.replace(placeholder, content)

