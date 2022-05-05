from features.boxes.controller import BoxesController
from features.stats.controller import StatsController
from sdk.client_service import ClientService

client_service = ClientService(
    [
        BoxesController(),
        StatsController(),
    ]
)

if __name__ == '__main__':
    client_service.listen()
