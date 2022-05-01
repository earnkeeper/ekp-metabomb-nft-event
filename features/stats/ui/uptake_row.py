from sdk.components import (Column, Datatable, Fragment, Span, collection,
                            commify, documents, format_percent,
                            format_template, is_busy)


def uptake_row(collection_name):
    return Fragment([
        Span(
            format_template(
                "A total of {{ total_addresses}} addresses have participated in the sale. The table below shows which boxes they have been buying...",
                {
                    "total_addresses": commify(f'$["{collection_name}"][0].total_addresses')
                }
            )
        ),
        Datatable(
            class_name="mt-2",
            data=documents(collection_name),
            busy_when=is_busy(collection(collection_name)),
            pagination=False,
            show_export=False,
            columns=[
                Column(
                    id="title",
                    title="Box"
                ),
                Column(
                    id="addresses",
                    right=True,
                    width="160px"
                ),
                Column(
                    id="uptake",
                    title="% of Total",
                    right=True,
                    width="160px",
                    format=format_percent("$.uptake")
                ),
            ]
        )
    ])
