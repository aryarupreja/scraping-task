import requests
from bs4 import BeautifulSoup
import pandas



url="https://www.oyorooms.com/hotels-in-bangalore/?page="

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

hotel_info=[]

for i in range(1,3):
	req=requests.get(url+str(i),headers=headers)
	soup=BeautifulSoup(req.content,'html5lib')

	all_hotels=soup.find_all('div',{"class":"hotelCardListing"})

	
	for hotel in all_hotels:
		hotel_name=hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
		hotel_add=hotel.find("span",{"itemprop":"streetAddress"}).text
		hotel_price=hotel.find("span",{"class":"listingPrice__finalPrice"}).text
		try:
			hotel_rating=hotel.find('span',{"class","hotelRating_ratingSummary"}).text
		except AttributeError:
			hotel_rating=None

		# parent_amenities_element=hotel.find("div",{"class":"amenityWrapper"})

		# amenitis=[]
		# for amenity in parent_amenities_element.find("div",{"class":"amenityWrapper__amenity"}):
		# 	amenitis.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())
		
		dict={"name":hotel_name,"address":hotel_add,"price":hotel_price,
			"rating":hotel_rating}


		hotel_info.append(dict)

df=pandas.DataFrame(hotel_info)
df.to_csv('oyo.csv')

	# print(hotel_name)
	# print(hotel_add)
	# print(hotel_price)
	# print(hotel_rating)
