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
<img src="https://cdn4.telesco.pe/file/Ml65uXVels5owHQl03LxrefYi-i9e6Ygi-gcHENWkmPUqU7ReoiOr77i6KBRAFeyUIW5Bql7GomY9qGBXaaSmUVku2sJRN85wwUKcVlNwqdS_JpJpx8lfP2_XU7T62g6HJQoy1li70qxyt9BlCOxH14fb5WDNqWgAFEGRI2Pp0i3r4B4cIiL2h1an8sy7FcWYH3CZ41PfwjPiipKAY6meZUz6ksr2jz4Xu_sIejR3Vz0t035ryPBIvR6X30KS4Q12QyLa7y68ZBP1ZOg_pFIDWGj_Fv4ROCf482Puq6C4CYnbIT70aG35lFz4ZfgigkV7BsjNzQrAtJZaAdL_1FtVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 11:20:30</div>
<hr>

<div class="tg-post" id="msg-21681">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حمله آمریکا به چند قایق در سیریک</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SBoxxx/21681" target="_blank">📅 10:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21680">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ادامه رزمایش های موشکی سپاه</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SBoxxx/21680" target="_blank">📅 10:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21679">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آمریکا دو پایگاه نظامی جدید در گرینلند تأسیس می‌کند  واشنگتن قصد دارد طبق توافقی با دانمارک و گرینلند، پایگاه‌های نظامی در نارسارسواک و مسترسویگ تأسیس کند و حضور آمریکا را فراتر از پایگاه فضایی پیتوفیک گسترش دهد.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/21679" target="_blank">📅 07:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21678">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ابوالفضل ظهره‌وند، نماینده مجلس:
پیش بینی میکنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود
نتانیاهو بدون جنگ باید به زندان برود، برای همین چه با ترامپ و چه بدون ترامپ، جنگ را شروع میکند!
برای زدن زیرساخت‌های ایران ۳ روز برنامه ریخته اند، با این‌کار نتانیاهو انتخابات را به تأخیر میندازد</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/21678" target="_blank">📅 07:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21677">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ:
ما به ایران درس سختی خواهیم داد. ما دیگر از رفتارهای آن‌ها خسته شده‌ایم صبر ما تمام شده است</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/21677" target="_blank">📅 06:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21676">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آمریکایی ها میگویند یک شرکت چینی به حوثی ها برای هدف قرار دادن کشتی های آمریکایی کمک می کند!</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/21676" target="_blank">📅 06:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21675">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استفاده از نام درست «کاسپین» بجای نام منحوس خزر برای دریای شمال ایران در سداوصیما</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/21675" target="_blank">📅 00:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21674">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2RAIt04wMIzFeY8451mHqUhGomYWYOiV8mqv8WEo8jnna-Klui3Yn-LAL8ayJNOO2FLJ5oGwaSsXssxq3mJLCpRUceYkrZ-74GRMwW6cge19E4oePe1t_HxsGsnHwV8DgaYHLVyiVc_iCLVf2pNryWBZe8Jw54DOyXAyDAQNqtNigEf3R3fM4o-Kr3ATdnvei6Enj-_uAjzNek1CYyLpTcixubiv-BV-WxfAErIpSdgvDdMxqhDR-6uzy0ubLl3aJzz_8Y-m9r7eET9rRu5aopdgHiFKqnsMFUU_lyN_dTOD8VN-D5uelWfGKRVjhvAVzOJT40VkbPUVn8XehBL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده از نام درست «کاسپین» بجای نام منحوس خزر برای دریای شمال ایران در سداوصیما</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/21674" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21673">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حمله حوثی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21673" target="_blank">📅 23:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21672">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گویا نتانیاهو در حال برنامه ریزی برای حمله به ایران حتی پیش از انتخابات اسراییل (۲۷ اکتبر) است</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21672" target="_blank">📅 22:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21671">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پوستر جدید سایت دفتر رهبری !  مشخصا بر جنگ ترکیبی (زمینی + موشکی/هوایی) اشاره دارد</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21671" target="_blank">📅 20:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21670">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21670" target="_blank">📅 20:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21669">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu1o2Ql5IaTwjW0X0cs_-J8VX4dqRHvAq0iZAXffHFugM29Ao4qhyVR08Kq0Al05Id1lfyDQYOaNc5pVGEmwXqg79XFVqC00yg8x4Sq0fL-wKLEZlvmKW5-L39OMslLJ4wE_CUVoK0-Ild9peSZUfBzG9IjwXYcksQMCBpCftA6Id7nArml1JOxBk6mo3y5iDzxdy7SntpI89cO0SrO_NDH6MjM1LtUIyDwIyZPiuLjyQm5yUuBIp7QMnBmVG5N53l4RYiQ-HMh0QwQm4AYo8uWoCeaByz3SczrPCPR4zMa5FaZuyVoJWNGY-8GlLp3a5S5Rl7TLbvzAsUxQvZ78uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی:    آمریکایی‌ها اگر تصمیم به حملۀ زمینی بگیرند آن‌قدر تلفات خواهند داد که خودشان تسلیم شوند.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21669" target="_blank">📅 20:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21668">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سردار نقدی:
آمریکایی‌ها اگر تصمیم به حملۀ زمینی بگیرند آن‌قدر تلفات خواهند داد که خودشان تسلیم شوند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21668" target="_blank">📅 20:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21667">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:
رفتار حوثی‌ها بسیار بد است. فکر می‌کردم آن‌ها یک سال پیش درسشان را گرفته‌اند؛ یعنی زمانی کما آن‌ها را زیر شدیدترین بمباران‌ها گرفتیم و به درخواست خودشان، عملیات را متوقف کردیم.
آن‌ها مدت‌ها ساکت بودند، اما
اکنون دوباره سر برآورده‌اند—احتمالاً به دستور ایران (کشوری رو به زوال که نه نیروی دریایی دارد، نه نیروی هوایی، و بدترین اقتصاد جهان و تورم ۳۰۱ درصدی را دارد)— و به شیوه‌ای بسیار زشت به عربستان سعودی حمله می‌کنند و عمداً سعی دارند قیمت نفت را بالا ببرند،
احتمالاً پیش از انتخابات آمریکا؛ که اصلاً کار پسندیده‌ای نیست.
کسی باید برایشان روشن کند که من قرار نیست در انتخابات نامزد شوم [چون] همین حالا پیروز شده‌ام، آن هم با یک پیروزی قاطع و عظیم؛ اما پس از انتخابات هم آنجا خواهم بود و هرگز فراموش نخواهم کرد!
رئیس‌جمهور
دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21667" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21666">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرنگار:
آیا از ترکیه می‌خواهید که در پاسخ به حملات حوثی های یمن شرکت کند؟
ترامپ:
شاید این کار را بکنم. رئیس‌جمهور اردوغان دوست بزرگی برای من است. من احترام زیادی برای رئیس‌جمهور ترکیه قائل هستم.
رئیس‌جمهور اردوغان، به نظر من، هرچه از او بخواهم انجام خواهد داد. من احترام زیادی برای او قائل هستم.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21666" target="_blank">📅 19:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21665">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5Np0MOe7U3WQFJZM_K1HNzmq49tWKxbKVk1CMkwoiOXSVMs4vp8HvlJZhvQQ68ngZ7zHNo0nk14_RAifBWN2Ee8_uZSzyvMtrypA2uipvyzzMbbgz3hCmKWPezIcJSe1B1kH2kmOCEbzGCfXo7gNTlOb9eJ0w1fYSctPHUjGN8XGUPoTa0Q6DH6g-VfqYJbT0GKQxF9jQnnjAZyaPJ88KWJqZOOL6dBGrQ9v9Sw7G1ppraY9zYZUP3oydfZjx0otMW2xyrtSp2X_haMB2xIC_biQkrkqKjootQDhbNNgZaOYdecKfpg9g4CzB45aLpIAeO00sTJefUDgsfp3bI1Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی قرار دارد و با توجه به رشد صبحگاهی طلا، فروش رو به بالا از 4190 توصیه می شود.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21665" target="_blank">📅 18:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21664">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
اختلال شدید در اینترنت کشور آذربایجان در پی وقوع اعتراضات سراسری علیه قانون ممنوعیت حجاب</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21664" target="_blank">📅 18:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21663">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">— حملات نیروی هوایی سلطنتی عربستان سعودی ترمینال نفتی بندر رأس عیسی در الحدیده، در مناطق تحت کنترل انصارالله در یمن را هدف قرار داد.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21663" target="_blank">📅 17:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21662">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">— حملات نیروی هوایی سلطنتی عربستان سعودی ترمینال نفتی بندر رأس عیسی در الحدیده، در مناطق تحت کنترل انصارالله در یمن را هدف قرار داد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21662" target="_blank">📅 17:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21661">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
آقامیری؛ دبیرشورای عالی فضای مجازی
:
مودم های استارلینک اگر برای اهداف مخرب استفاده شود ، هدف مشروع جنگی خواهند بود</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21661" target="_blank">📅 17:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21660">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر بهداشت:   در ایران سالانه حدود ۲۰ هزار جوان در جاده‌ها بر اثر تصادفات جان خود را از دست می‌دهند</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21660" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21659">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر بهداشت:
در ایران سالانه حدود ۲۰ هزار جوان در جاده‌ها بر اثر تصادفات جان خود را از دست می‌دهند</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21659" target="_blank">📅 15:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پایان درگیری مسلحانه در کورین زاهدان با کشته شدن ۵ تروریست
یک منبع آگاه گفت: «درگیری مسلحانه نیروهای انتظامی با عناصر گروهک‌های تروریستی که از صبح امروز در منطقۀ کورین زاهدان آغاز شده بود، با هلاکت ۵ نفر از تروریست‌ها پایان یافت.
در این درگیری، یکی از نیروهای حافظ امنیت نیز به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21658" target="_blank">📅 15:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21657">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔸
زارعی ؛ عضو کمیسیون امنیت مجلس
:
در اسرائیل گندم کاری خواهیم کرد</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21657" target="_blank">📅 14:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21656">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
عبدالملکی ؛ وزیرسابق کار :  اگر گرانی رفع شود ، قطعا مشکل اقتصادی دیگری نداریم</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21656" target="_blank">📅 12:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21655">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
عبدالملکی ؛ وزیرسابق کار
:
اگر گرانی رفع شود ، قطعا مشکل اقتصادی دیگری نداریم</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21655" target="_blank">📅 12:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21654">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⏺
دبیر شورای عالی فضای مجازی
:
اینترنت در سال گذشته فقط یک بار قطع شد
هیچکس دوست ندارد اینترنت قطع شود، همانطور که هیچکس ترجیح نمی‌دهد در دوره جنگ، پروازها بسته شود اما چاره‌ای نیست
﻿</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21654" target="_blank">📅 12:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21653">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">روزنامه وال‌استریت ژورنال گزارش داد که مقام‌های ارشد ایران هشدار داده‌اند در صورت حمله به ایران، تهران ممکن است دامنه درگیری‌ها را در سراسر منطقه گسترش دهد.
به نوشته این روزنامه، اظهارات مقام‌های ایرانی حاکی از آن است که سپاه پاسداران انقلاب اسلامی ممکن است حتی به عملیات زمینی و نفوذ به خاک کشورهای همسایه روی آورد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21653" target="_blank">📅 11:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21652">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzPbu6iaz7Qlr93FHagVbzSjcBZzrM9uNkChdLHDRfRvlQa3O2ANCcIt1xjWEdYDrqi7bNjZ4Bmrvkv8XWnOByC_mfKhJ5KfPNHo4CH6uyO01FZZiDUimwsoGGAa2rEm1ew-953qGc5lv8-n8LP4AYXiASXRH9Ws1HCrxNv_ye1Hdfb9btt2S3CqOCOYAA_rdkEyCsByw9TVzBkUqp5SWWdS8CL0P8qNEbRpTUfnZKwAhTDIZKKrDb9dHFY-ZJqoiMoUsbdbtr-XWOq0DIljccD81tMxSTVZ0lI0ruCRyF_fSL1gzZ5rMWLzc2RyrBk5Hbxnm4a8t2vNPYLlh8I1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نیز نزدیک به محدوده قیمت منصفانه است و توصیه به خرید قوی ندارد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21652" target="_blank">📅 11:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBwE46NHiO7kg05reDu4vn6gyB7Acu0tZUs_q2hk1Nf0hxFnDVBv3rXxtl8bowIaUUY64NtfWAS2y-zu0bTZZXgZ999vzoVbbo6FJLELSuDWz_oH-oN8mdKaMOUniErHT68C7Z2E233MWwtY2T4s-GmQufItXtHjvIruqaSVXfLoQJ884G7DLL_04PHqWpzM7Pc5lf_vHnVmMf_lnfGcl_lR4ws-XVfkFAmRuJNnDy1eJbvF7aJIK0NUOSO4SVOoxWQZTm0EVriypZGnNvfJNFx_1Ht51uPcE0fhNnEbxr0AHqR336JGaZ240hUN71COoLygw5nI9ImN3h3DtnLHlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی قرار دارد و با توجه به رشد صبحگاهی طلا، فروش رو به بالا از 4190 توصیه می شود.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21651" target="_blank">📅 11:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21650" target="_blank">📅 11:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU7ZWvtNHkyTRxHDgHyLV0Na7ivDCVULbC5uif2lxlQDOWvFTcF4IjhXp0qlsTasMjRMHHdSMJGd0PPpRFucRvYvNPmABR69_yJE6hMPERwA0uNH8y1kEsVhoLWjKQ0wU6ZECakXosHw4s_kgXqQZWlovTbVvcDYSoPEsXGb_K4mdJ7CTwryXDONShy8XKtOOx4mzzJMoQ7Bor7gYAivw03xYmu-Q8bpRRqF9c7DM9hBfb9gP2uuGYcdYedT1QqvVZzeTo6pt2gNwCdHELqIxwji6leZBf72XBmPl3urNFeQtBk4m42JLV664vDHnpr1P8a6x8DCg9fcJa72TBcIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD — M15</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21649" target="_blank">📅 11:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21648">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgKsbNZ4_aa5xdyW9D-2pET0k6EGjcC6dQ-PmGm6Z76DrhlHWpcyHQXBJ7V_ye1iWNJGdGMFSM_Oq10BsA3CeCDRuz1yUptmXpXRnha9s1onrQS3Z82AAcq4FBIjorW9hO0_hBs8yCOMlyLqGCkJn84GZSpXvEuh6aRENu7qzo8vk2XzUSB_GfK8gVECnoiT1OBS4qhF3MyAgnj3oSUxQjwz7Xwg6XnDdCcEm0XWem-9Ce_9d-sp-zzTuZivcJoD3ZQJzIkgZdCD49o1wLZ1eVOyDvykqiJSlSTxrWQur8n8faRvpddBw6OSvOofFXXcFsgrFapZGj85hLHA8jb5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD — M15</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21648" target="_blank">📅 11:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21647">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنظامی ترین(گذر زمان)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb4e26728.mp4?token=ZBeZBEKgakc6JCsuaR6JRKbBSmOtYaaay_oyn-iUEc3D9Yfk8pauQxYZvxAOrcLbICN3o4S60xzYdS6Z92NhRUhytq7qGKViqa1g4hhdtmeJVP5lla085Vjvp-1mQgslpsfq3d4I0H8AxfefUYXWNMUnYDfg2mUlpTUW6LEsMjKKb6xD5kGL8FBB9KwsHwVuy0RqwzTFfrZMKEgBfrNtc75-N15gLLGStD5WjEmtDVufVSkCH0mgBvj_kJatQltQz1LobFthHZS8OwzOJMfQH3lpdO5uSj5GajbDRrLvTU4GpRGiqql5d_rIkih6nvhRO2J93P6aGUrF8UYUrvBhyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb4e26728.mp4?token=ZBeZBEKgakc6JCsuaR6JRKbBSmOtYaaay_oyn-iUEc3D9Yfk8pauQxYZvxAOrcLbICN3o4S60xzYdS6Z92NhRUhytq7qGKViqa1g4hhdtmeJVP5lla085Vjvp-1mQgslpsfq3d4I0H8AxfefUYXWNMUnYDfg2mUlpTUW6LEsMjKKb6xD5kGL8FBB9KwsHwVuy0RqwzTFfrZMKEgBfrNtc75-N15gLLGStD5WjEmtDVufVSkCH0mgBvj_kJatQltQz1LobFthHZS8OwzOJMfQH3lpdO5uSj5GajbDRrLvTU4GpRGiqql5d_rIkih6nvhRO2J93P6aGUrF8UYUrvBhyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افشاگری‌های احسان موحدیان، تحلیلگر مسائل بین‌المللی
یک لابی قوی پشت دیدارهای پزشکیان با الهام علی‌اف است
بیشترین خصومت را با ما آذربایجان داشته است ولی پزشکیان زنگ می‌زند تولدش را تبریک می‌گوید</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21647" target="_blank">📅 11:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ:
شاید در هدف قرار دادن رهبران ایران زیاده‌روی کردیم و باید در سطح اول یا دوم تنش‌آفرینی متوقف می‌شدیم</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21646" target="_blank">📅 10:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بزرگ‌ترین صادرکنندگان و واردکنندگان سلاح در جهان</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21645" target="_blank">📅 02:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obiUkXqitn16gLk6wEXFS_dC-ERDAGbI2bs8AyGcz-oy3Mdl3Mdy5_JTXfz7vZUdV2rfV4rfp1M1vegt3K2WMuvgFCJsj_PbXZc3v9GrIiYjvmwtga7I-GfhUFm26F0Pgw4auMq27oGKBqcX_xWH7oeFMFbLWPPDJWZKHseeo4GJqF3jVhGQ32CNjJ57mBEUC2BrUeb4avZLB3XUa612FuwMwys6ayzfqoXIAjGAoKDkyMUh0IcQ7ftRI8hssN0-Xq5DsN-9m88gcsdzVNDne_r0FW2dVebvSEL5rSM4RtoXAKM5Jt9FwnkTkMboPUsTvHeCdi3hnLKA_b-ke2sD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین صادرکنندگان و واردکنندگان سلاح در جهان</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21644" target="_blank">📅 00:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6CImhUxry3A25JbYC0n1VoLJOfJ2oPdyhI92IoY1kayOp5_ZkgxsXtVUeaqxTn3LjjDAqi68rali7twrNJqTC3qYNpBCir-8Z9AbCNXmNfAFSYy4MPnCL_NTZjj5uumgfDLXIPJZzIhCrjz8f7H_d61tQXXzkH0qH4BbCZL5QdZftmVrRlTMWoC4qfPUdzbnO3FFOQkHcfjRq4IL6f1_hlyHxap_uZPie_jV1kLpp03gwkSM_YBf1og61u7ymiqFzxQ4OlCnhItlKiT8eZwKMUsWIwt4_PsGOKNMOooaubpB-gzbijAxGmP1E09llzRULTvynnbpznr-rxYM7eRIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ ایران هنوز تمام هزینه اقتصادی خود را به جهان تحمیل نکرده است
جنگ ایران و اختلال در عرضه انرژی می‌تواند با تأخیر، هزینه تولید، حمل‌ونقل و قیمت کالاها و خدمات را افزایش دهد؛ بنابراین، آثار تورمی جنگ ممکن است هنوز به‌طور کامل در داده‌های اقتصادی نمایان نشده باشد.
تداوم این فشارها می‌تواند بانک‌های مرکزی را به حفظ نرخ بهره بالا وادار کند و با کاهش مصرف و سرمایه‌گذاری، خطر رکود جهانی را افزایش دهد؛ تورم غیرانرژی، انتظارات تورمی و بازده اوراق دولتی از مهم‌ترین شاخص‌های قابل‌پیگیری هستند.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21643" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ در حالی که به توافق تأمین سوخت دیزل با مسکو اشاره می‌کرد، گفت که اتحادیه اروپا ۲۵۰ میلیارد دلار به روسیه برای نفت پرداخت کرده است، اما رسانه‌های آمریکایی ترجیح می‌دهند در این باره سکوت کنند،
او همچنین تأکید کرد که تنها در منافع ایالات متحده عمل می‌کند و به اصل «آمریکا اول» پایبند است.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21642" target="_blank">📅 17:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21641">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔹
شریعتمداری
:
درصورت جنگ مجدد کابل های اینترنت و فیبرنوری تو خلیج فارس را قطع میکنیم تا علاوه بر اینترنت ایران، اینترنت کل منطقه و جهان قطع بشود
﻿</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21641" target="_blank">📅 16:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سومین تانکر در تنگه هرمز به دلیل عبور از مسیری غیرمجاز از سوی ایران، به یک مین دریایی برخورد کرد</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21640" target="_blank">📅 12:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21639">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♨️
سامانه دولت من در پی درخواست افزایش ۵۰۰ هزار تومانی کالابرگ مختل شد</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21639" target="_blank">📅 12:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21638">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
حملات پهپادی اوکراین به دیتاسنتر روسیه ترافیک بات‌های یاندکس را تقریباً به صفر رساند
▪️
در پی این حملات، حداقل ۸۴ سرویس ابری یاندکس از کار افتاده‌اند و ترافیک کلی شبکه به شکل چشمگیری سقوط کرده است. این عملیات در پاسخ به حملات موشکی مسکو علیه زیرساخت‌های فناوری اوکراین انجام شده و کاربران روسی را با افت شدید سرعت اینترنت روبه‌رو کرده است.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21638" target="_blank">📅 12:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21637">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♨️
سامانه دولت من در پی درخواست افزایش ۵۰۰ هزار تومانی کالابرگ مختل شد</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21637" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21636">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRGRtnt8lXjyG_AZNMbOeEUYjITGTVmvTkXBegsg9KtZ7B8BJYO8h3W22AT4DL5EmyHrRoNqnPctCuhVtByZbzRIJLDGd3TdQFt34Pu_LYDmD_1YhQhQQwHhgPJOKOf0JYkb3_xh6MkrOA6oS-bX5S814EWSqCEryUGbxJoxbmPhBff3Aqh665RKqgBsc2kBFqBAsaq_S3o49_sROM3o9M5MUQ7aLLlh79rXfn4NkJuk8mX9y-Huk4URlfZoB2uhgBLm4IlHPtQbg8rnhBF-IM5qVWodzHTBFSAgftZUnMPNVyR5w676tqyDwHoFanM2RqhhqhcHXht3QRLf3X59gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
— M15</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21636" target="_blank">📅 11:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21635">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcBxvLI2IgLW42h32i9aKI8l4AjDbOW536ZNZruS9Jul0nXuQGk0PMA_jv1d2YFWz5Ao9chGQfOj2-Y4F9EycpTm6b4dhuMKQTvU-tThvQJZG1jKZMx1eUANqtGlHCvuDCW1UssEgEge95AlOfQrGb4ReRC6YXEf-6OlR7BPGEl2qDDH8kabRCtsMMjcv_TpcGpZDzX-umfn62qyNNgyXT36k8Zuhay0e4j30NoTAWoXPTIdrPHpVv4Hb9yc4XTWWgUQBPoiW_DhF-WX3eU2l8sC80NOG8TEIUpgv_ktu8_U8W0ye0EzPdHQZWh6G55vJDfxwhZpodTRVPjt8_HM8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD
— M15</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21635" target="_blank">📅 11:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_AddrLB9yCowddCx5j23tGu3bgcanOwCl-8IhjFEO5ptKcRiCyk15PXbaO7TbyyEDcS_UuW2hma6pzsMufzLuy23G1jXLowqlvkb_HaR8v6hdzOpIEujt1-PZUxf06BpIVWQUxp05hgo8U8QBxGCdZ2qsSycHuA0rT1fIUDD0qCaAXfKV9mJ8Ecq-LEniM796HTazGSuUH5n4ylqPFdcl8g-_1u9w1eWsqVLkbtljksWkeY4FokrR0fh6Mvjkekqdj9k1u7EV6n7L3PK0M18QJyvRzADErJ_tX8_KRmU6Mw8DqQSPTuT4WAUfEdBYDRprxRQsAHhJV3M8BEwTJtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC برای امروز نزدیک به سطح قیمت منصفانه قرار دارد و سیگنال خاصی صادر نمی شود.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21634" target="_blank">📅 11:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5BeDcxbH2LWYWjZ1iNZ3JC_RFkWhRpgsp8QthJWuPSaovSJIOBaguLC7vxSNaqA25ZwHD7wywqkxGJo2IEKa8oZ2aMbr0uU5nQNJ8X-_b17Ne5q85gFbvP1by3BW16eALB-HjbgFK00aj9vSS5z7004fN_3O4R7JkLGvHlza910p7UMaf4PuzdUsfFTZ4S1cBIAGOvrqUuaFToTEJjhEi4d6yrU88XCg-py4Dipp6gtvdDcdY774h9rEq1_FU86D_942fQtztoBO9WiInsFPMc4bPWP1rpFNiq28Zhd8os-AnOilSIzEHy6jk4-Od05qCW8B63Qk55pVab042f27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21633" target="_blank">📅 11:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اخبار فوری: چین اعلام کرد که حملات حوثی‌ها به عربستان سعودی را «محکوم» می‌کند.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21632" target="_blank">📅 11:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">توطئه در کار است؛
توطئه بزرگ در کار‌ است؛
توطئه ها در کار است!</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/21631" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اوضاع یک جوری است!
زینب ابوطالبی می‌رود اما بیژن مرتضوی برمیگردد!</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SBoxxx/21630" target="_blank">📅 01:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbQALjzsMp9zj2iQDyN-AYUh59rUS0DD0yAAnSVXftjh0oMBDWnsNJPHjhUMYiaQ9wdyZ0hfiy1y8lCHkPy0913zY1XV5_LLj_2CWAbJN6Yku81voIgTRdi-PsJ3Zzo0WypkY3BTcITW_FK02YFYMJpZHYbc5VFy620HE7qQBrE6vCeshGWtH4wdyMfp1jM5u5AxuMFKAXZq7beJjGrW4b-dBZSBl5EY7dPyBYceg5_0cYkO5oOaUjDs8csfamn028x7pSXO-rb5gIP-7vv4HvOldbiO7K1zLawLew_E0J5xAuutzbBrJlWJo4TYZnHvRXXy1Ae3WOqDjxHe9LS5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SBoxxx/21629" target="_blank">📅 23:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZzMLHA2ADjLSCStMOphlnPja9eXGkNCFcTl9CfiSCDBiAHBqB9iBhgSR3ApKH14l8D8EFyY1LnVUMLJHDpgjCPYDw8rpdCJof5lJr3SvLrpNaJHNRpCzufk-S2Z8BKyuGwpZR-C2HQ8PqdWM0oaEfUutMQ_1Cwlc3GAyiwJdgGYQyTqcm_e8IbbBdNKZU8C649jeMJSKAFOGcNAzytlmDIiw-KQiFTtX7eLr0nG9_dpo9fQeG-r0BhvMvwjwIL0RQ17X0mfn1OeG8W4-aTcPCu1mRmXUfRZ5xf7u_dN9Gp0G9TEj-d06hSQOMIoQZdx7arsRvlCiYKrEJQUTkJptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کری خوانی سخنگوی سپاه با استناد به «سلحشوران» اشکانی و ساسانی !</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21628" target="_blank">📅 22:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیروی دریایی سپاه:
دومین سوپر نفتکش با مین دریایی در تنگۀ هرمز برخورد کرد</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/21627" target="_blank">📅 21:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21626">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">محسن رضایی  رئیس‌جمهور آمریکا، ترامپ، و فرماندهی مرکزی ایالات متحده (سنتکام) متهم کرد که بر یک عملیات قاچاق نفت در سواحل عمان، با کمک نیروهای نظامی امارات، نظارت دارند.  رضایی ادعا کرد که قایق‌های کوچک نفت را به تانکر‌های بزرگتر منتقل می‌کنند و نیروهای ایرانی…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/21626" target="_blank">📅 19:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21625">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">محسن رضایی  رئیس‌جمهور آمریکا، ترامپ، و فرماندهی مرکزی ایالات متحده (سنتکام) متهم کرد که بر یک عملیات قاچاق نفت در سواحل عمان، با کمک نیروهای نظامی امارات، نظارت دارند.
رضایی ادعا کرد که قایق‌های کوچک نفت را به تانکر‌های بزرگتر منتقل می‌کنند و نیروهای ایرانی از چند ماه قبل، هر شب، به پنج یا شش فروند از این کشتی‌ها حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SBoxxx/21625" target="_blank">📅 19:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21624">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUBj9Iq8PpyztjDWlh3G28woVI2W-lwbRrlKtwvaxK6hdScl9PpmdCngasRAlnaFaCzRTUp1atNetvTR7fHAFKjLV7uqrnCy9jak5hVbkodiYrKx8-Fgkkd2akgqP5_JWG0onVUQLjm0XaZqBE2kyVYuBAwHDZ14uN3x-8X_1rjIlYYQROlNXsGIMscW1bosxJYgzNtGDbguKG1lN-XC-_15GyS21CZ0cgR1SHQanF_JW5cjjWPek0lsaBHOVSjoj3zjc1j01ZLJxXWsvrMzKy3-gbiLKKGYLHTKhiTjBISKYLyViP_ngNc8F40DhKk93llg7OfW-Fd0Cz0R1WARaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ دال بر آغاز «آتش بس انرژی» میان روسیه و اوکراین</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21624" target="_blank">📅 18:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21623">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حمله دوباره حوثی ها به فرودگاه ریاض!</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SBoxxx/21623" target="_blank">📅 18:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21622">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔹
سرلشکر محسن رضایی ؛ دبیر شعام
:
تحریف کنندگان تاریخ برای تکرار شکست های باستانی از ایران آماده باشند</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SBoxxx/21622" target="_blank">📅 18:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21621">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
عزیزی ؛ رئیس کمیسیون امنیت مجلس
:
کشوری که ذاتش با استعمار و خون ریزی است ، هخامنشیان را که خالق بیانیه حقوق بشر است متهم به جنایت میکند</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SBoxxx/21621" target="_blank">📅 18:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21620">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هدف قرار گرفتن یک نفت کش دیگر توسط سپاه</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SBoxxx/21620" target="_blank">📅 17:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21619">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شلیک موشک از تهران</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SBoxxx/21619" target="_blank">📅 12:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21618">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبرگزاری یمنی YNP به نقل از منابع آگاه:   عربستان از چین خواسته رسماً میانجی‌گری با یمن را برای اعلام آتش‌بس، بر عهده بگیرد</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SBoxxx/21618" target="_blank">📅 12:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21617">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرگزاری یمنی YNP به نقل از منابع آگاه:
عربستان از چین خواسته رسماً میانجی‌گری با یمن را برای اعلام آتش‌بس، بر عهده بگیرد</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SBoxxx/21617" target="_blank">📅 12:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21616">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
ایلان ماسک رسما به اپراتورهای موبایل اعلان جنگ کرده است
♦️
شرکت SpaceX با یک قرارداد ۸ میلیارد دلاری، فرکانس‌های رادیویی با باند پایین ۸۰۰ مگاهرتز رو خرید
♦️
ویژگی این موج‌ها این هست که به راحتی از دیوارها، ساختمون‌ها و درخت‌ها رد می‌شوند و گوشی‌های معمولی هم از آن پشتیبانی می‌کنند
♦️
علاوه بر این، مجوز ارسال ۱۵ هزار تا ماهواره نسل جدید را هم گرفته تا اینترنت ماهواره‌ای پرسرعت را مستقیم روی گوشی‌های هوشمند معمولی بیاورد، بدون اینکه نیاز به خرید گوشی خاصی باشد
♦️
ماسک دارد کاری می‌ کند که به‌ زودی کل شبکه موبایل از روی زمین به فضا منتقل شود</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SBoxxx/21616" target="_blank">📅 11:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21615">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سنتکام از هدف قرار دادن یک کشتی در حال حرکت به سمت بنادر ایران خبر داد.</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SBoxxx/21615" target="_blank">📅 10:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21614">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عربستان از ۱۲ کشته و ۳۰۹ زخمی در پی اصابت موشک به فرودگاه ریاض خبر داد  سازمان هواپیمایی عربستان سعودی مدعی شد که در حمله موشکی یمن به فرودگاه ملک خالد، ۱۲ نفر کشته و ۳۰۹ تن دیگر زخمی شده‌اند.  ۴ نفر از گشته شدگان عربستانی، ۲ نفر از بنگلادش، ۱ نفر آمریکایی،…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SBoxxx/21614" target="_blank">📅 08:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21613">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21613" target="_blank">📅 08:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عربستان از ۱۲ کشته و ۳۰۹ زخمی در پی اصابت موشک به فرودگاه ریاض خبر داد  سازمان هواپیمایی عربستان سعودی مدعی شد که در حمله موشکی یمن به فرودگاه ملک خالد، ۱۲ نفر کشته و ۳۰۹ تن دیگر زخمی شده‌اند.  ۴ نفر از گشته شدگان عربستانی، ۲ نفر از بنگلادش، ۱ نفر آمریکایی،…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SBoxxx/21612" target="_blank">📅 08:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21611">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">۶ کشته و بیش از ۱۰۰ زخمی</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SBoxxx/21611" target="_blank">📅 08:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سخنان عبدالله النفیسی از کویت و وعده اش برای حمله به «صنعا» و پاکسازی آن از ایرانیان و مجوس‌ها!</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/21610" target="_blank">📅 00:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21609">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">video.mp4</div>
  <div class="tg-doc-extra">1.6 MB</div>
