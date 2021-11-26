import requests


url = 'https://superheroapi.com/api/2619421814940190/'

def search_hero(heroname, url=url):
    searching_url = url + 'search/' + heroname
    data = requests.get(url=searching_url).json()
    results, count = data['results'], 0
    for hero in range(len(results)):
        hero_id = results[hero]['id']
        name = results[hero]['name']
        count += 1
        print(f'#{count}. Name: {name}, ID: {hero_id}.')
    ask = input('Would you like to search another hero? Type Y/N: ').lower()
    while True:
        if ask == 'y':
            another_hero_name = input('Please, Type Another Hero Name to Search: ')
            return search_hero(another_hero_name)
        elif ask == 'n':
            return 'Successfully Exited'
        else:
            el = input('Please Type: "Y" to search another Hero or "N" to exit: ').lower()
            ask = el


def the_smartest_hero(url=url):   
    num = int(input('How many heroes would you like to compare? (int): '))
    list_ids = [int(input(f'#{n} Please, Type Hero "ID" (int): ')) for n in range(1, num+1)]
    get_data, min_ = [], 0
    for num in range(len(list_ids)):
        by_id = url + str(list_ids[num]) + '/powerstats'
        data = requests.get(url=by_id).json()
        if data['intelligence'] == 'null':
            data['intelligence'] = '0'
            hero = [data['name'], int(data['intelligence'])]
        else:
            hero = [data['name'], int(data['intelligence'])]
        get_data.append(hero)
    print('Among Presented Heroes: 👇 \n')
    for hero in range(len(get_data)):
        print(get_data[hero][0])
        if get_data[hero][1] >= min_:
            min_ = get_data[hero][1]
            beast = get_data[hero]
    print(f'\nThe most smartest hero is "{beast[0]}" with the intelligence of "{beast[1]}".\n')
    ask = input('Would you like to compare heroes once more ? Type "Y" for Yes or "N" to Exit: ').lower()
    while True:
        if ask == 'y' or ask == 'yes':
            return the_smartest_hero()
        elif ask == 'n' or ask == 'exit' or ask == 'q':
            return 'Successfully Exited'
        else:
            ex = input('Please, Type "Y" if you want to compare more heroes or "N" to Exit: ')
            ask = ex



if __name__ == '__main__':
    print('''Welcome to the Super-Hero Api.\n
Type "1" If You Want to Find Heroes IDs (recommended first).
Type "2" If You Want to Compare Heroes and Check For the Smartest One.\n
Or "q" to Exit.\n ''')
    user_selection = input('Type and Press "Enter": ').lower()
    in_process = True
    while in_process:
        if user_selection == '1':
            hero_name = input('Please, Type Hero Name (e.g: Hulk, Captain America, Thanos ) to Search: ')
            print(search_hero(hero_name))
            user_selection = '2'
        elif user_selection == '2':
            print('''I am function to compare and find out the smartest hero by Hero ID.
(e.g: Captain America = 149, Hulk = 332, Thanos = 655 )''' )
            print(the_smartest_hero())
            in_process = False
        elif user_selection == 'q':
            in_process = False
        else:
            print('Please, Type "1" to Search Hero ID/Type "2" to Check The Smartest Hero or "q" to Exit.')
            making_choice = input('Type and Press "Enter": ')
            user_selection = making_choice