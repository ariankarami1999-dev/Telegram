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
<img src="https://cdn4.telesco.pe/file/QaZrj4j7IHBWdnWc5zb17TD0_5x83v10LU0ZZ37IEEyCllzE1OPW36p5tmyuUFRnK_GjktDpjCExQiDouwLiAzT71RbCXAYblhsUvSu-CJOeW2hV5Qlz3vyOZbmQz4AUtSYrtdgBkCq7fJgcPHeyzo0xflgVSN2R4SOpjyfTWHeQr8VXZTFYgPBp0Y4r8CR_Wnf2ZRUXyM-5G7XhA7mFp6y7GFEskWlUtrE9KVdjNzXjTB5X2VbVSVgZ1Jyck7h0Vnq-bKGktv3x0SLqiBx60OT9GJyBcf9e0FMvjqHmzXUHjB4d8tMgfvzfpyO46uOAvYfST9__z-0uALpVz387RQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 16:05:54</div>
<hr>

<div class="tg-post" id="msg-19740">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صدا و سیما
:
جمهوری اسلامی بارها هشدار داده است که هرگونه عواقبی که ناشی از انحراف کشتی‌ها از مسیر اعلام‌شده توسط ایران باشد، مسئولیت آن بر عهده‌ی آن کشتی‌ها خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/withyashar/19740" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19739">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرگزاری وابسته به رژیم :
سخن از هدف قرار گرفتن سه فروند کشتی تجاری و نفت‌کش در میان است؛ دو فروند در باب‌المندب و یک فروند در تنگه هرمز. ایران در حال بازی با اعصاب ترامپ است و احتمال دارد قیمت نفت در زمان بازگشایی بازار به ۱۱۰ دلار برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/19739" target="_blank">📅 15:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19738">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یک منبع آگاه وابسته به رژیم : کمی پیش یک نفتکش متخلف در تنگه هرمز که از مسیر مشخص شده توسط جمهوری اسلامی خارج شده بود، بعد از برخورد با مین دریایی منفجر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/19738" target="_blank">📅 15:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19737">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/withyashar/19737" target="_blank">📅 15:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19736">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ادعای منبعی عربی به نقل از مقامات آمریکایی و اسرائیلی: نشست ترامپ و نتانیاهو، زمان عملیات مشترک علیه ایران را تعیین خواهد کرد.
مرحله اول این عملیات، بر تاسیسات هسته‌ای متمرکز نخواهد بود و تا 10 روز ادامه خواهد داشت.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/19736" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19735">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کریم خان دادستان کل دیوان کیفری بین‌المللی ، که حکم بازداشت نتانیاهو، نخست‌وزیر اسرائیل، و گالانت، وزیر دفاع سابق، را صادر کرده بود، پس از اتهامات سوء رفتار جنسی از سوی یکی از کارمندان سابق، توسط کشورهای عضو با رأی قاطع برکنار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/19735" target="_blank">📅 14:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19734">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سوأل شما : ترامپ رئیس قوه مجریه است، اما همه چیز را نمی‌تواند شخصاً جابه‌جا کند. معاون رئیس‌جمهور یک جایگاه انتخابی در قانون‌اساسی است که برای تغییر ونس ، پای کنگره و مقررات صریح قانون اساسی وسط می‌آید ؛ تنها راه‌های عملی برای رفتن او، استعفا، مرگ، یا در موارد خاص فرآیندهای قانون اساسی و رأی کنگره است
@WarRoom</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/19734" target="_blank">📅 14:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19733">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نیکزاد، نایب‌رئیس مجلس :اقدام نابخردانه دولت اوکراین درهدف قراردادن کشتی ما بی‌جواب نمی‌مونه
@WarRoom</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/19733" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19732">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سازمان دریایی بریتانیا یک گزارش جدید در جنوب دریای سرخ دریافت کرده است.
گزارش شده که یک نفتکش در نزدیکی خود، برخورد/اصابت موج آب ناشی از یک پرتابه ناشناس را مشاهده کرده است. گزارش‌ها تأیید می‌کنند که کشتی و خدمه در سلامت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/19732" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19731">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کانال ۱۴ : منابع تأیید شده گزارش می‌دهند که جی دی ونس شایعات و نگرانی‌ها در مورد ذخایر مهمات ایالات متحده را دامن زده است. در صورتی که اگر مشکلی بود وزیر جنگ باید این را عنوان کند
@WarRoom</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/19731" target="_blank">📅 14:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19730">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گرندپری فرمول یک بحرین به کشور مالزی منتقل شد : دلیل جنگ ایران و آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/19730" target="_blank">📅 14:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19729">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شورای اتحادیه اروپا پنج قاضی دادگاه‌های انقلاب و یک هکر ایرانی را که می‌گوید در «نقض جدی حقوق بشر» دست داشته‌‌اند در فهرست تحریم‌های خود قرار داد.
«مصطفی نریمانی»، رییس شعبه سوم دادگاه انقلاب کرج؛ «ابوالفضل عامری شهرابی»، قاضی شعبه ۱۱۹۱دادگاه تجدیدنظر کیفری تهران و معاون پیشین دادستان اراک، «مهدی راسخی»، قاضی شعبه سوم دادگاه انقلاب رشت، «محمدرضا عموزاد»، رییس شعبه ۲۸ دادگاه انقلاب تهران و قاضی مشاور شعبه ۱۵، «محمدرضا توکلی»، رییس شعبه اول دادگاه انقلاب اصفهان پنج نامی هستند که به‌دلیل محاکمه اقلیت‌های مذهبی و مخالفان سیاسی توسط شورای اتحادیه اروپا در فهرست تحریم‌ها قرار گرفته‌اند.
اتحادیه اروپا همچنین «نیما صالحی» را به دلیل همکاری گروه هکری «آشیانه» با پلیس فتا و سپاه پاسداران و نقش این گروه در حملات سایبری علیه مخالفان داخلی و نهادهای خارجی و کمک به سرکوب جریان آزاد اطلاعات، تحریم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/19729" target="_blank">📅 14:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19728">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">العربیه: منابع آگاه گزارش دادند که واشنگتن و تهران پاسخ‌های خود را به پیشنهاد پاکستان و قطر برای از سرگیری مذاکرات ارائه کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/19728" target="_blank">📅 14:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19727">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from❤🦁💚</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJok1OI0LMlMcHWk_pIm9nSlY_NBmyT53H2TktSIn8QUGjPTSLpITXFnmxE5jeacRjG4lIfuHAwX0zNqoriuy2ZycRJ_IUZJh_LVoTWHfYZxvUFzFGcgmaMO7uIBd2jWIUvJcoLxVp5sGBW_KxG3v6kTbYdXrnZ2YoKeY5GT58VUU200C8IppNOKnnDrUEn4H5poqx6Nq7QjTQpZOpSNlHnNAwTqe4JtpAM7L4mmCVDyDBz-uRw6zrlq7-7COjGUVXnbvnUn5q65_PVzX5oy27cZWA_9RX_W7pQxnVCJ8P_BPN6HgoHypccXc8yLOpHcPwo7huvp-xZ3suq-rMtOYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار داداش دیشب سنگ قبر رفیقم طاها نادری رو جاوید نام شهرضا رو شکستن حروم زاده ها دارن سنگ قبر جاوید نام ها رو تو این شهر میشکنن حروم لقمه ها از قبر هم هراس دارن ولی روز انتقام نزدیگه</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/19727" target="_blank">📅 14:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19726">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کاخ سفید: در مورد ایران هنوز همه گزینه‌ها روی میز است
در پی گزارش رسانه‌های آمریکا که دونالد ترامپ فعلا از تشدید عملیات نظامی علیه ایران منصرف شده است، کاخ سفید تاکید کرد که همچنان «همه گزینه‌ها» در مورد ایران روی میز است.
@WarRoom</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/19726" target="_blank">📅 14:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19725">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjzBKSgz8M8DkMSiEnH7mowSo5KXYNQ8Nkhn8fKDm-xrvPhyBE0Nc6QTm54f8QoUwc8FVuQbLTmK_ZxkkKlJB7pM9QKAQoc44cKXJqb9FMBNj55rCDvJiTlvZOfqJmF1fJUTPhDawSedAZV71Nj63kmxY2za_OAtmi36ihucaYc-tYVtd9_osMxENsJL3X7D95oFXd_c_0FgV8Fq9SVYHVIzhVESPWKY4w9s_ooePH6OZNUFS39YWfNje_fTAgRn4G0IFHjmIG-6s889LC_8eRKOHQ_I4MFeGUGlHDhTbKImcdujofHG7N6lLrKss6fQ4fZDO_tvjMk43DJKYkIG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:این هفته با ترامپ ملاقات خواهم کرد تا درباره تمام موضوعات، از جمله ایران، گفتگو کنیم. @WarRoom
🚨
🚨
🚨
🚨
یاشار : آلبوم جدید داره میبره رو کنه
😁</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/19725" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19724">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتانیاهو:این هفته با ترامپ ملاقات خواهم کرد تا درباره تمام موضوعات، از جمله ایران، گفتگو کنیم.
@WarRoom
🚨
🚨
🚨
🚨
یاشار : آلبوم جدید داره میبره رو کنه
😁</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/19724" target="_blank">📅 13:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19723">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y42wzKKbDiXMeOcl8zwnVjJzhsPIVmVSJSHq0n-j6CKlJYPphJ6Qnja6KCApXIp8cTvXgnVEhY-IpIUJYlSWuqImIIidU2tILuYNmhfw2xmF9WMiZNcDCTbBcryDfp-dal_G7agZ57_HS_Lo3QPU93wam_0X2DzAELfhVmJOMG7bpcjzmEXjCQacDHMvNtYOnzVFRLOf6ZrAdZ9P5TOcSrrV3F-6h1nY0w32IoP-J0S6LVD689KMzbXehADpCT71oHhGgIPW_ZchLt4X93mxVc7Zju9NSH_mxxUFlhD9LWG--OcqfgHBag-GGmCZzVsoN00snnA9FpdV0LACMi9i4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن شرتی و غول برره که به مرده ها هم  رحم نمی‌کنند و پریدن توی‌ کادر زیر تابوت اکبر عبدی و بلند میگویند الله اکبر.
@WarRoom</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/19723" target="_blank">📅 13:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19722">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw4jSYI5-N47siZ4tmpDIIhGsw57p-5lakNFx5JneBOoT4JgFHnVP8E6UmOXHHSWQZ2NjZHn46AhLCCmRfwKwIQOkLv0gFc0ocv0aFl754v4gvnHrDHJ1eSWVN7NC2pPwMW7kGPJOUs8_x_kqdVOl8LShVFLa5NDVVUzcE-Pfyx8byrgNJqoPNr9IBSW6zsc2k_JIGOHcDpEJx3hEgSU8pkk_y4Ml5JqBLHkf1SpxHQP_9dxQC_9mmL4lHPvJC0CdQGzPNeYlYlSs_yljr3lDlFF29sdPVMy0xWWMCh-f45r-oLUIZWWDYVm-BFXIJ-j8-uKGPs-Ax4MkRAE2I0pSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از وقوع حادثه‌ای در جنوب دریای سرخ دریافت کرده است. به UKMTO گزارش شده است که یک نفتکش شاهد پرتاب یک پرتابه ناشناخته در نزدیکی کشتی بوده است. گزارش‌ها تأیید می‌کنند که کشتی و خدمه در سلامت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/19722" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19721">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هم اکنون هدف قرار گرفتن یک کشتی دیگر در دریای سرخ
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/19721" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19720">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سخنگوی ارتش: با توقف حملات آمریکا، عملیات تلفافی‌جویانه را متوقف کردیم
ما برای تمام سناریو ها آمده ایم
@WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/19720" target="_blank">📅 12:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19719">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ویدیو انیمیشن بسیار زیبای تحلیل فرضیه حمله به کوه «کلنگ گزلا»زیر نویس فارسی هم زدم ، از دست ندید
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19719" target="_blank">📅 12:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19718">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات سابق و کارشناسان هسته ای گزارش داد، اگر دونالد ترامپ، رئیس جمهور آمریکا حملات آمریکا به ایران را گسترش دهد، واشنگتن می تواند چندین تاسیسات هسته ای باقی مانده را فراتر از کوه کلنگ هدف قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19718" target="_blank">📅 11:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19717">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تلگراف: وزیر دفاع انگلستان قصد دارد روابط با دولت ترامپ را بازسازی کرده و همکاری‌های امنیتی را تقویت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19717" target="_blank">📅 11:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19716">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یِوگن کورنیتشوک، سفیر اوکراین در اسرائیل، در گفتگو با N12 به حمله به یک کشتی ایرانی در دریای خزر اشاره کرد: "کشتی که در دریای خزر مورد حمله قرار گرفت، قطعات مربوط به پهپادها و موشک‌هایی را حمل می‌کرد که در راه ایران بودند، نه کالاهای غیرنظامی، همانطور که ایران ادعا کرد. این اولین باری نیست که به اهداف نظامی این‌چنینی حمله می‌کنیم، و البته می‌توان انتظار داشت که دوباره به آن‌ها حمله کنیم. از نظر ما، این یک هدف نظامی مشروع است."
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19716" target="_blank">📅 11:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19715">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCnoEbbwuvXAE5ysbkN40RR3G4aZT_h8tbobqeVQ3O5BlJNqDIIY1uPL_9QQtEC0qZZtUUubsZs69uRJ_aFFlwYHTwq3sukLIEdO3IZSpXrKDkwwZ4EHwNLsOGyTgNAW-ePonbUaMg6npBBFvOXCSxu_3B0RprS-WyS8JO560WJ5zVLn7_iUY-MJGKFZixag0fhP-5Ia9FHQOVjS0XJ_8wFt-i15Oer7XamLYIBMnF5f8Vp6hCJAOWxBeBz8DM6jf_TpwuJXYTp0XT3eWkF8AyTnahbhhg2-7qc0ubKUtkTLzhmisG3tQIZEsTe5r4l9MklEZCXAbCL6-0qypAbWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون حداقل ۱۷ فروند هواپیمای ترابری نظامی آمریکا از نوع C-17 و C-5M و سوخترسان در حال رفت و آمد به خاورمیانه هستند
@WarRoom
دیروز خبر فیکی مبنی بر پایان نقل و انتقالات پل هوایی آمریکا پخش شده بود !</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19715" target="_blank">📅 10:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19714">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">امروز چهارم مرداد؛ سالروز درگذشت رضاشاه کبیر پدر ایران نوین
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19714" target="_blank">📅 09:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19713">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صدا و سیما :
‏ سناریوهای احتمالیِ آمریکا در مقابل ایران
سخنگوی ارتش
: یکی از راهبردهای آمریکا خروج از جنگ است البته اگر اسرائیلی‌ها اجازه بدهند.
سناریوی دوم
اینکه تحت فشار اسرائیلی ها عملیات هوایی گسترده انجام دهد. یا انجام عملیات زمینی.
‎
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19713" target="_blank">📅 09:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19712">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به گزارش سی‌بی‌اس نیوز، مذاکرات عمان و ایران برای بازگشایی تنگه هرمز پیشرفت‌های مثبتی داشته، هرچند رسیدن به توافق نهایی نیازمند زمان است. همزمان با سفر روز جمعه مقامات عمانی به تهران، آمریکا نیز برای جلوگیری از اختلال در این روند حساس دیپلماتیک، بمباران‌های ۱۳ روزه خود را عمداً متوقف کرد؛ موضوعی که کاخ سفید و سنتکام حاضر به اظهارنظر درباره آن نشدند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19712" target="_blank">📅 09:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19711">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شبکه کان اعلام کرد که اسرائیل امروز تمدید وضعیت اضطراری را تا ۱۱ آگوست (۲۰ مرداد) به دلیل اوضاع در ایران و لبنان تصویب کرد. همچنین در مورد سفر نتانیاهو به آمریکا گفت: نتانیاهو فردا به واشنگتن سفر خواهد کرد و روز سه‌شنبه باترامپ درباره موضوع ایران گفتگو خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19711" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19710">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شان پارنل، سخنگوی ارشد پنتاگون در بیانیه‌ای به سی‌ان‌ان گفت: «ارتش آمریکا قدرتمندترین ارتش جهان است و هر آنچه را که برای اجرای عملیات در زمان و مکان مورد نظر رئیس‌جمهور نیاز دارد، در اختیار دارد.»
«ما عملیات‌های موفقیت‌آمیز متعددی را در سراسر فرماندهی‌های رزمی اجرا کرده‌ایم، در حالی که اطمینان حاصل می‌کنیم ارتش ایالات متحده دارای زرادخانه‌ای عمیق از توانمندی‌ها برای محافظت از مردم و منافع ما است.»
@WarRoom
part5 final cnn</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19710" target="_blank">📅 09:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19709">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بر اساس گفته چندین منبع‌ به سی ان ان، افراد کمی در حلقه نزدیکان ترامپ یا در داخل پنتاگون بر این باور بودند که گزینه‌های رئیس‌جمهور برای تشدید تنش، نتایج مورد نظر او را به همراه خواهد داشت.
پیش از آغاز جنگ، کین و سایر رهبران نظامی به ترامپ هشدار داده بودند که یک کمپین نظامی طولانی‌مدت می‌تواند بر ذخایر تسلیحاتی آمریکا تأثیر بگذارد(استراحت بین حملات لازمه برای پر کردن ذخایر)
@WarRoom
part4</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19709" target="_blank">📅 09:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19708">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به گفته یک منبع آگاه، تا بعدازظهر جمعه، دولت ترامپ هنوز در حال بررسی این موضوع بود که تشدید احتمالی تنش چگونه خواهد بود. این منبع گفت که کشورهای حاشیه خلیج فارس در گفتگوهای اخیر خود با مقامات دولت خواستار خویشتن‌داری شده‌اند، اما اذعان کرده‌اند که ایالات متحده توانمندی‌های منحصربه‌فردی دارد که در صورت تمایل می‌تواند از آن‌ها برای تشدید درگیری استفاده کند.
@WarRoom
part3</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19708" target="_blank">📅 09:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19707">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">استیون چونگ، مدیر ارتباطات کاخ سفید، در بیانیه‌ای گفت:
«با توجه به ترکیب تحریم‌های موفقی که اقتصاد ایران را فلج کرده و ۱۳ روز پیاپی حمله به اهداف نظامی در پاسخ به تجاوزات مکرر آن‌ها، عاقلانه است که ایران برای رسیدن به یک توافق مذاکره‌شده تلاش کند. در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
@WarRoom
part2</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19707" target="_blank">📅 09:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19706">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک منبع آگاه و یک مقام آمریکایی به سی‌ان‌ان گفتند که جی‌دی ونس، معاون رئیس‌جمهور، و ژنرال دن کین، رئیس ستاد مشترک ارتش، هر دو در جریان نشست روز جمعه در کاخ سفید و در حالی که رئیس‌جمهور دونالد ترامپ در حال بررسی این احتمال بود، نسبت به تشدید جنگ در ایران ابراز نگرانی کردند.
@WarRoom
part1</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19706" target="_blank">📅 09:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19705">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ به LCI : توقف موقت حملات به معنای عقب‌نشینی نیست, برای انجام حمله گسترده علیه ایران آمادگی کامل داریم!
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19705" target="_blank">📅 09:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19704">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزارت امور خارجه: گفتگوهای ایران و عمان درباره تنگه هرمز که در تهران برگزار شد، سازنده و مفید بود.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19704" target="_blank">📅 08:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19703">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2743288b5.mp4?token=PXmFXVudkdvdIWIGLEytlNhIccnFoh7ebUu-SePaqBHpTjX5LmFoRA5nqRRoYE1j4O0OJ3ThMX7Bokaf9bLqbKGJDX5i_m0ZlhDQcIJDqGPZfG3IIRJEMdN6iuSah5T9DRW5yiWUsoKS_xJcGgh-jsdquJSRGkswPPaYhf7eC67KkxysRYPbP1lEMb5dJSHbLMQeaUTSQvTa5GyzHj5B_WiGZdbPnekxn79kJ9VoeFUYcBoJZ49UrUyDVcHc6lx0tsnLHHETZF7nWWmL_nHnAHjKXb6zkXC1M4NMAT42egjAO_ah73c0oW4aitv82Fl5TsClASGGs9-QyoKMMlKvnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2743288b5.mp4?token=PXmFXVudkdvdIWIGLEytlNhIccnFoh7ebUu-SePaqBHpTjX5LmFoRA5nqRRoYE1j4O0OJ3ThMX7Bokaf9bLqbKGJDX5i_m0ZlhDQcIJDqGPZfG3IIRJEMdN6iuSah5T9DRW5yiWUsoKS_xJcGgh-jsdquJSRGkswPPaYhf7eC67KkxysRYPbP1lEMb5dJSHbLMQeaUTSQvTa5GyzHj5B_WiGZdbPnekxn79kJ9VoeFUYcBoJZ49UrUyDVcHc6lx0tsnLHHETZF7nWWmL_nHnAHjKXb6zkXC1M4NMAT42egjAO_ah73c0oW4aitv82Fl5TsClASGGs9-QyoKMMlKvnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاصره دریایی ایالات متحده علیه ایران همچنان به طور کامل برقرار است. از ۲۵ ژوئیه، سنتکام ۱۲ کشتی تجاری را که سعی در عبور از محاصره داشتند، تغییر مسیر داده، ۲ کشتی را که رعایت نکرده بودند، غیرفعال کرده و ۲ کشتی دیگر را برای اطمینان از رعایت کامل محاصره، سوار بر آنها کرده است.
اوایل امروز، نیروهای آمریکایی عملیات تأیید ورود به کشتی M/T Charminar با پرچم کومور را در دریای عرب تکمیل کردند و این نفتکش اکنون به سفر خود ادامه می‌دهد.
نیروهای سنتکام، M/T Lavine با پرچم موزامبیک را در ۲۴ ژوئیه در خلیج عمان غیرفعال کردند، پس از آنکه خدمه چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران در حال حرکت نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19703" target="_blank">📅 03:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19702">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک پهپاد در نزدیکی منزل ایتمار بن گویر، وزیر امنیت ملی اسرائیل، سقوط کرده است ، جزئیات در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/19702" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دریای قزوین
😁</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/19701" target="_blank">📅 23:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارت امور خارجه ایران:
ما محکوم می‌کنیم اقدام دولت اوکراین مبنی بر حمله به یک کشتی تجاری ایرانی در دریای قزوين«خزر»که امروز صبح رخ داد. این حمله منجر به انفجار کشتی و شهادت یکی از ملوانان و زخمی شدن ملوان دیگری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/19700" target="_blank">📅 23:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19699">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کانال ۱۴ : ترامپ دستور توقف تمام حملات به ایران را صادر کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/withyashar/19699" target="_blank">📅 22:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانال 12 : بنیامین نتانیاهو تصمیم دارد در نشستی در کاخ سفید، اطلاعاتی درباره پیشرفت برنامه هسته‌ای ایران را در اختیار ترامپ قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/19698" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زلنسکی : ما دریافتیم که ماهواره‌های روسی به تهران در حمله به مناطق خاورمیانه کمک می‌کنن
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/19697" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19696">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری وای‌نت : قطر و عمان ،رژیم تهران را تحت فشار گذاشتند تا سازش کند و از یک عملیات تقریبا قطعی و بزرگ آمریکا جلوگیری کند
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/19696" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19695">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ممد باقر : حملات ما به اهداف آمریکایی در منطقه، تا زمان تسلیم کامل دشمن و به عنوان انتقام خون کودکان بی‌گناه در میناب، لامرد و سایر مناطق، ادامه خواهد داشت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/19695" target="_blank">📅 21:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19694">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🥛
امشب دوغ  میزنمااااااا</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19694" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19693">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ , تلفنی به یک خبرنگار از شبکه فرانسوی LCI:
اگر از ایران ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19693" target="_blank">📅 21:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19692">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ : آمریکا «آماده حمله گسترده» به ایران است (کانال ۱۴)
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19692" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19691">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19691" target="_blank">📅 21:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19690">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی سپاه: در طی ۱۵ روز نبرد، نیروهای مسلح ایران ۱۱ فروند جنگنده و بالگرد آمریکایی را در پایگاه‌های منطقه و روی زمین منهدم کردند؛  شامل یک F-15، یک P-8، یک C-17، هشت هواپیمای سوخت‌رسان و ۱۷ پهپاد شناسایی و عملیاتی.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19690" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19689">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ایلان ماسک: در سیاست زیاده‌روی کردم!
بهتر بود به جای دخالت در امور اجرایی واشنگتن، تمام تمرکز خودم را روی مدیریت شرکت‌هایم می‌گذاشتم.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19689" target="_blank">📅 21:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19688">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رادیو و تلویزیون اسرائیل:
در حال حاضر بیش از 90 هواپیمای سوخت رسان آمریکایی در اسرائیل مستقر شدند، موشک های رهگیر پدافند به صورت گسترده در حال ورود به اسرائیل می‌باشد، هواپیماهای ترابری آمریکایی بدون وقفه وارد اسرائیل می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19688" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19687">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شبکه
I24News:اسرائیل برای یک حمله گسترده از سوی آمریکا در پایان این هفته آماده‌سازی می‌کرد، اما این حمله اتفاق نیفتاد. تخمین‌ها نشان می‌دهد که آتش‌بس فعلی موقتی است و هدف آن فراهم کردن زمینه برای گسترش دامنه عملیات نظامی در آینده است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19687" target="_blank">📅 21:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19686">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19686" target="_blank">📅 21:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19685">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXcLZKpXegyD9m662fXUdxgekGyMixyoBNutlf8Cqvt_yZY08UK8xnucYIPSOogBrYIAU3ANAEVveWhgvE5LE47yXzu1B3_ZWdYyFEzcGfAIZJ6gzHxqIHDAmbIdsWUGo4JTIv_6xL9jPv5RWjVlAGgOKvQueP09dEuX0C3OvObooPdbtqlvl3ilXeMtyRHO6u6adCWXlva6LPLQGKKmcXVzcBuAlrEYa2EafOhEtWI3rNqzYkvsPVOECGl4hfaziASQQSe4bMQSbjemDU6nevtxMfTMyfQ3REpb1tYq_pP15xc635Q_RTwytn9UWGHMO2CPFPZInTv3tmoLphGnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقال مجروحان آمریکایی از اردن و کویت با هواپیمای C-17 گلوبمستر به بیمارستان نظامی آلمان؛ مقصد نهایی مرکز پزشکی لنداشتول
بر اساس گزارش‌های منتشرشده، شماری از نیروهای نظامی آمریکایی که در جریان حملات اخیر در منطقه خاورمیانه زخمی شده بودند، پس از دریافت مراقبت‌های اولیه در پایگاه‌های منطقه‌ای، با هواپیمای ترابری ـ پزشکی
C-17 Globemaster III
نیروی هوایی آمریکا برای ادامه درمان به آلمان منتقل شدند. مقصد این انتقال،
مرکز پزشکی منطقه‌ای لنداشتول (Landstuhl Regional Medical Center)
در ایالت راینلاند-فالتس آلمان بوده است؛ بیمارستانی که سال‌هاست به‌عنوان مهم‌ترین مرکز درمانی ارتش آمریکا در خارج از خاک این کشور برای پذیرش مجروحان جنگی فعالیت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19685" target="_blank">📅 20:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19684">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19684" target="_blank">📅 20:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19683">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromَ</strong></div>
<div class="tg-text">یاشار جان سلام خسته نباشی اول از همه مرسی از زحماتی که میکشی ، من المان زندگی میکنم بعد ما رفتیم بیمارستان ارتش مخصوص کسایی که زیر نظر بیمش هستن فامیلمون عمل لازم بود قبولش نکردن گفتن تو حالت اماده باش هستیم پرسیدیم برا چی بخواطر جنگ خاورمیانه گفتن اره  هرچی خواستیم ازش جزئیات بیشتری بگیریم گفتن محرمانه هست هیچ جوابی بهمون ندادن</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19683" target="_blank">📅 20:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19682">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیویورک پست: ایران در هفته‌های اخیر دفاع خودشو به‌شدت تقویت کرده و برای سناریو حمله زمینی آماده شده
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19682" target="_blank">📅 20:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19681">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19681" target="_blank">📅 20:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19680">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دو شرکت زیرمجموعه لوفت‌هانزا آلمان پروازهای تل‌آویو را تا سه‌شنبه لغو کردند
این تصمیم در پی ادامه نگرانی‌های امنیتی و ارزیابی وضعیت منطقه اتخاذ شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19680" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19676">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سفارت آلمان و فرانسه رسما شایعه تخلیه کارکنان خود را تکذیب کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19676" target="_blank">📅 20:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19674">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19674" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19673" target="_blank">📅 20:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19672">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19672" target="_blank">📅 20:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19671">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKUJig2z8wTnGo_K896_U1c1f3U1bVg8eOT-VMZjm6a9NRweh5etpDeTnKHyaUPntTW6xvtFMydM12tOBQpJpi2bdpjyt06zkoUnnPslRJXwykkIni-1AryHeLozt7NFDwCjoVm_Xmq5tORCG8VHGh4JXsB4WPXhOXKaTXFIBlWI3S1d0584AmkO7ZmkMb1h8AL58TcRLPzDOkfUA0kvYytwGXrP9vZT4PFBPgllGEZyJNk7bzL2TP2hoMndLqo2y8QXiLfs-xBJ9vD2mtBD_uGbNMTT7t2wLQjvcyPoUf8iMS9-XuqpZ4IyCHvhuxw2oFOTLhEGKH4AplBeIxMmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ریزه کاری هایی داره ولی خیلی سخت بود تا این بشه ، سلیقه داداش رو که قبول دارید
😎</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19671" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19670">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19670" target="_blank">📅 19:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19669">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حمله به یک نفتکش در نزدیکی عربستان
سازمان عملیات تجارت دریایی انگلیس از اصابت یک پرتابه به نفتکشی در ۷۰ مایلی ساحل الشقیق عربستان خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19669" target="_blank">📅 19:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19668">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ3Rh-BFi4nKLZVLTnpetXvdA89iTZ9-_VlOCriTtBflscCMhd6elp1cQKWmtvl9zX5WoPcKVNlHoCkmD9LP-i_sct6pHAnS0cnCKiHwXfZZWgZNTxpIwbGiXQNKd61c1ugiog-s3ikQ1vkVyf3qq4_YkU1ArfQqEq1TBtwfEvBewpXb4gKjYNkFqvStbKtgBOmTpOipTWUH-un-llZOScU6-giPA2msgyhLpMZhq7uomP9Hni_NqKKOftCqmeJiGegaZBaV5_LyI8rySwXSDN8aVapdAApTaRz4eHRCDgEM8yHrqiKilfpuk7rmU6lagwW67lvpB8SYVZnsMt33eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یک هواپیمای آواکس E-3 Sentry در فرودگاه جده فرود آمد
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19668" target="_blank">📅 19:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19667">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U29wrCktO1-HqvP7IOXMVHOhivCAuNE2AnTxvU13WqiIpG84Unhek7M672Plcnar0gD3BX1g_F4cU9iDYZ8ugg7QW5TeV_hxZK5OWhFiWqGGRBTGMUhY0h2RL73e5cFCFh_T2-aLOgxsOcTaXM9Zb9mhLSOyS1nC1t1SQwpF9nitboXpnD-Vw7X3itXbgpR3feBdBudhs9VU7qtYanLMQqCxFrN-L7_V8kO7pBdE3incnsKUUCVB2qSrGlubeGneNDmIas3ufJG-n0isJpwoReMNacOLqtaYhJGcKL5JGo1BU0utbwQOReZz7V-8_41gBEOfN5X9jHRzoJPIkbue7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ سوخترسان هم اکنون در آسمان اردن
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19667" target="_blank">📅 18:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19666">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اکسیوس با رد خبر رسانه‌های عبری:
آمریکایی‌ها دیروز برای یک عملیات گسترده‌تر علیه ایران آماده نشده بودند، بلکه برای حمله‌ای با همان حجم و ابعاد حملاتی آماده شده بودند که در دو هفته گذشته هر شب انجام شده بود
.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19666" target="_blank">📅 18:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19665">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به گزارش کانال ۱۲: آماده‌باش در سطح بالا در اسرائیل برقرار است؛ آنها منتظر تصمیم ترامپ در مورد آینده رویارویی با ایران هستند, همچنین شرکت‌های هواپیمایی خارجی لغو پروازهای خود به مقصد و از مبدأ اسرائیل را آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19665" target="_blank">📅 18:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19664">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وای نت : ترامپ قرار بود دیشب یک حمله بسیار گسترده به ایران انجام بده ولی وسط کار نظرش عوض شد و تصمیم گرفت فعلا به ایران فرصت بده تا مسیر دیپلماتیک جواب بده!
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19664" target="_blank">📅 18:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19663">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏وزارت حمل‌ونقل قطر اعلام کرد از روز ۲۶ ژوئیه، تردد تمامی کشتی‌ها و شناورهای دریایی به طور کامل از سر گرفته می‌شود. با اجرای این تصمیم، همه محدودیت‌های اعمال شده بر فعالیت‌های دریایی لغو شده و عبور و مرور در آب‌های قطر به وضعیت عادی بازمی‌گردد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19663" target="_blank">📅 17:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19662">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تلگراف : یک مقام ایرانی ناشناس، بریتانیا را تهدید کرد و هشدار داد که در صورت مشارکت این کشور در جنگ به همراه آمریکا، مقر نخست‌وزیر هدف قرار خواهد گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19662" target="_blank">📅 17:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19661">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وال استریت ژورنال: موشک‌های خیبرشکن ایرانی با ترکیبی از مسیر‌های پروازی، مانور‌ها و سرعت‌ها، سامانه‌های پدافند هوایی را گیج می‌کنند
این موشک‌ها بسیار ارزان‌تر از رهگیرهایی هستند که برای انهدام آن‌ها استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19661" target="_blank">📅 17:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19660">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اکسیوس: طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است @WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19660" target="_blank">📅 17:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19659">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz1suJlgJZkhS2hXAftP95lT2soDN8YZUgZKjzj3TDcg0yU5K3WJX4dRRS3qrogh1mV5QAZlxQXUZAW_3FuuirVUQdAcuSYAsWlHicr9XaI57FXgZd5oxj3ERueBptHRnPHWF__a7t7Rr4nzDlh2bskAyCUayo1VsZjYPNZwkU5EQgz87Jb_1bsEMBavcaplsIzWSsLGYW0Ui39izr2x31j8C6rxK53bcRYaXgtmXhOuj4H3B9yfSIMJIopacsV7njPbgD24tWfQM5iHxvvyGg33GmccPjcd_wmIgEtallpanMiSGm7J5jQIT_ylLF0Y79bvHC_xCM4KWRCNvxHwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسال سنگین تجهیزات و مهمات به اردن فقط در همین لحظه ۴ هواپیما C17 در‌ مسیر رفت و برگشت ! نشان میده آمریکا در حال کشیدن کامل کمان «فول دراو» است
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19659" target="_blank">📅 16:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19658">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ورودی جدید
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19658" target="_blank">📅 16:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19657">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH</strong></div>
<div class="tg-text">الان جدی جدی آمریکا قبول کرده ایران فقط تنگه رو باز کنه و پولم بگیره؟؟</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19657" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19656">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اکسیوس: طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19656" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19655">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9083629166.mp4?token=coIfFj5yWPo0zmERTqHv_UGJvmT_OT1YZnNpf7HsX8V5C4ncBwSA-C7796HQDPM6djEhJ7IbJpDjwbC7mqXl246X76A5bbc6adQ4GqMW_2pH_6szciN_DLI3EPrtll8P2DziaDCR1Ta_YGBbtZyxF6CLHxlMCIuoBvsnHMtFwTWgW5xJVY9YMlSEDElPo-O47lxegg8xpcfUQHujs-3XYhDkV6kwVtmRCfIh-_GPmCRxNwbca9sZgu_WFGuG5eYclhd-Np4EbmNaBWnXNdmH4PtjStu9cjU7DDWQBB3H1MBo0mLRzzg-pdYU2BMyfuqi7adkyjA72sM6g57EANYWTTwq2xpF3oY8sqZ-Wfdy4DG_PQPxv3Y0OC7DnZqdOW-ngKcHoN_ZUvW2BBYdO7h2l_BP3fvgRfBybOrRZu7Gj1N48xXa4HuzMhD3tTJNe8p9mCjMPcqwoThtscxpg12Zi2X_DNlGdqduulAzRFvrnfVd77M505zWo7n6uCE2nRJX5PU0L_Nr39n1wRxCICED68LBVEfRXpWZtpDn_DlTr341i2gs7Q7zk_TiSw16llGDbDZQOh6r3JgiuEiN3-jWsBkoOJm_tZPbYGzpZi4goYzuEUKwBq0WOpcHndCknQFRrLDpJ08Nv8wFgwEMbXC-YXrKtvLl7WlllF5Fx0kN7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9083629166.mp4?token=coIfFj5yWPo0zmERTqHv_UGJvmT_OT1YZnNpf7HsX8V5C4ncBwSA-C7796HQDPM6djEhJ7IbJpDjwbC7mqXl246X76A5bbc6adQ4GqMW_2pH_6szciN_DLI3EPrtll8P2DziaDCR1Ta_YGBbtZyxF6CLHxlMCIuoBvsnHMtFwTWgW5xJVY9YMlSEDElPo-O47lxegg8xpcfUQHujs-3XYhDkV6kwVtmRCfIh-_GPmCRxNwbca9sZgu_WFGuG5eYclhd-Np4EbmNaBWnXNdmH4PtjStu9cjU7DDWQBB3H1MBo0mLRzzg-pdYU2BMyfuqi7adkyjA72sM6g57EANYWTTwq2xpF3oY8sqZ-Wfdy4DG_PQPxv3Y0OC7DnZqdOW-ngKcHoN_ZUvW2BBYdO7h2l_BP3fvgRfBybOrRZu7Gj1N48xXa4HuzMhD3tTJNe8p9mCjMPcqwoThtscxpg12Zi2X_DNlGdqduulAzRFvrnfVd77M505zWo7n6uCE2nRJX5PU0L_Nr39n1wRxCICED68LBVEfRXpWZtpDn_DlTr341i2gs7Q7zk_TiSw16llGDbDZQOh6r3JgiuEiN3-jWsBkoOJm_tZPbYGzpZi4goYzuEUKwBq0WOpcHndCknQFRrLDpJ08Nv8wFgwEMbXC-YXrKtvLl7WlllF5Fx0kN7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرچی‌ میشکنی‌ بشکن ، ولی دل مارو نشکن
@WarRoom
💃🏼
🕺🏻</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19655" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19654">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیویرک پست : آمریکا در حال بررسی طرحی برای تصرف اورانیوم غنی‌شده از تاسیسات هسته‌ای ایران است. این طرح به اعزام هزاران نیروی زمینی، خنثی‌سازی تله‌های انفجاری و استقرار یک نیروی دفاعی بزرگ در اطراف سایت‌ها نیاز دارد. سپس یک تیم کوچک از نیروهای ویژه عملیات اصلی تصرف را انجام می‌دهد. این مأموریت بسیار خطرناک و از نظر لجستیکی پیچیده توصیف شده است. گفته شده ارتش ایران تا حد زیادی تضعیف شده، اما هنوز از نظر تجهیزات از نیروهایی که مادورو را محافظت می‌کردند پیشرفته‌تر است. این طرح فعلاً در حد بررسی است و تصمیم نهایی درباره اجرای آن اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19654" target="_blank">📅 15:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19653">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صداوسیما: اهالی جاسک اسلحه‌ به‌ دست منتظر آمدن نیروهای آمریکایی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19653" target="_blank">📅 15:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19652">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: نتانیاهو در 48 ساعت آینده به آمریکا سفر خواهد کرد و در کاخ سفید دیدار خواهیم داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19652" target="_blank">📅 15:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19651">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تلگراف : جمهوری اسلامی از شبکه‌های قاچاق مهاجران در کانال مانش برای انتقال برخی افراد مرتبط با نهادهای اطلاعاتی به بریتانیا استفاده کرده است.
مقام‌های بریتانیایی چند نفر مشکوک را هنگام ورود با قایق‌های کوچک شناسایی و متوقف کرده‌اند. برای ردیابی این افراد از پهپادها و برج‌های نظارتی مجهز به هوش مصنوعی استفاده شده است. بخشی از این شبکه‌ها با سپاه پاسداران و به‌ویژه واحد ۷۰۰ نیروی قدس در ارتباط بوده‌اند. یک مقام ایرانی گفته «افراد انقلابی» در لندن مستقر شده‌اند و مسیرهای قاچاق را از موشک‌ها مؤثرتر دانسته است.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19651" target="_blank">📅 15:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19650">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زلنسکی : ما با حملات دوربرد در دریای خزر  از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی به نتایج بسیار قوی دست یافتیم.
از این نتایج متشکریم! افتخار برای اوکراین!
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19650" target="_blank">📅 14:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19649">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حمله عربستان به مأرب و الجوف در یمن
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19649" target="_blank">📅 13:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19648">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وای نت به نقل از مقامات اسرائیلی: بعد از آزادسازی تمامی گروگان ها، دست اسرائیل برای انجام حذف هدفمند در غزه زیاد شده و اینکار با شتاب بیشتری انجام خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19648" target="_blank">📅 13:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19647">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الجزیره : چراغ سبز عراقچی به شروع مذاکرات
عراقچی: پس از بروز تنش‌هایی در هرمزگان، در جریان مذاکرات سوئیس، تصمیم گرفتیم یک خط ارتباط مستقیم ایجاد کنیم تا از بروز سوءتفاهم‌ها جلوگیری شود.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19647" target="_blank">📅 13:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19646">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرده است که گزارشی درباره وقوع یک حادثه میان یک نفتکش و نیروهای نظامی مهاجم در خلیج عمان دریافت کرده است @WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19646" target="_blank">📅 12:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19645">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjbbde3ZOne__Ylwi_1dgVBRh9a3cAruyE_hKGlew2-I36ewIxb8d5FR35R44ixCl1zVTUC7TE2oO9GNdTQGP1exdiCdHRaovqJH_ROOugw9NnvpMohoRuwwvy3jB05f611jYtYKPMJhJg8p3WIyQn8BD8GcPJ22iRKy2ow_XT6amnqs3Hh2qsjFgOtPTX-qCIiP6T-ZxyB3HtWpQMEW0gfnCtHAAVEJLSLDgDNAqPEr0AjXZle4lYqejoQnN6serQuNcIT1Jn9nqeHtDwlpOsiRbuK0CfYb71KGq3CpGytOc50fZLgqiDRbm-2C7ImucAAivdGOM7MoxK-503cm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرده است که گزارشی درباره وقوع یک حادثه میان یک نفتکش و نیروهای نظامی مهاجم در
خلیج عمان
دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19645" target="_blank">📅 12:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19644">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19644" target="_blank">📅 12:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19643">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DizdVGNVgC90fnk_Y0nIEgFRTU7jXnygkv0lVARgpb8jfv9neZ93XXGi8HNjGT_J9UKvXm7XniPl9oSQubBYpSIYgaRziyX9598GjCrRXqF4zYXEkhhonWHlDUh9lAtor7tjGvHKwlMHdHVEVL7rlDtNXboSttdcVno_59h3JJj6uWYQBbnaJAaf0YxS0m_N9ddxA0k9-cMtJHC2JtuXWEHG-g1GljV3xAahwlyJodVdurylU2IH4Fc6bALImUzz6B8fMX6rJAd7gXOZch8wgHlTOb3Bxjp8eRtLIoM0UzYMJGYaehET1mqh53d__iKVWIgrXcRDTkxcSEuGVHYOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین لحظه برای اولین بار‌ آشکارا یک هواپیمای
C-17 Globemaster III
یکی از مهم‌ترین هواپیماهای ترابری راهبردی نیروی هوایی آمریکا و ستون فقرات جنگ با توانایی حمل ۷۷ تن بار در حال انتقال  تجهیزات/مهمات احتمال زیاد برای کرد ها در اربیل عراق است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19643" target="_blank">📅 12:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19642">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فاکس نیوز: جی دی ونس امروز در جلسه شورای امنیت ملی در کاخ سفید شرکت نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19642" target="_blank">📅 10:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19641">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سی‌ان‌ان: پس از ۱۳ شب پیاپی ، روز جمعه هیچ خبری از حمله به ایران از سوی سنتکام منتشر نشد
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19641" target="_blank">📅 09:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19640">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QySjIyKkcWjdhytb-2cSTVKpDda84rzi82DXppslyFy9juf8QFzZj1Ysq8P4d0azoSYhgsYa-iihjFDOPVP-xeEHs7pQzve_KQ0BEe2BBOVTjs3MC7YoFzoumekuFwHV-Lm2JHxiYL5bYPLs6QkzG-oTaIAXM_F7QcU9AD_5g0CE8L_bc-wpW-9po_OZY401qowcfEhlAI9tka0GmkKfLZdaRxxA5g06NJ_YTSlhSAS2Zngg-1qL9O6F6K7TlBXrjob43cU09ecPz4srZOBwJQYp9WY9Vrwyn0DmKvYQdX0MKl0Fht0CCJy26GD4x9F3QaGbs5sV5l4S4oGL4GsbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : عکس باراک راوید خبرنگار ارشد آکسیوس به همراه تیم این خبرگزاری در مراسم شام کاخ سفید که بخش بزرگی از اخبار این جنگ را پوشش میدن و ما رو سرویس کردند ، دیشب اصلی ها نبودند که حمله رو پوشش بدهند ، در جنگ آمریکا و اسرائیل با ایران، رسانه‌ها فقط نقش اطلاع‌رسانی نداشتند، بلکه به یکی از میدان‌های اصلی نبرد تبدیل شدند. انتشار سریع اخبار، تصاویر، عملیات روانی، روایت‌سازی، جنگ اطلاعاتی و تلاش برای تأثیرگذاری بر افکار عمومی، همگی بخشی از این نبرد بودند. در چنین جنگی، گاهی یک خبر یا روایت می‌تواند به اندازه یک حمله نظامی بر روند تحولات اثر بگذارد
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19640" target="_blank">📅 09:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19638">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5168a521.mp4?token=pXQTz7LTIIU9RFmoxdZU2MRNCc6FBFZ1crdIEO2oHCVYFte1VEs2uq4VKZPJT9Mu_t8VMOSUiXz0eJkaqSRItGp93f-8sAeR_RxUyt4Jwl2qVCwwfurLtzzNh2e1upTBi9A1KonTSkt30MZ8jTCShYMbLvyqGHsPihNDm4nsntDoNA4sQUWSkoWe9-ehW9cIPMYG9FyrqvH9pFmdjU7OGWB7Ov_iDQsa4H85T8eBDltkBCo3ktY2aoO_XGngIV-nLQ5jR92k_94x2i5lcvsrzr9ZBcs3auW7EpUXagzIkP2wNW8Vifq8U8btBmc7IyN5wsD3cvEoD5u25MtoM3k0FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5168a521.mp4?token=pXQTz7LTIIU9RFmoxdZU2MRNCc6FBFZ1crdIEO2oHCVYFte1VEs2uq4VKZPJT9Mu_t8VMOSUiXz0eJkaqSRItGp93f-8sAeR_RxUyt4Jwl2qVCwwfurLtzzNh2e1upTBi9A1KonTSkt30MZ8jTCShYMbLvyqGHsPihNDm4nsntDoNA4sQUWSkoWe9-ehW9cIPMYG9FyrqvH9pFmdjU7OGWB7Ov_iDQsa4H85T8eBDltkBCo3ktY2aoO_XGngIV-nLQ5jR92k_94x2i5lcvsrzr9ZBcs3auW7EpUXagzIkP2wNW8Vifq8U8btBmc7IyN5wsD3cvEoD5u25MtoM3k0FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تیراندازی در ضیافت شام رئیس‌جمهور ترامپ در کاخ سفید @withyashar</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19638" target="_blank">📅 09:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کلش ریپورت : فرماندهی مرکزی آمریکا امشب هیچ حمله‌ای علیه ایران انجام نداد؛ احتمالاً به‌دلیل برگزاری شام انجمن خبرنگاران کاخ سفید و سخنرانی ترامپ در این مراسم.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19637" target="_blank">📅 09:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ در مراسم شام انجمن خبرنگاران کاخ سفید (WHCA):
«برای مثال، در دوران دولت من، آن رژیم(خامنه ای اول)که زمانی همه از آن می‌ترسیدند و بی‌وقفه به آمریکا حمله می‌کرد، سرنگون شده است. رهبران سابقش برکنار شده‌اند و حالا توسط یک دیکتاتور گِی (خامنه ای دوم) اداره می‌شود و با اختلافات داخلی دست‌وپنجه نرم می‌کند. اما من به نوبه خودم برای باری وایس در CBS News بهترین‌ها را آرزو می‌کنم.»
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19636" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
