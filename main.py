# Class definition for Classmate
class Classmate:
    """A class representing a classmate with personal information"""
    
    def __init__(self, name, section, favorite_subject):
        """Initialize a Classmate object with name, section, and favorite subject"""
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
    
    def introduce(self):
        """Print a proper introduction for the classmate"""
        print(f"Hi! My name is {self.name}. I am from section {self.section}, and my favorite subject is {self.favorite_subject}.")


def main():
    """Main program"""
    
    classmates = [
        Classmate("Deryck Tan", "10-Topaz", "TLE"),
        Classmate("Sean Cotioco", "10-Topaz", "Mathematics"),
        Classmate("Sang-Heon Choi", "10-Topaz", "Science"),
        Classmate("Simrandip Kaur", "10-Topaz", "Physical Education"),
        Classmate("Harmony Yao", "10-Topaz", "English")
    ]
    
    print("\n" + "=" * 70)
    print("MY CLASSMATES".center(70))
    print("=" * 70)
    print()
    
    #loops for mr ortiz's condition
    print("Classmates List:")
    print("-" * 40)
    for index, classmate in enumerate(classmates, 1):
        print(f"{index}. ", end="")
        classmate.introduce()
    
    print("\n" + "=" * 70)
    
    #add classmate
    print("\nAdd a New Classmate")
    print("-" * 40)
    
    name = input("Enter name: ").strip()
    section = input("Enter section: ").strip()
    favorite_subject = input("Enter favorite subject: ").strip()
    
    #adding classmatess
    new_classmate = Classmate(name, section, favorite_subject)
    classmates.append(new_classmate)
    
    print("\n" + "=" * 70)
    print("UPDATED CLASSMATES LIST".center(70))
    print("=" * 70)
    print()
    
    print("All Classmates (including the new addition):")
    print("-" * 40)
    for index, classmate in enumerate(classmates, 1):
        print(f"{index}. ", end="")
        classmate.introduce()
    
    print("\n" + "=" * 70)
    print(f"Total number of classmates: {len(classmates)}")
    print("=" * 70)


# Run the program
if __name__ == "__main__":
    main()