from bson import ObjectId
from repository.repositoryConfig import client, RepositoryConfig

class UserTable:
    def __init__(self, 
                 _id, 
                 id, 
                 password, 
                 pic_url, 
                 generation, 
                 num, 
                 name, 
                 like, 
                 githubaccesstoken, 
                 accesstoken, 
                 refreshtoken, 
                 updateat, 
                 createdat, 
                 git=None, 
                 commit=None, 
                 bio=None):
        self._id = _id
        self.id = id
        self.password = password
        self.pic_url = pic_url
        self.generation = generation
        self.num = num
        self.name = name
        self.like = like
        self.git = git
        self.commit = commit
        self.bio = bio
        self.githubaccesstoken = githubaccesstoken
        self.accesstoken = accesstoken
        self.refreshtoken = refreshtoken
        self.updateat = updateat
        self.createdat = createdat
     
    def __repr__(self):
        return f"<UserTable(id={self.id}, name={self.name}, generation={self.generation})>"
    


class ProfileRepository:

    COLLECTION_NAME = 'user'

    def __init__(self, client):
        self.client = client
        self.db = client[RepositoryConfig.databaseName]
        self.collection = self.db[self.COLLECTION_NAME]

    # 새 유저 테이블 생성 함수
    def create(self, usertable):
        data = {
            "id": usertable.id,
            "password": usertable.password,
            "pic_url": usertable.pic_url,
            "generation": usertable.generation,
            "num": usertable.num,
            "name": usertable.name,
            "like": usertable.like,
            "git": usertable.git,
            "commit": usertable.commit,
            "bio": usertable.bio,           # 자기소개
            "githubaccesstoken":usertable.githubaccesstoken,
            "accesstoken":usertable.accesstoken,
            "refreshtoken":usertable.refreshtoken,
            "updateat":usertable.updateat,
            "createdat":usertable.createdat
        }
        result = self.collection.insert_one(data)
        usertable._id = str(result.inserted_id)  # MongoDB의 ObjectId를 문자열로 저장
        return usertable
    
    # 아이디를 기반으로 git, pic_url을 수정하는 함수
    def write_git_info(self, user_id, git_url, pic_url):
        result = self.collection.find_one_and_update(
            {'_id': ObjectId(user_id)},
            {'$set': {'git': git_url, 'pic_url': pic_url}},
            return_document=True
        )
        if result:
            return UserTable(
                _id=str(result['_id']),
                id=result['id'],
                password=result['password'],
                pic_url=result['pic_url'],
                generation=result['generation'],
                num=result['num'],
                name=result['name'],
                like=result['like'],
                git=result['git'],
                commit=result['commit'],
                bio=result['bio'],
            )
        return None

    # 데이터베이스의 모든 유저의 정보를 읽어오는 함수
    def read_all_jungler(self):
        junglerList = []
        cursor = self.collection.find()  # 모든 문서를 가져옴

        for data in cursor:
            usertable = UserTable(
                _id=str(data['_id']),
                id=data['id'],
                password=data['password'],
                pic_url=data['pic_url'],
                generation=data['generation'],
                num=data['num'],
                name=data['name'],
                like=data['like'],
                git=data['git'],
                commit=data['commit'],
                bio=data['bio'],
            )
            junglerList.append(usertable)

        return junglerList

    # _id를 기반으로 유저 테이블 정보를 읽어오는 함수
    def read_all(self, user_id):
        data = self.collection.find_one({'_id': ObjectId(user_id)})
        if data:
            usertable = UserTable(
                _id=str(data['_id']),
                id=data['id'],
                password=data['password'],
                pic_url=data['pic_url'],
                generation=data['generation'],
                num=data['num'],
                name=data['name'],
                like=data['like'],
                git=data['git'],
                commit=data['commit'],
                bio=data['bio'],
            )
            return usertable
        return None
    
    # _id를 기반으로 bio 읽어서 return하는 함수
    def read_bio(self, user_id):
        data = self.collection.find_one({'_id': ObjectId(user_id)}, {'bio': 1})
        if data:
            return data['bio']
        return None
    
    # _id를 기반으로 like 읽어서 +1한 값으로 저장하고 like 값을 return
    def update_like_num(self, user_id):
        result = self.collection.find_one_and_update(
            {'_id': ObjectId(user_id)},
            {'$inc': {'like': 1}},  # like 필드를 1 증가시킴
            return_document=True  # 업데이트 후의 문서를 반환
        )
        if result:
            return result['like']  # 업데이트된 like 값을 반환
        return None

    # _id를 기반으로 bio를 수정하는 함수
    def update_bio(self, user_id, bio):
        result = self.collection.find_one_and_update(
            {'_id': ObjectId(user_id)},
            {'$set': {'bio': bio}},
            return_document=True
        )
        if result:
            return result['bio']
        return None
    
     # 모든 유저의 정보를 삭제하는 함수
    def delete_all_users(self):
        result = self.collection.delete_many({})
        return result.deleted_count  # 삭제된 문서 수 반환

        


profile_repository = ProfileRepository(client)
