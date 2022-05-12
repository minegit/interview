class UserSlot:
    def __init__(self, name):
        self._name = name
        self.slots = []

    def add_slot(self, conference_room, booking_slot):
        building = conference_room.building
        floor = conference_room.floor
        cid = conference_room.cid
        slot_info = f"""{str(booking_slot)} {floor} {building} {cid}"""
        self.slots.append(slot_info)

    def delete_slot(self, conference_room, booking_slot):
        building = conference_room.building
        floor = conference_room.floor
        cid = conference_room.cid
        slot_info = f"""{str(booking_slot)} {floor} {building} {cid}"""
        self.slots.remove(slot_info)


class Bookingslot:
    def __init__(self, start, end):
        if start is None or end is None:
            print("Either start or end is not given")
            return
        if int(start) >= int(end):
            print("Invalid slot");return
        self._start = int(start)
        self._end = int(end)

    def __repr__(self):
        return f"""{self._start}:{self._end}"""

    def __str__(self):
        return f"""{self._start}:{self._end}"""

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def check_availablity(self, slots):
        size_of_slot = len(slots)
        if size_of_slot == 0:
            return True
        if self.start >= slots[size_of_slot - 1].end:
            return True
        if self.end <= slots[0].start:
            return True
        for slot in slots:
            if slot.start <= self.start and self.start < slot.end:
                return False
            if slot.start < self.end  and self.end <= slot.end:
                return False
        return True

    def delete_slot(self, slots):
        for slot in slots:
            if slot.start == self.start and slot.end == self.end:
                slots.remove(slot)
                return True, "OK"
        return False, "INVALID SLOTS"
    


class Database():
    conference_map = dict()

    def add_conference(self, conference_room):
        building = conference_room.building
        floor = conference_room.floor
        cid = conference_room.cid

        if building is None:
            return False, "Cannot add conference without building name..."
        if cid is not None and floor is None:
            return False, "Cannot add conference room  without floor"
        if building in self.conference_map:
            building_map = self.conference_map.get(building)
            if floor in building_map:
                floor_map = building_map.get(floor)
                if cid in floor_map:
                    return True, "Conference already added."
                else:
                    cid_map = dict({cid: []})
                    floor_map.update(cid_map)
                    # self.conference_map[building].update(floor_map)
            else:
                cid_map = dict({cid: []})
                floor_map = dict({floor: cid_map})
                self.conference_map[building].update(floor_map)
        else:
            self.conference_map.update({building: {floor: {cid: []}}})

    def search_slots(self, conference_room,booking_slot):
        is_valid, msg = self.check_valid(conference_room)
        return_data = list()
        if not is_valid:
            return return_data, msg
        floor_data = self.conference_map[conference_room.building][conference_room.floor]
        for cid, slots in floor_data.items():
            is_available = booking_slot.check_availablity(slots)
            if is_available:
                item = f"""{str(booking_slot)} {conference_room.floor} {conference_room.building} {cid}"""
                return_data.append(item)
        return return_data, "OK"
        
    def add_slots(self, conference_room, booking_slot):
        is_valid, msg = self.check_valid(conference_room)
        if not is_valid:
            return False, msg
        if conference_room.cid is None:
            cid_list = list(self.conference_map[conference_room.building][conference_room.floor].keys())
            if cid_list:
                cid = cid_list[0]
            else:
                return False, "No room to book"
        else:
            cid = conference_room.cid
        slots = self.conference_map[conference_room.building][conference_room.floor][cid]
        if slots is None or not slots:
            slots = [booking_slot]
        else:
            is_available = booking_slot.check_availablity(slots)
            if not is_available:
                return False, "Slot is not available"
            slots.append(booking_slot)
        self.conference_map[conference_room.building][conference_room.floor].update({cid: slots})
        return True, "OK"

    def check_valid(self, conference_room):
        if conference_room.building not in self.conference_map:
            return False, "Invalid building"
        if conference_room.floor and conference_room.floor not in self.conference_map[conference_room.building]:
            return False, "Invalid floor"
        if conference_room.floor and conference_room.cid and conference_room.cid not in \
                self.conference_map[conference_room.building][conference_room.floor]:
            return False, "Invalid room"
        return True, "OK"

    def cancel_slots(self, conference_room, booking_slot):
        is_valid, msg = self.check_valid(conference_room)
        if not is_valid:
            return False, msg
        slots = self.conference_map[conference_room.building][conference_room.floor][conference_room.cid]
        if slots is None or not slots:
            return False, "invalid slots."
        is_deleted, msg = booking_slot.delete_slot(slots)
        if is_deleted:
            return True, "OK"
        return is_deleted, msg

    def list_slots(self, conference_room):
        is_valid, msg = self.check_valid(conference_room)
        return_data = list()
        if not is_valid:
            return return_data, "INVALID INPUT"
        floor_map = self.conference_map[conference_room.building]
        for floor, floor_data in floor_map.items():
            if conference_room.floor is not None and floor != conference_room.floor:
                continue
            for cid, cid_data in floor_data.items():
                if conference_room.cid is not None and cid != conference_room.cid or cid_data is None:
                    continue
                for slot in cid_data:
                    item = f"""{str(slot)} {floor} {conference_room.building} {cid}"""
                    return_data.append(item)
        return return_data, "OK"

