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
<img src="https://cdn4.telesco.pe/file/R-Gx3Mz_-1VjddNgHpdHQYlLi50S90lyzFtJoT9VcsHiidNeojEi7Kja1faHJacZt63hd-dLI-JnWxoG2Q9lTETruhOCxHMEKzyF7WpPHgpU9gQNbSy2FcxtsaYvRRc2xFyojbHkHZLZvJ25l92iYaPrVoBD981nMoYXhtDPmOLXkDX1DzZrbNV9iiK9sosTd5rv2VMSSOk1hkwOhvQdhRg_qE1qQBtKaLXmV0UKeWUeCqrNnVz348Nge5nco1Ait1EdAR4a_LtYvJ5mFyufSUfl8V5iwUIpSgE_BpKAtG3bHyV7Le6IggbrTHNLlKFBVB1XUdr3GBUBp86EMUhAfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 927K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-131045">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه قطر:
ایرانی ها از دیدار با تیم آمریکایی منصرف شدند. ویتکوف و کوشنر در دوحه حضور دارند اما با مقامات ایرانی دیدار نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/131045" target="_blank">📅 13:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131044">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7204ae52a8.mp4?token=o18pCHj8Y2_YbD667Uy1eKdtefxhU9RrqP8-TlQRi2wWo1jX2tM2TuuT3_Ls0g5l8z8U5H4M6RmAo9CcB4Hjwrg94hY5NA33YcpgF8Owo7jXEQmukyvms-RyRhxsmLuSvhG2GmW07itWUNWHSkQRxQVteCwSfw5lzCR0f95K7F62LtQKuxuEyHe_PDvX3X9oaQnAkBBsfZfaoBLzjw3mXXUSCZ99g24xBdW7pqcKwFK2gHKogmzT8OokXh_MMfAVKp0bEKBusswrILwN40lprRPbKBUsqE4NvhOvy8wVBCYyjOemXcg1DxgqWtaXd1SXkZJeIkOujk1lXriv1bS_BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7204ae52a8.mp4?token=o18pCHj8Y2_YbD667Uy1eKdtefxhU9RrqP8-TlQRi2wWo1jX2tM2TuuT3_Ls0g5l8z8U5H4M6RmAo9CcB4Hjwrg94hY5NA33YcpgF8Owo7jXEQmukyvms-RyRhxsmLuSvhG2GmW07itWUNWHSkQRxQVteCwSfw5lzCR0f95K7F62LtQKuxuEyHe_PDvX3X9oaQnAkBBsfZfaoBLzjw3mXXUSCZ99g24xBdW7pqcKwFK2gHKogmzT8OokXh_MMfAVKp0bEKBusswrILwN40lprRPbKBUsqE4NvhOvy8wVBCYyjOemXcg1DxgqWtaXd1SXkZJeIkOujk1lXriv1bS_BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزدی : توافق ایران با ترامپ و کنگره آمریکا نیست توافق با نتانیاهو هست
🔴
باید ببینیم نتانیاهو متن رو می‌پذیره یا نه چون تصمیم‌گیری نهایی با اونه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/131044" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131043">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66c8103ea.mp4?token=foMqiNxqRiu9AYhDFZ3xHcYNeWQyMobUDOXL9xDBG5SA1j2gMfXEq-ABk91SuDZeiO--1CvbDGDaMuGvNl4m5qvl6Yvym6dO8M-b1EanRLY6ByxItSrTBuj432KiEb6QcsnqTujvtdkd1QVepkwSNX-7lAL_HdBbtAXRQIWwFOniOasAi6Alhb_GEFgSHoNrkPqBPQUz4gqmIQFgCXOQcy33JowZFFzKP4EScV6ZKLHC8EUQ4my8u6AHZ4kb-28I9mIMQMDX3xcexVH_i3KpEj3NsVyw2hH7uM5rj1N-1TJ4pjPj5zgSmpEF0FN_rce9Pv4nT7LKHUd1TFOklXo-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66c8103ea.mp4?token=foMqiNxqRiu9AYhDFZ3xHcYNeWQyMobUDOXL9xDBG5SA1j2gMfXEq-ABk91SuDZeiO--1CvbDGDaMuGvNl4m5qvl6Yvym6dO8M-b1EanRLY6ByxItSrTBuj432KiEb6QcsnqTujvtdkd1QVepkwSNX-7lAL_HdBbtAXRQIWwFOniOasAi6Alhb_GEFgSHoNrkPqBPQUz4gqmIQFgCXOQcy33JowZFFzKP4EScV6ZKLHC8EUQ4my8u6AHZ4kb-28I9mIMQMDX3xcexVH_i3KpEj3NsVyw2hH7uM5rj1N-1TJ4pjPj5zgSmpEF0FN_rce9Pv4nT7LKHUd1TFOklXo-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزدی : جای تعجبه که عراقچی می‌گه گرفتن عوارض از کشتی‌ها در تنگه هرمز خلاف قانونه؛
🔴
سؤال اینه، کدوم قانون؟
🔴
اگه حتی رئیس خلیج فارس هم باشیم ولی نتونیم از این موقعیت استفاده کنیم، این اسم و عنوان چه فایده‌ای داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/131043" target="_blank">📅 13:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131042">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055600096f.mp4?token=cYkmVXhSUwvR_X9aSwtWyx3ZaT8QayUBep-fhh3blTpGmkwHwPLMXxuZ2PWfBH1PpCopxq28CRyVVFkLcpYBrtB_1x6_6WnsSd4_VF3vpIQ737PpD7uhKXpsSre_iUHXlWIYwGDRTkD8qU8sQcEHbki1Vu7YFVjSmBQQ1BW4FZTLej6fz_SG6iIgLagKvdg7_VReoYRXYWJCIf7pvPutTXkXu980KTULK5SY9Xm60cf7QvmmRuY-_lVokqEDuxyl-6fxd6zipM7IaJ0EY3si2hjZkQ9_P5_Pb0jQaV1qImKftkrR5OxV4aV_krlltIvtPYszlq-gRLliQ-11Fv4D-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055600096f.mp4?token=cYkmVXhSUwvR_X9aSwtWyx3ZaT8QayUBep-fhh3blTpGmkwHwPLMXxuZ2PWfBH1PpCopxq28CRyVVFkLcpYBrtB_1x6_6WnsSd4_VF3vpIQ737PpD7uhKXpsSre_iUHXlWIYwGDRTkD8qU8sQcEHbki1Vu7YFVjSmBQQ1BW4FZTLej6fz_SG6iIgLagKvdg7_VReoYRXYWJCIf7pvPutTXkXu980KTULK5SY9Xm60cf7QvmmRuY-_lVokqEDuxyl-6fxd6zipM7IaJ0EY3si2hjZkQ9_P5_Pb0jQaV1qImKftkrR5OxV4aV_krlltIvtPYszlq-gRLliQ-11Fv4D-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی، کارشناس مسائل آمریکا : ما
هی از آمریکا می‌خوایم تحریم‌ها رو برداره
🔴
در حالی که تصمیم اصلی برای برداشتن تحریم‌ها فقط دست ترامپ نیست؛
🔴
بخش زیادی ازش دست کنگره آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/alonews/131042" target="_blank">📅 13:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131041">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcftG55ukVmjaF3NWvDDES0ZxqrwN2TZ3eLx_SFPe12uM6AcwdWqUlmb0Wbv7R88boWFiyoP6ZUj9yht71DD3aub_4fwgEp_ZZ8viQ8u-l9iXFB_7VruM0haClEHNWADuVJCf7TaffLrin0_l94uhfJZM1nuaS5eRNPyRh0709Lf9ze9M_MWj1mRXZJNpm6-AF8lqQaKJt0AvTklU_C2Cip82Hvv2pbThqNzVQ4O_qRYrog7xVn96wGIbegalIWXj_bHQLUnO3aiJFZUmMWx5n25NRtxiD4lXk-RnqMprCjabxh-WcFFnuBFQyTIgU0-C3XlA6fnKIjTr_Q0IZIxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/131041" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131040">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
پزشکیان: اگر آمریکا به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/131040" target="_blank">📅 13:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131039">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیویورک تایمز :  بیشتر سربازان تازه‌نفس روسیه در خطوط مقدم اوکراین تنها ۲۰ دقیقه عمر مفید دارند !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/131039" target="_blank">📅 13:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزارت دفاع روسیه گزارش داد، شهرک‌های لسنویه و رونویه در منطقه زاپروژیا و شهرک مالینوفکا در دونتسک  توسط نیروهای مسلح روسیه آزاد شده است.
🔴
این وزارتخانه همچنین از انهدام هفت بمب هوایی هدایت شونده و ۸۰۶ پهپاد اوکراین طی شبانه روز گذشته خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/131038" target="_blank">📅 13:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: چرا اعراب پس از جنگ اخیر دنبال رابطه با تهران هستند؟
🔴
پای یک چارچوب امنیتی جدید منطقه‌ای در میان است
🔴
کشورهای خلیج‌فارس در حال فاصله گرفتن از اسرائیل هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/131037" target="_blank">📅 13:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131036">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-qaRUKsSftEzcmncNEEA1MZPRDx0PcBAORIcpFKde9fE0B9XKJvr__DXejZyCGM2PTZXx0xxE4zeZM-FHOPeLY7o4XCiMOttgfI1c10ykTBxDhR1ESLpSeWa-xXY2b_eLX1jeTIH6fm6-GPaeDY3YE6JU-Ik-hsuWEH_yTGuiMHfPndYnP6lBkSvhl42_oBPxttqiP_4JSRwyUI4cKWm_O_nkKgU7TplU27wel0-OIUsBYkYw2e-PCtWtXpXM7FaWPa2hDxrX-ytiaZFam8H81_UUJag5_vXU3FeKWsYwrIN0KG607H6bp9QJi5Hy1WX9JtqH_hPCz5rwh0t12QAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون اجرایی رئیس‌جمهور: جلیلی به امضای تفاهم‌نامه میان ایران و آمریکا رای مثبت داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131036" target="_blank">📅 12:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131035">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2xJJpu7SVLf5HVJcxeGEGjPPsuKLvN2yXJ2QgwVFn24iiDiWkla0zJ4d6OY_57ekaABI1EKMgu-uJJz7AQoMBQUuysjtZX98j084W5sSIr2BVflXYZOlCy_CP2nQhCE2RO7EgEt4fT6-aMpXIbMnv-6FKsC9rmmm6yW8YFc8KaieK-zMY7j_ikIK5tyJSnMVibc1h0I2qNqqlQ3jxVrM6LIkJ45MLgD6P8uvoSqeDc3rWPGAkDOthMUkQiMTrCaJdkE8LjDn1yOWevdIADCM_axja6V9c8vz0xXJ5-ie4QScALqwwO5Ym2paAW83jYMtnmot9o0VFvu0G23WzzvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخزن ۳۰ میلیون بشکه‌ای هند و امارات برای دور زدن تنگه هرمز
🔴
بلومبرگ: هند در پی اختلال‌های ناشی از جنگ و انسداد تنگه هرمز، با امارات برای ذخیره‌سازی تا ۳۰ میلیون بشکه نفت در ذخایر راهبردی به توافق رسیده و قصد دارد برای نخستین‌بار ظرفیت ذخیره‌سازی گاز طبیعی و LPG را نیز توسعه دهد.
🔴
حدود ۴۰ درصد نفت خام وارداتی هند از تنگه هرمز عبور می‌کند و این کشور تقریبا ۸۵ درصد نیاز نفتی خود را از طریق واردات تامین می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131035" target="_blank">📅 12:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131034">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myw3A2exYJUKEXRDzWTph3D522Czy3Ha_kxkeiEpFqMeuSrxNh2-jnQd_n6TDWaZDGCyorDN1_LT_j6qq6zMuAy8hqT2ZyjaeJcjuLdUsmbVJ1jbqbGM2M-4JswCKnZTaV0uusdkL1l96hk5-6ntZa4l0HjFOYAUY5YXAnfmDt0iFCSujVXsxTb33YsAxxEKP6dr2CtbeNXQMft182ywTEr8TeWF4ssFN4-bRu3ESDKiFlpKRD-ndyp4CW1vxAd2pRAh9fNhO7pfMMiOC2DbDcR4oFUZq5NulSntCc-QNuVZMX_8kGlV5zjdeDpvyV9Gn97kKCyzAbsaOcTvTJ4Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۶۸ هزار واحدی به ۵ میلیون و ۱۲۸ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131034" target="_blank">📅 12:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131033">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فارس: بیش از ۳۰ کشور برای حضور در مراسم تشییع رهبر اعلام آمادگی کردن و نمایندگان و بزرگان ادیان از ۹۰ کشور به تهران میان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/131033" target="_blank">📅 12:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C3PKACC8v12FS-cDZE5kLhLMGqpAC7_6BguVMGbcZEjfmvjGivWj7Z-BX_TQa-p0yT7tlry-wrMyfn6iG4ORw7i-0wu0fnsRUwICQrRpfqS4bJhgSFv58jj2IfauDhQ0h2Kui6oR5AyFQu_VmQwINCGT9x5eZkA2dvSOcOCvkhhUszn54yKiGkRxMrt_eD4jdnBtLvBx92AbjD6QaMovoXrj8Tk9AI7tRN0lAPtjxNuLfdoG4S_tK8wt7PMkW4iOFmd9UBoTiNgOz91U1OzbbI6rrUjO9K6POyWB-UpWqBcmFlkyWXfUIrLDh_HvisrJvm2y1ZFJXp9pkW1kE-M0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NrnHU_8CZ0V6YzrU2RwOaeqjea-C2TiIQ0uqgZCNeunBmcbCx2pMiULWQY7AzFr-NFZMSkoMn_ixAliI8qTn6PHND_hvQiTIGfYQBniJdE_U4Ung-hkhefVP8PJvzqc_HziNT1Qfnd49nCsirDOXQP67DGXWfiSCYYeuHQU9oQbCk_NbKAl6juqezTOCg6XblrfZSAkO30qZYaAwE4ZLNdKLvSp_n5D43-rZWfnz6GE98cWj9EUvnKFA3Lc0Kg9N0CnLMdiPFj4Ynt6uX2TS2vngWRtCslSIz0N8y0rl8imTvuZhsyKsrLW28NW4hdXJuKxdnyanB_JS69OcYo9Eww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی آمریکا به یک پست مرزی ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131031" target="_blank">📅 12:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131030">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
اژه ای: در حملات موشکی به زندان اوین، افراد زیادی می‌توانستند فرار کنند اما فرار نکردند؛ بعضی هم رفتند اما خودشان برگشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131030" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131029">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
منابع خبری از پرواز گسترده پهپادهای اسرائیلی بر فراز بیروت، و ضاحیه خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131029" target="_blank">📅 12:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131028">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=V5dKa52lJfQdqtZPi0zIF5MvadSlGqIqq-26GdTknLENCTBzEO_tNjuYJ0kn-lHAGloXkxzrBS_wmUXB68mpKTbObVRkF0mapX6w-Z5Cu8k-5YcEaLHK4fsOBeCGJPUEczrZRWwz68KxBIaiDI03BlCyBx4Nbv0uSnTCzSnGxtjnSIMDgBk5mLaFoN_j3FqEhwTwO_A9-bxKkAMj96CL4V0ratZJcKgjIhpvQfLI1o-xNEfeLZzfzaQsqknyLtS7141egFV-wA4YDggZOrLlp_Uk6KsgDp6FmrjKz0sQXjixI3qANr28DGKTHbtjg-ndfAYAnFrvkyl76NZ-GrR7uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=V5dKa52lJfQdqtZPi0zIF5MvadSlGqIqq-26GdTknLENCTBzEO_tNjuYJ0kn-lHAGloXkxzrBS_wmUXB68mpKTbObVRkF0mapX6w-Z5Cu8k-5YcEaLHK4fsOBeCGJPUEczrZRWwz68KxBIaiDI03BlCyBx4Nbv0uSnTCzSnGxtjnSIMDgBk5mLaFoN_j3FqEhwTwO_A9-bxKkAMj96CL4V0ratZJcKgjIhpvQfLI1o-xNEfeLZzfzaQsqknyLtS7141egFV-wA4YDggZOrLlp_Uk6KsgDp6FmrjKz0sQXjixI3qANr28DGKTHbtjg-ndfAYAnFrvkyl76NZ-GrR7uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو:تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود، اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛ متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131028" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131027">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6dgvKhqjSNaILz3u7JFbcVgIPyYAUyr1ELvZZgP6p-K4jZ4D6J7Wi861bcMtZUIgNHidsGyEqnyWeVsY2FdgfUzP01cC7fa8Y3mP7rpWcxBt0wsXDtTWOGMDTnt4r3NUnlLypNKJJfQ6Iy-ZrBZkHySmtzuXVQpZc7gAhNDobKHiSo8sr09TyweXDIbYkZYrMsSTgColv5_XGViJs--PbCyJo3IYugwEkgljgUGI3bzeG0lM6m5l2y10ou5W6iga6gamjNluKxSUXx7BgXGPuWMNW4w3VPm82a4mMizCabdL5CXMWXIAvJDa3yCkVheH-FPV0zzkcSr9s6DrmJhrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه نیویورک تایمز گزارش داد، مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است
🔴
مولین روز دوشنبه در نشست خبری مربوط به جام جهانی گفت: خوشحالم که کارشان تمام شد و برنمی‌گردند. وقتی ویزاهایشان را گرفتیم و گفتیم باید خاک آمریکا را ترک کنند، خیلی خوشحال شدم و ممکن است رقص شادی کرده باشم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/131027" target="_blank">📅 12:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131026">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
میخائیل اولیانوف و رافائل گروسی درباره چشم‌انداز حل مناقشه بین آمریکا و ایران و نقش آژانس در این فرآیند گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131026" target="_blank">📅 12:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131025">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
یک هواپیمای دولتی آمریکا از میامی به مقصد قطر در حال پرواز است و احتمالا فرستاده ویژه ترامپ، استیو ویتکاف را برای انجام گفت‌وگوهایی با ایران حمل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131025" target="_blank">📅 12:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131024">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بلومبرگ به نقل از داده‌های شرکت کپلر: حدود ۲۴ کشتی باری، از جمله کشتی‌های حمل نفت و گاز، روز دوشنبه از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/131024" target="_blank">📅 12:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131023">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUFUloqTw7zAAryoETCzjiL79tm-0oYM56xPD_b3PAj-GDJDWvySKp4Vc1pNET2wzGQZoBG-4uTmf-XL5_artkB82AGGKJ3GKyeXy-VFKWyR02ioZTduVkm4USbY6wDIIn_XhcbIaoNwk6oQ4U07vOdAggy5fNpbm0npI2fYx19yuKfarv017556sW4cqWkoPznj8UQHBAR_AJ2wvAtpuOHH8OJftJrPrkWfYFhaXy4X9JxrokA2ISBgtdDfom_g0Ru1HdrBw9ThznpLD1cC1nv0e63yCVDyizfK5pese0OIUhQ8tTtWN9_uQeP9tCz7QywiVVT-zkcoLPiM42Tp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما: فرزاد جمشیدی درگذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131023" target="_blank">📅 11:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0uAC4-F5Z6xydXrq0xzHTspQX8jT0PjIp0ujAB9YjcyI8f7IjBDSemykHPLXaOyKaKQb-0O1g3gHNhysQVfy_eTXzR-3PbOdJfc0SJxFGUsD0xAiB2YUW9QaDYDtUGUfIMkl8GqdYHT9GjBtiQYcjgJxOTEnJrF4wDWE-4QLmal3bVCkZuNCRvC8QxTHQS1J6-v7MEx3Du5jl1RYHoGnyLl5vRpXsQDRGriK1xu0DMKfjJittJ4upW8JEdyCmkXIzRmEZR3QWJijyD6h1zMIF8QKxzK6GEazdd7pPQZdNvEeRe3tmDmvgeA7oCKTxj98XRfjfBUTbnRda332ciMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LkEvG18YidNMSQ7nY41sjYibs3zl855bBWXw-qHdvMhXrlycoriFBBTa8i2PsvxZkIIzCsNaZ9gLW_uMWngaKran--KIpVgIVUkrEZqR4IMff-211kgqSWO2G3VXp-htdHZjJNXfN4Wsl69eKgGXQhAkHVGggCI6wMJdE5v-cc9_3rL8Fut_qGjggqJJbTPUw6c3W9ZgZ40v3DnqkGuUiKPI0mRFBc_6TXFOQaTTOZ3-2YjAXo5trnjvJTsCrN_Gfd288TRtVR9kR0b3SJisVgul5behQboWzqcwt2NhUWY7NVC0aqCNLt7txQkeyE_4kPCnDvqgvb6w38DazYKJhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش‌سوزی در پالایشگاه شرکت هالدیا در ایالت بنگال غربی هند به دلایل نامعلوم، ده‌ها زخمی به‌جا گذاشت و حال برخی از مجروحان وخیم است.
🔴
شرکت پتروشیمی هالدیا یک واحد اتیلن با ظرفیت ۷۰۰ هزار تن در سال را در ایالت بنگال غربی هند اداره می‌کند که بخش عمدهٔ سهام شرکت متعلق به شرکت خصوصی در آمریکا به نام «گروه چاترجی» (TCG) است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131021" target="_blank">📅 11:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
واتس‌اپ به‌زودی قابلیتی جدید ارائه می‌کند که کاربران را از اشتراک‌گذاری شماره تلفن برای آغاز گفت‌وگو بی‌نیاز می‌سازد.
🔴
بر اساس این قابلیت، کاربران از همین هفته می‌توانند یک نام کاربری منحصربه‌فرد برای خود رزرو کنند تا پس از عرضه رسمی این ویژگی در ادامه سال، از طریق آن و بدون تبادل شماره تلفن با دیگران پیام‌رسانی کنند.
🔴
این قابلیت که از سوی شرکت متا، مالک واتس‌اپ، ارائه می‌شود، با هدف افزایش حریم خصوصی کاربران طراحی شده و یکی از مهم‌ترین تغییرات این پیام‌رسان در سال‌های اخیر به شمار می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131020" target="_blank">📅 11:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131019">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کاتز، وزیر جنگ اسرائیل: من به ارتش اسرائیل دستور دادم تا خود را برای عملیات «آبی و سفید» در ایران آماده کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131019" target="_blank">📅 11:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131018">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وال استریت ژورنال: وزیر امور خارجه آمریکا، مارکو روبیو، موفق شد ترامپ را به دیدگاه خود قانع کند که اسرائیل باید در لبنان بماند و به ایران حمله کند.
🔴
معاون رئیس‌جمهور، جی دی ونس، مجبور شد عقب‌نشینی کند و او نیز حمایت خود را از توافق اسرائیل و نه آمریکا اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131018" target="_blank">📅 11:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131017">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر امور خارجه عمان اعلام کرد که ما طرفدار اعمال عوارض ترانزیت در تنگه هرمز نیستیم، این امر طبق قوانین بین‌المللی ممنوع است و ما به آن قوانین متعهد هستیم
🔴
این مسئولیت ایران است که مطمئن شود خطوط کشتیرانی عاری از هرگونه خطر مرتبط با مین هستند.
🔴
وزیر امور خارجه عمان با این حال، اخذ هزینه خدمات را به بهانه افزایش ایمنی ناوبری، آمادگی برای حوادث اضطراری و مبارزه با آلودگی رد نکرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131017" target="_blank">📅 11:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131016">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
الحدث: در آخرین تحولات مربوط به مذاکرات تهران و واشنگتن، قرار است تیم‌های مذاکره‌کننده ایران و آمریکا روز سه‌شنبه وارد دوحه شوند، هرچند تهران تعیین تاریخ برای دیدار دو طرف را تکذیب کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131016" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131015">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZufYMnkQytEIZkQm2IgrrbhKDQvSx8BPSFuQP467B2S2ATY8VhbDzAz6uY3EHI-odcY5THmlE7_P7MN16nA_Dl5MvOAdiFUxvWCb-QNt5gGRLyqsSU_p5bt9Azpmmc_YYNyUCTsko0AHGcWw0dkr34kncROnehMQtxgPfP3o4pGH73PvTau12ZaAhZ4H1at2Wlthtq4_aVy2f7E7iUqJoSrUrtliLbAAcZMlW-Vb4QNyXRIKOWo8AZPk2JL1ot_N_wGQRlZnNb592o-OexQ19t4HnkfVqRxaVjBbVwV4dBzb5VcyU8uu09SBuYGMrnAN4a3knAwzDw11-48f1QfZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دخانیات صدرنشین مجموع تورم ماهانه ۱۴۰۴ و بهار ۱۴۰۵
🔴
تورم ماهانه گروه دخانیات در فروردین، اردیبهشت و خرداد سال جاری به ترتیب ۳۰.۷، ۱۷ و ۳.۷ درصد بوده که در مجموع به۵۱.۴ درصد رسیده و این گروه را در صدر جدول تورم سه‌ماهه قرار داده است.
🔴
نکته قابل توجه آن است که الگوی تورمی سال جاری، مشابه روند سال گذشته است. بر اساس همین آمار، مجموع تورم ماهانه گروه دخانیات در سال ۱۴۰۴ نیز با رقم ۷۲.۶درصد، بالاترین میزان افزایش قیمت را در میان تمامی گروه‌های اصلی به ثبت رسانده بود و این گروه برای دومین سال متوالی در صدر جدول تورم ماهانه قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131015" target="_blank">📅 11:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIRdE-qSHKKTONDHDitqqebaRI8KuoZCeNDxW28zV4XF40KBS-PanfQqh0zWNIv77dDfW5rxXMb53dLIuH7b9jjao3yOisMLG8noZc1Kf8c9VITbvFZJOWp-ImhaX0LKoU8QHUen6AE9is5ByzD9_E5j5zQ_g8JqxVzONWwz_0xZX0pZX9dKFvi5rkdtSwngskafxs0PvnEB4XZY9jy0RfGVYwO8D6qbWnA3b2hWZjjhpb9jTUsL5y1T42F-WYg46-sJUKrJbrEPPcruoQAaf_m768PZYfxYRc2N1_jFYqXVI2z-AO7tmFgalaraieO0YeLyfXI4MDt2mCb1kqx2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۷ سپتامبر ۱۹۴۴ عملیات مارکت گاردن و فرود چتربازهای بریتانیایی و امریکایی در هلند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131014" target="_blank">📅 11:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6bsbwul_LbmCrqDlxEtMIS0a4HzavQKaysBP_uinH_UIEe7EzIHSO3jTyw-nWSVtx3R7iGEFjLYCdPK_pv56SUIXfufDih3ZSZijUVb3e7pxA2LLzsACygUCMndKgzz7oV9xU-WWgZkwfRRSBXaEBrc_OVKMh-FAgLuFW0L5HN-Xnq8DnDiKg80bcch_geqQjiqZtPLlQCJ1I-7jFZWpwvPkx4fWe9WMH9Lr_Mg2q5TcReWYnM-eGjdu6Tt8xZPlJcK8wQia8Fo4FXg75ADdFVnkqSHByRvzS7o9tEkGjSxFWjQRxM6g1aSPWjwXs92ONkJT6ygT9bXHEOQjTRDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ونزوئلا: شمار قربانیان دو زمین‌لرزه به ۱۷۱۹ کشته و ۵۰۳۴ مصدوم افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131013" target="_blank">📅 11:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یک شرکت ارائه دهنده خدمات رهگیری کشتی‌ها : با وجود نگرانی‌های امنیتی، رفت و آمد شناور‌ها در تنگه هرمز در طول آخر هفته ادامه داشته
🔴
طی سه روز، ۱۰۸ عبور ثبت شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131012" target="_blank">📅 10:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
الجزیره: ایران اعتراض‌ها و نگرانی‌های زیادی درباره کندی روند اجرای تفاهم‌نامه دارد
🔴
در مورد اجرای ماده پنجم توافق هم سوء برداشت وجود دارد؛ ایران می‌گوید می‌تواند تا زمان دستیابی به توافق نهایی، تردد در تنگه هرمز را مدیریت کند، اما آمریکا بر این باور است که ترددها باید بدون محدودیت ادامه یابد
🔴
همچنین تهران نگرانی‌های فراوانی درباره ایجاد مسیر‌های جدید دریانوردی در نزدیکی بخش عمانی تنگه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131011" target="_blank">📅 10:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131009">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GeMdx3GFAj4FKbKMt2yH_iuGgNlYo_TotDaC1Aaa0ZOrdyA7UCH3NAMq2uZwS2ytF26EjNY5UmuodNnr4-XkDHMqPjJLYDoGeBZCKQCVnzZ1YsprufL7Gt7Wm8oxa_atXTKmL3VkhdpJ48P8hVGPuHnFik7IvAgRc_4y8IpKfEsIva8pfZRjsbaf3vOfeHdUFfmcthcZjPG80jRrr7H_BjR1m0nq-l1-XCGMfA9SWA8RqIsAGv4n6dGJZnpzpYzcrmbQXcA6mpm8FbrxtB6hT1qLO-9TAP6oeVD5tqQCatQav_18awWzyNweqaQnkUGxyPRWXQfUyxCFjzz-ufKpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qwvrdy1zXxdCx2vbbkV83IrGn_QvcV3zAw_uXsmXI45TO4jB32UlMX45np_aMnQILOvIY8DcJTwALJgXKMAj7aZhOxpk7sgEy_6vInLZdSYfHzFJrTFYFm9MHyHS1eRgsgQRAoY136XCAKWFw4BxRqml2aat4kLogi62XqOobdRELRCyF1gqIvAulALsnozSNZasdsPsE8dccISYS3lZUbo9dFYm66qDypfOvZDo7z17q8G2GxOGWiRoaZq5o_21c4RkcqsQ-IAVeoICvY-pe_Jl1GG5B2LSGCmxqpYKE_ByeOkEHO0N5_fT77RntA9Tmb9g6YOovYcbyCRCclGt-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک نفتکش صبح امروز در کریدور آمریکا مشاهده شد
🔴
پوشش سنگین هوایی به‌صورت ۲۴ ساعته و بدون وقفه فعال است؛عملیاتی بسیار پرهزینه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131009" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131008">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
دبیرکل ناتو: چهار تا پنج هزار سورتی پرواز از پایگاه‌های اروپایی در چارچوب عملیات علیه ایران انجام شد
🔴
آمریکا بدون اروپا به‌عنوان سکوی بزرگ قدرت‌افکنی قادر به اجرای این عملیات نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131008" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131007">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سرپرست وزارت دفاع: به دشمن اعتماد نداریم؛ دستان ما روی ماشه است
🔴
در صورت نقض مفاد آتش‌بس، اقدام و واکنش متناسب و لازم را خواهیم داشت
🔴
امنیت، مقوله‌ای درون‌زا است؛ کشورهای منطقه باید خود درباره امنیت منطقه تصمیم بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131007" target="_blank">📅 10:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131006">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سپاه: انهدام مهمات عمل نکرده در محدوده سرخون و ایسین بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131006" target="_blank">📅 10:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131005">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پزشکیان: توافق اخیر در هماهنگی کامل با رهبر و حمایت شعام به‌دست آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131005" target="_blank">📅 10:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131004">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی اورژانس آذربایجان‌شرقی:
حادثه واژگونی یک دستگاه اتوبوس ساعت ۶:۵۰ صبح امروز سه‌شنبه در ورودی چهرگان شهرستان شبستر به مرکز فرماندهی عملیات اورژانس استان گزارش شد.
🔴
عملیات امدادرسانی به حادثه‌دیدگان آغاز شده و بر اساس اطلاعات اولیه ۱۵ مصدوم تحت اقدامات فوریت‌های پزشکی قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131004" target="_blank">📅 10:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131003">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ8mAY4pU7g3oMyihAPc_HB9VPCN1P-JhXk5jbM8R3TaxPagW3MjYBGD2fWLjrnVH5oyzknDl49MoXIbvVlgDO3HZTZSBUPRXiP-Z7UxR8occWClUKE9subMxDmGM5lEI-TvuXon-Kewxw3e8aY533anIkFN6YQe7lSOWoLmgq_BYzMrBOtabfKFN8wWkfkm04RnY1FSrbSbijdLy2Q0ebX0K2NwOFdiKI1sE_tFd01hQYMxWHAx2Jg4YpGCf5xEZeWyjoeKucSj2yJ_6FoVrMvxvixhROCLQghVIRQpf37ys3CYO47faCjEPO3T32X4xOvtdBCioEt8MTmZQ4wkeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: هدیه‌ای طلایی به کاخ سفید به مناسبت دویست و پنجاهمین سالگرد تولدش
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131003" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131002">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت خارجه آلمان: توافق آمریکا و ایران برای ازسرگیری مذاکرات، گامی مهم برای دیپلماسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131002" target="_blank">📅 09:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131001">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
روزنامه جمهوری اسلامی: در جامعه سالم، مداحان نسخه دیپلماسی نمی‌پیچند / دیپلماسی با شعار اداره نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131001" target="_blank">📅 09:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131000">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
پولیتیکو به نقل از منابع: روبیو و ویتکوف به قانون‌گذاران تأکید کردند که ایران تاکنون هیچ مبلغی را بر اساس یادداشت تفاهم دریافت نکرده است
🔴
ویتکوف به قانون‌گذاران گفت که تیم فنی مسئول مذاکرات هسته‌ای، سوئیس را به مقصد قطر ترک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131000" target="_blank">📅 09:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130999">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دونالد ترامپ از خرده‌فروشان سوخت خواست که قیمت‌ها را «فوراً» کاهش دهند، با این ادعا که قیمت‌ها نسبت به قیمت نفت که در حال کاهش است، بیش از حد بالا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130999" target="_blank">📅 09:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130998">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ادارات شهرستان کرمان تعطیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130998" target="_blank">📅 09:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130997">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbc09fa73.mp4?token=hNKQ6V-tdtKqp3YaEm6rookbYyuvJa4E6Fi8jq8Ifd8IosCn76MVo5CeD5pc0uD_QMSbKB7yl3de9sRlittE2_v_o07cP4VwL992TiNK0t9nUXpTeJATALl5MsBQTRQwM9jwZgRfTyQ2eN6W9Tne8FwDuqV542lKL9F7G1r-1rjAoPSuFrlpzWDtQhDC5QhShIZhwWgEMkbFx0rHSs7ViScly34DFk_IT75cCle3TPZraZg9A5xWKS1krX1m0EkDsRiwFwIr7h5jj5NlbkoPds-n2QGwyLezsM6lYgD712mPwaIdjbNaBECSV6njoJY6TTlIrA8aDpxLD5Xw2xQb9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbc09fa73.mp4?token=hNKQ6V-tdtKqp3YaEm6rookbYyuvJa4E6Fi8jq8Ifd8IosCn76MVo5CeD5pc0uD_QMSbKB7yl3de9sRlittE2_v_o07cP4VwL992TiNK0t9nUXpTeJATALl5MsBQTRQwM9jwZgRfTyQ2eN6W9Tne8FwDuqV542lKL9F7G1r-1rjAoPSuFrlpzWDtQhDC5QhShIZhwWgEMkbFx0rHSs7ViScly34DFk_IT75cCle3TPZraZg9A5xWKS1krX1m0EkDsRiwFwIr7h5jj5NlbkoPds-n2QGwyLezsM6lYgD712mPwaIdjbNaBECSV6njoJY6TTlIrA8aDpxLD5Xw2xQb9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در اردبیل جلوی پلیس اینجوری به یک نفر حمله کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130997" target="_blank">📅 09:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130996">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnq3t7n30hxDOE288c4g1SQnM7JJbeKfgmUULMsl_nsVwyoH1bhFCxQOSuVX7_5wmyaf6xFCwIt10tG7MxaoQib7avYuqZNiiPMSZWdvD7LE5NPeDbHq5K2eHiSaEceecvyOdeXnkwyxqTi2XFFsCN1rzDkeFTtLtIv_u_VHROFhqxujZnXBtYtHi0I34bwIJsEnNj9uIvtK-qKTtgRdCWtucqvAfz-Tj8hlSM_Z0X3MsIKFSUWcSG4X70R3Km0o28l2yq3-z_6aTXpw4kb82cBeqGJlsgHJq8uapdKH8vvu-UsznzADpipGwaHkHH3AT1YrOrUohHAACD1w0kFpWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دریای خزر در حال کوچک‌شدن!
🔴
۲۴ هزار کیلومتر مربع آب کاسپین در سه دهه ناپدید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130996" target="_blank">📅 09:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130995">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDxy-eo6I25_XsaNtKY4qJ4l3rZwT3GEL7nj3CI7IXHTbJQnYQTodq3d6PZzp9aMo3_Fwy266m6jcEnk8PuywV3boSr-15uWrrztNZ6IfDaIF-x-Svx8XkbWs73-nj39BAsFSJOJWrBPrFLg1T355GxPgMwYITDTIO6ZGtEW17_JG9NJr2Zb8nn_WwFhzAMAyiF6NcHY82wWtasAZRjGvIhbMEG43pzgnyTilQUQ24YUaZ0eTnu7O9xPL5B3Acf2xo7I7Ddkf8b44-4oi4fLhUDJ-5NjXtJI43uwTjJPhHgJpPqdJ-RO1wuYRNuyKj8z9qZdkT9xEpx45l7d6Lz9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش مشاور رئیس مجلس به ادعایی که نبویان درباره کودتا مطرح کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130995" target="_blank">📅 09:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130994">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTqOXrWtNfQXI5JCi0OQt8sA6nHjAVqqEr6TiDdm6Bfa_6UZrtuEmKbduhz-scxd4CerrTlzrjqhlA3UXhajNCnhBeV0UlSfBWgUYfEWu517pvWmwzz6qruPjXk-4w_q9i7-3fTZaE8y_bx1qzYRww8ceQlD5eDwxww99HR_zjErVDFX30VEVCrufofBevBRI77HAmC1kCNpoFZoSJ3UybjurhY9XJGM7Y2QzBlEgSrA3rn8gSFZEhdhRLpy4WtML4yj0nk5RNH-1OYS7NyOPSRJsKBeae0DzUBaT-aVmdMPH8lhSEET6h16YfPzLr50Ow2h7YrMQ9_l-sBPk-tfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: ویتکاف راهی دوحه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/130994" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130993">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شبکه «ام‌اس ناو» به نقل از منابع مطلع: روبیو در جلسه توجیهی با اعضای کنگره آمریکا، گفت که دولت ترامپ هیچ توهمی ندارد که مذاکرات با ایران آسان خواهد بود.
🔴
روبیو به کنگره گفت که احتمال شکست مذاکرات وجود دارد، اما دولت می‌خواهد به مسیر دیپلماتیک فرصتی بدهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/130993" target="_blank">📅 08:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130992">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G46hkXXUV2N6KOTxWNc53w3JbSDTcahH4kVYYkErnutoEC-ySziOfv7R8Pk-lO7edArN8_Vcmal-ABQet1ai-vPHM46x0pngKJJBjAokMPxuPr6BL6no-1Hhw0WJm_cl-MJ2sYjFdSxrCENUO9a0hy_m2ndIC5-H59ILKjYFqIJtIUOYOpBfoCNt2vM5nuNyLZUn9RqpJFdDpUb8cDnAe1GfcTWa44w0B70k9zO8eLOEXkBpiIkOz419sFP9WxN_Lbo7DZWAXKbTbn8noicNH8d9qN5EGevH9M0V5rM1ybNXKeu-eas2xDpAc_rFXDXjJ6mHxdvc6fVxua9sB16G4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی 170میلیارد تومن از فدراسیون فوتبال حق الزحمه جام‌جهانی دریافت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/130992" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130991">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSCHJH1uCRwQe5m1YCSEZILqYYWWW5v0IRzFZehCk5D8579rAv_33Grr5c0szu_jinaX2D_O6oLJjLmNRh7MkdOw2NU0Vm7Gs-ARYw3yCBd2zjPsmOg39Cvz2Di238mfVdp2Yk-PRFhW1kBg5NPH8iyv-gBRSLFobBl8_6oidW_D5d1ok0lxW10MN8Msah_-kIKKIsDpKjhMzKJPCZBWD6-xaXqF5vGXKq9EfGvmmHkMtIzaTevAvvzNIeM14rysbZ3wHBP2Qa0bh-w8WMe0kvSxp8t1gdtu_e2OfomP8mqxxsXp_39JGjsGUpoX_L0Zm41-lGrcGhnEjxsbIhiU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: باید ترامپ را اعدام‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130991" target="_blank">📅 07:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130990">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSooraSkyvia@chToolsBot</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4RfI7CpdUrH7S9uS135CmwlQ4P1Sfs6QK7YD4Ro6TwWYmW_-dWkvUMyhRJIqKTVaVderZ4mGub4-GA6pNpyb20XU3dUuv4Uliv_tgnPDKXGAdHmSqVHOaQNrngv1CsbcazAetBBMSsjPdhup_Odz0iVkZoUQe2TOXgMtIe6wAcTxX6_OmTgldpa6EeLIP7y0ZvzQDlW5YiVql4B5RJO-r1De5X7g8E0vLgxOX7OuZAJ2NuSAataLAAPZ9m-pIsN5e0godvgcA0cFpigUiBKWQOjooR6Aoerj1quum8G5q6Pe4Zx_x2bV67AWo59e6Saxv4hs5dDmHKRCAf5jj9QOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه تحمل شنیدن حقیقت‌های تلخ رو نداری، اینو اصلاً تست نکن!
❌
همیشه به این چارت تولد و ستاره‌شناسی می‌خندیدم، تا اینکه خودم امتحان کردم و لال شدم...
😶
دقیقاً همون مشکل‌هایی که تو
کار
و
رابطه‌هام
داشتم رو مو به مو آورد جلو چشمم!
انگار یه نفر از بچگی داشته منو آنالیز می‌کرده و می‌دونسته کجای کارم می‌لنگه.
👀
اگه می‌خوای بفهمی:
✔️
کدهای پنهان شخصیتیت چیه
✔️
مسیر اصلی موفقیتت کجاست
⚠️
این آنالیزگر روانی رو از دست نده.
⬇️
فقط یه بار تستش کن تا بفهمی چی میگم
⬇️</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/130990" target="_blank">📅 01:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130989">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=rXwpycFR1JVUq37WKv3ipVY0rESnO6eO9a0BrBLtgpb8mPvyFF0lfdyXEkfr04FtdjJQz_I298V02ZEHQh4w_BsmPrpYKVLsIsyKtEghRq10EDgfGmLIVwLyoiyidmM8YN_9MTvJwOl6MNVIzemvhamPMmzoPDNBprFMgg5oQU3rasbDGP-yAu8hVMJM1kgIRGz7CRMts_r96teHfwzAFP_a0q8JXrI4xh8HWgbnIzSk45Y8n4KHxlMxFGy7jFY04bSJ-9FydxW3BJ-UGX0UO-9Vm-8LSIrQ9GNizP4ECmRjChf-BRd8UQg6a1bBYiTWt3L3qLK8Tbk80GRFWPQnvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=rXwpycFR1JVUq37WKv3ipVY0rESnO6eO9a0BrBLtgpb8mPvyFF0lfdyXEkfr04FtdjJQz_I298V02ZEHQh4w_BsmPrpYKVLsIsyKtEghRq10EDgfGmLIVwLyoiyidmM8YN_9MTvJwOl6MNVIzemvhamPMmzoPDNBprFMgg5oQU3rasbDGP-yAu8hVMJM1kgIRGz7CRMts_r96teHfwzAFP_a0q8JXrI4xh8HWgbnIzSk45Y8n4KHxlMxFGy7jFY04bSJ-9FydxW3BJ-UGX0UO-9Vm-8LSIrQ9GNizP4ECmRjChf-BRd8UQg6a1bBYiTWt3L3qLK8Tbk80GRFWPQnvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مداحک:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید
🔴
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/130989" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130988">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
شمار قربانیان دو زمین‌لرزه ونزوئلا به ۱۷۱۹ کشته و ۵۰۳۴ مصدوم افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/130988" target="_blank">📅 01:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130987">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndy6RAiOKaMhzGOVLPxEdNcylou2cvKplIyMavqt_dxf0GRUWbmK5s5mnXX6iiRug3C700reMXYBjaMWrCDQvnkxCpkoeIUAixZ5DvxthFVjplgHGZ4PATyYj7GoOFahTqzlaTTE9OCEUz9q-cQSIIMIiYuuGmpZbXV7tL3bVVRwHGAXVLj8uApJ2EjO9p3SibMNEZLU2xOnxDyxF912b-hbg4ZHqJiy5FAwQ_4FSyM4uz8JtABjpMsKXgfbhBF8-MS0TxzDlZmeFlXf6N1l7VmW-UWPC6essaUb0nV91QV8rOIW1mV94sEkUFIgie5pBHiL11iE02oQshSZoTGgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز(مِگامَن):امتحان نهایی هارو به تعویق بندازید تا بچها از امتحان الهی یعنی اربعین مردود نشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/130987" target="_blank">📅 01:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130986">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDHfTv2imygSrp40neFTPGJXRiisCxxEzIsgil1tSXijMzTxlGOI3eYCr88RheUoJgJK792wXlm4epNg7RarFlRuWPXnMyuVb13jch1YKzNd43mXHJITfsRxHySqTWsxaTglN_g87l_tPSHhpQThbz1Wj3Ta8kahKzq6pk3fLxtVKIJLNX4gRReEw2_o7QTzVj5AzdSbiWmIqADHgwYuK88uLqrzqZI8fQnZQrz_XQbjvuw1G8GzLiA09dnWNWi26sc_qs0QPhmJTnyT3P-zt7cJrYadcIZCup0m-bsBvDd7EpyXBCm5a14ATG4breOM3Ol1ZUSjy5gmrICfNW-W1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در شهر موناکو فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/130986" target="_blank">📅 00:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130985">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ48TBNqtPo3bEUja5fXnwhRjono4JJJmCi8XjtE4MpIiwdQr4CYoiUXKA_yTyBCj2_S_HHUEQALnT-vSBSHwTrqrQwZX73TQSXE04YY1TFR_iSwB-xH4ZHL0P38st2xkmu633CJ_Q5xJ2-y84de9BHIWOscOO7PtlT3Ft_YfQdGllwIYShFDz3wk7d_JiOxgqwUs4BTPc8ZAsI9pk82wsYz5CurYV8oVyX3lUxV9SVUbKqbfFyPw9io-NiWIDUWxDYdnhyZpohe4cCScVLM0EqQnAQ3SCkgF4-rDvFRj7qJOqGfWLiXjhTyd_cCigbizq-FPLJlyYVRwn3R44yVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امسال تعزیه‌های محرّم چرا اینجوری شده؟
🔴
داستان عوض شده یا فصل جدید کربلاست؟
🤔
آخرین باری که اینو آتیش زدن خودشون پوکیدن</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/130985" target="_blank">📅 00:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130982">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQJWR6RIWKuDJKTdQOjmCXvLJNlTM8o86yoTVJZAncLbMQOzDa4Eg9z7jvSuJhmfBEs87HHx5cpZI4XNU9ARpHfpEy40uocpIm4qJb1V7fTV1YhSwma6u21Bj9QiTpaTYFgbottWOtfCfncWbnFfzjiprXPXfDyj9u4P9q_Aon_TFGlc89jlaNRTuaCPz9JyWR7iRX2RBgdnHySoDben7AySnnxCy1MgQFAVrRA_eD9qrPMlk8hHm1aAnwFQEKvj4R4T7VuxaktDonYbTn50KP9DFRgvJURyQPlZRHoyeuQaa0PXr9EJwdCPOUjoHom8aOj1Rcvdsz4Eg6uaxsSFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI3LaR9gSF_X4ZExFOru6gxzqxkUteJCUzZXA_Wiqzn_wCHDosBvrvSW3Sfmrh-P5-t8lsiDujJaDxDBcTUeYXJw7h2ulfrGLZ_tKq6gzKD4UYSQJPP-B0aEJoQLjEKfsO9I73jAaEifT4FmyCbFRRkTfiAGHOtleE6MkvEB4kZN-1Oj9Y0jUwyGiT4juqrQxOgrvzsUJRjTBrnqJcs07975P_fyQw6axTUatUFV--5U9yrXsxjAUTyKOStUMfLZzRrq6x5HxKXgR52lja7GYLYsHeISRkV_6WJ0hzHOeO8xUoXMxEOP3czjOCxmbxMwLWiJ2s-L8DyRahuJri6lyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سرویس امنیتی عراق از منزل این‌نماینده شیعه پارلمان عراق که طرفدار مقاومت و جمهوری اسلامی بود، 20کیلو طلا و چندین‌ میلیون دلار پول نقد کشف کرد
🔴
در روزهای اخیر از منزل صدها مسئول طرفدار جبهه مقاومت میلیون‌ها دلار پول نقد و صدها کیلو طلا کشف شده
#مرگ_بر_آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/130982" target="_blank">📅 00:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130981">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSFyQwOuAGxwJgZg9FMTW2O_Gqbf-vevi1G0taCLZNCsQOmbdcmiCK7U0QU_kGaUfQProXL6koKdczuK2Kd9xOWST-_cLfm-Nn77rTivz5DSfF7tvO_R_z5mmillNgZLtQXFU4z2WrihmHF2UGKCjgB6QZg6j3O5oMNk6YjlThxstxJXcbNt-QXzq5v4SWFRXuGb6-IxK66MFG57PJBKAXa_CzuhbDYt2JWP3mp-R_03ZV2x1HybsLfo-M7XjNFS0Bf-G5gGNZ1MN3nszvPSIT3BhqQll_Ku0d4c9knQhHq_OGxrj7-SkjewHEjAwCEg01B5VtCcadzpoRTHZu32_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط یادی کنیم از شغل جناب حدادعادل قبل انقلاب که در دفتر فرح پهلوی کار میکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/130981" target="_blank">📅 00:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130980">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❤️
حداد عادل: محمدرضا شاه هم مثل پدرش عوضی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/130980" target="_blank">📅 00:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130979">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngG9tRf_7bUJ4QwFHp4htz3fxEZrvbVqy45K_7djZcv5iXCjFr8pWc_IHNWoWNCfZ2fQ71gEfIrnfjuXkOc0I4xAaoSBlXc_VL6DecpCLxE8JWgazAleYwh1SCFUsmBYzNLqKVjh2lhqNgVlfst5WchUhVw2CCEaFxhC02RMtDnYl5vt-kFnmfV7VjDILc44a7D8uNQq6snL9uwZCL0ZRqX2YCN0cNYLM7YQ0n19PC8zp3_zajCMR4Zimiqdtfi5qSNOyXjS3NHwIcEojXRTs6V8Le3YSzTum3WCI-U2MJsqxVYayf7wXTHqqyMzib9J4M35CqXdml2tKTh2FiI0kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
محمدرضا شاه هم مثل پدرش عوضی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/130979" target="_blank">📅 00:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130978">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwGWXSQk6jHt8MZwrotXMnX1GvmYXdg-qG1TvHOLxoxZLbVr4alNskSlkdHAVbl3has66FrBlqynRTLJlRy_ZDYhSJHH2EnSPGm2yvk6r5DdrDoNXO7UPWcEmsfIUELySgFycb-zE4WfjOT0jQBXY_pCYek4cnfB1jQKSejbdLGohktFJsmvUmm_zLwxzbJDDBJy0xxMSVueNt9er7xlsPMztuACOBBnYLwfW2pnyhkiw6F6ujkowrNL9C-RpdEY26R_BA3osC5YnlY5hxPF2JuNQadxeWQs5NFv-MXe6yRoZIFeuoROE7JHlei1UwzSOKOLVu2zBgRP5Lyn56Antg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه ایالات متحده، با سدام حفتر، معاون فرمانده ارتش ملی لیبی دیدار کرد تا درباره تلاش‌ها برای یکپارچه‌سازی نظامی لیبی و پیشبرد شرایط برای صلح پایدار گفتگو کنند.
🔴
ایالات متحده اعلام کرد که به همکاری با رهبران لیبی و شرکای بین‌المللی برای حمایت از لیبی‌ای صلح‌آمیزتر، متحدتر و شکوفاتر ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/130978" target="_blank">📅 00:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130977">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
شبکه خبری فرانس ۲۴: ایران روز دوشنبه اعلام کرد که نخستین دیدار خود را با عمان درباره مدیریت تنگه هرمز از زمان امضای تفاهم نامه برای پایان دادن به جنگ با آمریکا برگزار کرده است.
🔴
آمریکا در تلاش است قوانین قدیمی عبور و مرور در تنگه هرمز را برقرار کند، در حالی که ایران به وضوح اعلام کرده که قوانین جدیدی در کار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/130977" target="_blank">📅 23:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130976">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری/وزیر دفاع اسرائیل: آغاز جنگ مجدد با ایران ممکن است در عرض 2 روز آینده و با شلیک موشک از ایران به سمت ما رخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/130976" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130975">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روایت الشرق نیوز از متن کامل پیوست امنیتی توافق لبنان و اسرائیل: ارتش لبنان متعهد می‌شود اقدامات عملیاتی لازم را برای خلع سلاح حزب‌الله و تمام گروه‌های مسلح غیردولتی انجام دهد
🔴
تأیید پاکسازی از سوی یک نهاد ثالث مورد توافق طرفین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/130975" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130974">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
خبرنگار نیوزنیشن در ایکس نوشت: یک دیپلمات آگاه از مذاکرات به من می‌گوید که فردا (سه‌شنبه)، استیو ویتکاف و جرد کوشنر، در دوحه با نخست‌وزیر قطر و دیگر مقامات دیدار خواهند کرد تا در مورد مذاکرات با ایران گفت‌وگو کنند
🔴
وی در این باره افزود: روز بعد (چهارشنبه)، تیم‌های فنی از ایالات متحده و ایران به‌طور جداگانه با میانجیگران قطری و پاکستانی دیدار خواهند کرد.
🔴
پیش از این کاخ سفید مدعی شده بود که مذاکرات ایران و آمریکا این هفته در سطح بالا در قطر برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/130974" target="_blank">📅 23:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130973">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
موافقت عمان با اخذ هزینه خدمات دریایی
🔴
وزیرخارجه عمان تفاوت میان عوارض عبور و خدمات دریایی، زیست‌محیطی و مالی را توضیح داد که می‌توانند به‌طور داوطلبانه با کشورها و شرکت‌های ذی‌نفع مورد بحث قرار گیرند.
🔴
او افزود که برخی خدمات ممکن است شامل افزایش ایمنی ناوبری، حفاظت از آب‌ها در برابر آلودگی و ارتقای آمادگی برای مقابله با حوادث یا شرایط اضطراری باشد.
🔴
وی به امکان بهره‌گیری از الگوهای موجود مانند تنگهٔ مالاکا و سنگاپور اشاره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/130973" target="_blank">📅 23:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130972">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: ما تا حد زیادی با عقل سلیم حکومت می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/130972" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130971">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d045164058.mp4?token=Njosgr_odkLr4XmYtHKnLvlvJdgjtXbuTPV6K2LTVGSmxOk_RHx5oZc28WPckmVvPjMNblvJs68vDzMIO3F5fajrfb50e8dDReGP-k1pHFQaN6mqKIqMufr6cQYezNlG5k-pKyiH1mzoQ8PkngZjWhWOYZDYaJJAqk6TFCSgYkPzEQmAAHcq-Zrafn46-Qea-VlaMs3UDaTHF-EV8W2IPsb9JWph-jaI1FQ9L1qOo7TLtdqOZaLsdHxU90_VqLWmG4kY8Z1FWfLrEPst_x2MmYStmJiMdQ2jCrlJo8Mg53B1e7587IvOStfYqUFODeisq1lHsJIf_KK2pCyArlFmiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d045164058.mp4?token=Njosgr_odkLr4XmYtHKnLvlvJdgjtXbuTPV6K2LTVGSmxOk_RHx5oZc28WPckmVvPjMNblvJs68vDzMIO3F5fajrfb50e8dDReGP-k1pHFQaN6mqKIqMufr6cQYezNlG5k-pKyiH1mzoQ8PkngZjWhWOYZDYaJJAqk6TFCSgYkPzEQmAAHcq-Zrafn46-Qea-VlaMs3UDaTHF-EV8W2IPsb9JWph-jaI1FQ9L1qOo7TLtdqOZaLsdHxU90_VqLWmG4kY8Z1FWfLrEPst_x2MmYStmJiMdQ2jCrlJo8Mg53B1e7587IvOStfYqUFODeisq1lHsJIf_KK2pCyArlFmiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من قیمت داروها را ۲۰۰–۳۰۰–۴۰۰٪ کاهش می‌دهم. هیچ‌کس حتی درباره‌اش صحبت نمی‌کند.
🔴
دموکرات‌ها با این مخالفند. اگر آن‌ها به قدرت برسند، قیمت داروها ۳۰۰–۴۰۰–۵۰۰٪ افزایش خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/130971" target="_blank">📅 23:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130970">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8fc62c34.mp4?token=V2Dv8VHEP5_hJDA1KrLsapfxT3Rq4w3Ahjbljm21R6Huvmd3XxQSUBN3Cg3irZrvJ0cA-E_q5OFmwH6NvauesBqxPrtdtvOr73YGN_qJFj_oug6ehSj8x2zrQq-JJFUPofwSv4rZDUdbUl0n-zeEP2axhJmvvOs5rFBvzMLLKuK_azmuMe5zq-zy69DiCQI3pDolymxikv5mBE_jSsedJGvX4LjZ3oc6CFav3Lfjb9hpfP0u-achN_pDCOR1Wzp-99bf3A7a-6656cVO9kS2vpdVrJRYVuxDtq_SjIOwo_C9bFMnuULGHVkykllLPIspsUlf8eJttfaLcsm4Y4m_xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8fc62c34.mp4?token=V2Dv8VHEP5_hJDA1KrLsapfxT3Rq4w3Ahjbljm21R6Huvmd3XxQSUBN3Cg3irZrvJ0cA-E_q5OFmwH6NvauesBqxPrtdtvOr73YGN_qJFj_oug6ehSj8x2zrQq-JJFUPofwSv4rZDUdbUl0n-zeEP2axhJmvvOs5rFBvzMLLKuK_azmuMe5zq-zy69DiCQI3pDolymxikv5mBE_jSsedJGvX4LjZ3oc6CFav3Lfjb9hpfP0u-achN_pDCOR1Wzp-99bf3A7a-6656cVO9kS2vpdVrJRYVuxDtq_SjIOwo_C9bFMnuULGHVkykllLPIspsUlf8eJttfaLcsm4Y4m_xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در میدان نظامی پیروزیم. می‌توانم بگویم تقریباً در میدان نظامی پیروز شده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/130970" target="_blank">📅 23:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130969">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262fb7eb01.mp4?token=WGAaIYw2BZ9FjJe1tWvIj14uDHL00vJ_maqrrqub8OqUdgqMrwJzJoHXjwPAaiwfbYe6M9u1raVZya9W_m523n3F6I1zSjpol9FK5DTtbzaKWuj9m4wWDmUmMl_qD1UzKa5DcJqdGCLLzYrh4y_mF8-ZBNALt80LFKz5uPidUNwame9blpaMap3B5MRCmBpWSi8Am-y4NuBF3swrWgYMXxnrjqp6GoFSNH-7b9cCAWIEcIjRj06GqkT3FRgKNx7QPWNnnXrF8vak6I7-mVA4a2-_Z2YMlllH10TWOYevhA9SRnra6OIRSWvvkt6BTDAnjo3YbATvgKzxUUtJ9iNryBEt7Xlt0lZ-zkhvDaN8PpZ5TG85C11nL-Tc-kvUxG4JZEUMyN_Unb5P1Sa0tgMeF3U_WUg79_aARWB3AKAuT6zRpLEpfCLYU9xhzOLYS-NwYuGf8_qFMvCUlsL-2RHMVoMELoQdawoucTpf6-Bio5LYXydFtqKRn-TPRgmtZ1bzQOZupeXPq-EuGkTfrqfEN4w3ZECdCpzg5DiB4YB2W4W-JfokR8qvx_Hq9-lhhIdzWUj3kcqxk4YrmXapACWssmc31AbqyHcDjhFfg6sexhjg1wl5onu_GFLxKbjn6XLNnQC67OxHW3cpMoRnZjPqh4MwZX2SaM1l9uUXgCHiy4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262fb7eb01.mp4?token=WGAaIYw2BZ9FjJe1tWvIj14uDHL00vJ_maqrrqub8OqUdgqMrwJzJoHXjwPAaiwfbYe6M9u1raVZya9W_m523n3F6I1zSjpol9FK5DTtbzaKWuj9m4wWDmUmMl_qD1UzKa5DcJqdGCLLzYrh4y_mF8-ZBNALt80LFKz5uPidUNwame9blpaMap3B5MRCmBpWSi8Am-y4NuBF3swrWgYMXxnrjqp6GoFSNH-7b9cCAWIEcIjRj06GqkT3FRgKNx7QPWNnnXrF8vak6I7-mVA4a2-_Z2YMlllH10TWOYevhA9SRnra6OIRSWvvkt6BTDAnjo3YbATvgKzxUUtJ9iNryBEt7Xlt0lZ-zkhvDaN8PpZ5TG85C11nL-Tc-kvUxG4JZEUMyN_Unb5P1Sa0tgMeF3U_WUg79_aARWB3AKAuT6zRpLEpfCLYU9xhzOLYS-NwYuGf8_qFMvCUlsL-2RHMVoMELoQdawoucTpf6-Bio5LYXydFtqKRn-TPRgmtZ1bzQOZupeXPq-EuGkTfrqfEN4w3ZECdCpzg5DiB4YB2W4W-JfokR8qvx_Hq9-lhhIdzWUj3kcqxk4YrmXapACWssmc31AbqyHcDjhFfg6sexhjg1wl5onu_GFLxKbjn6XLNnQC67OxHW3cpMoRnZjPqh4MwZX2SaM1l9uUXgCHiy4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کمونیسم: این سوسیالیسم نیست؛ واقعاً کمونیسم است. آنها از عبارت «دموکرات اجتماعی» استفاده می‌کنند چون زیبا به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
🔴
فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ما است، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، یازده سپتامبر و حمله پرل هاربر می‌شود.
🔴
فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ما است. مردم وقتی این را می‌گویم لبخند می‌زنند، اما افراد باهوش خواهند گفت: «می‌دانی، احتمالاً حق با اوست.»
🔴
در واقع این معرفی کمونیسم به ایالات متحده آمریکا است. هرگز چیزی به این خطرناکی نبوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/130969" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130968">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681f6a849a.mp4?token=E2MDJ5kcY9bFS3Iua_pSQ69PUniaPp0X67HbsZ4LYbgz7NUZ0fUlA0rrBPArKLthMedRSmZpH3Rr5c7QFva-Eqpfszw9AOess21ty19KisoUcBepB2qgy6A6VelCDbYjlwW4QWf9zLQVhudXm7PFo5yvLyI-F6vV31V3w4AHMuoO--6JkZ9MiN2onMC82aCN-km_KpP9MgusXygcfwpEBYIDJ4WEC2-J0Yib5Mj6uc5pSa_Th7VpNRzvqTCM_y3Vd8-wwemJbr09N_7eNVteQrual62yad0JeixFgf9KHh-FFWNOq937jpFYdzkTAriT59BPZHsPBHjDrTuVqTjSyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681f6a849a.mp4?token=E2MDJ5kcY9bFS3Iua_pSQ69PUniaPp0X67HbsZ4LYbgz7NUZ0fUlA0rrBPArKLthMedRSmZpH3Rr5c7QFva-Eqpfszw9AOess21ty19KisoUcBepB2qgy6A6VelCDbYjlwW4QWf9zLQVhudXm7PFo5yvLyI-F6vV31V3w4AHMuoO--6JkZ9MiN2onMC82aCN-km_KpP9MgusXygcfwpEBYIDJ4WEC2-J0Yib5Mj6uc5pSa_Th7VpNRzvqTCM_y3Vd8-wwemJbr09N_7eNVteQrual62yad0JeixFgf9KHh-FFWNOq937jpFYdzkTAriT59BPZHsPBHjDrTuVqTjSyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنها مردم را به خاطر تعمیر ماشینشان دستگیر می‌کردند.
🔴
این حتی باورکردنی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130968" target="_blank">📅 23:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130967">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ : قیمت نفت خیلی کاهش پیدا کرده، ببینید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/130967" target="_blank">📅 23:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130966">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca333bc10.mp4?token=RiduC8BIrr8DzTU34Z34Hr9XxusfXF71-LzS4TW2Jz9nTK0i5z1zm2LMFUyDLrFis7xWI7Jfqm9HRt7owX8cX_RFfxId6KbILifqnK2_spLbueEmI93erQNn_gyVyFF5UkXwU-vYqbf2W-dfXN9xHLINCnsEFhQOTNrPF-vSLoH4DdFq6BIPYwD2AV5wWgFXVuQ10KobaXrKtaHJiNUXl9fDN-DyCbdzHs6j-Kk-IsFZjcBCZdqJj50JWP1rcGHMk-QnIGUYsaXxyEAY1crsAV9tPOdFEOhTTx84Tc7Z2G2YeMLpAjQKOrDQUtviSAdPBacnP19q-pTZK3fBr-_H1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca333bc10.mp4?token=RiduC8BIrr8DzTU34Z34Hr9XxusfXF71-LzS4TW2Jz9nTK0i5z1zm2LMFUyDLrFis7xWI7Jfqm9HRt7owX8cX_RFfxId6KbILifqnK2_spLbueEmI93erQNn_gyVyFF5UkXwU-vYqbf2W-dfXN9xHLINCnsEFhQOTNrPF-vSLoH4DdFq6BIPYwD2AV5wWgFXVuQ10KobaXrKtaHJiNUXl9fDN-DyCbdzHs6j-Kk-IsFZjcBCZdqJj50JWP1rcGHMk-QnIGUYsaXxyEAY1crsAV9tPOdFEOhTTx84Tc7Z2G2YeMLpAjQKOrDQUtviSAdPBacnP19q-pTZK3fBr-_H1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: نشست دوحه برگزار خواهد شد؛ شاید مهم باشد، شاید هم نباشد
🔴
خواهیم فهمید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/130966" target="_blank">📅 23:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130965">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گزارش ها از آغاز دور جدید حملات هوایی در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130965" target="_blank">📅 22:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130964">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n47KQhw6TGatFeo1IFg-O5IwRZw0tQ3ydRkqRtxdoRIhevmfU_k5NvHETl1OT2uKoRblxlCqGRGvEB-vEEoi29w6gkY4Z7xTdk8InByeCfppGfdVyAYtJSNTRk6uYZPp89KUuDWxk59v9wqrf59IdNl5AuotFtZsQh6EFkXtyu-BaNLw_ruVy-kUILqZh1ARtJyikNAQqCzu_XTi9OutpgLUVKvtcf3y7zLgYdCy26lYMoLU6Z4jgmyvnucMuuO8oCr1i4GyiE1FxqwsAZAPeF3D5bEbPWIJnGVQKTkFtPT3As7y8yW7EIuRBT8Dft0qedXjLM2vEImtlhdh0OyGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاضل میبدی : جنگ‌طلبان اگر عاشق شهادتند، راهی بیروت یا غزه شوند/ رفراندوم بگذارید تا ببینید مردم چه می خواهند، مذاکره و صلح یا شعار مرگ و جنگ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/130964" target="_blank">📅 22:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130963">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTlfMcrjL4_BWUU6i5Gd0II39lV1zP_9cxvoFtlQTI-vB8Vd7z4_e8Hw16RmXAmkrbsTcBAO5urtAo31cK7yxZNuuV1zcsRpztkwyeKimVHQCVkolV3mc-Em0sFV4XXnocDXLFToaCPe43YGU4HkmmAmQ66t5KZVqFOqefiO1OLoibMap-TQ-llIlCFjYgTfhvgtm1Mkt7ZIxsOD138sx77nYmZ3iY8Q_k5H8A2swSToVj2P9mgUYBEUBCh0SElm7tKiVCKomu0cr4Z2rGGhgtBsT-cPQ1WXPONCEq2OsPWlXUSMkUSu7GOV-_pvE1qX1FeuaFylPKhiWSYinipc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ادعای اینکه من با تهدید به استعفا موجب تغییر تصمیمات نهادهای عالی کشور شده باشم، صحت ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/130963" target="_blank">📅 22:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130962">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8j2hcUwtYP3Zw_QHldY0VZ111_6F64bd0jrgARaHDlRIWVXFms28VLrmbKlgoaAPYIX9Shyu8mWinQjgIoLGfd4asqlkfdsjIsCu8x9lDGN2YHo1Fr48hlL2RLhOCEIhK6RFgI_bBVbhrSK_QrqOvT6ZPU3nydhTzaV7SRsdGVbiooSn6HA-Zz5-iJeHy3B0lu8BFc_pXepz6pE3EVW0j7k0HW-VK_jGlH7Te23Xa9KWHLTUHAQWv72FFJkvm8sfsrLbGY7fRgR7MA-IzmvIiqA8jq4KCvQD7FcFuWYMNV56h2nx1AcP9q3tzB9EQNoBa9HvetIxPs7Og2agvVZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
رضا شاه یه آدم بی دین، فاسد، عوضی بود و وقتی مرد کل ایران خوشحال شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130962" target="_blank">📅 22:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130961">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات های زیر :
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/130961" target="_blank">📅 22:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130960">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/130960" target="_blank">📅 22:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
جیک سالیوان، مشاور سابق امنیت ملی آمریکا: کشورهای منطقه دنبال توافق اختصاصی با ایران بر سر تنگهٔ هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/130959" target="_blank">📅 22:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزارت امور خارجه ایران اعلام کرد: ما خواستار دریافت هزینه خدمات در تنگه هرمز هستیم و این موضوع را با سلطنت عمان مورد بحث و گفت‌وگو قرار داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/130958" target="_blank">📅 22:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130957">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
حجت میرزایی، اقتصاددان: نمی‌گویم ۲۰ سال اما حداقل ۱۰ سال زمان می‌برد تا پس از لغو تحریم‌ها به دوره اقتصادی سیدمحمد خاتمی برگردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/130957" target="_blank">📅 22:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130956">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=J6fnWK3Kna6zDDklEGq7rdL9z28yoJbhePagZQe7TX4PgsrzQdw5t6nouRgWkjK8GiXsI0POe3iNaMSD_9MrguUPJmhTec1vVJhbUJmB9a1ZGhGYy-qV4ScEiWCxxmsZ7L_1zjHLCGSzxuNwcNYSSHFrwOFe_oeCeSX8dn_ZOj7LameyrQFhyA2wkYTynigjotbzEHPvYmPELGblYYy9YWEtQtt1C6Gek_ZBjWlSPrNFWsdkByXIR8l4trTArLrgrHj3J4VSJEAZ820tEHv_1DVgaML04wR6HIBHJsX0Mq0jl6PSESl0NuBuU6ksQcHx-oprESIHKwJeDrR5u_u6NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=J6fnWK3Kna6zDDklEGq7rdL9z28yoJbhePagZQe7TX4PgsrzQdw5t6nouRgWkjK8GiXsI0POe3iNaMSD_9MrguUPJmhTec1vVJhbUJmB9a1ZGhGYy-qV4ScEiWCxxmsZ7L_1zjHLCGSzxuNwcNYSSHFrwOFe_oeCeSX8dn_ZOj7LameyrQFhyA2wkYTynigjotbzEHPvYmPELGblYYy9YWEtQtt1C6Gek_ZBjWlSPrNFWsdkByXIR8l4trTArLrgrHj3J4VSJEAZ820tEHv_1DVgaML04wR6HIBHJsX0Mq0jl6PSESl0NuBuU6ksQcHx-oprESIHKwJeDrR5u_u6NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس تلویزیون: جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/130956" target="_blank">📅 21:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130955">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آنتونیو گوترش، دبیرکل سازمان ملل متحد: تروریسم در حال تحول است — فناوری‌های نوظهور از جمله هوش مصنوعی، پلتفرم‌های دیجیتال و سلاح‌های بدون سرنشین را مورد سوءاستفاده قرار می‌دهد. هیچ کشوری نمی‌تواند به تنهایی به آن پاسخ دهد.
🔴
ما باید پیشگیری، همکاری و تعهد خود به حقوق بشر را تقویت کنیم تا جهانی امن‌تر بسازیم که در آن مردم بدون ترس زندگی کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/130955" target="_blank">📅 21:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130954">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-zRR4t-C3ONOwISpD6oxrhn2YZEwqEVKpi_tuoYJf53CJcfJvF8U1GaCXbeePOZ-P-27_YKqz8uVrAIQ8PPEezzgOwXTVYE7FWF6IMXAyG20IwJlLUOVB9Nw-EZQtELgouUL-fk8uy6DHO8h1iGRbqQ16JG1hdjETX9JU5eEBUklQE37G_1y3Y3-jZq_s813ITZaTgM7_L4hkCFajBKMnRhtRaSJd8fDs-jTxpWuJ9p2TTAS9BUtwnrG1Np0azw5XtjNetY3IsoPX2YWcSxlhkL3rJ2hFhMLhgcZijt2rLxhg9zODSF2j9wnTkcF9INTFlyAZVgCf3SoYaN3e8B6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: آمریکا اگه توافق میخواد باید ترامپ رو تحویل ما بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/130954" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130953">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=vrRcOPtO2Ts1Qf3DVUmLaOc8gFeTuwaHmvArMBzNJk9yhFGWnE-GSiLmIN9gc5hac5wux1rRZV_YDAjUcf-Hcwrt8SLXlnhig_J0jY-lp28Mk7VsO2w_7qh85u_UnpbPmdhe863qhLNO4zP6VibP5XwCYLDjEtIVfv-jVCo0hOkosq6LGy461xnD-TAD0ftO2iu7N-xW0hr7BbiFrG_HEZXgUb0MrmkCiC_KpqIRL3knD-oEwf58uthOjXVK_l2bMUSqdX3b5-8dasouepb4cgOpiqQnRD20pQ9-O2bFnogjm92Cyfpii1RC2OZqPGwzv8ExhDBw6ZnjB9XFDZfjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=vrRcOPtO2Ts1Qf3DVUmLaOc8gFeTuwaHmvArMBzNJk9yhFGWnE-GSiLmIN9gc5hac5wux1rRZV_YDAjUcf-Hcwrt8SLXlnhig_J0jY-lp28Mk7VsO2w_7qh85u_UnpbPmdhe863qhLNO4zP6VibP5XwCYLDjEtIVfv-jVCo0hOkosq6LGy461xnD-TAD0ftO2iu7N-xW0hr7BbiFrG_HEZXgUb0MrmkCiC_KpqIRL3knD-oEwf58uthOjXVK_l2bMUSqdX3b5-8dasouepb4cgOpiqQnRD20pQ9-O2bFnogjm92Cyfpii1RC2OZqPGwzv8ExhDBw6ZnjB9XFDZfjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا مذاکرات هسته‌ای با آمریکا آغاز شده؟!
آجورلو، عضو رسانه‌ای تیم مذاکره‌کننده:
تا الان هیچ مذاکرۀ هسته‌ای با آمریکا انجام نشده و تا عملی‌شدن شروط ایران هم مذاکره‌ای دربارۀ موضوعات هسته‌ای انجام نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/130953" target="_blank">📅 21:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130951">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس:
محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه،
در یک سانحه رانندگی ساعاتی پیش درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130951" target="_blank">📅 21:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130950">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/130950" target="_blank">📅 21:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130949">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: هنوز وارد مرحلۀ مذاکره برای توافق نهایی نشده‌ایم
🔴
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آن‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130949" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130948">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=M7p6FEkjdwJUrZ_X-gmnIpQPL6fRzDimg23SehNMdJmOV8VGDge4LmnVh1hqnI-lM5yn-gK62y7Zuxi3PbV2Zek0Qboql9lRPQ83gB6ALjyVUJ_q2jCPLlJ72vCuJQ4TD5g5OpJP-I-kXrJSIin1O5aC-mt0ikKOCUiWpzh0ucNSeynTTzyPIjMPg7kdK-rdJkY91VAZP2aHBDhjv_DG1KWKThyWIAkx33pUrsDANwWQ_PU-jX2-_5aYXIw4aR9Rj47hZv8OcvJg-GuUYcz-V-VLGFT4cWJHumRUTCHaLHgHslADaAB2KpaN8BZsrqZ03UPKzUNQ42fAFFHt_NSSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=M7p6FEkjdwJUrZ_X-gmnIpQPL6fRzDimg23SehNMdJmOV8VGDge4LmnVh1hqnI-lM5yn-gK62y7Zuxi3PbV2Zek0Qboql9lRPQ83gB6ALjyVUJ_q2jCPLlJ72vCuJQ4TD5g5OpJP-I-kXrJSIin1O5aC-mt0ikKOCUiWpzh0ucNSeynTTzyPIjMPg7kdK-rdJkY91VAZP2aHBDhjv_DG1KWKThyWIAkx33pUrsDANwWQ_PU-jX2-_5aYXIw4aR9Rj47hZv8OcvJg-GuUYcz-V-VLGFT4cWJHumRUTCHaLHgHslADaAB2KpaN8BZsrqZ03UPKzUNQ42fAFFHt_NSSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات حق استاد محمود سریع‌القلم، مشاور سابق روحانی:دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
🔴
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
🔴
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/130948" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130947">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEgc1yoLO0Gg_ZQWVh_v4ig05K7qUp1qtHprCUJKxzVYC2KZa5SyDC1v2wXMBZx24YTrIGlX6fJvwgTFIe43vs9_HlApbnI8ZITgmNP5ShkKjXYoWpMkthP_uQrpvQVF_nn5b3ZA2zLFRft93Vj7MhZbIxy_tKLNXy_W3IfKVWy7C9tMJsvpQNSaSYqTXc9XyS1vWYx1-9y6BgNJv6xuQNbr7cr-S9lfu6snwuzYCB_0ha3ojuHc0TMwI40AWtNk0zLMjfvMpDN-Evo0TItlEdotyyvWMR5MR6s1KV5HExA7j_a4ad4ZtCk0GeSY898iw5A5FpBA1RtEmpjSndKYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژاپن موشک هایپرسونیک «تایپ ۲۵» را برای حملات دوربرد عملیاتی کرد
🔴
نیروهای دفاع زمینی ژاپن نخستین یگان مجهز به موشک هایپرسونیک «تایپ ۲۵» (HVGP) را عملیاتی کرده‌اند؛ سامانه‌ای که با هدف تقویت توان بازدارندگی و اجرای حملات دوربرد علیه اهداف دریایی و زمینی توسعه یافته است.
🔴
این موشک از فناوری Boost-Glide بهره می‌برد؛ به این معنا که ابتدا توسط یک بوستر راکتی به ارتفاع بالا و سرعت بسیار زیاد می‌رسد، سپس سرجنگی گلایدکننده آن با سرعت هایپرسونیک و در مسیر مانورپذیر به سمت هدف حرکت می‌کند؛ قابلیتی که رهگیری آن را برای سامانه‌های پدافندی دشوارتر می‌کند.
🔴
«تایپ ۲۵» به سامانه هدایت ترکیبی، ناوبری اینرسی و ماهواره‌ای مجهز است و برای هدف قرار دادن شناورهای سطحی و اهداف زمینی با دقت بالا طراحی شده است. ژاپن همچنین در حال توسعه نسخه‌های پیشرفته‌تر این موشک با بردی بین ۲ تا ۳ هزار کیلومتر و سرجنگی ارتقایافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/130947" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130946">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd900cb7d1.mp4?token=YRrBkTUly-Q6ZwSDpDL8CYvhu6tdZ1NZLypJs2Vna9tI5NDyoPQL_S7fxiEKSgET0izng1w6vWoLjUrEayEAnthzF6ZDf60IieQiR4nxu-1TylgKB-RbAAxEjlDwbVv-LKQZGFbzZeRMzog5KB0UOj3OP_dWXu8zfYhIfmiWrhYmhnoZdb2dnF_qWlPwHNP4yio2SwRTkRe0F98C-FnP-Pj9898q5BViKfjJkNwAqChdBnsrOrtEN2uAYf3JDIDSCxYutyIVdp5zgDeNMQxN1V7QbbMGx7jNrig57NCi-_fRz-FYl4pnlbNwPWWt1n_m4sd82onByKTx5snx3EyTww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd900cb7d1.mp4?token=YRrBkTUly-Q6ZwSDpDL8CYvhu6tdZ1NZLypJs2Vna9tI5NDyoPQL_S7fxiEKSgET0izng1w6vWoLjUrEayEAnthzF6ZDf60IieQiR4nxu-1TylgKB-RbAAxEjlDwbVv-LKQZGFbzZeRMzog5KB0UOj3OP_dWXu8zfYhIfmiWrhYmhnoZdb2dnF_qWlPwHNP4yio2SwRTkRe0F98C-FnP-Pj9898q5BViKfjJkNwAqChdBnsrOrtEN2uAYf3JDIDSCxYutyIVdp5zgDeNMQxN1V7QbbMGx7jNrig57NCi-_fRz-FYl4pnlbNwPWWt1n_m4sd82onByKTx5snx3EyTww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: آزادی گروگان‌ها بدون پذیرش شروط حماس و خروج از غزه ممکن شد. فشار نظامی، فشار دیپلماتیک و حمایت آمریکا عامل این نتیجه بوده و اگر اسرائیل با خواسته‌های حماس موافقت می‌کرد، رهبران این گروه و دیگر گروه‌های هم‌پیمان همچنان در قدرت باقی می‌ماندند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/130946" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130945">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8jMKX6pp3BWnxbvdNcM1kIVze5X8GYp4kR8jV9G-EhEiJSnUJAmODMloA_ZykrnThBxl3m7oXQQUOxtCyYcXewS4JoHRWIoyzv_P1izW-Xm8vbT4pYl7SxwMWr70YbF7s3nZ6QvlaqcJVqG_E_SMIS1bMzRLCg-1Sez7HB1R7FrVDfPrqoUNWNS3cti9ZxiCxFdVKXfr8Nc3wpUqPwOXdB94garECY-sNo_lVkw-u5dVX6mZrR6JPzuI2s5AABnv9Yz_Tyx3aQhA5sTKvyJKUv19Y3Q2DhUEGaNBzIgmwEEMXPJ0Af1ffVRMGn1sHabrOsitf0wMBF5xb9yKaB15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری میکند. طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام میشود و نه هیچ کشور دیگری، اصولا اجازه چنین کاری را هم نمیدهیم.
🔴
شرایط حساس و پیچیده است. توصیه اکید میکنیم فرانسه آنرا با تحریکاتش پیچیده تر نکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/130945" target="_blank">📅 20:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130944">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ایران اعلام کرد که برخلاف ادعاهای مقام‌های آمریکایی، هیچ برنامه‌ای برای برگزاری مذاکرات مستقیم با ایالات متحده در این هفته وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/130944" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130943">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی دولت عراق اعلام کرد:
دولت به کلیه گروه‌های مسلح در این کشور تا ۳۰ سپتامبر سال جاری،‌ هشتم مهرماه آینده، فرصت داده تا سلاح‌های خود را تحویل دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/130943" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130942">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0F2CUWjBb9_4xni-lT7w28dPdqMeXLGTacWJ_uuZxlZ9pYBi6Ukq8yeqoNYgLkBKO077TPdenUHBqra_5R24FOCZtu6iTyO1lJDjcvW97XhxJnpNMsDDkqdCSbP_EGjx1Ze_yY_1gYBU5x9EJ9eORiAE0fm9d8nu7VG44NvzUmTgNCXl3nedomFvTiagO2Bwpfhzww0xumGJ7eAdMMM5EHBjBYoiPODTM-uZt78IbPnr1oWFid5_qEaaoEl7D-_Iv_3haq8s8U14aWaKTWHvOVOm7-WzDW1l1XKNUI8LCj8xLlv-O3Fjbb1G8S0o7_8u5bTXRbnnrrsFEEndjvJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عالی ایالات متحده روز دوشنبه با صدور حکمی، اخراج روسای نهادهای مستقل توسط «دونالد ترامپ» رئیس‌جمهور آمریکا را آسان‌تر کرد؛ تصمیمی که توازن قدرت را از کنگره به سوی ترامپ تغییر می‌دهد و می‌تواند نحوه فعالیت بیش از دوازده نهاد فدرال را بازتعریف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/130942" target="_blank">📅 20:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130941">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8041c64fe8.mp4?token=R1QAx8at2YerX3949VlSvDto7zSpPHwq4hXqQJcYhv_YO6NbPKxGSDKaWEhdqd_ippEtmnx6IfaIfIAzwoA6e-3raSJiP5B2q2qQfq03XdfV7DAb0WoYicaNwYZVBj_XNYfPlbOgZnQBueBNUshPuV3IIaxG0YUTxXkzhNE1lSmmIxu2TKHJZ59kGjpGl5Czojv6QELysGAgz5e_Hf1AZI-G2CDGQSKtnmz2xaGJAAlwhv9_CvW-sIxCx6ynkKxnnkaARU5wkEq7pFiVnAHXRmNpTIHQDgPwFq0GmAtVTmEvXd_4JyK2DI_4s8YgKPp7YOnYMeJpPciUJ3SdhWO3JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8041c64fe8.mp4?token=R1QAx8at2YerX3949VlSvDto7zSpPHwq4hXqQJcYhv_YO6NbPKxGSDKaWEhdqd_ippEtmnx6IfaIfIAzwoA6e-3raSJiP5B2q2qQfq03XdfV7DAb0WoYicaNwYZVBj_XNYfPlbOgZnQBueBNUshPuV3IIaxG0YUTxXkzhNE1lSmmIxu2TKHJZ59kGjpGl5Czojv6QELysGAgz5e_Hf1AZI-G2CDGQSKtnmz2xaGJAAlwhv9_CvW-sIxCx6ynkKxnnkaARU5wkEq7pFiVnAHXRmNpTIHQDgPwFq0GmAtVTmEvXd_4JyK2DI_4s8YgKPp7YOnYMeJpPciUJ3SdhWO3JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال مکرون (رئیس جمهوری فرانسه) از سلطان عمان در کاخ الیزه پاریس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/130941" target="_blank">📅 20:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130940">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3dcc1c10.mp4?token=L_KiX0abHgpLFtKxs-XPFdcOcoAH7b1WNNxX7ctbQbDiRDOUNCxJFiyE-q8cR7E51f1M2PZnuO0MPeCaUWpSOe2VrIYzk-qQ9CsYuLvCAXwzPmWdWUb1FvDY1J77hortxjcmPt6uzA95ehwGGxeP1ophfXWSCFe8yC-e0VyBUDkQP1g4r7taviMlmE3MKjPYzZZRejbKoKMBunjZDi8NiqvnLTYwrOHQHFdixnWwRfgf03MypxrZFKKUksV_CAkSTvVNGzY30rPkdx4lUZPdBhdJgBwRefM13w1JJinNG6s6-0OPIFBEVosQ4dTbudNUxnzhXOx2ECOA9MXFO8dWvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3dcc1c10.mp4?token=L_KiX0abHgpLFtKxs-XPFdcOcoAH7b1WNNxX7ctbQbDiRDOUNCxJFiyE-q8cR7E51f1M2PZnuO0MPeCaUWpSOe2VrIYzk-qQ9CsYuLvCAXwzPmWdWUb1FvDY1J77hortxjcmPt6uzA95ehwGGxeP1ophfXWSCFe8yC-e0VyBUDkQP1g4r7taviMlmE3MKjPYzZZRejbKoKMBunjZDi8NiqvnLTYwrOHQHFdixnWwRfgf03MypxrZFKKUksV_CAkSTvVNGzY30rPkdx4lUZPdBhdJgBwRefM13w1JJinNG6s6-0OPIFBEVosQ4dTbudNUxnzhXOx2ECOA9MXFO8dWvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروژه تانک ساخته‌شده توسط دانشجویان طالب دانشکده مهندسی در افغانستان: نصب دوربین مداربسته روی تانک کنترلی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/130940" target="_blank">📅 20:20 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
