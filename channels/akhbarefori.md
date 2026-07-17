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
<img src="https://cdn4.telesco.pe/file/uhDvF0Gd3UEBtEBFl4Yp7Sh3i_muUp38zvdlXLEKhGwsCO4Ia8JfvG34n7f23tFfktpfRgkygpIhV9EDe_JocDXI037w3kc47LmuKryf5dRDQh6pRb7vApZMvyt9YWo7sTaQ3B4Le138NoBtqwFFM04DJ0-y_wx8KK71UMidxZ38dfLtUAVygO2-GAfzrMxg-IJEWKMp4Bv-o03ShPmVM3v-U9REKx8EBRwDZJcHkXLRwoDflmxT852VRvjgKHrAONAnk_15mMLOvMtILUjhDlz8jxqEL_2-er1RINOdbdc8KpLlMrtAjQEgKg0kCvB4lUzADkKyMbtWlCgTZyXukQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 20:31:51</div>
<hr>

<div class="tg-post" id="msg-672235">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مخابرات منطقه لرستان: اختلال در زیرساخت ارتباطی شهر ویسیان لرستان برطرف شد.
🔹
موگرینی: دیپلمات‌های ایرانی برابر فشارها خونسردی خود را حفظ می‌کنند.
🔹
قطر بر لزوم توقف فوری همه اقدامات نظامی در منطقه تاکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/672235" target="_blank">📅 20:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWFkG8psdkTnqIjHYEnNQbpGq7C7RPakXtk6Tts25er69DHefCNKovzWjvIs0g_pegqA55Xyh6U9nqRFjCrKZCIq2W16jOxHmLZ8cCdzhZ6XlbEKu0JYfnRtdZyCKeyx7O-urmlLdgJsscnjdEFV4_Sd-s8ahEQrj7OlgHtrNY1c7QLdJftu6sTD6FKcWhmQk2QzuHMPAOGPgCLohu39GVQjLO9vXsOLPROyKeU-nrl6yaGiD99w8s3OWquKrUIERaZqyW9mBQKqbyOtJ5xDQl6fAkb2HkseoUykmIUGn4mwiQ-9s2Hj4ummBd2D6Zp_s1GM-Ufnt9OaXt318urZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه امروز قیمت‌ها رو دیدن...
تو شرایط خریدت رو هم ببین
💎
اجرت از ۳٪
🏦
خرید طلا با هر بودجه، از ۵ میلیون تومان
🔄
تعویض طلای سالم با عیار۷۵۰
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
📲
داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/akhbarefori/672234" target="_blank">📅 20:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672232">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
یمن خواستار باز شدن مسیرهای پروازی از صنعاء به تمام مقاصد شد
یک منبع در دولت صنعاء:
🔹
خواسته ما این است که مسیرهای پروازی فرودگاه صنعاء به تمام مقاصد بدون هیچ استثنایی باز شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/672232" target="_blank">📅 20:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672231">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqwQ3Ru2ZXcg4GYiAau48MFCHwvDNMw-fX4g8zh52qHcas-UmjrX7jVX1L49GRin0Pgo34ZPidzEy9pF50XMkoqF7XXjJacQ-tOC08he7hnG6qQ4QfeWDbxI2rnwzKk0sUA5rGVtxGamLHmUvIELLW6w2CBui2IjecbVLdIvQizMHgYkfYzrwUsdFTjl86GJFwa4u-556w2cwjcipTZyDD9Kgeq4UgxFyG46S3hGoFcjt2wZNtPO6ZRfAqKkuzg6x6Ps6cbESeyweENzyWDvCHIuTZimvd8Og8rnay1gesmb8y28cxVlHOotqLtjqEYfQGeK5vOpy7s34vclq1t0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثبت نخستین تصویر پلنگ ایرانی در منطقه شکار ممنوع کوه‌خم فارس
رئیس اداره حفاظت محیط زیست شهرستان سرچهان:
🔹
حضور پلنگ ایرانی برای نخستین‌بار با استفاده از دوربین تله‌ای در منطقه شکار ممنوع کوه‌خم فارس به ثبت رسید.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/672231" target="_blank">📅 20:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672229">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehZG7ZOCInTlB7ftXqMHdVC8U-tXl6mZsfLZgEtoExVK17r_h2dNxGDg7cenPZaj3y_G5LsXcnB6kB0XKujzBnzVT0FIu4hP1AHPAs9Ii4WKbq9C8gb2loo1zc9RJ7ET206pPAyFK3lIh33G_mz5sxTcOCHMb9NZ_LGO32RZSppJBKXHM3M537qMWdrBTfD2F4HSoGazNH1kowkBUmRagC3eBNnO2rW7MF3m52RWds2ONNQ_dr5yP6wMjFoQTthAxv9FEj_K7fyihIYtB0pP5rHOfopn3H5cEzO5nq-irb2d6l6ON53DpXcJ1HwjN92LYs6qgcmXirJDHFUN46kf3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/672229" target="_blank">📅 20:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672228">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
آکسیوس به نقل از مقامات: واشنگتن در راستای پیش‌بینی گسترش احتمالی عملیات علیه ایران، به اسرائیل از استقرار هواپیماهای سوخت‌رسانی اضافی اطلاع داده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/672228" target="_blank">📅 20:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672227">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
قلعه‌نویی تا جام ملت‌ها ماندنی شد
رئیس فدراسیون فوتبال:
🔹
آقای قلعه‌نویی باتوجه به مشکلات و محدودیت‌ها نتایج قابل‌قبولی کسب کرده و همکاری با ایشان فعلا ادامه پیدا خواهد کرد./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/672227" target="_blank">📅 20:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672226">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از مقامات آمریکایی: ترامپ ممکن است در روزهای آینده دستور تشدید حملات به ایران را صادر کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/672226" target="_blank">📅 19:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672225">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e68436f0.mp4?token=qZB6l1XdT8PJ4KqIJT1RzprTqRRsYLkhupJwQ-KjeD9ITczjEFJv0JhlBiLvKK7U4FalFQlTS1i7wqWBHLFVq3VHcv5lVd1YOZ3y8kjZamr7QW8Q4oIOqupPApuJtt_xHVLIafY2jpaMwSdm9xCqIdo_q1i2LAK3xxjsahqTI-4hk4_NxBqD3QeAvUFlRm5Zn_2Akp1QzsoWQlxNCB1Vd41I3A_P9sfG7-Oi9ZDW7UW2VJ6eboPcvNguyogCRZiBkv0OcKDeTsUBlmysDg9ywu_OWNz3DxmxHk8gmcnbWI5zLAFzSLUQMWm64KnHnS-mJufXNBmfSYewCW7rSNYliQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e68436f0.mp4?token=qZB6l1XdT8PJ4KqIJT1RzprTqRRsYLkhupJwQ-KjeD9ITczjEFJv0JhlBiLvKK7U4FalFQlTS1i7wqWBHLFVq3VHcv5lVd1YOZ3y8kjZamr7QW8Q4oIOqupPApuJtt_xHVLIafY2jpaMwSdm9xCqIdo_q1i2LAK3xxjsahqTI-4hk4_NxBqD3QeAvUFlRm5Zn_2Akp1QzsoWQlxNCB1Vd41I3A_P9sfG7-Oi9ZDW7UW2VJ6eboPcvNguyogCRZiBkv0OcKDeTsUBlmysDg9ywu_OWNz3DxmxHk8gmcnbWI5zLAFzSLUQMWm64KnHnS-mJufXNBmfSYewCW7rSNYliQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از اوضاع تنگه‌هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/672225" target="_blank">📅 19:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672224">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4sWr6siHKM-4tixmapfwlNwZsRsOvM_7VG8WY2EWlinI4Oh7bLuL6flYPd3ko5jdOcjubOoq-BQfxR7ajPCfc7gIluvJUVKOKxDBrDraYNUCA8Rcw8uIoTOWU-IlKZT_ks28JGcl5Ei4iqaSSi_RasIq03ImVJr0JfzU-Dy5643uqlFYYKeHMxfa60Krc0QPci872vguBxv1uPf6ujV4d96JM154yCudI3TRJFWvvZcpeFVKHk_0wf6NZVAudausK4y370nG6ZigzES6KFcyOmOd2pmwBlqHM200L213T-n3KbkZIJrNb_nBKCR9bg1hcZK26cNaxawwPKoR4AITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یک فروند پهپاد آئروویرنمنت آرکیو-۱۱ در رامشیر منهدم شد
روابط عمومی سپاه حضرت ولیعصر(عج) خوزستان:
🔹
یک فروند پهپاد آئروویرنمنت آرکیو-۱۱ ریون توسط آتش سبک سامانه پدافند هوایی پیشرفته سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی در منطقه رامشیر رهگیری و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/672224" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672223">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC5qXIZvVQYvd_f8wRp-6ZT_8p2dtKUjLHdXyJvP02_fKZ9tVDO8JU8UcY-AV0X84NlidNSOlF1gIQVXf-Lwp2o2cNlMhc7c3klnBUEgp6Ry8m4Ob_9hEFLcY0QDKYm8Yw2eYeQg_JX0kWksrUY7n1xw31-fjWD04gKIOb7goA62B20LQCYgeqfBrHutyzLB8Oq8q8JzlM9idyJ3_s5_ipVMoGg9zCpxiipMobnUSdRhaEuQw8ZWBEKOOtpgRLp2pdThuhUUu1uSJJ9-JJeugccTtxxasuudGhMeDHcMImiQMBMRK5SdKEofzWT5gmi0ZAyyv0GMAknPDvNWs2bdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام یک انبار لجستیکی آمریکا در کویت پس از اصابت پهپادهای ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/672223" target="_blank">📅 19:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672222">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvBxRWocydVBHyJohwfgF7DnUbidU_2L_0WsduykWMQK9-gk2ZKvfdwlEFaxFiLvPJxCMSma0GOyvqZe2_XTImYmvyhw2dXSXwmICLu6SXbN5VcGa_hWqDZpWAxFG-XOd1EtbSMKBF6ohXDZKCUv5ecgDG4qdYCreXfS8pHdmBS-Y-2SjBGRrUcg4bfDCKrgyXKwcfxChPz3i43ewlqC4HbODJzXQf-NR9DEO0o8UcyC-cq-SbQI8QS42HzA_XIxhz8hDpwa2MpudB_ei2UR1MoXgdIKMrqhFylWfvzmtVqpJbVyT4K8BPTJU2Ksxl37GsAUWQUT5CBKI2SySWgsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرژانتین و اسپانیا در فینال جام‌جهانی با پیراهن‌های اصلی خود به میدان خواهند رفت
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/672222" target="_blank">📅 19:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672221">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حمله مجدد جنگنده‌های آمریکایی به برج مراقبت دریایی چابهار
🔹
صبح امروز ۳ انفجار شدید باعث وحشت مردم منطقه شد، اما منطقه مورد انفجار مشخص نبود. جنگنده‌های ارتش متخاصم آمریکا ‌برای سومین بار طی روزهای اخیر، برج‌ مراقبت دریایی بندر چابهار را با شلیک سه موشک…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/672221" target="_blank">📅 19:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672220">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZbDzgmrFjlxNaGHtuFRPIsQ1dZ-ANupuTqwnOMJ6Vn4yakpbA1uxOL2Q01EkHmwfdnv7cuqKpoWJ8anRbLJqKqanonW4D-GWFWh1qwcQVAyRiJk6AdRWLN79Su7PiufE4b5PxtyxZ5NkUVMZKwbf76saMuPqI-y5uR3G-9QgfxXWV0AVs66lWWm5ZxkxsZp0Y0KemnidsY917tq9k27Co5oF2QM-guYZVO40-ED5BOgclzGuh_H8VkfXjvf0SlFf4Q1o8Hg92geIWsmXIM0LPg-r82vDzo5s_huVfzmXfhRu-acAZja7dxobcN63KXAqxeAGq5mUyNrerCIA542MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش یحیی‌گل‌محمدی به حملات آمریکا به جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/672220" target="_blank">📅 19:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672219">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZzhkCy4H8Vmvz6Nvxxs0tkFDkv7Oz11wEvnQcZAJPy2gw0RkP8ahUn3i2N91vHozrsg3ycyZuhJ1FcllzcHQOgJkmvGyadRbINojEJKYwvDaDwguKpm9bYEW1_2P3-zQgrE9EuD8Jp38SFORpqiUzKnh0NhRNs22zSvhxCQb3-boxv6ajxZham0m3-Ed6nXya4aZ5KE6hA1Nz_cvj6X0AWgu_8tz5XxBMOUZ9NBjr6-JxJ_EOIXSDXA80qHnMLLt45-DX2MfdMUbrqWCUX6-AJ_glwGKI5aaj6eWkG2NCwy54hsiz1uY28TNJnGW7fU-l_IRY6BGrhYEFZTcjfbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست‌های ترامپ هم اشتراکی شد؛ هرکس پول بدهد زودتر می‌بیند!
🔹
شبکه اجتماعی Truth Social در حال آزمایش سرویسی به نام Truth API است که به شرکت‌ها و معامله‌گران اجازه می‌دهد پست‌های جدید را چند ثانیه زودتر از کاربران عادی دریافت کنند.
🔹
منتقدان هشدار می‌دهند با توجه به تأثیر مستقیم پست‌های ترامپ بر بازارهای مالی، این کار عدالت را زیر سؤال برده و رانت اطلاعاتی ایجاد می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/672219" target="_blank">📅 19:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672218">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da8847885.mp4?token=Knt3X3RlhxCG-8iUjIugmSRc3uq9aNazw_hj8Lox2VTSbTendJYeXNF_LbrR4VvFQ_2YiDF7Umw-NZzyDJ2kKdouHfJTcWzkPbrtWqWV98UGQExr99W_njAlo2HjJ3Si3bZVl22LmCnAAxpe0d2Lfnha7dIh3PRYfnDe7IOXUQi9PzxbODGlEVvJV66gw8L5ayrwUS2FwIh_yjCZNeUsBNUHISfzYJNWLTNcsuaV_Bw0R1LDZwHs9f4jcXi5VaHH0Gjg4BEQuTH-AynreQTyOxU7QO5XPmWP8zhhlCivC0Brw_yPcWkRbUjg8WeO1q4XOCj5LLZBt3gqKqJh55ajNzKtx_WvNzEbWOLHn4BOUajvrWRhG35DjtTIrPrOTUkcSOXp9HAHEyq4K1YJlfRggXtC4t1TPeLG1kEo2GSe8jnpO7pA6vxmrlT8LhQ4HlyMfWu6pMhRi9jgkiRVvDiNP8Rq5VxFpqdJuqsm71ZvioDbxSAOsazNt5EkvQfRk0KN8-cB0VfJ-oBNa-JWXVOimViW2QuQRdJ2Cpae-izzsFSt8SNslACDYMLfT6VbhQBA9-MTbjwqFGKelOtSEnO1xWA6QGbAhhYzIWM_h8Obnn1-k7FOslXh1OCkGwCB7SL62whmyxyggCtaYZHtiAt-WtW_zc_WT64C2iCPIJleR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da8847885.mp4?token=Knt3X3RlhxCG-8iUjIugmSRc3uq9aNazw_hj8Lox2VTSbTendJYeXNF_LbrR4VvFQ_2YiDF7Umw-NZzyDJ2kKdouHfJTcWzkPbrtWqWV98UGQExr99W_njAlo2HjJ3Si3bZVl22LmCnAAxpe0d2Lfnha7dIh3PRYfnDe7IOXUQi9PzxbODGlEVvJV66gw8L5ayrwUS2FwIh_yjCZNeUsBNUHISfzYJNWLTNcsuaV_Bw0R1LDZwHs9f4jcXi5VaHH0Gjg4BEQuTH-AynreQTyOxU7QO5XPmWP8zhhlCivC0Brw_yPcWkRbUjg8WeO1q4XOCj5LLZBt3gqKqJh55ajNzKtx_WvNzEbWOLHn4BOUajvrWRhG35DjtTIrPrOTUkcSOXp9HAHEyq4K1YJlfRggXtC4t1TPeLG1kEo2GSe8jnpO7pA6vxmrlT8LhQ4HlyMfWu6pMhRi9jgkiRVvDiNP8Rq5VxFpqdJuqsm71ZvioDbxSAOsazNt5EkvQfRk0KN8-cB0VfJ-oBNa-JWXVOimViW2QuQRdJ2Cpae-izzsFSt8SNslACDYMLfT6VbhQBA9-MTbjwqFGKelOtSEnO1xWA6QGbAhhYzIWM_h8Obnn1-k7FOslXh1OCkGwCB7SL62whmyxyggCtaYZHtiAt-WtW_zc_WT64C2iCPIJleR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاد بگیر مثل سرآشپزهای حرفه‌ای مرغ رو خرد کنی!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/672218" target="_blank">📅 19:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672217">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پیام قاطع وزیر دفاع یمن به دشمن سعودی: تداوم محاصره بی‌پاسخ نخواهد ماند
وزیر دفاع یمن:
🔹
ما به کشورهای متجاوز، به ویژه دشمن سعودی و کسانی که پشت آن در تحمیل محاصره هستند، هشدار می‌دهیم که گزینه،‌هایی برای نیروهای مسلح باز است.
🔹
ما بر آمادگی نیروهای مسلح برای اجرای هر دستور فرماندهی در صورت ادامه محاصره علیه مردم یمن تاکید می‌کنیم.
🔹
سطح آمادگی در اجرای منویات رهبری طی روزهای گذشته بالا رفته است.
🔹
گزینه‌های ما باز است و در همه نوع و تشکیلات نیروهای مسلح آمادگی بالایی داریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/672217" target="_blank">📅 19:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672216">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330fbcbd73.mp4?token=pcvghnLQnyd3ZZtxq-Q0O9GxpS-Rswywoxvg6nj_hU4z_RuOyPnvBYmJeS2vODsHkgx-umO4oJe1yDnBR5zI9G96nlquYXCnkC6J_QtCofmHUSy-OYTGAME_R9ur7wELXqxcOoOtm3gO4zGqP40Wep5kk5sTZ8PYDWg4wN6sb-gMxem_c0C3qv47jY6azlWyqrCNgi7bn2z92_lvmgJxk9emjVjvaiALQbYEP6dhYAyM4K5nxV_7oDOi0AKzXhnsMZxrB6VWSVPTJ9O7-Iptxsodo9UfuLunhKEsy94xEYMX7IK--92hEan3CEqjFmuKSwO0uCztQ-t1SZxRkWL5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330fbcbd73.mp4?token=pcvghnLQnyd3ZZtxq-Q0O9GxpS-Rswywoxvg6nj_hU4z_RuOyPnvBYmJeS2vODsHkgx-umO4oJe1yDnBR5zI9G96nlquYXCnkC6J_QtCofmHUSy-OYTGAME_R9ur7wELXqxcOoOtm3gO4zGqP40Wep5kk5sTZ8PYDWg4wN6sb-gMxem_c0C3qv47jY6azlWyqrCNgi7bn2z92_lvmgJxk9emjVjvaiALQbYEP6dhYAyM4K5nxV_7oDOi0AKzXhnsMZxrB6VWSVPTJ9O7-Iptxsodo9UfuLunhKEsy94xEYMX7IK--92hEan3CEqjFmuKSwO0uCztQ-t1SZxRkWL5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرزو کرد که آرزوی پرشیای سفید پنوماتیک به دلش نماند؛ اما ماند...
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672216" target="_blank">📅 19:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672214">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebff8c971.mp4?token=saBkTas-FILavmj6pFT02VKjL3R9qvwRFpFreB9GFLhtO1K_tj21g4UQ5UTppBWd0C4muk84ML8Xb6qeBJx0cLg9wHI-93WnrO6tYcJZmCBlANHA5jy6vXEW_CzFkWfhr7mUpHRfvah3jnv6SQfYfX96ibqaKaagF1X5TbOqUj2qThAEzRVxOvRNxcU5YdJjYp9tlvakFxeIBD-dyIr6tf5kzj-7vB3qBOSE7Jm_-A28NYXo5adiI0tKpKLZ5FLGyTqxnm-Vqzfdq0pIeT2FW3GQWR40kMdxP-ecS-I-dhu44BA8JGzRvbW4--9v1RP55cpi0vC84YGzDtytheayDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebff8c971.mp4?token=saBkTas-FILavmj6pFT02VKjL3R9qvwRFpFreB9GFLhtO1K_tj21g4UQ5UTppBWd0C4muk84ML8Xb6qeBJx0cLg9wHI-93WnrO6tYcJZmCBlANHA5jy6vXEW_CzFkWfhr7mUpHRfvah3jnv6SQfYfX96ibqaKaagF1X5TbOqUj2qThAEzRVxOvRNxcU5YdJjYp9tlvakFxeIBD-dyIr6tf5kzj-7vB3qBOSE7Jm_-A28NYXo5adiI0tKpKLZ5FLGyTqxnm-Vqzfdq0pIeT2FW3GQWR40kMdxP-ecS-I-dhu44BA8JGzRvbW4--9v1RP55cpi0vC84YGzDtytheayDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور و مرور زیبای تنگه هرمز ببینید
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672214" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672213">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGcHuSOvYreQZzsopa1TbKXKFN5Qv-USJei1JXpifnDPw00LEc0w30HNQ7e-o6TiPyBR9hIrSWChADcSyC8TEDrlXwQpWfJro2wWc0HUxlkLbVJSo843t6JgE7SdfRsnytXKYhHsQ6AlBwAyiwM1hfgl7bhL7ocks1qY8XfewMXX-ippCbPgmGoaG-2J3g8lbxgqpRiMTZraPKYPysLg1VnSnG4J8e5YsiWUMWGlHEmmLfNDtEyN0nxPkFobUM30xrc861JOuUs1xnZSjUEgWJ39aEdM20tr1SJ_Qie9y9hmdGGAdVUXiXMSypC6tu-SK7zT2XLSoy83QOvmDjG55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
https://khabarfoori.com/</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/672213" target="_blank">📅 19:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672212">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06710ec42.mp4?token=lJG7633Y_OgGpoNT8TZOu4lW-7FLwbt6kt6oJ0BT-oRoFvDMnAdYkbSmzuUh88PZOYFgfXQgEwjV1RFCIbFpS2F4wpX-QUm8sP7nuMUW6Owi0NNJcaczeh7soWz4XeUuxX9IBoCOO50fLxNsBZPbp_eOFetjqDahceR03ESfvRl7Q1og3J5lzXKACgTtkvAq39LNYz0ezQU28--BnX11519Qx4yaD0zF5WyWKqJIblieuMvS5-4zb6T52ruu4z34CMCfWalMI9wgZafSOq_Cgme8UbyG7VSULg8kJwIUPfGcyutugZ_RYYQMB4qrnredMEuRBbxE_HQNAPk2nqEPIUsBCDrc1JIYDkZnZrykYxCe2MUhdX7J358n4TWvZYqmbHKJFShtQHwpQ-sBDTOF3T23Pw_OV_TfC_qb5mxFOb4qK3Zxjd1VS_u7mqRQagKY2YggQlAbAFZoBq_nFx8t99VGWGGBndz8_UZrRQuGgvJFffpBK-sK73-RNigiZlOyeRq4RMvRysekkuNURov_r1ZfQT3HAb8Vj1UTIvdiYsdZQiRGpKAlSBmkXWMeV0Mds6PJ8qdowfqgc8yt2CT8EIn3zw4cWzh_Y8EE287ZGvX6cU_Go7jL8_HLxzNUJqO0pqn7IzJgthUJ53MV-18ZXscRO4ud9_XxWk7w2MSXD7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06710ec42.mp4?token=lJG7633Y_OgGpoNT8TZOu4lW-7FLwbt6kt6oJ0BT-oRoFvDMnAdYkbSmzuUh88PZOYFgfXQgEwjV1RFCIbFpS2F4wpX-QUm8sP7nuMUW6Owi0NNJcaczeh7soWz4XeUuxX9IBoCOO50fLxNsBZPbp_eOFetjqDahceR03ESfvRl7Q1og3J5lzXKACgTtkvAq39LNYz0ezQU28--BnX11519Qx4yaD0zF5WyWKqJIblieuMvS5-4zb6T52ruu4z34CMCfWalMI9wgZafSOq_Cgme8UbyG7VSULg8kJwIUPfGcyutugZ_RYYQMB4qrnredMEuRBbxE_HQNAPk2nqEPIUsBCDrc1JIYDkZnZrykYxCe2MUhdX7J358n4TWvZYqmbHKJFShtQHwpQ-sBDTOF3T23Pw_OV_TfC_qb5mxFOb4qK3Zxjd1VS_u7mqRQagKY2YggQlAbAFZoBq_nFx8t99VGWGGBndz8_UZrRQuGgvJFffpBK-sK73-RNigiZlOyeRq4RMvRysekkuNURov_r1ZfQT3HAb8Vj1UTIvdiYsdZQiRGpKAlSBmkXWMeV0Mds6PJ8qdowfqgc8yt2CT8EIn3zw4cWzh_Y8EE287ZGvX6cU_Go7jL8_HLxzNUJqO0pqn7IzJgthUJ53MV-18ZXscRO4ud9_XxWk7w2MSXD7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابستان گرم هست و همه نگران پایداری برق هستیم .....
🔹
این ویدیو را ببینید تا زاویه دیدتان به زندگی تغییر کند....
👆
🔹
ببینید اقوام ایران چه درخواستِ مهمی دارند....
😊
🔹
اگر میخواهید همه چیز را دقیق و موثقی در مورد برق بدانید.... در این آدرس‌ها در پیامرسان بله با ما باشید
ble.ir/bargheiran
ble.ir/tavanironline
اینجا همه قرار داریم ....
قرار همدلی
🫶</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/672212" target="_blank">📅 18:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672211">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
زمین‌لرزه ۷.۴ ریشتری در جنوب غربی مکزیک
🔹
زلزله‌ای به بزرگی ۷.۴ ریشتر در جنوب‌غربی مکزیک رخ داد.
🔹
تاکنون از میزان تلفات احتمالی گزارشی مخابره نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/672211" target="_blank">📅 18:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672210">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
بیانیه ارتش: ۱۱ عملیات برون مرزی تیپ ۶۵ نوهد ارتش مقتدر جمهوری اسلامی ایران در خاک کردستان عراق، با همکاری اطلاعاتی گروه‌های هم پیمان ایران، ۸ فرمانده میانی گروهک‌های تجزیه طلب را حذف و ۳ مقر را تخریب کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/672210" target="_blank">📅 18:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672209">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnXcDnS-CRXmatTZPFbQ_EaPxWN0j9PJShIUwuFmFyygCNQo7d5GKBiSNtgxHSfa_JbjfJFkQV8R-rWSuReoNy5qwB3xG77uzvkyTNI8uHBkoe1gmMG17zMjypxFq9parlnBx9B_4Z9RsllsDQvfMUc5LDAgJj0voD3BPNJ89M0tWjcvNnRj_dik50Ea-t4V1ke2twRCfhFZXVqGjDVUzCur6oNTmDkUQX9DT3taIFyrLXxZYjzjpgBE4_lTwTe_b_IZPT5a8f5NS6Xmu5yXXOnJ8t7b1q78iz_4Bfq4PsNWeq-0P_2egVWkE5iOUIGSApBgsNN19ZZGxPzsF3RcAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تظاهرات میلیونی امروز در صنعا، پایتخت یمن
🔹
اعطای اختیار آقای عبدالملک الحوثی به نیروهای یمنی برای پایان دادن به محاصره یمن و یمنی ها از سوی عربستان در دریا و هوا.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/672209" target="_blank">📅 18:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672208">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDRpkbI9gnyQICoDzobCR2uXgJUIf_XR9Cgq6QPg6kinMoYqeOyTW4p2tD1sE5ic1DZr7pNG-WS_Vqyo38nlCmYFe5HuVkTboXnYhQf1LkphiAEDSUTVQx5JYQwl46feo1qW3Wzg4idINp92XvhZgeXqsdnEMvZCyZ4xWzEVnbWBr34VRFBfLQWWfcBngikOuaDAac4MqwjfB_F-APzaM-phHexdDDAW7zeEA9ijN2EWEYFvInkBU3hUIbO5wdu0GBVye0PwJwLc-hrFgeRijUMDMOKIJG9elobIqWOO_Q--stJeeC2dI7qcPTnsultn-9IB0e-_ThQYrf-G9n4Qcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیراهن نمادین پله در فینال جام جهانی ۱۹۵۸ با مبلغ ۴.۹ میلیون دلار در یک حراجی فروخته شد
🔹
پیراهن شماره ۱۰ برزیل که پله ۱۷ ساله در فینال جام جهانی ۱۹۵۸ بر تن داشت، به ارزشمندترین قطعه از یادگاری‌های پله تبدیل شده که تاکنون فروخته شده.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/672208" target="_blank">📅 18:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672207">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت خارجه هند: پایانه بندر چابهار در ایران هیچ آسیبی ندیده است.
🔹
ادعای آماده‌باش دیتاسنترها برای قطع اینترنت صحت ندارد.
🔹
ارتش کویت: چندین نفر از پرسنل نظامی ما در حملات اخیر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/672207" target="_blank">📅 18:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672206">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
معاون استاندار بوشهر: یک نفتکش مورد اصابت موشک آمریکایی قرار گرفت
معاون استاندار بوشهر:
🔹
نفتکش بلما ان آی ۲۲ دوباره مورد اصابت ۲ فروند موشک آمریکایی قرار گرفت.
🔹
این نفتکش که تانکر آن خالی بود در جزیره خارگ پهلو گرفته بوده است./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/672206" target="_blank">📅 18:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672205">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تردد‌ها در تنگه هرمز کماکان از مسیر ایرانی است
مرین ترافیک:
🔹
داده‌ها نشان می‌دهد که ترددهای تأییدشده در تنگه هرمز، به ۸ فروند کاهش یافته است.
🔹
از ۸ عبور انجام‌شده، ۷ مورد از مسیر آب‌های ایران صورت گرفته است.
🔹
هیچ ترددی از مسیر عمان ثبت نشده است؛ همچنین هیچ گونه جابه‌جایی از سوی ناوگان سایه مشاهده نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/672205" target="_blank">📅 18:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672204">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
صعود پرسرعت قیمت نفت ادامه دارد
🔹
قیمت نفت در سایه تشدید درگیری ها در خاورمیانه، به ۸۶.۵۵ دلار رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/672204" target="_blank">📅 18:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672203">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe3776c2d.mp4?token=V1tt044jy0OilVUz0qCq1zFNKaOAjvrja-PGuKyxXE4IcO2pX6KCHN0YDBJ9o-zchnb0036FcEUtiXNFMrfOTQqWaW6dddmRlGB1Kf0fALb6TZBGxZxQ8LanyVD6r2-LeAFRnrWq3rxAOrEKbyFxHwTiRcarIDC3tUm8kcug1SVa1SxF8lYqy7wY31my7arEuQYuHo_xMobL0pZeFWzjHHeTvoeYl2KTgTp9hC4YPQvrcZVmLf4OO4pBhqsBby21M-tQjJcFERecUSLnunYjuzLKByCIo5fAk3MtR_NOzbvfpUdb1Syk4O0AhzVMg55kOPmZQptjJ_xarFZyE3nKQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe3776c2d.mp4?token=V1tt044jy0OilVUz0qCq1zFNKaOAjvrja-PGuKyxXE4IcO2pX6KCHN0YDBJ9o-zchnb0036FcEUtiXNFMrfOTQqWaW6dddmRlGB1Kf0fALb6TZBGxZxQ8LanyVD6r2-LeAFRnrWq3rxAOrEKbyFxHwTiRcarIDC3tUm8kcug1SVa1SxF8lYqy7wY31my7arEuQYuHo_xMobL0pZeFWzjHHeTvoeYl2KTgTp9hC4YPQvrcZVmLf4OO4pBhqsBby21M-tQjJcFERecUSLnunYjuzLKByCIo5fAk3MtR_NOzbvfpUdb1Syk4O0AhzVMg55kOPmZQptjJ_xarFZyE3nKQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله جدید ارتش رژیم صهیونیستی به مراسم تشییع شهید در غزه؛ ۶ نفر به شهادت رسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/672203" target="_blank">📅 18:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672202">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f1d97831.mp4?token=mEWAA9V_N-nnjFeakNoheKov1xgfRY3sihZFuhroCQ8c7aHip46L7xJAEyU57HLvLac0hpnndpQznEMld09ub7y63NAGgZGLl705AuAyTUXMYYRkb8aeo1JNbGtJaJ0-wrNoJ9BoZ2_gniSIkzH3aOenZTCqtM8t6jvmwLE09wYoOTr9_f3JCpZjp9TAZMSrgzKWoJfOEBvEHPYXMOYJn2UDL_azsV1hi4kKyJ6UPbDOfH6U32PimTbjAZ4N_sOFwloYYv00DQ7g0lyrBGc1x-6i5QXzhvgKEu3cMy9YPqu8s9dzI9sWfHbhGtHCOgkj95BvhTDFnXILCqzOxgllekmUs1cQuf7o6bxYtV8a8O7DskEoLBzi_56GbeEIzwoQ6mcO5rlWOCdxHY-PG0l3coRSK2v2XCgHVwSjgsWeZA0V2bO7kZBvLA-PDVpegDEXHGV7Ols7ATQotdT76RyLDlkvaghD3D1dg4KHQrj8LAr3NT97kiDTFDPr8CFvs5aCV7n5q6BL5KlZOTX4UlFGKZwJJhxqqGoJYqSa-0SmBoIQzd3vkUooynsNWRtcxcfxiw_Oq0CfTS_58iR_0sCH1AS-giQrGaGROiDug_HdSMiqmMuf7x9qcFOS_BifMZPk_SY7oaM84Ol7Lw1Ag_-YZIhcI5ZosZAMIzx8GLp04xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f1d97831.mp4?token=mEWAA9V_N-nnjFeakNoheKov1xgfRY3sihZFuhroCQ8c7aHip46L7xJAEyU57HLvLac0hpnndpQznEMld09ub7y63NAGgZGLl705AuAyTUXMYYRkb8aeo1JNbGtJaJ0-wrNoJ9BoZ2_gniSIkzH3aOenZTCqtM8t6jvmwLE09wYoOTr9_f3JCpZjp9TAZMSrgzKWoJfOEBvEHPYXMOYJn2UDL_azsV1hi4kKyJ6UPbDOfH6U32PimTbjAZ4N_sOFwloYYv00DQ7g0lyrBGc1x-6i5QXzhvgKEu3cMy9YPqu8s9dzI9sWfHbhGtHCOgkj95BvhTDFnXILCqzOxgllekmUs1cQuf7o6bxYtV8a8O7DskEoLBzi_56GbeEIzwoQ6mcO5rlWOCdxHY-PG0l3coRSK2v2XCgHVwSjgsWeZA0V2bO7kZBvLA-PDVpegDEXHGV7Ols7ATQotdT76RyLDlkvaghD3D1dg4KHQrj8LAr3NT97kiDTFDPr8CFvs5aCV7n5q6BL5KlZOTX4UlFGKZwJJhxqqGoJYqSa-0SmBoIQzd3vkUooynsNWRtcxcfxiw_Oq0CfTS_58iR_0sCH1AS-giQrGaGROiDug_HdSMiqmMuf7x9qcFOS_BifMZPk_SY7oaM84Ol7Lw1Ag_-YZIhcI5ZosZAMIzx8GLp04xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از سوراخ ایجاد شده بر روی کشتی فله‌بر تایلندی بخاطر اصابت موشک نیروی دریایی سپاه در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/672202" target="_blank">📅 18:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672201">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrTuc-hg_iH8urBI2ti0464kFcsL0PvvET8WilaEe3vDuDM4uqKFKVXKHMOhpCbRcHAAD_s3J_J8z7b1i7DuHMB527siUQTGCQvX55o0Ny6gVsEfBD48g9m2ZhcuBm84Tuz3-HmyJ5e_zgFTCKS9cf8ts6YvZV73XfryzRjFPOmdwp0Pw-UzedHLTFJUNBRItDSAMyv2g7yyXXblmc1LjYk_KDv_xk2fI9nPvzYjiKIkbPO9pAQhdfEa2NWIjzeWNVyXyBVhD38EN_hUT2Xq5-rhXyCqETplxwiimEq5qwvsUZ_lAWwRbFaf3VjVidodOtFnY7j9aI3lV2VTpNVDmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهی نیروی دریایی سپاه:
آمریکایی‌ها هر لحظه خود را به ساعت صفر عملیات علیه یگان‌های دریایی سنتکام در آب‌های منطقه، نزدیک می‌کنند.
🔹
انتظار بکشید...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/672201" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672200">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da5fcca64.mp4?token=fMHbpccf8bNxpNAn7CQttMfGmstSrUflSA7wlZoo6sXJ74A9ltjM6icaTkwyp_KNTPO7eQnXgLP-YyeutPxlj1NKq4Un9PPHLD73FS9X-A6uFKFgOnMmfEhpzMYM6rw9Wd68xa6aJ0_pIAjXNRIld9-buSBhQ7jmOnKcxoZZYMIv5GZioXFUMLC9pzDOiLMoBEsTkO2WDD2UYoXNUJ1BWX0IUjuGq5eN44-d_cxoQjuhoVfCL40hnGY7BOrvt7jLLanltANlhdy7JPndDgvSoR-S3wLc58_cllzr95bmtbpUaRdQ6ukpuwLsytFAk1UrWBVLb85CNMoLTQTozRoTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da5fcca64.mp4?token=fMHbpccf8bNxpNAn7CQttMfGmstSrUflSA7wlZoo6sXJ74A9ltjM6icaTkwyp_KNTPO7eQnXgLP-YyeutPxlj1NKq4Un9PPHLD73FS9X-A6uFKFgOnMmfEhpzMYM6rw9Wd68xa6aJ0_pIAjXNRIld9-buSBhQ7jmOnKcxoZZYMIv5GZioXFUMLC9pzDOiLMoBEsTkO2WDD2UYoXNUJ1BWX0IUjuGq5eN44-d_cxoQjuhoVfCL40hnGY7BOrvt7jLLanltANlhdy7JPndDgvSoR-S3wLc58_cllzr95bmtbpUaRdQ6ukpuwLsytFAk1UrWBVLb85CNMoLTQTozRoTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترس غربی‌ها از حق وتوی ایران در اقتصاد جهان
🔹
حقی که اگر تثبیت شود، رفاه و امنیت را با هم به ارمغان می‌آورد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672200" target="_blank">📅 18:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672199">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16aeb874a3.mp4?token=qFLg-_Zm7D_14iPOLfts1OfpJmFQqjWdX4gcHnLaAOvgEOYdbP8yIazgssBXOYGZMQee7C15gPaabgdk-BeOFeL4ZJgJRwZ7f1hmg8XWJj_ClMToXb5Cfo8aquS546YNNO_g456UvFwLV6PLJIHhDubruRhGRG1jbcijtx_4asIzoTreHJg7DBzfmhiwlLMfndHfX-73PxrJPcI4SMjYCiBoJp5gdmdSTGR1GCCXh-nvGi3-EZUzR4o3BSMdhbPPGk5eCs18rcqIU6_9djVelmlCLZ0f3c0-VlFQ2SCngfyQGRM5E2dmEHxx4BNjDT5SAKQQr6_5KXDqW6skD5Lq2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16aeb874a3.mp4?token=qFLg-_Zm7D_14iPOLfts1OfpJmFQqjWdX4gcHnLaAOvgEOYdbP8yIazgssBXOYGZMQee7C15gPaabgdk-BeOFeL4ZJgJRwZ7f1hmg8XWJj_ClMToXb5Cfo8aquS546YNNO_g456UvFwLV6PLJIHhDubruRhGRG1jbcijtx_4asIzoTreHJg7DBzfmhiwlLMfndHfX-73PxrJPcI4SMjYCiBoJp5gdmdSTGR1GCCXh-nvGi3-EZUzR4o3BSMdhbPPGk5eCs18rcqIU6_9djVelmlCLZ0f3c0-VlFQ2SCngfyQGRM5E2dmEHxx4BNjDT5SAKQQr6_5KXDqW6skD5Lq2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دشمن آمریکایی با بمباران پل کهورستان در محور بندرعباس - لارستان به هدف خود نرسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/672199" target="_blank">📅 18:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672198">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5UQm9Pje6I1S3UW3ZZbCjf52Pw4OYpsfNaKwW2VoeEG9_6k0-6jcQFzO5PDK8I76vMnIhU74Z4OU-pte7dJ4Y7AUS1w_-waAMp5XRNqKFcnZaeoYO5Zof4GILvkWKSZ2wQD8bZww6aZS4CM7yTKxMZORNtgHHwCziuF9_FBg6YepJ_qxHy6h2IYWaWEoec4NSbONdE8B4yRHUkTUPeMDGEXrkEHRp7qQLDWdVXWumjQjohlyFudE53A2aMCpr-LpubCFpJK3Wp0b4BdejhxE96TDDIy-mFzeWL1AM8Ac467YwMIs41SRT5ULjXUwD2YmRS4-TXiDyPXSvW1Z0yNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شدت حملات آمریکا به زیرساخت‌های غیرنظامی و پل‌ها این تصور را ایجاد می‌کند که ایران به یک هدف بسیار مهم ضربه زده و این حملات در واقع واکنشی عصبی و از روی خشم به آن است
کنجکاوم بدانم آن چه بوده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/672198" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672197">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vma5ocxFQEiLC5LFq9WOw9deiD93a9kU8ig6dqsIRXcGKgD5L-yl9QjCIj7zqadaVSgUmK-xjBqchsLei-ImQETSoyu-5shltYwbzOAlmA8v7qM1JnwwiRSxOx6USk0ggNqyKwncc5P48dps8R-egXkm4yf5QLoftluVwYIIjiWVABHaernY8VzNvIfzxroJaWuJ8MhkRKs2Rhn53IlpI-CE5vW5jROKgD75o1M2XM1v5670WdnbVaGTO6ENX7aW-Yusbh7RD_zj9gOQNNbnqB1KOeg6MUkNAc9D4-qn6CnAT7axmtVic3OvZam3gGMiw-6d_uj77s9RbgxPHNP2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت ابوالفضل بازرگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/672197" target="_blank">📅 18:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672196">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a84b28869.mp4?token=tGytKabP5xV9gmRhsSS0GsVcQ6YsO4NzpekmHfm2vOvrqbENe6suEQ3uGxvviYEgLxjxr0Fp0s_-Z44OZlbH8kuQTNi-Vk-Pi_r1J10xZxDC9_7HnRgpSD4ThTrZ-9IORZrHSrQ02lfi6XJTodcAwOru-tEEm58qkq-7qk4mUZG_DvbUdvDjILvJATCSIWwCjwz-eCJv3vZ6on5iiJojDUwMMzqaGsvu9qbb2CWotbZ26RDiuMK1iubsAHg-UjHgQmVgcEEWrZ7pnduUSf47kDbqXowtzSHldChSXefHbOvVB1lnxps_Aym3l37fS5C4ezujymbgZKzZ7V_4KmRHPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a84b28869.mp4?token=tGytKabP5xV9gmRhsSS0GsVcQ6YsO4NzpekmHfm2vOvrqbENe6suEQ3uGxvviYEgLxjxr0Fp0s_-Z44OZlbH8kuQTNi-Vk-Pi_r1J10xZxDC9_7HnRgpSD4ThTrZ-9IORZrHSrQ02lfi6XJTodcAwOru-tEEm58qkq-7qk4mUZG_DvbUdvDjILvJATCSIWwCjwz-eCJv3vZ6on5iiJojDUwMMzqaGsvu9qbb2CWotbZ26RDiuMK1iubsAHg-UjHgQmVgcEEWrZ7pnduUSf47kDbqXowtzSHldChSXefHbOvVB1lnxps_Aym3l37fS5C4ezujymbgZKzZ7V_4KmRHPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا تنگه هرمز خط قرمز است؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/672196" target="_blank">📅 18:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672194">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d7ddd4f3.mp4?token=CuyfqA3PbXVHGUUWX3HaOZRC_vXJgxTdL4aXcLWIZeuxCD31z5Mqu7Vlh_FuW_foPdNuXbZIIRTcj_TH1pny8Qmxg8a2UKIaJ11Oh02WMr5rXq3vTA3r-nrgs5sArrZj1_cJCHSOiQQyDmSFRa3GBHX5lktB483pmNoD3K8fw7U-zn3tvTkG7DtFO5YkjWZSIlB9xc7B7IkTtJpB2abO8zNwYgpn2gFVzm1zQTs4mYG4L4nCYn6hi4a-4ZJDBK4PKHJBlbzSH8tsu4UUz81tMunfJ7zZnssNPlVUZysVIDFLxBVDHTCFZ_cz-fzn0mOY8gLrwwUmOjkS8kx57dYU5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d7ddd4f3.mp4?token=CuyfqA3PbXVHGUUWX3HaOZRC_vXJgxTdL4aXcLWIZeuxCD31z5Mqu7Vlh_FuW_foPdNuXbZIIRTcj_TH1pny8Qmxg8a2UKIaJ11Oh02WMr5rXq3vTA3r-nrgs5sArrZj1_cJCHSOiQQyDmSFRa3GBHX5lktB483pmNoD3K8fw7U-zn3tvTkG7DtFO5YkjWZSIlB9xc7B7IkTtJpB2abO8zNwYgpn2gFVzm1zQTs4mYG4L4nCYn6hi4a-4ZJDBK4PKHJBlbzSH8tsu4UUz81tMunfJ7zZnssNPlVUZysVIDFLxBVDHTCFZ_cz-fzn0mOY8gLrwwUmOjkS8kx57dYU5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از گرما یخ رو بغل کرده
🥹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/672194" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672193">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FylQbTfffNgmoMzzDsVPklGsmwovYXXI0uk3ZRy0r4hIfyi6R-dnHUrIB78jlcdHaAo255BFdA1eV4LYlbBGBNKLdtdiSslkB4sf2AZb8DAmIDdrAHoyWnf8KuIf43x46DbFns1n6roJ2eos-A1JCmXq-zhy9n1Rp9qvIC7tw0RrTmjOATyJkH0hnwDaZVPE33QJHk3hHMnwq5d03KuN5Y8269MmkDJJ9BVr-Q_z8FPr9yIujTkdJT7YmIgtJxgWD6ieAxxMtPGHg0yteL1F5JcIX9OkyrVv7u0ui58abFgqaxINKoQHwLreUZ22RQDHhTJuaOzATHa-H1CwkauOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت یک مادر و قطع دست کودک یک‌ساله در حمله آمریکا به بندرعباس
🔹
در پی حمله آمریکا به محله «تپه الله‌اکبر» بندرعباس، یک مادر به شهادت رسید و ۸ تن مجروح شدند. دست کودک یک‌ساله این بانو در جریان انفجار قطع و وضعیت وی وخیم گزارش شده است.  #اخبار_هرمزگان در…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/672193" target="_blank">📅 17:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672192">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/672192" target="_blank">📅 17:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62390cef03.mp4?token=WZwn36Bk4XCUC9GLX76ppb0W0nZk2wIGCPAYZStlxjP5O0PokimfzPRGt9elaciq-DcHH8LNyK_yimfup09xR8WQK7BxpOJIoSrmjVfr88CeKts89fM2Tj_5DWN8dIqfesYI7bBewYX-XPjunNe0HQamij8M6Tpn0YFKRLx4x2cIhXTldtHB_bjpp5-_p56wfdFKp5K9LqX2VZ-ojDn53xQBAWi3YRB9ojOwAbXAIFFoPhZ2AuuFvet7DaY3oC6rZjtf-TZvSPdoZIt8vzMIah2azlr5dvBmv6o0xib6WfYX8GskPSTQ2WJhV2QSbJ_D4dUkSG3cOFctu_WvRq-9r3IarexCiptPD1d7kId2NraesyPAyr1a-itr_1n4T3y6D_nKQtRLTtXkdNV2uUPYQbECOLeb0JQwkGM5ulHY0VF_QEGftQSsCHAjTFLXukNDBhTo33KdqIRggT9JSV04ubYE1q-04GrxxnJFgCB5I0VnPmtPsWtzrwdUG4nP1Pt7_TvOPejOxe1pm2o2YQCzWLeVMeydvHuF7nGdLxNgjmBBS2qgImOi1pHR9B1zinNmcQLgrJMRVdlZtEKFB8i4StNhHroZFLiYPzcZnXM0pkTqvppyUIBUsddrPI7oKyTr7zRwdaOUHMo8C9vIdBPkPj4_Xx9NlBlLb056YrxsPrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62390cef03.mp4?token=WZwn36Bk4XCUC9GLX76ppb0W0nZk2wIGCPAYZStlxjP5O0PokimfzPRGt9elaciq-DcHH8LNyK_yimfup09xR8WQK7BxpOJIoSrmjVfr88CeKts89fM2Tj_5DWN8dIqfesYI7bBewYX-XPjunNe0HQamij8M6Tpn0YFKRLx4x2cIhXTldtHB_bjpp5-_p56wfdFKp5K9LqX2VZ-ojDn53xQBAWi3YRB9ojOwAbXAIFFoPhZ2AuuFvet7DaY3oC6rZjtf-TZvSPdoZIt8vzMIah2azlr5dvBmv6o0xib6WfYX8GskPSTQ2WJhV2QSbJ_D4dUkSG3cOFctu_WvRq-9r3IarexCiptPD1d7kId2NraesyPAyr1a-itr_1n4T3y6D_nKQtRLTtXkdNV2uUPYQbECOLeb0JQwkGM5ulHY0VF_QEGftQSsCHAjTFLXukNDBhTo33KdqIRggT9JSV04ubYE1q-04GrxxnJFgCB5I0VnPmtPsWtzrwdUG4nP1Pt7_TvOPejOxe1pm2o2YQCzWLeVMeydvHuF7nGdLxNgjmBBS2qgImOi1pHR9B1zinNmcQLgrJMRVdlZtEKFB8i4StNhHroZFLiYPzcZnXM0pkTqvppyUIBUsddrPI7oKyTr7zRwdaOUHMo8C9vIdBPkPj4_Xx9NlBlLb056YrxsPrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش دوخت خلاقانه کاور برای دستمال کاغذی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/672190" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: شورای نگهبان افرادی را فرستاده بود که از همسایگان من سوال بپرسند که آیا همسر من چادری است یا خیر/ شورای نگهبان کسانی را مامور می‌کند که در خانه طرف بروند که ببینند ماهواره دارد یا ندارد!
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
خیلی‌ها را به خاطر اینکه حرفشان مطابق نظر آن‌ها (شورای نگهبان) نیست، رد می‌کنند. بسیاری از این نابسمانی‌های سال‌های اخیر محصول تفسیرهای شورای نگهبان است. تفسیر کرده‌اند از راهی که دوست داشته باشیم، می‌توانیم نظارت کنیم.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/672184" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458316cecf.mp4?token=nAwmeLqFSwIoxcgHKn3pP0m9RFgT77aRs5a_H1DQ0-iwPrCWfM8_QPlQ8i8oie4jt5UtkN2SuFhCnEIkI4UN2m2uQWdAzvHOXcMLGacFjukrvfQY8lRH25DsZrudB4gN9WUoUkCwS-VYVK1eScvtZ96aQATrmqGy9eApA2NRui2p0Gd0MNF8T5zvK_tQVK7kU2xxi1mgqa-Qq7rSGCaKFHlegePAyUY0xhMHM-QsFD-BqDAvR1EfVevsalkofOjCXh79fmV4Fm3-V1vhEovXP3InT2peeUsoECNBZTfAtctYWmsWGw34GTl745GWxELXfN_VI_qV225ksne48A9rHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458316cecf.mp4?token=nAwmeLqFSwIoxcgHKn3pP0m9RFgT77aRs5a_H1DQ0-iwPrCWfM8_QPlQ8i8oie4jt5UtkN2SuFhCnEIkI4UN2m2uQWdAzvHOXcMLGacFjukrvfQY8lRH25DsZrudB4gN9WUoUkCwS-VYVK1eScvtZ96aQATrmqGy9eApA2NRui2p0Gd0MNF8T5zvK_tQVK7kU2xxi1mgqa-Qq7rSGCaKFHlegePAyUY0xhMHM-QsFD-BqDAvR1EfVevsalkofOjCXh79fmV4Fm3-V1vhEovXP3InT2peeUsoECNBZTfAtctYWmsWGw34GTl745GWxELXfN_VI_qV225ksne48A9rHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارخانه‌ی شکلات سازی/عجب جای شاهکاریه
🍬
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/672183" target="_blank">📅 17:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e468509e2a.mp4?token=iIDAXW07s39X6MBXIhyVSidbtivIb9fQi6W5EuF9t88bZM3qm-6sUbYR-G3in641dS5gbmK8Ck3e0LZM_y-iUiHJ3hdp8O3VRsMFqdDNlX4H8MsbyqGCpRC3xZEE_P9CnEW-ksqhzpuwAinYl8VaQp9FEHl1_vsKeb1o76BRnEYbw_hXa4WhCbDMJ5CsWNU6dzkLGEPXyApjgkmyyRYwplDKIxd77tOMJqvwhaOSv_fmpt6WoVwf6wW81E7Adk2qU9gEqW6P8KcL33Z1PN_deXLx-o4ix1dLoiD7tcFVVJeNl_eG2_K6gd-O43DCRGuUH2XJ3Dhwvn2uZF78HsUJlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e468509e2a.mp4?token=iIDAXW07s39X6MBXIhyVSidbtivIb9fQi6W5EuF9t88bZM3qm-6sUbYR-G3in641dS5gbmK8Ck3e0LZM_y-iUiHJ3hdp8O3VRsMFqdDNlX4H8MsbyqGCpRC3xZEE_P9CnEW-ksqhzpuwAinYl8VaQp9FEHl1_vsKeb1o76BRnEYbw_hXa4WhCbDMJ5CsWNU6dzkLGEPXyApjgkmyyRYwplDKIxd77tOMJqvwhaOSv_fmpt6WoVwf6wW81E7Adk2qU9gEqW6P8KcL33Z1PN_deXLx-o4ix1dLoiD7tcFVVJeNl_eG2_K6gd-O43DCRGuUH2XJ3Dhwvn2uZF78HsUJlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه پایگاه العدید قطر؛ جنگنده‌های آمریکا به اسرائیل و عربستان منتقل شدند
🔹
تصاویر ماهواره‌ای از خروج ده‌ها فروند جنگنده و سوخت‌رسان آمریکایی از بزرگ‌ترین پایگاه هوایی آمریکا در قطر حکایت دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672182" target="_blank">📅 17:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672172">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKyqoL4y7QJgqqJ5BBYPOwV0j5gpVHoCy9NmLMM9ey99fNSHrNljI8uatQ5wK5Bt-BUg9EPEhRInf7QIBVKkzze9TW6Gfu2v4SnN3-6BZr1jgyRnygCJ-zxbnMUWJRog40zuFvoFVczRigTgF3S3UWQe2-InnoTt_MWO-iRPy-W-f9xOFKly2zUNjX_pZxyelJt5ExAzxX3XkyDtciLLRkCKWrMUTLV98uyOT_lGs-xCm5oPzsUKpeajnW2Q0RoMT869wXY4o03um41wD-VqqndRoaiydE26rynezB4S94J5pN-wNiNyAytIlMjQt7vpmKO8gar3rKVr-M-UHp4PwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H59_WhzC7jR-UjR3SI-gZLfamE54Jx_7FIIHZMoPffIenqBZJL75w_6Qrd5znYrvLE1x7HwYt-Qoi-E_4IPDKNINIlCYKUP_3J11S_0WbJBx4r-gN7fFIMOdhaXPyfD6vdh7L47MeEQGW-xizpfOGwM_uBiKGOATSebswbcwoK0evGGKcXou_t1I7OfRg2lBlLf56FtmMi9z2Mq9RalyvGj6ZQZ0VPpuv-xW1ckiMvHzXjTQx2lYKY4q76ZGodOmRPGEph9rs2jEgQAROZ7VHMM7pnYryDCI4bC0gp4v-Kv7iPDVB_-_6LMoHBsHnpAVecvcwjIrhHVtD4ib-ezzRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTO8W3EBkGpSE4YeVymfXIxMAjK7JSpzgPD4QdPyyB_sK5wNG25JZ_xd0JEmQEtQ5xCgKzuf8v_sTGJYP648O3mJndWO8jvYcj4-UPiG-PaW-m9woWucBtX2HSFnwm6E-xb9jKsr0nb2vIQr8KzSrD1J6RPORcTgqXGnV-_y7te5xHcqM9Exgzep6c7hAR7eO1_wu503gsD7XdDBohFbS8EIg-t0M1lvxAyYWZO2HkiN8ty2wS_uGIpNQj3ucKB5j1nNj-GeXrwEjByEFOWlcb7lGpZSQCqJN-0Ai4EEv-scYKPI40Rx_jOinNnk8PZaTnAbu_H7e5KmfkEnJooXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jILjTZLnjdTmO6WmarGHDLB_FL4vMsw3d5wRZ24Hnh-4gJVB1nZE7e1Hl_L0mCI85Q89LekJ2CSGirACcPw_US2qAp6IUpjO7knjnFd7PMML_8--JvmgirhIZTUcBY5g7Ifp5-irpoUZBpZyxU3SyyoA2BagADk2fA9qtqe8-NPoZcCWOWShRnzngwuB-hsRlvaT6lPx1ophZ50PBpczPj3StCocOKLSE8_ObR4CfBYCXi9bLx3e0hy0zvDdJwVpAo7-l52Qi1eTk2xlK-ccnBjLsvqa980COFqDoXh_gXWDIiB3ij4-AkJcEfB21RJ1FVaf2gjWx2hf4Vtj0BNpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ev2FrqrLMKbzMmhNTG7ITUjBpd2yLyhLmDOefoJedPwTR06czemW9hpDRknidISo19BBzKdUHIr9KkI4SyODRy94gVc3ZAikA0ERgnFcEuDmN56cK25N5TDnU5BC_wSYUzQa50gCYMuAgdMxj1QHpQrnDBf_A2nLQuNBtC6IL77onjuGRccTzCPd53lNnu28XsJ0esx6lJyI9t44x6nNn5vPWpRWZxORIu81Thh-19KAzPDh3cnB14xtAEUI3pKNYtmxcmp29aIgqJkEGDzFu9TV4U9O22RByHkvDv0PpDctYjmyCZlTiCilZHew6AAEecfzNn5fsIAyhwXWYlo_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ae6uMQm_VaqLK1H1iwKj9dYgfzKy2viK1kzdGiGKXsTCEalwAbofBFo2ocFxZG-RYBkXHOfZG_rzuhRSGm6LgMfM9XLUZ7vxqGKk4quBdNups7ISCnoYBQCqwJtMOkz1K1VMNxeKiBezknu52nzd0Z5deFXJtL1Zi3-ezlAuYr4_EbzXWfRY9vKf_7YYNIYjQOtyU38rGgqT9m47zVi63yovf3XhUkWnYPJDUe6I2BB1I7UyohFUweoE_2KjRlixxdlS4LjUYtfdMezHZAYKmn87-fjIMAdGHuBKj1GBfpprBPRUR--Nf4a6aH30X9nOZckNCVvglKoLL9htLUpoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u09AkJM2tiRFdVXGO_yzHz4KSHf1TsPDY5Hnfj9h3Ui5eVpWgC4_AvnPBblq7PQvEI1jd9oTQmA_2BG2S1AiMZxrxtD8tEa974az3whyObd-kCCnyPSr-8q_PD61IxoCLCAl9DAQNVlf27B4xWBPaRYtpW17UOZEjqPf6bb9Mkx4TUpU0IarlcR5wOpeMRA7N5LBdr9w1rsveizJVkLi3LzihF6zttycp5qjQqY0ARDzVUxCQzeQDpysChQ0Sq1NaIXBeOHwheueWN7tQg_pyTkOpIfEuJgD55ICeDbTvi1-_6-xzKB0za1X5Q3ioWWY6QrXAM6wxe4zY6PAwIksPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WM5f57qCRtIaVQjsGe1mi31xdmwoJ2HTCiFZi1QPPGplD4l81I77vCI2_FVARBPPHbJHt4CnRmHsDY7UyiFbd87Xh6tQcgcWkMMpA9Kny65IhM92tir9yMCM9-QhiTZFlZEB3Yobc61t2UIgU4pJ7P__o-kiDopZN3vXx8GL1GVWIM5SdPYxX_mrq9j2k1mpvkKo8ZZ__3r_ZKuYnGBS3-wmPL2XJst9ThL0-o7psJAyLwWAMPyNBJ1bM3xZEuo-15Mj8_yum-I828GORUyGHMOKDIBoDkXjz9PoKlDwti785gWDEU91O4jU1iQlgj5Bp7sPH--6wlRpo_sZwiuQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLXY-cGfZ233NGnpbXNNIOGX7lcJkqmeO6v4KxhA7ECrVqTdhe7W-VE2N5tNArsW7Cy7695vSR-zOmFz1Pjv1XthneKIWFEeShLIVOgbSmdidOPSAlJf8n7lHXoIAKd6aN-YupJ2KRB0PNsYd2IMhGNoU_jVn44zYGERuJCfqL4PoYG1Q7L0rNCkiG7FTWtsvZc8dTgHXPY80cmMEtbum_5vWPsEMq2x3HskXMPd25_bDCStygkoByjvadFXd7f1jh2rM7xpvF2O1olrJdx4eb9x3KNE1pFPT3qaCDisB4HBmwAmoTdfPkSdWFRw9kJK9h5wPfGz3-gMk8imasl6nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی از جنایت آمریکا‌ در حمله به پل‌های بندرخمیر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/672172" target="_blank">📅 17:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672171">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETniqasXkCe4wZa3EOG1CF_v3tVn60KwzX5BbSNtlbYBaWM8H9EeaSYrVJ4QetA9MrCemeiZSTo_RfyWnlts3GsF46gcDslUU9hZ7_ECwfln3xSyZHQG0Nx1v-zyxrRfV2CLnKrxBBcWLO5SYGVco2enPBQwZBfl0u1yHdBJVSejJcfYEiP780hAbBz9ntQgtKF-K5JoN0a55YxUuG2k5lSgPegEEszAH_03lg2X8o9Kq4_uJKdMkRGeE-xbKmY3TBk9MGi5Gz3LQ3_V3K7P4b5yrAEg2hVPOH0rCVzRsot49nUQV4j51P5cTLASd9qqa8Bg8K0UoSo2VQIW-LzvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/672171" target="_blank">📅 17:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
برخورد پلیس فتا با کانال‌های مدعی فروش سوالات امتحانات نهایی
رئیس پلیس فتا:
🔹
کانال‌ها و وبگاه‌های اینترنتی رصد و با گردانندگان این قبیل صفحات، بدون هیچگونه اغماضی برخورد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/672168" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672167">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIgq7ROBc1n9jbDEEE1s9yGfrCw3mML3K93BKrcMvrNnD27DulUC5PfZrwRov650QXNhAARcgIe7rmeSDUddHk-g79RtKUSlOmFf9d9291POyHMhVpxSqyKjODNLnpRzEvEgyTg7VrF2q_GWWgFK_cysqaTKOxKEcTYZD1mwpk5u0SrNy9O4_99tQpn_mEs_UfcJ1q4caQTklpF3CqcmBe-_0L-rHh-T3vkve-QNIAqdQVqkMqMkThy2sSrmp5OD6rB9P4fZoyGArfHvc_y2hlnesFkq8DDtlwUn_4-mKr7IIEVNQD8NtAC_X4oaeT9y0vd4jHcyPYunNC_Tgmk6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانه تامین کالری در کشورها چقدر است؟
🔸
این شاخص، کالریِ در دسترس برای هر نفر در روز را نشان می‌دهد؛ نه لزوماً کالری‌ای که افراد واقعاً مصرف می‌کنند.
🔸
میانگین جهانی کالری تأمین‌شده ۳,۰۵۶ کیلوکالری است؛ آمریکا با ۳,۹۴۷ در صدر و یمن با ۱,۸۸۱ در انتهای این فهرست قرار دارند.
🔸
ایران با ۲,۸۷۵ کیلوکالری و رتبه ۱۰۷ جهان، کمی پایین‌تر از میانگین جهانی و بالاتر از کشورهایی همچون تایلند، هنگ کنگ و اوکراین قرار دارد.
@amarfact</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672167" target="_blank">📅 16:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672162">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a02bc8676.mp4?token=BavI1kvASiOCIYVLoF5q_KETcGLofcfkxF9SX1pMqWPHZCUwNds1pMjxvYXcNJk2PlsTd3NNyk0Ti58qz9rQ5w4J76kGFP20ySmpChhGw8Bm4RDbaP5QQ7yDJqvLfF0BDWH0hRdtzCvtp7jgQIDmq7sTwYbA8I10FCuOke8CeFiPtbzMzBADw-7IVGenwr_Gvdd5IHSjqQwzgJML5frlABBqXlmXjRy3pc83LoPqWKbMh10orJK-5kg0gG5EhfZjhsFV4pviHHXAtRztG25f2BL0vg61ga6Jc7fR3BOnqaJo9MhTtLnt-Qhq-KUidBmxSP55R8KXnMBlfZQcVXmHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a02bc8676.mp4?token=BavI1kvASiOCIYVLoF5q_KETcGLofcfkxF9SX1pMqWPHZCUwNds1pMjxvYXcNJk2PlsTd3NNyk0Ti58qz9rQ5w4J76kGFP20ySmpChhGw8Bm4RDbaP5QQ7yDJqvLfF0BDWH0hRdtzCvtp7jgQIDmq7sTwYbA8I10FCuOke8CeFiPtbzMzBADw-7IVGenwr_Gvdd5IHSjqQwzgJML5frlABBqXlmXjRy3pc83LoPqWKbMh10orJK-5kg0gG5EhfZjhsFV4pviHHXAtRztG25f2BL0vg61ga6Jc7fR3BOnqaJo9MhTtLnt-Qhq-KUidBmxSP55R8KXnMBlfZQcVXmHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
احتمال به تعویق افتادن فینال جام جهانی به دلیل آتش‌سوزی‌های جنگلی در کانادا
🔹
دود غلیظ ناشی از آتش‌سوزی‌های جنگلی در کانادا، ایالات متحده را نیز فرا گرفته است.
🔹
به گزارش خبرگزاری Ole، احتمال به تعویق افتادن فینال جام جهانی در حال حاضر کم است، اما فیفا این سناریو را منتفی نمی‌داند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/672162" target="_blank">📅 16:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672161">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بسیاری از افراد شناخت مستقیمی از رهبر جدید انقلاب ندارند/ برخی نمایندگان تلاش می‌کنند برای شورای نگهبان خودی نشان بدهند
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
شناخت مستقیمی از آیت‌الله سیدمجتبی خامنه‌ای ندارم؛ نه ملاقات حضوری با ایشان داشته‌ام و نه ارتباط تلفنی.
🔹
برخی نمایندگان به فکر دوره بعدی خودشان هستند. برخی افراد در مجلس به من حمله کردند و قصد پاره کردن نطق مرا داشتند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/672161" target="_blank">📅 16:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672157">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpnVdyHkbYAWUZ62EEr6DVbuw2oYjKClCHoNyPxevruBPZLcPexnNlmmwRYUciytfAxSjPYOwMST51-LEJnV7Rur10DmA6uHA8pokgxYIbJEk9bto8LZE4eTQkNDsn97HlC3txTqvfuW7K3npEi3Y_ACkMqgVmjXjQB-CgfIDGZCtNm4rBzpxEyaPiMgAVW8toIIdLB7s1pFE73LxulHgZ5XK50A0hefoqaSMvl0UTbc1nskg9fFwyxBP20MDNwBemkbv0tSmODAIFHJRlg2ImdVT45pCSxaAr03TS5sfEizr9_5uTR1quuepBnG8Rgg_qtUhG6ftiFZ1bvArTT3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e0ee339a.mp4?token=gU2_FjRRoFm_I88LnkOxbIRr2Gr1WbybW7R3plkkybJaUlzUPquyTb7DPCoFgb090ChcqLprA9Q_oApAA_aaCT0vKBToS0Tv7wWlgzYBlQum3RvnVq440LrN_3Ph5WvlJuKNfiFn5vncL-goPp8swZIJk4loIf-IC7PwNJIHREYlbt2K4jL8MQdB8R2fxVE_xF-D3aG52TEopKhdzZ1XzCabjjZTXuF-Y5AzPbnqdI6mcvrqoflOzCSprPf1KU6trlzOmpVkkUfiQwUgiNyWpCgaZ4keDCGM6XgyDh2S_w1SgUxzC-sFcZWxC9CrKmuC4oIhJ7kZiGAOsoFeZc_uBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e0ee339a.mp4?token=gU2_FjRRoFm_I88LnkOxbIRr2Gr1WbybW7R3plkkybJaUlzUPquyTb7DPCoFgb090ChcqLprA9Q_oApAA_aaCT0vKBToS0Tv7wWlgzYBlQum3RvnVq440LrN_3Ph5WvlJuKNfiFn5vncL-goPp8swZIJk4loIf-IC7PwNJIHREYlbt2K4jL8MQdB8R2fxVE_xF-D3aG52TEopKhdzZ1XzCabjjZTXuF-Y5AzPbnqdI6mcvrqoflOzCSprPf1KU6trlzOmpVkkUfiQwUgiNyWpCgaZ4keDCGM6XgyDh2S_w1SgUxzC-sFcZWxC9CrKmuC4oIhJ7kZiGAOsoFeZc_uBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام یک انبار لجستیکی آمریکا در کویت پس از اصابت پهپادهای ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/672157" target="_blank">📅 16:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672156">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3V79j-lon73oNDaFz94Urgd-oVMV2ffkA166x0XEF1rZV9MjAfes_wgBz5LenMOHFEvqNV5_x6KvkoqizfpPAustwI1O2RzdKozVRQZxC5g3dcuaXdywMF04ICePuDZlen9e-yj54QFPxTHFr1zLWxZqOeDq6LqD_B1UGkQdnq_RyMUNkTlC7--4ned8Pu4MoVsP7wLFY5tfstlBlExCesHhWDYiF1npgWzqSQtCDpzVMzUWw31zu0R4IIoYeg6kv6bxQmI5zrrmf08gDtY6G9g8fcUs-jB2KZMsY4u3pbQFra2oqOdj82SsjUFJuXCXtgEC351cvG2SgJ_Z7zbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابی جدید از مزار نورانی «رهبر آزادیخواهان جهان» در رواق دارالذکر حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/672156" target="_blank">📅 16:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672153">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-text">🔹️
ویل لكل همزة لمزة
💥
نباید به یکدیگر برچسب بزنیم.
نیروی انقلابی نباید اهل «هَمْز و لَمْز» باشد.
🔰
آیت‌الله میرباقری:
1⃣
دشمن با اخبار یک‌سویه و گزارش‌های ساعت‌به‌ساعت، می‌خواهد دلهره ایجاد کند و پیروزی ملت ایران را وارونه جلوه دهد.
دشمن جنگ رسانه‌ای راه انداخته تا میان ما دعوا بیندازد. دشمن خبرسازی می‌کند و نتیجه این می‌شود که ما شروع به محکوم کردن یکدیگر می‌کنیم.
2⃣
علاوه بر این، همز و لمزهایی در کلام وجود دارد که قابل‌گفتن نیست. کجا خدا به ما اجازه داده که با هم این‌گونه برخورد کنیم؟! «سابقون» نباید اهل همز و لمز باشند؛ وظیفۀ آن‌ها این است که دستِ کسانی که پشت‌سرشان هستند را بگیرند، آن‌ها را آماده کنند و به جلو بیاورند؛ این مسیر باید مسیرِ «راه بردن» و یک مسیر تربیتی باشد.
از هر کسی باید مطابق با توان و جایگاهش انتظار داشت. ما نمی‌توانیم همه را وادار کنیم که دقیقاً با گام‌های ما حرکت کنند. «مدارا» یعنی همین؛ یعنی جبهۀ مؤمنین درجات مختلفی دارند و با هم مدارا کنند.
3⃣
وقتی ما با این حرف‌ها با هم درگیر می‌شویم، مشخص است که آن ۳۰ درصدی که به سرمایه اجتماعی ما اضافه شده بود برمی‌گردند و می‌گویند: «بگذارید این دعواهای غیرمنطقی را ادامه دهند». و دیگر در کنار ما نمی‌ایستند.
ما درست در آستانۀ یک پیروزی نشسته‌ایم، اما باز هم معلوم نیست چرا این‌گونه با هم حرف می‌زنیم.
☑️
@mirbaqeri_ir</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/672153" target="_blank">📅 16:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672152">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2871b47955.mp4?token=bmdpk7GveZ0YErrnEmE-5t-881JZnSB0SyVycli4tFjTIodSlSlW9sFNx3uThO73k-f6lMeRVIBZKJZeFis1O92SBmemVouLnU2HlA9y5Rt7t0FPb8S1sQz1SGopGeSTw-Agarlu9BXtapC1W7LKzJMObbxuoFrWYMwFop-Inw0fHf28XD9vXQebncgNj2YmS2A2Rv1tQsqukHrV9ZmyM8VxslA20gGixv91nKNmqqutc0hsgnFPnbc_U1iPcJkfsOHog5l9c4kf4FwYEjIHbqVqS3ttbY9MPX3KWLf3ieLx8D8NGe6oFcOMay6zfv_u4kN49YYt2mRXboPmmS8X9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2871b47955.mp4?token=bmdpk7GveZ0YErrnEmE-5t-881JZnSB0SyVycli4tFjTIodSlSlW9sFNx3uThO73k-f6lMeRVIBZKJZeFis1O92SBmemVouLnU2HlA9y5Rt7t0FPb8S1sQz1SGopGeSTw-Agarlu9BXtapC1W7LKzJMObbxuoFrWYMwFop-Inw0fHf28XD9vXQebncgNj2YmS2A2Rv1tQsqukHrV9ZmyM8VxslA20gGixv91nKNmqqutc0hsgnFPnbc_U1iPcJkfsOHog5l9c4kf4FwYEjIHbqVqS3ttbY9MPX3KWLf3ieLx8D8NGe6oFcOMay6zfv_u4kN49YYt2mRXboPmmS8X9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاقانه‌ترین چیزی که امروز می‌بینی: لیوانی که با عرق کردن بهت لبخند می‌زنه
:)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/672152" target="_blank">📅 16:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672151">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e876bc17ee.mp4?token=ehr4_nLfaKC_NX4DYgv46v1Ne1tSm54h4-ahOlxcIgg1js9ob8pjvfMAaiG00xE1hJPfrWML2biqofWyfHoS88KVioSBDCxv0tgh_vrq51B8jbTSsNJNngGFng8joNL4rDgebzQ9g0KVgMLp74JetbuD9eNSXFmMfO9aCyQapgYHzlSmcp3U8jNc-75o3xnytlqTbQFsu79NsamP1eqERL5djOufkO3Gmxu14FRWYhrJkYpsKBtCS4KOLUU0GDom3op-oamGA4xYfx97QDtY4k8n_16ArtZpzt4EgGrba4k7DCuCYMSHKl-3kvkRYd0XJSfm4VEZPZFv911v0AD0VgyZ8LnKzGpraqUSVquVjwmA9yBhRkctMWwL9BqpHUaYN5StMyGlNUmoShZQdYCFPzJ76-FYNG21Dh4pJFV0Rqh4afTDdchnfphr91TRp0PK0IGMv0KwRhLuRjQIzICZWTuLllbnjBnhiaJgxcboarJTbUhqPUUFnC26voB-WmSbrKNicPdAJkYMxUrEkywTgupz6FwwBKgl8b1eWI9YaCmXrpDBVL4UqKL1Wm6jPrNQhmBoNYZztTe6TkjArVwPnzfihqrf3ptA7urktRmiYpgKUgGT4vfduwtXG6j-QF3nCXA09-Az_L4yoWPiA1kWSB6GBA7gcm4Fi6XOk8aePOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e876bc17ee.mp4?token=ehr4_nLfaKC_NX4DYgv46v1Ne1tSm54h4-ahOlxcIgg1js9ob8pjvfMAaiG00xE1hJPfrWML2biqofWyfHoS88KVioSBDCxv0tgh_vrq51B8jbTSsNJNngGFng8joNL4rDgebzQ9g0KVgMLp74JetbuD9eNSXFmMfO9aCyQapgYHzlSmcp3U8jNc-75o3xnytlqTbQFsu79NsamP1eqERL5djOufkO3Gmxu14FRWYhrJkYpsKBtCS4KOLUU0GDom3op-oamGA4xYfx97QDtY4k8n_16ArtZpzt4EgGrba4k7DCuCYMSHKl-3kvkRYd0XJSfm4VEZPZFv911v0AD0VgyZ8LnKzGpraqUSVquVjwmA9yBhRkctMWwL9BqpHUaYN5StMyGlNUmoShZQdYCFPzJ76-FYNG21Dh4pJFV0Rqh4afTDdchnfphr91TRp0PK0IGMv0KwRhLuRjQIzICZWTuLllbnjBnhiaJgxcboarJTbUhqPUUFnC26voB-WmSbrKNicPdAJkYMxUrEkywTgupz6FwwBKgl8b1eWI9YaCmXrpDBVL4UqKL1Wm6jPrNQhmBoNYZztTe6TkjArVwPnzfihqrf3ptA7urktRmiYpgKUgGT4vfduwtXG6j-QF3nCXA09-Az_L4yoWPiA1kWSB6GBA7gcm4Fi6XOk8aePOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسعود اسداللهی، کارشناس غرب آسیا: هدف ترامپ از امضای تفاهم‌نامه بازگشایی مجدد تنگه‌هرمز بود/ شخصی که تفاهم‌نامه را امضا کرد باید به این تفاهم و موارد آن شک می‌کرد، این تفاهم نبود سوءتفاهم بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/672151" target="_blank">📅 16:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672146">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bh3DblFetmAA6js5DrfG4X1c848q-7E8JjJ_rFpkZKd01970OtSW7gd4iIcxera65uBMKlu0n0iiQnwQbbNc9rx8BKQPYor-_ne-aZJr29W8Hj6565ESeuKhXnoxJf9CTsYimGHsSULxnmRnCZpoF7TQ_-9A2HqORHOEdwj6a2Iq8RcYgDJsHJSyxV9pL7u0mi9HsZx0ENfbEBpK0kB_eZHBOxzNsRn6FZ_Z8eSsSn8JRkN9846GMqmRU-xdSSBQ8kk6Jtzv7HdOze2fSbYDhDWlOuzuNdhkQmhs68ZXjvwwZJF-hD6m3bD8bFKj4ZrPHuljZrqDW6xV4tBpYMhCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaeGcT7L0UFSLfnvNM9kXQafY9GO8r2LKDJAi8FQPdzW4kXH1_ACZ-pe3nH6xjPDqC70RoRDuw2XvJ6lyATdXM4Hf6tKeUi3N3kxG7s9Gdxc1bu3ZPgZyRr8q8QT2ZGo_A698OeC9pxoFBSVe5Z5QfvBlEj55J8z80KHlEyOaAgO2p7qi0k4rFbiR3lrohVoeQUFdaz1rbTUlw4nbM18gEZeFaClO3JzGlbDv9drFg8Lzgd1iR9GkhjNmmFb0ofuJZaGrK1XT0fkrpc_rNz2xiK-phTq4GpvKyVMhmRaid1vPJQKpt9ZTjBjchVhv9HgIVsrZMVP-vQKofqWh_fVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdSej6mET_ilvwfl5CpmNJYEWs1_iX8z4OFL2gNXJxUMo00uD9WetohHOv78db48oOSu4l1uQHL0gQtmjy6Jc3uN5Wvxpo8M6S35yUpX4JXD6Z5wH1f5yZC66YPnjuhPtPCYrV5oWclnmEtB5F8REV8Z95kB9cb3yn9wF9dvsPjX44TvwBK1BCx4jDTauCiMI_upvg67JmhIsuTP_dkzHXDASa4QPNi2nBeqdznjy7b9sAxepeswpLdRwlS1l8b1gJ5RJ61s9pkRJ6w3bQAiCaCUuX2hs6S9n_moNUb0AX01D4TsbJsElbCcQnEqmo-YzFsm1vLF_BZ7Wqjs38vM2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
محصول جدید تسلا به بازار آمد: دوچرخه تعادلی ۲۲۵ دلاری برای کودکان
🔹
تسلا دوچرخه تعادلی ۲۲۵ دلاری برای کودکان ۲ تا ۵ ساله (بدون موتور و پدال) با فریم منیزیمی و صندلی تنظیم‌شونده عرضه کرد، اما قیمت آن بسیار بالاتر از رقباست (زیر ۱۰۰ دلار).
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/672146" target="_blank">📅 16:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672145">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: برخی مخالفت‌کنندگان با مذاکرات از روی اعتقادشان چنین نظری دارند/ ممکن است برخی از صحنه‌گردان‌ها اهداف سیاسی داشته باشند و بخواهند به رقیب سیاسی خودشان آسیب وارد کنند
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
استناد می‌کنند به برخی از سخنان رهبری مبنی بر اینکه مذاکره با آمریکا جز خسارت چیزی نیست، و این را به تمام شرایط تعمیم می‌دهند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/672145" target="_blank">📅 15:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr1K1jYN8UATFqLCLHFvq4tuDFZAVYzgMzjQ5ZzP82H3OeS4hBTIRRiIP7gZoGIRyU5ipd6Vow0qT1KgG5Q3F9u4EiKwTn9RPyZS5EA5nSUeDwcjvmjlo6WqRN8f3ruId1r-VJPVfER-tuSTJ6iGhbz6yaChA9Z7ZSyDSTlsbbVjOAj3xzsvyVENZJHE9VXWKspmRDdHPgRLBHR5BZw46bJmLJaMrofbo6PFLnhG4yvu27XiV7qq9vZP26yclIUXi16pj9gCjuQ2o5qMG8WZZhdwt8ZK7MKbSkJuNMSi2VcxApT5X6V6eiDCupr7oR2wZgJX_MMWBLuyA42wyzPAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده هوافضا: شلیک‌های موثر و هدفمند ما تا برگشتن آرامش ادامه خواهد داشت
سردار سید مجید موسوی:
🔹
در نظام محاسباتی ما خاک، خاک است، تهران تا جنوب یکپارچه برای ایران هستند. شلیک‌های موثر و هدفمند ما از سراسر ایران بر سر دشمن تا برگشتن آرامش به خط ساحلی جنوب و تنگه هرمز ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/672143" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osknJBMIlTmDHBanXoZFd3id5wnIV-t9SL9EYXHgmBrWCEiF-ChJKg1I2A93HHgGGS66B5bcanWEIhlLIGAxvwDrsWlkF7v6KMlM-5Qqt_oWb-UXJk3GFEZzcKn829wSreBbN7oFwy4vfXauBX6kxyANsBf1rxCqSh03PgjVy2B3Rmwc3Q1uqppnsuyBkoBaASxcDzYq4_aytDfDF4AnJLIL4_d7zrYuaUr28AjDzreckW2wnWnVlE2R217VKK8owLdFQ6qsn6GN2YwcjJ57Dqt1REXJ-GZA4B_bVbEzvPNtjcJrPpasIkc2empZ-dqLY3PQjjFJzS03IkLxRuKukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام پایگاه های آمریکا در منطقه مورد اصابت موشک های ایران قرار گرفته‌اند؟
🔹
اطلاعات موجود نشان می‌دهد که در شبانه روز گذشته پایگاه های آمریکایی در ۷ کشور منطقه مورد هدف حملات موشکی و پهپادی نیروهای مسلح کشورمان قرار گرفته اند و خسارات زیادی به آنها وارد گشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/672142" target="_blank">📅 15:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb1219524.mp4?token=i5xvlSV7gjBNlWxbBToNwFpSEw5jvCF1uw1fh4dwcBCKeg6d9sIbpGY9tMBO-VHkaU5vQnpr7mu9JIPWLrvtuxQvCrUA9fXLnKhEfOtxC9iMpLvUmFYzmgzHXX-oeRvQ39W0Cok3OXwv2fSz67BksVjpaDvnDQHNmJY4hRV6PlCLrdH8Z-hDkoCaAm_j_Xscg5nCrxlHmCxsUoCn88tB7cIk03f6PfM2HTpQgRbuMuxaEMnZQCcUpKdu7BeFYSHIDL4pvsoUnIH8TI36O9y8K-NuZMwxziGXvETuSfCiIyFneXYrMKgo6_mx4RE90GhARVOkYAzn4qpeA40KMQpmjQ3r5pI6GHdMG1uqNINUFLNOq8WIOQ5VMgz3MKp33V8ZC3IhkiXRL_APnyii6MKCNkS7VGRvqqBt4znhVvDmKRx5X_QqId4OTkzxJ7fLHUPhAjO6oOY0oX4_seLlGKCyHYjb-nWp6kOOk7pwW_MLcRUsJXuX4c6WujSUayVSENllDEhGzKDfy93ykN1vQ5lhu-cpGvLMtRPn6oSsYxDq9vy8_zQzDVnkkXv95mKOgnIaQjDpgtPkWR6Y9kUrVsrwY5lUzRUQ-vPQzczeRD-Jc3KSJXPZHATC5wkr34MVVKAJ6t34Hbz_F0xXnDLh7fGd0l3ZSlFxTmriMLylwmCigh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb1219524.mp4?token=i5xvlSV7gjBNlWxbBToNwFpSEw5jvCF1uw1fh4dwcBCKeg6d9sIbpGY9tMBO-VHkaU5vQnpr7mu9JIPWLrvtuxQvCrUA9fXLnKhEfOtxC9iMpLvUmFYzmgzHXX-oeRvQ39W0Cok3OXwv2fSz67BksVjpaDvnDQHNmJY4hRV6PlCLrdH8Z-hDkoCaAm_j_Xscg5nCrxlHmCxsUoCn88tB7cIk03f6PfM2HTpQgRbuMuxaEMnZQCcUpKdu7BeFYSHIDL4pvsoUnIH8TI36O9y8K-NuZMwxziGXvETuSfCiIyFneXYrMKgo6_mx4RE90GhARVOkYAzn4qpeA40KMQpmjQ3r5pI6GHdMG1uqNINUFLNOq8WIOQ5VMgz3MKp33V8ZC3IhkiXRL_APnyii6MKCNkS7VGRvqqBt4znhVvDmKRx5X_QqId4OTkzxJ7fLHUPhAjO6oOY0oX4_seLlGKCyHYjb-nWp6kOOk7pwW_MLcRUsJXuX4c6WujSUayVSENllDEhGzKDfy93ykN1vQ5lhu-cpGvLMtRPn6oSsYxDq9vy8_zQzDVnkkXv95mKOgnIaQjDpgtPkWR6Y9kUrVsrwY5lUzRUQ-vPQzczeRD-Jc3KSJXPZHATC5wkr34MVVKAJ6t34Hbz_F0xXnDLh7fGd0l3ZSlFxTmriMLylwmCigh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از استقبال گرم و پرشور مردم جنوب عراق از زائران پیاده ایرانی برای شرکت در مراسم اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/672141" target="_blank">📅 15:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb3be02fd.mp4?token=nt8d0X_wmzC04_VvTRFk3-spInx9JRXkWcmvfzXqNCpNTiKDpwjoyxu6DltI_e_GlHN9_g49DpQZqmhFhs0wbHbyM3xkWL2KWrP_Y3uiHzJxHdfHqTdoya79ltvx-hYANVKuLjERo1Q2N4llgnoCXAmIje1wVJ_w4kfa-HBfapRucgSVwiciyV5k9pGtFmqT8O0pTpmMuPK-GajsqObrln9bFhjSlL69FDpIRMiJv4t0NkdqbowZ7zHHKfoefczIvIvXSF6k2GI8zBTyfJKWJxlKHp5Z2VN3I6WJUIICdZGt27HQ_xjlXwwz9afasPNGK8yu_u3CuTBtbUVrAyui3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb3be02fd.mp4?token=nt8d0X_wmzC04_VvTRFk3-spInx9JRXkWcmvfzXqNCpNTiKDpwjoyxu6DltI_e_GlHN9_g49DpQZqmhFhs0wbHbyM3xkWL2KWrP_Y3uiHzJxHdfHqTdoya79ltvx-hYANVKuLjERo1Q2N4llgnoCXAmIje1wVJ_w4kfa-HBfapRucgSVwiciyV5k9pGtFmqT8O0pTpmMuPK-GajsqObrln9bFhjSlL69FDpIRMiJv4t0NkdqbowZ7zHHKfoefczIvIvXSF6k2GI8zBTyfJKWJxlKHp5Z2VN3I6WJUIICdZGt27HQ_xjlXwwz9afasPNGK8yu_u3CuTBtbUVrAyui3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منفجر کردن مسجدی در جنوب لبنان توسط ارتش رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/672138" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a81372c62.mp4?token=hUpZCG8jpdmgQ0OWzm9uY4IJOQvQC-6SNl6fzBFAz5sqw9hbYcd_b4V7-QDOIKTjHU_tCk0ziFuw4Q-8LYEXODPm0H7zCjVLaNOBO3mLlD6bs9QzdRFqnRQ1deNIY1Qdoaau0h-LkqPohYqL9hr9aqVT6rAIrI8o8BSpjKS1N6zOfB0ly3dpHUiXEd3zp1aqFZFM6_YvD_uXohpMmxbKap-gB_ex34llO254vp2RwsoEcWKN3mek_crntYyhgn_d-4W-TaI9mOn5tdirEw7OlHTWy3S9pAq75b7mfjvioX4-P8ivartme85vTnoP3GjpRv1ohn9kBqi73M4j5r0Mew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a81372c62.mp4?token=hUpZCG8jpdmgQ0OWzm9uY4IJOQvQC-6SNl6fzBFAz5sqw9hbYcd_b4V7-QDOIKTjHU_tCk0ziFuw4Q-8LYEXODPm0H7zCjVLaNOBO3mLlD6bs9QzdRFqnRQ1deNIY1Qdoaau0h-LkqPohYqL9hr9aqVT6rAIrI8o8BSpjKS1N6zOfB0ly3dpHUiXEd3zp1aqFZFM6_YvD_uXohpMmxbKap-gB_ex34llO254vp2RwsoEcWKN3mek_crntYyhgn_d-4W-TaI9mOn5tdirEw7OlHTWy3S9pAq75b7mfjvioX4-P8ivartme85vTnoP3GjpRv1ohn9kBqi73M4j5r0Mew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاوی تصاویر دلخراش
♦️
موشک‌های جدید رژیم صهیونیستی پیکر قربانیان را غیرقابل شناسایی می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/672137" target="_blank">📅 15:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed2a9082f0.mp4?token=lQy7oe0TyeuQhWmywEyOBUqbkLWenwiKsctWUyVlubvvp4-Rci9n69caN_cFcr6v8eNf4lTPYVmomsQVA3wsF-8S2LnrwMob_jEc-0VQGxv4yeEuiVD1pwm6Wu-q5g93SRZqX6g4G8HXRSjrInAEiMGTtEfy9ZoGI4MPPdV4qUWMU_CAUxd6Q0TpgKuJOtHnThkWLNeJauNFEX6N6lpWKQCZdjMoAfamZucXGczXLsHHRhiEzBHzATUSbIRLXLHu0j2MWZkz0efud5FMz04rkqyfiTvGl9Ju32vGRak4qbRmYWjqQqP_44oz_LCOW_sXQYdu5qad7swCTqjGc9lmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed2a9082f0.mp4?token=lQy7oe0TyeuQhWmywEyOBUqbkLWenwiKsctWUyVlubvvp4-Rci9n69caN_cFcr6v8eNf4lTPYVmomsQVA3wsF-8S2LnrwMob_jEc-0VQGxv4yeEuiVD1pwm6Wu-q5g93SRZqX6g4G8HXRSjrInAEiMGTtEfy9ZoGI4MPPdV4qUWMU_CAUxd6Q0TpgKuJOtHnThkWLNeJauNFEX6N6lpWKQCZdjMoAfamZucXGczXLsHHRhiEzBHzATUSbIRLXLHu0j2MWZkz0efud5FMz04rkqyfiTvGl9Ju32vGRak4qbRmYWjqQqP_44oz_LCOW_sXQYdu5qad7swCTqjGc9lmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاضری برای وطنت اینو بپوشی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/672136" target="_blank">📅 15:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
آرزو داشتیم به نجف برگردی اما نه اینگونه...
🔹
قاب‌هایی اشک‌آلود از بدرقه‌ی پیکر مطهر  مرجع تقلید شیعیان جهان، حضرت آیت‌الله العظمی شهید خامنه‎‌ای توسط مردم شهر نجف عراق.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/672135" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ2Z82n7Fp6hmYlmXX_gbNKyUTV6nzDSIvtbhneawjGPTh9EMAUhXeik8GGopVKGF3mP2wXrN8TJtYubGZ6PLQCklNXuGeZMf3oZlFBj0UyjcNtLNEy47Nsf16xpotWYMvMYO4PDyv__qihF2T1gTUTqxo0Ie-z8X6smifBWWpkKvXlAtHZI9Knq5K1jpzp10ghOTw9PpJibccdjrrT2IxjQoSjBBQIjyKeROQoQtmUN_s1Zglqqtp8a4RTHJzsNY2EDuHz1gNPMv3cTi_kx91BH8jWaVT6JlO9w1DwUpJqFiBAbn0kP-RcX5e0ZhGBXRcjdvdAGDS-t-_XN51PVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست وزیر جدید انگلیس معرفی شد
🔹
اندی برنهام، شهردار پیشین منچستر بزرگ، با کسب حمایت گسترده نمایندگان، اتحادیه‌های کارگری و شاخه‌های حزب کارگر، به رهبری این حزب انتخاب شد و قرار است روز دوشنبه جایگزین کی‌یر استارمر در مقام نخست‌وزیر بریتانیا شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/672134" target="_blank">📅 15:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672133">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtzJ3KietRUyMrJXn9hs3rEZHdPE_fLZLIQRq57-PHjjG-efPAzjzbUsQvz4nEJjd9nRPWIjcmwG5E4vfKMVOABwgSvPhHRdf1bKlvoa_-RdGigOagfQGb8q4g515A-MjNDIm-zYaSIs6qAYh5_AEEkbhLkRE_fuWSZkq9yUwIRRUyNBTu1k9C-5bUbU9xq0LCzTkIin9lq_xANXBiOBDch-yKagFezbplZL0xp4yyjA7ywnudCXwH66BuiUIA22UxXkyoJqrupGZrGV9bO5ur4PRMWk9UFY9peUq5bcabTHV02KsF12k24IMiMm9_e1AicIHKedtQv7ZqC7ngBrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمیته وزیران امور شین‌بت تصویب کرد: سارا و بنیامین نتانیاهو تا پایان عمر نخست‌وزیر تحت حفاظت خواهند بود
🔹
وزیران همچنین با تمدید پنج‌ساله حفاظت امنیتی از دو فرزند این زوج، یائیر نتانیاهو و آونر نتانیاهو، موافقت کردند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/672133" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672132">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش علی مطهری به گزارش نیویورک تایمز در خصوص احمدی‌نژاد: احمدی‌نژاد دیگر در جامعه ایران طرفدار زیادی ندارد
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
آقای احمدی‌نژاد چندان پایگاه اجتماعی ندارد. عده محدودی طرفدار ایشان هستند.
🔹
اگر هم بحث آلترناتیو بودن احمدی‌نژاد (به ادعای نیویورک تایمز) مطرح بوده باشد، چنین تصمیمی درست نیست.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/672132" target="_blank">📅 15:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672131">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988241fe78.mp4?token=aXNsaGbg6zA8CsVwnjeKBoeFcOO9k3g4S1hC8Ous29NI1-xyUqVI2ahqWVAYshp43IGjfGzaVKTyjnE_EygzQJkYfmlPVFN4BxilTkeOmtp2ciNvLMeQ5qyUpXBMXXVMYwpQSJdCBVXcm1zTLRDvUYqIe7JobaXMxpkRsw1VJHAOoVIsV6NvHF30AGbeH26G4zsDWWxumCPyv8DPwLbbpzCJoQLuOCq7ZUTbEHxVVlccWFQdC3cR-G3yzjuaucr4JFRpnQsti_A92PBtD2qUt8vWiy4VuQ3f3XEV9R3WeHsBFeGk3w4FwFrJ9cJkb1ncMgpBOOoSuNc2pgjYGB7-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988241fe78.mp4?token=aXNsaGbg6zA8CsVwnjeKBoeFcOO9k3g4S1hC8Ous29NI1-xyUqVI2ahqWVAYshp43IGjfGzaVKTyjnE_EygzQJkYfmlPVFN4BxilTkeOmtp2ciNvLMeQ5qyUpXBMXXVMYwpQSJdCBVXcm1zTLRDvUYqIe7JobaXMxpkRsw1VJHAOoVIsV6NvHF30AGbeH26G4zsDWWxumCPyv8DPwLbbpzCJoQLuOCq7ZUTbEHxVVlccWFQdC3cR-G3yzjuaucr4JFRpnQsti_A92PBtD2qUt8vWiy4VuQ3f3XEV9R3WeHsBFeGk3w4FwFrJ9cJkb1ncMgpBOOoSuNc2pgjYGB7-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت‌هایی که‌ آمریکایی‌ها در هرمزگان انجام دادند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/672131" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95465ecf3a.mp4?token=IjtGll8iVxgrsS-XFd2Jr_8x38gEl6NgXzvHbxj4o8am5E3vxl1sdVFCb3jBYskomkq1JwaXph7jONWYGsYNuKAMHcnBfDLIt6wGyTQw0Mop1xj3GkVQOwpwguekdravTi4Dmd8_BU4AmNIRvIm0ZFCTe9Wnc7c9CzdxD4UIodLlVc7xCl1vMPnVCfDqxtHsGWEmpAsvF082z-7KoahWfmRceg2kkZmroTNBXTH1RgztWun76y-pqgstFj5A0TBGIQfdGTt-yiydSQrjFdvYltFaxHsxHKaXi0I0yNkJLmRgTfcrEMTbn3B7mEJ_KoZ6AbSbJQazJlZ6bwj6qGP4pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95465ecf3a.mp4?token=IjtGll8iVxgrsS-XFd2Jr_8x38gEl6NgXzvHbxj4o8am5E3vxl1sdVFCb3jBYskomkq1JwaXph7jONWYGsYNuKAMHcnBfDLIt6wGyTQw0Mop1xj3GkVQOwpwguekdravTi4Dmd8_BU4AmNIRvIm0ZFCTe9Wnc7c9CzdxD4UIodLlVc7xCl1vMPnVCfDqxtHsGWEmpAsvF082z-7KoahWfmRceg2kkZmroTNBXTH1RgztWun76y-pqgstFj5A0TBGIQfdGTt-yiydSQrjFdvYltFaxHsxHKaXi0I0yNkJLmRgTfcrEMTbn3B7mEJ_KoZ6AbSbJQazJlZ6bwj6qGP4pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپاد اسقاطی لوکاس امریکا، نسخه فیک شاهد ۱۳۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672130" target="_blank">📅 14:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672129">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViP6-rTQ5dGK-3GfmHRjzALsywu-NFKnf1V2p7V55SewdFNy_G3WJMXl4iDSc6PxwGrhI85aYA2nSBdFTN7f7sjKWSPFyAAItpfOImQG2WVtKC9xcuFhwdZqovsAqA2tilQ6IqdqPNAT-ouUM6v5ziBCxhlPca1ars8L6skUCsvesjBcQM5Xc-Wteeh_QbXiMLWyvkUbv9t8h89GvnmpPJ9J44H-dSOMOc18ABkTsCwYITWOFHJSaNw3ZLnhXkaULjWNTED_kVc3ia7jNtaqp1xj27bgwx8mUAqXOEcj5swiAGCdDt6yLztcUVXl5vbpiA2OWm-6_38ZBw8p947ZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
پایگاه‌های آمریکایی‌ها در منطقه باید تعطیل شوند
🗒
ما با پانزده کشور همسایگی خاکی یا آبی داریم و همیشه مایل به ارتباط گرم و سازنده با همه‌ی آنان بوده‌ایم و هستیم، لکن دشمن پایگاه‌هایی در بعضی از این کشورها احداث کرده تا تسلّط خود بر منطقه را تأمین نماید... من توصیه میکنم هر چه زودتر آن پایگاه‌ها را تعطیل کنند
✍
بخشی از اولین پیام رهبر معظّم انقلاب | ۲۱/اسفند/۱۴۰۴
🖨
نسخه کیفیت اصلی
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/672129" target="_blank">📅 14:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672128">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-text">"نه به جنگ" گفتن ساکتان جنگ رمضان  در واقع جبهه گشایی برای تجاوزات اخیر دشمن است. اینها پیاده‌نظام رسانه‌ای دشمن‌اند. دندان‌هایشان باید خُرد شود تا به‌یاد بیاورند جنگ را دشمن شروع کرده و ما در حال دفاع و مقاومتیم.
@yaminpour</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/672128" target="_blank">📅 14:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672127">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9g4SAWFnAps8gnb3cDtBblKD1WZwq5985o7-DMmtAtuGn3dy07YjOY93o7ev2NtShoJ-t6rbIyyTZAtb8FHzvROtsWyIaTaX8lgIiUUthlvLYS_OGMJCSZ5lAQLukE9-uUSL24lypRdczbkqhhItWym8EsY8CdzdjLoGTrxZF_pRswSSPTKKjF-VRvCqPnRnVg3yKl_6HzAejTwUiWvEWoag4PAzwsnPE7KHM2S7iGjvWarX0p7C9Kvc5mBJZZ-g0Y-5SJz82W0qa2aTNZ3PX2fYWbcz0d7d6hqbpfCC5y7KkXwqnGlKXMqqwrhejgsaXSU_-nt8_vFbqw-xdKYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تصویری از کاپ قهرمانی جام جهانی ۲۰۲۶ در نیویورک
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/672127" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672116">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-yfiMkObJUnNrxUdteAvfIWw-CTI-Ege5SEimRI9jvYicGnL1onFapaRZFAKV1RkwwSY2lUYNeJhe6hfM0chTsedKeFBXAI_RI_hC2RPf3cPm9_xnVLduBocp_cuh8yIA8TIPiqqaJC5w6X2EHAsiNZyeYxYhXPzFkaEPoZzYyArQHZmCZswtCYHAhW2oLgqpUBG_-dng9WUBEMDi7zF7Yq0Y_OIzhpn7U5fWLQwU_TOK_8L5m7LJ6haJ-IeOMFnr8bWjYz6eqbUV27_HjFX77JorAeoFbEvWGcV6NfEupwKLKA0qs7DVVHa_O4G-FTb794Yru8RPB4yXS3E-2STw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPp83XGcE-6EYGQ3iSwguFxPVnkeBoNPU-sy1-H44qr6fWy_A5VdE--oz-6ZXG2HxZW2_mo3F7ciZP4OjK5B162U5aoUvWysC8ZYYaVVRIPv49I2wehRgzn8exGrI0DLuz8wqwsrpJSLm7rAUhYai---2XI4cwtFX98fpGJhJBUKnJAykf3UzrM85yJgm0PsLon3G3IEFkS2dSldPURE6X4BXEm2a_Sryb93q3sMTG9qfptoUqQWIaqzQveCxq9jOOSMv6RCTUhp-bIinydNxyhXtcO3EW1wPOzJwjJckrRwVMZreMQF7MRKCoeKsAoX2PtyINGP8pv1MzxOKJntUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESr2OF-5swkRSZcxjyAVlNz0ViBCbP41YP54WZ1KLT32kcaHUiccRpbEUglyzQqjzK2SciDYSShL5MydCaa5b1EliyDieUzFEmtBVfDnMFuhKVoQ0agl0mMei2RmfpNAz72_6g9ccnNZBkEV8Ccle67PRtDjWITd3O5gIXVO_7w4JCDPH1XTji1UwnsBiBn0A-_d1ZJHCmk35yFJda4xK9cczvbnhEbHjD4tbAT52fr2jpLHKnFo0T5ch7MWr6DBrKJ5Ys7KmGYRVvZSjks_JAAug3w26UG0KYROp-VzO7Z5Qq1VHH-qqfrk2aK29vsBrhXqzoSew72C207DyX0KlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1e_Jf3Xr-HlTSgHyAqs4OyT_c2jFjCfamO2NybM_eecQmubR2Nnh8b-Zse4tcfow_vOOgiaxeOL6qqLgj30_GFTxAM5ai7gXfh-D6EmGtUdb5tMtGAjDC5eMYAyZJHpTC5su9-JmbItNJuK2x47usVmC735IgUyhopfbEgyB4U-ZV_q6omd7Ia2AgkJ1TqzFGzxLOYSS7f5Hglq41BMWfD08XDF1GAhtWxRgfOP5IReF1WlQGcMPNVtZGmxr-yH0W-yhaNZH6CVhZ7fN_FESJeHpKMGRquq1PM1I41kfykq7TLGWJFhssRV8Vv_lXqNWaKUfCSmzz76wbRMvc1Ihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPBJfARUyfyTDWw8Wd4mF5qi9aez0HM_SYbhBJCgTmYYpA0BDT1Bgo-pX2jeZFO1mF2VI6Fl_rxEEkJXfAUQCe3RT4qTM3bZPp0Hbdv5n52cJFdOABhG2cp96JwZF0XarmDKnWnGY-2dBgc4yM6ER1vhQb5v2ud5UD2rWp-cC8REu7odXyh1JiMh3tM33Ryzk0m4xlInL6qfn2UsTVj7O51wQjGgSuGunozR2nmpidn302irZdHrTk7xYy4Ll0LekZAQVSaDntgwMyJOVWyCLzFxQC3HdhVXjuTq-xYhrotvdlAW4fKN21Lcexxgjr5AL2PCixPq5fllVfkllpUEgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVeYAb-EI3gDJ7V9IdwaDrUUuIuAoodTw0OE0mxxz7PEhUwvM19bD82S7iaXieASWiIIfLxqL6B2ZsLEV21-RIdAA4K-T6iri-YD4KTd4ayLLFfyq7DGcOtK4LVH2EcdnZeI0rMMYP2OYfe4GDzmoorCmhYc4QXH1TDasFTnUAnOZpk4-pq3lRGXvN27hm-ykSnYtXstB6wyNCKOKJsc0lwWft2Mww44JamClO3_zvlFuOyu8LBmM99jCqpFWiLFfT2DOZLifnpPk6dftJCtMAtccBAmjixeARlY7xazWwE0Y6bISGcul_uDmNjcZfC7Ucozq-ZN4RAYCJwqP61VjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERPGWfRAGlcD0xgEKX1jd_5_I0PYE-Cg4tLcKqy6as862w44e2Kl1uVNodO_Bntyd9EGWVw9xCcH-lcJJOpk8Hn-U_s78PgX2i2oXwVTF-pklsk18PZVFPLaPVB3SV2JaiMRAT21QYocyNmEOfNXOjutneloWR5Cqpm4h-iXxIKV7rS-8yu5_LTM_DtdwbVH_DcP1jpqi0yncwN1I99GoYQxu2f1k783auN9bz2YsobxDExKkskNnnlIZ-k0oWh1pBv6J-1HcYGmPVP1EpK1Rb8ixJ8ujKs4_76Nm5wzwhGUZMXqUEYnG95eZy1wWbFrId3sJ4RC-V3pjbHyMFI-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPZHz8YkndHEtjGkuzFYTP8s6OMnr4-lYIri_wqLzn69TV8G-SF73LA1cetwH8RksOgR5NGfdxPjcn2cnbAQA0WcBbaYn95bHJHj_KTs_nEGPlDCBmWD1DsGSmA8kANja48mAT_L4aE55P6Xh_ECmEs6DSfF6WI6LzQHHbPuzgWw6PztnlWRhYmijlB8TW29y8ZR8UvJML3Ns0gEV2HGtZrdtIKXnhSHUm6ap5MMegbsqBmLpDeb5BGD-OyTzTolIZmhvAjxXoWxH6EmNB7HGhEx2MH1ynHah9aVBpjeysSmSHQyk3wRWqe5HWyS3QO8sKh_AI1e2h0jPbjKgD3J6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFIUlhgaedH9KHWV8YZ_qUF5snjE3OdpFEOFRfM9c9nFuwnpsPhti6Ii0XPc61pVt3uPlvvr-_PwOZG7ZommNS1rRXcXOeAlYwm7HU1zBMUwhWzgDhWTQ_f2y7dzlwxqhyuTHdN8UECVfKUeTh9Dx642BMy_CyhZA5eyONEdjHKrRcgWWLoCNOgZnQJjJ_ky6Qb7CNk_8Hs4DgZ2RPTGqy2xtogXpJ_Te8UTCz-gXoEPiGxjQG_kLmpXAAnpCHGFDWtfKoKTr26ygsD4Q_9Djdzg4p7sgzlJ5cmzBD426v-UcME97xtqoO_hpvwZxdnA5nLYxyaKPQIvAmse9wPVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_Wrl6VJKQxX-_mqvs7puKYbStAqhSPAiNZpDAng_T3IyjW8X6ddOJ4TdiXWGMOkPrPlCE2TyYSvnBY48pV0-4kds62jAqjvsiCe1vIg46Dc_RvH4XstqMaA6qs0IyZhLFaJaZ76ehJ228ufxqzX90x-aHF3RjEZ8w3BQtrCpK_oOV_5cmeUdexWVdID-fKMDcvlr7HnQ9uh7nP9-PeBCzTfO3KA5C4h6Wxn7H6C_7V9EjzrG6Oi6dzHyMefzVqka4N1MqzpQokgNKdw-jakA5u65XQjGiJioE_jEL8s5gDSoo1MvlS-seBA_nz1r532pCPa2JfgluKO-w4S1wCmHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت‌های ارسالی مخاطبان خبرفوری از قطعی برق خارج از زمان اعلام‌شده
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/672116" target="_blank">📅 14:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672103">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msbNhsPPQwDcx4wTKOaoHVTkyIFaQR_H-XEtQe3kS1-SclAam_qhGr8jicstccLuxq04tNxA4dy3tT6UxmZ1Z2FD63Ec7OfQyyF5LWlA_M5lTEcr-sq93jA0Z5qkryWjumHFdaiGlvhsPkORUL3iWLKqQo9cBgqhJ1WH5cl78OBLcYhAmQJ7Isw8DsRDW6NNOOMX3ouxAJFuKkXSGMjUT3_DGGGq04CYLBSEvNu3xPpj-pMj4AnwdAo14FrzI2xURTZEuSDvIdljmmQc4YlxBEdz9Zvu7k--em6aGoNBHUFC8Cd-xZt1EjU_9gIlhMbUs5qLcD5xNoPXGC_E632nyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای دروغ‌گویی اردنی‌ها در رهگیری موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/672103" target="_blank">📅 14:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCzUARU6Qkqz7zg10OYGmpUjV0lX2wuJHl0mx4_LPzQFawLi9r80YPF-qQvd-wABWVEaq25bYs0L9Mc36bAI9mYb3BibuM907immUkm050FQu0fyb7ReHWpfJZ_M4g9kWZfd3Pzva9Rx2T-8N5VSwgIgTD8-zMeoRrxhZW4M28vEoOsowQOWQw2foC2ESXKyvYecy_FeEUWqKw1EFS4eVq0QSAv_F1mBjPxalm1Lb_nP3ZfmAoVKZXMqfBkvT6HMrtArRAQgMNUaU3k0zFHhI5-ssHd-HZ--UEQ5qZYFub5oF0776YYhcfdKCw9MkAJIE6YkAOwEPfi71pw_6V6CSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میثم ظهوریان، نماینده مجلس: یکی از عجیب‌ترین و غیرقابل دفاع‌ترین تصمیمات کشور بعد جنگ رمضان پذیرش قطر به عنوان میانجی مذاکرات با آمریکا بوده‌است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/672102" target="_blank">📅 14:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672099">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF14xEPYA_gyrl3KE3Wr5X3u9Ndj-5jGkOzUD__CXTsG1F9YFDH4IO8HthJJF8UX9XjdxipAAt6AxIvvh4y8VSaobTJDMIg1aQxIm_dSZP4R2xDMAevaHCpJrADlDtNu9yiTFhlBkGlt4gce1t_LG947NhkUk5ZChQjKUfUfKvvEAgkqU8DQAvePVrTIicLbUZht0yCbGcrrimdSordrVlLlE6IbwcyCWCjFGB6X8QQVEiScv4MAvrqJxjVTNOG0mYEX45YxIdBWf1Pxps_yJrsf0rk6GqV7hEj5axk_LfACdqIMYM1Wm-h79hlCMXXFCGN7dQ5y06X1tJi6AT9_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلیمو برای استان‌های همجوار خلیج فارس رایگان شد
پلتفرم فیلیمو با انتشار اطلاعیه‌ای، تماشای محتوا برای هموطنان ساکن چهار استان جنوبی کشور را به مدت ۲هفته رایگان کرد.
در متن منتشرشده آمده است:
فیلیمو برای استان‌های هم‌جوار خلیج فارس رایگان شد
❤️
ایستادگی قهرمانانه شما، داستانِ فرزندان امروز و آینده‌ی این سرزمین است.
❤️
🫂
تماشای فیلیمو برای شما قهرمانان حقیقی ایران، هموطنان نجیب و خونگرم جنوبی، مجاوران و حافظان خلیج همیشه فارس، در استان‌های «هرمزگان، بوشهر، خورستان و سیستان و بلوچستان» به‌مدت «دو هفته» رایگان است تا شاید ساعتی را در قاب تماشا، هم‌داستان شویم!
با هم از این روزهای سخت عبور خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/672099" target="_blank">📅 14:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672098">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=bTQSML_4G8pxWV3nE0BKsNUHSc8aBcnWry0e2pDmu-sYj3r2LlnAymda0WaRIV6mJCmtqT0lRfZVWfGQtMf-V7m3sqDYXk84l5O8WpwqAzKQI4aw60j2A_Lo3iiekBNyzsnoU2-1To4SS34YfsxtLe6zdK20Baog9eIxCFtw2Cl77TcQ4uQxff2qGTmZQ70qp5H4gIWAZrwiDK1DLHmRhFLnvc8Z5-DlsvQzFtkCPQ-HYQfpm41EY5EwoeKgz7s9ER8EmXH2Fedkds8vPVwj_YN-bOPDsxvyBwvugBn0eKCpeIvmQdw7w9R7VMBMXPdmYSaD9_rE8gj6GL59eHRoKSANCTH7vCsjqbOIj3f4x5X-tpcvS5yyddK2svImcadn9Mh8bEo0xAWEWH2fnDYfhjP4F3-I_tmM1zzUcyUECERiIaaTdc-HTx9-vfpiaNEkqtCH5k6oDXApZJxh8GU7FHFly1rryilBzWbJAX9UuKWh7Uep6xnbyxxNkshzjMpZOm0BBGfEgG2vmNY2gFV_YKg1e3dSsCya-7GKStpPEglFSPFIZHQp3M6dNbBZ_c6AVJWdhRTgNfQM0q4k-eg5HJsW1RB2MG61mWkhBiSpXpGJgHHVnXGXALBkShNkRFcbudI13fv3LPmX_OgyR-SJjd4oKEm7jLUdoEumx2s6MS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=bTQSML_4G8pxWV3nE0BKsNUHSc8aBcnWry0e2pDmu-sYj3r2LlnAymda0WaRIV6mJCmtqT0lRfZVWfGQtMf-V7m3sqDYXk84l5O8WpwqAzKQI4aw60j2A_Lo3iiekBNyzsnoU2-1To4SS34YfsxtLe6zdK20Baog9eIxCFtw2Cl77TcQ4uQxff2qGTmZQ70qp5H4gIWAZrwiDK1DLHmRhFLnvc8Z5-DlsvQzFtkCPQ-HYQfpm41EY5EwoeKgz7s9ER8EmXH2Fedkds8vPVwj_YN-bOPDsxvyBwvugBn0eKCpeIvmQdw7w9R7VMBMXPdmYSaD9_rE8gj6GL59eHRoKSANCTH7vCsjqbOIj3f4x5X-tpcvS5yyddK2svImcadn9Mh8bEo0xAWEWH2fnDYfhjP4F3-I_tmM1zzUcyUECERiIaaTdc-HTx9-vfpiaNEkqtCH5k6oDXApZJxh8GU7FHFly1rryilBzWbJAX9UuKWh7Uep6xnbyxxNkshzjMpZOm0BBGfEgG2vmNY2gFV_YKg1e3dSsCya-7GKStpPEglFSPFIZHQp3M6dNbBZ_c6AVJWdhRTgNfQM0q4k-eg5HJsW1RB2MG61mWkhBiSpXpGJgHHVnXGXALBkShNkRFcbudI13fv3LPmX_OgyR-SJjd4oKEm7jLUdoEumx2s6MS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد/ دولت پزشکیان می‌توانست فیلترینگ تلگرام را رفع کند ولی متاسفانه چون پزشکیان روی وفاق تاکید داشت این اقدام را انجام نداد
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
دیدیم از طرف مقابل خیلی مقاومت شد و هنوز نتوانسته‌اند باز کنند. اگر قرار است بسته شود باید به شکل قانونی انجام شود و اینگونه نباشد که یک نهاد امنیتی یا یک نهاد قضایی اعلام کند که فلان سایت بسته شده است.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/672098" target="_blank">📅 14:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672094">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تیزر قسمت چهارم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حسین حاتمیان که به دلیل سقوط از بالای تریلی و شدت ضربه به سر، روح از جسم جدا شده و قدم به دنیایی بسیار زیبا و دلنشین می گذارد؛ منزل و باغ بزرگی که متعلق به ایشان است را رؤیت می‌کند ولی عذاب دردناکی از دوستان و نزدیکان گناهکار را نیز درک و احساس کرده و در نهایت به دلیل سلام دادن همه روزه به اهل بیت در دنیا، از آنها پاسخ سلام را در برزخ دریافت و توسط نوازش دست مبارک امام جعفر صادق(ع) به دنیا باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حسین حاتمیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/672094" target="_blank">📅 14:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672093">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f48ceb9ad.mp4?token=JvJSPw9k1WGS2PkLPY4wAohTo7qNzlfHvrvWP8ewst3KuaLZ2v66ocj93nKePMZ-jMvwibFdkYNxlt_FyGYiZJGkiY5Ko9xVCMuRPew64dIwis3D_Qytr9uLj2sh4SuSwyS6tDJslece2blUKS8yYZ4Y16clycs5kHDbTbP_SVYwT0fBZ_TS0iE8BCArBRgpgKhk3DDyYxpDKRznWr8kz3j-me_S5ChB1_BCSRz_KCQe0DPs6HC5hNDrRwQ8mBHUBV7NMKzgzyR7Bt-Iw9VKjpr0Lh2Hbuy2PfpJqkJvmHrWBlvH-9gwqBPw5v685BUG6c7cci7zJFnMcsK7xv0eIDM9WyWON_u_r0_uDSA9z-aMEQmnscxRqED8Z9hruOI0xMOKr2XYrLk0Z0ScRixWIDmGRtMR41ugVJ3wYevTRA2GLFopU_m7fDw_VjNW9K-UqFFMGdXwfxeT7FzS8ixweq-jNy51nIwDIOhg8J2AGxt__5MdgmRVMnmwn6yopTkXPtPOGRCw-K2CeoMtQwaclCJ42c58DerjR1FqmGtkEPwkdBV9mbBILO9qpfBVA58gSjBhhDjdqx35oDxpghJaykfVFweG9aH6HjGlwdq837RLG8fnR_SUnrheiE8UkWgNkbgnpHn5MQHBSwmgaYKx9y9eSW7V9OKqZtIYni8IabM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f48ceb9ad.mp4?token=JvJSPw9k1WGS2PkLPY4wAohTo7qNzlfHvrvWP8ewst3KuaLZ2v66ocj93nKePMZ-jMvwibFdkYNxlt_FyGYiZJGkiY5Ko9xVCMuRPew64dIwis3D_Qytr9uLj2sh4SuSwyS6tDJslece2blUKS8yYZ4Y16clycs5kHDbTbP_SVYwT0fBZ_TS0iE8BCArBRgpgKhk3DDyYxpDKRznWr8kz3j-me_S5ChB1_BCSRz_KCQe0DPs6HC5hNDrRwQ8mBHUBV7NMKzgzyR7Bt-Iw9VKjpr0Lh2Hbuy2PfpJqkJvmHrWBlvH-9gwqBPw5v685BUG6c7cci7zJFnMcsK7xv0eIDM9WyWON_u_r0_uDSA9z-aMEQmnscxRqED8Z9hruOI0xMOKr2XYrLk0Z0ScRixWIDmGRtMR41ugVJ3wYevTRA2GLFopU_m7fDw_VjNW9K-UqFFMGdXwfxeT7FzS8ixweq-jNy51nIwDIOhg8J2AGxt__5MdgmRVMnmwn6yopTkXPtPOGRCw-K2CeoMtQwaclCJ42c58DerjR1FqmGtkEPwkdBV9mbBILO9qpfBVA58gSjBhhDjdqx35oDxpghJaykfVFweG9aH6HjGlwdq837RLG8fnR_SUnrheiE8UkWgNkbgnpHn5MQHBSwmgaYKx9y9eSW7V9OKqZtIYni8IabM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر عملیات ترکیبی موشکی و پهپادی با تاکتیک های ویژه و غافلگیر کننده علیه مواضع آمریکایی در موج‌های ۱۰ تا ۱۶ عملیات نصر۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/672093" target="_blank">📅 13:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672082">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: برخی مسئولان امنیتی با پرونده‌سازی برای افراد تلاش می‌کنند انتخابات را مهندسی کنند/ گاهی مسئولان شورای نگهبان فریب می‌خورند و به نوعی رأی می‌دهند که منجر به رد صلاحیت برخی افراد می‌شود
علی مطهری، نایب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
گاهی مواردی را که جرم محسوب نمی‌شوند، به عنوان جرم جلوه می‌دهند. دلایل رد صلاحیت آقای لاریجانی خیلی سست و سخیف بود و در دوره دوم که ایشان کاندید شدند دوباره ردصلاحیت شدند که این‌ها ناشی از مهندسی انتخابات است.
🔹
گفتند شما در نطق خود گفته‌اید نهم دی اگر باعث تفرقه شود دیگر یوم‌الله نیست، بلکه یوم‌الشیطان است.
🔹
رهبر انقلاب گفتند که اگر امام بودند (درباره موضوع حصر) خیلی سخت‌تر برخورد می‌کردند. به یکی از  اعضای شورای نگهبان گفتم متاسفم که شما با این افکار عضو شورای نگهبان هستید.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/672082" target="_blank">📅 13:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672080">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7D8s4m-BiR5gKF23Iye0rGVzqjk5Mk7ogWUqzd4r7EzgyGsGvC8BWSazM_tcClOHAFq_aSBF45K9DtaJOm0cXgc3e5ioElxP7p9bJ-bBidGT5wmXmywIibAcst8xvnf6tlXhdRdp066JgispIQ8tS06uKnBwdNa2iD2VE0bQftsTWs3SyPC0QcKU8t1LgAfaGURN9BYLRlfnr-nxA-RwWFO6_HtiVgAlDCnqLdSmtE24ZHMnkmzlbCARpVsbxX6ru25VTqrFv4G29PhRDI8hmzQGxz2zLjNEJu1C9XseWZ0THJtPgZiz7v100UC3lbT1qiXgJ7h3drFj0UsG-OSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴ خاصیت سیب که سلامتی شما را بیمه می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/672080" target="_blank">📅 13:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=J2PUNRXcirImWdNgiPIH5Bqqto51bcSxi5tHO4ejDSpoO6ekUPTHqhdG0aT_huH91enqF6T4RBouJOcWjzKDnSgculPK6GEiLMBann90VOLVy2McbcA_dYQjkdwv9Zly5SxnSr6kzqkfRnOuZim13VsP4D9r7fxeqcQOkuI7s_5-3cbD2bCOWc5VloaJ4zFlB05K3Rn_HlEOhT7tDaY0_R1kMT8Y17ViXDBrweCQ1QKDS67rC8DxeWo4pnASnfpvSXOYcxcZ9_w9fTgyx4KL-4WYscXXyrcQYW_YuYC_7dwLVM8E1vIOsPzaX0MITSX7pFO1ZbsAwKbBaRKgof2kWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=J2PUNRXcirImWdNgiPIH5Bqqto51bcSxi5tHO4ejDSpoO6ekUPTHqhdG0aT_huH91enqF6T4RBouJOcWjzKDnSgculPK6GEiLMBann90VOLVy2McbcA_dYQjkdwv9Zly5SxnSr6kzqkfRnOuZim13VsP4D9r7fxeqcQOkuI7s_5-3cbD2bCOWc5VloaJ4zFlB05K3Rn_HlEOhT7tDaY0_R1kMT8Y17ViXDBrweCQ1QKDS67rC8DxeWo4pnASnfpvSXOYcxcZ9_w9fTgyx4KL-4WYscXXyrcQYW_YuYC_7dwLVM8E1vIOsPzaX0MITSX7pFO1ZbsAwKbBaRKgof2kWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرائت دعای سلامتی امام زمان(عج) توسط رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/672079" target="_blank">📅 13:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSS4IkDqKDFdnOw_SE-Vx5jV_3S0ZhZwD7vYATOrMWFPPJ0oPZ6Zzpg0RRY6gE4w4V7vaGXSDsiaEsiGWNt7VTz6f9_TJbqINQU0P7Sz56WCPe6YeoQa_YtowEaDLBWGVzkw7xgIJIdOHhstAIMmgilv1nwg3z4NaiQbtprXRo6HyHjw3QMMcUA3KUbhp1hqlXCBYILL7lmXJxUUe0kxqUHiZMztc_REnAOOmv1JxIz0wKxaZbs__RbQuEnDKboN-2R_tNRIDx7wUlamueWKnNjaYxJjv4x8fT0JE77Nm8UlwdmyKrV249F_uXOd6091zEFljecfeGNqChP0hYX_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اشاره عراقچی به جریان نفوذ اسرائیلی در امریکا؛ همه این‌ها به‌زودی برملا خواهد شد
🔹
به آمریکایی‌ها مرتبا درباره «نفوذ خارجی» هشدار داده می‌شود؛ پس در مورد کارزار گسترده اسرائیل برای فریب دادن دولت آمریکا و کشاندن آن به یک جنگ انتخابیٍِ بی‌فرجامی که حتما پیروزی در آن نخواهد بود، چه می‌توان گفت؟
🔹
بدتر از آن، اسرائیل از پول مالیات‌دهندگان آمریکایی استفاده می‌کند تا هر صدای منتقدی را در داخل ایالات متحده خاموش کند.
🔹
اما همه این‌ها به‌زودی برملا خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/672078" target="_blank">📅 13:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672076">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا به شهروندان خود؛ به عراق سفر نکنید
🔹
سفارت ايالات متحده در عراق با صدور بیانیه‌ای سطح هشدار سفر به این کشور را به بالاترین درجه افزایش داد و از شهروندان آمریکایی خواست به عراق سفر نکنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/672076" target="_blank">📅 13:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672075">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند  استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/672075" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672074">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
تعویض گل‌های مزار مطهر رهبر‌ شهید ایران و خانواده ایشان در رواق دارالذکر در جوار حرم امام رضا(ع)
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/672074" target="_blank">📅 13:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672073">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: شهید لاریجانی ساعاتی قبل از شهادت با پزشکیان جلسه داشت/ پیکر شهید لاریجانی چندان سالم نبود
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
ایشان جای خود را در خانه آشنایان و اقوام به طور دائم عوض می‌کردند. افطار همان شب پیش آقای رئیس جمهور بودند. عوض کردن مکان‌ها به صلاحدید دکتر لاریجانی، فرزندشان و تیم حفاظت بود.
🔹
این اتفاق کار اسرائیل بود چون ترس داشتند به وسیله علی لاریجانی توافق و نزدیکی بین ایران و آمریکا اتفاق بیافتد. هروقت احساس کنند قرار است با آمریکا توافقی شکل بگیرد، کارشکنی می‌کنند. دلیل اصلی شکست خوردن برجام نتانیاهو بود.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/672073" target="_blank">📅 13:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672072">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8bc8dc64.mp4?token=Ev9Ex4jzSy0LWw_GXfAuhnlHsl7mDb2gmCvMpGsmhJOQdmtc8K_-Qe-tCWnvyWIygRqAiqDfhKimnRQ-oNXNKlcAYZze3HQRjm65BDZJO6JZOo0W3OU1HaRxPQhBYrswLseudGbjS8X0TtuAW50cAtMFLcpkbgYDAX596JajDbwqHZ1pWwH1ddrNV-O8erloF-9Qtx3Gsfkl_zJq1_jVBdl2f-58kGo4TnbavCk4u-3PmWc25CNiXcQ-tL_b8LLhfAkkccmjUx76Axr0Bo0z6QHC2V2edlWJG0Hss6PV1oiJnJHnfJrNRzRvnVvVNcnA5airDPDcHENwyErZ0_tJxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8bc8dc64.mp4?token=Ev9Ex4jzSy0LWw_GXfAuhnlHsl7mDb2gmCvMpGsmhJOQdmtc8K_-Qe-tCWnvyWIygRqAiqDfhKimnRQ-oNXNKlcAYZze3HQRjm65BDZJO6JZOo0W3OU1HaRxPQhBYrswLseudGbjS8X0TtuAW50cAtMFLcpkbgYDAX596JajDbwqHZ1pWwH1ddrNV-O8erloF-9Qtx3Gsfkl_zJq1_jVBdl2f-58kGo4TnbavCk4u-3PmWc25CNiXcQ-tL_b8LLhfAkkccmjUx76Axr0Bo0z6QHC2V2edlWJG0Hss6PV1oiJnJHnfJrNRzRvnVvVNcnA5airDPDcHENwyErZ0_tJxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم ملی والیبال نشسته ایران برای نهمین بار قهرمان جهان شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/672072" target="_blank">📅 12:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672071">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaQg__fJmj-1Pv-uLDWThEcx0m3K-N6JYllJhd3pLK_MBrICxwPF50k5LhCmEfkkTSzJu_o5uwie20NrtzOUmgmRG-ym6xTx3AZxRBIucuBUhg9DumGchQNewnkmiS7QRpKdZaRvCBe8pGlo4ZpV9mw2biAIDQTzs4KwlwB1JTrSXCr0BVp-n-Lc0yjL2nPC498p8rIBvgmcEP4FvSAunzqQvAPi1f0scyJDZpQ0f7QjHbp9CddSM5aoh586MtNEs8M5iGyM4EFh6-3tG5XfPs4Q7kLy3YkgMj4y_GiE_YWgMFFByzAwu3yN6NcxcFmgnNINevKQ_VOj670beEe87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام لانچرهای موشکی مستقر در اردوگاه سازمان ملل توسط ایران
🔹
ایران در یک حمله پیش‌دستانه، لانچرهای هایمارسِ مستقر در اردوگاه سازمان ملل در کویت را منهدم کرد؛ این رویداد بار دیگر نقش پوششی این نهاد در عملیات‌های نظامی (مشابه عملکرد آن در غزه و یمن) و فریب افکار عمومی درباره ماهیت سازمان ملل را آشکار کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/672071" target="_blank">📅 12:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672070">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
افسر ارتش صدام: روزی نبود که خبر ترور کسی را در خانه‎اش نشنویم؛ ایران بعد از جنگ هیچ‌کدام از فرماندهان و خلبانان بعثی زمان جنگ را رها نکرد و همه را حذف کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/672070" target="_blank">📅 12:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672068">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF48efWsOLelUaWj4QWQZUql0q6TNDWtbzaA9r_wqrEj-W3-VhT4aZAOig0Z9BJrOe3VazUIRF4ZkdWcVYGSw1yJtnNahO2xBNIZ2-FxbpIN93SwJ_E1D5YLZ3scb_UJ7HEOIMZlL0Lymq7pAaHtpqaS3jWK2Rj1WMsESgheTekdjpmZ9V0pzJk8yIqy2A-WGpMRU2QRs_IcvChlHvlidUCJevO_78UssHE_7G_c4KknVNm5IfWTT7E8co38F2_syAqCLkDEJcWt2Hn0z8YJD682h9uhtBWIqmhrOZt3F23SbtBpQwXNKm0C46vXk1MIW0SKSJpXAoqa8PXayY5f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد
🔹
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/672068" target="_blank">📅 12:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1DRes35gqWz5Lo81xponQv1iqmDtl_ZIULBHg3PDWlALDDtMxca4Hi1-bGeKpP6AsDKnTAzeJlepOUdkRaSBUxEvsQDlNGpWl7isTycq_SBlp2_cwGqYaaIJiN3jlwaRTuwvbpw0Js1CFM3taxK98La53HgsGdnnbDojc26GTfVmPy3uA6AzOWVCbMTmqIyILzlqOCaptNjSlpILIWwWJqQ-ffnNT85Dpbq0WVx9QYeSHqO9jTecXmUs3mC_qEviPOoAvpr5lTbEnhan--PRl0_2egaSPdHYVDrHif7xDh2FoOLNmR2lqb9-AnuQ9M49k4bUZWi5Rbmbkv_wrUphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBxFyh31G-IXcoUa0MgVxkrO6FZmlL-Ejz398Uz6jXnwEc_T4rqmJVNr8QF-aTn16AG0kVjCREuvdsn8LHhJfzsKSZ0oUh1UyEUZl8Bgaqtt25qH_Qsc4ISC7AujY6NDCejDyvY4HEO66S5gsySURKIbe7pztyTy8IhmUCk85QjhbdLV3-ad6XPTpy5bZ1pFOmimoS8rfru5QML4Inpgw4djFmHgUAKmGe9w_YfBFK7ClmGmoJT7Z64hrGVAZdALK2h-kOnwGkJ9eNWskXPhDoizH1h3vxTQcD3U0NXRPPeOHAxeiftriqARGbegvWUqbSr5AWY3SYnu3TfMBqlANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4cQjdWi-ZFv9CcgNX_a4N6Utc_0Q_gQqNATFfU3DkZLeZSzLl1bGP28fCH7Iptt3xC5Hgep5BnR4Pc0OCoPat2BoGhl3JKP_gdLLtWrz02rp4noZX1dZBB1PKwyMcUIgQ1nVe4zWLym0F24lAvGFtRdGgsigkrBiZnbTeAFtYHjtg3o8wl0LieOev4iu0VA4X-UsFFtrGe9Qx0APSlAOEMqObJQL6Tu8fjF8RXq8hpfNuuYBJsasMOKyZhxptTgWgEBn1vrcnI_xfWG4DpeKxLuGnn4mVF6xAC-tnD4ZL_OtDIf9O-5KCOdUXEu30xIXAFbQuIEU-_15B59EP2R9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8cUuZWg3AM9YUOY5FTv_MI1nEyX-zGQzKP-kTv3xRS_MVq1I4ndT6N5rSeRNnV2NqjyLZVsWQqpO2EqgYq1jD2LY-IcvTUoQgra2NZGJet6sKWgacMaiBBRNj6NBD-f6NIjAGhjqmjELMePpcxknFH6ZeoivBpkKErTqpSnc4Vfbl35bwuAwXlK3ctjQs-kfAB3u92fey46l1OPIxQ1d-nJEmjzteKKPILCzRI8bIHMAZXA0MDaqpIa6GsOiocZfpQJVN44qI1sThq8-XjAsA_UbSW3J5t2ClmoQE1j5fMtWXm0yqP1-Y5lgOErp8gbgwTzvCDjwV6UIaWhKJ__ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlX-KvBf-k9vD3QvcldF5q6zLQkEmffFgk1Mc4J7Kb02R317Q8rkdQYFvjPH7920pPwBouyQG_E5uuURe4bDkxoIzOxoozpxKA2pPg_SJT2NkhX8qI3tFnpNrDSqaz9GbPZ-QCarTM6KGgYMh_SR_89bjpf_KwoTfkPLbb_W32Bmv1_xngJS3KBp-edTlTmrbmouUXrbnimNesT9IB9uRtLx1aqWu2ZOdQC2rsxsYEbakl1jAiE2MAovxt0Vt_zeDJbIVofCMj1Oa0JdUkKww-D8Y3dTvX1gAa4vqpV3Itl7c6IWZT68wlYTZmyGqz5r17ojrzPUjJ9Gc857Xod4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uV2tFHKkbYQQA-ymqmXwipAlT4n0Nu87-ILWGRjQG9epIjBb0qiSYVh6iRTr6FtnB0OQNaYUh9cTB2TtWhEsf5IsDhIikhl_AXThHWokmW3gyMKBcL2F84hJIUmPJQdBLR017z8FByIlOBaLRW5f56SCBLg1PI945exe9aPzBENln4JvTxCMTpTJ9-rCGtmE4k2rTiXqZNz8kRlDtX1wvjRNok8ZCx-p1k4PLn_s4tX-wNGHxuJKtaTICFSJbIpe55UvQBxASBSm3NPmTo7XT0L3N6Kf82fe3T1vwYlDvO_QQTsZfLQVG9Ki69kcsx3p1Wtyn5IPb-q3RvGwyBN32g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افشای دروغ‌گویی اردنی‌ها در رهگیری موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/672061" target="_blank">📅 12:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f51880bf.mp4?token=ivIqseVfjjM9eihXX555qP50Os6_cWhg4qkj3444SwfJeFAGB3FnlJ8bLyJ4ifhtRyvdrW5bT8rHVB89TduxDvjbA6vEbhJpRBqart_5Oof0nLGJs_Mtr1CJJP7oOXkyFj27xS-7QYjGOr546gypw6IQvGVEUimZFzDpEdqdyoOdi5MsUjLct4gm0Uvdgs9KV79U5OMqib-wmCPmDC7TLtl3952pf4bik362dbwrBVuQUwFvB3jORYZZVV-9cJJO-iNIhac3vNoHVSaJmVCqzJ6IUWojTcdI-RzFgZ9oYYOus4bGfDTnXttSTIV08eKJ57sRQV6t_3-a-qffPVcm5RKdhfmTz3rZN0irQv4G4uhiWCjIMuE-j8adb8WiBT32mqIPegbbU0ymVgwSuoXdemTSIKILNZLD3lCs-rxQ0XPrhuSsCntIi3llDm5USis7N8R4OCja8DDD7pQ2oKP6qUnkHSwI1twINe2IefkZObfZqKgLHzPTOWqnK0x0KGjdwbN3DTb4u2rcaLvVxSlAKyVdYilY7dGduzwttkvzpdapH2zNrCM3WSsJRRsgfs5cQhmSDMrTL9HeG7FhLWMozOXH6TEk636BZKA9Rm1284wCOc0KqxP9VRxtin1UW23wwrXbxKZvqnxV4XZ4O2-1viKbOSSlCTHptEHtgQEDyEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f51880bf.mp4?token=ivIqseVfjjM9eihXX555qP50Os6_cWhg4qkj3444SwfJeFAGB3FnlJ8bLyJ4ifhtRyvdrW5bT8rHVB89TduxDvjbA6vEbhJpRBqart_5Oof0nLGJs_Mtr1CJJP7oOXkyFj27xS-7QYjGOr546gypw6IQvGVEUimZFzDpEdqdyoOdi5MsUjLct4gm0Uvdgs9KV79U5OMqib-wmCPmDC7TLtl3952pf4bik362dbwrBVuQUwFvB3jORYZZVV-9cJJO-iNIhac3vNoHVSaJmVCqzJ6IUWojTcdI-RzFgZ9oYYOus4bGfDTnXttSTIV08eKJ57sRQV6t_3-a-qffPVcm5RKdhfmTz3rZN0irQv4G4uhiWCjIMuE-j8adb8WiBT32mqIPegbbU0ymVgwSuoXdemTSIKILNZLD3lCs-rxQ0XPrhuSsCntIi3llDm5USis7N8R4OCja8DDD7pQ2oKP6qUnkHSwI1twINe2IefkZObfZqKgLHzPTOWqnK0x0KGjdwbN3DTb4u2rcaLvVxSlAKyVdYilY7dGduzwttkvzpdapH2zNrCM3WSsJRRsgfs5cQhmSDMrTL9HeG7FhLWMozOXH6TEk636BZKA9Rm1284wCOc0KqxP9VRxtin1UW23wwrXbxKZvqnxV4XZ4O2-1viKbOSSlCTHptEHtgQEDyEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: در ماه‌های اخیر که نظارتی بر موضوع حجاب نیست با موارد ناهنجار مواجه شده‌ایم و دولت باید به این موضوع ورود پیدا کند/ ایران قرار نیست اروپا شود و نمی‌توانیم به برهنگی و بدن‌نمایی بی‌تفاوت باشیم/ قبل از سال ۱۴۰۱ حجاب در کشور وضعیت خوبی داشت
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
حجاب یک اصل اسلامی است و نمی‌توان گفت هیچ نظارتی در این زمینه نباید وجود داشته باشد.
🔹
نمی‌توان اجازه داد خانم‌ها و آقایان، هرطور که دوست دارند، لباس بپوشند.
🔹
اینکه مسئله پوشش در خانم‌ها و آقایان به تدریج به برهنگی و بد‌ن‌نمایی تبدیل شود، چیزی نیست که نسبت به آن بی‌تفاوت باشیم.
🔹
برخی اقدامات ستاد امر به معروف مانند مقایسه تصاویر افراد با کارت ملی، ارسال جریمه به در منزل و محدودیت‌هایی که برای تاکسی‌های اینترنتی ایجاد شد، ضرورتی نداشت و جامعه را تحریک کرد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/672060" target="_blank">📅 12:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbIe5H-fG9msX32QafKFeS_hU6XqtPR6WtJqgeA6SeykKwDjdUrqIF_RMhRoEKdDy750fWY3aYDemT67RQWCaIl3yN_9JOUj4qyhnAledj_Mb_QpyaKxrGb-m5bXVq4RJ0eFSMQyxAlNF8mriwp8K3-OZD9h2hWI-j6YlgbGygTDNrYYyhHefvgFjpbGNuQMaO8un9gKuOnxnEohJFQhAfFwrBHQAqqFhM8Xj9KQA3EqCj-vDNAVGx18uuEOR3jzOVUANeENaRpNos8XN77UbnIcDA8ST6-z9odadh6DNUxdMyuJv4lVnsD1YB3MkYcSqMnEo_CDpOcsR1xVvcmhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این مطالبه‌ی جدی و قطعی مردم است! خونخواهی قائد شهید امت و مجازات عاملین جنایاتی که علیه مردم ایران به وقوع پیوست
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/672059" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672054">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تشدید عملیات سپاه در اقلیم کردستان؛ هدف‌گیری مواضع تجزیه‌طلبان و تأسیسات گازی
المیادین:
🔹
عملیات پهپادی و موشکی سپاه علیه گروهک‌های تروریستی تجزیه‌طلب در اقلیم کردستان عراق برای سومین روز متوالی ادامه دارد.
🔹
این حملات علاوه بر مواضع تروریستی، تأسیسات گازی مهم منطقه که با پیمانکاران آمریکایی همکاری داشتند را نیز هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/672054" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672053">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcF6-lYdCN415gJfRJ_Yfxofte75fIFPJOEZ2fr8lHDun4dvHA7leYRB1pkVBJAtKouAWRPczYI44W8EJHEYtOGljOVhpYe1xIBr7detyP4g5wPxOb8VEh9ZMkR-IHtNn4W7IFtRf_DXLsBA6AcQd12UyCts7LZzwONbqhvI7gAzeBeLkUJNe2ZYHX1jvSOWfBOnzvQuiCTrYR5M8kcVk_4YIYddH8C7RsWni-_Q6BnKAURHEH9hVbNDZSzlTagZ_QG4ODg5rehj4dklA9fzpm2wNl2c3VotPwj0tC0QFDXBHG480ZlTD6Z-NxQT2RYIspwQYpoZK2m6dmlxU6p77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فصل پایانی امپراتوری آمریکا؛ ترامپ و کابوس جنگ زمینی
تحلیلگر آمریکایی:
🔹
ورود به یک جنگ زمینی فرسایشی، تیشه به ریشه هژمونی آمریکا خواهد زد و فروپاشی آن را تسریع می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/672053" target="_blank">📅 12:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672052">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تجاوز دشمن آمریکایی در تپه الله اکبر بندرعباس/ ۷ نفر مجروح شدند
🔹
دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
🔹
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/672052" target="_blank">📅 12:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672048">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dr7R3WM4XGK-kq40X6KuJgy4WFISQmMck9zRp9YaOrKW1omY1TUd-ZIJG5AWCeA8gtQBCLZcMp7v2rzU9KxIjcmmWN3am_9Pnb7RbNock2Z1Gy8V3t71XQotE-LQKZiXZAjfXj3OU0TceDN22AQgMXRNi5ZEf--owQ9aU3WBi02y-km-_sHrggZdyF5KC86mBCaoYpSUtjujOypLvuOZCH7nXNxB2CQ_DuAvLB5-e08NbUb9R-bVw3RhrmCYjt6OYv9s3nC6riZmBJcjj7Nlxt_PgIuQF0UEoOyVXntg1Jb_mUcr52ww9geS0ZgpQPJukPLyxI7SgmqJL5L47RWm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYM04zD5XPSIUZGr_ZjwfzoH37bXt4ZfIksjvLYd6kTQRJ9K8A93o3N_IUhyEYwtW2kyYd9UL9ZNP5JXRzkmluj7n5npKgrHC50GbA0dNn_lrDA9bG7lp8L94z7G_1NgmoKbDMfAuKTwOHIlJ1iP701suMtRDQcSBzcO2gVChtFx3WEeeB21ESgU7gGcAVY8xvo8XBj6iDv0FsyQHPJQgI5wyg4Kf7wy1hOm7tHkNlX6EZrpUWEWI20Xt8l1bLdxqQSSdnX-B0u_5CTGALDerJ00K7imrjo6YuigxMm7TQWZuMoLFO3jYEII4omwswlMWHjXVCE7pjCvbhApzYRjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0vtZrQIkzZa9ahfCOm6_w8srsqw4LhqFdPxcJrBUxSEggAu9VK0l7a9AzzhRMOQpFiyi9oBbnCGxhq0rjSEVGqEMJWScVVS_-lZzKhZzFv1Uv13nQU1ti5QNjh7N491XUliRMHftdoUC5hdWGtpLGEcM3a4PDphKpXDQLcYvQvdfOiEX7DHv_lzx6UHl7HmPvAJFLKjUa90Cv8e0tl4-peL4H2TH8fnJHfJQS1CqJW7-2lVJU2hEKpoV7WVvRkY1qjrmYlu8NLpuxG_YkqfSvF5CUZd62GRprYjuEbd4pPECrr2y4ns4TqSEaMx1-DXSqAmjiNzLGevwOGmF8n2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjjS71GHEWN_QtI-UmE2ap_AoFtzPUYp5Aj3_w88WGRCb682T1phRVdReSbQJjfQdDP_fF3k2I55AmdQexOd8cwVqjpANCFQms7UsvzD0qBFKAy5B3gxcmi6aWVvcseX_9PMVPyWTEUNGqUSdEq3LDK6Vu1wz2CGf7v5yqaT995wC0xzf4yiPFmZ22oQ2T9WiuQFeVpeNPqCzWDuZz62pa9m7I4_fyRjsbvZRWyZr3Q-V9CH9aEvHweY07C5occOyEFjGn3u-C6HpLPDtULftjWdayQhW3KDWSWPvl8cLthe9RaCNg1PxJGEL6id723N4fR-i02yWSchfe6eXosUwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زیبایی کوههای مریخيِ چابهارِ ایران
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/672048" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672047">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امنیت خونه و محل کارت رو همیشه زیر نظر داشته باش!
🎥
💡
دوربین مداربسته لامپی V380؛ یک دوربین هوشمند در ظاهر یک لامپ معمولی!
✅
نصب آسان بدون نیاز به سیم‌کشی پیچیده
✅
اتصال به وای‌فای و مشاهده تصاویر با موبایل
✅
مناسب منزل، مغازه، دفتر کار و پارکینگ
✅
دید بهتر برای کنترل محیط در هر زمان
✅
طراحی لامپی و کم‌جا، بدون اشغال فضای اضافی
🏠
با این دوربین، هر لحظه از محیط اطرافت باخبر باش!
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۱,۷۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
همین حالا سفارش بده و امنیت محیطت رو بیشتر کن.
http://memarket24.ir/briefcart/180124/g-en50734</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/672047" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672046">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
♦️
سپاه: سکو و موشک‌های هی‌مارس در کویت و محل استقرار نیروهای آمریکایی و ضدانقلاب درهم‌کوبیده شدند
🔹
در تداوم عملیات مقابله به مثل و پاسخ به جنایات جنگی شب گذشته، رزمندگان غیور نیروی زمینی سپاه در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یامهدی ادرکنی" علاوه بر انهدام سکو و موشک‌های هی‌مارس در کویت، طی یک عملیات ضربتی پهپادی و موشکی چندین محل استقرار نیروهای آمریکایی و ضدانقلاب مزدور آمریکا و اسرائیل را درهم کوبیدند و تعداد زیادی از ضد انقلابیون و نیروهای ویژه آمریکایی را به درک واصل کردند. عملیات مقابله به مثل ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/672046" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
