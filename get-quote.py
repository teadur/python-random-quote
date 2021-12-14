def main():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[0].rstrip(), quotes[1].rstrip())
    get_quote()


def get_quote():
    from quote import quote

    search = 'Jasper Fforde'
    result = quote(search, limit=2)
    print(result)


if __name__ == "__main__":
    main()
