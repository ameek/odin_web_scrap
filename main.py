import requests as req


def API():
    response = req.get('https://api.evaly.com.bd/core/custom/shops/?page=1&limit=200')
    if response.status_code == 200:
        content = response.json()
        cards = ''

        for dic in content['data']:
            card = """<div class ="card" style="width: 20rem; margin: 10px auto;">
                            <img src = "{}" class ="card-img-top" alt="{}" >
                            <div class ="card-body">
                                <h5 class ="card-text text-center">Name: {}</h5>
                                <p class ="card-text text-center">Number: {}</p>
                            </div>
                        </div>""".format(dic['shop_image'], dic['shop_name'], dic['shop_name'], dic['contact_number'])

            cards = cards + card + "\n\t\t\t\t\t"
        return cards

    else:
        print('{} is not connect'.format(response.status_code))


def Read():
    with open('index.html', 'r', encoding="UTF-8") as file:
        doctype = file.read()
        return doctype


def Write():
    with open('index1.html', 'a+', encoding="UTF-8") as file:
        str = ""
        table = API()
        lists = list(Read())
        lists.insert(-22, table)
        for x in lists:
            str = str + x

        print(table)

        file.write(str)


Write()