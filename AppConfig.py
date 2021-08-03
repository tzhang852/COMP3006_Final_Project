import configparser

class AppConfig(object):

	def __init__(self):
		"""
			Constructs a new AppConfig instance and populates settings based on appsettings.ini first, then appsettings.development.ini
		"""
		read_config(self, "appsettings.development.ini")


def read_config(self, file):
	parser = configparser.SafeConfigParser()
	parser.read(file)

	self.Bucket = parser.get('AWS','AWS_S3_BUCKET')
	self.AccessKeyId = parser.get('AWS','AWS_ACCESS_KEY_ID')
	self.SecretAccessKey = parser.get('AWS','AWS_SECRET_ACCESS_KEY')
	self.Region = parser.get('AWS','AWS_REGION')
