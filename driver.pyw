from win10toast import ToastNotifier
from find import getItems
from send import sendEmail

toaster = ToastNotifier()

while True:

	print("getting page...")

	items, categories = getItems()

	for i in range(len(items)):

		print("Page found! Posting notifications")

		mail = sendEmail(items[i].text, items[i]["href"], categories[i])

		toaster.show_toast("Found " + categories[i] + " for sale! \
		 Check your phone or /r/buildapcsales/new/ \
		 for more info", items[i].text)
