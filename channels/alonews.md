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
<img src="https://cdn4.telesco.pe/file/EqFI2UokJEolmIbK9pNbdtcJ1NZQQurgw03JUc5bzQVSn_7Zw_QFba2wIJaBfJ4Dv0k93QsTHbAUtxGlBPqQVt_3WYlG7Xi7sUmGrNWCYv6NTq6nIJk6N3eCwif8MSSwIUQTHeUQMsmzP7OQtVLvzlCVg0REnEWNabnNRfu6mwB3l9HNUZnogGONSsTN8RrhNI11N0J-I3HRGz7ouemnTT_TLadha9vbVlJHoXtU000ed42pKxxQWhs9hibs1eOyvTN7i_kri4jx4xX28LHZDSerfA9IUY8TJKQG6xVJlUFnos2CmCmGHNIuOiOMbkTnnAWuI6eo5mvl9-jDZf5aqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 22:46:24</div>
<hr>

<div class="tg-post" id="msg-132609">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
مقامات ارشد آمریکایی به CNN:
حملات آمریکا به ایران ممکن است در ساعات آینده آغاز شود، تیم امنیت ملی ترامپ در حال تصمیم گیری در مورد دامنه و گستردگی حملات آتی می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/132609" target="_blank">📅 22:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132608">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a187b5378.mp4?token=GytHCOWnYyQJL0nUJuh4sMIEfjq3E8eFs8OKL2231QCs6ERpg0YQ7UQL9sFyteJzrhicltQHhXcckAsaW7vQaYpxbY5LPN4VbLRPTdvYue9zTI2xEKkj-3uqGGedcwMejldT2BcUDRfhVIpp4q9ovjS1XYFHfriARtB_PKxkdXbgYG9j9tSix64B5kVf8doQqgbhbkz9vo8om12y2EupoFWmNZRvSQ1pqc2Ye6Vrmczfc827HlUMqVTGpVbqR-LGnzKpjTF9NpwQKQf5-B2N6HfHHg07dR5PLG5p-fUdXgH9cKLiwP8yMHopP1L0jzWUx1vUbE0o__W05fSduCxWNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a187b5378.mp4?token=GytHCOWnYyQJL0nUJuh4sMIEfjq3E8eFs8OKL2231QCs6ERpg0YQ7UQL9sFyteJzrhicltQHhXcckAsaW7vQaYpxbY5LPN4VbLRPTdvYue9zTI2xEKkj-3uqGGedcwMejldT2BcUDRfhVIpp4q9ovjS1XYFHfriARtB_PKxkdXbgYG9j9tSix64B5kVf8doQqgbhbkz9vo8om12y2EupoFWmNZRvSQ1pqc2Ye6Vrmczfc827HlUMqVTGpVbqR-LGnzKpjTF9NpwQKQf5-B2N6HfHHg07dR5PLG5p-fUdXgH9cKLiwP8yMHopP1L0jzWUx1vUbE0o__W05fSduCxWNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس گوشی خودشو چک میکنه تا ببینه ترامپ بهش زنگ زده، یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/132608" target="_blank">📅 22:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132607">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
به گزارش بلومبرگ، دونالد ترامپ در پایان اجلاس دو روزه ناتو در آنکارا خطاب به رهبران این سازمان گفت که «عشق و محبت» را احساس می‌کند؛ اظهاراتی که پس از دیدارهای فشرده او با سران کشورهای عضو ناتو مطرح شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/132607" target="_blank">📅 22:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132606">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
جی. دی. ونس، درباره ایران:
ما با ایران یک توافق انجام دادیم. بنابراین، این توافق بسیار ساده است.
🔴
اگر آنها به سمت کشتی‌ها شلیک کنند، ما به شدت به آنها پاسخ خواهیم داد، و این همان چیزی است که قرار است اتفاق بیفتد. این روش اساسی کار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/132606" target="_blank">📅 22:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132605">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ادعای العربيه: فرمانده ارتش پاکستان با مقامات ایرانی تماس گرفته است تا از تشدید تنش‌ها جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/132605" target="_blank">📅 22:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132604">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e556b8541.mp4?token=MsRoQYjsSJA5SlpdNMMIfp5Ehf6KNPhlWS_R65CtXIc76VQGu34pJ7Itha9YSF7G4OjjVAJ3UnuNfJMjinpd5wpNJ0IA8UoFWacr6MHUl6vsGnrh6JZ5q2XBmBywozJ3_9OQ-vOw-GZlURpfCnCLK8qFzElGcWlaQY5_ZtHEVldg4Sy2VCZjhIEpuckfDe4_4syEaAhU9svp762FXQj8L5TbffBTPfwopy6m--aXNKVfOtOTabjPFHWiHNfHe4si5J8SihrOd8CvMcr6N5Jah3McM1ZYuT9p4jBiDAWfx7RWYYlSlU279y6udl4n6PC42IS4gJlZ3cs644EjAj866g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e556b8541.mp4?token=MsRoQYjsSJA5SlpdNMMIfp5Ehf6KNPhlWS_R65CtXIc76VQGu34pJ7Itha9YSF7G4OjjVAJ3UnuNfJMjinpd5wpNJ0IA8UoFWacr6MHUl6vsGnrh6JZ5q2XBmBywozJ3_9OQ-vOw-GZlURpfCnCLK8qFzElGcWlaQY5_ZtHEVldg4Sy2VCZjhIEpuckfDe4_4syEaAhU9svp762FXQj8L5TbffBTPfwopy6m--aXNKVfOtOTabjPFHWiHNfHe4si5J8SihrOd8CvMcr6N5Jah3McM1ZYuT9p4jBiDAWfx7RWYYlSlU279y6udl4n6PC42IS4gJlZ3cs644EjAj866g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی. دی. ونس، درباره ایران: اگر ایران تلاش کند تنگه هرمز را مسدود کند، ارتش آمریکا واکنش نشان خواهد داد. این موضوع بسیار ساده است – این توافق است.
🔴
آنها می‌توانند از این توافق پیروی کنند یا دقیقاً همان اتفاقی که شب گذشته رخ داد، دوباره تکرار شود.
🔴
این وضعیت همینطور ادامه خواهد داشت تا زمانی که آنها این مسیر را باز کنند و از شلیک به کشتی‌ها دست بردارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/132604" target="_blank">📅 22:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132603">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
معاون ترامپ،ونس: رئیس جمهور ترامپ گزینه‌های زیادی در مورد ایران دارد و من دقیقاً به شما نمی‌گویم امشب چه اتفاقی خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/132603" target="_blank">📅 22:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132602">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ از کنگره خواست تا سوریه از لیست تروریسم خارج بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/132602" target="_blank">📅 21:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132601">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
اردوغان، رئیس‌جمهور ترکیه، در مورد همکاری با آمریکا در صنعت دفاعی: ما حتی در مورد اقداماتی صحبت کردیم که ترکیه می‌تواند در صنعت دفاعی برای همکاری با آمریکا انجام دهد.
🔴
این اقدامات چه می‌توانند باشند؟ ما در صنعت دفاعی، به ویژه در زمینه ساخت کشتی‌ها، در مورد این موضوعات صحبت کردیم و امیدواریم که به سرعت اقداماتی را انجام دهیم.
🔴
این اقدامات می‌توانند شامل ناوهای جنگی، زیردریایی‌ها و کشتی‌های کوچک‌تر باشند. ما در مورد همه این موارد صحبت کردیم، و آیا ترکیه می‌تواند این کار را انجام دهد؟
🔴
ترکیه می‌تواند این کار را در کارخانه‌های کشتی‌سازی خود انجام دهد. ترکیه از نظر توانایی، قادر به انجام این کارها است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132601" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132600">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ابراهیم رضایی: کشور های حوزه خلیج فارس مراقبت چاه های نفت و گاز هایشان باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132600" target="_blank">📅 21:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132599">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBAPgqC6gQ0zEuKTEbu_6KjdI2_4CLy_IRdy2ImgBuDzLaBelpkppFzYi7Sw_N2SxcrZfqdk5u2Up48Qrw64FMI_soQjJtacIMT1ov1SXlErEW6VXgDjW6LxGjCI4X8ANkBh_ISUCcrOQceKps1HWcV27EIv1DfXj6rCam2akL1I_EO6TxtyOoz6PTN8kK5pr2R0mEl_e0BL44N5IzH3xYfAd7_QxFcGIg8kDIRLRs78URShRScjJXgx-Cga_4PJHDQkrYHghjJ3Umz8Z-0op0zYpO2WHZPGtpVfUVKXudJGGbxL0Rs-ZGd6tl3IRRfgWU-gVTlJqr4htPkZTedE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: آمریکا ساختار توافق را نقض کرده ‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132599" target="_blank">📅 21:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132598">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVXuTIP1OtJ3jpcF1-ScRDCahrirbplGEeUDrfpNSn0turbLhns1iXxYTTPNgAzwuwL7RWF6rdXKD_Nge4juWlebjZEpT9z1GC8MfQ-W3EWPjZgX1Uy727sd6oExOkBiTw4sAV7zAKbi9Qk8s8YnYCEt3AnOOisn7td16FDkWjK6Yrir-2PNEaCwgV87SpWbChSexDTGuBj-eDx4T2BWht3SkbAb7PdyKicZyaCKQQWxC1-i0J-Vhg4cvKVRsvEVdRbBtZFluJ9qyVFjM456-gnlOwj1sL6qgRg_gycHBPM0WWFzWSSDIqoslCCjUD_-jsYjA8W33q8r1bp7eFx1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سوخت‌رسان‌های آمریکایی بر فراز خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132598" target="_blank">📅 21:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132597">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
به گزارش واشنگتن‌پست، دونالد ترامپ از ولودیمیر زلنسکی تمجید کرد و با لحنی مثبت از حملات عمقی اوکراین در خاک روسیه سخن گفت؛ همزمان به نظر می‌رسد یکی از درخواست‌های دیرینه کی‌یف برای تولید موشک‌های پدافندی پاتریوتِ طراحی آمریکا در خاک اوکراین در آستانه موافقت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/132597" target="_blank">📅 21:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ آنکارا رو به مقصد آمریکا ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132596" target="_blank">📅 21:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMFopm-9G1XQjyR2-muS48nBDkY0zGumVGmMhVaURxEOE9x1ZdOCCKM_zOt58v1-LtajKa8FTYTm_gJUezm_hzlB5Ds9lhNwmQsaBj8rMqsim_e2iaRIVNI8Y2BlPociri8NPi4t8Q062uITiAoh1BWNFA4VYY39o4I9fFDUrTiluBeAYLItPC-Vt8BIY34M6hwccO6RnDANbXqe5xlpnFH9G5AAvIPClSapbEFEmYWA5UF5XrTWkGZVzjV3wPb0WCuuDPwRI1D3wH0ZB6K_3dcXxjWLe7zQ4YeySi8u-zNCUM0YMZhaafiapSIwM97Qyc-pxzMNhB5DnAcTFVZrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله رسایی به تیم مذاکره کننده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132595" target="_blank">📅 21:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132594">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کان نیوز: بازگشت سوخت رسان های آمریکایی به منطقه آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132594" target="_blank">📅 21:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132593">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان در نشست ناتو در آنکارا: ما به عنوان ترکیه، نتوانستیم همان‌طور که دوستان اروپایی‌مان توانستند، از سود صلح پس از جنگ سرد بهره‌مند شویم.
🔴
بسیاری از بحران‌ها و درگیری‌ها در همسایگی نزدیک ما رخ داد.
🔴
زمان‌هایی بود که تنها رها شدیم و با رفتارهای ناعادلانه مواجه شدیم.
🔴
اغلب اوقات مجبور بودیم به تنهایی از خود دفاع کنیم.
🔴
امروز، از نظر هزینه‌های دفاعی، توانایی‌های نظامی و قدرت صنعت دفاعی، ما از بسیاری از متحدان خود پیشی گرفته‌ایم.
🔴
رئیس‌جمهور ترامپ همچنین تأکید کرد که میزبانی کشور ما از این اجلاس در تصمیم او برای حضور نقش تعیین‌کننده‌ای داشت.
🔴
همچنین به‌ویژه معنادار بود که او بر دوستی شخصی ما تأکید کرد.
🔴
دوست عزیزم را بابت توجه و ملاحظه‌اش یک‌بار دیگر تشکر می‌کنم.
🔴
فخر ما، نیروهای مسلح ترکیه، قدرت و توانایی خنثی‌سازی هرگونه تهدیدی علیه امنیت ملی خود را در اصل و ریشه آن دارد.
🔴
ما در حال حاضر فرماندهی و مدیریت دومین ارتش زمینی بزرگ ناتو را بر عهده داریم.
🔴
برای دهه‌ها، امنیت باله جنوبی-شرقی ناتو عمدتاً به کشور ما سپرده شده است.
🔴
ترکیه به حق این اعتماد را پاس داشته است.
🔴
جنگنده‌های اف-۱۶ ما از ماه اوت به عنوان بخشی از مأموریت گشت هوایی ناتو در استونی مستقر خواهند شد.
🔴
ما فرماندهی عملیات کفور ناتو در کوزوو را که در ماه اکتبر بر عهده گرفتیم، تا پایان سپتامبر ۲۰۲۶ ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132593" target="_blank">📅 21:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132592">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ادعای سازمان پخش اسرائیل: نتانیاهو و ترامپ در حال مذاکره مستقیم در مورد تنش‌ها با ایران هستند
🔴
ایالات متحده در ساعات اخیر شروع به اعزام مجدد هواپیماهای سوخت‌رسانی به اسرائیل و خاورمیانه کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132592" target="_blank">📅 21:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132591">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loOtt_Ke6FkHuQRdXrEwDe_Nf27CR4covpOD_77GoIr8rZpzS0LOrrl3Cb77lnS-uDs9nfMxXfIimwks_T1LYd6lwKq1_I1IaVqz31_0rWG2NiL5rUcirshTZDMsIGPvcqK8Bw5O1ugNI5uvpGYU39qBLLoL16ARr2hh6Q_zI1tL40plo6KQZP_LukJQnaAJGjoFS5mfnXQ4-rqnPPK7lell9dUgVYXpcgsmDQQcKvp4tJ0aXiTmOIrjzDpNVnbP5HpKfj8MXvLEGfnmqK-XOhGokunNEEBm6U31ZpaOpdyrHKekvog6a9oS8aH57OKBzwVA_xizkdoLSzFyqn0F9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه، عراقچی : اینکه به ملت بزرگ و متمدن ایران توهین کنن
🔴
چیزی از بزرگی این مردم کم نمی‌کنه، ایرانی‌ها به فرهنگ، ادب و ارزش‌های اخلاقی‌شون شناخته میشن
🔴
ما جواب بی‌احترامی رو با بی‌احترامی نمی‌دیم؛ جواب ما عمله، با شجاعت و بدون ترس
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132591" target="_blank">📅 20:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132590">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سازمان ملل: از تنش های پیش آمده در خاورمیانه عمیقا ابراز نگرانی میکنیم و خواهان صلح فوری هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132590" target="_blank">📅 20:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132589">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کارشناس شبکه ۱۲ اسرائیل :  تبادل آتش تو خلیج فارس؛ ادامه مذاکرات از طریق روش‌های دیگ‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132589" target="_blank">📅 20:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132588">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ضرغامی: رئیس جمهور فاسد آمریکا را در ترکیه ترور نکردیم؛ به دلیل حفظ دوستی و حسن همجواری
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132588" target="_blank">📅 20:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132587">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d05cb3f5.mp4?token=u6hWPIp7wDiQVnJlma2RdFi10T76pbTexFAVO133ZCm8zcobGhSF3lqi00ok6Mk6PSd7pm6727GqAjVaB9YYWeXjCGrteDW-CS8Mko5S4eK-4dQxsWbD1Da8zQgEIyhkkOFrUMTqp7ipdCUId34dV4zPq2GcsRYuyuQWkCE2GZlao_wFbrsSAUB3gE3DT82aPHYbGqtjVRKw9o9gh_rV9k8ymUYmMi0GEQjps4qsbIGTz0QFygj5hJT022EeDzlxD43INvhS5D381IrPf5-WaVJSGbSmawsW0JFVJnx7k6FQ0-aGfasMwibV-mxtaHkvO-bpiursqgwnVuzt4jUg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d05cb3f5.mp4?token=u6hWPIp7wDiQVnJlma2RdFi10T76pbTexFAVO133ZCm8zcobGhSF3lqi00ok6Mk6PSd7pm6727GqAjVaB9YYWeXjCGrteDW-CS8Mko5S4eK-4dQxsWbD1Da8zQgEIyhkkOFrUMTqp7ipdCUId34dV4zPq2GcsRYuyuQWkCE2GZlao_wFbrsSAUB3gE3DT82aPHYbGqtjVRKw9o9gh_rV9k8ymUYmMi0GEQjps4qsbIGTz0QFygj5hJT022EeDzlxD43INvhS5D381IrPf5-WaVJSGbSmawsW0JFVJnx7k6FQ0-aGfasMwibV-mxtaHkvO-bpiursqgwnVuzt4jUg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خنده های معنادار مارکو روبیو پشت سر ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132587" target="_blank">📅 20:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132586">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KARvNoSoAPRBVCADGYMjk89PaQesZEnr9U8evT-DIuERw3U_8W_FY_sM81T1gYgl8Q8f1jat3DiFA_uaSQ6sfI7Hl53xx6FpMLxIIr5-HhN6pt4lZi_zsuoxG9pyv4LXz-64a_liTJYPH5eTJwDYWvPv2sSF7X3W-ObTwjfkn1xjvku00MoV4ZaDmPYhaezscAVYoukHW-oMEjH5ZfCkAe30kE46CZ2sdLy0qpJFBJpCEDIUnqJ3Lt2OWltfENmeaw7XmWX82PkhlS-6Hr8hEjL7YPpUbgMTXOPRXj6X7gLS2lMu0GUfUo1cia11Hhf9O0UfOuEPrI4YIwQB_m0VCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: تفاهم‌نامه را آتش بزنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132586" target="_blank">📅 20:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132585">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0t3wc8-EWhUL67tkzzuhYaDCAmopO09EuINScLzgn__o2cHr5YdqHs0TpQ5MO92XiPWWOqBNIftkEPXqK0KlewukufvrL0P6L0VS5r9Fxk7xjYz4Oz56fugzRRtlIEI_GuokboVcSnvLuQD8FAFmHyXJGFNaqLnYaL_GJf8JAHrrjpXkNL-kvtu2lPWRJWCrVk6mXLF8yPhEW3ONgofGIa1Xg1dJzVCfjJ7MlPYF1Twz_gcBDUDN6JyNvPohGaqeCaRON9KGAux94yaQNJP_Xrga7UNzjLS5Lk7EKwE7Y4qyxbISLJL4s6bPtb__ic77DHU7napKAzDkA73J5kIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: میانجی‌ها در حرکتی مهم برای جلوگیری از هرگونه تنش بین تهران و واشنگتن، و ارزیابی این است که میانجی‌گری‌ها ممکن است در مأموریت‌های خود موفق شوند و طرف‌ها به اجرای مفاد یادداشت تفاهم بازگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132585" target="_blank">📅 20:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132584">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
گزارش جروزالم‌پست، امانوئل مکرون گفت ایران با حمله به پایگاه‌های خلیج فارس، توافق خود با آمریکا را نقض کرده است؛ با این حال او تأکید کرد انتظار دارد مذاکرات آتش‌بس ۶۰ روزه همچنان ادامه پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132584" target="_blank">📅 20:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132583">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: ترکیه بسیار قدرتمند است. این کشور دومین کشور قدرتمند در ناتو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132583" target="_blank">📅 20:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132582">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ در مورد دادن F-35 به ترکیه:
هنوز کاملاً تصمیمم را نگرفته‌ام، اما تمایلم این است که بگویم: «او همه کارها را انجام داده است. او به روش‌های بسیار متفاوتی به ما کمک کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132582" target="_blank">📅 20:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132581">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69062797bd.mp4?token=V6sVRG0W1agZ1MHWaHzqbPG_8rvB8OKrAnmndAIPfa_x_DeAN2FkxGt8uL-SOeaLU0fS-sRKaw7JbBdKx6CmlniB-Fq60QIf9VFLes6BloF5_qCl6ViLQayFg6WpGcAQqbFcFiM0v0uKvhiCdjP90zzlkBj95ZYwuS7nWJFJUrWEatAQNQPMxyl1jShsoxHySGqHJKVXV7XIgrj3NsFH5SlQErosym60E9eZyMkTeFYGTdm0HjVg2zVIqzrdrTVHVNA2OVQw02x-XQ0Yda5bzgqTRcqiI4ExZnS_SVHVHesrmQaxh6TG5qVCYVvICXS0tyd-sQYkoQ6BhBrGcFa76A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69062797bd.mp4?token=V6sVRG0W1agZ1MHWaHzqbPG_8rvB8OKrAnmndAIPfa_x_DeAN2FkxGt8uL-SOeaLU0fS-sRKaw7JbBdKx6CmlniB-Fq60QIf9VFLes6BloF5_qCl6ViLQayFg6WpGcAQqbFcFiM0v0uKvhiCdjP90zzlkBj95ZYwuS7nWJFJUrWEatAQNQPMxyl1jShsoxHySGqHJKVXV7XIgrj3NsFH5SlQErosym60E9eZyMkTeFYGTdm0HjVg2zVIqzrdrTVHVNA2OVQw02x-XQ0Yda5bzgqTRcqiI4ExZnS_SVHVHesrmQaxh6TG5qVCYVvICXS0tyd-sQYkoQ6BhBrGcFa76A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: از کدام رسانه‌ای؟
🔴
خبرنگار: MS NOW.
🔴
ترامپ: اون یه شبکه رو به افوله. چرا دلت می‌خواد برای اونا کار کنی؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132581" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132580">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ: اردوغان طرفدار بزرگ بی‌بی‌ و اسرائیل نیست.
🔴
اما از آن جنگ دوری کرد.
🔴
او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من از آن جنگ دوری کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132580" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132579">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: من شماره یک لیست ترورِ جمهوری اسلامی هستم.
🔴
واقعاً برام مهم نیست، دارم کارم رو انجام میدم
🔴
فکر نمی‌کنم جنگ ایران دوباره شروع شود
🔴
هر اتفاقی قرار است بیفتد، بسیار سریع خواهد افتاد. ما به دنبال بلندمدت نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132579" target="_blank">📅 20:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132578">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: من شماره یک لیست ترورِ جمهوری اسلامی هستم.
🔴
واقعاً برام مهم نیست، دارم کارم رو انجام میدم
🔴
فکر نمی‌کنم جنگ ایران دوباره شروع شود
🔴
هر اتفاقی قرار است بیفتد، بسیار سریع خواهد افتاد. ما به دنبال بلندمدت نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132578" target="_blank">📅 20:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132577">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a722cf540b.mp4?token=PtyGLNGEr-Ksfb0NGXTv94vunBgWR5F3JhGwyvO4ykfusvfR9_ObKwbwMPuN-Xs14Phd_wEmbMC7Rpn6RfFPwPak6DCpYUD75bmH2A3BP4VSN2eunKRBi7f-Wa4sdkihCXJ3OZ4y46xUZDBi51y1S7E7RVW2ZYBJqh2Es8nwWlktbTZKMvkz_h0Al8YCPNpwj1ZeWsLuBrypy-_ZwWIir_tZPKdJskDSL0p0SdYoNbpx6-tyqvY_B93MAyZQV-zJjFjO5XOXwuBWv1_2npq51PwZiulrmxgQ_5oG5LCjFhqLRSVO-hB0VfWbjCxde1fynVqoDlh9CEG2X_tp6yd4yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a722cf540b.mp4?token=PtyGLNGEr-Ksfb0NGXTv94vunBgWR5F3JhGwyvO4ykfusvfR9_ObKwbwMPuN-Xs14Phd_wEmbMC7Rpn6RfFPwPak6DCpYUD75bmH2A3BP4VSN2eunKRBi7f-Wa4sdkihCXJ3OZ4y46xUZDBi51y1S7E7RVW2ZYBJqh2Es8nwWlktbTZKMvkz_h0Al8YCPNpwj1ZeWsLuBrypy-_ZwWIir_tZPKdJskDSL0p0SdYoNbpx6-tyqvY_B93MAyZQV-zJjFjO5XOXwuBWv1_2npq51PwZiulrmxgQ_5oG5LCjFhqLRSVO-hB0VfWbjCxde1fynVqoDlh9CEG2X_tp6yd4yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به محمدباقر قالیباف:
محمد چیزی آنجا با بیل‌هاست.
🔴
بیل‌ها شما را به آنجا نمی‌رسانند. بزرگترین ماشین‌آلات جهان شما را به آنجا نمی‌رسانند
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132577" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132576">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b19994818c.mp4?token=EQKG037YPEszzmZCgEBMh6LjB6uUXsZnnj657-Ctq00dDhaPEMf0WsdQdQjmMxL8zBfgpfqbAwdqUrOR75hO58UW8-cIPQqkVYmMOq4kzK8C5_QRCsaIFUYRwpBLUDCOust25NpTN_vr9_4rPJqT2hCV0ov8NbXpV26xJDdFF2tflEbM7JfRYHe4-8zqvKc6lXy1yUrGhCkGQR3mAZh6r8E99R4uToE0NFamNJay3WyQTLe0_TMgamkd22WdMp19N1Ci_WoWyX6OOB0yRIG14Saq2XhuN6QOgZHlQHUlsfAPcE20vp_7UGVkl2uqhkhM-n2mi2Aout1FHm7Mlk7BNx10QASkaLJzryBJuCVopPGX0CZMCsn156zINyPMvBrn86PfnjjeuxCsko4sNbzEhDoeEAS31zBz-Xzy5RGCsI8hHuLHl3fR0W-oJgQhbjFDPCk7Qd70EOHC0ycWCcQVLUbxFRZJA3JDCn24a3M1mWoFW2Xi9XUcgEQMELAyHd3v9QJv6MQvGehs1ZrnnJuvsQU-zPq_f5XU5lZn1n4W8OiTvGpqnd4nDCVuW_uObdKZRVfvBPoCGSiAlP0XNEeoXx5OVxXyrOgZHxuErqIxB2t97sSc-4jRYcrzSfjSpj39M5Mk6A1_GFIHxLt2KmGnJRb-BJpMiQhaIQ6TgXE5TD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b19994818c.mp4?token=EQKG037YPEszzmZCgEBMh6LjB6uUXsZnnj657-Ctq00dDhaPEMf0WsdQdQjmMxL8zBfgpfqbAwdqUrOR75hO58UW8-cIPQqkVYmMOq4kzK8C5_QRCsaIFUYRwpBLUDCOust25NpTN_vr9_4rPJqT2hCV0ov8NbXpV26xJDdFF2tflEbM7JfRYHe4-8zqvKc6lXy1yUrGhCkGQR3mAZh6r8E99R4uToE0NFamNJay3WyQTLe0_TMgamkd22WdMp19N1Ci_WoWyX6OOB0yRIG14Saq2XhuN6QOgZHlQHUlsfAPcE20vp_7UGVkl2uqhkhM-n2mi2Aout1FHm7Mlk7BNx10QASkaLJzryBJuCVopPGX0CZMCsn156zINyPMvBrn86PfnjjeuxCsko4sNbzEhDoeEAS31zBz-Xzy5RGCsI8hHuLHl3fR0W-oJgQhbjFDPCk7Qd70EOHC0ycWCcQVLUbxFRZJA3JDCn24a3M1mWoFW2Xi9XUcgEQMELAyHd3v9QJv6MQvGehs1ZrnnJuvsQU-zPq_f5XU5lZn1n4W8OiTvGpqnd4nDCVuW_uObdKZRVfvBPoCGSiAlP0XNEeoXx5OVxXyrOgZHxuErqIxB2t97sSc-4jRYcrzSfjSpj39M5Mk6A1_GFIHxLt2KmGnJRb-BJpMiQhaIQ6TgXE5TD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مواد هسته‌ای ایران:
ما دوربین‌هایی داریم که بخشی از نیروی فضایی ما هستند و می‌توانند نشان شناسایی افرادی را که به یک محل خاص می‌روند، بخوانند. [نامی]، به نظر می‌رسد که چیزی با استفاده از بیل در آنجا وجود دارد
🔴
بیل‌ها به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند. این موضوع بسیار، بسیار عمیق‌تر است.
🔴
اما ما این موضوع را زیر نظر داریم و اگر کسی به آنجا برود، منفجر خواهد شد
🔴
بنابراین، هیچ‌کس به آنجا دست نخواهد زد. در نهایت، ما آن را تصاحب خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/132576" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132575">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10af6b9606.mp4?token=uEXAnYzSZrYVh8DVEcpXW5aPDLcft_NrnB_DGjubufe-XZb1gqLJI1rcVBGnW-DB3ROi4-2N1fbL0E_6xfMxYBA9pPFnclLxpqXhEk7SGrRR_sEO1Fsf2VsjSCj_OjxwmCXjDnn5w__ZLokInTQWgPF19m4g-T7yYcKR6iIWpGeSPCbFWypGmMxav9SW77sZBCm9pc0QDAAf-VIcTNjO7hK8Qn7FfXS5CtemSUeCYDeU9pik6dSzJTsjflK-BWTaczLJFaDiLO5o08bujRNT5ju1Udm5jVttE9ebZdDTlhSN8rZ1IoGzmUVN8KcRhcNPQW0clzOVoIxm6-pk7-tlYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10af6b9606.mp4?token=uEXAnYzSZrYVh8DVEcpXW5aPDLcft_NrnB_DGjubufe-XZb1gqLJI1rcVBGnW-DB3ROi4-2N1fbL0E_6xfMxYBA9pPFnclLxpqXhEk7SGrRR_sEO1Fsf2VsjSCj_OjxwmCXjDnn5w__ZLokInTQWgPF19m4g-T7yYcKR6iIWpGeSPCbFWypGmMxav9SW77sZBCm9pc0QDAAf-VIcTNjO7hK8Qn7FfXS5CtemSUeCYDeU9pik6dSzJTsjflK-BWTaczLJFaDiLO5o08bujRNT5ju1Udm5jVttE9ebZdDTlhSN8rZ1IoGzmUVN8KcRhcNPQW0clzOVoIxm6-pk7-tlYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من همه چیز را پیش‌بینی کردم. من مدت‌هاست که در مورد همه چیز درست گفته‌ام.
🔴
به همین دلیل است که من سه انتخابات را برده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132575" target="_blank">📅 20:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132574">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / ترامپ : من مطمئن نیستم که بخواهم با آنها معامله‌ای انجام دهم.
🔴
فقط بیایید کار را به پایان برسانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132574" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132573">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ : قیمت نفت کمی افزایش یافته و دوباره کاهش خواهد یافت
🔴
رهبران ایران اکنون منطقی‌تر شده‌اند
🔴
ایرانی‌ها به کشتی‌های ما حمله کردند، بنابراین ما با حملاتی ده برابر قوی‌تر پاسخ دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132573" target="_blank">📅 20:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132572">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c735101f5d.mp4?token=fQww-MFGyqLEQ9rwc4xJl5PgYHH5UbvY8VmymPtLh7yDI-e-SUq9E9_utpCdhE7_xxjGjNDS2k1garemxnjkV86ZJGO-Xh1JKFUph8_rXeDIEz3wAoov_25fcg1ywGcMCwCtKBaiwfv7u10R-rSEPUQAOFBHalHTEToGRQPswAcrVl6k_DFjZSWIzLfh6r4VKUjnLhyGdhRidFMDFc7ppv9pi0kpMVbA4Dd64Jcm9p3t68MeHe3r0brGNY_VxIQjrgkjOwPM3bzc-_Ppq45zG86xMX91Sk3s2m4lxAWbVjU7pHpfYWtRVAXKOLhwN477JQjYg78XTuRkXhpXKCiQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c735101f5d.mp4?token=fQww-MFGyqLEQ9rwc4xJl5PgYHH5UbvY8VmymPtLh7yDI-e-SUq9E9_utpCdhE7_xxjGjNDS2k1garemxnjkV86ZJGO-Xh1JKFUph8_rXeDIEz3wAoov_25fcg1ywGcMCwCtKBaiwfv7u10R-rSEPUQAOFBHalHTEToGRQPswAcrVl6k_DFjZSWIzLfh6r4VKUjnLhyGdhRidFMDFc7ppv9pi0kpMVbA4Dd64Jcm9p3t68MeHe3r0brGNY_VxIQjrgkjOwPM3bzc-_Ppq45zG86xMX91Sk3s2m4lxAWbVjU7pHpfYWtRVAXKOLhwN477JQjYg78XTuRkXhpXKCiQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی در سه ماه گذشته ۵۲,۰۰۰ معترض را کشته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132572" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132571">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c1f3d00e.mp4?token=fNGDhT8zvkv3uuRgPmFFuqwVIBWAj7GkT9v8aVNPN6IzbJatWDBft4oK0HYBsQKJMjCwq6VW0JiREo6Wu2gau-jXzb8LqA4Cm4QkRXtwgQzt1S94-iC_iUB3pVzGmCdaHw07az--Ma_mEAS-WSEkFkvdXZKNFFttCkTioA6Jj5nLbfKxzqHPt5nHNl82e3R4R8cVX0a8alZKmK4rPmh23rW5WYK2OAJhAuspl1C5btNJFiduK2uQoV_Hbh7OW5Svqfsx7VIMMg5rY8QDr5UXOebisrmIc9DcJfgahgHH4vMgYTRjJhkArfIGPyCdgaZkr-gE1iHZ8SUSedk8CU4byA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c1f3d00e.mp4?token=fNGDhT8zvkv3uuRgPmFFuqwVIBWAj7GkT9v8aVNPN6IzbJatWDBft4oK0HYBsQKJMjCwq6VW0JiREo6Wu2gau-jXzb8LqA4Cm4QkRXtwgQzt1S94-iC_iUB3pVzGmCdaHw07az--Ma_mEAS-WSEkFkvdXZKNFFttCkTioA6Jj5nLbfKxzqHPt5nHNl82e3R4R8cVX0a8alZKmK4rPmh23rW5WYK2OAJhAuspl1C5btNJFiduK2uQoV_Hbh7OW5Svqfsx7VIMMg5rY8QDr5UXOebisrmIc9DcJfgahgHH4vMgYTRjJhkArfIGPyCdgaZkr-gE1iHZ8SUSedk8CU4byA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي : «می‌دانید چیست؟ شاید من هم تا آن موقع دیگر نباشم. من هدف شماره یک آن‌ها هستم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132571" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132570">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری /  ترامپ: میخواهم پرونده ایران را یکبار برای همیشه تمام کنم، نه اینکه با رهبران فعلی بازی کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132570" target="_blank">📅 20:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132569">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e090ee0c.mp4?token=Qrj0hVhQ7DunBpx_3ocyjzMRXafoKnA9r5U5wuJ9avMvbkPpP7j1GG8y7ewliNaaQTqEOTtauXURudjkFGwmdeoTq9T4RAzvSkLZ1cL-R9rgS8cRrWoddCRWx4VoFy1xGJU7thZ_Tk75nFpExBTkf8MbuigLy2OxPiN9uazJ9bitjEGrL6llB4Ausdwc9EyVC9AuNnWZvQCddBKL47z-HkAH3eo5Q_m-t_4R-7owB6YqQ23zbJnH9tXbI7KurTNlLiDQY0d3sGkbpUTJFB77e47sgJsmmV3_RvDDmK6bIho1UvQ6RB2iOYW8Yx8ShmzamHbd-FyhJZiG3VD_YwQCMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e090ee0c.mp4?token=Qrj0hVhQ7DunBpx_3ocyjzMRXafoKnA9r5U5wuJ9avMvbkPpP7j1GG8y7ewliNaaQTqEOTtauXURudjkFGwmdeoTq9T4RAzvSkLZ1cL-R9rgS8cRrWoddCRWx4VoFy1xGJU7thZ_Tk75nFpExBTkf8MbuigLy2OxPiN9uazJ9bitjEGrL6llB4Ausdwc9EyVC9AuNnWZvQCddBKL47z-HkAH3eo5Q_m-t_4R-7owB6YqQ23zbJnH9tXbI7KurTNlLiDQY0d3sGkbpUTJFB77e47sgJsmmV3_RvDDmK6bIho1UvQ6RB2iOYW8Yx8ShmzamHbd-FyhJZiG3VD_YwQCMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد توافقی انجام دهد، اما نمی‌داند چگونه توافق کند.
🔴
و سپس شب‌ها به کشتی‌ها شلیک می‌کنند. من آن را دوست ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132569" target="_blank">📅 20:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132568">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3852511a3f.mp4?token=IamPQC-QANBL1ZifQPQskPoJNHO9IL38906_680egDsywZ6izJLDACET1IrViU9n-Oah4QA6FxUUtK9W413tLpod4JjaPmmbV8cu0HwRzN5xP4cC71w3Ux7byKIT6GQD8Tu4zV8fdSIWspI5vYGFtikQEFJLQQYyFlU-08pmPTLu7rfbNi_tbwEWNYvp-cwnj1S0_4h2e5FhbVguJ9vfyJnIZ76KnDk658_jsKUiUmf_2sjW9tAWgpt4cM9D0Ovh1u5EQ2hQcA2kqFVVxn5WYd5vaHRVOpQfgU59iDj5BpIiddXO1rz6sMunWGvDxPInTzSGsCd7titAg5eTKJHD2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3852511a3f.mp4?token=IamPQC-QANBL1ZifQPQskPoJNHO9IL38906_680egDsywZ6izJLDACET1IrViU9n-Oah4QA6FxUUtK9W413tLpod4JjaPmmbV8cu0HwRzN5xP4cC71w3Ux7byKIT6GQD8Tu4zV8fdSIWspI5vYGFtikQEFJLQQYyFlU-08pmPTLu7rfbNi_tbwEWNYvp-cwnj1S0_4h2e5FhbVguJ9vfyJnIZ76KnDk658_jsKUiUmf_2sjW9tAWgpt4cM9D0Ovh1u5EQ2hQcA2kqFVVxn5WYd5vaHRVOpQfgU59iDj5BpIiddXO1rz6sMunWGvDxPInTzSGsCd7titAg5eTKJHD2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد تورم موجود در ایران: تورم آن‌ها ۳۵۰ درصد است. وقتی جنگ شروع شد، ۵ تا ۶ درصد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132568" target="_blank">📅 20:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132567">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: جنگ علیه ایران یک موفقیت نظامی بود
🔴
ایرانی‌ها دنبال توافق بودند، بعد به کشتی‌ها شلیک کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132567" target="_blank">📅 20:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
پرس‌تی‌وی به نقل از یک مقام ایرانی:
تحولات ۴۸ ساعت گذشته، عزم تهران را مستحکم‌تر کرده و یک دکترین نظامی و راهبردی جدید به اجرا درآمده است.
🔴
هر تهدیدی با پاسخی قوی مواجه خواهد شد. ایران بین ایالات متحده و همپیمانانش در منطقه تفاوتی قائل نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132566" target="_blank">📅 20:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8fc7e935.mp4?token=CV9uB3LQlSwThT9GngeRIw54baht32f3wnUcIkbqiLDJMyLpSNHOcBuHJu6bAXgIt_U0VvUodLui6RgphZx1bhuCTer2HcIpdL2kEydOe6PPKo9bEXb4bubpJ9O-mQbPiZzfKEkoXgoYHb6jsf5usRim9098ThnAB4sJ0UIF0EOEa2C_NwISDxA1yMgk-2B_K2hieDxM3l5SbgrLFDjS1dXfbSTqTbQkr5WNXBdBoSchR0b1fng6LSGGM_bK1fq2odILoqD_epnt-NOV-PQkzMA371RHn3jlEFZJqjV64GyU015cxfkEX4KBRkAWFOQ8-nxCd8nWpUVlEZmNDh3Agg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8fc7e935.mp4?token=CV9uB3LQlSwThT9GngeRIw54baht32f3wnUcIkbqiLDJMyLpSNHOcBuHJu6bAXgIt_U0VvUodLui6RgphZx1bhuCTer2HcIpdL2kEydOe6PPKo9bEXb4bubpJ9O-mQbPiZzfKEkoXgoYHb6jsf5usRim9098ThnAB4sJ0UIF0EOEa2C_NwISDxA1yMgk-2B_K2hieDxM3l5SbgrLFDjS1dXfbSTqTbQkr5WNXBdBoSchR0b1fng6LSGGM_bK1fq2odILoqD_epnt-NOV-PQkzMA371RHn3jlEFZJqjV64GyU015cxfkEX4KBRkAWFOQ8-nxCd8nWpUVlEZmNDh3Agg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در آنکارا: اندوریل در حال اعلام یک توافق برای ساخت موشک‌های جدید باراکودا خود است.
🔴
ما این کار را برای لهستان انجام می‌دهیم. لهستان با داشتن یک رئیس‌جمهور عالی، بسیار پیشرفت کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132565" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: امروز، بیش از ۲۰ کشتی جنگی نیروی دریایی ایالات متحده در سراسر آب‌های خاورمیانه گشت‌زنی می‌کنند در حالی که نیروهای سنت‌کام به ترویج امنیت و ثبات منطقه‌ای ادامه می‌دهند.
🔴
ماه گذشته، کشتی‌های جنگی دریایی و هواپیماهای ایالات متحده در نزدیکی هم از دریای عرب عبور کردند و قدرت نظامی و آتش بی‌نظیر آمریکایی را به نمایش گذاشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132564" target="_blank">📅 19:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: کمونیست‌ها خدا را نمی‌خواهند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132563" target="_blank">📅 19:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae48e0068.mp4?token=smJP8C4EuRuq92ZYwRi2gV1s_L55l4Rh6hPOwe8AVD565TZEFqpgVpRVtOpIImjB9duRstV7palHzJz_EFEq-xSemXVnX5-ILR6SNBG6aOuNGU8yUSo6S4jyyfXNhAwd2N1LyBDCxvjdS8EEvr9dIw5811AXq-8pZIW2UKPW8RH-liczLcqLj8FjIV-B5S2MgCbVW4jjg_t_3scsNBbwM5wmCkpyCMw3rDhp7DEoDDziuI5_et6KX5DKO5BXufu9mg9O6WtfiiNrtzZ-IKVMQ36hd66ZLNIsVqmGSTY73kqQU9NTbO0_9zJest1mgWOn8CCZhoSJgYWxaglfh-T71A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae48e0068.mp4?token=smJP8C4EuRuq92ZYwRi2gV1s_L55l4Rh6hPOwe8AVD565TZEFqpgVpRVtOpIImjB9duRstV7palHzJz_EFEq-xSemXVnX5-ILR6SNBG6aOuNGU8yUSo6S4jyyfXNhAwd2N1LyBDCxvjdS8EEvr9dIw5811AXq-8pZIW2UKPW8RH-liczLcqLj8FjIV-B5S2MgCbVW4jjg_t_3scsNBbwM5wmCkpyCMw3rDhp7DEoDDziuI5_et6KX5DKO5BXufu9mg9O6WtfiiNrtzZ-IKVMQ36hd66ZLNIsVqmGSTY73kqQU9NTbO0_9zJest1mgWOn8CCZhoSJgYWxaglfh-T71A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در آنکارا
:
لاکهید و راینمتال شراکتی را برای ساخت سیستم‌های موشکی تاکتیکی ارتش اعلام کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132562" target="_blank">📅 19:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ در آنکارا: مارک روته کار باورنکردنی انجام داده است؛ نمی‌توانستم کسی بهتر از او پیدا کنم.
🔴
فقط می‌خواهم بگویم که در آن اتاق عشق فراوانی وجود داشت. در واقع گفتم که متاسفانه مطبوعات نتوانستند این صحنه را ببینند، زیرا هر یک از آن‌ها برای مدتی کوتاه صحبت کردند و من نیز مدتی کوتاه صحبت کردم.
🔴
آن‌ها افراد بسیار باهوشی بودند و قلب‌هایشان سرشار از خوبی است، نه بدی، بلکه خوبی.
🔴
تجهیزات ما کار می‌کند، اما باید آن را سریع‌تر برای همه، از جمله خودمان، تولید کنیم.
🔴
فکر می‌کنیم در عرض یک سال — حداکثر یک سال و نیم — به جای اینکه یک یا دو سال صبر کنیم، آن را با دو هفته انتظار، شاید حتی یک هفته انتظار خواهیم داشت. این همان چیزی است که می‌خواهم. و واقعاً خوب عمل خواهد کرد.
🔴
بسیاری از مردم فقط در حال انتظار هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132561" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: ایالات متحده همچنان با اختلاف بسیار، بزرگترین کمک‌کننده به ناتو است.
🔴
رهبران ناتو گفتند: «قربان، ما شما را دوست داریم.»
🔴
این افراد بالغ هستند که این را می‌گویند.
آیا این خوب نیست؟ شاید آن‌ها سعی دارند به من نزدیک شوند.
🔴
ترامپ درباره ایران: توانایی نظامی جمهوری اسلامی بسیار پایین است. آن‌ها درصد کمی از موشک‌های خود را باقی دارند.
🔴
آن‌ها چند پرتابگر موشک دارند. اما بیشتر آن‌ها نیز نابود شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132560" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ در اختتامیه نشست ناتو در آنکارا:
ایران صدها هواپیما داشت. همه آن‌ها رفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132559" target="_blank">📅 19:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffb435c8a.mp4?token=s1JJk-m4OVh_6fJgEcnxm3W1mgBNDfwBA3WEzmBeBFqExMtcODvgUniDvrDhw26khD6q4geKCUkdZYuzOxUHBDAZ17qQJB2wYnzEpV5y98qI8wWstrdvlI_mCFW9020W5KGIJ-ZIymu4AHdZxhQv1ju3R_miprXzZ-U73TgY39OERQlbLhZbOUzmA-NGxwIpoZQeafsPYKgRzc6G5tmg2s6YrARm_-Q_o0vv6E1_6OLGFyY5tU52-KwUnjXGUy57NfbkLmsCg764ADI2C3aqNgR0htfX2MwbYuu12zow-7ppMvRsmgbsLKWFHcXzSOroW91wvYU29Gu_8oHT5QwYlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffb435c8a.mp4?token=s1JJk-m4OVh_6fJgEcnxm3W1mgBNDfwBA3WEzmBeBFqExMtcODvgUniDvrDhw26khD6q4geKCUkdZYuzOxUHBDAZ17qQJB2wYnzEpV5y98qI8wWstrdvlI_mCFW9020W5KGIJ-ZIymu4AHdZxhQv1ju3R_miprXzZ-U73TgY39OERQlbLhZbOUzmA-NGxwIpoZQeafsPYKgRzc6G5tmg2s6YrARm_-Q_o0vv6E1_6OLGFyY5tU52-KwUnjXGUy57NfbkLmsCg764ADI2C3aqNgR0htfX2MwbYuu12zow-7ppMvRsmgbsLKWFHcXzSOroW91wvYU29Gu_8oHT5QwYlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ترکیه:
فرودگاه‌ها زیبا بودند. آن‌ها یک ترمینال جدید برای ورود ما ساختند.
🔴
همه چیز زیبا بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132558" target="_blank">📅 19:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر حمل و نقل روسیه، نیکیتین:
وزارت حمل و نقل تمام تلاش خود را برای رساندن سوخت به شبه جزیره کریمه به کار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132557" target="_blank">📅 19:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132556">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نتانیاهو از ترامپ تقلید می‌کند—او هم به یک پزشک هوش مصنوعی تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132556" target="_blank">📅 19:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132555">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43d7823e8.mp4?token=dcXpcMlmfuaq6lyV8ZIO5-jdT4xyfmyYCUXzHekqE9GWuQ7hGhrZSriiM40Vr-xg5DDFawE1Ixvohr8JBI338mVcrmWbNTXFRfps-ld5gAonQf_BqSa6lZ8b2ta1AXa6f6OHWtkDLwIwzhdlUqWzGBHnEIjSHm5jwY307Gbw-X6j4pQJrz7mJD_0PwsuJF1C9KbNRbGxZMgmkwq03tH9gDJKIneu2cXbtgX06idAWBmTRMGkdCx4YXzu8KN0u6doD-s79fwxcHdNOQ3Jk7uoZI_vQdezibmRU4ePbSmho4rbh0ecQTtla-1Qiz3rX6_vqs6zNLdkAlyGTO0qH7MdvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43d7823e8.mp4?token=dcXpcMlmfuaq6lyV8ZIO5-jdT4xyfmyYCUXzHekqE9GWuQ7hGhrZSriiM40Vr-xg5DDFawE1Ixvohr8JBI338mVcrmWbNTXFRfps-ld5gAonQf_BqSa6lZ8b2ta1AXa6f6OHWtkDLwIwzhdlUqWzGBHnEIjSHm5jwY307Gbw-X6j4pQJrz7mJD_0PwsuJF1C9KbNRbGxZMgmkwq03tH9gDJKIneu2cXbtgX06idAWBmTRMGkdCx4YXzu8KN0u6doD-s79fwxcHdNOQ3Jk7uoZI_vQdezibmRU4ePbSmho4rbh0ecQTtla-1Qiz3rX6_vqs6zNLdkAlyGTO0qH7MdvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال انجام عملیات تخریب گسترده در طیبه در جنوب لبنان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132555" target="_blank">📅 19:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132554">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
تأخیر دوباره تو دفن سید علی خامنه ای.
🔴
دفتر مکارم شیرازی: با توجه به اینکه استقبال مردم ایران و عراق از مراسم تشییع علی خامنه‌ای خیلی زیاد بوده و ممکنه مراسم خاکسپاری دیرتر انجام بشه، مجلس ختمی که قرار بود 19 تیر برگزار بشه، به شب 25 تیر موکول شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/132554" target="_blank">📅 19:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132553" target="_blank">📅 19:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
جورجیا ملونی، نخست‌وزیر ایتالیا:
ما از همان ابتدا گفتیم که در حملات علیه ایران مشارکت نخواهیم کرد.
🔴
ما در حملات علیه ایران شرکت نکردیم و در آینده نیز در حملات علیه ایران شرکت نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/132552" target="_blank">📅 19:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132551">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تأخیر دوباره تو دفن سید علی خامنه ای.
🔴
دفتر مکارم شیرازی: با توجه به اینکه استقبال مردم ایران و عراق از مراسم تشییع علی خامنه‌ای خیلی زیاد بوده و ممکنه مراسم خاکسپاری دیرتر انجام بشه، مجلس ختمی که قرار بود 19 تیر برگزار بشه، به شب 25 تیر موکول شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132551" target="_blank">📅 19:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkeoUaJm5eToraZlRKQiaGxWZ3ZL-uN2ltZfkqhjicGQAJXcg8XV_JgoBqw1MdQN3aamorbkdxfrS63IIpGx-VkVejhPc4ep-XySbRpAjfY5Pc39e12x35lnnaPxrApwY3esd2qYKqcrc9E4_iaUfhLft16dSp6bjkCGf13P9Sx-h6RstmPni_sLVo2qThYtnbsttQW-IvxgCns_a218Z0Hdu74NmiPyJ62dXghMoiPA7eCgR0oZjnOjiktB1AuBmVZC-SURqjHWlXnWVXfTIoirsXzZO6FbPGhtpo8unRyaWNk6scGg8-5tLmnZ9OUurucpZT2USuJKSfWkF6Uhtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:یکی جواب فحاشی ترامپ رو بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/132550" target="_blank">📅 19:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132549">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
تاس: مذاکرات ایران و آمریکا متوقف شد
رسانه روس به نقل از یک مقام ایرانی:
🔴
«به دلیل تهدیدهای مستقیم علیه مردم ایران از سوی رئیس‌جمهور آمریکا و نقض مکرر تعهدات واشنگتن، ایران مذاکرات بر سر انعقاد توافق نهایی با آمریکا را به حالت تعلیق درآورده است.»
🔴
هرگونه تجاوز نظامی‌ایالات متحده علیه ایران با پاسخی گسترده‌تر و قاطع‌تر از قبل مواجه خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/132549" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ درباره احتمال اعزام نیروهای زمینی به ایران:
«چرا باید الان وارد عمل شوم؟ زمانی وارد می‌شوم که یا آن‌ها کاملاً از بین رفته باشند یا توافقی حاصل شده باشد.!!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/132548" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رسانه‌های عبری:
نتانیاهو و کاتس نشست خود در یک رویداد را به طور غیرمعمول لغو کردند و در حال گفتگوهای امنیتی در مورد ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132547" target="_blank">📅 18:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پرس‌تی‌وی به نقل از یک مقام ایرانی:
ایران در صورتی که با حملات جدید مواجه شود،
تنگه هرمز را خواهد بست
.
🔴
ایران در پاسخ به هرگونه حمله، اهداف دشمن را با نسبت دست‌کم دو به یک مورد حمله قرار خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132546" target="_blank">📅 18:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6e761e2c.mp4?token=NVO0JBjck8GKBbTEwBohEnKjp5UW4kmt-l1P9EaKnaIC1JhnVdn0ZtfbUEEUUOepDizclksLg1cxAZ8FXYYlG3FbboZqzEtS3ZX7in7g83JYa4Qg63DU1gqUTt44zmChtVWFs1MRta9gK4lkVhy_zpjMgmxAvWG4Ab0gDgfEmoNea3RDAzmZ6-N-l1Fc2Ctr1WTLtH7g3TQgmd318OpW2uTaMlDHR02I6Trn5HHNnZlqJRincZlWHh5P_2PcCCG7ryeVqLOngmuY46grZpPNXxeXKXL3q7xyJR0jp3ADK_P-4sYa9A50hOdhoxAGhCDrgskoY0vVT4FCvBpJIdYURw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6e761e2c.mp4?token=NVO0JBjck8GKBbTEwBohEnKjp5UW4kmt-l1P9EaKnaIC1JhnVdn0ZtfbUEEUUOepDizclksLg1cxAZ8FXYYlG3FbboZqzEtS3ZX7in7g83JYa4Qg63DU1gqUTt44zmChtVWFs1MRta9gK4lkVhy_zpjMgmxAvWG4Ab0gDgfEmoNea3RDAzmZ6-N-l1Fc2Ctr1WTLtH7g3TQgmd318OpW2uTaMlDHR02I6Trn5HHNnZlqJRincZlWHh5P_2PcCCG7ryeVqLOngmuY46grZpPNXxeXKXL3q7xyJR0jp3ADK_P-4sYa9A50hOdhoxAGhCDrgskoY0vVT4FCvBpJIdYURw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره اسرائیل:
اگر نخست‌وزیر دیگری داشتید، اکنون اسرائیلی وجود نداشت. توسط ایران به تکه‌های کوچک تبدیل شده بود.
اگر من به عنوان رئیس‌جمهور نداشتید، اسرائیل امروز وجود نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/132545" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9b8be6df.mp4?token=Z8jZGLSqtzPUgryQLb_2vO_VX98FU2RWLzT12MfYufxotv5QaVI6VnKK3-GdiOKpGHP0W_z_meTsTleppGrtXCoHYcYfza21lS99XcAauIMQdX8myLZ-E5l975DW1BE9DAqZzXuWiFjLXG6HFTLle_V_biyts1X29vug4PpQbCTjvXeW8jXNbWC1sLHNM1JkBXDwxP4U3FeqD527Hob29MJaFeGNGQhDTc6LaL91J8EI_mSuqYgU8FEpUtO3TFdbp8Kg8jETLVeIl5UfpKQDeuYvSzukC-BROlYiMIXE1RyLJBk-tHWTG_NpB464FsH2KMyGFpET1HAxrlOV1Za9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9b8be6df.mp4?token=Z8jZGLSqtzPUgryQLb_2vO_VX98FU2RWLzT12MfYufxotv5QaVI6VnKK3-GdiOKpGHP0W_z_meTsTleppGrtXCoHYcYfza21lS99XcAauIMQdX8myLZ-E5l975DW1BE9DAqZzXuWiFjLXG6HFTLle_V_biyts1X29vug4PpQbCTjvXeW8jXNbWC1sLHNM1JkBXDwxP4U3FeqD527Hob29MJaFeGNGQhDTc6LaL91J8EI_mSuqYgU8FEpUtO3TFdbp8Kg8jETLVeIl5UfpKQDeuYvSzukC-BROlYiMIXE1RyLJBk-tHWTG_NpB464FsH2KMyGFpET1HAxrlOV1Za9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره لبنان:
به نظر من اسرائیل در حال عقب‌نشینی نیروهای خود از جنوب لبنان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132544" target="_blank">📅 18:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e990ae2ff8.mp4?token=HM3WZoxoJXNjaWdO_qCYVzavFG8N_mHRCwZxkpfw_RQ7-10AudnvF-U5LbScYZR9I4QondLug-mkostlyp5yYnTgS55XmU9BwV1HeLkVwox72mmhpB1P7QGmO8mI_FdrotA7CqG96n8mXLXhWnXJmHIpx31MoXzuqUdtt4xku5f1CVojLzEvY1gG3pZSmThNWEWACMfOrogZeiXgP4Ivwnvn6PQOuAr4jT6A-N48kt_ebDwHP1O9pVNd7sZdZiGL2jAoQ4EHRxHFAyQxx7iRFRnpxG5vR3lx-DIHLCB5Y35gFKvT28z5jCr33i6Jev7QGTe6MOWqd8ma5i7uClKs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e990ae2ff8.mp4?token=HM3WZoxoJXNjaWdO_qCYVzavFG8N_mHRCwZxkpfw_RQ7-10AudnvF-U5LbScYZR9I4QondLug-mkostlyp5yYnTgS55XmU9BwV1HeLkVwox72mmhpB1P7QGmO8mI_FdrotA7CqG96n8mXLXhWnXJmHIpx31MoXzuqUdtt4xku5f1CVojLzEvY1gG3pZSmThNWEWACMfOrogZeiXgP4Ivwnvn6PQOuAr4jT6A-N48kt_ebDwHP1O9pVNd7sZdZiGL2jAoQ4EHRxHFAyQxx7iRFRnpxG5vR3lx-DIHLCB5Y35gFKvT28z5jCr33i6Jev7QGTe6MOWqd8ma5i7uClKs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هر وقت به ایران حمله کنیم، قیمت نفت کمی بالا می‌رود.
🔴
اشکالی ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132543" target="_blank">📅 18:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ee945f4b.mp4?token=NkC0ohBMQ2YHQ4CD08KCNDysHMNPJ6qfFDesH9dH0aCUmn2EjEgyu285tYI_IAUAQu9PGXcJLF7yzdU7ccx-zQaB-mPN9DVOZsZib6aQb9L8uknltuD8qr84T4HJgbqFo-1T3LDHUPshTmBfbdjYwwQr5VUrkpRVu1lD9WEPQ9B4NLUO_Cn10EzLCIN0z-nvdEwTyS4K82AoveEVrppXjfx-EKezC9ABnhZrAu9vMaTW3ozG4tj2LWHGvfoI3IwbSGI4dIDRqevLqbxIjsyANWHPWN3Ozda5C-8ntrHkB4UkyMRo5w7qaGjQSwd-74zE0pWB5G4a016rI4kMLvIlbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ee945f4b.mp4?token=NkC0ohBMQ2YHQ4CD08KCNDysHMNPJ6qfFDesH9dH0aCUmn2EjEgyu285tYI_IAUAQu9PGXcJLF7yzdU7ccx-zQaB-mPN9DVOZsZib6aQb9L8uknltuD8qr84T4HJgbqFo-1T3LDHUPshTmBfbdjYwwQr5VUrkpRVu1lD9WEPQ9B4NLUO_Cn10EzLCIN0z-nvdEwTyS4K82AoveEVrppXjfx-EKezC9ABnhZrAu9vMaTW3ozG4tj2LWHGvfoI3IwbSGI4dIDRqevLqbxIjsyANWHPWN3Ozda5C-8ntrHkB4UkyMRo5w7qaGjQSwd-74zE0pWB5G4a016rI4kMLvIlbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ در مورد غبار هسته‌ای‌ جمهوری اسلامی ایران:
این‌قدر در اعماق زمین قرار دارد که هیچ‌کس جز ما نمی‌تواند به آن دسترسی داشته باشد زیرا ما تجهیزات آن را داریم.
این‌قدر در زیر کوه قرار دارد و اکنون مشخص شده است که به ماشین‌آلات عظیمی نیاز دارد که ما داریم و هیچ کشور دیگری ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132542" target="_blank">📅 18:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=qyTkufY8RfKaIWlgrqXYABVVhWe0rTgrY7IAMcaTHrhGe99qPrSAoxuixS-3RjZ9M1V718nqlIUcteglvrVGD3S6RbBDqxwuq_5vRUmEJz0ORm2_CPQ46QXDw_zmbyS1pJz6NuCPXSG8JJRhHx5jZAWKPuxbTugo1Y9it-9TNOIxEzpD_QMqMffgXytk7mKovaqp-yLuE3140wB549jfyhwtdh9KX48nIwlhUiudTLuV-6df0vxs0BStUI5pz1pg4ehiJDWBb7bqXm5Km6a4Aw0XXxmJhvkTHw6ewVtwMpAcqYL1W_i5AGrj8xRCmQ7_qpoK_1e4vT9DTCg_h0bHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=qyTkufY8RfKaIWlgrqXYABVVhWe0rTgrY7IAMcaTHrhGe99qPrSAoxuixS-3RjZ9M1V718nqlIUcteglvrVGD3S6RbBDqxwuq_5vRUmEJz0ORm2_CPQ46QXDw_zmbyS1pJz6NuCPXSG8JJRhHx5jZAWKPuxbTugo1Y9it-9TNOIxEzpD_QMqMffgXytk7mKovaqp-yLuE3140wB549jfyhwtdh9KX48nIwlhUiudTLuV-6df0vxs0BStUI5pz1pg4ehiJDWBb7bqXm5Km6a4Aw0XXxmJhvkTHw6ewVtwMpAcqYL1W_i5AGrj8xRCmQ7_qpoK_1e4vT9DTCg_h0bHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میرباقری تو صداوسیما:
دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
🔴
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان شهید شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132541" target="_blank">📅 17:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132540">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h27dMrdSbK4gHipNXTTHTIXhRQhnMxwuKsnggzB5A1n1cXVAC4-1W776zlWlJoIopb3cHYnjtEO0ew0_fuUqEDVmFTt_NgXN36zGgs_H4QzKsp7CbHTBp6cWqy4saDXLl0gQ2w7oChcK7ZVsSPqzZfp3g5BBzwJ84r3lMSeKtubQ5kFXAwkeIbTV0WkyDAOmEHoLbnRa_JCF-aGXssD9EHqVudhG_rGydkeyC142lNBH527hnnZPAtqQzCs7YYLoFV8LcifYLmO5EJjMHoKmco6W6idC46B7Tjbd3-ljiJDWbFs2L8pMFnraFqMy1NmtXQQHisqZFZljcD5Cd28-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خلاصه از اظهارات اخیر
پرزیدنت دونالد جی ترامپ:
ما دیشب به جزیره خارک حمله کردیم.
ممکن است جزیره خارک را تصرف کنیم
من قصد دارم به ایرانی‌ها یک هشدار ساده بدهم که امشب به آنها ضربه سختی خواهیم زد.
در یک روز، می‌توانیم تک تک پل‌های ایران را خراب کنیم.
اگر مجبور شویم، نیروگاه‌های برق آنها را که برق خود را از آنجا تولید می‌کنند، از بین خواهیم برد.
آنها کارخانه‌های آب شیرین‌کن دارند. اگر مجبور شویم، آنها را از بین خواهیم برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132540" target="_blank">📅 17:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132539">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3pk_gbvSO3vQh9YfVDuN8sQAktScmYU0MPsuNr_tWjqiyig6FbUoyCTI1UOF8I_P5gHiVoLCfX5pzGZR--gkLCdibE_64gFA7PZVgzmWk9kNuPL32lcRGnwAibGMKEygv9QHPy-nlkmqvahhzt_qh3bkzeWN0R97uzDhdBxskcuM0QfaRuyzGxFKZdJzFFDVq10-39t9AJS2MqNS5Zr8hH-ybp-yemEm642ymV6VTXw-EpN2PSphCYnJmFD4dOhfX6_HobI_swqeHK_lCcBK_q3eyjAIC26rma4GdtiM6IMc9tU9tYCy-iNUexCA8jqZwYrpSFArJ5HrtCeLx5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یک نفر پیدا نمی‌شود پاسخ فحاشی های ترامپ را بدهد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132539" target="_blank">📅 17:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام آمریکایی:
تمام موشک‌ها و پهپادهای شلیک‌شده از سمت جمهوری اسلامی رهگیری شدن یا به هدفی اصابت نکردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132538" target="_blank">📅 17:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/cde45b3538.mp4?token=OsV4nnmqheosbxxuBKxulBS_WS4f-ybEFeSIhuve9ceJr8B4ImucP4FvrgDrrgaT3IhBm8sjHk2SO9dDaXaxUmH9P1jxSuehQaW3pPh5prR0pTLgY8ZBM0U6Ur43D0jNKbiRjGHdxaMJaN7H3y5cB-Ep3tg9avy10I-_uJwB_stBbcRSJWOQVSzWZlWx9Qp0GxOp3iuO6j1z1E79-da2IW0qUTuK7PLRVkHzsP4tIZi6SajcKTeYVOv591HmteF7MNYeQWbq34DaFIl35EsugPmOl65zYkMQF3FSQB3Vg2SVbDsDuedicdnmVSw6NOVYvD-7Y3IlF1fFWgBfyVRF9g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/cde45b3538.mp4?token=OsV4nnmqheosbxxuBKxulBS_WS4f-ybEFeSIhuve9ceJr8B4ImucP4FvrgDrrgaT3IhBm8sjHk2SO9dDaXaxUmH9P1jxSuehQaW3pPh5prR0pTLgY8ZBM0U6Ur43D0jNKbiRjGHdxaMJaN7H3y5cB-Ep3tg9avy10I-_uJwB_stBbcRSJWOQVSzWZlWx9Qp0GxOp3iuO6j1z1E79-da2IW0qUTuK7PLRVkHzsP4tIZi6SajcKTeYVOv591HmteF7MNYeQWbq34DaFIl35EsugPmOl65zYkMQF3FSQB3Vg2SVbDsDuedicdnmVSw6NOVYvD-7Y3IlF1fFWgBfyVRF9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ:
«شب گذشته ۲۸ قایق را منهدم کردیم، آن‌ها فقط قایق‌های کوچولو دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132537" target="_blank">📅 17:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/980e8489e8.mp4?token=mc-TSi5Fj9P3fe2gdhqp3zH8iXy01hI17sv6HN009cPoYrfAzNkAO-crv-oFxGbucTwk7JfAkUbuVvpMzj-E-gtCPd-bsqdrXC1TlrDRKtZ7yN0xPZWrRckuy_StsMV184uYJ3aH33ckSzOtScln6ZCYDeTHZzPiVqTWSMLLlsqvVUjWNhedcxunY7AoTp84IZVVaYqaxVcSAKYhwrWbcUO-azialD9HjaLf0rA2JiXmKfKcUwYWVXBmXw91AjqHC8ogk1D95qCoMs33cmt3mJI-bmHTzI-qO6lDWsHm_ljGOoEQTsqhe-NdBEMMSZHKQfdhbY141NpsQMQVkw7q7g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/980e8489e8.mp4?token=mc-TSi5Fj9P3fe2gdhqp3zH8iXy01hI17sv6HN009cPoYrfAzNkAO-crv-oFxGbucTwk7JfAkUbuVvpMzj-E-gtCPd-bsqdrXC1TlrDRKtZ7yN0xPZWrRckuy_StsMV184uYJ3aH33ckSzOtScln6ZCYDeTHZzPiVqTWSMLLlsqvVUjWNhedcxunY7AoTp84IZVVaYqaxVcSAKYhwrWbcUO-azialD9HjaLf0rA2JiXmKfKcUwYWVXBmXw91AjqHC8ogk1D95qCoMs33cmt3mJI-bmHTzI-qO6lDWsHm_ljGOoEQTsqhe-NdBEMMSZHKQfdhbY141NpsQMQVkw7q7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ هگستث:
«امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»
🔴
پرزیدنت ترامپ
:
«ممکن است محاصره را اعمال کنیم، ممکن است آن را بازگردانیم؛ این محاصره فقط برای ایران خواهد بود، هر کس دیگری می‌تواند هر چه بخواهد داشته باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/132536" target="_blank">📅 17:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132535">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11b06ef2b9.mp4?token=dXx8jvckdI-aWthJuuRVK2Uc-3FWIi_JkYs3ZhmSQ7jeW4XEcyudGhQuma_Ciy4REc8Q9D2Hu3g4I8IBpuPM891pHit4HW6dxEzGAp510CSLLmS_UfU7Symo-zaD9jBuO8l8IqNo10HhaC1q7Sn5PUlTzVHUXbJExggEhOHxOXqz0S3XJPNH5hYNNbVhyEG4LamdX_aNChHgQXPz_va9w1MBW4Og7ghH_cCV-889v1oUBymOFPUvNhqgzx_7hpNnmBP20OvXNlj6jQXfPZ_Ph3hdYwkgZYGbc_jIrOU7-jpZdw39BtoDJibcrly_0Qj4woNefAPR0N1KCRj2JwQAQ34HcXKDgS0QKmZZluie9WES_2FkzGWDYXKBfejBEaPxc2sgdfbB-NzUHPZmquuf-HPTpXRHyo5c2TMx_eXgEFdV0ZXgazp-f6yo20E8YtSyrWUQXjoQH2K6UxXIZqZK7V_nXoeXwC35_HES7CUnaj0PI-WkINau-Qd2N556I_U7hXEacOGQfTNYcdv3o5kwvRyqF10Yr_3a2pgExmPGaXndVweUicy33qf-p5WAhXUw7hE0dYi0__1Cs3B-jZEDes8HEUHeEgMO7tU47tB4uQKhuw3y6ZTg87PRvI6ZgG-QAjkllQveo1xo18EKNbmZXqDGe-u2G_Y_Ze7kUmu5NaM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11b06ef2b9.mp4?token=dXx8jvckdI-aWthJuuRVK2Uc-3FWIi_JkYs3ZhmSQ7jeW4XEcyudGhQuma_Ciy4REc8Q9D2Hu3g4I8IBpuPM891pHit4HW6dxEzGAp510CSLLmS_UfU7Symo-zaD9jBuO8l8IqNo10HhaC1q7Sn5PUlTzVHUXbJExggEhOHxOXqz0S3XJPNH5hYNNbVhyEG4LamdX_aNChHgQXPz_va9w1MBW4Og7ghH_cCV-889v1oUBymOFPUvNhqgzx_7hpNnmBP20OvXNlj6jQXfPZ_Ph3hdYwkgZYGbc_jIrOU7-jpZdw39BtoDJibcrly_0Qj4woNefAPR0N1KCRj2JwQAQ34HcXKDgS0QKmZZluie9WES_2FkzGWDYXKBfejBEaPxc2sgdfbB-NzUHPZmquuf-HPTpXRHyo5c2TMx_eXgEFdV0ZXgazp-f6yo20E8YtSyrWUQXjoQH2K6UxXIZqZK7V_nXoeXwC35_HES7CUnaj0PI-WkINau-Qd2N556I_U7hXEacOGQfTNYcdv3o5kwvRyqF10Yr_3a2pgExmPGaXndVweUicy33qf-p5WAhXUw7hE0dYi0__1Cs3B-jZEDes8HEUHeEgMO7tU47tB4uQKhuw3y6ZTg87PRvI6ZgG-QAjkllQveo1xo18EKNbmZXqDGe-u2G_Y_Ze7kUmu5NaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زیرنویس فارسی/
پرزیدنت ترامپ:
آنها ۴۷ سال است «رفتار بسیار بدی» دارد؛ پاسخ سخت آمریکا ادامه خواهد داشت
دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ۱۷ تیرماه، گفت نیروهای آمریکایی شامگاه گذشته در پاسخ به حمله جمهوری اسلامی به کشتی‌های آمریکا در تنگه هرمز، «ضربه‌ای بسیار سخت» به ایران وارد کرده‌اند.
ترامپ گفت جمهوری اسلامی «چند پهپاد، یک راکت و یک موشک» به سمت کشتی‌های آمریکایی در تنگه هرمز شلیک کرده و افزود این کشتی‌ها «کاملاً حق داشتند» در آن منطقه حضور داشته باشند.
رئیس‌جمهوری آمریکا همچنین با تهدید به ادامه حملات گفت، «احتمالاً امشب هم دوباره ضربه سختی به آن‌ها خواهیم زد. این یک هشدار کوچک است؛ ما امشب ضربه سختی به آن‌ها می‌زنیم.»
همچنین ترامپ در بخش دیگری از سخنانش، جمهوری اسلامی را به «رفتار بسیار بد» طی ۴۷ سال گذشته متهم کرد و بار دیگر از سیاست‌های تهران انتقاد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/132535" target="_blank">📅 17:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132534">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
دبیرکل ناتو: تنگه هرمز را باید باز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132534" target="_blank">📅 17:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132533">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/ترامپ اعلام کرد که در تشیع پیکر آیت الله خامنه ای ممکن است تروری صورت بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/132533" target="_blank">📅 17:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132532">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: در یک روز، می‌توانیم تک تک پل‌های ایران را خراب کنیم.
🔴
اگر مجبور شویم، نیروگاه‌های برق آنها را که برق خود را از آنجا تولید می‌کنند، از بین خواهیم برد.
🔴
آنها کارخانه‌های آب شیرین‌کن دارند. اگر مجبور شویم، آنها را از بین خواهیم برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132532" target="_blank">📅 17:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132531">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f407ca85.mp4?token=cMJUVfpvCamdk4rjhliAQ2uLrnIUoeCzTD3S19hCpoBB23NAvq8EB37LJbt1enkiUyqVU-HJszQ1DKG8chOplT8abYmhSdSc-UgPiaTKt1IrDdAIvb6-ZVrXTVQYHQSjYLyFdmVQOU5p1Ov-KK18oCtwuixQDgmNQK6l1ystuSEmgE_LlMtCA4AIXojgGuKHlrl0yW-dWo50zDKyeWClg_spelR6y3jlzU0G2CaXuK7PmAsi3ykro5W3VA1q-kZuf6EmbVJiRfWhqEZLe794cdICczVl0Bxbi5tidw3OH4CjYwmo6y4FgLCJRHEFtoS6r07JIJmbExCBNR7Pm58EtaijKf0o9nO45ZfVeQW4Hvo6hHsoy_HdLTcVPAS0doHG1wyanxSjgSkL-oYQb92oBAg53Qyqt01mP8qbRgwIbBWt5vsQlqtVltMWnn9eHlHqyrQQFkeddyGEEL5ZLuLPKudR-qUHbUxDBqkQqQv70-SPsCdDuBazOVMttkpQMJhSbW4LoqDFDKORcT8kjM6WVY3lo7e_lifGHvQvDSytI7nQnKhQhg1kSy6Gf_CtfjujUlWWewypbsT8mgz0kpO_Pg57vsp2-5qiB2yLAiJBwhhpxXhbmo-mVR3hiq1U2DATk4pWPRKHRm-NoFw6YhoohLjSt5XlTnfGC8Dux9l2TLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f407ca85.mp4?token=cMJUVfpvCamdk4rjhliAQ2uLrnIUoeCzTD3S19hCpoBB23NAvq8EB37LJbt1enkiUyqVU-HJszQ1DKG8chOplT8abYmhSdSc-UgPiaTKt1IrDdAIvb6-ZVrXTVQYHQSjYLyFdmVQOU5p1Ov-KK18oCtwuixQDgmNQK6l1ystuSEmgE_LlMtCA4AIXojgGuKHlrl0yW-dWo50zDKyeWClg_spelR6y3jlzU0G2CaXuK7PmAsi3ykro5W3VA1q-kZuf6EmbVJiRfWhqEZLe794cdICczVl0Bxbi5tidw3OH4CjYwmo6y4FgLCJRHEFtoS6r07JIJmbExCBNR7Pm58EtaijKf0o9nO45ZfVeQW4Hvo6hHsoy_HdLTcVPAS0doHG1wyanxSjgSkL-oYQb92oBAg53Qyqt01mP8qbRgwIbBWt5vsQlqtVltMWnn9eHlHqyrQQFkeddyGEEL5ZLuLPKudR-qUHbUxDBqkQqQv70-SPsCdDuBazOVMttkpQMJhSbW4LoqDFDKORcT8kjM6WVY3lo7e_lifGHvQvDSytI7nQnKhQhg1kSy6Gf_CtfjujUlWWewypbsT8mgz0kpO_Pg57vsp2-5qiB2yLAiJBwhhpxXhbmo-mVR3hiq1U2DATk4pWPRKHRm-NoFw6YhoohLjSt5XlTnfGC8Dux9l2TLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
آن‌ها به ما گفتند: لطفاً در مراسم تشییع جنازه ما را نکشید. من گفتم که این کار را نمی‌کنم و ما هیچ کاری انجام ندادیم.
🔴
سپس آن‌ها به سه کشتی حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132531" target="_blank">📅 17:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: من قصد دارم به ایرانی‌ها یک هشدار ساده بدهم که امشب به آنها ضربه سختی خواهیم زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132530" target="_blank">📅 17:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132529">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: ما دیشب به جزیره خارک حمله کردیم.
🔴
ممکن است جزیره خارک را تصرف کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132529" target="_blank">📅 17:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132528">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری / وزیر دفاع آمریکا: اگر رئیس جمهور ترامپ دستور دهد، امشب به ایران حمله خواهیم کرد و ممکن است محاصره دریایی را دوباره برقرار کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132528" target="_blank">📅 17:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132527">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ: اینها دیوانه هستند و باید ۴۷ سال پیش از بین می‌رفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/132527" target="_blank">📅 17:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132526">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرنگار : امشب هم قایق‌های ایرانی بیشتری رو هدف قرار می‌دید؟
🔴
ترامپ : معمولا بهت نمی‌گفتم ولی می‌دونی چیه؟ هیچ کاری از دستشون برنمیاد پس جواب احتمالا آره‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132526" target="_blank">📅 16:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132525">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ : توافق ممکنه دوام بیاره، و ممکنه دوام نیاره، ولی میاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132525" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132524">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرنگار: آیا به اوکراین خواهید رفت؟
🔴
ترامپ: من می‌روم. ترجیح می‌دهم جنگ تمام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132524" target="_blank">📅 16:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132523">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ درباره حملات اوکراین به پالایشگاه‌های روسیه: این یک اقدام تحریک‌آمیز است که می‌تواند به پایان دادن به این وضعیت کمک کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132523" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132522">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d492dd26e.mp4?token=SI59uDcJvDizK8_VLKkt1WwWBkEt1M66UKZtVEEK_VBBUj2IrZhdoLxvpwAKyrTllN0GJ6CnxDCVO3EWicAbu8zSXemeDaiIgbghYPgwhOWwrK3HMg8Yr6vOAXXA6jSyEv__Kjo1swHTmoYgzjQCjXjeGlfVfZyn7UMx985kGA9b_3t88uV76tO4b68DGnUaEOPIVm1-vaNhMMF623ctFGTOBdNyhpzVELQCnF6FJl-pd5nSsh09YH_MZcBBn1BOtYSaJ_xSiu8E9hm7NhorCxT5VCi1nzkT23XKd19T6LPvp7tlTQadpOwnb7IUZFvjl6RGq7LBSh3TzRudmxCsfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d492dd26e.mp4?token=SI59uDcJvDizK8_VLKkt1WwWBkEt1M66UKZtVEEK_VBBUj2IrZhdoLxvpwAKyrTllN0GJ6CnxDCVO3EWicAbu8zSXemeDaiIgbghYPgwhOWwrK3HMg8Yr6vOAXXA6jSyEv__Kjo1swHTmoYgzjQCjXjeGlfVfZyn7UMx985kGA9b_3t88uV76tO4b68DGnUaEOPIVm1-vaNhMMF623ctFGTOBdNyhpzVELQCnF6FJl-pd5nSsh09YH_MZcBBn1BOtYSaJ_xSiu8E9hm7NhorCxT5VCi1nzkT23XKd19T6LPvp7tlTQadpOwnb7IUZFvjl6RGq7LBSh3TzRudmxCsfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره جنگ روسیه و اوکراین:
ما جنگ‌های زیادی را حل و فصل کرده‌ایم. و این یکی، جنگی بود که فکر می‌کردم شاید از همه آسان‌تر باشد.
🔴
اما پوتین شخصیتی پیچیده است، و این فرد هم شخصیتی دشوار دارد.
🔴
این کار، کار آسانی نیست، اصلاً کار آسانی نیست. این نیازمند تعهد زیادی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132522" target="_blank">📅 16:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132521">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ به زلنسکی: ما به شما مجوز ساخت پاتریوت‌ها را می‌دهیم.
🔴
به این ترتیب او نمی‌تواند شکایت کند که ما به اندازه کافی به او امکانات نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132521" target="_blank">📅 16:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132520">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fb7d4eaa.mp4?token=Ca5WekYbt74eb1pAmd7hc0ci_dCV8b_nWmDiidxkh5s46aKoX54xHHPhmYikcMC2nMX7HodzTG4bdw4xFnwLUopz4fh00-vmTV_bzLdNA8inqK48Qoh46miM71osWUX4WnK987A_0OKC4gcyyotnR7DjOVlRWmXnbxY7PKElbB7RzvTEdNdJwuCx_Pgzx4_yCBHkQgMFMVNs214dl12MrjvszfHSExAWdJxV4VkI7IIDiI4klnlm07zuNKCYqhxNXQ3-low8BkZslesF_ODjWVztp-OH5ed37y-YY17qRcSSQIsjGk5Wc5fqkFUc3f3iRY0JkCkttqUIbp57K6aHjIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fb7d4eaa.mp4?token=Ca5WekYbt74eb1pAmd7hc0ci_dCV8b_nWmDiidxkh5s46aKoX54xHHPhmYikcMC2nMX7HodzTG4bdw4xFnwLUopz4fh00-vmTV_bzLdNA8inqK48Qoh46miM71osWUX4WnK987A_0OKC4gcyyotnR7DjOVlRWmXnbxY7PKElbB7RzvTEdNdJwuCx_Pgzx4_yCBHkQgMFMVNs214dl12MrjvszfHSExAWdJxV4VkI7IIDiI4klnlm07zuNKCYqhxNXQ3-low8BkZslesF_ODjWVztp-OH5ed37y-YY17qRcSSQIsjGk5Wc5fqkFUc3f3iRY0JkCkttqUIbp57K6aHjIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران: ممکن است ما این کار را بدون توافق انجام دهیم. این آسان‌تر است.
🔴
این افراد دروغ می‌گویند و تقلب می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132520" target="_blank">📅 16:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132519">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: رئیس‌جمهور اردوغان مدت طولانی است که دوست من بوده است. مردی خوب، مردی قوی.
🔴
او کارهای فوق‌العاده‌ای انجام داده است. همه جاده‌ها بی‌نقص هستند. همه چیز عالی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132519" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132518">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: ویتکاف و کوشنر به کار روی پرونده ایران ادامه خواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132518" target="_blank">📅 16:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132517">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5cb41015d.mp4?token=WCyc4SWJ8adxN0lJPnW9jXzlorZjK0uqiNcG68m14mr1i5fciFwLoXsI3zy-pKd8Dg2VS6GxcuhbmLoMsyys0JicST4V_SXhCBo2yrlEfTxaVtCIQKOc5yx98O5cr5J8ztwQMrL3ssq7sYM6sxaYwgTOhGC9NRK4mnBG_NCKEuYjYxuAYHD997pJHSGwyQuj_otDD7kA_w95B54izuls4I8Gp4BAThkSCp2DglodiFDK8LrX76jy6q2oLeMaj1biw05k_Sx9XAXcxnWUy196XiwPampddbxKyGNOvF3O3tPnoBEJnXW7JRwO9tFxHpBgAliB-g4uFROykNwi6Si8nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5cb41015d.mp4?token=WCyc4SWJ8adxN0lJPnW9jXzlorZjK0uqiNcG68m14mr1i5fciFwLoXsI3zy-pKd8Dg2VS6GxcuhbmLoMsyys0JicST4V_SXhCBo2yrlEfTxaVtCIQKOc5yx98O5cr5J8ztwQMrL3ssq7sYM6sxaYwgTOhGC9NRK4mnBG_NCKEuYjYxuAYHD997pJHSGwyQuj_otDD7kA_w95B54izuls4I8Gp4BAThkSCp2DglodiFDK8LrX76jy6q2oLeMaj1biw05k_Sx9XAXcxnWUy196XiwPampddbxKyGNOvF3O3tPnoBEJnXW7JRwO9tFxHpBgAliB-g4uFROykNwi6Si8nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به اشتباه جمهوری اسلامی "ایران" را جمهوری اسلامی "ژاپن" خواند
/ترامپ: جمهوری اسلامی ژاپن 111 موشک به ما شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132517" target="_blank">📅 16:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132516">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40023a358f.mp4?token=nWb_UzXqBol7aELCfqwXXBghnpfWOWedT89R9aMDgZiG8vnlEYQfmA7pNr5n1W51I084J6oHSWSEvVcqdU_2AZTv0JEUK2cV2nRSCffnYDzXLuMRLtmKB9trjQkm8vkboVKGGbzEzc1EgkXag69zQLoJqkjARjCp43s0_rYXjA_w6Z-8-YbwjcS9Nz0IMlFpNZHFu2HkAb4zmm8hEDICKHkP2PmmpItE0fgyeMfRchb80Ew0l4DYt_88GqL4P3eWs89oAkVTNY-fGOi__JaXtbB44plxU5dLVfIT-lwlpwVkAoovZpcjGxtntk3-CO95lN4GiETiEtj4kRzPTthW5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40023a358f.mp4?token=nWb_UzXqBol7aELCfqwXXBghnpfWOWedT89R9aMDgZiG8vnlEYQfmA7pNr5n1W51I084J6oHSWSEvVcqdU_2AZTv0JEUK2cV2nRSCffnYDzXLuMRLtmKB9trjQkm8vkboVKGGbzEzc1EgkXag69zQLoJqkjARjCp43s0_rYXjA_w6Z-8-YbwjcS9Nz0IMlFpNZHFu2HkAb4zmm8hEDICKHkP2PmmpItE0fgyeMfRchb80Ew0l4DYt_88GqL4P3eWs89oAkVTNY-fGOi__JaXtbB44plxU5dLVfIT-lwlpwVkAoovZpcjGxtntk3-CO95lN4GiETiEtj4kRzPTthW5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جنگ با ایران: این یک جنگ نیست. این، خلع سلاح هسته‌ای ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132516" target="_blank">📅 16:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132515">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها بسیار بد رفتار می‌کنند، همان‌گونه که در ۴۷ سال گذشته به همین شکل عمل کرده‌اند.
🔴
‏ ایرانی‌ها رفتار بسیار بدی دارند و ما پس از آنکه آن‌ها کشتی‌ها را در تنگه هرمز هدف قرار دادند، اقدام به بمباران آن‌ها کردیم.
🔴
‏ من از اقدامات ایرانی‌ها رضایت ندارم ولی موضوع مورد نظرم تغییر رژیم نیست، اما واشینگتن نمی‌خواهد ایران به سلاح هسته‌ای دست یابد چون اگر داشته باشد از آن استفاده می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132515" target="_blank">📅 16:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132514">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: ممکنه امشب دوباره به ایران حمله کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/132514" target="_blank">📅 16:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132513">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOynXCcJ41ONzIiI54_ovEgzRnYr18cgf_v5fhJXTHfgQ9QB1rwcci0mGIXz5QmlvN9RqABE8o7Dh0SIGpJn-g15uJPgdlcEArSQtFUCnavYVwqUPPyEM8gD3y7nj1plQ4Yu2lenqAcyOLY5rTxY31fIuj2F3X1pSsJ7tEpGxgGiPNdEPOM-z_VR_fLvAyEP31wGrTQuJCZnH3SSLUMzRxslvW-1-NcUBNIRBlbQAbsRBvA_2t4YBRKx3ZF2rJevl9kcxsH7xE-HRngJX44epuF6DKcb8e9nEuleoQLaqqj7FqYf-J4j28C7XS9rrpFiFpeanUmKjJ3c-mOrldUjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واحد آسیب‌دیده نیروگاه ری پس از حادثه حریق، دوباره وارد مدار تولید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132513" target="_blank">📅 16:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132512">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شیوع ابولا در کنگو ادامه دارد/ شمار قربانیان از ۵۰۰ نفر گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132512" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132511">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری/همه فرودگاه های هرمزگان به دلیل تنش ها تعطیل و پروازها کنسل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132511" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132510">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ1kjky0fLfvcoTYrdVr2wavdLcNqgDZ0SV6w-pxHqpTVmCMUlaem9bdPYpBGvmCgQ-Q1UOhJg1q-cTvyD0zkMdVKMKgDsm2wOYI1ENMxQE4PABXsPE4UvLof8F0e2f2IWw3gEyLmR7ITxF7boAMVNGw32V1qYWMfGImeRNxSr7yH3cDAjqkzRiJ6sGFe9fGoC57IgQtXIJSiXD4hPMqRhRSw0UYddTYKciBAUJm0j3lLqQDa-gZVuNp2OuEU9FtfQiezBCatpLO6JDz3h_bxFVWmdsg3RFXgVetuJHloJH1I36fUsX9e5-TooeHYpaZIMJbSrW48qCRUp5NXqLtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایمز اسرائیل: "ارتش اسرائیل اعلام کرد که انتظار چندین روز درگیری با حکومت ایران و احتمال ازسرگیری کامل جنگ را دارد؛ ارتش اسرائیل همچنین از «هماهنگی کامل» با فرماندهی مرکزی آمریکا، سنتکام، خبر داد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/132510" target="_blank">📅 15:53 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
