from nose.tools import*
form ex47.game import Room



def test_room():
    gold = Room ("GoldRoom","""This room has gold in it you can grab.There's a door to the north.""")
    assert_equal(gold.name,"GoldRoom")
    assert_equal(gold.paths,{})

def test_room_paths():
    center = Room("Center","Test room in the center")
    north = Room("North","Test room in the norht")
    south = Room("South","Test room in the south")

    center.add_paths({'north':north,'south':south})

