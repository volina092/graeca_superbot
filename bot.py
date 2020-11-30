import telebot as tb
from telebot import types

TOKEN = ''

bot = tb.TeleBot(TOKEN) #имя бота: @graeca_superbot

ERR = 'δεν καταλαβαίνω =( ρώτα Μαρία, τι να κάνετε\n\n' + 'не понимаю =( спросите у Маши, что делать или просто скажите \"привет\"' 

IDs = {}
acts = {1: {'ru': 'магазин', 'el': 'το κατάστημα'},
           11: {'ru': 'яблоко', 'el': 'το μήλο'},    
           12: {'ru': 'расчёска', 'el': 'η χτένα'},    
           121: {'ru': 'сломать', 'el': 'να σπάστε'},    
           122: {'ru': 'отдать маме', 'el': 'να δώστε'},    
           1211: {'ru': 'да', 'el': 'ναι'},    
           12111: {'ru': 'да', 'el': 'ναι'},    
           12112: {'ru': 'нет','el': 'όχι'},    
           121121: {'ru': 'да', 'el': 'ναι'},    
           121122: {'ru': 'нет','el': 'όχι'},    
           1212: {'ru': 'нет', 'el': 'όχι'},    
           
           2: {'ru': 'кино', 'el': 'τo σινεμά'},    
           21: {'ru': 'на фильм', 'el': 'η φιλμ'},
           211: {'ru': 'да', 'el': 'ναι'},
           212: {'ru': 'нет', 'el': 'όχι'},
           22: {'ru': 'попкорн', 'el': 'ποπ κορν'},
           221: {'ru': 'съесть', 'el': 'να τρώτε'},
           222: {'ru': 'поделиться', 'el': 'να δώστε'},
           2221: {'ru': 'взять', 'el': ''},
           2222: {'ru': 'не брать', 'el': ''},
           22221: {'ru': 'пешком', 'el': 'με τα πόδια'},
           222211: {'ru': 'да', 'el': 'ναι'},
           2222111: {'ru': 'свитер', 'el': 'το πουλόβερ'},
           2222112: {'ru': 'джинсы', 'el': 'το τζιν'},
           222212: {'ru': 'нет', 'el': 'όχι'},
           22222: {'ru': 'такси', 'el': 'το ταξί'},
           222221: {'ru': 'да', 'el': 'ναι'},                
           222222: {'ru': 'нет', 'el': 'όχι'},
           9: {'ru': 'заново', 'el': 'ξανά'}
           }
