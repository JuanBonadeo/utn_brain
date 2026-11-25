> **Cómo usarlo.** Hacelo de corrido, sin diccionario, en 3 h (tiempo sugerido por
> mí; es más largo que el examen real, porque trae todos los tipos de consigna de los
> finales). Para el listening, poné `audio/sim6-part1.m4a` y `audio/sim6-part2.m4a`
> **una vez cada uno**, después de leer las consignas. Ojo: el listening es **más
> exigente** que el de los simulacros 1 y 2 (más velocidad, ruido de fondo, acentos
> distintos, correcciones y distractores). Recién al final abrí `simulacro-6-key.md`.
> Los textos y audios son originales.

# INGLÉS II — EXAMEN FINAL (SIMULACRO 6)

ALUMNO, LEG. & FECHA: ……………………………………………………………………

## PART 1-A — LISTENING (15 p.)

### BRAIN-COMPUTER INTERFACES

**QUESTION 1 (5 p.)**
Listen to a lecture about brain-computer interfaces and complete the notes below. Write
**ONLY ONE WORD/NUMBER** in each gap.

1. Hans Berger made the first recording of the electrical activity of a human brain in ……………………… .
2. Sensors placed on the surface of the brain, beneath the skull, are called ……………………… devices.
3. The classic Utah array has ……………………… electrodes.
4. In 2012, a woman with paralysis used a robotic arm to drink ……………………… by herself.
5. The main long-term problem of implants is ……………………… around the electrodes.

**QUESTION 2 (3 p.)**
Listen to the same lecture and complete the diagram of how a speech brain-computer
interface works. Write **NO MORE THAN THREE WORDS AND/OR A NUMBER** in each gap.

    Electrodes in the brain
            ↓
    6. They record signals from the ……………………… cortex
            ↓
    7. A machine-learning model converts the signals into ………………………
            ↓
    8. The sentence is spoken by a digital ………………………

**QUESTION 3 (1 p.)**
Which table shows the speed of the three systems mentioned in the lecture? Write **T**
next to the correct table.

Table A ……

| Year | System | Words per minute |
|---|---|---|
| 2021 | Imagined handwriting | 18 |
| 2023 | Speech decoding, Stanford | 62 |
| 2023 | Speech decoding, San Francisco | 78 |

Table B ……

| Year | System | Words per minute |
|---|---|---|
| 2021 | Imagined handwriting | 18 |
| 2023 | Speech decoding, Stanford | 62 |
| 2023 | Speech decoding, San Francisco | 70 |

Table C ……

| Year | System | Words per minute |
|---|---|---|
| 2021 | Imagined handwriting | 20 |
| 2023 | Speech decoding, Stanford | 62 |
| 2023 | Speech decoding, San Francisco | 78 |

**QUESTION 4 (3 p.)**
Listen to a radio discussion between a neural engineer, **Tom**, and a lawyer,
**Thandi**. Who expresses each idea? Write **T** (Tom), **Th** (Thandi) or **B** (both).

| | Idea | T / Th / B |
|---|---|---|
| a) | Selling implants to healthy people will help to finance medical research. | ……… |
| b) | Neural data needs special legal protection. | ……… |
| c) | Only rich people will be able to afford brain implants. | ……… |

**QUESTION 5 (3 p.)**
When will each of these developments be a reality, according to the speakers? Write
**A**, **B** or **C**.

- A — already available
- B — within the next ten years
- C — unlikely in our lifetime

1. Consumer headbands that measure concentration ……
2. Hospital-approved implants that restore speech ……
3. Direct brain-to-brain communication ("telepathy") ……

## PART 1-B — READING (45 p.)

Read the following text and answer the questions below it.

### Who is looking after the code we all depend on?

*by Nora Whitfield, software engineer*

