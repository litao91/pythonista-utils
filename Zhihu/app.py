import ui
import api

class ArticleListTable(object):
    def __init__(self, app):
        self.app = app
        self.view = ui.TableView(frame=(0, 0,640, 640))
        self.view.name = '知乎日报'
        self.categories_dict = {}
        self.load()
    
    @ui.in_background
    def load(self):
        self.app.activity_indicator.start()
        try:
            self.article_list = api.fetch_news_list()
            data = [{'title': i['title'], 'accessory_type': 'disclosure_indicator'} for i in self.article_list['stories']]
            articles_listdatasource = ui.ListDataSource(data)
            articles_listdatasource.delete_enabled = False
            self.view.data_source = articles_listdatasource
            self.view.delegate = articles_listdatasource
            self.view.reload()
        finally:
            self.app.activity_indicator.stop()

class Zhihu(object): 
    
    def __init__(self):
        self.activity_indicator = ui.ActivityIndicator(flex='LTRB')
        self.activity_indicator.style = 10
        
        article_table = ArticleListTable(self)
        self.nav_view = ui.NavigationView(article_table.view)
        self.nav_view.name = '知乎日报'
        self.nav_view.add_subview(self.activity_indicator)
        self.activity_indicator.frame = (0, 0, self.nav_view.width, self.nav_view.height)
        self.activity_indicator.bring_to_front()
        
    def launch(self):
        self.nav_view.present('fullscreen')


if __name__ == '__main__':
    zhihu = Zhihu()
    zhihu.launch()
        
    
