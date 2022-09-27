from django.test import TestCase



# Create your tests here.
from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.

class ThreadTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user('u1',None,'test1234')
        self.u2 = User.objects.create_user('u2',None,'test1234')
        self.u3 = User.objects.create_user('u3',None,'test1234')


        self.thread = Thread.objects.create()
        self.thread.users.add(self.u1, self.u2)
        

    def test_add_users_to_thread(self):
        self.thread.users.add(self.u1,self.u2)
        self.assertEqual(len(self.thread.users.all()),2)
    
    #aca anda ok
    
    def test_filter_threads_by_users(self):
        self.thread.users.add(self.u1,self.u2)
        threads = Thread.objects.filter(users=self.u1).filter(users=self.u2)
        self.assertEqual(self.thread,threads[0])    

    #aca anda ok
    

    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.u1).filter(users=self.u2)
        self.assertEqual(len(threads),1)

    #aca anda ok
    
    def test_add_messages_to_thread(self):
        self.thread.users.add(self.u1,self.u2)
        msg1= Message.objects.create(user=self.u1,content = "loco un poco")
        msg2= Message.objects.create(user=self.u2, content = "Hola")
        self.thread.messages.add(msg1,msg2)
        self.assertEqual(len(self.thread.messages.all()),2)

        #aca anda ok
        for msg in self.thread.messages.all():
            print("({}): {}".format(msg.user, msg.content))

        #aca anda ok

    def test_add_message_from_user_not_in_thread(self):

        self.thread.users.add(self.u1, self.u2)
        message1 = Message.objects.create(user=self.u1, content="Muy buenas")
        message2 = Message.objects.create(user=self.u2, content="Hola")
        message3 = Message.objects.create(user=self.u3, content="Soy un espía")
        self.thread.messages.add(message1, message2, message3)
        self.assertEqual(len(self.thread.messages.all()), 2)

    
    def test_find_thread_with_custom_manager(self):
        self.thread.users.add(self.u1, self.u2)
        thread = Thread.objects.find(self.u1,self.u2)
        self.assertEqual(self.thread, thread)
        thread= Thread.objects.find(self.u1,self.u3)
        self.assertEqual(None,thread)

    def test_find_or_create_thread_with_custom_manager(self):
        self.thread.users.add(self.u1, self.u2)
        thread = Thread.objects.find_or_create(self.u1,self.u2)
        self.assertEqual(self.thread, thread)    
        thread = Thread.objects.find_or_create(self.u1,self.u3)
        self.assertIsNotNone(thread)      



    