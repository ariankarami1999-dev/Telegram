<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/I_6TyvfvTYFRLjeO_IAeJD6kmXInTEaLYe3gWzxJNfjeypcHlgEuszMclycf9z6FXpW5aDsll8OUUXAcvqAGNpS6ushpfhkOeKBEHMiK-0Ma86eQXDmtF3W-Dw0ZI0ZnSw6S4JR9jJkrjcEQvA9mB0cZLif1TcFF5Z2lAXI-KzfVqz7UBrmLersLyhRrsT7AlYrtdgKRBeQklk5On_Q6plgtXDaoX9CjhBkgvIpXK4yjabyBkHLvgjcMQ54Vkx8xvwFLvDVelLJCF_pzYpV6sYFPvkyQwJGTS8_Z-0BTXkG0quF8qmfrnFE_AurGYbGAhpByc-gamQ_pSy1n5mZb-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 490K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-30004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEq8TeofjxaLw294Yq-snDKMv8rI8vWJALxNsI86TdcnuFyhjHlmQRLkSGu1uxRVvd0UMVPYatN521Vvvir3FaeUrCu-NM3_zDdAR7JY46-4VRsG5JVkrekKmZwpKsA7wW8H3_oUF1SJq-m9L0M8_-310Oi-k0t8AXRLq0hcp1YphSFGH1ZqTreVVZmH_SVQ6qTyW2CHdhztDCql7V0gqjAQ1sHfI2HwwXdx_TQTVFmbK2wTAPX1S_X1Qf-7jcji5bBBqFMUtHjBcL96-q_2zJeiozFnaPDiZlBMgq4Za7XzKIxU_9Emtl9BFMNz8g7pPZJ60c_mlyCIICB6XmZmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/persiana_Soccer/30004" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3aujRsgqkh1-5Q6LTD6gpCmPLgzMTKXtlpdXGCpg2GwScvj69Vtzb5Y8neAWDw4It1khwfZz2q5tLRKYvv7l8T5Ek1d8G2myW9McTdd5cfz9Y-1Mh2WGP4yoLQaMcGQG6x7H4aeOfaXCpKotvzA7XW0w5vGaK1tUV2H28qBrxXb_MPD91TbIKJxLdET0LLg7aoKB-Jr0xAqq9clbZTxDTPmd4sffQrg9FPByNgacG2a6mowY04pi2OnF8bK3xQLv76Qn26gVVD4gqYI9ipM7u93cEwpmPx15VNN2uNgVC96MFVyI_qRWOuiueRvoqs4cpX1y0X0vazkCxEnHlLzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/30003" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULsq8TQz16i42KwR6RYOFSIIqr3huwHcuCVLG0f5yp15uyGY7hC66RHFmxBiYOaAJ2E3RLVJD6rmwIJpG2g__lNr2-7xzmMUdVRq9eMmgqnmgZtPFV3l9XOmxMPewfHKnIQ4CLCC9ZA0U6GTSSve3iuNBMDC_FaR1QeTNTtVEm6BdBLuSbWxC3OpYBOpEoH0WjcAby3SqzXIKb4z2HLImWC6LMeYvS_PbhxQGNDwfjKLxUrYhwWr4Dhu8gWHouJ13grDC5OPlJSxsswGP-zmfYRw-lG9vVIewXUcrRWbdvJDFilerelJiEntFXsre5o0ZFYoeBa58WcOZdj5oUAX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/30002" target="_blank">📅 15:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=m_WlzsXLQ_MNlb4As00ZG2-t3151Dewy4Yl8-JJoXJUzJM5Lyv-CJQ9YaxhZEg-M1cyrweCtHdrfBiH4-rkeV-zcajJgw0kteUjrAVU1TuGOp3sgoAh9KwQfOKp9OobiTdY6AY3UAhEb-RNQQfMdfy0rYIfqYGzxgWDUw9KPOCtnAo9ergHD0rmoon9lFPSimIXuH_yzieNbOgcA1u2FYQ6WBvXvjY8ohS1_GPH9bdZz3qrxeeQX4MF-m3jj8x70QmmLk6Kq1DaR249R_kEug16iX1kYimEzDnhNRI1rFW-OzOThKwuIKuApujVostAZJwxbS6-ZAGBAdTY6oChaLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=m_WlzsXLQ_MNlb4As00ZG2-t3151Dewy4Yl8-JJoXJUzJM5Lyv-CJQ9YaxhZEg-M1cyrweCtHdrfBiH4-rkeV-zcajJgw0kteUjrAVU1TuGOp3sgoAh9KwQfOKp9OobiTdY6AY3UAhEb-RNQQfMdfy0rYIfqYGzxgWDUw9KPOCtnAo9ergHD0rmoon9lFPSimIXuH_yzieNbOgcA1u2FYQ6WBvXvjY8ohS1_GPH9bdZz3qrxeeQX4MF-m3jj8x70QmmLk6Kq1DaR249R_kEug16iX1kYimEzDnhNRI1rFW-OzOThKwuIKuApujVostAZJwxbS6-ZAGBAdTY6oChaLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو ستاره‌برزیلی‌سابق رئال مادرید: حاضرم تمام پنج قهرمانیم تو چمپیونزلیگ رو بدم تا فقط یک قهرمانی جام جهانی با تیم ملی برزیل داشته باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/30001" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdLriqM2nkUmrTxhjSTdI5aJcEfh-sGV0BdpQgpxM4BMyLmHTATPNCihr1_j_8cJ5VqzepTt6RNNr-UPzp2-jXImT6PhpU7BrHz1PyPV2uKtiF1Z-4kV0Mw7si225i_uMKApTGyNfBAquFKwK8_fMTZRJDm9UtWo8-xtIj-uWMww7gFEQy6nz5qGXKIoAOhJ725hv-TxQ8m5vNa5MPzrYSsg7AnMUVSY1SadJbwnN9UQizq7Z9jKJ8Ul_gHfKQJNu45-2T7Imj5SRoFVb7Ce-yOJDLB0LK54tcOXCgBEqZ-6txidu1sPhDuy5jjqfueHDwXvkfZAVgjfuU5gYfXMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/30000" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVSUY8I3hLeIw9BQJiysmqwt9ojNEs5e4jp8C25nqcBxS1LtFrNjhQer3x3JnJt5BPijlPfKThVUPRqFrJGcjsNJIhO47nLmG1j0EXiCI3f4kL-4cm3e1rMQfNXtGQ8V4KvBCLoPYlkGXrBHLZwGUoJpWeeQik_1yqDB9OA8KVxPQUBwidCN7GGzVX04j4QjX5K56yvWTfx3F4WT6lZLVk4IkSfuAPoA7TNLQotDDji46Xuw5_xphlUBUU3P8uu1Fvl0x3y8-YSxk9ONZxBpeb-LiljZ6J5cL2Ybgnj919Y-q3iAz3fX_cUOm_2znlAsgWgkJqpNhBvLBDYIq7GSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
👤
عملکردفوق‌العاده درخشان تیم منچستر سیتی انزو مارسکا در فصل جدید در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/29999" target="_blank">📅 14:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfdssbuHzgS_pdB4TY1r18_vlSpLI8sQKGDapZfdO3ddNQV3euj4ZFypQ5LVU1z8_T5FNxxRfuv1xTFKH5lOqPe_js5ZQFP8GbH1XW3gKtCgWMhdvceRvdlXL6ySStYqkrF62yp1ulLV5peAbfulAjDjQqAok3t-GOKpwFtoIOArbjD7IrvF-M53lxEDbbGF33KbQosdgrwg9H_p6BgdBdX8XVuttMnMLlu5EOyu3eBFetmFR9WNckEyDV-Q7HEfj-HcYZyGbhO7Jmj-FyLRh14ba_N1y5-1B_d9j5Xh4Zb24ndR5p_kq2iCO67aNRekYnzDGcSipcUEG7uhTU306g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/29998" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=SOn8G8TmMARtsQ9jsTIgZGZDj5oCvjUgQD9KItl2NTLZG_y-slxFjbgUsOV6hpDa_QBYqkHPadCvgRcna3IgaiGZtXQs5rLvR9oF6Z9q4NTQWCbl7zJwgbL9aLyOhDx5Pp-V66x7qJ7YZgfd-EZgCLF1gRRMZCXiPtAhkqTJ2XokDbm7lwms7I6Ouc7w58ge5ABGVZWEbyT51vtq_Jcvo0TbChreBH02tyc3bV2UWtyx2AnCfWjVau2KEG-ihEAWYenK9g-jY0UPKiLgJcJ5drRnWmsHfCa6s0kEWJn0E2Gsq15hAqzIUH3yTVOABi4Y4l0ZjN8EisOQfLCz1lHxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=SOn8G8TmMARtsQ9jsTIgZGZDj5oCvjUgQD9KItl2NTLZG_y-slxFjbgUsOV6hpDa_QBYqkHPadCvgRcna3IgaiGZtXQs5rLvR9oF6Z9q4NTQWCbl7zJwgbL9aLyOhDx5Pp-V66x7qJ7YZgfd-EZgCLF1gRRMZCXiPtAhkqTJ2XokDbm7lwms7I6Ouc7w58ge5ABGVZWEbyT51vtq_Jcvo0TbChreBH02tyc3bV2UWtyx2AnCfWjVau2KEG-ihEAWYenK9g-jY0UPKiLgJcJ5drRnWmsHfCa6s0kEWJn0E2Gsq15hAqzIUH3yTVOABi4Y4l0ZjN8EisOQfLCz1lHxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ 15 سال پیش در چنین روزی؛
نانی ستاره پرتغالی منچستریونایتد این سوپرگل دیدنی رو در رقابت‌های لیگ جزیره به چلسی و پیتر چک زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/29997" target="_blank">📅 12:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf51IvkjXUEM2_62Zo9BDW3pRBmdWjXEPXK9iuvqS7qOatnRRCK50mY00D3dXkX0ZM03js1qy6_Z8mEek4nP8RwTc6-IHRWMZX19j0ix9VPmWihn0OQjVS2TNN3vFwqVGgiyEMXX6ZYd95iPbLZ1Ssbc6JYDRdFxRkyI2uERDs8_hlMC_4S3SNYTC_uUPrCmPT_plQujArhyZaCVMshc4g5GBWE4AVNkky0VPOlb3ezjboaCvBPw1P9YCxbAuU7ak8xMauF3FYNeiaoes92iNqn97RjoW9ETV0rtM8LYxULjb7rNzTn7Ns9mUh3OpmlO08hkuDU35DSHX0X8XJTXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب پشم ریزون و استثنایی فوق ستاره‌ هایی که همگی‌موافقت‌ خود را برای‌حضور در مسابقه خدا حافظی کارلوس توز از دنیای فوتبال اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/29996" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In_vWZCzBfLXZBJ33w3zrhqDy5ClgcGqG8Q71tBhSoV3Cs7kfAUG69KfsRUPZ09APFNJLwFFbzLNJ_1NCMSYl-8tGtq5sWbVo1-i4OmeZ-irKaRucSwAt-jtt-Np2isiJlK2dLgnGNaMz0s0fCJgwI4XTGOzTriig-jlVzfDX_-jMNFpZ_AEOlir2XfFAbWLBrxkkS_C9tUHegONdTuOAjCe982IcqWLnXnsTWwroxOitl2MdtU35IyxKEqpQicEM8dm-AUOSvGW-OTL2KT8pqs4MeuID2-FlLnmU3tg4TO2UQbibO9ok513RJJvx74Jd6hN48IG67CeojdlCpT0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/29995" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCiu8q5L2A9ODEnPaEG8KLmOgaq8VOMR06h6gsP2dOFRr593SbfYpCAM6s-wWtvmjXA9xA_FMmYPGnNDtfkCsx8BubxBeQp0J-EcVWH5rsl6px-5F1DNQS8Jqqa4Kc-8TrJSrM33RlY0YRKG-7fjJFWCnGCD-VWfB6byA8ZCt_p-hQ4F1ork2WSyluQ6wqoKprLBbFEwL8cecC3JCIyD4lUfohHsI5vRDJwj1Dtvzj3H2T0lfGsCzJDZFQm5uRp0OwyU0ULLQKGr6INCnMmAdtrV7_2KzA6AKQpQJOFWsXCXRX2kjqsyTbycip_VVsHkb7kNqf1pcmDfg6nAX1Kp9IGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCiu8q5L2A9ODEnPaEG8KLmOgaq8VOMR06h6gsP2dOFRr593SbfYpCAM6s-wWtvmjXA9xA_FMmYPGnNDtfkCsx8BubxBeQp0J-EcVWH5rsl6px-5F1DNQS8Jqqa4Kc-8TrJSrM33RlY0YRKG-7fjJFWCnGCD-VWfB6byA8ZCt_p-hQ4F1ork2WSyluQ6wqoKprLBbFEwL8cecC3JCIyD4lUfohHsI5vRDJwj1Dtvzj3H2T0lfGsCzJDZFQm5uRp0OwyU0ULLQKGr6INCnMmAdtrV7_2KzA6AKQpQJOFWsXCXRX2kjqsyTbycip_VVsHkb7kNqf1pcmDfg6nAX1Kp9IGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از کاشته های دو ضرب در محوطه جریمه حریفان؛ همه خراب کردند تا اینکه بالاخره یه نفره یه بهترین شکل مملکن دروازه رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/29994" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IenKI4Shd-7KNkvbHTlRWYGFRL6VGpUKb5ykXSXu8DnqtbDSBASUhxpWFcvPIaWUvtVyDVM64k-OcmBTNYfSowQVI1reorQXB7_ABeJfazaeawyzwY9wFmhuXelCgHpxnh2dfooyyG94NJkxbSxSyx1kGEWXBKg72oJHxqbUMlz_Jmyh5muRAGE-Ttq3c_pq1q4oIcTpUDJHTmyLyQhvGS13nIUTwzGJPIk28VL5zC9CjuazbvA2TbZPN-_wzXwQ6vhNW6TgzMLwb_iRx_xoMwr6KvlsWYIAN3wz79xKTlAbR8a3odOsDsXKiXvH0DFJwi0LEnTQdHSmi2nqGlAO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
جمعه‌های انفجاری در یک بت
💥
🔄
🤩
🤩
🤩
بانس کازینو مخصوص بازی‌های انفجاری در یک بت
💬
پشتیبانی آنلاین 24 ساعته
🔈
کاربران‌میتوانند درروزجمعه‌پس‌از هر بار شارژ حساب‌کاربری‌خودازپشتیبانی‌بانس
🤩
🤩
🤩
کازینو راتاسقف 30.000.000 ریال دریافت نمایند
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r27
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/29993" target="_blank">📅 12:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSJKqjDa4GXATE0dU7yEAksZ_O1Zo2Ky6PUt6u-IjpmvPCJRZkbEgjyvEYQwodXt_63tzcNpLqPMWCpw9mbk9glzjrCrCWnJfqaIYB1QLYrSQGx_pgL6j7-PcVLIF8yLzy9t2lOMrgzFA5UVrjf-0OgQ8AtQCHhEO1zNMo0cQ_n_VCdIMUAuzLll-SiNXzZ6UZ7B5Hxz1aBVUW74eN7KC59pjY_jIgPg2OhNhZSwlW_TS1mO6qmevoAJjbMhN8bDHLZzWShw5aKhErReIgiLN3vX9JnufwLmF_TrhD3OpGjvc79yGfzeJ5CQdjPlE3Hk0J-qLwPYpmP44J5_1zXeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/29992" target="_blank">📅 11:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zYhOdt_AdUQWpukLO7EDtooosS0s9om2gKy8xjl-P_XtyOJPuT1IpwxFKS4BHpESWTHW4MrhCNJO3aXlR712dq_T7HwdV4-VRWLuGaUQgZnexU9RsjibgGDWB6btb_rJZF-PiMn-XcQ08xZEPQlsfiUuVCNMQONmsuetxihel1MOBl-mKbpRf1DqAzC9tiau7k1h5P4ZVrB-eOX2dmByLbThAZ7S0_XxGwyam0bK7xMzI8uaK86DtyLzK4KWb37yOaF7Om2hYpOx2tyDGY2p1KmFyrL7RWyYd-wbP1MV6Ek8A_-3-F4He2F6pGDXgQhWfSPhSZp3XvyDUTBOMsTtpNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zYhOdt_AdUQWpukLO7EDtooosS0s9om2gKy8xjl-P_XtyOJPuT1IpwxFKS4BHpESWTHW4MrhCNJO3aXlR712dq_T7HwdV4-VRWLuGaUQgZnexU9RsjibgGDWB6btb_rJZF-PiMn-XcQ08xZEPQlsfiUuVCNMQONmsuetxihel1MOBl-mKbpRf1DqAzC9tiau7k1h5P4ZVrB-eOX2dmByLbThAZ7S0_XxGwyam0bK7xMzI8uaK86DtyLzK4KWb37yOaF7Om2hYpOx2tyDGY2p1KmFyrL7RWyYd-wbP1MV6Ek8A_-3-F4He2F6pGDXgQhWfSPhSZp3XvyDUTBOMsTtpNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دقیق و برگ‌ریزون عادل از پاداش 20 هزار دلاری مهدی تاج و دار و دسته‌ اش سر پیروزی شاگردان کی‌روش مقابل ولز درجام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/29991" target="_blank">📅 11:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29990">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiJiqAxcJ4s5jd3ksqDaprHbGljwlfYprp45Kybx-gnIdA-S6dd6tCzohGvBdCyZA7ZdAoT1vgtEtbzL_JrzLa55iVGIB-aSq4iIfW3AptZaoqg88E-IFFQPGtMn2LZyywhbVoHkgas92JLqfpDd5831EvH3dfcsFnEn0N1Qqkuq4xrownbNUU1pECOyPYU9GVTQW32TMbjK9db_9oFFOJQFWUBcGM1NQZs78ls6IHDL72fggG2AN7HwY1vmEURDm-JVBZpM5mXbmdvNfHc15nhpA1iG86XIj_j_FF2amxwvIlbHKMzJh5IHvaqefGEXtB_V9CLPAtbNsU4Bpu_7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور
🆚
رافینیا دیاز با پیراهن بارسلونا؛ رافینیا همین امسال به تعداد گل‌ های نیمار در کل دوران حضورش در بارسا میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/29990" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RosLnKfcyKB1Kl3yckG_RZMGGWHZfQt_95v0NRw3N3JW9F2oVomcIASPgsIHkUv_hl6rpJm0tz4spc3uYeYZEsRv-w6ciprcsKDB8zyhvzgM_4KBPcyIjzNQczABSsaQ5NntiZnsz03-89K14DXLvFrXaK-QWHYz_OEFDt9k-8AQVFUlB-9_UHTzCP6mgqd3dkj3GnB5NpmjWy55b4dEQyZuM_atKXfec0o1Mt3JNeuZcQ2WF_F9If1F8J7h91GTYkS_5bNLie0Nul7HkG4VYe5kBrWWW2U_aMTucgeHSVcJpvyu7Idiu08eogiWHqvmliw_I2YCjGO6v0pV_AwiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برترین‌گلزنان‌ پنج‌ لیگ معتبر اروپایی تا پایان رقابت‌های این‌هفته؛ رافینیا دیاز با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29989" target="_blank">📅 10:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKbls051N-w8up2YsRU7NGg0PN48LLhQe6RDAorDaInMBDKMb0AHI-d9JuztPf8O1KCPdba2wTZS4MEwJ7sN9uwQ8VnH7tbvg6vi3cBCmNGmnO3ddr6VkrPU3VSOu5iyUEdn9avfJX6c-8mwOlUvvVX2fq5BEuvityeAKs5Dv0lOMKk9_2ioEmwVoF8maFxC2XlqNrVlmkU0mzvrz15DuvzJOw-S9JjQCuVwS0_0p9-wlZ97rjSNhWmyJtLstH7yWGTCdoLouG-16_Jf04Yrlo6WW56RaowOh8lE8Wdxm1FCl4YftEZHD1d_ngqc8mUwa9lRlhRiOCNwmg2EKq30Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/29988" target="_blank">📅 10:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=rHVTBu55SiamxdJjhZzGSGqEwxr7mvPN10gJXFdItGyBX_5XrnmwieDvlbFxr9AvjDQj1owqYOXeHKEGd4ullyhzV1Yl3NaSNFw3mayCYLjOXsbW6Ed9PlBJC-pyT9mhQ3EXDx0STCo5aPTi_cxE-RgPbReiHnGDls1GpG_G2wxmNPrvdxt3iy7vVXeLjDkV4MA67GYGibtco5hl8qinYk-Z8QGHgAuBlKCXFlWNfKMiHbfJSSvz2sB_hAgw22VfGEPGPYQG2RnVphmzO0XzkziLwDmZIsSacmIcAqrXmKDdsy2OfPVHP_B1SxN8ZRGRTh_zQVhV_tZfQlKyY9GDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=rHVTBu55SiamxdJjhZzGSGqEwxr7mvPN10gJXFdItGyBX_5XrnmwieDvlbFxr9AvjDQj1owqYOXeHKEGd4ullyhzV1Yl3NaSNFw3mayCYLjOXsbW6Ed9PlBJC-pyT9mhQ3EXDx0STCo5aPTi_cxE-RgPbReiHnGDls1GpG_G2wxmNPrvdxt3iy7vVXeLjDkV4MA67GYGibtco5hl8qinYk-Z8QGHgAuBlKCXFlWNfKMiHbfJSSvz2sB_hAgw22VfGEPGPYQG2RnVphmzO0XzkziLwDmZIsSacmIcAqrXmKDdsy2OfPVHP_B1SxN8ZRGRTh_zQVhV_tZfQlKyY9GDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی مثبت 18 مجری‌صداسیما روی آنتن زنده؛ طبق آماربببنده‌های‌صداوسیما از سال گذشته تا کنون به یک دهم‌تبدیل‌شده. مثلا یه برنامه تلویزیونی زنده شاید روی هم50هزار ببننده‌داشته‌باشه تو ‌کل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29987" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a52708609.mp4?token=NCjdTpQXMGE5nr24SL3mbisuaFBVkA49pOjeuEzifxOu2csALJgILIS38pJoMC4o37ho4zR1HUhhr69AaV6YsiNRF9Sy9b1rFWJEeRdVzIzTRI3H8tnDLupNfr5DVWm3i7819SgoAbeGpqH6I9sc-8l7GE5UNQTQLq2t9IACjck6VnBPmJDDJ-11DrbZdV4ijm7D5cWZQZ3KoDm8XDO_jjmDzdVa5PZUSbHarBsQyc7iPc9flRW0t0ljmAzmOgRbdzqwG3KkDh5_dIfuK2Ny9EtEIFU-J8GsWkqATkNSXyvcTvEKZoffxK0zBQbKvSWD4vfewZ5vF1fVQgttOUWP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a52708609.mp4?token=NCjdTpQXMGE5nr24SL3mbisuaFBVkA49pOjeuEzifxOu2csALJgILIS38pJoMC4o37ho4zR1HUhhr69AaV6YsiNRF9Sy9b1rFWJEeRdVzIzTRI3H8tnDLupNfr5DVWm3i7819SgoAbeGpqH6I9sc-8l7GE5UNQTQLq2t9IACjck6VnBPmJDDJ-11DrbZdV4ijm7D5cWZQZ3KoDm8XDO_jjmDzdVa5PZUSbHarBsQyc7iPc9flRW0t0ljmAzmOgRbdzqwG3KkDh5_dIfuK2Ny9EtEIFU-J8GsWkqATkNSXyvcTvEKZoffxK0zBQbKvSWD4vfewZ5vF1fVQgttOUWP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
محمدجوادحسین‌نژاد که جدایی‌اش از ماخاچ قلعه در نیم‌فصل قطعی شده امشب از نیمه دوم برای تیمش به میدان رفت و با اینکه بازی رو سه بر یک واگذار کردند نمره خوب 7.0 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29985" target="_blank">📅 09:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxSFqyW3FpK2kNjPMH1KpopUQtC_YOXIDGKdlWEDAn9qQWmVsNXILvM6LcHPSwZA2PC4w3r3qrSJi0nmr2HWifqO2sGHJHF7DVn9TTUwtYkzwbrkOTXC6wHDJyiNUfZMLU9iwMmPn-wTx7S8hNqV-50D2vQmlA33N7xgdZezeJ3ZpHzH59sHB8gOl989RCGBxuc1SL9gTT6YXQ5PXvX6QowZccFXmwv4bnCSsN8a8202R3xcJfsAYuDoIJdXe8lQRa1owOdHprmoi5GkGX1Z4BUsu8QnWupAGK5vaFB9wQl94auX7qg81BQe0OezZMhoM-kz2XIBqJtcTUgXScVbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امباپه‌ستاره‌رئال:
اگه‌میتونستم یه بازیکن رو به رئال مادرید بیارم کریس رونالدو رو میاوردم. او در این سن هم میتونه موثر بازی کنه. اگه به رئال مادرید برگرده قطعا میتونیم یه زوج خطرناک تشکیل بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29984" target="_blank">📅 01:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzmfOV8bY5vW40rqrjO-5I_Gos8FEcVL9uKs_tjFGRRllp-31QhfKuAgV7GA0RFteWsN0bc2UZ2HLtRkL5j2c12cqtqyWLCBKVCFXQ6M69eT21MfQ6odTGJrDNmgHhLtNINKSf5h8NAneB0njjEHrf-TSvC_98mj9u0yLGq5W6pfSRYlY1grbRulwnrj6ENtmtyqcmGUQwoRfHFvsycTpE07vHoWdOj21D_H_Q8HMxb9TDFyyonEpbztWJs74VcFCc6ZzJAxm2hXIDLqCDXK9GkLftvIP8buu7I0ZkcQv0vWwLK36R3gK3WQ-1KsbfInWKdiGqNXycQ9d5X2imSRIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29983" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29981">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXBL_IUrCDnx10h2Y5JlyKyU9D8kd8HBAsq5lUSyRAzBkrmZnJ3t3oKvQKpcIP2U3oCYNZ90IcrjfPTC7UO2Q9sySHftX_SiAv1gJsvZryoP0maQontbn-oH49_lE91vd23lOMqDexJgIpmhDqknszvhx--vJRZDPphqS77IxBKSKBEmto0P-vMu0ulr62ZATaokIu7l0bx0Hk2dwY0DxrHmzgRkZSiwK5-osx5jRgL4m1pv1hAFwtc6opWZib_zW3qS1TzYgS1NjEZdqs7upTegSBWVdofb-dgw9S8SXYvG85nsAM9-4HqZaZweSHCCRmx5A907tynALMm0sk768Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛جدال آلونسو و شاگردانش با برنتفورد برای بازگشت به کورس صدرنشینی لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29981" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29980">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw3LnjSjexzwVG1GQTVslvDCtLsmLLVHMWo5K2v3ktk38CGPIqs4vwRXFXiEgxShVRpEF4O_2CGMcmkdymY8ZIXcVBfNHKa7GppvUKA6an2xuyDrCayfhZ04R91wvpj9T6X_jsvkTs9gCnSYMQsscpIekkC2DZ_sh1Q0pb1Cdo0Kl8o3ZJb3CGpucB8hK13QkKDBISWk20KfZXvxSgVKCRrfK-xcUV-N-R-lRndJcfzMiUu_bThrvb5gDmbfn6rPuFPSkXXwBny_oILV_XL2XV21z0sS0V_au9VEGf66h9yyxunT_hzpssIQfAMMxrdo9UoUCdH1vH7KIcxZ_xUKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازچهل‌‌نهمین‌قهرمانی مسی افسانه‌ای تا برد پرگل یاران اسپالتی در آغاز لیگ‌اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29980" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📊
عملکرد بازیکنان رئال‌مادرید درفصل‌جدید؛ امباپه با 8 گل‌زده و 2 پاس گل برترین بازبکن کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29978" target="_blank">📅 00:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29977">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8GIaB2KtyKqb5EKp2h5_GvplbkBLR7_RNY76XyjItYHotYlH71KSCy6UMK9qmwpLbmqW-hSYjgXfJ9VS9uilsCRBlh71Ammj_EGuu449xV69_RT563vFBuJ5MCKr6tevc4-vJy2PSR1pwFc4b1EfqzAVExIpsF7dFwZXX7cVvX6JRQz_E-MZ4ZhrfFV_hk9-6AQFrnxfvxVyBSsqr38WBqBblW5AyrkuF7bWXKDQNRtb8kCmrkKJuwe6DKuRAQfpgoaBJ-vlMRLkyuC10Gc6lfwXJ8alb3ZkIKdg6HBBjckKgH2VDE-bdYYtBLrqXn2oT_1_8JUmMhvyTE8mB4juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29977" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVjX750q9KeLL7PfDnn4GCRNL7MhcSobmFmxo-ITFMutZZvFVF-PPhAEvBjeOu10jH65OzwAXfMqEB6xI7PRzX6dvqFBaweKI5spItSFJykZ5oyazLlDROTFE4eDwsvQ_J3-oCEMy2r8A1LzjBC96hvbpWy6ElcM4w0fgQ-1oHMZZ-V34Krum49XePfqpg7kTq_0czjPcZHYHqPcr2ZYggAp2Do8nvsg1tJBT9ED2qyy3E6-mSKRZXOE0FHFUeN-wDX5eQdLnCIQLF4RWFQDo06xlP93UzdxFHDEm-ovWqXDzSGTBS_RPwgpHwWYJkKPZwFzYQq1xVAnPrWNBG4oKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29976" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGTkeCqEYVML6Es8klr-6asAnJc5snq_IrQJQNvqTxSZB-xIfnbL2MdTYwiHfJQI_VxGKL_8E9sYJ_8YU4rVPOmf22cpIkXhsD7lUx-R4OvmME4y8UjF2sSZY3-nHtrn-CFUtHzOruTF3f44hWKpPfOmLSAJxqGBbMyb4ndYFG-KEvUbSsHktQF0us5sPKtmF0_f0xRhOz6KiD58aSN4-ULpdBhuXjOT1mMW0-esV8e-nRs0nopuBc5xXB-TTs_ICrlZYukrxR6l_oY2U4UOxQTSr1mst53WXTvzQr_PPFIoZAWNHRLAsrgcDgaS9FNLOabL4kSseV5VkJAIxLvspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این پست برای رفقایی که بدنسازی کار میکنند؛
ویتامین‌ها و مکمل‌های‌مهم برای وررزشکاران در کنار یک تمرین خوب برای ساختن یک بدن حرفه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29975" target="_blank">📅 00:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPubMdc2m7P3qNULK0jN9-HuagsNko8tbQi3aT98TUS2LYumkjiHP9dlu5SrK6-p_d-ivPc6f8YO0AbWC1MEUKq4XXP-gi0w06vBKpylxziFjyQXAFHT6_ObXdGEt3LbqOaSO3ATYEXdtOsk7eN5Po1gbrq5VstTnVWxh_obczQUz8Go5flI_HvZ4d34btLsfhr-jiuPGV1AV69Xt8Tn6H3Fh7frQXBxpT7JyzEB-eD6PtaoJRZtLnr7j72M8qwDFpa365JBvwE1WtzdFg7TnEH2_lSnG9uauBZ6wf74VTYW5UnDgaI8uX-rF1qVF7TBd9_ESwbhStOM2z3wk6bPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29974" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ala6qJNumOgm7BvrXgwRyRr4pAX-qOC2iOAYBf2d9vk7YICpN9cz7sDfSZery9ShJubi881WGcqUY561kt3sreJRsP5utv8ApLUTFUf3wRB3VwQ38pwoKw21l8ev3wpBZ8ciPR0_JHJJSij0Z0rjHcqxEjin8NnhHqL1spSZ8Nn7ePn51e6WyAOyNY3K8dCK5GF4ENrVKD_gRZ1MS2DnvCt3nvbImTs7SEJbTi6vI-lmO0PgPP3AjCi1CdqHYfh1YXGx7qD0r1D5JY-jPwzVXb3i4umL8XYyEkPhAObZuIul_JnA-yPj8EeRU5yKBcctnNJSQzh8N8VWF7wbkNpC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN
: درصورتیکه‌هانسی‌فلیک امسال تیم بارسلونا رو به‌قهرمانی لیگ قهرمانان اروپا برسونه لاپورتا قراردادش رو سه ساله دیگر تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29973" target="_blank">📅 23:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8Zd2aKCp6HtWRs_Gj0JaEhzsftX2ev5A0N-UHEZRis5cyJ7McAozkFRWT8juvGHwhB5xr8We4CdEPHsRb72XA8etEIlJeUTu-lVsp8uzaGlI3L3wBMN1r2i9U4l1Nvhoc7t8RsnkRXJMFfmY9TiF7r2uegvjVCud4PK1YlDLTkt8OvmpAQTkedN3vuPsBQy5uxFG5WQ3ocKI1qS2uy0N7DM0BzBKcjuuRaBQrPGwO8_2EHPIaZDPsKS7WCSs8G9HwvpaTh5Gnt8CTCJrx4285GVf2ecOKgiWH7gpYFp7B8D_MA-bkeSkMq1pVxug0A2aawmZM9fygQ0AWVDJ_QDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29972" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB4Afa2ED13-pue830vGAX40wBga6z8us0GtWlz1yj00hz19lomv5Pyu3mx6xjL7UzifdMvkcxeUcSbX-BgBzTvT2rHbtf3cy0QgBHaNum8dTjYdwjptICIGdgfHvDmMi1YQbrNzVxAhoEuQaDuOnhDEFj6GpTscMLK-WzKoN5wN3oH9J5rY6TnUbejChq7n69E4kyTFJHyWrt8WnTZ02gf1RTct85teOQOYjLv8KjphJrYSDc2jQs25qDa1L6e-Rk6jddN8YqulKj1mDAMwdmUUBwedBAJNmc3KZoDj7OH9ucUyG4l1wZ8Ta8u6s-JwsBgAuyOGikufyIhW5YF-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29971" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPH9wkPP6OPuXqLdeYB3fuWS3-qx_VLjbFUktcrOyuSJMwKbzNi3b1s8NOiKyXcJnPtOr_nf9Sgfvg0QqgiSraHOR7FIt800FcIzq5tH_g_NzNi_DoLvUkLUv9Mj9CfpJ5ZRu8nm2xrMKDYOW1hRuD595wdhBNukVUI_kXtHy6OWMPCOTemiaZ88deXYYf_MtaGimpUWfFesGjRNzjpMmjEDF9ER-LaINAGP1c_RBLxi3b9pUedKpnivzeScwq1OZUHGo1K4M2p6PhadPl8tKtV5Iuq1aFUGLTCWF2FekkkWReVffGzNJn5HdfCpRjzp_nf_qJlqh2eCnt3cVw89IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29970" target="_blank">📅 22:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=OPMqhgXKFz-l5_p1MmsK-FjEFfk6HhekFl4NS-bI8V37pLTV_DJYB4atTI3VZwvrpX2YXSBMGGZOW0t1-tmCDLS8NQCdRmUwJfd5nXnfzi1RwiVyXhXG4wA92_7Fxn8iprELaZJGMB3hJucinxAp4I0JUsUjC3eEWXTGEkFY24gCPs5ZhWoqRKjC7ynWK78-SCPmbcRdp9cTFM8SCfn-YHO-vXQtkGQ9731sFixkJbmw8wFDmbJsef3jzCbKhkEBPQz0F4BSR7b0_FIi0JpzuhhIvhB3BCTAEjF0uYR2wWqd1jFTYzeUPz3LH6HEKI-t7xqqkQPjh-eXFrwZEzK_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=OPMqhgXKFz-l5_p1MmsK-FjEFfk6HhekFl4NS-bI8V37pLTV_DJYB4atTI3VZwvrpX2YXSBMGGZOW0t1-tmCDLS8NQCdRmUwJfd5nXnfzi1RwiVyXhXG4wA92_7Fxn8iprELaZJGMB3hJucinxAp4I0JUsUjC3eEWXTGEkFY24gCPs5ZhWoqRKjC7ynWK78-SCPmbcRdp9cTFM8SCfn-YHO-vXQtkGQ9731sFixkJbmw8wFDmbJsef3jzCbKhkEBPQz0F4BSR7b0_FIi0JpzuhhIvhB3BCTAEjF0uYR2wWqd1jFTYzeUPz3LH6HEKI-t7xqqkQPjh-eXFrwZEzK_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29969" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=ozEdJVPpnepuYghHzUIvHyGB7pfMJtbnG8rKQQ7NWmx3YRPh4FGi4E8vfcAesfU6uRldAWzJvTRY3H499NGBO8L_b8ogOOA1OvXky3zYG6_th7jwb2G2tzJgeAdGcI9bpOJIS8HyNNiFTdabCICN5hyoruANpjkWObZ8bU5dwsju2SDgL_Oe0usWyfv9bdTczyKQIg5-OOihgzAsTnJO5BSEj88-CYMF1JWair2oRJfTlJDMAv97iRCtet5Sx4GGlMQxo2jBXQ8lVA-vqL-rhP7LjQnimX1OLk8cnkX2lrf0rbGJSMu98TLVQBathiRjLP142Pz_zCTw_QKrpN0SiYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=ozEdJVPpnepuYghHzUIvHyGB7pfMJtbnG8rKQQ7NWmx3YRPh4FGi4E8vfcAesfU6uRldAWzJvTRY3H499NGBO8L_b8ogOOA1OvXky3zYG6_th7jwb2G2tzJgeAdGcI9bpOJIS8HyNNiFTdabCICN5hyoruANpjkWObZ8bU5dwsju2SDgL_Oe0usWyfv9bdTczyKQIg5-OOihgzAsTnJO5BSEj88-CYMF1JWair2oRJfTlJDMAv97iRCtet5Sx4GGlMQxo2jBXQ8lVA-vqL-rhP7LjQnimX1OLk8cnkX2lrf0rbGJSMu98TLVQBathiRjLP142Pz_zCTw_QKrpN0SiYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌انگیز و نوستالژی از تکنیک برگ ریزون نیمارجونیور در دوران حضورش در بارسلونا. اونقدر خفن بود این پسر ویدیوهاش تموم نمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29968" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29966">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX3xfYtVFI_VIdEOxjIJw8qsJgi5mzYq-5HrYLmjjLLRS6PcX8HWRT63XdQphlcyoCr5qL_OTj4YTZuQ_tf9KVvhjZcrFVkGQFNVnKxxK_ubA6UMQwJnHGvEOiDMI6uPwCcBr9DImkChgFY9QKbmyCtmOCxKhMEA4bVFg3bGBfe2s4bBS2SyV23eC1KLxTHfuv3bra9BzVW1xu-OScbzVkc7wuuY_lpjOc1VCxnEbrh-r2ugAsu-a1JwWzoX3Ep9pIAcJJo0-n4ihq_bcZBKtzmcEHu4x1JbjM5fbVUVy1aHBjJWavo2qN-8LEUV2l8V03ySMN3PDSDCobVgp5aOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29966" target="_blank">📅 22:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29965">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKmd0x3SvhpvfZU3XMArG8DLcRXaon2CeJ3RqmUkhbdr-yFsOdvtFpW8iZkZmth6haPrZM2DE5VJx4SUvn7zKEP5VlN17Nc7Wkaa3G6Zl60BewoWFfqiPnORNurGkGPCZDZST_aRJAs2pC6cKH5v7i0Zw_yrRe7b_y7MJ2irlBRxAYXZCStxahVniGpgQ3fS-haWacd7gYc9fc3s9gBaooHlSByg1A53OlSegiBP6S7l4N-yxW4K3JO56zA8sVepX2oqTgp0fpsp53Qt6B6C-UvkGVWUm97sdcMbCPwbeNFHZ4HaBDjacCt6ESySgw82PT27OyIVfb5KsCRPSsrAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک‌تعدادقهرمانی‌ستاره‌هایی‌که‌بیشترین تعداد جام رو در کل دوران حرفه‌ایشون بدست آورده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29965" target="_blank">📅 21:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29964">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojt9KO6jkgZXp1S-wlQCBPALBXr5ayh4Zjztbl-A0E6KJnY19ML3w96KQhbp5UZ4oq3h-ymdkeMSZPUgteLOQRHxYXJhBFNCQY2dk0vjt5he6y7b_2Y7BVK8YboCJ8Vu2krOZbHC_ujex10iVlc7bdECP31IdFmXwOMCDGRDsO7hv0TDmGIVoRY8rMC02lEXvRvwXWhehcGxL50lAS9SBC_fgli6DZ5har__NQTZMlOpx-rLuNv6rlMw2AzuGDK7Foamap7SG9p8pIBp-BFqceCEsqAGue24rrFFp-WDZ7eRyy9nJuExrjm3N3PZu-mjc8xcZGr37zOtV5IMD3w81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29964" target="_blank">📅 21:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29963">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_QerDCJn-JNhONgvGs4AS0Y3JaB9zsr62aTqNSwp3OEZJJKauB_05hZeqiOZqfWMJxUs3cT6ui1TCxmbpmPG7R79qO-nm_gXWKhIAvCR62dnsQa5kiG-KTDTd3CPRp3WKRVU5Rp0KUH2KY2twedJ89bXYe__fRExVaBNt-QXLIwuX92D8dw18SPCNTAVrgtXLIAgrq0DLrHG_--0nrSl22NFBgRgm72IypjHlcbbI2X_xq-O62AtyMe6iN0xCFeG711_-SskGGI2RSEoCnzw6ExIykIsMRNpPNuMMiX1huonJDV8-4a6waIhGiVV268wCYxDMWUCzKEJEOYpfajyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضا بیرانوند دروازه‌بان ملی‌پوش تراکتور قبل از اعزام به خدمت از تیم تراکتور آفر تمدید قرار داد سه ساله‌دریافتی‌کرده. درصورتیکه بیرو به‌این آفر پاسخ منفی بدهد بعداز خدمت بازیکن آزاد به حساب خواهد آمد و به هر تیمی که بخواهد میتواند برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29963" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbMknA5fmDlBuIWZYfbN1S-nDR2ijNZEVv_Qc0G4nKbjdeulIUilWx7g225bxKl5EMZb2KB_NYY8rcUOv3-1PJGu7ofv49q2LW4AIE1hgSIcoYGCMtz5obRtxxGnJLtNUFM2ys1Y3PO8LpIgrv1AFleD9qhTpBqqL3DYu2sdKwUPBc5QwiGDlaB4KfTc_2Rwy6fk8Hdj7RggeRNWH4jkHumy5QI3DQyMGEV2a5ydbs7Ayu12zS0UTc83y0DczTwG8PAlu29AhPVsOMqPdVYRja07E9MUyECHsszlRDgOuNJ-9ILyOc_nXC7dh4PGVkOqIIdbtsl68kLFezkg57Alfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛ ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29962" target="_blank">📅 20:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2ioLJxJkeYuCdbAMwV23D0qG-SaOHdn3dhAzehkRdPqxYmsjWGCn91K8Mhz-bFSRrSaFWVv24nQay2goO_Jn6toFoxcEXWcCBy7gocv4krK8meGdqLkBVUd9GgmFAUHjPd8Gd33L9bbg7s1eA48jRKdN2Y8DZyk_KmBAnV4wdtTyvQLUC0jlIbI23jIJ2oljzSLFdTUHZZfpv0BlGdWHtrhOJh8h1SuvJmBkHGmsM_MQ85dXgcx5cG-JUFNNEBEkShEXy9PyMQ8mHM1bfEVRljYdrmVseCNeShJNebhmzYzc59hpasT-mLHqZC6E2TjpfforY6qqX60vVUUhTNjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگهداری درست از کنسول بازی، عمرش رو بیشتر می‌کنه! اگه داری این‌نکات رو رعایت کن و قدرش رو بدون. الان‌شده‌حدود 300 تومن. دوهفته‌دیگه 400.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29961" target="_blank">📅 20:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29960">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE8pGjYjoRoyxRF5dwouWCHZodhHU2rzXXp9DFWzWyOVLLMxCtIukKjKwWBjYcKbgHf7hIKJtVxrSsLHFpLsbSHCU6PcJFusghswtWBMwTf0VY6LrdjV65IfVsILlFigXYkAecUJbnoMweYYuVaAEKmXpyMoiSCY6xwX5C-MG-O4PlUbLCU3aq6E76f1fAPSBu8P9S5zvZLTH9JTYYCR-v5nk7ZTMRLCrXHUWeD998PeB4bmpBSIfUpYcZiUMGQBUttCQS6tLgQyZrvHMF4oE3b4pd77NdfkiPsD2xJeRP8QWnNXRrBx3Fsw8vtYGbNQCe0ync34gkQwrTLnoAyR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29960" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29959">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef9E8x8eO3sMToBkoANjo-aROECWV6C2XqDWUnHfdF3b2WvtHjUnbEekoZIq4BpbBLcGXbFm0WoAgH-8gbmUrbCf2D3o3oDC1hPvh-1iAoiVvWvZSirU01lAwEFP_WnsiAiRqk2HMVexKHblms7JtqmHoZvYdxzcHAH0IhL3ltpZNvdnQFK1HAIbWklB7kmYKBEG6SV1ukH14XUwRz-siEhy0kY7K2Gh2Fy9MLd-60nnGwqwk0F-rr290hKgvKvEpczVi1iBt5NEgRnspOz1M-sReVJxb2fUN2cAkgyOPiSu1ktRISLBRWcvRQ3fZFR9tf69BGXwSx-BgOwEY5Qazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بازیکنان رکوردار بیشترین تعداد جام در کل دوران‌حرفه‌ایشون؛ لیونل مسی با 49 جام بااختلاف پر افتخار ترین بازیکنان تاریخ مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29959" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29958">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAemwGuvWj_CXVzEEWBrVqRHshD8vHgniOQ3Ohf8l8YgLYUJZgGE7uuv-zgOrSMxb0CSPoPVvSgxlSMNTQAY4_MrMVKENLL5w6GsLDo-O5bETK-Z68yjP91T_3bNuN3rnGgfoyT5ran6EHd7fZAHSWa9XB2ySaWyFjdI9kG0oqCuXJZkE7ySDXK1jtfmyATBa_pW4OXs93AofBM58cUipT5mgYVC1ibim2CZQKRAC1CvB-wCplb_LWa3oDRb3NljSPVUEFqISk5RKy-sXr5TVd1IWGUH_uAJTBcn3bFQTpI_ohkfPE9soNsUCqXsMbmCknq-ZCK92ObzmJcqqygEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29958" target="_blank">📅 19:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq8sTzu4nfdXI2UXYHGxOKN5nT30zLrYfVTmSqvPaavmAJDmag3M8NWCJSZFiTp2ynkdaGhfBjGsiVmcB9fdyNFDar6d2301LmxEgJ61VuMJZKI3ywbTi-fjRnT1DOYgM5AkIT-BxAUybM54y_NUJpvpb87IrTjZ5o0L8wQp2j3EMzGsOHjbY468xVuFjYBLKJQBs-Rjct1qE9jJpMHy64wa9oXLHQozLW08bQpoa0OGJggH2oqmyukz9I-rlOybTTTqmCLlkMllu-rvwOhPYxIyGHuTcjbYwOGozoNboVDFlqp_MilaerhgV0seefuG26jhVNaB9HyI21ZJzCe-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس میخواد درپایان جام ملت‌های آسیا برانکو ایوانکوویچ‌سرمربی‌سابق سرخپوشان روبعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29957" target="_blank">📅 19:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4vfa0Fk2gjRD464R_eZI4Fc6MUp8wBN4iHqmTK7LDZ6560ikkmmQSXDFgz3Hd3Gcl5YVkxPlmaT7F3aX0a73tNyIwa8wdCs22eJKvl1y0czDgVL6Hg-V2QKQCZyT5Ly7mbRsnU_CKn7tOf3R_bEOlNcOCxfvPtD1iASaWZr_mbd-ry9rLFaopQJvINgrTYJx2aHb4usjKMYdWqKUZWi9KITkhgjUa_k_Z89399DlHyWbUokCLKj2rXxg2rpVWrHTuhdp5XjjsW-2KuUmI-Fe7c86E0Wc6ovl4AZ_jMqPjjMuN1vqxjtFNIaOE6ANFDNUpksUH1wCBJ_ACAkjQVeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29956" target="_blank">📅 18:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29955">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-D0j7GjW67aBrTEG_vSGurbOQHsKGl4o8WI6p7HVdssjbFBxs05WB5xMI_6AYdM4YfdOpAZS-EpW8eMZ9mDjr00agxcMdzokceERKLjOycgEMwDaov1CVZVaqmcUXOJmSKXCYIupjL1CQB7_pJZMlZycxBs9ZY2GoEcA-pDs3hF9oJuC9FkEAyJVavuSY3FgE_mFdUY88Rl4gofTgAN6Pm9cbG5LOQCqm8YS4EUZ0zNa97iyR4EIGQMI8U87DgnUbD1al10QCtgtTObuy70kyMzE9U2HloJ6WKrIaWzkzjbn3HA_gj-8Q3-9PqeQWwgpSMErzffX0Edm673GrCQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ارزش باشگاه‌های لیگ برتر ایران براساس آخرین اپدیت سایت ترانسفر مارکت؛ پرسپولیس ارزشمند ترین تیم این فصل لیگ برتر ایران لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29955" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=l4LQvCHEPi-UtytybufBTczHEQfgm6XXmgfzImSulX3e-tBBQ8kuVh07O4T3PBgl3kA_vrRir07QNfYx-S6l5oknHFQDtQFWJoT1xYpXmGDq93CRpZgQOdGYVMLiIFvF2L8LYkb9mco6W2gp6-4CORxjMSjpaUFjhN4oTAjOXzHswPQVT361t3dftEuWUyCWSQdOUw195EhYdNJ6dp_EvDnYDTXfl9WX6-JAmXvKQtfS9vzueIs20IFUwbeL6pGmP7r3M_vxr10BVkaKKR3WSM2BuQ0LU5p4sba7_72H-9rAM3U_3JhEtRUkSOuB7Th1xuUacxfp7v7augWWDwSOCDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=l4LQvCHEPi-UtytybufBTczHEQfgm6XXmgfzImSulX3e-tBBQ8kuVh07O4T3PBgl3kA_vrRir07QNfYx-S6l5oknHFQDtQFWJoT1xYpXmGDq93CRpZgQOdGYVMLiIFvF2L8LYkb9mco6W2gp6-4CORxjMSjpaUFjhN4oTAjOXzHswPQVT361t3dftEuWUyCWSQdOUw195EhYdNJ6dp_EvDnYDTXfl9WX6-JAmXvKQtfS9vzueIs20IFUwbeL6pGmP7r3M_vxr10BVkaKKR3WSM2BuQ0LU5p4sba7_72H-9rAM3U_3JhEtRUkSOuB7Th1xuUacxfp7v7augWWDwSOCDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29954" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTxtxuZHLtjACiDXqOuHZoicg8mIUaOzRc66oOsjoNAfeIYbJBBrIwfy1sdFFpEoSjzYKKV09bNQiNJl7qJrEK0VXsh_8pLz8yQrQTtlD9GPAlHQZrtZzJ1Gh14GDge_BeQ7weGH3KwbD4uUxdBpGjIBn8vZa-9Du7ht-9XNYuTW1cmvXpuzJYWYK-ajbUE2Kv0XSs_tbcXtKCU3d-4N3043Znft-eoFyvQBfGFaor4ONaXzW_AaXY1_yq3BZ7EhmZ1Aw-hNz5DsA3FTdX8Xro0lcqvHlcCaG19YpFWaenCeeut08rYXJeQthvu4CtyfMa0wqLduutNLBURmtaJ6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
❗️
❗️
💥
چالش بزرگ پیش بینی
🤩
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🌟
از
🤩
🤩
تا
🤩
🤩
🤩
میلیون ریال جایزه برای پیش بینی های درست
📌
فقط کافیه در طول هفته 500هزارتومن واریزی داشته باشین وقبل از شروع مسابقات به
🤩
🤩
سوال پاسخ بدی با حداقل
🤩
پیش بینی درست شانس برنده شدن داری
🙂
🔜
نتایج برندگان حداکثر تا 48ساعت بعد از پایان مسابقات اعلام میشود.
👀
آماده ای شانس خودتو امتخان کنی
❓
🌐
لینک ورود به پین توتو
🤩
🔗
https://pintoto.xyz
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g25
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29953" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fItsuduR5kNv2AG_4MK-o62XLyRabhk0HIpkIJV7vzY1393KEBlHBq3RYSSarhqC22UufBCbD1nluWcDKcorxG8X1SvHDik7DWLGCFNZhFopKYJyN0uT9B_zNDdQ437OvOEE8yhVG4iXc3zKXk1e_yIcWcNG7dWMeVnnhtuqRDDyb841Wt_VmvRB7EHjzvtTq5IQdYhvAjk7hw5aVvXWnTFt_nNqTN76PiZUFXz1_WPjE6XKqSwk2NZ-0fZ5oLl1WihOxVm4l9oKBuD2Iu3Cc_vVAWTxjoZie_RMmbwuqG6PmPlFRCc8aAYy4Z1mTS44Rog_Y77Ps6to-v2OWFIQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29952" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHufio9rachCp_hRAvumICJwZkN2JP1e4rRdiG2M9_7zxcbJdPjMy8lHvAji6DheLFG6Hy1G1qURew897lmH_FdYLLqkMQcgXsinRNNHIkaWxLkj6JQrm5qs1t4IYeBbi3l4Yjj2sJjwgrY2eZhfZsbxfHYD3Gr62TIukUhsmiQXYEb9YjXEx1sQ3uVSBoxi4uIdjyE91BbCC9wvym9GN3mLtv1cvDYnQg2r65Fk5YMcL-MhYI7CLb9DKgejZnA9tQETOmSa_99Ix815fFeWStKldEd0J0kLjSsYvqGEEejPy8aeayAF1XUOmH_Q2L5whe44x5Gia6_eVw--Y25ewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌سوپرجام اسپانیا
؛ بارسلونا و اتلتیکو روز 13 بهمن‌ساعت 23:30 به مصاف هم میرند. روز بعد همون ساعت رئال باسوسیداد بازی میکنه. برنده این دوبازی مسابقه فینال سوپرکاپ رو برگزار میکنن که روز 17 بهمن ماه ساعت 23:30 برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29951" target="_blank">📅 18:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZM6h7Cjsdmn1Q0mGSRn0v1auGUfEzA0TSRxuAjBQ-davnbruCpqVwAb879rmO0TZ8Dk6YEXbXuO0cw49EhmTmv_9F9vcVeKR8x7PlY_mE0WXjvRN83YWHQlHrsDgOq4jcX8fD4lpXnqUlqmqdi89_Bszlrb8lr9_HCA5oQzha7cmQqtdvHDvIDdEwAMwVa1vcUVyUu8IsWR_S0hDV6-GywGv3htPwVLF5jg1UdS9ncl9ROhSYZxo7IUooS0watWfGf-1Rts5xc1L-5rkOSJIEyFEOY2fw7uo-36RtAaPYIiP76pszdlveSjV-jZe0dfmPdF4MtqgKJbFCZDtZqHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌پیگیری‌های‌خودراانجام داده و در تلاشه تا علیرضاجهانبخش رو نیم فصل به این تیم ببره. جهانبخش از اول دی ماه سرباز خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29950" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfN7zp2TstFfYhN2B_qZlaT1r2mPOaRQxV7tC_xPXrpgQ1WHWrvBW6yM5kfZr6D4FHgV-UuqdN3U_eYBQv-GZZlCI5QUeLWqBBS3c_ppAgxDZ5PNZ89TYcLMM3qk-TWolDcuEiL3obq5qdUlX27WpZ0kOaMPquuYHcFeOjGt6RezwZk4k4x9ETZWPSC09tQHGzPfQmdtaNHByUdPokmqZV0oz7aom3rFHpmXY30hYtKkHZLebuAnxcbrNyhZVi01FcUBs071rbnhZo9lpur-ZnhEIZnW9eGfYw_hofvZ3SC5-TPv3EbEXgWCUUNU73_B5YE-9p2oYp3sR2OPjPV-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29949" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjQH2w6UqlvXWXAaQbrg0zSYS9mb8D47du1FaTGaJnlgxwT7IirPON_r4t_wgLeLC6q26m_GUlxBrU0076Yvz_QVId0R5bUMzzanTcogCVCr1L9oWvPF0Fd4_btLaLQxvfKrnplEwBjDqDeRP1MG_J_MXV8CaG4ykb_AVQU8yI8GVBQPYADZhIV4ZGWg2ncL566W9a6DZLNk3aCdMDbhaEVlQABjPrx2zjRcZ8nwYY4YmN0p2hJlt1QCPGDpEm3m3aoFTc-diTyydfWrQ5KuZ6j775WV1C1Y6HQA9vmDSSYj73XA77lQuNrqXmDhrEtCqy7zv-eVX2KzvXPBYWtDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29948" target="_blank">📅 16:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moC9FlXrP6C7oasnBWxInr_zG30hLqB9Ji1_9xm2JC1avbuw-c9-r9V4k2m8o9DDNQ13-uwABxztNqqIjAs6n3LkiVeMytZSxSaPZNnPMGvaZYbnJAuRh_Eb5rUr7ilaEEjGAYbvSr4ZpmUsMTgGQERcOPj9ae-Vbb9Ym7dB2LnfcqV0c_54hMKN8hhuLsNEKNLlovKq3UiK8TVfh3Tk1XLuX8vZEYRElKAXdTpkHyYneKjxYJzC76ClfQT-K5lw0dwoOyX8AvTF5MrnW6t1r3s3IcgFOrO9rEbEPNNY3tRo4ccWr_NA1UU8jltpNsZW6MolxPEkxa0gYamy4L14DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29947" target="_blank">📅 16:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29946">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=qDfHWvu6FFgTuvQup2JAKkaCCbtF5xeTZkW64XTdbRUwPOCgCWMCHOgIStX8ZbTkD6qCAp8Dkpzta-9mJS6e6tI0hAV4xk8amBqQMLbVYPttlC51m09b2k3X_h-E_H3iVa80R2moZhNcOJ3gIfj-pEP7E0TbYRyxyQECQmJJrI58tfWfEdlGdDEesz-u3F298o_Ag3cpwOv_9J7suWy9GJtsGNpmC8jbHrgfDRnH9MLMN_eNkU1ZzMmfHG_IRqe5p8_bIahv9ypLtJUmSX2HvD8Xk68D7RuuQg8EW5x8lGVQ44nloXczrJ1OYsCwdDXHm3jz4BW3VGvsVGB7BvysjYEYb7MfizPIJc3K5KjGVPTeU1-7uH3Tnra8acB7gzsOLiS84DJk36hR528_EAbrYy_ZM31k37ybDPcupFVANLlUtgeH47bzxd1T-_pBsyPJUa0fGmGkcS6nraDqihNDjdcbW9_vO68gJxn16YufnMmwwngjMX3WKOiV4N2woM_Aym2aEgWuqeSl_r4GnMpyCvBm39Ucz6tP4b-EYg3ugVzKvhkajZ-E53T_g54iG4dGJVQJGPk-PrbjRZIbELG2KqJXge3Xxub0NfdbLrJuywVVy9ao9SZNNSnR2p8OMgAbz3K-T_F_D5IRpVfcgJ-BzFWja7fPGHdlwm7zWOOojXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=qDfHWvu6FFgTuvQup2JAKkaCCbtF5xeTZkW64XTdbRUwPOCgCWMCHOgIStX8ZbTkD6qCAp8Dkpzta-9mJS6e6tI0hAV4xk8amBqQMLbVYPttlC51m09b2k3X_h-E_H3iVa80R2moZhNcOJ3gIfj-pEP7E0TbYRyxyQECQmJJrI58tfWfEdlGdDEesz-u3F298o_Ag3cpwOv_9J7suWy9GJtsGNpmC8jbHrgfDRnH9MLMN_eNkU1ZzMmfHG_IRqe5p8_bIahv9ypLtJUmSX2HvD8Xk68D7RuuQg8EW5x8lGVQ44nloXczrJ1OYsCwdDXHm3jz4BW3VGvsVGB7BvysjYEYb7MfizPIJc3K5KjGVPTeU1-7uH3Tnra8acB7gzsOLiS84DJk36hR528_EAbrYy_ZM31k37ybDPcupFVANLlUtgeH47bzxd1T-_pBsyPJUa0fGmGkcS6nraDqihNDjdcbW9_vO68gJxn16YufnMmwwngjMX3WKOiV4N2woM_Aym2aEgWuqeSl_r4GnMpyCvBm39Ucz6tP4b-EYg3ugVzKvhkajZ-E53T_g54iG4dGJVQJGPk-PrbjRZIbELG2KqJXge3Xxub0NfdbLrJuywVVy9ao9SZNNSnR2p8OMgAbz3K-T_F_D5IRpVfcgJ-BzFWja7fPGHdlwm7zWOOojXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🔴
#تقویم؛ 8 سال پیش در چنین روزی؛ شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29946" target="_blank">📅 16:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29945">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vynW9-tPlQhnqznmQUrVrAgyfDqpESfSkCK9oYH0YOZIBDjeQ_fjjCf9REemz87zeiEIMfY5OCZ-6dtgHyHrzS0CRjcs3Wop6x2PntcD4mmrO3DeP0amzxxJCY1W4rrdeNNUP2jhHjuTDWMqrMwN6UAd5rUfUueyAjcqSwx7RWL2djmaORQqV9tYSGG6fIu0ULGJ5WouG7N-YZOclsU2MLUAbESn7AwlDAabS6juoVPEulV-ueiMaFpLfwoFJAGeAGA8pDLqMcYpITS_nCC7p5rly-uGDZW4jB2SVg5Zy4b3m6e0zwIDPPkhyQALjhJQ2H1Ft_R7JzeDr4Y13OUcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🔴
#تقویم
؛
8 سال پیش در چنین روزی؛
شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی لیگ قهرمانان را در آزادی پر از تماشاگر برپا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29945" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29944">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=gIFh9sJyjxuF26P2raTLQBvz2S5mKeqZiyJQDNid3RbavDZC6kVhuHe1B_JDrxX8sZmDcv_OXqE0La8zlDlbOM-x9KNmywrARa8s1vme75qgR5N3Ezvt74crTudBXn9UJ3Lh9QknDK2L3h_gRZBptrgT4OrFQTPM_BYYbUgKrYNR_l7uj41Si-R1sxcm911t2xSmkQh5IfIXg96XcdPz4ptmIvgFqulKT340_lOEb6v7ep7gVeysoKmbtQFgGSwmFGNL69OW1Uth9BufaSq0clh12Ep4zM9sInS9CJoPdXRsn8LBxeqmky082hXCBtSm-yZW7gLdDPRCrCaAhlW1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=gIFh9sJyjxuF26P2raTLQBvz2S5mKeqZiyJQDNid3RbavDZC6kVhuHe1B_JDrxX8sZmDcv_OXqE0La8zlDlbOM-x9KNmywrARa8s1vme75qgR5N3Ezvt74crTudBXn9UJ3Lh9QknDK2L3h_gRZBptrgT4OrFQTPM_BYYbUgKrYNR_l7uj41Si-R1sxcm911t2xSmkQh5IfIXg96XcdPz4ptmIvgFqulKT340_lOEb6v7ep7gVeysoKmbtQFgGSwmFGNL69OW1Uth9BufaSq0clh12Ep4zM9sInS9CJoPdXRsn8LBxeqmky082hXCBtSm-yZW7gLdDPRCrCaAhlW1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ خاطره‌‌انگیز و نوستالژی از سوپرگل‌های تماشایی و برگ‌ریزون کریس رونالدو در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29944" target="_blank">📅 15:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29943">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCbCBkPPeGGJ6ucOu0iTuN_zG4YLDkKn9Vib3jXiI_qr_uzj9hEwew9ssl9rMKPJn5xIgN_VYMiTMi26cJk42aOz0Z3D4d2tkYNsxV07zNMV-iVSeV5lJud8nw7pIFhtTxFjZbvfhqWjKZnXmEVzh5zpRoKKQ0-V3g8_QSebcPIHwgPj1CdrjLcYXDTmQ5g-NdzYz5WsAqsrrBAqtoO7WYo_TWxOwenX17xSecscTPhU9ZWyk1Mq4OeBKolyakCYAz4Bm18gf79wJy3bVK14tciTj1NRC8N0vzAiiOxlH4jSdoqTFt7en2P2M2eNPzwUU0fFdogh0ezqAi98qdY0UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29943" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29942">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpbZVJdz60pKVURwgemKpsgZciQLTe75YHDI6dyBa43sG0QPJRY8XE24LbpdJOCs1EH5fhR0PLaf25lbCLQ4S_nXLXZTau6agEkWY93aZkC0hZu32MMcoYhIaMX_GyTNYwStrd0MJTKK1kYHUPoKCdozYh7_3YsP4UTMrNyo-qCZ6aCfngSlMHdiQtHK3SPtcuTvXaaQaGT6vHDVIvluG0iV_AQZox5_cLguMg-VB_dR5rHw0NuLRGclUCPGoOucS3nHN0b4KduICuCYjN2bzHSjPmDCi1786ZJ2Mbvnp3VQp0WBNZf7EBoJZ22NEM3cQbZ7F5E-ISLKDUMEpwYIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
از 368 بازیکنی که در یورو 2004 بازی کرده اند 367 نفر بازنشست‌شده‌اند و تنها بازیکنی که هنوز هم پرقدرت ادامه میدهد، کریستیانو رونالدو است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29942" target="_blank">📅 14:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29941">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChiHDLHBP1utDKb2iXnvInk3bf0p3tF6jY7ddaBC--KsnSbdV5eFQhh_gPTXGbg1MH6xdUY7GHOCrET6UOQG6uuB0pZ5Azs89nnXtfwOrCS5m_PmSyqxdHrtLpKqyfByOxAil3J-vctDJDDzm-vWHLk0SHTNtyPOgXurFzGwvmiyDcUhBs3hTkH4vxkcjb9Q6soVwIfeuWZbNOKKBAwjjsWFTcUjWpHJDycdN5uVKAgI9K1p4TMxRGJ9S2LJJiklqiNqHk79odtLWRyVbRB4CYpcDJtbLID52xojbNd7sE4O8dQmPvZjM3TChgw8s6ehLNpOAb1BjGZMaMmGQeXIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
باشگاه‌پرسپولیس‌بزودی هزینه حق دادرسی که حدود 150 هزار دلاره به CAS پرداخت میکنه و پرونده یاسر آسانی رو به دادگاه عالی ورزش میبره!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29941" target="_blank">📅 13:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29940">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-aZONeE_3-3ja2FuoqvBDyXfeRCj8R0cbNeXFK5zf64edCDMuc7j_1oFMkxDdaKtcQajZ-dMj7m-569w7m2iO9mgZ-WDqz8bTLlBO2MhoTrwB2__QcAu9G78et45vifVLUDWi6u89As0sikc8NGsV3GymsILq0P0QGfVnnPsFjq5ivIeXBWfHy4boElOUGMZWdkPuI3wh1Umxw7LojbEc4F3P0uJffLrq-VhHRgbTx6iNXnXUjGUFgUqWUoJpRQk9eFBvC5nPG7aVPpsDq-KrMAoLeEi5h2nImqIsud4yhJPA2jOzWKtNXv0k7ISJNe5njjF9eums9eHDCmXsowbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29940" target="_blank">📅 13:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29939">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFre8wJtTqQbSPgngkt_nbyZWBLRu4C6NhIF81wJJH810BcpaVOoLcIv4eg3cxft5HWvBwPSAjJWM7ESh0HHUdI2iQuivlrsLfQPlX_8C4spfMO3449cWsb5EETgzQY_zUMfvVGDhncliqO7Vkq-FLqb7XRw1Bj-3t3iUuykXc6Xt1IMkXTsQcwF3hr6Sy_ZPgbbGxBNQuVOy7zTaGLeKdlKv8GBMEOCEQZdke5jQ8s4c5RjlR27aZbED6OYVPwKuAGA9tdoD3w0zKl2VZ7Unfb9c2ZTZihGrjXmXQqG5zKQ5TzXK_efFMmTLVRzrZ3YfxVA6m-PkXawKs9it_epzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29939" target="_blank">📅 13:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29938">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjNmYORGnGamqSbWlsXpWw9YyL_QUKnq5yEj2_PMlUpmk_j8kyNDDeRJWLTkSuPwjiJ-GysFsymuDcGCf6IoIP18XoNZoJ26Ukr7ARcTH1byU6ePdQNg_xZ53JSpeqK1HIR48lNonfUDCD5aMREEdc--_DcGAg32Xc8t9OqrIYqbl3q6NEqLq2Qre-0Nv1hJYZEHmEHXn_fifYglOkyU984-eJotU3ASd3BkYnOYBtDbtUwOef4MKvZ8TZLNEc48swF3R9qbpn9zbQ40OCnxoVipg5RldUc6qxRKr2AOYmOsyn2RSc1l6EAq29LPWXJnJBQe2t8XxJe5gTjEBsLkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29938" target="_blank">📅 13:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29937">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un0ym-Fck_GGTyEYrM9XvfmdWYMSHpqU4ijstCFo1iS1SYGAIsA9S7gXOLtb1MubPPppnhlUVHslu3NrlKMFAGZ6oVMf1rKj-_aqCBH9C9A388bQ4J814qantpYxjrHS1a1Rb-OQLZ8rz-TJHnghDVXpQQQV1e8HKNi7n8kkzPnw6hUbSGC0cEfu1FKqRbY-L8qn1-ili3SJs2OlKHwHiCMoYlLBg1oTwwlA0TQ8WVZSocoNbvB_ypGhTyKKKp5PWjMS7D55TmZ_zodhDItMpErN1mkVc7Y-EDqm-ugfAHzoHqGHv7nM5zQfDi6gbjIoQE5O5CN9EJ4jCZmvXFlZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29937" target="_blank">📅 12:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29936">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=C29vykCTr-_W7aYAPr1go4yYBBtJOpnEIy3iXZIKq_nacgY4lWs2j_MabqEcsBlLi9sx2NvG-jtx0eTZemQqonkAKyrNW5St6qObXZY-MDh6a_T3eSJoFRFVL32R2w0VjU4MdeEPVKg8DZuZMQcAQcLDHF0YYG7Ib1ZbERtOiKrHJG_1oqpVGC9PkJkb5zuaEOt5rMuXMBEszH2oeot2UnnWQV0SUIR6SBSQ5h0Zc_aEu25oVqMCzQ58cPs27cPWU6iGPtGojoB0xI5y4GF7VAzDHdLDsnuCJ78wfUZkZ3aTFGxUDExPsrHkAcy-bshs0DSVIwLsXrAEtqdy_8koxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=C29vykCTr-_W7aYAPr1go4yYBBtJOpnEIy3iXZIKq_nacgY4lWs2j_MabqEcsBlLi9sx2NvG-jtx0eTZemQqonkAKyrNW5St6qObXZY-MDh6a_T3eSJoFRFVL32R2w0VjU4MdeEPVKg8DZuZMQcAQcLDHF0YYG7Ib1ZbERtOiKrHJG_1oqpVGC9PkJkb5zuaEOt5rMuXMBEszH2oeot2UnnWQV0SUIR6SBSQ5h0Zc_aEu25oVqMCzQ58cPs27cPWU6iGPtGojoB0xI5y4GF7VAzDHdLDsnuCJ78wfUZkZ3aTFGxUDExPsrHkAcy-bshs0DSVIwLsXrAEtqdy_8koxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
صحبت‌های دیوید بکهام مالک باشگاه اینتر میامی درباره لیونل مسی بعد از قهرمانی دیشب: ما هنوز باورمون نمیشه که لیونل مسی رو داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29936" target="_blank">📅 12:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29935">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaB2R0PufMLF2fEKVq7EXM8w6IzlP8NTZ63px9ZY4yOZNtHJfrFFCYNIYaTnLP-yqQWF0mzlMRtmfvtx5fkHBeL4Ihj_O-GeXEghQkMMEgRv5vWArbA4BxnVeK7ydqfKiwxRda9c9xzQoj4qLlulr1exMXc24PL2AOd85UyA08D_k9llgSmRlVmtrTqWs6SW7M9Nr3tzkKfsX2nwE_h4xhTCw3nO35Y8cGNxe2s8E2kgqUG_SdjxPwgPU0uFpqMN27C770VwT31GyvN09mAWZZQkgjw_Je_xke3lrlo3kmYIBB6zrckqocFgzRqV33mt6WcgjbzC_wEJ4JFM7zAdQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روبن نوس ستاره‌تیم‌الهلال: کار زشته هواداران التعاون رو هرگزفراموش نمیکنم. اونا ادعای مسلمان بودن میکنند درحالیکه‌به‌کسی که دستش از این دنیا کوتاس رحم نکردند. توصیه‌ من به اونا اینه که دیگر نماز نخونند چون اصلا مورد قبول الله نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29935" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29934">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0uen8v2ETOSJgIgPqR4QZYmw9X-Cjp9cHOtFk5AVop-6UGM0DGO7Euz2QyT97X-ftAul7N5N6vIKqpkZ2d8XBTFFfk7lFP_DI1_x-yVP4ghWTlIdd-FOMr-QNnqd2MyBv54G3xRP5Z5qukBF-hJY4vCYAqEBSSZgwtgmytN57rUqg6OkB3RRnA2DpbySky9U3ffq4trjMRA1EnqVYZejoPpOGrYGysv5TXCgWKowbFBqcQBkfq1IaF6PoKMZuSupIv-_fqCDs-iZtypzo06mWBv6ADBrxlJEVq7Y5YlOi73mCerOKC4r2gvPvw5vOmJsmUbgdkd0u1jdo3LZF9Rpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29934" target="_blank">📅 11:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29933">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryBMx-TLBpUP5gNTalcvj6cPFZ1Iu0OkLM4EaZFHp9s7BZ0onhPy6uooYRoN9PriHEi9efvw1qopbOZzCRyfSbArBeUDAyrhs3yZRSiWQgAiYPYGZ3bRRNElMziNnBFYCTpIt0X3SrODmo6r1e8Q5CeGVyb4fH7-GtuOyX9Icl6DteMMyUzoOyvYlWgWGhwIOYzuSiyiMMWm191kpEih56QO_gw1UoVeW4CpgMyxUXRek1OeMfKCsONUThUgfpS1Z4_Zisn2XmFHKP31N-AScHLOszgNiNM_QkPwQ6f3FyLfB2AJiaspG2DhuzbSf2lhfjeEKW1iCkDQoUrO4Fxohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29933" target="_blank">📅 11:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29932">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKeaQCsTkyPCamTzaNCVuMgzKdZYh4Jo31_j2cbkOfdlHAX5iwQtmvrSRMX73N_Jw9x42I23-JKm_pke2XVhTfgoY4VmdHzwMF4rfZurOFK7C0I6Sb5JZOXVA2i-5KgMjU6JTwVAXJl0rWOpuDKl_xADdEYgQsI-5FqesuI-TodCvzIuzwlRe7M-zcug_S69IzFl06pc5axQuZw5ARNytE4SUXpzDPb8YL6j2NzTbqs_qy7S3FBZYf-Nk-eoHE3IhQs5U3zwGvLdQ9r9ch7YXBjAcRC4rduo03SshQx9EhpU-IRBdllP2RCtazGgnfwct3NCNBXkDh0ZI242XSteAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29932" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29931">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXIPofXgQ9zgTFF6kH4FNeNrAOUOD1UNdZbWkjtqx8svWFir1q3zGA6svjD0BsDumaRcB98Qt3zDIIFNr44JqUiCdXqpfo6g1Tf8DT84aQbGZUNVVubTXUXAyNqMUbDRWuV1RhcIMf11S56Nfk1eETU0rTr0qvCWVJuH6pX6F1E7cBsSGmYV_Sl-yHW7Ig9RIX84jVzJH8IiX074l6KQ00qf351_OKOsHUS3ji15ydB7yj7hQgyCkfvYg_YVTFNGe6KzOqEDjkD8bHTswDyLe8mxRoAw0RTuOus0agC4_7oA2beiKJMmxlLoPKmNCXo_kVOQCGY15SKZ0hRyDw30Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جی جی گابریل پدیده 15 ساله منچستریونایتد که در دو راهی رئال مادرید و بارسا قرار گرفته تموم بازیکنان تیم‌رئال‌مادرید رو در اینستاگرام فالو کرد تا نشان بدهد علاقمند به پیوستن به باشگاه‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29931" target="_blank">📅 11:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29930">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJFel1a0qIVjyDpi3pk0Oeg4EppZDGzs2aRPZ53ZuOsagXJ9kUxmYortp7FN5OR4wp_rq18u8r0Wor3LdjgO6J-nPbUzJSvNqJR1WuXZb8WBfkFsVQbdUOzseaxLmld_Ojufk-Ny5p1Yni21nTjNPTdW8ZNWWoxeDZ9SsjqKj4TeMW7TV8rxs9UPZFrSmJusjXLlEvJeAgbd6FAVt6vSfx3xIv7x9o8Ar9uJLv_Tw0TQeHRZx7kXyE5IjMR8TA4XDBnpGKqivzPSL_ysg2TGMcNAd3Wj-1oCP7GFa3mjg8tms4g1oPlj1gDPreYIuKWKEb_yoLgnSnHHgTFn8R9jYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29930" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29929">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RglrKop9ftecQPlH2Ed3EOUdGIVfmUJJ-Ush7Lm-l9Ul_KpzAYJAFU5SIJf0DyxemigbdlucoS6s8DvTV6EyiMhV7s8DO95uPHca9t9heltYa2_S7Lm_jYqL4nMID9BymYjp-UOyeiZ9HGXnrPnIPSg_NC3eviJ_wotZUpHiAQJI8So2UKYt1cHGGpad8G3yiAFFA38kpLs0USm8txc_Xpo4jvdxbliewaChOINZUYFFv1Y1QE8_MzLodt6b8LYAaY_Cyrpx15OmZZri7S7yqyiOPKWXoXSHDx3OT_BuwvMsXVfUJAAMagrKsohJ2kouciokLRi27ITmscdnw0mPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیونل مسی بامداد امروز 49 امین جام خود در کل دوران حرفه‌ایش رو با اینترمیامی بدست آورد. لحظه بالا بردن کاپ قهرمانی توسط لئو مسی همراه با آمار کلی او در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29929" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=cg1Luiubq0mC68ONwxiPV6dezEVms78RGukb1Sh7iLLdTKVcTSEQgvUvJMeKfpDwYL1YGlBXk1lVYQz85KOO9bYSEd_DlU_c099lee7X7ZrS5Y1-bq2J_04HoxoQoWSC4KDdnwe6S-JMSQ5BKtO87CQe6e-PSLp3hAC7r6ixpQv1mgVRiqPK3AKDjenym0IyApn8uqxouNaF2ktgprZZmmUK0_F158zZ8RctDh9Vf2-er7Smw2U0oeOAO1DKCpD6BUB9fH_Hp9maWnuRlr6Te95osqGvszsGym79sSzNHQObw1SnBMQjnypiDUB59ekEx6lVDmpoT6C15cWaaWK-JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=cg1Luiubq0mC68ONwxiPV6dezEVms78RGukb1Sh7iLLdTKVcTSEQgvUvJMeKfpDwYL1YGlBXk1lVYQz85KOO9bYSEd_DlU_c099lee7X7ZrS5Y1-bq2J_04HoxoQoWSC4KDdnwe6S-JMSQ5BKtO87CQe6e-PSLp3hAC7r6ixpQv1mgVRiqPK3AKDjenym0IyApn8uqxouNaF2ktgprZZmmUK0_F158zZ8RctDh9Vf2-er7Smw2U0oeOAO1DKCpD6BUB9fH_Hp9maWnuRlr6Te95osqGvszsGym79sSzNHQObw1SnBMQjnypiDUB59ekEx6lVDmpoT6C15cWaaWK-JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇹🇷
کاشته‌دیدنی آردا گولر دربازی این هفته رئال مادرید و شباهت‌آن به‌سوپرگل‌اوزیل درفصل 2012
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29928" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29925">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXbBTT1NCy-aWvvsl4eFCovfddcgBOaanBlOkbgGJWQt4D-SBpbGftYvX8EDPWMEjSVCferUgVqC21uPb72AmKSS3uzQNVtrEfscasZzM0T7gu3fZ86vFFPt9hL14Lmr6WNMgunWZMr6g1CDBV_VaUIgu9EwiM6_iqXVIZZyL3eW5Wc9Rs8l6mV4IJgi0n_2itUJk-I15m7xfqtqp6LNBOfZTcV7YHzZC8wfn0h3MpjOs7zytpWr3E1kCF7oD1nKjcB4UbMYQ_n03-U82VvOXQloZUQ7t6C8vKE2Y0f1zZuS3MpW2HxYdy18RrRshn6tMPfRJg2fRPrnbKDLsr1goA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7ZqJwIkjgPJMgY8LpsKrHzMMou6X0DcANEf3afix0xhhCTjPpS8-NBS9Y_-cl7IdGZxNfBMiYhnwLV6EMoI8otg5QJXtkKLEhncQszClB_WaHI1ANp5Oo_C_jqFr4HGMfAgtZgU8nOfG30iLUS25HFr0qZhAA3rt9hM-eIrxakyk7AFPKrM5j8Z6y8PO0l3imvGGhUp5eL9ethmkifBHz2HqxegV4Y53SUtUq3f9mNOvHeywoT4nQGGWeghkOzNd51spLdDho1wjBq_jERVT85BgBnhhkfkQDHbwFJx9rfa7qnS1MoaX0-6LPmdsU56pdGazSGs8NrsWOmmY830KhI8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7ZqJwIkjgPJMgY8LpsKrHzMMou6X0DcANEf3afix0xhhCTjPpS8-NBS9Y_-cl7IdGZxNfBMiYhnwLV6EMoI8otg5QJXtkKLEhncQszClB_WaHI1ANp5Oo_C_jqFr4HGMfAgtZgU8nOfG30iLUS25HFr0qZhAA3rt9hM-eIrxakyk7AFPKrM5j8Z6y8PO0l3imvGGhUp5eL9ethmkifBHz2HqxegV4Y53SUtUq3f9mNOvHeywoT4nQGGWeghkOzNd51spLdDho1wjBq_jERVT85BgBnhhkfkQDHbwFJx9rfa7qnS1MoaX0-6LPmdsU56pdGazSGs8NrsWOmmY830KhI8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29925" target="_blank">📅 10:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om3mCdVP32ISuUouV8y_evlUHtvxKDY7S4pbdGN1nrOrDuI7cRQdBhm6BF8PmwJaf-t5yj4toqYWvxR0HehnA6z52BO8_X-CCfhT-XY_QAx4evpKRhGWwNWSLi3RGc7cZkPYU_Py5NCNjLfOGFYil5_5WQwrrmECSqBsv0Cq9TZmEaAsUPbZCKcMA-0Kb4DAo1v2GlGMdI72OQP9h7bXw53e9LzxITwdU5RIYL9PgUEnpr9DBjS7-MozEnO87OpnrGigLl25MDnx6kBm-Y-6RRwaO6y-Ar4EN5RortKxGI6mBLlz_gAP7sJtTe-EUBpLLgx-e4MuB8QHLs_DHMA3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد
؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29924" target="_blank">📅 09:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29922">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29922" target="_blank">📅 09:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29921">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
کریم آدیمی ستاره‌جوان بارسا دیروز سومین گل خود را برای آبی‌اناری‌ها به ثمر رساند او در این شش مسابقه‌برای بارسا 3 گل و یک‌پاس‌گل به ثبت رسانده حالا پارتنر آدیمی با یه کامنت به یان دیومانده خرید 140 میلیون یورویی رئال که این فصل اکثرا نیمکت نشین بوده تیکه‌انداخته.…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29921" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29920" target="_blank">📅 01:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKjsNDq_4CvdkBjS_ZvTB5tZ4rfrVg-5arBzgWAwU9HjUz-pwIzgfwwjCE7CxkeS4D33IBULn5Ij8wohuKzQwfGNDMMxM70XamPpLyLy5x-Wz4vub4tl43UT-4NTRDtIYyugi3w7E463lanpbWneNIcyqdh-oiClxYsNRWXRQxEYj-O2iw-mijizyTWZkYLcLC6pnMVcCP7GdaVtBXq0AVmZxuv-V7GdOrNcCiYFRYuJqXbEtje9CDvx-GswUxDIhntPPfKsgX6zelyIaYVh_qJCJfg9JlhA5hZjturnkEnA_-wyeSLPbApZBcn652HzdJR4XAE4u1MHRDQUBoFhXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز
؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29918" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qx4WpoWVVqS1HpOty6MllQraHFpvPTmaVQv8IomqlaQvBOzk2YL0VGAHWx76PG5tXtdfZc7VcOu_BVj_A3PuFmI4koMvbkuj-D6-HN7O5BgyVKy1-mFLakW_sMM_AD5c5kT_1lTDndZspsuuF9rI-YLaSvVn0qVVaeLWbPNzJ2K4cwVfeXtlz5PzsKmx3jCGQ58QDI2wzq0m6kSFtjt7tvouag2JkRYAcnHsOVSF0syoXv2sOETVySGNHgSAJPS0Zu8A7LJwKHf4Yl2I5h71eFOA-mDshQo7adWK0JAgl25JsBze1eaVRX6hT44MB8qqfLChyaSDfhqXhIEfPvvvrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازکامبک‌برایتون برابر یاران کریک تا برد هفت‌گله بارسایی‌ها و تثبیت صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29917" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29915">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWoGpYlitJj-2P0LxQ2ynv6xyHN1BHrwwZ8na_MLhKWm7BPnh4t8mlfC-L7WqO8Z3cViXbAY1AelRtZ-hSB8qrLQRb2l3waSnEZvezoBpWWp9od8Hdv0MplU_hpP6aW2plFZsvkOrAfhR-5UCMwP-4vLHKEtHh0jQNNSEA9QiP_pHD4yEID1ua30OtpQngCVbSRheFF5hXve2ole7kpP3bPRJQfepdCT6TQVDd3R820KBCZ1PD8NXrawIm4CwR7-InrgnPL629wXrfyQNP8mAYK49lR4GBw6u0vIS07UlnYte3_8i5CxDGZu63_eysyqENJT3bnl1joVYkOHhBTtDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqUaAY1i_yucCbFlpn5bYXCEvItlhfu9RR_9sIkQqFDYBjw-XJaN10PTGQIjQIMB-5Pcnla-qni7RKDMhYQzrRRoeya8FKvgSIFNzXhpebf5LGQ6ju7EW2ih1paz5FulGt7HPtbPBy-mI-KD8wIHoPXe3D1NKOHz0M4ufP6c4u4Jc5DBqjxuAKRkrEnNxUKnb2EyHirOyE4EWRjNLMD_fw9RLPaclYZRCWmLjwaL88-EyAbjIL4IeCLLYKY8RmByGviWaqLP5ljjLlAZVtoD9SdClkKeM2reiorXxXCZZjRZpXUiqwoSIxgTNSN8yEsO_K9H3bfXYxw9xOXDYKF0dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29915" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29914">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD3shm42LtR-VJxpynaXqHq_H8w7hwTQOagohRB1p5-V6KvEWJSFaGjhreW4C69tjSZYP-QEYSf18igofGwCI8MG0yfd3NYqKoRz1y0SCk5a-zzq1dNw-_AZqjPkveW3ANpLqJpqpEHkuipqLH94aO11IrGPhSoucSbKIGL19gq6cpskwCtomv8jDbb_O2nVaPw3LfQRdf6qZ1vWCKvdxlwHgCXToQUKjUcH9-i7Rcppyvu8Xr5eHJlocL9Tyu29B2eHe6p6kBLBTgiP8W5sldfFdCswrG2PPUmt29eErE6t5Rwglck6l939dat7UxUfAU9wcnfZUiAvz0kjlXNTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/29914" target="_blank">📅 01:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29913">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVGIgIZyCc3meg8OgzYvzdek3HSUT3qxPmGVHaJpoID2Oxxp9qfCXtSFHXvNcHD26pFKuItMLvpAIwQiwlw9YNjElw008C28iN4WqfboFmEdLXZs4x9UY-RI3Cirp9NwrCNfr9VUI7CWPtN-AkJJ6JHVU18SX90hapECD8q7S6DMDhC6WtS3fEmNF3UDd3eoh6do2TIcC_ZcSr9JoNXYQnK5tdmelO6fPh6S-zmX5QQAbcPQkCf6oJ0yQLJuvvP55qmqD0119lc74CLQUEOj1USltgPzQ6eRf3MGZKjNhFebozzBGmrxWRWyfTUr5UtoQmTL2eaDYbgNtgBbmTXx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/29913" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29912">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri-wqWkVa0MDMbck_WoeLl4vWyGXfHzE7gxiNXl4-d-0lEM1Uu3jckx0ZQdHQzdeXJjHzkNDc-O_a0JArh1D4ggbUdIgWAj8D_PVEUY3FsQh0tcJ_xuGf872NpIPM_5F8qoDvxF2nLBrpQE_wUqgGhZF1aFTRuPMJkrQ70_fmGqAbzwK55H5GK8DSeU5LuvNiCE6JthOaHcBSr3wHDaxKtTjSkVe4Ez2Tm4kKBltcccV7DCl3yJTZzHSFR4ej2Rjrz6X0VeJOoLF4pJf2gJy8GDvYsgI04GXWbtopEudvF3XwYr-C49AWqkt0AyI28taAZdzxvLh2UTGjhasHwJP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29912" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29909">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfTf8-e_b_J8k70v3dqH0H0rU1NdJSWAvkay7BjjdoqpY3pieD4m8tnV16q5OQiBfLUnfLOLW36UZt0s3EKVWrdmOPG6fPfXy_8YtNDpjo3k0ZM33TeCQfn_N4qlwG7MJO9OsxapZLmAqWBlYW_54ulmCaEDVEFZvFjtKvylItbBoMFD61wxsjbrR_HUlXejbqA1V4zeM1wwy7_O4PqHz-Me_tsdIpdR3ciSdIKOr4mmvNTdQXJLCgIwICg0V1TAP3ls5btMuaEY3kIqHhkpX5-fQ-QBBZ945WYRSJHuDws6B5lZEJODtWrdujqfa_DlBwX3TolX2ysaUwRliQCGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7cwEwbj-qCFEyEAujHAnUyWy_UGxJNGgUnqS9e4KO7W-lZ4wHf8E2qcF7Mxbtl1zmO-fQx6EWn9KnwDeS8bkgIfKAKyQ72ncbw01yO2p3Z-WGKqlOM7xRR8LBotfTl5PKFPft2phrejcU-kIrd1G2ZG7S_nGItHm-uduIF57iWf5xxhALm738lHu-5IAzZIxehRQ4xotDcdiNIkIbQxA2xvL9h4uN7SPscMsxhzgj0WuEUdnrYvpR5AUl9Jr-7H5qE6LmQfKndb0zDA7uN9nUc7BY9lqXXzgS5TeiRmN1iz290hgo8l90RMi5VtNPs7HSwM9ojqPhOdvWyhBzEpBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدارمهم‌امشب؛
حذف عجیب و دور از انتظار شیاطین سرخ از جام اتحادیه با طعم کامبک خوردن و شکست میلانِ روبن اموریم‌مقابل‌بنفیکا درفصل‌جدید لیگ اروپا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29909" target="_blank">📅 00:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29908">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tH1P6M2iBH4BftpAgEDH7ygWuxJ3VTYfBiCGi8XiSmDU9w9omO0-XxF7kJtRsA3W52MegBv966rJDAQCCxd_G_NC4MFkjba0yRz63PLQaPF27MsonzF3p0VYG4xlY-NUs6R03Hr2PUO9NDXeK7bRSKHhBvKyaP6Kr89KxUp3kWQq8xDPTe0t5woh4q8Q7aujkJrXMy4waoLDYVDigT2ELs97n5ra4Tj-46kqLbBVCseL1yycRlLLxFfXpB-aDT3NKwIS0Zx6vKRrbxELmiHm4-AT8H-3tCshuCOWJo0VaBUi5YvbFUAQc9ywufXCRfkIG_yAuzKQm8szyyZ4uYcKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/29908" target="_blank">📅 00:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29907">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2KlYCPscupPvFPjPT38VPBPjhQEn7Z4EsQnJHJp2UDMf5roC2Mi-nOnWZ6A2H-jgBNPIa-I7JPlLEBT-m5Bi2mB6xrgIN9ZHA6IzV70-Q8QdlGuxd84zykduITpcD_mkGMNyJtLfium2Qw1J653ZeUa_yXKKN6qEQydlktIMBG2lYJGCyqhTPCLHt0XvaQ34YctOBqK5mBFohUWu00kqUs_UCkNrgpbc3J_NwcqJHWKdrdB-Q5qXjEkTkuuFzZsUZ7wjI_W1XgPQlnoXfDieYI41QCayNQ1PWXvbsWTu1TKtZt4FhmF71lEp_LmSv9N41PBBILgbq6GuaBtQOMyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/29907" target="_blank">📅 00:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29906">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLSHf_PGH4OA4TB6ew5Cf5XZhUvvpdnrhNgwzar5gCEfeOo3sxABOWh1AuYgvZWO9m23_1kemvR5hSvnZkKyXoFYRmfFMslM6cMwq7Iuf0oLon15Hrq85aigX1BmM7uDe9LefESHRqYGe8xNtGlV76wF38Y66CytehtcxM4cI3rgnmfTR5UKDvhRATghVR7uoESwHgNGMLF05dOR-mpLC8QEIW389qcytJWqgjp5iXPnej8P3KUQe9uvzGHCP1d4D-itOaqRaIl6QCRO5_MpdlOu8kkRSdKnxZNd_KnD3x-wPhekyQx2xV2dRY0Du6y91Z6wAzn9LP8TRguYJc_N0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/persiana_Soccer/29906" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29905">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=NVIriswhsYd2Nw8UwP_P3qUIqzVakhiZHT8JoPouTI3oQFyOqWJvrXwVqpextx9I314H7fvpBEpex8ocXBGombabsvGMqOQBbs8dxHYpYgGxqbeqDUhasMPu_XKrFRxIRKliqIq2P_N-RqRiZMU7Kheik9kDQP7XYoXhtvMiKFBAIpakXmqyeU5BqZ_KKKOWmIZaE8QavJgbAG49wbD4LmZnAA4GrYThCYyCa3xdCS5IRkkbs2TrbnZ11oULDFeExnYq-o4lGoZzsfJsamjS7x9v_lZTcLm4I8SmGztDVrsJgaa0IbbUGxlShT_sq2h6BqmA81EkChk47upryej0OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=NVIriswhsYd2Nw8UwP_P3qUIqzVakhiZHT8JoPouTI3oQFyOqWJvrXwVqpextx9I314H7fvpBEpex8ocXBGombabsvGMqOQBbs8dxHYpYgGxqbeqDUhasMPu_XKrFRxIRKliqIq2P_N-RqRiZMU7Kheik9kDQP7XYoXhtvMiKFBAIpakXmqyeU5BqZ_KKKOWmIZaE8QavJgbAG49wbD4LmZnAA4GrYThCYyCa3xdCS5IRkkbs2TrbnZ11oULDFeExnYq-o4lGoZzsfJsamjS7x9v_lZTcLm4I8SmGztDVrsJgaa0IbbUGxlShT_sq2h6BqmA81EkChk47upryej0OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
گل‌فوق‌العاده‌دیدنی ژائو کانسلو مدافع راست بارسلونا در بازی امشب آبی اناری ها برابر سانتاندر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/29905" target="_blank">📅 23:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29904">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=rNEt3isQTapkOq6FHqnyqWOwH6pED2nC3c-TkFwBgxYz8kwcI7LZkDQ5M4Vu3P-0NEswrTQ6Dh_jKpjCGhp2awGwgjPNJwjQ8JSErW423uSqR7on3oMspnR5gSrh-k9x-Eh1UdZfjhRU9l-k4sCaNI6mMvrXkr0jCxIEBokPQARavcmKGhaHbkGHxbzd11MgiN-3SHXZTeUbE8LcfP3EDXlcJlnhpSyEzrR7Z5RP8Vndy3dUIRhjRZ3XNpxVYRf5oW_W6Nj4sTrf69R0NQd75S9AvjaXrJMlXEigq25zeeiQwwbLaB9yt1zFbNb2qeKZSXby3mn-EQJ5SYJZpMKStA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=rNEt3isQTapkOq6FHqnyqWOwH6pED2nC3c-TkFwBgxYz8kwcI7LZkDQ5M4Vu3P-0NEswrTQ6Dh_jKpjCGhp2awGwgjPNJwjQ8JSErW423uSqR7on3oMspnR5gSrh-k9x-Eh1UdZfjhRU9l-k4sCaNI6mMvrXkr0jCxIEBokPQARavcmKGhaHbkGHxbzd11MgiN-3SHXZTeUbE8LcfP3EDXlcJlnhpSyEzrR7Z5RP8Vndy3dUIRhjRZ3XNpxVYRf5oW_W6Nj4sTrf69R0NQd75S9AvjaXrJMlXEigq25zeeiQwwbLaB9yt1zFbNb2qeKZSXby3mn-EQJ5SYJZpMKStA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لالیگا|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/29904" target="_blank">📅 23:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29903">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTy9-tr2qk93cP6g_F5cSByFRr1EykkTOpxVo2kgPGoEJ9DG1yNmJwRBUjFYLuc6MVaTmci--cm3aaPni6Lz5NfjibswZlu34hkNtGctD3s2Ik-ZSMmWsyaVWIrnZLmsZ1bBhv_N1i3FUXv60ByDsNj-Lyls3L3GWV1tymEQcF3ma_u37YGYSRU7R7-bNyf2S6Hr4yZek3g6TkImhjYqkMPEJ8TJDSm4sbXIrepTrQ-JZghb3xHEfTiCQoWcnZsbIeZyTaFD3TYGEHMcEn2IBNaOMB3Ul63BJqMBkjPFLp-zzc2j9gE6cL9LMVrhw8Jr6p9BnV258IS7r6RS09R-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/29903" target="_blank">📅 23:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29902">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQuWu0Z-RXetg4Y66SlJwq7s0lMQWGL9UXx3ffdwX2LMdPbNtR3qQi2FO-5tIb4Ukv-3ogKeETZtgS1sAzwGcs2A5faCYvwfLzOv4UDY0LRE2zGTGtTBOFMdXcTt1BROlmFK2hqB2s0TfdbTSoSUxvzvKfFaWRZcUO1HrhwdAZAXSNhpif_QdXx0N18K-JSGSP-ayOe_ZkPvcd0X4qRSg9MorE_M962jo3_Xg7zkL9kQVTJEls1AADfo5YxXygU1ElcAirgBnUc3CHNbyVt-Sxf-DRaKJ0gg6eZVFdv4ZO0z2n1Ob_-V7TkEyTlQDhEbBSsfR7IeKaT8zpS1Co0kYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29902" target="_blank">📅 22:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29901">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItUt-w6IWePz0HRJVl-KNGZTsbmGgZtSjQcYGujAa0Gv9C6ij213iupxAxbdRsJSZ06mAMYogha4mHkSQVknzCi5EMZ4F3IYwYbMfvXoQQ8FRQHTsckgqgAT5PL1Jt-Bb_Lv7vEcqGzsrMlYW7n_y9lFfgm3a7jeU_bQ4B_UA-u9iJzTpkqOY-xf-oFo7yH1cvqbFfQ3Mi8_5JQnytEKME3y04u7Iwo4hmMmd1JNaSSHQBYXtKQFU8eLvQoATWmUoWUvvo3CDExviXcq8rEH2034A_YJ2pHpQ8Sw5unytMY0F13u_lSqqaFXPIve_-sNYBy-xBS8ntKCBJShv0feCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇫🇷
فلش‌بک‌بزنیم به UCL فصل 2017
؛ که تیم موناکو بادرخشش‌ودبل‌کیلیان‌امباپه 17 ساله بورسیا دورتموند روشکست داد. تک گل دورتموند هم عثمان دمبله ستاره18ساله و فرانسوی زنبورها بثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29901" target="_blank">📅 22:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSaPkBWlDNiTFcjvjiZwnaYhHW_O4h3OuwKnLejFb6JJ7yB1mbNHLSjCHIK0uHiiv2wVEPb9P0xMCO8J5zRC3tqcwZsmfyBKg8soG49AO5t1Qxu08HwdJtAmgWZn81YuOv0Y8fmg6zAitQkHiaOiqpFUUhCINhDM_14RV7eP5y8cDFxUeh61ngW-v9iwnPC_hYzL9QnhOsnklPoG2JA68cY_Gs3A3yQbGcK1zxM__5PXJ7qvLHIEzor8sDJksJHyXv3STlz64skt0iNIRB3sIi9AG7BJzzQKvkrHS4u6DowBDos1Z4ffF6nr-Tm7FgQgtgKvaRmFFB5GBFJrddYLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش یان دیومانده خرید جدید رئال مادرید به شعار هواداران الچه که دیشب شعار سر میدادند که رئال کثیف ترین تیمه. اینم از حرکت دیومانده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29900" target="_blank">📅 22:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29899">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJeptFzQreSj6Eje5MqtCDxUDcGeHY7e8ASlPUARyANmDtOEV4CBRAhiXy9O2313CShYo2fBDbiyhMNR4QCvnxqj9f5VsUPEUu7Ws64aAyxbqZnRtdKcJsBxyvBoNJSeaP7hDWoffoE9HGDDSU9CGooeKwbn02vLceWxJqiTsYICuuYg8HnpM-cKFw6Njd4lNhk-bFdCNgs4t14roJBWjo_zXgoztBleh5PUtIE-P3REVEoHi4DgtE7bT43Q7kodpgRv3tXvtGMAVk-dYk8lv0SfD1S2YLWK_F8qYAUAAQPt0T7gESQKISZ4FQNRdhun3SQ6_0fzcYXz01GutNPwDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لالیگا
|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/29899" target="_blank">📅 21:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29898">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8ZgDIJoaN4zFIPVB7qBVoJBjE1Ug8LVjwtLy4gLzvmg1Jf8J1hM2Y7rXdyD92QXyyor6bYJM6zuEQ4QAeOIiVZeR673-7Vtq7pTq6VwjLUjqbZZlzzK1T566gjYBBbhQlc-o6qWHrvpVWSngVcKUTaQSO7rz3-L257WAOtPUBquy6w_8dVjbotljHfNMaQg7jPMyHTTF70Ks7KHiiO3P7qHjP1V3vVLRcD-ev7M0Z2L6uzaty4FUMFOdmuX353-1eCBPTmLvpSKv5afH9e9Fq-uOOiviTeSpY3Dylde_fIiek2uBmjYYdLk7K1EAoMLdUYLfOpx1sbtUIQt3kCHTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/29898" target="_blank">📅 21:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29897">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ3hVx2RjjVqC3JmBMPLt6zrY-lg2DuwDhY2dVWE3fSFmDrK65kLQ49nz-uiZAvoq2dAZjkVHikeCnn8L_QLJqAQm5rLlhfe6_UVKwxUr87aop74H3rthjn4h6VpFmAz2vl5dSrfR8gtz1i7Dy7sp-bF41kNEgDJSGDwen__OgUD-1pcNsUOsNvVKQaGKd-2sFwBYhE-SioX1IC7yo6ITj4kGzlhiIn9oIifopXe2McNSSGukwH0kpCsMfeNbDUgx0FLn6mXRfiTomLwPfRgqPhAGv8sRMMRELajZ1HSIT28pXffYrRqtMy97Qp2RjcVioHY6omxTKA61i4px9FsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ رونمایی باشگاه پرسپولیس از فرشته کریمی خرید جدید خود؛ کریمی از 18 سالگی تاکنون درتیم‌ملی فوتسال حضور داشت و بعد از خدافظی از این رشته به تیم بانوان فوتبال پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29897" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29895">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7igMYIGUrmkdno0q-SgLPbvxmaYGJ8_He9htqosYdK4SgHzA9fejhIEYVHGGcNKngWfrO2Gpm84wMzdfkWlejI28SsqeavlOdLDUUtdgW8p3Gf9ODb144RNmiv0XIkrvvxp8kZsqeTO5gLafO7DHR55hol9eQ5su6Vv1arIWXn0g4VKQOxd3Curhh1XBdFDPI9dqD_ZLSZ5LFtUpyrXRm_b-uEKBjTfUIvDbNs5_CYe68Jw5ZLnf8th22-uWEex4po97d6XU14KYHpZlXHgQgf9hEim9Dz_r15NuySWTx-UPjs1KuXfJJRe9_BVlAbLhDa25NAkz4A5b_n0uo2syw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ یکی‌از مسئولان سازمان لیگ امروز صبح به‌مدیریت‌تراکتور اخطارداده درصورت استفاده ازعلیرضا بیرانوند در بازی با استقلال در هفته هشتم لیگ برتر که روز پنجشنبه 16 مهر ماه برگزار میشود بازی سه‌برصفر به سود آبی‌پوشان میشود. اتفاقی که سال قبل برای سینا خادمپور…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29895" target="_blank">📅 20:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29894">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By3p1xrY2K4L7-SUTrg6a73UDznb-GAc10BaYFHlwT0j0Xpg41OExlRj6Quy4UO3QBNwxdHXTDNfynnSMlgwlYFhe_O52DLWuwBSyeT2hyMImoPc2TLE8KRuXIxNd3HfXcIN-d_lcsmA3eDEcoEQsLNWAeLgAOrw8unG_AKdMgCWO_Nl0bqAojlJihUBuhtf4HckWH61yjuGnnhPg80bLatJ8O0WplWVJ3qXwuEktIkOgRU1whbETRWVqpbFqKwD49GehfxLv2Y6t-w2jbM-hdxsm_OHBybZgFmf2scLBWuvGD2mOITY7jeCiGAmv5SRMUXqkktZC4o18y23sVZwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه: پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه.…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29894" target="_blank">📅 20:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29893">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl9t9CGL1mR0WFO9YBV-KGSxsf6ja5M325V6E7ScsckNdYNxB0zZfaXW-5B8NArghRxgF8SSXb2WYcUMHDPxnHYV9gxc353-gJJkUyQZCDJFTjOqr1z2Fo1TEqKBjWVXAtdFdeDxipATZKP490srO-ZltaZXAhKqst7Nghj77qCvsi-FJ3Zp8ZN7N7j-o-QLftYimZi37tl4zovEI5cPiu_mw1ovj2Zf6pl7QWFozyjT8D6K58rW68__2lDfdthNPMV5DuUGIDFzm-UxFJQ1Da2Q_J-R8yGVIFJXY4g02himNtDhzuwMFeBAPwUXLYxp7FEKFV0G1vHw9xoxbrQAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
رئیس‌سابق‌اینترمیلان:
سال2012 خواستم به هرشکلی‌که‌شده لیونل‌مسی رو به این تیم بیارم. به او پیشنهادسالانه 500 میلیون یورو دادم و حتی معاون باشگاه رو هم به اسپانیافرستادم‌که او رو راضی کنه که از بارسا به اینتر بیاد اما لئو حتی نامه‌ای که من براش فرستاده بودم رو باز نکرد و آفر رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29893" target="_blank">📅 20:12 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
