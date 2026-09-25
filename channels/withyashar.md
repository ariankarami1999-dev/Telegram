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
<img src="https://cdn4.telesco.pe/file/fthqcpi9im6uJnsfx2w_IFLZI81MX7W9Zh8ziO3YNfyFPLhz50AWCOSx_hOuWn5Z-BD_1oNIYg954EgctOWUtWC0XRv56QVowvCcuzcOtzA2hGzNuR5ma6jzc-7cYa1RvjySOdqnsJ4Z6zLHJOps6DGUz_l-mt_jU3jisV52qZMg6MPLeuqzJDinzeHJJSYklaF0YN3N-eOsfwuOjvgLWJD6JXI_wqVEBJz_SBkxFE_CClDppJpjuMLWCZoeOAHJtDLLeZaoFvdwaa-OXU57IvQ_ZaAqEKO2-bYEZm3mYosELa3vYwBoARqsR1XX5hpGSLZTaER7KXNJjG0A3OOzcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 466K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">در‌ حدود ۱۰ دقیقه تنگه ۳ بار صدای ناله اپراتورهای لانچر که کتلت شده اومد
@WarRoom</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/withyashar/24137" target="_blank">📅 14:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سی‌ان‌ان به نقل از منابع: تصاویر ماهواره‌ای و اطلاعاتی که از سوی گروه‌های چینی ارائه شده است، به ایران کمک کرده تا کشتی‌ها را در تنگه هرمز تهدید کند و حملات دقیقی را به پایگاه‌های نظامی آمریکا در خاورمیانه انجام دهد. این بخشی از بهبود چشمگیر توانایی‌های هدف‌گیری ایران در چند ماه گذشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/withyashar/24136" target="_blank">📅 14:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیروهای دولتی یمن: در یک حمله سریع ما به قله کوه نمان و منطقه دار الکافر تسلط یافتیم.
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/24135" target="_blank">📅 14:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">3 رسانه‌ به کاخ سفید بازمی‌گردند
پس از آن‌که دونالد ترامپ دسترسی خبرنگاران سی‌ان‌ان، MS Now و پولیتیکو به کاخ سفید را لغو کرده بود، یک قاضی فدرال دستور داد این محدودیت برای
14 روز متوقف
و مجوزهای خبرنگاران فوراً بازگردانده شود.ترامپ پیش‌تر مدعی شده بود پوشش این رسانه‌ها «دروغ» و تهدیدی برای امنیت ملی است، اما قاضی گفت شواهد کافی برای اثبات این ادعا ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/24134" target="_blank">📅 14:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز: فرودگاه‌های اربیل و سلیمانیه در عراق نیز از روز جمعه، پذیرش پروازهای هوایی از ایران را متوقف خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/24133" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۴ ریشتر در عمق ۸ کیلومتری، سفیددشت اصفهان را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/24132" target="_blank">📅 13:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e7fd7acc.mp4?token=fODAL_gbuRMNJxbt4WWCe6JgIaobV2dCS6R9eOspK6D2HaL0asTH4yxEqE6jQiCGJaJp-kc8TKuDVe0b6nOglTBFawXkjmYk13whjhxIkXJCP6Rw4cfEXtMFNnykqGuhu6D5k1uf-1piPoOqSKUVVUM-YK2_OFwmG0pk8LrBOVjt5jL1i88g4ayaIcdZQ5bZAwOrZewxQOFoKt44W48qU7Fhv39MsPQIqS5tmuvu2IF-DRR0wYBMgObgH4wPy4JfBEI0_ZRNezEsuVWRZewGO8lsba0C-3LQKRcphDM-gERoj1w75FoZg43yrj2Q6B2ZhkBGded5e_R1mnZBEaFkGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e7fd7acc.mp4?token=fODAL_gbuRMNJxbt4WWCe6JgIaobV2dCS6R9eOspK6D2HaL0asTH4yxEqE6jQiCGJaJp-kc8TKuDVe0b6nOglTBFawXkjmYk13whjhxIkXJCP6Rw4cfEXtMFNnykqGuhu6D5k1uf-1piPoOqSKUVVUM-YK2_OFwmG0pk8LrBOVjt5jL1i88g4ayaIcdZQ5bZAwOrZewxQOFoKt44W48qU7Fhv39MsPQIqS5tmuvu2IF-DRR0wYBMgObgH4wPy4JfBEI0_ZRNezEsuVWRZewGO8lsba0C-3LQKRcphDM-gERoj1w75FoZg43yrj2Q6B2ZhkBGded5e_R1mnZBEaFkGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیپلمات اسرائیلی نام تمام کشورهایی که جلسه را ترک کردند یاداشت کرد تا بعد به خدمتشان برسند.
@WarRoom</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/24131" target="_blank">📅 13:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زلنسکی، رئیس‌جمهور اوکراین:
«طرف آمریکایی پیشنهاد برگزاری
نشست سه‌جانبه در امارات متحده عربی
را مطرح کرده است.
ما منتظر پیشنهاد آمریکا درباره
تاریخ برگزاری این نشست
هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/24130" target="_blank">📅 12:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01aa2ba27b.mp4?token=uv0SU_UHHAZXIezFS1PD3VodZ7xVuiYxl-Dhkjehem0G8BdYvdDP2KVLVWpZtxUJyyEi0a5Y9W6fR5wAsoxjjmjwzqydqD2sOuODDtmIqxABSVTEZLZmit9Hl-Kn-spIn6QATaiMICyVKEo_NLOSGQiL84I8xgnpfBfFV3CXK-3PdTLudwqAH9jTDhq_sqjZBVAv4tgfaOZ0g6OMMJekEcNCaVtcyG7Ebcv_ar2NiW90cd3nptn68PqcLPV0gOfFnKQX_5opkkJZi-s4VikCgePG2qOKlTIvIAcd3xHLyviigHuAbvsiJU4dTaww6Ll1MAbbX7o1Us3TLFfPiRRiOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01aa2ba27b.mp4?token=uv0SU_UHHAZXIezFS1PD3VodZ7xVuiYxl-Dhkjehem0G8BdYvdDP2KVLVWpZtxUJyyEi0a5Y9W6fR5wAsoxjjmjwzqydqD2sOuODDtmIqxABSVTEZLZmit9Hl-Kn-spIn6QATaiMICyVKEo_NLOSGQiL84I8xgnpfBfFV3CXK-3PdTLudwqAH9jTDhq_sqjZBVAv4tgfaOZ0g6OMMJekEcNCaVtcyG7Ebcv_ar2NiW90cd3nptn68PqcLPV0gOfFnKQX_5opkkJZi-s4VikCgePG2qOKlTIvIAcd3xHLyviigHuAbvsiJU4dTaww6Ll1MAbbX7o1Us3TLFfPiRRiOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ :  چونفدا ها رالی موتوری برگزار‌کردن هم اکنون میدان آزادی
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/24129" target="_blank">📅 12:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEkZjznGHLfopAI0oU5pcylSgp_OziCfCVm9e5DOoX3VCMiy3mph0RPyhESk3xDM4szNIwgpgVVaNvG0Jr2hQrVIXTdjMlM8Sfu_gu7xLomac5XKyuDh-3NBGRLu1p-lXkPg_IdUo02moOlIL3XDYzso7ux4SfMQ_6bKUYZLDCxBaOhJxeQ4DvnuSU0Qjrh1UUTUHerHWDx96B3xLaSSbzekBntquXC5vCyq_696l-WpVZBv7SP08fLuiz1o3PVxHY8E-AyK7Y0_ThL0AfiTCaMJZarUWcHiIlpY6XZQg1AcxodAgIlMGrz8YEW7UdVaJFZzzx4vnP5YMBsOrYFQLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید غضبان (دیپلمات اسرائیلی و مشاور در وزارت امور خارجه اسرائیل):
«اسرائیل او را از میان برداشت، اما قاب عکسش مجبور شد تمام آن سخنرانی را تحمل کند؛ به‌ویژه آن بخشی که نتانیاهو با شور و حرارت از فروپاشی جمهوری اسلامی حرف می‌زد»
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/24128" target="_blank">📅 12:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وال‌استریت ژورنال:
میانجی‌ها
در تلاش‌اند
دور جدید مذاکرات میان آمریکا و ایران را
اوایل هفته آینده در عمان
برگزار کنند؛ مذاکراتی که محور آن بازگشایی تنگه هرمز و تلاش برای پایان جنگ است. این مذاکرات هنوز قطعی اعلام نشده و در مرحله رایزنی قرار دارد.
@WarRoom
حقیقت یاب اتاق جنگ : این اصل خیر است ، مذاکرات هنوز نهایی‌نشده و خبر رسانه های زد فیک نیوز است</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/24127" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دریادار رابرت هاروارد، معاون پیشین فرمانده سنتکام:
«من ذهنیت مردم زیبای ایران را می‌شناسم. آنها به آزادی و زندگی باور دارند. ایران نخستین کشوری بود که منشور حقوق بشر داشت. من
متعهد
به کمک به همه شما هستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/24126" target="_blank">📅 11:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDdET9NxlwXQET1bTfTSQOFqtE6Uc_YnDtgkIG4amSDVu-fPBUvem2Z9jTgN-NwdxU3IZcMBfsR9iIKExihAUK7KkY8RU1Ob5ZreqGc1teIIksE-CYM0-dAigsXB7Qz4HHbRQFGDnkt84CQT-EwNqmTR81bSi_pvtyEoOPBd_BFFeykx_90WZOqq-wBHWAf6E0qPhPdfz3lHj9rRyf_NNSvzAnwOyUJx-vvVGBfq8SZRxRjpGRRHg6N2xZWKknGx5G9vPBn-tgoz0OfeUqcLmjmCOTHaNB9ifmYfPsCxGfS_kE7x7iFuMvawwZQu4PrI7f4tiDjBAx-_cWw92p3EEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پی۸ پوسایدون ، ام ۴۰۰ (نمونه مشاهبه هرکولس از ایرباس) و ۴ سوخترسان هم اکنون در حال انجام مأموریت در منطقه خلیج فارس و تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/24125" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ نتانیاهو در پاسخ به خبرنگاری که پرسید پیامش برای مردم ایران چیست،گفت :
«ما با شما هستیم. ناامید نشوید.»
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/24124" target="_blank">📅 11:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ان‌بی‌سی نیوز:
عباس عراقچی، وزیر امور خارجه ایران، در نیویورک به خبرنگاران گفت تهران از طریق میانجی‌ها طرحی را به مقام‌های آمریکایی ارائه کرده که در صورت پذیرش شروط ایران،
پس از هفت روز به بازگشایی تنگه هرمز و ازسرگیری مذاکرات
منجر خواهد شد. به گفته عراقچی، یکی از شروط طرح، پذیرش مسیر عبور دریایی مورد توافق ایران و عمان در تنگه هرمز است. ان‌بی‌سی نیوز گزارش داد کاخ سفید تا زمان انتشار این گزارش به درخواست اظهارنظر درباره این طرح پاسخ نداده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/24123" target="_blank">📅 11:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جروزالم پست:
نیروهای دولت یمن حمله حوثی‌ها به یک مسیر مهم تدارکاتی میان عدن و تعز را دفع کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/24122" target="_blank">📅 11:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کوین‌دسک
:
حدود
۱۸ میلیارد دلار قرارداد آپشن بیت‌کوین و اتر
امروز منقضی می‌شود؛ حجم بالای سررسید می‌تواند در کوتاه‌مدت نوسانات بازار و جریان‌های هجینگ را افزایش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/24121" target="_blank">📅 10:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رویترز:
تعداد عبور کشتی‌ها از تنگه هرمز در روز پنجشنبه به ۹ فروند کاهش یافته، در حالی که روز قبل ۱۴ فروند و میانگین ۱۰ روزه حدود ۱۸ فروند بوده است؛ البته کشتی‌هایی اصلی که انتقال را انجام میدهند و ترانسپوندر خود را خاموش کرده‌اند در این آمار نیستند.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/24120" target="_blank">📅 10:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24119">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYwXw38Y4-FYzEgGkm9gt6SAKYiggEc0wV2YlaFuyUWlPMnxjhZCO45XYO0JZmQC9hYLE5k23X_zhkMQDuoB4lvS7CMmRktEKnTAqxAo9LDH2V0XJydyKKK2cvY1l70GAjH4UgFF4TTXQgrYT8bZvyB-UgN-OnYXFvAkXPys-O5vP-xVgdqDccJtK3Uos71asG-_Bf0nXPAl5UGkgAecvP7Rq3ut6lnu2nvAkMZoLSqCkx1ML7SNbS59MPJAF-mqfklN7fWJg4G_4gaFnM9MCNa1DMHXrcQ6DyHFVmQQwyXpjTablAPq1x-hDcLRz9hOQESLvOw0ElyOxUjuzuoDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وار زون
:
یک فروند جاسوسی SR-71 Blackbird با شماره
NASA 844
، آخرین SR-71 پروازکننده در تاریخ، از محل نمایش عمومی خود در مرکز تحقیقات پرواز آرمسترانگ ناسا در پایگاه ادواردز ناپدید شده و اوایل امسال به یک آشیانه دیگر منتقل شده است. این اتفاق پس از انتشار تصویری مرموز از سوی جرد آیزاکمن، مدیر ناسا، از یک هواپیمای سیاه شبیه SR-71 و صحبت‌های او درباره بازگشت به پروازهای بسیار سریع و در ارتفاع بالا رخ داده است. انتقال این هواپیما احتمال استفاده مجدد از آن یا حتی انجام یک مأموریت پروازی محرمانه جاسوسی را مطرح کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/24119" target="_blank">📅 10:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏دانیل رافکاس، قاضی فدرال آرژانتین، برای هفت مقام و شهروند ایرانی و یک عضو حزب‌الله لبنان در پرونده بمب‌گذاری مرکز یهودیان آمیا قرار تعقیب صادر و مسیر محاکمه غیابی آنان را باز کرد. محسن رضایی و احمد وحیدی از جمله متهمانی هستند که دستگاه قضایی آرژانتین آنان را به نقش داشتن در تصمیم‌گیری و طراحی حمله متهم کرده است. بر اساس این حکم، توقیف دارایی‌های هر متهم تا سقف ۵۰۰ میلیون دلار نیز دستور داده شده است. بمب‌گذاری آمیا در سال ۱۹۹۴ به کشته‌شدن ۸۵ نفر انجامید.
@WarRoom</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/24118" target="_blank">📅 10:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه عده سیاه پوست و محجبه سالن رو ترک کردن  @WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/24117" target="_blank">📅 10:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیویورک‌پست: سنای آمریکا بار دیگر طرحی برای محدود کردن اختیارات جنگی ترامپ در جنگ ایران را رد کرد؛ این رأی به معنای حفظ اختیارات فعلی رئیس‌جمهور آمریکا برای ادامه عملیات نظامی است. @WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/24116" target="_blank">📅 10:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جروزالم پست:
عمان هم پروازهای شرکت‌های هواپیمایی ایرانی را تا اطلاع ثانوی متوقف کرد؛ این تصمیم به تحریم‌های جدید آمریکا علیه بخش هوانوردی ایران اعلام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/24115" target="_blank">📅 09:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24114">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رویترز:
عربستان سعودی، ترکیه و پاکستان قرار است در پی تشدید حملات حوثی‌ها، نشست فوری فرماندهان ارشد نظامی برگزار کنند؛ این نشست در چارچوب پیمان دفاعی مشترک سه کشور انجام می‌شود.
همچنین مقام مذهبی ارشد عربستان از نیروهای نظامی این کشور خواست برای مقابله با حوثی‌ها آماده فدا کردن جان خود باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/24114" target="_blank">📅 09:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وال استریت جورنال: بن سلمان ولیعهد عربستان سعودی اخیراً به مسئولین آمریکایی اطلاع داده است که ایالات متحده باید به تحریم‌های دریایی ادامه دهد تا تهران را مجبور به امضای یک توافقنامه جدید کند.
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/24113" target="_blank">📅 09:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کلمبیا در مجمع عمومی سازمان ملل متحد، قطع روابط دیپلماتیک با ایران را اعلام کرد. @WarRoom امشب الهیه صف سفید‌ بازاست فردا قیمت میره بالا
❄️
😂</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/24112" target="_blank">📅 09:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادعای احمد بخشایش‌اردستانی، عضو کمیسیون امنیت ملی مجلس: او مدعی شد شنیده است که ایران از کره‌شمالی سلاح هسته‌ای خریداری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/24111" target="_blank">📅 09:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مصاحبه‌کننده:
«پس آیا تصاویر ماهواره‌ای چین به کشته شدن سربازان آمریکایی به دست ایران کمک کرد؟»
پزشکیان:
«ما به دنبال کشتن آمریکایی‌ها نیستیم. همان‌طور که اقدامات، اقدامات قابل اثبات، نشان داده‌اند، آمریکا به دنبال کشتن ایرانی‌ها بوده است.»
مصاحبه‌کننده:
«اما آنها در آنجا کشته شدند، آیا شما از تصاویر ماهواره‌ای چین استفاده کردید؟»
پزشکیان:
«نه. اصلاً. نه. نه. اول از همه، من مشخصاً از این تصاویر گزارش‌شده و ادعایی که شما درباره آنها صحبت می‌کنید، اطلاعی ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24110" target="_blank">📅 03:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شی جین‌پینگ: امروز من و ترامپ گفت‌وگویی صادقانه و عمیق داشتیم و درباره بسیاری از مسائل به تفاهم مشترک رسیدیم. این تفاهم، محتوای جدیدی به روابط سازنده چین و آمریکا با هدف ثبات راهبردی اضافه کرده و راهنمایی راهبردی جدیدی برای روابط دو کشور فراهم کرده است. @WarRoom…</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/24109" target="_blank">📅 03:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/24108" target="_blank">📅 03:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519484d74f.mp4?token=p38Ivp0e9eq46815O_UtDSb7uVz500Dpmi8QvIfQBop8G5ROyv6ZQWIA-uDSEnjnm8FppWVQZVx4QbWuJkl8W5bUoVnUUCvbyeGZ9azSWqn9P3o0P6talGxYYxclXbxa3s312N_81vUgW80oW1_zaZUpdTL3oA-U4x9GqLUyL8WcRp5FtMjKD_OTHoC9fBvf5aHQr4lehWgAg8Yo_PrXdRM9hEaiqVjKRp7hUea4dIBWM7Y9Oo9L_MaRmy5BSJfr_xcq--QpT8dKahR3OROsWKhq9dJaY0PoqKf3PmHAuq3Y0pTVrXF0RiXlraWf97KlWKxfY7djtjV53NBtFC0ehw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519484d74f.mp4?token=p38Ivp0e9eq46815O_UtDSb7uVz500Dpmi8QvIfQBop8G5ROyv6ZQWIA-uDSEnjnm8FppWVQZVx4QbWuJkl8W5bUoVnUUCvbyeGZ9azSWqn9P3o0P6talGxYYxclXbxa3s312N_81vUgW80oW1_zaZUpdTL3oA-U4x9GqLUyL8WcRp5FtMjKD_OTHoC9fBvf5aHQr4lehWgAg8Yo_PrXdRM9hEaiqVjKRp7hUea4dIBWM7Y9Oo9L_MaRmy5BSJfr_xcq--QpT8dKahR3OROsWKhq9dJaY0PoqKf3PmHAuq3Y0pTVrXF0RiXlraWf97KlWKxfY7djtjV53NBtFC0ehw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ:
امروز من و ترامپ
گفت‌وگویی صادقانه و عمیق
داشتیم و درباره بسیاری از مسائل به
تفاهم مشترک
رسیدیم. این تفاهم، محتوای جدیدی به روابط سازنده چین و آمریکا با هدف
ثبات راهبردی
اضافه کرده و
راهنمایی راهبردی جدیدی برای روابط دو کشور
فراهم کرده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/24107" target="_blank">📅 03:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24106">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d93f107e3.mp4?token=TuODhAUfUbo9e15Dal2Fojdt3MNYN-e-x8zLYLDuCOj3Cqu2NrzNeNdJL5XB1hRtW6nghMG-MkNBsSaujCc7cJkw7GBstIN1uph3o96v4ysOMwT7NDF-QmaamRSPDDwVvTeco87F-eiviPtM63cOq6infUDrnuEDaivVs9_EPBMg9YzKFgjs1WuwLw_vzFG8K9tLm79c3gbe5GImv79VbYRN4TUmrZwg15yiTnX4EMl2rGRlYTNZVEzi1XUytokcOAfK0PJcr78FMTRW-BX_MD697v88WdJOAPKBnr0_G9X-uo_r0osvWsANEU4UXlMiJSn4BhbLfjevjPKcI8_R1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d93f107e3.mp4?token=TuODhAUfUbo9e15Dal2Fojdt3MNYN-e-x8zLYLDuCOj3Cqu2NrzNeNdJL5XB1hRtW6nghMG-MkNBsSaujCc7cJkw7GBstIN1uph3o96v4ysOMwT7NDF-QmaamRSPDDwVvTeco87F-eiviPtM63cOq6infUDrnuEDaivVs9_EPBMg9YzKFgjs1WuwLw_vzFG8K9tLm79c3gbe5GImv79VbYRN4TUmrZwg15yiTnX4EMl2rGRlYTNZVEzi1XUytokcOAfK0PJcr78FMTRW-BX_MD697v88WdJOAPKBnr0_G9X-uo_r0osvWsANEU4UXlMiJSn4BhbLfjevjPKcI8_R1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
به
رئیس‌جمهور شی جین‌پینگ هدیه‌ای
داد
@WarRoom</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/24106" target="_blank">📅 03:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90b4fb0cfe.mp4?token=OSpIyBci2JQlk3H1pjmoQHE6tj3ef6uaRVJ2u7CtO0MsrSnvruAgcorLtK0HHTbsfPpTYqK6pIRdMRfFxHAwyrNgtbIC3oxpXF9Fj3zQ1M0JImGZ20eFENZM1pgmTTFaMc4YDXGhF5mYgUZ2Ttx6lGCAl-pHebgoxAiKdDnLSYHRbE78p2OHTqQGqUhAB9gpL9aPfQg9rKm10cxqrg9Kx0TvTG0ZyP4g___GbT7OTM16QQMFvlNI2u4KUYkeV9YlE74lqB9Qs8IUnm7D7YnAb8RMKxA7WWYol_b25G21zVGEnFI5UFn5yx-M7UrBQfxqSvnkCouiw3uLBCJFkftOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90b4fb0cfe.mp4?token=OSpIyBci2JQlk3H1pjmoQHE6tj3ef6uaRVJ2u7CtO0MsrSnvruAgcorLtK0HHTbsfPpTYqK6pIRdMRfFxHAwyrNgtbIC3oxpXF9Fj3zQ1M0JImGZ20eFENZM1pgmTTFaMc4YDXGhF5mYgUZ2Ttx6lGCAl-pHebgoxAiKdDnLSYHRbE78p2OHTqQGqUhAB9gpL9aPfQg9rKm10cxqrg9Kx0TvTG0ZyP4g___GbT7OTM16QQMFvlNI2u4KUYkeV9YlE74lqB9Qs8IUnm7D7YnAb8RMKxA7WWYol_b25G21zVGEnFI5UFn5yx-M7UrBQfxqSvnkCouiw3uLBCJFkftOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من و شی هر دو می‌دانیم که نماینده
نظام‌های متفاوتی
هستیم، اما روابط میان مردم دو کشور همچنان پابرجاست و
هیچ‌وقت به اندازه امروز روابط خوبی با یکدیگر نداشته‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/24105" target="_blank">📅 03:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d197af82.mp4?token=lozhitKxVRqGeZxDD96CLnlfTvimOnsV6BMHGLPBSEG9vXnFBoQ28YpktMjYyMpdwk5osinjz8Jxbxxcy6XQaVdngZ3h81knbBCQnPvV3M8DgeTwqch-CY9Dckp1Tl7tzqttbj6AdWqOFXHRB-Ng2fYfwGqCNV-TSeKTlxXBYb4-c0nRJrWXx2Kwz6YZi3Lq_XI5vhfG7nFq20o3Ty2eYZc_4ELSvgs_EhkCD8OhVaQPUmg0Yx4ejQ6OiSrtAEF4LEGC3Ds_x0M7PSutFlNv6QI9WD_ktkzkDEDyfuXYojjeyTNX0rMTNnddfbtBoxrf8dIl2M_Xm_GtfSuVs_vMAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d197af82.mp4?token=lozhitKxVRqGeZxDD96CLnlfTvimOnsV6BMHGLPBSEG9vXnFBoQ28YpktMjYyMpdwk5osinjz8Jxbxxcy6XQaVdngZ3h81knbBCQnPvV3M8DgeTwqch-CY9Dckp1Tl7tzqttbj6AdWqOFXHRB-Ng2fYfwGqCNV-TSeKTlxXBYb4-c0nRJrWXx2Kwz6YZi3Lq_XI5vhfG7nFq20o3Ty2eYZc_4ELSvgs_EhkCD8OhVaQPUmg0Yx4ejQ6OiSrtAEF4LEGC3Ds_x0M7PSutFlNv6QI9WD_ktkzkDEDyfuXYojjeyTNX0rMTNnddfbtBoxrf8dIl2M_Xm_GtfSuVs_vMAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا غنی‌سازی اورانیوم ۶۰ درصد را کنار می‌گذارید؟
مسعود پزشکیان:
بله،
در چارچوب قوانین بین‌المللی و بر اساس معاهده منع گسترش سلاح‌های هسته‌ای (NPT)
. هر چیزی که موظف به رعایت آن باشیم، رعایت خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/24104" target="_blank">📅 03:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
حوثی‌ها مسئول اقدامات خودشان هستند و از ما دستور نمی‌گیرند. ما به‌عنوان کسانی که در منطقه مقاومت می‌کنند و با توجه به شرایطی که به آنها تحمیل شده، با آنها در ارتباط هستیم؛ اما
هیچ رابطه سازمان‌یافته‌ای میان ما وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/24103" target="_blank">📅 03:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/24102" target="_blank">📅 03:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24101">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تصاویر نمای نزدیک و چشمگیر از بمب‌افکن راهبردی B-21 نیروی هوایی آمریکا (نسل جدید B2)
که امروز برای انجام آزمایش‌های پروازی از پایگاه نیروی هوایی ادواردز در کالیفرنیا به پرواز درآمد.
این بمب افکن مخوف هنوز عملیاتی ‌نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/24101" target="_blank">📅 03:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24100">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f0f08a00.mp4?token=rDVjlIZkUGcjzE1FJX97tkXknnM4yJ5ywtnC6rTeIMqongzf-olZJpjxViaVxSXfQQFq1ctzLQShjRhe05QGpW6Fdqcz7HCxNaCVBRO2nagnRIUVPdMRBoJHUqCkPnaJ2911FzsZ0jSvMOxeFzAsUvXbMEDIIFR7qYX51n58ze5jgj6J3M4qqC-ggXROttIEfJOYkfpNilTQZ0s5Yn2atABeNhZBaGy2WIKZZl4b9TnwfIz3RzMQaglJLpM6aivUTUDI9PS_nHfAVlOrMbzv-uvkSGx3xBQoN9zSm9ALtvVae81OX3REzHJux6LrIfqliet5JWv_UFsLN2vO3odfDn_vn6UkosNGvDEFvIHnY-eeHQMjef8Zp-KU1IWiEA5Js4-vs-4f49c8NRNvqQXZH3QOnNKc8fol5N1u4ytc41NkGTtnvmHURBrFYWzlLsAp2dILijEVzkqqLdzLDWTKO2bH3v2eOZqvAShV6WSy2uNg_O_WNRFugkw6ErQJ6TDU_F2SC2xG6ThL42Lzh1a6nspYOEmY7loQYC8SK9EvB9af3HLhzbTLrMNijJ18Ds5WykOg9Fnz8B2o0FX6WWlnTnSjH3akl2ZHe6JVRrvJdL0Ce-UBOz9CjxZMktNOHtK8qkTGfDmgzjIDGYDfutRaIFwjEiFDOVki1geOYSPWpaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f0f08a00.mp4?token=rDVjlIZkUGcjzE1FJX97tkXknnM4yJ5ywtnC6rTeIMqongzf-olZJpjxViaVxSXfQQFq1ctzLQShjRhe05QGpW6Fdqcz7HCxNaCVBRO2nagnRIUVPdMRBoJHUqCkPnaJ2911FzsZ0jSvMOxeFzAsUvXbMEDIIFR7qYX51n58ze5jgj6J3M4qqC-ggXROttIEfJOYkfpNilTQZ0s5Yn2atABeNhZBaGy2WIKZZl4b9TnwfIz3RzMQaglJLpM6aivUTUDI9PS_nHfAVlOrMbzv-uvkSGx3xBQoN9zSm9ALtvVae81OX3REzHJux6LrIfqliet5JWv_UFsLN2vO3odfDn_vn6UkosNGvDEFvIHnY-eeHQMjef8Zp-KU1IWiEA5Js4-vs-4f49c8NRNvqQXZH3QOnNKc8fol5N1u4ytc41NkGTtnvmHURBrFYWzlLsAp2dILijEVzkqqLdzLDWTKO2bH3v2eOZqvAShV6WSy2uNg_O_WNRFugkw6ErQJ6TDU_F2SC2xG6ThL42Lzh1a6nspYOEmY7loQYC8SK9EvB9af3HLhzbTLrMNijJ18Ds5WykOg9Fnz8B2o0FX6WWlnTnSjH3akl2ZHe6JVRrvJdL0Ce-UBOz9CjxZMktNOHtK8qkTGfDmgzjIDGYDfutRaIFwjEiFDOVki1geOYSPWpaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ و ملانیا ترامپ
در کاخ سفید از
شی جین‌پینگ، رئیس‌جمهور چین، و همسرش پنگ لی‌یوان
برای ضیافت شام رسمی دولتی استقبال کردند.
خبرنگاران CNN و MS NOW
اجازه پوشش و حضور در مراسم ورود شی جین‌پینگ به کاخ سفید برای این ضیافت شام رسمی را دریافت نکردند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/24100" target="_blank">📅 02:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684edd63a4.mp4?token=s4VnQp2KJdBSuEPMNwiBn3-nmPsqUuVad7g102xeRK-62jpvRyG4qlcqyVCg_quy-JcUAb8t2xw18Fz36A8GtNjuydXTWt2S5Wq_RFviAi7EQE0mVL_aNxd6mAkQsXSM3otlUfbD_Uq-lZqSKDMWITPrSbv3TRjoO2Ym3D-UEKck98sN-7gu_0GWCNz6EaO-vtfdpySnUFLyRKi3ZGjQ1kxQUHzezmhZRcplqfjH5D6a04oFsgOjOPXYLlifS_IR182BsxnOKAaTCZYjAZBNaxV6xDc6bUaF3sYFyEVEUVg0KOe8zP3Yy8O0oAfp4TH5IIIeAfmOumb3-ZpJl2HX4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684edd63a4.mp4?token=s4VnQp2KJdBSuEPMNwiBn3-nmPsqUuVad7g102xeRK-62jpvRyG4qlcqyVCg_quy-JcUAb8t2xw18Fz36A8GtNjuydXTWt2S5Wq_RFviAi7EQE0mVL_aNxd6mAkQsXSM3otlUfbD_Uq-lZqSKDMWITPrSbv3TRjoO2Ym3D-UEKck98sN-7gu_0GWCNz6EaO-vtfdpySnUFLyRKi3ZGjQ1kxQUHzezmhZRcplqfjH5D6a04oFsgOjOPXYLlifS_IR182BsxnOKAaTCZYjAZBNaxV6xDc6bUaF3sYFyEVEUVg0KOe8zP3Yy8O0oAfp4TH5IIIeAfmOumb3-ZpJl2HX4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان :
ما هرگز به مردم خودمان حمله نمی‌کنیم.
برت بایر، خبرنگار فاکس نیوز:
اما این کار را کردید.
پزشکیان:
نه، نه. چه کسی علیه ما اقدامات تروریستی انجام داد؟ چه کسی به مدارس ما حمله کرد؟
بایر:
متوجه هستم، اما در روزهای ۸ و ۹ ژانویه، نیروهای امنیتی شما قطعاً شهروندان ایرانی را کشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/24099" target="_blank">📅 02:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24098">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مسعود پزشکیان درباره اعتراضات ژانویه:
خود آقای ترامپ اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده بود تا دولت ایران را سرنگون کنند. افراد نتانیاهو اعلام کردند که نیروهایی از استان‌های کردستان و بلوچستان وارد مراکز کلان‌شهری خواهند شد تا دولت را سرنگون کنند. آنها تصور می‌کردند این ماجرا سه‌روزه خواهد بود و دولت سقوط خواهد کرد، اما دولت ایستادگی کرد، منسجم‌تر شد و اتحاد بیشتری پیدا کرد. حتی کسانی که به دلایل مختلف در برابر دولت ایران ایستاده و با ما مخالف بودند، اکنون از ایران حمایت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/24098" target="_blank">📅 02:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">از وسطش +۱۸ هست</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/24097" target="_blank">📅 02:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24096">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/24096" target="_blank">📅 02:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما
تا آخرین لحظه به مقاومت ادامه خواهیم داد
. بله، قطعاً با مشکلات اقتصادی مواجه هستیم، اما برای اینکه بتوانیم پابرجا بمانیم،
هر سختی و فشاری را تحمل خواهیم کرد و از آن عبور می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/24095" target="_blank">📅 02:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه بیاورم»، اما هدیه‌ای که آنها برای ما آوردند
موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی
بود. آنچه آنها واقعاً می‌خواهند انجام دهند،
ایجاد و تحریک حوادث و ناآرامی‌هایی در داخل کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/24094" target="_blank">📅 02:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت کنونی آمریکا بخواهد
در چارچوب قوانین بین‌المللی
به توافق برسد، بسیار خوب. اما اگر نخواهد،
برای ما چه تفاوتی دارد که این اتفاق قبل از انتخابات آمریکا باشد یا بعد از آن؟
@WarRoom</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/24093" target="_blank">📅 02:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
هرکس بخواهد اعتراض کند،
کاملاً حق دارد این کار را انجام دهد
. ما با بسیاری از این معترضان نشستیم و با آنها گفت‌وگو کردیم؛ اما
مسلح‌کردن اعتراضات و تبدیل آنها به ابزار درگیری، موضوع کاملاً متفاوتی است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/24092" target="_blank">📅 02:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
یکی از مشکلاتی که با آن مواجه هستیم این است که
پول ایران در چین مسدود شده است
. ما حتی نمی‌توانیم پول خودمان را از کشوری که در ازای آن به آن کالا صادر کرده‌ایم، خارج کنیم؛ چه رسد به اینکه بتوانیم از این منابع برای پرداخت به فرد یا طرف دیگری در نقطه‌ای دیگر از جهان استفاده کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/24091" target="_blank">📅 02:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مسعود پزشکیان:
ما با ترامپ به توافق رسیدیم. آن توافق امضا شد و بر اساس همان توافق، ما آماده بودیم و همچنان مایل هستیم که مسیر را ادامه دهیم و چارچوب آن نیز مورد توافق قرار گرفته بود. ما تنگه هرمز را نبسته بودیم و تنگه باز بود؛ اما آنها بدون هیچ توجیه یا چارچوب قانونی به ما حمله کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/24090" target="_blank">📅 02:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مسعود پزشکیان:
ما جنگ را انتخاب نکردیم؛ جنگ به ما تحمیل شد. ما به‌دنبال جنگ نیستیم، بلکه هر زمان به ما حمله شود، مجبوریم از خودمان دفاع کنیم. ما هرگز آغازکننده جنگ نبوده‌ایم، اما اگر آنها بخواهند به جنگ با ما ادامه دهند، با قدرت پاسخ خواهیم داد
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/24089" target="_blank">📅 02:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24088">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e58f2038.mp4?token=IDDvQRvkF2ooHd1S8XB4HRqitjAWsp1a6kWtGcVeMWjRMv7rNwejE3jnex0faPUjbolQ5G_Wf-JQZOGHPt3vb0IywLKbeioEuavC7Il8KwRqH7wx-EmFmuKGc4zUeCW0p_Oio6qC1NXQ9oqD3CV1Z2AYzxW0syAJ_BXR7iHUgan-K9xj3GXwTqb0gbAARG9-TjYUnxpwQAC51SlCc_HYKfHCZBDF3O9KbDzH7Q1XHPNOh8K44E80a4AkqTID-039n4I0864VXedN-78vzZ14AO45i5-jECKNmx10Hgnd_u4qz_jNshNFBZi6QCmZ_dIdotXTJPMh3w4kLxRa7b-8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e58f2038.mp4?token=IDDvQRvkF2ooHd1S8XB4HRqitjAWsp1a6kWtGcVeMWjRMv7rNwejE3jnex0faPUjbolQ5G_Wf-JQZOGHPt3vb0IywLKbeioEuavC7Il8KwRqH7wx-EmFmuKGc4zUeCW0p_Oio6qC1NXQ9oqD3CV1Z2AYzxW0syAJ_BXR7iHUgan-K9xj3GXwTqb0gbAARG9-TjYUnxpwQAC51SlCc_HYKfHCZBDF3O9KbDzH7Q1XHPNOh8K44E80a4AkqTID-039n4I0864VXedN-78vzZ14AO45i5-jECKNmx10Hgnd_u4qz_jNshNFBZi6QCmZ_dIdotXTJPMh3w4kLxRa7b-8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز: آقای رئیس‌جمهور، منظورم همان حادثه ژانویه است. شما جراح قلب هستید.
نیروهای امنیتی ایران چند ایرانی را کشتند؟
پزشکیان: ببینید چندان هم دشوار نیست. می‌توانید افرادی را به آنجا بفرستید تا حقیقت را مشخص و احراز کنند. آنچه فلان و بهمان نشریه در خارج از کشور گزارش می‌کند، با روایت دقیق و مستند از وقایع مطابقت ندارد. وقتی می‌گویند ۱۰ هزار نفر یا ۱۷ هزار نفر، چرا دست‌کم دو شماره ملی ارائه نمی‌کنند؟
@WarRoom</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/24088" target="_blank">📅 02:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/24087" target="_blank">📅 02:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24086">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c08c2421f.mp4?token=i4P10mX0evpwjP-W5EJ4QoJ66t-RTdOOs8uU-T7-hdNb7A_IQ4ugAyLsY5rQYyxdwEYjIuaekgYoQ7reUmQKFwk_MpKIQN7Y3gye7EAfrkdr9slrPKi6J1pGXX1NVVDotOkYswud44jzrBmyrQ9I9eopO0ys3WwUEXolgmJ_l8ynpEvNfOdtmkXp7SuRP8y2HppamftqJePydhE0JNizwv2_YjCZyP90JtX_y0OXFaj-ZC6wi9aw-YROV5Ze3uESz2ZXccZTdDlYAcLBfwgA3nMM6O4aB8Hrc-cSUVnCPGjHOEdBst2dm16m1uFdrRPEpM32-_fRRR78gjVvbK8f5GWpiMX4SPL0H28ExQM9_gZKb1uuTbHxCZLK0SVJ0iDaZ_FNs_bF6ncYlE6-u1oYqb2RI7fH2nQq69O9chi26LNNXwIixxWqjzZl9844QGFM1hMUiiOfo8pCrlTyhMf6jDgOIJzvavuwxAawxuBTaNwFuafmZAFuMrLE8xPmWtlwq21mX0F4fgZqJW4871qVy3ZbaqyXYeq4WJbS3zNFpbwBebMEHt1dVUObmV9W83z13DtPUn0sOhN8woLMusCvWlifwoP4qHlcCMAGU6DX9GReimgPiNggjQAUfhztuH0cSaQGQIf-4CsA-qrIqRWoVjjiaQ21xLr9zq6vfo-tQJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c08c2421f.mp4?token=i4P10mX0evpwjP-W5EJ4QoJ66t-RTdOOs8uU-T7-hdNb7A_IQ4ugAyLsY5rQYyxdwEYjIuaekgYoQ7reUmQKFwk_MpKIQN7Y3gye7EAfrkdr9slrPKi6J1pGXX1NVVDotOkYswud44jzrBmyrQ9I9eopO0ys3WwUEXolgmJ_l8ynpEvNfOdtmkXp7SuRP8y2HppamftqJePydhE0JNizwv2_YjCZyP90JtX_y0OXFaj-ZC6wi9aw-YROV5Ze3uESz2ZXccZTdDlYAcLBfwgA3nMM6O4aB8Hrc-cSUVnCPGjHOEdBst2dm16m1uFdrRPEpM32-_fRRR78gjVvbK8f5GWpiMX4SPL0H28ExQM9_gZKb1uuTbHxCZLK0SVJ0iDaZ_FNs_bF6ncYlE6-u1oYqb2RI7fH2nQq69O9chi26LNNXwIixxWqjzZl9844QGFM1hMUiiOfo8pCrlTyhMf6jDgOIJzvavuwxAawxuBTaNwFuafmZAFuMrLE8xPmWtlwq21mX0F4fgZqJW4871qVy3ZbaqyXYeq4WJbS3zNFpbwBebMEHt1dVUObmV9W83z13DtPUn0sOhN8woLMusCvWlifwoP4qHlcCMAGU6DX9GReimgPiNggjQAUfhztuH0cSaQGQIf-4CsA-qrIqRWoVjjiaQ21xLr9zq6vfo-tQJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج پیغام های  شما از گزارش عجیب ایران اینرنشنال توسط مجری افغان این شبکه مرضیه حسینی که مجاهدین خلق رو مردم ایران میدونه و پرچم جعلی اونها رو پرچم شیرو خورشید عنوان میکنه ! و پروموتشون میکنه !
@WarRoom</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/24086" target="_blank">📅 02:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کلمبیا در مجمع عمومی سازمان ملل متحد، قطع روابط دیپلماتیک با ایران را اعلام کرد.
@WarRoom
امشب الهیه صف سفید‌ بازاست فردا قیمت میره بالا
❄️
😂</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/24085" target="_blank">📅 01:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtiF6Xbxfx5YLRObKN8xD6HYVH7-Msz7bcSKzL5oQD4BeiUbc-O_t2rhrToYFNdjJ4zIqBNGPyTFZ5RiL26YcouPMofAHkierr9F0F4f9Yus7rGePo_lMKCk_LE0mW4YpuBJFUSjODdbWHeIrf8tdz36o0WJ2-VluF99KBPwwAMg5_5re8vVJGz4BfdLD7DZy5djeL_lgv2XllOhwdJZiXeVkdWK575YL4lq7QZ20IuJ8t0DyKpiaiY_cgjTntBCKakYPdUZG22JLBqp-M_pWobM2XVOjq9lk8g1ge0lETWdfc9ag5EvtFPEZPGdzmYhIzPxnz9BEdHmiydlwrYiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده اسرائیل یه استارلینک میبره برای نمایندهی ایران در صحن سازمان ملل و می‌گه اینو بگیر به کارت میاد. و می‌گه ما عاشق مردم ایران هستیم و برای تغییر رژیم دعا می‌کنیم. @WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/24084" target="_blank">📅 01:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137bb832f8.mp4?token=bX5_DS3swzyiIoTSpsiO_RoYX9LtWpMUoLTO1GFVMgINsJniftU9poucigXSSgZnVxwjVjvjPln1wZyNNBDC4UUXtIwECzExmI0AMQr1d1BlaOcFzWrFsyk0c-U47_PsAXa7vu-GwtJCxcWDDYHD0NYA2V49LEd9oZm5nglNP6aJL3WHj0x6LCnf6hldiOIBCE2DSf1UG-aBem8Sknl0873Atz5NbKwAP56Pa2d7N9vGwnSSgu9hugpphvwK-EadhqxaFdYzU229k2aD7z_URCJsDP3Rz02xvz1JsUuouc-wFQdXjpG3coIfS4Znl7Rb9pwfQRVQV13TBp1gujAd0zXojYsyxLFBD0OoTHVhk6LhuGZryPJMYL5wrtlBDlBXNljCZRm_IMCZtNZ7f7-SmTMsLv5LU68oaYZrDR484Kub4_5zG8OgQSkQPyO1x_rBzhJFkREMI4MS55lJdIQGXdO4z_OItsKW2oY-OkXsNA9EVUxMamErf1NF39BmrdzLAZNUWAeuMq3gSNubCbbg8cPwyLjMmcP0affFij-BKPuclhAWNmgZe3t5v61nHy2dBgZ3qpxyrzVxOqwTanHl2kP8U6DJt85e3Jm1X5NdhNO5ZqD2AdfkD4HW83A32wy_H1tPhWphp3bfpw61aggcjg1lX55pK45fO-u5SbHiLMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137bb832f8.mp4?token=bX5_DS3swzyiIoTSpsiO_RoYX9LtWpMUoLTO1GFVMgINsJniftU9poucigXSSgZnVxwjVjvjPln1wZyNNBDC4UUXtIwECzExmI0AMQr1d1BlaOcFzWrFsyk0c-U47_PsAXa7vu-GwtJCxcWDDYHD0NYA2V49LEd9oZm5nglNP6aJL3WHj0x6LCnf6hldiOIBCE2DSf1UG-aBem8Sknl0873Atz5NbKwAP56Pa2d7N9vGwnSSgu9hugpphvwK-EadhqxaFdYzU229k2aD7z_URCJsDP3Rz02xvz1JsUuouc-wFQdXjpG3coIfS4Znl7Rb9pwfQRVQV13TBp1gujAd0zXojYsyxLFBD0OoTHVhk6LhuGZryPJMYL5wrtlBDlBXNljCZRm_IMCZtNZ7f7-SmTMsLv5LU68oaYZrDR484Kub4_5zG8OgQSkQPyO1x_rBzhJFkREMI4MS55lJdIQGXdO4z_OItsKW2oY-OkXsNA9EVUxMamErf1NF39BmrdzLAZNUWAeuMq3gSNubCbbg8cPwyLjMmcP0affFij-BKPuclhAWNmgZe3t5v61nHy2dBgZ3qpxyrzVxOqwTanHl2kP8U6DJt85e3Jm1X5NdhNO5ZqD2AdfkD4HW83A32wy_H1tPhWphp3bfpw61aggcjg1lX55pK45fO-u5SbHiLMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایمان دشتی، دانشجوی دانشگاه میشیگان، در گفت‌وگو با ویل کین از فاکس‌نیوز گفت از عبدالسعید (نامزد دموکرات انتخابات فرمانداری میشیگان) پرسیده آیا بدون هیچ ابهامی با سپاه پاسداران مخالف است، اما به گفته او عبدالسعید از پاسخ مستقیم خودداری کرد. دشتی گفت فقط کافی بود او صریحاً بگوید با «بزرگ‌ترین حامی تروریسم در جهان» مخالف است و مدعی شد شاید عبدالسعید به دلیل حمایت بخشی از هوادارانش از حکومت ایران و سپاه، نمی‌خواهد آنها را از خود دور کند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/24083" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24082">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری NBC به نقل از مسعود پزشکیان: می‌‌خوایم قبل از شروع انتخابات میان‌دوره‌ای آمریکا توافق کنیم!
اصلا نمی‌خوایم کار به انتخابات میان‌دوره‌ای بکشه و آرزو می‌کنم آمریکایی‌ها قبل از اون به تفاهم‌نامه‌ی آتش‌بس برگردن
ایران برای بازرسی از تأسیسات هسته‌ای خودش اعلام آمادگی کرده
ما به هیچ‌وجه دنبال ترور ترامپ و یا اعضای خانواده‌اش نیستیم
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24082" target="_blank">📅 01:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24081">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400ab8f284.mp4?token=OqSBcDCmZj-9veP7_wlvBB7vvuEcONgW0hPzdPNhd7PMn1n-IAcPbWPTEErvzPD2n_Qk6SrHrhI7l55cKn6XE_wzhQAyRUFlbF40P9ArC52rdNdMZ35PFt0g0f_TgBYReO8Mi6iwxDBwJ2AwEFoEx1AR6yP561g1cQlqqTj7rZ5qc_dHcY-VPQEUvQpCXe0wW4Zd_Sp-NT_5TvH3S5MEs_oiVcrfBW2c81VUzpp16dZ9PiFClq_nscRNS_5cofDlgrtw_PNXFzty0WTPauwg7Fgbi9C-H_iMtkscVaF_CPwelY1rpTLP-YrE7MTl7464Q_mrUxz4G6Gs0GVu1YBbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400ab8f284.mp4?token=OqSBcDCmZj-9veP7_wlvBB7vvuEcONgW0hPzdPNhd7PMn1n-IAcPbWPTEErvzPD2n_Qk6SrHrhI7l55cKn6XE_wzhQAyRUFlbF40P9ArC52rdNdMZ35PFt0g0f_TgBYReO8Mi6iwxDBwJ2AwEFoEx1AR6yP561g1cQlqqTj7rZ5qc_dHcY-VPQEUvQpCXe0wW4Zd_Sp-NT_5TvH3S5MEs_oiVcrfBW2c81VUzpp16dZ9PiFClq_nscRNS_5cofDlgrtw_PNXFzty0WTPauwg7Fgbi9C-H_iMtkscVaF_CPwelY1rpTLP-YrE7MTl7464Q_mrUxz4G6Gs0GVu1YBbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده اسرائیل یه استارلینک میبره برای نمایندهی ایران در صحن سازمان ملل و می‌گه اینو بگیر به کارت میاد. و می‌گه ما عاشق مردم ایران هستیم و برای تغییر رژیم دعا می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24081" target="_blank">📅 01:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24080">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7adc972c.mp4?token=VU3EK0vIsCI3wp3qN4AYepMdk1b6mgihLNxzuudWdQ_mpOHFIuAxe9c8aPnV37fT3oYXlguVXEGRcN4oRFZnTomzps2WUa98QLqHIzZlQvmTPXab3Ro2X2Mil42mNmgi0EZj7qEEX5EPVr6nz4azrIP_CCxJ6gqVBGAaLa6Tjd9vAo91QKciF9SULzJ5bu9Hd5qDYzF4GM8ANxAeHGCXDuuPowFuu0v2lNGAR7g3Hj8QgyIBdtigxwYUYKZNKr9VtfGVvNwCJJ7iznYaN8CDBcuG2s5uG8k4EFLKOVYfO5zpcmAUla9kDKhhmoIDvVNTLSh_uEWQPcGFOe5EKtlnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7adc972c.mp4?token=VU3EK0vIsCI3wp3qN4AYepMdk1b6mgihLNxzuudWdQ_mpOHFIuAxe9c8aPnV37fT3oYXlguVXEGRcN4oRFZnTomzps2WUa98QLqHIzZlQvmTPXab3Ro2X2Mil42mNmgi0EZj7qEEX5EPVr6nz4azrIP_CCxJ6gqVBGAaLa6Tjd9vAo91QKciF9SULzJ5bu9Hd5qDYzF4GM8ANxAeHGCXDuuPowFuu0v2lNGAR7g3Hj8QgyIBdtigxwYUYKZNKr9VtfGVvNwCJJ7iznYaN8CDBcuG2s5uG8k4EFLKOVYfO5zpcmAUla9kDKhhmoIDvVNTLSh_uEWQPcGFOe5EKtlnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان به فاکس‌نیوز می‌گوید مجتبی خامنه‌ای بسیار سالم است؛ «بعلهههه بسیار زیاد. کاملاً.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24080" target="_blank">📅 00:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مدیریت فرودگاه بین‌المللی نجف:
بر اساس دستور رسمی مراجع ذی‌صلاح، تمام پروازهای ورودی و خروجی از مبدأ یا به مقصد ایران از ساعت
۲:۰۰ بامداد جمعه ۳ مهر ۱۴۰۵
(۲۵ سپتامبر ۲۰۲۶) تا اطلاع ثانوی متوقف می‌شود. از شرکت‌های هواپیمایی و بخش‌های عملیاتی خواسته شده تا زمان اعلام رسمی، هیچ اقدام عملیاتی برای این پروازها انجام ندهند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24079" target="_blank">📅 00:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24078">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پرتاب دو موشک از نوع ابومهدی المندس ، از سیریک به سمت تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24078" target="_blank">📅 00:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24077">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیویورک‌پست:
سنای آمریکا بار دیگر طرحی برای محدود کردن اختیارات جنگی ترامپ در جنگ ایران را رد کرد؛ این رأی به معنای حفظ اختیارات فعلی رئیس‌جمهور آمریکا برای ادامه عملیات نظامی است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24077" target="_blank">📅 23:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش‌های تأییدنشده از شلیک دو موشک/پهپاد از ارومیه، به سمت اربیل عراق   @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24076" target="_blank">📅 23:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیویورک‌پست :
ارتش آمریکا در حال استفاده از
سامانه‌های لیزری
برای مقابله با برخی پهپادها و موشک‌های کروز و همچنین اهداف زیرساختی ایران در منطقه هرمز است. طبق گزارش این رسانه، هزینه شلیک لیزر به‌مراتب کمتر از استفاده از موشک‌های رهگیر عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24075" target="_blank">📅 23:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سازمان هواپیمایی کشوری امارات اعلام کرده پروازهای شرکت‌های هواپیمایی ایرانی
از امروز ۲۴ سپتامبر تا اطلاع ثانوی
به مقصد و از مبدأ امارات تعلیق شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24074" target="_blank">📅 23:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز ـ مذاکرات آمریکا و ایران وارد مرحله جدید شده:
منابع نزدیک به مذاکرات می‌گویند تهران و واشنگتن در نیویورک درباره یک
توافق مرحله‌ای
برای پایان جنگ مذاکره کرده‌اند؛ طرح مورد بحث شامل بازگشایی تدریجی تنگه هرمز در برابر کاهش یا پایان محاصره اقتصادی آمریکا و احتمال آزادسازی بخشی از دارایی‌های ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24073" target="_blank">📅 23:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مسئولان جمهوری اسلامی بعد از ترک سالون، عکس قاسم کتلت را روی میزشان قرار دادند. @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24071" target="_blank">📅 22:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjcFRfXp_t8pZEesMh6bRZAUXe4iXOYQ1K6sY7XRtHsdEXy8ZVlUN99M4MtyfZ4wjTGXizU-NIh8eq1qbkkn1AKhKeYXxoZH_gY9EyAqCU8coS1Lit_40pm26ERNHH1B0kJ_D0Fd4mQ77EusWlanX1kSzhzKlp1ylynob4oiuFe_bl51WkPBkmwGdJQjTdAxe1_QH36sS7C5XZLmWk8k1lVIsYfxNuqaEoXcXJqFvPg1tMHS5_onlS2b1mQcxzTRyO0bqJGtb7SUIavWN1lC-88dfgpZjzIxXYegG2VySi1gJj0y-n54EwXJhy4tBLTv37_tmLbU7ymUysWIO3zcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئولان جمهوری اسلامی بعد از ترک سالون، عکس قاسم کتلت را روی میزشان قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24070" target="_blank">📅 22:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24069" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24068" target="_blank">📅 22:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24067" target="_blank">📅 22:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24066" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24065">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نتانیاهو:
در طول قرن‌ها، حکومت‌های مستبدی که تلاش کردند ما را نابود کنند، بارها و بارها شکست خورده‌اند و به خواست خدا، همچنان شکست خواهند خورد. اگر شجاعت خود را جمع کنیم و عزم خود را جزم کنیم، به پیروزی ادامه خواهیم داد.
همان‌طور که در کتاب مقدس آمده است: «נצח ישראל לא ישקר»؛ یعنی «جاودانگی اسرائیل هرگز لغزش نخواهد کرد.» و دلیلش ساده است:
ما انتخاب دیگری نداریم.
از همه شما متشکرم.
חג שמח לעם ישראל
؛ عید بر مردم اسرائیل مبارک. متشکرم.خداحافظ
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24065" target="_blank">📅 22:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24064">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e66c6dc10.mp4?token=n_w7nwZLdeBfIooERgH-EZZXBEE06UKRUR_szVz_LcCBkWlN7ZjLJklxwKtNmPNNacJR99OtiTRuCDioHEPfkpAJANa114Ggy67_dcfOe5Ep6ji-A6hgSDiu4k_yhyqwYUBtC76FnGYD3k1MXT727YZnhed4fYOt1M-FJWaMVlgzG-19hoehYda4UPEHHXu__cpjjs2_-Kag_YyboW-SSGRtwJQ0H_58ihIo-UfJeNilTTfrxepqnO8KKhmLLOvFfrtaau6yh-tYZWa2-EhDiudZOGzXbWAPv8skCPyCcjLxkYSRQ9O-pRCvLbiC1vVtyWmCrJsThbiqH9o9-QLDIigd0RGw2FKI0-yvL0FPHpQ57xmcIMxK9X4mvjl5PRYfgX0uxQUD1l9qWsJ8QQBhydQKkDTpefzcQLXBHpup9qBHnl7spppvMbL9AwuzYjJfDi8GGXo5bjefc6eiNoEsK4MiCeyxLCcSdmR_wI4rYGJQfsgRheZw3JqYHBzh6lb8Lm5lYMM6dNG-CBsaZygyuq7wkDt6TbWJp0YeUEjhUzPXWi_ECEugbUzavbS6idzTNAks8d7xpTQbjtoQKbPixvzinX-F8sol4CyMoxXbk-LAjWHtAyzPTMq_dG_jXEmhD6_F7WztDQ6EeFOvddOuU_dHIykWSAdeESGzibHsROo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e66c6dc10.mp4?token=n_w7nwZLdeBfIooERgH-EZZXBEE06UKRUR_szVz_LcCBkWlN7ZjLJklxwKtNmPNNacJR99OtiTRuCDioHEPfkpAJANa114Ggy67_dcfOe5Ep6ji-A6hgSDiu4k_yhyqwYUBtC76FnGYD3k1MXT727YZnhed4fYOt1M-FJWaMVlgzG-19hoehYda4UPEHHXu__cpjjs2_-Kag_YyboW-SSGRtwJQ0H_58ihIo-UfJeNilTTfrxepqnO8KKhmLLOvFfrtaau6yh-tYZWa2-EhDiudZOGzXbWAPv8skCPyCcjLxkYSRQ9O-pRCvLbiC1vVtyWmCrJsThbiqH9o9-QLDIigd0RGw2FKI0-yvL0FPHpQ57xmcIMxK9X4mvjl5PRYfgX0uxQUD1l9qWsJ8QQBhydQKkDTpefzcQLXBHpup9qBHnl7spppvMbL9AwuzYjJfDi8GGXo5bjefc6eiNoEsK4MiCeyxLCcSdmR_wI4rYGJQfsgRheZw3JqYHBzh6lb8Lm5lYMM6dNG-CBsaZygyuq7wkDt6TbWJp0YeUEjhUzPXWi_ECEugbUzavbS6idzTNAks8d7xpTQbjtoQKbPixvzinX-F8sol4CyMoxXbk-LAjWHtAyzPTMq_dG_jXEmhD6_F7WztDQ6EeFOvddOuU_dHIykWSAdeESGzibHsROo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: شما درباره ایران هم سکوت کردید، اما من خبر خوبی دارم؛ با وجود این سکوت و آنچه من ریاکاری می‌دانم، روزی قدرت مردم ایران بر حاکمان آن غلبه خواهد کرد. ممکن است این روز چندان دور نباشد. مردم ایران روزی آزاد خواهند شد و رژیم حاکم، که من آن را سرکوبگر و جنایتکار می‌دانم، به‌دلیل دروغ، فساد و ظلم خود سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24064" target="_blank">📅 22:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24063">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو: به هیئت ایرانی توصیه می‌کنم این پیام را بشنوند تا اگر روزی از کشورشان خارج شدند، بتوانند آزادانه داستان خود را در شبکه‌های اجتماعی بازگو کنند. خطاب به معترضان حقوق بشر در خارج از اینجا می‌پرسم: وقتی حکومت ایران ده‌ها هزار غیرنظامی ایرانی را شکنجه و مجروح کرد و هزاران نفر از مردم خود را کشت، کجا بودید؟ آیا تجمع گسترده، اعتصاب غذا یا اعتراضی مقابل نمایندگی ایران در سازمان ملل برگزار کردید؟ درباره مسیحیان تحت آزار در ایران و خاورمیانه چطور؟ هیچ‌کدام
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24063" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24062">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو قول بر اندازی رژیم و جشن همگانی را داد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24062" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24061">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac08257aa.mp4?token=bv2lUI5NQhgRRSXE-9iUSei85bxn0WCumafYpDTQQxUfSqii8HgDwYA_lRFobcAvvnPypL0u4q8uIKxXrObCjjN41cAPxo_CeVJddf7Qqr33paiprMyhOBMw-FlAPlZ1b4sK_dfnTaw3os8M4DFRRZV8uuURq8fxX2-RreUKkDCLyv-hNadMKVTT7yxAPhPJ7Jc6kO_o20p0O7cXNHDwlidm_JWbwEkJnkXm1U3qgM_dvU6jk-nCwERI55QbApijcUCeZxjnApoLBGv5HEc3cZhHYpCR3en3_aap08h6xSso23VUXGfW8BMD_gXxlu9_u2smPEcA20iPkOb16ErfzHES_W2UiQ1wrCaxQT4h0fIK-xAdWsXj2onMjSttB-fCznXHr5NvWa5S6bujye6aydkoTbyoWymcpp045jMRw9uMNgUOP7N9xO4nXWkSuHCMg8s7HjeCrEk2gm2U1JAy82JgpF6v7otT0i6oqqAEBwOTw1T72EhDOtkjhrazf2qRPiAyWxrpb0fbKZA2cKgGOoYUN1dr1apXixGzcBV5Ddesz9hMe9DzK5kYN0LEMVQJPnw3FbJc4C3_WbsZjjCU9C2DCmRvtLUMhzEaduNdkc0sgrAOVD_rQh--e0K3VqB-p8yqkZGUsYy95MlslcEEjE7C0mDQrYeBAexATPDdY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac08257aa.mp4?token=bv2lUI5NQhgRRSXE-9iUSei85bxn0WCumafYpDTQQxUfSqii8HgDwYA_lRFobcAvvnPypL0u4q8uIKxXrObCjjN41cAPxo_CeVJddf7Qqr33paiprMyhOBMw-FlAPlZ1b4sK_dfnTaw3os8M4DFRRZV8uuURq8fxX2-RreUKkDCLyv-hNadMKVTT7yxAPhPJ7Jc6kO_o20p0O7cXNHDwlidm_JWbwEkJnkXm1U3qgM_dvU6jk-nCwERI55QbApijcUCeZxjnApoLBGv5HEc3cZhHYpCR3en3_aap08h6xSso23VUXGfW8BMD_gXxlu9_u2smPEcA20iPkOb16ErfzHES_W2UiQ1wrCaxQT4h0fIK-xAdWsXj2onMjSttB-fCznXHr5NvWa5S6bujye6aydkoTbyoWymcpp045jMRw9uMNgUOP7N9xO4nXWkSuHCMg8s7HjeCrEk2gm2U1JAy82JgpF6v7otT0i6oqqAEBwOTw1T72EhDOtkjhrazf2qRPiAyWxrpb0fbKZA2cKgGOoYUN1dr1apXixGzcBV5Ddesz9hMe9DzK5kYN0LEMVQJPnw3FbJc4C3_WbsZjjCU9C2DCmRvtLUMhzEaduNdkc0sgrAOVD_rQh--e0K3VqB-p8yqkZGUsYy95MlslcEEjE7C0mDQrYeBAexATPDdY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
این یک وسیله ارتباطی است؛
استارلینک
. ابزاری که به مردم اجازه می‌دهد به حقیقت دسترسی پیدا کنند، انتخاب داشته باشند و از آزادی اندیشه و آزادی بیان برخوردار شوند. به همین دلیل است که رژیم ایران از دسترسی مردمش به چنین فناوری‌هایی می‌ترسد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24061" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24060">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتانیاهو:
می‌دانید چه کسی می‌ترسد؟
مستبدان تهران.
و بیش از همه از چه چیزی می‌ترسند؟
از مردم خودشان؛ مردم شجاع ایران که برای مدت طولانی فداکاری کرده‌اند.
رژیم ایران به‌ویژه زمانی می‌ترسد که مردم ایران به ابزارهایی برای دسترسی آزاد به اطلاعات دسترسی داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24060" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24059">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو:
ما در اسرائیل منتظر نمی‌مانیم تا دیگران از خواب اخلاقی خود بیدار شوند. ما به پیش می‌رویم و در حوزه‌هایی مانند پزشکی، کشاورزی و هوش مصنوعی پیشرفت می‌کنیم و این نوآوری‌ها را در اختیار بشریت قرار می‌دهیم. اسرائیل هرگز قدرتمندتر از امروز نبوده و ما نمی‌ترسیم
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/24059" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24058">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتانیاهו: جهان باید بداند که حماس از غیرنظامیان فلسطینی به‌عنوان سپر انسانی استفاده می‌کند و از بیمارستان‌ها، مدارس و مساجد به‌عنوان مراکز فرماندهی بهره می‌گیرد. اسرائیل برای دور کردن غیرنظامیان از مناطق درگیری، میلیون‌ها پیام هشدار، تماس تلفنی و اعلامیه ارسال کرده است. اتهام نسل‌کشی علیه اسرائیل، به گفته من، «بزرگ‌ترین دروغ قرن» است؛ زیرا اسرائیل هم‌زمان با جنگ، یک میلیون واکسن فلج اطفال و دو میلیون تُن غذا برای مردم غزه فراهم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/24058" target="_blank">📅 22:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24057">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نتانیاهو: برخی کشورها میلیاردها دلار برای انتشار آنچه ما دروغ علیه اسرائیل می‌دانیم هزینه کرده‌اند.
قطر و ترکیه
از جمله کشورهایی هستند که به انتشار این روایت‌ها متهم‌شان می‌کنم. قطر سال‌ها از دانشگاه‌ها و رسانه‌هایی مانند الجزیره حمایت مالی کرده و ترکیه نیز تحت رهبری اردوغان بارها علیه اسرائیل موضع گرفته است. اردوغان خواستار نابودی اسرائیل شده و گفته است که می‌خواهد حاکم اورشلیم شود؛ اما این کشور و این شهر، پایتخت ابدی ماست
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/24057" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24056">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو: مردم اسرائیل در برابر هزار موشک بالستیک سنگین ایران که بر سر شهرها و غیرنظامیان ما فرود آمد، ایستادگی کردند. شما در سالن مجمع عمومی سازمان ملل نشسته‌اید؛ اگر تنها یک موشک بالستیک یک‌تنی به اینجا اصابت کند، می‌تواند کل این مجموعه را ویران کند و دو موشک از این نوع می‌تواند سازمان ملل را نابود کند. حال تصور کنید هزار موشک عظیم از آسمان بر سر شهرها و خانه‌های شما فرود بیاید. من به شجاعت مردم اسرائیل و سربازانمان، از یهودی و مسیحی تا دروزی و مسلمان، ادای احترام می‌کنم
@WarRoom</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/24056" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24055">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو: چرا پیروز می‌شویم؟ یوناتان نتانیاهو پاسخ را ساده بیان کرد: «ما انتخاب دیگری نداریم.» هدف ما در تمام این جنگ ثابت بوده است؛ پیروزی با اراده‌ای تزلزل‌ناپذیر و شجاعتی بی‌وقفه. این اسرائیل است؛ یک ملت با یک آینده مشترک، از چپ و راست، جوان و پیر، مذهبی و سکولار
@WarRoom</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/24055" target="_blank">📅 22:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24054">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو: در این نبرد با آنچه «بربرها» می‌نامیم، هیچ شریکی بزرگ‌تر از رئیس‌جمهور ترامپ نداشتیم. از او و رهبری جسورانه‌اش تشکر می‌کنم. او دهه‌ها پیش فهمید که اگر با رهبران افراطی ایران که شعار «مرگ بر آمریکا و مرگ بر اسرائیل» سر می‌دهند مقابله نشود، در نهایت به دنبال عملی کردن اهداف خود خواهند رفتاسرائیل و آمریکا در کنار یکدیگر برای حفاظت از خود و نجات تمدن اقدام کردند. خلبانان شجاع آمریکایی در کنار خلبانان اسرائیلی در مأموریت‌های مشترک بر فراز ایران فعالیت کردند. دو کشور همچنین برای بازگرداندن گروگان‌های باقی‌مانده همکاری کردند و همه آنها را به خانه بازگرداندیم
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/24054" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24053">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نتانیاهو: با وجود همه این رنج‌ها، تسلیم نمی‌شویم. «نریا» در آخرین نوشته خود پیش از حمله به او نوشته بود: «ما کشور دیگری نداریم؛ دفاع از آن یک افتخار است.» به نریا و همه قهرمانان اسرائیل قولی مقدس می‌دهم: فداکاری شما بیهوده نخواهد بود. ما به دفاع از کشورمان ادامه می‌دهیم و پیروز خواهیم شد، چون انتخاب دیگری نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/24053" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24052">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رسانه های عبری : نریا لیتر، پسر یحیئل لیتر، سفیر اسرائیل در آمریکا، در حمله با خودرو در ایست‌بازرسی مَکابیم در مسیر ۴۴۳ در کرانه باختری به‌شدت زخمی و به بیمارستان شعاری زِدِک در اورشلیم منتقل شد. راننده خودرو محمود محمد محمود سلیمان، ۲۹ ساله، ساکن روستای بیت‌عور…</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/24052" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24051">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو:
ای
امانوئل مکرون، همکارم، به این موضوع توجه کن: دو یا سه روز پیش، یک شهروند فرانسوی به نام ناتانیل شوکرون، پدر شش فرزند، هنگامی که همراه پسر ۱۶ ساله‌اش از یک چشمه بازدید می‌کرد، هدف گلوله قرار گرفت. یک تروریست حماس در یهودیه و سامریه از فاصله نزدیک به او شلیک کرد.
آخرین کلماتی که او بر زبان آورد این بود: «فرار کن، فرار کن پسرم، خودت را نجات بده.» این اتفاق سه روز پیش رخ داد
@WarRoom</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/24051" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24050">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتانیاهو:
سران تروریست‌ها و بزرگ‌ترین عاملان کشتار جمعی در جهان، نه‌تنها اسرائیلی‌ها، بلکه آمریکایی‌ها، بریتانیایی‌ها و شهروندان ده‌ها کشور را به قتل رساندند؛ خامنه‌ای، ضیف، سنوار، هنیه، نصرالله و هزاران تروریست دیگر که در پی نابودی ما بودند، همگی از بین رفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/24050" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24049">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو:
می‌دانید چه اتفاقی برای بخش عمده زرادخانه عظیم حزب‌الله، شامل حدود ۱۵۰ هزار موشک بالستیک و راکت که همگی برای هدف قرار دادن غیرنظامیان ما آماده شده بودند، افتاد؟ همه آنها از بین رفته‌اند. رهبران حزب‌الله کشته شده‌اند و روحیه آنها درهم شکسته است
@WarRoom</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/24049" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24048">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو:
ارتش، نیروی دریایی، نیروی هوایی و تأسیسات هسته‌ای ایران را هدف قرار دادیم. اسرائیل حماس را به‌شدت درهم کوبید و ما نیز حزب‌الله را به‌شدت درهم کوبیدیم. آن ضربه را به خاطر دارید؟ می‌توانم این را به شما بگویم: حزب‌الله قطعاً آن را به خاطر دارد
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/24048" target="_blank">📅 21:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24047">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو: دشمنان ما انتظار داشتند اسرائیل پس از ۷ اکتبر فروبپاشد، اما ما فرو نریختیم و جنگیدیم. طی سه سال گذشته، سربازان ما در یک جنگ هفت‌جبهه‌ای با حماس، حزب‌الله، حوثی‌ها، ایران، شبه‌نظامیان عراق و سوریه و گروه‌های مسلح فلسطینی در کرانه باختری جنگیده‌اند. همه آنها برای نابودی اسرائیل با یکدیگر همراه شدند، اما شکست خوردند
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/24047" target="_blank">📅 21:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24046">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو: به دنبال برادرم، یوناتان «یونی» نتانیاهو، رفتم که افسر ۲۱ ساله تیپ چتربازان بود و واحدش از قبل بسیج شده بود. وقتی او را پیدا کردم، از دیدنم شوکه شد. از او پرسیدم چه اتفاقی خواهد افتاد. مکث کرد و گفت: «ما پیروز خواهیم شد؛ انتخاب دیگری نداریم.» این…</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/24046" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24045">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتانیاهو: به دنبال برادرم، یوناتان «یونی» نتانیاهو، رفتم که افسر ۲۱ ساله تیپ چتربازان بود و واحدش از قبل بسیج شده بود. وقتی او را پیدا کردم، از دیدنم شوکه شد. از او پرسیدم چه اتفاقی خواهد افتاد. مکث کرد و گفت: «ما پیروز خواهیم شد؛ انتخاب دیگری نداریم.» این جمله را هرگز فراموش نکردم
@WarRoom</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/24045" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24044">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نتانیاهو: اسرائیل کشوری بسیار کوچک است؛ مساحت آن حتی به یک‌سوم یک درصد از کل سرزمین‌های جهان عرب نمی‌رسد. با این حال، ما را به استعمار متهم می‌کنند؛ آن هم از سوی کشورهایی مانند بریتانیا و فرانسه که خود سابقه استعمار گسترده دارند. این هم یک دروغ دیگر است
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/24044" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24043">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو: در بین کسانی که سالن را ترک کردند، کشورهای بودند که در خفا برای نابودی قدرت هسته‌ای ایران از ما تشکر کردند؛ و این نهایت تزویر و ریا است.
اگر هنوز بزدلانی هستند که اتاق را ترک نکرده‌اند، از آنها می‌خواهم همین حالا بروند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/24043" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24042">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو: تخریب تاسیسات هسته‌ای ایران بسیار سخت بود، اما برای من یکی از آسان‌ترین تصمیم‌هایی بود که گرفتم
من به آقای احمد الشرع سوریه ای می‌گویم که یهودیان از زمان موسی در بلندی‌های جولان بوده‌اند و اگر جرعت داری علیه جولان اقدام کن.
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/24042" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24041">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو:۱۴ سال پیش گفتم مانع این میشم که جمهوری اسلامی به سلاح هسته‌ای برسه و ما دقیقا این کار رو کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/24041" target="_blank">📅 21:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24040">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتانیاهو : ما باید ببریم هیچ راه دیگه ای نداریم
حاضران : تشویق
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/24040" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24039">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینستاگرام بی بی رفت لایو</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/24039" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24038">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765c13dc80.mp4?token=kxtHQRsccBqOx-bEti46RZSlBi816egVXuWDFL9YJYxN_C6LKGurumpxLuWqXwDJoA0OqQpYtoXEMftis_YZaRoqlYuxb9Pyb4pe9FfW2Ri7J_1RpR8lKyAFYzZ1r3y6GyhqoxFY43pW0L2jlhWz-MWAXX9QnDInv_MV3RMU5aCh4dLgu3VYCoUweO4LIm2BCXsFWFHH_LKl9kW1JFb5g83X7N5oI62WfpLfyOm-nMNlBE2JooOqZynAGD912Zyikuhwn-ApCxtSyQ9AaTVPJ4P47djvmVq4BtXF2OjyYXHGsoqGwveFGm2vRPXwOvs0aQ2emcfEOAwHWLvDoBNY4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765c13dc80.mp4?token=kxtHQRsccBqOx-bEti46RZSlBi816egVXuWDFL9YJYxN_C6LKGurumpxLuWqXwDJoA0OqQpYtoXEMftis_YZaRoqlYuxb9Pyb4pe9FfW2Ri7J_1RpR8lKyAFYzZ1r3y6GyhqoxFY43pW0L2jlhWz-MWAXX9QnDInv_MV3RMU5aCh4dLgu3VYCoUweO4LIm2BCXsFWFHH_LKl9kW1JFb5g83X7N5oI62WfpLfyOm-nMNlBE2JooOqZynAGD912Zyikuhwn-ApCxtSyQ9AaTVPJ4P47djvmVq4BtXF2OjyYXHGsoqGwveFGm2vRPXwOvs0aQ2emcfEOAwHWLvDoBNY4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/24038" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24037">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شروع نکرده گفت ایران داره بمب میسازه</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/24037" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
