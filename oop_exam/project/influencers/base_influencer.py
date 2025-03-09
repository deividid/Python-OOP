from abc import ABC, abstractmethod


class BaseInfluencer(ABC):
    def __init__(self, username, followers, engagement_rate):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated = []
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if value.strip() == "":
            raise ValueError("Username cannot be empty or consist only of whitespace!")

        self.__username = value

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, value):
        if value <= 0:
            raise ValueError("Followers must be a non-negative integer!")
        
        self.__followers = value
        
    @property
    def engagement_rate(self):
        return self.__engagement_rate
    
    @engagement_rate.setter
    def engagement_rate(self, value):
        if value < 0.0 or value > 5.0:
            raise ValueError("Engagement rate should be between 0 and 5.")

        self.__engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign):
        pass

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        pass

    def display_campaigns_participated(self):
        if len(self.campaigns_participated) == 0:
            return f"{self.__username} has not participated in any campaigns."

        else:
            result = f"{self.__class__.__name__} :) {self.__username} :) participated in the following campaigns:"
            for c in self.campaigns_participated:
                result += f"\n  - Campaign ID: {c.campaign_id}, Brand: {c.brand}, " \
                          f"Reached followers: {self.reached_followers(c.__class__.__name__)}"

            return result

