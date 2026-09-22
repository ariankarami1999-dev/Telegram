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
<img src="https://cdn4.telesco.pe/file/h96nGzkQy63eRxG3JAWldUtC2NgiS2k6G2yVQfNR2JZNncjS-ItERj74JEQiXNNEA7_Lgmm36whuIAA5aR6HPrDMEuVVNlrACQk4Qkg7UpvTWejmxe1WQOsz6Ai2QdZm29nkluePeYL6bN4ewO6MA2KLZLp9LMb6S9mXqPRe9XFYamHbtTomtSF7_43tekxkSrN_aR1PxgLBpWH0U_4yI3TBAdEZFthqnkAIq0LSxLuPfsbtQACAlx4rPsksaGvcKuw0x9ppfLKIdmTB8Fz4O5vWqDX7vSnW-f3fH2eg4Y_o_416eLqibJSz0FNxs3h2Vxs6BVMQir4TCaKp0miN2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 08:42:09</div>
<hr>

<div class="tg-post" id="msg-140381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsCrWojCXdiB6dg787rAYoHbcD7bBrvUGUK-D6sqvbrUexXgyCimyPnU_WAYJ5t6-k6kX7ECRGwRgHo9mu-x88V4XrdqVV5BVbUGzusnTTTg0rgAffUtPp3poOVKtEhP-iKZcxO_5NGXyyRATI-o7BFgEDAJgWvVfXOajLFhu7ERdecRtrnucoPhc6RCiaq9s_7kmA57inRDwX__TIu2WBYv_BHdcDFMV2LklbSGdZYbBEZzsi_K5t058idL5lK_CFAn_wfZn-HBnIZ9KyLcg2Rt6kYbTcIs6n-nRumyXI1UvGNBzPWkhRacVttX_QanIC4xINdOx6Z7meerXOtHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/140381" target="_blank">📅 01:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
✔️
احمد نوراللهی بار دیگر پیشنهاد فدراسیون فوتبال برای عذرخواهی از امیر قلعه‌نویی و برگشت به تیم ملی را رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/140380" target="_blank">📅 00:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
✅
پژمان راهبر: علت دعوت نشدن الهیار صیادمنش مسائل سیاسی هست و تا اونا حل نشه امکان بازگشت صیادمنش به تیم ملی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/140379" target="_blank">📅 00:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
⭕️
⭕️
علیرضا جهانبخش به پژمان راهبر: تا دو سال میتونم معافیت بگیریم و به زودی برای بازی در پرسپولیس به ایران میام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/140378" target="_blank">📅 00:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/140377" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی : مشکل سربازی ندارم و معافیت دارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/140376" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
ابوالفضل جلالی: هوادارا خیلی بهم انگیزه دادن و تو تمرینات هزار خودم رو میزاشتم. متاسفانه مصدوم شدم ولی الان آمادم
◻️
من الان طرفدار پرسپولیس، عاشق پرسپولیس و سرباز پرسپولیس هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/140375" target="_blank">📅 23:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ابوالفضل جلالی: من سرباز پرسپولیس و عاشق پرسپولیسم، همه کار برای هوادارای پرسپولیس میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/140374" target="_blank">📅 23:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ابوالفضل جلالی مهمان امشب فوتبال برتر است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/140373" target="_blank">📅 23:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ابوالفضل جلالی مهمان امشب فوتبال برتر است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/140372" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
احمد نوراللهی بار دیگر پیشنهاد فدراسیون فوتبال برای عذرخواهی از امیر قلعه‌نویی و برگشت به تیم ملی را رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/140371" target="_blank">📅 23:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
فوووووووووووووری
⏺
باشگاه پرسپولیس بار دیگه مذاکرات شو با احمد نور شروع کرده‌ بود تا بجای قربانی جذب بشه و احمد برای دومین بار در این مقطع پیشنهاد پرسپولیس رو رد کرد‌/ هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/140370" target="_blank">📅 22:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
کنایه فردوسی‌پور به فدراسیون:
✔️
✔️
استرالیا با برزیل بازی میکنه، ژاپن و کره با اروگوئه بازی میکنن بعد ما برای بار N ام با ازبکستان!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/140369" target="_blank">📅 22:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140368">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: حسین کنعانی زادگان به تیم ملی دعوت نشده است که هیچ ربطی به مصدومیتش ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/140368" target="_blank">📅 22:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140367">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a200ac824.mp4?token=LAmzQafdtBYJ0xhkZXEJVk5exWEZhWnFqejLAszwrpWLKMfx6-ZJj0OuPTfFs15TT8rAsX8lkjXpZW36TplMQ9FcS9I8qHclhk2aO3omgCMpvHXupFVjpk_3vCgNnSO8Txp8Q1Shi6_kFcobx2ISR11PAM2Nr-N62oFe6YXRxkgUHcSImdTyBL2IEbs4RvuZUGqzP10xgXgw5aSIuh1hjvoL7oskA5QMSm60fg6XistQsMfEZcI4KnGTrAxncrNl2-CBJdJnmDIbV0YQ_wB6LwCdNENiZFWWP1OwXSytiGjTuhZyJqWeI9BTE1xTaDPnxUPcZKlG9Ygnc7900I3LJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a200ac824.mp4?token=LAmzQafdtBYJ0xhkZXEJVk5exWEZhWnFqejLAszwrpWLKMfx6-ZJj0OuPTfFs15TT8rAsX8lkjXpZW36TplMQ9FcS9I8qHclhk2aO3omgCMpvHXupFVjpk_3vCgNnSO8Txp8Q1Shi6_kFcobx2ISR11PAM2Nr-N62oFe6YXRxkgUHcSImdTyBL2IEbs4RvuZUGqzP10xgXgw5aSIuh1hjvoL7oskA5QMSm60fg6XistQsMfEZcI4KnGTrAxncrNl2-CBJdJnmDIbV0YQ_wB6LwCdNENiZFWWP1OwXSytiGjTuhZyJqWeI9BTE1xTaDPnxUPcZKlG9Ygnc7900I3LJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: حسین کنعانی زادگان به تیم ملی دعوت نشده است که هیچ ربطی به مصدومیتش ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/140367" target="_blank">📅 22:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140366">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
حمید کرمی مدیر اجرایی تیم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/140366" target="_blank">📅 22:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140365">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
فووووووری از فارس
✔️
خبر ابطال شدن کارت بازی علیرضا بیرانوند صحت ندارد و این بازیکن تا زمان صدور رای کمسیون پرشکی میتونه بازی کنه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/140365" target="_blank">📅 22:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140364">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE3wY-32nZoKxtB3KnPHlTCLOfgM29capom-DpsId4cLZHQnkcX8rzP9bmKFUSrCWyIIZiTHgrMVCkkIsVzfhSwlx6CwUnQXdLnbDnhzxAYVj25zVYOYHhEcNtufYkRT4UGIKYCAXiN0pBdc9nig1wm9x5yg8q84eqcUyzTyrYe1j9k2sEkEHOA4Tjl6gdJ07cAAse1JjXmim3Hc1noaiINZetyVVOp-oQKJieciHoKM0SzQAGIPNhiHuceuOJMqdDYKO60oq57qSfUUKS5TkTN3Ne2ODyhL6y6oit1CvBYSQ0S51qAU1km9MGECpwKACr373UBO7stvCx25M8xYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
به نقل از رسانه ها دنیل گرا بزودی با گرفتن ۲۵۰ هزار دلار از پرسپولیس جدا خواهد شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140364" target="_blank">📅 21:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140363">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
✅
✅
تیوی بیفوما که بدلیل مسائل سیاسی دعوت تیم ملی کنگو را رد کرده بود دقایقی پیش برای حضور در تمرینات پرسپولیس وارد ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140363" target="_blank">📅 21:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyO4Huj436f_UnGZTWRHVFolWtrJ6yQLBiGTdUl3pBDYtpufqLJrn23nXN1nA4rpusM4fq5pZPvEv7my4nmI2m8sx1cvsNHKRTmjT2Oz2NmAW-bBJo4xTwaLQlo4O_yfwOg-JsDELWGNTkUVMi30R-LGwM0MZ3n8D3_OGZ5C0c0DHP1u0W46mf45yBBd8SSQLPY9HBseeh-zUGW3SEJsN0q8GTbhqMTeHCPedURhnypILOfVe1Za7H4P0JrbkkITK4KspNJB0uQk96-2rtZ30LkZeqUfWRL5bMBYyNdJJM8kYDSLa3EunJiRyTowgShVuu7HAj7Z410L5eLARbpsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی جام ملت‌های والیبال به اوج هیجان خود رسید!
🏐
نبردی حساس و تماشایی بین اسلوونی و صربستان در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با اسپورت‌نود، دوشنبه ساعت ۲۲:۳۰ دوتیم اسلوونی
🇸🇮
-
🇷🇸
صربستان به مصاف یکدیگر می‌روند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140361" target="_blank">📅 20:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
🇨🇬
تیوی بیفوما به علت مسائل سیاسی کشور کنگو و در حمایت از مردم، دعوت تیم ملی فوتبال رو رد کرد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140360" target="_blank">📅 19:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140359" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
با ‌درخواست تیم ملی علیرضا بیرانوند تا نیم فصل اجازه بازی خواهد داشت تا در جام ملت ها آمادگی داشته باشد سپس به سربازی میرود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140358" target="_blank">📅 19:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140357">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGYGTqYu7OITRtjUogX1K_RA2WLOEa5woE6iOHx9OKV7DNbVMYDAEMkoKlxlh6VY7y49axctbkUwO3maojjMa1GbgN7SBxTYT-po_BY2tL8ZSMoyi39K3gseKyy_yC6uZ-oZFHcxwGI0pw0po7aAABploPItOm9YiKf2-dYvL1v_MiJHbNJv55J00eZZtBJ5ld3tYOBL1KmkzvpNVytSU0ICZKzv3zWD8IPOheJ8DrR5sny6xnuL37hNRF-ezmVZGpLXtQCzoBjoRlaDJryUeiYgn43j63XsM7MbtcuxhOKBwQacM69zhZjAW_Qlw6nf-nnUzGxrwSiGUw9GDzuDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمید کرمی مدیر اجرایی تیم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140357" target="_blank">📅 19:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140356">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری از فوتبالی
🚨
سازمان لیگ کارت بازی علیرضا بیرانوند برای تراکتور را باطل کرد.
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140356" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISCDrW7KtoSXuFXZl4DWvmEWyIdn21cs5Uo7l_PG2K2gSpRxBsXpkyR36pEb8qBwtPbIPv3k12vuOnJSGGv0CErf8C35CPN3ikxcgqwjoTSqfqbgQNUQRZVFMPqREFglvrT1sy22Jaoru7KT1B_MKMDDWPAmnbCo7V8UfvnmpiZJ_9K5GSoOuQxEHgiOwQgnvEJs5DC66_t3CtF3p1hRlmOuNcM-yS7pqoREncqUuLhy6sY-xmsR7tVT74RoUuEOpycRVxE2Bg-QyzVGByvMKy5wwSVlNh_xzfWgCqxaP3iveASWdMv6_i4fUBqyS35Yud2DfvQfC4myu1DyqoUoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری از فوتبالی
🚨
سازمان لیگ کارت بازی علیرضا بیرانوند برای تراکتور را باطل کرد.
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140355" target="_blank">📅 18:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140354" target="_blank">📅 18:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbMAXl3cvxfCdmnmDVGvjZhDSCFQBaY4g6yZLVuoXazNFXMR1yXsehLJUxzjv-mrKBCI98Cfj3J_o0iDfCcCNBLg7AAthJD1TCHYkUD9qwra_L_zo8RJiNWFItsYZet0ZhZ9Eaf7nRke58JVay0VF02BlnX06WaFLxGDMl5G1_1TVA4UhNYPO3M5Rsu5Ya_IubTIGNZnfMusdfHRahakzvJU6xppSmZl3ukomeDKfrgTqBlqZNYUGIE8h5vPY7nYQbHhC4hWS3KGwt8H-gsK7yaiSv155dDaoc1zqUbHjkXdjf51fPIuoTLTVMVlwmxvHX5rv3oofYBddT6gzQaXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بسته شدن پرونده حقوقی بانک گردشگری علیه پرسپولیس
🔺
باشگاه پرسپولیس با انتشار اسنادی، خبر از تسویه بدهی این باشگاه به بانک گردشگری خبر داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140353" target="_blank">📅 16:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140352">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140352" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140351">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140351" target="_blank">📅 15:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140350">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
✔️
از باشگاه پرسپولیس خبر می‌رسد مسئولان این باشگاه در مرحله استیناف مدارک جدیدی علیه یاسر آسانی را نیز ارائه کرده‌اند و امیدوارند با بررسی این مستندات، رأی مرحله نخست تغییر کند/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140350" target="_blank">📅 15:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140349">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140349" target="_blank">📅 13:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140348">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7sfO0WOyEL9ZxSgS5JonlnHrtM_2nzpc6geZxbtHiAzeuLiWXR7haxEZZxhYlUttMHSirl6OOZpYQbS8TSgivhDWFQRmoJLTbyTJMcFX1d6D6BAxnTX6mn3bADPaDkrOpbJOjtz90j1BG7Ym9b5sS0RrB1URqa9eyfwMwcGrkZtx0ajmHBIayN6AjXKGpdXcEdoKieT5KAdjZvOJ_URIDmhaty5ZcUUjvkIrh43J7E_jRa4-748lCaEJ3WhixM1UNfT5OJZF6WBd2rJM9kl2fNn7vmIHVafdk4mAF6oc6OIOnPLa8TqMCn06x34GSP5aa1XBgxpNw9wQ1BBJyA2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140348" target="_blank">📅 13:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140347">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140347" target="_blank">📅 13:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140346">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2tPtmbq2WaJIHJgvkhLwYyanEToA5PRcjY61u6d8jEFOc0uWwGhYbJMHEZO5L8AsZLr2HJYExcjLQp1LeAWomaVs8rWRNKGD4BGe3UItcvJhspvR6EkqW3sn7ubY9DTquJDmN6Fmi7eJCA5oQuvzv3_3DUHTFij2U7Isd9Lcg8-EZIyCPcpLKZJ_GM_drPLANsuFCMl1MTxUlepPsMv7gvbDAogxUcVu2G849M2lFhxkqiTAACHaHeCDJ0vq-_kWZ8iMXiIS2pQvm8svZkBJNmetdFHmjEftuzJ9WOo2KShvNTzIphSrk1LK_HEs7z9g3XuQvuC7HIlsguKoGwnMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام ملت‌های والیبال اروپا
🇸🇮
Slovenia -
🇷🇸
Serbia
⏰
Tonight 22:30
🏐
اسلوونی با سرویس و بازی سرعتی از مرکز، تلاش می‌کند دریافت صربستان را از نظم خارج کند؛ نقطه‌ای که می‌تواند جریان ست‌ها را عوض کند. صربستان از نظر قدرت حمله و توپ‌های بلند خطرناک است، اما نوسان دریافتش مقابل تیم‌های قدرتمند می‌تواند دردسرساز شود. با توجه به حذفی بودن مسابقه، انتظار ست‌های نزدیک و طولانی منطقی است؛ احتمال کشیده‌شدن بازی به ست ۴ یا حتی ست ۵ هم بالاست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدار هیجان‌انگیز امشب رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140346" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140345">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
✅
رونمایی از مدارک جدید پرسپولیس علیه آسانی در کمیته استیناف
✔️
✔️
باشگاه پرسپولیس پس از آنکه شکایت این باشگاه از استقلال به دلیل استفاده از یاسر آسانی در کمیته انضباطی با رأی منفی مواجه شد، نسب به رأی صادره از این کمیته به کمیته استیناف ارجاع داده است. …</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140345" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140344">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
پرسپولیس قراره ۳ ،۴ بازیکن جوانش رو با هزینه باشگاه به چند تیم پرتغالی بفرسته تا تجربه کسب کنن و دیده بشن؛ در صورت انتقال، سرخ‌ها هم از ترانسفرشون سهم می‌گیرن.
❌
فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140344" target="_blank">📅 09:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
✔️
پیمان حدادی: به‌دنبال این هستیم بازیکنان آکادمی پرسپولیس را به پرتغال بفرستیم!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140343" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140342">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHadJs0KrK9rIZ-Y5aOhMF9Md9ZH3omlVIcZUfiIG6G_6HDkJE9i0WU65CXmXtxXprDzHlwSqMFZbEglovEffGBYLmPeCdMfhmNOmeMsedKzHDJOW2S39IFz5nU4HnZfo7zqM-ICKbDN-WKM4PmpHSaZw4FBzXLqkVyZIwmpxvqm05RvnkrUW9ZNyALDxEFe3_JfqYiANdl3BfeMSAn1QINAM5oVR0zfOd3jYxHfu72pPN3mAVW6gqGjCteODOr292V8WLL6u45YFcoR0suVkwwKcvjNloxtx1RUAbWjLukyGMpGSng5db6IpLC4SPAPPv8rp6U-xOdu7K7sK6YTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140342" target="_blank">📅 09:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TylBN0AQe5Xwqc115U27mJzlR-m3OETELdp5FPU0wqoKzNmpPvCNFQF1TqBQc7UNyPAFh0S1ZOHYp4K9wIsL6sg0RHKGlbWusjP_AxIrvNlfiMBqCt4cGM6vT0rF8Qw6UsAf5pK8yPZl11eWhXdrAjHhPFJxjVzYThhWSpTsmA-jhceY4ZDOWL4ng_NYbgtVYqvIILjzMQQwhzBRFTNeGBd0JNHDYbL0PV5lnBohqhhOBo-rxB7F3X0yDDJpLuZ_aMniT3SKtjicgdFZg02bv1vt2RnVYGDQHEK61QcDEU8RmjhrDL__vmwKz-3QSAVr1m1v1FfcV1T0WshCbqBMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140341" target="_blank">📅 02:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
تاج: بسته شدن مرز عراق مشکل جدی نیست و با AFC مکاتبه کردیم/ عده‌ای با کارشکنی و انجام اقداماتی به دنبال عدم خروج تیم‌های ایرانی از کشور هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140340" target="_blank">📅 00:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140339" target="_blank">📅 00:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9814f0d7ba.mp4?token=EhLjFxqogelgq6FxY7XWxA9SiMR_UXovG9Xd-F8qUG51gzIggcUO9FT_HpDxcOMgTH_1EGon26SxE0cYk4wMjCJuFIchLx-CeRPaThwmNOn9aLLc_muPFvtgVutsKX4u11DaIBZSIhYpMb_XbcEcBMViNhNHZxLKJZkm-T748IecZfrJNqK_IWadSZzNVmkpHWW92QFtRraVPd5bhguDSDS0SfbdcdnD4hU8ORtmGFEQUH7svz-XADcf_3B73i5E-W_EhDnGvdNjQGH1QRGF7n2MK1acb3vnKfPOaeNzw0LLaa_TwQPeP8PZDuwuHL_gyRmCtAgwb1XyztJ0JBPlgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9814f0d7ba.mp4?token=EhLjFxqogelgq6FxY7XWxA9SiMR_UXovG9Xd-F8qUG51gzIggcUO9FT_HpDxcOMgTH_1EGon26SxE0cYk4wMjCJuFIchLx-CeRPaThwmNOn9aLLc_muPFvtgVutsKX4u11DaIBZSIhYpMb_XbcEcBMViNhNHZxLKJZkm-T748IecZfrJNqK_IWadSZzNVmkpHWW92QFtRraVPd5bhguDSDS0SfbdcdnD4hU8ORtmGFEQUH7svz-XADcf_3B73i5E-W_EhDnGvdNjQGH1QRGF7n2MK1acb3vnKfPOaeNzw0LLaa_TwQPeP8PZDuwuHL_gyRmCtAgwb1XyztJ0JBPlgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فووووووری و رسمی: وارد فیفادی شدیم و تا 3 هفته خبری از بازی‌های باشگاهی نیست...
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140338" target="_blank">📅 00:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔄
✔️
✔️
✔️
🔄
سعید دقیقی بعنوان سرمربی جدید نساجی انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140337" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pih8Rx4JsrTYINOALSqcXvv5rk6L55lFM8KnkwJudysQJLZxyYrMLS-UViLI7ZnRkXGZOLtE0-OhXluasM-Xi0rrJkR40BHzuTxVR7TvOQrsdxvBSBgObCyqY0Nt8PkD8L9wc9RcEdUXQ94dewPdX1sQ2nxncAyW1-0CvVjYFTwMNSIuisKhghrnxbNYU1JNZEJHwApCep1kSRdqaQc1ps06uZACaKrmZcZSyuYNU9VWF2e3KFH92f0kFq4-RefJfTsK8Kz0-wUrKhVYuUht6JHnRTHPaNNxC_Wqa2s7w0Lt8cnk9s7vSftev9o-BiTTlDoLB4bC7QQnfOWRJuAdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
💛
🔥
غوغا کردی امیر قلعه ؛ جوون‌گرایی نوین قلعه‌نویی: ( جمع سن نفرات تو عکس : ۱۰۹ سال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140336" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140335" target="_blank">📅 00:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔄
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140334" target="_blank">📅 00:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pt8z8MK9l17FX_bsNacrmFST-t_7wTc21e2t4O7-EaN3X7s_OHnY7q06Ki6W2vjLE1rvyLY5nXNkV7MScwV-djFheX05VDp956f5gKGLKfST2RtrQYzVe-T8QgwW87PgXigCtenuDLnNrXkrBmZrObY18tNRUn6n0wkddClmjr6vWMvapfMxYqyDg0hA41k-yL0ij9Tn4icnfNDrO6ywqzWCWCw7b3RUd2G5slg8m223lbx2zrBpsNbt0leCjnlYfobg_6pDM_CZX9DsyMEEkJu86TQM007x5I-I_Mr10WV_RKJVc_NOfD6TqgP-oBWhuje61xOzmkz1ZAXvCgcqCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛎
پپه لوسادا مربی پیشین پرسپولیس به عنوان مربی بدنساز تیم ملی انتخاب شد.
🚨
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/140333" target="_blank">📅 23:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9Kun6uEIQzD0cg5-Iq_CqRO6z3c87HXdcNueeOxzOAX8BmJyY9_bfuhAB8JiBMJrMS8vpYGyaeXjYl0fzEy6xDm0ZauC-5lXWG2JgP2d62lNO2dCQK7F-iZduscQ6o93Hr-X2A_wNGseIwBp4-kGsG-D-n0ZRTcaa-90bteEkhYyfteOW-euBIYkzcJnzatzey38uBiT5mZeDgggjDfOKJdOR01Y5DC6wJpsE0a039CJrhIS3BHAbcHgDXxPAG8cB_Erv5M4_2B4qc3f15mtnw0GSoDPO3AZjR2qmLywXCfutHdR23SWmDjVUnxCk2qiDp-vcnyYLMpaZwgjR5S1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
مهرداد خانبان به کادرفنی قلعه‌نویی اضافه شد
❌
❌
پس از پایان همکاری آندرانیک تیموریان با تیم ملی فوتبال ایران، کادر فنی این تیم با یک تغییر همراه شد و مهرداد خانبان به جمع دستیاران امیر قلعه‌نویی اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140332" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtOLmX8ggBLenqzb5cVkQ3hDBbhJ1uAcmcCqa71vbB4ZZLClEGrkTtce-kHXLCaM_45dx19VNtA6XH--YUQ5CYanT_JzDNTDLwJqqXVAs_AxNidj5nA612HZpbkFQ0KmtkXP6njXNFNkDM3sULCoZRxzq3_vhb5jUqzWakRnBbkX-xcpet7XsI7ZqMNHwa0qtRRXsyheBIYx6HzZh6fFaK6gx9wUuXP-N4FIC7yqb4qGeoBnFxsSLKmfxsh4Db_-cK1x_6O5nC48WurJ4GTiH-UCqCp6tfdLjhz1t8HZhyu1b5hk5xNT71jntoSoUS3pstybsR3tC6AMs1s2bt5GjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
خبرنگاران عربستانی: کریستیانو رونالدو نیم فصل در انتقال آزاد راهی فنرباغچه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/140331" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv7nP260vJICDpT2kL-QBeK9kSob8_EFk_hX7pmXjIdXwtS2eY1xjCW8fXSh_gN5rs_DkgZyO_T0XPPNNPZ6BInxZPp3_FpdwAnHhRIL4xfF721JJ7QV8l75Pm5KNgFfEOyUdRg48qEGozt1jI4vOWUJxixBUOBfMu3rovDAOUFJhxmeEZX8eDC3Y_V5iVOh-X32zPxbiC9hiocHwuCRLl53QWfCkUjM1ur9ERRl7IuBhiDhbjOhBusPB5leFH0jP4rhDw_ueIQHFOmmHAcjFwl1jn__CxkjUn-J3d-I_l30RPXyF9ocnMn1y58EWpAsCTWLqGlTfRCIbb3Z0QjT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/140330" target="_blank">📅 21:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔄
⌛
بشار و فرهان گزینه‌های روی میز تارتار در زمستان؛ پرسپولیس به‌دنبال پلی‌میکر
😀
درصورت تایید مهدی تارتار مذاکرات با بشار رسن آغاز خواهد شد و فرهان جعفری نیز گزینه‌ی دیگر سرخ‌هاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140329" target="_blank">📅 21:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
رسانه‌ های عراقی: باشگاه پاختاکور ازبکستان با ارائه پیشنهادی جدید به بشار رسن قصد داره قرارداد این‌بازیکن 29 ساله روتمدیدکنه اما فعلا پاسخ مثبتی به‌این افر نداده. اولویت‌بشار بازگشت به پرسپولیسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140328" target="_blank">📅 21:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140326">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7pBGJG3Mlp9-3EE1DV0XFBNC95MQM4cuqlOPliKR2YX7jDodycMwMaB5TF9oHnIxApK1NmGzCiyZZKl69BVIn4jz4gmGOOm2_ougfcS6Bkr9UFXcM0ZS-RLXNqLBcTy8MoOl6F1-QQ7_O3yunSoaSUOKU74fYSbRdskZxlfShKPCOBr2H7gxlUrFbGldjGXLAc1G9bk1_KdBIp0VVAGouw9AsoDvJqf56qIzHAT1n8hoiVXS1lzXQCOKhxkEEXKS6tbJdObzXX5byqqGZNB1YiRKTEbkiwfuF0XXfeNTEEf7suSlFhfJv6Co7hIUKayLa6eXqHm_msUxoVHJfCCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Marseille -
🔵
PSG
⏰
Tonight 22:15
🏟
CEPAC Vélodrome
🔵
مارسی با شروع ضعیف فصل، در ۴ بازی فقط ۳ امتیاز گرفته و ۳ شکست داشته؛ پاریس هم با ۵ امتیاز هنوز در حد انتظار ظاهر نشده است. در ۵ تقابل اخیر، پاریس ۳ برد، مارسی ۱ برد و یک بازی هم مساوی شده؛ آخرین تقابل هم با برد سنگین ۵-۰ پاریس تمام شد. از نظر تولید موقعیت، پاریس میانگین ۱۸.۷۵ شوت و ۶.۵ شوت در چارچوب در هر بازی داشته؛ مارسی به‌ترتیب ۱۳.۵ و ۵ ثبت کرده است. با این حال، ولودروم و حساسیت «لو کلاسیک» می‌تواند بازی را نزدیک‌تر کند؛ انتظار یک بازی پرفشار با موقعیت‌های جدی دو طرف می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140326" target="_blank">📅 21:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140325">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKvcHn7JrFHCDvJDiE3JJfgcwbNxCkp_w6h27gMLkwQgp2K1aRMVMJfGTApCsCvUXFzX48WIrJol8kpx03Zk_ZVQ8_wQgazn0-BetqtWXG7otUVczcYQplhmNkNE_GIHNOpINADClX80GuJDggXCcPsGRVTjMobsfjQneh4TBx4U7DTOWHJAajNHQi2Xv6MwagcBZ70gmSyBVE8ql7VjyncuIima_hUGd1J87kZ2pvBMuR1DWguyYekf-vsyo7SqMAhyP1jY9NPndMaq7k92BzU__UuhvQR6VybYFtFDUqE2VnLfJbAFbOKicKmStm--qoyLszPxSU1hP_EtgJf3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140325" target="_blank">📅 21:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140324">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
✔️
✅
تصمیم پرسپولیس درباره اورونوف
✔️
✔️
پرسپولیس فعلاً هیچ برنامه‌ای برای جدایی اورونوف نداره و این بازیکن همچنان در برنامه‌های باشگاه و کادرفنی قرار داره.
✔️
✔️
شایعه انتقالش به تراکتور به‌خاطر نیمکت‌نشینی تأیید نشده و حتی اگر در آینده بحث فروشش مطرح بشه،…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140324" target="_blank">📅 20:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140323">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140323" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140322">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140322" target="_blank">📅 19:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140321">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAOou1n3poRcTVoIGT7HBRIolAKTy9mD8qlX6EBVf4mqw55MLQRU3BL9ZvfluR369H2eljORlxCiRzZbHbkWXZInBlpmBbJy9uMypCwzvA-w-3ThALzY0qbOwpvWDlztx60s1Q16wp9_UU595IHBoYpg8l3x1tcxVwyd0JlpyrtH9imrPkXEEmyJ6FsYSWmn8hyKqLy-ikEJ6ClAMqWA8t5IpF-R4u66Lj4of19JAwZdMDR7085xgaS8DmGmdJoHIVVSa16oalWsxDuSYoQdbOLo8OoTCQurW4gAORI8_fAipnOsB3jEDCDsWe9J0nkdieGqjk7XXgvcAEF1Jd4X1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
گزارش تصویری از تمرین امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140321" target="_blank">📅 19:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140320">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWcVBrDy5hEjUdT3rKjnJGdt762cDqaqwho4LfM1KDDjcvmCbtq3MgHtOH4UMh0GWIxD2ci8AopXgOmEMug6QMvXekDwc5Vo32DhCN4VY0k46c5eGBMyLZi5vVSQEPJ02uM0IP37iwxC3MjmU0G2siqfEVwbL8Jqu043w9pz5-Lcbya4_2vkjSe0UttqnGrawBio3z32_3BRWBxqtDUONDK60iXixYfEM3D3qHakifWMlI7pZsGfFLm7_de1o9P5iZUQfvn-jrTjrZqBn_r_0JqRnodAGn-1J-tQ_MrFH5HbNh71cxjb90-4jDQNYpRq2NRhRlsrCgeQEjuya3St_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140320" target="_blank">📅 18:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✖️
✖️
✖️
🇺🇸
ترامپ به فاکس‌نیوز:
❌
من می‌خوام با مقامات ایرانی
🇮🇷
مذاکره کنم، ولی چالشی که الان باهاش روبه‌رو هستم اینه که اونا مثل موش تو سوراخ‌هاشون قایم شدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140319" target="_blank">📅 18:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140318">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140318" target="_blank">📅 18:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140317">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
فووووووری ...شنیده ها
🔴
قرارداد استون اورونوف با پرسپولیس با دستمزدی ۲.۲ میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140317" target="_blank">📅 18:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140316">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
رسانه های مملکت گفتن آمریکا مجوز لازم رو از چند کشور منطقه برای شروع دوباره جنگ علیه ایران رو دریافت کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/140316" target="_blank">📅 17:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140315">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140315" target="_blank">📅 15:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140314">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
❌
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/140314" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140313">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
❌
⭕️
⭕️
فوری/کانال 13 اسرائیل گفته آمریکا و اسرائیل تو تدارک حمله سنگین به ایرانن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/140313" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140312">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=vRs7MVi0u33rPvK2WD0GSHSCykwrEp8X99WLBhpjzrnOnlbtvBeFrsjPR7FmEn2XW7Dlc_9WQ5nP0IRnP-j5lpdZHcRl5nEdlOY0puDygrpdIhaCEXtIBSem9ADT-EWEohouAGhkhwhTlVRTLtVXsdvpcV4FAlL0t32RdBznh_3-dM2mExiINWs2p0GzRJEbuaYNDjY5qS6iUp3kckX-r22bE6GLr63QXdTagetZ0bsg9LkRZ-DxFDMR8Q6TRJYFyl6i2UVHhwiXltXv-5d2z_uGfW2UUe5HBnTohMEpvxIcAA5V2rFshiFYa13TKIJqAw97RTmX5zQINCfnmcXY1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=vRs7MVi0u33rPvK2WD0GSHSCykwrEp8X99WLBhpjzrnOnlbtvBeFrsjPR7FmEn2XW7Dlc_9WQ5nP0IRnP-j5lpdZHcRl5nEdlOY0puDygrpdIhaCEXtIBSem9ADT-EWEohouAGhkhwhTlVRTLtVXsdvpcV4FAlL0t32RdBznh_3-dM2mExiINWs2p0GzRJEbuaYNDjY5qS6iUp3kckX-r22bE6GLr63QXdTagetZ0bsg9LkRZ-DxFDMR8Q6TRJYFyl6i2UVHhwiXltXv-5d2z_uGfW2UUe5HBnTohMEpvxIcAA5V2rFshiFYa13TKIJqAw97RTmX5zQINCfnmcXY1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
| فوری از برنا:
⚪️
❌
ظاهراً عباس کهریزی از ناحیه رباط صلیبی مصدوم شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140312" target="_blank">📅 15:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140311">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140311" target="_blank">📅 14:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140310">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td7HBHjyRI4sQZ_vzgPsS4dgk8wiz37xddCsRsMgf-qF8JJj49z8zF_pZZufN9dQ_DJmEUBHyI-jVcjgma-1QjL8FKbtDU3USyzkwl9-uCwKeSqdHQILq20qEErrI6wmkhSkz4UrkqjZwOUx90bfsq1H5Bto9TUz8GBaFyD6xShrWGdv32ZsLD58qskXU3FAYEI0E5jItKoL31atHGRwX41cjg8ktiPnjhAHqthbJJd36biFYiuzzLwVL5d36Domt_Z3jNpMQvxkfDEosfg4wNYAVdsiWwMBdqlDL3U8hHtYEmaFzuSonq8E-nIb3CXgHCMrVp6LjliEFDINz_QsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مادرید در انتظار یک شب داغ؛ اتلتیکو یا رئال، کدام‌یک حرف آخر را می‌زند؟
[
اتلتیکومادرید
🔴
🆚
⚪️
رئال‌مادرید
]
⚽️
اتلتیکو با بازی فیزیکی و فشار در میانه میدان می‌تونه ریتم رئال رو مختل کنه. رئال اما در انتقال سریع و خلق موقعیت از کناره‌ها، تهدید جدی‌تری برای خط دفاعیه. دربی مادرید معمولاً پرتنشه و استفاده از کوچک‌ترین موقعیت‌ها می‌تونه سرنوشت بازی رو تغییر بده.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140310" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140309">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
اوستون اورونوف و ایگور سرگیف از پرسپولیس به اردوی تیم ملی فوتبال ازبکستان دعوت شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140309" target="_blank">📅 14:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140308">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
✔️
#تکمیلی؛ فرهاد مجیدی سرمربی سابق استقلال ضمن تشکر از حدادیان‌مالک‌نساجی آفر این باشگاه رو کرده و اعلام کرده در ایران تنها حاضر است سرمربی استقلال و تیم ملی ایران شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140308" target="_blank">📅 14:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140307">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">😰
مدیران نساجی دارن با فرهاد مجیدی مذاکره میکنن تا این سرمربی جانشین مجتبی حسینی بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140307" target="_blank">📅 14:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140306">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQACS_mM8EZJk4BsBaKcQptD9tw91d4BSvKC2JjspFylVr3SM-h-NyjIQJNngxlcCNH8JSIJ-nycmuVWcO72H9SnIz2OElIKIvipuYgGJJyNxK6S2GdNFO-v7Ti0ZdoIbWQx_D6t8nZYrloY9SKM4On4bQVozkWfuwhTxS6MfTWYRtBN15sObdFKxFsXh-lszyspi3ANnBs6WlYcs3KdEs0JRRBqss7z9FEj8qF1GjvvFnOiMhyj_b01M6pRpv1ETn_Km525OvZmqUZ6wcOFZ5U8zu6LxCwifG9XHAEBw0RYlH_rCe2aWRyPAJ4GBWT_aIfu915Ie2-xqq4EAUlh0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140306" target="_blank">📅 11:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140305">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6AaaZ35Vw_cU-YYzSGCXViFUPr0yI0SDdVlzG3SMXIlM5Zmom7XFUOuAF6mdIoOvSiY1bqnSloi3Liy7FK0N_lVCkVqUv-fBiYZstLooDwu_ic2UB2ntx5dd9R2oJoxeJDco7xp9UMzTA817JmumR5bwW80WOzZ97g-aFnrNrRFPaoDUv64Knc0CvrBw8diI3MuQRtkX16doeaGt-Lxk83NtHx9U8OuBnLivvnMQy76ZoGBnnVC2RUFCVvHIgEed9HAOXCRaGfM9U7xJM-c3rKCGgvaYPDd_-nR_A3M_MkTcrzm1aspGVturu-qo7pv2gnbE0aqYD3rIzs2JlJEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140305" target="_blank">📅 11:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140304">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIFJXngyWfC8eqt5U0fk6BZQtRUvs-QFocE3pAeHffuTdiiHoR8z_eXMDLFIz9WYF4XWNn3MA9sZYngf-agP5dIP12FMOui8_lTiPc64ozAYw-LemMla2RQthh4Dfr6aOZu3nvYN1fLsl5P_zZYCqQ4N-H5XXr224VVkC2d3D1DRSVHkkvdrYfjbEIZxIJGcvPBLUSQ4AHbKioPT15d1upZX_WfWuCStoyKhmDL-AQ4D9A0sZIYwhssu7NE4BE50heQ0CM_dtc4NQHLu9eYr1CifCbjO7rrWgAmn_NC_0E96Kyhbe1x7ehFIZO10InKg8wPVzrrs6WrmOmlAF1OWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
✅
امیرحسین محمودی بعد از اتمام فیفادی برای تمدید قراردادش به باشگاه میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140304" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚪️
مهدی مهدوی کیا: مجاهد خذیراوی به حقش در این فوتبال نرسید/ حیف شد و واقعا سوخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140303" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140302">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140302" target="_blank">📅 09:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140301" target="_blank">📅 09:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/140300" target="_blank">📅 07:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">■
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/140299" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTYjK6wNdD3bmrDoSq2lHlxyJrWlUoVckk1Qp3XddGmlMGTNRtL5nug0ZrLButImxIcnEja8OfJiHcgtT2NB7CjxzG4JiMkUGzzVn2g9095LVBF29OEVMWLECYSKovxzbZ8TeNU64M11tayJZ6BmCGC4ZGrwE1M5PKnd0WwBqc53-YP4nstTnuw-DI770XXfV3K2rPWMtj8yf8JNnX-o_hEAODlk6Dibskc-l5iJCCRyMKxnHEeSify1F2m3m6MrCLv15ur2GKsypbOPCXyfUrctRfj2GHvfb490e7WHO1I_1CFRoQwwMOxZPG0FvVgVE_kH2DWWvxPKhd8iDwny2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140298" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
باشگاه نساجی مازندران کسری طاهری رو با 703 هزار دلار خریده و با 863 هزار دلار به سپاهان فروخته!
❌
❌
قطعااااا این انتقال پل محسوب میشه و باشگاه سپاهان تا نیم فصل حق استفاده از کسری طاهری رو نداره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140297" target="_blank">📅 00:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
❌
دوگزارشگردیگر نیز با صداوسیما قطع همکاری کردند؛ نیما تاجیک و سعید زلفی دو گزارشگر مطرح، خوش صدا و با سابقه تلویزیون بعد از قطع همکاری باصداوسیما به پلتفرم نماوا اسپورت پیوستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140296" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140295" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140294" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140293" target="_blank">📅 23:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DagnACPeayr4ey3GysvB2Hleu3UsdUqAL76eGPG4oeiFSxoNGG3teK8FXKWPL_XewgxVGr-Q15EKAbpWz4pN8AJAcMsfWJ8ggEiRijKJkgTV5kl84BrWiNblyPukf_U2FVW5kK2K6rTDV_agMjKpfREhqXbgUPAKhf7XeicDYk7LXryw6N67J1K8_qUA41oKCRTYXbSvgNsr03bxpaxs24GeD9rTCB2rmFghqnw-P8IvUlx0mVEr_-d7zxfEa6wiCD6daslBkpfOmAsCOiJ4chXEYxhqhqwLr5BE-Scp5WIDezJGOFho21AA-iiIZ_BVmTqpGViRJhaEtERnyPev2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گزینه جایگزینی یحیی در دهوک مشخص شد
❌
باشگاه دهوک به دنبال توافق با گل‌محمدی برای جدایی است و رسانه عراقی «روداو» این موضوع را تأیید کرده است. مسعود میرال، سرمربی سوئدی، گزینه اصلی دهوک برای جایگزینی یحیی گل‌محمدی معرفی شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/140292" target="_blank">📅 22:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=cXBeoKTAjpMD-_m-f0KuJr5X5QIpZ7yCIo6x-_ZHTs1XH0p6nKJMnAFf5REvfAsPybrfTPWepINH6zkpWPLDrcFy0n9CLhs8l4q03p3ZiTBX8BB5xCkL9IpXEo-Ce5SeIY8IZAtjVW9dtTOpUzvUBTeR-adGbTg1YztlgVspTwC2KSC_sfhPEXSmRU7V95RG9NEJOe75AIXy0_iWQM6SeY_jxERe_lRU_hNIB4r-39Io7F3FDBTaX2noAeSpGLrDjmmDpce_iRHKtJOykj_zquaEGg5553kYH7ya2UOoYwsqz0CJrA6F0rKcw4rqNI7F205QiX-3-h1zzH8Lg1X6nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=cXBeoKTAjpMD-_m-f0KuJr5X5QIpZ7yCIo6x-_ZHTs1XH0p6nKJMnAFf5REvfAsPybrfTPWepINH6zkpWPLDrcFy0n9CLhs8l4q03p3ZiTBX8BB5xCkL9IpXEo-Ce5SeIY8IZAtjVW9dtTOpUzvUBTeR-adGbTg1YztlgVspTwC2KSC_sfhPEXSmRU7V95RG9NEJOe75AIXy0_iWQM6SeY_jxERe_lRU_hNIB4r-39Io7F3FDBTaX2noAeSpGLrDjmmDpce_iRHKtJOykj_zquaEGg5553kYH7ya2UOoYwsqz0CJrA6F0rKcw4rqNI7F205QiX-3-h1zzH8Lg1X6nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
مرتضی پورعلی‌گنجی تو بازی امروز تیمش دقیقه ۹ اینجوری ساق‌پا بازیکن حریف رو قلم کرد و خورد کرد و اخراج شد
❌
بعدش جالبه اعتراض میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140291" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqixsudIpvN0TVak7JBqQKUBPRS5Yjb3gImHELDxKP8CImdjpIxvy-yxCxCE905NN0EbKVPDwziaE3CR-JDEeiE_5uOx3veZL5Ssw0iZ14t22Ssf2Ub7vA4Zh3xdd5AVsUjTdz_qIbPOFLhJkjCCBLSPjVSQ9UZrThmNMiSNwYr4faA1RebocvO7F1bl0sv8mzsKPz3o8vBwcPl91oQUggXU7d_3BJAk0q-Ua0jp7-StsRZ6R3sUh_HKZ59f_8cCMLVBAo1oOfS68u6IDcOdYzCWF1czjhpEJgoOTWxqFkY4O_hXor4cY092DCYgKRzAW9ysJvK-7OSV9xCxTK3x-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/140290" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140289" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔄
🔄
محمدرضا احمدی از صدا و سیما به طور کامل حذف شد و حافظ کاظم زاده مجری فوتبال برتر شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140288" target="_blank">📅 21:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
بشار رسن پست مربوط به بازگشتش به پرسپولیس را لایک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140287" target="_blank">📅 21:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
❌
❌
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140286" target="_blank">📅 20:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9CFbPmBk-1nsOmkcfmMp9i0zbnXJgN559oZ-zUjPp5XjP5ZfdmucgTnJWmJoiYJ600qwn9JlEVfsaGxNnUTw3luF7NjffqvedHEw91W0Gw4p6P9vO9rIn32nvPKo8TJ9hFX41n8Gw1s3Oz_0nl95UW2N2v1Kr2NZvR_7F700KxjWbHSzaDLu5GTXxyGgARuzc52d5oUarbqwuCjS_XCrqiu5ub7LMfzTTddQA9RhkMDI3BJbcsyIru0V9U0LtECttaM_DjR4lIUQGXaCHuNNc1IuR6UCHrhccbkElmiIQerSpNwGSOipc5azUFl6sifmh62qb9AMr2Q0rQM5FdU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزگاری سیدجلال حسینی با وجود اختلاف قدی بیش از ۱۰ سانتی متری که با کیروش استنلی داشت با پرشی فوق العاده سرزنی کرد و رکورد فوق العاده ای از خود به جا گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140285" target="_blank">📅 20:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140284" target="_blank">📅 20:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140283">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ-U2H9jVUX0Wju_7C5W35Y0vyqYwy0KZ255L9hnPeGcuQXK9NfibWfCMGBd-LInLLt7ywPQsEvqTo-2qiR1tdtkm10dyOHOC2E0R39iacvEwBNkUhFlG5ULcgcXab3gMLoc2SXBXH9Si_pnxFUBIOAZrVXZaFUs3B4_N2RtxDcuSJ4R5vvfjPcprNZX1JQvhcNwigRcbL1rgt76-x2BAfMWW6eDR-mqoqZTUmnBdZt9CsObrdtPE3MpFofKTct9lXIydis1mL0Jh3ozyjaGquera1lEE15ddOMcdsXxY_rMPOCdLRUeO8nBYQhvaKv1q4-w7cNUNFIzpJyAt97TDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبرد آندلوس با کاتالان‌ها؛ سویا سد راه بارسا!
[
سویا
🔴
🆚
🔵
بارسلونا
]
⚽️
سویا با اتکا به بازی مستقیم و فضای هواداری، می‌تواند کار را برای بارسا سخت کند. بارسا از نظر مالکیت و کیفیت فنی دست بالاتر را دارد، اما مقابل فشار سویا باید کم‌اشتباه باشد. تقابل دو سبک متفاوت؛ جایی که مدیریت فضا و استفاده از موقعیت‌ها می‌تواند تعیین‌کننده شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140283" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140282">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXyvpaXo9i-SRJaSxcNJCm9NptRSlMuffyMLChiMwVb9T9HuMWrrfE8ZtMsdvyi_B90mjmdsemU_RqJ5wy1qqLg3u5Gu9-NByQsrDsZoVLozn6a7NEd7H_c1qUWBVk1Xpsl5c3b0VZWFFDNZjwC0RYWR1GGR-6gVZ7PvnlP_CRB9UbrAVqK4LN1JWYI422c-zRhh6U4O5mTUbbSFLnwH_KeupJ1nJ171P5laJTn4YTPHhhDFia63B0rk6F-1L4cYwV2m-EVH0Im31TPcG79-TgOzCQhDtJTVVp9s9wioBSRjkqSRC-JS6oiZ2mkfTsnzTRID9gFuF9yTKLv5keJctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140282" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140281">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhdzJjTtjZNpwSAvjXV_DG1DnWSroyBJQJJRrh4SERy2j6C6qaPgjUOALX5OxSdsvKvrOewZI8Pd0eiRX9VqJLtTZy0BK06o3STO8I2u7ip7ByCnD127B90uJ8zFPd_B7gAXDb0eS6NDp4zyUPY6Kf8Q8BAAuNK3E-6dLjg18iE9O-ordMygDlbEGYIUqQ7TYBqY3tiDUHMyZWesSYG4G0wu2xJmn2lvqpJSg0h1W_luXfR0fAc3Cxie43oiquMCtjtbduto85Bx8PCfl5BBGYwN_gjOKNlXiPiJ7Mb-oh63QLWpJ2VhYGTscOOu8zYi7dTAcrFg7R-BDV-GwUEgLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
بازگشت سرخ‌ها به تمرینات
⏺
تمرینات پرسپولیس پس از 5 روز استراحت امروز با حضور 15 بازیکن از سر گرفته شد.
🔻
ملی‌پوشان و بازیکنان خارجی تیم غایب تمرین بودند.همچنین حسین کنعانی؛علی علیپور؛محمد عمری؛حسین ابرقویی و امیرحسین طاهری به دلیل مصدومیت زیر نظر کادر پزشکی تمرین کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140281" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140280">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp5fuPVBtQTkDlGym-ehu61ePD1VFsFnh5iVRAyUEzGIi4g5-_cpYIPOGFZbpQmOm12nMl5mcsIo1xLXVESJamWbXtqXXd7vQx2DLicDyJ7XgHmNg0c35IEClVqdN2KMZXMmKty13b5U-8v89c7ceZ2J8wTbX8diWHuXN3ELUleIT6QHLg4UdY1bRHfi32o2T82cdOZyw9LH27CT5EKrP2Zh09vYReVm5T3TfXsbxz9tRYXrilqkplHPaWKQbuJO5ma18Z7Op0YvsN2OoLjuWG1wj6vntO207ZHmK0DHK-B1iKffg9KwbWCe6wSqluScrMUSbhIRgumDCCXrEiiwiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری شایعات
🔴
🔁
🇮🇷
ایگور سرگیف پایان فصل از پرسپولیس جدا خواهد شد و مهدی طارمی به پرسپولیس باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140280" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
