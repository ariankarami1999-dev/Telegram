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
<img src="https://cdn1.telesco.pe/file/bnyZmc_s3b6Vcc9Gy59q4gU2m7Z8dQygr_aRCrq-7S8yLTWy_vnkZVfnDB1y2-foz6Wkem0iiNJycQzWClDFofVY_H-D4J5z0TzP1y7aHHYXmUnXUjPngYH9LYxmdwa2ZYdIGdKC1wm0qgHDYdMltPNFGYaBI2MEU44krdVAvET2QRqmUVpyyTIi92RV4MHYIXlkT22VQ9iSRHCRB95HesBndg_vF-vakLDOgIGEfIGPTKXw1ISI45aNd7Ka7vee7vZM7fW87tm9Ji1qFhtit5LDC6GA5IhC76Gjv2-Oqp7g9bj3hKVstAl6YB5bHxPFZpl88a4hEKS7VgSmApYuEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 03:16:00</div>
<hr>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qZYJWmN-ALnp-vfWzY91qsCx1gb9Y99_W_uV6nfKdPbtAjNczVg3AYqHIru5ZxJ4cwYG0emQu5Ss92a3uPLZawKNdvPvS2vyCdslhFJIAS2kOALCU0K200Fk9qp2wobl_EThEFox6gaIYlR__rpVW9B34qUD1K_xxNFPflayxSNeuuahNVkGyITGzZKEU79Hd7M-FobBJE3gmGikRBhy5nVYEFFhUdf0c5ELKYs-g7gbzdIxkACkjNdNRKit9omI1TCDChaiok1AFsivKNhDe3k199ut_Duh4pWHa5w--gtutFrq7JsBs-XLWBN527qN8geDC7rEoS6s7V86Yso-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aZmxV2PAbph-rV8awzg3jGwL_jYimvgYdfZSEgKwS3ZxUTIq0Dcpnib3-KG8VIz-PY7EZr3diVXaO84TI-cP288suNBabF2oHfd4yFmKuf3DilrAGMXG0BFTIeY7Aj8yAjcBy-7F-VsnQ4J3rsksS8tSwJ1swAo0UwXvOxX6A3ORsdeAmdsQHoFTbUXosPi87p5yguyzNe63mB-QSpW3Mg0Awi5dT88-B1BYEom4qh34ZL4wb3PWQb0-HgwweknZNH6BEsBaWNnc8CKR81_GvnMnkty_pJxC3YJnbZTTWOI3tneMhiBVoiKMz9mQVk9qm8GnkKkfnKWiRJBuVP3_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SeCzrfFEbOfAH4pGS5kVx7uJtrbcbgbaIWL2EOM94jbYF54of9iLyofjmKqJroiprRFIODOnL5GLOZCbn3xuj2YWVKVO1cYBWis-dzOrjLi4ibARiw-oGY2qd5hPflxlMzl0TUDKMgt_UZEONkOjz6-PmkrOm0JsMeFrK1dLHOslyO96eVqCMZ-m6pzDqojc1poeVI8n6wJFjtgwSSFGA8F7SJ4X70Ls1-Ai3mW7Ez785vzz6F3QNwdF-7hX0DLYKW4xDQ5IXhIuHM29KevTOmxKMLu4P-dFVIlbnnvY-o3MKGJYcCb15oI8XHRrj5k1Aqeux61iPJSqRrPH9cYcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bcjon3ThXZV2kZ9qmmaF_QFAY03nVF_-OA9sA4zQ3Hv75GmjvfGDqYX1tGQZ7vUfdATA-bhDgbGORsW6pdQZDh7LuOBGTw7sl-aSZ1AsB5N9e-PzWA19Z2qw81s_14o6dfxR4s-aalLW9Lj94W3jPVXAam8VFJ_J8PnO7cF84nIxTEMldLck_MzWvL_SkccpQd8QrvQ1Hv4Y5owI_9woh9QfOF15gY4lg6Hv8w50HHr15OeH9v8GPmKoGs4nO-NuSjyraT_MpZ5COQjKjXyIIqDLOCNrT8T2otuSS6ms75SUHk74DjFha7Wua3rxHlLTvV_ScGTTEpNCymIv-ftasg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LTVNarbu2w9ezwgo1UZDGRXVZHMfvnUfpQDzzfpj8SAmiTMuqcekEVkjvbg6q-5_QmJ_sNJ2cfyZLdvZaOVVeGa1ZeEbh5Xkb2HNhGTOB7Udtt29dJloXpFRZv-g5WPtG2yb4elcPgqJhm0BAmacbPlGQd_4AmYXM4TMupAetBNb_WsZXUMuhezDV09VgZrq59M70dsOZQBEgVnD2NNiQhZI_JZaEnO9w-Y0txVqWGPU0-grlc5GoJyv5izyWcUfuN4v79v2LWMj_JUXMmzUlPGhpPl45NESSP41LYMww3Df8Zh4gIlmQ_6lUOfS2Gl6I_rXTaZve9aMw4qhFYCPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AkarenA9KOK_Yi-hWqq1Un_mP83ImMH6t5790IWsY1s-NdYpbQmFXUVcycBcGPTkFlewNDQMKxTGVx_uzrByQH2KOqHzB8Bb6N8PpfOrjqIDocCXOHEIhCOAkKwc1EZW8sdolHqsz8lQGB7NYbA4YATS5gygAHGkyVRiJbHL6zjkmQRIvQwjNIFHu946NmG5QS0fssOfz8USKLHFGTV_O_0Ql5GHQzRXcf4KD63ucj3ot-bKH7oeT0JncCkjSlHB8TyWzwULBe_9XWQh2S6HZph0JKMM0U2i_eQJrnCzfUMGTxh-qvWYGn_yF3r5jNZiJijSuD0gtJvj5Gbx9GBeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PtW3LtKNFw4XIoE247FLs752LZ6tyeNyjIfNmSU1E2OnRnccKvcY3UfdHhQ5NlmMWkcP7jnHnlT8HnY4O6NmRYOpmTGtLWixZbCgEcIJXOiXR5HWsKs6qzTOtzRvdPjYHceJJF41gmM9YcrSaiJx_Q0Ha9NR0ztBuYIqk1NMwgkVJbvpHR3ASYFuLkRe7A6ys_pJISnbuJZKUtmPAHWE74OkjQrVllsQkB1RmSFrxWRIVDMlNyzEXrOPbwqEuBxkFfhFItJAz08KnbAR2EWp6oc128az6VIoOgD4_EGR0ygsUGjmE98KvEFGdFYB6DGuAYBeZcAtr1bMHomYS-255Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxuwvPqkKJdBmOn6sLlgliY43r4mOU_e6aY078ENGKfeVFbflDP1ZHzHoCurJKt6doBcM27NKjVywmcKSaJSf2HwTQtje3udsKSD9hEo46mxkXBk7XbUyYba0_J8AbCRE9fdNYpdrP43CWwLubVODlXloFM5luM9iqGHFK9NoPvU5bImK8C7OmkZZ8LHHDcLnwcrvPpSC0Bg2ew8rAEs78DhAMHYm2icK_nHqqis17jKnOZYVsB0pXXCGVgRCrNue0Zal1Ma1hSdnaZe1R_pXum5dsizPXQrEy0gYMirjOO3HUTpPaokCGDsi3fMuymzha8w_H_LeoUMQd3oxHOLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKKMdbWDMICInmRs4B3INefZPG97RPZKomvnrTjbZO0L_ksF3mWmIVWUdRLJiJvIaGD9mBMiJUUjpoXQUjguzK_QN-Glt3vOIJKf6KJ9yG2vgTXPEaRyXNXP9ktZ-A2TuDbiG68QKFcH0lMBDYIlr0yVJi--14W-qJ3SZAe1oSvEgLBuix6vKjlk0sIW9FGhP_sHRLWuQr1G5L0NGb7MnWuymxR87m8PSq9v2J17cr8rhvocGTM6b5rB-VF9gVrjY5wC1RDSAb2nf0CFsMGsIOIudf1zYviZrM1ZJ-RJEbFn15pBz7_6SuRHkewc7TGJy2RdA_YdXjwe4RL3_i61sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntcGWi3KdogXHUri3FtS2ey_AD6dzQ6AGHZJEqWX7-37LnVWfvvS3bPr570Z-WF3bbrsyv-F0OmR2Sh8FA9fUuKB9JxItb5gWCxjM5msfSgU015Vm6sa0ETz4uOqdGqm7YBAxWCjGGal2s4V1BrY9LcKY78VUhz8Ct3iSEGenR95BERut-uVzbqS_mto3eWaO6wqk6kdeaY3gzWNXPDuJY7y1LREVO8YLV44Mt05wGRza4TBk425Da7lCaspl9Nl1z_5qzNcI1Jil-dOBKuMjl1RhM7VWkmWEuV9_UljOgSROJaHc_Se6nn4AejihMdpU9zDV6CgMH0bzyxJ8YfTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qipdO0XbBtrT56B7c7qa7IdFMvxdaizLy3REuKqprV16xb2J1Met6RyIt-M0lf-nD5iU3oofyAETJKjrnX7U3BcwzzxUdbAbYA64NmQPAmjtRQRo59UXbKUqZoXXR-tk8ssE7_d1_5Bc5bEoezv6yrvIKCgBRmSvph28j0TmeKUlbw1bn8D969anFGBadpPNSBSaeVu9XFU84_cVbQ0OZk28kafFIkuQNCdwIFxAKH1q70IF11qao9hbOO2ROf-on4kyFKZPVhfY_saf5jsdMpSBX8id2A1QtZ6sXWf9NjaoOzLx9YKtSoyhzmB8LLOqWaUEza5212jfbNPEKmXsmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KrWeoshFxYaa_XxY1fkP-vfmIJDm-vgz0nrzKtuX0WlUPqY5uN8PqIPnS968iZJMkziorYj-rWEZ8hoC3-Eug56Z7uHbvLBqk9u8UdnzRbzW8jV1HEB2kPV6M9nVhrxey1OzrhvHVtJ2VvmhDnl7zmJXcaYHNIMoho6a-y8b-MtpEVnnihd34lQG-FDL_ZH8YQexA4uHj95H436sq4X7T2Mr_nHmpTX8oq1N_cmfSZCd3DKRbnDZRjmAMNt5z-Zjn5CfE39GRs6fu9w7yAJA_feUf8Wn-QsQZrbr_0IyoMmTOoR2XQjGzGJpD2DhjGgY9Dt1miTfr-3pJvKQu7NiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TJI91L_Y750-47FS_qHaUWeiQ0Pf3n3jMDbkOyfX1UCtaOpl195vJ0MOjgC5NBYiCA3x2-sLSeDH86MPc8UDmeyCb53ANagB6zE--Y3N8N4iCkWWbNh9Yb3ed2OtR-pxWv4AmZCrFuDyKHUIs2bNG0G3ifVLKjvcf99AE-ujROjt8AgVSKEAo98nRsejS0-OSR9FCnP7fse2GF341589jwnZcaNzh6x2wexVvXaA1C3GsnFrq9OJFau6ide8t4BpF6H6BVlnB_lws7eZGwzH4UAKdVBvO4JM2PT_TSYOO3cOi_ZOin28PRDSq8VcWOqBI4iMMSRxQHJnX-FzkAkvtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbiuzepz6n3I4F5TZACWcLuehSxvg28m7IA8ZxsITFCI6vqiDpGKmLu3pJV81oyJRquWEFoRYTFA3Z1LhFFNuoVxFISg76M97Q-gI5WG-JLL88d0dju7s56gCPyeGsPhFwNRdFrFd_M98lVqKnf11ugNQMFJHNlKKQiNRM1aNxVH2ozRCz_caYI95-vAVGB7uUa30YHUNg4irpTmvYL6yOYtHAKKyulEEAJsSAPx87Kb3RE6d8AlUQ5H3_NNUePWtE_vhu8RWLrJKZ-sKKOkxA7mbgScrCizchze8DkilIk3mvBKd4CYgowX_LGwLn9BbAbTStvKoT-meF2UC4ZUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uuiGZYSdBqmDm9e0kmFAuSEhpwEo77qU-P9uGT9PSLsP7rFqFFZYmWTgDYoTMcr1ZLuc3YPvUxc1RjBjFAmxnMW1knhlU0TC0XcCY8GZOZilLJk_3AdPZ5rwFGZdwSh54X1ZKDuxE7F9HvHbExv7HZaDWJQXTVJPXyEtoJwK9eO9aIO5ZW84DvPcS2RA7hY-FL_-1WVhRhbxfcTIDptwlW-8SS-xApnPw85rLc19cU60x2y4qfjf8A4ZSKwCSbeso5oVrUsKyFtHBPOCTZSB6B3392zjigaFny-Og_Ky2r2DqhPwQne9-CaD7vRGtkYtw-DiQkg2N5aBonMNK7O85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Yx3ra6nOPYo0ux6ppqoAbVjzLNynSCJaimQqFMRE13CCwaWEbyMqBPZ6sd7O_j6uLpVfcxrZ8CTfEnPiXsNeXZ6Rll8mJWE48TaGuUUJyMpvwmuLqDn9OV8_PfHkcWFFZaKB7sbEo99UeUv63dRzbVa26vWd6UFab9YVQCOAl3QWapKBbsq-VH9jpmOIVtCflKudlxAW63DD0-J8old7DUWhnGWog0-VXjEFAGvRFGPcop-bub8i-yk4tGFbdgNPXinea8aaiEsottDyvEnENy5GmtwbwQULtllCDqAA4C_djaldH8KADP-sYMMSTKeWZ5J4PNPfcAyTooVyPhuILQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Yx3ra6nOPYo0ux6ppqoAbVjzLNynSCJaimQqFMRE13CCwaWEbyMqBPZ6sd7O_j6uLpVfcxrZ8CTfEnPiXsNeXZ6Rll8mJWE48TaGuUUJyMpvwmuLqDn9OV8_PfHkcWFFZaKB7sbEo99UeUv63dRzbVa26vWd6UFab9YVQCOAl3QWapKBbsq-VH9jpmOIVtCflKudlxAW63DD0-J8old7DUWhnGWog0-VXjEFAGvRFGPcop-bub8i-yk4tGFbdgNPXinea8aaiEsottDyvEnENy5GmtwbwQULtllCDqAA4C_djaldH8KADP-sYMMSTKeWZ5J4PNPfcAyTooVyPhuILQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X_DrxA1xqDsvALrVv3iTvXuPc8uegn3fqAlyP5MjODml1tmJZharlrdkMF-62kUA4a7Rtxdb4dP0JQVVGoB6bpvs-8Ot0vxZU7YNxh4nHxux2P_ExzCAYykLvVDrSYHC2yal0A7lRMme61EFxguW-_HPZlUYDolofOwa-nMi-ufceYhZVOPxnmOCMD2NvaK-4UYEeApBvH0l23vtIgCqUPk5TLdCj63E__Aan_ygx6bF8HLhoIZoitsLYe4O8Zdmr4UTrLXpH8lmZ1puLBXOkNX-n-hbRFUyV-vbOvAy1NNsmsLMUtSU-VnFqiGTNnP7ha37vHwdns3Gg3Ronc-lFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCkeW2KqbMMXy26ybi07xAe-mxDos8zzbCbDj86NAkhDWJIUKB2hMi-Jhxmj07xQvR1wvd1lV5GT_mJwZo7xCRhIkdvsm0b_LHfFvRPhZfTthf1DZz2rWoJgSKPsRRE8z1jMV3nk9UYblB_FlrrU1yWVuT7z45Oxg85BDauWllrl7mJSdG9xBma20FQ6YdrGTi0DnpKNt--hBZNko5mpeFVjVALn02txtRWuQWOh2P8AF_C_xOj0GkNzVOnQo539T2oWucr3gWva3yYEk9mONLVWrxbiDSfwXltFww7N1d0CjN404WiWKIySi0XrxctiwRro5e7R3Cykc1fCsulw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSm0zfvNJUUEw2SCEVcBU3enwVm1N0Dc2umEjrr18MLI4Kc9pyPsCVIS-DgpNVmzhsMssY70rb7kfJTWG4VK3AZCBnOBiyk7srGIzvH-aaEw35c_4I4BXhYviY7th8dcvxFu1fjo2UGGQli_EqiEmxhtiJnCqknzE9wjQGIidw1H1Xdyru6FjWi_VOWppzZ9r8KhtyqPu1i9U2tAxO7qFiLKBPTX6xrEnOMcZRd8-w7PeD4QVHb_LQXBHJp9SHftQ68dyiVHhTc7ZTOEp6t6UBbKoH4D3t9fE1403C8kC-IQIR0uB2ucPQjpdZZiCRlpegyWP_tzAGIub2amysRkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=o5hOGJ2vmvMppRC_7PPGJzb1X4SZEcmg0Xr23czYabUzTQrhoKwT-3JHUYOcd3F0SNJgjdVIzzMuvDQyLRqw-7OeiugnmSQg-W9vtCZXPUlYH4emcJesaXcyFTSgU_lbYWvxzPpSCTUP9AhOYPJsruS8wu06FC4hLQutvz7qVETJJgq_U6WFNtm0fk--v5iSm9PpauK_YPCfHUpPN7CbRXN4eHJRAz7f83GxBTzC1pduSVYJO4Ja5kbO-fxJTnHWMTBOxZa0llSWiASbczHHzcQXb6iAb4g4RR6RkRbhZckwTDmTLUwIa4grpBgXw7DpuWmFJ6oySnpzhBbDQhFR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=o5hOGJ2vmvMppRC_7PPGJzb1X4SZEcmg0Xr23czYabUzTQrhoKwT-3JHUYOcd3F0SNJgjdVIzzMuvDQyLRqw-7OeiugnmSQg-W9vtCZXPUlYH4emcJesaXcyFTSgU_lbYWvxzPpSCTUP9AhOYPJsruS8wu06FC4hLQutvz7qVETJJgq_U6WFNtm0fk--v5iSm9PpauK_YPCfHUpPN7CbRXN4eHJRAz7f83GxBTzC1pduSVYJO4Ja5kbO-fxJTnHWMTBOxZa0llSWiASbczHHzcQXb6iAb4g4RR6RkRbhZckwTDmTLUwIa4grpBgXw7DpuWmFJ6oySnpzhBbDQhFR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0LAlZM2dbqtqJ8kPTlg1Z7VtH5jvTSo0XpZuC9V609dTOQ9BpWW_-CtyWRW-cPEMRuQwM1Kj1PpSSOKjCDqwXc-ivKJwJR5BmiLcJ9QZ7s10Rai-gesz-yIlI-0-CeKCeAKnDe-leL-LkCZkAoBTgcnl47jw-m-TQjd0Qqg0efWO3Hcma6tVtlA7s3Ym9fU6gHbZHvoR5YjxKm3-mYmC7gLzeRXMm_f4ULsw-zT-1-yEw2t_ZqwUa9Bu-RWv6fkz3rj60f0Xs2LZjaitWUNyrfSNZwWpTw_0YhCFRMbzlurha6CZHHVU2QPl1hyu_wdGmg2fJDM0BXdpcvrL1USpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SrhcjAM5B9MPFlfLA2RqcDCz9nFeKHffUL8oI18BBF-ccQkHW5EXyLjS_F_G-N4GNrzL3kVIxE_hEXdAa3zSbF2-NYjZBpDJt_OUR_qlquI8jQzSm2AA9pw-cBJ1gc8-oodSe47CQC5DRPvWYrEdnRfHIRTCEYrpr6cge2pOXXISWOGqv8gzoIMiToQ40VtYrNN_Jzq3oNMbp-XJrkovIJdJIfyeRq5kOQg0YaK9ApIDHQfgoQAFPGViLhKjB20W6oxSM_hSqiqnHfsf-YO6gbh6MXVXAZ2U_4FEaN2_6qoOqoOajmbvi4cx7Wsdw_93is5uet25C7cvLWFuwVzU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NvFs000hPEc1XQWRc6KLATvT68abDCmwEUIV8WRfz3CGSohyhB286RNOUCKLbOtO9zK32H-biC21D7bXD2VdnkGdIYbJc_-QZSXpN0hpQef9jIk4EtpyR9CQnm8aspIUXrEcQGM4nD65WK4FfOBAaxTrq9TxmYNW25NYC72f-o1ZuOVd4J17pSGLcxdbX2UdALMs_PpuPjFXrHt6cv4dlbcVpK-_ciTTlrw9NC_EHbf6UD5wb_Apg0OGDf_tRdRP0J99C0l3Zbcp6Qcx5lbc8dzWrDCpwtnz5TfCfFWNWHraRRwYHmG9Q6xBtzvjVJd9DZjDiW18D5s3nzEyLWglKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rTmA15XqglTTSAv8nKxjhG1kEpfdJobIT6KUTQ173Yo4-Bzrfs30XYDA3RLFRwv6xdlWacfmtuc4FnhoTT5H5BGWj--c9rI9fTiKUvnEJkgOcVHAL5dEbe-fb8YmBjA7mhblXyVpE_udvNb4Rqcv124yTqRDH96lJHAI-LYMP9tdYga61cQsWw9549Z8VXFSn_6igLh4ZdvrsOztg6y1EjzHdufyuWNjbAjwMKvEn1BxB2WFekfqHhR57nnzQsdEeHzlpeR7V6R_Hwe1-Ub2IpkzwWRijN2xWC3bu021Y-3ykFG21Dk14nFYOiNBnqC4N1IHtomEUNc8b_itmCR7SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl2CyET5GOBf1WsAtOp34F8Sm3YAjYTcEeS3Yl3SvhgrTu4t8c9D5k0NPEsG3UO1Tqmc0_L2bPf5o-lw0vi0njoch1eWQgNFPf6QENmfYBXdW3por31WIOmSqNtfpDG0yHVvq0fNYBIvbcQp0feHepMYFBgKKzI35nQahq0GsJelXIBV9QYUnZEAE39bRhG2BqU_rvP094dxhuGqlBDidHmGd45YdZLva-D3RghPpoBMy1RYERdyCXJfZ744uQgOqjVKLP76_tiYxy2TunrHLc8UhrOjRV5tsbnn9uvz70v1HyDBfNKdNjAdBApzNdjMWfY9KP87_IXoYbabAjP5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n-awt1Cv1m9xYjRRhzDEF_HEZs1AtsKT-aNbXJlRaHQ0_f4Qh7BzevNMTW7JwYm6TA2MGkPacB8yAJSlZZj5C6GOJiUdpY3gNLLosfVGdE3Zfx8mJHNKyFv3ah5pPxh7wI87yN4C1NzxzEhlUFP6IvpRT26mIVnv75XYHteJT2QVKUUybk8xFF-S91ZNveBK3awoBXQo90ew8zzJ15mVlP22YBk8jlmqt2iPiaoaMaVvcewwnbNpAMZX71a-9D3Xo2RqR0YNOnS7Cp65fEKGkto0d7MVji0VkIgOjK6rt5lfdEXtLKOpvALC2nqGyF3z8RWbgb2NakEIbL3Za6GCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=OrAYkt21TrWElKCcO10jzu4MYGBTh5EcndpuuxtI2BHT23fjeCxabR4Z7ydQhZbd0AqbGLbEB6nA1umJNFcUjB5YDBZLX8JbLJkzt06W7G-dcN4LkIvF6e2JbRXs6l3BhuC1ugOfyyAPRiPGsgmsvsoqk3ScwzQtJORr2_9zQNDDU0qMQr2ZYGS0wLuOeo37CWYUE-ePGH2oZEWN636bOmY3SPSeNL6cfFM6oWc08zLelbnpS2k_MgSG4iZCfmasZEMRUx60sK1cSS5IS_v3_5ugIGgYTZrpsCPNu4L7Gm__xffpmnclKabyIqzo5dax-uqesi05hA1fnZaGT01nBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=OrAYkt21TrWElKCcO10jzu4MYGBTh5EcndpuuxtI2BHT23fjeCxabR4Z7ydQhZbd0AqbGLbEB6nA1umJNFcUjB5YDBZLX8JbLJkzt06W7G-dcN4LkIvF6e2JbRXs6l3BhuC1ugOfyyAPRiPGsgmsvsoqk3ScwzQtJORr2_9zQNDDU0qMQr2ZYGS0wLuOeo37CWYUE-ePGH2oZEWN636bOmY3SPSeNL6cfFM6oWc08zLelbnpS2k_MgSG4iZCfmasZEMRUx60sK1cSS5IS_v3_5ugIGgYTZrpsCPNu4L7Gm__xffpmnclKabyIqzo5dax-uqesi05hA1fnZaGT01nBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ocp2_PXqI1BYCLuHWCBNG_qK9n-zaCV_Jp3b8gy5hOU2K7mLutxO17S0o8V3G48J3vu7zXvhVvi043f9NmtFLFZZ-9w8X5XEBsxjk_ZcppfEjzCVPT6PShNuofSlf3wTCiVOXQSKytem6G-VqR1FdYDGvqOs7TlsJoI5KTBr_B0dWcZ3w72r4xK3KNucsTl4XaSC_VQLozlinWvhXhShjUVlvpgzIEbM-TMNwbw0loCGwXiBQ301kdUm0keCM5J7rB7OJEz98YGZsRYJQtn8ER9O_6-9YfoD3XGB4Tuc-_Y051k6s1j5d8t_s7Rq2gJy_aYIsWCVjlwEAdeYkHBTcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EKiq1tfVNWERnfkFmzA0k-nx0CRmdDZc24uHKiI308g-mr1kf2iOQdnf7B8-KZIIdgwEChw_CIuKOtiPdfT-eksciMC5GNrctO0qPl4fQob-ulWHT88XRDgwshFmhFyY2X0eBMqIMdU4BstjViyrV97zKiWsvk8tsZsD6_6i1o9caFbC94c3vU5MsigQV21YV8jeY6iVGk7UTqQ2LxOzChC-DDUUq-UNklGey1A01Ou2qWOknlKGpS679xUXEXDTWZyL_pPtW8jMiaEy6Ac-IqGpzpVmDyr13fCDQzNkU6bPwzG2Bh2tONcmday-T1dfScr9k6_d05Cy7xJ1PknVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/js4wQ3IojfWOltxeQdn68BU4OBgj2s8VHIgfcYCDxAhTRXgOIViywd8ZDXXFkYiGIVOm4tv57oI5vvz7nwOohXelJVKQl-pQkHMsc8Rzpg_uYJ6MF4A8ukohD4TyWun_lXCY8PXNKOM3DcUTjCQUxSDBJIv_o640JZfwVYuRDCBn-8fJR7KixXYl8HF3rkWIOK7ytvwvEzcAXMjBHwEqRZ0174mvU6AXxmNv8KJ2d1r0Q-nalf2Ho6OK00yNkwwdetfWvdLpcHcLkT9TMsIoPv75IAsCeldtWwrL7ZdylVzWOIbnpT-Vlp-_1lOGhYQzxBKP0yNRJhuEvPlkCBIcnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuVHcy66cXKsjn2kNx_ltWScDrfAq8l-lbajO5GI7ih-LUT16txRAJiTdqjBvhsJ9LSq6fgVMj_etNe8KyoTkIY157Tfactf1TBbK74fI7rg5O8944jya_WQF2hP9AwostY_63JerKn-AlpIT61grWR7EHEY8scnEn5gFVu_yRPAqCEAALSyLfDVC_dgEYnBRXrFXzRtze3t0p9FvHHVLV_K6YXZMbUVJLF2YXhpeDvegbBaddA691uU0YVaDayLHdudp--DFvDeFph-2D1NaQ8FdAqThyYLUTldh9_yVCj0wDqFFk-8Wjr7zI6qecGROhLfkCt1US0YLwdO8VyjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAaWYTs4lanIq1q4PfxhgrG9mvjBGqZ3_SpMUzIXx7If34IXJ_VYOGbXbtxJ7NA1zbPXOOlGG3qmgu_3o5Ep2pKmAAK-NgICbpDOKMdZ1bqC4sPP9LYEAQv6mjQPIDgGjX9k5p0wzmaromXwYMrMH8Q9OFZoJmtKzoN7621RVo6a_wXrsj1niMEfQJlQGsPlJ4wfnmpvZEuPGSIc1ZJ8MKQe_LOta7qnajT7U57XEbFPJb0qCmJTY7DHv56awrWy2ey9SHk4fSczUSzHmed9tzuGnmk481EDJt8UgMw2Hy5CIG4AKueB--IYOS_KTFHuNIB6olR7pTjPUO3R0c9tpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDdNFWTA6xn00o7VDZ720liHO3YTinQVGi4kEJPQkRdbaoBd3c3zSmpPr_qdrDgdTeMcjFWzpr9I30QcNOBA_qtjej2dFO6w4IDNJqVbvm7rmyLmkAc5R1xJsBal2Smatt4bIBhP6lwsCQjqZr73WnXawf-_HbBqwOgHUF6qpdmTeDO-KSQCs2xDP7WdIjJdZ4HytbRdD4QkyuZFdKXpiQU-dEzLskGU7x4AhhsE6TE2zKM-VwXZuIoQIixhzYlc2061Kp9pJvcNdRarYS5wKHyvVymq7jPhVWOXXlsLKZiEp9ZUSFJp-7kiYYaATyRQH-RSqYTuVshrXaf00gT2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ueok_5qt1fH33WILV53rHzVSoT0bhB2-K6tu8h8J3wZMBKwGMuvTsc3QwfDQPBgAR_dZNMTJQPwiZ0naV2OVKri0J03UuRXst1MCjEco3meyb2CM_euPWPN8hmQs7J5P70ZJRfKhRSE76VKlzCsz6SkfYhpR8kQpEe-IFyq-oW7g8DwtWv-ziRyQXr_qndbfpVlijk7Aha1GnZMHDY-OJSGeYtxGWhHRYzH53db5jydrSAdEZanp0dR9YCX3yMbgT4ZKcuGJOWKz9qkbmFDNFRR32h6FIsu1EOEtw_5DXDi7SWpf8AGmK63o-suzWNLmtrzw3IMsWFbdvg84HR0KOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPNHfNUu38tDXpy8UzrEZqL2Te0CC-g6WmhvPSzWEnqkGeAOBANCBJlplGOeu9szIQjyd4VN-KxmemyD1f7I0eF7zexCPE9_W24D3krYKJo0dHCzSlyfw8kbJh-FSHyR8K7GhXGVo53TzyrvYAcgY_qnJulhwo8kcJnjQLm5GoxdnE2JTXXAyfv2PWFBXOuDOSAMIOOQtccc9jKhjsjdSlsmX6FmctfERS801ZMMLMYijdPwAdsPpuWb9OlvZj0_ipRZezSspAxAaVrpCpovjio2ZnrgyHQYv-3R-vLe7TUV-Ak_p-fnhECU6eS-0fSg9n5azDD96YJV_pJiHEuivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=uKJV4gcZTc-KsDcTQ72bJfxnvdc0CFgtYFybldbhCgy4O87iuSfSLeJXnwvxqiMFQQGzOfXD_ZQ6KdXbj28iG0D-K6fW4j_sh8PHeRFBILTb7bM996x94dHH1-Y2gywgZ65ZE-FjTe1F2O8DDGg8sr4uYsRBemRXXCNIxaV-1h5i3IzdC_DeAuQw16TIeYqBat1uIjKfAy1HWl11DUOUEBy731CEqwXh_icj1MPCTP2DrTHu9DH1yPxwwfJMA2UJgXQsF97wmOyiSt7v7XGdtZvTBKb7N5T2vdscuJXctt_BgBf2OwFhQNHlyRmkwpyj8sdX5tLjqH15f4kkPXO05A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=uKJV4gcZTc-KsDcTQ72bJfxnvdc0CFgtYFybldbhCgy4O87iuSfSLeJXnwvxqiMFQQGzOfXD_ZQ6KdXbj28iG0D-K6fW4j_sh8PHeRFBILTb7bM996x94dHH1-Y2gywgZ65ZE-FjTe1F2O8DDGg8sr4uYsRBemRXXCNIxaV-1h5i3IzdC_DeAuQw16TIeYqBat1uIjKfAy1HWl11DUOUEBy731CEqwXh_icj1MPCTP2DrTHu9DH1yPxwwfJMA2UJgXQsF97wmOyiSt7v7XGdtZvTBKb7N5T2vdscuJXctt_BgBf2OwFhQNHlyRmkwpyj8sdX5tLjqH15f4kkPXO05A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NPDm0UG7-nx8GDCcE8KB9GyLasCkE5qjU55C2vtrQk3vQFeowO6bseF55uZJxZKI33E_uL6p_1dSNzixBieUqZKHLmJKWg3pueBzx-Od6T9cHgv9UQnYnWW4SITze-rY7Ny-mOeVjEX6sFVU0aKi70p0E4qmCK7yuLjgFYXQ-lKj-u6bEVylQ9-bl_bi_IHANXWPi07gyLSL8UcX4qM4wegMMHdnLiHpzvmmqu2tqoZi4JvTSUUei4t-0cphoIJpUomzcMafbO3htuVMg18BPdTpJmcKmGP6frac9eJDF0OOLlkB6BphRpLz4tKDjbaYazODIJfBOLgzvd91rc28IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfUq4m5ozdjm3NWM1Y6FuUt6DqohpTiaMwPMHkPpI15Exnv341-FNz_kBw1ZSuRtPvvYA9gChJohzsMwahDJYKjGcRI8GuG9BSF4ONjzLKMmmKCLBiQb9yR-myuFjHAwTX4_WhQpM7RgTDUNM7XE5NUbB9UY2d8AbtxMFIqDUs7S4zddOl_Khqeffyg3ZxQClg66-ckQEsFqPjXqsZzLGl1YiO_rOFkpFurXl5LqiU-DrSulyoNQG6-70CS5sM-QWvSHhbnyUJYHAsfYhEbXQyPRZfoF67lb1wTUXDsD3zibyeB9vyScWyHrOHVJGbHFwdSO1WsWeFN05Cth4xxlXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXyqk1qsk09NsezVv8N5nf3_Osef6dJJRvGVdM5N09RuWxRMZA7toxwVT0y-zNh0sbHPl4e_ND7Ts7UnLaLgzibyyAkbDevKqsSu0WRGmQu-mjOfKcrvw9ptnodgxWCa9csYa1q0UZ-YdyWotTbps-GuoG6dgyk9D6P1fLuh06ClUnAMT3qeXwxXd6PR-MjA0cWILl5kXPBg9XlVqFgE7nFachLneO7Ftz1baXkSeYx2tOagwEMvCQ1NMk8MnEaJsIIyEW9w3vE7Y80nVcYG1h1Nytq-7n4c-OTnkeezn4WrqMWzxLZRdKwLoAVT6ez4f3x41vMTF4ch82E8hcbeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBsS_fKU6lvoh3AdvDz80tzaCA4eQcnFolSZt0qeD2tMpN8-wi9Mh_VPA2No46yR7NWrG0NamBfh3HveLYK_bD4H72ugP4-l3omSu0x4YTAFnOo9DvuUgIn6BkzW71-P4kgJanQw0NxLaOFh0cGWlrS6VKporEYNYebvavUk0xWFVZcQfrFU8qxTuai3jsKc7mEFTSmUCbFhBls_lPWlqtYwPazi4E_vw7dTKStKzREq_YaocvFuY9FQwoWtj-opB8003waK-pcuJMho5cpgzQTH01biMdXca13bDWyRXx7J49HpM3SjgtAWJ5VKxqVgfbuwGtt9rkXUNdV7h9LLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PvIsQj6lMO7q-G7vHQp_hp7dE83f3HO6usr56jDdKbfTKFnm_MzuGCSKkbaiehvCUzaVFGGSTX6BgbWU9xaNVwHrE128LMkHlCsxLhrsAnoNwyt7VayUCJP21jrDNJedj1QfpEbwDcDPjWaoBk1mJ_t9GG7YVteUq4jb4ukGaSm4HGqoM-bsyce-ZDFONy3EjeYcCB6jrMORcMmm_mXTOQp86wdNeadqo2na6zjGMyIQuKL0F9vXYqZg1WGQREvDT51xiWSxVh3ihz2CntRyq93qDUeCBN90DJGd6a65c42uo8xBcrBbueC4u-jGL6FFj9deS0x7pMCcvPer29gg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o6grHuYPfWW5Q_-2t9P54_RDstt3LJWUmY2ugdFhZwNKWuy8-xk34Zd13ejODKCWTG4rOZGUkkO67N5sW8SEcOdhgZH2eZw2UpIBGH1MoNwonkju1Kvbvusqg9HMgZQqYyppg_y_HpOUfmVxAFTbllRFSusR74x0R3evnJpXvWQihShjHFobXi7qvMWAOvx87WZmlA2KAT7XM2jYQNZupBOCZJ4dfLGsSEBBqnO4FlK6uFO3SfMFbgBe7zzGy41WOHz_Ghhkqks3KNKF-dPw-dUeDmzZ14D5zkzonb4wH9MUIb_-FqHWsI5YGRJJmyHHaKm7aeUYUY82sqvT6aGYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OGzi2EtNmX9hB5COnpT4EkP9bK15x7FHGsdxjyYm3YEWt649mUw9rIdgisdmIZX9lRcj9SteoweR-gm5lhW8mziWdAZCO6H3EhBGkoEUGokTBSSIPKFN4qpjElLqS6obLiGUh6T-b9oJkbry4dh9SspFpHsqeGUKydxKG2RLCQzTcGIgkW2KXN8tevzYn1aTmI8Qp_vBbowIZLbHrEiA2-NqjWzjCDlSjvdgQwc7T4wvSqfWXMCWmVFRpeTcVx9_b_iIxAhUKP6aJyde2REmkP8Df9Ko_8ZHGw9yp1EtabKyIa2zHnML0XJyYuxQE9wqAZXirxeHSmLjUrWC8nFuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b5Gel1lQWGZVhs3mtOaN1lSsLkYxPIlR58VwF6M5mD5CLdlL8ekpwf12cQRK3Bw8cppJaF-Nkq48Z8DStjyy1Mtp5_0-LZTT1H2_Xs1d08_BujC00bwsQ_0Gpg54Lxo6gFx4TEcr_8SrX5zTVUwrs-wXu6kwWumlUuPSvIT7ZN9BwHYzVVNZaipEwFTDuMJ1v2f0kQiC3xz6-y15aE9guois5hBSpAKDtzD2E15j3A8hqT-9QJ-StAvRSYoepzhAkO5_82F2zh8pEBQYQuYwQ16jZAPjur6H-OSCu7F3w9TSauhAGOHLDqkrxQfkYb4qveyuQW4H7KIRT9myDU8XxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GMhyJPEtZ7yx_sxN1Hq_yWI7RUHXlkK1SM5BtppA3-7K_rcRE62MDuVGJD1SyMOOjMK1QgVMprmns2ZaILD_nUGgylX3dyG5ig6_zEwHNP5c4qOk0bcpQiNsWfPVVof98pd0DIY9QCo_4rfPKKBtEAYPEuGl-mnUK4j9gbYcdlTx6eF50scdXcCJffSJMAmVqLI4dCz7Y7q0vBesnOZreEwDZKeYWhA28inbWHrX8p8K_jSYHTDC1hOYyI8pFJp5M5na63fGIHEVRVDv9ZTfqgpgd2anKcs1Gxg39E-nWxWLqFANwASutSJjudMgCkyFjFS8KWFMTFGQ-KVgxlRZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NL8CyGFYdPdSXV3nd5bK_oOMPlj6QzGiS4514B0AuCIcQS8sqI95u0gE38qbF0oQdmPcuBO3jZETXNYj4H6rAZZebcsgzo8sO6YGtFjE_gEvmxvcCdPwYQq2d1islCQb4YYDdTwGy74QMze8zc5DfhdUJjiNMfVVQCwRLzGpS_2PiBpbdFMv9C76e2_i-TMJSLvfV3eJClRybFyJr03DjOLBu7ivhPv5axx-6g6l0AkB7QFoJeBMu1AJ5rlgYUwbMr3fZ6HC4rpztEX2EEIQULa1tzRGYnO-Npv-Ueirq6E4dI8I49tnUzEAjodlniKWogTiwktaGZBWYbO_fpqDKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jMLPr_IyAq2cOoJsY3uym76dJM_RLs-1ItrbjhNrpPUAWqYrraSfFPkThJaoI8v7w-I5tCuGU-OeYm3gXqmcH_rbN__IISj_zE_ecZd1qNXPSSSx5TGHuCjfn7rXaAwm-g7BfXqbEQAfDUe-OokTw8tSavH8bNBtOLU65p6QU5Fdo_LTXbh7oYVPCaPM1ZYqGvb612V-AnyFHDjIDrJKmzvxYZTprTWbr-fq3-JHc7j6BLRia15DitdX495nRi9B7qel1uC5oCqbGPwlBgKEAQd5apZG0LjNG2BOifzruIBemFzugRhBBhLcssrnyF_JblcgJHCZk4AOwugTTjqc5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=j1E8umnVm45yKzWBF1xLZJchQW6DgQJHSa5pyWULU6zt7RVCMuuUVftEWi1US754RU02YtONoTDQ6JmQr44AaXZistsbPWTt0isw6WXnGdnH6dSMvlVoowe1b5JSxzF1peHQV3QRgzgMyo3t4Y5VEoau5wUOioSXTQyYbmgD2l4wp9nd4w0b5JDKlGVAxNUhCsaw5HoHg80KZHId3pEFf6LdysZrWPlY-wE9-arbsPk4Ze1a7kNDDqCmeeuw4EPZqUg5KRZX-Zp6ZcQ7zjsL-s0K366thNZvKzCq4xcZb_CEvrPmDTDikqBuiZjKbUFPgj2sGIb8zs3BeDIvW6FQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=j1E8umnVm45yKzWBF1xLZJchQW6DgQJHSa5pyWULU6zt7RVCMuuUVftEWi1US754RU02YtONoTDQ6JmQr44AaXZistsbPWTt0isw6WXnGdnH6dSMvlVoowe1b5JSxzF1peHQV3QRgzgMyo3t4Y5VEoau5wUOioSXTQyYbmgD2l4wp9nd4w0b5JDKlGVAxNUhCsaw5HoHg80KZHId3pEFf6LdysZrWPlY-wE9-arbsPk4Ze1a7kNDDqCmeeuw4EPZqUg5KRZX-Zp6ZcQ7zjsL-s0K366thNZvKzCq4xcZb_CEvrPmDTDikqBuiZjKbUFPgj2sGIb8zs3BeDIvW6FQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vS2eGTQWD3JTneEkMO2D3JuyxPJG3COmafk8aboQL2Ji9k-pOO4BYkP0e6cArV3Tkcycqmmd8SYYiqEnlKl4CAN7llpYzxg6p1TpkswD4FVw3JGHmDbq9Gkw9tJDShaFHVCUsOUYPHaVhZ4qztOcBaU07wslzLuHBMO6rXfCJnx3e7F7MlS_6_1bLxhhrZ_pBdXyGAWydjiGCYpNmEfR73AKRvwC21-39qlbhZQf7vn8CZKJxs5ZoG9zTaecf7sW5NipCTQJbA10ZQSugNA1TYGy9UcM9wXtO8QWpZBY01UAmhk0ZeyzU0HfDZBddK661YZThy6NU-zA8bCyd4mCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FqQVXepcDIwaAnHYvNoQGgAiehIYrU2qvbwSZ0vQreWON1Wl-r5LFMBWM0zYDX_VbZfx2MxWeHfkhz1JnT--Qe9pg3e_4xUDYFaY23f2tp6omy-3I_O12xwh6yNarYulDGNrtQFdNPGkIbWzprNxNEHsBIhRCSOJVkhVGFu-u8iEKBSZQVS-JNUhd6Afzk0NJqa6mHjaF1pi9HfkyxckIpJ2ZjFPQ5s4A59TbCgoFQBs0UhaRc_-ufOIJu6mR-x2Om087OSD_k24rQMvBqetmGozhtmm9IbOrfNwgMmvuXDklV_fX8UCFEuOB0Vmzu3oezdmG2C4RDhrEdDL-AMREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BDM5jCk6mdEUOWmgYZLAFCemKrLjSovIgI2QyEv0Mxc-8mhtKw2-3iO8Ma9PMOKeyT3PBjrOQHBtrSqPMxi2tOyptgtzGuzCuqUMKd8t9cEYvXBin5L3l81_5depTagW5TnqMkoiKGGEZ2ygOcbUia3vdrJIbvyqTGmN6adjcvM_53Dn6AVDq-OA2wvbtQ85-jXtnkKCEEqwJ-XiQW1U5z9_67ZEQbVkG2UYlbc-1z0oBPj6cs1pIar2uW8jbL6NS-oHm5IAhYRv5tvaOttkKV2mZH0r1EnWHkK_DdzSNuOK0ORLJCG57xx8zfzJ_RrcHAUoDUUzgvUGgtmN79xXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TDLtgILd62lHHc0gHfSV-ogbz_ROoJZ5b0lkVOP6zkr894w9Nz7M8_gRecMh0l4bssbT9zbK1AbvfmLEgM29CigzFhJ_odXH01w4T4SECUGeW-UkkIMwaOGDarTiZfgYT7-wASkiPgxwEOMUSvsuoEL8hZ6pyAqfskLGt_nYsxJMqtpGVCYF0K1QFC7b8wndXdNCYgthx89AgKJDWUDKUbCpmvwjuSuaBOd-9GqC_xbypldhdfOJXz3htiykrx7R2ScAJ-Bi0EpKXHTayQ3bxu1RugacEUPQxpTUk-BPAaEAEIyBDb3TNvFiO83dVm6bOPT1bIYjjPav4YjZpKHLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KCxip2rlCiz71hJUe1-me42csEEwvT1Lhx1GLIe4eyUlN5y-7IMR9d74RRx_gU-sV-kC9dXzfZM9mxy6us0G3K0SSqAUfQraRZSKOOSXD-wjvlVOy6xqy1FqIEyGNwSht33r8QhG5hYvWPT4nh2OtI_OYht00CmeGOC6ydp1yRodxfJz5ntohtFGhAvUaBc5dM4bsgZG4xBU2ex9wziiEYGM30d-6k2HafqY979ElCxJ9iMk_2g1udtkVaiF4TDNPL-5YNEUPmSATZBt7SKqjSdob9ohHBbuye4z8I-lM0Im-mEXGN9uqvJpw75hcVflT10SqH9mnoH2aLXqWb5hxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TeaLgv--2lT9ZhFLd7CTf90kbz5eH7mRSsRyxysPe5MjIdDKBgF-2hC1kmwcwG2-ds_Yde4cvQ-Kth2UuQxfHDcXfk1YeUk5sYhO7Sro5ZrZ5JGcF2hUW7eYSeskSEcpeh-5cbgAM6IExUZuuk2ne3xld5LFBoAVx2vITVQMgn2fD7piPPKgB157UDgSAX_mkCPvN5IyCQSmbrRfUtfmgnE5HkjylYpTUGY4FsV8_ObKd_LbWdh9qpSs1kL7ajqxwuf2LNiQIbZddU-HUs-1sk-6XmTj7l9HYRteNQ5Ufncu_A3B_9NVfHMngwwCtTUjfssHYq0ShlDAeon8xM9aUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K5PzQt8eI7Dv2Fw1dg34VlGYojJ2Vyfc4uw9HrsdjzZYYMKfA6fpF7qzpFbM22EWWAlQJUHC8xsrHIDz_x9Y1wMlYc0dJe2B_2BJD6zNPWVM2TCVoDTuWUxSVCxLJEhyROFPSv4mxuDnx5fbgKS-mPUfEYaT3GM8O1OcHg1E9PPHGM5jQGbSI8zkzgaetiQAN1t7SGJTyyb0JiHj4vjHM5qT-cIc-AlfahoLvSDBQHf1iM1z8BlK0EHX9XWbNOiGVGrFieHaxT7LTbKhoJMAdKQb55QjcYxuyvMENd0t5fDJc4-JcGXHcuQTm53xirIavHSx6gEObTv5I-OrzJUXvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/am8zwte7ZF0J2rawp34gwm-VtX8oWyvmHuNjB4s0DpZ_fvslWR7Cye3bzptTCLITZ8R8JAoQzHek14OwVTPhJxk_oibJOqy3vc2NhMi4S9d8Rh827M6BHYB_JvMaS1J1cG7boCIotmRfrz_juD7TLr_1cmfpbriegYGtvwc69V2sBJfs45_TipG7_u3o-n_7gmF4vCNk7sAz5vqC70eDrK76nXskCxRsVoEwE1R0-Zbef0mrQLfBbN-RVcU4Okd9LhCxjNtuy_CVEs55vHzJYsbXhYOw64Uodjo7zBq271LNxb5bqQYb0BdcgX3jG96RBCdXzLeJUTwOSg0QS2ldCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K_uKGrRtXfcF7_60E9llkMMCZVfAGNorkv6rOkfdwKtx1j0bAPGht7Rb09HQbZIk_WBpk5EMeeL-CB5Jh8W-seyEa52CSvCDoTi2KRpYY7whj7f0v-LxKZOIF-UyunD1RQwzzfGHbaX12sV-v_JTl1ghM-SPKyI1InI6vIOK9v7e0G7d9-b8LQ3HVFpGnwVTd-z7KhdjsXzgGH8Z9JoZO5GrEBOYUlioeeL89aA0vdrm2KnBBbYMlbpZwwhvriyaud7UqMkkkX_XI-D8kYy0oR7dy5aSGrEHPkO4ED1VhE1d_MZJvuiTd0FgpXbxpbIiqcMaZtvJjiMnoI_so6CMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H8CYcKxb1YCYCHXdpVrh9LfcVHuM5JdIb2Gk3he4CsaKe0Ygy0ViTIt65YBpj_-CKWym_9Sm05ThXBRnuf0gnRxta0_AqLSe_J3LwkRLbuweGf2eM4kZAZqgISdt3shHrqZL89sLYlXP1Uh3THe3GtftsYfWTZT09h1qi6rE4Rj7S1DZX4utBNn-nsVNsWpIoRFan8lvC_zk56gb9pJC0_arEJKOO0kZi36SrXGwCFEEHJcNU6o5Yq0QDaXO0Qiz92RM5hXd3nPSyUv-QLZpE41sDHkC_yfmirQlpoYVf6DOkkHLKugKY-wElLj4V-OQ6-vRMGy22kfmHCtQ4t9Hzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sb5hsnMaPR-B28lhT_FLLn3phEI8KqwmUDZ8LMgOSY5gGMSqtxvFTHvbN1GfrGVAGpwGfC6XI_glI0WhJLm_eXAHERSpv7-FNDkcw2TA-6_75EoyehU59jQ88rxaZ75XlotvGnz9PrUgiH9w3a5YUpoTbmc_E_FZ0aCQt9D1Dx1ZtyD6sNI6qfxNeD82taXYC-IP7JD5Es4oFhm_X7zx1cB2h7--jQLXmuvIxSee2Hki1gDU52t4XTtHfp4Mt9HiLwjxu8M-rmrOmj_1I14wima8t3Nx3hNzEzBfdpmaj0hvgVZqpxx4sDlWRYvxd9fJj5M5_C6nEarR-whk4fUB0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FOeLxahakj9xJtT95GSHy63ZT7qzD8vX8D-Mzr72T89nGX05Hzk35aOUGrQ37AXqpaznkNSV4_8zKhewePVpJyWiS90ta7Z1GZJBVmqMa19Q_Us5YPdursjEqyxYxfffhtgSjXOb6KErWhRH--zi6ymfi417vHmzFH3wrfj8ncc5XULPVjle2w9PSCHaIxm3TyRpvspfcsDpeQ0EwGoI6PIH7j7pKREG8PM5WVtdg8fs8NM1-R71GRMszF3EJNtDv04CSvgaBEBbya-8UVzRw1zJpGEKNzrAa4uV1BkHLYhyEgAKQJmijOXAJT1rh7VuD78lyoZ5QFZzX896-7g6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oj1jmiKlQiw61OxG3uQmqNuSVpPQaXyaFGXKsCflfM17EBGRfeazAoIFN7t46Xx_e0pHXGAzTIqh8oIjsTcxCIyVts8veR5dL65ZsME3AtJuJCtDpjv8PdnGXBFks9wwZY4rxbfcQhLxEMEOXbfQ2xstxvDCdJg8crmZ1SwTjX-M3B0AfloVwd2R51p69BxbZ6IARR_8l38snhsvASISEHP_D6ZpXS44APEMDKB-rbvv8SSTzwicOmtNRTV_yiykuCTfseH1q5m_fFVnKTeYdw73Eb8yubOkLRSWuztvXAiA6wqAAnVpAbDB_x79Gh7ZBhh2W9nbCixpjS_68zRnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AAhqFIQB3akr2h0MHFKMtieA3kRxdUXK-elDOoe_pScDQMLV7v--2149hTTP1iMUX4Ub6FPlLP-gfkDV8GkFZIj3wLzH3R43h1jkoZoIIlsjKCxHn33mrrH3U1W__rtMuMheLJb1P7JGVXGqehCHAoc_OxcmSCuaI22KBCHLhpZvMlCW6J_ZF-tH9FkHRhDue76lQieJpRDaJsuOT8Ce9PH1UHegSbBdwujoChGQd3cNxqizog5NnhhGt1IJOsVm4NvvCvk2X5-J24ui1x0xzwklQBqjr4HlooTdfqVUf0WtjiDNIf5UZQwiICZolRs8FfGoWHwp1yozaQ4q12x7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UdlIO7IKb-FbJjyCuB7iK8pAExWp3YG1qcst-9Phu4ZfUk2yIoUwOOiBU4ZG5uPSKhQ6F0rokzaGoQOjA2MRGIUvvZZuFwqRVxqcLNq9oSd0sRlKj78mdYWIusZAqsEChJI2ft8vg_2raOoY9Yd60dG9Re6i-L5PEwNMtgR5Y0ibSSXhY0tuaQQyaZ3nLGp5MKwJOHCPDKkwwhtzMMDni0wc9jK1BnNUjxHZaLRFzqjTJZ_qSFIXp2wPUn27m-OgoWl6qFjUIH-Lhyk0o_NuniJGaWb6CMZrp3j55HXRmxnTFVVYF-OgCgEpLuYCbHZQWJrFqCl9pSxY-jhxlBnbgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q2-a-jqQ2Fqciyp0UhwjS_q6R9FyB_n_ihxq9KwcW7_FkeLOqJA3UmXDIODbSTMrT25yG1-WgaOz2ivVTHFvOEX0lVnXFu_h9n7ig4lofZV-4QOuiWbeEG5Mc8zjBJg_YfbfVIuEvVKONnIAm4fF9qQHNKqxqWG1jpzUsaMWsJiLHkLvoMC6iztr-MR9pMMa3cWLzLiLTg0XLXIF6bVvwdU9lbTXoNRFt1VdmAaZm4D-NeZWNT6lne_e8lo1pPTpt8vN38SW9CkWtu3Em4N5bvq8_aQKmcdH6s2q5vVhCqWBAp1bKZ1kJ6m5v4Jkwku-CgP8-Ok4zyKxfZL-GYA-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I4bwZyVLGG8zjnjRpCce90G4BYrZ5jZ59q9DXHdY6VZaZFUxM8hUmea5nptr388svv8VvNe88uhFSxz2yydLfAEXKj4L75Cz-RgiDvZY4Dt0fL0k4wn9Bl-ciu8I_SvaoRKAS9UJ0iyG9S5JZfY7keghT4PT0YT4tDpRejfQEgmWb0qkTBzzBdNmhS6TIEommmKNuYBWQHBOJuTWXkzsNnmWD7r7OyVeOOFeAELZEfzaEGBe0LypJl7oEbVEhXYNe6QStHM_8S5ajo9mTMdGXWINOsDQDErd27P8yDV26sJbjsE1AkP5C36kAxGO4lL1ItbhX4GiDPAvXIqClzK1bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
