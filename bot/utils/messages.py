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
            "👋 Приветствуем, {user_name}!\n\n"
            "🌍 Давайте начнем с выбора языка интерфейса. "
            "Вы всегда сможете изменить его позже в настройках.\n\n"
            "⬇️ Выберите один из доступных языков ниже:"
        ),
        "welcome_back": "👋 Рады видеть вас снова, {user_name}! Добро пожаловать обратно 😊",
        "lang_set": "✅ Язык успешно установлен: Русский 🇷🇺\nГотовы продолжать!",
        "lang_buttons": ["English 🇺🇸", "Русский 🇷🇺"],
        "ask_time": (
            "⏰ Хотите установить режим сна?\n"
            "🛌 Это поможет нам создавать для вас более персонализированный опыт."
        ),
        "start_buttons_ask_time": ["✔️ Да, конечно", "❌ Нет, позже"],
        "wake_time": "🌅 Во сколько вы обычно просыпаетесь?\nВведите время в формате HH:MM (например, 07:30):",
        "sleep_time": "🌙 Когда вы обычно ложитесь спать?\nВведите время в формате HH:MM (например, 23:00):",
        "time_error": "⚠️ Пожалуйста, используйте формат времени HH:MM, например, 07:30.",
        "saved": "✅ Отлично! Все данные сохранены 🎉",
        "menu_buttons": ["👤 Профиль", "📅 Мой День", "📝 Запись"],
        "menu": "📋 Главное меню:\nВыберите нужный раздел ниже ⬇️",
        "error_user_not_found": "⚠️ Мы не смогли найти ваш профиль. Пожалуйста, начните заново с команды /start.",
        "error_wake_time": "⚠️ Упс! Не удалось сохранить время пробуждения. Попробуйте еще раз.",
        "error_sleep_time": "⚠️ Упс! Не удалось сохранить время сна. Попробуйте еще раз.",
        "error_menu": "⚠️ Возникла ошибка при загрузке меню. Пожалуйста, повторите попытку позже.",
        "error": "❌ Произошла ошибка. Мы уже работаем над решением.",
    },

    LanguageEnum.ENGLISH: {
        "flag": "🇺🇸",
        "name": "English",
        "welcome": (
            "👋 Hello, {user_name}!\n\n"
            "🌍 Let's start by selecting your preferred language.\n"
            "You can always change it later in settings.\n\n"
            "⬇️ Please choose from the options below:"
        ),
        "welcome_back": "👋 Welcome back, {user_name}! Glad to see you again 😊",
        "lang_set": "✅ Language set successfully: English 🇺🇸\nLet’s continue!",
        "lang_buttons": ["English 🇺🇸", "Русский 🇷🇺"],
        "ask_time": (
            "⏰ Would you like to set your sleep schedule?\n"
            "💤 This helps us personalize your experience better."
        ),
        "start_buttons_ask_time": ["✔️ Yes, sure", "❌ No, maybe later"],
        "wake_time": "🌅 What time do you usually wake up?\nPlease enter time in HH:MM format (e.g., 07:30):",
        "sleep_time": "🌙 What time do you usually go to bed?\nPlease enter time in HH:MM format (e.g., 23:00):",
        "time_error": "⚠️ Invalid format. Use HH:MM (e.g., 07:30).",
        "saved": "✅ Done! Your data has been saved 🎉",
        "menu_buttons": ["👤 My Profile", "📅 My Day", "📝 Note"],
        "menu": "📋 Main Menu:\nChoose one of the sections below ⬇️",
        "error_user_not_found": "⚠️ We couldn't find your user profile. Please run /start again.",
        "error_wake_time": "⚠️ Failed to save wake-up time. Please try again.",
        "error_sleep_time": "⚠️ Failed to save sleep time. Please try again.",
        "error_menu": "⚠️ Could not load the menu. Please try again later.",
        "error": "❌ An unexpected error occurred. We’re working on fixing it.",
    }
}
