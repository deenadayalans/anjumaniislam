// Content data. Types: a=admin/academic, f=festival/observance, c=competition, e=exam, h=holiday
window.SCHOOL = {
  calendarLabel: 'Academic Year 2024–25 (sample from prospectus — to be updated)',
  types: { a: 'Academic & admin', f: 'Celebrations', c: 'Competitions', e: 'Exams', h: 'Holidays & breaks' },
  calendar: [
    ['May 2024', [['15', 'Teacher’s report and meeting', 'a'], ['15', 'Teachers’ training programme', 'a'], ['16', 'Dorm in-charge report', 'a'], ['18', 'Students’ report', 'a'], ['20', 'Academic session begins', 'a']]],
    ['June 2024', [['1', 'Welcome assembly', 'f'], ['5', 'World Environment Day', 'f'], ['15', 'Spell Bee competition', 'c'], ['17', 'Bakri Eid holiday (3 days)', 'h'], ['21', 'International Yoga Day', 'f'], ['29', 'Indoor games competition', 'c']]],
    ['July 2024', [['1', 'Orientation for new students', 'a'], ['13', 'Art competition', 'c'], ['16', 'Islamic quiz competition', 'c'], ['18', 'Indoor games finals', 'c'], ['20', 'First unit test begins', 'e']]],
    ['August 2024', [['10', 'Musical choir', 'f'], ['10', 'Monsoon break', 'h'], ['15', 'Independence Day', 'f'], ['23', 'Teachers’ report', 'a'], ['24', 'Students’ report', 'a'], ['26', 'Classes resume', 'a']]],
    ['September 2024', [['5', 'Teachers’ Day celebration', 'f'], ['9', 'National Literacy Day · Inter-house JAM competition', 'c'], ['14', 'National Hindi Divas', 'f'], ['16', 'Eid-e-Milad celebration · Primary quiz', 'f'], ['17', 'Anant Chaturthi (holiday)', 'h'], ['21', 'Inter-house dramatics', 'c'], ['28', 'Inter-house football competition', 'c']]],
    ['October 2024', [['1', 'Inter-house badminton', 'c'], ['2', 'Gandhi Jayanti (holiday)', 'h'], ['7', 'Half-yearly exam', 'e'], ['15', 'Inter-house cross country', 'c'], ['28', 'Annual Sports Day', 'c'], ['28', 'Students leave for Diwali break', 'h'], ['29', 'Staff leave for Diwali break', 'h']]],
    ['November 2024', [['16', 'Staff reporting', 'a'], ['17', 'Students report', 'a'], ['30', 'Inter-house debate competition', 'c']]],
    ['December 2024', [['1–5', 'Educational excursion', 'f'], ['7', 'Prelim 1 for Std X begins', 'e'], ['14', 'Storytelling competition', 'c'], ['16', 'Second unit test', 'e'], ['31', 'Anjuman Talent Show', 'f']]],
    ['January 2025', [['1', 'Prelim II for Std X and XII', 'e'], ['14', 'Kite Flying Festival', 'f'], ['18', 'Quiz competition', 'c']]],
    ['February 2025', [['4', 'World Cancer Day', 'f'], ['10', 'HSC practicals', 'e'], ['15', 'SSC practicals', 'e'], ['19', 'Shiv Jayanti (holiday)', 'h'], ['27', 'World NGO Day', 'f'], ['28', 'Ramadan begins', 'f']]],
    ['March 2025', [['1', 'Annual Day and prize distribution', 'f'], ['3', 'Final exams', 'e'], ['8', 'Mahashivratri (holiday)', 'h'], ['20', 'Boarders depart', 'a']]],
    ['May 2025', [['15', 'Teachers’ meeting and training programme', 'a'], ['16', 'Dorm in-charge meeting', 'a'], ['18', 'Students report', 'a'], ['20', 'Academic session begins', 'a']]]
  ],
  exams: [
    { id: 'jee', n: 'JEE', full: 'Joint Entrance Examination', desc: 'Engineering entrance coaching delivered on campus alongside the Jr. College timetable.', metric: 'Best rank / percentile' },
    { id: 'neet', n: 'NEET', full: 'National Eligibility cum Entrance Test', desc: 'Medical entrance coaching with regular mock tests and doubt sessions.', metric: 'Best rank / score' },
    { id: 'cet', n: 'CET', full: 'Common Entrance Test (state)', desc: 'State-level entrance preparation for engineering, pharmacy and more.', metric: 'Best percentile' },
    { id: 'nata', n: 'NATA', full: 'National Aptitude Test in Architecture', desc: 'Drawing and aptitude training for aspiring architects.', metric: 'Best score' },
    { id: 'ca', n: 'CA', full: 'Chartered Accountancy foundation', desc: 'Early guidance for students aiming at a career in accounting and finance.', metric: 'Foundation cleared' },
    { id: 'ssc', n: 'SSC', full: 'Std X board examination', desc: 'Board results for Std X, with preliminary exams and practicals.', metric: 'Highest percentage' },
    { id: 'hsc', n: 'HSC', full: 'Std XII board examination', desc: 'Board results for the Jr. College, with preliminary exams and practicals.', metric: 'Highest percentage' }
  ],
  years: ['2025–26', '2024–25', '2023–24']
};
