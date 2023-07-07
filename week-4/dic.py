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





# def get_sentence(words):
#     items = ''

#     price = ''



#     itm_or_price = words.split()


#     for x in itm_or_price:

#         if x.isalpha():
#             items += x + " "

#         else:
#             price = x
    

#     items = items.strip()

#     return '{} on a sales for ${}'.format(items,price)
                
# print(get_sentence('White Floor 4.4'))

























# def get_sentence(itm_and_price):
#     items = ""
#     price = ''


#     itm_or_price = itm_and_price.split()

#     for x in itm_or_price:

#         if x.isalpha():
#             items += x + ' '

#         else:
#             price = x


#     items = items.strip()
#     return '{} on a sales for ${}'.format(items,price)


# print(get_sentence('white floor 7.7'))

    






# def extend_two_list(recent_first,recent_last):

#     recent_first.reverse()

#     recent_last.extend(recent_first)

#     return recent_last




# recent_first = [2022, 2018, 2011, 2006]
# recent_last = [1989, 1992, 1997, 2001]
# print(extend_two_list(recent_first,recent_last))


# def reset_score(game_scores):
  
#   new_game_scores = game_scores.copy()
  
#   for player , score in new_game_scores.items():
    
    
#     new_game_scores[player] = 0
    
    
    
    
#   return new_game_scores
  
  
# print(reset_score({'Danyal':3,'Ali':7}))  
  






def network(servers):


    results = ''


    for hostname, IP_address in servers.items():


        results += 'The IP address of the {} server is {}'.format(hostname,IP_address) + '\n'



    return results

print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))

  
