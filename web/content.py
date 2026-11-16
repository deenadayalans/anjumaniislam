"""Single source of truth for all site content (real data from anjumaniislam.org + school prospectus)."""

SCHOOL = dict(
    name="Anjuman-I-Islam Public School & Jr. College",
    short="Anjuman-I-Islam Panchgani",
    place="Panchgani, Maharashtra",
    phones=["8275204302", "8275205404"],
    email_admissions="info@anjumanislampublicschoolpanchgani.in",
    emails=[
        ("Admissions", "info@anjumanislampublicschoolpanchgani.in"),
        ("Principal", "principal@anjumanislampublicschoolpanchgani.in"),
        ("Executive Chairman", "chairmain@anjumanislampublicschoolpanchgani.in"),
        ("Accounts", "accounts@anjumanislampublicschool.in"),
        ("Careers", "careers@anjumanislampublicschoolpanchgani.in"),
    ],
    parent_url="https://anjumaniislam.org",
    parent_email="info@anjumaniislam.org",
)

QUOTE = "Step into a world where education meets compassion, and learning goes beyond the books. A place where lifelong friendship begins and the future is bright."

STATS = [  # label, value, suffix
    ("Years of education", 100, "+"),
    ("Acres of campus", 174, ""),
    ("Competitive exam tracks", 5, ""),
    ("Seats in the dining hall", 300, ""),
]

NETWORK_STATS = [
    ("Learners reached every year", 100000, "+"),
    ("People receive health care each year", 50000, "+"),
    ("Orphans enriched each year", 400, "+"),
    ("Students get financial assistance", 15000, "+"),
]
EDU_STATS = [
    ("Learners in education institutes", 96000, "+"),
    ("Trained teaching and non-teaching staff", 3200, "+"),
    ("Education institutes run by Anjuman", 90, "+"),
]

VISION = "To enrich lives and develop model citizens through inclusive, globally competitive, quality education."
MISSION = "To create and nurture educational and social institutions with special focus on women and marginalized sections of society."
SCHOOL_VALUES = "To cultivate a dynamic learning community within our boarding school where every student is empowered to explore, discover and excel — fostering academic excellence, character development and global citizenship."
SCHOOL_MISSION = "A transformative education beyond the classroom: a holistic environment that nurtures intellectual curiosity, creativity and personal growth, preparing students for success in higher education and beyond."

GOALS = [
    ("I", "Adequate infrastructure for all institutions", "by December 2027"),
    ("II", "Residential facility and new institutions — Schools, Health Care, Technical & Hospitality Management", "by December 2030"),
    ("III", "Build and enhance STEAM-based pedagogy in each institution", "by December 2027"),
    ("IV", "Obtain relevant accreditation for each institution", "by December 2027"),
    ("V", "Establish a Professional Development Centre (PDC)", "by December 2025"),
    ("VI", "Build capacity and competency of all professionals through a Performance Management System, including a Leadership Development Programme for all heads of institutions and CXO personnel", "ongoing"),
]

HISTORY = [  # year, text
    ("1874", "Anjuman-I-Islam is founded in Mumbai by a small group of Muslims with a “desire to see the Musalmans rise higher in the moral, social and educational scale.”"),
    ("1880", "Presents a Memorandum to the Indian Education Commission urging vocational, industrial, commercial and agricultural education, physical education and education for girls."),
    ("1936", "Starts the first technical school for artisans — the seed of today’s technical hub at the M.H. Saboo Siddik campus."),
    ("1939", "Opens its first school for girls, which grows into the Saboo Baug girls’ education campus."),
    ("1946", "Incorporated on 20 November as a not-for-profit company; also registered under the Maharashtra Public Trusts Act, 1950."),
    ("2020", "The Panchgani school completes 100 years of imparting education — the Centenary celebration."),
    ("2024", "Dr. Zahir Kazi, President since 2009, receives the Padma award. Robotics, Agriculture and Basic Aviation are added at Panchgani."),
]

PIONEER_NOTE = "Pioneering firsts: kindergarten, mid-day meals for students and subsidised fees for the needy."

