# Json Model

Month
```{
  "id" : "m202511",
  "month" :"2025-11",
  "categories": [
      { "categoryID" : "cat001", "progress":50}
      { "categoryID" : "cat002", "progress":50}
  ],
  "overallprogress" : 40  //weighted progress
}
```

Category: very limited number
```
{
  "id": "cat001",
  "name": "Cornoddity Art"
}
```

IdeaItem
```{
   "id": "id0001",
   "title": "zoda",
   "category":"cat001",
   "status" :"new",   //new, scheduled, completed, deleted
   "tags" : [ "a","b"],
   "priority": 'high',
   "createdat": "2025-11-10T10:05:00Z",
   "deadline": "2025-11-10T10:05:00Z",

}
```

ScheduleItem : once item can be scheduled for different months, repeatitive.
```{
   "id" : "sched001",
   "itemid" : "id0001",
   "month" : "202511",
   "progress" : 40,
   "category" : "cat001"
   "isrepeating" : false,
   "status" : "started"
   "assigneddate" : "2025-11-01T09:00:00Z",
   "deadline": "2025-11-20T23:59:00Z"
}
```

Set
```{
  "id": "set001",
  "name": "November Art Collection",
  "categoryId": "cat001",
  "month": "2025-11",
  "items": ["sched001", "sched002", "sched003"],
  "progress": 50,   // average of all items
  "createdAt": "2025-11-01T08:00:00Z"
}
```

FutureList
```{
  "id": "future001",
  "ideaId": "idea010",
  "plannedMonth": "2026-02",
  "categoryId": "cat001",
  "priority": "medium",
  "notes": "Do this after completing November Art set."
}
```

AchievementList
```{
  "id": "achv001",
  "itemId": "idea001",       // could also reference a set
  "setId": "set001",         // optional if completed as part of set
  "categoryId": "cat001",
  "completionDate": "2025-11-30T17:00:00Z",
  "repeatsNextMonth": false
}
```

### Relationship
- Category → IdeaItem (many ideas per category)
- IdeaItem → ScheduleItem (1 idea can have many scheduled occurrences)
- ScheduleItem → Set (many scheduled items can belong to one set)
- Set → MonthlyOverview (month progress aggregates set progress)
- ScheduleItem → Achievement (when completed, moves to achievements)
- IdeaItem → FutureListItem (store repeating or future-planned ideas)

### Rules
- Every ScheduleItem must belong to a month.
- A ScheduleItem can belong to a Set (optional).
- A Set always belongs to one month.

### Suggestions

- "month": "2025-11"   → this month  
- "month": "2025-12"   → next month  
- "month": null        → future (unscheduled)
