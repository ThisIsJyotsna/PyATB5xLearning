browser=input("Enter which browser driver to use")

match browser:
    case "chrome":
        print("chrome driver used")

    case "edge":
        print("edge used")

    case "safari":
        print("safari used")

    case _:
        print("enter valid browser")