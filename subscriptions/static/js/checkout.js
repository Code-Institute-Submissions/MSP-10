var stripe = Stripe('pk_test_51KNe9dBAHJm9GG3TEh3TgUcOZIfUVkMpVb6Dj2USEw7Xi0vXdag2g35yEIZxiSQIjN9kDTpsbeT6Jz0OEOG000sc007CmjtRu3');

var checkoutButton = document.querySelector('#checkout-button');
checkoutButton.addEventListener('click', function () {
  // const price = modalBtn.getAttribute('data-amount');
  // const name = modalBtn.getAttribute('data-name');
  const stripe_id = modalBtn.getAttribute('data-stripe_subscription_id');
  stripe.redirectToCheckout({
    lineItems: [{
      // Define the product and price in the Dashboard first, and use the price
      // ID in your client-side code. You may also pass a SKU id into the `price`
      // field
      price: stripe_id,
      quantity: 1
    }],
    mode: 'subscription',
    successUrl: 'https://www.example.com/success',
    cancelUrl: 'https://www.example.com/cancel'
  });
});