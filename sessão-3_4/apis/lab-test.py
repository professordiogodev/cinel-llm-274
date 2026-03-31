import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

# 1. Total de posts
print("Total de posts:", len(posts))

# 2. Título do post 42
post_42 = None
for p in posts:
    if p["id"] == 42:
        post_42 = p
        break

print("Título do post 42:", post_42["title"])

# 3. Posts do userId 7
posts_user7 = []
for p in posts:
    if p["userId"] == 7:
        posts_user7.append(p)

print("Posts do userId 7:", len(posts_user7))