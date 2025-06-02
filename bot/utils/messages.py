from models.models import LanguageEnum

LANGUAGE_BUTTON_TO_ENUM: dict = {
    "Русский 🇷🇺": LanguageEnum.RUSSIAN,
    "English 🇺🇸": LanguageEnum.ENGLISH,
}

LANGUAGE_CONFIG: dict = {
    LanguageEnum.RUSSIAN: {
        "flag": "🇷🇺",
        "name": "Русский",
        "welcome": (
            "👋 Привет, {user_name}! Я Роки, твой напарник по СДВГ! 😎\n\n"
            "🌍 Давай начнём с выбора языка. Можешь сменить его в любой момент!\n\n"
            "⬇️ Выбери язык ниже:"
        ),
        "welcome_back": "🔥 Йо, {user_name}! Рад тебя видеть! Давай зажжём сегодня? 😊",
        "lang_set": "✅ Русский язык установлен! 🇷🇺 Погнали дальше!",
        "lang_buttons": ["English 🇺🇸", "Русский 🇷🇺"],
        "ask_time": (
            "⏰ Хочешь настроить режим дня?\n"
            "🛌 Это поможет Роки напоминать о задачах в твоём ритме!"
        ),
        "start_buttons_ask_time": ["✔️ Да, настроим!", "❌ Пропустить"],
        "wake_time": "🌅 Во сколько ты встаёшь? Напиши время в формате HH:MM (например, 07:30):",
        "sleep_time": "🌙 Когда ложишься спать? Введи время в формате HH:MM (например, 23:00):",
        "time_error": "⚠️ Ой, формат неправильный! Используй HH:MM, например, 07:30.",
        "saved": "🎉 Круто, всё сохранено! Теперь Роки знает! 🚀",
        "menu_buttons": ["👤 Профиль", "📅 Мой День", "📝 Заметки"],
        "menu": "📋 Йо, {user_name}! Что будем делать? 😎 Выбери раздел:",
        "error_user_not_found": "⚠️ Упс, не нашёл твой профиль. Начни заново с /start!",
        "error_wake_time": "⚠️ Не удалось сохранить время пробуждения. Давай ещё раз?",
        "error_sleep_time": "⚠️ Не сохранилось время сна. Попробуй снова!",
        "error_menu": "⚠️ Меню не загрузилось. Повтори через минуту, ок?",
        "error": "❌ Что-то пошло не так. Роки уже чинит, подожди чуток!",

        "morning_message": (
            "🌞 Йо, {user_name}! Доброе утро! 😎 Сегодня в плане: {task_text}\n"
            "{trial_status}Готов задать жару? /menu"
        ),
        "morning_no_task": (
            "🌞 Привет, {user_name}! Утро — время для подвигов! 😄 План пока пуст, "
            "добавь задачу, вроде 'Python 30 мин'! {trial_status}/menu"
        ),
        "trial_status_active": "🔔 Осталось {days_left} дней пробника! Подпишись за $12/мес и продолжай с Роки! 💸 ",
        "trial_status_expired": "⏰ Пробник кончился! 😔 Подпишись за $12/мес, чтобы не терять структуру: /menu ",
        "task_added": "🎉 Задача '{task_text}' в деле! Роки напомнит завтра в 10:00! 🚀",
        "task_list": "📋 Твои задачи, {user_name}:\n{tasks}\nДобавим ещё? /menu",
        "task_list_empty": "📋 Пока задач нет, {user_name}. Давай добавим 'Python 30 мин'? 😎 /menu",
        "achievement": "🏆 Вау, {user_name}! Ты получил ачивку '{achievement_name}'! Продолжай в том же духе! 🔥",
        "make_note": "✍️ Напиши заметку:",
        "back_button": "🔙 Назад"
    },
    LanguageEnum.ENGLISH: {
        "flag": "🇺🇸",
        "name": "English",
        "welcome": (
            "👋 Hey, {user_name}! I'm Rocky, your ADHD sidekick! 😎\n\n"
            "🌍 Let's pick a language to start. You can change it anytime!\n\n"
            "⬇️ Choose below:"
        ),
        "welcome_back": "🔥 Yo, {user_name}! Great to see you back! Ready to crush it? 😊",
        "lang_set": "✅ English set! 🇺🇸 Let’s roll!",
        "lang_buttons": ["English 🇺🇸", "Русский 🇷🇺"],
        "ask_time": (
            "⏰ Want to set your daily rhythm?\n"
            "🛌 This helps Rocky remind you of tasks at the right time!"
        ),
        "start_buttons_ask_time": ["✔️ Yes, let's do it!", "❌ Skip for now"],
        "wake_time": "🌅 What time do you wake up? Enter in HH:MM format (e.g., 07:30):",
        "sleep_time": "🌙 When do you go to bed? Enter in HH:MM format (e.g., 23:00):",
        "time_error": "⚠️ Oops, wrong format! Use HH:MM, like 07:30.",
        "saved": "🎉 Awesome, your schedule is saved! Rocky’s got you! 🚀",
        "menu_buttons": ["👤 My Profile", "📅 My Day", "📝 Notes"],
        "menu": "📋 Yo, {user_name}! What’s the plan? 😄 Pick a section:",
        "error_user_not_found": "⚠️ Can’t find your profile. Start over with /start!",
        "error_wake_time": "⚠️ Couldn’t save wake-up time. Try again?",
        "error_sleep_time": "⚠️ Sleep time didn’t save. One more try?",
        "error_menu": "⚠️ Menu didn’t load. Give it a sec and try again!",
        "error": "❌ Something broke. Rocky’s fixing it, hang tight!",

        "morning_message": (
            "🌞 Yo, {user_name}! Good morning! 😎 Today’s task: {task_text}\n"
            "{trial_status}Ready to rock? /menu"
        ),
        "morning_no_task": (
            "🌞 Hey, {user_name}! Morning vibes! 😄 Your plan’s empty, "
            "add a task like 'Python 30 min'! {trial_status}/menu"
        ),
        "trial_status_active": "🔔 {days_left} days left in your trial! Subscribe for $12/mo to keep Rocky! 💸 ",
        "trial_status_expired": "⏰ Trial’s over! 😔 Subscribe for $12/mo to stay on track: /menu ",
        "task_added": "🎉 Task '{task_text}' added! Rocky’ll remind you tomorrow at 10:00! 🚀",
        "task_list": "📋 Your tasks, {user_name}:\n{tasks}\nWanna add more? /menu",
        "task_list_empty": "📋 No tasks yet, {user_name}. How about 'Python 30 min'? 😎 /menu",
        "achievement": "🏆 Wow, {user_name}! You earned the '{achievement_name}' badge! Keep it up! 🔥",
        "make_note": "✍️ Write a note:",
        "back_button": "🔙 Back"
    }
}