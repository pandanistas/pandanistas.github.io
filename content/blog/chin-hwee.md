title: Interview with Ong Chin Hwee
date: 2020-03-07
description: pandanistas is running a series of interviews where we interview contributors to the pandas library. Read our first interview featuring Ong Chin Hwee, one of the contributors to pandas' 1.0 release.
tags: interview

pandanistas is running a series of interviews where we interview contributors to the [pandas](https://github.com/pandas-dev/pandas/) library, especially those coming from underrepresented communities. We hope that this could encourage more people, especially from underrepresented communities, to make their first contributions to pandas.

For our first interview, we're super excited to be talking to Chin Hwee who had her contribution to pandas documentation included in the [pandas 1.0 release](https://pandas.pydata.org/pandas-docs/version/1.0.0/whatsnew/index.html). You can find out more about her through her [blog](https://ongchinhwee.me/) and [follow her on Twitter](https://twitter.com/ongchinhwee).

If you know someone that you think we should interview, or if you have a story that you would like to share, don't hesitate to [reach out to us](/pages/contact.html)! We would love to hear from you.

**Hi Chin Hwee! It’s nice to be able to get to know you! Can you tell us a little bit about yourself?**

I am a born-and-bred Singaporean Chinese who loves food, aviation and music, in no particular order. Before my current role as a Data Engineer, I majored in Aerospace Engineering with a minor in Business for my undergraduate degree at Nanyang Technological University on a scholarship, worked as a Research Assistant at Rolls-Royce@NTU Corporate Laboratory for around 2 years, and went on to pursue a Masters in Mechanical Engineering with specialization in Computation and Modeling at National University of Singapore. I graduated with Honors for my MBA from Quantic School of Business and Technology (formerly Smartly Institute) in November 2019, and I hope to make use of technology and business knowledge to contribute positively to the community.

I learnt C during my freshman year, realised I’m pretty decent at it, and subsequently picked up MATLAB, C++ and Python on my own. Currently, I write a lot more Python code for my work and personal projects, since Python is primarily used in the data community and requires less lines of code.

Outside of working hours, I attend local tech meetups and volunteer as a mentor with BigDataX, a data community in Singapore that aims to build literacy in data engineering through conducting hands-on workshops. Since August 2019, I have also started speaking at meetups and regional conferences - in fact, I am excited to be speaking at FOSSASIA Summit 2020, which will be held on 19 - 21 March 2020 at Lifelong Learning Institute in Singapore. 

**Can you tell us about your first contribution to pandas?**

My first contribution to pandas is improving the documentation for MultiIndex.set_levels to clarify that the `.set_levels()` function interprets passed values as new components of the `.levels` attribute and stores the passed values - even if the number of values passed for any of the levels is more than its existing length.

**What made you decide to contribute to pandas?**

I use pandas frequently in my data analytics projects, mainly for data manipulation, cleaning and analysis to extract insights from raw data. To help in my daily work, I refer to the pandas documentation to figure out which methods to use for data manipulation - be it filtering data tables with specified conditions or setting MultiIndex for multidimensional analysis. However, like most developers, I end up finding my answers on StackOverflow first instead of the documentation - reading the documentation became more of a hindsight. While I don’t feel entirely comfortable pulling answers from StackOverflow without understanding how the functions and internals work, we had to get work done.

After my first conference talk in August 2019, I was brainstorming on different ways to contribute back to the tech community that empowered me as a data engineer. One of my work projects requires multidimensional data analysis to track patterns within the data, and I was exploring the use of hierarchical indexing (MultiIndex) for that particular project. While I was looking through issues on Python libraries to find something to contribute, I came across an issue relating to the pandas documentation which was tagged with ‘MultiIndex’. I thought, why not take this opportunity to contribute to the library that supports the core part of my data analytics work while learning how MultiIndex actually works? It’s going to help me with my work, help fellow users with their work, and save a lot more future agony associated with not understanding how the function works.

**We guess something that a lot of to-be contributors can relate to is the fear that we may not know enough to make a first contribution. Did you have these thoughts? And if so, how did you overcome them?**

Thoughts of not knowing enough to make a first contribution? Yes, I did have them - I was trawling repositories on Github looking for issues that are not yet being worked on by other contributors. In fact, I was hovering around the pandas issue for a few days before I decided to turn on my “F*ck It” mentality and raise my hand (virtually) to ask if I could work on the issue. After all, I have nothing to lose from asking - contributors start out by making their first contributions to the project; they do not start out knowing everything about the codebase of the project.

**Which knowledge you think was necessary for making the contribution to pandas?**

Firstly, you do need to know how to work with version control, Git and GitHub, and best practices when working in a team - you're working in a team with many contributors who are working on loads of pull requests. That being said, there's a contributing guide that helps a lot when making the contribution. Git might not be the easiest thing to learn, but there are people who would be willing to help you out if you ask for it.

Another point I would like to highlight is that you do not need to understand every single operation or feature in pandas; knowing how to use some pandas operations is good enough knowledge to start contributing to pandas.

**What things did you learn while making your first contribution to pandas?
**
An important learning point I learnt while making my first contribution to pandas is that it is important to understand how the operation you're working on (be it code, documentation etc.) works behind the hood to perform the operation on the object, and why the operation is designed to follow certain behavior that changes the object properties. Implementing a sequence of pandas operations to transform and analyse the data might seem to be something we do as part of our data analytics work, but understanding the fundamental concepts behind the operations is more important when working on the contribution to pandas.

Let's take the `MultiIndex.set_levels()` operation for example. We use `set_levels()` to define the levels property of the `MultiIndex` (to be more specific, the level labels that identify a subgroup of the data), and all the values passed through `set_levels()` are stored in the `MultiIndex` levels even if not all the values are used. The levels property could be fairly easily confused with the names property in `MultiIndex` for typical pandas users, since we are "passing names to the levels" in a way. As we dig further into the definition for `MultiIndex` object properties, we learn that the names property in `MultiIndex` refers to the names for the levels themselves, not the (named) values of the levels - each level has a name and contains a list of values that can be used for indexing. 

Another important learning point is that contributing to the docs is one of the best ways to learn more about the project. You get started on a small segment of the codebase without breaking the code and add value to fellow users, which helps build up your confidence in contributing to the project. In addition, you are learning from the core contributors who do care a lot about the project and how the project is being used - what better way to learn more about the project than learning from the primary source?

**How did you feel after your contribution was merged?**

Pretty accomplished, I would say. Now I appreciate the docs more, knowing how much time and effort it took to improve the docs for a single function that I can't even find on StackOverflow.

Another thing to mention is that when I shared the news on my Facebook news feed, someone commented on how much precious time had been wasted on trying to figure out how to use the `set_levels()` operation - and how the improved docs would help save more time for other pandas users. It feels great knowing that my contribution to the pandas docs would help fellow pandas users like myself save time on trying to find answers through search engines after failing to find them on the docs.

**What’s the most exciting project that you’ve worked on using pandas?**

Exploring seasonal insights on Singapore weather station data using pandas! It's a personal project that I'm passionate about, since I'm pretty concerned about global warming and extreme weather conditions which make me feel really unwell at times.

I used the Requests library to extract 3 years of temperature and rainfall data from the Data.gov.sg APIs, converted the JSON to pandas DataFrames using a series of operations, and analysed the data trends and patterns to determine whether the weather is getting hotter and wetter than before. I first delivered a talk on my analysis at Open Up Summit 2019 at Taipei, and subsequently delivered a follow-up talk showing the full 3-year results at JuniorDevSG Code and Tell about 1.5 months later. The analysis results do indicate that year 2019 was indeed hotter than previous years on average, and our dry months are getting drier and wet months getting wetter, so we have to be prepared for more extreme weather in Singapore for the years ahead.

**Let’s talk more about your work! You’re currently working as a data engineer in Singapore. Can you elaborate more about what you do?**

I currently work as a data engineer within a data analytics team at a government-linked corporation in Singapore. I do a myriad of stuff that supports the data scientists in the data science process: data cleaning, data processing, data quality assessment, exploratory data analysis, solution deployment and delivery etc. Together with my fellow data engineer in the team, we support the chief architect in maintaining the operations of the on-premise development cloud which supports our data science workflows.

I have been working on projects relating to aircraft systems and business processes, both of which are areas that I have some domain knowledge due to my background in aerospace engineering and business. I am looking to explore further into projects relating to other engineering systems with larger datasets, in order to develop myself not just as a data engineer but also as an engineering researcher who has the domain expertise and data skills to come up with sustainable solutions that benefit the community (myself included).

**What’s the most enjoyable part of your work and what’s the most challenging part?**

The most challenging part of my work is dealing with bad quality or limited data. I can learn how to use tools and libraries by referring to documentation and online resources, but there is little we could do when a significant portion of the data is either missing or invalid and there is no clear way of handling such data. After all, a common adage among data professionals is "garbage in, garbage out". If there are no other mathematical or physical models that we could fall back on to generate the data, there is nothing much we could do except to work on the limited data that are usable.

It is also a challenge to explain to clients why we need certain types of data, and that comes with domain knowledge about the data analytics project. Having a sufficient domain-based understanding is needed to convince the client to work together with the project team to come up with an analytics plan that aims to alleviate their pain points. You don't need to know everything about the domain, because the client knows more than you about the domain and the domain knowledge is gained through years of work experience. However, you do need to read widely to gain a better understanding of the context of the project and to understand the potential benefits the project could bring to the client. It's about learning to have empathy for their pain points and working together to discover insights that they might not know without the help of advanced analytics, and that is the most enjoyable part of my work.

**Any advice for people who are looking forward to making their first contribution in pandas?**

Start with small fixes - even fixing typos in the docs are welcome improvements that contribute to the user experience of reading the docs. There are issues listed under "Docs" and "good first issue" which you can start out with - there are friendly maintainers in the project who would help label the issues to make identifying those "low-hanging fruits" easier for new contributors. Most importantly, when you start small and make small fixes that get merged into the project, you will slowly gain the confidence to work on more contributions in the future.

Contributing to the docs is one of the best ways to get started - that's how Marc Garcia ([@datapythonista](https://twitter.com/datapythonista)), a pandas core contributor, got started with contributing to pandas! Delving into the pandas codebase can seem quite daunting at first, but working on the docs for a subset of the codebase is very useful in enriching your understanding of the operations and getting familiarised with parts of the codebase.

Don't feel too discouraged about not getting things right the first time round when making your first contribution. The pandas core contributors are your best mentors - they know a lot about the project and will be happy to guide you along your first pull request. I made a few mistakes here and there for my first contribution and messed up my branch, but I got some help from the contributors and managed to get my first contribution merged into the master branch in the end.

**Thank you so much Chin Hwee for taking your time to chat with us!**