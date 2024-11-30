import React, { useState } from 'react';
import axios from 'axios';

const Signup = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleSignUp = async (event) => {
        event.preventDefault();

        // Check if passwords match
        if (password !== confirmPassword) {
            setMessage('Passwords do not match.');
            return;
        }

        try {
            // Make API request to the backend for signup
            const response = await axios.post('http://localhost:8000/api/signup/', { email, password });
            console.log('Sign-up response:', response); // Log response for debugging
            setMessage('Account created successfully!');
        } catch (error) {
            console.error('Sign-up error:', error);
            setMessage('Error creating account. Please try again.');
        }
    };

    return (
        <div style={{ maxWidth: '400px', margin: 'auto', textAlign: 'center' }}>
            <h1>Create an Account</h1>
            <form onSubmit={handleSignUp}>
                <div style={{ marginBottom: '1rem' }}>
                    <label htmlFor="email" style={{ display: 'block', marginBottom: '0.5rem' }}>Email:</label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        style={{ width: '100%', padding: '0.5rem' }}
                    />
                </div>
                <div style={{ marginBottom: '1rem' }}>
                    <label htmlFor="password" style={{ display: 'block', marginBottom: '0.5rem' }}>Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        style={{ width: '100%', padding: '0.5rem' }}
                    />
                </div>
                <div style={{ marginBottom: '1rem' }}>
                    <label htmlFor="confirmPassword" style={{ display: 'block', marginBottom: '0.5rem' }}>Confirm Password:</label>
                    <input
                        type="password"
                        id="confirmPassword"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        required
                        style={{ width: '100%', padding: '0.5rem' }}
                    />
                </div>
                <button type="submit" style={{ padding: '0.5rem 1rem', cursor: 'pointer' }}>Sign Up</button>
            </form>
            {message && <p style={{ color: message.includes('successfully') ? 'green' : 'red' }}>{message}</p>}
        </div>
    );
};

export default Signup;
