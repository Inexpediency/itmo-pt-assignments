# Converter

Необходимо реализовать программу, которая бы
конвертировала документы заданной структуры из одного
формата в другой с дополнительными условиями.

Документ представляет из себя блоки текста с форматированием.
Неформально можно представить его как очень-очень упрощённый
Word-файл, в котором можно менять только цвет текста.

Один и тот же документ можно сохранить в трёх форматах:
- .fdtxt
- .fdbin
- .fdjson

_Примечание: всё это - выдуманные форматы специально для данного задания._

Цвета записываются в HEX-формате (напр. `#FF0000` - красный, а `#FFFFFF` - белый).
[Наглядная демонстрация](https://www.w3schools.com/colors/colors_hexadecimal.asp).

## Формат `.fdtxt`
Представляет из себя обычный текстовый файл.
Выделенные определённым цветом блоки заключаются в теги.
В этом формате теги никогда не бывают вложены друг в друга.

Например:
```
If a <FF0000>dog</> chews shoes, <99FFA1>whose shoes</> does he choose?
```

Здесь, тег `<FF0000>` означает, что дальнейший текст будет записан красным,
а тег `</>` - окончание выделения цветом (дальнейший текст будет обычным).

Если в тексте встречается символ 'меньше' (<), не являющийся частью тега,
его можно записать специальным тегом `<lt>`.

Например, "a < 5" можно записать как `a <lt> 5`.

## Формат `.fdjson`

Формат основан на формате JSON и хранит текст как набор
отрезков (span), каждый из которых имеет свой собственный цвет.

Например:
```json
{
  "spans": [
    { "text": "If a " },
    {
      "text": "dog",
      "color": "#FF0000"
    },
    { "text": " chews shoes, " },
    {
      "text": "whose shoes",
      "color": "#99FFA1"
    },
    { "text": " does he choose?" }
  ]
}
```

## Формат `.fdbin`

Представляет из себя бинарный файл следующей структуры:
- число N (int, 4 байта) - длина текста в **байтах**
- строка S (utf-8, N байт) - не форматированный текст
- число K (int, 4 байта) - количество форматированных отрезков
- далее K форматированных отрезков, для каждого:
  - число A (int, 4 байта) - индекс начала отрезка включительно (отсчёт с 0)
  - число B (int, 4 байта) - индекс конца отрезка включительно (отсчёт с 0)
  - 6 символов (ASCII, 1 байт на каждый) - HEX код цвета

_Примечание: HEX-цвет в бинарном файле можно записать как
всего 3 байта (по одному на каждый цвет), но для упрощения задания
выбрана посимвольная запись._

## Задание

Необходимо реализовать функцию, принимающую два параметра:
- `in_file_path` - путь к исходному файлу
- `out_file_path` - путь к файлу-результату

Функция должна по расширению файлов определить их форматы,
прочитать данные из файла `in_file_path`
и вывести их в файл `out_file_path` в правильном для него формате.

Например, `convert('hi.fdtxt', 'hi.fdbin')` должна сконвертировать
данные из формата `fdtxt` в формат `fdbin`.

**Обратите внимание:** реализованная функция не должна оставлять
после себя дополнительные файлы (помимо `in_file_path` и `out_file_path`).
Если функция в процессе своей
работы создаёт вспомогательные файлы, обязательно нужно убедиться,
что уже не существует другой файл с таким же названием.