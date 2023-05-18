import random

# Chatbot cevaplarının listesi
responses = {
    "Merhaba": ["Merhaba!", "Selam!", "Merhaba, nasıl yardımcı olabilirim?"],
    "Nasıl gidiyor?": ["İyiyim, sen nasılsın?", "Harika, sen nasılsın?"],
    "Teşekkürler": ["Rica ederim!", "Memnun oldum!", "Her zaman memnuniyetle yardımcı olurum."]
}

def chatbot_response(message):
    if message in responses:
        return random.choice(responses[message])
    else:
        return "Anlamadım, lütfen başka bir şey söyler misin?"

# Kullanıcının mesajını al
message = input("Kullanıcı: ")

# Chatbot cevabını yazdır
print("Chatbot: ")

