import tkinter as tk
import requests
hieght= 500
width=600
root = tk.Tk()

def test_fun(entry):
    print(entry)

def fr(weather):
    try:
        name = weather['name']
        des = weather['weather'][0]['description']
        temp = weather['main']['temp']

        fs='City: %s \nConditions: %s \nTemp (C*): %s' % (name, des, temp)
    except Exception:
        fs="Location Not Found......"

    return fs

def weather1(city):
    key='8f38c3036b95711787bb4fb29c1dde56'
    url='http://api.openweathermap.org/data/2.5/weather'
    p={'APPID': key, 'q': city, 'units': 'imperial'}
    r= requests.get(url, params=p)
    w=r.json()
    label['text'] = fr(w)
    print(w['name'])
    print(w['weather'][0]['description'])
    print(w['main']['temp'])

label1 = tk.Label(root, text='Weather App', bg = 'white')
label1.config(font=('avenir', 20))

canvas = tk.Canvas (root, height=hieght, width= width)
canvas.pack()

frame = tk.Frame(root, bg='#000000', bd=2,)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
button = tk.Button(frame, text="Fetch", font=36, bg='#C0C0C0',command=lambda: weather1(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

entry=tk.Entry(frame, font=30)
entry.place(relwidth=0.69, relheight=1)

frame2 = tk.Frame(root, bg='#000000', bd=2)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label=tk.Label(frame2, bg='#C0C0C0')
label.place(relwidth=1, relheight=1)

root.mainloop()