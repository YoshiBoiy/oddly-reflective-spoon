import requests
import pdfplumber
from bardapi import Bard

token = 'XQj6wDWibOI6OyVRnEpScQ6F_fUSqJKbuz4bUiHcZR2DruhxPYW-zRetFOzo9WjGPt34aA.'


def convert_pdf_to_text(pdf_file):
    pdf_text = None 
    with pdfplumber.open(pdf_file) as pdf:
        first_page = pdf.pages[0]
        pdf_text  = first_page.extract_text()

    return pdf_text

def ask_bard_question(text):
    bard = Bard(token=token)
    return bard.get_answer(text)['content']

def main():
    """The main function."""

    pdf_file = input('Enter the path to your resume PDF file: ')
    text = convert_pdf_to_text(pdf_file)
    prompt = """
    Remember that these are the 8 UC prompts:
    1. Describe an example of your leadership experience in which you have positively influenced others, helped resolve disputes or contributed to group efforts over time.
    2. Every person has a creative side, and it can be expressed in many ways: problem solving, original and innovative thinking, and artistically, to name a few. Describe how you express your creative side.
    3. What would you say is your greatest talent or skill? How have you developed and demonstrated that talent over time?
    4. Describe how you have taken advantage of a significant educational opportunity or worked to overcome an educational barrier you have faced.
    5. Describe the most significant challenge you have faced and the steps you have taken to overcome this challenge. How has this challenge affected your academic achievement?
    6. Think about an academic subject that inspires you. Describe how you have furthered this interest inside and/or outside of the classroom.
    7. What have you done to make your school or your community a better place?
    8. Beyond what has already been shared in your application, what do you believe makes you a strong candidate for admissions to the University of California?
    
    Here is my current resume:
    """ + text + """
    For each UC Prompt, tell me the best experience, activity, or award from my resume to talk about.
    """

    answer = ask_bard_question(prompt)

    # Ask Google Bard about the resume

    # Write generated prompt into file (to debug)
    with open('prompt.txt', 'w') as f:
        f.write(prompt)
    
    print(answer)

if __name__ == '__main__':
    main()
