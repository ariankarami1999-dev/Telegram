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
<img src="https://cdn4.telesco.pe/file/QOEophbe4vwzvEx3gWiqCcqBUliPVmePcVswv_gCWZYteI3F88-7GLKrC5bszKMJLqVQO6xOkKfW1nYnLYKjcQG9JEYFbB-1j4jnVsVk_G-63QYWLGGgMqnHK6BJnXmOIJ1yX4AaK6wZJMmUGFTeN57tBZR7sEbxU57VmRBfViRCZQqZ7l3Swo6q3kPjKzU7CfhC5_OuQIRHmsKjJVMyX-pAatc4N95c7fyfk2EcPuZifnSYwL19md2WTXCQD7mITlUpvEpGADvKvYyUhfzDNzLW4PXNDDHENzKbuFWyM7c269RIxFKZfnUmUy-f4FdMQ0K95TryiaovYFz2E1fzOg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 03:13:40</div>
<hr>

<div class="tg-post" id="msg-7641">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CirL0Lo64gaN7BP1dA_xnbTIMbODhB87Kt1xvbUmSERwJCUm5wSMGvjYlcPBUJpt66DrApqq3MW5rwexCZl1NJccVAe4eMA7O7VkFJL966QuENtD6I5ZsG3HZHk91YwcxGn8QAT5_7DKtiMMa6DxQ7Tfh6HeR0qskMtBWicjo85DkFBXvRKPTAQ4HQk-nPgV91PwNuz8sKdJ0rG6azuFrfqB5PeIBq-jssnOcAmMSas0lDVwpmyONHjvzce6247e1VDrdMzuRViW4GtarKvI0Qy6wvxJMvg46TNiiZAKDWq732B_Xy3i6ZPsoQdm1GqiSh5sy-Jvzn906e7BtevuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
Claude Fable 5.1 API
⚡️
20
میلیون توکن بدون محدودیت زمانی
✅
ویژگی‌های ویژه:
✅
تضمین
اصالت و پایداری ۱۰۰٪
✅
بدون
محدودیت زمانی (No Expiration)
✅
عالی برای
برنامه‌نویسی،
تحلیل متون و پرامپت‌های سنگین
‼️
قیمت: 12 دلار
💵
📌
سایر مدل‌های هوش مصنوعی ها(
🤖
🤖
⚡️
⚡️
⚡️
🤖
,...) با توکن دلخواه شما نیز موجود می‌باشد.
🛡
جهت مشاوره و خرید:
@Configvortex</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/ArchiveTell/7641" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7640">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/ArchiveTell/7640" target="_blank">📅 21:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=cezzpr6vktNLrlubx5vHAjaflWa5PH6HGOaR_RRBqDkFtjwXvRit_ulFrVebZGejJxRnn9eL1DflHVZauLK3b12O-A5fE8rzFahS98FJFndRsfFhJdlMK1gmtT3JHCXImMddFyrAKKcrXn4hCndljA0DnztRV_6ZMYBYL07wrXF9lpgnXixoSii3vZEHTqHJZzERf0MNI_QrB-m18V8tOUtZ470oaLM3KB4UOwiaMB-vx5yYJJZSBHH-YoL140T8U7Tk9sah8hOsfAHYobpnH5EampXr7r_OTzVrH5YJ4pSJmGEATtL1ALTWiWCLC_pBnaAGuBUBJnB_G4uvBuo1Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=cezzpr6vktNLrlubx5vHAjaflWa5PH6HGOaR_RRBqDkFtjwXvRit_ulFrVebZGejJxRnn9eL1DflHVZauLK3b12O-A5fE8rzFahS98FJFndRsfFhJdlMK1gmtT3JHCXImMddFyrAKKcrXn4hCndljA0DnztRV_6ZMYBYL07wrXF9lpgnXixoSii3vZEHTqHJZzERf0MNI_QrB-m18V8tOUtZ470oaLM3KB4UOwiaMB-vx5yYJJZSBHH-YoL140T8U7Tk9sah8hOsfAHYobpnH5EampXr7r_OTzVrH5YJ4pSJmGEATtL1ALTWiWCLC_pBnaAGuBUBJnB_G4uvBuo1Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2SvA4bxe4A5KNkfg9v53Cf0bOWJVmdTttKzTrW3wQ4k-KAEryf7C9vo-QilCiquRvfMMt2ZgNTduN9X3ZLS8gkyc29lsujgxY8htmm7u1H1vuLq7LgA3su-YZeWbpEM8nC_vwYR29TVMt5720FMBX__IqcQRDIwHrcIpcueBRgVgUtuvWytHYvtWdrwTRBxoJ-_XjxykTDZmed14E2KY202nivvMyhuwLVy7pu76p_t7t3gSZcTSIvGHm1PmTlvXlBYxi4UokoPE-IU4KtAmqNJ-8XYhXHzuXOToD45guI3X85aiGVqVSisomiIHcaOgHjz5Am-y13dAn4LQ7y_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7zh07g96yOduQ3a4uHtiDH4Jtmo5CLhdFdN0j1CDL8opnEEecRj3Fp2q_8GAQxC9qLGqDzBq_9jmxCJNZCs9yYXhRyXfeIwCgUTlyRD2buPygZios8ZT92hhbzahQhrY5NtvT5YXayIv9n9YoBCH59IGB4Orhx4jxVCNIF57V1MdArZCVJFLg72LRKHAPY8fsEC110nLu7iF02CndXcSkPuTEu9SU5NaX0bg0EXpcdtfaICWJaDHjyeCvlJYsv9CiRa7wO1E4YTGnAKsgVk-N3oKSBnsx0WDduVpYK3IESSKJxjAoKMkrf4-rJyU--pa_BHkQZ-QrzSz_iQfEKMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=qLt1w4xFocfFau-qeNEvSibICVI2ENTNSzCQEL4GGkCDBuLVOZJPAbo_QWhFAomNKUwLzImIWsW8rd_1dnzW1Eo6e_ybR7qfakyL-QlenkBRRcqMi6o7GVXJo2YdfDL5dZgOCi9cBpxi3zHQuDUNhwD2dOsY88U2Mn9iH77iLzqSQiwUkd-7k-42BKV3eP70J7EcoWeBG3rJPYmrLkW3aHlXi8d-x0vUWmzg9-QawCYIdty0jrmev1hEdd5eMX_dObZuWvDQy_up07Cn5ZfcGlhHWDszGiiJKbCEmY2yVnu4fcCDqmY_AZ04IKH9re22u2hSU6kMnzxWwcLIRX19Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=qLt1w4xFocfFau-qeNEvSibICVI2ENTNSzCQEL4GGkCDBuLVOZJPAbo_QWhFAomNKUwLzImIWsW8rd_1dnzW1Eo6e_ybR7qfakyL-QlenkBRRcqMi6o7GVXJo2YdfDL5dZgOCi9cBpxi3zHQuDUNhwD2dOsY88U2Mn9iH77iLzqSQiwUkd-7k-42BKV3eP70J7EcoWeBG3rJPYmrLkW3aHlXi8d-x0vUWmzg9-QawCYIdty0jrmev1hEdd5eMX_dObZuWvDQy_up07Cn5ZfcGlhHWDszGiiJKbCEmY2yVnu4fcCDqmY_AZ04IKH9re22u2hSU6kMnzxWwcLIRX19Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=JHzqIfwQxxS_dX2t1IzVxHd4X5inCRtfun42O6RMw_xNuuRSDJp-r_jGQ6q4aRBbHrh_CqgM02GdkolhMtq6YNR9osxghbUfA6XrQ8A-437QkmBeCU7_pFOA8sCdTAenhvP1W_r8UQklHfHcCmUGsnmUUKVavDGDiPeqU_S_zB829ltoyX_rmc-UELumS3jNgW2W2o8VC_HxBjthW322AMODmUNyLrTj-mnQHJZ6GNeqh0utLZydfMWhYKF0NHfdzTkMBtjx7rwNiPDB02l-YNonR4LDvwpDgy1vNkwU8-K5YujTk5LhTmZCYzmdQG_w_RE3xpvC1PCoccn9deg1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=JHzqIfwQxxS_dX2t1IzVxHd4X5inCRtfun42O6RMw_xNuuRSDJp-r_jGQ6q4aRBbHrh_CqgM02GdkolhMtq6YNR9osxghbUfA6XrQ8A-437QkmBeCU7_pFOA8sCdTAenhvP1W_r8UQklHfHcCmUGsnmUUKVavDGDiPeqU_S_zB829ltoyX_rmc-UELumS3jNgW2W2o8VC_HxBjthW322AMODmUNyLrTj-mnQHJZ6GNeqh0utLZydfMWhYKF0NHfdzTkMBtjx7rwNiPDB02l-YNonR4LDvwpDgy1vNkwU8-K5YujTk5LhTmZCYzmdQG_w_RE3xpvC1PCoccn9deg1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=iinuBCtLDZZS-Zu-dygFN_EmDDMVe9Dwo4TsOKK8MbM3X6bJXvhzg3yjqTx_BIY6mHHzn4LiERGY5_u046M0tgR0_OVc2sg9mQNQp7d7thyFeLbRdS55wFUA3ITMh7HHJt_7GWq8eBzaKJVaAYBMB2m4-0i7FhLlqeORnFRYoleqyI_rT_lC8LGnsTtuwzkF0MyO9qDztxO6QFzJXy7IaZPNdzCytiGein-goTqNeG18UJrpz8rJR_9F4LUiYnKFQgQDQQFWIJ5gUmxXlFZTbWTBjyYn48v8GzMV6NK9Br1j9R8MgrZVs3dkdzhR4gYKUXHbztl1jeEnTH2VIkAlCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=iinuBCtLDZZS-Zu-dygFN_EmDDMVe9Dwo4TsOKK8MbM3X6bJXvhzg3yjqTx_BIY6mHHzn4LiERGY5_u046M0tgR0_OVc2sg9mQNQp7d7thyFeLbRdS55wFUA3ITMh7HHJt_7GWq8eBzaKJVaAYBMB2m4-0i7FhLlqeORnFRYoleqyI_rT_lC8LGnsTtuwzkF0MyO9qDztxO6QFzJXy7IaZPNdzCytiGein-goTqNeG18UJrpz8rJR_9F4LUiYnKFQgQDQQFWIJ5gUmxXlFZTbWTBjyYn48v8GzMV6NK9Br1j9R8MgrZVs3dkdzhR4gYKUXHbztl1jeEnTH2VIkAlCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMFvZ53dR0lV0a1slCX33caf5nwxjmQ8791LpFfn-6Qs5rPIEmkeE0w7sgKRrGpV50E5geo79ndXJmP35i1Xr4iCcS9dEJCluy7-0iD56ZC_uURhgJQStUUr56enddw5-A0indoHp_J30ULXnjyK-7vtpV4TWWSJGRLaWqxXm1D6e-Kex9VVvLJQkHRcNr2D-4EDPWQ0k09cyZhcHava6J2HNxxTb9JW2altd6G4IGHZWpI0ut-v9Mk46SvhyF9yNZeazPvo3qeBYMMvheOD1Z3_JA21w27fxuv0hqrs7EdQh9UwNRFNVv09cluy5vR0VGgRPgjS9WbOPP5_8GZBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=YZUPn-XnanGuaWAHAtCZTWdIao6UMcKx-i8iGh6goyZdS3iJvYkvf4uQTusPZGGxNZCY6_GuJY0XwYBZQ5F4RtoFYSX2KI1BJrirne3vdGl1j73xLEObpL4l91-jJVOkbuHtltlhUkxswTFHh70xN7oHau0nW8IMtq2SlCDzoz_A966P_dCb7_bG0v-NSM8Ni6ObcoLF_nT--yHv4aufUsXTdwMZ-okz0hOyuJudpoRfxF-Gwvm90JFzdocdZbc95h3hJ1YqOjKMhSf2Ls5xNHmuUExHreXnxbVoZhnaIzQkNmPsJUpnKdlOkG-9_aQTXGomHsH4xCVmEKJedeqOZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=YZUPn-XnanGuaWAHAtCZTWdIao6UMcKx-i8iGh6goyZdS3iJvYkvf4uQTusPZGGxNZCY6_GuJY0XwYBZQ5F4RtoFYSX2KI1BJrirne3vdGl1j73xLEObpL4l91-jJVOkbuHtltlhUkxswTFHh70xN7oHau0nW8IMtq2SlCDzoz_A966P_dCb7_bG0v-NSM8Ni6ObcoLF_nT--yHv4aufUsXTdwMZ-okz0hOyuJudpoRfxF-Gwvm90JFzdocdZbc95h3hJ1YqOjKMhSf2Ls5xNHmuUExHreXnxbVoZhnaIzQkNmPsJUpnKdlOkG-9_aQTXGomHsH4xCVmEKJedeqOZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvMZrDjuxd8OKafrUnSdE3FmiIG2khvq3cO4YUiDVSHMdSZVtpSKXKjcZw15V3BFlVlBMnKAj3aUxyoWe-IKjRBPkteW5xgAq8Ntm0nFsyY3HhljTUqhD4aX-BhRvvSkKOTQSl0Jxuc-mvo7qYmEpNsJ57G2MufRczS8GAThHwQd5QSjkapbAWdexVJ2ERznG7cFELQ8Og6jc-gChRMvRhm6N6WKwULIZcIbYyX9OqLKVoC_MshzZmr5m1YOfvApn3gSBJ6uCQVkx4r4Vh9N43EFPHd-fZGAX0lcajo3ED99xNFLDbc6cNEnKFoqQGMEe0__9v5hwmv5rUB-m0gu2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7618">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGEMION | مرجع خدمات مجازی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIStyhUQ_L5j6idoCnOdI4SP9vPbfJg6_DNCdrW7SloZq8A0EkbpqH2tXufh8GT-1XM_1jVwjFFQlbWmYzaunygLb-9GSxhao9j0LFlJe3tNQzAlSQIr2Mm_WjpNpep756fHKMu_Tu90yH4o81hgzAYkifBX35yZca-_tJOTXyC-Je6Tvf5Jk2EskfYvSgeeaCyfnOD81LDIv-ubcuGkjsCKhVFV5X-k9kY400o2eGll90UI9QpqpmGWPfFSum-AV5CU5WkaiPnxHbwRQdFxcilbyiqlkM7JjvZZi0vOHkPmpMVWKtgAI6hD76pNYGt5zePfg3R0-Yw9J5h4v48p_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی که تو دنیای دیجیتال لازم داری، جمیون کنارتــــه
😄
پـریمیــوم،اسـتـارز، ارز، گیــفت و خدمــات مجازی؛ هــمه با هــم در جمیون
⭐
🤖
☝️
@Gemion_bot</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7618" target="_blank">📅 21:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7617">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7617" target="_blank">📅 21:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nksMmVaKnXaq6rC-YeLEDWCzE-7Z71ITMxQo52ErMn8fJ516mAcWIit5ZUHx0HQOV3mH2S27z3pEeid6LANNor-8O7Vw5Coxr-m9rLPNTVVOtPCzFgn8-Iz58tDSLHtDd6zTG4XawKporZFBgb2CojUtwpCWPPVOttqai2sp8gzNdATJtoGEYlPtBdHOM5GYDlZtvo2b0t7K20lzalurp0KNhBVjNV6lsQLp_O1BC6_oeA76DDp1dc1PKcoVbV7rNRq6XnQPqF9_qSHIPvr7ca6y5reNSP1Oi59Qa_liSoO_kK4awDIVlRX54sZgPiKcKIq-r8G5rNnYSIHPGOupKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgMFKmp1l5MkXNfqtj5Gd9lQsp-9uUZLUQ3-EJNq43URobZKR8Ejp6ndrnzX0gK-wNb7-EVcAdTbmNyVsT1TA9ZNFkSRuSwrlpn9lNbZkc1dTEwth_jusAJQVxK4R-17RCjBO7zL-VpeJjFdK-KB6_yfSL3MjicBxuTHybEGzD-wwNfkzI8-R-7jKC7EeuMPcoFmOHqqovwg_e_vQKdgTztwwZ79Sw8FNxc4_k9ltJuKrNWFw-ybgRiAPAE1YS9zm947g4_4XFCDLcVaW-IgQgiETVb2h6ZUqQSscEaj2-Bl_lBdf93EOVlaH8E0TU8JOg17dOtyZ7nW30TBVK8r8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOx7-5ih7LkwJIBJDhRLKIjvG3wtphnefN6fwUREjIN6CHQ3rNyCSbKiewNjLbFLIJZc6d2GRkrx6nonlsNTboa_XZ5X6fEyHrw5uFOOXfdAskW1pJzplTOr4Pu_QYpaNCKXcW5Zy-0dbi21gVH0VOG4m9kU-90_VIgD57ZIIDFff-VRsp5eKMoT_9YkBr-NGZ9Mkq7G_JLXWSN4dn2rij1_Pk3DwuOJKw_LTS97eRsm9CWozcDNo_0Z2yGbqVpb-Ti8EfSkW3ChUPBBVTxX4g4p88vFL1XFiHGAw24Q62LbIr2AohG_ZiRM0Tx2JzJR8xW7QTU7oaMFetz-Gc9a-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRK1r2oDPNo5R8FF3oG5VMrNM342f1butR2P8-r00RL4qQPutS7_WiIiOHtpuh6QdgdCdzHxYO9Y3DVg-1wX7MkhZ1adjKsCyr9fV364GghqGsmqQO2344jFQWimv5dgnze3gEKCAuQp5jYK-1Iq3dUFRZCg9nUKxLbIHsOa9RKxspXZ8bMUsKbq-nrpOtnTmEySLhANb88i5RdmFpl51IQSHedFXaEQPgvDYT3HXSy1cT0SVIvgTjMSIPRkbfK17o3YP9oJ7eic5fnV0F8CY4P5Z7W6pWm9YObBkJaYQaseZmfLe_2g594mQcs20GT_D8AuQsrh0HSuGEckovkrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq8p0z-5t3iDw914lIiUsXcHLN90MsuetSabo3xamHE6Kqlkiu1pYHnZ-6CZlHIICuKNnMnlj-yASGtSHOPD9ZPuGpldGMkAp0rlwed58T3vyzT2YCt6tshmL0d4fX8_Ntciz6A6hwfUyOjg_0evj4Ku_Ac-TaL-ROphazZ9K4dUnHhS485fCJADuJ5mIgDVvsA71H-tYLh9yEsSj0B5rJ1XCdYsfkpsh7jE58wStbtTrAFz1YHOKmLrDV_XGst55dp-IP0m7lZMPnhKMcXKH_jIh23tXxXJAuRGaDK2FNoQQzzUmlmZkKQr8cplxxVMcolhInY-NgUmLFaD6ngX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH1DyK6c9PR4Uldx1hzLS_FZf7KJCCT5gwxCwFePkjx1a5MObRtf2PN9ihwxNt0p-R9BPDtnDyEsMV9ucUsFTfIemIdOm8TdFVG5h4Q2hVUEeETP6le3dyrgVBrO46fUfhq_vT12YSQifEwicMjGsH45ZpA6PhpDjGySLcU778L8C0hyH1L2SGdjf98d81BVXnSV_SlnKd0VZUlnw7u7oerQLnSjgs_JLAh-UsvbO4zPLYKGrr3NzP2jnu3JmUiUjlvnOx3VxKkLM_KWxBsT-XNa6_j5CJLeoOnlNVWj01cx1ZSlz2Rp-dYjAzCXwzN3PXw6P4b90GGC6jfu5zkIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcF5wMnRRLKQzUhWLZn6cGr-CqOB-XDTe1ajOtB6SzMdVYpDUEOcEqj3w0aW6cbvutS6MUb6FAOK8VOMb_GYIOq3onksZnfTHPZIeUiyYdg72V23xdAj7cPBbQwaps-KQHZK9X7APtOUDCh289dytb4quimN2tkK7oA3S45ntWM3HdnldUpa0rYi9bY8uRzkK2UYIRTYAlEIhcVf_oG58ol81kaptgTRBT4RKL0fM9bX1WIoO162TQkrhVwJWIUT9OU1Ig-HyOa-ie_lqrqhjD6awOclUq-Vv5cko6IaWHIN8zuIiSTtIVWdfh6pQg281yeC56oC51KPDWLLMpxwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M80XBMDSJhqYpjuezCdR2exv9qnwNyVR69yxl5fQ7Sdut49dpS_ol9rvV5Q4xmgV8ApTOJ-kxvDABGPrG6OJmH4r2L78Og2YYBfJwPsT_Sov2WXdk1s-J9FnzSCQjY-1kbvWryE8cl_q0ylHfPrL6PdMcsjQixXW6p6c_Fwx_N0YxzCkJlGg4xGOGqSnjt6UkI37tc3QgF2dyYtfSiQ6qq6lF-_wmZ2772xDsstxCRSwnTltaBZTW_s7t1eHFcQWhG8XUhv4rwYGoflRkNDNtKEb4-cm6rH1srtdzyOxxez2iL0iJEf6ewO3wCtN7X0Hb-COsUJDD4mRSOYM-F3oKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_vwJ7JVnnou2xxLm7ZeTm2_32XZ1Kb_jwU9LSSvvyJGbr1vWu6IXv15jWmCCh9gBBsTTOdUlO-vQtm795ZRWVwq7m_I84Zt78pJkdKm_yZs5FCKcYkumcWVztDjdGnUbuH1vJTHLlj3ZADsOfrQiNOL2BpczHafhhn-TaUChWwJZiOhvOaCyAxLI9QkveLfchs_UFVoVFT9b6nkuD-VRFHmf7aKAl-gzdDj9z07cucCknVcOG93bnG6r9yBF7KCtiCQ1eSoULR_K3fncX9ZHuy7TboxofckNmmkfushzNXumlQfgDz1sZkXGYJdswbenMYjrJAg8qKLsN7wykSpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQbAeccs2UeNblZ9UeKozyzdJnA2VmOZXhF0CWT3MsktWLxfJPOIMLQC5n9ZLnG_Pf2dNi9ndHnqHrI6jdKzmNoV6ItJKS3ArVKE6LZB9uUwrXONaXdqY46k5Nwyrl1BGmfF_zP04zyQ-n5fwMNUsn6rNFAH2ePbseCSH3KgGolPAyu00VgPp5nkoj24rPu5oMf-phAZ1kYC-EirEd-GAJpaIZ3ZC1FAgCAklKZgah0xvCKeS3T8AfJTAXoxnuwZOwqZKbdpJQ28N_A7TZSmJiv3804CpO0iLPk7f04bdjPNDnVMd7nEajsAhqqHijV42HRkkrtlPLmHip_IHUohYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5wtQYxSNDQOC67CWxQ8PRackykIwArPqsZ6-UdrnCjyS1Z8Ro3UUUjpF9igmWNmmBvd3ZR4tvrVklwUnauFBPo9NUevKXhVLLCOcwHTCtHP0EYXVNf-EHhT9fiU1L73BFa0MARrAv-Te2XXZb84bE_ySa27GnI74b6-2dyztFKSNVJKRaU9bjO0y_ej-WNgLVFumMURgib_pX4m3H1FLUKasUMVQtE0QgpvXaeIf_gguLdFQlTw_LJByI0UFz5ku-mqdbUqTrZAfWyhKgKNHUZgSYLf1Io-znaJfoTf1Od2Wi7AQJyXOCKHhirgWnOkkMDVam5_TVyIL2jTFKXTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBEfHcBsPUP_TD3-rMfIgx2s85pFxeI4qajWPa--xGJXNwgHBhcu-fu9ykswwR3urRnj4xPDAA94V6awVa_eb0CP_0g7SGti6FuxlHxJilPZhsZx71LPwhmmmpwHewBl71UKk4i1uZONwk8oM7Bf36Hb-wZCeU_CR_7WYon8vOODZstwZQszbg1kgY-ggUUE6ztZ03W9rgKZjFWeQ4vRN3C_x3Q_dP3HdctIoEP3-740gRSP5o4UizEQKmshCjOP9mZwcy9uB2AVJMTgEeIe7dXPYV3EKJO7bzPDQ9L19hZEYbZ41sxVF-RsokA3blfYeyPi-0W6llZ9ND86nUirRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt7IraKD89aAuRcJP3wP4IjBaHTHUcW9PjdvL1kyZp6ut-UNDG7KIvhtJHK2LcnvtKPcGlskjNEDzA60hE9L4L_d5v094uIEmgS0E09b07qcqBhYdPU5Olc6lXgXRN4B1VMd772fqOMdBXPmIl046H_0Q-He8hcjsfisq9KofnxiXBxlUEpYoPVXtXArfTZIBW8DR4HL7rD5X1znVdqYWAfeIHV0AtrDjfgPamdM2-Ve7QNaVDess3tpyHrFH5hbECQcRIMjYYqTueD1d9zfWtJ8qppu-eMIlmgQGTLv7BpxaXEL0tkmCgL8fOGMqT62G9GdUGB2C-LGB7IRcY6jnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilfKn3MebtdA4ueupfn5eUR-dfCG7raQ4MaK9x2ip6DESnKWpBEvjeZ9M99tMtbqd4YBkAgI-Vsg8KP0bDcTtd0dNHczFiXRZgofLE_0OtrFw87g_cIjy0DP734OR2hm5dOxGDdtTJhocVD0PvcTSzzOav_uZzLgqb0Jr8W6aBm876JArAgJW7yYiyoMLH-6urHItTwNjJRgMK14fe_FTCh4QNXsrUyKOhuYQlhkvTtNKMXSJWY796tDenctX0pqf765eQ78A1-K3Hy1RbSmSKjIY8asLoRp2W05VTHXA0MjNxEzZguetiwCZ9ajQqtk33rChoBaV2X9yBzZimVCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHcnPz4UW5lt7Wx0pZ5qZlM-eb1aogk0Z8mkSJh_uVLK2_mGnEiuSMk9kEbHIfa2DLNXoUa1WNvp-r9DrwtRvNIdc-QvUFBDcthYdjQLXlq-HlSeqJP21imMLkiM5OaKtQCA3iGyCQWuncZuy47z1axvBWK-D2YP_yeXfJ0ykzdiBbZbQD5AG_TK3Drrj7ZxLOzFF8SaXAH6TOmRVd5q8Lz_QTnrmOX6rKE3zttRSCiTiWvg0i_uW_8X_niJm2O3PqvDpZTOYVofgZa4grg62YEaZI0I7T4tj-SlJLZBSlAypXDYuRIkDcJwQvGiWP4yp6x2r8fo2g6Wd40whznh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxc5fK3P2M4mhL6dB2xUUdCWjZkXosyg_VcrGn7m4qWW0z_Axt9xWPysqT6BTzZ2IOaDW9t1QaWP5y2zPhS0i8lvz7-NDefCnJl7gJKGa_oRo6BGMSG9J1koshetMnUWMv5KqZJQ8gwVaOUeKi4GxD0aAbxo6oWhnzRuTYMviDmqZ6gZ_56QfJfdeEjx_gyyTZ60UCQtOXXwND1q1Eu331U7g4fszw8YFy3yev62fH2RAZkOgI-DGRpByFEmDQ7BJJ-rC2gaKdLQjBeASB422spAajUL2IcCGoIje0uxc5Ob60OUzR7nsBR2_oiUxK5FXpRjyJFHFh3DF75Otyzk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAk8B90nl0WVrRypPj8eqgbAy-GxtjvboYeRDb90lu-FkNZKyvjvaQTeAAxBvG22spEJkBuygf9X7Dz5UznKWae-BEnCMqrNtqC64QzVHlIMyXpjQ_k18m_e1eB7ySfx8WmcqAOd3uVP4kdHtgoyYJKU8m7GMbmWxFn1SbaZQoOxUGlaBkUi2s0610264ajes4wN4qnTLm0BUtky7W0SWkUky5zU6ET8HZLJREHbT2MaE0UnxbSLIg5aUKIPfrE5oxuHixwzLbacQf1b_Blo6sQa-iWwNYNZ8QG1Pjk4EHNn9A57USX3KnrEqPDjRzZb2sDXbg5vZdnj13aCUkUFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=DNzp5Urs5xwDFsihppWT-rrYLLOZ_AvMH_Zx9m_hUIFsAPq7lDOYPfdeqgGgd5PwfOiVuUfpj9s6dPRELNBz6ysEXHypb8sAlNbJgva0puGWKC-qV08vtJAVPomgbj2CtpowMtulvIq46zLqdFkp8sQUtsatzWCgq4M_y0H1ULcnFbgesOU-BsDnyLEXIiZHx54ElkbYSrSVqi3nQr_x6GfRp99kr0g5BsdkvubcwtD7XjRa0d-OuWYVZl2EYiwwgsn5DfIJpYgAme0jVNFWC9Hzu4wsrEnX090AQHZagviY50PSaOyac--bIczcenIlbUMaaYsc0iGDWtvV-ulvIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=DNzp5Urs5xwDFsihppWT-rrYLLOZ_AvMH_Zx9m_hUIFsAPq7lDOYPfdeqgGgd5PwfOiVuUfpj9s6dPRELNBz6ysEXHypb8sAlNbJgva0puGWKC-qV08vtJAVPomgbj2CtpowMtulvIq46zLqdFkp8sQUtsatzWCgq4M_y0H1ULcnFbgesOU-BsDnyLEXIiZHx54ElkbYSrSVqi3nQr_x6GfRp99kr0g5BsdkvubcwtD7XjRa0d-OuWYVZl2EYiwwgsn5DfIJpYgAme0jVNFWC9Hzu4wsrEnX090AQHZagviY50PSaOyac--bIczcenIlbUMaaYsc0iGDWtvV-ulvIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5vqkyEKi2dBd-m8mE-TjHkiKjkgfleP_5Ep2mdWQTwSwUtEBhmCgnRCWt5z7XdXW2n-PVMQKt05YzdfthQwvZCaY8fhvRIQdbzki3RFG942HY6ebmzk61zazYSo-a0Z_D0MfSD40O5DnbwUpksOca1AbvhGsYaeBus7nPOTN7BqARqJbRbLkSxHmtNOi3mwDOGuahY3u9mcdPAploFkz_EdIOYxnPRRgzrEv5KCX1JO15AoSImiswt5rRpExqlIoc6Uf6bB_b9qhysoNTWbWmv6A7-ygrbUFICUzpNQIlMDhrdFT9ihCEiHAwFIzg_R4ra3nvBsxgVt0KyIUJkWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=O6CfZH-JoGDRY-AAVQQAnETWFK3j_UtACEnP-mv2zrBPgV3Y2zkKyZ7XIp2JTxdIH-G1iUt4YKndJKstPv3wVdcDokoXsfGkbrBS_Igc1p4DkRQyxX2pKRQipdUyByNEXUXvt5vEHaXlVkaUqUDYHNkgCZM-c9XREXOjqCTWsVPpYSmOqzLWbg-OM0f9XnvpHzjkV3bsBJJmLVu_hQbTA5PwMzIM5IBneScQ1XHu0yEH3qlnfjM4uydE8M5jcfCogmwx0RP2PyOG5Z-kbLKVZGO4qKj0VTti6kBmrmAbSJp7DAvXDcHLtVjJiMGIZFA4IgKV-1wQx1V9oRwAD1ofSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=O6CfZH-JoGDRY-AAVQQAnETWFK3j_UtACEnP-mv2zrBPgV3Y2zkKyZ7XIp2JTxdIH-G1iUt4YKndJKstPv3wVdcDokoXsfGkbrBS_Igc1p4DkRQyxX2pKRQipdUyByNEXUXvt5vEHaXlVkaUqUDYHNkgCZM-c9XREXOjqCTWsVPpYSmOqzLWbg-OM0f9XnvpHzjkV3bsBJJmLVu_hQbTA5PwMzIM5IBneScQ1XHu0yEH3qlnfjM4uydE8M5jcfCogmwx0RP2PyOG5Z-kbLKVZGO4qKj0VTti6kBmrmAbSJp7DAvXDcHLtVjJiMGIZFA4IgKV-1wQx1V9oRwAD1ofSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwBPGpgb1lSBB5eCFd8Q8v-SLfh0SPhv09PIYpw7TKnobTeZHM0q_bI4cmyWz1-l54uM1RTve_lm2UJcQBJobkwfmDjDyvxpaaV6QGxGSeJsa_8nnWGxrSy_huVgbcKooBMrYRQgxvTV_-blsOAxji-rSOUd6x4o1UO-Eh48VgbadlIhDqY2zKZ4-tiME1Ut8PeZwjiyL0v9Pn2-D9ow0ubGWaULYozn8fH-YenoGAGKNhEpGeMgwJ0noBSRbPCzCafG-Tl8hQIMLNPY1Z272_J3HP8BehnOxytFtbiidgbEPpcv8KhWkVLL8V3nVh-AEZDMz2QfsmZIy63OF9w95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgEeSLjXTutLxt0BVpn3gdOp42sNAheoze8xBpmzfGACNM_SplYOUFSl7LH4jTdOetcbiRrFZSJePp0EVzGTk5AEtMHkCar2mboC1v2kH-URyhVVllmTrux-y3Qev9q1fUuXPMLkAAF863fMDnrwrUXigwiWzYOQ0qKdGdAmTpC49rcxKpcFNWsroFxcYUCZkIPFBLBTDZpFv77y8iTvJ5cYHDf0K6mVlgScvV74bdH71BVdVQ1aTeLcNwmupssWGYCTJfBH0qEXiYRLa9FILaKwOmVxm-uukCSujcAR0yrvVy4NQZoafq1Fnh7_83lO-N4t2JSmLv47k85ZGWEKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vymDLIuLN6L9KStMr3ISqMDnqg7cLHuUWLa5w7XN00qNr7mTfQ88mi6kfraXqsVPS1CnGU9zvslqecpYQWCzO6b5AS1_jnCUvKG2vXch7SOxeR-b8i77o0ulMsMqG7RTWw_6XlBP9YdxwNdHd6Bs8DhMFeYLgkuJwK7DdlMQL1T5zSLupoKPKgZgZm1TlTlSTt-zUyYkHMS_JnqWCgUG95PFwwLAcvT3tk2SSA0_W8FoXfQEXTv0ukIfr99HcCTAW2m0IVcq6oTfQeTCUbETo3UQUQHkFGs1_dMoHiPYBMSK1ktnK73ogKau1BKy1HFsXwJLJHSnIRSyKVXHo5hCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvbXH2R0fOwjovqDLsApaB1Cd_-jS0HHgHpgY1FTVxZZBUZ-WMLpe45B6uhkzXOYbyCcz7Te9QwbWHzUuQxslAPPc-IoD9RoTGJSjFFz___IF3qrT08KmNgZgbwzGv4F38RBvltrC9pfAV5snkC_V8KDYt9eeTTV0tRIz7B5gk2usT3-J3WREVsQlF4gQP2z0Yv0fA7GjJKNZ1GVWAuGAJGUxIvIbxUrkMgNfBI1Mf92u5PgWQO1_KQQiOOmYLw8CjjPceeFvhabBTCwoxL2cGDb3KdRjaKxImOqxpX2h_D0E-_3Hct7qDdHXFRRi82fGwYHkZwr94oigH2fioxfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr4eePoCc7F0G6Kyx1y5tl7TvH4t0aKfIUrxwkn6sxejJPhEQqCvlwSJv1G3klLo3fH3C4u4fjD1ut2ChO3N1w_NsETQW2Er2irpCJ0Rh4u-oTjDTEihNIqhyAjH7OFF5qrdaQ1sTcYSn3o_Yd1krszdn2A57RPPb5dKrLDq3-SV63FR6PSqDd6q2g4b0NkJHHwKPb7KzMIE_E-wqFWsCw4ycO6xQ0YDFcZ7MfDfzeKcdm_VmFiUXDSYN6MX_k7630K7HMoSnknPvVT3zRtddgUi8PJQ89Y59J6leL1RD-dpgUNtIhqrBD4dF9QVfosELr-LLDnhE_LDPfTv8A0B9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7WOqJjcMeQgWeMflslxcSI6UZuCzoUxVoH_vOAFsi3T4-FOW69f12MnYNuutJQxt9TR5CKZCj9094hMuy1n7HkBD7q8Sg478c8d4wowd5OBcwXCOgqrq3Q6vMxuGkubVfHefdu2G-bgyRKv855Ns7MzmPKdzYQF3ly7nEsOIjhCBgfA9ybQ5K10cv6bU7EWJnQDk-ha9HpZ_9NBb664s9cNGbMLGTkyoaR_8B62KD7Oe3TedM04TLQPiGMK2LEskx4W2lXi4w34uOR-OvtDjk0ezVHUqK29vt7qEpfWZfBpWfE2DyEkbS5jNnS7dHmRzOjf3TUEtNn4xk5nTyzyAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks2VgjH5Rb9G9EW0ZXPvrdhRmy41UY0umtVr0wCfgi8_ndkTegbk6sxK9SY7BRm7iS8clEAJ94E_K2c37WhjRjoT0vTft4RV_BL4P_cXACBVGPPqkQ-OHnag_Ai2oSFbZJBkHMKaIT-bmHt4G2DgpDkTQ5nWnIY7aRZezCGkdGmc0S_OTzPeiWukAfXvGUaL600f3HyntqqeqtVcGmIyM4lT2xfGSGvKbkBDdXFU4QninoFEDqiaHCvb8R7EhdKe-8xdzYZdTxhp0JtcxN4Zx6L7AXzxBAFgGXJqMJQbhK_wg51agbrwel9it0O4im_zGAGU38qPHnoHIuRLGsTKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUg8W7yg7J7fQuuN_dTxIyV_ItcwW8F4tlF9QPDHnkrJwI0BqZVHZccB29ag9lGWP0r5kZeeu9hkOxopX84a5T0s1vbftLdyLDN6TdZAAZmLxRu2rGutmsakmUugqnKpCPEVDY4SoqLjfdpYPbfXw6INEnYRAQiw83U8ereNr07zwr5fQrS5eZGXdh3ZIUQgJvdSv4F4Eeyatnz19gCfwqR_DHxyj8Tgj2t2JmUP0-OttusQn9mIoRCGatw-fwYUjAwNH9TkhzmLu4R0djoZwkOnvZH85nxHJpcjuKwo5UzugxyoTCFxuDQlIBsHKFqODZA-JnghOF6uyv1sTULevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpD5kfF75PyfJM5DbQAEmO0xauqVI4EroqESLWcwA3mWdbW77ze3HCgkbV1jBziuMlVicaqNzIhrb5dJRcFr8A-k1vjPJAOOGwnmUiLdnVrf4gYJuOTQSiqdxl5mLnERthy-8oNy4kF1nyZ5Kfq1761KTHNn3gaiSq8pNDnqAeCxSA2htcSSChP1XKvamcbddyIUSSnAwfYvEqhTxHs8H-09Y82doZ_QbNHKt6AmakGpNiNE2mqoNtoVK5rGoXzDagc7uFcY77sIV1euuizmEPxWMwrW2rVNIDqGQnrVFsREF3qyQR2UWqh9LSaBTbR6CumOi-7yNGVzZeRq1vxZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWt5bmgmT2VhEN3ijXWhFvSzYbLFT9v_2iA74clBiepVBdoSJIkZorvdz_MU3Eonbx5yP0G1At1WPlJa4dCYB2GkYtxb38bZNr2kMnPSLEBoKwNYYAey42_Dqz5lNSJPVQ_t9if692QXVshxZC4Q00bGMcFyWCzVTa-sEIgueN6AtacLMqb_ELDVyB9p_g-nFCSMaJ6VgFtcNwXmp6HDvG_6EYuC_frm37ouujmkIE6AHo9VhM1oxhZjXZAYe3Iar1C3RpNv1nPA9U-4UbabSAtquK2xvMjW8FQzzWUGids9rJ_DlzpH-AOQXaFli8qZy2HP_-y4FNZk9LApOvZi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtGdnEwov165cKw11qp7jlpq7IjggvCVSlS4k46sXO4_PS5yORQ9s26bmrqUZjY_K53VrzqDbao50brki_2NGv5dG7pN2qy-N9KybFbWv0i1STBTztXENhgsvR_J7SvnV35tiwLzvme-kGc3ZOHxZzTa8d2OgZI-q-XDNCosY57b1cvVpJnSEOjvl4q0yhOxpS_D3-amigGyq8frNGRj9ofOvJVDoeK3bqOwYw7JB83yifEQIVQUB5w6ILPo4s13lzWoniBreT0DU_1fIulxMYoUvoe41i1AaGfbIJpxfGPepTWFJ31YMX9TPlOnVOVwMvlp1nZGlbOQPFbb-wYcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMTR2x6lcTkg59mhN__GbJpwM0Br08Lt-j6VqVvCvDgUhu4rJOtQEbvUQTcwv8xyZETf00JpIFbMHjF7hVngXhTl9c6hg3Uno8WaL_6j3GrZrOJO8XNvexgvdIYqkB1issh3PpuTwiNPPAMTwMvIxkOB0lRdT1jC1OaYYJE0lbS5_AgUzzNQXLEoLptoMrbAxH2igwTi6-Npz_z37EfhKXf4meDfTVBjWBQ0WBB3OvdaLz2VrXBYnPxzCHILUSFtmkLPhm4uYvEuHe3PpliciNFmO-zY1hEBEhAWvf0I07xkX2xlFNFna-pPwCHwuTC1tgBj5Nv_uTqfMoBHoGWEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwDLgkNxUIFwEy8zqECn9cJQb6cj5GILmZ7Win63K43LXjyyUI7EWP5XzszpaK95x0QfJ6wxKX0_ACbCt55vg043GJ87qESANH4OzzCscJEX1F4T63TC1AC_AdItuL7UIgo0u52dRn-mt6fxqWbjSfZ5iOufx3J6VtTx08WkWWjVhD99iUD0sAxLCnDuAx_Io5gLh-dXqqM_tKerpf4n3CoFyWgY94zeYLe1aafpWYwp9bud1QG2cuA3gGV3Zcnv-ffW_PzORNzxGNh6pPc3u1zZnae0EN2xMiW1C9KTVDNmUkuwj32_VAxaLepwkNcwog7peLpGG5FSgpBaTrLdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=acvxA2fo_n3U6srkEhc4XO1a3F3d9uJLOxI5mZCOpicDFexdkT7VWoBlHc3RrZB8lr5zRB8CU8F-9B7ch8zT_oWvOcF9FVkCtblqDj9j2r0tL-Fz-8vFHtcX6gyr-e4lyg_WBpyYHfPygiCJlZV7nn-arE7l3hb1gYO35TEwo8rytF-Yjgzpeb_fBwNGNiyWKHAF-xXy3trZzLYWjv7J7ebRSUIbeIFehew7eXMPGMmI1DQP9t6ZrKhsqJR01aAPGRq6s1qV89tLNEMBbxZcapjprhwRBTVHGaCrzGSkuzTgqXgB3GLHggzrzw_9Wq864zFLkQdYnTxMtpQoXjdI3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=acvxA2fo_n3U6srkEhc4XO1a3F3d9uJLOxI5mZCOpicDFexdkT7VWoBlHc3RrZB8lr5zRB8CU8F-9B7ch8zT_oWvOcF9FVkCtblqDj9j2r0tL-Fz-8vFHtcX6gyr-e4lyg_WBpyYHfPygiCJlZV7nn-arE7l3hb1gYO35TEwo8rytF-Yjgzpeb_fBwNGNiyWKHAF-xXy3trZzLYWjv7J7ebRSUIbeIFehew7eXMPGMmI1DQP9t6ZrKhsqJR01aAPGRq6s1qV89tLNEMBbxZcapjprhwRBTVHGaCrzGSkuzTgqXgB3GLHggzrzw_9Wq864zFLkQdYnTxMtpQoXjdI3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=JSl7AjvbHCvcn64vJlH4EGZQIPiz7vI6V6dmfILVO6_OEjs8ev5R4cMKcRfHPu9wWu6upu0tvAFeQ2vhQNqhUAziIgQC1pfHS8Y1hHlYNQPXA4a3P_HpjQY8ZwRr17QGjACLB-YWsUsYuieJ-4QtgtFzso-JAam5jJBDWPkEj67ojdS7fKg_ZOOIVoOMBOHwJ_xDTuoCWeI4vGXWocafxTFrVQah0pqkt-zD9TZXOz-sSwSkusSO1-nL6lEwwlfmH1m9PxIRuWdykAKMGWNTKV0wZMk-XhSVeWSRRs5DA9BOxZAyRylrsmEGVy8K3VH6tDPnAflgaUZqy3CvoC5rMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=JSl7AjvbHCvcn64vJlH4EGZQIPiz7vI6V6dmfILVO6_OEjs8ev5R4cMKcRfHPu9wWu6upu0tvAFeQ2vhQNqhUAziIgQC1pfHS8Y1hHlYNQPXA4a3P_HpjQY8ZwRr17QGjACLB-YWsUsYuieJ-4QtgtFzso-JAam5jJBDWPkEj67ojdS7fKg_ZOOIVoOMBOHwJ_xDTuoCWeI4vGXWocafxTFrVQah0pqkt-zD9TZXOz-sSwSkusSO1-nL6lEwwlfmH1m9PxIRuWdykAKMGWNTKV0wZMk-XhSVeWSRRs5DA9BOxZAyRylrsmEGVy8K3VH6tDPnAflgaUZqy3CvoC5rMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfluT13YC1QZx87BGt9bq2WBELGlKkar4kjDCXtOo5KBbzNax86l82I391ZJFWS9Ld2OxbKKhAJ-bC4QY2q611fZ0ywczlHNCsgAOhcGZU-iVRBMzsCVYs49YTCDL3aXH_prAVMYJLJb61KbL0xwxaTfUSsts4t5pmlnCXApUUpnre4yAUayvnYYaDBifZo_adT242uODZgVLCiIf8VtggkTKyynyU8F89W4hvGhfwIIxQnVCHa4ytl-1sBOvALjPg8OKNlMhEnfoqmqg7WHwIItGYjZF9omDKsPu_T7RpolnEXD44TJbEvrdVYQhX2huN5GuW2pmbs-63louxcbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_6YDEJYNoUVXdaHXAXJMMFGlIPfCgyu84Sv0_56OGvqGzgQe_ORN83OFiqSQiap42ufnOWy6afRgcgLDdAyKoP4-jXvtGTaEwhNILOF9My9koMAe726YIHsydErRTXaDQOFbfngGDpPucKZsd0wd_kNd4RUK5U_gtG4wny-yEKKtAimpkgI72uImMKunO3KWmeXj7p2YA4Koac99l3O9s2Cw_UbvdT_FXbZ5AULdFdPpl8pRVDNiOlHMRnh2LDiWu4ym-IHX2JtVCLh6z2Fy2op9L6bIIVNU6ynCnZoMaCEM1UBs72fBVvPFERtitdFAHP6HPrRWr_WerQETPJ7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ-asy9UfZ5bSAAoa_OIMXB0m0nkORSo0J21lHi6wnXdcy_d1mMc8WVfQTUKUGntUNiZghMiGPDcZLVdWSIlM-gpTAfKmCE3KzFZ6n3w7lMmF7HIk93ArV0YXyi45PzTb-r01o68iswIq5sx422ClP0y0mYarLPDjsMbzUDsHPJrJSZIUSpIodUq2GMDAICMcrkCD82TcpcQvb741h5po7J_Sx9veIfanden4xx5GIcpA6sgiMbO_z6dYH5BM0zqzFCm8AwLMD8DhuI_hFp-O_p9EqTjiQnA3Nn90xR7YPeitLa6BEzH8bxg2Dj_MuXWFoRXsgVOdYqc3BoM5rLEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=O2UlhPcOdjvtXo2ifc1Y_30dvNG10Jyjc0qG4a4_YO1mqPTd99Lsjz8hSuf2HyK4tEALdfCc0xaDs_AVvfQvhl5p4SXmoB2cB-nyO7Oztv8OkOumMQEqHNy5b_vDYTCEP5BEOHJ8_JIrE4nxdgPmf72kf4urBVvFbhaCFbkjfxYjSCoLhW5CS9GjU52etGMmk4RB8MbBDwlVm1R7Km4W64nXZo7Z1AKxbDd3WX7GwC1T4RbI_ApejzzcYkH8qWAEH6wo59pSXkusIKRNJ_eiuqwIfHgeUysf_3ci8LazAwvDbQAAxm1F18tZf2Px7lBqpagtUQMqgTg3X26EI77MAmHgDNrdYCgNQL3MkBnlJT0NecGVmz-scTRxkI-RaZTFPE_EYcPSIBWWzBUlMpz0Jkgga7-hloYXZ5JEgSIQsIwCmYWAzpbnD_PGiFf2nEiJrpogvIhn4eyt4tMy567UEm-31BCqaEkmMu2N3O8-DWKXjp8yu-H2v8TOxqA7qBjfv8C0Sri5GeQj1KsOAgNnXVy8Y2uiIm96r2OdAWAx2TjWs3ZMAQqOLnMBcm3ABy64-XmzGOO65hIKsGTgGZ31x0myVXX0JyPbsvSvIoGyePNcS0lWRfRgUCuJqspt8Ic6skn7tiJCegCa4D70YzWywoZVwtd3Gzy2u4JYC2QFjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=O2UlhPcOdjvtXo2ifc1Y_30dvNG10Jyjc0qG4a4_YO1mqPTd99Lsjz8hSuf2HyK4tEALdfCc0xaDs_AVvfQvhl5p4SXmoB2cB-nyO7Oztv8OkOumMQEqHNy5b_vDYTCEP5BEOHJ8_JIrE4nxdgPmf72kf4urBVvFbhaCFbkjfxYjSCoLhW5CS9GjU52etGMmk4RB8MbBDwlVm1R7Km4W64nXZo7Z1AKxbDd3WX7GwC1T4RbI_ApejzzcYkH8qWAEH6wo59pSXkusIKRNJ_eiuqwIfHgeUysf_3ci8LazAwvDbQAAxm1F18tZf2Px7lBqpagtUQMqgTg3X26EI77MAmHgDNrdYCgNQL3MkBnlJT0NecGVmz-scTRxkI-RaZTFPE_EYcPSIBWWzBUlMpz0Jkgga7-hloYXZ5JEgSIQsIwCmYWAzpbnD_PGiFf2nEiJrpogvIhn4eyt4tMy567UEm-31BCqaEkmMu2N3O8-DWKXjp8yu-H2v8TOxqA7qBjfv8C0Sri5GeQj1KsOAgNnXVy8Y2uiIm96r2OdAWAx2TjWs3ZMAQqOLnMBcm3ABy64-XmzGOO65hIKsGTgGZ31x0myVXX0JyPbsvSvIoGyePNcS0lWRfRgUCuJqspt8Ic6skn7tiJCegCa4D70YzWywoZVwtd3Gzy2u4JYC2QFjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyZaegZN9iebQ-1OxRJwn_trT0zn1tcxHf-DXfR0nC54_5N7OOCKV13ViCHbvA-Fhc00I70zDf5ZjZmsJKObqcVIJekqYVEuHkw-ujeoQVw7diYB1rNMRR1VnB-pNtBmb-F8hIg3cWTO2TyRYSRHqqqIrZiaCaC-vEbmh5-kHFaZf11dcUqzvjz9EEFCMdUM4ardBdvM65XTRWFg5tCD8TaASUaM3C9kiLIFlBSPn6a6yYpRqBC3MgHcxCItmgKfTzZfA0OEZV0akTyrXDeW67EUsOFu0Vi_wDEDNToC0IKwQtK44ivSavZuVmEa-TwTPUhA8UG63eUDME2YU7k4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVLdvK9rkZCCzyJ2JCk76CNc7LMKwVzO4rduIuEwVWYFnBtK3GSWEeg98wZ0Iq5oRofLwX6-pKL3V_IcC-rHTy2FzuV83A_i-iEj6u3pgZcbjguRLQ3QT7c7Yq0uIEDCrA9rZJUqLZTHP26eVnNbceTzsOJwVA1ElXB3EAQOCkvGh7633fkxVchC_O8ldDRfekeGPwgIhe7ptt22wYhgpTgvneR1cAuik4tT8Kxldpy2_c-rq0HvJpOcNV1O5bbrTz261ojIWl_d1NwHvGbGDuzhfxC9D-dlfL4TwO7yMzsfqZe5MRzDfw-u15Mj4DVAKniBL_bs2B_IKOcH_11Jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnrYkD-doWUXcvNkAl556k4id5e5d3k7bnKugG1PIgEW60SyPCAazYSdbBaBmsLCy4iV8k-xdI1sCfZTQ6NWvmcxr7iRs0LxXPl28mUGC-fiC2oSA7R7jkJyRlaysVoiHaMCv52MJ7in4v0RXLR18_-RLV_oo5oPsFlgnxBHcuJbS9blaIBvGH8uLdCho15ppIWy6UwFBrfEFkJiUyaWmfw0cI9FXZAOzCtdDD2MqNlpOeILKGf-3ARgQ_-3XpyzwU18FnqQ_pNFSX-SYCuDcLT8HenH8az5W_m4XnR9WwqLGXQm1LHHxlZdAl-GEE06cMPVFp2a_hO3g0ji5Df6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFr604GSnk9yGbRspMnCvuVdV4WQBoJd4T4bblmfC_HYPa1_Bq86_SpanLcEd8rsf9Zt1b5mPGI2kdcbJFVDDxUySOGvYjhO0BkX8NiGuVCLizKo0pO5OWErrdeZQLGAGhqokF0dGq6JO_klmlPwM1C3tJwXxZizhrwu5e6z2yPuoZ6jNt1V4ZALG2R_jQrsgD5wY6FxgOvh2jBOsyGvaJ2brxqSuL8rnMXS2DKBLEvU3dqPwMwlb6ol0-BBXgWrKEbWKNTgzyBNCNtR-Cc1OYjTiLilufvgGMeASVDvWMJMKfjBvfyxZG_d5rTzmZXood5OOOi49RamZ70Bu4b30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K63KFVYYrD9GoieQp5raZQo0RiaL-562LaFxRWP2AP8SRzQKBgq0H5YUQzj0UqvXWqnBadAopLBZDgXGYA3Vn_UUQcTUdQ0aDm2comzOtoQUUYVf2a8yiL5LUhbX_kOnUlqp0eHVFquX6gOS0N8QTfZGy2_KLxtinLSCktmkyy-9XPu94bxOJFdOduC4AX1mjC_mygA_Ff3faYXpgZz5cD9-Wg_k5bIheimGFcHa7Swn9qb9U2U6zfHpN3O_t8W5tsPji3Q2THoMIsYXDvHeYD-56_A2NA8wAfh0ivv3Q1qcfA-lfoIqPCO4MMB2H0AVC8bO2CQRjuHlQLoY-Kbl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jfxhvj0ACnU-P93xJQ885WuhBUsnwMyhZsq0QIqbwduAfNcpTkOhDASm4P-PnED_gY0fcZmFD6-I8jP5hO_TeQkRKCWtQ1moECHTroWDCuMoitSdyX6-xIXiyY2aqauClvdRnIJU5YpH37bQYVUcvD2uNkflHUeU6pInuog9YiG1NESSyXDjWFw-lBm_fyO0-9rhcaBVhjMWq7WwKPh8q6aZGpiDCjII6b0m1XDPG9Ur6J9U_LskGNpTYI495R0f2UANsVCajdNAsWdkQHbPNSTpU5tSontHF9Nf0xKVQPe-dzmKsrLkgRnBo060ewJtMJYa8u7bYt8Xmwqw9yCwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=Ha2LYZlp9tAugS-Y_auBNPJ_xCdykEYuTnTYTQrGy0suigW8Ho0c08ZSsA5dFT2b-OlUznxRNraoZ5iQXmFy2h_jYWjac40uYdq7wfMe2zwde9IZlgbdQjQNawN9vjxzXwjHFU8W2GQ7Mf9zgJ54CUdRDiCdWVRaxb61pgIHylucOohz4wQPb5wdNGL7ssz_mcIzHTQN9LRpYPVTpcL2PIGcmqu29l5wR5Xvc94-H7jr11ceVYcIRxrjqxgIqDj03zTIIVRWhdLyZpzo_quu1Y8nbHZAJl6q8ScM3AEYX5WeD7fJAiyRIqsBAHRhARBR5vcyzKMBCyZMv-r1BSiBcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=Ha2LYZlp9tAugS-Y_auBNPJ_xCdykEYuTnTYTQrGy0suigW8Ho0c08ZSsA5dFT2b-OlUznxRNraoZ5iQXmFy2h_jYWjac40uYdq7wfMe2zwde9IZlgbdQjQNawN9vjxzXwjHFU8W2GQ7Mf9zgJ54CUdRDiCdWVRaxb61pgIHylucOohz4wQPb5wdNGL7ssz_mcIzHTQN9LRpYPVTpcL2PIGcmqu29l5wR5Xvc94-H7jr11ceVYcIRxrjqxgIqDj03zTIIVRWhdLyZpzo_quu1Y8nbHZAJl6q8ScM3AEYX5WeD7fJAiyRIqsBAHRhARBR5vcyzKMBCyZMv-r1BSiBcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQUAAX7a_dn6yuY4Q8E61-4JzWNV6rJmu0MHJoPGrvCHSl-R1IPojWqNKZugWZG6-kyc5Ay_ePWMTp4t0NsN0VBY62utHRZPNOnA3qrsaTMhleVOKaKOqqQmLyPIdtNFb3iqN1vSua0jG1riCEEudmYXjP_-xdX54ytdrddADWDlJ-VgCTUfonVXNvUb63F21ms-BR6rwBqu3AtMYxH1LQMZjuTtt4okcYgxSi8KnntoyZigGur-gIWXX4lmdE8PxxOdBr0nd9Yvzs9gn3IGQ759-d_iTU7WIIowN8Xy4_IfthAtSIIefTTJSerdNptmyJ8t9Ursi7OBuj2bxEHHAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4k07il6isCG_lmulHyFkf6JBPZd7G2QpqZlrdV9ddSZh7sSVPrgFNe429Vgx_nL5Fq0dg1PkLdxbQxeO-Eys1mpCBJiJNPcBqvesKqGBEnjc5j-fhmSEKaHEuVlld8-m1crua4BcF9PKqZ4skN8osTsf1IhMhdJt0k_m5oalL-prAT222XRJtu8JThrpt3mh07o2S89HUSlRQJknkw2aEfENe8vUujyeRGgpYQpnNOCjsUkuIS4q-vSJnzJYXB1la0dSTG8dgmhIJrQEiDwoQHdRqBoCini8-iilgDX68vmsmL9qlSyIKzmggrNHtMdClA1SAHFxyVsARxzg5uQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBWb5SgHj0AsJYyGYSExJfG5wMNThUV-aLrVTHWESHfMOdPh-5NeavulS3jt3lk086McbucY9-_3d4rRP57jOuvT0Up3-M1kFE96l5qbxEls9q18lHBtm2uoo9VWVsRznSCbS5Jdu01PjihxNx-hewRONCmkNAwhp9a0B4NRMg4anOdtm008-M8EXjlFnZq2frp-7h0jZ_MAuKmd9Lxx7q3zRhoQLydJ5sTi0HZYp8Yct10zoq290kM2A_RB2vlWVueRU5FS3rdQnJ7zMaTQob14hqjaacD_HCKFwpGoc0jAxrZ3BehT44uIsV7tHOBOaMt89p3TZvCP6uhsM6i83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIvjC2MYVgJmuahvftiqKnKZ8-DDOu6K8QS6m2pJQyMHXhILOUARB-o_Jzif4iR0sQryOX6y5cIhkcBVcKKpMGF4LKrWeZmX5NjvFEKNesfTbWiPTKMNHlvTt6PFnQoXqJXoM0cietnB2e2k7qd7nx7WTv2TQ8Ikq7h_HYZ-58_WAJa0nCH-pvO7uhHVQ1vHMCBF1OF1Z0LoKaI75-pAJym90oNw8KY53QJ7hJIvX-L891ifQ4CVQwCoDdKA5iyFS3KnLwvwzy5SdqStM1IekAHNsCLEp2lUqWU1xkTE8GqEdKxVekeh8ouLtuSbK1WkpNf9x9zX4JHqovRaRH7GAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFoglpdn5-8geT7WLHJmNb58ad3tx35_0Aox3aZ9MoDPXCnAC5b5OdyDjbYeNz4Z9qO2PTAWBUJbVS5V3MSh9JnZggjBMLXm7RCx_QmqY5RnKK3hczu4_oo0HcIMizFiUUh8aCSLNHDG05YcyaHE5XXhvNRGzCvqDJNhT-f-9cMJep8MGdVNo3kMqnBnc5_5SkaW529CB5zVEmKeeOwmFWzEdRY9sptAS4ih9jtcZ7JggIYkYrc_jstma5nJvkS5gysgz4RdabQN6jCzH2kcRfy0_YAEFLWwE9SW-J-jIUfZlBt0qJ_SvO5UlLkrr2lyehVaJ7V_HVLLq2aHzipzQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI5ehr6gpQIztkNP_xJD6x1yLaxVYPflkJ8S2ofFuW16lGocAyOnBGj3QYO-w54mm1QE_9Z40B1dOJKmBA8dnh3Ipj_1zyNx4tZl8MvOYYNMDUMlYq4ArzlNDShgVynplYzKFTdhRwDhJ4U5doxrqB6FrVcIh1T2YHn2YKr2mvZHMq63nJ3JUJTIh1QlJOu39OAQ1-g5Bnuvyk2aWUFo-G5jyb5LoAVKHkF74Tj7xBPQbOr2V_bz1rgKi5xob_gcDs1CHb8FY4AGVE9xvMApXnHR8LfffyVb_CqOJ8WB9HmtU6gz35rl8sz0TcvvOk7mXUXfWeO1K5DaI_PI73gtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB-8RTT_WdjDkg-m9vjum24hFH833dEJ99054z8W4M-NWmg68tJmCjfORHIv2kHfMawz9tD_H7d5W1xE9bPToZNzlbVUTwMDyF9lraa_4Mg505QAfGJAmJllahXTs7hHmyCK4MCy2x8w-fnKXcVMsBAmzA923itnve5vrwVaqKcTpXDhaJLDvxc-qdGRnqA3gDQm3gJf1Az1ncQyRnSE_7ZBT9zgrGT9fjzJazcAit4svpaD3-o6BJApJngZRdfqxJrPoVZepLuPjDBJPsvKvcMlPP9BmTtCSbMkfgzHBvNCtMaHysQwcyNYSdk188JUUwhOwDO948cR8XqkhlrgnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK4F4P-ESUkC5GlS8COZHO18qibRC9btKKgoTRD_vTWT8vhXn3VtaF65Tovh_e4cEW88R3YXRdU7rlTNpt2MZzrj4A8nc37vRnMErcoweA4jBxt5eYSsV5N9yaEtyKlNun-KLTXRAqafNgiOopcoXn0fCzY2TdvYmdgbWjmSh2MHApVsFNh4oDj6mA_KH6Nxe7N9AXF0o9LAoc8m3jn4HcTnnA_YowLByQKuFpsA_fq1XBer3OVUGozbGU3NvzflXSHgNib-gW-1Hm8-QzHdBXfnTREPpoNSlZkZx8Re9oXVZKl7t4ncvDXqZH9kt9qRv3nkVvVbmKxccOEwObFAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sra-tyTDLPUQyALdxj6TgklLg5YlOmkueZoFH-RxeBZFb4hD4YKTqgdBr4EPX2C3pcHtqPv2PeWsGW89z0WgYNEiMcDxtAXstIvxBbK3aHIcyyq17sTwV9xvlsrfy8icaL4eM5yHfG5JHRb83_RszqXsS6uM_WoeXg3ddNEwLcpW22mSKydqgLRESpbpySYFixw0E9n6bD81WTcFaqxPSa4QUVAsjvOwO4w-dMNd29AAbuAJ32CTVyGy_MblHFz48mRcPFa41YRBsrXFcE2Q4aHQa6CNbUmB4EDhxJAYpxa-0VJJZ_GvcmnMFWi1urdQSBjAhw6qHLJtBqSQGNwKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=C4vDt_f7la9NLGr4lChzzKHl_8O-Wbs3brePu59xXwFE4U2oaHchr227Qyrh6Vsbv94iHAewBIs9ZKsdSZiI6qcfNIoRHqAD2J-sk-W2orG0g2oMt7Y3jif7n3467Fqxq_jmIamWoN4bP039I5evaN737I-xZx7x_iX1gaRUnhh-7UaVYV9LeqsBRMd8mr5iFvudmfV0UClWfcGSXBBFShs013IRG-Z7l-0Ujdo_f9QQKNG3mzIsihjMYaFCP6Mn5Od7Epi9xbbfHZZ0kjmRHpJG44qxCh8fkte6oSlfk9C4fzRevc6Wsh6FO70TH8nfBBTQ8_C9QERngWewNQf8woWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=C4vDt_f7la9NLGr4lChzzKHl_8O-Wbs3brePu59xXwFE4U2oaHchr227Qyrh6Vsbv94iHAewBIs9ZKsdSZiI6qcfNIoRHqAD2J-sk-W2orG0g2oMt7Y3jif7n3467Fqxq_jmIamWoN4bP039I5evaN737I-xZx7x_iX1gaRUnhh-7UaVYV9LeqsBRMd8mr5iFvudmfV0UClWfcGSXBBFShs013IRG-Z7l-0Ujdo_f9QQKNG3mzIsihjMYaFCP6Mn5Od7Epi9xbbfHZZ0kjmRHpJG44qxCh8fkte6oSlfk9C4fzRevc6Wsh6FO70TH8nfBBTQ8_C9QERngWewNQf8woWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الان سه تا مدل قوی رو می‌تونید کاملاً رایگان تست کنید
🆓
برید سایت زیر ثبت نام کنید و به راحتی از مدل های زیر استفاده کنید
✅
✔️
مدل‌ها:
•
z-ai/glm-5.3-free
• dots-studio/dots3-note-prev
• deepseek/deepseek-v4-flash-free
🧾
Link
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تلگرام برای دریافت پسوند دامنه .gram درخواست داده است
🉐
اگر این درخواست از سوی ICANN تأیید شود، بیش از یک میلیارد کاربر تلگرام می‌توانند دامنه سطح دوم اختصاصی خود را داشته باشند
💎
مثلاً
@durov
می‌تواند durov.gram و
@monk
می‌تواند monk.gram را ثبت کند
☑️
علاوه بر این، کاربران فقط با نوشتن یک
پرامپت ساده،
وب‌سایت‌های تعاملی خود را مستقیماً روی زیرساخت تلگرام راه‌اندازی خواهند کرد
🤯
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAhrVZ98WT0-TJ6lw9R6a-8ZSHRJ2ng4uMBqeRNP04PZoT5C5_PUVGYwt1Btlp83XYNvmBZhI69jymhJjk3T6g7ZK0q_jxHH_ld-2T4aDyKpzWmnjyhFhRG7ZgAXgmj7aP1vX2DPNI8guQc6X_t5Lgco5flT138Wr_TgMu7ohK3l_4UI-NtHmrgVT6pdqOLAF9vdUwzh3qHFqc-hOGDxFiUPSKWyvc3rBDFIyzdIkrACtvGhqcsuA54SrhkLtjswYgIR7cqjuUiFPKRIeDOSwKWZ7m-oFrwQJQx8FklL-q-4tFIRi4FU2Vmem5Oafo7HMsZAiSaQvE2w23sGEWJ8MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود کد ابزار قدرتمند طراحی گرفت
🎨
تیم Anthropic به عامل هوشمند خود قابلیت جدیدی برای طراحی رابط کاربری وب‌سایت‌ها و اپلیکیشن‌های موبایل داده است. کافی‌ست دستور /design را وارد کنید و تغییرات موردنظرتان را توضیح دهید.
🔥
سیستم به‌صورت خودکار کدبیس موجود را می‌خواند، خودش را با سبک طراحی فعلی تطبیق می‌دهد و پیش‌نویس‌های متعددی را در قالب طرح (artboard) تولید می‌کند که می‌توانید به‌صورت آرتیفکت به‌اشتراک بگذارید  (The Decoder) . کافی‌ست طرح موردعلاقه‌تان را انتخاب و ویرایش کنید، سپس آن را وارد فاز کدنویسی کنید.
✨
این ویژگی هم‌اکنون به‌صورت پیش‌نمایش اولیه در دسترس است  (The Decoder) ؛ برای امتحان کردنش کافی‌ست دستور claude update را اجرا کنید.
✅
🔗
لینک دیدن جزئیات
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تست کردن مدل‌های هوش مصنوعی
🚀
حتماً براتون این سوال پیش اومده که مدل هوش مصنوعی‌ای که از یک سایت دریافت می‌کنید، چقدر به مدل واقعی نزدیکه؟
🧐
آیا واقعاً همون مدلی رو که ادعا می‌شه دریافت می‌کنید، یا یک نسخه‌ی ضعیف‌تر و متفاوت؟
👀
✨
توی این پست، ۲ سایت معتبر رو بهتون معرفی می‌کنیم که باهاشون می‌تونید مدل رو تست کنید و خودتون نتیجه رو بسنجید
🔗
لینک سایت اول
🔗
لینک سایت دوم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
