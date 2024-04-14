some_str: str = "A very very long string from user input"
n: int = 20
splitted_str: list[str] = [some_str[i:i+n] for i in range(0, len(some_str), n)]
result: str = "\n".join(splitted_str)
print(result)