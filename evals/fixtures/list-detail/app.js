const state = RecordState.createState();
const list = document.querySelector('#list-view');
const records = document.querySelector('#records');
const group = document.querySelector('#group');
const detail = document.querySelector('#detail');
const nameInput = document.querySelector('#name');
let activeId = null;
let origin = null;

function renderList(scrollTop = 0) {
  group.value = state.group;
  const page = RecordState.pageRecords(state);
  records.replaceChildren(...page.rows.map(record => {
    const row = document.createElement('div');
    row.className = 'row';
    const text = document.createElement('span');
    text.textContent = record.name;
    const open = document.createElement('button');
    open.textContent = 'Open';
    open.setAttribute('aria-label', `Open record ${record.id}`);
    open.addEventListener('click', () => openDetail(record.id, true));
    row.append(text, open);
    return row;
  }));
  document.querySelector('#page-status').textContent = `Page ${state.page} of ${page.pages}`;
  document.querySelector('#previous').disabled = state.page === 1;
  document.querySelector('#next').disabled = state.page >= page.pages;
  list.hidden = false;
  records.scrollTop = scrollTop;
}

function openDetail(id, fromList) {
  const record = state.records.find(item => item.id === id);
  if (!record) return;
  origin = fromList ? { group: state.group, page: state.page, scrollTop: records.scrollTop } : null;
  activeId = id;
  nameInput.value = record.name;
  list.hidden = true;
  detail.hidden = false;
  nameInput.focus();
}

function leaveDetail(restoreOrigin) {
  detail.hidden = true;
  const target = restoreOrigin && origin ? origin : { group: 'all', page: 1, scrollTop: 0 };
  state.group = target.group;
  state.page = target.page;
  activeId = null;
  origin = null;
  renderList(target.scrollTop);
}

group.addEventListener('change', () => {
  state.group = group.value;
  state.page = 1;
  renderList();
});
document.querySelector('#previous').addEventListener('click', () => { state.page -= 1; renderList(); });
document.querySelector('#next').addEventListener('click', () => { state.page += 1; renderList(); });
document.querySelector('#save').addEventListener('click', () => {
  RecordState.rename(state, activeId, nameInput.value);
  leaveDetail(true);
});
document.querySelector('#cancel').addEventListener('click', () => leaveDetail(false));
document.querySelector('#close').addEventListener('click', () => leaveDetail(false));
detail.addEventListener('click', event => { if (event.target === detail) leaveDetail(false); });
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !detail.hidden) leaveDetail(false);
});

renderList();
const directId = Number(new URLSearchParams(location.search).get('record'));
if (directId) openDetail(directId, false);