texts = {0: {'ru': 'Начинаем веселье!\n\nЧем займётесь?\n\nПойдёте в магазин или в кино?',
             'el': 'Αρχίζουμε το κέφι!\n\nΤι θα κάνετε;\n\nΘα πάτε στο κατάστημα ή στον κινηματογράφο;'},
            1: {'ru': 'Вы в магазине. Что купите?',
                'el': 'Είστε στο κατάστημα. Τι να αγοράζετε;'},
            11: {'ru': 'Яблоко было отравлено. Вы мертвы =(',
                 'el': 'Το μήλο ήταν δηλητηριασμένο. Είστε νεκρός =('},
            12: {'ru': 'Что делать с расчёской? Сломать или отдать маме?',
                 'el': 'Τι να κάνετε με η χτένα; Να σπάστε ή να δώστε τη μετέρα σας;'},
            121: {'ru': 'Вы нашли бумажку, в ней написано подойти к вашему университету. Подойти?',
                  'el': 'Βρήκατε ένα κομμάτι χαρτί, λέει να προσεγγίσει το πανεπιστήμιο. Να έρθεις εδώ;'},
            122: {'ru': 'Ура! Вы победили!', 'el': 'Πολύ ωραία! Η νική!'},
            1211: {'ru': 'Вы видите драку. Вмешаетесь?', 'el': 'Βλέπετε τον καβγά. Συμμετέχετε;'},
            12111: {'ru': 'Вас избили, вы мертвы =(', 'el': 'Δέρσουν σας πολύ. Είστε νεκρός =('},
            12112: {'ru': 'Пойти на занятие по новогреческому?', 'el': 'Nα πάει να διδάξει νέα ελληνικά;'},
            121121: {'ru': 'Вы пришли на заняте, ура! Победа!', 'el': 'Είστε στο μάθημα. Πολύ ωραία! Η νική!'},
            121122: {'ru': 'Ваш преподаватель вас уничтожил =(', 'el': 'Ο δάσκαλός σας σας κατέστρεψε =('},
            1212: {'ru': 'Вы умерли от скуки =(', 'el': 'Πέθαναν από την πλήξη =('},
            
            2: {'ru': 'Вы в кинотеатре, пойдёте смотреть \"ΣΤΟ ΠΑΡΑ ΠΈΝΤΕ ΓΙΑ ΠΆΝΤΑ\" или купите попкорн',
                'el': 'Να πάμε στην πρεμιέρα "ΣΤΟ ΠΑΡΑ ΠΈΝΤΕ ΓΙΑ ΠΆΝΤΑ" ή να αγοράσετε ποπ κορν'},
            21: {'ru': 'В зале террористы, бежать?', 'el': 'Στην αίθουσα τρομοκράτες. Τρέχει; '},
            211: {'ru': 'Смерть =(', 'el': 'Ο θάνατος'},
            212: {'ru': 'Это была шутка. Поздравляем - это победа!', 'el': 'Αυτό ήταν ένα αστείο. Η νίκη!'},
            22: {'ru': 'Вы с другом. Съесть весь попкорн самому или поделиться с другом?',
                 'el': 'Είστε με τους φίλους σας. Να τρώτε όλα ή να δώστε στον φίλο;'},
            221: {'ru': 'Попкорн был отравлен, вы умерли =(', 'el': 'Είναι δηλητηριασμένo. Είστε νεκρός =('},
            222: {'ru': 'Друг даёт вам книгу почитать',
                  'el': 'Ο φίλος δίνει το βιβλίο να διαβάσετε'},
            2221: {'ru': 'Ура, вы стали умнее! Это победа!',
                   'el': 'Πολύ ωραία, είσαι έξυπνος! Η νική!'},
            2222: {'ru': 'Ладно, вы дурак, но игра продолжается\n\n' +
                   'Вам необходимо теперь попасть в магазин одежды. Пойдёте пешком или вызовете такси?',
                   'el': 'εντάξει, είσαι ανόητος, αλλά το παιχνίδι συνεχίζεται.\n\n' +
                   'Τώρα πρέπει να φτάσετε στο κατάστημα ρούχων. Πήγαινε με τα πόδια ή πάρτε ταξί;'},
            22221: {'ru': 'На вас напали, защищаться?', 'el': 'Σου επιτέθηκαν. Υπερασπίζω?'},
            222211: {'ru': 'Вы защитились и дошли до магазина. Что будете покупать? Ваш любимый синий свитер или',
                     'el': 'Υπερασπιστήκατε και φτάσατε στο κατάστημα. Τι θα αγοράσεις? Το αγαπημένο σας μπλε πουλόβερ ή κόκκινο τζιν;'},
            2222111: {'ru': 'По этому свитеру вас нашёл киллер и убил вас. Это конец.',
                      'el': 'Ο δολοφόνος σε βρήκε σε αυτό το πουλόβερ και σε σκότωσε. Αυτό είναι το τέλος'},
            2222112: {'ru': 'Джинсы отлично выглядят! Это победа!',
                      'el': 'Φαίνονται υπέροχα! Είναι νίκη!'},
            222212: {'ru': 'Ладно... Вас избили. Это конец.',
                     'el': 'Εντάξει ... χτύπησες. Αυτό είναι το τέλος.'},
            22222: {'ru': 'Вы попали в аварию. Вызвать скорую?',
                    'el': 'Βρίσκεστε σε ατύχημα. Καλέστε ένα ασθενοφόρο;'},
            222221: {'ru': 'Вы боролись за жизнь как лев. Это победа',
                     'el': 'Πολεμήσατε σαν λιοντάρι. Αυτή είναι μια νίκη!'},
            222222: {'ru': ' Вы погибли =(', 'el': 'Είστε νεκρός =('}}

nexts = {0: [1, 2],
         1: [11, 12],
         12: [121, 122],
         121: [1211, 1212],
         1211: [12111, 12112],
         12112: [121121, 121122],
         2: [21, 22],
         21: [211, 212],
         22: [221, 222],
         222: [2221, 2222],
         2222: [22221, 22222],
         22221: [222211, 222212],
         222211: [2222111, 2222112],
         22222: [222221, 222222]}

