const assert = require('node:assert/strict');
const test = require('node:test');
const { createState, pageRecords, rename } = require('./state.cjs');

test('group filtering and pagination retain the page size', () => {
  const state = createState();
  state.group = 'A';
  state.page = 2;
  const page = pageRecords(state);
  assert.equal(page.pages, 3);
  assert.equal(page.rows.length, 30);
  assert.equal(page.rows[0].id, 61);
  assert.ok(page.rows.every(row => row.group === 'A'));
});

test('save changes only the selected name and validates input', () => {
  const state = createState();
  rename(state, 17, ' Updated name ');
  assert.equal(state.records[16].name, 'Updated name');
  assert.equal(state.records[15].name, 'Record 16');
  assert.throws(() => rename(state, 17, ' '), /required/);
});
