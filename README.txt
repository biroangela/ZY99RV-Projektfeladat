Szimbólum Rajzoló

Név: Biró Angéla Marianna
Neptunkód: ZY99RV
Monogram: BAM

Feladat leírása

A program egy grafikus felületet biztosít, ahol a felhasználó négy szimbólum (kocka, szív, rombusz, háromszög) közül választhat.
A kiválasztott szimbólumot a program lerajzolja, majd három műveletgomb jelenik meg:

- Új szimbólum rajzolása: visszatér az elejére, és új szimbólumot választhatunk.
- Rajz mentése: a jelenlegi rajzot .txt formátumban menti egy megadott fájlnévvel,
 amelyben leírja, hogy melyik szimbólumot rajzoltattuk le, illetve a mentés dátumát.
- Kilépés: bezárja az alkalmazást.

A mentés után is aktívak maradnak a gombok, így több rajz is elmenthető egymás után.

Modulok és függvények

main.py
- A program belépési pontja.
- Létrehozza a fő ablakot és elindítja a BAMApp osztályt.

BAM_appclass.py
- Tartalmazza a fő grafikus logikát és a saját osztályt:
  Osztály: BAMApp
  Függvények:
    - show_symbol_buttons() – a választó gombokat jeleníti meg.
    - bam_draw_shape(shape) – a kiválasztott alakzatot kirajzolja.
    - show_action_buttons() – a műveleti gombokat jeleníti meg (új, mentés, kilépés).
    - bam_save_canvas() – elmenti a vásznat fájlba.

BAM_szimbolumok.py
  - A rajzolási függvényeket tartalmazza:
  - kocka(canvas)
  - sziv(canvas)
  - rombusz(canvas)
  - haromszog(canvas)


Saját elemek

Típus           Név                   Leírás
Saját osztály   BAMApp                A teljes grafikus kezelést végzi.
Saját függvény  bam_draw_shape()      Monogrammal ellátott, saját logikájú függvény.
Saját függvény  bam_save_canvas()     Monogrammal ellátott, saját logikájú függvény.
Saját modul     BAM_szimbolum.py      A rajzolási funkciók elkülönítése a fő logikától.



Használt modulok

	Tanult modul:
		- tkinter – Grafikus felület és eseménykezelés.

	Internetről keresett /bemutatandó modul:
		- os - Fájlnevek, elérési utak és kiterjesztések kezelése a mentésnél.
		- datetime – Mentés időpontjának beillesztése a .txt fájlba (év, hónap, nap, óra, perc formátumban).
	
	Saját modul:
		- BAM_szimbolumok (saját) – Rajzolási logika.

