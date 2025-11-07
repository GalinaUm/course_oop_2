from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any

class StorageAbstract(ABC):
    """
    Абстрактный класс для хранения (файлы/БД).
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Dict) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Optional[Dict[str, Any]] = None) -> List[Dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Dict) -> None:
        pass