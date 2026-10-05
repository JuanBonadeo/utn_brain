Proceedings of the 2024 Winter Simulation Conference
H. Lam, E. Azar, D. Batur, S. Gao, W. Xie, S. R. Hunter, and M. D. Rossetti, eds.
ENHANCING PASSENGER FLOW AT SUBWAY TRANSFER STATIONS THROUGH
SIMULATION MODELING
Dongyang Zhen1, Zhuoxuan Liu2, Yonghao Chen3, and Qingbin Cui1
1Dept. of Civil and Environmental Engineering, University of Maryland, College Park, MD, USA
2China Academy of Public Finance and Public Policy, Central University of Finance and Economics,
Beijing, CHINA
3Dept. of Civil Engineering & Engineering Mechanics, Columbia University, New York, NY, USA
ABSTRACT
With the increased popularity of the public transportation field, congestion in multi-line subway transfer
hubs has become one of the hot issues. This study presents a comprehensive simulation model utilizing
AnyLogic software to evaluate the performance of the 59th-Street-Columbus Circle subway transfer station
in New York City by addressing challenges of inefficient passenger flow management. Leveraging the
NYC turnstile usage data, the simulation focuses on this major three-level transfer hub to analyze passenger
flows, identify bottlenecks, and evaluate potential solutions. Extensive simulation experiments reveal criti-
cal high-density regions prone to severe congestion, particularly at intersections. With an inverse relation-
ship between crowd density and average passenger speed, higher densities lead to near-stagnant conditions
during peak hours. By providing data-driven insights through simulation analyses, this research aims to
enhance the commuter experience, reduce delays, ensure efficient behavior at vital transit hubs, and contri-
bute to more-sustainable urban transportation by encouraging public transit usage.
1 INTRODUCTION
Subway transfer stations are critical nodes in urban rail transit systems, serving as connecting points where
passengers can change lines or modes of transportation. These stations play a pivotal role in facilitating
seamless travel and ensuring the efficient movement of commuters within cities. However, the operation
of transfer stations is often delayed by various challenges that can lead to congestion, long waiting times,
and overall inefficiency (Shi et al. 2020). One of the primary challenges faced in transfer station behavior
is the management of high passenger volumes during peak hours. The convergence of multiple transit lines
at these stations can result in overwhelming crowds, straining the station's capacity and leading to
bottlenecks (Kim et al. 2017). Insufficient passenger flow management, badly organized subway transfer
routes, and complex construction design can further exacerbate these issues, causing overcrowding and
potential danger to all passengers (Li and Zhou 2013). Another significant challenge is the coordination of
train schedules and dwell times. Misalignment between the arrival and departure times of different transit
lines can lead to extended waiting periods for transferring passengers, thereby reducing the overall
efficiency of the system (Nie et al. 2021). Additionally, unexpected platform overload and travel delays
due to passenger congestion can disrupt the entire network, causing profound effects throughout the transit
system.
To address these challenges and evaluate the performance of subway transfer stations, simulation
modeling has emerged as a powerful tool. Simulation techniques enable the construction of virtual
representations of transfer stations, allowing for the exploration of various scenarios and the evaluation of
different strategies before implementation in the real world (Li et al. 2012). By leveraging simulation
models, transportation planners and operators can gain valuable insights into the complex dynamics of
979-8-3315-3420-2/24/$31.00 ©2024 1398

