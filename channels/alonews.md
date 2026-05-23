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
<img src="https://cdn4.telesco.pe/file/GF3qY5PHxQrJubVCVnqCBGxJVuDmbjZNpZDpQWCvz4v6KP8LR91hMGs76EOdmBEHKmQ_2dTU_673JQVt-OZ4X6yM88Fcjoi15jLKz0odBD0-LkMpW6L6w4ZjVOmV-w35U9xBVskEvkAg5Aaz--V0vghYMO0Wz4gI1qtyBp7r4dWTyEttM2ks_lpiJeNPQmbvwfMedrMWh9VjicJ_FZZuhtjyP2MwPvOELM_0yxjWcup1Lx2bVUsmFkT2igAzFJjoXqAMJwJqbISNB93xZxbEI5jrhCF5bbcKXGiLKBRw7gnBRg-rHEW6sJJ3X5O3xLuohUGt7smAjsvfU5LrM4XOfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 22:33:04</div>
<hr>

<div class="tg-post" id="msg-122152">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یک دیپلمات منطقه‌ای به فاکس نیوز:
«تماس سران عرب و ترامپ بسیار مثبت بود. پیشرفت خوبی در حال انجام است. رهبران منطقه از این پیشرفت که ترامپ با مذاکرات به دست آورد، حمایت کردند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/122152" target="_blank">📅 22:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122151">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / هم اکنون جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/alonews/122151" target="_blank">📅 22:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122150">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سفیر ایران در پاکستان: چند دقیقه پیش، جناب وزیر محترم کشور پاکستان، برادر عزیزم محسن نقوی، پس از بازگشت از تهران، مرا از دستاوردهای مذاکرات با مقامات کشورم مطلع کردند.
🔴
با خوش‌بینی محتاطانه می‌توان امیدوار بود که در صورت پایبندی کافی طرف مقابل، گام مثبتی در حال شکل‌گیری است که نتیجه مواضع جمهوری اسلامی ایران مبتنی بر عزت، ایستادگی نیروهای مسلح شجاع و مقاومت ملت شجاع ایران، همچنین ابتکار و تلاش‌های فداکارانه میانجی پاکستان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/alonews/122150" target="_blank">📅 22:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122149">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
۷ نماینده کاندید نایب‌‌رئیسی مجلس شدند
🔴
علی نیکزاد ثمرین نماینده اردبیل
🔴
عبدالرضا مصری نماینده کرمانشاه
🔴
حسینعلی حاجی دلیگانی نماینده شاهین شهر
🔴
حمیدرضا حاجی بابایی نماینده همدان
🔴
رضا جباری نماینده مسجد سلیمان
🔴
علیرضا منادی نماینده تبریز
🔴
پیمان فلسفی نماینده تهران
🔴
انتخابات هیئت رئیسه مجلس دوشنبه این هفته برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/alonews/122149" target="_blank">📅 22:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122148">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0PzAOaJ0XfpzvMClKdWmVbd0hu0TaGV50G6J1j4vEz055srVrCOBeBT5D-_anLYWScdxg6PpHzpIfZ12FiZ5xj-a5ZyQ57spX1DkdjRB-BG4AXvlHAAgytp1DYtdGRItEOb1P0R1dXI4lceMpQi9a3miuB6Im4uyeBOHMqtMvl7zaI_rs1ejOPaJihne8Xnmt2QszEnA2EYuGw7WQad-HvX5BIT_0G5FMgwtJ53mkQLWj3tlYHRKy0CeC8PdHY2VV_906YEw3Ued3mxDd2BX2Q4V1l-hbjBTn75It7Gr7HE9POXFZ9zzEeR8KIz3pdLejtVWjcA9kRAHqkcgb8NVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت قیمت تتر بعد از اخبار مذاکرات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/alonews/122148" target="_blank">📅 22:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122147">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سی ان ان به نقل از یک منبع اسرائیلی: نتانیاهو یک نشست امنیتی محدود برای گفتگو درباره تحولات مذاکرات با ایران برگزار خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/alonews/122147" target="_blank">📅 22:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122146">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
اکسیوس: معاون رئیس جمهور از اوهایو و وزیر جنگ از نیویورک برای جلسه‌ای در مورد این توافق به واشنگتن احضار شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/alonews/122146" target="_blank">📅 22:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122145">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kS26UoylyETSh7kHn_8_oLe4hkiGWYkDTRt21yqOQGhldumCUvIlbezTFvMqjK1kmcmbYOKtZZJnM7f3gGRbqdo4zvL_qM8R0CeUjAn7MyL8MHUUfR-qI4qa9wNjvpP0zDrh60gT23dkxeLWqfYlaQojFj-0mItB0gJyVGpx72HsX55g1LkulRdy4WdGydTNw6gAym6sUl0TsHJStw8jOMeS-j80ZTBie4pEAitSUvC4CabkzRG3dXK3XL1ShxELQevWnfJq5-Q1dYeuV0-zqZWgSPRj138WYc9NIfnW1-T6hYtMB2RUSE_ljgOsrqeLdUv4a4ts9bTBKqO39Gn6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال توافق ایران و آمریکا صدای انتقاد سناتور لیندسی گراهام را بلند کرد!
🔴
گراهام اگر توافقی برای پایان دادن به درگیری ایران حاصل شود،زیرا اعتقاد بر این است که تنگه هرمز را نمی‌توان از تروریسم ایران محافظت کرد و ایران هنوز توانایی تخریب زیرساخت‌های اصلی نفتی خلیج فارس را دارد،در آن صورت ایران به عنوان یک نیروی مسلط که نیاز به یک راه حل دیپلماتیک دارد، تلقی خواهد شد.
🔴
این ترکیب از اینکه ایران به عنوان کشوری که توانایی ایجاد رعب و وحشت دائمی در تنگه هرمز را دارد و قادر به وارد کردن خسارات گسترده به زیرساخت‌های نفتی خلیج فارس است،یک تغییر عمده در توازن قدرت در منطقه می‌باشد.و با گذشت زمان برای اسرائیل به یک کابوس تبدیل خواهد شد.
🔴
همچنین،اگر این برداشت‌ها دقیق باشند، باعث تعجب می‌شود که چرا این جنگ آغاز شد.من شخصاً به این ایده که نمی‌توان توانایی ایجاد رعب و وحشت در تنگه هرمز را از ایران سلب کرد و منطقه نمی‌تواند از خود در برابر توانایی نظامی ایران محافظت کند، شک دارم.مهم است که این موضوع را درست درک کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/122145" target="_blank">📅 22:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122144">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
دو منبع پاکستانی به رویترز: انتظار می‌رود پاسخ آمریکا به پیشنهاد توافق فردا یکشنبه اعلام شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/122144" target="_blank">📅 22:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122143">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ با سران منطقه ( رهبران عربستان، قطر، امارات، مصر، ترکیه و پاکستان) گفتگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/alonews/122143" target="_blank">📅 22:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122142">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ادعای کانال ۱۴ اسرائیل: چند منبع معتبر تأیید می‌کنند که ایران با برخی از درخواست‌های کلیدی ایالات متحده موافقت کرده است و کمتر از ۲۴ ساعت دیگر اعلام توافق انجام خواهد شد که به تهران چند ماه فرصت می‌دهد تا کاملاً تسلیم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/alonews/122142" target="_blank">📅 22:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122141">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بلومبرگ: ایران و پاکستان پیشنهاد بازنگری‌شده‌ای را به ایالات متحده برای پایان دادن به درگیری و بازگشایی تنگه هرمز ارسال کرده‌اند؛ دو منبع پاکستانی آگاه از مذاکرات این موضوع را به بلومبرگ گفته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/122141" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122140">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبرنگار الجزيرة: ۳ حمله هوایی اسرائیل به شهر دیر قانون النهر در منطقه صور در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/122140" target="_blank">📅 21:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122139">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
هم اکنون تماس تلفنی نتانیاهو و ترامپ!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122139" target="_blank">📅 21:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122138">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
آکسیوس به گفته یک مقام آگاه آمریکایی: ترامپ هنوز تصمیم نهایی در مورد توافق با ایران نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122138" target="_blank">📅 21:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122137">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری / هم اکنون جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122137" target="_blank">📅 21:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122136">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ارتش اسرائیل: کشته شدن یک سرباز و زخمی شدن ۲ نفر در انفجار پهپاد در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122136" target="_blank">📅 21:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122135">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام پاکستانی: نمی توان این موضوع را تمام شده دانست مگر اینکه توافق نهایی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122135" target="_blank">📅 21:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122134">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش آمریکا، ژنرال دن کین هم اکنون تو کاخ سفید حضور داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122134" target="_blank">📅 21:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122133">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شب قبل از حمله تقریباً تمام تیتر خبرها درباره توافق بود و حتی خود ترامپ هم از عالی پیش رفتن مذاکرات و نزدیک بودن توافق صحبت می‌کرد!
🔴
حالا باید دید این‌بار واقعاً توافقی در کار هست یا باز هم فقط بازی رسانه‌ایه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122133" target="_blank">📅 21:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122132">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اکسیوس : مقام آمریکایی که تو جریان مذاکره‌هاست به من گفته دولت ترامپ و ایران خیلی نزدیک شدن به یه توافق برای تموم کردن جنگ
🔴
گفته اختلاف‌های باقی‌مونده فقط سر «اینکه چند تا بند چطور نوشته بشه» هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/122132" target="_blank">📅 21:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122131">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
قطر: تماس امیر قطر با محمد بن سلمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122131" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122130">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / الحدث به نقل از یک منبع عالی‌رتبه: تنها ساعات کمی تا اعلام توافق بین آمریکا و ایران فاصله است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122130" target="_blank">📅 21:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122129">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4afc1b07c.mp4?token=qS0ZWk--tK0YuuBpqxloTv2-ZSXiD5xCcK10_RP-zpCOC632ftuA7408F6n0LW-Do_SBRMNoAlA_Pysw3d7-41079BfYDROrJbmqm2wr9e0AXvSiRh-mw8Sd_n2qO9Y5jK2zsBxoaDTjESE9W9w2PEqFjVugqm2G_JKXs_5pe25HdBrlaCW606xiBGGseQ1ggRzF0vI3dxO8T2xa1TSYjLaMMT5mTcH3vtgIIIAMo3DRnQvQVPIeGiGBkZ2hI7ySkizZg9RRN8NmXaUpZl3L-5P651dp-f4jFAe0TUC0dnkofY37FlHDM69ZVkAy-_izlFNVgcdwaJeexq9zLSgX7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4afc1b07c.mp4?token=qS0ZWk--tK0YuuBpqxloTv2-ZSXiD5xCcK10_RP-zpCOC632ftuA7408F6n0LW-Do_SBRMNoAlA_Pysw3d7-41079BfYDROrJbmqm2wr9e0AXvSiRh-mw8Sd_n2qO9Y5jK2zsBxoaDTjESE9W9w2PEqFjVugqm2G_JKXs_5pe25HdBrlaCW606xiBGGseQ1ggRzF0vI3dxO8T2xa1TSYjLaMMT5mTcH3vtgIIIAMo3DRnQvQVPIeGiGBkZ2hI7ySkizZg9RRN8NmXaUpZl3L-5P651dp-f4jFAe0TUC0dnkofY37FlHDM69ZVkAy-_izlFNVgcdwaJeexq9zLSgX7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتیجه همنشینی روبیو با ترامپ
😂
🔴
روبیو: ممکنه امروز بعدا خبری بشه الان خبری برات ندارم ولی ممکنه یه خبری باشه یکم دیگه امیدوارم که باشه ولی ممکنه هم نباشه، ولی هنوز مطمئن نیستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122129" target="_blank">📅 21:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122128">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ در مصاحبه با کانال ۱۲ اسرائیل: اگر توافقی برای اسرائیل خوب نباشد، آن را امضا نخواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122128" target="_blank">📅 21:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122127">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ce7c88a80.mp4?token=k7m8CaqfVA9IDDubaUI6EMSE89BxIDDi3wJQU8syxNYYyQfOq67uRdrF7ZR6e2LSjt5FsNY13_DJ3GNcpltoFgJV_1VI9Dk7V0vX0vR-j6SMO5Hjetv3PXZl-59tOt6ikkNJmH1SlTITo4zrV-G8hbhZiwosZpdZ2a-N0jWL8VK-g50quRGoGHk5zin9rFQSAO9wB_Q-4qbalSycWbXwVSYJiwY3M3d1XwL6GCG-0oU0h0HpvEYvnPVOTLNSrL8A1NMZ0kOT49m_m7yZkObaOSqSXDwea9TBy3MYQbkP9tXiPmtth8a9iTDGoRxVb2au4UyistogQ6gCBj7w5iUP5EnZM67tOoU7RABNVWHCNycbtlC41SCrOuFbHoAMMadDooGwuLsU1zGvp0jZqJNNw99PVfE0nsJQNW3NfCNj7wDloUspkzKHbVU6HEPXfh9NKkzepwLJGMfv8LEoTI2du9a0oCA5r22-vaUpH0a9ZxXdJ8Y-OBMs3kUmZCtXNEsRZj-jlFuz5Et81U3KSLhsZz40Kk7Cpvb7fhIEw0CVcUTAqbO7-6SmWnaVcvr5m0cffBCM0d_INW9HqnRq-nSa-IQRbpjuqaAa97oue6pmIJp_DBs0S4srUl4sasyYNd3tBattDOV8ftmJ_1VTivbvV96c07fyoyttoRV-X3yjECs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ce7c88a80.mp4?token=k7m8CaqfVA9IDDubaUI6EMSE89BxIDDi3wJQU8syxNYYyQfOq67uRdrF7ZR6e2LSjt5FsNY13_DJ3GNcpltoFgJV_1VI9Dk7V0vX0vR-j6SMO5Hjetv3PXZl-59tOt6ikkNJmH1SlTITo4zrV-G8hbhZiwosZpdZ2a-N0jWL8VK-g50quRGoGHk5zin9rFQSAO9wB_Q-4qbalSycWbXwVSYJiwY3M3d1XwL6GCG-0oU0h0HpvEYvnPVOTLNSrL8A1NMZ0kOT49m_m7yZkObaOSqSXDwea9TBy3MYQbkP9tXiPmtth8a9iTDGoRxVb2au4UyistogQ6gCBj7w5iUP5EnZM67tOoU7RABNVWHCNycbtlC41SCrOuFbHoAMMadDooGwuLsU1zGvp0jZqJNNw99PVfE0nsJQNW3NfCNj7wDloUspkzKHbVU6HEPXfh9NKkzepwLJGMfv8LEoTI2du9a0oCA5r22-vaUpH0a9ZxXdJ8Y-OBMs3kUmZCtXNEsRZj-jlFuz5Et81U3KSLhsZz40Kk7Cpvb7fhIEw0CVcUTAqbO7-6SmWnaVcvr5m0cffBCM0d_INW9HqnRq-nSa-IQRbpjuqaAa97oue6pmIJp_DBs0S4srUl4sasyYNd3tBattDOV8ftmJ_1VTivbvV96c07fyoyttoRV-X3yjECs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ پیتر هگستث
:
اولین حمله هوایی که هرگز انجام دادم و یک دسته را در وسط شب در بغداد رهبری کردم. ما ۳۶ ساعت برای آماده‌سازی داشتیم و من هر دقیقه از آن ۳۶ ساعت را صرف آماده‌سازی کردم.
🔴
وقتی خلبان‌ها ما را چند صد متر در نقطه اشتباهی در وسط یک زمین گل‌آلود فرود آوردند و GPS کار نمی‌کرد.
🔴
یک مرد بود که آن دسته به او نگاه می‌کردند و آن مرد من بودم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122127" target="_blank">📅 21:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122126">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ادعای سازمان رادیو و تلویزیون عبری: اسرائیل سطح آماده‌باش را کاهش داده و برآوردها حاکی از عدم وقوع حمله قریب‌الوقوع به ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122126" target="_blank">📅 21:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122125">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFoww2hwkoPcXupeOtw7mzN1EQMTc7MhNXmeczC2dXkPlu1PAc7URHqpDt3nMBa3OUVueNhqXL0oUiS2UM0_SYl9apQDSnQSfw5x1UrjA4sY-Sh4JfkriBdDugpS5MjPHspCzpxIEIW90x5kTYVAJblDBeEIjWdnBYZNFJNBuhEdPi9cqrsaZGaGuBvf57SON5DzSBfJ0vp5dt-tvxZ7Wt9xfbc4DZTRyhnu9B_uq_mF798m_0ZRd1gTRjQOM8NWnsLhz8cddN49F1pK7Ia7C1_P-ZvS2TKk6YuJ0Mh6MaGES8Moz_9h06c2Lcklcaw39CgjzwlRz8qy1cAt2GHAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122125" target="_blank">📅 21:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122124">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1XLJ-_zjp0f8oHbP_NUeZ4XkWROXQs9bQJugaJT4VR6z9sQUhC3j8hO-Tbxk4Cm4FKR3Ilanq_qUOUBwQFn15CQLaMxLE7QjpqNlFLhLkWiZZ8seqGHe1Ijtv-rz8HjU2AOk0TqbicnhGA1-svCjy8ppyvJIIklcFSe0vYRnxYvVG9k3t_E8v8PyApWGf5DLVRQCz34pQX8BkLeB-JjxlKswVfibnXD7L_FI3FywRTVS0UsRICm4v0tutK3xT1urh6tuD-pTfgkpRut6lU_TUDklheUWkaOii1iQ7vzsEv0SBRf-FGqiQl50v7jpDUeZ8gn4ILNTnbl3nNgHwIu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتظار می‌رود ایالات متحده و ایران تا بعدازظهر یکشنبه توافقنامه صلحی را اعلام کنند که هدف آن پایان دادن به درگیری‌ها در تمام جبهه‌ها است، طبق گزارش واشنگتن تایمز.
🔴
پیش‌نویس پیشنهادی اوایل شنبه نهایی شد و برای تأیید نهایی به رهبران هر دو کشور ارسال گردید.
🔴
شخصیت‌های کلیدی در تأیید این پیش‌نویس شامل محمدباقر قالیباف، رئیس مجلس ایران، معاون رئیس‌جمهور جی‌دی ونس، استیو ویتکاف و جارد کوشنر بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122124" target="_blank">📅 21:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122123">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
هشدارهای پهپاد در منطقه خط تقابل، شمال اسرائیل فعال هستند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122123" target="_blank">📅 21:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122122">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: اگر آتش‌بس به مدت ۶۰ روز تمدید شود، این گام کاملا مغایر با خواسته‌ها و اهداف اسرائیل خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122122" target="_blank">📅 20:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122121">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AabzgOicEW6KoWZWuUihkzf8sEsChcDRcBwrAdvbEIZLzCo5-wJ_HWz3ykO8fbclJW9Ese7UOhVBcQ8nxV9FQJIu0z-nxtTELPOpuyl_3-MGz_NAOPfMG75wPaR0SgnMrWQgCVjg6GghU5MSGcavZLTEdQwIoeBOyM6lDPynSqUg35gh0xTlvWW7Moov7MpSAYQtz6T3vlDpluANcMPs98doaOaDjpgJcklPmxz-Ue4UN2WnMY3OyRdCI2h88bqOy-B7DF-53l_Tp2ulo4wHg5uJCBRC5ZQjQVkqU4NNlzXOjSpXNi-CEmVI4u8X1RIzHNaVE4uhXz8YAacPirIRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای پهپاد در منطقه خط تقابل، شمال اسرائیل فعال هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122121" target="_blank">📅 20:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122120">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c1ceeaff3.mp4?token=SxC-8qeJpjxZP0YLSIDQPlUpjfQcpu8-qUP5DyyUdLvOLSVeMiJIgDBjZpfTlWAWCDE2S93ZdFLL83HSuvmYLiunSR8jm9aVTwRVWfsaCqsnE1__OSXHJNVExKvRnhS2e3E9RV1rxDzqWECSVj6gmJheeIaTuXRvQVT3kCgQRk4weMqGBx0-EG1ErkgN3hEb2ly7sOBPI_cfYuDTmuJQanSqVIJ9FVz3nRvWT3eUOknDibs6R4PjJ7Rfm6eY4naZPrJxCzUxL_KDd9FTWlKcO1roZwZYug3S1SWk61eYT4mM3dQrd8PMGRABQw-tCXJsQOgkWCy-PufkJAPQ9pBqIY3n1V1A8fIj_sfTe3HN4Gp_J5AMbFFntxQdydv-z19fu8W4yK64RNQntd1xJvxgDchcPLDysz8FTXwmk6aTsUFMY8gM9mblnE9UB79BbDt3-5mh_n5yjwpM2ldQnJOrAyxDdvTzjEFvp49emVNO0Ijz1Kfyv-M1TIghezc0A7xvVkTDFLO01e2h9LLd8mb7iFZsuNjyv1LDyPqSS-rqcMeajY6R5bdE5D0_lzHso28-QZ0gxEbsuZIEFVKNg74UavlY6OLACF2tlU_YGXCdaeo92JMZcBHUf9CWU5HX8nfILSJUL3IE1JlGrlZOuUPltTyi4PN9SMUsv2XBql2qGgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c1ceeaff3.mp4?token=SxC-8qeJpjxZP0YLSIDQPlUpjfQcpu8-qUP5DyyUdLvOLSVeMiJIgDBjZpfTlWAWCDE2S93ZdFLL83HSuvmYLiunSR8jm9aVTwRVWfsaCqsnE1__OSXHJNVExKvRnhS2e3E9RV1rxDzqWECSVj6gmJheeIaTuXRvQVT3kCgQRk4weMqGBx0-EG1ErkgN3hEb2ly7sOBPI_cfYuDTmuJQanSqVIJ9FVz3nRvWT3eUOknDibs6R4PjJ7Rfm6eY4naZPrJxCzUxL_KDd9FTWlKcO1roZwZYug3S1SWk61eYT4mM3dQrd8PMGRABQw-tCXJsQOgkWCy-PufkJAPQ9pBqIY3n1V1A8fIj_sfTe3HN4Gp_J5AMbFFntxQdydv-z19fu8W4yK64RNQntd1xJvxgDchcPLDysz8FTXwmk6aTsUFMY8gM9mblnE9UB79BbDt3-5mh_n5yjwpM2ldQnJOrAyxDdvTzjEFvp49emVNO0Ijz1Kfyv-M1TIghezc0A7xvVkTDFLO01e2h9LLd8mb7iFZsuNjyv1LDyPqSS-rqcMeajY6R5bdE5D0_lzHso28-QZ0gxEbsuZIEFVKNg74UavlY6OLACF2tlU_YGXCdaeo92JMZcBHUf9CWU5HX8nfILSJUL3IE1JlGrlZOuUPltTyi4PN9SMUsv2XBql2qGgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس معاون اول رئیس‌جمهور آمریکا سفرهای خود را نیمه‌تمام گذاشته و به طور اضطراری به کاخ سفید بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122120" target="_blank">📅 20:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122119">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
لیندری گراهام، سناتور ارشد جمهوری‌خواه و دوست نزدیک دونالد ترامپ، به آکسیوس گفت که رهبران منطقه در توصیه‌های خود به دونالد ترامپ اختلاف نظر دارند و برخی از او برای ضربه زدن به ایران برای تضعیف دولتش و دستیابی به توافقی بهتر فشار می‌آورند، در حالی که برخی دیگر به همراه برخی از مشاوران ارشد کاخ سفید از او خواستند که پیشنهاد فعلی را بپذیرد.
🔴
گروه اخیر استدلال کردند که ایران توانایی تخریب زیرساخت های نفتی مهم خلیج فارس را در صورت حمله حفظ می کند و امنیت تنگه هرمز را نمی توان در برابر نفوذ ایران تضمین کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/122119" target="_blank">📅 20:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122118">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkM7xS6_b2kl2HMoZsdlC2xm6e8vqGBHnkH5CrFs-jUG8V-Y31k0OFpftdUWZeb4FS9f-4muWfvnBn32518NfiJsNFMQruwqdbnMRwLjBON2WkihQZRIlcjDJxX44PIC_54Q-pxar8gh4Y8-gE1jEryHHjC36bDfPwbDTp_8cuC6Z5-Qt3rijK2km5OXxtFjXkzqXCQLXfkCGvRNzDy17jkt8rJ3go7Ofe4Kubl04cKuRnkYR8-5ZevnnkfJ_gfM2Aq2GpfIbi-_ZLEXBc2caHao_w6Nj-T8P0f_qJBqWtGd_xIPWrlF9bTrfoM0Ed8emJ7fyMc1wyWn_1UbL4IDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازنشر می‌کند:
تسلط پرزیدنت ترامپ بر بهشت برای آمریکا خوب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122118" target="_blank">📅 20:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122117">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg-ivsZNZ6hl6nvoTJctEgWDsoqfLtnOYnV_7Mxf1dN-Cl0qgUSqjJ2cthZLfLQ_9n-KvAobTylGb9qn1eo2w7oOSgrSt9wSZjzhTZD2CrGVuNrRvgcZhx-ZyJ7LUvnuQ21DWJ4_uDQ3AYv4hfrFuct511jzuWc1n6e-3T9SpmWi1E8brUAJw1UlNw9hD55G2UEh9AGKopDT25sG4w5WtmO5lr5YhAYFbaPOoUc26K85fWZPBRqhQir2KN4GOox0h3w5ku041hxwQ5AxHdGnEraHyKhrjXiQdsfk5vu1Qhd1fAOmkSh509CSY4ldkEnDlyK1RIocbwLAEHT32bzn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزيدنت
ترامپ از اردوغان تشکر کرد که او را رهبر جهان قرن‌ها منتظر خوانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122117" target="_blank">📅 20:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122116">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر با وزیر خارجه بریتانیا در مورد تلاش‌های حمایت از میانجی‌گری پاکستان گفت‌وگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122116" target="_blank">📅 20:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122115">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
منبعی عالی‌رتبه به العربیه: نشانه‌ها درباره توافق بین آمریکا و ایران بسیار مثبت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122115" target="_blank">📅 20:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122114">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آکسیوس: دونالد ترامپ گفته است که فکر نمی‌کند بنیامین نتانیاهو نگران یک توافق احتمالی میان آمریکا و ایران باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122114" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سفارت ایالات متحده در کی‌یف هشدار داد که ممکن است در ۲۴ ساعت آینده یک حمله بزرگ‌مقیاس رخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122113" target="_blank">📅 20:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خبرنگار کانال ۱۵، یوسی یهوشوا، می‌گوید احتمال درگیری مجدد با ایران بالا است مگر اینکه یکی از طرفین انعطاف نشان دهد؛ او نسبت به گزارش‌های مربوط به یک پیشرفت بزرگ شکاک است و با توجه به حجم شایعات در ساعات اخیر، به احتیاط فراخوانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122112" target="_blank">📅 20:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: استیو ویتکوف، نماینده آمریکا، در تلاش است تا به هر قیمتی به یک توافق دست یابد و بر رئیس‌جمهور ترامپ فشار می‌آورد که به جنگ با ایران بازنگردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122111" target="_blank">📅 20:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
گویا چندتا از هواپیماهای ترابری امریکا دارن از خاورمیانه می
ر
ن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122110" target="_blank">📅 20:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام امنیتی پاکستانی: یک یادداشت تفاهم (MOU) در حال نهایی‌سازی برای پایان دادن به جنگ آمریکا و ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122109" target="_blank">📅 20:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ادعای کانال ۱۳ اسرائیل: اسرائیل اطلاعاتی دریافت کرده که توافق [آمریکا] با ایران ممکن شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122108" target="_blank">📅 20:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122107">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
صدای انفجار در استان سلیمانیه، شمال عراق، شنیده و پس از آن ستون‌هایی از دود در این منطقه مشاهده شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122107" target="_blank">📅 20:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122106">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
آکسیوس: ترامپ امشب علاوه بر کشورهای عربی با اسرائیل هم در رابطه با پیش‌نویس توافق گفتگو خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122106" target="_blank">📅 20:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122105">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
لیبرمن وزیر دفاع اسبق دفاع و خارجه اسرائیل: هر توافق [آمریکا] با ایران برای ما فاجعه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122105" target="_blank">📅 20:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه  ایران و عربستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122104" target="_blank">📅 20:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
معاون رئیس‌جمهور ایالات متحده، جی‌دی ونس، به طور غیرمنتظره‌ای از سینسیناتی به واشنگتن دی‌سی بازگشته است و کاروان او در حال حرکت سریع به سمت کاخ سفید دیده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122103" target="_blank">📅 20:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری/  وزیر جنگ آمریکا: ما از نیروهای هوابرد و واکنش سریع خود خواسته‌ایم که در هر لحظه‌ای آماده اعزام به خاورمیانه باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122102" target="_blank">📅 20:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
آکسیوس، به نقل از مقامات اسرائیلی: نتانیاهو عمیقاً نگران توافقی است که در حال حاضر مورد بحث است
🔴
به نقل از مقامات اسرائیلی: نتانیاهو از ترامپ خواسته دور جدیدی از حملات علیه ایران را آغاز کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/122101" target="_blank">📅 20:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع آگاه: بن‌بست در مذاکرات بین واشنگتن و تهران پایان یافته است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122100" target="_blank">📅 20:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل اعلام کرد که تل آویو به دقت پیش‌نویس توافق ایالات متحده و ایران را رصد می‌کند.
🔴
تل آویو نگران است که تهران بدون حل مسائل هسته‌ای بتواند از کاهش تحریم‌ها بهره‌مند شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122099" target="_blank">📅 20:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
قطر: در تماس تلفنی میان امیر قطر و رئیس کشور امارات تلاش‌های انجام شده برای تقویت راهکارهای سیاسی مورد بحث قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122098" target="_blank">📅 20:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122097">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع آگاه: بن‌بست در مذاکرات بین واشنگتن و تهران پایان یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122097" target="_blank">📅 20:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آسوشیتدپرس به نقل از مقامات: امیدواریم ظرف ۴۸ ساعت تصمیم نهایی در مورد یادداشت تفاهم ایران-آمریکا را بگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122096" target="_blank">📅 20:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس به نقل از مقامات: واشنگتن و تهران به توافق بر سر یادداشت تفاهمی برای پایان دادن به جنگ نزدیک شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122095" target="_blank">📅 20:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبرنگار الجزیره: دو حمله هوایی اسرائیل به شهرهای مفدون و کفار در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122094" target="_blank">📅 20:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع: خوش‌بینی محتاطانه نسبت به مذاکرات بین آمریکا و ایران وجود دارد و امور در مسیر مثبتی در حال حرکت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/122093" target="_blank">📅 20:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : نتانیاهو امشب با رهبران ائتلاف دولتیش یه جلسه برگزار می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/122092" target="_blank">📅 20:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فارس: یک منبع آگاه و نزدیک به تیم مذاکره‌کننده: آمریکایی‌ها اگرچه از رویکردهای اولیه خود عقب‌نشینی کرده‌اند اما همچنان ۳ موضوع اختلافی پابرجاست که اگر حل نشوند مذاکره انجام نخواهد شد.
🔴
اول: موضوع هسته‌ای ، ایران اعلام کرده که در این دوره وارد مذاکره درباره موضوع هسته‌ای نمی‌شود.
🔴
دوم: پول‌های بلوکه‌شده ، پول‌‌های بلوکه‌شده باید واریز شود
🔴
سوم؛ کنترل ایران بر تنگۀ هرمز؛ کشتی‌ها باید تحت مدیریت ایران و دقیقاً از مسیری که ایران تعیین می‌کند عبور کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/122091" target="_blank">📅 20:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
آکسیوس به نقل از منابع: تماس تلفنی بین ترامپ و رهبران کشورهای عربی در مورد پیش نویس توافق با ایران ساعت ۵ بعد از ظهر به وقت گرینویچ انجام خواهد شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122090" target="_blank">📅 19:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122089">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3eYaaHFfW6I_nWVYiJWBSIOEsq0EquTJLOWcqrmtj68RR4hu9c9GysvOHiPSNGuGPNrrrad-wnasq9X3EX8CafpIZqqoiEySvW9coXbAatq-TkEIjBI-99g5dMQbmHsnKJxzUmleHFNzbTHuRzCI0bjdyOnrJxwWOTDGPce1-w5EQd0qeTej_LsBgAapiX0iuxFdvb9P_h-n2agRI85meF7v2Bjc-ZsxW5ghfK28-_r7_5l8b-1A_EC3mTAZwFoAzp2CqY2f5KrbbYLdzKTO3_XtDEoiDZaXB4tqy6rv1tnvIxCtPHMRYsQIByKcmJZ9ww8xkrxx42_gAItL9lYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی کارکنان غربی صنعت کشتیرانی در دبی به دلیل جنگ آمریکا و اسرائیل علیه ایران، قصد ترک امارات و نقل مکان به یونان یا قبرس را دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122089" target="_blank">📅 19:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122088">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / یک منبع نزدیک به تیم مذاکره‌کننده به خبرگزاری فارس گفت که مذاکرات بین ایران و آمریکا ممکن است فروپاشی کند، مگر اینکه واشنگتن انعطاف‌پذیری بیشتری نشان دهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/122088" target="_blank">📅 19:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122087">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آکسیوس به نقل از منابع: تماس تلفنی بین ترامپ و رهبران کشورهای عربی در مورد پیش نویس توافق با ایران ساعت ۵ بعد از ظهر به وقت گرینویچ انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/122087" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122086">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ به کانال ۱۲ اسرائیل: اگر برای اسرائیل خوب نبود، معامله‌ای انجام نمی‌دادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/122086" target="_blank">📅 19:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122085">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سی‌بی‌اس، به نقل از منابع: دولت ترامپ علی‌رغم تلاش‌های دیپلماتیک مداوم، در حال آماده شدن برای حملات نظامی جدید علیه ایران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122085" target="_blank">📅 19:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122084">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری / سی‌بی‌اس نیوز به نقل از منابع:  ترامپ در حال بررسی سازوکاری برای بازگشایی تنگه هرمز، آزادسازی بخشی از دارایی‌های مسدود شده ایران و ادامه مذاکرات است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/122084" target="_blank">📅 19:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122083">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری / سی‌بی‌اس نیوز به نقل از منابع:
ترامپ در حال بررسی سازوکاری برای بازگشایی تنگه هرمز، آزادسازی بخشی از دارایی‌های مسدود شده ایران و ادامه مذاکرات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/122083" target="_blank">📅 19:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122082">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ گفت که معتقد است توافق نهایی ایران را از دستیابی به سلاح هسته‌ای بازخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/122082" target="_blank">📅 19:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122081">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ در گفت‌و‌گو با سی‌بی‌اس نیوز درمورد جزییات توافق احتمالی: «نمی توانم قبل از اینکه به آنها بگویم، به شما بگویم، درست است؟»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/122081" target="_blank">📅 19:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122080">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKydTeUmhFiXR3_DBH8Dy5BHUH_m8kbr6cwoU4J7Yx1GalRyb9iJymWFsyqxg803iA4usRUmw5lX_KsVSDWfFi_IgWUgT2udV5e1XxFAwWCMv99GcY5M33xDLvTSlxZ_dYgeaGxuMa76NoFzEtd9eCZhu6E5K8-OIxr2FfFLTcmPYokfUlbGmA9JG275HifM9wwXARdQBthpm0V06-HqNlwOVuVdh4rU9pyMvr5d51k6gS_psv3c_W6vtnpifBIqKPR2bXXnFQsnVOXpfvJA8ae_XhN1VfOCtx4f0R9JeZtMV-N0UM4Sv764t9eY1WfKRIrUxfELGABebixAZM-rqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
تصویر مزار جاویدنام عرفان کیانی که جز ویدیوی اعتراف اجباری هیچ تصویری ازش منتشر نشده بود.
🔴
باغ رضوان اصفهان، قطعه ۸۶، بوستان۱، ردیف ۱، شماره ۳۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/122080" target="_blank">📅 19:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122079">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سی‌بی‌اس‌ به نقل از یک منبع: ترامپ هنوز در حال بررسی پیشنهادهاست و تصمیم نهایی خود را نگرفته است
🔴
او با مشاوران خود مشورت کرده و با رهبران خارجی از جمله رهبران عربستان سعودی و دیگر کشورهای حوزه خلیج فارس گفتگو می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/122079" target="_blank">📅 19:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122078">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری/ترامپ به سی بی اس: هر روز اوضاع بهتر و بهتر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/122078" target="_blank">📅 19:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122077">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ، در گفت‌وگو با سی‌بی‌اس نیوز:
مذاکره‌کنندگان ایالات متحده و ایران «
بسیار به نهایی کردن یک توافق
» برای پایان دادن به جنگ بین دو کشور نزدیک‌تر شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/122077" target="_blank">📅 19:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122076">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
الشرق نیوز سعودی به نقل از منابع منطقه‌ای:
🔴
قرار است دونالد ترامپ، امروز ساعت ۱۳:۰۰ به وقت شرقی با رهبران پاکستان، امارات، عربستان سعودی، قطر، اردن، ترکیه و مصر تماس تلفنی داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122076" target="_blank">📅 19:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122075">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ به آکسیوس: برخی ترجیح میدهند توافق را منعقد کنند ، برخی دیگر ترجیح میدهند جنگ را از سر بگیرند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/122075" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122074">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ به آکسیوس: تنها توافقی را در رابطه با غنی سازی اورانیوم و سرنوشت ذخایر آن است را میپذیرم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/122074" target="_blank">📅 19:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122073">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری/آکسیوس : ترامپ گفت احتمال اینکه به ایران حمله کنه و یا توافق بشه 50/50 هست همچنین ترامپ شنبه با استیو ویتکوف و جرد کوشنر دیدار میکند تا آخرین پیشنهاد ایران را بررسی کند و انتظار میرود تا یکشنبه تصمیم‌ گیری شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122073" target="_blank">📅 19:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122072">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/آکسیوس :
ترامپ گفت احتمال اینکه به ایران حمله کنه و یا توافق بشه 50/50 هست
همچنین ترامپ شنبه با استیو ویتکوف و جرد کوشنر دیدار میکند تا آخرین پیشنهاد ایران را بررسی کند و انتظار میرود تا یکشنبه تصمیم‌ گیری شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122072" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122071">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
العربیه: ایران پیشنهاد تعلیق غنی‌سازی اورانیوم بالای ۳.۶ درصد را به مدت ۱۰ سال ارائه داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/122071" target="_blank">📅 19:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122070">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
العربیه: ایران پیشنهاد تعلیق غنی‌سازی اورانیوم بالای ۳.۶ درصد را به مدت ۱۰ سال ارائه داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122070" target="_blank">📅 18:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122069">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از یک دیپلمات مطلع از مذاکرات: به نظر می‌رسد توافق در مسیر درستی پیش می‌رود. اکنون توافق برای بررسی دست آمریکایی‌هاست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122069" target="_blank">📅 18:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122068">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a779c321.mp4?token=s0zfkTUKRjbDRL4xYdGP1dx5FDQnq8P_3nipQCd1DN41Bii5feNs2DTkhinJ4WWcieW6jRjlaw1Z3MldeOeTMmBPMYg4kfHVwokNAPax78X_4bS8VtIWiVOKXRUQYzCV5vP_PvwWuS7NbKAALkPPvv8m0ktALOHni6frFyUenFtVAWVGCTM5mevr6vPBAVutKxRF6tiJiQL3GYhtoCybH6Fc9GxteXTHHWve01wMgM4PtS8nh5cY-Fn3TW_9C_sdZhPbTDXe2HadDFabT0Hj4wLGXPtxP6lN1YmLtmizppvssXyr6CegAo7rzoAjWltGWqpr58vQqjsIqCTyUVY8MpwkoZHXJnKJrex2bWHBjc-W1U3-17mr8H1c0AU4pKcfPxuXKoWBK06bHd1rDp-Qsrw5pCqE61vVux2v_KItW9-8VVCHbHRft9gRvQTHv6jGU7gOXKAlRD4QJ_mEroiwzLLXQjCO75Jdqd2oYiPrqmqtxUIMJu6dsVMVUZZefu7oc4-L-QBnaTHHG7K23ptRZRf-B6WNlVP3HsTJuUO2k3OgFKBZyreyigpl1EmcoXSDXPDhEbHj6rMe5kCIWlmRnGkcYPTdGjRybAdxtaz-BL2qfBsVWs9kvkTYk-DZHDoH8wtD2ZB4XZc7DN9ewfAIKJSiHUbp6Oyn8DeF2tUQ2oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a779c321.mp4?token=s0zfkTUKRjbDRL4xYdGP1dx5FDQnq8P_3nipQCd1DN41Bii5feNs2DTkhinJ4WWcieW6jRjlaw1Z3MldeOeTMmBPMYg4kfHVwokNAPax78X_4bS8VtIWiVOKXRUQYzCV5vP_PvwWuS7NbKAALkPPvv8m0ktALOHni6frFyUenFtVAWVGCTM5mevr6vPBAVutKxRF6tiJiQL3GYhtoCybH6Fc9GxteXTHHWve01wMgM4PtS8nh5cY-Fn3TW_9C_sdZhPbTDXe2HadDFabT0Hj4wLGXPtxP6lN1YmLtmizppvssXyr6CegAo7rzoAjWltGWqpr58vQqjsIqCTyUVY8MpwkoZHXJnKJrex2bWHBjc-W1U3-17mr8H1c0AU4pKcfPxuXKoWBK06bHd1rDp-Qsrw5pCqE61vVux2v_KItW9-8VVCHbHRft9gRvQTHv6jGU7gOXKAlRD4QJ_mEroiwzLLXQjCO75Jdqd2oYiPrqmqtxUIMJu6dsVMVUZZefu7oc4-L-QBnaTHHG7K23ptRZRf-B6WNlVP3HsTJuUO2k3OgFKBZyreyigpl1EmcoXSDXPDhEbHj6rMe5kCIWlmRnGkcYPTdGjRybAdxtaz-BL2qfBsVWs9kvkTYk-DZHDoH8wtD2ZB4XZc7DN9ewfAIKJSiHUbp6Oyn8DeF2tUQ2oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست : میدونم ارتش عاشق غرق کردن نیروی دریاییه
- و فعلا تنها نیروی دریایی که اجازه دارید غرقش کنید نیروی دریایی "ایرانه"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122068" target="_blank">📅 18:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122067">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PazF_vzAMN-ogRAYmrc3wAyff_4Fly_4rISYUaBOfDSKO9wDTbsqHTPVS3gfxHesYWiMuKDLdYoxWWtcdpnrdV5hzhc_5Zp4eZr7MGtFJAGINJmOq2VMRBBlXNuojHSImjM_4SV05eL7i3T7PGm808tnQZSAYEaQ-uaIL9nCbY9oGO7IaKsjZaEWfSDNBrKLix3Bjdz06QQ_5rZ4MCp9XiCusc57GJcfnqvmyYT5o13ywKzY5H2UFcqXhTacebONPmFmyYLcBjx1vIzM8nQbVtcZvyt5YCboP303pf8IIURgTxZlvTEMDqnTWz_GHUrdJ78iEDOzoTLces07zC_mUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجری صدا و سیما آرپی‌جی آورده تو برنامه، انگار قسمت سربازی برره‌اس :)))
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122067" target="_blank">📅 18:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122066">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس به نقل از مقامات پاکستانی گزارش داد:
🔴
اسلام آباد به تلاش‌های خود برای ترتیب دادن دور دوم مذاکرات مستقیم بین تهران و واشنگتن ادامه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122066" target="_blank">📅 18:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122065">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
طی ۲۴ساعت گذشته بولشویک‌ها حملات شدیدی علیه پزشکیان انجام دادن و طبق شنیده‌ها دنبال استعفای رئیس جمهور هستن تا گزینه مد نظر خودشون(زنبیل به دست) رو بیارن بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122065" target="_blank">📅 18:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122064">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ارتش پاکستان
: مذاکراتی که در ۲۴ ساعت گذشته انجام شد،
به پیشرفت امیدوارکننده‌ای به سوی تفاهم
نهایی منجر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/122064" target="_blank">📅 18:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122063">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الحدث:ایران دو مسیر برای مذاکرات پیشنهاد کرده که با اعلام پایان جنگ و محاصره آغاز می‌شود.
🔴
ایران تأکید کرده است که در متن یادداشت تفاهم، به عدم تولید سلاح هسته‌ای متعهد خواهد بود.
🔴
ایران خواستار حفظ حق غنی‌سازی در هر توافقی شده است
🔴
ایران پیش از مذاکرات هسته‌ای خواستار آزادسازی دارایی‌های بلوکه‌شدهٔ خود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/122063" target="_blank">📅 18:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122062">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fd66f216.mp4?token=s6yTswWGgze4sshJDzG8_BYXSN9W4mqGXer2_LJ0C7j203mNhERwTgxtvGmjjIuhlM0gmajr8jAPBK2XAkUuE3RL1ZW3Jew4zQYtuNCvUwc6pHzAlHTufcomn-gI8trMyaaoxVoKYBtmJzuqhuyqvHVJxsE0hYhq8Dzzb8QxR9y2gjcmCv3qTl2-Xu_y7-hVxEzR4Im283J4Qh5id30aatgFb-TRkUUSGCs4nNFwLlKjUS4s_KvacqSo8hElZ-R9A4hUyD5wYmzoWtbzEIAe0cvdTTmn7F2Ruhnp6qsGGtqrfw7dSIgiRwkj4aCFLIG2dFFEgEgu7_7Po-okBJV0yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fd66f216.mp4?token=s6yTswWGgze4sshJDzG8_BYXSN9W4mqGXer2_LJ0C7j203mNhERwTgxtvGmjjIuhlM0gmajr8jAPBK2XAkUuE3RL1ZW3Jew4zQYtuNCvUwc6pHzAlHTufcomn-gI8trMyaaoxVoKYBtmJzuqhuyqvHVJxsE0hYhq8Dzzb8QxR9y2gjcmCv3qTl2-Xu_y7-hVxEzR4Im283J4Qh5id30aatgFb-TRkUUSGCs4nNFwLlKjUS4s_KvacqSo8hElZ-R9A4hUyD5wYmzoWtbzEIAe0cvdTTmn7F2Ruhnp6qsGGtqrfw7dSIgiRwkj4aCFLIG2dFFEgEgu7_7Po-okBJV0yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی شما/سلام ادمین ماهم تجمع کردیم جلوی اداره آموزش پرورش لرستان و اینجا هم امتحانا مجازی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122062" target="_blank">📅 17:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122059">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7394b357e.mp4?token=YgQc6GOrjQKA0XIIZn-UCzw8onaQVI8YFFxQJI3uFA5o1-rv8PfR6d8ey-Cm3Y63s-Vkd-B_IHDYCmyaI4QF2KEPxMdURSQq7dxC2cECQh2YVe4d3wiR4Q2aHDRA8_WlVK7QcXYtgdjcQHFFidFVVCB_8y15_UuIbRcCuj8duFEBq_t7wGkTFwWU4Cp6290RKP7s6weg2RDXADnqZjgWthyz1WKCda6UkPh7P1EriiJKICJwhkipAkF3ZPjwqOG323SnAzJEGupIKJG7KXwsS38GkASy5AErG4i58jL5pH-xiHeHogmFU3uG9rZA553bStHzYJk83bw3f_1X3n0hDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7394b357e.mp4?token=YgQc6GOrjQKA0XIIZn-UCzw8onaQVI8YFFxQJI3uFA5o1-rv8PfR6d8ey-Cm3Y63s-Vkd-B_IHDYCmyaI4QF2KEPxMdURSQq7dxC2cECQh2YVe4d3wiR4Q2aHDRA8_WlVK7QcXYtgdjcQHFFidFVVCB_8y15_UuIbRcCuj8duFEBq_t7wGkTFwWU4Cp6290RKP7s6weg2RDXADnqZjgWthyz1WKCda6UkPh7P1EriiJKICJwhkipAkF3ZPjwqOG323SnAzJEGupIKJG7KXwsS38GkASy5AErG4i58jL5pH-xiHeHogmFU3uG9rZA553bStHzYJk83bw3f_1X3n0hDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جدیدا دانش آموزان استان‌هایی که امتحانات‌شون حضوریه، می‌ریزن جلو آموزش و پرورش منطقه و میگن ما فقط مجازی امتحان میدیم؛
🔴
اتفاقا جواب هم داده و تا الان این استان‌ها مجازی شده :
- یزد
- مرکزی
- گیلان
- کهگیلویه و بویراحمد
- کرمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/122059" target="_blank">📅 17:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122058">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
منبعی به من گفت که فرمانده ارتش پاکستان قرار بود یادداشت تفاهمی بین ایران و آمریکا را از تهران اعلام کند، اما
برای تکمیل هماهنگی‌ها با ترامپ
، تهران را ترک کرد.
🔴
منبع تأیید کرد که پرونده جنگ با تمام جزئیات آن مرحله اول را تشکیل می‌دهد و آنچه به مسائل هسته‌ای و تحریم‌ها مرتبط است، به پس از ۳۰ روز از توافق موکول می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/122058" target="_blank">📅 17:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122057">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا: تنگه هرمز باید باز شود؛ ایران نباید سلاح هسته ای داشته باشد؛
🔴
ایران باید ذخایر اورانیوم غنی شده خود را تحویل دهد؛ معضل غنی‌سازی ایران باید در مذاکرات در نظر گرفته شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/122057" target="_blank">📅 17:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122056">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c565cc9c05.mp4?token=gt-EF7bEjwOSPqD9LcBF0u76e8ii96ZFEVxMHuAUET6csbgKhq0H8398DO2oeWcnoGPntSqgTgd5ovbs-z1AC8Ad-6ASxT7aTV-BT0v8im3Iz8gvcOBl_Tmeezih7dp03zSQkDKsUyk9wUwAmaKPbHe934F7y28pKJ0SXbluKeLVx1ZyjzKo1UGv1Flb4m4E99rZ_mGeNcvMSN5ZNckp4b83_1T4URPLqt21gUkpLJ8kNtY_YmErzAgGw2yS0QtUCS92yWlVMopAfQF78YBN7emIPLzkv6Ee6rYOP3UcxOjNQbI6r-3157dqNKaAtlzNh2EzRsa2QRln6FURsoCo2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c565cc9c05.mp4?token=gt-EF7bEjwOSPqD9LcBF0u76e8ii96ZFEVxMHuAUET6csbgKhq0H8398DO2oeWcnoGPntSqgTgd5ovbs-z1AC8Ad-6ASxT7aTV-BT0v8im3Iz8gvcOBl_Tmeezih7dp03zSQkDKsUyk9wUwAmaKPbHe934F7y28pKJ0SXbluKeLVx1ZyjzKo1UGv1Flb4m4E99rZ_mGeNcvMSN5ZNckp4b83_1T4URPLqt21gUkpLJ8kNtY_YmErzAgGw2yS0QtUCS92yWlVMopAfQF78YBN7emIPLzkv6Ee6rYOP3UcxOjNQbI6r-3157dqNKaAtlzNh2EzRsa2QRln6FURsoCo2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو : شاید امروز یا چند روز دیگه درباره ایران خبرای جدیدی بیاد یه پیشرفت‌هایی شده
- ولی ایران نباید سلاح هسته‌ای داشته باشه و ترامپ میخواد قضیه دیپلماتیک حل بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/122056" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122055">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری / روبیو: فرصتی برای پذیرش توافق توسط ایران در نزدیک‌ترین زمان وجود دارد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122055" target="_blank">📅 17:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122054">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/122054" target="_blank">📅 17:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122053">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrCrdTGh4exDQoryZ4QmpBVOY8zMlf3WRGWsGNzJYlDcr3lhyWzx3CAnSVJB_iJYl_j2XO66PL_O_azBPagP6gAoZ8xFrCdM7pwn_RYwheBuEtZmFnXGoSuwPUJAiHFSEtlad-H_4gdOrGfFkNvRCi_5f9JDJQl4TmmpEmpGfKnGOYC_G_BSTQTd6Fd3Ex8FYSOX_iL5yMMwTNNxA5dTFgbj7OEB4wRfJ8aguxVPKGg_topx69ab84dyKFrhS12uPQ9ntm7n6v2NNafWb-REuWkhgzxf7wxsieG4XL2MiD66lbKfpUEOlxWijN9oiB1Q75fsYzWHxrq2MgPtrSc1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122053" target="_blank">📅 17:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122052">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تفاهم‌نامه چهارده بندی هم موضوع هسته‌ای مورد اشاره قرار  می‌گیرد و هم موضوع آزادسازی اموال بلوکه‌شده.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122052" target="_blank">📅 17:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122051">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / روبیو: فرصتی برای پذیرش توافق توسط ایران در نزدیک‌ترین زمان وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122051" target="_blank">📅 17:13 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
