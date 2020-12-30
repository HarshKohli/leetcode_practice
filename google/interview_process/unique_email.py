# Author: Harsh Kohli
# Date created: 7/4/2020

def numUniqueEmails(emails):
    unique_list = []
    for email in emails:
        local, domain = email.split('@')
        rel_local = local.split('+')[0]
        rel_local = rel_local.replace('.', '')
        fwd_mail = rel_local + '@' + domain
        if fwd_mail not in unique_list:
            unique_list.append(fwd_mail)
    return len(unique_list)


input = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
num_unique = numUniqueEmails(input)
print(num_unique)
