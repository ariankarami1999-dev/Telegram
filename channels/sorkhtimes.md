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
<img src="https://cdn4.telesco.pe/file/K8k_wOvr-ZHact7WsHMpuXkF-okP18UfCYn7D6FfxwnLhNBaqJ5EdKWN5aPiBuCvSki1kO_A1qoAzc82vOPLicdp0I_YApdEzUOPPxZe-qODm15wZIgXFhmXJu2E95TU1RjVa-P9Y7yCfCnmxniJ6nkPXhhewLET1HMl625GIKF4_eRLiiYkr_MP-aNM6ep4hIOtN7YJPtQ9xZvqC2tlNpIzhK8guGsya_dsQ2n-WAltld7q4F9sHnTgGcE1t2IJ5BtbPrJ5nwzbbXXYLD3dDIWwOzqred3j7RrDwUjIkA1Yc15LXnJG-0GVZ8U8N5zKvEFSBUq1qXgNGw4heyOCzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-139365">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes   ﻿</div>
<div class="tg-footer">👁️ 789 · <a href="https://t.me/SorkhTimes/139365" target="_blank">📅 18:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139364">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
با اعلام کمیته انضباطی قرارداد یاسر آسانی با استقلال قانونی است و مشکلی برای همراهی این تیم ندارد
✔️
البته خب انتظار دیگه ای هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SorkhTimes/139364" target="_blank">📅 18:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139363">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE2ewwMtKiPt7DPc_Vb-bcThfIB433MDE2uDw8CXJsx9efqYn1wWbBZYY-KvFtH2QU36nCpyKw9HMV02o2PC6ZcjJtDCUKEPmgfpTqId2gYbBUmzUb1pIJZIfegWYRaOkb9RC6fp2SR2eo-jA-PBXAKY7izGPDDZbkJtMjJ0EtPCso4qbPTj0eraCMKTrr6wUdj_AiAaDlkqnhUAdzmcXIPXmZ2s6N7tzqWy0dNz29iCv5MeyNH-pM8Exv8Cgxxjftlg6nZa_TN66PaeKiUjU1e-rwrgH5J6w_qk8BCi-tsyv9N3nwcFiL0rINXko3wU7DvKQvvzNBW5mSHnaLl_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/139363" target="_blank">📅 17:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139362">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj8hXTpHFDO7JXhlFUg4tDufKF9NykrUemVewCLU-RuA0iXYQpPG1GYXoJrDmo-DXON3Qv1n77mG7zUw8uSOb5EMCvjHYbz0_CN091u4SwHRlp6jwMNdFMhYBHDQyaDdvtj2EiPkfIYP-aE2SnPE8ZJ5p_24BAalkyenIPJ_pt7GAxbCGp0R_wuvr0MVLLOXiHaHUgC9PH2opPZMGY1rfz9AU1s_G6T5m7qf2JM8mBpJhvUYcgKrUzSYhWgfZYvxCPB0MN5rsm9UOgsGcA5LkXXNhja2JnoSWtCrQW8xPJycCsU6vCt10fXmYdcBtVAjSTxv7EtpdasyHR8kjc4ybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
کاروان پرسپولیس راهی اصفهان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/139362" target="_blank">📅 17:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139361">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
کاروان استقلال با تاخیر به اصفهان می‌رود
⏺
پیش‌تر قرار بود کاروان استقلال همزمان با پرسپولیس و ساعت ۱۶ با پروازی اختصاصی پایتخت را به مقصد اصفهان برای برگزاری دربی صد و هفتم تهران ترک کند.
⏺
با این وجود به دلیل همزمانی حضور تیم‌ها در فرودگاه و رو‌به‌رو…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/139361" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139360">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
تیم داوری دربی ۱۰۷:
⚪️
داور: موعود بنیادی‌فرد
⚪️
کمک‌داوران: علیرضا ایلدروم، بهمن عبداللهی
⚪️
داور چهارم: سیدرضا مهدوی
⚪️
ناظر: اسماعیل صفیری
⚪️
داور VAR: میثم حیدری
⚪️
کمک VAR: علی احمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/139360" target="_blank">📅 16:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139359">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/139359" target="_blank">📅 16:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139358">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
❌
💢
💢
💢
گفته میشه تارتار قصد داره ترکیب پرسپولیس مقابل استقلال رو بازهم تغییر بده و عمری برای مهار آسانی بجای سرگیف وارد ترکیب بشه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139358" target="_blank">📅 14:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139357">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن جانشان را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/139357" target="_blank">📅 14:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139356">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
هفته هفتم لیگ برتر فوتبال ایران به دلیل اصرار بر اعزام تیم ملی امید به بازی‌های آسیایی ناگویا و تداخل برنامه‌های اردویی این تیم با مسابقات باشگاهی، در آستانه لغو قرار گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/139356" target="_blank">📅 14:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139355">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vedS6JbFk7NH4c9LjEiVySMRcDscfg1yQfW_sLvcxEG1PQ6JI6sIio-9qKsiJlZxsLzdefDq923rcWdjzMrw--bpqUv9cmIWUdJAX_EixjdTDzd47OKnUOi9gw-69Edx2tyG-X5m9swqniQZzW1vq9fC7QMr5tZddT0d9pGfNFm8SCNO7_5MWgVei4sk02Y-m4zZzggNAOvfU96Jey73ofP-GTxMFdLXOr-0mmMjRWk8cYtqxri6VziiSpSA8jOjaFKZyaUd-gjx77qqQFFpyEt41vLNXlPQGeK4j5F_iO1Gux15eUmWPFtteVFu8GkSD2WkjxUTs4jKymHoXjh5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبردی برای سه امتیاز در قزوین!
⚽️
تراکتور با انگیزه‌ی برد به مصاف شمس‌آذر می‌رود؛
یک بازی سخت، حساس و تماشایی در انتظار دو تیم!
[
شمس‌آذر
🟢
🆚
🔴
تراکتور
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139355" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139354">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
گویا هفته هفتم لیگ برتر بخاطر مسابقات تیم ملی امید لغو شد
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139354" target="_blank">📅 12:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139353">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووری
❌
احتمال تعطیلی لیگ ایران بعد از بازی دربی وجود داره. علتش هم برگزاری اردوی تیم ملی فوتبال امید هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/139353" target="_blank">📅 12:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139352">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
تا کنون حدود 40 هزار بلیط برای بازی دربی فروخته شده و ظرفیت فروش پر شده اما احتمالش وجود داره‌ بازهم چند هزار بلیط دیگه شارژ بشه؛ ظرفیت کلی ورزشگاه نقش‌جهان 75 هزار نفر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/139352" target="_blank">📅 12:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139351">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/139351" target="_blank">📅 12:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139350">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/139350" target="_blank">📅 12:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139349">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووری
❌
احتمال تعطیلی لیگ ایران بعد از بازی دربی وجود داره. علتش هم برگزاری اردوی تیم ملی فوتبال امید هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139349" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139348">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
☄️
تماس تلفنی پیام صادقیان با پدیده ۲۰ ساله پرسپولیس
✔️
✔️
ستاره تکنیکی و سابق پرسپولیس قبل و بعد از پیروزی شاگردان مهدی تارتار با امیرحسین محمودی جوان گفت و گو کرد.
✔️
✔️
گویا پیام صادقیان، پدیده 20 ساله پرسپولیس را دعوت به آرامش کرده و از او خواسته است…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139348" target="_blank">📅 11:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139347">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139347" target="_blank">📅 09:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139346">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
🎙
سامان آقازمانی، بازیکن پیشین پرسپولیس:
‼️
اصلا دوست نداشتم جای بازیکنان تیم ملی باشم. راست بری، با دولت درگیری. چپ بری با مردم درگیری. بی‌طرف هم بخوای باشی بهت تخم‌مرغ میزنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139346" target="_blank">📅 09:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139345">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
فووووووووووووری
✅
شنیده می‌شود سازمان لیگ تنها مجوز فروش 70 هزار بلیط برای دربی داده است! ظرفیت ورزشگاه نقش جهان اصفهان 75 هزار نفری است...!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139345" target="_blank">📅 08:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139344">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139344" target="_blank">📅 08:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139343">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JppoJcfuE7Ox0DCVgE37-vfnsc2e4JPpTDCbU9-T3_TQ6KjLR9z3vrarRq0XXJAKMs-M0L9eki-KrnFT4TXX1C_fBt7BPZPk902Go7duVFfGJAXYUpR5pOZqMFgkalqlh3oS3gR0DwdsKI6KPkXLuumuoaxXlxLo_0DMNF8jEwCffeee9pK5YrllWWFjHVqkT9IR2n3mgV-e7e-AgIcWIXF7vvjqPYl8Rat7j_cIx0ZnsjRP0mQIqLkO-6e851Fr3A5amgkl1oQRQNE5bxkbcZ2gR07JO5bU9uMRbFKDQMFb4c8TiGL_CZv8-vrz5eRtdxctGl-GCR9SnfX7pyhFAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139343" target="_blank">📅 08:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139342">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxRX4jgW6d4MH-6XlQ-lbhTlR6soycFaSnmU6Bv2eoRY9UHeipD-_2yjIkBk7Jb4zCrQaMYsXfR857s-tw_idzN2Vu0bdBk9lqv-DvCwgV5uW2_PCWUNcJziepRVvpcf9g7ARLLt_6oAo9Xtn_dV8hzE-88LUd4h0wEVVmNxD7RCZMEyddRHJd6onFOtZ8VGv16-SM2vRKVMkL6GqU_BpU0PXecuFtgyWtWx5AmIHk-jdCAjf79hOf6xL5E_mr8gh7sj3Lko4DbNkCfw1bnQbPeblaKQd0PCUDnnA1LKVzLgLSjleiqXpAPIoKDgV2-jisSw5H1K4RRxmdIFo6LbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
بن شلتون
🆚
خریکسپور
🎾
تیافو
🆚
مارتین دام
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139342" target="_blank">📅 02:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139341">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: فوتبالیست‌های ایرانی قلیان می‌کشند
✔️
✔️
چرا باید دروغ بگویم؟ بازیکنان ایرانی قلیان می‌کشند. قطعا فوتبالیست حرفه‌ای نباید این کار را انجام بدهد اما متاسفانه این موضوعات وجود دارد. در ترکیه چیزهای بدتر از قلیان می‌کشیدند
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139341" target="_blank">📅 01:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139340">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: حضور من در ورزشگاه شهر قدس خیلی حس خوبی بود/ دوست داشتم لباس عوض کنم و به زمین بروم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139340" target="_blank">📅 01:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139339">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
پیام صادقیان: حرفه‌ای ترین دوران فوتبالم ترکیه بود اما زیر تمرینات پرفشار آنها بدنم دیگر جواب نداد و فوتبال را در ۲۷ سالگی کنار گذاشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139339" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139338">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: بهم گفتن سایت شرطبندی که میزنی قانونیه مثل نیمار و فوتبالیست های بزرگ و اسپانسرش هستند و نمیدونستم قانونی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139338" target="_blank">📅 00:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139337">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
پیام صادقیان:
❌
شرط‌بندی هر نوعش تهش باخته و فقط شما می‌بازید؛ من اشتباه کردم و همینجا میگم پشیمونم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139337" target="_blank">📅 00:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139336">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
صادقیان : شرط بندی تهش باخته و سرابه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139336" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139335">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: با محسن مسلمان تو تیم ملی زیر 10 سال با هم بودیم بعد هم در پرسپولیس و تیم ملی با هم بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139335" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139334">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
ورزش‌سه: در تمرین امروز تارتار به سبک بازی با تراکتور بازی با ۳ هافبک و ۳ مهاجم رو تست کرده که مثلث خط حمله رو علیپور ، بیفوما و محبی تشکیل میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139334" target="_blank">📅 00:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139333">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
پیام اومده فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139333" target="_blank">📅 00:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139332">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139332" target="_blank">📅 00:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139331">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=luxOo39vqqI1KdpfQ8cGhMdXZjAvYoYHwrzhFtIcQG_RqrczSZn7W8i5_KlrIQx7Q0SzCRv1ZDUF9uMOEI6m3VcixcrvbdLHUNuzoHL94BOSVca9gUKXZX0mMMdwQZK0RMboQZ_KAzAH0lsQSNns4-C8PhCM4WV61dCO1WNU-zCOUyYM-9ndm_eIewsHtToOK9oYdYw29_zvoqiMRP37ZZLcdIyaKRrln46oLXRJ49XHT0CBIdrBRsVprtQeSQQUmM_6ztMBJPgcqUV-XfGnSQo-QTQqkc5Z0jIn0nbPuu7TtBVCrj3nNGXO-VMNYr0uVvHZzv8qzYl7vf1jwA6Wvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=luxOo39vqqI1KdpfQ8cGhMdXZjAvYoYHwrzhFtIcQG_RqrczSZn7W8i5_KlrIQx7Q0SzCRv1ZDUF9uMOEI6m3VcixcrvbdLHUNuzoHL94BOSVca9gUKXZX0mMMdwQZK0RMboQZ_KAzAH0lsQSNns4-C8PhCM4WV61dCO1WNU-zCOUyYM-9ndm_eIewsHtToOK9oYdYw29_zvoqiMRP37ZZLcdIyaKRrln46oLXRJ49XHT0CBIdrBRsVprtQeSQQUmM_6ztMBJPgcqUV-XfGnSQo-QTQqkc5Z0jIn0nbPuu7TtBVCrj3nNGXO-VMNYr0uVvHZzv8qzYl7vf1jwA6Wvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139331" target="_blank">📅 23:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139330">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139330" target="_blank">📅 23:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139329">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❤️
❤️
اورونوف در تمرین آماده بوده اما وضعیت جسمانیش همچنان بهش اجازه نمیده که ۹۰ دقیقه بازی کنه و قراره نیمه‌ی دوم به بازی بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139329" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
‏ ترامپ به شبکه فاکس نیوز: ما امشب به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139328" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❤️
❤️
10 دربی بدون شکست برای کاپیتان
✅
حسین کنعانی در آستانه یازدهمین حضور خود در شهرآورد پایتخت قرار دارد؛ کاپیتان سرخ‌ها در 10 دربی گذشته که به میدان رفته، هرگز شکست نخورده است. او حالا به دنبال حفظ این رکورد ارزشمند در یازدهمین شهرآورد خود است.
✅
پیش از کنعانی نیز کاپیتان دیگر سرخ‌ها یعنی امید عالیشاه که امسال از جمع تیم جدا شد. با ثبت 18 دربی بدون شکست، یکی از ماندگارترین رکوردهای سرخپوشان در تاریخ این رقابت را به نام خود ثبت کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139327" target="_blank">📅 22:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139326" target="_blank">📅 22:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139325">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=memw8nYgm8d5npOgfPAzpKH9IxpZqY9Urd-ylpJHzSc2F8Cdat_aeo8LL_d1yg0Cfl_uwYTTSaG6G52vOD86Qpk4nXy8_4wC9R7lQhSPpIdWy2aJdZQrpLWkwCnq1uUA9CFHGQMR-2n5ZhniivF_UC-dCfJzrfF_aa3sVSqA1XVyqBWOdvFw9EEMScx5OEbHV1Z99R7tLt98N7Qa-wpOKZtM29imXqgVgOCxlVeIIqd6hOWVmLx4w4MTd9KYZl8c_sJozwTwLrYGKY3m00P5nSN0Jplkgpp7DR3cFdpRCqPCwv6y1SP-xwi5AyWKA2suqofL2WIX3elp-WK0_6l_Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=memw8nYgm8d5npOgfPAzpKH9IxpZqY9Urd-ylpJHzSc2F8Cdat_aeo8LL_d1yg0Cfl_uwYTTSaG6G52vOD86Qpk4nXy8_4wC9R7lQhSPpIdWy2aJdZQrpLWkwCnq1uUA9CFHGQMR-2n5ZhniivF_UC-dCfJzrfF_aa3sVSqA1XVyqBWOdvFw9EEMScx5OEbHV1Z99R7tLt98N7Qa-wpOKZtM29imXqgVgOCxlVeIIqd6hOWVmLx4w4MTd9KYZl8c_sJozwTwLrYGKY3m00P5nSN0Jplkgpp7DR3cFdpRCqPCwv6y1SP-xwi5AyWKA2suqofL2WIX3elp-WK0_6l_Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی تو لیگ دو روسیه‌ با پرتاب اوت پاس گل داد و پشمای گزارشگر به این شکل ریخت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139325" target="_blank">📅 22:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139324">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
تأیید پارگی رباط صلیبی «مهدی ترابی» بعد از MRI اول، در انتظار نتیجه معاینه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139324" target="_blank">📅 22:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139323">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyrCoYsALdiD8Mi4QwMTWAx_c6IP6F94ZbUQ5w0ogaUqW1JCCc1pfOYZJc3L4GxmuEzS-MCPmD6Vg1Z_3LiPcKr4-F2tAxL13wIhRouVe0ukuUHnptdP6JIr5uO4Z4CWJN7MbDc0th5XY5pwYF_oH1O1E2VU2YnFPyIR7qP7Ztg3a_HV-1SsmpaWVOSYNHjPKqKkosmSVOXgXzGmDjUcaeNmiTqRrN9SCVug2bT8rEa0A5EYNmx05y2LWF2dTYjdw8XuyFWb__3Fzc4sES8oBNvgzv0dvZ4TBvb8VUc-CKgpKocGCljj3XZEqu_vaOr_XazSuLGf3_ZdfueU92gD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139323" target="_blank">📅 22:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139322">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139322" target="_blank">📅 21:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139321">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139321" target="_blank">📅 21:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139320">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139320" target="_blank">📅 21:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139319">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد  هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139319" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139318">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Arp7sXtuMorV9z5Z6KvNXyesHPI6JQdOPDumtorZtAtGb4qU0t3NIQ7HtFEusSrrngBj1YM-o_8L_IPEhkFnn0EFPUis70oTWwyOkeJowvDPp0U_9B3pFiu0Mzrr_eQbjfv85XzbZPNuzRxQ-EMJGXMy1HG-41Wzpmler87WXS6UamBhDURJzQB2niWCQYu_UgWOlq0h-2-VkvVZ_HBCU5CFpE6gHpiNYDCBCiFXmTO_z07PJaUT--gdnZRCZdQnDR6AyB7gKOKLgKnYlf8gS1x4lC_A1GWDPOI2e4cgW3ix7zsc0f5J6GAYMBUDgoDu956L_by1VNCLINxBrnFKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139318" target="_blank">📅 21:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139317">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-YVlb0FqVpwct3WxINjo6-_p64GyK5HH-VWvx8IMcYMVFuy8_ckSQxi-jT8Orknm63PEoYLwoUAidh2tAn275rPvMNRdnJb5ExKrIVL1N3d7YYUQjpmpVfmpJd1xEWce4_R7MnXW8XHVqDKJhsnRFH_BtSuLydLHmsQrcH5qixuq8bOW68bCvhSm2O_rGHIq5hjNb9l-yXCMyudGqB_fVwEPv1S-_HhaqukZbbeKSMKNqn9ijdXiJrc33_l1vcAtqVhh3YJr8D8kDTWGUJBek-OOtQg3h9qg06D0tSCMDnvHTec5Hp0ttDdqnZUsO8-8Ld3FKkU7hCMXS5ObZoEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد
هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139317" target="_blank">📅 21:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139316">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJb5D2E3qxDp106UFZufx1WmIt-d8E0W9raS5uEtf9kjyEcy7ljl91tQC3j42PO-hdJmGO4R_RXdZHhNethVJDH-rThjGhTN7aD-VAZrAK4lkea4GMZjLi-tpVG0Oc2OKhkLhdqgw20u6yIa5Y1R7EY985fqApmILBRjdDUvtqbHrvLN4tHaMYeKRhcM6OGvNbA-OyGbq2HBtPyLsXZN1aRVRep2pgSMxgD1zr7T8gLblrhx-e7pLQtN-oNRI6k10Mgx6GOR2GHUVn8fjhEv9FZ6uxY1VzTlkMxSEV9w7qH9wMIBqfpo_VoXyY1kpD0iWp0kSkYXWatxt5v1XX1RPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بارسا به دنبال ادامه مسیر بردها!
⚽️
رایووایکانو آمده تا کار را برای کاتالان‌ها سخت کند؛ نبردی برای صدرنشینی جایی برای لغزش نیست!
[
بارسلونا
🔵
🆚
🔴
رایووایکانو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139316" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139315">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139315" target="_blank">📅 20:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139314">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
احتمال زیاد پرسپولیس با ۲ مهاجم بازی میکنه و بیفوما هم وینگر چپ هس تا پرسپولیس تو حملات با توجه به ۳ دفاعه بودن استقلال کمبود نفرات نداشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139314" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
کامنت کریستیانو رونالدو برای مسی:«لئو، توی این روزهای سخت، یه بغل خیلی بزرگ برای تو و عزیزانت میفرستم. خیلی قوی باشین.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139313" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139312" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139311" target="_blank">📅 15:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
تارتار نمی‌خواد ریسک کنه!
✅
به احتمال خیلی زیاد جلالی در دربی به میدان نمی‌ره و تیکدری مثل بازی‌های قبل در پست دفاع چپ پرسپولیس قرار خواهد گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139310" target="_blank">📅 15:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
فوری؛ هدایت ممبینی برکنار شد و با حکم مهدی تاج، حامد مومنی به عنوان سرپرست دبیرکلی منصوب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139309" target="_blank">📅 15:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139308" target="_blank">📅 15:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139307" target="_blank">📅 15:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt-LaIfOi9BB7W08rZc1e9n1L9_300DZyG8c48DHjGAABv2Q33wkUOnEjVVZIplklyWpv7g7bAjjtAiLLFHVNajx_0ISGPm-HEtODg8NC6tZ214gGrMaKGWw4nePLgcPAF1JcFLlpmbiGFEKC5wQYhWklCB6O8IWKfty3zIaJczcyHRJSTtpBnX0v7FK5c1f4LXF5EysmGnBvce7H-PqJZu6cJhGG-zQZkoZuoo-AtBBDbv5Lgdga7WgpRlsVCpuU7DithRK5Kw5_t-1Ya1yXQNt-6rvJZReoqLW58zLjSoQtZij8rFoxjsxbR2QjLt6wzZRrLPwywoucmCcqKEQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
ویلا پارک آماده یک شبِ آتشین
🔥
استون‌ویلا و آرسنال؛ جدال قدرت و جاه‌طلبی
اینجا هر اشتباه می‌تونه بهای سنگینی داشته باشه!
[
استون‌ویلا
🔴
🆚
🔴
آرسنال
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139306" target="_blank">📅 14:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
حدادی قول داده فردا صبح پاداش پیروزی مقابل ملوان رو بریزه به حساب بازیکنا تا قبل دربی انرژی بگیرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139305" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139304">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
‼️
بلیت فروشی عصر امروز شروع میشه که ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به صورت ۵۰ ۵۰ بین هوادارای دو تیم تقسیم میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/139304" target="_blank">📅 10:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139303">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووووووری
🔄
🔄
با اعلام باشگاه استقلال بلیط فروشی دربی از ظهر امروز آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/139303" target="_blank">📅 10:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139302">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
بلیط فروشی دیدار پرسپولیس و استقلال خوزستان شروع شد . از طریق لینک زیر میتونید برای خرید بلیط اقدام کنید   https://footballeticket.ir/buy-ticket.zul;jsessionid=23B55854CCBC6E89F276AA81C2DC01A1#  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/139302" target="_blank">📅 10:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139301">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
ممبینی : به عنوان دبیر کل فدراسیون فوتبال تا الان نمی دانم چه کسی گفته است که تورنمنت سه جانبه برگزار شود/  هیچ کسی هم نمی گوید که من گفتم و اصلا نامه ای هم در این زمینه وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139301" target="_blank">📅 10:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhrABwhDU8J2Wene1s1xTBIx2MeCoPhi-GFptFE53LhKBkmyArb8MInBwFT8k11tTBh-hAXhYsIpSwWVj0cv_JfjTpY4vVgGVZhWl19DxURPBpa1GfYwrBGJB6HW9Lm976IkX8JNI1rl0X3HHR7EZlpOMF9LsAiu3BwyUQmTqkX-AGsSTgYTF7ksWK9v_tp68lsjO3iO069wBVars3ddqsiXbVUaWKXFpBhVh9UxXDziQBY_qapxN3PX01xpiq15pdXcX7uabASS2c64406XcGMoRdOPx4MaS8bu4LE_5_SmnIuHULH6XIyM3OzR-4ywhsC3GW0TwAgdbKMITbbxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139300" target="_blank">📅 10:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139299" target="_blank">📅 10:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
از هتل المپیک خبر رسیده است مهدی ترابی ستاره تراکتور به علت مصدومیت ادامه فصل را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139298" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
چند دقیقه پیش تهران لرزید کیا حس کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/139297" target="_blank">📅 08:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139296">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139296" target="_blank">📅 08:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139295">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ..
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139295" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139294">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad7r2biA9mToy-v50UX7ff5oJe-p4XZ05_04LUouDi4P9FBmY2pqkLdQDS1b2zDuUjICUkplBCSqOSoIgdW6TFfTCjqa4VmIh5rTaDJMlYR-Fy7sgOPIJqDgN2k29IO4_KO4QR4ZNAHd8QLaleRC7F50OViAJgQKw_T9OZVUXIhRts-rlplFb2_6aYpPZF6sTNV0JDcmJ-zriX6Y9cPyxu_6Q23eLTerZuExFvBELLE9ZjgYAS9tHeTy2D0CLZRAH5ifs28PBXT8oz0YyHB6oLEygO2gABzxwOoT3RYUDarhzW3IN5H3sE1nFW0YAnit1dGfTUAndTFji4R1pbn2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک شروع شد!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/139294" target="_blank">📅 02:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139293">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
سپاه پاسداران انقلاب اسلامی :
🔴
🔴
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/139293" target="_blank">📅 01:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139292">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
قیمت دلار برای اولین بار در تاریخ به ۲۰۶ هزار تومان رسید  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/139292" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139291">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139291" target="_blank">📅 01:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139289">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
درگیری ها بین ایران و آمریکا دوباره بالا گرفته و درصورت تشدید تنش، احتمال لغو دربی زیاده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139289" target="_blank">📅 01:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139288">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💢
💢
💢
احتمالا دربی پایتخت لغو خواهد شد .
🟥
چون پرواز ها فعلا لغو شده
‼️
گفته میشه در صورت تداوم شلیک موشک ها از سمت آمریکا و ایران هفته پنجم لیگ برتر ایران به تعویق خواهد افتاد.این تعویق شامل دربی هم خواهد بود
⏺
همه چیز تا فردا شب مشخص میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139288" target="_blank">📅 00:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139287">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">💢
💢
💢
احتمالا دربی پایتخت لغو خواهد شد .
🟥
چون پرواز ها فعلا لغو شده
‼️
گفته میشه در صورت تداوم شلیک موشک ها از سمت آمریکا و ایران هفته پنجم لیگ برتر ایران به تعویق خواهد افتاد.این تعویق شامل دربی هم خواهد بود
⏺
همه چیز تا فردا شب مشخص میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139287" target="_blank">📅 00:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139286">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🎙
🎙
تمامی پرواز های کشور از جمله فرودگاه مهرآباد تا ساعت 6 صبح فردا لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139286" target="_blank">📅 00:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139285">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
فرودگاه مهراباد بعد درگیری ها تا اطلاع ثانوی و معنوی تعطیل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139285" target="_blank">📅 00:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139284">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQtuUyozTToWUmhGn8ZZR_gwAz-0xCzat9hg4FcoEhlQUlJw6z7O_S_R4hynMW8oSatVx-UvtAwDfHHs018v6YPFAXxvXch79QDZ5ysR0SReO8Glwwggap5sjXlWKCXK3uV6TqFuSGnnqgkJbpmEvuhBXmYZVXiJExbDG-sf2-wacNNnELKPFnALN4IanjmBNRU_-wuLDRZFUTfwvOsgks_DjX_Zzerf154BpJCjA5sYdJRKWPL400cfvyHJh8FqLGMxKltlE88g2hbsPafUYoHUTTnVhYwJn5B9b6cV35HayKGo5l4D8tYhv1TH_J8rRVp-gxBIENrQrXwCl-aqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
فوری، با تصمیم تارتار و موافقت علیپور؛ محمدحسین کنعانی زادگان بعنوان پنالتی زن اول پرسپولیس در دربی انتخاب ش
د
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139284" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139283">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jocvaSsH7W_QMnzNOrBaG69Fi_BopKeDDfbD0xr50yPgKz_O9pd6SZGa_hbyjmjtpT4XDAP_jnMz0EDezP471W4U_MgU9oeTixk0mQfDs6d-lH7oMHpdXFgfc3UW3yFjSBlK6Gub7uiC5nwr--ZmQ4SI8XeGHjghvCwMvPjhrWic8_ILaBRw3FEMDHYt2qIFCCglVPz_ZgREV86-cskyqxh6SZcFyY--_Q_F6jXilRGNW0O-AEEWfWYTnjHv4pjzEKVTAP1YMPB2fPqxrqQlaREZrAja2Bc7QceYLMVTK191TvZaSS8r1rP9gafB9xijLEGj6BkVx4Eg3twZhbzpqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139283" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139282">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139282" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139281">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🟥
حاتمی: پرسپولیس در این فصل تیم خوبی است
❌
دربی‌ای که در ورزشگاه آزادی با نتیجه یک بر صفر پیروز شدیم در ذهن من مانده است چون اولین دربی من بود. ورزشگاه آزادی باید به این فصل می‌رسید اما این اتفاق رخ نداد. بازی‌های بزرگ باید در ورزشگاه آزادی برگزار شود. امیدوارم دربی خوبی داشته باشیم. پرسپولیس با مهدی تارتار عملکرد خوبی داشته است. همیشه هوادار پرسپولیس خواهم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139281" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139280">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚽
نورمحمدی: هت‌تریک ایمون زاید در ذهن من مانده است
‼️
دربی سه بر دو و هت‌تریک ایمون زاید در ذهن من مانده است/ هواداران دیگر مشکلی با حضور بازیکنان استقلال در باشگاه پرسپولیس ندارند/ زمان ما تغییر تیم سخت بود/ من پرسپولیسی بودم و استقلال را زیاد دوست نداشتم/ امیدوارم شاهد دربی خوبی باشیم/ پرسپولیس در این فصل یک‌تیم بسیار خوب و کامل دارد/ پرسپولیس در این فصل موفق می‌شود/ جذابیت دربی به ورزشگاه آزادی است/ اینکه دربی در اصفهان برگزار می‌شود عجیب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139280" target="_blank">📅 00:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139279">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ
: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139279" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139278">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❤️
🤩
کنایه مدیرعامل باشگاه به برخی رسانه‌ها:
‼️
این سفری که به ترکیه داشتم و چند ساعت دیگر برمی‌گردم، از چند روز قبل برنامه‌ریزی شده بود. خداراشکر همان‌طور که ترکیب تیم‌مان لو نمی‌رود، دیگر سفرهایمان هم لو نمی‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139278" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139277">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c73b4d12.mp4?token=IWcJ4zFtqb9-tdG8oF1_MpLQJjJdBfu8uOmnsdAnVx8duwnhtzW26yNRkLLN72u_vxNkYQOuTV5yLErQ_KnofoymZB2hlcs5dhfVYnVZBCdVEPywqPrE29IOjMABGJga_Tnaa05YtISU6JM3Uxob1_n0mAsh5omyo69N7RyR012uf44xnOlF1G8FCX7nNhawwO1opSMpvX1JK66OsKMXulXA_pFg2RxvFCfiDWW7vQAeH1Tfp2nhrk4L8NBpndEOTyEGFKzhD_EKC6fGFWBkANH0eYz5U3vkX8qdlw4GlJPqkyqeEo4lBJunYP1sFKMiSwtqWj_WGPdWQB-Vg5cw7V3jPieXPXSOLORuNhzKVqD_qRaHBlHPvW1jily68_vKEyhELItcK_ACWxI7qUqzVwx6mC7MY-41hgBlDOwrUvGWXzwvxa25Ce-u1OASkDCei5iD68GABd_1JnSaIP9oslbYxXgkk0F3_mvY68Qaegl_ggyDWhvidEfWnzUwIodyAACbjmM0SmRAIKEo-os-3umEEEj7Uygq-mkYhaPKQwAgboCyBiXPE9aOmeD0foTb4FF4nRekfVcUGl3DVnH5ilwhUQKwHg4Nnd2SmCs3RYReTZxlvdPSxdDQkDn6nAIMXUrQQoxQ7iaV0lAILJpyR96cF75nRtlWatr8FCGK3mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c73b4d12.mp4?token=IWcJ4zFtqb9-tdG8oF1_MpLQJjJdBfu8uOmnsdAnVx8duwnhtzW26yNRkLLN72u_vxNkYQOuTV5yLErQ_KnofoymZB2hlcs5dhfVYnVZBCdVEPywqPrE29IOjMABGJga_Tnaa05YtISU6JM3Uxob1_n0mAsh5omyo69N7RyR012uf44xnOlF1G8FCX7nNhawwO1opSMpvX1JK66OsKMXulXA_pFg2RxvFCfiDWW7vQAeH1Tfp2nhrk4L8NBpndEOTyEGFKzhD_EKC6fGFWBkANH0eYz5U3vkX8qdlw4GlJPqkyqeEo4lBJunYP1sFKMiSwtqWj_WGPdWQB-Vg5cw7V3jPieXPXSOLORuNhzKVqD_qRaHBlHPvW1jily68_vKEyhELItcK_ACWxI7qUqzVwx6mC7MY-41hgBlDOwrUvGWXzwvxa25Ce-u1OASkDCei5iD68GABd_1JnSaIP9oslbYxXgkk0F3_mvY68Qaegl_ggyDWhvidEfWnzUwIodyAACbjmM0SmRAIKEo-os-3umEEEj7Uygq-mkYhaPKQwAgboCyBiXPE9aOmeD0foTb4FF4nRekfVcUGl3DVnH5ilwhUQKwHg4Nnd2SmCs3RYReTZxlvdPSxdDQkDn6nAIMXUrQQoxQ7iaV0lAILJpyR96cF75nRtlWatr8FCGK3mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139277" target="_blank">📅 00:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139276">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdMEH0iPh4A4v-_P_-hBoGcFfG7Cx77B7rLZGdd6mYcTDCVCrzUrPGLcs6zXfVWf4JSzM1fEd3TPT58ZIOPPx2CJvIrxSUwh0yJw9gU18Av2qfqyMiK6Mjz-EVD0P2C0DyAeiSspH3IeC1ahKx2TaeTZLuu-vw5nHdJMJE8KExWvgOpxdEsFL7hIdKSCTgMZtBeKs-mjrYEe5vtldV7gN3KMaqFo-y_UYja5xBYy9H05ootx-XhVBH9MLNz8QhCdCb3oa8PQaETr6OVukKDs_W-sa-VgA344qFlcWBBDwpw3zgKQLc_IsWfgzYLCr1wCvDS9yBOElDFGv1zdMeTQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139276" target="_blank">📅 00:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139275">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqiSbQpa0jdtcNj6p4uLaNIasFmMKg_4gkOoeBcf8KurepyLVhAYxnV1zTmOIrXh5xlBd7Wawn1xs_sZuyt4WZNd7XNpQqcaY770oaQUnJTvf8p3JZ4uEaErCHew8YXYfl9HcOb8ZV41uE9vt0ymMGsBrSyPcjIE233hAU0AmgNBpgk-U4-LECYSQpQ_9hTV9CyfulxBNLipNsi2IKXQK1-77ZbGfQYlnaoQesflxVolIRFFm2DFJA9_e7qkNxALE2Sv1GS0iXXS9I7pAE5po10kW53ztCfYVVgkAL8huzvSjZw-wcMpDzdwn3AOffp9Lg8aXHOJH4Zjnsb2_Z9lDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139275" target="_blank">📅 00:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139273">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324bfbe3b7.mp4?token=RgOIDjh5yBdfHpq1Q2Ih8gXWirettl7cnut8mbxiycSGPXHZd7N7H9H8TskRL1HaU9O0ciP-VReLWQwugMlyxETn0OGM041PgoUlnM-4Q-Vccxmn3MW6S1GHG3rz68TPYxLP5g209EWr2hbPbV9QEMp8GoOUOPxkJ8b7Ma-I3jldxR-1LhEfddvsQ1WHoedqoMi7r8szSYNMVsOrCqNVHSekYqKJsePPuuacz2XWi5Ukn2gKNXNlof7hQL1m4-inUKvTI7F7O69glJZOtHGZunsPwQIi0ySeqLtOPEJzHFPudVl2Sfdv4MyOLNvARm3tQaQ8Y1nmKIoXGnpMI5gbZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324bfbe3b7.mp4?token=RgOIDjh5yBdfHpq1Q2Ih8gXWirettl7cnut8mbxiycSGPXHZd7N7H9H8TskRL1HaU9O0ciP-VReLWQwugMlyxETn0OGM041PgoUlnM-4Q-Vccxmn3MW6S1GHG3rz68TPYxLP5g209EWr2hbPbV9QEMp8GoOUOPxkJ8b7Ma-I3jldxR-1LhEfddvsQ1WHoedqoMi7r8szSYNMVsOrCqNVHSekYqKJsePPuuacz2XWi5Ukn2gKNXNlof7hQL1m4-inUKvTI7F7O69glJZOtHGZunsPwQIi0ySeqLtOPEJzHFPudVl2Sfdv4MyOLNvARm3tQaQ8Y1nmKIoXGnpMI5gbZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محمد تقوی، برنامه هت‌تریک در آنالیز فنی بازی پرسپولیس - ملوان گفت:
✔️
✔️
«حسین کنعانی‌زادگان در حال حاضر بهترین مدافع وسط ایران در بازی‌سازی است. از سوی دیگر، پرسپولیس با تعداد بسیار بالایی از بازیکنان در فاز حمله، به دروازه ملوان یورش می‌برد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139273" target="_blank">📅 23:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139272">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocGBGLJO2xiocZsuppejuBWVmcKCZFlDiCCtGlNyyWY9nW3WFEhCy5eq9Cj0neQHXsoPQMGJ7J-dGXS8C_chtL8CzK3_WvTDqdb6nOjXxmPRDVWbYQYxtzB9sZsgBsgQWjZ3wLBlKzgwWN6f9bK24_GPGvk688aXLTSxguqf6A2SfXAHudEP51vicB23nxq17AoAmkMtbBCz0ownmsDC48TihV8kPMY7kfvXBwHMIFCJT4nMp6q_b3_9_pLAF6YKLVO-Ie2x9N2PWmiV2EvjTHg3V3_d1lBdFyhXlB5d0D6RI2p8EhUrtnscFWWoMCAw-cTpCS4d0G30ZNaCvAooZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
وحید هاشمیان: همه اعضای هیأت مدیره پرسپولیس به جز یک نفر موافق سرمربیگری من بودند که به گفته خود آقایان، این عضو هیأت مدیره در صورتجلسه نوشته بود که وحید هاشمیان ۵ بازی بیشتر نمی‌ماند و امضا کرده بود. سردار دورسون هم به من گفت شما تا هفته پنجم بیشتر نیستی!
‼️
👀
وقتی فصل را شروع کردیم، سقف بودجه داشتیم، اما تیم‌های رقیب شروع به هزینه‌های زیاد کردند و بازیکنان اسم و رسم‌دار گرفتند، در حالی که پرسپولیس نقل‌وانتقالاتش را زودتر شروع کرده بود. بازیکنانی که می‌خواستیم را به باشگاه معرفی کردیم که هیأت مدیره و آقای حدادی گفتند شهریار مغانلو گران است، آن یکی پول زیادی می‌خواهد و آن یکی هم گران است! ما هم گفتیم گران است اما وارد فازی شدیم که تیم رقیب ما بازیکنان گران گرفت. این اتفاق فشار زیادی را روی باشگاه و همچنین بانک و مدیریت آن ایجاد کرد که تماشاگران می‌گفتند شما چرا پول نمی‌دهید و بازیکن نمی‌گیرید. آن موقع دیگر دیر شده بود، بازیکن خوبی در مارکت نماند؛ بازیکنان مسن از قاره آفریقا مانده بودند که برخی از آنها هم مشکل زانو داشتند و آوردن آنها فقط بار تبلیغاتی داشت و مالی و فنی نمی‌توانست به ما کمک کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139272" target="_blank">📅 23:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139271">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚪️
⚪️
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139271" target="_blank">📅 23:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139270">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚪️
⚪️
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139270" target="_blank">📅 23:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139269">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139269" target="_blank">📅 23:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139268">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139268" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139267">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
✔️
✔️
طبق گفته رسانه‌ها؛ به احتمال زیاد داور دربی کوپال ناظمی خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139267" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139266">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139266" target="_blank">📅 21:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139265">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔄
🔄
یحیی گل محمدی در لیگ عراق :
🔴
3 بازی
❌️
0 برد
❌
3 مساوی
‼️
عملکرد یحیی مورد انتقاد شدید هواداران دهوک و کرد نشین عراق قرار گرفته زیرا که دهوک بیشترین هزینه را در فوتبال عراق انجام داده اما تا کنون بردی به دست نیاورده است
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139265" target="_blank">📅 21:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139264">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139264" target="_blank">📅 21:46 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
