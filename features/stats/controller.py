from features.stats.data.chart_documents import chart_documents
from features.stats.data.uptake_documents import uptake_documents
from features.stats.page import page
from sdk.sockets import emit_busy, emit_documents, emit_done, emit_menu, emit_page

path = "event-stats"
chart_collection = "nft-event-chart"
uptake_collection = "nft-event-uptake"

def on_client_state_changed_stats(sio, sid, event):
    emit_busy(sio, sid, chart_collection)
    emit_busy(sio, sid, uptake_collection)
    
    emit_menu(sio, sid, path, 'NFT Event Stats', path, 'sunset')
    
    chart_docs = chart_documents()
    emit_documents(sio, sid, chart_collection, chart_docs)

    uptake_docs = uptake_documents()
    emit_documents(sio, sid, uptake_collection, uptake_docs)

    emit_page(sio, sid, path, page(chart_collection, uptake_collection))

    emit_done(sio, sid, chart_collection)
    emit_done(sio, sid, uptake_collection)
