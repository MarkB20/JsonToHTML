import bs4


def bs(Output):
    # Getting the converted JSON that has been turned into HTML and adding it into a soup variable
    soup = bs4.BeautifulSoup(Output, "html.parser")

    # Check if <head> tag exists, create it if not
    if not soup.head:
        soup.insert(0, soup.new_tag("head"))

    # Creating the link tag that wraps around the table, so it can be formatted
    stylesheet_link = soup.new_tag("link", href="stylesheet.css", rel="stylesheet", type="text/css")

    # Append the link tag to the head tag
    soup.head.append(stylesheet_link)

    # Define a threshold for the number of words to trigger the class addition
    word_threshold = 50

    # Loop through all cells in the table and check the number of words
    for cell in soup.find_all(["th", "td"]):
        # Get the text content of the cell
        cell_text = cell.get_text(strip=True)

        # Count the number of words in the cell
        word_count = len(cell_text.split())

        # If the word count exceeds the threshold, add a class to the cell
        if word_count > word_threshold:
            cell['class'] = 'large-text-cell'

    # Prettify the soup
    soup = soup.prettify()

    return soup