# name, tenure, philanthropist-star
PRESIDENTS = [
    ("Mr. Cumruddin Tyabji", "1875 – 1889", False),
    ("Mr. Nakhoda Mohd. Ali Roghay II", "1889 – 1890", True),
    ("Hon. Mr. Justice Badruddin Tyabji", "1890 – 1907", False),
    ("Sir Currimbhoy Ebrahim", "1907 – 1912", False),
    ("Haji Yusuf Haji Ismail Sobani", "1912 – 1917", True),
    ("Hon. Mr. Justice A. M. Kajiji", "1917 – 1932", False),
    ("Hon. Mr. Justice Faiz B. Tyabji", "1932 – 1934 & 1935", False),
    ("Hon. Sardar Sir Suleman Cassum Mitha", "1934 – 1935", False),
    ("Mr. Hussain B. Tyabji", "Jan – Mar 1935", False),
    ("Mr. Osman Sobani", "1935 – 1938", False),
    ("Mr. Mohd. Haji Ahmed", "1938 – 1941 & 1949 – 1954", False),
    ("Mr. A. E. Maskati", "1941 – 1944", False),
    ("Mr. Hadi C. Tyabji", "1944 – 1947", False),
    ("Mr. Saif F. B. Tyabji", "1947 – 1949 & 1954 – 1957", False),
    ("Mr. Akbar A. Peerbhoy", "1957 – 1974", True),
    ("Mr. A. K. Hafizka", "1974 – 1975", False),
    ("Mr. A. R. Antulay", "1975 – 1976", False),
    ("Mr. Moinuddin Harris", "1977 – 1983", True),
    ("Dr. M. Ishaq Jamkhanawala", "1983 – 2006", False),
    ("Mr. Sami Khatib", "2006 – 2009", False),
    ("Dr. Zahir I Kazi", "2009 – till date", False),
]

BOARD = ["Dr. Zahir Kazi", "Mushtaq Antulay", "Dr. Abdullah Shaikh", "Moiz Miyajiwala", "Shakil Shaikh", "Aqeel Hafiz", "Shoaib Jamkhanawala", "Shohab Rais"]

ZAHIR_BIO = ("Dr. Zahir Kazi is a distinguished educationist and recipient of the Padma award, one of India’s highest civilian honours. "
             "Born in Ponda, Goa, he has served as President of Anjuman-I-Islam since 2009. Under his leadership Anjuman runs around 97 schools, colleges, hostels, "
             "orphanages and institutions across Maharashtra, serving over one lakh students, primarily from minority communities. "
             "Though a successful radiologist, he reduced his medical practice to devote more time to philanthropic work.")

OBJECTS = [
    "Promote the educational, social, economic and general welfare of Muslims by all lawful means",
    "Execute trusts and act as mutwalli (guardian) of waqfs recognised as valid in Muslim law",
    "Acquire, construct and maintain buildings and property needed for its purposes",
    "Accept gifts, donations and subscriptions in support of its objects",
    "Publish newspapers, periodicals, books and leaflets that promote its objects",
    "Establish and support associations and institutions that share its objects",
]

# Panchgani school units from the Anjuman institutions list
PANCHGANI_UNITS = [("Primary", "English", "Un-aided"), ("High School", "English", "Aided"), ("Jr. College", "English", "Un-aided")]

