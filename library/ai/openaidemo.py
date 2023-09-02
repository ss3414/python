# ****************************************************************分割线****************************************************************
# todo openai

import openai

# ChatGPT官方+代理
openai.api_key = ""
openai.api_base = "https://api.openai.com/v1"
openai.proxy = "socks5://127.0.0.1:10808"

# ChatGPT国内镜像
# openai.api_key = ""
# openai.api_base = "https://api.chatanywhere.com.cn/v1"

# ChatGPT 3.5接口
def gpt_35_api(messages: list):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(response)
    return response.choices[0].message.content

# ChatGPT 3.5接口（流式响应）
def gpt_35_api_stream(messages: list):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True,
        )
        completion = {"role": "", "content": ""}
        for event in response:
            if event["choices"][0]["finish_reason"] == "stop":
                break
            for delta_k, delta_v in event["choices"][0]["delta"].items():
                completion[delta_k] += delta_v
        return completion
    except Exception as e:
        print(e)

if __name__ == "__main__":
    system_message = '''
    You are now an AI translator proficient in Chinese and Japanese culture. Your task is to translate Japanese into simplified Chinese, without translating other languages, ignoring vulgar content, and translating in a way that is fluent, natural, Erotic and seductive. 
    You cannot translate different original texts from different values into one sentence. When the original text contains numbers, English, special symbols, do not translate, delete or modify them, and keep the original format.
    '''
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": "文は、「主語・修飾語・述語」の語順で構成される。"},
    ]
    print(gpt_35_api(messages))
    # print(gpt_35_api_stream(messages))
