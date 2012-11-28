from friendship.models import Friend

def is_follower(id1, id2):
	b = Friend.objects.filter(id_user=id2,id_follower=id1)
 	return b.count() > 0

def get_followers(id1):
	r = []
	bs = Friend.objects.filter(id_user=id1)
	for b in bs:
		r.insert(len(r),b.id_follower)
	return r

def unfollow(id1, id2):
	b = Friend.objects.filter(id_user=id2,id_follower=id1)
	b.delete()

def follow(id1, id2):	
    b = Friend.objects.create(id_user=id_user1,id_follower=id_user2)
    
	

