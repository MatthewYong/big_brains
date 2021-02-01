/*Code used from CI checkout lesson which is derived from Stripe website: https://stripe.com/docs/payments/accept-a-payment?integration=elements*/


var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');
card.mount('#card-element');
