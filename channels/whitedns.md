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
<img src="https://cdn4.telesco.pe/file/X8_YRHetvm-zgeeNh8mVx4Xa8YZufAvKE2ENa9TDZFw67-8AP4L08vaHAfMjplg8x_ktmStQgUyC_oxOFPFMvskOMXY_cI5oFw5-lm7HLlImmRtCrjTRs6C_K1ZyLRT_JgBmUW-FBVpGiOOUSxgZg84hEz9EUdmJmb5-v47aTLwk4iEHsDwQkE3q_ebAWXUQU0zaVTffH8ugcclaJuikrp9r3nt_5IUtamd05vaRtLQMn7oemn67_UWrTm9wlM1DoBbMI-xkuRqEG8kpV5BSmHDJS32ekhVJtGf_rlSunnkAlpzAqXeR56JHkpBxlrJN4h-uUjyI-BswAJNYg6CwwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 02:50:38</div>
<hr>

<div class="tg-post" id="msg-1954">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سرور whitedns که از طریق بات درخواست میکنید یک روزه هست اگر لازم دارید
به درد روز مبادا نمیخوره ،درخواست ندید</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/whitedns/1954" target="_blank">📅 13:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1953">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/awl4gECNxpNfoCZcd_5VOtaBwGEHigdeGxRbwmFXooikskX0lV1_v2PZpY3mYcL8lZ6omq5_VjQAY3xkYwE_lNKDvSsO8Qw1FPUsW_lVeNGV6Nzy1rzlp7-eKPFFMlDcTAsY81lgPLWvtNdd_V17rsPg7bPTwF9W3ybHQg6JMF8xqz0O2iEQROwHhjfWBRUDa1rXJ7cRqkhkIq0Br7xdy89Nd4gddtKITrrpl-7o6uUqKEDAzFMgB8VSl5iKj0inDl50mEmHPk0aJryrxF12P679Y0gbqbm0K7VbwDctfU3pCAfb-hdnEtTO1HDQF_loazGfD9lJsrs7cacJmnBn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/whitedns/1953" target="_blank">📅 13:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1952">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-text">🎬
آموزش کامل TheFeed | از صفر تا صد + پیام‌رسان جدید + ظاهر جدید
اگر تازه با TheFeed آشنا شدید یا می‌خواهید با قابلیت‌های جدید آن آشنا شوید، این ویدیو را از دست ندهید.
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
استفاده از کانفیگ‌های پیش‌فرض
✅
آشنایی با ریزالورها و DNS
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با TeleMirror
✅
رفع مشکلات رایج
✅
فعال‌سازی پیام‌رسان TheFeed
دفید یک پلتفرم مبتنی بر DNS است که برای شرایط محدودیت اینترنت طراحی شده و حالا علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را هم فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصبی:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
ضبط و تدوین ویدیو:
@vahid_4444</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/whitedns/1952" target="_blank">📅 11:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1950">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/g18j6xB5r3YkNhjYeFKt79r6RK66UMO8sfQvFW7HsqQYLwzA9Bc5zDatm3uwa7iw1QPLl6GY4IBgYGC1UjZyaHHfRYQiwAfWyYpYU3PjpLe6SONU9zKDBNmFPTUMNVQVDc8YFbpyDdlbLGM2slBkf06hropAZBb686TByYRBd1RNS3UkecxpO_w1FOKYGQ8ZERyIuXXzLSuAWGryvF5tcBytm_yPQz_gcsODbS5r4KgPn3T5wgKUEbrY21BUNR9ITkHK3QIdsHODQS8ITXf6sc645kqybILeyHIfGy_dMTH_1MV6odZWPR9BOnJAWnooTLaiajbixiIs99WNwazCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتیم برای WhiteDNS یه Patreon راه بندازم.
حدود 9 ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱5 هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://www.patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1950" target="_blank">📅 06:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1948">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qJoXsSOEyW1fqVtRAZ8xo34daUDKmXwRRZfUYsEBbSr2zViBST4e6-TKHEFIlChqI3nNJRfMI-IuUVa1s-_BX8PvSmZh1HTgJd7DEYjLNyVEgUfFeBedN4wy_WaWZuuvSF-dMo39tX47tWJui3RartqsTAOi6EZO8dNevKRf7iLPO2EiQwjXyZrIsni3I5rOSeHplQUiqKcbzEU8x3LUxnfEDu9WM6kSyczAc8BPwE6zP1FcNN1f3G8RMKKSEsMe__OGtcAodiZB_nEuQIXOh5ovFR5VOyLRMmtKAGlRy1gs7YNfPDTWHCf2pfuq6JF_ydXPVI13cylHp8xiP8GfaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1948" target="_blank">📅 06:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1947">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4HjDK5F8x8GtgvKrF6Q5abP844FRucvG62eKA27jX1k0nxGtAwOFvLaeI95IXw2RRAuJYiXcIv1SI_yN3ciS0WEncIwz1qnC6MpEbHGxLNB-6aEfcdF3GHHmy2UOsXdRx4tTi2KmtXb81jb7YQnEADzFuJVCwGAky1CtuBNdRv06d5hD1nij4m8pkN-GEYC6L_o6JSeoYX2jhVIE6SMutnAbFrgswq3srqEsgbznVvyPldgVq9Wg19vZtT4bUW1wMrs71eOIg02QcMje3Gph6P6TnR6fj7C-qh90nQLEnwst_ZZLpMzdSbaanvgjQ4vCm1I1v27H4Qbs-cc9ARBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/whitedns/1947" target="_blank">📅 18:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iH7QsyDMWkG6i1IBEDjHR3xlQ6lTqlHb31oKuVvRcSUBb42HaCNouUnZyK2OlPuXF2HT7lK_RyGB27P1v8RvX9U-SbseMX03yIRgS1gfgL9TWfIfjnxQdaygw7KvypHabnDaaguteBCC2R8F5Ex0421E1cxBD57uInpvCXb3e56cTZxhnzyqna0dYCShdTViLh8vIJez0Yz-daH8z_rw1U4pzi08dx9TPEiiJveR5MYmarRdkhOlUuH8XGZevbWQrS8XykbOh2MIjCCpQN-oDKYkKeubu2sLb2Hh2E8l_hKkhXHdQeqaZ45cx827S5DXQvPgagiMRiRpiA9MrralJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
آموزش سادهٔ TLS Split و ECH در WhiteAesther 1.11.0
این دو قابلیت به اتصال
Aether
کمک می‌کنند:
🔹
TLS Split
پیام آغاز اتصال را به قطعات کوچک‌تر تقسیم می‌کند.
🔹
ECH
بخش داخلی همان پیام، از جمله نام سرور، را رمزگذاری می‌کند؛ سرور باید پشتیبانی کند.
✅
برای کاربران معمولی: حالت خودکار
۱. اتصال را قطع کنید.
۲. در
مسیرها / Routes
، انتخاب مسیر را روی
خودکار
بگذارید.
۳. وارد
ترافیک / Traffic ← پیشرفته / Advanced
شوید.
۴.
Split the TLS handshake
را روشن و گزینهٔ
خودکار
زیر آن را انتخاب کنید.
۵. برای ECH نیز
Encrypted Client Hello
را روشن و زیر آن
خودکار
را انتخاب کنید.
۶. به خانه برگردید و وصل شوید. هیچ کادر سفارشی را پر نکنید.
⚠️
هر قابلیت کجا کار می‌کند؟
• تقسیم TLS: روی
MASQUE H2
و تونل بیرونی
WireGuard over MASQUE / WOM
.
• ECH: فعلاً فقط روی
MASQUE H3
.
• این گزینه‌ها تنظیمات داخلی Psiphon یا Tor را تغییر نمی‌دهند.
🛠
تنظیم دستی تقسیم TLS
در
ترافیک ← پیشرفته
، تقسیم TLS را روشن کنید:
•
Records / پیش‌تنظیم رکوردهای TLS:
الگوی آماده؛ عدد لازم ندارد.
•
Compact / پیش‌تنظیم فشرده:
الگوی آمادهٔ دیگری است.
•
Custom / سفارشی:
مقدارها را خودتان وارد می‌کنید.
مقدارهای پیش‌فرض بخش سفارشی:
▫️
اندازهٔ قطعه:
16-32
▫️
تأخیر:
2-10
▫️
تقسیم در محل نام سرور:
روشن
16-32 یعنی اندازه از بازهٔ ۱۶ تا ۳۲ بایت انتخاب شود. 2-10 یعنی تأخیر بین قطعات از بازهٔ ۲ تا ۱۰ میلی‌ثانیه انتخاب شود.
اندازهٔ مجاز:
1 تا 16384
تأخیر مجاز:
0 تا 100
فقط عدد یا بازه را با اعداد انگلیسی وارد کنید. این مقدارها تضمین اتصال نیستند؛ قطعات خیلی کوچک یا تأخیر زیاد می‌توانند اتصال را کند کنند.
برای انتخاب مشخصِ H2 یا WOM، در
مسیرها ← خودم انتخاب می‌کنم
، مسیر شامل Aether را انتخاب کنید؛ سپس در
پیشرفته ← پروتکل
، H2 یا WOM را بگذارید.
🔐
تنظیم ECH
برای بیشتر کاربران،
خودکار
کافی است؛ برنامه تلاش می‌کند تنظیمات لازم را دریافت کند.
سفارشی / Custom
را فقط وقتی انتخاب کنید که یک
ECHConfigList معتبر و سازگار با سرور، با فرمت Base64
از پشتیبانی دریافت کرده‌اید. خود رشته را بدون عنوان ech= یا کوتیشن در کادر بچسبانید.
آدرس IP، نام دامنه و کلید وایرگارد برای این کادر کاربرد ندارند. اگر رشته را ندارید، حالت
خودکار
را انتخاب کنید.
برای انتخاب دستی H3:
مسیرها ← خودم انتخاب می‌کنم ← مسیر شامل Aether ← پیشرفته ← پروتکل ← MASQUE H3
H3 به عبور UDP نیاز دارد؛ ECH به‌تنهایی مسدودبودن UDP را حل نمی‌کند. همچنین روشن‌بودن گزینهٔ ECH، فعال‌شدن موفق آن را تضمین نمی‌کند؛ دریافت خودکار ممکن است ناموفق باشد و تلاش اتصال بدون ECH ادامه پیدا کند.
💾
تنظیمات خودکار ذخیره می‌شوند. پس از تغییر مقدارهای دستی،
قطع و دوباره وصل شوید
. اگر ورودی خطا دارد یا اتصال بعد از تغییر ناموفق شد، تنظیم مربوط را به
خودکار
برگردانید.
@whitedns</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1946" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1943">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.11.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/whitedns/1943" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخهٔ 1.11.0 Whiteaesther mobileمنتشر شد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1943" target="_blank">📅 19:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1942">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RcXITHY5De4M6F1FX4WlF2kQzFjkZKMdnr7EBthIIfztEnN3eCWgBk_PbN108Sq6mir5BqwQ04tIYuJCgIZbX4-QQRvS7ZvTlh3ri9xZLoGSjit5pE9p2BlWx8TZw_-7nIPj4a9cHssIVGhOnFH3AB8wY47jfv1VVqM30mLxTd8bbzqChbufhQodsPqvvML-QATncWMobHtK89BMFHqBTCUFNQYji20AfOOHdOGbuZwxtsbHxqe-ZNpbm8KchHga6HJq064wFgtj5ePzR2ec2jgBRRfG0kxgyOk6KeW9_YcZZyau7EUQQdNEfZ2j2-wTncME95P6ih6M-IJN8_pg1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخهٔ 1.11.0 Whiteaesther mobile منتشر شد
این نسخه روی اتصال‌های ناموفق، انتظار طولانی و گیرکردن VPN تمرکز دارد:
🔹
پروتکل جدید WARP WireGuard over MASQUE
وایرگاردِ خودِ WARP داخل یک تونل MASQUE روی H2/TCP حمل می‌شود. این مسیر، وقتی ارتباط مستقیم وایرگارد با UDP مشکل دارد، یک گزینهٔ دیگر برای اتصال فراهم می‌کند. سرور وایرگارد شخصی لازم نیست و می‌توانید آن را به‌عنوان مسیر Aether در ترکیب Aether + Psiphon هم استفاده کنید. قبل از نمایش «متصل»، عبور داده از هر دو تونل بررسی می‌شود.
برای انتخاب دستی: در «مسیرها»، «خودم انتخاب می‌کنم» را بزنید، Aether یا Aether + Psiphon را انتخاب کنید و در «پیشرفته ← پروتکل»، «وایرگارد روی MASQUE» را بگذارید. حالت خودکار خودش مسیرهای جایگزین را انتخاب می‌کند.
🔹
اتصال خودکار بهتر
حالت خودکار زودتر سراغ مسیرهای جایگزین می‌رود؛ روش‌های مختلف دست‌دهی H2، تکه‌تکه‌کردن TLS، IPv6 در صورت فعال‌بودن و WireGuard over MASQUE را بررسی می‌کند. مسیر موفق برای همان شبکه ذخیره می‌شود تا اتصال بعدی از آن شروع شود. آدرس ذخیره‌شدهٔ WARP هم پیش از انتظار برای دریافت دوباره از API امتحان می‌شود.
🔹
تنظیم دستی کنار حالت خودکار
در «ترافیک ← پیشرفته»:
• «تکه‌تکه کردن دست‌دهی TLS»: پیام آغاز اتصال را به قطعات کوچک‌تر تقسیم می‌کند. حالت خودکار، Records، Compact یا تنظیم سفارشی دارد. در حالت سفارشی اندازهٔ قطعه، تأخیر و تقسیم نام سرور را تعیین کنید؛ مثلاً اندازهٔ 16-32 بایت و تأخیر 0-1 میلی‌ثانیه. این اعداد فقط نمونهٔ ورودی هستند.
• «سلام اولیهٔ رمزگذاری‌شده / ECH»: نام سرور را در بخش رمزگذاری‌شدهٔ ClientHello قرار می‌دهد. دریافت خودکار یا واردکردن ECHConfigList با فرمت Base64 در دسترس است؛ این مقدار، نام دامنه یا SNI نیست.
تقسیم TLS روی H2، از جمله تونل بیرونی WOM، اعمال می‌شود؛ ECH فعلاً مخصوص H3 است. تنظیمات سفارشی در تلاش‌های بازیابی حفظ می‌شوند و تغییرشان با اتصال بعدی اعمال می‌شود.
🔹
رفع باگ‌های اتصال و تغییر پروفایل
تونلِ در حال آماده‌سازی پس از شکست یا لغو اتصال بسته می‌شود. هنگام تغییر پروفایل، موتور قبلی کامل متوقف می‌شود تا پاک‌سازی آن اتصال جدید را خراب نکند. خطای تنظیمات ناقص هم پیش از روشن‌شدن VPN بررسی می‌شود.
اگر در Aether + Psiphon پیام «اشتراک یا نود اضافه کنید» می‌دید، در «مسیرها» گزینهٔ «فقط مسیرهای انتخاب‌شده / Use carriers only» را بزنید. این گزینه زنجیرهٔ خروجِ بدون نود را خاموش می‌کند و ترکیب انتخاب‌شدهٔ شما را نگه می‌دارد؛ خودِ Aether + Psiphon به اشتراک نود نیاز ندارد.
📥
دانلود نسخهٔ جدید:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.11.0
اگر معماری دستگاه را نمی‌دانید، APK نسخهٔ universal را انتخاب کنید.
@whitedns</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1942" target="_blank">📅 19:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1941">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iw7ui66St1BeHl3WelWMPn6YZmt_xU1iH2QwlDtT1lY86gznICnCj0Vh4DMzvdkjGzfm2COixc_XHhM2tremqpUszuRYmRD1FiXDQ1ojwa6X2jzsoDTKh2psQILfB6IxkeXp6ymhrtHTInU_H43sIWeHXgWhT8jA8AO_8JYcWBZfdO2uk8Ytgr2xAkA-_cO8yTuSCUicnR1hKt3rg7jsxfbuwf0V2-ImkG77YFrO71Ndt_0_P5PqUVmPa6wvKJHB0L2mk1nMmwKe43q4njmobnLmLvZqDsM1ffctzdLVMs_Ms1mHmfXGNda33SbMZ8FVrIQg6iJCT4aYRr275pGkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/whitedns/1941" target="_blank">📅 12:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1940">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Fragment + Fingerprint
📱
روی بعضی از اپراتورها
میتونید با اعمال کردن مقادیر زیر در pttn/pttng روی کانفیگ های BPB دوباره متصل بشید .
💻
https://github.com/patterniha/PattNG/releases
/ windows ,linux . mac
📱
https://github.com/patterniha/PattN/releases
/ android
در قسمت finalMask کل عبارت زیر را وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
در قسمت cipherSuites کل عبارت زیر را وارد کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
@whitedns</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/whitedns/1940" target="_blank">📅 12:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1939">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WInmtCo3b_ZNCYwxF_NPOfYDMM8rNfmMnkIgd1zrHPcyPadQBTHe2GdMy5PVBk3d50lOa5NExlON_lfJvIJ4jv3zTntZnqq_yzNw3O1A5gjVCQWw-2984tTOxjV3A0FYDP-Nm_oEFs0NTsdv9CQfhYkTZbwy_ATZFbrQ8dEDVQEljD5ZRvwoA3ySH31AAA8Ky7ACWsHM7Dm40JAMl2aV01_WwVj9K7sAwzLwVAUZml2wv5-7aTpJ-GL-pw0CU80Ek8MkOk0ctOWAhKKY-yrk4BKVMRzdbXINvqWg9Kz-4nyGGinv7uIcfkFTP-sRggEVpwEv1Fko8qM5gKHPryKSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دو عدد تصویر هم برای دوستان هستش که ایرانسل دارن که باید طبق آموزش گزینه های موجود رو انتخاب کنند
@whitedns</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1939" target="_blank">📅 05:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1938">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lzj54cxRjyznc613REhWb1eBALNsF-n1Csi0w30j4WaAxqOnDmrQGRYVhvSk__ajhkwx_Lyklm38z2gMnXwDFmks5F7wqAb7tQ6hDNerq9Ezg4sGkdiRR2uBBY3kbxbTQN_Sjrrakv3RYhmrtdt5P_LrC8qIH_xqMDDkWWei4OT4HxIilI_3Gcnz2yJSVdj1-5Usnbdz6puPK3vqKa1-SUO-p5uAgjqMBX0_5mDIKV54iwl81EBt5ExenbU-sUhFCmvoisrdWPENm48-SyXecjicoUGmgUrPTXg2uX2svOCAckLga7v9ZKl6fQnusZw7J-4ho0dXMsMQBqf2hUiAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ین تصویر هم مربوط به آموزش هستش برای
دوستانی که اپراتور هاشون رایتل و همراه اول هستش در این بخش باید مقادیر وارد بشود
cloudflare-ech.com
+udp://1.1.1.1
cloudflare-ech.com
+udp://9.9.9.9
cloudflare-ech.com
+udp://208.67.222.222
cloudflare-ech.com
+udp://8.8.8.8
نکته : فقط یکی از این عبارت ها باید وارد بشه یکی یکی تست کنید ببینید کدوم بهتر هستش
@whitedns</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1938" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1937">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سلام به همهٔ همراهان عزیز
👋
امیدوارم این روزها با وجود همهٔ فراز و نشیب‌ها، حال دلتون خوب باشه و اینترنتتون هم روان و بی‌دردسر
💚
از وقتی فیلترچی‌های عزیز محبتشون رو بیشتر کردن، دیگه هر روز باید یه راه تازه پیدا کنیم. این روش رو اول کانال پترنی‌ها (
https://t.me/patt_channel_x
) با کلی آموزش مفصل معرفی کردن؛ من فقط یه بخشش رو برداشتم و یه تغییر کوچیک روش دادم که جوابش واقعاً عالی درومد.
📌
نکتهٔ مهم: توی منطقهٔ من این روش فقط روی رایتل و همراه اول جواب داد. برای ایرانسل هم پایین‌تر آموزش جدا گذاشتم.
---
🟢
روش اول — مخصوص رایتل و همراه اول
۱) کانفیگ رو وارد کن
هر کانفیگی که دوست داری از هر پنلی بردار و توی PattNG بازش کن.
۲) آی‌پی رو عوض کن
برو توی بخش ویرایش، یکی از این آی‌پی‌ها رو کپی کن و توی «نشانی» (Address) بذار:
۱۸۸.114.97.1
188.114.97.1
۱۸۸.114.97.2
188.114.97.2
۱۸۸.114.97.3
188.114.97.3
۱۸۸.114.97.4
188.114.97.4
۱۸۸.114.97.5
188.114.97.5
۱۸۸.114.97.7
188.114.97.7
۱۸۸.114.97.8
188.114.97.8
۳) اثر انگشت
همون‌جا پایین برو و گزینهٔ «اثر انگشت» (Fingerprint) رو روی Chrome بذار.
۴) echConfigList
باز پایین‌تر برو و یکی از این‌ها رو توی بخش echConfigList بذار:
ECH ۱
cloudflare-ech.com+udp://1.1.1.1
ECH ۲
cloudflare-ech.com+udp://9.9.9.9
ECH ۳
cloudflare-ech.com+udp://208.67.222.222
ECH ۴
cloudflare-ech.com+udp://8.8.8.8
ECH ۵
cloudflare-ech.com+udp://1.0.0.1
ECH ۶
cloudflare-ech.com+udp://8.8.4.4
ECH ۷
cloudflare-ech.com+udp://149.112.112.112
ECH ۸
cloudflare-ech.com+udp://208.67.220.220
ECH ۹
cloudflare-ech.com+udp://76.76.19.19
ECH ۱۰
cloudflare-ech.com+udp://76.76.2.0
ECH ۱۱
cloudflare-ech.com+udp://94.140.14.14
ECH ۱۲
cloudflare-ech.com+udp://94.140.15.15
ECH ۱۳
cloudflare-ech.com+udp://64.6.64.6
ECH ۱۴
cloudflare-ech.com+udp://64.6.65.6
ECH ۱۵
cloudflare-ech.com+udp://45.90.28.0
ECH ۱۶
cloudflare-ech.com+udp://45.90.30.0
ECH ۱۷
cloudflare-ech.com+udp://185.228.168.9
ECH ۱۸
cloudflare-ech.com+udp://185.228.169.9
⚠️
نکته: این عبارت‌های ECH ممکنه منطقه به منطقه فرق کنن؛ پس همه رو تست کن تا بهترینش رو پیدا کنی.
۵) ذخیره و وصل شو
روی تیک بالای کانفیگ بزن که ذخیره بشه و تموم — راحت وصل می‌شی.
✅
---
🟢
روش دوم — مخصوص ایرانسل
بازم ممنون از پترنی‌های عزیز که روش فایروال ایرانسل رو هم گذاشتن. من یه تغییر کوچیک روش دادم که به نظرم سرعتش خیلی بهتر شد. اینجوری:
۱) آی‌پی
کانفیگ رو توی PattNG باز کن، برو بخش ویرایش و یکی از این‌ها رو توی «نشانی» بذار:
۱۸۸.114.97.1
188.114.97.1
۱۸۸.114.97.2
188.114.97.2
۱۸۸.114.97.3
188.114.97.3
۱۸۸.114.97.4
188.114.97.4
۱۸۸.114.97.5
188.114.97.5
۱۸۸.114.97.7
188.114.97.7
۱۸۸.114.97.8
188.114.97.8
۲) finalMask
یه کمی پایین‌تر توی finalMask گزینهٔ tlshello-0-len رو انتخاب کن.
۳) اثر انگشت
باز پایین‌تر توی «اثر انگشت» گزینهٔ unsafe رو بزن.
۴) مجموعه رمزنگاری
باز هم پایین‌تر توی «مجموعه رمزنگاری» (Cipher Suites) گزینهٔ real_firefox_cipherSuites رو انتخاب کن.
۵) ذخیره
توی پایان روی دکمهٔ ذخیره/سیو بزن تا اعمال بشه.
---
امیدوارم این راهکار به دردتون بخوره. موفق و پایدار باشید
🌹
🚀
⚠️
یادآوری آخر:
توی بعضی مناطق سیم‌کارتت ممکنه همراه اول باشه ولی فایروالت ایرانسل، و برعکس؛ سیم ایرانسل ولی فایروال همراه اول. بقیهٔ اپراتورها هم معمولاً از یکی از همین دو فایروال استفاده می‌کنن. پس یه زحمت بکش و هر دو روش رو روی اینترنت خودت تست کن
❤️
@whitedns</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1937" target="_blank">📅 05:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1936">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUak7Ipis5K2v9QVftqZm5P459tao1vZHJg9ZJ8m6PAAPGiFyIsnQyC9haEXRHXwSxYD7sXw3xTngRz4Bk4p3hrEVGZJEspjev4FjJOogRydOPccs5W3Ht0_OUHaW-0o4OAbACRaoM10NvUDk4fBDcByDOxCC7EddZuP7xiBp6H7kj3acSJyAyPSRz3jZiI-K7sMab2RYGSyQ9s64DaTxHDvN2ouE7l0p426old-YdvhocMu4yFcSTxjpjcvgRZiTzkDB7EcXvdmPFab8TRfssCE2qtCNiMF-dDs22Hd6AftWLPKIJSxB9GxxdsLdYzc7dVfGnhgURPP3NdHkcLg_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
ساخت پروکسی رایگان با Cloudflare!
⚡️
توی این آموزش یاد می‌گیری چطور فقط توی چند دقیقه پروکسی خودت رو بسازی.
🚀
🔗
لینک ویدیو:
https://youtu.be/8JytQZ1unz0
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1936" target="_blank">📅 18:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1935">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGFYJo3cvHju0R4Kz7x5AB1z8ToP5E_Ln-02-_G0EFJK6sLUVX_heeZEYwOLAhiLI_TOqgOZG4EM5JNqs1oXUCn-BV6pT78-dhCZx_xx7N1fzNyFgmpMjLwFTwr4H7t_AwxgtPQBJUiNZC2vuIDjlhrsIxAeYaJRjD4DPmcHIo444V7Ryh3rJRerUi4kh1dgJZtTvwJE_itxIeGGDRy2eLak4Pu0H3mvbdjox_vIwUZDvi5wKVbmx7k4p9zxcofx3pJbS-c9iFFR7fBikZxzgkCbXFH1nPrU5DrDfum_nFz4TO9FOgRNFgTOgP5TagxCCfuag9MChju_lIeViNCuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی ویدیوی جدید رفتیم سراغ CoreForge، یه اپلیکیشن کاربردی برای آیفون که از روش‌های مختلف اتصال، از VPN معمولی تا DNS Tunnel، برای شرایط متفاوت اینترنت ایران پشتیبانی می‌کنه.
🔥
از نصب و تنظیمات تا قابلیت‌هاش رو بررسی کردیم.
📹
تماشای ویدیو:
https://www.youtube.com/watch?v=yPLb4z4nF70
📱
کانال برنامه:
@coreforgeios</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1935" target="_blank">📅 14:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1934">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.3.10-P63_arm64-v8a.apk</div>
  <div class="tg-doc-extra">73 MB</div>
