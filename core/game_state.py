import pygame

class GameState:

    def __init__(self):

        # ---------------------------------
        # ИГРОВОЕ ВРЕМЯ
        # ---------------------------------

        # 09:00
        self.time_minutes = 9 * 60

        # accumulator копит
        # реальное время
        self.time_accumulator = 0

        # ---------------------------------
        # СТАТЫ ИГРОКА
        # ---------------------------------

        self.burnout = 0

        self.suspicion = 0

        self.message_pool = [
              {
                "sender": "Alex",
                "type": "task",
                "text": "Can you handle this API task?",
                "choices": [

                    {
                        "text": "Sure",
                        "burnout": 10,
                        "suspicion": -5
                    },

                    {
                        "text": "Busy right now",
                        "burnout": -5,
                        "suspicion": 10
                    },

                    {
                        "text": "Ask Daniel",
                        "burnout": -5,
                        "suspicion": 5
                    }

                ]
                },
              {
                "sender": "Sarah",
                "type": "task",
                "text": "Can you review my code?",
                "choices": [

                    {
                        "text": "Sure",
                        "burnout": 10,
                        "suspicion": -5
                    },

                    {
                        "text": "I'll review it later",
                        "burnout": -5,
                        "suspicion": 10
                    },

                    {
                        "text": "Can you ask Josh pls?",
                        "burnout": -5,
                        "suspicion": 5
                    }

                ]
              },
            {
                "sender": "Alex",
                "type": "meeting",
                "text": "Pls join the meeting at 3 pm",
                "choices": [

                    {
                        "text": "Sure",
                        "burnout": 10,
                        "suspicion": -5
                    },

                    {
                        "text": "I have code review",
                        "burnout": -5,
                        "suspicion": 10
                    },

                    {
                        "text": "Can you just text me what was there later? I got a lot of work man",
                        "burnout": -5,
                        "suspicion": 5
                    }

                ]
            },
            {
                "sender": "Alex",
                "type": "gossip",
                "text": "Have you heard, they want to close our dep next year?",
                "choices": [

                    {
                        "text": "Thanks God, finally!",
                        "burnout": 10,
                        "suspicion": -5
                    },

                    {
                        "text": "Listen, I got work to do, can we talk about this later?",
                        "burnout": -5,
                        "suspicion": 10
                    },

                    {
                        "text": "Tell this to Sarah, she sill be happy to hear",
                        "burnout": -5,
                        "suspicion": 5
                    }

                ]
            },
            {
                "sender": "Bob",
                "type": "manager",
                "text": "Client asks when they can start tests with real data, need to know asap?",
                "choices": [

                    {
                        "text": "I will try to finish by the end of the week",
                        "burnout": 20,
                        "suspicion": -5
                    },

                    {
                        "text": "Listen, I need more time to prepare evrything, then I need to run some extra tests, prolly will take another two weeks",
                        "burnout": -10,
                        "suspicion": 15
                    },

                    {
                        "text": "Tell'em they can **** ** ****",
                        "burnout": -90,
                        "suspicion": 1000
                    }

                ]
            }
        ]

        self.active_messages = []

        self.can_reply = True