**A** Almost every application you use, from a banking app to a car's navigation system,
is built on open-source libraries: pieces of code that anyone can read, use and modify
for free. Estimates suggest that between 70 and 90 per cent of the code in a typical
modern application comes from such components. Open-source libraries are invisible to
most users. Almost every modern application depends on them. They are like the pipes
under a city: nobody thinks about them until they break. A single banking app may depend, directly or indirectly, on hundreds of them.

**B** Behind many of these libraries there is a very small team, and often a single
volunteer. Surveys suggest that most of these maintainers are unpaid. They fix bugs in
their free time, and they answer the demands of users who treat a free tool as a paid
service. Many maintainers have thought of quitting. They work unpaid, often at night,
for users who rarely say thank you. The result is burnout, and when a maintainer leaves,
a library that millions of programs depend on may be left without anybody in charge.

**C** This situation is attractive to attackers. Instead of attacking a well-defended
bank directly, criminals attack a library that the bank uses. Once the compromised
version is published, it travels automatically to every project that depends on it, and
the victims install it themselves, because they trust the source. This is called a
<u>supply chain attack</u>: the attacker poisons a component that its victims already
trust, and lets the update do the rest.

**D** For years, a comforting idea held that open source was safe by design. Eric Raymond
famously wrote that, given enough eyeballs, all bugs are shallow: if thousands of people
can read the code, someone will notice every flaw. In 2014, however, a serious flaw known
as Heartbleed was found in OpenSSL, a library that protects a large share of the world's
web traffic. It had gone unnoticed for about two years. The project was maintained by a
handful of people, mostly volunteers, and it received very little funding. Many
programmers had used the code, but hardly anyone had actually studied it. Everybody assumed that somebody else was checking.

**E** A more recent case shows how patient an attacker can be. In 2024, a backdoor was
discovered in xz, a compression tool included in most Linux systems. The story had five
stages. First, an exhausted lone maintainer, under pressure from impatient users,
accepted help from a friendly newcomer, whose real identity remains unknown. Over almost
two years, the newcomer made many useful contributions and gained the maintainer's trust,
and was finally given maintainer rights. Then the newcomer hid malicious code, not in the
main source, where reviewers look, but in test files. The poisoned version began to reach
Linux distributions. Finally, a Microsoft engineer noticed that remote logins were taking
half a second longer than normal. Curious about such a small delay, he investigated and
raised the alarm before the update reached most users.

**F** What can be done? The proposals are practical. First, the companies that profit
from open source can pay maintainers, directly or through foundations, so that nobody has
to work for free. Second, popular libraries can require two-factor authentication from
their maintainers, and a second reviewer for every important change. Third, companies can
keep a software bill of materials, a list of every component their products contain, so
that they can find out within hours whether a newly discovered flaw affects them. None of these measures is expensive compared with the damage of one successful attack.

**G** So who is looking after the code we all depend on? Too often, a few tired
volunteers. Companies that earn billions from open source treat it as a free resource,
and the next attack is a question of when, not if. Unless they share the cost, with
money, with engineers' time and with responsibility, the foundations of the digital world
will remain fragile.

**QUESTION 1 (7 p. — 1 p. each)**
Choose the correct heading for each paragraph A–G from the list below. There are two
extra headings.

| Paragraph | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| Heading | …… | …… | …… | …… | …… | …… | …… |

1. Attacking through a trusted component
2. Practical remedies
3. Why open source is cheaper than commercial software
4. Volunteers close to burnout
5. A responsibility to share
6. Anatomy of a patient attack
7. Software built on borrowed code
8. The rise of AI coding tools
9. A comforting idea that failed

**QUESTION 2 (12 p. — 4 p. each)**

a) With information from paragraph C, write a definition of "supply chain attack".

……………………………………………………………………………………………………………

……………………………………………………………………………………………………………

b) Is Eric Raymond's view in paragraph D ("given enough eyeballs, all bugs are shallow")
supported or contradicted by the Heartbleed case? Account for your answer.

……………………………………………………………………………………………………………

……………………………………………………………………………………………………………

c) What is the author's answer to the question in the title? Account for your answer.

……………………………………………………………………………………………………………

