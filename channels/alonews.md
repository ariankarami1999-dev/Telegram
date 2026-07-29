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
<img src="https://cdn4.telesco.pe/file/uY-NJy5aX6_IqawzALUZWRvW8UT_wjYfLj7vF5MtjvImJiXn9QHV1oBolL-j9sGN9TMfeQabH6eUjCUHpfCKA72Avr7eY-V_etHhNwCtn2787CMAzlOo7ltq8Wss_26SnJFXjJJkV_Jk-L1_mD5KOE9jDvWSYxBhtahc15vcW5zwjlIoIQpMdxvog04vRRgQLPuzsk0SKc1tHB-Q-zdjYndrhQR8kBnTwQ_eYlEFF2nE1nywKPpf7wRaWim3sQEYx9cP0Lp0lYYtCHCA__KNi9C2BCV9WzLVJqy70X3RNPKRIw3jk2l8pmQ7XZ8nQkdcNiAlUXDa8ptNF171hM8BDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 20:16:35</div>
<hr>

<div class="tg-post" id="msg-138492">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7b1b38e0.mp4?token=kDuZa-fBGDUOU1vTH7oH3r73tEBnCFGBOrbe8gcz1zjm5MCV5Qyyb_feebBYjIfF5pb7yikNlmFQ42uB1Jf7kxPUBHJLVjUQqsnk9DRl7hqLHJ54UifFrZxYYiKlzwrNfa4Rozwo4BWpOOxqZDN_qdSzgH8Y6WUFVzIhmJ0o0w7NndpJD147XzuYL4uXqcoUuZWn7V1oRUOXmTMKkFusXpjSKfmEE2G1ywQJyxyD7u-Eq4XMuzUBkasMsi6lqkqKL4U5qF6wG4MOPVl5OGPai4uKhO3bszTmt4tOVCgbA0ESuKrKPBgbht-jORrGHFgObbWRvJPt3PAZLq7h4QTuWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7b1b38e0.mp4?token=kDuZa-fBGDUOU1vTH7oH3r73tEBnCFGBOrbe8gcz1zjm5MCV5Qyyb_feebBYjIfF5pb7yikNlmFQ42uB1Jf7kxPUBHJLVjUQqsnk9DRl7hqLHJ54UifFrZxYYiKlzwrNfa4Rozwo4BWpOOxqZDN_qdSzgH8Y6WUFVzIhmJ0o0w7NndpJD147XzuYL4uXqcoUuZWn7V1oRUOXmTMKkFusXpjSKfmEE2G1ywQJyxyD7u-Eq4XMuzUBkasMsi6lqkqKL4U5qF6wG4MOPVl5OGPai4uKhO3bszTmt4tOVCgbA0ESuKrKPBgbht-jORrGHFgObbWRvJPt3PAZLq7h4QTuWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تشییع جنازه شبه نظامیان حشدالشعبی در عراق که دیشب تو حمله آمریکا و عربستان کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/138492" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138491">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: نتانیاهو نهادهای امنیتی را برای تدوین طرحی جهت انجام عملیات نظامی در کرانه باختری مأمور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/138491" target="_blank">📅 20:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138490">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کانال ۱۱ اسرائیل: در آمریکا، از اظهارات کاتز، وزیر جنگ اسرائیل که فاش کرده بود هواپیماهای آمریکایی از اسرائیل برای بمباران ایران پرواز می‌کنند، خشمگین شده‌اند.
🔴
رئیس ستاد مشترک ارتش اسرائیل، از آمریکایی‌ها عذرخواهی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/138490" target="_blank">📅 20:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138489">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نقدعلی، نماینده مجلس: یک نماینده مجلس به من گفت از درد بی حجابی در خانه گریه میکند !
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/138489" target="_blank">📅 20:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138488">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نتانیاهو : سفرم به آمریکا خیلی عالی بود
همه دائم از موج نفرت علیه اسرائیل تو آمریکا حرف می‌زنن
🔴
اما شاید از موج‌های عشق و حمایتی که وجود داره خبر ندارید
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/138488" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138487">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
بنیامین نتانياهو: من همین‌جا با وزیر دفاع، پیتر هگستث، گفتگویی را به پایان رساندم.
🔴
او نکته جالبی به من گفت. گفت: «ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما توانایی آن را ندارند. و کشورهایی وجود دارند که توانایی را دارند، اما اراده را ندارند.»
🔴
او گفت: «فقط در اسرائیل است که ما هم اراده و هم توانایی را می‌بینیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/138487" target="_blank">📅 20:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138486">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI0ZL81ywTD9N_H39XsJwj_GmnKcuIdYSPl5H486r5B2V_ddlf86uZQi-oJ7hHmlTL6Yej0ocRlDFYtstpHwfk_9LZ6vuPL-jeZI8y9I9U5XTkWTUBshAO894nRf_nvSn-58CifmrOKLwKkJjDXptQYADUEDLOP7K33vvQvzwXHQXn_lIa63dGSil5YySoPnjLuIfkx2QenBDoNok_uyMdWYXujmyU2fHiALZXJCkHv-rp1Gp2Opr9vTtKjokiJH7zmiURyOv1RpouJf2PutAW57_YDqO3zESbh_1VnF5Vn-t65vNKHUu8wQja1-_GhnMHCulTVs6iL5ejGZusz2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتسب به لحظه خاموش کردن آتش کشتی حامل LNG آمریکایی توسط مصری‌ها در بندر دمیاط
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/138486" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138485">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc310ff270.mp4?token=nqjwmwa0-FZ5cgtRfCtawsGqaZmpG4u22VcQk8_lNF-TdE2pYxxclIJWAPBHFEnv4pvWTwirE2ESVfmIf9koaUws67128QI_ceEiTzgsxKfYCE5tmqWLIVqG-J0J6XoqaM3hRKIdDzV4kZyRTJH9naA3kL7gPD-Drd9lQ3vJ7uLGF1NItcKuuQe7CbA-A6Y1z1ejP_MfcG4dO1hPL-Gn1vRaJ3Ok7CE2_0t5DJtIaY8hBHZyrXq9P8kkSx9RichRLfIfflYo1jDKG2vgbjohc5gd-iWrkwprSq_MN9kmQS_Ollw2_ZyxmUY3KNRlUBCdbtI7o2Ls96MTfkCyVK4zXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc310ff270.mp4?token=nqjwmwa0-FZ5cgtRfCtawsGqaZmpG4u22VcQk8_lNF-TdE2pYxxclIJWAPBHFEnv4pvWTwirE2ESVfmIf9koaUws67128QI_ceEiTzgsxKfYCE5tmqWLIVqG-J0J6XoqaM3hRKIdDzV4kZyRTJH9naA3kL7gPD-Drd9lQ3vJ7uLGF1NItcKuuQe7CbA-A6Y1z1ejP_MfcG4dO1hPL-Gn1vRaJ3Ok7CE2_0t5DJtIaY8hBHZyrXq9P8kkSx9RichRLfIfflYo1jDKG2vgbjohc5gd-iWrkwprSq_MN9kmQS_Ollw2_ZyxmUY3KNRlUBCdbtI7o2Ls96MTfkCyVK4zXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کشتی آمریکایی هدف قرار گرفته در مصر
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138485" target="_blank">📅 19:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138484">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کوثری عضو کمیسیون امنیت ملی:
حمله آمریکا به عراق مانند حمله به خاک خودمان است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/138484" target="_blank">📅 19:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138483">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رویترز: یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به آمریکا و تحت بهره‌برداری این کشور، هنگام استقرار در بندر دمیاط مصر هدف حمله پهپادی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/138483" target="_blank">📅 19:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138482">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
الجزیره: شرکت امنیت دریایی امبری گفت که حداقل یک حمله پهپادی به یک تأسیسات ذخیره‌سازی گاز طبیعی مایع ایالات متحده در دمیاط، مصر اتفاق افتاد
🔴
تأسیسات ذخیره‌سازی شناور مورد هدف قرار گرفته متعلق به یک شرکت آمریکایی در دمیاط مصر است و توسط آن اداره می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/138482" target="_blank">📅 19:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138481">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بلومبرگ: ایران معتقد است که توانایی ترامپ برای تشدید این کارزار به دلیل کاهش ذخایر جهانی نفت و مهمات آمریکایی محدود است - ذخایر استراتژیک نفت اکنون پس از کاهش ذخایر برای کنترل قیمت سوخت، در پایین‌ترین سطح خود از دهه ۱۹۸۰ قرار دارد
🔴
بعید به نظر می‌رسد ترامپ تا زمانی که ایران از موضع خود در قبال هرمز کوتاه نیاید، عقب‌نشینی کند، اما ایران همچنان به دنبال کنترل تنگه هرمز و مطالبه هزینه‌های عبور است. مقامات انتظار دارند که درگیری‌های سطح پایین برای مدتی ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138481" target="_blank">📅 19:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138480">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqnz6sO-liifwUxtxawZlnIFwsy_3Bd2AvZV-qf8mDrikPhS4k05FcR1vqWP5_vCxOyBCaM363s3Qj82y79XgJTVVbRXkxbw7aMy9O9j3MypKs4EmN7TnsXbHCWRpCYnodO1SHCJAT-8pE97d8z3ZS6GoXreiD8QOpB1jXmJWiOPiix2K0rt_lkPSAT1Bwm6JPxHsKG3UUO_NpJoF2sqE0mldShEk2WAir875vMWM_v-bcPoapYjM8ImoDlXFK-Jrt-5LAfE21qdmkpiTNAcUe9PBVkP6rV4gpbOMAiHSUN0MB7YYgqglygrtheIAgCk0_FSVSxGIID7YvYBwc-qJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین: تحلیلگران هشدار می‌دهند که حملات مشترک آمریکا و عربستان سعودی در عراق، منطقه را به سمت یک "ناآرامی و بی‌ثباتی" سوق داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138480" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138479">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPO_ojrACqki-zlDuEnVtHJnnn2iVTFn-adHLvYGKvWIxnn-vD1iIkXOQ0NRGkQeY4WtnsH7qdR0W-HvmBT9ha2Dcpy5w_gtxzgpDwXHUunuuMJosvJ25H2zKoBLh8Z07xkkj_aC7fksulU8dGxDXuliq1lexmM9uV8A3bFVmCDCYcKHSKiZ0hU-zzDkxnOqBYaqufHOWDAogiETW6x-XGIAhIVHX-Uc56ipWVq479ZNjVeejsvqhrHokubbrVCmORC_43KGzMcjZSkQNSsqxN25Dm3V9Rrm6RqCpCkuaR2xdKF-Xx0FFnoMiqH4rOWDpV9377RRdY61BPjldVw6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۰.۲۴ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/138479" target="_blank">📅 19:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138478">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پس از حمله مشترک عربستان و آمریکا به نیروهای حشدالشعبی، نخست وزیر عراق، علی الزیدی، خواستار دیدار با محمد بن سلمان، ولیعهد عربستان سعودی، در جده و در روز پنجشنبه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/138478" target="_blank">📅 19:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138477">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzrAjDfJH0QbiPBniqnZQtRBLruFmDlw5T9dvKTbl4s9-wJ4l_E1IxRQaWaVE1VDesZkyqBhaahMGgwP0pGa3D9kkBi-azRD67b6j3rPQLr0R78GV7jx7fHZN0Yxc6yNdEg8bxfXJSXlUr8wPwCnC7K_dALGf9_E8-TF6V-YB-RsV7XAxF-wZv591d2g6aE6amjqDJRk02KHEukugt2rHGbw8harohBWptZz_mxeWLFFE4t6k-y1Z5S9nTT09ojQQdYLU4Pr9atZvVAgjMkjl7grvoYLHR5mCUe-5QcKVumkULo3Lnt_rU0yXI3zA5dOGIebbF9D7KJHUlbxgeQapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
تنگه هرمز یک آبراه بین‌المللی است.
🔴
سپاه هیچ اختیاری برای تعیین مسیرهای تردد برای جریان آزاد و باز ندارد. کشتی‌های تجاری همچنان از این تنگه با حمایت نظامی ایالات متحده استفاده می‌کنند.
🔴
از اوایل ماه مه، نیروهای سنتکام به عبور تقریباً ۱۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138477" target="_blank">📅 19:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138476">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی : مجتبی خامنه‌ای قطعاً زنده‌ست؛ ایران در حال حاضر تقریباً ۱۵۰۰ موشک بالستیک در اختیار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138476" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138475">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / نتانیاهو : ایران غنی سازی را در زیر کوه کلنگ آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/138475" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138473">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-bLYmS7rgACOSNr-GVyERA9kL3LEqnGQBKlbdQpFaFOZf4DYrNdz5NY6hAORdULZV_xzgnZiA6-YSQAGzTpRhAbk8u74pmAJwdqj33ZjGsRySDMsKr0isAgmd9AgklBDre5osWzR-fiwI9_2W44YCwbsle8QloK21YesdSIIkUwF03JeVLQShxkFiaKgaTToVDe_fUzElZ0DBnNaHLqp_uVWxd7UcFHNKv1dqIC_BJ10hw07OM8kG-lSd7-tQQkzsBjJww4isCtJFTJC5jk7QyL95dKT5U2ih-d1o3zfOr3ToqbfX7gZFfIlxHaFr8ZL93XjWTjR6RT0zUmwRMLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PallF82-k0IRhQAMLn5NIyKxPL1Tl0tSJ7excsvGV2_1QEOa9pY3VuhVvgJPVoWOuy5VoWZqrdM_cNlhL8-yipRIiNyi_5Q2-jF-sCbtouyesirP83fjnC3iBkjuXJLwAfSM2sGmw_qtgi4yZaMtTcBMSlubEug2XWNlq8Pg-baF7sVbln0NvE_dAWOfBC2_IvLy00v7-OgHQqNRfuHpqbBvOk3BOqo6DPSgjByQwiGPmYmvqtvNthbN4qkX_h92ELHAcEw8hmnMBGcCaD-xtB-LRtrwE-poP_X_DHfbqSq1SP-f56JUc7Xds7ezecCA4qNmk1-vOMmwk7E1tWdBWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فعالیت‌های گسترده آمریکا در خاورمیانه، به منظور آماده‌سازی برای حمله به ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138473" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138472">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95b6749bb.mp4?token=QhIzAmu0sTAzM-7rL-DyM_sJ1XRL0siSwxxFxTcoFJTlekYsRhXYrqipuIGwZX-FmFJqK3jXhcyUJpsLnSTuvPZfDXxZoYUyh1AzMy9x_S2mYjpFVwen7zGFmaSWKlagpDmyWxtZUFPr_EjceQBwh7s-Wj4L_4fJhhUU6K2Im1FtW8Qo8FJ31HRr9K3TgDR-U0L15ZMFeTyVgFeuHuUEcfe7mtipdcuBX6djZyGhliYqJnPfsFUKO022X7lNaNy9vRQPTrex2VGZyInUNJtc5Yh3-pOHEQLbEQWrHsWNT2vJFE4XHqlnCn2tzw_7WP8YcTRT0ns7bEv7vxHs2gfjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95b6749bb.mp4?token=QhIzAmu0sTAzM-7rL-DyM_sJ1XRL0siSwxxFxTcoFJTlekYsRhXYrqipuIGwZX-FmFJqK3jXhcyUJpsLnSTuvPZfDXxZoYUyh1AzMy9x_S2mYjpFVwen7zGFmaSWKlagpDmyWxtZUFPr_EjceQBwh7s-Wj4L_4fJhhUU6K2Im1FtW8Qo8FJ31HRr9K3TgDR-U0L15ZMFeTyVgFeuHuUEcfe7mtipdcuBX6djZyGhliYqJnPfsFUKO022X7lNaNy9vRQPTrex2VGZyInUNJtc5Yh3-pOHEQLbEQWrHsWNT2vJFE4XHqlnCn2tzw_7WP8YcTRT0ns7bEv7vxHs2gfjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیتر هگست، مشاور وزیر دفاع، در واشنگتن دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/138472" target="_blank">📅 18:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138471">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
روزنامهٔ هاآرتص: دو سرباز زن اسرائیلی این هفته خودکشی کردند
🔴
از ابتدای سال دستکم ۱۶ سرباز جان خود را گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138471" target="_blank">📅 18:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138470">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GlfkpGK7VZNrMNmI7RcegcSNmsVPxzl1GmaBBadVl95rdjMeqGVHbvFA8MhjoMnhpQDRZVTZQUTKJRwfyeg92F0tUUqVXByOhhunnXNJlYLO0MAOApavFgFoKDR1XR0_mTo6o8Ui7OGqz1rJET0AntleLSb2BvDsODPSvl3TjbDZLa7RAH5g2ypiBXRJg9bnvLq4wr8_BGqUZqzFzba2sgq_p2YbOE-PISPFY4E2IIcEdgzsUsC-ws-IDJTWEYyP2wbLscAZ54MHNqGZcNUmXgTV8ASCHCilJSh76MGFNwxSPPgSDsgMYZ66gNEF6W6mc3fMdP6enf5gebweVoKt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنبش حزب‌الله نجبا بیانیه‌ای صادر کرد و در آن به حملات هوایی اخیر عربستان سعودی و آمریکا در سراسر عراق اشاره کرد.
🔴
این جنبش خواستار اخراج تمامی نیروهای آمریکایی از عراق، قطع هرگونه همکاری با عربستان سعودی و همچنین درخواست از دولت عراق برای تهیه سامانه‌های پیشرفته پدافند هوایی به منظور حفاظت بیشتر از عراق شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138470" target="_blank">📅 18:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138469">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
مقام ارشد اسرائیلی به i24 news :هنوز غنی‌سازی اورانیوم تو سایت «کوه کنلگ» شروع نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138469" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138468">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39fa80d3ba.mp4?token=nKtTWrtsnrTqbpXVasw1eoqtcWCNraodxoELnsL0JuFnWTxqJFF3fBRTIdzF9n87yKgCkqlpmmx1YT43Vkgg4JysMvGzPv6DGh5orbHYyJEkxrQv1sUAoiBxVgpaE9H2S30HBxlrTNFORlol0XhXIRHJXhbjeETkKByWDcL1uLmBOwzHFMKdZrlnRdIhIBYjshDRrRP1Z0pOMZHi0H8AKMlB65NszfxUVffeGPA9VuPMZhFckV-a7KOVSM3dpT_0WK161V0qFk8Zq5y0IsZcQg7C_FAyUmpc34-WyBZ9jc-88oD6qQEzAtmeugEIFM1GiY_NNcjFGvnp4yAlWSQisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39fa80d3ba.mp4?token=nKtTWrtsnrTqbpXVasw1eoqtcWCNraodxoELnsL0JuFnWTxqJFF3fBRTIdzF9n87yKgCkqlpmmx1YT43Vkgg4JysMvGzPv6DGh5orbHYyJEkxrQv1sUAoiBxVgpaE9H2S30HBxlrTNFORlol0XhXIRHJXhbjeETkKByWDcL1uLmBOwzHFMKdZrlnRdIhIBYjshDRrRP1Z0pOMZHi0H8AKMlB65NszfxUVffeGPA9VuPMZhFckV-a7KOVSM3dpT_0WK161V0qFk8Zq5y0IsZcQg7C_FAyUmpc34-WyBZ9jc-88oD6qQEzAtmeugEIFM1GiY_NNcjFGvnp4yAlWSQisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رونمایی چین از موشک بالستیک هایپرسونیک YJ-۲۰
🔴
ارتش چین برای نخستین‌بار تصاویر شلیک موشک بالستیک هایپرسونیک ضدکشتی YJ-۲۰ را از روی ناوشکن مجهز به موشک‌های هدایت‌شونده تیپ ۰۵۲D منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/138468" target="_blank">📅 18:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138467">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به رادیو ارتش اسرائیل: تصمیم‌گیری درباره اینکه آیا به ایران حمله شود یا نه، بر عهده رئیس‌جمهور ترامپ است، مگر اینکه ایران تصمیم به حمله به اسرائیل بگیرد.
🔴
هیچ حمله بی‌جوابی وجود ندارد، و ایرانی‌ها می‌دانند که اسرائیل پاسخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/138467" target="_blank">📅 18:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5fJ_H9c0w4EjMhGOq0Frcct2bC5AuzMqjRgDe65HQ5am5UuWUOvmuckETSzQEEVFTNnj01eoMLB5TC9N8LlaxSGQs1h-a2MCv5xSrzU83LZgEZ_1QvXf6XzRmwVdxyNek1S11vrc-KCpOv4r_1OEw0lR7Nhz2YQws9T_eCQddZqCWM5h5wFHlFddhGMmi76lK_Gy9X1KqSNcZ8edcll7zlGVaQ-HoxfqNnlbe7d4m7bz2qMtC_TCebUoPxze114Eg4HC_ep_Mcle4fsFY9lmrYyzogC87tf7fm01mlBtySWC2foTDzz_80fDDCaEJB380rPshtqOyKvBOfDSCJvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کوثری، عضو کمیسیون مجلس : جنگ تموم نشده، نباید جنگ رو قطع کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138466" target="_blank">📅 18:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
برخی منابع عراقی ادعا کردن که سردار حاج علی اقبال پور، فرمانده ارشد قدس و مسئول پرونده کرکوک ۲۰۱۷، به همراه تعدادی از نیروهای یگان قدس هدف قرار گرفتن؛ البته این خبر هنوز تایید نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138464" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از منابع آگاه گزارش داد که «بنیامین نتانیاهو»، نخست‌وزیر اسرائیل در جریان سفر خود به آمریکا از دیدار با «ولودیمیر زلنسکی»، رئیس‌جمهور اوکراین در واشنگتن خودداری کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138463" target="_blank">📅 18:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قیمت نفت خام برنت با ۷ درصد افزایش، از مرز ۹۰ دلار در هر بشکه گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/138462" target="_blank">📅 18:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d19039aae.mp4?token=rw2I2Qu_cT0xUCsuz4-G5io-IB1nT7xIw0Xv6jrT9i2eT0oQISQTzr4j0aBcCwMYFwsj8Oujz__eaegrJZ5wQV8zR4rvxF6Vzn0YAuiHp7hHxMBYaywW76KsMJSPyH4E5N8dvak_VVQ2R9mAoEYY0N5-BHisEfy4VomO1fZ96o65WFzXtQ2aPcYk3JwWxw32qDUEePHhiK4iqb0ss9q3bwoNXFCFaBP5QJsquTJonKyrQrKr29DbAJ40M-rS888XNgYh4cWqbycMh_INQOtU7aykrmo7a2aVhN5Ogqnsu3kcaKnTBBrHimGEeZrB2nbKgv_4C-hKW60OwsLWA5DvKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d19039aae.mp4?token=rw2I2Qu_cT0xUCsuz4-G5io-IB1nT7xIw0Xv6jrT9i2eT0oQISQTzr4j0aBcCwMYFwsj8Oujz__eaegrJZ5wQV8zR4rvxF6Vzn0YAuiHp7hHxMBYaywW76KsMJSPyH4E5N8dvak_VVQ2R9mAoEYY0N5-BHisEfy4VomO1fZ96o65WFzXtQ2aPcYk3JwWxw32qDUEePHhiK4iqb0ss9q3bwoNXFCFaBP5QJsquTJonKyrQrKr29DbAJ40M-rS888XNgYh4cWqbycMh_INQOtU7aykrmo7a2aVhN5Ogqnsu3kcaKnTBBrHimGEeZrB2nbKgv_4C-hKW60OwsLWA5DvKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراینی ها امروز هم بدین شکل یکی دیگر از مراکز وایلدبریز روسیه (بزرگترین مراکز خرده‌فروشی)، را پودر کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138461" target="_blank">📅 18:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPZDsGQtkEHweFYOLbCGqy9jRncKj21AqbMMAAo2vXDy3_KiwMgNqZc21jBGSKIKGFz_Q6c2YxTsnlXFcSZssRnpW-jIj00rjVjtq5TipnYAvMo17P-xkE3Ps6vGF_3ltXx4F1H-y13CaaAkMXusj__g9tO1GzYXpVyResubC-E93e-Gi4vrP2QeFIRRp2-vQUgJP3LrMzFhwKFHA5A_aLARBTPKnX_tD5OiJtuOhYBBHQhAbf6dDLUdY03WaaWLSDpHHDACNU1mWaSUcvBN5IRTuznEC_RJ-tpNFB931w2aMGd5MNhX6MFpI4apDR80S8y7ci_3U942OJKjYNLK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138460" target="_blank">📅 18:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138459">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxu5BnFA5BF2PCDYA4yiEYW6sCG_5EW56zct2k9lSDucRrg0i_I2l5LsfkpCOXAuodEfNUJmDS1QRMO5TSHDuNNJFkSTOofBD0iBBEELNJLoFvZR7Rt4Ln8H8Lur238k6nfNaPg94m5cm2pJ9qASUDQFqCQbokcCQM-5NuI9nVmUZUbITtqWc9UK1q6R-dn4kDe6ydoUDTpAkpECGQX2FhchIAuYkM5NgCK26mOYmi14EJHL-bbB8Odcvh2UeEhWcUPJ7Z5t5doZyOnkqqc_Osi1pUyEkf0jdiuPuHX9yHCDfpKfDLKyiz8WY1NW1OKG9o1nzSsgtglxrwSjuUToyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وثیقۀ تحصیل در خارج به ۲۰۰ میلیون رسید
🔴
براساس به‌روزرسانی سامانۀ سخا، مبلغ وثیقۀ مورد نیاز برای خروج از کشور با هدف ادامۀ تحصیل از ۸۰ میلیون به ۲۰۰ میلیون تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138459" target="_blank">📅 18:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پزشکیان: ما با دشمنان می‌جنگیم تا زیر بار ظلم و زور نرویم، پس نمی‌توانیم خودمان به مردم زور بگوییم یا ظلم کنیم
🔴
اگر معیشت و سطح زندگی مردم را بهبود نبخشیم، خداوند از ما نخواهد گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138458" target="_blank">📅 18:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138457">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
زلنسکی: از ترامپ درخواست کردم که یک «بسته اضطراری زمستانی»، شامل ۳۰۰ موشک رهگیر پاتریوت را در اختیار اوکراین قرار دهد
🔴
اگر مشکل کمبود این موشک‌ها برطرف نشود، حملات روسیه نیروگاه‌های برق ما را نابود و یک بحران انسانی ایجاد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138457" target="_blank">📅 18:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138456">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدیدی علیه شرکت‌های مرتبط با ایران خبر داد!
🔴
وزارت خزانه‌داری آمریکا ۸ کشتی و ۱۰ شرکت از ایران، چین و چند کشور دیگر را به بهانۀ ارتباط با ایران تحریم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138456" target="_blank">📅 18:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138455">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22502e2a34.mp4?token=wAK4kXR1CVc8otpRaI2v5HEhQowXar4YFdR5feqCGASun2A1pGWlPlrq6Gr1z5J42w5e6cxaakG44FmMpEQjaKTkT2pzk17kM0CDRFEfNe0iR73CbTcpt3fk-RdQbDYRHR5pfBsGI6ulf4jHPNObqhwBgcM7G4W7Szri_DBcmHgODpikH-qP7DmoWVioiXqXwSzGzfz8_QIxbjzpvK2x3XdzW8cAFvxjV8NQVpZ0xyB9bII2YK9ml6YUBE6_RHoRmu4V_i1DNIzuG-5FyQkKTgmjJqmGzbojbdwlf-uCwufVrTGfRtj_qP9hVFhx3Nmgcz4kL_oa55-Gj5TUMZUG0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22502e2a34.mp4?token=wAK4kXR1CVc8otpRaI2v5HEhQowXar4YFdR5feqCGASun2A1pGWlPlrq6Gr1z5J42w5e6cxaakG44FmMpEQjaKTkT2pzk17kM0CDRFEfNe0iR73CbTcpt3fk-RdQbDYRHR5pfBsGI6ulf4jHPNObqhwBgcM7G4W7Szri_DBcmHgODpikH-qP7DmoWVioiXqXwSzGzfz8_QIxbjzpvK2x3XdzW8cAFvxjV8NQVpZ0xyB9bII2YK9ml6YUBE6_RHoRmu4V_i1DNIzuG-5FyQkKTgmjJqmGzbojbdwlf-uCwufVrTGfRtj_qP9hVFhx3Nmgcz4kL_oa55-Gj5TUMZUG0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امام جمعه رشت: بابت اعدام‌ها تشکر میکنم و امیدوارم همشون اعدام بشن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138455" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138454">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
تلگراف: چین قصد داره راکت‌انداز به ایران ارسال کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138454" target="_blank">📅 17:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138453">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1pqd4At9a2Z9swjyxc5B3oZtod54dH7R6y7MMjKjAZYpSMlvIlaOA9qAsTufa-YNhkgbM-o8bxfV0tuTN4kieg8MyXWgzPMAvAspy7ChG53D-VlOBgXkB200I8pG7mT-Uze8HLDs2ybX2Shpe5aTRzjKGwh3-d_7RHr9QHxAUKAtgaOsJ4uGWbrs241BP1oWVyud3PkO_vpWWbcRk1oN5uBkklwbM48chs7dhLK_-D2QbYckiSxztCxMSjb3BmgD2BJFjSolygHmQke6nrgbxsXhS6YrDbJhvvbUW1zshsD4qN9VgaNfGLhEmfyanFEarDZYCX8ELHZKw7aTFUcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز پیش این مرد تو آمریکا یهویی روانی میشه و اول زنشو با تفنگ میکشه بعد ۶ تا از بچه هاس که همشون زیر ۱۵ سال بودن رو میکشه و آخرشم تو خونه آتیش درست میکنه و خودشم با تیر میزنه تو سرش خودش و خودکشی میکنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138453" target="_blank">📅 17:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138452">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
اینترنت استارلینک در عراق فعال شد
🔴
سرویس ماهواره‌ای استارلینک رسما در عراق راه‌اندازی شد. دولت عراق و کمیسیون ارتباطات این کشور با هدف بهبود دسترسی به اینترنت، مجوز فعالیت اسپیس‌ایکس را صادر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138452" target="_blank">📅 17:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سفارت آمریکا در عراق هشدار امنیتی برای شهروندان آمریکایی صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138451" target="_blank">📅 17:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت خارجه روسیه در پیامی کشته شدن تعدادی از عضو های گروه حشدالشعبی توی حمله دیشب آمریکا و عربستان رو تسلیت گفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138450" target="_blank">📅 17:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138449">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUAyi0upAJhdSZLrWLnNEHS_Br5b6vGO5IQgs9LYbtReImMtscGPoAjlGyjS40CHdYClO9oq5VWB_zSsDJHluKnCoTt6awGwwQIDWdyh3ho-Ew870-G5knSGo-fcrtI5wd0tl-M2Sz9afGxGixBG-MJEqmgoASszkFrd-ivyRwtZ0J8KNtZhE6LsAX8GDzSLwyxT5U26fuMSggIa9DgzpYuGlFVItm2EX2cMq0V4ybUj4xR2BDIiqzo5v15AcJRHWSPeEU70UV4CxKso6t0j1prt2Lq5QoryAtDa0ppVBOEFoJR7B4VVKiNS89fWSLGuxpO6lghTiV8D0o7s9vfgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آمریکایی تانکربنزین (برای سوخت‌رسانی هوایی) در حال حاضر در نزدیکی سواحل سینای مصر در حال عملیات است، که یک اتفاق نادر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138449" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138448">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMqTIpPtrneuO_SXxxcZ16fBjvgF90XTEcIshkJqZfYLp6paQ23i6j-1d2rxCzyOrRhl5VbsoEd0kP7QW4v-PFtY98yjkEJ-MALUiPV3khDPEcye_pdUOCkvgyyHGV9JKebrNtEx3l9S0Gr86mI6hLOKe02uYU9p8CxvVb3p6o8YOeqQ4wj4dM-CyUnTtMmg-kWr5POwhBXzy7rVpLvEvRkyGnxN_YcR-KhUvUxWw-QN4AM9VEyybFybB-B3aEVpWxKGS7FIDNsO8Af2bS9RZBVmDd7laOxP6R8L7aQUropmUfYQ3q9Ka_b9KQZaefPqWRPASJL2ceh0TMdyXrO9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138448" target="_blank">📅 16:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138447">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
این حرومزاده به اسم نوید زیاد خان قره باغی، با شیرین زبونی برا دخترا می‌برشون‌ خونه‌اش و داخل لایو می‌زنه و تحقیرشون می‌کنه.
🔴
تو این ویدیو که از لایو هاشه یه دختر اینقد می‌زنه خون بالا میاره و گریه می‌کنه و یه دختر دیگه اینقد می‌زنه بیهوش میشه.
🔴
روحیه حساسی…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138447" target="_blank">📅 16:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138446">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
این حرومزاده به اسم نوید زیاد خان قره باغی، با شیرین زبونی برا دخترا می‌برشون‌ خونه‌اش و داخل لایو می‌زنه و تحقیرشون می‌کنه.
🔴
تو این ویدیو که از لایو هاشه یه دختر اینقد می‌زنه خون بالا میاره و گریه می‌کنه و یه دختر دیگه اینقد می‌زنه بیهوش میشه.
🔴
روحیه حساسی دارید ویدیو رو نبینید.
آدرس این بیناموس: تهران،۱۶متری امیری، کوچه بهفر پلاک ۷۰۱
کد ملی ۰۰۱۲۰۸۴۸۶۷
+989351197525شمارش
برسونید دست پلیس فتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138446" target="_blank">📅 16:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138445">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c546530197.mp4?token=hOrphoEOgD8Z0U2EYBYbU93WcsuBwbnhlv85a5NO7FsSuz3sKV4yyybEaUKS_CEpQ5SgtkdmMYfcixJcQjlIgFA60pIY2U1di0mkpyFE_FrtQ5RsjTVEf7YZnv1G122beHjXNpVEVGRm0Vw19uHknzM2wgBpQ8rNeXJCG_d668ZbGi-1a3vPkNnXMyeOctryJZlGf5HYlGZf1ju3ubApFKhaBUz5qPGMpDGZH55qFO2n4u4CEJKWWjuIEmSDsw-IZ8ah-Vz9eSAt9mBbFzp9VMJOVCLkbNLNQtJ-bbz5TmofNbKpsHsLZ580PczXmlE9A_0w9e2eAzy705c7w3klew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c546530197.mp4?token=hOrphoEOgD8Z0U2EYBYbU93WcsuBwbnhlv85a5NO7FsSuz3sKV4yyybEaUKS_CEpQ5SgtkdmMYfcixJcQjlIgFA60pIY2U1di0mkpyFE_FrtQ5RsjTVEf7YZnv1G122beHjXNpVEVGRm0Vw19uHknzM2wgBpQ8rNeXJCG_d668ZbGi-1a3vPkNnXMyeOctryJZlGf5HYlGZf1ju3ubApFKhaBUz5qPGMpDGZH55qFO2n4u4CEJKWWjuIEmSDsw-IZ8ah-Vz9eSAt9mBbFzp9VMJOVCLkbNLNQtJ-bbz5TmofNbKpsHsLZ580PczXmlE9A_0w9e2eAzy705c7w3klew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جمهوری‌خواه، تد کروز: فیدل کاسترو یک میلیاردر بود. پوتین یک میلیاردر است.
🔴
رهبران رژیم‌های کمونیستی همیشه ثروتمند هستند. آن‌ها از کسانی که بر آن‌ها حکومت می‌کنند، دزدی و غارت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138445" target="_blank">📅 16:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280385abd0.mp4?token=Z6FuK21NctE8GJo4SwSYYOqHABXaLrVDXJ7pTIWc1AOBTRED_iQt8etm_hRnwGkR3AvPqjYebYMVJzwpGMCk1LPkxH6WL9WKRFPMWTrtBv7t6c0qZulKCxgDHxAQxB2Yi3-sRfjN5XTMvwKbUSYBN3d4KaREygB5BUTr2g4mRZCTnhJnPIgEwFTQPSLmxlSKFT-jlSvS_yeY7GhRTj8w6FuZsFGTbjFBg60bjKI2VjGt_hvhzZyRumsUaGA3mUxvt0qdWrZrKCnZR6j_HgoNGb0H8sxGhCsResA2LSMXTHWBUJ5j4OwN5scSUTcI-ksQP4iuN6Nid4XePzYFQdQuRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280385abd0.mp4?token=Z6FuK21NctE8GJo4SwSYYOqHABXaLrVDXJ7pTIWc1AOBTRED_iQt8etm_hRnwGkR3AvPqjYebYMVJzwpGMCk1LPkxH6WL9WKRFPMWTrtBv7t6c0qZulKCxgDHxAQxB2Yi3-sRfjN5XTMvwKbUSYBN3d4KaREygB5BUTr2g4mRZCTnhJnPIgEwFTQPSLmxlSKFT-jlSvS_yeY7GhRTj8w6FuZsFGTbjFBg60bjKI2VjGt_hvhzZyRumsUaGA3mUxvt0qdWrZrKCnZR6j_HgoNGb0H8sxGhCsResA2LSMXTHWBUJ5j4OwN5scSUTcI-ksQP4iuN6Nid4XePzYFQdQuRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد دیدار خود با نتانیاهو:
این یک دیدار عالی بود. او اکنون همه چیز را متوجه شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138444" target="_blank">📅 16:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138443">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
در جلسه امروز هیئت دولت عباس عراقچی وزیر خارجه، گزارشی از تماس تلفنی وزیر خارجه اوکراین و آخرین وضعیت مذاکرات با عمان ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138443" target="_blank">📅 16:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138442">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUilM4Wv7wv_s-cQ0vcw2F-G1v3YukqeYiegwU9AZL2evpayDQnlDlC0JPdOM7RQyBaLpV100f6OIWmw3uMafqIhaH_eq7RSFoj-9X94k5S8UUIU2XxtKwa21Of3iPhCIno8HvLnDGkVK7bODOP2YFMdXOT0Jhi2w1413o6QE7bxdPHiyWt8hmmQm9bCYhdQSEU6OxnhNNsn8BLZb5lo2NG30YRdkKRl7FyRBg0G6JrRDu56OWVhSZIzoeYq3VKbgqIJDWRhn5xFjIKNvX6snj6inoqPpqO1dK1i5mRZqGfYSL-FvYR2ANqKkMhYsV5sQo_u-0YvCBXVeQmS0cvJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138442" target="_blank">📅 16:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نتانیاهو امروز با وزیر دفاع آمریکا، هگست، دیدار خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138441" target="_blank">📅 16:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138440">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFmoXMv07MBXA78wSgerIy3nUlvXSkGwzZlQOWERmOE0yGUmZGrVClp-cShtQm5s6iCYuVvn9U_UVJJbsbLvAtePRBSbpy37pLkWLPsjXTip0ljD02OBxgyhZuHvHdLUv6KqARj15R5nBz7LI5sIB7SQtA_B0RPA2Jr58HO1W84S4b5YJhpf4NCztmVl7usjksg4-VUEftV1N93AJ3kZlRHdX3Q7Lu_hY75J-Iq-zfY_A_w2CZaBR0YDaUHexOOf66zuyUn2xcddg-PDvtsYGNro1zCQTQRD0d-TraM32RlvIfCotVBU3t3TPugTqtafm0-5zIq2Dey5W31Yk37g3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون جهش قیمت نفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138440" target="_blank">📅 16:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138439">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: من در نظر دارم اخطارهای جدی‌تری را علیه نیروهای نیابتی ایرانی مطرح کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138439" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138438">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: شبه‌نظامیان مورد حمایت ایران «سرطان جهان» هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138438" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138437">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ:  فعلاً اجازه می‌دهیم ایران به گفت‌وگو ادامه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138437" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138436">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=J_TAOVLA1B8m75KU4EgcP3MmfL5HGMknk764zeKIHIUUBx599OtZXapGFlwiBJdV1TGeHJjzoKhjkrmg_EwlDQ8CguMjGjc-jNlzW-nE-E3nbWQ8U3kzVGG1sdljiFe4Xhk1RXftN30O-zv2RWd2ft4VaLtXR2ZGrriJ-gmWX14MUitySgnvgva5Z-EOSp0n-L4Lb0DmcKGUHzS4_1ne1f-rPfl9Z9bvbRlallp1QUugBTb3NBpLXEjvRWTOeQJe9bnDNxly_mcrIQjzgSq6OaUVYtQ4ZF_sHgiZbKoAYtntsaJ1YXeFxzYQAFMrqmz11J_e2iR7nuAyaKBKaqIliQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=J_TAOVLA1B8m75KU4EgcP3MmfL5HGMknk764zeKIHIUUBx599OtZXapGFlwiBJdV1TGeHJjzoKhjkrmg_EwlDQ8CguMjGjc-jNlzW-nE-E3nbWQ8U3kzVGG1sdljiFe4Xhk1RXftN30O-zv2RWd2ft4VaLtXR2ZGrriJ-gmWX14MUitySgnvgva5Z-EOSp0n-L4Lb0DmcKGUHzS4_1ne1f-rPfl9Z9bvbRlallp1QUugBTb3NBpLXEjvRWTOeQJe9bnDNxly_mcrIQjzgSq6OaUVYtQ4ZF_sHgiZbKoAYtntsaJ1YXeFxzYQAFMrqmz11J_e2iR7nuAyaKBKaqIliQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد حمله اخیر ایران به اردن: این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را سرنگون کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138436" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138435">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27adb3179e.mp4?token=mG0_BQraJGu0VmMafOk6bZh_hOG53VaYyIEkwDN78U5dmJgdA0yZyvJWYu5dBVIXsHGyPJQG5k0N9WUpPit4w26md8_2j2scJFNpRNngpvsEk3URm0ahZe-BqxI6K0sQxpyGpIvdO1ZGXI3EWsJ4YudhSzgewBjuZQt_dzH1vSWOX1clT_pbFd8-FUfSWPOmC35vI1UeeF_wgh30EOLWi9z72ARvz9kpk-IbzbVlzniYhP8ChWjg5BBsJep8pU_9S1Urjss9mKhXBIE94aiztcT2bMh8JSJPk-YbKMVz6PUI_o1pVUSRjtfhVnZn5xhU8qtEbBapciLG7jP7wywSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27adb3179e.mp4?token=mG0_BQraJGu0VmMafOk6bZh_hOG53VaYyIEkwDN78U5dmJgdA0yZyvJWYu5dBVIXsHGyPJQG5k0N9WUpPit4w26md8_2j2scJFNpRNngpvsEk3URm0ahZe-BqxI6K0sQxpyGpIvdO1ZGXI3EWsJ4YudhSzgewBjuZQt_dzH1vSWOX1clT_pbFd8-FUfSWPOmC35vI1UeeF_wgh30EOLWi9z72ARvz9kpk-IbzbVlzniYhP8ChWjg5BBsJep8pU_9S1Urjss9mKhXBIE94aiztcT2bMh8JSJPk-YbKMVz6PUI_o1pVUSRjtfhVnZn5xhU8qtEbBapciLG7jP7wywSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما قرار است حسابی لجنشان را دربیاوریم.
🔴
آنها را به شدت خواهیم زد — کتک سختی میخورند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138435" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138434">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ در مورد حمله ایران به اردن:
حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
🔴
حملات دیشب به نیابتی های ایران در عراق، با هماهنگی با حکومت عراق انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138434" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138433">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری/ترامپ: ضربه سختی به ایران خواهیم زد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138433" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138432">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رئیس جمهور اوکراین مدعی شد پوتین قصد دارد 500 هزار سرباز دیگر را بسیج و به اوکراین بفرستند همچنین 30 هزار نیرو از کره شمالی و تعدادی موشک بالستیک از کره شمالی و ایران(؟) دریافت کند،لازم به ذکر است زلنسکی به ترامپ در مورد رهگیری پهپاد‌های انتحاری ایرانی پیشنهاد ویژه‌ای در ازای دریافت کمک‌های نظامی داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138432" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138431">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عارف: وزیر و مدیری که اختلاف را به جامعه بکشاند عزل می‌شود؛ تعارف نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/138431" target="_blank">📅 15:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138430">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
دریادار سیاری: بدون اجازه ایران هیچ تحرکی در تنگه هرمز انجام نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138430" target="_blank">📅 15:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138429">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
آمیت سگال : نتانیاهو دیدار خود در کاخ سفید را، به گفته خودش، «عالی» توصیف کرد و گفت: «این یکی از بهترین دیدارهایی بود که تاکنون داشته‌ایم.» کاخ سفید اما با لحنی محتاطانه‌تر، تنها اعلام کرد که گفت‌وگوها «مثبت و سازنده» بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138429" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138428">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
آکسیوس گزارش داد شرکت لاکهید مارتین از موشک رهگیر جدید PAC-3 ACE رونمایی کرده است؛ محصولی که با هدف پاسخ به افزایش تقاضا برای سامانه‌های پدافند هوایی، کاهش هزینه تولید و مقابله با تهدیداتی مانند پهپادها، موشک‌های کروز و موشک‌های بالستیک توسعه یافته است.
🔴
بر اساس این گزارش، هزینه هر فروند PAC-3 ACE حدود ۲ میلیون دلار و کمتر از نصف مدل فعلی PAC-3 MSE برآورد می‌شود. این موشک که قابلیت استفاده در پرتابگرهای فعلی پاتریوت را دارد، نخستین پرواز خود را در سال ۲۰۲۸ انجام خواهد داد. آکسیوس همچنین از تلاش پنتاگون و صنایع دفاعی آمریکا برای توسعه سامانه‌های پدافندی ارزان‌تر، از جمله پهپادکش‌های کم‌هزینه، به‌منظور افزایش ظرفیت تولید و کاهش هزینه‌های دفاعی خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138428" target="_blank">📅 15:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138427">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
به گزارش العربیه به نقل از یک منبع ناشناس در ارتش اسرائیل، فرماندهی مرکزی ارتش آمریکا (CENTCOM) پس از آنکه یسرائیل کاتس، وزیر دفاع اسرائیل، به‌صورت علنی اعلام کرد که هواپیماهای آمریکایی مستقر در پایگاه‌هایی در اسرائیل طی هفته‌های اخیر در حملات علیه ایران…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138427" target="_blank">📅 15:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138426">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
به گزارش العربیه به نقل از یک منبع ناشناس در ارتش اسرائیل، فرماندهی مرکزی ارتش آمریکا (CENTCOM) پس از آنکه یسرائیل کاتس، وزیر دفاع اسرائیل، به‌صورت علنی اعلام کرد که هواپیماهای آمریکایی مستقر در پایگاه‌هایی در اسرائیل طی هفته‌های اخیر در حملات علیه ایران مشارکت داشته‌اند، ابراز نارضایتی کرد.
🔴
این اظهارات جزئیات حساس عملیاتی را فاش کرد و در پی آن، سپهبد ایال زمیر، رئیس ستاد کل ارتش اسرائیل، از دریادار برد کوپر، فرمانده سنتکام، عذرخواهی کرد. همچنین اسرائیل پس از این اتفاق، سطح آماده‌باش خود را افزایش داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138426" target="_blank">📅 15:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138425">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNsWZaeJaRF8dk6Kh77kon7R0Qi5SymG651i93dtsKtMc4vRqt4_cGmVK0u-J6beDgBhcyK9Xr2VwZuMZCYMAPle3lMa5SWuPFi1Six7hfA_HgcBlPCPqJMK3ettYzXmU8QKAKm0AhLO1C_e-o8wdEjR-SjiZlS322eaM6vWtekcGpPfLZdCJdleIXvcD67ouJaP6vv2XHk5Z4FwZktfz0AcSfSepJZzA_tjX0Jx2be70EDGc51vTb8wTIKPmXydukvROYr9gRdn1rKor2M1xQo4KK-_99vQ3K2pzuZykHJMdhBmZRp1AP4sGYebm7cM9VCpL7Orsk65sUkIQGiE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسپانیا با پخش اذان از مساجد در برخی از مناطق این کشور موافقت کرد.
🔴
دولت سانچز، یکی از چپ ترین دولت های اروپایی حال حاضر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138425" target="_blank">📅 15:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138424">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
چین: تفاهم‌نامه ایران و آمریکا که نتیجه ارزشمند میانجیگری و تلاش‌های چندین طرف است نباید از بین برود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138424" target="_blank">📅 15:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138423">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عراقچی: اوکراین باید مسئولیت حمله جنایتکارانه به کشتی تجاری ایرانی را بپذیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138423" target="_blank">📅 15:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138422">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
الجزیره: تعداد کشته و مجروح های حشدالشعبی تو حملات دیشب آمریکا و عربستان به 50نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138422" target="_blank">📅 15:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138421">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شین بت : یک شهروند اسرائیلی به اتهام جاسوسی برای ایران بازداشت و متهم شده؛
اون قبلاً تو یک یگان نظامی محرمانه خدمت کرده و متهمه اطلاعاتی برای کمک به دشمن منتقل کرده
🔴
همچنین از اون خواسته شده یک سرباز اسرائیلی دیگه رو برای ارتباط با اطلاعات ایران جذب کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138421" target="_blank">📅 14:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138420">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008da4110.mp4?token=qNq0ED3a35Wjh0AZaiTWhMVKLOF1L2eWmP5ymWViOR1CkAg0dHgPk9PhlexLld7sJQEFv09pbRjJj5u8irVIcNRU7Scw2AiCHT5gquUXlUQRYYsrbeQGGDOj__T4mm5uyanLPN-O5RKjzaSqVGRIYaW2t8TizpBSvRJALUmO82FHKT9ZJ5qaDrlURcsQqcIKE-oV-XEKdMByBfEPmm41MfldDbwsSahL7j-50RCZ_n56PifSyd9_TJkNKu2K_d-ZEev1bXWmV-sNolmuaxOgm4XCcWh6UI9ZCuQWD39rtHvVoCsC_JGo0t7zaNFchXc8iWMSARHpQ4TseYUTgDoe7JuzD2ruK5WDaPFxPb4DUzuGDo9X3vZg0MjRjCbKPnjElMnQeDSUFuT_-9dSns4-9axJUvzTQ__dU9jZ_2eeNY5Bz7r5nNlIypN0Pnjr5E3pAQk2Fu5Zoi3O-CmJkPM8y03SPM38tNF_3r15zrKp5sPzrloYIhjdMWBwelzlKnHvcHs6-XTJQW5mt6pDLYM8-36Mf50UUxIXmfnt_bvxRwr6BfSEN4Lx0pPd_5crLeeznhJShPG6OfIjpYLtynXQZ1_2yP8vi8DZ8LeRdFBg01YPSu8Y0tMBAqrA785nMPLw5kqyStJ4815VpP6XOpooIcjHiESeSZE9SW9NZs5kR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008da4110.mp4?token=qNq0ED3a35Wjh0AZaiTWhMVKLOF1L2eWmP5ymWViOR1CkAg0dHgPk9PhlexLld7sJQEFv09pbRjJj5u8irVIcNRU7Scw2AiCHT5gquUXlUQRYYsrbeQGGDOj__T4mm5uyanLPN-O5RKjzaSqVGRIYaW2t8TizpBSvRJALUmO82FHKT9ZJ5qaDrlURcsQqcIKE-oV-XEKdMByBfEPmm41MfldDbwsSahL7j-50RCZ_n56PifSyd9_TJkNKu2K_d-ZEev1bXWmV-sNolmuaxOgm4XCcWh6UI9ZCuQWD39rtHvVoCsC_JGo0t7zaNFchXc8iWMSARHpQ4TseYUTgDoe7JuzD2ruK5WDaPFxPb4DUzuGDo9X3vZg0MjRjCbKPnjElMnQeDSUFuT_-9dSns4-9axJUvzTQ__dU9jZ_2eeNY5Bz7r5nNlIypN0Pnjr5E3pAQk2Fu5Zoi3O-CmJkPM8y03SPM38tNF_3r15zrKp5sPzrloYIhjdMWBwelzlKnHvcHs6-XTJQW5mt6pDLYM8-36Mf50UUxIXmfnt_bvxRwr6BfSEN4Lx0pPd_5crLeeznhJShPG6OfIjpYLtynXQZ1_2yP8vi8DZ8LeRdFBg01YPSu8Y0tMBAqrA785nMPLw5kqyStJ4815VpP6XOpooIcjHiESeSZE9SW9NZs5kR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فوران آتشفشان کیلاویا در هاوایی
🔴
تصاویر منتشر شده لحظه فوران دوباره آتشفشان کیلاویا در هاوایی را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138420" target="_blank">📅 14:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138419">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فارس: تنگه هرمز رو یجوری بستیم که دیگه از این بسته تر نمیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138419" target="_blank">📅 14:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138418">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf55992ebb.mp4?token=ntU9TRSiM_Yk6pWqxjG-_ZNsDnjtn-jitYODAqjCHU0ThpK9C7s0ySAXe8OXu1wJrsptYEwbtliJYxpKTZF5-CR9rWoyDZVRZvTMO9mz2WRJfJ98BS_pDqo7EersJOPtAM9GkYDCs5OEmsNc8t-NWiAZ8KwQyEbDc8Bvj_g-mlJ0KclHMvGwyoedS1XcuFEGqlWTCrFo6qpEJwxOxo9vRBVMM6Mc7dvetsh58IHY0ii7Zwbn5uzljo8KR6hjKXxMz-eeAhyejOU5Gxtqh_9kEBgGKwmObxM2jpIvWsWqwrxE4HvWGMiA3TnW3gWgWtkykl4PeEE67Yy_PvcT7FjPt0ZDCkutRDeHZxvpAlVx-a1hYtmEv6731HIGCZgD9pk4fs29Jrc2F6FlVg9t1WPerQORbwNVhKwO9yVbKZLx3XPbfp8wHyieGK4fp-JL4G8mtBDeQz6kJD5bvGLbTVqz_MuRcnW0MgAN4-1Xe7WH5NABL8tI9BHnU9caZJFHJLoDke1oRRZP2CFOMQdwYzA2vkfeUt_MQ0tIr9XH3OlZAuBISMXNxYZGBUBVwaUNV2zJHMd2pNYWlRCwAvS9Z__eA4pV2CwZR48oaQCG2q3hn3TCRVKwrrHJghDtnV672ev1nHNDp2uNXjmTsusA5oKCLN5sWaLhHpn-e19LTl-tZ98" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf55992ebb.mp4?token=ntU9TRSiM_Yk6pWqxjG-_ZNsDnjtn-jitYODAqjCHU0ThpK9C7s0ySAXe8OXu1wJrsptYEwbtliJYxpKTZF5-CR9rWoyDZVRZvTMO9mz2WRJfJ98BS_pDqo7EersJOPtAM9GkYDCs5OEmsNc8t-NWiAZ8KwQyEbDc8Bvj_g-mlJ0KclHMvGwyoedS1XcuFEGqlWTCrFo6qpEJwxOxo9vRBVMM6Mc7dvetsh58IHY0ii7Zwbn5uzljo8KR6hjKXxMz-eeAhyejOU5Gxtqh_9kEBgGKwmObxM2jpIvWsWqwrxE4HvWGMiA3TnW3gWgWtkykl4PeEE67Yy_PvcT7FjPt0ZDCkutRDeHZxvpAlVx-a1hYtmEv6731HIGCZgD9pk4fs29Jrc2F6FlVg9t1WPerQORbwNVhKwO9yVbKZLx3XPbfp8wHyieGK4fp-JL4G8mtBDeQz6kJD5bvGLbTVqz_MuRcnW0MgAN4-1Xe7WH5NABL8tI9BHnU9caZJFHJLoDke1oRRZP2CFOMQdwYzA2vkfeUt_MQ0tIr9XH3OlZAuBISMXNxYZGBUBVwaUNV2zJHMd2pNYWlRCwAvS9Z__eA4pV2CwZR48oaQCG2q3hn3TCRVKwrrHJghDtnV672ev1nHNDp2uNXjmTsusA5oKCLN5sWaLhHpn-e19LTl-tZ98" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای حشد شعبی عراق تصاویری از پیامدهای حملات هوایی آمریکا و عربستان به مواضع خود را منتشر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138418" target="_blank">📅 14:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138417">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد یک خودرو مهندسی D-9 مورد اصابت کواد FPV حزب‌الله قرار گرفته است
🔴
این اولین حمله به نیرو‌های اسرائیلی از زمان آغاز آتش‌بس میان دولت اسرائیل و لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138417" target="_blank">📅 14:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138416">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfzZISBHE-1fPO6mvtDPl4bF1OdBk17ElK4E4GkqQYZ2UXE1YvNLr2VOrJqtzuckoH1bpc41qx82ggnlcJSPliFysTAARmm-EdlWUMbiBPGCQ-HoRe7ou4NxofBUhxJFcVirk2zZHcEWvsaqPv6pReIA6G1ScgIqjVGyYbqjdwxUaSs50978EzTuRCSEGaz9sPoJRrzKHac4KbiB3qAzAAsJ4FbLzrQnWwkgCxwzPMS2-zLEhOpnbsxg0KTXBZj5I2C5VTukUGSbuqbRwo0rVOERzibzgrI1gEgTuZy-wgnxKHSRgycdbW4KSDtprEFeaFkdDcH3jdGkC5cLwrngBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران حملات آمریکا و عربستان علیه عراق  محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138416" target="_blank">📅 14:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138415">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نشریه پولیتیکو گزارش داد که هم پیمانان اروپایی آمریکا از حمایت از طرح این کشور برای گشت مشترک در تنگه هرمز سر باز زده و اعلام کرده اند که باید آتش بس دائمی با ایران محقق شود تا وارد چنین طرح هایی شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138415" target="_blank">📅 14:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138414">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/245226179d.mp4?token=nCwhbWBuKyRHgqCEJSjkQvHvcPVtU9J74QHc_CTS-1Ne0fMPzXgJAxEI1qvOMMJ9MrxJz_zTae3Z_NkyF9e2KuiV1AoJQO8PnW8cDZ_DjezwKivJN35s71K4ICXXNOTHDtrI1uN4bgQeWRyk4m5jjBZx4y4gETtG4zXtQpftS11MNDGYLNPL7Q85uk8p1cPABSqTGy0hsoVMUPzjsqFv2KSUwxlO4pcHm9RJBYJVsqG_a-how8gWwN24MbMaHAdROKQQzoRKQJXy3b-vNDCzJazAQlBkg53XiRc9vj8JP9M6c5FyYZCxDhzzjawTA78v6rvqNRZAAFyQBAit6onuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/245226179d.mp4?token=nCwhbWBuKyRHgqCEJSjkQvHvcPVtU9J74QHc_CTS-1Ne0fMPzXgJAxEI1qvOMMJ9MrxJz_zTae3Z_NkyF9e2KuiV1AoJQO8PnW8cDZ_DjezwKivJN35s71K4ICXXNOTHDtrI1uN4bgQeWRyk4m5jjBZx4y4gETtG4zXtQpftS11MNDGYLNPL7Q85uk8p1cPABSqTGy0hsoVMUPzjsqFv2KSUwxlO4pcHm9RJBYJVsqG_a-how8gWwN24MbMaHAdROKQQzoRKQJXy3b-vNDCzJazAQlBkg53XiRc9vj8JP9M6c5FyYZCxDhzzjawTA78v6rvqNRZAAFyQBAit6onuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چُرت زدن ترامپ در مراسم خاکسپاری گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138414" target="_blank">📅 14:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138413">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز: ژنرال براد کوپر، فرمانده ستاد مرکزی فرماندهی ایالات متحده (CENTCOM)، به نیروهای آمریکایی مستقر در خاورمیانه هشدار داده است که ویدیوهای ضبط شده با تلفن همراه و منتشر شده در اینترنت، به ایران کمک می‌کند تا میزان اثربخشی حملات خود را ارزیابی کرده و موقعیت‌های نظامی آمریکا را شناسایی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138413" target="_blank">📅 14:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138412">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyxjOn-_9fRy440YGJ9S8RGiwNz7cqgehPg6dnEpgGHs-_kUVBAcrM-Sy-cWP8xz_RDZpXVAshO_ws9zbt3PiX8ujDr1vF4CQvRC3ij50ZhDqV160YlmSn8zbTRIiQG8uuqH428hSnANLu2MMW-S_Pk9Xi9aCEADZ-DOb2S5XPojhtNv66i3HYyvKAY8pRcVc0aW7VNCavX9suJivCHq7hfKkAynqh-I1RhC3vEb1iSyddGyQx6yEBI5yUhcm9QZbDRmcAUShbfzSJENqXwE34VX1rHW3G8qPKixvz9tKAAkme0qWctLdLLyuz9QK7sBTmbzd6P5H8SfTG73SiI3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده، حوادث متعددی از جراحات جمعی را که پیش از این فاش نشده بودند، گزارش داد. این حوادث شامل ۷۰ مورد جراحت در ۱۸ مارس و ۲۹ مورد جراحت در ۳ مارس بود. در میان مجروحان، دو ژنرال به نام‌های کلینت بارنز (سرهنگ) و براد هنسون (ژنرال) بودند که در جریان حمله پهپادها به بندر الشعبه در کویت در تاریخ ۱ مارس، دچار جراحات سر شده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138412" target="_blank">📅 14:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138411">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
لاوروف، وزیر خارجه
روسیه :
روسیه مورد لطف خداست
🔴
وقتی شرایط واقعاً سخت می‌شه، کمک از بالا بالاها می‌رسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138411" target="_blank">📅 14:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138410">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دقایقی پیش، زمین‌لرزه‌ای به بزرگی ۳.۹ ریشتر حوالی سرگز احمدی شهرستان حاجی‌آباد را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138410" target="_blank">📅 14:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138409">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مدیرکل مدیریت بحران آذربایجان‌غربی:‌ یک پرتابه به یک منطقهٔ خالی از ابنیه و سکنه در استان برخورد کرده هیچ تلفات جانی نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138409" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138408">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رویترز: یمن در حال بررسی امکان وضع عوارض در تنگه باب‌المندب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138408" target="_blank">📅 13:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138407">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری / بنا به گزارشات دریافتی، دقایقی پیش نقاطی در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/138407" target="_blank">📅 13:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138406">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
اکسیوس به نقل از زلنسکی :  رابطه‌ام با ترامپ خیلی بهتر شده
🔴
الان رابطه‌مون سازنده‌تره و مثل قبل دیگه این‌قدر احساسی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138406" target="_blank">📅 13:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138405">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d865add6d.mp4?token=u1Vov9bObfpvsfh5NWUHP2OYbwtIdxDUMRsJUIwlLiH5u7wUecyC4pG2Rg7R9DFdJZrXZXFrFZ-E6OawRE9pOW1peS5CX2PN5Pt2SXNBeQBm8oDuUGE4nflfLgt0hcmOqIkTLNDsopTR8WfwomY58iFuV9aW_ADz-pDLNbdqCus8CvNr6C_w6XwCOYobqfh_swlCpHoNj7T3sF1fyu1r0UNazHTnDZ7H2BbEWlJae9jyLxH6aUyr_VZkZ8w9ERXlaFRvFPLZPD_XpBC_eLNisrMRAzVF0TPKbxCgN_bjF8FN3R9q-xBI0lTcvXBn1DGhNSzNlbcLR0R_9SZ16O5zYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d865add6d.mp4?token=u1Vov9bObfpvsfh5NWUHP2OYbwtIdxDUMRsJUIwlLiH5u7wUecyC4pG2Rg7R9DFdJZrXZXFrFZ-E6OawRE9pOW1peS5CX2PN5Pt2SXNBeQBm8oDuUGE4nflfLgt0hcmOqIkTLNDsopTR8WfwomY58iFuV9aW_ADz-pDLNbdqCus8CvNr6C_w6XwCOYobqfh_swlCpHoNj7T3sF1fyu1r0UNazHTnDZ7H2BbEWlJae9jyLxH6aUyr_VZkZ8w9ERXlaFRvFPLZPD_XpBC_eLNisrMRAzVF0TPKbxCgN_bjF8FN3R9q-xBI0lTcvXBn1DGhNSzNlbcLR0R_9SZ16O5zYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع چندین انفجار شدید در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138405" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138404">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وقوع چندین انفجار شدید در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138404" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138403">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گزارش انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138403" target="_blank">📅 13:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138402">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مشاور ارشد ترامپ: "ایران می‌خواهد حزب‌الله در لبنان فعال بماند، ما اجازه این کار را نخواهیم داد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138402" target="_blank">📅 13:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138401">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrWP1pwfWKh8f6tpQfaGJ17ls1lgVBQviCub09Lj9OVbb-bQ8FraPeaFtE7ea0mEulayRoot4IFDIGoIhSgHQJ14jALich7dI0WlSGOpE_XSCIObW7z-663voxAM7PNHeuEXE1RrVM5S8E8IiJD84r03EVCXKKomxD5gOF2fZjD9RiBfU4SXIG3iAGn1Q4qVpGuSXKczQtpsdJaxN5L3gFYX3rTeMoioLwL-SdTC1_SxLMMZ51p6EgjM_ThXgsE7PPLtASiwyjLBa6qdSupGTwEeoGhQOnVNk5g4m1WHryGKhxZ-_T4oZ9pRptIqgwfnRDQoFJXPXrJhGgQyGhMtIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با کاهش ۳۴ هزار واحدی به ۵ میلیون و ۷۵ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138401" target="_blank">📅 13:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138400">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag2Q6t9FXiHMEXIftmx9QsljX0c4AdvvQi_fzTE_pyTjpqITDN9N745Q6mhXDU5QOfmNwATlRqsjhVTZzdQpfslSFnwDBJoP_CHFR0-7NgiTji0DisMw8nCK_P7P-PhFtqeNGO2vKFKB2CyCQiNtjX_4gfhgtB0H2TYIOS7j4vHg0SQGRNBSOc-nEq8O_3tEBFnG0gA62qBOjCjTewdqrGpzey1HdnOg0s2fKfFQiWq6KbPMGqn8E5kHG3OXXaDTedtz7UBu8hbfPDncoizk_sikNvD4jGJ1eUMwRUeJfQiJArHcnxq4jsTF3Y_BFr61c7UJ4qj82HJVB5YcEnN0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی باری که پرچم پاناما را به اهتزاز درآورده و نام آن "جدة اسپرینگ" است، حدود چهار ساعت پیش در مسیر تنگه هرمز شناسایی شد. این کشتی پیام سیستم موقعیت‌یابی خودکار (AIS) را با عنوان "بدون خدمه سعودی و نگهبان" ارسال می‌کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138400" target="_blank">📅 13:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138399">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سلیمی، عضو هیئت‌رئیسه مجلس :
ترامپ و نتانیاهو دنبال کُشتن «رواجب‌القَتل» و «مهدورالدم» هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138399" target="_blank">📅 12:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138398">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دلار هم اکنون 193,400 تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138398" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138397">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرگزاری ژاپنی:
چند کشتی مرتبط با ژاپن که در خلیج فارس حضور داشتند، از مسیر مورد تأیید ایران از تنگه هرمز عبور کرده و از خلیج فارس خارج شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138397" target="_blank">📅 12:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138396">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پس از درگیری های دیشب خاورمیانه، یمن حمایت خودشو از عراق اعلام کرد و کشور های عربی حاشیه خلیج فارس در یک بیانیه دسته جمعی از عربستان حمایت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138396" target="_blank">📅 12:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138395">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نرخ بیکاری ۹.۱ درصد اعلام شد
نرخ بیکاری افراد ۱۵ سال به بالا تو بهار امسال ۹.۱ درصد بوده؛ یعنی نسبت به بهار پارسال ۱.۸ درصد بیشتر شده
🔴
بخش خدمات با ۵۳.۸ درصد همچنان بیشترین سهم اشتغال رو داشته
🔴
همچنین تعداد افراد غیرفعال اقتصادی (مثل دانش‌آموز، دانشجو، خانه‌دار و بازنشسته‌ها)
🔴
به ۳۹ میلیون و ۵۳۵ هزار نفر رسیده که حدود ۷۹۶ هزار نفر بیشتر از سال قبل شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138395" target="_blank">📅 12:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138394">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با کاهش ۳۴ هزار واحدی به ۵ میلیون و ۷۵ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138394" target="_blank">📅 12:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138393">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ادامه آتش‌سوزی در بخش ایرانی هورالعظیم؛ حریق به دایک مرزی رسید
🔴
محیط زیست: احتمالا علت این آتش‌سوزی عامل انسانی بوده
🔴
مدیرکل حفاظت محیط زیست خوزستان از تداوم آتش‌سوزی در بخش ایرانی تالاب هورالعظیم خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138393" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شرکت منابع آب ایران: شرایط آبی کشور در وضعیت نرمال قرار دارد، ولی بارندگی در ۱۲ استان پایین‌تر از حد میانگین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138392" target="_blank">📅 12:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138391">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
👈
فروریختن یک مرکز خرید بزرگ در ژاپن در پی وقوع زلزله
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138391" target="_blank">📅 12:19 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