Zhen, Liu, Chen, and Cui
passenger flow, identify potential bottlenecks, and test the effectiveness of proposed solutions. Meanwhile,
it can also help to analyze the impact of layout modifications, operational adjustments, and passenger flow
management strategies on transfer station efficiency. This approach enables data-driven decision-making,
facilitating the identification of optimal solutions that can minimize congestion, reduce waiting times, and
enhance the overall experience for commuters (Zhang et al. 2022). The significance of this research lies in
the development of more efficient and sustainable urban transportation transfer systems. By optimizing the
passenger flow and travel time of subway transfer stations, cities can encourage a higher capacity of public
transit, reduce reliance on private vehicles, and mitigate the negative environmental impact associated with
traffic congestion and emission.
2 LITERATURE REVIEW
Numerous research efforts have been addressing the challenges faced in subway transfer station behavior
through various approaches, especially in simulation modeling. One study highlighted the potential of
dynamically adjusting pedestrian routing and crowd control measures to alleviate congestion and reduce
waiting times at transfer stations (Owais et al. 2021). Another study employed a discrete event simulation
approach to analyze the effects of platform and concourse layout modifications on passenger movements
and overall station performance (Xu et al. 2014, Yang et al. 2017). In addition to layout optimization,
researchers have also explored the role of operational strategies in enhancing transfer station efficiency.
For example, a simulation framework was utilized to investigate the benefits of real-time train rescheduling
and dynamic platform assignment adjustments in response to disruptions or overcrowding situations at
transfer hubs. The findings demonstrated the potential for significant improvements in passenger
throughput and reduced transfer times by implementing such measures (Yap et al. 2019).
Simulation modeling techniques have been widely adopted across various transportation domains to
study complex systems and evaluate potential solutions, encompassing diverse methodologies and
applications. Discrete event simulation (DES) and agent-based modeling (ABM) are among the most
commonly employed simulation approaches in the context of subway transfer station optimization (Marsha
et al. 2021). DES models simulate the movement of discrete entities (e.g., passengers) through a system
over time, effectively capturing their interactions at a microscopic level and enabling the study of the overall
system dynamics that emerge (Zhang et al. 2014). On the other hand, ABM is focused on modeling the
individual behavior and decision-making processes of autonomous agents within the system, allowing for
the exploration of emergent patterns and phenomena arising from the interactions between agents and their
environment.
Other simulation techniques have also found valuable applications in the analysis and design of
transportation systems. Microsimulation models provide an extremely detailed representation by simulating
the movements and interactions of individual entities such as vehicles or pedestrians within the system.
While computationally intensive, this high-fidelity approach can capture intricate dynamics that may be
overlooked in more aggregate models (Merz 1991). Contrastingly, mesoscopic simulation aims to strike a
balance between computational efficiency and the level of detail modeled, representing entities at an
intermediate level of aggregation between microscopic and macroscopic scales. This approach can be
advantageous when studying large-scale systems where a fully disaggregated representation is infeasible
or unnecessary.
While the studies conducted to date have contributed valuable insights into optimizing subway transfer
station behavior, several significant gaps remain in the existing literature. Many research efforts have
focused narrowly on specific aspects of transfer station design or behavior, such as layout configuration,
passenger flow management strategies, or operational policies, without comprehensively considering the
complex interactions and combined impact of these factors on overall system efficiency. Furthermore, a
substantial portion of prior work has relied heavily on simplified assumptions, limited real-world data, or
isolated case studies, potentially failing to adequately capture the nuances, variabilities, and multi-faceted
nature of large complex transfer station environments.
1399

Zhen, Liu, Chen, and Cui
Addressing these gaps, this research study aims to develop a comprehensive, agent-based simulation
model that captures the dynamic of passenger flow and movement in a subway transfer station. The research
could give inspiration for future passenger throughput management such as station layout and transfer route
design, operational decision policies, crowd management procedures, and stochastic demand patterns. By
leveraging advanced simulation techniques, extensive real-world data sets, and empirically grounded
behavioral models, this research endeavors to provide a more realistic and representative virtual
environment for studying transfer station performance under diverse scenarios.
3 METHODOLOGY
3.1 Anylogic Software
Anylogic is a multifaceted simulation software that supports system dynamics, discrete events, and agent-
based modeling. It is well-known for its flexibility and capacity to model complex systems in various fields,
including transportation, healthcare, manufacturing, and logistics. For this study, Anylogic's comprehensive
toolkit for transportation and pedestrian flow simulation offers a robust platform to accurately model the
intricacies of passenger movements and interactions within a subway system. The software’s ability to
integrate different simulation methodologies and its extensive library of pre-built models and components
make it an ideal choice for modeling the dynamic environment of a transfer subway system. Additionally,
Anylogic’s pedestrian generator library is specifically designed to simulate the behavior and movements of
individuals in crowded spaces, making it particularly relevant for this study of passenger flow in subway
systems.
3.2 Simulation Model
Within this model, the authors simulate the multifaceted process by which passengers transfer between lines
as they travel towards their destinations. This includes the detailed modeling of train arrivals, passenger
flows, as well as flow exchange between layers, which are fundamental components of the system's
operation, influencing passenger flow and the overall efficiency of the subway network. At its core, a
discrete event simulation framework is deployed to model the movement of passengers through the transfer
station over time. Discrete event logic models and simulates the operational process, including train sched-
ules, platform assignments, and crowd control measures. Besides the discrete event simulation framework,
an agent-based modeling element is also incorporated to capture the decision-making process and dynamic
patterns that arise from the interaction between individuals. Each passenger will be represented as an
autonomous agent with different arrival time, subway station entrance selections, and route planning bet-
ween platforms. This agent-based element will help to explore the microscopic behavior scaled up to
macroscopic behavior, such as crowd formation, bottlenecks, and congestion patterns. By seamlessly
combining these simulation techniques, the proposed model will offer a realistic and multi-scale represen-
tation of transfer station behavior. It will enable the analysis of diverse scenarios, ranging from routine
behavior to disruptions, crowding, and emergency situations. The model will be calibrated and validated
using extensive real-world data, including passenger flow data from NYC turnstile counts.
By capturing these key dynamics, the model offers a powerful tool for understanding and improving
the efficiency and user experience of subway systems with line transfers. It enables transportation planners
and engineers to test various operational strategies and station designs in a virtual environment, thereby
identifying solutions that can enhance the flow of passengers, reduce congestion at critical points, and
ultimately improve the overall performance of the subway network. To conduct the simulation, the
following assumptions are adopted:
1. Train Arrival Times: Trains arrive at each station according to a Poisson process with rate 𝜆 ,
(cid:3047)
which simplifies the variability of arrival times during peak and off-peak hours.
1400

