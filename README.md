## Architektury rozwiązań i metodyki wdrożeń SI 

Projekt został podzielony na 3 części:
* Wcześniejszy notebook z przedmiotu PUM 
* Ten sam kod wykonany w podejściu funkcyjnym
* Implementację kolejnych zadań z projektu zaliczeniowego w chmurze azure 

Projekt w dużej części został oparty na materiałach do egzaminu *DP-100: Designing and Implementing a Data Science Solution on Azure*. Można je znaleźć pod linkami [1](https://microsoftlearning.github.io/mslearn-azure-ml/) [2](https://learn.microsoft.com/en-us/certifications/exams/dp-100/).\
Kod azure zawiera 2 główne pliki. Do jego uruchomienia wymagana jest subskrypcja Azure z dostępem administracyjnym. \
Plik  **setup.sh** tworzy:
* usługę Azure Machine Learning, czyli środowisko, którego używa się do zarządzania projektem ML 
* instancję Standard_DS11_v2 (2 cores, 14 GB RAM, 28 GB disk) za którą płacimy 18 centów za każdą godzinę użytkowania. Trzeba pamiętać o jej wyłączeniu po skończeniu pracy.
* Klaster obliczeniowy składający się z dwóch instancji takich jak ta powyżej. Uruchamiają się one w momencie kiedy zlecimy zadanie i po jego wykonaniu wyłączają się.
Plik **pipeline.ipynb** zawiera wszystkie kroki, które zostały wykonane w trakcie implementacji rozwiązania. Część z nich jest w postaci kodu, a reszta opisana jest za pomocą zdjęć.
### Tworzenie środowiska na platformie Azure

Aby uruchomić skrypt setup.sh należy zalogować się na koncie azure. Kliknąć guzik  [>_] (Cloud Shell) w prawym górnym rogu ekranu. Wybrać Bash jako powłokę. Następnię w terminalu wpisać po kolei komendy: \
*git clone https://github.com/s20636/ASI.git azure-ml-lab* \
*cd azure-ml-labs/Azure-Implementation* \
*./setup.sh* \
Uruchamianie środowiska trwa około 5 minut. \
Następnie należy przejść do Resource Group o nazwie rg-ASI, wybrać Azure Machine Learning workspace o nazwie mlw-ASI i klinąć niebieski guzik *Launch studio*. Po uruchomieniu przechodzimy do zakładki Compute, wybieramy Compute Instance o nazwie ci-ASI i uruchamiamy na nim terminal. W terminalu wpisujemy komendy: \
*pip install azure-ai-ml* \
*git clone https://github.com/s20636/ASI.git azure-ml-lab* \
Po ich wykonaniu stworzy się folder Users/nazwaUżytkownika/azure-ml-labs. Następnie należy wybrać notebook Azure-Implementation/pipeline.ipynb i uruchomić go. Reszta kroków opisana jest w notebooku.

