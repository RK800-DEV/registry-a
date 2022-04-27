import telepot

TOKEN       = '5254610019:AAFLGBtPwB4NRJd3zFpVEKmAjz6-rhwA8OY'
GROUP_ID    =  -1001660825886
TELEGRAM_BOT = telepot.Bot(TOKEN)


def send_message(text):
    TELEGRAM_BOT.sendMessage(GROUP_ID, text, parse_mode="Markdown")


def get_client_ip(request):
    """Get real client IP address."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip