import subprocess


result = subprocess.run(["py", "--version"], capture_output=True, encoding='utf-8')

result

result2 = subprocess.run(["python3", "--version"], capture_output=True, encoding='utf-8')

result2

input = """for i in range(1,3):
    print(f'Hello {i}')
    """

result3 = subprocess.run(["py"], input = input, capture_output=True, encoding='utf-8')

print(result3.stdout)
