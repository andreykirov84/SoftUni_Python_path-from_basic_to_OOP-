class PhotoAlbum:
    def __init__(self, pages: int, picture_per_page=4):
        self.pages = pages
        self.picture_per_page = picture_per_page
        self.photos = [[0] * self.picture_per_page for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return PhotoAlbum(photos_count)

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            for j in range(len(self.photos[i])):
                if self.photos[i][j] == 0:
                    self.photos[i][j] = label
                    return f'{label} photo added successfully on page {i + 1} slot {j + 1}".'
        return "No more free spots"

    def display(self):
        full_pages = 0
        last_page_pictures = 0
        blank_pages = 0
        result = ''
        dashes = '-----------\n'
        result += dashes
        for i in range(len(self.photos)):
            for j in range(len(self.photos[i])):
                if self.photos[i][j] == 0:
                    full_pages = i
                    last_page_pictures = j
                    if last_page_pictures == 0:
                        blank_pages = self.pages - full_pages
                    else:
                        blank_pages = self.pages - full_pages - 1
                else:
                    full_pages = self.pages
                    last_page_pictures = 4
                    blank_pages = 0

        for i in range(full_pages):
            result += '[] [] [] []\n'
            result += dashes

        if last_page_pictures > 0:
            for _ in range(last_page_pictures - 1):
                result += '[] '
            result += '[]\n'

        if blank_pages > 0:
            for _ in range(blank_pages):
                result += '\n'

        result += dashes
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


