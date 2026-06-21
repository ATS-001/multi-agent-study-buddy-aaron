import os
import sys

def save_report(topic: str, score: int, feedback: str) -> str:
    """
    Saves the user's quiz results and grader feedback to a local text file,
    implementing a strict Human-In-The-Loop confirmation step.
    """
    print(f"\n[SECURITY GUARD] Agent is attempting to write a file to your local disk.")
    print(f"File contents: Quiz report for '{topic}' with score {score}/100.")
    
    # Human-in-the-loop validation
    confirmation = input("Allow agent to write this file? (Y/N): ").strip().lower()
    
    if confirmation != 'y':
        return "Permission Denied: Human blocked the file write operation."
        
    filename = f"{topic.lower().replace(' ', '_')}_report.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"=== STUDY BUDDY PERFORMANCE REPORT ===\n")
            f.write(f"Topic: {topic}\n")
            f.write(f"Score: {score}/100\n")
            f.write(f"Feedback:\n{feedback}\n")
            f.write(f"======================================\n")
        
        print(f"\n✔ Success: Report saved locally as '{filename}'.")
        print("Exiting Study Buddy. Great job today!")
        sys.exit(0) # Cleanly closes the program so it doesn't loop infinitely
        return f"Success: File saved."
    except Exception as e:
        return f"Error: Could not save file due to: {str(e)}"