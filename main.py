from dao.createTables import createTable
from dao.insertCompany import InsertCompany
from dao.insertJobListing import InsertJobListing
from dao.insertApplicant import InsertApplicant
from dao.insertJobApplicant import InsertJobApplication
from dao.getJobListings import GetJobListings
from dao.getCompanies import GetCompanies
from dao.getApplicants import GetApplicants
from dao.getJobApplications import GetApplicationsForJob
if __name__=="__main__":
    try:
        createTable()
        while True:
            print("Enter 1 to insert new company")
            print("Enter 2 to insert new job listing")
            print("Enter 3 to insert new applicant")
            print("Enter 4 to insert new applicant")
            print("Enter 5 to get all job listings")
            print("Enter 6 to get all Companies")
            print("Enter 7 to get all Applicants")
            print("Enter 8 to get all job applications")
            print("Enter 9 to exit")
            c=input("Enter choice: ")
            if c=="1":
                InsertCompany()
            elif c=="2":
                InsertJobListing()
            elif c=="3":
                InsertApplicant()
            elif c=="4":
                InsertJobApplication()
            elif c=="5":
                GetJobListings()
            elif c=="6":
                GetCompanies()
            elif c=="7":
                GetApplicants()
            elif c=="8":
                GetApplicationsForJob()       
            elif c=="9":
                break
            else:
                print("Invalid Choice")
    except Exception as e:
        print(f"An error has occured: {e}")