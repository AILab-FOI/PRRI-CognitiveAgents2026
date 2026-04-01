from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from collections import OrderedDict
import sys, os
from time import sleep
import _thread
from chatterbot import ChatBot
from train_analyst import LOGIC_ADAPTER

FOLDER = os.path.dirname(os.path.abspath(__file__))


class EngineerController( WebSocket ) :
    def __init__( self, *args, **kwargs ):
        WebSocket.__init__( self, *args, **kwargs )
        self.BUFFER = [ 'tisina' ]
        self.LAST = None
        self.chatbot = ChatBot( 'Engineer', read_only=True, logic_adapters=LOGIC_ADAPTER, database=os.path.join( FOLDER, 'engineer_db.sqlite' ) )
        print( self.chatbot.get_response( 'tko te napravio' ) )
        _thread.start_new_thread( self.listen, () )
        
    def listen( self ):
        while True:
            try:
                if self.BUFFER:
                    self.BUFFER = list( OrderedDict.fromkeys( self.BUFFER ) )
                    print( 'BUFFER:', self.BUFFER )
                    cmd = self.BUFFER.pop()
                    print( 'Sending', str( cmd ) )
                    self.sendMessage( str( cmd ) )
                sleep( 0.1 )
            except Exception as e:
                print( 'NLPController: There was an error!', e )

    def handleMessage( self ):
        print( 'DATA:', self.data )
        if self.data != 'connect':
            print( 'ASKING CHATBOT' )
            result = self.chatbot.get_response( self.data )
            print( 'RESULT', result )
            if result != self.LAST:
                print( self.data, result )
                self.BUFFER.append( str( result ) )
                #self.sendMessage( self.data )
                self.LAST = result
        
    def handleConnected(self):
        print( self.address, 'connected' )

    def handleClose( self ):
        print( self.address, 'closed' )
        sys.exit()

class AnalystController( WebSocket ) :
    def __init__( self, *args, **kwargs ):
        WebSocket.__init__( self, *args, **kwargs )
        self.BUFFER = [ 'tisina' ]
        self.LAST = None
        self.chatbot = ChatBot( 'Analyst', read_only=True, logic_adapters=LOGIC_ADAPTER, database=os.path.join( FOLDER, 'analyst_db.sqlite' ) )
        print( self.chatbot.get_response( 'tko te napravio' ) )
        _thread.start_new_thread( self.listen, () )
        
    def listen( self ):
        while True:
            try:
                if self.BUFFER:
                    self.BUFFER = list( OrderedDict.fromkeys( self.BUFFER ) )
                    print( 'BUFFER:', self.BUFFER )
                    cmd = self.BUFFER.pop()
                    print( 'Sending', str( cmd ) )
                    self.sendMessage( str( cmd ) )
                sleep( 0.1 )
            except Exception as e:
                print( 'NLPController: There was an error!', e )

    def handleMessage( self ):
        print( 'DATA:', self.data )
        if self.data != 'connect':
            print( 'ASKING CHATBOT' )
            result = self.chatbot.get_response( self.data )
            print( 'RESULT', result )
            if result != self.LAST:
                print( self.data, result )
                self.BUFFER.append( str( result ) )
                #self.sendMessage( self.data )
                self.LAST = result
        
    def handleConnected(self):
        print( self.address, 'connected' )

    def handleClose( self ):
        print( self.address, 'closed' )
        sys.exit()

class CartographerController( WebSocket ) :
    def __init__( self, *args, **kwargs ):
        WebSocket.__init__( self, *args, **kwargs )
        self.BUFFER = [ 'tisina' ]
        self.LAST = None
        self.chatbot = ChatBot( 'Cartographer', read_only=True, logic_adapters=LOGIC_ADAPTER, database=os.path.join( FOLDER, 'cartographer_db.sqlite' ) )
        print( self.chatbot.get_response( 'tko te napravio' ) )
        _thread.start_new_thread( self.listen, () )
        
    def listen( self ):
        while True:
            try:
                if self.BUFFER:
                    self.BUFFER = list( OrderedDict.fromkeys( self.BUFFER ) )
                    print( 'BUFFER:', self.BUFFER )
                    cmd = self.BUFFER.pop()
                    print( 'Sending', str( cmd ) )
                    self.sendMessage( str( cmd ) )
                sleep( 0.1 )
            except Exception as e:
                print( 'NLPController: There was an error!', e )

    def handleMessage( self ):
        print( 'DATA:', self.data )
        if self.data != 'connect':
            print( 'ASKING CHATBOT' )
            result = self.chatbot.get_response( self.data )
            print( 'RESULT', result )
            if result != self.LAST:
                print( self.data, result )
                self.BUFFER.append( str( result ) )
                #self.sendMessage( self.data )
                self.LAST = result
        
    def handleConnected(self):
        print( self.address, 'connected' )

    def handleClose( self ):
        print( self.address, 'closed' )
        sys.exit()