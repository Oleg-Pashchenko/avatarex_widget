import os

from misc import AvatarexSettings, read_avatarex_settings
from openai import OpenAI


def prompt_request(messages: list[dict], settings: AvatarexSettings) -> (str | None):
    try:
        client = OpenAI()
        messages.insert(0, {'role': 'system', 'context': settings.context})
        response = client.chat.completions.create(
            model="gpt-4-32k",
            messages=messages
        )
        return response.choices[0].message.content
    except:
        return None


def knowledge_request(messages: list[dict], settings: AvatarexSettings) -> (str | None):
    return None


def knowledge_mode(messages: list[dict]):
    try:
        avatarex_settings = read_avatarex_settings()
    except:
        return "Ошибка подключения к базе данных!"
    os.environ["OPENAI_API_KEY"] = avatarex_settings.api_token
    try:
        answer = knowledge_request(messages, avatarex_settings)
        if answer is None:
            answer = prompt_request(messages, avatarex_settings)
            if answer is None:
                answer = avatarex_settings.error_message
        return answer
    except:
        return avatarex_settings.error_message
