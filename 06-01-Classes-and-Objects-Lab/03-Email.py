class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


mailbox = []

while True:
    email = input()
    if email == 'Stop':
        break

    sender, receiver, content = email.split(' ')
    current_email = Email(sender, receiver, content)
    mailbox.append(current_email)

sent_emails = list(map(int, input().split(', ')))

for index in sent_emails:
    mailbox[index].sent()

for email in mailbox:
    print(email.get_info())