Zhen, Liu, Chen, and Cui

2.  Passenger Arrival Rates: Passengers arrive at stations following a separate Poisson process with
| rate 𝜆 |  , differentiated for peak and off-peak hours.  |     |     |     |     |     |     |     |
| ------ | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
(cid:3017)
3.  Walking Speeds: All passengers are assumed to have a uniform walking speed 𝑣, simplifying the
model by not accounting for variability among individuals.
4.  Transfer Decisions: Passengers choose the shortest path to their destination without considering
real-time conditions such as congestion or delays.

  In the simulation, Queueing Theory is used for the passenger source generator. Queue models allow us
to simulate various scenarios with a high degree of realism by capturing the essence of how passengers
arrive, wait, and are serviced boarding or alighting trains. These models are based on probabilistic laws that
account for the randomness of events such as train arrivals and passenger entry into the station. By
leveraging these models, the impact of different factors – such as train frequency, platform layout, and
passenger arrival rates – on overall system efficiency and passenger satisfaction is evaluated (Wang et al.
2021):

  Train Dynamics: The time between train arrivals 𝑇  at a given station for a specific line follows an
(cid:3028)
exponential distribution due to the Poisson process assumption:
|     |     |     |     | 𝑇 ∼        | 𝐸𝑥𝑝(cid:4666)𝜆 | (cid:4667)   |     | (cid:4666)1(cid:4667)  |
| --- | --- | --- | --- | ---------- | -------------- | ------------ | --- | ---------------------- |
|     |     |     |     | (cid:3028) |                | (cid:3047)   |     |                        |
  Passengers Arrival Dynamics: The number of passengers 𝑁  arriving at a station in a given time
(cid:3017)
interval follows a Poisson distribution:
|     |     |     | 𝑁   | (cid:4666)𝑡(cid:4667) ∼ | 𝑃𝑜𝑖𝑠𝑠𝑜𝑛(cid:4666)𝜆 | ∗𝑡(cid:4667)  |     | (cid:4666)2(cid:4667)  |
| --- | --- | --- | --- | ----------------------- | ------------------ | ------------- | --- | ---------------------- |
|     |     |     |     | (cid:3017)              |                    | (cid:3017)    |     |                        |
  Passenger Flow and Congestion: The model of passenger flow through the station, especially at
transfer points, uses an M/M/1 queueing system for simplicity, where the arrival rate 𝜆  and service
(cid:3017)
rate 𝜇 (related to train capacity and frequency) are key parameters. The average number of
passengers in the system 𝑁  and the average time a passenger spends in the system 𝑇  are given by:
(cid:3046) (cid:3046)
𝜆
|     |     |     |     | 𝑁   | (cid:3404) (cid:3017) |     |     | (cid:4666)3(cid:4667)  |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | ---------------------- |
(cid:3046)
𝜇(cid:3398)𝜆
(cid:3017)
1
|     |     |     |     | 𝑇   | (cid:3404) |     |     | (cid:4666)4(cid:4667)  |
| --- | --- | --- | --- | --- | ---------- | --- | --- | ---------------------- |
(cid:3046) 𝜇(cid:3398)𝜆
(cid:3017)
  Train Capacity Constraints: The probability 𝑃  that 𝑘 passengers board a train is modeled assuming
