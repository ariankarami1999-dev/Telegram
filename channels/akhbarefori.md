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
<img src="https://cdn4.telesco.pe/file/GCnh-bCLnt0Wqg2N7c1X17BohsVdYaVSj7or_mjxLFuS6ZBRCd9pEM-yeb5lwZupsLKjS2Fm_IbVhY8xylyHe5TZVFgPsr7ijObyMjsMHtUFRTZa2QD20b4IqWC4ACrBj0X5AO15Ag38Nt1M9VALkCIJTUulDTN4OiTQAtfCEJ3NjyNxka_Nx8YXTYAFsTxolJzpgtWXdmxqzHAsk8e7pnsBtg53kQKTv1T36oSzirGAo40cUBOh1FV6o58Lc3Ck_Fgd-rrRnkF4liJv1Ig767xZ1IafbLqOzJDi1C9HSTJdXn9hdN87cOdMca9X_ozUl4yX01RknuhowxrEoyIB5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 22:11:46</div>
<hr>

<div class="tg-post" id="msg-690730">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6b82fae1.mp4?token=V4wA2xc9B4uRwBci-3G-yhygk-yXqf78g7dxxQKo7nOQTQx-f2xAgvhaSzR7AWQ64JXBO_WXSiPcZFYM_yAPGfLnirtbYQVUZ7U4EhnL9HsebhhEqe5m6kCUNHCGqVt-uc4KjKyDS9udVRvl2HlGL88MXDnIp2ybZOMUGpsmbLLOSlBxq4_fJqS94ENfY0guLoVKPqwhEfWnTGW1FcGbA1YdS8pUVnU9lOuXdiDLcjGH6iUT8c0d2ZnJp6IxgpPiJOmuQ5WWXHxPl-UINgeUNKBF5kNlK_uoBhPuSQTRwS3FmWslccUTjXTCrUBGNFq3mEXlad1XfEgGqhj8yp-hhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6b82fae1.mp4?token=V4wA2xc9B4uRwBci-3G-yhygk-yXqf78g7dxxQKo7nOQTQx-f2xAgvhaSzR7AWQ64JXBO_WXSiPcZFYM_yAPGfLnirtbYQVUZ7U4EhnL9HsebhhEqe5m6kCUNHCGqVt-uc4KjKyDS9udVRvl2HlGL88MXDnIp2ybZOMUGpsmbLLOSlBxq4_fJqS94ENfY0guLoVKPqwhEfWnTGW1FcGbA1YdS8pUVnU9lOuXdiDLcjGH6iUT8c0d2ZnJp6IxgpPiJOmuQ5WWXHxPl-UINgeUNKBF5kNlK_uoBhPuSQTRwS3FmWslccUTjXTCrUBGNFq3mEXlad1XfEgGqhj8yp-hhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از چند قالب ساده تا یک کسب‌وکار خانگی
🔹
در کمپین #چرخ_زندگی تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه اولیه نسبتاً کم، امکان شروع در خانه دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
این بار سراغ ساخت محصولات…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/690730" target="_blank">📅 22:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690729">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c6b995de.mp4?token=Z_4phr5npTceUQtNRip1qoaralt7ADXeadMw0ODuGJkuBFWL_F0xBzNewq4RngIaTNSJJdiAgxrda0srQf0BWflUC3ttHWdz-EnRb9_3kCPZ2TwDQ1_akap2exaHLk_4WGcDuvLTn9yT53kTeC5gCb2-g4RDKneeKqCVA8bvqkoQvTNeQT4judWbLdeuTjlN_OujOcRtsHbg9rS9_vSfG4e_l8cRKNkiEv9R6VPUw36zV9uzUIMX3FCrm-jMbqmwEZmp7UbsS8HIHzhZGMTWHAo-5GPXXoFf-S_uqwj0xY2cQH0fG6F1SKHCVL5ozNLyMOsUEtrVvfY5d-bl0pKBJCcv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c6b995de.mp4?token=Z_4phr5npTceUQtNRip1qoaralt7ADXeadMw0ODuGJkuBFWL_F0xBzNewq4RngIaTNSJJdiAgxrda0srQf0BWflUC3ttHWdz-EnRb9_3kCPZ2TwDQ1_akap2exaHLk_4WGcDuvLTn9yT53kTeC5gCb2-g4RDKneeKqCVA8bvqkoQvTNeQT4judWbLdeuTjlN_OujOcRtsHbg9rS9_vSfG4e_l8cRKNkiEv9R6VPUw36zV9uzUIMX3FCrm-jMbqmwEZmp7UbsS8HIHzhZGMTWHAo-5GPXXoFf-S_uqwj0xY2cQH0fG6F1SKHCVL5ozNLyMOsUEtrVvfY5d-bl0pKBJCcv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعترافات عامل قتل عام خانوادگی تو پونک  متهم:
🔹
اختلاف ارث و فشار روانی، او را به فروپاشی رساند.
🔹
مادرش برای واگذاری سهم ارث تحت فشارش می‌گذاشت؛ از خانه بیرونش کردند و کارتن‌خواب شد، خانواده‌اش می‌گفتند سهم ارثت را واگذار کن یا برو بمیر.
🔹
کسی کمکش نکرد؛ مادر…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/690729" target="_blank">📅 22:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690728">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
خشم شهروند آمریکایی: ۱۴۲ دلار دادم تا فقط باک لعنتی‌ام رو پر کنم!  مرد آمریکایی:
🔹
روزانه یک میلیارد دلار خرج جنگی در ایران کردیم که توش به تمام معنا افتضاح بار آوردیم و مفتضح شدیم؛ قیمت همه داره سر به فلک می‌کشه، اونوقت این عوضی (ترامپ) میگه نگران نباشید!…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/690728" target="_blank">📅 21:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690727">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91be67c90a.mp4?token=M6gIJTInxPcJ9TNsgb7gdx_MkHUA4PG834pPGWpRjlKyCTuxIL9VSD8bQY9UviD_1jG1jfsFy1DjUAPOCIjlcejVRQY9RXxGP0duEypttUn4Ua0ESgRgH341c6BMkVu_SP2jBs0b7yO1IkfKCnH9YYSEOo5cLJj4LHAT7aB6nUS0rYWLV5d79woibLRNw7EEgZhhcCleghcaCjGeKLKdCcSbv_PQ4xCVDBySTxzwVKED-0O45IBDgp9sYO2GROzKl0mE1VcRK-OHOGZz621rjiK6nXzYQtMQTTsg23LR4JXcIXLvwsqx-zKJvTzXnUYTAofwdIp_Xq8Hps9bXcYBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91be67c90a.mp4?token=M6gIJTInxPcJ9TNsgb7gdx_MkHUA4PG834pPGWpRjlKyCTuxIL9VSD8bQY9UviD_1jG1jfsFy1DjUAPOCIjlcejVRQY9RXxGP0duEypttUn4Ua0ESgRgH341c6BMkVu_SP2jBs0b7yO1IkfKCnH9YYSEOo5cLJj4LHAT7aB6nUS0rYWLV5d79woibLRNw7EEgZhhcCleghcaCjGeKLKdCcSbv_PQ4xCVDBySTxzwVKED-0O45IBDgp9sYO2GROzKl0mE1VcRK-OHOGZz621rjiK6nXzYQtMQTTsg23LR4JXcIXLvwsqx-zKJvTzXnUYTAofwdIp_Xq8Hps9bXcYBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس ستاد مشترک ارتش آمریکا: دشمنان ما ممکن است از نظر جغرافیایی پراکنده و دور از هم باشند، اما به شکلی فزاینده با یکدیگر در ارتباط هستند
🔹
از این پس باید فرض را بر این بگذاریم که یگان‌های ما توسط سامانه‌های خودکار شکار، در تمامی طیف‌های فرکانسی مختل و به‌صورت لحظه‌ای ردیابی خواهند شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/690727" target="_blank">📅 21:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690726">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای خصمانه وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم!
بسنت:
🔹
تحریم های امروز علیه ایران یک شرکت تجارت الکترونیک و سه شخص حقیقی را هدف قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/690726" target="_blank">📅 21:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690725">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b1c5a1ce3.mp4?token=O033VBtJrskO9F7mBWRJh4GTyciT3yyZQCYHtoxPpgWwSFEhYesO1t1h_xM8ZraGg3WCiTBcGp16qu7cg-Id_CdQ7gE0EEy0SK9J2NmQgwF5tEZ-PTYewEaJxY9JjJ6jf0whZCcZ__-GgXy5PAQuGGtQgjANex7rSQGNNBEEvWAKdJ1HP_q0mCUhCWP-zv4765aJ5EFuiQPkYDnSZzQ4OdvfClFGKXZ-HFbxydWbVU0RSnOO6tajfu6V5m9-VQJpi2QOLIDUn8ZuD2_vZPJbwR8-GAbQYl4tXYOfYqT0LjZTfePlJsjeQmjLID2uNkPYjrxq6-x_bLXvcYwHgB0w6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b1c5a1ce3.mp4?token=O033VBtJrskO9F7mBWRJh4GTyciT3yyZQCYHtoxPpgWwSFEhYesO1t1h_xM8ZraGg3WCiTBcGp16qu7cg-Id_CdQ7gE0EEy0SK9J2NmQgwF5tEZ-PTYewEaJxY9JjJ6jf0whZCcZ__-GgXy5PAQuGGtQgjANex7rSQGNNBEEvWAKdJ1HP_q0mCUhCWP-zv4765aJ5EFuiQPkYDnSZzQ4OdvfClFGKXZ-HFbxydWbVU0RSnOO6tajfu6V5m9-VQJpi2QOLIDUn8ZuD2_vZPJbwR8-GAbQYl4tXYOfYqT0LjZTfePlJsjeQmjLID2uNkPYjrxq6-x_bLXvcYwHgB0w6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای آرامش‌بخش درختان کاج در باران
🌲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/690725" target="_blank">📅 21:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690724">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
رفاهیات کارمندان در کیف پول واریز می‌شود
/
استفاده از کیف پول اجباری نیست
🔹
طبق تصویب‌نامه هیئت وزیران، دستگاه‌ها باید بخشی از رفاهیات کارکنان را با رضایت خودشان به کیف پول ایران واریز کنند؛ حداقل ماهانه یک میلیون تومان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/690724" target="_blank">📅 21:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690723">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu-RWjtzb1CjIfR1_deE_d_WnbO1bVUsixe8W3YEJcbxPGfgsXI2yYYnPCWa7TkBwWnXwJ_QXM0Bz07HTEDsRUG_SIkBGDTzCdDhn3afYM4I9UTodxNL8F-XF_rAeoLQNEEWRGokO8g9M1XOF2ur-DKsPPFdNCNNT76SkbO8heILFCjMJ175_pMZiGfFG1yNxol4ZcV9vUw0hhIgRpgkSxf7oc494DP9p9oXxNLVj_YblK415qfDOL2juar5I5hiZnOMP0Yvw9zOoOvDuXTj9JOvCGHUJ5RGFqD-8oOPcLUcituU2f4OoD556z9JmwjHNlj_F9ANQi1pUP_7YHVcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوران یک آتشفشان از فضا
🔹
این تصویر، آتشفشان کلیولند در آلاسکا را نشان می‌دهد که از ارتفاع حدود ۴۰۰ کیلومتری بالای سطح زمین ثبت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/690723" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690722">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
الجزیره: تهدیدهای ترامپ زمینه‌سازی برای مذاکره با ایران است
خبرنگار الجزیره:
🔹
صحبت‌های ترامپ درباره حمله به ایران تلاشی برای زمینه‌سازی مذاکره است؛ چون بلافاصله پس از سفر عراقچی به پکن مطرح شد، تماس وزرای خارجه چین و آمریکا نشان می‌دهد چین در حال سنجش تمایل دو طرف است و ایران به دنبال کسی است که تضمین‌های لازم را بدهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/690722" target="_blank">📅 21:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690721">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
عربستان برای تقویت پدافند هوایی دست به دامن چند کشور شد   آسوشیتدپرس:
🔹
ریاض با نگرانی از کاهش ذخایر موشک‌های رهگیر، از فرانسه، انگلیس، پاکستان و مصر خواسته سامانه‌های دفاع هوایی خود را مستقر کنند.
🔹
این درخواست در حالی مطرح شده که آمریکا نیز با محدودیت ذخایر…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/690721" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690720">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d07cea0f.mp4?token=TPaE_DfEDWx9vUmGoKZqjXjd-gf2uHSaXeCocCkp5TOCj6_4PmTAKW9zFN8fMw5g92tg_QDqwn5MZLLYwNtYmsfOg6cjpnwCVG4UhOzOmMaiXmt4pVKEKgAHQ5WYOYHaB3I9E3m8snnXy6HIu6KuCYOugaMmknBplXgIg0JBJPlOuAwqqqYpmodblN0ZPHMH5Olv_VUf7YFSbZGqEPCPc7t_IZUHm_vmtvtP6mTQxxluLfCLTje7qCOTVywn1hwhOpPyuEIBQRdgW1CgQw_1U9Smz3du44uzOF5G2p9J4FidUgGqvEAvGezcNs1r139plD3_t4b3eUu-ADPUAsA2Exjp4h2Qb68uBgi7Ctt7sx8QgzH2j5dsV4pBbEA_QGkEbnMVQWtR02e5WgotHDiffU-iQh2bmPFfY7G1BNwKqd2j8exofGUg_a68DxcucJWdB4WhsfIVv6i2oNHMi1xfDaRpKcALzdnVqwLFshJ12om_c0nPzfxaLwodwvx9NphiwUSb-t6OaZDA0MQgyaJxeujoGG_iUgMSBnqxCf_AtafSOJgVEDzXHkLTJFo4bTbRDHddqGuu-U7_FQnIjqIuNkUdu0PWTf6cx0cHJgUz0FDzKyc0Vfa-NjlTkOx-hSc-l0NnnaAfVYkUwpL2TaNsWlbExDARm2BS3xpyRW5EcPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d07cea0f.mp4?token=TPaE_DfEDWx9vUmGoKZqjXjd-gf2uHSaXeCocCkp5TOCj6_4PmTAKW9zFN8fMw5g92tg_QDqwn5MZLLYwNtYmsfOg6cjpnwCVG4UhOzOmMaiXmt4pVKEKgAHQ5WYOYHaB3I9E3m8snnXy6HIu6KuCYOugaMmknBplXgIg0JBJPlOuAwqqqYpmodblN0ZPHMH5Olv_VUf7YFSbZGqEPCPc7t_IZUHm_vmtvtP6mTQxxluLfCLTje7qCOTVywn1hwhOpPyuEIBQRdgW1CgQw_1U9Smz3du44uzOF5G2p9J4FidUgGqvEAvGezcNs1r139plD3_t4b3eUu-ADPUAsA2Exjp4h2Qb68uBgi7Ctt7sx8QgzH2j5dsV4pBbEA_QGkEbnMVQWtR02e5WgotHDiffU-iQh2bmPFfY7G1BNwKqd2j8exofGUg_a68DxcucJWdB4WhsfIVv6i2oNHMi1xfDaRpKcALzdnVqwLFshJ12om_c0nPzfxaLwodwvx9NphiwUSb-t6OaZDA0MQgyaJxeujoGG_iUgMSBnqxCf_AtafSOJgVEDzXHkLTJFo4bTbRDHddqGuu-U7_FQnIjqIuNkUdu0PWTf6cx0cHJgUz0FDzKyc0Vfa-NjlTkOx-hSc-l0NnnaAfVYkUwpL2TaNsWlbExDARm2BS3xpyRW5EcPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسعود بهنود تا پیش از نوروز به ایران بازمی‌گردد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/690720" target="_blank">📅 21:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690719">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
کلاد حالا می‌تواند مثل یک مدیر پروژه، چند کار را هم‌زمان جلو ببرد
🔹
کارها در فضای ابری انجام می‌شوند و حتی اگر لپ‌تاپ را ببندید ادامه پیدا می‌کنند. هر پروژه حافظه مشترک دارد و فایل‌ها یکجا نگه‌داری می‌شوند. این قابلیت فعلاً برای برخی کاربران فعال است و به‌زودی برای همه عرضه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/690719" target="_blank">📅 21:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690718">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mES-bJbTvImbjuxt6LpZ_uy69qTtnc2-ECA96bCEu7lYVwoGeuEgn6QWOziV-75CHhqFCfZvP8tdqHkieUHwt2hsJ28udmJITax6p-djRXKUy8bKMeBBhO2PunwqNXy0y9zcpgGd2s_0rLOTQil-2vdNNASarJhHYq_RNqghbv1IMXC1N9Hz2HBvuXdlGoWWWninKpb2MMFsS5QHdHi29HjOjIYymm_1xBfdbewoiKxnwaOyilBbANs6-U8CxnnlLbg44H6hQs_fOGRXlUELdB8Ga8btEeWt8Cf7GnM6cyzMZCKfmsgDwVCA5Pm5gNHElGdFshSqnPv-Mp5Xsd_nHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افراد مبتلا به آستیگماتیسم در شب چگونه می‌بینند
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/690718" target="_blank">📅 21:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690717">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de3a763e9.mp4?token=Cj27zZew3QAAsaElzkJuSUB7sJLGQF3vlMVJhYwNxZJgiYpPKcN7LoodZdPS8CkLLsw101TWY5ytmFCnbCtVk_glUOkNRltvyigJGOo3xWz_hLqlnLrdPOoSXxgFh2j8wUvMAxQxsfxGBVmf7QX0OP2dZbUIb4tI4Zc7Mznp7aQvNqxdfLJclMkIITf_tfH4cvUSgEMOUEc23hunbMUHgogwYAYQG5bljsd55-MoARUng2gutcefy8b7vZRNL4Hbkn8g9jczMb-kEILFu_X2XvFPtwkvytrbc06VBVJDSS6geKYH56pmRTKYsxzBkLmG8lxKfhqAw3gfD6UgwJoKdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de3a763e9.mp4?token=Cj27zZew3QAAsaElzkJuSUB7sJLGQF3vlMVJhYwNxZJgiYpPKcN7LoodZdPS8CkLLsw101TWY5ytmFCnbCtVk_glUOkNRltvyigJGOo3xWz_hLqlnLrdPOoSXxgFh2j8wUvMAxQxsfxGBVmf7QX0OP2dZbUIb4tI4Zc7Mznp7aQvNqxdfLJclMkIITf_tfH4cvUSgEMOUEc23hunbMUHgogwYAYQG5bljsd55-MoARUng2gutcefy8b7vZRNL4Hbkn8g9jczMb-kEILFu_X2XvFPtwkvytrbc06VBVJDSS6geKYH56pmRTKYsxzBkLmG8lxKfhqAw3gfD6UgwJoKdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی رسانه‌های انگلیسی از حمله‌ها می‌نویسند؛ روایت جنگ از نگاه دیگران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/690717" target="_blank">📅 21:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690716">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZZQknSNGtagCgtPG9XR4gpOrI0j-pKJxkefxRPl6WfvSd2ttph9osZMaIpokFW-BSvfJc_QsiGM8-hZZlAUymP-W08900D_V_A2pFv3qoMyJ3qHuwbGSUSk5HYyNYm2LNkZXYUY7uYx6Vf98xdRiCNhcSyUfXbmiHL-pAvTG_GmJJh_3xif-O8bUIFbOhS9q6akbmLdceBaslgaW9XnvX3vG0EsbXMcfvjvLG8Jk_BtY-gAimHz9glnjLLVWyCq_t8M1x1fvGz24h-dKkQD3RbqhEGdh2Ds6sZwjbnpXLPnrBh_vUK6G_Q3cvupypgAmHnJMHNAbYf8PVLHVEGiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیرانوند برای سربازی به فجرسپاسی می‌رود  مدیرعامل فجرسپاسی:
🔹
طبق اعلام ستاد کل نیروهای مسلح، علیرضا بیرانوند باید خدمت سربازی خود را در این باشگاه سپری کند؛ هرچند فجر تا نیم‌فصل امکان استفاده از او را ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/690716" target="_blank">📅 21:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690715">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e2adbde4.mp4?token=rMm0mOnHsAByFfTMvy72gdsPSS33lL7DL6foGMEhk18qcdaYTg3bg7YLopHkB5Zk3AqUkY0SxCU8DOT0WAicFvcARH_t_wjJ39tIykAm3Su4RDETcYgIv0WZFEjkFtB08oqubW4-KL3oJrMsnFE_kHOP0UtCq40P4RHDWVBFHO4jb05vbIm9jxUqqAZNu8ZRYwp5jy98o_pAcTRfXmjDOotnTvcOTJfdiSY8JrxBr2yAR-tXj1RJZTGpKcVtXi6pdcxzd542avlMntIu5SusjqNdFMHimtZcayvVCRWNMjyLM2m4pw6LOwKFAV1yjHDid8tSR4q-eRAmXQpvdMVilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e2adbde4.mp4?token=rMm0mOnHsAByFfTMvy72gdsPSS33lL7DL6foGMEhk18qcdaYTg3bg7YLopHkB5Zk3AqUkY0SxCU8DOT0WAicFvcARH_t_wjJ39tIykAm3Su4RDETcYgIv0WZFEjkFtB08oqubW4-KL3oJrMsnFE_kHOP0UtCq40P4RHDWVBFHO4jb05vbIm9jxUqqAZNu8ZRYwp5jy98o_pAcTRfXmjDOotnTvcOTJfdiSY8JrxBr2yAR-tXj1RJZTGpKcVtXi6pdcxzd542avlMntIu5SusjqNdFMHimtZcayvVCRWNMjyLM2m4pw6LOwKFAV1yjHDid8tSR4q-eRAmXQpvdMVilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ مدعی شد: تصمیم بزرگی در پیش دارم؛ یا وارد عمل می‌شوم یا نه
🔹
ترامپ روز پنج‌شنبه به «آکسیوس» ادعا کرد در جنگ ایران به یک نقطه عطف حساس نزدیک شده است؛ جایی که باید درباره ازسرگیری حملات گسترده با هدف پایان دادن به درگیری تصمیم بگیرد.
🔹
«تصمیم بزرگی…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/690715" target="_blank">📅 21:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690714">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سخنگوی قوه قضاییه: پرونده ترور امام شهید به دادگاه می‌رود
🔹
برای ۱۵۹ تن از مقامات ارشد سیاسی و نظامی دولت آمریکا و رژیم صهیونیستی کیفرخواست صادر شده است، ۶۷ نفر از این مقامات اسرائیلی و ۹۲ نفر آمریکایی هستد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/690714" target="_blank">📅 21:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690713">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqiObyrIVw8P_GUB0wfrDh-PPYNoVD_RRfmlOpdDwphKNA09oXCHOlr_7aw0u7sJRQw2RDnUlFmm8SVGSMJAeeH_t1mGycHBNvrokFU3_6HDjhr2vuZbzbvOdUVhm3xPDZLR4O_iCho8OJbU45yzNFPBmjUpLJw2mBYOuE0xNj36i1at1xuq_JduovCFYn0lRHjS0W-HUMbALpILXBjqkYB1RBqhedtW_nU7LHW57bluk55djEV5CR_O8W7YyZW9aaGnV_yFmx4ikENwecc_zMjs2pSXGJznH48Bk_i5n34r82HhRQu5iU4RyIsTPReoSNOUe8gx6PBR1LEikhrvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدن با علائم مختلف بهت پیام میرسونه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/690713" target="_blank">📅 21:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690711">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ترامپ مدعی شد: تصمیم بزرگی در پیش دارم؛ یا وارد عمل می‌شوم یا نه
🔹
ترامپ روز پنج‌شنبه به «آکسیوس» ادعا کرد در جنگ ایران به یک نقطه عطف حساس نزدیک شده است؛ جایی که باید درباره ازسرگیری حملات گسترده با هدف پایان دادن به درگیری تصمیم بگیرد.
🔹
«تصمیم بزرگی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/690711" target="_blank">📅 20:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690710">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ترامپ مدعی شد: تصمیم بزرگی در پیش دارم؛ یا وارد عمل می‌شوم یا نه
🔹
ترامپ روز پنج‌شنبه به «آکسیوس» ادعا کرد در جنگ ایران به یک نقطه عطف حساس نزدیک شده است؛ جایی که باید درباره ازسرگیری حملات گسترده با هدف پایان دادن به درگیری تصمیم بگیرد.
🔹
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آنها را نابود کنم یا نه؟ این تصمیم بزرگی است. هر اتفاقی ممکن است از طرف من بیفتد./ انتخاب
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/690710" target="_blank">📅 20:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690709">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnDfYApZ6Ba4w4Pwfheyjnx1GOvSlgSs1OcdMIoUb9s5ee4GvfB5gYSyxJQcXvUJiVqgaDSxHsTRHf4ekKE1sB4kj5RrVmYnAFNRG-SL0GXFkFsVXpv5YxYz_KE7cdWxOhJ_s1JzUbN1OpHTM0lgF1U1vyU60xde89npitWDuFF6SM70FbeqV1-NI29JkD21YN2vL30BDKqwh3T6tOKO3QOXKoN7M5tPXyxxLSlbOnKg5Yf5_Fx7mL6zb5hxki8cWDJooTbgV84kdHuSwfJ64WvUZjp7jDKANbBVh-tpjS7J_fJwezSjngnc0AAbmoJmUEGLHyEHTL-UquZ2dSiZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه آبگیر، سه رنگ، یک بهشت در گیلان
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/690709" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690707">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
مالیات هر نخ سیگار ایرانی در سال ۱۴۰۵، ۷۲ تومان تعیین شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/690707" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e039be7.mp4?token=gNJNe9OMvFef8jSA2Qej3FqAihQMzr9zue9r4V37twueU-igJVbQOx6V7u33efRai9bbuUP8kVvli9WdZXzRdaoCXOddddrd67SdUtWsvLaUajvxR00cWnQL2kvb5mRMaAulGVzbAvk_bnrKF8zauKStMb0yrN2JGkVd_ucKtnWe_SGL97q92lol35-rDy4zKFxAvSJqYMBgoJQ45Yw7FJAY6ii4O7uLGyJ-5dR3966g_C4hJjaOM76xXdC7OEGdx6PqW6Xde7FkkvsxT-vWnjGHvCICcdjmIyh5E57XAwbxkZH3Y8vvy5QfpLT2mb_gHbE9SAHQjLFuXOc0YN0OaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e039be7.mp4?token=gNJNe9OMvFef8jSA2Qej3FqAihQMzr9zue9r4V37twueU-igJVbQOx6V7u33efRai9bbuUP8kVvli9WdZXzRdaoCXOddddrd67SdUtWsvLaUajvxR00cWnQL2kvb5mRMaAulGVzbAvk_bnrKF8zauKStMb0yrN2JGkVd_ucKtnWe_SGL97q92lol35-rDy4zKFxAvSJqYMBgoJQ45Yw7FJAY6ii4O7uLGyJ-5dR3966g_C4hJjaOM76xXdC7OEGdx6PqW6Xde7FkkvsxT-vWnjGHvCICcdjmIyh5E57XAwbxkZH3Y8vvy5QfpLT2mb_gHbE9SAHQjLFuXOc0YN0OaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زدن پهپادی سعودی توسط انصارلله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/690705" target="_blank">📅 20:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419537b841.mp4?token=nniIo3WxeJpwEK5kymo0XIaDfkGYmKZG5Bmj-QphM4tVXhr-IqpNlBqs2QhLMADO1hjYeo1i6bmrdtkfpDHlcX043vnOaNr4_eWVkfVOmMaacgHmVWeDmGDfMVrj8LANfPtIkLGoqzmNKbVHF9bZRs4gd-fRSUmdWFpZ0V4B9rB9hUx1iErRt_XAc7OULze5lQRdEWa_bkEKSef25Gwbd8eWrukBYVIyDc5DQz1AyaImpNFGigQOPr00zJ9fBtWGa4KTCDRLE1sZd9OdMDpZB7NmrjhUgN9DoSoe1PbYPkhDDNxyffMsRuSulobF4aWiP_iMiZLANk-jlbiocoHgQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419537b841.mp4?token=nniIo3WxeJpwEK5kymo0XIaDfkGYmKZG5Bmj-QphM4tVXhr-IqpNlBqs2QhLMADO1hjYeo1i6bmrdtkfpDHlcX043vnOaNr4_eWVkfVOmMaacgHmVWeDmGDfMVrj8LANfPtIkLGoqzmNKbVHF9bZRs4gd-fRSUmdWFpZ0V4B9rB9hUx1iErRt_XAc7OULze5lQRdEWa_bkEKSef25Gwbd8eWrukBYVIyDc5DQz1AyaImpNFGigQOPr00zJ9fBtWGa4KTCDRLE1sZd9OdMDpZB7NmrjhUgN9DoSoe1PbYPkhDDNxyffMsRuSulobF4aWiP_iMiZLANk-jlbiocoHgQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبل از اینکه گوشیتو بدی برای تعمیر، برای حفظ اطلاعات خصوصیت این کارو بکن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/690704" target="_blank">📅 20:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690703">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: «توافق مکه» در صورتی که عربستان با حملات بیشتری روبه‌رو شود، می‌تواند فعال گردد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/690703" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690702">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
احتمال شنیده شدن صدای انفجارهای کنترل‌شده در ساوه
🔹
هم‌زمان با برگزاری نمایش بزرگ محیطی و میدانی، صدای تیراندازی و انفجارهای محدود و کنترل‌شده از شنبه ۲۸ شهریورماه به مدت ۷ شب در این شهر شنیده خواهد شد.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690702" target="_blank">📅 20:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690701">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfiWkKhncuCLLitG9-YRH87By7PJuXhpA8Rn-MVGSlr_EtYOaIATDV8pDeRuFSUKBkxzudiMeYiFJBOMgh7CDeIyWVJKoqkTnmLSTExH57vT4grW0whLWr7bn-UB_GUV7bNvxqYOnzPCIydyLqBv1h7bdr7bw0GUsMMaWs_P5GmA-4jrCyB30emlK8aCbVL3-XLotMCobuZLHphfsL6U-xWd7zm2Kc6qjCzg_JCWSawlOu_9ctuqyUIciiRNTxCTfE95G3WVhvbCM69pbI7VEt-2Yjlumj55B2mgThzcS_aiDgMb1netLeQn0Lm-1XYtnQiCBzn0DmL1lJf-NthIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دشمن واقعی
🔹
توصیه‌ی مؤکّد و مکرّر این‌جانب به حکّام کشورهای اسلامی خصوصاً کشورهای منطقه غرب آسیا و حاشیه خلیج فارس این است که دشمن واقعی خود را بشناسید و نقشه‌اش را دریافته، با آن مقابله نمایید.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت | ۸/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/690701" target="_blank">📅 20:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690699">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lw0hdhYHKRzDYltLvDpnjbhbbwED2T5DcD7GvOMMAYwd9yFAqKdRvnOk_XX3gM8ZaZgR7ZittaF2GSM2dyxZ1vgYwwkJBGjdsZhVKB3UORXjzpnB9GHgqgyEEn9aOb1VZchRF66JPs_izhuRmv1ZRdhdfMTFLDippB_7KQLrHv7VIlDP5CPHDXtLtpi9SFg1jrx_VwH9HgRrGt1B7M7gyfa2BMrVxOf9j7A25eGCSHui463-tFyD32Pa67HIy1w0M1IqPkZSuAJBJ7OK2atmEzJl1y2Dr7V3WmNELMhRLv769jphnTYcRF4IXbsksnLaBZ8hgBnzaUwma8z01FjiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjITjQsAgmYug4anTfaq8h9ZzQm-tJoPwwfox0qxVPBF3As9as3CiMhl63Fb5SFEDe6LztHvD3-bAQZQP7udhoM7UKKp7fHTbVS3Bvg15HKRJUpl23Xy0UT8OjDhCVnXtQPJr_S8Bh2ipUSta0pEocy-kBjHx5SlqCD_d79TJsnunraGGSRSxP1eXSgLPQPqxT6nQyOZdog8oBF5h9h8J_q8bLN5jHE75wyAVnMfpaMKV2xXZtNCPSOOwYtkt46NM0dAZRx3yez5GKOudFyK6wscishB5v7qcxtTxPx-k9uyBfL8pn5m7xMxTAs3ebXBAO0sq4ZkpjwvQOwV8nWgrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعداد و ارقام عجیب و غریب در صورت‌های مالی صنایع غذایی کوروش؛ ثبت ۳۵ درصد کاهش فروش سالیانه و در عین حال ۴۵۲ درصد افزایش فروش؛ پای رانت ارز ترجیحی در میان است یا احتکار؟
غکورش از زیرمجموعه‌های گروه گلرنگ و تولیدکننده روغن‌های خوراکی با برندهای اویلا و فامیلا، در سال مالی ۱۴۰۴ توانست سود خالص خود را ۴۵۲ درصد افزایش دهد؛ جهشی که در شرایط کاهش حجم فروش رقم خورد.
بر اساس گزارش‌های مالی، حجم فروش شرکت روغن خوراکی در این دوره حدود 35 درصد کاهش داشته، اما سودآوری با جهشی کم‌سابقه همراه شده است؛ موضوعی که این پرسش را مطرح می‌کند که چگونه با فروش کمتر، سود تا این اندازه افزایش یافته است.
یکی از گمانه‌زنی‌ها می‌تواند این باشد که تأمین روغن و مواد اولیه برای تولید محصولاتی مانند اویلا و فامیلا با ارز یارانه‌ای و سپس فروش آن با ارز آزاد پس از حذف قیمت‌گذاری دستوری دولت است، با این حال باید صبر کرد و پاسخ مسئولان این شرکت را شنید.
@Titretejarat</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/690699" target="_blank">📅 20:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690697">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k76WBizo5NdgvGk8fereDpV1s9rlt00a9s8Nd0KUuHeZ2tYWi01ehIarLm3js79oWmCJ0JcmI0E7RdX5N65WyrTMI7UOaYsZ13RxfMY7bBXT-rJn6wRywwmioH0R--dzo941pDCH6Nkd8c-y95YYPysuLwmcG7eZNuoJgsifNbzneIzOtrSpzdsEgeggpysot7JywxchlDClTW9alTFya3sCineSorUMUvg63owOGdNY2jq9eSCDWdDeINCeKtxiKImJgIVaUzVtnxyUowTu9jKEG7IwcxrFB1_GgFpndzc1kj6UB6oZ1x55EtIslt2OTtu1gSkSnCXXaX0D2g_Ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارزش باشگاه‌های لیگ برتر ایران
پرسپولیس ارزشمندترین تیم این فصل لیگ برتر ایران شد
./ ترانسفرمارکت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/690697" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690696">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjtRaUh-ooq970L7fp4TVC0MhE9BrhP4R9SzRSR6cHLlHurVGn3RBGiAA6ZLY6LLuIGr-NKaAjNcokJMe2fgr9dbNwroHcrigdZQZH23Fr2CeknoKBWreN3PohcLmfqPuUzCAT2CDif1w9y7DOamwq2DoG6uacr-dYs9omTsdQ1v-XAMMtS8i5X9GRfEw2UoWDmC3AwpGkGptVIbWyq2BeTMhw1wZgBKeFBTgYdhCLaVAoKuyXWr2y9OoF5-OP9Nbsno9gcuCZnoI13RZdcGk1jJA6ODvN0RklMbN3nXPdK43WQ3IyRAzX4kH_NQqrOSOn-2mNWhFXWi-EdIVb6tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه امنیتی برای یک نفت‌کش در سواحل یمن
🔹
سازمان تجارت دریایی انگلیس گزارش داد یک نفت‌کش در ۷۵ مایلی شرق بندر عدن توسط یک قایق ناشناس تعقیب شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/690696" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690695">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مقام‌های کشورهای عربی به ایران گفته‌اند که می‌دانند هدف اسرائیل پس از ایران، خودِ آن‌ها هستند
احمد دستمالچیان ، سفیر سابق ایران در لبنان و اردن در
#گفتگو
با خبرفوری:
🔹
این‌گونه نیست که کشورهای منطقه علیه ایران با اسرائیل همراه باشند؛ این موضوع دو دلیل اصلی دارد: نخست خواست ملت‌های خودِ آن کشورها و دوم، هشدارهایی که مسئولان این کشورها دریافت کرده‌اند.
🔹
اسرائیل رژیمی توسعه‌طلب و تجاوزگر است که تمام منطقه را هدف قرار داده است. تنها هدف این رژیم، با همکاری ایالات متحده، تسلط بر منابع نفتی، انسانی و سرزمینی خاورمیانه است.
🔹
از ابتدای پیروزی انقلاب اسلامی تا امروز، اولویت اصلی سیاست خارجی ایران، داشتن روابط حسنه با همسایگان، به‌ویژه کشورهای عربی حاشیه خلیج فارس بوده است و جمهوری اسلامی همواره دست دوستی و برادری به سوی آنان دراز کرده است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/690695" target="_blank">📅 19:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690694">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
جنگ ایران کشورهای عربی را به فکر سامانه ضدپهپاد انداخت  بلومبرگ:
🔹
جنگ علیه ایران، کشور‌های حوزه خلیج فارس را به سمت هزینه‌های کلان برای سامانه‌های ضد پهپادی سوق داده آنچه اکنون شاهد آن هستیم، احتمالاً بزرگ‌ترین موج هزینه‌کرد در تاریخ دفاعی خلیج فارس است.…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/690694" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690693">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c76888993.mp4?token=qSLVY4UwdbGdFcICrURwuMBLLEIkS_5dV7d4sxuNjQHB0YTlDpgdzTBWDoj6gDhNTcxqAznyjnxRWC_qsifNsbVuAyUTIMmdlD1TxTQEy7N8LeV6XXc0vfU1kTAjgAs1vAqkizAKxHH7V0EtgBvlBG-5KKu0R9XPhObeORWgKGlZ_CZdvzpKtMLcsoFpSIw7jyHAlzdFyfOp41_ONJnIvgYjmLoSstLbA8vN25HBhqyMMPUHH250GwB_zVkQkfdpMTeUthaAl6KdiXTJEsAAx-GhQfmHS2_x1e58MGFnw-8YRErTIPx3rXgx8vLF2gt9sFwrGpX9GtyaQvKh-Zt-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c76888993.mp4?token=qSLVY4UwdbGdFcICrURwuMBLLEIkS_5dV7d4sxuNjQHB0YTlDpgdzTBWDoj6gDhNTcxqAznyjnxRWC_qsifNsbVuAyUTIMmdlD1TxTQEy7N8LeV6XXc0vfU1kTAjgAs1vAqkizAKxHH7V0EtgBvlBG-5KKu0R9XPhObeORWgKGlZ_CZdvzpKtMLcsoFpSIw7jyHAlzdFyfOp41_ONJnIvgYjmLoSstLbA8vN25HBhqyMMPUHH250GwB_zVkQkfdpMTeUthaAl6KdiXTJEsAAx-GhQfmHS2_x1e58MGFnw-8YRErTIPx3rXgx8vLF2gt9sFwrGpX9GtyaQvKh-Zt-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از خودروی ۲۰۰ میلیاردی در تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/690693" target="_blank">📅 19:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690692">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee665b774d.mp4?token=Gacza1iltwvV9ZPhCbdMX_smLQl6aQA6rdnb_FlYYygA6rzB1NmbvTWrgm37DNgR6O3oJIxRi0S43OwbgNbvwR-aiSkiujYRhKTor4Qxzorj-LukWkFViq-cu8etM4lya7D8lHcQvIVVwNagEuJiLwTYTgya0aM4sMNheYPJIo2ZTR16S5wrRS78z45FIuSTnE2L9vlxpIvSDWYrZ00N8z1ZARZB-GEX-K9DXrzt1wKJpVjNIGTJm4cvH1ezTgbbLySNmi_U96jeaxI8QhyBHcLJo5bzSfZsob-2QDGNBT5JHlT7iC_XbYt6EuECE_bhildqemQ5h96-5MLt68R9uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee665b774d.mp4?token=Gacza1iltwvV9ZPhCbdMX_smLQl6aQA6rdnb_FlYYygA6rzB1NmbvTWrgm37DNgR6O3oJIxRi0S43OwbgNbvwR-aiSkiujYRhKTor4Qxzorj-LukWkFViq-cu8etM4lya7D8lHcQvIVVwNagEuJiLwTYTgya0aM4sMNheYPJIo2ZTR16S5wrRS78z45FIuSTnE2L9vlxpIvSDWYrZ00N8z1ZARZB-GEX-K9DXrzt1wKJpVjNIGTJm4cvH1ezTgbbLySNmi_U96jeaxI8QhyBHcLJo5bzSfZsob-2QDGNBT5JHlT7iC_XbYt6EuECE_bhildqemQ5h96-5MLt68R9uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاکانی در پاسخ به اظهارات روحانی: برای ‌پاسخ به کسی که به خانه ما حمله کرده که همه‌پرسی نمی‌کنند/ یا از سر خوش‌خیالی این پیشنهاد‌ها را مطرح می‌کنند یا از سر ترس/ به خانه ما حمله شده و ما مقاومت می‌کنیم و باید سایه تهدید، تحریم و جنگ را از سر کشور کنار بزنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/690692" target="_blank">📅 19:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690691">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msNrCNDKJCBS_sT_LnYvuw7Z0ugAL8v06_K2aI_wusRfgSi41aU0rzoKCT-XAhEhKf1qVo68pk6Cp_fI9b9QoaD1DyclMhiTFkjJeGS5gQ5tyFqOxaF9Y49MP1WOh3SUx4_XHCS3SLspB0z7PlYitHS0CAZSnHBpFH9RwEzWZrdFNBVLnR8GNF_PIAxkX17BgrE8wXmwaLR_XsP_UhvM7pT4ZspdZr4S-IbFXAQ-ynvTKIEAAPIg8BBYRHjmcCqYOXb-4NTQcPg1u17KOnsedffwh2YqEuKxLAsgNKJ1V58RSN6A5mKbVZWmFBMqZtzlTMCDji1rgk538FerCaLPCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر انتخاباتی برای ترامپ/ ۴۷ روز تا انتخابات
🔹
در انتخابات میان‌دوره‌ای ۲۰۲۶ آمریکا، رقابت اصلی میان دموکرات‌ها و جمهوری‌خواهان (حزب ترامپ) است؛ برخی برآوردها از افزایش شانس دموکرات‌ها برای کسب کرسی‌های کنگره خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/690691" target="_blank">📅 19:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690690">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIdHnAgiNnicwAmkceTduB_aT85h_nTk9vXXAYROsYlx_r6Ob6_g8qIy2XKdMycrENMzZT3x4mWXsFsMY-kLwfoRoGlQqO1VAq005Wi0cNrL0OGVnAMg4PY4PldwaB7MkQWKAe2xUtSFd8ijua5XcUj4VRaRtH9ck2kdSKIV7A-NgPEof4viiBSzAIKTaszc-wRwXYntMP9MS3uCDpsOhT18i93pMnFv8fMPP67UaR8efyCf2c-29LEwEayQkIHjj2gK17p2zL1xsuWM74atteEGgpr6viFdJ9juC3LZt4L9a1HeSM656XoB38IBCZLEZY9J02eD3IDKWfWoop8KrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/690690" target="_blank">📅 19:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690689">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
جنگ ایران کشورهای عربی را به فکر سامانه ضدپهپاد انداخت
بلومبرگ:
🔹
جنگ علیه ایران، کشور‌های حوزه خلیج فارس را به سمت هزینه‌های کلان برای سامانه‌های ضد پهپادی سوق داده آنچه اکنون شاهد آن هستیم، احتمالاً بزرگ‌ترین موج هزینه‌کرد در تاریخ دفاعی خلیج فارس است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/690689" target="_blank">📅 19:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690686">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXy7Ota5_IN6haJXq-3IXsXB62nv1Nb-Q-24gSERikywh2CbPW1VfzdW4YTcxC1VT9NDNcnq0EM9pdJjzobFoP0x-gTyqe0-7sQi2bWMFCxPhIi_cAHhHwh1d7UOuqfle_MeLZxJJafZaxpoG1B6cEpDxUE-HBXffOpidoH2SV6k8I3IdqEsogt-6BkuvWOwmoqEzzG2mLbPzted_QWBzyljYhjojD_aFqIcS_xyhR_1MH6VNZDEjyhW8cv-3SqZwi_5WID-FOa7ijR9EFMFcI3lOeja1SZRFicbmLTseBMYw7Cg52nMHaHyQmzwCYzCNsj1rmq7qAh8efYJBuHxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMXxpPxe4LchrBgriiH2k7d5AV4Oj91TQY0HLGmof8-nEd4ix2Vf1iBglI6ue_I2O03SiqVXD2L1L_wcSCf8cpF71rCmx9grjIvJBlNzrkG39D_H9qrxGzE2vk1DWHfOGxYeZ76U0ZrpVHV47WgibkrHT1lTRvoQOyDNUXsAwzSaYpeFn3JrORPGM2d_FocbT-jnYNT_eulbMbm3CZCEkoGUWq0EoANrfI8fh-SSWK5PQcDb2BxePpP_SnLVv6-1GioMMpAeAal_BhtmLHU2yJBHWogxsAHluTO9R51qJLzMZdeGKalvoSVUjXP4VsD2LmjbYHvTORuJaMT92v-xtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دستگاهی که به گوشی می‌چسبد و صدای شما را تغییر می‌دهد
🔹
گجت Key Pocket، با اتصال مغناطیسی به گوشی، صدای زنده را تغییر می‌دهد، با دور زدن محدودیت‌های نرم‌افزاری، صدا را مستقیم به اپلیکیشن‌ها می‌فرستد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/690686" target="_blank">📅 19:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690685">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2705b1db6d.mp4?token=CAHF3N6SbV2p7GlcF3_HJoe7NrRUGD2VOb3MR5BcApHNMxnls8e1dJjdNqwbmcpbkCo6qhuw2UN_e80Kghe1Xsu0-XzkqfxvNrqRkdTgwkPYY2qeAudJ1n38ySh8yOXFoYb1DODeb0BDBjprDicLRD9GuGrC2LHyTzsvyR4q3OGtPwoiKBuinVnyCZvHuUpDhCVOmsDfG2NOiZmLA04mfNdVsqxnqmuBkqPwEF3AvJzb-q2YjyMO9VT99kt5wTme7ZTMFXJpG2pnBHyA__9MsJKgwbFuA_z7iZjajEZMv9qquMPjZ-EZkNCwoOZqEnqf4d0D85ajWlOCIrepATjblg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2705b1db6d.mp4?token=CAHF3N6SbV2p7GlcF3_HJoe7NrRUGD2VOb3MR5BcApHNMxnls8e1dJjdNqwbmcpbkCo6qhuw2UN_e80Kghe1Xsu0-XzkqfxvNrqRkdTgwkPYY2qeAudJ1n38ySh8yOXFoYb1DODeb0BDBjprDicLRD9GuGrC2LHyTzsvyR4q3OGtPwoiKBuinVnyCZvHuUpDhCVOmsDfG2NOiZmLA04mfNdVsqxnqmuBkqPwEF3AvJzb-q2YjyMO9VT99kt5wTme7ZTMFXJpG2pnBHyA__9MsJKgwbFuA_z7iZjajEZMv9qquMPjZ-EZkNCwoOZqEnqf4d0D85ajWlOCIrepATjblg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسیاب آبی خوانسار تنها آسیاب آبی فعال در کل ایران است که هنوز با سیستم ۲۰۰۰ سال پیش کار می‌کند و همه بازدیدکنندگان را شگفت‌زده کرده‌است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/690685" target="_blank">📅 19:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690684">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh7mZ9BqhIAPrcjxwXyZYmdQ7_21QR5WlxAlROdQamIcwj__-vguEelc-uI_m3vIahFQw5NHmAM5s5lIAU4pUm9EbZP0a-j4JQzkbi-2orIavZBC7Naf_88c-vXrRyFDRF3CztnDjrG2RaDCgNNeLL9fnSjgAFjJKFbmWBD5hEQKEbSDBkvaEIkgpCamJIC3YvGI2I5o4aQTyV4ixYmlwB6tYhdRIUHL96dPU7zA7c9SHHA62jWrg3mcyPh9waAvc5ZUuLXVzm6UKKNVxg1n0uAi5VjtOXFfKukRyPjGXKQZzEXdAzSrVjL1XCQFV63OYmbXZFmfiySuKH9S7GFz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین عکس از یکی از دو قاتل پرونده قتل عام ۵ عضو خانواده در پونک تهران  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/690684" target="_blank">📅 18:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690683">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAQRBzbICrtL9eLT3RKGglQrPjgyNkKJszOwHuRL_bprIXEDB0DJ2yFMGRDS2A63TSvWtpSRMsbwgRH3FA_vpE5qL1cTtjsHZHqYTYh_TtuYcMTMk9nmajUKOtvIh2ZAsT7PH1JmJD5yfdY8UAXmyvLaPVEpYVWcGc6voFkSsdL0LRrmuaOEw-rI3Hp-4GdKDeFMTS3Vmj6l6oLDHGIHad_-uQ1b7hXcb3yolHxED2mw-v47Ewa_S9xkTBNrzTR5TBEfkYtE8wparUmC7qGFYErF8ZZfD0Axw0UX8Ihs0KoymX334NO5vvSqXvDtg-Meubg8GX0UqiYug9s38doM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با عرض معذرت
🔹
محمدرضا عارف، معاون اول رئیس جمهور در مجمع صنفی کانون استادان دانشگاه: از مردم عذرخواهی می‌کنیم و  شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند. نمی‌توان با تورم ۴۰ درصدی و رشد ۲۰ درصدی حقوق در دو سال گذشته، انتظار داشت مردم بتوانند زندگی خود را اداره کنند و اگر تورم امسال به بالای ۶۰ یا ۷۰ درصد برسد و افزایش حقوق ۲۰ درصد باشد، ادامه زندگی برای مردم امکان‌پذیر نخواهد بود.
🔹
هشتصدوشصت‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/690683" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690682">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
واکنش شهروند آمریکایی به افزایش قیمت بنزین: سه بار بهت رأی دادم ترامپ و این تشکریه که ازت می‌گیرم؟ تو خائنی!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/690682" target="_blank">📅 18:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690681">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
آناتولی به نقل از منابع پاکستانی: عاصم منیر از ایران خواسته تا انصارالله یمن را متقاعد کند که به تأسیسات انرژی عربستان حمله نکند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/690681" target="_blank">📅 18:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690680">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82885dd77.mp4?token=u9Uu4mV8RF-YO0waX_abiJG2GrWHf-CAL3_vjOp2HOEYntBOSASeTlPq5CkLftw1PLQ37hkL2VaEFlHAPFBKlWcQpBGI5iLYqsa-zmhHRGCL86VYLTr9UjynvzAXB8naJW32P0WD480C7279C5i4IE2OaG9T6wf3DcSDqWf03Pjo8QJMLb6V9uvPgwpEOpG8jsPyUvxnrgqFTapqzwVryLONfgqnqXXOVvTASPwsQR6qMqz_OdN4LqnkECrY-FnsX8nrB1X37ppt7nXy0MQnsg9-Faeur4qqF9bgN2zvDFS56SLyf3YaaUIOu4Fxggo8koprrYvu4lKVg40uBlfO0T3uCpjT2jqiOMB1zIbjRcGmpf0oSChkWuKS6b0MVeGOo3N9dC14kCG4sWlPoh7tPfW4a7VAnL6TW3zPlJhCuUSK72xirGik8P4_9MM-WQLfLK1lw9lUatngq9UkSI01ELTlaeHYksHK2aNLX9InB3yttz762qPTO0SFlwBG5P3X8e77JbrhZKLK3Wue9ZZL7CpVq9MBWe6RnKwYJqGFMHKdk-jF5fNNjNmIRJBN9ibnIIXpWgiW66EU01WVm686wZDZd1HDZs0LDVPd_ldMx-E_1tjxhBAox35osftAYfia_R1fEL8-f-nHa2Fy40DLEGeesgqungkSXWgqu01AhG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82885dd77.mp4?token=u9Uu4mV8RF-YO0waX_abiJG2GrWHf-CAL3_vjOp2HOEYntBOSASeTlPq5CkLftw1PLQ37hkL2VaEFlHAPFBKlWcQpBGI5iLYqsa-zmhHRGCL86VYLTr9UjynvzAXB8naJW32P0WD480C7279C5i4IE2OaG9T6wf3DcSDqWf03Pjo8QJMLb6V9uvPgwpEOpG8jsPyUvxnrgqFTapqzwVryLONfgqnqXXOVvTASPwsQR6qMqz_OdN4LqnkECrY-FnsX8nrB1X37ppt7nXy0MQnsg9-Faeur4qqF9bgN2zvDFS56SLyf3YaaUIOu4Fxggo8koprrYvu4lKVg40uBlfO0T3uCpjT2jqiOMB1zIbjRcGmpf0oSChkWuKS6b0MVeGOo3N9dC14kCG4sWlPoh7tPfW4a7VAnL6TW3zPlJhCuUSK72xirGik8P4_9MM-WQLfLK1lw9lUatngq9UkSI01ELTlaeHYksHK2aNLX9InB3yttz762qPTO0SFlwBG5P3X8e77JbrhZKLK3Wue9ZZL7CpVq9MBWe6RnKwYJqGFMHKdk-jF5fNNjNmIRJBN9ibnIIXpWgiW66EU01WVm686wZDZd1HDZs0LDVPd_ldMx-E_1tjxhBAox35osftAYfia_R1fEL8-f-nHa2Fy40DLEGeesgqungkSXWgqu01AhG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غول پیکرترین و عجیب‌ترین امواج ثبت شده زمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/690680" target="_blank">📅 18:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690679">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
برنج، افزایش قیمت افسارگسیخته نخواهد داشت
محمد مختاریانی، رئیس انجمن واردکنندگان و صادرکنندگان برنج ایران در
#گفتگو
با خبرفوری:
🔹
با وجود محاصره دریایی و اقتصادی مشکلی برای تأمین برنج در ماه‌های آینده نداریم و برنج هندی از مسیر دریایی و برنج پاکستانی از مرز زمینی وارد می‌شود.
🔹
با توجه به تولید خوب داخلی و واردات انجام‌ شده، پیش‌بینی افزایش قیمت آنچنانی نداریم و برنج در محدوده تورم نوسان خواهد داشت اما جهش افسارگسیخته قیمت‌ها اتفاق نمی‌افتد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/690679" target="_blank">📅 18:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690678">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh9fqiAMB7gt_QTq-FqlWO_ra-U47PcnoXzHaqtzb4L9WXQgIWRMrlbQ_-dkEl6POGuVAkxJraq2-j6DeS9zIJLcEAmH2TjsxGmyABbakbw7_mEt0BDFeheH7hjUI46uB7uUPipcojGxm7s-DHrHGW96IrzwRZe6v16kS1eqi36J-fA_LIuk6uj0EYQi9_oJZTGUxwvr28klBzKvkDyjJwybeypEfe6v7XhIaWAyYOhp30hNbVUb-3JkqJDwgq7tH_4QswaY6xCVatllvS_sXuMG33gVdt2gkwz9_XNLR_QyxTUUXXblvRXE0oTdZsqZ_mKHMBjWzWZ5iaIQE_HHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این‌بار به میزبانی استانبول/ برنامه سوپرجام اسپانیا ۲۰۲۷ اعلام شد
🔹
سوپرجام اسپانیا ۲۰۲۷ از ۱۳ تا ۱۷ بهمن ۱۴۰۵ در استانبول برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/690678" target="_blank">📅 18:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690677">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11691d20c7.mp4?token=U71mC_sK9IuFNiBm_giZyhz_JpoOBT2JZuZsfCk7PkRABGGZs106yc4W-0ykY8ai198flJHFD1cpZx28xqduN9kzVpklY6HtdDacCKh5PX93DnhrruYZWN4byppBa2VrQfV7Tmf4ZIUZt2tRwcFND-v5FxB4xoIEchpAyoz3ttR_W9EqRpAnHRzqIpp-7Ek3d44K5mh2feIlm9l0O-36U_RwjXck1QV2EW60_M3ufuL7GLFCGSVrVDyAnAnOHUhAuVA4W-5q0zhXVqVR7yf6aLfhX0puR09q2QrdNfcHpydMk1yB2oP9K0OGzsb_Jl2kNQ80y35az2FEmu3yZOB3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11691d20c7.mp4?token=U71mC_sK9IuFNiBm_giZyhz_JpoOBT2JZuZsfCk7PkRABGGZs106yc4W-0ykY8ai198flJHFD1cpZx28xqduN9kzVpklY6HtdDacCKh5PX93DnhrruYZWN4byppBa2VrQfV7Tmf4ZIUZt2tRwcFND-v5FxB4xoIEchpAyoz3ttR_W9EqRpAnHRzqIpp-7Ek3d44K5mh2feIlm9l0O-36U_RwjXck1QV2EW60_M3ufuL7GLFCGSVrVDyAnAnOHUhAuVA4W-5q0zhXVqVR7yf6aLfhX0puR09q2QrdNfcHpydMk1yB2oP9K0OGzsb_Jl2kNQ80y35az2FEmu3yZOB3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیو رو ببینید تا در طلافروشی سرتون کلاه نره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/690677" target="_blank">📅 18:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690676">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه ملت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e913bccf1.mp4?token=K8k3aMFs-WSij3y14-wj1X45kz3vmnqfMA0oI9jNDpHk48Q9jC-SXkM8gMkz4eSGgiP_g7Hf7Tn1A7St2wNcY_do9l6W3LgEAnKtDe9imx1Y48awHfDdGis4-mJh_S86u3iLfQ_oPhmzZZp320DpgaNCiKRTvocM9VD2cNZqjsVCA1ps5Vxa48sBhFuMzehaIcMsSAjtrCzqQgFYKTCJfyEu4jvPJiMP_lh5o-Ie9GOS3Jtn2FYgcFqgcsYjQw0Dt4fl_rVfs2gHu0GTf6L1tOWbLj_pfKghMzSMNze-EiGkzxLCtQqZjGvBPaXssZt1sdyUM23aQsLXsGmu6HkhnzJVbsI565t4fpwpxwLTUrFTuAL_DyIQb2oTNCdojP7Dc4aCtJv_ksbAmOagvG-UJGK7IT9sfqrh3LYIkiHg7YugmLG0Ysq0iK75uMBmkGCGgaLjaobV4YEZrl51rC8FYxG-fbRPrc9TAcO4yKM23zvpUmTdb-3ABUICRc5sp31DHU0FAVPQA14qapXvCsoXYZO4IWQBl7flwfBKJp-oZ8vp11_NWgqbblEjvo81Ifq_T-IFTRNJtgbOM_VMmH2ewlb3ctrtGAnHu6fmtESDWMsrEDYFZb4TS7ppWLz72CvproKLexdWm86D9hEloqf-WfUlkhxESoSq1pSexgZjbPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e913bccf1.mp4?token=K8k3aMFs-WSij3y14-wj1X45kz3vmnqfMA0oI9jNDpHk48Q9jC-SXkM8gMkz4eSGgiP_g7Hf7Tn1A7St2wNcY_do9l6W3LgEAnKtDe9imx1Y48awHfDdGis4-mJh_S86u3iLfQ_oPhmzZZp320DpgaNCiKRTvocM9VD2cNZqjsVCA1ps5Vxa48sBhFuMzehaIcMsSAjtrCzqQgFYKTCJfyEu4jvPJiMP_lh5o-Ie9GOS3Jtn2FYgcFqgcsYjQw0Dt4fl_rVfs2gHu0GTf6L1tOWbLj_pfKghMzSMNze-EiGkzxLCtQqZjGvBPaXssZt1sdyUM23aQsLXsGmu6HkhnzJVbsI565t4fpwpxwLTUrFTuAL_DyIQb2oTNCdojP7Dc4aCtJv_ksbAmOagvG-UJGK7IT9sfqrh3LYIkiHg7YugmLG0Ysq0iK75uMBmkGCGgaLjaobV4YEZrl51rC8FYxG-fbRPrc9TAcO4yKM23zvpUmTdb-3ABUICRc5sp31DHU0FAVPQA14qapXvCsoXYZO4IWQBl7flwfBKJp-oZ8vp11_NWgqbblEjvo81Ifq_T-IFTRNJtgbOM_VMmH2ewlb3ctrtGAnHu6fmtESDWMsrEDYFZb4TS7ppWLz72CvproKLexdWm86D9hEloqf-WfUlkhxESoSq1pSexgZjbPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ارجان؛ جام ارزشمند زندگی
🔶
«بیمه زندگی متصل به دارایی ارجان» بیمه ملت، پیوندی میان پوشش‌های بیمه‌ای و فرصت‌های سرمایه‌گذاری.
برای معرفی این محصول، کلیک کنید
✅
بیمه ملت، همراه خانواده
🆔
@Mellatinsurance_official</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/690676" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690675">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
الجزیره: روسیه و چین پیش‌نویس قطعنامه آمریکا در شورای امنیت سازمان ملل متحد برای تمدید ماموریت کمیته تحریم‌های ایران را وتو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/690675" target="_blank">📅 18:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690674">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
صدای تیراندازی و انفجارهای محدود و کنترل‌شده در حوالی بوستان فدک ساوه شنیده شد.
/ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/690674" target="_blank">📅 18:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690673">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a6facd2.mp4?token=q9zV9_s_SWkdh10mMg6JCPmHHR3kCZpyTMQ3IV4A7uPzZUNspbuyYbNvnbfYhMeEKLL4pnfE8bYtow31wkMkaVpD2Mb1AuFPnbOoQwYA3V5UJVRxC1yps6lDypHP9TZARkdBQ2qAldP_o52lrAesXqD77W39ZvWOl4Zd_3kriHB3xnuSMYMYR0NgDHrLHfAzqvddHjS1S89CCTlS699JcxEoa_He6pgG_zg3WHJOV4yuX21kYt_NL2KsWHIZoM9y5NDvNgW1dwecTMfaNBNPTV51kjfQBHcMmo57KWIdt8eXO10qx3Jgn0vwRSOd09dZOKQiIG2Y0ML0mOKP0m0H8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a6facd2.mp4?token=q9zV9_s_SWkdh10mMg6JCPmHHR3kCZpyTMQ3IV4A7uPzZUNspbuyYbNvnbfYhMeEKLL4pnfE8bYtow31wkMkaVpD2Mb1AuFPnbOoQwYA3V5UJVRxC1yps6lDypHP9TZARkdBQ2qAldP_o52lrAesXqD77W39ZvWOl4Zd_3kriHB3xnuSMYMYR0NgDHrLHfAzqvddHjS1S89CCTlS699JcxEoa_He6pgG_zg3WHJOV4yuX21kYt_NL2KsWHIZoM9y5NDvNgW1dwecTMfaNBNPTV51kjfQBHcMmo57KWIdt8eXO10qx3Jgn0vwRSOd09dZOKQiIG2Y0ML0mOKP0m0H8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه گویی نماینده بحرین در شورای امنیت: ایران و نیروهای نیابتی‌اش منطقه ما را به هم ریختند
🔹
نماینده روسیه در شورای امنیت: تحریم‌های «اسنپ‌بک» علیه ایران هیچ وجاهت قانونی ندارد
🔹
نماینده انگلیس در شورای امنیت: برای اعمال فشار بیشتر علیه ایران آماده همکاری هستیم
🔹
نماینده چین: با انقضای قطعنامه ۲۲۳۱، بررسی پرونده هسته‌ای ایران در شورای امنیت پایان یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/690673" target="_blank">📅 18:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690672">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G24qNOHDY3pV_nQyqrYzJkZxNXiD9ysX0Nh3ZLFwFU98DtxwIE1hm6MDvT9JaLz6PMGHbR4_CX7Uwja7HqaqU5nWlpTgaUJCGfKQaNVY2PPyJ3giZlUjFV22-xGmaboDzUBYkd3uFfWdIfqS_KCC2aGDAtBBLpjfFZpCUkKXEkd-v80vxj6IIpBSd1PW2O1q-QDD0Mbgs9RjDnyajBWAhfNsdC3RyKn4vXYSeMUWr1eG0e-emshrODGEROfEaP7LrMNX-sI1oEpp-ggyrG3L3osbahJIXX2cPrxzI6Bx7uVdRa_h80-IbmcWvpoYPTRL6KqHANzncwCQHWW16Yy9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه‌ توییتری استقلال به پرسپولیس پس از رد شکایت از آسانی
🔹
چگونه جلوی فوتبال بازی کردن آسانی را بگیریم؟
🔹
خطا؛ چیزی پیدا نشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/690672" target="_blank">📅 18:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690671">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab06e42f5.mp4?token=lHgn1f8lzJp-vyACiuXB_Azyq8aA7FTOhLQhvl9mPDhv8jKUX_r618_PE_l9Pv4ub0WrIBYX_p9cJckriTrtEEIG0er89PDEHgMXQRB8OIDd2YypvNTVcjhAIM122INmE1YQ-TyPdfrqhmKk-FP1P3f2YGxev78fc-qeefUT8w6ece83Eo4wqYMjKdriGdugS27itNkGBq6Jf0VupZpZC0XT20VdAcq4GAOKpH9vs9hdc2OaHVy2TuwbCeYpI4w-ZdtgB0w5LuZugpIQox-pKGxKrxBCO5lH9DOxjigqY05rTYS5whDOLl6dKwmLGyuHrMpZX5YTIf8t3cM9b4XOGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab06e42f5.mp4?token=lHgn1f8lzJp-vyACiuXB_Azyq8aA7FTOhLQhvl9mPDhv8jKUX_r618_PE_l9Pv4ub0WrIBYX_p9cJckriTrtEEIG0er89PDEHgMXQRB8OIDd2YypvNTVcjhAIM122INmE1YQ-TyPdfrqhmKk-FP1P3f2YGxev78fc-qeefUT8w6ece83Eo4wqYMjKdriGdugS27itNkGBq6Jf0VupZpZC0XT20VdAcq4GAOKpH9vs9hdc2OaHVy2TuwbCeYpI4w-ZdtgB0w5LuZugpIQox-pKGxKrxBCO5lH9DOxjigqY05rTYS5whDOLl6dKwmLGyuHrMpZX5YTIf8t3cM9b4XOGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در انگلیسی یک سری کلمه‌های جالب داریم که از تکرار دو کلمه شبیه به هم ساخته میشن و خیلی کاربرد دارن #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/690671" target="_blank">📅 18:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690670">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24536a38e5.mp4?token=pZ-EQbd7enxT0_VQbPf1kGREGkt0eB4sSZIPs0XMgxFIxvwRDTnSOJiaHnRcWKUboqEkf8S1QM6WtELaO67RONc3RzvvOgOk-UsrtQTbppKqOjfl0JNFDH1KOmdH3Ww9PdV-cQLusvTlWwLPKGh_V1YBxnNAtXmV0tSxu0YROnFDNEh6I4EijdMnby2sT4AWvO15NPg4en6tgBXn29JR-RQsRX6Tpmxk6oVaA14hQi4UCrXotQ5N5aKM5dt9Jx5vSb2L9o5itsVs5d-aNeHYOk5-cA7Z_uV4OfJDy4vpo2e1QanC_qJGsVerX_24bvy57GoC-ns64AUCddgx1fL1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24536a38e5.mp4?token=pZ-EQbd7enxT0_VQbPf1kGREGkt0eB4sSZIPs0XMgxFIxvwRDTnSOJiaHnRcWKUboqEkf8S1QM6WtELaO67RONc3RzvvOgOk-UsrtQTbppKqOjfl0JNFDH1KOmdH3Ww9PdV-cQLusvTlWwLPKGh_V1YBxnNAtXmV0tSxu0YROnFDNEh6I4EijdMnby2sT4AWvO15NPg4en6tgBXn29JR-RQsRX6Tpmxk6oVaA14hQi4UCrXotQ5N5aKM5dt9Jx5vSb2L9o5itsVs5d-aNeHYOk5-cA7Z_uV4OfJDy4vpo2e1QanC_qJGsVerX_24bvy57GoC-ns64AUCddgx1fL1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جدیدترین بیلبوردهای شهری تهران که واکنش‌های زیادی در فضای مجازی به دنبال داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/690670" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690669">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
الجزیره: روسیه و چین پیش‌نویس قطعنامه آمریکا در شورای امنیت سازمان ملل متحد برای تمدید ماموریت کمیته تحریم‌های ایران را وتو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/690669" target="_blank">📅 17:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690668">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346fb64e2a.mp4?token=RZFZ61nF0nxU4A6N0_KutTpICGaWBhPqB2u-T7Q9uFTfRGhvvbd1484Xf_qNK-WPdo6vWC6NwTDImwMIHtkRIGRpFKTMvldD_KHQpMW7rEU_2OEyxIlZk_2TNCSGSQcYsNQAnzIey9qFvGPb-In0jNLXPTDA_NXlvJzuZUgVmrJvEV8Nb3EO3aiJp9jTpct0I9rDI-AKJu8AhTyjXbT8SxOOaSCB5vdYtg2HwwTxFjE_piuAbcnK3NEw6e6yiTIoVQaiMpTe06nFP5k3CcFX7iNwCijVXhCyTnteYDrnbRTb0WEXyDk3kv5RlKT-tHm-UHuFT4aS2NgnIeqZUMHGJ1VonhaxehI-tH64TgFSwxfP057fvL_ur1JjxW-2HHumfolRK8G76Ll-he2Z91Lc4NqXGrLH9pGC7OyXAJolr7IxkrX6khThUT4f8YyLIQfntRzyJxS6K5uSUvuGU_-uM1KwpEygEyRhgunt7nbOjE-ZDp_rT2dZB9_BvHNca70Lezg93H730C-4pxGoc_oZyvXj3QwedmhngxijLxHcBPrKnBTs1OCbgv9E2nUCaL1Llm6zBkAZxggtxoBLI28z6sdOIkdZWqcCzPo6jmwTCqea_jGHxfkiVkJSl405CyG5P9TNo3FX39q_xihLSJAemhC0Z0KUen3jdBFZ1rr0rnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346fb64e2a.mp4?token=RZFZ61nF0nxU4A6N0_KutTpICGaWBhPqB2u-T7Q9uFTfRGhvvbd1484Xf_qNK-WPdo6vWC6NwTDImwMIHtkRIGRpFKTMvldD_KHQpMW7rEU_2OEyxIlZk_2TNCSGSQcYsNQAnzIey9qFvGPb-In0jNLXPTDA_NXlvJzuZUgVmrJvEV8Nb3EO3aiJp9jTpct0I9rDI-AKJu8AhTyjXbT8SxOOaSCB5vdYtg2HwwTxFjE_piuAbcnK3NEw6e6yiTIoVQaiMpTe06nFP5k3CcFX7iNwCijVXhCyTnteYDrnbRTb0WEXyDk3kv5RlKT-tHm-UHuFT4aS2NgnIeqZUMHGJ1VonhaxehI-tH64TgFSwxfP057fvL_ur1JjxW-2HHumfolRK8G76Ll-he2Z91Lc4NqXGrLH9pGC7OyXAJolr7IxkrX6khThUT4f8YyLIQfntRzyJxS6K5uSUvuGU_-uM1KwpEygEyRhgunt7nbOjE-ZDp_rT2dZB9_BvHNca70Lezg93H730C-4pxGoc_oZyvXj3QwedmhngxijLxHcBPrKnBTs1OCbgv9E2nUCaL1Llm6zBkAZxggtxoBLI28z6sdOIkdZWqcCzPo6jmwTCqea_jGHxfkiVkJSl405CyG5P9TNo3FX39q_xihLSJAemhC0Z0KUen3jdBFZ1rr0rnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی فداکاری، معنای واقعی شغل آتش‌نشانی می‌شود؛ نجات دختر ۸ ساله سبزواری از عمق چاه
🚒
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/690668" target="_blank">📅 17:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690667">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
رهبر یمن: دشمن سعودی تجاوزات خود علیه یمن را با پشتیبانی آمریکا و نظارت اسرائیل انجام می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/690667" target="_blank">📅 17:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690666">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJAhamEJ37QQRiYgWATgcmeBh0uOspKMndORr_zfHDWX_UprnkXp1aN9ugorZZSqYAac3KzLyCuFL7UW90zQMWc-QYtfwgt9IHM8JQE-peO6We37aANeIhhsFlY-pTA9csVlgJROmI-k6dT9ad3uWQHtnN2WyzbBI2Ja9GhTtMQYBVDqqskmt6CQvgGxptcWFZuFRYXI4eJNR2jGy_B6Xp-f5tOwlXz11O6b5lSjNeT3bdmk0cL9lLzrgTNuAJRYZJfEVhYszv5gFDI6uZIu3QQIpTCve7ssI1nQsC6hitYCVNKv6NRcbEO6vxWeB5zCDykBim_jw3COoEV11OBaFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانبرهای کاربردی word که باعث میشه سرعتت بالا بره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/690666" target="_blank">📅 17:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690665">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fd05d5a7.mp4?token=QrfGIa71r-i70lsrXuR4FZyQ9eB7uPM750KpalOlogd7JF9k7AYGRtkyhCJpt_p1Tc6oWiehNMahIx-GOBmheusy6jfRgOZ5AaBWMA0-8c8a_sdtnE6Jkfq7Cfq7KcgvxGWaElkB6xJUz-cOk8ld97Wsv_uj7HsFleYx_8fJd18LZR1V7b7wyIzHmkXIO42oc_Fr1UwmNiGiDidyZkFizLE9v5VhiVYu0clTu84r--aju7At0mQa8oo8U1sd8Qs63KF8gna9uI6QdEZAkC3T0qipQuzxJuef28vw0XS7PfYNJuUlChLPihyNz3hhe92wg-11X1hLcMCWPIZnXnLIFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fd05d5a7.mp4?token=QrfGIa71r-i70lsrXuR4FZyQ9eB7uPM750KpalOlogd7JF9k7AYGRtkyhCJpt_p1Tc6oWiehNMahIx-GOBmheusy6jfRgOZ5AaBWMA0-8c8a_sdtnE6Jkfq7Cfq7KcgvxGWaElkB6xJUz-cOk8ld97Wsv_uj7HsFleYx_8fJd18LZR1V7b7wyIzHmkXIO42oc_Fr1UwmNiGiDidyZkFizLE9v5VhiVYu0clTu84r--aju7At0mQa8oo8U1sd8Qs63KF8gna9uI6QdEZAkC3T0qipQuzxJuef28vw0XS7PfYNJuUlChLPihyNz3hhe92wg-11X1hLcMCWPIZnXnLIFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر نوربخش دوبلور ۴۴ ساله بر اثر سانحه رانندگی از دنیا رفت
🔹
او به جای شخصیت‌های انیمیشنی زیادی صحبت کرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/690665" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690664">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
آمار مشارکت هر استان به نسبت جمعیت در پویش جان فدا
🔹
زارع؛ سخنگوی ستاد مردمی جان فدا: استان‌های تهران، خراسان رضوی، خوزستان، فارس، آذربایجان بیشترین ثبت‌نام را در جان فدا داشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/690664" target="_blank">📅 17:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690662">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a596aec23e.mp4?token=ZyNXLXeAi4fJhvoDmWfoBwKITFb79Yb6j6f_giM2y2vhigWZffaou4vTPn-beqOCsIjM-yRMzh_NjGeGo7ucChi-LbgloYLwAv34SEF8PP93zg1nWS--oonfHQzl8CHMSbKXQAAIlRU5N5cs4IfKf5HTDR778QYTEbwQl8zfnlovqXgJ0Mj0ucFCTVncJmB2Zgam1vZS_vpsCegj2Y9n873L4hu_6KWHaDR6OP19UFQWoIuXL6UdfIhrv9RKDzblfKpyBduHms03Aj-E6myk1CWTFf25Hp9Ui8-4MOqgcR6C5nS69mle-cQeO2pttdrwzXJNdUhPN7OrC1f9JSHSyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a596aec23e.mp4?token=ZyNXLXeAi4fJhvoDmWfoBwKITFb79Yb6j6f_giM2y2vhigWZffaou4vTPn-beqOCsIjM-yRMzh_NjGeGo7ucChi-LbgloYLwAv34SEF8PP93zg1nWS--oonfHQzl8CHMSbKXQAAIlRU5N5cs4IfKf5HTDR778QYTEbwQl8zfnlovqXgJ0Mj0ucFCTVncJmB2Zgam1vZS_vpsCegj2Y9n873L4hu_6KWHaDR6OP19UFQWoIuXL6UdfIhrv9RKDzblfKpyBduHms03Aj-E6myk1CWTFf25Hp9Ui8-4MOqgcR6C5nS69mle-cQeO2pttdrwzXJNdUhPN7OrC1f9JSHSyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهد انصارالله یمن در حال حفر خندق (حفره) در اطراف تنگه باب‌المندب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/690662" target="_blank">📅 17:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690661">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
متکی، نمایندهٔ مجلس: در این مقطع نباید از مذاکره صحبت کنیم و نباید پیامی به آمریکا بدهیم و پیامی هم از آن‌ها دریافت کنیم
🔹
دیپلماسی همیشه به معنای مذاکره نیست و گاهی دیپلماسی یعنی مذاکره نکردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/690661" target="_blank">📅 17:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690660">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBPlFBCHAoBxC-fVWXdNuRnmfPWwi-H-hk6_Tzmj8_Lf89BZPCkxTMcN6fXyJVnIFnda7DQa8ngrgCr42FuYHyrvd3oCLhKseLvilZ-hsarxJJYa10jOcGPknI1Bbkeudm1C8oomk3F1ZZkVo1yVhZuVltEL7T7RRMvYYTrtdq80NsxtiUR6bxObHK08tcW7cTyDvK4g5__RC7vvpk_J6fdWL1gLZGqsf_MH2UT07RDK9yyrmOqgnzxSG7ttMPXZVFnGL22EOXrkJV2t0IljlKHxa_G0G4211_f_ziOdxvX0Mqw0BOxZzYaYv_yemPKEaS5dy_qnuF54Xv_Eb-Ufow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: آمریکا برای مقابله با ۲۰ موشک ایران، بیش از ۷۰ رهگیر شلیک کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/690660" target="_blank">📅 17:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قطعه‌سازان دست به دامن دولت شدند؛خودروسازان بدهی خود را پرداخت نمی‌کنند!
محمدرضا نجفی‌منش، رئیس انجمن قطعه‌سازان خودرو در
#گفتگو
با خبرفوری:
🔹
برای وصول مطالبات خود از خودروسازان دست به دامن دولت و بانک‌ها شده‌ایم، چرا که از دست خودمان کاری برنمی‌آید.
🔹
قیمت‌گذاری دستوری باعث کمبود نقدینگی شده و راه اصولی این است که دولت دست از قیمت‌گذاری دستوری بردارد تا خودروسازان نقدینگی لازم برای پرداخت بدهی به قطعه‌سازان را داشته باشند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/690658" target="_blank">📅 17:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690656">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز به نقل از مقامات آمریکایی: چین می‌تواند از طریق جاسوسی در عربستان یا همکاری‌های امنیتی و اطلاعاتی با این کشور، به فناوری جت‌های اف-۳۵ آمریکایی دست پیدا کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/690656" target="_blank">📅 17:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690655">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
بلومبرگ: محاصره دریایی آمریکا علیه ایران بیش از ۷.۱ میلیار دلار برای واشنگتن هزینه داشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/690655" target="_blank">📅 17:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690654">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223070706a.mp4?token=IJYSUkxZLZm6X2awbZGDc8vQvRPKcK1tiVQugJl5ogXsLHDGpxwhSCfkkjP0Mgp4wH6-fEwHuQacfKLUo7x8wos0zhGC0tVpKQrDO8abMOd4IjKMDekMI9knsbkrr9VUthvLGHwsDqM_GBWY0x-hDErJRhGyI7UUBYt0J9geeBx6tfJjPJNABuCHlxC1m1MNFsXPO-vnG-rgLXXoeSfrFyp6oKWIWZV8RyR22PadhZcNRQ5jCBUUFk5ZiI0NiwMEY2998a9vQVDAwuNVSqNb5MdUYerhbklaNvBZEjb_oYp-glcb18GE9xAPNytcvuZgHpT062tpZbaISGztnLSFIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223070706a.mp4?token=IJYSUkxZLZm6X2awbZGDc8vQvRPKcK1tiVQugJl5ogXsLHDGpxwhSCfkkjP0Mgp4wH6-fEwHuQacfKLUo7x8wos0zhGC0tVpKQrDO8abMOd4IjKMDekMI9knsbkrr9VUthvLGHwsDqM_GBWY0x-hDErJRhGyI7UUBYt0J9geeBx6tfJjPJNABuCHlxC1m1MNFsXPO-vnG-rgLXXoeSfrFyp6oKWIWZV8RyR22PadhZcNRQ5jCBUUFk5ZiI0NiwMEY2998a9vQVDAwuNVSqNb5MdUYerhbklaNvBZEjb_oYp-glcb18GE9xAPNytcvuZgHpT062tpZbaISGztnLSFIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از مصرف امگا ۳ چه اتفاقی در بدن می‌افتد؟
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/690654" target="_blank">📅 17:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690653">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرفوری
pinned «
‼️
خبرفوری/ رهگیری و انهدام پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا
🔹
پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا به وسیلهء آتش سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور ساعت ۱۰.۱۲ صبح امروز در آسمان  جزیره قشم…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/690653" target="_blank">📅 16:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690652">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQyDvw3Y-8lLtGkXdoiWgJMjLKZbYU5JeCdzldssK0Zn71uTk0ppJU9trpm3zHM1v3W38IQYJJs3s8qLITZdQsVH3SBMzEYSXIm4v3GpqG7cyu7ezb4xOXenAC7eAX1lPcrPQpt12qy_ena0J9jkEGu-HlUeBV1wE5t5-D82c1irJnAZbauDh_8Z_6B2VbQEx1TEOvv2yUJnRiX38FwWiFpKEmuK27rAZFlzKsKm5AOmUiGAujpnPJc6LJXIHP_HY6rQYJ6ECjVouX6jBICEIFy_wRfNJ3xTuAr5CNT0YVVMmepYaeRC5feuz89WHATOovzXDgio-q1gNy3ZiOxEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلنسکی در آمریکا محبوب‌تر از ترامپ است
شبکه CNN:
🔹
رئیس‌جمهور اوکراین این روزها در نظرسنجی‌ها ۳۱ درصد محبوب‌تر از ترامپ است. برآیند نظرات مثبت و منفی در رابطه با ترامپ ۱۸- است؛ درحالی که این آمار برای زلنسکی ۱۳+ است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/690652" target="_blank">📅 16:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690642">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYLla3Z3z5yRqT1yfGfy1lf1rdf6mMavHaLhzupozP9MsrZzTMstReekaOWfHglZsvCx2EA6npiMO4xUdHExwYz5hZGE_-awX6cIXuJj6sHBTsDiWTwbCAN6lCt8O8rLIzjEZq62vjUhopsPXRbAEytNuOSDui2pTSudIDmS6I1VQ6I7amR3-VgRHaiLrS1KeaGi86sfGpoKsKLquXbuy688jZd0U5BsHlbPXsXdY48XGMlKOYGkrg-57qn9NlX6MxZn1W_nkkRLyOk7VLyWEF5HzKbwQatdXRIYgjcENhW7SwQn7ctkH5ARWaD12LpAXdvFT0-M7oik9SdILlM8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaFyPZnOJ0rO4LaXGKhMmXD_mZh9f--FcMH1FEaqQZnRNPiXtCge98R4Av0qo253PZso6whJIFQjWC3gZkoXwrfqJ7gZeYG7oPEDWSbdfA7NXk0Gm4zrBfbYux9M2WJ6ATXJAAS2J5xTVwIFSS2sRo1XwsrEkUcpQQQyJWnHyVBCcb9seKhQetwv0dWfL_Nr9iyx2ZLC619RG3H3LUJaCdzCfwttFiQlmmANBxmNX85XUqpPGnt5ZA6xNWmWLETKXxoJhHvCBYB14ScbMcCgUtf8aaPadNZNP7ocUl4J_BRUR7eP3DTpty4riUrKLYQwg9AsbW2cIE3wrAYixL03oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfFmdXBlOg5QVfobqTJGLKPxCe3Gp1XP4IUECdKIIKDagm-5EsZ1barX_RIwXjxgpMcRpLcPVfK2E4NFZxNBoOegrHW761bAvoXD9haKW7hUGkp4gYgOeOihab1zhGv7a1vw2YzoAyDHWwTHN8pfYcLkJ-LisIVzXe5PouqodeFlJkGR1neCSckhV5jzlEkp_dZngDdfev1c9FrPL_7_hfgxYUmPsnktKdL7CkRgT3Wy4wpbSpn8gUKirkTyBou49hckZWV5Ilrl4FY8P5_e0XJPsKoOxyGZuvgc9BH3U_yOO4cXkpBt6g4hL6WqKnI-FdbjDw4lyg2OIPT0qo6kwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUbVSnGrvOaxS1edYP9dSLn9MQqyao1lna8Dtln-YdFpbH8adokmyLxSgGJzuQ2VrIoot60s6SSRSeG5wgLB89xwTEVNHLFCeEgAL2wYPnYhFs3obk_yWapPR3Nfib2mn3OgdbYW9NU4DD7GwshSJcioodFswU2Z2dsF-maZ5JZC5uRm2IuLF1zbG8yi48dY9gjhv4Q_iyr7knkJjHxiQF0xvorFPbuk20LzxYMtmIQoQLMnDkKE0GdEM6coeJZMxKybrhT5c4MIOJENwHcZZNtikpbM2T4t5wxX8eHA04fhnb8gVk2K91BGzg7NtRCxf6cMkDrQca9yX2GQz2nu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_K2sQPkDEn_hrrc-c2E5kCB-Tnc3iDxpPrdnhaRCg5WCJiuNRuv6K0VOIzD8udfJcV2NCpUJO2kFSc6v9kMooHQjrSt_8vqHMuff1hou9NJClYlIv25zx3Qd1dp3kmq49IReU9RvY3j1jikKTbKssX0d7JCBpMrjPgUii8dSyf1uLo4QoLdnVXN-wNgBESmfGKSdbE0eSfpwI1oBPJ5I_1xNZI87RA7ooYIF6rPWCRSy-87JzeD9DOKgMHu4A1FlwdElh8vLNqThscc6ELIPpnmL27NxTjU99WZej12IgQeGbyqFEs3ujCgA6DfWQum2Ori_f5D26ni51IpQoxvVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukH-rgihIka_nhTAupm8D-Nz7uYlPpvTU_zQ5cdsN1-BFttW4xNhT5OuR2swKyZcfKQa3rXDQ7HXxCf9GyBIr4Pg1EDnkrA7rH0qIHSJS2fMPr8Y65D4RsTGQ4hDV2eAA6AHFJR5yadMnZjefIkOiM_ppKkmtPvx6m7LwNG0aVxZwaz5qZrXYuNt09IMv9oV4DIYQ7U8nTZYiYemu4DHiO49sHHVlJa5YD7zF7lb4IscCC01n6TaYsOPBdKE30ubqEfMGdpIwsHmBWRvXp2a7kTdm-jXRmfJquGfCTMjeATNdWDY0GMfn5SJxJSdt7mpcDUdiRk2P7w8-jUci6LVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5rQPiYZUkRH2VMqEk457C0CA90GTTsdBnl661wL40NzwYYjZXOfp7K-3uLxU3oUNrXl2VHnYk6THPHJ6o3Cgxsc-vJLIReLn6wdyBWLx8qpfpalN7IP33fVubnxMjmZzZnsrn_LAdiUn5suBSrI77bTJpwspi9whC3G8XnAx9QUas1g5FzGCA-g6VFeiP106u4J5yrBXJbHgMkIAq_N2p_qYvuFAYq0ll-wBZFNxznDetV-QwhNKlUVmvWbGR1ue3BfyuW3v8kALf0xGAev9qqU5m348YGK-MP-tMoQrmQ3qqFSSvLo3gJYN2ozPWTcnvQBoxJ8CJp7-vrEw8oITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kermSMDvlQ2LrE1hVEZXD44kKVo76QkO2ZahC6R6pEAZZC37rCtIocUAlAKn0HaoBBQNGoumAfWBj8AT-Sj6U5Aq4azavS9lAjQ5oX3zBbe0U9SoKK8Q5VTgekPbngwIOZAnfe6PLa0VVCNMCjhtFadTXMsZFJeTK93W_VUVOTGouBtE380SlhMnB9mVq6TidGMe-DCfGCroibvSskQowARe2agVqDmY3GGqKNSxD6Om831RKiTLZ2qS0TvKpDXKAE8vQ6YL54RHsUPzj1LmCz9HRDWeXX9Ncc0ZgezA24zPWQz2iiG9tBN_kkmjS1Fbb55nOU0MmTE7HZvQIi0Tjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gi_A-baDoTld80YyP2LeN3zbMOdmXHnmTpcZlULLn4YRaMq8HHY9yJSW1EVBnitchJ1VHRpF-gagUauAtGqzN3xZ406ztNKdMD0_EcqajiySSj6VwBUCbwM6TTsOWYgV7FdTCRjMCRsVlo_s0KYOu1WgBtvs0yD4JvBkWhkbCza4nfyanwJNa9O-J2s2sEE3_B52CHOnLbK_jJhA64PRvhWDcr728_2UCPUrbnCa_2R0NAD_ck5XigzDrJOjE7e1JZjFu7JLOMgRBZXXChMgy09KrSNBxI9-Jz72Vw_J96R-LMjduudaBYUDKhImuiSFMPMh2nI6vqogX9UTUIRPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErbcVtsLy5KMR9Mv4atOJMiqzYingw5jS0rJVv47i0f21QAwHO_t24pWnNiGdB2_TLXNV2i3BoxCpgmILU_gJCc7OTfW2cmWQKAl3XTWrXWghOpYSh0V-XNer05c9IFz5jr7v2gos0vLmmuAE7eMFh2gwo3YTGCfVswlfXIpMIgetyV_6y-al2LkZ1H5pvQi_fk5KktE9r9aGFa-xCLzXvEswAU5b2RIWetxqYxhnPkVO8sfo-Sp9O_9s4ywkmTQbx8h3xfbXIOZgtDmPN-5IkDNmXVOo7GTVsVpcqkCybwbBtzFCSu2cWIUxk3yXLVjL11WZqN8_a1vP-V1860gdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
روایت دغدغه ها مطرح شده از سوی مخاطبان الوفوری هم زمان با آغاز سال تحصیلی جدید
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/690642" target="_blank">📅 16:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-tcoo-Bn5UXqanpw2P5jB8fiRKg1csafdQso1caL_CxqF0bkEZF6oQv4jYVf5E97jx_6qUmLqhsuOAaOeILYnTL9rpNKhvOhJmbiyCz8QLXnNpu1p3mYQWH7-7nJN-qvpbS2WfburZ_fn4l6giIZnoxZiuDcgWCti7NBCO8M5oNLW_qSOoDlhtcvWrVgwTQBgvtYUwCTUcd4-0BT8sP0LJwB-iZcBMwTkn9aEbc-q1V8PCLKjogrXOKbW5ycnv-Rt-Eocm_CcNouNL2Nw9MTj62BsJ0SxzKIB313KM2qsZFtxYds9OwbIgiykN_VUN4TVeW06gPpYwXViqq0NChpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdGJggK5iaahHxT-sz5DQ_vsFT8KuHuFB4KDjNtP0NLVKITLJFI9WYzxf1UXQRbabedaDT_AiIkiHwl69kHnmtaLl1BG5sFlBEq3l5lSa73BIVVG9d4Ois9PR9MlS8UpRmTlzahQB6EZaskQ8r0g_t0bWt_HYCwZ2GWueGdv43U12K6vIgWBKQHF3AxWj51PWOFFaxWaulEiSA-0T5oPLoVCnz9A1FDODmVIyDn1folz-vXQRjktZaLuf-4YXXKQKhPMzXq9C2eV-o9yiyoEtgpJRpGNZ238nm7Pfr5RsRgBggOCeTTEflOQETTM3Kf4F8KfgAkJJuJa5zPIvr3qzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عاملان رفتار نامتعارف با متهم در تبریز تنبیه انضباطی شدند
فرمانده انتظامی آذربایجان‌شرقی:
🔹
ویدیوی منتشرشده از رفتار غیرمتعارف با یک متهم مربوط به ۱۴ خرداد ۱۴۰۵ است که پس از دستگیری فرد مذکور در جریان یک نزاع خیابانی رخ داده است.
🔹
مأموران دخیل در همان زمان، طبق مقررات انضباطی فراجا تنبیه و «انتظار خدمت» شدن
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/690640" target="_blank">📅 16:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwAJ7LGSW6_KFQl0WnFt7OMPgNZKaAnFnR-jupD5ts2WHQH8AfwpVidL2pU6eMwtcCyUt6Guj9yt6PFhDYE6VIOKOM_h_XiH7JdhllmyIlpdooQmcrH-qWwlPAoRxnfVTcNVIb5RSAlvMGimOdzExDf1joc9aZADiuAQGpv3VKkO0A9LQS891XwkGDfPPP-A4jGZd9TbPoA2K_b5XsbAwJfwpfOH3j84F-jjBHknOxhaOHFtOzdrMaq9huljTYkvBbyWVSd108OW4epbEO99QRuUFX4DzNOdKnVp4b_sBipSVlcT73zZwgAh6JEouSMNp14VTnCYz-rQwDUkNO_UnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت ۱۰۲ دلار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/690639" target="_blank">📅 16:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
المیادین: عربستان از طریق عمان از انصارالله خواست آتش‌بس دو هفته‌ای برقرار شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690638" target="_blank">📅 16:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNT6O5JAALEz-dKXK8a5Qq7ufn6ao6biJ13IQU4FfaunMZRhJQYv4K8ns-w6TlHgGWLl2HuvkpEIHn2_V4JKHTcLtKhTKIZd2_18C9SvByJjcTSBgZlL3xFBndjbTdntmjwns6t2ESmlD7i-KOtEd8C-QQKFlkGaLC5t1VNBF0bgZhKlrT4NJFFRY-U3-VxXb95Nw2HjwDukJlm6eUPjCCdIJYJ_DyoP9lLOg-40tOKkJK9qRfvXBnG53qxovetYyg6PGR5whoW-4aEpEdNZBTRoTYbwaDEtM0YGgIGsTgrLKbfljAp3u9OhUaH2K18d0WhdNq2B_1XtfopwEKiIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوسه نادر با رنگ‌ نارنجی در آب‌‌های کاستاریکا مشاهده شد
🦈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/690637" target="_blank">📅 16:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
احمدی، عضو کمیسیون انرژی مجلس: کارت‌های سوخت جایگاه‌ها به‌ تدریج جمع‌آوری خواهند شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/690636" target="_blank">📅 16:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مشاور سیاسی رهبر انقلاب: تا به زیر کشیدن ترامپ و نتانیاهو، تنگه هرمز را نخواهیم گشود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/690635" target="_blank">📅 16:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0629df4d41.mp4?token=F8gElEqYEL0BImC3sz2AJmGiRzm7aUWab3JoqNqtxdC2W6rdOTBSSG5z4YVxzs7q8gbJVEp6Jq5bvkgepgT1QLsMjt4h44bjr1lNZXtb_FwdPs2NIZcYCQXlZ7AQiKrwreDnCvWyMvi0gsPY5FqsP04F3sW_Yyf_nfQP4kfjtTw5RFgURA8oNIywOwvbzMTz7n3c_dginkx3mGE03EZUICWbCvF4RXTx3dN7OU83im1TUqYjmaxTHcOXpn4j6CsemOYgnibVFo_osQmQHyeYkoZcNF5_axH2PgaXiDXWAlJ-GSJt83-RdMk1BSi4LYRd9y-ky1pPsqxFy8q6wIP1r6wGHKZBiP2xbt5sTZAutNwjGOzHu0Yc3NJTAK5ziHGuJrFDGKAUBpamslOnRPl9ltriyVp_qMAvhsaIK1PPloNDBX3oDV4B-L6cLb0di0eRUYjTqgruJ4Vab1QIqdmYYEFQWeuTO7BVLAUTpy_QYlz7XHFl2nJ-dOqyDYCKTz6UHh_LP6Xli9ede9DdzTNuSW4ZahQnfqzYxs1zd6di_SK0VBmVR7u_QHcVyHQm6pRo42DylrRQQ9TOKUbje5nxeyfB5h8mFIVicQsRD8fAWoTzg9yt3v_FOpjglV7zlARnJSmOibjBJLjQIZdgvhiwZG5wmza_6za0vhCkQO2DQQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0629df4d41.mp4?token=F8gElEqYEL0BImC3sz2AJmGiRzm7aUWab3JoqNqtxdC2W6rdOTBSSG5z4YVxzs7q8gbJVEp6Jq5bvkgepgT1QLsMjt4h44bjr1lNZXtb_FwdPs2NIZcYCQXlZ7AQiKrwreDnCvWyMvi0gsPY5FqsP04F3sW_Yyf_nfQP4kfjtTw5RFgURA8oNIywOwvbzMTz7n3c_dginkx3mGE03EZUICWbCvF4RXTx3dN7OU83im1TUqYjmaxTHcOXpn4j6CsemOYgnibVFo_osQmQHyeYkoZcNF5_axH2PgaXiDXWAlJ-GSJt83-RdMk1BSi4LYRd9y-ky1pPsqxFy8q6wIP1r6wGHKZBiP2xbt5sTZAutNwjGOzHu0Yc3NJTAK5ziHGuJrFDGKAUBpamslOnRPl9ltriyVp_qMAvhsaIK1PPloNDBX3oDV4B-L6cLb0di0eRUYjTqgruJ4Vab1QIqdmYYEFQWeuTO7BVLAUTpy_QYlz7XHFl2nJ-dOqyDYCKTz6UHh_LP6Xli9ede9DdzTNuSW4ZahQnfqzYxs1zd6di_SK0VBmVR7u_QHcVyHQm6pRo42DylrRQQ9TOKUbje5nxeyfB5h8mFIVicQsRD8fAWoTzg9yt3v_FOpjglV7zlARnJSmOibjBJLjQIZdgvhiwZG5wmza_6za0vhCkQO2DQQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریجستری موبایل؛ هزینه‌ای که بی‌سروصدا گران شد
🔹
در شرایطی که خرید گوشی موبایل سخت شده، یک هزینه پنهان و اجباری هم وجود دارد که گران‌تر از قبل شده است.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/690634" target="_blank">📅 16:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfdabf7cc.mp4?token=WBk7Pm-l2WPINDVmlsRpurc19-QvjSQ1q0rH57fsQEufU7ClxwVBBcqW_nmvIJbTWhMH3dnjGvM5Ll4PC-O8Phx7uMDFB1UcUuBRL7-wz7PI64J15a-6l8Ko64j42aVUyZdsMYMIRJcw9RY67UGgs6bx6ACnYkBQy4HFdK1a9o9Dt8dOV11CKRtEnYydRZtVFDWRuq_ZBVMKXv6x3J3tVNrJTZRTldI5A9v-BJ6VoZ3ztsMqJQI9YsTUg9GhOVqJorlnHXUtixavu_OGumAj4yN0qhJPhBm60mHmNnEpbUn6CTUPQ6qsR4fZAmlYZOjv3D8eG0WqgMfn95CvwHH4YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfdabf7cc.mp4?token=WBk7Pm-l2WPINDVmlsRpurc19-QvjSQ1q0rH57fsQEufU7ClxwVBBcqW_nmvIJbTWhMH3dnjGvM5Ll4PC-O8Phx7uMDFB1UcUuBRL7-wz7PI64J15a-6l8Ko64j42aVUyZdsMYMIRJcw9RY67UGgs6bx6ACnYkBQy4HFdK1a9o9Dt8dOV11CKRtEnYydRZtVFDWRuq_ZBVMKXv6x3J3tVNrJTZRTldI5A9v-BJ6VoZ3ztsMqJQI9YsTUg9GhOVqJorlnHXUtixavu_OGumAj4yN0qhJPhBm60mHmNnEpbUn6CTUPQ6qsR4fZAmlYZOjv3D8eG0WqgMfn95CvwHH4YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملک بخریم یا طلا؟ کدام تصمیم بهتری است؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/690633" target="_blank">📅 16:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e19e8cd2a.mp4?token=XloRrUPEsMzvRmgmFkGkXZgt8SiDPKgAhIUPLc57nqGWJMcAaaqOS6z73ww5JQAsmzCsecMKNIA6EFzQMdJmFhbMHQoqgax3uWMBLDZ0vg0T1YutD7vkW4B3tjhJFzVwRsfWputLNHGpDY24PwWu2NirAEi2Y51OyMMISXtpHFhWmNwX5LRFFjy_Zhx6ybJjnFb5OixSSYurf189EkQOVJmYEvt8EXu5Sy-A5zq0gnz42CCjgLOOenZ8EGwWI7C6kWl8pY6Hekl6p24KdkN9z8-MZY9q4OzuiG5nND6HI0s7xEoOF3sl6rg7P3DJyoPiOYfm581LZJjl3yEQAUr4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e19e8cd2a.mp4?token=XloRrUPEsMzvRmgmFkGkXZgt8SiDPKgAhIUPLc57nqGWJMcAaaqOS6z73ww5JQAsmzCsecMKNIA6EFzQMdJmFhbMHQoqgax3uWMBLDZ0vg0T1YutD7vkW4B3tjhJFzVwRsfWputLNHGpDY24PwWu2NirAEi2Y51OyMMISXtpHFhWmNwX5LRFFjy_Zhx6ybJjnFb5OixSSYurf189EkQOVJmYEvt8EXu5Sy-A5zq0gnz42CCjgLOOenZ8EGwWI7C6kWl8pY6Hekl6p24KdkN9z8-MZY9q4OzuiG5nND6HI0s7xEoOF3sl6rg7P3DJyoPiOYfm581LZJjl3yEQAUr4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی نتانیاهو: نظام ایران را سرنگون خواهیم کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/690632" target="_blank">📅 16:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIZhqJpgPVX4RHD-kRQO7m3BmeD3CijZZNCSrZv6IUYZoPSvXyLO2eXf18ao-rz1SXB-COX9vyiGD4pq7X42X07foy2cHH4IyN6jjLSEGZELyGGg3MKIqSVqd_Nv44S7M9t4ZPg8t4XYEV6Rxb9VcHcK4D0iNTkNrLUobqW6y7C0ilvP7FZ0a4qr8HVCsh7kPDQu56xq5DSKlxW26YZ_KdaUJL-SzfbFdGduHCqFLO-iPVYS40d9Iek2lxWVY041dw0OuUFOdA633J4lVNi67lfKXjP1e6UIOgLFltdLkB8nuvfk6tgwlgbtWweUVNbBO0RJc_vmQjcAc49G6xS4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشورهای جهان که اکنون درگیر جنگ هستند/ هرچه پر رنگ تر نشان دهنده نبرد سخت تر
است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/690631" target="_blank">📅 15:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پلیس فتا: در سایت‌های خریدوفروش آنلاین پیش از دیدن کالا، بیعانه نپردازید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/690630" target="_blank">📅 15:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690628">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQPn-M3GiBUIlY3vj4mUPyhSAw0PR4nMYHa_MAQT82mj8bftQyfHUL19cYR83OroyJCp_jlD8chMgRqcwMy62k0ZwqTqFWh9BAGgreLpvS8isOUkpBF08SGeAE2z6LRlE5gr7gc1vN7AW4ygr9BUSGlQPwrunL6GKdTkNpDzYF5ZRKEFc1BI0Ay2togGoH01nGJtWIIFyPtz1qj7RVVth7Joh652HWlW0ETBryrSD3Mb5Oo6foK6yiarbG1z9cf96xWCk0PADT7COJEgjjqep7su9hiFeQTpg6y4_f6Z1YUWOFMY57J5e2e1CKqC-4J1bwaJCZV40Pb2Zpyficxw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d007ce2bd.mp4?token=UoT--RRytwrv_fGXzC_DqtcWS4KIGryO4C7s4sdWpgMyf08z12B8GXkKptAnZCmI1leh3r-6JdcwkVu-SN_Z8YZn7U-FAoCyOXXjlUbkhp1Xeyec7LGBsaOVVEnYW83zovXBbYGne3SINZvrJ7OAHKJfFRm6mcD6K06VzyF3OS1xn_-0gKnsUV8-0xFtNfU3xAOgNxgltF6boPaNJcdLESKQl3B91-8lJflVRYVDvN_nvW2f80_l5CeO1Pye2hA0Bn6WcZ8UdNnUnsu0xRpZCYpucRW2bhJWObxNSNO4Arvq7RZzfp5eyI1RXdEEcr5esHGJ8wddERGsmIz8YUnMkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d007ce2bd.mp4?token=UoT--RRytwrv_fGXzC_DqtcWS4KIGryO4C7s4sdWpgMyf08z12B8GXkKptAnZCmI1leh3r-6JdcwkVu-SN_Z8YZn7U-FAoCyOXXjlUbkhp1Xeyec7LGBsaOVVEnYW83zovXBbYGne3SINZvrJ7OAHKJfFRm6mcD6K06VzyF3OS1xn_-0gKnsUV8-0xFtNfU3xAOgNxgltF6boPaNJcdLESKQl3B91-8lJflVRYVDvN_nvW2f80_l5CeO1Pye2hA0Bn6WcZ8UdNnUnsu0xRpZCYpucRW2bhJWObxNSNO4Arvq7RZzfp5eyI1RXdEEcr5esHGJ8wddERGsmIz8YUnMkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«قورباغه کرمیت» گونه‌ای از قورباغه‌ است که الهام بخش شخصیت عروسکی معروف بوده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/690628" target="_blank">📅 15:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690627">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cf4fe2cb.mp4?token=vXd45NICxr9f6oVQ4xdNcgDJ-sw7lAMW4GVwl2cvq2uhnXw0x8FOCbEo43E3lFStyMGYv1d-aORo3rOG5Wn6qeuc7qElhnXIZwGo-Yo2DOW_K81Dcc8eq0QpLahJxWcx9j28fnP38Glyi73H4D2DdisWmvIdXaJTKHJ4RHdwyLDl8ATIyQ8sm-oltQ2wzlkvnIjek60rbjNFWfb9Iu7Sx4Aofk0VtVsI6uQTKS0FM7ZFotSt7RLwkIhykl_s4KNWDFWAj3Nf53gZ9ZC9DlyA95D3cSDBz1GmUDQO7DGd7N_UIGVzyRONITAiDB3d7kDOJmdrygAk13KQMHmhzYYnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cf4fe2cb.mp4?token=vXd45NICxr9f6oVQ4xdNcgDJ-sw7lAMW4GVwl2cvq2uhnXw0x8FOCbEo43E3lFStyMGYv1d-aORo3rOG5Wn6qeuc7qElhnXIZwGo-Yo2DOW_K81Dcc8eq0QpLahJxWcx9j28fnP38Glyi73H4D2DdisWmvIdXaJTKHJ4RHdwyLDl8ATIyQ8sm-oltQ2wzlkvnIjek60rbjNFWfb9Iu7Sx4Aofk0VtVsI6uQTKS0FM7ZFotSt7RLwkIhykl_s4KNWDFWAj3Nf53gZ9ZC9DlyA95D3cSDBz1GmUDQO7DGd7N_UIGVzyRONITAiDB3d7kDOJmdrygAk13KQMHmhzYYnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب یک کاربر فضای مجازی به پیشروی یمنی‌ها: «اگر همینجوری با دمپایی پیش برن، مکه زودتر از غزه فتح میشه»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/690627" target="_blank">📅 15:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690626">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
خبرفوری/ رهگیری و انهدام پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا
🔹
پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا به وسیلهء آتش سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور ساعت ۱۰.۱۲ صبح امروز در آسمان  جزیره قشم رهگیری و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/690626" target="_blank">📅 15:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690625">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dg2SN-fnq5TKQmRINfrvxLKf_kxnnO94E6QY8Wcmz0ZcLVNn63RXhPedt3NyfHS1c21SizIQlsWVkoZN3iY7qJkGH6_sRwwbOw7wNP1yJefMaTMKQp5_Wz3bRB0h-GRn_lKxGnq-6uHju-iv5mjKX-6sG839eTHiw0zc5CK2wmiEt07bg4YNPK3nTPJYHl_Z0NefCl7_mlDB1zpuVB9oL9DnPV3pC7T6ja7gUqU2YunPdI4VvPrPG0UDnmwPOAdlHNrXcDThs-eZskGNGAH0_31CtsZEdG8lNWW-JGCaGIeEGcSdO5q8quJcR7C-6lzdNVpKb7YU3QlIkE8IUPsIow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«مبارز با فریب و دروغ»؛ لقب تازه ترامپ متوهم برای خودش!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/690625" target="_blank">📅 15:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690624">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf34568fe3.mp4?token=iVLd7i3F2gb3bylwHAjq8n507Kb2KTJRY2sEDHvdUTy1mlEjs8_z6bGkyrVwxtalQGyw5tritUnT-CF_ZkklrFPNST5DIau0KeyLVDtXwHeLE4XXM8qxlD6g4nmNhbDD4TXZlO-4K3BfJ3Zl88j4u-Y3VeGYBfEEXV4_Tu5fmOZFW7zb9re-Vy0G-gOPo1c1_aFIEify0Rq8qV7o3zWvAd8gCW3n1VJsQ8ecnQX7IpyjbQkRdiUHE-qi5NTCYfVPJzul9gn5GL1POmPE-fm8ImEXo87lLRBYrVgZCxR_Odr2RVOc0DBCMQWHDuhZ8ujSmjE2eXe0fP1YXiCXQ37LgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf34568fe3.mp4?token=iVLd7i3F2gb3bylwHAjq8n507Kb2KTJRY2sEDHvdUTy1mlEjs8_z6bGkyrVwxtalQGyw5tritUnT-CF_ZkklrFPNST5DIau0KeyLVDtXwHeLE4XXM8qxlD6g4nmNhbDD4TXZlO-4K3BfJ3Zl88j4u-Y3VeGYBfEEXV4_Tu5fmOZFW7zb9re-Vy0G-gOPo1c1_aFIEify0Rq8qV7o3zWvAd8gCW3n1VJsQ8ecnQX7IpyjbQkRdiUHE-qi5NTCYfVPJzul9gn5GL1POmPE-fm8ImEXo87lLRBYrVgZCxR_Odr2RVOc0DBCMQWHDuhZ8ujSmjE2eXe0fP1YXiCXQ37LgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکنولوژی جالب یک پمپ بنزین برای دزدیده نشدن کارت سوخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/690624" target="_blank">📅 15:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690623">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLEZTb53IgOHLONWYnXZhwTup_nltsK5jeajU3lhm0HViruEfJcWbRyBxnS5ok53ZAykPdcgFUHtD3pTFAcY2vO0MZY73GxtH-CfxbrLHFRtfEDYl-zh3mwCsm1omjq5Qn32fMz0Ti_7mCnRmUHoz9zvAmkK4gTyMPWfQd-P5itVy50xQ-kbYwNPiiXir0tU8UHu__CPIR2Xw7zLJDBV7hiwUmdsD1uP6FrBLPan8mubdJyGg2oJYtcFNh8Yk8lEHh3z1GhQEMhbzHreZZUtBS7lXneK9YktGAodeiLgx2A1_9366pfrnjo6hKHEd0mRl0xFnfG0RETtuJZB7LzjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهرانی‌ها با چه وسیله نقلیه‌ای تردد می‌کنند؟
🔹
بر اساس آمارهای سازمان حمل‌ونقل و ترافیک شهر تهران، «وسایل نقلیه شخصی» با ۳۳ درصد بیشترین سهم را در رفت‌وآمدهای روزمره شهروندان تهرانی به خود اختصاص داده‌اند.
🔹
ناوگان «حمل‌ونقل عمومی» با ۳۱ درصد در رتبه دوم جای دارد و «موتورسیکلت» نیز با اختصاص ۲۳ درصد از سهم ترددها، نقش پررنگی در رفت‌وآمد شهری ایفا می‌کند.
🔹
سایر وسایل نقلیه نیز مجموعاً ۱۳ درصد از کل سهم ترددهای روزانه پایتخت را تشکیل می‌دهند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/690623" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690622">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
هیئت حقیقت‌یاب مستقل سازمان ملل درباره ایران اعلام کرد؛ «دلایل معقولی» وجود دارد که نشان می‌دهد ایالات متحده در دو حمله هوایی در ایران، از جمله حمله به مدرسه شجره طیبه در شهر میناب، مرتکب جنایت جنگی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/690622" target="_blank">📅 15:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690621">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCvK6lno2JGlyxb9n8pZ0p146LZrJMETjWNQE6XIIWAFi3Mx5nru86fnScxILFIOno4Y1keI6XlhmRm5NUTfXsDV7OS-nOSbdWi5NZHiaHhZ1veYDjoYOYg2cbAZOfq7sD4R-qmNGxk2KYzNBqJY2P7HhR9-40QODj8DTTd9VeeAYAyaZb86O0xsP8_vXpoYN6K1Acanwp79lPhzr7tu6mwrIxtfdWQLjjDVBH0sjaWfjdZLyLADv2vrJgg2o5QFZirLUMg8EPUn9ry0rIE7OM-nRuwuGsUt4MRG5QkgEF_a-FoXkiu1qPe5Fb97cNBJx8pTsUjKu_trSFGUWf30PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسعود بهنود تا پیش از نوروز به ایران بازمی‌گردد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/690621" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690620">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: «توافق مکه» در صورتی که عربستان با حملات بیشتری روبه‌رو شود، می‌تواند فعال گردد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/690620" target="_blank">📅 15:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690619">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39774e207.mp4?token=N1jGTK7r2D4mtbWJ7I23mrTASEBI7aZpJ3L268tFZgBV6c2hIo8B-wJT9NdjVoUcZKO_i1BQqCxFhOiSCClQ2Ec7HU6AhSeZ_xygKBgbmmfjR0ajBFVj6FW08Hr3F_imi1P0jpXaMOzLi3kaHivO1TJcCUxgK3r7_nIlT9re7WsipLIKG1gaF-f0D30Uc1TC7U9IGLHYeMRBxOGLHV0KBX8vZhe6yoR8w7nCjGHH2uDHNlRlkacg45Mm7SB2TI9Crdj5iGXp9hp06w9ia2B9KgfBQzSunHNbtP_mpiSE1ucqT5ymg3k6BNVIUQpMwvLbAdg7fikYV8OAGx85O4iuWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39774e207.mp4?token=N1jGTK7r2D4mtbWJ7I23mrTASEBI7aZpJ3L268tFZgBV6c2hIo8B-wJT9NdjVoUcZKO_i1BQqCxFhOiSCClQ2Ec7HU6AhSeZ_xygKBgbmmfjR0ajBFVj6FW08Hr3F_imi1P0jpXaMOzLi3kaHivO1TJcCUxgK3r7_nIlT9re7WsipLIKG1gaF-f0D30Uc1TC7U9IGLHYeMRBxOGLHV0KBX8vZhe6yoR8w7nCjGHH2uDHNlRlkacg45Mm7SB2TI9Crdj5iGXp9hp06w9ia2B9KgfBQzSunHNbtP_mpiSE1ucqT5ymg3k6BNVIUQpMwvLbAdg7fikYV8OAGx85O4iuWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپی وایرال شده از شیرهای آب پارکی در تهران که برای جلوگیری از سرقت با بتن پوشانده شدند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/690619" target="_blank">📅 15:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690618">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b19e47999.mp4?token=FHRVaQkQOT__tAOaPXHq3Jzru-jBWcprZ81MBHLHbRxFm80HVS_L_U-HkGRkgVyL4dSqXWTaLpaQ7hauCdoBx4bYoCffVd8aR8gAv723XjEwRnjgoFmV21ybp1ZoFUjxas72Yta2tvNecjPKHISRnIXBsIdLz5PQnVmw5QUzJRGtuiJLaRpMay81YYrT_MFHM8r1mV3OOkMD0YsBrh_CSgw08nMxwPlfekSLo_oLOJ3dOBeNphi7l8Dp3BN7y16gteKLqhkCaFIsaYYZ4nlhH40_NPxymEPkiodNaTlne-Lm9bdDfF5tvijEz7Z417jIKpoLltKGrc0mLZVvPURP5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b19e47999.mp4?token=FHRVaQkQOT__tAOaPXHq3Jzru-jBWcprZ81MBHLHbRxFm80HVS_L_U-HkGRkgVyL4dSqXWTaLpaQ7hauCdoBx4bYoCffVd8aR8gAv723XjEwRnjgoFmV21ybp1ZoFUjxas72Yta2tvNecjPKHISRnIXBsIdLz5PQnVmw5QUzJRGtuiJLaRpMay81YYrT_MFHM8r1mV3OOkMD0YsBrh_CSgw08nMxwPlfekSLo_oLOJ3dOBeNphi7l8Dp3BN7y16gteKLqhkCaFIsaYYZ4nlhH40_NPxymEPkiodNaTlne-Lm9bdDfF5tvijEz7Z417jIKpoLltKGrc0mLZVvPURP5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجاوز هوایی رژیم سعودی به منطقه الحوبان در شرق تعز یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/690618" target="_blank">📅 15:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690616">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhZhD-Wep_nNmUYJMbnwtm2Nv5JlDK-uE3YjHZiW944IKDJnd108aLyWbgp0FHWDpbU7dlUet4JyBhX0UMPrmqK8IoVj44KfTYVFL92sSpGTpQ-MdENvHtkt_xLdPPZ7yfyVEl1ezzohBo_wxq3KhlOctVeH1h7SqF1IAvUKTll_zmLushOLJ1NkeHaOxYUJcPCja5AtfqxTZ0_kP5ofsKTlu4I7-4A-wagDB9QWtm3mGkseG5FAbW0utUjXV9X_hC5XzwieMF-i9gt9M5K0RcM-147t-A8mUgHEQzjSrn7L7FjtgNyYIWeXgquHijOYNaiCSTO_tZfctcYtuSqqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMTiu4gkx3vyo1EYqPb4urSQbkYWTI4FoRHtrYfeuYO62w-4GzDaK1vGVGu9N4Nc33pcB31ARjdeRJsMCZyIIA6ll_9--4qrWRR8lgYvJ5xgXAVc9nYKfoa75KETXp81EGriIZnBLWIIpUtq_ECA052I9LAJZURH8DIqbxuopZUb_tEGlJ8z2O44pUXz-ptuKk4ugYNaqlsgSaR7SvLpEj8c7fPe1Ge2cqF3_zdeH5d4vrz9WVZGZDrYJaXRkRiUz3pqoMpwLgAovdoJP754Rr65QhyrEqNV78OGm6ovvfy65b_cYLIeev9JwlDdCiJ-5NcMI7xvrN8GPciu3QnH1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
علی ضیا ازدواج کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/690616" target="_blank">📅 15:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690615">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
وزیر جنگ رژیم‌صهیونیستی: به ایران یا هیچ گروه دیگری اجازه نخواهیم داد که حماس را دوباره مسلح کند. اگر اردوغان می‌خواهد به آن‌ها کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما غزه هرگز محل قدم‌های او نخواهد بود. نبرد با ایران و سایر جبهه‌ها همچنان ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/690615" target="_blank">📅 15:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690614">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f887250b0.mp4?token=VwKJHarUyc-sCbqI-BHyaEN4TUmux9rKLxPdkv1TRQ1yyhzYo7QJUNarhHatO-PR9lcIOT1Qyxd_Qbhpu17oTPrlEF0EsIrqDHs0zC9meDLibYzOM83TVkhPvjekqo4H_h74tmipjwXlplTy3jqznUy5EMW_CFULUpv9HCQIgfQTclLUgtagOjp6hGg4C_0X9yMPhar-g650RhQBw-LFoXe-eckPXJmkMLUWfnBH6SQmw5BltoJVUOxDnXE-qeYTiBIugDa2T7HeHm8eRzU8pMS_fTsMa4vVjfqLSdDRnkLRc1Q0h9tPebZxzfu2nMC8fXX4L_7DohuJjCrXhtchzzj6aF-YKGk5vLBC2DLZHPl_FRxQaO3Xr1JSiTY0Q0WCURTpPQKyuo_1hLYN-a3huedUs6Rnfbnfrbn7VRtIbbaHOuVBhkS6579LwVKFtWxjc9k_fA87zX1XSzFPkxsO_3PRo0AaoBZpigYcNvpih7x6erHi7RW5oQVx_6bLy9QddSeL8MpmFz96wq488K6J3A_O76qTsQwVqbzneJLSVVKzjuvKGTs9lbyJKglAN4PackQu1MAf6BlRtn7HudA8cjhxtw7D163CEL87DAkmlFWAZtRk-3KRPDn9-UYAai1FYpl91SA9a6cfQttxGP3d0XWzSKg70W89OOvt24plSnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f887250b0.mp4?token=VwKJHarUyc-sCbqI-BHyaEN4TUmux9rKLxPdkv1TRQ1yyhzYo7QJUNarhHatO-PR9lcIOT1Qyxd_Qbhpu17oTPrlEF0EsIrqDHs0zC9meDLibYzOM83TVkhPvjekqo4H_h74tmipjwXlplTy3jqznUy5EMW_CFULUpv9HCQIgfQTclLUgtagOjp6hGg4C_0X9yMPhar-g650RhQBw-LFoXe-eckPXJmkMLUWfnBH6SQmw5BltoJVUOxDnXE-qeYTiBIugDa2T7HeHm8eRzU8pMS_fTsMa4vVjfqLSdDRnkLRc1Q0h9tPebZxzfu2nMC8fXX4L_7DohuJjCrXhtchzzj6aF-YKGk5vLBC2DLZHPl_FRxQaO3Xr1JSiTY0Q0WCURTpPQKyuo_1hLYN-a3huedUs6Rnfbnfrbn7VRtIbbaHOuVBhkS6579LwVKFtWxjc9k_fA87zX1XSzFPkxsO_3PRo0AaoBZpigYcNvpih7x6erHi7RW5oQVx_6bLy9QddSeL8MpmFz96wq488K6J3A_O76qTsQwVqbzneJLSVVKzjuvKGTs9lbyJKglAN4PackQu1MAf6BlRtn7HudA8cjhxtw7D163CEL87DAkmlFWAZtRk-3KRPDn9-UYAai1FYpl91SA9a6cfQttxGP3d0XWzSKg70W89OOvt24plSnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چک بی‌محل ۵ هزار دلاری ترامپ
🔹
۵ هزار دلار برای هر بزرگسال، وعده‌ای حدود ۱.۲ تریلیون دلاری در آستانه انتخابات. اما پول این چک از کجا می‌آید؟
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/690614" target="_blank">📅 15:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690613">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b5c3313b8.mp4?token=CVsc8vs8NV4i-VJPLaVkjAxObWZ6cW5RVzS6nFbHsSm4wivQ1AV9Dyit1E2qekIDO135TQUi3oVU-m8ckymMvanZxyTjtf-iXNMDExvqNythzLOHN6-SA7WDpMgqVexHSOqCVjMTKKsCQZ6EVJraAw9xfNshTGGFaslGSJ1Gf1lc3XmUK-BAiBUQ-nazuhcsonJ38ZTNHurzzlS5CXRDWxM3mUAWlWoDsmKnXE5O0CtYFZfriIqVD-jMJElMV1awPLSI0ReyS9BL_9ICCiXsO4ldmlVudod3hS7MxT3P4O_v5dDECH2OiG_IqUjRETIwkmsD4ONiv9H-bOVmd67Nuqzubxbi-nVseNZYx5wayWSwUzuOJfaO_9qLonf0wKdLcnBhpkQCBQ8oIP6gMwvsdIAP0AyCnLYMCwhD2KcRmZqg_K41ApEBXHV3jvTi_GZMfAWDrak9QTwe6CQgm_6voysFLIV7ozNhbxeywNHsee_dymbD9T8_rcaWKZ5a_7bMBg3QrOdVDcNYv_fyisKzcrQMNKPXZ9iIXx6sqiNKIDj25yf7nnz-sLbG2JejXW1WA3bX8Xs9EI0DBLO9pWIXzBScNVtLKaFBMB1pdGQkiN3B0gx-yYrXwFZqGuOFhepnR5OuUX9NGHKoLwrKg7UNptu3nYGnSWynDPO-G-NKFXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b5c3313b8.mp4?token=CVsc8vs8NV4i-VJPLaVkjAxObWZ6cW5RVzS6nFbHsSm4wivQ1AV9Dyit1E2qekIDO135TQUi3oVU-m8ckymMvanZxyTjtf-iXNMDExvqNythzLOHN6-SA7WDpMgqVexHSOqCVjMTKKsCQZ6EVJraAw9xfNshTGGFaslGSJ1Gf1lc3XmUK-BAiBUQ-nazuhcsonJ38ZTNHurzzlS5CXRDWxM3mUAWlWoDsmKnXE5O0CtYFZfriIqVD-jMJElMV1awPLSI0ReyS9BL_9ICCiXsO4ldmlVudod3hS7MxT3P4O_v5dDECH2OiG_IqUjRETIwkmsD4ONiv9H-bOVmd67Nuqzubxbi-nVseNZYx5wayWSwUzuOJfaO_9qLonf0wKdLcnBhpkQCBQ8oIP6gMwvsdIAP0AyCnLYMCwhD2KcRmZqg_K41ApEBXHV3jvTi_GZMfAWDrak9QTwe6CQgm_6voysFLIV7ozNhbxeywNHsee_dymbD9T8_rcaWKZ5a_7bMBg3QrOdVDcNYv_fyisKzcrQMNKPXZ9iIXx6sqiNKIDj25yf7nnz-sLbG2JejXW1WA3bX8Xs9EI0DBLO9pWIXzBScNVtLKaFBMB1pdGQkiN3B0gx-yYrXwFZqGuOFhepnR5OuUX9NGHKoLwrKg7UNptu3nYGnSWynDPO-G-NKFXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فکر می‌کنی اندازه واقعی اندام‌های بدن انسان چقدره؟  #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/690613" target="_blank">📅 15:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690612">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اتحادیه اروپا با رونمایی از «قانون کودکان» استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۳ سال را ممنوع کرد
🔹
طبق این طرح پلکانی، دسترسی نوجوانان ۱۳ تا ۱۵ ساله نیز منوط به نظارت والدین و محدودیت زمانی روزانه (حداکثر یک ساعت) است.
🔹
پلتفرم‌ها همچنین ملزم به حذف قابلیت‌های اعتیادآور مانند «اسکرول بی‌نهایت» شده‌اند
🔹
این محدودیت‌ها که در صورت تصویب نهایی اجرایی می‌شوند، علاوه بر گروه‌های سنی زیر ۱۵ سال، برای نوجوانان ۱۵ تا ۱۸ سال نیز استاندارد‌های «طراحی ایمن» را اجباری می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/690612" target="_blank">📅 15:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690611">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b75213502.mp4?token=LBHZ7WidA2SWUpSFJEV7GvNur23PBDTSC3G4H1VHqu8jbGZW14a5nsIQrmV5sHng0GA6HQoyS6Be0W4cgILyQqupvdOsZM9Tzg_bFwWs34LaUglt6ZeA6injzOq2SYM6r2XPAombQ1PKbBS1X9oqFed7SxliubqWZzDmBGBq6nUL26MFeRS6iO2eSkJ0Hxy8CMllBqw1usKuVWjTAQ_L6lWLUbG1CXc9-e3lZs9tco04jCxcO9kT3xogC2hA24IfvtPxTR2a0jqxaHKxmHqZRFXC_FmzbnNS2yJExAkwTAVG5YYaj5-etL73Dxr02zdSlluLmUAiyfZhQKVOl8ZDyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b75213502.mp4?token=LBHZ7WidA2SWUpSFJEV7GvNur23PBDTSC3G4H1VHqu8jbGZW14a5nsIQrmV5sHng0GA6HQoyS6Be0W4cgILyQqupvdOsZM9Tzg_bFwWs34LaUglt6ZeA6injzOq2SYM6r2XPAombQ1PKbBS1X9oqFed7SxliubqWZzDmBGBq6nUL26MFeRS6iO2eSkJ0Hxy8CMllBqw1usKuVWjTAQ_L6lWLUbG1CXc9-e3lZs9tco04jCxcO9kT3xogC2hA24IfvtPxTR2a0jqxaHKxmHqZRFXC_FmzbnNS2yJExAkwTAVG5YYaj5-etL73Dxr02zdSlluLmUAiyfZhQKVOl8ZDyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس اینترنشنال: باید زیرساخت‌های اقتصادی ایران کامل از بین ببرید. پالایشگاه‌ها، تولید بنزین، نیروگاه‌ها و منابع سوخت را بزنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/690611" target="_blank">📅 15:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690610">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
آناتولی به نقل از منابع پاکستانی: عاصم منیر از ایران خواسته تا انصارالله یمن را متقاعد کند که به تأسیسات انرژی عربستان حمله نکند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/690610" target="_blank">📅 14:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690609">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035fb6a3c2.mp4?token=jkYILkqNhK3xy7qfJGzxgOGFPAHyys8PjUEv6Rzk1rxTwwOOktOFfa_6T0dPZRWUPIxdsEXlM-mIogcHHE6UKnDRJTOjloq-fK8r1wGqvbePi6PQt5r-TCkoQH3W4vVbH7hPRL9NAR_MPGaIH_Hcs3YGzFNvfRuRnhla6Nqz3BIUiAwHSgHGYJDdmrqzUWFzSIN3V9wLd9otZWjdPzaJDNtkKEiR-eG3ZHK1KVimewdCJk9ZmBvfiN5u1TfLuWNGmSI3d6ulG4eB2qjI8ih1c07HZdLicyumhDJxvx_7xhAnzpzPHW5StzAE4ThLKSvKQdSeIsi41NbJkg-CCYdg1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035fb6a3c2.mp4?token=jkYILkqNhK3xy7qfJGzxgOGFPAHyys8PjUEv6Rzk1rxTwwOOktOFfa_6T0dPZRWUPIxdsEXlM-mIogcHHE6UKnDRJTOjloq-fK8r1wGqvbePi6PQt5r-TCkoQH3W4vVbH7hPRL9NAR_MPGaIH_Hcs3YGzFNvfRuRnhla6Nqz3BIUiAwHSgHGYJDdmrqzUWFzSIN3V9wLd9otZWjdPzaJDNtkKEiR-eG3ZHK1KVimewdCJk9ZmBvfiN5u1TfLuWNGmSI3d6ulG4eB2qjI8ih1c07HZdLicyumhDJxvx_7xhAnzpzPHW5StzAE4ThLKSvKQdSeIsi41NbJkg-CCYdg1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین قشقاوی، نماینده مجلس: قبل از جنگ به ترامپ گفتیم ۵۰۰ میلیارد دلار به شرکت‌های آمریکایی می‌دهیم، اما جنگ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/690609" target="_blank">📅 14:57 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
