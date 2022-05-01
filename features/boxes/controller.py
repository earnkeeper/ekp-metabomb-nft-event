from features.boxes.documents import documents
from features.boxes.page import page
from sdk.coingecko import latest_price
from sdk.components import  selected_currency
from sdk.sockets import emit_busy, emit_documents, emit_done, emit_menu, emit_page


def on_client_state_changed_boxes(sio, sid, event):
    emit_busy(sio, sid, "boxes")
    emit_menu(sio, sid, 'boxes', 'NFT Event', 'boxes', 'sunset')
    emit_page(sio, sid, "boxes", page())

    currency = selected_currency(event)
    usdRate = latest_price("usd-coin", currency["id"])
    mtbRate = latest_price("metabomb", currency["id"])

    docs = documents(usdRate, mtbRate, currency["symbol"])

    emit_documents(sio, sid, "boxes", docs)
    emit_done(sio, sid, "nft-event")
