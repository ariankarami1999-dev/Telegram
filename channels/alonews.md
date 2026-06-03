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
<img src="https://cdn4.telesco.pe/file/Kk6zki0WAcTQH4lrISgtfPA8VutdwbqykJx-bZhBubUujfcBmzthiU4JZT5B9h3aOflFpk-lM5L7O2bWA4oRBCmq4YKngJlJvOl8W34wUMqirm0GSm_WuOBXivBx0fQnjodfS2amdTNxfHDE-ReRpZQHLAsM5kLfq_lER3GktdXTfMXTnACo3wKNp1eneo6i9ATUGry_kF-mJUxLzxypRcTmscCJjv_IsFGOiXkQOOyHtSoGVM3BSKuYxd67Yw6hEXEZvTLpDYjGVSABZkdG4hfd8hbnaezcmWALMFPETl342Y3BYHz4wUFGOlbjNqBb8sZsrg3Sd1unUySRKqXaTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 955K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-124788">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نخستین جلسه قالیباف، نماینده ویژه ایران در امور چین با وزرای اقتصادی دولت
🔴
وزرای اقتصادی دولت به برخی نکات اساسی در مورد رفتار‌های اقتصادی چین در ایام جنگ و همچنین دوران بسته بودن تنگه هرمز اشاره کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/alonews/124788" target="_blank">📅 15:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124787">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ارتش کویت: ما ۱۳ موشک بالستیک  و ۱۷ پهپاد را شناسایی کردیم
🔴
یک مقیم هندی جان باخت و شماری از افراد زخمی شدند، همچنین خسارات مادی سنگینی وارد شده است.
🔴
به دلیل حملات، امروز ۵ بار آژیرهای خطر به صدا درآمده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/alonews/124787" target="_blank">📅 15:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124785">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqoiK80nAFoAGrb2Sv6nyk_66A5H7i8fjRKvklTWghIgTLNQCMz3rPJ6Ns0FmE7Y8z79YKfrn3E9us2fuyKn96szTvmrxa6ZoC0Gf-bDPVo6V30lq7I52_FRKpWX0WdC58CN3yrAAD56vD_MLKeBNMF_3mb29Atykh_ALAubLlgvnTmx1eXrRNdT_HY0oilPJYu1X9VflxEl7GlO-p6UNHewqu83OebS5AGXJ4YUBKDJiGs3jYRZ6rmn6TMXJW9J_TYzs-nuXIou7zVHjbjoSgpGTBGzqB5VtXiDAodJDTgaWF5SVsEMq_eHeuayHPn8PmhIxNoFHUSksJmEIPe0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61fbd0e8c6.mp4?token=EY9ZT4GGxCCP0BeLUyw3XFuEfY7EuhmSY8ihVPrkPEAkQOwcCA1Mo9NxOra_iyTFsnLEeE9un4rrTzF_SobZxkCLkH4zm6YLzziIgNGE1xkPB6MDZphd02r0IHztz9w9WdRpzK50lNkKv_lP82i-sgEI10Zkb_VuAfLb5n9fWMZZrXTef5pZm3lspJgzwIPJ6dY-5BY0QF7SlEV90fHd6hIVKJsnhOiUQkq5Ru5KxMkZJkH6dlvCnE75nltZCUId6PteKNiB5m6OYei0kD6rB6KCeuDYJ5PVvKhiw-ckkmoXws9DnQlkdf1qLYIsjifSUwUtI6ur_CTWdqOIpHos7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61fbd0e8c6.mp4?token=EY9ZT4GGxCCP0BeLUyw3XFuEfY7EuhmSY8ihVPrkPEAkQOwcCA1Mo9NxOra_iyTFsnLEeE9un4rrTzF_SobZxkCLkH4zm6YLzziIgNGE1xkPB6MDZphd02r0IHztz9w9WdRpzK50lNkKv_lP82i-sgEI10Zkb_VuAfLb5n9fWMZZrXTef5pZm3lspJgzwIPJ6dY-5BY0QF7SlEV90fHd6hIVKJsnhOiUQkq5Ru5KxMkZJkH6dlvCnE75nltZCUId6PteKNiB5m6OYei0kD6rB6KCeuDYJ5PVvKhiw-ckkmoXws9DnQlkdf1qLYIsjifSUwUtI6ur_CTWdqOIpHos7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید، تخریب یک پناهگاه پهپاد/هواپیما واقع در مختصات ۲۹°۲۱'۰۴.۷۲"شمالی، ۴۷°۳۰'۱۴.۰۶"شرقی در پایگاه هوایی علی السالم در کویت را پس از حملات موشکی و پهپادی سپاه ( که به ادعای سنتکام همه رهگیری شد) که اوایل امروز این پایگاه را هدف قرار داد، تأیید می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/alonews/124785" target="_blank">📅 15:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124784">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
به گزارش وال‌استریت‌ژورنال، قیمت هر بشکه نفت به دلیل تنش‌های مداوم خاورمیانه افزایش یافته و هم‌اکنون به ٩۶ دلار رسیده است. تنگه هرمز که بخش قابل توجهی از نفت جهان از آن عبور می‌کند، دوباره در معرض خطر بسته شدن قرار دارد و به همین دلیل، مذاکرات صلح آمریکا و ایران پیچیده به‌نظر می‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/124784" target="_blank">📅 15:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124783">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/124783" target="_blank">📅 15:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124782">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jxr6myGJD7ZBuhrAPvbxwvxrVyz0EywH6CGteVyqSqBu6mkVgK6U8XUrml_Kfih_FXV92VPdAE23ytoF-qmreTppnuHLQe4Wbw4BttXV2sXb_LVwjTIbL_g4w24ZTGeH76suo1CFTJjT0dS0DCVQlq5C_NPVEJ9HlrlEY3BeVpSk8rkQvHvrq0TLs7lkpei_a8qQL1dUewm2T6_vlcjfW5iyYFKHH46jegnuTmV8lUxRFYOO2ASoU7dBFEFtGbc0ZpqVn3dAiq6lmCJUqoHDDjmbCqD3uXT4hEHKMDhnoXWpvJq-bQF-pHLO2H7zxdlD0QdXhWNAWfDMFERq3jOcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/124782" target="_blank">📅 15:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124781">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا: هر کسی که اطلاعاتی ارائه دهد که منجر به افشای یا مختل کردن یکی از منابع مالی سپاه پاسداران شود، جایزه مالی ۱۵ میلیون دلاری برای او در نظر می‌گیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/alonews/124781" target="_blank">📅 15:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124780">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">کی ب کیه
تو دنیایی ک ب ۳۳ کیلومتر میگن تنگ توام بگو بار اولمه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/alonews/124780" target="_blank">📅 15:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124779">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
جراحی زیبایی به قیمت جان؛ مرگ دختر جوان در پی عمل بینی
🔴
دختر جوانی که از یکی از شهرستان‌های غرب کشور برای انجام عمل زیبایی بینی به تهران آمده و در یکی از بیمارستان های خصوصی بستری شده بود، شب گذشته جانش را از دست داد.
🔴
اولیای این دختر جوان ۲۷ ساله از کادر درمان شکایت کردند.
🔴
به دستور  بازپرس شعبه پنجم دادسرای جنایی، این پرونده به دادسرای ویژه جرائم پزشکی ارسال شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/124779" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124778">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
تغییر ساعت فعالیت میادین میوه و تره‌بار پایتخت در روزهای ۱۴ و ۱۵ خرداد
🔴
فردا پنجشنبه ۱۴ خرداد ماه همزمان با رحلت جانگذار حضرت امام خمینی (ره) و عید سعید غدیر تمامی میادین و بازارها از ساعت ۸ صبح تا ۱۳ فعال  هستند.
🔴
روز جمعه ۱۵ خرداد ماه نیز مصادف با سالروز قیام پانزد خرداد نیز تمامی میادین و بازارها تعطیل هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124778" target="_blank">📅 15:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124777">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046f93f3b2.mp4?token=WltqcbHjlqKk6EEgO1-kvpZqSjNEYZbCcT4A5eSKArM9g-bqgXbqhHDsWQuSU-p05_glX6fntCtmaR3em4Lkyc8uH_H3MDTysrXZMXzhSo71VrKz4Oen0NXOdSAzkcLeFG-x6RlYJyyeWxv5kGWG93Wmgkr7mDskLpPgdfBVsSIrUKHI0GmbBNTUvB_ouGAFQH092gA2vyadIJmqnJEGfPSf0qpHxV507jYqXREy6UQdc8pAd1aEUafcOFiY-_eW2Ucwr9e7n9u894wWkllDTEr1Jh21IYrIUfjWlhhYAXc25komF2LzOY8scHVtI0pPPeAlNcF28Prhnt4Zz-KOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046f93f3b2.mp4?token=WltqcbHjlqKk6EEgO1-kvpZqSjNEYZbCcT4A5eSKArM9g-bqgXbqhHDsWQuSU-p05_glX6fntCtmaR3em4Lkyc8uH_H3MDTysrXZMXzhSo71VrKz4Oen0NXOdSAzkcLeFG-x6RlYJyyeWxv5kGWG93Wmgkr7mDskLpPgdfBVsSIrUKHI0GmbBNTUvB_ouGAFQH092gA2vyadIJmqnJEGfPSf0qpHxV507jYqXREy6UQdc8pAd1aEUafcOFiY-_eW2Ucwr9e7n9u894wWkllDTEr1Jh21IYrIUfjWlhhYAXc25komF2LzOY8scHVtI0pPPeAlNcF28Prhnt4Zz-KOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل یه ماشین تو جنوب لبنان رو زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124777" target="_blank">📅 15:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124776">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
تماس تلفنی بین وزرای خارجه قطر و عربستان سعودی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124776" target="_blank">📅 15:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124775">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e001f7b2.mp4?token=mEGzlLVCCDZ0zHoh58GO0SYj7w6NreUzewTpbsU8R7o3KcFIb57XPaTe6CGHgOz0Vg-pDVfX1SWhAz54-Vr3hhPTGkBYR5V3F4Im9CjGFgCYD1C4EqWKdvY2G2JvUZkIjsiDPKkSNFXfLtjk2HRBz8H50QkXAoegsCbTCJOdUhVTET7O7TIDt-0E8oQeU_ESmrQToKxIo1K_WGI465lUD4WfqCyvNBMv4K4YZm81qAlOp35lT67rplzVI5cdpOnEZH-59vdHkjsh0PwOkDnESRKz0GHMbFsAM2rPWW07HvdwEKaLsHr9hF4a1InMkPHLILcP5C22bj-MBonoJG4PXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e001f7b2.mp4?token=mEGzlLVCCDZ0zHoh58GO0SYj7w6NreUzewTpbsU8R7o3KcFIb57XPaTe6CGHgOz0Vg-pDVfX1SWhAz54-Vr3hhPTGkBYR5V3F4Im9CjGFgCYD1C4EqWKdvY2G2JvUZkIjsiDPKkSNFXfLtjk2HRBz8H50QkXAoegsCbTCJOdUhVTET7O7TIDt-0E8oQeU_ESmrQToKxIo1K_WGI465lUD4WfqCyvNBMv4K4YZm81qAlOp35lT67rplzVI5cdpOnEZH-59vdHkjsh0PwOkDnESRKz0GHMbFsAM2rPWW07HvdwEKaLsHr9hF4a1InMkPHLILcP5C22bj-MBonoJG4PXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کسایی که تا دیروز به بهانه ناموس جنایت میکردن حالا بصورت عمومی جهاد نکاح راه انداختن!
🤔
شرم و حیا چیز خوبیه که در وجود حرام زاده های عرزشی نیست که بصورت علنی ناموس همدیگه رو دست به دست میکنین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124775" target="_blank">📅 15:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqOlmLLY9MHyKyehzt-tI_5OszvF3h1UTHtkKsLms4sJzlpOMbv-C8MluPv65dfV0dqcIrOy09ic7MpDpNsr-UeSl58_RG-_qSzqlEpiujBxY1PQS7Ho4DgeapQcWnAAiU9J85uAVbpir38cT8L9nLnJpTLiEakq_7-ahw9tbLV9eIRnK3viBPZXpku03wN1ZNQdr_8112mI_LpUh5ehCy4YWM4uSLzeUPmJBX-IwBM8wjHZStRbie-4TEHzmP8xwSIUDZjZDIecJ6Qrp7QVXnlKG_Crz27XrU_Iamh1hfEaOI4iWQclp7asXrU8eIYktitjFEW9_ZuBP0lh-54hog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BY64PcATaQGUS8tnhhTPwnfZtZlOmtII4b4WKl6Gi7ykrI577fp-ZiiZ7zibciPrxk_Pg7m4DuKgCZPm70SoVgoIK3GNzQArsmXjAR3rxxcJExt_sWX6L4zTx7gtaqLVLoivJusV4lArvbQPDjhAn9wnO0bUPFINEcRytZXK6Ox1IEypJC6dr1eE0G_cPuaiCL-M6jVY3cX4Vu8j9mPXnf0-GEvBRLrTCIvTb4x5S48TgGkcIw-ZDyzqJgtpmkhs4FNLANXgCyr0oT10S6tAAlrL99bK_6-LyOHdD85pBiByn--bJJCKMDpC5spGGXl6PGoLUK7GwooQD5eYZ_Ki3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_p3GmohvbhuXcrmO5Jl1Bl-qSLCh6dJQN1IG9ip9T4L9XkGAHNMZOWsGoq7ntDlxGolNehbCtem7DCYA9WxbXjPs9VVGdCuDsg_VjvAEN7wrSlgIlv3SKgJxEe7AI5vHX-CsWw-jAadaIDv3cayLdU-cHI6RjXc7F9t1efQlH5PNHyMkBjFwn5jJUrJeFuZhxOaBmUJMcN4A4dQ39ZU8GywafjnOLSrT18Tq3ddMmuyX-wZrWlgHOx-n5OeenxG_es5ic_laJfRIjVHPf02aY5IiaTaI-K7_FoBTKLcdMbvVp8DWS6K4ecX29YId8XdL0BtWzkmy5idJYfVgyGwgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم‌اکنون حملات ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124772" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124771">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRsdoijQHPzeTa1aj4luFAUgQKKgYy9xw-hSi1vciBXN_JEp7xw62K57gb_nSKn_rbcZXkivyylpNh8VrkA19HVC5Yip6rgApzQ9q-BKIpflP8yZHlKdQMYy7lq6KRBQTEKYJdcPPg5itqWVNQs_3W1A3lk9dEdJePMK8rZRkVuduNP7mT_r3wpwY0GOPYjI63qVkPTvtqI3MXQV0hrQl8MleujB7H-5Uq4az1l3VW95tzSSzl9u3qlhRjKO-23WwxrcWXYSzPHzSmtROgZW8xJMBP0SGfgtfqhgxC2bI9Xu_DuqpRpWO5rrq4G0yFwAtxaW-EUoq0yH966JoV8b9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واحد سگ‌های اوکتز ارتش اسرائیل برنامه آزمایشی‌ای را برای آموزش سگ‌ها به منظور شناسایی و هشدار درباره پهپادهای FPV حزب‌الله از طریق صدا راه‌اندازی کرده است، که هشدارهای زودهنگام به سربازان، به‌ویژه در شب یا شرایط دید کم، ارائه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124771" target="_blank">📅 15:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124770">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
هشدار نیروی دریایی سپاه: فقط مسیر تعیین‌شده ایران برای تردد امن در خلیج فارس است / شناورهای متخلف هدف قرار می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/124770" target="_blank">📅 15:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124769">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxo5n-_PiJwMc_q_HwPL8Y-U4RkAroybSBHbvjWf54qTAJEMbE72aeVCODnoOqxCWXPVjI74T9WI4BdsYktcaSKkWPxq4uIv1U56ufQ0l9yBUO-oBuxNOMBqIpwlhBqk6PUuAJrR2JVbgIvjxQ_5PrvGmwBxtntOiRL3ugpl9gO1pjAZ58ods6WXQXmislSXWFAH-PqSY-VflQuX96b0so6aO33q1o6n95hyT9Xr5kPj3hjwXdxNbfzABQnQF4Q7mtxJGeNJXEhl3Ptnd_ACwtFY-t82niTl_KhljN6pvEe4eRLC14stdkRo9uSmPeku4ypoiKQqdkVoHsfD2qDcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجوز پوتین به نوردلاین برای خرید سهام توتال در پروژه آرکتیک ال‌ان‌جی ۲
🔴
ولادیمیر پوتین، رئیس‌جمهور روسیه، به شرکت نوردلاین اجازه داد تا ۱۰ درصد از سهام پروژه آرکتیک ال‌ان‌جی ۲ را از شرکت توتال انرژیز خریداری کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/124769" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124768">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036437ff69.mp4?token=P0318qudaizM0YGQd7_kJiOJZAQaYaUlwW99K4AjlhjL4PBo87tElMFbr2LzS06vp_PXEW8Inp8_pgl1O5Fj-MSAVNqPFjtZHCTZdzvJepEEelO85aHnXFFrBUoyDreGMTGmb5i7cA6CouaP4JnuM9haN4iuiyJEI-NTBqlnEuQ_U0sAqa0NTv-DCZQWBoeYp80bb4clYZAz_Rh7tlDC1JrodG5qOgiMdDA2EkVXMIm9FKMXy9sFwPWelgRmlDNLJc7bdRuxYiPhkLjSncxbdj6vuUP-XhzeM-twWKgpWamYSa1_ZNB7W5voGydqJ_vTx3wHwh8d0z-OOa34uAuvyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036437ff69.mp4?token=P0318qudaizM0YGQd7_kJiOJZAQaYaUlwW99K4AjlhjL4PBo87tElMFbr2LzS06vp_PXEW8Inp8_pgl1O5Fj-MSAVNqPFjtZHCTZdzvJepEEelO85aHnXFFrBUoyDreGMTGmb5i7cA6CouaP4JnuM9haN4iuiyJEI-NTBqlnEuQ_U0sAqa0NTv-DCZQWBoeYp80bb4clYZAz_Rh7tlDC1JrodG5qOgiMdDA2EkVXMIm9FKMXy9sFwPWelgRmlDNLJc7bdRuxYiPhkLjSncxbdj6vuUP-XhzeM-twWKgpWamYSa1_ZNB7W5voGydqJ_vTx3wHwh8d0z-OOa34uAuvyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما خیلی خوب با هم کار کردیم. من «بی‌بی» رو خیلی دوست دارم و همکاری خیلی خوبی باهاش داشتم
🔴
می‌دونی، ما تو شرایطی بودیم که اون نخست‌وزیر زمان جنگه و من هم رئیس‌جمهور زمان جنگ هستم
🔴
ولی در کل رابطه خیلی خوبی دارم. با هم خوب کار کردیم، نتیجه هم گرفته شده
🔴
همیشه هم همین‌طوره. بدون آمریکا اصلاً نمی‌شد انجامش داد، همه اینو می‌دونن. ولی ما تونستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/124768" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124767">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FEjLS6FnjTPm9fP_KST9bemFKdSkzI2SYsam83r1zB9ntW6k1s-flE8pC3tV6KwaIDs6jXXEzZmgSWqEyUPxiolCO_A3_usgGtayMJUoptLINMfTAxlB8qof18dkoJLAfQHlbo9ClWbkfdePyUGa-wJsndRr3UGlyRlhxN__IiBcm7W9sbQXRJ-3rImvYi7eernV1IqC54RcWst1pWDXqfn4w_5NVGCDkLBp_3V472K1US7MCJdATU9EO6-QKrJxjLLkCfOYp_QFFBy_kvvWutDL2zV5Ug7ockxhyStMCaf1ulXk7-098suyLpBHUzMTkosnbRJYZ46zzghRzOok-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/124767" target="_blank">📅 14:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124766">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سپاه : ایرانیان هرگز تسلیم شرایط ساختگی و دستاوردهای دروغین دشمن نخواهند شد.
🔴
دشمن مجبور است قوانین جدیدی را که ملت ایران و نیروهای مسلح در میدان، به ویژه در عرصه مدیریت هوشمند و کنترل تنگه هرمز تحمیل کرده‌اند، بپذیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/124766" target="_blank">📅 14:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124765">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d02ae267.mp4?token=iPiS03Hp1I2jMtlY900434qscn0D4y2JvkiokD9A1LJJjcMeat4tLBTOYnq3D36kwAsD-M1SzpPrrkiDNj4Gzqati8UeHnE45E08hFujV32q0BvfPYWHnljp0IH7cbYhRpRigBZLmXMt2AtYQ1BurY2Xikol3Q0337MX_eJJh02h9hqnE6iYdK3hfNX3Gi7GE1P-TubHBz3OrcfPdXW_YYToZivFbgCJmXDqJ9MN_UhCOcEB2CMkLwNOt2O4uG2giw7nyT02dp8dmP217w2WcJwPJJ0FmOFixV2eombyRhZHoqYXoUUykoJNLGyv4_a0dHv0H5tmKlKwa0NxDFCop4RdKsyAYOkeikXDTzZ9-1UjirhoKtzrPg6M5M03oDzyYcVaUAoL8Jwe_Y-re4-UFoQAD8ZE9ocgcmxHsAK2hv2HnbvalVKpS9ARsCbWyOEQwjflbMSHHkYRiuynR038S1SbZY91CbL1z0whj01_vBfXnhQkBBdnlQt5euP5lQxHbET9AWvBCIuY865x4wYyNSCKda0-gPhTSTAI95CDb26PSTK3ZUQjwg2TKmd2YMqDKe-cxX5-RWufnbmsTeF_M-sy8XAB1ot96g0AijHnlpL8ab9vQ7rK1WXpk3d_hToLBWTxgaFyTTfz8nrfzrZTa0Bew3bIRjy4ZwdP2AvS5KI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d02ae267.mp4?token=iPiS03Hp1I2jMtlY900434qscn0D4y2JvkiokD9A1LJJjcMeat4tLBTOYnq3D36kwAsD-M1SzpPrrkiDNj4Gzqati8UeHnE45E08hFujV32q0BvfPYWHnljp0IH7cbYhRpRigBZLmXMt2AtYQ1BurY2Xikol3Q0337MX_eJJh02h9hqnE6iYdK3hfNX3Gi7GE1P-TubHBz3OrcfPdXW_YYToZivFbgCJmXDqJ9MN_UhCOcEB2CMkLwNOt2O4uG2giw7nyT02dp8dmP217w2WcJwPJJ0FmOFixV2eombyRhZHoqYXoUUykoJNLGyv4_a0dHv0H5tmKlKwa0NxDFCop4RdKsyAYOkeikXDTzZ9-1UjirhoKtzrPg6M5M03oDzyYcVaUAoL8Jwe_Y-re4-UFoQAD8ZE9ocgcmxHsAK2hv2HnbvalVKpS9ARsCbWyOEQwjflbMSHHkYRiuynR038S1SbZY91CbL1z0whj01_vBfXnhQkBBdnlQt5euP5lQxHbET9AWvBCIuY865x4wYyNSCKda0-gPhTSTAI95CDb26PSTK3ZUQjwg2TKmd2YMqDKe-cxX5-RWufnbmsTeF_M-sy8XAB1ot96g0AijHnlpL8ab9vQ7rK1WXpk3d_hToLBWTxgaFyTTfz8nrfzrZTa0Bew3bIRjy4ZwdP2AvS5KI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد FP-1 اوکراینی در جریان حمله امروز صبح به سن پترزبورگ دیده شد که تنها چند متر بالاتر از سطح آب در خلیج فنلاند پرواز می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/124765" target="_blank">📅 14:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124764">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iStkS_0G3MGcm7Ui_fTF53KPsc_qeBkNIOCUTnngAkHJTTO8AxF2PK3x7_NhKE6lhnGGcvSqfC5cZYHtlF4ftyfuBQEmel1nq7IgI_y2SPi19cE_k0fWq9KJKkdQmfmg18bQPydJuv4iXBmX2AKThlarQS3dGG_xvkl5jmCqu_nOsn4TBzuk7nKcQg7cbh1AMhzjLl_Wckq3v_pBervfFH7C8e_PI5nu2lHzdJawZErsovswA_mHntr2y3XgWta7oK-_UyOwlnIsgqCTAkX3zYuruv5nDl18nOJKY90o2C2B1BVLQ2elJfIyJWzLD9_AAnAUTrKybbR2MM7SKFIUpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت حساب ایکس خبرگزاری صداوسیما که همزمان با اتفاقات دیشب منطقه، مورد توجه کابران خارجی قرار گرفت
‌
🔴
تجارت به سبک آمریکایی:
🔴
۱. یک پایگاه نظامی در کشور شما می‌سازد.
🔴
۲. از آن پایگاه به کشور دیگری حمله می‌کند.
🔴
۳. سپس یک سیستم دفاعی به کشور شما می‌فروشد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124764" target="_blank">📅 14:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124763">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT_P80ZjkAgH6EyXkHj1xGZKiJh3OkadTW00RiI-d0awDQ4lEFdkh3Nwzm83lLI44ZzF2zrAWIP9_s-3AFZli5ID9F5mmsdVoHYCyQK3swVc_YRgDsDRzDaAogXyUBCqqsiK5M4z5yd798WI0PEH9z_9h1QhRM8z7y53v0ToQbNPIbs1-RQge6EhYFvXDGlIR7lDv5xVLSPIK_lSUiJHHEH8-1zsje4d5lktr9BX1qMeGY4IRDxEFO8_-TJXwt9L47eC6HHM0zMUZvIfi15RJ1Pc3F_MYGi9wbddOBpupYbmvV6AX6smRawTZzbHe366dShWpiazULGW0aiH80-obA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین ابرنفتکش در تقریباً یک ماه گذشته در تأسیسات اصلی صادرات نفت خام ایران در شمال خلیج فارس پهلو گرفته است که نشان‌دهنده ماهیت عمدتاً مؤثر محاصره آمریکا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124763" target="_blank">📅 14:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124762">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c24b9554.mp4?token=eQSTD1mt4p3XcMFLkVdKvjuna7wkLYkvkKX0HLsHqMUvwZwS0xFocC_SnECZj51PCYqnaWPx-tksaBMOhLg3cuD4DTBPoU-AAJmqRiUARjPq2KMo4UUkBMWAHUYqJ0qadKbc3PcyMVdXTX947MBY8MHeBMR43CgkGr0U-sXgYvt4ifErSileeqE_3TN4aEdquTYx50fbfncT_LmrowRwdkDEsqh7dkKyXMN4KVotfdUor0YLLCXRygSGtI62Pfls_AL2SyuX8iFkLphpYQYBuYTTMv2tznHQoWvWuY7pNCWlRaHXGVsIqeQhaQXAiqfij54Ijd-LMqPkO3TrK5uOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c24b9554.mp4?token=eQSTD1mt4p3XcMFLkVdKvjuna7wkLYkvkKX0HLsHqMUvwZwS0xFocC_SnECZj51PCYqnaWPx-tksaBMOhLg3cuD4DTBPoU-AAJmqRiUARjPq2KMo4UUkBMWAHUYqJ0qadKbc3PcyMVdXTX947MBY8MHeBMR43CgkGr0U-sXgYvt4ifErSileeqE_3TN4aEdquTYx50fbfncT_LmrowRwdkDEsqh7dkKyXMN4KVotfdUor0YLLCXRygSGtI62Pfls_AL2SyuX8iFkLphpYQYBuYTTMv2tznHQoWvWuY7pNCWlRaHXGVsIqeQhaQXAiqfij54Ijd-LMqPkO3TrK5uOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من می‌تونستم انجامش ندم، ولی نه، چون این موضوع خیلی مهمه
🔴
اگه انجامش نمی‌دادم، اونا خیلی زود سلاح هسته‌ای می‌داشتن
🔴
حتی ممکن بود دو هفته بعد از اون حمله‌ی B-2 هم به بمب هسته‌ای برسن
🔴
یعنی اگه اون کار رو نمی‌کردم، عملاً خیلی زود به سلاح هسته‌ای می‌رسیدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/124762" target="_blank">📅 14:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124761">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d15be3fa5.mp4?token=ucS7QTLdZPWQOSjYlpumslfWwRE5v1X3SGXuT4PPtzMnHdzKVHKY9ISlrhk0Caau-fv2TozJlgRmoVzG21fAiJpzAFkzZ8JsMpWNafw41qKVsEIXzIpTK28iBS7R9pkbT6c9qStEvOtvumCp_iHBqLMMkug_PUe0lU0Yf778u0pL6-5BCTX7J0tzm_doqtf_7Cu-PbNey-5teKi8hAAw2saD0qCkn3So3e-DyK9tDBF_zNdiM6DnTQo-C-in1IbpeaEpk9v7ND7ZGdqYnCohHkxGHg2836VeDJ61YciUfxZMWDXp5C1KTIZhz6tvVSisK7t1Y8Q7VM5y6S2pFyUyw2SV4y-cOeTUDbHDIwIdfE7hGIUxRTsdsDxFs9c0UB4Flnx1xySfZV-4Rm13XTTP-jU56fV10m1NmCdpJJ2mBBYEjqb3KytbOSSFMhwIbLLrusABdFFMKWpbP0Xa-2OR5I_YcpvxKUG8ZD3zJsRsMJy6g0fEtjku_BCE2k3ERCO4DPFTopp9aLoRhmr3NNjRgLqohIEqdY2jdKd8YB6VMR1UUZegBV2xec9FsCj_eslXU3Zz_GIbKLPtN06SPLCXtWyCVqEAyEkMj6yYP-wpAYRchjT4cVV6x74hOk8q7kM9x867d6aWx9ceqXdn30U5_Qr4ahi3FbRb3Zs51K4bFuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d15be3fa5.mp4?token=ucS7QTLdZPWQOSjYlpumslfWwRE5v1X3SGXuT4PPtzMnHdzKVHKY9ISlrhk0Caau-fv2TozJlgRmoVzG21fAiJpzAFkzZ8JsMpWNafw41qKVsEIXzIpTK28iBS7R9pkbT6c9qStEvOtvumCp_iHBqLMMkug_PUe0lU0Yf778u0pL6-5BCTX7J0tzm_doqtf_7Cu-PbNey-5teKi8hAAw2saD0qCkn3So3e-DyK9tDBF_zNdiM6DnTQo-C-in1IbpeaEpk9v7ND7ZGdqYnCohHkxGHg2836VeDJ61YciUfxZMWDXp5C1KTIZhz6tvVSisK7t1Y8Q7VM5y6S2pFyUyw2SV4y-cOeTUDbHDIwIdfE7hGIUxRTsdsDxFs9c0UB4Flnx1xySfZV-4Rm13XTTP-jU56fV10m1NmCdpJJ2mBBYEjqb3KytbOSSFMhwIbLLrusABdFFMKWpbP0Xa-2OR5I_YcpvxKUG8ZD3zJsRsMJy6g0fEtjku_BCE2k3ERCO4DPFTopp9aLoRhmr3NNjRgLqohIEqdY2jdKd8YB6VMR1UUZegBV2xec9FsCj_eslXU3Zz_GIbKLPtN06SPLCXtWyCVqEAyEkMj6yYP-wpAYRchjT4cVV6x74hOk8q7kM9x867d6aWx9ceqXdn30U5_Qr4ahi3FbRb3Zs51K4bFuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آتش‌بس و این چیزها آیا هدفش اینه که ایران رو در حالت سردرگمی نگه دارید؟ یعنی دارید بهشون پیام می‌دید؟
🔴
ترامپ : نه، چون بعضی‌ها داخل کشور می‌گن این وضعیت براشون اضطراب و سردرگمی ایجاد کرده
🔴
این خوبه این خوبه که هم اون‌ها سردرگم باشن، هم ایرانی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/124761" target="_blank">📅 14:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124760">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c32e4aeb.mp4?token=Z4jeCIYQ8jBjxkqo1vmZkdVJCCWO-TTRdm97qGTWd989CcKtQu-zBr14NldqvDwblS8tdGZZJKGDUpj1z87170b1TviG7XijnY1UDCWwQbVomflg2WMf7YojhBK1luNltPvGGfRUqHFZ_9bpHTVZJ56zpihnhGP9XFcwNtWnFVbDEkbAQgXndqRiD7aGsek-wK317Pp0ESrRxkvNCKPbwkq_vmwgcYPunHoANd8DBAEj-BCevRmU5aH_ZfqF4HCofT4U-ra4z4tdS2yy-rbzD_KNulvg8ViB0pYX_yNIDbtduMrsEWA2yXVZgVdSj7pwiWxVrsOnBgkWXnQWihSbDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c32e4aeb.mp4?token=Z4jeCIYQ8jBjxkqo1vmZkdVJCCWO-TTRdm97qGTWd989CcKtQu-zBr14NldqvDwblS8tdGZZJKGDUpj1z87170b1TviG7XijnY1UDCWwQbVomflg2WMf7YojhBK1luNltPvGGfRUqHFZ_9bpHTVZJ56zpihnhGP9XFcwNtWnFVbDEkbAQgXndqRiD7aGsek-wK317Pp0ESrRxkvNCKPbwkq_vmwgcYPunHoANd8DBAEj-BCevRmU5aH_ZfqF4HCofT4U-ra4z4tdS2yy-rbzD_KNulvg8ViB0pYX_yNIDbtduMrsEWA2yXVZgVdSj7pwiWxVrsOnBgkWXnQWihSbDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: انتخابات ۲۰۲۰ تقلبی بود... وقتی پای انتخابات به میان می‌آید، ما از برخی کشورهای جهان سوم بدتریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/124760" target="_blank">📅 14:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124759">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-wk3mhhVep9tmCODtS-daveES8vFYFuxOh8lan5KdnnSNtyl4Eyb9wRyAkl4enGQIq5KL9YSimOW4GWGhGjP6x1G7koS6FhdONWr6hFqd8ODnCueccskGHxnKZfZv1W4I9-5ZprayGwFXOV9f8CZofxeA8aXDLxpWCxuhKCiBG1NG0X4vEy4zK8WMu8XGii4ahEjN_m6wPmM9EmPgH6-Zb8hcaNRbH0Y4blzCWERPvAqWY9IeIviDDXNBXuM61UVqpwZOWQcAYwqaUPVQo2wPgq594nlbl2qfTrH7UeYEJQ2_toah4cuBpww8Xxt65GAlEqDAjsz_Lc6vLn5Nl4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی‌زاده ، کارشناس صدا سیما: فروش نفت ایران بعد از محاصره دریایی به صفر رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/124759" target="_blank">📅 14:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124758">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
صدای انفجار در بندرعباس و قشم / استاندار: مهمات عمل‌نکرده منهدم شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124758" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124757">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: ونس و روبیو اگر با هم به عنوان یک تیم در انتخابات کار کنند، شکست‌ناپذیر خواهند بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124757" target="_blank">📅 14:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124756">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ادعای کویت: ۶۳ نفر در اثر حمله ایران به کویت مجروح شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124756" target="_blank">📅 14:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124755">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
تسنیم: علیرغم تخیلات ترامپ، ایران در این چند روز هیچ پاسخی به آمریکایی‌ها نداده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124755" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124754">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fcf127299.mp4?token=s2-M9wAgffWsz3Jv3fpEfpMMI-ACShSEyup0US58VYpsna8dDHZcWXRE3-pnQH8ola-QUwBeXNrejxk58y_ovZ_KxIr8OkNKTbdBI9nmUWL1_rV1M4TsFjIg3eOKbc-B15XHWCYW_gMS3_xI9-UAyi7UE1NXSntN38cBVEVryWVnwMSM4VH_uf8mwQCYFuMx65AwNoCQFX5Pwc-jEZD9O9bhB4K8_BtaslZ7VrOJin3Xj9C3LRHq3iWXqPXmE6djP6pZHRI2IkZ7FtIbzBtdjcFRxyTZdtQzwxTtyn6VK7xanAU5-zbOtpyO3dC55D27HEqPC4ceUfVFzXRq03EJ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fcf127299.mp4?token=s2-M9wAgffWsz3Jv3fpEfpMMI-ACShSEyup0US58VYpsna8dDHZcWXRE3-pnQH8ola-QUwBeXNrejxk58y_ovZ_KxIr8OkNKTbdBI9nmUWL1_rV1M4TsFjIg3eOKbc-B15XHWCYW_gMS3_xI9-UAyi7UE1NXSntN38cBVEVryWVnwMSM4VH_uf8mwQCYFuMx65AwNoCQFX5Pwc-jEZD9O9bhB4K8_BtaslZ7VrOJin3Xj9C3LRHq3iWXqPXmE6djP6pZHRI2IkZ7FtIbzBtdjcFRxyTZdtQzwxTtyn6VK7xanAU5-zbOtpyO3dC55D27HEqPC4ceUfVFzXRq03EJ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: مجتبی خیلی آدم خوبیه، من واقعا دوس دارم از نزدیک ببینمش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124754" target="_blank">📅 14:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124753">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076531569b.mp4?token=Xixe44jubbZ75QGl4Woade2u7xHg3DUigJ-CjdtuG97jaMSPnYcpLE0sgR8PkTKT0kLjZPqD3TQSapQiN65yoeB4LNVoTgEimZ_akQJi-AwuCFRO-XGm0A8y2ve1bidpMv4_1FZXM0i51gZmkDyrZACmBQz9CvDFbPcFoM10qjDM4IcvUO8tCehACe6Z4XZ4-1zQUE7wHP-NRom3oioZBpqnUa8W3eJ8_r4crsvYhtPjlb0BMB4cyyh22y0IFcZBeMmETlUKN47cY3rIgnbqlqqQefzjbFicWeZCraxtbjc4CrBS5kWqa5XrI5SmQFkmkiI5tu3zCZEt2DnQixRx6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076531569b.mp4?token=Xixe44jubbZ75QGl4Woade2u7xHg3DUigJ-CjdtuG97jaMSPnYcpLE0sgR8PkTKT0kLjZPqD3TQSapQiN65yoeB4LNVoTgEimZ_akQJi-AwuCFRO-XGm0A8y2ve1bidpMv4_1FZXM0i51gZmkDyrZACmBQz9CvDFbPcFoM10qjDM4IcvUO8tCehACe6Z4XZ4-1zQUE7wHP-NRom3oioZBpqnUa8W3eJ8_r4crsvYhtPjlb0BMB4cyyh22y0IFcZBeMmETlUKN47cY3rIgnbqlqqQefzjbFicWeZCraxtbjc4CrBS5kWqa5XrI5SmQFkmkiI5tu3zCZEt2DnQixRx6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : گروه‌های مختلفی از آدم‌ها هستن؛ گروه اول دیگه نیست، گروه دوم هم نیست، بخشی از گروه سوم هم حذف شده
🔴
و اون آدم‌هایی که الان باهاشون طرف هستیم، همونایی هستن که الان کشور رو هدایت می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124753" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124752">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owf4wVZuCUg_rvZnVKgGd0T3enzY532FtcQH5uQpyn40vsX2AxZ4pkTrUjC2qfjcu6-2C6hJTA0kVi_acELQdTCm4yx5PnPfFxlbAFLJeOOqy2gfqacnI2WcBaeP3_WVsexpR86arBgjzla-2JH4qgdBP5OWpV_8J3UQ9r3_E5TTzIlL7xr_F4V5CoKLkQ9S8yVXnFsSBkJvcpfxLqjzN5rfM-0A6eHq7xk6A2rEZwkPu5sHfYFVGbOkYmiiMXFfi4mTZvuUWx1XRCpXgI5FAeU5_fwmIRXjDcs79MKl8BzthkIkj__HuuSJFKK683r5ZDwu7PVY3Zz_AtfL3yH7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش طلای جهانی به اظهارات ترامپ در مورد چراغ سبز رهبر جمهوری اسلامی ایران برای مذاکرات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124752" target="_blank">📅 14:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124751">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: در حال حاضر نیازی به اعزام نیروی زمینی به ایران نداریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124751" target="_blank">📅 14:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124750">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0becb1cf02.mp4?token=rjOmpr-nRKtrRyAuIp8WeQa6JjdXCeMR4IEmzdUawQoVmmw31wHCMQHcZ2d-4h0h60QhsY3ziYSz8xQJ4X6CwZ84OsdEhB-z77N3J-Qp8vVDtvz9wMMs8XzdfiBmlsHoA98xYrdkmCPnx4TGJJWojWyrvBt9TGgZzxfQPcsHWXrT2s77IOiRoFj0xITom215ohsvTmbT0yoTcHBv4BKSbrmPhrTxLJxXh7tOn67bs92mhAwdtVvZ3hhy8OHYbPLxMjPf6DWRmGo3QWJQ9qbOLgYArZtNXGphDEVFaGZmVnYtB8SH4C9OSKM-Qs6l_LE6b6SAYqcmFsnaSbNZyD4czQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0becb1cf02.mp4?token=rjOmpr-nRKtrRyAuIp8WeQa6JjdXCeMR4IEmzdUawQoVmmw31wHCMQHcZ2d-4h0h60QhsY3ziYSz8xQJ4X6CwZ84OsdEhB-z77N3J-Qp8vVDtvz9wMMs8XzdfiBmlsHoA98xYrdkmCPnx4TGJJWojWyrvBt9TGgZzxfQPcsHWXrT2s77IOiRoFj0xITom215ohsvTmbT0yoTcHBv4BKSbrmPhrTxLJxXh7tOn67bs92mhAwdtVvZ3hhy8OHYbPLxMjPf6DWRmGo3QWJQ9qbOLgYArZtNXGphDEVFaGZmVnYtB8SH4C9OSKM-Qs6l_LE6b6SAYqcmFsnaSbNZyD4czQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:می‌توانم پاسخی بدهم و سپس، ۲۰ دقیقه بعد، وارد دفتر بیضی شوم و متوجه شوم که پاسخ من اکنون نادرست است.
🔴
تغییر می‌کند، می‌دانید. واقعیت‌ها تغییر می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124750" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124749">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985f8781a1.mp4?token=AB7CIUPo-JUelG5wQ00MZ8UQL9AywSaJKV9Z42rPCzcqdwULbOX_5qo1kobV3-dcKIMHO7cO2a_nnk53CEByADUIIrKbzB8cW6ABw3IkKInluiMxtR8A9gPd2LfYGgeX78f5PTlaC1nWMfiDRYtZSnGYtkQGwGFBFY1U-wOixMWMZl9rexLWaa4oyhfsTN9C-WVAFD8fBmF6nT0V3PnTKT9KKmhg8m_8SJU25U4WppE1b4iNl0gHJeOt5M_OqSR2NGDAdp1aLU3eAHwJfHsMTCAVETqHSgaia8btUrrLqIU3COvoS3zY6duKcRq9jdfNb6VbnOvcf9V6m_7v7yrmog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985f8781a1.mp4?token=AB7CIUPo-JUelG5wQ00MZ8UQL9AywSaJKV9Z42rPCzcqdwULbOX_5qo1kobV3-dcKIMHO7cO2a_nnk53CEByADUIIrKbzB8cW6ABw3IkKInluiMxtR8A9gPd2LfYGgeX78f5PTlaC1nWMfiDRYtZSnGYtkQGwGFBFY1U-wOixMWMZl9rexLWaa4oyhfsTN9C-WVAFD8fBmF6nT0V3PnTKT9KKmhg8m_8SJU25U4WppE1b4iNl0gHJeOt5M_OqSR2NGDAdp1aLU3eAHwJfHsMTCAVETqHSgaia8btUrrLqIU3COvoS3zY6duKcRq9jdfNb6VbnOvcf9V6m_7v7yrmog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:ایران سربازان بسیار کمی دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124749" target="_blank">📅 14:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124748">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=eyFpQqvc5rCo5lvVbYkPKS_KDeHlceQuNCXcmkYoNO7Fcg66m1xZvKzMl7R5WbKu_Kfzpaj0WxXqWcMwVej2y5uxMcvyUjFVoVDJT3aqwRc9WPbNL5_mWC14qYX5Io05T_U4wfncRBv45iLdqHzfFhXJJu3FqizXdrMDaZK5eUu2QNQUq0cQ0AXKT26GAeEzufJXOTIJK9q8Y3u8DPdG5VSBHsZD5sSHsahRmZwDikp4-Z2BJ7iW2AL-kOPg_y442XK4ZfHwE9XI8wmHm3hmLLjOKYiK3JLiW-76slZv-n6mxeuIU1_HvRAFlq-VhH4_rKlTwgttnBtPuVQOOl0xYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=eyFpQqvc5rCo5lvVbYkPKS_KDeHlceQuNCXcmkYoNO7Fcg66m1xZvKzMl7R5WbKu_Kfzpaj0WxXqWcMwVej2y5uxMcvyUjFVoVDJT3aqwRc9WPbNL5_mWC14qYX5Io05T_U4wfncRBv45iLdqHzfFhXJJu3FqizXdrMDaZK5eUu2QNQUq0cQ0AXKT26GAeEzufJXOTIJK9q8Y3u8DPdG5VSBHsZD5sSHsahRmZwDikp4-Z2BJ7iW2AL-kOPg_y442XK4ZfHwE9XI8wmHm3hmLLjOKYiK3JLiW-76slZv-n6mxeuIU1_HvRAFlq-VhH4_rKlTwgttnBtPuVQOOl0xYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
🔴
منظورم این است که من کسی هستم که این را شروع کردم.
🔴
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
🔴
اگر من نبودم، اسرائیل وجود نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124748" target="_blank">📅 14:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124747">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ: من از درگیری جاری بین نتانیاهو و لبنان نگرانم.
🔴
«به بی بی‌گفتم تو دیوانه شده‌ای؟ این چه کاری است می‌کنی و اون قبول کرد دیگر به بیروت حمله نکند….»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124747" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124746">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ تو مصاحبه پادکست : وضعیت ایران خیلی سریع داره تغییر می‌کنه، و در نهایت اوضاع خیلی خوب پیش می‌ره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124746" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124745">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: قیمت بنزین به زودی کاهش می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124745" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124744">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / ترامپ : احتمالاً تا روز کارگر (Labor Day) بتونیم محاصره ایران رو برداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124744" target="_blank">📅 13:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124743">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ : هیچ‌وقت به دیدار با هیچ‌یک از مقام‌های ایرانی فکر نکرده‌ام
🔴
آیت‌الله ایران تو مذاکرات با آمریکا نقش داره و تو جریان گفت‌وگوهاست.
🔴
احتمالاً یه زمانی با آیت‌الله ایران دیدار خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124743" target="_blank">📅 13:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124742">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / ترامپ : داریم روی رسیدن به یک توافق با ایران کار می‌کنیم؛  ایران قبول کرده که سلاح هسته‌ای نداشته باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124742" target="_blank">📅 13:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124741">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رئیس سازمان هواپیمایی کشوری: ۹۵ درصد بلیت پروازهای لغو شده جنگ تعیین تکلیف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124741" target="_blank">📅 13:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124740">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر حمل‌ونقل ترکیه: ۹ کشتی ترکیه ای در تنگه هرمز قرار دارد که ۷ فروند آن درخواست خروج داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124740" target="_blank">📅 13:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124739">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
قیمت نفت: ۹۸.۳۴ دلار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124739" target="_blank">📅 13:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124738">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ادامه جنگ در تمامی جبهه‌های خاورمیانه به‌رغم آتش‌بس روی کاغذ
🔴
درگیری‌هایی که در سه سال گذشته خاورمیانه را درنوردیده‌اند - در غزه، لبنان و اکنون ایران - همگی روی کاغذ در وضعیت آتش‌بس قرار دارند. اما در عمل، جنگ در تمامی جبهه‌ها همچنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124738" target="_blank">📅 13:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124737">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
شورای همکاری خلیج فارس: تجاوز ایران به بحرین و کویت، پافشاری ایران بر پیگیری سیاست‌های خصمانه را آشکار می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124737" target="_blank">📅 13:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124736">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
هاکان فیدان، وزیر خارجه ترکیه: ایالات متحده به وضوح اعلام کرده که نظام بین‌المللی فعلی و سیاست خارجی که آمریکا برای دهه‌ها دنبال کرده، دیگر به نفع منافع ایالات متحده نیست
🔴
بنابراین، آنها در حال بازتعریف و بازطراحی چشم‌انداز راهبردی خود هستند
🔴
در نتیجه، شاهد ایجاد یک خلأ به‌ویژه در معماری امنیتی اروپا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124736" target="_blank">📅 13:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124735">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj52lKe_yGVTKzsscy6A_ItaYnEg6RaKldLUtmHiGPT9FMSTizx_EJR1I-us_wYuBkxP0q_efQJOv7NUEvB1lNdISMaqv0bMNGxrEXKYENswXQttzQYXHTdUsXsYRrxZ9IUkY4rBTx3mT3fxPnp_wEFuPeVk172ho3TE7x62AYkdhIco1FTuokezOOUSsNeU_1sAkhG0UegfiWpMwClCHajbc04RTHka7D_MkPWNyK4f1jukaMn6gidsUurZ6LIzFJAd9N7k2fr2apzV9SLtAdzhOLR5xuOWXiUQvhHYIrI4y0wDVNPLcL1HzaPvp4xUCGeH5yv7EWQzF5DGFbVhJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکارد تجمعات شبانه: جلسات مجلس برای تصویب قانون تنگه هرمز را در میادین شهر برگزار کنید، مردم با زنجیره انسانی از شما محفاظت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124735" target="_blank">📅 13:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124734">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061ee52229.mp4?token=i0-O1PHhHjfyFg04S7PLGrav1dycW3jinbWROTyC8IcMs9LHW2-4YXac63IISx8Y8ZYRgNfqLa5OnveZ1HPNEU5dsiUGRHRSLOGoUfvWZrPmj8p61mBGincIX6soZRtNd8pHGnVSytWPLpBRWaaUfzyBQaW1JMPcvHHcf_RsKgv0TyyWhybXLSqShM3M-XgFEmH0brQDAbUjHuF23e9xiLOqzmEU8yomlwM7oIXF2xwQQz4x7NdsYPWjbMOH5MMSjN4KrHKy_I4lggHcNQHdm_1TiCZwGDATOjaneehs7F8Gx7gXxK_jMPlMcZoMbjjnxDGiLP6vQEap8G5ReD7Pqh_togXb6cj3OdxWyqjKAB1yl9u9MLw3_lgJ30KN55PjyCjEL0m4DyZHW9Dyc0uaxG8b-IB3An6iulMJja0BmkpkId7I9V03E4pPZTH-dW4NUwsVoK_EhJ6fPDeQ5HRi77uJw9GsPNINhrrRnQTeyswm9yIuVinTSdxphij-9SC5OWxAgaJ7pI1NWYPXzQ680_Gdmify4tj982ETKwcJYsx5GwLwArkZoyPwWwKsQ_O0TLk0a-nfhBIZW2Ju_9m4P1yL1_P0fxqaGwoAo1bnwOIrqY-5G-lthWsdVTT144dQvGyz2t-8-vLZ-UXDEQfO6AmG43pR5LqBLJ0H97TfY4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061ee52229.mp4?token=i0-O1PHhHjfyFg04S7PLGrav1dycW3jinbWROTyC8IcMs9LHW2-4YXac63IISx8Y8ZYRgNfqLa5OnveZ1HPNEU5dsiUGRHRSLOGoUfvWZrPmj8p61mBGincIX6soZRtNd8pHGnVSytWPLpBRWaaUfzyBQaW1JMPcvHHcf_RsKgv0TyyWhybXLSqShM3M-XgFEmH0brQDAbUjHuF23e9xiLOqzmEU8yomlwM7oIXF2xwQQz4x7NdsYPWjbMOH5MMSjN4KrHKy_I4lggHcNQHdm_1TiCZwGDATOjaneehs7F8Gx7gXxK_jMPlMcZoMbjjnxDGiLP6vQEap8G5ReD7Pqh_togXb6cj3OdxWyqjKAB1yl9u9MLw3_lgJ30KN55PjyCjEL0m4DyZHW9Dyc0uaxG8b-IB3An6iulMJja0BmkpkId7I9V03E4pPZTH-dW4NUwsVoK_EhJ6fPDeQ5HRi77uJw9GsPNINhrrRnQTeyswm9yIuVinTSdxphij-9SC5OWxAgaJ7pI1NWYPXzQ680_Gdmify4tj982ETKwcJYsx5GwLwArkZoyPwWwKsQ_O0TLk0a-nfhBIZW2Ju_9m4P1yL1_P0fxqaGwoAo1bnwOIrqY-5G-lthWsdVTT144dQvGyz2t-8-vLZ-UXDEQfO6AmG43pR5LqBLJ0H97TfY4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
به دعوت صداوسیما میلی؛ اینفلوئنسر یا خبرنگار مستقل؟
🔴
از بهمن ۱۴۰۴ تا بهار امسال، معاون برون‌مرزی صداوسیما تحت عنوان «جشنواره رسانه‌ای صبح» سه تور اختصاصی برای تعدادی از اینفلوئنسرهای خارجی برگزار کرده تا روایت خود از اعتراضات و جنگ را مخابره کند.
🔴
یکی از چهره‌های اصلی این برنامه‌ها «بشرا شیخ» اینفلوئنسر پاکستانی-بریتانیایی است که دسترسی‌های زیادی از جمله دیدار با مقام‌های جمهوری اسلامی و حضور در تنگه هرمز به او داده شد و حتی به سخنران تجمعات شبانه حامیان حکومت در تهران تبدیل شد.
🔴
در همان روزهایی که اینترنت برای میلیون‌ها ایرانی قطع بود، شرکت‌کنندگان این تورها با اینترنت آزاد و لیست سفید حکومتی فعالیت می‌کردند تا روایت رسمی جمهوری اسلامی را بازتولید کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124734" target="_blank">📅 13:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124733">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7841f0ce05.mp4?token=VMpN_LlotrDiYi1bSGO25INbhqCoUBdLetGU3C4XT10DFMzPHHHzBjKhDPwPdftvq8OS1bjFQthgfcxCB1YT2UyxJ-2n9VamYp8cIV9ivEHwGc2EfGOw_gEY4gZWFVLtKsPOJ3Ofk8hbSV9bRX0vVsNUZAbNcflrM7QKhPiAiqrFq6z9ctRwD6VcYxHA3qLlyRsa_Hpmokw0smjBEJrsh1Od-FTux6SfffMGTze1ho8NFJ4odkeNAdNR2t5qX2qT9AaWtTTxs_arjCZGwbjxzagu7d4STU4Oz4y3j8sNsFY-uYYAYrExLTKX_CjG66hIzX8L4DHJbD2Yv4_TIlLASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7841f0ce05.mp4?token=VMpN_LlotrDiYi1bSGO25INbhqCoUBdLetGU3C4XT10DFMzPHHHzBjKhDPwPdftvq8OS1bjFQthgfcxCB1YT2UyxJ-2n9VamYp8cIV9ivEHwGc2EfGOw_gEY4gZWFVLtKsPOJ3Ofk8hbSV9bRX0vVsNUZAbNcflrM7QKhPiAiqrFq6z9ctRwD6VcYxHA3qLlyRsa_Hpmokw0smjBEJrsh1Od-FTux6SfffMGTze1ho8NFJ4odkeNAdNR2t5qX2qT9AaWtTTxs_arjCZGwbjxzagu7d4STU4Oz4y3j8sNsFY-uYYAYrExLTKX_CjG66hIzX8L4DHJbD2Yv4_TIlLASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از آتش سوزی در فرودگاه کویت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124733" target="_blank">📅 13:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124732">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزارت دفاع کویت اعلام کرد در اثر اصابت یک پهپاد انتحاری ایرانی به ترمینال فرودگاه کویت یک نفر کشته و هفت نفر زخمی شدند.
🔴
همچنین دو پهپاد انتحاری دیگر توسط پدافند کویتی سرنگون شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124732" target="_blank">📅 13:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124731">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ستادکل نیروهای مسلح و قرارگاه خاتم‌‌: نخواهیم گذاشت دشمن به آرزوهای شیطانی خود برسد
🔴
بیانیهٔ ستادکل نیروهای مسلح و قرارگاه خاتم به‌مناسب ارتحال امام خمینی(ره) و قیام ۱۵ خرداد: ملت شریف و مقاوم ایران، در سالگرد ارتحال امام خمینی(ره)، فقدان قائد شهید عظیم‌الشأن و شهدای مظلوم خود را در کنار پیوند عمیق میان ایمان، بصیرت و ایستادگی در برابر استکبار جهانی تجربه می‌کند.
🔴
جنگ‌افروزی اخیر آمریکا و رژیم صهیونیستی، چهره واقعی مدعیان دروغین حقوق بشر را برای جهانیان آشکار کرد که شهادت ۱۶۸ کودک مظلوم و بی‌گناه مدرسه میناب یکی از صدها جنایات آن‌ها می‌باشد.
🔴
ملت ایران در برابر تهدید و تجاوز، نه‌تنها عقب‌نشینی نمی‌کند، بلکه با اتحاد و ایمان، مسیر عزت را بیش از هر زمان ادامه می‌دهد.
🔴
نیروهای مسلح همگام با ملت و تحت رهبری فرمانده معظم کل قوا از آرمان‌های انقلاب و کیان کشور تا پای جان دفاع خواهند کرد و نخواهند گذاشت دشمن کینه‌توز به آرزوهای شیطانی خود رسیده و خون امام شهید و سایر شهدای والامقام پایمال گردد.
🔴
دشمنان آمریکایی و صهیونیستی در برابر اراده الهی نیروهای مسلح و امت بصیر و آگاه، چاره‌ای جز تسلیم نخواهند داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124731" target="_blank">📅 13:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124730">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea45369d6d.mp4?token=WpV0cfgh66InXl_clJnV59pHYT-vaiK7shWU9rHswBCLPm55tc9K8LWauWuK6BXmpc3nX-M4bQvOuDO1CjIaKhJOMo3maNrHlsRkVSoRpDDVdMVSOCs0FeyJhGC3Yqw9AqVEjvjk9HSDzRCfRCoZ87fhzJoJ7a5aD-cTS6yF3m6-MmsXmozGn2NIC6HWP-6lNMhj8T8t0NYduneCAEgFGNgS3xcDAzQe-ClHOvltjRPOmcrmj6LkjMIozbbuYvA80C5C0mb9s0aTBQpGHsGb__5L62OJQO0ftg78I2dW4tA4yDgGon8pJ5LZUBkZrvmtfLmRTW5_PHyH1KUp8jBHjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea45369d6d.mp4?token=WpV0cfgh66InXl_clJnV59pHYT-vaiK7shWU9rHswBCLPm55tc9K8LWauWuK6BXmpc3nX-M4bQvOuDO1CjIaKhJOMo3maNrHlsRkVSoRpDDVdMVSOCs0FeyJhGC3Yqw9AqVEjvjk9HSDzRCfRCoZ87fhzJoJ7a5aD-cTS6yF3m6-MmsXmozGn2NIC6HWP-6lNMhj8T8t0NYduneCAEgFGNgS3xcDAzQe-ClHOvltjRPOmcrmj6LkjMIozbbuYvA80C5C0mb9s0aTBQpGHsGb__5L62OJQO0ftg78I2dW4tA4yDgGon8pJ5LZUBkZrvmtfLmRTW5_PHyH1KUp8jBHjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشر شده از خسارات وارده به فرودگاه بین‎‌المللی کویت در پی درگیری‌های بامداد امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124730" target="_blank">📅 13:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124729">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAwzQS-xLELVLkWdEi2c5oRq-gJe8ydeWrUTHeI7hX46x-SX_NqePUIGMfa3obGr6leboMOzv_YKXzcVu4OJ_tbUEKzAoPMZ0FSptGhwk3-2n3h0EqOcQ7COEBI3_P_uX98CjGr0k0vZIUSjFimiCnrnBLAH-U4MS7UNV5mwsKSdRDZ-RmelhrL_4JNZAcj4CF4DdIFmWcVQ6eu5Yk2znNCiiNyg9Ps1DK7xCeaBJSaHO2rihF1ZOI2XzX-5scwxl38y9W1cKy7x8bdfBqNlI6WZV0QYMi40EfBNlJtjwsERfqQjumr9YLPPNOra5gd2aMWlulvuEasmhnxyjt1Peg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید محمدرضا گلزار که حسابی دل طرفداراشو برده :
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124729" target="_blank">📅 13:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124728">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d662fdebd8.mp4?token=TFqPtGXaOjgg1RfV0JAeDUyKqtrNGSbhDYKhnoUlNtKo246SOluAX3PiJpU79LIuYlAYqFrYxzEfAO50Sjg08B0zcu8fTNyLnp5WlDCy_9vG8B--4Now8w2pBL8zzoE9t6vPcpKJHhvbS6ABpFJU1SrJHWvjSWVksmcbZKl-tTtvD-oHQnnTtYDHjClpz8MbFyWJscMIAtR06PjxrSYiP-zyvaYS18w4OSWyZ7jBC6PC-LtM0e8QCP92tJnjZOwOWbnV2iFc54-uxCuCWWhOSeg_GscPLP6vA-B_dHo0EiT2vqU7SE0R68vyWrA5dBIsAxjcMtjMe--yNaliS5pWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d662fdebd8.mp4?token=TFqPtGXaOjgg1RfV0JAeDUyKqtrNGSbhDYKhnoUlNtKo246SOluAX3PiJpU79LIuYlAYqFrYxzEfAO50Sjg08B0zcu8fTNyLnp5WlDCy_9vG8B--4Now8w2pBL8zzoE9t6vPcpKJHhvbS6ABpFJU1SrJHWvjSWVksmcbZKl-tTtvD-oHQnnTtYDHjClpz8MbFyWJscMIAtR06PjxrSYiP-zyvaYS18w4OSWyZ7jBC6PC-LtM0e8QCP92tJnjZOwOWbnV2iFc54-uxCuCWWhOSeg_GscPLP6vA-B_dHo0EiT2vqU7SE0R68vyWrA5dBIsAxjcMtjMe--yNaliS5pWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شما، کفتارانی که با زن ایرانی اینگونه رفتار کردید و ادعای دینداری و احترام به زن دارید.
🤔
عرزشی های حرام زاده مدعی عدالت علی هم هستند. روز مجازات همه شما نزدیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/124728" target="_blank">📅 13:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124727">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزارت خارجه کویت: یک نفر در حمله دیشب کشته شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124727" target="_blank">📅 12:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124726">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/814d4b04d0.mp4?token=Zib7CrEDLlQmU_G1tJPK0o9o2PvGvHcWRwVCdz_pZF-CRbWP7-czPaLJ_IcufUJbGJFuzuJ97E7LyBXuY4beRfYqRF9T_2c7cVLkiIOSDsH38NelbY0Kg1wh8coxXeelEwwKQP1a5fLU-hYVmi26K-Svwt1dEDmD7LoNG2dASUGAVNBPBB9Ts490UFNzNIGD7dtso-cR4vgIedeMp1t6KBIkwlueKQ7c9sDN0b6aWv9mqNFyq7QeOkHWETgmIlX2v8YsWjPt8cRnVDfclbmez1zzA_BpSzHxWt9jN-SjPbSQYa4M2VLoezn8g0U2DUY19JYBabk68gEwMIqU981Vfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/814d4b04d0.mp4?token=Zib7CrEDLlQmU_G1tJPK0o9o2PvGvHcWRwVCdz_pZF-CRbWP7-czPaLJ_IcufUJbGJFuzuJ97E7LyBXuY4beRfYqRF9T_2c7cVLkiIOSDsH38NelbY0Kg1wh8coxXeelEwwKQP1a5fLU-hYVmi26K-Svwt1dEDmD7LoNG2dASUGAVNBPBB9Ts490UFNzNIGD7dtso-cR4vgIedeMp1t6KBIkwlueKQ7c9sDN0b6aWv9mqNFyq7QeOkHWETgmIlX2v8YsWjPt8cRnVDfclbmez1zzA_BpSzHxWt9jN-SjPbSQYa4M2VLoezn8g0U2DUY19JYBabk68gEwMIqU981Vfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام قالیباف به ترامپ
از زبان آیت الله ک.ص زمین خوار اعظم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124726" target="_blank">📅 12:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124725">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ارتش اسرائیل: هشدار تخلیه فوری برای ساکنان شهر خریبه در شهرستان صیدا، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124725" target="_blank">📅 12:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124724">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ادعای ای‌بی‌سی به نقل از مقامات آمریکایی: ترامپ، از تهران می‌خواهد که امتیازات مشخص هسته‌ای را به صورت مکتوب به عنوان بخشی از یک توافق مقدماتی ارائه دهد
تا بتوان بر بن‌بست طولانی میان آمریکا و ایران غلبه کرد.
🔴
ایران در حال بررسی شرایط به‌روز شده است و مذاکره‌کنندگانش نشان نداده‌اند که آیا تهران این شرایط را می‌پذیرد یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124724" target="_blank">📅 12:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124723">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8daea91c.mp4?token=s07q6zcki0F-NrfAIqG22rJ29El0nEQg3Pg6uEpcakSAXYevI6I9E3O6lV3J9QT5oXHhYpjEg4_aP3uPv0fzzME46CDneq7cx--MD3oCEDJvXJXr-weI3by7o70D05C5HMZe6Q0WWjFZlZgPwoNtc45YbgCHMVsU_VSh2dDdATYHXJYPDMeVTeR8-VSya3Hbxvw8jVm918KfqOWPj5yDc-_0hiyiA0Mpe_T3bXuykZnV0YVvfIpDcm4Z9zsDnZEKzci0qk5pb2BGBl4NIv8otfmNKb8OfDiAuTAVPYEF7pU9VBGXZm8_JG7rOGL6TKllcAFgCGU2Q7E3uo87zpY06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8daea91c.mp4?token=s07q6zcki0F-NrfAIqG22rJ29El0nEQg3Pg6uEpcakSAXYevI6I9E3O6lV3J9QT5oXHhYpjEg4_aP3uPv0fzzME46CDneq7cx--MD3oCEDJvXJXr-weI3by7o70D05C5HMZe6Q0WWjFZlZgPwoNtc45YbgCHMVsU_VSh2dDdATYHXJYPDMeVTeR8-VSya3Hbxvw8jVm918KfqOWPj5yDc-_0hiyiA0Mpe_T3bXuykZnV0YVvfIpDcm4Z9zsDnZEKzci0qk5pb2BGBl4NIv8otfmNKb8OfDiAuTAVPYEF7pU9VBGXZm8_JG7rOGL6TKllcAFgCGU2Q7E3uo87zpY06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب الله همچنان داره موشک و پهپاد ول میده سمت اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124723" target="_blank">📅 12:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124722">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQzeZvzGNxO3k2mmkBVoNVw6qg_Vz8NXHDkY9cEPik0G663Vr2e67OUv79H0yXeCxheepMO6MJAf7rzG_peRXly8yGAvj9SkxASBFbDrdkSuS9Ai-vSHV60GwYNEfTsr56PPFGoMQCunrZ0EnvSqyRCs7MksERT8A0hCmozz4yF4M5kCsCq8A1LD_5csOsWsRIliImZCl-YSbdS9rizQ_eqDFKBXJFlaFvM9JP_hUHsmiFWFG0yOuqSBjswWUhQQDk9J-TWyidaZEgxg-l9MZ5TwB528yuXnMl-b4bUTx-BzoyBTfSOscpLh-RPn6Dd2HfdA8lHXLIsy1STfJNSI3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از صبح امروز چند خودروی نیروهای حزب‌الله در جنوب لبنان هدف قرار گرفته است و طی آن چندین نفر کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124722" target="_blank">📅 12:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124721">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d6b2780d0.mp4?token=cgnnqAn_BuZqVNq5PbHi3CbMqsGcus8C9cJECWzpLIH2dw87dvbe4xwgv-IMAeiQG2ldjOW9xDytl-I5HwCXbwTNugr0PBvIC0DqGyyHhpFapaS9YGP9h789qkpQ9bmHWcTIY4YrxiHy-1cggAD56Hkj97w-6aIavWx2371PFyfg4RHamYUmN6-ypeNvuys0qSc6VkTulKWqxU513q-WZfe_3l7JPNglEa_6A7ZeOo0zqrTFfXVL2CLF4e8avJlCUcJ8VDm9yTqANLDo5j4g9B3D5PhgV_ih1VUH4oL8vWxfZQXqxrOiCZyXdDtTxEphw-3PYb4CiGJKifF5Dkyv0n6bcMbtmc_WgAq-ZeZ64e1HnHZbposyeT_8llq2K3uXC4FMIDADAuNnzzNMDEVfMW79POPLVYFvWQ5K8SOYgeaBaKSvq7BsWaNZhZ3roIzmIkJZDMBsoV-xPaWuSBs2NlRYT6wmryOl0uOSAQ7DtjmpaGxgmPq676lvqV4kVKM-o_nw1cCwpNKq-D3ETYJWECdGpvZaAZEWTms6ifQshXlLOVwKiOsR24u6RxZvTEMafXVy_i2oLQoH7brlvKgA5fTgNUyoKTn1tvP7KQR0apS2NDjlmYvDvjI7acmqjRlPbv7dLT-mPI9RA3zjHyfN3I6E3F1bd3IxY9u1qsZFEto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d6b2780d0.mp4?token=cgnnqAn_BuZqVNq5PbHi3CbMqsGcus8C9cJECWzpLIH2dw87dvbe4xwgv-IMAeiQG2ldjOW9xDytl-I5HwCXbwTNugr0PBvIC0DqGyyHhpFapaS9YGP9h789qkpQ9bmHWcTIY4YrxiHy-1cggAD56Hkj97w-6aIavWx2371PFyfg4RHamYUmN6-ypeNvuys0qSc6VkTulKWqxU513q-WZfe_3l7JPNglEa_6A7ZeOo0zqrTFfXVL2CLF4e8avJlCUcJ8VDm9yTqANLDo5j4g9B3D5PhgV_ih1VUH4oL8vWxfZQXqxrOiCZyXdDtTxEphw-3PYb4CiGJKifF5Dkyv0n6bcMbtmc_WgAq-ZeZ64e1HnHZbposyeT_8llq2K3uXC4FMIDADAuNnzzNMDEVfMW79POPLVYFvWQ5K8SOYgeaBaKSvq7BsWaNZhZ3roIzmIkJZDMBsoV-xPaWuSBs2NlRYT6wmryOl0uOSAQ7DtjmpaGxgmPq676lvqV4kVKM-o_nw1cCwpNKq-D3ETYJWECdGpvZaAZEWTms6ifQshXlLOVwKiOsR24u6RxZvTEMafXVy_i2oLQoH7brlvKgA5fTgNUyoKTn1tvP7KQR0apS2NDjlmYvDvjI7acmqjRlPbv7dLT-mPI9RA3zjHyfN3I6E3F1bd3IxY9u1qsZFEto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رفتار عجیب زائر ایرانی در عربستان
🔴
میدونستین بابت این سنگ ها پول میدن؟ پول میدن سنگ میخرن که برن به شیطان سنگ بزنن!
🤔
عربستان خوب احمق هایی گیر آورده برای کسب درآمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124721" target="_blank">📅 12:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124720">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
یک کارشناس شبکه: اختلالات پس از بازگشایی مجدد اینترنت، ناشی از بازسازی مسیرهای ارتباطی است
🔴
به‌روزرسانی روش‌ها و تکنیک‌های جدید فیلترینگ هم ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124720" target="_blank">📅 12:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124719">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزارت خارجه کویت: یک نفر در حمله دیشب کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124719" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124718">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مقامات آمریکایی و یک منبع مطلع دیگر به شبکه آمریکایی ای‌بی‌سی نیوز گفته‌اند که دونالد ترامپ، رئیس‌جمهور آمریکا، از تهران می‌خواهد به صورت مکتوب، امتیازات هسته‌ای مشخصی را به‌ عنوان بخشی از یک توافق اولیه با آمریکا ارائه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124718" target="_blank">📅 12:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124717">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exHDMEVILBDaewcFwGZ1Dkdxzp2wUvqilCQdgOyedN3CgjEVYfJOD46zma-wYH1wcKxVpzU7zGQRS9Z-kfiYVQSU_nc7zLbphpqTDBXzJ70xQ65OojURVvtWUEKFvPIijj3SJuXfIZ86Fe44u9i2CjBq_9JGbttMXRUWyx6HNd53KwNgGZIVATx5YtYPv0zOIn7zY8s5HrHC7pFVoc7fCA9MJGjP6xssc1QaSv-TbfrmzudIjbO22PtmcVah_WxmXNK37ilgu7tzMouWKHHu66yjd-U_K60Bgz6Fw8ADE3KdldjOiyojXQvYHL-VpNDV6kmTdEH3O4cc8f9OqENvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: پاسخ هر شلیک و تجاوزی رگباری از موشک و پهپاد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124717" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124716">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزارت خارجه  :  اقدام آمریکا نقض آتش بس است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124716" target="_blank">📅 12:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124715">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfgbYSDNxs2HOdMQYMCeimV5Kj1MAT3sit7kF0QEE2DDHq9ngGdl-LwrB5IBnVrNJz6bjqyusjN5_QsiPij7aRGGyekZktiCizpm0_jUIfoFkLRwW7s0Ken9EpEASW2-fzXqosSK9io98gc7lEdutrF0mk2uzkkUZUMeT1mQ9ySgWdy1JMsEgPYFBuN0RiIAEhsqjO7U20uXyOAqP5fqTZHJtt3lufwIKKS8nY6X_rWLG7SG15EXMR9ThQZymyc0t6KGRJUkoDYc_VX2UcX1mb1sDI1XYZKxW97XzCIxIK-Lme09j06N2q6ONUBviDlYrYpiuWCWmwY0HFbdG5wYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال‌تایمز به نقل از یکی از بزرگ‌ترین مالکان کشتی جهان: پرداخت ۲۰۰ هزار دلار عوارض برای هر عبور از هرمز بهتر از انسداد یا اختلال در آن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124715" target="_blank">📅 11:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124714">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
دانشگاه آزاد اسلامی: تاریخ امتحانات ۱۸ و ۱۹ تیرماه دانشگاه آزاد اسلامی به روزهای ۲۲ و ۲۳ تیرماه تغییر کرد
🔴
این تصمیم به منظور جلوگیری از تداخل امتحانات پایان ترم دانشجویان مقطع کارشناسی با آزمون کارشناسی ارشد 1405 اتخاذ شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124714" target="_blank">📅 11:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124713">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=q5QT5cuKJbU_63IU7bf3ZldR9_VYewRiDhzVaB-yG27dIpKc51ayCSHAUVul8bWeaHytLAYIKwJcbYMiDGEdGCP4h4X5SyFJ6kbO6HOr49zZvQuUda2lnCbommsoq_tOS1BCMRkNSU2xhNQCfXH6Ef9P7EQRcdXW2xJft7rmV8RP6Yy8AUkVfq7tq-H3OS_xBXEQRfAn1JX1K3esJ7QHFWIz-wZOEDhMirb-ep7zFzQD8xNM64Z09gumP0n7t4tSvutxyBltmjesuaYjJs_R7RxJ-deaNfMsBgucDX5eAB9rglbXRab0tUh8C89eBCIThuOPgJqII_KP_XUyirKRNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=q5QT5cuKJbU_63IU7bf3ZldR9_VYewRiDhzVaB-yG27dIpKc51ayCSHAUVul8bWeaHytLAYIKwJcbYMiDGEdGCP4h4X5SyFJ6kbO6HOr49zZvQuUda2lnCbommsoq_tOS1BCMRkNSU2xhNQCfXH6Ef9P7EQRcdXW2xJft7rmV8RP6Yy8AUkVfq7tq-H3OS_xBXEQRfAn1JX1K3esJ7QHFWIz-wZOEDhMirb-ep7zFzQD8xNM64Z09gumP0n7t4tSvutxyBltmjesuaYjJs_R7RxJ-deaNfMsBgucDX5eAB9rglbXRab0tUh8C89eBCIThuOPgJqII_KP_XUyirKRNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش‌چشم، تحلیلگر صداوسیما: احتمالا نگرفتن انتقام شهدای اخیر، به‌خاطر حفظ جان قالیباف بود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124713" target="_blank">📅 11:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124712">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
براساس تازه‌ترین داده‌های هواشناسی، از بعدازظهر امروز تا اواخر روز جمعه پایتخت و شهرهای اطراف آن شاهد وزش بادهای شدید و خیزش گردوخاک خواهند بود.
🔴
در روز پنجشنبه با افزایش ناپایداری جوی، در بعضی ساعات با تشدید وزش باد و بارش پراکندهٔ باران همراه خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124712" target="_blank">📅 11:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124711">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c45c67b3.mp4?token=JLKauvq1RQap6UXMGX158Bz1FpZ0UKlWfQgop5lg6c2y2kdgxsk6IQuzHgr6ysMROlV5bLITEsUc7fJwxJWFWlu74zbnpqNDzCCX1dDtHiQV_0cK3FW3E6UhGAjlABZBh0XR0_nYGRMcuxwc-c2wJl2gDakYw9OnwxCVieI2bBFPrABig8g8lMWeSt_KCltnE5lcMd4-8Cl6L0iBNp6TSYOhQGiDn82H14DbRxUkBeZNoPtAHi4-Za1cWWtFhyiHuZ5vUHSiaXjYJdmItPTyyjc2Ft0JMMIbXXYmbyfhhjIVtW7prb_q41oO8u__WPzTbViEHNDDPrswA7fnd1mj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c45c67b3.mp4?token=JLKauvq1RQap6UXMGX158Bz1FpZ0UKlWfQgop5lg6c2y2kdgxsk6IQuzHgr6ysMROlV5bLITEsUc7fJwxJWFWlu74zbnpqNDzCCX1dDtHiQV_0cK3FW3E6UhGAjlABZBh0XR0_nYGRMcuxwc-c2wJl2gDakYw9OnwxCVieI2bBFPrABig8g8lMWeSt_KCltnE5lcMd4-8Cl6L0iBNp6TSYOhQGiDn82H14DbRxUkBeZNoPtAHi4-Za1cWWtFhyiHuZ5vUHSiaXjYJdmItPTyyjc2Ft0JMMIbXXYmbyfhhjIVtW7prb_q41oO8u__WPzTbViEHNDDPrswA7fnd1mj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های لبنان گزارش دادند که حمله هوایی اسرائیل یک خودرو را در بزرگراه ساحلی در جنوب بیروت هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124711" target="_blank">📅 11:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124710">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نیروی دفاع بحرین:
فرماندهی کل نیروی دفاع بحرین اعلام کرد که ایران با حملات موشکی و پهپادی شوم خود که به زیرساخت‌های غیرنظامی در پادشاهی بحرین هدف قرار گرفته‌اند، به تهاجم سیستماتیک خود ادامه می‌دهد.
فرماندهی کل تأکید می‌کند که با عزمی راسخ و آمادگی رزمی بالا، سیستم‌های پدافند هوایی نیروی دفاع بحرین موفق به رهگیری و نابودی سه موشک و چندین پهپاد شده‌اند.
فرماندهی کل تأیید می‌کند که تمام سلاح‌ها و یگان‌های آن در بالاترین سطح آمادگی و آماده‌باش دفاعی برای محافظت از پادشاهی قرار دارند.
فرماندهی کل از همه می‌خواهد که احتیاط کنند و از نزدیک شدن یا لمس هرگونه اشیای ناشناس یا مشکوکی که از بقایای تهاجم وحشیانه ایران ناشی شده‌اند، خودداری کرده و بلافاصله گزارش دهند.
فرماندهی کل تأیید می‌کند که پرسنل یگان مهندسی پادشاهی کاملاً آماده‌اند تا این اشیاء را به صورت ایمن و فنی مدیریت کنند و ایمنی عمومی تمام شهروندان و ساکنان را تضمین نمایند.
فرماندهی کل تأکید می‌کند که استفاده عمدی از موشک‌ها و پهپادها برای هدف قرار دادن زیرساخت‌های غیرنظامی و اموال شخصی، نقض فاحش قوانین بشردوستانه بین‌المللی است.
فرماندهی کل نیروی دفاع بحرین افتخار و سربلندی خود را در برابر آمادگی رزمی پیشرفته و هوشیاری بالای مردان شجاع خود که وظیفه ملی مقدس خود را در دفاع از میهن انجام می‌دهند، تأیید می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124710" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124709">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/124709" target="_blank">📅 11:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124708">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FS4kvzCqtXNyKUUkTes5RKi58z9IMaRhXG-aBrg3jpSihBuI914lLCEYPhhWAwyvK7RLzNHleq3wvbU_tY-xyuvV7JocmDJWqqt3uw8BTo4ZKigMe0sG3mKR5rBOYPeXw4CAmWlXRdEee5nfXBdC8FvCiRy1I6M8YijXldQuTsKaHwsPHaCz6cGJBz8aRqBiDyRAeV58-5UrA-HHOX1ZLs03LUVvZOK6KtSotHwnDBXSJ9Z0B3qHiUDCvHORs8-PVFT5NBa6J9ewfD4zdKSFvQfpVh2VYsYZGDGbLViYUVmA5jQwtFOxAVl1wrmvxbv7dahIAeOw8kY-jAEBc9A2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/124708" target="_blank">📅 11:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124706">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/038102f967.mp4?token=DSGkzMZ7ppFm4crtCy9OJDadLkTDejsZJmYa4dT5YJ1e73So0Er6DBT4DuCHpw9tUEuL9D-hZbsfwvcD_5CW520tN1q4rCoJERN8fXc2PP5AQQNfNIjWGc3lZ2jonw1AHvbA-e58EqAMe6nZ5mnelvSox1xLnAILqAmGLUnDABBnBz0lPeeYEVPym4qRqAki8kUquRuKfr7EtOnWsYsikF0kZ5JtFsJJ2qB-ANj6JDGt10kyovQ5x0lSNH5Bp4eBIHH0yNLO5n_9z5u2bN9KZb6CHG2iyfkMYagnrPE-2MtSnF1eak4_WdNX5PR70wfGWcgsJrSNLgVVWeGQeBew_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/038102f967.mp4?token=DSGkzMZ7ppFm4crtCy9OJDadLkTDejsZJmYa4dT5YJ1e73So0Er6DBT4DuCHpw9tUEuL9D-hZbsfwvcD_5CW520tN1q4rCoJERN8fXc2PP5AQQNfNIjWGc3lZ2jonw1AHvbA-e58EqAMe6nZ5mnelvSox1xLnAILqAmGLUnDABBnBz0lPeeYEVPym4qRqAki8kUquRuKfr7EtOnWsYsikF0kZ5JtFsJJ2qB-ANj6JDGt10kyovQ5x0lSNH5Bp4eBIHH0yNLO5n_9z5u2bN9KZb6CHG2iyfkMYagnrPE-2MtSnF1eak4_WdNX5PR70wfGWcgsJrSNLgVVWeGQeBew_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای جاسوسی که با لاشه پرندگان مرده ساخته شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124706" target="_blank">📅 11:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124704">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedd715615.mp4?token=nBv7qBoUNdokHv2DbJueR3Kft2iIYWBHjvAeZEIfaBuY_6SdL_y_6kRfpjh3GZ4kLYFriQYM3RwN3yXdNlW40lO13fj9GI_XQiDwRsEu4HTOqiIGPiNQWgL_wOXOcWfSKECO3AFZ-4V614Ptcv2fsyC_SFXUJ0pcASGW0C1sol0xgYSXOmztNL0JhppHfF_8LacHG7c30bSFaZowscoap18-yhN-DYgEfaDq0f_H2FDPbM7PmN6nSp5VHnq7JsgV93blN8dknehrYODITAlzmH5u1WJbBis_EmvirObA2KPyMr0cPQyPS_MtQ4G3pSyo6vrfrlMstIPg_ArCM9iFHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedd715615.mp4?token=nBv7qBoUNdokHv2DbJueR3Kft2iIYWBHjvAeZEIfaBuY_6SdL_y_6kRfpjh3GZ4kLYFriQYM3RwN3yXdNlW40lO13fj9GI_XQiDwRsEu4HTOqiIGPiNQWgL_wOXOcWfSKECO3AFZ-4V614Ptcv2fsyC_SFXUJ0pcASGW0C1sol0xgYSXOmztNL0JhppHfF_8LacHG7c30bSFaZowscoap18-yhN-DYgEfaDq0f_H2FDPbM7PmN6nSp5VHnq7JsgV93blN8dknehrYODITAlzmH5u1WJbBis_EmvirObA2KPyMr0cPQyPS_MtQ4G3pSyo6vrfrlMstIPg_ArCM9iFHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاربران رسانه‌های اجتماعی لبنان تصاویری از یک انفجار بزرگ را منتشر کردند که ارتش اسرائیل در منطقه «عریض دبین» در جنوب لبنان انجام داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124704" target="_blank">📅 11:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124702">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uprviZhGp4W9xqvtXVLGJjdX2zfjJAO1akzgJBA-89KLSMTsUBXxnpa73ywhuHDMAzoXq5Yv5y97VengC-2R0CoF2HTp-XtgJWeCn2Ct6QP3WQ_f0QccbF6MQt0Gr8KabI-Z_h_RHiB_S48xOgZwX_iSdywD1NlfzmnF70KYeRkIFoYiAFZouWM8MpzlK6TaiOhoPe831XCVIICKJTJigPOfryVSGqShs9DzarjKKniZOgw5vYqci4l2WiBp4ppcjf2Jr5f1SkDJmZEEp1H8FxwVHxDHPJAcWSl9F_Z_d2lMpP1BVmB7IurCesE8pNg8uCJlQKESOkFjRqRiWGGeFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vRcu43h9jbQdHeL7m1liWh31AOoS3cToMI8iURfyJXXFdUdnXI2ZOPICSo4h8P1XaRGhOR8hzLcjOb4ajNrwiMGgVAFBbxtwV-UL17Gq_Qhm1mu14sSx9AKhpcYhBEDWO0ROjQih14qrQdQX6h9Fhl17ac98BnhR9KHW53awSHwg9aVxS_ET4yKedb5P3im6972ISkuGWfWp4bnZgb9urpGzluwvlC2akeUc1E0xleJgn2DdjPOW_EJLeZebLuPXcTu9sm3Kwg60Ld0kjBTqkr_il1DKfUcV8AQDu1NyOH6EGrcRP0sv8W3QJWvIvbqZVyIp7XJzhwvyPSOvIMp82g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آسیب‌های وارد شده به فرودگاه بین‌المللی کویت پس از هدف قرار گرفتن آن توسط پهپادها و موشک‌های ایرانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124702" target="_blank">📅 11:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124701">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
عراقچی: روابط تهران-باکو در مسیر توسعه و پیشرفت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124701" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124700">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نیکزاد، نایب رئیس مجلس: در مذاکرات پاکستان، قالیباف به آمریکایی‌ها گفت با عدم اطمینان و عدم اعتماد پای مذاکره آمدیم/ هیئت آمریکایی دیگر بازنگشت و همین باعث می‌شود آن‌ها را بدعهد بدانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124700" target="_blank">📅 11:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124699">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزارت خارجه چین: نگران وضعیت کنونی خاورمیانه هستیم و جنگ مجدد در ایران به نفع هیچ طرفی نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124699" target="_blank">📅 10:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124698">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
اسرائیل دستور تخلیه سه شهر در منطقه صیدا در مرکز لبنان را صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124698" target="_blank">📅 10:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124697">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
هوای مشهد برای چهارمین روز پیاپی در شرایط ناسالم و غبارآلود برای تنفس شهروندان قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124697" target="_blank">📅 10:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نایب رئیس مجلس: موشک‌هایی که به بیت اصابت کرد تنها چند کروز بود نه سنگرشکن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124696" target="_blank">📅 10:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
روزنامه اطلاعات: ۸۵ درصد آب مصرفی کشور به بخش کشاورزی اختصاص دارد، آن هم با قیمت بسیار پایین/ معلوم است با این قیمت آب را هدر می دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124695" target="_blank">📅 10:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرگزاری فرانسه: کابینه ژاپن ۱۹ میلیارد دلار بودجه اضافی برای محافظت از خانوارها در برابر تورم مرتبط با جنگ آمریکا و اسرائیل علیه ایران تصویب کرد.
🔴
دفتر نخست وزیر سنائه تاکایچی گفت که بودجه تکمیلی به طور رسمی در جلسه صبح چهارشنبه تصمیم گیری شد.
🔴
سخنگوی مینورو کیهارا گفت که برای به حداقل رساندن خطر در بحبوحه ابهامات مداوم خاورمیانه تدوین شده است.
🔴
تاکایچی ماه گذشته گفت که این بودجه افزایش هزینه بنزین، برق و گاز را کاهش می دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124694" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124693">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
تبریک ترامپ به «آبلاردو دِ لا اسپریِلا» به دلیل پیروزی در دور اول انتخابات ریاست جمهوری کلمبیا: آبلاردو خستگی ناپذیر برای کشور و مردم بزرگ خود می‌جنگد و عاشق آنهاست، درست مثل من برای ایالات متحده آمریکا
🔴
نتایج این انتخابات برای آینده کلمبیا و رابطه آن با امریکا بسیار مهم است
🔴
حمایت کامل و بی‌قیدوشرط خود را از آبلاردو اعلام می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124693" target="_blank">📅 10:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124692">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
خبرنگار الجزیره: بمباران اسرائیل با بمب های آتش زا به شهرک الحنیه در منطقه صور در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124692" target="_blank">📅 10:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124691">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOXkQvf0NbTTr9OGYaV08F7lUITrqNRBKpUyaab2I7LA2lv32-89c6ii9NPgA9orwuN8tqx15c_nW5Ulm3eDt0_g6jwarty6Y_9B6QckLAkMJsPBjegCniic67s21dURk83amwX8ZFvoXtmnLK2Nn0Q4_80QdRSV_1BceMkp7TgFT5Dw1EoePQIZyLAwD-HAGpZRb85sahEPVMfDYOoul2dykZ5BDVYlbI1nx0C6EN1IFbDM0_hRY3auct2mzAAO7Qq1zrCZgBOFXG9cgrF4it-UGCOMdAMpkLIklhN1pU7Xdoj-CJLbLl4qMyfISfpcUtPdxcZpOfJLoivYAl9UyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از قرار گرفتن نام چهار صرافی رمزارزی ایرانی در فهرست تحریم‌های وزارت خزانه‌داری آمریکا، نوبیتکس، والکس و بیت‌پین در بیانیه‌هایی جداگانه اعلام کردند دارایی کاربران در امنیت است و فعالیت پلتفرم‌ها بدون اختلال ادامه دارد.
🔴
این صرافی‌ها تأکید کرده‌اند تحریم اخیر به معنای توقف خدمات یا تهدید مستقیم دارایی کاربران نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124691" target="_blank">📅 10:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124690">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7l_YOgsuvgjLCs3b25FQefmmY6GgsXLuqV8Xdiu6EcPXX14bdXiR4s0Y4K4i1OU8vTuJFeDaiky9w-RhluTsqll_VWR7tp8ZAjuqPi67ovNuWWHX2DYydlbssIUva5B-IMj-KXNDzdDn1YvFP-A2h6_cjxOQfEHw2NbkQlhxG0e1KB3cIFADvCRpOhvLrCcgvub_ohjwFuPSxtaWKMA050Xij9LMCmnHh9H6E8bpa45x6p1KsEi4dJqhBgZVybvV6iwR99HX2-jWVwm7anPRNKDBNZa62fcVpHWCP991AIEfBBx-mqzzYnqYRTx7rdAyTVTg3R1ER6dmYNGvMRr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: افزایش ۳۰درصدی قیمت مواد اولیه داخلی، قیمت خودرو، لوازم خانگی و بسته‌بندی محصولات، در موج جدید گرانی در راه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/124690" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پرداخت افزایش حقوق بازنشستگان در سال ۱۴۰۵  به تأخیر می افتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/124689" target="_blank">📅 10:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP1Qh-yQZ4s5iPamI-_LCkVIkmbIWxT3iruhDaL8eFLQk61_PruRf7KtwUcc9kU4yz_jktnD6SSLF2I44c1FhPL_lDhT9DxUV4Bjo8lyc5UvQ71viYKOmc6IjKfO8Ni0OEk5aCAAm-w2LrROxoozLt3QRBHwFpBgBVKoe-hUQ2ogN7SABtNzFbCtif62rLZUFWzby4YxrQPxzRczy1XCMtdo0FcGB-H_8Cm_6FZohfFvcGgUw_uxYi3zQkvbLBgeHm-k6FB165UHf7aL3jIybHOlqFC-YbpJUUpJ8NO-EH-qEiEdwURmesY4s7Z1iw6-9QO43uHiBKEA-RZ68oZtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک ماه پس از آن‌که دونالد ترامپ طرحی را برای اسکورت کشتی‌های تجاری از طریق تنگه هرمز اعلام کرد و سپس از آن صرف‌نظر کرد، ارتش آمریکا در تلاش است با روش‌هایی کم‌سروصداتر از شناورها در این آبراه حیاتی محافظت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/124688" target="_blank">📅 10:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
جنگنده‌های سوخو-۲۴ ایران مواضعی در نزدیکی اربیل را هدف قرار دادند
🔴
گزارش‌ها حاکی است نیروی هوایی ارتش ایران شامگاه گذشته مواضع گروه‌های مسلح کُرد مخالف جمهوری اسلامی را در نزدیکی اربیل، مرکز اقلیم کردستان عراق، هدف حملات هوایی قرار داده است.
🔴
بر اساس این گزارش، بمب‌افکن‌های سوخو-۲۴  به پرواز درآمده و اهدافی را در چند کیلومتری اربیل مورد حمله قرار داده‌اند.
🔴
این حملات تنها یک روز پس از برگزاری رزمایش‌های گسترده و تمرینات آتش زنده نیروی هوایی در مناطق مرزی با عراق انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124687" target="_blank">📅 10:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نیکزاد ، نایب رئیس مجلس: وزارت خارجه اذن تشکیل کارگروه تنگه هرمز را از رهبری گرفته بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124686" target="_blank">📅 10:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
فرمانداری دزفول: درپی امحای مهمات از ساعت ۱۰ تا ۱۲، احتمال شنیدن صدای انفجار وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/124685" target="_blank">📅 09:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXIxHkuXVQXrlfrfSI7JuHijWmIWLh6Xtthw8viWKE3YcMBDi_8XfYStxXBM8ICXLthCvEyAt5Yf1d_B9JH-_VCigdPSccRFofR69uFpf-LXw0_C8TbfUX0spi7UziHeA3bT6YSywoiTyYSjMVTRxD8IRgzwxmiypD9Fa2MxpLD69GhcBden3zTYJuvTfmRcrSD2S7xiTgb89cU0WXOreGusEgA3JvhofBb-0JXlqmdLkOi6rPQMapVevox8sxNmGRWfBKsBFXsrMbI7grPlZ27y3tN7KnjzDWFWkh8jupi-Gp_hMNoQWZDyoIOl1WD3ufYwCvgUqOKrEYES3rS6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس تهران در دقایق ابتدایی آخرین روز کاری بازار در هفته جاری ۱۷ هزار واحد رشد کرد و به تراز ۴ میلیون و ۳۶۱ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/124684" target="_blank">📅 09:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4f12ee39.mp4?token=BKWkB4t6L-JPPbuNvp-yTO7AYDsm5lxoau_1ppnrZ1sk25mlgoppOwaq0DnimTjjCIVrYplbwCsCy5deN1ZVMPuwlaf71ArapRgF84MjhN4bZjz3N77UGJHLZlzINIiHB6F28UTdb5yGGa9gQ3KWcZ73ems98aZyeqgSreqfu4_FC19XXQ0swuv8fWQuuOFduKsRs-SMUCWAWqlyRRuFZCoHyzTnlOU0K3RErWuXd6M1Q9sQlGEhf0oiYjVfGRSTsdgam2b1_9k2TgoZjc2DYuJDYhZCUfN15gWz8Pj1a38V2jGrM8-CSrv3REueoVv8HybneV2bxO8r4Gj3668s2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4f12ee39.mp4?token=BKWkB4t6L-JPPbuNvp-yTO7AYDsm5lxoau_1ppnrZ1sk25mlgoppOwaq0DnimTjjCIVrYplbwCsCy5deN1ZVMPuwlaf71ArapRgF84MjhN4bZjz3N77UGJHLZlzINIiHB6F28UTdb5yGGa9gQ3KWcZ73ems98aZyeqgSreqfu4_FC19XXQ0swuv8fWQuuOFduKsRs-SMUCWAWqlyRRuFZCoHyzTnlOU0K3RErWuXd6M1Q9sQlGEhf0oiYjVfGRSTsdgam2b1_9k2TgoZjc2DYuJDYhZCUfN15gWz8Pj1a38V2jGrM8-CSrv3REueoVv8HybneV2bxO8r4Gj3668s2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساعتی قبل، حمله پهپادهای اوکراین به سن پترزبورگ
✅
@AloNews
خبرر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/124683" target="_blank">📅 09:48 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
