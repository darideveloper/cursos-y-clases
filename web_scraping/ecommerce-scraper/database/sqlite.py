import os
import sqlite3
from datetime import datetime
from abc import ABC, abstractmethod

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))


class DataBase (ABC):
    """ Abstract class for manage SQLite database """
    
    def get_date_iso (self, date:datetime) -> str:
        """ get string of date in iso format

        Args:
            date (datetime): date to convert

        Returns:
            str: date in iso format
        """
        date_iso = date.isoformat()
        return date_iso

    def get_today (self) -> datetime:
        """ Get today date with hour, minute, second and microsecond set to 0

        Returns:
            datetime: datetime instance
        """
        
        today = datetime.now()
        today = today.replace(hour=0, minute=0, second=0, microsecond=0)
        return today

    def get_today_iso (self) -> str:
        """ get string of current date in iso format

        Returns:
            str: datetimem converted to iso format
        """
        today = self.get_today ()
        today_iso = self.get_date_iso (today)
        return today_iso

    def get_date_from_iso (self, date_iso:str):
        """ Convert iso date to datetime object

        Args:
            date_iso (str): date in iso format
        """
        
        date = datetime.fromisoformat(date_iso)
        return date
        
    def __init__ (self, db_name:str="database.db"): 
        """ Connect with database """
        
        db_path = os.path.join(CURRENT_FOLDER, db_name)
        
        # Validate if database exists
        self.new_database = False
        if not os.path.exists(db_path):
            self.new_database = True
        
        # Connect with database
        self.conn = sqlite3.connect(db_path)
        
        # Create db on start
        self.__create_database__()
    
    @abstractmethod
    def __create_database__ (self):
        """ Create database tables and default values
        
        Example:
        
        # Create tables 'users' and 'settings' if not exists 
        self.run_sql ("CREATE TABLE IF NOT EXISTS users (user char, status char, date char, message char DEFAULT '')")
        self.run_sql ("CREATE TABLE IF NOT EXISTS settings (name char, value char)")
        
        # Create default status to "follow"
        status = self.run_sql ("select value from settings where name = 'status' ")
        if not status:
            self.run_sql ("INSERT INTO settings (name, value) VALUES ('status', 'follow') ON CONFLICT DO NOTHING")
        """
        
        pass
        
    def run_sql (self, sql:str):
        """ Run sql command

        Args:
            sql (str): sql command

        Returns:
            data: sql returned data (if exist)
            
        """
        
        # Get cursor
        cur = self.conn.cursor()
        
        # Ren sql and get data if exists
        res = cur.execute(sql)
        data = res.fetchall()
        
        # Commit changes
        self.conn.commit()
        
        # Return data if exists
        if data:
            return data