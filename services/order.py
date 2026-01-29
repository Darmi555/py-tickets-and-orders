from django.db import transaction
from db.models import Ticket, Order, User


def create_order(tickets: list, username: str, date: str = None) -> None:
    user = User.objects.get(username=username)
    with transaction.atomic():
        order = Order.objects.create(user=user)

        if date:
            order.created_at = date
            order.save()

        for ticket in tickets:
            Ticket.objects.create(
                movie_session_id=ticket["movie_session"],
                order=order,
                row=ticket["row"],
                seat=ticket["seat"]
            )


def get_orders(username: str = None) -> list:
    if username:
        return list(Order.objects.filter(user__username=username))
    return list(Order.objects.all())
