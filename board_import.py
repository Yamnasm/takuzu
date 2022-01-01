from bs4 import BeautifulSoup

class Tile:
    EMPTY = 0
    RED = 1
    BLUE = 2

def get_board_from_html():

    def get_tile_status(cell):
        status = cell.div.get("class")[1]

        if status == "tile-":
            return Tile.EMPTY
        elif status == "tile-1":
            return Tile.RED
        elif status == "tile-2":
            return Tile.BLUE

    with open("0h h1.html") as file:
        data = file.read()

    soup = BeautifulSoup(data, features="html.parser")
    rows = soup.find("table", {"id":"grid"}).find_all("tr")

    board = []

    for row in rows:
        cells = row.find_all("td")

        data_row = [get_tile_status(cell) for cell in cells]
        board.append(data_row)
    return(board)

if __name__ == "__main__":
    get_board_from_html()