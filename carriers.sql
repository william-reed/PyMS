SELECT `carrier`      AS CARRIER,
       `email-to-sms` AS SMS_EMAIL,
       `email-to-mms` AS MMS_EMAIL
FROM   email2sms
WHERE  `requires login?` = ''
       AND `email-to-sms` != ''
       AND `status` != 'X'
       AND `country` = 'United States'
        OR `country` = 'Any'
ORDER  BY carrier;
