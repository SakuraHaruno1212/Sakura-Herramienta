import requests as r

respuesta = r.get("https://www.facebook.com/profile.php?id=61583385128191")
print(respuesta.text)
