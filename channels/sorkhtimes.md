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
<img src="https://cdn4.telesco.pe/file/piGl73GdhNQhrUosfF7Rqb80v5mSORjtBLIVNVD10WBKMLxVziObjNt2Q3RMgeAt7x71v_qJlX1M_mzD-VqzNZGsLfFgMOLurM5JikfnNYPdUCtzC-w_a8DBZuYlGeFqppuVb8N8S5FvxBVps707dKeGSG4UXpCFUorzBHqLT5YqjfLMz74YBjwUHBIJhIm_AG5T296Q_CcpHGw5caA2mH4RveQVSSa5R5-Rcnuei8eWgSgPyIOwvBJgf-KWe_WoI_3ocY_9uxQK_RZpdebwwxFHTXjZcrGC2zeQtkqECFnUS7WCSrJRxoTES8lkmpuvLjl7EmO6Fy_viL80YIQeKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 03:29:47</div>
<hr>

<div class="tg-post" id="msg-134238">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtfOFcb9uJsDLUTaBzM7225-NZOcGHyww-Tt8yq3s4-2oMGIXomKutSsZUxiLh37bG6v21qBH-2dCPZdnFtYVXfqJ-_9eaiAAybSaNYDp0dcbP0KsSG3OQSKz2ZYHLvGLAe9K5OYjb9VOxuf09kDyaG58prRnUHJPrbbo1YOb8aRE0N7cUSae6oYlS_DY7tZwxcZgqCRAYRJFieaNJuKSq7-3a8_L-YmKJ_8tK7PzsVnmLsDBA9xRK_c4nBt9WAWmzYRk9MElvIp8KILPuPsVux64LBzu3t4hjNNxqcbJzkrWhkWEKfwtptZdMDcuGyZGK92dm4H2F_PyczD-qdMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه A جام‌جهانی ۲۰۲۶
[
جمهوری‌چک
🇨🇿
🆚
🇲🇽
مکزیک
]
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
استادیوم
آزتکا مکزیکوسیتی
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
<div class="tg-footer">👁️ 734 · <a href="https://t.me/SorkhTimes/134238" target="_blank">📅 02:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134237">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blBUaNRSDIeH2MSL4DPhGHPCS9RMiqkljr7gyoHgWeUZPuYWCYIU9VIR_CjQVpuS_LzolHfxPZUDLjt26RWPMQJKOQUofBmz-2F7OjwKLTpnkANJaug1YPv9kj_BdEnPdLTN8uj30Kds0IFiaYelaaJGO23qcJIL9RzG3kxpVIl2Kxt2wM5dPJiTQ9WC7iNNggSDaW_AgCycfhA5dFQPes9CXR2bf4aRiULM9FCOk65PQaWxP6MweEFWyvs-hY5UP07ItXhOMfAZT-5JbSYjcaJebDVKEemxJcbp0EqgVwepvXsOJPf8hnAhoBVf-o6VxdqFyz654QaQaBxxiVE7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شباهت 100 از 100 بدون شک
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/SorkhTimes/134237" target="_blank">📅 01:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134236">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baZasCpTxycC4SWOruAKo3WvrxJrXpY_aHO2-yRXaDvA47j0Gb6z0Y03aI3qqbKtWLgswDR2ugGVY-7y2B-jAUDx8ta9yw4Fr2VtCFeffFtm_7JvfeJsjQgkhnjbp_fet2dFflNMaoie18fF6NY1YPUDfAs4iB0-j5aPP5f53-Iioxw9SgCViaiUtaKSpZDu6pc24ECm23APvsWTgsnIWiBEyar0BY70gh3ueNU9eEcuPwHD-4iALy3RabJ8jpjlyZgfRu7arWhyN-eS7oUXLcMyfofCcMwcvQmfpC71UG6GLRUoaJ7hWCd9jqlP9JeVPJsaqBe_x95SUblpfjX-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه  جام جهانی پس از پایان بازی های دورگروهی این گروه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/134236" target="_blank">📅 01:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134235">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
❗️
فارس : پیگیری ها از باشگاه پرسپولیس نشان میدهد  تاکنون قراردادی میان طرفین به امضا نرسیده و تنها توافقات اولیه و نهایی بر سر مسائل شخصی حاصل شده است.باتوجه‌به اینکه طاهری همچنان با باشگاه روبین کازان روسیه قرارداد دارد، پرسپولیس برای نهایی کردن این انتقال…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SorkhTimes/134235" target="_blank">📅 00:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134234">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
فوری از قرمز آنلاین: حضور اوسمار روی نیمکت تیم مقابل چادرملو قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/134234" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134233">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
فوتبال جام جهانی و نشون ندادن به خاطر والیبال ..خود والیبال از ست دوم قطع شده و دیگه نتونستن از جایی دزدی کنن و پخش کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/134233" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134232">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
والیبال فنا امشب لیگ ملتها هفته دوم شروع میشه و ایران ساعت ۱۰ مقابل فرانسه بازی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/134232" target="_blank">📅 00:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134231">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/134231" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134230">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba8fslAgPVVii4Lniybrt9-YmFco4jIh5w3xza79rBGNsyRhYsG_dMHC8pxDbMZKb3Ir5ZxGvcUuv3WaP5U6cw9WcRQhL5g46nELeieJsm4kP8KhdaX69ERPSj5EbMQrQy08CO6k5wd1dA7V0tYaQ_vJDKZ4B1l2PK16w-uFosyGqrnl3OtM2Hcpna3zb9mEzNd_g68gzcIRQs957t87PnM3m8rDvis3ALDLAz478eZvziNF0JLfx9ZoKSYVjcaB5VCu5ibu4MSGPR2QNCyNY-QSEsFVxacC71PLaaJM8zgp4rLBCUyscIE4HvkCa9wia_lXZXmp_dmSz2ziunF2lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
صفحه رسمی باشگاه دهوک عراق عکس ها و ویدیویی هایی از معارفه یحیی گل محمدی و دستیارش محمد عسگری را در پست و استوری به اشتراک گذاشته که نشان می دهد مراسم معارفه ویژه ای جذب پرافتخارترین مربی ایران در جام های سراسری برگزار شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/134230" target="_blank">📅 23:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134229">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
#فوووووووووووووری
🔴
با اعلام رسمی پایان فصل؛ قرارداد امید عالیشاه با پرسپولیس یک فصل دیگر به طور خودکار تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/134229" target="_blank">📅 22:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134228">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/134228" target="_blank">📅 22:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134227">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
پدر کسری طاهری: کسری فصل بعد پرسپولیسی ست و قرارداد داخلی امضا شده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/134227" target="_blank">📅 21:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134226">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
❗️
البته ی بازی گروه b امشب پخش نمیشه چون ساعت 22 بازی والیبال فرانسه و ایران برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/134226" target="_blank">📅 21:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134225">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: با ایران داداشی شدیم و به توافق «صلح‌ تاریخی» رسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/134225" target="_blank">📅 21:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134224">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6Jib5IRfzhJGxPrgJuuUPjslck1R61y_Than-wsOLcFNUYzmoGR4hGQ3jnILRJiWP9s3JG_smr_xl6iQsHXVth1h7GbeQiRYgHd4RFnEcOiH83TOzr5afVh8Eu84LEb-46t2_E4TA4yzlDe4v4zmIMBFKOAG9A78CN3bWgpLlms7rmBrbGN8exK63ojIkkifqk-axmAmXsBOZIM_ZKP4c9wjpeGSwY4P-y6scpkJxE0VmeIPN8Xo1kmPgEAKrHT1gIzQTrPqKrGQR_4wEAn9NAIqmIjUORxqz8yPkKsyaQZsGiB19mqbWpIyB4wlMhvGhOAdl5Jc2O_L2e3cqjvGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خطاب به هواداران کریستیانو رونالدو و لیونل مسی؛ به‌جای درگیر شدن در بحث‌های بی‌پایان و مقایسه، بیایید از تماشای این شکوه لذت ببریم
.
🔴
ما در دوران معجزه‌ای هستیم که هرگز تکرار نخواهد شد. این آخرین فصل‌های نمایش دو اسطوره است؛ قدردان این لحظات باشید، چون تاریخ فوتبال، پس از آن‌ها، دیگر هرگز بازگشتِ چنین عظمت‌هایی را نخواهد دید
😭
😭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/134224" target="_blank">📅 21:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134223">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Majnoon Ye Rooz</div>
  <div class="tg-doc-extra">Hossein Sotoode @cafe_tarfannd</div>
