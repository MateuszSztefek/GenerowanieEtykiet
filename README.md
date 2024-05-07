# GenerowanieEtykiet
Programy wczytują dane z pliku **.xlsx** i generują plik **.pdf** ze wszystkimi etykietami, następnie taki plik drukuje się na drukarce do etykiet samoprzylepnych. W folderze **Typ1** i **Typ2** znajdują się kody źródłowe programów. W pliku z końcówką **.py** znajduje się program, a w plikach **.pdf** i **.xlsx** znajdują się odpowiednio gotowe etykiety i plik wejściowy z danymi dla programu. Dodatkowo w folderze **Typ1** znajduje się folder **fonts** z fontem, który umożliwia drukowanie etykiet z cyrylicą.


## Typ 2
Jeden rząd w pliku .xlsx odpowiada jednej etykiecie. Dane są ułożone w kolumnach według porządku:
- Nazwa producenta
- Numer zamówienia
- Kraj pochodzenia produktu, który jest w kartonie
- Nazwa artykułu, który jest w kartonie
- Kod kreskowy artykułu, który jest w kartonie
- Rozmiar artykułu, który jest w kartonie
- Ilość
- Numer kartonu
- Ilość wszystkich kartonów<br><br>
Wygląd etykiety:<br>![image](https://github.com/MateuszSztefek/GenerowanieEtykiet/assets/88203590/e7264223-adf0-4bb1-b70e-40abf3b4b48e)<br>

## Typ 1
Jeden rząd w pliku .xlsx odpowiada jednej etykiecie. Dane są ułożone w kolumnach według porządku:
- Nazwa zamówienia
- Numer kartonu
- Nazwa artykułu, który jest w kartonie
- Kolor artykułu, który jest w kartonie
- Rozmiar artykułu, który jest w kartonie
- Ilość<br><br>
Wygląd etykiety:<br>![image](https://github.com/MateuszSztefek/GenerowanieEtykiet/assets/88203590/8e4ac464-cfc0-43a0-8ff8-1e4cea0296a3)<br>







