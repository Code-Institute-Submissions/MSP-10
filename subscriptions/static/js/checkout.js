
const stripe = Stripe(process.env.STRIPE_API_KEY);

var checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', function() {
  stripe.redirectToCheckout({
    // Make the id field from the Checkout Session creation API response
    // available to this file, so you can provide it as argument here
    // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
    sessionId: session.sessionid
  }).then(function (result) {
    // If `redirectToCheckout` fails due to a browser or network
    // error, display the localized error message to your customer
    // using `result.error.message`.
  });
});


    // var stripe = Stripe('pk_live_my-key');
  
    // var checkoutButton = document.getElementById('checkout-button-plan_id');
    // checkoutButton.addEventListener('click', function () {
    //   // When the customer clicks on the button, redirect
    //   // them to Checkout.
    //   stripe.redirectToCheckout({
    //     items: [{plan: 'my-plan-id', quantity: 1}],
    //     // Do not rely on the redirect to the successUrl for fulfilling
    //     // purchases, customers may not always reach the success_url after
    //     // a successful payment.
    //     // Instead use one of the strategies described in
    //     // https://stripe.com/docs/payments/checkout/fulfillment
    //     successUrl: 'https://www.lewisbnb.fr/success?session_id={CHECKOUT_SESSION_ID}',
    //     cancelUrl: 'https://www.lewisbnb.fr/canceled',
    //   })
    //   .then(function (result) {
    //     if (result.error) {
    //       // If `redirectToCheckout` fails due to a browser or network
    //       // error, display the localized error message to your customer.
    //       var displayError = document.getElementById('error-message');
    //       displayError.textContent = result.error.message;
    //     }
    //   });
    // });