</div>
<a href="https://t.me/whitedns/1934" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/whitedns/1934" target="_blank">📅 04:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1933">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">PattNG v2.3.10-P63
منتشر شد.
تغییرات اصلی
:
۱. با تغییرات انجام شده امکان اتصال به پروتکل MASQUE-HTTP/2 روی اکثر نت‌ها امکان پذیر شد.
همچنین پروتوکل جدید
Wireguard-Over-Masque (new gool)
اضافه شده، اتصال به این پروتوکل به شما ipی غیر ایران میده، در نتیجه برای دور زدن تحریم‌ها نیاز به چین کردن آن با سایفون و یا سایر کانفیگها ندارید (نوع HTTP/2ش رو اکثر نت‌ها وصل میشه).
۲. کانفیگ‌های اتر (warp/psiphon/tor) را اکنون میتوانید به سادگی از طریق exit-node با هر کانفیگ دلخواهی از همان منوی اتر چین کنید:
selected-config -> warp/psiphon/tor
(برای برعکسش همچنان باید از قسمت add proxy chain اقدام کنید)
///
فرگمنت به طور کامل روی فایروال همراه اول حتی روی IPv6 هم بسته شد، در نتیجه فعلا تا انتشار متد جدید امکان استفاده از Serverless-for-Iran رو اکثر نت‌ها مقدور نیست (همچنان برای دسترسی مستقیم به یوتویوب برای سرعت و حذف تبلیغاتش میتونید از Mitm-DomainFronting استفاده کنید)
///
با توجه موارد بالا پست
https://t.me/patt_channel_x/166
هم آپدیت شد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1933" target="_blank">📅 04:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1931">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gCXfuZ4k_B796mtl7RCN97KSLk6mCQxistj7btZzVDvoD1bmIA1iq7tSs1_0QXpaE5hS8tiCJ91Bu06r4Kmh-b1xbBAkXDL3jn53vlpHT_03bVaD54XJESaITfXViDz7kYB0gQkct9fiDiVWW9UXrT1J_myIUYXxufwSumEDwyEMd1P5Nz8oHMTE7WbHoqa33QqGtGQbw7gXQRIqtuHSUYmDeealDIKQhq2N_-Hx5x8AgNaydK8FVI-CSau2_N__nje2w0DWzIdB_lFkXaC9LTB_QEWx_s24U8D6hrpUhBGHfm4caSuZH3DFfvOaiH5KZoZhVxQ5VFW5T43fxlkE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kYm8cP1LnruiPnsCMy9eWLZ4cADKS7iRDIrU_sbFR0JjpI_sZj1fSNFCjmuWM_Y9WMabqCK71bPcblg8MT5F6ZQbkVc79guMPfLb3bojypVeUO1fNwZ35yCdCIJeGSTCPgWz-LPZxpBM9eKGV9LWovI3rQsehz3P3Bp6ZQsPJJlqgOYe6NU18hXTHEybp8wheWy81njV7HZzguP7LNGUnZE-1sYaT7q54_oX4Q_Vow3VTJ-bhEGbdTZgIPwL4MASdBcWtvT5-oqQQcaBD93qgwu-2qu7TjESgjhuLtfRNPs1Za1hYI6pPcnrIJv9jSBRCTFLcFDV-s78jvpQOu5UNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این تصاویر هم مربوط به تغییراتی هستش که باید در کلاینت MahsaNG ایجاد کنید دوستان گرامی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1931" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1930">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">درود بر همگی دوستان عزیز
😊
یک راهکاری را یکی از بچه های کانال پیشنهاد داده
اسمش رو نمیشه «متد» گذاشت، ولی راهکار خوبی هست.
میتونید امتحان کنید امیدوارم برای شما هم کار کنه
مرحله ۱ — آماده سازی کانفیگ
ابتدا یک کانفیگ از هر پنلی که میخواید (مثلاً BPB و ...) بگیرید و متد Fragment + Fingerprint رو روی اون اعمال کنید. برای این کار، نصب کلاینت PattNG لازمه:
🔗
https://github.com/patterniha/PattNG
مرحله ۲ — آموزش اعمال متد
۱. کانفیگی که از پنل گرفتید رو در کلاینت وارد کنید.
۲. روی آیکون ویرایش (مداد) کانفیگ بزنید و مقادیر زیر رو اعمال کنید:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
۳. بعد از اعمال، یک تست بگیرید و سرعت رو بررسی کنید.
⚠️
نکته: من به تازگی متوجه شدم سرعت متد افت کرده — و به نظر «فیلترچی» عاملش هست، بگذریم!
😅
برای افزایش سرعت این متد، دو راهکار داریم:
راهکار اول — ساخت کانفیگ ترکیبی (Chain)
۱. یک کانفیگ «اتر» با قابلیت سایفون روشن و پروتکل WireGuard بسازید (نوع پروتکل برای هر اپراتور فرق داره، نوع اتصال سایفون هم خودکار).
۲. کانفیگ ساخته شده رو در کلاینت، از بخش «افزودن کانفیگ»، گزینه یChain Proxy رو انتخاب کنید.
۳. دو کادر خالی ظاهر میشه:
- یک اسم دلخواه بذارید (پیشنهاد من: «فیلترچی احوال مادر گرامی چطوره؟»
😄
)
- در کادر اول: کانفیگ BPB که متد روش اعمال شده
- در کادر دوم: کانفیگ اتر
- بعد دکمهی Save رو بزنید.
۴. حالا سرعت رو روی منطقهی خودتون تست کنید. اگه کارتون رو راه انداخت که عالیه؛ اگه سرعت ضعیف بود، برید سراغ راهکار دوم.
راهکار دوم — کلاینت مهسا NG
۱. کلاینت MahsaNG رو از گوگل پلی دانلود کنید:
🔗
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
۲. همون کانفیگ BPB که متد روش اعمال شده رو کپی و در مهسا NG وارد کنید.
۳. نحوهی انجام کار رو به صورت تصویری براتون میگذاریم
موفق باشید!
🚀
به امید آزادی
🫡
@whitedns</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1930" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1929">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!  نسخهٔ مک ForgeCore از ریویو اپل گذشت و حالا روی TestFlight در دسترسه.
🚀
📥
دانلود و نصب: https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید: اول اپ رو کامل پاک کنید، بعد از لینک بالا دوباره…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1929" target="_blank">📅 08:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1926">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCoreForge</strong></div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!
نسخهٔ مک
ForgeCore
از ریویو اپل گذشت و حالا روی
TestFlight
در دسترسه.
🚀
📥
دانلود و نصب:
https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید:
اول اپ رو کامل
پاک کنید
، بعد از لینک بالا دوباره نصبش کنید. بدون این کار ممکنه نسخهٔ جدید درست بالا نیاد.
ForgeCore چیه؟
یه کلاینت شبکه برای وصل شدن به سرورها و کانفیگ‌های پروکسی/VPN خودتون:
- افزودن کانفیگ با
لینک اشتراک
،
QR کد
یا
لینک تکی
- تست
پینگ و در دسترس بودن
همهٔ کانفیگ‌ها
- پشتیبانی از پروتکل‌های متنوع
- اشتراک‌گذاری اتصال روی
شبکهٔ محلی و Personal Hotspot
برای نصب کافیه اپ
TestFlight
رو از App Store بگیرید و لینک بالا رو باز کنید.
🐞
اگه کرش یا مشکلی تو اتصال دیدید، همین‌جا بگید تا سریع درست بشه.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1926" target="_blank">📅 00:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1925">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-gsvNevu_7mEv3sm0iAuugf_pT94u34Mrg-vRLpcSL9lNPmdLuKGS8PeS-tgDfoDdmHtYkzSrsKeowrRZ6BwioWIDu2d0jIgZGHtWinJMhWn55AePhzRi6DpLJVitDEcl49as7GMsvbVkOEAYf4twV-aXw4e2T4BPJfU9VmCxx5jHIZYB61rmyVY8kyotyVpTifQUoycXTFKLcl_LEM7UooUAVpIobwOUlPhXkeFIgNwo2AMBujlM_m9Rv3Kwh1AYIbmouU0RTDFAYpSKFe0J95z2aJbMlLnOxv-yjfbdoGHaDSKimaWf1UhOKYb6NlrtB22BNCXxzjON0oI_BzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/whitedns/1925" target="_blank">📅 00:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1924">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔥
آپدیت مهم WhiteDNS
فایروال جدید، ترافیک DNS بالاتر از حدود ۶ کوئری در ثانیه را محدود می‌کند و همین موضوع باعث قطع شدن بسیاری از تونل‌ها شده است.
برای اتصال پایدارتر، برنامه را به آخرین نسخه آپدیت کنید
👇
📱
دانلود نسخه اندروید 1.6.4
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.4
💻
دانلود نسخه دسکتاپ 1.2.4
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases/tag/desktop-v1.2.4
⭐️
تغییرات و تنظیمات پیشنهادی
🔹
محدودیت نرخ ارسال کوئری
در تنظیمات پروفایل CottenDNS، گزینه Query Rate Limit را روی ۳ کوئری در ثانیه قرار دهید. ممکن است سرعت کمی کاهش پیدا کند، اما اتصال پایدارتر خواهد بود.
اگر با اضافه کردن Resolverهای بیشتر سرعت بهتر شد، گزینه Rate Limit Counts را روی Per Resolver قرار دهید.
🔹
تصادفی‌سازی زمان ارسال کوئری‌ها
گزینه Timing Mask را روی Light یا Strong تنظیم کنید تا زمان ارسال کوئری‌ها تصادفی شود و ترافیک شما ریتم ثابت و قابل تشخیص نداشته باشد.
🔹
تعویض خودکار دامنه
اگر دامنه سرور مسدود شود، برنامه به‌صورت خودکار به یکی از دامنه‌های جایگزین دریافت‌شده از سرور سوییچ می‌کند؛ بدون نیاز به ساخت پروفایل جدید.
🔹
اتصال پایدارتر
پاسخ‌های جعلی Domain Does Not Exist یا NXDOMAIN که فایروال ایجاد می‌کند، دیگر باعث حذف Resolverهای سالم هنگام برقراری اتصال نمی‌شوند.
👀
محدودیت نرخ ارسال کوئری و تصادفی‌سازی زمان ارسال به‌صورت پیش‌فرض خاموش‌اند. برای استفاده از آن‌ها، تنظیمات بالا را فعال کنید.
🖥
برای مدیران سرور
ابتدا نسخه سرور CottenDNS را به آخرین نسخه آپدیت کنید:
https://github.com/WhiteDNS/CottenDNS/releases/latest
• برای استفاده از Domain Rotation، دامنه‌های جایگزین را در ADVERTISE_DOMAINS قرار دهید
• مقدار ZONE_NS را روی Nameserverهای خود تنظیم کنید تا سرور به کوئری‌های نوع NS مانند یک DNS Server عادی پاسخ دهد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1924" target="_blank">📅 14:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1923">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مادر بزرگ ۷۰ساله من برای اینکه بتونه با بچش ۱۰دقیقه در روز صحبت کنه VPN استفاده کردن باید یاد بگیره.
باید استرس بکشه که الان قطع میشه، همراه خوبه یا سامانتل، باید بدونه سابسکرسپشن چیه، سرور چیه و ۱۰تا روش امتحان کنه تا به گوش من برسونه که 《مامان VPN من بازم قطع شده》
😭
لعنت بهتون که به دل کوچیک و بزرگ حسرت گذاشتید.
ببخشید یکم شخصیش کردم و میدونم این وضعیت دردسر هممونه و نه فقط من. شاید این در مقابل دردسر خیلی ها حتی چیزی هم نباشه.
خیلی از این متد ها مناسب افراد مسن تر با دانش کم نیست. تا جایی که میتونید هواشون رو داشته باشید
🥲</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1923" target="_blank">📅 13:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1921">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-GUI_0.8.0_x64-setup.exe</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/whitedns/1921" target="_blank">📅 13:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1920">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PM-yGYPmXPlrKxABv2GIjRUmJZthU4gzUVScIT97lawiJFO8EpFqdHDomf-PYDytygbzZSOl0AYp4SFLjWeA9grH4bBSCLiXqrZSJlitNk5QOetLm-o88Cw8s6TIgZ6wn6FOse6yJ4H0mOdc85HdxkxJdzUaXJiGUH0C-_njYay3ELyx7clKEDt72-Ht4yIH-gqWNuEfmAvpZ6Nsm3xmgBQ9TXLdTQHNOX4Xhb0s086tp2CMpunUQ0fFWaEd6rkAGYl2nRwmLswBjnyX0oTWlr5VRq2nBpeVorbsxVGyoN6aN4cg6YIch2ICNnLZFBFJac5a6d3meaGQe21QRQ0O7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1920" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1918">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Qig2TW9wu76d1xn12wM54oLc-9Z3pJn0JGfOXkFNEavFenW80EIa1FLk5zVpR_4fmLd5UbrwfdY0tPYxj9BoUEZU2fgJYQbGm7S2H9wE3RjTrYf7l93UPgxjaI--M7xx1aAFxoJM5AoYCNFiU8V0-Lxz4ZBu3lDFATgSLs-Qlw7qeOnV5pQ9Mj4fHw4R05NkKnJnN9C7YYYQCWnrDUUYrQujHDcJUyjCuaM5CIWOwqnoZwhJfI7FnDy714qdtC1pOupAE5sWRHLCTLR-8wu1c4eTqQWMqaVBHVTmGuFnJYdpJ375jlaRjE2asMPRkAKpSazZN9pdXHH5Ulg8pwU-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/mMu5bCy5bFNTioKeQJUhngopYp1F5JtxcRdwLNaCwM8YZ1_-MTluL8Dz9WOf2K7Hkj7lduUJZNO3PnFvonNEzN7MpenhK52rgwj_Fs0QewHc5Ns6_bId96mITIeNJ6TdB_otJLNa1Wf1u5Rb_Qz09_T0ANLXZZghfqN7pPMmEJJorMVtl1oTVnN5FRRCRC_gO8Dhv9rbzPe0ts36zfEoI2trvmbOR9Qq4m_WNo00g8ICV5lpb9Cb5i-AlsG9mFu9XATS56LQEwALEIH8RoG3FBzBlfgqK1jsu0Ac8rbLPJ3BqfsExF4JDWRyGiJZMs2x1oM5KXjoBo4fy2vsGovVFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان
🙋‍♂️
در نرم افزار
whiteaesther
اگر برای اتصال مستقیم با aether مشکل دارید، این احتمال وجود دارد که دستگاه شما به هر دلیلی روی اپراتور کنونی نمی‌تواند هویت WARP/MASQUE ثبت کند
📡
برای حل این مشکل برید routes  و اولی را روی تور  یا سایفون و دومی را روی aether بگذارید و دکمه اتصال را بزنید
⚡️
. صبر کنید تا سبز شود
✅
حالا شما هویت masque خودتان را دارید و می‌توانید از aether به تنهایی یا ترکیبی استفاده کنید
🚀
@whitedns</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1918" target="_blank">📅 13:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZW-pAyMA4kwKxHVnVkzwFYb5JLn8i6ZBwPsg4uuxWNPERZs-c2Jy5VR0eziCxkHo0CWhx99Uk-n5ULmfqNxo2bkclAF5J_aSmuKp5FiyCAfqG8TlOEv7V0fIk5LQ6QyCKHgr1g_jMpvqf6DDx3AYoq8fmJ6fzXcOspIzNb6WjX95s2N8a-pZWUdJJKjI03cPpQeRpVtz3TyquZyPilOhfwycjrkLfkP4AObl-O-rD5JejWyq-85kJ4f6LrVsJ96lDsaqh113A6TQH7YDwzExQkHnDDcz4GebZO6Z1D5FYhxWhiQwtvw7IJbJNjcCywjYJR3R-8dqodCeFWaoShBHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر WARP محدود شد، چطور از WhiteAesther استفاده کنیم؟
⚠️
طبق گزارش‌های دریافتی، ارتباط UDP با IPهای کلودفلر روی همراه اول محدود شده است. احتمال گسترش این محدودیت به اپراتورهای دیگر وجود دارد، اما هنوز نمی‌توان آن را قطعی دانست.
این محدودیت می‌تواند اتصال
WireGuard و MASQUE H3
را مختل کند؛ با این حال، WhiteAesther مسیرهای دیگری هم دارد.
۱️⃣ ابتدا حالت خودکار را امتحان کنید
در تنظیمات برنامه:
🔹
Traffic → Coverage:
گزینهٔ «کل دستگاه»
🔹
Routes → Carrier:
گزینهٔ «خودکار»
در نسخه‌های دارای این قابلیت، برنامه مسیرهای Aether، Psiphon و Tor را بررسی می‌کند.
⚠️
اولین اتصال روی شبکهٔ محدود ممکن است چند دقیقه( تا پنج دقیقه ) زمان ببرد.
⚠️
۲️⃣ برای اتصال مستقیم، MASQUE H2 را امتحان کنید
از مسیر زیر پروتکل را تغییر دهید:
🔹
Routes → Advanced → Preferred transport → MASQUE H2
H2 روی
TCP
کار می‌کند؛ بنابراین بسته‌شدن UDP به‌تنهایی آن را از کار نمی‌اندازد. البته اگر مسیر TCP هم فیلتر باشد، اتصال برقرار نمی‌شود.
۳️⃣ امکان استفاده از IPv6 را حفظ کنید
🔹
Traffic → Addresses → IPv4 + IPv6
اگر IPv6 روی اینترنت شما قابل‌دسترسی باشد، ممکن است مسیر اتصال باقی مانده باشد. انتخاب این گزینه داخل برنامه، به‌تنهایی روی خط فاقد IPv6 دسترسی ایجاد نمی‌کند.
۴️⃣ تکه‌تکه‌کردن دست‌دهی TLS را امتحان کنید
🔹
Traffic → Advanced → Split the TLS handshake → روشن
این گزینه ممکن است در برابر بعضی روش‌های فیلترینگ کمک کند، اما مسدودشدن کامل IP یا TCP را برطرف نمی‌کند.
۵️⃣ اگر اتصال مستقیم جواب نداد، حامل را تغییر دهید
در
Routes → Carrier
حالت دستی را انتخاب کرده و
Psiphon
را امتحان کنید. گزینهٔ دیگر،
Tor با پل خصوصی obfs4
است؛ معمولاً کندتر است و ترافیک UDP را حمل نمی‌کند.
نام و محل گزینه‌ها ممکن است در نسخه‌های مختلف متفاوت باشد.
⚠️
هیچ‌کدام از این روش‌ها اتصال را تضمین نمی‌کند. بسته‌شدن WARP لزوماً به معنی ازکارافتادن کل WhiteAesther نیست؛ نتیجه به مسیرهای باز روی اینترنت شما بستگی دارد.
تشکر ویژه از
@patt_channel_x
@whitedns</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1917" target="_blank">📅 09:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1916">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">پروتوکل UDP هم به طور کامل روی ip های کلودفلر بسته شد (فعلا فقط روی فایروال همراه اول)
در نتیجه امکان اتصال به warp از طریق پروتوکل wireguard و یا masque-h3 دیگر امکان پذیر نمیباشد.
برای پروتوکل masque-h2 نیز، امکان استفاده از ECH از سمت خود کلودفلر بسته است، بنابراین در حال حاضر فقط با استفاده از IPv6 میتوان از این پروتوکل استفاده کرد.
روشهای جدیدی که بزودی منتشر خواهد شد امکان اتصال کانکشنهای TCP را به کلودفلر فراهم میکنند، در نتیجه، میتوان از آنها برای masque-h2، کانفیگهای ورکر، cdn و به طور کلی تمام اتصالات TCP روی کلودفلر استفاده کرد.
حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1916" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">PattNG v2.3.10-P59
منتشر شد.
امکانات اضافه شده
:
۱. مقادیر متد فرگمنت+فینگرپرینت اکنون به صورت آپشن تو خود اپ اضافه شده، بنابراین برای اجرای متد فرگمنت+فینگرپرینت کافیست:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
را انتخاب کنید، و دیگر نیاز به کپی پیست ندارید.
برای اجرای این متد روی کانفیگ‌های اتر نیز کافیست:
finalMask: tlshello-0-len
fingerprint: semi-python
را قرار دهید.
۲. اکنون امکان chain کردن کانفیگ‌های psiphon/tor/warp با هر کانفیگ دلخواهی به صورت
دو طرفه
برقرار شده.
به طور مثال برای chain کردن سایفون با یک کانفیگ دلخواه ابتدا باید یک کانفیگ psiphon-only بسازید و سپس از قسمت Add Proxy chain میتوانید آن را با هر کانفیگ دلخواهی به صورت
دو طرفه
chain کنید.
همچنان برای chain کردن سایفون با خود warp باید از همان منوی aether اقدام کنید (warp -> psiphon/psiphon -> warp)
۳. با توجه به فیلتر شدن دامنه دریافت کلید وارپ، اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) و یا حتی ech این محدودیت را دور بزنید و بدون نیاز به فیلترشکن مجزا کلید وارپ را دریافت کنید.
۴. به طور مشابه با توجه به فیلتر شدن دامنه masque-h2, اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) این محدودیت را دور بزنید و به پروتکل masque-h2 نیز متصل شوید.
امیدوارم حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/whitedns/1915" target="_blank">📅 04:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1914">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ARhEe_8BsMaFogeqjJJc9oMhieo3SaK53GNk1qzQQFeOPlOQfR2nFLakxYYorLPXdXGHDg15tOk4f0A05VfJHu54XQdukYfKmBLxSvZ_uM3K9fyTlvwn8yrKvX3Lr3FDb1LMpWZ58wKLpQdu9RVWvn3YYe4RYI6q3lZoOBqidCrUfXujX0cMtRCS6Q826oAF0jUy8Z9QsQrDMMjmqz_oNQGdxwZsFIb4LrzE-wc_m4rfwtuk09IahYCaN3mArCQAfztFq__P6LsS2DgqCre4BTVC1uW_g75jduSwvXAiOkld7QD_9go5QdlJyc_JOLH3k9nGu4dqcDNwdfzslAM0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1914" target="_blank">📅 01:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1913">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👆
این کانفیگ ها را هم برای amneziawg روی آپ whitevpn امتحان کنید
یکی از دوستان خوب زحمت کشیدند این کانفیگ ها را بازنویسی کردند
❤️</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1913" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1908">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-mx-free-5.conf</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/whitedns/1908" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1908" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1907">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوستان عزیز:
به جز خود سرورهای whitevpn , الان ۶ موتور اضافه شده است که هر کدوم روی یک نوع اپراتور و یا منطقه کار میده
شما باید خودتون موردی که الان کار میده را پیدا کنید .
فیلترینگ مثل سالهای گذشته یک الگوی ثابت نداره و نمیشه یک نوع خاص از فیلترشکن را به شما داد که روی همه چیز کار کنه
ارادتمند
تیم وایت
❤️</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1907" target="_blank">📅 19:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1906">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn3.10.2026.conf</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/whitedns/1906" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1906" target="_blank">📅 19:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1905">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-13.conf</div>
  <div class="tg-doc-extra">340 B</div>
