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
<img src="https://cdn4.telesco.pe/file/bEiDHH-8iQI9KCUJeW3glFQxnGg2Wfgu71d4xPcJa19CSCtgAQwVcrSfciJL7bbmq2e2dezjtafjh9qrnjmPXLhVhQk2P4cXVOf_h8uJ8bnzlzQ3vg5PyF2xv-xc_OE4vf_bdwOVOlv2LbdPI4flKC6oG2xdYULSeZu-vf2WFMTF1kZNKYC1Sk-Yifhbj4TBlfuVxHjeQ5SMAxlXOSXSkcoUSJQvvFYmPttnbtDvOZP2wxKvrHb_Fbf8RjQBTfX6HeScnHt6jem9zgrnQHAqq4tbztiMtoOint3srtpjF-k-z-4sGH4Ux-IKcP2lIU6ahTQzNsqMmux3oQfDS38d7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-15061">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: اگه لیندسی گراهام بیاد و به این توافق با ایران شک کنه و حرفی بزنه، واقعاً براش دردسر درست می‌شه و حسابی به مشکل می‌خوره.
@withyashar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/withyashar/15061" target="_blank">📅 16:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15060">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آکسیوس: جان رتکلیف، مدیر سیا، به دونالد ترامپ و مقام‌های ارشد آمریکا گفته ارزیابی‌های اطلاعاتی نشان می‌ده ایران احتمالا تمایل واقعی به اجرای تعهدات هسته‌ای خودش نداره.
گفته می‌شه تفاوت میان حرف‌های داخلی مقام‌های ایرانی و آنچه به مذاکره‌کنندگان آمریکایی گفتن، باعث این نگرانی شده.
مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر دفاع آمریکا، هم نگرانی مشابهی دارن.
@withyashar</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/withyashar/15060" target="_blank">📅 15:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15059">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، سه‌شنبه 26 خرداد از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی، دو زندانی سیاسی بازداشت‌شده در اعتراضات دی‌ماه در استان سمنان خبر داد. میزان اتهام آن‌ها را «افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد در شهرستان…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/withyashar/15059" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15058">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6041510c69.mp4?token=gx6vB5WMqLYlxTxN_aCefr7jwisvOmDKTva2qh4WJV1BKe1PwCk99kyC_J9PvcaIu20nW1hIOKaftccnBxmIIjJLGrPQYq1o-ZSIZrvboE9FBOsT47mFQrBJVDTTALWAmMsVEBSk5Gu7dv7MRn3V9G960ZO1TI7zhiY5j_sUvHz7DmdnV86iUY58FQ9i2WAeXDPPCjlBfhDcClSNFlZH8vWifC7l3kJjgYSys8djy8RiNUs7q1_ZeYi4CY6-t34AAm7Ex1LH_AqxHDtoiL69yAe7jYXGagr2peo86cGb0jl2nyvMhAnkK1cFipKWl5mwc_rhmv168BErwSejNoz0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6041510c69.mp4?token=gx6vB5WMqLYlxTxN_aCefr7jwisvOmDKTva2qh4WJV1BKe1PwCk99kyC_J9PvcaIu20nW1hIOKaftccnBxmIIjJLGrPQYq1o-ZSIZrvboE9FBOsT47mFQrBJVDTTALWAmMsVEBSk5Gu7dv7MRn3V9G960ZO1TI7zhiY5j_sUvHz7DmdnV86iUY58FQ9i2WAeXDPPCjlBfhDcClSNFlZH8vWifC7l3kJjgYSys8djy8RiNUs7q1_ZeYi4CY6-t34AAm7Ex1LH_AqxHDtoiL69yAe7jYXGagr2peo86cGb0jl2nyvMhAnkK1cFipKWl5mwc_rhmv168BErwSejNoz0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با پراید رفته دم لانچر در حال شلیک
@withyashar</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/15058" target="_blank">📅 15:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15057">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرگزاری دولتی ایسنا:
محاصره دریایی آمریکا در حال لغو شدن است
@withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/15057" target="_blank">📅 15:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15056">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=QQciIbSi7cB2xZ9Si8vqZaQZ9Pdc7JUN_yeoGVOVYUzRkn0k2ZG35h6orRuGdoWlAaeeicnvgRjTbU1eCOM36if8F_nck6C92p4t8luB5RYAg1tc1bMx26OByzZLmzqhu1x_MtIkkawS2qQI1VYfWKZFm5alv2f2QlT4oXhSDdXZs-E93MIWsqvN7dOAHDidmbKMCbSFu3f6XqOLM-yhr1TnAY6vGZFNP2FIF9Qm2VYIA26zxNS7xISj56AN6FqZ9QojOpnK3Hl18DTdb4f3AK6CfxQopTRDvFX-R0zUEnSphUDozkpPgWO4Ck_diEhSVnqyP62ybW-5PmkYNvZqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=QQciIbSi7cB2xZ9Si8vqZaQZ9Pdc7JUN_yeoGVOVYUzRkn0k2ZG35h6orRuGdoWlAaeeicnvgRjTbU1eCOM36if8F_nck6C92p4t8luB5RYAg1tc1bMx26OByzZLmzqhu1x_MtIkkawS2qQI1VYfWKZFm5alv2f2QlT4oXhSDdXZs-E93MIWsqvN7dOAHDidmbKMCbSFu3f6XqOLM-yhr1TnAY6vGZFNP2FIF9Qm2VYIA26zxNS7xISj56AN6FqZ9QojOpnK3Hl18DTdb4f3AK6CfxQopTRDvFX-R0zUEnSphUDozkpPgWO4Ck_diEhSVnqyP62ybW-5PmkYNvZqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران حتی یک بار به ترکیه حمله کرد، من هرگز این را درک نکردم، هیچ‌کس آن را درک نخواهد کرد
این مشکل است، آن‌ها کاملاً غیرمنطقی هستند و اکنون آن افراد رفته‌اند، فکر می‌کنم ایران اکنون رهبری منطقی دارد!
@withyashar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/15056" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15055">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش روزنامه New York Post می‌گوید که پلیس فدرال آمریکا (FBI) پنج نفر را به اتهام طراحی یک حمله به رویداد «UFC Freedom 250» در روز تولد ترامپ که در محوطه چمن جنوبی کاخ سفید برگزار شد، بازداشت کرده است. گفته می‌شود این طرح شامل استفاده از پهپادهای انفجاری، تک‌تیراندازها و همچنین تلاش برای نفوذ و شکستن دروازه‌های محل بوده است.
بر اساس این گزارش، FBI در تاریخ ۱۰ ژوئن از وجود این توطئه مطلع شده و سپس طی یک عملیات چندایالتی اقدام به بازداشت افراد کرده است. مقام‌ها می‌گویند در جریان تحقیقات، چت‌های رمزگذاری‌شده در اپلیکیشن Signal کشف شده که بیش از ۲۰ کاربر در آن‌ها حضور داشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/15055" target="_blank">📅 15:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15054">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=bxdyI30zQsLJuygINkjT65BpaRHQru3-gjOcVg9u1n-P7jHZ3lY7JJ9LF8cmTcemli2oPr_UvSxj5BF5bGjY2jHvs9NFF6pU7hCWhNJp-GGQeKP1_F0ptExgLVsvyOOPnUbYRZEoKFc9osA6IprlWIUVaKkvIOdZZD0XMQJ2raMH8Af1eeHEfUFTfpOyzuhd6CmS5okThVRj_wKYUf0kq9QRBVHnKT7GTfJULaMh-IE-f3_NwjWKBt8gD18cxgNGchQqZFJtDc9NnFYU8BcX0DkybLfwzLVoQKo87RERXXyk2xR2OOzaFgxCjJYcdhNwxTsjGc9V61g3EvzggbTcoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=bxdyI30zQsLJuygINkjT65BpaRHQru3-gjOcVg9u1n-P7jHZ3lY7JJ9LF8cmTcemli2oPr_UvSxj5BF5bGjY2jHvs9NFF6pU7hCWhNJp-GGQeKP1_F0ptExgLVsvyOOPnUbYRZEoKFc9osA6IprlWIUVaKkvIOdZZD0XMQJ2raMH8Af1eeHEfUFTfpOyzuhd6CmS5okThVRj_wKYUf0kq9QRBVHnKT7GTfJULaMh-IE-f3_NwjWKBt8gD18cxgNGchQqZFJtDc9NnFYU8BcX0DkybLfwzLVoQKo87RERXXyk2xR2OOzaFgxCjJYcdhNwxTsjGc9V61g3EvzggbTcoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدراعظم آلمان در جی۷ پیراهن «ترامپ ۴۷» را به رئیس‌جمهور آمریکا اهدا کرد
@withyashar
خانواده دونالد ترامپ ریشه آلمانی دارند. پدربزرگ او، فریدریش ترامپ، در شهر کالشتات آلمان به دنیا آمد. او در سال ۱۸۸۵ و در شانزده سالگی از آلمان به ایالات متحده آمریکا مهاجرت کرد. پدر ترامپ، فرد ترامپ، در آمریکا متولد شده بود و شهروند آمریکا محسوب می‌شد، اما از طرف پدری کاملاً تبار آلمانی داشت. از سوی مادر نیز ترامپ ریشه اسکاتلندی دارد. مادرش، مری آن مک‌لئود ترامپ، در جزیره لوئیس در اسکاتلند به دنیا آمد و بعدها به آمریکا مهاجرت کرد</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/15054" target="_blank">📅 15:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15053">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ با انتقاد از نتانیاهو  :
لازم نیست هر بار که دنبال کسی می‌گردی، یک ساختمون آپارتمانی  خراب کنی.
تو اون خونه ها ادم های زیادی زندگی میکنن و همه عضو حزب الله نیستن
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/15053" target="_blank">📅 14:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15052">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7693c44486.mp4?token=hM9xswnAQpS6Up2A3p_9iCKZrdtPyTCbm-oXPLPmDBH8U4u14Vaz1USH6yVC0NixBlS54gW8E4cNTqzHED8S182dUuCxF56ilM3eh_JSTjgqUIwAfZAKdbYrTtiaTivtRiNjdRRhdYCGpGQLC1kEPqKJwyJtNQuQmyhId1MfL1mdMNc4o-D7PIVYr2piVHmIWkCxAWBQop5ut3hdOP4-R59qiw9e02zvUh2BF6641H8gW6eKDN4JWJYr9yAkrKWIv-tGd0sBI5jhApLpGoWVTT82tTM0d2qH5ymTE4Scpjt7euyUltYAz6wdURwRz8pVzIqWGziobadoQ4rZt6pXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7693c44486.mp4?token=hM9xswnAQpS6Up2A3p_9iCKZrdtPyTCbm-oXPLPmDBH8U4u14Vaz1USH6yVC0NixBlS54gW8E4cNTqzHED8S182dUuCxF56ilM3eh_JSTjgqUIwAfZAKdbYrTtiaTivtRiNjdRRhdYCGpGQLC1kEPqKJwyJtNQuQmyhId1MfL1mdMNc4o-D7PIVYr2piVHmIWkCxAWBQop5ut3hdOP4-R59qiw9e02zvUh2BF6641H8gW6eKDN4JWJYr9yAkrKWIv-tGd0sBI5jhApLpGoWVTT82tTM0d2qH5ymTE4Scpjt7euyUltYAz6wdURwRz8pVzIqWGziobadoQ4rZt6pXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : اگر رژیم ایران به کشتن مردم خودش ادامه دهد، آیا شما همچنان این معامله را پیش خواهید برد؟
ترامپ: ما با آنها در این باره صحبت کردیم. بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، بسیار بیشتر از الان.
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/15052" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15051">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرگزاری msn
: ترامپ و کنگره به هگسث و روبیو اعلام کرده‌اند اگر با توافق با ایران مخالفت کنند ، از سمت خود برکنار خواهند ‌شد
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/15051" target="_blank">📅 14:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15050">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: جنگ لبنان مسئله فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم که از حمله آنها به بیروت خوشم نیامد
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد
من از نتانیاهو ناامید نیستم. ما رابطه بسیار خوبی داریم
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/15050" target="_blank">📅 13:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15049">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: من به تغییر رژیم اعتقاد ندارم. سال‌هاست که تغییر رژیم‌ها را دیده‌ام و هیچ‌وقت نتیجه نمی‌دهند!
فکر می‌کنم توافق با ایران عادلانه است
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15049" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15048">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:
می‌خواهیم اورانیوم غنی‌شده را از ایران بگیریم
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15048" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15047">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: ما می‌خواستیم برای دریافت اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15047" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15046">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: تلاش‌هایی برای تغییر رژیم در ایران صورت گرفت، اما موفق نشدند.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، اطمینان از این بود که ایران سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال دستیابی به سلاح هسته‌ای باشد، جهنمی به پا خواهد شد.
ما از نحوه مدیریت امور توسط قطر در طول بحران اخیر، احساس خوشحالی و احترام می‌کنیم.
توافق با ایران به مرحله دوم منتقل می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15046" target="_blank">📅 13:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15045">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5d35b80d.mp4?token=CxCvxJdU1Q83bm5x3eUj1EIN_IhwC1xI6AcF-oQU2vw4iBecm_4WwYSXjC4uNK2O7i3Ys_8xGKp2wP7D3ZUaObUnpludQDVpYPR6pvNINrGkNJw06NPfePe532LvXkb1kzDFLibp2ciCght-J1drIjFsYdjE8yi-BaPIfZZqFYipaVXbIqrXR381JQ0ZLinV0k_oP-ff1EHVxMNv8bIR9Wk46rcvaDQ9s6SuCVVnTUlXMFo6oUoLoHH99B-n18hgs_Gd-tA2GOVlKB3I2fFqjoHzFGrX_RxqA1ZtiQpmbkbAX0mXuchi0BoDZumhpzd6SmOWnkh5z109GpeuW0KdQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5d35b80d.mp4?token=CxCvxJdU1Q83bm5x3eUj1EIN_IhwC1xI6AcF-oQU2vw4iBecm_4WwYSXjC4uNK2O7i3Ys_8xGKp2wP7D3ZUaObUnpludQDVpYPR6pvNINrGkNJw06NPfePe532LvXkb1kzDFLibp2ciCght-J1drIjFsYdjE8yi-BaPIfZZqFYipaVXbIqrXR381JQ0ZLinV0k_oP-ff1EHVxMNv8bIR9Wk46rcvaDQ9s6SuCVVnTUlXMFo6oUoLoHH99B-n18hgs_Gd-tA2GOVlKB3I2fFqjoHzFGrX_RxqA1ZtiQpmbkbAX0mXuchi0BoDZumhpzd6SmOWnkh5z109GpeuW0KdQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ما هیچ پولی در ایران سرمایه‌گذاری نمی‌کنیم، راستی. دیروز شایعه‌ای پخش شد. مضحک بود.
ما حق داریم روزی وارد شویم و اگر من بخواهم کاری انجام دهم یا کسی بخواهد کاری انجام دهد، اما ما هیچ پولی سرمایه‌گذاری نمی‌کنیم.
ما هیچ تعهدی برای سرمایه‌گذاری پول در ایران نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/15045" target="_blank">📅 13:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15044">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: ما هیچ پولی در ایران سرمایه‌گذاری نخواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/15044" target="_blank">📅 13:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15043">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، سه‌شنبه 26 خرداد از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی، دو زندانی سیاسی بازداشت‌شده در اعتراضات دی‌ماه در استان سمنان خبر داد. میزان اتهام آن‌ها را «افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد در شهرستان شاهرود» اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/15043" target="_blank">📅 13:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15042">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ویس میلیارد دلاری ۲
💰
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15042" target="_blank">📅 13:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15041">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ویس میلیارد دلاری
💰
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15041" target="_blank">📅 12:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15040">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15040" target="_blank">📅 12:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15039">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/15039" target="_blank">📅 12:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15038">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3Z_ehBNzKylUTxFEd2fq3iTrbNwRkIQdh5PLaoa0H_u0CUcZJeGQMk__GcRsCuB7wQ9BoyYhdPbrfk4a11gbLlfg0Rro8tD_RZxUrbfRvSi8Foo2UPL8u07Da8Lq5SOvNw8PTkC3G6rV8-nWaNp-AvHHi0ig9hJ3BVr_U_HphLB9qeW_dF8VtREq9fIGbMrx_fiAOUBzKci3WEHD8qzVMO90h9y4WD2h2bGkCjo_9K6Q4R1GKBhvQ1DaLVrrnZuVf9DeahJbr7lKWtLtCHSlcxVaFMHmyzEIu8GqIe2_mNsZL9tPaZiNGCDuZ3hIOEAxJD39faJ70nWRbzmNFEu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی پیش اهواز چیزی نیست کباب‌میزنند
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15038" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15037">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15037" target="_blank">📅 12:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15036">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارسالی</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15036" target="_blank">📅 12:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15035">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15035" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15034">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چپقچی: در سوییس پس از اینکه مسئله امضا ( تفاهمنامه پاکستان) انجام شد، مذاکرات شروع خواهد.
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15034" target="_blank">📅 12:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15033">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcV5sNWzq6YQURNmRIZr2SJZlyLz3YCqc8ouHZU-oAfVRAzHCt5eVV8jpwxoGE_Oyy9V3O1jxQrdZcKS71Vt2a3NhenX8r6KWEYAElPEkg3XgdJWxUhccoTobLvuNkUAtLbehOEn4_kCPkqHL_zI2zIKTqfQ1yuDsZW4gIo03Xhy_MrNxR2TyQDLm90-Qoiu_2WwAUapCSqXtVKtc4KHNzY0_Xej944kFMeSXXvBcem7_GZTbauRvpe8NT5YtZQQzAt0hPG_Z_pvzFL5pulUgX97TE5v2RmVg9hI9lIjBhV8KZbnbzOu448YYXjsYODBfb-kyU12wYWwlCMpEOpXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روزنامه همشهری از متن و مفاد توافق
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15033" target="_blank">📅 12:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15032">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عراقچی: هرگونه حمله نظامی اسرائیل به لبنان ، نقض یادداشت تفاهم محسوب می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/15032" target="_blank">📅 12:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15031">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کیهان: معنای سکوت رهبری درباره هسته‌ای این است که دیگر مذاکره‌ای در کار نیست
@withyashar
روزنامه کیهان وابسته به اصولگرایان تندرو نزدیک به بیت رهبری است و مدیر مسئول آن مستقیماً توسط علی خامنه‌ای انتخاب شده .</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15031" target="_blank">📅 11:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15030">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bf6e0591.mp4?token=DoL-WPuS9iT9dhuCkujjV4YdDuXXuC8OAghEszLCrdPobPcwrjgRYkO8qC7OZuIrmgf0Misw2HBs7YTVCa__PrVgt4HEkIV_c3mCUuP9VfUcWvKANZ3HcOkS20GcbcaYRNk7sV295Lw65gsxMHSClDDL4S6nUDDi7jXzDx6XT3FqOA-4WSppyWxZmqYlKTkXrcMAsGIZx5h9NPOyJtoBhIW3Dxs74TSGuECvw5_1hFmDQlHnnusz5_WT_DYPlFUWn0tePUg3ndlKMWQytrcPbs1TkidFAw6UiouP6OvaBXp9LKyoTgVFMdIe7-i5nnTfNQbOGqwjYx6rmrsr8cK31A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bf6e0591.mp4?token=DoL-WPuS9iT9dhuCkujjV4YdDuXXuC8OAghEszLCrdPobPcwrjgRYkO8qC7OZuIrmgf0Misw2HBs7YTVCa__PrVgt4HEkIV_c3mCUuP9VfUcWvKANZ3HcOkS20GcbcaYRNk7sV295Lw65gsxMHSClDDL4S6nUDDi7jXzDx6XT3FqOA-4WSppyWxZmqYlKTkXrcMAsGIZx5h9NPOyJtoBhIW3Dxs74TSGuECvw5_1hFmDQlHnnusz5_WT_DYPlFUWn0tePUg3ndlKMWQytrcPbs1TkidFAw6UiouP6OvaBXp9LKyoTgVFMdIe7-i5nnTfNQbOGqwjYx6rmrsr8cK31A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبی بعد از  زدن گل دوم، با نشان دادن اسلحه و شلیک نمادین به تماشاگران نشون داد این تیم مزدوران حکومتیه نه مردم ایران
این نفهمی او واکنشمنفی‌ در‌
رسانه های جهان داشته
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15030" target="_blank">📅 11:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15029">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دونالد ترامپ در گفتگو با CBS در واکنش به سفر کاروان تیم فوتبال ایران به آمریکا گفت:
"افتخار میزبانی کاروان تیم فوتبال ایران را داریم. آنها تیمی بزرگ هستند.
به قلعه نوعی گفتم اگر اینجا جایی نداری شب بمانی به منزل ما بیا. شاید قبول کرد. شاید هم نکرد. باید ببینیم چه می‌شود"
@withyashar
.
😂
شوخیه</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/15029" target="_blank">📅 10:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15028">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ویزای مهدی ترابی باطل شد
در حالی که برای بازیکنان تیم ملی برای سفر به آمریکا روادید «چند بار ورود» صادر شده است اما ویزای مهدی ترابی تنها برای یک بار ورود اعتبار داشت و پس از سفر تیم ملی به لس آنجلس جهت دیدار برابر نیوزیلند و پایان این بازی، اکنون ویزای این بازیکن منقضی شده است.
فدراسیون فوتبال ایران برای اخذ مجدد ویزای ترابی اقدام کرده تا این بازیکن بتواند در دیدارهای آتی تیم ملی را همراهی کند.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15028" target="_blank">📅 10:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15027">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک بمب‌افکن B-52 استراتوفورتراس نیروی هوایی ایالات متحده بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.    جزئیات تلفات هنوز گزارش نشده است. @withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15027" target="_blank">📅 10:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15026">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ونس: ترامپ ممکن است که پیش از روز جمعه، جزئیات توافق با ایران را فاش کند
جی‌دی ونس، معاون رئیس‌جمهور آمریکا اظهار داشت که رئیس‌جمهور دونالد ترامپ ممکن است تصمیم بگیرد پیش از روز جمعه جزئیات توافق با ایران را منتشر کند
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15026" target="_blank">📅 09:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15025">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امکان پلاک‌گذاری خودروهای بالای ۲۵۰۰ سی‌سی در مناطق آزاد فراهم شد
معاونت حقوقی ریاست‌جمهوری در نامه‌ای به دبیر شورای عالی مناطق آزاد از امکان شماره‌گذاری ملی خودروهای وارداتی بالای ۲۵۰۰ سی‌سی موجود از قبل در این مناطق خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/15025" target="_blank">📅 09:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15024">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Feb-BcFQr3mdZNT8KDJQtj_WuR8ILus-L9BA_r8CUCC3CIEUm_JrR8-lEGiH2ie9PRhKGwCh6ypMoF7pmdWDtRSIlSTxJR4RmuNqCtxfRsDB_rlxgJ3UDXeULm38MWfXoROinhj2k7stOtPC_3DpyWL5fEQuZNXMXGqRSF4IMuAZGcM1gRw66jqyfOL7W9Zi9TIbzUU1jbh2K6eBCn3g4KnP4S82YKG12RL9BMgUeAWAMRxdQmpXL5JuVJ7wDmB0wKRUlh1jtK5z8An2aYMyoxJfyuV5S5cHwOsJwLMFdUS6o2k8PDdkPysbAlk5eYLQtp2AGJj-14e-2Smt9qhSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندین بار در جریان بازی مسابقه امروز تیم نیوزلند و تیم ملی در صدا و سیما پرچم شیر و خورشید به نمایش درآمد.
کارگردان فیفا تا حد ممکن در حال سانسور صدا و تصویر (شامل هو کردن و پرچم شیر و خورشید) بود. از طرفی تعدادی از پرچم‌ها هم با نزدیک شدن به پایان بازی توسط نیروهای امنیتی جمع‌‌آوری شدند.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15024" target="_blank">📅 09:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15023">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a672a698ff.mp4?token=MDsFAd1BQjAf5CH5qGFZnl35DwKrEFfO_vtX_2o1ru-8-Bpu_PSBMeLZceuSu2R3Qg4DEY-t4X62kzzmcfRc5mNhT76ho4x1PrmRqMztFl4tus3iND8pn_L7LCyO3ZgXCFPcwpNk1LYUtpSxoZ_oW1u8qcYM64LUicqTT2C2XE_5ODgnav-MeWF7d0Cc9btc_O40Vv65iXh8Lkl8Tu8QxHKS6FmjEHpN3N7Ean9dfn-jY3gG6DM4OITSngwnldU6LcrUVKWOxi6DneycBGx-yOXWg_zXShOv0-nHdpnq3cp6lHjlItKUwiicIf5f3KPV_lHCsX7e--4MlGrnkwV8tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a672a698ff.mp4?token=MDsFAd1BQjAf5CH5qGFZnl35DwKrEFfO_vtX_2o1ru-8-Bpu_PSBMeLZceuSu2R3Qg4DEY-t4X62kzzmcfRc5mNhT76ho4x1PrmRqMztFl4tus3iND8pn_L7LCyO3ZgXCFPcwpNk1LYUtpSxoZ_oW1u8qcYM64LUicqTT2C2XE_5ODgnav-MeWF7d0Cc9btc_O40Vv65iXh8Lkl8Tu8QxHKS6FmjEHpN3N7Ean9dfn-jY3gG6DM4OITSngwnldU6LcrUVKWOxi6DneycBGx-yOXWg_zXShOv0-nHdpnq3cp6lHjlItKUwiicIf5f3KPV_lHCsX7e--4MlGrnkwV8tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7’—Iran 0-1 New Zealand
32’—Iran 1-1 New Zealand
54’—Iran 1-2 New Zealand
64’—Iran 2-2 New Zealand
گلهای بازی و تساوی ۲-۲
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15023" target="_blank">📅 09:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15022">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ecb9fedcf.mp4?token=UvX2cHOkS0nJ4SgD2l0eKcvy268nyelWD-sjxTRmYw_XU4suwZSugi-pg9XTd3JG2nGucG4mWQNtTsRmSYgs6jkzpUYPKoaayx9nBxQZrxbD6WVdQTbwgBnNyDNVidsWKTMbyYFUbXPCRwOgnO__Mr4inRSeRao_WxuC6jGCO9-SpjywFEGctLpD9ikTM6g2smRVWmmj1NbtlZ5I7MbtgHDEg9JYjueE96fHt97ajXOAlg92YpvjRV2rNWNRQ-ePQB6gxG3seHRXU3810fAIdVo09EEC3wKg6JcWQtzh-9VFROWMF1lJxOYrdrfqtia8PpT_H9VqA3Z3xmTs8a9Ncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ecb9fedcf.mp4?token=UvX2cHOkS0nJ4SgD2l0eKcvy268nyelWD-sjxTRmYw_XU4suwZSugi-pg9XTd3JG2nGucG4mWQNtTsRmSYgs6jkzpUYPKoaayx9nBxQZrxbD6WVdQTbwgBnNyDNVidsWKTMbyYFUbXPCRwOgnO__Mr4inRSeRao_WxuC6jGCO9-SpjywFEGctLpD9ikTM6g2smRVWmmj1NbtlZ5I7MbtgHDEg9JYjueE96fHt97ajXOAlg92YpvjRV2rNWNRQ-ePQB6gxG3seHRXU3810fAIdVo09EEC3wKg6JcWQtzh-9VFROWMF1lJxOYrdrfqtia8PpT_H9VqA3Z3xmTs8a9Ncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج مکزیکی بازی ایران نیوزلند
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/15022" target="_blank">📅 09:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15020">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLg7IleMcnLdSesLOFhnUs-8cK47n_UEXJkPUvtsWWXTjr6nC4U8anBhHZOGzeCZzZRSbz2D-o6lrjh4kzmeIHNR_87MHpyEMPXz3gDog5-wdpmEmjoJV0bwmLIkxCV37TmfB0JesWfr3NfOow093RIuL7dLt8WZv8Ce5UTIV0Y9wTbUf3hq3rhcO83Ckzp5bjCuHM6JsaxuT_mwnOktmmsAaB_wokcihLhGboJoNbmjhL9MWRDSXZiQEOiE278O2-5cxEAxEs2bx2Wb9gyQLQsm9i37C1v-qF7rfvCNslLgyqz_WpI3527BuIfZnH5l4z5zMbleF9f012t8Bsho6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین داستان اینکه آمریکا به ایران ۳۰۰ میلیون دلار می‌پردازد، خبری جعلی است که توسط دموکرات‌ها منتشر می‌شود!!! رئیس‌جمهور دونالد ج. ترامپ
@withyashar
فقط این ۳۰۰ میلیارد بود که میلیون نوشته</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/15020" target="_blank">📅 09:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15019">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769eece9da.mp4?token=PT6p-fM7vqWPmBPQQe9sUYfY3ub4lDn5pKGmqUFX8q4kDJ5VYdrUksiErRyldl8QKVn3jcSOzNeCIWqmjSF7-4QWP8xH-l3JRPSH839ZYbojqwpgCqOfC7ZiN-cPlXP6nDQI9le1Oz8KFyO4UKtFf2ORTyGslvoilKStit4lZO-_CKGz8CtgPaU1T11C7lOiVHf7LF4DTiupMo3al-EC6un2PydsvdHbU_UiORi-LSGhdCaE6oHvUlseuCzQZxJ5RmCmMuqwrifVWErRJTFBREPxZ5Ikd9oVeR6c-Dz-ZrVfClbT7t6BZbPlYxJxUNR5Zb18IunTleu4GNl_mhFBIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769eece9da.mp4?token=PT6p-fM7vqWPmBPQQe9sUYfY3ub4lDn5pKGmqUFX8q4kDJ5VYdrUksiErRyldl8QKVn3jcSOzNeCIWqmjSF7-4QWP8xH-l3JRPSH839ZYbojqwpgCqOfC7ZiN-cPlXP6nDQI9le1Oz8KFyO4UKtFf2ORTyGslvoilKStit4lZO-_CKGz8CtgPaU1T11C7lOiVHf7LF4DTiupMo3al-EC6un2PydsvdHbU_UiORi-LSGhdCaE6oHvUlseuCzQZxJ5RmCmMuqwrifVWErRJTFBREPxZ5Ikd9oVeR6c-Dz-ZrVfClbT7t6BZbPlYxJxUNR5Zb18IunTleu4GNl_mhFBIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس : هیچ دلار تخفیف تحریمی یا پول بلوکه‌شده‌ای، نه از آمریکا و نه از هیچ‌کدوم از متحدای ما تو خلیج، آزاد نشده
این امتیاز فقط وقتی بهشون داده میشه که به تعهداتشون تو توافق عمل کنن
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/15019" target="_blank">📅 01:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15018">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پرس تی وی: ۳ نفتکش و ۲ کشتی با کالای ایران از محاصره دریایی عبور کرد
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/15018" target="_blank">📅 00:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15017">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">@withyashar
تحلیل وضعیت</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/15017" target="_blank">📅 00:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15016">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCk13Ml3gh-O2A0qWa2JIJYRKPotzZRH5cbbvzthUZGLd5uJJhP2v8DcvojqMmJ9DAvugX15VbyCvpP7dpbIeNsDY0RnOG9puouGDLM17npfkEspPSJKIVIohaunMh_-lAX6Ia1XlaBRMHTcic0jaUItC7W0VR4zHlcdumMdMIFrvWJWJVIeu51mU_W6pyEi-mmPpvtzb9SlwbhxQqEsf7GO3q1Y0EJZLaEFBIu2ZSrYqSjNNZ0JBBCjyM9NmWoOvKQbjdYva4gGO0KLgT7ON72O0arree67v8Kdp112-vbz5gXJy2eUyCWSGXA9gIY7k2sqzTDGqdXyAn-gyrlbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشم  سمت سوزا همین الان خیابون اصلی
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/15016" target="_blank">📅 00:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15015">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">صدای توافق از قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/15015" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15014">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzx5-f7FSHtSinG5XunIZiRAwdqnJTlVuZG3Dpsq_elQbBWFlStBtE0tLrCsiCYpMvLZng4gQ42ecNU9sdK4QAEwv9GleERu80Hb5jO8EGruBmZP4OOX0DU1eloizbKo0Zig6pPBrfTWx1zbE7Bpo_fyYRodhwYAqD_9YXH_myhqxsIp8Z8LNMbN7K2qYvJ0aPqR38aIpc_rJfJkvysrHBF-SkO64ZUpQySFy9V8QmGO69SbKhgfAPI8h_XMfXbMqX1CmFQ6TEFonPzX--Ahr6TjH1MkzrY0YPgSv6dK16YLeWraPxiXMyqhkH6ieE9TxzGzlj6G1fiTwAbT3Q_p7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
توافق یا عملیات فریب برای حمله وحشتناک امریکا و اسرائیل!
⭕️
مشاهده تحلیل
🇮🇱
🇺🇸
🇮🇷
👇
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/15014" target="_blank">📅 00:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15013">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/15013" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15012">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال ۱۴ اسرائیل: تعجب جامعه اسرائیل از این بود که مقامات ایران قبل از دفن علی خامنه‌ای با قاتلینش توافق کردند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/15012" target="_blank">📅 23:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15011">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/15011" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15010">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عراقچی: جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/15010" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15009">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیویورک تایمز گزارش داد که ممنوعیت ورود پرچم‌های شیروخورشید ایران به جام جهانی که از سوی فیفا اعمال شده بود، پس از برگزاری یک جلسه اضطراری دادگاه در لس‌آنجلس در روز دوشنبه تایید شد و قاضی کرتیس ای. کین حکم داد که این ممنوعیت به قوت خود باقی بماند.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/15009" target="_blank">📅 23:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15008">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76cd0f1e71.mp4?token=oDYd3V2Fdyi02GXiXgqhcXv95Svfz7p6REjSq5Y4kNxtGrISZ-p0YyFIEGQspMqa0V3ZcBVPmU8xNIOerbTls56PPml3oLnZvhLLlGn903HhjY_udkDX_c9nli2MHm7wu8PhfWKWXRxPRD-dAafDiUnLvQxgza24vQ95E6wZHilI_kZtbi3gu7dRx3u--9KxWNNKMp-yJa21iArrHYciXxJw5wzduWrhk5rnUyeieYZtLu4oVCBe5y9sAewoiJ4CQikp4l6q8wK4vkx8lKhXVzqetP9ummOHad2VjG-GNoaVqeQGGUD5gLzvPJTXgSY2PNwK8gMv-M6lUuJBAxYhjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76cd0f1e71.mp4?token=oDYd3V2Fdyi02GXiXgqhcXv95Svfz7p6REjSq5Y4kNxtGrISZ-p0YyFIEGQspMqa0V3ZcBVPmU8xNIOerbTls56PPml3oLnZvhLLlGn903HhjY_udkDX_c9nli2MHm7wu8PhfWKWXRxPRD-dAafDiUnLvQxgza24vQ95E6wZHilI_kZtbi3gu7dRx3u--9KxWNNKMp-yJa21iArrHYciXxJw5wzduWrhk5rnUyeieYZtLu4oVCBe5y9sAewoiJ4CQikp4l6q8wK4vkx8lKhXVzqetP9ummOHad2VjG-GNoaVqeQGGUD5gLzvPJTXgSY2PNwK8gMv-M6lUuJBAxYhjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از محل سقوط بمب‌افکن استراتژیک B-۵۲ آمریکا در کالیفرنیا
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/15008" target="_blank">📅 23:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15007">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pASTIJs3ch7nYtWIA3Q-XAlPZANbqCh15yMiezjNQfqx-Y-8629u4sAg02SCaUaSBTXi9vsguEhE-0UpHeiuwTi87zaxsIwNxvf70gJRiabLF2jCLjvNB5y-9umVlbFOG2oiuDa_UHvnVjKf8icuIrvNbcvegruifFjsO-FP_mBlc8EfQBcQ1amgCFzhNznrQiqS2OLHtePX4eLqn_H6pIfO1tQ0AueEs48ldI6AFp522ouR5cNesYHRPrvuCFO49deJtzozoNlCG7FURtdMyzDfJj_jYCdQYxkOSL5IiardMvwf9ZfNyJ4M_UJxfUQgHcYDg9_QdVeZOqbkNhAbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بمب‌افکن B-52 استراتوفورتراس نیروی هوایی ایالات متحده بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.
جزئیات تلفات هنوز گزارش نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/15007" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15006">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoji pers</strong></div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/15006" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15005">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به ارتفاعات علی‌الطاهر در نبطیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15005" target="_blank">📅 22:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15004">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15004" target="_blank">📅 22:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15003">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پست جدید که در اون هنرنمایی هم کردم براتون کلیک کنید و حتماً کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DZngOTKRtYt/?igsh=MWwzcTZmaW9oZndxcQ==
⁨ اتاق جنگ با یاشار : سفر قاهره «ملودیک»⁩</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/15003" target="_blank">📅 22:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15002">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتانیاهو: از موارد مورد توافق بین ایران و آمریکا مطمئن نیستم ولی قطعا در انتخابات پیروز خواهم شد
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/15002" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15001">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUhNcZPUL0AGtBSzdp9RR_pLa-jfJaExiO15qAV7lMwn2fmOq2LtPUxyxm0tqGCpAPitorZz1sBu5gq8M3kKBuwQKLXs-njcdh-4w3h-bS_RGf17XZSDRBsXgFoIOTbVsVdM1zb2QZ5d4CVXnl-zLJMhu93P5G6ubF0GQSxdMfIG-ms4_EvRVHAI2xqDG-lk6JxLlqcfz0rl3IDWW6PoydIAidVmqKqfCMyThYBbDefPhSS-rOgBdxia4uTVzE-K1NrIVFdVDHnUZd6QHek-3MTtUGok8GkjNNEupJF-6JJAdyAFDU4u117xCEPlsGyPYtrb2B8g3KGGnxs3Wi_A_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15001" target="_blank">📅 22:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15000">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو: تا خلع سلاح حزب‌الله، اسرائیل از منطقه امنیتی جنوب لبنان خارج نخواهد شد.
همون کاری با غزه کردیم، با جنوب لبنان هم خواهیم کرد؛ همونطور که غزه دیگر تهدید جدی‌ای برای اسرائیل نیست، حزب‌الله هم در آینده نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/15000" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14999">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو: توافق با ایران توسط ترامپ منعقد شد، این تصمیم اوست و ما منافع خود را داریم‌‌
ترامپ رئیس‌جمهور آمریکاست و من نخست‌وزیر اسرائیل؛ من از منافع کشور خودم دفاع می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14999" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14998">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو: من نگفتم هدف ما سرنگونی رژیم ایرانه، گفتم میخواهیم به مردم ایران برای انجام این کار کمک کنیم
@withyashar
یاشار : توجه کن این جمله بار حقوقی داره با این حال بنیامین نتانیاهو بارها این حرف رو زده</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/14998" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14997">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو
: مبارزه تمام نشده است. ما باید همچنان هوشیار، قوی و مصمم باشیم تا از خود تا حد امکان دفاع کنیم. این نه تنها در مورد ایران، بلکه در مورد بازوهای تروریستی ایران نیز صادق است. ما به شیوه‌ای بی‌سابقه به آنها ضربه زدیم. ما این کار را در غزه، لبنان، سوریه، یمن، اردوگاه‌های پناهندگان در یهودا و سامره و همه جا انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/14997" target="_blank">📅 21:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14996">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو: من با ترامپ موافق نیستم،
بنابراین، اسرائیل هر کاری که لازم باشد در برابر ایران انجام خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/14996" target="_blank">📅 21:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14995">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شبکه ۱۳ اسرائیل به نقل از یک منبع:
تل‌آویو و واشینگتن بر سر عدم عقب‌نشینی کامل اسرائیل از لبنان به توافق رسیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14995" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14994">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbac886c1.mp4?token=Cvk3M31yemqtXzYLDMkqln_HzOY2OU3oNW1zHVrrMnfI5YAVPyoLJVFZDSQmapWupc54vmPmzJ0_6J7h9bt3jfrWqAzVEL3gditbIvBbR3T3xGM9yPg8Qk2MIIT2KQ50S_NzbIiSOMYMuA25r6WV_DIfuP9fJdvlIRuoO-xtRIbS7WAHM6bScVolKyVk2J5ecevDtilYV7HANm6pPH2MTI0aZKezKwy3fLlLo1HHZQ9SWE8pIwd5Ly2KOhs6OH1DRA0JpGxrknU60qJSCyTAauZhl51wA-Bmk-rMXR8tKsB2kU7dI23MSDmI8teBHym0HGJ99OdnWDxZr_g9SzQDRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbac886c1.mp4?token=Cvk3M31yemqtXzYLDMkqln_HzOY2OU3oNW1zHVrrMnfI5YAVPyoLJVFZDSQmapWupc54vmPmzJ0_6J7h9bt3jfrWqAzVEL3gditbIvBbR3T3xGM9yPg8Qk2MIIT2KQ50S_NzbIiSOMYMuA25r6WV_DIfuP9fJdvlIRuoO-xtRIbS7WAHM6bScVolKyVk2J5ecevDtilYV7HANm6pPH2MTI0aZKezKwy3fLlLo1HHZQ9SWE8pIwd5Ly2KOhs6OH1DRA0JpGxrknU60qJSCyTAauZhl51wA-Bmk-rMXR8tKsB2kU7dI23MSDmI8teBHym0HGJ99OdnWDxZr_g9SzQDRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:  ما در لبنان خواهیم ماند. کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/14994" target="_blank">📅 21:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14993">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو: ما خسارات عظیمی به ایرانی‌ها وارد کردیم و اسرائیل را از خطر نابودی هسته‌ای نجات دادیم.
اگر ما به سرعت برای حمله به ایران اقدام نمی‌کردیم، این کشور به بمب هسته‌ای دست پیدا می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/14993" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14992">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو: «اسرائیل تا هر زمان که لازم باشد در “مناطق امنیتی” باقی خواهد ماند.»
«ما شراکت‌های جدیدی را در سراسر منطقه و فراتر از آن شکل خواهیم داد، در حالی که توانایی اسرائیل برای تولید و تأمین مستقل تسلیحات خود را تضمین می‌کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/14992" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14991">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/14991" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14989">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مقامات آمریکایی اعلام کردن حتی با وجود توافق قصد عقب نشینی از منطقه را نخواهیم داشت و نیروهای آمریکایی در منطقه خواهند ماند.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14989" target="_blank">📅 21:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14988">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14988" target="_blank">📅 21:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14987">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کانال ۱۳ به نقل از یک مقام اسرائیلی:
ما از لبنان عقب‌نشینی نخواهیم کرد، اما از این پس هر عملیات نظامی قابل بررسی خواهد بود.
ما برای دستیابی به توافق بین واشنگتن و تهران قربانی شدیم.
معاون رئیس جمهور آمریکا از نتانیاهو خواسته است تا حضور اسرائیل در لبنان را کاهش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14987" target="_blank">📅 21:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14986">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو: می‌توانید طناب را با آمریکایی‌ها بکشید، اما نباید آن را پاره کنید.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14986" target="_blank">📅 21:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14985">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانال ۱۳ اسرائیل به نقل از منابع:
گفتگوی پرتنشی بین نتانیاهو و معاون رئیس جمهور آمریکا در مورد حضور اسرائیل در لبنان صورت گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/14985" target="_blank">📅 20:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14984">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبرنگار : آیا قصد دارید در تشییع قائد امت، حضرت آیت‌الله عظما جانشین امام زمان علی خامنه‌ای شرکت کنید؟  ترامپ: بله @withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14984" target="_blank">📅 20:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14983">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خبرنگار : آیا قصد دارید در تشییع قائد امت، حضرت آیت‌الله عظما جانشین امام زمان علی خامنه‌ای شرکت کنید؟
ترامپ: بله
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14983" target="_blank">📅 20:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14982">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fba57ac4d.mp4?token=JMz2wVKWUc54HZH_e2YGSJNtKC_wU56HODSVqN5vl37WuwKWKXv2DfM-j-1OHc6701HWd_b7si4ulhuPJ-rS1lTOL1p6CqUag96ZLSwYVW9yds61yZv8n6GIJTLcbh5MULQhF7aMVxaGFNLB9fRXvez9NAjKGspqpnhCpktnqfvcRhEA7cSCVR9Y55bNqHCnQC3fvpZRJgonKmFPNugt9mHd2Df8aRQJG6DKfqeQROQETk39yJkzRw1pm8oITkjL7ZWv0JUpIeq9jQ3N5OXGLeu4dIJXVtLELExXq7sn5xUeZ-kyhNb-Jq9jY3dzPOnO_n5uQvUnxOHg8sngsnjd7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fba57ac4d.mp4?token=JMz2wVKWUc54HZH_e2YGSJNtKC_wU56HODSVqN5vl37WuwKWKXv2DfM-j-1OHc6701HWd_b7si4ulhuPJ-rS1lTOL1p6CqUag96ZLSwYVW9yds61yZv8n6GIJTLcbh5MULQhF7aMVxaGFNLB9fRXvez9NAjKGspqpnhCpktnqfvcRhEA7cSCVR9Y55bNqHCnQC3fvpZRJgonKmFPNugt9mHd2Df8aRQJG6DKfqeQROQETk39yJkzRw1pm8oITkjL7ZWv0JUpIeq9jQ3N5OXGLeu4dIJXVtLELExXq7sn5xUeZ-kyhNb-Jq9jY3dzPOnO_n5uQvUnxOHg8sngsnjd7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار به ترامپ : آقای رئیس‌ جمهور، آیا این توافق شامل لغو زودهنگام بخشی از تحریم‌ های ایران میشود؟ این موضوع از چه زمانی اجرایی خواهد شد؟
ترامپ: نه، چنین چیزی در توافق وجود ندارد، این توافق بیشتر به رفتار طرف مقابل مربوط میشود
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/14982" target="_blank">📅 20:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14981">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: احتمال دارد جمعه حضور داشته باشم و با ایرانی ها دیدار کنم
از اینکه مجبور شدیم دو شب دیگر به حمله ادامه دهیم، احساس بدی داشتم. و فکر می‌کردم برای بار سوم هم همینطور، اما ما قبل از آن توافق را انجام دادیم.
فکر می‌کنم اتفاقات خیلی خوبی قرار است در خاورمیانه رخ دهد.
قیمت نفت در حال سقوط است و بازار سهام مثل موشک در حال افزایش است
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/14981" target="_blank">📅 19:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14980">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ: می‌خواهم یادداشت تفاهم با ایران را منتشر کنم زیرا سندی مهم و قدرتمند است و ما به زودی آن را منتشر خواهیم کرد
تنگه هرمز پس از جمع‌آوری مین‌ها به‌طور کامل‌ بدون عوارض باز خواهد شد
کاهش تحریم‌های ایران به رفتار این کشور بستگی دارد
اکنون ما می‌خواهیم ببینیم چگونه می‌توانیم مناقشه در لبنان را حل کنیم و باید در این مورد با اسرائیل صحبت کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/14980" target="_blank">📅 19:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14979">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ: توافقی که اوباما با ایران انجام داد، این کشور را قادر به ساخت سلاح هسته‌ای می‌کرد
ما خواهان روابط خوب با ایران هستیم و اگر این امر محقق نشود، به جنگ باز خواهیم گشت و امیدوارم این اتفاق نیفتد
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14979" target="_blank">📅 19:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14978">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: ما با ایران تفاهم‌نامه‌ای امضا کردیم و تنگه هرمز تا حدی بازگشایی شده است
تنگه هرمز روز جمعه به طور کامل باز خواهد شد
: توافق با ایران به نفع منطقه خاورمیانه خواهد بود
ایران سلاح هسته‌ای نخواهد داشت و من با این موضوع موافقت کردم. این اصل موضوع مناقشه بود
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/14978" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14977">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فوری: اولین سخنرانی مجتبی بعد از پایان جنگ و توافق با آمریکا.
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14977" target="_blank">📅 19:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14976">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81cca2afa.mp4?token=nYZyb-xIOYaWzziF5azj2KCAmvoQ1fnj1fWLxNJA4SPQDn3gtsWCV0LwSF-rPc4iRYY5xinCskcR6hBnyJkPHqyUPB5mvcMvbtmzUTcbpqjdx7yRMfcjhn15EXGOaBUJfmP8S9o53Npw_gGw1ulNnVrBlF1y3PvPJ4Dfq4DwXvMXgMlW_NxwzKGgGYSMRt0aDGqaIZMI-yc8EVVOvlo0pO3BfqL9qDDQl7AyDnLwRM-MOh1mU46U809XznkMP2cIMalnlQEfHQ4Yo7Si1ouIzVUOKf1-b-IOMfMdrVxnSfOjos9r-caWRiLjGMKY2k61cM3D8D_xm3lutHE3mSxp8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81cca2afa.mp4?token=nYZyb-xIOYaWzziF5azj2KCAmvoQ1fnj1fWLxNJA4SPQDn3gtsWCV0LwSF-rPc4iRYY5xinCskcR6hBnyJkPHqyUPB5mvcMvbtmzUTcbpqjdx7yRMfcjhn15EXGOaBUJfmP8S9o53Npw_gGw1ulNnVrBlF1y3PvPJ4Dfq4DwXvMXgMlW_NxwzKGgGYSMRt0aDGqaIZMI-yc8EVVOvlo0pO3BfqL9qDDQl7AyDnLwRM-MOh1mU46U809XznkMP2cIMalnlQEfHQ4Yo7Si1ouIzVUOKf1-b-IOMfMdrVxnSfOjos9r-caWRiLjGMKY2k61cM3D8D_xm3lutHE3mSxp8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، برای شرکت در نشست سران گروه هفت (G7) وارد شهر اویان له‌بن در فرانسه شد
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14976" target="_blank">📅 19:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14975">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkF6p4nfyRKBtXmnfDzyUtosbc0im4GT8vXonDSoovjIQU3TicI8xI4Gd1mGiDPzRzuqcWmM-ap_ggvls9P8lFBcR4gTUq-xCUnZjh-WOiD_RWMb5TLDFWvlsGKuVF8aPbDjbZrnPinFV0gK01JDonSYq7Vyb0DlYPyKyd-DXju5HvBbH214pwwKC7_TVWAacMMaz2N6VSLWV0pB238y9pCHrfN2dj0RXciYO04R1rQEgMgphiouEb80iaaCsbsFgQ3thXNMwRdFvpQyN8JSLvSFaeK75TGcq0q3TQgcCAVGhje4OdbLlueyO4KRjodVCqteVO5ktr1C2MKwj_pzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر ماهشهر همین الان
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/14975" target="_blank">📅 19:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14974">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
به وضعیت کاملاً غیرقابل قبولی رسیده ایم که ایران در مورد آزادی عمل ما در لبنان «حق وتو» دارد و این یک واقعیت پوچ و غیرقابل قبول است.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/14974" target="_blank">📅 19:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14973">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/14973" target="_blank">📅 18:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14972">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ6oTLpHi4mqrWI9GO_fluDK59_KN50DUQn1G1OYrmS7TGndKAxxKBH1Vy9olGHAY-0JNSkEp95beKbQN0cgR4qtdv_P05wawKZI955JkEFuhgEitaac2hM4S4diUtOel0fk2pX92_annksSVxoobWGXXyR79vjI4M-vJIcHUBoEPO-aNImYact0K7kPogz535yGWI10MqCFJscbneWaAPi37oRga4pA4OrF9L9qQ09ecdmaB6R6naPvypvKW8wT9M7kekWeaLHeOfe-TqS5VFKjNayAPDVgTNqxsyP4SJ-OjZkeCLi9y5Q6aMBG0LzG0bynqmaVjIp9YV2Snso8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرجنگی عمل نکرده موشک کروز تاماهاوک در ورامین
این حمله چند شب پیش انجام شد و ده ها سایت راداری در سراسر ایران اعم از کرج و تهران و چند سایت قزوین و جنوب کشور توسط ۴۹ موشک تاماهاوک منهدم شد ( به جز یک موشک تاماهاوک )
موشک های تاماهاوک بار دیگر نشان دادند از دقت فوق العاده ای در زدن اهدافشان برخوردار هستند.
@withyashat</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/14972" target="_blank">📅 18:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14971">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو تا چند ساعت دیگر سخنرانی خواهد کرد و این اولین واکنش رسمی او به اعلام توافق پس از ساعت‌ها سکوت است
🚨
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/14971" target="_blank">📅 18:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14970">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/14970" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14969">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/14969" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14968">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جزئیات دیگری از یک اتفاق قابل توجه درباره ساختار تفاهم اسلام‌آباد
یک منبع نزدیک به تیم مذاکرات در گفتگو با خبرنگار تسنیم، جزئیاتی از یک اتفاق قابل توجه در روز آخر مذاکرات مطرح کرد : بند 13 تفاهم‌نامه مربوط به این موضوع است که تا زمانی که برخی بندهای دیگر تفاهم‌نامه عملیاتی نشده، مذاکرات درباره توافق نهایی یعنی موضوع هسته‌ای صورت نمی‌گیرد.
وی خاطرنشان کرد: تا پیش از روز آخر مذاکرات، بند 13 شامل بندهای 4 و 5 و 10 و 11 بود؛ بند 4 مربوط به رفع محاصره دریایی، بند 5 مربوط به آغاز بازگشایی تنگه هرمز، بند 10 مربوط به اسقاطیه تحریم‌های مربوط به فروش نفت، پتروشیمی و مشتقات ایران و همچنین بند 11 مربوط به آغاز آزادسازی اموال بلوکه شده ایران است.
بنابراین بند 13 به این اشاره داشت که اگر این 4 بند گفته شده (4 و 5 و 10 و 11) انجام نشود، مذاکرات توافق نهایی آغاز نمی‌شود.
این منبع مطلع تاکید کرد: اتفاق مهمی که روز آخر مذاکرات به وقوع پیوست این بود که با پیگیری ایران، بند 1 نیز به بند 13 اضافه شد.
به گفته این منبع آگاه، معنای مهم این اتفاق آن است که اگر جنگ و هرگونه عملیات نظامی، از قبیل ترور و ... در ایران یا جبهه مقاومت از جمله لبنان اتفاق بیفتد، طبق تفاهم هیچگونه مذاکراتی برای توافق نهایی صورت نمی‌گیرد و طبیعتا اجرای تفاهم‌نامه (از جمله بازگشایی تنگه هرمز) از لحاظ ماده ۱۳ متوقف خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14968" target="_blank">📅 18:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14967">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عراقچی: جمعه تفاهمنامه ایران و آمریکا امضا می‌شود
اقتصاد ما نباید خود را متکی و موکول به این قبیل توافقات اقتصادی از طریق مذاکره با آمریکا بکند
در راستای منافع کشور، نیمی دیگر از راه مانده که باید طی کنیم که نیمه سختی خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/14967" target="_blank">📅 18:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14966">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu_Q6HqGdXSiemRMmUekTXxLymL92iFZvIgEbRnQ-DaH6VYyaJMnuckLL8LYUeEvzw_4yOr-Looqd5Z6hwOoH_6M2v2lhOzHv_A7OV_VyErTN6_StRFmNG33hQLLDNpImLv-SnK3lSnWWCbGsz8VlMc8Eu8sBf_JDfkTvaQrz1BWC4gMXQDq024P96nBrZIYruURwiKy98-0uakK-RFj7PiR9hybUzJ20MQTw4YAdRqPGkLC_D0IVTH88jt_D0jGgzKc6Oamv56Ep4eJ9uLmExgCgR9ZDcqOuGlpPJPmnMXSAY_NuBNuBh1Jo7wBUSMfCdKiEkFayrHoYWrakXq3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث: متأسفانه، اگر افراد را از کشورهای جهان سوم وارد کنید، به سرعت خودتان تبدیل به یک کشور جهان سوم می‌شوید و هیچ کاری نمی‌توانید در این باره انجام دهید
آمریکا را دوباره بزرگ کنیم!
@withyashar</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/14966" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14965">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادعای جی‌دی ونس درباره ایران: ما دیروز به صورت دیجیتالی پیش توافق را امضا کردیم
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/14965" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14964">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406b9170ab.mp4?token=NiZewHQpNYihyGg_ZhTI-OQjf72gz14dM5ZhOI1fnSH4U-ybkGtWFM5CWBMNxco6_CiA9moNR_1nG4MxZaLVie7XKfclzjhor4LA62TXVbonXbIbYXDKvopYPu5OSomnPWTJAyShXORYKMTK4kT67b7VtSyf_2Km3hUSXdwWWhhY4FzHZjAV0Uv3OE3fC9ql_rFDlDUVJXWi0XR9maSlK_yg0i5wC1lUmKfWAScNlDAnDsAoP97xSYuOxGDdKATpXOGo0Eup6zjxLStITtGVV8Vj1HYK8hEumRjWbOTvUcmh9xZQRWWYejmihbYf8D02j2EDxx6ai0yq0gt1iLexPzuPROTreNuntRgktak1tm5fn6qizaxgmvdr7yyo3SKnlpUcH1wrwSI0f3Jo8130moARXMPs6p3TNjMHbKHta1_f9FLsoVVsh4pnH1LK4ORXDU6ipixSYRP2lqa5rSNTmip_oN2h396qRxYLH4sv4qtO1EP6CE4cdh-Su1z1niyn5E_PrMfWF_tKiL6JeU_hAyWghgPQqjZEmAwKeavWZWVCiunZ2L6CZzgQr9lBT7fKLU3td9Jk5z2-TWP3OYxj3bjRa7pFsYoJPWZSoxVSByhMsNZc6hETlyzLiXXvJpzMRBuo2kN4WaTw7ZsB7F5lKcTh2mf6enJb0HIm2-BP6sI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406b9170ab.mp4?token=NiZewHQpNYihyGg_ZhTI-OQjf72gz14dM5ZhOI1fnSH4U-ybkGtWFM5CWBMNxco6_CiA9moNR_1nG4MxZaLVie7XKfclzjhor4LA62TXVbonXbIbYXDKvopYPu5OSomnPWTJAyShXORYKMTK4kT67b7VtSyf_2Km3hUSXdwWWhhY4FzHZjAV0Uv3OE3fC9ql_rFDlDUVJXWi0XR9maSlK_yg0i5wC1lUmKfWAScNlDAnDsAoP97xSYuOxGDdKATpXOGo0Eup6zjxLStITtGVV8Vj1HYK8hEumRjWbOTvUcmh9xZQRWWYejmihbYf8D02j2EDxx6ai0yq0gt1iLexPzuPROTreNuntRgktak1tm5fn6qizaxgmvdr7yyo3SKnlpUcH1wrwSI0f3Jo8130moARXMPs6p3TNjMHbKHta1_f9FLsoVVsh4pnH1LK4ORXDU6ipixSYRP2lqa5rSNTmip_oN2h396qRxYLH4sv4qtO1EP6CE4cdh-Su1z1niyn5E_PrMfWF_tKiL6JeU_hAyWghgPQqjZEmAwKeavWZWVCiunZ2L6CZzgQr9lBT7fKLU3td9Jk5z2-TWP3OYxj3bjRa7pFsYoJPWZSoxVSByhMsNZc6hETlyzLiXXvJpzMRBuo2kN4WaTw7ZsB7F5lKcTh2mf6enJb0HIm2-BP6sI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: ایرانی‌ها می‌گویند قرار است به یک صندوق ۳۰۰ میلیارد دلاری برای بازسازی دسترسی داشته باشند. درست است یا نادرست؟
جی‌دی ونس: چنین چیزی می‌تواند در دسترس آن‌ها قرار بگیرد، مشروط بر اینکه به تعهدات خود در این توافق پایبند باشند.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14964" target="_blank">📅 17:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14963">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHzwBlIJDEE-WQ3S1LW7fcueuzIF-7Y8XLR3MRNtDN6y6YQoolWdXVlRhCi-V4gsdd87vfKy17nibFFj98uVV_HCsPYM8ygYfaBm0iB2_xvwQ05ZajZ8wI5MhHa6dCs1IksAH2J0Z1nK9_x0NnouXXIANDK121EwDuu8g7ADsWPFYatVq31X_XHWTFKkpsCTuWA46JHjcKMOmdKdqclZ3oYgdOj9GYOgTfJRxstSVEvlXFheKyLXYEnfDcZC0Xb8UV6U9dJZXEKugZVVCysQeD89Pb7LjWVjYb6yKa3K6ONZBzm32X823pNX9H6hLu4oAaLSue0zhKotgHSY1v79Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث: کشتی‌ها شروع به حرکت کرده‌اند، بسیاری از آنها با نفت بارگیری شده‌اند، از تنگه هرمز خارج می‌شوند.
آنها در امتداد «بزرگراه» جنوبی حرکت می‌کنند که کاملاً ایمن، مطمئن و بکر است. مناطق دیگری برای سفر نیز وجود دارد!!!
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14963" target="_blank">📅 16:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14962">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مکرون:  پرداختن به برنامه موشک‌های بالستیک ایران در مذاکرات آینده مهم است.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14962" target="_blank">📅 16:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14961">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تسنیم: یک منبع آگاه در گفتگو با خبرگزاری تسنیم، درباره وضعیت نیروهای آمریکایی در منطقه طبق تفاهم اسلام ‌آباد گفت: بر اساس ماده 4 تفاهمنامه، 30 روز پس از توافق نهایی، نیروهای رزمی آمریکایی باید از محیط پیرامونی ایران خارج شوند.
همچنین بر اساس بند 9 تفاهمنامه، در طول 60 روز مذاکرات برای توافق نهایی، نیروی جدید آمریکا در منطقه اضافه نمی‌شود و ایران نیز در این بازه اقدام هسته‌ای انجام نمی‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14961" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14960">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مقام ارشد کاخ سفید به آکسیوس:
هیچ دارایی مسدود شده ایران پس از امضای یادداشت تفاهم نامه در روز جمعه میان ایران و آمریکا آزاد نخواهد شد، همچنین هیچ کاهش تحریمی نیز برای ایران اعمال نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14960" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
