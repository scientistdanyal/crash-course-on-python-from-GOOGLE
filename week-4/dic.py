# def greet(text):

#     result = {}

#     for letter in text:
#         if letter not in result:
#             result[letter] = 0

#         result[letter] += 1

#     return result


# print(greet('Danyal'))


# dic_1 ={'a':1,'b':2}

# dic_2 = {'b':2,'c':3}

# dic_1.update(dic_2)

# print(dic_1)




# def fullname(employee):

#     full_name = []

#     for last_name ,first_names in employee.items():

#         for first_name in first_names:

#             full_name.append(first_name + ' ' + last_name)


#     return (full_name)

# print(fullname({'ali' :['ahmed','malik','danyal']}))        





# def invert_resource_dict(old_dic):



#     new_dic = {}


#     for resource_group, resources in old_dic.items():


#         for resource in resources:


#             if resource in new_dic:

#                 new_dic[resource].append(resource_group)

#             else:

#                 new_dic[resource] = [resource_group]


#     return new_dic



# print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
#         "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))





def get_sentence(words):
    items = ''

    price = ''



    itm_or_price = words.split()


    for x in itm_or_price:

        if x.isalpha():
            items += x + " "

        else:
            price = x
    

    items = items.strip()

    return '{} on a sales for ${}'.format(items,price)
                
print(get_sentence('White Floor 4.4'))