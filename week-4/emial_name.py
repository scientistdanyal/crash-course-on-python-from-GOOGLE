def full_emails(people):

    result = []

    for index,(email , name) in enumerate(people):
        result.append(' ({})-{} <{}>'.format(index+1,name,email))



    return result



print(full_emails([('dk.yalgar@gmail.com','Danyal Ahmed'),('ali@example.com','Ali')]))
