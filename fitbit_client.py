import fitbit
import datetime

#TODO: Save keys in a config file
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

#permanent OAuth keys
RES_KEY = ''
RES_SECRET = ''


if __name__ == '__main__':
  authd_client = fitbit.Fitbit(CONSUMER_KEY, CONSUMER_SECRET,
                               resource_owner_key=RES_KEY,
                               resource_owner_secret=RES_SECRET)
  fitbit_stats = authd_client.time_series('activities/steps',
                                          base_date=datetime.date.today(),
                                          period='1w')
  print 'Activities:'
  print fitbit_stats