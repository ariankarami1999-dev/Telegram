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
<img src="https://cdn4.telesco.pe/file/EO0nGAgN7y0ioDz39dUd0ETLm18aF0ymHcc-WZ71t5mKinEnKubP5tVyT7PcYd8JKmO3K1r7i-GimMyqfB6KgF0fX0llHfYhQ6NZP5b6q6OVkvCRtYqtYtt8HntatS85WMWU3m20-2bZhNVe_6ltm0NRtpOSsQrM7D1lV5jAokEjNkfjLUxb5O3uzHbuZtp51KFFTBjNpZcSLQk438bWS_FVcXALVyVDHC4FaTWPu_I-DpHtQsaDXnPJv3nNVZ0WbyMbEpOHo5S72a23iZnfMCY6Dq4l1AHYmHB0T3eGBwZ9hkQrfQHFlW7CBbAN_k3XwpHj0_QbrBKrl5_52LX9OQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.28M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 16:52:31</div>
<hr>

<div class="tg-post" id="msg-673448">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq43cVdlYpL_aYf5DpQS790jlOXawjGkLUL61L1uEFm8j0iBHs7NQa43tj_4hvZYx4pA0lzvRrEUt7mGgFKZdOuxFUtzwZuUfOsg7gWrxXw68QFpJ1GEY9O7QazC5d-9Rs_rUarK3H0TNZnuJOXehvctIbJGsDaHXsvVxqPdYRbTpf7Dn6Qlos50T2_ocPNEh3LJq8F-vhUoM7eOaxU_r8IB1JWszLk1M0uIGSr5ztH1o971d3rEBO-jkEB9sUdhFsMQ5DCnAxSV4h55fq7NAlhfh4IHxr1fw-NIE5ZypFfNZY0dBKnN8dQraPF1YQUVNWwRzBsOQmRhIE-AsH7_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به مناسبت روز جهانی ماه؛ نزدیک‌ترین همسایه زمین و شگفتی بی‌پایان فضا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/673448" target="_blank">📅 16:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ضربات سنگین دریادلان نیروی دریایی سپاه به ارتش کودک‌کش آمریکا با حمله همزمان در سه محور
🔹
ملت به پا خاسته و حماسه آفرین ایران اسلامی، با توکل به خدای متعال و دلگرم از حضور هوشمندانه شما مردم بصیر در صحنه، دریادلان نیروی دریایی سپاه با حمله همزمان در موج ۲۳ عملیات نصر۲ در سه مرحله با رمز مبارک یارقیه (س) ضربات سنگینی به نیروهای تروریستی آمریکا در منطقه وارد کردند.
🔹
مرحله یکم: حمله به سوله‌های نگهداری و تعمیرات پهپادی واحدهای آمریکایی مستقر در فرودگاه اَلصَّخیر بحرین که منجر به انهدام آنها شد.
🔹
مرحله دوم: حمله به سوله‌های آماده سازی شناورهای تی‌اف۵۹ در بندر سلمان بحرین که منجر به تخریب آن گردید و خسارات سنگینی به شناورها وارد آمد.
🔹
مرحله سوم: به آتش کشیده شدن سوله‌های محل استقرار و پشتیبانی و تجهیز نیروهای تکاور ویژه دریایی در پایگاه عریفجان کویت و منهدم شدن آن به صورت کامل.
🔹
حملات کوبنده رزمندگان اسلام با انبوه موشک‌ها و پهپادها در مقابله به مثل و پاسخ به تجاوزات ارتش کودکش آمریکا ادامه دارد.
🔹
رئیس جمهور بی‌خرد آمریکا که بارها به ناآگاهی و بی‌خردی خود از اوضاع عالم، اعتراف کرده و می‌گوید بدون اطلاع از عمق نفوذ امام شهید ما در مردم جهان و عشق و علاقه عمیق مردم ایران و سایر کشورها، ایشان را به شهادت رسانده و اینکه می‌گوید بی‌خبر از اهمیت تنگه هرمز در اقتصاد جهان در این منطقه، جنگ به راه انداخته است، شب گذشته باز هم بی‌خردی و ناآگاهی خود را آشکار کرد و اظهار داشت تعداد موشک ها و پهپادهای کمی برای ایران باقی مانده و رو به پایان است.
🔹
رئیس جمهور قاتل آمریکا بداند اگر این جنگ چند سال طول بکشد به اذن الله تعالی تا آخرین روز آن موشک ها و پهپادهایمان بر سر جنایتکاران آمریکایی خواهد بارید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/673446" target="_blank">📅 16:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac7897cd4.mp4?token=DVYjYs_aoGC4KrsPvuawQ04KVEJCAwxEkVnRZrsWd9wWYeeEe8lmaNIZTsLZbRpc2c0jvwR5DIa5FNjctfChTstoirfIOiE_9vNyRo8NC6vQzzK_PohhreP-nQZ7mpDDq3TZwX3jgbmD-MeDJTJVU8uNh5ZVyiLyhXuD6vB9bqiI8KawPjKlAZ51yQU8rezxillMs5dId57nOL90S9VWzwtlWtj-xmId0Ucn_dEAISKSyj-vqCAa_Psljuvz2U4db2mEBT3_NC5Aii4ZnYgGqgSHRckJNj46jZ9W-TcmlGZNSuoDlaKo0O4EBoZ7CULI81MO4mY0sAm0WypAJqBGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac7897cd4.mp4?token=DVYjYs_aoGC4KrsPvuawQ04KVEJCAwxEkVnRZrsWd9wWYeeEe8lmaNIZTsLZbRpc2c0jvwR5DIa5FNjctfChTstoirfIOiE_9vNyRo8NC6vQzzK_PohhreP-nQZ7mpDDq3TZwX3jgbmD-MeDJTJVU8uNh5ZVyiLyhXuD6vB9bqiI8KawPjKlAZ51yQU8rezxillMs5dId57nOL90S9VWzwtlWtj-xmId0Ucn_dEAISKSyj-vqCAa_Psljuvz2U4db2mEBT3_NC5Aii4ZnYgGqgSHRckJNj46jZ9W-TcmlGZNSuoDlaKo0O4EBoZ7CULI81MO4mY0sAm0WypAJqBGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی رباتیک Honor با بازوی رباتیک برای دوربین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/673445" target="_blank">📅 16:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl0_HBMPqPHgGgAK7GGfsIlHED7JRA97O9qLfBpdXmw1JFcmsXR-OzGvh4LEzdwGhh7vb1S5gng918ryO0JUH_X8lBjWRl25e6NrzmqSM4aQwR73SZDsTlk5sIv1bNX9G5fKvD0uuIVVklZp2BjjO9QJ1pqey3lL1ggyLfCw3lnxMnbRgRcGEsMhama8f4rwg1ooRLSoTJHQY-WVLHrUVjg5REN1_Ust96NBuaObkZGe9WariAa1RU04IbCfz0yk-WYw5AbeRSe4ZpcPKhSoIcMjIN16CgoIRWyGSNuAj587ZIlS8lTptf6if4H_121Y4vyJWydk0db9cPwyNfNk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا هویت دو کشته خود در اردن را اعلام کرد
🔹
ارتش تروریستی آمریکا اعلام کرد دو نظامی‌اش، «تایلر جیمز فیهان» ۲۵ ساله و «ایزابیلا گونزالس» ۱۹ ساله، در حمله ۱۷ ژوئیه ۲۰۲۶ به پایگاه «موفق سلطی» اردن کشته شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/673444" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پاسخ بقایی به احتمال دوباره مذاکرات و گنجاندن شروط جدید از سمت ایران: ما فعلا متمرکز به دفاع از ایران هستیم
🔹
سفر نخست وزیر عراق به ایران بسیار مهم است و نقطه عطفی در روابط دو کشور است. در جریان این سفر چند سند و یادداشت تفاهم به امضا خواهد رسید.
🔹
وزیر…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/673443" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5597d61522.mp4?token=s14Iw2yPtjOiYCOtxlTLlMNMvC7Z21dNN7VE_-rjBpiBvIfOgIrpGqLovZpTSSFBgbUIsK317o2ILcu5Wx_c3u6hcfBKt1W8zJCMw6mbcZplN44mmGaZ3Lh-Yq_sX54n1swCrpj2YpXbCW4KTvQcUsQWFjackQNPlPJXjliy94JEkjuiARZ9jaDTLGemiIIC0yo6mrgSELtT4p9nmMxhd-Fj94BCAta5gEkhOmRMsB13NgzE4KDJwvsLWWX6FgKdgZ0VBE9X14WkfONqhbARmYnlFWgv1QjoyI3QyRa14wdUJjmzLLt0djpo2pWDVnfdwBqd8dcGl0qHyauDU9u3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5597d61522.mp4?token=s14Iw2yPtjOiYCOtxlTLlMNMvC7Z21dNN7VE_-rjBpiBvIfOgIrpGqLovZpTSSFBgbUIsK317o2ILcu5Wx_c3u6hcfBKt1W8zJCMw6mbcZplN44mmGaZ3Lh-Yq_sX54n1swCrpj2YpXbCW4KTvQcUsQWFjackQNPlPJXjliy94JEkjuiARZ9jaDTLGemiIIC0yo6mrgSELtT4p9nmMxhd-Fj94BCAta5gEkhOmRMsB13NgzE4KDJwvsLWWX6FgKdgZ0VBE9X14WkfONqhbARmYnlFWgv1QjoyI3QyRa14wdUJjmzLLt0djpo2pWDVnfdwBqd8dcGl0qHyauDU9u3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران وطنم
🔹
پیام‌های صوتی ارسال‌شده به پویش «ایران وطنم»، بازتابی از مهر و غیرت هم‌وطنان است که با گویش‌های مختلف، کلامی از جنس امید برای مردم صبور جنوب ایران به یادگار گذاشته‌اند.
🔹
این هم‌صدایی زیبا ثابت کرد که خانواده بزرگ ایران با تمام اقوام و تفاوت‌ها، در شرایط دشوار شانه‌به‌شانه یکدیگر می‌ایستند.
🔸
شما هم صدای گرم خود را ارسال کنید تا پیام‌آور همدلی دیارتان با مردم غیور جنوب ایران باشید.
👇
#همه_باهم_برای_ایران
#ایران_وطنم
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/673442" target="_blank">📅 16:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سخنگوی ارتش: جنگ تا دستیابی به بازدارندگی کامل ادامه دارد
🔹
امیر سرتیپ اکرمی‌نیا تأکید کرد که بر اساس عقلانیت و تجربه، جنگ تا ایجاد بازدارندگی کامل برای جلوگیری از تجاوز مجدد دشمن ادامه خواهد یافت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/673441" target="_blank">📅 16:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7297ee97.mp4?token=rvDQnVzva6JQIHUnGRmOjQEP9XJFpYkg4cGAA-48Em6cMJjESHZ-G4sUpJQQ3Id5UHvtBWaMPcx5F85_2qeMv0h48uPhWrh-KFjS39G3qSLv0YaSC7q897uiLQ-rUJv0ja5C-gr2ZaPi0LkFOgH9-59PNnyWii5txV_yjogM4co2bAA484Pli8dsBSHqt4XP7Xkt364bNDZocepmvqfqCJUlDRfnQ-SzzFa_GL5edAb9chyHR8C8VrteyCI9_Bfz6EQPdnMwpaZoj-ww31RxMi6nUrac75gaUvA_SRtiHWCusHgrTKwou4hUjYUrT1R7c4dw8_GjZkEgN2YqNI09QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7297ee97.mp4?token=rvDQnVzva6JQIHUnGRmOjQEP9XJFpYkg4cGAA-48Em6cMJjESHZ-G4sUpJQQ3Id5UHvtBWaMPcx5F85_2qeMv0h48uPhWrh-KFjS39G3qSLv0YaSC7q897uiLQ-rUJv0ja5C-gr2ZaPi0LkFOgH9-59PNnyWii5txV_yjogM4co2bAA484Pli8dsBSHqt4XP7Xkt364bNDZocepmvqfqCJUlDRfnQ-SzzFa_GL5edAb9chyHR8C8VrteyCI9_Bfz6EQPdnMwpaZoj-ww31RxMi6nUrac75gaUvA_SRtiHWCusHgrTKwou4hUjYUrT1R7c4dw8_GjZkEgN2YqNI09QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما جنوب را نه فقط برای دریا و نخل‌ها یا نفتش که برای مردمی دوست داریم که همیشه کنار ایران ایستاده‌اند... #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/673440" target="_blank">📅 16:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
وزارت کشور بحرین: هشدارهای حملهٔ هوایی فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/673439" target="_blank">📅 16:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2cd50499.mp4?token=bbCXNEhG2TkRUaAH0_QUFw6Mv95Nak4KsaFcm-WpDibtG1BETKs4A4rr6F9cn_J4-15cUBtdZgSsUlPjKpSkH1JYvN5DKkB3eBghtV_815CXqonrWAqhh_HNMJnNq99Zq5FuAz932xKHw88hMwgZfCyebd4TvZxlhekGRTZePfXGWQpTOjSEKbSy3-HTIB-74JjXe7bBcruYO7dnysIKyOwS5smHNdYGJ74rg6uwCCCbjjt2EslLfwqp3eDXfV8fRUilj-Op3eUN2tK-zP_DfdOHTLYJvb9NVlj4I9S7i4Low6ty1OvUeM1JWjiVKcSUXnRY1rwqiuRmKvEVXD6tbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2cd50499.mp4?token=bbCXNEhG2TkRUaAH0_QUFw6Mv95Nak4KsaFcm-WpDibtG1BETKs4A4rr6F9cn_J4-15cUBtdZgSsUlPjKpSkH1JYvN5DKkB3eBghtV_815CXqonrWAqhh_HNMJnNq99Zq5FuAz932xKHw88hMwgZfCyebd4TvZxlhekGRTZePfXGWQpTOjSEKbSy3-HTIB-74JjXe7bBcruYO7dnysIKyOwS5smHNdYGJ74rg6uwCCCbjjt2EslLfwqp3eDXfV8fRUilj-Op3eUN2tK-zP_DfdOHTLYJvb9NVlj4I9S7i4Low6ty1OvUeM1JWjiVKcSUXnRY1rwqiuRmKvEVXD6tbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ۳۰ روز قند رو حذف کنید ، چه اتفاقی برای مغزتون می‌افته؟
🧠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/673438" target="_blank">📅 16:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673435">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/673435" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673433">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3047709d8a.mp4?token=KqPqiuVI0JIcby-Pkhnd7JGf55-2f6pfk0vBRzgoGzNDl8054lezP109vIFrvqzmGzOtEapYanXQ8W6nnzdAcip99D8G9ka2CBOKtbk78D7A7njk-t932UA_ti_Fpc45kIMIePJ-fQYKGRT8o2LhuLj0NNoXjLduwKhZ9wrvgSykOTL-ifS8-8k4TPpw5h6skdTtRIE1f0MVI1zcTrO4l7E3CQr-NORHqvyql79FlrQoSXSb79_1qQo75okxKpwQ1ClkexaIfhlE-j0HdegNIEH8-w0u0VpXXqyvrUjb_39vtvRal47bBqQVfXUaYNLHPU1snaf_KvvKYn2pl8CqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3047709d8a.mp4?token=KqPqiuVI0JIcby-Pkhnd7JGf55-2f6pfk0vBRzgoGzNDl8054lezP109vIFrvqzmGzOtEapYanXQ8W6nnzdAcip99D8G9ka2CBOKtbk78D7A7njk-t932UA_ti_Fpc45kIMIePJ-fQYKGRT8o2LhuLj0NNoXjLduwKhZ9wrvgSykOTL-ifS8-8k4TPpw5h6skdTtRIE1f0MVI1zcTrO4l7E3CQr-NORHqvyql79FlrQoSXSb79_1qQo75okxKpwQ1ClkexaIfhlE-j0HdegNIEH8-w0u0VpXXqyvrUjb_39vtvRal47bBqQVfXUaYNLHPU1snaf_KvvKYn2pl8CqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معادله حسابداری رو با این زبان ساده و مثال کاربردی یاد بگیرین #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/673433" target="_blank">📅 15:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673432">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
امیر سرتیپ شیخ: آمادگی دفاعی مؤثرترین ابزار حفظ صلح است
معاون اجرایی ارتش:
🔹
هر اندازه توان بازدارندگی کشور تقویت شود، احتمال شکل‌گیری تهدید و بروز جنگ کاهش خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/673432" target="_blank">📅 15:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673431">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d40c47dcf5.mp4?token=lop4D_pD_8h1lmvhSs0ldWb6DFKqNcXQhvmZJAVCqqhxAe-11E5Lr1ZWA3rI7IwJ_WmATO44q_31Pz1a_KlsEEumQEm7QzQdarRbYTHTL1eEyhY5ayBv1wGqtnRoiJdR1Qe3dlhjWK8lcBtoxtnOIb3vbLqebVcZICu3nGuJdcjaX9GIzHQ82nML0c85cHwy7zKp7CqF3znogAlg2wCvsqGMiFpBtFeKy3JQ7yW_lyZl8aQdeOJnGQL58gZql_AtaMJ6Nxzo4k_pSAxidyutiiZfUSsgRlVh2kQ9d0DG0JRRNtHYf0LRbsZMBZyX8EDor1l6Puc0vjiieLvGv-V4JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d40c47dcf5.mp4?token=lop4D_pD_8h1lmvhSs0ldWb6DFKqNcXQhvmZJAVCqqhxAe-11E5Lr1ZWA3rI7IwJ_WmATO44q_31Pz1a_KlsEEumQEm7QzQdarRbYTHTL1eEyhY5ayBv1wGqtnRoiJdR1Qe3dlhjWK8lcBtoxtnOIb3vbLqebVcZICu3nGuJdcjaX9GIzHQ82nML0c85cHwy7zKp7CqF3znogAlg2wCvsqGMiFpBtFeKy3JQ7yW_lyZl8aQdeOJnGQL58gZql_AtaMJ6Nxzo4k_pSAxidyutiiZfUSsgRlVh2kQ9d0DG0JRRNtHYf0LRbsZMBZyX8EDor1l6Puc0vjiieLvGv-V4JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
سرم سفیدکننده دندان LANBENA
🦷
کمک به کاهش زردی و لکه‌های سطحی دندان (چای، قهوه، سیگار و مواد غذایی رنگ‌دار) و روشن‌تر شدن لبخند
😁
✅
روش استفاده:
بعد از مسواک، دندان‌ها رو خشک کن؛ ۱–۲ قطره روی گوش‌پاک‌کن/برس بزن و فقط روی سطح دندان بمال (با لثه تماس نداشته باشه).
⏱️
۱۰–۱۵ دقیقه بمونه، بعد با آب ولرم آبکشی کن.
🗓
روزی ۱ بار (ترجیحاً شب‌ها) | دوره ۷ تا ۱۴ روز
برای دندان حساس: یک روز در میان
⚠️
روی دندان آسیب‌دیده یا لثه ملتهب استفاده نشه.
🍵
تا ۱ ساعت بعد، مواد رنگی نخورید.
📦
حجم: ۱۰ میل
🟢
قیمت تخفیفی: 898 هزار تومان
🔴
قیمت قبل: 1̶1̶6̶7̶ هزار تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/56228/180124/</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/673431" target="_blank">📅 15:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673430">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fa5c4042e.mp4?token=qKtLbpov1aJj5TujqE2KwNiLSedt3fdBdE9Fc0t_7JN4FiAi-J4GAa8UsLMEBle51sNDoMv9FbFTiyzIwNYIppeXYqXYgTHY01bTXi07Km15t1jMB1As7DscwRMQzlF69axTTlxWrkVW6Auit0bqMMQcKmkz2Acn-CbVgPxoh3te2TJ4wMv7uccG0BvYC9B-X_VQlfnkAnO1YhyVUcTG1zhhJxFji_aswq072ssub0oroyVFuKqGriuUfpzhYhxI2c8O5IcUTEAlZ0bswkDDvPlv8GBA8utT8znhixl3ZQsp96pZeczS6PeS-QiZ2xMtXtfcFP04XwgxitT-v9JmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fa5c4042e.mp4?token=qKtLbpov1aJj5TujqE2KwNiLSedt3fdBdE9Fc0t_7JN4FiAi-J4GAa8UsLMEBle51sNDoMv9FbFTiyzIwNYIppeXYqXYgTHY01bTXi07Km15t1jMB1As7DscwRMQzlF69axTTlxWrkVW6Auit0bqMMQcKmkz2Acn-CbVgPxoh3te2TJ4wMv7uccG0BvYC9B-X_VQlfnkAnO1YhyVUcTG1zhhJxFji_aswq072ssub0oroyVFuKqGriuUfpzhYhxI2c8O5IcUTEAlZ0bswkDDvPlv8GBA8utT8znhixl3ZQsp96pZeczS6PeS-QiZ2xMtXtfcFP04XwgxitT-v9JmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر شلیک موشک های سوخت جامد، خیبرشکن، فاتح ۱۱۰، ذوالفقار و موشک سوخت مایع عماد در عملیات آفندی دقیق و تاکتیکی علیه مواضع آمریکایی در منطقه در موج های ۲۱ و ۲۲؛ عملیات نصر ۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/673430" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673429">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ff2d4703.mp4?token=JeJK2gUpTVdrew0Q7YfOjn8f8CCLKw2J-PpyuaPA3louPfwl3LWfsr0Q5QkrCFGIbfk9BmR3Blsz5ml0GYtH-2GjBaH_C6fUG0Xjxd7MMawIBHxTFBgZleJGh2fj97o225jAg16wIs-pGGg9lgXtzVgLzxJ-B_2hKlGqGFjDIwGPy9CaIhdPMwwJ_dUZ9KE0miiTHcdoCu9NG8IthPFps0XHM6QhVh8nKYweAQEjP1VEe3GjvTuva1BaILu2wS5nC1E9Y8LQ83ryzx3eqiUneaNMfdUoDYuR_ycIRl1PKRN9jfjhDOMywfwfvu8VNlN8U30Z7dbwyOs0IUH2b620WYzB4Vr1hnoUdGaBXSRM92YIQ3uVbBdJixeZPfLqpZGqR6mFAXGhLnqBqpa3Faysl9dsn3nnR5oUT99E8Se07BJCOcT-AgAeLXcvaFnYU9jeTxwiX74MUIwbqnHWqPWcJndRGfFFMNhpJYInBkfg7BInHAX38nQU6xckphWGOGWQuRQS_UMVCp_98B1qJ4Tg99rceFZmDmvSXxZC4ZsH8SkIp6vnKOtJaNioLXTRm78q6N0imFZGknvzgeS2YJb7KNXtk2x3b8Qh6mVhGhKvvKyLarSmkzWMbZeo3JNTBBmqtmBduDw2DYLfmGH_fb2H5lv2oQQa0hlr8IOFa3R85UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ff2d4703.mp4?token=JeJK2gUpTVdrew0Q7YfOjn8f8CCLKw2J-PpyuaPA3louPfwl3LWfsr0Q5QkrCFGIbfk9BmR3Blsz5ml0GYtH-2GjBaH_C6fUG0Xjxd7MMawIBHxTFBgZleJGh2fj97o225jAg16wIs-pGGg9lgXtzVgLzxJ-B_2hKlGqGFjDIwGPy9CaIhdPMwwJ_dUZ9KE0miiTHcdoCu9NG8IthPFps0XHM6QhVh8nKYweAQEjP1VEe3GjvTuva1BaILu2wS5nC1E9Y8LQ83ryzx3eqiUneaNMfdUoDYuR_ycIRl1PKRN9jfjhDOMywfwfvu8VNlN8U30Z7dbwyOs0IUH2b620WYzB4Vr1hnoUdGaBXSRM92YIQ3uVbBdJixeZPfLqpZGqR6mFAXGhLnqBqpa3Faysl9dsn3nnR5oUT99E8Se07BJCOcT-AgAeLXcvaFnYU9jeTxwiX74MUIwbqnHWqPWcJndRGfFFMNhpJYInBkfg7BInHAX38nQU6xckphWGOGWQuRQS_UMVCp_98B1qJ4Tg99rceFZmDmvSXxZC4ZsH8SkIp6vnKOtJaNioLXTRm78q6N0imFZGknvzgeS2YJb7KNXtk2x3b8Qh6mVhGhKvvKyLarSmkzWMbZeo3JNTBBmqtmBduDw2DYLfmGH_fb2H5lv2oQQa0hlr8IOFa3R85UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه‌ ما یه ریشه داریم... ریشه‌ای که اسمش ایرانه هرچقدر شاخه‌هامون دور بشه، ریشه‌مون همونه #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/673429" target="_blank">📅 15:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673427">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی کامل برای رویارویی با هرگونه حماقت ریاض، اعلام کرد هرگونه تصعید نظامی را با تصعید متقابل و همه‌جانبه پاسخ خواهد داد و از ملت یمن خواست بسیج عمومی را تقویت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/673427" target="_blank">📅 15:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673426">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec3e9b7c6.mp4?token=W27zGnfIqqe-6hC-kE2SKrszFwN9fxJ9RlT9GYmqQYmwbojUsRJmo5MhYTZB3iA7P-qC63K9wRBnpmiCjBBzbpty-PUlq_w9Y8WDpKt78_sBzHSPE_XcIxM9zScGrsSdj_SFmtaRjiFabfuPoICL76JeF-dHeVRz8IyOU6rLu5WA4kd0NHQn7zybkNUmD2HsyOmvTxIaRnPJTqdWmR4fxPdnykfoJBY0yCwOQ0a68rvSRAcoQIoRswDbx7NMUPaS-uOhywCf_1yaD4NMY_J6SVj8NbKjr2vc0TRQi2P5CxwfnpHgXGcQT_HTbm_BAg9Qpt49X7bQjHrZCRD5I9NjeWtJm73uh-E9y_gaFLEg-DeYO9DgJP5dfK1FD-gQYDbO3Eg70yBA8bnCLo02QCayTeWDICN03wtq6Bt9dW85MZe_-R3XWwiSyBC-ChkcJfxy1ZJ933vn12TRPt6D2eN6HW5donUjPAOldHM3bktC6Aem3o5c33l-AKwSNIknNoWiDBOygCZiFc-rYkxKqJysti0V19hObMwkOZo2I2uQsjAsW58TORwwVTw1VWWG5LZNrH54ywzwALKtBstbdhLr6FyBuJN2E1tLVsf7Cy-YGfK5RN5J8CHBaV98g9CHWKlhBR86924P_mLl_lJlg3dnSb0334YsB7NrBJ0L0gFTFXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec3e9b7c6.mp4?token=W27zGnfIqqe-6hC-kE2SKrszFwN9fxJ9RlT9GYmqQYmwbojUsRJmo5MhYTZB3iA7P-qC63K9wRBnpmiCjBBzbpty-PUlq_w9Y8WDpKt78_sBzHSPE_XcIxM9zScGrsSdj_SFmtaRjiFabfuPoICL76JeF-dHeVRz8IyOU6rLu5WA4kd0NHQn7zybkNUmD2HsyOmvTxIaRnPJTqdWmR4fxPdnykfoJBY0yCwOQ0a68rvSRAcoQIoRswDbx7NMUPaS-uOhywCf_1yaD4NMY_J6SVj8NbKjr2vc0TRQi2P5CxwfnpHgXGcQT_HTbm_BAg9Qpt49X7bQjHrZCRD5I9NjeWtJm73uh-E9y_gaFLEg-DeYO9DgJP5dfK1FD-gQYDbO3Eg70yBA8bnCLo02QCayTeWDICN03wtq6Bt9dW85MZe_-R3XWwiSyBC-ChkcJfxy1ZJ933vn12TRPt6D2eN6HW5donUjPAOldHM3bktC6Aem3o5c33l-AKwSNIknNoWiDBOygCZiFc-rYkxKqJysti0V19hObMwkOZo2I2uQsjAsW58TORwwVTw1VWWG5LZNrH54ywzwALKtBstbdhLr6FyBuJN2E1tLVsf7Cy-YGfK5RN5J8CHBaV98g9CHWKlhBR86924P_mLl_lJlg3dnSb0334YsB7NrBJ0L0gFTFXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیامی چهارصد ساله...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/673426" target="_blank">📅 15:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673425">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEeSOvEUjU6UebBg8c_MyMrUB34ga8fYvIFoglEqTPuDaW37wBOWf8SJcf77smxdz-zib8d8v22ZQ111BR658rTD-JQqXAuH2rIkrCMy-0Pmg9yG6bMNtjRfchQ-qRAzsla8rcXvuQcHthnrCCOQ8XiBb7GrUjYe6dSgxm7WYpp5chUWYtkbA1VnUTDjHCvNm5iob3qdYYVsAkT9MRDIzCN7ncpmglOTQCATs33_kVtSSjZqzxq7U3fLzZm6jwt1XDoa4SsWc4Rw47v53v0vh31QdPNMGeocStJn1yLh1QITI5CTddGCgsSz0ZfN51dxHLk8psuA7zXV51hNiVVJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش قیمت نفت در‌پی بعضی ادعاها درباره آینده جنگ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/673425" target="_blank">📅 15:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673424">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای رویترز درباره پیشنهاد آتش‌بس ۱۰ روزه
رویترز به نقل از یک مقام ایرانی:
🔹
میانجی‌ها پیشنهاد آتش‌بس ۱۰ روزه را برای گفت‌وگو درباره راه‌های احیای تفاهم‌نامه اسلام‌آباد ارائه کرده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/673424" target="_blank">📅 15:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673422">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پیشنهاد پاکستان و قطر برای بازگشت به میز مذاکرات
🔹
پاکستان و قطر امروز دوشنبه پیشنهاد مشترکی ارائه کردند و در آن از ایران و آمریکا خواستند به عنوان گام اول برای ازسرگیری مذاکرات، به مواضع خود قبل از ۹ ژوئیه (۱۸ تیر) بازگردند./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/673422" target="_blank">📅 15:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673421">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-p3Tbof02MAx38b7csGb9_NzAUKVbvP0sJBe5Aw8dhf3qk13RBn18gLTnWBdtDQNm50Kae7rL4W25U8qbycAPaSw8SzMQoAH-QaJr5OZ39JfJHHVXmygHGjkpoCtjl_zgdNniPq5lhWldZV4ZtnCBvSmA0IqL0nUZnj12Hon24OVHLRs5D_eo8lNeSTu5J5pNHHu8jNbfoWwRCT5hHAPKhlhoCaoYuJJJ3X1g6PG5xra9GHp0235mEo7lJk3Kp14PXV4LlY-zYTPFya17YEzEGsQpa7TbFMGpIRvDj1vNHc0FhEv4p7C6n64HwOhOgZpTpIboSvwIXU7lTzdjay4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اژه‌ای: من شهادت می‌دهم که رئیس‌جمهور مخلصانه در حال خدمت به مردم و نظام است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/673421" target="_blank">📅 15:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673420">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlKz_q8Te5tU-i_uyHf-bOFTl_cd4j88as1hXXYrlzkavvJuqRZPwdOqgjVxp-AXY5Z2Msf9UFObnrhDuvIGeuPcoaHhYaPmoDwz3bBmrDb8cSPwTxm_3wRzLmPUabhDYIWx6uqoWgcBd00iz42EKjHGlVQ_doF5NWmK-mnuPk4m7w7zEh6UiMOMAKRXA23gj5Y-1UuPiQDJcwpBjHBAR0rrbvShgOGYKOcwMl7_hRHUZaC22At38y7VYVRkUPOZgE8U3tWf5svPM1aYE2zKB1m_f_MNAreR5fD6z5Nw_35rnf3u1xi5jWMIgVySnAAjizKec-YfppUs89Uxxck6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استارمر اعلام کرد امروز دوشنبه دوره مسئولیتش به‌عنوان نخست‌وزیر بریتانیا به پایان رسید.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/673420" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673419">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C71EPojgB2PQEYMAOsu1T1E6h_HWwJ7dklix9EOtOyAEigkhIVtxybe3aYcZ8ePRp2MbaDSrJEdIbKzalURjCgywFCGaISGXPknBVMFbraM0_zdgevAn65hOQucyCp-joZBrPJ_fsa5lVbpexXT_ZXprm82vJyKhaLBR8OjlBd7T4QCD02iORjXOdFeZL4vGcJrUI5xmMKl0o0a0I_Ih4Tq_GBbGO1Efo_AVuKE_iSJX79vmN_3J688uMmorq8MomYWXIed3UOuqNhkusi7HCwMRpagzVvSWMVlIgPlkEQEsL0_PNepaCJmVwVSzEFZhnNFKZ4-ND2E_h7tHa0DOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ‌زرد: بر اساس یک نظرسنجی، اکثریت مردم آمریکا از توافق با ایران حمایت می‌کنند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/673419" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673418">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سازمان مدیریت بحران: ۱۰ مصدوم در زلزله کرمانشاه؛ خسارت مادی ناچیزی گزارش شده است.
🔹
سرپرست وزارت دفاع: تولید موشک و پهپاد در طول جنگ متوقف نشد و چند برابر افزایش یافت.
🔹
استارمر اعلام کرد امروز دوشنبه دوره مسئولیتش به‌عنوان نخست‌وزیر بریتانیا به پایان رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/673418" target="_blank">📅 14:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673416">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4d38b366.mp4?token=pKvhcyN2s4ewEAcRNVpzZF-LbIdntxFNUZ9vUzrtXo0RxbB_KpVKWFEVOUPLb35bNOTl6aJi83jwW3ZjEIUTCPTf9Q_lJLmOuknoG5iYOdR0Q-JSoDjiBJ6rDRyo2vhWgoXKmVtgUMwIZqQnJgRokNaJ73a5Suc3MPVpAFt8AlvYWTzQAhSlBoaQ9qM4z7qRfW7uKnTE8ILcuvzSccXmdrlPkjW6SUUfP7T-BsHFXQeGbamxkteQkQ1FyWckaCkC7gdV9tf4PqC9dL3TKNyIUatTbJH49YQ59QalVv66cDWF8ZpLFJ8RjIh-ikcl90bkqMuP-lFDipYAODuA1Bh-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4d38b366.mp4?token=pKvhcyN2s4ewEAcRNVpzZF-LbIdntxFNUZ9vUzrtXo0RxbB_KpVKWFEVOUPLb35bNOTl6aJi83jwW3ZjEIUTCPTf9Q_lJLmOuknoG5iYOdR0Q-JSoDjiBJ6rDRyo2vhWgoXKmVtgUMwIZqQnJgRokNaJ73a5Suc3MPVpAFt8AlvYWTzQAhSlBoaQ9qM4z7qRfW7uKnTE8ILcuvzSccXmdrlPkjW6SUUfP7T-BsHFXQeGbamxkteQkQ1FyWckaCkC7gdV9tf4PqC9dL3TKNyIUatTbJH49YQ59QalVv66cDWF8ZpLFJ8RjIh-ikcl90bkqMuP-lFDipYAODuA1Bh-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایات رژیم صهیونسیتی ادامه دارد
🔹
حمله به یک خودرو در غزه منجر به شهادت و زخمی شدند چند تن گردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/673416" target="_blank">📅 14:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673415">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixxFuUynPgtYjgIuhZFbVsnWeGEexQ0zFKbz-PfXgDiIn92MSY7YD8BevlgtBwvr8tAMSSUsfRmt9uKRn-671wIPKQMxIfFFyoKDBG6CKs1T1VPZ6ku62Oujmlw4cR_DFGKvXNrjFbrqFzlbUK6Jzmt0Y6pNd4BjTJOrjUnkAzyn0bhDTWNC65lQKlU_zlK765D0El0ikZi-cdmD2Hj5jFEFxNPvzaByKDjb64_pZZE9sCdSYHJDBgxiwzSPhvCKEHGqHHcip21TJVD5dpDAHSjkrETXhH7CH_LnlcT-xJkj0MaKENbsU8TdQ_eYp8d3588JTwLLmAf1Leq0BZ7KSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند
🔹
آمریکایی‌ها روی هوش ما اندازهٔ آی‌کیوی مختصر خودشان حساب کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/673415" target="_blank">📅 14:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673414">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEGbqkQX6IkaSZkUaN_D_RRhoVpkBqWJ1tmhtJlYbmHRwZ7MSsBEFY5YufuvF4Wmc6ceGTpf-t-bePyepemZgl-N-scxTyPFcJ6MhgR2cjEBv5Qdlkw0Y2RfaqufwLlFZETiKpC_sRLnKI7W09sNB0EQ0YMdYfWlp12Qhbd5T6pO9U90QndcJ6BSOwEWMrL7ONm_Fzi7i7FYFkBaxAI2uKcfGyQlPHNOCQD6QMkY3T6ScoEfYmuWinv47PV6BmCCzSy2ObY35OBiGyScs1pIw6bYbI3DNXC4vmyusKGX32NPoxL7hTwhqazJMnJ9fF7AjPSINj1zeoEw41LQdqEHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خلیل الحیه رئیس دفتر سیاسی حماس شد
جنبش مقاومت اسلامی حماس:
🔹
پس از یحیی سنوار، خلیل الحیه به عنوان رئیس جدید دفتر سیاسی این جنبش انتخاب کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/673414" target="_blank">📅 14:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673413">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سازمان هوانوردی بحرین: ایران با پهپادها، تجهیزات ناوبری هوایی این کشور را هدف قرار داده است/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/673413" target="_blank">📅 14:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673412">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99db1856dc.mp4?token=j6KDxdk0xpsuIWMv262xHVS52Y4TsYaYKwP6bAchVbdH8eCpyjsnZ6_4TBL3wAynxBFv3NMr9gR8uR90FyovgpXfPd8--LNN_y5jK2DEnW08Va5lSYPW46WfBnwtTqd_nMP_uzGGwUYR1eHV8wCEg2X6KVdfpH-_iSXULdYyhIOnVkXn1I0K5aS6Yu84Em0sLQCtH0LC4ZQw3G4z02c39F5wisGwruBCoaGUWOnqIBwnYhP-hOr3YcMScTnQh5QV4j51aACi-ADOPmrpTPB7QnI8cjhVZcAl-pTGRdl1uuiLzrwbhtkxNxjdrz1hktk4XmtVS1S2jpBgyxnbrfrqlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99db1856dc.mp4?token=j6KDxdk0xpsuIWMv262xHVS52Y4TsYaYKwP6bAchVbdH8eCpyjsnZ6_4TBL3wAynxBFv3NMr9gR8uR90FyovgpXfPd8--LNN_y5jK2DEnW08Va5lSYPW46WfBnwtTqd_nMP_uzGGwUYR1eHV8wCEg2X6KVdfpH-_iSXULdYyhIOnVkXn1I0K5aS6Yu84Em0sLQCtH0LC4ZQw3G4z02c39F5wisGwruBCoaGUWOnqIBwnYhP-hOr3YcMScTnQh5QV4j51aACi-ADOPmrpTPB7QnI8cjhVZcAl-pTGRdl1uuiLzrwbhtkxNxjdrz1hktk4XmtVS1S2jpBgyxnbrfrqlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف پهپاد انتحاری حامل مواد منفجره در سواحل استانبول
🔹
بقایای یک پهپاد انتحاری در منطقه قره‌برون استانبول کشف و پس از خنثی‌سازی، برای بررسی فنی به آنکارا منتقل شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/673412" target="_blank">📅 14:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673411">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
آمریکا هویت دو کشته خود در اردن را اعلام کرد
🔹
ارتش تروریستی آمریکا اعلام کرد دو نظامی‌اش، «تایلر جیمز فیهان» ۲۵ ساله و «ایزابیلا گونزالس» ۱۹ ساله، در حمله ۱۷ ژوئیه ۲۰۲۶ به پایگاه «موفق سلطی» اردن کشته شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/673411" target="_blank">📅 14:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673410">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تکذیب حمله به خرم‌آباد؛ آتش‌سوزی بیمارستان نیایش حادثه بود
🔹
مدیریت بحران لرستان شایعه حمله دشمن به خرم‌آباد را تکذیب و اعلام کرد آتش‌سوزی در کارگاه بیمارستان «نیایش» یک حادثه عادی و بدون تلفات بوده است.
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/673410" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673409">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
بانک مرکزی: حمله سایبری به شبکه پرداخت کشور کذب است
🔹
بانک مرکزی با تکذیب شایعه حمله سایبری اعلام کرد لغو ناگهانی گواهینامه امنیتی شاپرک توسط تأمین‌کننده خارجی، خللی در خدمات ایجاد نکرده و پرداخت‌های اینترنتی طبق روال ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/673409" target="_blank">📅 14:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673408">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
پزشکیان: واقعاً معتقدم وحدت و هماهنگی‌ای که امروز میان قوای سه‌گانه وجود دارد، کم‌نظیر و شایسته قدردانی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/673408" target="_blank">📅 14:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673407">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
هواپیمای نتانیاهو حریم هوایی اراضی اشغالی را به مقصدی نامعلوم ترک کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/673407" target="_blank">📅 14:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673406">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfmGoM7FHDzmo5H0NyumL6xLomANLlp17V9GfSGZXAYEQjc-5ENtRbk2Pn7Ol_xSSxCmqkDBzYS1-lKC7JtfEFUt7_VjkkU0oh-p9px7d6wysSg42HeTc3bP9vSqN-Toy-Q9vlp9O8qG68PUsno5mWAmID9pRkY3oGgHdG6Y3m71N0D1gqQ0CWjBAw05Mg5wz495VADs4fE46imlWyhYbVfseJKhI5fTMCHvuIRUupXWtGxdE7ys5NcrkCvb1y8-XF-kshEGcEESA7ACHmaRg70tpEY_XUEvVsRh3a_cy0qEM4uIDs6mPA48NjLXz2sbRYV5BDxeWlsju-uFOx-mmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین مدل‌های آستین که استایل شما را متحول می‌کنند
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/673406" target="_blank">📅 14:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673405">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CapjIHIqsL8icdIPSZWu5n7Y6PF5LZBxcgMkJahe30AQFSYwERecuJ7Q0FKegBCIpD3Ex37ol44fGdwd0ssJktVLYwV08M8g9coMv8gRfg3M-2mWMaxlScI1fmbJK2Bp1Gb12U_fnDikjssa1q94TLprGN8iw5C0V071FXa0W9MfixwmhfG7plvMfNZXr0CMRgrQDfCWpJbM5zW1Q0ZxwJaPB59Ff4SvSoMo797gVE2Z6gdZ-pZ7niuVLMJ1q1zl8hFrxImfR-E3zag62pNdsZE2oil3zhHYImlAgxYNi3ryryYXtE0tpVuiGVsEjKlEXSzV8HcvJaoHoHP61YurSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نیرو: پایداری برق جنوب، ثمره حماسه «قرار همدلی» مردم بود/ همدلی؛ تنها رمز عبور از روزهای داغ تابستان
🔹
وزیر نیرو با تأکید بر اینکه پایداری کنونی شبکه برق در مناطق جنوبی کشور، بیش از آنکه مرهون عملیات فنی باشد، مدیون مشارکت فعال مردم در «پویش قرار همدلی» است، اعلام کرد: آنچه این بار توطئه دشمن را در ناامن‌سازی شریان‌های انرژی ناکام گذاشت، نه صرفاً بازسازی تأسیسات، که همراهی آگاهانه و همدلی مثال‌زدنی مردم شریف بود.
🔹
عباس علی آبادی امروز در بازگشت از سفر به استان هرمزگان، ضمن تشریح شرایط مناطق جنوبی کشور اظهار داشت: دشمن در یک حمله ناجوانمردانه سعی داشت با هدف قرار دادن زیرساخت‌های انرژی، آرامش خانواده‌های هموطنانمان را هدف بگیرد. اما آنچه محاسبات دشمن را برهم زد، قدرتِ شبکه برق نبود؛ قدرتِ "قرار همدلی" مردم بود که با درک شرایط خطیر، الگوی مصرف خود را با مدیریت شبکه برق تطبیق دادند و اجازه ندادند خللی در پایداری شبکه ایجاد شود.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/673405" target="_blank">📅 14:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673404">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تیزر قسمت هفتم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای مهدی زنجیرانی که در اثر سکته قلبی به بیمارستان مراجعه و به کما می رود؛ با رؤیت روح مادربزرگ و همراهی روح پسرخاله بر روی ابرها، شادی و خوش‌گذرانی یک روزه در برزخ را تجربه کرده و در نهایت با رانده شدن و بسته شدن دری در آسمان، در روز اربعین به جسم باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: مهدی زنجیرانی فراهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/673404" target="_blank">📅 14:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673398">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIljnqKpxaFLXDPfgiN9onRtPomKqnnFJG4lsK2RF_KUZR9CcmQikJknCMVQ_1DJqsbbFlWHD_ZDZMNq5VBinCQKn9372STFLF2Ui8Q_TsWPmSMzSi6QNhujV93NhVIlNSg9fvBzHYIi5PyFFw7phN1kxkjyF1RD1BwxHcWfi-osiURb2X1UPc5eUhRc8t68BoGUh5UV4zsGLkJW8ujZqWVLU9095Hl2hf3nKUqy0XcV-hiHBG5bLjfvXL0rBQ7LFV39dFaaUNJGnP-5U-5pcWMncSI5Ze93HDoZlfvl37jS0bZvmH0MZf4EBKiL_S6WQMmNlUcgzi3PcdDfgon_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVpd7eukvYizxOAirwlLXpxjAjRXAGUGDqUfrXhJld0pzwBX97XTdfQdl2WVi1ergwqi-TbRGl0RkUcSVx0kFkbg-xbKww_4Qs2xKkKzMw2fiF0oUXKO1Uo8MScFlIeLtjFYyKgtQZzLwZKw_Humx_fPpuXNgyYZnj0vqVX5CUSIwBQuYxCbX31agwerAHEFbsvIMaWTPaddhhAIKYS8XmXdFNoIgSDOlBQKMqBqkctrMtxcfaP9lg1aW5DVIo6ZuRS6flXj0LbuxTL2Fum9pJNX6I6ZBBWTLZy59bj1rAIejeAxppfEZc6_aSJYoyhTKOZAeq3JxDkUC2defGxtVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_PXRZA5mfj7HhT107E4jw2qCCK20joRSAMjrNMfStP6-UuQXhYKLsZQYnfiENwSGZsPWNzGwK_CbNbbcpu3gO3ztHuTQ6Me1whc3k0RoBdgnWa98pIAMAxC9wW2kqYJAx4mBcRc4cRWkwgx1kBH7WqyOvNWqSCB4JZPAt22qAHby4OiJoDHidjI2fExndy2xngXRRKSMhSIqGDt480MQmyx31quydz9QJDJ4eZm_PsEKOK9I7GhmVsCw0ZVrEFHrt5eQnS1T7OeP-Iz_7x9_dr_W5kqJNDkFtpiBnq7QIZtvrIN9duUHFwDP1VkddT6n_3fJJcDropAN8koEzOuMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyaS8RAJfOP2mSxisEbCH0MF01-ATtCTtFCZJ-vW5aLE6g19Hb5fWlKkuJo7iT7H9nkEvJ2u-p7euldWtzlCUWiC7JxKjnvAEEzMFbAvqhD-2R3Sy7bC8AzAn2QVQOOVP5H3h-lOadFZU1VA9E2txtJyqeVTD_WJWfx1V04XKlOv2dkWVN039gjYo8I9uaFIIOJJpXlUD0Ln4mEwBofywbna05E785YHSHkNwnNKzVTfEpzv-bN6sEAIhsRdJspo_GOz2A2Uc_lExVtsjTdnXjMj2hEjpPMIayBsnLOt48Wlt4Z7_mZy9w7eQLwt3kcK3fPysvJhEYlVr_D5jhSSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNDFfikypk5Udr7epDZjB5XE_77OvFt-BC5UBI52TwgOdGaNpRcRKZEtsaCUUz2IKLIqEu-MNqmx_AFEzLgRyxb7q772D6LsQSweNV4TAx-DFFyuCB1XzOAFCegLBHcjbQ5iSDJXwaCIAUGr8WGXds0NYH3KIpTlbMMOZXwxtLY0JuA8ltQhaUylvQa-zArA5BXMZJX804OlwXei7gy7_tbiVQzmDGOYvX7EyTFcd9JrReHsKRLJd1tKoNBgDBLpDgY_qJVImPiAKXqmZUq5qP6WDN9OefAxmIqbVeAefea2GekxcMw9Y94T9Ihwjmksn6FuXMmpML2wJs9wlQu0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKezLvOObKuNtuRZZLiOEjsbcasF8QfhIQqDx3pvwFAkqeRxuWXjA9JKKbcxwzBMBp-RlgLdcKEoQNIRGG447rUZZ1yVvvGHbsJsRQb-sqdnnotZ6BgW6oEoA3qGk65l1EqaODpZ0QlZ45aVFPLGjj9EtwrjFqReg5knybSgNrmxcr3z0j8D4vQNh24Ee8pm-udIKrHDI3Zc_FCtjKSgZYdtXB1Uu-o0-d-QXQbbrb-1aTUX5kJzKa7tny5Bti6S9YbgRT_2U49a4H2_7wd16yBYShVfCkNJ-6m2k5v3kl-OYb9Y28q84M6wqpFQuR54wzjgUTYXhBUmp6MIHrxP8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر جدید از خسارات ایران به دارایی‌های آمریکا در منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/673398" target="_blank">📅 14:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673396">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ae26d0c29.mp4?token=vfBahpkVlcrWLvzh1N_OqRzV7W0pYqlwLhOCeTZFU3UcKHVMhdeyOudcFZAyWruwL0pPuDN3Wnfjghwa9utziOO-IogmuV0roD51T0dymCBgP4B20wUDYIgGUj3XerKtlsMBcq_Gi0OIegzusEhrbsQ6A96go_OPk_r6uibLp41fRwmbsbPrTfActam3Pay63s5azXNPw7jtgRk0NV1qSDaCmM3eY-oA4WylZKJDaSz8Upd8xLISYOAHZXFGx_alLyKaMaXsiPb8BKGTU-5PXEzByv_pQyPBHeI-IaVY1dhldrS4SKOhTNNiKoY7wA5diQnPkB0kaCTIh6Ib7owwMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ae26d0c29.mp4?token=vfBahpkVlcrWLvzh1N_OqRzV7W0pYqlwLhOCeTZFU3UcKHVMhdeyOudcFZAyWruwL0pPuDN3Wnfjghwa9utziOO-IogmuV0roD51T0dymCBgP4B20wUDYIgGUj3XerKtlsMBcq_Gi0OIegzusEhrbsQ6A96go_OPk_r6uibLp41fRwmbsbPrTfActam3Pay63s5azXNPw7jtgRk0NV1qSDaCmM3eY-oA4WylZKJDaSz8Upd8xLISYOAHZXFGx_alLyKaMaXsiPb8BKGTU-5PXEzByv_pQyPBHeI-IaVY1dhldrS4SKOhTNNiKoY7wA5diQnPkB0kaCTIh6Ib7owwMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ویدئویی منتشر شده از که کوکوریا به این شکل با کاپ قهرمانی جام جهانی از استادیوم خارج می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/673396" target="_blank">📅 13:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673395">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a594ec6809.mp4?token=NUIP3l-eSzCbL4FKORvBV8GlWMT_iUDhFYhAo9a3nhHwAcYcyV3jrxMM81XGSpMxVmrHVH1Dehj3Vbz6YfagF8taTzISh2MGWQbUK0wAnNqJiP0OKIfdeGsqVYRQ2VY8D6sFUPj3wpCal2gbpMQqRLlFpyPeYYgvFYNYFbsA_Ic17C5j8ovDmFfYCUxIyCHyjSQcfyCxurTF-z9Isn5NL8in11Z8eT5QotG5P9Sk8n-NDqbWWGQsI7OIYChuSGOmSLSEHnjBw9bUYeF-wkbQYmMdIZ_AXMn-4p0HLElIaPtHzoXFuIC5OWv2aijHbdeh36OAY4zph1QUEjbLpN6pKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a594ec6809.mp4?token=NUIP3l-eSzCbL4FKORvBV8GlWMT_iUDhFYhAo9a3nhHwAcYcyV3jrxMM81XGSpMxVmrHVH1Dehj3Vbz6YfagF8taTzISh2MGWQbUK0wAnNqJiP0OKIfdeGsqVYRQ2VY8D6sFUPj3wpCal2gbpMQqRLlFpyPeYYgvFYNYFbsA_Ic17C5j8ovDmFfYCUxIyCHyjSQcfyCxurTF-z9Isn5NL8in11Z8eT5QotG5P9Sk8n-NDqbWWGQsI7OIYChuSGOmSLSEHnjBw9bUYeF-wkbQYmMdIZ_AXMn-4p0HLElIaPtHzoXFuIC5OWv2aijHbdeh36OAY4zph1QUEjbLpN6pKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: اجازه اضافه‌برداشت به بانک‌ها نمی‌دهیم و هرگونه اضافه‌برداشت منجر به عدم صلاحیت مدیران بانکی خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/673395" target="_blank">📅 13:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673393">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پزشکیان: از هیچ‌یک از بندهای ۱۴ ‌گانه عقب‌نشینی نکردیم
رئیس جمهور در جلسه شورای عالی قضایی:
🔹
امروز بیش از هر زمان دیگری به وحدت، همدلی، تصمیم‌گیری مبتنی بر خرد جمعی و همراهی همه ارکان کشور نیاز داریم و دولت نیز با بهره‌گیری از همه ظرفیت‌ها، اصلاح ساختارهای ناعادلانه و خدمت به مردم را با جدیت دنبال خواهد کرد.
🔹
از منظر اعتقادی،‌ پذیرفتنی نیست که در جامعه‌ای زندگی کنیم که مردم با مشکلات معیشتی، بیکاری، فقر و گرفتاری دست‌وپنجه نرم کنند.
🔹
در هیچ‌یک از بندهای ۱۴ ‌گانه آن تفاهم، از حقوق، اصول، منافع ملی، ارزش‌های انقلاب و اعتقادات خود عقب‌نشینی نکردیم.
🔹
نه‌تنها هیچ امتیازی برخلاف منافع کشور داده نشد، بلکه با بررسی دقیق مفاد توافق، بخش عمده‌ای از دستاوردها به سود جمهوری اسلامی ایران بوده است و عملاً بندی را نمی‌توان یافت که منفعتی یک‌جانبه برای طرف آمریکایی ایجاد کرده باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/673393" target="_blank">📅 13:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7e070012.mp4?token=MJzRZWdOomEOxKAVDQTP5ZmKmfmtUTN4Gw9OvzxAsvkQfYzwRWd-cZNFYBrPEzXKZuL1i6oYr9hyzKHH3w5PwHyRxzUNiVJAKiDL7s569hiCcpyPLqd6dkCI16ReHGXEQ77-UaxlHLEAuXdV0AiT6ynBWQ4wW5WM6RPE0g5v8mGZj_Nb6qpIYU7MoPOSn15V-n3FOzkVxcVp2Jy4AbX97O3oUxBW9dkalAIegbiGdMBJox4kjw_C6M-PPRvff1e0vE8fXCAZVvQFnMDt-l2Ve09s8q8a99MkDrJ6ryQQdF7DSl-mqfRjZ7msMvbOrkcYWfyVZjYxo1WOlgKAaIngXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7e070012.mp4?token=MJzRZWdOomEOxKAVDQTP5ZmKmfmtUTN4Gw9OvzxAsvkQfYzwRWd-cZNFYBrPEzXKZuL1i6oYr9hyzKHH3w5PwHyRxzUNiVJAKiDL7s569hiCcpyPLqd6dkCI16ReHGXEQ77-UaxlHLEAuXdV0AiT6ynBWQ4wW5WM6RPE0g5v8mGZj_Nb6qpIYU7MoPOSn15V-n3FOzkVxcVp2Jy4AbX97O3oUxBW9dkalAIegbiGdMBJox4kjw_C6M-PPRvff1e0vE8fXCAZVvQFnMDt-l2Ve09s8q8a99MkDrJ6ryQQdF7DSl-mqfRjZ7msMvbOrkcYWfyVZjYxo1WOlgKAaIngXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان یک جام پرهیجان؛ اسپانیا با شایستگی بر قله جهان ایستاد و آخرین پرده جام جهانی برای مسی هم ورق خورد
▪️
قسمت هفدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/673390" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
حملات به کویت تأثیرگذار بود؛ دولت به تعطیلی ادارات پناه آورد
الجزیره:
🔹
کویت به‌منظور مدیریت فشار بر شبکه توزیع برق و مقابله با چالش‌های ناشی از حملات اخیر به نیروگاه‌ها، در حال بررسی طرح کاهش حضور فیزیکی کارکنان در ادارات است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/673389" target="_blank">📅 13:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
همتی: بخشی از افزایش نقدینگی در ماه‌های اخیر ناشی از افزایش ذخایر ارزی کشور است و این به معنای نقدینگی با کیفیت است/ سیاستگذار، برنامه های متنوعی برای
افزایش
تاب‌آوری اقتصادی کشور دارد و کالاهای اساسی و نیازهای مردم تامین می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/673388" target="_blank">📅 13:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA1WslTfbQgbP6R3xUrkwOKP4iNRKpcGKxsM9JDHJOsHWSB_ezlVDPekRa1a9Ve_CSlx0eIQm6ZqOYSSwpGjqMjSa03n-21hLYdAfwQAqCXLNeYiNsiK0Jm7qnbO94wF5PjTJF9P3AJdYDHIZhA6vttwRF6SUlH9he6sXMA4oH6PuAWBFi7UJzrMYiqbo7nXwSKkve3bC7VhNjHA1U4QVvwJknR-TrbHkuKjTsI-wHnOQQ-xU8sQYD1adkaN_mTdOsa-J80DhTvwV22HcujP_D7rmCi1tQJbqS9zU0sTbzB8k_HzALZ9-IO65zdYRk4kt6C6Qr0Lq3py6E3p1o_FnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ به‌دنبال محدودیت برای هوش مصنوعی چینی؛ رقابت یا حمایت از غول‌های آمریکایی؟
🔹
دولت ترامپ در حال بررسی اقداماتی است که می‌تواند دسترسی و استفاده از مدل‌های پیشرفته هوش مصنوعی چینی در آمریکا را محدود یا عملاً متوقف کند. دلیل اصلی این تصمیم، نگرانی‌های امنیت ملی و امنیت سایبری عنوان شده است.
🔹
این تصمیم در حالی مطرح می‌شود که مدل‌های متن‌باز و مقرون‌به‌صرفه چینی، از جمله «کیمی»، با سرعت در حال افزایش سهم خود از بازار هستند. در مقابل، منتقدان معتقدند چنین سیاستی بیش از آنکه امنیت را تقویت کند، به نفع شرکت‌های آمریکایی مانند OpenAI و Anthropic خواهد بود و رقابت در بازار هوش مصنوعی را کاهش می‌دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/673387" target="_blank">📅 13:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9f31b607.mp4?token=A_S4yFHi37OMPqRnAbwibEg6jeERx32aAh3dtaxkBv16cqA6n_JX1VKYBdmvE0ZeoXjf7lVoZoOybWxzYbUgzvawEISaWl4D4hDnTaCCnBGhn72JTs53J9gwTDtCE8Zz9nbWnASJh1pjxDVJ1tt2MPPVS4YKj-_ITuQY_bKeSINAo1YiHZWaoQe4pInpXpvhrcdvjYcL4wAATB7hQyg4EOewrF4Bs7__QxBbTTpARGkpXUGuOMQ9uXY2o6IEXFpsrXAmTLCEjjaYloXw9uCNe35lvENiBJZoH_CkfrKNGqmk5nfVUsNVXNtiC20R1lYtVyGCo_I6njEb8ARftt9u-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9f31b607.mp4?token=A_S4yFHi37OMPqRnAbwibEg6jeERx32aAh3dtaxkBv16cqA6n_JX1VKYBdmvE0ZeoXjf7lVoZoOybWxzYbUgzvawEISaWl4D4hDnTaCCnBGhn72JTs53J9gwTDtCE8Zz9nbWnASJh1pjxDVJ1tt2MPPVS4YKj-_ITuQY_bKeSINAo1YiHZWaoQe4pInpXpvhrcdvjYcL4wAATB7hQyg4EOewrF4Bs7__QxBbTTpARGkpXUGuOMQ9uXY2o6IEXFpsrXAmTLCEjjaYloXw9uCNe35lvENiBJZoH_CkfrKNGqmk5nfVUsNVXNtiC20R1lYtVyGCo_I6njEb8ARftt9u-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از پایگاه موفق السلطی اردن که اصابت دست کم ۴ موشک دیگر به این پایگاه را تایید می کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/673386" target="_blank">📅 13:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673384">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0116054239.mp4?token=Fr97iH7Cs9aBIW5704T6laCk5BAzeH7eUziBC5nEL93W9tw2lYABy9o2izsi-Bq_7iVWI1OBt93MNZuVFh8htWrCCNCx264uxovSohHSBbS_3oqHcy5QKejfSogk0b8k2439Vv9qjOOdEJSKBhrDfEFH_XEpyuibFgCq9gvhAVxjKFemfF8avjtr8TURDj-hB4kqG3zQzJVGK-GXcg8x-A9krV3C9uMyjtilk8h9uERLLaPm5OXV45Rit3ufv6k-pudBER3vjUrulehWCn1KNQurA1ilGMNen5FzDYfDj2olS7AjQRpFAZ2SuxsFMXyxvPV9HQht_Dt_UDT3AE7ToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0116054239.mp4?token=Fr97iH7Cs9aBIW5704T6laCk5BAzeH7eUziBC5nEL93W9tw2lYABy9o2izsi-Bq_7iVWI1OBt93MNZuVFh8htWrCCNCx264uxovSohHSBbS_3oqHcy5QKejfSogk0b8k2439Vv9qjOOdEJSKBhrDfEFH_XEpyuibFgCq9gvhAVxjKFemfF8avjtr8TURDj-hB4kqG3zQzJVGK-GXcg8x-A9krV3C9uMyjtilk8h9uERLLaPm5OXV45Rit3ufv6k-pudBER3vjUrulehWCn1KNQurA1ilGMNen5FzDYfDj2olS7AjQRpFAZ2SuxsFMXyxvPV9HQht_Dt_UDT3AE7ToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: ادامه فعالیت بانک ها ناسالم و ناتراز را تحمل نمی کنیم/ مهم‌ترین ماموریتی که برای همکارانم در بانک مرکزی تعریف کردم، کنترل ناترازی بانک‌هاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/673384" target="_blank">📅 13:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fca1b40d.mp4?token=D-KBgpa4UYavMyanekwXzBFt3NrV___5K7VmdOaPmHFK-qzbRNDK09sZDjq1rkQXuNEwyTioPDBrS2Lwh6rrvVUkp1mtwWnX67_t6T3ubBBVpcGir7qFU70CSqS4F2RCRHLJIO_fGxn3psAs6-92kSJNrUKIwgljtXo8_FDOINhmBk44C6j66TZEWawxG_j3yEZZThJRG607i5c_CpbiyPNfTvhVgdaZ6pNsgc1oQnNFkwEnjJdhQPwyCzz3SwSF7yHLPdoxTI21fuYxqUuwYidgDQDViaSkxu2vsSbiY2JGLz4CVCHTksr_SADYHz1Y8N7Tfz8A_wOvkI6AjtkaZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fca1b40d.mp4?token=D-KBgpa4UYavMyanekwXzBFt3NrV___5K7VmdOaPmHFK-qzbRNDK09sZDjq1rkQXuNEwyTioPDBrS2Lwh6rrvVUkp1mtwWnX67_t6T3ubBBVpcGir7qFU70CSqS4F2RCRHLJIO_fGxn3psAs6-92kSJNrUKIwgljtXo8_FDOINhmBk44C6j66TZEWawxG_j3yEZZThJRG607i5c_CpbiyPNfTvhVgdaZ6pNsgc1oQnNFkwEnjJdhQPwyCzz3SwSF7yHLPdoxTI21fuYxqUuwYidgDQDViaSkxu2vsSbiY2JGLz4CVCHTksr_SADYHz1Y8N7Tfz8A_wOvkI6AjtkaZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: امیدوار هستیم که در پنج هفته آینده خاموشی‌ها تمام شود
🔹
برق صرفه‌جویی شده توسط مردم را به مناطق جنوبی اختصاص می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/673382" target="_blank">📅 13:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ قیمت خودرو فریز شده و به اندازه دلار رشد نکرده
بابک صدرایی، فعال بازار خودرو، در
#گفتگو
با خبرفوری:
🔹
قیمت خودرو در بازار آزاد فعلاً فریز شده و هنوز به اندازه افزایش نرخ دلار رشدنکرده است. اگر بازار سامان پیدا نکند و عرضه منظم نشود، احتمال رها شدن فنر قیمت‌ها و وقوع جهش قیمتی در ماه‌های آینده وجود دارد.
🔹
دخالت دولت در قیمت‌گذاری، خودروساز را با زیان روبه‌رو کرده و انگیزه عرضه را کاهش داده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/673381" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673379">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10488c82b9.mp4?token=pC5VYqBbFNNcin3nfbIu4rNiOTRFFhcpBi4INqMLpsfw24geQwUlHGinotlYMckbKWJvoVTOhiSC9DONQyABITmteOG-arZPSB0Gkyh9zkv7LMhmRgZBKdX7Y01i1XIigopphYYD2rUl-4U6KnL55T8ZURGVbTwIsZDlrm9WHA1lbt1S9Xuynh7jNXf842mmQPelDsRwozI8WTwNGICxTuF3SuTo1i1IyAB5Nbh5lHZ0vC6vSPjrXdQAi9kmYIg0Yd23Hv94DhGqtZICmluVIk05DtBgFdHI4T52E4JjpA5Nj_Q3dqqBaObb9RuQCqY2B3b8Vb2mHCDKpOxS-e4aAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10488c82b9.mp4?token=pC5VYqBbFNNcin3nfbIu4rNiOTRFFhcpBi4INqMLpsfw24geQwUlHGinotlYMckbKWJvoVTOhiSC9DONQyABITmteOG-arZPSB0Gkyh9zkv7LMhmRgZBKdX7Y01i1XIigopphYYD2rUl-4U6KnL55T8ZURGVbTwIsZDlrm9WHA1lbt1S9Xuynh7jNXf842mmQPelDsRwozI8WTwNGICxTuF3SuTo1i1IyAB5Nbh5lHZ0vC6vSPjrXdQAi9kmYIg0Yd23Hv94DhGqtZICmluVIk05DtBgFdHI4T52E4JjpA5Nj_Q3dqqBaObb9RuQCqY2B3b8Vb2mHCDKpOxS-e4aAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بانک مرکزی منشأ تحریم، جنگ یا کاهش درآمدهای خارجی نیست اما این بانک مسئولیت دارد از تبدیل این شوک‌ها به بی‌ثباتی پایدار جلوگیری کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/673379" target="_blank">📅 13:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
امنیت سایبری در صدر افتخارات ایران؛ تداوم مدال‌آوری تیم ملی مهارت در رقابت‌های جهانی
🔹
معاون برنامه‌ریزی راهبردی و صلاحیت حرفه‌ای سازمان آموزش فنی و حرفه‌ای کشور با اشاره به عملکرد تیم ملی مهارت ایران در سه دوره اخیر مسابقات جهانی (WorldSkills) گفت: نمایندگان کشور در رشته‌هایی مانند امنیت سایبری، جواهرسازی، مدیریت سیستم‌های تحت شبکه، پردازش ابری و تبرید و تهویه موفق به کسب مدال و مدالیون برتری شده‌اند.
🔹
به گفته فاطمه منصوری، در مسابقات جهانی ۲۰۲۴ فرانسه تیم ایران مدال نقره امنیت سایبری را کسب کرد و در رشته‌های جواهرسازی، پردازش ابری و تبرید و تهویه نیز مدالیون برتری به دست آورد. همچنین ایران در رقابت‌های ۲۰۲۲ صاحب مدال طلای جواهرسازی و برنز امنیت سایبری شد.
🔹
وی تأکید کرد نتایج سه دوره اخیر نشان می‌دهد سرمایه‌گذاری در آموزش‌های مهارتی، به‌ویژه در حوزه فناوری‌های نوین، می‌تواند جایگاه ایران را در مسابقات جهانی مهارت بیش از پیش ارتقا دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/673378" target="_blank">📅 13:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjdkOYvTBaJs8Ms_vwqy6pHSm5t8Mj0cbBC6XqF7TjpnlJ7B_6a3xHp1HxwsxItUujS_oUbKJl-2B254s-8wwWo1VrWvn5b2VX8lA6hbEOvY2wFCl20ELRQKLSPvP-Q4325d5VFgCz06HvNjmLDY7EWfuvgNKl3TUnCT7wFOrPwaVumxl5ltvzZEZ6gsR59IcFfqtyKeJqDI160q7QmbglxILw2gjofrZk4ArM10dGGha25wfbZhw8503m8ACLM-Qn8Dk8zFUJ0KSAgpSVLfxevRBTZqIPc0LiZwB6spRfgHJ8kW-6w2EfglBRlYcKtm6QGeV8Z1aTgj_nnx-qIoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMbyeZWPeF0c0OVWVvCZm05Om-QKSZ5UgA1zkfk618YNge2qinsLcRL1zqZwg0K04mmfa4NIlCAIEiZMy2gX61ceX8PxHGUvjgvB1r76F-oOQi9Yf30eS33JCbgiGckvbMqIR9iIAf1S8wPMq5q6Xan5j-yocDa3mq4ekE_H3wJx4smUmT-l4jfyuWTXMc7JkjhBg_EZUPGX_QoYNykmq2Pl2MZgMs9TiSaaXcv2t-1yBDEhCMT4zsNNGB7MUKLzLxYuwxnv8nmuB15_BKG6iPkcKhKHvZI_tQpTn07IfN-LrYeVtNMnnfP5vWzI_lOND5NIcECi363reor2xutU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbc-s3eycjOv1XBf7uNCB7Q17Qlyhn7StCCmgW-QKnd9Pj54DAJWqAFLLeWODIvYmHBhLiyj11lHqH_0VyVK8kgmQqtIOSzbnBcTlTDwT0EupELfYcaBY5aFtmvSWB7Gge1xp_NP7nVdRPE6eov3eI0lZOdckrcT8A0ZZ-8Zkwb3xiBuHrz5hwp1Dy01otYXC8LWouC7xtuhl_3eUX1y9Ge7yuziwdw31DRU9fEa-FdFfGLdulu3AXW4z0DZH5QENGbNt4QILh_kD_SHxsfPZjho2HGNCSy5nZelabvp6-m5wl9FRtauzOzdA_EwLNTXs3XlFtApPzL2VcV6SllxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVrIM7ODJEFsAwuLKv0-VJzZ-PDsv_Rjws4YNFg6OenWE_ZwPOSUNpehQKZAf4eiZzhvvOwriUeYRQPHJGXdwWNlQ25lR2Wg1Bzz5PpGl8S4UtfM2_5Tkg1vJzKdLFIXjdcilvnPX4aztDUYAeC-pzkx2KtmZHBapc7Nh_yHKKri-lEJjqhgzXCirWPXUfN52QouyZQ2Sq_KLi_cxpP_fU97iYpk827hjvImt4YcUTCTWxNwy9hqgOe-K9hEYjcAf8RMsKezOMw8TErdEJ5fjn0jGWYABR-41iDMCOZ32SlwgaygK69p2npVMGBWRS7OWLex-nkC6hAIVc7ry-4cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AlSFxDfKmy-2WpMrPuSGhrhb-6xJ6fKhyEkzvS8jwQAS5D2IVQPMhrxdzYPa4LEANsMPfLRzZ6xYii0Pb0fPTjX4PBpEeBmoSn5wbwwXBEDbjJYIoyvYW5u8EZy2mtZaM5n0wQ0S_0Iy8aShSxNhKGyVqQcc3eJnfVrV-Qor8K76nORRTwo7bfBro3ndsScbGdjwQjiD2T9dq_1D5ySoeDGrGl3htDEbsWYKvFlHge5g1x6pxY-VRKfJVbY8Gi3ooZl2cfe3TA_jq98X2RGKCAZFPx1dvNFtPawR61Ra5LslMz3A4j5GmQpGATWclbMynT2iTZpOd4slcdNTaYf9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-G7v9pgB4jMwfm6JJ_ULzrRQlvlaE2Ss9Hn_er1D1oh_jPQZEiASdsGvqRHJHI4VIGmqCSfOoAVZxohGhhkOr8VaFwmdKpczG1c28yIygpl7QGy8sbwKM_naGj9po5TGlo7s9iGlAk2NUFz70RGbNJfFfqe_X61wonWF7x6RaHJ5V7YzHi4yfyEJ1ggMw_p0Pe7P3rinqY5-wspR53DJYLOOCCqDGFKvVlg4xmladMQ-4Iy8kJwjX3MIdMudLoT7qoq5iyIYlNJv-76HAJCrhFTXB4-SSgRJHBxulHwoWszZxj6d5ndGLAUW-tO30qYE-S-YBSiB1OOXMpKEq7WuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyAxm13IGIKlueuoy3pC9BuJSeb0rxgv2XFmGQAXa86nxd7KWyXYzqRO3pDGYY8zB5jdmHaWJJM7_AZjS1g5FdzmdG65qo_hFB4Rrkw1ImvMhUgyoq4zYsV03H1Zfu6fI41ijy1wFMlIR1izX6X1fEESUPXbE_ivA7D0_rNM4orHHKIYiZB9bYWWmS_lK7qfjiZ5108Zh8VpbYPXtqqDUKrpHEPN8133D_eBfdArmVMrMiTlOKVblrDi6W1SZQ2o8_DimoN7OsFd2CrW0c_5J-FawyYFn2ghifjrrH0Lzeg25CzCTMDlPH3Rm76HZQE78X-oZuPRThjQQ4A5gVKx7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با
این ترفندهای ساده، مواد غذایی را چند برابر تازه‌تر نگه دارید
💫
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/673371" target="_blank">📅 13:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">◼️
حمایت از کارفرمایان در شرایط بحران با مشاوره اتاق تهران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه بیمه بیکاری، به کارفرمایان کمک می‌کند از ظرفیت‌های قانونی ویژه شرایط جنگی، از جمله ثبت گروهی درخواست‌ها و بهره‌مندی از مقرری بیمه بیکاری استفاده کنند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/673370" target="_blank">📅 13:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ea2a3fd4.mp4?token=XOy_4fT4Fah2G6HtFG1at-A7ZQkLIvqXUB1fPgEvInSrzIuyPierhuCKO09Ud-HmOb0P6Y22Ck7vn7Ra3vNP8RzoaJ8qOsG23IPa3gCP9Oj29r78PK1x5YeUfnAaxJlzJ9g4NHre53oJWnCelrb96FzJb0SO4LygwznSV73MftEIwRy7U2Tnxej5kXztUoKgevhtHCaC9keO9koSwAAuUV7uVRgw_OU3JfP3iUQDLZ0NOp35RHdKp6fTitZMquZ-VLxBhf6IjXHtkXSo9BTXeGjSS9BBBbasvX9wXjmIXw5RITo1fVts4z0I1uanFJGxjHaZ5jwBYYfxcdosTRe-cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ea2a3fd4.mp4?token=XOy_4fT4Fah2G6HtFG1at-A7ZQkLIvqXUB1fPgEvInSrzIuyPierhuCKO09Ud-HmOb0P6Y22Ck7vn7Ra3vNP8RzoaJ8qOsG23IPa3gCP9Oj29r78PK1x5YeUfnAaxJlzJ9g4NHre53oJWnCelrb96FzJb0SO4LygwznSV73MftEIwRy7U2Tnxej5kXztUoKgevhtHCaC9keO9koSwAAuUV7uVRgw_OU3JfP3iUQDLZ0NOp35RHdKp6fTitZMquZ-VLxBhf6IjXHtkXSo9BTXeGjSS9BBBbasvX9wXjmIXw5RITo1fVts4z0I1uanFJGxjHaZ5jwBYYfxcdosTRe-cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این‌ها غریبه نیستند؛ هر کدام از این چشم‌ها، روایت یک هموطن است #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/673368" target="_blank">📅 12:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54f111886a.mp4?token=vvGYAAw7n_6a_jyAAewMrx70fr_gkDaZE1eqC91ma9qP4MxYhEgR92p7wI7MDAjX8sDIgYEn6HtTbL07WBVUFXCSDxcQ2_kvhQmlYmCsChAWsNVd0LHTVKXvEc0gFZ1AuqzS8t857_q8Cp8w_XY-SFWKyXN102nbu5TRj2ZzeDbvxttfiiudmbXU-3KMyvlMgcKfwWM7i8wfyD1uPbL_Mrrbd0wWo3L3PT6nSyfEX3JUV8FyoZoMZ11DXZ1VlnVeOm2kWKS_cx0FU7FVrlaEWHPzwE3MKqjMrf_kelCh762Y0mwJ7qM8YMnB7aM0I5UX4BGTjsRgHNoca5e4oxY0cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54f111886a.mp4?token=vvGYAAw7n_6a_jyAAewMrx70fr_gkDaZE1eqC91ma9qP4MxYhEgR92p7wI7MDAjX8sDIgYEn6HtTbL07WBVUFXCSDxcQ2_kvhQmlYmCsChAWsNVd0LHTVKXvEc0gFZ1AuqzS8t857_q8Cp8w_XY-SFWKyXN102nbu5TRj2ZzeDbvxttfiiudmbXU-3KMyvlMgcKfwWM7i8wfyD1uPbL_Mrrbd0wWo3L3PT6nSyfEX3JUV8FyoZoMZ11DXZ1VlnVeOm2kWKS_cx0FU7FVrlaEWHPzwE3MKqjMrf_kelCh762Y0mwJ7qM8YMnB7aM0I5UX4BGTjsRgHNoca5e4oxY0cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمبرداری با گوشی رباتیک آنر
توسط
بازیکن اسپانیا
🔹
پس از پایان بازی فینال، «اریک گارسیا»، مدافع میانی تیم ملی اسپانیا، با گوشی بسیار متفاوتی روی چمن ورزشگاه نیوجرسی نیویورک ظاهر شد. تصاویری که در شبکه‌های اجتماعی دست‌به‌دست شدند، گارسیا را نشان می‌دهند که مشغول فیلم‌برداری از این لحظات تاریخی با گوشی Robot Phone آنر است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/673366" target="_blank">📅 12:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای روبیو، وزیر خارجه آمریکا: من واقعاً فکر می‌کنم که جهان به نقطه‌ای رسیده است که روشن شده ایران، می‌خواهد تنگه‌ها را کنترل کند و از آنها به عنوان اهرم فشاری علیه جهان استفاده کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/673365" target="_blank">📅 12:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673361">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff28efaf80.mp4?token=PEfCinesv3tSzMJV32UjKfEB04Jeza0zLizY5AkUIR6rpDkPk2S3BVobx1kauNaoltrQSaE--aSKz6vyHZDzwtAKYnEWCDldooToa_Ijub8D-ALKSxkm97diPS9gMGQltIhqDZJ2WN9rqW43AT0HCXHgEeo4-BgPXPFhSYW1MV0vRkLJim8ZeUsmktwpm2USk20PsSTJxeeGo5p937VAO8FNvp9CCYEPIyq-cEzbHWp1ya9NeKjQpRTPCapvJPPUoD5Z2Rjyyzsdnrx1ArW4kEwdPMGEVnCVM4e5bpWuq8TGr2yUUQD1cPDv4s5E17JTEtQmo7ZQf_RB4QR_3V-2hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff28efaf80.mp4?token=PEfCinesv3tSzMJV32UjKfEB04Jeza0zLizY5AkUIR6rpDkPk2S3BVobx1kauNaoltrQSaE--aSKz6vyHZDzwtAKYnEWCDldooToa_Ijub8D-ALKSxkm97diPS9gMGQltIhqDZJ2WN9rqW43AT0HCXHgEeo4-BgPXPFhSYW1MV0vRkLJim8ZeUsmktwpm2USk20PsSTJxeeGo5p937VAO8FNvp9CCYEPIyq-cEzbHWp1ya9NeKjQpRTPCapvJPPUoD5Z2Rjyyzsdnrx1ArW4kEwdPMGEVnCVM4e5bpWuq8TGr2yUUQD1cPDv4s5E17JTEtQmo7ZQf_RB4QR_3V-2hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی رئیس جمهور متوهم آمریکا خواست سهمی از جشن قهرمانی داشته باشه؛ پایانش دیدنی شد!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673361" target="_blank">📅 12:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a34c44b8.mp4?token=epGHtq6LTSECep1Kz0cx3nwmgkPSfpKwElz54jEa9ZsV5GQD3Hua8w3BSti0cp1xmUekVIsioh7_c8byYDpKcXVz_4OoskUag57fR8UREJPxWpYmU326knyWvO8yq7Hk0RZs1-7tZZW90uHm-YMod5xW_Z-TpLSMWyw_s85ysWaFfse4ehRiqWZwShZy6foqO7FrdIMipNBHYzU7lia2H4YVCrGoAnlADI49D1AC0RzmBYorUowyDUEJ24iK20eUxSsCs2y94Hzx-uw6Jydp76yfFFQH2UEq_Pp1OdERJwBXCBhLuSXVz7QurCC9IK4Mc5IOO88cRMwMzFqU-_oQXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a34c44b8.mp4?token=epGHtq6LTSECep1Kz0cx3nwmgkPSfpKwElz54jEa9ZsV5GQD3Hua8w3BSti0cp1xmUekVIsioh7_c8byYDpKcXVz_4OoskUag57fR8UREJPxWpYmU326knyWvO8yq7Hk0RZs1-7tZZW90uHm-YMod5xW_Z-TpLSMWyw_s85ysWaFfse4ehRiqWZwShZy6foqO7FrdIMipNBHYzU7lia2H4YVCrGoAnlADI49D1AC0RzmBYorUowyDUEJ24iK20eUxSsCs2y94Hzx-uw6Jydp76yfFFQH2UEq_Pp1OdERJwBXCBhLuSXVz7QurCC9IK4Mc5IOO88cRMwMzFqU-_oQXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت شهر والنسیا پس از قهرمانی اسپانیا در جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/673359" target="_blank">📅 12:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMGesclDb2q4Wqv-AP0HsGsd4z1c9stXvG81FpasHaXdO8x7HBn5w9xeAi-ZBOVJ7ZoUee9fzAkyl9Nl1eG6V_ZeNWiHw4IArQWHDXDWvM_ggXn7w3kCAiARQGUv27xz6xklom_-C0PPw8-sbJkOBcbbAC1FJPMNdsqnGJBz79Vs4SFww1W2z4UYAU1y-2OECO4-sbOYZ9I3HqHNSLwJY6gY7_ixMkQ9v8SjhKWVfFoujTs0w5LKr52-EVEEO8QYPCtukpoKPCJw3HgY6gkelOhWuMpd1GM34jGhQKPrIkcUSUWfVuZJlnCKoPlySajgTP6drB_5d53kzBVJWxc6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۹ تیر ۱۴۰۵؛ ساعت ۱۲:۲۰
🔹
در معاملات امروز بازار ارز، طلا و سکه یکپارچه نزولی شد و این عقب‌نشینی تحت تأثیر سقوط اونس جهانی و فروکش کردن هیجانات سیاسی منطقه رقم خورد.
🔹
با حاکم شدن فضای احتیاط، فعالان بازار احتمال تداوم این روند کاهشی را در روزهای آتی بالا می‌دانند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/673358" target="_blank">📅 12:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673357">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/673357" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673356">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/093f5b50a1.mp4?token=LDBmltH58pdEuVlk-eBm80bjhTAWPPgi9SSuuY-pQqqbhpZVIYw4Vt1qZw0VQ5tRezNGkSuq9Rzpa8JMLvZvwU0x6R4TmYAskGjxk-hGFbQfcY4G-GzS4VHrFS8xOJ5QHd_nICLZ9jcwzXj943MFyCvIVYdAvb9lRUG5pQqN-Mw05tWWhhgTfNsvNtwsH8UaGEnnH7qTcmUXjauP7-9L2NdlHsrjFqMsvKhMJ41OlApEok4LEgG6BacoCq9BKrKNiAcCQDooS8WzNy9z2s_IMCeVltXTbMlAHVk3YtPSOvoYeihjkJlknw2P_0Mv7Qz334iewogiSdIHP0_5a_mc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/093f5b50a1.mp4?token=LDBmltH58pdEuVlk-eBm80bjhTAWPPgi9SSuuY-pQqqbhpZVIYw4Vt1qZw0VQ5tRezNGkSuq9Rzpa8JMLvZvwU0x6R4TmYAskGjxk-hGFbQfcY4G-GzS4VHrFS8xOJ5QHd_nICLZ9jcwzXj943MFyCvIVYdAvb9lRUG5pQqN-Mw05tWWhhgTfNsvNtwsH8UaGEnnH7qTcmUXjauP7-9L2NdlHsrjFqMsvKhMJ41OlApEok4LEgG6BacoCq9BKrKNiAcCQDooS8WzNy9z2s_IMCeVltXTbMlAHVk3YtPSOvoYeihjkJlknw2P_0Mv7Qz334iewogiSdIHP0_5a_mc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا وقتی والدینمون صحبت می‌کنن، احساس کلافگی و پرخاشگری پیدا می‌کنیم؟
🧐
#سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673356" target="_blank">📅 12:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMGIx7fnT6ihHkCb9MtFkkTFqCil6llYNPMYE-cUO7-ZHHwsf_g6wUQQsbrisyORqG24Es5p6v1xa2pBt5rnHQKZ-JZFSi2Zkew_OLWnmqNx0HUzYfYjRMgL2G-0M89axGQGDuDP9BGMYmJf55n6DjaqIY1qhVMjEfMP36LcNc41sA8Tv-zKbxkrmC5QiUqMP5AA1O3pUgqUhvJWpxeQZOQ2Z76mIK4UUlHKwk5IdzKLhOqwmegpK7NolpxkbZKYbNCtUViJoWTLDZhx1hQHn95UxBqiyqwI5uJPose22HQmb7gh65h-SLOuQaRROo6uYmreWWZkiHEGOrAu3PGLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErJwepdFPmScE2ylBy0fINZzGwhq-3V9y6vlcyaGkOiWYzANqQNBuz3cJSCHjqaZQqfadtrvZZDWnUFJsDVfyId_uPt_D_TgEbu75D-SgkmaQhWk88M39gyYj3SbAFA3Z3J1fAEEO88s1GqHpMRzUgqQ6A-rrtZ5N1AmMxx7V-eFxzcdwZMaoxk4Unfve6vuvD_N1UmHtz4fiozL1BPi7us1ZtVQztTlQWAc9zZ3PrdWep6AeH0Cwo0FrpbKITKfrqvRqVyM-qGbx0tpwZPLHclHCUfrgaBdKcbEHK6DkiPpd0SHJGJLkmGtNtjcw-l-Bx3dPKdiuCDJwCNTbd16aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9UNOdgyfo2ZcRFZ1fTzzF4W-narTYBoeWaYLFM-2E0CIACYg2-4KeS2wt4WHPpG8N9LeycVcBG9u4DvbjgIlryrDufUpkqkMzOgE3sp44fdyWEoI3v8iPpbDxWi25xBDzeRRsmmT1W5IX9Kcho81RFgQswrUEYh_gHQBFQ8acpJ5Ut1ZIBEnL4pn50g8_3SFx4RD1otIQyFruDwAGorS9ZSRr2u8xCCULH_yLFmDsmjNEqmqG3VdCv1uXDyQ7fNE2HcvEkposzCjEP_6kPRe5AxBBwff17idm2BIZBgTtpmq1LZI9qc0AFAHu5wdvB5TUcd9ZeK0EUkuaSahkddEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمید رسایی با انتشار پست و تصاویری تحت عنوان مغزهای کوچک غرب زده به روسای جمهور سابق ایران حمله کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/673353" target="_blank">📅 12:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673350">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2eec77dfd.mp4?token=bd2liA5uMNtucwMeoEofcTlLUEnKBnOwUpV8zoRESPlfrN3TvBbkEihY7oQFUISfhNtkp7rSzAiNaSjXV3V0s1eIqqQDcBN6x9WuH3ugGtDibhBbONsl6zI8fdIAavJUAdm8fK4l6C76r7nnMdg9ulMabVAkhUm-_LMX1t8qLE7YFnMN8aH-IKJMsP47VT1IhlTz3sm-p7tLaibW3wMV1YW5gbg7vgwmioyIA9qseY2B_JV1EvvV8YAgPU1KYDIJDJAf-_h2gT7n-Uo_clDWT727fM0Jexk-MiHrbhvqlXavKyyfvt9kj_2Wt3OyngAxoDWF8uESZADGJmK_5bMZ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2eec77dfd.mp4?token=bd2liA5uMNtucwMeoEofcTlLUEnKBnOwUpV8zoRESPlfrN3TvBbkEihY7oQFUISfhNtkp7rSzAiNaSjXV3V0s1eIqqQDcBN6x9WuH3ugGtDibhBbONsl6zI8fdIAavJUAdm8fK4l6C76r7nnMdg9ulMabVAkhUm-_LMX1t8qLE7YFnMN8aH-IKJMsP47VT1IhlTz3sm-p7tLaibW3wMV1YW5gbg7vgwmioyIA9qseY2B_JV1EvvV8YAgPU1KYDIJDJAf-_h2gT7n-Uo_clDWT727fM0Jexk-MiHrbhvqlXavKyyfvt9kj_2Wt3OyngAxoDWF8uESZADGJmK_5bMZ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو جدید حمید سحری: رونالدو، هم اکنون
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/673350" target="_blank">📅 12:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673349">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM7UEm-pBmmFtHQM4v3VtlY4os9tPborgKdYLheKbaZh_JSPCHi62SXLY0ID21nJ2VcssSb7MKk84vNza46ONL78okX6kaKPozBh1bZVJewML-X3C2Wf8I33-0jxBOakGY1iz9hJAkBQVP64XHT8LDd5-6hSNle7xwEBAAGe7Sf-ZAEGP9F-eW7gUN69duLfPEAVIwwE-I9j2jIo6OHOAiDDANROf1UC2wKKWvZlIphkOw1LbR00e3ITl1oB1c5HIuF5Y5kkpbDGjjNKw4RyGrbjkXBvVlQ-LZ6VjVA24ImP6WmZ9BVGr-FFbcCB0cns5qqxSl1HrF6IfS7oCBJ2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهدای برق = اهدای خون / به یاری مردم جنوب می رویم!
🔹
جنوب، این روزها هم زخمِ جنگ را بر تن دارد و هم گرمای طاقت‌فرسای تابستان را....
☀️
🔹
امروز، همدلی فقط یک احساس نیست؛ یک اقدام است
🔹
هر کیلووات‌ساعت برقی که کمتر مصرف کنیم، سهم بیشتری از برق پایدار به مردم آسیب‌دیده جنوب می‌رسد.
🔹
امروز اهدای برق مثل اهدای خون باید اولویت تک تک ما ایرانیان باشد؛ برای جنوبی که مردمانش سمبل هستند؛ سمبل مرام و معرفت و انسانیت
🔹
بیایید با مدیریت مصرف برق، کنار مردمان نجیب جنوب بایستیم؛ همدلی امروز ما، روشنایی خانه‌های آنهاست.
#قرار_همدلی
#مدیریت_مصرف_برق
#همدلی_برای_جنوب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/673349" target="_blank">📅 12:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNvNi7_XIX5FSTFmWrhgHQFjJTQSYSkEESyPpyY8OCstmVGH7-WmmwrKe1Kun8D8c68RaLnMGZK9UwD5C6P5vTRrQE5GKAobBBmYwH1KxB6-7IxWChph1jTO1SZBVKh2muPYVLFsABCTJ4mVRp-lDAxCSyLpSSVfPm9E76Qg7vl4_S0eyZR7ql7ts-dZjv1uLwV-eaHpDgRhbVOdVzDEv8j9aW3XdKLHaSwVV-RCx1IGeNrMOALIsH1XZBNJUZPVEbWdecWWYgUgJkk9bfyzPxTG3oKvdWJ3HfkD_RbVtPK6c_v0x73aTyoAL6LR1kzEQ828INUCP5RyY51O16Zf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥀
در گوشه خرابه،کنار فرشته‌ها
با ناخنی شکسته،ز پا خار می‌کشد
دارد به یاد مجلس نامحرمان صبح
بر روی خاک،عکس علمدار می‌کشد
💔
شهادت حضرت
#رقیه
(س)تسلیت‌باد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/673347" target="_blank">📅 12:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEc-dEi1_cIsyC1SR4fjGj-_3x4VjQC57lngl9QAUCfO7PUYteLk_CTK2339SQp4ZjbAmuxPZeg1EX6XEqANT2AjWtAp5Z97L_W9v44mvxN8V90osQlhDz6lImQZIIKO3IX3ODETfxvSbQpEHczGuFx9PA9ucaTtQ6je1mQPy8Gvo9p03ckX38z-i4imo-NghkV3ATpFugHRhBhh9aAYmvXrLnTNafUy2bf5lNkHxxGjq9P2AOIN4vuqvKCEYJHAettj-1ziDH-TCFCgbJGIOupyZgNdWzNMn9UzTBrjmBWZBGPT0n8k_i1ZpVUNocn6puSYjISSO-AZifZr3V2dRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: شادمانی ملت و دولت دوست اسپانیا، شادمانی ملت و دولت ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/673346" target="_blank">📅 11:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlDXMv18ifSx2yEYAJEOlJD5WjzYPjOOpWuOa_SGxKmmTiHdzigew8p4npYYrWC75d2pcXO_CGvl_FJJFttKKHLhOt5nkAgYM-WbY3WWA0FXPpON_97ko1chwCu5yHQ2V2FhkxEg4wl058ynsottJ6MBxgaL_T2VCnnYd7caY7z-z8aJm9SPnnDseJI1Dx3JolWh6xZLSef5KOPCtN55BxfQ5QqEfFxfcYbPdcPXcMpyykV2DzHJ9bnVSgFv8lA_fgo2pn8R3K-nTP6MEwRG9m7wKdjgFzbPcqupy0KVJUZ1DrB2Hw4xNq3pzhVsjlycHBk0QtCz9l4LVj1BnWNFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از پایگاه موفق السلطی اردن که اصابت دست کم ۴ موشک دیگر به این پایگاه را تایید می کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/673345" target="_blank">📅 11:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hlh-lAFmdKBRWacnI5mh5rIh3PGpghGdZSHw6Z3qNwD0JMRSLXdkITBqQWRSawXSGufrx1g_dxltJFfDkSzvAiJ_zLpK8Q_rXX9IR0-CPgf9KqzpZ8loJwe-0SSR8Ys9dG5ckVlEmQrmB2vJKJf9kL6mWxI-DW8o-R6ZV8iKyLsaymLsF-9_L3PxS7jo0vUwJEyts4FfyOoj44arsVLvXN4VMnYW44LgyY_ZJJLoymD6dzx1TcevKEAI9kOb9EasWNOJvGbmaN_Ed3TFge3X9USlzR_CpsEkdk0c1S2IXvhCNuwuShhV_T7i-vP2GgnDHBl5wp4IWZawdMGm2j2xIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏡
زمین را قسطی بخرید
بهترین فرصت خرید زمین
جهت مشاهده مزایده بصورت هفتگی به سایت املاک و اراضی آستان قدس رضوی مراجعه نمایید.
🌐
آدرس سایت:
https://amlak.razavi.ir/panel/auctions/#auctions
📞
شماره تماس:
051-91008003
#زمین
#مزایده</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673344" target="_blank">📅 11:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673342">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تبریک قالیباف به روسای مجالس اسپانیا به‌مناسبت قهرمانی در جام جهانی فوتبال
🔹
پیام رئیس‌مجلس به روسای مجلس سنا و نمایندگان اسپانیا: قهرمانی تیم ملی اسپانیا در رقابت‌های جام جهانی فوتبال ۲۰۲۶ را به شما، مردم و دولت اسپانیا تبریک می گویم.
🔹
دفاع شما و بازیکنان آن تیم از ملت فلسطین و حمایت‌های آن کشور از ایران در جنگ تحمیلی سوم، نشان داد که آزادگی و سلطه‌ناپذیری از ویژگی‌های آن ملت فهیم و محترم است.
🔹
این پیروزی و قهرمانی ارزشمند، نه تنها دل مردم آن کشور که دل بسیاری از آزادگان و ملت‌های مستقل و عدالتخواه جهان را شاد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673342" target="_blank">📅 11:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673339">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e08b658f4.mp4?token=pA5N64-3x19C1P63-EuOuFlQMXJXCOXQcffXIifiNGPIboeHOXhHKe_bm2FG80sDN_1yAKhijBue5yb_Qk-_A8jBs0izWbi-Th0g8_2M07NoA1ziCM6aJ1cK4Wb2kUfx6cIrSQCDEeuB-6HzdAyFo8IlB2jc6CCF82amC4AwocvRz4X-SQxD5vQImN6qJqTFbbpqUkYFTAZJFzTPO71tVAgX2X6NQ6cbT3sqN6eXtvV7Vm8hvBl7oa7tFbgHBUs6jen-n7GpSfTi91PL8oFOPdyShlnlrdVjWZ0r7UZvI-jKY-t-bp8krn7am_IlNBVv9YGsGQ_d_2RDHdgiS3s2kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e08b658f4.mp4?token=pA5N64-3x19C1P63-EuOuFlQMXJXCOXQcffXIifiNGPIboeHOXhHKe_bm2FG80sDN_1yAKhijBue5yb_Qk-_A8jBs0izWbi-Th0g8_2M07NoA1ziCM6aJ1cK4Wb2kUfx6cIrSQCDEeuB-6HzdAyFo8IlB2jc6CCF82amC4AwocvRz4X-SQxD5vQImN6qJqTFbbpqUkYFTAZJFzTPO71tVAgX2X6NQ6cbT3sqN6eXtvV7Vm8hvBl7oa7tFbgHBUs6jen-n7GpSfTi91PL8oFOPdyShlnlrdVjWZ0r7UZvI-jKY-t-bp8krn7am_IlNBVv9YGsGQ_d_2RDHdgiS3s2kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ بقایی به احتمال دوباره مذاکرات و گنجاندن شروط جدید از سمت ایران: ما فعلا متمرکز به دفاع از ایران هستیم
🔹
سفر نخست وزیر عراق به ایران بسیار مهم است و نقطه عطفی در روابط دو کشور است. در جریان این سفر چند سند و یادداشت تفاهم به امضا خواهد رسید.
🔹
وزیر کشور امروز به پاکستان سفر خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/673339" target="_blank">📅 11:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673333">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzKIrLNhDbvu8w5v9LNVyASGvMuCjVIE0INA5dKvSz9W3NmA9hu3otXs2X0res8grM2ejvoWvHxzWB3D9dYg-S9lFH0SxCWp3v46a3olmZ4unPc486r7jAKI8WoSKcAg3ZXpGW2O4J2IUdO32_qSjeO8vmga5GTZL-qPf-uwvGSSQhlQLtr-odc_Qu5bl3Te0GhEyRbdKUZER6TTLXyERYJUVt-yYbWvz4tgykQNfI08UqEyq6hWKdhUSHRJ0wVL4tRhR-xbRWAYm8GPhbL9oULMQld5GV32jYE1jpYLPFCJyVTp9Wib2txJdGM6pUl9qxy1D2oFDpRftLDDoos-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حالا با آمریکا چه باید کرد؛ جنگ یا توافق؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/673333" target="_blank">📅 11:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673329">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc10b46a1.mp4?token=bvyjwm0E_djqgfe5MxrW3gmeoZDi0qWe8O3_vAyi75YdMsROQGmSRA-hqLd3TyrnltyU1tldZYCXmijwM1n596I_TdfIkdfv5K2MP0629O90qqpx8gyyS9626Wq4fHjSxeUYiCLmWkalouu57tc-Lm3s0C1iRM2YuSjG1nGZwOuitAhXfVDvD6riyFS_zABqHxQ2PEzsKWBAH07uyhNBByBTcip-5k8bNOa1eR46SJ2saHfeCn3YPQT_NhMRffyw7MXRUsunizUPm6p3sHFAxXbqXKizzytgoxEvrrmd18ml56BXLy8LfQ5wDrYViGzBymikn2NtVPXmwbXgiIg_Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc10b46a1.mp4?token=bvyjwm0E_djqgfe5MxrW3gmeoZDi0qWe8O3_vAyi75YdMsROQGmSRA-hqLd3TyrnltyU1tldZYCXmijwM1n596I_TdfIkdfv5K2MP0629O90qqpx8gyyS9626Wq4fHjSxeUYiCLmWkalouu57tc-Lm3s0C1iRM2YuSjG1nGZwOuitAhXfVDvD6riyFS_zABqHxQ2PEzsKWBAH07uyhNBByBTcip-5k8bNOa1eR46SJ2saHfeCn3YPQT_NhMRffyw7MXRUsunizUPm6p3sHFAxXbqXKizzytgoxEvrrmd18ml56BXLy8LfQ5wDrYViGzBymikn2NtVPXmwbXgiIg_Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش پربازدید کاربران فضای مجازی به بازی‌های آرژانتین در جام جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/673329" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673327">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تخم‌مرغ گران‌تر شد، کوچک‌تر هم شد!
🔹
قیمت هر شانه تخم‌مرغ در تهران به حدود ۴۸۰ هزار تومان رسیده؛ یعنی ۸۰ هزار تومان افزایش در دو هفته، خریداران می‌گویند با وجود قیمت‌گذاری شانه‌ها بر اساس وزن ۲ کیلو، تخم‌مرغ‌ها ریزتر و سبک‌تر شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/673327" target="_blank">📅 11:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673324">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b519d16da.mp4?token=VP109NDXvKUAFRJny2sMowwcvM01yH4hE4Tdf9uPwvip7D08FqMdpGnjmSUf7VuF28I5cBnhM4-gRThMTuXgAKsc7o9CDqy6U1hQ73FA0ic8GwAkzYTdOJS017vzeUX2_5kav0Sbc5rjywEeAocN3EJouoJvd2qFZ4ly2A_b49aG8OJwS5UkmhGcrZZ0Slv2D9dwLjlJd86GeUbgd5QFKkMuw3eR8uOLe9E7ywMaWxbrCW4yHsuoMehDcDmIn-Q-Atl7tcqsSjFuxdA4P2_JPTpTsWxl32AJPY5EqHjWMskBTvG0bKoD6YSJO0ursEI3c6KdTb-7hvYNA7gJlY-Wjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b519d16da.mp4?token=VP109NDXvKUAFRJny2sMowwcvM01yH4hE4Tdf9uPwvip7D08FqMdpGnjmSUf7VuF28I5cBnhM4-gRThMTuXgAKsc7o9CDqy6U1hQ73FA0ic8GwAkzYTdOJS017vzeUX2_5kav0Sbc5rjywEeAocN3EJouoJvd2qFZ4ly2A_b49aG8OJwS5UkmhGcrZZ0Slv2D9dwLjlJd86GeUbgd5QFKkMuw3eR8uOLe9E7ywMaWxbrCW4yHsuoMehDcDmIn-Q-Atl7tcqsSjFuxdA4P2_JPTpTsWxl32AJPY5EqHjWMskBTvG0bKoD6YSJO0ursEI3c6KdTb-7hvYNA7gJlY-Wjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش بقایی به تهدید آمریکا به تصرف جزیره خارک
🔹
مقامات آمریکایی این‌قدر در معرض گزارش‌های ساختگی هستند که هر خبری دوست ندارند را هوش مصنوعی می‌دانند
🔹
وقتی آمریکا حرف از دیپلماسی می‌زند معنیش تهدید و تحریک و تحمیل خواسته‌هایشان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/673324" target="_blank">📅 11:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673321">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZR7aeNFpmHjti6qewXsVBgF5X9Wsd_uoTFMcLuDBlmorowUcEq6IbW1vwivfBop4YhHYIDHh3T8m5I94qAt-J2ArBHTjhmMzbYLxHhvs2NvY9PikM2VkScJExge3SFvtyMBtHIbrp2PmgLJZp3AB5vB7PdsvU4tBJwcDE7C7CdP2gCbo83LbWYxWx84DbQ0z4g27lS22hHiDCYTK8rb87H7WYTt5b6U1Zn7egmQY2Ju_S_dcfFMI8lPKUNDfECqZX1lYZaB9_UcV1tz79i8Pr-fogC12nY_NCBL2wwz258DB4D-BYsPh8ZGusBUmS0wHRNIRrNg76bE-1iKrWLVLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNnDHEjbw7dXns6WcpEleIjWSU-_zNeVV6u_YSSZLWJAs38sMEydXvNdjcNNyReOwmduYperazPE3dN7A_OHMCUXWdG2AI0J4mSy8px12mL9MWgypsxgQbwdiraOXeQwwQAAkqA7VjT3G6EneiLr-i-w7qpbnsYflHeSGX336rO1H96nTYqdjcOo2GythmVMs561fyo_XelnJ0R5Nz-PAmuUYfCEX6SVXMyCpbDJ75R0ZPX4pXwpA9S9oKYvZOGrxXU2LLWVOOmrOlT5HRfw3NvflWRF_Nqn3S_4BT0sUGWUOf6kEvaR2yEBOguIOM_vrxeCr4wt7wAGHcOm_Z9dCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce7cd88cb1.mp4?token=n1roViAn3Iiuw-13IqrFHBN1LJ5Uoi0X43MVveX7dPchBiILusKuoNavArqjDma44Gj9HfVnG8lgb_sWAPB01LzSjHDMEcOnKO28gpRGvX55eNBlZ9A_ZWlJB2uG-7fkiSbnl-Skhhurnh3C_L_8npZnpAh5CztinvE15za6zCzohjaEQ7e_2FvCOPcxKXyv00my7SaauXnF1MNHZjClGWFB9HjCHbtvmqC1Xe-bxS6i1kognEuvYBLFA8N2_CC3GWyIswHIfrYDwYU1tJNHSkaPPmH1HKLHYfdOc1OMrkVHwlu6YrIjNiABLB2lSG6Kw8c8Zrpd4_z8S1YG4nMEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce7cd88cb1.mp4?token=n1roViAn3Iiuw-13IqrFHBN1LJ5Uoi0X43MVveX7dPchBiILusKuoNavArqjDma44Gj9HfVnG8lgb_sWAPB01LzSjHDMEcOnKO28gpRGvX55eNBlZ9A_ZWlJB2uG-7fkiSbnl-Skhhurnh3C_L_8npZnpAh5CztinvE15za6zCzohjaEQ7e_2FvCOPcxKXyv00my7SaauXnF1MNHZjClGWFB9HjCHbtvmqC1Xe-bxS6i1kognEuvYBLFA8N2_CC3GWyIswHIfrYDwYU1tJNHSkaPPmH1HKLHYfdOc1OMrkVHwlu6YrIjNiABLB2lSG6Kw8c8Zrpd4_z8S1YG4nMEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اعضای تیم ملی اسپانیا مدال طلای جام جهانی را دریافت کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/673321" target="_blank">📅 11:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673319">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d6385f7a.mp4?token=Q7SbP3L-IPKQApMHAbieDj1I54fUlKeD1Qg7GymoyL4o3jlKdxtdcnlDLS91BW3EAUL1Pp00rxdKtpcFwHQ39efZ4l1qsFe9aMzn0CTgiKNz08-YMbW0xHoIQ_XlbiMA6w1_YCWwOTWcrt1QnOkn6ZWQe8JI2FV-1C_HJsOeCC2aUsSnpZmt2ItIwA9vcDs18yoZ7Rp7apfIgO6uhPwlsbo2olIlIfgXYbdQjwzOg6LJlyshUzg9n1U8heOENfV_BJdYFHNzeOXwAq337G3EqBlIbjm_-SSB3-nS-jxk-1Ibf0789_09jCLRI6vQj8ttYOfmVHoniumVVYiUjaM4GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d6385f7a.mp4?token=Q7SbP3L-IPKQApMHAbieDj1I54fUlKeD1Qg7GymoyL4o3jlKdxtdcnlDLS91BW3EAUL1Pp00rxdKtpcFwHQ39efZ4l1qsFe9aMzn0CTgiKNz08-YMbW0xHoIQ_XlbiMA6w1_YCWwOTWcrt1QnOkn6ZWQe8JI2FV-1C_HJsOeCC2aUsSnpZmt2ItIwA9vcDs18yoZ7Rp7apfIgO6uhPwlsbo2olIlIfgXYbdQjwzOg6LJlyshUzg9n1U8heOENfV_BJdYFHNzeOXwAq337G3EqBlIbjm_-SSB3-nS-jxk-1Ibf0789_09jCLRI6vQj8ttYOfmVHoniumVVYiUjaM4GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: هیچ بهانه‌ای برای پیمان‌شکنی آمریکا وجود ندارد/ دشمن فریبکار، خدعه‌گر و وحشی است، اما این دلیل برای عقب‌نشینی نیست
بقائی:
🔹
پیشنهادهایی مطرح شده از سوی میانجی‌ها و دریافت کرده‌ایم، اما درباره جزئیات بگذارید ورود نکنم. اینکه ایده‌هایی واصل شده بله تایید است. بند ۵ یادداشت تفاهم حق مدیریت ایران بر تنگه هرمز را تثبیت کرد
🔹
اصرار بر دوگانه مذاکره یا جنگ، دیپلماسی یا جنگ برای کشور ما مفید نیست؛ کاری که سیدعباس انجام می‌دهد با کاری که سیدمجید انجام می‌دهد با یک هدف است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/673319" target="_blank">📅 10:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673317">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d51adb6372.mp4?token=obvyEUPlEkCrcboqZUA1HNcYcZpqJyXVA_riVTNZj5AEf9o0d9WVfFlzYeKu2B454pT4-rpxU6a6BxHMHvBuA1gPAVxGCUa_FPEm6KktRl5JQdGdv61Acy9GkCUPiSw96yuO_xvofW81CSOqOFh-HAxW8xj6SKl6HQzNimf_wQTmiij1T1edZpKx_DAUBt16EgOJDIRx7Pm-_cSr2nggnTIXpncssszrH6nQcKtOQ5WKdsc9MoCUNRPzNgiOAF5rj-C63CoIg_Sn02BhACVXGdzwbKFBn31MY6fdQ_dYWEAosbpylTs3Ss7W34-AIILGAXJIG7Iex2YPc6L2nRa4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d51adb6372.mp4?token=obvyEUPlEkCrcboqZUA1HNcYcZpqJyXVA_riVTNZj5AEf9o0d9WVfFlzYeKu2B454pT4-rpxU6a6BxHMHvBuA1gPAVxGCUa_FPEm6KktRl5JQdGdv61Acy9GkCUPiSw96yuO_xvofW81CSOqOFh-HAxW8xj6SKl6HQzNimf_wQTmiij1T1edZpKx_DAUBt16EgOJDIRx7Pm-_cSr2nggnTIXpncssszrH6nQcKtOQ5WKdsc9MoCUNRPzNgiOAF5rj-C63CoIg_Sn02BhACVXGdzwbKFBn31MY6fdQ_dYWEAosbpylTs3Ss7W34-AIILGAXJIG7Iex2YPc6L2nRa4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام تأسیسات آمریکا در پایگاه ملک فیصل اردن
🔹
تصاویر ماهواره‌ای انهدام بخش‌هایی از تأسیسات نیروهای آمریکا را در پایگاه هوایی ملک فیصل در اردن نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/673317" target="_blank">📅 10:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673316">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای الحدث: وزیر کشور ایران فردا در اسلام‌آباد با مقام‌های ارشد و رهبران پاکستان دیدار خواهد کرد/ انتخاب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/673316" target="_blank">📅 10:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268c33ffdb.mp4?token=aGR5Rt-7WIcY0Gz1LfBrryJocQ5KtJrMYlaLrbESRYTyg-YH2s8VcvuFVRQArCz_x-rcUO8olFeGvzdVCqR8rcVAZuLVEF5IUC-AdTIYtM8CTlnr0Xzwm4vpdLy9E5Qhxao0dCCPNImY9WxkyJQJhs1_cQXyfzyZOlXC8DXE4gsF7vl9495Qg7eLxhsUjcnkf06_NkFcfmQO-DFdNgZ_3FPBsrvmJMVYk9_F7cl4iQQBYvEn_Xx4haZYadxRxPe4kT_EOucD8SqB8rCkm0GjyMgUbp1Pxjfk2c48R2JxNpGbjJHpsNvbGMhwmIh0lyEyo5gMV_iE6Pybh3481fwZZ11AZbEgp9HQWOIAkGSM0LJcmtNBAA-aFnQ7pW5yO5tnEgZUH0Dep4CeXUvkc67qFHn3CyL-VhL2rKmszM318yABCzM4uHgA0gIE72ybAd7fRbQgzMHzcHc2y8376WT2OlowomkCUb2mw-8TJxtU-17VcAZpQw0eMR3K-STZE-BO3Y4O9-dTvaPedIiYk0eCQ8xPGbt9T-WjPMWjK08wrh9CeM1ZshtkmdSDXWxqTm4wG8-0XB6jnkrq6pRxKCNW2w2YTevi-6oyksv65Omqn6aFz04qtdxXDJOA9HrIBclPmyx0LA1VnW7JOSDU1UwVx-WMhJV5DNyq7N3pKLsMjB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268c33ffdb.mp4?token=aGR5Rt-7WIcY0Gz1LfBrryJocQ5KtJrMYlaLrbESRYTyg-YH2s8VcvuFVRQArCz_x-rcUO8olFeGvzdVCqR8rcVAZuLVEF5IUC-AdTIYtM8CTlnr0Xzwm4vpdLy9E5Qhxao0dCCPNImY9WxkyJQJhs1_cQXyfzyZOlXC8DXE4gsF7vl9495Qg7eLxhsUjcnkf06_NkFcfmQO-DFdNgZ_3FPBsrvmJMVYk9_F7cl4iQQBYvEn_Xx4haZYadxRxPe4kT_EOucD8SqB8rCkm0GjyMgUbp1Pxjfk2c48R2JxNpGbjJHpsNvbGMhwmIh0lyEyo5gMV_iE6Pybh3481fwZZ11AZbEgp9HQWOIAkGSM0LJcmtNBAA-aFnQ7pW5yO5tnEgZUH0Dep4CeXUvkc67qFHn3CyL-VhL2rKmszM318yABCzM4uHgA0gIE72ybAd7fRbQgzMHzcHc2y8376WT2OlowomkCUb2mw-8TJxtU-17VcAZpQw0eMR3K-STZE-BO3Y4O9-dTvaPedIiYk0eCQ8xPGbt9T-WjPMWjK08wrh9CeM1ZshtkmdSDXWxqTm4wG8-0XB6jnkrq6pRxKCNW2w2YTevi-6oyksv65Omqn6aFz04qtdxXDJOA9HrIBclPmyx0LA1VnW7JOSDU1UwVx-WMhJV5DNyq7N3pKLsMjB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: قهرمانی اسپانیا در سیاسی‌ترین جام جهانی تاریخ رقم خورد/ رویکرد ضدتجاوز اسپانیا محبوبیت جهانی این تیم را رقم زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/673315" target="_blank">📅 10:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673312">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
اعلام آمادگی پوتین برای تماس با رهبر معظم انقلاب
سخنگوی ریاست جمهوری روسیه:
🔹
در حال حاضر هیچ ترتیب خاصی برای تماس تلفنی بین ولادیمیر پوتین رئیس‌جمهور روسیه و آیت‌الله سید مجتبی خامنه‌ای رهبر جدید ایران، وجود ندارد؛ اما پوتین آماده چنین تماس‌هایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/673312" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673311">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267327f2c2.mp4?token=QuaQXGciJvktgXQ3zPcHxvQKTKNRKMqnecmR6jHITwmlHUxVNCx1X5bKrDJFRufJaPt3stb5idnRSnwDgHSiezjRlQttNCgjlbfJzfaCuqQWVOmNPZV13MTGDhTJYnQX4GjRl5ViONtiJVbvbrSgNG-Er2ff5sNSf8nIz0BNee7352TVomn5NFWvRZ4IcBrWCDJGiiJAToU7fjYESfZRO3IAzcGisQI5PXxohM9NA9wlrIva634HJDnbxYpiJ2nOusB2lsxGoYfUwXY0XikJv8yOdoEWC4yOrdK8i86Bt3NNXd8JIhTPy-k0d8aZBrAkmRJIES0q4AwEa1tPClwkAVpV7sM7suIgU2QAZMnW7JcmOjgYXp-jus5qFW8rpTEWrTyL6k5GK9txi0n6j9QdcPJUehfskE0CEfqBUdTRT-G8d9rO2zGOugSW1dgLkTmtUvAk_sHLHaoatiSw0tMTaamJbwLMgsCptsjaAY-q9wgk-w1ux-6-hIkdYzjdEuVLy2NZvJoE5t9U2kD5GB87Yxe4pXk1RI_fxFZqyGnBEJVNSrNP8g1E1j4OKGLc0LzLPOaOEP8cwGD4uK8Ce6x1XlF8M_dSklQogk_eJE8nTWUXIVmpW5UdVvPOy4j6Uzx_s2bY5GrLqPBsbBY36etl2t_y-gP2O466YfRNMQe2nlE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267327f2c2.mp4?token=QuaQXGciJvktgXQ3zPcHxvQKTKNRKMqnecmR6jHITwmlHUxVNCx1X5bKrDJFRufJaPt3stb5idnRSnwDgHSiezjRlQttNCgjlbfJzfaCuqQWVOmNPZV13MTGDhTJYnQX4GjRl5ViONtiJVbvbrSgNG-Er2ff5sNSf8nIz0BNee7352TVomn5NFWvRZ4IcBrWCDJGiiJAToU7fjYESfZRO3IAzcGisQI5PXxohM9NA9wlrIva634HJDnbxYpiJ2nOusB2lsxGoYfUwXY0XikJv8yOdoEWC4yOrdK8i86Bt3NNXd8JIhTPy-k0d8aZBrAkmRJIES0q4AwEa1tPClwkAVpV7sM7suIgU2QAZMnW7JcmOjgYXp-jus5qFW8rpTEWrTyL6k5GK9txi0n6j9QdcPJUehfskE0CEfqBUdTRT-G8d9rO2zGOugSW1dgLkTmtUvAk_sHLHaoatiSw0tMTaamJbwLMgsCptsjaAY-q9wgk-w1ux-6-hIkdYzjdEuVLy2NZvJoE5t9U2kD5GB87Yxe4pXk1RI_fxFZqyGnBEJVNSrNP8g1E1j4OKGLc0LzLPOaOEP8cwGD4uK8Ce6x1XlF8M_dSklQogk_eJE8nTWUXIVmpW5UdVvPOy4j6Uzx_s2bY5GrLqPBsbBY36etl2t_y-gP2O466YfRNMQe2nlE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک کیک خیس فوق‌العاده خوشمزه، اونم بدون فر ‌همزن و فقط در ۲دقیقه
😍
مواد لازم:
🔹
۲ عدد موز
🔹
۲ عدد تخم‌مرغ
🔹
۲ قاشق غذاخوری شکلات صبحانه
🔹
۲ قاشق غذاخوری پودر کاکائو
🔹
۱ و نیم لیوان آرد
🔹
۲ قاشق چایخوری بکینگ پودر
🔹
۱ قاشق چایخوری وانیل
🔹
نصف لیوان شیر
🔹
…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/673311" target="_blank">📅 10:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673310">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsAh_hYnSQ32OFL8EX-r0zjd3V7QFy7ej5zHOh369fkLmapg6glBd7WHfbNysIRLbe34FBpEcPdQD5SvdgURlNlZVCZ07f8E9QXM6CcMwIZ9lQk3GgKBxpCrvymDU6-o7OVJpDsTBMJeN5IUOasFMAeMgNWKMUKH-UJIawmI7JQMAT0HoSIu2x5OB0BDqlo1uVvNVSCqi94MxBVxWscpBnUTP1ZFzwPn9ShsqHEM-tp_TuDdLCda7lWNZ_xQDixk_nhGguDyJ4HMjIRlPLJfWwrHkbiSqms317lwbM5ykXC_uo1nLqTPW14bNYTBDi1SgKKm6qSJCv8eDKu0hZMZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجرای بیژن مرتضوی، موسیقی‌دان مازندرانی بین دو نیمه فینال #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/673310" target="_blank">📅 10:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673309">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e669f7f60c.mp4?token=PrOuodmD_Z8x3zg4Fo3Ungx5BqFDSWj9nvEdNNv0GWmQiGDHx_wM_XeYWRr_t3v6Di0Dw73oy3QfR3Vvwq3mcV4f9pi2LTtmYOWDcFFHf710I1j8vopbpscOk0G51wBaXV-L4kbUhNJ0KsJHRBWJ9BjH6m1Zj3y3MRRdzbYeKUDDiwOfxXw8cSkQQHdQ4LI0lnessWmtc4ow0Y2BM1PDplYKG6VPZKYQUwzwmdaQKM9zzI4UML1nJlhQvCAVW6i6dNPcFgkSuKWMpvbpaUEpTlUw892FZLIXVXXzNw_5USWUStimCx0oY63KrvyjBWrMpLqXI5ldc-J4-Y6Yr7ypAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e669f7f60c.mp4?token=PrOuodmD_Z8x3zg4Fo3Ungx5BqFDSWj9nvEdNNv0GWmQiGDHx_wM_XeYWRr_t3v6Di0Dw73oy3QfR3Vvwq3mcV4f9pi2LTtmYOWDcFFHf710I1j8vopbpscOk0G51wBaXV-L4kbUhNJ0KsJHRBWJ9BjH6m1Zj3y3MRRdzbYeKUDDiwOfxXw8cSkQQHdQ4LI0lnessWmtc4ow0Y2BM1PDplYKG6VPZKYQUwzwmdaQKM9zzI4UML1nJlhQvCAVW6i6dNPcFgkSuKWMpvbpaUEpTlUw892FZLIXVXXzNw_5USWUStimCx0oY63KrvyjBWrMpLqXI5ldc-J4-Y6Yr7ypAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خداحافظ اسطوره‌های بچگیمون؛
خداحافظ نسلی که به مستطیل سبز معنا می‌بخشیدید
آخرین رقص همه‌شون در جام جهانی با اشک‌ گره خورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/673309" target="_blank">📅 10:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673307">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdgiIos3v4AbkRlTM4hJ-HEvXIETS8_yrHJdzPolZkp6gGJd5sq9YAaeXg67KXjo-umAXzpz0ilHrJNL74iVJLc_r8Vssg9Dlj9qssN4gOcTY1QZRognbS95sBdb_V5meS8e1g42O6BzA_7F_5KfYzTg3FqON31hlE-xSuQYcwlkpbgyPQ1IOgefsd8lEfd1IIwuMwyKzkQ8kc1oSOU8zeUUY-OTdYo54r3Nf8VIWy6CgTRexOr0Xh2OJYzP-HK0TeTLjPBc7p8CGlpUG4ZX2PMlKHWVnzUsc1uPCLOMbX5Efzf7qn6lNEKbVe6Y-7C1pSOlLd09Cry6KL7h_Pi_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ایران به قهرمانی اسپانیا در جام جهانی ۲۰۲۶
سفارت ایران در مادرید:
🔹
به نام ملت ایران، صمیمانه قهرمانی درخشان اسپانیا در جام جهانی را تبریک می‌گوییم.
🔹
این قهرمانی کاملاً شایسته بود؛ دستاوردی که حاصل استعداد، تلاش، فداکاری و روحیه کار تیمی است.
🔹
این پیروزی تاریخی را به همه مردم اسپانیا صمیمانه تبریک می‌گوییم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/673307" target="_blank">📅 10:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673305">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQRendKore7_R94y_x_d9OmFo1VGtzWYBQhrZMzRKP9X1dDazmyXpX6A15WbnLeDutcFiP0SBZsC9qyRqjaDMGRVMNJ3-LhpimMAc4dYFapxsx9_VOXQWRgF3bWFYyF2fko3MXyD97obmk2zF4FHdcOd_ipb-BxwuJdJO_9-cLYzmOEEfo3jeFezZSHOqhNhv7U4SvwLS4-ZdbxHE50h94iEsPfnCoddTBlWUcF5ztzI9qM0-g1bdq2B8KwcdxnPNKQIzclZfDTPe-w0mjWXdr8lUsill-nW3McKeatpckGDzVsnNWMhUXJfLBBntt7BvdLI_zvZNZrjfuhuurjeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام فهرست داروهای ممنوعه عراق پیش از اربعین
؛
۱۴ دارویی که ممکن است در مرز عراق برایتان مشکل‌ساز شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/673305" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673304">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04c55b88b.mp4?token=kykL9qsT7uNYhUyBkbru_fIsFwsw5Skgdzt-8ou3u7Zems8kqAJxR5NxFuzMYaK1vDGKjzHwDwwfNvaPBZwJcxQ_jlzOUZg8whz4l4H6w7c4Pqlo3egIvJT7hHOy8ZjjS_SO6tdJUm7HgKdP9F9bjpGMByyANmF_kHJZsR9iK2EYjnCc8jWkWMmq9dJ5i1ApZ2IdVgQF1H2L7utOcoT4qX02hCb9c_91LtC1FocBDBo7ELRzKz8C0nsKN_KvxKZfpwNiNdfTuMHTMtU1FX3x8YzUHrNTcRLaI7PUvo7qpW9tYgc3IAOpUNSnK742ZGkTNbje76mYErjOtlzy8yETtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04c55b88b.mp4?token=kykL9qsT7uNYhUyBkbru_fIsFwsw5Skgdzt-8ou3u7Zems8kqAJxR5NxFuzMYaK1vDGKjzHwDwwfNvaPBZwJcxQ_jlzOUZg8whz4l4H6w7c4Pqlo3egIvJT7hHOy8ZjjS_SO6tdJUm7HgKdP9F9bjpGMByyANmF_kHJZsR9iK2EYjnCc8jWkWMmq9dJ5i1ApZ2IdVgQF1H2L7utOcoT4qX02hCb9c_91LtC1FocBDBo7ELRzKz8C0nsKN_KvxKZfpwNiNdfTuMHTMtU1FX3x8YzUHrNTcRLaI7PUvo7qpW9tYgc3IAOpUNSnK742ZGkTNbje76mYErjOtlzy8yETtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علاقه‌ی بی‌پایان مردم به خوک زرد؛ بیشترین هو کردن تاریخ ورزشگاه مت‌لایف به نام رئیس‌جمهور کودک‌کش آمریکا ثبت شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/673304" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673303">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
صداهای شنیده در اصفهان ناشی از انفجارهای کنترل شده است
مدیرکل مدیریت بحران استانداری اصفهان:
🔹
انفجارهای کنترل شده مرتبط با مهمات عمل‌نکرده در جنوب و غرب شهر اصفهان بهارستان  و محدوده صفه و محدوده شهر ابریشم از صبح روز جاری تا بعدازظهر ادامه دارد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/673303" target="_blank">📅 09:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673301">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07536f9517.mp4?token=j8bggeYH0l_E7ffnPYLxA7Kv1ERbKgGhjFrBGrBAqlgZ1VdhbzpnGEDea12HcfLp6s32e685nqq3nopuMzS2hWQ0FsqFfbJruMyRUwlFjkD90mOC3jL6K_bcleYakt0J7YnKCAF0JJoNon-yC_k9MyNKo1AVKmekDmkCyO3AtCY1N-CTgC6Qit8iyVsO74cm8lwPa0Rwns8lLA-l75UUYjbnT6UtV3iUVIJIOGS_smzBSO95uVxJFKFAqCj7s3AJKybv1saCtEzA3n5sULl0gD49af4TEfl4KLMfS0ZsZfJWWTC3qDmV8U16qCKilxxCRDDe8jAJ9Aag1AMtzNAIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07536f9517.mp4?token=j8bggeYH0l_E7ffnPYLxA7Kv1ERbKgGhjFrBGrBAqlgZ1VdhbzpnGEDea12HcfLp6s32e685nqq3nopuMzS2hWQ0FsqFfbJruMyRUwlFjkD90mOC3jL6K_bcleYakt0J7YnKCAF0JJoNon-yC_k9MyNKo1AVKmekDmkCyO3AtCY1N-CTgC6Qit8iyVsO74cm8lwPa0Rwns8lLA-l75UUYjbnT6UtV3iUVIJIOGS_smzBSO95uVxJFKFAqCj7s3AJKybv1saCtEzA3n5sULl0gD49af4TEfl4KLMfS0ZsZfJWWTC3qDmV8U16qCKilxxCRDDe8jAJ9Aag1AMtzNAIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدرت‌های بزرگ همیشه اهل حق را «برهم‌زننده آرامش جهان» می‌خوانند؛ اما ما اجازه نخواهیم داد آرامشِ ظلم، جای عدالت را بگیرد #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/673301" target="_blank">📅 09:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673299">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
چند نقطه شهر بوشهر هدف اصابت پرتابه دشمن قرار گرفت
فرماندار بوشهر:
🔹
دقایقی پیش چند نقطه شهر بوشهر مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت. / ایرنا
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/673299" target="_blank">📅 09:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673296">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
انفجار در قلب پایگاه آمریکایی بحرین؛ تصاویر ماهواره‌ای از خسارت به مرکز فرماندهی و داده‌های هوش مصنوعی پس از حمله کوبنده ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/673296" target="_blank">📅 09:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673292">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏆
اسپانیا برای دومین بار قهرمان جهان شد/ پایان رؤیای مسی در شب سرخ نیوجرسی
⬛️
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/673292" target="_blank">📅 09:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673291">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a646ece7.mp4?token=hV3wspVdAR4yNa-C8GkpwDnImuSGmVBJIRDDNHKN_TYh72kNEpg7V11Fc3wJusGMjTOFWHa4vItZoSw7_vc39NTAc7sYZMtRsDHYVGH8OvN4ZXk4yHdR8JbevUb8ZwB_cRMmNwH9ybZf8pCj1k34-6g68mTvRHYfkGOwjjKqGNMO133ieApREwGat4gJmAa5c4mYXLzgyEiPdzbn_cVC9gxjfeBSp_Dv6s_N5ls8M9QgkdcrosTYLIyFgsR_dRfRx6S4v8GIxMFffHHy3r-s7orre0v2rHlzP_uPmsHiWnmm19m_D2Wh5ieDvlibfXI1MrP9qD0Q7LDOZvX1y-fOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a646ece7.mp4?token=hV3wspVdAR4yNa-C8GkpwDnImuSGmVBJIRDDNHKN_TYh72kNEpg7V11Fc3wJusGMjTOFWHa4vItZoSw7_vc39NTAc7sYZMtRsDHYVGH8OvN4ZXk4yHdR8JbevUb8ZwB_cRMmNwH9ybZf8pCj1k34-6g68mTvRHYfkGOwjjKqGNMO133ieApREwGat4gJmAa5c4mYXLzgyEiPdzbn_cVC9gxjfeBSp_Dv6s_N5ls8M9QgkdcrosTYLIyFgsR_dRfRx6S4v8GIxMFffHHy3r-s7orre0v2rHlzP_uPmsHiWnmm19m_D2Wh5ieDvlibfXI1MrP9qD0Q7LDOZvX1y-fOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلگرام حالا از تصاویر اسلایدی پشتیبانی می‌کند
🔹
«پاول دورف»، مدیرعامل تلگرام، اعلام کرد که قابلیت Carousels به این پیام‌رسان اضافه شده است. او به شوخی گفت با این قابلیت کاربران اکنون می‌توانند تصاویر گربه‌ها را درون اسلایدهای ارائه خود بگذارند. با این ویژگی می‌توان با کشیدن انگشت به چپ و راست بین عکس‌ها جابه‌جا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/673291" target="_blank">📅 09:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
مدیرکل مدیریت بحران آذربایجان‌غربی: بامداد امروز دوشنبه، نقطه‌ای در حوالی ارومیه هدف اصابت پرتابه دشمن قرار گرفت
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/673285" target="_blank">📅 08:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673283">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2jabE0Ouzt4ZxHCLZr00hgcaEPTcpaRVkqeeGdLC5vmq62tO3WXNYOShLfsMIkR-NadW5Fhm4u16tFbAMfjDSUSGlcl4v_ZnttLK3QeG-1Y2-RSPevNHYVkGwKaiY92lnDmB5-5Xk0UD0f8R7mCBwyLGt_THxLmi8bxrZrS68gxjuXhHU37uepN-GUXICEVAkP8hmmHrWctSJEqfw7FIycbnfFzMe0HS_6kPuvBq3unCYGlriaqZHY8VAK04j9vjrlxR_X3TYWKwaL0mfVYOwokW-JRWADHwUcpiLCkIfKR-Xnveo0PfMvqmLrxPE65_mTxPb77ojwaXSE23Q4C2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امام جمعه اهل سنت میرجاوه ساعت ۴ صبح توسط افراد  ناشناس ترور شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/673283" target="_blank">📅 08:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673281">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITmX2B9--j4gGreFeQfxik3QJnuPMXJeYN81VZ0rao70tA8N6WVUCa0Hkg6ZEwM0WUlfc1CrGj_WeKLSeUncSX9lUV0CmoiIWa6YfedoQ7bNOvgxKrgLETtCURXTnXdG1TFU3MgYqS0ulGBJHyp1RkYwZIOB4Y-wxF5SmPvNchprGhOJ6hrvrVQYrTsYlsKuaV6F_Rn3H3cqFtnU45nC4jU38pyiJWUcwfqv6qy4luJ4F8DrVlwjwS-BDlJDUVVB_-iJ6-LemzZoEz0PnspRL2PBNJ3qkH1w5yGKOqFXeblzL8ZO-l2T9PRsWMNvBOfAaw2d6jc4oEzDCUki9D3OQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/673281" target="_blank">📅 08:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673280">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
فقط ۲ روز تا پایان مهلت استفاده از اعتبار کالابرگ باقی مانده است
🔹
معاون اقتصادی وزارت تعاون، کار و رفاه اجتماعی: مهلت استفاده از اعتبار یک میلیون تومانی کالابرگ خردادماه، تا پایان ۳۱ تیرماه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/673280" target="_blank">📅 08:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673276">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
گزارش صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن به کشورمان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/673276" target="_blank">📅 08:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
زلزلۀ ۵٫۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵٫۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند.  #اخبار_کرمانشاه در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/673272" target="_blank">📅 07:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
زلزلۀ ۵٫۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵٫۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/673269" target="_blank">📅 07:34 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
