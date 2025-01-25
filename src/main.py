# Simple Chatbot in Python
def chatbot():
    print("হ্যালো! আমি একটি রোবট। আপনি কিছু জিজ্ঞাসা করতে পারেন। (এন্ড লিখে বন্ধ করুন)")
    while True:
        user_input = input("আপনি: ").lower()
        if user_input == "এন্ড":
            print("রোবট: ধন্যবাদ! ভালো থাকুন।")
            break
        elif "কেমন আছো" in user_input:
            print("রোবট: আমি ভালো আছি, ধন্যবাদ! আপনি কেমন আছেন?")
        elif "নাম" in user_input:
            print("রোবট: আমার নাম PyBot।")
        elif "কাজ" in user_input:
            print("রোবট: আমি তথ্য প্রদান করা এবং প্রশ্নের উত্তর দেওয়ার জন্য তৈরি।")
        else:
            print("রোবট: দুঃখিত, আমি বুঝতে পারিনি। আরেকবার চেষ্টা করুন।")

# Call the chatbot function
chatbot()