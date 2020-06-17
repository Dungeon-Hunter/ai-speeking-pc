from chatterbot import ChatBot
#chatbot = ChatBot("Ron Obvious")
bot = chatBot("My Bot")


convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Durgesh',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
    'In which language you talk?',
    ' I mostly talk in english'
]

trainer = ListTrainer(bot)

trainer.train(convo)

answer = bot.get_response("what is your name?")
print(answer)
pip install chatterbot_corpus