def make_keyboard(act_num, lang):
    keyboard = types.InlineKeyboardMarkup(); 
    keys = nexts[act_num]
    
    key_0 = types.InlineKeyboardButton(text = acts[keys[0]][lang], callback_data=keys[0])
    key_1 = types.InlineKeyboardButton(text = acts[keys[1]][lang], callback_data=keys[1])
    
    if lang == 'el': key_2 = types.InlineKeyboardButton(text = 'ru', callback_data='to_ru')
    else: key_2 = types.InlineKeyboardButton(text = 'el', callback_data='to_el') 
    
    keyboard.add(key_0, key_1, key_2) 
    return keyboard

def new_game_keyboard(act_num, lang):
    keyboard = types.InlineKeyboardMarkup();
    key_restart = types.InlineKeyboardButton(text = acts[9][lang], callback_data='new')
    if lang == 'el': key_2 = types.InlineKeyboardButton(text = 'ru', callback_data='to_ru_last')
    else: key_2 = types.InlineKeyboardButton(text = 'el', callback_data='to_el_last')    
    keyboard.add(key_restart, key_2)
    return keyboard

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    now_id = message.from_user.id
    print(str(now_id) +': ' + str(message.text))
    if message.text.lower() in ["\start", 'καλημέρα']:
        IDs[now_id] = ['el', 0]
        bot.send_message(now_id, 'για να παίξετε, γράψτε \"αρχίζω\"' +
                         '\n\nαν αργότερα θα θέλετε να παίξετε ακόμα μία φορά, γράψτε \"αρχίζω\"')
    elif message.text.lower() in ['привет', 'здраствуйте']:
        IDs[now_id] = ['ru', 0]             
        bot.send_message(now_id, 'чтобы начать игру, напишите \"начинаю\"' +
                         "\n\nесли позже вы захотите сыграть ещё раз, напишите \"начинаю\"")
    elif message.text.lower() in ['αρχίζω', 'начинаю']:
        if not now_id in IDs.keys(): IDs[now_id] = ['el', 0]
        bot.send_message(now_id, texts[IDs[now_id][1]][IDs[now_id][0]],
                         reply_markup = make_keyboard(0, IDs[now_id][0]))
    else:
        bot.send_message(now_id, ERR)
        
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    now_id = call.message.chat.id
    
    if call.data == 'to_el':
        IDs[now_id][0] = 'el'
        curr_text = texts[IDs[now_id][1]][IDs[now_id][0]]
        bot.send_message(now_id, text = curr_text,
                         reply_markup = make_keyboard(IDs[now_id][1], IDs[now_id][0]))
        return None
    elif call.data == 'to_ru':
        IDs[now_id][0] = 'ru'
        curr_text = texts[IDs[now_id][1]][IDs[now_id][0]]
        bot.send_message(now_id, text = curr_text,
                         reply_markup = make_keyboard(IDs[now_id][1], IDs[now_id][0]))
        return None
    elif call.data == 'to_el_last':
        IDs[now_id][0] = 'el'
        curr_text = texts[IDs[now_id][1]][IDs[now_id][0]]
        bot.send_message(now_id, text = curr_text,
                         reply_markup = new_game_keyboard(IDs[now_id][1], IDs[now_id][0]))
        return None
    elif call.data == 'to_ru_last':
        IDs[now_id][0] = 'ru'
        curr_text = texts[IDs[now_id][1]][IDs[now_id][0]]
        bot.send_message(now_id, text = curr_text,
                         reply_markup = new_game_keyboard(IDs[now_id][1], IDs[now_id][0]))
        return None
    
    if call.data == 'new':
        IDs[now_id][1] = 0
        bot.send_message(now_id, text = texts[IDs[now_id][1]][IDs[now_id][0]],
                         reply_markup = make_keyboard(IDs[now_id][1], IDs[now_id][0]))
        return None
    step = int(call.data)
    print(str(now_id) +': ' + str(step))
    
    IDs[now_id][1] = step
    if step in texts.keys():
        curr_text = texts[step][IDs[now_id][0]]
    if step in nexts.keys():
        bot.send_message(now_id, text = curr_text,
                         reply_markup = make_keyboard((step), IDs[now_id][0]))
    elif step in texts.keys():
        bot.send_message(now_id, curr_text,
                         reply_markup = new_game_keyboard((step), IDs[now_id][0]))
        return None 
    else: bot.send_message(now_id, ERR) 

bot.polling(none_stop=True, interval=0)