</div>
<a href="https://t.me/whitedns/1905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1905" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1904">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-5.conf</div>
  <div class="tg-doc-extra">342 B</div>
</div>
<a href="https://t.me/whitedns/1904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1904" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1903">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-poll">
<h4>📊 دوستانلطف کنید اول این فایل ها را ذخیره کنید بعد از قسمت پروفابل - افزودن- amneziaWG  -وارد کردن فایل پیکربندی این فایل را وارد کنید و امتحان کنید که ایا وصل میشید یا نه</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1903" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1902">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-poll">
<h4>📊 کدام پروتکل(های) زیر روی شبکه شما کار میکند ؟</h4>
<ul>
<li>✓ سایفون</li>
<li>✓ تور</li>
<li>✓ Ssh</li>
<li>✓ امنزیا amnezia wg v3</li>
<li>✓ IKEV2</li>
<li>✓ سرورهای عمومی whitevpn</li>
<li>✓ سرورهای اختصاصی whitevpn</li>
<li>✓ اتر whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1902" target="_blank">📅 15:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1901">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/khZHAQ3aBjEYOiQdzjA4UsGn79STNiPWY9I916kkrIyuNjm5xNv26viplF5ca936KylN9-hcLwK9gHHInkLwmou1wjlh21XKBRqbh6gCgRsb7in2RqvYWHoSUnjDTeANHOjdMW9xKB3l4P2a-1rI9bg3kkKuLz4U8RkF2FJEXJhqL3sNJZNE08dI67uZImhfS_TexxNxHymx2dhF0RuRcnojxebmaMhOFl3VOV733fUfrjP1kqEIT6AOn5OvRhst9cxv43E9ZTZbPiMoGXzBmCWKSy196G0_PyKgX6rj4TcOCuBpBhuvfsCWuDfoRF3ldennEFyXDUWKNLCHGIF9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای دسترسی به امکانات جدید نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 میتونید با مراجعه به تب "پروفایل" - "افزودن" آنها را مشاهده کنید
@whitevpn</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1901" target="_blank">📅 14:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1898">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.7.0-beta.1-universal.apk</div>
  <div class="tg-doc-extra">203.4 MB</div>
