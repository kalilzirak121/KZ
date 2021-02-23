aclNum = int(input("What is the IPv4 ACL Number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a Standard IPv4 ACL")
elif aclNum >= 100 and aclNum <= 199 : 
    print("This is an extended IPv4 ACL")
else:
    print("This is not a Standard or extended IPv4 ACL")