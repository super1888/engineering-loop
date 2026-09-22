(function (root) {
  function createState() {
    return {
      group: 'all', page: 1, pageSize: 30,
      records: Array.from({ length: 180 }, (_, index) => ({
        id: index + 1, name: `Record ${index + 1}`, group: index % 2 ? 'B' : 'A'
      }))
    };
  }

  function pageRecords(state) {
    const filtered = state.records.filter(record => state.group === 'all' || record.group === state.group);
    const start = (state.page - 1) * state.pageSize;
    return { rows: filtered.slice(start, start + state.pageSize), pages: Math.ceil(filtered.length / state.pageSize) };
  }

  function rename(state, id, name) {
    const record = state.records.find(item => item.id === id);
    if (!record) throw new Error('Record not found');
    const value = name.trim();
    if (!value) throw new Error('Name is required');
    record.name = value;
  }

  const api = { createState, pageRecords, rename };
  if (typeof module !== 'undefined') module.exports = api;
  else root.RecordState = api;
})(globalThis);
