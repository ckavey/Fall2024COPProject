import React, { useState } from 'react';
import axios from 'axios';

const Donations = () => {
    const [amount, setAmount] = useState('');
    const [message, setMessage] = useState('');
    const [responseMessage, setResponseMessage] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post('http://localhost:8000/api/donations/', {
                amount,
                message,
            });
            setResponseMessage('Thank you for your donation!');
            console.log('Donation response:', response.data);

            // Reset form fields
            setAmount('');
            setMessage('');
        } catch (error) {
            console.error('Donation error:', error);
            setResponseMessage('Failed to submit donation. Please try again.');
        }
    };

    return (
        <div>
            <h1>Donations</h1>
            <p>Support the library by making a donation. Your contributions help us grow and improve!</p>

            <form onSubmit={handleSubmit}>
                <div>
                    <label>Donation Amount:</label>
                    <input
                        type="number"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Message (Optional):</label>
                    <textarea
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        rows="4"
                        cols="50"
                    />
                </div>
                <button type="submit">Donate</button>
            </form>

            {responseMessage && <p style={{ marginTop: '1rem', color: 'green' }}>{responseMessage}</p>}
        </div>
    );
};

export default Donations;
