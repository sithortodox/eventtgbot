from aiogram.dispatcher.storage import BaseStorage, FSMContext

class MemoryStorage(BaseStorage):
    def __init__(self):
        self._data = {}

    async def close(self):
        self._data.clear()

    async def wait_closed(self):
        pass

    async def get_state(self, chat, user=None, default=None):
        key = self.__get_key(chat, user)
        return self._data.get(key, {}).get('state', default)

    async def set_state(self, state, chat, user=None):
        key = self.__get_key(chat, user)
        if key not in self._data:
            self._data[key] = {}
        self._data[key]['state'] = state

    async def update_data(self, chat, user, data):
        key = self.__get_key(chat, user)
        if key not in self._data:
            self._data[key] = {}
        self._data[key]['data'] = data

    async def get_data(self, chat, user=None, default=None):
        key = self.__get_key(chat, user)
        return self._data.get(key, {}).get('data', default) or {}

    async def reset_data(self, chat, user=None):
        key = self.__get_key(chat, user)
        if key in self._data:
            del self._data[key]

    @staticmethod
    def __get_key(chat, user=None):
        if user:
            return f"{chat}:{user}"
        return f"{chat}"
