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
<img src="https://cdn4.telesco.pe/file/LucBEnIW3xQ1js7fjDD14wqoWoMQ05EELkb7BkCQasP5vz1-FSGX7cqvcxPjyHxFzpXKd7AsKz8Le45UWl8wnTETdNggvRm7j11neUzpVrbCDx54nRbLU_q4PE1XegMg70pEZFIp30IEjJpmQfyf6K1NWNQV1qFXkRUjeUTmYuTlSC99PW0xbZBVVIBroD--by7i2ypjdgWtOtRM9E98Cx3amvL4V569DirCTKcnnfc5zbAlFEqnHQmmg-NmDM9feS7NERHCjtjCR9uKVJeI4FjbJp57kLk6ftj-U8MgetJ3ScaOZayv7N8Uhjlt7SQBfHRA3mtVDPjxC2cMMU-lrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 14:17:28</div>
<hr>

<div class="tg-post" id="msg-133335">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
#فوری | سخنگوی وزارت خارجه:
🔴
متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 185 · <a href="https://t.me/SorkhTimes/133335" target="_blank">📅 14:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133334">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NizfDodmzmjVJj7n0hRl58V4uME8jIoc-xCv-SznTaS0m8pmM6I-6jBbwtiRMl8djjFK0HFAp1pS7nIkKJ_Yk3wHqQ-9DY_MpeCfplX7_ntMEc3-SfMuboRzjV-D_vMcsflqrl_if4UC7nwVJXqcFsoukH7oXjcoQZ16CnXq6nqZhmjOYlNBSUB7hNCEudMAHCcqEDqJWemFsXnborQpPYKo3-HTpsq8oECoTistuGyDUnntN8Ia7jJsF-YtyGgF7K1aXAqznqwI8yNsRSd0qzV0rtUZNjGNmZME7TBr7CcEkDkVTlcZXjAO6Q52fgdKUI9AFiIMin2LW4dQwFHkBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای تورنمنت 3 جانبه
پ.ن نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 519 · <a href="https://t.me/SorkhTimes/133334" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133333">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmBiieDm1__55HvoHnAoTgJTlbFoXwUBC-jATF6BuJ6ypzkQ6Hm4fCUZLTzSTug-6REDs3zNhNZWjELIZ0Z57auVrMAFuCT1CggX2Lb1Ogtlxu63rYTN-dHwequk_A6Yt2UHFnAFmaOMV1nlOByrWy4Ow-uPwCzA2mhEn1B9twDpA1EF6cLLkJk-FYactcEN6oNUSHgyxKYit7KAYPQ69cFiA5ahXo1LKL8o-c0O_6gBNMMRFI54n34hMEmRYTDvT9HMPOF3yOrZYBCMdfekdkpa16dPuWHBI0H1WWEDng2byJ2qktXgHBEpACMqLN-C2HFpb8wzCCrFapWP5hnSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سینا اسدبیگی در لیست‌ اولیه‌ بازیکنان‌ مدنظر اوسمار ویرا قرار ندارد اما مدیریت باشگاه قصد دارد درصورتیکه با احمدنوراللهی یا محمدقربانی قرارداد امضا نکند سینا اسد بیگی رو بار دیگر به جمع سرخپوشان بازگرداند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/SorkhTimes/133333" target="_blank">📅 14:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133332">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
ادعای العربیه: یک تیم حقوقی پاکستانی برای حضور در مراسم امضای توافق میان ایران و آمریکا در یک کشور اروپایی شرکت خواهد کرد.
❌
ایران درخواست کرده است که توافق با آمریکا در یک کشور اروپایی امضا شود تا به آن جنبه و اعتبار بین‌المللی داده شود.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/133332" target="_blank">📅 13:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133331">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAarWZf8Y_mWYkr2Z_MdvVaos-18mV-IY-J-xAwclyhjqV8a8r1_Aob5JFoymRVU_UoGMKfqygHy1QO-GttSy3lJ1lPthUCW8awv9FKviIqvWMtTf4LPyhtPBdu-9qedDiH-vU2eBD5EWOrhLPAkK2jPmNpm49m7Q-tJDNejV-VLI18OlRIU2OM35Iq7JFsRAtqgxE78FUblQqrm89v4d-RDgM2fAv623HzFETyK2AfN78eqzPCr5nUBnAXW4QqFy4dfYliFtCzwllyXAQxGnupY2eWxJindQRCv8kV7Fs3b9E09KZHoS_Io0kGs0o7kAtdIJwqIpdceBMBfFmoj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بونوس ویژه جام‌جهانی برای تمامی کاربران به مدت محدود
🎁
به مناسبت شروع جام جهانی، برای مدت محدود
۱۰٪ بونوس ویژه واریز
برای تمامی کاربران در نظر گرفته شده است، تا با قدرت بیشتری وارد پیش‌بینی مسابقات و رقابت‌های این تورنمنت بزرگ شوید.
🎁
این بونوس ویژه به‌صورت محدود و تا ساعت ۲۰:۳۰ امشب می‌باشد، که قابل استفاده برای تمامی کاربران سایت به‌همراه یک گردش پیش‌بینی با ضریب ۱.۸ ‌می‌باشد.
📌
برای ورود به وینکوبت از طریق ربات رسمی سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/133331" target="_blank">📅 13:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133330">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/133330" target="_blank">📅 13:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133329">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/133329" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133328">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
#فوری |دونالد ترامپ، رئیس‌جمهور آمریکا: ما امروز به جنگ با ایران پایان دادیم و این کشور توافق کرده است که هرگز سلاح هسته‌ای در اختیار نداشته باشد، چیزی که ما بر آن اصرار داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/133328" target="_blank">📅 13:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133327">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
فوری/ مدیران باشگاه پرسپولیس با ارائه مدارک مستند به afc خواهان رسیدگی به روند صدور مجوز حرفه ای باشگاه استقلال شدند. مدیران باشگاه پرسپولیس معتقدند فدراسیون در روند صدور مجوز حرفه ای دچار تخلف شده و خواهان حذف این تیم از آسیا شد/فارس
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SorkhTimes/133327" target="_blank">📅 12:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133326">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
حمله علیرضا نیکبخت به افشین قطبی: ذات خوبی نداشت؛ در قهرمانی پرسپولیس هیچ کاره بود! آن تیم را حمید استیلی و مرزبان قهرمان کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/133326" target="_blank">📅 12:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133325">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1vRffZ4X8gWOnhcwPhhj0v-HqciTJDCel7T6aK3mmgvAlfXA31o_yrcVLTOwK7J-CJVSLjATzJJl-DPoEZjenHcrJBV2gEcYdy07pqMidzwWzyM6QzDaCIsQQDBU9xRvR9MKjTb-P_iUhk7aPwQDvP_5z32cr-nHlZGo_x14ItaihPDZfzgXcT3jJhAANqfRV33tdscQou8mbPKR9aG0d8IBOHeOm_FLLLKTdk0tRcxdqgyg9DxcduaD3bqTzzcCtI9bRmka8WtJlMMnEPqTMYH8xtCpjznzKTr05wF_F2X5OjXYOLCS39CzA244EXspCTTGU0KpEocdOMutiyIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
محبی چرا با پرسپولیسی‌ها میپره
🧐
✅
پ.ن خبریه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/133325" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133324">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
فوری/ مدیران باشگاه پرسپولیس با ارائه مدارک مستند به afc خواهان رسیدگی به روند صدور مجوز حرفه ای باشگاه استقلال شدند. مدیران باشگاه پرسپولیس معتقدند فدراسیون در روند صدور مجوز حرفه ای دچار تخلف شده و خواهان حذف این تیم از آسیا شد/فارس
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SorkhTimes/133324" target="_blank">📅 12:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133323">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/133323" target="_blank">📅 12:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133322">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 226 · <a href="https://t.me/SorkhTimes/133322" target="_blank">📅 12:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133321">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/133321" target="_blank">📅 11:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133320">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
🎥
لحظاتی از یک روز پرکار در زمین تمرین؛ جایی که پرسپولیسی‌ها با انگیزه و تمرکز، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/133320" target="_blank">📅 11:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133319">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/133319" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133318">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/133318" target="_blank">📅 10:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133317">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
خلاصه دیدار
🇰🇷
کره‌جنوبی
2️⃣
🆚
1️⃣
جمهوری چک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/133317" target="_blank">📅 10:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133316">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇲🇽
🇰🇷
مکزیک و کره نصف راه صعود را طی کردند/ جدول گروه A جام جهانی پس از پایان شب اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133316" target="_blank">📅 10:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133315">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
‼️
باشگاه استقلال صورت مالی شش ماهه (۳۰ دی ۱۴۰۴) رو روی سایت کدال آپلود نکرده است. به این دلیل که مدارک مالی و شفافیت در بخش‌های مختلف باشگاه در راستای حرفه‌ای‌سازی از سال گذشته آماده نیست.
🚫
یکی از الزامات اصلی مجوز حرفه‌ای‌سازی است که حالا استقلال فاقد این…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/133315" target="_blank">📅 09:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133314">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNyiAAcg5m404pPmLxl7kZXWoDcXjw77YsBCPuPVElNV2qN8xVPETlj5vy-hrhroxa1s2F8pEdS8sP5h4_kC1la7nzXuKljPZFqOj19a3mDTf18Qc3BvtESY_DscdhlH_F1mR09oHeaLAhK3SK1hBr6GNMXWu8BZXDu63ELMmpo6s2PEBPAAITrB6iw7iLn5UMpLQEq_jSYDuW8Q0WkHBVnvA85uRWekJ6KA0geEtSmQUAoeUs0kRQsHyK2ZtnioDkaqzzvx0v5TgbvgfGrTDbE23YTfY5qztZQ5rfTC7kTeezSX1rHWEoyyOCutXL62wuZU00fyRNtSv9m9mx3xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🇰🇷
مکزیک و کره نصف راه صعود را طی کردند/ جدول گروه A جام جهانی پس از پایان شب اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133314" target="_blank">📅 09:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133313">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ed2nvvR-_TK3LOJOphJPESzmdYQz7OBfWL_Q2w1bTJlNELoonP7fWGnCCQ6LxjPlb5lEsm7MyOr5kXbeJTOHlyZ7wTO1fpQ2jG4wDO1kKh1aHBqfTL4XdScyrzlpGkRfVcklxlGGeV5zLsLjfbVGkZC_MvGeC5gutpS9jbnPdYAvUuhZpxCdAAiWxOVP_--_lEYAvKmZR91RQGKgceL-uMZo2TmAvmwfUkkfCduew0lvAsn4_TP2INoVr6KuIGQNIjnaysQRAoOi5ytjsODg61D-EUw5c3wiz3V2lqvD62EoNcexyBFUtcPPb_COx_f3pTA2DbeIizWsqwD6eZhKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بونوس ویژه جام‌جهانی برای تمامی کاربران به مدت محدود
🎁
به مناسبت شروع جام جهانی، برای مدت محدود
۱۰٪ بونوس ویژه واریز
برای تمامی کاربران در نظر گرفته شده است، تا با قدرت بیشتری وارد پیش‌بینی مسابقات و رقابت‌های این تورنمنت بزرگ شوید.
🎁
از همین حالا تا ۲۴ ساعت آینده ۱۰٪ بونوس ویژه روی تمامی واریزها به مناسبت آغاز جام‌جهانی که قابل استفاده برای تمامی کاربران می‌باشد به همراه یک گردش پیش‌بینی با ضریب ۱.۸
📌
برای ورود به وینکوبت از طریق ربات رسمی سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133313" target="_blank">📅 01:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
والیبال هم که زاییدیم و ست دوم هم باختیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133312" target="_blank">📅 00:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133311">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
ادعای واشنگتن پست: رهبران عالی رتبه ایران و ایالات متحده این توافق را پس از دیدار با یکدیگر در مقابل رسانه‌ها امضا خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/133311" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133310">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133310" target="_blank">📅 00:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133309">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133309" target="_blank">📅 00:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133308">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133308" target="_blank">📅 00:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133307">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
ترامپ: عملیات جزیره خارک از دستور کار خارج شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133307" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133306">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
والیبال هم ست اول و ۲۵ ۲۳ دادیم به بلغارستانیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133306" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133305">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
#فوری | نورالدین الدغیر خبرنگار الجزیره در تهران:
🔻
همه چیز انجام شده، چیزی باقی نمانده جز امضای توافق
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133305" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133304">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚩
خبرنگار: آیا رهبر ایران این توافق را تأیید کرده است؟
🔴
ترامپ:  تا جایی که می‌دانم پاسخ بله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133304" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
خبرنگار: وقتی این توافق امضا شود، آیا آمریکا فوراً محاصره را لغو خواهد کرد؟
🔴
ترامپ: بله، این بخشی از توافق است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/133303" target="_blank">📅 23:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133302">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
ترامپ : همین الان با نتانیاهو صحبت کردم‌..او باید با توافق موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133302" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133301">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2zRh3UnZUTC45PP_MTaodtT8a1k5Kp9L4TUbGCVauhfkvsfkkKkfTuNqaaMXX05igkREF1m9KRxFluxGW3eV9ellyN3Hn9laFfDLVdW-HHLiZiluQNEv2p-tlAgBrOqTxBmOpJZV-W4nwhbLxMK61OX4p_3rlA0nHnok610ZvqP59kj5iiJICldYZjI89xD0G41m6r_HnTsOT1V9-smQLMF1Pk4XHAHj2M8v0ZIITmzOiOD3-26OaU6BD4sbjL_RSh5UJAm0q92iok26UAHO19K14mjxV8KT4QKR9kXR4RzH5m6bVUtw9nSTWOiJ99_hNSwiC2Ao81Y56WeN3jKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
توییت بزرگ‌ترین صفحه ترول فوتبال : خدایا، خواهش می‌کنم، بذار این اتفاق بیفته چون خیلی خنده‌دار می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133301" target="_blank">📅 23:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
مبلغ رضایت نامه محمدمهدی محبی از سوی باشگاه اماراتی یک میلیونو دویست هزار دلار اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/133300" target="_blank">📅 23:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133299">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
بازی دوم والیبال ایران با بلغارستان هم شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133299" target="_blank">📅 23:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133298">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
ترامپ : همین الان با نتانیاهو صحبت کردم‌..او باید با توافق موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/133298" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133297">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
ترامپ درباره توافق با ایران: همه بسیار خوشحال هستند. کل خاورمیانه خوشحال است. و فراتر از خاورمیانه نیز همین‌طور.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133297" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133296">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
🇺🇸
ترامپ: توافق به دستیابی به توافق در روزهای آینده بستگی دارد و ممکن است امضای توافق ایران در اروپا انجام شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133296" target="_blank">📅 23:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133295">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb3074466.mp4?token=i1g9scXDZO9Mk21AQv93wLQ7pt6JYsMCqes1mfmrkaHObpHyMjpQfblII1-SvJ0VOArWo4ZvGjNEGVzas9V4ZXj4BsTgRFXirKmnVuJ8SKAWeYsFLef5NLDcDqJVB_J31W-CXk12yT1hKWESY5TlSmHJVs2d-a_l5dKQt_Rqw-kiJdQlOmdSqwxdhoiu23TyDGShqBUnv5ZFqQibICfjhFVDDPk73TDkZwIvvQlOKpybbH3xUIijLGjl4_NDdwsBHhTbb186A2Q07MUNCgyw584t3QXs67HOfWdHaBhXWNHZK0bszGYfdcCiXQg_5CzJAI3sSMd-ZNP-G6AGOagHkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb3074466.mp4?token=i1g9scXDZO9Mk21AQv93wLQ7pt6JYsMCqes1mfmrkaHObpHyMjpQfblII1-SvJ0VOArWo4ZvGjNEGVzas9V4ZXj4BsTgRFXirKmnVuJ8SKAWeYsFLef5NLDcDqJVB_J31W-CXk12yT1hKWESY5TlSmHJVs2d-a_l5dKQt_Rqw-kiJdQlOmdSqwxdhoiu23TyDGShqBUnv5ZFqQibICfjhFVDDPk73TDkZwIvvQlOKpybbH3xUIijLGjl4_NDdwsBHhTbb186A2Q07MUNCgyw584t3QXs67HOfWdHaBhXWNHZK0bszGYfdcCiXQg_5CzJAI3sSMd-ZNP-G6AGOagHkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول مکزیک به آفریقای جنوبی در دقیقه 9.
✅
اولین گل جام جهانی 2026 توووسط کینیونس زده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133295" target="_blank">📅 23:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133294">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
#فوری | منابع داخلی :
🔻
جمهوری اسلامی ایران پیشنهاد آخر آمریکا و توافق را قبول نکرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/133294" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133293">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
کانال ۱۲ اسرائیل: از توافق امریکا و ایران بی‌اطلاعیم و از اینکه رهبران ایران موافقت کرده‌اند ، متحیریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133293" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133292">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
👈
ادعای اکسیوس: منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/133292" target="_blank">📅 23:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133291">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">☄️
☄️
اولین بازی جام جهانی رسمآ آغاز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/133291" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcYiD0fPXeIKORLda9b-YzTXj6oEerSWvUHg30BTEmDTWhBAnii63h50iweRwdjQ6IkHe363YWdnW-rDxwimfxnReMWpies6cTErd8xpr4mMAwqa38ahiPOyJwLu_-aA7a9_ND4Y1HPVMdBeGBy3S1ldOym8OU9rbiCZGvyOprl7LTlQUrlZXbAl_E0a6rXlwZJ8ZvZcJSoRytiGlhXx8nZWXFyde78uCWyhdlY_fOi0zX4hEo3a_yjjjj34V9su0kp5t3vDl322xYxBsM92vZSQ3ISBqVHVcr17IYHJZ3sfLpZaGqLsGblPLTxsQZfNcCIbpXfl9yUoG9T24zsBxVcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcYiD0fPXeIKORLda9b-YzTXj6oEerSWvUHg30BTEmDTWhBAnii63h50iweRwdjQ6IkHe363YWdnW-rDxwimfxnReMWpies6cTErd8xpr4mMAwqa38ahiPOyJwLu_-aA7a9_ND4Y1HPVMdBeGBy3S1ldOym8OU9rbiCZGvyOprl7LTlQUrlZXbAl_E0a6rXlwZJ8ZvZcJSoRytiGlhXx8nZWXFyde78uCWyhdlY_fOi0zX4hEo3a_yjjjj34V9su0kp5t3vDl322xYxBsM92vZSQ3ISBqVHVcr17IYHJZ3sfLpZaGqLsGblPLTxsQZfNcCIbpXfl9yUoG9T24zsBxVcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقدام جدید در جام جهانی 2026؛ بازیکنان ذخیره هم در مراسم پیش از شروع بازی شرکت می‌کنند و سرود می‌خوانند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/133290" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
از امروز جام جهانی ۲۰۲۶ شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/133289" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llkLsY9G88RqQHR7jQqZhyIaZaep6VLQ7vJDiexyP2kURPZPtxKVDFdMlq2AwfGo0pn1iWtWbXcldsQAhdxmvUtQnerGB7BueMOaQzxZM7eUqKwXP3a5ZN_SGpoIUcei6UgojucG0ZvC9aXUqnGAX79G4ONCjimDEhNjGQSXvkiEWUHCll_qZnllYM9wdiTnr0CkJxluiNrV_W1_uIK2H-CI8izU-wxHSv_G0hBE8nJvkekF7n-r_6yzXzrybbXk8tMgjk8YC1Qf6S2wfFMNszcnMxycOq21E1weMsKHUmEeEkQIY5lTffF4JK5w1IQ0_T8dTm8oxTq9_IrxYwphsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این دیگه چه وضعشه...
🔴
تا باسن بازیکن های سنگال و چک کردن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/133288" target="_blank">📅 22:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133287">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/133287" target="_blank">📅 22:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
#فوری | منابع داخلی :
🔻
جمهوری اسلامی ایران پیشنهاد آخر آمریکا و توافق را قبول نکرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/133286" target="_blank">📅 22:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
معرفی تیم ملی ایران در مراسم افتتاحیه جام جهانی با نمادهای فرهنگی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/133285" target="_blank">📅 22:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/133284" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ac505c0c.mp4?token=s3NEue7GCts9zoWPBbbZyFtq96tyn6a-NnCeVBLrE0RVWijE8Yxb3zSiLFMpZa0AQJKuimu9c5T8MZfqITmAUn1eNPkDWTxBSd-EzIHTtxzyqoi3GxT0QRwAByA8R73au8ZsNZZtd-q484nUyGkVK8Xi1CqsqGCoFyge3om_ax1BBUqex5nplN4CtNLSayt5jtW7jdFUpjO0ZJ5h99BwJfxvKRDO4GLX5UcuPnmINIwXYKbyXVuLhSOPSsKllTAwqT4VOhqZ0GffOVarwB_a2gNGKPpcYUFzLkWJfoddwFVgM04Cb5pVNgl-LieCOvS_7IbQyRe32jAg2lI78IIZa1i_wcCclmmtjqAlw381ix41EWgiAMxJZxgYrit2FievCtZDBbBqCPI0-36ZjR7zJHe7-cvhMHBBzuC8yy6ODIr7bjRe5mFkvFoCGUthCXCUH-08G7ChwVjFgsnVE60jiq4vLKBDSMEVWd1KGbaN3-NCQn4b8j6EIsWhWY2Ncktat--h1oR5alyNGwRRjQx_qmrw2kg9M_U9j0fbSmOsqIY4t4RDqo0qa6oGpjJHyr7rvJhtrYJ1HhB3hoT-zktxyc8Cctg3ZysVTySfyvxbwG1u0hj54WtLsv7cNAL3hfl0FZoK0WjVaAxCXR839cVlvqHErKpb3lJ9Ub2WGzdHmw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ac505c0c.mp4?token=s3NEue7GCts9zoWPBbbZyFtq96tyn6a-NnCeVBLrE0RVWijE8Yxb3zSiLFMpZa0AQJKuimu9c5T8MZfqITmAUn1eNPkDWTxBSd-EzIHTtxzyqoi3GxT0QRwAByA8R73au8ZsNZZtd-q484nUyGkVK8Xi1CqsqGCoFyge3om_ax1BBUqex5nplN4CtNLSayt5jtW7jdFUpjO0ZJ5h99BwJfxvKRDO4GLX5UcuPnmINIwXYKbyXVuLhSOPSsKllTAwqT4VOhqZ0GffOVarwB_a2gNGKPpcYUFzLkWJfoddwFVgM04Cb5pVNgl-LieCOvS_7IbQyRe32jAg2lI78IIZa1i_wcCclmmtjqAlw381ix41EWgiAMxJZxgYrit2FievCtZDBbBqCPI0-36ZjR7zJHe7-cvhMHBBzuC8yy6ODIr7bjRe5mFkvFoCGUthCXCUH-08G7ChwVjFgsnVE60jiq4vLKBDSMEVWd1KGbaN3-NCQn4b8j6EIsWhWY2Ncktat--h1oR5alyNGwRRjQx_qmrw2kg9M_U9j0fbSmOsqIY4t4RDqo0qa6oGpjJHyr7rvJhtrYJ1HhB3hoT-zktxyc8Cctg3ZysVTySfyvxbwG1u0hj54WtLsv7cNAL3hfl0FZoK0WjVaAxCXR839cVlvqHErKpb3lJ9Ub2WGzdHmw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عادل:
❗️
دیبالا چقدررر خوشتیپ بود.
خیلی خوشگل بود
😂
😂
🔴
نکونام:
خوشگل و جذاب هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133283" target="_blank">📅 22:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVyCLj7oaNeyePC4gurp0cpxEAxQrOTYrJLABDGBB5ZzrYz4GJW08_5E-TdGmRmVXukhbCXuFMTLpLf5KKwsDP02skBdwuETdKpm1n58u5c0i7sYJRT8LjNp8A-Bsqsuo1p9_PeiJBFnnBWaLx2BY4AqzQl4CUO7DB1AZGAz-Djt7b9UYCdN_bCgB9I8RrnLVafq_boRW9ivW8Gd72X0kC5WkXnBq1w30SLgpUXvafJ3wErl_Iy6TUAaw3fB9AUGWZtL1FvMJKKIR1trWx69cO2w00wk1JgYvxpKxF9LIuSHs1_aWKO4uxIStOTLdOGnQhKC6lkLseOIprqazfnHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133282" target="_blank">📅 22:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
#تکمیلی | با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران ارائه شده و مورد تأیید قرار گرفته است، من به عنوان رئیس جمهور ایالات متحده آمریکا حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/133281" target="_blank">📅 22:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
#فوری | خبرنگار نیویورک پست:
🔻
ترامپ همین الان به من گفت که توافقی با ایران "تقریباً کاملاً نهایی شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133280" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
🎥
لحظاتی از یک روز پرکار در زمین تمرین؛ جایی که پرسپولیسی‌ها با انگیزه و تمرکز، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133279" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133278">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
#فوری |  | ترامپ :
🔻
من، به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران را امشب لغو کرده‌ام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133278" target="_blank">📅 21:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133277">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
#تکمیلی | با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران ارائه شده و مورد تأیید قرار گرفته است، من به عنوان رئیس جمهور ایالات متحده آمریکا حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/133277" target="_blank">📅 21:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133276">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
پست ترامپ از اولین بازی جنگ جهانی  امشب تا پاسی از صبح همراه با صرف موشک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/133276" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133275">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp5lYrERrPY7Z3nhRRQwjRjMfhDdqhjixjg5HraV1cH1CK-IRiq58-WLs2il0BRjNIiD_WrOpmjfWVUkI16cvVoesSA9oetV-E5PeuJisP5Lp4tjMJJ4roPVtJyrMOUvuTH3Fx_Zx29cR-7D7a2XOABbwKgqJPUkI93LazAGflNRHP0xlKL4LObxB5x04F5DujxHj46ic0IAyHzU_NY8vh5n0_Ia71rJvj22HlG86b7TqwKu4hrUISjF1xJNyzJiqW7v3WgT04P5-Yv7XDc6qEYN4cvO6LF3mOAFthvLcNaBT35wxzcsz4nIGRK2teuRiGq6To2Eyzl_wDwHi7V7tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
دیدار افتتاحیه جام‌جهانی ۲۰۲۶
[
مکزیک
🇲🇽
🆚
🇿🇦
آفریقای‌جنوبی
]
⏰
امشب ساعت ۲۲:۳۰
🏟
استادیوم مکزیکوسیتی
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133275" target="_blank">📅 20:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133274">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
داستان پیچیده سهمیه آسیایی همچنان ادامه دارد!
🔻
در حالی برگزاری تورنمت سه جانبه میان پرسپولیس، چادرملو و گل‌گهر در هیات رئیسه فدراسیون فوتبال به تصویب رسیده و  اعضای هیأت‌رئیسه فدراسیون فوتبال به اتفاق در مصاحبه‌های خود درباره برگزاری تورنمنت سه‌جانبه صحبت…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/133274" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133273">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98745e731.mp4?token=i-pH8OmYAxbXLNM8U41s0hIiJHClGzNC7p2I1YDl7h2zJTVQ-VaeHIHQDV_HNdekbSxh01EYoF2OWe1zXVe5QaAIwi4hEzkVWEUugRCXRjywTvOc6W6_vIV47OFQCyQ6Cbj4X4vwuIMktJpcte4tow4vJ7Wps0IL8L_qpuwkQW1eIRBxQtpJSVxR9elnwzW9d58CbtQMlCFYbaSlViqcy82pKHuhUZv5vdJguwZTNoG10QOH6hyLSTGyyJHSSUw7PZWhR4pZZyYcJpTHzv5qoOhUjd_aZawmJiIfCw-XvCZwoLfchWNuK4B64bYpwBnYW75TxvVbE3OVV1zzJRLH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98745e731.mp4?token=i-pH8OmYAxbXLNM8U41s0hIiJHClGzNC7p2I1YDl7h2zJTVQ-VaeHIHQDV_HNdekbSxh01EYoF2OWe1zXVe5QaAIwi4hEzkVWEUugRCXRjywTvOc6W6_vIV47OFQCyQ6Cbj4X4vwuIMktJpcte4tow4vJ7Wps0IL8L_qpuwkQW1eIRBxQtpJSVxR9elnwzW9d58CbtQMlCFYbaSlViqcy82pKHuhUZv5vdJguwZTNoG10QOH6hyLSTGyyJHSSUw7PZWhR4pZZyYcJpTHzv5qoOhUjd_aZawmJiIfCw-XvCZwoLfchWNuK4B64bYpwBnYW75TxvVbE3OVV1zzJRLH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کمتر از ۳ ساعت تا شروع جام جهانی؛
درب‌های ورزشگاه تاریخی آزتکا مکزیکوسیتی برای ورود هواداران باز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133273" target="_blank">📅 20:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133272">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G84qF8uwgJ-DqsPN3eL2MbCPkNT3luk4Mkvkq7PiXrQ6w8rK5UjWgGs7t-Ci4Q4-__kUqSyYq6XRHVBqoSwREbQZuy5BmycBowKhFlJqAppzmgkNqeLffn5jPtiEFmSbdxxbzf94bUIYdANiDNS6PPPPxWWGkCsrryi_8awWVaM_AUk40ON8-G2xVbWqUWq6aeK6eTep1Ob4AnXLZ4HYBIJBfY9Iq9fN480RExZvmVnnAsps05cfyINaiYrGgc18qmR5fj0b74933WK9sgCh33SbvX4hpV9T9o3SxaoREHXdQ_8jDCK_dQYBOHwJicmkuYmqdjLq_ME4rh3jy-7vvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کشورهایی که هوادارای اونا حق حضور در آمریکا برای دیدن مسابقات
#جام‌_جهانی
2026  رو ندارن!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/133272" target="_blank">📅 20:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133271">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgutFXRg0mfPKzhl2ShhQR841oGCLnqk_VjETOGqJUrGWazXseedMtAtj311lbTtvN0nebObYxp2MWYFl3Y5emkH0dmzxJZUO80mwI7pd9wIebqd1UjTvpSh-x5rWvhG5YxEq6le_sQxzwRvUUARuFYPBQ_H3KaF65OT5OxDmCAmP-zWnrsfMsRXgeUKIkUMRMMa3eoJWkGXh-nNXnxPmA_FeTA8RNXFqMaJHERtWCaOvDLfRckYitGlf3E4My8IqXYDct2BLpWBTzNOM5_bzwE3cln-lP-Rw3rcstJoex2bT1c79IcUDh2yF2OVGX9vndmhDdXaGOduPwfVVoX0vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست ترامپ از اولین بازی جنگ جهانی
امشب تا پاسی از صبح همراه با صرف موشک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/133271" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133270">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
کاپیتان عالیشاه: بدترین کار ممکن الان انجام میشود مثلا ما تمرین میکنیم اما یکسری تمرین نمیکنند
🔴
ما نمی‌خواهیم سهمیه آسیا را گدایی کنیم این نوع سهمیه اختصاص دادن خوب نیست و باید در زمین مشخص شود زمان برگزاری بازی‌ها بود و راحت‌ترین کار ممکن برگزار نشدن بازی‌ها…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/133270" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133269">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
ورزش سه: مهدی ترابی مصدوم شده و ممکن است لیست تیم ملی تغییر کند و از بین هادی حبیبی نژاد و امیرحسین محمودی یک نفر مسافر جام جهانی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/133269" target="_blank">📅 19:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133268">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
گفت و گو با محسن خلیلی در حاشیه تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133268" target="_blank">📅 19:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
گفت و گو با محسن خلیلی در حاشیه تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/133267" target="_blank">📅 18:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133266">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
اوسمار فردا راهی ایران می‌شود
❤️
❤️
محسن خلیلی:
🔴
باشگاه پرسپولیس بلیط پرواز اوسمار ویرا برای حضور در ایران را برای او فرستاده و قرار است او فردا جمعه عازم ایران شود.
🔴
او به همراه کادر خود عازم ایران خواهد شد تا تمرینات پرسپولیس را زیر نظر بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/133266" target="_blank">📅 18:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133265">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❤️
❤️
محسن خلیلی:
🔴
برنامه فوری فیفا همواره اعلام کرده باید بازی ها برابر باشد و عدالت رعایت شود
🔴
در لیگ ما بازی ها برابر نبوده و این عدالت نیست
🔴
اینکه بگوییم شرایط برای برگزاری بازی ها بود بماند
🔴
انتخاباتی باید صورت گیرد که شرایط همه با هم باید در نظر گرفته شود
🔴
دیروز جدول ای اف سی اسم گل گهر را گذاشته بود و ما اعتراض کردیم
🔴
ما دنبال عدالتیم و می خواهیم بازی ها داخل زمین انجام شود
🔴
چطور این قدر سریع سه نماینده به آسیا معرفی شدند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/133265" target="_blank">📅 18:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd56fa69a.mp4?token=utZSJLe_UeewHIFBDntgAkTHLSzxOaAIBlGQd9vfV9CBxPR7ZbmwBuNrxkivYTLqtxWzpR4a17bjpb3izah1CI9Oe4N13pLcdsiSwTOvkp3M2AZkmj6YrD26pjHGlIGwOw2Op1GJg3MTmtpdrm0Xnpty1w-K8pY2p0dKvYimotmYFEVC6Xxy3ycrICWN2cFL43mb-Lvi1Ys2ar7OW3Pri0nibEMnewRc8p_2MAyOr_QD9wpk8_vFkeUT1-h75zkO8mqdCXmMdWeZyrowL8AmS0i9S_eOmwUeRqE01_iQ-yqmlJU4tmj_FT10eIeUPDg9Q8bk2Ok5LSYt-qwwLuE1ZUVncg-TcLIPn7eGy-6PacWDfqUMg92-YMq8VFf7V9bn2Ly8xmctLvWDk8fFTG5Qa4VmoMs2F66GGgqFKWIL7N9CkakM6vGh6a9sxkf2syWWkxE55DDoE4bRqrCurIRz0AHMKc3iMYFd7T88tU5pE6DwSCUvuUStsPXdf0turiLGaLaHAMJWJ30W0lJI5BcHrqBMAaVvr7tuUGhfVH-h4AVA-mReZUzP5fDMQJY78bu8mTliJO6LCmZLN6zKFTUGMmlyRhnjgI9qvrFbAKNuwQqNHCD9VKSYPAKn0TH0QjD9WiW54dOMoFP5_5mpBIguJAxgXwIf_STRr_lJs-dOUlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd56fa69a.mp4?token=utZSJLe_UeewHIFBDntgAkTHLSzxOaAIBlGQd9vfV9CBxPR7ZbmwBuNrxkivYTLqtxWzpR4a17bjpb3izah1CI9Oe4N13pLcdsiSwTOvkp3M2AZkmj6YrD26pjHGlIGwOw2Op1GJg3MTmtpdrm0Xnpty1w-K8pY2p0dKvYimotmYFEVC6Xxy3ycrICWN2cFL43mb-Lvi1Ys2ar7OW3Pri0nibEMnewRc8p_2MAyOr_QD9wpk8_vFkeUT1-h75zkO8mqdCXmMdWeZyrowL8AmS0i9S_eOmwUeRqE01_iQ-yqmlJU4tmj_FT10eIeUPDg9Q8bk2Ok5LSYt-qwwLuE1ZUVncg-TcLIPn7eGy-6PacWDfqUMg92-YMq8VFf7V9bn2Ly8xmctLvWDk8fFTG5Qa4VmoMs2F66GGgqFKWIL7N9CkakM6vGh6a9sxkf2syWWkxE55DDoE4bRqrCurIRz0AHMKc3iMYFd7T88tU5pE6DwSCUvuUStsPXdf0turiLGaLaHAMJWJ30W0lJI5BcHrqBMAaVvr7tuUGhfVH-h4AVA-mReZUzP5fDMQJY78bu8mTliJO6LCmZLN6zKFTUGMmlyRhnjgI9qvrFbAKNuwQqNHCD9VKSYPAKn0TH0QjD9WiW54dOMoFP5_5mpBIguJAxgXwIf_STRr_lJs-dOUlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کاپیتان عالیشاه: بدترین کار ممکن الان انجام میشود مثلا ما تمرین میکنیم اما یکسری تمرین نمیکنند
🔴
ما نمی‌خواهیم سهمیه آسیا را گدایی کنیم این نوع سهمیه اختصاص دادن خوب نیست و باید در زمین مشخص شود زمان برگزاری بازی‌ها بود و راحت‌ترین کار ممکن برگزار نشدن بازی‌ها بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/133264" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133263">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b0d9daf7.mp4?token=nYVo1Mk_WsyJOyymrdVS55Ph4MnL9Tn-JkegMgSaXtSDSDL4csdXQGuCYlmjbf1AVTEd4bvKsNhoj_XpTvq4Vpjw3b2UDGI-D6wZGJDyv7NJtPrps3CR8KsMnz6TKvGBPCuyM8CMvN7eilnn-j7YUg5GY9Oyl-SMJ3Gkv0yikDCFEdd8KgWnxwJraKAzAJTM5tkhAuIYbhwxaM_o9VzMvUDRY1n9WIW-OGEIYhsMpBf3KFVrshluel-wzo8Rps1GXRm_XDrcAqpV5IOfFpqECNTNftQrXYKF3M0gdzX1PINQ2sTTqNAJefKg7bUds6e7j-V1FhMr42JtU02_zNY1nLShUxT2d1ZzGDsdDzFtSsomlPLEiRjQcFTcIdkZ4lZZ8MlYdvMpF7amz6MMtHX1e_Wu8gZlr9GYYkzQqlR9S7kkqDmpQZcG_xX_nirUyjQT_Posp1m5WyqOapaDpTJnS5C2lBTdGfpVQKqjqKEloLVWH4H8Jidk53KiFG6W1nqaghojdVaJhqn9nBufyaNdFnGKeOwSUJ1dZPs74EEq5hTvHLr2z9ZrnalTjmyJqjD-fw-PUtsmZ-4trnXczBl1i71FgB3vX-f9QWrakeIaXy_eAmEdGUObwM1lXkQP8r6ExlakgIVY3x_RIDkit_Go14FjnVo65qafpLttlAMEppQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b0d9daf7.mp4?token=nYVo1Mk_WsyJOyymrdVS55Ph4MnL9Tn-JkegMgSaXtSDSDL4csdXQGuCYlmjbf1AVTEd4bvKsNhoj_XpTvq4Vpjw3b2UDGI-D6wZGJDyv7NJtPrps3CR8KsMnz6TKvGBPCuyM8CMvN7eilnn-j7YUg5GY9Oyl-SMJ3Gkv0yikDCFEdd8KgWnxwJraKAzAJTM5tkhAuIYbhwxaM_o9VzMvUDRY1n9WIW-OGEIYhsMpBf3KFVrshluel-wzo8Rps1GXRm_XDrcAqpV5IOfFpqECNTNftQrXYKF3M0gdzX1PINQ2sTTqNAJefKg7bUds6e7j-V1FhMr42JtU02_zNY1nLShUxT2d1ZzGDsdDzFtSsomlPLEiRjQcFTcIdkZ4lZZ8MlYdvMpF7amz6MMtHX1e_Wu8gZlr9GYYkzQqlR9S7kkqDmpQZcG_xX_nirUyjQT_Posp1m5WyqOapaDpTJnS5C2lBTdGfpVQKqjqKEloLVWH4H8Jidk53KiFG6W1nqaghojdVaJhqn9nBufyaNdFnGKeOwSUJ1dZPs74EEq5hTvHLr2z9ZrnalTjmyJqjD-fw-PUtsmZ-4trnXczBl1i71FgB3vX-f9QWrakeIaXy_eAmEdGUObwM1lXkQP8r6ExlakgIVY3x_RIDkit_Go14FjnVo65qafpLttlAMEppQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
رضا شکاری: باشگاه پرسپولیس هیچ وقت سهمیه را گدایی نکرده است؛ما مطمئن هستیم با برگزاری بازی‌ها می‌توانیم به آسیا برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SorkhTimes/133263" target="_blank">📅 18:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133262">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf92abe2e.mp4?token=f6MsJynYG898-Wjs9EZBoWT_xRjDsHHMCHSufcKjp-eUYpOINzlFZCQunVW8aMAEggfy7GVox4kRtQNy3zXCN9qNH4LApApczVQnJD79_9GLr5fSusmEy-PFEKrJDJL4dG23iitPyL5UU8V0xPFF_leG0WcCM5wi6H1gu50L3KUBz7392SO0YK2t3Mr3k2EbzqwSCs2P3kQEPmqiRFNESCj71qy8o6uF2VzJxZrD5eHEw69c8tnMrGQj_h-_PtnuwxyIiQNoZdNopd2yhLTjj9U664IwNPBVkG0CcONWROK5AfvuqRW4PQfVK6_VMSQNHhTjag9Xs_0yp6ifJXxLDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf92abe2e.mp4?token=f6MsJynYG898-Wjs9EZBoWT_xRjDsHHMCHSufcKjp-eUYpOINzlFZCQunVW8aMAEggfy7GVox4kRtQNy3zXCN9qNH4LApApczVQnJD79_9GLr5fSusmEy-PFEKrJDJL4dG23iitPyL5UU8V0xPFF_leG0WcCM5wi6H1gu50L3KUBz7392SO0YK2t3Mr3k2EbzqwSCs2P3kQEPmqiRFNESCj71qy8o6uF2VzJxZrD5eHEw69c8tnMrGQj_h-_PtnuwxyIiQNoZdNopd2yhLTjj9U664IwNPBVkG0CcONWROK5AfvuqRW4PQfVK6_VMSQNHhTjag9Xs_0yp6ifJXxLDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور باکیچ و گرا در تمرینات پرسپولیس
✅
تمرین تیم زیر نظر کریم باقری در حال پیگیری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/133262" target="_blank">📅 18:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133261">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
اینطوری که فرهیختگان گفته باشگاه به علیپور گفته فصل بعد کاپیتان اصلی هستی این یعنی جدایی سروش و امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/133261" target="_blank">📅 18:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133260">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a69b9d7d1.mp4?token=DCs-sg80zm8MyF1naGtwVu4Jaq2vctWysyEQbZnmtdZjAYCzDPzb1rEVD6kcALFtOrX9-3InjD_gaNbS9rmV5orwh8qlpYIBenLCV0E9k0Aji_66I20Fq9cwxjecH78HoYUa0BdF9uJBrRGGaWj5iTvMfJ92MgraP66wLL7UpqU7KO15KvqP_rsIqrpCubrc1zq6TCg9ARdzeU7MgJetgSIopzPnjWTlukI2ecLcHkE7T3Z6kd-XHDoFszLnRgxYysqhXkGwAiSMWVoanY014i_Ox7ywt44jmVi7iRijzdhHM8G9or_gh11TJJi8yr3WwFuJO3aUPTgKZoCRxTlZZil_ZpL1_lrzzPPFJMnBk7b-z_d3nIw5lRcbnDuHrQDGjsNfxRK_67bCAFZOD3R_snP7UJLMOvUEN51_FVmF6s0lhtUKgxMVr4qqlp_n51AdrkRInTikNqb9iYbzBI5qqjtqNrU2DA87iUcYcSmullEjgZ7OqujNrAOWhpegUhXVbbO442a-AmLJpLtTuzYMlnZNRtU5PrmLHgDInwdmZe5xYL9a6Hs9s2ph_1V4QG-4Yp06LUdR5CZN9bvdl4VDVeUMPEDDMmRHqzhTKwzgfD6xf0ye-ghQbf2FF-_MNoJj9uTnYA0TNKLN1z3OXZNaZkn4Sl2yNAxNkwn2DdAmJyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a69b9d7d1.mp4?token=DCs-sg80zm8MyF1naGtwVu4Jaq2vctWysyEQbZnmtdZjAYCzDPzb1rEVD6kcALFtOrX9-3InjD_gaNbS9rmV5orwh8qlpYIBenLCV0E9k0Aji_66I20Fq9cwxjecH78HoYUa0BdF9uJBrRGGaWj5iTvMfJ92MgraP66wLL7UpqU7KO15KvqP_rsIqrpCubrc1zq6TCg9ARdzeU7MgJetgSIopzPnjWTlukI2ecLcHkE7T3Z6kd-XHDoFszLnRgxYysqhXkGwAiSMWVoanY014i_Ox7ywt44jmVi7iRijzdhHM8G9or_gh11TJJi8yr3WwFuJO3aUPTgKZoCRxTlZZil_ZpL1_lrzzPPFJMnBk7b-z_d3nIw5lRcbnDuHrQDGjsNfxRK_67bCAFZOD3R_snP7UJLMOvUEN51_FVmF6s0lhtUKgxMVr4qqlp_n51AdrkRInTikNqb9iYbzBI5qqjtqNrU2DA87iUcYcSmullEjgZ7OqujNrAOWhpegUhXVbbO442a-AmLJpLtTuzYMlnZNRtU5PrmLHgDInwdmZe5xYL9a6Hs9s2ph_1V4QG-4Yp06LUdR5CZN9bvdl4VDVeUMPEDDMmRHqzhTKwzgfD6xf0ye-ghQbf2FF-_MNoJj9uTnYA0TNKLN1z3OXZNaZkn4Sl2yNAxNkwn2DdAmJyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
مرتضی پورعلی گنجی، مدافع پرسپولیس: پرسپولیس در یکی دو سال اخیر با چالش هایی روبرو شد
⏺
بازی نکردن در ورزشگاه آزادی به ما ضربه زد. از وقتی آزادی را از پرسپولیس گرفتند به مشکل خوردیم. هر وقت در ورزشگاه آزادی برگزار کردیم به سمت قهرمانی رفتیم. بازی های فصل قبل دست به دست هم داد عواملی که نتیجه نگیریم
⏺
هواداران همه چیز را کنار هم بگذارند و بدانند چرا نتیجه گرفته نشد. باید تصمیمات درست تری برای تیم هایی مثل ما گرفته شود. تیم ملی؟ از سوال در این مورد باید بگذرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/133260" target="_blank">📅 18:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 194 · <a href="https://t.me/SorkhTimes/133259" target="_blank">📅 18:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133257">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBqokCg7jlJAvjQ0XcjcFhKqhwkBQVq1L1q1_hqJEmg7KBuD91SU4-KKvIQd_VGqg2deZiZQaQaMjwXYMNL7o03C1ZFvPMlC13Jibz5Aci-4s9yMRcHxbZeTyUjXXOfqRCMBv7DUGGoPUc6SjtHkXWImTgz4cDdbAhAGNF2_VuePAaW-p67GjZoQiNtVwMoFbEwRibR7RxCARn147VS4BeOeP9V3K1edliMODTvvTeSul8IkJIkjd-Ed4gjr9mevTQ7PthCtiz1pA00nhojIsYV7YMy7FgGgLVfUJVjZ3Owu5XHVpue5S9-PJMLIPQNAZbEMI5NvkDniDwRRMyGyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
رای دادگاه صادرشد؛ حبس ۲ دوومیدانی‌کار ایران در کره‌جنوبی و تبرئه ۲ نفر دیگر
🔻
حکم دو دوومیدانی‌کار ایران که در پرونده اتهام تجاوز به دختر کره‌ای در این کشور زندانی شده‌اند، پس از بررسی در دادگاه تجدید نظر، تایید شد.
🔻
دادگاه تجدید روز گذشته برگزار شد وبر اساس آن حبس ۴ ساله دو نفر از ورزشکاران تایید شد.
🔻
دو نفر دیگر هم تبرئه شدند و می‌توانند به کشور برگردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/133257" target="_blank">📅 18:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
لحظاتی از تمرین عصر روز گذشته پرسپولیس؛ پرسپولیسی‌ها با تمرکز و انگیزه، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133256" target="_blank">📅 17:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
فوری/ ترامپ: اگر ایران نتواند توافقی را امضا کند، به شدت بمباران خواهم کرد‌‌. هواپیماهایمان را بر فراز قلب تهران پرواز می‌دهیم. آن‌ها ۴۷ سال قلدری کردند.   پ.ن امشب میاد سراغ تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/133255" target="_blank">📅 17:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
فوری/ ترامپ: اگر ایران نتواند توافقی را امضا کند، به شدت بمباران خواهم کرد‌‌. هواپیماهایمان را بر فراز قلب تهران پرواز می‌دهیم. آن‌ها ۴۷ سال قلدری کردند.   پ.ن امشب میاد سراغ تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133254" target="_blank">📅 16:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
فوری| ترامپ: آمریکا امشب هم به ایران حمله سخت می‌کند  پ.ن خسته شدیم دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/133253" target="_blank">📅 16:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
دیشب شب سختی بود .آمریکا تقریبا همه جارو زد ...امیدوارم حالتون خوب باشه .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/133252" target="_blank">📅 16:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133250">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
سردار آزمون: حقم بود که در جام جهانی باشم.  من ایرانی ام و کشورم را دوست دارم و بخاطر همین ناراحت هستم. می‌توانستم کمک کنم اما دعوت نشدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133250" target="_blank">📅 16:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133249">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
مجتبی پوربخش از تدریس در دانشگاه آزاد منع شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133249" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133248">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
اوسمار ویرا جمعه در تهران؛ شنبه در تمرین
🔖
بلیط اوسمار ویرا امروز رزو و صادر شد و او روز جمعه ساعت ۱۱ صبح به استانبول می رسد و روز شنبه هم در تمرین خواهد بود
🔖
اینکه اوسمار برای بازگشت مردد است از سوی نزدیکان سرمربی پرسپولیس تکذیب شد.برخی رسانه ها هم مدعی…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/133248" target="_blank">📅 15:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133247">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
سوشا مکانی دروازه‌بان سابق تیم های پرسپولیس، صنعت نفت آبادان، فولاد و... به اسگاردستراند در لیگ دسته سوم نروژ پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133247" target="_blank">📅 14:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133246">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
رویترز:
✅
با اینکه ایران و آمریکا هر شب دارن همو میزنن ولی بازم درحال مذاکره برای یک توافق اولیه هستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133246" target="_blank">📅 14:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133245">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🔴
رضا کرمانشاهی از باشگاه پرسپولیس جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133245" target="_blank">📅 13:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133244">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3B00B4B7dayyeomGbiFhZ7BPfHQsyIB2kBNiP8Xg56YogQm1m5DYbRP5kfwG1wdb7nJrYBydUkRKflo6ziLRENZqU3PzrjL_0eRTRv-XmtpKj3u6bd3TyP6jzXyOHqzHdsORVGaJLVtBJQNIMsDPia4iIrI0wuzz660DvGmxgC9tziilFVn683ezbobH01NF_2j1VkWliEit_XUn-xGYMnijtsD_H6gpTHVTvi5JIQ1W3lrkB6pvr04B0ZfKU2W5pFq_WUDUvsVNjm9ZftuFXvbxLhbvGK1ey87t7238BrFuUXeNHUp4esIpE9mQsqsL5n3vmDgOShGaI08IZIvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
شمارش معکوس تمام شد!
🏆
امشب با دیدار افتتاحیه بین دوتیم
مکزیک
🇲🇽
و
آفریقای‌جنوبی
🇿🇦
رقابت‌های جام‌جهانی ۲۰۲۶ آغاز میشود، همین حالا وارد سایت شو و
دیدارهای جام‌جهانی رو با بیشترین آپشن و بالاترین ضرایب در اسپورت‌نود پیش‌‌بینی کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133244" target="_blank">📅 13:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133242">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
ممبینی، دبیر کل فدراسیون مصوبه تورنومنت سه‌جانبه هیات رئیسه فدراسیون رو به AFC ارسال نکرده و برای همین AFC بدون اطلاع از این موضوع گل‌گهر رو بعنوان نماینده سوم معرفی کرده///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133242" target="_blank">📅 13:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133241">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
ترامپ: اگر ایران توافقنامه رو امضا نکنه، امشب هم به بمباران آنها برمیگردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/133241" target="_blank">📅 12:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133240">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
محمد مهدی نبی مدیر تیم ملی، هدایت ممبینی دبیرکل فدراسیون ، مهدی خراطی مدیر اجرایی تیم ملی، سیامک قلیچ خانی مدیر رسانه ای ، محسن معتمدی‌کیا مدیر روابط عمومی و یکی از آنالیزور های کادرفنی به همراه افسران أمنیتی تیم ملی موفق به دریافت ویزای…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133240" target="_blank">📅 12:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133239">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
هافبک پرسپولیس به استانبول رسید؛
✅
باکیچ امشب در تهران
🔻
باشگاه پرسپولیس برای بازیکنان و مربیان خود بلیت برگشت تهیه کرد تا آنها یکی یکی راهی تهران شده و در تمرینات سرخپوشان برای تورنمنت سه جانبه‌ای که در پیش است، شرکت کنند.
🔻
در همین راستا مارکو باکیچ امروز…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133239" target="_blank">📅 12:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
فرهیختگان: آریا یوسفی، علیجانوف و صادق محرمی گزینه‌های پرسپولیس برای دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133238" target="_blank">📅 12:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133237">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
🔴
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
🔴
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133237" target="_blank">📅 12:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133236">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il5dsN-Wep80uTIBo2mX0PQqzeiUVHH38kNGcgGftgTMWL8EYMWDLmgxTM9eBNkoCXlc70UkLCSDAepHqR-dv0WCUHZfPiKeWJZLAtcvwnt2n80pm2vB5oe80j7Q_pFCXNpIjaDlQ2QGa3-EasNAgDQznIoA35OMByKbfRgjZSb-GYarxdN5pC0_QNU3NtB8vxs6EG3kjovuMhczrh6SuZVBXZc9wj82X_qkdBdc3qxVG1TWgdHmfHiOYRyQg4fB-ftv8OfMfz3Vs-eSOc7IKaJXFswZCa_Q6LOZz4enLJ4bYiWz__9kZcui9mWTderLA0Yr-bIf5lbEEn2uerFB6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
منهای ورزش
⏺
یه زن ۲۷ ساله که معتقد بود با خوردن فقط میوه میتونه یه زندگی سالم داشته باشه امروز فوت کرد.
😞
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/133236" target="_blank">📅 12:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133235">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
🔴
وحید امیری پس از پشت سر گذاشتن مصدومیت طولانی، به بازگشت نزدیک شده و می‌خواهد با حضور در تمرینات پرسپولیس به شرایط مسابقه برسد. او در تمرین اخیر حاضر شد اما به احترام کادر فنی، جداگانه تمرین کرد. امیری برای شرکت در تمرینات گروهی منتظر موافقت اوسمار ویرا…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/133235" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133234">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚡️
23 ساعت و 55 دقیقه دیگه جام جهانی 2026 رسما و شرعا آغاز میشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/133234" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133233">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇮🇷
✅
🇺🇸
فوری به نقل از صابرین‌نیوز: هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/133233" target="_blank">📅 09:11 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