INSTITUTIONS = {
    "Schooling": [
        ("Bandra", "Urdu", "Dr. M. I. Jamkhanawala Urdu Girls High School", "Aided"),
        ("Bandra", "English", "Dr. M. I. Jamkhanawala Girls Jr. College", "Aided / Un-aided"),
        ("Bellasis Road", "English", "Begum Sharifa Kalsekar Girls English Primary School", "Un-aided"),
        ("Bellasis Road", "Urdu", "Saif Tyabji Girls Urdu Primary School", "Aided"),
        ("Bellasis Road", "English", "Begum Sharifa Kalsekar Girls English High School", "Un-aided"),
        ("Bellasis Road", "Urdu", "Saif Tyabji Girls Urdu High School", "Aided"),
        ("Bellasis Road", "English", "Saif Tyabji Girls Jr. College of Arts & Science", "Aided"),
        ("CSMT", "English", "Allana English Primary School", "Un-aided"),
        ("CSMT", "English", "Allana English High School", "Un-aided"),
        ("CSMT", "Urdu", "Anjuman-I-Islam Urdu High School", "Aided"),
        ("CSMT", "English", "Allana Jr. College of Science & Commerce", "Un-aided"),
        ("Kurla", "English", "Allana English Primary School", "Un-aided"),
        ("Kurla", "Urdu", "Allana Urdu Primary School", "Aided"),
        ("Kurla", "English", "Allana English High School", "Un-aided"),
        ("Kurla", "Urdu", "Allana Urdu Girls High School", "Aided"),
        ("Kurla", "Urdu", "Allana Urdu Boys High School", "Aided"),
        ("Kurla", "English", "Allana Junior College of Science & Commerce", "Un-aided"),
        ("Mahim", "Urdu", "Khalifa Ziauddin Girls Urdu Primary School", "Aided"),
        ("Maulana Shaukat", "Urdu", "Abdus Sattar Shuaib Urdu Primary School", "Aided"),
        ("Maulana Shaukat", "Urdu", "Abdus Sattar Shuaib Urdu High School", "Aided"),
        ("Maulana Shaukat", "Urdu", "Jan Mohd. Cassum High School – Day", "Aided"),
        ("Maulana Shaukat", "Urdu", "Jan Mohd. Cassum High School – Night", "Aided"),
        ("Maulana Shaukat", "English", "Akbar Peerbhoy Jr. College of Commerce & Economics", "Aided"),
        ("Nagpada", "Urdu", "Ahmed Sailor Urdu Primary School", "Aided"),
        ("Nagpada", "Urdu", "Ahmed Sailor Urdu High School", "Aided"),
        ("Panchgani", "English", "Anjuman-I-Islam Public School – Primary", "Un-aided"),
        ("Panchgani", "English", "Anjuman-I-Islam Public School – High School", "Aided"),
        ("Panchgani", "English", "Anjuman-I-Islam Public School – Jr. College", "Un-aided"),
        ("Pune", "English", "Ahmed Peermohamed English Primary School", "Un-aided"),
        ("Pune", "Urdu", "Valimohamed & Dostmohamed Peermohamed Urdu Primary School", "Aided"),
        ("Pune", "English", "Ahmed Peermohamed English High School", "Un-aided"),
        ("Pune", "Urdu", "Valimohamed & Dostmohamed Peermohamed Urdu High School", "Aided"),
        ("Pune", "English", "Peer Mohamed High School & Junior College for Girls", "Un-aided"),
        ("Turbhe", "Urdu", "Zubeida Talib Urdu Primary School", "Aided"),
        ("Turbhe", "Urdu", "Mustafa Fakih Urdu High School", "Aided"),
        ("Turbhe", "English", "Mustafa Fakih Junior College", "Un-aided"),
        ("Vashi", "English", "Abdul Azim Khatkhatay English Primary School", "Un-aided"),
        ("Vashi", "English", "Abdul Azim Khatkhatay English Secondary School", "Un-aided"),
        ("Versova", "English", "Anjuman-I-Islam English Primary School", "Un-aided"),
        ("Versova", "Urdu", "Fazilabai Abdul Sattar Oomer Urdu Primary School", "Aided"),
        ("Versova", "English", "Anjuman-I-Islam English High School", "Un-aided"),
        ("Versova", "Urdu", "Begum Jamila Haji Abdul Haq Urdu High School for Girls", "Aided"),
        ("Versova", "English", "Begum Jamila Haji Abdul Haq Jr. College of Home Science", "Un-aided"),
    ],
    "Tertiary": [
        ("CSMT", "English", "Begum Jamila Haji Abdul Haq Degree College of Home Science", "Un-aided"),
        ("CSMT", "English", "Anjuman-I-Islam College of Hospitality Management Studies", "Un-aided"),
        ("CSMT", "English", "Anjuman-I-Islam College of Hotel & Tourism Management Studies & Research", "Un-aided"),
        ("CSMT", "English", "Anjuman-I-Islam Institute of Hospitality Management", "Un-aided"),
        ("Maulana Shaukat", "English", "Akbar Peerbhoy Degree College of Commerce & Economics", "Un-aided"),
        ("Maulana Shaukat", "English", "Akbar Peerbhoy Professional College of Commerce & Economics", "Un-aided"),
    ],
    "Technical & Professional": [
        ("CSMT", "English", "Allana Institute of Management Studies", "Un-aided"),
        ("CSMT", "English", "Barrister A. R. Antulay College of Law", "Un-aided"),
        ("Panvel", "English", "AIKTC – School of Architecture", "Un-aided"),
        ("Panvel", "English", "AIKTC – School of Engineering & Technology", "Un-aided"),
        ("Panvel", "English", "AIKTC – School of Pharmacy", "Un-aided"),
        ("Saboo Siddik", "English", "MHSS College of Engineering", "Un-aided"),
    ],
    "Skill & Vocational": [
        ("CSMT", "English", "Akbar Peerbhoy Girls Polytechnic", "Un-aided"),
        ("Mahim", "Urdu", "Mohinuddin Harris Jr. College of Education (D.Ed)", "Un-aided"),
        ("Panvel", "English", "Abdul Razzak Kalsekar Polytechnic", "Un-aided"),
        ("Pune", "English", "Anjuman-I-Islam Polytechnic for Girls", "Un-aided"),
        ("Saboo Siddik", "English", "MHSS Polytechnic", "Aided / Un-aided"),
        ("Saboo Siddik", "English", "MHSS Industrial Training Institute", "Un-aided"),
        ("Saboo Siddik", "English", "MHSS Technical High School", "Un-aided"),
        ("Saboo Siddik", "English", "MHSS Vocational Junior College", "Aided / Un-aided"),
        ("Vashi", "English", "Akbar Peerbhoy College of Education", "Un-aided"),
    ],
    "Healthcare": [
        ("Versova", "Urdu", "Dr. M. Ishaq Jamkhanawala Tibbia Unani Medical College", "Un-aided"),
    ],
}

