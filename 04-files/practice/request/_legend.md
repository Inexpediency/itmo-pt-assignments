# Github

Требуется реализовать одну функцию, которая возвращает имя вашего аккаунта
на гитхабе, используя Github API.

Это значит, что нельзя просто вернуть его - надо создать свой
GitHub Access Token и сделать с ним соответствующий запрос к GitHub API,
чтобы получить имя своего аккаунта.

Access Token можно создать в [разделе настроек](https://github.com/settings/tokens).

Пример обращения к Github API:
```python
import requests
request = requests.get('https://api.github.com/user', auth=('username', 'access_key'))
data = request.json() # прочитать ответ сервера как json-объект
```

# Wikipedia
**Это бонусное задание, но желательно его сделать.**

Требуется сделать запрос к русской википедии к страничке с
переданным именем `name` и вернуть первый блок текста,
выделенный жирным шрифтом (то, что стоит в самом начале текста статьи,
обычно это расшифровка или другое представление заголовка).
Стоит посмотреть, как выглядит страничка википедии в html-коде и понять,
чем характеризуется этот блок текста.

**Подсказка:** в html-инспекторе популярных браузеров можно скопировать
XPath определённого элемента и получить примерно такую строку:
`/html/body/div[3]/div[3]/tbody/tr[2]/td/p`.
Тогда, получив исходный текст страницы (`request.content`), можно
удобным образом извлечь содержимое этого элемента.

```python
from lxml import html

# создаём "дерево" на основе HTML-кода страницы
tree = html.fromstring(page.content) 

# получим список элементов, соответствующих XPath
elements = tree.xpath('/html/body/div[3]/table[1]/tbody/tr[2]/td/p')

# выведем текст первого найденного элемента
print(elements[0].text)
```

Пример:
```
wikipedia('ICPC') -> 'Международная студенческая олимпиада по программированию' 
```