……………………………………………………………………………………………………………

**QUESTION 3 (3 p. — 1 p. each)**
Complete the flow-chart of the xz attack (paragraph E). Write **NO MORE THAN THREE
WORDS from the text** in each of the three empty boxes.

    1. An exhausted lone maintainer accepts help from a friendly ………………………
              ↓
    2. The newcomer gains the maintainer's trust and, finally, maintainer rights.
              ↓
    3. Malicious code is hidden in ………………………, not in the main source.
              ↓
    4. The poisoned version starts to reach Linux distributions.
              ↓
    5. An engineer notices that remote logins take ……………………… longer than normal
       and raises the alarm.

**QUESTION 4 (3 p. — 1 p. each)**
List three measures mentioned in paragraph F to make open-source software safer.

1. ……………………………………………………………………………………………………………

2. ……………………………………………………………………………………………………………

3. ……………………………………………………………………………………………………………

**QUESTION 5 (4 p. — 2 p. each)**
Use the connectors in the box to link the ideas in the following quotes from the text.
You will have to make a few changes to the sentences. There are two extra connectors.

> because – although – unless – until

a) "Open-source libraries are invisible to most users. Almost every modern application
depends on them."

……………………………………………………………………………………………………………

b) "Many maintainers have thought of quitting. They work unpaid, often at night, for
users who rarely say thank you."

……………………………………………………………………………………………………………

**QUESTION 6 (3 p. — 0,5 p. each)**
What words from the text can be replaced by the ones below? They are in order and
should be interchangeable.

1. unseen (A): ………………………
2. giving up (B): ………………………
3. heavily protected (C): ………………………
4. undetected (D): ………………………
5. concealed (E): ………………………
6. inventory (F): ………………………

Read the following text and answer the questions below it.

### Too loud to live with: noise in the city

Noise is the most underestimated form of urban pollution. According to the European
Environment Agency, about one in five Europeans live with noise levels that are harmful
to health. Children living near busy roads or airports, for example, tend to find it harder to concentrate at school. The effects go beyond annoyance: chronic exposure disturbs sleep, raises
stress and increases the risk of heart disease. The World Health Organization recommends
that road traffic noise should stay below 53 decibels during the day and 45 at night, but
in busy streets the levels often exceed 70.

The decibel scale is logarithmic. An increase of 10 decibels means ten times more sound
energy, although the human ear perceives it as only about twice as loud. This is why a
small reduction of 3 decibels, which seems trivial, actually halves the sound energy.

Cities have several tools. Speed limits of 30 km/h reduce noise, because engines and
tyres are quieter at lower speeds, and quieter asphalt can cut traffic noise by several
decibels. Electric vehicles are often presented as the solution. At low speeds, where the
engine is the main source of noise, they are indeed much quieter, and they are silent
when stopped at traffic lights. But above about 30 km/h the noise of the tyres on the
road dominates, so on faster roads the difference is small. In addition, silent cars are
a danger for pedestrians and cyclists, who cannot hear them approach. For this reason,
new electric models in Europe must emit an artificial warning sound at low speeds.

Planners can also separate people from noise. Some cities create "superblocks", groups
of streets closed to through traffic, where residents report much calmer surroundings. Green barriers, for example, improve the look of a street, but they reduce noise only slightly.
However, no single measure is enough: the most effective approach combines lower speeds,
better road surfaces, cleaner vehicles and careful urban design.

**QUESTION 7 (4 p. — 1 p. each)**
Write **T** next to the best answer.

1. The World Health Organization recommends that road traffic noise at night should stay below:
   a. 45 decibels ……
   b. 53 decibels ……
   c. 55 decibels ……
   d. 70 decibels ……
2. An increase of 10 decibels means:
   a. twice as much sound energy, perceived as ten times louder ……
   b. ten times more sound energy, perceived as ten times louder ……
   c. ten times more sound energy, perceived as about twice as loud ……
   d. half the sound energy, perceived as twice as quiet ……
