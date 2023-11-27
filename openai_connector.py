import os

from misc import AvatarexSettings, read_avatarex_settings, get_execution_function, download_file, get_keywords_values, \
    get_answer_by_question
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
    except Exception as e:
        print(e)
        return None


def knowledge_request(messages: list[dict], settings: AvatarexSettings) -> (str | None):
    try:
        filename = download_file(settings.knowledge_link)
        func = get_execution_function(filename)
        response = get_keywords_values(messages[-1]['content'], func)
        if not response['is_ok'] or len(response['args']) == 0 or len(response['args']) > 5:
            return None
        return get_answer_by_question(response, filename)
    except Exception as e:
        print(e)
        return None


def knowledge_mode(messages: list[dict]):
    try:
        avatarex_settings = read_avatarex_settings()
    except:
        return "Ошибка подключения к базе данных!"
    os.environ["OPENAI_API_KEY"] = avatarex_settings.api_token
    try:
        answer = knowledge_request(messages, avatarex_settings)
        print("KR", answer)
        if answer is None:
            answer = prompt_request(messages, avatarex_settings)
            print('PR', answer)
            if answer is None:
                answer = avatarex_settings.error_message
        return answer
    except Exception as e:
        print('All exc', e)
        return avatarex_settings.error_message