NEWS = [
    ("6 Nov 2026", "Champions of Harris Shield 2026 — a hat-trick of victories", "Sport", "https://anjumaniislam.org/anjuman-i-islam-champions-of-harris-shield-2026-hat-trick-of-victories-a-legacy-of-excellence-6th-november-2026/", "harris-shield.jpg"),
    ("29 Sep 2026", "Anjuman-I-Islam in collaboration with the Government of Maharashtra", "Partnership", "https://anjumaniislam.org/resources-and-media/", None),
    ("11 Aug 2026", "From student to professional: the journey of alumna Humaeyra Rashid Alam Khan", "Alumni story", "https://anjumaniislam.org/from-student-to-professional-inspiring-journey-of-anjuman-i-islam-alumna-humaeyra-rashid-alam-khan/", None),
    ("31 Jul 2026", "Mumbai University topper — a testament to excellence", "Achievers", "https://anjumaniislam.org/mumbai-university-topper-a-testament-to-excellence/", None),
    ("9 Jul 2026", "From learning to leadership: Anjuman’s Urdu-medium education", "Education", "https://anjumaniislam.org/from-learning-to-leadership-discover-anjuman-i-islams-urdu-medium-education/", None),
]

# Network-wide published results (anjumaniislam.org, 2026)
SSC_2026 = dict(appeared=2153, passed=2136, distinction=473, first_class=793)
HSC_2026 = dict(appeared=2002, passed=1697, distinction=72, overall=84.77, streams=[
    ("Science", 803, 776, 30, 96.64), ("Commerce", 1040, 785, 31, 75.48), ("Arts", 159, 136, 11, 85.53)])

