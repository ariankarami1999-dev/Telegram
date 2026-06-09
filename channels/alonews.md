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
<img src="https://cdn4.telesco.pe/file/jW6S-yCiFaKFmxA6l3b4xDlSAI0NDTvuToXB99bn-rwSRY0DCw4KkswGTKG-TYHbPE_3nkr69dqX6pKg6D6aGRQSUwghNo9Zi7nbr2dt38UBQr-Qh8bj1Qrt4XDC_F_tBebH10Kcpwyx3NaPml8yLjpUEeLcI1MeNG7nZqoWT9vEK7jSoUZp-lhYlXCI9hXQgA-62GScjRlZlJFUgs58QMfaPsD3zdJ43VlwSgx-CyXVz8pf3FQuUjz_4ECkSIwWr46UbJe7Dxy_tTuSyCIUbDy9q-abTSWO-t3BWmdIJaKHbxCI-PrUKuFWD6vHlIJhh48VpIwqoh1gC2aKCZj9oA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 19:46:14</div>
<hr>

<div class="tg-post" id="msg-126561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ونس: جنگ ایران یک سال دیگر به تاریخ خواهد پیوست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/alonews/126561" target="_blank">📅 19:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126560">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
گفتگوی وزرای امور خارجه مصر و عربستان درباره تلاش‌ها برای کاهش تنش در منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/126560" target="_blank">📅 19:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126559">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فعالیت‌های پروازی فرودگاه کرمانشاه از سر گرفته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/126559" target="_blank">📅 19:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126558">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
العربیه : حزب‌الله اعلام کرد دولت لبنان باید «روابط خود با ایران را اصلاح کند».
🔴
حزب‌الله همچنین تأکید کرد اتهام‌زنی‌های دولت علیه ایران «برخلاف منافع لبنان» است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/126558" target="_blank">📅 19:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126557">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
منابع خبری از حملات جدید اسرائیل به صور لبنان خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/126557" target="_blank">📅 19:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126556">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
به دلیل ریزش آوار در معدن گلتوت زرند، یک کارگر جان باخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/126556" target="_blank">📅 19:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126555">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: ارتش از پایان وضعیت اضطراری در شهرهای اسرائیل در بخش شرقی مرز با لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/126555" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126554">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKYLVI_NRSTJZuMbB09VZzQ4mCe4p21FZX7kOL_WuyeHgReKKNLoTSAmURY-Asaqfp_2rXhtXew8T58tW38mvw0L0RozKIzXBy5ypNhBtHj5n9Rtvga7kDg2RjxgfbksSfbIBUyRCgQ4GSyz0A_AWD2zJmXhPWjD255Zd4P6cCfB3txoef5yOB_D2ss6T9g1q9CuXduza8mF0fZndTC1BWqCbT42ABUUZkGitmSLvLfWe_LZULBvtXXOA35C4YPlMvQO3Po7KcjsMqDXERzsaDuOFbyevFHfqXYoIFTqWicjCsRrqB18UN2JS2pYMOoVP2wLzjYi55mqnlNOSifSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: در طول آتش‌بس دو ماهه جنگ ایران، تیراندازی‌ها واقعاً متوقف نشده است. با وجود این، یا شاید به همین دلیل، اقتصاد جهانی، نفت و بازارها به خوبی از این وضعیت عبور کرده‌اند - اما تحلیلگران هشدار می‌دهند که این وضعیت نمی‌تواند برای همیشه ادامه یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/126554" target="_blank">📅 19:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126552">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFc0lyePZ7vVCzszoXHva4cdbFVT0CX_IEKyqjNjASTJFrZ4jt3ZdnBXOoIQ3CRFA-rjdQM9cn3ql45hM5jHDJ2VUvSShAVff3PNXvwl4zjdPpi9aLSCh0329T1XjCl4pKCZgzsZEP_WHVjpLuWqOUZ2g0xIOfiwzyIGBwodbgITlvreIEQonetnZmE9aSHq0rD-mdt8ADy85z4qk0TE-aUJMfWiuP9tdKlpUGGZfHaBYhqr-xyLZoQJNnvyRYPNpmeTOMhHIw0o2zurbk3cQ2G1Tc-s0PrABKs1a5pW1BYzjKGZAyYHF-UIxHfSLjCZO_xo7iSpNWeXNIzhTxm2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8884fe0fce.mp4?token=la0IN0TTmZG7N2ikKOdV8UQnOuB3AYkHIXRvLxI1WXGoKZYoDwLJNuGyNthoGkV6T7GUJKzNfkBEYKLLsuyKbWDv_HpIPD-oVFMYu8WdyAue1lgjlPG4_-p7xHcpjGrI-B0T_mYdoZPm8GHuNaphV7gTbFbnGkd1ms3s6U8BZHGfNdfBM4HKrJ4ZNiSRSOYNo_XR12LPVkZ2ojC4-WST_0Nj3UUr5NNn59VEjCYIJLuB7UWM97L6yBG2TG1in7fn-Q6SDAdHgnBVAPSaUYBWu8OEJpvjFfw07vwZ7HVYKAg8AzUY2ce_w0cuksOpbU2tVmViz-OfUrNcLHfjPbZk6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8884fe0fce.mp4?token=la0IN0TTmZG7N2ikKOdV8UQnOuB3AYkHIXRvLxI1WXGoKZYoDwLJNuGyNthoGkV6T7GUJKzNfkBEYKLLsuyKbWDv_HpIPD-oVFMYu8WdyAue1lgjlPG4_-p7xHcpjGrI-B0T_mYdoZPm8GHuNaphV7gTbFbnGkd1ms3s6U8BZHGfNdfBM4HKrJ4ZNiSRSOYNo_XR12LPVkZ2ojC4-WST_0Nj3UUr5NNn59VEjCYIJLuB7UWM97L6yBG2TG1in7fn-Q6SDAdHgnBVAPSaUYBWu8OEJpvjFfw07vwZ7HVYKAg8AzUY2ce_w0cuksOpbU2tVmViz-OfUrNcLHfjPbZk6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال انجام تخریب‌ها در بیت لاهیا، نوار غزه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/126552" target="_blank">📅 19:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
زلنسکی: روسیه درک می‌کند که اگر ۶۰۰+ پهپاد و موشک وجود داشته باشد، آن‌ها این جنگ را دقیقاً همان‌طور که ما احساس می‌کنیم، احساس خواهند کرد، اما آن‌ها این را در خانه خود احساس خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/126551" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde767e669.mp4?token=IJKG1yaGvQlxGEw8bWGAq-czlwxdcHARSeNmkBsz5Lz3B0GTvqNFbAx5jIknfbznlDX8gNIinkj5p0hMpiPQg999Y2D9xRFVirjTCYkY9SMjG0-_FPFdb6sJA0YeNonw3T1j_StbG90slUvgQW12d8PR6PPUf436-m_uCB7nh3w0ZNlu4A7FhIOiryD7-YAqdeZhf1sOlLbaxtW95vNteCeHez7dY7vIdOX_vSkZW7SrT3-n6AZLb-yfYjUzGE4kt32kqwULQZgLTtoyT3enB9-_3k0QKSo19epGeqaV3xZTD-pLE4W8ZzYuM7n3m5eBeDcBCDeN0jJfdS1LzWkcxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde767e669.mp4?token=IJKG1yaGvQlxGEw8bWGAq-czlwxdcHARSeNmkBsz5Lz3B0GTvqNFbAx5jIknfbznlDX8gNIinkj5p0hMpiPQg999Y2D9xRFVirjTCYkY9SMjG0-_FPFdb6sJA0YeNonw3T1j_StbG90slUvgQW12d8PR6PPUf436-m_uCB7nh3w0ZNlu4A7FhIOiryD7-YAqdeZhf1sOlLbaxtW95vNteCeHez7dY7vIdOX_vSkZW7SrT3-n6AZLb-yfYjUzGE4kt32kqwULQZgLTtoyT3enB9-_3k0QKSo19epGeqaV3xZTD-pLE4W8ZzYuM7n3m5eBeDcBCDeN0jJfdS1LzWkcxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: همان‌طور که شریک امروز در طول جلسه ما گفت، اروپا بدون اوکراین نمی‌تواند از خود محافظت کند. و این بدان معناست که اوکراین باید در ناتو باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/126550" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: تردد کشتی‌ها از تنگه هرمز به‌طور چشمگیری افزایش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/126549" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNwIiueLekstbd2GJpLU4wtSTcW9c_ys_m1K0XlKuSPrl_EktBGlb-Q8syaehTnjfhu_WtFw-LvpXWD_qsqcKL3sObsWlwKnX0hFyUkfpWyvJ5lXj3TpxHZh2FtQW0c8BGAePbdhtSJ-C5Bgycde3St-yLy9sTgUicSnwlem7PnVKpxDNXAVBFTD3BCO0UgJts-D5K3bOpi1rKevuuQToQdbupRFWNxGP_Tqgud63JoPoLnL-psmVfh7CvuPrQImTNmH97yKndyRieyF404YvmL50vVkJ2z_5HNXBuLl4N4WZ9tSPIjFHR7Z3iLi2BnUctXOYgX-15sPV4gUblDZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید حساب رسمی کاخ سفید در X
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/126548" target="_blank">📅 18:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knitpwVh_eoRZyEoZ-qWCCdo1bC4pxbSpiRPxZKZBLngU6v13m4Ben2x2Y5wMGdFYzeO9m98AKoTUerJVB_mYE2xdJcEYWmrD2ZWmLrC2BxesAuauUcFH27tdaYgbgaS3F2O8isO8iBY90RYOF7As7FNmoen-8pU0kzg_XubKxWTx_BS1hAF6CG4NQtkO8ye_nGrF5uPjhGKSo-bJq_vHghdRFFYGdTx-rot4-bbBhbA0GUuFFsqzgLz5PoaQxXoHcmj4o4j8YSPm-EznbDNNf4y10ysWnnCzOFFHJrAMITZD8pBI0pU_H4rcdX7juBLrJUSCvN7_e8igbt68kLSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه رسمی فیفا : دیدار ایران و مصر قطعا دیدار افتخار همجنسگرایان خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/126547" target="_blank">📅 18:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر دفاع بلغارستان: ما دیگر به اوکراین سلاح ارسال نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/126546" target="_blank">📅 18:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNfFAYhfdlV1Tie3ZUbxLoL8-46_PpRF9Rdc98N2o1cY0uwKnaQ5P8vPwhOHRSTJ1q-zEqSN2zysURU9pPiyc_7sLve7ifugeJQFy-gIjfTXpmZoBjp7g10IGwdqhAmiAuOsCQh7cQvD1oquyacCr0842C61e8Zz6zEVtEBED83Mr8Gbsuv-jKyauHc5yh_ONuUNcRVwhmA2BLc1zv2gbDFCcFJjNZCxJ_Te-3fJzOgw2Q7m1o82pTNlVdHxkDbV0e9lU8Xff7BeXTvGx0GGsaY5f85NAN3XHbjsP9G6C0fNuJibfoPudtvaK-MOY5lR7yUWqjkjfsmDLFaQy7ctww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/126545" target="_blank">📅 18:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی جنبش حماس:  گذار به مرحله دوم توافق آتش‌بس، منوط به توانایی میانجی‌ها، کشورهای ضامن و «شورای صلح» است که بتوانند اسرائیل را به توقف نقض توافق و پذیرش این توافقات ملزم کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/126544" target="_blank">📅 18:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126542">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شبکه العربیه، به نقل از یک مقام کاخ سفید: مذاکرات درباره توافقی برای جلوگیری از دستیابی ایران به سلاح هسته‌ای نتایج مثبتی به همراه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/126542" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWU7bd3Rh0EX79ciPbGbEbHQ3GY5laCRxIE-CMS80yuSVnt6rksMBj4pj1E8_-K0IT7srUQHf62qPSPd6nECMSokC_UdhxfWFfM4SFka0vGKgE3SQEToWfJFswWcgStJnlT2ZA4fsWAVNFxK5NzRoc9masoni7XZk2pC1rqjUDFJV5p0HRmn0SM-T1WazqYdwRdEmMX28uwHpBMRLh0XvB9mBlK68JseFcnjV7HyyzP-Y7tlG7398B658QQMhNWNny3p4zVy2pkP8WWYjm9NwscqpTfjzrMq7alDcwJivCRQb1lvw_oQb1UqINUyyVr3khZm39nIPLbQKwI_z3W35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل امارات یه منطقه ای هست که جزو عمانه و داخل اون منطقه یه منطقه دیگه هست که برای اماراته!
خاورمیانه همینقدر عجیب غریبه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/126541" target="_blank">📅 18:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
منابع دولتی پاکستان به خبرگزاری آناتولی:
دستیابی به توافق برای پایان دادن به جنگ بین آمریکا و ایران در چند روز آینده به دلیل وضعیت پیچیده فعلی، که عمدتاً ناشی از نقض‌های بی‌وقفه آتش‌بس توسط اسرائیل در جنوب لبنان است، بعید به نظر می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/126540" target="_blank">📅 18:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5669cdcaa7.mp4?token=lzUD4GV11PJmeiFxLfnf9YvYwFN-eMEMV3cRi1QTwl7JFhaH3Hkmv87UjU_PihwgX98L6x6BPEehYQfIpkIgfSyXwVbQdkKffinZwaPoSHPy1LvqOb-DbHPWm_ObxsqcqIye8MZeE1mVcVXEWKkjk3Jgb_hiaSY0k1N1T8xpdQBqfdk0sU-x3tatRtfdJRCs3SnUpnB2Ho6hB4ySwNoXYy_6tFxaUe-sO_g8XFyIvfUGEXTsDWJyyMtfYML1Q8berW96f6hDaJDsNXBlRoNNZ_fWwd_jybpbZkb7fC6gHjhZ-Sa9FdcTF-jsSZtwAAyJ2jyPJe4Cq3TXDk6YdHS8cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5669cdcaa7.mp4?token=lzUD4GV11PJmeiFxLfnf9YvYwFN-eMEMV3cRi1QTwl7JFhaH3Hkmv87UjU_PihwgX98L6x6BPEehYQfIpkIgfSyXwVbQdkKffinZwaPoSHPy1LvqOb-DbHPWm_ObxsqcqIye8MZeE1mVcVXEWKkjk3Jgb_hiaSY0k1N1T8xpdQBqfdk0sU-x3tatRtfdJRCs3SnUpnB2Ho6hB4ySwNoXYy_6tFxaUe-sO_g8XFyIvfUGEXTsDWJyyMtfYML1Q8berW96f6hDaJDsNXBlRoNNZ_fWwd_jybpbZkb7fC6gHjhZ-Sa9FdcTF-jsSZtwAAyJ2jyPJe4Cq3TXDk6YdHS8cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇺🇿
کاروان ازبکستان وارد خاک آمریکا شد؛
پلیس آمریکا هم بلافاصله با سگ‌های موادیاب و انواع دستگاه‌های ردیاب به سراغشون رفت
😂
@AloSport</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/126539" target="_blank">📅 18:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3Jl2EQHlX6FOfWI87hl-H8Y6Zo-5zsE6Ns8knU8QhHb8v2mEEyzJ7f2Om9Ip_1J3Ov3MgTFujUJArY4fsPv4Gf5nY3zv0Qp0Cq-qxX-0IGuSphmocMTAvvroHjJEz-FwXnZ5Jfi7p6x9c8y5YyIAMdNGSn9rLjLKyvNlA2OzYUF-RTM09LsvcET9KQw0CDdr343Wx_5Pp52fIKi6JK7caZcF8R0hc2NM37FpfjmNgnY08nF_4PwmoQ6j3y-3Zua4db-f3Lu6TE_IyAKc_cDswE4O25Goi5EKpS8bnH1bpBTcAOyMT3yfsRcsvrTBGJMAf8spkA1s3ca-jNsWNJSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aqx3YkERBkVunjydVA_YfIFGLxZY3qj_GaTBagYFChGkK739FQrLbVGfegZPRxvVTjRQgtxv_ov0eO8WwlvdkqlY-r_3y1QCXQ6GrxgaTlb8h3tZXR7Flt0THrJ4z4vQnDQdIlN7jpVb1NkMq2wT2RNRXdMbV49C_GwX75TQ_4fFXi3N70F-x7URXy2GcJ5LNAQ_suOUdPU0T9gFpDm4i6_LUaqafcK62dafuUOZULTeVXC1bGOkAc5nSJSDPKiXJ-BBOLMO2_ZcvRckf9Rr60T93wTZ07kPJujo_dcF8RIsWauoS6cn202ITQu3awfzLtk7jvNj6zTjL-9xkVUXOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=YQkyjKan_cr2NEq0xT6VTzmM8nrRHHAAkQC0xI6AqmTGvg-pADp2I8oy4JuBUzpgIt4PMV2q05lWRDZ4bYVW2KGPbmiLes0eaKHuQcF0e8Zf63hdwAfemKcaEehrwg87ZFeweYqwgnCM4kLgC1O7OifK9rzjpEq5ySyMJwXrjOHGk83ptHzYmxUpmUV1AB_W5HBibzvi8zZZ2O2AZO5drqEXPfjMpMbITGIHkQgpYmcfeIiMzVZZ8f_X18ksWxuVw98IoDhwTj3CB9nITaaf8QukS-zsgSi6Aw4QA6Auhp5fil8wsYwc5vXHcOyMuTEgc-nA6o_AsXiCaZxpgMfQaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=YQkyjKan_cr2NEq0xT6VTzmM8nrRHHAAkQC0xI6AqmTGvg-pADp2I8oy4JuBUzpgIt4PMV2q05lWRDZ4bYVW2KGPbmiLes0eaKHuQcF0e8Zf63hdwAfemKcaEehrwg87ZFeweYqwgnCM4kLgC1O7OifK9rzjpEq5ySyMJwXrjOHGk83ptHzYmxUpmUV1AB_W5HBibzvi8zZZ2O2AZO5drqEXPfjMpMbITGIHkQgpYmcfeIiMzVZZ8f_X18ksWxuVw98IoDhwTj3CB9nITaaf8QukS-zsgSi6Aw4QA6Auhp5fil8wsYwc5vXHcOyMuTEgc-nA6o_AsXiCaZxpgMfQaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل از اوایل صبح درحال بمباران شهر بندری صور در جنوب لبنان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/126535" target="_blank">📅 18:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126534">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8ZaeeFtcu7h12SkFNXKeZ-wdxEk-8KBPurPCIAREgEvxvewrusKCurlDONjiNODotGvVVH725d2A7dRJPlmcEOkH4g7I3LQzO9NmjaymiX06AnYFQI1bprzprk1o6bSq0pxPlLsI0y-OO_evgqlBz4JfBYIbhsfSauU1DwYmnOLnNrc97yT2TfrdbrZmfJu28SE1xwkGUd63AqRpVhIPOJDOH2KpTt8v-2o8tinIL-XkmkzrwsmIKgE-etry-f05FDBIAxdQ_QzTdo3CxWY-BFk99bYZ4corY1Juh9bERHJrBXjAwRwy0BfZCGP1VUwbT71-KucpoJynuxNTVDJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل به i24 :
🔴
حمله‌ای که به ایران انجام دادیم فقط مقدمه بود و برای یک حمله خیلی سنگین‌تر و گسترده‌تر آماده شده بودیم
🔴
تلاش ایران برای تحمیل معادلات جدید و تغییر شرایط موجود شکست می‌خوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/126534" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e18f9d77.mp4?token=bxuVm67HzUzflbz7VlPeaA-7_HbcCbJX7R0T_kkyzdsEkm2KH1KgpXTHo9q5EVyymo_STK3AhPNmhddaWclWVmzr0zl7twYM6CUsBzqDebPzWlilfGRNVEe5g9fFTbslZS6j7hhkECZGz7OeaUWSxOo18QRF_fuPKFGE_tLRSRYrCgxYaR4spb7yzsrn4rmB55105-ZDQZN5pz_kBX5ABbeosgbrvumOq0qOJhteuVvGAqitN0iN2DY9ya082ZlrIXk7LgNjQRzRjAkjT1qBTw36a8B9WjjgDGQZMfDbVUYnMTr6x08ekQoLRHbbuKUspWZiwsM5UOwRDncb5dnsBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e18f9d77.mp4?token=bxuVm67HzUzflbz7VlPeaA-7_HbcCbJX7R0T_kkyzdsEkm2KH1KgpXTHo9q5EVyymo_STK3AhPNmhddaWclWVmzr0zl7twYM6CUsBzqDebPzWlilfGRNVEe5g9fFTbslZS6j7hhkECZGz7OeaUWSxOo18QRF_fuPKFGE_tLRSRYrCgxYaR4spb7yzsrn4rmB55105-ZDQZN5pz_kBX5ABbeosgbrvumOq0qOJhteuVvGAqitN0iN2DY9ya082ZlrIXk7LgNjQRzRjAkjT1qBTw36a8B9WjjgDGQZMfDbVUYnMTr6x08ekQoLRHbbuKUspWZiwsM5UOwRDncb5dnsBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعضای طالبان در ملاء‌عام گوشی‌های هوشمند خودشون رو با چکش شکستن تا وفاداری خودشون  رو به رهبرشون که خواستار ممنوعیت گسترده‌تر گوشی‌های هوشمنده نشون بدن.
🔴
این در حالیه که طالبان تقریباً تمام حکومت خود را از طریق واتس‌اپ اداره می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/126533" target="_blank">📅 17:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da6cf7b2a.mp4?token=pDBQ24Xark0Dj6TCsDOw_yFWong9TB-R_oj4LlxMClr4GqJYihwhSUsHnKfEYZwAQFFnb3SAPau7_idI5smN1t7QaJj4Lzhzt8z9r3ixIvibsgaN8YpKrEdPOlpS5laFeQOstTDqXWCVrWrI4wC6favjTSvAC7vrUiaHpSb-Sk7csAkrHr99guM2GS1XdTmjM8Q3C4LDTvAokGZuNoqMHI8u6Rb2NzW1KttXzDKJBXO_EbyTs0SX7NcO-eVXSL4RNlVn40_GGdAvgswkOVLDiSDdHdUSyPGUH6-6z3Ksbb6yHLvkbEZiWZo7yn7SJJL8aKUBxm_aAEml3uZEMBrIuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da6cf7b2a.mp4?token=pDBQ24Xark0Dj6TCsDOw_yFWong9TB-R_oj4LlxMClr4GqJYihwhSUsHnKfEYZwAQFFnb3SAPau7_idI5smN1t7QaJj4Lzhzt8z9r3ixIvibsgaN8YpKrEdPOlpS5laFeQOstTDqXWCVrWrI4wC6favjTSvAC7vrUiaHpSb-Sk7csAkrHr99guM2GS1XdTmjM8Q3C4LDTvAokGZuNoqMHI8u6Rb2NzW1KttXzDKJBXO_EbyTs0SX7NcO-eVXSL4RNlVn40_GGdAvgswkOVLDiSDdHdUSyPGUH6-6z3Ksbb6yHLvkbEZiWZo7yn7SJJL8aKUBxm_aAEml3uZEMBrIuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به صور لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/126532" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
شبکه الحدث:
نبیه بری،رئیس پارلمان لبنان به سفیر آمریکا اطلاع داده است که جنبش امل و حزب‌الله آمادگی خود را برای برقراری آتش‌بس فراگیر اعلام کرده‌‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/126531" target="_blank">📅 17:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:
🔴
ما در حال بررسی این موضوع هستیم که آیا شلیک گلوله از سوی ایران باعث سقوط بالگرد آپاچی در نزدیکی تنگه هرمز در روز دوشنبه شده است یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/126530" target="_blank">📅 17:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126529">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شلیک مستقیم نیروهای طالبان به معترضان در شهر هرات
🔴
طالبان میگوید که اینها مردم نیستند و نیروهای تروریستی هستند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/126529" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126528">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a789mwh72weXBEl8ZQHfGM1I16b5KFs5Bz-dzxAK_bjEt9Gn7kgETTcJlNkRCo4sRmq4VKVFeW-Vh0xGNTncC1s6sE0gIA5tQz_PdoIfOKaA8nkQLDhqv8Yc--l9zOtnXbJwEm0WaJz-qjxd9wFkOTX0t3eXVC18-sZIwt0SLfdBuwyBx1DLEQpC1bn2u9y6W0HIuQ8Us0P7v5kzxQe4pQGzq6QJs6JWoGCT1YJ9EZ3nO5zBTAIPwnw-E_PCeyEyq7A2Ej2etBlVbxxWlduWssKAvMiCvQ-fthtnuWfClFri7QNHodz0kI_yU9wSDcwasqh14_S73bsW6kQYRZCIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلیا خانم ایران
۵ قلو زایید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126528" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126527">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126527" target="_blank">📅 16:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126526">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126526" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126525">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C6oNjj1nnppyGmWZhybHRw0z6iWIJO0yWKZB2_fhwSPvb5AMgALs8xA1sFekye_5UTDNYkZxm2IoRriae45v_Mw41w12tay8isfP1QgsZ7aBUrbvTfgFKzYEoocFRwNGFjsJd3ZQifywIgHrnEvyV5OJ3eZLtp3hIlB4267_Kve8b7_aHfUSrYB3AF7R4JTae887ImE9aReM7SKMAm6xjBVtPLDxZJa9irGN8VitbuygyxOel-odaPzKvkyuvOtTMX07mr4jYhWDkCY42CWKh3N2piwgdWip4z8VYgOpNDNvBq_cH1sh9TIdpDb-RySnFLH4LQWK3QXTCNTboVCehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خان میرزا بلاگر ایرانی در حمله اسرائیل به عراق کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126525" target="_blank">📅 16:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126524">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR55R6RIrmA8wUoyZxg4jue2m1zU2--6DY2Y_LLaf3saYnYVI0a1cC7IlaYb9TGFLlm6dy0oUWYksZIBul8PSai_zWmfeYlrQ4GcjogrsPN47uhUFL-eiJ4MNZUozJSbTGa-hgTogId31Q6jsepBjS_UP3gIo64j2WATFFk9IwbYu4KqR6Pzuo9Rw0aNgOSyS-sVmKHHOqaJxZhsOEhHrVbpskbzQj78sAq7i-K6pCjEIxPf6jzYE4PH4osRLbctMM1JatuWCxMJCkTyENqfs2auLf2Pc42ovhSmEiaeGqqvnZ1MNJRuVaYpKe2UNMPADE_YPKv6cilulZRY-nhFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126524" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126523">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu-HBinKNcpae9RBU4rslVbFzvdxPAXwZR6QDcoa6ovpk0cdLObXpfhfXPCtQvRsWOnWp2elNaIwkpDCKA_OhPwLxSZQAL31oj0ep2VxuFqV9nmrBrK8xJvAcioZ1L18mIkNigfTUaZX2579iBFzwqw5fc6MAEkA9TJ6VenaovjCDCEGUC-IFH-0kncYokT5EMQ8fi-I56G_HplVfbFjmQZldrJWl4UHcxAmor34GyjIRHxyDGNK5x7FdIUMQ-uXH22QK6OUn9nVWXpMwP79JOycP2g1qTEpreXmr9svEgjSVJchqGQzeRZaENI6HLPRsI0v6BOYV3LTsvOTcupEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / اسکای نیوز: ایران یه پیش‌نویس جدید برای آمریکا فرستاده و گزارش‌های اولیه نشون می‌ده طرف آمریکایی اون رو قابل قبول می‌دونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126523" target="_blank">📅 16:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
حزب‌الله ادعا می‌کند که با حمله پهپادی به ساختمانی در تلات الصلعة در شهر قنطرة در جنوب لبنان، یک نیروی اسرائیلی را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126522" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126521">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به شهر عین بعال در منطقه صور در جنوب لبنان هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126521" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126519">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaW-Hws7SD9TKgW1oibbeI2cqaYJg8MYEbc9E2vX2evyBWTEyoCNq4X7yAYEyEfyrsmjf4YFnKXFyYgZupOIaSDwoGQAb2MC-abVp4GlLpAfIdhqCMbEddXiT-7GfcJ2FYZTKSbLnTX2uVrztILBK2Z2r7hNjqWl-CW3oGNGb85x4Z2w_WuM5FQeqVivdnS2je4SOrFmv56ZKcytgSJRxC-h4eE4ZtNL2mvSSvvKioV-M2n_GVZpUStWZwdOvdbZvrw1Ivl-bwPln7D9xRE3p3NtvfxuF5m58pESWS5QY5d3h3y8u-xAnauJ6v3BNWBn9O8mqOlqWDx2KdIUxB_emA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه و عربستان برای بازسازی خط آهن مشهور حجاز به توافق رسیده‌اند
🔴
قرار است این مسیر ریلی به عمان و بنادر اقیانوسی نیز متصل شود تا به گونه‌ای برای دور زدن تنگه هرمز هم مورد استفاده قرار گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126519" target="_blank">📅 16:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126518">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزارت دفاع ایالات متحده ۴ شرکت چینی، علی‌بابا (پلتفرم تجارت الکترونیک)، بایدو (گوگل چین)، بی‌وای‌دی (تولیدکننده خودرو) و نیو (تولیدکننده خودرو) را به فهرستی از شرکت‌هایی که گمان می‌رود با ارتش چین همکاری می‌کنند، اضافه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/126518" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126517">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urjz2ho2LbimJNi77Rz0ivogBS-yjiNBCkV1WCsSuriFIH_jL6fyqp6tZaQcxsX-Udvcc-iMofWu6z0rFMWIXhyiaSmjxsuP8VQiGCnwNYDbSMlK0UlvCQm21RO493wUg_ytYrNWZCpal2MMcxQA2Z6p6-IPBuSlfud4WDdivZE8fKbVTNkUatMiJnZqyGMc0JXRzT-OvzLRZmjQh0MR1kdrcr4lYGZutsWS527XQ2G3v3jV4Xasa13noK5rD0LqMQ1lq2y4IbEoZK50ah_TiOSHNPJLtKjfRJ_7vA4DVjQRNfF1dbKTbQcYLnuBolQvjnZOhJdj3PqbSHxum2WcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عدالت اداری شکایت برخی مسولین تندرو بر علیه رئیس جمهور جهت تشکیل ستاد راهبردی فضای مجازی و آزادسازی اینترنت توسط وزارت ارتباطات رو رد کرد و به نفع دولت و ستاد راهبردی فضای مجازی رای داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126517" target="_blank">📅 16:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QZ_bqrGMAKoa5oEq3RbYTy8zBsZkFNEt3b9c9A7OQn9YPsa56yk0glBJnitHMW4vyxECcN5K5zieYQFc1tqtUVS9DVxhF0ZIjjHi2sLJSZRL5VDrT5-kNEautLWPzNHoAxV9OMISn8onBodARQdiji_u4XQP2JsJKxT581GT9MmXUIBxikbNU8rFKNj-IcxLqGlAoB2JA04jt-I2am4yirM1tOwauMVTtkuLO066A4Ew60iCj7QsSfVkTsnWp1w7GxB9UcSRVwkp6D44lhjuyCqZFNMKlX6DK9TmDW4s-yBI3gEOoJJ4EE75vxnPDm1pCBLD5odvfY9aUcdKDSbxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BfRpcIc99y8Ml0NZLgEHhTLMa9ccI_GmbBobq-5tZPweb6kyjKa56GHrpUq0LZpxxUkdMZ64qj8v66zE0mW-nVXtEEBNmUwrZMVVs-fq3xDGfbI7PFeu9qTorcxF28J_5DhhuCNEBRCgBimnIgym484uvTeOew0gmJ472xXCELVXfnzL_zNy_K474agvS4ERQf-eeVo8vb6O5bKP-mEdUwA-xcnRp_1FMiPHwU335Adwy8zNI8HSPbMaOa3g6gUteywQzzQbeCZYxmrSeCEFXB-ZVg2eD5z7yz-TIsnv0nvEFO2X3CPPYRwOx03Xr_ipi64sTkq-7uvnPeypIb6Myw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا امارات صادرات روزانه ۱.۵ تا ۲ میلیون بشکه نفت خود از طریق انتقال کشتی به کشتی که نیمی از آن در لنگرگاه صحار عمان انجام می‌شود را از سر گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126515" target="_blank">📅 16:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بر اساس نامه شرکت مخابرات ایران به سازمان بورس، این شرکت مجوز افزایش ۴۵ درصدی حق اشتراک (آبونمان) تلفن ثابت را از ابتدای خرداد ۱۴۰۵ دریافت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126514" target="_blank">📅 16:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE-5IsfXj2f9WFSYBYjIorOdDgladtuj6NC24_ERr3Jo909X1RgZtibVnldr6EAWnXMqYNPMN51VgdKz3kwKuC9PEpE4gpgpt5mmglT2t8Kb6_wjdVzvPPdZRKDj1T0ncphoqDDUQIRv4PKnzHfDPNry6E1EvjqOsazAvphkUZAhFfwItOXwbnXaZv9cM42sd9-6PGNxC034iszTg7Rxp-Uc2NrZlD-lbKdwKXbLbyWZu7gHQiuuEwct5R83EZJM8P1IhrPBHCp_XIifdMICeytBDhMSENi8O5HKbiHk5bWZbDqiifsSGEznj3rYeFGXPPxFrNpxXUrOJpAhlTq9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا کاهش بیشتری یافته و به زیر ۹۰ دلار در هر بشکه سقوط کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/126513" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2vD-cbY20LbkO-Wb-zO0UHOUi5mK8dTtBrvxvH7jeqMOf6JgcIK0HC1XC6Bqm5Xb2GQSmfPQaFgXT6KwmZTIzn18Uxw0T4C4NFgzeruUGsJqYXeOHh5Ov-I_-43r71Um0A5T6khEFdtwP7poh_-Di0zUYsE2dRkg26ZZpZDrdjeMoFf1E9STAGVoWBcJiGByjqm19sCz8ImlxeJgjgDj4i5OynHkwyHEcqGZmD4vODjA4wyT2OlgJbcXQqITUQKggl80eefrGtzHfbnCZGgX70ah9Mj4MwgV50FAwxBq1yQj0f2ZOdmR-MJSbG5LV9NgdpstZURBjBcTRsZOlUmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز مدعی شد، یک شناور سطحی بدون سرنشین نیروی دریایی ایالات متحده (USV) که توسط گروه ویژه ۵۹ اداره می‌شود، پس از سقوط یک بالگرد تهاجمی AH-64 آپاچی ارتش ایالات متحده در تنگه هرمز، به نجات دو خدمه کمک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126512" target="_blank">📅 16:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
به گفته اسرائیل ارتش، یک فرد مسلح که از لبنان به خاک اسرائیل نفوذ کرده و در منطقه رامیم ریج به سمت نیروهای اسرائیلی آتش گشوده بود، به ضرب گلوله کشته شد.
🔴
ارتش اسرائیل می‌گوید در این حادثه هیچ مجروحی نداشته است و نیروها در حال بررسی منطقه برای یافتن مهاجمان احتمالی دیگر هستند. یک پهپاد نیروی هوایی اسرائیل نیز برای کمک به جستجوها به منطقه اعزام شده است.
🔴
به ساکنان جوامع مرزی میسگاو آم، مارگالیوت و منارا در منطقه جلیله پنهندل دستور داده شده است که تا اطلاع ثانوی در خانه‌های خود بمانند و یک بزرگراه در نزدیکی آن به روی ترافیک بسته شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126511" target="_blank">📅 16:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-wIfqIy9l7hQqttKo25mt_E3eufz7GWKW7MLrbMkgbd_W3p93MMG90cyrtjNtRQ_yOQRP52aI_Iv1iW6nir3SVZzAT6Kr5IVcy1CUE5uJlknxOIAreZXPpQF7dXqGXiOkHNfIYCAxvV4JjiONNRnRyWTgTEH7F-d7Az9sedN8s7ipfvleLfXW4hoyVY2E6hAJOYefjQKetASd7uPpUQtq6xj0XC7xJinkjQKqz6_LVFG6jZOz9U-WuUo-OyR1DpaGYkErVt5Si72hZw2QmEW3WQ9-1F21IBiqFDzxn_aCYAjMRBLl7nxRZNTJ0wPAw5OPIeVPWtpqs_AxCMEenw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEcTAovwx2IPu7yZEQ9T-RWzQCIJGjPxqOECwO-zR_YRcJ0Qz5wDZDip02B10mQMEmVmsO1igppFyYOR3jZstqjOH9HM6phd22xYAU5hHH895p9vnh0Qsha_aIMFDbChTbdS49TG56y_RGimT23ZgFkZ90os50hqL0VZeoKpAl4iz57JdZqyi9W7TSsivUHPHbyJYNkeLsB08yQ3Zbc43dck5TSzT4TAkifUI0i3zh5hTQ_wY_iw2hjhBscy3wdO0M4Uphlcmy5UibAl5KoEH-R9qJfjCNjILM4ouK18nmh4nY7PPwuFdHLtPdEJfy_21vszF_aNYW-wieBmXcoJsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
زبان ترکی به سوپر اپلیکیشن بله اضافه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126509" target="_blank">📅 15:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر خارجه بریتانیا: با عراقچی صحبت کردم و به او گفتم که از سرگیری درگیری به نفع هیچ‌کس نیست
🔴
از اعلام توقف حملات متقابل ایران و اسرائیل استقبال می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/126508" target="_blank">📅 15:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126504">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmcDRzGep6wbX2QfCjqD4XSIr3WIJRgikDzQWK8sR9cqbK6utRNiG4z4vK0u4wCGPaMJbaMyd2-Jsg2zV87PhEpeyxQ2g8rsb1R_SmljE9rDMUDVwhXtJJ0FZIKE-pVd_xl4UnSB05d33eh1AYh1rs0r3QJRTNtizcX3eryBH1PW4pO0Dv7yyqa0qb3sL4vIvtstCBMkkec2TFKT7Fk5MCruybBrh0rPe3ecBUxE9jfMHeko9D_sVTMOrnXbneNTgJavZc1lVL6zgPDmOixkHAVoSFWPijeZpNNua5DBrGT88GC8V9d8faS_LF0I_TaI8sgDVgoZxq1GYiexAXGVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-SATOAunGhpERV1rR9MUe3_2VZZSYa8E-DbbviPtM2Dyk2IATTAxmoyW8JGdRsugCWh6b-2CCGemy_wO5DJih0FW-OL4G5LCiuxQqEvZYYtoaWMFgXiGo753v9SGjqA8dFk31mSLJg1uz_jwSf8X45kXe3zORWu8REzLYxp4oRPHuqIFJqwGMjgK8A-C1xOSupgTAu1HLRV6qYLS1fwToNjOUzw-Hr4NqMxdwcm0toH3QQetfGBPCC13tFvc7GoE2yEUcHtDCTohx5vjpXdtJO7SOV7tW1-lN18RbT01vFUzKmsYjadwIcdzpELe4g-GXPvBagM0EvXIx0yFIxVOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=KJr_KuZAONYR-FhbqJuoUe2Ob7mf7XGL_3QETLrw-nH-LzYaMd1wsuTdVZUnR8zY85CJRhcd0FcHHk4NDTQcRqxakSx2T2jqGMO8-d-IPOZSHoJT_G9ylkWl7EQFhD4LXaiyNscS2CkymHa4w5HmERLmOyiL7dhXafZ1cDrEe22CB9x-7IjlwembzvCuWp2F9XV2j85vX-8d6f3yuZqa3EKGHheTiywP4yXnA0TVlHoXsBVENg03M1dru7PPpD2rkbMrCNA_Vz84ZgOEmeWzGt8XD7RcfA3VW_YgH4wOnu5BOyzw6h6rn0I6VnlxRNQ0bUITycfqDEXAtzVusTvmnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=KJr_KuZAONYR-FhbqJuoUe2Ob7mf7XGL_3QETLrw-nH-LzYaMd1wsuTdVZUnR8zY85CJRhcd0FcHHk4NDTQcRqxakSx2T2jqGMO8-d-IPOZSHoJT_G9ylkWl7EQFhD4LXaiyNscS2CkymHa4w5HmERLmOyiL7dhXafZ1cDrEe22CB9x-7IjlwembzvCuWp2F9XV2j85vX-8d6f3yuZqa3EKGHheTiywP4yXnA0TVlHoXsBVENg03M1dru7PPpD2rkbMrCNA_Vz84ZgOEmeWzGt8XD7RcfA3VW_YgH4wOnu5BOyzw6h6rn0I6VnlxRNQ0bUITycfqDEXAtzVusTvmnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی امروز چندین حمله هوایی به صیدا در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126504" target="_blank">📅 15:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126503">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز بلافاصله پس از امضا باز خواهد شد، که ممکن است در دو یا سه روز آینده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126503" target="_blank">📅 15:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126502">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سفیر اسرائیل در آمریکا: می‌خواهیم جنگ را طوری پایان دهیم که تضمین شود ایران برنامه تسلیحات هسته‌ای یا موشکی و حمایت از نیروهای نیابتی خود در منطقه، از جمله حماس و حزب‌الله را متوقف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/126502" target="_blank">📅 15:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126501">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله هوایی اسرائیل به شهر نبطیه الفوقا در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126501" target="_blank">📅 15:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126500">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
پاریس:  ورود بتسالل اسموتریچ، وزیر دارایی اسرائیل، و ۴ نفر از رهبران سازمان‌های شهرک‌نشینان و ۲۱ شهرک‌نشین به فرانسه ممنوع اعلام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126500" target="_blank">📅 15:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126499">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی شد دو فرمانده ارشد وابسته به جنبش جهاد اسلامی فلسطین را در حمله‌ای هوایی در جنوب غزه هدف قرار داده و عملیات موفقیت آمیز بوده است.
🔴
در این حمله «ایاد محمد عبدالعزیز نفل»، از فرماندهان نیروهای نخبه جهاد اسلامی، و «احمد معروف»، رئیس یک هسته عملیاتی مسئول اجرای حملات راکتی علیه اسرائیل، ترور شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126499" target="_blank">📅 15:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126497">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bj8xLqqdp40YnyZf7NwWZvJd0kXM5MUrkG7GIC7vpOdEYXfhJVnM5ATVhtMac3AO52Xy8-ESUsxUNM9hT9Bolu37L_TR9ZmE2R9KipjBsq9z9YBoBmhZZ5lORjh0mZBGSwf7cZsFrU3YT3ugIniEXi3rPpuCUsfRVoy00jSdk1KBr2RGtoKEN-X02u0GC6__V9vvRiFmJKofkY7X1KriHg-X6S2QTbw5oR7ouE2O8RjxfEbicVpfofiAGAFfzUbCpFgoMSIlx3Jc95yZas3rqoiz5bArmda7lru6zGPaSGjIj63jRh0-xnvfhZfmVfVgCip4sc-lRk_j6O3CIrcUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjgcpfEsrL3IQF80Ne1ZIKxIqrtSkgWMPm2TvyGGmpDysY0ge-5VEYJlqlC84DOPb4eDPDSpiF5sqrCQSNBhkT9ZIEgG3VHlpA2fAJovRCmgKGg7b91GH34eOHqh0jCPRb4W3HXX8-G2YSiLzONhBeFoC9UdzGyboyoQrxQ3bPJGUpOriDf64V3fhcWGKrSn1FHKkb8j0eXNsKXh82X_DxwG_WxHuReGwrDqcChHFzNzo1ML4alj250TQXEF8uASUy-crLiWbHFz--zabhLmdzY79os0X4Lq0GTiRKYqXJFYSNjV5oiJctABu1E2DqwHjGOaEJqCYSiqELHjAsprEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملهِ هوایی به شهر کوثریه الرز جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/126497" target="_blank">📅 15:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126496">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل : شورای وزارتی کوچیک تصمیم گرفته هر موشکی از لبنان سمت اسرائیل شلیک بشه، جوابش با حمله به بیروت داده بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126496" target="_blank">📅 14:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126495">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اسرائیل هیوم: مارکو روبیو نقش کلیدی در متقاعد کردن ترامپ برای حمایت از حمله اسرائیل به ایران پس از حمله موشکی تهران ایفا کرد.
🔴
بر اساس منابع اسرائیلی و آمریکایی، روبیو از استدلال اسرائیل حمایت کرد که عدم پاسخ دادن به ایران برتری می‌دهد و تشویق به حملات بیشتر می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/126495" target="_blank">📅 14:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126494">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نماینده ایران در آژانس بین‌المللی انرژی اتمی: تجاوزات و تهدیدهای مداوم که شرایط استثنایی فعلی را ایجاد کرده‌اند، متوقف نشده‌اند
تلاش‌های آمریکا در شورای حکام آژانس بین‌المللی انرژی اتمی الگویی برای توجیه تجاوز بیشتر علیه کشورمان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/126494" target="_blank">📅 14:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126493">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e8515ff.mp4?token=H4HBaj51jiFEgfHAWAP0svHBf2ubW8-H7JmwTNNPiPtqvcFfN68Ps5yshljCvtt3efFbF9Ll0Rmz7ZNyTNpNUggBv9eI6HQcdlWfguACDJzgkGjbWhYFST5TKl_MmNWqFeuf15wsgg9tiNgrE_cGAcn2N07elf0MYdEXqSEL6sEY6BDXBTK2UM8rSaOjGJ0zy89a3PtJk8FGlpiBfacEFmfhOFKtXFr-C3k1Xk2I3rcGuKUko5nCkDYgclzn6zzNpy50HN92StHS-Yg3_8i8NCY3UIA_q1XNBYh4gG1h1bBsbOy_G9P3AKqXEiB9SjEaHTpw17G71742132kDJXpWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e8515ff.mp4?token=H4HBaj51jiFEgfHAWAP0svHBf2ubW8-H7JmwTNNPiPtqvcFfN68Ps5yshljCvtt3efFbF9Ll0Rmz7ZNyTNpNUggBv9eI6HQcdlWfguACDJzgkGjbWhYFST5TKl_MmNWqFeuf15wsgg9tiNgrE_cGAcn2N07elf0MYdEXqSEL6sEY6BDXBTK2UM8rSaOjGJ0zy89a3PtJk8FGlpiBfacEFmfhOFKtXFr-C3k1Xk2I3rcGuKUko5nCkDYgclzn6zzNpy50HN92StHS-Yg3_8i8NCY3UIA_q1XNBYh4gG1h1bBsbOy_G9P3AKqXEiB9SjEaHTpw17G71742132kDJXpWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس
:
خود آمریکایی‌ها تو مذاکرات غیرمستقیم به ما گفتن حرف‌های ترامپ رو جدی نگیرید
🔴
اون چیزی که از طرف آمریکایی‌ها تو مذاکره‌ها به ما می‌رسه با حرف‌هایی که علنی می‌زنن فرق داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/126493" target="_blank">📅 14:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126492">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucSCLoVOX3zpXgNSoBB40T8vxm9VFfwdsWt6SlHrlRF8wR7LPKiQ-Qy1k2UK0qI3hoaitmtpXbh9szaD3TWEEcLgx0KvZbV6OvYhlodh_2Mpj_WaOudWFcBHmUa2JtyW9daUa0kQvS8y7RX5_9UuvO24MWFk06vfrmlgt6dx3-l_NNQOo6Zl535-kPSe3Hx7J3NtYQs8pL2jW_TQn1A3pPo-YacokwrIUxFeQPzKIc6ZyN2ZMAz1OxFDfWEHgxxHIjtN4OwhYTZmPFQ7ogKZB4mwGb6d7n70dj3DEDrV9RDgMThoD8an4kQQ_SstawiTILBDA-YAviPIHQviGt0lgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش بلومبرگ، سقوط قیمت بیت‌کوین به زیر $۶۰,۰۰۰$ دلار در روز جمعه گذشته، بدترین عملکرد هفتگی این رمزارز را از زمان بحران و فروپاشی صرافی FTX (متعلق به سم بنکمن-فرید) در سال ۲۰۲۲ رقم زده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/126492" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126491">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ادعای یک منبع پاکستانی به شبکه العربیه: اسلام‌آباد در حال انجام تماس‌ها و رایزنی‌هایی با همه طرف‌هاست تا در همین هفته به یک تفاهم دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/126491" target="_blank">📅 14:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126490">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کانال ۱۲ عبری، به نقل از یک منبع امنیتی:
ما وارد مرحله «دورهای مکرر» با ایران شده‌ایم. ارزیابی‌ها حاکی از آن است که تشدید اخیر، رویارویی نهایی با ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/126490" target="_blank">📅 14:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126489">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
حمله به نیروهای امنیتی پاکستان ۱۴ کشته بر جای گذاشت/ ۷ نفر ربوده شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/126489" target="_blank">📅 14:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126488">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKW-hevoM5-_cT3ihVTr4g0_lZ41YR56bva9jR6JGoC1wxtnVizx7_wkJLPogQ9flf83tq_f6AaesafgxYVcn0MUZpm-n5QfZ4jyWqzg8owk8GHVZCuI6jEU8nco4Tgxgq2wCRx5ME3Y3RGib1OqzWGaFCzOJMu0aL73j8_u3OBjDQpufTG4UmXuLgK0Vp_s6FMGqpVd6h7uPM00CSkuxv-YkteyPCdHID0Rr3nYE_dqH3_ljPlySgCq7xuGq6rLBHUA-L7icWSLN_IWa0199YjpHHlcLUATJOStbXWnrNadDZt1-O6OQfEFNLJVp5x07Yb6vt8KZCtLYmaLgs5k5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش اکونومیست، ایران و اسرائیل که برای دهه‌ها درگیر جنگی پنهان با تابوی حملات مستقیم بودند، اکنون آماده‌اند تا با شکستن این مرزها، خطر یک درگیری تمام‌عیار را به جان بخرند؛ وضعیتی که دونالد ترامپ را در برابر یک دوراهی دشوار قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/126488" target="_blank">📅 14:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126487">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: ما دو خدمه یک بالگرد آپاچی را پس از سقوط آن در نزدیکی سواحل عمان در حین گشت‌زنی نجات دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126487" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126486">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کرملین: میانجیگری آمریکا در مورد اوکراین در حال حاضر متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126486" target="_blank">📅 13:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126485">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c08628adf6.mp4?token=j0xlu02Tiv-aaaQZCSNV5-tjbjMywHg3j_cA_au78qwoafnzado32w8q7H7IZ9L2lBYdxttrVVAxq7_zToeNONTRp60QtWCXjYMX0NvZT08HfKo0Gc6GK7ix7GH46DIurT_mi-shKbMnawHtL6r44IgkZZuYWFTLb5SdnhyxlyoavRr0TAyb_N-nnoIRpWCB5RGb3y-BgJnWEguEquPWIeK9kkY4HxXwwSghcLDRjlRr1P_h1amm4MIeqLLjKCPfVcjR2fIQZVKji2TFGhG0E73D-GqTDLXFagKsEP_daqxLwh-n4AeThl2ED91XSisSbQTrh3YRyJduYokNv-1HHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c08628adf6.mp4?token=j0xlu02Tiv-aaaQZCSNV5-tjbjMywHg3j_cA_au78qwoafnzado32w8q7H7IZ9L2lBYdxttrVVAxq7_zToeNONTRp60QtWCXjYMX0NvZT08HfKo0Gc6GK7ix7GH46DIurT_mi-shKbMnawHtL6r44IgkZZuYWFTLb5SdnhyxlyoavRr0TAyb_N-nnoIRpWCB5RGb3y-BgJnWEguEquPWIeK9kkY4HxXwwSghcLDRjlRr1P_h1amm4MIeqLLjKCPfVcjR2fIQZVKji2TFGhG0E73D-GqTDLXFagKsEP_daqxLwh-n4AeThl2ED91XSisSbQTrh3YRyJduYokNv-1HHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار خودروی بمب‌گذاری شده در مسکو
🔴
یک نظامی عالی‌رتبه ارتش روسیه در انفجار خودروی بمب گذاری شده در مسکو ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126485" target="_blank">📅 13:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126484">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dcf528f85.mp4?token=AFpwJpR2ql0N4gmZflBl09RJQ-oYFNouypLsDay0e85yOhsEes4LedhDThVeRNU6OAth5NgJAmec2vD3yAemiZRacDHs5cG1o2axRPGL44sV-Q9RfSprJy6pQ3Nq4RMylVnQf0Uu88o-oA8DMMCUAsITwfmjqmJefHBagkU1RCOM89MwQ8aJiW22jpUEFRYWYdPjgDT_fGzhjaBFYP-TBCQs2GBi3dDjtObJI9EMGIEl89Ryo5iXiR057IhRSJ8zBtzCDh43otStt2rKBVLfM0KUAUidtOi1zT7EayQFyFZo1QS7TCXRowb4q7KeZ6EyrAlkKzptb8PPlyQ5pfecE5PpgE2q9OVH5deVha1kLY7tc4FXpeVwcLB5X2SYci0ZJyWMAg6OjAss6z2xFONe4HCg74TrdIh0yCbgcUDr31XmONRG6kB5KVFfIP4ZtEkXQy4a98Ek7FEhMRrfX7tTfapdR1viPuN3uKJc8olgaGgnWdZvG072PcDbh3YATY4Ku1qw7fbGPN5HxH4lK3137BOBG67TIg5zTqqQ62u7CMqrp7V9eOkOmh34OPeV0YzjRf8VNFoJ6MJyhx0CJnIsHnHxfnQDQWyEAQda1uCZV-oKsyBw1aJmbRpEif7dt0cdaSc6UnXSaxi8c17HDcetD5n6Pe7hMjgsWeGDWvF9uEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dcf528f85.mp4?token=AFpwJpR2ql0N4gmZflBl09RJQ-oYFNouypLsDay0e85yOhsEes4LedhDThVeRNU6OAth5NgJAmec2vD3yAemiZRacDHs5cG1o2axRPGL44sV-Q9RfSprJy6pQ3Nq4RMylVnQf0Uu88o-oA8DMMCUAsITwfmjqmJefHBagkU1RCOM89MwQ8aJiW22jpUEFRYWYdPjgDT_fGzhjaBFYP-TBCQs2GBi3dDjtObJI9EMGIEl89Ryo5iXiR057IhRSJ8zBtzCDh43otStt2rKBVLfM0KUAUidtOi1zT7EayQFyFZo1QS7TCXRowb4q7KeZ6EyrAlkKzptb8PPlyQ5pfecE5PpgE2q9OVH5deVha1kLY7tc4FXpeVwcLB5X2SYci0ZJyWMAg6OjAss6z2xFONe4HCg74TrdIh0yCbgcUDr31XmONRG6kB5KVFfIP4ZtEkXQy4a98Ek7FEhMRrfX7tTfapdR1viPuN3uKJc8olgaGgnWdZvG072PcDbh3YATY4Ku1qw7fbGPN5HxH4lK3137BOBG67TIg5zTqqQ62u7CMqrp7V9eOkOmh34OPeV0YzjRf8VNFoJ6MJyhx0CJnIsHnHxfnQDQWyEAQda1uCZV-oKsyBw1aJmbRpEif7dt0cdaSc6UnXSaxi8c17HDcetD5n6Pe7hMjgsWeGDWvF9uEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات: پزشکیان، عارف و من نظرمان این است که وضعیت حکمرانی در فضای مجازی مناسب نیست
🔴
ستاد ویژه ساماندهی و راهبری فضای مجازی با قوت به کار خود ادامه می دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126484" target="_blank">📅 13:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126483">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پروازهای فرودگاه هاشمی‌نژاد مشهد به روال عادی بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/126483" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126482">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa05669d1.mp4?token=RPYiTikBzntG8nj7qzVSkRpNMYn6Mq7EE7dt_Ty40FkPAHmW8GgGEBxSG7owlaC5MXJAuhpbOQ21Xmw0hNQqU5LJb-u9tw5Kmb3AvtAJ8nvVqxjd5cVXtMez6RDixMelPF5msAVfSv_WoJd-6KDhxsk44uuk8rjQIwX78UhO66qkkDzRrQdBk0hZY4vKXgYWuEnr2Uvtv50i3HEDJkmv_JMIjHUDZfhJqKwVA33C_LgPPud348gQMzMHYm-1y-y92kwC5XqAC1ebletY_shSg0jV8D6EQYPfeaRvTgAub0zAykJQ4PplLMzdrCzXUetMw8XHnSR-2bwjLBGkOblAsbbt3kqR_uir3eUWg_3tFa5Ub3mGGMXUZtmLyBTPm9vn9l-7UvA82V9QutpIQZvp13NcVLOYAQ29BZVcOTDztx3Cc0-BWtNjvnGv4RmjR5GpfsZar2h45G0eRa8Z-RX9PeFoc19Yi5c73GyRvXTRfbr-46sU9n66W8ujyH4qJibzMy9iGjYizO8ORkqYB18jI5QBfFwap0o57YktIFE8AzyrrJyy391cYgK4aoey_6Iuyfz6f1l2S2bEATmX8tT7SzW_ejJ7WKdetw2Mv6P-y9QKCfS9V4GTXtx5twikQxRUmWycG_iwiew5g2RahPac8mlTzpC1R0H_6RC757hFtcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa05669d1.mp4?token=RPYiTikBzntG8nj7qzVSkRpNMYn6Mq7EE7dt_Ty40FkPAHmW8GgGEBxSG7owlaC5MXJAuhpbOQ21Xmw0hNQqU5LJb-u9tw5Kmb3AvtAJ8nvVqxjd5cVXtMez6RDixMelPF5msAVfSv_WoJd-6KDhxsk44uuk8rjQIwX78UhO66qkkDzRrQdBk0hZY4vKXgYWuEnr2Uvtv50i3HEDJkmv_JMIjHUDZfhJqKwVA33C_LgPPud348gQMzMHYm-1y-y92kwC5XqAC1ebletY_shSg0jV8D6EQYPfeaRvTgAub0zAykJQ4PplLMzdrCzXUetMw8XHnSR-2bwjLBGkOblAsbbt3kqR_uir3eUWg_3tFa5Ub3mGGMXUZtmLyBTPm9vn9l-7UvA82V9QutpIQZvp13NcVLOYAQ29BZVcOTDztx3Cc0-BWtNjvnGv4RmjR5GpfsZar2h45G0eRa8Z-RX9PeFoc19Yi5c73GyRvXTRfbr-46sU9n66W8ujyH4qJibzMy9iGjYizO8ORkqYB18jI5QBfFwap0o57YktIFE8AzyrrJyy391cYgK4aoey_6Iuyfz6f1l2S2bEATmX8tT7SzW_ejJ7WKdetw2Mv6P-y9QKCfS9V4GTXtx5twikQxRUmWycG_iwiew5g2RahPac8mlTzpC1R0H_6RC757hFtcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل به شهر ساحلی جنوبی صور حمله کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126482" target="_blank">📅 13:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126481">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooz8qw9g9T0wu1mV904PVqvG6_zFUUuIAMr3RgAo30HPnkLDdEJlPnCq-guqjmJMhZUZ7Y0bS6XOWa_Gufod_kBR48lT2MzUj1UWEz_oPZEiO-49Tig_C-HrS1mxEx5dWVtGFl5lrB6Ys99Dn2ENrcX7rtj0qVbi_E1beoNlrIzk4Inm25pDbraURWU3X9luMwpRP8CeEB_xH6nOU8HNU5fSqc8I5s3bPwn5DWf6GvuKcDGKbCtr88Az7ohxh8Ky41pk1Yt1KKxP9APyVcZQznR79ZfEv5kaxqlE7GDeTfAomxKALSpFSwTs2rt35IU4eHAT55lek1RuIYC_Eqq1zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۲.۱۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126481" target="_blank">📅 13:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126480">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نیروهای اسرائیلی در یک بازرسی نزدیک اورشلیم، هشت عرب از یهودیه و سامریه را که در دیوار دوجداره یک خودروی تجاری پنهان شده بودند، کشف کردند. راننده تلاش کرد فرار کند، اما پس از تعقیبی کوتاه دستگیر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126480" target="_blank">📅 13:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126479">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
به گزارش تسنیم دو عضو از یگان‌های پدافند هوایی روز گذشته در حمله اسرائیل کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126479" target="_blank">📅 13:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126478">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
زلنسکی، رئیس جمهور اوکراین :
- روسیه جنگ رو نمی‌بازه، ولی هر روز داره کم‌کم ابتکار عمل رو از دست می‌ده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126478" target="_blank">📅 13:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126477" target="_blank">📅 13:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
یک شاهد عینی اعتراضات روز سه‌شنبه در هرات به افغانستان اینترنشنال گفت که یک کشته و دست‌کم ۲۲ زخمی را از نزدیک مشاهده کرده است.
🔴
منابع محلی دیگر نیز زخمی شدن شماری از شهروندان و احتمال کشته شدن یک نفر را تأیید کرده‌اند. با این حال، تاکنون آمار دقیقی از شمار قربانیان در دست نیست.
🔴
اعتراضات روز سه‌شنبه در منطقه جبرئیل هرات در واکنش به موج بازداشت زنان از سوی طالبان آغاز شد. به گفته شاهدان و منابع محلی، نیروهای طا/لبان برای متفرق کردن معترضان به سوی مردم شلیک کردند و تجمعات اعتراضی را سرکوب کردند.
🔴
منابع همچنین گفته‌اند که طالبان شماری از معترضان را بازداشت کرده و برای بازداشت زخمی‌ها و معترضان به شفاخانه‌ها مراجعه کرده‌اند. به گفته منابع محلی، طالبان همزمان نیروهای بیشتری را در منطقه جبرئیل مستقر کرده‌اند و فضای شهر به‌شدت امنیتی و نظامی شده است.
🔴
طالبان تاکنون به‌طور رسمی درباره این رویدادها اظهار نظر نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126476" target="_blank">📅 13:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ به بی‌بی‌سی: اگر به نتانیاهو بگویم کاری انجام دهد، او انجام می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/126475" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تنکرترکرز: نفت‌کشی که در ۱۵ مایل دریایی سواحل عمان دچار آتش‌سوزی شد، با شلیک جنگنده F-18 آمریکا از کار افتاده است؛ موضوعی که سنتکام نیز در بیانیه‌ای به آن اشاره کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/126474" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی دولت: ایران و لبنان نه نیروهای نیابتی یکدیگر هستند، نه برای هم می‌جنگند، بلکه دشمنی مشترک دارند
🔴
تیم دیپلماسی ما متشکل از افرادی است که به شدت به میدان آگاهی دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/126473" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI-h6Rl9oI0Ii5Sr7mkQD3s_l7Zif87Smtb8GsSRd1caaoNd6F-tG3UPwofxTbFytIIfgfs5ggu7STbwpGMS3xDBzYZBg5dHJ5dtUQlniKqRW912ALoC0jkbhGwFIMw8yCD673D79hernEC-ilzNuxfHD4kbeOMa-KPjh3Wlr0afLsjJjloKOZmnbjZv7lHSJo6JEDdVFzmRqN3_jNBeZTZ71dCkJoYqYJAdBWLRm-z34c4HoM2PluTaaphk_XOJ4hf10QRpPkUg6O5QH6ZihLLd8k658orzQbbtmIjRMItxKkkfUyvxzcGmqJBSuWtxmu0m4190bWFvHpr9KHNKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش بیش از 114 هزار واحدی به 4 میلیون و 540 هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/126472" target="_blank">📅 12:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Itjd8xxnoQrCKCoRf6_ER2Fsun4vdMGVR8ThHkHZ8q2kehGCTcxraKdzS7amAxJDGDTo_DQAZ5xr8OKFOix6tviCsidIMCCFxAQSQQfDJ_BdC5abQK9ShD5qLG4k4WfxCWSK9rL00HgZngaJoxrlAFcBjTkdFYmzSPRgjoDy65clBFPsy0-yyYheCkDJoFSZDWkgmhfP3f7-zX_8wPArD3Y0Zc0TmyXwEnqAl0oCa6fhlbQEtbvErznEKoe7w6243a9YMkWCAYrBafXyn6UadVttlvxQPvJPT9LSsmV_N0eGkdQD4aDrlO1bsH0J1IhST3dO515MD_NTv5KX1pELJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: فکر نمیکنم حالا حالاها جنگ بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/126471" target="_blank">📅 12:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر ارتباطات: شبکه داخلی ما با قطعی طولانی‌مدت اینترنت، آسیب‌پذیر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/126470" target="_blank">📅 12:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
یوتیوب رفع فیلتر می‌شود
🔴
مصطفی پوردهقان، نماینده مجلس:
وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/126469" target="_blank">📅 12:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126468">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر ارتباطات: خسارات وارده به وزارت ارتباطات ۶۸ همت برآورد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/126468" target="_blank">📅 12:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126467">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر ارتباطات: دنیا دنیای هوش مصنوعی است و ما مانده‌ایم ارتباطمان برقرار باشد یا نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126467" target="_blank">📅 12:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126466">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/8d88eccc6f.mp4?token=h0P-zXuDva-UoSv1gbeBINAyEWTsWYP7DSeAj5Xmpv80LARn0_uOvkfvVMPAkJ4y8u5gXv0aGidGOVA6a85L3JijurcdB1HVor9LE41KpV07x_xa_cT56WOHdZwR3eODEHz-oDdxGlGQMSUqYZr9QzTyuZTweExES9rDetQ49318Ets3aoAxPAPnFSujUV8of9xDeIj32UBl_e2N4m1Lf1yThu0m80pTlfLKdxeZDVWItvGdLTVSYq1Bbq9TlrIlhijlwbQiaNDrRHP2iRdkv2XNyypMoKXGB37I4u4tWduKgN7MisZlpQshrs1bRS-3KvZBha0tXwRqf2f2-8839A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/8d88eccc6f.mp4?token=h0P-zXuDva-UoSv1gbeBINAyEWTsWYP7DSeAj5Xmpv80LARn0_uOvkfvVMPAkJ4y8u5gXv0aGidGOVA6a85L3JijurcdB1HVor9LE41KpV07x_xa_cT56WOHdZwR3eODEHz-oDdxGlGQMSUqYZr9QzTyuZTweExES9rDetQ49318Ets3aoAxPAPnFSujUV8of9xDeIj32UBl_e2N4m1Lf1yThu0m80pTlfLKdxeZDVWItvGdLTVSYq1Bbq9TlrIlhijlwbQiaNDrRHP2iRdkv2XNyypMoKXGB37I4u4tWduKgN7MisZlpQshrs1bRS-3KvZBha0tXwRqf2f2-8839A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی مخاطبان/تظاهرات در شهر هرات افغانستان ادامه دارد و طالبان در حال کشتار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/126466" target="_blank">📅 12:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126465">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=tjgNWNMu7kiLFp55-wIkJEHSjwZpymR7ThMDuGQMDv8O-WVDqRokixZeUDejHmLt70Vs9xHliohNZ-Rz_m9v9g3An_7uyeVzq8MQBFIaL5OM24beKkt_OU8Wi4MHPxrL0aqZ9qd67irpzliFnH1Wkgyb20XAs9upFSx21_7VOKkh_jVbjE1YJ92oNjSZUOq9T8B7lK2MRZtN2RlC_CkZDi9KHgq2oUawE6_rf0gF-y1RHcdHBHrFL-KmKoDwjCBi-ZtppK5yqsepq7G_UY0MdK73Uou9JNBJS3Kst-n47eE3-0w4LlJ3E2m4wHzde6lStJC5uywEf4Ue7MDTdEWJXA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=tjgNWNMu7kiLFp55-wIkJEHSjwZpymR7ThMDuGQMDv8O-WVDqRokixZeUDejHmLt70Vs9xHliohNZ-Rz_m9v9g3An_7uyeVzq8MQBFIaL5OM24beKkt_OU8Wi4MHPxrL0aqZ9qd67irpzliFnH1Wkgyb20XAs9upFSx21_7VOKkh_jVbjE1YJ92oNjSZUOq9T8B7lK2MRZtN2RlC_CkZDi9KHgq2oUawE6_rf0gF-y1RHcdHBHrFL-KmKoDwjCBi-ZtppK5yqsepq7G_UY0MdK73Uou9JNBJS3Kst-n47eE3-0w4LlJ3E2m4wHzde6lStJC5uywEf4Ue7MDTdEWJXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک مستقیم نیروهای طالبان به معترضان در شهر هرات
🔴
طالبان میگوید که اینها مردم نیستند و نیروهای تروریستی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/126465" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126464">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
چین: مذاکرات آمریکا و ایران در مرحله‌ای مهم قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/126464" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126463">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سپاه : اردن به اسرائیل تو حملات به ایران کمک کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126463" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126462">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413a6c6658.mp4?token=AKs2qfS6sknAF01C4RnUDMbsYuYWMCpivvDI4G4n4hG-SlHMyD_piZQqV8Vjh3kMsk3yad7vPCa0MRngVaJiHpf9KXZSdZHyNHINvz1dDHoPH8IkapPWDAfyQMZmS0MnWATWg7d0--NUIBGJq2UVuca2n6tHpaGI-i9rn9PlP8v3bly-eDLBaE9Z-atEaTLct4DChEn3ZNC1bOewMXVdGg7NldRSYOHuRzOzwxPCKSZKLYb1ZQpEDKIPRnjrmWziFlf0rnU4EIJMjOxstLNam3cTiOZuW8M_5jHHSNZw4AXjXUXNiXDQC6sq4qQLaiof8th_LQ3gRQBh7sg0Q4CC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413a6c6658.mp4?token=AKs2qfS6sknAF01C4RnUDMbsYuYWMCpivvDI4G4n4hG-SlHMyD_piZQqV8Vjh3kMsk3yad7vPCa0MRngVaJiHpf9KXZSdZHyNHINvz1dDHoPH8IkapPWDAfyQMZmS0MnWATWg7d0--NUIBGJq2UVuca2n6tHpaGI-i9rn9PlP8v3bly-eDLBaE9Z-atEaTLct4DChEn3ZNC1bOewMXVdGg7NldRSYOHuRzOzwxPCKSZKLYb1ZQpEDKIPRnjrmWziFlf0rnU4EIJMjOxstLNam3cTiOZuW8M_5jHHSNZw4AXjXUXNiXDQC6sq4qQLaiof8th_LQ3gRQBh7sg0Q4CC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به یک خودرو در روستای الشارکیه در منطقه نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/126462" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126461">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سخنگوی دولت: میزان قطعی احتمالی برق تو روزهای گرم پیش‌رو، قابل پیش‌بینی دقیق نیست و مستقیماً به الگوی مصرف و همراهی مردم عزیز بستگی داره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126461" target="_blank">📅 12:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126460">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پنتاگون در ماه مارس فاش کرد که بخش‌هایی از نیروی هوایی ۸۲ در حال اعزام به خاورمیانه هستند، اما این موضوع را که برخی از آن‌ها به سمت اسرائیل می‌روند، فاش نکرد.
🔴
دستور اعزام ارتشی که توسط کن کلیپنشتین به دست آمده است، نشان می‌دهد که سربازان از تیپ دوم، هنگ پیاده‌نظام ۵۰۱ در آوریل ۲۰۲۶ برای مأموریت موقت به اسرائیل فرستاده شدند.
🔴
یک منبع نظامی می‌گوید که این اعزام به برنامه‌های اضطراری جدید ایالات متحده و اسرائیل مربوط به عملیات‌های احتمالی علیه ایران، از جمله تصرف جزیره خارک، مرتبط است.
🔴
نیروی هوایی ۸۲، که نیروی واکنش سریع ارتش است، برای حمله‌های هوایی و مأموریت‌های «ورود اجباری» آموزش دیده است.
🔴
به‌طور عمومی، پنتاگون فقط گفت که سربازان به فرماندهی مرکزی (CENTCOM) اعزام می‌شوند که باعث شد بسیاری تصور کنند آن‌ها به سمت پایگاه‌هایی در کویت یا قطر می‌روند. مقامات هرگز اعزام به اسرائیل را تأیید نکردند.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126460" target="_blank">📅 11:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126459">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718745a1a.mp4?token=lL0wGQaXtgzbb9vsqeFsjR5HTiUvWdRUWvgPWeo3RdC1kxZ_8_BMrEc1wTXPXI5IkW0AvxPVA9Y_5G6ygGziReCVeghhtoRKri1UXlEDiARwjiVjLrgqJVbY2oCOUPRQDEH3joqL8h9ddjWldjxNolU1gypwUb6A4ONM2FXj_7zRUL4H2XEwdiz2fBWzEFp_pV-qfhEvmCxWDdQnZPxCZp-jdpAwTFWRr5MPXpskz02HlqrUo7pNUFnrfBYXHplmsALXH_8qlcWqe9Vq1HK47gkKUch8FHWFT1u97lhJWYYVApacBBY_Ep9JbyTHmSxGT4lMiCcachsYionvD70J5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718745a1a.mp4?token=lL0wGQaXtgzbb9vsqeFsjR5HTiUvWdRUWvgPWeo3RdC1kxZ_8_BMrEc1wTXPXI5IkW0AvxPVA9Y_5G6ygGziReCVeghhtoRKri1UXlEDiARwjiVjLrgqJVbY2oCOUPRQDEH3joqL8h9ddjWldjxNolU1gypwUb6A4ONM2FXj_7zRUL4H2XEwdiz2fBWzEFp_pV-qfhEvmCxWDdQnZPxCZp-jdpAwTFWRr5MPXpskz02HlqrUo7pNUFnrfBYXHplmsALXH_8qlcWqe9Vq1HK47gkKUch8FHWFT1u97lhJWYYVApacBBY_Ep9JbyTHmSxGT4lMiCcachsYionvD70J5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: اسرائیلی‌ها و ایالات متحده منافع مشترک زیادی دارند، اما همچنین شرایطی وجود دارد که منافع ما در آن‌ها متفاوت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/126459" target="_blank">📅 11:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126458">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuFxTAmzjgiI-t6jiQdOhBLqkHTvUEdAToqXUXx2UgeMjvE9P5hAN7cBb7eb_BPVNMDeINl2VC5AWOCZ2rhs5i5B0_qEjwNKA1e7bZ7pGCpJTU6pA8xwTfItg-WEF3b3bCHVr5NSVaHqsa8Cq6a9XKcboR0pFuzQ0Ko0bb6iKykI9IuRdPidxkrhS87Sw-TLS83FrqDXzcjQu5WdmjaOkD4iOvFSYffzuZYuZ_Et3NkugDowsgZAtdno5ez3eeKR_3IlsF1n8uelvB4YPe5uxEfl29QWu3Pp2E1AEBtz8mJcXFBjqad6Tip7fzAbDqHay26wNssjcAdDA-zaTXhuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: پنتاگون ایالات متحده فهرست شرکت‌های چینی را که به عقیده آن‌ها به ارتش چین مرتبط هستند یا از آن حمایت می‌کنند، گسترش داده است و شرکت‌های بزرگی مانند علی‌بابا، بدو، بی‌ای‌دی و نیو را به آن اضافه کرده است.
🔴
در حالی که گنجاندن در این فهرست به معنای تحریم نیست، پیامدهای قابل توجهی به همراه دارد.
🔴
طبق قانون ایالات متحده، وزارت دفاع به زودی از خرید محصولات یا خدمات از این شرکت‌ها، چه به صورت مستقیم و چه از طریق واسطه‌ها، منع خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/126458" target="_blank">📅 11:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126457">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ در مورد جمهوری اسلامی ایران:
فکر نمی‌کنم هیچ نقطه‌ای وجود داشته باشد که مانع شود. فکر می‌کنم بسیار نزدیک به داشتن یک توافق بسیار، بسیار خوب، قوی و قدرتمند هستیم
🔴
اگر برویم و بمباران کنیم، که اگر بخواهیم بسیار آسان می‌توانیم این کار را انجام دهیم و دو یا سه هفته دیگر بمباران کنیم، دیگر هیچ چیزی برایشان باقی نخواهد ماند.
🔴
اما تنگه برای ماه‌ها باز نخواهد بود. اگر بمباران کنیم، می‌دانید که بسیاری از مردم کشته خواهند شد. چه کسی می‌خواهد این کار را انجام دهد؟ من نه.
🔴
و ما به یک سند امضا شده دست خواهیم یافت که در واقع قوی‌تر از انجام بمباران است.
🔴
شما به یاد دارید ونزوئلا را، درست کمی پیش از این، یک جنگ یک روزه.
🔴
ما آن را تصرف کردیم و روابط بسیار خوب بوده و ما میلیاردها و میلیاردها دلار نفت گرفته‌ایم.
🔴
ما هزینه آن جنگ را بارها و بارها پرداخت کرده‌ایم.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/126457" target="_blank">📅 11:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126456">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9623807c6f.mp4?token=NjUVaQSlmlbP-Zv0Pi4QToAnntNrzDaFk1Buy9RBnOCJnRaShBgsUh4UWMlGghG0N8VUSFBYoz6RIJE7wt-2dCOmUvj6b7IqIgKcC-vR4grc1_C21RapG3pJWOG1UlioHTok05Nqwt3H1ExWTjrRMMp7fH-cmLRS61LWLjpJ78Tth1kBYjAUtLT2-sqaoj7lbmkbEbHQldSPJge_VAky8Fmox6oUbzjx1rX031y_Akqckqp87dLBEbtklSi0ccEY6h0Qkx_1Ad3__Xma45WW5t8uOJ5-vqCriQ9nEixZzVBdSKQoYviKZDkbKmgk-BMHT805XWUbfm3m0uFdpKbt3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9623807c6f.mp4?token=NjUVaQSlmlbP-Zv0Pi4QToAnntNrzDaFk1Buy9RBnOCJnRaShBgsUh4UWMlGghG0N8VUSFBYoz6RIJE7wt-2dCOmUvj6b7IqIgKcC-vR4grc1_C21RapG3pJWOG1UlioHTok05Nqwt3H1ExWTjrRMMp7fH-cmLRS61LWLjpJ78Tth1kBYjAUtLT2-sqaoj7lbmkbEbHQldSPJge_VAky8Fmox6oUbzjx1rX031y_Akqckqp87dLBEbtklSi0ccEY6h0Qkx_1Ad3__Xma45WW5t8uOJ5-vqCriQ9nEixZzVBdSKQoYviKZDkbKmgk-BMHT805XWUbfm3m0uFdpKbt3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر نوجوان سنندجی که قربانی خشونت خانوادگی شده بودامروز یکی از مهمترین مراحل درمان خود را با موفقیت پشت سر گذاشت و جراحی فک او در بیمارستان کوثر سنندج با موفقیت انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126456" target="_blank">📅 11:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126455">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400f3a9182.mp4?token=o0DEcsHSgFNAXNiS9Ot4zIER0rCgvBGGY-XeTQ_cVi-W8Jv8CSfqy19EjD-h1CJCd6Jsh_xrHcbWkT1vyzm029WqdVAzGtqwpw7a7zSocVgUjQz5iuydKB6toieJNwyZUjDQTTlBbCEYFqTy61KLEtnnyrVQz2qlO3QzWAiC6RGReC-UIzJL_rmtRgJYo1lDHcYb7F_r7-lPedmUQWoU3vgOOUvdaoQwff4aph5MelScLBFhsi2RzeePs_d_ID4TTNPC2MRRVG3hvJOvTTM9TIo1WdHfDn61u0Xx43F_i8JDIGpXO8E9PG2BNXaJgOwqRzGZJ_CsrfdSh93f88ixCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400f3a9182.mp4?token=o0DEcsHSgFNAXNiS9Ot4zIER0rCgvBGGY-XeTQ_cVi-W8Jv8CSfqy19EjD-h1CJCd6Jsh_xrHcbWkT1vyzm029WqdVAzGtqwpw7a7zSocVgUjQz5iuydKB6toieJNwyZUjDQTTlBbCEYFqTy61KLEtnnyrVQz2qlO3QzWAiC6RGReC-UIzJL_rmtRgJYo1lDHcYb7F_r7-lPedmUQWoU3vgOOUvdaoQwff4aph5MelScLBFhsi2RzeePs_d_ID4TTNPC2MRRVG3hvJOvTTM9TIo1WdHfDn61u0Xx43F_i8JDIGpXO8E9PG2BNXaJgOwqRzGZJ_CsrfdSh93f88ixCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد جمهوری اسلامی ایران: ما مذاکراتی در جریان در ایران و با ایران داریم و این کار متوقف نشده است.
🔴
ما می‌توانیم حداقل یک ایده را در یک یا دو روز آینده داشته باشیم. اما فکر می‌کنم همه چیز خوب پیش می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/126455" target="_blank">📅 11:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126454">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8080f5f9.mp4?token=LYQ2r9orSG3Uii4okf95rmz1LhqoiPs7-fqTWAjDEcW4LUl1L2PEn3O0tLdL8iX1CgoiSYWIcbUywNFsgyBs6Ko05U-Oeq2R88vIG3Bq8NkJ0aZ-aDWeOmxcQp_95TSYR8Fz1mBuHJAFzD7vsaeZolwLUSP4uVBghHjJcGvVbm-4Z08SVwNbeQnKZbEB9q8wFolNiNplnHfxXe8zDbZ7a0pp9eKZ35m4ouJu-dla-3h4DI7ph4Phu1iIy5KCU1pwBhRuv_LJ56Rx5kRXAk647iGZO8KVij3F36jJlh19UK71H2FfW9oEJSr5NPGFt98KQ53jbjy5Bt5ShT4JwC71Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8080f5f9.mp4?token=LYQ2r9orSG3Uii4okf95rmz1LhqoiPs7-fqTWAjDEcW4LUl1L2PEn3O0tLdL8iX1CgoiSYWIcbUywNFsgyBs6Ko05U-Oeq2R88vIG3Bq8NkJ0aZ-aDWeOmxcQp_95TSYR8Fz1mBuHJAFzD7vsaeZolwLUSP4uVBghHjJcGvVbm-4Z08SVwNbeQnKZbEB9q8wFolNiNplnHfxXe8zDbZ7a0pp9eKZ35m4ouJu-dla-3h4DI7ph4Phu1iIy5KCU1pwBhRuv_LJ56Rx5kRXAk647iGZO8KVij3F36jJlh19UK71H2FfW9oEJSr5NPGFt98KQ53jbjy5Bt5ShT4JwC71Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در فینال NBA (نیکس در مقابل اسپرز) وقتی که تصویرش در حین پخش سرود ملی در حال ادای احترام نظامی بود، هو شد.
🔴
او بعداً آن را «بیشترین تشویق» نامید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/126454" target="_blank">📅 11:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126453">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROEmAc8YUc-XIJlmyxKlZmZq4xkZnzKcgvxc4xKXjvyLNqXZ5P_FSZWRB6RsgIf2BQmYAUQxtg0FZhsqhaVPAziC8mndxk6PKeYBeDh-t3dGdMAQfEMhKl3BTGWmw4BSymQazST4Ib2eDhN27KqNFml721UZn34wI362lF_uqAkipG5e6OnGaMJIyKfKD0ZhoRMNAl5cvZE_5gFiWes3Aqo1G12cx6pLBjgKjvY9P4NH4Qa6f-hCOOygaE9HdAGduhly8ohtJToV5_DHazNerwzuQH_CqtN0pcooSr072uHCxVh-tcXz2hoGGV6SCsO-ItBlXsdHw-2xYzS5albyMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه سی‌ان‌ان: ترامپ ۳۷ بار توافق با ایران را «قریب‌الوقوع» اعلام کرده، اما هنوز هیچ توافقی حاصل نشده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126453" target="_blank">📅 11:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126452">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ممکن است اسرائیل از توافق هسته‌ای ایران خوشش نیاید، اما ما به دنبال منافع آمریکا هستیم
🔴
مجری: "شما چقدر نگران جاسوسی اسرائیل از ایالات متحده و اقدامات مستقلانه‌اش در لبنان هستید؟"
🔴
ونس: "ببینید، به نظرم واضح است که اسرائیل و ایالات متحده منافع مشترک زیادی داریم، اما در برخی موارد نیز منافع‌مان از هم جدا می‌شود.
🔴
فکر می‌کنم جایی که رئیس‌جمهور خیلی صریح بوده این است که در حالی که اسرائیل مشخصاً اهداف خاص خودش را دنبال می‌کند، هدف اصلی ایالات متحده در قبال ایران، اطمینان از نداشتن سلاح هسته‌ای توسط ایران است و ما در واقع، به لطف تحولات چند ماه اخیر، بلکه واقعاً یک سال و نیم اخیر، فضای لازم را ایجاد کرده‌ایم که رئیس‌جمهور معتقد است می‌توانیم به یک توافق بلندمدت برای حل مسئلهٔ هسته‌ای ایران دست یابیم.
🔴
حالا، ممکن است اسرائیل از این توافق خوشش بیاید یا نیاید، اما در بنیادی‌ترین سطح، ما فکر می‌کنیم این توافق به نفع ایالات متحدهٔ آمریکاست.
🔴
بنابراین به دنبال آن خواهیم بود، چون رئیس‌جمهور ایالات متحده برای همین کار انتخاب شده است. برای خدمت درست به مردم آمریکا، این کاری است که باید انجام دهیم."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126452" target="_blank">📅 11:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126451">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: موشک‌های ایرانی به اهدافی اصابت کردند که بتوانند به حزب‌الله در جنگ کمک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126451" target="_blank">📅 11:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126450">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر ارتباطات: ترافیک اینترنت بین‌الملل قبل از ۴ خرداد با ترافیکی که از مسیر استارلینک از شبکه‌های مرزی خارج می‌شد، برابری می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126450" target="_blank">📅 11:12 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
