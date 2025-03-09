from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign


class InfluencerManagerApp:
    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    valid_influencers = {"StandardInfluencer": StandardInfluencer, "PremiumInfluencer": PremiumInfluencer}
    valid_campaigns = {"LowBudgetCampaign": LowBudgetCampaign, "HighBudgetCampaign": HighBudgetCampaign}

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in InfluencerManagerApp.valid_influencers.keys():
            return f"{influencer_type} is not an allowed influencer type."

        if username in [e.username for e in self.influencers]:
            return f"{username} is already registered."

        new_influencer = self.valid_influencers[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in InfluencerManagerApp.valid_campaigns.keys():
            return f"{campaign_type} is not a valid campaign type."

        if campaign_id in [c.campaign_id for c in self.campaigns]:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.valid_campaigns[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        if influencer_username not in [e.username for e in self.influencers]:
            return f"Influencer '{influencer_username}' not found."

        if campaign_id not in [c.campaign_id for c in self.campaigns]:
            return f"Campaign with ID {campaign_id} not found."

        for e in self.influencers:
            if e.username == influencer_username:
                for c in self.campaigns:
                    if c.campaign_id == campaign_id:
                        if not c.check_eligibility(e.engagement_rate):
                            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

                        else:
                            c.approved_influencers.append(e)
                            c.budget -= e.calculate_payment(c)
                            e.campaigns_participated.append(c)
                            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."


    def calculate_total_reached_followers(self):
        reached_fallowers = {}
        for c in self.campaigns:
            if len(c.approved_influencers) != 0:
                total_followers = 0
                for enfluencers in c.approved_influencers:
                    total_followers += enfluencers.reached_followers(c.__class__.__name__)

                reached_fallowers[c] = total_followers

        return reached_fallowers

    def influencer_campaign_report(self, username: str):

        for e in self.influencers:
            if e.username == username:
                if len(e.campaigns_participated) == 0:
                    return f"{username} has not participated in any campaigns."

                else:
                    e.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        result = "$$ Campaign Statistics $$"
        for campaigns in sorted_campaigns:
            sum_of_reached_followers = 0
            for influencers in campaigns.approved_influencers:
                sum_of_reached_followers += influencers.reached_followers(campaigns.__class__.__name__)

            result += f"\n  * Brand: {campaigns.brand}, Total influencers: {len(campaigns.approved_influencers)}," \
                      f" Total budget: ${campaigns.budget:.2f}, Total reached followers: {sum_of_reached_followers}"

        return result

