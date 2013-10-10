import time
import urllib
import urllib2
import json

URL_cam_1 = 'http://192.168.0.156/image.jpg'
URL_cam_2 = 'http://192.168.0.153/image.jpg'
URL_cam_3 = 'http://192.168.0.152/image.jpg'

URL_cams = [URL_cam_1, URL_cam_2, URL_cam_3]

def retrieve_images():
	on_request = urllib2.urlopen('http://127.0.0.1/lights/ALL/ON')
	on_response = on_request.read()
	if on_response == '200 OK':
		time.sleep(2)
		localtime = time.localtime()
		time_now = time.strftime("%Y%m%d%H%M%S", localtime)
		try:
			for cam_num, cam in enumerate(URL_cams):
				proxy_handler = urllib2.ProxyHandler({})
				opener = urllib2.build_opener(proxy_handler)
				urllib2.install_opener(opener)
				image_path = 'Incubator/static/egg_programmed_images/image_%s_%s.jpg' % (int(cam_num) + 1, time_now)
				with open(image_path,'wb') as f:
					f.write(urllib2.urlopen(cam.read())
					f.close()
			#im = cv2.imread("image.jpg")
		except:
			print "No connection!"
		off_request = urllib2.urlopen('http://127.0.0.1/lights/ALL/ON')
		#off_response = off_request.read()
		#while off_response != '200 O'

retrieve_images()