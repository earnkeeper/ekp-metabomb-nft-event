from features.stats.data.chart_documents import chart_documents
from features.stats.data.uptake_documents import uptake_documents
from features.stats.page import page

collection_name = "event-boxes"
chart_collection = "nft-event-chart"
uptake_collection = "nft-event-uptake"


class StatsController:
    def __init__(self):
        self.path = 'event-stats'

    def on_connect(self, sid):
        self.client_service.emit_menu(
            sid,
            'sunset',
            'NFT Event Stats',
            self.path
        )
        self.client_service.emit_page(
            sid,
            self.path,
            page(chart_collection, uptake_collection)
        )

    def on_client_state_changed(self, sid, event):

        self.client_service.emit_busy(sid, chart_collection)
        self.client_service.emit_busy(sid, uptake_collection)

        chart_docs = chart_documents()
        self.client_service.emit_documents(sid, chart_collection, chart_docs)

        uptake_docs = uptake_documents()
        self.client_service.emit_documents(sid, uptake_collection, uptake_docs)

        self.client_service.emit_done(sid, chart_collection)
        self.client_service.emit_done(sid, uptake_collection)