</div>
<a href="https://t.me/SBoxxx/21609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/21609" target="_blank">📅 00:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21608">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گویا تلفات غیرنظامی بسیار بالایی گزارش شده.</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21608" target="_blank">📅 23:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21607">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">روابط عمومی نیروی دریایی سپاه پاسداران انقلاب اسلامی:
یک فروند سوپرنفتکش متخلف حامل نفت خام، که قصد خروج از مسیر غیر مجاز تنگه هرمز را داشت، به دلیل برخورد با مین دریایی از مسیر پر خطر اعلام شده، دچار انفجار پر شدت گردید.
این سوپر نفتکش که سامانه های ناوبری و موقعیت یاب خود را خاموش کرده بود، بعد از برخورد با مین دریایی در یک آتش عظیم در حال سوختن است؛ به گونه ای که برای مردم ساحل نشین نیز آتش آن به وضوح قابل مشاهده است.
نیروی دریایی سپاه اعلام می کند: آتش سوزی مهیب عاقبت هر نفتکش متخلفی است که بخواهد امنیت و قوانین تنگه هرمز را نادیده بگیرد.</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SBoxxx/21607" target="_blank">📅 21:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21606">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آیا موج آبی دموکرات‌ها در انتخابات میان‌دوره‌ای آمریکا واقعی است یا خطای نظرسنجی‌ها؟!
با نزدیک شدن به انتخابات میان‌دوره‌ای آمریکا، نظرسنجی‌ها از تضعیف موقعیت جمهوری‌خواهان و افزایش احتمال بازگشت دموکرات‌ها به قدرت در کنگره حکایت دارند. با این حال، یک پرسش اساسی همچنان مطرح است: آیا واقعاً شاهد شکل‌گیری موجی از حمایت انتخاباتی به سود دموکرات‌ها هستیم یا بخشی از این تصویر نتیجه خطاهای ساختاری در نظرسنجی‌هاست؟
بر اساس میانگین نظرسنجی های  RealClearPolling، دموکرات‌ها در رقابت سراسری برای مجلس نمایندگان با اختلاف قابل‌توجهی از جمهوری‌خواهان پیش هستند؛ به‌طوری‌که سهم آن‌ها از رأی عمومی کنگره ۴۹.۸ درصد، در برابر ۴۱.۹ درصد برای جمهوری‌خواهان برآورد شده است. مؤسسه Cook Political Report نیز پیش‌بینی می‌کند دموکرات‌ها بتوانند بین ۹ تا ۱۹ کرسی به دست آورند؛ نتیجه‌ای که احتمال بازپس‌گیری اکثریت مجلس نمایندگان را تقویت می‌کند.
در سنا نیز شرایط برای جمهوری‌خواهان چندان مطلوب نیست. برآوردهای کوک از احتمال کسب خالص 2 تا 6 کرسی توسط دموکرات‌ها حکایت دارد. دموکرات‌ها برای کنترل سنا به 4 کرسی بیشتر نیاز دارند و رقابت در برخی ایالت‌ها، از جمله کانزاس، اکنون بسیار نزدیک ارزیابی می‌شود. هم‌زمان، محبوبیت دونالد ترامپ نیز تحت فشار قرار دارد. بر اساس شاخص نظرسنجی‌های کوک، میزان تأیید عملکرد رئیس‌جمهور حدود ۳۷.۶ درصد است. در نظرسنجی اخیر اکونومیست و YouGov نیز تنها ۳۵ درصد از پاسخ‌دهندگان عملکرد او را تأیید کرده‌اند، در حالی که ۶۰ درصد نظر مخالف داشته‌اند.
با وجود این داده‌ها، نمی‌توان نتیجه انتخابات را از هم‌اکنون قطعی دانست. سابقه نظرسنجی‌ها نشان می‌دهد که برآورد حمایت از ترامپ در انتخابات ریاست‌جمهوری سال‌های ۲۰۱۶، ۲۰۲۰ و ۲۰۲۴ با خطا همراه بوده و میزان آرای او کمتر از واقعیت تخمین زده شده است. هرچند نظرسنجی‌های انتخابات میان‌دوره‌ای معمولاً عملکرد دقیق‌تری داشته‌اند، در انتخابات ۲۰۲۲ نیز برخی مؤسسات حمایت جمهوری‌خواهان را کمتر از میزان واقعی برآورد کردند.
یکی از مهم‌ترین مشکلات فعلی، کاهش نرخ مشارکت در نظرسنجی‌هاست. شواهد پژوهشی نشان می‌دهد جمهوری‌خواهان تا حدودی کمتر از دموکرات‌ها در نظرسنجی‌های تلفنی شرکت می‌کنند. بنابراین، نمونه‌های آماری ممکن است بیش از اندازه تحت تأثیر دیدگاه‌های رأی‌دهندگان دموکرات قرار بگیرند.
نظرسنجی‌گران برای حل این مشکل، از روش‌هایی مانند افزایش وزن آماری پاسخ‌های جمهوری‌خواهان و تنظیم نمونه‌ها بر اساس ویژگی‌های جمعیتی رأی‌دهندگان استفاده می‌کنند. با این حال، این روش‌ها نیز بدون ریسک نیستند؛ زیرا فرض می‌کنند افرادی که به نظرسنجی پاسخ می‌دهند، از نظر رفتار انتخاباتی نماینده مناسبی برای کسانی هستند که پاسخ نمی‌دهند.
بنابراین چنین می توان گفت که در شرایط فعلی، احتمال از دست رفتن اکثریت مجلس نمایندگان برای جمهوری‌خواهان جدی است و وضعیت سنا نیز می‌تواند به سود دموکرات‌ها تغییر کند. با این حال، سابقه خطاهای نظرسنجی و دشواری نمونه‌گیری از رأی‌دهندگان ترامپ، عدم قطعیت قابل‌توجهی ایجاد می‌کند. برای بازارهای مالی، نتیجه این انتخابات می‌تواند بر مسیر سیاست‌گذاری اقتصادی، مالیات، بودجه، تجارت و روابط خارجی آمریکا اثر بگذارد؛ اما تا زمانی که داده‌های معتبرتر و نتایج انتخاباتی در دسترس قرار نگیرند، نباید سناریوی پیروزی دموکرات‌ها را قطعی تلقی کرد.</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SBoxxx/21606" target="_blank">📅 21:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21605">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در ابرقدرت چهارم جهان؛  — برق به دلیل ناترازی در گرمای تابستان قطع می شود  — گاز به دلیل ناترازی در سرمای زمستان قطع می شود  — اینترنت هم هر بار یک شلوغی یا جنگی بشود توسط خود سران ابرقدرت قطع می شود!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21605" target="_blank">📅 21:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21604">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزیر ارتباطات:  در صورت وقوع دوباره جنگ به دلایل حساس و حفظ امنیت کشور مجبور به قطع اینترنت هستیم اینکه در چه سطح و چه مدت اینترنت قطع شود مشخص نیست اما به احتمال 90 درصد اینترنت سراسری قطع خواهد شد</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21604" target="_blank">📅 21:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21603">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزیر ارتباطات:
در صورت وقوع دوباره جنگ به دلایل حساس و حفظ امنیت کشور مجبور به قطع اینترنت هستیم اینکه در چه سطح و چه مدت اینترنت قطع شود مشخص نیست اما به احتمال
90
درصد اینترنت سراسری قطع خواهد شد</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SBoxxx/21603" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چه بازی شد….   طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21602" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسرائیل هایوم:
اطلاعاتی که سازمان‌های اطلاعاتی آمریکا در اختیار دارند، نشان می‌دهد که ایران با وجود ماه‌ها بمباران توسط آمریکا و اسرائیل، موفق شده است بیشتر تأسیسات تولید موشک و پهپاد خود را حفظ کند.
به گفته یک مقام ارشد نظامی آمریکایی که با جزئیات این موضوع آشنا است، ایران همچنان به خوبی مجهز به موشک‌های بالستیک، پهپادها و سلاح‌های ضدکشتی است و می‌تواند به سرعت ذخایر خود را دوباره پر کند.</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21601" target="_blank">📅 19:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21600">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انصارالله با موشک فرودگاه بین المللی ریاض را هدف قرار داد    گزارشهای غیر رسمی از تلفات خبر میدهند</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21600" target="_blank">📅 17:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انصارالله با موشک فرودگاه بین المللی ریاض را هدف قرار داد    گزارشهای غیر رسمی از تلفات خبر میدهند</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21599" target="_blank">📅 17:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21598">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انصارالله با موشک فرودگاه بین المللی ریاض را هدف قرار داد
گزارشهای غیر رسمی از تلفات خبر میدهند</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SBoxxx/21598" target="_blank">📅 17:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21597">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چه کسانی از خرابکاری در اهداف انرژی سوریه سود می‌برند؟
همان‌طور که سوریه خود را به عنوان یک مسیر بالقوه برای جریان نفت عراقی و گاز منطقه‌ای به سمت مدیترانه معرفی می‌کند، یک زنجیره از حملات مرموز زیرساخت‌های انرژی آن را هدف قرار داده است.
در ۱۸ اوت، یک انفجار پمپاژ گاز را از کارخانه ای در حسکه متوقف کرد
در ۲۸ سپتامبر، یک انفجار دیگر به خط لوله ای در دیرالزور ضربه زد
در ۳۰ سپتامبر، یک انفجار نیروگاه‌های تشرین، دیرعلی و الناصریه را از مدار خارج کرد
این حملات با تلاش سوریه برای گسترش لوله‌کشی گاز عربی همزمان است - بخشی که به تازگی در الفرقلوس افتتاح شده ظرفیت را به سمت ۱۱ میلیون متر مکعب در روز افزایش می‌دهد - و نیز احیای مسیر نفت کرکوک—بنیاس.
چنین مسیرهایی می‌توانند جایگزین‌هایی برای تنگه هرمز ارائه دهند، مسیر مستقیمی به بازارهای اروپا باز کنند و هزینه‌های ترانزیت را کاهش دهند
این مسیرها با صادرات گاز اسرائیل از لویاتان، تامار و کاریش رقابت خواهند کرد
اسرائیل، که از سقوط اسد حملاتش به خاک سوریه را افزایش داده است، از یک دولت سوری ضعیف‌تر سود می‌برد.
ایران هم از این جهت که جایگزینی برای اهرم فشارش در هرمز دشوارتر می‌شود از ناامنی در خطوط انرژی سوریه بهره مند می شود
باقی‌مانده‌های داعش با توجه به حملات گذشته به زیرساخت‌ها، یک احتمال دیگر هستند</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SBoxxx/21597" target="_blank">📅 14:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21596">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21596" target="_blank">📅 14:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رویترز گزارش داد که مقامات در تایوان می‌گویند معتقدند چین در حال تمرین برای یک محاصره دریایی احتمالی با استفاده از دارایی‌های نظامی، شبه‌نظامی و غیرنظامی متداخل است.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21595" target="_blank">📅 11:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21594">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚪️
کاخ سفید دسترسی مایکروسافت به ویزای کار دائم را قطع کرد
دولت ترامپ دسترسی مایکروسافت به سازوکار ویزای کار دائم آمریکا را به‌دلیل سوءاستفاده از برنامه‌ی نیروی کار خارجی مسدود کرد. ادوبی، کاگنیزنت و اینفوسیس نیز در فهرست تعلیق قرار گرفته‌اند.
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، مایکروسافت را متهم کرد که بیش از هر مجموعه‌ی دیگری از روزنه‌های قانونی بهره برده است. کیت ساندرلینگ، وزیر کار، اعلام کرد مایکروسافت و ادوبی در مجموع نزدیک به سه میلیون درخواست استخدام خارجی ثبت کرده‌اند که به تأیید بیش از ۲۳۰ هزار ویزای H-1B و صدور بیش از ۱۰۰ هزار گرین‌کارت انجامید.
مایکروسافت در پاسخ گفت حدود ۸۰ درصد از ۶ هزار پرونده‌ی H-1B سال مالی اخیر برای تمدید اقامت یا اصلاح وضعیت کارکنان فعلی بوده و تنها یک درصد از بدنه‌ی استخدامی این شرکت در آمریکا را نیروهای تازه‌وارد تشکیل می‌دهند.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21594" target="_blank">📅 10:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21593">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔸
قطعات حساس جنگنده F-۳۵ به چین رسید
🔹
اشتباه یکی از کارکنان شرکت پستی UPS موجب شد که قطعات حساس جنگنده F-۳۵ به جای آمریکا، در هنگ‌کنگ و در اختیار دولت چین قرار گیرد. این محموله شامل پوشش شفاف کابین خلبان با فناوری کاهش بازتاب امواج راداری بود که نباید هرگز به دست چین می‌رسید
🔹
کارمند مذکور ایمیل هشدار مربوط به محدودیت‌های حمل این محموله را نادیده گرفت و مسیر انتقال دو قطعه را تغییر داد. پنتاگون این قطعات را «غیرقابل‌استفاده» توصیف کرده و برای بازپس‌گیری آن‌ها با شرکای صنعتی همکاری می‌کند. پس از انتشار این گزارش بلومبرگ، ارزش سهام UPS کمتر از یک درصد کاهش یافت</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21593" target="_blank">📅 10:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21592">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زرادخانه موشکی ایران ممکن است شامل سیستم‌های پرتاب سرد باشد
سیستم‌های پرتاب سرد در اصل موشک را از یک کانتینر پرتاب خارج می‌کنند، پیش از آنکه موتور موشک روشن شود و به سمت هدف مورد نظر حرکت کند.
شایعات و ادعاهایی مبنی بر دستیابی ایران به این فناوری از تابستان امسال در شبکه‌های اجتماعی در گردش بوده و در روزهای اخیر شتاب تازه‌ای گرفته است.
با این حال، منتقدان ایران اصرار دارند که این گزارش‌ها عمدتاً توسط طرفداران ایران پخش می‌شوند و از تأیید مستقل برخوردار نیستند؛ که با توجه به بی‌میلی آشکار ارتش ایران به ارائه داده‌هایی درباره توانایی‌های واقعی خود به دشمنانش، چندان غریب نیست.
اوایل این هفته، سرهنگ‌کل محمد اکرمی‌نیا، سخنگوی ارتش ایران، اعلام کرد که تسلیحات پهپادی و موشکی ایران از ابتدای تهاجم آمریکا و اسرائیل پیشرفته‌تر شده است.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21592" target="_blank">📅 09:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21591">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پرواز انبوه هواپیماهای ترابری نظامی آمریکا به خاورمیانه</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21591" target="_blank">📅 09:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from(تحلیل نظامی و اخبار جنگ) MilitaryToday.IR</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7pCLZMHzT6r3Dm0kfft-Rafd-Gq7XV8lDAnLS9XIxGpXo0F0XzviquFh98L6HBtjH3fRH_JyCcRqgT9vB1V2oZPu-vrft-v5KEPbLWRtr2BmzntDg5jv8lYp2rT_6F41s_Y4-xGp0gkqRYJm35vM5w23iVqvv32ISTyyz755BwV_GB10JAX5Pn1uEgEzV6pU8u4LFy81pSwCEqfWHKgAlVoiSj2WHEiqn27Q3z7rA8v8Py3iTUmEgfTs8z-EVVvQIvWquPV1GJx4IOJc8T00Q4O3cbyF1JQd347LRc6YexIYEdsNVBB9Q81WAf7n95IwAELu0OlsURJ93CarQTJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
افزایش چشمگیر حملات مسلحانه به نیروهای امنیتی کشور: 12 کشته و زخمی ظرف 24 ساعت (15 تا 16مهرماه) ثبت شده و هنوز بخشی از تلفات احراز نشده است.
Leopard
✍
@MilitarytodayIR</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21590" target="_blank">📅 00:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZS1MZK6cMS2f6WLugdLAwboJVWuhM2TivTJ-6FfCJiDeRp7GxKaIfBPwyEXaDLHYPrj8kv-WYI_kvJaj9LfrL3g-Fu1DTBiw0BU81_WH8_Ew8iFMhyUe_iOG7R3ayIsVMeArQQxeLg7an3Gl0NTZNxh5f14Sd08v3yG87AUeG-RgAuQBxe-Gn1SoRXg5JW-k_pOQXHD6eFW009tjZHXr2V7amWbSxtTZNuTCqQ9azUkvf5i2VVpUG4V0afEgZOpmiaFW5n-1GWxDUySyG1pRiprqZiH3s239Jobs8r6oFE6xfih4RUDP9uZYjkoW-vTHUus1M3knjguuoEAjxbzIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم عکس تانکری که امروز سپاه منفجر کرد
به نظر می‌رسد گاز قطر را حمل می کرده</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/21589" target="_blank">📅 00:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قشنگ آدم حس می‌کند یک مشت مافیا با هم نشسته اند خلایق را از جانفدا تا جانفنا بازی می‌دهند !</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21588" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چه بازی شد….   طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SBoxxx/21587" target="_blank">📅 00:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21586">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuTewHs2YRIMMvhQQO1wcpgTvde5B1uzcaNglnUTI0EPZ1XnRSzvr_ST8nWr4II6nyfxDz7wYWgZbgD3XR3uFfbwytbXEIwG1WzXCGeecqCq9YtwZaBheoj7vH9aWhatiO7HBKVOjyjlEJ0z41ioCl3aTWAhnjQyd2uXUNffhNx9AgoJuzIFAjfF8mW3ZtHlMDb7urs-OygU2S9M-mn_NQpEZjJiuTs-29qdgsvT27qRaMhI1Wl_6I3sKYTxnthuWM56Rpl5Ll-Sf3YOXbtFsScVYNbRGF1jthBnSu37BFVDFA5AlxAcRRnlYZHSl817FD9Ro_dxxYgDcRaY6VZjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلی با کمک هوش مصنوعی از حرکت اخیر روسیه</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SBoxxx/21586" target="_blank">📅 00:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21585">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چه بازی شد….
طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/21585" target="_blank">📅 00:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حمله حوثی ها به تاسیسات نفتی عربستان</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SBoxxx/21582" target="_blank">📅 20:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21581">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خلبان یک هواپیمای خطوط هوایی سعودی دیروز در اثر حمله نیروهای حوثی به یک هواپیمای مسافربری که در فرودگاه ریاض پارک شده بود، کشته شد.</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/21581" target="_blank">📅 19:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">افراد مسلح یک خودروی هایلوکس حامل نیروهای نظامی را در منطقه چشم‌زیارت زاهدان هدف قرار داده‌اند. پس از این حمله، نیروهای نظامی و انتظامی به محل اعزام شده و گزارش‌هایی از ادامه درگیری و پرواز یک بالگرد نظامی منتشر شده است.
تاکنون آمار رسمی از کشته‌ها و زخمی‌ها منتشر نشده است.</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SBoxxx/21580" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
