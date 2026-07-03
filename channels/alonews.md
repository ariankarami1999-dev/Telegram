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
<img src="https://cdn4.telesco.pe/file/J5wUx1ecuigg8FHemIEK4JBpFcDnOGFT1VXwFPSLUZ9_rPlcWhO_KfWxZPvS9GXGuyP6pmJQQHRiccnzfyCYKiAPIVfyNWV7p0I8tNO7UB7zQVgaOE8FpBKoCCEIC9wLdgAva5I_zco1z0-k1lz2_tYTr8r1dYGUtnS2nbyKxbYAz-7zgsVIYHx1cMInLbQLEYiMXc_vWypdJMm77pbyMfFMf1sGc0nJedyiRwCifykBPrJGAE5AzyqPBbigQSyjmyRjpBWefuznKuxVam194w-Ye9HOMGIsXFDmggUm4UmaRJKHtza6qTnP5MGwjh0XDI679OJK6EKsRamdv9xSjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 19:49:21</div>
<hr>

<div class="tg-post" id="msg-131644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COifDbQuOexX8hJ4QSnR6-Kmp4EjxRMMRRPKjbCm10SY3Yi8ldFXF515AyP4wZSpcTbBiAIEd7bap2rlIOijQ94F9VvZ4ZfvN9F7-VQNJ6nbNtO6TgTOkGdfXPrZxx2nN5nf4bhOXHX-hIusLyWxTy0pTzvd7XiYbaZEV1hknt8_V3Bo7UawStdJeAI4Kaha3OBXYi8tUrsWusW_vtQ-IyyXXF_bB5P-87cv-cR5OWGDWcpe0pHE2wZGzweMEWTFeWvI_NpwnskOtnVwFNBOoD4W5WYUn1XAy1-eWBrPoPag23OgvRrPjBpiux2ddT9hBnn8R5LxwE55iTOvumcOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عاصم منیر با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/131644" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فردا از ساعت ۵:۳۰ صبح مترو تهران فعالیت خود را به صورت ۲۴ ساعته آغاز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/131643" target="_blank">📅 19:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ: اهمیت نداره که چه DNA تو بدنته یا چه چیزی مصرف میکنی یا عمل میکنی، وقتی به عنوان یک مرد به دنیا بیای هرگز نمیتونی تبدیل به یک‌ زن یا جنس دیگر بشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/131642" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131641">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
حوثی‌ها اعلام کردند که جنگنده‌های سعودی را از حریم هوایی یمن بیرون رانده‌اند، پس از اینکه این جنگنده‌ها تلاش کردند از فرود یک هواپیمای غیرنظامی ایرانی در صنعا جلوگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/131641" target="_blank">📅 19:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131640">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eizXhXu9KW576QlhLPD5VVogKrNaARrr9ZQ6CrI2swJOJq-8jBMDs3EkwOT9E7bfvudMNXpvX5UZnKDosjTY4ZGEl4AlPTit_EuHRez8XLn4XxHV3Ile-NlnZa2DdhNnPDO7xAn21zIt8r08NfXixHTQsUOYCKtLi27N0WGBPWfQL8VMRkGEqe5sCnv52bWWGL4osR3xrGHE40xvXa1Se0sOoAwDudnUS6_lkP0XBPvlV5FFpiANefERx9jvVl9xajAIG8iyluz52srZUEF0skrP51m2MTQEmcb97gxjlL7LELxj5vaXV8Jsuz5FrYRN342-K2ucXwFx8hGTUUduvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل، گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/131640" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131639">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگویی تاکید کرد که افشای درآمدهای میلیارد دلاری اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا از حوزه رمزارزها هیچ‌گونه «شائبه یا تضاد منافعی» ایجاد نمی‌کند.
🔴
بر اساس گزارش‌های مالیاتی و افشای اطلاعات مالی که اوایل هفته جاری منتشر شد، دونالد ترامپ از زمان آغاز دور دوم ریاست‌جمهوری خود، حدود ۱.۴ میلیارد دلار از فعالیت‌های تجاری مرتبط با رمزارزها درآمد کسب کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131639" target="_blank">📅 18:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/alonews/131638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
ویس لو رفته از ابویسانی، مشاور وزیر آموزش و پرورش که دانش آموزا زنگ زدن میگن بخاطر مراسم تشییع خامنه‌ای باید امتحانات عقب بیفته و در
جواب میگه خامنه‌ای و مراسمش چه مسخره بازی ایه
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/131638" target="_blank">📅 18:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz0WLejqufBY81xzrdjA6e03QDdc8FKotRw25LIIVVwztGNocsBwxM8L5swTiGjR1XWPqsTgmI2FLFRFR97_LeTTbXlMjyeuwmwxwMJ8FN5Bi6dlFxAZHAcg0Y0BdRgkFgLISX7963kpSCUX6AuIP_QZ9-nM2f3a2DwYtv_HLFHsl48PLGEM61F06h5ylasChc-vyiuxz2irziYK45MIvRtj1Yq6Pji1q9HAV-IKwPZOadfN_Qa1IzFYw949RVjy2PrYIs3Hpn9fTC0K4qH1dEVyPYseO0Gd2Cu_SR0i8j3IzYZfRNUeqFKimdrjw9pwKyEfQcw3nSigeA5hrJjMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاه و تعجب عراقچی از گریه قالیباف که مورد توجه فعالان فضای مجازی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/131637" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
دونالد ترامپ درباره باراک اوباما:
من نمی‌دانم که آیا او یک بازیکن بسکتبال خوب است یا نه. من شخصاً شک دارم.
🔴
در واقع، ورزش مورد علاقه او گلف است. اما او به زودی در مسابقات "ماسترز" شرکت نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/131636" target="_blank">📅 18:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: رئیس‌جمهور آبراهام لینکلن از سوارکاری با اسب لذت می‌برد. من هم دوست دارم سوار اسب شوم
🔴
اما وقتی از اسب می‌افتید، من شاهد اتفاقات ناخوشایندی زیادی بوده‌ام. افتادن از اسب اتفاق خوبی نیست.
🔴
بنابراین، ما یک اسب پیر و سالخورده خواهیم داشت که بسیار کند و تنبل است، و شاید من هم سوار آن شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131635" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=DUTR0sy1k6LSl9E57gijSdcswXzVk0gbrNqYsP9OYt7fLzlwF9trDGTkoFxAtADDKCLOWyrjb7ylfDAAQkW_Wn1F9iK-IdpKMUzvIyzgWQrA4kuy-aQ5eDn5gBUh6ZCJUbNpFHOwwa9CsIbvXGbJ86D2CDw-6HnaprKamQH-c-iyf_5ium_GdPsbl9L5Ol2v4kCdrhWfjWouwmd5488_hhfxHQ0MNyq8giVtJ9wTmbPjS-PWOmC4IQ0ftJ6UbJ3TaCUPnVFtuYnwXdexxmqx4U8hA53dKNiInmicLZA6_gpY91ArEKm2YZkmtBpkCTXW1G6NMtrsH_aT01XqUKXGaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=DUTR0sy1k6LSl9E57gijSdcswXzVk0gbrNqYsP9OYt7fLzlwF9trDGTkoFxAtADDKCLOWyrjb7ylfDAAQkW_Wn1F9iK-IdpKMUzvIyzgWQrA4kuy-aQ5eDn5gBUh6ZCJUbNpFHOwwa9CsIbvXGbJ86D2CDw-6HnaprKamQH-c-iyf_5ium_GdPsbl9L5Ol2v4kCdrhWfjWouwmd5488_hhfxHQ0MNyq8giVtJ9wTmbPjS-PWOmC4IQ0ftJ6UbJ3TaCUPnVFtuYnwXdexxmqx4U8hA53dKNiInmicLZA6_gpY91ArEKm2YZkmtBpkCTXW1G6NMtrsH_aT01XqUKXGaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بیل کلینتون: او در واقع آدم خوبی بود. من بیل کلینتون را خیلی دوست دارم. هنوز هم همینطور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131634" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131633">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn72V8-HM0Uabt3wLQTCvvmb3WDGEC5uiloJ4pe4WG2YV5rD9_-JzYD253_34PjuO-dbyXIWThQnnf9QyURTXwKUYZbeP8afEJ4pirGH8mpn3X5vSSOeEH93OrqChpHdRklqE3K-sbu4VZ1QEsD-mNPvbOZ0tyPyll4JSWMMdyr7cJcSsTdfb78P_aCQLBjrwbKVFGbqW5-8TzD3xQes4U5kn5KdyR1qJzaARSm3EB48JqcxdWmWR1AwntIGf9lB-2919lI61XZdJzsL6KXa-lk1aV4fmChn8eWjl94WbaiCXPtia9dOAw6cCpPnXtuZbaom40_VFBU-Om8Y7fMdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: تو این چند روز اینترنت رو قطع کتید تا دشمن سواستفاده نکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131633" target="_blank">📅 18:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYGS8nPezzPwbpynfIo85KMEgQ_kTCVRpw1dasKq0__TNQcWqW1l8Yya6F5WZm_KmuNUZgvxHvyvI3fwnHcWUDo_B9FtVIzBoFtP_d0RGHzFA8vRaAnY92ayXHuqWQ9wFc6Hn7HLk3isvDneXGhwNjyO0pMlVlZRNQnJeqTefxbpGFwBxPy9YDDlBQcpu2GZw6cRWTnPXIiFH8RsrXRXWyAXMUaPSEZY0grVHkhhbHyUFyLgPD5VWbpd9rH__jPzrs9P7eypu1Copd3qhZSt176KzSyS0twBdjy3d04WrTP7kQynuXa7jzlwQ9MBgnLsCEYGEfF_sbgFEVq6gbu--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس برآوردهای کارشناسان، هزینه جنگ ایران برای آمریکا می‌تواند تا سه برابر رقم اولیه کاخ سفید باشد؛ هزینه‌هایی که شامل جابه‌جایی تجهیزات، خسارت‌های جنگی، استقرار ناوهای هواپیمابر و سامانه‌های پدافندی، استفاده از موشک‌ها و بمب‌ها و حملات بمب‌افکن‌های B-2 می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131632" target="_blank">📅 18:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
🔴
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/131631" target="_blank">📅 18:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=Bqhcjk0fN86qxlgmgaXa_5TorfMiKDFD-55oe75XLZ0s-ZdqcAVk3-iPCWjs2QULD4LpdRIt6TutR6wDJTjZz2FLcnR_nxO7k6QY8OcNmBGyK8IUfBaf5Oa5RXr_Ke0WaR4l60k4DpJktWYruTO3SrTgK-IInuo7cQ-wYIMWzXnxdhZLfOAT_gHmC5tJUuetokUbXGGk4esuE5QgDSrvuLaqX9l1l4rfzEH808xXa05Zfq5uFCqDrx-T7gNuS9WvWaUMR54R6HLzwx4TSXEAhanP1rjoNvgMdC0WRraq-WAbK17llRDL_4k42dEbjn1GIrW_LBGmhxXwtlvjht11kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=Bqhcjk0fN86qxlgmgaXa_5TorfMiKDFD-55oe75XLZ0s-ZdqcAVk3-iPCWjs2QULD4LpdRIt6TutR6wDJTjZz2FLcnR_nxO7k6QY8OcNmBGyK8IUfBaf5Oa5RXr_Ke0WaR4l60k4DpJktWYruTO3SrTgK-IInuo7cQ-wYIMWzXnxdhZLfOAT_gHmC5tJUuetokUbXGGk4esuE5QgDSrvuLaqX9l1l4rfzEH808xXa05Zfq5uFCqDrx-T7gNuS9WvWaUMR54R6HLzwx4TSXEAhanP1rjoNvgMdC0WRraq-WAbK17llRDL_4k42dEbjn1GIrW_LBGmhxXwtlvjht11kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایا: تصاویری از حمله امریکا از خاک کویت به ایران، با موشک‌های هیمارس در زمان جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131630" target="_blank">📅 18:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: ارتش باید در هر زمانی که لازم باشد، آماده انجام یک عملیات مستقل و اسرائیلی در ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131629" target="_blank">📅 18:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی - دیپلماتیک اسلام‌آباد جواب داد؟
🔴
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131628" target="_blank">📅 17:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=NcpzDLS8xRyx0xxPatfDpUIhaGFlne3G1aQUYMbnWlLGyKuUfHM40mkO4Ot_ifa85G0FEsWoPODtv5yo1lJ6GGXavpZaT2Me8JDVXsicysv5nJdn6QGngZhGJqUwonRudFcAatjQfpyhrv13zf57D4EFO1IAlka87eZ-hjUAYuQf4jYcfie8HlkjCTk-he2LVptHTnnZMR8IfHs-RtWL3FrZ555oHmXBRJas7CwJRroHkXTAH6pKKG_42-zQi43eFYHdZ8nmOKVAyKEe_kuG-8TLGTq2DzfY_X9_pMlLPsHu9m4_KMx4DSMSmCBr3uvXRqyCQTc5xZvYrBs7Bu6PgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=NcpzDLS8xRyx0xxPatfDpUIhaGFlne3G1aQUYMbnWlLGyKuUfHM40mkO4Ot_ifa85G0FEsWoPODtv5yo1lJ6GGXavpZaT2Me8JDVXsicysv5nJdn6QGngZhGJqUwonRudFcAatjQfpyhrv13zf57D4EFO1IAlka87eZ-hjUAYuQf4jYcfie8HlkjCTk-he2LVptHTnnZMR8IfHs-RtWL3FrZ555oHmXBRJas7CwJRroHkXTAH6pKKG_42-zQi43eFYHdZ8nmOKVAyKEe_kuG-8TLGTq2DzfY_X9_pMlLPsHu9m4_KMx4DSMSmCBr3uvXRqyCQTc5xZvYrBs7Bu6PgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر وداع عاصم منیر و شهباز شریف
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131627" target="_blank">📅 17:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131626">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iK7j2tFVP4B5-tjz_EJ6kx5SvQxxOO0PnyQiOx6neTmrULEip1Fbpw5j7yrJTVNRStQhhkr1ThPGaMDRYA9sQbOncEJyiImUUxklKnomysVSdWXh-V5rk6KAIhiSY-usQYCAFBtXbCuXUr_PizvkZG4vwz3OKI6vO6PhHTp7uUQqsAlrrVxS3VIK-IbzHvTI02NkWyO_axTI1XAFIYipajh2r5_Cfmx8elSWRv2gRN4Y55s8DWG8qII_5Tc86FHuhmE0sj_z-IEwbZUuvcp9RNhRtLCmD2dZAYmrr2qY0ZfK5VsMAZ9XzqUzHgfRFDuYYkXrkQqWHsc7rxYjs3Vhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز
:
به سه منبع ایرانی و غربی استناد می‌کند، ایران مذاکراتی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است، اما خریداران احتمالی به دنبال دریافت معافیت طولانی‌تری از تحریم‌های ایالات متحده و اطمینان از ایمنی تردد کشتی‌ها در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131626" target="_blank">📅 17:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131625">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=gd2J9kp77UKN1zTkXTjMOExteskMA1digyy9jrvfd818twEjzEmh6wj5y4ltOdOY-Rgy7FzgYA7g7WFst3Z-7NqblyfR2MV9DLKCtYOoqTWTl9H9U5OUXKdcu1bhxqqDEBPQq3AqIOLVO_GbN4sxtjbM4eRbCFUVccQE18dXHuOobeTp9EzswSLTZDaksMwQlYucNixnPhg6FopRCWUzOJ-qmPDdR4MENAi5sIT5JWb7PPEnCnKDqm8rRDZ-uL7x0kNYKDuAcJ2WM52Vi5MMkKTffCbTJkIX_-lGtX0sW-0ktiZ6JjT2CNjcTQDZio-xmCGZ09KJORMxp42lRX4I0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=gd2J9kp77UKN1zTkXTjMOExteskMA1digyy9jrvfd818twEjzEmh6wj5y4ltOdOY-Rgy7FzgYA7g7WFst3Z-7NqblyfR2MV9DLKCtYOoqTWTl9H9U5OUXKdcu1bhxqqDEBPQq3AqIOLVO_GbN4sxtjbM4eRbCFUVccQE18dXHuOobeTp9EzswSLTZDaksMwQlYucNixnPhg6FopRCWUzOJ-qmPDdR4MENAi5sIT5JWb7PPEnCnKDqm8rRDZ-uL7x0kNYKDuAcJ2WM52Vi5MMkKTffCbTJkIX_-lGtX0sW-0ktiZ6JjT2CNjcTQDZio-xmCGZ09KJORMxp42lRX4I0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام دیمیتری مدودف، معاون رئیس شورای امنیت روسیه و فرستاده ویژه پوتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131625" target="_blank">📅 17:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131624">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/63e838adce.mp4?token=PH30KMGWD83z4asOzon0WMJWXCgI7Xgr-mhvgV1tbvv0PeqpxRic0x3C2KbgihMH4-Y7zsYR0G0sWlT371obu1qSji_vZQRNHvvCwreQAfb3xtXo4k1ve1-EZCDosIhh8k3WPHlFxb8EINyRBSqIPOZhPZG79d_QBnsVOH5u6hkCeBIkBS9dV6SQ7v1kTIRjjQ3BdTpwiKNyzS3aOLpKSv7dWZo8D3YtEWYcz7cC7Jsrxg2JuCaUymnnutKQmkLdHkSYxWX7SF4AGXuHgp8A-AlolS9crvmuQWhXl7mIBaPOW4Vq9BYNJvHew3TLA_l8rCThofqTHo2vx07A494R_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/63e838adce.mp4?token=PH30KMGWD83z4asOzon0WMJWXCgI7Xgr-mhvgV1tbvv0PeqpxRic0x3C2KbgihMH4-Y7zsYR0G0sWlT371obu1qSji_vZQRNHvvCwreQAfb3xtXo4k1ve1-EZCDosIhh8k3WPHlFxb8EINyRBSqIPOZhPZG79d_QBnsVOH5u6hkCeBIkBS9dV6SQ7v1kTIRjjQ3BdTpwiKNyzS3aOLpKSv7dWZo8D3YtEWYcz7cC7Jsrxg2JuCaUymnnutKQmkLdHkSYxWX7SF4AGXuHgp8A-AlolS9crvmuQWhXl7mIBaPOW4Vq9BYNJvHew3TLA_l8rCThofqTHo2vx07A494R_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر آموزش عالی گوام
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131624" target="_blank">📅 17:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131623">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
معاون اردوغان از سفر احتمالی رئیس جمهور ترکیه به ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131623" target="_blank">📅 17:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131622">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKr2OQm8eynDwlTO0VXHSqiYyUCVddljNAyaz6TnaTpNN7nKx19Zi0e-rQx6YuKc_p1H2ZeTyZJ3D76QaZS_OBKL1WZD2h46wLmlxHRTZn3aQLQWnTPDHld9swcEX5wm0SH14IxUXCFgO52SGkERCBAFpPUJW07XwKDpra8V77iqDIkt-3rIucUmq6kxefRD1YFMqOIJgw-5Pl_qIXOz_H6CyF4o0M0BArZdXqQu4Y552d8v0LZsZ1fTIrguW5jBI5R4sKlAk64OeP0U_jURMapo8ZJv5Mo8ohrqKrBuW_1uwb2PiEz5yl4ByFFlTAHom_LccP4n7FzgorOv3mPM8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز یک پرواز ماهان‌ایر جهت انتقال مقامات انصار الله به ایران وارد صنعا شده و پس از مدتی به سمت تهران بازگشت
🔴
این اولین پرواز مستقیم ایران-صنعا در حدود ۱۰ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131622" target="_blank">📅 16:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131621">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رایزنی احتمالی OpenAI برای واگذاری ۵ درصد سهام به دولت آمریکا
🔴
به گزارش تایم، شرکت OpenAI، سازنده ChatGPT، reportedly در حال بررسی واگذاری ۵ درصد از سهام خود به دولت ایالات متحده است؛ موضوعی که می‌تواند ابعاد تازه‌ای به رابطه دولت آمریکا و صنعت هوش مصنوعی بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131621" target="_blank">📅 16:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131619">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رویترز: ایران گفتگوهایی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است!
🔴
خریداران احتمالی خواهان تمدید طولانی‌تر معافیت از تحریم‌های نفتی آمریکا و همچنین دریافت اطمینان درباره امن‌ بودن شرایط کشتیرانی در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131619" target="_blank">📅 16:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131618">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=GFBHwoDj-s8lzFrRgSNOvpx15idB7WvAAk4Chd7GGNBGEd_GSzwWizr5gnj9ob9g5LzoAE4KfKx8EyTQUUud1H36XKnHeJSmxqdx-Ek7M2ubypqx70XBif-R8tECtYqotHUm1R9_F8k_7WFux44U8vyxQIKvP1PEEOZn8Bq5stpwf9M9LlFHvvHXYFvNAcgYxHcbSKJHBAfHlAUKP0mkjmAJEu4yn9oga8IYXo30dnwsu1rCT6tGVJTiDQ1H-N5zNwzbUQYZd-ozEnmvEh-ndPUYl50uvOip2Ap-DmjVYNbjXk8deo-Ff2TGxo6r1IizNOxQXY-Axir8OKSpX-Vr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=GFBHwoDj-s8lzFrRgSNOvpx15idB7WvAAk4Chd7GGNBGEd_GSzwWizr5gnj9ob9g5LzoAE4KfKx8EyTQUUud1H36XKnHeJSmxqdx-Ek7M2ubypqx70XBif-R8tECtYqotHUm1R9_F8k_7WFux44U8vyxQIKvP1PEEOZn8Bq5stpwf9M9LlFHvvHXYFvNAcgYxHcbSKJHBAfHlAUKP0mkjmAJEu4yn9oga8IYXo30dnwsu1rCT6tGVJTiDQ1H-N5zNwzbUQYZd-ozEnmvEh-ndPUYl50uvOip2Ap-DmjVYNbjXk8deo-Ff2TGxo6r1IizNOxQXY-Axir8OKSpX-Vr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر کابینۀ نامبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131618" target="_blank">📅 16:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131617">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=qTOo0MSqNops6vYpKQi7bTdjf7lAiwPS1C-Y3zMWI2MDGvmCXRUCJfowc2egACcpfGzhoFOlpqAXi_lnqqEU_PdeT7zKLgJ5oFaxg-T_JcPu3bsEDHheq5newG7kv2gCTMJ0cNR_EWf19NpCMAbEMdowDtD0_sQNlu3u_0nbPrz_YoaDmX4kNNlbKalQrayBmDmWIxt8DGjoIr1lVQdl8oXzxaWPBxEg9J5jiSa6wPOrP5pEuoo6reU9RCHnzgELbYftvt-goYZMwiBPHQ-Ce71WGYYCtWUvYD_9FmeaoLw0dZDau1hJXk1nSu2O0xdktAkHTmqj2_Poub6Fsd2Nmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=qTOo0MSqNops6vYpKQi7bTdjf7lAiwPS1C-Y3zMWI2MDGvmCXRUCJfowc2egACcpfGzhoFOlpqAXi_lnqqEU_PdeT7zKLgJ5oFaxg-T_JcPu3bsEDHheq5newG7kv2gCTMJ0cNR_EWf19NpCMAbEMdowDtD0_sQNlu3u_0nbPrz_YoaDmX4kNNlbKalQrayBmDmWIxt8DGjoIr1lVQdl8oXzxaWPBxEg9J5jiSa6wPOrP5pEuoo6reU9RCHnzgELbYftvt-goYZMwiBPHQ-Ce71WGYYCtWUvYD_9FmeaoLw0dZDau1hJXk1nSu2O0xdktAkHTmqj2_Poub6Fsd2Nmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیمیتری مدودف، فرستاده ویژه ولادیمیر پوتین وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131617" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131616">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMhaWwyk7ITp_ZGlnBWnuQgNKH9fxa19RrENgq1lni69BJoHWSNypwZcmg8FkQMHf4ut184CEs5XyCac9AVmfgrisDi7lSEIRMv6o7t3iJ7C40Vt-d-kKO4h0UpH6smsxcJpjQIx3-vIiLeywbdhgCvdTANQBHQu9n9XOFLQc1f7PknwDQ6nYPhf-8Y8WeYkmZ5BvPG6OvMYr0vDMGT_l8zfXQ3bRqqLlNB6q0vA0nw4sDGfdWAFXxS1DSv_znW3_UMC_txbPIsJEyHtGt7zkFoVt8C58kTCI0nIiev1MPn97T0ETQo9nCftUPFfTZpTpMoel9-Qin1wWn3PmOU9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، درباره ناتو : برای آمریکا واقعاً مسخره‌ست که همین‌جوری توی یه رابطه یه‌طرفه بمونه
وقتی طرف مقابل هیچ متقابلی انجام نمی‌ده، اونا هیچ‌وقت موقع نیاز کنار ما نبودن!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131616" target="_blank">📅 16:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131615">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131615" target="_blank">📅 16:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131614">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ارتش اسرائیل:
روز گذشته به زیرساخت‌های حزب‌الله در جنوب لبنان حمله کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131614" target="_blank">📅 15:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131613">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdoPNmNZBXok1qSBFUuUtsYe9XwYWJZWEEHotv_RF-_8MXuz4dtt75jh5fTME1pCRKnkqXdKsWHPjpwGW0p7fc4eqQeXjcvgL2SjYnKCVSvCiurXMh6U_E4xpnppVPnutU24FhloXHv0XzpHPlDVZIkxejNvVgbCBGfgirUVKsNo_VW7PyBMkkmX-xBH6f1nb5n_aVGGR5JpCz9emr6ZxA27qv560u8PJesx2u6ilWwTeMn8cF3dugt9QsXEkJI7llSAbNa_lg63NDppPX4VkOW0SROu8fwGTBU_cAGcZj51QXmDPiIT0vUwVXiVeHGn1aVyc2w67qUpY2B1ZzQpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
میثاقی به اسنایدر:
ما بدون باخت و با سه مساوی از ادامه باز موندیم
🎙
اسنایدر: وقتی صعود نکنی سه تساوی با سه باخت فرقی نمیکنه
@AloSport</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131613" target="_blank">📅 15:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131612">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otCSifEwsjuqiMW-JRmuf9hT4mqw2yTaSC9jtvcXNrip2a8ExsmGSq7-zOSXwDfGtreranWNvAaiF6RqwGXi-NeVa3NfAcB1fOLnNDZrj0wxUf2KZyCXVTvDiCHE1yYSg_-M7ALkrZcCa2uaRAkNp4QxUsQBaMemPJ25KwaCCl534eaOUhk7FCR9EBO2WsZNt6PZvSmTHk70PERWDLEWJA7ha4zuh_UmLJ9c5y_vFJUCGQjsmD3eSoNol1CF2ETcxDORvLapTmreCn4dus3ql4h3UgnQ40xiUBr-z6UDNZd9IRhUnjPCz3ZrOyLSni9SWdZydq22IEYXluwPOpDckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلش ریپورت: پنج فروند هواپیمای بوئینگ 777 که قبلاً متعلق به شرکت هواپیمایی سعودی بودند، علی‌رغم تحریم‌ها، به شرکت ماهان ایر ایران تحویل داده شدند.
🔴
دو فروند از این هواپیماها در فرودگاه مهرآباد تهران دیده شده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131612" target="_blank">📅 15:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131611">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt01xbCZu8S-iBTAlHwydQPlU6GdvB5J6Jy19gjQSQpH1_gb8kXJMgfFhbCt5_y15FqGg8_YpLB5LrTxGMe0kzcxfNbOQyuO0naC-4efBobLV9l1hNx0NxyW_RLJMVGDt9VC6wZ4PQ3oYuzEDZVoAOazmGlHqat9_GOcB-Y0slUy6c0cpmTP7RFkY_J5g0-Uuk7ztj5Zw1Uzmfx5CcqY1hmr6_H3zRWC7l65hAJz5m0wgXd7VSbAgMTdGLO6E8DFR8XXg8oyDjB6y1vw0t7Sq1EWmhxbWQxHIORQqNEekbbfar44EuA5DfkXV-aX_6V2u8hEpRHdjU-JZZaMcixDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش آشنا به نبویان: راست می‌گویی در حدی نیستی که از بالا تذکر بگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131611" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131610">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=fjitt_znSnDNve09W7Bsqq8hc5v7HEHyf1N6fhCPXqbw2nCZSBdBVX6hHymTOBjYg9aDv04kCinq9UErxY-x3TYeZpfzQorVeyBwmDA-70S9M9O1GtExb7ZqBr7fBBQFS6deIMExUfBABEINfUyCGISI1O8bAEcoTuXGkgbOUi8nMQk--pMwjlgLhumsQQB1M47GSDswm-ZgvA8UJXe7mEyF7hi6T_3miUperIHvZHQIkgABgCkTIcqYn3nrxe2dkFvXdLLt4WytxlBcWgoR-l0ISXQmCXevmtkK6D9qVLzCv5uf7jJIJIvumJYpOdriSFTnUh5OHrydBXMOtQnh0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=fjitt_znSnDNve09W7Bsqq8hc5v7HEHyf1N6fhCPXqbw2nCZSBdBVX6hHymTOBjYg9aDv04kCinq9UErxY-x3TYeZpfzQorVeyBwmDA-70S9M9O1GtExb7ZqBr7fBBQFS6deIMExUfBABEINfUyCGISI1O8bAEcoTuXGkgbOUi8nMQk--pMwjlgLhumsQQB1M47GSDswm-ZgvA8UJXe7mEyF7hi6T_3miUperIHvZHQIkgABgCkTIcqYn3nrxe2dkFvXdLLt4WytxlBcWgoR-l0ISXQmCXevmtkK6D9qVLzCv5uf7jJIJIvumJYpOdriSFTnUh5OHrydBXMOtQnh0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عده ای از مردم هند در راه ایران برای شرکت در مراسم خاکسپاری سید علی خامنه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/131610" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131609">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac7N7Bd7LH-HjwT373e1--HxBs0JoYoQScj7NenRinjwfl417ZBQ3qwJfly0gBr1LkOW7Q7GUoh9egNux5f9LN2-jxJOzxKNT1kAQRirJjS61yuTPTo2Z6pTrXUCmeDk3iQgf9k8G7Ck-Nzl4JHyv99NOa5Ivc-H61tMG3U2cOHP1iAGEqlYTTqL995eyOlRY8OsrLdGCEqFNTy5SRXRIkkmmRDc33sTjMeEkS9VVCoLluCokzgcrU289rWo-RLywO37RvzHuQvHhVf98Fs_o2LfqOzEQxZDAVZCky5u5eQiLbmuCcWbw9_KGt5YH9DPgPhkq9I-1IE9OpRe_VtX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهره خوشحال پزشکیان در استقبال از مقامات کشورها با انتقاد حامیان حکومت روبرو شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131609" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131608">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
احتمال گسترش بیماری‌های عفونی و آلودگی آب‌های زیرسطحی با برپایی تعداد زیادی توالت در سراسر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/131608" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131607">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سرپرست وزارت دفاع: اگر حین مذاکره تخلفی و نقضی را از آمریکایی‌ها و افراد مذاکره کننده در طرف مقابل‌مان ببینیم، در میدان به آنها پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131607" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131606">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
واشنگتن پست: اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
🔴
واشنگتن پست مدعی شد: مقام‌های آمریکایی اخیرا فاش کرده‌اند، واشنگتن طرح‌های از پیش‌تدوین‌شده اسرائیل برای ترور عباس عراقچی، وزیر خارجه ایران، و محمدباقر قالیباف، رئیس مجلس، را خنثی کرده است.
🔴
این اطلاعات همچنین اختلافات و شکاف آشکار واشنگتن و تل‌آویو درباره اهداف جنگ علیه ایران را برجسته ساخته و نشان داد که اسرائیل به دنبال سرنگونی نظام ایران و براندازی آن بوده است.
🔴
طبق گفته مقام‌های آمریکایی مطلع به روزنامه «واشنگتن پست» دولت آمریکا خیلی زود به این جمع‌بندی رسید که این هدف از طریق جنگ، قابل تحقق نیست و بنابراین تمرکز خود را بر هدف قرار دادن توانمندی‌های نظامی ایران و ناوگان دریایی این کشور گذاشت.
🔴
نقطه عطف، ترور لاریجانی بود؛ در حالی که واشنگتن به دنبال فردی در ایران بود که بتوان با او وارد تعامل شد و ناگهان چنین فردی دیگر وجود نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131606" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131605">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / آغاز درگیری ها در یمن!
🔴
گزارش ها از پرواز جت های جنگی عربستان بر فراز آسمان صنعا، پایتخت حوثی ها و بمباران مواضع حوثی ها در نقاطی از یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131605" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131604">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
تحلیلگر عرب در حوزه ایران و پژوهشگر ارشد مرکز مطالعات الجزیره: آماده‌سازی‌ها برای آغاز نشست‌های سطح بالا میان ایران و تعدادی از کشور‌های شورای همکاری خلیج فارس و عراق
🔴
این نشست‌ها طی چند هفته آینده آغاز خواهد شد
🔴
هدف از این نشست‌ها ایجاد سازوکار‌های امنیتی و نظامی است که منافع مشترک را تضمین کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131604" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131603">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خروج بیشتر نیروهای آمریکا از عملیات ضد داعش در نیجریه
🔴
به گزارش جروزالم‌پست، فرمانده فرماندهی آمریکا در آفریقا اعلام کرد که واشنگتن بیشتر نیروهای مستقرشده برای عملیات اخیر علیه داعش در نیجریه را خارج کرده و اکنون به درخواست ابوجا، پشتیبانی اطلاعاتی ارائه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131603" target="_blank">📅 14:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131601">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEfchmfzdsw7HsM_w0SJ_LnLvQWHs4IRae9mPIzsohfyiqgsYTzgnoFsSe0rhXFYRIaJVZT7nDR11zcTzIo8sbwGW4IRBabsEyAMXVHgBsJLOy4uwcT6fXZUxh7r2NDk0JP4SMVmdaBPgUoqe5SrU4e5h-bS-v2igPkRaVhOjDZWFz_LTsNeqeCtwk8OfxrzUyNVwYr56Z91cp-4piDlTvaAqyHZGmOUEQEwHbiYgwbuhQz_bOGaz2ezgkZwJNt0nwurKeMhtUseBTK5LKbfaYXw0rtjeGf6IzMRULaeadNKzrBvWbCxepr_U_qGa7zRKp_I_1l_-OMS3L39ho0bzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0pxGFr55rRlzjIs_RwBWphvZboXDJC4ovhBEBlgf9KYC8Ch8kSd3_j2vyj6mi28mdebunTTAgZn08p7tkdv6Hx0RyaAT4VfwZaaip_3vbiyO4JQ5zKLc8_mTHKHgqjmpj4CYjRSnU0pAs2VVApnKzS4r7hOoRhkfgJj4D_U2St7d57Ql3jF4MHcTDkOkIc5y5fo8OpZPv5dEC3lhyjQDq6zjA_41GU6n-kJrXqJOQkc5280xOdxfaAebj7QpDeAcRJku2UAfPV6OJSWvL4kBhGADgnqr-Z4UE3nHo-HwUAz7tDRRSsW3lIMwvLkUjO5OIvBVeut61dlfDtQ6tc_ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجله اکونومیست حدود یک سال قبل یک تصویر داد بیرون که اتفاقات آینده رو پیش بینی کرده و دونه دونه داره پیش میاد
نکته اینه مجسمه دست خامنه‌ای هم تو مجله اومده بود
😐
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/131601" target="_blank">📅 14:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131599" target="_blank">📅 14:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/131598" target="_blank">📅 14:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e23cf75c5.mp4?token=ln2lCW2GcP0wfTk2lUKVMZAH7AMecwRINezO6aG0pX9sdpVR2T8zhj7cN3qFjSvhBbkI-ZSNckl13lTkKIQGcVtoYipZM_Ubbc9nCdkaGwzVeY1lNc74UkQzKLk3a-44WGSokAbROs4KTMJIEOml6TAUlM074XGkwgUXOonjTUpLhCw00zJCM4i0B7T-4pCYpwRn9hv0XZhx2NZvAjlpTLSBebxkqslg5kKgicuMoBqOPSbpKsa45GBavXbbiG1j14FhzjQT_I-kqrz4iXCf2lbp3qXt9Zo950f3SVN-PyRvp_thrRAbSKZYfz9khAGA1i2HEhEeJdZSIo-EBpt9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e23cf75c5.mp4?token=ln2lCW2GcP0wfTk2lUKVMZAH7AMecwRINezO6aG0pX9sdpVR2T8zhj7cN3qFjSvhBbkI-ZSNckl13lTkKIQGcVtoYipZM_Ubbc9nCdkaGwzVeY1lNc74UkQzKLk3a-44WGSokAbROs4KTMJIEOml6TAUlM074XGkwgUXOonjTUpLhCw00zJCM4i0B7T-4pCYpwRn9hv0XZhx2NZvAjlpTLSBebxkqslg5kKgicuMoBqOPSbpKsa45GBavXbbiG1j14FhzjQT_I-kqrz4iXCf2lbp3qXt9Zo950f3SVN-PyRvp_thrRAbSKZYfz9khAGA1i2HEhEeJdZSIo-EBpt9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گریه پزشکیان، قالیباف و محسن رضایی در مراسم تشییع جنازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/131597" target="_blank">📅 14:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343711e162.mp4?token=BMyl19lS3ZfnmzfnPBFmZwIPy-f5y5vd102n9PpOUjfOOluynVl9TVfkY17YkNYvSk07korMimXMq2ZWkMYeAa5cs37CL2ngVc0MBEAvvIImnqP_p-Q3Ml_vcHqy_YTHStCmHiAuCOv66UikmSeY_327ttLkP4gd0Ico3A4yZ2UwgdtZw1SC69mi7Bx80-WPBt6_thqZ13123VujEOG5sOOtq-CzaHdkiL2EYheIFc7hAGIlMSCz_hbOJ3OIjQZACY8PF4pyh_PoYXDUmBVyXGwc0z5y1qRkOh2fokbkoLwnFU7IBzjl4RTyS4jjePp4jzDZSmkiii9iut7KoPOVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343711e162.mp4?token=BMyl19lS3ZfnmzfnPBFmZwIPy-f5y5vd102n9PpOUjfOOluynVl9TVfkY17YkNYvSk07korMimXMq2ZWkMYeAa5cs37CL2ngVc0MBEAvvIImnqP_p-Q3Ml_vcHqy_YTHStCmHiAuCOv66UikmSeY_327ttLkP4gd0Ico3A4yZ2UwgdtZw1SC69mi7Bx80-WPBt6_thqZ13123VujEOG5sOOtq-CzaHdkiL2EYheIFc7hAGIlMSCz_hbOJ3OIjQZACY8PF4pyh_PoYXDUmBVyXGwc0z5y1qRkOh2fokbkoLwnFU7IBzjl4RTyS4jjePp4jzDZSmkiii9iut7KoPOVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چندصد تن برنج
🔴
چندصد تن گوشت
🔴
چندصد تن مرغ
🔴
چندصد تن حبوبات
🔴
چندصد تن از همه چیز
👈
فقط برای یک مراسم خاکسپاری از پول بیت المال هزینه میشه
🔴
اونوقت به مردم میرسه میگن کمبود داریم و گرون شده و نخورید بابا
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/131596" target="_blank">📅 13:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی ۶.۲ ریشتر سواحل شرق اندونزی رو لرزوند - USGS
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131595" target="_blank">📅 13:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a42929a30.mp4?token=NCciB_DpxSEUP4vS3Nzm72PjNB7JkhNfzvi2yo07v5AYEwk3boI4VOdyjioEHsD5ZU-PQcZARk7_m0vXpuyh7NWIBjBb5JifHvZxhhuJvKh3KjPfOGIqdNNhkk4vFBAVg5tHe8V8BjpjeUOhOXyyK0K2zJbi34zkommYORdEmQi8uZcFsqlubPRucgJcjeXqHba5cEDFGIFVZYSgzP-yFl92OG1-ErWfLTS1Nu68CmIQmdT5hzOW8xeCg88svTV5PRyHyGCX859g0x3zS0HXr3sKoBc6dNoYwSKRonPRZABLfFGcJ7z__aKLUj6YQPd2BR6TeeGW7RHWB2Ov-kMU9QPqK4Dm1gn35oLqqWMetnTVJ7VwfYt3KA4Prwd6XX-iFmoKMJXlBRk2ie-6jHDmBiL2qiojjWRg_gIRX3ZdvoSBAP-P8Hm82p7itwySZRIBI7H9xHvx5dGvHZ2Er2mKCDmJG0JisN08jSKqbxBvs0fDx9kr5lRHLFGBcu5xIcq2EPWK3Wac-MXXcyNBPIq-1jhX6N75lPIdoWWdKufXlyrBdZLFPX7WeEOgN9swEuOUip9s_pGCAn7Kh85gBWilgZtZ4dpuNQCMUn_v0FyGzHXNI-V6K9cvZsMqXBh4rumbEhsN-dRGJ5kONVJrq7sg5BPI8xTTWn6idCxKskhYYyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a42929a30.mp4?token=NCciB_DpxSEUP4vS3Nzm72PjNB7JkhNfzvi2yo07v5AYEwk3boI4VOdyjioEHsD5ZU-PQcZARk7_m0vXpuyh7NWIBjBb5JifHvZxhhuJvKh3KjPfOGIqdNNhkk4vFBAVg5tHe8V8BjpjeUOhOXyyK0K2zJbi34zkommYORdEmQi8uZcFsqlubPRucgJcjeXqHba5cEDFGIFVZYSgzP-yFl92OG1-ErWfLTS1Nu68CmIQmdT5hzOW8xeCg88svTV5PRyHyGCX859g0x3zS0HXr3sKoBc6dNoYwSKRonPRZABLfFGcJ7z__aKLUj6YQPd2BR6TeeGW7RHWB2Ov-kMU9QPqK4Dm1gn35oLqqWMetnTVJ7VwfYt3KA4Prwd6XX-iFmoKMJXlBRk2ie-6jHDmBiL2qiojjWRg_gIRX3ZdvoSBAP-P8Hm82p7itwySZRIBI7H9xHvx5dGvHZ2Er2mKCDmJG0JisN08jSKqbxBvs0fDx9kr5lRHLFGBcu5xIcq2EPWK3Wac-MXXcyNBPIq-1jhX6N75lPIdoWWdKufXlyrBdZLFPX7WeEOgN9swEuOUip9s_pGCAn7Kh85gBWilgZtZ4dpuNQCMUn_v0FyGzHXNI-V6K9cvZsMqXBh4rumbEhsN-dRGJ5kONVJrq7sg5BPI8xTTWn6idCxKskhYYyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: ۲۴ میلیارد دلار منابع بلوکه‌شده در قطر و چند کشور، به‌زودی به‌صورت نقد و تهاتر آزاد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131594" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پزشکیان: ایران همواره خواهان روابطی مبتنی بر حسن همجواری، احترام متقابل و منافع مشترک با کشور‌های منطقه است
🔴
انتظار می‌رود هیچ کشوری اجازه ندهد قلمرو، امکانات یا ظرفیت‌هایش در اختیار متجاوزان برای اقدام علیه ملت و حاکمیت ایران قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131593" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
به گزارش جروزالم‌پست، محمدباقر قالیباف، رئیس مجلس ایران، در دیدار با مقامات چینی اعلام کرد که تهران و مسقط درباره تنظیم تردد در تنگه هرمز به توافق رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131592" target="_blank">📅 13:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131591" target="_blank">📅 13:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131590">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
دلار هم اکنون 175,700 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131590" target="_blank">📅 13:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131589">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d447837fc5.mp4?token=j0x-7-CCDa4kShstonCGI5l34ssb12j1VQywJkw64SVMHAffk37unpXzmpaA0liVlN_hBchqyQ1TBLk3tmj3-AG3KiHqRUR0PP-Kcn4McbbR8dsuF2jnSdxrcOh1QPUD2KYerzR3et9rKu-ESeRwGeZ9mhqnZtLQIgocuHbn7usJWtdFlQseJBZRVN1dE0OrfRYZN1SaVv9W0YRlfMdaUPRi8CIap0jWUDWKDOpdFhR7eGZc2a4HRlIemm8x2S5I--hQsoALW3BV_d3nE___gPQo4ZOT7E8GdPgRiw2fULwITXgQTOaP9-c1n2ODfdR9RYx4yoUDJ04lQvPQI2s-Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d447837fc5.mp4?token=j0x-7-CCDa4kShstonCGI5l34ssb12j1VQywJkw64SVMHAffk37unpXzmpaA0liVlN_hBchqyQ1TBLk3tmj3-AG3KiHqRUR0PP-Kcn4McbbR8dsuF2jnSdxrcOh1QPUD2KYerzR3et9rKu-ESeRwGeZ9mhqnZtLQIgocuHbn7usJWtdFlQseJBZRVN1dE0OrfRYZN1SaVv9W0YRlfMdaUPRi8CIap0jWUDWKDOpdFhR7eGZc2a4HRlIemm8x2S5I--hQsoALW3BV_d3nE___gPQo4ZOT7E8GdPgRiw2fULwITXgQTOaP9-c1n2ODfdR9RYx4yoUDJ04lQvPQI2s-Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده ارتش پاکستان با استقبال وزیر کشور و سرپرست وزارت دفاع وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/131589" target="_blank">📅 13:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131588">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
امارات : یه حمله سایبری به نهاد مالی‌مون رو خنثی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131588" target="_blank">📅 13:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131587">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=ib3kuZF7u5odnh210UXIQelfnSAHoWPGMmVFHnrGLZWwENKpUlaFdflyju3HWByNu0Xhh3PgFkCRVYmGUmNhM-11RQcmGcg6EJeUoaYfQkPrkAnILDoMe0XNOLWTh6wMmrytSZJQcug6szB7nNYOVjWMBssDkAH2tNYs6OdDGU-Y8_iB8dZjkkMHaeH2WVp_znN_zEO9W10Xr8MS0f2x_i6IqzlQ09eS0SJDb-eUS8FC2rdn3ajd0CGYDVj61gL72QINUqnBHrAB_nAzgn_kbM5sepXvgGl6A8QpBzmMG1Kz056HYm7S9vKfEbhfFM5yoJqb3SBosLJKHtvKObMx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=ib3kuZF7u5odnh210UXIQelfnSAHoWPGMmVFHnrGLZWwENKpUlaFdflyju3HWByNu0Xhh3PgFkCRVYmGUmNhM-11RQcmGcg6EJeUoaYfQkPrkAnILDoMe0XNOLWTh6wMmrytSZJQcug6szB7nNYOVjWMBssDkAH2tNYs6OdDGU-Y8_iB8dZjkkMHaeH2WVp_znN_zEO9W10Xr8MS0f2x_i6IqzlQ09eS0SJDb-eUS8FC2rdn3ajd0CGYDVj61gL72QINUqnBHrAB_nAzgn_kbM5sepXvgGl6A8QpBzmMG1Kz056HYm7S9vKfEbhfFM5yoJqb3SBosLJKHtvKObMx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
دیدار رئیس‌جمهور گرجستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131587" target="_blank">📅 13:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحرونوت: انتظار می‌رود «اسرائیل» برای مدت طولانی در منطقهٔ امنیتی باقی بماند و این منطقه همچنان یک میدان نبرد فعال باشد؛ اما این بار با اجازه و موافقت دولت لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131585" target="_blank">📅 12:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131584">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شرکت آمازون سرانجام به تعداد ماهواره کافی برای راه‌اندازی سرویس اینترنت ماهواره‌ای خود موسوم به لئو(Leo) رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131584" target="_blank">📅 12:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131583">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
گروسی: درخواست دسترسی به تاسیاست هسته‌ای ایران را ارائه داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131583" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131582">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
🔴
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131582" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131581">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBlioKFXI4dkqilQnKCf2zInwudWVo92Zr3LSGJLVdc_r13vnFlYyEw7XPRJVhYngEVV3wfBGCYurQiO6D3bN3qeKRpk8L9ZLZU6EjX2CXn_kg94GYn4hz7DlMaJPosPQmon5b8ZHrWXM9oV318JXajfeOH9mzomcv3NB4sV8nEjbA-t2estsA-lq-vbfZFXcb-Z_V8bic4nBd2bznwUrC71n--_vQM2bfrhhOxbMcDR_Rd0FdbM7rW8Z7WghBCFRT6uRhFTQDehWC8v3FI_HHFiTdkpE4Q9GlyFB0BLiI3xegpU3sOPKxBE_nxsTr88V1aiIP5OYm2vRjE_JIJ_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
15 سال پیش در چنین روزی؛ احمدی‌نژاد: به هر خانواده ۱۰۰۰ متر زمین می‌دهیم
🔴
مردم بروند ۱۰۰ مترش را خانه بسازند و در بقیه زمین فضای سبز درست کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131581" target="_blank">📅 12:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131580">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=kNihjiINQy4oP4ibiNIRFdUWkBadHcPVBm7IwvK3SgOGvZ9TxCBaXIQn7pOZO0wJP-GWzU3_OrpRY6j9UptAzAQE8xlAio3p4HTfsAxuyklv-y_QKCwKmbrDevEtYm3CIKB68pDSp59j8borHTJ4rLS5QCEXnd-zEWtxcDMMesjZfDMZPNlcfO4X8xReh-5zT0WZKrzS6wKWJvEmrAPSrAvu7tI25OZuTMa-32LY1QGLa_PJBiD3MCnPZDmJJtIRoCpML_g7pN82Hbu3e4o2JyQ0YnxHmDn6gVkul-zEs0YRcXccN97GJRRP3uxu5DqnWpU4YgBudP1-joAWP851SjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=kNihjiINQy4oP4ibiNIRFdUWkBadHcPVBm7IwvK3SgOGvZ9TxCBaXIQn7pOZO0wJP-GWzU3_OrpRY6j9UptAzAQE8xlAio3p4HTfsAxuyklv-y_QKCwKmbrDevEtYm3CIKB68pDSp59j8borHTJ4rLS5QCEXnd-zEWtxcDMMesjZfDMZPNlcfO4X8xReh-5zT0WZKrzS6wKWJvEmrAPSrAvu7tI25OZuTMa-32LY1QGLa_PJBiD3MCnPZDmJJtIRoCpML_g7pN82Hbu3e4o2JyQ0YnxHmDn6gVkul-zEs0YRcXccN97GJRRP3uxu5DqnWpU4YgBudP1-joAWP851SjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور عراق با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131580" target="_blank">📅 12:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131579">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
قالیباف: آمریکا و اسرائیل به تعهدات خود عمل نکنند، اقدامات متناسب خود را از سر میگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/131579" target="_blank">📅 12:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmpPTWpw2GpE6a_Sx174mkIpr3vMtwgMTNaPaht_CutQ2qROVau2sBVfy5k4LhyC-KIVjd6qnIxHtk1uSO_9mv4RgjvswrJncpJ_-NejmyChMyMoXUABIwl4JoTNBFSxdV7bKimmvfIUs8UGdImPkaW8DHT17rzvPy9LnE_yTMU8_Aq7QM_QERumztwiFm6tEo2TlwDPJmtCeHGYEGsoDQdoRUmQUm3dk9OY56KmHxXZmpqSM-1uZ6c9BFfuoOd1K5BZKg9Qbg_wXF4FdG70F0fAXzwcXRSnGY_cyvY06d3RyivAjPzOpQ0Drc55o91AgPfvErr0mSdzaO7YgDzOhRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmpPTWpw2GpE6a_Sx174mkIpr3vMtwgMTNaPaht_CutQ2qROVau2sBVfy5k4LhyC-KIVjd6qnIxHtk1uSO_9mv4RgjvswrJncpJ_-NejmyChMyMoXUABIwl4JoTNBFSxdV7bKimmvfIUs8UGdImPkaW8DHT17rzvPy9LnE_yTMU8_Aq7QM_QERumztwiFm6tEo2TlwDPJmtCeHGYEGsoDQdoRUmQUm3dk9OY56KmHxXZmpqSM-1uZ6c9BFfuoOd1K5BZKg9Qbg_wXF4FdG70F0fAXzwcXRSnGY_cyvY06d3RyivAjPzOpQ0Drc55o91AgPfvErr0mSdzaO7YgDzOhRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور تاجیکستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131578" target="_blank">📅 12:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131577">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رئیس مجلس عراق با قالیباف دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131577" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6D1udW72_NFpifCaCBXV94fCosYrzjjlOyjpKV4XhNBvFOTcg2ahgxnrR5XddY_TSO7qQXc537Fizluoo3tP00TWsvOlHxzw9FzAXyr6GkfyveQGYZ5tymcBHODK7uVgdUIlaWUgvvcVSW6teYf5ZqeM1U0r5pV9cMDZFF7WyrRkQWQuZsOekSgikJTkHYPUuYAbj6uza5eIBjjGyBP0PmMuosE2aw3otVhS_P5YhbbFfNKZEAiylUf8EUgorw7W-QUdfefLmF8WhTIAd-NldxbsVDSeNW8itOlBJ9Bnt5Ca22ToWbJz82Ced99vL5io9PH7iqPc9oGHtVUu5dCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس حوزه انرژی: با روند فعلی تنگه هرمز، آمریکا به زودی عوارض می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131576" target="_blank">📅 11:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131575">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رئیس سازمان هواپیمایی کشوری: فضای هوایی تهران دوشنبه به طور کامل بسته خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131575" target="_blank">📅 11:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131574">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیرجهاد کشاورزی: هیچ الزامی برای خرید کالاهای اساسی از آمریکا وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131574" target="_blank">📅 11:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سپاه : «خطای محاسباتی دشمن با پاسخی کوبنده‌تر از همیشه مواجه خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/131573" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlmITyIF0GCdLhHMvHT1kK6jrp3B2RgIVuVmi4dLmY13RJJaE1lZIXjGog38LBT9x8JY68e_xmKfBIlh01FyfRAF2GoHpcrBzC9NuN16IpuLM9HaMkqjlFqVgmBBPq-rcvo-EP3H6r6EC9q80KCkO5IGMhxprwuKxkBskyd33BhKk7b2Jq8LLJscf7WGvg5IaSs8omWwyRkWvlDTWqyFs14MiI7NpWGdTP_tA5ZLalRQtCnzwZkCVhkY84HPwKLn5VPJk_J_O-U4kuo5ECyP6la-jfSiCAfV8EH7vJItrEAZmT-K-Z9W7ubJB6ZbHSU4D-gEm5W9G9r0iKPhtsfLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از پل ارتباطی دو استان کرمانشاه و کردستان معروف به پل بین دو بهشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131572" target="_blank">📅 11:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی اتحادیه جایگاه‌داران سوخت: برای تسهیل سوخت‌گیری، تعداد کارت‌های سوخت جایگاه‌ها افزایش یافته است؛ هرچند اولویت همچنان استفاده از کارت سوخت شخصی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131571" target="_blank">📅 11:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131567">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QgqVCyCsx_87TtA2hagIoUYdt6JY8rhUlJcQqEl3Vd6CIgQF_81U5qhlQ25_YV07dvOdXQv44dOh9W-OqUZBuPEcngLaKCRM6URGRR4d2XgNAq3acPSOm3PzM7Kjp-T-db1AsDwUNOoZPSCm5Uh6igGZwbcCim9Y9cwiEAXJasiV7x198Z3pcCBm4gAvAJ2cR8DvPQN2xSUUBAmi3TwZBp-ZSWwLiL4QKFkG1Tgi4AAAFNTNSCr88_7pz2MUfvUVxlKJKRFhFOX2yB8FtAAt3kM6L19gScwb1YMaQ4aVEs43E8SGiqLqQdm0htfBN89ytgwM5mnNHIThfYkaGzJY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHybxhEmpSxzkqzB6fl9lNianju-SZso5Ro9Njb58T6qdQ2MbLm2l7Dw0SBX2E7qJgMon_sM7bbi7SfzhN9ege8o9sX7s13VK7C734EdkYihJ0aJBL0bu1gdoSJKWbHffomD1h1iY6E_WGOyiq7OHGL-py43QAJbOthXsrQzY2LQry863OWfRAIO6i9y1vqxopFNPSx0AZVsDg-rX4WreL02bCeNGw5uI7lU6HNAOxZltcnNNWASrGQSONLBd_rbip4Ijqs5ox-V3DEtUniBEfBAaFElxbZD-gT-LBwZdTTOWUkgYwHAfU82Z_N6ITn_8MoBpL1j20iyHXI8JNmDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E714aC2i3kxefHXAdrf6vsnMk3ARzaO78BFa3Ng5dljHuAQAnKuBkQPaZLOVWdTqO9uyS8yQBRwu5cmj2jba2rcf_r32wenYftACSBPVsvYlop9bP7U4bn0c-8eZRaVNPbATy6gqybJfBjXvaCb86PEHU6Ods981rx9ruCXI80bJWUKkWNr7--fKVM9hvTE9LrPY65BL_MCoGW0GIG7mYgbUfsjg1aCrmL2Y5qTtMBGfPs73YtMJS2YHvOLbfHpNtgR5s2sC1a2UL3H0jqjLyKsP0OPVJY-C8D8KPSDwGVLaAwUk7dJ-xtSseXT4LOlcuDAgSvXygfYo-c2q13TSKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAu4WbEcHtKMoD2wjm7cZ7cez4v96i2KH3IvhrfFOB_bgSMlKMGbXLMaNGbxBD4ydckWY2QSJtLvpjAUfSeB_fTF5uZZxhfGCH5zncT07HKNXvhJAnB6TGf1s8HsbGt9cb6PEAIkwNTFTjO6ltZu9TRjPQ0UHORfqMg3_6GUklWO842gJQQqKT5Uuj0n9mx1QVlH-9-6GWOTI08jsYjA3vgVWIZ-n8IhIk2GWQF_EVvd1DqzHhjmLzLFhYkeLcAVXsDaxbJiejAzTC0FTEmzMbBYcO3Md-8T6nPoqbK94JI71WxsIwwjs79rdAzSPP11LmMOvZIjAx3H36IkvqAkIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار نخست وزیر ارمنستان با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131567" target="_blank">📅 11:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131565">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSHrTV7PHiacc2NnHmeOK57u8Ua7vrYIL-omgDt9NJ44Qh0-dWyKtk5OMz1OuK3-TQXMg8r8W_oDIoGKndiMdXXZjiJSKITHt1ly6TxZlBTap1hXYXTGCMk6L4Z6Tmh4vk5Tn4p45NwYjZkfSYqc8pDRz1Ukdm_IkOqBPygSEBbMn4gO8laIfhGZIXz86nUEumU9_98HDmQ1Hf8wlYwjKynltjf5_UM6pyL_Q9BBbtvYAE-iJMzFx1LgkIQQrPM9Gn8BudsDMxSNHDeq6rSBFBwXMjklUuGc3sG3wRSkNiz3RFN5LbTXLD6RhDGpHzzmD47GmL__jbW7rgrVKiG4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbwUJsZYTJTuyMytzZa9LgwPeNdn4GArrHvCsAuxaK0I3pZ_xNR1CxXTv1FJ2x0BRefrEDt51ZqLv30D2xTfjribS4u0R8-NKCA7FA-XEVOcWRF_OsKFfspOuuCa5m3T1SvaItpa-er-zJdMByh4Da-yik1H6owfv7O4GEma6AYv13cmPwmqRCHwlgaID1TB4Q45NKM2f0xOv8ujCIwgJ-Ix6Egf5PEq-HG7ffn2klF07ro_HkkXTxv-zpuyrEDKOTRGK2G09muB6GQJ1Sf3W8_g5FdKTmH-5hrIlPb_PBj3eN-IoqfueMfeCjNIclSXw0c2F302RqrTmgB833A-OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
براساس تصاویر ماهواره‌ای به تاریخ 7 تیر 1405، آواربرداری و پاکسازی اغلب سازه‌های آسیب‌دیده در جنگ اخیر در حال اجرا است و برخی از آن‌ها کاملاً پاکسازی شده‌اند
🔴
هم‌چنین جزئیات موجود در تصاویر نشان می‌دهند که فعالیت‌های تولیدی در بخش‌های سالم این مرکز با شدت بالایی دنبال می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131565" target="_blank">📅 11:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131559">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKC027pDO8brm1uj_nb-tY0oHjdz4Mp9bKwEtm8aG15XBOwDUhgkZyf8oHiqQwn8cnsAqdQG3fEm24UOA8NS1VdfUiun0yldCTBd0Zq-yQ6-KP1XdyXI_7ekK0JOXBCS3yt4oP_nkge732dfP1TwcpShrBqLtiJon5KCCszL50VeGA9Ck-_4PFp_PnEEkDkRr-A2_e6neaoEj-LMdpRuRaZiaDJ8RYyhf_sBOvAef2MojfoB3ZIKSuzAxvwAAADfVg4MVKM7It19UUZNdLcpobJfG3QBiAd4rCoJFiOhVkRtdCExEWRYNc9YXRrqdr53BQPORcqQ8XulhXUrKuALXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t81wR-VcbUd-zLFA1zjzMB0xQY-DwlL8nRKvCxxDr5Uie2NhFIyB2gJJJ1iVcnKLcBDBHPUf8c3GhlEfkE6g6eGCNKsCHG-lKBD_K9KyvUFq3CkPwxn_a0OIpeLooFNVqtrP9soaRpYNvnghiVlVWm9naIGgpTsuh8uki_MWaa1-GuQvylWEASEc9zZkMZy-efPx2TRLbmPTucnwSNdAgTiIA8J0FWBKg-IoqszEn8IPKS0fjHM8lxINe2FOfl_8ADBkvU8T0WENP2_EsvA4SGQuwF87HSDe2Wt_MS_BQO2y7fNfLbP9den6vYM5HbfPbFWyMKIwf3WyHsirS3nIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rJbozgh_Lko3Jb57Q2HSJGqm59AM1V-Ns5pYoAezB1HAd74NG6PtZN9miKN1x7tpUWdwSO4frn2toI-XLIVZaF-fXG1oZLFoH_T5_HqWnxS7ElIZlzAvmh7_3nQKFLkC7viwELtefOubUEzjJuqvLQsg10I6YrtT2s43Y5gGxe_yKijatXL3mJouqAq1AKdl1IpFtdUzxPo0Wj2294Nm2VIxJKbpbv2pfMugghDDQJU02N4k2f4kBc8QihyyNlfS8UH8vKyu2Xju_5Z8IANDnS8_GT232jxDsxEACVPYAZBPeAYH-8Yb3bD8qUa13tMJIVUd055HuZ0XdxR5w2PXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cyv8vRIB0qxYdTLSMz6jvhiipqVk-Xgu9-9PQ-QoxuodUfrwTYhGCliIGahVy57ss0O6jjKGwAkTeIeHIfItiyNzI9WuZZS307WjKynEJuyVQfHoaviPMgI770WeZcEucA1HUM7HPWRtUe1AiMqfSwJLTMQ1ytU8gf1cyiTZqJt53YfsXO5TU1rcTUEuDeEgExq4k1NwNSPlFrqcyHP-IrM0hwPsRTfXVu_SL9FMGUD5wQPHjg6NJdooo3tNDl_-N-2KN28tfOl2EyjvDvywUQXa8NZtZohUTRdth9fJU6tXTQTuUzJ6XDSs49Id3pXithLpUramZLIDQO2goMuvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVEmoH_5ijeArHxovZCabpni3x3Me82o758PAgrCFOhoBaSN76YZr06rhLU2IrfigJBqxKe_J7Qrr-sDrtaLB7EmLqqH54aPmSUvahpBWNRnLIvJlbpkqW8cPK63VNuRi0ElmhWIXOm31WVnvLwMJ2TGWXas82JCkxfe0McM0RPKQ82hTqpPeGy2uIl9VzOPkzrWIPNxES8eOcz0kxeBZfh_KLNcTVEeeb2vI6W8_GI8YjPSbxZJ5PXkh_t32a0qpNT6HkAPW3jypDbqyHVYWqhCUzdvYcQVeH5oY-E7A8V5A_7ZDVeTsT84Z_Y7dYQCv_YMTpucuUkzGDQsvLLsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3XQJdh3UQxSTHZHBaUYC2UmuNX8t5zIaSzeYmG-VUWdv8WcsqjiNEH22Lwymwwe54fOe7bMu_1ECtzHZML6R6QDPWmIqP26xoR2TliDjG4oKDleOjzNcCc6ACQRSur2U5Qgks14Lrldmk0EJA44vHHgivDr5q_pQ1qqPiuGSzBcR4XzswWPqdmWGi0nPkFETMgVvZ5YGQnoIiMnmI498s31w11jNSt_33br2IWnk5ZojJkUnaJ1TtSNGQhKal9omojV92g8OHBosco6XYhJx5QIg0gl-8j5ag3IfVTj6hOCUVSjxxkQ46KJyfsRMEza39IImJxxQ3sdyzK1LHM1ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار رهبر ملی ترکمنستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131559" target="_blank">📅 11:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131556">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjTei0gYZKD68b55rSyrWs4dzoUtr9DENMHjFJ197bztz4dmtj2tbbDdw-RH_d444ELqgobC2pFL2R7tmZ43vlixqzKfNfYhkBGESlgBOEN0FeRb_3tXsMeD-TJ7vBl_ggheKGWYdL8bZWwflMDte_LNWBlTjhfJCH0-vGd0ZiCrvppCRGNo5U77vjwrutxQI0rdR66sXbJul7BwudZZiB55XzARQkfOI5qoVrDtBfLOD9AXSQ-3sKwtKlfxmSbn9E6qxKf7Ir6nBAqIM7YhHUJdOmUiON0i276NtNBZpSV8E3sXv_x2rokWNRmoqilHQMs0Sp4XjJTCeUFE2XgRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5t5zIeqtIVvw1Pu8-LaDor7wICYpFALlN8OzQBQOYG3Ov9218jvY7jpfyrrW5xe3qgK5LDyECHePOIG77FR-qi9oGssXbBLWhwaxgNBQa-NgzJv-Dw8Zxw5rDDzsvHg1B015pAW4c1CfX7-OcJ6OkMn5G626V-RfON8GOs6bVY0MjqK-FRWny9h8eBBD_uH_lcnZrOQVLz7UNkZwt7eMoynnRLGSLwnLzRDT3QadoUelhPt-k2aAzj0_ZOn7ljjP5Y9LmxGdEjSM1HjX5PYPYKCTcheGA0fdcWWqoVNC2E6Nii5tUFLkpZyFrwho5I4GUN7bnurhWSxQHQCXgTZog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMcTNRqD6GHLmu5kdmQm-fFMgrDeF3aMqYng5MMxbqYdUvjbCCKeXGW-l_n1elW0FfVp2DoibI9tE8ypJmnv2cBBpMcbhk8ctt-pEuSZ3Z78EUwinosYRjfSvdpH8Pdc57BeDTNdbKtwMwbFuHFu9oMkKRoRkzEo0-LiS4w_QA1jYnKJB6BE9nay6Vxsz1bXkxdi37t3R74xI33HntNEIDkVF6h_2F4xZWZ64x4fmwDYAkunLImsIAR8T7VhMchecEslx8zEDNqSdLU32rKonFkaAsbhPW87icMUvQwQTAJKkxj6lnsJWazqbfx49cxpGP6ZjwX7rP0xsUSG9tLXxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار چارلز موبیتا وزیر کابینه ریاست جمهوری نامیبیا با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131556" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131555">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBDMh315TJzUWJR9PW2bTdIA9p-e1XNTRtYBOEv8-_fqXpr4zrYFwcAclQqOxKE0DX9VZF69QOTU9-uHY-twPEnEHys0pg7vepZs1u0G36l0zK6zR4sMjM5Vj_axpdjy_hpCyGDKKbJZfNiAU7KYWjc1pYT16LNqkgS0xWgMCl761GWghuHyN9su8Aqhb2hcg3eMfCi945O3jsUr7CkGInqvJWDTlNmR2XdhIWmN0IICGgdbu3WcY3iyVAR52hlQ2ne2gKHU3WqU3NiiaA_ESCdQsC-rozoesJDziAI83n5ISF6gW_zSafpLW0Hn3DL3APR2RtBQuCINGwtP6RGm2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت جدید ظریف ، وزیر خارجه سابق
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131555" target="_blank">📅 10:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131554">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
قالیباف در دیدار با معاون کنگره چین: اجازه دخالت آمریکا در تنگه هرمز را نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/131554" target="_blank">📅 10:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131553">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9742057ed5.mp4?token=pryY0UEYF2En6NqLyckeAPu7twymr9phIacdur6NZrhy_6_N99lZhdEz3dFmpF4IFzkAMIAQvGO_1cYhvWfBxLiouLCRxBHboicnc2vg5xF6i0nWVW84UPJuBe6-RJqnVBdJx2oC6wszB3srLnG-d2d4kP5GFPb2L7iNNmvnSbO9PgaOXxqihdvynTdY1BM37lItsgV8SV_fI2F4JxV9jFfgxtxOvo_A2k7pinRVdq8N3bAD8naKNWS9KkPW4SFJ1JPEcToERbeS3Jcffp9FWLIn-PAzLt0sFUQJU6r9EHm3zho4_VAgcgqOpB75ocWNOxufrwu_ecn9EV1JvalPqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9742057ed5.mp4?token=pryY0UEYF2En6NqLyckeAPu7twymr9phIacdur6NZrhy_6_N99lZhdEz3dFmpF4IFzkAMIAQvGO_1cYhvWfBxLiouLCRxBHboicnc2vg5xF6i0nWVW84UPJuBe6-RJqnVBdJx2oC6wszB3srLnG-d2d4kP5GFPb2L7iNNmvnSbO9PgaOXxqihdvynTdY1BM37lItsgV8SV_fI2F4JxV9jFfgxtxOvo_A2k7pinRVdq8N3bAD8naKNWS9KkPW4SFJ1JPEcToERbeS3Jcffp9FWLIn-PAzLt0sFUQJU6r9EHm3zho4_VAgcgqOpB75ocWNOxufrwu_ecn9EV1JvalPqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشت جوان پول خود را روی هم گذاشتند تا یک موتور بخرند و نوبتی استفاده کنند...
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/131553" target="_blank">📅 10:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131552">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
فایننشال‌تایمز: ترددها از تنگه هرمز چهار برابر شده‌است
🔴
یک رسانه انگلیسی نوشت: اعتماد به آتش‌بس افزایش یافته و ترددها از طریق تنگه هرمز در هفته گذشته، بیش از چهار برابر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131552" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131551">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر کشور پاکستان پس از ورود به ایران: اینجا خانه دوم ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131551" target="_blank">📅 10:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131550">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd05539a.mp4?token=nRa8zF_BIJwa26SQzRtKJ6fvZkrvjD_PzP1RY83hkxvtIswzJXyiPQSRAAf-mN8Qp-Zm_kQD1hsxk2ALiefJW5fhrJtFeAdIta86YT1Cb6zaBIMyLzhBYSzu-tV1VtxN0uJAtHXSZbgkaxdL0UMsThCvLOEQpZAnk4ih38xyfoprSjSGGqEKSq02acHV4IE65Mvnvh45xq93DT_UPz1VoFQmoodadLhAIj-B0rJFl3njzm9TuOJ4J3l0MgN7HUGWqH49nJNx_zIYuOOrBpfiTtU1luy3N-hsgm685gRpQlVam9G6kcR9TxJxweNuczKJRYM0Ic2tjXEBnjHS9837madL7hd0-i0_yWidHQyiHPccbSZlv0Y3UXwKyFnj63auY2NHhhYf0HmsTLbkse8I6GZMpDrZrMC_bkcwdv2c-r47LgAOAsLSTjBQsf8fOMCLW8qJwIba0W6CnjSIPTOPW5VX3rPDhOmdRYagHKZ4DcGOdLOn_mjOQWznIWv2fY7rLOfnyPbtH8SfpKbwYKalwElrccYOpip3CkbOFliidE6jz4HSnbR8ixwXqRcLc1G2xiOhpVyu7C1349QpuQaWZ5QDMAHZ_GC8QJt2ttl5dBJFv_iiZPVF_AkgEFq-NqynPMJnsEjlCy2yNJpzJDdnfRr98jD_i5vyT9b020tK_JM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd05539a.mp4?token=nRa8zF_BIJwa26SQzRtKJ6fvZkrvjD_PzP1RY83hkxvtIswzJXyiPQSRAAf-mN8Qp-Zm_kQD1hsxk2ALiefJW5fhrJtFeAdIta86YT1Cb6zaBIMyLzhBYSzu-tV1VtxN0uJAtHXSZbgkaxdL0UMsThCvLOEQpZAnk4ih38xyfoprSjSGGqEKSq02acHV4IE65Mvnvh45xq93DT_UPz1VoFQmoodadLhAIj-B0rJFl3njzm9TuOJ4J3l0MgN7HUGWqH49nJNx_zIYuOOrBpfiTtU1luy3N-hsgm685gRpQlVam9G6kcR9TxJxweNuczKJRYM0Ic2tjXEBnjHS9837madL7hd0-i0_yWidHQyiHPccbSZlv0Y3UXwKyFnj63auY2NHhhYf0HmsTLbkse8I6GZMpDrZrMC_bkcwdv2c-r47LgAOAsLSTjBQsf8fOMCLW8qJwIba0W6CnjSIPTOPW5VX3rPDhOmdRYagHKZ4DcGOdLOn_mjOQWznIWv2fY7rLOfnyPbtH8SfpKbwYKalwElrccYOpip3CkbOFliidE6jz4HSnbR8ixwXqRcLc1G2xiOhpVyu7C1349QpuQaWZ5QDMAHZ_GC8QJt2ttl5dBJFv_iiZPVF_AkgEFq-NqynPMJnsEjlCy2yNJpzJDdnfRr98jD_i5vyT9b020tK_JM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مأمور پلیس آمریکایی، یک زن را به ضرب گلوله کشتند
🔴
مقام‌های محلی در اورنج‌کانتی آمریکا اعلام کردند که سه افسر پلیس پس از مواجهه با زنی که چاقو در دست داشته، او را هدف گلوله قرار داده و به قتل رسانده‌اند.
🔴
گفته می‌شود تحقیقات درباره نحوه عملکرد نیروهای پلیس و جزئیات حادثه آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131550" target="_blank">📅 10:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131549">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پنتاگون: اروپا مسئولیت دفاع از خود را برعهده می‌گیرد
🔴
وزارت جنگ آمریکا مدعی است که تلاش آن برای وادار کردن کشورهای اروپایی به برعهده گرفتن مسئولیت امنیت خود، موفق بوده است.
🔴
«البریج کولبی» معاون وزیر جنگ آمریکا در امور سیاست‌گذاری، در صفحه شخصی خود در شبکه اجتماعی «ایکس» (توئیتر سابق) نوشت که ائتلاف «ناتو» اکنون به سمت تکرار وضعیتی پیش می‌رود که در آن «اروپا مسئولیت اصلی دفاع متعارف خود را بر عهده می‌گیرد».
🔴
این مقام آمریکایی اظهار داشت که هنوز کارهای بیشتری باید انجام شود، اما واشنگتن به حرکت به سمت نسخه جدید ناتو که مبتنی بر مشارکت، نه وابستگی باشد، ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131549" target="_blank">📅 10:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131548">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
به دلیل تهدید مداوم وزیر دفاع اسرائیل به جنگ و ترور، ممکن است در دکترین هسته ای خود تجدید نظر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131548" target="_blank">📅 09:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131547">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سرپرست وزارت دفاع در گفتگو با وزیر دفاع ترکیه: ایران توافق آتش‌بس را با هدف کمک به بازگشت ثبات منطقه و به درخواست کشورهای دوست و همسایه امضا کرده
🔴
اظهارات اخیر مقامات آمریکایی درباره گشایش جبهه جدید علیه حزب‌الله لبنان می‌تواند کل منطقه را با مخاطرات امنیتی جدید مواجه کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/131547" target="_blank">📅 09:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131546">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
میخائیل گالوزین» معاون وزیر امور خارجه فدراسیون روسیه بامداد امروز گفت که مسکو آماده است تا مذاکرات با کی‌یف برای پایان جنگ را ازسر بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/131546" target="_blank">📅 09:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131545">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی:  مذاکرات با ایران همچنان ادامه دارد
🔴
ویتکاف و کوشنر، در قطر نشست‌های سازنده و ثمربخشی برگزار کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131545" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131544">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
تعداد کشته‌شدگان زلزله ویرانگر ونزوئلا از 2500 نفر فراتر رفت
🔴
به گفته دلسی رودریگز، رئیس جمهور ونزوئلا، تعداد کشته‌شدگان زلزله در ونزوئلا به 2595 نفر افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131544" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131543">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گروسی: ذخایر اورانیوم غنی‌شده ایران هنوز از تأسیسات هسته‌ای خارج نشده‌اند
🔴
ما دقیقاً می‌دانیم که این مواد کجا بوده و می‌دانیم چه مقدار از آنها وجود داشته؛ پس از جنگ ۱۲ روزه در تابستان، ما با استفاده از تصاویر ماهواره‌ای و سایر ابزار‌های مشابه، اشیاء را زیر نظر گرفتیم؛ هیچ حرکت قابل توجهی را ثبت نکردیم
🔴
بازرسان آژانس انرژی اتمی هنوز به تاسیسات هسته‌ای ایران بازنگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/131543" target="_blank">📅 09:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131542">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=u--Y6q81uoVpbZ26UiJuxQ9F__uEmdD_CuUfgK_pJ1hJukaP1nHUWcMB4phhd5vXjGHa9ZpfLwaHVDXiUteGRa2-J1F6EpXCubVmIDngeMDekIsJP1FgkRFR-Qw5IMQHwNzf9EwHYMMq7r6OC5HOLD_LEX8WI9hF-Dc6iEyTvKaombgMVENYk5NKlFodsPOG5TPSPWHyIcDOvK2oT9mwV8kfp9eVKdab2NnGslz164SQ_-bF1zO1ZBqXy41BLaxp67RDA2vimKGW-1Po9eKgbsx7rylbuoYD2i2bkM8YwrWJ2NRSXz0uqdQV4s3JyRUDmYyv0FthekVCAfPm_M2p0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=u--Y6q81uoVpbZ26UiJuxQ9F__uEmdD_CuUfgK_pJ1hJukaP1nHUWcMB4phhd5vXjGHa9ZpfLwaHVDXiUteGRa2-J1F6EpXCubVmIDngeMDekIsJP1FgkRFR-Qw5IMQHwNzf9EwHYMMq7r6OC5HOLD_LEX8WI9hF-Dc6iEyTvKaombgMVENYk5NKlFodsPOG5TPSPWHyIcDOvK2oT9mwV8kfp9eVKdab2NnGslz164SQ_-bF1zO1ZBqXy41BLaxp67RDA2vimKGW-1Po9eKgbsx7rylbuoYD2i2bkM8YwrWJ2NRSXz0uqdQV4s3JyRUDmYyv0FthekVCAfPm_M2p0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل : اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است
🔴
این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131542" target="_blank">📅 09:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131541">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فاکس‌نیوز: مقامات ایرانی نسبت به برخی بازرسی‌های هسته‌ای روی خوش نشان داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131541" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131540">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
فایننشال تایمز: با افزایش اعتماد به آتش‌بس، عبور و مرور از تنگه هرمز هفته گذشته بیش از چهار برابر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/131540" target="_blank">📅 09:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131539">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5NHks1ynTcw-h5ShiLV3Hoo5D8PhV8f8Akpxf8LPOCStWiVF0JbDlJe0-C9idWHt5dfB-P9sj6um1M8ppEWN_fJMgUkWmAEc4ej_W8p_hwL8Jo1eIkyBGWwW731EcbYknAVHY5QyIB2wt1uK1QjZO1ZiobhCoxb_wUKySFqdyZXPLfkfrNZiTwo3cSZk59twOztQz4wltUEgaaLkiTlJyQOX8GJHAotos_m4NyV0D-_T29JxO2e5RqPT6RMk9-tG5OEnd5syZlUe5qef_Yanloo9pUxqiHbXvFD_ys9CsIBOCj1jx5CMYacLak0hpgGxfj_yTxS46IVH14kBXH2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور پاکستان برای تشییع جنازه سید علی خامنه‌ای، وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/131539" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131538">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDoQAgOobv9SqtwCRTxDeUA3eYJZ2dsaCN__ybyAhb9YhgW_897LdBPung0UYXG7xFwZJDUC-ORI_5ZOUuqtnvanl5CsCA1MeACGRNU8mJ6tXCeXNxgSRSq3lDNZ1G1oatXuPJIcRllIYnGEZjFouvgy58joYNvyMiWOwD_cQzDsD0ytzV1a1KMQB5mGNSFnyh03mYC_nVcy1Dhg3ebRJ9OSos1mBLYsH7HvP6u5amqRp8XO51BWdMM6n3PbbtKVeKL6I1hdwnS9IzZYWFPJQ_P9HQ1sua2QNlZ7A6oJ9WMy1owyZaz3JZWXdOB05njq9BP3oPljYYdMtBQJbBQeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از آسمون منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/131538" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131537">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
منابع خبری از حملات اسرائیل به شهر صدیقین منطقۀ صور، در جنوب لبنان خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/131537" target="_blank">📅 02:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131536">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: مردم ایران از من تشکر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/131536" target="_blank">📅 02:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131535">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/131535" target="_blank">📅 02:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExpWcHgYyHRr1V9LRl9xb0ytjQwljjnTl4-uBp6SbV1DGYMtSDzFaZkCreGNHelv_hZyM1itjxFWp2FOm62kBoofq7kUPM5mf58gs0cU5XCN7eVPVXIUPuvl8SGNQ_de9mQZit66PQsgRzHS1XSfpUfq5jo_OKmISoL_n1O3E-zgPNi0VPSzNdBatk1JkC5ALp5rPaXY5d1JFaR-jgCX3SW3QTBrUA9vKREHf1mWKMCtufXYm3SDYqR0CPDj_KvsJjAMuh9z_o_nbGFDZFn13Dj4MES43-8wPYTY4MXtUYoXyTpm09GrqSqSxZNS6IzDIMQD2M_bT-s5Zb-zpJYEBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/131533" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3df6d8da.mp4?token=KHlL7EOumF-G8lzPnX-qsByevlTav9P59_qoJo69cXtVQTxGWUZ89KgrQ3ZtUz49OI2IK8nwuP-IAwelzd-Rx3--un9tmDuLUdmEbdG6YoZsUThdpnthAsocPr-vPxmpVA2nzb5RqBT-PNKzEq9ma8cPLL4aC9HU0hpYYNvjn2_lJw_b-QOjtfMSkEPOB_L4D0zV1HqefV1lLqICu8vK3DX4H675xXmEOLgQ1y0Gvc-X9XGAAIWaBU-IjPYC-Ad-qV9MOfPVSb23YMnKl7DX2O-jxAm1tS2J904HaSMcDgRLJrxdzqlu7oILpXWTxRVGXE4z85HxBK7jSbWNWAEb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3df6d8da.mp4?token=KHlL7EOumF-G8lzPnX-qsByevlTav9P59_qoJo69cXtVQTxGWUZ89KgrQ3ZtUz49OI2IK8nwuP-IAwelzd-Rx3--un9tmDuLUdmEbdG6YoZsUThdpnthAsocPr-vPxmpVA2nzb5RqBT-PNKzEq9ma8cPLL4aC9HU0hpYYNvjn2_lJw_b-QOjtfMSkEPOB_L4D0zV1HqefV1lLqICu8vK3DX4H675xXmEOLgQ1y0Gvc-X9XGAAIWaBU-IjPYC-Ad-qV9MOfPVSb23YMnKl7DX2O-jxAm1tS2J904HaSMcDgRLJrxdzqlu7oILpXWTxRVGXE4z85HxBK7jSbWNWAEb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور:
نمی‌فهمم چطور یک فرد یهودی می‌تواند به یک دموکرات رای دهد.
من بهترین رئیس‌جمهوری بوده‌ام که در تاریخ اسرائیل وجود داشته و آن‌ها هم این را می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/131532" target="_blank">📅 01:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131531">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac200869f.mp4?token=E6_66VUYyyUFi6BL7zIPuHeNLgjOTiAF19pdjeCJxOBC3wrY31PBa6-icClc-kjnfB4k-keZLWfh9SVf4Pu8MW0pFSxnJp55SeAmaUb2DHQoVUBbU-c4tOrbwotTa4y1BkGjkBRg9GzHhDB3dNcvfMU9ht8iHLN4huLAYWwUoJwYvhVpK05Ff2sUyetukfb8CCMPpa6816Zy5WvumiCXjbX3vpC5DKgheFH_ISscxxUzVAS1T1dlOdVrzKrAOWAxhHZLvz17UcCrXL1biCr1Ug14hWguDbVUmQnPp_mwKfXt6QEY7Pu89-Bby2ay_1Rq6H5Ryyi7NzB16P3MjQoAww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac200869f.mp4?token=E6_66VUYyyUFi6BL7zIPuHeNLgjOTiAF19pdjeCJxOBC3wrY31PBa6-icClc-kjnfB4k-keZLWfh9SVf4Pu8MW0pFSxnJp55SeAmaUb2DHQoVUBbU-c4tOrbwotTa4y1BkGjkBRg9GzHhDB3dNcvfMU9ht8iHLN4huLAYWwUoJwYvhVpK05Ff2sUyetukfb8CCMPpa6816Zy5WvumiCXjbX3vpC5DKgheFH_ISscxxUzVAS1T1dlOdVrzKrAOWAxhHZLvz17UcCrXL1biCr1Ug14hWguDbVUmQnPp_mwKfXt6QEY7Pu89-Bby2ay_1Rq6H5Ryyi7NzB16P3MjQoAww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همزمان که تو تهران با بیت المال داره اینهمه هزینه چند صد میلیون دلاری میشه برای یه خاکسپاری، بهتره این کلیپ هم ببینیم
🔴
ان‌شاالله که همه مردم راضی باشن با حقشون داره اینجوری ریخت و پاش میشه و دینی به گردن مِیت نباشه
#بیت_المال
#تبلیغ
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/131531" target="_blank">📅 01:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131530">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937314ac6d.mp4?token=I1N4VT5-wUvAJzP2S9BRz2E36QM5O7SvK5HzzSS4Gj52JIkkxawf61qt4ZCEwijl1zBAjOWy-2WhHNCtgO1gAq-MMXjFu_jURg7W99cZW7dNucF0-SBFjAgXAgLWDMPX9VEJAb-NHk3FYIrLoLfqfoEHzmy7JDm-yqLHY0v4Dej3NtS5KAF1Hv_ByUF6ob_57xkS2TPpzyFmBGOGnPqUNBEjqkIcZu60JEOUtd7jFGdD7CCkN72sRpnqQIVgl0tqbG0ojV04m4qlHu9MVeR-QD-ZKd-DlPi3R2TK5ZJhpFuoRknITXgFZNmd9Sc2va-paQWxb3uw_Bs5MpekeugBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937314ac6d.mp4?token=I1N4VT5-wUvAJzP2S9BRz2E36QM5O7SvK5HzzSS4Gj52JIkkxawf61qt4ZCEwijl1zBAjOWy-2WhHNCtgO1gAq-MMXjFu_jURg7W99cZW7dNucF0-SBFjAgXAgLWDMPX9VEJAb-NHk3FYIrLoLfqfoEHzmy7JDm-yqLHY0v4Dej3NtS5KAF1Hv_ByUF6ob_57xkS2TPpzyFmBGOGnPqUNBEjqkIcZu60JEOUtd7jFGdD7CCkN72sRpnqQIVgl0tqbG0ojV04m4qlHu9MVeR-QD-ZKd-DlPi3R2TK5ZJhpFuoRknITXgFZNmd9Sc2va-paQWxb3uw_Bs5MpekeugBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تورمشون ۳۰۰ درصده هیچ پولی هم درنمیارن برای همین یه بخشی از پولشون رو می‌گیریم
🔴
اگه به جایی که مدنظر ماست برسیم، تأمین غذاشون فقط توسط کشاورزهای آمریکایی انجام می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/131530" target="_blank">📅 01:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131529">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی: رهبران فعلی ایران منطقی‌تر هستند و ما با آنها کنار می‌آییم و این تغییر رژیم است
🔴
من به دنبال تغییر رژیم در ایران نیستم، بلکه به دنبال جلوگیری از داشتن سلاح هسته ای هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/131529" target="_blank">📅 01:31 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