EXAMS = [
    ("JEE", "Joint Entrance Examination", "Engineering"),
    ("NEET", "National Eligibility cum Entrance Test", "Medical"),
    ("CET", "Common Entrance Test", "State entrance"),
    ("NATA", "National Aptitude Test in Architecture", "Architecture"),
    ("CA", "Chartered Accountancy", "Commerce & finance"),
]
YEARS = ["2025–26", "2024–25", "2023–24"]

ACHIEVEMENTS = [
    ("2020", "Centenary celebration", "Completion of 100 successful years of imparting education, producing leaders across the globe.", "Institution"),
    ("2020", "World Stick Fight Championship, Goa", "3 Gold, 4 Silver and 3 Bronze medals.", "Sport"),
    ("2019", "World Thai Boxing Championship, Goa", "Gold medal.", "Sport"),
    ("2019", "INSPIRE Award — Taluka Level", "‘Innovation in Science Pursuit for Inspired Research’.", "Science"),
    ("2018–19", "Golden School Award", "Awarded by Indian Talent Search.", "Award"),
    ("—", "District-level cycling competition", "First Prize.", "Sport"),
    ("SSC", "Hindi Rashtrabhasha Puraskar", "Miss Shamsheera Nadaf (Std X) secured 95% in Hindi in the SSC exam.", "Academic"),
]

PROGRAMMES = [
    ("Primary", "Foundations in reading, numeracy, values and curiosity — quizzes, spell bee and early activities."),
    ("High School · SSC", "Unit tests, half-yearly and preliminary exams, practicals and Std X board preparation."),
    ("Jr. College · HSC", "HSC preparation with practicals, Prelim II and integrated entrance coaching."),
]

ACADEMIC_APPROACH = [
    ("Personal advising", "Academic advisors meet students regularly to set goals, track progress and offer guidance."),
    ("Peer tutors & resident advisors", "Dormitory study sessions supported by peer tutors and resident advisors."),
    ("Data-driven monitoring", "Administrators use data and feedback to identify areas for improvement and apply targeted interventions."),
    ("Innovative teaching", "Hands-on activities, discussion and varied methods to suit diverse learning styles."),
]

FACILITIES = [
    ("Robotics & AI tinkering lab", "chip", "A hub of innovation where students unlock the secrets of robotics and artificial intelligence."),
    ("Science labs", "flask", "Specialised equipment, with goggles, lab coats and emergency equipment ready and strict safety training."),
    ("Computer lab", "globe", "A digitised computer lab — a gateway to the future for the next generation of tech leaders."),
    ("Digital classrooms", "play", "A projector and AV set-up in every class, with a pre-designed library of e-materials for teachers."),
    ("Library", "book", "A vast collection of books and digital resources in the vintage academic block."),
    ("Performing arts centre", "music", "Music rooms where budding musicians, actors and artists hone their craft."),
]

BOARDING = [
    ("Dormitories", "bed", "dorm", "Fully renovated; a delicate balance between home and school so your child feels safe, happy and welcome."),
    ("Dining hall", "fork", "dining", "Renovated hall for 300 diners; five meals a day with menus designed by a dietician."),
    ("Prayer hall", "dome", "prayer", "Call to prayer five times a day; basic Islamic education and Quran recitation are emphasised."),
    ("Sick bay", "cross", "lab", "A trained nurse on campus 24/7, regular doctor visits and in-house care."),
    ("Akbar Peerbhoy Sports Stadium", "ball", "field", "The largest sports ground in town, with separate grounds for football, kabaddi, volleyball and basketball."),
    ("Green campus", "leaf", "garden", "Rainwater harvesting and organic gardens across 174 acres of flora and fauna."),
]

