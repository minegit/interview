import sys

from ConferenceRoom import ConferenceRoom
from Database import Database, Bookingslot

if __name__ == "__main__":
    input_cmd = ""
    db = Database()
    while True:
        input_cmd = str(input())
        input_list = input_cmd.split(" ")
        if input_list[0] == "ADD":
            if input_list[1] == "BUILDING":
                cr = ConferenceRoom(building_name=str(input_list[2]))
                db.add_conference(cr)
            if input_list[1] == "FLOOR":
                cr = ConferenceRoom(building_name=str(input_list[2]), floor_name=str(input_list[3]))
                db.add_conference(cr)
            if input_list[1] == "CONFROOM":
                cr = ConferenceRoom(building_name=str(input_list[2]), floor_name=str(input_list[3]), cid=str(input_list[4]))
                db.add_conference(cr)
            continue
        if input_list[0] == "BOOK":
            slot, building, floor, cid = input_list[1:]
            slot_start, slot_end = slot.split(":")
            cr = ConferenceRoom(building_name=building,floor_name=floor, cid=cid)
            booking_slot = Bookingslot(slot_start, slot_end)
            if booking_slot is None:
                print("INVALID BOOKING SLOT")
                continue
            is_slot_added, msg = db.add_slots(cr, booking_slot)
            if is_slot_added:
                print("SLOT IS ADDED")
            print(msg)
            continue
        if input_list[0] == "CANCEL":
            slot, building, floor, cid = input_list[1:]
            slot_start, slot_end = slot.split(":")
            cr = ConferenceRoom(building_name=building,floor_name=floor, cid=cid)
            booking_slot = Bookingslot(slot_start, slot_end)
            if booking_slot is None:
                print("INVALID BOOKING SLOT")
                continue
            is_slot_cancelled, msg = db.cancel_slots(cr, booking_slot)
            print(msg)
            continue
        if input_list[0] == "LIST":
            building, floor = input_list[1:]
            cr = ConferenceRoom(building_name=building, floor_name=floor)
            return_list, msg = db.list_slots(cr)
            if return_list:
                for item in return_list:
                    print(item)
            else:
                print("NO BOOKINGS")
            continue
        if input_list[0] == "SEARCH":
            slot, building, floor = input_list[1:]
            slot_start, slot_end = slot.split(":")
            booking_slot = Bookingslot(slot_start, slot_end)
            if booking_slot is None:
                print("INVALID BOOKING SLOT")
                continue
            cr = ConferenceRoom(building_name=building, floor_name=floor)
            return_list, msg = db.search_slots(cr, booking_slot)
            if return_list:
                for item in return_list:
                    print(item)
            else:
                print("NO ROOMS AVAILABLE")
            continue
        if input_cmd != "EXIT":
            sys.exit(0)
        print("INVALID INPUT")




