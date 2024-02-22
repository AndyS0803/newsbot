import json
import threading

import telebot
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def task1():
    bot = telebot.TeleBot('7183034616:AAFT7Ul3Ev68jMysx7gYOTudXVpkDZcFRkE')

    def send_html_formatted_message(chat_id, formated_text):
        bot.send_message(chat_id, formated_text, parse_mode='HTML')

    html_formatted_text = """
    Привет!
    
    В этом канале вы можете посмотреть последние новости России и Мира.
    
    Из меню выберите желаемую сферу.
    """



    @bot.message_handler(commands=['start'])
    def handle_html_formatted_message(message):
        chat_id = message.chat.id
        send_html_formatted_message(chat_id, html_formatted_text)



    @bot.callback_query_handler(func=lambda call:True)
    def callback_it(call):
        a = call.message.text.split('\n')
        a = a[0]
        #print(a)
        if a == 'Новости IT':
            # it_ref = '/it'
            # reformat(it_ref)

            req_it = call.data.split('_')
            #print(req[0])

            if req_it[0] == 'unseen':
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif 'pagination' in req_it[0]:
                json_string_it = json.loads(req_it[0])
                count = json_string_it['CountPage']
                page = json_string_it['NumberPage']


                markup = InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
                if page == 1:
                    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                               InlineKeyboardButton(text=f'Вперёд --->',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
                elif page == count:

                    markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page - 1) + ",\"CountPage\":" + str(count) + "}"),
                               InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))
                else:
                    markup.add(InlineKeyboardButton(text=f'<--- Назад', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page-1) + ",\"CountPage\":" + str(count) + "}"),
                                   InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                                   InlineKeyboardButton(text=f'Вперёд -->', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}"))



                #bot.delete_message(call.message.chat.id, call.message.id)
                bot.edit_message_text(f'<b>{nazv_it}</b>\n\n'
                                           f'<i>{it_ogl[page-1]}</i>\n'
                                           f'<i>{it_text[page-1]}</i>\n'
                                           f'<i>{links_on_state[page-1]}</i>\n',
                                      parse_mode="HTML", reply_markup=markup, chat_id=call.message.chat.id,
                                      message_id=call.message.message_id)
        elif a == 'Новости Политики':
            req_polit = call.data.split('_')
            #print(req[0])

            if req_polit[0] == 'unseen':
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif 'pagination' in req_polit[0]:
                json_string_polit = json.loads(req_polit[0])
                count = json_string_polit['CountPage']
                page = json_string_polit['NumberPage']


                markup = InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
                if page == 1:
                    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                               InlineKeyboardButton(text=f'Вперёд --->',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
                elif page == count:
                    markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page - 1) + ",\"CountPage\":" + str(count) + "}"),
                               InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))
                else:
                    markup.add(InlineKeyboardButton(text=f'<--- Назад', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page-1) + ",\"CountPage\":" + str(count) + "}"),
                                   InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                                   InlineKeyboardButton(text=f'Вперёд -->', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}"))



                #bot.delete_message(call.message.chat.id, call.message.id)
                bot.edit_message_text(f'<b>{nazv_polit}</b>\n\n'
                                           f'<i>{polit_ogl[page-1]}</i>\n'
                                           f'<i>{polit_text[page-1]}</i>\n'
                                           f'<i>{links_politics_on_state[page-1]}</i>\n',
                                      parse_mode="HTML", reply_markup=markup, chat_id=call.message.chat.id,
                                      message_id=call.message.message_id)

        elif a == 'Новости Экономики':
            req_econom = call.data.split('_')
            #print(req[0])

            if req_econom[0] == 'unseen':
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif 'pagination' in req_econom[0]:
                json_string_econom = json.loads(req_econom[0])
                count = json_string_econom['CountPage']
                page = json_string_econom['NumberPage']


                markup = InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
                if page == 1:
                    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                               InlineKeyboardButton(text=f'Вперёд --->',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
                elif page == count:
                    markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page - 1) + ",\"CountPage\":" + str(count) + "}"),
                               InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))
                else:
                    markup.add(InlineKeyboardButton(text=f'<--- Назад', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page-1) + ",\"CountPage\":" + str(count) + "}"),
                                   InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                                   InlineKeyboardButton(text=f'Вперёд -->', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}"))


                #bot.delete_message(call.message.chat.id, call.message.id)
                bot.edit_message_text(f'<b>{nazv_econom}</b>\n\n'
                                           f'<i>{econom_ogl[page-1]}</i>\n'
                                           f'<i>{econom_text[page-1]}</i>\n'
                                           f'<i>{link_econom_on_state[page-1]}</i>\n',
                                      parse_mode="HTML", reply_markup=markup, chat_id=call.message.chat.id,
                                      message_id=call.message.message_id)
        elif a == 'Новости Красоты':
            req_beauty = call.data.split('_')
            # print(req[0])

            if req_beauty[0] == 'unseen':
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif 'pagination' in req_beauty[0]:
                json_string_beauty = json.loads(req_beauty[0])
                count = json_string_beauty['CountPage']
                page = json_string_beauty['NumberPage']

                markup = InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
                if page == 1:
                    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                               InlineKeyboardButton(text=f'Вперёд --->',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
                elif page == count:
                    markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page - 1) + ",\"CountPage\":" + str(count) + "}"),
                               InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))
                else:
                    markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page - 1) + ",\"CountPage\":" + str(count) + "}"),
                               InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                               InlineKeyboardButton(text=f'Вперёд -->',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))


                # bot.delete_message(call.message.chat.id, call.message.id)
                bot.edit_message_text(f'<b>{nazv_beauty}</b>\n\n'
                                      f'<i>{beaut_ogl[page - 1]}</i>\n'
                                      f'<i>{beaut_text[page - 1]}</i>\n'
                                      f'<i>{link_beaut_on_state[page - 1]}</i>\n',
                                      parse_mode="HTML", reply_markup=markup, chat_id=call.message.chat.id,
                                      message_id=call.message.message_id)

        elif a == 'Новости Спорта':

            req_sport = call.data.split('_')
            # print(req[0])

            if req_sport[0] == 'unseen':
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif 'pagination' in req_sport[0]:
                json_string_sport = json.loads(req_sport[0])
                count = json_string_sport['CountPage']
                page = json_string_sport['NumberPage']

                markup = InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
                if page == 1:
                    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                               InlineKeyboardButton(text=f'Вперёд --->',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
                elif page == count:
                    markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page - 1) + ",\"CountPage\":" + str(count) + "}"),
                               InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))
                else:
                    markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page - 1) + ",\"CountPage\":" + str(count) + "}"),
                               InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                               InlineKeyboardButton(text=f'Вперёд -->',
                                                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))

                # bot.delete_message(call.message.chat.id, call.message.id)
                bot.edit_message_text(f'<b>{nazv_sport}</b>\n\n'
                                      f'<i>{sport_ogl[page - 1]}</i>\n'
                                      f'<i>{sport_text[page - 1]}</i>\n'
                                      f'<i>{link_sport_on_state[page - 1]}</i>\n',
                                      parse_mode="HTML", reply_markup=markup, chat_id=call.message.chat.id,
                                      message_id=call.message.message_id)

    @bot.message_handler(func=lambda m: True, content_types=['text'])
    def start(m):
        #print(m)
        #print(type(m))
        if m.text == '/it':
            global it_ogl, it_text, links_on_state, nazv_it
            it_ogl = []
            it_text = []
            links_on_state = []
            
            service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument('--no-sandbox')

            # Задайте путь к директории, в которую вы хотите сохранить файлы
            # download_directory = 'E:\\PycharmProjects\\nlp_lab6_app'

            # Указываем директорию для загрузки файлов
            # option.add_experimental_option('prefs', {'download.default_directory': download_directory})

            driver = webdriver.Chrome(service=service, options=option)

            driver.get('https://habr.com/ru/news/')

            time.sleep(2)

            elems = driver.find_elements(By.CLASS_NAME, "tm-title__link")
            for i in elems:
                if len(it_ogl) < 10:
                    it_ogl.append(i.text)

            elems_text = driver.find_elements(By.CLASS_NAME, "article-formatted-body")
            for i in elems_text:
                if len(it_text) < 10:
                    it_text.append(i.text)

            elems_link = driver.find_elements(By.XPATH, "//a[@href]")
            for i in elems_link:
                st = i.get_attribute("href").split('/')
                if (('https://habr.com/ru/' in i.get_attribute("href") and 'news' in i.get_attribute("href") and len(st) >= 7 and
                    'comments' not in i.get_attribute("href")and i.get_attribute("href") not in links_on_state) and len(links_on_state) < 10):
                    #print(i.get_attribute("href"))
                    links_on_state.append(i.get_attribute("href"))

            driver.quit()


            nazv_it = 'Новости IT'

            page = 1
            count = len(it_ogl)


            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))


            bot.send_message(m.from_user.id, f'<b>{nazv_it}</b>\n\n'
                                             f'<i>{it_ogl[page-1]}</i>\n'
                                             f'<i>{it_text[page-1]}</i>\n'
                                             f'<i>{links_on_state[page-1]}</i>\n',
                             parse_mode="HTML", reply_markup=markup)
        elif m.text == '/policy':
            global polit_ogl, polit_text, links_politics_on_state, nazv_polit

            polit_ogl = []
            polit_text = []
            links_politics_on_state = []


            service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument('--no-sandbox')


            driver = webdriver.Chrome(service=service, options=option)

            driver.get('https://ria.ru/politics/?ysclid=lsrftj5mnc715817108')

            time.sleep(2)

            elems = driver.find_elements(By.CLASS_NAME, "list-item__content")
            for i in range(len(elems)):
                if i < 10:
                    #print(elems[i].text)
                    polit_ogl.append(elems[i].text)
                    polit_text.append('')


            elems_link = driver.find_elements(By.XPATH, "//a[@href]")
            for i in range(len(elems_link)):
                if ('https://ria.ru/' in elems_link[i].get_attribute("href") and 'html' in elems_link[i].get_attribute(
                        "href") and
                        elems_link[i].get_attribute("href") not in links_politics_on_state and len(
                            links_politics_on_state) < 10):
                    # print(elems_link[i].get_attribute("href"))
                    links_politics_on_state.append(elems_link[i].get_attribute("href"))


            driver.quit()

            nazv_polit = 'Новости Политики'

            page = 1
            count = len(polit_ogl)

            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

            bot.send_message(m.from_user.id, f'<b>{nazv_polit}</b>\n\n'
                                             f'<i>{polit_ogl[page - 1]}</i>\n'
                                             f'<i>{polit_text[page - 1]}</i>\n'
                                             f'<i>{links_politics_on_state[page - 1]}</i>\n',
                             parse_mode="HTML", reply_markup=markup)
        elif m.text == '/economy':
            global econom_ogl, econom_text, link_econom_on_state, nazv_econom
            econom_ogl = []
            econom_text = []
            link_econom_on_state = []

            service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument('--no-sandbox')

            driver = webdriver.Chrome(service=service, options=option)

            driver.get('https://www.rbc.ru/economics/?ysclid=lssvra1ptl265936439')

            time.sleep(2)

            elems = driver.find_elements(By.CLASS_NAME, "item__title-wrap")
            for i in range(len(elems)):
                if i < 10:
                    #print(elems[i].text)
                    econom_ogl.append(elems[i].text)
                    econom_text.append('')

            #print(econom_ogl)
            #print(econom_text)

            elems_link = driver.find_elements(By.XPATH, "//a[@href]")
            for i in range(len(elems_link)):
                if ('https://www.rbc.ru/rbcfreenews/' in elems_link[i].get_attribute(
                        "href") or 'https://www.rbc.ru/economics/' in elems_link[i].get_attribute("href") and
                    '?' not in elems_link[i].get_attribute("href")) and len(link_econom_on_state) <= 11:
                    # print(elems_link[i].get_attribute("href"))
                    link_econom_on_state.append(elems_link[i].get_attribute("href"))
            link_econom_on_state = link_econom_on_state[2:]

            driver.quit()

            nazv_econom = 'Новости Экономики'

            page = 1
            count = len(econom_ogl)

            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

            bot.send_message(m.from_user.id, f'<b>{nazv_econom}</b>\n\n'
                                             f'<i>{econom_ogl[page - 1]}</i>\n'
                                             f'<i>{econom_text[page - 1]}</i>\n'
                                             f'<i>{link_econom_on_state[page - 1]}</i>\n',
                             parse_mode="HTML", reply_markup=markup)
        elif m.text == '/beauty':

            global beaut_ogl, beaut_text, link_beaut_on_state, nazv_beauty
            beaut_ogl = []
            beaut_text = []
            link_beaut_on_state = []

            service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument('--no-sandbox')

            driver = webdriver.Chrome(service=service, options=option)

            driver.get('https://www.woman.ru/beauty/?ysclid=lsuhq6ym4c399787471')

            time.sleep(2)

            elems = driver.find_elements(By.CLASS_NAME, "announce-inline__title-link")
            for i in range(len(elems)):
                if len(beaut_ogl) < 10:
                    beaut_ogl.append(elems[i].text)
                    # print(elems[i].text)

            elems = driver.find_elements(By.CLASS_NAME, "announce-inline__description")
            for i in range(len(elems)):
                if len(beaut_text) < 10:
                    beaut_text.append(elems[i].text)
                    # print(elems[i].text)

            elems_link = driver.find_elements(By.XPATH, "//a[@href]")
            for i in range(len(elems_link)):
                st = elems_link[i].get_attribute("href")
                st = st.split('/')
                if len(st) > 5 and (('https://www.woman.ru/news/' in elems_link[i].get_attribute("href") or 'https://www.woman.ru/beauty/' in elems_link[i].get_attribute("href") or
                   'https://www.woman.ru/stars/' in elems_link[i].get_attribute("href") or 'https://www.woman.ru/health/' in elems_link[i].get_attribute("href")) and
                    len(link_beaut_on_state) < 10 and elems_link[i].get_attribute("href") not in link_beaut_on_state):
                    # print(elems_link[i].get_attribute("href"))
                    link_beaut_on_state.append(elems_link[i].get_attribute("href"))

            driver.quit()

            nazv_beauty = 'Новости Красоты'

            page = 1
            count = len(beaut_ogl)

            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

            bot.send_message(m.from_user.id, f'<b>{nazv_beauty}</b>\n\n'
                                             f'<i>{beaut_ogl[page - 1]}</i>\n'
                                             f'<i>{beaut_text[page - 1]}</i>\n'
                                             f'<i>{link_beaut_on_state[page - 1]}</i>\n',
                             parse_mode="HTML", reply_markup=markup)

        elif m.text == '/sport':

            global sport_ogl, sport_text, link_sport_on_state, nazv_sport
            sport_ogl = []
            sport_text = []
            link_sport_on_state = []

            service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument('--no-sandbox')

            driver = webdriver.Chrome(service=service, options=option)

            driver.get('https://www.rbc.ru/sport/?ysclid=lsujpg1ueg863708069')

            time.sleep(2)

            elems = driver.find_elements(By.CLASS_NAME, "item__title-wrap")
            for i in elems:
                if len(sport_ogl) < 10:
                    sport_ogl.append(i.text)
                    sport_text.append('')
                    # print(i.text)

            elems_link = driver.find_elements(By.XPATH, "//a[@href]")
            for i in range(len(elems_link)):
                if ('https://www.rbc.ru/sport/' in elems_link[i].get_attribute("href") and '?' not in elems_link[
                    i].get_attribute("href") and
                        len(link_sport_on_state) < 10):
                    # print(elems_link[i].get_attribute("href"))
                    link_sport_on_state.append(elems_link[i].get_attribute("href"))

            driver.quit()

            nazv_sport = 'Новости Спорта'

            page = 1
            count = len(sport_ogl)

            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

            bot.send_message(m.from_user.id, f'<b>{nazv_sport}</b>\n\n'
                                             f'<i>{sport_ogl[page - 1]}</i>\n'
                                             f'<i>{sport_text[page - 1]}</i>\n'
                                             f'<i>{link_sport_on_state[page - 1]}</i>\n',
                             parse_mode="HTML", reply_markup=markup)

        elif m.text == '/projects':
            bot.send_message(m.from_user.id, f'<b>Наши проекты</b>\n\n'
                                            f'<i>Загрузка медиа из соц.сетей @Download_Media_and_Audio_Bot</i>',
                             parse_mode="HTML")

    bot.polling(none_stop=True)