(cid:3038)
a binomial distribution, reflecting the constraint of train capacity:
|     |     |     |     | 𝐶                                  |                        | (cid:4667)(cid:3004)(cid:2879)(cid:3038)  |     |                        |
| --- | --- | --- | --- | ---------------------------------- | ---------------------- | ----------------------------------------- | --- | ---------------------- |
|     |     |     | 𝑃   | (cid:3404) (cid:4672) (cid:4673) 𝑃 | (cid:4666)1(cid:3398)𝑃 |                                           |     | (cid:4666)5(cid:4667)  |
|     |     |     |     | (cid:3038) 𝑘                       | (cid:3038)             | (cid:3038)                                |     |                        |

  Besides, passengers normally move between B1, B2 and middle layers. This movement is driven by
the  need  to  transfer  between  lines  or  access  different  station  exits.  This  paper  identifies
𝑟  ,𝑟 , as well as 𝑟  ,𝑟  as the rate of transition between layers. The
| (cid:3003)(cid:2869)→(cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032) | (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032)→(cid:3003)(cid:2870) |     | (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032)→(cid:3003)(cid:2869) |     | (cid:3003)(cid:2870)→(cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032) |     |     |     |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --- | --------------------------------------------------------------------------------- | --- | --------------------------------------------------------------------------------- | --- | --- | --- |
Passenger Flow Dynamics can be expressed as:

  For B1 layer:
Δ𝑃 (cid:3404) (cid:3398)𝑟 ⋅𝑃 ⋅Δ𝑡(cid:3397)𝑟 ⋅𝑃 ⋅Δ𝑡  (cid:4666)6(cid:4667)
|     |     | (cid:3003)(cid:2869) | (cid:3003)(cid:2869)→ Middle  | (cid:3003)(cid:2869) |     | Middle →(cid:3003)(cid:2869) | Middle  |     |
| --- | --- | -------------------- | ----------------------------- | -------------------- | --- | ---------------------------- | ------- | --- |
  For Middle layer:
Δ𝑃 (cid:3404) (cid:4672)𝑟 ⋅𝑃 (cid:3397)𝑟 ⋅𝑃 (cid:4673)⋅Δ𝑡  (cid:4666)7(cid:4667)
|     |     | (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032)(cid:2869) | (cid:3003)(cid:2869)→ Middle  |     | (cid:3003)(cid:2869) | (cid:3003)(cid:2870)→ Middle  | (cid:3003)(cid:2870) |     |
| --- | --- | ---------------------------------------------------------------------- | ----------------------------- | --- | -------------------- | ----------------------------- | -------------------- | --- |
(cid:4666)8(cid:4667)
|     | Δ𝑃  | (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032)(cid:2870) (cid:3404) (cid:4672)𝑟 |                                                                   | ⋅𝑃            | (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032) (cid:3397)𝑟 |                                                                        | ⋅𝑃 (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032) (cid:4673)⋅Δ𝑡  |                        |
| --- | --- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------- |
|     |     |                                                                                               | (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032)→ B1  |               |                                                                          | (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032)→ B2       |                                                                                |                        |
|     |     |                                                                                               | Δ𝑃                                                                | (cid:3404) Δ𝑃 |                                                                          | (cid:3398)Δ𝑃                                                           |                                                                                | (cid:4666)9(cid:4667)  |
|     |     |                                                                                               | Middle                                                            |               | (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032)(cid:2869)   | (cid:3014)(cid:3036)(cid:3031)(cid:3031)(cid:3039)(cid:3032)(cid:2870) |                                                                                |                        |
  For B2 layer:
Δ𝑃 (cid:3404) (cid:3398)𝑟 ⋅𝑃 ⋅Δ𝑡(cid:3397)𝑟 ⋅𝑃 ⋅Δ𝑡  (cid:4666)10(cid:4667)
|     |     | (cid:3003)(cid:2870) |                               | (cid:3003)(cid:2870) |     |                              |         |     |
| --- | --- | -------------------- | ----------------------------- | -------------------- | --- | ---------------------------- | ------- | --- |
|     |     |                      | (cid:3003)(cid:2870)→ Middle  |                      |     | Middle →(cid:3003)(cid:2870) | Middle  |     |

1401

