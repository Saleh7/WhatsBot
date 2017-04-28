from yowsup.stacks                             import YowStackBuilder
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.stacks                             import YowStack
from yowsup.common                             import YowConstants
from yowsup.layers                             import YowLayerEvent
from yowsup                                    import env
from layer                                     import EchoLayer
from yowsup.layers.auth                        import YowCryptLayer, YowAuthenticationProtocolLayer, AuthError
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_presence           import YowPresenceProtocolLayer
from yowsup.env                                import YowsupEnv

CREDENTIALS = ("49xxxxxxxx", "=") # replace with your phone and password

if __name__== "__main__":
    stackBuilder = YowStackBuilder()
    stack = stackBuilder\
            .pushDefaultLayers(True)\
            .push(EchoLayer)\
            .build()
    stack.setCredentials(CREDENTIALS)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
    try:
        print("\nWhatsBot started. Phone number: %s" % CREDENTIALS[0])
        stack.loop(timeout = 0.5, discrete = 0.5)
    except AuthError as e:
        print("Auth Error: %s" % e.message)
    except KeyboardInterrupt:
        print("\nBot down now :)")
