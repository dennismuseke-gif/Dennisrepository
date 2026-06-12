# School Programmes Chatbot 🎓

A simple and interactive chatbot application that helps students explore and learn about various school programmes offered by the institution.

## Features

- **List All Programmes**: View all available school programmes at a glance
- **Search Programmes**: Search for specific programmes by name or keywords
- **View Details**: Get comprehensive information about each programme including:
  - Programme duration
  - Description
  - Key subjects
  - Career paths
- **Filter by Duration**: Find programmes by their study duration
- **User-Friendly Interface**: Interactive menu-driven interface

## Available Programmes

1. **Bachelor of Science in Computer Science** (4 years)
   - Subjects: Python, Java, Database Design, Machine Learning, Web Development
   - Careers: Software Developer, Data Scientist, System Administrator

2. **Bachelor of Science in Mathematics** (4 years)
   - Subjects: Calculus, Algebra, Statistics, Discrete Mathematics, Numerical Analysis
   - Careers: Mathematician, Data Analyst, Actuary, Engineer

3. **Bachelor of Arts in Business Administration** (4 years)
   - Subjects: Accounting, Marketing, Management, Finance, Business Strategy
   - Careers: Business Manager, Entrepreneur, Financial Analyst, Marketing Manager

4. **Bachelor of Science in Nursing** (4 years)
   - Subjects: Anatomy, Pharmacology, Patient Care, Medical Ethics, Clinical Practice
   - Careers: Registered Nurse, Clinical Specialist, Healthcare Administrator

5. **Bachelor of Engineering in Civil Engineering** (4 years)
   - Subjects: Structural Design, Materials Science, Project Management, CAD, Surveying
   - Careers: Civil Engineer, Project Manager, Structural Engineer, Construction Manager

6. **Bachelor of Arts in English Literature** (4 years)
   - Subjects: Literature Analysis, Creative Writing, Linguistics, Drama, Communication
   - Careers: Writer, Editor, Teacher, Journalist, Content Creator

## Installation

### Requirements
- Python 3.6 or higher
- No external dependencies required (uses only built-in libraries)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/dennismuseke-gif/Dennisrepository.git
cd Dennisrepository
```

2. Ensure you have Python installed:
```bash
python --version
```

## Usage

1. Run the chatbot:
```bash
python chatbot.py
```

2. Follow the on-screen menu:
   - Press `1` to see all programmes
   - Press `2` to search for a programme
   - Press `3` to get detailed information
   - Press `4` to filter by duration
   - Press `5` to exit

### Example Interactions

```
🎓 WELCOME TO SCHOOL PROGRAMMES CHATBOT 🎓

What would you like to do?
  1. List all programmes
  2. Search for a specific programme
  3. Get programme details
  4. Filter by duration
  5. Exit

Enter your choice (1-5): 2
Enter a keyword to search: Computer
```

## File Structure

```
Dennisrepository/
├── chatbot.py              # Main chatbot application
├── programmes_data.json    # School programmes database
└── README.md              # This file
```

## Data Format

Programmes are stored in JSON format with the following structure:

```json
{
  "id": 1,
  "name": "Programme Name",
  "duration": "4 years",
  "description": "Programme description",
  "subjects": ["Subject1", "Subject2", ...],
  "career_paths": ["Career1", "Career2", ...]
}
```

## How to Add More Programmes

1. Open `programmes_data.json`
2. Add a new programme object to the `school_programmes` array:

```json
{
  "id": 7,
  "name": "New Programme Name",
  "duration": "4 years",
  "description": "Programme description",
  "subjects": ["Subject1", "Subject2"],
  "career_paths": ["Career1", "Career2"]
}
```

3. Save and run the chatbot again

## Future Enhancements

- [ ] Add student reviews and ratings
- [ ] Integration with a database (SQLite, PostgreSQL)
- [ ] Web interface using Flask or Django
- [ ] Email notification system
- [ ] Programme comparison tool
- [ ] Admission requirements display
- [ ] Fee and scholarship information
- [ ] Application submission through chatbot

## Troubleshooting

**Issue**: `FileNotFoundError: programmes_data.json not found`
- **Solution**: Ensure both `chatbot.py` and `programmes_data.json` are in the same directory

**Issue**: Program crashes after selection
- **Solution**: Make sure you have Python 3.6+ installed

## License

This project is open source and available under the MIT License.

## Author

Created by Dennis Museke

## Support

For issues or suggestions, please open an issue on GitHub or contact the repository owner.

---

**Happy learning! 🎓📚**