Zhen, Liu, Chen, and Cui
3.3 Data Collection and Preparation
When developing the simulation model focused on a subway station with line transfers, the foundation of
realistic and accurate modeling lies in the robustness and relevance of the data collected. For this purpose,
the primary dataset was the 2022 turnstile usage data, which provides comprehensive information on
passenger flows within the New York City's subway system. This dataset, publicly available and widely
regarded for its granularity and accuracy, records the number of entries and exits at each turnstile within
the subway system, offering a detailed snapshot of passenger movements across different times and stations.
This paper chooses the 59th-Street Columbus Circle station in New York City as the base model. Selecting
this station as the simulation focus, the study leverages the essence of this major transfer hub within the
New York City Subway system, distinguished by its high passenger volume, service by multiple lines, and
a complex three-layered layout (B1, Middle, B2) as shown in Figure 1. This structure makes it a prime
candidate for a detailed analysis of passenger movements, including transfers between different levels and
the impact of station design on flow and congestion. The availability of comprehensive operational data
supports the development of an accurate simulation model. Insights from this pivotal station are not only
directly applicable to optimizing its operation and enhancing the commuter experience but also offer
valuable strategies that can be scaled to improve the broader subway network, addressing challenges
inherent to multi-layered urban transit systems.
Figure 1: 59th-Street Columbus Circle: (a) construction design (3D Models); (b) Anylogic simulation
environment set up.
The raw turnstile usage data, while extensive, required significant preprocessing to align it with the
needs of the simulation model. The following steps were taken to clean the data:
 Normalization of arrival rates: Given the variability in passenger arrivals across different days and
hours, this paper normalized the data to fit the simulation timeframe. This involved calculating
average hourly arrival rates for a typical weekday, allowing us to model both peak and off-peak
scenarios with a high degree of accuracy.
 Adjustment of train capacities: To reflect real-world constraints and operational practices, the study
adjusted the train capacities in the model based on the observed maximum and average passenger
counts during peak hours. This adjustment ensures that the simulation realistically captures the
limits of the system's capacity to accommodate passenger flow.
 Remove outliers and missing values: This step involved removing anomalies and outliers from the
data, such as days with atypical usage patterns (due to holidays or special events) and turnstiles
with malfunctioning counters, ensuring the cleanliness of the data was paramount to maintaining
the integrity of the simulation results.
1402

Zhen, Liu, Chen, and Cui

  Timeframe segmentation: To accurately model different parts of the day, the data have been
segmented into time blocks corresponding to periods. The Poisson distribution is calibrated from
the turnstile schedule data due to the absence of inherent stochastic properties in the deterministic
schedule. This calibration allows for the incorporation of randomness and variability in passenger
arrivals, which the schedule data alone cannot adequately represent.

  The turnstile data indicate a time-of-day pattern where passenger traffic is lowest in the early morning
(00:00-04:00) and increases sharply for the morning rush (08:00-12:00), with the station seeing the highest
exit numbers. Midday hours (12:00-16:00) show the peak in both entries and exits, indicating the busiest
period. Late afternoon into evening (16:00-20:00) remains busy, especially for entries. Late-night hours
(20:00-00:00) experience a moderate decrease in traffic. These patterns reflect typical rush and off-peak
hours of urban subway use.
Table 1: Passenger flow in time-of-a-day.
| Hour  | Statistic  | Sum    | Mean   | Std Dev  | Min  | Max     |
| ----- | ---------- | ------ | ------ | -------- | ---- | ------- |
|       | ENTRANCE   | 4,625  | 3,263  | 1,680    | 784  | 88,110  |
20:00-0:00
|     | EXIT      | 3,899  | 3,002  | 2,020  | 517  | 81,057  |
| --- | --------- | ------ | ------ | ------ | ---- | ------- |
|     | ENTRANCE  | 700    | 486    | 252    | 117  | 13,611  |
0:00-4:00
|     | EXIT      | 1,082  | 574  | 298  | 238  | 16,059  |
| --- | --------- | ------ | ---- | ---- | ---- | ------- |
|     | ENTRANCE  | 1,302  | 897  | 415  | 330  | 25,126  |
4:00-8:00
|     | EXIT      | 6,768  | 4,271  | 874    | 2,190  | 119,587  |
| --- | --------- | ------ | ------ | ------ | ------ | -------- |
|     | ENTRANCE  | 4,489  | 3,313  | 1,730  | 899    | 89,460   |
8:00-12:00
|     | EXIT      | 17,333  | 11,526  | 4,364  | 4,921  | 311,198  |
| --- | --------- | ------- | ------- | ------ | ------ | -------- |
|     | ENTRANCE  | 9,760   | 6,715   | 3,535  | 2,001  | 188,012  |
12:00-16:00
|     | EXIT      | 18,963  | 9,441  | 6,300  | 2,120  | 264,344  |
| --- | --------- | ------- | ------ | ------ | ------ | -------- |
|     | ENTRANCE  | 13,715  | 9,353  | 3,831  | 3,354  | 261,873  |
16:00-20:00
|     | EXIT  | 10,933  | 8,415  | 5,101  | 1,464  | 235,615  |
| --- | ----- | ------- | ------ | ------ | ------ | -------- |
3.4  Simulation Flow Setup
The simulation flow setup involves multiple interconnected steps (Figure 2). Initially, the inputs include a
passenger flow generator, transfer station design, and subway time schedule data. These feed into setting
up the geometry and underlying algorithms, incorporating elements like passenger flows from different
lines,  escalator  movements,  entrance  turnstiles,  and  train  schedules  across  multiple  lines.  The  core
passenger flow interconnection happens through distinct layers – B1, middle, and B2 – representing
different sections or floors of the transfer station. Finally, the simulation outputs include data recording and
visualization via heat maps, providing insights into passenger density and movement patterns across the
various interconnected areas of the station complex. This modular approach aims to accurately model the
intricate passenger flows, transfers, and potential bottlenecks within the multi-level multi-line subway
station environment.
4  EXPERIMENT RESULTS AND ANALYSIS
The simulation experiments yielded extensive data and insights into the passenger flow dynamics at the
59th-Street Columbus Circle subway transfer station. One of the key findings was the identification of
critical bottlenecks and high-density regions within the station complex. The regional density maps
generated from the simulation models revealed several hotspots where passenger congestion tended to occur,
particularly at intersections of major pedestrian pathways and near entrances and exits. These areas were

