
def get_main_menu(request):
    context = {
        'menu':[
            {'name': "Главная", 'url':'landing'},
            
            # {'name': "Список обращений", 'url': 'reviews'},
                    

        ]
    }
    return context