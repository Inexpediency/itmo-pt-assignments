# Задание git

Реализуйте функцию, которая работает похожим на команду `git` образом. Не требуется реализовывать ту же
функциональность, только тот же "интерфейс" &ndash; возможность вызывать функцию с теми же параметрами.

Формально, если в консоли можно написать `git команда параметр --опция`, должна быть возможность вызвать функцию `git`
как `git('команда', имя_параметра='параметр', __опция=True)`. Подробное описание интерфейса можно найти ниже.

Это задание довольно объемное, но в остальном, наверное, больше техничное, чем сложное.

## `git add`

Должна быть возможность вызвать функцию как `git('add', ...)`, где вместо многоточия должно быть передано сколько угодно
строковых аргументов, **но они все обязаны быть позиционными**.

Если команда корректна, верните строку `Added {number} files`, где `{number}` &ndash; количество переданных аргументов
после `add`. Иначе верните `None`.

Например,

- `git('add', 'practice/finish_me', 'homework/git')` &rightarrow; `'Added 2 files'`

---

- `git('add')` &rightarrow; `None`, так как не переданы доп. аргументы
- `git('add', 12)` &rightarrow; `None`, так как передан не строковый аргумент
- `git('add', 'practice', message='Added folder')` &rightarrow; `None`, так как `git add` не принимает именованные
  аргументы

## `git commit`

Должна быть возможность вызвать функцию как

- `git('commit', сообщение)` или `git('commit', message=сообщение)`, тогда помимо сообщения, в функцию не должны
  передаваться никакие другие аргументы, ни позиционные, ни именованные;
- `git('commit', __amend=True)`, тогда, аналогично, больше не должно быть передано никаких аргументов.

> **Информация**: `git commit --amend` &ndash; команда для добавления новых изменений в _предыдущий_ коммит
>
> Например, если у вас осталась мелкая ошибка, исправление которой не хочется выделять в отдельный коммит

Если команда корректна, верните строку `Commit successful`. Иначе верните `None`.

Например,

- `git('commit', 'Practice done')` &rightarrow; `Commit successful`
- `git('commit', message='Practice done')` &rightarrow; `Commit successful`
- `git('commit', __amend=True)` &rightarrow; `Commit successful`

---

- `git('commit', __amend='Message')` &rightarrow; `None`, так как `__amend != True`
- `git('commit')` &rightarrow; `None`, так как не переданы параметры
- `git('commit', message='Done', __amend=True)` &rightarrow; `None`, так как переданы оба взаимоисключающих параметра
- `git('commit', m='Done')` &rightarrow; `None`, так как передан аргумент с неожиданным именем `m`
- `git('commit', 123)` &rightarrow; `None`, так как то, что должно быть сообщением &ndash; не строка, а число

## `git push`

Должна быть возможность вызвать функцию как `git('push', назначение, ветка)`
или `git('push', remote=назначение, branch=ветка)`. **Вместе с этим** может быть передан аргумент `__set_upstream=True`,
а также, независимо от этого, аргумент `__force=True`. Другие параметры в функцию переданы быть не должны.

Параметр `branch` может быть не указан, в таком случае в качестве него автоматически подставляется значение по
умолчанию `'main'` (см. примеры ниже).

Если команда корректна, верните строку `'Push to {remote}/{branch} successful'`, если `__force=True` не был передан,
и `'Force push to {remote}/{branch} successful'`, если `__force == True`. Здесь за `{remote}` и `{branch}` обозначены
первые два параметра функции. Если же команда некорректна, верните `None`.

> **Информация**: если в `git push` передать `--set-upstream` (он же `-u`), то в следующий раз можно не указывать
> remote и branch &ndash; будут использованы значения, указанные в этот раз
>
> При передаче флага `--force` (он же `-f`), если в удаленном репозитории (remote) есть конфликтующие расхождения с
> локальным, они будут отброшены и заменены на локальные

Например:

- `git('push', 'origin')` &rightarrow; `'Push to origin/main successful'`
- `git('push', remote='upstream')` &rightarrow; `'Push to upstream/main successful'`
- `git('push', 'origin', 'practice', __set_upstream=True)` &rightarrow; `'Push to origin/practice successful'`
- `git('push', remote='origin', branch='main', __set_upstream=True, __force=True)`
  &rightarrow; `'Force push to origin/main successful'`

---

- `git('push', branch='main')` &rightarrow; `None`, так как не передан `remote`
- `git('push', __force=True)` &rightarrow; `None`, так как не передан `remote`
- `git('push', remote='origin', branch=123, __set_upstream=True)` &rightarrow; `None`, так как в качестве ветки передана
  не строка
- `git('push', remote='upstream', __tags=[])` &rightarrow; `None`, так как передан неожиданный аргумент `__tags`
- `git('push', 'upstream', branch='practice')` &rightarrow; `None`, так как `remote` передан как позиционный, а `branch`
  &ndash; как именованный аргумент
- `git('push', 'upstream', 'practice', __force=False)` &rightarrow; `None`, так как если `__force` передан, он обязан
  быть `True`

## Другие команды

Если `git` вызван с другим первым параметром, следует вернуть строку `'Unknown command'`.