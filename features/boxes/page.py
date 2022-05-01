from sdk.components import (Badge, Button, Col, Column, Container, Datatable,
                            Div, Form, Icon, Row, Select, Span, collection,
                            commify, documents, format_currency,
                            format_template, is_busy, switch_case)


def page():
    return Container(
        children=[
            title_row(),
            Span(
                class_name="d-block",
                content="The Metabomb Initial NFT Offering event starts at 1pm UTC - 30 Apr '22."
            ),
            Div(children=[], class_name="mt-1"),
            Span(
                class_name="d-block",
                content="Check your total costs below before buying!"
            ),
            table_row()
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
                    Span("Initial NFT Offering Event", "font-medium-3")
                ]
            )
        ],
        class_name="mb-2"
    )


def table_row():
    return Datatable(
        class_name="mt-2",
        data=documents('nft-event'),
        busy_when=is_busy(collection('nft-event')),
        pagination=False,
        show_export=False,
        columns=[
            Column(
                id="box",
                width="300px",
                cell=box_cell("$.box", "$.rarities")
            ),
            Column(
                id="quantity",
                title="Qty",
                right=True,
                min_width="160px",
                format=commify("$.quantity"),
                cell=qty_cell()
            ),
            Column(
                id="stake",
                title="Staking Ea.",
                right=True,
                width="200px",
                cell=staking_cell()
            ),
            Column(
                id="cost",
                title="Cost Ea.",
                right=True,
                width="200px",
                cell=cost_cell()
            ),
            Column(
                id="totalCost",
                title="Max Cost",
                right=True,
                width="200px",
                cell=total_cost_cell()
            ),
            Column(
                id="spacer",
                title="",
                width="10px"
            )

        ]
    )


def box_cell(name, rarities):
    return Row(
        children=[
            Col(
                class_name="col-12",
                children=[
                    Span(
                        class_name="font-medium-1 font-weight-bold",
                        content=name
                    )
                ]
            ),
            Col(
                class_name="col-auto font-small-1",
                children=[
                    Span(content=rarities)
                ]
            )
        ]
    )


def qty_cell():
    return Row(
        children=[
            Col(
                class_name="col-12",
                children=[
                    Span(
                        class_name="font-small-4 float-right",
                        content=format_template("{{ limit }} per wallet", {
                            "limit": "$.limit"
                        })
                    )
                ]
            ),
            Col(
                class_name="col-12 ",
                children=[
                    Span(
                        class_name="float-right font-small-1",
                        content=format_template("{{ quantity }} total", {
                            "quantity": commify("$.quantity")
                        })

                    )
                ]
            )
        ]
    )


def cost_cell():
    return Row(
        children=[
            Col(
                class_name="col-12",
                children=[
                    Span(
                        class_name="font-medium-1 font-weight-bold float-right",
                        content=format_template(
                            "{{ symbol }} {{ cost }}",
                            {
                                "symbol": "$.fiatSymbol",
                                "cost": commify("$.totalCost")
                            }
                        )
                    )
                ]
            ),
            Col(
                class_name="col-12",
                children=[
                    Span(
                        class_name="float-right font-small-2",
                        content=format_template(
                            "{{ symbol }} {{ cost }} + {{ symbol }} {{ stakeCost }}", {
                                "symbol": "$.fiatSymbol",
                                "cost": "$.cost",
                                "stakeCost": "$.stakeCost"
                            })

                    )
                ]
            )
        ]
    )


def total_cost_cell():
    return Row(
        children=[
            Col(
                class_name="col-12",
                children=[
                    Span(
                        class_name="font-medium-1 font-weight-bold float-right",
                        content=format_template(
                            "{{ symbol }} {{ cost }}",
                            {
                                "symbol": "$.fiatSymbol",
                                "cost": commify("$.maxCost")
                            }
                        )
                    )
                ]
            ),
            Col(
                class_name="col-12",
                children=[
                    Span(
                        class_name="float-right font-small-2",
                        content=format_template(
                            "{{ symbol }} {{ totalCost }} x {{ limit }}", {
                                "symbol": "$.fiatSymbol",
                                "totalCost": "$.totalCost",
                                "limit": "$.limit"
                            })

                    )
                ]
            )
        ]
    )


def staking_cell():
    return Row(
        children=[
            Col(
                class_name="col-12",
                children=[
                    Span(
                        class_name="font-medium-1 font-weight-bold float-right",
                        content=format_template(
                            "{{ symbol }} {{ cost }}",
                            {
                                "symbol": "$.fiatSymbol",
                                "cost": "$.stakeCost"
                            }
                        )
                    )
                ]
            ),
            Col(
                class_name="col-12",
                children=[
                    Span(
                        class_name="float-right font-small-2",
                        content=format_template(
                            "{{ staking }} MTB", {
                                "staking": commify("$.staking"),
                            })

                    )
                ]
            )
        ]
    )
