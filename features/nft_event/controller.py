from features.nft_event.documents import documents
from features.nft_event.page import page
from sdk.coingecko import latest_price
from sdk.components import  selected_currency
from sdk.sockets import emit_busy, emit_documents, emit_done, emit_menu, emit_page


def on_client_state_changed_nft_event(sio, sid, event):
    emit_busy(sio, sid, "nft-event")
    emit_menu(sio, sid, 'nft-event', 'NFT Event', 'nft-event', 'sunset')
    emit_page(sio, sid, "nft-event", page())

    currency = selected_currency(event)
    usdRate = latest_price("usd-coin", currency["id"])
    mtbRate = latest_price("metabomb", currency["id"])

    docs = documents(usdRate, mtbRate, currency["symbol"])

    emit_documents(sio, sid, "nft-event", docs)
    emit_done(sio, sid, "nft-event")
