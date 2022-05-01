from sdk.components import (Badge, Button, Chart, Col, Column, Container,
                            Datatable, Div, Form, Icon, Row, Select, Span,
                            collection, commify, documents, ekp_map,
                            format_currency, format_template, is_busy,
                            json_array, sort_by, switch_case)


def sold_row(collection_name):
    return Chart(
        title="NFT Purchases Over Time",
        type='area',
        busy_when=is_busy(collection(collection_name)),
        series=[
            {
                "name": 'All',
                "data": ekp_map(
                    sort_by(
                        json_array(documents(collection_name)),
                        '$.timestamp',
                    ),
                    ['$.timestamp_ms', '$.sold'],
                ),
            },
            {
                "name": 'Common',
                "data": ekp_map(
                    sort_by(
                        json_array(documents(collection_name)),
                        '$.timestamp',
                    ),
                    ['$.timestamp_ms', '$.common_sold'],
                ),
            },
            {
                "name": 'Premium',
                "data": ekp_map(
                    sort_by(
                        json_array(documents(collection_name)),
                        '$.timestamp',
                    ),
                    ['$.timestamp_ms', '$.premium_sold'],
                ),
            },
            {
                "name": 'Ultra',
                "data": ekp_map(
                    sort_by(
                        json_array(documents(collection_name)),
                        '$.timestamp',
                    ),
                    ['$.timestamp_ms', '$.ultra_sold'],
                ),
            },
        ],
        data=documents(collection_name),
        options={
            "chart": {
                "zoom": {
                    "enabled": False,
                },
                "toolbar": {
                    "show": False,
                },
                "stacked": False,
                "type": "line"
            },
            "markers": {
                "size": 0
            },
            "stroke": {
                "width": 1,
                "curve": "smooth"
            },
            "fill": {
                "type": 'gradient',
                "gradient": {
                    "shadeIntensity": 1,
                    "inverseColors": False,
                    "opacityFrom": 0.5,
                    "opacityTo": 0,
                    "stops": [0, 90, 100]
                },
            },
            "dataLabels": {
                "enabled": False,
            },
            "xaxis": {
                "type": "datetime",
                "labels": {
                    "formatter": {
                        "method": 'momentFormatFromUnix',
                        "params": ['$', 'Do MMM HH:mm'],
                    },
                },
            },
            "yaxis": {
                "labels": {
                    "formatter": commify('$'),
                },
            },
        },

    )
