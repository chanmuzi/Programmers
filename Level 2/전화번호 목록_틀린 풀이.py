def solution(phone_book):
    phone_book.sort(key=lambda x:(x,len(x)))
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] in phone_book[j]:
                return False
    else: return True