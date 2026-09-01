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
<img src="https://cdn4.telesco.pe/file/b0-U4v9vHM4d-LqL3F-o5sRPXb20BfPDCn0uMueNnyGvrByxwI1BQcJZgui74iJX_A-qcwPhOPHpSg9iNrbm_5B7ZdPwlnzh-FrCSvB4Ua24Xcf8kLjCOOsbFLaRoPEKvu6eqDpc1LvTJflgunhY1KWJslu32SpDUdCOeccjMHaMXRZVwmIbGW1h1OtYOpEo2BIKFNEkjbgb9JbRIQrdYUzu1gtKMylmBxcOZ_BEASrGV2qEfav2AmDRPFDG1u1HNgX69BQnrTCRVq2ldMwv8RkSr3uAOfteAEPPA2MRttBiwXXBzE8MPaw5EzjH7zvA8QKjnB4dA5o77r3syWr-CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-20397">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/20397" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20396">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/20396" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20395">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر راه:
رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/20395" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20394">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دلار فردایی تهران
⏳
213,600 فروش
🔴</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/20394" target="_blank">📅 13:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20392">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏نبویان:   اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/20392" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20391">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏نبویان:
اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/20391" target="_blank">📅 13:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20390">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/20390" target="_blank">📅 13:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20389" target="_blank">📅 12:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20388">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
آمریکا در جهت ضربه به تمام فرماندهان سپاه آماده می شود ! عملیات روانی همزمان با برنامه جدی برای ترور !
⏺
در لیست تهیه شده توسط دپارتمان جنگ ایالات متحده، فرماندهان بسیاری از نیروی زمینی سپاه، قرارگاه های این نیروی و حتی فرماندهان سپاه های استانی و فرماندهان…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20388" target="_blank">📅 11:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20387">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⚔Iranian Militarism⚔</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssZqkTP10cx4kyUqPRsiqqm88ZbIS-R1cZQdF-8_G50dLPFi4NhePCOGP0J735yuIWVMBZBfm9qU2h7SwJ0-kfyeFQo9u3lGD-mcuMAZp10R6TXFiNv4ynqHq_x_g-4cVjPSFdmfcBB5kPdg3tOhRgYa_8GFFzQ9UnY1pthEVrCLWB60VLUsmtrmQ8oVeKjErK9o-cobKW0fwQjf_3jVXLYljQUexEeEQK7Rb256lgItyr6dyolZYJIjokoKlwVFEwKQHza2RgSaRZfV6stz-cc0vRGBT_JJqZkexCLwhOXHt5QwWWp-fDwR8BbDCa7bCI-DUJa_conH1LmroVvEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آمریکا در جهت ضربه به تمام فرماندهان سپاه آماده می شود ! عملیات روانی همزمان با برنامه جدی برای ترور !
⏺
در لیست تهیه شده توسط دپارتمان جنگ ایالات متحده، فرماندهان بسیاری از نیروی زمینی سپاه، قرارگاه های این نیروی و حتی فرماندهان سپاه های استانی و فرماندهان نیروی دریایی دیده می شود! حتی سرپرست فعلی سازمان اطلاعات سپاه نیز در این لیست می باشد.
⏺
هدف آمریکا از تهیه این لیست اجرای یک عملیات روانی و همچنین دریافت اطلاعات دقیق از وضعیت این فرماندهان می باشد. همچنین به نظر می رسد آمریکایی ها با انتشار زودهنگام و غیر دقیق این لیست عجله در دریافت اطلاعات دارند .
⏺
گزارشی مبنی بر نشر این لیست در مجموعه های خاصی وجود دارد که مرتبط با اعضای نیروهای مسلح هست، نکات بسیاری وجود دارد که فکر میکنم اگر بگویم برای خودم دردسر ایجاد می شود پس فعلا از گفتن آن پرهیز می کنم. اما جدی بگیرید اوضاع را !
Join us |
@Iranian_Militarism</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20387" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20386">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⚔Iranian Militarism⚔</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU2E7Fouphn6nBc19TzChJ4vu1jeUF57tU7KFA2h3qa3uQWtEEGktg4jbrWAC70cKAQK4S-PUAhLWfa-Q40jTDWqJr3tk9aO4e58rseAirYgP52XLIqE1QcsdYiN1vkG2RIisAnrNNYkEN5TZ_lwyJTOJbxBQdxScPuiG4-hPuCDVPoEF74PDO9GU6sgunwWETbsO_gBDkO4Vj-Un4Lv1XpS_3CYYLh-Gw2Drdoym2AJ7SJvkbvBPOL7mLsqQ6pYf2Yydt0L7KJk4LZjzxZrwLFuavp6D_cwtJ8qa7HTveOK6tO6O-JZM1OyJRvu7YlKnSW38y2TMNaj7Z6vd80cYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر سردار حسن زاده در صفحه وزارت جنگ آمریکا به عنوان فرد ترور شده !
🚫
دپارتمان جنگ ایالات متحده سایتی برای دریافت اطلاعات از برخی فرماندهان ارشد سپاه تهیه کرده است! در این سایت لیست قابل مشاهده است که صرفا به چند فرمانده به صورت پراکنده می پردازد، نکته جالب اینجاست روی تصویر شهید خادمی علامت ضربدر قرمز خورده است به این معنی که به شهادت رسیده است! حالا جالب تر اینجاست روی سردار سرتیپ حسن زاده فرمانده سپاه محمد رسول الله تهران نیز همین ضربدر دیده می شود!
Join us |
@Iranian_Militarism</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20386" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-cBiyqkuRSaqsSDbd2gDMPmlMWakZXpl11OpnChPgocCkJ-m6ujXlT03VBwRj3Lzs2pSm55JqZGB19eNZd40Gq11It--N2k3DEAp9S4e9yUa5gyxFrCxe-O03JjZ_PupmydeKaEOUU1KmGFf8I_XTVanv8tHUriQfcbuyaYMYFN5pp3Xbg02MPm46qBLDzIgNd6Ctq1upvHz3KM5MC9MPSpq1v6sUxegLjrFZvQ_6t7-Ni6W9SHGVuYlsb_MZQFECi-so0WTuuQLBQMFGxUfsgIxzbCUcWMuSLaP43RLrVhpirkh5Z5qnBXxK1qfp1JzKtQbu2h5y73XTXf_S2FUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه بالا قرار دارد و بازار رنج و کم نوسان پیش بینی می شود.
با توجه به روند عمومی نزولی در 1-ساعته، فروش در سطوح مقاومتی (4477) بهترین راهبرد است.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20385" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این چیزی که ما اکنون تجربه می کنیم عملاً نوعی «تجربه نزدیک به زندگی» است.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20384" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجار در سیریک</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20383" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ایران یک تانکر نفتی سعودی را در تنگه هرمز متوقف کرد.
بر اساس گزارش خبرگزاری فارس، یک تانکر نفتی بزرگ سعودی در حالی که از مسیر جنوبی تنگه هرمز عبور می‌کرد، متوقف شد.
ظرفیت این تانکر 2 میلیون بشکه نفت است.
طبق این گزارش، در حالی که این کشتی از تنگه عبور می‌کرد، ناگهان سیستم شناسایی خودکار آن فعال شد. فعال شدن ناگهانی سیستم AIS نشان می‌دهد که یا به این کشتی دستور داده شده بود تا موقعیت خود را اعلام کند، یا اینکه در شرایط اضطراری در تلاش برای اعلام حضور خود بوده است.
امروز، سازمان UKMTO گزارش داد که گزارش‌هایی مبنی بر وقوع یک حادثه امنیتی مربوط به یک تانکر نفتی دریافت کرده است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20382" target="_blank">📅 00:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20381" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovrVLRQ9UGa0xGOLaN1BgQnEuxTT4DGm1zsiGTnWzkGEpa8Gk3xklqL8bRDOzjQXbR3-lEq5p1OvDlXXLimq8Ao_FzKBMpN2SxOkrKH7KyUX5il3ON1APH8xIEhpLRzaPJP5m0jQL5JWNshfzGfN_p91cOz9RPnEMGdM5JWDycW5uCtFtMIQXePZhLuWVFgPmSAmeEbg6YWrh8ckZegWQXBhMuAFplVBBV-NpLWibLbfmkmyGxv3b46QfYEMabuZnidfZLlmNXhPjqSC2rZgBxweMspkCVIiG2PnUmoh_tD_VMYTk_n3x4DGCzhE_ICX498d7FEJb_X7gU76Hes5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار رشدهای عالی را در طلا شاهد بودیم.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20380" target="_blank">📅 00:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش های اولیه از حمله موشکی آمریکا به یک نفتکش ایران در اقیانوس هند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20379" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حملهٔ مسلحانهٔ عناصر پژاک به اهالی یک روستا در مریوان کردستان
در جریان این حمله، تعدادی از شهروندان محلی زخمی شدند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20378" target="_blank">📅 00:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20377">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20377" target="_blank">📅 23:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDe8MHjy1vHw6FDb4Rmg7OGJwIFFUZO12hdcnwhOPDRfPRblUZHJitZuSiw8OEZPS9GSW2m-Rhtcx9VPBJHZkiYNkBhgY3gEYxVIhAu4XAcc1t-6RDtwb80eweYNjhCtBhFCSQHQBZHgLYVquizWjoTKdmvrG0EyHiL5W60D4ak_gLCp_dBzLaSfSZqhvFxGtSL1Ycy03Dw2f95LWWQ8aRCpuLTyGY-PV5PZVkskrro_go8iRlz-OctermcZb3tyvtx5fHqV7v8-dtfRM2cdvrnkpe5LuwNx1j0te4x8WDRXGVFsD4Yf9Oz62XgPat8vAzBcvIn4xy1GIbl_7MyNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20376" target="_blank">📅 19:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دادگاه مرکزی کیفری عراق، امیر رحیم جبار لازم، عضو کتیبه‌های حزب‌الله وابسته به ایران، را به دلیل گروگان‌گیری روزنامه‌نگار آمریکایی شلی کیتلسون، بر اساس قانون ضدتروریسم به ۱۵ سال حبس محکوم کرد.
کیتلسون در ۳۱ مارس در بغداد ربوده شد و پس از حدود یک هفته، در ۷ آوریل آزاد شد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20375" target="_blank">📅 19:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسکات بنت:
به دلیل محاصره، تنها 30 میلیون بشکه نفت ایران روی آب باقی مانده است - بنابراین حتی اگر آنها بتوانند از چین پول دریافت کنند، این مقدار تمام خواهد شد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20374" target="_blank">📅 19:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شمار کشته های حمله شب گذشته آمریکا در لارک به ۳ نفر رسید
خبرگزاری تسنیم:
در پی حمله شب گذشته آمریکا به نقطه‌ای در جزیره لارک، ۲ نفر به شهادت رسیدند و چند نفر نیز مجروح شدند. مجروحان این حمله برای مداوا به بیمارستان منتقل شدند که ساعاتی بعد، یکی از آنان نیز بر اثر شدت جراحات به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20373" target="_blank">📅 18:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20372">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«ایران تحریم‌ها را بسیار جدی گرفته است. رهبران ایران از وضعیت اقتصادی کشورشان شوک‌زده شده‌اند.
ما شاهد صف‌های ۳ تا ۴ ساعته در جایگاه‌های سوخت ایران هستیم.
ایران به دلیل از دست دادن توان اقتصادی خود، به اقدامات نظامی روی آورده است.
می‌خواهم از اتحادیه اروپا بابت حمایت آن از عملیات موسوم به «Economic Outcast» تشکر کنم.
خبرنگار: آیا بازه زمانی مشخصی برای فروپاشی اقتصاد ایران وجود دارد؟
بسنت: لازم نیست اقتصاد ایران فروبپاشد؛ فقط کافی است حکومت ایران به خود بیاید.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20372" target="_blank">📅 16:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20371">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سرتیپ ابوالفضل شکارچی، سخنگوی ارشد نیروهای مسلح ایران: صدها نیروی آمریکایی در طول جنگ کشته و هزاران نفر زخمی شدند
➡️
در این جنگ نابرابر، نیروهای مسلح ایران با استفاده از تاکتیک‌های جدید و نامتقارن در مقابل توانایی‌های فوق مدرن آمریکایی و صهیونیستی صف‌آرایی کردند و ضربات سنگینی به دشمن آمریکایی-صهیونیستی وارد کردند.
➡️
به عنوان مثال، هر زمان که یک پهپاد ۴۰ هزار دلاری ایرانی به سمت اهداف آمریکایی یا صهیونیستی پرتاب می‌شد، ارتش آمریکایی-صهیونیستی از چهار موشک به ارزش هر کدام ۴۰ میلیون دلار فقط برای رهگیری آن استفاده می‌کرد که نشان دهنده میزان خسارت مالی وارد شده به دشمنان آمریکایی-صهیونیستی توسط ایران است.
➡️
با وجود این هزینه‌ها برای آنها، پهپادها و موشک‌های بالستیک ایرانی همچنان از لایه‌های دفاعی آمریکایی و صهیونیستی عبور کرده و به اهداف مورد نظر خود در پایگاه‌های آمریکایی و سرزمین‌های اشغالی اصابت می‌کردند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20371" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20370">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ به فاکس‌نیوز:
ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد!
ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20370" target="_blank">📅 16:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20369">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">میگویم اینکه خارج نرفتیم به این می ارزید که موقع برگشتن زیر تیغ «حافظه تاریخی» نرویم!
سبحان الله !</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20369" target="_blank">📅 11:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20368">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geVXf7m6qVNo_0sYtg3GZ3HFbkfkhbTHSV_GF44_8B6Qvmt55ylUVbDEPbi3Qlb9PDKl9wNBqSxGZUxZM-jePV21J15ZjXZeQhafSxUGBq--KuneVaFoF4dOUN6sCIRNUBx0u_RhXD3d6QdR4xdt3HTGuaO0s0bn1udmuKGSKMu0xKHyvCjWadvgVxPlEAIAZkXcongKPQgFFTd75uz3pyR0hA_-yE4lYLBjySRfewbnELGqwz4PHVMYYKot4IzcU03jOpZ07boH0la7hSDulaBAb-mGDFZiZIGbVMdwWRth7WXJT3LTQhpzgmt7kgNkJ9uaHT6otHr_JNUsF07Eew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20368" target="_blank">📅 10:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20367">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امارات متحده عربی اعلام کرد که با یک پهپاد که از ایران به سمت آب‌های این کشور پرواز می‌کرد، مقابله کرده است.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20367" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20366">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gENEectD-VB8iJRJqvRyiVqo3CBl2SxNWui7u-pVcT9YRHyrxCLPVr6f-QQUcLKwv59vF7B8KncBwOnUKEo4LZNo7xH1IAKciVVDjRPObmY0psd0ENT78kaXvAqZ8I7lE7Qw1QMWVkJx4BsxcksBic0svQRgWAcR5k-Ahfi-hJLYIzLlH3frvXELKU6TI_M6EPPVUd9gggd3KjZEb5FRBYm5JlQcjBOZ0BhD0Le_9c_Y9RU4ydLZl3y7SO6Vy6HxbdTrs51mUf9PsM0z_gJQnIcDQq6TlWvj4M7WOpIY64hNpJonNTqeo3RwEFxns0-XD_f6UoSa88grqQgskkOPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20366" target="_blank">📅 09:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20365">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔺
پایگاه آمریکایی «المنهاد» در امارات هدف پهپادهای ارتش
🔹
ارتش جمهوری اسلامی ایران، محل استقرار بالگردها و نیروهای آمریکایی در پایگاه «المنهاد» امارات را مورد هجوم پهپادهای انهدامی قرار داد.
👤
روابط عمومی ارتش:
🔸
از بامداد امروز در پاسخ به تجاوزات اخیر دشمن متجاوز و در انتقام شهدای دلیر سپاه پاسداران انقلاب اسلامی و مردم بی گناه ایران اسلامی در جزیره لارک، ارتش جمهوری اسلامی ایران، محل های استقرار بالگردها و نیروهای ارتش کودک کش آمریکا در پایگاه «المنهاد»  امارات را با شلیک دهها پهپاد انهدامی، هدف قرار دادند.
🔸
پایگاه المنهاد، یکی  از مراکز مهم پشتیبانی و جابه جایی هوایی نیروهای خارجی است.  روابط عمومی ارتش، با اشاره به تجاوز اخیر دشمن به جزیره لارک، اعلام کرد، رزمندگان ارتش جمهوری اسلامی برای تامین امنیت پایدار و حراست از سرزمین ایران اسلامی تا رفع تهدید دشمن از متطقه، ایستاده اند و انتقام خون همه شهدای جنگ تحمیلی را از نیروهای ترویست آمریکایی خواهند گرفت.
☑️</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20365" target="_blank">📅 08:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20364">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBx-S5RCvSJh5DmBFHCXOD8Zi_TAdY8sNCFnPdxEH188TxVYgFUYHMEWAD3oBtp2eZEwWXUJO-_wjyMJfmVnLPwx6iqOPC0EUBmXgLYJDCSJbRicuBw9P5jhEH9z8Jz-ac3VlXOhKkMwFiIXCOhhPxanACDKGn3uUWV1glrFMQ-P9z8uia2Ggu0ccuo4eqOKhKfe1p0Q8zEwSCswD48yf1-CGjRw_EdQP_PnJK6XxSRa0qkPhn739Jk88lALMcw7QaJN4ziZJX-x7wIedd5BP42X9gktYaAvFAMuI6UNZRm2_UXfKJtAKo_lSrdeCiBDsfmz1e9KCArHt_ZuSHp07A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20364" target="_blank">📅 07:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20363">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:
دور جدید عملیات نظامی ما در ایران تازه آغاز شده است</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/20363" target="_blank">📅 02:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20362">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش هایی از حمله ایران به قطر</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20362" target="_blank">📅 01:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20361">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مدیر Secret Box بر این باور است که این تنش‌ها هنوز به جنگ نهایی موج ۵ ختم نمی‌شود و چند هفته ای دیگر زمان داریم.
لذا اگر تن ندارید لااقل آماده باشید.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20361" target="_blank">📅 01:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20360">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ادامه پرتاب موشک ها از ایران</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20360" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20359">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20359" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دلار ۲۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20358" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20357">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار در جزیره ایرانی سیریک</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20357" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20356">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارهای پی در پی در اردن</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20356" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20355" target="_blank">📅 01:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAXLPyuYgAv53p4UQWKoke0AI8p55Cy5qDDZxpNIRkHU6VEvMc2FB3WvIzPxRBBpeYG1J4mZpBP2-iYPsHcVIJuRqftTlEWbqBzOcvUtZXktonSsVXfHdAEouFkf0ufEsBQy9hGZi8s3rf8AUY7FJMK-T0SVVpXdEDpo5tG4kHv6qZ0qU1MANFnR5hvHNjpbjH5y0jc5M6FymaVKYgM631L1IGtxhPRTkPpnwEWE12JbmcY-EvlW9NPWRvfGxeaUz0I3x2Zr2ghZbi00CANvDG9Uc0wfnT4_zzK1MIpMr23cMeafKWV9dwonPq4hoM-RSGmjIvrXLrFmYokexpsfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان
بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20354" target="_blank">📅 00:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc-RCKkPj5L-HR3eDX5v3mSNr-3JRm45FVNFX_hki1hvjzjfYfvt0S47Fhpwd5CakdlBQR89HhbE5y8y3zwYFkb7C03lt99mXR6cVBmKPQ6SemYpC1zdpXTm51SzuXv6oWs_dGK6VXBaIA9IKtitGQsY6EDyt24wq64f_6F1y2HtEi0hR2HH9mAztTn5LDzQPnmbJ42lh0BQhpsCK9hNIvnN_Be_2B2TYakI2BzTQ42v7lCtmAoP1omaBWOpmKPGf9xWDvhvHOnl0sWgvc8lxcowAgp7HtEglG3EXZUUBwhBNFXY34WtexdjhiZ96vnJO19eWdXsRnzXLQu57OuJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20353" target="_blank">📅 00:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20352" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJ4yoOdZ7DH7rIYqMmHjRGVkrStsGI5gHo3XQQ1BTTNGxrZSNvVkgopVYY5j9CgNHyzZs9XtyVGpeaplOWs44euylWzVLhlszPT7Q5uV0jl3D3MVKZHfXLViXGs3uCQnz57JhOqmDcqGMFaWwkRCuDMSTXioUqLy4OLom-RStxISCYc6w6YpEnW1fzVmXPlo_zH7DkYO3U-bwT2P3hBm_xTpACjRKY_83kd3rATHKZ93jaModKbdadQgB4zjDsboV0aGXkpHbvTHNbYGRm5CuYTwA5QeWe9fceFD2HERHbB57FMjx5V3x63pPBuikhLH_qqcSBy3T40OitTvUqRoEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/20351" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20350">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20350" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20349">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اخباری دال بر شلیک موشک از مناطق مرکزی ایران!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20349" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20348">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اخباری دال بر شلیک موشک از مناطق مرکزی ایران!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20348" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20347">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برخی منابع خبر از کشته شدن 70 نفر در حمله آمریکا می دهند که به نظرم اغراق آمیز است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20347" target="_blank">📅 23:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجار دوباره در جنوب کشور!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20346" target="_blank">📅 23:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20345" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وضعیت خریداران نفت در شرایط کنونی</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20344" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=gE7rNroXMqBYG-vv2lgJGJJRKgN4WkeFOEg2iTOWPFy8CY90lGF0SXhzXsKmaSnSb2ZF80XHA2c_R4u827J28VFX3zpXIB5pQlR9NcruUZUFWZWECffcImGCHtSAspBsVpH3ERxic84206swbRi0pmMsmicmXfHl-LB4Tu8eVlUAlGkphkpMUdqttfbtY4y3dz35_ImIegGXT8UX-ArIzmXrAAXt8FlbEgUn47z1WwQ9oDhr9cNPPl62ytL2ae-HbYkGvynMIBYDnPBlntKOzqHyHqxHQHbMT52ZOhcg-uVJDy4ZSPKTnmLlZIykOolvul0c2Duh8iN1NMcqj8nP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=gE7rNroXMqBYG-vv2lgJGJJRKgN4WkeFOEg2iTOWPFy8CY90lGF0SXhzXsKmaSnSb2ZF80XHA2c_R4u827J28VFX3zpXIB5pQlR9NcruUZUFWZWECffcImGCHtSAspBsVpH3ERxic84206swbRi0pmMsmicmXfHl-LB4Tu8eVlUAlGkphkpMUdqttfbtY4y3dz35_ImIegGXT8UX-ArIzmXrAAXt8FlbEgUn47z1WwQ9oDhr9cNPPl62ytL2ae-HbYkGvynMIBYDnPBlntKOzqHyHqxHQHbMT52ZOhcg-uVJDy4ZSPKTnmLlZIykOolvul0c2Duh8iN1NMcqj8nP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کانال نزدیک به جریان تندرو:  بر اساس آخرین اطلاعات دریافتی، نیروی دریایی سپاه و ارتش در کنار هوافضای سپاه پاسداران امریه‌ای بسیار مهم دریافت کرده‌اند.   این امریه که از دفتر فرماندهی معظم کل قوا صادر شده به یگان‌های رزمی در تنگه هرمز دستور داده است که حتی…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20343" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20342">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک کانال نزدیک به جریان تندرو:
بر اساس آخرین اطلاعات دریافتی، نیروی دریایی سپاه و ارتش در کنار هوافضای سپاه پاسداران امریه‌ای بسیار مهم دریافت کرده‌اند.
این امریه که از دفتر فرماندهی معظم کل قوا صادر شده به یگان‌های رزمی در تنگه هرمز دستور داده است که حتی اجازه عبور یک قایق ماهی‌گیری را هم از تنگه هرمز ندهند، هیچ مجوزی به هیچ طرفی داده نشود و هر طرفی که از دستورات صادره تخطی کرد، هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20342" target="_blank">📅 23:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20341">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20341" target="_blank">📅 23:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20340">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اسمان ایران و منطقه  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20340" target="_blank">📅 23:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20339">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/COfB21QTSUOyqN1FyvRP8goTL8NWxQLBaWyYCW3JoQoeQJq9HLCT_HLr2-dVngx_FTaJjckTz1Y4e59bP07d1E9ONm8tDD0QcXfVfLVBKAavwqDtmrnE0B9l9TxqsJaJgFFBVclDT5NR9CaOFY5fYkn6jqdfAgk5Xe7EYsmDUH45I1VUJ1yDxkiM0866Tll2SpMcwfHSNA_0XdGnpFkhb87oyxeh3KykjSEpba9m24B7Ttrz-7FE091GadjXyJAnchHlok4zEJ-QHo4w-g5-hAJdC2RsTDfr-xhfSTyrfBJmk3dI3lg6_kpfNE_gW79Emeozf0dDbPyU4yNxzxgmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمان ایران و منطقه
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20339" target="_blank">📅 23:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20338">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سپاه: تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی، در اقدامی تجاوزکارانه، با حمله به جزیره لارک منجر به شهادت و مجروحیت تنی چند از رزمندگان و هموطنانمان شد.
این اقدام توسط فرزندان ایران اسلامی پاسخ داده خواهد شد و تنبیه متجاوز را به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20338" target="_blank">📅 23:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20337">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ygr-SGq2_WRr6ZUpDzSAkz48Pk1KiZUb5IH5iEURNfvkbcc6bD8h83VyoAxg2ZmbfogfAUmE_0jRQzbZv4HFgpMpYL3alOXzEPv_U0ZyJkKbIOHbV2VIulEb8C9PjahPa4SyZH1DoEp3a8C37L_0rIxi4gz33xz0pEOipglcBXs9HhQeI0w-IAS4dHtyGNABX5JRgoD4MwyiuMvGUsIH2dHJ9CLW7O4v_j_bKQpeWxqE8B6a4T-3ujX4vwJ34OqIbmuafUcAFom1mI7g164pQ2WfMS8iqG0hBADcK2_Iil3zieZJ--V_cesTOcBkGmqMUpMeVPuqLTFVmXIGfRpV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدافزارهای داخلی از آنچه می پندارید به شما نزدیک ترند....</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20337" target="_blank">📅 23:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20336">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مرندی :  رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20336" target="_blank">📅 23:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20335">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این صوتی را عصر ضبط کرده بودم و اتفاقاً محور آن همین وضعیت سیال و پرنوسان خبری — خصوصاً برای یک ایرانی — است و جالب تر اینکه از مرندی (خریدار سنگین نفت و خالی کننده شبه جزیره عربستان) هم یاد کرده بودم...
برای هشتگ گذاشتن تاخیری حاصل شد و در همین فاصله دوباره جنگ شد و مرندی و ....
سبحان الله!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20335" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20334">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB50GhFok70_saXQAlhaMqNJ3RJnScHMMLfW2SxPq3vBwEi5tyKbY2GjrzkoFrxeG3Fab_3xl_c_cEy_fiSb_t4R3BDOj1UMOHHyY4dvvX7Pn-dr2IhGZFAmZ7_wPvNWmGxP0Y2xg7RbJXiP8zvH5ugocmvLcUDN3Sb2jATmeH2qFNcLlXd94ixFIiChxNOy8r17pBoY2o-VFk2CDlfR3hMgzv-vX0IG0QrCA9_0C4G7Qdjn7LXq8-izKSygD7fVfmrZQdaY9_flFqkttAm4eaEdzLUP9dQyRH78JsJgEiQ3UaMf3Wp9OtZmpjhktB57AyvxnU76wW9betrx2MtfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرندی :
رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20334" target="_blank">📅 23:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20333">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه عراقی به نقل از یک منبع ایرانی:   شهادت شماری در پی حمله آمریکا به جزیره لارک در جنوب کشور</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20333" target="_blank">📅 23:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20332">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال Secret Box بی تردید ناهمگن ترین کانال سیاسی فضای فارسی زبان تلگرام است!
از بسیجی مبعوث شده کف میدان تا شاه اللهی مخلص اسرائیل اینجا هستند!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20332" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20331">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خب گویا لارک بوده نه خارک!  مقام آمریکایی به شبکه الجزیره اعلام کرد:    نیروهای این کشور امروز به یک پرتاب گر موشک در جزیره لارک حمله و آن را نابود کردند. مقامات آمریکایی اعلام کردند این سامانه آماده شلیک موشک به طرف تنگه هرمز بوده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20331" target="_blank">📅 23:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20330">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=lDmrNqLutJHzD2e-EuFJDpQCtP26Ivwu6Iz-q4jfundZnk1sqzgSSc3rAE02SO5sR635BYl1ZNqeNfza9nrQiFIBKlYhwmc_OhKVlxqVdBswerYNgUbr3FndxWPjLiOc0nOAR-_GVU9Fm3dHnuTc1J5LWsmlvCNSGDaMs5gV-S1zaQFQNu8eRHYypxqiMofV6rdfPslV51AO8EXgjhseV6EOHsl9p3LyR7HJvDWhuvuLAdzBO_Rb4JfTpYjfAoQYIkDgm9dTMrBtPf0gnwdYofTGi5A24GdzIBx640ryPd4WUfGaWhDnA4SGSQmkuUB897iLNlB8OYtwzMzSjORe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=lDmrNqLutJHzD2e-EuFJDpQCtP26Ivwu6Iz-q4jfundZnk1sqzgSSc3rAE02SO5sR635BYl1ZNqeNfza9nrQiFIBKlYhwmc_OhKVlxqVdBswerYNgUbr3FndxWPjLiOc0nOAR-_GVU9Fm3dHnuTc1J5LWsmlvCNSGDaMs5gV-S1zaQFQNu8eRHYypxqiMofV6rdfPslV51AO8EXgjhseV6EOHsl9p3LyR7HJvDWhuvuLAdzBO_Rb4JfTpYjfAoQYIkDgm9dTMrBtPf0gnwdYofTGi5A24GdzIBx640ryPd4WUfGaWhDnA4SGSQmkuUB897iLNlB8OYtwzMzSjORe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20330" target="_blank">📅 22:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20328">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو :
طبق اسنادی که به دست آورده‌ایم ایران بار دیگر می‌خواهد برنامه هسته‌ای خود را از سر بگیرد و بمب اتم تولید کند و ما قبلا هشدار داده بودیم که اگر ایران برنامه هسته‌ای یا موشکی خود را دوباره شروع کند ما به آن حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20328" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20327">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20327" target="_blank">📅 22:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20326">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حمله ایران به یک کشتی بحرینی در خلیح فارس</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20326" target="_blank">📅 22:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20325">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20325" target="_blank">📅 22:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20324">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سناتور تد کروز:
چیزی که من خواستار آن هستم این است که رئیس جمهور ترامپ و دولت او معترضان را مسلح کنند تا مردم ایران بتوانند این کار را انجام دهند، کردها را مسلح کنند و به معترضان اجازه دهند این حکومت را از قدرت سرنگون کنند، نه با نیروهای آمریکایی در میدان، بلکه با مردم ایران.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20324" target="_blank">📅 21:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20323">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل طرحی را برای سرنگونی نظام ایران تدارک دیده است. در راستای این آمادگی‌ها، هزاران نیروی کرد به اسرائیل منتقل شده و سناریوهای عملیاتی مختلف را تمرین کرده‌اند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20323" target="_blank">📅 21:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20322">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سازمان رادیو و تلویزیون اسرائیل:
شناورهای جنگی ترکیه به کشتی‌های نیروی دریایی اسرائیل نزدیک شده و برای آن‌ها مسیرهای دریایی مشخص کردند.
نیروی دریایی اسرائیل سطح آمادگی خود را به منظور مقابله با هرگونه تحولی در دریای مدیترانه افزایش داده است.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20322" target="_blank">📅 21:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20321">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20321" target="_blank">📅 17:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20320">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20320" target="_blank">📅 15:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20319">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315342d71a.mp4?token=gfzwFxGK3HNlI4J3aPjGfC5x3iDRNqFN9yb2cUmDkeJvvqlPsTMbShGNu4wHye5yZh-YiOU7gwFo3UTerd3Bj6-Y8mrB8oYyirCUuOAufPXAx0FJYrawdrzPVjhtCfDO6b0s8hHRXqcQKSYUzGEWHCmWon8ab_hMSHkg650JPj0ctNovVjtzgWH-OBUoZjQ9Qm7DUhylgr5CCYOqRjhF0Z5oHRxn-eCk_-PXVhboF9iOGF0VmZQMyqt4qzFSrVRzEzZok5v8moW2qXJzHhe3nufKm7FjwNDT3Q-OpMECo9G7bykzldgXLLHFPw3HqNKMQY6mE_RiHDaMbp_P5p1dBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315342d71a.mp4?token=gfzwFxGK3HNlI4J3aPjGfC5x3iDRNqFN9yb2cUmDkeJvvqlPsTMbShGNu4wHye5yZh-YiOU7gwFo3UTerd3Bj6-Y8mrB8oYyirCUuOAufPXAx0FJYrawdrzPVjhtCfDO6b0s8hHRXqcQKSYUzGEWHCmWon8ab_hMSHkg650JPj0ctNovVjtzgWH-OBUoZjQ9Qm7DUhylgr5CCYOqRjhF0Z5oHRxn-eCk_-PXVhboF9iOGF0VmZQMyqt4qzFSrVRzEzZok5v8moW2qXJzHhe3nufKm7FjwNDT3Q-OpMECo9G7bykzldgXLLHFPw3HqNKMQY6mE_RiHDaMbp_P5p1dBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح یه خط فاضلاب
به مناسبت هفته دولت
اوج خلاقیت
فقط اون روبان قرمز روی شیر تانکر
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20319" target="_blank">📅 15:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20318">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrQpkdgbIQWS6VtiT3p-s23zgBZF0H7RS5LN9JjAZZa3IOoqbWrhqKrEsJ5Bw_s_KrVbPeOsxh2DmyTZ5eNMhhtcmlHG74RZ5z6gi6Ed77_3jMMNyIXRd9iMpQeqT2puiz9k2Ku2DV9bGKMDrLUhbADEw1YXXUgTdPUdvwYJdvE8V56WjSpf_s3YM8B4vNMWQD1InT2mB7nv_mr9zB2qSO3LYjuDIzdc6LczUowU9zXTu-N4qHJkm0tlhMRbdfZSYN-jhBnlX7mGw-RIHOI8jDzU-wCFaGi4wvDl1e62onOFG0Zio8uuUmY37zDzfG3cfyLGWcF7nerdr4ixoXAF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور سرباز وظیفه در درگیری مرزی در پاوه
مهرداد طاهری آرپناهی، سرباز وظیفه اهل شهرستان کوهرنگ چهارمحال‌وبختیاری، در جریان درگیری با اشرار در منطقه مرزی پاوه ترور شد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20318" target="_blank">📅 15:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عراقچی:   ژاپنی‌ها آمریکا را بابت جنایاتش پاسخگو کنند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20317" target="_blank">📅 12:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20316">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بیکاری هم بد دردی است.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20316" target="_blank">📅 12:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20315">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فوت ناگهانی، هنگام سخنرانی شبانه!
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد حین سخنرانی شبانه فوت کرد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20315" target="_blank">📅 12:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20314" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20313" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=mlfMZtzgG0BwC3h7AlZSpsThVJxS7TBvGe_HbPPyCMCc9xQXVYS0kSbzICU1hgfD91x3TWymsCaUyaFk57_MaWSNwqzarsUaXqjqFVJBoC__v2huaDO8Tzuz0gXYdQRrmts0QavnuhNhw_yrs2Z4Gsx8cYObp9GWq1cSwAhBw_viQBT3VCy8vi-fK51L3dqYS7r5TWRIbZeSyjs3_MfrlUYk_g0YKqkGq7_WKiOjeVe1cWNcoF2Bvw4E7tj829KOF6e0WUlfTGRVR6QJdJQruQh2aGchXdRvIr0q6CPhi4U2c6fjjZxFkCGxUp9jI1xDnhFwQMm7I1VyQPPnxr4Q6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=mlfMZtzgG0BwC3h7AlZSpsThVJxS7TBvGe_HbPPyCMCc9xQXVYS0kSbzICU1hgfD91x3TWymsCaUyaFk57_MaWSNwqzarsUaXqjqFVJBoC__v2huaDO8Tzuz0gXYdQRrmts0QavnuhNhw_yrs2Z4Gsx8cYObp9GWq1cSwAhBw_viQBT3VCy8vi-fK51L3dqYS7r5TWRIbZeSyjs3_MfrlUYk_g0YKqkGq7_WKiOjeVe1cWNcoF2Bvw4E7tj829KOF6e0WUlfTGRVR6QJdJQruQh2aGchXdRvIr0q6CPhi4U2c6fjjZxFkCGxUp9jI1xDnhFwQMm7I1VyQPPnxr4Q6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20312" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=WUSpJKN5J5FVI18Hg98t4izxuqF7U6CULdXbtb43tD3NBSYSbMr33yc876xFinc1KmhEHVk5o42pS1G51sSWt-Fja-3gZ2tMIwDAojtYcklRiVuROaWH7UFqLDo8xBtn-_jX2Rzuw-KXhAU_0GSH6kNsHl1JcHm6q2SPwRXKLhsb_dqHJwOZXOWQOkWkXckHIua2mgLjSkM8kjyFOPjkPhsPzQvxA9U2qPzVxP4kgeGEasKE7hYf5MRCf4cFDWW5H0KE233pvKedkwEzhP7lccOXo2Rx8VNtxTqE4tkdAox6YTfJXp44AXzlaceMjyWsFhkZ4fM4oPyh6gbipnF9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=WUSpJKN5J5FVI18Hg98t4izxuqF7U6CULdXbtb43tD3NBSYSbMr33yc876xFinc1KmhEHVk5o42pS1G51sSWt-Fja-3gZ2tMIwDAojtYcklRiVuROaWH7UFqLDo8xBtn-_jX2Rzuw-KXhAU_0GSH6kNsHl1JcHm6q2SPwRXKLhsb_dqHJwOZXOWQOkWkXckHIua2mgLjSkM8kjyFOPjkPhsPzQvxA9U2qPzVxP4kgeGEasKE7hYf5MRCf4cFDWW5H0KE233pvKedkwEzhP7lccOXo2Rx8VNtxTqE4tkdAox6YTfJXp44AXzlaceMjyWsFhkZ4fM4oPyh6gbipnF9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:
به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20311" target="_blank">📅 01:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWZmtNocKcS9QBkpDvD3gzTDJia_tCX_TaOjzhFzS0KN7eODZi2509DoCap13oVpqovH8gdMma62AZkOMptXaiHSosxzyS9LGNkRWnLRun5qUxVtuf2JG4Y3syts29-A_zN71M3E5OBblsFIhiED7TQ0bh0qVZ7fXovvhBKtC9r_Yt8OvhMmFCWKbkjr9dp4fNW7IRI_FODCJKajFZSpv-3oFdIzCXzUm9FuNaauhcfY5TmacKPYysMO4H_ftp8vZuQerlVK4ID82qMHDd_GDBRqA6tw-8DcFydZd1JZvvH2bV4GjnK5JW1rkfQd9Bkz2K8H3Yz4O7pYi__n3YF0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20310" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند  وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.  و آن درس چه بود ؟  ترس ها برای ایستادن در…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20309" target="_blank">📅 23:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند
وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.
و آن درس چه بود ؟
ترس ها برای ایستادن در برابر شیطان بزرگ ریخته شد .</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20308" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">غریب‌آبادی:   هیچ کشتی‌ای بدون هماهنگی با ایران نمی‌تواند از تنگهٔ هرمز عبور کند   تنگهٔ هرمز کاملا بسته است و اگر کشتی‌ای از تنگه عبور کند قطعا با هماهنگی و مجوز ایران است.  نیروهای مسلح ایران کاملا بر هرگونه تحرک در تنگهٔ هرمز اشراف دارند و به‌هیچ‌وجه ادعاهای…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20307" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20306" target="_blank">📅 22:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌سرلشکر رضایی:  ضاحیه و بیروت خط قرمز ماست و هیچ‌کس حق ندارد به‌سمت بیروت و ضاحیه حرکت کند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20305" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRk-5JqJO_8lMAu7GC_sVlRjwVE-aU0eaoiKvsgKOdPud5JAqLhQdr3XdX-QYgE6BIbCRPdvJqEt6uPds2ThzrYXCuCrFzYcPhnFEPbob4M6hkmFb5k4HZeWjw4jpChZ9oCvAXzzcYgXIveNZvYdMyU08AUJH6eZgriWLliOA220WC3wZ09toY1UC49IcPVlE47XI0JaSlvtkkdiOWaqhe_eQ7nHhKqFvTTFQXpfy2n6SE-Gm5ndMcQnCusaubk7oSFAsdU_TzS_yezeybnHpNqy9pVdqa78Py6D0JkPHhKhTazoHTCjH2rl1n9frrBeJTwkLbwfrp1xSsduJGM3uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه هشدار داده است که در پاسخ به حملات اوکراین به اهداف داخل روسیه با استفاده از موشک‌های کروز بریتانیایی، ممکن است به اهداف نظامی بریتانیا داخل و خارج از اوکراین حمله کند.  این هشدار، قوی‌ترین هشدار از این نوع تاکنون از سوی روسیه بود که توسط ماریا زاخاروا،…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20304" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20303" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRUUhA0qOvzEemd34GqWSLYJLsXGMLpdyQjY_x3y3CyIr8_KMIL_SAoAqDXGnyr9sD9ViL5j5tja1twN6iB6Wb29Qq3Gxyz67VyP2-26ZPg9ZZzfY_6apEroaCFZqCK3C-nT_uLlZebAOW9Qv2_D-kuO9y4r-c5lm1I7P6-bwnLEbgXpgWaNkjcSwJCEKKT8AUXbjQTubABDfBaS9SETTO33zUhtB8GiiUEqtT83GshrjQPfDgYlUnIuD2qN295Y1SKp03fGxyUxYOxrAKzZe0ayTC_CV0xgH1NtGVWVVqdRLl9J810Q0zUGF_X9uVLe6AC2ZRu5cU6ZXTQ1FWDVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!
علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20302" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20301">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تحلیل اسرائیلی: اتحاد اسرائیل و یونان  بازدید رئیس ستاد مشترک نیروهای مسلح یونان از اسرائیل، اهمیت راهبردی روابط نظامی بین این دو کشور را برجسته می‌کند. با توجه به افزایش تنش‌ها بین اسرائیل و ترکیه، این همکاری اهمیت بیشتری پیدا می‌کند.  احتمال صادرات تانک‌های…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20301" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20300">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏پزشکیان:   اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.  با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20300" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20299">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏پزشکیان:
اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.
با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20299" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20298">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20298" target="_blank">📅 15:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20297">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i74SaFCc3DurytSbxN2rpCc_MKOgxhfmisaHPuLxqyi_g6CrKjjuhK92JNPdpioocFPs7VhIqefL9YCgnXYMYbIb1Hb2TlrxuNRc0WlBngy3rhJUalHzN-ca6gC2iQ2zwK5w0XB2r0Q5M9CCdZYxttUCpT2N1WOOQ3-vP5jXQBN4WABbxe8alY6x2yhRNzR_k3nNQ5_nh_BragTeLqc0MCgayx9tIF22mTB-od5ALnk-s0saaH4P74GCUbucGv2NM5kYEowmIxvGPUZqBkQ4O4uCwQj5VMyPeTiunRxxDaFbzrDn2dQWXR4jpBdPZImmY6J3IG68HXgNWg3kP6hpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20297" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20296">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20296" target="_blank">📅 14:53 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