ACTIVITIES = [  # title, category, icon, text
    ("Robotics & AI", "innov", "chip", "Tinkering lab — introduced in 2024."),
    ("Basic Aviation", "innov", "plane", "A new 2024 course."),
    ("Agriculture & gardening", "outdoor", "leaf", "Organic gardens and hands-on farming."),
    ("Horse riding", "outdoor", "star", "On-campus riding."),
    ("Archery & shooting", "outdoor", "target", "Archery range and shooting range."),
    ("Sky gazing", "outdoor", "sun", "Clear hill-station skies."),
    ("Team sports", "sport", "ball", "Cricket, football, hockey, volleyball, basketball, kabaddi, athletics."),
    ("Fitness", "sport", "trophy", "PT, gymnastics, yoga, open gym and a skating rink."),
    ("Pottery & ceramics", "arts", "palette", "Studio work with clay."),
    ("Music & choir", "arts", "music", "Music rooms and an annual musical choir."),
    ("Drama & storytelling", "arts", "mic", "Inter-house dramatics and storytelling."),
    ("Knitting & sewing", "arts", "heart", "Craft and creative expression."),
    ("Debate & JAM", "minds", "mic", "Inter-house debate and Just-a-Minute."),
    ("Quiz & spell bee", "minds", "book", "Primary, Islamic and general quizzes."),
    ("Community service", "minds", "users", "Service opportunities and World NGO Day."),
    ("Hifz course", "minds", "dome", "Available on demand."),
]

DAY = [
    ("Rise & pray", "Prayer hall, Quran recitation and breakfast."),
    ("Classes", "Digital classrooms, labs and practicals."),
    ("Lunch & rest", "Dietician-planned meals in the dining hall."),
    ("Games & clubs", "Sports, arts, robotics, riding, archery."),
    ("Study & wind down", "Peer tutors and the dorm in-charge."),
]

JOURNEY = [
    ("Arrive & settle", "Orientation for new students, a welcome assembly and the dorm in-charge as the first point of contact."),
    ("Build foundations", "Study habits, reading and core subjects, with peer tutors, advisors and regular unit tests."),
    ("Explore passions", "Robotics, riding, archery, debate, pottery and sport — inter-house contests let every child shine."),
    ("Rise to the board year", "Preliminary exams, practicals and one-to-one goal setting for Std X and XII."),
    ("Launch", "NEET, JEE, CET, NATA and CA guidance, the Annual Day prize distribution and a farewell."),
]

COACHING_NOTE = "Competitive courses attract extra fees. Extra coaching is also provided for vernacular-medium students who need additional help."

UNIQUE = ["NEET", "JEE", "CET", "NATA", "CA", "Basic Aviation", "Agriculture", "AI & Robotics", "Horse riding", "Hifz course (on demand)", "Skating rink", "Gardening", "Shooting range", "Digital classroom", "Open gym", "Sky gazing"]

STEPS = [("Parents’ interview", ""), ("Child’s interview", ""), ("Written exam", ""), ("Medical history", ""), ("Blood investigation", "Std 8 onwards")]
IMPORTANT = [
    "Admission is subject to performance in the written exam.",
    "Students with an addiction history will not be admitted.",
    "An undertaking / indemnity on a ₹500 bond is mandatory.",
    "Over-age students will not be enrolled.",
    "Strict disciplinary action is taken against those who break the rules.",
]
FEES = [
    "Fees are collected in two terms.",
    "The first instalment is paid once admission is confirmed.",
    "The second instalment is paid in the second semester, after the Diwali holiday.",
    "For the balance, parents submit a post-dated cheque along with a promissory note.",
    "Competitive coaching courses attract extra fees.",
]
FAQ = [
    ("Which levels does the Panchgani campus offer?", "Primary, High School (SSC) and Jr. College (HSC), all English-medium."),
    ("Is coaching for NEET, JEE, CET, NATA and CA included?", "Coaching is offered on campus. Competitive courses attract extra fees."),
    ("What is the admission process?", "Parents’ interview, child’s interview, written exam, medical history and — from Std 8 — a blood investigation."),
    ("How are fees paid?", "In two terms: after admission is confirmed and after the Diwali holiday. A post-dated cheque and promissory note secure the balance."),
    ("What medical care is available?", "A trained nurse is on campus 24/7, a doctor visits for check-ups and the sick bay can keep patients in-house."),
    ("Is prayer compulsory?", "The call to prayer is given five times a day and Muslim students are expected to offer salah. Basic Islamic education and Quran recitation are emphasised."),
    ("Are there supports for students who struggle?", "Yes — peer tutors, resident advisors, academic advisors and extra coaching for vernacular-medium students."),
]

