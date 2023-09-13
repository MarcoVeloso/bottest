from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSpeakToAnAgent(Action):

    def name(self) -> Text:
        return "action_speak_to_an_agent"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        elementItem = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": "Speak to our agent",
                    "subtitle": "Nikki",
                    "image_url": "https://the1webchat.azurewebsites.net/image.png",
                    "buttons": [
                        {
                            "title": "call agent now",
                            "url": "tel://+66819341789",
                            "type": "web_url"
                        }
                    ]
                }
                ]
            }
        }
        dispatcher.utter_message(attachment=elementItem)


        return []

class ActionHi(Action):

    def name(self) -> Text:
        return "action_hi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Olá. Estou respondendo via CUSTOM ACTION!")        

        return []