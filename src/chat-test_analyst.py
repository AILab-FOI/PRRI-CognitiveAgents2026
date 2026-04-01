#!/usr/bin/env python3
import os
from chatterbot import ChatBot
from train_analyst import LOGIC_ADAPTER

FOLDER = os.path.dirname( os.path.abspath( __file__ ) )
analyst = ChatBot( 'Analyst', read_only=True, logic_adapters=LOGIC_ADAPTER, database=os.path.join( FOLDER, 'analyst_db.sqlite3' ) )
print( 'Alien Analyst Here' )

while True:
    print( analyst.get_response( input( '> ' ) ) )    
    

