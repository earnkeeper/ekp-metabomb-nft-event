from features.stats.ui.cum_sold_row import cum_sold_row
from features.stats.ui.sold_row import sold_row
from features.stats.ui.uptake_row import uptake_row
from sdk.components import (Badge, Button, Chart, Col, Column, Container,
                            Datatable, Div, Form, Icon, Row, Select, Span,
                            collection, commify, documents, ekp_map,
                            format_currency, format_template, is_busy,
                            json_array, sort_by, switch_case)


def page(chart_collection, uptake_collection):
    return Container(
        children=[
            title_row(),
            uptake_row(uptake_collection),
            sold_row(chart_collection),
            cum_sold_row(chart_collection),
        ]
    )


def title_row():
    return Row(
        children=[
            Col(
                children=[Icon("sunset")],
                class_name='col-auto pr-0'
            ),
            Col(
                children=[
                    Span("NFT Event Stats", "font-medium-3")
                ]
            )
        ],
        class_name="mb-2"
    )
