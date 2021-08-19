import configparser


def read_config(file):
    parser = configparser.ConfigParser()
    parser.read(file)

    bucket = parser.get('AWS', 'AWS_S3_BUCKET')
    accessKeyId = parser.get('AWS', 'AWS_ACCESS_KEY_ID')
    secretAccessKey = parser.get('AWS', 'AWS_SECRET_ACCESS_KEY')
    region = parser.get('AWS', 'AWS_REGION')

    return (bucket, accessKeyId, secretAccessKey, region)


class AppConfig:
    def __init__(self):
        """
            Constructs a new AppConfig instance and populates settings based on appsettings.ini first,
            then appsettings.development.ini
        """
        # self.read_config("appsettings.development.ini")
        # self.bucket, self.accessKeyId, self.secretAccessKey, self.region = self.read_config("appsettings.development.ini")
        self.bucket, self.accessKeyId, self.secretAccessKey, self.region = read_config("appsettings.devolpment.ini")
