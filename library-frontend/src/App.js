import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header'; // Import Header component
import Home from './pages/Home';
import Fines from './pages/Fines';
import Donations from './pages/Donations';
import SignUp from './pages/SignUp'; // Import the Signup component

function App() {
    return (
        <Router>
            {/* Use Header for the navigation bar */}
            <Header />
            {/* Main content container */}
            <div style={{ marginTop: '2rem' }}>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/fines" element={<Fines />} />
                    <Route path="/donations" element={<Donations />} />
                    <Route path="/signup" element={<SignUp />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;

