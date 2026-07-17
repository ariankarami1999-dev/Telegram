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
<img src="https://cdn4.telesco.pe/file/e8zjN7w8JGJmu-poBtrnMpWKpmwWog1meAAtnsUL6k1IMeQ0Cu3hUnYPL9n9b5sICKrH45WZZtowkTJ9aK03Aw3MNyNv43NRcIojLHQnRip_Qea52HdDg6E190xB4JHxhS4dohhosyv7-B3V_-Xcq2ATnjDMxarkmYCi-bMBFJneu6J0J5ONZk9p_9KEPtgXJYMWHG5E3fe2JmXIw6Hm6g_zd_ck6w2s7gVGJLWt28k8dMTcqMZM25p6MdfzzP0VWsLk1KyTs24TsngWq5uSNJveD_MBvqO-lX0JTqDpmGEbB5T3_Qxb9zc31gphFDKfid_PjoZCcWmCrd6kLVEwlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 23:29:19</div>
<hr>

<div class="tg-post" id="msg-136052">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
علی دایی فقط یک نام نیست خود تاریخ و افتخار هستش  نه فقط تو عرصه باشگاهی و ملی و فوتبال بلکه تو زندگی هم شریف و عزیز هست  کمک های زیاد به خیریه و نیازمندا کمک به زندانی های مالی
🔴
بر بدخواهات لعنت جنتلمن
🍸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 759 · <a href="https://t.me/SorkhTimes/136052" target="_blank">📅 23:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136050">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
پهلوان علی آقا دایی خط قرمز مردم ایران است
❤️
🔴
با قلب قرمز به این پست تایید کنید
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/136050" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136049">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
هرگز برا کسی که در حق شما بزرگی کرده و شمارو به مقامی رسونده شاخ و شونه نکشید
❗️
یا رب مبادا گدا معتبر شود!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/136049" target="_blank">📅 22:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136048">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
❗️
واکنش تند گداوند به صحبت‌های اسطوره علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/136048" target="_blank">📅 22:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136047">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
واکنش تند گداوند به صحبت‌های اسطوره علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/136047" target="_blank">📅 22:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136046">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJYZkNXqRID34DTqZeWZTHCmrOkB9Sad-DuMGkcGLs07klJ9NkhA9mLEF-2huvKAgWwpXg7LpbWem1B5D0WlIL6XoyN15vxQeDNnLah_lGFr5SZSxvniOUQXmG5P4uo7eio9xvnpeXV5x7tdnOTNCZYdrBWoM3nLlyX1oQun31TL1ZzJYyej2Uzv2u9ogovNgxt_X0T4D-s09ESMMeS7dBQrc8LdiW-axbcmiB8870U9o31eCRFKJa73WPxyElktN5AkoEbmZFjRjSNsTDc3ney1PlHgDlxDc1mi6PggB6ERDtV6jar4nFV5LFfeOUm_WEifsHoEguCZKTxRsGtX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
واکنش تند گداوند به صحبت‌های اسطوره علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/136046" target="_blank">📅 22:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136045">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
جدول لیگ آزادگان در پایان فصل
🔴
نساجی قهرمان لیگ دسته یک شد  مس شهر بابک به لیگ برتر خلیج فارس صعود کرد
🔴
نفت آبادان راهی پلی‌آف صعود شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/136045" target="_blank">📅 22:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136044">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1HewT9Rm5WtrWryAibSuFOM_Jv5G0IfsTNLQLgi-rEN69LNCeCoPDUfGmtuR2MTKkgqbWM3IqtFcdYxdbLNZxrj_0MVrvwUsuLi8p_XA7-k9YnqUX3PhkDqao0MdzgtzvHh0gPkHkZWZS2QDwkZG1vmN_2IQ62uQlaoCrO1GhurFcKDDV_P50O0LgM09LerHtmpEAx36jl4JoQou17NG5cEpeLzGF8_f0bKx9zGnV-ZBZxDhj3ZPRApEKoNROyUrc45TZHcnaIBhylYjvL2WA9DJgRnzRsnbU-mRHDc_13X0FAOcqxcty8RUk4t3Tjk6WOh7-Pq4Sq9VoaMJW4e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
مس شهربابک دومین تیم صعود کننده به لیگ برتر بعد از نساجی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/136044" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136043">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فرهیختگان: محسن خلیلی دیروز در جلسه با تارتار برای برگشتن پورعلی گنجی به پرسپولیس وساطت کرده که تارتار قبول نکرده حتی بهش گفتن بزار ابرقویی بفروشیم مرتضی برگرده بازم زیر بار نرفته تا پرونده این بازیکن واسه همیشه توی پرسپولیس بسته بشه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/136043" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136042">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKXoJoXXhO3qah3DMK2gXQGZkCLrsScu3xJWp__xz53ozoYHMpwQApBkPjRi68Uh1wl3wfxrK9LzAvoAg5kS-N7v2BUIg53g7J-zfAT4EzOwr_HsfvrOOCjXKwQUS6KA3O5X1mEBstiSuXiKik6CqhaTMchhNkZ0Nxcyc2sTTakMzZMBsqd0b69apqzJ894Gh0bdGpfps-ilXx_Ebb9Mitl53g3XncPon61omuJdCxmR1MIFrkiFf8cGQhXwR_23xZy8VvAC2XuIMumATFTdBYgxfEz5Mh4ImaEjR5c0KM1ioV8FoQ1cgHS2ZCLKE6w1q4q83x3XxTwEJkRik7LY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
تصاویری از تمرین امروز سرخپوشان با حضور اورونوف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/136042" target="_blank">📅 22:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136041">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHfJe6cPa6kI7z3M2U2znx9mQTPYvtdpegrTDsDBd45JnpYWah7oThxS2YluL2rQg1-vhMhpBD3yeB_8N310t4s1Xcwumbz1u6rcuFbGzaHs8dv38MB8KEQNS17IR9Xl9Ux5ZuURKC-Ns3lZFLm3jZIQu5S9NLCuuSrsKDHotwZzSw8e4W1lO-Keick6eON28K9RyhdycPwUO4gf7n-xyfQyRFMtCgPX1p-TY43_2ot1tVvO3YGMXIF-xT7Dxr59nvMvb0kE-kTGRYRDZMWI-I3fz3lRVSzcZId-nKWsyD9wAlthmZJtuLrVqfbjztsFcdtlB2EVmnhmkhMoLvCyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بمب پرسپولیس در آستانه انفجار؛احمد نوراللهی به تهران بازمی‌گردد/
طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/136041" target="_blank">📅 22:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136040">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
اورونوف صبح امروز به تهران اومده و بزودی به تمرینات تیم اضافه میشه
🔴
مهدی طاهرخانی
🥇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/136040" target="_blank">📅 22:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136039">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyE_YAzhrOqArP34FUtJGyZhkuz0rzzXSuK3Hrz1NppYVF5htkI9BJQg2ikibw5eFWFF4PuJhSjHc82LzM4r6qjd5QhrMVHI3NdFumIAk5nTQKATLFwnqM0iiw5s-vVwDPAkqZnLoYSlxPq63DdE8tXnqwzvsLPwzCJKdVt3im-2DTklCfFnSNs2dzh3y70UInHe81DUxQsnN15ccv1_0SouU9fiqew-jcpbhUCM2G09wd-a63OwJ_PCBkIUvMv55zr1xCFJ3KKiMqSjQZvNOGM_kKbA45FFNRk-UmXMp_Po5ZU8hCdgbT5-xWiopOTyeTzxw3nKWdTG3KEvzJynEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
عجیب‌ ترین بازی سال در لیگ یک رقم خورد، نود ارومیه با 7 بازیکن مقابل مس کرمان به میدان رفت و بعد از مصدومیت یک بازیکن، مسابقه به دلیل کمبود نفرات نیمه‌تمام موند و با نتیجه ۳ بر صفر به سود مس کرمان اعلام شد. این تیم پیش‌تر هم یک بار در مسابقه‌ای مقابل بعثت کرمانشاه یا تعداد کم بازیکنان حاضر شده بود
😂
😂
😂
❗️
❗️
نود ارومیه به دسته پایین تر سقوط کرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/136039" target="_blank">📅 21:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136038">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5faf86265.mp4?token=QluCx1qJguw3l9iy8yMuIOmZJsqaPPypXfr-ZahXJYzacWM_LwhCKefEco-Ep85lvU_KaC5d_ZLOftkDCUMguvr6lPSQYkGPba1wnK42kC8MyXPd4cz-mnIr5wVTdXAl2jbXkksvLAjc4CJVbNN_eR-khIyeMq_p79Dng3LpT-kMP95NV6Dx4VQi3tv6udb6sq6fpjFjkAgPf8RIkKidtu0LPTkXMjMK9u5wdMz2O1mUpIwW1kdLoBLUUuO-FDuGKbjTIPFPcTUm6Vh4hrdj249RI-Rhe0lJUBB1zs6e4-ODAA0oaasy7j1BHMBfOMgtw4qn-7mubL5a3bB-kKy9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5faf86265.mp4?token=QluCx1qJguw3l9iy8yMuIOmZJsqaPPypXfr-ZahXJYzacWM_LwhCKefEco-Ep85lvU_KaC5d_ZLOftkDCUMguvr6lPSQYkGPba1wnK42kC8MyXPd4cz-mnIr5wVTdXAl2jbXkksvLAjc4CJVbNN_eR-khIyeMq_p79Dng3LpT-kMP95NV6Dx4VQi3tv6udb6sq6fpjFjkAgPf8RIkKidtu0LPTkXMjMK9u5wdMz2O1mUpIwW1kdLoBLUUuO-FDuGKbjTIPFPcTUm6Vh4hrdj249RI-Rhe0lJUBB1zs6e4-ODAA0oaasy7j1BHMBfOMgtw4qn-7mubL5a3bB-kKy9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
میلاد سرلک تو اولین بازی دوستانه فولاد مصدوم شد و به نظر میرسه چند هفته نمیتونه تمرین کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/136038" target="_blank">📅 21:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136037">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
باشگاه پرسپولیس با وجود داشتن پیام نیازمند، معتقد است با توجه به در پیش بودن جام ملت‌های آسیا و اردوهای تیم ملی، به یک دروازه‌بان با تجربه دیگر نیز نیاز دارد. در صورت جذب اخباری، امیررضا رفیعی به صورت قرضی راهی یک تیم دیگر خواهد شد. / تسنیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/136037" target="_blank">📅 21:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136036">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/136036" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136035">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/136035" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136034">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/136034" target="_blank">📅 20:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136033">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJdpE02S6eTL_Yy9oAQFDEOT9Aevwmj2HsxyYESVQkVkLKGbmNWGs9rs1kEJKXoWWJSIAEYg_rp8qpE5ab-mds2vLX3gVshlOhhEHad5uUGfVYGRvKGkqcwFSAaB74N5wrc7bGb38zuH-ip8z7If2Jhg3l9T8OKN2SQ_YnEMF7jOvURL_butBpVWdIEWqUxEWDr8aGiqGYiuTmNImmkK2x85kAswx9k-p3rw0lamp4f08723x1XqwWx7PQP2J6f-EVTBd_KbFwEiTKl_rqNzlc88gFPwo061zmEffsYApDBregD_Jbmqj4GUVbF9Gb7omXlI0NPH5dVhx9Zzzd8qVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/136033" target="_blank">📅 20:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136032">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
باشگاه پرسپولیس درتلاشه‌که‌از بین مسعود محبی و دانیال ایری یکی روبه‌خدمت بگیرد و مذاکراتی با هر دوباشگاه آن‌ها انجام داده. امادرصورتیکه بر سر رقم رضایت نامه به توافق نهایی و کامل نرسد به احتمال بسیار زیاد قرارداد مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان‌پایتخت‌یک‌ساله…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/136032" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136031">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/136031" target="_blank">📅 19:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136030">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
اولویت در دفاع چپ با میلاد محمدی است.او گفته اول طلبم را بدهید بعد تمدید.باشگاه هم گفته کارها همزمان انجام خواهد شد.محمدی هنوز توافق و امضا نکرده است.
🔴
الترناتیو میلاد محمدی رزاق پور از  فولاد است/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136030" target="_blank">📅 19:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136029">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔴
باشگاه تراکتور همزمان با علیپور و مغانلو درحال مذاکره است
🔴
شهریار به مراحل نهایی رسیده اما با علیپور بر سر مبلغ قرارداد تفاهم ندارد،
🔴
علیپور درخواست قرارداد بیش از 100 میلیارد تومان از باشگاه کرده که فعلا مورد پذیرش مدیران پرسپولیس قرار…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136029" target="_blank">📅 18:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136028">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووری از تسنیم
⏺
محمدرضا اخباری در آستانه عقد قرارداد با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136028" target="_blank">📅 18:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
#شایعات
‼️
با وجود توافق میلاد محمدی با پرسپولیس، مخالفت همسرش با زندگی در ایران مانع امضای قرارداد شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136027" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136026">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
مهدی تارتار پس از تمرین روز گذشته نام کاظمیان را در لیست مازاد قرار داد و قرار است کاظمیان فردا قراردادش را با پرسپولیس فسخ کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/136026" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136025">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
🔹
تارتار کاظمیان رو گذاشت لیست مازاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136025" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136024">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💢
💢
💢
پرسپولیس در حال مذاکره با محمدرضا اخباری برای گلر دوم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136024" target="_blank">📅 17:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136023">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hseZSkSQLX-z2_JVyUw8MTdDWCtwH-OmEM8YxtX01XDnBxEdKcLAvD6NZcCybpCSh5t-fvsHyzpeqsviN93JqP8319wx_EDtNcABcJ1iY293k_5oXVK92tcPY8C5jRufWZqezrvPO7QruuswPGMYbPM85kdXdSoxMQ6F_wA6kZL0HQgeOS6ZDqkOf5bxwtv0EzLLPfoJt__Jn258uAfv3XzAFli5_WKNIF_DxemE_Vwv7dW5YU8sJhgw6FmaiTweQ4qCKqXURo8cnRy6okruaiBlcR49ABO1YryP2x9mM8n7rthM4g327_mWuqVw9doNlAC-22kA6F1sAUM2hXFc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
رسمی؛ با توجه به پیروزی ژاپن برابر بلژیک بقا ایران در لیگ ملتها والیبال قطعی شد و حتی اگر دو بازی آخر خودشو ببازه سقوط نخواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136023" target="_blank">📅 17:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136022">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/136022" target="_blank">📅 17:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136021">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136021" target="_blank">📅 16:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136020">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
❗️
جذب لطیفی فر کنسل شده است / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136020" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136019">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
تسنیم : سامان قدوس در لیست خرید پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136019" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136018">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKkUVEvPzRmFtDlmGolsrb2biz7JOz-0AL-udBxX24V6PBFaVIxSuutiE2muOCQjCNV6IHHz-nVS-m5wMeMiFzyxWVB53OL9WMS03uXjHWidfsBfbrf9Uhm9bgFTqPX6DiVHvvq1ZoLg6N4RA5V3fXkrYbCiB6GNIxdRAf_6odxJdqr2JG6xFpZyOWaU0mBXmeYc1SgewpSshUGQExmf00FhiarWNdkJr3WMErC0r1npOkOpUrQuNqeG8g4vgZJDehPRsBca7OKMOFTOAhrPtyKaeKsmTjFvP0m2jOI7YpNyAGJmdIRFgWedXLgU8Zhwtb3k8NuiMv2pOVUuVupH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تو 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136018" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136017">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
تسنیم : سامان قدوس در لیست خرید پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136017" target="_blank">📅 15:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136016">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
❗️
اتحاد کلبا رقم‌ رضایت‌‌نامه سامان قدوس رو 500 هزار دلار تعیین کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136016" target="_blank">📅 15:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136015">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
با جدایی سرلک، محمودی خواهان شماره ۱۰ برای فصل بعد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136015" target="_blank">📅 13:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136014">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136014" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136013">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
چهارشنبه هم گذشت و اورونوف برنگشت !
❗️
روزهای پایانی هفته گذشته اعلام شد اوستون اورونوف ۲۴ تیر ماه به تهران برمی‌گردد اما هنوز خبری از این بازیکن ازبک نشده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136013" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136012">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136012" target="_blank">📅 13:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136011">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
یا تمدید یا خداحافظی!!!  فرهیختگان: میلاد محمدی باید سریعاً تصمیم بگیره قراردادش رو تمدید کنه یا بره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136011" target="_blank">📅 13:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136010">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136010" target="_blank">📅 13:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136009">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136009" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💛
آپدیت جدید اپلیکیشن اندروید MelBet
❗️
🎁
کد هدیه 100 دلاری:
giftcodeir
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را فارسی کنید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136009" target="_blank">📅 13:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136008">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💛
چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت
💰
هنگام ثبت‌نام با وارد کردن کد هدیه giftcodeir بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136008" target="_blank">📅 13:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136007">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDubhqieHusD9iXTe7sjA9BEmThlYsnLoNtM7jkn4i4gn-Hwu9TZ_BfGey6Ar2uy8QAhzE6SFtNRtMBxqmoz7hYPpYcF7Hy2mpL9HVECfQZwmUW9CMOI0WCHY6y4uVlbl1l6eS-vCJcATMXWpgQTynZcN1qEGvNnF1zl_r6BKjB86EqxrGvl1EXerZbWQluw1q3okWPo_-DtjmeBEZIgt23EP1fndA390xlCLNXIx6PlJwsS_EBpKrHfUZVMJOea6rMUfmT8eWGOEg7f95GAnTh7V-0pn1QUii3tN6ArEJO-p-WWgerMUW_FauHpSDXsvP_lgVjzE4qxIiu3IW4Y6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
چرا هیچ خبری از این بنده خدا نمیاد؟
❗️
حتی باشگاه پوستر خداحافظیم نزد براش
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136007" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136006">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rn307HzyPambmI2vuDirEUHAyX4r-JSPJx6cHpetnLcL5PUUhjeRJvvRp7FuM2eArBxvJrpPQvs5hB6UmoVD3qPPJWbnfnhjiFt_gvNARnwdBqRgmFarmpjBSfN6McchcwMtKjI7Ng9yW7ZLJPimIwdnJhqDy_eLiwekXO1EhgPKj8LHDI9MyYehhPu7TTatxUG5LkGxZKR3eGcnmsQK8rWWcAineJbdzIGZnD40Qpfywpp0KQslvhP_RPLRRZWdBR2QHL5jqw-GPUfLk39I8XS-ApKYMgPj4Ga8cNH-U-opweD20Ka-ecFytURb7CjwGDWRd4feUJaLVS0RRryDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
/ فرهیختگان
🔴
با توجه به بندی که در قرارداد آسانی با استقلال وجود داره پرونده حضور این بازیکن در تیم های دیگر در لیگ ایران منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136006" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136005">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
ابوالفضل قاسمی به پرسپولیس پیوست
❌
#پسر_پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136005" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136004">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE5euWsGvdTnE8Pj4V4meK77S7ysyt9wSY5pugLxzmwpK3D4BXOBX1Ieq_sVKnPSMkB-sCeeiWbRlnYmdwwvmHAVwRTKOw3cbuEuluyxNT0YulpuoS6cE39WY6_w8eWQwTAWRxdZTXf89ZIW2dRAWrZk3avEa2FKpyzxX3VtTDWRq90UoVgupQtSUqbXmMoChmY-k197pZagRy_flzm1SkvKJ6U3UqCf5TYzIuHEiRXRVwoA_nvdYNJnmFGIa-t6N7CIcbspsvqqXW6YRVMbnlV8d4657wcpMZmbi6uErAvxu_5DtDJN61Db6jSwer_Myr0cgxGJfmOd6YyJT9tUUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل قاسمی به پرسپولیس پیوست
❌
#پسر_پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136004" target="_blank">📅 11:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136003">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
برای این نتایج ۱۴۰ میلیارد پاداش گرفت؛ واکاوی پاداش تعیین‌شده برای اعضای تیم ملی بابت راه‌یابی به جام جهانی؛ رقم قلعه‌نویی، ۴/۵ برابر قراردادش!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136003" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136002">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
برای این نتایج ۱۴۰ میلیارد پاداش گرفت؛ واکاوی پاداش تعیین‌شده برای اعضای تیم ملی بابت راه‌یابی به جام جهانی؛ رقم قلعه‌نویی، ۴/۵ برابر قراردادش!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136002" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136001">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
فوری از سپهر خرمی: پوریا لطیفی فر به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136001" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136000">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136000" target="_blank">📅 10:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135999">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
باشگاه همچنان موفق به فسخ توافقی با بیفوما و گرا نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135999" target="_blank">📅 10:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135998">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
فوری از سپهر خرمی: دنیل گرا به طور قطع از پرسپولیس جدا میشه مگر اینکه به لحاظ مالی به توافق نرسن چون سلطان یه فصل دیگه قرارداد داره!
🔴
🔴
البته به نفعشه یه پولی بگیره و بره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135998" target="_blank">📅 10:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135996">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">📌
۴۰۰ هزار دلار کمتر از ایری برامون تموم‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135996" target="_blank">📅 10:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135995">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
احتمال خیلی زیاد امیر رضا رفیعی به علاوه 60 میلیارد با لطیفی فر معاوضه میشه و توافقات انجام شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135995" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135994">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2ZS4ybkbLd6PZ9xFrahPgdFQ1RB5P6Ns4_5sUMEkKoq6edVUvtnTfEXBhzSD2unyr5Jz_VCAwuVwG_cfVrKO8UYkwOXqyZOgFHuGhIhJWXyg3ThEXEqqTyWsNk8FP7jFPfXyHE1-PdRYiRRZvrRj9p8H_O8mHFj8rfA1_6SX1oDLvy5_kevAHpPKfmiAmmrM6RZnHAj1v1N5D9HvDRh0BZtxbeD7jlUdH-Ixcm_ILyQIQl4IqOQV6HdcemLslFJ45NacPr2eYoorHRKRmwstqwPUxC4Igb2vqD9CIplW3pyYMzoFHbY7D5t2hpoh2z1f0sCFSQ2TYh2qy73X2A7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برج ۸۰ متری کنترل دریایی چابهار در طی حملات آمریکا بطور کامل نابود شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/135994" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135993">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135993" target="_blank">📅 09:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135992">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
داورهای بازی فینال و رده‌بندی جام جهانی مشخص شدند و علیرضا فغانی در هیچکدام از این دو دیدار حضور ندارد.
❌
بر اساس اعلام فیفا، اسلاوکو وینچیچ از اسلوونی دیدار فینال جام جهانی بین اسپانیا و آرژانتین را قضاوت خواهد کرد.
✅
همچنین ژسوس والنزوئلا از ونزوئلا،…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135992" target="_blank">📅 08:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135991">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135991" target="_blank">📅 08:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135990">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-zqq7f0BqT9Z5SsloMpCOIZqdQE5Xlo731x0hiQWiER_NXvVCJ-bdIUvOqf9qSbwtzIeTUieAVUICzBacL2qYsfBj0bJLMlYdMc09jg0tqzb_F45XYa97qpqTvmFxVUgO4eTeVcViQWZeElivyeRqursf3Zh_oOzbfJJ5Ae9BmcmUeSdhrwramwavauuo8DThJsZmrtuYYZ3p_7-O2NJsNPyPYLvhHDLyMK9O5xVPIuqAWmDII8qWl-u0bjdIXLRVO873OlU5Ek4qlxis_VqxHqkO4lqPSgcrxR9qQ7_GjMqwXeTvLDglPJiIGiWMmhFg-0IFIkZqgR9JbPH-B0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135990" target="_blank">📅 08:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135989">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135989" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135988">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izZ4FANtb55Pdc-0Q7lp5vTcYQ4NERQOM19aA8_ax9x5HdkDTDdQ5L5FDvQOk6bl60HsIP23pCO6_mcSfw4lcI-0kTO-cc2frr6zWQnDogy_hi1XbOGy8_-CaTYNFquuAB8_i0y9v2jPihor5xtM8SFvLPekS7MV6v5plTGc9vid5QhHm_3aDBk35935EVQcOkhvuX5JXgDttTjGkVhZGkhVjiSRDHFRvLEhQBQILGsV-wkjU0eY33-Tdrg7Ap7LMHmwwW1WVMN3cjo5b69vJ58sk7XngqtwzcmkrBaaF0Z539tF1hRtSgwpXoDP2TZ3O7pYNKO4muA1pPrKXPYMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135988" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135987">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135987" target="_blank">📅 00:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135986">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135986" target="_blank">📅 00:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135985">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135985" target="_blank">📅 00:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135984" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
✅
یه خبر نصف شبی فوری، شنیده ها:
🔴
برخی از کارشناسان حقوقی معتبر به باشگاه اطلاع دادن کسری طاهری میتونه برای پرسپولیس بازی کنه و باشگاه داره مجدد واسه جذبش تلاش میکنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/135983" target="_blank">📅 00:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135982">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135982" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135981" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135980" target="_blank">📅 00:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135979">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
آمریکا پل ارتباطی بندرعباس و شیراز در جنوب ایران را هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135979" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135978">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135978" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135977">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
فووووووووووووووووری
⏺
ارتش اسراییل: آمریکا در حال نابودی زیرساخت های جنوب ایران است تا به راحتی به آنها حمله زمینی کند و سپس به مرکز ایران برسد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135977" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135976">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
🚨
حملات در جنوب کشور شروع شده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135976" target="_blank">📅 00:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135975">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🔴
موج جدید حملات سنگین آمریکا به جنوب کشور آغاز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135975" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135974">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzW7u-92QN08Qz1RogHfT919hlTfFBNXADPpwouHiQ9lxrg4zqrAR4LowUeQIlhJpXRtU_fdOKoLrGIJK-rRg-nfWcuO_1G9W0lO7Z-trS2MtpJ1gJzJXgZjO5KbjWG8JI8NQOAwwF3amQPm6KXjn3B6I64nB5RO6K3RRJLaoPZ-_9HLQ9rCRazpvUPbRo2PfZ3uuAr2aAw95J68Fyz9stj_dBfXq6CCn0fvirdyjKBCnCp9GmxzMNOor1iovMgsu2nBgf_NC-0mmF_UKj4Ev-dlSjQt6WGj2kYe0sKqTHJIsUcH1LPrFAYX2WMaXUk-c6F98lAtVyQRuVoeR-8uIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور رضا جباری در تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135974" target="_blank">📅 23:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135973">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm8Wtg1hTD4WijhAfzKVwBq2qxL_8pFm-owC6ONab075tf5O_zWqXk9Z4C0W-E1BHWjExJ9E-6DN0aJIOi02ima2XheODOFZ8xlSpZ8xPjFfVN32RDF3jmaU8n9yIuNnTWsu8ETepXmlCd8O9P48QOTkdVKWU0gbeRIWlCj5Au1RmzeEOBdrSwZ0Mjs-p248EcA-_1HENBlinAtAlpzYubpmgbleOmKs242B2XIxHohA7D2dncHVbzG0Vnl6kHHYrwfN7NhRqE3tHelX_ZQ7Q8ApSPiGmnHKcChh9eW64X5brafNDtQwcyTULGIkEml4-qty-l6Fqunkg2WmlQEvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری از تمرین امروز پرسپولیس
با حضور علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135973" target="_blank">📅 22:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135972">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135972" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135971">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0Iy_CmbEFOVe2SPkVhPKDqawXiqwHCWLsMPl1CSLZaQzOz8uMRvuiBLkXQikZsasT1B_zFi-TkSwW61GkTHGQsFeOFQufbTRQeO-M8kQApHlKb8NB0a9YaNPdi1p2E90aPrz1-OlIvzUz1KRomzf6_dD8jmh7thi20nAN9f0_IVw8SFnuzo3ncg26z8vnbY7VL_K_IfQe_N4Do0K3MGBxKAM7IoDC5y-xbRcxy3to8wJIMDxEMtEaSOD2Siv8M9iGftsUnEDNKN94dDP9zGAUOng1EwiSQ5EW7lLwe_6lDi3jTJwsdGmClfUtiQNLzdWrnW3uJDNn-Xrr07TN5E3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135971" target="_blank">📅 22:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135970">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
صنعت نفت آبادان با برتری 2 بر 0 برابر نیروی زمینی در رده سوم جدول رده بندی ایستاد و حریف مس رفسنجان در دیدار پلی آف لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135970" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135969">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135969" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135968">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن با دو سه برابر پرداختی شون به تیم های دیگه بفروشن این دوتا بازیکن رو…الان که باشگاه با علیپور تمدید کرده و زارع رو جذب کرده،مدیران نساجی الان زیرش زاییدن چون سپاهان سقف قراردادش ۴۵ میلیارد هست، استقلال بخره هم الان به کارش نمیاد، فولاد هم بودجش در حد سپاهانه… جز ما و استقلال کسی دنبال ایری و طاهری نبود که بخاد پول خوب بده الان به گوه خوردن افتادن مدیران شون ولی با این تفاوت که الان افتادن تو فضای مجازی و دارن کصشر تلاوت میکنن تا هجمه وارد کنن، بگن ما موز میدادیم کیلویی ۳۰۰ حدادی خیار خرید کیلویی ۲۰۰ اقایون جای این لاشی بازی ها بازیکن رو به قیمت بفروشید که اینجوری قهوه ای نشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135968" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135967">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135967" target="_blank">📅 20:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135966">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_-YT7ghcyNP8B3ogivBIxrl1gbE8rRFRbFcH8ISmJfMLK4GLgeQFFk6_kTkRzD4HvczjSQz-mN08ddu0MVj_bcGsKcTbyYZdMeh-Pbr2GsrF2kkMb4DuniJPk4hxgfYC9Jkm9xO2X9mX3Q3jhKFAp0w6DpPJ6rQspoLbn58VlYO9dwq5r7RikSeRNyu9F9N2_xGbcmoXa26Am_qg3rLxjTu-i5CV7ckkbLqr6FCgj9sSG-4HHAcjLKqlLSYKqZz1dLfUT5Z9c0cmmEtYbsnJDzlDFhBWZuhbxJb_DN0360JIz21iWHuicQck3FU3e9y_bE_1csWN_BS6G3JpN4pNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه پاکستانی
😀
اکسپرس‌تریبیون:
❌
بعد از از بین رفتن تفاهم‌نامه بین آمریکا و ایران، پاکستان تلاش‌های خودشو برای کاهش تنش‌ها و ایجاد صلح بین این دو کشور متوقف کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135966" target="_blank">📅 20:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135965">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135965" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135964">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135964" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135963">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDVoIG9uFWqKcTs8FIS2LbRIZqSPbjz0UaTNrWO_n3jGDhG68ZOG4DNLXx-Co4kWdH_bvPbyXAScUF5HFb6WhqA3vbF3OR6P1Mm2Cu47Bj5DqGLr_o6pZIqdzOpS8e5tqIgt3e-9ng3dTa5dr8qDi-tMghC3XpQRylaIxyOzdND5mgw8mc6vMq59_VTtANTrgKisRnXQ7gTerocsOHhDI3i2-jQ6fLIGQ5dnVw-Vb-dzQ0_Mv3idNXpQgaBPuY5dvmpVRVtEBZth1VyW7SS1gG6IFlLH1jmibwdPuDOxSKGYqAxJO-LDJUXasw-xUi1O7c2YalKZiUMa2kRljCJLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135963" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135962">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPdd88tbxrji3x16qtfdhwB9V4qvKg7l99kKGFLMGcG5NQUNcwhnPNWwMeodFtDpCFreUlijUVakFCgh6-XjMZAHPyt8k2thWbtNYs6mR2gGlow46Qy3uDY5dCgKr8VtYXiOaboEAfyMxrr0cDAm9c_acoOy5GRNCK0sAId4--WTfDi7DZiWniDLn28sC93V6ZL1hRqHUVv0BkwF44X4jbbFtKacjetZX_h0TvI2RaItPxmhYO4l7LUZnmIobezPx4ZiTFmHTUv_436WN20RLlnRrmB7C5NLklE1NrHmdHM0k4bnU1D0ik8-8OumjXzoC2jbJcy0LvkgaP-EdZF_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم ملی والیبال امروز تو یه بازی جذاب 3-2 مقابل آلمان پیروز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135962" target="_blank">📅 20:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135961">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135961" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135960">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=B8eG4mhb300iXezVwD1eURbMZQsoH2wYnXiezzNAJQS9rm7RVwYqzS0jTmoOXMfzgIce_WBTLjc60NhucVHyO81sUwnp7xl4guArF1Zp9SqXn7NvwBOABqMr9kpi04cRGpVVEqQYnENKXpeFcjmkbmSmQc5VetkGZOmSEqfUVskwXae2wyRU09qxsDOJtl2BXvOcp0rse0h95M0XaIuUeY3xwBDo-8asaYzHmT1bBbXZaD5NvY85gdVri42zBp8HY-pnJCGAEpsrlXo3d_lqMGdGLV2CbVyqQNLfnFOAPTGu9TBHM-Gky6nUWDz_pngWNSg5DSbOmg_Lvig5WN5YlnyTCHbgm8Qhf93yizg9Yz6Brqmifh5MjZgEizeCYG4HoYTD18wxl9QvqSx178ts0QG7oGxvv3YgJHFd29pkbTMyn2bNx8x2yvf9B9ZaJCsMed0uW29ZOPxcJJCl1MgIu8zpImSLDp6y6ogXEU38FE5l16Cc5AcHPaesaTDaWFGgITrutdTHxmrDakHzkepPdGPR3aLx_JaeqKhdf4rudFB9krtWFK-ipiE5F0n3PNcygcNuy2ccVI2p3z82ipXsGPa4ylClCMpVTxlBmIxv-EwwckLegw-HM6r8eZFK6k2ncL-ZAf3bNvICXYkAhi4qTx86vz4XDlObGRWzfEaCuhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=B8eG4mhb300iXezVwD1eURbMZQsoH2wYnXiezzNAJQS9rm7RVwYqzS0jTmoOXMfzgIce_WBTLjc60NhucVHyO81sUwnp7xl4guArF1Zp9SqXn7NvwBOABqMr9kpi04cRGpVVEqQYnENKXpeFcjmkbmSmQc5VetkGZOmSEqfUVskwXae2wyRU09qxsDOJtl2BXvOcp0rse0h95M0XaIuUeY3xwBDo-8asaYzHmT1bBbXZaD5NvY85gdVri42zBp8HY-pnJCGAEpsrlXo3d_lqMGdGLV2CbVyqQNLfnFOAPTGu9TBHM-Gky6nUWDz_pngWNSg5DSbOmg_Lvig5WN5YlnyTCHbgm8Qhf93yizg9Yz6Brqmifh5MjZgEizeCYG4HoYTD18wxl9QvqSx178ts0QG7oGxvv3YgJHFd29pkbTMyn2bNx8x2yvf9B9ZaJCsMed0uW29ZOPxcJJCl1MgIu8zpImSLDp6y6ogXEU38FE5l16Cc5AcHPaesaTDaWFGgITrutdTHxmrDakHzkepPdGPR3aLx_JaeqKhdf4rudFB9krtWFK-ipiE5F0n3PNcygcNuy2ccVI2p3z82ipXsGPa4ylClCMpVTxlBmIxv-EwwckLegw-HM6r8eZFK6k2ncL-ZAf3bNvICXYkAhi4qTx86vz4XDlObGRWzfEaCuhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چند ماه قبل پویا پورعلی به پرسپولیس با پیراهن گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135960" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135959">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=EhE6NM1nS2TH7D1R2xoRVl_7eEVOkgY8R1dSfoYsD0L34UU1ahGJlzFJ6mP5rDGcAvkmafopTA7iUSCdbBFsvANEtCF_V4tdRpaciTTIzhQHIVO6qtY62AeQoctwu-F2RAsaf6m-yU194VB4NNMEMCCVVUoBAAAaBJVcVBnYWlsbz_MUmvv0WXegBjuuH81cEkhQkOwfEfGiNKaZePom7Y5swOBv7LmDFNpFCgrr_0bTElvl8dx_gL87z4u-47cx-z_DQ_8LgDXKDsDb2nI_07SeFzN1_epB18piiHDQrSwjCmMLRBAfYnvN0LKkxvOOjZ9-4VGWZApDw-3wwwqaTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=EhE6NM1nS2TH7D1R2xoRVl_7eEVOkgY8R1dSfoYsD0L34UU1ahGJlzFJ6mP5rDGcAvkmafopTA7iUSCdbBFsvANEtCF_V4tdRpaciTTIzhQHIVO6qtY62AeQoctwu-F2RAsaf6m-yU194VB4NNMEMCCVVUoBAAAaBJVcVBnYWlsbz_MUmvv0WXegBjuuH81cEkhQkOwfEfGiNKaZePom7Y5swOBv7LmDFNpFCgrr_0bTElvl8dx_gL87z4u-47cx-z_DQ_8LgDXKDsDb2nI_07SeFzN1_epB18piiHDQrSwjCmMLRBAfYnvN0LKkxvOOjZ9-4VGWZApDw-3wwwqaTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب علیرضا، پسر نابینای ایرانی اينجوری با گل آرژانتین ذوق کرد
❤️
🔴
گزارشگر اختصاصی هم داره که پدرشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135959" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135958">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135958" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135957">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
اردوی خارجی پرسپولیس در آستانه لغو
❗️
❗️
در حالی که تیم فوتبال پرسپولیس قصد دارد روز جمعه تهران را به مقصد ارزروم ترک کند تا یک اردوی دو هفته‌ای را در مسیر آماده‌سازی خود داشته باشد، هنوز شورای برونمرزی وزارت ورزش مجوزهای لازم برای برگزاری این اردو را صادر…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135957" target="_blank">📅 18:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135956">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
ورزش سه: تارتار به وحید امیری پیشنهاد داده به عنوان دستیار و مربی به کادرفنی پرسپولیس اضافه بشه؛ اما امیری فعلا دلش میخواد بازی کنه و دیروزم داخل ترکیب پرسپولیس قرار گرفت تا خودشو به تارتار ثابت کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135956" target="_blank">📅 18:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=RneHA4EhpPI2gLyiWnuPX8itwjOyTMuLjp769LTDjoccnsRrw9SIYw-wG64Y1cTF7-DP4WiylCWY4WiYNL6lImoJcEiUh-eLEnbAISchbHe3fQPinqSRSnS7p_S4QDSVtkaVCcAsjteaKaYFJX3oqFqnvINj2otZdPITUKtyAOC1vlPezVE25lFJly5fEAB-6ADgo-QlSg6AFWdtVzw8Hi3iqieUE40vYk9-pvI0K1CwN-OWUPx3usg2xBkX9NgwxWbxaJ429-KEQsBxYcPMmQ70UPVJ72pzGuPoLMmqvwF65amNLvfOVN-xDec0b0Hjb-gqI5HM6_gV0sO5NDw2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=RneHA4EhpPI2gLyiWnuPX8itwjOyTMuLjp769LTDjoccnsRrw9SIYw-wG64Y1cTF7-DP4WiylCWY4WiYNL6lImoJcEiUh-eLEnbAISchbHe3fQPinqSRSnS7p_S4QDSVtkaVCcAsjteaKaYFJX3oqFqnvINj2otZdPITUKtyAOC1vlPezVE25lFJly5fEAB-6ADgo-QlSg6AFWdtVzw8Hi3iqieUE40vYk9-pvI0K1CwN-OWUPx3usg2xBkX9NgwxWbxaJ429-KEQsBxYcPMmQ70UPVJ72pzGuPoLMmqvwF65amNLvfOVN-xDec0b0Hjb-gqI5HM6_gV0sO5NDw2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فوووووووری
:
🔴
ماشاریپوف و نازون از استقلال جدا شدن :)
🔴
پ.ن فقط از استقلال ی سهراب مونده همه رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/135955" target="_blank">📅 18:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
اورونوف چهارشنبه‌ وارد ایران خواهد شد.
🔴
پیشنهاد ۳/۵میلیون یورویی الشمال قطر صحت ندارد.پیشنهادی باشد هم با میلغ بسیار کمتری است و از قرارداد مالی او یک میلیون و ۴۰۰ هزار دلاری با پرسپولیس بیشتر نیست/قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/135954" target="_blank">📅 17:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135953">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135953" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135952">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df7S8NgqK02e2uDydrlbW4w3uHY_58tdTn69BUaVWTlj47c_4uZBUu38aVilJl2sPx2u56EVn-cs-eSXw55IhFwfrL41EnR-Oe5SQUH7n1A9tp_CEp00aKCDBGlwOJ-qRtjXkrUIrMiZKmXdYljNE-07ClVTLVjY5vXGeyq5ZAWtyeFev1ua9_x-DCDtNJKm4dMZvMDwjAYkNQrb8Zp9i9wdV6Zo2m_nZfzZIHGn5GLIDSDip9JBWGaFILzcKoXQB3gnOa94m00PsOk1OoQWP9_RuvTkHgpkSk40sAGMtfqM81oQrOXb1yk4dRhYSnrd0yKpiNaIdjKLhEXyfBbjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل جلالی بعد از پیوستن به پرسپولیس یه میلیونی شد
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135952" target="_blank">📅 17:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135951">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری
هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135951" target="_blank">📅 17:26 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
