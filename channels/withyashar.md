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
<img src="https://cdn4.telesco.pe/file/RcNWJov13IRwYWKvNLtkRKXmHoK2PuJsOyDHUXwV5gJejWWv8cEh3hw-UE5p36v6HCnSH7Ozv7imNkbGJWIfvnMa-3Q2gmZI4eKURg42ZCzKTTKBaYa67edaOxHbZpI9IrrIYLDEsvd-kQ9Fa-f0CrpVtC-X2kxBYR10anlhBftsW3H1UweAdv8XumWhg3-1KaytA4llOoz2L3P_MG4bPMBR0g0fn_un0hoAjRa14T_xIziJ0EDvFzOLgdoifsGvRhG-4JyN88-YlFYXslv20CI5mcB2cHSxHqFUIEJpra9977P7wvazA0n82IKR0ePuLlNByLFR_nNsIrGSyNH4aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 411K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 18:26:48</div>
<hr>

<div class="tg-post" id="msg-18884">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/withyashar/18884" target="_blank">📅 18:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18883">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb62a2aa1d.mp4?token=f_jOJs-WrKrX9kPG_WnzRLHQtzXFJiaJVVcXRtqkA25FJwLKI1GcQ04rrfl8xnhgNOHzsWzmAkxbPW0z8FLUEXmQ4k4kfihN8anhHB75GKIUz8YPAWQXRxWKp1Io12lp13GoSi5ugTvl6DbAheHxjzondZyfoUWU1qq0u1GN2sVNhVypBNCS1c6wuipP0vNOPVDVewahEIrBgF9t83oJiYPLsvHfYJmxsiT2TsruM4zFc79MxdA9homdm_JVICfYGZoY3x97I3gjQzoWLwRCyQzJP2NAFSGVnsvdC72vLkRGARZsRJGEz0wRi_oQ58_bWS4K8e-mlnBStAEQP5lxTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb62a2aa1d.mp4?token=f_jOJs-WrKrX9kPG_WnzRLHQtzXFJiaJVVcXRtqkA25FJwLKI1GcQ04rrfl8xnhgNOHzsWzmAkxbPW0z8FLUEXmQ4k4kfihN8anhHB75GKIUz8YPAWQXRxWKp1Io12lp13GoSi5ugTvl6DbAheHxjzondZyfoUWU1qq0u1GN2sVNhVypBNCS1c6wuipP0vNOPVDVewahEIrBgF9t83oJiYPLsvHfYJmxsiT2TsruM4zFc79MxdA9homdm_JVICfYGZoY3x97I3gjQzoWLwRCyQzJP2NAFSGVnsvdC72vLkRGARZsRJGEz0wRi_oQ58_bWS4K8e-mlnBStAEQP5lxTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه I24NEWS: چند هفته پس از ترور رهبر سابق جمهوری اسلامی ایران، یک گروه تحت فرمان سپاه پاسداران در امریکا، قصد ترور پسر بنیامین نتانیاهو، به نام یایر نتانیاهو را در خانه‌اش در میامی، فلوریدا، داشت.
با این حال شین بت این توطئه را در آخرین لحظه طی درگیری در پارکینگ اپارتمان وی خنثی کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/18883" target="_blank">📅 18:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18882">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتانیاهو مصاحبه‌ای که قرار بود امروز با شبکه فاکس نیوز داشته باشه رو به دلیل شرایط اضطراری لغو کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/withyashar/18882" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18881">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb30b2010.mp4?token=ivPg2czr1nAZtUjCwyVT6hIR76sh9UQCvQ9P_GH2Mr265KvlLS-3Te-7GfwSmBVbF7lWz4zb9ri_WjUWtUdfScKiztCpXSok4Rx611robH1N5QBcHClYSDLEqQ0a2gyklz3Awx8YM8zLImgl6nlSBBQ1206OWJb9qx_154LTokujh2f-NT5ZOm7W-gZUvhbA6GSFWBlGT-jlJ1V_XMCF-LpWxhpbC4ioQMRlMyXK2-cf0dzDz_1ahlE11IC0WmesjesFcwtmGBT5lnPOlbdW9eERrWp9yTBNOF4mLuX3yNt8cMj5SMX2h-iUBK1AZiEzEKRMKzhoH0p8Old-rA-LMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb30b2010.mp4?token=ivPg2czr1nAZtUjCwyVT6hIR76sh9UQCvQ9P_GH2Mr265KvlLS-3Te-7GfwSmBVbF7lWz4zb9ri_WjUWtUdfScKiztCpXSok4Rx611robH1N5QBcHClYSDLEqQ0a2gyklz3Awx8YM8zLImgl6nlSBBQ1206OWJb9qx_154LTokujh2f-NT5ZOm7W-gZUvhbA6GSFWBlGT-jlJ1V_XMCF-LpWxhpbC4ioQMRlMyXK2-cf0dzDz_1ahlE11IC0WmesjesFcwtmGBT5lnPOlbdW9eERrWp9yTBNOF4mLuX3yNt8cMj5SMX2h-iUBK1AZiEzEKRMKzhoH0p8Old-rA-LMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام
:
ملوانان در حال آماده‌سازی جنگنده‌های پنهان‌کار F-35B نیروی تفنگداران دریایی امریکا برای برخاستن (تیک‌آف) از عرشه کشتی جنگی "یو‌اس‌اس باکسر" (USS Boxer - LHD 4) در حین عبور از دریای عرب هستند.
ناو باکسر، کشتی فرماندهیِ گروه آماده خاکی‌خاکی باکسر  یازدهمین واحد اعزامی تفنگداران دریایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/18881" target="_blank">📅 18:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18880">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee9644417.mp4?token=OgamqHUA7XTAwfu0SV5BwJwfLT5tYkV3bK-_1jtRu9bwvAKZF_sLSmmfDUJbkLupEYhQrBHzzRUrsMgbGt0QM-zMqh-uziJeFRb0jYlcZa71JVCghnacVp4IMeEtoVs_xFHqW-lMlflAsFQb80netEOpIJ596dkaeTGApHdoaTreIB4b5WLiQn2ZibzMJa3iM1hMSFBkIVuHOtw8t0K7kAnnDQCeIOq2Uj9GggkyJScDLeDhUaDqlNIilEYqHnyAoF3hKPAJ4Va2JQ0Bo2pUkRCZXtkH8NVqpbuNPKIstqr0iRAPQIFmCbml9WDsrMNA21DnRdkPr0ygLmbzcdHtfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee9644417.mp4?token=OgamqHUA7XTAwfu0SV5BwJwfLT5tYkV3bK-_1jtRu9bwvAKZF_sLSmmfDUJbkLupEYhQrBHzzRUrsMgbGt0QM-zMqh-uziJeFRb0jYlcZa71JVCghnacVp4IMeEtoVs_xFHqW-lMlflAsFQb80netEOpIJ596dkaeTGApHdoaTreIB4b5WLiQn2ZibzMJa3iM1hMSFBkIVuHOtw8t0K7kAnnDQCeIOq2Uj9GggkyJScDLeDhUaDqlNIilEYqHnyAoF3hKPAJ4Va2JQ0Bo2pUkRCZXtkH8NVqpbuNPKIstqr0iRAPQIFmCbml9WDsrMNA21DnRdkPr0ygLmbzcdHtfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از سخنگوی قرارگاه کلش آف کلنز منتشر شد:
@WarRoom</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/18880" target="_blank">📅 18:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18879">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مهر:
معاون امنیتی استاندار خوزستان گفت که مکانی نزدیک به شهر آبادان لحظاتی پیش توسط حمله موشکی متعلق به آمریکا هدف قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/18879" target="_blank">📅 17:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/18877" target="_blank">📅 17:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رویترز: حملات حوثی‌ها و ایران به عربستان پاکستان را به شدت از تهران خشمگین کرده و ممکن است پاکستان به درگیری عربستان و یمن کشیده شود
@WarRoom</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/18876" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سقوط بقایای موشک در اسرائیل  @WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/18875" target="_blank">📅 17:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18874">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حمله جدید اسرائیل به جنوب لبنان
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/18874" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18873">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دو انفجار سنگین بندر عباس
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/18873" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18872">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9kTc_kR68FLVIX9Id5c4xH-OJV_moKeznyRpc5OBPl9N4upSFiMp-sfAnwRREKJKNh7DV9xm8Q9RPAj7zmaaQuWGDEXDRwOBy04c76DtPmijBb1t1w7hTAe9Lpx-5HrpamgsZhvlLgKTjREYsnQxMKlRyQe-NatSX1RmZfyBkEst6oQ_E6JUEMEljlk_WNLNsepHiv7bnFjC9-eXMwTYismqcR0lwjIsNGxCkVKkx6ffwMilCxLV4SgdTm6rsaQaur-BsgANwKVZPyi57IWBFHnRrDQXwdL8iDj9eXDcpIs1NpdhmaSwL3ErBVMu3MTiS8Rf4xmxFjCX8H-mT-jaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : وصله‌کاری موشکی؛ نشانه‌های فرسودگی و کمبود در زرادخانه جمهوری اسلامی؛ کفگیر سدمجید به ته دیگ خورده است؟
‏تصاویر منتشرشده از یک موشک و پرتابگر غیرمتعارف، نشانه‌هایی از فشار بر زنجیره تولید موشکی جمهوری اسلامی را آشکار می‌کند. بوستری بدون رنگ‌آمیزی و با ظاهری متفاوت دیده می‌شود که به نظر می‌رسد با کلاهک یا بخش فوقانی موشکی از نمونه‌ای دیگر مونتاژ شده باشد. پرتابگر نیز ساختاری ساده، کارگاهی و به‌مراتب ابتدایی‌تر از لانچرهای استاندارد دارد.
‏
این ترکیب نامتعارف می‌تواند نشانه استفاده اضطراری از قطعات موجود، کمبود بوستر و لانچر، یا مونتاژ ترکیبی برای حفظ توان پرتاب باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/18872" target="_blank">📅 16:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18871">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPete Hegseth🇺🇲</strong></div>
<div class="tg-text">آبادان صدای یدونه انفجار اومد
خونه ها لرزید</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/18871" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18870">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش صدای انفجار آبادان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/18870" target="_blank">📅 16:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18869">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bql1IpMLlK0iVp7fWHmbs-1HBPkOtQEbGWzuxao9wWK3W0I0rpBZPivYoF-n5_SWZzREiaCDqKG2x-lMQUCN6-g85o1KUZBCvlgso2r4EY9m-A1zWbMvGpzWTGHDUL6oBpTVbaKKIHUueEn3n11qqZQXt8LTXWwGFob92eTN_GbahAoiK-0vouVHpgqJSQW2zskN4SfeVH5C3iTJuXOlAbibp4t0_M0HzlHB4UFhTZJ2tFyy4AZNHFZPzCRHXLEmIiDjoEmTXBpxX91CcqHfxa_jjYNXFDd-AL6V-JNsyL_pPvvoN0ZbQQTazYfV_lWGrDlCXeZOxEW4ptt70FYoDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشات میگن ، فرندلی فایر شده ، پدافند خودشون  موشک خودشون رو زده یا موشک خودش ترکیده
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/18869" target="_blank">📅 16:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18868">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چند فروند بمب‌افکن رادارگریز B-2 آمریکا تو روزهای اخیر در حال جابه‌جایی دیده شدن و به نظر میرسه دارن برای مأموریت‌های احتمالی علیه ایران آماده میشن.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/18868" target="_blank">📅 16:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18867">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚠️
کرمانشاه صدای‌ انفجار نیست پرتاب موشکه
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/18867" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18866">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پرتاب موشک از کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/18866" target="_blank">📅 16:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18865">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">طبق گزارش ها،اسرائیل ممکن است در 24 تا 48 ساعت آینده،ارتباطات رادیویی خود را به دلیل تنش قریب‌الوقوع با ایران قطع کند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/18865" target="_blank">📅 16:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18864">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شبکه ۱۳ اسرائیل: تخلیه هواپیماهای سوخت‌رسان آمریکایی از فرودگاه رامون پس از هدف قرار گرفتن عقبه اردن
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18864" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18863">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هم اکنون 14 هواپیمای سوخت رسان آمریکایی از اروپا به سمت اسرائیل اعزام شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18863" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18862">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رادیو ارتش اسرائیل:
سیستم‌های دفاعی آمریکایی دو موشک ایرانی را در منطقه العقبه رهگیری کردند
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/18862" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18861">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlwTnEzZqxA2HmpSK4A5Q19AaCP5yIk-NaQez3cWg1fd8iJvSWgHYaXekai5fVFDWOAJiXgE2MmxEo8lrcKBuboeKRfyyufsyA6L95OjG7cedmE1uLKoGcCJuD0wMZ4bPjPP5nRftvy08pumO6PGkG4jDL8mR3Lmq4REtnawrBiDiwOCkW3BBPEanXkIBpyrMzPmT1uzMWpARl4DvYBkUxmV27Q1FP9yZppFY26Kwm8dChOMIFaylgw3nAhLT4b0FOrn4PSYmP6hvexq9jKQvHu4BelaVzrbe1m7ZbQRAhub4AXRoJR8lUovh6NCFIfE5TBYHaeSn0c9-dABfId0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی در انبار گرانول مراغه… @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18861" target="_blank">📅 16:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18860">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIXqywgwM0VrISncvwWWVFI0jkNPABoCNhh_6T4doqwEJr0jFxLaMuD29jPnXXXr4yRyEUdHuC24RTBNzGdpg0IBgVRLjE7MvlMLrGM6E4vakF2gVARMbNasmyVvOxaaJU__IR3ErJuCCYerQehWZd61toGKyuwklYrmK1B9zjkktg4Wx-g0ahuwUXNBqvDoVDQki6FAxZD5-rPSUi_H1Tc3Crk-oeqX6dTGfF2BpKNLR1BkEsIuNUVbpGWTuRLdwMZWYOajcJbb4VvEF16w1pnx_ng26xEhwoIv9WhQKhKdJ9YV0i7z_IHMAELuL_I-uPzPTfObDbZJCGRONs7GhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از کوهدشت ، لرستان
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18860" target="_blank">📅 16:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18859">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e80cb396.mp4?token=Sru_V9I4OgecwZRC5zlDyS0FGIfvOmEySjpPQGb_ZHJLXJUE7rr84U92acGjQIX6k53ilZH1Wnh1UjmoM4TQaDZrZg094dt5obkTkmH41nMd9jeh65nYc4qqhIqmdN9UYvMBf7pO6MLilS2ouB2FXDqLuDddH5oGkLarawW3yn4T-DKOofVOKqpFxNQOz14Mw-b_B21VWlIOJbUSDenM_njuV-ysI-CGltnAf3Hby7nn5iSlah41r-Nc4zToJx044hupCgIn70lbHDEWLVRLXvB2-ejpkIKrWrL7VYwkTBKf2mexqOlwlB3bNqcCbJNqIpm4plTYaeAMSdNQ9KP5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e80cb396.mp4?token=Sru_V9I4OgecwZRC5zlDyS0FGIfvOmEySjpPQGb_ZHJLXJUE7rr84U92acGjQIX6k53ilZH1Wnh1UjmoM4TQaDZrZg094dt5obkTkmH41nMd9jeh65nYc4qqhIqmdN9UYvMBf7pO6MLilS2ouB2FXDqLuDddH5oGkLarawW3yn4T-DKOofVOKqpFxNQOz14Mw-b_B21VWlIOJbUSDenM_njuV-ysI-CGltnAf3Hby7nn5iSlah41r-Nc4zToJx044hupCgIn70lbHDEWLVRLXvB2-ejpkIKrWrL7VYwkTBKf2mexqOlwlB3bNqcCbJNqIpm4plTYaeAMSdNQ9KP5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط بقایای موشک در اسرائیل
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18859" target="_blank">📅 16:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18858">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqjMPHWaVem3NZXL3Mn2h0WY_jkxM0HYobZjJcgasg653QvZFLuxIqOvzP0lQaIln5VS_Ilr1pQFHr12WDuJ38T5qTV8ytcJwt2HrsXg1xoa0r-Mgw-V37G44U1yjfNl9k5HWilUydc-GZ7R5imaj5v3a6YIFNvOVuaIK0i6GHzEdtvBMYUq2LiKzSZcl4wVAkINIo7JKa2XuITxb6_r-Jp0UmKqtfpYgjozqb1x12nbvb2SjSV2JcpMhsu1o1crYaMU-WgPILbBRsdbruq2qF4isAk1E7iRuued3FG4BYEtmpWEhgHroTzVoqwdO7jipsS7poSguajRSmoAvbfF_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از ایلام ، لرستان
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18858" target="_blank">📅 15:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18857">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ارتش اسرائیل: چند لحظه پیش، ارتش اسرائیل پرتاب موشک‌هایی را از ایران به سمت شهر عقبه در اردن، که مجاور اسرائیل است، شناسایی کرد.
احتمال وجود دارد که در نتیجه این حملات، خساراتی به اراضی اسرائیل نیز وارد شود.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18857" target="_blank">📅 15:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18856">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آکسیوس: آماده‌باش هوایی آمریکا برای تشدید جنگ با ایران آغاز شده است
آمریکا تعداد سوخت‌رسان‌های خود را به سطح مشابه آغاز جنگ خواهد رساند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18856" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18855">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj_8nQ1X9Zgjw2IYHDdJwD3tXaPglg-ETafPlRqphp7wH4gX7IIMvKqbcYNNbyVQ7Ib8khwsI91uX3zMaAQkmrNDZN6OjqHAzdX131i_IKpVsA03Vri3JYrL9OrBabrc6gmRHx4hcteYBFfrDNu199GFrCSEKSTWU9iSVusjX1UGWYU01jv11JVTp2sAY7BHT6zSgxiNL7pgl35BA_-qPsj0cNqWqPBQrRRsbiZwYdi1oYYqZ7DvOYz7NhROPysWd1FCJ4zGiVqK4wgbVbBXVsnaWOxG-E18Ce_5bAcUBQu8jvshS9RzR3e2-ubdzJ7enlvpYkk61Ubeo21sw8C95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این کاری بود که لیندسی می‌خواست انجام دهد و قرار بود اتفاق بیفتد. مهم!!!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18855" target="_blank">📅 15:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18854">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770115730a.mp4?token=lBMui_ajFdPNGjrRZt4WNFt7rsLfNQH_gBpgZf6wKPeHD4hSREoXKcD6DS48p5oeF-2iXKgMNAAiXb2eJRoFZehODj3xbwfoTbA5_xk1v8fa0N3Qb7xiHAaYJs-0pEt6a4FYg0coQOOZlE17cVY1AYKJDIqgIuKzOVem_IFnaMjS1CdL7QVUA3nIsZ8ZETtCtbupKK1VKaoW6aDv2-tve3D4ZyyYSWGR8uz7Wws7yKQXBXw8hyZTgT9DHbAsJKeyVO9vUUbLAPA6OjPOURz0RSimtwP7932YLrLFLkU0HGij89hsEYYEBpkvH8_giv300V0V0LKarEOSZNdkY1zJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770115730a.mp4?token=lBMui_ajFdPNGjrRZt4WNFt7rsLfNQH_gBpgZf6wKPeHD4hSREoXKcD6DS48p5oeF-2iXKgMNAAiXb2eJRoFZehODj3xbwfoTbA5_xk1v8fa0N3Qb7xiHAaYJs-0pEt6a4FYg0coQOOZlE17cVY1AYKJDIqgIuKzOVem_IFnaMjS1CdL7QVUA3nIsZ8ZETtCtbupKK1VKaoW6aDv2-tve3D4ZyyYSWGR8uz7Wws7yKQXBXw8hyZTgT9DHbAsJKeyVO9vUUbLAPA6OjPOURz0RSimtwP7932YLrLFLkU0HGij89hsEYYEBpkvH8_giv300V0V0LKarEOSZNdkY1zJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی
در
انبار گرانول مراغه
…
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18854" target="_blank">📅 15:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18853">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USjGU0PQVAxZyXuNWAsKG0_7drT21x19hMFyPg5QJAPqwvUL6-0-PZ9BilCzHw1LrNjjdXpURNfTpb_p-bnyLytRTfz5rCMcXdqpjIAL3D0SIqnnZe0qnQ9mxJpjBbxsgTNIs7wYxH2_-6F_ajVv2LQZd81tZiJvFX3fOkR4qwiIa_Ay97FXWKIfv2kioGzmZ6_fC0QHDA5fsRWV2Szf8neRFGbmwnl0DO6yuVi-IljJ3TQSHjFxx_cHFJazbBKk9aNyWHxh6bIUGk267a9yYPzhhfdHUlklNBrvFM7-v5gNnoFIAOusQu3CPbI6sgFOOcQS1XxjvIL7YSDkrET_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهروند ایرانی/آمریکایی ممنوع خروج شده که ترامپ اداعی آزادی و رژیم تکذیب کرد با نام دنا کراری بعد از 566 روز به آمریکا رسید
کراری، ۵۳ ساله ساکن کالیفرنیا، برای دیدار با خانواده به شیراز سفر کرده بود که گذرنامه‌اش توسط مقامات جمهوری اسلامی ضبط و از امکان خروج از کشور محروم شد. به گفته وکیلش، او هرگز رسماً زندانی نشد، اما تحت بازجویی‌های شدید و مکرر توسط سازمان‌های امنیتی قرار گرفت و در چند ماه گذشته تحت شرایط بسیار محدودکننده‌ای قرار گرفت.مقامات امنیتی کراری را به «همکاری با یک کشور متخاصم» و «جاسوسی» متهم کرده‌بودند
وی به عنوان کارمند در شرکت امنیت سایبری پالو آلتو نتورکز کار می‌کرد. او در کنار حرفه فنی خود، بنیانگذار یک سازمان خیریه حمایت از کودکان محروم بنام فرزندان مهر را نیز مدیریت می‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18853" target="_blank">📅 15:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18852">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYDLsaCecx3G6eh70xzeUR5NKUY-foj8hdKsvY8hgzW985bpkUQAzmV5nFkMXsJyUGgxO2B7NivcJL5i5VDmUo_iC88FRyDMk7jsv9UxMttSvS7VGWIumLIfEuAsICJPr1yHMtFd9BErMiAGsUwh92fhZzUCuk70gceVHPwRBZxviWihd5igtcpKcTKMDmBBousMWrX9ShKmk9ABP8-C8nXNBbM6MJ-G2yUU24yEeWO53HtvLJrtpLamdWLRCnB8DOSxE9sl9fW5QB32phCY4L3Z1QOYQ88Z-ckOI3ieCgsIk7yLPovNuRv5Eb74AG5OulvApLEX7Z-ErfBZOVUO9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه هسته‌ای شهر دارخوین با نام های(کارون یا استقلال) در استان خوزستان، در ساحل رود کارون و حدود ۷۰ کیلومتری جنوب اهواز، در زمینی حدود
۵۰ هکتار
در حال ساخت است. این نیروگاه یک راکتور آب سبک تحت فشار (PWR) با ظرفیت حدود
۳۰۰ مگاوات
دارد که طراحی آن توسط متخصصان ایرانی انجام شده و ساخت آن توسط
شرکت
انرژی اتمی ایران
با مشارکت
گروه مپنا
و شرکت‌های داخلی دنبال می‌شود. عملیات اجرایی آن از
آذر ۱۴۰۱
آغاز شده، هزینه پروژه حدود
۲ میلیارد دلار
برآورد می‌شود و طبق برنامه قرار بود طی
۸ سال
حدود
سال ۲۰۳۰
تکمیل شود. این سایت زمان شاه نیز قرار بود میزبان دو راکتور ساخت شرکت فرانسوی
Framatome
باشد، اما آن طرح متوقف شد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18852" target="_blank">📅 14:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18851">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سازمان انرژی اتمی ایران: ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18851" target="_blank">📅 14:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18850">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سازمان انرژی اتمی ایران: ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18850" target="_blank">📅 14:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18849">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مجری : دست فرمون شما ما رو رسوند به جنگ  خلاصه گفتگو با سید عباس عراقچی  @WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18849" target="_blank">📅 13:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18848">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیروی دریایی سپاه: ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه، قصد ایجاد اختلال در تردد و خروج از تنگه هرمز از طریق یک مسیر ناامن را داشتند. دو فروند از این کشتی‌ها دچار حادثه شده و متوقف شدند، در حالی که دو فروند دیگر از ادامه مسیر منصرف شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18848" target="_blank">📅 13:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18847">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اختلال در اینستاگرام / واتس آپ ، به گیرنده های خود دست نزنید مشکل از مرکز است
@WarRoom
⚠️
⚠️</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18847" target="_blank">📅 12:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش‌ تایید نشده ، 4 کشتی در بندر شهید رجایی، هدف حمله قرار گرفتن @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18846" target="_blank">📅 12:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18845">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش انفجار در اربیل عراق ، مقر کردها
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18845" target="_blank">📅 11:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18844">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش‌ تایید نشده ، 4 کشتی در بندر شهید رجایی، هدف حمله قرار گرفتن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18844" target="_blank">📅 11:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18843">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آلارم حمله موشکی در ‌بحرین فعال شد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18843" target="_blank">📅 11:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18842">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادعای اسرائیل هیوم:مجتبی خامنه‌ای از ایران متواری شده  @WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18842" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18841">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ادعای اسرائیل هیوم:مجتبی خامنه‌ای از ایران متواری شده
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18841" target="_blank">📅 11:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18840">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک‌تایمز:دولت ترامپ نگران است که افراط در استفاده از تحریم‌ها علیه روسیه، کشورهای بیشتری را به روی گرداندن از دلار آمریکا ترغیب کند؛ در نتیجه اقدام به کاهش برخی از تحریم‌ها علیه مسکو کرده
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18840" target="_blank">📅 11:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18839">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0163277b0.mp4?token=oHaTdD6c6Z2hF1mAh89NfRaSisn81PfTmHJf14o2Xr9y7Xt9YgEqUhaI2enO6URA8PUH8V4K9zTEszGBZT7As6r20cc_sDDWGNVtB_7RW_U4-N42Z0kXG76f3aVtKTb2mKPuuaa7krfg9m3gMYOZh1a16dxh0v5hB3-G7nPTNe-Y0njee3JwTWzOvyD0ntci0XjJQ-Cfn0jkzZDEPtkf5dMC60GbJalMYGzmrV0FK2oCl3XKIqKjCOuTB7MeFStDOT7cojaYhCDTmhbPdqH0y4_xzFGqwtAnIMDSErEdlUETQKK0zHrXGKkBi_5EDtagAiQ8reMjhJJ0L2FKKTtbdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0163277b0.mp4?token=oHaTdD6c6Z2hF1mAh89NfRaSisn81PfTmHJf14o2Xr9y7Xt9YgEqUhaI2enO6URA8PUH8V4K9zTEszGBZT7As6r20cc_sDDWGNVtB_7RW_U4-N42Z0kXG76f3aVtKTb2mKPuuaa7krfg9m3gMYOZh1a16dxh0v5hB3-G7nPTNe-Y0njee3JwTWzOvyD0ntci0XjJQ-Cfn0jkzZDEPtkf5dMC60GbJalMYGzmrV0FK2oCl3XKIqKjCOuTB7MeFStDOT7cojaYhCDTmhbPdqH0y4_xzFGqwtAnIMDSErEdlUETQKK0zHrXGKkBi_5EDtagAiQ8reMjhJJ0L2FKKTtbdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رسانه‌ی فرانسوی با انتشار این ویدیو نوشت:
‏زنان ایرانی در نزدیکی بندرعباس در جنوب ایران گرد هم آمده‌اند تا خبر حملات هوایی جدید علیه رژیم اسلامی را جشن بگیرند.
‏آن‌ها پیام زیر را خطاب به آمریکا فریاد می‌زنند:
‏«ادامه بده. کارِت عالیه»
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18839" target="_blank">📅 11:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18838">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e681b632df.mp4?token=f3ylE0cqo6MgyV9UkXFb65eqGP4a-72SCjdtCcyQpm9p-d7BYbTl9naiDfGbVn9flLAfC7NIwSFhw-tiE5g3YXNHUZ64dnlVvqNot7XaQEUwqye6yCN4DyF6MjAc6rZVeGSWALJ9xdNoTYqLTE49DasKiDYB61TjNMAgAeLmk2q1BjkI88BOzuYLrdjsBbpkMVvjNHCQQPUfDV1y04_CZwsW80DS1-Kc29RQCEbLXf3Qe78y5KxJcFT6_1qRHd_AGSHAXXKIw6WkAjX3zLgx3j8c8bkpbO6DoKlQI93pl-oMD-wp6IcGjoptsePIdM-9elLCbLJS6KVPvLj3BO903RmSujjOWV4t-FwWamP1iok8HIgSYmdISkcodYgRw5xodGGczQZK36rycCjLAVbYALvmjOrfqMa2KZf-ewWf8oSHewBaP-aFnYJrsSUBmw0176bwlrXk94Tb0CbEx2LViPDpMcRr4Q_OtvZYD6O8Vw6_r4n6Csx8XGZDqf80lI6GH8hpyyXPWQEmxextbC0LXLjd3R6HB5A-OZ7-p97M-nW7c8ySgl85GZkJGWnLLQcu7sxFJUCVzr0R74F-5JNqcugzSa7t20oiPrxa39n58kLtJHziasAwCYS86leu03Nur5wh2OUqgAQOl62w9pYhatGngt4IbvuIGpEd2EJ2CpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e681b632df.mp4?token=f3ylE0cqo6MgyV9UkXFb65eqGP4a-72SCjdtCcyQpm9p-d7BYbTl9naiDfGbVn9flLAfC7NIwSFhw-tiE5g3YXNHUZ64dnlVvqNot7XaQEUwqye6yCN4DyF6MjAc6rZVeGSWALJ9xdNoTYqLTE49DasKiDYB61TjNMAgAeLmk2q1BjkI88BOzuYLrdjsBbpkMVvjNHCQQPUfDV1y04_CZwsW80DS1-Kc29RQCEbLXf3Qe78y5KxJcFT6_1qRHd_AGSHAXXKIw6WkAjX3zLgx3j8c8bkpbO6DoKlQI93pl-oMD-wp6IcGjoptsePIdM-9elLCbLJS6KVPvLj3BO903RmSujjOWV4t-FwWamP1iok8HIgSYmdISkcodYgRw5xodGGczQZK36rycCjLAVbYALvmjOrfqMa2KZf-ewWf8oSHewBaP-aFnYJrsSUBmw0176bwlrXk94Tb0CbEx2LViPDpMcRr4Q_OtvZYD6O8Vw6_r4n6Csx8XGZDqf80lI6GH8hpyyXPWQEmxextbC0LXLjd3R6HB5A-OZ7-p97M-nW7c8ySgl85GZkJGWnLLQcu7sxFJUCVzr0R74F-5JNqcugzSa7t20oiPrxa39n58kLtJHziasAwCYS86leu03Nur5wh2OUqgAQOl62w9pYhatGngt4IbvuIGpEd2EJ2CpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : دست فرمون شما ما رو رسوند به جنگ
خلاصه گفتگو با سید عباس عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18838" target="_blank">📅 11:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18837">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فرماندار چابهار گفت: صدای انفجار شنیده‌شده امروز، ۲۸ تیرماه، در حوالی این شهر مربوط به عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده و هیچ خطری شهروندان را تهدید نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18837" target="_blank">📅 10:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18836">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏ارتش جمهوری اسلامی با صدور بیانیه‌ای، مدعی حملات تازه به دو پایگاه نیروهای آمریکایی در کویت شد.
‏در این بیانیه آمده که ارتش جمهوری اسلامی در پی «حمله به پل‌ها، زیرساخت‌ها و مناطق غیر نظامی»، انبار مهمات ارتش آمریکا در اردوگاه العدیری و رادار پاتریوت و رادار هوایی این ارتش در پایگاه علی‌السالم کویت را، آماج حملات پهپاد‌های خود قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18836" target="_blank">📅 10:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18835">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیویورک پست از قول دونالد ترامپ: کشته شدن دو سرباز آمریکایی مایه تاسف است، اما ماموریت نظامی همچنان ضروری است
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18835" target="_blank">📅 10:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18834">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: اگر تهران متوقف نشود، منطقه ممکن است وارد یک درگیری گسترده‌تر شود
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18834" target="_blank">📅 09:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18833">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وال استریت ژورنال: بر اساس اظهارات افراد مطلع، در حمله ۱۷ ژوئیه ایران به پایگاه هوایی موفق السلطی، علاوه بر موارد دیگر، هواپیماها و پهپادها نیز آسیب دیدند
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18833" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18832">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Iz1-x8dAYFGCCDlBWYnpTWx2LZjRdev5uYXLB7cL5BfRq16gB613FOwkuI9cXHhAygWCx0NMApt6Hx4cJO9RguN71gyFkjFjBY8hDmNSzpgN-6ocvmrqb1ZfHtqayUV7vVAWEluR4xbY_pt3-BDrv3BEfMWHo3prMGDE_3OyALwLouQdJ2jDtVPLcXfcOyF44A2JHWmwr50CMAPlEhmC1Yzz-KsMsQg-RtJtIfQmm_ROEtkhgb5zPOpHJQNJoUiDrLMAlECwOPr4dm2UWgfsLsjpn0XqOtX8IJ-OqlsNwwBWPJn-qVtoyHujJIfpIjuHDUdBYBNDCabMCpxBvCHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله در دزفول و اهواز @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18832" target="_blank">📅 08:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18831">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">معاون امنیتی ‌استانداری خوزستان:
جنگنده‌های‌ آمریکا ساعت ۰۵:۵۵ دقیقه نقاطی در اطراف شادگان را مورد اصابت موشک قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18831" target="_blank">📅 08:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18830">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سایت موشکی خمین ,کوه انگشت لیس , بین خمین و گلپایگان @WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18830" target="_blank">📅 08:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18829">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">زلزله در دزفول و اهواز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18829" target="_blank">📅 08:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18828">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95514648b.mp4?token=NC-z4i61X0GebNF9dogSrqobPAgtcaKE_i1-ZJL0hCGCBz_lVnpuG1YGauFzX3cfHYp4wlCAFRa-gVJ_M_yzs-AWySkdVhaMhOzPWKPHRGgGgTOi6xP278r6g0tP1hBZSg3Q2cfx4_5M_ZchYf5AsqUBHdgxeNPn27NP4-wzMBEg517gLE4RMerXZIa_IT0JaNDrBvGPZ2FTzmNNW5zdfLV8tiM1W9_1kwJrLK2KCP2Gj6RqBQoFonDWEkKgwJ0IbCkujre3L06kym82lfaFRwKV_KFAdXESKkY16zAPI1jyL9zFWGCx6_Yh3s_RzoN5DXfW1bupE5J92Epke5HcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95514648b.mp4?token=NC-z4i61X0GebNF9dogSrqobPAgtcaKE_i1-ZJL0hCGCBz_lVnpuG1YGauFzX3cfHYp4wlCAFRa-gVJ_M_yzs-AWySkdVhaMhOzPWKPHRGgGgTOi6xP278r6g0tP1hBZSg3Q2cfx4_5M_ZchYf5AsqUBHdgxeNPn27NP4-wzMBEg517gLE4RMerXZIa_IT0JaNDrBvGPZ2FTzmNNW5zdfLV8tiM1W9_1kwJrLK2KCP2Gj6RqBQoFonDWEkKgwJ0IbCkujre3L06kym82lfaFRwKV_KFAdXESKkY16zAPI1jyL9zFWGCx6_Yh3s_RzoN5DXfW1bupE5J92Epke5HcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام :شب هشتم تمام شد
ما
دور تازه حملات علیه ایران
در
۱۸ ژوئیه، ساعت ۱۱:۳۰ شب به وقت شرق آمریکا (ET) (۰۷:۰۰ صبح ۱۹ ژوئیه به وقت تهران)
و
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)
به پایان رساندیم.
به گفته سنتکام، در
هشتمین شب متوالی
حملات آمریکا، نیروهای این فرماندهی
تأسیسات دیده‌بانی ساحلی و پدافند هوایی، توانمندی‌های دریایی، و انبارهای موشک و پهپاد ایران
را با موفقیت هدف قرار دادند تا توانمندی‌های نظامی ایران بیش از پیش تضعیف شود. همچنین نیروهای آمریکایی،
عناصر سپاه پاسداران
را که به گفته آمریکا در
۱۷ ژوئیه (۲۶ تیر)
در حملات علیه نیروهای آمریکایی در اردن مشارکت داشتند، هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/18828" target="_blank">📅 08:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18827">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09cf3dc329.mp4?token=vtZT_MwuvFHUYoPuCpJ-tEXR532Dhizl4Sv_A3-lnoVqdniRJPKyge-RWTTyfTj1kV_u1VlkGb-WrKMG6gRQpf4L-GoBiNHE3VDPD3tZQ-zzr4aNTcm17TdWIYA7USJLj5IZ1gPROogdcIgf-EeEOlG4Y_f4hMgvBk04PUJ_OER3Yd38UMwrk4Hq2U6tNIrqYVUrBq4bxrx_pJLyfu6ad4JjKBumVZ2DU61THsGlWdt4c9rd4abyOLXPTLdwX4cF_6HxCeGfzaLWfjz1pl5dY_iaYqs6txNkbgLm9w3zVjw11AQsRr1BNZSOEE7sB-vTuEX3wqwnbF8d8tBRamgoYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09cf3dc329.mp4?token=vtZT_MwuvFHUYoPuCpJ-tEXR532Dhizl4Sv_A3-lnoVqdniRJPKyge-RWTTyfTj1kV_u1VlkGb-WrKMG6gRQpf4L-GoBiNHE3VDPD3tZQ-zzr4aNTcm17TdWIYA7USJLj5IZ1gPROogdcIgf-EeEOlG4Y_f4hMgvBk04PUJ_OER3Yd38UMwrk4Hq2U6tNIrqYVUrBq4bxrx_pJLyfu6ad4JjKBumVZ2DU61THsGlWdt4c9rd4abyOLXPTLdwX4cF_6HxCeGfzaLWfjz1pl5dY_iaYqs6txNkbgLm9w3zVjw11AQsRr1BNZSOEE7sB-vTuEX3wqwnbF8d8tBRamgoYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش انفجار  در قشم
@WarRoo
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18827" target="_blank">📅 05:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18826">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سکوت عجیبیه</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/18826" target="_blank">📅 03:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18825">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سنتکام: امروز ساعت 6 عصر به وقت شرق آمریکا، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی رو علیه ایران آغاز کردن. هدف این حملات، تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب…</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/18825" target="_blank">📅 03:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18824">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جزیره لارک سایت سپاه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/18824" target="_blank">📅 03:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18823">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجار‌سایت موشکی حاجی اباد، هرمزگان  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/18823" target="_blank">📅 02:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18822">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDwNeSXT5yTnPgMzjk8RcLbUWCa5hYl_7lcmQsiEMurPNJwCQUYYbCYc2I4Y6hiV04f0Fs8EwG_jCPhTdGoNI3ztYpl2DUaS6glQ8e-4bmR4ho6X7j5SHXw_MFNbalUN4okx23FOgICY22GENTa8sLq8xk8FovVVBGuNizNNx6lCJ74mxwulKmOkXHmHgGOmkHV1ENQh1CE5AEEXyHihmzxnlnf2W8zzRiTNFgyj1GToJJWe9zzrwkcoCE19_s04OAB_fhcV_w7qzhEwlCbNtQGVkFgTtgrg5JvacHvBJZWucWKqE1JIYtGxKsmxt81iKPxxZUYY6KocVz8zW5z4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار جان الان امدم بالا پشت بوم جنوب تهران ستون دود بلند شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/withyashar/18822" target="_blank">📅 02:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18821">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از مدتها نمیتونم ببینیم چیزی
🤒
همه رفتن زیر پتو رررپتپتوووو  @WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18821" target="_blank">📅 02:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18820">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک صدایی شبیه به انفجار در کوه دراک شیراز که شهر موشکی هست شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/18820" target="_blank">📅 02:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18819">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجار‌سایت موشکی حاجی اباد، هرمزگان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/18819" target="_blank">📅 02:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18818">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش انفجار خرم آباد لرستان
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/18818" target="_blank">📅 02:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18817">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/18817" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هیچ گزارشی از‌ بندر عباس نیست !
🚨
🚨</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/18816" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18815">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش انفجار در بوشهر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18815" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18814">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش‌ انفجار در اراک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18814" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18812">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18812" target="_blank">📅 02:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18811">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/18811" target="_blank">📅 02:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18810">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/18810" target="_blank">📅 02:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18809">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/18809" target="_blank">📅 02:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18808">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش حمله با موشک های کروز تاماهاک (که خامنه ای‌رو کشت ) توسط ناو های آمریکایی‌به ایران
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/18808" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18806">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مسیر جاسک (بیاهی) از طرف دریا  ۳۰ جنگنده اومد
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/18806" target="_blank">📅 02:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18805">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حقیقت یاب اناق جنگ : همانجور که اعلام نکردم سیریک خبری نیست فقط نیم ساعت پیش صدا جنگنده اومد اما انفجاری چیزی رخ نداد فیک نیوزه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18805" target="_blank">📅 02:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18804">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۲ انفجار بندر لنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18804" target="_blank">📅 02:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18803">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جنگنده های آمریکایی بر‌فراز ‌کیش
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18803" target="_blank">📅 02:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18802">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش انفجار‌اهواز
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18802" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18801">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18801" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18799">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال ۱۴ : کنسولگری آمریکا در اربیل کردستان عراق در حال حاضر مورد حمله شبه‌نظامیان تحت حمایت ایران قرار گرفته است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/18799" target="_blank">📅 02:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18798">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDuexkjXapcc37QM5WDhVl_pnSf0ERkSbcOfo0A_gvNJOHpIs6qRRswuKxnvVp-DMvZn7CVFgGb75GqDPOZT-w7cwkt-IR6HPZuuTdzXi29dGQBwqLvvBrgO-NMUs_5VYUREs3vNUQOuPi0Wjc5E9AW41tcp8qqryf_WbpZGSvcuLMwFPxTcU6TlcTdxcmnVmkv-Hr-4RXghNdXsFt_syiNbDV1x8QSuF-49nN-JqzXpn4NAHwUyMqfDlV6mYfy9uCZ2KwgkGc59G0JNFtbrxcL_eaqnXxq-Dw7UZaOoPVBW88SiOnoIjJxcZXIejm6Qx9FvZBsYAV8QE0KUQSlEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اربیل عراق کنسولگری‌ آمریکا رو زدن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18798" target="_blank">📅 02:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18797">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18797" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18796">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18796" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18795">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سنتکام: امروز ساعت 6 عصر به وقت شرق آمریکا، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی رو علیه ایران آغاز کردن.
هدف این حملات، تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی است که شب گذشته حملاتی رو علیه نیروهای نظامی آمریکایی در اردن انجام دادن.
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18795" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18794">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سنتکام آغاز حملات را اعلام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/18794" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18793">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سنتکام آغاز حملات را اعلام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/18793" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18792">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وال استریت ژورنال: جنگنده های F35 ارتش آمریکا از بریتانیا به سمت خاورمیانه اعزام شدند
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/18792" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18791">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/18791" target="_blank">📅 00:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18790">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وزارت امور خارجه ایالات متحده آمریکا یک "هشدار جهانی" صادر کرد و هشدار داد که گروه‌هایی که از ایران حمایت می‌کنند، ممکن است به سایر منافع آمریکا در خارج از کشور یا مکان‌هایی که با ایالات متحده و/یا آمریکایی‌ها در سراسر جهان مرتبط هستند، حمله کنند
@WarRoom</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/18790" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18789">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وال‌استریت ژورنال: آمریکا به نقش احتمالی چین یا روسیه در هدف‌گیری‌های ایران مشکوک است
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد که پس از اصابت حملات ایران به چند هدف حساس با دقتی غیرمعمول، احتمال ارائه اطلاعات هدف‌گیری از سوی چین یا روسیه به تهران در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/18789" target="_blank">📅 23:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18788">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یک حادثه دریایی دیگر، سومین مورد در امروز، دقایقی پیش در نزدیکی سواحل عمان رخ داد.
@warroom</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/withyashar/18788" target="_blank">📅 23:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18787">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">طبق گزارشات غیر رسمی دقایقی پیش آمریکا پل سورمیچو که ایرانشهر رو به چابهار متصل میکنه هدف قرار داد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/18787" target="_blank">📅 23:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18786">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">میگم تا حمله شروع نشده، یه لطفی کنین خستگی منم در بره. چیزی نمونده بشم 1.7M یه هول بدین تو گروه چتا بذارین، به دوستاتونم که ندارن بگین اینستاگراممو فالو کنن. نوتیفیکیشنهای پیجم روشن کنین، استوریا رو هم حتما ببینین.
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/withyashar/18786" target="_blank">📅 23:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18785">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مقام آمریکایی به NPR : ترامپ دستور داده تا طی ساعات آینده ارتش آمریکا درهای جهنم رو به روی ایران باز کنن.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/withyashar/18785" target="_blank">📅 23:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18784">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وال استریت ژورنال : مقامات آمریکایی می‌گویند ایران در حال شلیک موشک‌هایی است که با سرعت بسیار بالایی حرکت می‌کنند و می‌توانند هنگام نزدیک شدن به زمین مانور دهند
@WarRoom</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/withyashar/18784" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18783">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : ویدئوی منتسب به پست دونالد ترامپ در اینستاگرام مبنی بر حمله زمینی فیک است و ترامپ از دیروز در اینستاگرام هیچ پست جدیدی قرار نداده.
@WarRoom</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/18783" target="_blank">📅 23:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18782">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NysWC6fYMgz430bE4pNdqerrcPk4bSyaInEB3yHpBNY2fjXHz4hfjINwGFg7C8T2pZJI9p6G_PTF2dQ1_PfiNBT0iO6EuhwRVEECQtW0uhLXbfdKqW_A6rMbunTXFKa-PFp64iMAzM5tXEMzegmJZVISpJ3gLoKcZvK6qAKNFktFVz5MG-2zB4xwORrVpsxdZ5jFyik7QlNoY42Lnqkre4Mk3OeYDoog541_P4oYR0s512jyLZ1tvXGwHcXzd0Yf_tXcNL171_xQiCK-ofsqDv26logWo4shMbjYf67OiJUKuhEmiAZs11LX8_sWaqYNQW1Ap1sLfYawNKqb0AoWLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از مدتها نمیتونم ببینیم چیزی
🤒
همه رفتن زیر پتو رررپتپتوووو
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/18782" target="_blank">📅 22:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18781">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هواپیمای های آمریکایی در منطقه فرستنده های خودشونو خاموش کردن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/18781" target="_blank">📅 22:53 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
