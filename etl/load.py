from database.models import FactTable


class Loader:
    async def insert(self, rows: list) -> None:
        """
        Insere um conjunto de fatos no banco.
        """
        events = []
     
        for row in rows:
            if row["value"] is None or row["value"] == 0:
                continue
            
            dimensions = await self.insert_dimensions(row)
      
            event = FactTable(
                metric=row["metric"],
                value=row["value"],
                **dimensions
            )
            
            events.append(event)

        await FactTable.bulk_create(events, batch_size=1000, ignore_conflicts=True)

    async def insert_dimensions(self, row):
        """
        Insere as dimensões no banco e retorna um mapa com os objetos ORM das dimensões.
        """
        from database.enums import DimensionEnum

        dimensions = row["dimensions"]
        map = {}
        dimensionsMap = DimensionEnum.get_ref_map()

        for key in dimensions:
            value = dimensions[key]

            if key not in dimensionsMap:
                continue

            enum = dimensionsMap[key]
            model = enum.model

            try:
                dim = await model.filter(nome=value).first()

                if dim is None:
                    dim = await model.create(nome=value)

                map[enum.column] = dim
            
            except Exception as e:
                print(f"Erro ao buscar ou criar {model.__name__} para {value}: {e}")

        return map

