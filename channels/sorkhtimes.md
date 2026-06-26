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
<img src="https://cdn4.telesco.pe/file/RYVg_D7F-GDBpBN6IFQk2FyJlSbjNmnaTwtU-Fdwn-DN-vGkBRMxecM1sqCwH8bWl04Tc3S-1nnxYtY933MrVGo1HslxVx8FMB9DeXNC9uZyzDHEBztt0JsLEav2mTxmOZ_Zh6FvQfAzxQpndZyNn66yVAZxbYkIgocm91fIQue0klg5baEttwf235kTItZfZovngFfhkq3UJ_Uuv4D8P7BRPsZ6cBdYgDz9Y-nPT6M0LMokUKYSl6EBTA_FuSEh3PfXv52mc6uscqPceypki8lS8NMSYXqDk2UwQqOU4ZxbMw_WMBRoKQdXAan9cSmBJ0ePf-txkEzEMoaYzPj2Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 03:26:33</div>
<hr>

<div class="tg-post" id="msg-134413">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a18df2d4.mp4?token=NVnpKAsazr7oMHy4qhhirIUSTkRoMr8DMgrDfpHqmojUsm3V6vrcT1venajUnG29y5jxOIxltV2vpzhr8bfXXMxfBHQU4oWmfDS1vd3Mxzvpzm8Q9EdFnKek_9HlWa87HfGx9N0w7K341EDtWvmN4HL5JH3OgrkWsLVGjEgsFaSCTESDN0Tqf5NaKXCC0B_uzgAjUa1HEZmdCQ7gDWPrSI7X2N5K2n1H8w3j7iGLoLBucdF6iB1_AZAZBVMBuVJ2TMaHV7qY0MZI5ff9NfSEekWhsSKJPtAuCtfSNMjkoxZFDZUGO03xDYOWsD7xoLIfwzBnT_I-8Jc8Ztc5FYRTzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a18df2d4.mp4?token=NVnpKAsazr7oMHy4qhhirIUSTkRoMr8DMgrDfpHqmojUsm3V6vrcT1venajUnG29y5jxOIxltV2vpzhr8bfXXMxfBHQU4oWmfDS1vd3Mxzvpzm8Q9EdFnKek_9HlWa87HfGx9N0w7K341EDtWvmN4HL5JH3OgrkWsLVGjEgsFaSCTESDN0Tqf5NaKXCC0B_uzgAjUa1HEZmdCQ7gDWPrSI7X2N5K2n1H8w3j7iGLoLBucdF6iB1_AZAZBVMBuVJ2TMaHV7qY0MZI5ff9NfSEekWhsSKJPtAuCtfSNMjkoxZFDZUGO03xDYOWsD7xoLIfwzBnT_I-8Jc8Ztc5FYRTzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👌
👌
👌
👌
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/134413" target="_blank">📅 01:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134412">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVevqOLjJS3omTgF4PeTFxVHVpodXoaeMHDwQVEI2Lb9o3IgV9ATQhDLiT7IiLlXHF-IoTfhXjmvy_SUNnWW7ChWKMZA5g58hWbvuM-asj1kfNpSXPS_f1ehv_oyYzopq0DVUZ6wyNd2O_NXDuOpgcsjly3sgdm0fA9vQPcLWec9BG3GoS0jsjDLO9sGBkIflCVe6wMwiJ7GZ_Vsw1UJSw995boTjhEZbafL9B67jr3ckrYZb0BOiPxS3EppqzEIj-Iz_xW6ZrHq1DlX81Y2jxeVhM_QZisL7qWwpKMH_uXNSY64yHdG1jKdXsicx84Js4V3QJP1hyKSjuQKuP7n0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدار حساس و هیجان انگیر بامداد جمعه ایران
⚪️
-
🔴
مصر رو در وینکوبت با بونوس ویژه و بالاترین ضرایب پیش‌بینی کنید!
⚫️
🔣
0⃣
2⃣
بونوس ویژه جام‌جهانی روی هر واریز برای تمامی کاربران!
🎁
تا پایان مرحله گروهی جام‌جهانی روی تمامی واریزها
🔣
0⃣
2⃣
بونوس بگیر و فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا پایان مرحله گروهی جام‌جهانی فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/SorkhTimes/134412" target="_blank">📅 01:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134411">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from7 .</strong></div>
<div class="tg-text">حدادی کوتاهی نکرد تنها کسی میتونه پوست اندازی تیم رو شروع کنیم همین حدادیه</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SorkhTimes/134411" target="_blank">📅 01:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134410">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚽️
تیم پیشکسوتان ما این تیم رو باید میبرد
❗️
این تیم باید پوست اندازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/134410" target="_blank">📅 01:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134409">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🤩
حدادی سهمیه مرده رو زنده کرد، با هزار یک لابی تیم ۶ جدول دو دستی داشت میرفت آسیا!الان مقصر باخت به تیم سوم چادرملو با دو جلسه تمرین کیه ؟!
❗️
تیم ما کل پولشونو گرفتن یک ماهه دارن تمرین میکنن، با سرمربی ۱.۲ میلیون دلاری که قبلش تپه نریده تو لیگ نزاشته بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/134409" target="_blank">📅 01:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134408">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#تلنگر
❌
❗️
پروژه بگیر ها و قالتاق ها دارن زیر پوستی حدادی رو میزنن خاستم بگم دنبال پدرتون بگردید… با تشکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/134408" target="_blank">📅 01:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134407">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🤩
صحبت های پیمان حدادی بعداز بازی…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/134407" target="_blank">📅 01:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134406">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
حالمون از این تیم داغونه و ناراحت .امیدوارم اتفاقات خوبی برای کادر و بازیکن بیفته .....بریم ی استراحت ریز کنیم .ساعت 6/30 برای بازی ایران بیدار شیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/134406" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134405">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkM9gSHJYT6J1ujKXRgj1dT_5kp_grUVY7KCrrXAuIiv6TLOdu_Di1f21MrsUfv0WeZlpJNPC6gLQFg28-em6WzLfBvwitmjm2S8dPe32MhZhwLWO1h0SktzI29gaVlDucoNpKBb6zou2r01LIGjqA_TPQp9brqB6bqYo8s4xaSFtLKgERVvMbdKQc7XCylwkN-EI8F7uy2taLKe8HGSB23g4FUR2ZSzKEElKT2yxgtDbmvsa_FCaJZBhQrZ9NN2M35fF4FVAV_X0coz4pCWcfO1qNwTyxWD5TaHg3d_KOTJMwyKD3I0DEoqSp7b_q36Ck4PQHZnAGkVne63oVp2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آپدیت جدول بهترین تیم‌های سوم گروهی
❗️
پ.ن: ایران با برد صعود میکنه، با باخت حذف میشه و با مساوی کارش به اما و اگر میکشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/134405" target="_blank">📅 00:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134404">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
#فوری
🚨
هیات مدیره پرسپولیس برای فردا صبح جلسه فوق العاده گذاشته و درباره آینده پرسپولیس تصمیم گیری خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/134404" target="_blank">📅 00:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134403">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
پیمان حدادی : قرارداد اسمار تموم شد و ما دیگه قراردادی نداریم هیات مدیره به زودی تصمیم میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/134403" target="_blank">📅 00:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134402">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
فردا 6/30 صبح بازی حساس ایران آغاز میشه .کیا بیدار میشن که ببینن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/134402" target="_blank">📅 00:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134401">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/134401" target="_blank">📅 00:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134400">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
اخباری سرمربی چادرملو: 7 بازیکن با تیم ما قرارداد نداشتند ولی برای ما بازی کردند که از آنها ممنون هستم/ حق ما سهمیه آسیایی بود/ بر اساس آئین نامه حق صد در صد با تیم ما است/ به قیمت باخت و از دست رفتن سلامت بازیکنانمان بازی کردیم که نشان بدهیم فوتبال باید…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/134400" target="_blank">📅 00:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134399">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/744d80c96e.mp4?token=dy_nYlpzcfbRs8wfYaK4wiKy0ahzkprBrDB-vej72ShGKfQaIVPgjdOzHfyUQqsGn9xZljG_W1BEEbx6ryj-JqA_u6XKXLC9ZQnT3pd5G0n9fmRBhoZleBytRLcMJr-F4CpRTVImkoaxjLjfyj08pffmmfVmF49MDYoAeXWm3bonztjmzYBWl_2JJCktJZzde4KqwPd5O2njPtgR1A0sYTC9yAZ3zsLGfbGa95xEMk871n9OU5Gc0pA1vv3xKBZ3OZen22J-daur3CEqr9maG0ny42ZhgyTVVW8hbNLw7CbG09SOSBKttoAmPeyHUZAW55lngs1I-iRaxYlNEw6mfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/744d80c96e.mp4?token=dy_nYlpzcfbRs8wfYaK4wiKy0ahzkprBrDB-vej72ShGKfQaIVPgjdOzHfyUQqsGn9xZljG_W1BEEbx6ryj-JqA_u6XKXLC9ZQnT3pd5G0n9fmRBhoZleBytRLcMJr-F4CpRTVImkoaxjLjfyj08pffmmfVmF49MDYoAeXWm3bonztjmzYBWl_2JJCktJZzde4KqwPd5O2njPtgR1A0sYTC9yAZ3zsLGfbGa95xEMk871n9OU5Gc0pA1vv3xKBZ3OZen22J-daur3CEqr9maG0ny42ZhgyTVVW8hbNLw7CbG09SOSBKttoAmPeyHUZAW55lngs1I-iRaxYlNEw6mfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم لو رفته از رختکن پرسپولیس بعد از باخت به چادرملو، باقری خطاب به بازیکنان: هر بازیکنی که بازی نمی کند قیافه می گیرد/ فقط زبان شما خوب کار می کند!/ خاک بر سر باشگاه ما که زور می زند به آسیا برویم!/ مگر ما لیاقت این را داریم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/134399" target="_blank">📅 00:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134398">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
اخباری سرمربی چادرملو:
7 بازیکن با تیم ما قرارداد نداشتند ولی برای ما بازی کردند که از آنها ممنون هستم/ حق ما سهمیه آسیایی بود/ بر اساس آئین نامه حق صد در صد با تیم ما است/ به قیمت باخت و از دست رفتن سلامت بازیکنانمان بازی کردیم که نشان بدهیم فوتبال باید تکلیفش در زمین مشخص شود نه در جای دیگر/ نمی دانم آیا تیمی که قبلا با قاطعیت انصراف داده الان بازی می کند؟/ از بازیکنانم خجالت کشیدم که چطور بدون تمرین برای ما بازی کردند/ برخی ها دیدن سعید اخباری و جایگاه چادرملو برایشان سنگین است/ این تیم با زحمت و تلاش به اینجا رسیده است/  امکانات خاصی نداریم و سال دوم است که در لیگ برتر حضور داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/134398" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134397">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f78f234af.mp4?token=TMfmhOcgWDSkTCqjrllGYVkelSiDIfzXKvSB1s20fR9VstRhFNu9vjZqLolpONgXQewPKQqmg9hXekCw93lve_bvVZvo9tCZmagdWt8OT_-U-6rqv1dsEmBiOho248VR-zdViU0bYBP54vCR9H9J8Wf7HstIRQafonlVQ4W2IcdxVslbLuwdv8s1EUBGEiGpAC676MlTsjSz8JGlsOT5mzdBWZ6Gm7LyMTZbz4qzso21HZ3y1AugEUPB6EmIMwrFNg5d8zp2Z2bScOkdcbuqwmh4QyOoqQUUXbg6HzTVaYiAnXLsOXNpy2aamm8j5WqZnqsv9EjGbEl57G-G-R1ykqZFW1Gyl6rzBkmkaStPPCMbutc5RufkegIj21udfcB7pq7yrvwWX3hEA-heffNe4gyz6wfPi5RWyB_hfpkD-XWkdsVJySq45LtOX2PLCk7JjUyJaqFokE4cnqtKuv7Cd0DPXOr20Ns5A_YLdQeUVLX7AUREWF9CnoepmcGbX1Q_lTFG_VzpnbY2WlehYkQdKamAZwwdw5EunOvTPCmkDriS-_Uifor6qqm8uIoQUGC37OdlnnjX9ZyH4oGzFulvyWBRqbTNw512HyWYQ_PDQniI0as8zHjmX69xXbifT8fa9pBnjHjre_2hn-dmXkJrqkAqeuJEChcianiKLMmd9JY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f78f234af.mp4?token=TMfmhOcgWDSkTCqjrllGYVkelSiDIfzXKvSB1s20fR9VstRhFNu9vjZqLolpONgXQewPKQqmg9hXekCw93lve_bvVZvo9tCZmagdWt8OT_-U-6rqv1dsEmBiOho248VR-zdViU0bYBP54vCR9H9J8Wf7HstIRQafonlVQ4W2IcdxVslbLuwdv8s1EUBGEiGpAC676MlTsjSz8JGlsOT5mzdBWZ6Gm7LyMTZbz4qzso21HZ3y1AugEUPB6EmIMwrFNg5d8zp2Z2bScOkdcbuqwmh4QyOoqQUUXbg6HzTVaYiAnXLsOXNpy2aamm8j5WqZnqsv9EjGbEl57G-G-R1ykqZFW1Gyl6rzBkmkaStPPCMbutc5RufkegIj21udfcB7pq7yrvwWX3hEA-heffNe4gyz6wfPi5RWyB_hfpkD-XWkdsVJySq45LtOX2PLCk7JjUyJaqFokE4cnqtKuv7Cd0DPXOr20Ns5A_YLdQeUVLX7AUREWF9CnoepmcGbX1Q_lTFG_VzpnbY2WlehYkQdKamAZwwdw5EunOvTPCmkDriS-_Uifor6qqm8uIoQUGC37OdlnnjX9ZyH4oGzFulvyWBRqbTNw512HyWYQ_PDQniI0as8zHjmX69xXbifT8fa9pBnjHjre_2hn-dmXkJrqkAqeuJEChcianiKLMmd9JY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محسن خلیلی، معاون ورزشی پرسپولیس:
🔴
🔴
انتقادات کریم باقری به بازیکنان و ناراحتی حدادی از بازیکنان؟ در زمان کمی پرسپولیس به این شرایط نرسیده است. با دو الی سه پنجره پرسپولیس می تواند پوست اندازی کند. خیلی مواقع می گویند بازیکنان خوب لیگ را جذب کنید اما همه نمی توانند در این تیم موفق شود
🔴
🔴
نیاز به انگیزه و تمرکز بالا داریم.‌هر بازیکنی در پرسپولیس نمی تواند موفق شود. مسلما تغییراتی در پرسپولیس خواهد بود و حتما بازیکنانی مدنظر هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/134397" target="_blank">📅 00:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
پیمان حدادی : قرارداد اسمار تموم شد و ما دیگه قراردادی نداریم هیات مدیره به زودی تصمیم میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/134396" target="_blank">📅 00:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32fe1fda5.mp4?token=UtgrUXNkcU8NMkL3lrwnXctLIeWpiVburNa201PlsdjtsT8xthWrChI1H9DbwmtHTI8S3gRtFVQn77yU2TGqZPGlmmXiDnB7uoJjJ-IPT7wYi-xAr1t1r7nhHLldZjGb2DRTxQEbsIfSPUtZ0bxber0SVvpXpIzHYoBwWKiz5zq6VfZyYVrHlyRM8Q-9MQjoq3nITH96KA3UuSrcC2MdWiqFm7aZvB2X3OpjCpqM1GUippm20I25oLBH1FW9MZKQCsktEq0pfLwWVoQPhNjiy5B8YTLhOjX_wd07Ez3tEQe9uv0dmJGM4BicEeW4Y0m7Oy3P4lxmoYBg6Ds1lsbxekivlifZSedm9ic2n2GDxsVnbe-5dySDHx3Ccj-w9bAzdB9RjZ_Cm-d6hUixgMuf1m6p0qZB6mydo9c3TJIi9fNLx2PGtxRLnNhPldRrKDyjZKHNUDoLL-6l6auBDEHqD4pl8q4a5qDil3tSJfDgrJRqKl4iyPyRAaFgqzmTtS394jm0D27e3V0771q3EcEoDGjr0dTVzJXO_Y16kAMRVW6gqTGxTV_xrj77pw5cC2cK8E9fHf_CwR87_MTyVi9nKbK8yj2eaq5hU_kwPXef6M142x8bly82Qqs_FXWntizUOyV6umwQLAscvU67VFpYehDf2oudIY0ur0uyzTxmyuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32fe1fda5.mp4?token=UtgrUXNkcU8NMkL3lrwnXctLIeWpiVburNa201PlsdjtsT8xthWrChI1H9DbwmtHTI8S3gRtFVQn77yU2TGqZPGlmmXiDnB7uoJjJ-IPT7wYi-xAr1t1r7nhHLldZjGb2DRTxQEbsIfSPUtZ0bxber0SVvpXpIzHYoBwWKiz5zq6VfZyYVrHlyRM8Q-9MQjoq3nITH96KA3UuSrcC2MdWiqFm7aZvB2X3OpjCpqM1GUippm20I25oLBH1FW9MZKQCsktEq0pfLwWVoQPhNjiy5B8YTLhOjX_wd07Ez3tEQe9uv0dmJGM4BicEeW4Y0m7Oy3P4lxmoYBg6Ds1lsbxekivlifZSedm9ic2n2GDxsVnbe-5dySDHx3Ccj-w9bAzdB9RjZ_Cm-d6hUixgMuf1m6p0qZB6mydo9c3TJIi9fNLx2PGtxRLnNhPldRrKDyjZKHNUDoLL-6l6auBDEHqD4pl8q4a5qDil3tSJfDgrJRqKl4iyPyRAaFgqzmTtS394jm0D27e3V0771q3EcEoDGjr0dTVzJXO_Y16kAMRVW6gqTGxTV_xrj77pw5cC2cK8E9fHf_CwR87_MTyVi9nKbK8yj2eaq5hU_kwPXef6M142x8bly82Qqs_FXWntizUOyV6umwQLAscvU67VFpYehDf2oudIY0ur0uyzTxmyuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی: از هواداران پرسپولیس عذرخواهی می کنم. واقعا نتیجه غیرقابل باور است
🔴
تلاش کردیم بتوانیم از حق خودمان دفاع کنیم و به آسیا برویم. با اینکه نفرات خوبی هم در اختیار داشتیم اما نتوانستیم بازی را ببریم
🔴
چادرملو تمرین زیادی نکرده بود اما انگیره زیادی داشت به همین دلیل ما را شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/134395" target="_blank">📅 00:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚠️
اقای هوادار شما صدای باشگاهی، نیم فصل زن بانک شهرو گاییدید که اوسمار بیاد، شخص احمدی گفت گزینه اول و اخر تون باید اوسمار باشه هرچقدر خاست ما میدیم بیاریدش
❌
اینو نمیگم که بگم بانک شهر عالی کار کرده نه پارسال ایشون اگر پشت درویش نبود تیم با اون شلختگی و…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/134394" target="_blank">📅 00:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134393">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚠️
اقای هوادار شما صدای باشگاهی، نیم فصل زن بانک شهرو گاییدید که اوسمار بیاد، شخص احمدی گفت گزینه اول و اخر تون باید اوسمار باشه هرچقدر خاست ما میدیم بیاریدش
❌
اینو نمیگم که بگم بانک شهر عالی کار کرده نه پارسال ایشون اگر پشت درویش نبود تیم با اون شلختگی و هاشمیان تو لیگ نمیرفت، ولی درس بگیرید اینقدر جوگیر نباشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/134393" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62d8762d20.mp4?token=rtVkFl0u22P_ivTxN8sICIYptQlxtn84zJFf6cHWgqRlgUtdB5qZrGVVrXJXiMRR6AaDXc6I2ZcFT06X7s0jDJXhOk7O9MmzIHmnNBGtc2tOdZxQs1JWiG3-F6VUegcXYj1LNg8KI0GhRNhyUreBPW19GsIPwNv9cWf8CrIC00zVhpJWngFDtOVADTeg6B5WgZl6wSJQAoubCSZyOC7KT8JLosB-Vfl6-gRiYsXQEIphytikh1PhbaQJeiaf1eXLjRVBV07HeEf-q0c4eX6r-PHOv05Vjo0UY2wkMLPzkHM3LMcjGE4a_KOOMCFgIMMAw2VFHSW1wdgSSnsR4deRjjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62d8762d20.mp4?token=rtVkFl0u22P_ivTxN8sICIYptQlxtn84zJFf6cHWgqRlgUtdB5qZrGVVrXJXiMRR6AaDXc6I2ZcFT06X7s0jDJXhOk7O9MmzIHmnNBGtc2tOdZxQs1JWiG3-F6VUegcXYj1LNg8KI0GhRNhyUreBPW19GsIPwNv9cWf8CrIC00zVhpJWngFDtOVADTeg6B5WgZl6wSJQAoubCSZyOC7KT8JLosB-Vfl6-gRiYsXQEIphytikh1PhbaQJeiaf1eXLjRVBV07HeEf-q0c4eX6r-PHOv05Vjo0UY2wkMLPzkHM3LMcjGE4a_KOOMCFgIMMAw2VFHSW1wdgSSnsR4deRjjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
کریم باقری: ما بد بازی کردیم و باختیم/ بازیکنان مقصر شکست هستند؟ در این یکی دوسال پرسپولیس شرایط خوبی نداشت آن هم به دلیل تغییرات زیاد است
❌
آمدن اسکوچیچ به پرسپولیس؟  تیم ما مربی داشت که بحث اسکوچیچ شد/ این موضوعات فقط حاشیه سازی  است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/134392" target="_blank">📅 00:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134391">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚠️
موقعی که نیم فصل کون خودمو پاره کردم که اقای اوسمار داره با دلال هاش کیر میکنه تو نقل و انتقالات و تیم یه عده جوگیر میگفتن این مربی منتخب هواداره باشگاه هرچی که اوسمار کونده میگه باید بگه چشم، باز خوبه امضای ایشون و فرزاد حبیب الهی پای تک تک خرید ها و لیست هست؛ یه جوی راه انداختن نیم فصل هوادار هم جوگیر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/134391" target="_blank">📅 00:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134390">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
پیمان حدادی : قرارداد اسمار تموم شد و ما دیگه قراردادی نداریم هیات مدیره به زودی تصمیم میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/134390" target="_blank">📅 00:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134389">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚠️
ک… اسب حضرت عباس تو دهن همه کس کارت اوسمار جاکش، پوفیوزای خونه خراب ریدم تو فرق سرتون دو ماه باشگاه و رسانه، مردن دارن کون خودشونو پاره کردن برای برگزار شدن سه جانبه، مدیران باشگاه تا کجا ها که نرفتن….
❌
یه جو غیرت تو وجود هیچکدوم تون نیست فقط پول مفت میگیرد میچوسید، شب میرید باغ کونده بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/134389" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134388">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9b2dc774.mp4?token=Poz1FFLLJYe1pVFh8igSQ9MKwfVjC8QXZjYvUs7ETuYxrL5eW7F36Q0lCu8AwUkAzF5VgbhyFwI8JeM42TReLWAPqry9SlCwywVyRaqoLihtRljQgO_dwdPL5BzbYn2_VNQVMbp2VEYLUUhvLCZiM2xyAfRgNwhurTOaB2mCozis5jzMtDUA7nc3Xai528DFSF0LscLqhttS158bWDSNQE5PeomFVP53pdGDbvZ8TLZSvD30qget-0un29EWsB0s5ZVOMVf3hILOHq8eYEEskWvijbTlUGl4cyvTJgyRV-E6wYCTw0waebJ8TiOD8dGRApn3ohgCb6KIwQPNHzpn0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9b2dc774.mp4?token=Poz1FFLLJYe1pVFh8igSQ9MKwfVjC8QXZjYvUs7ETuYxrL5eW7F36Q0lCu8AwUkAzF5VgbhyFwI8JeM42TReLWAPqry9SlCwywVyRaqoLihtRljQgO_dwdPL5BzbYn2_VNQVMbp2VEYLUUhvLCZiM2xyAfRgNwhurTOaB2mCozis5jzMtDUA7nc3Xai528DFSF0LscLqhttS158bWDSNQE5PeomFVP53pdGDbvZ8TLZSvD30qget-0un29EWsB0s5ZVOMVf3hILOHq8eYEEskWvijbTlUGl4cyvTJgyRV-E6wYCTw0waebJ8TiOD8dGRApn3ohgCb6KIwQPNHzpn0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محمد نوری کاپیتان اسبق پرسپولیس: واقعا برای بازیکنان تیم متاسفم، این پیراهن برای برخی از آنها گشاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/134388" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134387">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
اسکوچیچ یکی از گزینه‌های ما است و باید در مورد او صحبت کنیم. خداداد عزیزی با پرسپولیس قرارداد ندارد و توافقی با او نشده است. او و محسن خلیلی گزینه‌های سرپرستی پرسپولیس هستند
🔴
بازیکن پرسپولیس رویش می‌شود پول از باشگاه بگیرد؟ در نیم فصل که صحبت از حضور اسکوچیچ…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/134387" target="_blank">📅 00:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134386">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: با ایران داداشی شدیم و به توافق «صلح‌ تاریخی» رسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/134386" target="_blank">📅 23:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134385">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
بخش دوم صحبت‌های طوفانی پیمان حدادی مدیرعامل پرسپولیس علیه بازیکنان
✅
بزرگتر(عالیشاه و پورعلی‌گنجی) باید بزرگی را در زمین بازی نشان بدهد نه فقط با حرف. این تیم باید جوان شود و پوست اندازی در آن صورت بگیرد
🔴
بعضی از بازیکنان پرسپولیس فردا خودشان باید قراردادشان…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/134385" target="_blank">📅 23:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134384">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
عصبانیت آقا کریم که حسابی شاکی و عصبی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/134384" target="_blank">📅 23:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134383">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ee125817.mp4?token=IEEPhAXiImHgFOvnZUFThPzek4ks3uY8OZZpw66pkmUuX5HKVvHmb6nFCNMuJIQ12hLaniajC9IEJbZPrMWzekX5Ut2NGv8kXXY8yPwxB0Znuil0jGmAB-qNrAmWLf0ZFGoHxl5OJeoRo872lQpv-Md5Ux9Ut0e2749jJh5FaopcaXIeIpQjqanMmm2hi9JNRKg97bP-l0nJHzBYagoZZRwA2Z2uAm4pNwqKhfZP3aRswibmyW4xG1cJ78rOJhQfWCD5VZgmAClfcVixKOK4nyimHe69enBxw4NpP_f7s85J2bIqrKX-cbpbBN4C0GMTmw8msqUqZGtG_AUXULec-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ee125817.mp4?token=IEEPhAXiImHgFOvnZUFThPzek4ks3uY8OZZpw66pkmUuX5HKVvHmb6nFCNMuJIQ12hLaniajC9IEJbZPrMWzekX5Ut2NGv8kXXY8yPwxB0Znuil0jGmAB-qNrAmWLf0ZFGoHxl5OJeoRo872lQpv-Md5Ux9Ut0e2749jJh5FaopcaXIeIpQjqanMmm2hi9JNRKg97bP-l0nJHzBYagoZZRwA2Z2uAm4pNwqKhfZP3aRswibmyW4xG1cJ78rOJhQfWCD5VZgmAClfcVixKOK4nyimHe69enBxw4NpP_f7s85J2bIqrKX-cbpbBN4C0GMTmw8msqUqZGtG_AUXULec-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
عصبانیت آقا کریم که حسابی شاکی و عصبی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/134383" target="_blank">📅 23:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134382">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c153d248.mp4?token=LInbOn8s7sVRWktOPM3p5PdAIBnR-56uNX2DoBqfowb1Ao6YbpW5uALvt5L-JRf8Km_WM-MnnLPTgYawZWq_mxPaLR0rib6iYx1kZCGEHifPvmTTN7N6pGJIgg9uAM0aK11zAKEDO157f5CoQpM7rQvuY7T7RCxk3qIbBWY8hLSoC_aw4zzcVuZFhJnbjx9nCmIzWH2smICUthCp-uIN5I31aloDg3X2r9XUOOa6Nqclm9kATOiRre_PxvlLcc6DKLQNaQVcZMccqUOS2RbU5SALWFsToqu9WrlDQhzzC0FClJKacy0UKheTcVcX3RmvljtFHFDMT-uDGpDW1kZ5g3yk-iypNC4zVJLC0fUJfFoLAmE6loS5hUBt3fDSbgCDw1OGQVUQmTtkqEoNDIu1CaQVia0pBXAlXThJrRzaPjUWw1Sp3X7Viy-kuiOEv5lFRb81GG-EmZIoW4uwmrzdFDW-IjrN4a-8Nch5vXCNpt1mBPblh3tMARdwTwtzfZuKsKowYLtaxncrz6PF1aAh7lrC8Fgogtws5hEt-t8KMryWSZiilOBlTPi5BKBSq-u_XSopKVVuRPSUbnCtoO1mVM5vDF-5BT9Bv2RXV7X76s7IY9bU54Scs7EIo-e0LFB00VYQ08P_7UFb0jlLsG7OgulXnEZ-33CIH_a9I5oYP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c153d248.mp4?token=LInbOn8s7sVRWktOPM3p5PdAIBnR-56uNX2DoBqfowb1Ao6YbpW5uALvt5L-JRf8Km_WM-MnnLPTgYawZWq_mxPaLR0rib6iYx1kZCGEHifPvmTTN7N6pGJIgg9uAM0aK11zAKEDO157f5CoQpM7rQvuY7T7RCxk3qIbBWY8hLSoC_aw4zzcVuZFhJnbjx9nCmIzWH2smICUthCp-uIN5I31aloDg3X2r9XUOOa6Nqclm9kATOiRre_PxvlLcc6DKLQNaQVcZMccqUOS2RbU5SALWFsToqu9WrlDQhzzC0FClJKacy0UKheTcVcX3RmvljtFHFDMT-uDGpDW1kZ5g3yk-iypNC4zVJLC0fUJfFoLAmE6loS5hUBt3fDSbgCDw1OGQVUQmTtkqEoNDIu1CaQVia0pBXAlXThJrRzaPjUWw1Sp3X7Viy-kuiOEv5lFRb81GG-EmZIoW4uwmrzdFDW-IjrN4a-8Nch5vXCNpt1mBPblh3tMARdwTwtzfZuKsKowYLtaxncrz6PF1aAh7lrC8Fgogtws5hEt-t8KMryWSZiilOBlTPi5BKBSq-u_XSopKVVuRPSUbnCtoO1mVM5vDF-5BT9Bv2RXV7X76s7IY9bU54Scs7EIo-e0LFB00VYQ08P_7UFb0jlLsG7OgulXnEZ-33CIH_a9I5oYP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بخش دوم صحبت‌های طوفانی پیمان حدادی مدیرعامل پرسپولیس علیه بازیکنان
✅
بزرگتر(عالیشاه و پورعلی‌گنجی) باید بزرگی را در زمین بازی نشان بدهد نه فقط با حرف. این تیم باید جوان شود و پوست اندازی در آن صورت بگیرد
🔴
بعضی از بازیکنان پرسپولیس فردا خودشان باید قراردادشان را فسخ کنند. آنها باید خجالت بکشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/134382" target="_blank">📅 23:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134381">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
پیمان حدادی : قرارداد اسمار تموم شد و ما دیگه قراردادی نداریم هیات مدیره به زودی تصمیم میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/134381" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134380">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
پیمان حدادی مدیرعامل پرسپولیس:در این دو ماه گذشته تیم مدیریتی تمام تلاش خود را انجام داد.
🔻
نمی دانم چه نوع بازی کردن بود که بازیکنان تیم انجام دادند. کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی ها مشکل داشتند؟
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/134380" target="_blank">📅 23:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134379">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba8ed1d05.mp4?token=d64GRWkKEEkyrKt3fesyWPzPkFPiQUr4I4-tB1q0J78-3ha965ctR7zMaDXZqVg2pFwZHrNZAzK7-Z19lWmuAHzobg6oTqGFCyab0XAEl3wF5CYnT8c_lIwaCtAKoLi9xub_pWYH2rl7WGswjo5xZr0HkcOG2kPJTe-JHOorz4dTFLbPf7MLr8rva59FXO3WEGV-68k62_4CPszUhnf2et19lvx-ZxgA2_YsnedCweiW3AkZOm2B7Jsno4l3iOiHh56ESRSLK9BN17rXUPHmLhph1L3jh2uKFLwlPcNr32K5l_6v71KXwCR4IylaO7Il5dc9qPItkQbmwXsXJM7VsH8OAxmvSIEEPgS7TQ8ZZ7LljvgQBWVooz22goxjS5gIORWV6wHeSv-qxS1mU_Yin5-BK2Gh16f-HK9_IyT8q12AxCwSr1BwA3_KUH0UVKFLYbwwU1bbs9Q_7Rw6s5ZY1gQNIDDNoiM1AzRDKSWyWzdieEX1DeZC9ebfG4mPcVSOhR136dc0_Nyf9dks2WUDTOKndzMgntyZIKGS__somSQTbiOMuAVMeQWdcRiYMm6Pm8fxaOvTac2fhkFc1ybEyCONKXrBlWVobbYHQ_6TsaCsL4WaNgWZPyrmeKsk5ATYVBbtMjaUtHGFIgJYrTCxiXgSWvqQGrCft-exYywA5Po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba8ed1d05.mp4?token=d64GRWkKEEkyrKt3fesyWPzPkFPiQUr4I4-tB1q0J78-3ha965ctR7zMaDXZqVg2pFwZHrNZAzK7-Z19lWmuAHzobg6oTqGFCyab0XAEl3wF5CYnT8c_lIwaCtAKoLi9xub_pWYH2rl7WGswjo5xZr0HkcOG2kPJTe-JHOorz4dTFLbPf7MLr8rva59FXO3WEGV-68k62_4CPszUhnf2et19lvx-ZxgA2_YsnedCweiW3AkZOm2B7Jsno4l3iOiHh56ESRSLK9BN17rXUPHmLhph1L3jh2uKFLwlPcNr32K5l_6v71KXwCR4IylaO7Il5dc9qPItkQbmwXsXJM7VsH8OAxmvSIEEPgS7TQ8ZZ7LljvgQBWVooz22goxjS5gIORWV6wHeSv-qxS1mU_Yin5-BK2Gh16f-HK9_IyT8q12AxCwSr1BwA3_KUH0UVKFLYbwwU1bbs9Q_7Rw6s5ZY1gQNIDDNoiM1AzRDKSWyWzdieEX1DeZC9ebfG4mPcVSOhR136dc0_Nyf9dks2WUDTOKndzMgntyZIKGS__somSQTbiOMuAVMeQWdcRiYMm6Pm8fxaOvTac2fhkFc1ybEyCONKXrBlWVobbYHQ_6TsaCsL4WaNgWZPyrmeKsk5ATYVBbtMjaUtHGFIgJYrTCxiXgSWvqQGrCft-exYywA5Po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
پیمان حدادی مدیرعامل پرسپولیس:در این دو ماه گذشته تیم مدیریتی تمام تلاش خود را انجام داد.
🔻
نمی دانم چه نوع بازی کردن بود که بازیکنان تیم انجام دادند. کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی ها مشکل داشتند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/134379" target="_blank">📅 23:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134378">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
میثاقی: تارتار گفت در تورنمنت 3 جانبه بازی نمی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/134378" target="_blank">📅 23:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134377">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
فوووووووووووری : اوسمار برکنار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/134377" target="_blank">📅 23:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134376">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
پرسپولیس با اوسمار:
🔴
اولین باخت تاریخ به چادرملو و گل‌گهر
❗️
باخت به فجرسپاسی پس از ۱۵ سال
🔴
باخت به خیبر خرم‌آباد در تهران
🔴
باخت به ملوان پس از ۱۰ سال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134376" target="_blank">📅 23:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134375">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
چادر ملو گل دوم و زد ...و خداحافظ آقای اوسمار .....خدا نگهدار .....لیاقت رفتن به سطح دو آسیا رو هم نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134375" target="_blank">📅 23:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134374">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
این پیراهن بزرگ پرسپولیس از تنتون دربیارید که برای خیلی هاتون گشاده ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/134374" target="_blank">📅 23:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134373">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867470f8d2.mp4?token=r9q5bC2AkwpySiQwXk_mKvQa0nPQ8xLHfxAHCmD9dfeYD-P_uRTYgdLhcyYB5pVz2kmIE63Wrg9JdmYhItgaapecTsCDH-Zuqgo1eMZFjOIAEj9HFu-pidzXZeZ3rQkTfMR_hj1tFd_4sklJCCtqvKn26c4K7ImdYiXoSdqZFhswfSYKDkRP845q1VRtVO-lMfZ1Ys7GI29I4he4YCQSo_yE6-8PHI36aCqtFDuvcVwM8wAQWp9rLvUrM_T4HpYgGtJwndBocajWvo92UM_ZNmtSwm2-1VjYTW-YKsiGnO4S1uJ054aNOI4FAv-KEO1Q6GEBt1Srby2fsh83eYhjEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867470f8d2.mp4?token=r9q5bC2AkwpySiQwXk_mKvQa0nPQ8xLHfxAHCmD9dfeYD-P_uRTYgdLhcyYB5pVz2kmIE63Wrg9JdmYhItgaapecTsCDH-Zuqgo1eMZFjOIAEj9HFu-pidzXZeZ3rQkTfMR_hj1tFd_4sklJCCtqvKn26c4K7ImdYiXoSdqZFhswfSYKDkRP845q1VRtVO-lMfZ1Ys7GI29I4he4YCQSo_yE6-8PHI36aCqtFDuvcVwM8wAQWp9rLvUrM_T4HpYgGtJwndBocajWvo92UM_ZNmtSwm2-1VjYTW-YKsiGnO4S1uJ054aNOI4FAv-KEO1Q6GEBt1Srby2fsh83eYhjEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
لحظه رد شدن پنالتی پرسپولیس توسط بنیادی فر !
🔴
این کجاش خطای قبل هند پنالتی بود ؟؟؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134373" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134372">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
همین امشب نصف تیم و بیرون کنید و برای آقای اوسمار پست خداحافظی بزارید ....به تیمی باختیم که پنج ماه تمرین نکرده و با تیم امید اومده بود ...لیاقت سطح دو رفتن هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134372" target="_blank">📅 23:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134371">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
همین امشب نصف تیم و بیرون کنید و برای آقای اوسمار پست خداحافظی بزارید ....به تیمی باختیم که پنج ماه تمرین نکرده و با تیم امید اومده بود ...لیاقت سطح دو رفتن هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134371" target="_blank">📅 23:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134370">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
لعنت به این تیم .لعنت به این بازی .لعنت به کل کادر و بازیکن ..تیمی برد که پنج ماهه هیچ تمرینی نداشته و با دو هفته تمرین حذف شدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134370" target="_blank">📅 23:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134369">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
چادر ملو گل دوم و زد ...و خداحافظ آقای اوسمار .....خدا نگهدار .....لیاقت رفتن به سطح دو آسیا رو هم نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134369" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134368">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
احتمالا ضربات پنالتی و نشون میده شبکه سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134368" target="_blank">📅 23:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
دو دقیقه تا پایان بازی و ضربات پنالتی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134367" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134366">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
موعود حرومی رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134366" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134365">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
ظاهرا برای پرسپولیس پنالتی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134365" target="_blank">📅 23:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134364">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
از بس بازی تعطیل و خواب آور بود وقت اضافه دوم و شبکه سه نشون نداد ...احتمالا می‌ره پنالتی و حذف پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134364" target="_blank">📅 23:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134363">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
این تیم حتی تیمی که پنج ماه تمرین نکرده رو نمیتونه ببره ....به نظر میاد .اوسمار و باید ازش تشکر کنیم و ی بدرقه خوب ازش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134363" target="_blank">📅 23:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
این تیم حتی تیمی که پنج ماه تمرین نکرده رو نمیتونه ببره ....به نظر میاد .اوسمار و باید ازش تشکر کنیم و ی بدرقه خوب ازش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134362" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
این همه اصرار واسه برگزاری این تورنمنت واسه چی بود؟این چه تیمیه آقای اوسمار .چادر ملو چهارماه هیچ تمرینی نداشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/134361" target="_blank">📅 22:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
❗️
بازی همون یک بر یک تمام شد ...کسی نمیدونه می‌ره وقت اضافه یا می‌ره پنالتی ....خود شبکه سه هم از دو قاب خسته شد ....معلوم نیست ادامه بازی و کجا نشون میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/134360" target="_blank">📅 22:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
❗️
بازی همون یک بر یک تمام شد ...کسی نمیدونه می‌ره وقت اضافه یا می‌ره پنالتی ....خود شبکه سه هم از دو قاب خسته شد ....معلوم نیست ادامه بازی و کجا نشون میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134359" target="_blank">📅 22:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
شکاری و خدابنده لو میان داخل ..سرلک و بیفوما اومدن بیرون ...بازی و باید تو نود دقیقه تموم کنیم .وگرنه ضربات پنالتی همیشه بد بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/134358" target="_blank">📅 22:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134357">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
🔴
تیمی که پنج ماهه تمرین نکرده به ما گل زد و بازی مساوی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/134357" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
پایان نیمه اول  پرسپولیس 1 چادرملو 0
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/134356" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
ویژه‌ برنامه اختصاصی این مسابقه با حضور دکتر پیمان حدادی، مدیرعامل باشگاه پرسپولیس و حامد کاویانپور، پیشکسوت پرسپولیس، از ساعت ۱۹:۳۰ به صورت زنده از طریق صفحات رسمی باشگاه در اینستاگرام و روبیکا آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/134355" target="_blank">📅 21:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
تا این لحظه با توجه به انصراف گلگهر از حضور در تورنمت آسیایی برنده دیدار پرسپولیس و چادرملو به سطح دوم لیگ قهرمانان آسیا راه پیدا میکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/134354" target="_blank">📅 21:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134353">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
پایان نیمه اول  پرسپولیس 1 چادرملو 0
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/134353" target="_blank">📅 21:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134352">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
گل اول پرسپولیس به چادرملو توسط محمدامین کاظمیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/134352" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134351">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
والیبال هم به باخت عادت کردیم ...دیشب به فرانسه ..امشب هم به آمریکا باختیم ..برد والیبال شده آرزو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/134351" target="_blank">📅 21:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134350">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=g0YQzutPR81vBNT5RPRpwHYAcMmgX6SuGYGv72ro4iAFzNUp5brRfWSYFc2-xz-BVDWsw8NUlGZGVPt-q-_NUdmWi22qzY4BGYPAcn4FKqlco7jmhgbJ75nXjs4NeTaTiYigcdg-gaqnQinImdP0Kqswdgo4CVdBBNCs88-KglHQRSWo7tp8JCRXAlrlImTvW3oAAq-zin3WjTuzAZBAxVNQGHnn9xKCxAc4Gynk_I1vj2fqt15r1y69hJxgJaHyARsA9lGuMciMG2WIcU-GMzpBB3XjS4--XXeXUmHozW6NrVy5R9Zp4YFeQGrDZZe31F1PLcEwEfeQj682MJYdgw45ALkPLmIEa8wsw5WVNluEFulJxJRBA1HX1zj7akjN6h5MUWQLYa0G-kk2D7WMqpDu92qJM_Hy2WtKkKd0YYSy38vvcas87RLGhRGhQ1nalqhIq9Qe7nfsNODcUCGNqnHwF42ac_3ko-joqYm9TM0SSxOEwn-q7wjFws_7Yxaa0e1n7HyRe6X0qVSJEYOd-GMnwgvt7FfbbcOAuxje8ABPvYMe3bmp8i22lY4Qxc5H0uVviDvrN2iENzvdY7SqeQNl27p9ZXdXGFAnyLRrcDiApBA1catYUKEd9o0CaokmSjSLD-WWzhTFb4Rthoq02zZZ82xzTvJa15IzYC8gz30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=g0YQzutPR81vBNT5RPRpwHYAcMmgX6SuGYGv72ro4iAFzNUp5brRfWSYFc2-xz-BVDWsw8NUlGZGVPt-q-_NUdmWi22qzY4BGYPAcn4FKqlco7jmhgbJ75nXjs4NeTaTiYigcdg-gaqnQinImdP0Kqswdgo4CVdBBNCs88-KglHQRSWo7tp8JCRXAlrlImTvW3oAAq-zin3WjTuzAZBAxVNQGHnn9xKCxAc4Gynk_I1vj2fqt15r1y69hJxgJaHyARsA9lGuMciMG2WIcU-GMzpBB3XjS4--XXeXUmHozW6NrVy5R9Zp4YFeQGrDZZe31F1PLcEwEfeQj682MJYdgw45ALkPLmIEa8wsw5WVNluEFulJxJRBA1HX1zj7akjN6h5MUWQLYa0G-kk2D7WMqpDu92qJM_Hy2WtKkKd0YYSy38vvcas87RLGhRGhQ1nalqhIq9Qe7nfsNODcUCGNqnHwF42ac_3ko-joqYm9TM0SSxOEwn-q7wjFws_7Yxaa0e1n7HyRe6X0qVSJEYOd-GMnwgvt7FfbbcOAuxje8ABPvYMe3bmp8i22lY4Qxc5H0uVviDvrN2iENzvdY7SqeQNl27p9ZXdXGFAnyLRrcDiApBA1catYUKEd9o0CaokmSjSLD-WWzhTFb4Rthoq02zZZ82xzTvJa15IzYC8gz30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل اول پرسپولیس به چادرملو توسط محمدامین کاظمیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/134350" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134349">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
این شبکه ورزش و برا چی راه انداختین پس یا والیبالو پخش کنید یا فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/134349" target="_blank">📅 20:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134348">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
نمایی از تمرینات پرسپولیس در حضور وحید امیری و با اضافه شدن تیوی بیفوما، محمدحسین صادقی و فرزین معامله‌گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/134348" target="_blank">📅 20:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134347">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
دو قاب شد .بریم برای بازی مهم پرسپولیس بعد از مدت ها .الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/134347" target="_blank">📅 20:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134346">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
والیبال طول کشیده .شبکه سه نمیدونه قطع کنه بره فوتبال یا نه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/134346" target="_blank">📅 20:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134345">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
پنج دقیقه تا بازی چادرملو و پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/134345" target="_blank">📅 20:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134344">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
مرتضی پورعلی‌گنجی کاپیتان امروز پرسپولیس در دیدار مقابل چادرملو میباشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/134344" target="_blank">📅 20:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134343">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">💢
گرم کردن عالیشاه و دیگر بازیکنان پرسپولیس قبل از مسابقه با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/134343" target="_blank">📅 20:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134342">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c0f66cfd.mp4?token=K9hxUkzWJOMgbK65ImKmK0TIROw4qBevKo24mztr0KmcuTTTIN1zqDQ--GAsLuEz0fkTmQBPuRkX41KHeZGtcsz1rEIfJ943zYCR6vgHw_Zikkl48AoYhF-uF7_vsnNQK3NjaE7a5Inkl0Qgv-Czpoo0Sd86aZ6j986_aVYwJy-Kol7rXnWZwXRe1e3I9_CXcMRshahPEiRQdZEz6RhZXIvvNPf1aoqvl4Qk90zNd3kHLsDAfRiViyPEhY73VNhGNZ5xfOrA2STsdGKD1PQgJGyh0ruxRiz8_FhSdMbsPUt6Er9Ru1N6a3B4DhUwo_cEtzAX399Lp7FwiyeRBfVTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c0f66cfd.mp4?token=K9hxUkzWJOMgbK65ImKmK0TIROw4qBevKo24mztr0KmcuTTTIN1zqDQ--GAsLuEz0fkTmQBPuRkX41KHeZGtcsz1rEIfJ943zYCR6vgHw_Zikkl48AoYhF-uF7_vsnNQK3NjaE7a5Inkl0Qgv-Czpoo0Sd86aZ6j986_aVYwJy-Kol7rXnWZwXRe1e3I9_CXcMRshahPEiRQdZEz6RhZXIvvNPf1aoqvl4Qk90zNd3kHLsDAfRiViyPEhY73VNhGNZ5xfOrA2STsdGKD1PQgJGyh0ruxRiz8_FhSdMbsPUt6Er9Ru1N6a3B4DhUwo_cEtzAX399Lp7FwiyeRBfVTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
گرم کردن عالیشاه و دیگر بازیکنان پرسپولیس قبل از مسابقه با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/134342" target="_blank">📅 20:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134341">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
ترکیب پرسپولیس در دیدار امروز برابر چادرملو
🛜
سیستم پایه:۴۴۲
❤️
امیر رضا دفیعی
❤️
حسین ابرقویی
❤️
مرتضی پورعلی‌گنجی
❤️
فرزین معامله‌گری
❤️
دنیل گرا
❤️
میلاد سرلک
❤️
مارکو باکیچ
❤️
تیوی بیفوما
❤️
محمد عمری
❤️
یاسین سلمانی
❤️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/134341" target="_blank">📅 20:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134340">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215ef22d08.mp4?token=ddODNhr8MK7UB1wfpRSxa19o3htHdPyU-nTXP4B833zpdfWVVNJMtJJAN17BLLSUfpyWUXMUk5_MYY62ZYpL3y7Mx5cnRtFugZ_OcrEnPr-huXRwVunv2p_GIaJLZwuOnhGIR8lH4Oi21zzaRt9XuOY8l7lN8ldDQfBG0Tunr1kuFU2PBfHUeuOGyi5fHJV8qz6KddAzarVudzch5gsmEl_YnwokZCQEXe6h7f5GSU5Plps9G7do5zCYi49GIi325CdDs3RT8e2Ul6CaaCJ7buZQCZcMUP3YgtL4Umt45dJQJdUugPjKb1yoHXwZXah9PCEbRL3YxLyl9gwrbiajWoFmC4vBCowPurX7KAicZPxRaPXcuZ124wy9XeV0V6ZKUwViopPM-w9wUJsTgNJyaaOw_1rzrM-9ZFyD4U0cUQeUI071zPqdDnOp7n3cmCNsiHRE1pTdw2WxTBZvJWy0qfnhvULC1po6Exw4xPOcYjChQRABbZonkPMPR8ffpNre3UgsptnhhPdG_c6hBgdBS-DPHHeUqQC3gEattc8iy0-p9L_lS52no7C69BrFJQaB5arB4YMH_QTIsamw5PrUJr3TXyEHzw9_b1ELbnrAVb2CQmCNJ1XxoI6NOgZXg7I-6kqfG2RpOAkzbIaE8B0hVQPgjiWSBwsWJcxwz8rwxnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215ef22d08.mp4?token=ddODNhr8MK7UB1wfpRSxa19o3htHdPyU-nTXP4B833zpdfWVVNJMtJJAN17BLLSUfpyWUXMUk5_MYY62ZYpL3y7Mx5cnRtFugZ_OcrEnPr-huXRwVunv2p_GIaJLZwuOnhGIR8lH4Oi21zzaRt9XuOY8l7lN8ldDQfBG0Tunr1kuFU2PBfHUeuOGyi5fHJV8qz6KddAzarVudzch5gsmEl_YnwokZCQEXe6h7f5GSU5Plps9G7do5zCYi49GIi325CdDs3RT8e2Ul6CaaCJ7buZQCZcMUP3YgtL4Umt45dJQJdUugPjKb1yoHXwZXah9PCEbRL3YxLyl9gwrbiajWoFmC4vBCowPurX7KAicZPxRaPXcuZ124wy9XeV0V6ZKUwViopPM-w9wUJsTgNJyaaOw_1rzrM-9ZFyD4U0cUQeUI071zPqdDnOp7n3cmCNsiHRE1pTdw2WxTBZvJWy0qfnhvULC1po6Exw4xPOcYjChQRABbZonkPMPR8ffpNre3UgsptnhhPdG_c6hBgdBS-DPHHeUqQC3gEattc8iy0-p9L_lS52no7C69BrFJQaB5arB4YMH_QTIsamw5PrUJr3TXyEHzw9_b1ELbnrAVb2CQmCNJ1XxoI6NOgZXg7I-6kqfG2RpOAkzbIaE8B0hVQPgjiWSBwsWJcxwz8rwxnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
میرشاد ماجدی: پرسپولیس و چادرملو برای انجام مسابقات ٣ جانبه موافقت کرده‌اند اما نمی‌دانم تکلیف گل‌گهر چه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/134340" target="_blank">📅 20:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134339">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvI2D2pUENKWo54OLW3BUy3kaHWmrKZBT8Jh3G5_w5oaZaoLnLr79nPUBvlT3RG6vwZaBtDiGvMHeYDMPpfh5UCRm7m-Yazbl5RwinUkUL6FlMCEcPVxoN5Onqpx7wOLt4brzACePvk6Z07B8dGpRqZUhDQXOStNM1dyc5YyEVm0-OJVJu5hMQB0ab2-02t1uFbScA6W6gVHknRapGmUzICJiy5YLyIIs1qFcYRHPa1ZvLGmaZH6HTVcWZNRbrQhHbDz48oJCBWE8RFbX6TCZcfoI9cP5izygLeIWSDJegktTTDl_HiFIaksukMOErhh8G0SVE4GgqDlKnCMEbXaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه G جام‌جهانی ۲۰۲۶
[
مصر
🇪🇬
🆚
🇮🇷
ایران
]
⏰
بامداد جمعه ساعت ۰۶:۳۰
🏟
استادیوم
لومن فیلد سیاتل
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
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/134339" target="_blank">📅 20:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134338">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
🇪🇬
🏆
دیدار بین ایران و مصر در سیاتل از سوی کمیته محلی برگزاری این دیدار از جام جهانی بعنوان"مسابقه افتخار"(Pride Match)برای همجنس‌گرایان نامیده شد!
‼️
‼️
پ.ن:طارمی و صلاح باید بازوبندی رنگین کمون(همجنس گرایی)ببندن.
🫣
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/134338" target="_blank">📅 19:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134337">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
ترکیب چادرملو مقابل پرسپولیس اعلام شد.
❌
امیر حسین آسیابان پور؛سعید محمدی فرد؛سید محمدرضا حسینی؛سیروس صادقیان؛محمد حسین فلاح؛مبین قوچی؛علیرضا صفری؛محمد حسین خسروی؛ایلیا نگهداری؛امیر رضا اسلام طلب و رضا میرزایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/134337" target="_blank">📅 19:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134336">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
ترکیب پرسپولیس در دیدار امروز برابر چادرملو
🛜
سیستم پایه:۴۴۲
❤️
امیر رضا دفیعی
❤️
حسین ابرقویی
❤️
مرتضی پورعلی‌گنجی
❤️
فرزین معامله‌گری
❤️
دنیل گرا
❤️
میلاد سرلک
❤️
مارکو باکیچ
❤️
تیوی بیفوما
❤️
محمد عمری
❤️
یاسین سلمانی
❤️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/134336" target="_blank">📅 19:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134335">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
ترکیب پرسپولیس در دیدار امروز برابر چادرملو
🛜
سیستم پایه:۴۴۲
❤️
امیر رضا دفیعی
❤️
حسین ابرقویی
❤️
مرتضی پورعلی‌گنجی
❤️
فرزین معامله‌گری
❤️
دنیل گرا
❤️
میلاد سرلک
❤️
مارکو باکیچ
❤️
تیوی بیفوما
❤️
محمد عمری
❤️
یاسین سلمانی
❤️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/134335" target="_blank">📅 19:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134334">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
حدادی ساعت ۱۷.۴۵ مهمون شبکه تلویزیونی پرسپولیسه و احتمالا تکلیف مربی مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/134334" target="_blank">📅 18:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134333">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
خلاصه آخرین تقابل پرسپولیس و چادرملو که با تک گل امیرحسین محمودی به نفع سرخپوشان به پایان رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134333" target="_blank">📅 17:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134332">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
شنیده ها: یاسین سلمانی در ترکیب رسمی تیم جایگزین عالیشاه میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/134332" target="_blank">📅 16:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134331">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
دراگان اسکوچیچ پس از دو بازی تورنمنت آسیایی رسما و شرعا سرمربی پرسپولیس میشه/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134331" target="_blank">📅 16:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
با اعلام رسمی سازمان لیگ، به دلیل درخواست شبکه سه سیما برای پخش مسابقه تیم ملی والیبال کشورمان مقابل ژاپن، ساعت بازی دو تیم چادرملو اردکان و‌ پرسپولیس تغییر کرد.
🔴
🔴
به این ترتیب مسابقه دو تیم چادرملو اردکان و پرسپولیس امروز ۵ تیر به جای ساعت ۱۸:۴۵ در ساعت…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134330" target="_blank">📅 16:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134329">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
پرسپولیس با ارسال پیشنهادی به ملوان خواهان جذب فرهان جعفری 20 ساله شد
🔴
این بازیکن 2 پیشنهاد از خارج کشور و سپاهان و تراکتور هم داره
🔴
جعفری با امار 5 دریبل و 3 پاس کلیدی در هربازی بهترین هافبک هجومی لیگ برتر شناخته شده
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134329" target="_blank">📅 15:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
فردا 6/30 صبح بازی حساس ایران آغاز میشه .کیا بیدار میشن که ببینن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/134328" target="_blank">📅 15:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
امید عالیشاه سه روز پیش مصدوم شده و تمرینات اختصاصی رو انجام میده و گفته میشه امروز از رو سکو‌ها کار رو دنبال میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/134327" target="_blank">📅 15:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
۴ ماه از آخرین بازی رسمی پرسپولیس می‌گذره و امروز قراره دلتنگی مون به پایان برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134326" target="_blank">📅 15:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134324">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOPvwKtdAQ43qdBXjOYlHRUXPn4OQF6rretoziIYZY3JQBD6PDvVOXoOEIi9zOMhVFFXut1tH7Vx34jRaVjxD_cknk4XIMRlDX3F4dCTC_FsXh6e5pWCdTx6349hMZB9buHSCRa5_HBYLYU_y8f75a-RuO_1l7mraAUTeeX03w1TIqQ-xBUKdroTNfpiwlP5vUgj5gJUyCzxgfv217q4kCOHA-UGYet-Vgq9-8L9WRUp7j_ZFIFjKDfwk6hl5J3zUL-uhmqMRFIX9Nq8uE-xIaEJv3_u0cp5puGFexdUwaCl5bbYc4ACXfa19lWVD34STL6FgxL_Sw8VqL5VWgirjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه I جام‌جهانی ۲۰۲۶
[
نروژ
🇳🇴
🆚
🇫🇷
فرانسه
]
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
استادیوم
ژیلت بوستون
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
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/134324" target="_blank">📅 15:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134323">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjeKb2DA7ElSHA1f6Y6n1XTUFVwNJKn44Dw3BfgwdYEvXaeea7upzutHrHiWg7kbsadrA1Pa9mXDJBUWCzM354PG0LqOAXmnR_4QaxryuFiQBvaQfoKlxHas7C2rz_ZqE-b0PlVIXYopqDesOuBh1J8BzeaGEDuZYr-QN-eD1IGgwxiOt_3CMie33J6mJ7u7Zx2EZ24j5rmLg6E399Ze-xp42ligycVG-K_0DARn4QIQPXWtIWdLVUxI1yCIHM8sUfa-0mfIfDdwcTG6ZD-c2jAJhErWS-7Ndqi2EM2w9L6qKhITbELxKcF4CzIfQZxpyfDeHvamkhfHDdKf47zXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها: یاسین سلمانی در ترکیب رسمی تیم جایگزین عالیشاه میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/134323" target="_blank">📅 14:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134322">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
برنامه بازی‌های بامداد شنبه، جام جهانی 2026
✅
شنبه ۶ تیر :
🕖
3:30 بامداد |
🇨🇻
کیپ ورد
🆚
🇸🇦
عربستان
🕖
3:30 بامداد |
🇺🇾
اروگوئه
🆚
🇪🇸
اسپانیا
🕖
6:30 بامداد |
🇧🇪
بلژیک
🆚
🇦🇺
نیوزلند
🕖
6:30 بامداد |
🇮🇷
ایران
🆚
🇪🇬
مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134322" target="_blank">📅 14:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134321">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
فدراسیون فوتبال: فیفا به ما و فدراسیون مصر قول داده هیچ مراسمی پیش از بازی یا حین بازی در ورزشگاه سیاتل برای حمایت از همجنسگرایان انجام نخواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/134321" target="_blank">📅 14:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134320">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
اوریه از پرسپولیس شکایت کرده و حالا حدادی گفته باشگاه دفاعیه‌ی محکمی ارائه بده و تاکید کنن که بیماریش رو پنهان کرده بود و غیبت غیرموجه در تمرینات داشته/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134320" target="_blank">📅 14:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134319">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAn-qGpMWGm9FfUwBvjT8Cy2SHGZPNToFew-2OPixhn79kiOsGvjmR4k73xBU6pW9MgTJRVOz_tQ-17mTYlckKPyGgHvarBL6E_Lkn3kjN2Z3xVrakxrDNEDj4hyCE5jbqSKwXJEDpkgG3l0dG7P7XSac_HF14FkhbTRWpVLs2G1cYReJldgpnUd13ygZRvvk2ZhA6azHEuEmifKemlAYhGgGK6J5vUSrds55ArznxtymvLmcyXz8wD-dAI3kVe4Z41U4xFxEf0biKDDgmmfUbLmc2LVgKTQCMX8SyM9vmYRTR6fUmRH0xRwr5jWE-su-H0hsPKOPwc5cq4LUWxKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
۴ ماه از آخرین بازی رسمی پرسپولیس می‌گذره و امروز قراره دلتنگی مون به پایان برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/134319" target="_blank">📅 14:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134318">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
با اعلام رسمی سازمان لیگ، به دلیل درخواست شبکه سه سیما برای پخش مسابقه تیم ملی والیبال کشورمان مقابل ژاپن، ساعت بازی دو تیم چادرملو اردکان و‌ پرسپولیس تغییر کرد.
🔴
🔴
به این ترتیب مسابقه دو تیم چادرملو اردکان و پرسپولیس امروز ۵ تیر به جای ساعت ۱۸:۴۵ در ساعت…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/134318" target="_blank">📅 14:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134317">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
ساعت ۱۸:۴۵ بازی پرسپولیس و چادرملو از شبکه ۳ پخش میشه.و والیبال ایران و ژاپن ساعت 18/30 رفت شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134317" target="_blank">📅 13:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134316">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
ساعت ۱۸:۴۵ بازی پرسپولیس و چادرملو از شبکه ۳ پخش میشه.و والیبال ایران و ژاپن ساعت 18/30 رفت شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/134316" target="_blank">📅 13:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134315">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
فدراسیون فوتبال: فیفا به ما و فدراسیون مصر قول داده هیچ مراسمی پیش از بازی یا حین بازی در ورزشگاه سیاتل برای حمایت از همجنسگرایان انجام نخواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/134315" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134314">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMYsoCYWDQAUgD2loV_FW05tRRC-kHK4TlRscpd8_zlAi8lImzS3k-DbSKCC3_GI_VKVmsDo_DddVRMRLISXjwQ48UonnhQTa99wTdseU_7SMWL9HQHvKApn1EoLSNZu50RLxJak2lofjBhPMCCMAgBChasFglf3gYDMWwIafCx79W3x-LyjmYXMVBjOzdbfpkp3F9z1okm3Gv10VepwpphNPoAw6OdQBORC9O_MYIHZY8JXag_NTHrnBK3yAKPMzoLFoYN-FBbtusEerlTvJdZ_WC5HF3C3CEJF4UndpL7AHhkFxpySQevABhPTjpzE5XeNxeKW-mGZtQ377tcxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فدراسیون فوتبال
: فیفا به ما و فدراسیون مصر قول داده هیچ مراسمی پیش از بازی یا حین بازی در ورزشگاه سیاتل برای حمایت از همجنسگرایان انجام نخواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134314" target="_blank">📅 13:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134313">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
لیست تیم پرسپولیس برای بازی با چادرملو اردکان
⏺
1_امیررضا رفیعی
⏺
2_محمد گندمی
⏺
3_ حسین ابرقویی
⏺
4_ مرتضی پورعلی‌گنجی
⏺
5_امیرمحمد بخشی
⏺
6_سهیل صحرایی
⏺
7_فرزین معامله‌گری
⏺
8_علیرضا همایی‌فر
⏺
9_دنیل گرا
⏺
10_میلاد سرلک
⏺
11_محمدخدابنده‌لو
⏺
12_مارکو باکیچ
⏺
13_علیرضا…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134313" target="_blank">📅 12:26 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