3. Electric vehicles reduce noise significantly:
   a. on all kinds of roads ……
   b. mainly above 30 km/h ……
   c. mainly at low speeds, where the engine is the main source of noise ……
   d. mainly on motorways, because their tyres are quieter ……
4. New electric models in Europe must emit a warning sound because:
   a. the law forbids silent vehicles at any speed ……
   b. pedestrians and cyclists cannot hear them approach ……
   c. their tyres are too noisy at low speeds ……
   d. their engines are noisier than expected ……

**QUESTION 8 (2 p. — 1 p. each)**
What questions about the text do the following statements answer? Write one question
for each statement.

1. "About one in five."

……………………………………………………………………………………………………………

2. "Because, above about 30 km/h, the noise of the tyres dominates."

……………………………………………………………………………………………………………

**QUESTION 9 (4 p. — 1 p. each)**
Note-taking: complete the table with the advantages and disadvantages of electric
vehicles for urban noise, mentioned in the text "Too loud to live with: noise in the
city". Write your answers **IN A TABLE**.

| Advantages | Disadvantages |
|---|---|
| | |
| | |

**QUESTION 10 (3 p. — 0,5 p. each)**
Complete the abstract with the words in the box. There are two extra options.

> because – whereas – which – where – by – However – unless – until

### Compressing neural networks for on-device artificial intelligence

Running deep neural networks on smartphones is difficult (1) ……………… the most advanced
models contain billions of parameters, (2) ……………… mobile devices have limited memory
and battery life. Models that run directly on the device also protect privacy, since personal data never leave the phone. This paper surveys three compression techniques: pruning,
(3) ……………… removes unnecessary connections; quantisation, which stores numbers with
fewer bits; and knowledge distillation, (4) ……………… a small "student" model learns to
imitate a large "teacher". In experiments on several image-recognition tasks and three different smartphones, quantisation
reduced the size of the model (5) ……………… a factor of four, with a loss of accuracy
below one per cent. (6) ……………… , aggressive pruning degraded performance
considerably. We conclude that combining several techniques gives the best balance
between size, speed and accuracy. Future work should evaluate the energy consumption of each technique on real devices.

## PART 2 — WRITING (40 p.)

You are a member of a university seminar for engineering students on technology and
education. As part of the seminar, you have to write an **OPINION ESSAY** (**around 250
words**) with the title:

**"Programming should be a compulsory subject in primary schools."**

Do you agree or disagree? Give reasons and examples. Read the following text and use
its ideas, **in your own words**, in your essay. Do not copy whole sentences.

### Should children learn to code?

Computing has become part of almost every profession, and several countries have
reacted. In England, for instance, computing has been compulsory since 2014 for children
from the age of five. Supporters of this approach say that programming teaches children
to break a problem into small steps and to look for mistakes patiently, skills that are
useful in any subject. A child who programs a character to cross a maze, for example, must test, correct and repeat until it works. They add that children who understand how apps and websites work
become creators of technology and not only users, and that this prepares them for a
labour market in which digital skills are in high demand.

Critics, however, believe that primary school already has too much to teach. Time
devoted to programming is time taken from reading, writing and mathematics, which are
the foundations of all learning. A second objection is that many primary teachers have
no training in computer science. Without well-prepared teachers, lessons may be reduced
to following instructions on a screen, with little real understanding. Teachers who feel insecure about the subject may avoid it or teach it superficially.

Write four paragraphs: (1) introduce the topic and give your opinion; (2) and (3) give
reasons, with examples or data, that support it; (4) a conclusion that restates your
opinion in other words. Take **one** side only.

## ORAL — DEBATE (para practicar)

**Motion:** *"This house believes that companies that profit from open-source software
should be legally obliged to fund its maintainers."*

1. Prepare a 3-minute presentation on why the topic is relevant for engineering students.
2. Prepare three arguments **for** and three **against**, each one with an example or a
   piece of evidence. The examiner will tell you which side to defend.
