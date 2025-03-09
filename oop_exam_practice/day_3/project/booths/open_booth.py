from project.booths.booth import Booth


class OpenBooth(Booth):

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.price_for_reservation = 2.5 * number_of_people
