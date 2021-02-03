from django.http import HttpResponse


class StripeWH_Handler:
    """
    A webhook to handle Stripe. Code used from CI Stripe lesson
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles an unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
