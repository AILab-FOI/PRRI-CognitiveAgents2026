#!/usr/bin/env python3
import os
from chatterbot import ChatBot
from train_engineer import LOGIC_ADAPTER

FOLDER = os.path.dirname( os.path.abspath( __file__ ) )
engineer = ChatBot( 'Engineer', read_only=True, logic_adapters=LOGIC_ADAPTER, database=os.path.join( FOLDER, 'engineer_db.sqlite3' ) )
print( 'Alien Engineer Here' )

while True:
    print( engineer.get_response( input( '> ' ) ) )    
    

