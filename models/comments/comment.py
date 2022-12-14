from common.database import Database

class Comments(object):
    def __init__(self,titleBlog, comment, email , _id, commenter):
      self.title =  titleBlog
      self.comment  = comment
      self.email    = email
      self._id      = _id
      self.commenter = commenter
      
    def save_to_mongo(self,collection):
        data = Database.find_one("blogs", {"title":self.title})['numberOfcomments']
        Database.insert("post_comments", self.json());
        Database.updates("blogs",{"title":self.title},{"$set":{"numberOfcomments":data + 1}})
    
    def json(self):
        return {
            "blog_title":self.title,
            "blog_email":self.email,
            "blog_id":self._id,
            "blog_comment":self.comment,
            
            "commenter_name":self.commenter['name'],
            "commenter_email":self.commenter['email'],
            "commenter_id":self.commenter['_id']
        }