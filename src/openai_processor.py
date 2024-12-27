import json
import openai
from typing import List, Dict
from config.settings import TEMPERATURE, MAX_COMPLETIONS_TOKEN, TOP_P, FREQUENCE_PENALTY, PRESENCE_PENALTY, LIMIT_COMMENT


class OpenAIProcessor:
    def __init__(self, openai_api_key: str, model: str, prompt: str):
        self.api_key = openai_api_key
        self.model = model
        self.prompt = prompt
        openai.api_key = self.api_key

    def generate_summary(self, contents: List[Dict]) -> List[Dict]:
        summaries_result = []
        for post in contents:
            try:
                response = openai.chat.completions.create(
                    model=self.model,
                    response_format={"type": "json_object"},
                    messages=[
                        {"role": "system", "content": self.prompt},
                        {"role": "user", "content": json.dumps(post, ensure_ascii=False)}
                    ],
                    temperature=TEMPERATURE,
                    max_tokens=MAX_COMPLETIONS_TOKEN,
                    top_p=TOP_P,
                    frequency_penalty=FREQUENCE_PENALTY,
                    presence_penalty=PRESENCE_PENALTY,
                    logit_bias={"1734": -100}
                )

                # Restituisce il contenuto generato
                summaries_result.append(response.choices[0].message.content)
            except Exception as e:
                print(f"Errore durante la generazione del riassunto: {e}")
                return {"error": str(e)}
        return summaries_result