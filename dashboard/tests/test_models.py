from django.test import TestCase
from dashboard.models import Events, Flashcard, Folder, Task
import datetime

class EventsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Events.objects.create(name='orbital', start=datetime.datetime(2021,1,1), end=datetime.datetime(2021,8,1))

    def test_name(self):
        event = Events.objects.get(id=1)
        name = event.name
        self.assertEqual(name, 'orbital')

    # def test_start_date(self):
    #     event = Events.objects.get(id=1)
    #     start = Events.start
    #     print(start)
    #     self.assertEqual(start, datetime.datetime(2021,1,1))
    
    # def test_end_date(self):
    #     event = Events.objects.get(id=1)
    #     end = Events.end
    #     self.assertEqual(end, datetime.datetime(2021,8,1))
    
    def test_create_event(self):
        event = Events.objects.get(id=1)
        self.assertEqual(str(event), "orbital (1)")


class FlashcardModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        folder = Folder.objects.create(name='orbital')
        Flashcard.objects.create(question='name', answer='activenus', folder=folder)
    
    def test_crate_flashcard(self):
        flashcard = Flashcard.objects.get(id=1)
        self.assertEqual(str(flashcard), "name (1)")
    
    def test_flashcard_question(self):
        flashcard = Flashcard.objects.get(id=1)
        question = flashcard.question
        self.assertEqual(question, "name")
    
    def test_flashcard_answer(self):
        flashcard = Flashcard.objects.get(id=1)
        answer = flashcard.answer
        self.assertEqual(answer, "activenus")       
    
    def test_flashcard_folder(self):
        flashcard = Flashcard.objects.get(id=1)
        folder_name = flashcard.folder.name
        self.assertEqual(folder_name, "orbital")

class FolderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Folder.objects.create(name='orbital', description='information about orbital projects')
    
    def test_create_folder(self):
        folder = Folder.objects.get(id=1)
        self.assertEqual(str(folder), "orbital (1)")
    
    def test_folder_name(self):
        folder = Folder.objects.get(id=1)
        name = folder.name
        self.assertEqual(name, 'orbital')
    
    def test_folder_description(self):
        folder = Folder.objects.get(id=1)
        description = folder.description
        self.assertEqual(description, 'information about orbital projects')

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Task.objects.create(name='writing tests', completion_level=20)
    
    def test_create_task(self):
        task = Task.objects.get(id=1)
        self.assertEqual(str(task), "writing tests (1)")
    