class Content:
    def __init__(self):
        self.id = ''
        self.title = ''
        self.author = ''
        self.content = ''


my = Content()
my.id = '1'
my.title = '1주차 첫 숙제'
my.author = 'JS'
my.content = '1주차 첫 숙제 입니다. 너무 쉬워요~~'


print(f'{my.id} , {my.title}, {my.author}, {my.content}')