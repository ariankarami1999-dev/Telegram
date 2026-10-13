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
<img src="https://cdn4.telesco.pe/file/lkqQIQ7hElWDihTzjPI5cpVQMGP3w9ICNXZeWM6Kr-_EiRl2V7IWaVZzZ7BAXFtXruWmk424O_ll1bZqEtAKOzu78QDqZ2ueyf-HHUn5ouF46MVu8F_XUv_N96yQjdxltC_b5nnSMwXicy9QT-YWguqfT2bCSjXwluyLYRtnkjA880dVD5HvU499H0ETJcN8NdtFq1TZcw63TRdFTUW0eUg5csqqBwA6vqD35m-ODsuNWIf1juH8PYkD_9x1Yasr26zIh69CnVc4_sQMVAm6vmLoc_sUEbcAF-37bxQ77T4uyERM-N6pswtYYxTWptsqalCoeaz9Galx4EcRN1jpEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 08:11:45</div>
<hr>

<div class="tg-post" id="msg-1952">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/whitedns/1952" target="_blank">📅 11:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1950">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/whitedns/1950" target="_blank">📅 06:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1948">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/1948" target="_blank">📅 06:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1947">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9p98lEcEnHb6bxmF0bOFWqq2zwGSEOP5_91B0Pl0hb6mVwyrGQyLwTaZdQczCJtO2ampo5v1u3jGWkTnlbPcNMBNzzKDV0Hr73mwEh0Rndd_imIYlBiJ5QYVDYvApgCDzXd31cKtEKAazcMQm5pJzNYr2BI9YP_rFMSN-s5ll1oMP61DGOp6i0TqhUxrTJjedqnq2tiX9JlHtsfqWO-UVxcYCP7EzlYkx6ajmPUU216MiTG27ygkrRZz6C2mwhn7NKOWszFcmLITgi_uv1ppQrD0r2Q2rH2K6RIAiEtJnQHZLgUFYtE9tYMH5gB751XSpyeB38szfa9hy2CCQBelw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/whitedns/1947" target="_blank">📅 18:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1946">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TFkibC17ayx-p7YtvsgIYQj8_FeLv_ED1crW3l536bq-iah01nJXZewBiJOyRL5hWpKR3XU_eJE4aDIhhGYxFKg1okjhWXL9ynuzb-C0WOrc-0Ut65eNTeAuA6_2Y3qyE96YK1YdKY3eX_GZ85-WoATydSg9E3OebHwruye-nShvbTGR7TTnu6KyhT8OWdyGdHzHWgAZ7R_Jlw9h9j-GKjVI9fxNNYiH7K4X9mN8NcP94s8lWl6Kt_ky-rseVm-nqo1z0fZTTPWU8MwC1oX0XEH8AZCqfR1BCeYP69eeqP98U2_A7fMoCOAnW0vuFvN1togxdJrRRsjIMGMGFjMm8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1946" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1943">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1943" target="_blank">📅 19:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1942">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NLwaUTsdm59zJbxPPsqDcOwnt0l0v_nTKMMhqkVa3o9_engk44yZoooxK-qjjy3VSxm2uyxy6emgvOd5U4JHniA40WHB_y8mvoF-MFbJeZWC83AHV_vnu5W9PQzokumuIamyrFunADL4My6iVPUWmvTgi5N-_ywmZOzykXPlJQ45HbBsAGhWris9AahT0jkghozVt83Fa61bX_t6Nn8zZVf7f6gKvZ-5fZpq2fbycnMPmi69iuxIDGyvLKNk-2jbJDyNMP0xSj_WyDVZREt6AIA0ew-Nlqs3rGZJlgf0uvS_vFH78BkMvlsLWqgyz9uMhM1_ipMq6tcRpiEYAXUHhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/whitedns/1942" target="_blank">📅 19:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1941">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lFJpAAKRfT-cIVlzJkQi-iKX0ZTkVyiu66DOiz2u4kjHX_LXlEmqTsodZG9JxRzNDKkPQ1xRRwJ34h-A7v0GrszAX_TAjRbHfKZeNZlBh8ubCHiWHIpKoOJspC45WIq82wVBd_t1lS5KrxJE6Pd4BmnKk4hgzk3Xm8bdCF_e8r_KvtXa4IbUyJZaYQhHXUkaja6k07vmB9d7BOShHH1mgoeznXzUA0VxutuOCX1Ye68ISW04LSpVu6rN81l4-32cqc83YcVLXnjXVvEICaxanL1dju4Hy2Sz_ERndIrauzPokYeXwox6MMTCa0swczFvYOjpK1jB2DKFAJpQiDjueA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1941" target="_blank">📅 12:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1940">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1940" target="_blank">📅 12:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1939">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WInmtCo3b_ZNCYwxF_NPOfYDMM8rNfmMnkIgd1zrHPcyPadQBTHe2GdMy5PVBk3d50lOa5NExlON_lfJvIJ4jv3zTntZnqq_yzNw3O1A5gjVCQWw-2984tTOxjV3A0FYDP-Nm_oEFs0NTsdv9CQfhYkTZbwy_ATZFbrQ8dEDVQEljD5ZRvwoA3ySH31AAA8Ky7ACWsHM7Dm40JAMl2aV01_WwVj9K7sAwzLwVAUZml2wv5-7aTpJ-GL-pw0CU80Ek8MkOk0ctOWAhKKY-yrk4BKVMRzdbXINvqWg9Kz-4nyGGinv7uIcfkFTP-sRggEVpwEv1Fko8qM5gKHPryKSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دو عدد تصویر هم برای دوستان هستش که ایرانسل دارن که باید طبق آموزش گزینه های موجود رو انتخاب کنند
@whitedns</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1939" target="_blank">📅 05:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1938">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1938" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1937">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1937" target="_blank">📅 05:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1936">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnQZ3-z2TyEPxySrSs_yF-g1CHm3gKWovq7so9rBcwZ1rc6G_doky5VVxw7t-Aaezx0OfQtnil81uem92F6Ix1O269FhP05okV64d67hQEbrjDAYcW629Rwpf-YeBcx-os65GFsiqDx5AnZulb_99TZqkQ_LzXFS-zxHVVaZmWYMZcEHvpLIIQzbe6b2xfdywin8MatqFPrrT4nNKbvyp71d_OufgDYIDX9p8rRQ9_8yTLlTWFdj2WJKGknmfHBk4QuR9N_tt18wxU_KFA5zrpAW7ZTOOrIoGq6dU89nRd481-h6nRlXr4KYb1vQB1dPbiRvN3QtP5QLAfVgPwW9mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1936" target="_blank">📅 18:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1935">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjMf27xRVr6p8TSlLGR0v--fPbJKYcytcp48AJ5D90L_pg8acVbvUaYhhhZvnwx2M3cHyRQ8kfKUcnJvXjBj-kTOxkP4AshcYy_SuVjVvEDUajjSMbebqf7QtCh6E4LIFBwadHWpcRhCUuehuq8q6f3kVpr8P1YEpm0rN-Tq0T2mfDzKk8CV21r6q4raQ1OF2gTN2anrv6fQ28-BWYFigYXuWPjkL3lfGGbhmZMcHP65BxdNPUAGY_vh5F_R9gNtL3CJr78A3jLzIBijHXCXsam9UoOnbBYvl-LoTpQBPKhgPawulU0Yp-7WKGc75CkxRbGsTjV7pQXTejbpbx4ADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی ویدیوی جدید رفتیم سراغ CoreForge، یه اپلیکیشن کاربردی برای آیفون که از روش‌های مختلف اتصال، از VPN معمولی تا DNS Tunnel، برای شرایط متفاوت اینترنت ایران پشتیبانی می‌کنه.
🔥
از نصب و تنظیمات تا قابلیت‌هاش رو بررسی کردیم.
📹
تماشای ویدیو:
https://www.youtube.com/watch?v=yPLb4z4nF70
📱
کانال برنامه:
@coreforgeios</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1935" target="_blank">📅 14:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1934">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.3.10-P63_arm64-v8a.apk</div>
  <div class="tg-doc-extra">73 MB</div>
