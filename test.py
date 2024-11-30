import eel
from g4f.client import Client
from config import OPENAI_API_KEY

eel.init("web", allowed_extensions=['.js', '.html'])
client = Client(api_key = OPENAI_API_KEY)

@eel.expose
def ask_gpt(promt: str)->str:
   #Открытие файла со всеми лекциями
    with open("database.txt") as file:
        database = file.readlines()
    file.close()

    #Вопрос к чатГПТ на основе этого материала
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Используя только эту информацию: {database} как милая девочка по имени Ким ответь на вопрос: {promt}"
            }]
        )
        return response.choices[0].message.content

    except Exception as err:
        return f"An error occurred:{err}"

eel.start("main_page.html", mode="browser", size=(700,700))