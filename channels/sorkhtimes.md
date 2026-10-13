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
<img src="https://cdn4.telesco.pe/file/NZf9GTd3-HoeHcy01KZj-tdBotdXIX5dqqoBneD59t5sjPKhzBQsbcdN2zxOGM8JAUnAS6oWGT0843YNdbbr5aAniiZQYqSt1wdqsY2wxCIUcIFkjsSAiRkSaO-Ijd5Zu_PYI-clNAjJvi2VjeAvOnZWcq-qmfFdtKxl_z5S8h5zW3FvyAsChEKMJybN4OB04wV1VKsKwWSbIzuAiXTwQ7KS0WXkKuXGoSE8leST1dcMAUGzNUsY28GAwDT0s1boWg63MMM4qkkfnh_uU9eR_bnTxUCyT7KGXZ5KUggPwbB9laFSJx-EfUq7Hr4C8yc_-lMnexKBJEM78ZLMTYawyw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 08:11:45</div>
<hr>

<div class="tg-post" id="msg-141380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9HiDHD3T7LJAs8_byxYPR31qcTIHtoKrisCvhfnKEeDtJQwQzLKVVxnLXNlFRDpJ-YFiX5_MIyHmU8KArDAhfQTq6k7lYlu0uAcJhPJYsyChQHIAYLoU0CdAkIsOB3XmviCxSX9SCRrLjuAaT_zdd3xKccDFlldUhouHkZKxOeRLz9S0XD2z-dtvpPslRVUGGUm1buptbun0Zmpk33dkusbtdRS_uIKvj4xKE7YLqhVPyXnU5c2Dr-H4TAkx40sFiMzDFbeFQyUswcf1s0mlwSPzbvXRiVz5oprgxQpO1BJvfGMaEVfELJv6Tl5JHWHDJMaLGCrmAhczk4wiOvgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب اروپا در تب‌وتاب شب‌های سرنوشت‌ساز؛ جایی که غفلت، تاوانی به قیمت امتیاز دارد!
🔥
⚽️
فرداشب آرسنال با ضریب ۱.۲۱ و اینتر با ضریب ۱.۲۳ از نگاه ضرایب، مدعیان اصلی پیروزی هستن؛ بارسلونا هم با ضریب ۱.۲۶ شانس بالایی مقابل گالاتاسرای دارد. تقابل اتلتیکو مادرید و منچستریونایتد با ضرایب ۱.۹۱ و ۳.۶۴، از جذاب‌ترین بازی‌های فرداشبه؛ درحالیکه ویارئال و ناپولی با ضرایب نزدیک‌تر، رقابتی متعادل‌تر رو نشون می‌دهد. دیدار لانس و اسپورتینگ هم اختلاف ضرایب چندان زیاد ندارند و همین موضوع، این مسابقه رو به یکی از دیدارهای قابل‌توجه کنداکتور تبدیل خواهد کرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SorkhTimes/141380" target="_blank">📅 01:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/141379" target="_blank">📅 01:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
⭕️
⭕️
هومن هدایتی مشاور حقوقی ورزشی:
⭕️
استقلال تخلف کرده و باید منتظر حکم سنگین باشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/141378" target="_blank">📅 00:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
با توجه به مصدومیت حسین کنعانی و دانیال ایری، زوج خط دفاعی پرسپولیس برابر صنعت نفت آبادان، محمدمهدی زارع و حسین ابرقویی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/141377" target="_blank">📅 00:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
آسانی که مصدوم بود و جای رزاقی نیا اومد تو زمین ...خود آسانی مصدوم شد و از بازی خارج شد
😎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/141376" target="_blank">📅 23:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890159133.mp4?token=CLcJu9DOewlA5ZRDmtPwWeZbCqoxXnvpIBABAFQ0uiwjMhxwmzVALIWsCqMtgwP36L59KazmIN0y__X5rz69taAls0xut0avbZmSeokmcVhr_ulzqNCpjFHno92nt5iy1CGBs6xadF7JNiJnHFJ-BTZTBVjYyxL8gh63_tpRpZhvTxcORA7bM5vcmTcOrpg4xEgM5re08cTWU7nmDtYDtRaJKxyXsdg-qjCwQAo77FohvcvqLbBJMPoGIMNioGXB6QtWLd1wKS__sF5mwmH7j-f4AH-Lg-ZrPLSoWolrV3GLXdD7m354Tm_0MJeoSmn6fv-g7znK3ufxrf9W_biG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890159133.mp4?token=CLcJu9DOewlA5ZRDmtPwWeZbCqoxXnvpIBABAFQ0uiwjMhxwmzVALIWsCqMtgwP36L59KazmIN0y__X5rz69taAls0xut0avbZmSeokmcVhr_ulzqNCpjFHno92nt5iy1CGBs6xadF7JNiJnHFJ-BTZTBVjYyxL8gh63_tpRpZhvTxcORA7bM5vcmTcOrpg4xEgM5re08cTWU7nmDtYDtRaJKxyXsdg-qjCwQAo77FohvcvqLbBJMPoGIMNioGXB6QtWLd1wKS__sF5mwmH7j-f4AH-Lg-ZrPLSoWolrV3GLXdD7m354Tm_0MJeoSmn6fv-g7znK3ufxrf9W_biG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گل شماره ۹۸۱ اسطوره رونالدو
❌
پ.ن فقط 19 گل فاصله تا آمار عجیب و غریب 1000 گل مانده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/141375" target="_blank">📅 23:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/141374" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osMyJb6m7nJXPuZ1EVLcgD2WCOH7KBy-oY98xeZBddqiSHlMI4enEXCZ-BdW8wi-dayxUf2MRt2ijCbzF776PqCZmo3-rLsRAgYJzF_tnaxDfMh0gNNAXrAfIYy6CxR5nULTGymLNNC_wl52C5q2MFTt0PvgOSz2lVFv5Agopifvr3zMDhGDF43u6sxbCrL7zpqrSt8SqB2kxSnc52J_b0RJRaaIRvtcd6fLFrviis_m97B2Ky3YxzVdERbJnUHPxGlq9lqSbMekIj3is0lTI8x284lHDmeOCfX0ZE5QKJOgXyL7ejWuxtU0LgzTTChhqe3uEIYrXUAt9oWyKioPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زوج خط حمله مقابل خیبر
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/141373" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS1WJS0qQR8ToDwoE8uPoytp5DE_OlFCmcjjXyb3gAKghP6zAZUvao2nZ9zkQT0LMgfqJtyseoQ_SbNYU-yQHbl6R1ZNAIIwBKnFlv01uf96QDZmIPsuwul0bLXE5ujYh_1KpZK1jMjmHE0uEl1Fp7EiqOlvv1jW9s3ISFArmiekh1oF422BkFUX-Q_P7MO8Q1bejbMyh6Lfz8qQFhwUNcQkxT_RLeK74P3MV4BAZ4yCbtAzJogx_SmwnrWSzgR6HtKYSAQgiUyx_BEYI9RNQnAH0_9Dn5PA4aiOL63f5IP2wUQfCgSWNTJ1d41RrD_4M30hpyCNuhZerCzCb9wHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
احمد کونِ دروازه‌بانه الغرافه واقعا اسمش برازندشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/141372" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/141371" target="_blank">📅 23:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
الغرافه گل مساوی و به موقع به کیسه زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/141370" target="_blank">📅 23:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141369">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/141369" target="_blank">📅 23:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141368">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/141368" target="_blank">📅 22:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o35eiM3KE9bCDkoaF1A-3noYOO2nKxF5NeH3xnWjj59ZnY1YkA3X5ZM7I8z4NMGK1dq7M34mi5qnP8b1CNZ41HXfsCVSZuqV67btEgBn_9Sj6VAaiDVEF_MlwGCeSsDcYpXixcvJKiAC-kB8F-hwc98N1vtoMYoLIQCUGmJupb99YjsepNvFg7_J6SNFbSpBy0v9qhVqvlynpFi6aXW1m1SEVPGFsu9ZdwbTmSeWj-nwvfxK-bo1OXLou06-L9ul8FEuATEUk44h8SCfeIItVCBsptQC9gys2mI7mO2nh0DyjynpC6Y5UqhMbZJfFrS9-SUJa3JRRYM5fw1GlngZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پویا اسمی مقابل خیبر هم دقایقی بازی خواهد کرد/
فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/141367" target="_blank">📅 22:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/141366" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔵
💙
🔥
نماهای دیدنی از سوپرشوت یاسر‌آسانی روی گل اول کیسه به الغرافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/141365" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
احتمالا بازی های تیم های بزرگ عربستانی هم مثل ایران به خاطر شرایط جنگی شرایط میزبانی و دیگه ندارع و تیم های عربی هم میزبانی خودش و باید به کشورهای ثالث ببره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/141364" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
بازی کیسه و الغرافه هم شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/141363" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141362">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/141362" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=VC7NXrXW_GrKZSGG2ALkoo1zsVRg0peHFvqgitDjfEPbibDEnDBar7PcQnk3U2BwgtVVS8uvkxc5Y61n_e6Nsq9aWW_VPPaCnQ2YbzgGk37oinZGIM_eQzw_nDM2_JtjkYLl8qJ41Kw4wgEHqvOkY0qjFGacypLW8X7WNZmkQ898S36HovzJ3PlkqHS76mY3PO_q8Y9ixbddTdcp6hjBCZsSCp_16rG7mfJ3amhq1k3yc3yFrtofhuEWN0JAL3yt-dVJZJyKsDDJLjk0Qq5swt_UMAmAKhwylEThDCD14ikFh4PDE1SdMRE23gjmpqq53QBXGsEK2g5YMZlzNszwtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=VC7NXrXW_GrKZSGG2ALkoo1zsVRg0peHFvqgitDjfEPbibDEnDBar7PcQnk3U2BwgtVVS8uvkxc5Y61n_e6Nsq9aWW_VPPaCnQ2YbzgGk37oinZGIM_eQzw_nDM2_JtjkYLl8qJ41Kw4wgEHqvOkY0qjFGacypLW8X7WNZmkQ898S36HovzJ3PlkqHS76mY3PO_q8Y9ixbddTdcp6hjBCZsSCp_16rG7mfJ3amhq1k3yc3yFrtofhuEWN0JAL3yt-dVJZJyKsDDJLjk0Qq5swt_UMAmAKhwylEThDCD14ikFh4PDE1SdMRE23gjmpqq53QBXGsEK2g5YMZlzNszwtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/141361" target="_blank">📅 22:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
واقعا ی بازی خواب آور و بی روح و سرد و مسخره ...بازی صفر صفر تمام شد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/141360" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
پایان نیمه اول |
🏆
هفته دوم لیگ نخبگان آسیا
🎙
تراکتور
0⃣
🆚
0⃣
الشمال
🇶🇦
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/141359" target="_blank">📅 21:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
حجت کریمی شلنگ رو گرفت رو بیرانوند
😂
❌
❌
حجت کریمی: بیرانوند سال گذشته 100 درصد قراردادش رو دریافت کرده، در حالی که طبق مصوبه سازمان لیگ تراکتور می‌تونست 70 درصد قراردادها رو پرداخت کنه. امسال هم بیرانوند 35 درصد گرفته، در حالی که بقیه بازیکنا 8 درصد دریافت…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/141358" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141357">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRSaI4I0im9iLir2M5k_TH0OydMKh14mdFZY0XEr_geoaiUP00MrebatrVedwF3sUtKcXPQmFnA-dnjuEHm5PGw2hFj0dk-iKoiepTikS7cb8JbYH2Met9lElvrqqDq43cuiy1aI4zsHMskYLHbw4zQ8h3HjOSbYbNgafOI7O8x3WWwIPIkyhjfXP686kHnDeFhHvMu1ZVOL4o56DSgtrMY7V6yKrNFz1F3yw3MtTho9V_2O1DuF-2GKiK4ssNIbVeC2cUXObT-oL-Ody9UGW27F2XItJnXQuYLuodgktRpg8utpaBT91KaBT8AnpvfJSxKbR5SNviw92gJEptGueQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/141357" target="_blank">📅 21:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141356">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
سرعت، برگ برنده پرسپولیس تارتار
🚨
فرمول تارتار، ضدحمله‌های سریع و برق‌آساست؛ پرسپولیس با چند پاس سریع از دفاع به حمله می‌رسد و حریف را غافلگیر می‌کند. البته تیم‌هایی که دفاع فشرده داشته باشن، می‌تواند این تاکتیک را سخت‌تر کند
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/141356" target="_blank">📅 20:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
فوری؛ کد سربازی علیرضا بیرانوند فقط برای فجر  صادر شده و راهی این تیم می‌شود. او به دلیل تأهل و داشتن دو فرزند کسری خدمت خواهد خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/141355" target="_blank">📅 20:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f780d2f1fd.mp4?token=sESvdoSPsGNXomm5nTsVEekoChaVBauZL7aI3rKkRwP0FfuesEpLObmHLiksfO3FwR8xY-g4uU0mq2IMZSdp5o5gtXTzemXEeFdO5tQvYVLGDiorbFT-FiNqkja2EcN0uz2hB8ewKFTgk6r-pzjZptrqmLD1jZb_vGiJCv0WTe4yT4eW7PfqQO4ohYJ03sWBH3T4bGFpjqFB4p00U1mPTo-eW-k1a7nlVr7-eTqfQjYLEbXPF8SwpqfUwsz6ltSlwrjtXPt194fiJpvcJSOxluRUX_59qcOyNv84FD4Bw7NACVnzVbp-Tl3XVrb7uAJk3xR2dIswe7OMVtadPVKm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f780d2f1fd.mp4?token=sESvdoSPsGNXomm5nTsVEekoChaVBauZL7aI3rKkRwP0FfuesEpLObmHLiksfO3FwR8xY-g4uU0mq2IMZSdp5o5gtXTzemXEeFdO5tQvYVLGDiorbFT-FiNqkja2EcN0uz2hB8ewKFTgk6r-pzjZptrqmLD1jZb_vGiJCv0WTe4yT4eW7PfqQO4ohYJ03sWBH3T4bGFpjqFB4p00U1mPTo-eW-k1a7nlVr7-eTqfQjYLEbXPF8SwpqfUwsz6ltSlwrjtXPt194fiJpvcJSOxluRUX_59qcOyNv84FD4Bw7NACVnzVbp-Tl3XVrb7uAJk3xR2dIswe7OMVtadPVKm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پیمان حدادی، مدیرعامل باشگاه پرسپولیس، به مناسبت روز دختر در محل تمرین تیم فوتبال بانوان حضور یافت و با اهدای گل و هدیه به اعضای تیم، این روز را به دختران پرسپولیس تبریک گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/141354" target="_blank">📅 20:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
بغداد بونجاح و ریاض محرز، دو ستاره الشمال در بازی امشب که شروع شده مقابل تراکتور غایب هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/141353" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141352">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjpbeYpgJNR7I_jpHEajR1inRdTJm9oVGz9VuIkR1XhLRrmP3rGYmCBGlNW__8Jq4fuXblmD0Iuii83TWXw5_9czxM-Vu0L8L-v9dSIIhWCVxUM2m8ESh5vixs8-AhSGS0HmsaadX_fs8eSRNpEtHE-l-sLjOYzRjfyEvI6GJnvjuyWUwUn6_Th_PYn-PziOzAvM3L3a3LrhY29SzXnMxfWqshC4VGLN6pPz2oBCHGR1FkPqbKw1aoCo8JqvzlXgnDN7m0SqArOOEqFhmOISgEyy2alMlUMKzztYM6FW74jjNRyCg2pkk978bpSwCK-tLfuLM7dCWnNMIa3Blz33tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Al Gharafa
🆚
🔵
Esteghlal
⏰
Tonight 21:45
🏟
Thani Bin Jassim
🟣
الغرافه در ۸ بازی این فصل ۱۷ گل دریافت کرده؛ نقطه‌ضعفی که استقلال می‌تواند با حملات سریع از آن استفاده کند. استقلال با روند بدون شکست در ۹ بازی اخیر و برد ۳–۰ مقابل السد، از ثبات دفاعی و اعتمادبه‌نفس خوبی برخوردار است. با توجه به ضعف دفاعی الغرافه، گل‌زنی استقلال دور از انتظار نیست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/141352" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141351">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/141351" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141350">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
| ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/141350" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141349">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✖️
✖️
✖️
✖️
با توجه به درخشش مهدی تیکدری در پست دفاع چپ، پرسپولیس احتمالا بازیکنی در این پست جذب نمیکنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/141349" target="_blank">📅 19:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141348">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[ تراکتور
🔴
🆚
🔴
الشمال ]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/141348" target="_blank">📅 19:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141347">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/141347" target="_blank">📅 19:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141346">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVpswjkvlO7IUdLbDQjLMJYdsXCs265wHKhMJpXpZO8qyoqfNs0YR3zBwGzI-YXbSvZpGKNEKMfcZRk93eib-G_KG-8evon5hThUh5t8ceeVtxWICVdLAgIJBqQGb1glx_tNlnonl8ifTuG1wRH-PK-0O8SO3zDcb-V7G8ezbcsbkyNrhoyZ8WOfdNYzoBj-PJMsSrVmmSwOTYTCE1YxGPc7XpAHKaI9c72Nr9Ejen7ppTBut3wTGecNIq3nzmDFtG555cX0FW901RnXZCzu1XK8-XJW2d6NgxTdCCnjdlnwP1nrsBdFRgGdHd7K5idOak87AZyws20AtoJuw7eQ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/141346" target="_blank">📅 19:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141345">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfKbdqhwqqm6PIk68QFTwvyfWWYwfDjpzySJo1PgA-WEo-395X1uMx4jDmYLRlrwbDjLYqzsB-cgRriD_cKMLPBuh8JBsiixsmF1rVTmijNjhP3oDSkkByw3_krAsvzrpPTEZ6QQpMnhAiZRI-IFoQkkDodGF-a0pNQA94H272K0JKXKwUCdpnBLjqOHLjneTIkrbHnL8JnKRU-rUx2FYviH1kUpKQNFIjZbQ2ah6fuVqB9GCr1iR9w3W7r1tKVUCHS19NdQf4VJlYRt51u_UJD9YdF3qLbcqvCU9OWR4rktoI-RdeuzL7Yw1Xn3JurnGeev4euXLaJyUAMq5-e5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
مهدی‌تارتار به مدیران پرسپولیس اعلام کرده که اورونوف غیرقابل فروش است و این بازیکن باید در تیم بماند. تارتار معتقد است که با وجود سن و سال بیفوما، حضور اورونوف جوان در ترکیب تیم ضروری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/141345" target="_blank">📅 19:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141344">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGelBa_HnPTKaQnywMxmA1EqA7GJjH7sBhgOHGud4NI9On7VjmKOYe_y24YO5ixk11RASDhrK5Hhx4N6Ee-YRsaMHQBIgJQd2-cfruuMzVvEtDnScjtDM9i-nDBK8TDX2h-jxiZQGFH4_NKEvALW1_pBpwN6FqYrguBrMFusYKaLDOZ6u_SpRJHjd_nNFuyjcoIDZ5IHCEtt03OZUoy_DXxEBZYmc2ha4YIu3fhEnY2gykFMK0o8YTQDSCwdb1IXjpNI-Zq-0MT3AYu3NKQYabEmC1BB7tgmmZpfPIGrqOIRTsMxB90BkLpdvvfn27Otj9VEjAMP1amg8KTcQG5SuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
|
ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141344" target="_blank">📅 16:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141343" target="_blank">📅 16:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141342">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
رد درخواست پزشکی بیرانوند  اول آبان؛ اعزام به خدمت سربازی
🚨
🚨
ماجرای سربازی علیرضا بیرانوند سرانجام به پایان خود رسید و این دروازه‌بان باید چند روز دیگر عازم خدمت شود. دو درخواست پزشکی بیرانوند در این زمینه مورد بررسی قرار گرفت و‌ هر دو رد شد.
🚨
🚨
آسیب…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/141342" target="_blank">📅 15:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141341" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
قضیه پرونده آسیب کتف، پرونده اعصاب و روان و خالکوبی بیرانوند در کمیسیون پزشکی پذیرفته نشد و به صورت قطعی از اول آبان سرباز محسوب میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/141340" target="_blank">📅 14:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141339" target="_blank">📅 14:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
اول آبان؛ زمان برگزاری دادگاه پرسپولیس و بیرانوند در CAS
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141338" target="_blank">📅 14:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucfrIfVsF0f-m5sS8NOwbafHL04yJt2TF42dtbEAT1ykpRJCC0HRYnqZzil_vuB1-kdX7_iUR2r0bbYMCOtq1FWh06cti53ih_GZzf6Gxlw7gfqkpkwMpSk4T7FKmN96-uZnN--1IT0LCdnRHL2QChVwRal5QW7dRy5rHumfWqiNTKVJo6rkNwNRHs9GuHGpOd52IdH71YoZLeTxelUqqjlfB-Ciw3XQ1A6FS-gchY01Cx-uLut1aML_0LvCYLBfTLFRVgQOHDGoFGD3siRfhzI_rlT-1QvNyIECK5F8erJNpV2hd7rhx1XN0EKOYdhFWcR4AywZBDqP3ti9FN8KLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
استقلال در دوحه؛ جدال آبی‌ها با الغرافه برای یک شب سرنوشت‌ساز!
🔥
⚡️
[
الغرافه
🟡
🆚
🔵
استقلال
]
⚽️
الغرافه در ۵ بازی اخیر ۸ گل زده اما ۱۲ گل دریافت کرده؛ استقلال با ثبت ۶ گل زده و فقط ۲ گل خورده، آمار دفاعی بهتری دارد. استقلال در ۴ بازی خارج از خانه فصل، هنوز شکست نخورده و فقط یک گل دریافت کرده؛ نکته‌ای مهم مقابل خط حمله الغرافه.
سناریوی محتمل: بازی نزدیک و کم‌گل با برتری نسبی استقلال در فاز دفاعی؛ الغرافه با استفاده از میزبانی فشار می‌آورد، اما استقلال روی ضدحملات شانس گل‌زنی دارد.
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
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/141337" target="_blank">📅 14:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
بیرانوند به کمیسیون پزشکی رفت؛ در انتظار اعلام وضعیت نهایی
🖍
علیرضا بیرانوند، دروازه‌بان تراکتور، روز گذشته در نخستین جلسه کمیسیون پزشکی در تبریز حاضر شد.
🖍
بیرانوند که به دلیل خالکوبی به کمیسیون پزشکی اعصاب و روان نظام پزشکی ارجاع شده، همچنین برای بررسی…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141336" target="_blank">📅 12:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
باشگاه تراکتور به صورت رسمی به علیرضا بیرانوند اعلام کرده حق حضور در تمرینات بزرگسالان را هم ندارد و باید به تمرینات تیم امید برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141335" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyIUvYW8qsTuZf4ZfXk4RRwbsePieLpJimRUZ4yV1zzqMLuOkA5a6OZY-LotmwYwWAIs8znvNk4dvBuGMSNao_Ib_8DRSH--nPjCvqVp1IjS6_NalWQSj3kYndEAPq5EcRCR5CF7f_VOi8UnQ38I9oXPEtYf6snJCJQqKIUaTP3CV3on9dZh7d1h5K7obCVjmalDMS6p0kksJTUKFxjzjBXmeEF7Pt9PO2WmMMJFdydsZlTSF0NaiXlsi7x8SDGGzrgeehzyyXePDi4da3TrywL7tv19fI_eSLvB1j3TjY8bCfVbrawOADymX2HZoV90VNznvXjoIVBrX6OG3MesrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پوریا لطیفی فر در بازی با نفت نتواست عملکرد خوبی داشته باشد و مقابل خیبر نیمکت نشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141334" target="_blank">📅 11:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🆔
| ورزش‌سه:
🔴
❤️
دانیال ایری از بعد بازی با خیبر در دسترس کادرفنی پرسپولیس خواهد بود
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141333" target="_blank">📅 11:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiGBKAQlaQXpTCU4gxPcq7vHaWSLM9ryO3HMt6Pjt4wJZ0TPrqQVqtaAA4yxopQz8VXGBPdnzZQo_JRmScblcAbGiyVrRVPpnOfjFIzdrrCCuKLEBqYNvI27xu2spTmSScRj0wd8rfrKAk9lx_hMamCy-d2N_sok3STZkJ9ZD8luOlSVhlpjnL6ClucUMeI2-JqUmQiF3XzmKd-vUTf3M3qTzI7owWUZXDPzdp2zBAJKWoUel0YBeoDcOjH-LYqNgA91kk3ODP7BQ6otlRs-qjCUyGd0MzYkcyBc42EYJlJetp1FZ9qyiis8qCNN4LdYBWftPEZwy9bPuutCeYzElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اورونوف با به ثمر رسوندن 4 گل دیگه، تبدیل به برترین گلزن خارجی تاریخ باشگاه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141332" target="_blank">📅 11:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
| فوتبالی:
❌
مدیران پرسپولیس در دوراهی تمدید یا فروش اورونوف قرار گرفته اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141331" target="_blank">📅 11:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🎙
تاج :
✔️
امیدوارم ورزشگاه آزادی بهمن یا اسفند امسال وارد چرخه مسابقات لیگ برتر شود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141330" target="_blank">📅 11:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❤️
محبی؛ ترابیِ جدید برای اورونوف
⁉️
⭕
محمدمهدی محبی در ۷ بازی با ثبت ۲ گل و یک پاس گل، عملکرد قابل قبولی داشته است پاس گل اخیر او روی همکاری با اورونوف، نوید شکل‌گیری یک زوج جذاب را می‌دهد
🔴
محبی می‌تواند با تبدیل شدن به مکملی شبیه ترابی برای اورونوف، هم به…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/141329" target="_blank">📅 10:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO_OEFfR_XL0ZOtbOLFTzYTAXpHm54QAcbI8TYMYg5CEChRHLEUAxkWXDWFyF-tEXSGM3e7s0K3eF0954m4wY3yyfrCdqnZdw016TwdTnSLof2TsMsq6BnbIrdqNKVdTwXXuMU61suHhdddszOJMQ33nBuNqMR4Wij7BBUQzXVyj5VCg65KQ1FyCxOJTMG1z2i7skVADpqyxebK5jZhXZRVv1d6yfpG7xjx5ITI3ODjT6ztnaIvGl2XXQ8jZLIrMUJ-y9JXAKvdcqO1TJSDD6SsvPv9rML1QfnEhMhg2hD5ARKhOV_Rr3NCjKJuXlc77qvMfSj5OqqgE9aXnFiE3xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141328" target="_blank">📅 09:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnS11Vd6croGjTXyrLP23dAPy1yctOMslUDyzK0to2XjfCtvVQMOK6GZE_RsXZAK9wFTHwBQeeOx1WvzFTGYSX16wl-OU9QEXnNjb1GDmlrIK0USkETu5dbzaSDbk9ndaTy-1t2zwpHuYkJQXueMMX5Ua28KtN3KdfWGs964scD7RmvLh77iaWPJPE9rcF9FV-eJBF612DuXqN9EVJEolVNI5SBLKTfrYT0iCMP0ZgpE61YQnVH-Zu8a_bMtzpjnMG6GQC6JbPoLAh15jXaaITn9rlCR-XwQCHaDzvkgJpqQyA1_vb7JM7k2AqCfRgXiNzS_WYlRkrbJSLIk_aPIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[
تراکتور
🔴
🆚
🔴
الشمال
]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط حمله خطرناکی دارد؛ اما میانگین ۱.۶۷ گل خورده نشان می‌دهد در فاز دفاعی آسیب‌پذیر است. تقابل قدرت هجومی الشمال با ساختار دفاعی تراکتور، کلید بازی خواهد بود؛ تراکتور شانس خوبی برای کسب امتیاز دارد، اما غافلگیری در ضدحملات دور از انتظار نیست.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141327" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141326">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141326" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141325">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKemoq-7A8WosTt9itt_H5RtK9YSH4qrWZHT7_mfbwb6LXid0XYNdJcQ8ep6otHPAaLGhdRa0OE60xNX1BIBOCFg2yBvFFvSQw-Bfo2qKskO6k_ocg8CJczGE4wcSiLGiiItW_TKvv-y5OHNTzkuirYWXPJFBVtp2N4nZOaNlJQ3CsHSgBAO-Xog8uQJz1MozWtedBThPk6OtjcGtbvmJn_Ll7jTVDcg6-SUDy8im9lAVtvuOKUX--qVGtMZQ9SpQ3KE0Q8YdByXMLW5lcB42nYnR2EiIpyWOa2gBw_GhYjl2EoeQssgK2IWOQ7AI99GoLIwb5d556dwBRxIbLDalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/141325" target="_blank">📅 00:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141324">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=pnu8Y0q_pSnzwg19QXPWInEpdBneSxJA-BhqK0xTwEzpghqUcUZeLeLKP--3IHiNPbfcF09T7UyKFW5CCJBJyB_7bjMaj0ckhr8ajOJvsdSwAOC5yLcnUHpPTJuLyuzT-VjVt2RpdN1drBCRPSt-y9w8jI51k6oTHN1zoSiTpahgugz4-ZReO8Ff1L-PZOVJwyQDVkrwmi6TEp3DzGYGgEsZlQ3HYX4Tu_dBiqyRdKsVYWj6bnxLv0TEOEEF1DzO3awLVKrt32Pc38w2yzVeRQSIHX0Dn5gaQw7xgEMkNshp6ItugzujMs95AMEmh2WZOrBjf9Sm6pX7NsYt1S_U94i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=pnu8Y0q_pSnzwg19QXPWInEpdBneSxJA-BhqK0xTwEzpghqUcUZeLeLKP--3IHiNPbfcF09T7UyKFW5CCJBJyB_7bjMaj0ckhr8ajOJvsdSwAOC5yLcnUHpPTJuLyuzT-VjVt2RpdN1drBCRPSt-y9w8jI51k6oTHN1zoSiTpahgugz4-ZReO8Ff1L-PZOVJwyQDVkrwmi6TEp3DzGYGgEsZlQ3HYX4Tu_dBiqyRdKsVYWj6bnxLv0TEOEEF1DzO3awLVKrt32Pc38w2yzVeRQSIHX0Dn5gaQw7xgEMkNshp6ItugzujMs95AMEmh2WZOrBjf9Sm6pX7NsYt1S_U94i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/141324" target="_blank">📅 22:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141323">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
پشمااااااااااااااتون بریزه
‼️
🚨
🚨
🚨
با دستور مسعود پزشکیان رییس جمهور جمهوری اسلامی هواپیمایی مخصوص رییس جمهور برای سفر مستقیم استقلال به دوحه در اختیار تیم استقلال تهران قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/141323" target="_blank">📅 22:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141322">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=mwlr4WmSY9ojECvuUk5EfdPE-BstAYjRYTkp9rKzHiLnWjsI1OCFlmAYHQNaSHYsUqEk8wFi73eJV_KtmcLJLJtT3SXVFTww9QR26igtO7Wp6vUDoMBkQuycZOdu3WMZbtjgB-d5tQbxGLSTbHexSiEDFiVPH-HJjU09J56b6iMC2sWXYzfgc7E1tTnGrCaDcs3Czg-QiZhuo_X-Ko7X8f8aX2GF8UcSnS-AEW7sDMA18jzJtv5NG10K1EEsCvtLH0bmd2vjTVRyVW2rYaAwJyuKxMcLrDYKibtyBOxrV5otQydJ6w6h9cgIYYLGq8KXactHIbtadBvHk0cbO4SoTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=mwlr4WmSY9ojECvuUk5EfdPE-BstAYjRYTkp9rKzHiLnWjsI1OCFlmAYHQNaSHYsUqEk8wFi73eJV_KtmcLJLJtT3SXVFTww9QR26igtO7Wp6vUDoMBkQuycZOdu3WMZbtjgB-d5tQbxGLSTbHexSiEDFiVPH-HJjU09J56b6iMC2sWXYzfgc7E1tTnGrCaDcs3Czg-QiZhuo_X-Ko7X8f8aX2GF8UcSnS-AEW7sDMA18jzJtv5NG10K1EEsCvtLH0bmd2vjTVRyVW2rYaAwJyuKxMcLrDYKibtyBOxrV5otQydJ6w6h9cgIYYLGq8KXactHIbtadBvHk0cbO4SoTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🎙
پیمان حدادی: از اول فصل تیم گرفتیم هر یک از تیم‌های فوتبال پرسپولیس گل بزنه، یک زندانی آزاد کنیم و تا الان ۴۳ زندانی رو آزاد کردیم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141322" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141321">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc7J7c2dlrD1ke8IY86aeOL9Z9DRf2_Xa3yfukcNfuYMYd01kVRaSlAWY8xGyRjuDSqszrF9Ya2tmVeOvAiIxBvDCYCflQEnTTkmKDbz-5vNzdXhWCgyc-Jy0QqyR4mMYs1cUuA2e1gjIqaHi2Y9ZMUFmUlRYAsqLpNUIQaZDrNv5Gk4fGGsOne82QPaiHlTPgrxC-VsMgLYUrCsNJa9rNX5bCUr9kpnmuJqUWPpi6phMxwfZj2rmfnmnrj_6wl9497r_e8JprTXdl5ADCFZp4DW6B6nlPgDnWNQviZMVgqlRNSKkTSOasfeIhvTN20V-8WNQr3EQY0iZ2wew08Qig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دانیال ایری از بعد بازی با خیبر در دسترس کادرفنی پرسپولیس خواهد بود/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/141321" target="_blank">📅 22:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141320">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8GOtkuPPjnLYGDxS-D-eZFmHU3_AL95k2wCnnwqjLPOIPyk1TSZa0cOWSBnI9NR7t4zkdQ3rZ51cCsYhPukkWW2KHW9xlBnF8OXOeXX3rCbSytg_AJZVVXec0RnP-eo1ipEP2Cbexp46vGwY87gmN6qovV777ppSdoN3rKb_Rqdcfr2PsbFRMpA54bautXvVdBCFg8Cs437LA1uBwF1-I97EYsq3Lh3zGxU4W0CS7FSjawRct88mJFiOWPT-unvYaw4cJYW4w28PQxVUnJtdwPSx035SVtKQr3mvLz_60EPsNQcxmuUHdnDNQcAKn3PUeBibHNN0Dwqx7L8vG8-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141320" target="_blank">📅 22:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141319">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBAcZCX8lPP-WokjUD2xoFvzV6h1Xjae6oQH-Bz0Ue-UknnIHLB90m694OloT-DWxwYue_aLacsyYnEG9HGuInMykOEc06aUfTetr5mqrCSdzNb0kKotsjR9zm0VJPhXxaJcIrBL4Un275yx679rm2BSX9luROZ5pX4tngZG3nMU-0pmavWFSure1TnDvmjF0GkJlgaYAIrvfKbMI2a4RVFCMv6BoJW-5ZEHKJOBPMWEOzjIyQsAxf_50WoSkk8TO1Yjq2Sgw7lnMkYNQFvQMcOCFRtsQmTkYj2n4IzN7_emTr7bM4GAPen1Kyrp5YgFxdMtyHBcly4FTP1htULmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
فوتبالی: تارتار قصد دارد پست دنیل گرا را تغییر دهد و از او در پست هافبک تدافعی استفاده کند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141319" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141318">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی تعطیل شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141318" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoyEGO8yZU1-MgKImVYlCcrp8ROvSrc4tFIrlcklrYsdf-PwGDhzCK7bTvezUxnhazgbiRYtcRrTo0fApOA_dmOly_QJg166GPyEMfogKQdY7gneYx1HqrZpPfzKt7q91-AHKsiZk2H6tBNgUFrxbJCu3GoZVCHMMDb7iiHeo3sNAR1iQvk-1KBXBhngAWjgpL3q8ctoQ73y8HYdT6KfgjnN5Uqh4MTadM3MJ_PKz-ne5-l7QUyiyIR-NYtRTuuRdOqajPR0k9mXrjxPv-MCC-QYMqpxu5MiRIMeSppCQsUk2unmTGJh1p3Vta1hwJr4oV_JlPbC8rNprhqclE2Zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بیانکونری در کمین ۳ امتیاز؛ کالیاری سدِ راه بانوی پیر!
🔥
⚡️
[
کالیاری
🔴
🆚
⚫️
یوونتوس
]
⚽️
یوونتوس از نظر کیفیت فردی و تجربه، دست بالاتر را دارد؛ اما کالیاری در خانه می‌تواند با پرس و ضدحملات دردسرساز شود. کلید بازی برای یووه، شکستن دفاع فشرده حریف و استفاده از موقعیت‌های ابتدایی است؛ هرچه بازی طولانی‌تر بدون گل بماند، فشار بیشتر می‌شود.
سناریوی محتمل: برتری یوونتوس در مالکیت و موقعیت‌سازی، با احتمال بردی نزدیک و کم‌گل.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/141317" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووری
✨
میلاد محمدی در لیست مازاد تیم‌ بلاروسی قرار گرفته است و به زودی از این تیم جدا خواهد‌شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/141316" target="_blank">📅 19:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141315">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAmiVQeokO0gw7-9r3QOb63DfBSkk0B3wmHe-iC13_YAGcb4AKWzRJcEf4nWam40Nv4ffjWh7sLBY5Ie1tSgUz_LALe-6Axlraj9hWcDd2jQ_0lPo5SsPPAd_udbhdRnP36FJMLBAJVKki8Gsyh75rn6T77_XkiGw_rZ-u_8bNZCoqJWAHmm0VMZnqL_9AS42Cse6MTL13RHgPyfmdckHjv5ZPFI2yZevRBanjmbLcDaj-MrZnimoC7n2HMhbjsf_BmlbqmYyOFqvkBN5lGpGidzT2RC5_MFJdWQuv6tUxPglPgbijcCzp3t6Uggugg5ChW9uSy5Z9bzbEcehoZ-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر فاصله دارن.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/141315" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141314">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
پرسپولیس بزودی اقدامات نهایی خود را برای جذب عباس کهریزی انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/141314" target="_blank">📅 18:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141313">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC2BgycgisS3Y3jgF8SURK7_qMa3G2-ASXa8H1ngYHIt1tX69afozvg_EhKNCRb-B0R_4aKDEQZVVQXuwvD8sl8SD7Glbp5M2kLQK_vfo2x5OWH-bHn6dUxISvyYzhTpIC6vXD3_RdUrrGDPlXH8l7V3LgUC0BO3CT0jnVa7vigElPSr4gEyDL_Mv479cV1pHgAAC95bucYYaV0cLkNdPfK2I1DPG3qNxlmDJLjQJB8nmvIQ1mArSrKu6LTA_OZ55zK3NB3BwqSSZogmujMr7mdWSn2c2Ws6JOCAb2ofajPWxqhZkqiRJP9GGPeQUEqzUKheL0yYBvksx7wb92421g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
علیپور؛ کابوس همیشگی صنعت نفت
🔥
🔴
علی‌رغم بازگشت تازه از مصدومیت، علی علیپور در نیمه دوم وارد زمین شد و از روی نقطه پنالتی گلزنی کرد
🔴
او پیش از این دیدار ۶ بار دروازه صنعت نفت را باز کرده بود و با این گل، شمار گل‌هایش را به عدد ۷ رساند تا برترین گلزن تقابل‌های یک دهه اخیر پرسپولیس و صنعت نفت لقب بگیرد
👏
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/141313" target="_blank">📅 18:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
⚪️
⚽️
تاج: با یحیی گل‌محمدی برای هدایت تیم ملی امید به توافقاتی رسیده‌ایم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/141312" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/141311" target="_blank">📅 16:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
فوری ؛ خبرگزاری ایسنا :
🔴
🔴
🔴
فیفا در جواب استعلام باشگاه استقلال ، پاسخ داده که یاسر آسانی رسما فسخ کرده است و بازی کردنش غیرقانونی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/141310" target="_blank">📅 16:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141309">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
با تصمیم زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/141309" target="_blank">📅 14:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/141308" target="_blank">📅 13:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141307">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/141307" target="_blank">📅 13:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141306">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/141306" target="_blank">📅 13:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141305">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU5y_Wik_NcRidKi1S7ufzEYx49r7jqx39nbQQHb7Gvgtj2ovsEBTPRBDyJAzU949WDmcmbvcXEd9iXNK4Op4-Zq9WvAXYdSxS-1T1msfAWj16_ZO9BbzMh0342wR5maWxsv1Pt6lOiLyJzo2aJo0xXwRi8McXcr1nNMEhJspiYP1rfSzV3QJcBWfb8UQdc5ZfxhwSw1inZ7nGjoFlK-0eQSAfORTwe-CDGOhCask60hOgE7iNHHCYdItFBSukkQDRKdGCtB9DZViea_lb86VS6pZFYc0lTI3f38804HKQjClvc8sF5egq59UpISh64tC6uI5a9e2q0Ti3THTGKJ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیژن حیدری داور بازی‌ معوقه پرسپولیس - خیبر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
😀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/141305" target="_blank">📅 13:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141304">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH-BwDOOBsyqDXAtCYss_9DttNDpBype_FMAU1s0TtavOIyJeEXGkLxZjAjNWOUPV1pw2ZI0hVPScN2rFlG5b4UPlt1mjAh7096D3Z8ZxMLDIw4thM5nxZCvs2ZjRg6Se0t99KcVxMkuK2VrPl3SYf-NGZWcpcj6YOoFN73E1ao1M1HjsfWvQ6wIl791CUgjjpR-lImx5MHQw-CauyXhoNtYFd2m_5jJUuMme6uHxSFvb36nrIXt5xVMxvPWe6RG0lgzQlHdOpL-3tm48_mokcMQjZBeGbUSc9PGfpOY8uhyhxhsGwcM7uoEEcR1ju03eVqtWl86b_wmHftHs1onLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool
🆚
🔵
Man City
⏰
Tonight 19:00
🏟
Anfield
🟣
سیتی در ۵ بازی لیگ ۱۳ گل زده و با میانگین ۲.۶ گل، قدرت تمام‌کنندگی بالاتری نسبت به لیورپولِ ۷ گله داشته؛ در مقابل، قرمزها در آنفیلد از امتیاز میزبانی بهره می‌برند. غیبت الکساندر ایساک و کودی خاکپو می‌تونه قدرت هجومی لیورپول رو کاهش بده، درحالی‌که هالند با ۵ گل بهترین تهدید سیتی محسوب می‌شه.
از نظر مدل آماری Opta، شانس برد سیتی ۴۰.۷٪، لیورپول ۳۴.۶٪ و مساوی ۲۴.۷٪ برآورد شده؛ برتری آماری خفیف با سیتی است.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/141304" target="_blank">📅 13:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141303">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb0Q1J-Vn1zl9cxNZG6vSSnWie4Masd6c3EURNBb5TgMjOH3VRNTSGHe4qGzLunck1ktkLEaSp1QioMSnwAT3FOo-4TeLD_UAqV9RdVCd1ukovTz_BZtZWal7v6uIucMPFW2ZR72UrQuXANNm0dzGSx1LXIieaevvrYIP2kRLEJhauf002T_S7YeQ-U9w8OIvURepNUFOMjeMW86BT9NhgDbvdw-wHR16BLxm-xhDgwpz49jDJtZGRXS42uBZezvNBeYWNusxrrDn44dKDuxmgyB3A_f49_aOfGsjCOyz7Q1eEBHeigdZ-wIaYL4aNJwXw-STNeitsiFdoObYdw7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ابرقویی تارتار رو راضی نکرد؛ با بازگشت کنعانی و ایری، احتمالاً دوباره نیمکت‌نشین میشه.
🎙
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141303" target="_blank">📅 12:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141302">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇮🇷
👤
🎙
برانکو ایوانکوویچ: می‌توانم بگویم بهترین نتایج ایران در 40 سال اخیر را من به دست آوردم؛ قهرمان بازی‌های آسیایی شدیم و به جام جهانی 2006 صعود کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141302" target="_blank">📅 12:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141301">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
درخشش سرخ‌پوشان ازبکستانی پرسپولیس در رسانه‌های کشورشان!
🗣️
ایگور سرگیف با پاس گل در دقیقه ۵ و اوستون اورونوف با گلزنی در دقیقه ۸۴، نقش مهمی در پیروزی ۳-۱ پرسپولیس مقابل صنعت نفت داشتن.
🗣
درخشش این دو ملی‌پوش ازبکستانی مورد توجه رسانه‌های کشورشون قرار گرفته…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141301" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141300">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
⚽️
گل‌های پرسپولیس در بازی تدارکاتی دیروز مقابل فولاد هرمزگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141300" target="_blank">📅 12:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141299" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=jDb2xuQfzl5OznXcLQaHZJpFHhSvGscjlEKAWOpgFukPURp4HpoqPjpu_ajxOOlJOsA_pH51Ccw7AW6MLBq1xh95lKquKSYpMSxEFSMjZlg5WsT9q4SoizfzvDfjVXjEsIyPbkyNvt-I1qJe8h_ODAsYlcQbtXxquDqwGZEFQ-McvK5CAFeah9Uf-6srRpJNNWRP-5u3QU-ckAGleSCoUq-8kxGklzaXJGwrwp3_oKIfjXyjQb58Ola6lmhkMI31oOm6pyy0g6phr-qcqbDo8mL1HNgA58oSOp572Y9TNV3O_uoG9kAD2A87vLvpCdablOenMExx8KQ_dSyYikTsWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=jDb2xuQfzl5OznXcLQaHZJpFHhSvGscjlEKAWOpgFukPURp4HpoqPjpu_ajxOOlJOsA_pH51Ccw7AW6MLBq1xh95lKquKSYpMSxEFSMjZlg5WsT9q4SoizfzvDfjVXjEsIyPbkyNvt-I1qJe8h_ODAsYlcQbtXxquDqwGZEFQ-McvK5CAFeah9Uf-6srRpJNNWRP-5u3QU-ckAGleSCoUq-8kxGklzaXJGwrwp3_oKIfjXyjQb58Ola6lmhkMI31oOm6pyy0g6phr-qcqbDo8mL1HNgA58oSOp572Y9TNV3O_uoG9kAD2A87vLvpCdablOenMExx8KQ_dSyYikTsWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141298" target="_blank">📅 09:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqy7E0dB1HgH_kiU9T6PvmCuGApv0psDLjjXv8NGtWXZiDvW1LL9rYKso5tDs2ZYOt6yYOznApajLsmxCgRzfZSPDAjBiKOxR7jcbtjs4mKxX9ImzC_SbcuxQqhbEr3Mr13bNBrsxnyEvuWW00gRv1AjaTN69KUZAc_ksOixhqTuPiLsUwc5g6nrvirc5_n_z0QV3iQUQBn6TzdSy_uOBq8xrdvX0z7SoCRiQ1OTO1PcPF5ssIwSDN7IFJj-GdXf1ytQl-bjSOnrWmy4-TojpaTRo21aBOmckyzM2BLAkUMny7f7yhUcuMPafdBLWbBE6-0lB4fZV6sBW-l9xPYo6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهرآبادی از هفته‌ی بعدی فرصت بیشتری برای بازی کردن برای پرسپولیس دراختیار خواهد داشت.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141297" target="_blank">📅 09:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141296">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R12fohg2q0AtjEpZXx8Yz-LJ7aWMWAm7eZnV8T2n2vMsSgFRt-H9bHJJOv1kRcD6kB7KrXiAisgahz8bLdoAfIn2lw-_8hTm26i05hPKg_zgP5b4w-QeBRENfeEZUmb0BcBxFzLRiys-N4yE26GgLHdryZtxwkxtJwflxK6o8YYIKT5V1lfLtHIO2cG1_6YVur7EMPiShuw9nq3WvCyg5Dxwvl7SpM5_I6g5SkxzGF4-T0eJCx1edL3KA9sAMeLmZ5UXpW1QpyhMvto6nR8-mS-EaKCTWKWdM2fwEtwyxDVsVcPEeNjnP9AIsLOEjInN3Zb_M-4qQaXsZi-9LvJENw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141296" target="_blank">📅 08:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=JuGX-AiLDwuQdZcjN-iU1UpRwHZhHxCbLD-JCqM-it5GZCJiqnql3KwdCvzBdPRmovcudWR6eURHLO3JX1mXrECgm29QI0_bN--AFu6xxbBdz1z7rClHeZOw8-BYdKbAJdwUP4KrY-ehqDccbYluhqG1josDgJUdutPnXJ9tpkxEFoDaAvfGjzXlmbYsOv3ZmAhYRmtQZpPEviC72d33AX5bUaZn7Lvz931G2SJuMQP21AHhSIzD5dzjcCAEr7Vea1Fc3plYxbVNd6XXUEKEBoKkuVHkQ7QwCueM6TbDUBB0Mw0bcAeugzn8kZRoT5wuALlAs313-kn8gLR8yvm7gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=JuGX-AiLDwuQdZcjN-iU1UpRwHZhHxCbLD-JCqM-it5GZCJiqnql3KwdCvzBdPRmovcudWR6eURHLO3JX1mXrECgm29QI0_bN--AFu6xxbBdz1z7rClHeZOw8-BYdKbAJdwUP4KrY-ehqDccbYluhqG1josDgJUdutPnXJ9tpkxEFoDaAvfGjzXlmbYsOv3ZmAhYRmtQZpPEviC72d33AX5bUaZn7Lvz931G2SJuMQP21AHhSIzD5dzjcCAEr7Vea1Fc3plYxbVNd6XXUEKEBoKkuVHkQ7QwCueM6TbDUBB0Mw0bcAeugzn8kZRoT5wuALlAs313-kn8gLR8yvm7gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
آموزش ثبت‌نام و ورود به سایت وینکوبت از طریق ربات تلگرام
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/141295" target="_blank">📅 01:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhvNDMV7sOppBwKVvVgYxQR5etMns0vKfBBWxXl6jYkJ6Xx4kS6zgLbO6Hk1tCjqYmkajmEf3V2tRDmo5qkuzxBI_qY-YKVqKVT13OmotkXpdb3p7X7HrjjedG6q5tMKRNjT3bTSc6qWm-ZCtP5q0o99BQvtSy-zmWXarEK_RRzbCwlQRiOUzrUwByFywkts_kZjJEfv7AnFrbHixhXxbbQ5d9rP4ZQa5EKiprPWWUHHhuEHAJLm-geJcofV-PvOHehjpPR4JoyjdeiBD6riK4tkqQraJT_mOwpz3hSbq1J_uQ9O_9_pSH-rNo9QBCPzm84I5Rzox99R0biPKQEztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد خدابنده‌لو به اردوی بعدی تیم ملی دعوت خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/141294" target="_blank">📅 23:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=G-PDiRlGZHInxlK-S1hcs9SAwyH612MpyH1yHM_Z1aFLS3j9TVcMsmwPvg9OhRKaZNx6R_SCORW30I3ldE1t5wgmt3ZVZ0BSfSvPqiiMhm65-Cs4HkaWV3RTKr_DNc_oEaA2nyb8ypbwFu6CCvaDFvj9rnu2vVBt3jtlnTAjs08e38CMcmd4luBa85bOCs6_Mq_CdwIq1TFh4Q5xlrhJ5S9uVxRqUFtXhU8WzDn-JTEh-7Klr-HQjXKclJamURsSfWbQlpvs0i5vBbpCR_fkXR6AymIGB9y7c0K7sCvYfkywtEctSMmx1jdZ1J308fb4ZvAFVyW3kpNieI0CLMnajH96YDCZTmoFf5U4snUDrnvfoXkCZFrR3yHW027NDV31tlE6o_i0XhxoX4Mk0fpSaCoxffgdkjA23EP5Zla4ZOgHxrf9vlpUiY4QtNwTOMx7ruFDM5ARi02oD1tNw7n-owOmKpBO17pYl-gLS6DTBxTpexwwjuyb6KzhYWDyaikiVUix5zGGZ6vy7Xqkt_P5stKHB-UTkWh0dW7nncRuVaWY_wFMulwm6rY_ieFTrWbMZGLL35RoUVLVMxA8HDpBGI34mMWsENjz3BMdBY6OkPmAVT29yoEHc7LO6klRwZ5ywzUk9U8R8SPV4fnMb1m6cLzSQ1-S3CaIwpsSZIbjI5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=G-PDiRlGZHInxlK-S1hcs9SAwyH612MpyH1yHM_Z1aFLS3j9TVcMsmwPvg9OhRKaZNx6R_SCORW30I3ldE1t5wgmt3ZVZ0BSfSvPqiiMhm65-Cs4HkaWV3RTKr_DNc_oEaA2nyb8ypbwFu6CCvaDFvj9rnu2vVBt3jtlnTAjs08e38CMcmd4luBa85bOCs6_Mq_CdwIq1TFh4Q5xlrhJ5S9uVxRqUFtXhU8WzDn-JTEh-7Klr-HQjXKclJamURsSfWbQlpvs0i5vBbpCR_fkXR6AymIGB9y7c0K7sCvYfkywtEctSMmx1jdZ1J308fb4ZvAFVyW3kpNieI0CLMnajH96YDCZTmoFf5U4snUDrnvfoXkCZFrR3yHW027NDV31tlE6o_i0XhxoX4Mk0fpSaCoxffgdkjA23EP5Zla4ZOgHxrf9vlpUiY4QtNwTOMx7ruFDM5ARi02oD1tNw7n-owOmKpBO17pYl-gLS6DTBxTpexwwjuyb6KzhYWDyaikiVUix5zGGZ6vy7Xqkt_P5stKHB-UTkWh0dW7nncRuVaWY_wFMulwm6rY_ieFTrWbMZGLL35RoUVLVMxA8HDpBGI34mMWsENjz3BMdBY6OkPmAVT29yoEHc7LO6klRwZ5ywzUk9U8R8SPV4fnMb1m6cLzSQ1-S3CaIwpsSZIbjI5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی: تو فرودگاه بغداد ۲ تا سگ دنبال مهدی شیری و اعضای تیم افتاده بود!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/141293" target="_blank">📅 23:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141292">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDpQx6MqVUa27y1Gsec0r807vOtkSxbpFADE9e2NVtpZRFkd0aGM0A6gSXYjBENrx1HuVOjmNdjfpFFpLNeZsFbgsoJNu8fOa81HG26FQEMe0lI9-f0oQuiPm2tNrcS3zhxMTifL09yO83HVDiP9PhCbd8FlGoRMWLH1I4Ks4kUya5H2nbmRRJbT14uA6f33yKL-s22oEqhIH-q_fAc6R_I0cHBDx8wa7rpNvGMtx6aFSebk2o9wEUMNTH7Pe9fKShodFF3LTuwfqu7uCChQCbT7c0xeBtqgQQEYL83HmYT8myqsYLyP9ZmtTZb6sPWtyIZx18fle-ftzRJkG0Ju0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
❤️
⭕️
⭕️
علی علیپور و تیوی بیفوما با هم مجموعاً روی 73 درصد گلای این فصل پرسپولیس موثر بودن
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/141292" target="_blank">📅 23:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141291">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
⭕️
⭕️
#جنگ_کفتارها
🚨
محمدرضا زنوزی مالک تراکتور به تمامی ارکان باشگاه دستور داده  که هر کسی با بیرانوند در ارتباط هست فورا  قطع ارتباط کند!
🚨
به گزارش فارس امروز یکی از اقوام  بیرانوند که در مجموعه زنوزی مشغول کار بود به محل کارش راه ندادن!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/141291" target="_blank">📅 22:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141290">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
✅
تاجرنیا: بیرانوند دوست دارد حضور در استقلال را تجربه کند.
😀
به صورت جدی درباره بیرانوند صحبتی نداشتیم اما به ما هم پیامهایی رسیده است. اما الان فرعباسی و خلیفه را داریم بنابراین بحث بیرانوند یک مقدار این موضوع از ما دور است.‌ در هر صورت او هم شایسته است…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141290" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141289">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fcc915c7d.mp4?token=s0VnGtXSZ0qCPXWBYwqjs_10-C8-cV30IdeBIFA1qH8Xq0KDOtp6Fvze08D-FRFUJwBeibvu7U7MMpb-qY_ht8MHlu4EzUyD15FvdRWC_vWV-9Z_LhR-D8TMYxpjYjo_3LG71pDqE9xA5mEpZ16hpYrmmvYfmNnNUI1he1agSe_sgT7ABoR4vcJQrsXcO1nKtOnU8x_QDqOikFMP4fNqvWBfXSn_nb71yqoyoqkQrv8LR4IHA478IqCpB2-X8QHKTUBCfQ4uF1WMTKfBmcVIJtrbLyMMQLtcMo95tDYBc5k_FGAtLJVH0_2OI6F-LPZycAIfAG5q3cHXnll3tPQt0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fcc915c7d.mp4?token=s0VnGtXSZ0qCPXWBYwqjs_10-C8-cV30IdeBIFA1qH8Xq0KDOtp6Fvze08D-FRFUJwBeibvu7U7MMpb-qY_ht8MHlu4EzUyD15FvdRWC_vWV-9Z_LhR-D8TMYxpjYjo_3LG71pDqE9xA5mEpZ16hpYrmmvYfmNnNUI1he1agSe_sgT7ABoR4vcJQrsXcO1nKtOnU8x_QDqOikFMP4fNqvWBfXSn_nb71yqoyoqkQrv8LR4IHA478IqCpB2-X8QHKTUBCfQ4uF1WMTKfBmcVIJtrbLyMMQLtcMo95tDYBc5k_FGAtLJVH0_2OI6F-LPZycAIfAG5q3cHXnll3tPQt0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕
محبوبیت؛ فراتر از تصور
🥹
🔴
هواداری که با وجود سختی‌های جسمانی و مشکلات مالی، خودش را به ورزشگاه می‌رساند تا پرسپولیس محبوبش را ببیند و تشویق کند، به معنای واقعی عشق به پیراهن سرخ را نشان می‌دهد
🔥
🔴
آقای بازیکن! قدر چنین هوادارانی را بدانید؛ آن‌ها بزرگ‌ترین سرمایه پرسپولیس هستند
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141289" target="_blank">📅 22:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141288">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtIVgc-8N6AZngeBWiZfn84acwkhldfyWi8oTj428p7chaNGPKAbqx-BlQ97FKBIJRP0Zd3n3a9W0Wp3GV8zaUl07uvkDrUenJSBTgyiR9kbhC2hkqKScfqxJu3R1cPbRoEp_Lv9tsGcqrTHwXkfaCx3nqqrB8c9uuaElGPVz1GuziT547X8SYhad6sff4Y67i4fzRePtsdxjw-id2DK12lkHjAnIP-8y6SjYLyd-2cjrcOgGLhhcygA7Svx5fQqdSUyL022A9KRinstWBBxVDCm30yZGhcqsF3BGVyxN2gK35ysaAawG7q01apRPgtgF1m2-dpJdLranNHvE4vckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محبی؛ ترابیِ جدید برای اورونوف
⁉️
⭕
محمدمهدی محبی در ۷ بازی با ثبت ۲ گل و یک پاس گل، عملکرد قابل قبولی داشته است پاس گل اخیر او روی همکاری با اورونوف، نوید شکل‌گیری یک زوج جذاب را می‌دهد
🔴
محبی می‌تواند با تبدیل شدن به مکملی شبیه ترابی برای اورونوف، هم به پیشرفت خودش کمک کند و هم اورونوف را به اوج آمادگی برساند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/141288" target="_blank">📅 22:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141287">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
خطیبی از هدایت فجر سپاسی برکنار شد
❌
با اعلام باشگاه فجر سپاسی رسول خطیلی از هدایت این تیم کنار رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/141287" target="_blank">📅 22:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141286">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTIWrBPOAYDMJsoKtBqitSMZRnK9tZQr9kzWDohCabejdhquWgljCC5SyDhie4LUtYkjdlOmZouIJKCtrkv5p95nytIuLpumZfZ-uKsLing8Pl2JEX_AobZRZWwt0Ih1B1UIgvL5X9KhXqPH8jYLpPvWr7orz8kwhBShcnE4O1jgQgPRdBe6HoDW0sExCqllNRaF6chN-elFzCh4bALyf8G2o7p1sV5Qv5fLJmtGGEjjnG3mtkctCGQJBOnmLqOzHW9srGYweWG6PNFRIt3DSpyNNdWvR37KHT3hBl9u-TD2zuFbQxK7anc3KU3fgDSZ6oSiJCk8oZXN3x_OVCctUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141286" target="_blank">📅 22:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141285">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG2aZrLc2yd1ldIO2VwyWQzu1ZWz0bjlZ5ASC2ooYfQjgfdeU5s5sll8aV3QHZ382ZBPSlxAtf9_6NqtBwTgQ7pnqD269kbKJ1Kb7DDpsFk9gSr-K_6WMTaX1zNFqwwuFVGhlGALxgc39XuskAqOBtnwFUZQAHn1lr-Ok9KP0XpWyjbcaR3WJfwmHA5XXOtNrziQYXIiEb1WKc-GzGGXzemzVEqIjS07sSe6tx1l7jwJQIE6XZf4jiGqF6M86xbWf50Nqj4wVujeIyepaooiIYhxsJc-7wreGBcZweskgL_e_iJSbfns0D31EJpL4v0qUp5Xv572tzIepXaKF93Ulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جدول لیگ برتر در پایان هفته هشتم
✔️
پرسپولیس در دیدار معوقه هفته هفتم از ساعت ۱۷ روز چهارشنبه به مصاف خیبر خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141285" target="_blank">📅 21:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141284">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=PPD1e_gdQyAr5NKYAa0_oqn1TxJQCK2FD55dZc-qhEK343N8A5wJufkUOj5b_O_rfUfNNpmFMH-FoUqoh2XbtHeSUl82bZtAvzH8gM6Ep_ezqbPtEllSPifP0sM-kjJNgPpGpyahqatt04-JgqtUkwuVqahoQcD2sloh376SanCg7wCo-u6e0GOtTMgilr89QAnTYYMaXcpMuGVw1IJTy1Qd5ez-OEETNvWccynTa4iFTVtBT5lMk3R-z_WWiH1c7I20RxEMCIOQob0UDQvA0nns8-LDia28s4vIvvfj5d_ADCZ2zARd05pd5iSkXfz6MuGgPHS3zxMYjXwPxqbA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=PPD1e_gdQyAr5NKYAa0_oqn1TxJQCK2FD55dZc-qhEK343N8A5wJufkUOj5b_O_rfUfNNpmFMH-FoUqoh2XbtHeSUl82bZtAvzH8gM6Ep_ezqbPtEllSPifP0sM-kjJNgPpGpyahqatt04-JgqtUkwuVqahoQcD2sloh376SanCg7wCo-u6e0GOtTMgilr89QAnTYYMaXcpMuGVw1IJTy1Qd5ez-OEETNvWccynTa4iFTVtBT5lMk3R-z_WWiH1c7I20RxEMCIOQob0UDQvA0nns8-LDia28s4vIvvfj5d_ADCZ2zARd05pd5iSkXfz6MuGgPHS3zxMYjXwPxqbA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در پایان بازی پیکان و شمس آذر، رضا شکاری که پنالتی تیمش را خراب کرده بود، دل و دماغی برای خروج از زمین و رفتن به سمت رختکن نداشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141284" target="_blank">📅 20:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141283">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=dR7V8GGQ0pXrBHWT9-Z6xQsFvAB6Y75QA_bFCE6gZ6tzd8xdM1MFYCN_bDYEM7CY4qJ-wv6uXKh_InSOFjDGP-FG8tVfFmRn8uKpJ1BXhT8_1FFCbinznJXJeecP5o7hBUlfHsvaWWDGZzTFIO8iY5Be3fnBACzTW-IBXvaVcb-CpfWgwurwD1wJvjJFNr7vSl9cSvvFcsZHwg2u2qOnwNjFJTzypkeFKuWiObemWSBuY7L1hBvLr65OhdaZtk5xfU9OoQUPmL9ZbD4mZ7PQ0nCelR9IKgLXFXNYxN5m0P1BBiKpRba2V4G-DesPB7lkttgjk3fLHDVwbn53yZbsCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=dR7V8GGQ0pXrBHWT9-Z6xQsFvAB6Y75QA_bFCE6gZ6tzd8xdM1MFYCN_bDYEM7CY4qJ-wv6uXKh_InSOFjDGP-FG8tVfFmRn8uKpJ1BXhT8_1FFCbinznJXJeecP5o7hBUlfHsvaWWDGZzTFIO8iY5Be3fnBACzTW-IBXvaVcb-CpfWgwurwD1wJvjJFNr7vSl9cSvvFcsZHwg2u2qOnwNjFJTzypkeFKuWiObemWSBuY7L1hBvLr65OhdaZtk5xfU9OoQUPmL9ZbD4mZ7PQ0nCelR9IKgLXFXNYxN5m0P1BBiKpRba2V4G-DesPB7lkttgjk3fLHDVwbn53yZbsCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساکت الهامی به بازیکن تیمش اینطوری سیلی زد
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/141283" target="_blank">📅 20:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141282">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cett79_vAzeQdrsPSwh9e2arkO2EjMGitFedFDrgGF_ToYPWOc6PJJj47hWGU9rUgnY1inUeGj9JxtBORL7wxMW7BZunuC6_lqJK4g6sAfCjYxj2c3HOHWsKR2zK11DUgq8iXlRGBWP3WqiIB-oyGphnqSMVSz0YIj5EbVZCgNqYvICHa5tMIwcPeM5wRZlislYTAEmyr2RGEP_0loiluex7NZKIfPCBAVip2AYbz0zwpxlKYJqWGonPjtN4p-H0FcFC2igtTBzZtFxVh29u-_h7WZVxy6PqlgpEcl56ovyhonEmh1bhKGGLXgN43kZ35y1vw9kTHDAYZoXW1zIp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid
🆚
🟡
Villarreal
⏰
Tonight 22:30
🏟
Estadio Bernabéu
🟠
رئال مادرید در ۷ بازی ابتدایی لالیگا ۱۸ گل زده و فقط ۸ گل دریافت کرده؛ میانگین ۲.۵۷ گل زده در هر بازی نشان‌دهنده قدرت هجومی بالای این تیم است. ویارئال نیز با ۱۳ گل زده و ۱۲ گل خورده، توان هجومی خوبی دارد اما در خط دفاع آسیب‌پذیرتر است. باتوجه به میزبانی رئال در برنابئو و اختلاف کیفیت دفاعی دو تیم، برتری رئال و احتمال گل‌زنی هر دو تیم از سناریوهای قابل بررسی این مسابقه است؛ البته پرسینگ و مالکیت بالای ویارئال می‌تواند بازی را رقابتی کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141282" target="_blank">📅 20:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141281">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
تصاویری از آخرین تمرین پرسپولیس پیش از دیدار فردا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141281" target="_blank">📅 20:50 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
