from datetime import date,datetime
import re
import sys
import inflect

def main():
    print(verify(input("Date of Birth:")))


def verify(str):
    #2005-12-09
    pattern = r"^(....)-(..|.)-(..|.)$"
    matches = re.search(pattern,str)
    if matches:
        year=int(matches.group(1))
        mon=int(matches.group(2))
        days=int(matches.group(3))
        if year <= datetime.now().year:
            if mon <= 12:
                if days <= 31:
                    return convert(year,mon,days)

                else:
                    sys.exit("Invalid date")

            else:
                sys.exit("Invalid month")

        else:
            sys.exit("invalid year")

    else:
        sys.exit("Invalid format")


def convert(year,mon,days):
     try:
        b_date=datetime(year,mon,days)
        b_date=b_date.date()
        t_date=date.today()
        time_dif= t_date - b_date
     except ValueError:
         sys.exit(f"{mon} month does not have {days} days")
     total_min = time_dif.total_seconds()/60
     total_min= round(total_min)
     p= inflect.engine()
     t_min= p.number_to_words(total_min)
     t_min=t_min.replace(" and "," ")
     return t_min.capitalize() + " minutes"



if __name__ == "__main__":
    main()
