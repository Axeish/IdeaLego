# API Layer 

| Entity      | EndPoint  | Method | Description |
|-------------|-----------|------|-------------|
| Category    | `/categories` | POST | Create new Category|
|             | `/categories` | GET  | Get list of all new categories|
| IdeaItem    | `/ideas`  | POST | create a new idea |
|             | `/ideas`  | Get  | Get all idea ( optionally by Catehory or status or month)|
|             | `/ideas/{id}` | PATCH | Update item or change deadline or soemthing|
| ScheduleItem	 | /schedule | 	POST|Schedule an idea for a month|
|             | /schedule	 | GET	 | List all scheduled items for a month |
|             | /schedule/{id}	 | PATCH |Update progress or move to set|
| Set	        | /sets	    | POST | 	Create a new set|
|             | /sets	    | GET	 |List sets by month|
|             | /sets/{id}	 | PATCH |	Update set progress|
| Month	      | /month/{month}	 | GET  | 	Get progress overview per month| 
| Achievement	 | /achievements | 	POST | Mark item/set as completed|
|             | /achievements | 	GET	 |View all achievements|


## API Request and response 

Create Category

POST /categories

Request

```
{
  "name": "Art",
  
}
```
Response
```
{
  "id": "cat001",
  "name": "Art",
  "createdAt": "2025-11-10T10:00:00Z"
}
```

### List All Categories

GET /categories

Response
```
[
  {
    "id": "cat001",
    "name": "Art",
  },
  {
    "id": "cat002",
    "name": "Gym",
  }
]
```

### Create Idea

POST /ideas

Request
```
{
  "title": "Make Scorpio Celestial Art",
  "description": "Create zodiac gay art with celestial theme.",
  "categoryId": "cat001",
  "priority": "high",
  "deadline": "2025-11-20T23:59:00Z",
  "isRepeating": false,

}
```
Response
```
{
  "id": "idea001",
  "title": "Make Scorpio Celestial Art",
  "status": "unscheduled",
  "categoryId": "cat001",
  "priority": "high",
  "deadline": "2025-11-20T23:59:00Z",
  "createdAt": "2025-11-10T10:05:00Z"
}
```

### List All Ideas
GET /ideas?status=unscheduled&categoryId=cat001

Response
```
[
  {
    "id": "idea001",
    "title": "Make Scorpio Celestial Art",
    "status": "unscheduled",
    "priority": "high",
    "deadline": "2025-11-20",
    "categoryId": "cat001"
  },
  {
    "id": "idea002",
    "title": "Make Sagittarius Poster",
    "status": "unscheduled",
    "priority": "medium",
    "categoryId": "cat001"
  }
]
```

### Update Idea

PATCH /ideas/{id}

Request

```
{
  "status": "scheduled",
  "month": "2025-11"
}
```
Response
```
{
  "id": "idea001",
  "status": "scheduled",
  "month": "2025-11",
  "updatedAt": "2025-11-10T11:00:00Z"
}
```

### Schedule an Idea
POST /schedule

Request


```
{
  "ideaId": "idea001",
  "month": "2025-11",
  "categoryId": "cat001",

}
```

Response

```
{
  "id": "sched001",
  "ideaId": "idea001",
  "month": "2025-11",
  "categoryId": "cat001",
  "subCategory": "Zodiac Collection",
  "progress": 0,
  "status": "planned",
  "assignedDate": "2025-11-10T11:15:00Z"
}
```

### Update Progress or Status

PATCH /schedule/{id}

Request
```
{
  "progress": 60,
  "status": "in-progress"
}
```

Response
```

{
  "id": "sched001",
  "progress": 60,
  "status": "in-progress",
  "updatedAt": "2025-11-12T08:00:00Z"
}
```

### List Scheduled Items by Month
GET /schedule?month=current

accepted value :
- month=current (auto-detect current month)
- month=next (next month)
- month=future (month=null)
- month=past (older than current)
- month=YYYY-MM (specific month)

Response

```
[
  {
    "id": "sched001",
    "ideaId": "idea001",
    "title": "Make Scorpio Celestial Art",
    "progress": 60,
    "status": "in-progress",
    "Month" : "2025-01" 
  }
]
```

### Create Set

POST /sets

Request
```
{
  "name": "November Zodiac Art Collection",
  "month": "2025-11",
  "categoryId": "cat001",
  "items": ["sched001", "sched002", "sched003"]
}
```

Response
```
{
  "id": "set001",
  "name": "November Zodiac Art Collection",
  "month": "2025-11",
  "categoryId": "cat001",
  "progress": 40,
  "items": ["sched001", "sched002", "sched003"]
}
```

### Update Set Progress

PATCH /sets/{id}

Request
```
{
  "progress": 70
}
```
Response
```
{
  "id": "set001",
  "progress": 70,
  "updatedAt": "2025-11-15T09:00:00Z"
}
```

### Get Monthly Overview

GET /month/{month}

Response
```
{
  "month": "2025-11",
  "categories": [
    {"categoryId": "cat001", "progress": 70},
    {"categoryId": "cat002", "progress": 40}
  ],
  "sets": [
    {"setId": "set001", "name": "November Zodiac Art Collection", "progress": 70}
  ],
  "overallProgress": 55
}
```

### Mark Item as Completed

POST /achievements

Request
```
{
  "itemId": "idea001",
  "setId": "set001",
  "categoryId": "cat001",
  "completionDate": "2025-11-30"
}
```
Response
```
{
  "id": "achv001",
  "itemId": "idea001",
  "setId": "set001",
  "completionDate": "2025-11-30",
  "message": "Item added to achievements."
}
```

### Get All Achievements

GET /achievements

Response
```
[
  {
    "id": "achv001",
    "itemId": "idea001",
    "title": "Make Scorpio Celestial Art",
    "categoryId": "cat001",
    "completionDate": "2025-11-30"
  }
]
```