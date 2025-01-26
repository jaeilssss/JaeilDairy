from operator import and_
from sqlalchemy import Delete, and_, delete, update
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from src.repository.model.schedule.update_schedule_request_model import (
    UpdateScheduleRequestModel,
)
from src.common.enum.schedule_type_enum import ScheduleTypeEnum
from src.repository.model.schedule.find_all_schedule_request_model import (
    FindAllScheduleRequestModel,
)
from src.common.entity.schedule.schedule_model import Schedule
from src.repository.schedule.schedule_repository import ScheduleRepository
from sqlalchemy.ext.asyncio import AsyncSession


class ScheduleRepositoryImpl(ScheduleRepository):
    def __init__(self, session: AsyncSession):
        self.db = session

    async def create_schedule(self, schedule: Schedule):
        self.db.add(schedule)
        await self.db.commit()

    async def find_all_my_schedule(
        self, find_my_all_schedule: FindAllScheduleRequestModel
    ):
        # 기본 query 생성
        query = (
            select(Schedule)
            .where(
                and_(
                    Schedule.user_id == find_my_all_schedule.user_id,
                    Schedule.created_at >= find_my_all_schedule.start_date,
                    Schedule.created_at <= find_my_all_schedule.end_date,
                )
            )
            .options(selectinload(Schedule.user))
        )

        # 타입이 ALL이 아니면 type 필터 추가
        if find_my_all_schedule.type != ScheduleTypeEnum.ALL:
            query = query.where(Schedule.type == find_my_all_schedule.type)

        # 쿼리 실행
        result = await self.db.execute(query)
        print("여기 읽힘")
        return result.scalars().all()

    async def update_schedule(self, update_schedule: UpdateScheduleRequestModel):
        # 업데이트 쿼리 작성
        query = (
            update(Schedule)
            .where(
                and_(
                    Schedule.id == update_schedule.schedule_id,  # 특정 일정 ID
                    Schedule.user_id == update_schedule.user_id,  # 소유자 확인
                )
            )
            .values(**update_schedule.model_dump())  # 업데이트할 필드 값
            .execution_options(synchronize_session="fetch")  # 세션 동기화
        )

        await self.db.execute(query)
        await self.db.commit()

    async def delete_schedule_by_schedule_id_and_user_id(
        self, schedule_id: int, user_id: int
    ):
        # 삭제 쿼리 생성
        query = delete(Schedule).where(
            and_(
                Schedule.id == schedule_id,  # 특정 스케줄 ID
                Schedule.user_id == user_id,  # 해당 사용자 소유
            )
        )

        # 쿼리 실행
        result = await self.db.execute(query)

        # 변경 사항 커밋
        await self.db.commit()

        return result.rowcount > 0
