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
<img src="https://cdn4.telesco.pe/file/n5CoADku3CG6jc1JoSV0wO5a0FhdBxzU2IT_rVyQ8t-AQQpPhqNES8cR8jgzuDyQ6X5o5hLOsuklDcEyHt5CI1tO_cY4x8tIXIFebyV_C_WfKOyjkmnJBcqRipsJEkDZ3QDZq4QA9xAwId9EvAS_S_f_U-HDv-_NhvWSICI8eMwVZlqwm5pKhZwSsp7m1O0h5XC4Kk0sqsynXas7NmA_QFA5iCvJ49-rJSFDxKTri_OyhSFZlTphvie4ikpOedIDMrbEWKBhoPaetF8Ztvvm2Jps7ZYsQ7jJQ42-lhyRnreOCYqIdcXTclwX_K9LqPj81L2qZhms1U_TAN4B3KS80A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 132K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 01:23:00</div>
<hr>

<div class="tg-post" id="msg-90087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 654 · <a href="https://t.me/Futball180TV/90087" target="_blank">📅 00:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90086">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuQtSODTEACxVJxgGnvNSQK93E6LyZoQKrlN3njakZojC1b5oufpg7wdrCLvXwWc3dQ8G-r5JlI80gO6KZ7h2sJJV8YL-oe626rGLzvbSrL4IsmYzWrpzUs0odHiQ15s8lEIx-rsApEgL2GhLotobwNph0-cLMxpOl4fv_Y_tBKlW3Buwr42d9ODSQzY9XIHlrHVW-A2Xfeuo1o-jfMAiZJOKAH0JERIcrzp1QMpUZsHck_lM_0uKFH1TrGWc8HCvMgUh5JYOCifbXTAbPUr3NNvt4s2MivzvmJbabF77lNtvp6haBZ7aYkx-TOMzKLqLSYhxcrr1UDrTpwIaAoPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال لیگ اروپا
⚪️
فرایبورگ - استون ویلا
⚫️
را در 1XBET پیش‌بینی کنید.
💥
بونوس صد درصدی 100% اولین واریز
💰
پیش بینی تکی برای بازی پیشنهادی قرار دهید و در صورت باختن پیش بینی بازپرداخت تا سقف ۱۰۰ دلار دریافت کرد!
⭐️
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید .
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/Futball180TV/90086" target="_blank">📅 00:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90085">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=G9nDXoJG22LEsRjBisZ-SPkZRCte2hI3755EEJ_YQobz1gPZr-Qvfdn56fui8qc6TeAp3dF4FjSGOhxmHiOGqEP85ZhqqswG4jYKTuAiHWZupzoVA_haPxxvjYh5fwh-QKaKoEOr-v-Wqn5vQxDejAPeIV-3kz4gfrJIbeMRTvYsGo3GaCbCZWT0h5U0M8uoNBS7FQfdYQdkaERrtP3zOUpCGYcy2DRbFYigJRhtZ-pHZYGE9pW-cUckjb87ZGjW7QtKuHYcX4ymJa4Cuu5NX0WUR_vatkJ5zzcanC9XviQSED5FlMcsjN_yuP0Y_6zN5ql8uT0_WhH7BAhasF70eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=G9nDXoJG22LEsRjBisZ-SPkZRCte2hI3755EEJ_YQobz1gPZr-Qvfdn56fui8qc6TeAp3dF4FjSGOhxmHiOGqEP85ZhqqswG4jYKTuAiHWZupzoVA_haPxxvjYh5fwh-QKaKoEOr-v-Wqn5vQxDejAPeIV-3kz4gfrJIbeMRTvYsGo3GaCbCZWT0h5U0M8uoNBS7FQfdYQdkaERrtP3zOUpCGYcy2DRbFYigJRhtZ-pHZYGE9pW-cUckjb87ZGjW7QtKuHYcX4ymJa4Cuu5NX0WUR_vatkJ5zzcanC9XviQSED5FlMcsjN_yuP0Y_6zN5ql8uT0_WhH7BAhasF70eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارجدید حمیدسحری با کپشن:
تاج‌گذاری میکل آرتتا در لیگ برتر.
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال قهرمان لیگ برتر در فصل 2025/26 شد.
🥳
⚽️
Channel:
@Futball180TV</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/90085" target="_blank">📅 00:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90084">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb3LOschieqacODuUQQNtx-lRbSG44y2dngSLQS3ND9igDoY5BrHnZjdLSg5nhI2jQjRKF3iC1orv2GgbeznZjAJNXxhVNbzSod7h2E6zV_UxOPCCHSXUAGAOGPynq0D9CyVpG-dgDgU-yffligXkkbl1PqWksAkODQqsCsivvO5QR3yauQKN3cc3vHGBtalWE5ieEZliWo1IesacVnFC2X2GyNQwsp3-f1OWR4YouhGMWtnhA5EwmA4AUH_3L1B1y8XJ26WopIR9jIGU3iO3sEyQ3RwSoKncPJk68OG-Qeu83Kmr3VFrAtTF0j1FTNQ-dt3TnO_pM6NzVC65IUU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرایبورگ - استون ویلا
🏆
فینال لیگ اروپا‌
🇪🇺
⏰
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه بشیکتاش
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
فرایبورگ در
۸
دیدار اخیر خود در لیگ اروپا مساوی نکرده است.
✅
استون ویلا در
۱۳
دیدار اخیر خود در لیگ اروپا مساوی نکرده است.
📈
میانگین گل در
۱۰
دیدار اخیر فرایبورگ در لیگ اروپا
۲.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر استون ویلا در لیگ اروپا
۲.۸
گل در هر بازی بوده است.
🧠
وقتی پیش‌بینی برای فرار از فکر است، نه برای فکر کردن، خطر شروع شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/Futball180TV/90084" target="_blank">📅 00:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90083">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/Futball180TV/90083" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90082">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=dRI-KO5JU85eVLSAwykzNbBOOAEZS95buvfnh5xBbAkeHbc0sKFIFnxRUVZu8ZtgSaEI3Q2nA_wbkUTfR4WJdApIXHHiE_mIRc9m6Mw14hquJFppVp-aa2ktVNZbSIcNecQiLpELcWJI0Byf1p6JIbHGXUTbsx9qDB9Kw_hah44Gcp8mWytAJCAPoJEabV4_Sq5OpS9-HGy9aoRSgRdSFQpJ_XvpVp6jCroH9gQ_16ODdfWLRrYYMrjYXqfPkY2SFRbfU69vvjS3XiYn9PJLwQIH_AawB-nji9KTR1BFwa835JqSmsRhlGUJzCCPJo8Xz59viF_NBO_hzzJ8tqO3Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=dRI-KO5JU85eVLSAwykzNbBOOAEZS95buvfnh5xBbAkeHbc0sKFIFnxRUVZu8ZtgSaEI3Q2nA_wbkUTfR4WJdApIXHHiE_mIRc9m6Mw14hquJFppVp-aa2ktVNZbSIcNecQiLpELcWJI0Byf1p6JIbHGXUTbsx9qDB9Kw_hah44Gcp8mWytAJCAPoJEabV4_Sq5OpS9-HGy9aoRSgRdSFQpJ_XvpVp6jCroH9gQ_16ODdfWLRrYYMrjYXqfPkY2SFRbfU69vvjS3XiYn9PJLwQIH_AawB-nji9KTR1BFwa835JqSmsRhlGUJzCCPJo8Xz59viF_NBO_hzzJ8tqO3Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💙
سهراب بختیاری زاده سرمربی استقلال: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/Futball180TV/90082" target="_blank">📅 20:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90081">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-30rbpImuK-F-GdyvGJDAzKU84_SK9nVkcdbSWG2QyYkDOaDdA-feBL1CjZfBo9buZ9HttZbSCQ6tNMQL383WUGDqodS53pvCoFgKvqn0obmVDarM5FU2salNYEB0TsMljRofpOpLQka4mKbQREb0WaFoIx8Q-cuEjd1fXuwvtu4GxLSnHiKhhpDS4NxGR-F9lDRapJeyKJ49fLMWcTZEtyMZ4r5dvPhoR8o-9R7F7o6UtzHNjN7WMrC3tx1QWm_o0it0q6oq0A20zlGMK6wS23qWb1wU_4Zpyn0epM7n-KrxULO7ZzKIlo-J8AKVpelBRN1Kqeg_7TQpGudgueOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
از این منظر نگا کنیم؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/Futball180TV/90081" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90080">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90080" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/Futball180TV/90080" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90079">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap0gcRZHfcIu4lb3wEtOkjH-Y4fzn6y0jzhzYYCdJUGjFaBvwnjmCmlyMuDUfeKyA8aNAJS1D3Ely9k5k2rZNjO3AGW8PgUwpb21nmRCAw9y_sRT-wkz4uiUdLAcAQeGO_g-evNtFRIJ44Owy6I4DPYGrf4Q2GCWO7GW_V5T8x0G75nUkiBmxjv8ENzrKjYkIMJDBv_XrHJmyaGSX0nrdfrXpbm8CNWY-Tg0t2Z6lBHn9L8mKH8hb2f6RNsU97BNxBgCNgmOvtdlHlk8ykNeXxT7WwNOARm_u3LHf_pTedYNSRbD3Q7UI1qpcsDZB4sFto1gKUhYr9UL66ww5EAgLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
قرارداد «PSG: Champions Contract» خودت رو امضا کن و با قهرمانان واقعی یعنی پاری سن ژرمن و 1xBet درآمد کسب کن!
💰
پیش بینی روی PSG — جوایز تو در انتظارت
⚽️
🏅
شما در
Level 1
می‌تونین AirPods Pro، کیت خانگی PSG و جوایز دیگه رو ببرین، و در
Level 3
نینتندو سوییچ 2 یا حتی iPhone 17 Pro Max در انتظارتون هست!
😎
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/Futball180TV/90079" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90078">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=cYzthY_dGvB4QJBd3ieM6hl0FgGONPjVzGQz7V0EKoLy4rw_wlBzgepqT5q45kTdPv0aNuKJN84q7Fnt9vpUXU09KHMZLkiIGntwljXwjX-f2jL06Y7YiDJz6GYodtJp4dnFIa4_NNHx-rZob7BzRozfLgVQt-JXrslq6eMSZoTKih8j3O9swD4VO3qUKmP5_xNHJYdIuE2M-WcudxRa1bIZdmgeKQrMhc0kGOF50YEw6jUs90bxhcP7mSjs6lQp25ifWD91xfINJ-ALvfzs9AlMtq_V7NhWYsALKDvSywgM4PrkEsDgjcnTD0kukAS9OTHal7KblWw3Fef9IglEYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=cYzthY_dGvB4QJBd3ieM6hl0FgGONPjVzGQz7V0EKoLy4rw_wlBzgepqT5q45kTdPv0aNuKJN84q7Fnt9vpUXU09KHMZLkiIGntwljXwjX-f2jL06Y7YiDJz6GYodtJp4dnFIa4_NNHx-rZob7BzRozfLgVQt-JXrslq6eMSZoTKih8j3O9swD4VO3qUKmP5_xNHJYdIuE2M-WcudxRa1bIZdmgeKQrMhc0kGOF50YEw6jUs90bxhcP7mSjs6lQp25ifWD91xfINJ-ALvfzs9AlMtq_V7NhWYsALKDvSywgM4PrkEsDgjcnTD0kukAS9OTHal7KblWw3Fef9IglEYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
۵ صحنه بامزه از گزارشگران عربی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/Futball180TV/90078" target="_blank">📅 17:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90077">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=FzYqjIMf68fyAoRVealI0cn_8cIWi4Xk_CsVDykp4thu5Gruz6Z6G9EwDNDQDtqMFXE0GzqmC6Hmgz31HiZp7sHsApe-WzEPEiZ80UxDGURvpsiwRNFekWXV4eoKT_H0eqx94Lq2PNa-nJER6reLm8moozr-7XTLVAhbPcfTN4ioF17gtrA7XUogDERaPHrtjeG2mSL9-e54oH6-zf_2mYtTAG51IpXjDVURJ3WPVR6qgXAwJ3Tuc8bM_7s9QmUeqVJkAbGuU10uryzwPl0udjiNegB2UQmMxmVl9HsKFoi-YA7PACBXxzLHi6ZOY8ngWa9q-soDHW4M68XDc89QcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=FzYqjIMf68fyAoRVealI0cn_8cIWi4Xk_CsVDykp4thu5Gruz6Z6G9EwDNDQDtqMFXE0GzqmC6Hmgz31HiZp7sHsApe-WzEPEiZ80UxDGURvpsiwRNFekWXV4eoKT_H0eqx94Lq2PNa-nJER6reLm8moozr-7XTLVAhbPcfTN4ioF17gtrA7XUogDERaPHrtjeG2mSL9-e54oH6-zf_2mYtTAG51IpXjDVURJ3WPVR6qgXAwJ3Tuc8bM_7s9QmUeqVJkAbGuU10uryzwPl0udjiNegB2UQmMxmVl9HsKFoi-YA7PACBXxzLHi6ZOY8ngWa9q-soDHW4M68XDc89QcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
شادی نیمار از حضور در لیست تیم‌ملی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/Futball180TV/90077" target="_blank">📅 17:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90076">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J26AwqTrj9qtLx4UAr5EzUmznpphHU2qqDbxDqDpAhpSs68kvc873Lng141ZkjrWWYST1va-wMm84V4GFmiFUVL0eAO_JztgGj7RV_DYdXRirwGVnb_H0MhdN3ySd8GFjejRSkcL2lVp5ElfHhAS16XV95RKcSV0mO7Zyr33trI8_-WZiaa_g2ClJeOqiSI4hnb6PY3EyVOcMuOYR5dJfPHbo0FhyIcC23nFNnrAgD_3BOk04Z1wPZVB-q1E7M63LEjMvHC-RfkAKiiMA3Oguy-BdcTQMAOV9o4DgR_lgQPnE2ykWU_imDTu-R95LblPrXR5RkHadrwv1sjy4U2fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
لیست تیم‌ملی پرتغال برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/Futball180TV/90076" target="_blank">📅 16:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90075">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=PWV4ci979qTQxNkygldaK9vjd31F1taGDo-LkjOma0EdlgMzoad8IPJKhnVrfGIIkoseU2iZVTVt6c-qpEIgU8eZGMEypM1r7cw1h1rMJ91l5LJiiXbpoS5vJAxjJNhj5hrw2t0tG_mBaRXQl8_ZQQudZSQeGdPCbToExI9-E-PD_QKBbmAlw_1G7bYjLfcMpZ-HlGOWhkFt5oa0H5ZuPV3fDUsDPd3NnDGYUjdNUcKNqvZO6gBVbk8JG8kzTtr5YhlrzyyiV8vxnguPCx5sUqVLLfE28RkOv_4GPjxV41KD5zVeKDU6PqRoYYzipfkLYs_UDnbRUiiD8uANKEB5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=PWV4ci979qTQxNkygldaK9vjd31F1taGDo-LkjOma0EdlgMzoad8IPJKhnVrfGIIkoseU2iZVTVt6c-qpEIgU8eZGMEypM1r7cw1h1rMJ91l5LJiiXbpoS5vJAxjJNhj5hrw2t0tG_mBaRXQl8_ZQQudZSQeGdPCbToExI9-E-PD_QKBbmAlw_1G7bYjLfcMpZ-HlGOWhkFt5oa0H5ZuPV3fDUsDPd3NnDGYUjdNUcKNqvZO6gBVbk8JG8kzTtr5YhlrzyyiV8vxnguPCx5sUqVLLfE28RkOv_4GPjxV41KD5zVeKDU6PqRoYYzipfkLYs_UDnbRUiiD8uANKEB5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدا رحمت کنه زنده‌یاد علی‌انصاریان عزیز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/90075" target="_blank">📅 15:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90074">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1631168f15.mp4?token=tOip8Rt71bUZM-p9qWJjpF1nQjXY8jVGh3YH4fB6vh6ge8SYkgcYQcRU2k8eGG2oULMkZXfjjjtKP8DXjGSNSjUgDBvygcyNhTSuiqOU33kiLTWzNbKoaARAY7gx7UH0PJPNdZl5awTtS2Kv72NIcgZXY7OJkaF0Ob9eRUz78aVulMFHAWUs31ck6D5-eviupgtmSacptdtZyroWOtwJ-pyjn_WRkTvB-yFfWPa1jYvuiIlHmEYNZStpaiQ8qdtROKyGKEVjeM0uHnf8xmul0CTZD0rDfYSk8kGfWAdupPTaQRUs8zTe239N1qbzdashiJzb3xvEhTJC0jM-6CS_mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1631168f15.mp4?token=tOip8Rt71bUZM-p9qWJjpF1nQjXY8jVGh3YH4fB6vh6ge8SYkgcYQcRU2k8eGG2oULMkZXfjjjtKP8DXjGSNSjUgDBvygcyNhTSuiqOU33kiLTWzNbKoaARAY7gx7UH0PJPNdZl5awTtS2Kv72NIcgZXY7OJkaF0Ob9eRUz78aVulMFHAWUs31ck6D5-eviupgtmSacptdtZyroWOtwJ-pyjn_WRkTvB-yFfWPa1jYvuiIlHmEYNZStpaiQ8qdtROKyGKEVjeM0uHnf8xmul0CTZD0rDfYSk8kGfWAdupPTaQRUs8zTe239N1qbzdashiJzb3xvEhTJC0jM-6CS_mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ناراحتی شدید خانواده ژائو پدرو ستاره چلسی از عدم حضور در لیست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/90074" target="_blank">📅 14:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90073">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URQchoGR45V3FxTI6e2zxqLWs_C6oQJB3i69ippLgwhJnYROcX4ASLmovpoMSIXqrGS57L9depZBu-XE0Hc0pmN2gbJ4GvSY2GYgxn5Ct0Oll9Ed0ofEiCukhB6y2HiP3pZmSETQq6T6WQHc8r1x2UheXI5pW9o3BztQlf3uXvpE11-uCq5wxGxZmTNmMuzjC0MgbxVcyTYwRncO2lfS61tBSYkkXGToB-EaHQ6ukRJjlwZsucqE9nly7jf-2GpoboOD84njnpdRR2g_nFP-wI3b4Up_Bc4ZWVA7c2xvVH3_dQ3GTB5njnRWmiho4jMFrzVwVQ19XbCk96r1fd0uyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با ارائه پیشنهادی خواستار تمدید قرارداد یکساله با آنتونیو رودیگر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/90073" target="_blank">📅 13:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btZ3V1FwL8wffuKx7IkrZhl0V1LmUPiARMrAwIpOf_4NN17fpzkfQykAoqXDAQSDszDTJBylp0TCIq1LneWJk25Mjj0yhDR_tk1xL0HV_BEtfMlS-XwKOJJW-3KlZbwptngrW2sUctAfuGsAK3bff7k8V_RBrkfx_gI4COj1Wgvoqt_NNPlImGQVUJHfP64TY5j8Nue0zP3Nn7Pz0AUQtWBemASJsKCSw7zcD99MwOwSKNGp8iFGcLlthUPK2ivqZXJY1aES-ltCZTfWBlw9i_YjYXjAfQ3rUvVwvm9PxoP1YuJLkUOLJpPGEokWattbihSSHY2P9GRs6a-uK5WH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد قصد دارد با ارائه پیشنهاد هنگفت با لوئیز انریکه سرمربی فعلی پاری‌سن‌ژرمن قرارداد امضا کند اما در عین حال این مربی پس از پایان‌فصل قراردادش را تمدید می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/90072" target="_blank">📅 13:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c098031df0.mp4?token=POEbVB890fbrn5kblo4kSVrdiCZ4skScGXF__h2HjPxkjpSdd-PxvECQZ0GwFtNCfUvWbnuJEQ1PcWruXO9K4rRdZ--Cm5skkxlhd8E4Nr1ThaYENcUb_N6h_E9sY5rBLPE8uQgHApw2WxA28J6U9AHItJ8asmqkgNEO5_GWzXnHrNwyrJXj2bof8hoDZQDq3SmG68pQBIxRRMPMSubZeSiFfhRJ24N3__fItZC1r2UTJMym-CNdaPKoNSMCnbbgANWf-7SkcayFfrQks6lRBTwEENEO7zPft9CgKEAesUp5G4BtProb3Lf0xZMx5e6FRAhxjMJPcQHFn5viHxxP1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c098031df0.mp4?token=POEbVB890fbrn5kblo4kSVrdiCZ4skScGXF__h2HjPxkjpSdd-PxvECQZ0GwFtNCfUvWbnuJEQ1PcWruXO9K4rRdZ--Cm5skkxlhd8E4Nr1ThaYENcUb_N6h_E9sY5rBLPE8uQgHApw2WxA28J6U9AHItJ8asmqkgNEO5_GWzXnHrNwyrJXj2bof8hoDZQDq3SmG68pQBIxRRMPMSubZeSiFfhRJ24N3__fItZC1r2UTJMym-CNdaPKoNSMCnbbgANWf-7SkcayFfrQks6lRBTwEENEO7zPft9CgKEAesUp5G4BtProb3Lf0xZMx5e6FRAhxjMJPcQHFn5viHxxP1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
پاکتا هافبک تیم‌ملی برزیل و دوس‌دخترش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/90071" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90070" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/Futball180TV/90070" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twMg1l0_WqB-2I_ngBrD8PohgZGHPXnX3BxHzLr6_DGOjHESjbkm0C3_spl24lBW6l7g2QVGvqLHWZ3l8ogo4NUVS7JZ_NVFgFV_NWo5WDw_zZo_E2aiB8Vx1Ev2P5D4iBd67eAWIloeYbVRF5WAqLGPwkwyGK2BDBLIo6zVP0IEqJvoqmrJLlwcGXzt6gGrPXE8R68hUsNTeHeLUEcDz8IeK7Jry_k45feYyt9yQr2ykPDz4AiQH_EV0fnwYUMT6C4ureCF4UVwXS91qXmHLJf_LuKX9KP5Ll1A8gPympts0UhvDHJmrSIrrjpxmFdaNpDU88T9PCBghHby-C6JaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Ole, La Liga:
بر روی رویدادهای مسابقات فوتبال لالیگا پیش بینی کنید
!
💰
در ابتدای هر هفته، یک پیش بینی رایگان دریافت می‌کنید.
✅
هرچه شرط‌ها بیشتر، پاداش بزرگ‌تر!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/90069" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwZaRFrtFl0svGmtTL5uei7CA-2XoW0JaM6Mow9LG3vdMS7ND2cRGQbIfp-jIEhZvEhmnSRI8d14bicsPjBc5qHCjv2QinNAZmmb3ob6khnxGQROHG8mULbrS7lypO5z8Fuw4Wi7gEYmIkz57szQSE85EfNaJr_uVhdL3AyAW575jK4yA2-6lms4uYHuX4bbCjRvQvOJPHZlRasIiEBvtJrfmshIXjrxJ42jHL3eoqQnbkYzQOB0jf4cK9bWXkpH4pJKngG0Lxua64enrJq93p0nluLv0xKdq0zMVRK0teAEM0TD7LB-rd6lfc7XHN6h02YLSB03dbEknT7YIcJ27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کیت‌اول باشگاه اینتر در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/90068" target="_blank">📅 11:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSQpo2IkoqPxEfY18eSkTcRbawofi2GTTNbv7LK9BmUq3F_s3p3bwyBtr_6DdPB8t1Ju4_6jwq___ODXoN488oX_tw-q31pcPzLINaQer45dcXymmMoF_aDTPpQewxz-gtWtqSGns02pQy4bt9ST66R4AJvDOnj3mYdciLBM30Q2xmXWjf048VggTFVA_qTRFTVpWhie2v-2Nf3C21xNPPQAujo6IZIIp08cv75CXhq0LE2O-fngvFzaA52it1aB6cehGjKXsVEz14ljr2n7RsECKH7AGK283slxwJuJyE64I-yUwehrMX-bbDnTvAbramOquwXVyEjSNHTtTDo2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول فصل‌آینده لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/Futball180TV/90067" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=TaL4PljUxNudilpKFsrTtVqJb4bvb25-i5HAFCZlsTFfMPPuHCoO5xtV_11NbNSIy6GxWImCnK5bVaYKJ3aL-VzIShtv7BTAB-sgmdreQPVwMtJwoQ0aTdZFCiNpxf9b_oD27ocGTtwBweFm2NB8DncU3QpdKW-F6Jfb2NZrL1PJTyFhunoCPVipoO1lBrrF4up1KNvhSIxtX8AhjcV-57zRKt5sI_ZynkNMHYDS6WZIZSBUmCq0oTEWFbdd1duxogctB2G4ZdoAgV25dJFQ-SA9ehqFM7BVyhCpc9sVlPwoROKvfVc3x7eXxC0nCgmHJugKGxXMg_WcAtoD8v3nMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=TaL4PljUxNudilpKFsrTtVqJb4bvb25-i5HAFCZlsTFfMPPuHCoO5xtV_11NbNSIy6GxWImCnK5bVaYKJ3aL-VzIShtv7BTAB-sgmdreQPVwMtJwoQ0aTdZFCiNpxf9b_oD27ocGTtwBweFm2NB8DncU3QpdKW-F6Jfb2NZrL1PJTyFhunoCPVipoO1lBrrF4up1KNvhSIxtX8AhjcV-57zRKt5sI_ZynkNMHYDS6WZIZSBUmCq0oTEWFbdd1duxogctB2G4ZdoAgV25dJFQ-SA9ehqFM7BVyhCpc9sVlPwoROKvfVc3x7eXxC0nCgmHJugKGxXMg_WcAtoD8v3nMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر صحنه بازی دیشب آرسنال
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/90066" target="_blank">📅 11:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90065">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد آرتتا با آرسنال در پایان فصل به مدت دو فصل دیگر تمدید خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/90065" target="_blank">📅 11:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90064">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgBe99WVi8PDmUv6QdEgseKJfK_hAFuJi-GxZhbWV8lggGYU90RAZR9a5zGSAPcQfnRkF-Z1wdOjeR_TqWg6Uf9gW9tKlQs8Q_9tffFBlXvL9ZWOnrL-4K_7_sDEP30_mB2BsoCPwE5_n9KUPCxgrX0S2cbW-YRTFXeNTAQ-A0oqmZR6J-E2tT3D2BuhO3bietvpWp98oDiKyGxvf0869XAebHZ-qt5lxdh5ZIp2XMmjWUwXY6vLDIEMxpuyWUeR2OacoPszQwmbDpKeEUGVtlKue0VnAgFF-P5yZ5nLutn9aWTWE9SszeB1Sbb12QSBfUH_AiHu8vCZfLpUk7-Nqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
با اعلام‌فابریزیو رومانو، انزو مارسکا با عقد قراردادی سرمربی منچسترسیتی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/Futball180TV/90064" target="_blank">📅 10:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90063">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=BenyKiRAv2oCFaJdQyyGp-EsKbRw1qmSRM5EY3lPLamzZKVU_X-hfDwbFKvSpKzGiBHQP9G_YCGcHQhwRipwDIeac6MJyNIM5EwDyHRennWQw1Dsy4JD17FYufHuXsZ_uwSEHahDVCZhIaq2UrLWNJlK4uHT-1-fTRvGFgT75NGZ50weFgEBH5G0pJJRNB6CilQSJwx_UwDbdeGZtxQG-BACtXKn_on5DXWhqbHDFl9cYMrX_bhlAsYBNA9D4EsUqilsf5zte14qkVdBjkiv-yL4dXA7S9CFknFe8QpBnERkLFz_cIQw3BMzuf1dMdW5bXS9f2zCZ2JRkmdD-aYHhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=BenyKiRAv2oCFaJdQyyGp-EsKbRw1qmSRM5EY3lPLamzZKVU_X-hfDwbFKvSpKzGiBHQP9G_YCGcHQhwRipwDIeac6MJyNIM5EwDyHRennWQw1Dsy4JD17FYufHuXsZ_uwSEHahDVCZhIaq2UrLWNJlK4uHT-1-fTRvGFgT75NGZ50weFgEBH5G0pJJRNB6CilQSJwx_UwDbdeGZtxQG-BACtXKn_on5DXWhqbHDFl9cYMrX_bhlAsYBNA9D4EsUqilsf5zte14qkVdBjkiv-yL4dXA7S9CFknFe8QpBnERkLFz_cIQw3BMzuf1dMdW5bXS9f2zCZ2JRkmdD-aYHhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
شادی فوق‌العاده برزیلی‌ها از دعوت نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/90063" target="_blank">📅 10:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=WZux7ZBxqZlr-PZd_64iyzPYfHtrRRWB49eBZWA5Iu9VkjqLdGnii-bmTWCeGmoduUnqmC2Ln-0MHGP_9rcBrhFomV0kEV61Uja9HMKEBjs_sx3uiemlGkcjd-htK26ckXPbAmdfj0dBpQN_c4uI7IPg2UfEhE36g8uu9STH-emhI39ypBQHl273_rFhBjjjQ6a3ONfndC0AS1CHCm7PJxd-O-tPed2rgDvwhk_c7-wb02CCoSx2NW_KxbUlifWIauvSsEbRXzb6tzMd_E2k510r48tQXkC0uRwnAdVWbjiABGb-tU7tHgUvVUYWp194kjFYouSq7Z04SQm_unTv5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=WZux7ZBxqZlr-PZd_64iyzPYfHtrRRWB49eBZWA5Iu9VkjqLdGnii-bmTWCeGmoduUnqmC2Ln-0MHGP_9rcBrhFomV0kEV61Uja9HMKEBjs_sx3uiemlGkcjd-htK26ckXPbAmdfj0dBpQN_c4uI7IPg2UfEhE36g8uu9STH-emhI39ypBQHl273_rFhBjjjQ6a3ONfndC0AS1CHCm7PJxd-O-tPed2rgDvwhk_c7-wb02CCoSx2NW_KxbUlifWIauvSsEbRXzb6tzMd_E2k510r48tQXkC0uRwnAdVWbjiABGb-tU7tHgUvVUYWp194kjFYouSq7Z04SQm_unTv5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خوشحالی اندریک در کنار زیدش پس از حضور در فهرست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/90062" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=bBtzqO2hpx-2LijFXz6wBkH-8wUeL8-mWDpY1cJilDYjGsHTU7bP_jDvLP89R2EclXFzGs-TCID3I1CmdH1zsBnZknxh5_eFy2uo492eTiNqXpuhQabRPkRzQQDA4mw5eCuy0jSyIMh6QsBFWUs6bypR6cc3xbOfm0BccRCvfugg5M6gA2G-rMAbtt4-L8LbFLxDkfpbR3eq_m4SfZEBHHgOUPfNg1MJISTdz47qiS4Hesoyxv98jl3GfMPF8XTsLKFacGHjayl7meWYC1s5MfWxumHfusW9DJ7Rqmn88nLnT881RyynsSNhrsCFL0EundWETAYx8ma4DeH2kFUYVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=bBtzqO2hpx-2LijFXz6wBkH-8wUeL8-mWDpY1cJilDYjGsHTU7bP_jDvLP89R2EclXFzGs-TCID3I1CmdH1zsBnZknxh5_eFy2uo492eTiNqXpuhQabRPkRzQQDA4mw5eCuy0jSyIMh6QsBFWUs6bypR6cc3xbOfm0BccRCvfugg5M6gA2G-rMAbtt4-L8LbFLxDkfpbR3eq_m4SfZEBHHgOUPfNg1MJISTdz47qiS4Hesoyxv98jl3GfMPF8XTsLKFacGHjayl7meWYC1s5MfWxumHfusW9DJ7Rqmn88nLnT881RyynsSNhrsCFL0EundWETAYx8ma4DeH2kFUYVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
پایان عصر لواندوفسکی در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/90061" target="_blank">📅 08:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/90060" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AEb19xAMEueVsMXICRTQhuleuJkzEClEIqGBrCYNV790KPZTvKXfDwJOQuR6jKr96JzMO62DgPbRaHLKY5T4DOrWOBGAfJEjrFg8qh6sIojDY1clZxdxXgHxIYljG_3oGOvcp90rmxGYFU2Pqe4aRhr0GpaPD9ozZlk5zqUcSKlsVtfh1959HsrB8K6cNNTZpkoYoZQTQz_q6eBOeVLPterk_w0OcCOyoa1ve74-l8oCLjGwZr3f37ciWV3q4EfV5jk9_Qqp000KmyIlZHvW7p09sPsQALrzfL3u6qW3G6zRjFj5oXv-ES2J2lfgjt7niFnGk2OKEUpU5g-O-mqc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/90059" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=OLN8oj5pAQ9rdxNLrApUj48LRIYHizTtx_h8feFGTEvQ74To0yc28nHXBQDvQdATbzBL_0EIkzzaJoKI48eMmYqBE1mX5At6hN2Tq9tQa-Vyz71nuqUead029WzEDkEu50YHr0aSMR_t8j19GAn66ExB0kaRB-J-ZdzZ7vdPLD6xlWCMFQ9cFau6wc43qEVPDe7I2IIc1yraDtCXzX3d9zr9BBpkpCnwQhn4YU5PVibNfUpayfLpR8SkfcG-gPzqRTWfeDRuxiBln-Zl9553qQbPnHppmbHujkYrxsQpMnMZB6Lf3ZYZkhH0Vm6wF3_H6UIEJUiLdncrGZY17C6kvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=OLN8oj5pAQ9rdxNLrApUj48LRIYHizTtx_h8feFGTEvQ74To0yc28nHXBQDvQdATbzBL_0EIkzzaJoKI48eMmYqBE1mX5At6hN2Tq9tQa-Vyz71nuqUead029WzEDkEu50YHr0aSMR_t8j19GAn66ExB0kaRB-J-ZdzZ7vdPLD6xlWCMFQ9cFau6wc43qEVPDe7I2IIc1yraDtCXzX3d9zr9BBpkpCnwQhn4YU5PVibNfUpayfLpR8SkfcG-gPzqRTWfeDRuxiBln-Zl9553qQbPnHppmbHujkYrxsQpMnMZB6Lf3ZYZkhH0Vm6wF3_H6UIEJUiLdncrGZY17C6kvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
خوشحالی مارسلو برای نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/90058" target="_blank">📅 00:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZTA9lsGEjw_mKBHpvCKvCzp6mHyqK929DVBhE2u3PsI71qTqqqOZxPW4GuuFVZmgCvCi_-x9gUjNa7pF09N5aNy4pLSI9rM8bnF9ZduLUdy9wZANjIcMEKcJSDPylb6QrJYEPn0CeaxzOaKEBxo3z1imVNHDG2JNqPi0oGtPA8rbAqAQuZSHCV0LwGrv7FnmuQR1-jbe8xHOp3njKNTdCN4ra33VUGnTitf6tXRmysqh7lm5maYJuZ9MQT8yeNZk-0JLoY-2hkwtCNIdKdyKojaJN2r0KS-l1XxziKRlUtTFeUAtjEH3lKP4C4K4_aeunefSG9gm9zTrMENWhvQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر انگلیس پس از برد امشب آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/90057" target="_blank">📅 00:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtXJ9JXLE7gShX9Mv0VBvOKXe0Ng1FjZCOjQWmO_GYP0720duC7-YXjEHa81et4dK1i1s0-iRo3MOhDQOsqJoaV6Jj53Y448k8ON4ZsvUovplY9GQu8Tdlk9mggQ-JlJ90BYNJ6v3ilvne6bLSo0mUPjTxoo7KC1lRB-QIC2gCC_wGpGFF2nTC-mvqEcYmIn6N3GfzUuluKFbJ0T2dxdPdW2lBvQr6PhHzG_deeDXmMMBL3JCejZzAHaCAAbGC2GBqArmEGnRtVJ3fgO2if8ifcG1DDYksFaNe9ffKOh318OMNUpCtAefwjpEltbYn4o5cS9pCQC98HWkzkuWVXe3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
لیست‌نهایی تیم‌ملی برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/90056" target="_blank">📅 00:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAdfC2PPvWvf8kDxVq5lJVWm2LJgo1wZfwOLxJFESedMJOOKBTP9ZOyV2RdYWFW77XhQ1ePOz_ztfL6LWn_yAGZOcA8ql6JcSD8KDf_IFf79-vpSQU5kR6AQmB4aWHmCgLjH7PfmCN_jE6Pj_WFsZm2Cb9BQaqbv1PJUbGM4W2X4rLI3LJo9m-K8z_aK0x7fZKV5oA3FKYYng3W_I0IEpoDm2E6BRvDJww2STs79zC1jszbgMBNvRbvmnSzfBi4OlrVq0jpuWcaezp1nZgQsssW8Gp4iDO1GV5w4nPBT83AxODb89LTKUc7KYnR_jstao8z7l21KYfAbax67WI5gOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/90055" target="_blank">📅 00:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=kYBMFHRjnVdlYlUzZ6ynvpOS4OV4Icjmvc1BlaCp4ykhN8zzdGthTMf1t997flkaSsrc36-ga4N60i_z-agtZJ24tz6M8wFVwU95KPHeKIwwbDbwujVLESYBimc6MJ0Gbpx1Vrm6f9XjW2ar6bE3uZl0GIIlkAcpsnGsVECbTszLhizN2skjlRY0VLBqFiYASh07gYciVPmpFPlV3OThn1N9fSxyTRhgCxGSg9vNjKjRsZosKrXBdtmkKZeuVQiMso_5nMSwr9pG3aG3XZ7FksvJsPPo-pBI3c_ULbiUsUCEedaaFsHc4zsYF4i8hxv0GNUuxuB9Uv1FvDDlXZ_ntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=kYBMFHRjnVdlYlUzZ6ynvpOS4OV4Icjmvc1BlaCp4ykhN8zzdGthTMf1t997flkaSsrc36-ga4N60i_z-agtZJ24tz6M8wFVwU95KPHeKIwwbDbwujVLESYBimc6MJ0Gbpx1Vrm6f9XjW2ar6bE3uZl0GIIlkAcpsnGsVECbTszLhizN2skjlRY0VLBqFiYASh07gYciVPmpFPlV3OThn1N9fSxyTRhgCxGSg9vNjKjRsZosKrXBdtmkKZeuVQiMso_5nMSwr9pG3aG3XZ7FksvJsPPo-pBI3c_ULbiUsUCEedaaFsHc4zsYF4i8hxv0GNUuxuB9Uv1FvDDlXZ_ntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙂
شکار لحظه‌ای صداوسیما از بازی امشب آرسنال که با برتری یک‌گله این تیم همراه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/90054" target="_blank">📅 00:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F89ixMBuBOboBDKpx22HQaAYboPpJIVuCNf_COppaHUF1bFFGxWpo0CSxvFzw7ukRO6QJBnumtpd7Lova1hZrjxxFvZA5DRkSVBIPv6alC5REt9B6tC9CZAgvuH-78EEOdD_-XHhKIkyRXJJNAB4F5fjjK__iZcC0hHTvrAzsPflIc_JXs4FomDOREJ9Hy0wDrEGxHsk6XX9F1sYL05jMHwPZKAagCOjrSfv0daa0ICS-FFvbaa1ehQTWcuC1T_Z-c7LmudV2trz0ZB_k4aZnRJwrUXGYRdfiPEeIJ6gRDyWDTG-PamSQYkzgElCMu_7TAClpFNWlqLBrnrveiLFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/90053" target="_blank">📅 00:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🔵
🟡
🔴
با اعلام سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/90052" target="_blank">📅 23:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
لیست‌نهایی تیم‌ملی برزیل تا دقایقی دیگه توسط آنجلوتی در نشست خبری اعلام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90051" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90048">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90048" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90047">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkCvBIdKIfb5EeSO48jvekfxuZimu4qB9izNwV9oeG4waxfddIjLBWzaNt8ASn52WNujotRP292VgMzSI0_MYQ7R5Q547DwDMWd9Uj5S-0wUE6mMKRfin7-a7vit6WWTYSPFQ3ojio-xoIxVBufAamDQ0L1aMgmXpogYUc12gpPIinZdYDrtew55temcxC8X_9BSNlvKKc8zJKYfa3MIQAHXaT4BulI0ZnaXITBnV4FbYBBi_X0hoQQtmJsMAD6kkkRjb6DKLVZxXeO7hHm2rk12yRyLfRu2Xxq7uXLiVfySHI9cPQQIJo2P414TBZ9LaRLQZ3cBYwidLTM5dmYRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90047" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90046">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇺🇸
‼️
فوری از ترامپ: امیر قطر، ولیعهد عربستان و رئیس جمهور امارات از من خواستند که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی را که قرار بود فردا انجام شود متوقف کنیم، زیرا اکنون مذاکرات جدی در جریان است و بنظر آنها، بعنوان رهبران بزرگ و متحدان، یک توافق حاصل خواهد شد که برای آمریکا و تمام کشورهای خاورمیانه قابل قبول خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/90046" target="_blank">📅 22:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90045">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=lU1QdJbjPnTfIw3SqdRGSk8AZQPya7ezhJTUWmml78ZlWamMwxMQS3T9VxzIqoQXlxQhnwaVCkvIcVSMetlIYLBe9ce6ZsCLKDi7EWB7miuR22r6NZpEYiQ3ov7zemM96L3WByrh8ByTyHMZm0Jm_lkwAc4dLi7M6e4S4V3H2bQi8xwyWAGtlI00z81PQp0fP4-gpqyy_Mz9JDfDMVdtFytxAYSQ2_-GEErHMbKLafD-9pC22mo_T6BNnZXVeD0oW_esHPK74mLKLKLrhCrQTgR5NFXvkA89ZxlrfoZLOp7Qiva0ObQU7i-JS7RWC7Ygg1LpRhRF-GeoqYpVIudI4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=lU1QdJbjPnTfIw3SqdRGSk8AZQPya7ezhJTUWmml78ZlWamMwxMQS3T9VxzIqoQXlxQhnwaVCkvIcVSMetlIYLBe9ce6ZsCLKDi7EWB7miuR22r6NZpEYiQ3ov7zemM96L3WByrh8ByTyHMZm0Jm_lkwAc4dLi7M6e4S4V3H2bQi8xwyWAGtlI00z81PQp0fP4-gpqyy_Mz9JDfDMVdtFytxAYSQ2_-GEErHMbKLafD-9pC22mo_T6BNnZXVeD0oW_esHPK74mLKLKLrhCrQTgR5NFXvkA89ZxlrfoZLOp7Qiva0ObQU7i-JS7RWC7Ygg1LpRhRF-GeoqYpVIudI4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
لحظات احساسی لواندوفسکی در رختکن بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90045" target="_blank">📅 20:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90044">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4bBgCYFlCY66OdloVjS6nQ0kwsvQME27mEmXkOl_1EcLyJVbqmynfnXr0II5-sNtWnAyjNg3x2rsTmqkbQQM4VW1Nj-yZYQ-NUIRgBxbcgJsLwitAVibMO6VqizNhlh43ZtKx5YT6BtdXhQTStYgYgF_gtYS2opwtkfpa9oyt1txiNZ7Kn_VlyNE2EqgQwatwn9Imbn-QcIaw6xqzy20k5rDX5dtVmh4ZQk7U9k0k4YDM39IYhSqYvyFU7YEPkjV07AcvsUdaXbJ8Nc3N8OBkPLmEeQ7er3PH5b0p-hMQVW89bwgKSFOfrOdPo3j1GtWbElhHD5LdTrr-CIY2VmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
عملکرد ژوزه مورینیو در رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/90044" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90043">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/Futball180TV/90043" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90042">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF5G-2XufsB0Y0L9MRhrFxtsIRjigHuH5XraHHlfY2NRhoZSbzaN82oxtLbMzDfn43VzAdeRoxdJsFNIBNqHCHK7hIUcL9WdRHoYNasdet26Jm0q34BT1JueImIGLI5Rmrh6ysMiWyYBIq9ge-JzDL0URHM4awNxACUS2AbiN5Gd9cmphynJI4is0XwnDZuEUTRTn7mcX0iXVreYz8S4QgpCyWGNjakLz1olq2-kxWvDxTq4Uul08kauXKYmdFaVZF8qrZe3bTtU27iXtQ-fGWq5e63jpaQSi3vk4_GCCihajFOAcfHU7C5sFcydQA0JdOoIZMwcoM3RCC4Qy4rG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/90042" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90041">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dg3rVFyJMCiJi_9cvLK4Bvd9kRlGfunC6xqr8QG7gtiVAurK5c69e7MMbuYjKzgrSuerkiUHTUXfr6OsyCwFuqjvCDq7jcxUt6SAu6YmumpKwrcU23LApk4Bvjs8M-vQT3nHmxyNmD-n-3HFvEogEN-D2eAl-I8U5WQOVxccOeF5ggSDfLep8H0dUHCjr0fgOFHlrkXh0qyD_s1GAh32_p3gc8RWjpSZu7qKRfaNZpo-2lwZDIgT4QgHwsUUw86AKeja6u4vHPl6gLdVByAknjjh9xdrs2kNPhONx44b8qIbFyz-ZJavtpIzcMBrYN8zv3xQqdTrK0ZnpQxurARD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی که تا الان سهمیه حضور در فاز لیگی لیگ قهرمانان اروپا 27-2026 را کسب کرده‌اند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/90041" target="_blank">📅 19:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90040">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HPGOiZzgWcP_V5OFDTD-WD76b0R9scXVH18h2FABJS6EmATeLHQzMnO830_iCHX_wj89DdEH9MtuLsIZ4covm7EDS-GZ8cmPBcO21g6L7ui7OnE5cyl6laeHE77pHfdIKwjQhuUNmu-_NS00Xqs34DfLYCVcl3fw5vkKpbR3BYQEz_7uxXtL5Ij8_QSVLJndW0UMwwznAqtQTvtZhdkuEploStq25QFvJaEljPENB_Rs-91-tuR3W2b7kvtEx_SE140G_eZDLt1tV7iP0llbL4ympi5phBfigKsgQKTwhsC21Ss2WDSuIN0rEBHjS53wjoATUGZzrY_ZmGPO3nLvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/90040" target="_blank">📅 19:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90039">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmKbf9k90B688oOMXpYsjzyw9KtqnSiT4ZmNLqANQenrls8HbU50ZBgJCwjWSJ4LO8Ax4yc7lF8GOtZnlbU2JttMD6S4PZJAfx8AqYKXFKl8ROGMA13Zy4guIEjkddat7DNKBvgDaHQd8k4EP97uCAc3MrksYJbT_fpLNIM081qeGRPr7kZ0-EhZdU2NPAk1lbzio2o4k2zqa6_CEUxXeWmFvd0oa_yplCdO_o-sAYCAW1dMOEQZWo1DoL1CHf1DKSbNqnaag3kkaKkslo21x3_hY9_OgYDQVTipV5H1s99lVYrelPRgR0GMJyhfRLT5TvF8RD9WHmj8ymX-2fUC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
لیست تیم ملی کرواسی برای جام جهانی 2026 و پنجمین حضور متوالی لوکا مودریچ در جام های جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/Futball180TV/90039" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90038">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEQnhXAdEnq6xhFQK4NCYd4Our1nIm_z-cVMff9cUMIBmOqEFxnhFyCB5nWNXs1-MBQNMwTHGcKqpIC1_xRt3V2BWu9BY2stW6Lm4akmss0FvaeLokVU2T8liF2ubaeK9VuRF7zfb80ykkgUdpMoq8HE3jD_n1v-UTiD0FT0lhWuwLVpMUEC4t_udIDAVkgOHag-P8gQUkPCutd-JpjwtEaoVhzaFHjAW8V2Ciw-spQ3Ag93l1-Q8oimwFOIReB1N5pzYA-x3cQasi1vi6lYjifT1omWCS4-RLuQPEQUdB95kIJ2aUXlAE-vXDZxSqB8gAEhi3yY_iltvF91_yRPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسمی: هانسی فلیک تا ۲۰۲۸ تمدید کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/90038" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90037">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fNgh_Gh4EqF7ICcDJiJt5g8_sw-Xe0tnJ2uYajZH7IO_QK7IRKySQeP2V2lMjobNTHH89hhBqy3a7t27XPbtjJHUZ1vGMZXeUlvAvnXWoiujKRQVSLeZbodTcCsjwX5eaxkGTiCi9WOdHsiM0H7hXYEQ7gOeKP50YpPJPsOaghS_w6acp0aH-MLMgdZbcfyDIoMZXDBu_XhLkqr8h2W8p382C7yZeJTmYVW7Yq9cT-DGbPbKXJhHZeZKX1NqTAZ_kjFf4SNpMJdJz9Bj8OEFf1s10oKjilSG9VystudJakT-ek2gthEza1etINHw6sC7cLGVvgV3Ii2stg21DoUubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسمی: کارواخال از رئال مادرید خداحافظی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/Futball180TV/90037" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90036">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH2BcV_zBcrn4tffahoocsN3zV4FzBYZO3WdDFzQNIjUNtjCrjQs_SCOsiJ5FW7qOijSXMoA_oYg2Cggp2vcBfJWK3RzFl8dytBMLUPqoFRWsWiQasgY8o0Rv0AyEvi6LAj71tcfOoZf5ZuA-Z0IHjmXIUpHx6HzpNTiOgAkD_Jv6gVYmdkIvb7MNh7GBbUXrj-sHHesH8BQpG7Lmv49_W4ZABYZgMJ16XoCNsyKQoDHgONhTod9GdaSYtBQ8HJ1NRKp1UIuSPEI8FVGE4AeYUHupUkerz-dIlQqBQdnBIgko-wKneaqKNyrpcVRbIJwVwilYM0QKYW9vLeXnGWnAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدایای ویژه و شگفت انگیز چیتابت
🎁
۵ درصد شارژ اضافه قطعی
⚽️
بونوس خوش آمد گویی ورزشی تا ۳۰۰ درصد
💹
صدرصد پاداش خوش آمد گویی انفجار و کراش
✅
ورود به سایت و دریافت هدایای ویژه
📱
@cheetabet</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/90036" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90035">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7mHH13BQYJoEvez3JFYCqmUDxx7lZKm3eSRuwNahyfyyjupLegwDDWRdFx5qzmldnmEQDtcQ-Z0IK-7I1eVei9oMJDKcvHO4W3t_5c3fthBzNhIKjNnRp7vgV9EH5qQgyuOJLaSQaY9SWR3FEFMHloYtkmvXxUAy6mkEkZuJ2QsjVyw5wcjWJIeQ8v5Sz6AXmnrRxU5rwGDWUtGcLQLn-biKOqPpHYACSew-PaweJn-uGhktqdb9ApIUD77PJTlYe7iPt1hAKvWriz6KxQOX1qLAyOtgQy1XikarMXxu6VcYe7ZPgb7DuQw-ToL7PB4yjwnxMxucNuX0Cg1cw61ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکوردداران بیشترین بازی در تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/90035" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90034">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=Rzl3SptMlExTVxoHrWStsE9w9Wic0o2JhBrwsXn16DFHy0vCG-4_w5QR1S755fV1xx3yTrhDOtHNTwV53nhC9LJt1yNulK761BL5JtzAFiMOm5djThpeNuSmUPQE9ZZ96P25bbyujasGP67N_usREJLxm7p5y5wVC0uNaYijy_yFS4rGi9Y1kKrZYBBa4Uhw75bszgpLy4qFJbu-5Uj0LCRsbp0MBSFihdGjSVtdWTO13X7JHDGfernWHO0C-f6khGdfcXn5gKx-09LrqEGI2c0rlWiFrLULQ3Oc6UmISgbJf_jzsBBqhVmC0jTXvW3fbWimIARHBVaKhB2VyX4lTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=Rzl3SptMlExTVxoHrWStsE9w9Wic0o2JhBrwsXn16DFHy0vCG-4_w5QR1S755fV1xx3yTrhDOtHNTwV53nhC9LJt1yNulK761BL5JtzAFiMOm5djThpeNuSmUPQE9ZZ96P25bbyujasGP67N_usREJLxm7p5y5wVC0uNaYijy_yFS4rGi9Y1kKrZYBBa4Uhw75bszgpLy4qFJbu-5Uj0LCRsbp0MBSFihdGjSVtdWTO13X7JHDGfernWHO0C-f6khGdfcXn5gKx-09LrqEGI2c0rlWiFrLULQ3Oc6UmISgbJf_jzsBBqhVmC0jTXvW3fbWimIARHBVaKhB2VyX4lTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
📍
Tehran
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/90034" target="_blank">📅 13:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90033">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCzblIfLBw9kvrsd9I2J8eiIZg2iwd2DSsZ4bQkGxKnkIG_-PCsZobpodWKp9BF51Bskdwpw_8bnm_5qI2zmGr7CES3KCppeeiadyk1zkRJfIbnB9rWb-U6HvxVefNd8y-I5wiNXYlPf_nHs995XLZJ5_q2H0t-XmLIffBhswkKiFYOw6bOVVICYXoV4OHOrjRLeNNPe8Ct8Xq1_CRhs0gRxyG21IVdO1TJSTEewJcS-gv9wPnJkbOdbSEg894N_m46aYvHoEz_aeO4SMkMznRV3F31t7boDOJ4NQLmF_n_wyXUonixA7kJEADEEFrkkYye8vwsOHLAIXjgFPB_mlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
روبرت لواندوفسکی بعد از آخرین مسابقه‌ خود در ورزشگاه نیوکمپ، عکس نمادین اینیستا را بازسازی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/Futball180TV/90033" target="_blank">📅 13:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90032">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/90032" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90031">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiQcjT1f5Xxo8w-X58gT7Acwwyl1qjKd87UD9Vfi2165DjWiKN_EsggI-608AeFSqGEp49wTNopQg5ZtOihhMTboQ55Z9_C59u2BQftnioTaCiv3wA03vsSKnexWDspn1vZBqoQX7jDW3YzJMDjb5BbdUwOADQJPAApICZUqeIgMaM1UvzweeiDFeOTepednfc3bZ8KPSFx19dtBRgBxl7lddOx5_-U7GcdB4aezu-ydk6_rF6X7Fdx5pAUjSubUq0sViz8ZQfncZZCrceRL4itGekRzsRCCL8eJ5oUZunbXJMk56uDrb1lMJEJNkGBs0Uf1tTXj3geEXy0RoSNPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/Futball180TV/90031" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90030">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=ESotvFWV7VprpywTsIZZz1SLEUQTNUHrsLHejVO4UGpVC6JqcTmjS_jx9wPHJtGKv5a4CP2qFduCgDd5UdOddt2X5M0IPsmtAgwRsKkg1UWluqoJpwv_Hngz25XiacJlzY461qyNTy1HSIfe-lA4NdWReRSdN1ThNw23LaeyGTraLCTMdwBlPm3JaqUYqiE1PHiCpTSU92SDnPXKqnF00P0NpSwtD4jJFS2U3ABCFc1fxVjXv7-Fvxif03R-W6190tGLhaYNmXb8OkEjXHnkJdk-J6m4VKwU3Juez3i_qHkdvrjejpXwvVlZQncm76NzRbRSX8xqqSHsmPREaCV0wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=ESotvFWV7VprpywTsIZZz1SLEUQTNUHrsLHejVO4UGpVC6JqcTmjS_jx9wPHJtGKv5a4CP2qFduCgDd5UdOddt2X5M0IPsmtAgwRsKkg1UWluqoJpwv_Hngz25XiacJlzY461qyNTy1HSIfe-lA4NdWReRSdN1ThNw23LaeyGTraLCTMdwBlPm3JaqUYqiE1PHiCpTSU92SDnPXKqnF00P0NpSwtD4jJFS2U3ABCFc1fxVjXv7-Fvxif03R-W6190tGLhaYNmXb8OkEjXHnkJdk-J6m4VKwU3Juez3i_qHkdvrjejpXwvVlZQncm76NzRbRSX8xqqSHsmPREaCV0wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استایل متفاوت جورجینا، همسر کریستیانو رونالدو، با موهای بلوند شده، در مهمانی جشنواره فیلم کن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/90030" target="_blank">📅 11:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90029">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoMf-hSomyMRIxsQN1ckiZ2BlAAoXQFW8aQxSQGURBx3m1-NeCbdwhd8zZCS7KFvsvADb1gaBM4io2eAHx8nMdGA_UPR3UaxHo71drROGkjfd9lzu5ezvj1hcadNCe9Wc9cRtTQgalo7VGkRctmSzaUbVMCzf9HufcSwKjCaDv4nSiVFkQKDxEif9cMbhH-2CgvxJbQwhro4VrzIIz9kaxgHj8-IceE4jCactJHr6AoDGTXMfoh30Tbwpq40vkjL2IithgqLuF_hx4EDQrSjy8DwP2uui6X9Rxa-3EkKS_s3twRKh0Fl9JUT6gU1sA6mrVLaKy7cHXdw3rJvLX8Qpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت تورنمنت‌های رونالدو با النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/90029" target="_blank">📅 09:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90028">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441c980280.mp4?token=Naxj6oXh80lmPp-ozFiv3C79z_h5Nf7X5wqU6QHgPOJXXjFg1cCxeAQl0duQbNHqNi4x6lgaEmtN-yP4alhuwgN4iwyfyFB6OupgrAqGIFufJaTgfDBfWgSgZKEeW15wTEq13b1oxwgumu9LvT81nhHbyaxe7FNH9OMxzb9ZTr26Bja2OoM_8vwoQz9HXpBKFh3AcRKgqcJQv8R_MGgHtVhfEr9937UBldRmjtIZavJhwVdOQEj_W1HrVSFqP1vRMoU49aElvcp-L4lSgNkAkFtbQjXWZTrNflvSOnmQulQQHbaiwSLoAoIDFn6pjPFQxW_JufBPTYhi0739bfmDFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441c980280.mp4?token=Naxj6oXh80lmPp-ozFiv3C79z_h5Nf7X5wqU6QHgPOJXXjFg1cCxeAQl0duQbNHqNi4x6lgaEmtN-yP4alhuwgN4iwyfyFB6OupgrAqGIFufJaTgfDBfWgSgZKEeW15wTEq13b1oxwgumu9LvT81nhHbyaxe7FNH9OMxzb9ZTr26Bja2OoM_8vwoQz9HXpBKFh3AcRKgqcJQv8R_MGgHtVhfEr9937UBldRmjtIZavJhwVdOQEj_W1HrVSFqP1vRMoU49aElvcp-L4lSgNkAkFtbQjXWZTrNflvSOnmQulQQHbaiwSLoAoIDFn6pjPFQxW_JufBPTYhi0739bfmDFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
جادوگری بامداد امروز لیونل‌مسی در آمریکا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/90028" target="_blank">📅 07:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90025">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfPLwOn7uPAMmUgz8vhYp1AcA7S1HWzwzSscgTMIotbAHKj2vCYm7zrSBve1lAyEhyPugNCoWbtK_y2iDDYm8nySF0kzzrzBWMZx1Vtc2TWWI684hP0EeWWyi45rufJ7IvcEetAJC3vMOXnqEuc318HgMl86_woMtiXK_adOtGtuIYpFGMtXETq0V4g57-AGFmMC9BkWAIg42SzM-ovqgXobzOHNWdJ3wiAtcG6yrHp-WrvLkRtbWRCjFwtwbuIwndQuAUAFm67QZIQL-5R_pJVb-3ZpVKCQz-D7U6TLNQf--6G0CHXenr6jUmob-C_KaAowYlAUL8B6byQ4bTrGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫪🫪🫪
🤯
برای فهم‌اینکه لیونل‌مسی چه اعجوبه‌ای هست کافیه بدونید که این بازیکن سال ۲۰۱۲ موفق به زدن ۹۱ گل شد و تیم وحشی هانسی‌فلیک پس از ۳۶ بازی لالیگا این فصل موفق به ثبت ۹۱ گل شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90025" target="_blank">📅 19:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=KwXFc1KNMNFDJqSH71aHgV7Wo6QEVF4--DyEOHpRJDyDR4GE9LCYN7PyoR-GxS_aIYuAnM6p8cPSCyzWAewtkLWl3CdqQHnu9izmphzw4tWbBXMIRNUaAux6c2ktF9nCrt0VpIoUcIHw7LJH5tpo7YNIABibcRhXIOG_X65waDDjB-Vl0wRC-O0mBCTYOkm4NGqIUtbim_mKEdnt3zjM9agz81LjbmgllJ70mJZLEyV5e_cRwJY6bGH-kuBNCrQeoiaBS_0LZyRz-_4NlTAf1j98f0Zqc6vx3A0JMPoiSUBAdktVRhBMJE6_-hVc299KiYbK3VUsYM9POVL2v0_WmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=KwXFc1KNMNFDJqSH71aHgV7Wo6QEVF4--DyEOHpRJDyDR4GE9LCYN7PyoR-GxS_aIYuAnM6p8cPSCyzWAewtkLWl3CdqQHnu9izmphzw4tWbBXMIRNUaAux6c2ktF9nCrt0VpIoUcIHw7LJH5tpo7YNIABibcRhXIOG_X65waDDjB-Vl0wRC-O0mBCTYOkm4NGqIUtbim_mKEdnt3zjM9agz81LjbmgllJ70mJZLEyV5e_cRwJY6bGH-kuBNCrQeoiaBS_0LZyRz-_4NlTAf1j98f0Zqc6vx3A0JMPoiSUBAdktVRhBMJE6_-hVc299KiYbK3VUsYM9POVL2v0_WmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👋🏻
پایان عصر کاسمیرو در منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90024" target="_blank">📅 17:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90023">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=vbLr_IF-GjYPMr8foqA_GzkeO0TTB1jN0SBJoGya6XT-oArdZ2MIhrwCN4rEmnl054K5hllLKYJPLJ3bSaX36eSbvI_2Chy8sggYT94K7B8-MprcSnsNGG3h1hbMK5fmCWztlZzAwnfHTX0YDOvnOhv5zhRtDxCrM3UefB13s9l31N59NlU3BXLVTkejKu0jCIfqEEbuYfO98i97ta_huMLsHBS4_apLq6RQB6JVxBBZdst3uaQD_FQ5DPWb3t_japeLAFHyz5FYPWtr9WegWwNRPlWgPjZR80QG9pxl2NwBAYYGol189UQR9AtYD5AFIATNBwRarEAJSumDyqqSEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=vbLr_IF-GjYPMr8foqA_GzkeO0TTB1jN0SBJoGya6XT-oArdZ2MIhrwCN4rEmnl054K5hllLKYJPLJ3bSaX36eSbvI_2Chy8sggYT94K7B8-MprcSnsNGG3h1hbMK5fmCWztlZzAwnfHTX0YDOvnOhv5zhRtDxCrM3UefB13s9l31N59NlU3BXLVTkejKu0jCIfqEEbuYfO98i97ta_huMLsHBS4_apLq6RQB6JVxBBZdst3uaQD_FQ5DPWb3t_japeLAFHyz5FYPWtr9WegWwNRPlWgPjZR80QG9pxl2NwBAYYGol189UQR9AtYD5AFIATNBwRarEAJSumDyqqSEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
لحظه شکسته شدن رکورد دوضرب دسته ۱۱۰+ کیلوگرم دنیا توسط علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/90023" target="_blank">📅 16:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90022">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
جزئیاتی از درخواست‌های آمریکا از
جمهوری اسلامی
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/90022" target="_blank">📅 12:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90021">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2UNFBll93kZzQfUcFyGASeMZTwgqxInAkAmgSM6prV7SIgc7-YXoy5i7UjhpEj2dYLJHJfpP6aiRO7BkfnnwwMaUMymgcqZS_3pMngm031vnlmsmPO3wtyI_5na7Z_A6SBCm-x026HG2CTidyGwMVdMzSzP-4gPP2r7U2Q2nvNtb4P6IIzEzSsF8JRl6LYskiA1XMx63YTfuo6eZcrY1zoRfW0uvTsYzzZ9-TMAiI45xBzeL4j4JV88JbfdeCCrenL4Zr20LchiZZvyev5NGFD-bPuOXoLF1QLh3n_R0SRJJVov27eBYWAHq3LV7fvDg_Cz-UvjLT-r10Fmtje7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل‌مسی از سال ۲۰۲۱ کسب ۱۱ جام
👤
کریس‌رونالدو از سال ۲۰۲۱ کسب ۲ جام
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90021" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/90018" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90017">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXdl7BfTiKXNaiEzOl-qu5GMAXAGf5tI1f-5hViXGYB5MUFGZc-9y9PS5zPMt2GAXiO-yTlAUYfY1jtzNM4k2bqoVPqX7jQ6GYLVqsk_SJUt3d8GcbSD5D9MVzJC2s5KPZlUw_HD1_ZKAkpqr7Orc4KNHF61SwQxDPAuL9PEC7e8pyA7uTAs1su6LRwoV2klelCw5V8EQhDF6nsnQ37Kn-Hrs0rIqSzaWe2KF0Ax2Xvmd9C0RBWBLBQsMOZ3IBjGIRp-UT5G1UfViwJRCkX8HbR1EA1ov7C_NGeEDjjGfs8wxeLZDqG2zYQ9izVEG6vZdLBOx2ndFOVRgWCGyekfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90017" target="_blank">📅 11:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90016">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bj9j5AEUxPBQTdnjCUOdU_uOADjAM_AN9LAqWr8llCgnKmPskXqm82gZhBOCQRj6nwA_cKQ4Kf4k-8lzhH7yoXaqtAssehGhKYtrDU_vh4GWK1Duc-EOGUETpyBkyj4wfEXMPOljQhx0vpCXUQgAccAjvkjg5244Y4DLjWXESGX6acLmObTxWSfvv9C4SvCayGr75StwsUSU2a1VCZX26Kxt-bt_f9L_wsirdFEVTFK5R6OnFmeSMYBhQpiffr3UOtHt_i7V1wFJUHlwE4q0gq8ZuvoMSAxEqBe-6y5A270D_dseijU5KgI9hw3fktcx9QnXZsMZ8Ow47NVpowRmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
#رسمی
؛ ژابی‌آلونسو با قراردادی چهارساله سرمربی تیم‌فوتبال چلسی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/90016" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90015">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
⚽️
تیم‌فوتبال البطائح به سرمربیگری فرهاد مجیدی در لیگ‌‌برتر امارات به لیگ‌دسته‌یک سقوط کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/90015" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90014">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=ITD46eRlBpFIQQ49j7WFiejH89Tb_nMMV9bjv0zLm9YQ0nJpcwW9Beaf83ULO-V2Sgsa1im9fCWcXBUeyf7cQSySUI63zkYDzKHCWZJka-e1QDpA7Cb8ySd5u5mAaZLP_aPplvec86xZSkSdRfVX0ckfQV45IwprLZTWBv02VIj3xqxJzkDOKaVANUTDKLNiedqryDm4OUL8t3tgvmWCqjK5__iv7US_9NRdckTksSjebJAipQxOSG6_RY_KW6BCxP2WF6LPNYgCNw-1Zi2ACW3_ISelMKk2DHc9a0O16y0hbDLirrMu0-ENZApY2lnQi5AZCMF7K54d2npipcKRew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=ITD46eRlBpFIQQ49j7WFiejH89Tb_nMMV9bjv0zLm9YQ0nJpcwW9Beaf83ULO-V2Sgsa1im9fCWcXBUeyf7cQSySUI63zkYDzKHCWZJka-e1QDpA7Cb8ySd5u5mAaZLP_aPplvec86xZSkSdRfVX0ckfQV45IwprLZTWBv02VIj3xqxJzkDOKaVANUTDKLNiedqryDm4OUL8t3tgvmWCqjK5__iv7US_9NRdckTksSjebJAipQxOSG6_RY_KW6BCxP2WF6LPNYgCNw-1Zi2ACW3_ISelMKk2DHc9a0O16y0hbDLirrMu0-ENZApY2lnQi5AZCMF7K54d2npipcKRew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/90014" target="_blank">📅 10:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90013">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TFqjiluR1HskxjY7zc7q4LhUgDx0yjSGbI94tM3urH-9ZN9MkOMsf0Sa1QAaY6bjAESakj4FhtNs27W5BhyY1xnFERglbzHWMWCgIXfarmyQRYnJrvg_-Cda5k6Jc8D7ff6mR67r6xdlLyM242MhdDAj4dttgWWTkTd_KFY4S9yxRB6r4iYU-ZhvW5wKQKQGf2EKacAayE6dB0-PEc2NtnhNiGGCpbze6QF0GnpG0If0xvuuK2H8u1A6T_6Grpg3roC5yXCNletoVtYitRPPlXsqhXm4w140Acz0HorSLteYb4U0nmYldfbIpgH2t3CSvqXwbv13n4mj0UrTWSBb5ms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TFqjiluR1HskxjY7zc7q4LhUgDx0yjSGbI94tM3urH-9ZN9MkOMsf0Sa1QAaY6bjAESakj4FhtNs27W5BhyY1xnFERglbzHWMWCgIXfarmyQRYnJrvg_-Cda5k6Jc8D7ff6mR67r6xdlLyM242MhdDAj4dttgWWTkTd_KFY4S9yxRB6r4iYU-ZhvW5wKQKQGf2EKacAayE6dB0-PEc2NtnhNiGGCpbze6QF0GnpG0If0xvuuK2H8u1A6T_6Grpg3roC5yXCNletoVtYitRPPlXsqhXm4w140Acz0HorSLteYb4U0nmYldfbIpgH2t3CSvqXwbv13n4mj0UrTWSBb5ms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد رونالدو در بازی دیشب النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90013" target="_blank">📅 09:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90012">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hw-Ban-C036LnUi_MakeMDdIn5Jw8jm6IjMVdVG4yqNmGiC9vpzR5ozo1DCcYLUB4FPPAHLC-EVEQUJLXJ74QHkT09YFfCxwmHCfyYk3UohnvKEktJz0AxPVTr7ilqg3R0kzxUG2rojYA3LXCEVht9K9_qQARCw8CeB-3Y8auXo9NECuC8Ev3O7cQ61h98M3FyqqAsCAoS6bSNF93q64I6qQrsMWmGYS3mFHiq_jxK1DkqH57Dyf_WmHjCNOz-q44Kfu9koPCRNotXFKSw85rPv9tBsGPiPf314yjBtzan0Ahv5rPOfA2QI4dMIw4A9OAWEwYIO-vxKahXe169hxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش رضا غندی‌پور به عدم دعوتش به اردو تیم ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90012" target="_blank">📅 09:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=Ptst1xj-ehpdZ_SGKFmuvBC-kEUY69F_AI4rSpqadObUdKe3Lq5W0BqsWEo7rMwgjgertUb55jBwOwoIvqkxO6zItaKNzR8rsgtFJgkOLLjbZd9vH2HAKgbYmR6Qc9uHc2Va2BT9urrs1MIn_nZAgwKEbgL16lRdwYjWxYzBBl6QPw2U4R3UdbCngudZwgE3LGlBzyRSDZI0jBNwNHiKHBUUrVuv_b0gVY0K890hkrEUli6MglveQW-UIPt9ygHWXpCPFQBhzL6D6Wqwt-BriCzs5icT_OtxJWs23mmZ3ghJQLXHBPohckkoaQ_Qiwvmu4QmCA5ZAQc_BCKNQ3guOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=Ptst1xj-ehpdZ_SGKFmuvBC-kEUY69F_AI4rSpqadObUdKe3Lq5W0BqsWEo7rMwgjgertUb55jBwOwoIvqkxO6zItaKNzR8rsgtFJgkOLLjbZd9vH2HAKgbYmR6Qc9uHc2Va2BT9urrs1MIn_nZAgwKEbgL16lRdwYjWxYzBBl6QPw2U4R3UdbCngudZwgE3LGlBzyRSDZI0jBNwNHiKHBUUrVuv_b0gVY0K890hkrEUli6MglveQW-UIPt9ygHWXpCPFQBhzL6D6Wqwt-BriCzs5icT_OtxJWs23mmZ3ghJQLXHBPohckkoaQ_Qiwvmu4QmCA5ZAQc_BCKNQ3guOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوضاع اصلا به نفع رونالدو پیش نمیره.
🙁
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90009" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90008">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNaVak-GiKMPQsnh-16heM7Hc7f04sCWO7RV3CR1747zLepvpZ1UtRC2gnqUB-i-PmIevV20Z25bWWiqaWR9H6yoAVvJUttip6M6P1tOfWrfdw8yYe4yH8mMZFME0L74Zg5ADjBY8iwt8FWhvsaDXxLyFd1020qq5alXCQQwuPHu82CWUP7v9V0ISrKq5gw-V9HGvRHYpCPemA7n8_iORxJ84-8qHnzPyIa0TlQGGpeyC6fT0Fj4BWwotRvlu-esTKrrtWi_BUXPIJkmVyoEOvhc0-jI1pkJEPrgMixa22VXVm04kpZiThLQRkK2WVvuGLowHxwKCF5S8Q5A0aPysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
توییت‌جدید ترامپ: آرامش قبل از توفان
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90008" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90007">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWu2zrWezZWg3k5AWSWHlr7YptagBOc9pbQBzCWj5OM9wx68Onw8Tx_I5hzFlIrSuZ5JWLXqfTKLbEDxT5Kqs0PJy6BpBve5HZYkxTxkITmQcVZju5l9KyLf2naGO1OBimxOuIlC28Q-3MGQG1pboqApVnNoXUvu-G2RFqAxkj22hr0nNbV4ovdAHm-Npsrf5Rfjet5O6mr5r7g61AoRjTeKcNkvUZVJmF3iT2Ek2J-TOCgUu8u7zZz9MNPnLrUefDS80dDSgud6lmXIqlZpvQZxkJrTwxh5rHeNltCSlZsbrBYbCG8nTfNS23lK2-4Qpexx_KoT3sp-_Z4BTWsqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
النصر در فینال لیگ‌قهرمانان سطح دو آسیا مقابل گامبا‌اوزاکا شکست خورد و رونالدو بازهم نتونست با این تیم قهرمان بشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/90007" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90006">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDSBVL8EnEIO_Mc5fUunoph66bPIiPKAT1nrd5yRMe0DhJ3eaY_eiJ_6oEylaDYpek9lM7_dOG4BCuyvfaMIOanIJH4fmwsOEpC9VeUDjHaXk0j_iPPubBn6GoE_B0CiqF7Bn2-5KymljUwgelRrHm1p9o-oUAeKQj-UHfadMw1qBSKsWyLGB-iEgbDb2RVwl9gXQehGVH5GhD0TTkQme9lXIrQFWGY6t4dgGIp957cYVpxrnatBzy8XVt8Ir8kF6RbSS0xPRsnvHUWnXnIjOOSUmJYsc0iJyZt2mqxLuxhvOD82OxAmXH-LF--cMTEbJdlu9-pxRG-vvCMDLzwfCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90006" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90005">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💥
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
سامان قدوس، روزبه چشمی، امیرمحمد رزاق نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قائدی، مهدی ترابی
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علیپور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90005" target="_blank">📅 21:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90004">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQe_1yKJ4fAL4vIeBNNZyEGiyPuAKO4OieoCzp0Mf8sIrpb2ex_aGJum8O4wrZUC8eOkh58qX9FG_Yn4-CDHB6O7bddCObBIMqGdmwMlkb6KvsJPMeqLktvgZlVIIxm7Dk-WnyPRcoENqtiD5U45QSs9SBgDH_8HwaFAnISyJB7p4ttYJzUn1FVaPDSGLuRk3WOE-GI-NsktiIx8IBQ2ln7CGlDQLmhmgf_Eigt8586lnqbM07mB-FF1fbOVXXUUiejFOKVvPaQVoddoFco8xTzbS1LJ6pnU0dNZQ6Zqmp-9MNrF5FuS33aGSbhmQMMxtIHAaaHwh7tkrV0ZcFmw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/90004" target="_blank">📅 20:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90003">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTRTIZ8eXuM0g39wU0rL6BqjK3JRZ0czbQpLOM7qPUWyblffnuNy4AdGb1-lfWNe4hB4ob0z4Dr-qMDXft2sX28Xggtes_lCd5fuZfjOl2gBNBiUnE4ZUoyFycfHC9EIkzSQ5SyGv4_vr-6qUDV7Q9lTHujWv57Tm0fCu3LhbDt0igRrtjLCsKBFGruVltERLU8PWiTpLjzdf4US05n1slFQzB0BXr4M_mxgxKHNukHAKZeAc-ILFGH4xjFZoNJLtz-g1VgsSTTaMd5BRxOgnFdvJSzQOPIQi6jX6Yxmz79p9DYdHhUjRk1I2S8JAF-xOriukyUYkVbgLAFFWMqyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پپ‌گواردیولا طی ۱۹ سال ۴۱ جام کسب کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/90003" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90002">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6uB_wh6tOPnnQdOjxP9uDgadmjUEEPcBKi9dFzk5DwF89-H3q_UA0ind0_W8Af88mVGz9hditkpn_Kas52BM14HuGYI-SxZE3e2EI_JcUsEvfiIMpiPkL_qImbYveM5eBGOnAUJdRrJyicZXCGTdCK7df0wP1Vofvzk2FQy51gV1TZf6GAwuoieFVZSzr4zquc_VPHkQ375APA2a7ouyAXlNQEo7PKfcuoKIA1S_m-ZGZZJsWo-68SWHFnzxxj_OoNVhA63t3nlnpXjA6d7oJbdjbpGRNhzLC51QXK5QY4M8GSnOANdywq6xFgjtuaGUv8eFjZNe0uLbHO7dhAKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منچسترسیتی با برتری مقابل چلسی قهرمان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/90002" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89999">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA4oCrvSo0WW2ddeo4sm_xNFzT-QTWTDdPgufd6i8jM2DUITRGJFzb4aZSimesbMR-O0EYZ905b0_Gz65-vEROMnkElbKyxGPb7RI6ydqmoK2d1FRoaxqgifUulRZMaeJVtgeOeggrma2K6kMqwA9ef08daKvK091KU1T-DuJHQ-qKgAKSP2AfiqOir8uqZwOm4cu2L71MVzmUstgh0ea_hr1SrGd_CHWrp_jeGofCHVufw7TIVPb-k96fLKLBNSgBR0v-PDHuzSZQjIk0nDaFSeNjIaGgfhdlv9ITLxrnEtiJS6ao-Z6WTQZf6we0INsSVaWVayE9aDwv0AaSD3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام‌حذفی انگلیس؛ ترکیب سیتی و چلسی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/89999" target="_blank">📅 16:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89998">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msB9ZpZ_SAzlFm94IsdMp9g2lTPpG2ApqH6LKOYaROQ8R0T8g-S2sX2J73au5PGOeNZlKFXSsLwviIwPpGjMyl6dygFg3Cn2QS9S1P150szK1Pa045mheeYvI85EiA83MfYPzIUfIugYdVbysrDdnADKFhEKkhFDFadSyQ_9tvYRtCUf_lbrVWcTZwmM77Jt_HIvhumd7f4qSMR6ioxKINJlztMQi84SsU3w7LZWiotcKhjkIHKN75dOmVDdu0uiZ80TM0CvMRSFK9cy7USbou19kJK6TBrc3Zp9R45CdMNoWBnEjLCm4uaw5DbIBQTjPPbVGOqIv664spzTnp-e8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
فهرست نهایی تیم‌ملی کنگو برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89998" target="_blank">📅 16:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89997">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKxEW4mfPmHItMzArMlT4vVSDlU54LSJvvOFE07tfEWjEKQQJvvVquDkQxDMuXB9BpHxMRCAcBYSXIFNOuWfqsXR5B67_WG1n3UBtJmbUO0obd-QsGDqv16WxfIfp5fbYfdcS53mWQNbC3MdoU4GmyqvQtlmZlpxALQ3uPQPRyNQFUip_xp0noTvi0zIMFXmse8cVg1fayA9jMEF_pA80fq1tvINWhWjTN-V9O3SueaxDwaWk4qXVMirclz-0betWEKHyaqO6r3oENSh1iIUNfvuiOLDjcAMv73aeL0MnN6uuC3phXH_1cI4occSlUERHo4CmL6ngMeMR5hMx7ZxRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پپ‌گواردیولا: فصل بعد نیز سرمربی سیتی هستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/89997" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89996">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=ZEz3jjfKGSxEZdFVrejjKBocWP9CFB5m0yZazUDnaBIwD7y7GzoCOKcPFlH8gG_zq2LHKRvowQzaAvdKGrT-o4J81gXE-ckRUp-dGhTuPHmdXsjh7S48HbRT19ff9aihUz9pX0xSru15jlIDNawqkdIBECQjIR1aOinXj2yZR-l1NRYK2qnhg3C7pic17wOdXkHfKZhj2m-ubXhS_ekM0ACXNyryOIAlMHs2xCGUzCgstsB00gj0T9YRmWUBs77rqrkidQPCKWCydVRkcaX4P8TqOErDeZ04wpVYfV9cW-MhpMCG1P14DKejF0zvTaKRYy99haZ-RAlUnnjmvw88zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=ZEz3jjfKGSxEZdFVrejjKBocWP9CFB5m0yZazUDnaBIwD7y7GzoCOKcPFlH8gG_zq2LHKRvowQzaAvdKGrT-o4J81gXE-ckRUp-dGhTuPHmdXsjh7S48HbRT19ff9aihUz9pX0xSru15jlIDNawqkdIBECQjIR1aOinXj2yZR-l1NRYK2qnhg3C7pic17wOdXkHfKZhj2m-ubXhS_ekM0ACXNyryOIAlMHs2xCGUzCgstsB00gj0T9YRmWUBs77rqrkidQPCKWCydVRkcaX4P8TqOErDeZ04wpVYfV9cW-MhpMCG1P14DKejF0zvTaKRYy99haZ-RAlUnnjmvw88zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📲
پست جدید لواندوفسکی:
بعد از چهار سال چالش‌برانگیز و سخت، وقت رفتنه. من با این احساس اینجا را ترک می‌کنم که ماموریتم کامل شده. چهار فصل و سه عنوان قهرمانی!
هرگز عشقی را که از همان روزهای اول از هواداران دریافت کردم فراموش نخواهم کرد. کاتالونیا خانه من است.
از همه کسانی که در این چهار سال فوق‌العاده ملاقات کردم متشکرم. یک تشکر ویژه از رئیس لاپورتا برای اینکه به من فرصت تجربه باورنکردنی‌ترین فصل دوران حرفه‌ای‌ام را داد.
بارسلونا به جایی که به آن تعلق دارد، برگشته است. ویسکا بارسا. ویسکا کاتالونیا
💙
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/89996" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89995">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKwHkka9AgeyjrWgQE10MvqbKXqPhjv6v0ShJfBb6O_I66WX17tDY_wH05gpKenfO4oyld4NYVp2gNzU-wccSN8WkOK49l0FCcvzaO6wHS6pM4QZya8ivUHaCK5DO-GSNUP3B-M6aavTcSF4_X2iOGdO7poNMkeF6gzPl1kWTPouhdWAKiv7-o-Or8kDJxZw702XJuMZd4MfPk7V39xGWE3FsVyAaoPKcyX4TQsJmLunMD55DVUN26H2eiw1MzLspYdEDgHDGP7WBCmcILsrHCo_sIc3YMy0feFSiw6VAitrYTqjZ7ad9mwcFdbnubEA1Y_jjioeCzX7UcMVcBzrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نت‌بلاکس اعلام کرد خاموشی دیجیتال در ایران وارد دوازدهمین هفته خود شده و اکنون به هفتاد و هشتمین روز رسیده است که در سطح جهانی بی‌سابقه به حساب می‌آید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89995" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89992">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1aBVLfmAcyyyQBhjNEfE6uIobhkzpCNwqacpBSTzf0jRLtPeGBtmb_XHKhHMnz1T3_aDDaloA9cnW99P76EcB8Pg91a0LCwnv3Pu4urRsDdE9gVWd0wd5epkB6jMqYJO1Ybc8uFz-SQLnuNYL4Ih4Dmi8KeBL0kq6X1axxL7XyaDCHG28hLxIQO4tujI6Y5fJenbhjNA3v1L58uBE92J-kTozC1yJGuUU8MyWGaGP8GBrttBPmmdptJ7lN8RUOYcUaQ-hINj4EywL7Vfy0jMGEc_2n24MM4MfoPNAAbih1oWySAkwfS6OADWT7lhc3BUCUNu16bfmP_U_bt9Jn5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
تا اواسط هفته‌جاری انتقال ژوزه مورینیو به رئال‌مادرید رسمی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89992" target="_blank">📅 12:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89991">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=q2xjQ-loI5wLVFYPfkReqRdHMM4mYtbTlgfYDYJb-iUyeX4Dbx3mJIzTkYYkrTTExmfWiGtFmBuEN_WJMEYd45gx_CqjL3FyrZF-MwRp-ili9Akj2G1fv7aHq_Pjc1uU0ai__RuW9T2Gcm6nR1ziJXjLyPr8vIGWgYE0uQkqScOYiRMb_42QzhF9wbqoaCkanuxla6zOfrQxnFKv5nDe32XXFGaiWxNWYOBFZpIlSam3oSRNTRdE_u-7N793wDTfKRmSJrQbLzVD91PhvOwYpRkq8ujiydC_ngbFZYJCBVY4CrJfyFxRYNT8_CTFKpj9mOTHNghvAc2y1vTmG6aFZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=q2xjQ-loI5wLVFYPfkReqRdHMM4mYtbTlgfYDYJb-iUyeX4Dbx3mJIzTkYYkrTTExmfWiGtFmBuEN_WJMEYd45gx_CqjL3FyrZF-MwRp-ili9Akj2G1fv7aHq_Pjc1uU0ai__RuW9T2Gcm6nR1ziJXjLyPr8vIGWgYE0uQkqScOYiRMb_42QzhF9wbqoaCkanuxla6zOfrQxnFKv5nDe32XXFGaiWxNWYOBFZpIlSam3oSRNTRdE_u-7N793wDTfKRmSJrQbLzVD91PhvOwYpRkq8ujiydC_ngbFZYJCBVY4CrJfyFxRYNT8_CTFKpj9mOTHNghvAc2y1vTmG6aFZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آموزش‌مسلح کردن اسلحه و شلیک در آنتن‌زنده!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/89991" target="_blank">📅 12:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89990">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXTr94oGN-s-2dXCl5tN_rMz6ao7zOa47CWuF2qy9BTrxl1qPq0_NXsBoJS6VoDdWqSjvspo6UrvpifvaceCLekDvcLBUu8PpoGNf78Kws831wOnRY8iyfJJb3tro0lOe1PZ_IEDrJ5Pw3B7ueQllhFK9SxB4US593elSSSCK7UX4m3fXrLN7sRbb7upzkvKIDns4ENcfyZyOZaK07fSTyIfzEIUi-ZHgfW9OJhtZRE_iTMB9UE6Fp_VNndWhD6uRNNOnIiPOwFntmOLBW04H-KvyqUg1DC8bMzyXrA_PVWTzlR9WxsMWVxhb9yabUInbPOnFZ7nEaItkPBA6hzhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هانسی‌فلیک با ماندن رشفورد موافقت کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/89990" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89989">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWuYSfMgoMeHV9GPXLsqfhp8JOdw6lKQbOlZr6WaCGmMAHcdwcQmza3p2y7DB_PCnh--bbbGcrtwkwVZ6V5LPdSdhOtlJ2AziV2LPRj_vlq-Tt_ZmBsWBqDN0k_7mrpkpuVBkByZPt5RAVmtp9jKyKB9jjRCpsdbb8LoDiQ_R3jHDzKz1UdrDpdUuDlV0grcodXt8FMJUbXgp3Rg-iDX_LVrGQZ6OnfRPyzXTbSpcHzxSwJbvnuX8YCyMDJ8dsa6MNnd8103C1xbeFUrBYSz9tyEWP7F1HqM9pWG_iykWw8de0vJ8GwPIgS5GHkheDbAlbzCTJ2-RT2yHdxli-W18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
لیست کره‌جنوبی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/89989" target="_blank">📅 11:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvliiDf5ms242bM4JV1NXkk-W-ADuTqz-u6Ow8yiYtjwCzdJX-S-OyXgDzHvDKndwAszKu9ZgPaHGbPPMO6VoR21o5AnLKS_N62qj-V0Nw-ggYlgEgaY5vOpFD-kvOhi_Otwnsrq0ze6DPuYbMgK4wYKLIitSa53wvrERu3HXzie5i4GKJ2AYkxO6uXlJIPC4w3hgqCZS7CfzP9dBsYywJ-waMklWJIkhabKalDz8LCGv8lC7eMMAl0FCs9EglwNjfj-PfogSZF-a4em7CwtVraez3PQbsPG1XLCNq5iIi_UzoT7cnw9iOqTnPp47RRrajRnpxl1WYPBGoBA-5kTTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شدهش رو به آمریکا منتقل کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89988" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فوت پدرم باعث شد از آلمان برگردم/ کخ سخت‌ترین دوره فوتبالم را رقم زد
مهدی پاشازاده، پیشکسوت باشگاه استقلال: در اوج بودم اما به دلیل مصدومیت‌های پیاپی‌ای که داشتم، وقتی خواستم به استقلال برگردم، آقای کُخ گفت که باید تست بدهی و این برایم خیلی سخت بود.
به ترکیب استقلال برگشتم اما دوباره با دو بار پارگی رباط صلیبی لژیونر شدم.
کخ مربی بادانشی بود اما اطرافیانش خوب چیده نشده بودند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/89987" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzK8OrY0CkKnkoXqZxbfcsh2jUWbsBLU3KENf_NEQ4KAeBK2bsmu-JxenUWtgaZwRnHsoExlQi2MowRjOiopJVwO_v0fadjCZsNR2TYwmnMZWIsL-5YMTTXKohkxXrXV4v5KlSI19TBwZLU9kNv1AIQ7kGq9LIm-vX8q4btMBPA3QVdBDlna5J-CTPRrp_iLCsGaxSYGvYgplNJDR6q74XJWcB10C3hqu8sQsboPDr2GEMY5B653D9bwWnm1wmbCpLasRNVwhXDH1YUCOBTrHqzIc5O093r8TEwMT1EZFboaqxtzIT4UnTRLCnHfXtTgDFKxKugRVu24rPNQ8TXRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژوزه‌مورینیو اعلام کرده که پس از پایان دوران حضور در رئال از سرمربیگری خداحافظی می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/89985" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💥
🇹🇷
جشن‌ویژه باشگاه گالاتاسرای برای ایکاردی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/89984" target="_blank">📅 09:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kqpmdbu8MERoxP18UvoLDCvwkxaw2MLWcc9DOl_6lzw2jm782oFe2yqdhNz9S3XJF7ycVarStumaySP0iHOpUmO9tE2IBUENUPisg2q7WEgksYalowkNpeh_8X5UalYIoEvSbx_vOgztFsV2QeqFTUNYLYQkmfhcP5TEdTNv00CKuEBCLIeSx-UweISRlX-IWASW3lLJCut_jdgLUdmZW_CYPQPK_E5zA-AyIz72PaufaDUrAYMW68I5g5k0koSjf2nP5b2f4LBId2yzNpoauedW6YSPcG5HTz2sTq4nMPsSzDdYk-s_o6tTaFYp963Ol3b6t-mN3_2Lr_3fiYIWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک سرمربی فصل‌آینده تیم فوتبال منچستریونایتد خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/89983" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebqwjB2Cz8vHFTKKzF5juMMW8CrRYv9lVDiXjeExPSiWpst1JbrJe9xapAPoMBCucok7oMnkBwnQ8uSRc9_ixJ6oRAi_hZ02clscISoyjIAKVH_YLMspn-dCQIgVPyL87b6c5Ns4f47xHXT-h1oY_6KBX6Bjk_h002q9cvUU4KlAE6zSRHXqtk6_uXWiwdTStusa7ZfAInaAXsMl-I-5OD6IA3fzuIsNEqsjR58rsax0JZb3ymPfF3GU0Y1FJYxqoZzmQh2iFKHGe1HkNySUYE5TRQ9qnNKoexD4HUxJa-9IP2dVd-l0QghbUohUW3A9fgXjQEohIatnejzywVllQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل لیورپول سهمیه لیگ‌قهرمانان اروپا را کسب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/89980" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZIpDeIIiO0JRPz48g-80JfIfTbcgWiLlQREWO8vd_GooUT1_qKqEQO47y35yWwFyaBYSTlkTuKGMKUresqNw1DaM6PHZ8XRpizOgS66Y2o_lGWBEGiuaawu4i1bvCfQNNhZTVAw1X6GnckYHDOwF5GEnY5NWqNpoBP2FS98gUdg2rmcpDCFbPjdPCBk-EnLrQFvo_uvQU3KlmSbTTdwdbrXMHEITg_Ll2-tU5fAyCFJ-dKura5RIumJ2M0Np4TQx5A6fyNMnpD2wQTLsnEh_1HVu3dK6FaGxecv8Z7_3ADZtQOooiEgBiQ3EmONmtbWSEm0hNBXRnv_aXSSv9nkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/89979" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
‼️
سازمان برنامه‌بودجه به دولت جمهوری اسلامی اعلام کرده که با وجود تورم شدید اخیر، منابع لازم برای افزایش رقم کالابرگ را ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89978" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brA-iFsfHcyKedH_sIqbi75j9xDnaNdWAVZJKc4wpXb0maevMJkvlNH5QvcmVyF9IZQck8xW1NAwZtSkFV96Wk1baY0ncBKgyipngpmDYWXHVQctevAXI2EmCy43NXXnkpZXfwyVs0bMI92qaGf0ZFVrSXXsEkZLFoGEqwt-utUDfx_zdUVRR1YwslTNkQPYWamvJmyXnEbgFfq3tIYGupRQI4xsAoYVovqHQYWQMBs83frhart49nWlUUsBafkmu1idHqO4Ia1n-MVllfiBNO-H1JtI5BtZm1LS6iUg5yx37fTx8CJ77tVF30cyLCxIbg_Bz3HvGAO4aH8pvhkBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇱
تیم‌ملی لهستان از برگزاری دیدار تدارکاتی با تیم فوتبال جمهوری اسلامی انصراف داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/89977" target="_blank">📅 00:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMpPG9A2BaKo9WqALVF6VYx5ycfmQlk2hWPr2uiIG65_t2t7jsiCQIFXqzKTEjjPDA9OnvhCVe42IYb_UDd_djpW7JHUb2RqwOwnidm8kLIBRKBSqrTeIY16Pjv07-Vrq8WwArNweMgwWQCy7iGan87LdZWJP3ZRM5RCvv4VaMOjTSLy8eDroleso4r1G8jQEHWTrNmuhu1dbYlLi9UD00EfCPVT8ffatHbMwXDIcw1JfDIvLlhG7ggW6oIRkHcsvwmb1bBdTCCPd0kXPioNFfL_W1jlcPIxUklR11sewoazr94Z9n0GwJO1Tx3BXZ1skfk4wLnUKL6wqi8su4QNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
لیست‌تیم‌ملی هائیتی برای جام‌جهانی با حضور داکنز نازون مهاجم تیم‌فوتبال استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/89976" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZK7cRTk7qLXLxqbmtchXd4BtB9_PD5A_NiGI59Fy967XO5iY3TNvx3aDKvCFbyEPEB9MysXTC5kqYsGpDlgfe91bdxMhv12pehyKYgGj090pwN5cX1UXXZNlaP0PrZHLrcpGUT7v4QuKbldCPJRtIS5JUfjJBizkKjdICnozxp3sYOnSPZPucFg-3jKesZTcPlgg3xtrGQWaF5Ankdr2TRKQsRhxSZZ3d6-eHeQW9SHojF9bbTH3l7U7v2R_SpO3RDfNb4JysVL56GZEc36Uji8SGuaeCoDUyuO73AW0xFSCg7SrcG4dIRB6bA9N_fiOC-zVPoiRfWrywLvik2RNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/89975" target="_blank">📅 19:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMe-d-TzdETrZJEml5lfgXlMKQfo6TTkVr7lKmuY7fOE6xp5X8tJ4gjqsmwBcT2OQ86QMhUUjvjvkvhwOpB1NzTYtVURy0twRFaRTKzGB8DozvqHNeUhvWAEdU06SrYqsF52SeJM4v3mrnnTZHX9vSPbTBrysk5Mzg1j3GKqGSOXVswLwRMjxVrKIJZLql2x-bY44plPAvZE268RsrL2uD1Lu1v8fLWP_Fgmm3qHn4OAC7PgYNYr_vUJe8Jp7mbS71UaNpFT25NFpSq-yuYHZ0xkJaarEKrF3F59qJl7oSn9l3qAYCDBQ7R7ZIuiPcxjLPqSzW2sgZ30fQG2rPIO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
لیست‌تیم‌ملی ساحل‌عاج برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/89972" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxB6PrGMspg5NgvOaN0nND1sO9z1Bp6pj_06IhpLj7EqBBM2RPkSpMf8rX44TM2BtTPXGT1tHLQHEsLDi-mFXhQehRJYXWJyR1VyP9QwpeYC8CFSEibTY5nJZSx1-Fi9h4qvEU5OioI9jSWSBmheZy0kU8H0IRA7H4yA8kFkvOXPPScxt5tUMWJpW4VWSFBxqGv-k8ntLOdcuZ6fqgHhElsicpY4BFwbyonDR5KiSLHJbfD-kLimIZxcg1YZCQWvBR6bjQLjSiEb_ylg52pjO6ATZ00yKSwUe41HC1w2uXDAohRuAL4DD5VlTeri45KINgGEawORRWRTWe-ciDWPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
اعلام‌ لیست نهایی بلژیک در جام‌جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/89971" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
