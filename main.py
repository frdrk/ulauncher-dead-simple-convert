
import json
import logging
from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from convertable_units import parse_units
from converter import convert_from_unit

logger = logging.getLogger(__name__)


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        

class KeywordQueryEventListener(EventListener):

    def parse_query(self, query):

        try:
            input_quantity = query.split(' ')[0]
            input_unit = ' '.join(query.split(' ')[1:]).strip().lower()

            quantity = input_quantity.replace(',', '.') # Replace any colons
            quantity = float(quantity) # String to float

            fromUnit = parse_units(input_unit)

            if fromUnit:
                convertedItems = convert_from_unit(fromUnit, quantity)
                return (convertedItems)
            else:
                logger.info("No matching unit found")
        
        except Exception:
            logger.error('Error message')


    
    def get_action_to_render(self, name, description, on_enter=None):
        item = ExtensionResultItem(name=name,
                                   description=description,
                                   icon= 'images/icon.png',
                                   on_enter=on_enter or DoNothingAction())

        return RenderResultListAction([item])
    


    def on_event(self, event, extension):

        query = event.get_argument()
        
        if query:
            try:
                convertedItems = self.parse_query(query)
                
                items = []
                for i in convertedItems:
                    items.append(ExtensionResultItem(icon='images/icon.png',
                                                    name=i,
                                                    #description='...',
                                                    on_enter=HideWindowAction()))

                return RenderResultListAction(items)
                
            
            except ParseQueryError:
                return self.get_action_to_render(name="Incorrect request",
                                                 description="For example 1 cup, 2,25 m, 4 oz or 62.5 C")


        else: 
            return self.get_action_to_render(name="Convert by typing an amount and a unit",
                                             description="For example 1 cup, 2,25 m, 4 oz or 62.5 C")

 
class ParseQueryError(Exception):
    pass


if __name__ == '__main__':
    DemoExtension().run()