import kue from 'kue';

const queue = kue.createQueue();

const BLACKLIST_NUMBERS = [ '4153518780', '4153518781' ];

function sendNotification(phoneNumber, message, job, done) {
  let total = 2, pending = 2;
  let sendInterval = setInterval(() => {
    if (total - pending <= total / 2) {
      job.progress(total - pending, total);
    }
    if (BLACKLIST_NUMBERS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }
    if (total === pending) {
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    }
    --pending || done();
    pending || clearInterval(sendInterval);
  }, 1000);
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
