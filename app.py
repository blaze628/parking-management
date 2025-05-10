from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for slots
slots = {
    'A1': 'available',
    'A2': 'available',
    'A3': 'booked',
    'A4': 'available',
    'B1': 'booked',
    'B2': 'available'
}

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Slots availability page
@app.route('/slots')
def slots_view():
    return render_template('slots.html', slots=slots)

# Booking page
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        slot = request.form['slot']
        vehicle_number = request.form['vehicle_number']
        date = request.form['date']
        
        # Update slot as booked
        if slots.get(slot) == 'available':
            slots[slot] = 'booked'
            return redirect(url_for('confirmation', slot=slot, vehicle_number=vehicle_number, date=date))
        else:
            return "Slot already booked!", 400

    available_slots = [slot for slot, status in slots.items() if status == 'available']
    return render_template('booking.html', available_slots=available_slots)

# Confirmation page
@app.route('/confirmation')
def confirmation():
    slot = request.args.get('slot')
    vehicle_number = request.args.get('vehicle_number')
    date = request.args.get('date')
    return render_template('confirmation.html', slot=slot, vehicle_number=vehicle_number, date=date)

if __name__ == '__main__':
    app.run(debug=True)
