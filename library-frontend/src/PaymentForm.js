import React, { useEffect, useState } from 'react';
import { loadStripe } from '@stripe/stripe-js';
import { Elements, CardElement, useStripe, useElements } from '@stripe/react-stripe-js';

const stripePromise = loadStripe('YOUR_STRIPE_PUBLISHABLE_KEY');

const PaymentForm = () => {
    const stripe = useStripe();
    const elements = useElements();
    const [clientSecret, setClientSecret] = useState('');

    useEffect(() => {
        fetch('/api/create-payment-intent/')
            .then((res) => res.json())
            .then((data) => setClientSecret(data.clientSecret));
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();

        const { error } = await stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: elements.getElement(CardElement),
            },
        });

        if (!error) {
            console.log('Payment successful!');
        } else {
            console.error('Payment error:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <CardElement />
            <button type="submit" disabled={!stripe}>
                Pay
            </button>
        </form>
    );
};

const App = () => (
    <Elements stripe={stripePromise}>
        <PaymentForm />
    </Elements>
);

export default App;
