# Wtyczka QGIS
# 1. Do czego służy wtyczka i jaką funkcjonalność oferuje 
Wtyczka oferuje obliczanie przewyższeń między dwoma punktami oraz obliczanie pola powierzchni między minimlanie 3 punktami.
# 2. Wymagania działania programu 
Wymagane jest posiadanie programu QGIS oraz warstwa posiadająca współrzędnych punktów. 
Również folder z wtyczką należy umiejscowić w dobrym miejscu przykładowa ścieżka gdzie należy  to zrobić "C:\Users\Lenovo\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins"
# 3. Instrukcja korzystania z wtyczki
Po odpaleniu programu QGIS w górnym pasku menu należy wybrać "wtyczki". Nastepnie "zarządzanie wtyczkami" i wyszukać "wtyczka projekt 2", zaznaczyć ją i zamknąć okno.
Do korzystania w pełnej możliwości wtyczki należy posiadać warstwę, która posiada atrybuty ze współrzędnymi X, Y, h. Trzeci z kolei atrybut o nazwie "h" określa wysokość punktu. Jeśli warstwa nie posiada wysokości, będzie możliwe tylko policzenie pola powierzchni. 
Aby skorzytsać z wtyczki należy zaznaczyć wybrane punkty, które chce się uwzględnić w obliczeniach. Dla przewyższeń mogą być to tylko iwyłącznie 2 punkty, a dla pól powierzchni musza być minimalnie 3 punkty 
Po zaznaczneiu owych punktów, wybrać z górnego pasku menu "wtyczki" kolejno wejść w "wtyczka projekt 2", wyswiętli się okno główne wtyczki. Teraz należy wybrać warstwę na której się zaznaczyło punkty, oraz wybrać funkcję którą chce się użyć ( do wyboru "liczenie przewyższenia" lub "liczenie pola powierzchni"), po kliknięciu wybranej funkcji, wynik wyświetli się w górnej części ekranu. 
(jeśli chodzi o pola powierzchni można wtyczkę przetestować w dowolnej warstwie, jeśli jednak chodzi o przewyższenia, zalecamy skorzystanie ze specjalnie przygotowanej warstwy "warstwa_wysokość")
# 4. Znane błędy i nietypowe zachowania 
Błędnym zachowaniem programu Qgis jest błędne dobieranie punktów (w złej kolejności) do obliczenia pola powierzchni, w skutek tego pole powierzchni zostaje policzone w inny sposób niż użytkownik sobie tego życzy. Poprawne wartości wychodzą gdy punkty są 3 
