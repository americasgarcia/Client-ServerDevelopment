One of the biggest things I focused on in this project was separating responsibilities. In Project One, I created a CRUD Python module (AnimalShelter class) to handle all database interactions. Then in Project Two, I reused that module to connect the dashboard widgets to the MongoDB database instead of writing database logic directly in the dashboard.
This made my code cleaner and easier to manage. If something needed to change in the database logic, I only had to update it in one place. It also made the dashboard code easier to read because it focused only on user interaction and filtering, not database details.
In the future, I could reuse this CRUD module in other applications that need to connect to the same database. It gave me a better understanding of how modular design makes systems easier to maintain and scale.

How I Approach Problems as a Computer Scientist:

For this project, I started by understanding what Grazioso Salvare needed the dashboard to do. Instead of jumping straight into coding, I thought through how the data needed to be filtered and how the widgets would interact with the database.
This felt different from earlier assignments because it wasn’t just about writing a program to get an output, it was about connecting multiple components into one working system. I had to think more about structure, data flow, and how changes in one area would affect another.
Moving forward, I would continue breaking client requirements into smaller pieces, designing the database carefully, and keeping database access modular so systems stay flexible.

What Computer Scientists Do and Why It Matters:

Computer scientists build systems that turn data into useful tools. In this project, I created a dashboard that allows users to quickly filter and view animal shelter data instead of manually sorting through records.
For a company like Grazioso Salvare, this kind of system improves efficiency and supports better decision-making. It shows how well-structured code and databases can directly impact how an organization operates.
This project helped me see how technical design choices affect real-world usability — not just whether the code runs, but whether it’s practical and helpful.
