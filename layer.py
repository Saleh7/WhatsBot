from yowsup.layers                                      import YowLayerEvent
from yowsup.layers.auth                                 import YowAuthenticationProtocolLayer
from yowsup.layers.interface                            import YowInterfaceLayer                   # Reply to the message
from yowsup.layers.interface                            import ProtocolEntityCallback          # Reply to the message
from yowsup.layers.network                              import YowNetworkLayer
from yowsup.layers.protocol_iq.protocolentities         import IqProtocolEntity
from yowsup.layers.protocol_messages.protocolentities   import TextMessageProtocolEntity          # Body message
from yowsup.layers.protocol_presence.protocolentities   import AvailablePresenceProtocolEntity   # Online
from yowsup.layers.protocol_presence.protocolentities   import UnavailablePresenceProtocolEntity # Offline
from yowsup.layers.protocol_presence.protocolentities   import PresenceProtocolEntity         # Name presence
from yowsup.layers.protocol_chatstate.protocolentities  import OutgoingChatstateProtocolEntity   # is writing, writing pause
from yowsup.common.tools                                import Jid  # is writing, writing pause

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self, messageProtocolEntity):
        namemitt = messageProtocolEntity.getNotify()
        message = messageProtocolEntity.getBody().lower().replace('\b', '').replace('\n', '').replace('\r', '')
        recipient = messageProtocolEntity.getFrom()
        textmsg = TextMessageProtocolEntity

        if 'hello' in message:
            answer = "Hi {}, How can i help you today".format(namemitt)
            self.toLower(textmsg(answer, to=recipient))
            print("Reply %s to %s" % (message, recipient))
