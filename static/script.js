async function loadSlots() {
    const res = await fetch('/get-slots');
    const data = await res.json();
    const slots = data.slots;
    const slotDisplay = document.getElementById('slots');
    const slotSelect = document.getElementById('slotSelect');

    slotDisplay.textContent = slots.length > 0 ? slots.join(', ') : 'No Slots Available';
    slotSelect.innerHTML = slots.length > 0
        ? slots.map(s => `<option value="${s}">${s}</option>`).join('')
        : '<option disabled>No Slots Available</option>';
}

async function bookSlot(e) {
    e.preventDefault();
    const slot = document.getElementById('slotSelect').value;

    const res = await fetch('/book-slot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ slot })
    });

    const data = await res.json();
    alert(data.message);
    loadSlots();
}

document.getElementById('bookingForm').addEventListener('submit', bookSlot);
window.onload = loadSlots;