def task2():
    while True:

        global it_ogl, it_text, links_on_state, nazv_it

        it_ogl = []
        it_text = []
        links_on_state = []
        service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')


        driver = webdriver.Chrome(service=service, options=option)

        driver.get('https://habr.com/ru/news/')

        elems = driver.find_elements(By.CLASS_NAME, "tm-title__link")
        for i in elems:
            if len(it_ogl) < 10:
                it_ogl.append(i.text)

        elems_text = driver.find_elements(By.CLASS_NAME, "article-formatted-body")
        for i in elems_text:
            if len(it_text) < 10:
                it_text.append(i.text)

        elems_link = driver.find_elements(By.XPATH, "//a[@href]")
        for i in elems_link:
            st = i.get_attribute("href").split('/')
            if (('https://habr.com/ru/' in i.get_attribute("href") and 'news' in i.get_attribute("href") and len(st) >= 7 and
                'comments' not in i.get_attribute("href")and i.get_attribute("href") not in links_on_state) and len(links_on_state) < 10):
                #print(i.get_attribute("href"))
                links_on_state.append(i.get_attribute("href"))

        driver.quit()
        nazv_it = 'Новости IT'

        # return it_ogl, it_text, links_on_state, nazv_it
        time.sleep(1200)







def task3():
    while True:
        global polit_ogl, polit_text, links_politics_on_state, nazv_polit

        polit_ogl = []
        polit_text = []
        links_politics_on_state = []


        service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')


        driver = webdriver.Chrome(service=service, options=option)

        driver.get('https://ria.ru/politics/?ysclid=lsrftj5mnc715817108')

        elems = driver.find_elements(By.CLASS_NAME, "list-item__content")
        for i in range(len(elems)):
            if i < 10:
                #print(elems[i].text)
                polit_ogl.append(elems[i].text)
                polit_text.append('')


        elems_link = driver.find_elements(By.XPATH, "//a[@href]")
        for i in range(len(elems_link)):
            if ('https://ria.ru/' in elems_link[i].get_attribute("href") and 'html' in elems_link[i].get_attribute(
                    "href") and
                    elems_link[i].get_attribute("href") not in links_politics_on_state and len(
                        links_politics_on_state) < 10):
                # print(elems_link[i].get_attribute("href"))
                links_politics_on_state.append(elems_link[i].get_attribute("href"))


        driver.quit()

        nazv_polit = 'Новости Политики'

        time.sleep(1500)





