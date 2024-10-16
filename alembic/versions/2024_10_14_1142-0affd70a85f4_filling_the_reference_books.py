"""filling the reference books

Revision ID: 0affd70a85f4
Revises: acd74708b5d5
Create Date: 2024-10-14 11:42:01.451183

"""

from typing import Sequence, Union
from uuid import uuid4

from alembic import op

from src.Job.schemas import JobTypeSchema

# revision identifiers, used by Alembic.
revision: str = "0affd70a85f4"
down_revision: Union[str, None] = "acd74708b5d5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    place_id = uuid4()
    op.execute(
        f"""
    INSERT INTO places (id , title)
    VALUES
    ('{place_id}','Ижевск'),
    ('{uuid4()}','Казань'),
    ('{uuid4()}','Москва');
    """
    )
    kg_id = uuid4()
    upf_id = uuid4()
    op.execute(
        f"""
    INSERT INTO organizations (id , title)
    VALUES
    ('{uuid4()}','Восточный'),
    ('{kg_id}','Комос Групп'),
    ('{uuid4()}','Русская нива'),
    ('{uuid4()}','КОМОС ЛИЗИНГ '),
    ('{uuid4()}','ФТК'),
    ('{uuid4()}','МИЛКОМ'),
    ('{uuid4()}','КОМОС ИНФОРМ'),
    ('{upf_id}','УПФ');
    """
    )
    action_id = uuid4()
    op.execute(
        f"""
    INSERT INTO action_types (id , title)
    VALUES
    ('{uuid4()}','Грузчик'),
    ('{action_id}','Разнорабочий'),
    ('{uuid4()}','Водитель'),
    ('{uuid4()}','Разработчик');
    """
    )
    user_1 = uuid4()
    user_2 = uuid4()
    user_3 = uuid4()
    op.execute(
        f"""
        INSERT INTO users (id,login,email,hashed_password,is_active,full_name)
        VALUES
        ('{user_1}','manager', 'manager@mail.ru', '$2b$12$ItEZSkAxayiO7t.4cTNHsOKwKakTaPAYJ8m2qLgKPNd9k.1z0pWz2', TRUE, 'Менеджер Менеджер Менеджер'),
        ('{user_2}','user1', 'user1@mail.ru', '$2b$12$ItEZSkAxayiO7t.4cTNHsOKwKakTaPAYJ8m2qLgKPNd9k.1z0pWz2', TRUE, 'Иванов Сергей Александрович'),
        ('{user_3}','user2', 'user2@mail.ru', '$2b$12$ItEZSkAxayiO7t.4cTNHsOKwKakTaPAYJ8m2qLgKPNd9k.1z0pWz2', TRUE, 'Петрова Анна Викторовна');
        """
    )
    op.execute(
        f"""
            INSERT INTO manager_data (id, name,surname,patronymic, job_title, work_phone, organization, user_id)
            VALUES
            ('{uuid4()}','Менеджер', 'Менеджер', 'Менеджер', 'HR', '+79958751465', '{kg_id}', '{user_1}');
            """
    )
    op.execute(
        f"""
            INSERT INTO user_data (
                id,
                user_id,
                name,
                surname,
                patronymic,
                date_of_birth,
                phone_number,
                citizenship,
                city,
                passport_data,
                snils,
                medical_book,
                is_self_employed,
                work_experience,
                activity_type,
                contraindications,
                about,
                education,
                driver_license,
                languages
            )
            VALUES (
                '{uuid4()}',
                '{user_3}',
                'Петрова',
                'Анна',
                'Викторовна',
                '1990-01-01', 
                '79854758635',
                'Россия',
                'Москва',    
                '1234567890',
                '12345678900',
                TRUE,
                FALSE,
                '5 лет',
                'Разнорабочий',
                NULL,
                '',
                'Высшее',
                'B',     
                'Русский'
            ),
            (
                '{uuid4()}',
                '{user_2}',
                'Иванов',
                'Сергей',
                'Александрович',
                '2000-01-01', 
                '79865432154',
                'Россия',
                'Москва',    
                '1234567890',
                '12345678900',
                TRUE,
                FALSE,
                '5 лет',
                'Водитель',
                NULL,
                'О себе...',
                'Высшее',
                'B',     
                'Русский'
            );
        """
    )
    op.execute(
        f"""
            INSERT INTO user_rating (id, user_id, rated_by, rating_value, comment)
            VALUES
            ('{uuid4()}','{user_2}', '{user_1}', 4.0, NULL),
            ('{uuid4()}','{user_2}', '{user_1}', 5.0, NULL),
            ('{uuid4()}','{user_3}', '{user_1}', 5.0, NULL);
            """
    )
    op.execute(
        f"""
            INSERT INTO jobs (
                id,
                status_value,
                type_value,
                price,
                title,
                description,
                created_at,
                started_at,
                finished_at,
                action_type_id,
                city_id,
                job_location,
                is_active,
                organization_id,
                owner_id
            ) VALUES (
                '{uuid4()}',
                'DRAFT'::jobstatusschema,
                '{JobTypeSchema.HOURLY_PAY.name}'::jobtypeschema,
                400,
                'Оператор птицефабрик и механизированных ферм',
                'Отлов и погрузка птицы в транспортную тару ручным способом, перевод птицы из корпуса в корпус. Требования к квалификации - нет',
                CURRENT_TIMESTAMP,
                '2024-10-20',
                '2024-10-20',
                '{action_id}',
                '{place_id}',
                'Садовая, д.9',
                TRUE,
                '{upf_id}',
                '{user_1}'
            ),(
                '{uuid4()}',
                'DRAFT'::jobstatusschema,
                '{JobTypeSchema.HOURLY_PAY.name}'::jobtypeschema,
                300,
                'Обработчик птицы 4 разряда',
                'Выгрузка ящиков с птицей,навешивание птицы на конвейер убоя,загрузка пластиковых ящиков в контейнер,потрошение тушки. Требования к квалификации - нет
',
                CURRENT_TIMESTAMP,
                '2024-10-20',
                '2024-10-20',
                '{action_id}',
                '{place_id}',
                'Садовая, д.9',
                TRUE,
                '{upf_id}',
                '{user_1}'
            );
        """
    )


def downgrade() -> None:
    pass
