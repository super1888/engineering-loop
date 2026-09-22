from .storage import initialize


class ImportService:
    def __init__(self, db_path, processor=None):
        self.db_path = str(db_path)
        self.processor = processor or (lambda row: row['name'])
        initialize(self.db_path)

    def submit(self, request_id, rows):
        if not isinstance(request_id, str) or not request_id.strip():
            raise ValueError('requestId is required')
        if not isinstance(rows, list) or not 1 <= len(rows) <= 100:
            raise ValueError('rows must contain 1 to 100 entries')
        identities = set()
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get('rowId'), str) or not row['rowId'].strip():
                raise ValueError('rowId is required')
            if row['rowId'] in identities:
                raise ValueError('rowId must be unique')
            identities.add(row['rowId'])
            if not isinstance(row.get('name'), str) or not row['name'].strip():
                raise ValueError('name is required')
        raise NotImplementedError('submission persistence is not implemented')

    def snapshot(self, batch_id):
        raise KeyError(batch_id)

    def process_next(self):
        return False

    def retry(self, batch_id, request_id):
        raise NotImplementedError('retry is not part of revision 1')

    def records(self):
        return []