def task4():
    while True:
        global econom_ogl, econom_text, link_econom_on_state, nazv_econom
        econom_ogl = []
        econom_text = []
        link_econom_on_state = []

        service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')

        driver = webdriver.Chrome(service=service, options=option)

        driver.get('https://www.rbc.ru/economics/?ysclid=lssvra1ptl265936439')

        time.sleep(2)

        elems = driver.find_elements(By.CLASS_NAME, "item__title-wrap")
        for i in range(len(elems)):
            if i < 10:
                #print(elems[i].text)
                econom_ogl.append(elems[i].text)
                econom_text.append('')

        #print(econom_ogl)
        #print(econom_text)

        elems_link = driver.find_elements(By.XPATH, "//a[@href]")
        for i in range(len(elems_link)):
            if ('https://www.rbc.ru/rbcfreenews/' in elems_link[i].get_attribute(
                    "href") or 'https://www.rbc.ru/economics/' in elems_link[i].get_attribute("href") and
                '?' not in elems_link[i].get_attribute("href")) and len(link_econom_on_state) <= 11:
                # print(elems_link[i].get_attribute("href"))
                link_econom_on_state.append(elems_link[i].get_attribute("href"))
        link_econom_on_state = link_econom_on_state[2:]

        driver.quit()

        nazv_econom = 'Новости Экономики'

        time.sleep(1800)

