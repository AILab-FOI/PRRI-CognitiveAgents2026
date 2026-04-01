#!/usr/bin/env python3
import os
from chatterbot import ChatBot
from train_cartographer import LOGIC_ADAPTER

FOLDER = os.path.dirname( os.path.abspath( __file__ ) )
cartographer = ChatBot( 'Cartographer', read_only=True, logic_adapters=LOGIC_ADAPTER, database=os.path.join( FOLDER, 'cartographer_db.sqlite3' ) )
print( 'Alien Cartographer Here' )

while True:
    print( cartographer.get_response( input( '> ' ) ) )    
    