</div>
<a href="https://t.me/whitedns/1934" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1934" target="_blank">📅 04:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1933">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/whitedns/1933" target="_blank">📅 04:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1931">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kbpccUL0BNikspCW-zhlHi5-h-RUPeqHjP-uwQSNRCbsQGjAEP1JVK25-tIwplY8SI11Bl3Ld28mZQyfpuBL0Vfc1F0t2U3an4lgy8u2j6mexQ4nGPPLq0le_x10vqZLLvKoZjv_Sng14W3QinLHkvK9K89oQA58IeeJyIB9SBWBZ9rnKvgCLYRyrJc5VEzp0QJAyDpfMASdqTkUrYiaEzD9_ckwwfhZsCX0mR6OEfiVqh97Veo4pjA2GqqMh2zaP8XIP3jfkRw2QXa2m8k5RgD7N8oPr_-0xlR85JMozjL1f75rupESts9iwl5FI4NxquzX8S8mUuBUyyYX8KlsEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K0Gkbh_Fd6b0awKM-VS5Z0rv-LjNujsEzaG3sPQA0aXOwYL-ofe2HbwKp8bjnch8uclZQb9HaxxlfLeCfq9-msmRaAI_sO5bLNl2UIuYeTlsBjsQnfVULsCTiDkUducYhE75Sv5al1SkarleWfFiTM304GuuurfE-SZ-8CjJFEybCwY-YKIS8wbYdYJE-jPDE6MVr35Btm-6Gw66IRgJSzuRcCQfLGt0g6uDOwtbYqomJkVTtazCv9LOaCVsSQq9OF16TecRh_uwOIM-fi51AJJdBHtHQB7L_xLHHr_JvXCTdLtRaIKoVbo6_orY8TOpGayTUCbb7ruN3aBwZ2XuLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این تصاویر هم مربوط به تغییراتی هستش که باید در کلاینت MahsaNG ایجاد کنید دوستان گرامی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1931" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1930">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1930" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1929">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!  نسخهٔ مک ForgeCore از ریویو اپل گذشت و حالا روی TestFlight در دسترسه.
🚀
📥
دانلود و نصب: https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید: اول اپ رو کامل پاک کنید، بعد از لینک بالا دوباره…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1929" target="_blank">📅 08:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1926">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1926" target="_blank">📅 00:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1925">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7mvs2pJWrE0eobVD_oOSo92iUXa8ghw7_gZmimJQhxFQf6Cntf28SonBxIPvU1WvXFDBNopI3aILhTcO909nQs5ADWWnfDNnkuSIKIL4tw1MPnyaG8BPj692awp79TBcFcDID_bXwgL89iOwnerekzx4gByZd5VagtlVD2tAeenRIPd3g9Y_k_j2gqRH5ob47Zz1cOU6z5xtM0C7DTnMjdEulzh8yg3BifLUIJOHtTt-kr8x3mj6Gm-90Jzoysqii19VzoBH6OYD3_SWTNAMoE1AU-7C6_vxjqtE29gOLYo735xmj4KjERQQEg05cVkLdZzFKjabVN0wrXktGd8EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/whitedns/1925" target="_blank">📅 00:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1924">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1924" target="_blank">📅 14:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مادر بزرگ ۷۰ساله من برای اینکه بتونه با بچش ۱۰دقیقه در روز صحبت کنه VPN استفاده کردن باید یاد بگیره.
باید استرس بکشه که الان قطع میشه، همراه خوبه یا سامانتل، باید بدونه سابسکرسپشن چیه، سرور چیه و ۱۰تا روش امتحان کنه تا به گوش من برسونه که 《مامان VPN من بازم قطع شده》
😭
لعنت بهتون که به دل کوچیک و بزرگ حسرت گذاشتید.
ببخشید یکم شخصیش کردم و میدونم این وضعیت دردسر هممونه و نه فقط من. شاید این در مقابل دردسر خیلی ها حتی چیزی هم نباشه.
خیلی از این متد ها مناسب افراد مسن تر با دانش کم نیست. تا جایی که میتونید هواشون رو داشته باشید
🥲</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1923" target="_blank">📅 13:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1921">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-GUI_0.8.0_x64-setup.exe</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/whitedns/1921" target="_blank">📅 13:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1920">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BwdZ7HtyY0nSNH1UCd3FmcvGnH54YXQAMDkk9U64WkDR5CgyNoaxOqhFYe7td5PfqIuBNjHCoJe8_g6HeMUaYMq8ZNOH3P-qg2WA76AwWYIb7-imeL-7XgbxGNW6Uy487phUy_Zt-rqVUmUIePN0qpaJoW-MeEMlfpB3wnRA7N-i8wjJ275OdkF0Ar9v0jrI8x0128Au6JNlxNtkWTG1KE3ZU0VBy5KMh_bplYb11u33iwd2aIzl6Xb3olHl3tFNwRkFQcGSwWayXYfjskJswJliJNi3d8BdFxCaCPJ70cqmiystCIV3f3G0XU2JE8UDctxffFCzleMIPapg42Jskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1920" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/h1M6axSrubgD6PZz4c8tdNUzgNM_kql1ytW64kIRQ4wH2OyRK954Xn6qaQ40FPekbwetZwIhPWiWDSVFw3NdA9MI9Z1D1HOrtbNst62NAQ_2OQPoMRCA4q4VDRDPcenuptOSo7eokb_i4JgY8Bvd2chWeZFsw0zGWw9KigXz99KtpM0p317ahnRLDhnr1DYRVTrfjrXUEprRvAAPFCMTDb_EBSTfTkwB7pM1zMMciMfi30uwAIPJZtD4EwtWXXTQ25sWgEZvPKS1HvYqr4R74Cx4OQy_66wob8nSe5kC5BRPagFDHD2S4K5-fabV2-HiP9gS_ylErq0sgWgXW1Dwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/rQ1uf-5G5FGEUeI21-qD8ZT59sBWkPoOjXlOwELooZtN1ypy2_QHuFrB6HUrb96y8e7NAQhuSMgpVdxostR1TqDdAlsC-SZ2dBIe5J-spTRG3gNfRii1aQ72xFv8hNvZdOdJg9g34Krm-4j5jMHZoP9hY0PXkG_XCSauq_guiuBzjYC0WQ5yjjKXVr-zxiac5WEXaxGAw_rvA1Yl0A7Ma7mzI2k999trZg2vM3iNMzRFtHnZMbgPZTla9hMf1ZIrCJ3L915Oi8b4hAEUx6AGm16PJc9vNg69ju77_v26orF3l86tMa4r3FkvacSM8_fKfuN4fiQRLv9g9rUpK_tFbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1918" target="_blank">📅 13:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1917">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mVpgp1a0axSr_63i4lIkM53Gp7dsXzI1Y3L6_pNjfTMy1Xk-C-vGQ5ktKjLj6qEDH_Rrw1nQ1D0ADgMdQIYqXSWG06sUyTgalY5UtzFyQ4-4ZHS6x7dalJnIpSLUGEiE48XiNTI66Iesy5ql5-8cBuh_Xqq_PUOqGutWRBYSqnK8hi7JxNrLcDcOPCzW0PQ43jUsugA2zr80U_u9_jVxLnPhD7NucZNiguNjTPG4Bc15_GvEza0HlZwQvi3Tw-bKMbES1JDkjl7967wG1PKb3j4y8e1q-6vQqk9FKTfUZoz-OSWIB-u4-Hja7EWNKvBz_RHw-HqGZNoMKhttwB8YhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1917" target="_blank">📅 09:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1916">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">پروتوکل UDP هم به طور کامل روی ip های کلودفلر بسته شد (فعلا فقط روی فایروال همراه اول)
در نتیجه امکان اتصال به warp از طریق پروتوکل wireguard و یا masque-h3 دیگر امکان پذیر نمیباشد.
برای پروتوکل masque-h2 نیز، امکان استفاده از ECH از سمت خود کلودفلر بسته است، بنابراین در حال حاضر فقط با استفاده از IPv6 میتوان از این پروتوکل استفاده کرد.
روشهای جدیدی که بزودی منتشر خواهد شد امکان اتصال کانکشنهای TCP را به کلودفلر فراهم میکنند، در نتیجه، میتوان از آنها برای masque-h2، کانفیگهای ورکر، cdn و به طور کلی تمام اتصالات TCP روی کلودفلر استفاده کرد.
حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1916" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1915">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1915" target="_blank">📅 04:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1914">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QPzTN8aBCE_24sg79wjn7cqbZUcw5XPD4QY2RD9Cb65X0VYRb1XAnMFzgIVNa_FV1kMERRCAnUoSxox9Fwzgo5ju-WmF03TRW7UQaqw4V1s9aSj5wxWRM29Sp_XD2MZeEr803IkhaNRNvwD4BKIXTNpAcRC18dfaRuajHY32wCrOYXNK2o8GhPEz4dXb16lAwbivEkS4Kru03haQdIUf7sFrcNaMIq-tDrG5tRPCxwBRBm1danZnIUO7E5km1BLNM1pEbLurvbfgYcvxAFf7Rn1zuX2fju6sKkhx3Fb8jtKVWqtqis19-hMxftNejKX9-g4sHyJ5BYmdTiB0CIaA9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1914" target="_blank">📅 01:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1913">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👆
این کانفیگ ها را هم برای amneziawg روی آپ whitevpn امتحان کنید
یکی از دوستان خوب زحمت کشیدند این کانفیگ ها را بازنویسی کردند
❤️</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1913" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1908">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-mx-free-5.conf</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/whitedns/1908" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/whitedns/1908" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1907">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان عزیز:
به جز خود سرورهای whitevpn , الان ۶ موتور اضافه شده است که هر کدوم روی یک نوع اپراتور و یا منطقه کار میده
شما باید خودتون موردی که الان کار میده را پیدا کنید .
فیلترینگ مثل سالهای گذشته یک الگوی ثابت نداره و نمیشه یک نوع خاص از فیلترشکن را به شما داد که روی همه چیز کار کنه
ارادتمند
تیم وایت
❤️</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1907" target="_blank">📅 19:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1906">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-13.conf</div>
  <div class="tg-doc-extra">340 B</div>
