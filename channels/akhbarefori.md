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
<img src="https://cdn4.telesco.pe/file/T8fTVauWYWc2vY7wODxtSi6FWD2eMVKWjWNo9xHMIyh23g5Eiu08EEhFl9vJMJHlNW6bfD-9rOMu0-I0md56QAgVzmlEx6mUqPFUaUakt4sqlOd-7uHila4RW7nKZEU85dBABMhgFl4zlhPv5mGK8LiDNbcKj_zk5PVOM2R9xG_1Wspz7SwEmmLSG-9uyleQ7GDR4nHNoo7U45n0r6pSz9SL-1J1SpqD0MTEyIEDdpL5UDAa2vncgmaq-xoSzUJHxNzMLEUYqpnC13C4rp5hS892e8OeGmog6FYTdYBxdggrGdXUg_ifllO6pfBJYp32DWMLJ9Ayhut50M1HwA6M1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 02:27:01</div>
<hr>

<div class="tg-post" id="msg-679841">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
برای آزمایش بمب جان ۱۵۰ هزار نفر [توسط آمریکا] در وهله‌ی اول از بین میره...
🔹
به مناسبت جنایت آمریکا در هیروشیما و ناگازاکی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/akhbarefori/679841" target="_blank">📅 02:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679840">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به جنوب لبنان و فلسطین اشغالی
🔹
منابع خبری از حملات مختلف رژیم صهیونیستی به مناطقی از جنوب لبنان، و هم‌چنین مناطقی از نوار غزه در فلسطین اشغالی خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/679840" target="_blank">📅 02:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679839">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
افزایش قیمت نفت: ۸۴.۸۳ دلار/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/akhbarefori/679839" target="_blank">📅 02:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679838">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfs_1gfMCyqAadTCXVAxjs0MJeny1PPL56EEmv6ton7Bu-mkfGVeu2M6522TmfC5vCig1mPTsbGfe3IMccQFv0cPxTBCB0u21-j5yf8nX1CwZIoHJ5Ajh3FP-zS6MfvlROursRimotyKb4VoJdLVhV_6By3KFi08OcwDJfXYBju4tfIxPVbSCenSmBxdWxSDvVZ8wKVSMzK6eDVMXRGMxUwtwts-31Kx2J373ki5xoj4mvakNzhgV4xNxi8NB0V6UFNRfdaD6p4GJSbtrouBu1s9XeY2WKDu2P-QnjsfHsaVpPT3f_0djwAxF5B2-PWmdYevrMhG1E45UJ9YXNxyhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرنگونی یک پهپاد متخاصم در جنوب ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/679838" target="_blank">📅 01:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679837">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8104959d0.mp4?token=KJ3PLe0lI5utC80-BZVsNTtUuEMQBb4SK2ONUME0a8FOJ-b9PEj7iXGEgsUB-86jmGjb5T3Ydckko0M_KmU6yrlP2_rlRu4O-0NKTcgMnNLcZ0rBgew56G3IOohqGaLSV1ywi0SWGri9tgZyrKBuAzJ8cwZGAXNxYFsdi4yudWUUdBhhoHbpDbr4o5YRX3MYbo7kHqgVEV-fEKb7w1w8FhhFiDelSxRnoe--c_AwBe3iXowo7hXp17Vp-8mf6JS1eDMD7n--bEBHPCv-af1w7sTD3BzVaoafKAL9ccEdwIN35wAEr0UFhdQAxNJMkLIJIu949SSOXFUS9rTHhdMGKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8104959d0.mp4?token=KJ3PLe0lI5utC80-BZVsNTtUuEMQBb4SK2ONUME0a8FOJ-b9PEj7iXGEgsUB-86jmGjb5T3Ydckko0M_KmU6yrlP2_rlRu4O-0NKTcgMnNLcZ0rBgew56G3IOohqGaLSV1ywi0SWGri9tgZyrKBuAzJ8cwZGAXNxYFsdi4yudWUUdBhhoHbpDbr4o5YRX3MYbo7kHqgVEV-fEKb7w1w8FhhFiDelSxRnoe--c_AwBe3iXowo7hXp17Vp-8mf6JS1eDMD7n--bEBHPCv-af1w7sTD3BzVaoafKAL9ccEdwIN35wAEr0UFhdQAxNJMkLIJIu949SSOXFUS9rTHhdMGKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صفحه فارسی AFC با انتشار ویدیویی نوشت: وقتی علیرضا بیرانوند روی خط دروازه می‌ایسته، گل زدن بهش تبدیل میشه به سخت‌ترین کار دنیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/679837" target="_blank">📅 01:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679836">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای سنتکام: از زمان ازسرگیری محاصره دریایی علیه ایران، مسیر ۵۵ کشتی تجاری را تغییر داده و فعالیت دو کشتی دیگر را متوقف کرده‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/679836" target="_blank">📅 01:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679835">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بلومبرگ: توافق هرمز با رد مذاکرات مستقیم آمریکا توسط ایران، هنوز خیلی فاصله دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/679835" target="_blank">📅 01:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679834">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
هکرها با ترفندی جدید بیش از ۱۰۰ میلیون دلار بیت کوین از کیف‌پول‌های سرد سرقت کردند
🔹
هکرها موفق شدند بیش از ۱۰۰ میلیون دلار بیت‌کوین را از بیش از ۷ هزار کیف‌پول سرد شرکت Coinkite به سرقت ببرند. این نفوذ درحالی رخ داده که کاربران از کلیدهای سخت‌افزاری فیزیکی استفاده می‌کردند و تصور می‌شد این کیف‌پول‌ها امنیتی نفوذناپذیر دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/679834" target="_blank">📅 01:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679833">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef5_QAIu8fb2U9U8quVBwuYSSMDCIxH3uG4-SMDjzcfNLW5gTAA4AhYaLLBgUAKGKawoNjLzs2Y_2PFeV1l7NrcQZ3-Wul1WwPGBIJDAfEu2y9kbgzvR8zY8Ju707s2WkEUQjqMPjJwk5ZLgSr7-8WSpWsK0C0YL51ZRGPyYdYqaABQteS6a2W6laiGqh4aqm90QTLeBYfcH79LS0O7dQVOne4tg7ALlrgCygg6BcfDCZcYkrc2UlwxzYLUKN9ury76Uxg_22tN9__D6qvrk_6Qk2_E9QuR9XTrPf2I5SfcIwY8mZKIYn5PxXzfDT_iL85lDGY_SUAkAfJciIIZ4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور آمریکایی: همین حالا باید جلوی خسارت‌های ترامپ را بگیریم حتی با توافق بد
کریس مورفی نوشت:
🔹
من حتی از یک توافق بد هم برای پایان دادن به این جنگ حمایت می‌کنم، چون باید همین حالا جلوی خونریزیِ فزاینده خسارت‌های ترامپ را بگیریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/679833" target="_blank">📅 01:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679832">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54f13a0af.mp4?token=WISAQ054ZsEb0J4Q6g5zXeYTz3N5Rj08GoR1WhXXNfp3Nf0zXtrtA8n2eHYvDXMqiBHvyR1txTDVIzZwlcmS6igXE7VBSbJAdie09SPeKEhEJ8TF4wsI3OFHzxqAbTonO8eNAT-roIWZG75U3LeX8KlcqqPAWUx60K-jAJBq27ugb66N2tY_BXIReyomQv7xPdaiUeYY5qsTXgdOKLnpL9dAEJ1WCoR_HdpPa27o2rTtidtrUxfhOZK4Kd8_K6eNwyjLqhFrsmBNYsLZXGfVjMgD6QpjiIQVq3e4gVQOd_5MrA5t8xjK3J2zvQs6Sas9Iyx1TD8OOJ5go7aGV3TkvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54f13a0af.mp4?token=WISAQ054ZsEb0J4Q6g5zXeYTz3N5Rj08GoR1WhXXNfp3Nf0zXtrtA8n2eHYvDXMqiBHvyR1txTDVIzZwlcmS6igXE7VBSbJAdie09SPeKEhEJ8TF4wsI3OFHzxqAbTonO8eNAT-roIWZG75U3LeX8KlcqqPAWUx60K-jAJBq27ugb66N2tY_BXIReyomQv7xPdaiUeYY5qsTXgdOKLnpL9dAEJ1WCoR_HdpPa27o2rTtidtrUxfhOZK4Kd8_K6eNwyjLqhFrsmBNYsLZXGfVjMgD6QpjiIQVq3e4gVQOd_5MrA5t8xjK3J2zvQs6Sas9Iyx1TD8OOJ5go7aGV3TkvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرنگونی یک پهپاد متخاصم در جنوب ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/679832" target="_blank">📅 00:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679831">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
برخی منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی تنگۀ هرمز خبر می‌دهند
🔹
شبکه راشا تودی گزارش داد، شعله‌های آتش از فواصلی دور بر فراز آب‌های عمان قابل مشاهده است اما علت آن هنوز مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/679831" target="_blank">📅 00:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679830">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
برخی منابع خبری تصاویری از لحظاتی که یک کشتی در نزدیکی سواحل عمان، در مجاورت تنگه هرمز، مورد اصابت قرار گرفت و آتش گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/679830" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679829">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c140aa3b9.mp4?token=XbxGdmAl30pJWEkZ-4KxZCAQahjTvFbTR9sSazMFCxx3ArwICZ5I3jwoy8sEoZLgvwJewJ545GS2WEuomT820bZu1qg6b-8tSZ7h1CZ7yFZ8HOoNqXhhenaKinFMYxD_a9GjYgdaSRXBL8NdMexdzTy6IVi3PngAUbSQyDxwgY_Fj0cT0XNRJGd9m-91daRQF-jm-iM57ndPmymp0SFZ6vrIam4OCWT5-N8XxLFbWevOS2MaHe_lNuDk7f-HDBLcxd2qr8Ql94sBezGicDzhw7F29xBnD-8bHczB2jHSD6xNRg_uMCvaZokcoKGC9OsRZV2dYrzJ2uHTTw5IGvr3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c140aa3b9.mp4?token=XbxGdmAl30pJWEkZ-4KxZCAQahjTvFbTR9sSazMFCxx3ArwICZ5I3jwoy8sEoZLgvwJewJ545GS2WEuomT820bZu1qg6b-8tSZ7h1CZ7yFZ8HOoNqXhhenaKinFMYxD_a9GjYgdaSRXBL8NdMexdzTy6IVi3PngAUbSQyDxwgY_Fj0cT0XNRJGd9m-91daRQF-jm-iM57ndPmymp0SFZ6vrIam4OCWT5-N8XxLFbWevOS2MaHe_lNuDk7f-HDBLcxd2qr8Ql94sBezGicDzhw7F29xBnD-8bHczB2jHSD6xNRg_uMCvaZokcoKGC9OsRZV2dYrzJ2uHTTw5IGvr3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منایع محلی از شنیده شدن صدای انفجار در آبهای خلیج فارس خبردادند
🔹
منبع این صداها هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/679829" target="_blank">📅 00:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679828">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_7xFaJRtkFjKVdn-eE3b7U-jpZVFG-9q7yHuK3p1m-LuyAJID6SaaS7ztQpKOiklepRe2l24Fbc4p1bbE1Rvg0r-2lI8C5w68TGVz61UfTEJWImPB2d-Tnlc4sS0mlF2p1tSSGl3gRlkCU5Pzoxb7kb2TJRksewAyJhYplVAVDa0rUiKuyrQv_S2doFYkDFNP_0i39cbn3qLxarjG2g9PK_hqEnIt_RJavvXsXZVjG4yWjUrW3wc4ljVPHqGx8Ono8BeBjgR0XMUB5iQCFCdbcfgxvHHh-ryvtpTjDpG9-jpAvJUS9ExKEApRl6QAO1FQK-bk0tEOTc0_S6GhuqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دوباره به پول ایران حمله کرد
🔹
دونالد ترامپ طبق معمول پست گذاشتن در شبکه اجتماعی خود را امشب هم آغاز کرده و در پستی به پول ملی ایران حمله کرده و مدعی شد:
«نتیجه
۵۱ سال رفتار بد! ایران هیچ پولی ندارد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/679828" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679827">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
برخی منایع محلی از شنیده شدن صدای انفجار در آبهای خلیج فارس خبردادند
🔹
منبع این صداها هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/679827" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679826">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
یک منبع دیپلماتیک لبنانی به المیادین: هیچ برنامه‌ای برای برگزاری دور جدیدی از مذاکرات بین لبنان و اسرائیل در ماه آینده وجود ندارد/ دور جدید مذاکرات، احتمالا پس از تابستان برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/679826" target="_blank">📅 00:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679825">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
موشک‌های پاتریوت عربستان هم ته‌ کشید
خبرگزاری رویترز:
🔹
عربستان در ۳۸ روز نخست جنگ، حدود ۲۴۰۰ موشک رهگیر PAC-۳ شلیک کرده است؛ رقمی معادل تقریبا ۸۶ درصد از کل ذخایر این کشور معادل ۲۸۰۰ موشک که باعث شد تا آوریل گذشته، تنها ۴۰۰ موشک برای عربستان باقی بماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/679825" target="_blank">📅 00:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679824">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اندیشکدۀ آمریکایی: قدرت سایبری ایران در مسیر تبدیل شدن به تنگۀ دوم
🔹
کارشناس سایبری مرکز مطالعات راهبردی و بین‌الملل در گزارشی تحلیلی نوشته ظرفیت‌های سایبری ایران به نحو چشمگیری ارتقا یافته و عملیات‌های موفق اطلاعاتی علیه مقامات ارشد امنیتی آمریکا و اسرائیل، گواه آن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/679824" target="_blank">📅 00:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679823">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
از سرگیری مجدد حملات یمن به مواضع مزدوران سعودی
🔹
سخنگوی نیروهای وابسته به مزدوران سعودی از آغاز دور جدیدی از حملات پهپادی و موشکی نیروهای مسلح یمن خبر داد و مدعی شد پدافند هوایی این ائتلاف در حال مقابله با آن‌ها است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/679823" target="_blank">📅 00:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679822">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e44b695b75.mp4?token=kacZ2vn1feS89UAklSWLYMhCNeEumv4Q3MRShDDJ8y9GPSGLgrk1ems59P2hy9VmaktwP4CqqjVrCdFEVa96GHgzQBmHLtvKLOxa8xbt4KLavkY9sRAvZO6Fa8PVcshmVaCcq1t-7V6Imt8kgM5WHVi1GF4a-qRKG4mbQB6OYuvPH5eCn65qSIKCSmb7rLrcuLfUPh5T5hemPWCBOc4GJxGO9C0hGU_R2kn6QoEgIhWa0lIUUeXJmTny9LF2FCUS1xLQWS-k-DPDH83UOmxjqoUOnvxDIIN38Z8YlbMKAfrOMeum7zxrvinbkFmJKQstJf-6Azk4dGHl3SvW35pVCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e44b695b75.mp4?token=kacZ2vn1feS89UAklSWLYMhCNeEumv4Q3MRShDDJ8y9GPSGLgrk1ems59P2hy9VmaktwP4CqqjVrCdFEVa96GHgzQBmHLtvKLOxa8xbt4KLavkY9sRAvZO6Fa8PVcshmVaCcq1t-7V6Imt8kgM5WHVi1GF4a-qRKG4mbQB6OYuvPH5eCn65qSIKCSmb7rLrcuLfUPh5T5hemPWCBOc4GJxGO9C0hGU_R2kn6QoEgIhWa0lIUUeXJmTny9LF2FCUS1xLQWS-k-DPDH83UOmxjqoUOnvxDIIN38Z8YlbMKAfrOMeum7zxrvinbkFmJKQstJf-6Azk4dGHl3SvW35pVCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رجزخوانی مهدی رسولی در خونخواهی رهبر شهید انقلاب
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/679822" target="_blank">📅 00:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679821">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpmUk7zx3tkW0oUQPrb4rfay1b3kJ4pwxUzZKjWkkcJDgfJjMYaL2c2LXhnuxZje7MfrdI49h7hh9gRrqS6Kt4JxhodYbRjZZAo2vykeO4oPXK8rNe6ROY_rqXdkpUt5-vJiMMnjf6FG75NtB3_pK7qFroJROkexaAnplso7k2xXbZbNYLUvayk5wA-0PZwZh-IJih3R3v_bwHY66TsTesVeRQFDl2QrVXO6EZnrLLHomvLImGYxZcTTFUDkKSIVL9QSz-gEdsfUEzr0Kc-iVj_81Y-g121C3Faosf5RB17AIKSdOBUgJWvoMKeD8Ii9ciaj6Qj7zcFRi251OFRfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/679821" target="_blank">📅 00:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679820">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30866b92d.mp4?token=IeeW1eWV_BFvfwpdA2h5MkCe42vrO0MQvqnq3KN6-O1Yf5YF6wmSGv0TzKcKYAgF0xl_PkDRyT2Ney6kKOIrsFOMEfE6Jl098WoGW0GVTWP7KZZ7OMhoxqmsmTfpqoU8TrLPW90OJ7iNpn0zZsIvRELU4Hg0w2YBAa1-TqfCYGSzRCHJgqtCGT-LtfjwJ5VghiXeld2Wz7nspZB9yS_zfcUvYQXkjIkFRCauVugL7VsbYS2YyulguQy1o9DJK8qioxuSjPB7tnUNkiaQD0xk0-CoT3r2FM0L2FFcQGH2HkUh9c7jJdieLu5nGksVb5Hdlygvotl7HO5JfrSbSjPbRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30866b92d.mp4?token=IeeW1eWV_BFvfwpdA2h5MkCe42vrO0MQvqnq3KN6-O1Yf5YF6wmSGv0TzKcKYAgF0xl_PkDRyT2Ney6kKOIrsFOMEfE6Jl098WoGW0GVTWP7KZZ7OMhoxqmsmTfpqoU8TrLPW90OJ7iNpn0zZsIvRELU4Hg0w2YBAa1-TqfCYGSzRCHJgqtCGT-LtfjwJ5VghiXeld2Wz7nspZB9yS_zfcUvYQXkjIkFRCauVugL7VsbYS2YyulguQy1o9DJK8qioxuSjPB7tnUNkiaQD0xk0-CoT3r2FM0L2FFcQGH2HkUh9c7jJdieLu5nGksVb5Hdlygvotl7HO5JfrSbSjPbRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای نخستین بار | فرماندهی که در میدان مسئولیت و خانه، بار مسئولیت را عاشقانه بر دوش کشید
🔹
به یاد سپهبد شهید سید عبدالرحیم موسوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/679820" target="_blank">📅 23:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679819">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdm8vjTf51xmFSOeR3sBHD4gWy51rGFzpAQ6M452l-AY7rkh-wFSS919RMaDjWDYq5dpjfYMgPbmu4E-rIqvZpJh6fYLW4uvWtSAHYELIZUO8kSIRRClyrIhzBdeDRhZvNhnr5tzFJ4AjK0VNBnNbk-FG01ilTGc0e8NFgYeT8XCxeojfD6QpxfQnfPQeODvnGLcdJ2jsf8PLwCGiqIuokLMMLuoByayfR9Fdp2DS5FqVEEOT3kxS2iguAOOQ4EWVQffHPBwLeempayK3gf_12fFTVLfT7Fq_yelPoI903CWnOZUYz6YsPnHVirMTvzgFe6lHlJbdIRsmaTUPIuSUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پروژه‌های ناتمام در ایران
/خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/679819" target="_blank">📅 23:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679818">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gytxxFTngwD7D54RvtPa3kj5Ghg7rCcKh0Z-J5TQkkHvISJZ5rtEgBd-wkCYoCLrUOG_gFRjcmFWQ2YASVQAD7u8B_ftvdUYx7TvZS-2SThWjv8kRLTuhgAFlCVDCs4sNIQWRSg4znUCdcOKn--rAA9MlEcOjGWR3dDOPyN2P67X3YQg3Id7s7B9h2K7H-yL4XKKIah8loVwm145NSnKCeg2k7ufS9WXdM4Z3mSWcfIk0TMDMaXS4Rwh1DCG7v-kT_I9sNzcEetnxEsSYCMdT0TB6rWdx6OsUdZVjltDbdRGdEr-4q1tsjdhBADPZrnEBwwrUKNeQt-edhN1qLBCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین برآورد موسسات از قیمت جهانی طلا
@Titretejarat</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/679818" target="_blank">📅 23:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679817">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f416e4e6d6.mp4?token=l2Um50z-TaNw1qb0RWrWZT4lbNXwXV1L1RAZTuWb-phhdj7jG4Hw4YgBqgm_7E3du9FXGfY3gsfTf7ADdAPQWKugep7KDllnnVjVHxA5QQYB_v4hGrBuO0OwLPPZnTj-ByoKTPEy1i9PALSS0Um4npZrr1q8qWbfioCRdsHMhI-WuiK0tFDX-3Rh0DEb83NQO4lzLb_QtD_yqcp0DFRICZmF81XTK2BVZxMUdrYqtl85PawFUYYWP_UIa7hjEVtkyYnXETQGXEtsQBKsxISsu1gRx2cIPHm7rBfGc2CasgHkcT57-rHcBD78jGNc1w0CkAsytTfG3hsnWfms1cc2pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f416e4e6d6.mp4?token=l2Um50z-TaNw1qb0RWrWZT4lbNXwXV1L1RAZTuWb-phhdj7jG4Hw4YgBqgm_7E3du9FXGfY3gsfTf7ADdAPQWKugep7KDllnnVjVHxA5QQYB_v4hGrBuO0OwLPPZnTj-ByoKTPEy1i9PALSS0Um4npZrr1q8qWbfioCRdsHMhI-WuiK0tFDX-3Rh0DEb83NQO4lzLb_QtD_yqcp0DFRICZmF81XTK2BVZxMUdrYqtl85PawFUYYWP_UIa7hjEVtkyYnXETQGXEtsQBKsxISsu1gRx2cIPHm7rBfGc2CasgHkcT57-rHcBD78jGNc1w0CkAsytTfG3hsnWfms1cc2pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌‌های آخر الزمانی در کانادا؛ آسمان نارنجی بریتیش کلمبیا در پی آتش‌سوزی‌های جنگلی
🔹
با ادامه آتش‌سوزی‌های گسترده در غرب کانادا، ویدئوهای رویترز از نارنجی شدن آسمان یک روستا در استان بریتیش کلمبیا خبر می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679817" target="_blank">📅 23:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679816">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
سناریوی تازه درباره احتمال حمله آمریکا به کوه کلنگ
👇
khabarfoori.com/fa/tiny/news-3236499
🔹
جزئیات تازه از پرونده قتل یک مداح؛ پای یک زن در میان است!
👇
khabarfoori.com/fa/tiny/news-3236583
🔹
ادعاهای جدید محمدباقر خرازی درباره رهبری آیت الله سیدمجتبی خامنه ای و شهادت سید ابراهیم رئیسی + ویدئو
👇
khabarfoori.com/fa/tiny/news-3236624
🔹
جنجال جراحی زیبایی ۴۰ میلیارد تومانی خواننده زن | چهره او چه تغییری کرد؟
👇
khabarfoori.com/fa/tiny/news-3236501
🔹
سلاح های خطرناک ترکیه | آنکارا با این چند اقدام مرموز می خواهد قدرت اول منطقه شود
👇
khabarfoori.com/fa/tiny/news-3236597
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/679816" target="_blank">📅 23:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
از سرگیری مجدد حملات یمن به مواضع مزدوران سعودی
🔹
سخنگوی نیروهای وابسته به مزدوران سعودی از آغاز دور جدیدی از حملات پهپادی و موشکی نیروهای مسلح یمن خبر داد و مدعی شد پدافند هوایی این ائتلاف در حال مقابله با آن‌ها است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/679815" target="_blank">📅 23:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43fe88aaf.mp4?token=pPxtiXmGrsYoU9Z3i2x__PVBf300UShfD2OEisV6qysXPU0w_viG4F23aeo4aRDPb-CQusP0QTMKfaZuvG9yi7jFnQiAMMLqCEUSyQyv49VYjL8OraA8BTnbT-4GJEUOu0zmn_5J9kws3U9oH-o9EgdQXIFVRKgHwwVhJ8PkqkZYyNEZ5bHDmQB6tI2bhaPM76KzNXpkEM2_e6IdP-VPiG0ji-iCu_TunEDT0BM6U1XavnTFUXe3Z_3tAVxkHEZQxa8zRjp2OdBkgZ46_HcNj4ShWlt_mVs6aAXY-u1Ix08NeIGFsp2Bd9xjcLHhzKeIhhvtz7kG8NFnO-vGYxuFIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43fe88aaf.mp4?token=pPxtiXmGrsYoU9Z3i2x__PVBf300UShfD2OEisV6qysXPU0w_viG4F23aeo4aRDPb-CQusP0QTMKfaZuvG9yi7jFnQiAMMLqCEUSyQyv49VYjL8OraA8BTnbT-4GJEUOu0zmn_5J9kws3U9oH-o9EgdQXIFVRKgHwwVhJ8PkqkZYyNEZ5bHDmQB6tI2bhaPM76KzNXpkEM2_e6IdP-VPiG0ji-iCu_TunEDT0BM6U1XavnTFUXe3Z_3tAVxkHEZQxa8zRjp2OdBkgZ46_HcNj4ShWlt_mVs6aAXY-u1Ix08NeIGFsp2Bd9xjcLHhzKeIhhvtz7kG8NFnO-vGYxuFIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشاره‌ رئیس‌جمهور به فعالیت شبانه‌روزی وزیر‌خارجه با چاشنی شوخی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/679814" target="_blank">📅 23:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عربستان و سودان، شورای همکاری و هماهنگی استراتژیک تشکیل می‌دهند
🔹
دستور تعطیلی ساحل توسکا پس از مرگ ۶ جوان در رامسر
🔹
وزارت دفاع روسیه: امروز ۲۸۵ پهپاد اوکراینی را بر فراز خاک خود سرنگون کردیم
🔹
تعمیر پل آسیب دیده از حمله آمریکا در هرمزگان تا ۱۰ روز دیگر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/679813" target="_blank">📅 23:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679811">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukSVwJac2Pmgs3preeG-vIK4HDHli5oXn4NF9OJtQDsYSn3o7zG9bHjtEf-57Ns4MS4bJfuqZUhPF-rCjGr4hZBgfUtnqghQmHy7FxS6Ss7G4e_sqiVTaPpokbiu6xLKesgN4gFWJjwSFuJZWjp64YZC37P8hdgmmTMW3Rp9R8E0Jsk9LqGYL46lsZfuq6_1zNVxHQARxeG06YrTdm1bUiYY6O94jItsVQAs-v-MAk12Co9PAtUin9k0Bepq9XCsGwNP31g5rH1Q9GUqANq_EYrBRpCGA1TEdJ3AAF3-FRdFJMcsgvILl-L6JzYTKqfW3jr3_sDfG9-x7QEjmVkFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/448edf4631.mp4?token=rHpnRfMuyqXwEsA18QCu7esM4EWMWZmRvF2SUNvud4vVQ4ENAtlBe0GEiJVfwn1OzBJpP59K4QCVJCokqY2bZEC6LvX9TedJgXR0614FQrgngLMbTwfo_pB8LvmcVaPlGYjXyi38n1RP56NUwPPT5uKfzyMgmhRS6hFj9vYb3sb6cdkRbiBzYqSTrH3GfXvFCiFYoXkKvlMSgf6GdXOgeCCfc9C6HBpyld16vfmp3CzG2sX1Pqqfdcc6cB6NIHQ_JAz8fhOmEbd2IAvu5XVJPvFoRaBvS8tPFBWVbVQP1lA5gRxZenmCCvglq4wrt14clVtW2IoYDuUhkSpHGHC7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/448edf4631.mp4?token=rHpnRfMuyqXwEsA18QCu7esM4EWMWZmRvF2SUNvud4vVQ4ENAtlBe0GEiJVfwn1OzBJpP59K4QCVJCokqY2bZEC6LvX9TedJgXR0614FQrgngLMbTwfo_pB8LvmcVaPlGYjXyi38n1RP56NUwPPT5uKfzyMgmhRS6hFj9vYb3sb6cdkRbiBzYqSTrH3GfXvFCiFYoXkKvlMSgf6GdXOgeCCfc9C6HBpyld16vfmp3CzG2sX1Pqqfdcc6cB6NIHQ_JAz8fhOmEbd2IAvu5XVJPvFoRaBvS8tPFBWVbVQP1lA5gRxZenmCCvglq4wrt14clVtW2IoYDuUhkSpHGHC7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توئیت سفارت ایران که آمار بازدیدکننده زیادی پیدا کرد
🔹
ترامپ رسماً از رئیس‌جمهور به اسب شخصی نتانیاهو ارتقا یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/679811" target="_blank">📅 23:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679810">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
با حکم حضرت آیت‌الله خامنه‌ای محسن رضایی به عنوان نماینده رهبر انقلاب در شورای عالی امنیت ملی منصوب شد
🔹
حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند.
🔹
باتوجه به…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/679810" target="_blank">📅 23:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679809">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های بالستیک و پهپاد یمن به مواضع ائتلاف سعودی در منطقه المخا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/679809" target="_blank">📅 23:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679808">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❇️
کمک فوری برای درمان 2پدری که حالشان خوب نیست
🔹
پدری ست بیمار، مدتی است به دلیل سکته در بیمارستان بستری است و تحت درمان قرار دارد نیاز به عمل دارد که هزینه آن حدود 25 میلیون تومان است ، وضعیت مالی فرزندانش نیز خوب نیست و نیاز به کمک مالی برای درمان دارد.
🔹
مورد دوم:پدری ست جوان، یک فرزند دارد متاسفانه به دلیل سرطان معده  تحت شیمی درمانی قرار دارد نیاز به دارو دارد ، هزینه دارو بالاست هر دو هفته بیش از 40 میلیون نیاز داردبه دلیل ضعف بدنی توانایی کارگری ندارد و با کمک مردم امرار معاش می‌کنند.
🔹
مورد سوم:دختری ست جوان ، پدرش به دلیل فقط مالی توان تامین جهیزیه اش را ندارد و بیش از یکسال است که عقد کرده ، نیاز به کمک مالی برای تامین چند قلم جهیزیه دارد.
✔
پرداخت انلاین خیریه نسیم وصال:
http://www.nasimevesal.ir/payment-new
شماره کارت بانک ملت : ۶۱۰۴۳۳۷۸۱۱۴۱۶۲۳۷
شماره حساب بانک ملت: ۵۸۹۸۷۷۱۴۶۵
شماره کارت بانک ملی: 6037997599156198
شماره حساب بانک ملی: 0219934010000
شماره شبا: IR310120020000005898771465</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/679808" target="_blank">📅 23:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679807">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های بالستیک و پهپاد یمن به مواضع ائتلاف سعودی در منطقه المخا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/679807" target="_blank">📅 23:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGTx0yvPv2Akc-F0Yo0tvgbIh4JVJRtdFOSZzdQYq7niqQv0wQgNfHtJrRW5bDQaEifJuPi9eQ7mdpiBHXtv5mmVZBR-1JlPWd9SdkvmXYfxlKEo2b7lupYfuS8EzOOyUE0hdz1ZADyd1oiiCSXmfklCQYLQ8NErkF-FjOSUoiyBoLErDtRiKy9Vuv6lBe9Xvcr5-jJ2jVU0O-uv7vrznVKSEanUK5B148oxAL506V2IPavWe7TtcwtOg-wLtexM4sl8TcSXOXrQkSpKT2fGTQsNUd0w1oOY2cdop1mlMMGPV_dzkV2v2VWC185uvVoDfz_TdWyJPU_kKLzn5Od5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور: با حکم ریاست جمهوری اسلامی ایران دکتر مسعود پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/679805" target="_blank">📅 22:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onq8VovS0T-LVP_jhGsemJPQ9fwvbrvEnSdhmz-dheiJWlYrXwvaImELytOeaSwjQIP-tHwXiH1jIxhRXD1X7XuCkqNCXWJjmjxutWxtb6Av1Sw9FxooqIdiazWyCRHkrrRSP6hvamkcIrFchFFSm4xZEpqPHw0GQjpsHywfl_1jyClWSaQdKGyPbeNP6sCRU-5_QRu0NJkGR8IqMH4Y4F462KypY3rYbfDvu49gXiWHNrjOoS3OE4jQlDbDzxtFm3UwStLn9MP8-KkF5I1JEPCm8fvA114VatY8Uj3JFK4FPXz6hKjJUhEPQ2S-o8wM3B3YFJEUMJvA7EZcQuAk8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار امنیت
🔹
با حکم دکتر مسعود پزشکیان، رئیس‌جمهور، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد. رضایی با این حکم، مسئولیت دبیرخانه یکی از مهم‌ترین نهادهای تصمیم‌گیر در حوزه امنیت ملی کشور را بر عهده خواهد گرفت.
🔹
هشتصدوسی‌‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/679804" target="_blank">📅 22:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679802">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c8ba41d7.mp4?token=a89emb1mWuh2nUhuJXQaQ37Cq8vjseYxZ13XNNw5mHQl2_gddsThZzreFch4deazGgSEqeqEhMWwY6t9sPEnp2WzUgiUESzGijxATQGRnf8mWLblG1Og6t3T0uNnjCSyjZfTIB0mWh_4qeNerRNqpGMwiehK1rspDrxjz3bfaTvA9Ce7eSp7N_2OoSa7GE8GCcE31lb2ogBMypfw10qcjFYdPuELiyOTTjaRxQLQjMiQpZQ_glATXw0aelvhGn8psNbZ_I56WPMSlYDyxqgS3Mg6h3qmEMJoUiCn5-5YI6bBQO1BtIX2cJtDHVkSbcN0v10tEWZ2tUYpBAsY79Tr3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c8ba41d7.mp4?token=a89emb1mWuh2nUhuJXQaQ37Cq8vjseYxZ13XNNw5mHQl2_gddsThZzreFch4deazGgSEqeqEhMWwY6t9sPEnp2WzUgiUESzGijxATQGRnf8mWLblG1Og6t3T0uNnjCSyjZfTIB0mWh_4qeNerRNqpGMwiehK1rspDrxjz3bfaTvA9Ce7eSp7N_2OoSa7GE8GCcE31lb2ogBMypfw10qcjFYdPuELiyOTTjaRxQLQjMiQpZQ_glATXw0aelvhGn8psNbZ_I56WPMSlYDyxqgS3Mg6h3qmEMJoUiCn5-5YI6bBQO1BtIX2cJtDHVkSbcN0v10tEWZ2tUYpBAsY79Tr3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: تصمیم‌های مهمی مانند بنزین را نمی‌توان با دستور ناگهانی اجرا کرد  رئیس جمهور:
🔹
تصمیم‌های مهمی مانند موضوع بنزین را نمی‌توان با دستور ناگهانی اجرا کرد؛ باید در داخل و خارج دولت درباره دغدغه‌ها به تفاهم و نگاه مشترک برسیم تا اجرای تصمیم، کشور را با…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/679802" target="_blank">📅 22:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679801">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
کارشناسان چینی: ادعای ترامپ درباره بازگشایی سریع تنگه هرمز، صرفاً یک خوش‌خیالی و خیالبافی یک‌طرفه از سوی آمریکا است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/679801" target="_blank">📅 22:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679799">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
زاکانی: آمریکا در سمت عمان مسیر اختصاصی باز کرد / نقض تفاهم‌نامه اسلام‌آباد از سوی ایران نبود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/679799" target="_blank">📅 22:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679797">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVIcBgqZKVC1nVxfSNmBu8sHHpWEd_PA8UZyW3YbyBjoZ3r3aYmQo3mb5FWmM2HIhtdLkuIeGIjQRq8RTzbddeKburFl0YWS57wx6-uHFIiS-WgFAAsPHALHBIE_GdYoM9JlkRyQLnw0rp5wusw3_LZXu2sjDZu4EVfWsURaeKE8JJL97ucMBlbegAOndAh8zU130xIc3KbLzZO-uQlci_KJuyiJSPVNXt9_HjEMIEgNK0kOA-y9lTOsnkpJplZ9USFr5fKmM2F9wZxbzG_P316aKfU4pRiYfvzcIUNOFOseaIBwwbAEvNFNbHOHBMfMOnZDd39PSZYyXEw1kJaCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای اولین بار فروش مستقیم
در اتونوین
🚨
برای اولین بار عرضه مستقیم خودرو 《های وارداتی》 در اتونوین در تاریخ  1405/05/19
🔔
در این روش، مشتری بدون نیاز به بلوکه کردن پول، وکالتی کردن حساب و قرعه‌کشی، می‌تواند خودروی مدنظر را انتخاب کرده و
۱۰ درصد قیمت
را به حساب شرکت واردکننده واریز کند و سپس برای تکمیل وجه و عقد قرارداد در سایت شرکت عرضه کننده اقدام نماید
📌
اطلاعات تکمیلی مدل‌های قابل عرضه در این مرحله از طریق پلتفرم اتونوین در بخش فوروش قابل مشاهده است.
✅
اخبار و اطلاعیه رسمی عرضه های آتی در پلتفرم اتونوین را از شبکه های اجتماعی اتونوین دنبال کنید :
👇
👇
📲
تلگرام
💻
کانال بله
📸
اینستاگرام
🖥
سایت اتو نوین</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/679797" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679796">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhpXF569MGsya2V97cPha1tkSNEj3y4UdhW8vtDnUF4lJYkttbNnAGF6sDwEO_SkTFHUGWS62hV1p1FugAeceezesmRtJlRVE7h1VrDYCj8Lxj3TnmMYUe_y2lTrMG_qPiZcBBaS4on3NJA55fUbMiKnxHaBa1Vi_Jpecfrl9RKhlpRVxmSxe1-PuKgyNFG6m92eXWbizDPGD25H85GGvgpVOy1fi0X-lkDM7b9RROdcOR513tlHdM3y5mLtaF-68QBZm3S-5RMZpHXR8UYPk5XUE0EDiKkKsxggUOq_MUJMYbUQ3AJgVZdw55i8qQ4eBwSYwUHMbKbmn_rRkpwXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زندگینامه محسن رضایی دبیر جدید شورای عالی امنیت‌ملی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/679796" target="_blank">📅 22:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18b6ab1f9.mp4?token=MVdvuDTyRtRLG5fBJ3Sw9K87ZUKYT5LjfG_StlJ2jj6A_AccTBxWC_-_TkVCsWaswiSpLL-v8pd7bi7nLZaZs7pB4PEzwmCtOamcZ5_7VFkSIx81qhY6AV6B9wPmO5VL6d_ufIyciuUPzs17XOadiZnQUZnbLj1e0nkhQ7MAtLlr4wRWO5KzfEFfyXtlgI_vlSx5C62t-boUqOVT1Y0xYW7geCZtPKo9KjBy2zTTUZ-xjVJwSmu69YWBcGkQgh15D-yFLqT_XvU2AY-hlsUFEsx53GgpoUmfwrpWzG6VmsU4uyIAg7jUyvrt01_k3_F0vspwvOcx7gdsb95ynPBPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18b6ab1f9.mp4?token=MVdvuDTyRtRLG5fBJ3Sw9K87ZUKYT5LjfG_StlJ2jj6A_AccTBxWC_-_TkVCsWaswiSpLL-v8pd7bi7nLZaZs7pB4PEzwmCtOamcZ5_7VFkSIx81qhY6AV6B9wPmO5VL6d_ufIyciuUPzs17XOadiZnQUZnbLj1e0nkhQ7MAtLlr4wRWO5KzfEFfyXtlgI_vlSx5C62t-boUqOVT1Y0xYW7geCZtPKo9KjBy2zTTUZ-xjVJwSmu69YWBcGkQgh15D-yFLqT_XvU2AY-hlsUFEsx53GgpoUmfwrpWzG6VmsU4uyIAg7jUyvrt01_k3_F0vspwvOcx7gdsb95ynPBPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع «حادثه امنیتی» در نزدیکی باشگاه گلف ترامپ در نیوجرسی
🔹
فرماندهی دفاع هوافضای آمریکای شمالی اعلام کرد جنگنده‌های این واحد، دو فروند هواپیما را که به حریم هوایی ممنوعه در نزدیکی باشگاه گلف دونالد ترامپ در بیدمینستر ایالت نیوجرسی وارد شده بودند، رهگیری کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/679793" target="_blank">📅 22:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJLsm-29PfFRxR0qyR0VZ98qUVlNQMhfmrb6ERb_d0py7e42Fnk42H6GVjfz2bKi02wCr_dNj2K__E38vRMmnpRAz6oQZyXD-lZ7VgHTZVRYOvk68U51qcgWSeDravyOPscEi_K1V3uWvJg03Ut96eZ0BLZs6vR6pHFDfJXhwpfxdSDsAl_IwHjE0XNSXcPzKrt8TUCS7wEDzAFu5zRSP8u5fbUsJQQZzzHsP2eYjIkaSrDcmMB8mmqOHo2F_kuFGTkC2CVlt2HCxsJ838vehaKB0f0VUr4ndoRmrxtayus-feWggiBYXrDuFmEsLzcRUAV_fUTHfQV2GMziHA2-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات جدید از ضربات ایران به یکی از مهم‌ترین مراکز ارتش آمریکا
🔹
بررسی های اطلاعاتی نشان می‌دهد که در جریان عملیات «وعده صادق ۴» و هم‌زمان با پاسخ نظامی ایران در ۲۸ فوریه ۲۰۲۶، پایگاه هوایی الظفره در امارات طی چند موج حمله پهپادی هدف قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/679792" target="_blank">📅 22:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679791">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MID_7adHGYZO2DhzzM0AGt4NNMOl4i_6JjZaiDa6UlL5wn_MUiGxOawVQfSmXS2qVL6uElz3zUxH6dbvvG6qcud99PU_kRm3TRExLrgdg27YGU9jbcPmraPEIzkMhStCo6rwh63-Pt2K5Fy4CpU1lpZYeewjZVGFjHJzPmtv2v2KU2bqN3MwYxrDqukkmT7NShAV-Idw1OJUS1yakr9F_EtnIcTnjbaC-HjLJTIW_6MfNaUmZvMAmw2OE3TufWaGD_vna_LoxiVBfVhUmlqp0q6EjMbC5ao4H1f7UCwGhdByCHsIh1cuI1PXsDdKIg79RGI1ls6YhTzwVvMgKjK04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسی که نعمت‌های کوچک را نبیند، قدر نعمت‌های بزرگ را هم نخواهد دانست
🔹
این سخن یادآوری می‌کند که شکرگزاری فقط برای داشته‌های بزرگ نیست. توجه به نعمت‌های ساده و روزمره، نگاه انسان را عوض می‌کند و او را برای دریافت و حفظ نعمت‌های بیشتر آماده‌تر می‌سازد. #ن…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/679791" target="_blank">📅 22:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679788">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
توضیحات رئیس کمیسیون امنیت ملی پیرامون تصویب کلیات طرح اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگه هرمز و خلیج فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/679788" target="_blank">📅 21:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679787">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/679787" target="_blank">📅 21:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679785">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOOPAvi9RqUVDB85F2W0LDMHOOw37E8WPhh1pGILYhUvS-2QLrqp-OX-ICo-tK1t_i6hvGnMDQJdzb7Jf2zv320a7NZxOHDyAztPajG85iIjSPD7sCMnqAlERyNs2E-j4ZueYtZRtm4Rduye5KoMkLa9_9N-UeRI0268aFb6nQX0ZMx4slOhpYdr7I9bP5zFIXA-qTqm9qM0q6G9App5YbkEjZQ2N2CXU4VcvcPoEfNP-uJhxvkRZuuGzGprnUVKhGpPLEYie1HWhEULNLn374p4T1aI2DKtO30SRaJesW62SUn6VzqSwvOSpGcRafE2Bp8cwSF3dlkrflpcuzY7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس قدیمی از مسی در کنار خانواده و فداکاری مهم پدر
🔹
وقتی لیونل مسی ۱۲ ساله بود، پدرش از او پرسید: می‌خواهی به روساریو برگردی و در کنار خانواده‌ات بمانی، یا در بارسلونا بمانی و به آکادمی لاماسیا بپیوندی؟
🔹
مسی تصمیم گرفت در بارسلونا بماند. پس از این تصمیم،…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/679785" target="_blank">📅 21:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679784">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fbbd9ebf.mp4?token=YhcnOmuoAFBlCPknPOko_yIPAH00qJKgODgMXWPMs-AGNtE2E04muXqj_Yv1tcPgig2xKxM9VI5XKTr0I5zobAjuiiO3dhUyvkl7bCsWTYjWeSc8CRecs7Dntke61M8iq91QkkRymBhgbGQ05S55sIpI6c-ZhqAgIJDZ8jvgsl_W7iTkdHsTcHWBibKd_qmTA9Fu885isT7Atmnia3iib8BFp9IUU4smf8KlPOXI2haCUuAZ_SK7ZLxzwFqQqgHp-DSOMnuzklGePJt_yt8xereG5Y6oifcua7vtLpqEXeSfMwIFYeMtQCpJtdzN_5KK_AwhpImxxRB-EV_0ePE2Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fbbd9ebf.mp4?token=YhcnOmuoAFBlCPknPOko_yIPAH00qJKgODgMXWPMs-AGNtE2E04muXqj_Yv1tcPgig2xKxM9VI5XKTr0I5zobAjuiiO3dhUyvkl7bCsWTYjWeSc8CRecs7Dntke61M8iq91QkkRymBhgbGQ05S55sIpI6c-ZhqAgIJDZ8jvgsl_W7iTkdHsTcHWBibKd_qmTA9Fu885isT7Atmnia3iib8BFp9IUU4smf8KlPOXI2haCUuAZ_SK7ZLxzwFqQqgHp-DSOMnuzklGePJt_yt8xereG5Y6oifcua7vtLpqEXeSfMwIFYeMtQCpJtdzN_5KK_AwhpImxxRB-EV_0ePE2Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس سازمان پزشکی قانونی کل کشور: ۳ هزار و ۵۱۹ شهید در جنگ رمضان داشتیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/679784" target="_blank">📅 21:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679783">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjJw0hjstgEEFzIWOIX-fac128wHypjlC4HwL_VtI85YsILTSnTgYS5ulv-4lh68dTtPAj1Hcm036PadqMkAmcdy6aahmLIE0xfSW54Bvgk0aefDm7-Y8pIH6JnG0lMtxL0JGmi63hZR5pAMOT2JuXViINo37j2IeAcgnPQr-TZLQJnk1eNcho-06QAWQxlRbgtR-_5NXDUNBNjCYgH3UCq0-fyo0-YGnb4qo0ocP89DEzKf6IuDdmcSiMF-IZM7xwwuhUQ1Xb8aEvthsUuAWcd71mE9A7kaAfbyZkOqzYCaTAk29oax-7iEXiOjuQRoQyAFb7zAjEDwASfg9BJefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امکان مینا
🔹
کارگردان: کمال تبریزی
🔹
ژانر: درام، عاشقانه، سیاسی
🔹
بازیگران: میلاد کی‌مرام، مینا ساداتی، شایسته ایرانی، بهرنگ علوی و…  خلاصه داستان:
🔹
مهران، خبرنگاری جوان، زندگی آرامی در کنار همسرش مینا دارد؛ تا اینکه نشانه‌هایی عجیب، او را به رازی می‌رساند…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/679783" target="_blank">📅 21:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679782">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای کانال ۱۳ اسرائیل: اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/679782" target="_blank">📅 21:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679779">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5455897411.mp4?token=MYYpJOj_DzkoteDSSviDjqlQNl0EFhKgOmdL5GWGNPC7fE2VS4DyAlvMJBO-zfVsADsPhSveZ-jQGKoAuUbzUQAtLHhhNMJtuuhhiFL-bb8lJF-Vp34cZtOaEG8vOhwg4cjdRlDp2Mr5jwFQbZaSit-lky3mZy1ZB85o_cNvguerSkF-FFgl6faw5M7DkclHavtz0ZoCTePMamBksVtz6GXpZo0O3dtLdMTP43S7v3nmVghiI7npqvG4ybJi_mS3mfwH9zLoZVnnKp75CBRr-p7jslkB4fRYq92CqMynQu3RmoQJIsl2HFOIbO4HTZv1FiPciWsUTbRiW5KalC38eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5455897411.mp4?token=MYYpJOj_DzkoteDSSviDjqlQNl0EFhKgOmdL5GWGNPC7fE2VS4DyAlvMJBO-zfVsADsPhSveZ-jQGKoAuUbzUQAtLHhhNMJtuuhhiFL-bb8lJF-Vp34cZtOaEG8vOhwg4cjdRlDp2Mr5jwFQbZaSit-lky3mZy1ZB85o_cNvguerSkF-FFgl6faw5M7DkclHavtz0ZoCTePMamBksVtz6GXpZo0O3dtLdMTP43S7v3nmVghiI7npqvG4ybJi_mS3mfwH9zLoZVnnKp75CBRr-p7jslkB4fRYq92CqMynQu3RmoQJIsl2HFOIbO4HTZv1FiPciWsUTbRiW5KalC38eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک نقل‌قول جعلی منتسب به سردار وحیدی چگونه از هند به سخنرانی نتانیاهو رسید؟
🔹
هفتۀ گذشته نتانیاهو، نخست‌وزیر رژیم صهیونیستی گفت شنیدیم احمد وحیدی، فرمانده سپاه پاسداران به صراحت قصد ایران برای ادامه توسعه سلاح هسته‌ای را اعلام کرده است
🔹
درحالی‌که برای این ادعای نتانیاهو هیچ منبع اولیه‌ای پیدا نشده است؛ نه ویدئویی از اظهارات سردار وحیدی، نه متن سخنرانی، نه گزارش رسانه‌های رسمی ایران و نه تأیید مستقل خبرگزاری‌های معتبر بین‌المللی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/679779" target="_blank">📅 21:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa5gi5INOOdcxU2Iee198BNObY0fW8cIlFLc8uTSO1QuKG5qwF-WqugQ0ubEIdeiB9xrTKpTOuMQ_vE_LZMPb5yxuevWoG9NtuMCOFT4gnmHURJDYqq1Qf3i6cEgifUecddte_Yrm9XsApunMdu5qCipOCF8rsOcjNeVE7LE03DePQI_19bo_AFcs_ItfMrSA59tNBuFcBtY8VOd0Ca3k2GuNSKGTPXUVeET7Jo8UVSkcmj6fl-1RGORqZv5DIJthLFHDlRfGoWVWrb20LRa6s9LkUURj0107UTi7I7wGM53hoKhbKY3WC27wikiPWgUBR3nSDTw4v8VmvmHp3ZRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حکم حضرت آیت‌الله خامنه‌ای محسن رضایی به عنوان نماینده رهبر انقلاب در شورای عالی امنیت ملی منصوب شد
🔹
حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند.
🔹
باتوجه به…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/679778" target="_blank">📅 21:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679777">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
انتصاب دکتر ذوالقدر به عنوان مشاور سیاسی رهبر معظم انقلاب
🔹
رهبر انقلاب اسلامی در حکمی آقای دکتر ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔹
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
بسم الله الرحمن الرحیم
🔹
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر؛ باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/679777" target="_blank">📅 21:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679775">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUnfz6rMb0-QnfXfKEkKbYyIvX6JafF6NkbHJlJYcLYQk8ul6fIeRtTpSdD8ss6qU29KgOWtEiczcgxAuzpze_zRiwNnNczBXW9qvWC7bfWt9BNLPVgsP-z-_3sGFCLGvaivXvaF05aH1DeB98iTQHKSHyzzhFVyMGMaD_qyonWSZEkDLZsT5kKKyaDGpp_khJCzV0-hRYPhjQwgkgj1ZAWOHmT9lYxGf1gA6ooFw4jHfjX306AyoE60fjL649iMD5QWKv_6y-graHh1nrLUzQmzBlm_9alH2_QPDxD8ykFqA5dkV33kfdOyjR3xBqsgDfEQidwo61WdHgvqDcQY7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگاری که نامش با «روز خبرنگار» برای همیشه ماندگار شد؛ محمود صارمی
🔹
محمود صارمی، خبرنگار خبرگزاری جمهوری اسلامی ایران، در سال ۱۳۷۷ هنگام انجام مأموریت خبری در مزارشریف افغانستان جان باخت. شهادت او یادآور خبرنگارانی است که برای رساندن حقیقت، حتی در سخت‌ترین…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/679775" target="_blank">📅 21:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679774">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HITaXt4GRrvl3SG1fgSVmx3OqpFKKAQowSBubHPO3ddpyjfodHAJ6ZEP01NTPCbI8bzE199d9N4COUq1rllS_CSdj454asQZROWQDFzWahkrzQ9_0uXnkwkmrHWsG4LM-QKuIY6fem6g88GnyIxLolKp4u7d-EvooV4BYb6P2kNRMhyDAy-lX8IyI_YhbCngkr9etVntU9UOMbad89z5i2ltPr5O0Woy2gMkrPE7-5o7s6LrC7zZiKmhIn2SEwPF_wlNkAyoekdw53F_Lt5gsK1FJW1Z3wBTnvEKNQXZPpei2PunWIMWCIlYrOFHwDe9aAoW7bAJDa0TyvF6ZvTGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
📍
فرصت ویژه دندانپزشکی
📍
📍
🦷
در کلینیک
سرو cip سعادت آباد
✅
۵۰٪تخفیف لیست قیمت
✅
۱۰ سال ضمانت نامه و پالیش رایگان
✅
شرایط پرداخت اقساطی بلند مدت ۱ تا ۱۲ ماه بدون سود و بهره
✅
۲ واحد کامپوزیت رایگان
✅
تخفیف‌های ویژه محدود
👇🏻
👇🏻
برای
✨
۱۹ نفر
✨
رزرو امروز
همین حالا به آیدی تلگرام زیر پیام دهید
👇🏻
👇🏻
@Sabericlinicvip
شماره تماس
👇🏻
09384307498
📩
ظرفیت پذیرش شرایط ویژه محدود است
پیج ما رو دنبال کنید
😍
✅
👇🏻
https://www.instagram.com/p/DblisM0iNTa/?igsh=YXZ3MnZ6d214Y2Zr
sarv_royal_dental
✨</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/679774" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679773">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-vmwuXECtFfqh4Br_JDGY3XVQp5HBtyUQXoqOBCACB2Qa_sRY3EuRcxqh-g4fzI9PbsY2r8cuD0CZO5zN0taaBTDXG3pXH16INPBqhDGZ3SYREhxS0gZfzDa_O0Q-QmYEF-jrq5XIv_hdftXeTIdAooymfmttlENXswtmGCRvE3P3CfEwBu-q5X4z50F-gnaHlwAKj-6RwQNJbEA_--LinAxdrT_jBzs_otp9i0Tc5zGvcKFsXE09Uu3rC2ekRQuhrMVOkAIgIUnFKoifrOLDFIEVufiHVawEaESjqfpjt399E-FVxRAICqLCdwCWrglF2uSC4lvSVK8A0E5Dp3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی ابریشمی، انتخابی مطمئن برای معاملات ارزی شما
✨
💵
خرید و فروش انواع ارز با نرخ‌های رقابتی
🌍
انجام حواله‌های ارزی به سراسر دنیا
🔒
تضمین امنیت، سرعت و شفافیت در تراکنش‌ها
✅
اعتماد شما، سرمایه ماست
راه های ارتباطی با ما:
☑️
شماره تماس: 09158516875
☑️
لینک کانال  تلگرام :
@abrishamiexchangee
لینک واتساپ :
https://wa.me/message/32HOPV4AHR2HG
اینستاگرام :
‌Instagram.com/sarafi_abrishami</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/679773" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679772">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvArDR8_4UYLfigJudaO5chgQF8Siv7h1gZtWXT-WaeFbOd2Gq2yuyLgN737hkupBU0fjSMERVI0WeG02_ZofmS-aShJgB7JCbzrS6Fp8G0mpbcjZwzAEHioIr6TnaahiKS3qcGnef4uxQViEkUpKqeQTFFF_WCjoNcGdlNxr-NF51wsTyKOCwahAFyPH0lVLXJBsq38HaDjpPxlHKHx82peMEi21jwlqmv6guqWuIc4YD42eQ9AGc-6v4ZqYXaJ54NSSsY-6l0LvJuC1g1ORMHYXQQDwoYag6iKfYnTcYL0UCfEdd7YW8mvbuWuxdfCIyR6AHAbWhDRbtjxPAUTCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز عجیب پنجه‌های کوالا؛ اثر انگشتی که با انسان اشتباه گرفته می‌شود
🐨
🔹
کوالاها اثر انگشتی بسیار مشابه با اثر انگشت انسان دارند، طوری که اگر ناآگاهانه توسط یک محقق پزشکی قانونی بررسی شود، او حتی نمی‌فهمد که این اثر انگشت انسان نبوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/679772" target="_blank">📅 20:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679771">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
احتمال پرداخت معوقات افزایش حقوق بازنشستگان تأمین اجتماعی از ۱۰ شهریورماه
🔹
پزشکی قانونی: ۴۰ درصد از شهدای دو جنگ اخیر با استفاده از علم ژنتیک شناسایی شدند
🔹
رئیس لالیگا: دوران اینفانتینو به پایان رسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/679771" target="_blank">📅 20:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679770">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwBjgq7bRXSmyw8LfF3eTPZfhUo3QOACFGfB7RfxB-PQN4Mo26hK2SA2GXrni_HgWZ6VZCp8cGQqoHhqLVwiWC-UCtp6MlIpFV_9il4AL8hU5ce4cUGMode5bkurwjqqmnCp12vTQhLr0Drjkd3MW4algO60zwhensaAEsi9a43b1SqY19vxUPtwsqr8rLxD3tAga_UaljIWCvKPkzPNWw14kVtOS2CLkpkgKATPf_OwR574GBI51hx4FPfpF8vC9bRVLLjIp06viEJFlGvLfv3dyd5eAESEcGOnkIdwJtxRwMko9kkN4WtOgnG_sVVutZT07A5g8rInlaEbduxF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
هیئت غریب مدینه برگزار می‌کند؛
مراسم عزاداری ۴ شب پایانی ماه صفر
🔹
سخنران: حجت الاسلام دکتر رفیعی
🔹
مداحان: کربلایی جواد مقدم و حاج سیدرضا تحویلدار
🔹
با اجرای: رسالت بوذری
⏰
از دوشنبه ۱۹ مرداد - ساعت ۲۲:۳۰
📍
مکان: حرم مطهر رضوی - صحن غدیر</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/679770" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679767">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ شیاد درباره رفت‌وبرگشت‌ها و کشمکش‌های جاری میان ایران و آمریکا: همه‌چیز درست خواهد شد؛ همیشه درست می‌شود، این مثل یک بازی شطرنج است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/679767" target="_blank">📅 20:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
با آرامش با ایران تعامل می‌کنیم
!
ترامپ جنایتکار در مصاحبه با آکسیوس:
🔹
ما با آرامش و بدون تشدید تنش، با ایران تعامل می‌کنیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/679764" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuNc3zR6eoQRZCmpACo8XnNTFLqc_AQzf1MWMfUPOalYCt-gXGW4wYc3lRl-QgemM9F29ayJOj_yILH89gMkBHx_cWKJlI9uwr_0YGrXa2H2Dow4gzj9rv01Fc0gF0TWC048h-3eNil-HtXj00v7o2lknTPNJvTw57pbsgb7xJvKUQsOH9eUQ4xKJP73h1ztqqyWtepOtj1wSkJhl0br0egBTKRs2qLTUsrtwp7iVhLca1bb5ccGJFHUBHWS4zyqAFC8GAfQlKglm621xLFUCcA3N7hCvVSi7FyPparUsSo_OY2B7wBgfUMszTBeC0PFtpTqELn6t52qTi5pRrjK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حکم حضرت آیت‌الله خامنه‌ای محسن رضایی به عنوان نماینده رهبر انقلاب در شورای عالی امنیت ملی منصوب شد
🔹
حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند.
🔹
باتوجه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را که از پیشگامان دوره‌ پرافتخار هشت سال دفاع مقدس هستید، به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب می‌کنم. امیدوارم در انجام این مسئولیت مهم، کمال موفقیت را کسب کنید.
🔹
ضمنا از تلاش شبانه‌روزی محمد باقر ذوالقدر تشکر می‌شود. إن‌شاء‌الله تحت توجهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله تعالی فرجه‌الشریف همواره سربازی مجاهد برای ملت سرافراز ایران باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/679763" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
روایت تجربه‌ای متفاوت از دو مادر؛ از جدایی روح تا بازگشت به زندگی برای فرزند
🔹
00:07:00 حضور ناگهانی بدن‌های انشایی در همه جای اتاق
🔹
00:24:40 ارتباط صمیمی با موجود عجیب بلوری
🔹
00:33:00 بزرگی روح و سختی ورود به جسم
🔹
00:45:40 قدرت چند برابری در وسعت بینایی و شنیداری
🔹
00:50:40 تأکید هدایت‌گر به خوردن سیب بهشتی و امتناع کردن من از آن
🔹
01:03:45 ادامه یافتن صحبت با ۲ هدایت‌گر برزخی بعد از بازگشت به جسم
🔹
01:13:00 رعایت حجاب، نماز، اطاعت از همسر بعد از تجربه
🔹
قسمت بیست‌وششم (نخستین نفس)، فصل پنجم
🔹
#تجربه‌گر
: منیره محمدی/ نفیسه متعبد
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/679762" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y60jqdpp7umfQmu5fD232zUDU_V8rrXZUPlOx0seOPf7P-_CTDUukuQ3URpDEtu88As3UQZsnBAKDuev48L9otMmDbpuXPdgAIFjktXvqbgoypfs38ft8yMCJPhGbOGkxgDr-e1G9ETP_7Uw5rC8ku5iNNu2PkPAKDhTjK8QvoE1EyRcVIdCLSPDMP64HtwA5A3RUv2lJB4jTn-sEYF--_5rZo-_FjSIXxMJVdXGuAa8VgjvJNoyS_t0p8Asn5yPDpmUCx2kI8nLkukCyhEWg_qGhDVmK-ngpmUKCnTALsAcqfNLK0CN0yypT7SI6hBNzZ9-drIBkt9GVNbeJNbJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنجال جراحی زیبایی ۴۰ میلیارد تومانی خواننده زن | چهره او چه تغییری کرد؟ + عکس
🔹
ابرو گوندش، خواننده شناخته‌شده موسیقی ترکیه، بار دیگر به یکی از سوژه‌های داغ رسانه‌های این کشور تبدیل شده است؛ اما این‌بار نه به دلیل انتشار ترانه یا برگزاری کنسرت، بلکه به‌خاطر تغییر محسوس چهره‌اش پس از انجام یک عمل زیبایی.
بیشتر بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3236501</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/679760" target="_blank">📅 20:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boHXMkW7prRPXZISfBqhwvCEqkYQ0rx8DhdkYm4t8tIYwQdRbHhjVl4ymuYfoAq0bephJf0uMuMxks7g2kei-M3Nnaij3XIXfSEBPdyyN8XhPaB6VGshCZxeycq35SA2ruKF-is5O3004pkI6tVpsM2BvZUh3wHxcRHcvI3ZrJdlZE4ObialqtQ9kcj0Kl6b0DUOID7ErKdqsn8yIg7q27E-55Zgr1c1K2n4Y837SLjRoD8gOyFIZwzYb85VoqttqV1W9ansHKerKT2bpVMkiJ7VBXmvZlQrW933-ngDYYT5xFygbGUhYIGJLAd7Re4H6AIOIsDI0ctPh85JDxzvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسواییِ دشمنانِ ملت ایران با انتشار تصاویر حضور امام سیدمجتبی خامنه‌ای در میان مردم و جلسات با فرماندهان نیروهای مسلح در آینده
🔹
جانشین سازمان بسیج مستضعفین در آیین تکریم و معارفه معاونین نمایندگی ولی فقیه در سازمان بسیج مستضعفین:
🔹
تصاویر و مستنداتی که در آینده از حضور رهبر معزز و فرمانده کل قوا حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای (حفظه‌الله) در میان مردم و کوچه و خیابان و جلسات با فرماندهان نیروهای مسلح منتشر خواهد شد، بار دیگر موجب رسوایی دشمنان و بدخواهان ملت ایران خواهد شد.
مشروح خبر:
👇
basijnews.ir/00f14B
🔻
کانال خبرگزاری بسیج:
👇
@Basijnewsir</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/679756" target="_blank">📅 20:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679754">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713efbba80.mp4?token=QTBIgMRdnLXbkGrXKuf8MjiWJj4uE_Sfw2KwnquvXYJqxXCZ7eCHjVfFM1njeRT2Pn6N2-wqj9eVz0aXUN2iYnQ69MDQGqnnp1lNV4xWY2htOK1i7YJ92bj69K6vw7t8nzw8v2zV0hnGg-f5yc3fiESKFBiBF-N5zNF1RBpBEVqvNHufPE-NbTH96e0Ukbe1wiCZ59g3_mCyc2-B1RksI3KOhDgTYFMubcuFDr44BNqDXMI0oTf_tG_FzIAnB9jPrmNRkV2GuE7BbjqOyXaZDl16uWzmwdfkMAFBtX3ABDg7VMl0QuDjSTLyXnjpPQfcwnO0kW11pwIf5oRQIZejLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713efbba80.mp4?token=QTBIgMRdnLXbkGrXKuf8MjiWJj4uE_Sfw2KwnquvXYJqxXCZ7eCHjVfFM1njeRT2Pn6N2-wqj9eVz0aXUN2iYnQ69MDQGqnnp1lNV4xWY2htOK1i7YJ92bj69K6vw7t8nzw8v2zV0hnGg-f5yc3fiESKFBiBF-N5zNF1RBpBEVqvNHufPE-NbTH96e0Ukbe1wiCZ59g3_mCyc2-B1RksI3KOhDgTYFMubcuFDr44BNqDXMI0oTf_tG_FzIAnB9jPrmNRkV2GuE7BbjqOyXaZDl16uWzmwdfkMAFBtX3ABDg7VMl0QuDjSTLyXnjpPQfcwnO0kW11pwIf5oRQIZejLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مسئولان خبرنگار می‌شوند
🔹
دیروز به مناسبت روز خبرنگار این دفعه مسئولان از سلامی، خبرنگار صداوسیما چندتا سوال پرسیدن و باهاش مصاحبه کردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/679754" target="_blank">📅 20:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679753">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
پزشکیان: اگر به امید کشورهای دیگر بنشینیم شکست می‌خوریم
🔹
هیچ‌کس خود ما و مردم ما نمی‌شود. ما امیدمان را به خدا و مردم بستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/679753" target="_blank">📅 20:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679751">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVO-gxL-4dFxegdJWkIdrkKjy27J2v11YFK4PFS2Y6ihyK8_qFdHZ1mQYBPCgYbJpW7po2rM21awPJW_8Pgg8MQivOOPaqwFIHk7lf9lY1o3AG0P-v36s7Oetv7NkfNoE6JqyPnBDhKaZta3Ge31tShswduj4u5lkaY4-yZQnZiz2_5QkaYifhqbFiYOjrnyiI8sB6P62IxyUQ5Z32a3RKDtLtUfC00DPQhip_WqOAw0CjP3RQxmS5cOEyGZ3rzEaGfGPD_dLIFC3LhBPeipCrTXU8NPhEZCc8irJkGq7kPuPJMBYbEptplDofKyGURoVB7XeXRzWYz-qyb1rPM-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/679751" target="_blank">📅 20:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679750">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae43e83853.mp4?token=iwiScd6E7ImvnNjQyhicYeXEWoPvda4Me4udMqeYqf-6TyZrnQZhNBZV87miNPoK4vwmYBr0qzmKyMy6nt7gWnU7mC7BBPTJCYcQyw7WFNYz2fhqmI-HCpIIh3nsGPHqT3Pc3tjt-nC1sOBiZ2w4KEoFKqzOIoF5JzUh2iFM2CVD9C0Pk9eRSiOEX-rtRgy9dRGrbN34ajEqdzNCrQv_OBXMTv2Dja1FmbU5xUkxtrOa9Gya-Qyh67tP4qMMCQMlibyxPLuGYVKZyRG0_txxvT0EpGTxREohIsHlnq3z7f1W7-qzmj28ynqhFGwsfdhxPvUQY_LN3R9nY_qXZQel0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae43e83853.mp4?token=iwiScd6E7ImvnNjQyhicYeXEWoPvda4Me4udMqeYqf-6TyZrnQZhNBZV87miNPoK4vwmYBr0qzmKyMy6nt7gWnU7mC7BBPTJCYcQyw7WFNYz2fhqmI-HCpIIh3nsGPHqT3Pc3tjt-nC1sOBiZ2w4KEoFKqzOIoF5JzUh2iFM2CVD9C0Pk9eRSiOEX-rtRgy9dRGrbN34ajEqdzNCrQv_OBXMTv2Dja1FmbU5xUkxtrOa9Gya-Qyh67tP4qMMCQMlibyxPLuGYVKZyRG0_txxvT0EpGTxREohIsHlnq3z7f1W7-qzmj28ynqhFGwsfdhxPvUQY_LN3R9nY_qXZQel0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اگر به امید کشورهای دیگر بنشینیم شکست می‌خوریم
🔹
هیچ‌کس خود ما و مردم ما نمی‌شود. ما امیدمان را به خدا و مردم بستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/679750" target="_blank">📅 20:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679749">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaDGA9AnnVxjbHOHKU3yFUiKBvBopWpZSB3kEJ0yeO7jRAnv2uUVnrfZKkVb_sL6255meqjr6vkyo1Eg51Kj4ATzZ_NXzlW1oXoIkCSWt1Z46-ByZd7hupOqBD1uYTwWJhjwXx3ZwtppeynhAc_IE6yS1_ARzbLljxIuZN11DfJagfwPH_tw82sFgyB_qLHZCppGNkBlXJ_q4TzkediGTk0gRY8R6KD6Br5DnLKFPc_AxLxZkKoZUtKH14whYb45cDlbcPQWfoqMmNGTh2QOuK1rjt89CKCb0kzw4cG6rtS2GFRIRSIFL768pcbhQsYQI-eGlYVSJDj-G1czqcQJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
مام اسپری سورملینا
💥
✅
۱۰۰٪ حذف بوی بد عرق
✅
بدون حساسیت، بدون لک
✅
مناسب برای خانم‌ها و آقایان
✅
ماندگاری بالا با یک‌بار استفاده بعد از حمام
🔵
🟡
بسته ۲ عددی با رایحه اسپرت و دلپذیر
🔥
سفارش با تخفیف ویژه از لینک زیر
👇🏻
https://yeklinks.ir/mamtele?utm_source=foritel
https://yeklinks.ir/mamtele?utm_source=foritel
پرداخت درب منزل +ارسال رایگان</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/679749" target="_blank">📅 20:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679746">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtKLZB5nVWPewoShOxy4FNdhLvDDwugZDWhWj76SscsThvJQ8nL3d4cEpZtm1XgXGzW5ZCkvJWauwtHTasZQ2GJhm6LL5f6RD6RUXJbQa5uN7m0GjkGbP1bA0iKfwx6xOB67IJZMKVwhdy_knMfx5soCFDpvmTTsjkVaBupLgDbBypekyoLYcxEzgYaZyUP97sPwyQuMV0c_jsIydkHsjf6mDLSOpco_Zma60JQqjcRVnuhR6Oan_nYKBohgNiT7yOz7pLhLqXVk4A739SAe5o1mZBhqrWRCgRUGwag2KmBMVh-282R2G416EnLMmQqI2tvuxOh39q-tBrmr0s0sLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل تعاونی لنجداران: ممنوعیت واردات لوازم خانگی، درآمد ملوانان و شناورها را کاهش داده است
مجید کردوانی، مدیرعامل تعاونی لنجداران بوشهر:
🔹
از زمانی که ورود لوازم خانگی باتوجه به بخشنامه‌های اخیر ممنوع شد، شناورها و لنج‌های سنتی دیگر امکان واردات بسیاری از کالاهای مورد نیاز را ندارند.
🔹
با کاهش حجم فعالیت لنج‌ها، درآمد ملوانان و صاحبان شناورها کاهش یافته و مشکلات معیشتی برای آن‌ها ایجاد شده است.
🔹
مسئولان باید فعالیت‌های ته‌لنجی و ملوانی را گسترده‌تر و آزادتر کنند تا امکان ورود کالاهای بیشتری به بازار فراهم شود.
🔹
افزایش تردد شناورها به معنای ایجاد فرصت‌های شغلی و درآمد برای ملوانان، مالکان شناورها، صاحبان کالا و سایر شهروندانی است که به‌صورت مستقیم یا غیرمستقیم در این چرخه فعالیت می‌کنند.
🔹
کاهش هزینه‌ها و تشریفات گمرکی می‌تواند موجب شود کالا راحت‌تر و سریع‌تر به دست مردم برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/679746" target="_blank">📅 19:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679745">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d719b401.mp4?token=N88AZxTY0ZuXRzd3NlWYHw9H0TQ5K0kftGhpPxJEHMIhdOA5-iBqB_-Kn_1KzP_FrWcinXvdM8IkjbzlYC8BW0IyUIsL4DHsuVFyA2qK52gLoyyKCFvtuNuh9iW4HGaaWaHy1B7JYfbgFrUU4D5p4krNfYouLiqU1MOpc05Jv4ROVbX_kGRySbcaoQUcFwHGHgg9Z69mu2Cuh42zABlbpS5JYSS2hgeT2OCxn_uZX2AB1zmDrBX2oXPcWh5XH_Hhtw33dq5UsINl35RZQxgHvtFJDMUcHy9EYWqRTANdjQEXIiGIPqJQifLy1lE0s6_6HQjOBqReZDQ3DCYxd_dN6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d719b401.mp4?token=N88AZxTY0ZuXRzd3NlWYHw9H0TQ5K0kftGhpPxJEHMIhdOA5-iBqB_-Kn_1KzP_FrWcinXvdM8IkjbzlYC8BW0IyUIsL4DHsuVFyA2qK52gLoyyKCFvtuNuh9iW4HGaaWaHy1B7JYfbgFrUU4D5p4krNfYouLiqU1MOpc05Jv4ROVbX_kGRySbcaoQUcFwHGHgg9Z69mu2Cuh42zABlbpS5JYSS2hgeT2OCxn_uZX2AB1zmDrBX2oXPcWh5XH_Hhtw33dq5UsINl35RZQxgHvtFJDMUcHy9EYWqRTANdjQEXIiGIPqJQifLy1lE0s6_6HQjOBqReZDQ3DCYxd_dN6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری آمریکایی به یک اسرائیلی: دیگر نمی‌شود از شما دفاع کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/679745" target="_blank">📅 19:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679742">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327f3411fe.mp4?token=ZMhukPSLnYvHrCTmEZuZwXbMdgMqowLGglGM5JDDPDHbpeQaapM9N4Q1C1RUd4NeftzrpTR0hHE1vVTWKSzkLMLWFK0bWeOoG3hcddvZP1vsn_zg5D1TCZbGRJqIZPvFosJ6bRnjwYlPhoiA2wmrkgBQ4r3gMN27AbdA3SpW2iCmeZOydJaMLMguS_LIL-Bsf_LLds7hNUZZKLjQ58aD7SCKKTyzlv9ammVh_JoHrvBwew9bdkuVtLv1wXJb0OMq929fdbwJ7M_tVC1FL3SOQ5MTvgO8rqYj6jwnWlU0_11Lzi0zZnhVe7tKV6uebCXzwAzuMmO1W1i1RqZojrhJQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327f3411fe.mp4?token=ZMhukPSLnYvHrCTmEZuZwXbMdgMqowLGglGM5JDDPDHbpeQaapM9N4Q1C1RUd4NeftzrpTR0hHE1vVTWKSzkLMLWFK0bWeOoG3hcddvZP1vsn_zg5D1TCZbGRJqIZPvFosJ6bRnjwYlPhoiA2wmrkgBQ4r3gMN27AbdA3SpW2iCmeZOydJaMLMguS_LIL-Bsf_LLds7hNUZZKLjQ58aD7SCKKTyzlv9ammVh_JoHrvBwew9bdkuVtLv1wXJb0OMq929fdbwJ7M_tVC1FL3SOQ5MTvgO8rqYj6jwnWlU0_11Lzi0zZnhVe7tKV6uebCXzwAzuMmO1W1i1RqZojrhJQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: بیشترین دغدغه من مشکلات جوانان است / ما نسبت به سرمایه‌های جوانان قصور کردیم
🔹
کارها را به صورت چریکی انجام می‌دهیم، هزینه‌های جنگ از هزینه‌های یک ساله دولت بیشتر بوده است. همدلی سران قوا و رهبر عزیزمان موجب تاب‌آوری کشور شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/679742" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679737">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ترامپ می‌خواهد به تقابل با ایران پایان دهد
‏
🔹
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد دونالد ترامپ قصد دارد بدون دستیابی به توافق هسته‌ای، به تقابل با ایران پایان دهد و این اقدام را به‌عنوان «پیروزی» اعلام کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/679737" target="_blank">📅 18:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679736">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceacac0b90.mp4?token=Vd0fTl0PT3OGIR6B5b7GYGu-rmevxdemfCHuufZfc6uoEG_m3Tvy1RRm3ZRaZgJURCOGChA--KTRkeCODHNMxxqeVSit6ZpYQUiZUNtQLEH_eqtGJn6nyz7i8r56fp-hv7zqlggCA-5cnZ6Bd5nB550LR1yZ7OtvYPFTdkMLsUyyX6bLda2pTgnwl-T-_5xgXDMHugj-izvy9wqOIrev0VHcaFIq6wmAqSSbxUXV880JeOaPjW_aZLrfcDHhd_5S2AqJjPGP7wurJoI0R9IVVHSu6wfH-reAYz4zDZjOVNC3ia_wXWvhpfwFHhtSOSuMYLD-6Pa4f2bLql37ee5jwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceacac0b90.mp4?token=Vd0fTl0PT3OGIR6B5b7GYGu-rmevxdemfCHuufZfc6uoEG_m3Tvy1RRm3ZRaZgJURCOGChA--KTRkeCODHNMxxqeVSit6ZpYQUiZUNtQLEH_eqtGJn6nyz7i8r56fp-hv7zqlggCA-5cnZ6Bd5nB550LR1yZ7OtvYPFTdkMLsUyyX6bLda2pTgnwl-T-_5xgXDMHugj-izvy9wqOIrev0VHcaFIq6wmAqSSbxUXV880JeOaPjW_aZLrfcDHhd_5S2AqJjPGP7wurJoI0R9IVVHSu6wfH-reAYz4zDZjOVNC3ia_wXWvhpfwFHhtSOSuMYLD-6Pa4f2bLql37ee5jwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیف رهبر شهید انقلاب از تصویری که از شهید حججی در اسارت داعش منتشر شد
🔹
شهید حججی مثل شیر نر دارد جلو میرود و اعتنایی به کسی ندارد!
🔹
انتشار به مناسبت سالروز شهادت شهید محسن حججی و روز مدافعان حرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/679736" target="_blank">📅 18:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679732">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYFo65fwESPb77rf3MlLYF4xUjjbGE_cJe9V2SXHfD9_BYZMMoZfVc1iUYEAk271CXDiJ78x4H15I9jur_Z8cBHWxNDX6LwkygrJYNyCfaVQ6WcJaqkcXqGq22oKnRuOZPHjsZ0buEv4ftvMeW_tAPnFVfckZ-YiJUDWMAeZr2Ne3Ka45NJJjCsZ_47Pk_8MTam0sxkT9AuAaco7xskYUnrMR7twrkGZkFyq0v5SbYHutHR2dmT59alS-PwjSEq1GwrKZa4lw_lpjlAeCG-b22ITz6ixXKxsEMW3My5HfHnMOerKeb_Z5R78hdTnYFfAZbnkb5ArokKIcNeQdetQZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سلاح‌های خطرناک ترکیه/ آنکارا با این چند اقدام مرموز می، خواهد قدرت اول منطقه شود
🔹
ائتلاف مکه می‌تواند در بلندمدت، تحولاتی عمیق در روابط ترکیه با دنیا ایجاد کند. ترکیه از طریق ائتلاف با یک قدرت هسته‌ای مانند پاکستان و یک دولت ثروتمند مانند عربستان می‌تواند قدرت خود را بیشتر کرده و همزمان، قدرت نفوذ خود در شرق را بالا ببرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3236597</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/679732" target="_blank">📅 18:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679729">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سخنگوی فراجا: در پروندۀ قتل رجب‌زاده تاکنون ۵ نفر دستگیر شده‌اند  سخنگوی فراجا:
🔹
در پروندهٔ حمیدرضا رجب‌زاده تاکنون ۴ مرد و یک زن دستگیر شده‌اند که یکی از آن‌ها عنصر اصلی دخیل در قتل بوده است.
🔹
بررسی‌ها نشان می‌دهد بیشتر ادعاهای قبلی کانال ضدانقلاب جدیدالتاسیس…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/679729" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679727">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff5a9b291.mp4?token=eK_4i7rsZjuL31OGayHiFkLRDJNdaZSzwAHdYBYb8E59mk9Fo-dqBsA_uM3RTR_TkZTI-doe_-_YoJGnlPXgxSnPPuFw9wNA3aj0XYNX3UCcqJPjOfUIVJw7xIqWmTiWXc6UwOLy7nMPomV0c8om0Ra4nBw2AfLqvgQLxDhMSftFoT16hRNC_ErxmZubRHvNaOmCeV9AdgHwWvRoc3hY7IH7MSqkvmSF9KDtzF18CBnOLl__jwAiOdej1BLXuFZ-uz1VhC91ZjeyGJxGhoN5su6lrwuhOURr6sUeVicPaxcJ46sJWVX3iIeMGW3KrFv0tM5TQjUQKwUVhQuXOSuGMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff5a9b291.mp4?token=eK_4i7rsZjuL31OGayHiFkLRDJNdaZSzwAHdYBYb8E59mk9Fo-dqBsA_uM3RTR_TkZTI-doe_-_YoJGnlPXgxSnPPuFw9wNA3aj0XYNX3UCcqJPjOfUIVJw7xIqWmTiWXc6UwOLy7nMPomV0c8om0Ra4nBw2AfLqvgQLxDhMSftFoT16hRNC_ErxmZubRHvNaOmCeV9AdgHwWvRoc3hY7IH7MSqkvmSF9KDtzF18CBnOLl__jwAiOdej1BLXuFZ-uz1VhC91ZjeyGJxGhoN5su6lrwuhOURr6sUeVicPaxcJ46sJWVX3iIeMGW3KrFv0tM5TQjUQKwUVhQuXOSuGMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از لوگوموشن کنسرت‌ نمایش «سیاوش»
🔹
«سیاوش»؛ حماسه‌ای ماندگار از شاهنامه فردوسی روی صحنه می‌آید
🔹
کنسرت‌ نمایش «سیاوش»، سومین اثر حماسی و یکی از تأثیرگذارترین داستان‌های شاهنامه فردوسی به کارگردانی حسین پارسایی و تهیه‌کنندگی سید محمود شبیری و جلیل کیا است که با نگاهی هنرمندانه برای مخاطبان امروز بازآفرینی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/679727" target="_blank">📅 18:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679725">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuxVJVGhTF7dnxFGifQ_Gn3f39FRQYvssVOAfCuXeaS7DgVJHSHH3FP2fHQRdLMzaCwseypCDXI0X8PWtSiCumynSlNLpFmEL7_0SIxuKrRA3cWIp-ripOpi6jGWjX_-fnd55HJ2zLdbDr_AzvQP_F73CBht2BeYf5S35_qGGcIc50Y_4lmwtK2C6GowPvhLkS8ivamgo6SLYJ9obvpSWuvlxyxetE_B6A1zadV1aDjjiPSG4Het8A-AeWDUPr082F45lST0naoo0sQ-khsLhw3SrQM_nKFmqGHZN6Br4pV3igqBc5XxTLJFyktaiqMwUN1cFe28FoUugZUbs_hY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پردرآمدترین باشگاه‌های فوتبال جهان
🔸
رئال مادرید با درآمد ۱.۱۶ میلیارد یورو در صدر فهرست پردرآمدترین باشگاه‌های جهان قرار گرفته و تنها باشگاهی است که مرز یک میلیارد یورو درآمد را عبور داده است.
🔸
پس از رئال مادرید، بارسلونا با ۹۷۵ میلیون یورو و بایرن مونیخ با ۸۶۱ میلیون یورو در رتبه‌های دوم و سوم جای دارند.
🔸
حضور ۹ باشگاه از لیگ برتر انگلیس در میان ۲۰ باشگاه پردرآمد، نشان‌دهنده قدرت مالی بالای فوتبال انگلیس در مقایسه با سایر لیگ‌های اروپایی است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679725" target="_blank">📅 18:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULJfgHzFCotcLcIXRafb7d3p-l-jkRd-vfTzkqlQ49zoFaVxuc1J5bNl6NFspMInFGaPP1PcnJIaLAgmY3nSoBYKz0d_lGdUNwcU6lNneISxAsRhfuNB80mOiMph0blnfWqZEcm1UpzF8fzQr3ZrDjEALUxq2Oh-rRO2w87pCZ_01EkCX4_af70ERrbaGNKDh21cU3vQtxUTlgi6afFvFxFlavh_Y5kJua2j7aCdhzJXJCGULQHHd7laezPAiR3PJcSUv6VQIUpyDngQWnA-h1HavCCsr-VS6M2MGPA21lrX306km4y1Vddg_TdudlX0k_-QycBCD7_Obfp2N9NKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عددی که همه را غافلگیر کرد/ راز سود ۱ میلیارد و ۴۰۰ میلیونی هر کاربر اکوتراست در سال ۱۴۰۴ چیست؟
🔹
به تازگی مشخص شده که گروه مشاورین اکوتراست موفق شده در ۱۴۰۴ سود میانگین ۱ میلیارد و ۴۰۰ میلیونی به کاربرانش برساند! عددی هنگفت در بازار تورمی ایران که کل جامعه به واسطه اتفاقات آن، به دنبال حفظ ارزش سرمایه خود هستند!
🔹
حالا اکوتراست برای ۱۴۰۵ طرح ویژه‌ای گذاشته و به کاربران تازه‌وارد ۵ روز خدمات رایگان‌مشاوره سرمایه‌گذاری می‌دهد!
برای استفاده از نسخه ۵ روزه رایگان اکوتراست همین حالا کلیک کن
👇
👇
لینک
لینک
لینک</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/679718" target="_blank">📅 18:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
۶ سوخت‌رسان آمریکایی آسیب‌دیده از جنگ علیه ایران برای تعمیر به آمریکا منتقل شدند
🔹
دست‌کم ۶ فروند KC-135 در جریان عملیات علیه ایران آسیب دیده‌اند؛ ۵ فروند در حمله به پایگاه شاهزاده سلطان عربستان و یک فروند در برخورد هوایی بر فراز عراق.
🔹
سوخت‌رسان آسیب‌دیده برای تعمیرات اساسی به پایگاه تینکر اوکلاهاما منتقل شده‌اند و دست‌کم ۲ فروند دیگر نیز در حال انتقال به آمریکا هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/679717" target="_blank">📅 17:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/679716" target="_blank">📅 17:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679713">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تجرد قطعی در ایران؛ از وضعیت فردی تا سبک زندگی
🔹
به گفته یک جامعه‌شناس تجرد قطعی در حال تبدیل شدن به نوعی سبک زندگی است و بخشی از جامعه تمایل بیشتری به مجرد ماندن دارد؛ آمارهای رسمی از بیش از ۱۸ میلیون مجرد قطعی بالای ۴۵ سال و بیش از ۲۴ میلیون نفر مجرد…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/679713" target="_blank">📅 17:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679711">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/679711" target="_blank">📅 17:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679709">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
حذف بنزین خودروهای فرسوده؛ خودروهای تولیدی سال ۱۳۸۵ به قبل دیگر سهمیه سوخت ارزان دریافت نمی‌کنند
🔹
خودروهایی که به سن فرسودگی برسند، سهمیه سوختشان قطع، ترددشان در کلان‌شهرها ممنوع و نقل‌وانتقال پلاکشان متوقف می‌شود؛ در مقابل، برای نوسازی مشوق‌هایی در نظر گرفته شده است.
🔹
این اصلاحیه برای سال ۱۴۰۵، شماره‌گذاری خودروهای نوشماره را به گواهی اسقاط منوط کرده و استفاده از خودروهای فرسوده در سکوهای حمل بار و مسافر نیز ممنوع خواهد بود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/679709" target="_blank">📅 17:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679706">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ_gsbQNBAAKzruZOY7dSqHvN51XNLqOxJsaLwCIq-fJTv_CI3j5jtGU2yT_8LkgxTDkGXsbof_AFg4fr4AoXdmN2qlJDAwkl1cZuW2qZ3Xh5qMf5O0dGoEjU0QupZ9XCKJoqHb7YYxTy1FOF2qyoi4uU0SpkJC1K0dJXX1snZkHnihTy7sbJaBl-tIrPj7gBblDfttf8970l9k0q2z5Dbfa891RWz3wO7HyuMc5RFoTRZLG1P-jyVRICqBbY_3eBDiHsIyMF9aSVK3nIhZMlAATGGz0De09O9VJ7cuu0Sg5J6nytSc-q2LQ751XPCZo95Y6iXnhZhM2jyLXgs0aew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از نیمه دوم سال، طلایی شوید
🔵
اگر قصد سرمایه‌گذاری در طلا را دارید، بهتر است پیش از آغاز نیمه دوم سال و قبل از انعکاس عوامل اثرگذار در قیمت‌ها اقدام کنید.
🟢
بازدهی مثبت طلا در بیشتر نیمه‌های دوم سال
🟢
افزایش تقاضای ارز و اثر آن بر قیمت طلای داخلی
🟢
سرمایه‌گذاری در صندوق طلا بدون اجرت ساخت و ریسک نگهداری فیزیکی
🟢
پشتوانه فیزیکی شمش و سکه در انبارهای بورس کالا
🟢
ترکیب بهینه گواهی سپرده شمش و سکه در رز ترنج
🟢
شروع سرمایه‌گذاری در رز ترنج از ۱۰۰ هزار تومان
🟢
قابل معامله در تمام کارگزاری‌ها با نماد «رز ترنج»
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/679706" target="_blank">📅 17:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679703">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2ca95668.mp4?token=h4EkLXTPZnnV8iQCXHUrc5uVriblsYP2XgJuqJ1Zf0s_PVwz7ab8XkfG7L18s_kUiUWiud-5nZ2HNYFYrJvljAUDuv9iwzD9hvITJRzESKXrFWhFoZIfsi4gq8TZrfP6oqMuoC3SiNdDwlh20rkp5vJRezn5q6o4MdUJzzINyqFcAyq4-a67eaqaepnJQ3RRDw6DVEVXE5iDchxfwPla6Sg_Ymxkzl9Fg-ChRf54WFa9V6YkH7gMzQhMHw48eYSSQKBYulwQP9qmwtDggpwY9v5yXwZCxlCsmuRSa62ZhKKnldkGJspUvi4LEtgraVvph5l41q9JFhNVhXXIeZuR6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2ca95668.mp4?token=h4EkLXTPZnnV8iQCXHUrc5uVriblsYP2XgJuqJ1Zf0s_PVwz7ab8XkfG7L18s_kUiUWiud-5nZ2HNYFYrJvljAUDuv9iwzD9hvITJRzESKXrFWhFoZIfsi4gq8TZrfP6oqMuoC3SiNdDwlh20rkp5vJRezn5q6o4MdUJzzINyqFcAyq4-a67eaqaepnJQ3RRDw6DVEVXE5iDchxfwPla6Sg_Ymxkzl9Fg-ChRf54WFa9V6YkH7gMzQhMHw48eYSSQKBYulwQP9qmwtDggpwY9v5yXwZCxlCsmuRSa62ZhKKnldkGJspUvi4LEtgraVvph5l41q9JFhNVhXXIeZuR6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکنیک سنتی که توسط چوپانان جوان قبیله بنا اتیوپی انجام می‌شود
🔹
چوپانان جوان برای مراقبت از دام‌ها و دوری از مارها و شکارچیان روی چوب‌های بلند راه می‌روند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/679703" target="_blank">📅 16:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
بیانیه شدیداللحن سازمان حشد شعبی عراق و حمایت از فالح الفیاض
🔹
سازمان حشد شعبی عراق اتهامات مطرح‌شده علیه رئیس این سازمان را افترا خواند و با تأکید بر اینکه دستورات هوشیاری و آماده‌باش پیش از حمله صادر شده بود، از پیگیری قانونی علیه شایعه‌سازان خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/679702" target="_blank">📅 16:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679701">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa3kddMkGv45JHanzQSDgVWWTNGsK0Ga1hgGOvp482hFICeOOic5_qgd304hGcEE4sn71WKF24be6WFX6iZDcALxrOgInlcynCTKPfZt7sT6wSmJHOFv2HZwS-fP_RI1FMmDmb9nEfMM7SonS0atajCfikPxGsFCdYjnYItocvkWjaO-k0lXxQqpTiz2scs0Nay8AEXHzkWwn1DiSXoFOR8imzuDFKdsd703KiqK-H_fo0rz9Na6c24FLAD1Id7uyD-wJ-92IQ1NrR0NNHdAFpRg3MieaK4NQd5poua5nf_AozIF-pIJ7XU_KjkLlU03N8NGksy-rK9b3za0o7CegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
قیمت طلا منتظر جمع‌شدن پول ما نمی‌مونه.
اگه خرید طلا رو گذاشتی برای وقتی که پولت کامل جمع بشه، باید بدونی که با ازکی‌وام امکان دریافت اعتبار خرید قسطی طلا تا سقف ۲۰۰ میلیون تومان رو داری و می‌تونی آنلاین طلا بخری.
✅
فوری
✅
بدون نیاز به چک و ضامن
✅
با اقساط منعطف ۶ تا ۲۴ ماهه
شاید این همون فرصتی باشه که شروع خرید طلا رو دیگه به آینده موکول نکنی
👇
https://azvm.co/ptw0</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/679701" target="_blank">📅 16:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679700">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b463873e3.mp4?token=lhGwyay97ab50Qz9HPSYeMK6bSHjjZ79Cv01J-6ceigPxgVspdNTOu-HGAQGQXe8xU04YWym40d2kRzOQ2gHfPEPn3RnUjRFy6hJ59WfvQhrT7WN-OZJAQaShCn0JDi7kzvjfrVLrsULqwVSGbEXLJR6sHrHc2Y2FX7DOZbD4qoowGq-h4lm5iu8iNpSJplMfx-gy3BCqL_oQtDF9QdNZeaK3c34zHYZmXOhG5zHIuAZuOdItNZjn_iB4-V7oxhEbdRcXO1WCtJuta-Lsp9qbVX0kvtVDCY324nB8kDFU9nNuMeePpyhxzRIe5jFZjnHEaAmfLNf2YfqChPGK4BNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b463873e3.mp4?token=lhGwyay97ab50Qz9HPSYeMK6bSHjjZ79Cv01J-6ceigPxgVspdNTOu-HGAQGQXe8xU04YWym40d2kRzOQ2gHfPEPn3RnUjRFy6hJ59WfvQhrT7WN-OZJAQaShCn0JDi7kzvjfrVLrsULqwVSGbEXLJR6sHrHc2Y2FX7DOZbD4qoowGq-h4lm5iu8iNpSJplMfx-gy3BCqL_oQtDF9QdNZeaK3c34zHYZmXOhG5zHIuAZuOdItNZjn_iB4-V7oxhEbdRcXO1WCtJuta-Lsp9qbVX0kvtVDCY324nB8kDFU9nNuMeePpyhxzRIe5jFZjnHEaAmfLNf2YfqChPGK4BNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های خارجی درباره جنگ ایران و آمریکا چه می‌گویند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/679700" target="_blank">📅 16:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679698">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c1573314.mp4?token=BHz4oh2YQm5J-qbq33CkMmvTEroogblRbybZRx8NYQVkeQBuluydBVwGXVP2jhs8O1ybwrn3WqnM8Qd3PUyeg9_bsXGghewGNtbKvsX9XBkfknBeTkKHYu97ltF1kfxwo6-6WVHH9h6upWnrR12U-xWl-e69aHvHFkubRtecKPYC97cEZCZSK8IA_6mFef-30sdPVLkUc1HP0O8M2NFwn6n7gOH1c-ghicqta9uDOnNj9X4P29u6hk266SpxSOpp9Kj5IZwCbsvWuqDDUgvRCmJb1SFVCxvUUP-zw7c3FsLJ1Jg2U_YIw1BwIsKfRoj7MjohjF8F2XLRbXBrkyMLqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c1573314.mp4?token=BHz4oh2YQm5J-qbq33CkMmvTEroogblRbybZRx8NYQVkeQBuluydBVwGXVP2jhs8O1ybwrn3WqnM8Qd3PUyeg9_bsXGghewGNtbKvsX9XBkfknBeTkKHYu97ltF1kfxwo6-6WVHH9h6upWnrR12U-xWl-e69aHvHFkubRtecKPYC97cEZCZSK8IA_6mFef-30sdPVLkUc1HP0O8M2NFwn6n7gOH1c-ghicqta9uDOnNj9X4P29u6hk266SpxSOpp9Kj5IZwCbsvWuqDDUgvRCmJb1SFVCxvUUP-zw7c3FsLJ1Jg2U_YIw1BwIsKfRoj7MjohjF8F2XLRbXBrkyMLqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور بعضی از خرید‌های ساده به‌جای این که پولدار نشون‌مون بده، تبدیل به یک سقوط مالی میشه؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/679698" target="_blank">📅 16:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679697">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بورس کالای ایران: ساعت پایان معاملات بازارهای مالی بورس کالا به ۱۸ افزایش یافت
.
🔹
عضو هیات رئیسه مجلس از وصول ۱۰ سوال نمایندگان از وزرای آموزش‌وپرورش و راه‌وشهرسازی خبر داد.
🔹
پاکستان: هدف پیمان دفاعی جدید، تقویت صلح منطقه‌ای است.
🔹
انتشار اطلاعیه ثبت‌نام آزمون دفتریاری ۱۴۰۵ در سایت سنجش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/679697" target="_blank">📅 15:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
چرا سقف ۲۵درصدی افزایش اجاره رعایت نمی‌شود؟/ مالک می‌گوید تورم ۶۰درصد است، چرا اجاره ۲۵درصد افزایش پیدا کند
علیرضا نوین، عضو کمیسیون عمران مجلس:
🔹
افزایش سقف ۲۵ درصدی اجاره‌بها مشخص است که رعایت نشده و در عمل مالکان آن را اجرا نمی‌کند.
🔹
باید با متخلفان برخورد جدی شود. اگر ۱۰ متخلف را شناسایی کنیم و محل فعالیت آنها را ببندیم و حتی روی آن پلاکارد بزنیم که این واحد به دلیل گران‌فروشی یا اجرا نکردن مصوبه دولت پلمب شده است، دیگران نیز متوجه می‌شوند که قانون باید اجرا شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/679695" target="_blank">📅 15:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رئیس اتاق تعاون ایران:
بخشی از سود سهام عدالت ۱۴۰۴ تا هفته دولت واریز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/679694" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY9aF2x4i1WDyzFS_7bd1KDk4bEw5TnsDEnJ-8PP9_sW_2vX8gHL1QakW7MRsduGCu279hH7ElMNETMIZzEZFmwz8_c2YpljgsSRYGVnoIs09YAbR5Y_u98paZsIkRkxSpaXS-eSaNHlD7KfKdAb4IwBSE6hlIi8hbdMUeTbyLsJi0G7ngu-B3E3eLz9K-ICwXPODMYfKRnK262_safqpcJo76zvOSoG6LE8MYPa7PQu0m7ebmF_8HncyldjGCoHUiix-tmDDSenc43xsMrG_KCLJWp9VHSKZv1Gp-AzmFF0cfRsbD5xXJmtAp97AvbpXAgBV1vAgErD79le038jEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک سوءبرداشت تکراری از ردیف تبلیغات در صورت‌های مالی فولاد مبارکه
🔹
هر ساله با انتشار صورت‌های مالی شرکت‌های بورسی در سامانه کدال جهت ارائه به مجامع عمومی، موجی از تحلیل‌ها از زبان برخی تحلیل گران بازار سرمایه و در رسانه‌های مختلف شکل می‌گیرد.
🔹
یکی از بندهایی که همواره و در سال‌های گذشته نیز مورد سوءبرداشت رسانه‌ای قرار گرفته و این ابهام درباره آن هرساله تکرار می‌شود، ردیف هزینه‌های تبلیغات است. تحلیل‌گران شتاب‌زده معمولاً کل این ارقام را به پای هزینه‌های جاری روابط عمومی و رپورتاژ رسانه و یا تبلیغات رسانه ای می‌نویسند، در حالی که ساختار تفکیکی این سرفصل‌ها ماهیت کاملاً متفاوتی دارد.
🔹
بخش عمده‌ای از آنچه در گزارش‌های مالی گروه فولاد مبارکه به عنوان هزینه تبلیغاتی ثبت می‌شود، در واقع بودجه باشگاه سپاهان است. این بودجه در قالب یک قرارداد رسمی تبلیغاتی ثبت می گردد و ماهیت آن با هزینه‌های مرسوم تبلیغات تجاری کاملاً متفاوت است.
irasin.ir/xKCh
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/679693" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679691">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
خاموشی‌ها تا دو هفته آینده به حداقل می‌رسد
رجبی‌مشهدی، معاون برق و انرژی وزارت نیرو:
🔹
خاموشی‌ها­ در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
🔹
عمده مشکلات ما برای تأمین برق در ساعت ۱۱ تا ۱۸ است که ساعت ۱۵ تا ۱۸ اوج بار را تشکیل می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/679691" target="_blank">📅 15:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679689">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: تهران برای بازگشایی تنگه هرمز ۵ شرط کلیدی تعیین کرد
وال‌استریت ژورنال:
🔹
ترامپ امیدوار بود که بازگشایی تنگه هرمز به او امکان دهد پیروزی را اعلام کند و درگیری با ایران را به پایان برساند، حتی بدون دستیابی به یک توافق هسته‌ای. اما تهران خواسته‌های خود را به شدت افزایش داده است.
🔹
ایران خواهان خروج نیروهای آمریکایی از منطقه، لغو محاصره دریایی، برداشتن تحریم‌ها، آزادسازی دارایی‌های مسدود شده و دریافت میلیاردها دلار غرامت جنگی پیش از بازگشایی کامل تنگه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/679689" target="_blank">📅 15:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679687">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCeUeL4aYEwsIhEkDTAkZVJW_t2z052LtDeG4Y4dcNFEpKwenoLFwEcTyyjTByRo63XJhT61qIsGHcqda_FqporaDVCxHP_8r1mqJUEAPyDKMYZ9cwyXzZi0IvfsoIa5A_l8P-H6yWaZ94X3cHdA4W9mjGLOAbyI0X5kxxTM4jAoYaez-sVrsOvq_kZm56J5HMrJ1HZP6pAb6DiV1BCf_4UGanjdVdVGfd59z6zUC1bnd0BUVe8fI3T17Xhw5AMoqYqLE3uM9YWmuRD-bwxXzA7dc4-btiunPhuhTxCT0y_vGgJJLO2zBT4Ss808mfi9DImn5g-QDJv1401qSTvBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
‏
استوری بهنوش بختیاری: آمریکا در هیچ مقطعی از زمان، دوست هیچ کشور صاحب تمدنی مثل ایران نبوده، نیست و نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/679687" target="_blank">📅 15:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679685">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1NELEV8tUCLLHRRuZb7UpjA_qDqGSLGMKmZN-ZuQTdG0OyohZsiQgrVqFd2s8Ha2IjaR6_gVfBbt7CFCwHpc-zB6_VpSL6jWXTH6r-CVtQ728fZDeIFx9_nFJu6hPIBx5nFHt-kzGWOJJIqeRt28dA3BBZFxU_TOzuGrgo3Fv_oFjwIRDzEEKs125jwz0QPvvAGmaGKB9QVA3Uq2geGrpiwZwEb5pA7V2uN3-jaqRKStB7--5PdsgU5a7Mf_hFXNPuJYaTWXRlMRDO4Pad_kCMCvjjo-soIyX6kmpHRC3BTNK6nsGSVoA-fOkj4whdqUuJq73urPGxwgjSXyuZpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۲
🔹
سپرده‌های بانک کشاورزی طی سه سال گذشته ۳ برابر شد
🔻
حجم منابع بانک کشاورزی با افزایش ۵.۵ برابری طی ۵ سال اخیر، از ۱۷۹ همت در تیرماه سال ۱۴۰۰ به ۹۸۳ همت در تیرماه ۱۴۰۵ رسید که ظرفیت این بانک را برای ایفای نقش مؤثرتر در حمایت از امنیت غذایی کشور با تأمین مالی بخش‌های مولد، به‌ویژه کشاورزی و صنایع غذایی تقویت کرده است.
🔻
شتاب رشد منابع این بانک در سه سال اخیر، به طور محسوسی افزایش یافته و از ۳۰۲ همت در تیر ۱۴۰۲ به ۹۸۳ همت در تیر ۱۴۰۵ رسیده که بیانگر افزایش ۶۸۱ همتی و رشد بیش از سه برابری سپرده‌های بانک در این بازه زمانی است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/679685" target="_blank">📅 14:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bd56a25b.mp4?token=uUZJAR__eB3L5kh8I-QHbpxomRfAxF0rkmxh-kUhCO0AHecaklcswAgjbM9fM_uzs8LSM8uhvgZEuhy4rvB3IZi4x_ZKtgUid4Me8uWP6OQ6Mtj7YvWtxCpV5nJuPya6Upc-PyN2qGZqu-8-H6Yghu-ReViRBKnfsA-Uz5dqf612ihihVNMB9EmG37XBV9NL0ybuc-jBadEYzycFejS4VIMWv-ONUZnp4XfC6BLsst0_DefnTB6jFFyzsFdfReGIZkPgNeFBcT89ElgTUQuxYDhlXu_rUoU1y2gOkwgt1inc9h5akqhCcRQ7RyOvotTOYGTnrT2QX7XlkNFzYBnNz1wWLiaAPyUCwNbbdvfPdObvz6O-9JVzTYwNFAjkqbm4ggmAGu7a1IZK-3fjDd4_6OqOcw5g73UQn96SNS-ETT0Lzr1Zs4_VWtMqnH4Z-Y0bzxV8bwYxEGm_5Eb4OL5RB_yXI2uUs1CN2CzC8Bm-6cvFwg2jfyRsXv_PwPXL_AOwGCVqIQ-jRTFSUjElCH7EwUqYM99UY-nuBb_GwGBoUagd_2Q0axfrnUPyvrU9eBnIFhwn6Qu1_Ct8XSi1sL87ELU_Mm51yVVQwtLnQCmLryniUIq8ecPtb-b_LZVktJ-M5M5VymLSU2ol9eTNMrSzS1zNfo2KVpo8hEm0tJ4cs1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bd56a25b.mp4?token=uUZJAR__eB3L5kh8I-QHbpxomRfAxF0rkmxh-kUhCO0AHecaklcswAgjbM9fM_uzs8LSM8uhvgZEuhy4rvB3IZi4x_ZKtgUid4Me8uWP6OQ6Mtj7YvWtxCpV5nJuPya6Upc-PyN2qGZqu-8-H6Yghu-ReViRBKnfsA-Uz5dqf612ihihVNMB9EmG37XBV9NL0ybuc-jBadEYzycFejS4VIMWv-ONUZnp4XfC6BLsst0_DefnTB6jFFyzsFdfReGIZkPgNeFBcT89ElgTUQuxYDhlXu_rUoU1y2gOkwgt1inc9h5akqhCcRQ7RyOvotTOYGTnrT2QX7XlkNFzYBnNz1wWLiaAPyUCwNbbdvfPdObvz6O-9JVzTYwNFAjkqbm4ggmAGu7a1IZK-3fjDd4_6OqOcw5g73UQn96SNS-ETT0Lzr1Zs4_VWtMqnH4Z-Y0bzxV8bwYxEGm_5Eb4OL5RB_yXI2uUs1CN2CzC8Bm-6cvFwg2jfyRsXv_PwPXL_AOwGCVqIQ-jRTFSUjElCH7EwUqYM99UY-nuBb_GwGBoUagd_2Q0axfrnUPyvrU9eBnIFhwn6Qu1_Ct8XSi1sL87ELU_Mm51yVVQwtLnQCmLryniUIq8ecPtb-b_LZVktJ-M5M5VymLSU2ol9eTNMrSzS1zNfo2KVpo8hEm0tJ4cs1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرزند شهید لاریجانی: شهید لاریجانی درباره حوادث ۱۴۰۰ [ رد صلاحیت] گفتند: «آبروی هر کسی متاعی است که خدا به او می‌دهد و ما باید وظیفه خودمان را انجام بدهیم اگر وظیفه را درست انجام بدهیم خدا می‌داند کی و کجا آبروی ما را تدارک کند»
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/679681" target="_blank">📅 14:33 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