</div>
<a href="https://t.me/SorkhTimes/134223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎤
حسین ستوده
نوحه محرمی
🏴
»ری اکشن فراموش
نشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/134223" target="_blank">📅 21:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134222">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
عاشورا حسینی بر عموم شیعیان حضرت تسلیت باد
🖤
التماس دعا
🤲
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/134222" target="_blank">📅 21:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134221">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/134221" target="_blank">📅 20:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134220">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6MuE69Q96WVfZKEeeTT87UjJxtr1pAvvqU_IIwLF28r-2drOTDPpdDh49L29eFJW3T8WdNGBFkuhyMplCUXzZCt4fwEVqanaAR394UJQ5HPC_qOt78PhhgCWkv3Mb3sqQiSsdT4D-YKGe0J3bEu5L6c-SDxrWYzNiHPoCkdpUKzWZjJ9n-byra-asRP1QCYMfrg9FxNq_cGA24JidhQT9DI6J3j2k9Y8Z1qsUrQsccmrmOeqeNAtmGsOnXfvw5iTxJocUnVMwJU4I3-4fbAZxXcJURCff6jAjPhMk07LCAIe5U8OsGeltWBRLqih14168MjJxVCB1-aCA0UEBYd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه C جام‌جهانی ۲۰۲۶
[
برزیل
🇧🇷
🆚
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند
]
⏰
بامداد چهارشنبه ساعت ۰۱:۳۰
🏟
استادیوم
هارد راک میامی
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
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/134220" target="_blank">📅 20:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134219">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHJy9Y8AbB5ltK2HuMyvbO-CopOgE4njykT4eWdqLXAkMLpHDfu2WAh3ZzruKH5vxnpILTLc3dv0Epqod5587G-K2xW1tjuuUDsKNUv2dyk7sZBftLBZ2ot19e8COhkUaiYu-3INC_XbNRIH_wFiITpcHGlUFQA-nryw3C-gVvsfDcxNOXBpf_SAYlSAfgpPzETh96khgKtNT5I4nWjTOrp1hQlscOM-ZQgmrtAV-DyzmO8D50dS22GN6UnSnXok1LOqosZpRyjkzyM_0z_XyW28kauc24WGUKeWjmnO1ruKasEMD_idIFAtX0AcBXgr1oot_5X5PeE1eD4o77vWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/134219" target="_blank">📅 20:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134218">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">💢
اوسمار خودش اعلام کرده قرارداد نداره به شایعات توجهی نکنید دلال های ولدز…میخان باشگاه رو سرکیسه کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/134218" target="_blank">📅 18:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134217">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
❗️
مارکو باکیچ: آماده بازی برای پرسپولیس هستم. دوست داشتم در جام جهانی برای تیم ملی ایران بازی کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/134217" target="_blank">📅 18:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134216">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBDNynvIVTBa_jSm97loxwcU691R9JsWM0LH81KeFcVdPiLFmTAsv80LCl1qyMPN-Kf6uAnHdQ_CG6Hr_vSQZyxa_z3JRv9xeof8VjiRP93kV68THjwmM_S5FMxY51WjrGOHZ4Bkyjj-N6CYPbSdQLXoTO1lPFSl19xLOMIunL5TRW-Q4oAb4Lo0IC6P5LmBU4J0LrH0sxPyD5RQWh28HXtJfWlLyqJ59Ecv_w9Iy_prVRsKvtmKzILukXRH5MI1SPjZ1NJh6j7R3ZmV-TzUv59xdvAMGU2uMmLnGBaUqouuU17A5Y87-ZbsP6IanWbJTYjKX8WpaS7dHfpYzLFUzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽
رئیس فیفا اعلام کرد که در پایان رقابت‌های جام جهانی ۲۰۲۶، جام قهرمانی توسط رئیس‌جمهور آمریکا، دونالد ترامپ، به تیم قهرمان اهدا خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/134216" target="_blank">📅 18:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134215">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
یاسین سلمانی در پرسپولیس میماند؟ آخرین گمانه‌زنی ها از ماندن ستاره خاموش پرسپولیس
◽️
یاسین سلمانی که پس‌از پارگی رباط صلیبی خود بازگشت موفقی در دو فصل اخیر سرخپوشان نداشت، بنظر میرسد یکبار دیگر شانس به او روی کرده و اوسمار ویرا قصد دارد این بازیکن را به…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/134215" target="_blank">📅 18:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134214">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">◀️
از امشب بازیهای هر گروه به طور همزمان شروع میشه ....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/134214" target="_blank">📅 18:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134213">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
1. روز اول، بازی‌های چهارشنبه، ۳ تیر:
🔴
گروه B:  سوئیس
🇨🇭
×
🇨🇦
کادانا؛ ساعت ۲۲:۳۰ بوسنی
🇧🇦
×
🇶🇦
قطر؛ ساعت ۲۲:۳۰  2. روز دوم، بازی‌های پنجشنبه، ۴ تیر:  گروه C:  اسکاتلند
🏴󠁧󠁢󠁳󠁣󠁴󠁿
×
🇧🇷
برزیل؛ ساعت ۱:۳۰ مراکش
😀
×
😀
هائیتی؛ ساعت ۱:۳۰  گروه A:  چک
🇨🇿
×
🇲🇽
مکزیک؛…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/134213" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134212">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚫️
دور سوم مرحله گروهی رقابت‌های جام‌جهانی
6⃣
2⃣
0⃣
2⃣
از راه رسید!
🔵
اوج هیجان فقط با وینکوبت، بازی‌‌های امشب و بامداد فردا رو با
🔣
0⃣
1⃣
بونوس اولین واریز پیش‌بینی کنید!
🔴
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
🟢
چرخش…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/134212" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134211">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
خبرگزاری فارس: نقل و انتقالات پرسپولیس  تا زمان انتخاب سرمربی جدید متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/134211" target="_blank">📅 16:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
فارس: بین پرسپولیس و اسکوچیچ در اغلب موارد به توافق رسیده‌اند و تنها اختلاف بر سر مدت زمان قرارداد باقی مانده است.
🔴
مهم‌ترین مانع موجود، مدت زمان قرارداد است. دراگان اسکوچیچ خواهان عقد قراردادی ۲ ساله با باشگاه پرسپولیس است اما مدیران این باشگاه خواهان قرار…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/134210" target="_blank">📅 16:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134209">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه کنیم.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/134209" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">💢
اوسمار خودش اعلام کرده قرارداد نداره به شایعات توجهی نکنید دلال های ولدز…میخان باشگاه رو سرکیسه کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134208" target="_blank">📅 16:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKLLBN7csDLQ8wQwB0NIKP5X5UM6YoLLNUWSkBSLDDodlnKChz8fIPhDQygCcX5HONb4OYMpKwtp1R1lmLUE2UWaAEJ4pCYT3wmx7nJpO7NSjxDqfggoRSMYr849GrWnCoThgtvhrev8fBUSxfO1oGScWMb5dOOtIDq0O0gxeXjUwrgLgmkOIfhiayLD4Hdm5wkMTIciA893ia5SuSg5cP2KWhtKnSiBkE4ZdJ5-iM2Q9xJXzhCfyH_VEH1qUO-AOCZmkco8Mp6r9VSiJHZKeXvUAaJlh9K8GaqFz7l3Nsy4d0O67Rp62PZM5jJpSN5ATTyMZvyWt8tiQuVGehFo3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دور سوم مرحله گروهی رقابت‌های جام‌جهانی
6⃣
2⃣
0⃣
2⃣
از راه رسید!
🔵
اوج هیجان فقط با وینکوبت،
بازی‌‌های امشب و بامداد فردا رو با
🔣
0⃣
1⃣
بونوس اولین واریز پیش‌بینی کنید!
🔴
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
🟢
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
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/134207" target="_blank">📅 16:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
طی ۲۴ ساعت آینده جدایی اوسمار ویرا از پرسپولیس به صورت رسمی اعلام خواهد شد.
🔴
بدین ترتیب و در صورت برگزاری مسابقات پلی‌آف احتمالا کریم باقری به صورت موقت هدایت پرسپولیس را بر عهده خواهد داشت. البته هنوز احتمال حضور اوسمار در پرسپولیس در این تورنمنت وجود…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134206" target="_blank">📅 15:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
باشگاه تمایل به فسخ قرارداد و قطع همکاری با اوسمار ویرا دارد.
🔴
🔴
به گزارش خبرنگار قرمزآنلاین، قرار بود اوسمار ویرا در باشگاه حضور پیدا کند، اما هنوز این اتفاق نیفتاده است.گویا مدیران باشگاه هم تصمیم داشتند جلسه ای را برگزار کنند که این نشست به ساعات دیگری…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134205" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
اسماعیلی‌فر، ترابی و هاشم‌نژاد با تراکتور قرارداد دارن و تراکتور هم قصد فروششون رو نداره///آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134204" target="_blank">📅 14:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤩
تتوهای خانوادگی مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134203" target="_blank">📅 14:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
پرسپولیس و مسیر جوانی در تیم
♦️
شاید بعد از چندین سال بسیار واژه مسبر جوانی برای سرخپوشان مهم و حیاتی باشد چون تیم از لحاظ میانگین سنی در وضعیت بسیار بالا قرار دارند و شرایط ایجاب میکند که در فصل جدید به جوان گرایی رو بیاوریم تا از لحاظ سبک بازی هم شاداب…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134202" target="_blank">📅 13:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
باشگاه شاید قرارداد میلاد محمدی رو تمدید نکنه.چون قیمتش بالاست ...سر همین داستان دنبال جذب ابوالفضل رزاق پوره///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134201" target="_blank">📅 13:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
اختلال در خدمات کارت محور بانک‌ها رفع شد و خدمات کارت‌ محور هم‌اکنون در دسترس مشتریان است و روند ارائه خدمات به روال عادی بازگشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134200" target="_blank">📅 13:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
درصورت جدایی اوسمار، کریم باقری با توجه به این که اسکوچیج بارها از او تمجید کرده است، ماندنی خواهد بود.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134199" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134198">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
فرهیختگان : اوسمار تمایلی برای ادامه کار با میلاد محمدی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134198" target="_blank">📅 11:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ترامپ: ایران اگه توافق نکنه ظرف یک هفته تمام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134197" target="_blank">📅 11:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDU28daw-Z0AZopIq7AROJZJlxCILCUygb3ctpYj4G7E2EygiDrsn7VZNL4lrALqx1ot7j9ynE8K6B4tWYp8zo0lcf2BJV0P9csfUuicxK_Tqnsv0HClBlmfUwk7NfpeHDr3Qfb4JueCWJAwrCSWqZkrrQ-MRPSXcVH3ZXmbktLIsIBHAtjYhB0nCHUR8XGkI4Qa2AuIiHLu2aXj-ep_xldK94UKxhMo3OCsYL2TaR8uaFlHobVSWzAKUYJyViSUJWgrl-9GQ-uCGNrSBNZUVTvLLA2UxqDB4V3WzWNUipanzChq8bXzc4-EnH0-XX1ii3kJ2kt3iNASyS2WScfrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رونالدو فقط انقدر تنها 25 گل با 1000 گله شدن خودش فاصله داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134196" target="_blank">📅 10:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134195">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
باشگاه فرهنگی ورزشی پرسپولیس با انتشار پیامی، صعود تیم نساجی مازندران به لیگ برتر فوتبال ایران را تبریک گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134195" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134194">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
❗️
تیم چادرملو اردکان برای دیدار مقابل پرسپولیس، ۶ ستاره خارجی خود و از جمله هادی حبیبی‌نژاد را در اختیار ندارد و به نوعی یزدی‌ها هم نیز مانند پرسپولیس با ترکیب نسبتا ذخیره وارد میدان خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134194" target="_blank">📅 10:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134193">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭕️
برانکو پس از بازنشستگی از سرمربیگری، به عنوان مفسر و کارشناس جام جهانی با دو شبکه تلویزیونی از کشورهای کرواسی و ترکیه همکاری می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134193" target="_blank">📅 10:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134192">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
امیررضا رفیعی:
❗️
من یک فصل دیگر با پرسپولیس قرارداد دارم. پرسپولیس خانواده من است و دل کندن از این تیم برایم سخت است. دوست دارم بمانم اما به شرط اینکه فرصت بازی به من برسد. من قبلا هم خودم را نشان دادم و ثابت کردم دروازه‌بان بی‌استعدادی نیستم
🔴
شما اگر از…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134192" target="_blank">📅 10:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134191">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEalcGpnMoDxBprVe7mgJ78Fvux2MZf7iYl-GsIx4L8BmC4pgVylM2WM1zr0wp-VSdtNkHqnTYSfLiFy6h4vvjZSZ8asu9FEY-uc_QpAGANsSmrcMkzVfrXDUpaZkiyBTPEmaODrBljEiJRStoyv_ijBqjr2rOxus5lHAsW5b-aQuolld04EP99CpF9BDvn_s5mEGbbejh5T35q6-oADWKzn3Z0ucUnh3VSwDBk7_x3aMEclqqeQQMHReyVjBvQtPzkieutCI4TKRm3UkAAndVj2bdFbEiIx6UQeq_ewCB7DDgtbWYLHfpiACm58NyVShkfprt1qJHZlW8nfZElHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارت امنیت داخلی آمریکا اعلام کرد که به تیم ملی ایران اجازه می‌دهد 48 ساعت قبل از بازی حساس مقابل مصر وارد سیاتل شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/134191" target="_blank">📅 10:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134190">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
شرایط جالب برای صعود :
🔴
با توجه به اینکه 8 تیم برتر سوم صعود خواهند کرد، در صورتی که شاگردان قلعه نویی در بازی آخر مقابل مصر به مساوی برسند به احتمال قوی جواز صعود به مرحله بعد را کسب خواهند کرد
🔴
اگه ببرن که مشخصه قطعی صعود حداقل به عنوان تیم دوم، اگه ببازن…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/134190" target="_blank">📅 10:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134189">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
رفع اختلال تمامی بانک‌ها تا پایان امشب
🔴
بانک مرکزی:
🔴
اختلال خدمات کارت‌محور در اکثر بانک‌ها که اقدامی پیشگیرانه برای حفظ امنیت بود، برطرف شده است؛ خدمات بانک‌های ملی، صادرات و تجارت نیز در حال بازسازی است و پیش‌بینی می‌شود تمامی خدمات بانکی تا پایان امشب…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/134189" target="_blank">📅 09:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134188">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cydTpG97yIiMP70WVmeA9vNCxUWc1u08Cs2q1kzz0j5gc4TFk_qziXUUBvPfW25_JZ5eyf9E-JuZIHtLx_qrUgKsoeLab8W3MgfqKf472TQNJGsD31q6625tCH48OGQDxftUhKDvA7bfccUbn399SWxFg6AN-ZFe7W_aufq1mkUk_N03AbbS8xrs6hbUSD8w96TLQPtJxi82nZvYEmku5CQwNEi9gH7ZaaWOj7ZAZ3Xxc-v2KBPeNZoXYgWjIFySPrlyjuYbQ6CDiMtsmuzZCPrM-HEJHiUokfUImGw7Fn5iMdSKJkCv-bNWLsJjFIbapJ2dXCuDb4TdCqHZB9EwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌ بامداد امشب رو با ۱۰ درصد بونوس اولین واریز پیش‌بینی کنید!
🟡
Colombia -
🔵
DR Congo
⚫️
جام‌جهانی گروه K
⏰
بامداد چهارشنبه ساعت ۰۵:۳۰
🏟
استادیوم آکرون
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
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134188" target="_blank">📅 02:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134187">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134187" target="_blank">📅 02:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134186">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
❗️
اسکوچیچ خواهان جذب دروژدک مهاجم اسبق خود در تراکتورسازی، برای پرسپولیس شد.
🎙
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134186" target="_blank">📅 01:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134185">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ترامپ: ایران اگه توافق نکنه ظرف یک هفته تمام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134185" target="_blank">📅 01:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
فوتبال 360: مذاکرات پرسپولیس با هادی حبیبی نژاد مثبت بوده و این بازیکن در آستانه همکاری دوباره با اسکوچیچ قرار دارد. هادی در فولاد نیز شاگرد اسکوچیچ بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134184" target="_blank">📅 00:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134183">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKqKFZOClk18uPK4MgqNP0vBI_8aLneKYyqda-xSOyNNrjsB6j2R8IN9O4_B5wK_vkzzlWWWzOo02jafjDv1LvlfV8w6b2SLQ9EkTK9k95BRSFHLmb4zh1zfr2qMzKY-JMfUecHQUY0bpoQkFZZPBS5v11DDE3RmfPf9hQ_astjHtdM9pEcBspPrHmd6HuLnrWQ-Tuz03NSGW7CC_axspDeGdcKP1Efl_aVj3Lg7kzlv1TXhGal6KfK3nlOFMp53PyRvAOXk1cN1QTbjGPUXOOiQ3sHFCXt2nbBnLzjW3MJBs4Ss36hGNYIO8aCFLvqFV6mR-Q40GfB7Cv2BV6jd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
برانکو پس از بازنشستگی از سرمربیگری، به عنوان مفسر و کارشناس جام جهانی با دو شبکه تلویزیونی از کشورهای کرواسی و ترکیه همکاری می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134183" target="_blank">📅 00:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
🚨
#شنیده‌ها
💵
پیشنهاد مالی جدید علیپور به پرسپولیس برای تمدید قرارداد: ۲۵۰ میلیارد برای ۲ فصل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134182" target="_blank">📅 00:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
کریم باقری: دروغ می‌گویند که سبیل من را زدند
❗️
کریم باقری، مربی فوتبال:  نمی‌دانم چرا به دروغ می‌گویند سبیل من را زده‌اند در حالی که خودم اولین بار در بازی مقابل قطر سبیل‌هایم را با قیچی زدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134181" target="_blank">📅 00:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134180">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8081bf998b.mp4?token=a2C-_eNLalf7nicnPrcK6IFvN_-s6fJtjks5dECMBIznCD0XKGFvlH7LtaqxgTxT56HVjcJ5ciVdWRPLzGPiOzd7TlAWrooeYKP81Rzgz_Ykm003cblAZA09OlmLChbpVGCNnUMubZx85PBU28cHgOQOMtWJy_KZeDm3fhh7-1tZq3cUC68RhGNyE6IjZLXNzKXp0A9_gB14aPIVi2Ai7iHpIc10pJgatwmDxsYsZpCKM4IXHGQN-oH9HXjUbIzYJSJ8wPbdHF1ADrze8ti0QYjG3eHWSfb3QICsdDp1o9yBW2wh8WeIF-4iskafjMcdVVvMzKPf3lA6u0ScSAfZyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8081bf998b.mp4?token=a2C-_eNLalf7nicnPrcK6IFvN_-s6fJtjks5dECMBIznCD0XKGFvlH7LtaqxgTxT56HVjcJ5ciVdWRPLzGPiOzd7TlAWrooeYKP81Rzgz_Ykm003cblAZA09OlmLChbpVGCNnUMubZx85PBU28cHgOQOMtWJy_KZeDm3fhh7-1tZq3cUC68RhGNyE6IjZLXNzKXp0A9_gB14aPIVi2Ai7iHpIc10pJgatwmDxsYsZpCKM4IXHGQN-oH9HXjUbIzYJSJ8wPbdHF1ADrze8ti0QYjG3eHWSfb3QICsdDp1o9yBW2wh8WeIF-4iskafjMcdVVvMzKPf3lA6u0ScSAfZyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کریم باقری: دروغ می‌گویند که سبیل من را زدند
❗️
کریم باقری، مربی فوتبال:  نمی‌دانم چرا به دروغ می‌گویند سبیل من را زده‌اند در حالی که خودم اولین بار در بازی مقابل قطر سبیل‌هایم را با قیچی زدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134180" target="_blank">📅 00:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ca2071a6.mp4?token=WoVQInoCgJLFFeXgC9h8jQEuVjS6aizyhuh1rkg1EJrwXPy0HPBiwndj6aug0ov1odtN8zI8s09cBpVMziwT26bChHuCuMFdvM6-33gUTO9BtUPUdqZa9Wp0y4RGH-jb9pjunvBdee2m54iNuSFkDNc4YOrUciIBSk68Z4HMzbg7oTJxhCFwiEdwK4wyFrPJr-BLbbxCHqPtnb8RJWQdkm5KRCpWOSbYOkcWapeNm82IxHigVvC4UcZoSjIgzqtuahfqP9oIGph-IC4jsieYUo9Gll6W-LxvJM3JfO3Tt_dXbm4XMptxvMoEMo4v5iPWTogm2j-Sj_V8KMd8ZSvkyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ca2071a6.mp4?token=WoVQInoCgJLFFeXgC9h8jQEuVjS6aizyhuh1rkg1EJrwXPy0HPBiwndj6aug0ov1odtN8zI8s09cBpVMziwT26bChHuCuMFdvM6-33gUTO9BtUPUdqZa9Wp0y4RGH-jb9pjunvBdee2m54iNuSFkDNc4YOrUciIBSk68Z4HMzbg7oTJxhCFwiEdwK4wyFrPJr-BLbbxCHqPtnb8RJWQdkm5KRCpWOSbYOkcWapeNm82IxHigVvC4UcZoSjIgzqtuahfqP9oIGph-IC4jsieYUo9Gll6W-LxvJM3JfO3Tt_dXbm4XMptxvMoEMo4v5iPWTogm2j-Sj_V8KMd8ZSvkyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
چه قابی….
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134179" target="_blank">📅 00:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYC64Ox-t7IuS8t0LNpReQp0Z0Y9aPZ2qkQ99FOvX7YEJRrq5y_d8RABvPYfdZpbZMS4aDN0iTmUy_vVlU8L3TB9_KBLaQPVggOAjchM7XGutr4khm7ZPoyTotCY1p9QzNvdpqaq1cUJkLWo1pz3fWuZ0pO34E12eMkf8mWzhve1TmaVCVFvvqz2VDWoKD7RmtZF7mz1hqHoXUtN82y1QivgYnmVegiO4UJKadWsLAq5EXzd-wwyKSjw_S6QCBmFXW44riw9gHofl9ONWPTrZOAwQqUHDCBfxk8-c778cRu-7Wl4TA7xcOA_ecHRLK76UnYPUCHraoPev2MEpP7x-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
بیفوما برای فسخ قرارداد با باشگاه پرسپولیس خواهان600 هزار دلار است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134178" target="_blank">📅 23:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134177">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4agjzVKmsLrj3n5kWsSFQtFIdlwDbOZoo26pmReI1ad5NsyHJO1hf3GG3U3yLOvrZN2oI-b22wJ71Ns9Sfww2KonRvur5_xC5oF0cZ0HzoWH9uK5JzPiIUCOm-G-0qXt4eCpoxq3VqaweaJg-2lw3_fmHcK0JAa6CgIb1fXCLMYMxHd-TU8tvCWzcII4g2oMSotFs_9QP07KIs8qo1SZhje_W9l6lga6hENoOo3rXpS5vWiovSp9uh87_9cACqNYTia0FyOXAdQIpdCfwYcQzEGry7XPWyFTkh0U23DDclIKoeGUyI0_oXTrZ104ty2C6d-EYDoP4MAxRx3lUqL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
فوتبال 360: مذاکرات پرسپولیس با هادی حبیبی نژاد مثبت بوده و این بازیکن در آستانه همکاری دوباره با اسکوچیچ قرار دارد. هادی در فولاد نیز شاگرد اسکوچیچ بود
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134177" target="_blank">📅 23:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134176">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36a825c4c0.mp4?token=ZE8A0WPFFB3gOYGRCO9XHLquT-aecx6XCC8j0A7AQ6Ks7KgaREUi8xbNboHRlB0EdRi7afuhycKNZ_oLp2Zgqg6Y4YlZiKYKz9m40aCF1lXnJuDsdpuw_UU9FrIJz2LGpW9uPiOtlNx0Qb_cPm_AWCQ9Y-OYrjX8lQezqDfgrQElIyL-IYmJk14dJNt0R3Msy8xvYzgMRZSqoxAIzQ5vbSD-RuQXYSjGMUkfX7ljzt5uVIBobonyk7RZy4c-h_0c9HHcKb43R3sGhZ9qBQFBKOaHh92S8jUWNF-U2zRM5jKdipK6QhtZEdxFfbJF0Av6bQcIwrTZm7q59XVxD65nqLRYzNBAcUb1g352nep-3HbIO47I_o5lRc7u1yMydHgQnk3Z92JZwy-MM3lctjVPNmTmfb67dZQg3wjNTt3nX9bt14pylUhNoXfKknF0jv7OKzPHzfppBmagMPYSLVLLSJTcJmJYhoQdPuWrlNe-9toRXrXzEpJH6wrDEx7OYriu1K8A9xBjfvzzjgw25PfQ15N94NnDYNiKpe0rANzUq2oI0-JAyvpnn1IVLiG7U8ebOq6lsbwYVHpaU1uKuNe0yHrpmLmFxWnwNmCPxDPx96yGysw0e9snjGy1RpQrO3tAMlOUb1c5rQC61iPeZu3-dxpEIYFSUZbpNX14o348bKs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36a825c4c0.mp4?token=ZE8A0WPFFB3gOYGRCO9XHLquT-aecx6XCC8j0A7AQ6Ks7KgaREUi8xbNboHRlB0EdRi7afuhycKNZ_oLp2Zgqg6Y4YlZiKYKz9m40aCF1lXnJuDsdpuw_UU9FrIJz2LGpW9uPiOtlNx0Qb_cPm_AWCQ9Y-OYrjX8lQezqDfgrQElIyL-IYmJk14dJNt0R3Msy8xvYzgMRZSqoxAIzQ5vbSD-RuQXYSjGMUkfX7ljzt5uVIBobonyk7RZy4c-h_0c9HHcKb43R3sGhZ9qBQFBKOaHh92S8jUWNF-U2zRM5jKdipK6QhtZEdxFfbJF0Av6bQcIwrTZm7q59XVxD65nqLRYzNBAcUb1g352nep-3HbIO47I_o5lRc7u1yMydHgQnk3Z92JZwy-MM3lctjVPNmTmfb67dZQg3wjNTt3nX9bt14pylUhNoXfKknF0jv7OKzPHzfppBmagMPYSLVLLSJTcJmJYhoQdPuWrlNe-9toRXrXzEpJH6wrDEx7OYriu1K8A9xBjfvzzjgw25PfQ15N94NnDYNiKpe0rANzUq2oI0-JAyvpnn1IVLiG7U8ebOq6lsbwYVHpaU1uKuNe0yHrpmLmFxWnwNmCPxDPx96yGysw0e9snjGy1RpQrO3tAMlOUb1c5rQC61iPeZu3-dxpEIYFSUZbpNX14o348bKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حمله تند سعید اخباری، سرمربی چادرملو به پرسپولیس: سهمیه آسیایی حق تیم ما بود، باید با تیمی بازی کنیم که از ما امتیاز کمتری داشت و سه هفته است در حال تمرین است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134176" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134175">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
گفته می شود در صورت صعود تیم ملی به مرحله بعدی جام جهانی ممکن است، بازیکنان مشمول به خدمت مثل علیرضا بیرانوند و مهدی ترابی از سربازی معاف شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/134175" target="_blank">📅 23:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134174">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6-7sYHg0Xs0FGUKiyN467BXuzOWL337zaJgr17Oq2VIlOOcMIrS4vRHYnnqYtLELvIUdRtcGZDGgzp7U-Wy9y6a90AQ_vN0nc6GRHIJTIFab_1YEjd2QBRLEz7gEc7Qo2krieN7VNIyAcRPgZ9SoKD3SAXwWolQl7EaANsU3xrW-H1iOMJNBXYiVXEWpCA6AS6SO8S_VWqGqLvp4NRnrKB06I8Ot7EXJcd6Zb9kQ9Odp0xPYE_Vrk9dAdYIQSPn_2XC2NTsXxH0H8Rl7cP23KmHXQHPS34CHR4nAEIZCaHuZ7tY0AynONClQocnC_B6Eyo5IYA-THFrX9HrWTnahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مادر دیدیه دشام سرمربی فرانسه فوت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134174" target="_blank">📅 23:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134173">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
نشست خبری پیش از بازی پرسپولیس و چادرملو برگزار نمی‌شود
🔴
به گزارش رسانه رسمی باشگاه پرسپولیس، به مناسبت فرارسیدن تاسوعا و عاشورای حسینی و به احترام ایام سوگواری اباعبدالله الحسین (ع)، نشست خبری سرمربیان پرسپولیس و چادرملو پیش از بازی برگزار نمی‌شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134173" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134172">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahyNfWjFFdeoEyV2PMH885-88v2ku_mAfywzoBZCa0FTRiY3wgw6BsPM9eO2JgtbCIhmmRuWzTddaNZ6w12sfHG_fC553fh4gWBuz0PUCX-ADHm-S_WXFFDAQCxZhcTMPE1AA7J8cPm61kS8TvWnn096TS9n8F3Ryw8GxbBNHVGofC3yn8zHjwlf0CfivYb9dLv0u0QUzYfpN9O4z8MO1qy67llMC5vwCnUI9rBbVk0wKe37XKi_X7TLq3Ujv_iWLuDJ0Wu8WnElxN8eR8IOfN20WmndtNvKULmBg0vmRfQ0UmMm-gEce8BihG0J-DRFHW2Q4zzm5QsU7xYgX4V-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
امیرحسین محمودی: اگر فوتبالیست نمی‌شدم احتمالاً کشتی‌گیر می‌شدم. اول کشتی را شروع کرده بودم و دو سال کشتی گرفتم. در کشتی هم خوب بودم و استعداد داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134172" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134171">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
خبر میثاقی برای تصمیم درباره نماینده سوم آسیا: تورنمنت سه جانبه بین گل گهر، چادرملو و پرسپولیس برگزار می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134171" target="_blank">📅 22:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134170">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
ازبک دومی هم خورد ..احتمالا سرگیف و ارونوف و بیاره تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134170" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
ازبک دومی هم خورد ..احتمالا سرگیف و ارونوف و بیاره تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134169" target="_blank">📅 22:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134168">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnkYV4Fii7G9yPoIlEUOn0eTgZ53-JFJAKcbFKLlJZDXZhdPY3tQ1XzgDG5Rv-QJRQqo_s9Ww2ZU2Pe24eCW_HnVi7zAeY54qtcMr5JkFMrTKmVTM-qf_NGkTec18PrvqdZNZUsguaK4Y0PaYk8OUGxTV9M-y6ytxlYCmetUPtfkgkRmjS9p9zR9-EvOD_ZDYLSR1Ckklwr7L5E3wrd7ihTWHcrZrUUR2X0LMxH6bwX-WkEAPaoTel5eCnmygGROwaAiPjYtVPYwTao5-4rUY63nMfxzRdxIfCJMxy6bfvk-vPy3o3HT5U_akMKbmYTcRwRsgemP4VotVE7Lx2TFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گزارش تصویری از تمرین امروز پرسپولیس
🔴
پرسپولیسی‌ها در ادامه روند آماده‌سازی، با تمرکز و انگیزه تمرینات خود را برای حضور در تورنمنت انتخابی آسیا دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134168" target="_blank">📅 22:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134167">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚽️
✅
رسمی؛ اسطوره کریستیانو رونالدو باز رفت تو گینس؛ بیشترین گل زده در جام جهانی توسط یک بازیکن - 6 گل توسط کریستیانو رونالدو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/134167" target="_blank">📅 22:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134166">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-xpRNf1D-IURupufh8_IHxWvfns04l46-WwSKzB7v8zHQIbzzXU00iXjSC4UwyPVB2T3tLrWZNh6JThuq1Gph4n9GuNuucjA3JFI0Tp7cUh-ytgYRaQ2_925TvRHbJwfNcWa-Jn8Qc_-hSnVZS2StAauV_44y2G0I3JjX-97zQMtSbYLvWThdXYUcGwZXkufCWt1l_d6p5zctjYEeJTQA-7vbRZNkq4_LcThA8wC7GU-BAW0F3FtmWk4psNRBMAwrv1CKnwJrts57MDur0b9LzmTxZYF6FYkQiGH4-0qndTdGTQwACOKXxzyjiI7rjAxpaGa5ZsFXz3621XlRCX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های امشب جام‌جهانی رو با ۱۰ درصد بونوس اولین واریز پیش‌بینی کنید!
⚪️
England -
⚪️
Ghana
⚫️
جام‌جهانی گروه L
⏰
سه‌شنبه ساعت ۲۳:۳۰
🏟
استادیوم ژیلت
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
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134166" target="_blank">📅 21:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134165">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdBnLN8WiNB8XdOmAm7g6cC2-MEvOYBGfL2PXwlyTuyyDwAtFhI7k9W5jCT-69xXhLTMItMUnHt-HNvoI99is8l8DtrHR_Iu-Eu1u78bHJxm6BuYTtT0EeGcqUWcvztlclQ8fJSecebLTyVKKH62YIT39fXB9pPUOYaIK3GLXZ-EKVNCToUyQWHyz28-dp4cZsuUXd5qMQJqr7p_YrYKYHcFg0Y9ku5eus0b2jO_UceJdYDwfZxjW9uCDgXcoFVkbTK_5PNXS2t2Bi7Zfftm--BLvCihh__PbFksBBYtvR9lh3fYQhBUm3gpE2zHvwQo-4m6AB7AAzCzdLB9RjswvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✅
رسمی؛ اسطوره کریستیانو رونالدو باز رفت تو گینس؛ بیشترین گل زده در جام جهانی توسط یک بازیکن - 6 گل توسط کریستیانو رونالدو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/134165" target="_blank">📅 21:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134164">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
فووووری: سعید اخباری سرمربی چادرملو در مقابل پرسپولیس حاضر خواهیم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/134164" target="_blank">📅 21:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134163">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
داور فینال جام جهانی قطر
❗️
سیمون مارسینیاک از لهستان داور دیدار ایران و مصر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/134163" target="_blank">📅 21:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134162">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
رونالدو گل اول و خیلی زود زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134162" target="_blank">📅 20:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134161">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
✅
رونالدو گل اول و خیلی زود زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134161" target="_blank">📅 20:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
ساعت 20/30 عجب بازی بین پرتغال و ازبکستان انجام میشه ..هر کدوم ببازن حذف میشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/134160" target="_blank">📅 20:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
فووووری: سعید اخباری سرمربی چادرملو در مقابل پرسپولیس حاضر خواهیم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/134159" target="_blank">📅 20:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
❗️
تیم چادرملو اردکان برای دیدار مقابل پرسپولیس، ۶ ستاره خارجی خود و از جمله هادی حبیبی‌نژاد را در اختیار ندارد و به نوعی یزدی‌ها هم نیز مانند پرسپولیس با ترکیب نسبتا ذخیره وارد میدان خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134158" target="_blank">📅 20:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
تسنیم : مخالفت سازمان لیگ با حضور تیم امید چادرملو مقابل پرسپولیس
🔴
با توجه به اینکه بازیکنان چادرملو هنوز در تمرینات حاضر نشده‌اند، مدیران این باشگاه از سازمان لیگ خواستند با تیم امید خود در تورنمنت فوق حاضر شوند. این درخواست با مخالفت سازمان لیگ همراه…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134157" target="_blank">📅 20:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
عجب جام جهانی شده ..اون از اسپانیا اینم از پرتغال
🔴
پایان بازی رونالدو و یارانش در بازی اول غافلگیر شدند.
🇵🇹
پرتغال 1-1 کنگو
🇨🇩
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134156" target="_blank">📅 20:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
فوری: حملات سایبری شدیدی به بانک‌های کشور انجام شده و اکثرا از دسترس خارج شدن.
🔴
یه سریام میگن بعد از محاصره دریایی آمریکا، دولت خیلی ضربه دیده و در آستانه ورشکستگی قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134155" target="_blank">📅 19:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
🔴
مدیران باشگاه پرسپولیس در آستانه نهایی کردن قرارداد هادی حبیبی نژاد ستاره 30 ساله ملی پوش چادرملو اردکان به عنوان خرید سوم هستند. مدیران باشگاه پرسپولیس گوی رقابت برای جذب این بازیکن از استقلال و سپاهان ربوده اند و اگر اتفاق خاصی ندهد حبیبی نژاد فصل آینده…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134154" target="_blank">📅 19:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
داور فینال جام جهانی قطر
❗️
سیمون مارسینیاک از لهستان داور دیدار ایران و مصر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134153" target="_blank">📅 17:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
باشگاه شاید قرارداد میلاد محمدی رو تمدید نکنه.چون قیمتش بالاست ...سر همین داستان دنبال جذب ابوالفضل رزاق پوره///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134152" target="_blank">📅 16:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
باشگاه تمایل به فسخ قرارداد و قطع همکاری با اوسمار ویرا دارد.
🔴
🔴
به گزارش خبرنگار قرمزآنلاین، قرار بود اوسمار ویرا در باشگاه حضور پیدا کند، اما هنوز این اتفاق نیفتاده است.گویا مدیران باشگاه هم تصمیم داشتند جلسه ای را برگزار کنند که این نشست به ساعات دیگری…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134151" target="_blank">📅 16:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
ورزش‌سه:
🔴
اوسمار ویرا از پرسپولیس جدا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134150" target="_blank">📅 16:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAIq7GAf0r4D2KD_3dDwAa-DDs7unL2G9e5b_vD20ywjXE3rWWtUeRAqTC6omF2fGPVI4cX8USPLYrePtJmw8NvTyQ6G4bDxe3Pvq-1EQYm8c2lbVQ63eicQSCaE4lkcYmUkRQDCs8Hl-LWUzxJdh7V0IwNkW4lBm2TxWXetc6kRowARjXs-MnEA7Olo16eJAV8vff-LJ4n0Bj1_kwljYUD3VcGs-vl8nFuix6pzFj0z8mAi5dqb80qetl9oOZ_Jx3fHqT8daByKGRakIBx2ufiuD1idBXHEz9pvYnt9CTOFMobGDHPyIw9_htYWkiGNmTuO2hYlBXAe2G_PE0EIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
داور فینال جام جهانی قطر
❗️
سیمون مارسینیاک از لهستان داور دیدار ایران و مصر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134149" target="_blank">📅 16:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3o8i2gAXMm0KVjtq3Ver_sbtLe8N1dFpLhOBIwdFQOzRdNfXTfkHDzrTiV38v3goQPjgI1VGF_xGsnrQyGDR-NpYpO3TlhEvv_5DIINLEaaGK06dF9iQr4D0A4RXKuajmUr6BcIfLcptWGcErlKHJB4_LUDLcKuWQNqve95AxtQ559A7kqOPn0JEGA6fh95UTHhsleT_iBD5qJoIjhZh6iXyH3tAMb8s2Pjv3hEFqENMagTDCpcMTYqShteYVOTaJQ1ga6HD8WW4mruQT7pi_FjaIqmY5MtRhiOm_GFv8ZZPqcqoDn6JL0o1BRdaOGm9Ghr6OGTUtUa-He5-FOR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
رده‌بندی تیم‌های لیگ ملت‌های والیبال 2026 در پایان هفته نخست
🔴
ایران در رتبه پانزدهم جدول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134148" target="_blank">📅 16:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq1652fwgDKi_ijr8z5FLlre2vvj22Dgr0GD0rWaE0PrlRYWfx2V3mpwjQahAAmt0j5KG-MwgN3wBdAQE5Tp6q9NNfcscbauEgr5k6XfmPgTxMKtTyhu4E3TZYVwz2BiAuh7M6ir7cKi1GwdAJ2OPWmzvOd74gQHDFl4boztyqtw17AIieBTgNW3XzQC_fUeFMGQOlBNgym-9LD38uQ-IRI7QUspjIr3gokkiApQVbo_rfR0Nq7Ylv9Bx8BTGsCNi6hS2URJhWTERBOzM4ODMPW4g9qjEyIX5fOJjKzQ831kllr0BghIFz13C2fO5RGVGPPw4bQ-p6z5Yxu4QIoKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت جدایی اوسمار، کریم باقری با توجه به این که اسکوچیج بارها از او تمجید کرده است، ماندنی خواهد بود.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134147" target="_blank">📅 16:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d841d0291.mp4?token=OE9-rBMo7Y57pc8Tw3TlLCwa7YBkNbUDqKq4A21pT2iwdDYvlfrmoe1fCa3aJlYuWAmAnAWV7VlJCXIrDcO7B8pu7m8wRMvRwDsAdi7ay2DKLcSlzlMzJE9oTRfaMA7e2k93tNrenznPbuAfconG63Jka9XRgm0goPL72Yco21gvKQf4jXCuDidCHiHAKt3zx8T8ZBwfOuMbu2SlPfgCBBIQytXEnfpTvta-pKRniecNSm6GR3hFYMsQ5CzIs2HLnWDQIpX579okEzLJ9Md_t9ZDjSY_qCBkvatPNqR3RpJpd7zfs24AS0iHxqS5VVUNyEn0tWYs38YlFIKO9c2xKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d841d0291.mp4?token=OE9-rBMo7Y57pc8Tw3TlLCwa7YBkNbUDqKq4A21pT2iwdDYvlfrmoe1fCa3aJlYuWAmAnAWV7VlJCXIrDcO7B8pu7m8wRMvRwDsAdi7ay2DKLcSlzlMzJE9oTRfaMA7e2k93tNrenznPbuAfconG63Jka9XRgm0goPL72Yco21gvKQf4jXCuDidCHiHAKt3zx8T8ZBwfOuMbu2SlPfgCBBIQytXEnfpTvta-pKRniecNSm6GR3hFYMsQ5CzIs2HLnWDQIpX579okEzLJ9Md_t9ZDjSY_qCBkvatPNqR3RpJpd7zfs24AS0iHxqS5VVUNyEn0tWYs38YlFIKO9c2xKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محمدرضا اخباری
: کارهای انتقالم به پرسپولیس تمام شده بود اما در نهایت آقای تارتار با جدایی‌ام مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134146" target="_blank">📅 16:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
#فوووووووووووووری
🔴
با اعلام رسمی پایان فصل؛ قرارداد امید عالیشاه با پرسپولیس یک فصل دیگر به طور خودکار تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134145" target="_blank">📅 16:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
مسن ترین بازیکنان حال حاضر پرسپولیس:
🔴
عالیشاه(34)
🔴
پورعلی گنجی(34)
🔴
بیفوما(34)
🔴
سرگیف(33)
🔴
کنعانی(32)
🔴
محمدی(32)
🔴
باکیچ(32)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134144" target="_blank">📅 16:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
مذاکرات پرسپولیس با اسکوچیچ مثبت شد
🔴
مذاکرات پرسپولیس با اسکوچیچ داره بهتر می‌شه. اسکوچیچ که سر بند فورس ماژور جنگ و مدت قرارداد بحث داشت، ظاهراً با باشگاه به تفاهم رسیده و فرداست که همه چیز نهایی بشه.
🔴
اوسمار هم که قبلاً می‌گفت می‌تونه برای بند تمدید…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134143" target="_blank">📅 15:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
#منهای_ورزش
✅
اختلال گسترده در خدمات بانکی؛ بانک صادرات، ملی، ملت، تجارت و کشاورزی باز هم قطع شدند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134142" target="_blank">📅 15:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
خبرنگار الجزیره: ظهر امروز به وقت محلی قرار است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134141" target="_blank">📅 15:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
واکنش باشگاه چادرملو به برگزاری پلی‌آف آسیایی؛ بازی را عقب بیاندازید.
✅
ما هفته گذشته فراخوان دادیم، اما بازیکنان مطمئن نبودند که این بازی واقعاً برگزار می‌شود یا نه و اصلاً فرصتی برای آماده‌سازی وجود نداشت. قرار بود بازیکنان پس از مراسم عزاداری امام حسین…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134140" target="_blank">📅 15:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134139">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otML8a0oh-ItxKmkff4V7RbR_EmIQcXIsN6qJhZKAYJ2OdMGHfdIJrM3xjZ9gEbBwHXrCyk_Tzn9UFWH6Kc-St4q9aGpjLGGFhWTDJvb8ZSI81iOhXp28xPBRmsBSEIgf9SosudYNWoKXoDgVMEmj46bLmg8RORK0G6cxRLgkzIvUk2Fwmqwa_xIrRvVKQKBl8MpHf8F-DWi-sg3hxQQ8JPr56xni3nWoV7Wash0cHqr2d25ZwuTh-BjQ7Gw1X1ST4pnrxT-8-IG6JFYbvXKh5ujzlH79ir2lp8-ypKMy1L7eJCGYjYzGITYSdl4esB73oRyNBrEhVs_M5z8DmtO4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
توئیت کاربر بلژیکی با نزدیک دو میلیون بازدید:
🔴
ما نتونستیم ایرانو شکست بدیم اما حداقل (مثل دولت آمریکا) ۳۰۰ میلیارد دلار هزینه نکردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134139" target="_blank">📅 15:03 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
