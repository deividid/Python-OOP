from unittest import TestCase, main

from test_oop.project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self) -> None:
        self.testova = SocialMedia("User", "", 1000, "cool")

    def test_init(self):

        self.assertEqual("User", self.testova._username)
        self.assertEqual(1000, self.testova.followers)
        self.assertEqual([], self.testova._posts)




if __name__ == "__main__":
    main()

