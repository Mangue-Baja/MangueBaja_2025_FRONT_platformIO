# LEIA 
Foi feita uma mudança do Keil Studio para o platformIO porém ainda utilizando o `mbed`. Segue algumas coisas que são cruciais para o entendimento do funcionamento do projeto do platformIO com a STM32. No `platformio.ini` tem tudo o que você precisa, mas explicarei os tópicos importantes.

- `board = nucleo_f103rb` e `framework = mbed` são referentes a configuração que era feita no Keil Studio, *NUCLEO-F103RBT6 e MBED framework*.
- `board_build.f_cpu = 72000000L` é a frequência do microcontrolador.
- `extra_scripts`: signica que quando você der **build (crtl + alt+ B)** ele irá executar esse script `extra_script.py` que copia o `.bin` gerado pelo platformIO para a pasta [bin_files](bin_files/).
- É **Extremamente Necessário** que tenha no seu projeto do platformIO o `extra_script.py` (mencionado acima) na raiz do seu projeto, e caso não tenha a pasta **bin_files** o script irá criar essa pasta automaticamente e la ficara o .bin gerado pelo último build. Lembrando que você **ainda usará o `st-link utility`** e que ele funciona com `.hex` e `.bin`.
- É inutil você usar o **upload (crtl + Alt + U)** no platformIO, irá adiantar de nada porque ele não vai fazer nada. Use só o **build (crtl + alt+ B)** que irá funcionar tranquilamente.
- O tempo de **build** total dele é bem longo (bem longo mesmo!!) devido a quantidade de dependências que o `mbed` tem. Então evite ficar dando **clean** desnecessariamente para não perder tempo.
- Recomendo fortemente você criar o projeto da `STM32` no caminho padrão que o platformIO já oferece, colocando em outra pasta a chance de dar erro no **build** é muito grande (vá por mim, descobri da pior forma). Aparemente como tem que compilar muitos arquivos, se o `path` do seu projeto for muito longo ele vai dar erro de `fatal error opening dependency file` ou `No such file or directory`. Resolvi isso colocando meu projeto com um path bem curto, mas tente evitar dores de cabeça. Em resumo, use `paths` o mais curto que você conseguir colocar!

# ECU Front
