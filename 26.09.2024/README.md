# 11.2_tdd_ihk
Ihnen liegt folgende UserStory vor:
>Ich benötige ein Python-Skript  zur IHK-Notenberechnung und möchte:
>1. die erreichten Punkte und die gesamt möglichen Punkte eingeben und den erreichten Prozentwert erhalten
>2. den erreichten Prozentwert eingeben und die schriftliche Note (z.B. „sehr gut“) erhalten

Setzen Sie die Anforderung um, indem Sie: 
- eine Grenzwertanalyse [in dieser Datei](Grenzwertanalyse.md) durchführen 
- nach Test-Driven-Developement (TDD) arbeiten
- das Arrange-Act-Assert-Muster (AAA) einhalten

## Tools
[siehe letzte Aufgabe](https://github.com/gsoTH/11.2-erste-Schritte)
## AAA-Muster einhalten
### Positivtests
```python
def test_func__<hinweiseZumTest>():
    # Arrange
    testwert = ...
    soll_ergebnis = ...
    # Act
    ist_ergebnis = func(testwert)
    # Assert
    assert ist_ergebnis == soll_ergebnis
```
### Negativtests
Negativtests sind erfolgreich, wenn die erwartete Exception geworfen wird. [Liste der Exceptions](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
```python
def test_func__<hinweiseZumTest>():
    # Arrange
    ungueltiger_testwert = ...
    # Act
    with pytest.raises(ValueError):
        func(ungueltiger_testwert)
```
