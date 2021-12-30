# 전화번호 목록
def solution(phone_book):
    phone_book.sort(key=lambda x: (x, len(x)))

    for i in range(len(phone_book) - 1):
        length = len(phone_book[i])

        if phone_book[i] == phone_book[i + 1][:length]:
            return False
    return True