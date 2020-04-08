#! /usr/bin.env python

import requests
import sys
import json
import click
import os
import tabulate
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

SDWAN_IP = os.environ.get("SDWAN_IP")
SDWAN_USERNAME = os.environ.get("SDWAN_USERNAME")
SDWAN_PASSWORD = os.environ.get("SDWAN_PASSWORD")

if SDWAN_IP is None or SDWAN_USERNAME is None or SDWAN_PASSWORD is None:
	print("CISCO SDWAN details must be set via environment variables before running.")
	print(" export SDWAN_IP=10.10.30.190")
	print(" export SDWAN_USERNAME=admin")
	print(" export SDWAN_PASSWORD=admin")
	print("")
	exit("1")


class rest_api_lib:
	def __init__(self, vmanage_ip, username, password):
		self.vmanage_ip = vmanage_ip
		self.session = {}
		self.login(self.vmanage_ip, username, password)

	def login(self, vmanage_ip, username, password):
		"""Login to vmanage"""
		base_url_str = 'https://%s:8443/'%vmanage_ip

		login_action = 'j_security_check'

		#Format data for loginForm
		login_data = {'j_username' : username, 'j_password' : password}

		#Url for posting login data
		login_url = base_url_str + login_action

		sess = requests.session()
		#If the vmanage has a certifate signed by a trusted authority change verify to True
		login_reponse = sess.post(url=login_url, data=login_data, verify=False)

		if b'<html>' in login_reponse.content:
			print("Login Failed")
			sys.exit(0)

		self.session[vmanage_ip] = sess
	def get_request(self, mount_point):
		""" GET request """
		url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, mount_point)
		#print url
		response = self.session[self.vmanage_ip].get(url, verify=False)
		data = response.content
		return data

	def post_request(self, mount_point, payload, headers={'content-Type':'application/json'}):
		"""POST request """
		url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, mount_point)
		payload = json.dumps(payload)
		print(payload)

		response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
		data =response.json()
		return data

sdwanp = rest_api_lib(SDWAN_IP, SDWAN_USERNAME, SDWAN_PASSWORD)