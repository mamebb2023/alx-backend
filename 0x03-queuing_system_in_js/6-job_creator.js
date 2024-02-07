import kue from 'kue';

const queue = kue.createQueue();

const data = {
  phoneNumber: '251987654321',
  message: 'test the job creator',
};

const job = queue.create('push_notification_code', data)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

job.on('compelete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
