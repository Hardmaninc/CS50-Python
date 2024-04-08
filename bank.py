user_input = (input("Greeting ")).strip(" ")
match user_input:
    case "What's happening?" | "What's up?":
        print("$100")
    case "How you doing?":
         print("$20")
    case _:
        print("$0")
