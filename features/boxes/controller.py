from features.boxes.documents import documents
from features.boxes.page import page
from sdk.coingecko import latest_price
from sdk.components import  selected_currency

collection_name = "event-boxes"

class BoxesController:
    def __init__(self):
        self.path = 'event-boxes'

    def on_connect(self, sid):
        self.client_service.emit_menu(
            sid,
            'sunset',
            'NFT Event Boxes',
            self.path
        )
        self.client_service.emit_page(
            sid,
            self.path,
            page(collection_name)
        )

    def on_client_state_changed(self, sid, event):
        self.client_service.emit_busy(sid, collection_name)

        currency = selected_currency(event)
        usdRate = latest_price("usd-coin", currency["id"])
        mtbRate = latest_price("metabomb", currency["id"])

        docs = documents(usdRate, mtbRate, currency["symbol"])

        self.client_service.emit_documents(sid, collection_name, docs)
        self.client_service.emit_done(sid, collection_name)
