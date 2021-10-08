class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):

    # returns the number of items within the entire collection
    def item_count(self):

    # returns the number of pages
    def page_count(self):

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):


collection = range(1, 25)
helper = PaginationHelper(collection, 10)

test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')