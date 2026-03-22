
# 📡 Programação de Microcontroladores com Python

Este diretório contém uma coleção de programas em Python voltados para o aprendizado dos conceitos fundamentais da **programação de microcontroladores** e **sistemas embarcados**.

Os exemplos foram desenvolvidos com foco didático, simulando comportamentos reais de hardware como LEDs, sensores e atuadores, além de incluir uma versão para execução em microcontroladores reais com MicroPython.

---

## 📂 Estrutura dos Arquivos

```
├── led_blink.py              # Simulação de LED piscando
├── botao.py                 # Simulação de entrada digital (botão)
├── controle_led.py          # Controle de LED com toggle
├── sensor_temperatura.py    # Simulação de sensor analógico
├── controle_automatico.py   # Sistema automático (sensor + atuador)
├── sistema_embarcado.py     # Menu estilo firmware
└── led_real.py              # Código para microcontrolador real (ESP32)
```

---

## 🎯 Objetivos

* Compreender conceitos básicos de **GPIO (entrada/saída)**
* Simular o funcionamento de **sensores e atuadores**
* Entender a lógica de **controle embarcado**
* Praticar estruturas de decisão e repetição
* Introduzir o uso de **MicroPython em hardware real**

---

## 🧠 Conceitos Abordados

* Entrada digital (botão)
* Saída digital (LED)
* Leitura de sensores (simulada)
* Controle automático
* Estrutura de firmware
* Interação com hardware (MicroPython)

---

## ▶️ Como Executar

### 🔹 Simulações no computador

Certifique-se de ter o Python instalado:

```bash
python nome_do_arquivo.py
```

Exemplo:

```bash
python led_blink.py
```

---

### 🔹 Execução em microcontroladores (ESP32 / Raspberry Pi Pico)

1. Instale o **MicroPython** no dispositivo

2. Utilize ferramentas como:

   * Thonny
   * uPyCraft
   * VS Code (com extensão)

3. Envie o arquivo:

```bash
led_real.py
```

---

## ⚙️ Requisitos

* Python 3.x
* (Opcional) Microcontrolador compatível com MicroPython:

  * ESP32
  * Raspberry Pi Pico

---

## 🚀 Próximos Passos

* Integração com sensores reais (DHT11, LDR)
* Uso de displays (LCD/OLED)
* Comunicação via Wi-Fi (ESP32)
* Controle remoto via aplicativo ou web
* Persistência de dados

---

## 📚 Finalidade Acadêmica

Este material foi desenvolvido para a disciplina de **Programação de Microcontroladores** no curso de **Ciência da Computação**, com foco em aprendizado progressivo e aplicação prática.

---

## 👨‍💻 Autor mvdevelop

---

## 📌 Observação

Os arquivos simulados não interagem com hardware real, mas representam a lógica utilizada em sistemas embarcados. Para aplicações reais, utilize o código baseado em MicroPython.

---
