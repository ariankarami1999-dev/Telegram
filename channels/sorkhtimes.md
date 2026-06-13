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
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-133380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkxzrPdSu23JQRs3he09VRK9qzztFPsmxp0bcHkC__cLRAzUSmuyJDGhphwmQaVZBs3swlX5m5nsX7n54MZ7jfW0RnUbv-gI4fsj6pFj2XaKQbNlJ_Yag1DsIeKQKe-e3uRbvejyoVpFXrvfor59DTTlxr43WQa_yshYp2VHhzNCr8a6iUut6KzkaHsPjBoKoakJXL7gdljKb0Iehf8HEbMobyiyVxYP_ASPdza9pIJI_A0zgGX-6bB5QjcDgIrrUbXRhKgd97jN46tf0XW5nz3XcZtLpTXUBnFfE3YInOw7nD8_2i3KP8XDqi2VOF1hnIuU0QtosK-3y-hdUE1Vuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
دیدار اول گروه C جام‌جهانی ۲۰۲۶
[
آمریکا
🇺🇸
🆚
🇵🇾
پاراگوئه
]
⏰
بامداد شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/133380" target="_blank">📅 01:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cje3My5plPQY_Mfi24JsQfA410xmMnaxbCmvxr20yUVG8gSj3fgO6OuB6KB8JkLLZ06_eAfQ6W715mrlTeBVskIdc8q4ifyEZUldSGBdw2ellVRvXPJTYEJ6pxxF4Wn6fTzRen_owpgf-rtvENcaSdHodQX3f0IF6QX4L6U2rL-DYJevvcSdAdJaV9OG_PdOHeAnkLPXXZ6XNaRxwg3i8SrrME1EHHqe53cmkcKHWZstUyCabsDQGrOjxxvG644SIPVhM3kihgLFYVfD3BzeXc5A-xddztztAyAG3Q0ijeR5wrJ-6mEtCQRwBXck7IPInks-mTz0gtoEDoT6eELczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
دیدار چهارم جام و سومین و آخرین افتتاحیه رو آمریکا با پاراگوئه از ساعت 4.30 صبح برگزار خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/133379" target="_blank">📅 00:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/133378" target="_blank">📅 00:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhinUA2r1mx5xyfXUYz2Z6W3ipuYbt6xlmSaYBDR-MtMhDx-UOevoPMs-qe7Ia-300fLKUJD4bgkPncEE4hhx9ucE1WTmqd7eay9SIM-Vo0zHybNqL87j6S4svTSQ0--2y0F3W0PakPHnBu_I4H52EEcXfmX1hDtI2d4x6t7gWqzA5zbJZpTPJuqrf7avUUUetE-g9zdH4tdDHf7t_FDoiyt8FgNmvRmUapgpIMYzbeKfSdNWEb7K2gUjQMoKI4w3YwuyWt-IE-yVcVH4oU17yzGLjSF6iq4O1dM7hmb_YFOOEHVdG5mGlP-aHngvwqAKdAeidpJN-wyea4nRwQ1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
برگاتووووووون بریزه
😳
🚩
🚩
بازسازی ورزشگاه آزادی بالاخره داره تموم میشه و این ورزشگاه بالاخره شکل قشنگی به خودش گرفته
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/133377" target="_blank">📅 00:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/133376" target="_blank">📅 00:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=G9uw2A98Gb3_OAFX1TZ4xdlpTtJNIJQp9lPw8VvOURDvpTkE8cT0T4L4-tgOHhOgcPeAyVQ0UkoLt4LkZeMIlNGHrk7YkA9CwXrZknE3Kb9LB9vQuw_SaaKWBxN1g6OcfDd4H8Zi6FJRWngyvhEGft2IWblKZvVsaT3OlsbMvls8NCJUWdcDm73i1mjzel4zFzsEf3Z5HvxaseXxm8kkThqQ_lJxMF9IzYwM4jb_FBZFtFlpf5atq8eXh_eLiiLKm6h9MQEyct-lxoX4-tN2VA5jpdSuzosl1vwK1AFD4P2oxEJf8R4eGf_H75g3gL5Ql4FiJZQ5J3JhISNxEryOAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=G9uw2A98Gb3_OAFX1TZ4xdlpTtJNIJQp9lPw8VvOURDvpTkE8cT0T4L4-tgOHhOgcPeAyVQ0UkoLt4LkZeMIlNGHrk7YkA9CwXrZknE3Kb9LB9vQuw_SaaKWBxN1g6OcfDd4H8Zi6FJRWngyvhEGft2IWblKZvVsaT3OlsbMvls8NCJUWdcDm73i1mjzel4zFzsEf3Z5HvxaseXxm8kkThqQ_lJxMF9IzYwM4jb_FBZFtFlpf5atq8eXh_eLiiLKm6h9MQEyct-lxoX4-tN2VA5jpdSuzosl1vwK1AFD4P2oxEJf8R4eGf_H75g3gL5Ql4FiJZQ5J3JhISNxEryOAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حمله تند محمدحسین میثاقی به منتقدان تیم ملی روی آنتن زنده تلویزیون: آدم مفت بر از خاله،
کصکش
تره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/133375" target="_blank">📅 00:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🔴
اوسمار راهی ترکیه شد/ویرا شنبه شب در تهران
🔴
اوسمار شنبه ظهر وارد استانبول  خواهد شد و بعد از چند ساعت توقف در فرودگاه این شهر سوار پرواز استانبول_تهران شده و  شنبه شب به به تهران می رسد و ضمن حضور در تمرین نشستی هم با حدادی خواهد داشت.اوسمار احتمالا در…</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/133374" target="_blank">📅 23:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همسر اوسمار تو یک استوری از اوسمار خداحافظی کرد و اوسمار راهی ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/133373" target="_blank">📅 23:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=txC88KUYDitcSm3rIrjl8EWN0z_e8xancu_iVfYWjCOfDWDdkWHIipKZs5H20cIjNhpVegWQWI6tBZOwQHBDfNHperHvTPjh_d0Mj7oUUmbaul_Evg3BVRFK24oNZOdMEwQXhRtiMYO-SCTNkGoaHVdbcZ3tenN6zxGG9DSXDk6KLuJNngBKKZ6znpN3Ij3rQ-qP63ikon3DGeccHc4fmgJO7Mhtn5JVQF1rLHEDURhFIU_dcMb-GNb8acDg0zJyACvIo9Wrhd9L9x0oQaR2VPH4svYMkAuy6cUVBTuU9wJp5UpLpGjg7IArsAjNDd4gsmiOTYgJYXdB9cg5OW-VnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=txC88KUYDitcSm3rIrjl8EWN0z_e8xancu_iVfYWjCOfDWDdkWHIipKZs5H20cIjNhpVegWQWI6tBZOwQHBDfNHperHvTPjh_d0Mj7oUUmbaul_Evg3BVRFK24oNZOdMEwQXhRtiMYO-SCTNkGoaHVdbcZ3tenN6zxGG9DSXDk6KLuJNngBKKZ6znpN3Ij3rQ-qP63ikon3DGeccHc4fmgJO7Mhtn5JVQF1rLHEDURhFIU_dcMb-GNb8acDg0zJyACvIo9Wrhd9L9x0oQaR2VPH4svYMkAuy6cUVBTuU9wJp5UpLpGjg7IArsAjNDd4gsmiOTYgJYXdB9cg5OW-VnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشاگری جنجالی عادل فردوسی‌پور: فدراسیون فوتبال بعد از اتفاقاتی که افتاد تصمیم گرفت سردار آزمون رو به جام‌ جهانی ببره اما فهمیدند گاف دادند و اسم او را در لیست ۵۵ نفره نداده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/133372" target="_blank">📅 23:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
عراقچی: اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/133371" target="_blank">📅 23:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
🔴
اوسمار راهی ترکیه شد/ویرا شنبه شب در تهران
🔴
اوسمار شنبه ظهر وارد استانبول  خواهد شد و بعد از چند ساعت توقف در فرودگاه این شهر سوار پرواز استانبول_تهران شده و  شنبه شب به به تهران می رسد و ضمن حضور در تمرین نشستی هم با حدادی خواهد داشت.اوسمار احتمالا در…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/133370" target="_blank">📅 23:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133369">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⏱
پایان نیمه اول
🇨🇦
کانادا ۰ - ۱ بوسنی
🇧🇦
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/133369" target="_blank">📅 23:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133368">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
🔴
قدوسی: اوسمار راهی ترکیه شده و به زودی میاد ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/133368" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
عادل فردوسی‌پور باز هم ثابت کرد که برای ساختن یک برنامه حرفه‌ای، بیشتر از امکانات گسترده، اعتبار و درک درست از مخاطب اهمیت دارد.
✅
در شرایطی که صداوسیما سال‌هاست از بسیاری فرصت‌های مهم رسانه‌ای عقب مانده، عادل فردوسی‌پور در برنامه ویژه افتتاحیه جام جهانی…</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/133367" target="_blank">📅 23:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
عراقچی: اولین چیزی که در توافق اشاره شده این است که محاصره دریایی رفع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/133366" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
عراقچی: اولین چیزی که در توافق اشاره شده این است که محاصره دریایی رفع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/133365" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
عراقچی: اگر موارد یادداشت تفاهم رعایت نشود توافق نهایی امضا نخواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/133364" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
عراقچی: موضوع هسته‌ای، رفع تحریم‌ها، بازسازی و پول‌های بلوکه شده در یادداشت تفاهم آمده
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/133363" target="_blank">📅 23:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133362">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
عراقچی: دشمن تعهد خواهد داد که دیگر آغازگر جنگ نباشد و از تهدید و زور استفاده نکند و دوطرف به حاکمیت یکدیگر احترام بگذارند و در امور داخلی یک‌دیگر دخالت نکنند
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/133362" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
عراقچی: وقتی توافق نهایی شد بندها را تشریح می‌کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SorkhTimes/133361" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
⭕️
فوتبال ۳۶۰ مدعی شد که اگه اوسمار تا ۲۴ ساعت دیگه نیاد،باشگاه سراغ گزینه های دیگه میره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/133360" target="_blank">📅 22:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd1dc6dde.mp4?token=bCZdFdSjRdpIOLXNyUa9jCUOv9YmG1pMLN7EJsL5omJ0v5aa15zJiqQhWqiEd0qUMv7EfqCwJ8-xwIIdZBTvvmvt93EMYxBX_kMWxUy-KCyzRt6UiM63sOr7iT9m-GrxqB0aGFA6Y3p_SQctoa4GfgXwGxV89UHoP_uMH1tE8i1YuAUzvyIuqzwTPbTIM9_b_L8XbPjbOpXkbU5qjPM3An-y_davPwl5P9VAdmuVB2_4hfpBap9uTFHQ7j-ef5FBs3vfIbUe09clHPfR99GnVIn5WplLXHn8ibqqdG27-LqDpJ75uexZXUP50__8oNuNeHMfW6_vEV5E7C_HVD_Qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd1dc6dde.mp4?token=bCZdFdSjRdpIOLXNyUa9jCUOv9YmG1pMLN7EJsL5omJ0v5aa15zJiqQhWqiEd0qUMv7EfqCwJ8-xwIIdZBTvvmvt93EMYxBX_kMWxUy-KCyzRt6UiM63sOr7iT9m-GrxqB0aGFA6Y3p_SQctoa4GfgXwGxV89UHoP_uMH1tE8i1YuAUzvyIuqzwTPbTIM9_b_L8XbPjbOpXkbU5qjPM3An-y_davPwl5P9VAdmuVB2_4hfpBap9uTFHQ7j-ef5FBs3vfIbUe09clHPfR99GnVIn5WplLXHn8ibqqdG27-LqDpJ75uexZXUP50__8oNuNeHMfW6_vEV5E7C_HVD_Qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
لحظاتی از مراسم افتتاحیه جام جهانی در کانادا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/133359" target="_blank">📅 22:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
رویترز: امارات با آزادسازی مجموعاً ۱۰ میلیارد دلار از دارایی‌های ایران موافقت کرده بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133358" target="_blank">📅 22:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133357">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
🔴
آکسیوس : ترامپ در  تماس تلفنی با نتانیاهو گفته:
❗️
«این همون توافقیه که دنبالش بودیم؛ یک توافق عالیه و وقتشه جنگ با ایران به پایان برسه .»
🔴
طبق این گزارش، نتانیاهو در این گفت‌وگو زیاد حرفی نزده و ظاهراً متوجه شده که توافق در آستانه نهایی شدنه و توانایی…</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/133357" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133356">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
⭕️
آکسیوس و کانال دوازده اسرائیل تایید کردن  توافق بین جمهوری اسلامی و آمریکا نهایی شد
✅
کانال 12 اسرائیل : سرانجام توافق شد ؛ این توافق قطعیه و به نتانیاهو اعلام شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133356" target="_blank">📅 21:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
#فوری | ادعای ای‌بی‌سی به نقل از منابع:
🔴
پیش‌نویس توافق از سوی مقامات عالی‌رتبه در نظام ایران تأیید شده است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/133355" target="_blank">📅 21:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
حالا دیگر ارتش سرخ هست تا جلوی هتاکی شما و تخلف غیرحرفه‌ای را در راستای حرفه‌ای‌سازی و معرفی نماینده آسیایی بگیرد. حرفه ای گری کسب و کار پرسپولیس است.
🔴
با مراجعه به صفحه AFC در اینستاگرام با هشتگ #FairACL2ForIran به اقدامات غیرموجه فدراسیون و سازمان لیگ…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133354" target="_blank">📅 21:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-Wr9wAvjQUJ6GUGgGIXU4szmlstNAHFVyhF5kdPVlHCLn9qlV32YnVPTtADsDWh1hOtox5xtxfPv_RU8NkcpUtGEgqFMZaE4CMiRBzFacQayLI2lxxs31ESoqEoROaj5hxrTKjOsm56LiRePK6n-jYbc9TSZ9jbkL_uUPZr4b8a87iDcQvmJI-CZsIx_tVQX-8dCs_wGhLX6KNymd7jvieog3joyB2FMb5CKcSyxEH8T_JnI1dpDY3S5ihXHsx_lPZjFTUOMF0-SNrOaAKSVB_nMWDE1w5GDPnxokPTfAhQvebAjFHN-EbpC_G6W8dM_eZ957ly96174EVrbRQwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حالا دیگر ارتش سرخ هست تا جلوی هتاکی شما و تخلف غیرحرفه‌ای را در راستای حرفه‌ای‌سازی و معرفی نماینده آسیایی بگیرد. حرفه ای گری کسب و کار پرسپولیس است.
🔴
با مراجعه به صفحه AFC در اینستاگرام با هشتگ
#FairACL2ForIran
به اقدامات غیرموجه فدراسیون و سازمان لیگ اعتراض کنیم
https://www.instagram.com/p/DXkUpt7k5yN/?igsh=MWU5dzJvYnd3anpoMA==</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/133353" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133350">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAxbBD4jZ7btNCv0Uf3Yfk79nW_hYSV1epsJ37rEVQYiBtyhzUl5qjfn7oU79iqGLQ7dMfvZtoGTBGUXqtGEu23aRkg-BxoPyZITlhV8435lVm1V09WqxtJLx5PkZrK29h99SFQNoCk9vzKjDS_XYWJ7a3cwZ6fuedOVqjYp9JkewTClRBgZIgjscYt3iAhEJTABytGuautFzwr9i442E9kpqwsiEdq4pqPv0ql9nzHforK9Xo-ZzWqrROFBJ6Tvz-6hkVv90EdJFoLlT3qHl8m_IpIXi9x8KoulBsRMH0Mv1g2017wQ-HUa13Y88zonjib1HV0OJWIHD3voN2CmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های امشب جام‌جهانی رو با ۱۰ درصد بونوس اولین واریز پیش‌بینی کنید!
📌
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
📌
چرخش رایگان گردونه، شانس روزانه تا سقف ۱ میلیون تومان.
🔗
برای پیش‌بینی بازی‌های جام‌جهانی با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔗
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/133350" target="_blank">📅 20:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133349">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
⭕️
فوتبال ۳۶۰ مدعی شد که اگه اوسمار تا ۲۴ ساعت دیگه نیاد،باشگاه سراغ گزینه های دیگه میره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/133349" target="_blank">📅 20:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133348">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133348" target="_blank">📅 20:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133347">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
پرسپولیس که مجوز حرفه ای خود را بدون مشکل در فصل جاری کسب کرده، به دریافت مجوز حرفه ای از سوی برخی باشگاه ها معترض و معتقد است کمیته صدور مجوز حرفه‌ای در این زمینه دچار تخلف شده است.
🔴
یکی از مدیران باشگاه پرسپولیس در این زمینه گفت: باشگاه پرسپولیس قرار…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133347" target="_blank">📅 20:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133346">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
مهدی سالاری مدیر گل‌گهر: رای قطعاً به نفع ما خواهد بود و توصیه میکنم تمرینات پرسپولیس رو تعطیل کنید تا بازیکناش برای فصل بعد آسیب نبینن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133346" target="_blank">📅 19:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133345">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
خبر فوری رویترز:
🚨
توافق توسط جی‌دی ونس و قالیباف امضا می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133345" target="_blank">📅 19:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133344">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
پرسپولیس همچنان دنبال تیم «ب» از لیگ یکه، ولی باشگاه‌ها قیمت نجومی دادن و فعلاً معامله قفل شده؛ با این حال سرخ‌ها هنوز بی‌خیال پروژه نشدن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133344" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🔴
پرسپولیس در مشهد کپی می‌شود
🔺
مدیران پرسپولیس در ماه‌های اخیر طرح‌های مختلفی را برای تشکیل تیم دوم مورد بررسی قرار داده‌اند تا از این طریق زمینه رشد بازیکنان جوان و مستعد را فراهم کرده و مسیر حضور آنها در تیم اصلی را هموار کنند.
🔺
گفته می‌شود یکی از گزینه‌های…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/133343" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133342">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
ایرنا:
❗️
متن توافقنامه با دقت بالایی نوشته شده و دیگه هیچکدوم از طرفین قرار نیست بدعهدی کنن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133342" target="_blank">📅 16:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133341">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzWY_fbhURXEK1FNU1fJOyOArko3HuCq_jJFzt3hL9aIRW3c8aQx8eKgVgBarMJxgNyt8afHqbP4WmuEVpek7q5oMV0i2qdDtMNe0bS-qHd1mfV0GEoWp6qXSD19FZvNh45aEIt5iEpf1DEiXK_4QhL2sE3IZmXF1UmlyEMA-a-g7EYIjFWH_NlT1Xbcwv26hA4hW-xGKaDw2Qo1JfFf7lH5_v91Z9wjcl4tpWvbqpAmbrkf5lTezOOr97BTCH8O_i-7pghjRvWbyYbo8uhnNtcbCmu8n5v-b9i0YHPdbLBhXh4wWFeT-01pwYHaveM14L9VsqILwCH0i7g_Uc1ZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در نزدیکی کمپ تمرینی ارژانتین تیراندازی رخ داده و تا الان یه کشته و دو زخمی داشته!!!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/133341" target="_blank">📅 16:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133339">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
پرسپولیس معتقده مجوز حرفه‌ای استقلال غیرقانونیه و داره در AFC پیگیری میکنه/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/133339" target="_blank">📅 15:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133338">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📌
📌
خبرگزاری دولت:تمامی خطوط قرمز تعیین شده از سوی رهبر انقلاب، آیت‌الله سید مجتبی خامنه‌ای، در چارچوب نظارت مستمر شورای عالی امنیت ملی در متن مورد توجه قرار گرفته‌است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133338" target="_blank">📅 15:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133337">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚡️
⚡️
خبرگزاری دولت:تهران در طول دوران تبادل پیام‌ها، برای اطمینان از اجرای برخی مفاد تفاهم‌نامه تضمین‌های معتبری از برخی طرف‌های ثالث برای اجرای تعهدات پیش‌بینی شده دریافت کرده‌است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/133337" target="_blank">📅 14:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133336">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚡️
⚡️
خبرگزاری دولت:تهران در طول دوران تبادل پیام‌ها، برای اطمینان از اجرای برخی مفاد تفاهم‌نامه تضمین‌های معتبری از برخی طرف‌های ثالث برای اجرای تعهدات پیش‌بینی شده دریافت کرده‌است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/133336" target="_blank">📅 14:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133335">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
#فوری | سخنگوی وزارت خارجه:
🔴
متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/133335" target="_blank">📅 14:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133334">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyd5uD36yAsgEeQkXptk34lA0XU9LsnF5CYGT2tut1Jsyxi0dSE5j3THM-loOIuxc8shq8PMG3xI6akqNw1txyWU8M9bxRrKFCFAlP7o_24D3Un4stcION_xRKcHfJCTEJqbjJuRgDHD0hIimeyfJmdihaQyyyLEdv8wPAfcs4xY3DdD6ubfTojSmymwmFgO5NYaaN5EvszBmmpxd7PsICWC1dReE7in9w-KFrZJc-pbLNDJc0JpDQ_rrriGlFTmsDJMV5gmZ8m8ijapkqY8_Q8-LI-IS2Ue8Hcc6jrlZWlUg-voOJLzltcKmb9UE1Qq7RioSSxgxSLrBLsDgYXKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای تورنمنت 3 جانبه
پ.ن نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133334" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133333">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmBiieDm1__55HvoHnAoTgJTlbFoXwUBC-jATF6BuJ6ypzkQ6Hm4fCUZLTzSTug-6REDs3zNhNZWjELIZ0Z57auVrMAFuCT1CggX2Lb1Ogtlxu63rYTN-dHwequk_A6Yt2UHFnAFmaOMV1nlOByrWy4Ow-uPwCzA2mhEn1B9twDpA1EF6cLLkJk-FYactcEN6oNUSHgyxKYit7KAYPQ69cFiA5ahXo1LKL8o-c0O_6gBNMMRFI54n34hMEmRYTDvT9HMPOF3yOrZYBCMdfekdkpa16dPuWHBI0H1WWEDng2byJ2qktXgHBEpACMqLN-C2HFpb8wzCCrFapWP5hnSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سینا اسدبیگی در لیست‌ اولیه‌ بازیکنان‌ مدنظر اوسمار ویرا قرار ندارد اما مدیریت باشگاه قصد دارد درصورتیکه با احمدنوراللهی یا محمدقربانی قرارداد امضا نکند سینا اسد بیگی رو بار دیگر به جمع سرخپوشان بازگرداند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133333" target="_blank">📅 14:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133332">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
ادعای العربیه: یک تیم حقوقی پاکستانی برای حضور در مراسم امضای توافق میان ایران و آمریکا در یک کشور اروپایی شرکت خواهد کرد.
❌
ایران درخواست کرده است که توافق با آمریکا در یک کشور اروپایی امضا شود تا به آن جنبه و اعتبار بین‌المللی داده شود.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133332" target="_blank">📅 13:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133331">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133331" target="_blank">📅 13:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133330">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133330" target="_blank">📅 13:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133329">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
✅
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133329" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133328">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
#فوری |دونالد ترامپ، رئیس‌جمهور آمریکا: ما امروز به جنگ با ایران پایان دادیم و این کشور توافق کرده است که هرگز سلاح هسته‌ای در اختیار نداشته باشد، چیزی که ما بر آن اصرار داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133328" target="_blank">📅 13:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133327">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فوری/ مدیران باشگاه پرسپولیس با ارائه مدارک مستند به afc خواهان رسیدگی به روند صدور مجوز حرفه ای باشگاه استقلال شدند. مدیران باشگاه پرسپولیس معتقدند فدراسیون در روند صدور مجوز حرفه ای دچار تخلف شده و خواهان حذف این تیم از آسیا شد/فارس
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133327" target="_blank">📅 12:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133326">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
حمله علیرضا نیکبخت به افشین قطبی: ذات خوبی نداشت؛ در قهرمانی پرسپولیس هیچ کاره بود! آن تیم را حمید استیلی و مرزبان قهرمان کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133326" target="_blank">📅 12:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133325">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133325" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133324">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
فوری/ مدیران باشگاه پرسپولیس با ارائه مدارک مستند به afc خواهان رسیدگی به روند صدور مجوز حرفه ای باشگاه استقلال شدند. مدیران باشگاه پرسپولیس معتقدند فدراسیون در روند صدور مجوز حرفه ای دچار تخلف شده و خواهان حذف این تیم از آسیا شد/فارس
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133324" target="_blank">📅 12:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133323">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/133323" target="_blank">📅 12:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133321">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/133321" target="_blank">📅 11:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133320">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
🎥
لحظاتی از یک روز پرکار در زمین تمرین؛ جایی که پرسپولیسی‌ها با انگیزه و تمرکز، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133320" target="_blank">📅 11:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133319">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133319" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133318">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/133318" target="_blank">📅 10:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133317">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/133317" target="_blank">📅 10:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133316">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇲🇽
🇰🇷
مکزیک و کره نصف راه صعود را طی کردند/ جدول گروه A جام جهانی پس از پایان شب اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133316" target="_blank">📅 10:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133315">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
‼️
باشگاه استقلال صورت مالی شش ماهه (۳۰ دی ۱۴۰۴) رو روی سایت کدال آپلود نکرده است. به این دلیل که مدارک مالی و شفافیت در بخش‌های مختلف باشگاه در راستای حرفه‌ای‌سازی از سال گذشته آماده نیست.
🚫
یکی از الزامات اصلی مجوز حرفه‌ای‌سازی است که حالا استقلال فاقد این…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/133315" target="_blank">📅 09:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133314">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNyiAAcg5m404pPmLxl7kZXWoDcXjw77YsBCPuPVElNV2qN8xVPETlj5vy-hrhroxa1s2F8pEdS8sP5h4_kC1la7nzXuKljPZFqOj19a3mDTf18Qc3BvtESY_DscdhlH_F1mR09oHeaLAhK3SK1hBr6GNMXWu8BZXDu63ELMmpo6s2PEBPAAITrB6iw7iLn5UMpLQEq_jSYDuW8Q0WkHBVnvA85uRWekJ6KA0geEtSmQUAoeUs0kRQsHyK2ZtnioDkaqzzvx0v5TgbvgfGrTDbE23YTfY5qztZQ5rfTC7kTeezSX1rHWEoyyOCutXL62wuZU00fyRNtSv9m9mx3xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🇰🇷
مکزیک و کره نصف راه صعود را طی کردند/ جدول گروه A جام جهانی پس از پایان شب اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133314" target="_blank">📅 09:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133313">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SqJ8HcJ2r9eDbtTZ6Cel4NR4AuvjlnkngTXwEXCOBQ5jpgJU98lUcF8XyW1cVAHtYcosHWhk9-94H15nToLD9knTgZhsR8n6qRoXAHNZGqT9BkuSVn4lB7s7zxy40tlhgBZldjoop1KzbbIdqTR96xGFg-yn0xc8L_zBO2oHQclNxbcN5ylVhyMu5Ctp6X4Lpz0BtpsdAmY-AxT_JgaY35s1SpncrPJQlDPTBEfmIF7vISHZcQGMNsM8JTKs8jmViAggM5PGYUvIYb9_RgQvLqMpCpc_BniVoIthWnvyn8fjYHaxVIMFg24_jUPi0RgNiPBAm4ZccT4XR_EIBnRFVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133313" target="_blank">📅 01:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133312">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
✅
والیبال هم که زاییدیم و ست دوم هم باختیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133312" target="_blank">📅 00:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133311">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
ادعای واشنگتن پست: رهبران عالی رتبه ایران و ایالات متحده این توافق را پس از دیدار با یکدیگر در مقابل رسانه‌ها امضا خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133311" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133310">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/133310" target="_blank">📅 00:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133309">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133309" target="_blank">📅 00:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133308">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/133308" target="_blank">📅 00:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133307">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
ترامپ: عملیات جزیره خارک از دستور کار خارج شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/133307" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133306">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
والیبال هم ست اول و ۲۵ ۲۳ دادیم به بلغارستانیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133306" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133305">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133305" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133304">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚩
خبرنگار: آیا رهبر ایران این توافق را تأیید کرده است؟
🔴
ترامپ:  تا جایی که می‌دانم پاسخ بله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133304" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133303">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
خبرنگار: وقتی این توافق امضا شود، آیا آمریکا فوراً محاصره را لغو خواهد کرد؟
🔴
ترامپ: بله، این بخشی از توافق است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133303" target="_blank">📅 23:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133302">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
ترامپ : همین الان با نتانیاهو صحبت کردم‌..او باید با توافق موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133302" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133301">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxZGHJGNKnEd6x2IzQMRHAXc2NH-RPJyCBxPVlDsU6uRR5kP1sAt3hlSKG1SIBHl4RWupRDDKKaZUuM4Zrop27FrTI3BIcjCg8-CRFPi6GU7KiFTr4m8Ohjnm9WLrk7nc0TL7RzZMdvSVvad2MWHYR-f0dqMJ3Dsy1YUEPPIhQRwDrSd13C_6m1uq0TeiOF2cDsjyFy_vzbEb0rTv-iYboYjV5T03dbYjoLKQPb8IM3k5dgvb9kvRwFT7cIsFIehlTjdRFJzKSnZdD9-GiwgIDDPZtlu1G7i-E866tVE7WFpkIK2zFBLLQblYsVyALHnMR5Iwrg1BbWqdsLBkn1yQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
توییت بزرگ‌ترین صفحه ترول فوتبال : خدایا، خواهش می‌کنم، بذار این اتفاق بیفته چون خیلی خنده‌دار می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133301" target="_blank">📅 23:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133300">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
مبلغ رضایت نامه محمدمهدی محبی از سوی باشگاه اماراتی یک میلیونو دویست هزار دلار اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133300" target="_blank">📅 23:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133299">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
بازی دوم والیبال ایران با بلغارستان هم شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133299" target="_blank">📅 23:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133298">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
ترامپ : همین الان با نتانیاهو صحبت کردم‌..او باید با توافق موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133298" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133297">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
ترامپ درباره توافق با ایران: همه بسیار خوشحال هستند. کل خاورمیانه خوشحال است. و فراتر از خاورمیانه نیز همین‌طور.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133297" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133296">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
🇺🇸
ترامپ: توافق به دستیابی به توافق در روزهای آینده بستگی دارد و ممکن است امضای توافق ایران در اروپا انجام شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/133296" target="_blank">📅 23:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133295">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb3074466.mp4?token=N1SHuu-wxg7ai5Rt2D9IGCaKV7NpVyb5T2Y-a1XUHoXGvteDHxM74YuoOkklKtkR6GghfbTMiWZ4-rA3eBViVoH5lOm-Wt09iFDz0GjAQz0SYccaeZ23UitpCHolKknUma_fR_XSXQBHVWDZnTI2VQEQDS-aPtRAEjt_YyI9PDdZGwuIB1VUE0aQUKW0yKRUB1AKiBHxeN2-0jV5AIwNOxOkW95euUeq9wtI9X-7qJP_J6qQ3CMYRNOJfHbcMKxsN9f4rfZw9nLtGWgQJj0JqbopQBTdfkImVC_zL-w_lwYl0F68JiY_bOMoEwQwWdP4MjUFgkXoyk3F89BpPClrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb3074466.mp4?token=N1SHuu-wxg7ai5Rt2D9IGCaKV7NpVyb5T2Y-a1XUHoXGvteDHxM74YuoOkklKtkR6GghfbTMiWZ4-rA3eBViVoH5lOm-Wt09iFDz0GjAQz0SYccaeZ23UitpCHolKknUma_fR_XSXQBHVWDZnTI2VQEQDS-aPtRAEjt_YyI9PDdZGwuIB1VUE0aQUKW0yKRUB1AKiBHxeN2-0jV5AIwNOxOkW95euUeq9wtI9X-7qJP_J6qQ3CMYRNOJfHbcMKxsN9f4rfZw9nLtGWgQJj0JqbopQBTdfkImVC_zL-w_lwYl0F68JiY_bOMoEwQwWdP4MjUFgkXoyk3F89BpPClrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول مکزیک به آفریقای جنوبی در دقیقه 9.
✅
اولین گل جام جهانی 2026 توووسط کینیونس زده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/133295" target="_blank">📅 23:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133294">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
#فوری | منابع داخلی :
🔻
جمهوری اسلامی ایران پیشنهاد آخر آمریکا و توافق را قبول نکرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133294" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133293">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
کانال ۱۲ اسرائیل: از توافق امریکا و ایران بی‌اطلاعیم و از اینکه رهبران ایران موافقت کرده‌اند ، متحیریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133293" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133292">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
👈
ادعای اکسیوس: منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/133292" target="_blank">📅 23:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133291">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">☄️
☄️
اولین بازی جام جهانی رسمآ آغاز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133291" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133290">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcRV8Do-3M-jKsfz9i-_JjSajCk8txVNFSpYHZfRt0jRBWmfuB7BG_RKZf4wd96L-hG4Pr4biUFknRUOt5Acj3MA4iFa0wvYbkX5Js5qXFt99kdRDshw88I7xlEiUPjq124CrSJYZ8JQnCYSbCmHdJRmrhDusxgnY5AqBkt-bvmy2HwqgXWQRU0_TQQpf8Yta5X5tNAwQGDAL9ZItRrnkidQ4K9t3vClqUQ5KrWu_EfILAmANksMWS6IhJFaBLNQGOeBOvyQUc-RwGVlXZLGiV0zv4BWxV_CvO6lWhnAZlitMceaJ9pYajOAqz_IH2Hgtqn6Eom9VASbM5z4mcZoxax8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcRV8Do-3M-jKsfz9i-_JjSajCk8txVNFSpYHZfRt0jRBWmfuB7BG_RKZf4wd96L-hG4Pr4biUFknRUOt5Acj3MA4iFa0wvYbkX5Js5qXFt99kdRDshw88I7xlEiUPjq124CrSJYZ8JQnCYSbCmHdJRmrhDusxgnY5AqBkt-bvmy2HwqgXWQRU0_TQQpf8Yta5X5tNAwQGDAL9ZItRrnkidQ4K9t3vClqUQ5KrWu_EfILAmANksMWS6IhJFaBLNQGOeBOvyQUc-RwGVlXZLGiV0zv4BWxV_CvO6lWhnAZlitMceaJ9pYajOAqz_IH2Hgtqn6Eom9VASbM5z4mcZoxax8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقدام جدید در جام جهانی 2026؛ بازیکنان ذخیره هم در مراسم پیش از شروع بازی شرکت می‌کنند و سرود می‌خوانند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133290" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133289">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
از امروز جام جهانی ۲۰۲۶ شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/133289" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133288">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZxYnd4otEXvGS2k9oZpNUDf-mzm7DtcigwPQYTTVnfXEfZPt8-Y6K8iqlphck9--SjiRkhzBENg56SRlZBRfd8BH5FEDsc---xCzMiDN2ZeyNdO9mDEgE5kyEMY3IeXAoT9UKlaeJtkxotBy77w_q8ungvINOoqJLHve5l-5a2pIIFGD85OCH89xsNgXXcWbXv92SORwzyWgkUgmK0T3mG1bDDR746Y1J-GSE9yb5-BGMsgqnkFdcuoTNokW5W-nBOBo0TycQpfxU_KbWMMtBEuFKsQ9QXKMhWeR_GGE3Eqw1r4LJrJhqVtylAY3TLP87ZcDVtfALVfzMo3_6gRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این دیگه چه وضعشه...
🔴
تا باسن بازیکن های سنگال و چک کردن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133288" target="_blank">📅 22:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133287">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/133287" target="_blank">📅 22:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133286">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
#فوری | منابع داخلی :
🔻
جمهوری اسلامی ایران پیشنهاد آخر آمریکا و توافق را قبول نکرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133286" target="_blank">📅 22:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133285">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
معرفی تیم ملی ایران در مراسم افتتاحیه جام جهانی با نمادهای فرهنگی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/133285" target="_blank">📅 22:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133284">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133284" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133283">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ac505c0c.mp4?token=B34-IqfSbQ9OHETGYF2U3ZvfqXZDOv-P8mgZQol4ErZAUjt27hW8q8_DsHxLZuBbvQiwL17uXpp65Zg8587FvVXHHm-6xshG5Fc0NoXkJ7EQCK7r6r9ewXQTBK9Izg-JT7xEpTH4Gja8bJWqrWnTowQfoN3XzqAGNLQySn8ZRxe7TPyivEmC27acufMGq2bYbuIp9znSe_Y1-LgMCVI6IMrL-0Wo6tVaMMQzG_ejKL0m9eQbb8MdI8Be9hLdUB8kg6p9ALm0m9eO-xcQgfPqDVBn1O_M8asmNGQfP5ip9jCa6GvBzvJ34GA6zSfNqx__sMAjAqWqEBVocWqNhlMcIYMRMnRBum-0MYAwlDzLmIFG_NyUfc21UI2BswYwuxxaeoM3GB2cAqFe-LsN9yLfAxyixukOH2Vz2KOjLnH0XbJPQDCnySXIt3OSCX6NNEBugaidaUMGzfPocxMehXJgbxrQMWl6eJmS0-mSzlAx9HhAMzB_ePMCQJWLo-tBO0ExmDky08V9PCtAyikOMm81329BGrv4dLSNb8N5KXC_oSQZfaRPCAnNe7Jgjxhl2YPLTy2sVkDbqHHYcBzksMTDmymY7A23FoHmbOM4LUUZrNlA3w2A0mHixgOdM-u9geJEAkqUkG6poHUujl6ZI-dqu0xqJcHK97Ot_YqPFIn9YE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ac505c0c.mp4?token=B34-IqfSbQ9OHETGYF2U3ZvfqXZDOv-P8mgZQol4ErZAUjt27hW8q8_DsHxLZuBbvQiwL17uXpp65Zg8587FvVXHHm-6xshG5Fc0NoXkJ7EQCK7r6r9ewXQTBK9Izg-JT7xEpTH4Gja8bJWqrWnTowQfoN3XzqAGNLQySn8ZRxe7TPyivEmC27acufMGq2bYbuIp9znSe_Y1-LgMCVI6IMrL-0Wo6tVaMMQzG_ejKL0m9eQbb8MdI8Be9hLdUB8kg6p9ALm0m9eO-xcQgfPqDVBn1O_M8asmNGQfP5ip9jCa6GvBzvJ34GA6zSfNqx__sMAjAqWqEBVocWqNhlMcIYMRMnRBum-0MYAwlDzLmIFG_NyUfc21UI2BswYwuxxaeoM3GB2cAqFe-LsN9yLfAxyixukOH2Vz2KOjLnH0XbJPQDCnySXIt3OSCX6NNEBugaidaUMGzfPocxMehXJgbxrQMWl6eJmS0-mSzlAx9HhAMzB_ePMCQJWLo-tBO0ExmDky08V9PCtAyikOMm81329BGrv4dLSNb8N5KXC_oSQZfaRPCAnNe7Jgjxhl2YPLTy2sVkDbqHHYcBzksMTDmymY7A23FoHmbOM4LUUZrNlA3w2A0mHixgOdM-u9geJEAkqUkG6poHUujl6ZI-dqu0xqJcHK97Ot_YqPFIn9YE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133283" target="_blank">📅 22:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133282">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leTH1fm05PpuRdt0w0j7qoMIxe4ygUDAYH8nUBqaTGJMTL0wbDf3LeUxagbLoDuNW9RE8G2zz5dp_mO4Sr4GT6KencvgyZaQ4UATZqr2fRdttroUvHKar2r6BczkYTv8CkTGVThkaj8UFAxBXGPzaJhbWzhKBtlAL7MITv0vFR8tOMOTj14U5K0yfM8yFen9cDmZdUwcvbTbpLnjP4iSVm9dOGKH81Bip6JDfyGTEyrQDmg-kxZAjZGdOq9jjfDiugx0sy7tMRW43SVJxSfvgJOM0mQMYhDHCv2eRSWzvolJQiPdKGsj-BIX6Z3WsqmA5x9NzIVzG6xvdkokszxQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/133282" target="_blank">📅 22:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133281">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
#تکمیلی | با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران ارائه شده و مورد تأیید قرار گرفته است، من به عنوان رئیس جمهور ایالات متحده آمریکا حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133281" target="_blank">📅 22:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133280">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
#فوری | خبرنگار نیویورک پست:
🔻
ترامپ همین الان به من گفت که توافقی با ایران "تقریباً کاملاً نهایی شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/133280" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133279">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
🎥
لحظاتی از یک روز پرکار در زمین تمرین؛ جایی که پرسپولیسی‌ها با انگیزه و تمرکز، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/133279" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133278">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
#فوری |  | ترامپ :
🔻
من، به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران را امشب لغو کرده‌ام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133278" target="_blank">📅 21:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133277">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
#تکمیلی | با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران ارائه شده و مورد تأیید قرار گرفته است، من به عنوان رئیس جمهور ایالات متحده آمریکا حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/133277" target="_blank">📅 21:43 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
