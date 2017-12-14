# md_utils
Список программ:

auto_umbr_frame.py – генерирование файла зависимости расстояния (COM) от
 t и автоматическая фильтрация конформаций для окон umbrella sampling (US)

chain_trjpdb.py – переименование цепей с перенумерацией а.о. в pdb-файле

chain_trjpdb_tk.py – tk версия chain_trjpdb.py

comdom.py – расчет расстояния между центрами масс доменов по траектории МД

comdom_tk.py – tk версия comdom.py

conf_rename.py – перенумерация конформаций US

creat_xvg.py – генерация xvg- файлов по результатам US

dna_srg.py – генерирование случайной первичной последовательности ДНК

dna_srg_tk.py - tk версия dna_srg.py

gro_conv.py - конвертер gro-файлов ProDrug-сервера

hcheck.py - утилита для проверки валентных связей H-атомов в структуре

multigraph_tk.py – отображение на графике данных одного или нескольких xvg-файлов
 — аналог xgrace - tk версия

ocucheck.py – проверка суммы заселенностей атомов и а.о. в pdb-файле

occucheck2.py - проверка суммы заселенностей атомов и а.о. (biopython)

occucheck2_tk.py - проверка суммы заселенностей атомов и а.о. (2 режима, tk версия)

setb.py  - установка значения B-фактора заданному диапазону а.о.

setb_tk.py - tk версия  setb.py

split_chain.py - разделение pdb-файла по отдельным цепям

________________________________________________________________________
Зависимости:

auto_umbr_frame.py – numpy, matplotlib, progressbar

comdom.py –  periodictable, numpy, matplotlib, progressbar*

creat_xvg.py – numpy

histo.py – numpy, matplotlib

multigraph_tk.py – numpy, matplotlib

occucheck2.py – biopython, numpy, mmtf

________________________________________________________________________
*- tk версия не зависит от progressbar.
У tk версий зависимости те же, что и у консольных (кроме *).
