import datetime

class MessageUser():
    user_details = []
    messages = []
    base_message = """Hi {name}!

Thank you for the purchase on {date}.
We hope you are excited about using it. Just as
reminder the purchase total was ${total}.
Have a great one!
"""
    def add_user(self, name, amount, email = None):
        name = name[0].upper() + name[1:].lower()
        amount = '%.2f'%amount
        detail = {
            'name': name,
            'amount': amount
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        self.user_details.append(detail)
        if email:
            detail['email'] = email

    @property
    def get_details(self):
        return self.user_details

    @property
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details:
                name = detail['name']
                amount = detail['amount']
                date = detail['date']
                message = self.base_message
                new_message = message.format(
                    name = name,
                    date = date,
                    total = amount
                )
                self.messages.append(new_message)
            return self.messages
        else:
            return []

default_names = ['Justin', 'John', 'Emilee', 'Jim', 'Ron', 'Sandra', 'Veronica', 'Whitney']
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 134, 99.99]

def demo():
    obj = MessageUser()
    min_len = min(len(default_names), len(default_amounts))
    for ith_user in range(min_len):
        obj.add_user(default_names[ith_user], default_amounts[ith_user])

    obj.make_messages
    [print(message) for message in obj.messages]

if __name__ == '__main__':
    demo()
