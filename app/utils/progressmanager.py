from datetime import datetime
from copy import deepcopy
from app.storage import db

from app.routes.achievements import add_achievement

class ProgressManager:
    """
    Central handler for progress updates.
    Use this in routes when tasks are added, removed, moved to set, or completed.
    """

    def __init__(self):
        pass

    def on_task_added(self, sched_item):
        # If task is attached to a set, recalc that set
        self._update_set_progress_for_task(sched_item)

    def on_task_removed(self, sched_item):
        self._update_set_progress_for_task(sched_item)

    def on_task_moved_to_set(self, sched_item, new_set_id):
        # assign setId and update both old/new set progress
        old_set_id = getattr(sched_item, "setId", None)
        sched_item.setId = new_set_id
        sched_item.updatedAt = datetime.utcnow()
        if old_set_id:
            self._recalc_set(old_set_id)
        self._recalc_set(new_set_id)

    def on_task_completed(self, sched_item):
        sched_item.completed = True
        sched_item.updatedAt = datetime.utcnow()
        # update set progress if in a set
        self._update_set_progress_for_task(sched_item)

        # Add achievement for the task if not already present
        if not any(a.itemId == sched_item.id for a in db.achievements_db):
            add_achievement(
                name=f"Completed Item {sched_item.itemId}",
                type="task",
                categoryId=None,
                month=sched_item.month,
                itemId=sched_item.id
            )

        # If the item repeats, generate the next month instance
        if getattr(sched_item, "repeat", False):
            self._generate_next_for_repeat(sched_item)

    def _update_set_progress_for_task(self, sched_item):
        if not getattr(sched_item, "setId", None):
            return
        self._recalc_set(sched_item.setId)

    def _recalc_set(self, set_id):
        s = next((x for x in db.sets_db if x.id == set_id), None)
        if not s:
            return
        # compute progress
        if not s.items:
            s.progress = 0
        else:
            completed_count = 0
            for sched_id in s.items:
                sch = next((x for x in db.schedule_db if x.id == sched_id), None)
                if sch and sch.completed:
                    completed_count += 1
            s.progress = int((completed_count / len(s.items)) * 100)
        s.updatedAt = datetime.utcnow()

        # if set complete, add achievement
        if s.progress == 100 and not any(a.setId == s.id for a in db.achievements_db):
            add_achievement(
                name=s.name,
                type="set",
                categoryId=s.categoryId,
                month=s.month,
                setId=s.id
            )

    def _generate_next_for_repeat(self, sched_item):
        if not sched_item.month:
            return
        try:
            year, mon = map(int, sched_item.month.split('-'))
        except Exception:
            return
        mon += 1
        if mon > 12:
            mon = 1
            year += 1
        new_sched = deepcopy(sched_item)
        new_sched.id = f"{sched_item.id}_next_{len(db.schedule_db)+1}"
        new_sched.month = f"{year}-{mon:02d}"
        new_sched.completed = False
        new_sched.createdAt = datetime.utcnow()
        new_sched.updatedAt = new_sched.createdAt
        db.schedule_db.append(new_sched)
