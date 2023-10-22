import httpx
import asyncio


async def main():
    url = "http://localhost:8000/employees_gen"
    gender = "female"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params={"gender": gender})

    if response.status_code == 200:
        employees = response.json()
        for employee in employees:
            print(f"Name: {employee['name']}")
            print(f"Email: {employee['email']}")
            print(f"Age: {employee['age']}")
            print(f"Company: {employee['company']}")
            print(f"Join Date: {employee['join_date']}")
            print(f"Job Title: {employee['job_title']}")
            print(f"Gender: {employee['gender']}")
            print(f"Salary: {employee['salary']}")
            print("-----------------------------")
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")

asyncio.run(main())
