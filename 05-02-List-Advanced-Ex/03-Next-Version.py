current_version = input().split('.')

new_version = list(str(int(''.join(current_version)) + 1))

final_version = '.'.join(new_version)

print(final_version)
