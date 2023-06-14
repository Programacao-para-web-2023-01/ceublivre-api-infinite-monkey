import stripe

# Set your Stripe API keys
stripe.api_key = 'your_stripe_api_key'
stripe.api_version = '2020-08-27'  # Replace with your desired API version


# Function to create a payment intent
def create_payment_intent(amount, currency):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency
    )
    return intent


# Function to confirm a payment intent
def confirm_payment_intent(payment_intent_id):
    intent = stripe.PaymentIntent.confirm(payment_intent_id)
    return intent


# Function to retrieve a payment intent
def retrieve_payment_intent(payment_intent_id):
    intent = stripe.PaymentIntent.retrieve(payment_intent_id)
    return intent


# Function to cancel a payment intent
def cancel_payment_intent(payment_intent_id):
    intent = stripe.PaymentIntent.cancel(payment_intent_id)
    return intent