</div>
<a href="https://t.me/whitedns/1898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1898" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1897">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/veTlfyqPQntCv2RviEdFyr4L1MhAekAiPU3oUt2ruZXP6KTD4kKOJgt9nN1VislCmARe_ucrrR--1KoS-ht6iXAHrV4FKhuxtCcQsoiByqXoAql-3ELrtO5IhD1669jY7nykuBt8ou5I6g69ciTHJ3jT0yK30bVy4PinZm1UPfEqE3YNMs4keFyKULm_vLWOdp2J8JExn_GyDJc6AkEzGAx2-Sk0yLFnV4G8NV5JB1VQH1CS85xaj5xKe3p14Cj7RMoRphYwKF6HSHzG81Ew0uqgeYHgQkGC1uRsXFEiqP13LdQJXE1-Sao_fQnfPtQ_Chn2c6Wi3CSrNzucGcQ_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!
⚠️
🔥
در این نسخه، شش موتور اتصال در دسترس هستند:
Psiphon، Tor، SSH، DNS Tunnels، IKEv2 و AmneziaWG
✨
تغییرات اصلی:
• صفحهٔ یکپارچهٔ «پروفایل‌ها» برای مدیریت اشتراک‌ها و اتصال‌ها
• واردکردن کانفیگ AmneziaWG از فایل یا لینک
vpn://
• انتخاب کشور سایفون از فهرست
• هماهنگ‌سازی فرم‌های فارسی و انگلیسی و اصلاح نمایش گذرواژه‌های طولانی
• بهبود پایداری اتصال و قطع سایفون و نمایش ترافیک
⚠️
این نسخه
آزمایشی
است؛ بررسی کامل همهٔ موتورها روی دستگاه‌های مختلف هنوز ادامه دارد. برخی موتورها به سرور و کانفیگ سازگار نیاز دارند. نسخهٔ پایدار
1.6.10
همچنان در دسترس است.
⚠️
📥
دانلود نسخهٔ آزمایشی
اگر مشکلی دیدید، همراه با نام موتور، مدل گوشی و نسخهٔ اندروید گزارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1897" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1896">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hCpRImgizJQLQiYRxSC_azJjlM9HAHfwTukzkucLO9atymVweP-bWU6-VKIg1M3hCJvZ_AcCAYTmz9957GJY_sryou15fJ64irxQG-Tb3w-VzH56OmlFG2VSLZIl9KOrpIxS7wMqooK_jZTsGlY2CSHGBuLCN9KZcXEgF0-TWOXmJMdlqa4ssqPPCumIymG4x-vDOuSN1H7YYGhq4t20YfLy2A6xtceyh2S8F_XK4a0RXOt9Gzg-FNP52Fn2K-xHPVotfQgSxz73M8y9JgVkX-N7LGtNOFIlplwHUKsd-AE3S3TubsfiMcIEymsudmpBOlU__3YcWxNwFRz55E4_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/whitedns/1896" target="_blank">📅 19:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1895">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/h2k-GaF34hSlxGxS2CI5jObOmHsMR3Or-741Rr37j_BQX0AhSy1xdnI4KA5bggCwNuk0lL2gVQQNbbMoijVvOAA_sT-sh-3HjKeOz1O3iixMRmt7VRFT3syRZ1qEfY7VSCJ0yMKnrRykAM_ft-MbpJYoaRfi3qwgNV2KpuSrdktB7veQZ28MM2tN-3BvQARCEYzb4RC8inrcR5agCimiiCFn8Fb9Nv2VSE9ouyBKHqCtJJty6VE-EMxOLH1jhlZe_BgjrWdNLUxky-lTKf8Qh_9_I_W_q_qfCEUy5iE_msQqukymXlYN2aiNhi7_gMjXC1Q2FjnrrHO0XWCtQwz_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/whitedns/1895" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1894">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X66g9cbGtg53bJfEwd4I2hJ7_qRpOCjC3cg_tVbN6G6n4-XTXo0wT7HOytBRy8LnAaUAerBVzFxESfZapAA-wUog0EatNvFGcnB6FbjSDNjkZmQxdmDfQ6800L6h6jIm9W6xz2e3vwAau-vH6l5jigjOO0Dfun2yUbISdEb9JkYVtolIaYMz-f4gQETB1NCRKjj84rzhUEn54cNbO_uoLcCjkn6OC_fDhOFLuPBva0WW0QSjUNom3PAFO1v5EMGJp3BcdISXNFqnz07SmGiMgAmVj9Io5eQ8PSDkj-Z9I4fH-LsH_hsEMxAnV6F6XyLntMNXBCsGbD5oVZgYkklaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/whitedns/1894" target="_blank">📅 17:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1893">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommmahdi_sz</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrYPXbek9ALrhdnIbgezohFbdymdRkz4F79pOpTFbEzT6uGGAk2GRdq8uVK3DyCc268CNGiPVsBXv6NyQH8KnnWwgReoIxPE_IrVfjyriCPhHcTwcXz739H0Aev7e1Y-u71FHozRuwqQIaNvvLU1a-g8qdVLjnco8yU2gjtXsym8H4yI03buevJ42tsj45YWY9K6smUVGkpovpotcCVuQA2QKtvZRlwXh8FXZ0p-hvhJo2Qqah0Y_VM215Fd9YVHz4Wf9Cztkmor6CFMKkuqIO9YLzTdwTjKur0V1V4wC_bflbohnbKG_OtwPVi4plDpzzJWkdUFeEm73M2Kqkw-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ArasClient | کلاینت قدرتمند اندروید
یک کلاینت مدرن و متن‌باز برای مدیریت کانفیگ‌ها، Subscriptionها و اتصال‌های مختلف، با امکانات پیشرفته برای تست و مدیریت سرورها.
➿
➿
➿
➿
➿
➿
➿
➿
➿
⚡️
Smart Connect
تست هم‌زمان کانفیگ‌ها و مرتب‌سازی بر اساس Latency برای پیدا کردن سریع‌تر گزینه مناسب.
📡
Subscription Management
مدیریت چند Subscription، بروزرسانی کانفیگ‌ها، نمایش حجم مصرفی و زمان باقی‌مانده و امکانات بیشتر برای مدیریت سرورها.
.arasc
فرمت اختصاصی ArasClient برای Import / Export و اشتراک‌گذاری کانفیگ‌ها با حالت Protected.
🔐
Per-App & Routing
پشتیبانی از Per-App، Routing، Proxy Chain و Policy Group در بخش‌های پشتیبانی‌شده.
🔥
پروتکل‌های پشتیبانی‌شده
VLESS • VMess • Trojan
Shadowsocks • Hysteria • Hysteria2
WireGuard • AnyTLS • AmneziaWG
MASQUE • Mieru • SOCKS • HTTP
➿
➿
➿
➿
➿
➿
➿
➿
➿
🌐
Aether / WARP
پشتیبانی از پروفایل‌های Aether و قابلیت‌هایی مثل:
• WireGuard / MASQUE
• ECH و Fragmentation
• Endpoint Scanner
• WARP Key
• Psiphon و Tor
📊
امکانات بیشتر
• تست و مرتب‌سازی جهانی کانفیگ‌ها
• نمایش اطلاعات اتصال و مصرف ترافیک
• تشخیص کشور سرور بر اساس IP
• Backup & Restore
• Dark / Light Theme
• Logcat و ابزارهای عیب‌یابی
• تنظیمات پیشرفته Core و شبکه
➿
➿
➿
➿
➿
➿
➿
➿
➿
😎
Open Source • Android
👩‍💻
GitHub:
https://github.com/ArasTey/ArasClient
🖼️
Telegram :
https://t.me/imArasTey
📥
Releases:
https://github.com/ArasTey/ArasClient/releases</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1893" target="_blank">📅 17:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1892">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مشکل ربات
@WhiteDNS_installer_bot
حل شد
با این ربات میتتونید ازطریق تلگرام روی سرور خودتون MasterDNS نصب و سرور خدتون رو مدیریت کنید.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1892" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1891">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASwhOs4B7FKxg_mFkepoaZRbLU_e5K9J5dZ6hGZnBsaMU5PMPYaFA_dhRe7F582zIs3gKfC5pUuEUFxEfLA3GGVfRjbILoDYyoOvVKNGX8D_guFsENJjVVRAZq6ufU22x-S23lWa_mmVMiEpqUJ_bIr5yMEYd9nsdBGAZjEe35bCrW141-MFIQ-oaI9hJGOq9MZduAB9iFKjmGMqUSaPs-bsC7MIhZGoy2hdpXmzBq-q85yj7NfqYPWLI84BiR9v3rb4ox8WygNGIAyS3k6eIbNgF91KBBQrs_RVzu3SgxIEFl91ZvT5AGPgAipVQLqMsKdHSWaTmSK-D308XB4r5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
آموزش جدید رسید!
🥹
✨
اسکن آیپی تمیز با WhiteDNS Scanner و استفاده ازش توی کانفیگ
🔥
💗
از نصب اپ تا تست نهایی، همه‌چیز مرحله‌به‌مرحله توی ویدیو هست
🎀
🎬
ببینینش:
https://youtu.be/GDo6p_z3CAw
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1891" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1889">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوست عزیز :
خرید ، فروش ، درخواست خرید ، آگهی فروش هر چیزی که توش پول رد و بدل بشه ممنوعه
🚫
بلافاصله بن میشید</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/1889" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1888">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1888" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1887">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/1887" target="_blank">📅 13:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1886">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1886" target="_blank">📅 13:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1883">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1883" target="_blank">📅 13:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1882">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel WispByte.rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1882" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1881">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vifvP2JrOZCr_FokCtzkBg2rXmCWMPfQAz7TH3DnRBDTuknUzxOdLGjsji5RVdHN7irbHMEYrKpgk1nGxdRAo8IZXJwXd0geSdDYecsG4RYFBxZJSTMYHlHPi8ldqJJ680HnVxurmhrRVHMZqMhNf-kfyzMMC-ub8u1_xzkMJ3SW89lyQAKsoFlsNeiIKynA0ZiuTiHzfbpDNSWPcGAar5AgawoP8twHIbcQoUlgC-Yp5J2DBh06lF7EOxe2hkYF3FLTi_azKnP_EJ4q098pc094EeyNDCPAuHKkXcDxyOUlWHZReRH4oV7UTYNWC4pYkVF5E7bkPrjBo374XL5Eng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎀
بچه‌هااا یه آموزش خفن و کاربردی جدید دارم براتون!
🥹
💗
می‌خواین هاست رایگان بسازین و ازش کانفیگ V2Ray رایگان بگیرین؟
👀
✨
توی این ویدیو با Blue Knight Panel همه‌چیز رو از صفر باهم ساختیم و آخرش هم کانفیگ رو تست کردیم
😍
🔥
اگه این چیزا برات جالبه، حتماً یه سر به ویدیو بزن؛ قول میدم ارزش دیدن داره
🫶🏻
🎬
ویدیوی جدید رو ببین:
https://youtu.be/TmHM_yBPOUU
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/whitedns/1881" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1880">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">💬
تعدادی سرور اختصاصی جدید اضافه شد!
دوستان عزیز، برای استفاده از سرورهای جدید، لطفاً از مسیر زیر سابسکریپشن اختصاصی رو تازه‌سازی کنید:
✨
بخش سابسکریپشن
✨
سابسکریپشن اختصاصی
✨
دکمهٔ تازه‌سازی
🔄
فکر می‌کنیم ظرفیت فعلی برای همهٔ کاربران کافی باشه، ولی اگر نیاز به ظرفیت بیشتری باشه، حتماً سرورهای بیشتری اضافه می‌کنیم.
آی‌پی‌های این سرورها اختصاصی هستن و انتظار داریم باهاشون بتونید به‌راحتی به شبکه‌های اجتماعی و تمام ابزارهای هوش مصنوعی دسترسی داشته باشید
❤️</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/whitedns/1880" target="_blank">📅 11:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1879">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-poll">
<h4>📊 الان با چی وصلین ؟</h4>
<ul>
<li>✓ whitevpn</li>
<li>✓ whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1879" target="_blank">📅 11:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1878">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
۵۰ سرور اختصاصی اضافه شد!
دوستان عزیز، لطفاً تست کنید و نتیجه رو به من بگید. موقع فرستادن نتیجه، اسم اپراتورتون رو هم بنویسید تا بهتر بتونیم وضعیت اتصال رو بررسی کنیم
🙏</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/whitedns/1878" target="_blank">📅 07:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1877">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌎
سرور IPهای اختصاصی ری‌استارت شدن
🔭
برای دریافت آخرین تغییرات، برید به:
سابسکریپشن ← سرور اختصاصی ← دکمه تازه‌سازی
بعد از به‌روزرسانی، دوباره وصل بشید.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/1877" target="_blank">📅 03:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1875">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚠️
دوستانی که از نرم افزار whiteasther استفاده میکنند و مشکل ورود به وبسایت ها و یا سرویس های  تحریمی دارند
:
🔥
با یک سری تغییرات که روی سرور exit chain  یا همان زنجیره خروج  دادیم . احتمالا مشکل خیلی از دوستان حل خواهد شد
🛠
برای این منظور کارهای زیر را انجام دهید :
1. وارد ربات
@WhiteDnsChainbot
شوید و کانفیگ(های) مورد نظر خود را انتخاب و دریافت کنید
📥
2.در تنظیمات اپ whiteaesther به مسیرها-زنجیره خروج و در نسخه دسکتاپ به قسمت پیشرفته - زنجیره خروج  بروید و ادرس ساب خودتون را وارد کنید
⚙️
3.کانکت شوید
🚀
موفق باشید
🙏
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/1875" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1874">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1874" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1873">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">💬
با از کار افتادن سرویس های BPB فشار بیشتری روی سرور های اختصاصی هستش (شاید براتون کار کنه و شاید درست بشه).
ما سعی میکنیم کیفیت سرویس های عمومی رو بیشتر مدیریت کنیم و از شما هم میخوام اگر مایل هستید به ما کمک کنید.
❤️
تنها راه کمک به ما سرویس Patreon هستش و فقط برای ساکنین خارج از ایران قابل دسترسی هستش.
🗺
امروز به ما ماهی ۲۲دلار بهمون کمک میشه اما ماه ها بوده که هزینه های ما بیشتر از ۱۰برابر این هستشو همش از هزینه شخصی پرداخت شده و تا جایی که بتونیم ادامه میدیم.
https://www.patreon.com/cw/WhiteDNS
یک سرور آمریکا
🇺🇲
جدید اضافه کردیم و سرور هایی که براتون کار نمیکرد رو حذف کردیم.
برای دسترسی به سرور جدید، به بخش سابسکریپشن برید و ساب اختصاصی رو بروزرسانس کنید.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1873" target="_blank">📅 13:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1872">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👀
یه تغییر آزمایشی روی
سرورهای اختصاصی
دادیم
فعلاً تعداد سرورها به
۴ سرور
در این کشورها کاهش پیدا کرده:
🇺🇸
آمریکا |
🇸🇬
سنگاپور |
🇫🇮
فنلاند |
🇩🇪
آلمان
آی‌پی این سرورها
هر ۲۴ ساعت یک‌بار تغییر می‌کنه
تا احتمال فیلتر شدن کمتر بشه.
قبل از تست، حتماً اشتراک رو به‌روزرسانی کنید:
بخش اشتراک‌ها → اشتراک اختصاصی → گزینه «تازه سازی»
بعد از به‌روزرسانی، سرورها رو تست کنید و نتیجه رو بهمون بگید
🙌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1872" target="_blank">📅 06:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستان سلام :
ما برای کانفیگ whitedns ربات داریم
@MasterDnsManager_bot
این کانفیگ ها یک روزه هست ، با حجم محدود
⚠️
به درد افرادی میخوره که هیچی براشون کار نمیده و با یک سرعت خیلی خیلی پایین فقط می‌خوان یک وبسایت چک کنند و یا تلگرام اخبار بخوانند و یا پیام متنی بدهند
این روش سرعتش در بهترین حالت ممکن شاید به ۵۰۰ کیلوبایت برسه
عده ای از دوستان درخواست میفرستند که برای روز مبادا می‌خوایم ، که درخواست رد میشه ، توضیح دادیم که دوستان دلخور نشن
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1870" target="_blank">📅 14:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1869">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BAzDMG3cBtxoIsY8rC9R6oB7wAv_qiojCEayC_JVWO4T9g0jXCON14zvSvaCiBfE6pXCzGTA84Xy30GCR3udRLlwmsmsfygTmhPeQRhVK1gHar8m_XRlH4-eHzxVs6CIceEDr8BU5SS8uWT2pDwhphyOR8oUvYYI3X0fh3la7oNJznb9VZLim9U56WllRziGxu_83et0OtJCLXS3_kIXnm4oHZFbMOTD3muZrk3-re_J-gv8RKoPDzb8zoE8zl21sdguTLdXIHrPC1m_q4QonmBVb8TJ5Biba7yM961BOnIxXwito1JCBogVa4sxrkhREiz5MotgFwLZTw0a83OD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه پایان فعالیت ربات
@WhiteDnsResponder_bot
کاربران و همراهان عزیز،
به اطلاع می‌رسانیم که فعالیت این ربات و خدمات مرتبط با آن از امروز به‌طور کامل متوقف می‌شود و پس از این، هیچ‌گونه سرویس، پاسخ‌گویی یا پشتیبانی از طریق این ربات ارائه نخواهد شد.
از اعتماد، همراهی و بازخوردهای ارزشمند شما در تمام این مدت صمیمانه سپاسگزاریم. حضور شما نقش مهمی در مسیر فعالیت این پروژه داشت.
با آرزوی بهترین‌ها برای همه شما
🌹
تیم WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1869" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1868">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مهم "
⚠️
⚠️
⚠️
📢
راهنمای تست اتصال WhiteVPN نسخه 1.6.10
لاگ‌های ارسال‌شده از چند دستگاه، نسخهٔ مختلف اندروید، وای‌فای و اینترنت همراه بررسی شدند. در بسیاری از موارد، کاربران فقط چند ثانیه بعد از زدن دکمهٔ اتصال، آن را دستی قطع کرده‌اند؛ درحالی‌که برنامه هنوز مشغول بررسی سرورها بوده است.
در نسخهٔ 1.6.10 برنامه ابتدا سرورهای اختصاصی را آزمایش می‌کند و اگر آن‌ها پاسخ ندهند، سراغ مسیرهای جایگزین می‌رود. این فرایند در شرایط فعلی اینترنت ایران ممکن است
تا دو یا سه دقیقه
طول بکشد.
لطفاً برای تست دقیق، مراحل زیر را به‌ترتیب انجام دهید:
مطمئن شوید نسخهٔ نصب‌شده
WhiteVPN 1.6.10 (85)
است.
وارد تنظیمات برنامه شوید و گزینهٔ
تعمیر اتصال / Repair connection
را اجرا کنید.
بخش
Split Tunneling
را موقتاً خاموش کنید.
در بخش انتخاب موقعیت، گزینهٔ
Automatic / خودکار
را انتخاب کنید.
اگر امکان انتخاب سابسکریپشن دارید، فعلاً
سابسکریپشن عمومی WhiteDNS
را انتخاب کنید.
دکمهٔ اتصال را بزنید و تا
سه دقیقه کامل
برنامه را قطع نکنید.
هنگام اتصال، بین وای‌فای و اینترنت همراه جابه‌جا نشوید و برنامه را از Recent Apps نبندید.
اگر پیام «متصل» نمایش داده شد، حداقل ۳۰ ثانیه صبر کنید و سپس موارد زیر را آزمایش کنید:
بازکردن یک سایت در مرورگر
ارسال یک پیام در تلگرام
بازکردن یک سایت خارجی دیگر
⚠️
اگر برنامه متصل شد ولی اینترنت یا تلگرام کار نکرد:
لطفاً اتصال را بلافاصله قطع نکنید. در همان وضعیت متصل:
اگر برنامه «متصل» شد ولی اینترنت کار نکرد، اتصال را قطع نکنید. در همان وضعیت، از همان گزینه‌ای که قبلاً برای
کپی و ارسال گزارش اتصال
استفاده کرده‌اید، لاگ را کپی و برای ما ارسال کنید. سپس نوع اینترنت، نام اپراتور، مدل گوشی، نسخهٔ اندروید و اینکه سابسکریپشن خصوصی یا عمومی انتخاب شده را بنویسید.
آیا هیچ سایتی باز نمی‌شود یا فقط تلگرام مشکل دارد؟
آیا حالت Always-on VPN یا «مسدودکردن اتصال بدون VPN» فعال است؟
اتصال با سابسکریپشن خصوصی انجام شده یا عمومی؟
اگر برنامه بیشتر از سه دقیقه روی «در حال اتصال» ماند، باز هم ابتدا گزارش را کپی کنید و سپس اتصال را قطع کنید. گزارش‌هایی که بعد از قطع اتصال گرفته می‌شوند ممکن است بخشی از اطلاعات اصلی خطا را نداشته باشند.
بررسی‌های فعلی نشان می‌دهد تعدادی از مسیرهای اختصاصی
AnyTLS
داخل ایران پاسخ پایدار ندارند. در چند آزمایش، سرورهای اختصاصی شکست خورده‌اند ولی برنامه پس از انتقال به سابسکریپشن عمومی با موفقیت متصل شده است. به همین دلیل تا زمان اصلاح مسیرهای اختصاصی، استفاده از
سابسکریپشن عمومی
پیشنهاد می‌شود.
همچنین اگر از نسخهٔ 1.6.9 استفاده می‌کنید و برنامه «متصل» نشان می‌دهد ولی دیتا ردوبدل نمی‌شود، حتماً به نسخهٔ
1.6.10
به‌روزرسانی کنید. نسخهٔ 1.6.9 در بعضی شرایط ممکن بود اتصال ناموفق را به‌اشتباه متصل نمایش دهد.
از ارسال گزارش‌های دقیق شما ممنونیم. این گزارش‌ها مستقیماً برای شناسایی اپراتورها و مسیرهای مسدودشده استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1868" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1866">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚠️
🔥
تعدادی از دوستان به خاطر فیلترینگ شدید توی منطقه ای که زندگی میکنند توی نسخه 1.6.9 دچار مشکل شده بودند .
کانکشن برقرار میشد ولی ترافیک نداشتند .توی نسخه 1.6.10 این مشکل به طور کامل رفع شده است و احتمالا خیلی از کاربران مثل نسخه های گذشته به راحتی متصل خواهند شد
دوستان تا ما مشکل سرورهای اختصاصی را حل کنیم فعلا از سرورهای عمومی استفاده کنید
⚠️
دوستان چنانچه هنوز برای اتصال مشکل دارید لطفا با نگه داشتن انگشتتون روی دکمه اتصال لاگ برنامه را کپی و برای ایدی ادمین که توی بایو هست بفرستید
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/whitedns/1866" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1863">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1863" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/whitedns/1863" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1862">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YGJyBk472x3H72G5AsW-cGbkYdA89dn0ZQ1Qi1QG4FH_h9PHcWYT_bJD950reylfikjEkG_8vKAc6XdiNxe4dvP8H_XYZ8OIib-TxKkq_mHBzwT7zOlFomuQq8BJNFf28smmWZzhW2uC8zI4TAVd_hIs0JVCFS4OBHEoscRlpb1FiYKqda6OJuIc5p6yB_b3tOgWBINCPPTdfLo4SdfD9vvS46ILsMfh_gdXkkCqPNLngA_ZG_UDea63zjzq_D_oQU5cTSPEKhF5xT6SjM7X88dVR07yoY-qRT23A7sDS3jkTLIIXQeBYuGYe6xJbh4mWuVKNeuo2V9IB8ls2tt58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/whitedns/1862" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1860">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/itp1UvP3OEtOX0RCafuowERkIAwWXaXne1E8Q_udS7P2AvH-tw08TjLfi-p25EkrLui5ixesfhY5MOO8XL1FhwgA2lClQgvHAqIongFTc8T_0OSwKfLkYL1W4ODEKZrTZkapOneISGWdhA58X-m6TkCJP04S40YCUwDiM5xhzJKXFxvC_EgecY4iYC8wMXOaOBtYoEeeyT1ih-4s-v9WUQkyWw1SkrWhYWllTSC0wGKKzExnteEJBfI0Q_OwjKOizJEAns7MtesVFVxWRQMSl9r0SEmUSSUypN5o91M9JYvkmc5TYgKaQYuBxfiTScKgV5EKsA3R821GCsoW_hhp8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1860" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1855">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.10.0-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/whitedns/1855" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1854">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fhGeM2O0BRK2yNUDsfVrpnzipV_frUPa1pXE8QcTcKXavL6FWh8zxuqOiZ7FV_38GzoeEmIF6PUbBn9DtOJDizpU3JrgnpcogQ3L2VkiAFX32OsLATCg8FjRZQ7AYw2x7Sn9lWBxC4qJHyuZM3wVmStFk72ILfhjHwBNqmZKEc5KdBr07nvo90HggCc_iRz7wAJ9Wn8tiq5niD5tcVKTl_pm1jBNKHASv56tJ07UKbEv5wNEvZkoJniX0sJy8CFV86zN1O0TAEyYax9_NjQaz4dATUNvkZbu_Pc0uAYiykmkQ49AQEjhRV7cT77IRhMJcXDhxUWjs14pqvJ9x5uVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Whiteaesther mobile v 1.10.0
حالت خودکار حالا جست‌وجوی مسیر را ادامه می‌دهد و مسیر موفق هر شبکه را به خاطر می‌سپارد
🧠
پایداری اتصال بهتر شده و سرعت دانلود و آپلود در اعلان برنامه دیده می‌شود.
📶
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.10.0
@whitedns</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1854" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-poll">
<h4>📊 الان با چی وصل هستید ؟</h4>
<ul>
<li>✓ اخرین نسخه whitevpn</li>
<li>✓ اخرین نسخه whiteaesther</li>
<li>✓ اخرین نسخه whitedns/coreforge</li>
<li>✓ هیچ کدام</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/1852" target="_blank">📅 18:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آمار اتصال ها داره برمیگرده به حالت عادی
❤️</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1851" target="_blank">📅 13:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1850">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.  لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید.…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/1850" target="_blank">📅 12:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFVwFGrXs_AnxX8xRDT-lhXy47oCQijkHbcTuYqaQcREPP6oYWSNVT19_NyVh4RA9IQfzsvFUREiDDcmLiIOesNMGFwHkdh3AGgt-8XKDdIDwbl-yk0s0S5EkWaRmfX9h6WQOd37MpoqZ1odLvfxkn5YgaPi8u2yBm8N0CCR4OliTofGuUf4Yynoh0cdlJbsjxJ52Rs0oRth37xu7Aymrs7Fm5hifeqPz2C718X9nUXMG16CvN8mkx3h6VrP0gU4obkyvk1TibxOM-9lIpw6O-KYUI0VT7ZLKConOkhhHcIj2LtfSPUzWbXaGgE3BMJ010PWQaYl31s4Rx4-JnBavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.
لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید. نسخه جدید رو می‌تونید از صفحه GitHub ما هم دانلود کنید:
🛡
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.9
💬
بعد از نصب نسخه جدید، اگر هنوز مشکلی داشتید لطفاً بهمون خبر بدید. گزارش‌هاتون کمک می‌کنه مشکل‌های باقی‌مونده رو دقیق‌تر پیدا کنیم.
ممنون که با گزارش‌هاتون کمکمون می‌کنید
🤍</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/1848" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EsRQuzgNV1TDW0QJ3GIOXWhqKnPBdh9GH7NTebB7K8iIOFtE_uUqsFsJbEb6IshEaDxtOIJD97JDLPDBGkd8Q2QaBerlKGxv6rN_yDRMOZmJ-9kVxZ_NZ5lf4PwWsFpEHXJHrTCBz71Grm-NK2RAnfYoM4HpprqITPI8cz7ugVV1dOTKL84lZeYrVAcbkoNH52BuhGaitI3bbJ8wY3ydQ2a7e-WjocefNEJOXHqqdXewPOZlkaUOlS2N99lwKxIbtyovIfB44Wt6qGx-r-k6BSQ-VtRlcjWVI_WHuY2WMYO6-2JcBpG1WgMZiYpTBpTYG_G0tIgZWha2oOqHg5Svzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی whiteaesther desktop 1.9.7 pre-release
⚡️
اتصال باید خیلی سریع‌تر شود
کلادفلر در همان جواب ثبت‌نام، آدرس دقیقی را که به دستگاه شما داده اعلام می‌کند. موتور آن را می‌خواند، ذخیره می‌کرد، و بعد نادیده می‌گرفت — و به‌جایش حدود ۲۵۰۰ آدرس را یکی‌یکی امتحان می‌کرد تا یکی جواب بدهد.
🔑
و مشکل «دیگر نمی‌توانم ثبت‌نام کنم»
اگر تا حالا پیش آمده که بعد از چند بار نصب مجدد یا اتصال ناموفق، برنامه اصلاً نتوانسته شناسه بگیرد — این همان بود.
ثبت‌نام همان لحظه‌ای که سرور جواب می‌داد خرج می‌شد، ولی تا چند مرحله بعد روی دیسک ذخیره نمی‌شد. اگر وسطش چیزی قطع می‌شد، ثبت‌نام رفته بود ولی شمرده شده بود. و چون سهمیهٔ کلادفلر روی آی‌پی است، همین می‌توانست گوشی روی همان وای‌فای را هم از کار بیندازد.
حالا اول ذخیره می‌شود، بعد بقیهٔ کارها.
🛡
و یک حالت خراب که دیگر ممکن نیست
قبلاً اگر با وایرگارد وصل بودید و MASQUE را امتحان می‌کردید، هیچ‌کدام دیگر کار نمی‌کرد. ساختار جدید طوری است که این وضعیت اصلاً قابل ساختن نیست.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.7
⚠️
نسخهٔ آزمایشی است — در فهرست به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد.
شناسهٔ فعلی‌تان خودش منتقل می‌شود؛ کاری لازم نیست بکنید و چیزی پاک نمی‌شود.
💬
اگر اتصال سریع‌تر نشد، یا هر چیز عجیبی دیدید، بگویید.
@whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1847" target="_blank">📅 12:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/l7HfABnj4jnTORKLUfWfo5T0871Ow-IWryZFHDGF-b-kz3BE2PnwD2OWFh9IRhlg2tkON12voysFfjQqcxILgvsUo7YP0iVy5uWPC3-Ab1Yl-Ptp9-gvdr9LRyYonOTbpSPlJDh21PRj7bVrw1EBSoHn_GsAp5p59HJ2qrGr4J1dytKtbTL1q_jRrfhXq9HJQCTpEp1ZKDUvVUC8jXnOx6L0BWKdCKgwWpMaxWt3yoTPuvGRmQ7QcF6EN962AYHmpsBRe3qc59NBICpUOY_fNZTQADNsATAl09AquBYCDhyNneArB9IhO6Tw93ll3TjA6DoU7FrGyapNCcvrKxxJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/NdPgztLR_NwBs_WgpYyZnkhcGnYGpj4fgqVysumT_nF3ytt58LWzm85e_1rvWBxoVQIN_9Cli-r6YQt3T7AESvyhuUWg2a5uMKeY7fNFmZTQFheWGihKlflB2wxrKPyyHYIyaXhxJMzqa_m0y-EWJ0-wCA1epDIn5jO4ppBuyoFvLpYRn6wpLxQ6UNFnTzjK7p2wtaUZjAdA_av1eTdw7APChHZLUjYLe2pQ_HhtzNkJ8m6kSXZQuDswDPQoFhJ8gOZI748YjNmxLGu4EA94ckH-nfZ89hO3YB58Spg8DWHb2V7mXargaTNM6qTvWh_0fqcjUrLs9FHg16yXItE8yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚠️
یک امکانی که توی اخرین نسخه ازمایشی whiteaesther موبایل و دسکتاپ تقویت و بهینه سازی شد - امکان ست کردن dns بود که تقریبا هیچ کس بهش توجه نکرد جز یک گروه خیلی کوچک به نام گیمرهای عزیز
😁
😃
از این امکان استفاده کنید حتما خیلی از مشکلات شما را حل میکنه
🤓
لیست dns های عمومی :
۱. DNSهای عمومی و معمولی
Google
8.8.8.8
8.8.4.4
Cloudflare
1.1.1.1
1.0.0.1
Yandex
77.88.8.8
77.88.8.1
Quad9
9.9.9.9
149.112.112.112
OpenDNS
208.67.222.222
208.67.220.220
AdGuard Unfiltered
94.140.14.140
94.140.14.141
Control D
76.76.2.0
76.76.10.0
DNS.WATCH
84.200.69.80
84.200.70.40
DNS.SB
185.222.222.222
45.11.45.11
AliDNS
223.5.5.5
223.6.6.6
DNSPod
119.29.29.29
—
Hurricane Electric
74.82.42.42
—
Comodo Secure DNS
8.26.56.26
8.20.247.20
Neustar UltraDNS
156.154.70.1
156.154.71.1
LibreDNS
88.198.92.222
—
360 Secure DNS
101.226.4.6
218.30.118.6
OneDNS
117.50.10.10
52.80.52.52
Quad9 Unfiltered
9.9.9.10
149.112.112.10
DNS4EU Unfiltered
86.54.11.100
86.54.11.200
۲. DNSهای امنیتی، ضدتبلیغات و خانوادگی
Yandex Family
77.88.8.7
77.88.8.3
Cloudflare Security
1.1.1.2
1.0.0.2
Cloudflare Family
1.1.1.3
1.0.0.3
AdGuard Default
94.140.14.14
94.140.15.15
AdGuard Family
94.140.14.15
94.140.15.16
OpenDNS FamilyShield
208.67.222.123
208.67.220.123
CleanBrowsing Security
185.228.168.9
185.228.169.9
CleanBrowsing Adult
185.228.168.10
185.228.169.11
CleanBrowsing Family
185.228.168.168
185.228.169.168
Control D Malware
76.76.2.1
76.76.10.1
Control D Ads
76.76.2.2
76.76.10.2
Control D Family
76.76.2.4
76.76.10.4
DNS4EU Protective
86.54.11.1
86.54.11.201
۳. DNSهای رمزگذاری‌شده (DoH و DoT)
Google
https://dns.google/dns-query
Cloudflare
https://cloudflare-dns.com/dns-query
Quad9
https://dns.quad9.net/dns-query
AdGuard
https://dns.adguard-dns.com/dns-query
Control D
https://freedns.controld.com/p0
NextDNS
https://dns.nextdns.io
Mullvad
https://dns.mullvad.net/dns-query
DNS.SB
https://doh.dns.sb/dns-query
AliDNS
https://dns.alidns.com/dns-query
DNSPod
https://dns.pub/dns-query
OpenDNS
https://doh.opendns.com/dns-query</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1845" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1844">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">💬
کاربران WhiteVPN روی اندروید
اگر اخیراً داخل برنامه با مشکل اتصال یا اختلال مواجه شدید، لطفاً برای کمک به تست و بررسی مشکل این مراحل رو انجام بدید:
1. ابتدا گوشی رو یک‌بار
Restart
کنید.
2. وارد تنظیمات گوشی بشید و برای WhiteVPN گزینه
Force Stop / توقف اجباری
رو بزنید.
3. سپس
Clear Data / پاک کردن داده‌های برنامه
رو انجام بدید.
4. برنامه رو دوباره باز کنید و اتصال رو تست کنید.
در اکثر موارد بعد از انجام این مراحل مشکل برطرف میشه.
اگر بعد از انجام این مراحل همچنان مشکل داشتید، لطفاً نتیجه رو به ما گزارش بدید تا بتونیم دقیق‌تر بررسی کنیم.
ممنون که با تست و گزارش‌هاتون به بهتر شدن WhiteVPN کمک می‌کنید
🤍</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1844" target="_blank">📅 09:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1843">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hlPQ1oNyKwg_dZQzhaLGdXeh_hRzPH60kW8lPSlNst27KICrmms_0GzjNYBZ4yDqT3cq6H3Au8ArTzQL4YTn4HAwdII4JbTesWozV6k1mjFCnIaP0TGndQsDlMpEE8w-jHeYK9NrTZrKsu5nUmw4Zcv3HJRORk5BtNNxksGUNJ9MaCdplAqhU7LwguDqadOc7MPqCMBfnyn4slJwrVp1BKqKPhFrsdby1C-oByZEPUeqFo0Uw2piXws6MNsLP48F2S2i3nHGDxQDktt9Y_miaypg1TrUze3jLT2oRjMPtRJaSGZk0eykzQDP6Y6rdukbLXgMliWigg9cUl9DRqMu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ازمایشی whitevpn desktop1.0.23 pre-release
🧪
این نسخه آزمایشی است، نه انتشار رسمی. برنامه خودش آن را پیشنهاد نمی‌دهد. اگر نسخه پایدار می‌خواهید، روی ۱.۰.۲۲ بمانید.
چه چیزی تازه است:
- فایل نصبی
.msi
برای ویندوز — نصب در Program Files، میانبر منوی Start، و حذف از تنظیمات ویندوز. نسخه zip هم هست.
📦
- گزینه «همه سرورها» — اگر چند سابسکریپشن دارید، از میان سرورهای همه آن‌ها انتخاب می‌کند.
🌐
- پروکسی سیستم و حالت تونل حالا در منوی آیکون کنار ساعت هستند.
⏰
بیشتر از همه به تست فایل نصبی نیاز داریم، چون اولین بار است ساخته می‌شود. اگر ۱.۰.۲۲ را دارید، این را رویش نصب کنید و ببینید درست جایگزین می‌شود.
اگر مشکلی دیدید گزارش بدهید — اگر بتوانید محتوای صفحه Logs را هم بفرستید کمک بزرگی است.
📝
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.23-rc1
@whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1843" target="_blank">📅 06:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-poll">
<h4>📊 خیلی از دوستان میگن الان یکی دو روزه اختلال شدید دارند و برنامه های white براشون کار نمیکنه . شما چطور؟</h4>
<ul>
<li>✓ هیچی کار نمیکنه</li>
<li>✓ همه کار میکنند</li>
<li>✓ فقط whitevpn کار میکنه</li>
<li>✓ فقط whiteaesther کار میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1839" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1838">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E4x_uXE0SvnkYmIuf3te7IKAk9TkqA7-M1l5YAj4CP0-MhxdxNBzQm9KSiGqjGwYkcB5mKqCaibqvX_X-L2eoCUbCGBe-F_cJv3OMYb9TQsZaAIuYL_aa408DU0_6s6VHw87yxIXHDCnJdyLa4VEPt1cKcMRlWCs_4aSb93-R3q50OEB5VAyXVTRAqtf0DmWJPVw8lPElbN_4P2N8KxvrN8Vhr2P1h_i_LSjxzKgcB5hLpFuO_sx0t-qqHj-R89ZUkOLNjM1TJv6XBcRF1A01Fkb_c1xiqw7b0zn7V23qYA7TR_dtXNSuaPnJgTuUBBcQNpYU8nWTGNfWLRWT-kC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther mobile V1.9.4
pre-release
الان DNS inside the tunnel روی همه حالت ها اعمال میشود - قبلا این امکان فقط برای حالت proxy بود.
🌐
چی درست شد
▫️
فیلد «DNS inside the tunnel» بالاخره کار می‌کند.
✅
تا حالا هر چی وارد می‌کردید نادیده گرفته می‌شد و همیشه از
1.1.1.1
استفاده می‌شد. اگه با سایت‌های تست DNS چک کرده بودید و جواب عوض نمی‌شد، دلیلش همین بود.
اگه خالی بگذارید مثل قبل
1.1.1.1
می‌ماند. در حالت chain اعمال نمی‌شود، چون آنجا نام‌ها رمزگذاری‌شده و از سمت خروجی پرسیده می‌شوند.
🔒
و بهینه سازی موتور و routing , ......................
نصب:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.4
@whitedns</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1838" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1837">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VqbiL2_xVhzvSIuUsYbxdCyXO-oIha5jNoBE8GY9_SG2m4ZmlgpG_MXVFcTkmmpgZQM4aCW-Tc5-NoHx9uviY86bjFSlTktZsajlhe2fywclruXpJlO34Uu8kpPDzDCT6678xWOPkbdK0bzFy1a9atRnCJOnwU9nUt-zoW4mxURBWyFFHuh3ZMyhF6F9H6FqIiLmNfRQdbdEAXwuqkTm0ZfW7wtlDi4H5VVWqm55au1jYaFVMNOgog6o7BySgqGTNbQhiWtZePDJu1OuuVRJT3KoX3fp7PCa207hMDgbYVRpBaEDtVYvncdTLCXdqrB8fo4b0vRDD2JExYbR9FHozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ آزمایشی whiteaesther desktop 1.9.5  — رفع باگ پورت و یک سری بهینه‌سازی روی موتور و .........
🚀
اگر بعد از هر بار اتصال، پورت پراکسی محلی عوض می‌شد و تنظیماتتان به هم می‌ریخت، این نسخه همان را درست می‌کند.
✅
پورت دوباره ۱۸۱۹ می‌ماند — هر کریری که وصل شود.
🔒
این باگ از نسخهٔ ۱.۹.۲ به بعد دیده می‌شد، از وقتی دکمهٔ اتصال شروع کرد خودش راه خروج را پیدا کند و سایفون یا تور بیشتر برنده می‌شدند.
🕵️‍♂️
📥
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.5
⚠️
نسخهٔ آزمایشی است — در فهرست دانلودها به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد. با همین لینک بگیریدش.
اگر پورت باز هم جابه‌جا شد، حتماً بگویید.
📢
@whitedns</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1837" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1836">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه WhiteGame یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1836" target="_blank">📅 09:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1835">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfmZgojFrBSLtE_fJby7BfEj3toU3pcJHpAsyf_lDKJUggckocHVywMLOiw4iYnu84DxFRMeKjyYCi3P8aGWxAcOMEH-qpdzR_eElvojb1ZWHtBzvrSKeVaeHuzAURNz13IW-Kzj4kRDlQVPUlmhfD6lrPD91Yj-2w4EosJMzmMvg6zoQhbz3xcngjLe16vnXbOU1QszxOyp2jyVMadB-e2miQRVb6JclTgSiDCUgIuEmP0t6f4SnUDT1Mbi3qCGbb7YK4mp5v55IGlhTL2kCbf0MEvejTD58cgNAB7xY4tSILID4b65fx7XtBra5XxQWSWcXQNEsBcobYkzr9wJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه
WhiteGame
یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور ویژه برای بهینه‌سازی پینگ، سنجش کیفیت اتصال (QoS) و رفع چالش‌ها و محدودیت‌های ارتباط با سرورهای بازی طراحی شده است.
📊
این ابزار با شبیه‌سازی پروپ‌های شبکه‌ای و سنجش شاخص‌های کلیدی و نوسانات پکت‌ها تحت وب، به گیمرها این امکان را می‌دهد که وضعیت زیرساخت اتصال خود را پیش از ورود به بازی ارزیابی کنند. جای دارد گفته شود که تمرکز ما روی
UDP
است، همچنین قابلیت
Test Real Path
در اپلیکیشن، پینگ واقعی و دقیق شما را در زمان Matchmaking و InGame نمایش می‌دهد .
🔐
پروتکل‌های پشتیبانی‌شده:
Warp | WireGuard | Amnezia | Xray
✨
ویژگی‌های برجسته:
• Packet Loss Injector
• Jitter Plus
• Gaming DNS Spy
• Optimizer Warp و WireGuard
⚙️
علاوه بر این، ابزارهایی برای ساخت و مدیریت کانفیگ در اختیار شماست؛ با استفاده از بخش Generation برنامه، تنها کافی است Public Key سرور خود را قرار دهید تا خروجی موردنظر به‌صورت خودکار تولید شود .
📉
همچنین در مرحله تست آزمایشی (Beta)، حدود ۳۰۰ نفر از کاربران با استفاده از ترکیب Warp و پنل BpB توانستند میزان Packet Loss خود را در شرایط ناپایدار کنونی به نزدیک ۰٪ برسانند.
🤝
امیدواریم با بازخوردها و پیشنهادات شما، این پروژه را روزبه‌روز بهبود ببخشیم.
https://github.com/TaJirax/WhiteGame
@Whitedns</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/whitedns/1835" target="_blank">📅 06:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1834">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cC42dPIM0nWCfvaNgPD2FCOzf6Faw2oOzj9pSaAOgNWL_3N0Z9jkAfQLSUdtBKASgDAS-wZsRn3_Zy-jhUJPlWUXZXqb0xTWbLrfoGLH9eWw69gjUtJn75aWB3XW3T-eRUMMQREvosA_Q3bf0mzf5CXM7-PpO3yuJ-DEZNBeXRjo8VEWQilq83Ircs5C7t5_4srss4sqHC__T1Hfc5YfF4JPOq_WyHxctoY0maa9RXDqPu9Ju7-E3eFtynjo1tXbr3U3GBPMcJpO3wJ_EomsVsEOUv6r1fNyLHu5Kv0udSYKyX0ohWyGUrG42MXtRO_74u-vVnF31NcCX0PfDNNqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا در گروه whitedns عضو بشید
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1834" target="_blank">📅 20:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/N_0X-dyg54dLz-C1TREAWFudYGbfTpcQ_KOGBM8wIxb0NvCuVj-tFjHazwGktneAB_WD5wmrjSBoauQ_Jjt7Gp2e6P1UZZX4jriktEkWF9_0LlwUDhCJyf7iDd4LnUSLCiYgbK9Rha9htxSuiyFsz-BsDlvUtEQ75Dqiz2vbos4iLst_HP0T9c2b49dy3CyIaWuD6BzYtVCSkq-_kFbMM2dbz3PCJfzEI2FC0Un5zQC2ykqPAXxCMfhw0BXSsdIh5OdcBR8nQNfsqQ5GNkXPLz_NQ58IHnwsUVTOmTUOQw2_ii6eXIav3PKkt93RJwp25w7Wgf1y9Nv-eINRvrOsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1833" target="_blank">📅 17:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1830">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel (Orihost).rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1830" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1829">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqW78ELRY_3ne-RjmcRqL54LPKPN89j-HoEQxYfXLsVVkkdfgBGrGSRy5IpEN9iqVyAzUkdycAcJtzoqSNBH2oixsP2bQ1E8jB6JIK7HNmHEuf2vAa-A651WhEtwtt0HVad2XKXw1psQlXucBjuIVKVF_AqQNo_cRgHOOggWq7_OOruNAPiWs0DmJNqGQeNul2YYlndMZgeQxJH77FnwvoMVgAm_a4B_Z1h4Y8DHON7nYuvyUqhLaEM_J-JSYWJHp_wsNOMOihblwnpirz9cBv7zBuCjczMRFbGYtVlTovCiehqu7mA5P7cggO993OO5ESkyEeLz4OhgISp7lVDeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1829" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1823">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.9.3-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/1823" target="_blank">📅 14:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1822">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/m0R7uP6EIqnmT-NsXuTqmHpAyD9R_40354KjIUzs8XKC5308JhEQxUPQU4WcXUuCUO_-fOTLLUpA5Dc56_kYLhw1LfPc_GboCXgkEKltc-8SojIV2U1tb49Cx9QdyQtmjr1J76gtBZMK-SgPAFvrLMoVaNvunG8lqy4RTEbsSoaaAe4oTvJu6jNGSGBPy6tbZN9IebQIzfOcMMv7xVYFWTr2x5EJyQeo4oOv9FbMQO3FuVsSr7YXsPMSUOgCpLgtCZdySNkDqXDq-yedHj3YvumUQ1V5TOlYwfMvIQgn5skQrwHJjWLYdVZJz2Upjt2SRXTdQUi90e408_DZsPWEGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
Mobile 1.9.3 — نسخه پایدار
🔥
نسخه پایدار 1.9.3 منتشر شد. برای به‌روزرسانی می‌توانید از قابلیت جدید داخل اپ استفاده کنید یا فایل را مستقیماً روی نسخه فعلی نصب کنید.
برنامه را حذف نکنید تا هویت و تنظیماتتان حفظ شوند.
قابلیت‌های جدید
آپدیت مستقیم از داخل اپ
کارت «نسخه جدید منتشر شده» حالا می‌تواند فایل به‌روزرسانی را دانلود و نصب کند.
این قابلیت فقط زمانی فعال است که:
پوشش اتصال روی «کل دستگاه» باشد.
فایل با همان کلید نسخه نصب‌شده امضا شده باشد.
ابزارک صفحه اصلی
بدون باز کردن برنامه، اتصال را برقرار یا قطع کنید. برای افزودن ابزارک، در Settings دکمه Add را بزنید.
هنگام جست‌وجوی مسیر نیز دکمه قطع اتصال در دسترس خواهد بود.
مشکلات رفع‌شده
مشکل نسخه 1.8.0 که ممکن بود برای یک هویت دو رکورد نگه دارد، برطرف شده است. اگر نصب شما در این وضعیت گیر کرده باشد، با اولین اتصال خودکار اصلاح می‌شود.
جست‌وجوی طولانی finding a working route اکنون محدودیت زمانی دارد. این فرایند قبلاً روی شبکه‌های دشوار ممکن بود تا ۲۷ دقیقه طول بکشد.
هنگام جابه‌جایی بین وای‌فای و دیتای موبایل، تونل تا جای ممکن به شبکه جدید منتقل می‌شود و از ابتدا ساخته نخواهد شد.
اتصال MASQUE in MASQUE اصلاح شده است. اگر روش اول برای هاپ داخلی پاسخ ندهد، روش دوم نیز آزمایش می‌شود.
تمام اصلاح‌های نسخه 1.8.1 نیز در این نسخه قرار دارند.
روش نصب دستی
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.3
فایل مناسب معماری گوشی را دانلود کنید.
اگر نمی‌دانید کدام فایل مناسب است، نسخه universal را بگیرید و آن را روی نسخه فعلی نصب کنید.
در صورت مشاهده مشکل، از مسیر Settings ← Diagnostics گزینه Send diagnostics را بزنید و گزارش را ارسال کنید.
⚠️
@whitedns</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/whitedns/1822" target="_blank">📅 14:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fN4YVxl_W-_iAxbbhPMxO5LeWnN9yDHMYf6DF4p0MU8ESX-du1uIGOOj8FbvCclN4feM5F_X8H8C33kX4TZmfkjXXuZI-kN1ORE10KMI9IST_AKDyY7sIgRdjsKuk6vvFz_zKcVPao1FYdLqwZ4h8bTtMZhD2-r_hPM-iaCLZH88H9svilgQFmLJDNKC2RWtNll95FPf7QgpvN0bbf0TM4a0CuY6wjykfhZnhtevIKfq-9nZE9kcooB5GzWF4WLZeaukOqYGS2g4pourqpNy40Ev6Od0iEzILvPQvI1aHLkZGcGz0nC2tfPAbrMBwn4Bl3t5nkL66PTviBCsrbECyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/whitedns/1821" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1820">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qjKk2ItFM6Z7xiFm9927bngjGcLwpbt69hltWOQ7cqNaw6xwg4ytvssCHaxOAi-F7BxTzgwFSgWUWRULBNxtpLPUtgbN-sj0cXHIsAwVfDjcsuRQFlo7UPwPW6whxb3gUDp1ODqDOQU667RuCCepaYYRBWOiChyIPQq8H3tFGvwJTgsnKxY4N9FB6z44gIes_XUDcljADejRZYFKJAmbyjz9N0bEZ47XmYkwyxStiGfw27YTJuw3aLXRlwlnHh36V91H3cZ-y0NFzTQidkPltxwsVeZdKsqHnPj7CTsQAh9EyyXm8XfghtGq2l934RfjKkG6eNv4y7-NHUNQ-FwOQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
CottenRouter v1.2.13
منتشر شد!
سریع‌تر، پایدارتر و آماده برای ترافیک سنگین
⚡️
• رفع مشکلات نصب
SlipGate
روی سرورهای تازه
• جلوگیری از Down شدن Router هنگام قطع نصب یا SSH
• رفع تداخل Domain و Port بین Backendها
• امنیت بهتر
CottenDNS
و
StormDNS
0
٪ Query Loss
در تست ۵۱۲ کلاینت همزمان
• پردازش بیش از
۲۲K Query/s
• بهبود TUI، خطاها و سیستم Purge
✅
آپدیت مستقیم بدون حذف Routeها، Backendها و تنظیمات قبلی
💻
GitHub
https://github.com/TaJirax/CottenRouter
📋
لیست کامل تغییرات
v1.2.13
https://github.com/TaJirax/CottenRouter/blob/main/docs/releases/v1.2.13.md
@whitedns</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1820" target="_blank">📅 16:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1819">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/V0Q0QdNNY7fO8xTMlnd_scilRaPQyn87LZqqoCixN1SWOTYAZc05KzoQ_3j63hIsbRqEM6pP3LX42ak2xzwjqXOUYtfICEWnpZxRDurQxTIClnpginXSR1GtLzsGmCcLItJz7sgEOyhSJOSltXPHrBwTLx9oKVGou4OhNNRL1Pb1zuHJabVN_RmhOJ4yzDHwxJFrgRjBIXcuTbxsL4gfKlGe3yh2qjwh9JnKFJnJmCGsXqyKwcSMcY_7hPstRQ_XVoQD0aUzTJkRySdIaY9KfTpjwIBZ-xrybEDJwEq9eRO1k4zAhEkrac3zAZcUJbaS6_CdxeumFKknJTJG7o2Mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whiteaesther moblie pre-release 1.8.1
⚠️
این نسخه برای کاربرانی هست که توی چند روز گذشته اختلال شدید گزارش کردند و نسخه آخر هم مشکل انها را حل نکرد
برخلاف باور غلط عمومی ورژن ها در حال بدتر شدن نیستند بلکه امکانات بیشتری در حال اضافه شدن است - اما به دلیل گستردگی کاربران ما مجبوریم حداکثر بومی سازی را انجام بدهیم که این کار گاها زمان بر خواهد بود .
اگر روی ورژن قبلی مشکلی ندارید فعلا اپدیت نکنید !!!!
⚠️
⚠️
⚠️
دو اصلاح، هر دو روی حساب زنده اندازه‌گیری شده:
MASQUE دیگر دنبال آدرس نمی‌گردد. Cloudflare در هر پاسخ ثبت‌نام آدرس اختصاصی دستگاه را می‌دهد و موتور نادیده‌اش می‌گرفت
ثبت‌نام‌های Cloudflare دیگر دور ریخته نمی‌شوند. هویت بلافاصله پس از ثبت‌نام و پیش از هر کار دیگری ذخیره می‌شود؛ مسیر مستقیم یک بار امتحان می‌شود نه پنج بار؛ و نصبی که enrolment مربوط به MASQUE کلید WireGuard‌
اش را باطل کرده بود، در اولین اتصال خودش را تعمیر می‌کند.
این نسخه به‌صورت خودکار به کسی پیشنهاد نمی‌شود.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.8.1
@whitedns</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/1819" target="_blank">📅 12:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1818">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">😎
دیگه لازم نیست برای آپدیت از اپ خارج بشید.
اپ اتوماتیک ورژن جدید رو دانلود و نصب میکنه.
این به کسایی که اطلاعات فنی هم ندارن کمک میکنه.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1818" target="_blank">📅 11:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1817">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brK22HHgPt-uCc622eEPFt89aidbQxNQnvl3lgDtRk98AMIDUAAVB5c-6L8FafYXT2-fbqP1y3Aa03q5T8avtErZtXPPCgM3dY5goaDoEZcURCcBI7yGoaQnSH9RzB2LIPlv9LBFZOeLqFZTFE50Ww_kY07JETUL5YxZN7GJ8JRcY3ioIJn1Tljt_81TZnoG0aZOJalwq60EGn_JkQ6uEsiskFpZ8qvCEr_CT_7kuyMLvnj8B8rYXBdpzgPRqdFRSQYjARPWftw3iCExtqO9NlGcl2bSrIxV4SOl9RvHS4Z04doYOt0EI5dE2oVjCykpPzn-JhXuTUK9dyFf9nkj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.8
تغییرات نسخه جدید:
🟢
ویجت صفحهٔ اصلی برای اتصال، قطع اتصال و نمایش وضعیت VPN
🟢
به‌روزرسانی از داخل برنامه، با نمایش پیشرفت دانلود، امکان رد کردن یک نسخه و بررسی صحت فایل و امضا پیش از نصب
🟢
اجرای Real Delay Test و تست سرعت در پس‌زمینه و هنگام خاموش بودن صفحه
📱
دانلود از گیتهاب</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1817" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭐️
چطور API رایگان DeepSeek V4.1 Flash بگیریم؟
توی این ویدیو، قدم‌به‌قدم نشون می‌دم چطور به API این مدل دسترسی رایگان بگیرید؛
اگه با API آشنا نیستید، خیلی ساده یعنی به‌جای اینکه فقط توی سایت با هوش مصنوعی چت کنید، بتونید ازش داخل برنامه‌ها و ابزارهای خودتون استفاده کنید.
چه بخواید ایده‌ای رو تست کنید، چه روی یک پروژهٔ شخصی کار کنید یا تازه کار با API رو یاد بگیرید، این آموزش می‌تونه نقطهٔ شروع خوبی باشه.
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1815" target="_blank">📅 22:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1812">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✍️
موقت
دوستان هم نسخه مبایل و هم دسکتاپ برای کارایی بهتر اول ورژن قدیمی را uninstall کنید و بعد نسخه جدید را نصب کنید
در نسخه ویندوز موقع uninstall کردن حتما گزینه delete app data را بزنید
ممنون</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/1812" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XdERWzxS9Mq1OXji569dy_dSsnpPv9Bx8sE82w8jW6Glo9UZ31YSNTuKJ2kOxCBGyUxnP9FtasyrnI2GtPimPi1mJ5YytgC3BePLulfgL5RCGwnGBMsBHQO1vOy8-vz2ccn3DK14L5a355_AYxORg5OEt3mgM6cuHAQxRyfn7IWGNJgdtrXpzHIbKMP23QCKcTfzhiCMpL5wouo-7ZmhguScSr20ZhJ5h6r7ku6Y9N_pKvPnaionCq_lWNEM_JopWyq9IyXDq_fQwkFupG35MdCxj5_glKUFPW8nKUrhx_I9hYo8uQmxs9yHYdeBN7_y7L7gFCcfQXAsD70KIMLoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteAesther Mobile ۱.۸.۰ نسخهٔ پایدار
این نسخه دو کار را با هم می‌آورد: هرچه در نسخهٔ آزمایشی ۱.۷.۰ بود، به‌علاوهٔ یک راه خروج تازه. اگر روی ۱.۶.۱ هستید، هر دو را یک‌جا می‌گیرید.
⚡️
اتصال روی شبکه‌هایی که تا حالا جواب نمی‌دادند
حالت خودکار حالا واقعاً خودکار است. از همان لحظهٔ زدن دکمه، اتر و سایفون و تور را هم‌زمان می‌فرستد و هرکدام زودتر ترافیک را رد کرد همان می‌ماند. تشخیص اینکه کدام مسیر واقعاً کار می‌کند هم دقیق‌تر شده — دیگر یک مسیر سالم را به اشتباه کنار نمی‌گذارد.
این حالت از این نسخه پیش‌فرض روشن است. اگر خودتان قبلاً حاملی انتخاب کرده‌اید، انتخابتان دست‌نخورده می‌ماند.
🧅
ماسک در ماسک — راه تازه
یک پروتکل جدید برای شبکه‌ای که یاد گرفته یک تونل ماسک تنها را بشناسد. دو پرش تودرتو: پرش داخلی از دل بیرونی دست می‌دهد، پس چیزی که شبکه می‌بیند یک تونل است که محتوای مبهم حمل می‌کند، نه الگویی که آموزش دیده دنبالش بگردد.
هم در فهرست پروتکل‌ها هست، هم آخرین چیزی که حالت خودکار امتحان می‌کند — و بخش دوم مهم‌تر است: شبکه‌ای که این برایش ساخته شده همان جایی است که بقیهٔ راه‌ها شکست خورده‌اند، و کسی سراغ تنظیمات پیشرفته نمی‌رود. پس خودکار خودش به آن می‌رسد، بعد از اینکه راه‌های سریع‌تر نوبتشان را گرفتند.
از یک پرش کندتر است و عمداً آخر است. جایی که یک پرش کار می‌کند، چیزی برای شما عوض نمی‌شود.
🧠
موتور اتر ۲.۰
هستهٔ برنامه یک نسخهٔ کامل جلو رفت: سرعت عبور ترافیک روی تونل‌های TCP بیشتر شده، یک لایهٔ تازهٔ دور زدن تشخیص پیش از دست‌دهی اضافه شده، و پایداری تونل‌های تودرتو بهتر شده است.
🌍
کشور خروج روان‌تر
فهرست کشورها بلافاصله به‌روز می‌شود، «بهترین گزینهٔ موجود» همیشه در دسترس است، و اگر کشوری که انتخاب کرده‌اید در دسترس نباشد برنامه صریح می‌گوید به‌جای اینکه بی‌صدا تلاش کند.
🛡
پایدارتر
اتصال مجدد بعد از قطعی، حفظ تنظیمات محافظتی پس از راه‌اندازی دوبارهٔ سیستم، و رفتار دقیق‌تر هنگام جابه‌جایی بین وای‌فای و دیتا.
━━━━━━━━━━
📥
دریافت
برنامه خودش این نسخه را به شما پیشنهاد می‌دهد. اگر می‌خواهید همین حالا بگیرید:
برای تقریباً همهٔ گوشی‌های امروزی:
WhiteAestherMobile-1.8.0-arm64-v8a.apk (۴۵ مگابایت)
اگر نصب نشد، فایل universal را بگیرید — روی هر گوشی کار می‌کند ولی حجمش بیشتر است.
🔗
github.com/WhiteDNS/WhiteAestherMobile/releases/latest
روی نسخهٔ فعلی نصب می‌شود و تنظیماتتان می‌ماند.
#WhiteAesther
#v1_8_0
@whitedns</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/whitedns/1811" target="_blank">📅 16:54 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