1403

Zhen, Liu, Chen, and Cui
marked by deep red zones, indicating dangerously high crowd densities that could potentially impede
efficient passenger movement and pose safety risks. Notably, the congestion levels appeared to worsen
during simulated peak hours, exacerbating the bottleneck effects. Further analysis of the time distribution
data highlighted prolonged dwell times for passengers attempting to enter or exit the station through these
bottleneck areas, with some individuals experiencing delays of over ten minutes to complete their transfers.
Figure 2: Simulation modeling pipeline.
According to Figure 3, the overall heatmap in the top left corner suggests that the majority of passenger
flow is concentrated along the main thoroughfare of the station, with particularly high densities at platform
access points, turnstile areas, and especially at junctions where passengers might converge or diverge from
different directions. The B1 layer heatmap in the top right shows a similar pattern but with reduced density,
indicating this level might be less traveled or has a more efficient flow. The middle layer in the bottom left
shows less intensity in density, suggesting it could be a transition area or a less busy platform. The B2 layer
heatmap in the bottom right, conversely, displays a high-density area on the platforms themselves, which
could correspond to either a busy line or a bottleneck in passenger movement. These maps are instrumental
for understanding the flow and can inform station management and design to improve traffic, enhance
safety, and increase efficiency by, for example, expanding capacity in high-density areas or optimizing the
flow in transition zones.
Another crucial aspect examined by simulation was the average passenger flow speed within the station.
The results demonstrated a clear inverse relationship between crowd density and average speed, with higher
densities leading to slower overall passenger movements. During off-peak periods, when the station was
less crowded, the average speed hovered around the expected range of 0.5-0.7 meters per second. However,
as passenger volumes increased, the average speed progressively decreased, dropping to alarmingly low
levels of 0.2-0.3 meters per second during the simulated peak hours. This drastic reduction in speed not
only caused significant delays for individual passengers, but also had ripple effects on the overall efficiency
of the transfer process. Furthermore, the simulation revealed a bunch of low-motion flow in specific high-
density areas, where passengers were essentially trapped in a crowd lock, unable to make meaningful
1404

Zhen, Liu, Chen, and Cui
progress towards their destinations. Figure 4 illustrates the average speed of pedestrians over the simulation
time. The initial high speed (around 9 km/h) rapidly decreases and fluctuates around 3 km/h for the majority
of the simulation duration. This pattern suggests that pedestrians encounter congestion or obstructions that
cause their speed to decrease and vary over time. Such variations in pedestrian speed can contribute to the
formation of bottlenecks and congestion within the station. The queue length at the B1MiddleOut location,
as shown in Figure 5, exhibits periodic spikes, indicating recurring periods of congestion or bottlenecks at
this particular point within the station. In Figure 5(c), the queue length rises sharply to around 0.8 persons
and then quickly dissipates, suggesting short-lived congestion events. However, in Figure 5(d), the queue
length shows more pronounced spikes, with some peaks reaching up to 2.8 persons, potentially representing
more severe congestion episodes at the B1MiddleOut location.
Figure 3: Passenger flow heatmap: (a) overall; (b) B1 Layer; (c) Middle Layer; (d) B2 Layer.
Based on the comprehensive simulation data, it became evident that the current station design and
operational strategies were inadequate to handle the projected passenger volumes, particularly during peak
periods. The analysis highlighted the need for targeted interventions and design modifications to alleviate
the identified bottlenecks and improve overall transfer efficiency. Potential solutions could involve
reconfiguring pedestrian pathways, strategic placement of barriers or guidance systems to better organize
passenger flows, and increasing the capacity of critical chokepoints through additional entrances and exits
or wider corridors. Additionally, the simulation underscored the importance of implementing dynamic
crowd management strategies, such as adaptive signage, real-time monitoring, and proactive personnel
deployment to manage congestion during peak hours. By scenario exploration and parameter tuning, the
optimal scenario with the least system total waiting time was identified, in which the two parameters
passenger arriving rate 𝜆 and rate of transition 𝑟 are significantly lower than the baseline scenario. By
(cid:3043)
leveraging these insights, transit authorities can enhance the commuter experience, reduce delays, and
1405

