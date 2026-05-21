# playwright-zimaev-stepik
Прохождение обучения https://stepik.org/course/128626/info

Обход блокировки исчезновения сайта при появлении инспектора  
в dev tools прописать:
```js
const intervalId = setInterval(() => {
    const glass = document.querySelector('x-pw-glass');
    if (glass) {
        glass.style.visibility = 'hidden';
    }
}, 100);
```

Запуск теста с записью в файл

```commandline
playwright codegen --target python -o my_test.py http://my_site.com
```
