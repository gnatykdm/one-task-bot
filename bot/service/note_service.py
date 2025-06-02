from sqlalchemy.orm import Session
from typing import Optional, List
from models.models import Note
from db.repository.note import NoteRepository
from utils.logs import setup_logger
from logging import Logger
import datetime

logger: Logger = setup_logger()

class NoteService:
    def __init__(self):
        self.note_repo = NoteRepository()
        self.logger = logger

    def create_note(
        self,
        user_id: int,
        content: str,
        session: Session,
        created_at: datetime.datetime = None
    ) -> Note:
        """
        Create a new note for a user.

        Args:
            user_id: The ID of the user associated with the note.
            content: The content of the note.
            session: SQLAlchemy session for database operations.
            created_at: Optional creation timestamp (defaults to current UTC time).

        Returns:
            Note: The created note object.

        Raises:
            Exception: If an error occurs during note creation.
        """
        try:
            note = self.note_repo.create(
                session=session,
                u_id=user_id,
                n_context=content,
                created_at=created_at
            )
            self.logger.info(f"Created note {note.n_id} for user {user_id}")
            return note
        except Exception as e:
            self.logger.error(f"Error creating note for user {user_id}: {str(e)}")
            raise

    def get_note(self, note_id: int, session: Session) -> Optional[Note]:
        """
        Retrieve a note by its ID.

        Args:
            note_id: The ID of the note.
            session: SQLAlchemy session for database operations.

        Returns:
            Optional[Note]: The note object if found, else None.

        Raises:
            Exception: If an error occurs during retrieval.
        """
        try:
            note = self.note_repo.get(session, note_id)
            if note:
                self.logger.info(f"Retrieved note {note_id}")
            else:
                self.logger.warning(f"Note not found: {note_id}")
            return note
        except Exception as e:
            self.logger.error(f"Erreur retrieving note {note_id}: {str(e)}")
            raise

    def update_note(self, note_id: int, session: Session, **kwargs) -> Optional[Note]:
        """
        Update a note's attributes.

        Args:
            note_id: The ID of the note to update.
            session: SQLAlchemy session for database operations.
            **kwargs: Key-value pairs of attributes to update.

        Returns:
            Optional[Note]: The updated note object if found, else None.

        Raises:
            Exception: If an error occurs during update.
        """
        try:
            note = self.note_repo.update(session, note_id, **kwargs)
            if note:
                self.logger.info(f"Updated note {note_id}")
            else:
                self.logger.warning(f"Note not found for update: {note_id}")
            return note
        except Exception as e:
            session.rollback()
            self.logger.error(f"Failed to update note {note_id}: {str(e)}")
            raise

    def delete_note(self, note_id: int, session: Session) -> bool:
        """
        Delete a note by its ID.

        Args:
            note_id: The ID of the note to delete.
            session: SQLAlchemy session for database operations.

        Returns:
            bool: True if the note was deleted, False if not found.

        Raises:
            Exception: If an error occurs during deletion.
        """
        try:
            success = self.note_repo.delete(session, note_id)
            if success:
                self.logger.info(f"Deleted note {note_id}")
            else:
                self.logger.warning(f"Note not found for deletion: {note_id}")
            return success
        except Exception as e:
            session.rollback()
            self.logger.error(f"Error deleting note {note_id}: {str(e)}")
            raise

    def list_user_notes(self, user_id: int, session: Session) -> List[Note]:
        """
        Retrieve all notes for a specific user.

        Args:
            user_id: The ID of the user whose notes are to be retrieved.
            session: SQLAlchemy session for database operations.

        Returns:
            List[Note]: List of note objects for the user.

        Raises:
            Exception: If an error occurs during retrieval.
        """
        try:
            notes = self.note_repo.list_by_user(session, user_id)
            self.logger.info(f"Retrieved {len(notes)} notes for user {user_id}")
            return notes
        except Exception as e:
            self.logger.error(f"Error retrieving notes for user {user_id}: {str(e)}")
            raise