Zhen, Liu, Chen, and Cui
ensure the safe and efficient operation of this vital transportation hub. According to Figure 6, all three layers
are suffering travel delays, at least three times during the overall simulation. Among them, the B2 Layer
has a longer tail on delay distribution, indicating that it has a greater probability of longer delay.
Figure 4: Average speed of pedestrians.
Figure 5: Queueing length over simulation time: (a) B1 Middle Out; (b) B1 Middle in; (c) B1 Left Out; (d)
B1 Down Out
1406

Zhen, Liu, Chen, and Cui
Figure 6: Average delay on Layers (a) B1; (b) Middle; (c) B2.
These findings highlight the importance of identifying and addressing potential bottlenecks or conges-
tion points within the subway station. The periodic spikes in queue lengths at specific locations, such as
B1MiddleOut and B1DownOut, warrant further analysis and the implementation of mitigation strategies to
improve passenger flow and reduce congestion. Additionally, the varying arrival patterns and pedestrian
speeds observed underscore the need for a comprehensive approach to optimizing the station's design and
behavior to accommodate diverse pedestrian behavior and dynamics.
5 CONCLUSION
This comprehensive simulation study employed the AnyLogic software to comprehensively analyze and
evaluate the passenger flow dynamics and transfer efficiency at the critically important 59th-Street
Columbus Circle subway transfer station in New York City. By constructing detailed computational models
and running various simulated scenarios, the research was able to gain unprecedented insights into key
performance metrics such as local crowd densities, average pedestrian speeds, and time distributions for
entering and exiting the station premises. These quantitative measures provided an objective lens through
which to assess the station's operational capabilities and identify potential shortcomings or areas requiring
improvement.
The initial simulation runs yielded worrying results that brought to light several significant issues
because of the station's current infrastructure and design. Alarmingly high regional densities were detected
at multiple convergence points and intersections where passenger flows from various directions converged.
These hotspots of overcrowding not only prevented the smooth movement of individuals, but also exposed
potential safety hazards due to the increased risk of crowd-related incidents. Furthermore, the time
distribution data revealed extended delays experienced by passengers attempting to enter or exit the station
through these congested bottleneck areas, with some commuters enduring frustrating wait times exceeding
ten minutes to complete their transfers.
1407