# Calendar: month, [(day, title, type)]   types: a admin, f festival, c competition, e exam, h holiday
CAL_TYPES = {"a": "Academic & admin", "f": "Celebrations", "c": "Competitions", "e": "Exams", "h": "Holidays & breaks"}
CALENDAR = [
    ("May", [("15", "Teachers’ report and meeting", "a"), ("16", "Dorm in-charge report", "a"), ("18", "Students’ report", "a"), ("20", "Academic session begins", "a")]),
    ("June", [("1", "Welcome assembly", "f"), ("5", "World Environment Day", "f"), ("15", "Spell Bee competition", "c"), ("17", "Bakri Eid holiday (3 days)", "h"), ("21", "International Yoga Day", "f"), ("29", "Indoor games competition", "c")]),
    ("July", [("1", "Orientation for new students", "a"), ("13", "Art competition", "c"), ("16", "Islamic quiz competition", "c"), ("18", "Indoor games finals", "c"), ("20", "First unit test begins", "e")]),
    ("August", [("10", "Musical choir", "f"), ("10", "Monsoon break", "h"), ("15", "Independence Day", "f"), ("26", "Classes resume", "a")]),
    ("September", [("5", "Teachers’ Day celebration", "f"), ("9", "Inter-house JAM competition", "c"), ("14", "National Hindi Divas", "f"), ("16", "Eid-e-Milad celebration", "f"), ("17", "Anant Chaturthi (holiday)", "h"), ("21", "Inter-house dramatics", "c"), ("28", "Inter-house football", "c")]),
    ("October", [("1", "Inter-house badminton", "c"), ("2", "Gandhi Jayanti (holiday)", "h"), ("7", "Half-yearly exam", "e"), ("15", "Inter-house cross country", "c"), ("28", "Annual Sports Day", "c"), ("28", "Students leave for Diwali break", "h")]),
    ("November", [("17", "Students report back", "a"), ("30", "Inter-house debate competition", "c")]),
    ("December", [("1–5", "Educational excursion", "f"), ("7", "Prelim 1 for Std X begins", "e"), ("14", "Storytelling competition", "c"), ("16", "Second unit test", "e"), ("31", "Anjuman Talent Show", "f")]),
    ("January", [("1", "Prelim II for Std X and XII", "e"), ("14", "Kite Flying Festival", "f"), ("18", "Quiz competition", "c")]),
    ("February", [("10", "HSC practicals", "e"), ("15", "SSC practicals", "e"), ("19", "Shiv Jayanti (holiday)", "h"), ("27", "World NGO Day", "f")]),
    ("March", [("1", "Annual Day and prize distribution", "f"), ("3", "Final exams", "e"), ("8", "Mahashivratri (holiday)", "h"), ("20", "Boarders depart", "a")]),
]
CAL_NOTE = "Dates shown follow the 2024–25 school calendar and are tentative; parents should book tickets only after confirmation from the school office."

MARQUEE_INSTITUTIONS = ["Allana", "Akbar Peerbhoy", "Saif Tyabji", "MHSS Saboo Siddik", "AIKTC Panvel", "Jamkhanawala", "Mustafa Fakih", "Peermohamed Pune", "Khatkhatay Vashi", "Kalsekar", "Panchgani"]


