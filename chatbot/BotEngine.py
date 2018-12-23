from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response

import os

chatbot = ChatBot(
    'qosbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': "I couldn't understand. Can you rephrase it for me?"
        }
    ],
    response_selection_method=get_random_response,
    tie_breaking_method="random_response"
)

chatbot.set_trainer(ChatterBotCorpusTrainer)
temp = [
    os.path.join(os.path.dirname(__file__), 'trailer.json')
]
chatbot.train(temp)
chatbot.read_only = True