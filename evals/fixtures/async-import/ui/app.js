const rows = document.querySelector('#rows');
const status = document.querySelector('#status');
const message = document.querySelector('#message');
document.querySelector('#submit').addEventListener('click', async () => {
  message.textContent = '';
  try {
    const response = await fetch('/api/batches', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ requestId: crypto.randomUUID(), rows: JSON.parse(rows.value) })
    });
    const batch = await response.json();
    if (!response.ok) throw new Error(batch.error);
    status.textContent = 'Completed';
  } catch (error) {
    message.textContent = error.message;
  }
});