def task5():
    while True:
        global beaut_ogl, beaut_text, link_beaut_on_state, nazv_beauty
        beaut_ogl = []
        beaut_text = []
        link_beaut_on_state = []

        service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')

        driver = webdriver.Chrome(service=service, options=option)

        driver.get('https://www.woman.ru/beauty/?ysclid=lsuhq6ym4c399787471')

        time.sleep(2)

        elems = driver.find_elements(By.CLASS_NAME, "announce-inline__title-link")
        for i in range(len(elems)):
            if len(beaut_ogl) < 10:
                beaut_ogl.append(elems[i].text)
                # print(elems[i].text)

        elems = driver.find_elements(By.CLASS_NAME, "announce-inline__description")
        for i in range(len(elems)):
            if len(beaut_text) < 10:
                beaut_text.append(elems[i].text)
                # print(elems[i].text)

        elems_link = driver.find_elements(By.XPATH, "//a[@href]")
        for i in range(len(elems_link)):
            st = elems_link[i].get_attribute("href")
            st = st.split('/')
            if len(st) > 5 and (('https://www.woman.ru/news/' in elems_link[i].get_attribute("href") or 'https://www.woman.ru/beauty/' in elems_link[i].get_attribute("href") or
               'https://www.woman.ru/stars/' in elems_link[i].get_attribute("href") or 'https://www.woman.ru/health/' in elems_link[i].get_attribute("href")) and
                len(link_beaut_on_state) < 10 and elems_link[i].get_attribute("href") not in link_beaut_on_state):
                # print(elems_link[i].get_attribute("href"))
                link_beaut_on_state.append(elems_link[i].get_attribute("href"))

        driver.quit()

        nazv_beauty = 'Новости Красоты'

        time.sleep(2100)