</div>
<a href="https://t.me/whitedns/1905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1905" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1904">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-5.conf</div>
  <div class="tg-doc-extra">342 B</div>
</div>
<a href="https://t.me/whitedns/1904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1904" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1903">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-poll">
<h4>📊 دوستانلطف کنید اول این فایل ها را ذخیره کنید بعد از قسمت پروفابل - افزودن- amneziaWG  -وارد کردن فایل پیکربندی این فایل را وارد کنید و امتحان کنید که ایا وصل میشید یا نه</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1903" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1902">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1902" target="_blank">📅 15:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1901">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NsiDSfEHyc85C-FnXqm8wd7F3GuVQKDT9p_8vlFDBxwTUjl-xk8sacsD3rEhMWeHiF-5-I-C0M9Klh8ygGed7oF7Y8KFJRhVBAkk-K4JnDBlYnx7I13nFxyllN0Dp-kfQh3ZOmYwN9egEvhIBpNp_4qRd4aRSr1DWwhoe_qkc4CLgm8nl1RXuQN-j4iJmaN4zArGN82q6Kr3Y1WBa0idqup5h0UgjaMO1j7qQzAdqqM_iGJyalXANtK3pIbxtTYd7so9zbDySt6ShrRm2TbNwx3gbUNV5cztrZIcKo_Do56Jdf_D2C3tCjvTHcVSa_8iw1pIk5sdpCmokBLF-fwYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای دسترسی به امکانات جدید نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 میتونید با مراجعه به تب "پروفایل" - "افزودن" آنها را مشاهده کنید
@whitevpn</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1901" target="_blank">📅 14:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1898">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1898" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fMWScFWI7CADQVqoby3QAHMi8hDtA6YjI3MBLphYucCkX4TdNl1AIGuUkFZ0WHg8bs1RhdWnsJYvsSYUoZK_pNf1n1ips0DCB01XSxpnp29c4n7HPvNF6aq_d8-pp-U5Rkvix5ChH1xQ5bK38ylUgHarVBzLv2gRv1RSwb_rAmBH0G01niyioQGrwFJlU19eWObGp9K7MPkf7UkNLa7WKVEl3ptXeNu8tBaIq97L0beJCnRbaEOJCFJdqFQ5_8A6s6XDzWiNrA4MAWals2NBnP9kOK7lnrrPGbgHoVb_OEQke2VOmA2JdDQmnOcg9bYrNG8E8_RPGE3TsohwrkU5tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1897" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E-6ks2n_P_RuZ0hz7pdcFAhlytsCOkX_x3mbu2R2G1Su8LqAC-3hO6az6dQ_C7_tQAdzgq9o72JE_fsMSKdFFvPZ8qat2S11UxpIjVkUiSjZIeTq5Y5Br1UAka_f2UQireH7YiqfcTMB7VMVae_0BCxllaE-5LFVVjzCOheNqL0FRJ1RyBjRw5dm2ALP9v00d2TM7HwDpBMowQ4bZASTuE_RhstyZ8SpRLDbxIaTlasShr8i1oMdUQttzpTlHrSa2INU3M6-kEIFQT4ex0d9z6dIZkVBVoB1rWAEOI0jGIYITxv-Ui4---sBGX9LavfJIy6AUwRm5frAQLIub-PnLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/whitedns/1896" target="_blank">📅 19:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PFThxu4gzImrfLVY6xTm5aKnfqtpeoycGz_4VlOerOk-Wi_ebrNn541PoqP621akqkLsd70oDi76Yd4c-Neqmcd2Q95ElG3s1D9hTmNYD4bseO0GIB86IV_K3irSlDyAeAWJHWbmRpMg9yAtOCfI345Ct3wdohaiNLc8Pul1NUfbu3-WLEhFjWfUG4DVujPBO5NqyaRcBZ4mitlx7X0v7FJ5m3pN1Q-K_wjj1Xd6So6HVgvP98R7LibE3XZTRKbbuYBJadQxmnsbs_udhhWb5hAm2iKM3HpyTv1L8pFPZv5qPfvVoRRO5zk6ylcoHVs4MwBPGj0q8Ki6JVXc0z0wyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/whitedns/1895" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVtptVy24_5ZYrdTV_YxE42qL41TYoRNWtxCRL6VDlio0ZnzJfo8xJa-H9VMUD4DyXOYetAEBla-tlBEDLajaksfz0cV2XMO2kliHzyvPEVGAel8pwv4hn97j9igGSDX6-QCBoaAzacSjtHdsxw_-bNOxQeI539KZB_bIRmQnXRabWr3mlsPwmFqky0FPwBJSEwQRMrej8WZzjeGy6F2uhIHphbcYfj5ELKkI_giiPlvK69ZOWbJHXEzX82orsdXd5sKcOddQ1T-xxb_oGea5_LWh6KLkMUQ4OiRjiBSS9gO-9rMB3_MWCLe2HeZuqTpee3_FDUmCHTNHL-0oBiulA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommmahdi_sz</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YacBHZydMHvfCTgd6XPGOVJkD7HRaT6O6srVSCcd7cem8pA7iNy-63CHRNo-olx_3eDNACBpPesXaHbVnJGdoaQ5s8M1nlNDbaAMCjXEcfpcCiDeGYlYuohoj_D70AMBi-63at6HAb59T1hchZaPIuGvkzbpDWUmAKmrCDtbVsGYV_meEgdWivChqMll4MFS416X1zRReI3DaEyTjxs-cZYCh7vmroz7G7JtomuYTESNjYS9MFZULpm-ZruETQFYXTkYdCp8QddhANsxz894q0mfwamRWCidvtTXKTior9kG33DYtTXl3TvzvgptIFL5fVRoPGQMZ4jPARqQE9FAmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مشکل ربات
@WhiteDNS_installer_bot
حل شد
با این ربات میتتونید ازطریق تلگرام روی سرور خودتون MasterDNS نصب و سرور خدتون رو مدیریت کنید.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1892" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSMIFIEf4eFwv6VmrxwNGxxm63e2gTeEfVMl63FFqiBTZFwZI8PjMviVdsN95dGi55gcuRPtutDZXvlkamV650jLtA5gUq-qb-ndX5ePlXLCEyKY8rPwQABCtkyRvn1DwDJQB5xjHLRm_l3oZZxBfKBYHpqe1ADlHqX66y0QLL7Nk3RlhfPWT2Kqxau5IzVaeYqaxgT5dbmdAwGQQMJZgYkGwZZyYZUf7rYxbgNd009a2Ib6jgzV-kOpWxBbj07I_5Ti7lBSlcneptYj2Cvqs9KzsIPpSz_sYH1abgvZxFe1q2ovyjw2d0LRPFg5vItldbfyPAVN_vCgUrdZliJ_Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1891" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1889">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوست عزیز :
خرید ، فروش ، درخواست خرید ، آگهی فروش هر چیزی که توش پول رد و بدل بشه ممنوعه
🚫
بلافاصله بن میشید</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1889" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1888">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1888" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1887">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1887" target="_blank">📅 13:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1886">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1886" target="_blank">📅 13:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1883">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1883" target="_blank">📅 13:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1882">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel WispByte.rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/1882" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1881">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrVppyMPxG-5NkAC1NEj4i7YfbUnnNCSG6D0z2xQZ0Sva3SL4dVK8V4oy4FTBjYAYKaUEIgPYnXjQaHQFX84NcOfhDudU9VSL4Mtsu6PCQLbvh4qG32hVcZw_MtjHuace168OtUPLt59Semx3w5iMiysWQAIyy3wJTntK2VOdqt-hvFu6hJn5f7YgrP0K5CJrcrxBlTOssOIWV6O-SAx17DQKzrSHPCbZMgES466AMOOKG9Z80yzTfLbsZUQQfEcsDGjqLH945L2HBkUjCwlokxmfqdwgXc23sOu8ERDAoXGMZ4sGKopgSxedGUvfoac-XvbvXQvlVjohaEbIU4K9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/1881" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1880">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1880" target="_blank">📅 11:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1879">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-poll">
<h4>📊 الان با چی وصلین ؟</h4>
<ul>
<li>✓ whitevpn</li>
<li>✓ whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/whitedns/1879" target="_blank">📅 11:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1878">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
۵۰ سرور اختصاصی اضافه شد!
دوستان عزیز، لطفاً تست کنید و نتیجه رو به من بگید. موقع فرستادن نتیجه، اسم اپراتورتون رو هم بنویسید تا بهتر بتونیم وضعیت اتصال رو بررسی کنیم
🙏</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/whitedns/1878" target="_blank">📅 07:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1877">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🌎
سرور IPهای اختصاصی ری‌استارت شدن
🔭
برای دریافت آخرین تغییرات، برید به:
سابسکریپشن ← سرور اختصاصی ← دکمه تازه‌سازی
بعد از به‌روزرسانی، دوباره وصل بشید.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/1877" target="_blank">📅 03:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1875">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/1875" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1874">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1874" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1873">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1872" target="_blank">📅 06:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1870">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PnpDFauK9YVzzsUuoLe8YR_kNTgybMU9wFfWndp47Rw_3SP4Y8OYhUSxyEz1zsELzICNyhQ_gkfROiH-TvTb3uBWt3omYzQy7P09bxL7OM1kP9R2kHVWldyxxkaTB6FuZV7BM3sLpOdLdPy51otaW9b2425s0K6ZSqhYI6_aptBK_tF_pN-RcDsKuxJVFm5JRZqz1mtxdswQHmn56QGj5d6E-cloS1aQ6CunyQryflmHtBXgJmSsduutWE5I-GkeaNDUXy4j7wJqVLjs9ea7VMva7mH6oDtsGQ4rJ8TtqBQBV38lQBA5k1Y2FsOcNahwqNMK3ays5j9eqZ4Tsdj38A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1868" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1866">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1863" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/whitedns/1863" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WKq2_AJ8_pZ46uN-AlVDaEDXMTnrMJStkjtiSeDPJkTuL3Fyl9_KNbSNpX7VLN6agTBdkkWnknzj0zcG1wKRnXCzJM29r52LoXILyDtaXjaH146xV1XYPujimqvSNmSE-PM6Ist0yCKAD2hn4TGFpK0FSrnq-R7WEVh1KRvAfVHIkhPJ16ChiPUMbTtU8u4Hm-SfCTrU-aYMW-r1qrUA4DNPHVPG41YccDUq-cHPDe9LL29kFBAlWBrehUeJanHzFyukd3fm1Agpb96ZdhAPcITH_bF1VcekZh028EOjPJPYItakkCzIgWSnXr2Yw5u6rWQ38WOXmf-jn7N4Dutczg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52K · <a href="https://t.me/whitedns/1862" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1860">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Vh13Gd5VdB1Dav8JcwqhYBoxmqOjpiho0WPHN3EhJF5RC8YwPT-AlJVv4WaoGq-7CWo7a7CL7lt_pj_vboOtkkt83ip7K42KlKheJ4QdY4s93ai6OOd_tfz4t_2dYhgD2HsJVk_kCTnxZaOr48PVOQO_40kuSEKUh30p-pdyXK_G_36mSEdr8EvWLr_iXFQP-UAIa5PXdodXCfg5BXSGFM-HGgj-qcZesKXEmJcEYCkVxpdaJ3vv9Xcw2DBZ5xUiZtCk5sJf1HrNQbzVMVAtDwLG1GCADc4R2Fl4FcoYe2soPqf5WnKD00ymEAkUZ84jK0aRg9C42HAgwHdqe2L5ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/1860" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1855">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.10.0-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/whitedns/1855" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kzoEhoStlrSpMlT2iK93SlP8u4ErT0652Fjsd_U07RkL2cB_0_cezJQB8svn_IoFKWuaVC6CYFl3JwW9ThHht8sVJloLVnTWBtU92duLc6bgtZrdT4jJTdwAJSJfj1OO8JXdVJKYX82XMjac_RlSEyskhPcKKHjEH45MvVnWs-RzQPnLnRJ5heQlCkBtwjJsPqYN_8qJ9yv9TBwLlpqJsAOcwQVOC4yIPE2RJRdi1TUw3MlOitFX3isY2ymsO4SmT9wugTjAV1d8lociskt7D5YyK3xDndpG_4RdM0QsiHV9fTI5tF22nRdzUQsBC9sZ-0BjG0Owqhtl2X7PqJrs1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Whiteaesther mobile v 1.10.0
حالت خودکار حالا جست‌وجوی مسیر را ادامه می‌دهد و مسیر موفق هر شبکه را به خاطر می‌سپارد
🧠
پایداری اتصال بهتر شده و سرعت دانلود و آپلود در اعلان برنامه دیده می‌شود.
📶
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.10.0
@whitedns</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1854" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1852">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آمار اتصال ها داره برمیگرده به حالت عادی
❤️</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1851" target="_blank">📅 13:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1850">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.  لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید.…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/1850" target="_blank">📅 12:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9FIu4xLme_Rr_KL2-1UOJm1VZlvo963o4cXnUn9fWQ8XqHe8x4bmOQnMNyYyMRaU_NewvayvOqgxKSzKjru5VH89rK647wN0BI5jfS4I7Fpo0PAdfxOaYvT1pBpPGL6z8sQz0Z-B9OsR4GL3oGubstztUhc6sx2AaMzm2qKYQD4s0IAJM5s8398nVTXcFasEL7b_dJrPSOwf5talBL8ihv87cNAF4LffbnKc5rUr7TnJlq84jOCI3AlD1es8ulksF5anzn2I9we2-niiQOSySgRZ_kGQc6W48jvbXo01GF1KHxPfIgppLV5gbqr9wrWL0ld465eKnNl4oGMPmUAWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/i0au4vMgTWH12yTPm_1mSZmh6d6VLf_wNFhzbV-qcK9yY7dPRAaGIVXy9zcpKSnNdOraQcn0z7ZxYaN4Ct6iu0mAsv0DTw8kt-htRx4WJ731n_3AnWtqAUQN_4HwfgGVDrPyX7_PUKD2nYwrq8Z5pVgUAOQ5Ao_2P1zbkwDnFVvb_5BZqclE2tadpCddlcN8PrGKCf7UBlR1WZS2N12-5GFLEmaJRPfwk5y9D-sKsqEj729Z9BdejBAoziH9V-uJqTQjlcaupQzGyriKtXadfDZabU3pS9caNnpy1E-GrQge7IEchER9_D0gb7etpuvBpozc-ll4iLiWrkIo7p2MjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/DJ6zx27zaQJboYWdDh4zavloGIuygmq7T8JZqU3s8EzBRGSlDQ6HmQWFKQJw87uyxBs9PUKkUrvd4a7uz9yPyDZNiqLZ5uswLfgK-OoHeCqsmB__ZpArouNUursATUUz_m-EMqBRmm-UqVrTgP_dVw_Biay3sNtjuQ7ppxy73OtO1aD0-K8tgGeczmbmd2JOjBDE-V8gfMNJe6rxUd071_IS7IMP6ei2BwS0xj5Q1bfb3OEVE5fJJ65vmzKuZx2oG4rs3ZXzaknfeIptkNHX_9X7zLu-GUjeXynh58Awrz7KD9oZsuXRoubiEck7cr8Btie5c6RPU4flbBax795fgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/WanYwKIv8fFjt4jVYQL2qNZYoRHEiw-iiKjTo7iDsx9ampKyojBErfzCR8KOYyaF98_FNyQj44T_35UhTjUU1oowAzfPWCxsyedacHM9-RlgxJkVKCgo7IpXS2lg4hirZQqvnA9DUdA-Rek93a-q-qBwgZ3pGIu0vWQavO6MmTE3x5xYIYXZu7HkIUE42U1zAxpACMZg-I6KyVmW8jJBVS_8kR3jit9_I5VWbcII3GwKKste8aS9HD719aH3s8_jFRJfS3ISBbjVoPhZ_CWEFETbmBmXrVA4ROr-WSFE25XaISfPTr-phN9Slb1m-3PK2ywPZxXjWw7MCaeqQi6fIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Rybn40bUGkEnBOi47y7osb2dPH5w3ya9Z0oWCrON7U_720E3Q9GCkYbngAP7mnu7cCnX79GLjuPgeuWlGXtu5C9nTmg4tuaASGAFxjSogQi4E1nb-UzWEQrHmOpXp-8yi-xOz4p9F2qrMmpEMMdDg1UfA5M2iVh_vm4uQIFDr5nD1-yN4NQ6ATAefslVGOpdNxKemJzstbqByJ0rYQ5OPlMOw08fP-_1oR8QU-iM1PYBSAIlHFTuoIC83gbYT39MGNkx-jNeLeTQc2IlCHWksbCpGIHCrZCH-ETj7ePxMseGD_wtj3bSmWwkypmsfBC0MIyLw7c8x2i94Dj2QZgdnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/r6VactIXlWAXLJghgdqctrc7dHgxMRQQ7NFhay-_eYNpxlD4uxJ4N0W-mBNYWJ0Zykr4SXoj30nWVihIVvlW4nJ7SyL-aO8QWD9j-TLav_yhPzB4Nb0AsMum_h29x7jzqb5YQDDHpEKrnsZ--t1647Cr3hYIGJKBjGPaQvCPqThdMksHNIuwff7y3TpI1jNwLHoDVm3qqp0_JwhlaS0x9mhicIfk_FYIu9ok5DHVm-O3_X3JAUDp4_uYPauC0dFb6J_kQWyxCsnQGwWsxhjy1OUaDSsUJLz1NJfW7bgKJDu89ootvn_pjht6UU0C-yFQHw4GTtR4epDncs_83M_LWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/d6SNXtc1sNtF7aZ47Jkh4cMWdM5e99CGSnX5WIh3OftzqvlBTMl3k70Y_vfCUFpXWM1aqpeGR1AbbGjiZRtcoit0S9n63njMmX0ZQmT1w6nkiAbQoo4FsqBHpBE5_BbPADGsgPWFulDvrT3vTuJeId1mpw8DpTg6nB0Bss8JlJDHAQ3srXxFpHUFZRsB6N-FHrvMas-MyMzYW1uNWYtXzxrQGol4wR90r98pVFX7FiCuXUiaBwj549Gb3AfjhIFIwN57oFYJl6sc7fMDEAjLfLxxp64so86Z8ZFrnTp5dggQyoHIlES_gMsdCE7qnu4IeZy_ljb2LtP4248IZI330g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه WhiteGame یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1836" target="_blank">📅 09:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1835">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BibrPTuIUHmaJvb18g4x21aa5CqO_8D07YTbqUk_4r2c_8eWoWN6Sm5sCsgdP4B3xL_aVGaNvm2vRw9iZy-ffWKfH0cE345Qb9hi8odi3Ue_WrggnjqM0K8Oiq6R789LbOECpvMzk3Pg-WoRtQObAVgKDHWHC3kCBwLE8Z-7vqBLmFSYZFiM0MssY2p3ig8OV-4_HxwGTk5jul1szjmENldiIVUiWY5HRv_VWo4qD1Mnvwd9B8VC5cYgzjGk-TQ-yUu88OwH_iBH2xqmuQhdfxkt4l-3Z6OR6wLqpSNUu806md22QaRUp98tEXkFrqKwQLr8O0DCYDFPNp4JucqVvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/whitedns/1835" target="_blank">📅 06:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Sch4847hqd_kg3A3zoeOO8jOJ4xnplrtrkzNZjLP1VUfwM3d7w6dZXEMIjHTc9WkBkRhfcB37cq75q4dFJCNgyx40qs7UIchfcHLeGRLiUJ-n8terNL_iPV5lrLqBqFslWaRbUdD7DOet2MqrbYNrmN5NcbT--iP6Hbc9g1EsocPNSoyZqEE6kSf6E7rmjZZngUtjdGn4bB44pVsPweNaUdOZ8xoNVrFkQhPszG5BFhsnJyD30rlQN2XHUkM1WPGsdsHX5jhBgRnr0xjKg8e1TQmDlIhMvV-SRXWTltE7DaOL3OkrBGM05YYCQD8-UU9LkK7dKLAipG_Dlo4SJY3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا در گروه whitedns عضو بشید
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1834" target="_blank">📅 20:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1833">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tlTPJ7R8dTS26cb_pwB7TG6GeSDghIbIxaiHk73l9pKtkyFb6P2W10ebcyIB-wQTHabCytYTqZJbNmIFF6yrq_PNHJQ0qKAjZsxNMqUIK56k_lQXei-DI6xYOn5BphFA0Khk_I3bzeu1kVn__wJW2N1jbZX7ju3CCf8eES8fawEvSDZ-CQlPUhsMrZQmpKyeYjlJ0L5TP1KoN2JTnuXYKmeFXWVTdzFrjVzpcCVWQ4QMymFmapPQX-c61XuwvKgXV6JHwqezYmgb6WBPWjjmdXGdivIGvG7tfGdTFN9sm4l4UqGXuI9C5FL_GfAJaYWw9hIdD_d0_LiyXoLror0pDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8r3l5fAfMMvFmdb0ad-Ss7cSjec9t4ZBS3tWob34Sgz0tC9sDCLU7kqQvZ8K2S0Upw_OBtf2ULE9FOM2pGP0EaYrnkKtai13AyBgkNZUI-klSBbyyhvlNr3jlecVdFtPhMNGZKdJYEu_K9hT1eO-lREr3xZhTAzWurIZ9u4sVH5s_tLuDaAPSXNQCm6_zGUNBd_ooHh3aX7afABIudbX7-Bp7PSdrTkDpWG3Qq9gBH3g9lD_DIJIhQggkJwcAaB18u5N_tmn4_wH-sTaTi5DOWq5oMq1ipys0s2nprrQ_E811-f_bJF3nM_Tvad0t5cpvx8JKbfDnVA_mSA4t3ZbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hyyDBo2r-9gCiliE_PpejFzMq6iLnlAeZ4A-chNB9N0eYkT02m376N63Lg9NRKjQZX7UL0TMIH8A1BIHYstzrXybDg5sQeavktcMBWacc8Cbus6Hhl1vFSA1XllxbpIawAMiBSQ9d7QxOou8Uk-zf4jMatfBGL4CFFs9xSIUSx5hiIhH2TkOKaeUJTlsjvhLd0rUdjsvUywwpwFmoAperDMkwisjtcTBECDuh3vgEgLyz8k5Y-p8osb-D53NEIq3nSD0qnyVKGDqLgAO93J-VUs0tYbUUGOR_JIh3aWYhv3_PrOoPhrVF3Nwm_MnWTM3zsjAwvfe5srjL7YbRTRWiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/whitedns/1822" target="_blank">📅 14:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1821">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Qo2Zkaixq9Ui_cmowaaEDJ496MtTaCYqYzacI3as0MA05viJFt7lscOGOaf4RsWrCLGotG0dq6rw7QK-MLeq14352QumAgyuWAq9FTBPG1UekYwbCEtGsBEkAxtSv7xJRrUq3vjOSGIswtfN-ZBK90gEanEQe7mOoYYvmtUjFjSrEzXI8HVtpU_W8l6-oZAZyvhlBnHgTe9wBcdl5s10Vg2oJZiIr4KPihH51ffKWMFJwQt8pboUFF3jgRO2unIymQ2IWntyp_g_v5-Q73QotFbukQC4LdE0VMvbk83h5t0C1BD445cy6Xl_nnewMtw89WV66DqQlQfPInutKRUPeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/izQIiMl2otoLN0Jh03K55kB75vMtatFLxQH7IL2AUopqF1V4YBsCASZ-X9JWzK12B_tTeIA4Ekje6eLHKyXP5ikELZjXUSpZyO3Wetv91LzI_-EJWYDK4w0BWs2rWmROomY1UNeoUDQMTHvMHqQXdCJDccrMdKVIJ4uABK5VFveBWxCxbsgU7k8sxtDGcno2KVq-rO3JNcyp-D3OYfCAXaC5M-iWKNUb-4YefOqGS_gstm6knK54cntXlgGb80jyDqMfJOAtNxM9Y9pnx6Pt_9LAJTnNGVy1y5rLm73EpSQxUDbTgnUWnd3bXevuXraVUyWG2x6BsCoOST7cdy-jvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oOjpPpIKx-1v4ktzs_NHms-l09Fuw_OPyvi5A9gHoMVLhJEYrXRqi7crdgitYyUJdL3ywjlT1DTUaRjT7Us9B6kNgl8J7JpTMQ6XJCZJm1s2XhORLWfrAkj9SYm8ztq3ogVVu58buV0d_YdKtVLMzLD7TzeQwdQ4boecY4TmPfu28KXvEMHYFqMn6_CAeeIVRkSjjSDaJ2q5s5MqtyrKnkgNuWCdAkrloybzxdn6IU-hTjgHAgVUHuGUtiKbMWDlK10N70LXmtlue6M9puyZiFgPx1WZgvR0d60fqcV54Uh6kEmLzEUe7C2PTTGX2t5ioVW36CyYRKX4rLYlTkDMEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">😎
دیگه لازم نیست برای آپدیت از اپ خارج بشید.
اپ اتوماتیک ورژن جدید رو دانلود و نصب میکنه.
این به کسایی که اطلاعات فنی هم ندارن کمک میکنه.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1818" target="_blank">📅 11:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1817">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk3FriijYLjwII7k0zWzGCplZywSPh3-W7rgzRPF-YngajGww5-fFcYXb58mkdYmk_muJJMmQXBM6_7RQFBw0ZNr7HfH23D3UMGiv6cRPSxlELORrEsr0dMO2ab4gyftJHV3XSP2QF9un5C4_VHxmr7JNREIHdJ2msFMgErMMc68X7vla3rCVuKObDtZxJ9HPEFqlzDLg-4vzio21g6tfuBUK-8IuZSkYk0ToCCF1dEDYtWDTUD4L4-KvsLwUk5O-JqmJNOXLJ0Dx7qVfHpu4UKz1holWYaDcOJv-tLTnlu39QWQxfu67ZNZXfbp1x8n9ytvGOqz-A4IMUqpK_FK8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✍️
موقت
دوستان هم نسخه مبایل و هم دسکتاپ برای کارایی بهتر اول ورژن قدیمی را uninstall کنید و بعد نسخه جدید را نصب کنید
در نسخه ویندوز موقع uninstall کردن حتما گزینه delete app data را بزنید
ممنون</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/1812" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1811">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XUm-GfpxlRzzKuCF2SVVCPt4MZh_2s0Ff68DgovygnQj0LZKIbE8vrIQWfK-3lHV0fyPNcgv4jc8Ltjqccuttn1h3t5f1gPU11dE5lnxGYtV9haKJrhjXLRwr2-C9ZQJHkz0xuijvhP-xMKOH6dI4zOWVpMg7dIHDRCN_8nx-1_YDXYdoLes9MmwJyAJkkSFN7a8lPaV-xyPyGZQt7_TGGxUr3ZbcIWW1I9NowdMJ1NytoQWY5Rpp-ZjSr5HXaCTfPdzz1xa0qNxmdOm3LbNSL8RMPBryUWHmUMuB2BJpnio2QGrurrNgngIlbCYFAkrYPPZJqNQvlzgXQ_8uNltLQ.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-1810">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aRYrIxHEFTOyKFLAwDtZ_FuRcVt2hJKfKjsMuIX0aJ5M_ozRs9M5ew1E4YuC4Mo_L60ljCXK5f-oEjy5Re6a5VhVatSFiOR5Bze4cAnfcdBTGH9Rw1Z7UAQ5BRxuHHHyO0p19GJ4OK0AfQip0lebXbjDKpEYwN_T1lRdQWSQ-ANGCbUBgta73hIO-KNWzJYh96VUoLSYs2uTGYLj3jFwiSjPvrNwTmKS9afLsONoPuWq7X7-Q3BI-HNrKduigFXPDfd8qpVR1bxfd4cXhy6S6AqdN4_an0HGN-DJ1TO3FgdXUVBo9Dm03CNDieoStWbQfb7K4XIpeYFH_ZUzFsjSiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteAesther Desktop 1.9.4 — نسخهٔ پایدار
بزرگ‌ترین تغییر از زمان ۱.۹.۱، و دقیقاً همان چیزی است که بیشتر کاربرها لازم داشتند.
دیگر لازم نیست بدانید کدام راه کار می‌کند
تا امروز اگر وصل نمی‌شدید، باید می‌رفتید در تنظیمات پیشرفته و بین Aether و سایفون و تور یکی را انتخاب می‌کردید. بیشتر مردم اصلاً نمی‌دانستند این گزینه‌ها وجود دارند و فقط فکر می‌کردند برنامه کار نمی‌کند.
حالا فقط اتصال را بزنید. برنامه هر پنج راه خروج را هم‌زمان امتحان می‌کند و اولی که واقعاً ترافیک حمل کند نگه می‌دارد.
قبلاً یکی‌یکی امتحان می‌شدند: اگر Aether بیرون نمی‌رفت، باید سه دقیقه صبر می‌کردید تا نوبت سایفون برسد. حالا همه با هم شروع می‌شوند و معمولاً چند ثانیه‌ای تمام است.
🆕
یک راه خروج تازه: MASQUE در MASQUE
بعضی شبکه‌ها یاد گرفته‌اند یک تونل MASQUE را بشناسند و ببندند. این حالت دو تونل تودرتو می‌سازد که از داخل هم رد می‌شوند.
لازم نیست انتخابش کنید — جزو همان پنج راهی است که خودکار امتحان می‌شود. روی شبکه‌ای که بقیه بسته‌اند، ممکن است تنها راهی باشد که باز می‌شود.
⚡️
موتور به نسخهٔ ۲ رفت
هستهٔ Aether از ۱.۸ به ۲.۰ ارتقا یافت. محسوس‌ترین اثرش سرعت است: بسته‌های بزرگ‌تر روی MASQUE H2 و دست‌دادن سریع‌تر.
🔒
حالا مطمئن می‌شویم چه کسی جواب می‌دهد
قبلاً برنامه یک مسیر را «کارکن» حساب می‌کرد اگر چیزی از آن برمی‌گشت. ولی روی شبکه‌ای که ترافیک را شنود می‌کند، خودِ شنودکننده هم جواب می‌دهد — یعنی ممکن بود همان مسیری انتخاب شود که در حال خوانده شدن است.
حالا از سایتی که به آن وصل می‌شود می‌خواهد هویتش را با گواهی ثابت کند؛ چیزی که فقط سایت واقعی می‌تواند ارائه دهد.
🐧
و برای کاربران لینوکس
پیام خطای «تونل کامل» دیگر شما را دنبال دکمه‌ای که روی لینوکس وجود ندارد نمی‌فرستد. حالا می‌گوید واقعاً چه کاری از دستتان برمی‌آید.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/1810" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1807">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">💬
تقریبا ۵۰۰۰ هزار کاربر فعال از کشور روسیه داریم که روانه دارن از WhiteVPN استفاده میکنند.
اونا هم اندازه ما دردسر فیلتر دارن، اما با توجه به «چراغی که به خانه رواست ...» از ورژن بعدی دسترسی کشور های دیگرو به اپ میبندیم.
• از ورژن بعدی میتونید اپ رو ببندید و پشت صحنه اسکن انجام میشه.
• آپدیت داخلی و اتومیاتیک به اپ اضافه شده
• بکسری تغییرات کوچیک دیگه
💬
اگر مشکلی داشتید که به ما گزارش دادید و ما فیکس نکردیم، لطفا برامون بفرستید.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/1807" target="_blank">📅 09:23 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
