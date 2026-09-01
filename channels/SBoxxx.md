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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-20397">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 556 · <a href="https://t.me/SBoxxx/20397" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20396">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/SBoxxx/20396" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20395">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر راه:
رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 771 · <a href="https://t.me/SBoxxx/20395" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20394">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دلار فردایی تهران
⏳
213,600 فروش
🔴</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/20394" target="_blank">📅 13:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20392">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏نبویان:   اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/20392" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20391">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏نبویان:
اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/20391" target="_blank">📅 13:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20390">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/20390" target="_blank">📅 13:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/20389" target="_blank">📅 12:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20388">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
آمریکا در جهت ضربه به تمام فرماندهان سپاه آماده می شود ! عملیات روانی همزمان با برنامه جدی برای ترور !
⏺
در لیست تهیه شده توسط دپارتمان جنگ ایالات متحده، فرماندهان بسیاری از نیروی زمینی سپاه، قرارگاه های این نیروی و حتی فرماندهان سپاه های استانی و فرماندهان…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/20388" target="_blank">📅 11:09 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/20387" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/20386" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-cBiyqkuRSaqsSDbd2gDMPmlMWakZXpl11OpnChPgocCkJ-m6ujXlT03VBwRj3Lzs2pSm55JqZGB19eNZd40Gq11It--N2k3DEAp9S4e9yUa5gyxFrCxe-O03JjZ_PupmydeKaEOUU1KmGFf8I_XTVanv8tHUriQfcbuyaYMYFN5pp3Xbg02MPm46qBLDzIgNd6Ctq1upvHz3KM5MC9MPSpq1v6sUxegLjrFZvQ_6t7-Ni6W9SHGVuYlsb_MZQFECi-so0WTuuQLBQMFGxUfsgIxzbCUcWMuSLaP43RLrVhpirkh5Z5qnBXxK1qfp1JzKtQbu2h5y73XTXf_S2FUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه بالا قرار دارد و بازار رنج و کم نوسان پیش بینی می شود.
با توجه به روند عمومی نزولی در 1-ساعته، فروش در سطوح مقاومتی (4477) بهترین راهبرد است.</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/20385" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این چیزی که ما اکنون تجربه می کنیم عملاً نوعی «تجربه نزدیک به زندگی» است.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20384" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجار در سیریک</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20383" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ایران یک تانکر نفتی سعودی را در تنگه هرمز متوقف کرد.
بر اساس گزارش خبرگزاری فارس، یک تانکر نفتی بزرگ سعودی در حالی که از مسیر جنوبی تنگه هرمز عبور می‌کرد، متوقف شد.
ظرفیت این تانکر 2 میلیون بشکه نفت است.
طبق این گزارش، در حالی که این کشتی از تنگه عبور می‌کرد، ناگهان سیستم شناسایی خودکار آن فعال شد. فعال شدن ناگهانی سیستم AIS نشان می‌دهد که یا به این کشتی دستور داده شده بود تا موقعیت خود را اعلام کند، یا اینکه در شرایط اضطراری در تلاش برای اعلام حضور خود بوده است.
امروز، سازمان UKMTO گزارش داد که گزارش‌هایی مبنی بر وقوع یک حادثه امنیتی مربوط به یک تانکر نفتی دریافت کرده است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20382" target="_blank">📅 00:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20381" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovrVLRQ9UGa0xGOLaN1BgQnEuxTT4DGm1zsiGTnWzkGEpa8Gk3xklqL8bRDOzjQXbR3-lEq5p1OvDlXXLimq8Ao_FzKBMpN2SxOkrKH7KyUX5il3ON1APH8xIEhpLRzaPJP5m0jQL5JWNshfzGfN_p91cOz9RPnEMGdM5JWDycW5uCtFtMIQXePZhLuWVFgPmSAmeEbg6YWrh8ckZegWQXBhMuAFplVBBV-NpLWibLbfmkmyGxv3b46QfYEMabuZnidfZLlmNXhPjqSC2rZgBxweMspkCVIiG2PnUmoh_tD_VMYTk_n3x4DGCzhE_ICX498d7FEJb_X7gU76Hes5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار رشدهای عالی را در طلا شاهد بودیم.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20380" target="_blank">📅 00:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش های اولیه از حمله موشکی آمریکا به یک نفتکش ایران در اقیانوس هند.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20379" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حملهٔ مسلحانهٔ عناصر پژاک به اهالی یک روستا در مریوان کردستان
در جریان این حمله، تعدادی از شهروندان محلی زخمی شدند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20378" target="_blank">📅 00:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20377">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20377" target="_blank">📅 23:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKbPJbTQbqzL5cSstZkr56Px5qKX1JsfFSBl5skxwf2H7UkiwVbT7kf6vo9cxZmRJ3GGMY-46D4ffRneAI9JqY1Wx8f-C-U4L35foxvz_KhphH9Scfk0XBKJgaXDxJFUpFHuYpTcXAgcPvBa1TBX_xem7COfidFCOlYK15M3GwR6uee06x7JsWejtEYIIjxKQK-wm_yrthfcSZANZmZUurkXVCjCGBBvjm4cVtuiHipnrUuNQvFCgkgagQhxgSc5j8BBVVkfRbgAXLeaJ24a3_qRwPUnK6O7C8GWUNfIGpQ8FSNxA_vRbYVRRUZbuzbXQuNYvSmeC5kY0zWyYdkviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20376" target="_blank">📅 19:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دادگاه مرکزی کیفری عراق، امیر رحیم جبار لازم، عضو کتیبه‌های حزب‌الله وابسته به ایران، را به دلیل گروگان‌گیری روزنامه‌نگار آمریکایی شلی کیتلسون، بر اساس قانون ضدتروریسم به ۱۵ سال حبس محکوم کرد.
کیتلسون در ۳۱ مارس در بغداد ربوده شد و پس از حدود یک هفته، در ۷ آوریل آزاد شد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20375" target="_blank">📅 19:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسکات بنت:
به دلیل محاصره، تنها 30 میلیون بشکه نفت ایران روی آب باقی مانده است - بنابراین حتی اگر آنها بتوانند از چین پول دریافت کنند، این مقدار تمام خواهد شد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20374" target="_blank">📅 19:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شمار کشته های حمله شب گذشته آمریکا در لارک به ۳ نفر رسید
خبرگزاری تسنیم:
در پی حمله شب گذشته آمریکا به نقطه‌ای در جزیره لارک، ۲ نفر به شهادت رسیدند و چند نفر نیز مجروح شدند. مجروحان این حمله برای مداوا به بیمارستان منتقل شدند که ساعاتی بعد، یکی از آنان نیز بر اثر شدت جراحات به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20373" target="_blank">📅 18:01 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20372" target="_blank">📅 16:51 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20371" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20370">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ به فاکس‌نیوز:
ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد!
ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20370" target="_blank">📅 16:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20369">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">میگویم اینکه خارج نرفتیم به این می ارزید که موقع برگشتن زیر تیغ «حافظه تاریخی» نرویم!
سبحان الله !</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20369" target="_blank">📅 11:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20368">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZWEWDIwiLVUVaFuKjbTqGrmOkAObg0GXRPbuw01ZT__K5tR57ywqrDf-lx_x_CypnCs6MOIo8F4H1tjScZjN8rj7z77DfbsonHQ4q1Wpzh0nAdhCf1HwCdfKALFiEZ-gc5O7fG2cU1SegW7WqtugLeKsImOJUstdYCCJGDjUSeiBNwroQdfBRJy1OAnRswmg3eWtes_w35Tx0kvoNbUPtj_u6kvAt_gWMNLASj51fs7V7YxTY53QoYrkJMXv-gn7dRlaHnjaK4O3FMQh1oV18u_7jHt83SccsaZAZSjbvuyFXGgFrOUbbMIlQet-PJUghrv9d8PRjNDVt5L2G7NNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20368" target="_blank">📅 10:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20367">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امارات متحده عربی اعلام کرد که با یک پهپاد که از ایران به سمت آب‌های این کشور پرواز می‌کرد، مقابله کرده است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20367" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20366">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruxyX9b9ei0MbFP75DdRaLNn-PrGDEDHkg7tYVpdjD1IL7vOreShEIq7ZmHKUND5Eh8fSVbKz3bDfiWZa6HUwH36vzWQbMLJeuvbapkWNROfnCm1Yq8zsXLGraPvVDQGK5A1fZsowWEZsf6KWDc89Y33N0EISamL03tYG9uI8GYZ4h0B0-8UtHFEZ49NudaruuS4ZL7AcP66HDfVtrCP4OaRi0PObu1-ENFHikcM_rBE1sZnH0Ea0LC0lRnKP1WkiCc1AnHK71r1Ae-CVWessTf4WY1MKWTON2xyUQn0KrLsmSygwZWSa4sBZjWTfUk2gyjZwdv1TdIJXvmJZPRFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20366" target="_blank">📅 09:31 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20365" target="_blank">📅 08:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20364">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEqWWLzurNBEM3M6AAQ3Ov6a37daRNF7IG0_TkGgcCQLKn_xIh_mDRQ9uj3H0sNbwoZKUrHgA9YaxgLMiTLiGPu5RLegqPh6o_tResLJ4p0Hi5ok0CpJbrP7BAvMm8brQ4v8r7ZI6YlFPRnOVeIjZoK9-WwRgkbRn0w3hblAoGGhb3vLf4TQsxdllKDreDwkIy0RhlZFU9D5mpOI72Prl_p3iGyTNUPWcwjAtr7F4Oa2YgxMM8batQ9uYxTbCiKOfnbtlW9bdMdBg4l_h6RCVtjxGycOVAUon-f1hkrX_ovu0v3RWliVYHrwrEK6NQjsnfl2dGjjeoGtLfLP9DEELQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20364" target="_blank">📅 07:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20363">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:
دور جدید عملیات نظامی ما در ایران تازه آغاز شده است</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20363" target="_blank">📅 02:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20362">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش هایی از حمله ایران به قطر</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/20362" target="_blank">📅 01:52 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20360" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20359">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20359" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دلار ۲۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20358" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20357">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار در جزیره ایرانی سیریک</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20357" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20356">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارهای پی در پی در اردن</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20356" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20355" target="_blank">📅 01:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpcAhK324WUK8SC7E6DCzxKkvaWlN2lNM6Gjgt78q-5s_A0yqWO5lUD_F8jzQ6AbqWj-1lnxlxnBwQxfzaGJOaybHvwgdT1soakt7lXQGr8lKTrcmarzkH7SQCay4TLNavFTdWPKs0-FdxKHALESqGfEM-BuzXMDJthnwWwE6X43qOE9B9Rwi78uAA-YDlW7dFs2r5zISrTupTT6TVMmfh42PA4eRgKtasv-oGeCKPluHgGaqhOkIwZ8f0H6IlXDkmJWRldKpF9gKk7QhUfej18yBGphd2Qu1Yhj7RvsuITOcZrjr78NXPYHNt2POPNfoj6vD6P56jqhzDGrko2aKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان
بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20354" target="_blank">📅 00:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTB2woPBRUYnBJ8cci_W7x0A98kqczo2keFRiLeTAH8RCHsUR37BUnSbDRQ-xMWpo49WybDqwdvCPcqXkwVdyEYaHvdlqXOEiQWR7ae1SLUn4OYoUjZ89i55_Kdw63w8nLIhpKTIsG9Hs4pFJpPS2_cg8nOU19mSKcUrPhaJ_76fWQdIU8Cm3ynkR9NyGZNF5GrXXpww5eHqbejRzafqaqBi6dH46ZR6F8IcbcL88UWK8cE-0YEYtHiuN-iicIvMnzuaAgDJga0n2BGUiNlJWwljqNsubZOJDFt518XuIEr1CvqMBNaeIN4MQS-gr3SGVVqj_Er-mjAGYGke08yUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20353" target="_blank">📅 00:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20352" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZCG8RxqneU_6Iw-PysKhAfvJNoY9_xAOm7eg1hrdLYTIyVbRhrUEurg8ZIQ33DNH97KN3z49tcUfpl3a1GYjiroBpROnPA79P_3MEgaJbQ6lhBf_w1PKqJ3W4jyawUfox7ol5BBlRYn_BFp5qMG6fV1rpIH3lLQvXmOXr1e-cpQZq5W39YFF3tAwwMhOMyHyyOcdGlJGAm3g1swTeIf2nLSZ0OXECspjYkYt616nXp6ttwopRbwO3gdm5c8hklFDt50F0sCi8Z_httJfSbLpSPZh7UeAI1HbXHHzhZIyoW3fEGGvujjuoS2xI2YjbwynybXrdsmsVIM8vL5SHzspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/20351" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20348" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20347">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برخی منابع خبر از کشته شدن 70 نفر در حمله آمریکا می دهند که به نظرم اغراق آمیز است.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20347" target="_blank">📅 23:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجار دوباره در جنوب کشور!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20346" target="_blank">📅 23:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20345" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وضعیت خریداران نفت در شرایط کنونی</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20344" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=vNGSjJYlkZi_PAENyBcyHeMLJJuTqrM8t6Vb1auqrjXU2YxHVM-gqcI-4Zk9ZGXzblYn088yLpzC89UC1SOwaA0JYgzr2glI_DFYaeNT6eDL4cdyj9G1sB__KJhH0wrRSlNMVAcAG7Lmb7q3YFvHfO-HyKgq3Jfo7KEUFJeLOUjU4v5USEnQtB-CLARppPW-tk9-Oh2dlU0_eFuukntjZOxjXfUFLJhSQFDHsuVvl3-nGWwop-y0mRgn7S5hHaN8W9gMXVVwLAbftKqiR75dxFSMXrw_PrToVctP86iSHpA7u1fVJZ8KpnXhLApDDNeJKENyq354CAuE40jkJf090g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=vNGSjJYlkZi_PAENyBcyHeMLJJuTqrM8t6Vb1auqrjXU2YxHVM-gqcI-4Zk9ZGXzblYn088yLpzC89UC1SOwaA0JYgzr2glI_DFYaeNT6eDL4cdyj9G1sB__KJhH0wrRSlNMVAcAG7Lmb7q3YFvHfO-HyKgq3Jfo7KEUFJeLOUjU4v5USEnQtB-CLARppPW-tk9-Oh2dlU0_eFuukntjZOxjXfUFLJhSQFDHsuVvl3-nGWwop-y0mRgn7S5hHaN8W9gMXVVwLAbftKqiR75dxFSMXrw_PrToVctP86iSHpA7u1fVJZ8KpnXhLApDDNeJKENyq354CAuE40jkJf090g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کانال نزدیک به جریان تندرو:  بر اساس آخرین اطلاعات دریافتی، نیروی دریایی سپاه و ارتش در کنار هوافضای سپاه پاسداران امریه‌ای بسیار مهم دریافت کرده‌اند.   این امریه که از دفتر فرماندهی معظم کل قوا صادر شده به یگان‌های رزمی در تنگه هرمز دستور داده است که حتی…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20343" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o8L_GRBbvtF-6zSxgjFiSGxzXox-90pYgsyksGRrecGF_lSGgfz_LzyrLtcK3PWT2-FOF5E7QTuMmkrb3vCCusFAWC3r2Th3BgWfEm_QJ-GoVHWcEqY7fAxMpxn2Ej3yoJZBldEV_-2fXRCsKfcUYQTb_8Of1l9c997RFvSuRpzXLhh-VGwfQ0enmmupP05waZbLZJ8MJ1j_WcnrYu1z3GHIZfINy3xIe1SnG3O5xbnkW0tgrfRGeHOgGwez4HEcFALOwfZxGHe_p7d9ATGKNmsI3QKba6c3VDGgkiUpsrRTzgQBV61FxJ7iMUCgCiwagjEFhH3o0IwC6m9Ex7IKfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20338" target="_blank">📅 23:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20337">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAwBJ5SflBM0QqtK_EFfH8rClRc14UrhOs58dpWMYYSyecELprsee5rDm_uyF6RRIguxcA3Znq5H6CZXa2G3YBRBL2e-6CDtyHRy-Q-cIzVU9XeUaNSzAXYL-eH3UFHpdxpQ7CWIfvFHOHg-3cq_jRHpE5ra5_-L5j2Kj4YouMh-8FUU0hY23luTJHLB03BR3ZSqca23V9JUQ9Qhe4ZS1u0Z4_YK8dr2VNxu9Q3yBPAOoRBU6W-Ij4E7xPWgtDxhbm8tp7RaWFWJffY7s0lqIFHLpxoGVFP3-t0IE3Y_cJjIOXxpAi49IsJC99mPr2wITTMTPAzu_lvQc3Kxuc6ZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدافزارهای داخلی از آنچه می پندارید به شما نزدیک ترند....</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20337" target="_blank">📅 23:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20336">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مرندی :  رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20336" target="_blank">📅 23:20 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20335" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20334">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcGScOaYc2L2YQjscsM2IjwrylF2CQoIOjgc8tlMHhKs5sT5l67dyhlb3NJaBKRRyyXV7DiPP5Evec1uFlOD1akcCebBvXDnX7gDbLuyh5VVGccY-mbtpu6lwzdZpg7ixH0XKwuyvheVyjtpulzgy-zcLDHnPzlMzZrYdZHA7SnytICVv53q55rJF_CiobBb6cfliJXLx9dsO1ATvt2fkQQ9KGLI8E57Nzw9sGLkawdKHATnVetB1jWG8nfUGpA-gWHk-j_neBKIIevMAwt2ZfAwiAx3ko8-Kzjfs6FrPyBrCH0V-QsCPIywBt8PXpQlkj6-CQuRytJ6zewUcT3geA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرندی :
رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20334" target="_blank">📅 23:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20333">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه عراقی به نقل از یک منبع ایرانی:   شهادت شماری در پی حمله آمریکا به جزیره لارک در جنوب کشور</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20333" target="_blank">📅 23:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20332">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال Secret Box بی تردید ناهمگن ترین کانال سیاسی فضای فارسی زبان تلگرام است!
از بسیجی مبعوث شده کف میدان تا شاه اللهی مخلص اسرائیل اینجا هستند!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20332" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=tX-X6QmkbvYX2gNaTFqwY8f3zrRrimTRmgz39zHbViu0NimayV-mhNeVGyAAJE4ztheJrjfO8CN6OqTJ-DvFVz_IuAg2pga72jgKJkpayfGnZVDnh0skDf_mxFKwR0aSjUfb04dLhwVGK7eBK71YLxZJOy6o2vigHSEpAeNHCHCw1pM14t-iAHXyIatUuU91WAoX0RdvICG1KsUFvXtUhniEqzy49yZBuBTQW0itPU8ssfeY1rQ9KM3pnPS-2EaQfvVSp-0W_fu2G7_dcPa3zTZG3i9uTruA2qGubhVX0PXZ4K4JTFa1EJMEFeVTm0F4heVfV6YVQVUMDwy850hEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=tX-X6QmkbvYX2gNaTFqwY8f3zrRrimTRmgz39zHbViu0NimayV-mhNeVGyAAJE4ztheJrjfO8CN6OqTJ-DvFVz_IuAg2pga72jgKJkpayfGnZVDnh0skDf_mxFKwR0aSjUfb04dLhwVGK7eBK71YLxZJOy6o2vigHSEpAeNHCHCw1pM14t-iAHXyIatUuU91WAoX0RdvICG1KsUFvXtUhniEqzy49yZBuBTQW0itPU8ssfeY1rQ9KM3pnPS-2EaQfvVSp-0W_fu2G7_dcPa3zTZG3i9uTruA2qGubhVX0PXZ4K4JTFa1EJMEFeVTm0F4heVfV6YVQVUMDwy850hEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20330" target="_blank">📅 22:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20328">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو :
طبق اسنادی که به دست آورده‌ایم ایران بار دیگر می‌خواهد برنامه هسته‌ای خود را از سر بگیرد و بمب اتم تولید کند و ما قبلا هشدار داده بودیم که اگر ایران برنامه هسته‌ای یا موشکی خود را دوباره شروع کند ما به آن حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20328" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20327">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20327" target="_blank">📅 22:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20326">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حمله ایران به یک کشتی بحرینی در خلیح فارس</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20326" target="_blank">📅 22:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20325">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20325" target="_blank">📅 22:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20324">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سناتور تد کروز:
چیزی که من خواستار آن هستم این است که رئیس جمهور ترامپ و دولت او معترضان را مسلح کنند تا مردم ایران بتوانند این کار را انجام دهند، کردها را مسلح کنند و به معترضان اجازه دهند این حکومت را از قدرت سرنگون کنند، نه با نیروهای آمریکایی در میدان، بلکه با مردم ایران.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20324" target="_blank">📅 21:43 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20322" target="_blank">📅 21:35 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/315342d71a.mp4?token=d5lFIME63zpvtHlKhbsmaspJwGLHVfBmJ0N9uMz3UiY-QmqRKGLNh8SEYOzXhVhQrJBJRhXLQ4VZ5XO4WTTpYhFLtaRe1YInL-qWTXRG0mK33ge35xiLTeMmBRAJ4eqmQak4OgrVndejaUJJi65YMdpJXDA-b1t_dJ19d0t5ch8zDF3_pra4tIQd7FU6mhGTOGMu5K8cYfwkdwxWT4aUbz-k9b1UX-jXBzxYwAeOFOH3P8P9Q2Dq4eFLiSH97Mkxdw7J9AwuRIoPqMCxO9dW96y3IVyxmQulh2A0dvqwRkhagyie1fc42PY8Pdee7sxtlXRaXkSc-w30MpYKFKX9fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315342d71a.mp4?token=d5lFIME63zpvtHlKhbsmaspJwGLHVfBmJ0N9uMz3UiY-QmqRKGLNh8SEYOzXhVhQrJBJRhXLQ4VZ5XO4WTTpYhFLtaRe1YInL-qWTXRG0mK33ge35xiLTeMmBRAJ4eqmQak4OgrVndejaUJJi65YMdpJXDA-b1t_dJ19d0t5ch8zDF3_pra4tIQd7FU6mhGTOGMu5K8cYfwkdwxWT4aUbz-k9b1UX-jXBzxYwAeOFOH3P8P9Q2Dq4eFLiSH97Mkxdw7J9AwuRIoPqMCxO9dW96y3IVyxmQulh2A0dvqwRkhagyie1fc42PY8Pdee7sxtlXRaXkSc-w30MpYKFKX9fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح یه خط فاضلاب
به مناسبت هفته دولت
اوج خلاقیت
فقط اون روبان قرمز روی شیر تانکر
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20319" target="_blank">📅 15:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20318">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRoDWqPSwlIL0XJcsAvXd-GsH5Hnp_EJQhHtrVMbfGysFcznB_YPSFr5aP6dv617pKZQlQRSKIJpCcW7EkzmA4HeOp3BjxC9AD8Bope_jTIBxwmYznANzAtwAz3ayC92dhKQLwUCNhZpfxKIF1nB9_kVUnyUHbWV888I9J-VB_TgRYeFYf7hs7OpYSVtk_vuLS0N03AeOHBxjkY_PSfWlLJDH4yASpUb0JwM1S7jGNP4ZO1eFeOAHNr12kxCYcK5VbVF2Fmxm70AceZFqUXkp4xK8J_-RXrGmmbyBB2X8J2pY3Hr5G8eUZED6KWZV5jFEHhqMhvAHAeK0XhxPi3EBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور سرباز وظیفه در درگیری مرزی در پاوه
مهرداد طاهری آرپناهی، سرباز وظیفه اهل شهرستان کوهرنگ چهارمحال‌وبختیاری، در جریان درگیری با اشرار در منطقه مرزی پاوه ترور شد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20318" target="_blank">📅 15:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عراقچی:   ژاپنی‌ها آمریکا را بابت جنایاتش پاسخگو کنند</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20317" target="_blank">📅 12:15 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20315" target="_blank">📅 12:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20314" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20313" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=tlABkbSwUuJLnHR5Q-z3jMO5K5gPYt3tIdtCurlH7gLyqltdYSfODRi81rU9NmjK2U_-NUK3_nfMr8eK89leVUuPN-6E4QRi3c27NRF4sDtoNBSouR2mp0jLe4MPG3zE8L-XTfldHm8hlHqohJ_2h_CfyR2QrfRiXCm3uQa7wMP3wCPnKSZnmftSl9RoB6Wz7j5s4x2Ba4nAAfvu3oVvsXqvMTTugue9jV8orbpi-4MUqGA2EtVZH4eQbKppY4mlq94CLtRuFOc5aDTMBMJWrQ7WyeaDqxlf-blm7pRYDVnXVlo4zUw1PBqYYYkWQfT3LjKIpeCzS4pT6uIVxciIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=tlABkbSwUuJLnHR5Q-z3jMO5K5gPYt3tIdtCurlH7gLyqltdYSfODRi81rU9NmjK2U_-NUK3_nfMr8eK89leVUuPN-6E4QRi3c27NRF4sDtoNBSouR2mp0jLe4MPG3zE8L-XTfldHm8hlHqohJ_2h_CfyR2QrfRiXCm3uQa7wMP3wCPnKSZnmftSl9RoB6Wz7j5s4x2Ba4nAAfvu3oVvsXqvMTTugue9jV8orbpi-4MUqGA2EtVZH4eQbKppY4mlq94CLtRuFOc5aDTMBMJWrQ7WyeaDqxlf-blm7pRYDVnXVlo4zUw1PBqYYYkWQfT3LjKIpeCzS4pT6uIVxciIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20312" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=QoNAsJdlS1AwDW6HKWsEUaWZVnAZ5A2nPm2ZXEEsUDW0iCZ1r5WaNH7pVArdWVIrCLfo4BOy-cbC_7j4t_x4dSFVn0t_MwUczTiMZbt-wbDwUVF20sUFLqooAwAw7Xa3C8tq1d0W6TVxzwqVuDS-xzDEZoNNQox5VigDmWoDhRDJ_BFGOI2gpDTmdzyfOZQSOpnab8JvvvI7mPJizi0R7wgAsfLyzv1Vzz6oE0GonH0zUWC1PrKqz770DG_E4C6AevIvPtNncNZ6QuKUSAzK6lhrXCco7dpfF6ZFbZkUZdoqnhAIV445CsV-YoqZ0Jm0U80zJhlGBq2bn6ZVN_WBvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=QoNAsJdlS1AwDW6HKWsEUaWZVnAZ5A2nPm2ZXEEsUDW0iCZ1r5WaNH7pVArdWVIrCLfo4BOy-cbC_7j4t_x4dSFVn0t_MwUczTiMZbt-wbDwUVF20sUFLqooAwAw7Xa3C8tq1d0W6TVxzwqVuDS-xzDEZoNNQox5VigDmWoDhRDJ_BFGOI2gpDTmdzyfOZQSOpnab8JvvvI7mPJizi0R7wgAsfLyzv1Vzz6oE0GonH0zUWC1PrKqz770DG_E4C6AevIvPtNncNZ6QuKUSAzK6lhrXCco7dpfF6ZFbZkUZdoqnhAIV445CsV-YoqZ0Jm0U80zJhlGBq2bn6ZVN_WBvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:
به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20311" target="_blank">📅 01:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOstBt96pkf2ab4XT44sS4g1TM7jI4y97hIxoszh6GqpU41npywpL-DsM8PLrxrm_-tSs7mtj-HgCKGJj8qs0YLhLdr1xyu6Pdpso6oIlBtwlfySrhMxH2hhvitxdyYuogeVRI9sN3nNFvGBI5oh0NSfe9rAZdN3T5MT406oBoGNDIhoZOM_DjguBdH_oDgXFgAOga1_4MiqETvqSs6itApgV_S4ENbCDYWlBWzb_V3YcUAzJDtYahZ9zkDeWGxwiusOD6Uwmr4oW_ueACNjoHKgs1NAAv7ycuD5-LIIoNwrR1wYH5Y1sF4YhH5NguiRPz7OB17jKvk9jGUvC97mDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20310" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20307" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7aX2ul-P5durDMkGIujT9PXL8xdOpYXSl6rjt9RaqjnUo8-h9MGCJOMkjNbYhwcwTlvX6K5rGJkU8R3jeuvy5Pb4jDSCz25y_KNVzQZBa_EyeVQhLIizuoXLRj14ZdNuo8gIHiPbsQcyrR7a6yeVuRQ_pr1GDJ1pyqGXlAUcEupbardgDkRr-AeOeQDlb3eHANdgfZbIKna4zjsF9QYVcQQws_EevXgWIlpQ76Q3QSe01QxDI6fZ7qVmE637yB-K1rfyKBKC308ghHhccqlmNuWwF3FmRz1WkUx_lQau7lgHOeuyZvD5JR_09wKPBFFPEvyc6-0Ld77tLPfGsZ0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه هشدار داده است که در پاسخ به حملات اوکراین به اهداف داخل روسیه با استفاده از موشک‌های کروز بریتانیایی، ممکن است به اهداف نظامی بریتانیا داخل و خارج از اوکراین حمله کند.  این هشدار، قوی‌ترین هشدار از این نوع تاکنون از سوی روسیه بود که توسط ماریا زاخاروا،…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20304" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20303" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXPN_nW78lzLYNZRXgdvLHh8yOQJP-212NPnCM7J_TFpLV9QKMHunAYajuO8OsZlLecPp-fTZqpcn0I9y3wFaSWr0B4A9ndtfuco2oXrOWBH0IYdohPPDdhk7_EK54-SfLE0CunTqDNwRX_vUcg5PA2uHYw62KlegaNpvAXOGak8G2F06HRM3VRxbJk49ujf7e5IUBxKDXFSB09cEokcY7Yxxa-Z3yV5YjQBVqLGyUWRAdriIgcPuUPC7TtXMenAxlvMvMBf4W4wjcm3IY8aFjxXg78kPaQuW_1uGjEaAge8xpcUKPH4DWhHhg1WGCXnxOD9fDLjIkwzqb97OgWgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!
علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20302" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20299" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20298">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20298" target="_blank">📅 15:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20297">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csWbgTn_zjBgVx5uz4IPS7NxLotMdg_yHhArSj_0n36MzqNa9F1-K8rdxuSemAO0wMf6gZ6zyVAYSkO5f7EhcYD9zknA3gZfZjzLo13LCnut1HfOgr2CkZU7UlA-AiJik6_ZNzl7WBurbt9EkdinlJfDL6iQjfIkrx24PnOX-8ee7TqE-IR1mFEVvcVV95ih80wiItvuu5rfOIx4CPg3w2L1pDxCAWxJjWg4ruK0hGpNx4A2AyTJWtAn1urFoC9_sKgmysU3k_4f15sMbatfhAP8F0YmIlYiiuFWVJgnJVAVqtDR0Q_RFchy3l9-NtlDCCH6SbrpwdPVr8a_9rQPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20297" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
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
