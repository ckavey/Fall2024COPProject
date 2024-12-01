import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Home = () => {
    const [user, setUser] = useState(null);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    useEffect(() => {
        // Fetch logged-in user details
        axios
            .get('http://localhost:8000/accounts/profile/', { withCredentials: true }) // Ensure cookies are sent
            .then((response) => {
                setUser(response.data); // Set user if logged in
            })
            .catch(() => setUser(null)); // Set user to null if not logged in
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post(
                'http://localhost:8000/api/login/',
                { email, password },
                { withCredentials: true } // Ensure session/cookies are set
            );
            console.log('Logged in:', response.data);
            setUser(response.data); // Update user state
        } catch (error) {
            console.error('Login error:', error);
            setErrorMessage('Invalid email or password');
        }
    };

    const handleLogout = () => {
    // Log out user
    axios.post('http://localhost:8000/accounts/logout/', {}, { withCredentials: true }).then(() => {
        setUser(null); // Reset user state
        window.location.href = '/'; // Redirect to home page
    });
};

    return (
        <div>
            <h1>Welcome to Your Local Library System</h1>
            <p>This is the home page of your local library system.</p>

            {user ? (
                <div>
                    <h2>Successfully Logged In</h2>
                    <p>Welcome, {user.username || user.email}!</p>
                    <button onClick={handleLogout}>Sign Out</button>
                </div>
            ) : (
                <div>
                    <h2>Log In</h2>
                    <form onSubmit={handleSubmit}>
                        <div>
                            <label>Email:</label>
                            <input
                                type="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />
                        </div>
                        <div>
                            <label>Password:</label>
                            <input
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                        </div>
                        <button type="submit">Log In</button>
                        {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
                    </form>

                    <h2>Or Log In with Google</h2>
                    <a href="http://127.0.0.1:8000/accounts/google/login/">
                        <button type="button">Login with Google</button>
                    </a>

                    <p>
                        Don't have an account? <Link to="/signup">Sign up here</Link>.
                    </p>
                </div>
            )}
        </div>
    );
};

export default Home;
