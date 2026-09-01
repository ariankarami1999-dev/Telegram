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
<img src="https://cdn4.telesco.pe/file/j_MuSm4VCHnWYJY9oh6ywNqTDEVTm1ZuWZRuM19vddntOUWwPSv48URmqGAMyA7xCzrHIdaIPx_WtKqLxKn8kHnZWg1mthim-TxL-Ipwn4zBjTzsDFp1ZI3OLyW9b8rtuIdJGQHBQMqFQRehbOs9amQu1slc6rWZyUyIwJEzYbRCHPHZsknk_hcSIXlBNqnDV_XD0KlhTWhsGs6adA6V7GuPVfTkZvGDs8xQwNeLG29jJHVxxD5ZHtTByHGvNkn85dmVKcW5UXv3NfiOJe1IwCzVrPhRCbWqZPi7hhY-lPki1fHzn5V-xcy6N-YEmDYaU3Z0kU3IKTz1LXCMG2OSjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-686160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=oMAvuDgdX69EIriMipwVNGAgQm-U2isf8iyP1lLJnAN2xWni9fQRb3rTIJADLAfwl99PD3w8paBz0MdI0Lr9amUmc2mGJJRRdb_nyqKSkpvdf_HO_0_5ySi3Is7zqzRH9-3sLgxu8Zpoc4gT6Wy2r7OWo3apoc4TsDYd7k5h0O597fBdOJHOaBTFZYoH4Vsf1OuaqxVW8-oQie3oWJjjKX3jTVv99oABuJGKIAU9SzMcySukjCV2tOpmEtcWX3DUCDX1Jz3kXhpE8p92dFy8EROZlPYXIF3VyNDO8_TpFuR77flTpbDpFnZakcS_ctuBVU4o9m95efxzmTC2PYu7yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=oMAvuDgdX69EIriMipwVNGAgQm-U2isf8iyP1lLJnAN2xWni9fQRb3rTIJADLAfwl99PD3w8paBz0MdI0Lr9amUmc2mGJJRRdb_nyqKSkpvdf_HO_0_5ySi3Is7zqzRH9-3sLgxu8Zpoc4gT6Wy2r7OWo3apoc4TsDYd7k5h0O597fBdOJHOaBTFZYoH4Vsf1OuaqxVW8-oQie3oWJjjKX3jTVv99oABuJGKIAU9SzMcySukjCV2tOpmEtcWX3DUCDX1Jz3kXhpE8p92dFy8EROZlPYXIF3VyNDO8_TpFuR77flTpbDpFnZakcS_ctuBVU4o9m95efxzmTC2PYu7yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: عاصم منیر نه پیام مثبتی داشت و نه منفی؛ بلکه برای کمک به کاهش تنش به ایران سفر کرد
🔹
آمریکا مفهوم مذاکرات را با دیکته‌کردن اشتباه گرفته. نیروهای مسلح ما هیچ تعرضی را بی‌پاسخ نخواهند گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/686160" target="_blank">📅 15:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
دیدار پزشکیان و پوتین در بیشکک
🔹
روسای جمهوری ایران و روسیه در حاشیه اجلاس شانگهای در بیشکک قرقیزستان دیدار کردند.
🔹
طرفین صبح سه‌شنبه به وقت محلی در بیشکک دیدگاههای خود را در اجلاس سران شانگهای و شانگهای‌پلاس بیان کرده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/686159" target="_blank">📅 15:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
همه اقدامات آمریکا در تجاوز نظامی مصداق جنایت جنگی است  سخنگوی وزارت امور خارجه:
🔹
ما نیازی به استناد به گزارش نشریات غربی یا کارشناسان غربی نداریم که اتفاق میناب و لامرد مصداق جنایت جنگی بوده است.
🔹
یادمان نرود یکی از شیوه‌های آمریکا برای پوشاندن عمق جنایتشان…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/686158" target="_blank">📅 15:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
همه اقدامات آمریکا در تجاوز نظامی مصداق جنایت جنگی است
سخنگوی وزارت امور خارجه:
🔹
ما نیازی به استناد به گزارش نشریات غربی یا کارشناسان غربی نداریم که اتفاق میناب و لامرد مصداق جنایت جنگی بوده است.
🔹
یادمان نرود یکی از شیوه‌های آمریکا برای پوشاندن عمق جنایتشان این است که رسانه را مشغول کنند تا صرفا یک یا دو مورد را بپذیرند و باقی را قانونی بدانند.
🔹
همه اقدامات آمریکا در تجاوز نظامی تک تکش مصداق جنایت جنگی است. میناب برجسته شد به دلیل اینکه جمعی از معصوم ترین انسان‌ها به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/686157" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbFfKLJ8PfawXf3fgTI5Qc1cp5d25xn-0r9CeSQCglHanNV31VQJNXtVS5dACLaezOMQ2d4V2Y-QuHy6PXRu0d5jmuDJsVSkBmngfAIVX0ZXIqlZDt_cnTH3vyVGgF0HEC_S9LfU7Nx65mBgyjlse7NgKEeFWK81LWq-CzDhwqHk5F4YIOKC9cdR3pGHAlrMXL-96YpVHtFh8h7tfFnoJTVFsn_uUztzIi4khTrnMXTVH8BHmZd-h3Te8T2Uw7ZlHFdevKYmy48n5HDZ4iBnyJ5-YHD5Rf6rrbn5Xbii1bgZvJ_NX-fZ1b4S2kN3p-PEb0nHRpnw9ahwXBlem4Xu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۳ درصد آمریکایی‌ها می‌گویند واشنگتن باید نفت ایران را تصاحب کند!
🔹
نظرسنجی yougov نشان می‌دهد که تنها حدود یک‌چهارم آمریکایی‌ها (۲۳ درصد) معتقدند اگر آمریکا ایران را شکست دهد، باید نفت ایران را تصاحب کند.
🔹
در مقابل، ۵۳ درصد می‌گویند آمریکا نباید چنین کاری انجام دهد.
🔹
در میان دموکرات‌ها تنها ۹ درصد، در میان مستقل‌ها ۱۹ درصد و در میان جمهوری‌خواهان ۴۲ درصد خواهان تصاحب نفت ایران در صورت پیروزی آمریکا در جنگ هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/686156" target="_blank">📅 15:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686155">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8482f20060.mp4?token=RYlJYb-ArZxzurBl8GjK1iDJ7MqeDJflI2PupBbrEAEIbz2CFGr3rFGi6StQx6aBvIiddD16CV7cPa_yNDkl7_P7z8zcxbMZN7u9J2cs1mCw6AARHuWzndpXm01BUnAr9-H21sIrku7w7O1DBdZWmFyqHVJ0iy41CiWmota8v3_p9p3ePMzfwHtZlDG826tVx_ovbKV8T8EUxCkPqkPsXn-uu_y2xCRDd_etlp5hmDpmhrM7jyUyB5-06FseOSfVlaHdu4yb9AsNhk1n5YBIyvRUjZkkr6m6FU7I31LNs6l0u986UkEstQISda6uwU9Y2nmj1GmRr9w9UUBgvmlQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8482f20060.mp4?token=RYlJYb-ArZxzurBl8GjK1iDJ7MqeDJflI2PupBbrEAEIbz2CFGr3rFGi6StQx6aBvIiddD16CV7cPa_yNDkl7_P7z8zcxbMZN7u9J2cs1mCw6AARHuWzndpXm01BUnAr9-H21sIrku7w7O1DBdZWmFyqHVJ0iy41CiWmota8v3_p9p3ePMzfwHtZlDG826tVx_ovbKV8T8EUxCkPqkPsXn-uu_y2xCRDd_etlp5hmDpmhrM7jyUyB5-06FseOSfVlaHdu4yb9AsNhk1n5YBIyvRUjZkkr6m6FU7I31LNs6l0u986UkEstQISda6uwU9Y2nmj1GmRr9w9UUBgvmlQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمول متفاوت «مای‌دات» برای شبکه‌های اجتماعی: پاداش به آشتی، نه جنجال!
پویان رازانی، مدیرعامل دات‌وان سیستم در حاشیه نمایشگاه الکامپ:
نقطه اشتراک مای‌دات با بقیه اپلیکیشن‌ها، دور هم جمع کردن مردم است؛ اما مزیت ما این است که به
تعامل و آشتی دادن
جایزه می‌دهیم، نه به دیده‌شدن به هر قیمتی!
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/686155" target="_blank">📅 15:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686154">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
برگزاری آزمون‌های تافل و GRE رسماً در ایران متوقف شد
🔹
مؤسسه ETS در صفحه رسمی ثبت‌نام آزمون TOEFL iBT اعلام کرد که در راستای رعایت تغییر اخیر در مقررات وزارت خزانه‌داری آمریکا (OFAC) برگزاری آزمون‌های TOEFL و GRE در ایران متوقف شده است.
🔹
این مؤسسه یادآور…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/686154" target="_blank">📅 15:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686152">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آپارتمان‌های لوکس پایتخت متری چند؟
🔹
در شمال تهران، قیمت خانه از مرزهای تصور عبور کرده است. هر متر آپارتمان در گران‌ترین معاملات منطقه یک تا ۱.۵ میلیارد تومان قیمت خورده که معادل حدود ۷۵۰۰ دلار است.
🔹
در صاحبقرانیه، متوسط قیمت آپارتمان‌های نوساز در مردادماه حدود متری ۸۰۰ میلیون تومان بوده است. این قیمت‌ها مربوط به بخش بسیار کوچکی از بازار است؛ تنها حدود ۱ تا ۵ صدم درصد از کل معاملات در چنین سطوحی انجام می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/686152" target="_blank">📅 14:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686151">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c2539c0d4.mp4?token=M3bk1_bsIw5lmwA4SYEjg0A7JleGzbHVGxnSKfZe8s_DnVcWZqLFrH8iecscnul6bsQnPTF4CcH4bRIzPCxWM4ibw2QtwKY-6w0EUJBy1TCdOuq9T7cO-D03_fGdcLUWUBBA4M9cgIV0b_378ZQczeG8fXfbbMfe6iyv1zjiJJAkxUep82SI7X4qWRC591AcASo6Zmh8XC33YTSHAFk7Lw1JI8MDkLrYWn2HxWQRQGICer2ps3_f-LG8Nr-2twTXwYoDOfJ8Gc7HOUCrP-J9Jbok9PTP2ZOrlYavhgxvoB4-y6ekO39v6gnW-hsU88Uph1F_0rG-6PDXix_vZsNFVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c2539c0d4.mp4?token=M3bk1_bsIw5lmwA4SYEjg0A7JleGzbHVGxnSKfZe8s_DnVcWZqLFrH8iecscnul6bsQnPTF4CcH4bRIzPCxWM4ibw2QtwKY-6w0EUJBy1TCdOuq9T7cO-D03_fGdcLUWUBBA4M9cgIV0b_378ZQczeG8fXfbbMfe6iyv1zjiJJAkxUep82SI7X4qWRC591AcASo6Zmh8XC33YTSHAFk7Lw1JI8MDkLrYWn2HxWQRQGICer2ps3_f-LG8Nr-2twTXwYoDOfJ8Gc7HOUCrP-J9Jbok9PTP2ZOrlYavhgxvoB4-y6ekO39v6gnW-hsU88Uph1F_0rG-6PDXix_vZsNFVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود یک فروند بوئینگ ۷۳۷ به ناوگان لاد ایر
🔹
یک فروند هواپیمای بوئینگ ۷۳۷ با اتمام مراحل چک سنگین C، به ناوگان شرکت هواپیمایی لاد ایر اضافه خواهد شد. این هواپیما چند ماه پیش به کشور وارد شده بود.
🔹
به گزارش کن‌نیوز، ورود این هواپیما گامی دیگر در مسیر توسعه ناوگان لاد ایر و افزایش ظرفیت عملیاتی این شرکت به شمار می‌رود. لاد ایر که فعالیت خود را با محوریت فرودگاه لارستان توسعه داده است، در ماه‌های اخیر در مسیرهای داخلی از جمله مشهد، شیراز، ایلام، اصفهان، آبادان، اهواز و... در حال خدمت رسانی به مردم می باشد.
🔹
با اضافه‌شدن بوئینگ ۷۳۷، ظرفیت ناوگان لاد ایر برای توسعه پروازها و افزایش مقاصد پروازی داخلی و پروازهای بین المللی تقویت خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/686151" target="_blank">📅 14:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588e633c3e.mp4?token=ePTlgbNVgVDueM1WGn163geoIB7wCUvVTtU2O6p-u1vsJZJ4d2g0EGHbKMkr31NePolhe1SjXhA5OLjnr4PD1np-yDrviGJ2t4C7t9nCo_xKqcEbRhfRKhex0KNCLygEeQOEitLxDck6LJUEsIUE1yqji5LIvtrCE0DbgQ6RVsqrdISB96NPVpGjlJ4xqhw5zVUiBPRrAh0oa3aAW4KiusTTfdEE2kwHfiNqTfEx6E4l6PpiFOgrpGTgagmZxsikV40fpQHgJYm22Cxza5Ov63L7OiLnCF8QA-2wb3JdIHytbmcCmRJrtsleDCx5vmuz6GvHU8xnydGqCkc3-iqzLDeps8aiKSd-0iT6LUAGJKZMkWcUCoyJghTVAZxdNPt1n1gpmi1Yx8v1TRx_uXjMMLQ6_KUN5AquJF30tHjO94ovd1ALvOVKYkq5uCx1sRXA6iyYFFePtb9lXJQtMNZ-J47Y2XaxtmboZJ_1olWktpRCjgKUGP0QfM9YveF6bz39Ugpvvgehm0LZT0N1yO31FAexWn66Xm9S2CRFj0MTpmWerKNBQUOny0dyXkFGJhpW9VHSTqQIhgPRO_IxMlYbEgtcBGkLLmX_v33b6lLsLHHOUzpt6xQ-XhGw3OywU-A7qMfS2B2AhLV42iPZuaO2N89vFpbpQ5uNVDzRlWm64cU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588e633c3e.mp4?token=ePTlgbNVgVDueM1WGn163geoIB7wCUvVTtU2O6p-u1vsJZJ4d2g0EGHbKMkr31NePolhe1SjXhA5OLjnr4PD1np-yDrviGJ2t4C7t9nCo_xKqcEbRhfRKhex0KNCLygEeQOEitLxDck6LJUEsIUE1yqji5LIvtrCE0DbgQ6RVsqrdISB96NPVpGjlJ4xqhw5zVUiBPRrAh0oa3aAW4KiusTTfdEE2kwHfiNqTfEx6E4l6PpiFOgrpGTgagmZxsikV40fpQHgJYm22Cxza5Ov63L7OiLnCF8QA-2wb3JdIHytbmcCmRJrtsleDCx5vmuz6GvHU8xnydGqCkc3-iqzLDeps8aiKSd-0iT6LUAGJKZMkWcUCoyJghTVAZxdNPt1n1gpmi1Yx8v1TRx_uXjMMLQ6_KUN5AquJF30tHjO94ovd1ALvOVKYkq5uCx1sRXA6iyYFFePtb9lXJQtMNZ-J47Y2XaxtmboZJ_1olWktpRCjgKUGP0QfM9YveF6bz39Ugpvvgehm0LZT0N1yO31FAexWn66Xm9S2CRFj0MTpmWerKNBQUOny0dyXkFGJhpW9VHSTqQIhgPRO_IxMlYbEgtcBGkLLmX_v33b6lLsLHHOUzpt6xQ-XhGw3OywU-A7qMfS2B2AhLV42iPZuaO2N89vFpbpQ5uNVDzRlWm64cU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روز شلوغ غرفه خبرفوری در الکامپ ۲۰۲۶
🔹
از اولین ساعت‌های شروع نمایشگاه تا میانه روز، غرفه خبرفوری شاهد رفت‌وآمد و حضور پررنگ بازدیدکنندگان بود؛ از دیدارهای تازه و گفت‌وگوهای جذاب تا ثبت لحظه‌هایی که حال‌وهوای الکامپ را متفاوت‌تر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/686150" target="_blank">📅 14:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686149">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcB2GVHl2b9fiE77Hvvl9HofcTRgRznXpYMr0a_7mPo1Nrx4PuRXc2EWIO1OwSMTqct_UMgWzgVDU3hA4Vv1vwpa1B46hvDzpLKA6U5HjV_-Kq9WtXmvTu3A0oHbQpytaMlK6aSVfSJMSi98sE0_LzR7GkSAiBYmOi5JiqVOtXRtgbL8be7L-7KU7vLhutAonofBpZAzp10yeGVq1qVShLr43wiS3qIr8Krqlin2tC8nwWfVbjC3xVtY9UmatkIwoJRXVkcG9m9tY5WGWmDgJXoy2gH4A2_FcygYxN-V95MIMaCDPnMUp6t2sA3oeROTbILUERHXGAmeT0eexmJ6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دهم شهریور روز پدافند هوایی ارتش، بر تمامی کارکنان این نیرو که در خط مقدم جنگ با دشمن آمریکایی اسرائیلی بودند مبارک باد
🔹
آمار زیر تنها مربوط به عملکرد پدافند هوایی ارتش در جنگ رمضان می باشد:
۱۷ پهپاد MQ-9
۲۴ پهپاد هرمس
۱۸ پهپاد اوربیتر
۲۷ پهپاد لوکاس
۲۱ موشک تاماهاک
۱۳ موشک JASSM
۱ جنگنده A-۱٠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/686149" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686148">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H33eV8QqhOSiH_hLjAWaO-lC1gKmCfhAsKiIfLR1ePl2qodIAsgFgsOl56da8zBFBYO9E2Pf5aryEhPCvmP7wEkvZG_dDqdH-e8fKuNsy5wUZQXUTIG-jh-tO8hkYIX5vwFAIyEnEBQuMba1JX0nfI-84ZFsYF5n8l5V0cw4y77GkZ3gJRNRXbnjKiw7HQsQvtPYt1Py0IykZyHDjOP73xfRY-9CBogFiZxatrX6NVMlj64OwJlOKW-DSaQ7sCsAVhCixFffp3tDLhH1OxbyRX6-lj2tpYSCYh9ihQDJH9u7lKcVAyv2nR4rnW0iOZf0wE6QbT9X1GDID9PYFUFcxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نبویان: اکنون بهترین زمان برای حمله پیش‌دستانه به منافع آمریکا است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/686148" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686147">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8874808e.mp4?token=niYZhycWQ0VLdBbX_ayKsOuxhs1-UBL8kTyZvG2lpbIOMU8JWpnUkLS3f6Nz9RFJUYLaEPbEDeVmIut1oCiEn5UkWQZT11SV0Csgyjo1gDno0Kh7vlP89-THtchLzFaxRDOAb_cLaMdtvCE4_Uy2p2kJufXI1bc16vng6gUjgJ0RPzKab6jbPOcpoQ-432iv0g3kqFhhfm0jma05QqJBYmBYkxrpucei_x-ZpjmBqbQauC39ZqiM6I2dlqRNipJPn9P1lm0kHY_bADWktu4vsSZTdHIlwK7R5g3Nt0GIkuU9USFIRK6ZcIztYhKPDvDuK970d9o9mfWAVp0ZE-5Etg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8874808e.mp4?token=niYZhycWQ0VLdBbX_ayKsOuxhs1-UBL8kTyZvG2lpbIOMU8JWpnUkLS3f6Nz9RFJUYLaEPbEDeVmIut1oCiEn5UkWQZT11SV0Csgyjo1gDno0Kh7vlP89-THtchLzFaxRDOAb_cLaMdtvCE4_Uy2p2kJufXI1bc16vng6gUjgJ0RPzKab6jbPOcpoQ-432iv0g3kqFhhfm0jma05QqJBYmBYkxrpucei_x-ZpjmBqbQauC39ZqiM6I2dlqRNipJPn9P1lm0kHY_bADWktu4vsSZTdHIlwK7R5g3Nt0GIkuU9USFIRK6ZcIztYhKPDvDuK970d9o9mfWAVp0ZE-5Etg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این اشتباه ذهنی می‌تواند شما را فقیر‌تر کند!
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/686147" target="_blank">📅 14:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8c04b989.mp4?token=W6xr4MpQgA1Xxz7zV9fBLi3D_q6W9ExwBosrV3yYJmvgaEQgD6URaW90dE80YWVqLgdzF3l1pOZ8RlZcQoovDYgZIMf1I4X3h6yez5fN-EoxW96Qxb5nBSw65P1MUYeUAfSS1D7MsJf4Nm6S312m_Uo42-c1uqsIRKGbx3UGk-v06oORCZXM3d0X7MoyaOcmj8UnugkZ960slWegqGTnn5z0LlfH9QlBE9wFXA9aaGosY4RkWOneA7tX1jLI-icBybOAUnRODfJdOB-8ih1O486mREIbr4Cb8DQ9p5wnh6Qep411www_Ef46I4O324jVKzpXLPDz6CxEob-amt9ZNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8c04b989.mp4?token=W6xr4MpQgA1Xxz7zV9fBLi3D_q6W9ExwBosrV3yYJmvgaEQgD6URaW90dE80YWVqLgdzF3l1pOZ8RlZcQoovDYgZIMf1I4X3h6yez5fN-EoxW96Qxb5nBSw65P1MUYeUAfSS1D7MsJf4Nm6S312m_Uo42-c1uqsIRKGbx3UGk-v06oORCZXM3d0X7MoyaOcmj8UnugkZ960slWegqGTnn5z0LlfH9QlBE9wFXA9aaGosY4RkWOneA7tX1jLI-icBybOAUnRODfJdOB-8ih1O486mREIbr4Cb8DQ9p5wnh6Qep411www_Ef46I4O324jVKzpXLPDz6CxEob-amt9ZNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار بزرگ در ادلب سوریه
🔹
منابع سوری از انفجار در یک انبار مهمات در شهر «بنش» واقع در شمال استان ادلب خبر دادند که تاکنون دلیل آن مشخص نشده.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/686144" target="_blank">📅 14:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa9e-URV1qwPxgTkT2swZickkzd4SaXAhOgjcygV5Jwc6bJC9qOfQiLa5eKPC4XZfWSDSzoDkyzfkay9kiDArxqgqeGhygBfILDah0UJVKBCozrmrUQMdggazhEB0XrNlBs9388usSH8YRylj7jCnOO9O-6bgozl5ZuHWRD1-MJoX8lqIKBODClJPKA5ujwzPLviSvDR26TYf5cmsec4qN9Z26w3ew0fdUDMaVreZsse0FSnXYkgoe9mgo3Nv0Cc09oWG3ki2_MIQAr9a8fmZpjDuPmPiJ3R1IrEIUY4O_2p1p7Xw4a-PGnd__zVJ76-ijSTT-pTWB8edSRThtjmfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس سبز شد، اما پول حقیقی‌ها فرار کرد!
🔹
بورس امروز با یک تناقض بزرگ به کار خود پایان داد، شاخص کل ۳۶ هزار واحد رشد کرد، اما بخش عمده بازار در محدوده منفی معامله شد. در پایان معاملات، ارزش معاملات خرد به ۵۹ همت رسید و حقیقی‌ها حدود ۴.۳ همت پول از بازار خارج کردند.
🔹
همزمان، صندوق‌های درآمد ثابت شاهد بیش از ۲ همت خروج نقدینگی بودند و صندوق‌های طلا حدود ۶ میلیارد تومان ورود پول ثبت کردند.
🔹
با وجود رشد شاخص کل تا ارتفاع ۶ میلیون و ۵۸۳ هزار و ۹۳۲ واحد، تصویر کلی بازار چندان سبز نبود و ۷۷ درصد نمادها منفی و تنها ۲۳ درصد مثبت بودند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/686143" target="_blank">📅 14:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e871d307.mp4?token=h2gW6i5ZbIKTdHjWe6qsDNrzci8K8QLPwXUXAJaSgTZaSxfKN8QXlWHE_sfEY2Wj_UOvM30qYP9tT4NyAGnyQa86aMKHpVIgK0Zw7aHly088hRjkwyRVh32Q93MlzPctoXhBMKN2xxlKn2GDVDTNrSTyAfORmcwDZb6ubF0jpSPorDDjzwk-22XfpVw6ERggXzKIT8YADLUOMLUTRwBp7txevedKjw5eOhHwjxsuJIkb_B0NcoUD__npoVdVCLN3AnerogXZxc2mJUNUieV-QTZeMW8dAiIB6BdfQgJ2MsxHAiMbtxtoCoy1U5vZ5kcPtbv4eTBBCRLFOonZHJxGuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e871d307.mp4?token=h2gW6i5ZbIKTdHjWe6qsDNrzci8K8QLPwXUXAJaSgTZaSxfKN8QXlWHE_sfEY2Wj_UOvM30qYP9tT4NyAGnyQa86aMKHpVIgK0Zw7aHly088hRjkwyRVh32Q93MlzPctoXhBMKN2xxlKn2GDVDTNrSTyAfORmcwDZb6ubF0jpSPorDDjzwk-22XfpVw6ERggXzKIT8YADLUOMLUTRwBp7txevedKjw5eOhHwjxsuJIkb_B0NcoUD__npoVdVCLN3AnerogXZxc2mJUNUieV-QTZeMW8dAiIB6BdfQgJ2MsxHAiMbtxtoCoy1U5vZ5kcPtbv4eTBBCRLFOonZHJxGuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با هر رنگ شلوار، چه شومیزی بپوشیم تا استایل شیک و رسمی داشته باشیم؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/686142" target="_blank">📅 14:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
خبرفوری در الکامپ اخبار لحظه به لحظه رویداد بزرگ فناوری و اقتصاد دیجیتال را به اطلاع شما خواهد رساند
🔹
ما در نمایشگاه الکامپ در سالن ۶ غرفه ۳۲ میزبان حضور پرافتخار شما عزیزان هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/686141" target="_blank">📅 13:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686138">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRm10D9sOiMdgAZeR86KSYBckSng3fD1kR49JH6x00fMWiwF56obQ7xx4PXjsWTtmcTKxoHtZfm-DEd3jO2r4FHlagXEEtHPvA7AbrIvkkzsHbjIc776t6LGbzq0-gItqNuqqrY8nCognXrcUr_Uh8FnSYPPFySpNprrryfVMF4Jmjstnu1JMugEOe85RDhS9TivwUn1UPy0eSwZIWBIZGi2geN-8yeBN-IODVrGH6WBrbNzltTW8tycYY9dA3j83yECIhOAEXP4VaxcqtNnxIl02LC-nsvScEcsTT96yajXj_u2FXTXKhHrWPPVs2du14Zn7c6mohZ2TYl7-up0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjsCTnAXHlFR7E6kurmyeYvc_p0D6cJj3iPdW4UAKxfy7ZXZ3gNF_z2dF7prMsNTzDz3TNjVue9dVn56wLMGhSrApsp9oyR88-QatIGiW_XrE4DphRj0OgH2QOs8KKGl7DWSJX0Pm7eTPeajhaGnX-FZrxuBWNzUVUTMCs2w2F3q_iimGi0HqnujP2NJ3tzsoTJIKNgrJoY08vULlGOrQoakI8XQg6LRhqhzf1bgC6vN0mRctJh4jjRLZaVJ5qmnoWXYq52VT4Rq0G6XYlxSx8kYkfV18TBTfF8zLYh_LvvlhexXwlIoVGLogAIdT-o4mA0hrVdXPBLQqgYRPByINg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرعت عمل در بازسازی پل‌های بمباران شده در جنگ
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/686138" target="_blank">📅 13:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686137">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رئیس بانک مرکزی: احتمال ابرتورم را ضعیف می‌دانم  همتی:
🔹
با وجود فشار تحریم‌ها، تورم و مشکلات معیشتی، هنوز وارد ابرتورم نشده‌ایم و احتمال وقوع آن را ضعیف می‌دانم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/686137" target="_blank">📅 13:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686136">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
کدام جاده‌های شمال یک‌طرفه می‌شوند؟
پلیس‌راه مازندران:
🔹
ترافیک ورودی در جاد‌ه‌های کندوان، هراز و سوادکوه سنگین گزارش شده است.
🔹
از ساعت ۱۲ مرزن‌آباد در جادهٔ کندوان مسدود شده و از ساعت ۱۴:۳۰ مسیر جنوب به شمال پل‌زنگوله یک‌طرفه خواهد شد؛ جادهٔ هراز نیز به‌صورت مقطعی یک‌طرفه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/686136" target="_blank">📅 13:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686135">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEB3DcETJfUBp5pioux4Q_swgV6LsBJ7tPoTYBDABH1ivDa07eanZVl9HaOj0hIfSO_mIQ8LxT-XEvzPLQyQt4XMNqrLr4-lRT6Xco1V63u-LuOqC80X54vYFaZfARHJZbpGs9_NVDSi2Ioo9c1xtGT6kWpnPOBFtnCGOnhgr3WczWlrFgbepYaHc1WtyOwzwMX5mQtvar0N1zL1vCls6Z8AjShKKzsFpZP8QxZlMrBds8Q6yENAYbd-ufVghAIec1FoQxc_wKccT-OD_r4sBwecX_uOOgfJE4-W2fe9M_dO8HjCX9PyR5TKRSUUAD3TQe70QSvYAErfCStWjPKaPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۰ شهریور ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
امروز دلار از مرز ۲۱۲ هزار تومان گذشت، و هر گرم طلای ۱۸ عیار ۲۲ میلیون و ۲۵۴ هزار تومان معامله شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/686135" target="_blank">📅 13:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686134">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPEJf5yLcyNl9OfDCcGPOUfEbou0Bpixf9edPFKumU8OcoV_dgEVf74Azm_B60Bwcdub7zDF3sip9effMbgzIoMwcoDscLBW1uKhG4AYRx9mvkNQw7D5iwuqq2e9TVyjAL0GpNqYiCsAcCvdujG2O4wAN0y-lv21IMvg3LUuo-K0P7S3xupzgufgmMNyzWgJdTxf7lxCWB2T2LmOltCmr19eruN-OQgkRywr8loR4PH7mF-MUxOjYqrXclEai-D0kHwiPvxOK4NB0H6gzPba4a2wdjTF7bmwwbfbICrxMiX12UNVzIeLwtvkDJ3N9es1WfZ0n4mbjR673S9pBtV2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جا دستمالی دست‌ساز؛ با یک ایده ساده خلاقیتت رو به درآمد تبدیل کن
🔹
این بار در #چرخ_زندگی سراغ ساخت جا دستمالی‌های دست‌ساز رفتیم؛ محصولی کاربردی و دکوراتیو که می‌تواند با طرح‌ها و رنگ‌های متنوع تولید شود.
🔹
با مواد اولیه و ابزارهای ساده می‌توان این محصولات…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/686134" target="_blank">📅 13:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686133">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حباب سکه گرمی به ۱۸.۸ رسید؛ آبشده منفی شد
🔹
بازار سکه امروز شاهد حباب‌های سنگین در قطعات کوچک است. سکه گرمی با حباب ۱۸.۸ در صدر قرار گرفت و ربع سکه با ۱۳.۴۳ در رتبه بعدی ایستاد.
🔹
نیم‌سکه نیز حباب ۳.۷۵ دارد، در حالی که حباب سکه امامی تنها ۰.۹۰ و بهار آزادی ۰.۱۴ است. در مقابل، آبشده با حباب منفی ۱.۲۳ معامله می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/686133" target="_blank">📅 13:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686132">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازنشستگان ۸۲ هزار میلیارد تومان طلبکارند!
علی دهقان‌کیا، رئیس کانون بازنشستگان تأمین اجتماعی تهران در
#گفتگو
با خبرفوری:
🔹
در حوزه افزایش حقوق و متناسب‌سازی، دو ماه عقب‌افتادگی داریم که مجموع آن حدود ۸۲ هزار میلیارد تومان است، یعنی در هر یک از ماه‌های فروردین و اردیبهشت حدود ۴۱ هزار میلیارد تومان افزایش حقوق برای بازنشستگان پرداخت نشده است.
🔹
هر بار وعده‌ای برای پرداخت این مطالبات داده شده اما هنوز به‌طور کامل پرداخت نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/686132" target="_blank">📅 13:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686131">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیام انبوه سازمانی سروش‌پلاس
سروش‌پلاس سرویس «پیام انبوه سازمانی» را برای ارسال پیام‌های خدماتی، اطلاع‌رسانی و تبلیغاتی ارائه کرده است؛ با امکان ارسال متن، لینک، فایل و دکمه‌های تعاملی و اتصال از طریق API.
تیک آبی نیز برای افزایش اعتماد کاربران و کاهش جعل هویت در نظر گرفته شده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/686131" target="_blank">📅 13:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686130">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس بانک مرکزی: معماری آیندهٔ شبکه بانکی بر فرض وقوع حملهٔ سایبری طراحی می‌شود.
🔹
هفته هفتم لیگ برتر برای کمک به تیم ملی امید لغو شد.
🔹
رئیس سرویس فدرال همکاری نظامی-فنی روسیه: روسیه و ایران برنامه گسترده‌ای برای همکاری نظامی دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/686130" target="_blank">📅 13:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686129">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اتحادیه اروپا: آزادی دریانوردی در تنگه هرمز باید بدون هیچگونه هزینه‌ای محترم شمرده شود
مسئول سیاست خارجی اتحادیه اروپا:
🔹
ما حملات شهرک‌نشینان در کرانه باختری را محکوم می‌کنیم و به اقدام قوی و بازدارنده نیاز داریم.
🔹
پیشنهادهایی
از سوی اروپا برای توقف تجارت با شهرک‌نشینان وجود دارد، اما بدون اجماع.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/686129" target="_blank">📅 13:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686128">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kibP5ZM3q6cJAErPtEK3ovu44JpTzB4_0RoLXJFcoNdxNOoLryLQGwdrfHS5Rl0zIq7owWS3M3SR_weFM2FFzxEFpnb-FpUS_6GugWQ1fsC6VtLYHub4ROJz0NE5KO2ctNQpwZOnWu3MKtaWFSqPYfqkyK9WvUW6ug1CGkoHrs3yl1-xXNYWzvszUVxKBX7Sb7qJDc3tVWJ3NEnHn4WG37N9KYqCBYuLu0Lb5dstWBFb0NU_8Q2BSlpbXy1BmZT73R_4KnFLQgUGBAbC9R1pw47QmaugCvKhGDOpa4RHaw12GqR7vq3Nieo2ZyRoOk-J2RsMa4PI_QYEXWSMTps0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع خستگی و علائمشون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/686128" target="_blank">📅 13:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686127">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
لابی ویژه اوکراین در واشنگتن علیه ایران
!
ادعای خبرگزاری GAZE اوکراین:
🔹
ولادیسلاو ولاسیوک، نماینده تحریم‌های ریاست جمهوری اوکراین، برای مذاکرات سه روزه با هدف جلب حمایت مجلس نمایندگان آمریکا برای تحریم‌های جدید علیه روسیه و ایران، وارد واشنگتن شده است.
🔹
انتظار می‌رود ولاسیوک ده‌ها جلسه با اعضای کنگره و مقامات وزارت خزانه‌داری ایالات متحده برگزار کند، زیرا کیف به دنبال پیشبرد قانونی است که برای افزایش فشار اقتصادی بر مسکو و تهران طراحی شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/686127" target="_blank">📅 13:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686126">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF-DCw3_pBB2ANR9nTq6xql-kuvHRDscuVipbp5IvJnXUzCDIPyUYITHZJsAmb5bMu4z9V3145LwmIBi56V60h3RcQ_gNBiaPSfxtOercPOpTZeDD5xESEzDdJ3cQz7bnb38Qn8I4MmGjOiVuZFSWiebS5ol-EMqR7oNJu5TdPgx9_5B3D9JMwfNan8TxdNIsNiL_LW4xIHBelWFwQczH4tEEFp8-fcV1UFvSr9DVaZLCyuu974usyfXbqGeya4t9NFzMNF4R2v2CtortybGx-6rhQPlexeT8hGL83KnsWznrxH3BPKaQ2Ra_QY5X6ZP4j1fWuq05lnIeZ7QiW51qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤝
🙏
گام بلند بانک تجارت در حمایت از کار و تولید با مشارکت در طرح ملی همگام و معرفی محصول ستام تامین
🔵
این طرح ملی که در قالب تفاهم‌نامه همکاری مشترک میان بانک تجارت و سازمان تأمین اجتماعی و با حضور وزیر تعاون، کار و رفاه اجتماعی به امضا رسید، به‌دنبال مدیریت هوشمند تعهدات مالی کارفرمایان و رونق‌بخشی به صنایع است.
🌐
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/686126" target="_blank">📅 13:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686125">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
عارف: اهل جنگ نیستیم، اما خوب می‌جنگیم
معاون اول رئیس‌جمهور:
🔹
اگر این کشورها و این شیخ‌نشین‌ها به مردم خودشان برگردند، مطمئن هستیم که منطقه آرام خواهد بود.
🔹
مسئله اصلی تنگه هرمز، تأمین رفاه برای مردم منطقه است، نه برخورد و حذف؛ کشورهای منطقه خودشان می‌دانند چه کار باید بکنند.
🔹
اهل جنگ نیستیم، اما خوب می‌جنگیم؛ برای منافع ملی‌مان و منافع کشورمان به هیچ وجه کوتاه نمی‌آییم و اهل گفت‌وگو هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/686125" target="_blank">📅 12:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686124">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیش‌بینی‌های تولید گندم محقق نشد / دولت باید ۴ میلیون تن گندم وارد کند
ناصر مرادی، عضو کمیسیون کشاورزی اتاق ایران در
#گفتگو
با خبرفوری:
🔹
امسال پیش‌بینی می‌شد تولید گندم کشور به حدود ۱۲ میلیون تن برسد اما تاکنون فقط حدود ۸.۳ میلیون تن گندم تحویل سیلوها شده است.
🔹
با این میزان تولید کشور برای تأمین نیاز آرد، نان و مصارف صنعتی به حدود ۴ تا ۵ میلیون تن واردات گندم نیاز خواهد داشت.
🔹
قیمت خرید تضمینی گندم امسال ۴۹ هزار و ۵۰۰ تومان تعیین شد در حالی که کشاورزان معتقد بودند قیمت منصفانه حدود ۶۰ هزار تومان است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/686124" target="_blank">📅 12:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686123">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر خارجه پاکستان: اجرای یادداشت تفاهم منعقد شده بین واشنگتن و تهران همچنان تنها راه پیش رو است.
🔹
وزیر علوم: تحریم آزمون تافل برای ایرانیان رفتار «عصر حجری» است.
🔹
جاده چالوس و آزادراه تهران-شمال امروز از ساعت ۱۲ یک‌طرفه شد.
🔹
شاخص کل بورس با افزایش ۳۶ هزار و ۱۱ واحد در سطح ۶ میلیون و ۵۸۳ واحدی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/686123" target="_blank">📅 12:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686122">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تکلیف سوابق تحصیلی کنکور ۱۴۰۵ مشخص شد
🔹
پایه یازدهم: تأثیر مثبت
🔹
پایه دوازدهم: تأثیر قطعی
🔹
سهم سوابق تحصیلی: ۶۰ درصد در رشته‌های پرمتقاضی
‌
🔹
این مصوبه از سوی رئیس‌جمهور برای اجرا ابلاغ شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/686122" target="_blank">📅 12:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686121">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVslmvc2WhfZYhdYTIhFB1FfyFREW6lnQIglo84xk4SwwDSi_jzBJG0IH1uebBIXzSJfumpNd1OuLTSDwTM3NPnp15DMB2ftYOn3z0emkwLr1M8qIaw8-mS3d7JrBL068QaXKh_UaM9WLU6Y5TYzmRkTVLaa-MXjpWl12Byzp6w5NgDvUD-K3o_l6rymuXoouL9p8htafaGrf22GNufYbefFoGTXe6xByE9gr_9pVqHTVazJ5ntaviW7sqEP-k9ZtZ2XxYIbwjdU-GRakZvQi4MNKDitMfUBo4XgIcGHGHACdoiECMgl62rweb6m8mss2vLifmvY5iBuR-e6Zo4vKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلگرام سرور را حذف کرد/ اجرای رایگان بات‌ها بدون خرید VPS!
🔹
تلگرام از قابلیت جدید Serverless رونمایی کرد. قابلیتی که می‌تواند دردسر خرید، مدیریت و نگهداری سرور برای توسعه‌دهندگان بات‌ها را به پایان برساند.
🔹
در این مدل، تلگرام اجرای کد بات را در محیطی ایزوله برعهده می‌گیرد و منابع را متناسب با میزان ترافیک به‌صورت خودکار مدیریت می‌کند.
🔹
بات‌ها همچنان می‌توانند از قابلیت‌های مختلف تلگرام استفاده کنند، به SQLite متصل شوند و درخواست‌های HTTP ارسال کنند؛ با این تفاوت که دیگر خبری از مدیریت سرور نیست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/686121" target="_blank">📅 12:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686120">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c879625ad8.mp4?token=sODoFgCjf1AH8_D4AiCMYknYo-q_tK0CM1tLZaj6dYXixj7-A_o6WHZ0GRc4S7O032LUN9wtKaF0pTmwyDChu9viI5mVu8j8hoR8GVyCT88-u3QWFt-YXulGyHPSAVs13XCzsVFrFPJ4fiL-P3lGzO6NmteiOv-wFZD60zXvNl1Xun9Ye64Cx8VQzhINSNnadYFMALEFrV4CKu7WulvooemXMwtPQxFi1GgfGUXK2H8ajaZMwTwo_ra8qQejeKNUisuuDD0z2z_CG-ntpHd709MByQWpS0al_rBt4pXhs-LmKJDNBSnF3xi7EbgW7m3KxzOHyrKQ3b15mRolFy2pFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c879625ad8.mp4?token=sODoFgCjf1AH8_D4AiCMYknYo-q_tK0CM1tLZaj6dYXixj7-A_o6WHZ0GRc4S7O032LUN9wtKaF0pTmwyDChu9viI5mVu8j8hoR8GVyCT88-u3QWFt-YXulGyHPSAVs13XCzsVFrFPJ4fiL-P3lGzO6NmteiOv-wFZD60zXvNl1Xun9Ye64Cx8VQzhINSNnadYFMALEFrV4CKu7WulvooemXMwtPQxFi1GgfGUXK2H8ajaZMwTwo_ra8qQejeKNUisuuDD0z2z_CG-ntpHd709MByQWpS0al_rBt4pXhs-LmKJDNBSnF3xi7EbgW7m3KxzOHyrKQ3b15mRolFy2pFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از نظر علمی چرا نباید خانم‌ها استرس مالی رو‌ به دوش بکشن؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/686120" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686119">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📷
عکس یادگاری سران کشورهای عضو سازمان همکاری شانگهای
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/686119" target="_blank">📅 12:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686118">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
کرونا دوباره فعال شد؟ وزارت بهداشت پاسخ داد
وزارت بهداشت:
🔹
افزایش فعالیت برخی ویروس‌های تنفسی ازجمله کووید۱۹ در کشور مشاهده شده، اما نشانه‌ای از وضعیت بحرانی یا ویروس جدید وجود ندارد.
🔹
مردم تهویه فضاهای بسته، شست‌وشوی دست‌ها و رعایت احتیاط هنگام علائم تنفسی را جدی بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/686118" target="_blank">📅 12:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686117">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c029cf629.mp4?token=oQ3MjvhvniGWQXTUvnKDRESYwhlstKuEGeNbD7BBLUjKEPU9QqV4yV4IMb1nGm3uBmf5eczhD9b5vJhYKZ31DXiOQtlgsA4pvM1rKMt-Tfbaf5PLQKI_JZCYymP-EEIqubfl9esixeAuN_CqFidq5cvszHlt2lfUK-R6HIWVFnO3sX0EWZVVEVjrXgaHKMK4RmIVid0cPXAuzV1wstodVNq7cOs8cBlT1xy2UmZ_EW-tkr_e_zBerSM4P14OaN6tsk43METMyPpfaZYBeSt9Y8DH8m9-YaZUUjcdNLa7IkBjItfxEaETs49iahJopIlj7yVSPMg7ipE59huWD5iPkrtRMRtq_tguJO160iteUkvo2AY1-H7Ooq3JdwPhCiaTLiT7jRu-9ncEvX0KyH0y9d6xghvLIlMArENWdgaLhebStE08pP6pSSNxZu55Rl_PcM72XdbrjzDiBsRZ7EN5ZHwKtcZAz1S3e6NmsguKohNpYOJV4QI6J8uk1m6RYvel2mTdt2VdbOPu8MEiRMhsi0b2O9LynKAQ0wiY5qhG9OAumo9vPWFpXIb2Drh0yN8VkmUgIRvNrP5BTX4m5mJW_xChy3kmQkkdSAKq9cb6PIR7jOq-FycBJe3joxG3QRpJgcp1yHFBGHvHT06flsMsNVSZ7Ho5PIR-zX158DPvPuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c029cf629.mp4?token=oQ3MjvhvniGWQXTUvnKDRESYwhlstKuEGeNbD7BBLUjKEPU9QqV4yV4IMb1nGm3uBmf5eczhD9b5vJhYKZ31DXiOQtlgsA4pvM1rKMt-Tfbaf5PLQKI_JZCYymP-EEIqubfl9esixeAuN_CqFidq5cvszHlt2lfUK-R6HIWVFnO3sX0EWZVVEVjrXgaHKMK4RmIVid0cPXAuzV1wstodVNq7cOs8cBlT1xy2UmZ_EW-tkr_e_zBerSM4P14OaN6tsk43METMyPpfaZYBeSt9Y8DH8m9-YaZUUjcdNLa7IkBjItfxEaETs49iahJopIlj7yVSPMg7ipE59huWD5iPkrtRMRtq_tguJO160iteUkvo2AY1-H7Ooq3JdwPhCiaTLiT7jRu-9ncEvX0KyH0y9d6xghvLIlMArENWdgaLhebStE08pP6pSSNxZu55Rl_PcM72XdbrjzDiBsRZ7EN5ZHwKtcZAz1S3e6NmsguKohNpYOJV4QI6J8uk1m6RYvel2mTdt2VdbOPu8MEiRMhsi0b2O9LynKAQ0wiY5qhG9OAumo9vPWFpXIb2Drh0yN8VkmUgIRvNrP5BTX4m5mJW_xChy3kmQkkdSAKq9cb6PIR7jOq-FycBJe3joxG3QRpJgcp1yHFBGHvHT06flsMsNVSZ7Ho5PIR-zX158DPvPuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قمار دریایی آمریکا برای نفتکش‌های ایران
🔹
زمزمه‌هایی در آمریکا به راه افتاده که آنها برای نفتکش‌های ایرانی نقشه کشیده‌اند!
🔹
اما این نقشه آنها تا چه حد عملیاتی‌ست و چه عواقبی برای آنان خواهد داشت؟
🔹
ماجرا را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/686117" target="_blank">📅 12:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686116">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f2bedb73.mp4?token=RnmdFaknqRjVFhYO89Lbhzpa6VOO4LQTNRIT9zTYuIvzv_VfuDFQaNkNo0xBlbrPbTC9QouLoevyh3hS-wPKiHtYLlPhUFlsxa1KplsXwBzbjkvP_chqY-dWrhQVvOhqhp1g5agmvZ5IRQh5ODtW-5oOkGLLtaSTqGD7O2TlJmdTrZjGUoccpQSxtW4BgErb2y0uDTwYFGLK4rWK30WcUTqBrRQQyuwKnk69ZmCS2PQlRWFotoNwE1X7p_5NL6fbKDuDTZDtiwDgLfusXMUR43nUhd6XURn9PPyc0n5RBJYS8O6lfd0876zhAHrcVRNCxK89JGEr48sdKpVbOPGj1E3GYkjh3G3DADHtceWwb2XAhpfuABxKIPru-ZhBjohQ_G6FJj4iv31hlnc24Lub4kzQkSaUmLrRYG_YsfUySych2l095zeP6fnaM4ylmxdMMerImVrxQfEfMIWavzzpVBk14px8hDRfC-m1FWI8ARVcCIvuaSYL_cqsk2Vdq60unX633lAYTduPU9b29_yYemURjammVbVcx4c--vm5nqAgfZVq2yyjwx4YNOONCoBV9Dzt3FnOrO1rfgE8N89m6kT55v7h05Df9bVvdO9qAa4mh_CsR6eND6N9Dpdx0Gb2RuuekKwE_C3KaENxDbO9bNdcL42E2pKuPrBn4ObOViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f2bedb73.mp4?token=RnmdFaknqRjVFhYO89Lbhzpa6VOO4LQTNRIT9zTYuIvzv_VfuDFQaNkNo0xBlbrPbTC9QouLoevyh3hS-wPKiHtYLlPhUFlsxa1KplsXwBzbjkvP_chqY-dWrhQVvOhqhp1g5agmvZ5IRQh5ODtW-5oOkGLLtaSTqGD7O2TlJmdTrZjGUoccpQSxtW4BgErb2y0uDTwYFGLK4rWK30WcUTqBrRQQyuwKnk69ZmCS2PQlRWFotoNwE1X7p_5NL6fbKDuDTZDtiwDgLfusXMUR43nUhd6XURn9PPyc0n5RBJYS8O6lfd0876zhAHrcVRNCxK89JGEr48sdKpVbOPGj1E3GYkjh3G3DADHtceWwb2XAhpfuABxKIPru-ZhBjohQ_G6FJj4iv31hlnc24Lub4kzQkSaUmLrRYG_YsfUySych2l095zeP6fnaM4ylmxdMMerImVrxQfEfMIWavzzpVBk14px8hDRfC-m1FWI8ARVcCIvuaSYL_cqsk2Vdq60unX633lAYTduPU9b29_yYemURjammVbVcx4c--vm5nqAgfZVq2yyjwx4YNOONCoBV9Dzt3FnOrO1rfgE8N89m6kT55v7h05Df9bVvdO9qAa4mh_CsR6eND6N9Dpdx0Gb2RuuekKwE_C3KaENxDbO9bNdcL42E2pKuPrBn4ObOViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بات از تو، ۲۰ میلیون کاربر از سروش‌پلاس
سرویس توسعه بات سروش‌پلاس راه‌اندازی شد؛ فرصتی برای ساخت بات‌های کاربردی در حوزه‌های مختلف از خدمات و پشتیبانی تا اطلاع‌رسانی و سرگرمی.
با ابزارهای توسعه بات سروش‌پلاس، بات خودت را بساز و به بازار ۲۰ میلیونی کاربران فعال سروش‌پلاس دسترسی پیدا کن.
🔗
مشاهده مستندات و شروع توسعه:
https://soroushplus.com/p/documents</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/686116" target="_blank">📅 12:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686115">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBank Pasargad</strong></div>
<div class="tg-text">☀️
جشنواره حساب‌های قرض‌الحسنه پس‌انداز بانک پاسارگاد
🎁
جوایز جشنواره:
۲۰۰ جایزه ۲،۵۰۰،۰۰۰،۰۰۰ ریالی
و میلیاردها ریال جوایز نقدی دیگر
⏳
مهلت شرکت در جشنواره:
پایان شهریورماه ۱۴۰۵
📅
زمان قرعه‌کشی:
مهرماه ۱۴۰۵
📌
صفحهٔ ویژهٔ جشنواره:
bpi.ir/qh1405
🌻
سهمی ماندگار برای مهربانی
🟨
کانال رسمی بانک پاسارگاد:
@Bankpasargadtelegram</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/686115" target="_blank">📅 12:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686107">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFaDnRfVnmObt6UJrnc8cMmQ7XZl2wroPuDDf8O5j-lTcpFVpEfMcXBklFCXUK8wVK0pS4E5mksLr-pMBMa71S-9DO248GVQnde8Fc0bgRH8AoaAtSaRiQRBQHXKjtFLDgg5mTMDNh3A0lTfJoPyszX8vS4bx7WLd7hwCVh7XVkTVZzlmRtsOdcA4Ag0VOCoIun9_CWps84KLkW5PI5n7fuo7rJ0BQxLEQAv1YGl-ob5V8xJ5G_KpQDgVkDwSKs5aRoqwxdFTA7VNpBsZ_YTbu7Qpx8Eu0SeTEQ7Ca0vNfDYbkID8BrqCOIozg1L3DIVTDTPVmzilnj098Y3caX46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzxPzq-fRtx1j9Xo2-9Lw7zKbUY8SMfGsxq-iUb8h63JrBArD59x1kqK9Ocfukqt-blRaFNTFFuUjDh3Z8ixEPI31yDDuDFHrexLEeefoC1ILFCGzPl5mbR5ISXohD8JVc_bN4QBxiIdV1DPXS7Xh-CR6lITAOTIYJld3sOa6aCsQpcHB3MgtoisU-x_pZttANfJF7ZS88dI7TMAgEh45bztX6gOEisRGhQI6nRuzTrV79juFejZzxV1RwBkQ4qTSfqdyYMdqMRJjl8_0IhZxlWjsDgULIgqUk2Z2fC2QSjle2DmdoL8mD98YbN7J9hw5eOO7TaEz6bwDY4e6YmzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rwvnv0ACucOMMk4710zqPSOr233SDg7omu5TgarRKRJ--Pes1yPA2DUadWEtED16rzxsDNxtK5NrGI98zmoaCPqckhG1_SxeGr-WhfIj7Pd8SPp76FvaP7scifCIllHockR_AqR4CUl8PXieHnFcEdtla3KRt7rwT4jQrF32Is8RRxJm3Pqp5NDaQ52PRUx2KuLFSRznPxoQhrG-2l1L2NcwiQ46usnIQT0RKIDFyKdMbT748bFGv-ypRKA4_tB-HcmySWH1RGhgiNdpcgShP55ybzREMpr9ZECpa1dH5_-159ZCvnMoa24kctggFXZEYvg6MvKWeFMjOff812I76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwZoMHW0sZqTrHT7lWVTcZ7wxojitIwcLbZU9xmsXICoE0vbJ6VOeFQWcNZ6VI6htb9IM54LET2qJjRDDJOkxnhprhyDk8WJzbOwkp-PZIpKmXH6vudVhtKlbWYuuFxwRI0gmQpwzRbvTQsVjvSSevr15eL5DpJ-jdSoJ2fGBSTuSmgSQfw7vs0MHQJd91WgNQHPFSkXNQ4vntCBrc20QtevDmhUNFKbVzzF8Uxx8AISpm3AMoJDDNXuCsUf--rTL7QyM11XF6C8e4gh2qH-NFWsVwktZkPiq3RiOUGHhYMjsvfGD5postqQtMV6wcwZ_QDkJ10nXzyrOzuu2YPRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLSvxnULJY3ODRwY1dOVpqUBN4txkghTH4ODzEx2Rx3yXgzGH5F9BUeA9wuE9g-wp15ok-z2n04eOlILuhhxfMo49i5nyiZrHdYVUpsxwcoDnHoqZS6Li-TLEma5SDGxnhkZ6id7RVJxTKG12wevpyPbGX3y1ax_WX99YwD7R0-bDgUYCQqcDkLSffoLVib_fVNapz9zB0_16G9kzjFjhIvQoEHve_VycAqhtrbCFiHumnorKhnL1SOWRDhvowQqbD3mRGACG_HB1AyWzMXeyIyhsYhgff59eHo-RycIsuEBk93xm6zQZHA4HdGmbpiAV5ecKjOj7LeDnli4yiRi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGFgdrOxHQOSvD3T6fKzMnx2ADrO7qzeNLhV3O3ZmZOLEmsfGK6elNK_o9xF-FgfYYEtEPyXC_cCquAlwDWRl9fOTIES9ZUmOp_gt6bKv_5ofSpEuOeMZ-u7t4SHs823J57duuxYLodZ3iA8R9j-HOMOB4-y10T5sfePjsmjZuuY_zmzfw_rQ5qh-zAljzAUcj3UDpuFCfOLLSbauJqMmIQo6Rg4PmTZzIMNvRLXy4dzpqGpYFOy_foG776Cn2Jo53YhPZ8ZkYKiluam_0RmB-ZrPuBro70e19Fq0_9bNXs1Dqa7HJ0lXSKMa-zle4z5f7VM-Tf7FcjI9cdAiv9uRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdFRipguV-ng0_w8cDH5Vj_I8exB3twiIRaf-u7IfRM_swER8hxLV2v3KL92dfRrSiYF0LtsOweN0iDr6MtBa6FJ63YO3xIrwXb7J0DWUbmTrJFmkYktLbn2LPwMoMZNNP9JvHaR7wnFzGzW5WV6HxhXVJt61o5niPKiPSrdlPxIqTMENgatS8qALOUrhMf5nESPSOIN4_BIpKwi5QKwBzyr81XDP5li_GWiAvBQ_mHKGj7m1Joz_cmjRMNY93PC7vsTRiMIhmUR9ZOx8-mED1_a6WtxiZ7G5Od_Iamj-hiVLa73bdAzj_U8bISHIPDriwkWEME2Ar8E6_iqyMyoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_rLlTl-Y0vWQJxMZ9j3TkOBOTWG8JsM-El5PIZQ4ggHWIZJn2fo14tCIbNSAx_n3Hvw9TQCfqF0AxLCX3E5Al4RLpwvcL_FglvfKS_njH61v4ze60kaOLkl2j_CjXzfx-IJPiaE7YxUK3LKCAnTz_2pK6mYF58e48BKsRb3sqNLYi_76ieiS5rvI2hDudAMH1g-To4tIhc4fYcZwoiO5A2yuYxLZv2frsBrrrqGdXq5hnRWnmCRHYPccDee6EPBibpnnUETrIwOCXxOc3tdXY0VHvrLEyBa5eYgANnlN6y2I5nwEMwtSUF8YwwpM0f_ahxZn1hIpPjp0U8oL-lJkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دومین روز الکامپ ۲۹ از قاب خبرفوری
🔹
روز دوم نمایشگاه الکامپ آغاز شد و خبرفوری در سالن ۶، غرفه ۳۲، همچنان میزبان شما عزیزان است.
🔹
تصاویری از حال‌وهوای روز دوم الکامپ و حضور بازدیدکنندگان در غرفه خبرفوری؛ منتظر دیدار شما هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/686107" target="_blank">📅 11:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686106">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyA-sD1C2TyhxUzPz51R4ipLPLNf4k1heVkghzTaPIXi6LCRy923eWMAxB_2D9ZkPhIU4jnKC4ldD0JpkKGG5LuX-X9JRt958ZM9zyfXPTym9uSe_bnjnfQravU7zD1-qbcPEOvfaZRMoSbQypTrYKgFXWZuJ7VJZ_6fqhlmaTxJUSDt8aXY5BNdaoi2lBcZiQwh0mr9hzscFP1BYRZKzVrA53aVapvb79iPsVo3vAFps0MJPRr6A9S15fE3pdXD7euzF6VUzi_b2Nq2xIFZQCNYfz_yUhUsNk7A4eub9Pk8i2l57D_FUJh5HdRhQ9rJEC9FsZ9qn1TTRD1yWU7CkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست: انبارهای مهمات حیاتی آمریکا رو به اتمام است/ نیروها تحت فشار قرار گرفته‌اند
واشنگتن‌پست:
🔹
دولت آمریکا به طور سیستماتیک تلاش کرده تا هزینه‌های واقعی جنگ انتخابی ترامپ، از جمله تأثیر آن بر آمادگی نظامی، را از مردم آمریکا پنهان کند.
ژنرال‌های آمریکایی به وضوح دلایل خوبی برای نگرانی از بابت کمبود منابع دارند.
🔹
نیروها بیش از حد تحت فشار قرار گرفته‌اند و این موضوع بر روحیه آن‌ها تأثیر گذاشته است.
🔹
انبارهای مهمات حیاتی رو به اتمام است. حدود یک‌چهارم از پهپادهای ریپر (Reaper) پنتاگون به کار گرفته شده‌اند.
🔹
تنها ناو هواپیمابر آمریکایی در اقیانوس آرام اوایل این ماه به خاورمیانه منتقل شد. متحدان نیز دچار نگرانی شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/686106" target="_blank">📅 11:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686105">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRcvxGgXFr7w-Ws4xDmjIQtQ3BrfDq107WZgB3oz-eX4ZAxxj2h8qaws8bx3vp_R31oVguecK_gSw6Xl2bYNLyBAmdQfkiWdb6vs7v_vxadhxvwBuZoU5XkE_-O4739p7Ym1YIaifMXeGGJSuQw0isXtW-9e14L1kEtf9yD2qsOyq21wimeoiGTJUu51q3lEf78Gng2jjrcG32UFTvinadmH7UF3CooHXbNvyVvh9EhEWV4ogr39VltydKzizogZTV7BgO2cPatrKcMLXR27zdJjowbHknq2Dvf4n8p7WgVz5wgalTTxatbuerGffzl14IuBNiMkqhurNcaa30RMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌وگوی کوتاه رؤسای‌جمهور ایران و چین در حاشیۀ اجلاس شانگهای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/686105" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686104">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isPSVDMnF938w7E2vCj8OB1hQAFnm0luQVSizW6UAOt7xkm4WfeP21i218WGfgxkYas1VGKQq4KgKSlgEf-tXryX_xuuFi983G0NEgnbjik1EGsbM-WY9eWq6leBTn56y1TGlAhXFEeUe7HxzWg43dmMzrM1a69g7J3k842xg6uO2wyDjAhe6lxNaFw1RWZ8P83_QQd9HGSFuCBCG4skUiN8JkLM-1O0nnX0kTYKvXt0YHbpb8TQqt3WquWNOVvm_rX-ZdGqFe-oE5zbgw_vH5wunz6_x5NFlwBYgIKuauycXEABJXpgolJpoWKDLc80iv9FIHkTPDop9VVCW0cdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایتی از قتل هانا راکان دختر ۱۶ ساله کرمانشاهی که قربانی خشم پدر شد
🔹
هانا راکان، دختر ۱۶ ساله‌ کرمانشاهی در مسکن مهر دولت آباد کرمانشاه بر اثر اصابت گلوله به سر جان باخت.
🔹
مادر هانا مدعی شده است که همسرش را در حالی مشاهده کرده که به صورت سراسیمه از پله‌ها به سمت طبقه دوم ساختمان می‌رفته و یک قبضه سلاح کمری با رنگ مشکی در دست داشته است.
🔹
فرد مورد ظن در این پرونده تاکنون دستگیر نشده و متواری است./رکنا
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686104" target="_blank">📅 11:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686103">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1thNXNNTo1HWUWbR0_0m3iYqcjC-DgHs9BJcdQp5ErUUgEw-3iNRs2zJnWCzQdC1-ym-vfseiizSOVo-8yzPzBUCCy8NPjX_SIkyRZvrBdzVHvZi3rZgMHFg_51UhYEDO-wGBcAo4YCn-9fw9v2sGVggUk7CxWQgK0e6Mkip1WllB1KqyMdkvvqj2HSUeCqYHiwT4nu1hvBfz0rmXi8rYb7OAhNDcFtKvdlDfGzVJit9bdK5CVRdUDxpjJ8_ayh7-BRbTdkb3E5M756Gb4ycUj4TCtrfwg4ecgwCZXxlAIEvGaiaBqrV7UINt_22M14RegOL38XzFbUddM32Px00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری در آستانه بازی استقلال و پرسپولیس
🔹
همراهان گرامی خبرفوری؛ برای حضور در این پویش کافی‌ست یک پیام صوتی ۱۵ ثانیه‌ای ارسال کرده و پیش‌بینی خود را درباره دیدار حساس پرسپولیس و استقلال با ما به اشتراک بگذارید.
🔸
برنده مسابقه کدام تیم خواهد بود؟ پرسپولیس، استقلال یا تساوی؟
🔸
نتیجه دقیق بازی چند چند می‌شود؟
🔸
گلزنان احتمالی این دیدار را حدس بزنید.
🔸
لطفاً در ابتدای پیام صوتی، نام و شهر خود را اعلام کنید.
🔸
پیام صوتی خود را به آیدی زیر ارسال کنید
👇
#دربی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/686103" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686102">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
رویترز: نفت بالای ۹۱ دلار رفت؛ نگرانی از تورم دوباره بالا گرفت
🔹
با تشدید درگیری‌های ایران و آمریکا، قیمت نفت برنت از ۹۱ دلار عبور کرد و بازده اوراق قرضه در آمریکا، اروپا و ژاپن به سطوح چندساله رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/686102" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686101">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سخنگوی دولت: هیئت دولت طرح دورکاری برخی ادارات در فصل زمستان را بررسی می‌کند
🔹
سازمان اداری و استخدامی موظف شده برنامه این طرح را آماده کند تا پس از تصویب در دولت، جزئیات آن به‌طور کامل اطلاع‌رسانی شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/686101" target="_blank">📅 11:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686100">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کمیسیون آموزش:مدارس مجازی شود، هفته آخر شهریور اعلام می‌کنیم
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
در حال حاضر از سراسر کشور دانش‌آموزان درخواست مثبت شدن تاثیر معدل پایه یازدهم را دارند، به‌علت اینکه این دانش آموزان تحصیل خود را در ایام جنگ سپری کردند احتمال مثبت شدن تاثیر معدل یازدهم برای سال جدید وجود دارد.
🔹
مجازی یا حضوری برگزار شدن کلاس‌ها به دامنه و میزان جنگ بستگی دارد، اگر بنا باشد کلاس‌ها به‌صورت غیرحضوری و مجازی برگزار شود هفته آخر شهریور اعلام می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/686100" target="_blank">📅 11:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686099">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpDjwRsMILEF4x7cui-ZQy2cjkJSseGZiv2fLIK9YGrxTJcwROJlpKbBfItYZ5DNaDmykMOAk6h6L1vAX97ngVL0K6kEgBibUiW-KJPZMjUYZNVh6t7o_0r-mIPeV9dCU35vuxO9wo41u2oApBB3cHCLKDv8hKyof74_deQIGg7QeaMb5Etu6K24Qeu9rokh7POl-JfJ3DGNhyb0eEIEYT9Vnw0SdGhWQbADpMOL_PtyKYY9o_9zVmRhvSEhyQ8IDH5GLqdaYipTQwTiQaRvTPXO9yrNee8DZcqIC5L-yzP4110ggdYb5RSEnA2MI4TrMDI3i79JCIk9Ma8rRCLUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس از حمله آمریکا به لامرد پرده برداشت؛ ۲۱ غیرنظامی از جمله ۷ کودک کشته شدند
آسوشیتدپرس⁠:
🔹
بررسی «ایروارز» نشان می‌دهد سه موشک PrSM در حمله به لامرد، با پراکنده‌کردن ده‌ها هزار گلوله فلزی تنگستن در شعاع وسیع، غیرنظامیان را تا شعاع ۵۰ متری محل انفجار کشتند؛ دست‌کم ۲۱ غیرنظامی، از جمله ۷ کودک، جان باختند؛ ارتش آمریکا استفاده از این موشک‌ها در ایران را تأیید کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/686099" target="_blank">📅 11:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686098">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
مهاجرانی: منکر فشار اقتصادی به مردم نیستیم. افزایش قیمت دلار ناشی از فشارها و تحریم‌های ظالمانۀ آمریکاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686098" target="_blank">📅 11:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686097">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
خبرها از هدف قرار گرفتن یک کشتی دیگر در تنگه هرمز حکایت می‌کند
🔹
گزارشها نشان می دهد که یک نفتکش در نزدیکی سواحل عمان با شلیک سه موشک هدف قرار گرفته است.
🔹
منابع عربی مدعی شدند نفتکش مورد حمله، متعلق به عربستان سعودی است.
🌍
تازه‌ترین خبرهای ایران و جهان…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/686097" target="_blank">📅 11:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686096">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80a57d36c.mp4?token=u0Q80TCPGTRZc-GpXR51CbYIXF_RKv_KOz3KVq0hvWsfSpTC0qtb0bfkcE78jYx5WeH_u0v_8nd7p-4MfiBFxw657pUVDla-L4nQ5dVIQuHOmIvPLPUUykdZNX8lNnP9YFsqASi76WuWaiLfhNAeKm6LC0wml-dY55jchr9tD1U6xfdv3X0l0K3EpCpo2M8E0USY7AG1BzDbsiTjqmLI2gMdqZ1xKcrjszzrtUkFGmNP83mWq3b7GyGDziokvLrpnW0eM4QgTAhy1_dS9NoHvwFpfFv2ws6MKunr9QgvFxY9xyEVa8zVijcOG86WCe3eXK53-DOIEG7xIFYrWUF83U2FFmdS4QHNx-4dp8YOrLf_bQcJk6i6z6DVhFZLn1PUZfhepw7KIzpCJpbBY6fpncWgMrLGEETHIMpwvs5NlpPnhjHUw5ooITPGfOHmwmaCK10WwMwFr-28h7Ojx2uTizJPNUslNF2TTJPRhyMjszhsMhkiK40p3BMvsXyFccjMKb5TszNuHv4rMF4YjvIW1E57fkgQxcdf3wi3iiEeZ3-Yp8_jMaxsgvYg-BiK2Dy8kHGKY4YGt1c5KGRPcvqQ9zzVo4JZSbJFQS7sCjhHSRUoO4Yma-Zvoj04xmLVrk7jdhitiblcqb78LWIPITiKz6pRAFp13K5L0vqy42T2NDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80a57d36c.mp4?token=u0Q80TCPGTRZc-GpXR51CbYIXF_RKv_KOz3KVq0hvWsfSpTC0qtb0bfkcE78jYx5WeH_u0v_8nd7p-4MfiBFxw657pUVDla-L4nQ5dVIQuHOmIvPLPUUykdZNX8lNnP9YFsqASi76WuWaiLfhNAeKm6LC0wml-dY55jchr9tD1U6xfdv3X0l0K3EpCpo2M8E0USY7AG1BzDbsiTjqmLI2gMdqZ1xKcrjszzrtUkFGmNP83mWq3b7GyGDziokvLrpnW0eM4QgTAhy1_dS9NoHvwFpfFv2ws6MKunr9QgvFxY9xyEVa8zVijcOG86WCe3eXK53-DOIEG7xIFYrWUF83U2FFmdS4QHNx-4dp8YOrLf_bQcJk6i6z6DVhFZLn1PUZfhepw7KIzpCJpbBY6fpncWgMrLGEETHIMpwvs5NlpPnhjHUw5ooITPGfOHmwmaCK10WwMwFr-28h7Ojx2uTizJPNUslNF2TTJPRhyMjszhsMhkiK40p3BMvsXyFccjMKb5TszNuHv4rMF4YjvIW1E57fkgQxcdf3wi3iiEeZ3-Yp8_jMaxsgvYg-BiK2Dy8kHGKY4YGt1c5KGRPcvqQ9zzVo4JZSbJFQS7sCjhHSRUoO4Yma-Zvoj04xmLVrk7jdhitiblcqb78LWIPITiKz6pRAFp13K5L0vqy42T2NDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«ایران‌بوم» در الکامپ ۲۹ رونمایی شد؛ دولت پلتفرمی در مسیر تحول دیجیتال
پاویون دولت هوشمند با حضور وزرای ارتباطات ایران و عراق افتتاح شد؛ جایی که «ایران‌بوم»، برنامه ملی زیست‌بوم‌های دیجیتال دولت به همت سازمان فناوری اطلاعات ایران، برای نخستین‌بار با هدف معرفی تصویری و تعاملی خدمات این حوزه در الکامپ ۲۹ به نمایش درآمد
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/686096" target="_blank">📅 11:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686095">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رانت بازار خودرو ۵۵۰ همت شد!
🔹
بازار خودرو در سال ۱۴۰۴ به یک غول ۲۳۵۰ همتی تبدیل شده است.
🔹
پشت این عدد بزرگ، یک شکاف ۵۵۰ همتی میان قیمت کارخانه و بازار آزاد پنهان است.
🔹
ارزش خودروهای سواری نو در قیمت‌های کارخانه حدود ۱۸۰۰ همت برآورد شده در حالی که رقمی که در بازار آزاد به بیش از ۲۳۵۰ همت رسید؛ بازار خودرو در ایران معادل حدود ۱۴ میلیارد دلار است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/686095" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686094">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102dacb925.mp4?token=OdPiPEOoSJotPpU6e63qk91KMFuh_yp-NX_5g9s-QXeyUJjkHn_uSXsB_lrUv1H3E3eAFAmvzDkd5myCnb158OEHCxJZBNtcuhEn0NetqP8nJBACP8s5ucPnETmrwEo6CfIdQyWhkek69iHQR4p-EqiYoMyvoYhfck8dpAdjMbMqreva27cj7bjpULkwG9LgKuhe0FoXqNcFMecGGQyrzBuFeTm2lbkimoHRETHK6BcJxqP8rWOza3yXhup1W2pSst__GZ500QDI6D9u2m8SzfCd83XhfuHsCGxa5nEqoL6KcJC98Nfq7q6H_Vrp8NQ66gZz69b-1NmIQ496D_Tvhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102dacb925.mp4?token=OdPiPEOoSJotPpU6e63qk91KMFuh_yp-NX_5g9s-QXeyUJjkHn_uSXsB_lrUv1H3E3eAFAmvzDkd5myCnb158OEHCxJZBNtcuhEn0NetqP8nJBACP8s5ucPnETmrwEo6CfIdQyWhkek69iHQR4p-EqiYoMyvoYhfck8dpAdjMbMqreva27cj7bjpULkwG9LgKuhe0FoXqNcFMecGGQyrzBuFeTm2lbkimoHRETHK6BcJxqP8rWOza3yXhup1W2pSst__GZ500QDI6D9u2m8SzfCd83XhfuHsCGxa5nEqoL6KcJC98Nfq7q6H_Vrp8NQ66gZz69b-1NmIQ496D_Tvhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: غیرحضوری شدن مدارس امسال شایعه است؛ برنامه دولت به حضوری بودن مدارس است مگر اینکه اتفاقی بیافتد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/686094" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686093">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARSOsnl2zlNbIOZplG-wbdomILSlNeEnv9xkKYzw4UhAzXb3E63wmCUfjIEuouhoxxQjqhWolhbprBTZ1AVpzGlcVmGxzeFzo95zo07Il5IqcUR-ChlR7tl_v0Q1Ulpi4P2u3_YT5uwu3OR4t5kHO6S8cxaQ3Z83z7_rnDtp8eSSlckbOrwGo6m31YLd8cAWVZkTGY9b0WdDilJakWxk1iNL7ViuXnpAhm7nIj6c-nZGK02ZYCleUN7fAzOiP2oWTFdemiy1L1SIjT9KMykRtwW-Vj5_RJxvx-Cq4_UIEnRtcNjJ4pVmzGPvy_mvmbQQmY35HmkWl-tz6ddDdVUGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یو‌اس‌ای تودی: ایران با موشک جدیدش به آمریکا شوک وارد کرد
یو‌اس‌ای تودی:
🔹
ایران نسل جدیدی از موشک‌های بالستیک را به کار گرفته که می‌توانند از پدافند هوایی آمریکا عبور کنند و با دقت بسیار بیشتری حمله کنند.
🔹
جهشی تکنولوژیکی که به گفته کارشناسان نظامی، حلقه پایگاه‌های ایالات متحده در سراسر خلیج فارس را آسیب‌پذیرتر از دهه‌های گذشته کرده است.
🔹
محور این تغییر، یک موشک بالستیک با قابلیت جابجایی بالا است که ایران آن را خیبرشکن یا «قلعه‌شکن» می‌نامد و بردی معادل ۹۰۰ مایل و کلاهکی با قابلیت هدایت ماهواره‌ای و مانور دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/686093" target="_blank">📅 11:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686092">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnjaRKAJ_0LHVQxnURRPY8K2gigLVKavbN_2ppBMMBCLY7tfBW0Wc_e2Wmu6KD7xeL-Iam4-E8of1QwgQE3i3FgdAEQTj0PTH6hiL3Uy9yflnJr9C3TnwLLwkagxKEwrTlNTciVWR9k-NSRexp_Xf2BEvqx427MdmrTt2IozcaLB71Rq2oiNphBO3ZQwVTaaV1j3YuGMKvuf_T4Fk_HLsB0nDpPru6ceN0bndEMmnWPWTlD8IxA5fCwRrduwU4aGHODPBR38wtKkAIorhkbu2t1MBl7wznwV4YwvPaatagDyipxfZRso74kkFa74BoBU8l5AnZpYbALptkDClX9YaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/686092" target="_blank">📅 10:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686091">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سخنگوی دولت:‌ کسانی که تا سوم شهریورماه مراجعه کردند و محل زندگی خودشان را اعلام کردند، کالابرگ مردادماه به آنها تعلق گرفته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/686091" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686090">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fef35b95.mp4?token=YAjC1WRcuBO2WRwZ_CrPY7WcHyejo91mn2zT5CjVHs-FkDU5x66_OVLt6oQ4O3zmyfvIk1lCYQi56WS8K_ls4D_cmHbdBMGyeUhr9hziBQupQ06yUY33dl6u6Ig7m85o3EOWbSoM7fEiRNY9wY_ovaQEZ9Hj175QZhcA0thDQSl4GOBU7iA6M6IIN_O9H6TBC_YQexB2qBQoz0fQQg3SsC48jE7ISOdIYuZu395IQ1xLHAp9qpbVt_AkKN07tWCLcapuXsEZUct_63f1oLeCOug24Xd5xH2EFk_JJaU_x-PbLlK86B5srrm8MnWdeY9e3RlMrUqzZTDoPVlnfnVbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fef35b95.mp4?token=YAjC1WRcuBO2WRwZ_CrPY7WcHyejo91mn2zT5CjVHs-FkDU5x66_OVLt6oQ4O3zmyfvIk1lCYQi56WS8K_ls4D_cmHbdBMGyeUhr9hziBQupQ06yUY33dl6u6Ig7m85o3EOWbSoM7fEiRNY9wY_ovaQEZ9Hj175QZhcA0thDQSl4GOBU7iA6M6IIN_O9H6TBC_YQexB2qBQoz0fQQg3SsC48jE7ISOdIYuZu395IQ1xLHAp9qpbVt_AkKN07tWCLcapuXsEZUct_63f1oLeCOug24Xd5xH2EFk_JJaU_x-PbLlK86B5srrm8MnWdeY9e3RlMrUqzZTDoPVlnfnVbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت:‌ کسانی که تا سوم شهریورماه مراجعه کردند و محل زندگی خودشان را اعلام کردند، کالابرگ مردادماه به آنها تعلق گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/686090" target="_blank">📅 10:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686089">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae60853db3.mp4?token=mmrdcnTqZpds4mjy0i31q7EsQJ8-dhXIc78XEboslys6J0LWJDicZla87E6uGeNBb1VcddWbvgsnR66I-PsmekAcThijdqHIrMa703LvfHFnvL7iUOkTZBZ448ClBjU8Cswg4XOTornSYdJjNd3xL__9ScCEEpcfFuL9QTX_KusIeSqesGOCvc5y1Rs93eu2_IHEXwYEd9QUhTFL5uQkpHqBa8gSJVkG7hQFXnLhvIKljPrxuuzSnyWZL5AVJ315shLaR-1Bcatdd6Gy2MSzJnrfoFyygLXtEyCoyRgXbXO6NCEvMdQ85s8TzqfksvK5B9mMY7VYYECpcylo9vcsdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae60853db3.mp4?token=mmrdcnTqZpds4mjy0i31q7EsQJ8-dhXIc78XEboslys6J0LWJDicZla87E6uGeNBb1VcddWbvgsnR66I-PsmekAcThijdqHIrMa703LvfHFnvL7iUOkTZBZ448ClBjU8Cswg4XOTornSYdJjNd3xL__9ScCEEpcfFuL9QTX_KusIeSqesGOCvc5y1Rs93eu2_IHEXwYEd9QUhTFL5uQkpHqBa8gSJVkG7hQFXnLhvIKljPrxuuzSnyWZL5AVJ315shLaR-1Bcatdd6Gy2MSzJnrfoFyygLXtEyCoyRgXbXO6NCEvMdQ85s8TzqfksvK5B9mMY7VYYECpcylo9vcsdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جا دستمالی دست‌ساز؛ با یک ایده ساده خلاقیتت رو به درآمد تبدیل کن
🔹
این بار در
#چرخ_زندگی
سراغ ساخت جا دستمالی‌های دست‌ساز رفتیم؛ محصولی کاربردی و دکوراتیو که می‌تواند با طرح‌ها و رنگ‌های متنوع تولید شود.
🔹
با مواد اولیه و ابزارهای ساده می‌توان این محصولات را در مدل‌های مختلف ساخت و برای فروش در شبکه‌های اجتماعی، فروشگاه‌های دکوراسیون و بازارهای آنلاین عرضه کرد.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/686089" target="_blank">📅 10:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686088">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پروازهای فرودگاه چابهار تا پایان هفته  مجدداً از سر گرفته می‌شود.
🔹
سرویس اطلاعات کره جنوبی از احتمال برگزاری نشست میان مقامات آمریکا و کره شمالی در هر لحظه خبر داد.
🔹
زمین لرزه ۴ ریشتری ساعت ۹:۳۵ دقیقه امروز یاسوج و مناطق اطراف را لرزاند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/686088" target="_blank">📅 10:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686087">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f28cf9f5a.mp4?token=FkDVTshtYaI0aMGzq8St6oukXMoxr5zQy6txa1AJg3HeqYalrCy4BvX4u8dfoAaQ7KwP5tDwN0c7C0HScI_DCIYyVyNgK1lK8dFNyTw4EdExDesdG2O-nR870Ny7OTR8eYWNz9H_wnlZBTTLlpL9vr5upUnriY-JkkWKPRtExQBmnZLNzUoUGIeyznJFt99h-A6kRicD7DssjDmAH2XegJLzA4Rp8nBVm1DV1TAc0YJwGe9itTG6pj7gUdygF0vGR4NzMNL7pKpmM-nU6Sq8gs5w4U9mkaPJ7yw8FYptICmg-0Zt3hfk0xaLQgHFBAc-_3306Z10nWqnhBgxzwiiGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f28cf9f5a.mp4?token=FkDVTshtYaI0aMGzq8St6oukXMoxr5zQy6txa1AJg3HeqYalrCy4BvX4u8dfoAaQ7KwP5tDwN0c7C0HScI_DCIYyVyNgK1lK8dFNyTw4EdExDesdG2O-nR870Ny7OTR8eYWNz9H_wnlZBTTLlpL9vr5upUnriY-JkkWKPRtExQBmnZLNzUoUGIeyznJFt99h-A6kRicD7DssjDmAH2XegJLzA4Rp8nBVm1DV1TAc0YJwGe9itTG6pj7gUdygF0vGR4NzMNL7pKpmM-nU6Sq8gs5w4U9mkaPJ7yw8FYptICmg-0Zt3hfk0xaLQgHFBAc-_3306Z10nWqnhBgxzwiiGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با وجود سانسورهای شدید و ادعای ترامپ مبنی بر یک اصابت در پایگاه های آمریکا، تصاویر ماهواره‌ای برخورد موشک بالستیک ایرانی به پایگاه هوایی شاهزاده حسن را علاوه بر الازرق در اردن را نشان می‌دهد
🔹
علامت برخورد با آتش شناسایی شده در سامانه‌های تشخیص آتش ناسا مطابقت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/686087" target="_blank">📅 10:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686086">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ابداع عجیب علیرضا منصوریان از زبانی نوین!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/686086" target="_blank">📅 10:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686085">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhrRjMCC7OuTW5z5zirKkFgDraaDGhN_7dLTRJyolKGzQ9k7U-lJfb0f_CoV8e63EUR1LxEaSAdzd-bK-EiUHwfGfrnLNIDcYeXYUAxLLjo2UMEhaz9thsqOizmwwu7b8wwAJ3iTyawAe1rNYEBzWRu9FZJ3fpViFp5-T8wGW1XhM13DTPuegHrJ6Od6CvK1WkVd8sWtKPa9-FPkSKJ7F7FVyeH3btEFk_U-SBl31AOm4IXJTu5wrpkn_ViKe5IbuTpkR8ciRjuwffF1z9BW9qrnWT5vHxsRXDpb4KnPkG5rmeFLdAy5TUBu9UJ6MLgj7fMKjdK3klOTfdBCgWu8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازسازی زیرساخت‌های آسیب‌دیده از جنگ در هرمزگان؛ پل گریوه(گچین) بندرعباس تا پایان هفته زیر بار ترافیک می‌رود
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای هرمزگان از اتمام روند بازسازی پل گریوه در غرب بندرعباس که بر اثر حملات دشمن جنایتکار آسیب دیده بود، خبر داد و گفت: با اتمام عملیات بازسازی، این پل تا پایان هفته جاری زیر بار ترافیک می‌رود.
🔹
عباس شرفی با اشاره به آغاز عملیات بازسازی دهانه پنجم این پل هشت دهانه از پنجم مردادماه امسال، افزود: با انجام عملیات آسفالت‌ریزی و نصب نرده‌های فلزی، این پل آماده بهره‌برداری است.
‌
🔗
لینک خبر:
https://rmto.ir/s/mfaonFY
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/686085" target="_blank">📅 10:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686084">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUyaZhET3nS1i3ZqMSV_95qqCOEbC4sB899j35xXTQOwoAo4ZOCeRmksWxRCIce6ltZLtDBL5Zj5lVmwn8jJUnSyKXOGfOY1ENd0y-Ob1ElWzi8y02TsowX9w6kfnW4ggQ4ahHZspsgn0tQQ6Jz0sS4kZ8DGc1ceKv4dxTMutZ0yxiEmDQCDvhS3-sawyP3Vqd-iskeJ-KMYOht7C_HxG1--vnWd8Ghx7nw1ta6m_Ef-SHsximPLGbFC9fKViuWOAjJVRpoEAWVPnPwsfIKz_-bJMmSaq1KIXgBhUvYbU3kN1mol6oWhWBBitD4bnKE5XJaT0quK6-MmOSUAmYy_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری آزمون‌های تافل و GRE رسماً در ایران متوقف شد
🔹
مؤسسه ETS در صفحه رسمی ثبت‌نام آزمون TOEFL iBT اعلام کرد که در راستای رعایت تغییر اخیر در مقررات وزارت خزانه‌داری آمریکا (OFAC) برگزاری آزمون‌های TOEFL و GRE در ایران متوقف شده است.
🔹
این مؤسسه یادآور شد داوطلبانی که تحت تأثیر این تصمیم قرار گرفته‌اند، هزینه آزمون خود را پس خواهند گرفت و افرادی که درباره این موضوع سؤال دارند می‌توانند با ایمیل رسمی بخش TOEFL تماس بگیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/686084" target="_blank">📅 10:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686083">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تردد کشتی‌ها در تنگه هرمز همچنان ضعیف است
🔹
گزارش های منتشر شده در حوزه دریانوردی نشان می دهد طی روز گذشته تنها چهار کشتی وارد تنگه هرمز شده و یک کشتی از آن خارج شده است.
🔹
تعداد کشتی های باربری عبوری در تنگه هرمز به صورت میانگین به ۵ عدد در روز می رسد، در حالی که طی ۱۰ روز گذشته این آمار به ۱۴ کشتی می رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/686083" target="_blank">📅 10:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686082">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb3297357.mp4?token=npUL1kuT-1LT6XKDTqRFotEZJ_obIQa94h3MH7-iZ3NWSbyZjUZhHsetnMRmDJD7c6JF14Cr3WHdHAJAzpMDfJrksQEy9KpIhmmgqMcqEeZ8HPYY98xhDuWQl3-MdPuMPAu3EEDzX0zmKgbwESSKboLZhUHjG56Hx8Cikr1cVLYCfZRIPrpcmciQskJ2L7nhzw8cRthJ4BW4iwByVgri8jDRR13z8vGamk0rPGbBfxRIw-Pdo7wrtXQkcEwaqGZXGztwuYYH9wSQ73lOcdgt1JSGIhBHv_mKQLvj8QiWWGTNrPEAInV7ffBuKr4Jzd9CyWHbm-iCAMzJawvD6CIQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb3297357.mp4?token=npUL1kuT-1LT6XKDTqRFotEZJ_obIQa94h3MH7-iZ3NWSbyZjUZhHsetnMRmDJD7c6JF14Cr3WHdHAJAzpMDfJrksQEy9KpIhmmgqMcqEeZ8HPYY98xhDuWQl3-MdPuMPAu3EEDzX0zmKgbwESSKboLZhUHjG56Hx8Cikr1cVLYCfZRIPrpcmciQskJ2L7nhzw8cRthJ4BW4iwByVgri8jDRR13z8vGamk0rPGbBfxRIw-Pdo7wrtXQkcEwaqGZXGztwuYYH9wSQ73lOcdgt1JSGIhBHv_mKQLvj8QiWWGTNrPEAInV7ffBuKr4Jzd9CyWHbm-iCAMzJawvD6CIQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتشه تا با یک‌ روش ساده و آسان زرشک‌پلو با مرغ رو‌ متفاوت درست کنی
😋
مواد لازم:
🔹
مخلوط سینه و ران(سینه یک عدد ران دو عدد)
🔹
پیاز: سه عدد متوسط
🔹
فلفل دلمه: نصف یک عدد
🔹
رب گوجه و رب انار: هر کدوم یک قاشق غذاخوری
🔹
زرشک: یک سوم لیوان
🔹
نمک،فلفل و زردچوبه و زعفرون…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/686082" target="_blank">📅 10:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686081">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بلیت فروشی دربی تمام شد
🔹
سامانه بلیت فروشی دیدار دو تیم استقلال و پرسپولیس که فردا در ورزشگاه نقش جهان اصفهان برگزار خواهد شد از روز گذشته باز شد و در کمتر از ۲ ساعت ۳۵ هزار  بلیت به فروش رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/686081" target="_blank">📅 09:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686080">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo1ejPd6oPPL7l7Ay_vcBuDWkk34pD-6yD39n5z7dWH76IIG1s10wNX4W8HceiEHAsuushK_K9IDaQGFSO9pngF-8EgAdIMKdcnrralSU19sYtXPsQ8PC11iBO8p29ApHM2vSdv9g7ZFePpRVo76Lvp0fscafQz8qx6yixKYdNyPgaI1z12J4Luh24Bq5QsLkM8yxrxxJczi9JojL6yJxKv4dJDCwXpqrjL-jMcB7WQ4CYQXtUYLzxFOeYNsfloPohe5u4UIOpm0CDt_tUXYCdY-XDYX5UI9ptKyhnjhMYif7b6ubVKNwrsgOqfAG8IOVlFpXkwDwB1HPlKWAT2-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بازار بورس از ۶ میلیون و ۶۰۰ هزار واحد عبور کرد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/686080" target="_blank">📅 09:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686079">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75d20de6b.mp4?token=hLoxPx9exMpHuf2c9A3P3IPgQeh0g8VtvBYsILirnDBrHS3LLZ7D453nguPXwA1uknM2Vewi_f5AUENkot55s_Kx8ztNVKdSo6lINyuB3s3xAgWW-zivhsFR0lSuOLV0VGxjU9NoPY9-JWDkcbSL3cnswdAuhMzDsZfaKXO2draTRnU7tt6vJ3k2R5RQO-B4jXuCen2PFpK4eJhmrA0vGOeyvDJnzlgMz2SxZwxwTJPywuIdo6Zz8sj2UlBg4I5ZItDAdvDIiKOrMqRFYPI9oQIYugxApFqfSxVWoPe8P8vxHzH4YB1ogyQ2eyTucwnHNo5mWtURooPpLXlDEoWdQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75d20de6b.mp4?token=hLoxPx9exMpHuf2c9A3P3IPgQeh0g8VtvBYsILirnDBrHS3LLZ7D453nguPXwA1uknM2Vewi_f5AUENkot55s_Kx8ztNVKdSo6lINyuB3s3xAgWW-zivhsFR0lSuOLV0VGxjU9NoPY9-JWDkcbSL3cnswdAuhMzDsZfaKXO2draTRnU7tt6vJ3k2R5RQO-B4jXuCen2PFpK4eJhmrA0vGOeyvDJnzlgMz2SxZwxwTJPywuIdo6Zz8sj2UlBg4I5ZItDAdvDIiKOrMqRFYPI9oQIYugxApFqfSxVWoPe8P8vxHzH4YB1ogyQ2eyTucwnHNo5mWtURooPpLXlDEoWdQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید در ایالت یوتا ۳۴ واگن قطار را واژگون کرد
🔹
طوفان شدید در شهر لیندیل ایالت یوتا آمریکا باعث خروج قطار از ریل و واژگونی ۳۴ واگن آن شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/686079" target="_blank">📅 09:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686078">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
همتی: بازار ارز آرام می شود  رئیس کل بانک مرکزی:
🔹
دشمنان هر هفته تحریم جدیدی علیه ایران اعمال می‌کنند، اما سیستم اقتصادی کشور همچنان به کار خود ادامه می‌دهد.
🔹
گرد و خاک ایجادشده در بازار ارز فروخواهد نشست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/686078" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686077">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر نیرو: سوخت ‌زمستانی نیروگاه‌های برق تامین شد.
🔹
وزارت ورزش و جوانان: سقف زمانی پرداخت وام ازدواج در سال ۱۴۰۶ سه ماه خواهد بود.
🔹
معاون هماهنگ کننده نیروی پدافند هوایی ارتش: ۲۴ ساعته حتی فراتر از آسمان ایران را رصد می‌کنیم.
🔹
قایق‌های جنگی رژیم صهیونیستی با ادامه نقض آتش‌بس سواحل غزه را گلوله باران کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/686077" target="_blank">📅 09:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686076">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
همتی خطاب به ترامپ: ارز داریم به قدر کافی هم داریم  رئیس کل بانک مرکزی:
🔹
به‌طور قاطع می‌گویم این ادعا که ایران وارد فروپاشی اقتصادی شده، درست نیست.
🔹
روند وصول مطالبات و منابع ارزی ایران همچنان ادامه دارد و علاوه بر آن، از ذخایر داخلی نیز برخورداریم.
🔹
همچنین…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686076" target="_blank">📅 09:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686075">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
همتی خطاب به ترامپ: ارز داریم به قدر کافی هم داریم
رئیس کل بانک مرکزی:
🔹
به‌طور قاطع می‌گویم این ادعا که ایران وارد فروپاشی اقتصادی شده، درست نیست.
🔹
روند وصول مطالبات و منابع ارزی ایران همچنان ادامه دارد و علاوه بر آن، از ذخایر داخلی نیز برخورداریم.
🔹
همچنین منابعی در اختیار داریم که به دلایل مختلف امکان اعلام جزئیات آن‌ها وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/686075" target="_blank">📅 09:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
توجهی به قواعد حقوق بین‌الملل امنیت و  ثبات کل منطقه و جهان را تهدید می‌کند  رئیس‌جمهور در اجلاس سران سازمان همکاری‌ شانگهای:
🔹
امروز منطقه ما با مجموعه‌ای از تهدیدات پیچیده و درهم‌تنیده مواجه است. تروریسم، افراط‌گرایی خشونت‌آمیز، قاچاق مواد مخدر، جرائم سازمان‌یافته…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/686074" target="_blank">📅 08:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686073">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
توجهی به قواعد حقوق بین‌الملل امنیت و  ثبات کل منطقه و جهان را تهدید می‌کند
رئیس‌جمهور در اجلاس سران سازمان همکاری‌ شانگهای:
🔹
امروز منطقه ما با مجموعه‌ای از تهدیدات پیچیده و درهم‌تنیده مواجه است. تروریسم، افراط‌گرایی خشونت‌آمیز، قاچاق مواد مخدر، جرائم سازمان‌یافته فراملی، جرائم سایبری و تهدیدات نوظهور امنیتی، همچنان صلح و ثبات منطقه‌ای را با چالش روبه‌رو می‌سازند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/686073" target="_blank">📅 08:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686072">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
محققان: برای کنترل فشار خون خود، بدون عذاب وجدان آخر هفته‌ها بیشتر بخوابید
🔹
پژوهشی جدید نشان می‌دهد افرادی که در روزهای تعطیل حدود یک تا دو ساعت بیشتر از روزهای کاری می‌خوابند، کمتر با فشار خون بالا مواجه می‌شوند و یک ساعت و ۲۷ دقیقه خواب اضافه با بیشترین میزان کاهش احتمال فشار خون بالا همراه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/686072" target="_blank">📅 08:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686070">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdsRSZp6SNPMlBTtVt9uz9dQAH7pyphYIeLICB3C00BRAg0wYYaitZ3l6g4nP5qZvUhzy0urA0_nY6z7YO9hk3_B0CXQaq63YPjbger0LTjQDDxBwxS9oraOa2I5MCB3XSRhAQk5c910KKaoCEi4HQ8wH4eTxTsxDhLHMNLHMYAPLk_uMSsMhv-pvIa3voEPcDesFCtrtI4TnfTBn_ABc13flPafD6-KyQibuL1YVboCEmmMAbeA_FOjgBTgDv854BWPEooKqElI25BVHzLQSg5f7X4e0Uo4tIEYZ7waLr-4RM_j4k7-3ndvPGeoOSB6DEXNcjCWxRuLKC1FMS6uOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس یادگاری سران کشورهای عضو سازمان همکاری شانگهای
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/686070" target="_blank">📅 08:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686063">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52eec2cc0c.mp4?token=FvXGcqcZCIsBYm6YSQGM4B82CXSvAoHXaxXgcEQTbln7JbCrmBYB7EfSzhwqUSX6uhQ18HwsEXqaNF9XCJnt0el7X8GNeRccOxZJD9zWBMZhSdtqZd9ofK4TGg45ANyYrTpUoagPJy4f9LFF1X-ZC5zL9WBTUaXq7OccCT-xEbH-8B4G2pQelnJkKBrQalyosAOhzl5gaFXuzyOjMpr6NmIpbV7o5PLbMeYtQ8z23cUsO1Hgt3XASXAkOs6_Wb4l7Y5DugX_vo6FncWt-CenZjx9ihDN4tVuAwzFd3nGnFzmNcd1xfU06V9BTiywDdsnK8HDArv9nvkjzzjj8lysuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52eec2cc0c.mp4?token=FvXGcqcZCIsBYm6YSQGM4B82CXSvAoHXaxXgcEQTbln7JbCrmBYB7EfSzhwqUSX6uhQ18HwsEXqaNF9XCJnt0el7X8GNeRccOxZJD9zWBMZhSdtqZd9ofK4TGg45ANyYrTpUoagPJy4f9LFF1X-ZC5zL9WBTUaXq7OccCT-xEbH-8B4G2pQelnJkKBrQalyosAOhzl5gaFXuzyOjMpr6NmIpbV7o5PLbMeYtQ8z23cUsO1Hgt3XASXAkOs6_Wb4l7Y5DugX_vo6FncWt-CenZjx9ihDN4tVuAwzFd3nGnFzmNcd1xfU06V9BTiywDdsnK8HDArv9nvkjzzjj8lysuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش چند حرکت کششی کاربردی که می‌تونه در برنامه تمرینی روزانه قرار بگیره #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/686063" target="_blank">📅 08:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qekj5zJ2WqxAHp5_Wxu6ZZn9NXyqnt84tsj0iH3YQ31SBJ0axjMrrfilGTXqxd9VDBtA9beqHHPRA4V8V0TsQ27ZP0gP4D8y0PGrMwoGVAno7Qr8v852urZ0xf1x_Ijf-cUFibQDNp7sbARbeYu1Buut1AUwMtqtmDCH4GF3ZA52850yCKmEduJnS5wsA7x9vV-qdEVv__IzeYoKeCLGvQohqkhIElORCq-ND4lrz-RyGO_TOdkowXVF6yfUMkpN3QVfWWwQlRPNDPkUfSRmK1SI0yIicOYyB4qlSiF_x6wYlIDugEZe9PdSX20z3bF84BqsMl2lzsbEN6mGPIWXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۰ شهریور ماه
۱۹ ربیع‌الأول ‌۱۴۴۸
۱ سپتامبر۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/686056" target="_blank">📅 07:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayoXbfAb35_oscPGwMOPsE_OwMc8POHwezEVphX3CI87R5WXxYN2cmj7uebMyiBIYaKhGNWrOmrvAxPI43o8Erejp2NK4M4h1Y1_ZPYPyEMoQn1TtRImPWZGlDKV1DHBUQG-dHaRVPVAETivS5jfjSq1sk7DGgCo9o9cODXGZxdWX7pdhEqYsEvGLtYT8KHdq0tkPDDUs_7KaYy3Ar-m--63CDz94H1SFz3nIn03UyCWUHZq6o3zN1LXhS1MG1W672UWQndaAPGIif05rLguAPBYrzHKHtAR3pPtf2dvfqDBT-INhNs4SD3dyr9Ghv_kyoJkkOXhgDCmlwTbhfAwZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک نفتکش عربستانی در کریدور جنوبی تنکۀ هرمز متوقف شد
🔹
نفتکش عربستانی غول‌پیکر با نام سیدر، در حین گذر از کریدور جنوبی تنگۀ هرمز متوقف شد.
🔹
ساعتی قبل UKMTO از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش خبر داد.
🔹
نفتکش سیدر قابلیت حمل ۲ میلیون بشکه…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/686051" target="_blank">📅 02:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686050">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
فاکس نیوز: درباره جنگ با ایران چه چیزی یاد گرفته‌اید؟
ادعای جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔹
«آنها حاضرند برای رسیدن به هدفشان دست به هر کاری بزنند و فکر نمی‌کنم پشت این اقدامات، حکمت و دوراندیشی راهبردی چندانی وجود داشته باشد؛ هدفشان این است که جریان نفت و گاز را تا حد ممکن کاهش دهند.»/انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/686050" target="_blank">📅 02:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686048">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP1a5X6MPq7izmDGqWHotr4lrsQ68LE19RxNxT5wsOwHTx96gHe-XbBp9fLT9i3Sf3LppGGwNbg_AZ9K5mx6VlzLhH0s3-0Pb1_NkYCgvQyREM79locgnPEw4-IfAOosZxj6niBTz7Zas3nj4cY_OfbpY6qkSLyBiRzLolSHgjB7xRqSxcBF4KgHdnVpsO-A2osdHjbIJ8YDVzvKusPjIiwUIugBxAbone8WOAOKLjQ7tojTVm3PP0UcfY_fuOQLC0cIrJ8W2521mieK2zWzximLjPVM5U1p1hveEn2cRAibaXZ1EWg5UE4nmWvNDvrApCYtGhXigUw9iH_m5KFFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر جنگ آمریکا استعفا داد
🔹
سی‌ان‌ان استعفای «دنیل دریسکول» معاون وزیر جنگ آمریکا در امور ارتش، بعد از ماه‌ها اختلاف با رئیس پنتاگون خبر داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/686048" target="_blank">📅 01:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686046">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b7ac2b46.mp4?token=ttHccm9LKLqaIwespLJoBEauIASRmxL-D3k9ZXMabDypszMRG0O94KE73_wnYXdALRQdAD2acAceLoDf8tjueeQbbcHwOa0joTUbttMMdBbIhrQK65bfP5J_e8vn6lq5VmL0aAWb7nrs1HGHLynaBLDZTCAP45G89vcsH0YzyvOnkAAmldBkbUTwUUEBrJux8u1COLcLfkglorvq6ToJd_un2BvGP3cY-4dm7N1N8T-0foLvLohWLSTUvj7rcFntlipl4nSotw0ydo50jvCFcbut1NtufeO3Kw8g0dRirwFEuWZtzQ988cOwNKYN_XJu7n7Dy2zlqlinu5nQMJwj0L20QkaeKUvT5oRBnVyfwBYUbfBdmRvzFxCCc3IP-0BGQXZLbT_QecKq5RGtK7M0IcaKlIZIdcMsCwS1dsIHDkpGtmehygCvkRC_VzFcivsn2QVU7-7ODJvGOvzQCk2-fGyxNUPj9KIm6WyWIM8uo48itV-DkC9guEhBWuKd-IQ5qcppcChWadAdZUHYQDd1RB4KwsO8j2kuTbofwQEsb4Zcoiy2TpZJoK-9yv787z0dxTDrDKi1MFafdzDGGP62mri9MpAX8A2ExhllpqlyrEhv2qHbmgQQadRrXeBQLFcbJ5jbxRzFkS1qUeKEry6FryBaFcmyYBWNSLFzrl-UouA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b7ac2b46.mp4?token=ttHccm9LKLqaIwespLJoBEauIASRmxL-D3k9ZXMabDypszMRG0O94KE73_wnYXdALRQdAD2acAceLoDf8tjueeQbbcHwOa0joTUbttMMdBbIhrQK65bfP5J_e8vn6lq5VmL0aAWb7nrs1HGHLynaBLDZTCAP45G89vcsH0YzyvOnkAAmldBkbUTwUUEBrJux8u1COLcLfkglorvq6ToJd_un2BvGP3cY-4dm7N1N8T-0foLvLohWLSTUvj7rcFntlipl4nSotw0ydo50jvCFcbut1NtufeO3Kw8g0dRirwFEuWZtzQ988cOwNKYN_XJu7n7Dy2zlqlinu5nQMJwj0L20QkaeKUvT5oRBnVyfwBYUbfBdmRvzFxCCc3IP-0BGQXZLbT_QecKq5RGtK7M0IcaKlIZIdcMsCwS1dsIHDkpGtmehygCvkRC_VzFcivsn2QVU7-7ODJvGOvzQCk2-fGyxNUPj9KIm6WyWIM8uo48itV-DkC9guEhBWuKd-IQ5qcppcChWadAdZUHYQDd1RB4KwsO8j2kuTbofwQEsb4Zcoiy2TpZJoK-9yv787z0dxTDrDKi1MFafdzDGGP62mri9MpAX8A2ExhllpqlyrEhv2qHbmgQQadRrXeBQLFcbJ5jbxRzFkS1qUeKEry6FryBaFcmyYBWNSLFzrl-UouA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از اوضاع دردناک کودکان نوار غزه در سایه ادامه محاصره ظالمانه این منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/686046" target="_blank">📅 00:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686045">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
خبرنگار: بر اساس گزارش‌ها، چندین فرمانده نظامی به هگست گفته‌اند که جنگ در ایران توانایی ما را برای مقابله با تهدیدات در جاهای دیگر، از جمله خاک میهن، تضعیف می‌کند
ترامپ متوهم:
🔹
هیچ‌کس دیگری به اندازه کافی دیوانه نیست که این کار را انجام دهد. ما در سراسر جهان مهمات زیادی داریم که در صورت تمایل می‌توانیم از آن‌ها برداریم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/686045" target="_blank">📅 00:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686044">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
هدف قرار گرفتن یک فروند کشتی در نزدیکی سواحل عمان
🔹
یک کشتی در آب‌های ساحلی عمان، در تنگه هرمز، در حین تلاش برای عبور از این تنگه، دچار حادثه دریایی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/686044" target="_blank">📅 00:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686042">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cede7dbb3e.mp4?token=mj47TwRt3BSM50xojbjGS5tQHTCuaeNyxdekbSkM-FFMtZl9_bGnL9dcqieE9r0ZgM8_SP9vDWBcjQjmXHTi6ZH9UhfDnLETJd5dcv8DyvxNSwA7j-1jNedV3HjKZyaV3ZDTwIDmanR4O1i2XTtyFiyFsQsDTMcPFk5tHtuvnNCYZ42u8FK8_08DqRvOrMqQB3LIaHXyVYkQcmEfrstFPJ6TZZB2_ihEBQFLKP2X15k_15H2VQmNOUH7lAlDN4yVtFVs6f_AH_sDjSZYUhKbECGSAKaA8GlZOerKX6wzC7Kn2_UEZulo1-Wckm3CCu1zR23RGbd0pLIgK3cngRTQEDLIBMZNnJuW428G7hMvofKwyvq2x0MqD-U32AQs6tXHsqurkY5-UnbqsFrWk8We-5oIqKTYRl_olDYACYQlE3trKPN01OqbVX7LemKpLn-6XzNaKvK1Pk1lBQ7fQCdiQrHSo1P-9_DIXEsS47kSKA8YrATmWL7CiGaCKDW6ov1Eba-VEa3BqSFJvm-y7NzNNDyaXECVTSqHmE1t4BvLQY05C57yY1s45tzRijKNSgNGYOmOqnuuS6qoF6sZJBtwHw1PLLELXwED0YsLhK1jqcAfEGc_LDD2J0k-Q9vXkYpJpcmIpao4If2e2N2QB9DspKRHogvl5NHwdA_-YAUqKuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cede7dbb3e.mp4?token=mj47TwRt3BSM50xojbjGS5tQHTCuaeNyxdekbSkM-FFMtZl9_bGnL9dcqieE9r0ZgM8_SP9vDWBcjQjmXHTi6ZH9UhfDnLETJd5dcv8DyvxNSwA7j-1jNedV3HjKZyaV3ZDTwIDmanR4O1i2XTtyFiyFsQsDTMcPFk5tHtuvnNCYZ42u8FK8_08DqRvOrMqQB3LIaHXyVYkQcmEfrstFPJ6TZZB2_ihEBQFLKP2X15k_15H2VQmNOUH7lAlDN4yVtFVs6f_AH_sDjSZYUhKbECGSAKaA8GlZOerKX6wzC7Kn2_UEZulo1-Wckm3CCu1zR23RGbd0pLIgK3cngRTQEDLIBMZNnJuW428G7hMvofKwyvq2x0MqD-U32AQs6tXHsqurkY5-UnbqsFrWk8We-5oIqKTYRl_olDYACYQlE3trKPN01OqbVX7LemKpLn-6XzNaKvK1Pk1lBQ7fQCdiQrHSo1P-9_DIXEsS47kSKA8YrATmWL7CiGaCKDW6ov1Eba-VEa3BqSFJvm-y7NzNNDyaXECVTSqHmE1t4BvLQY05C57yY1s45tzRijKNSgNGYOmOqnuuS6qoF6sZJBtwHw1PLLELXwED0YsLhK1jqcAfEGc_LDD2J0k-Q9vXkYpJpcmIpao4If2e2N2QB9DspKRHogvl5NHwdA_-YAUqKuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✂️
ماشین اصلاح GYT-999
✅
صفرزن و خط‌زن | تیغه استیل
🔋
شارژ Type-C |  تا ۴ ساعت استفاده
📊
نمایشگر شارژ + ۴ شانه اصلاح
🔥
فقط ۱,۳۹۸,۰۰۰ تومان
💰
قیمت قبلی:
۱,۶۹۸,۰۰۰
✅
پرداخت درب منزل | ضمانت تعویض ۳ روزه
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/686042" target="_blank">📅 00:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686040">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac8097603.mp4?token=KFsZVbEAsUQr5Sx46Fkec2kl_27NFs5laZ4QHy0rCxCZekiGAaWyoEWMGuRUJCJ_j-h4MKXTlAI1X1S71Yyq4REHoFfeYTvgvI8rOe3AB_twdl6NvLLnQS7a120D6uNMJrEPawNZZpfCK0aWid2bS9FQWYhtVzZhQeItPlCPZ-m_GEoZec7CAZC3Q044oPyc7IdUvrArdKQ9rEzbs2bwU3ZlWWGfj_s1QHRm1ASyr4gpt-Rozl9vtdPdygx1974bofSbDh1dt5G1qJhnrl0YYrFjy4RN7tKivOAMRu2thPzRahisXizVFUrd5OdMUuFrVIgU2KkcW1OghuwZRE1J3CLHoZP5LlISaRkSuM1z-83BNs05AwTrzqXlF1LfHB1EheH6r7HmZctDVBhrBlbd3gDW_ykY0v0q7lU_0a3vqmCjMtmQ7MpZFBG2t-laNhOnFqkFG_chBX6pi85aKWhB6v-eYUW7FT43yap-dZZh4ihvXpUCq4WsTy_RKTAhdKqyyTLathkWkU7dfGCsmJ8Qkwb4qMorcBtZ0imudYnXzn-qDk2fCMomnW2DwmQtCgFoRpouDnbBDlnMixJDrnbUw5iP6S2Pwp8ik1ds48sebWHz-dBNyJcVIu6_gZt0PxYjRzYT5Hk0WoXSfvx7zt2qUtw-qxHl2-4VEr2L9b3jstk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac8097603.mp4?token=KFsZVbEAsUQr5Sx46Fkec2kl_27NFs5laZ4QHy0rCxCZekiGAaWyoEWMGuRUJCJ_j-h4MKXTlAI1X1S71Yyq4REHoFfeYTvgvI8rOe3AB_twdl6NvLLnQS7a120D6uNMJrEPawNZZpfCK0aWid2bS9FQWYhtVzZhQeItPlCPZ-m_GEoZec7CAZC3Q044oPyc7IdUvrArdKQ9rEzbs2bwU3ZlWWGfj_s1QHRm1ASyr4gpt-Rozl9vtdPdygx1974bofSbDh1dt5G1qJhnrl0YYrFjy4RN7tKivOAMRu2thPzRahisXizVFUrd5OdMUuFrVIgU2KkcW1OghuwZRE1J3CLHoZP5LlISaRkSuM1z-83BNs05AwTrzqXlF1LfHB1EheH6r7HmZctDVBhrBlbd3gDW_ykY0v0q7lU_0a3vqmCjMtmQ7MpZFBG2t-laNhOnFqkFG_chBX6pi85aKWhB6v-eYUW7FT43yap-dZZh4ihvXpUCq4WsTy_RKTAhdKqyyTLathkWkU7dfGCsmJ8Qkwb4qMorcBtZ0imudYnXzn-qDk2fCMomnW2DwmQtCgFoRpouDnbBDlnMixJDrnbUw5iP6S2Pwp8ik1ds48sebWHz-dBNyJcVIu6_gZt0PxYjRzYT5Hk0WoXSfvx7zt2qUtw-qxHl2-4VEr2L9b3jstk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به راستی شهید قاسم سلیمانی کیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/686040" target="_blank">📅 00:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686039">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">افتتاح نمایشگاه
#الکامپ
، رییس سازمان نظام صنفی رایانه ای: امید آفرینی یکی از اهداف این نمایشگاه است. از استقبال روز اول راضی هستیم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/686039" target="_blank">📅 00:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686038">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7UTdbjjtzdEfe7GWbjrvLpX5VM_HXI4Q_-fR4CSt0LkQy5CoQMAH7NEhc7GUxL4-IxwZrj2edWyQjLUL1NnGSbBfU2L8olRb8nrhu0j0a7HLQSyZB2WENUzzQusNNLKGL9Wy1B9LpSrBH9g11p-uKN4uPMjiJSI4vc1TfkCnxEc3NESI6VPBSYwh3vuAsatdri9ircYRSTLTXe-b36VSh5Yyj56EA-ek_Cbd6J78W0V1NlTdL6owCd10NDfI_CYbqGfIv-h-QEIGZfGRP-JYu5AvU1Hcw3D8ZeZvCeOjsq8pTLs50N0tITOF7lem-u2a9MmkzAVhN5i822r9cXGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/686038" target="_blank">📅 00:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686037">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUiyL7Rz1IYuFJqpWFEcfH62y5vsWu98A-ngal3utIrzCpgjfaf5X8Xur6Eu_Qf6N5mfCCBFZTBKfhMGkgiQWAfH-ujs6Rd-QJU7npTe-8-yj2kdQD9rTfW59CZwH7mnXugj9ougkRTRfpYUibkZDZ1zPrzEpaVNTWvPGfaPbCp9LPJwXZDvAO8rTYM4FFxxiYz3dxk1Xn2OJPAXUlToGH6Z2ffp8aaaaHaS0VOlKh5b7LTTo-UkRrnwj_lD9do4TRR4bH2-MzZA78usOlFPLubs0-FH213ZfNCM0syRiKIlWXxZ2x0KMOxoftFrROV8Ta4omQhB5Rb5K7FL_dXkLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمایی سریع برای اتو کردن پارچه های مختلف
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/686037" target="_blank">📅 00:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
رایتل در مسیر اپراتور صنعت و دولت هوشمند
🔹
دکتر مهدی فقیهی، مدیرعامل رایتل، در حاشیه الکامپ از حرکت این اپراتور به سمت خدمات تخصصی صنعت و دولت هوشمند خبر داد.
🔹
رونمایی از eSIM عمومی و صنعتی
🔹
همکاری با فولاد مبارکه در حوزه 5G خصوصی
🔹
رونمایی از دوقلوی دیجیتال و سیم‌کارت گیم
🔹
توسعه خدمات سلامت الکترونیک
🔹
فقیهی همچنین گفت: قیمت اینترنت در ایران بسیار پایین‌تر از قیمت‌های منطقه‌ای است و اپراتورها با وجود افزایش هزینه تجهیزات، امکان افزایش متناسب قیمت‌ها را ندارند.
▫️
مشروح خبر
khabarfoori.com/fa/tiny/news-3241824</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/686036" target="_blank">📅 23:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686035">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R36jWpvd1z9PrcCWwRxt0sR6GwPizhqntAm_w6xzjkQ_f50xrV4rGgOJcFpbqrh7E4h3vep6Wf3SvuWkTtq9Cl3zzKIBSaAL5EYxa4lHQ_r1WiuIs9X0eJ4P9hiM-TLF7GvFDNMDNrU0yg-l7Z04JmInnRIn5Z-p17F8P8hiz5V0pajzp9h0R89ptUiNWdvDFWxRhmB7A4cHxX8n3YL2cJrjzyMDEEDIrkLTZpNd4As7gQPZ2tikN-nuUeh3pol6gt7g_J1X6TUblZOuBQR_HYysMRNb6f1lJGhJxOO0Yb8tlVTXAyS1yQhpxdEYoVIV_iwFe9UinoL6YiokKLx8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت به عصر «تاناکورا» | رونق بازار خرید و فروش کالاهای دست دوم در ایران | بازارهای پُر و جیب‌های خالی!
🔹
این روزها ترافیک سنگین پلتفرم‌های واسطه‌گری و شلوغی راسته‌های کهنه‌فروشی، نمایشی فریبنده از یک «رونق دروغین» به راه انداخته است؛ رونقی که پشت ویترین پرزرق‌وبرق اصطلاحات شیک مانند «اقتصاد چرخشی» و «فرهنگ بازیافت»، حقیقتی تلخ و گزنده را پنهان می‌کند: سقوط آزاد قدرت خرید و عقب‌نشینی ناگزیر خانواده‌ها به سنگر کالاهای مستعمل.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3241757</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/686035" target="_blank">📅 23:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686031">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUnAKKK3BdBq4WJPuOBcjCVq5dqP_pLG4CAUlwBiLs-TW5NHgNvJRoZQ97qrSv1QVaKRz0-F_gjsrn6QkMmMkLBYH7tRiO-mEYDb8RqZrlxTknkmq_IB0Pu5qJlnFGDbPGwwPLv58yT42PbdKyWmupR_ee9kto9M7KWYxoy6GxCpDm4me-90hoVU3sCg9HtEPp2iQLm5RrxElnd3-N0XLEzBvbgef2rL1puuI97jnEvrgEyjEVSjnZ8WDNVtZ8W5I3STqaIwireEZLKcodyHPZ53BwD53FJ7i4qnFdYEEc6nb21sEKlCoiFkc4VPecvkEM9lNAyTwI2wsue5DlY8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف قرار گرفتن یک فروند کشتی در نزدیکی سواحل عمان
🔹
یک کشتی در آب‌های ساحلی عمان، در تنگه هرمز، در حین تلاش برای عبور از این تنگه، دچار حادثه دریایی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/686031" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ترامپ درباره احتمال نامزدی هگست در  ۲۰۲۸: صحبت درباره این موضع خیلی زود است   #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/686029" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d36d4d7fcc.mp4?token=q8nI_OMz470pzEnl-yVjI5htmJa1N1yqiqrpdo4mGO2NTbHpXMJOLt_Sy4cSqCA1RtTPLhV28XGl4SH9P72vEZqcMjGLdP_tMRnB5vLyErDVbGEyUStlCVhwJgpJb2T6-pydV3OVPYnVxJZPNk9lCyTcYrZb6R7aoNCtDtEAuac6Q1ovnkqLtp6cNtRUsE7oDOPNPnXV-gGIXoxfFyIe4Gnf0BAMqEROCI6rpkv3gRK_v8-zLzs16YCcYAKbQkRW1HIvQbffYSuOVd6MIB9DOJVdutaf0BxDrKlB3YYuXU4dqvcqlXnlDr7WfKGTlGruBn5KtkeE4bBVu1DbgoxZqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d36d4d7fcc.mp4?token=q8nI_OMz470pzEnl-yVjI5htmJa1N1yqiqrpdo4mGO2NTbHpXMJOLt_Sy4cSqCA1RtTPLhV28XGl4SH9P72vEZqcMjGLdP_tMRnB5vLyErDVbGEyUStlCVhwJgpJb2T6-pydV3OVPYnVxJZPNk9lCyTcYrZb6R7aoNCtDtEAuac6Q1ovnkqLtp6cNtRUsE7oDOPNPnXV-gGIXoxfFyIe4Gnf0BAMqEROCI6rpkv3gRK_v8-zLzs16YCcYAKbQkRW1HIvQbffYSuOVd6MIB9DOJVdutaf0BxDrKlB3YYuXU4dqvcqlXnlDr7WfKGTlGruBn5KtkeE4bBVu1DbgoxZqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره احتمال نامزدی هگست در  ۲۰۲۸: صحبت درباره این موضع خیلی زود است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/686028" target="_blank">📅 23:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdWVRs43c8sMPKldYaprs0-y0YDBeyFypGaokK8_5HoZTj-yVeYR7VZPOsw2aycQAojx904yg__aDwXxjqoru549W9ZbHvVITKqw6_coHfngjfnviPzfHVU59CQehDGTCqQtEKBq0l8q6dVam8Is-Jj-k-KPMqbNqorxnF1EZPohmlTtfjE3i9EJ0DCNDvzAFfRkFrqMFNnmPEh4rvnIyOcc4p77P7NQ8HvseTeuSH9ljhvrq0yNcuujlbZpd0bHnRebJQicEUhHS50vG2vS95ZheS1KDAwmKOuhg18QDUCQcZxS67vXg6I57QVuzVRItQrbNmQPbS7HKMSQd6WWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رابرت پیپ، استاد علوم سیاسی دانشگاه شیکاگو: ترامپ اعلام کرده که آمریکا کنترل کامل نفت ونزوئلا را در دست گرفته و این نفت قرار است ذخایر رو به کاهش آمریکا را دوباره پر کند
فقط دو مشکل وجود دارد:
🔹
اول، در بهترین حالت، سال‌ها طول می‌کشد تا این نفت به دست آمریکا برسد.
🔹
دوم، نیروهای آمریکایی باید از پیمانکاران غیرنظامی محافظت کنند؛ وگرنه آنها حاضر نخواهند شد به آنجا بروند.
🔹
پس فعلا روی کاهش قیمت بنزین حساب نکنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/686027" target="_blank">📅 23:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686023">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ترامپ متوهم: تنگه هرمز در وضعیت بسیار خوبی قرار دارد
🔹
رئیس‌جمهور آمریکا مدعی شد که تنگه هرمز «در وضعیت بسیار خوبی» قرار دارد و نفت زیادی از آن خارج می‌شود. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/686023" target="_blank">📅 23:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da02bc0ad8.mp4?token=r4CbFRpOl9G8AoccaSkpvlpDFaaG2VIeRp24t3GDmT6BsY9fq_Vg5gaHtDAmbraTf92etmOMFntRWXaVfcBPG94KjxMfzPgM7YjEq9dOJMloVnuzpLxKmggxl7zgBPxWBiKlnaTTds4SwMsVCItXJsQqUADdjCEXQ0sYeDOintcWUboJMZkb4lwYYWEEY__3ek7-l97vk5LB61wLYSe4rZ0xUF0PlINUf5FtywucMUpiF7afhnCstR5I6TAJEbHSwRDWovRr7YT8u5Q9RDydNlrMqn7vdxMu0jmIvzYViZCedJmJEymtWc3PeJLtGbnuntWE6nOjs5vJ_uOvMWK1Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da02bc0ad8.mp4?token=r4CbFRpOl9G8AoccaSkpvlpDFaaG2VIeRp24t3GDmT6BsY9fq_Vg5gaHtDAmbraTf92etmOMFntRWXaVfcBPG94KjxMfzPgM7YjEq9dOJMloVnuzpLxKmggxl7zgBPxWBiKlnaTTds4SwMsVCItXJsQqUADdjCEXQ0sYeDOintcWUboJMZkb4lwYYWEEY__3ek7-l97vk5LB61wLYSe4rZ0xUF0PlINUf5FtywucMUpiF7afhnCstR5I6TAJEbHSwRDWovRr7YT8u5Q9RDydNlrMqn7vdxMu0jmIvzYViZCedJmJEymtWc3PeJLtGbnuntWE6nOjs5vJ_uOvMWK1Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: تنگه هرمز در وضعیت بسیار خوبی قرار دارد
🔹
رئیس‌جمهور آمریکا مدعی شد که تنگه هرمز «در وضعیت بسیار خوبی» قرار دارد و نفت زیادی از آن خارج می‌شود.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/686022" target="_blank">📅 23:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686020">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf83a88f5.mp4?token=pQ_7Y0Pncp1W5PdmMSaR9zH1b0gUWgsTrGQwfmj8DepyQNcyRtHL4A3M3u15RcbxwUDByfrf7xnFvKmE_6vIy2KH1JVEtMjqsxh34-VhhnGQ88OpIOh-kwL1PZSx_dTvyGPQ2HD3zvQKUEAF-4rQ9LaxQsN6HqCmC8JofkLcAxGFb0qQT6YHpd3MpsKUpa5d-wEzcgvVMkMrHOQwEsY6IdRA1sastlc_Xa5e86oL6vc-FKMpDbYHrp0ko9U0R0bTur2TLaG8JkBDkg1eCSiUTgzveDrkO9yC6sK8_eBq6g3xzChVObth_qs_zOU2KOztLXL-TCx9v6nnEQdmscPqpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf83a88f5.mp4?token=pQ_7Y0Pncp1W5PdmMSaR9zH1b0gUWgsTrGQwfmj8DepyQNcyRtHL4A3M3u15RcbxwUDByfrf7xnFvKmE_6vIy2KH1JVEtMjqsxh34-VhhnGQ88OpIOh-kwL1PZSx_dTvyGPQ2HD3zvQKUEAF-4rQ9LaxQsN6HqCmC8JofkLcAxGFb0qQT6YHpd3MpsKUpa5d-wEzcgvVMkMrHOQwEsY6IdRA1sastlc_Xa5e86oL6vc-FKMpDbYHrp0ko9U0R0bTur2TLaG8JkBDkg1eCSiUTgzveDrkO9yC6sK8_eBq6g3xzChVObth_qs_zOU2KOztLXL-TCx9v6nnEQdmscPqpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات تکراری ترامپ تروریست: ایران یک کشور شکست خورده است
رئیس جمهور جنایتکار آمریکا:
🔹
نیروهای دریایی و تجهیزات آنها از بین رفته است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/686020" target="_blank">📅 23:23 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
