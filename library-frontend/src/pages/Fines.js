import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Fines = () => {
    const [fines, setFines] = useState([]);
    const [error, setError] = useState(null);

    // Fetch fines data from the Django API
    useEffect(() => {
        axios.get('http://localhost:8000/api/fines/')
            .then(response => setFines(response.data))
            .catch(error => console.error('Error fetching fines:', error));
    }, []);

     return (
        <div>
            <h1>Fines</h1>
            {error && <p>{error}</p>}
            <ul>
                {fines.map((fine) => (
                    <li key={fine.id}>
                        {fine.description} - ${fine.amount} - Due: {fine.due_date}
                        {!fine.paid && <button>Pay Now</button>}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Fines;
