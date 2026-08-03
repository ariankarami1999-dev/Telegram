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
<img src="https://cdn4.telesco.pe/file/WU6BpnzJYukzp2zzjJTQE0Pe3Lisl0capAPMOHOYSMzCXTWTgoCetx5HslCwz09o7BrpZlAtryWTwFuE4y5SaJVDHXfMNF6QwzfgDZeIcZ2fmBDJMnuG4KEn8OA7Ot-bNBTTcxHLCuElcVH1b1onk5w6_pgEJ-y-PPGKYBBMJhczm-kSvlPhTXhfgxf5xAVRur3-4att_Qa3JFs_7UzqnQAKQxYhKugbjLu3Qemon35ZQNB8-OSjztq3a4mo6TF4hWKqU9I6s9SCfUh-8J2ESqo5ZzAtHESXHO8Tp9gXyEVe8WmbRnbyhfbrUs8PW8rUSPhY7fw38lMDDia4t9xOXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 20:14:56</div>
<hr>

<div class="tg-post" id="msg-19621">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:
رهبران ایران به طرز باورنکردنی‌ای ریاکار هستند! آن‌ها درخواست ملاقات می‌کنند، برخی می‌گویند "تمنا می‌کنند"، مذاکرات آغاز می‌شود، و جلسات بیشتری در آینده نزدیک برنامه‌ریزی شده است، و در عین حال، به صراحت و با افتخار اعلام می‌کنند که هیچ بحثی در جریان نیست، هیچ موضوعی مورد گفتگو قرار نمی‌گیرد، و آن‌ها فقط با "عمان" در ارتباط هستند.
سپس، آن‌ها به سخنان همیشگی خود ادامه می‌دهند و ادعا می‌کنند که تنگه هرمز به طور کامل توسط آن‌ها کنترل خواهد شد، در حالی که در حال حاضر، این تنگه به طور کامل تحت کنترل نیروی دریایی ایالات متحده و "محاصره" ما، یا همانطور که برخی می‌گویند، "دیوار فولادی ایالات متحده" است.
هیچ چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ چیز نخواهد رسید، مگر اینکه یک توافق حاصل شود، یا ایران به طور کامل تسلیم شود. چه ایران این را بپذیرد یا نه، در واقع، ما در حال بررسی راه حلی برای مشکلی هستیم که آن‌ها برای دهه‌ها ایجاد کرده‌اند.
این موضوع بسیار ساده است: ایران هرگز سلاح هسته‌ای نخواهد داشت!</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SBoxxx/19621" target="_blank">📅 19:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19620">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پاکستان وجود هر گونه مذاکره ای میان ایران و آمریکا را رد کرد.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/19620" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19619">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تصویر نگران‌کننده بازار کار ایران.
بر اساس تازه‌ترین نتایج طرح آمارگیری نیروی کار مرکز آمار ایران، اقتصاد کشور در بهار امسال حدود
۴۵۰ هزار شغل
را از دست داده است. همچنین
۶۲۹ هزار فرصت شغلی در بخش صنعت
حذف شده و شمار قابل‌توجهی به جمعیت بیکاران افزوده شده‌اند؛ آماری که از تشدید بحران در بازار کار حکایت دارد.
﻿
همچنین مرکز افکارسنجی دانشجویان ایران (وابسته به جهاد دانشگاهی) اعلام کرده است که
معیشت بیش از ۳۲ میلیون ایرانی
به‌صورت مستقیم یا غیرمستقیم به پایداری اینترنت وابسته است؛ موضوعی که اهمیت دسترسی پایدار به اینترنت را در اقتصاد و اشتغال کشور نشان می‌دهد</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/19619" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19618">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نتانیاهو:
ما باید روابط خود را با متحدان بیشتری تقویت کنیم.
به همین دلیل است که من سرمایه‌گذاری زیادی در رابطه خود با هند انجام می‌دهم، با دوستم نارندرا، که یکی از بزرگترین دوستان ماست.
برخی می‌گویند اسرائیل منزوی است. اما حمایت‌هایی که اسرائیل – و من شخصاً – در هند دریافت می‌کنم، واقعاً شگفت‌انگیز است.</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SBoxxx/19618" target="_blank">📅 18:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19617">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتانیاهو:
اکثریت قاطع مردم ایران، اسرائیل را تحسین می‌کنند.</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/19617" target="_blank">📅 18:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19616">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Geomarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">324.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19616" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 17</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/19616" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19615">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجار در دوبی همراه با یک کشته و 5 زخمی</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/19615" target="_blank">📅 17:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19614">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqQMrXVyHqp9Dww3TSfKv3TKYnR6s-r6zRHOmGzvCt9oA8Jcpu4f2WXJt6RbBqcb9F-r31gyK9lDM2cihXHvV9kVeAgvSlNEJtdxMlzthovF1N_e--N4Ji6NTD7a-YzOrs_mnJRv-QIoDFXBA3NBROpksj7AYSK2THRVgE-b9zVxS265JNr3D-PS0oC5-OAXVM-sRe9TUQMVqwBFwFVbtvyr_2kV9uXSZzuf3MrL7-qtztlgcK0f6GWnw3Ywi8_oTPczYncIxYi1oUJx6ADzuiZHb48A8Q394td1kEikCcFVs1ila59I9umn5FaBAw5QRnMzDkRr7B0mpD-zKe2srA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا بسته‌شدن 20 درصد صادرات نفت جهانی منجر به افزایش 80 درصدی درصدی قیمت شد؟
بسته شدن تنگه هرمز فقط به معنای حذف ۲۰ درصد از عرضه نفت نیست؛ بلکه ظرفیت مازاد تولید جهان را نیز از بین می‌برد و با از بین رفتن انعطاف‌پذیری بازار، حتی یک شوک محدود می‌تواند جهش بزرگی در قیمت نفت ایجاد کند.
علاوه بر این، بازار نفت ریسک‌های آینده مانند گسترش جنگ، اختلال در تأمین نفت جایگزین، محدودیت اوپک‌پلاس، مشکلات پالایش نفت سنگین و معاملات اهرمی را نیز پیش‌خور می‌کند؛ عواملی که مجموعاً جهش شدید قیمت‌ها را رقم می‌زنند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/19614" target="_blank">📅 17:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19613">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ:
مایک ویرث، رئیس هیئت مدیره و مدیر عامل شرکت شرون، همین‌اکنون در مصاحبه‌ای با ماریا بارتیرومو که فوق‌العاده است، تمام دلایل موفقیت شرکتش را بیان کرد.
تنها چیزی که او به‌طور مصلحت‌آمیز فراموش کرد ذکر کند این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و خود کشور ما مرده بود!
به عنوان مثال، آن‌ها مایک و شرون را از ونزوئلا بیرون انداختند، اما اکنون آن‌ها بازگشته‌اند، بسیار بزرگتر و قدرتمندتر از هر زمان پیشین، و انتظار دارند ثروتی عظیم کسب کنند!
این موضوع برای سایر شرکت‌های نفتی نیز صدق می‌کند... و همین حالا قیمت‌های مصرفی (خرده‌فروشی) نفت را پایین بیاورید!
بابت توجه شما به این موضوع سپاسگزارم.</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/19613" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19612">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">المیادین:
ایران پیشنهاد بازگشایی تنگه هرمز تا پایان کامل جنگ را رد کرد.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/19612" target="_blank">📅 17:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19611">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گادی آیزنکوت در مورد ایران:  در مورد ایران، یک هدف برتر و دو هدف بسیار مهم دیگر وجود دارد. هدف برتر، حذف حدود ۴۴۰ کیلوگرم اورانیوم غنی‌شده از ایران است.  اگر این کار انجام نشود، ایرانیان می‌توانند با تصمیم خود، به سمت سلاح هسته‌ای پیش بروند. این چه معنایی…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/19611" target="_blank">📅 16:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19610">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6c5fe91f.mp4?token=tbfwYUBXvox-wsP_vFecLg96XXYx60nfnZ8FjshOApc76LetHUdXU1WgxmhOZ3-SF7UH9vuXmNVjsfcrVEHgsMTp3hTG_s9I1fEXvig3Yxt35dneX1g5BAwopGwZuP2yQZCB9p_qyeZ2VgAT1iQOBBaltNG2jPvhe0i1hHvNr5zEK-jOw9PycrFjgLaPHQSe8jVxOqNg1r1kwONfbMJrc0xbtszZYEn-xFp8XZgK5YtEyklF0QMI10LKbKrxLDG3k95JlW9VwkhGqiTn3Ix43tCJW0HlK12J1druptQTUIEBdswvl-1jMdM2bJ9bCYFctoCBH9S2_an3j_2EW8Hr2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6c5fe91f.mp4?token=tbfwYUBXvox-wsP_vFecLg96XXYx60nfnZ8FjshOApc76LetHUdXU1WgxmhOZ3-SF7UH9vuXmNVjsfcrVEHgsMTp3hTG_s9I1fEXvig3Yxt35dneX1g5BAwopGwZuP2yQZCB9p_qyeZ2VgAT1iQOBBaltNG2jPvhe0i1hHvNr5zEK-jOw9PycrFjgLaPHQSe8jVxOqNg1r1kwONfbMJrc0xbtszZYEn-xFp8XZgK5YtEyklF0QMI10LKbKrxLDG3k95JlW9VwkhGqiTn3Ix43tCJW0HlK12J1druptQTUIEBdswvl-1jMdM2bJ9bCYFctoCBH9S2_an3j_2EW8Hr2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های خارجی گزارش می‌دهند که یک مقام ارشد فرماندهی مرکزی ایالات متحده (سنتکام) هفته گذشته ایمیلی را برای گروه بزرگی از تحلیلگران ارسال کرد و در آن نوشت:  «ما به دنبال راه‌های جدید، نوآورانه و غیرمتعارف برای تحت فشار قرار دادن ایران و مجازات آن هستیم.»…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/19610" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19609">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6aAkB7lpWdfj8JAvzC8CqLFy9ePW5KJMWmg3qKg0NiZbi_hRAWXsNx3JwqyvA0Buc4nHIubIDilzQdZ2DpGpY19SopdmUY6TAs8bnaUSk9WjwAtPOp1SD1eyU9CDbgqiK165w7feaJJb9Lk_zBDs5AbL-on1bN3n1xsPXnx4X_P5UMYOMTw4mEi435rSwuK1LRT2FnT6Di2bL8vDOfiIdey0vBOzSGe56bPs6eGCF_eQbGDSnKK6h11w6xsmjCWIoxyiEfQ6CBj58MO991_sE0CaAXSj38vlXRZlPHQlw0kdqe7fp5616uGb0E1cT7uIIQKQlqg6kWZsVzr3128RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسناد فاش‌شده نشان می‌دهند که شرکت اسرائیلی "ال بیت سیستمز" (Elbit Systems)، فعال در زمینه تسلیحات، به دنبال انعقاد قراردادهای تسلیحاتی به ارزش تا 1.3 میلیارد دلار با امارات متحده عربی بوده است، که شامل پهپادهای پیشرفته "هرمس" و سیستم‌های اطلاعاتی می‌باشد.
منبع: هارتز (Haaretz)</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/19609" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19608">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:  در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.  گزینه‌های نظامی واقع‌بینانه در نظر گرفته…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/19608" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19607">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:
در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.
گزینه‌های نظامی واقع‌بینانه در نظر گرفته نمی‌شدند. رویکرد غالب، آشتی با رژیم بود. اگرچه بسیاری از سیاستمداران ترکیه در کارآمدی آشتی تردید داشتند، اما این مسیر در حال پیگیری بود.
ترکها همچنین می‌ترسیدند که اگر یک تهاجم نظامی شکست بخورد، روسیه با حملات هوایی گسترده به مناطق تحت کنترل مخالفان پاسخ دهد و موج دیگری از پناهندگان را به ترکیه که خود با بحران پناهندگی روبرو بود، وارد کند.
حتی کشورهای عربی - به جز قطر - در حال پیگیری عادی‌سازی روابط با رژیم بودند. هدف تأیید آنچه اسد انجام داده بود نبود، بلکه دور کردن سوریه از نفوذ ایران و کاهش خسارتی بود که به منطقه وارد می‌کرد.
عملیات نظامی با وجود آن نگرانی‌ها آغاز شد. این کاملاً تصمیم خودمان بود.
منبع: الجزیره</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/19607" target="_blank">📅 15:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19606">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 17</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 17
دوشنبه 3 آگوست 2026</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/19606" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19605">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIh6rHP5rCsBMgVjo8r6jSNKy2ucVLxpfKYFqqnnKLdkqUXRAzjg_OpWzYit5docyZcDzbtHDTTOJJBiX6WKA9Zf4k5ERd7_lk6Tf2RfrdsqNIffOV0jUnK1o4ml849q1IWmB2Ay8KUxurUAaXvetS3A36Z0VCmF_DK3xGETnagv0aZ0noTpZy5gg7k5pG-fL4IZNSRHmkqzkBiTkFfTuyHyetq2RRoy_t8woUFk6tT-cm6ma7IThePWP32EuPJECQdDp7p53xPraMWW8ipWY2eCqlI75qfu5xb--qwpPQB2MWeWIG397PC_XKnfu_fr1RVUPIhYp8gZnr98pc9cUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رنکینگ مسخره ضریب هوشی کشورهای جهان را ناموسا رها کنید!
اگر میانگین ضریب هوشی ما واقعا چهارم دنیا بود باید سطح رفاه و توسعه اقتصادی ما هم دستکم در ۱۰ کشور برتر جهان قرار میگرفت (کشورهای دیگر صدر جدول را بییینید) نه اینکه رییس جمهوری مثل پزشکیان داشته باشیم که سطح ادراکش از توسعه برق این است که برود آستین کوتاه بپوشد و یک لامپ خاموش کند!</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/19605" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19604">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/19604" target="_blank">📅 12:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">توضیحاتی درباره روند تکامل صنعت دفاعی اوکراین و پیآمدهای خطرناک درگیری با این کشور برای ایران  #ژئوپولیتیک   لینک مقاله مرتبط</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/19603" target="_blank">📅 12:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19601">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رسانه‌های خارجی گزارش می‌دهند که یک مقام ارشد فرماندهی مرکزی ایالات متحده (سنتکام) هفته گذشته ایمیلی را برای گروه بزرگی از تحلیلگران ارسال کرد و در آن نوشت:
«ما به دنبال راه‌های جدید، نوآورانه و غیرمتعارف برای تحت فشار قرار دادن ایران و مجازات آن هستیم.»
این اقدام نشان‌دهنده درک این موضوع است که گزینه‌های موجود در حال حاضر برای دولت ترامپ محدود هستند و ممکن است از نظر سیاسی یا نظامی قابل قبول نباشند، که این امر ضرورت بررسی راهبردهای جایگزین را ایجاد می‌کند.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19601" target="_blank">📅 12:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19600">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUborIMjQD8qc80cXd8F2_MOLA99Xy4HTwbkPH7GMUxsPFX1Yac29Up2mhOuGAsB17wvF9cmnWVGu7l6ydUZxeK13AN6uvzGCxJGUTc2Rh0TKb8SyVEalxDJ9z6vB9ErV5Fva82JIu2ei7qL-DyeEGE7Gxuj3qgcAQTI3Zqi41phEJQ_GKuhU_wW-qDELcHQjAlDS9mUQomqeGwM3dz3z2u0dGP98UuKOGzynhqKICJv025Al2rl4-gDjZrVXMyE_AhFCEmoqYeGTa777OcgluIA7G-_A2v4NYiRTjDZBUdc6L_dWSx5J5I-EGKV3k6UAW040v5wIXrF0Dg7aKtriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19600" target="_blank">📅 10:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19599">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.  این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19599" target="_blank">📅 10:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19598">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.
این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.
منبع: i24</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19598" target="_blank">📅 10:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19597">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ ادعا می‌کند مذاکرات آمریکا-ایران روز دوشنبه آغاز می‌شود
او‌ گفت:
«خب، کاری که الان انجام می‌دهیم این است که در قالب مذاکره با آن‌ها صحبت می‌کنیم. این کار فردا بعدازظهر آغاز می‌شود و خواهیم دید که آیا این واقعیت دارد یا خیر. من عاشق انجام این کار هستم،»
ایران این ادعاها را رسماً تأیید نکرده است.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19597" target="_blank">📅 02:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19596">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19596" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19595">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19595" target="_blank">📅 01:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19594">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ درباره ایران:
نمی‌دانید این حملات به کجا منجر می‌شوند. منظورم این است که آیا همسایگان ایران با هجوم مردم (ایران) به کشورهایشان غرق خواهند شد؟
یک فاجعه. اتفاقات بد زیادی می‌تواند رخ دهد.
من ترجیح می‌دهم توافق کنم. به دنبال کشتن مردم نیستم. مردم می‌میرند. بسیاری از مردم می‌میرند. ما نمی‌خواهیم این اتفاق بیفتد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19594" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ می‌گوید عربستان سعودی، امارات متحده عربی، قطر و ایران همگی از او خواسته‌اند حملات را لغو کند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19593" target="_blank">📅 01:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19592" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کشته شدن مامور پلیس در درگیری با اشرار مسلح شادگان  ستوان‌سوم شهید «سینا سیاه‌نژاد»، از نیروهای حافظ نظم و امنیت، هشتم مرداد در جریان درگیری با اشرار مسلح و حادثه تروریستی در شهرستان شادگان استان خوزستان، حین انجام ماموریت به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19591" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سنتکام:
تا تاریخ 2 آگوست (و در راستای اعمال محاصره دریایی ایران)، فرماندهی مرکزی ایالات متحده (CENTCOM) مسیر 35 کشتی تجاری را تغییر داده است، 2 کشتی را غیرفعال کرده و 2 کشتی را بازرسی کرده است.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19590" target="_blank">📅 22:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترکیه با پیش‌بینی تشدید تنش‌ها، اقدامات کنترل مرزی را تشدید کرده و  مرز خود با ایران را با دیوار فولادی تقویت می‌کند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19589" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک دیپلمات ایرانی به روزنامه وال استریت ژورنال گفت:  مقامات ایرانی از آسیب‌پذیری‌های سیاسی ترامپ آگاه هستند و در صورت لزوم، به دنبال بهره‌برداری از آن هستند.  در صورتی که دیپلماسی به نتیجه نرسد، سپاه پاسداران انقلاب اسلامی در حال بررسی حملات پیش‌دستانه است،…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19588" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک دیپلمات ایرانی به روزنامه وال استریت ژورنال گفت:
مقامات ایرانی از آسیب‌پذیری‌های سیاسی ترامپ آگاه هستند و در صورت لزوم، به دنبال بهره‌برداری از آن هستند.
در صورتی که دیپلماسی به نتیجه نرسد، سپاه پاسداران انقلاب اسلامی در حال بررسی حملات پیش‌دستانه است، حتی اگر ایالات متحده حمله نکند.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19587" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19586" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فردا یک صوتی مفصل درباره این داستان قدرت نظامی اوکراین و بحث زیرساخت ها خواهم داد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19586" target="_blank">📅 19:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یک حمله انتحاری به ایستگاه پلیس کابال در منطقه سوات، ایالت خیبر پختونخواه، پاکستان، انجام شده است.  بر اساس گزارش‌های اولیه، چندین نفر از نیروهای انتظامی و غیرنظامی در این انفجار کشته یا مجروح شده‌اند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19585" target="_blank">📅 18:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک حمله انتحاری به ایستگاه پلیس کابال در منطقه سوات، ایالت خیبر پختونخواه، پاکستان، انجام شده است.
بر اساس گزارش‌های اولیه، چندین نفر از نیروهای انتظامی و غیرنظامی در این انفجار کشته یا مجروح شده‌اند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19584" target="_blank">📅 18:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19583">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">با گند زدن عبدالصمد ونساوی در حوزه برخورد با جمهوری اسلامی، اکنون شانس روبیو برای پیروزی در رقابت های درونی نامزدی حزب جمهوریخواه برای انتخابات 2028 به 31% رسیده که بالاترین میزان تاریخی خود است.  در سوی مقابل شانس ونس ترنس به 39% سقوط کرده است.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19583" target="_blank">📅 17:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19582">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نیروهای اسرائیلی در حال هدف قرار دادن ارتفاعات علی الطاهر در جنوب لبنان با بمب‌های آتش‌زا هستند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19582" target="_blank">📅 17:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19581">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGv08djs3ExC0fvnrKZoxYHKdTpyI039kyDnGR2MZ01U26Xg5KSMwuaOpsziS-Ii12xe-whSCp4jF7h90yVnoOVmRNdPhKJgZJjL9eHWUMiyZAp9yyyL5QIX4HU2LpmnivtSMg8J_1TWJzEmgE6sMsidZwYd0GxHbwBZQItt_I9uiYtqBhzKXyEr-9EU8EjZdYGnD4-rxqiMAgPUPJl34XBsczGmBAS1RJ3Fx8Qvfrs0KcEynaOrJ_0R0I1l6WK5xbxDQKnKV9fsfLqX9QHbxvz-vb8_MvQoFDkD8X_-hHflTzw3QM6GLAGqpTeI0ToxiCP55Yu-AfzujZU3ExPTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19581" target="_blank">📅 15:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19580">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بسیار بعید میدانم جمهوری اسلامی بدون لغو محاصره دریایی، تنگه هرمز را باز کند، حتی اگر ورودی تنگه هم در اختیارش باشد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19580" target="_blank">📅 13:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19579">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:   حکومت ایران در طول جنگ سقوط نخواهد کرد.  مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.  تأکید باید بر این باشد:…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19579" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19578">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:
حکومت ایران در طول جنگ سقوط نخواهد کرد.
مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.
تأکید باید بر این باشد: اقتصاد، اقتصاد، اقتصاد، اقتصاد. این چیزی است که در نهایت حکومت را سرنگون خواهد کرد.
به نظر من حکومت می‌تواند به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی این اتفاق بیفتد، ترس دیگر مانعی نخواهد بود. آن‌ها بیرون خواهند آمد، قیام خواهند کرد و حکومت را سرنگون خواهند کرد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19578" target="_blank">📅 13:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkH9s1JkHEY0aik3vbApCt72lYrv5UfPBZC-B9bgL69p5ibmfcDbbho5Se8Ah2jpNLfdnjngGCpNebVgOPsSVCpm96tA8bOUu2ooQ2Z6yX_gpAQObAqxTK_JZBCMRYSpc7u1iubTyDmAdyHMN4_V0wJxqgHFp-mZuJmoW8lh79c1_06xBOnBIc95DRlvcB75BoAX5pkDoPfEXoj_hGTz3lH21Rk6BuO-eLc3GOjTmlH6oiwDVm1JD9XRz02KwXhM2QqfbHtypv7Dp1dbMmt6nZuZJxOzrMBoaGmqGf1GcDCr2GCPRRykCdJ0I3XjVtA_-NDXhV4bJZk2xA_Fxw32Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarket Podcast Text.pdf</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19577" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آکسیوس :    ایران با طرح بازگشایی تنگه هرمز موافقت کرده است و قرار شده مسیر ورود از طرف ایران و مسیر خروج از طرف عمان باشد</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19576" target="_blank">📅 11:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19575">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یعنی موج 2 اینقدر کوتاه بود؟!  سبحان الله!   همه 5 سانت و 10 سانت و ....</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19575" target="_blank">📅 11:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نیروهای مقاومت بعد از اربعین پاسخ آمریکا را خواهند داد
علاءالدین بروجردی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس، با محکومیت شدید حملات بزدلانه ایالات متحده و عربستان سعودی به مواضع حشدالشعبی و موکب‌های عزاداری امام حسین(ع)، این اقدام را نشان از استیصال و ناتوانی نظامی دشمن دانست و گفت:
با وجود احترام به قداست ایام اربعین حسینی(ع)، پاسخ قاطع و متقابل به این جنایات در زمان مناسب و پس از پایان این مراسم مقدس، توسط نیروهای مقاومت انجام خواهد شد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19574" target="_blank">📅 11:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس
:
ایران با طرح بازگشایی تنگه هرمز موافقت کرده است و قرار شده مسیر ورود از طرف ایران و مسیر خروج از طرف عمان باشد</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19573" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ گفت که حمله دیگری به ایران را به تعویق انداخته تا مذاکرات به سرعت ادامه یابند.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19572" target="_blank">📅 09:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ گفت که حمله دیگری به ایران را به تعویق انداخته تا مذاکرات به سرعت ادامه یابند.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19571" target="_blank">📅 09:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">باراک راید از آکسیوس، با استناد به دو مقام آمریکایی و یک منبع دیگر، گزارش می‌دهد که محمد بن سلمان، ولیعهد عربستان سعودی، نگرانی‌های خود را نسبت به طرح دونالد ترامپ، رئیس‌جمهور ایالات متحده، برای انجام حملات گسترده علیه ایران ابراز کرده است.
بن سلمان در یک تماس تلفنی با ترامپ، درخواست جزئیات بیشتری درباره عملیات کرد و از او خواست که حملات را آغاز نکند.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19570" target="_blank">📅 03:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19569">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حمله ایران به سلیمانیه و اربیل</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/19569" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19568">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این شرکت Fire Point، بجز موشکهای دوربرد فلامینگو، پهپادهای انتحاری دوربرد FP-1 را هم تولید می‌کند که اخیرا در حمله به تاسیسات نفتی روسیه عملکرد درخشانی داشته است.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19568" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19567">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دنیس اشتایلرمن، رئیس شرکت فایر پوینت، تولیدکننده موشک‌های «فلامینگو»، پیامی با تهدید علیه ایران منتشر کرد.  این تصویر، فلامینگوهای صورتی را نشان می‌دهد که در امتداد مسیری که اوکراین و ایران را به هم متصل می‌کند، پرواز می‌کنند و لوگوی شرکت و عنوان زیر آن آمده…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19567" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19566">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تهدید یک نظامی اوکراینی به حمله به ایران با موشک های کروز فلامینگو</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19566" target="_blank">📅 01:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19565">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19565" target="_blank">📅 01:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19564">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Egs-5OfyzSIwASMUh8BQKb9EzMAHTLkvqyf_mTYWG7rr_X1dI-0LFy09NxtX3cCh81QQvWuEky8pKzNteGoW7yz3AouIFxgT2JrLDUJxE5Z0J_kSsft-zRXrnm6md5Yj5b-76KNY6Iw8MvH4jPgBuc95cvTC31CBLGcV9LiPO96vw4gR2dOw2fY4PwsBMjggF1PE3DKls4jI6ASCkOyAw-3CO10AxhQhU8OEGAJoF_qFUuRHML4kxKY6rAoFy2_yJTUu6_eAO9pSC0ckVL7K3-hepd7iYvEYGREeKcQAcSPIE2Sa3zQ98CdPF2G08lTQMV2mngz-GSf9TEQ6e6QSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت اتاق جنگ اسرائیل</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19564" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19563">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دکتر مرندی این بار دستور تخلیه کل خاورمیانه را صادر فرمودند.</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/19563" target="_blank">📅 00:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19562">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEx-q6DGatRXDFMw4SyBEPj3_6iFuPLNpmDR_un_vcrFDEFwsCOvl_sFQ_qDFO6kYYnx_ZrrQmUhSyfk7Udk_REqmKg3YmPnj4GEiBVehJGMTRWNAFTBVQpV0yankcL2mBIZZIGboFNfjlogdhaTTzN-sjSKINITq74VY2-YmLZ-JYQcsaXq2dxje8y0VcLEcNUTKtKqr0r_qiBuIcBFN5TBNTTPgrufeZlGAn2mIhQCEiOC1R3TXn0qLmr0ltWfNXPAiYAcOHI8zzMUTTUw5OvKu0vnsoIX3nsXVhaCVyZI_XgU5fWXOr1VH7Ik74AD3dQreyTwK48iQon7gueoKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/19562" target="_blank">📅 23:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19561">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک منبع از وزارت جنگ ایالات متحده به شبکه فاکس نیوز گفت:
«ما برای یک جنگ تمام‌عیار علیه ایران آماده هستیم.
در چند ساعت گذشته، رئیس‌جمهور ترامپ دستور انجام تعدادی از حملات مرگبار و خطرناک علیه نیروهای سپاه پاسداران انقلاب اسلامی را صادر کرده است.»</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/19561" target="_blank">📅 22:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19560">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsm_GoWLKrQhpfYHO2ljN9Hl96T5n8JsmJdbPJtttdXWpBbHxYBZ1a7mcScHTjII1O-X06nbLFmaKVAPztIvbNhA7HNIvCK7STeTGfKCYVKpguUpVddqhtjo4cXmPaN23qmUe2hqGf6o89p9ygjmZy6ZsepsBKVYRsYcJwxcJ1sA83JkfFMHJL0t3OdJzazgHkTSKDjINsTRLbsKV3_T_x9-hmDvnlADglP_Gu3rAeeGAYghTBR7D66QLp3ODFshUKGRGMODCsdxcQuybQ2-g7I1OUdTZQs-e4MnsoR0mlyhmUWtbBcckhPhCEryzmxJRJ7sFOBl6ObqCqhCbVRHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ترامپ در حال نابودی ارز ایران است.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19560" target="_blank">📅 21:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19559">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">برخی گزارشهای آمریکایی می‌گوید کشورهای خلیج فارس به رهبری قطر در تلاشند تا از جنگ مجدد آمریکا با ایران جلوگیری کنند.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/19559" target="_blank">📅 20:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19558">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">— مقامات آمریکایی در حال بررسی موجی از حملات سایبری علیه سیستم‌های آب در حداقل هفت ایالت هستند، با شواهد اولیه که به ایران اشاره دارد.
حملات برخی عملیات را مختل کردند اما آب آشامیدنی را آلوده نکردند و هیچ خطر شناخته‌شده‌ای برای سلامت عمومی ایجاد نکردند.
دونالد ترامپ نقش ایران را زیر سوال برد، در حالی که مقامات ایالتی و فدرال گفتند که ایران بر اساس اطلاعات موجود همچنان مظنون اصلی باقی می‌ماند.
متخصصان امنیت سایبری این کمپین را یک بی‌سابقه در هدف قرار دادن زیرساخت‌های آب ایالات متحده توصیف کردند که احتمالاً قصد بهره‌برداری از سیستم‌های آسیب‌پذیر را داشته است نه هدف قرار دادن جوامع خاص.
— نیویورک تایمز</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/19558" target="_blank">📅 20:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19557">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مکن ای صبح طلوع …</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19557" target="_blank">📅 20:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19556">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTGX69ByeVcVejQG9UqrO8mQIZ9VsvgiNuBThjgrBSQf8WMePEPsNdUB1uwrsn26UoLq0t0159i0tkNVUjnXZhOhlnsSRH1UPaoxp-qsZ-uVIbuKqaYUGAuJACBVVB9LOO5wKPWHzMD2AshFRUsOI5qD0KeOVQSxCc5iBjOkHbUtNvpwgtjyFjtwOzCGcRf6m1M3AFPpSZ9yu90ScjPGxSqJN9W_sKQVp5P18Azen8-UD2mDEhF87-jdlEGVHNfs9-3tpQvCY9EM_WRmiDxwK3aabQ_HRqCrg8FoDSrf2LCx80T4PW5t-endwYTfu-FuL0lFD5n1GxPsjwKOfuTMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر مرندی در پاسخ به تهدید ترامپ دوباره دستور تخلیه شبه جزیره عربستان را صادر فرمودند</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SBoxxx/19556" target="_blank">📅 20:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19555">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu__hS9lxqERombeS1IS5ZaD-m6gYmmf2ADKm4uwio99Lyqw1uCg-x0HFf22YIMUtymqX_Acxjb5MxTclTp-rVlhOf3i_yuh1qewDYGVTPPAHMFn1nCFUhEU5a2ipLuw5JxEOsD31OSFtqUDrUy13631eI1DVojenXq1By2RyQ3YoZ-zfRIZz3Ccf-tlhvXw3lZsn4dk5iP-ECiMYYzXlSYNnJvrH1hanTdyhWyMRfuLBs4oEacQphosN6RU9mse_PUirw6VXZER2wmy0H2jv-ac04V3cGipI5kwE8y0B42up0MINVllPCeShcI7g9RMDitCCmTwK0iSzpEZlUlHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه روسیه با پهپادهای ایرانی رقابت تسلیحاتی در حوزه پهپادها را تشدید می‌کند   رئیس‌جمهور اوکراین، ولودیمیر زلنسکی، ماه سپتامبر مجمع عمومی سازمان ملل هشدار داد که «ما اکنون در حال تجربه مخرب‌ترین رقابت تسلیحاتی تاریخ بشر هستیم»؛ اشاره او به بهره گیری روزافزون…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SBoxxx/19555" target="_blank">📅 15:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19554">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به جای جای ایران که مینگرید، نشانه های بازدارندگی قدرتمند جمهوری اسلامی را می‌توان دید</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/19554" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19553">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در اسلام آباد غرب، کرمانشاه خبر داد.</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/19553" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19552">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در اسلام آباد غرب، کرمانشاه خبر داد.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/19552" target="_blank">📅 14:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19551">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd37ccbfd.mp4?token=G6iWzWmKqF290lqNcM4i-Gf6rnimzY0oLg7VxdVIFBHw0hpPcJMdiHfZxkbyEq10aPBVCdqY17LkslYOjv-8yi6SWMOropPjSEsAlZrnx4u6ghMZO7TCL23LRj7F-HWr8yAG-lDC6IjTdsqvcTI7xK1Eu-M8JO9rG3a4_l8aUhUH6ojqu53fhkR0oax67yhm_ApMbcc1h4VN9EbBL9jNF5crTSoAZrcWJoUTAZwBhE8gVV5Kh9UmQT0JDFcw2IIQm_DIyWmmHN8b-TYN7ZLW1mz74KdnuACg5I07TJH2oaGStq294DHY5U8yCB_0utytwBvdRanZxJO4RZ6zcbG0s30ppCjx11BHWrTGirgoAwmsMzaqY7di9uguzqmbl0lcJuuF_mrvZjEYN1s_itnod_x-8vfgklbWaJ8wOLbcCZsEWL48W3_HWEFLuVhouWZ0gPuemqiBjdGepIEn0MyUenRXR_vO8_mvWNkbnVQd40VYyN-PB4x7PmzmQAFLiUNk9-w4NPrZclCAZG-d1-2FPJgHoAXe7WtE7FUKexIW_DJEYrJKVq6mK2NMdTrrklVIFLLGAYt5exp5tMe_WayWN78K2eyJxl2Zya89q9uidJZzIuiNxasEawYldSyx46FRtedpbppdXtGD60fKXp0T4DXarG7TVPiocfzmZvNFi7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd37ccbfd.mp4?token=G6iWzWmKqF290lqNcM4i-Gf6rnimzY0oLg7VxdVIFBHw0hpPcJMdiHfZxkbyEq10aPBVCdqY17LkslYOjv-8yi6SWMOropPjSEsAlZrnx4u6ghMZO7TCL23LRj7F-HWr8yAG-lDC6IjTdsqvcTI7xK1Eu-M8JO9rG3a4_l8aUhUH6ojqu53fhkR0oax67yhm_ApMbcc1h4VN9EbBL9jNF5crTSoAZrcWJoUTAZwBhE8gVV5Kh9UmQT0JDFcw2IIQm_DIyWmmHN8b-TYN7ZLW1mz74KdnuACg5I07TJH2oaGStq294DHY5U8yCB_0utytwBvdRanZxJO4RZ6zcbG0s30ppCjx11BHWrTGirgoAwmsMzaqY7di9uguzqmbl0lcJuuF_mrvZjEYN1s_itnod_x-8vfgklbWaJ8wOLbcCZsEWL48W3_HWEFLuVhouWZ0gPuemqiBjdGepIEn0MyUenRXR_vO8_mvWNkbnVQd40VYyN-PB4x7PmzmQAFLiUNk9-w4NPrZclCAZG-d1-2FPJgHoAXe7WtE7FUKexIW_DJEYrJKVq6mK2NMdTrrklVIFLLGAYt5exp5tMe_WayWN78K2eyJxl2Zya89q9uidJZzIuiNxasEawYldSyx46FRtedpbppdXtGD60fKXp0T4DXarG7TVPiocfzmZvNFi7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SBoxxx/19551" target="_blank">📅 12:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19550">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سفارت ایالات متحده در اردن :
«آمریکایی‌های حاضر در خاورمیانه باید احتیاط و هوشیاری بیشتری به خرج دهند و برای لغو پروازها، بسته‌های دوره‌ای فضای هوایی و اختلالات احتمالی سفر آماده باشند.»
«آمریکایی‌های حاضر در منطقه باید به ترک آن فکر کنند، یا در صورت تشدید درگیری‌ها برای ترک منطقه آماده باشند».</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/19550" target="_blank">📅 12:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19549">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ویدیویی بسیار جالب درباره روند ایجاد و تکامل ایده ساخت پهپاد لوکاس که مشابه شاهد-136 است اما مجهز به هوش مصنوعی و توان رهگیری بالاتر  https://www.msn.com/en-us/news/other/watch-how-the-us-turned-iran-s-drone-into-a-weapon-used-against-them/vi-AA20tLa9?oci…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/19549" target="_blank">📅 11:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19548">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ارتش آمریکا یک یگان ویژه پهپادی در منطقه عملیاتی سنت کام (غرب آسیا) مستقر کرده که در آن از پهپادهای Lucas با طراحی تقلیدی از پهپاد شاهد-۱۳۶ خودمان استفاده می‌شود.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19548" target="_blank">📅 11:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19547">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">افزایش اهمیت اهرم فشار چین
به گزارش رویترز، با تشدید دوباره جنگ ایران، کشورهای عرب حاشیه خلیج فارس به‌جای واشنگتن، به چین روی آورده‌اند تا از اهرم اقتصادی خود در برابر ایران برای بازگشایی تنگه هرمز و مسیر دریایی دریای سرخ استفاده کند. این وضعیت در واقع آزمونی است برای اینکه پکن تا چه اندازه توان و تمایل دارد تهران را تحت فشار قرار دهد.
منابع کشورهای خلیج فارس می‌گویند تلاش آنها برای ایفای نقش بزرگ‌تر چین، ناشی از افزایش نارضایتی است. جنگی که در ۲۸ فوریه با حملات آمریکا و اسرائیل به ایران آغاز شد، اگرچه به رقیب منطقه‌ای آنها آسیب زده، اما هم‌زمان صادرات حیاتی انرژی این کشورها را نیز محدود کرده و آنها را، با درجات مختلف، در معرض حملات قرار داده است.
سه منبع منطقه‌ای می‌گویند از آنجا که ایران و متحدانش هم‌زمان تنگه باب‌المندب در دریای سرخ و تنگه هرمز را تهدید می‌کنند، کشورهای خلیج فارس از چین درخواست کمک کرده‌اند؛ به‌ویژه با توجه به اینکه جنگ محدودیت‌های قدرت آمریکا را آشکار کرده است.
وانگ یی، وزیر خارجه چین، ده‌ها تماس تلفنی و دیدار با همتایان خود داشته و برای دستیابی به آتش‌بس جدید تلاش کرده است. همچنین ژای جون، فرستاده ویژه چین، با مقامات کشورهای عرب خلیج فارس و همچنین ایران مذاکراتی انجام داده است.
اما این دقیقاً چیزی است که وضعیت به آن نیاز ندارد! هیئت تحریریه وال‌استریت ژورنال هشدار می‌دهد که نتیجه جنگ ایران تا حدی به رفتار و عملکرد قدرت‌های محور مقابل آمریکا بستگی خواهد داشت.
این نشریه می‌پرسد:
«با وجود اینکه آمریکا بخش قابل توجهی از زرادخانه موشکی ایران را تضعیف کرده است، آیا چین به‌سرعت به بازسازی آن کمک خواهد کرد؟ آیا روسیه که به دلیل کمک‌های ایران در جنگ اوکراین به تهران بدهکار است، به احیای برنامه هسته‌ای ایران کمک خواهد کرد؟ آیا هر یک از این دو کشور، سامانه‌های پدافند هوایی پیشرفته‌تری در اختیار ایران قرار خواهند داد؟»
در واقع، نگرانی اصلی این است که چین و روسیه به‌جای ایفای نقش میانجی برای پایان دادن به جنگ، به بازسازی توان نظامی ایران کمک کنند. چنین سناریویی می‌تواند جنگ را طولانی‌تر کند، رقابت ژئوپلیتیکی میان آمریکا و چین را تشدید کند و هم‌زمان ریسک اختلال طولانی‌مدت در مسیرهای انرژی هرمز و باب‌المندب را افزایش دهد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19547" target="_blank">📅 10:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19546">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">CBS News:  آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.  ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/19546" target="_blank">📅 09:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19545">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هدف قرار گرفتن ۲ کشتی در نزدیکی سواحل عمان در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19545" target="_blank">📅 09:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19544">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf2ln5mri4FcbTfoKVzLLaHO7etMbr6gFZNc-SMdcSOszm-MRBS-33oSxVmag8H-5ata47fxowxlVQxFAOQcLGSvOEYa-UNrhKL3ruqmUgVM61NRQTRsLfwVT-GGHxaVwHVSBrOxhtr4mytM8G3QK6rWo8761PZyfbJC3jXGywgzICn0-aYUNJUw6IRRB_Wlh1tZai1veB-NUJsGpDhfev68-yg3TE4Te0yNvZeM94ap691Zh0ZZTvhDKEQu1kjWyxRckuZW2tNCXgJWMtBHSTH6-LxbzaFac65hq1r3OWXo65PDV9etM_6U9Ku4AzqfsGXNaX2h0BTSAR7bHX-8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار : آیا چین و روسیه اطلاعات هدف‌گذاری را به ایران می‌دهند؟ این حملات اخیر ایران  بسیار ویرانگر برای نیروهای آمریکایی بوده‌اند.  روبیو: هر زمان که در یک منطقه جنگی مانند الان هستید، خطراتی با آن همراه است. منظورم این است که در نهایت، این واقعاً ثابت می‌کند…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/19544" target="_blank">📅 01:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19543">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو خطاب به رئیس جمهور ترکیه:   اردوغان یک دیکتاتور یهودستیز است که مرتکب نسل‌کشی علیه کُردها می‌شود  او که از حماس حمایت می‌کند، مردم خود را سرکوب می‌کند و مخالفان سیاسی خود را زندانی می‌کند، آخرین کسی است که می‌تواند درس اخلاق بدهد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19543" target="_blank">📅 01:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19542">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">CBS News:  آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.  ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19542" target="_blank">📅 01:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19541">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مرندی:  رژیم مراکش صرفاً ابزاری دیگر برای نتانیاهو و ترامپ است. آن‌ها اسپانیا را به خاطر حمایت از فلسطین تنبیه می‌کنند.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19541" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19540">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19540" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19539">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">CBS News
:
آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/19539" target="_blank">📅 00:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19538">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ:   ایران موشک‌های بزرگی به سمت اردن پرتاب  کرد و قبل از اینکه نزدیک بشوند  توسط سلاح‌های فوق‌العاده‌ای که داریم زدیم: بینگ بینگ بینگ بینگ بینگ بنگ</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19538" target="_blank">📅 23:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19537">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📡
استفاده ارتش چین از هوش مصنوعی آمریکایی برای تقویت توان نظامی
🔷
خبرگزاری رویترز در گزارشی اعلام کرد که پژوهشگران نظامی چین با بهره‌گیری از خروجی مدل‌های پیشرفته هوش مصنوعی شرکت‌های آمریکایی «اوپن ای آی» و «انتروپیک»، سامانه‌های بومی هوش مصنوعی را برای تقویت توان دفاعی و نظامی این کشور آموزش داده‌اند</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19537" target="_blank">📅 23:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19535">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e924f93a.mp4?token=HXKiifc5RIJ8DBOeseVjmZ-714BzbNS5mzbOKMz2_ogiV7eDUrBKR9lkTVxfcwF7FaGodmwE0h3FzrYAJQ4MjzUMLw22lQU2Uyxnt1ZNdP851U2fq8xoqJJg6vijQuyI5npUViPC-QpRbh7OhVwvbcKvQpJQ5Y0X6mVv04RJzQnhHp2mcAjS5i-UREXCxlYChq8KgmlU3DcsO-sMeMAjVR1TSInjfVVTLA9H6yMZuyGVQdpYeJV_yoNzlq6XRieMvyXG56sL8u0mydJhHQoBt6ySvCF8NTOfzthYgT_IDHTDQGyEDbEltC3rutDr56e4dJoDz0vKYjeLMIIhZojkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e924f93a.mp4?token=HXKiifc5RIJ8DBOeseVjmZ-714BzbNS5mzbOKMz2_ogiV7eDUrBKR9lkTVxfcwF7FaGodmwE0h3FzrYAJQ4MjzUMLw22lQU2Uyxnt1ZNdP851U2fq8xoqJJg6vijQuyI5npUViPC-QpRbh7OhVwvbcKvQpJQ5Y0X6mVv04RJzQnhHp2mcAjS5i-UREXCxlYChq8KgmlU3DcsO-sMeMAjVR1TSInjfVVTLA9H6yMZuyGVQdpYeJV_yoNzlq6XRieMvyXG56sL8u0mydJhHQoBt6ySvCF8NTOfzthYgT_IDHTDQGyEDbEltC3rutDr56e4dJoDz0vKYjeLMIIhZojkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19535" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19534">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ درباره اوکراین:
تانک‌های روسی در حال حرکت به سمت کی‌یف بودند، اما در گل گیر کردند.
یک ژنرال روسی تصمیم گرفت به جای استفاده از بزرگراه که به خوبی در حال حرکت بودند، از میان گل عبور کند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19534" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بسنت وزیر خزانه داری آمریکا :
ما در مارس ۲۰۲۵ شروع کردیم. در دسامبر ۲۰۲۵، بزرگترین بانک در ایران فرو ریخت.
بانک مرکزی مجبور به چاپ پول شد و این باعث تورم گردید. اکنون آن‌ها قادر به پرداخت حقوق سربازان خود نیستند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19533" target="_blank">📅 19:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19532">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19532" target="_blank">📅 19:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19531">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ:
شنیدیم که در مینه‌سوتا یک حمله سایبری رخ داده است. آن‌ها آن را به ایران نسبت دادند. من این را نمی‌پذیرم.
من آن را به مینه‌سوتا و فرماندار فاسدش نسبت می‌دهم.
آن‌ها دوست دارند بگویند، «آه، این ایران است. ایران باید خیلی خوش‌شانس باشد.»
ایران مشکلات بزرگتری نسبت به نگرانی درباره مینه‌سوتا دارد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19531" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19530">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">روسیه حدود 30 هزار تن بنزین از مراکش وارد کرده است تا کمبود سوخت ناشی از حملات پهپادی اوکراین به پالایشگاه‌های بزرگ را جبران کند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19530" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19529">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8-Kums9CRjFKSAjdK6L9opWjZrUTGHKCX8W0wSjxgYvrQ_qMsuPNvFk5vI9IWlT3URpNL6FrC2P-wJNrcq4FZiuiU6KtzxiVOZqWC8LntESEHFBLezEZpPuTwKbXlMK8Kb3Pt-wEMpkR230Yv2pFzqgJzaYdrJfeAIyexUEaN2M5D14xXIdUI9Ci0CpGxR3i6SbcAVj2K3rauPO1lMJeikj_QzoJm0I6l4W2lA2_P9BIsBAOweSaWZCGAiTZ0WfxsR9KMumAMcAedilevx7W4vfvQVm4AFolANgZEJ5yPjmtPdyBc2OB6san1pa4YKwvauxmZa9cJj0FzkP1qNyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19529" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19528">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اسرائیل طرح "هیئت صلح" رئیس جمهور ترامپ را که هدف آن خلع سلاح حماس بود، رد کرد. این کشور مدعی است که این طرح برای اسرائیل قابل قبول نیست و اسرائیل هر حقی را برای هدف قرار دادن و کشتن افراد در غزه دارد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19528" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19527">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این اسپانیایی ها 700 سال زور زدند تا عربها و بربرها را از خاکشان بیرون بریزند؛ چپ ها در 2 سال دوباره همه آن کوششها را بر باد دادند!
چپ = نکبت</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19527" target="_blank">📅 17:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19526">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یک زن وحشت‌زده در سئوتا درخواست کمک از نیروهای نظامی می‌کند و می گوید: "ما تنها هستیم":  ما به حضور نیروهای نظامی در خیابان‌ها نیاز داریم. آن‌ها اینجا نیستند.  ما تنها هستیم.  چطور ممکن است من نترسم؟ من می‌لرزم. این یک تهاجم است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19526" target="_blank">📅 17:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19525">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19525" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19524">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdpZ8AdQf0HrEqs6XYcqKj9bF2QsAuNMlZ0mVTXPT-nyZ0jjRc0LCdbvvEeOPbCS03lM6SVBxVu05LY2WnBwEZY4FVB-wKYZmZ2kWx9KtzHy1kHl9st2TPKbg_Fqb2cC-RPd3EbyNhN0ECl7w9KivdmsTNJ0AlB05g4qny5S5nCp_nOVQgiJRxqLtHW9I8GxIcFjrTMMH0H7eHMH1BAIUuRu08Pej76ejFKzJUcHjERwe-uJApUt0auYf3kbgJU22jFKo8A88A4zbGVxzwz_YEyB6SjUFxccjhCnSzsHTg4F_1X76I37iUv9r9b6EC-G4BZe0xumuuwbp1RCnwmh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز بسیار بالاست و پیش بینی می شود طلا (و شاخص های سهام) زیر فشار فروش بروند. (خصوصاً شاخص های سهام)</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19524" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19523">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ:
"جنگ با ایران به خوبی پیش می‌رود. ایالات متحده ضربه‌ای سنگین به ایران وارد می‌کند و ما به سادگی به پیروزی ادامه می‌دهیم</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19523" target="_blank">📅 17:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19522">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19522" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19521">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تنگه ای که استراتژیک نخواهد ماند  وقتی گفته می شود ایران‌ استراتژیک‌ است، بخش مهمی از این‌ گزاره به دلیل اشراف جغرافیایی ایران بر تنگه هرمز است. چون دستکم‌ یک پنجم انرژی فسیلی سالانه جهان از آن می گذرد. ولی گلدن ساکس مدعی است که تا امروز ۷ خط برای دور زدن…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19521" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19520">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndf78a7-B4PUy2oJri8EUYueYy5Nd0KwlHSdPAxipcvEIGeJ0DE1MIRvR0pCpGNhvw8WC_zmnKxYuB79nGCRXbAxBgIpaKoknQrQKL9OSsb1-JXt4HzGBC4maUp0hhb2XLh5yLJhOZ0cKMw5T7oOQBlzKGQgXneMg3Hvb3X5f6RjqKiooFedlDEJXeJDjXiF9QU73MVMTo9m0eaw01ofxf6s-pmX_63bP5twcqeQTPosYFm_NpBidRAgWYodHT-86CBVzbM9WezZZjc62gRNL6U4CfRbanEBXG_x8NivOElWrd0RE4dsnj2_fkV5rktuwEHJ7QCgG0zl75fGpKghWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عصر اقتصاد دانش بنیان، تنگه بندی و گردنه گیری تنها منجر به انزوا و تیپا خوردن خود عامل می‌شود و اندونزیایی ها خیلی سریع فهمیدند که این لقمه برای دهانشان بزرگ است ولی خب.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/19520" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
