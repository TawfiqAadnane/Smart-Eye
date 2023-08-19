
import requests
import telegram


token = 'YOUR API'
chat_id = 'YOUR ID'


class TelegramBot:
    """Telegram Bot
    """
    
    def __init__(self, token, destinationID):
        self.token = token
        self.destinationID = destinationID
    
    def send_image(self, image_path, caption=''):
        # Create url
        url = f'https://api.telegram.org/bot{self.token}/sendPhoto'
        
        # Create json link with message
        data = {'chat_id': self.destinationID,
                'caption': caption}

        # POST the image
        response = requests.post(url, data, files={'photo': open(image_path, 'rb')})
        if response.status_code == 200:
            print('Image sent successfully')
        else:
            print('Failed to send Image:', response.text)
    
    def send_message(self, message):
        """ It takes the bot token, an ID destination (should be yours if you want to receive the message) and your message. The function
            interact with telebot API to send you a private message """
        # Create url
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        
        # Create message
        message = message
        
        # Create json link with message
        data = {'chat_id': self.destinationID, 'text': message}
        
        # POST the message
        requests.post(url, data)
    
    def handle_command(self, command):
        """Handle user commands and provide answers"""
        command = command.lower()

        if command == "/start":
            return "Welcome to the bot! How can I assist you?"

        if command == "/help":
            return "Here are the available commands:\n/start - Start the bot\n/help - Get help information\n/call - Call the Police🆘🆘\n/ - Get help information\n/alerte - Turn The Alerte On🚨🚨"

        if command == "/call":
            return "Calling The Police🆘🆘🆘!!!"
        
        if command == "/alerte":
            return "Turn On the Alerte System 🚨🚨🚨!!!"

        return "Sorry, I don't understand that command."
    
    def send_error_message(self, message):
        """ It takes the bot token, an ID destination (should be yours if you want to receive the message) and your message. The function
            interact with telebot API to send you a private message """
        # Create url
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        
        # Create message
        message = message
        
        # Create json link with message
        data = {'chat_id': self.destinationID, 'text': message}
        
        # POST the message
        requests.post(url, data)
    

