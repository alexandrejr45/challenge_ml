import requests


def getUsers(page: int):
    url = f'https://jsonmock.hackerrank.com/api/article_users?page={page}'
    return requests.get(url).json()


def storageUsers():
    users = [getUsers(1)]
    total_pages = users[0]['total_pages']

    for i in range(2, total_pages + 1):
        users_new_page = getUsers(i)
        if users_new_page:
            users.append(users_new_page)

    return users


def chooseUserPerSubmissionCount(threshold, users):
    valid_usernames = []

    for page in users:
        for user in page['data']:
            if user['submission_count'] > threshold:
                valid_usernames.append(user['username'])

    return valid_usernames


def getUsernames(threshold):
    users = storageUsers()
    valid_usernames = chooseUserPerSubmissionCount(threshold, users)

    return valid_usernames


def main():
    print(getUsernames(10))

if __name__ == '__main__':
    main()
