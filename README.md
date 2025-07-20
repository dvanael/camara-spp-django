
# Câmara dos Vereadores de São Paulo do Potengi - RN

**Projeto de Interface do Usuário**

[Sobre](#sobre) • [Tecnologias](#tecnologias) • [Apresentação](#apresentação) • [Colabodores](#colaboradores)

---

## Sobre

Uma reconstrução do antigo **[Portal da Câmara de São Paulo do Potengi](https://camaraspp.rn.gov.br/)**, buscando melhorar a experiência e interface do usuário. Adicionalmente com um backend para processamento de funcinalidades dinâmicas.

Esse projeto foi criado para a conclusão da disciplina **Projeto e Interface de Usuário**.

Para a prototipação das telas do projeto, foi utilizado o **Figma**. [Confira os prototipos aqui!](https://www.figma.com/design/P9IzMY8T5NImyTdwmuTX72/CAMARA-MUNICIPAL---PROTOTIPO-BAIXA-FIDELIDADE?node-id=0-1&t=sxuRjeeXWv4zEKa5-1)

No desenvolvimento do projeto, foi priorizado **principios de UI/UX, Mobile First e Responsividade**.

Esse projeto é a continuidade de um frontend estático, acesse o repositório [Câmara SPP](https://github.com/dvanael/camara-spp).

---

### Funcionalidades

As funcionalidades implementadas no **Django**:

- **Pesquisa de páginas** do Portal

- **Pesquisa e filtragem** de Projetos de Lei

- **Paginação** de objetos

- **Formulários funcionais** com notificação de envio
  
---

## Tecnologias

![Django][DJANGO__BADGE]
![Python][PYTHON__BADGE]
![HTML][HTML__BADGE]
![CSS][CSS__BADGE]
![Javascript][JAVASCRIPT__BADGE]
![Bootstrap][BOOTSTRAP_BADGE]
![Figma][FIGMA__BADGE]

## Documentação de cores

Cores usadas no projeto.

| Cor               | Hexadecimal                                                        |
| ----------------- | ----------------------------------------------------------------   |
| Branco       | ![#E4E7E7](https://placehold.co/20x20/e4e7e7/e4e7e7)  #E4E7E7             |
| Preto       | ![#0C0D0D](https://placehold.co/20x20/0c0d0d/0c0d0d) #0C0D0D |
| Azul       | ![#0B45F4](https://placehold.co/20x20/0b45f4/0b45f4) #0B45F4 |
| Azul Pastel       | ![#668CFF](https://placehold.co/20x20/668cff/668cff) #668CFF |

---

## Apresentação

Gravações e imagens do site funcionando.

<img width="800" height="503" alt="image" src="https://github.com/user-attachments/assets/4d72e1a0-58a9-4b12-a8ad-7143cc8dc145" />


---

**Página de resultados de pesquisa**

<img width="1315" height="943" alt="image" src="https://github.com/user-attachments/assets/5420adce-be65-42df-9a40-0eb8b7c7b1a6" />

---

**Tabela de projetos de lei com filtragem**

<img width="1302" height="947" alt="image" src="https://github.com/user-attachments/assets/a91ce342-8138-44f9-85cc-d532edba5377" />

---

## Instalação

- Clone o [repositório](https://github.com/dvanael/camara-spp-django)

```bash
git clone https://github.com/dvanael/camara-spp-django.git
```

- Crie um ambiente virtual

```bash
python -m venv .venv
```

- Ative o ambiente virtual

_windows_
```powershell
.venv/Scripts/activate
```
_linux, macOs_
```bash
source .venv/bin/activate
```

- Instale as dependências

```bash
pip install -r requirements.txt
```

- Crie as variáveis de ambiente

```bash
python scripts/env.py
```

- Faça as migrações necessárias

```bash
python manage.py migrate
```

- Crie um **super usuário**.

```bash
python manage.py createsuperuser
```

- Rode o servidor

```bash
python manage.py runserver
```

- Acesse a aplicação localmente: **[localhost:8000/](http://localhost:8000/)**

- Adicione objetos no banco de dados para testar as funcionalidades.

---


## Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/dvanael" title="Ana Barbosa">
        <img src="https://avatars.githubusercontent.com/dvanael" width="100px;" alt="collaborators pictures"/><br>
        <sub>
          <b>Ana Barbosa</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Thaynix" title="Thaisy Juliany">
        <img src="https://avatars.githubusercontent.com/Thaynix" width="100px;" alt="collaborators pictures"/><br>
        <sub>
          <b>Thaisy Juliany</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/JoaoP360" title="João Pedro Moura">
        <img src="https://avatars.githubusercontent.com/JoaoP360" width="100px;" alt="collaborators pictures"/><br>
        <sub>
          <b>João Pedro Moura</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---

[DJANGO__BADGE]: https://img.shields.io/badge/-DJANGO-0d1117?style=for-the-badge&logo=django&logoColor=green
[PYTHON__BADGE]: https://img.shields.io/badge/-PYTHON-0d1117?style=for-the-badge&logo=python&logoColor
[HTML__BADGE]: https://img.shields.io/badge/-HTML5-0d1117?style=for-the-badge&logo=html5&logoColor
[CSS__BADGE]: https://img.shields.io/badge/-CSS3-0d1117?style=for-the-badge&logo=css&logoColor=blue
[JAVASCRIPT__BADGE]: https://img.shields.io/badge/-JavaScript-0d1117?style=for-the-badge&logo=javascript&logoColor
[FIGMA__BADGE]: https://img.shields.io/badge/-Figma-0d1117?style=for-the-badge&logo=figma&logoColor
[BOOTSTRAP_BADGE]: https://img.shields.io/badge/-Bootstrap-0d1117?style=for-the-badge&logo=bootstrap&logoColor
