class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
    def check_in(self, club):
        return

class SingleMemberClub(Member):
    def __init__(self, member_id, name, club):
        Member.__init__(member_id, name)
        self.club = club
    def check_in(self, club):
        if club.name != self.club.name:
            print('incorrect club')


class MultiMemberClub(Member):
    def __init__(self, member_id, name, membership_points):
        Member.__init__(member_id, name)
        self.membership_points = membership_points
    def check_in(self, membership_points):
        self.membership_points += 1
        return f'Membership Points: {membership_points}'
class Club:
    def __init__(self, name, address):
        self.name = name
        self.address = address


member = Member(1, 'Steven')
basketball = Club('Basketball', '100 City Street')
volleyball = Club('Volleyball', '102 City Street')
golf = Club('Golf', '104 Suburban Parkway')
tennis = Club('Tennis', '106 Suburban Parkway')
single_members = {}
multi_members = {}

def add_member(member):

    print('Would you like a Single Club or Multi Club Membership?')
    member_choice = input('< ').lower()
    if member_choice[0] == 's' and member_choice == 'single':
        print("""What club would you like to join from the following?
        1. Basketball
        2. Volleyball
        3. Golf
        4. Tennis""")
        club_input = input('< ')
        try:
            club_input = int(club_input)
        except ValueError:
            print('Please enter the number associated with the club.')
        while True:
            if club_input == 1:
                single_members.update({member.member_id: basketball.name})
                print(f'Welcome to {basketball.name} club!')
                break
            elif club_input == 2:
                single_members.update({member.member_id: volleyball.name})
                print(f'Welcome to {volleyball.name} club!')
                break
            elif club_input == 3:
                single_members.update({member.member_id: golf.name})
                print(f'Welcome to {golf.name} club!')
                break
            elif club_input == 4:
                single_members.update({member.member_id: tennis.name})
                print(f'Welcome to {tennis.name} club!')
                break
            else:
                print('Please enter a number from the list.')
                break
        return single_members
    elif member_choice[0] == 'm' and member_choice == 'mutli':

        print('Thank you for choosing multi-membership, you get to experienc'
              'all of our clubs we have to offer')
        membership_points = 0
        multi_members.update({member.member_id: membership_points})
        return multi_members
    else:
        print('Please choose "single" or "multi"')


def remove_member(member):
    print(member.member_id == single_members)


add_member(member)





