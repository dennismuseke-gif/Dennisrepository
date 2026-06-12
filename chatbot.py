"""
School Programmes Chatbot
A simple chatbot that helps students explore school programmes
"""

import json
import os
from datetime import datetime


class SchoolProgrammeChatbot:
    def __init__(self):
        self.programmes = self.load_programmes()
        self.conversation_history = []
        
    def load_programmes(self):
        """Load school programmes from JSON file"""
        try:
            with open('programmes_data.json', 'r') as f:
                data = json.load(f)
                return data['school_programmes']
        except FileNotFoundError:
            print("Error: programmes_data.json not found!")
            return []
    
    def display_welcome(self):
        """Display welcome message"""
        print("\n" + "="*60)
        print("🎓 WELCOME TO SCHOOL PROGRAMMES CHATBOT 🎓")
        print("="*60)
        print("\nHello! I'm here to help you explore our school programmes.")
        print("\nWhat would you like to do?")
        print("  1. List all programmes")
        print("  2. Search for a specific programme")
        print("  3. Get programme details")
        print("  4. Filter by duration")
        print("  5. Exit")
        print("-"*60)
    
    def list_all_programmes(self):
        """List all available programmes"""
        print("\n📚 AVAILABLE SCHOOL PROGRAMMES:\n")
        for prog in self.programmes:
            print(f"  {prog['id']}. {prog['name']}")
            print(f"     Duration: {prog['duration']}")
            print(f"     {prog['description'][:60]}...")
            print()
    
    def search_programme(self, keyword):
        """Search programmes by keyword"""
        keyword = keyword.lower()
        results = [p for p in self.programmes 
                   if keyword in p['name'].lower() or keyword in p['description'].lower()]
        
        if results:
            print(f"\n🔍 Search results for '{keyword}':\n")
            for prog in results:
                print(f"  • {prog['name']}")
                print(f"    {prog['description']}")
                print()
        else:
            print(f"\nSorry, no programmes found matching '{keyword}'")
    
    def get_programme_details(self, prog_id):
        """Get detailed information about a specific programme"""
        try:
            prog_id = int(prog_id)
            programme = next((p for p in self.programmes if p['id'] == prog_id), None)
            
            if programme:
                print("\n" + "="*60)
                print(f"📖 {programme['name'].upper()}")
                print("="*60)
                print(f"\nDescription: {programme['description']}")
                print(f"Duration: {programme['duration']}")
                print(f"\nKey Subjects:")
                for subject in programme['subjects']:
                    print(f"  ✓ {subject}")
                print(f"\nCareer Paths:")
                for career in programme['career_paths']:
                    print(f"  → {career}")
                print("\n" + "="*60)
            else:
                print(f"\nProgramme with ID {prog_id} not found.")
        except ValueError:
            print("\nPlease enter a valid programme number.")
    
    def filter_by_duration(self, duration):
        """Filter programmes by duration"""
        results = [p for p in self.programmes if duration.lower() in p['duration'].lower()]
        
        if results:
            print(f"\n⏱️  Programmes lasting {duration}:\n")
            for prog in results:
                print(f"  • {prog['name']}")
                print(f"    {prog['description'][:50]}...")
                print()
        else:
            print(f"\nNo programmes found with duration '{duration}'")
    
    def run(self):
        """Main chatbot loop"""
        self.display_welcome()
        
        while True:
            try:
                choice = input("\nEnter your choice (1-5): ").strip()
                
                if choice == '1':
                    self.list_all_programmes()
                
                elif choice == '2':
                    keyword = input("Enter a keyword to search: ").strip()
                    if keyword:
                        self.search_programme(keyword)
                    else:
                        print("Please enter a valid keyword.")
                
                elif choice == '3':
                    self.list_all_programmes()
                    prog_id = input("Enter the programme number for details: ").strip()
                    if prog_id:
                        self.get_programme_details(prog_id)
                    else:
                        print("Please enter a valid programme number.")
                
                elif choice == '4':
                    duration = input("Enter duration (e.g., '4 years'): ").strip()
                    if duration:
                        self.filter_by_duration(duration)
                    else:
                        print("Please enter a valid duration.")
                
                elif choice == '5':
                    print("\n👋 Thank you for using School Programmes Chatbot!")
                    print("Have a great day! 🎓\n")
                    break
                
                else:
                    print("Invalid choice. Please enter 1-5.")
            
            except KeyboardInterrupt:
                print("\n\n👋 Chatbot closed. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")


def main():
    """Main entry point"""
    chatbot = SchoolProgrammeChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
