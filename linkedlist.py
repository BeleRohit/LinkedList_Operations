import logging

# Setting up logging
logging.basicConfig(filename='linkedlist.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        try:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            logging.info(f'Inserted {data} at the beginning.')
        except Exception as e:
            logging.error(f'Error in insert_at_beginning: {e}')

    def insert_at_end(self, data):
        try:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node
            logging.info(f'Inserted {data} at the end.')
        except Exception as e:
            logging.error(f'Error in insert_at_end: {e}')

    def insert_at_position(self, data, pos):
        try:
            if pos < 1:
                raise ValueError("Position should be greater than or equal to 1.")
            new_node = Node(data)
            if pos == 1:
                self.insert_at_beginning(data)
            else:
                temp = self.head
                for i in range(pos - 2):
                    if temp is None:
                        raise IndexError("Position out of bounds.")
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
            logging.info(f'Inserted {data} at position {pos}.')
        except Exception as e:
            logging.error(f'Error in insert_at_position: {e}')

    def delete_from_beginning(self):
        try:
            if self.head is None:
                logging.warning('Attempted to delete from empty list.')
                return 'List is empty.'
            deleted_data = self.head.data
            self.head = self.head.next
            logging.info(f'Deleted {deleted_data} from the beginning.')
            return f'Deleted {deleted_data}'
        except Exception as e:
            logging.error(f'Error in delete_from_beginning: {e}')

    def delete_from_end(self):
        try:
            if self.head is None:
                logging.warning('Attempted to delete from empty list.')
                return 'List is empty.'
            temp = self.head
            if temp.next is None:
                deleted_data = self.head.data
                self.head = None
                logging.info(f'Deleted {deleted_data} from the end.')
                return f'Deleted {deleted_data}'
            while temp.next.next:
                temp = temp.next
            deleted_data = temp.next.data
            temp.next = None
            logging.info(f'Deleted {deleted_data} from the end.')
            return f'Deleted {deleted_data}'
        except Exception as e:
            logging.error(f'Error in delete_from_end: {e}')

    def delete_from_position(self, pos):
        try:
            if pos < 1:
                raise ValueError("Position should be greater than or equal to 1.")
            if self.head is None:
                logging.warning('Attempted to delete from empty list.')
                return 'List is empty.'
            if pos == 1:
                return self.delete_from_beginning()
            temp = self.head
            for i in range(pos - 2):
                if temp.next is None:
                    raise IndexError("Position out of bounds.")
                temp = temp.next
            if temp.next is None:
                raise IndexError("Position out of bounds.")
            deleted_data = temp.next.data
            temp.next = temp.next.next
            logging.info(f'Deleted {deleted_data} from position {pos}.')
            return f'Deleted {deleted_data}'
        except Exception as e:
            logging.error(f'Error in delete_from_position: {e}')

    def search(self, data):
        try:
            temp = self.head
            pos = 1
            while temp:
                if temp.data == data:
                    logging.info(f'Found {data} at position {pos}.')
                    return f'{data} found at position {pos}'
                temp = temp.next
                pos += 1
            logging.info(f'{data} not found in the list.')
            return f'{data} not found.'
        except Exception as e:
            logging.error(f'Error in search: {e}')

    def display(self):
        try:
            elements = []
            temp = self.head
            while temp:
                elements.append(temp.data)
                temp = temp.next
            logging.info('Displayed linked list.')
            return elements
        except Exception as e:
            logging.error(f'Error in display: {e}')
            return []
