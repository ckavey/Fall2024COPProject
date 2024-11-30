import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography } from '@mui/material';

const Header = () => {
    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" style={{ flexGrow: 1 }}>
                    Library System
                </Typography>
                {/* Navigation Links */}
                <Link to="/" style={{ color: 'white', marginRight: '1rem', textDecoration: 'none' }}>Home</Link>
                <Link to="/fines" style={{ color: 'white', marginRight: '1rem', textDecoration: 'none' }}>Fines</Link>
                <Link to="/donations" style={{ color: 'white', marginRight: '1rem', textDecoration: 'none' }}>Donations</Link>
                <Link to="/signup" style={{ color: 'white', textDecoration: 'none' }}>Sign Up</Link>
            </Toolbar>
        </AppBar>
    );
};

export default Header;
