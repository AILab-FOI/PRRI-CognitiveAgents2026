#!/usr/bin/env python3
from flask import Flask, render_template
from websocketserver import *
import _thread
from chatterbot import ChatBot
import argparse
from random import choice


app = Flask( __name__, static_folder='static' )

@app.route( '/' )
def home():
    return app.send_static_file('index.html')

@app.route( '/agent-exception' )
def agent_jura():
    return render_template( 'exception.html' )

@app.route( '/agent-engineer' )
def agent_engineer():
    return render_template( 'engineer.html' )

@app.route( '/agent-analyst' )
def agent_analyst():
    return render_template( 'analyst.html' )

@app.route( '/agent-cartographer' )
def agent_cartographer():
    return render_template( 'cartographer.html' )

@app.route( '/agent-narrator' )
def agent_cartographer():
    return render_template( 'narrator.html' )

@app.errorhandler( 404 )
def page_not_found( e ):
    return render_template( '404.html' ), 404

@app.errorhandler( 500 )
def server_error( e ):
    return render_template( '500.html' ), 500

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/media/<path:filename>')
def serve_media(filename):
    return app.send_static_file(f'media/{filename}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( "--trainException", const=True, nargs='?', type=bool, help="Train exception?")
    parser.add_argument( "--trainEngineer", const=True, nargs='?', type=bool, help="Train engineer?")
    parser.add_argument( "--trainAnalyst", const=True, nargs='?', type=bool, help="Train analyst?")
    parser.add_argument( "--trainCartographer", const=True, nargs='?', type=bool, help="Train cartographer?")
    parser.add_argument( "--trainNarrator", const=True, nargs='?', type=bool, help="Train narrator?")
    args = parser.parse_args()

    TRAIN_Exception = bool( args.trainException )
    TRAIN_Engineer = bool( args.trainEngineer )
    TRAIN_Analyst = bool( args.trainAnalyst )
    TRAIN_Cartographer = bool( args.trainCartographer )
    TRAIN_Narrator = bool( args.trainNarrator )

    engineer = ChatBot( 'Engineer', read_only=not TRAIN_Engineer, logic_adapters=LOGIC_ADAPTER, database=os.path.join(FOLDER, 'engineer_db.sqlite3') )
    analyst = ChatBot( 'Analyst', read_only=not TRAIN_Analyst, logic_adapters=LOGIC_ADAPTER, database=os.path.join(FOLDER, 'analyst_db.sqlite3') )
    cartographer = ChatBot( 'Cartographer', read_only=not TRAIN_Cartographer, logic_adapters=LOGIC_ADAPTER, database=os.path.join(FOLDER, 'cartographer_db.sqlite3') )
    exception = ChatBot( 'Exception', read_only=not TRAIN_Exception, logic_adapters=LOGIC_ADAPTER, database=os.path.join(FOLDER, 'exception_db.sqlite3'))
    narrator = ChatBot( 'Narrator', read_only=not TRAIN_Narrator, logic_adapters=LOGIC_ADAPTER, database=os.path.join(FOLDER, 'narrator_db.sqlite3'))

    if TRAIN_Engineer:
        from train_engineer import *
        train( engineer )
        sys.exit()
    
    elif TRAIN_Analyst:
        from train_analyst import *
        train( analyst )
        sys.exit()

    elif TRAIN_Cartographer:
        from train_cartographer import *
        train( cartographer )
        sys.exit()

    elif TRAIN_Exception:
        from train_exception import *
        train( exception )
        sys.exit()

    elif TRAIN_Narrator:
        from train_narrator import *
        train( narrator )
        sys.exit()

    server_engineer     = SimpleWebSocketServer( '0.0.0.0', 8009, EngineerController )
    server_analyst      = SimpleWebSocketServer( '0.0.0.0', 8010, AnalystController )
    server_cartographer = SimpleWebSocketServer( '0.0.0.0', 8011, CartographerController )
    server_exception    = SimpleWebSocketServer( '0.0.0.0', 8012, ExceptionController )
    server_narrator    = SimpleWebSocketServer( '0.0.0.0', 8013, NarratorController )

    _thread.start_new_thread( server_engineer.serveforever, () )
    _thread.start_new_thread( server_analyst.serveforever, () )
    _thread.start_new_thread( server_cartographer.serveforever, () )
    _thread.start_new_thread( server_exception.serveforever, () )
    _thread.start_new_thread( server_narrator.serveforever, () )

    app.run( host='0.0.0.0', debug=False )
