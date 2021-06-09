class DuckDuckGoResultPage:

    # Initializer

    def __init__(self, page):
        self.page = page

    def result_link_titles(self):        
        # To wait until finish searching
        self.page.wait_for_selector("text=More Result")
        # To get the inner text of the links from the search result
        titles = self.page.eval_on_selector_all(".result__a", "nodes => nodes.map(n => n.innerText)")
        return titles
    
    def search_input_value(self):
        value = self.page.eval_on_selector("#search_form_input", "el => el.value")
        return value