def task6():
    while True:

        global sport_ogl, sport_text, link_sport_on_state, nazv_sport
        sport_ogl = []
        sport_text = []
        link_sport_on_state = []

        service = Service(executable_path='/root/parse_tg_bot/chromedriver-linux64/chromedriver')
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')

        driver = webdriver.Chrome(service=service, options=option)

        driver.get('https://www.rbc.ru/sport/?ysclid=lsujpg1ueg863708069')

        time.sleep(2)

        elems = driver.find_elements(By.CLASS_NAME, "item__title-wrap")
        for i in elems:
            if len(sport_ogl) < 10:
                sport_ogl.append(i.text)
                sport_text.append('')
                # print(i.text)

        elems_link = driver.find_elements(By.XPATH, "//a[@href]")
        for i in range(len(elems_link)):
            if ('https://www.rbc.ru/sport/' in elems_link[i].get_attribute("href") and '?' not in elems_link[
                i].get_attribute("href") and
                    len(link_sport_on_state) < 10):
                # print(elems_link[i].get_attribute("href"))
                link_sport_on_state.append(elems_link[i].get_attribute("href"))

        driver.quit()

        nazv_sport = 'Новости Спорта'

        time.sleep(2400)


if __name__ == "__main__":
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    t3 = threading.Thread(target=task3, name='t3')
    t4 = threading.Thread(target=task4, name='t4')
    t5 = threading.Thread(target=task5, name='t5')
    t6 = threading.Thread(target=task6, name='t6')
    t1.start()
    t2.start()
    time.sleep(60)
    t3.start()
    time.sleep(120)
    t4.start()
    time.sleep(180)
    t5.start()
    time.sleep(240)
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
