
company_connections = {}
pending_connections = {}
list_of_companies = []
employed = False

def make_list_of_companies():
    interested = True
    while interested == True:
        company = input("What company do you want to add that you are interested in? ")
        list_of_companies.append(company)
        response = input("Are you interested in more companies?(Y/N) ")
        response = response[0].lower()
        if response == 'n':
            interested = False
    return list_of_companies


def check_for_connections(company):
    list_of_invites = []
    list_of_to_remove = []
    if company not in company_connections:
        company_connections[company] = []
    if company not in pending_connections:
        pending_connections[company] = []
    print(f"\nCheck on LinkedIn for people who work at {company}")
    response = input(f"Are there people at {company} you can connect with?(Y/N) ")
    response = response[0].lower()
    if response == 'y' or response == 't':
        to_invite = True
        while to_invite == True:
            name = input("What is their name? ")
            list_of_invites.append(name)
            more = input("Is there another person?(Y/N) ")
            more = more[0].lower()
            if more != 'y' and more != 't':
                to_invite = False
                print()
        for invite in list_of_invites:
            pending_connections[company].append(invite)
            print(f"Send a connect invite to {invite}!!")
    for pending in pending_connections[company]:
        add = input(f"\nHas {pending} accepted the invite?(Y/N) ")
        add = add[0].lower()
        if add != 'y' and add != 't':
            print("Don't worry about it, they might not use LinkedIn much")
        else:
            list_of_to_remove.append(pending)
            company_connections[company].append(pending)
            print("Talk to them dummy!!")
    for remove in list_of_to_remove:
        if remove in pending_connections[company]:
            pending_connections[company].remove(remove)



def check_for_postings(company):
    print(f"\nGo to {company}'s website and check for job postings!!!!")
    response = input(f"Does {company} have job postings?(Y/N) ")
    response = response[0].lower()
    if response == 'y' or response == 't':
        print("APPLY!!!")
        if len(company_connections[company]) != 0:
            print(f"\nHere are your contacts that work at {company}: ")
            for person in company_connections[company]:
                print(person)
        response = input(f"Has {company} offered you a position?(Y/N) ")
        response = response[0].lower()
        if response == 'y' or response == 't':
            print("AWESOME!!! CONGRATULATIONS!! YOU DID IT!!")
            employed = True
        else:
            print("Hang in there buddy")
            employed = False
    else:
        employed = False
    return employed


while employed == False:
    looking = input(f"\nAre you looking for a job?(Y/N) ")
    looking = looking[0].lower()
    if looking == 'n':
        employed = True
    else:
        list_of_companies = make_list_of_companies()
        for company in list_of_companies:
            check_for_connections(company)
            employed = check_for_postings(company)
