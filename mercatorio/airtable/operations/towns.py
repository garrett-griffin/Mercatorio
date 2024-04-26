from mercatorio.airtable.operation import SyncOperation

TABLE_NAME = "Towns"


class TownsSync(SyncOperation):
    """Syncs town data from the Mercatorio API to AirTable."""

    async def sync(self):
        table = self._get_table(TABLE_NAME)

        data = []
        for town in await self.api.towns.all():
            data.append(
                {
                    "id": town.id,
                    "name": town.name,
                    "location_x": town.location.x,
                    "location_y": town.location.y,
                    "region": town.region,
                    "capital": town.capital,
                }
            )
        self.client.upsert_records_by_field(table, "id", data)

    def __str__(self):
        return "Towns"