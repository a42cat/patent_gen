# patent_gen
Скрипт для конвертирования файлов проекта в документ нужного формата (pdf, docs, etc...)

#Parameters

-p, --prescan: Предварительное сканирование файлов проекта. Нужно для того чтобы понять какие директории или файлы стоит исключить. Без этого ключа скрипт обработает все файлы и директории без исключения.

<pre>
patent_gen.py -p
</pre>

-i, --input: Путь к директории проекта.<br> 

<pre>
patent_gen.py -i '/home/projects/test/'
</pre>

-o, --output: Путь к папке для выгрузки результата.<br> 

<pre>
patent_gen.py -o '/home/projects_pdf/'
</pre>

--exclude: Расширения файлов которые нужно исключить.<br>
При выборе 'all' будут исключены все файлы (требуется указать расширения   принудительно через ключ -include, --include) <br>

<pre>
patent_gen.py --exclude 'txt,log,bak,all'
</pre>

--include: Расширения файлов которые нужно Использовать. Работает при --exclude all.<br>
<pre>
patent_gen.py --include 'txt,log,bak,all'
</pre>

-l, --log: Путь к логу скрипа (если не заполнено лог не ведется).<br>
<pre>
patent_gen.py --log '/home/logs/patent_gen.log'
</pre>

-v, --verbose: Подробный вывод скрипта.
<pre>
patent_gen.py -v || -vv || -vvv
</pre>
