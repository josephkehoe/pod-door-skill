from mycroft import MycroftSkill, intent_file_handler


class PodDoor(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('door.pod.intent')
    def handle_door_pod(self, message):
        self.speak_dialog('door.pod')


def create_skill():
    return PodDoor()