# ---- A day at Panchgani (indicative timetable; hours are 24h, sleep runs past midnight to 05:00) ----
DAYPLAN = [
    dict(id="wake", s=5, e=8, w=1.2, kicker="Rise & shine", title="Wake up to a fresh day",
         text="The hills are cool and quiet. Dormitories stir, the call to prayer rings out and the whole house starts the day together.",
         points=["Wake-up and morning prayer in the prayer hall", "Group yoga and stretching on the lawns", "Freshen up, tidy the dorm and a wholesome breakfast"],
         icon="sun", scene="garden"),
    dict(id="school", s=8, e=16, kicker="School hours", title="A full day of learning", text="", points=[], icon="book", scene="books",
         subs=[
             dict(s=8, e=11, w=.9, label="Morning classes", text="Digital classrooms with a projector and AV set-up, teachers who love their subjects, labs and a library of e-materials."),
             dict(s=11, e=11.25, w=.4, label="Healthy snack break", text="Fifteen minutes to refuel with something light from the dietician-designed menu — and catch up with friends."),
             dict(s=11.25, e=13, w=.6, label="Classes continue", text="Lessons resume — discussion, hands-on activities, practicals and academic advisors checking progress."),
             dict(s=13, e=14, w=.55, label="Lunch", text="The renovated dining hall seats 300. Hygiene is paramount and meals are supervised for balance and nutrition."),
             dict(s=14, e=16, w=.65, label="School continues", text="Afternoon lessons, labs and coaching — including the NEET, JEE, CET, NATA and CA tracks."),
         ]),
    dict(id="play", s=16, e=19, w=1.2, kicker="Play", title="Play, practise, explore",
         text="The golden hours belong to the outdoors: the largest sports ground in town, an archery range, horses, a skating rink and clubs for every passion.",
         points=["Cricket, football, hockey, volleyball, basketball, kabaddi, athletics", "Archery, horse riding, skating, shooting range, gardening", "Robotics, pottery, music, drama and debate clubs"],
         icon="ball", scene="field"),
    dict(id="dinner", s=19, e=20, w=.7, kicker="Dinner", title="Dinner together",
         text="The day’s last meal — warm food, stories from the day and a settled, family feeling.",
         points=["Dinner in the dining hall", "Evening prayer and a quiet moment"], icon="fork", scene="dining"),
    dict(id="study", s=20, e=22, w=1.0, kicker="Study time", title="Study, homework & wind-down",
         text="Supervised study sessions in the dormitories, supported by peer tutors and resident advisors.",
         points=["Homework and revision with peer tutors", "Resident advisors and dorm in-charge on hand", "Reading, reflection and getting ready for bed"],
         icon="book", scene="books"),
    dict(id="sleep", s=22, e=29, w=1.2, kicker="Lights out", title="Rest — and tomorrow begins again",
         text="Quiet falls over the dormitories. The dorm in-charge is on duty and a trained nurse is on campus 24/7.",
         points=["Lights out and a good night’s sleep", "Dorm in-charge on duty; nurse on campus 24/7"], icon="moon", scene="dorm"),
]
# sky colour keyframes by hour (24h clock; 29 = 5 am next day): [hour, top, bottom]
DAYSKY = [
    [5, "#3a3a6a", "#e59a7a"], [6.5, "#fbd0a5", "#ef8a6c"], [8, "#9fd3f2", "#e6f5ff"], [12, "#8ccbf2", "#e4f4ff"],
    [14, "#a9d6f0", "#fff0cf"], [16, "#ffd8a0", "#f4ab66"], [17.5, "#f39c5a", "#8e5ea0"], [19, "#4b3b7c", "#1e2250"],
    [20.5, "#18233f", "#0b1226"], [22, "#070b18", "#0d1430"], [27, "#0a0f24", "#101a3a"], [29, "#3a3a6a", "#e59a7a"],
]
DAY_NOTE = "Indicative timetable — exact timings will be confirmed by the school."

MAP_QUERY = "Anjuman-I-Islam Public School & Junior College, Panchgani"

PLACE_FACTS = [
    ("174", "acres of campus", "A hill campus home to a huge variety of flora and fauna, with organic gardens and rainwater harvesting."),
    ("300", "seats in the dining hall", "Five meals a day with menus designed by a dietician — hygiene and cleanliness come first."),
    ("24/7", "nurse on campus", "A trained nurse on the campus around the clock, plus regular doctor visits."),
]
PLACE_INTRO = "Panchgani is a hill station in the Sahyadri range of Maharashtra. Our campus spreads across 174 acres of hill country — cool mornings, clear night skies and room to roam."

MAP_LL = "17.924394,73.765705"  # campus centre as reported by Google Maps