Zhen, Liu, Chen, and Cui
Compounding the challenges posed by localized crowding, the simulation also uncovered a clear in-
verse relationship between passenger volume and average flow speed throughout the station complex. As
the simulated peak hours progressed and the station became increasingly populated, the overall average
speed of pedestrian movement declined precipitously. By the end of the simulation period, these speeds had
decreased to sub-optimal levels, indicative of severely unsmooth mobility and stagnant conditions in certain
high-density zones. This phenomenon not only exacerbated delays for individual commuters. but also
profoundly impacted the overall transfer efficiency of the entire station, thereby undermining its core
functional purpose.
The simulation results proposed new directions on the current station's ability to adequately serve the
needs of the city's rapidly growing population and the ever-increasing demands placed on its public trans-
portation infrastructure. To be specific, rather than representing an intractable problem, these findings
present a valuable opportunity for transit authorities to leverage data-driven insights and implement targeted
interventions to alleviate congestion and improve transfer performance. Potential solutions could involve
reconfiguring pedestrian pathways, optimizing the placement of vertical transportation facilities such as
escalators and staircases, or implementing dynamic crowd control measures during peak periods. By
embracing simulation-based analyses and iterative design optimization, urban planners and transportation
officials can enhance the commuter experience, increase operational efficiency, and ensure that vital transit
hubs like 59th-Street Columbus Circle remain capable of serving the public transit needs of densely
populated urban centers.
REFERENCES
Anon 3D Models. 2024. Project Subway NYC. http://www.projectsubwaynyc.com/3d-models , accessed 12th April.
Kim, C., S.W. Kim, H.J. Kang, and S.M. Song. 2017. What Makes Urban Transportation Efficient? Evidence from Subway
Transfer Stations in Korea. Sustainability 9(11):2054.
Li, W and J. Zhou. 2013. The Optimize Management of Passenger Organization in Transfer Station based on Dynamic Passenger
Flow Analysis. Procedia – Social and Behavioral Sciences 96:1322–1328.
L, Y., X. Sun, X. Feng, C. Wang, and J. Li. 2012. Study on Evacuation in Subway Transfer Station Fire by STEPS. Procedia
Engineering 45:735–740.
Marsha, D.V., R. Sarno, and K.R. Sungkono. 2021. Standard Operating Procedure Optimization of Resource Level for Hospital
Waste Handling Using Hybrid DES-ABM Simulation, Genetic Algorithm, and Goal Programming. In Proceedings of the 3rd
International Conference on Business and Management of Technology, 31st July, remote, 87–94.
Merz, J. 1991. Microsimulation – A Survey of Principles, Developments and Applications. International Journal of Forecasting
7(1):77–104.
Nie, W., H. Li, N. Xiao, H. Yang, Z. Jiang, and N. Buhigiro. 2021. Modeling and Solving the Last-shift Period Train Scheduling
Problem in Subway Networks. Physica A: Statistical Mechanics and its Applications 569:125775.
Owais, M., A.S. Ahmed, G.S. Moussa, and A.A. Khalil. 2021. Design Scheme of Multiple-subway Lines for Minimizing Passen-
gers Transfers in Mega-cities Transit Networks. International Journal of Rail Transportation, 9(6), 540–563.
Shi, X., C. Rong, H. Cheng, L.Cui, B. Wang, and S. Sun. 2020. Analysis on Deformation and Stress Characteristics of a Multibraced
Pit-in-Pit Excavation in a Subway Transfer Station. Advances in Civil Engineering 2020:e8844461.
Wang, X., D. Ni, J. Qu, and C. Zhang. 2021. Evaluation of Subway Passengers Transfer Hub Congestion Based on Queuing Model
and TOPSIS Method. Journal of Computational Methods in Sciences and Engineering 21(3):643–664.
Xu, Q., B. Mao, M. Li, and X. Feng. 2014. Simulation of Passenger Flows on Urban Rail Transit Platform Based on Adaptive
Agents. Journal of Transportation Systems Engineering and Information Technology 14(1):28–33.
Yang, X., H. Dong, and X. Yao. 2017. Passenger Distribution Modelling at the Subway Platform Based on Ant Colony
Optimization Algorithm. Simulation Modelling Practice and Theory 77:228–244.
Yap, M., D. Luo, O. Cats, N. van Oort, and S. Hoogendoorn. 2019. Where Shall We Sync? Clustering Passenger Flows to Identify
Urban Public Transport Hubs and Their Key Synchronization Priorities. Transportation Research Part C: Emerging
Technologies 98:433–448.
Zhang, B., W.K.V. Chan, and S.V. Ukkusuri. 2014. On the Modelling of Transportation Evacuation: An Agent-based Discrete-
event Hybrid-space Approach. Journal of Simulation 8(4):259–270.
Zhang, L., M. Li, and Y. Wang. 2022. Research on Design Optimization of Subway Station Transfer Entrance Based on AnyLogic.
Procedia Computer Science 208:310–318.
1408

Zhen, Liu, Chen, and Cui
AUTHOR BIOGRAPHIES
DONGYANG ZHEN is a Ph.D. student at the University of Maryland, College Park, majoring in Civil Engineering. His research
interests include transportation engineering, operation research, and computer science. His email is dyzhen@umd.edu.
ZHUOXUAN LIU is a Ph.D. student in the China Academy of Public Finance and Public Policy at the Central University of
Finance and Economics in Beijing, China. His research interests include quantitative economics, causal inference, and data analysis
and modeling. His email address is liuzhuoxuan@email.cufe.edu.cn.
YONGHAO CHEN is a graduate researcher at Columbia University, majoring in Civil Engineering. His research focuses on smart
transportation, agent-based simulation, and construction management. His email is yc4141@columbia.edu.
QINGBIN CUI is a Professor in the Department of Civil and Environmental Engineering at the University of Maryland, College
Park. His research focuses on construction management, infrastructure resilience, and sustainable engineering. He has published
extensively and contributes to academic discourse on project delivery and risk management. His email is cui@umd.edu and his
profile can be found at https://cee.umd.edu/clark/faculty/255/Qingbin-Cui.
1409