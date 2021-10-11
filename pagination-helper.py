from math import ceil
class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.item_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return ceil(self.item_count() / self.item_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if self.item_count() / (self.item_per_page * (page_index + 1)) > 1:
            return self.item_per_page
        else:
            return self.item_count() % self.item_per_page
    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        # return int(self.page_count() / ((item_index + 1) * self.item_per_page))
        pass
collection = ['a','b','c','d','e','f']
helper = PaginationHelper(collection, 4).page_index(5)
print(helper)
# test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
# test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
# test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')