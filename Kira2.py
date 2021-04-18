import wikipedia
import webbrowser

while True:
    print("Hello user...THIS IS KIRA 2...A all in one assistant")
    print('Here are some rules for me to work properrly')
    print('''1.if you want to know about something then enter the spellings correctly
    2.if you want to know the time type (time in it)
    3.To break type (break)
    4.There are some pre defined websites that I can open like:-
       Whattsapp
       instagram
       twitter
       pinterest...More websites will be asdded later ''')
    query = input("ENTER WHAT YOU WANT TO KNOW")
    
    
    print("You asked for - ",query.lower())
    
    if 'wikipedia' in query:
                print("Suffering the internet")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences = 2)
                print("According to wikipedia")
                print(results)

    elif 'Whatsapp' in query:
        print("Opening ")
        webbrowser.open('https://web.whatsapp.com/')

    elif 'email' in query:
        print("Opening ")
        webbrowser.open('https://gmail.com/')

    elif 'Youtube' in query:
        print("Opening ")
        webbrowser.open('https://Youtube.com/')

    elif 'break' in query:
       break 