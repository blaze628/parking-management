from flask import Flask, render_template, jsonify, request
import os  # ✅ Import os to read Render's provided PORT

app = Flask(__name__)

# Shared parking slots - this will reset if server restarts
available_slots = ['A1', 'A2', 'A3', 'B1', 'B2', 'C1']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-slots')
def get_slots():
    return jsonify({'slots': available_slots})

@app.route('/book-slot', methods=['POST'])
def book_slot():
    data = request.json
    slot = data.get('slot')
    if slot in available_slots:
        available_slots.remove(slot)
        return jsonify({'status': 'success', 'message': f'Slot {slot} booked'})
    return jsonify({'status': 'error', 'message': 'Slot not available'})

# ✅ Dynamic port binding required by Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render provides PORT dynamically
    app.run(host='0.0.0.0', port=port)

