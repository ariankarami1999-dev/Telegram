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
<img src="https://cdn1.telesco.pe/file/VCnuBJjL4Fx_GtBtZoCzBZgQFurfBT4kEczeQ05ZLvksmH3ysHB9F1DFfCXMjupOxgfoZ3WhzD1S2cX9XiqEWmB8-_VG8zA1dZd7yn_N3Vh7Nf6bk74cxNDZ9pgXygaDNApoL7x_-ZDD01BoJVhLfudcLjqtRBowqXvUR9zmjZ7wBWgvdh7DYpqoPMnf4Fluk7iGZEOzkzg07ld_t-8iSS059zr7F1XBUXYOIxZkdlvj4FsRjIQF9Wa41pKXZr_auzWKRj_S3Aq97ou1qPjldwHH6a4_2vUdp6Zhh8evhIqyEI20wso-kFy0ZtZ5dOo-kbblpy8-lJblgoo41LMZiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 19:23:40</div>
<hr>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWt9AECqz_rREKo0AJMhVqfmAP6TV39MREdFJyCyZK5SnXxl2l1hve1f7BBVPJirLyt2jb8xwSktz7Gd5SNmbGG5S4B74KJLNkOXYt1lohi0euYZyTuO2dRu4prFua5GProH8rmfGl0sPjk9AJCgpXcOBDfdQ14xx4SMgaIZxGtLUG9Bxpc0rFVQElGbnSospKTzDhhEnrF3y-vnMAOFfpkcYbp8wZ57SHvanYuhM90QyVGqyhWazvTuIdH8UMsLIeOFp3_5CEXwkbkovFU74CKCXLayCD76gl15RfBSFvsFZgTALvZd3NJj2qAs2Vcu1-9DfnDLPn5uVhHrUOvZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی و انتظامی استانداری خوزستان عصر روز یکشنبه از «حمله موشکی آمریکا» به نقطه‌ای در اطراف شهر آبادان خبر داد.
ولی‌الله حیاتی اضافه کرد که این حمله کشته و مجروحی به جا نگذاشته است.
سنتکام، ستاد فرماندهی ارتش آمریکا در منطقه خاورمیانه، [هنوز] درباره این ادعا بیانیه‌ای منتشر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/VahidOnline/77279" target="_blank">📅 18:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1Z0zwXCEj6eP4ULNLCSxXpzwu0-doSqfH0t6A1C6NtSMTHWqO8yXP9hR0cTG6lMTtv372-gafDFkXOkoHWCKNRAks92drQTUY0r27vbgmPJXdNHYqNBFExBX-UkIZ6sJW_RxXe_Xk8h7XcKWhumqhBEArJLvo9bmaMcaU9swQoyFA4Bs7PsAot3DNpH1JUZd4q0oc0CqbTSf3ra63CHUGN7_PEYHpOW6NLCNDah4CeVg6vQ5SELhliJuelKKYDY8sFcz94XJmARG_0ifeZPyKwI437DOPxTpChU8XbHfXo-xPj9fRM24q6RMTTVHmvhnW6QMWeHfFa1ujzAVzfPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز یکشنبه اعلام کرد که نیروهای اسرائیلی و اردنی یک موشک ایرانی را که به سمت شهر عقبه در اردن شلیک شده بود، رهگیری کرده‌اند.
دقایقی پیش از این رهگیری، ارتش اسرائیل اعلام کرده بود که موشک‌هایی را که از ایران به سمت عقبه شلیک شده‌اند، شناسایی کرده و نسبت به احتمال «سرایت» حملات به خاک اسرائیل هشدار داده بود.
سخنگوی ارتش اسرائیل در پاسخ به پرسش خبرگزاری فرانسه دربارهٔ گزارش‌های مربوط به شنیده شدن صدای انفجار در نزدیکی شهر ایلات در جنوب اسرائیل گفت که نیروهای اسرائیلی و اردنی به‌طور مشترک یک پرتابه را رهگیری کرده‌اند.
در همین حال، ارتش اردن اعلام کرد که «سه موشک ایرانی را که خاک این کشور را هدف قرار داده بودند» ساقط کرده است و یک موشک دیگر نیز در منطقه‌ای بیابانی فرود آمده است، بدون آنکه محل دقیق آن را اعلام کند.
ایران در دور تازه درگیری‌ها با آمریکا که در هشت روز گذشته ادامه داشته است، اردن را در چند نوبت هدف قرار داده است. ارتش ایالات متحده اعلام کرده که در جریان حمله روز جمعه ایران به اردن، دو نیروی نظامی آمریکایی کشته شدند.
@
VahidHeadline
آپدیت:
اکانت ارتش اسرائیل، ترجمه ماشین:
⭕️
ارتش اسرائیل شلیک موشک‌هایی از ایران به سوی شهر عقبه در اردن، در مجاورت اسرائیل، را شناسایی کرد. چندین موشک رهگیر به سوی بقایای موشک‌ها شلیک شد تا از اصابت این بقایا به داخل اسرائیل جلوگیری شود.
هیچ خسارت یا جراحتی گزارش نشد. مطابق دستورالعمل‌ها، آژیرهای هشدار به صدا درنیامدند. این رویداد پایان یافته است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/VahidOnline/77278" target="_blank">📅 18:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/224ff6e0b2.mp4?token=OVrrJ_q1wlh9-glmbBxaaZv5F7bPbqmuRf7Sz_8wNCUT0dN5pWVy1im3VraxmfxXvVUxGMBAS96WyAvgzkSw8bdMMXvThdwRdJ7X9wNFwb5xVslNMuQRlX1hMVVEylehL9pvW67MmjUBbyjYDPR977Q_hxGar8rGXHrOhYLD7TAs5yyralb5GuhVBRbfrlcChnBIq2Le9-LOWf114PjpQn9r3oY3HEYNy3Nc-qyzSAUyQnqMnRhsFLY3AWAoZQBwXkCsDbVV_TcX9HeNhv77VDi_8KL9FPhQ0VlmaoP-GBX3iwhgqQxIZberTeBiczquN6cve-L0fKyKvRmASsU0c1mYLRSricXHylXEbxJMIlIxmDdPdcPyQGbOjpnD0FylpfEkUzxpvq-UzPtt2RVh-vRLY1lj8XAPeI6AKzGDFONrG1iECZsbdIUHZTfb4Ebprfeg93bLYqkWvijy_UXh2_Z88N2t3Dkl4UxFKTiJ0cfAb4llAnNZwCbhGr7RkWD-HjCxVmRzOZoZri1MCGUA-Zxr_55erOuSHBRLdIxSqVjdmwYY5ZRMV9cFm1mATTOGnG9kWmeTl4L_ThpYLi44gJgFejbyJcZSOVk3fMTd06LknT4_dpMtFo4R-s-AwSIv81JJAzQxrEgtycos4vd7KB6BT1PSZymeu0vZq4Z9ga8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/224ff6e0b2.mp4?token=OVrrJ_q1wlh9-glmbBxaaZv5F7bPbqmuRf7Sz_8wNCUT0dN5pWVy1im3VraxmfxXvVUxGMBAS96WyAvgzkSw8bdMMXvThdwRdJ7X9wNFwb5xVslNMuQRlX1hMVVEylehL9pvW67MmjUBbyjYDPR977Q_hxGar8rGXHrOhYLD7TAs5yyralb5GuhVBRbfrlcChnBIq2Le9-LOWf114PjpQn9r3oY3HEYNy3Nc-qyzSAUyQnqMnRhsFLY3AWAoZQBwXkCsDbVV_TcX9HeNhv77VDi_8KL9FPhQ0VlmaoP-GBX3iwhgqQxIZberTeBiczquN6cve-L0fKyKvRmASsU0c1mYLRSricXHylXEbxJMIlIxmDdPdcPyQGbOjpnD0FylpfEkUzxpvq-UzPtt2RVh-vRLY1lj8XAPeI6AKzGDFONrG1iECZsbdIUHZTfb4Ebprfeg93bLYqkWvijy_UXh2_Z88N2t3Dkl4UxFKTiJ0cfAb4llAnNZwCbhGr7RkWD-HjCxVmRzOZoZri1MCGUA-Zxr_55erOuSHBRLdIxSqVjdmwYY5ZRMV9cFm1mATTOGnG9kWmeTl4L_ThpYLi44gJgFejbyJcZSOVk3fMTd06LknT4_dpMtFo4R-s-AwSIv81JJAzQxrEgtycos4vd7KB6BT1PSZymeu0vZq4Z9ga8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی در یک مصاحبه ویدیویی اعلام کرد که از زمان آغاز دوره جدید رهبری، شخصا با مجتبی خامنه‌ای دیدار نکرده و تنها افراد محدودی موفق به ملاقات با او شده‌اند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، با اشاره به دلیل کشته شدن رهبر سابق جمهوری اسلامی می‌گوید هنوز این احتمال هست که در رده‌های بالای حکومت «حفره امنیتی» وجود داشته باشد.
او در گفت‌‌وگو با یک مستندساز حکومتی در تهران که بخش‌هایی از آن روز یکشنبه ۲۸ تیر منتشر شده است، با اشاره به «وجود عوامل نفوذی در بالاترین سطح نظام» گفت:‌ «نفوذ فقط در گرفتن اطلاعات نیست، بلکه در تصمیم‌سازی هم هست، در جهت‌دهی به فضای روانی هم هست.»
او تأکید کرد بمباران «بیت رهبری» که در جریان آن علی خامنه‌ای و شماری از فرماندهان ارشد نظامی ایران کشته شدند، از طریق یک «حفره امنیتی» صورت گرفت و افزود که این حفره همچنان وجود دارد.
به گفته عراقچی، در روز ۹ اسفند ۱۴۰۴ که حمله مشترک اسرائیل و‌ آمریکا به ایران آغاز شد، علاوه بر دفتر علی خامنه‌ای، دفاتر علی شمخانی و محمد شیرازی، دو مقام نظامی، و علی‌اصغر حجازی، مقام امنیتی بسیار نزدیک به خامنه‌ای، هم هدف قرار گرفت. از این میان، فقط حجازی زنده ماند.
جواد موگویی که با عراقچی مصاحبه کرده است، در جریان این گفت‌وگو توضیح می‌دهد که علاوه بر جلسه خامنه‌ای با مقام‌های دفاعی کشور، در آن روز یک جلسه بسیار مهم دیگر هم برقرار بود: جلسه شورای معاونین وزارت اطلاعات در نقطه دیگری از تهران.
به نظر می‌رسد اشاره او به جلسه‌ای است که اسرائیل اعلام کرد در نخستین ساعات حملات مشترک با آمریکا، آن را هدف قرار داد و چند تن از اعضای بلندپایه وزارت اطلاعات جمهوری اسلامی را کشت.
ارتش اسرائیل روز ۱۱ اسفند پارسال اعلام کرد سید یحیی حمیدی، معاون وزیر اطلاعات در امور «اسرائیل»، که به گفته آن «فعالیت‌های تروریستی علیه یهودیان، بازیگران غربی و مخالفان رژیم در داخل ایران و خارج از کشور را هدایت می‌کرد»، جزو کشته‌شدگان است.
جلال پورحسین که از او به عنوان «رئیس بخش جاسوسی» وزارت اطلاعات نام برده شده، نیز بر اساس اطلاعیه ارتش اسرائیل ازجمله کشته‌شدگان است.
رسانه‌های ایران پیشتر خبر کشته شدن محمد باصری، از مقام‌های ارشد وزارت اطلاعات، را در حملهٔ روز ۹ اسفند اسرائیل تأیید کرده‌ بودند.
@
VahidHeadline
عراقچی همچنین ادعای منتقدان مبنی بر اینکه مذاکرات زمینه‌ساز جنگ شده است را رد کرد و گفت جمهوری اسلامی در مذاکرات بر موضع خود درباره غنی‌سازی ایستادگی کرده و پس از ناکامی مذاکرات، طرف مقابل گزینه نظامی را انتخاب کرده است.
عراقچی همچنین گفت برای احتمال کشته شدن رهبر جمهوری اسلامی نیز سناریوهایی طراحی شده بود و «این سناریوها حتی کد مشخص داشتند»، هرچند به گفته او در جلسات تصمیم‌گیری کسی تمایلی به طرح آن‌ها نداشت.
@
VahidHeadline
عباس عراقچی درباره فرایند تصمیم‌گیری درباره مذاکره با آمریکا گفت: «آن زمان [بین دو جنگ] کمیته هسته‌ای را در داخل دبیرخانه شورای عالی امنیت ملی تشکیل دادیم که اکنون به کمیته مذاکرات تبدیل شده است و به کمیته شش نفره معروف است.»
«تمام بحث‌های مربوط به مذاکرات، در این کمیته صورت می‌گرفت و مصوبات آن، عینا همان روال مصوبات شورای عالی امنیت ملی را طی می‌کرد.»
به گفته عباس عراقچی، ریاست این کمیته ابتدا بر عهده علی شمخانی و سپس علی لاریجانی بود که هر دو در حملات آمریکا و اسرائیل کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/VahidOnline/77274" target="_blank">📅 18:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77270">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWjt5h9nVP-_fgZzrWr8RNq6bZnqzyyANzJijvmBOCdiBT1jpewI4dpQ5D6e2-FEiEM5Adtzj0GQagf5ebAdjfTRe3-hXKxtqCYPcO9dQBOgZVGBPSIPYbHYkiZO526v4eGZQmX8Scxj4faSTQkcCQXDyg89Tr6AtQMTXYOx-rO_F3PTC-Ki4i6822u8zIgRCMdtCpk0elOi28V8axowYwxAy9G3xx0ikgzg2V5oMSMkystvPHDw3RWtzmMrQFrvRtXu-ydCyhBUN3zaDmAW-Qj4XwiShTVXWlW1z9Vg4bpso_Jupbf01fWwZSiPWGsxLaQrqVKre6qXlZH_u8ekzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d80bc4cf46.mp4?token=LUgNIcYFzUIp1vai3YTSiAi9m8fY3tuNPvzAZoXH0OdTydQm9W6Rlw-IkDSrOmDPYytlCPgGKNW5b7wybtXusRDPW-C1Q6JmYs20yuGsKhdlwi7PkI4y5VnvE7CubwuN3x_FOkkyC6N93dpapXRM5-bLQdbgY8NMMOqnznPoW-wXXDYXXGuDILrvgIXIKw-q_pbMsc956S_bFT0PzpIVwK-fVXySF-D2nI4hFyLA7wY7AWHwdl-h6CiM_RCUVG8t6hX6cegbyo-OoEKvIseY1DlSqt0cMHz_egx-fhFm23-AikiXO5FGxtqZBgiMnroKLzbbx1mGYVivs-Hvez0S0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d80bc4cf46.mp4?token=LUgNIcYFzUIp1vai3YTSiAi9m8fY3tuNPvzAZoXH0OdTydQm9W6Rlw-IkDSrOmDPYytlCPgGKNW5b7wybtXusRDPW-C1Q6JmYs20yuGsKhdlwi7PkI4y5VnvE7CubwuN3x_FOkkyC6N93dpapXRM5-bLQdbgY8NMMOqnznPoW-wXXDYXXGuDILrvgIXIKw-q_pbMsc956S_bFT0PzpIVwK-fVXySF-D2nI4hFyLA7wY7AWHwdl-h6CiM_RCUVG8t6hX6cegbyo-OoEKvIseY1DlSqt0cMHz_egx-fhFm23-AikiXO5FGxtqZBgiMnroKLzbbx1mGYVivs-Hvez0S0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خواننده زیرزمینی زن که با نام «آنیتا پاپیست» در ایران فعالیت می‌کند روز شنبه با انتشار حکم قضایی‌اش خبر داد که در دادگاه به ۷۴ ضربه شلاق محکوم شده است.
آنیتا که ویدئوهای آوازخوانی خود را در شبکه‌های اجتماعی منتشر می‌کند، طبق آن چه در این حکم آمده، به دلیل «جریحه‌دار نمودن عفت عمومی» به این مجازات محکوم شده است.
این خواننده همچنین تصویری از رسید توقیف پاسپورتش در فرودگاه را منتشر کرده و خبر داده است که خط موبایلش هم مسدود شده است.
یک ماه پیش دادگاه کیفری استان قم پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌ طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
این خبر به‌سرعت در صدر اخبار قرار گرفت و واکنش سازمان عفو بین‌الملل را نیز به دنبال داشت، اما خبر حکم شلاق برای دو خواننده زن دیگر و اخبار این‌چنینی این روزها به دلیل اخبار جنگ و حملات بی‌وقفه به جنوب کشور مورد توجه قرار نمی‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/77270" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8YIL2qCSnCbHYau2AUws66okddCRTbksYmSbtBZs2r7-1CBuaOOsPf_oYcRr5yJOc_c2vhxJcdK7Ob7ZIegOqK-TQl8PDJmlmFSG0h6YnYUowR9omIvxelToUoAZw777moz5JFVFxUnnsGWcIAxYDzTNFLw28SdzNKBkecepQ-zAnR7-Tek9UE_QXPewy0UXK4pvUkHiVgiVoNtvtjOwJ6JD6OH1DMfmpqH8kPhRMoI_FxEh5wGBoJuYkDwW7oj1yBvCHONwsJdt8pAo0sLRZdXTpNnsarTJggKoXLiBFF02d-KG98f-n5lqBgDCqUGMYpPItThGVbIOj_R_QHP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنا کراری، شهروند دو تابعیتی ایرانی-آمریکایی که پس از حدود ۱۹ ماه ممنوع‌الخروجی و محدودیت‌های امنیتی سرانجام ایران را ترک کرده بود، به ایالات متحده رسید. هم‌زمان، مقام‌های جمهوری اسلامی همچنان روایت منتشر شده درباره آزادی او را رد می‌کنند.
جرد گنسر، وکیل دنا کراری، با اشاره به «۵۶۶ روز بازداشت ناعادلانه دنا کراری توسط حکومت ایران» از همه افرادی که در آزادی او نقش داشتند قدردانی کرد و افزود: «اکنون باید تلاش‌های خود را برای آزادی سایر شهروندان آمریکایی که همچنان در ایران هستند، دوچندان کنیم.»
خبر خروج دنا کراری از ایران نخستین بار روز ۲۴ تیر از سوی دونالد ترامپ، رییس‌جمهوری آمریکا، اعلام شد. ترامپ در شبکه اجتماعی «تروث سوشال» نوشت ایران به یک شهروند آمریکایی که به گفته او از دسامبر ۲۰۲۴ «به ناحق» بازداشت شده بود، اجازه خروج داده و این اقدام را «نشانه‌ای از حسن نیت» جمهوری اسلامی توصیف کرد.
اندکی بعد، جرد گنسر هویت این شهروند را تأیید کرد و گفت دنا کراری پس از ماه‌ها محدودیت امنیتی، در مسیر بازگشت به ایالات متحده قرار گرفته است.
با این حال، خبرگزاری میزان، وابسته به قوه قضاییه، گزارش‌های منتشر شده درباره آزادی یا مبادله یک شهروند آمریکایی را تکذیب کرد و مدعی شد هیچ «زندانی محکوم یا جاسوس آمریکایی» از زندان‌های ایران آزاد یا مبادله نشده است.
با وجود این تکذیب، میزان به اصل خروج دنا کراری از ایران یا لغو ممنوع‌الخروجی او اشاره‌ای نکرد و توضیحی درباره چگونگی ترک ایران از سوی این شهروند دوتابعیتی ارائه نداد.
دنا کراری، ۵۳ ساله و ساکن کالیفرنیا، سال ۲۰۲۴ برای دیدار با اعضای خانواده خود به شیراز سفر کرده بود. به گفته وکیلش، گذرنامه او در ایران ضبط شد و اجازه خروج از کشور را از دست داد. هرچند او هرگز به‌طور رسمی زندانی نشد، اما طی ماه‌های بعد بارها از سوی نهادهای امنیتی بازجویی شد و تحت محدودیت‌های شدید قرار داشت.
بر اساس گفته‌های وکیلش، مقام‌های جمهوری اسلامی او را با اتهام‌هایی از جمله «همکاری با دولت متخاصم» و «جاسوسی» مواجه کرده بودند؛ اتهام‌هایی که کراری و وکلایش آن‌ها را بی‌اساس دانسته‌اند.
گنسر همچنین گفته است حساسیت نهادهای امنیتی نسبت به موکلش به فعالیت او در «بنیاد کودکان مهر» بازمی‌گردد؛ یک سازمان غیرانتفاعی ثبت‌شده در آمریکا که با مجوز دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) و با کمک‌های مالی خصوصی، از کودکان کم‌برخوردار در ایران حمایت می‌کرد.
برخی رسانه‌های بین‌المللی نیز گزارش داده‌اند که کراری علاوه بر فعالیت در یک شرکت فناوری آمریکایی، مدیریت این موسسه خیریه را برعهده داشته؛ موضوعی که به گفته نزدیکانش، به افزایش حساسیت نهادهای امنیتی جمهوری اسلامی نسبت به او انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/77269" target="_blank">📅 17:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HgucFNe2n3rrKTqpVcDJbrktzrv2bgj5W_T4hFd9eVS3_5lYwYOESlXNqY0Ujm7it-nO82ukNKKS23ObNd73xhREnz0h5USMpCCc3D-Jq8uUhhdPyvCnMM2y2LmFH1TgARbHPh6zzdYbk_TKAZ20A0eUJAHJJabhsEOcympJ2ADqjHdfyE2nhXoa-cr-4NJ61aj4A3gAcPbJCno4kYobCaeqkpjxdxEAXmHBjXjSQuXx14Osh96WnxAh350NuigyEHiJJMv1Fczjo5Vj691Ayx7TuaWxnB1-rQRZ89zwmQtVb198hOTzBOuVE2j0e7d_aUfnR_n7AHdW2pkC9ttqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه، روز یک‌شنبه خبر داد که حکم اعدام عرفان اسفندیاری و گل‌محمد محمدی، دو تن از جوانان معترض دی‌ماه ۱۴۰۴ متهم در پرونده موسوم به میدان علیخانی اصفهان، در بامداد همین روز اجرا شده است.
هفته گذشته کمیته پیگیری وضعیت بازداشت‌شدگان در ایران هشدار داده بود که حکم اعدام ۱۲ نفر از معترضان دی‌ماه در اصفهان در پرونده موسوم به «میدان علیخانی» این شهر، در دیوان عالی کشور «تأیید شده» است.
در میان این ۱۲ نفر که برخی از آن‌ها به دو، سه و حتی چهار بار اعدام محکوم شده‌اند، چندین نوجوان و یک شهروند افغانستان نیز دیده می‌شود. بنا بر گزارش‌ها، گل‌محمد محمدی شهروند افغانستان بود.
این پرونده به وقایع ۱۸ دی‌ماه ۱۴۰۴ در محدوده میدان علیخانی، بین ملک‌شهر و کاوه اصفهان بازمی‌گردد، جایی که مقام‌های جمهوری اسلامی اعلام کردند چهار نیروی بسیج و یگان ویژه به نام‌های حسین رمضانی، محمد همتی، سید علی خشوعی و ولی‌الله صفری کشته‌ شده‌اند.
در پی کشته‌ شدن آنها، ۵۹ نفر در اصفهان بازداشت شدند و برای آنها پرونده‌ای گسترده تشکیل شد.
@
VahidHeadline
این رسانه حکومتی معترضان را به «آتش زدن ساختمان‌ها، تخریب تابلوهای شهری، دوربین‌ها و چراغ‌های راهنمایی و رانندگی، تخریب پاسگاه و کلانتری، آتش زدن لاستیک، مسدود کردن خیابان، حمله به مردم در حال تردد در خیابان و تخریب مسجد» در جریان تجمعات ۱۸ دی در میدان علیخانی متهم کرد.
بر اساس این گزارش، «عوامل دشمن» در اعتراضات ۱۸ دی به «انواع سلاح گرم، چاقو، قمه، قداره و کوکتل مولوتوف» مجهز بودند و در جریان درگیری آن‌ها با نیروهای جمهوری اسلامی در میدان علیخانی، چهار مامور انتظامی کشته شدند.
در پرونده میدان علیخانی ۱۲ نفر به اعدام محکوم شده‌اند.
در زمان اجرای حکم اعدام، اسفندیاری ۱۹ سال و محمدی ۲۴ سال سن داشتند.
۱۰ متهم دیگر این پرونده که زیر حکم اعدام قرار دارند، به سلول انفرادی منتقل شده‌اند و نگرانی‌ها درباره احتمال اجرای قریب‌الوقوع حکم آن‌ها بالا گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/77268" target="_blank">📅 17:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگر صدایی شنیدید و خواستید به من هم اطلاع بدید لطفا فقط بگید صدا شنیدم. یا نور دیدم، زمین لرزید... یعنی لطفا تفسیر نکنید که: زدند!
آبادان تک صدای انفجار از دور ۱۶:۳۸
سلام همین الان ابادان رو زدن برق هم نداریم
صدای انفجار آبادان همین الان
همین الان صدای انفجار یا شلیک موشک از آبادان
نمیدونم دقیقا کجای شهر بود
سلام ابادان همین الان ۱۶:۴۰ صدا شنیدیم
سلام وحیدجان همین الان صدای مهیب انفجار از آبادان
همین الان آبادان رو زد نمیدونم کجا بود ۱۶:۴۰
آبادان صدا انفجار
صدای انفجار ۱۶:۳۹ آبادان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/77267" target="_blank">📅 16:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌های دریافتی الان درباره شنیده شدن صدای انفجار که می‌تونه انفجار پرتاب موشک باشه، انفجار شلیک پدافند باشه و...
سلام وحید جان
الان ۴:۳۱ صدای انفجار اومد، کرمانشاهم
کرمانشاه صدای انفجار اومدددد
وحید جان (۱۶:۳۲)  کرمانشاه دو انفجار مهیب. احتمالا داخل شهر یا بسیار نزدیک به شهر
سلام وحید جان
کرمانشاه 4:31، دو تا انفجار بزرگ صدای جنگنده خیلی نزدیک و زیاد
همین الان کرمانشاه صدای وحشتناکی اومد
صدای پدافند نبود
الان 2 صدا انفجار آمد کرمانشاه
سلام همین الان کرمانشاه صدای وحشتناکی امد
ما شریعتی هستیم
وحید الان کرمانشاه ساعت ۴:۳۲ زدن
سلام وحید جان الان صدای ۱ انفجار از کرمانشاه اومد
صدای شلیک موشک آسمان کرمانشاه ساعت 16:30
دو تا موشک کرمانشاه خیلی نزدیک بود.
انگار تو شهر بود
صدای سوت موشک کامل پیچید
کرمانشاه ارسال موشک ساعت 16 و 32
دو پرتاپ موشک
[هنوز از اخبار ساعت‌های گذشته بی‌خبرم]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/77266" target="_blank">📅 16:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/miDyvAE_0ePfu2X0a1A4CbrnWztALdE-dwLb3lHd68wqhOEsI0G8s_y1XCDwvR-HjqpseG-9flQPkg_Ocg2aZnMQW1KZfuioc-VRPR17CC36xW0Gt97_dWTYXsV0xNhoF4Lcd-PRJ_zQVfQx59J9zaMHRW7378fLNN9M_8pTwgrTiAyUsKSuOjji4ozKTPTmAUCB8DczqWBLUKBEa3xKz7H5XM84RTeGR6VhdeKaybnuR68zBVWcNmEnwhvv70yRwnKcH60H4-H3EamDOW6ZT7LaZYNSGDkkVMHBy9EIF44--uzbLfb59Bko4qrXua7YUNY17ACJ7hcWFFLpNgGPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار در کویت هم‌زمان با پیام‌ها درباره پرتاب موشک از خوزستان
آپدیت:
ستاد کل نیروهای مسلح کویت در بیانیه‌ای رسمی اعلام کرد پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی «متخاصم» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77265" target="_blank">📅 10:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیام‌های دریافتی:
صدای یک انفجار چابهار اومد دور بود فقط موجش بود
09:42 بدجور زد الان چابهار رو نمیدونم کجا بود
چابهار یهو صدای انفجار اومد شیشه هامون لرزید
🥲
قبلا تو روز روشن نمیزد
چابهار یچی زدن همه ریختن بیرون ولی نه سمت اسکله نه پایگاه امام علی اصلا هیچ دودی هم نیست به شدت لرزوند
آپدیت: منابع حکومتی
فرمانداری شهرستان چابهار: صدای انفجار شنیده‌ شده در روز جاری (۲۸ تیر) در حوالی شهر چابهار، ناشی از عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77264" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSSRY5QKG2eErTTq-E4TR8kEOQALdN8055_u62l5n-dFS2PcYWukeHkd2BuCQwEEuzm9zz9DPP3jI81lQK9M_QsXLIYwzs7TBbawbSntTz_lTKbTQnzEUTWs2fDh6yUcUG1jt6U9VYRho18Uqv85QQeJyLy-XPvh7WIJf2-F_Mco5t8QZE-q-tF_MWwI-UXsHQdSv9JX8-0kz3hcuX_EuR0EcDEsM3psWR2yF50MfPV4e8_BGF9JscAPU2RetdrYVnUWYUHgGmMp81395rfHkm6zhILWwig6ktGk5lGyBonckymvwghO46o4rT8g3mIUNGt9TYbn_r8geRLCuyeI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های ساعت ۹:۰۹
سلام وحید همین الان گرگان زلزله اومد نسبتا شدید بود
آقا وحید گرگان گلستان الان ساعت 9:09 صبح هم لرزید، زلزله بود
سلام گرگان الان زلزله اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77263" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOzP_i9PRU7oGxxOzGXDGVEs8WLuGYLNeIC9295WUIUSXOBS5jSzhBPnQTKmIaElkq9AidKihHg8zZ2lKozSEiV6DMbujrEMk3WLgZfiiONhHIRBFj8WZpmqQV-L1EREqYJTKFFsq41hyexEeDsghdB2hZ0y5xxseEyNinV2eOBDnBLczFIxBQwAfKQRUuqiGmXOCuCCKd7gNVh_0n3pZnkC9R5wen1JHRuzjN4rU34jtHFCEVd8UP1fgfRUo7JLhWJh_fKTBzcXplEtQMayvYiKuSkl0VGJdETGO2tW65vzaWbaMlKnZU_ViEWtZsvbfe_DDrIvgkCHz6WnKFuO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت: زمین‌لرزه به بزرگی ۴
دوباره
در سالند خوزستان
پیام‌های دریافتی:
۷:۵۷ اندیمشک دوباره زلزله اومد
دزفول لرزید دوباره
اهواز دوباره زلزله اومد
دزفول لرزید بازم فقط شدتش خیلی کمتر بود
زلزله ۷ و ۵۷  دقیقه باز هم دزفول با شدت کمتر از قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77262" target="_blank">📅 07:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77261">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj8qZVOnhx_nPxJRrGXBoKkBFTO_ppsFwJFO_6jxeW9cLFvHJ_gEG-KuT5s_pUnIukWSPOiVFEFQiqFf1uH77mKYuXeT1lXbVD5kUstMD-eqmFn5YFcOFstV9dIbtI0wCRqKGKrnN7BRRDmHrgCC2AWAa5Vjkz3qEeGg3vp0Y08zQ7m_-pR1He45KZ5DrIW0BbsCUMbiOb82GJ1sD4i02tVkgqP3wbgpHKRx98dDzKRkgZEH7Vyn6YhcwSOMMqET_HEPtYKtLs64WJZRlMIyCULnBon3Oa7hCxQsxccstZYh01m0WHTEO_Xa8qQlWzz95Qe_SjMPNsou0eFO9fTQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه سقوط ارزش ریال، قیمت ارز، طلا و سکه در بازار ایران به سطوح تازه‌ای رسیده است.
براساس نرخ‌های ثبت‌شده در روز ۲۷ تیر، قیمت هر دلار در بازار آزاد به حدود یک میلیون و ۹۴۵ هزار ریال، معادل ۱۹۴ هزار و ۵۰۰ تومان رسیده است. یورو نیز حدود ۲۲۳ هزار تومان و پوند بریتانیا بیش از ۲۶۲ هزار تومان قیمت‌گذاری شده‌اند.
در بازار طلا، قیمت هر گرم طلای ۱۸ عیار به حدود ۱۹ میلیون و ۱۳۸ هزار تومان و هر مثقال طلا به حدود ۸۲ میلیون و ۸۹۵ هزار تومان رسیده است.
قیمت سکه نیز یک میلیارد و ۹۰۰ میلیون و ۵۰ هزار ریال ثبت شده که معادل بیش از ۱۹۰ میلیون تومان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77261" target="_blank">📅 07:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b791da5472.mp4?token=iAJxzbnHTr6IRN4Kqk5F3Dro9m-w0rtIqQQt3fGOpt_yoov2JxaXs959_L6GAiVR6YbhRP4E5-ZcwF-4g96WkXf8qOzW0WUo7l9RIRkKHFTslAt63tvp7I4zALMcU1keitH82AwMsar4IuVXKeklfCzxfp3NGDHtKGPt5D069CPXwzaZDXGGDKycD62GzAv1MrmYoOrCaFuDxRRJNEw347ehmA0cZPObE6ZvzUqvcifQrC5dZzzPC-OANII8UGB8PBMlmtT4xP_WK35BbGNyzacUaNsiMkeVnVS2A1qJe7jNX7hZdJeYTihzj53LmJd7IxjaQ4DgL9dUKH8V-kbetA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b791da5472.mp4?token=iAJxzbnHTr6IRN4Kqk5F3Dro9m-w0rtIqQQt3fGOpt_yoov2JxaXs959_L6GAiVR6YbhRP4E5-ZcwF-4g96WkXf8qOzW0WUo7l9RIRkKHFTslAt63tvp7I4zALMcU1keitH82AwMsar4IuVXKeklfCzxfp3NGDHtKGPt5D069CPXwzaZDXGGDKycD62GzAv1MrmYoOrCaFuDxRRJNEw347ehmA0cZPObE6ZvzUqvcifQrC5dZzzPC-OANII8UGB8PBMlmtT4xP_WK35BbGNyzacUaNsiMkeVnVS2A1qJe7jNX7hZdJeYTihzj53LmJd7IxjaQ4DgL9dUKH8V-kbetA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا هشتمین شب متوالی حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) به دستور فرمانده کل قوا، دور دیگری از حملات علیه ایران را در ۱۸ ژوئیه ساعت ۱۱:۳۰ شب به وقت شرق آمریکا به پایان رساند.
در هشتمین شب متوالی حملات آمریکا، نیروهای سنتکام با موفقیت تأسیسات نظارت ساحلی و پدافند هوایی ارتش ایران، توانمندی‌های دریایی و محل‌های ذخیره موشک و پهپاد را هدف قرار دادند تا تضعیف توانمندی‌های نظامی ایران ادامه یابد. تجهیزات نظامی آمریکا همچنین نیروهای سپاه پاسداران انقلاب اسلامی را که در ۱۷ ژوئیه به نیروهای آمریکایی در اردن حمله کرده بودند، هدف قرار دادند.
بیش از ۵۰ هزار زن و مرد نظامی آمریکایی در سراسر خاورمیانه مشغول عملیات هستند. آن‌ها همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77260" target="_blank">📅 07:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منابع حکومتی:
‌معاون امنیتی ‌استانداری خوزستان: ‌جنگنده‌های‌ آمریکا ساعت ۰۵:۵۵ دقیقه یک نقطه در اطراف شهر شادگان را مورد اصابت موشک قرار دادند.
ساعت ۶:۱۰ صبح امروز جنگنده‌های آمریکایی بار دیگر مناطقی در جزیره قشم را هدف حمله قرار دادند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77259" target="_blank">📅 06:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77258">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام‌های دریافتی:
الان دو تا افنجار بندرعباس ۶:۹
اصلا تا حالا این ساعت حمله نمیکردن!
وحید جان ساعت ۶ و ۹ دقیقه قشم صدای چند انفجار اومد باز
وحید ساعت ۶:۰۷ دقیقه دو بار قشم صدای انفجار و لرزش
دو سه ثانیه قبل از زلزله،صدای بمب سنگرشکن اومد،قشنگ از دوران جنگ تو گوشم صداش هست
بندر عباس ساعت 6:09 دقیقه مورد اصابت قرار گرفت دوباره
سمت پایگاه هوایی دو انفجار بلند
یکی دیگه هم الان زدن ساعت ۶:۱۰
سلام بندرعباس رو زدن ۳صدای انفجار پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77258" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mz65I-ibq1SYPjxM3t-W9mZRgH6efEUCpnQJmEgcvUG3lVPJVk5TShs0NE0nPNShoVTRd7MSPQEo9u1y_80El_JRqeMMi--lV3XxccMDA-mpNkSmqeWoWzqBPA3bnmZHix5_wrxSW5oasErUJl34mhKXGDvRGG_dwcUkxax9PbuXuGxDY9wQX2iOUjRlFhGLZqYbN6688RgobVfbW-Wg97kVIcPWiRg7E_zZdvgEgpPGevgTiKhQUL5zx4FksuiGxVO-Temi4V84gYxMsFNDnN082rjqrIhdw7wNQ3WL1i1_V2tzKpZwGxZmEVroH8IvgTe9Dsvts7gKms1q2-FTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
زمین‌لرزه به بزرگی ۵ در عمق ۱۲ کیلومتری زمین در سالند خوزستان
پیش از آپدیت:
پیام‌های دریافتی درباره لرزش زمین:
وحید جان همین الان زمین لرزه شدید شهرستان شوش
خیلی بد بود
دزفول  رو زدند
همین الان تکون خورد همه جا مثل زلزله بود
زلزله اهواز
خونه لرزید بد جور دزفول چ خبرههه
همین الان اهواز زلزله اومد
5:55 دزفول
از توی خواب پاشدم،تخت و خونه و تمامی وسایل داشتن با شدت بالا میلرزیدن
اصلا نمی‌دونم زلزله بود یا جایی رو زدن
اقا وحید اهواز همین الان زلزله اومد 5:56
اهواز ۲ بار پشت سر هم زلزله اومد
ساعت ۵:۵۵
یکم ترسناک بود
اهواز زمین لرزه اومد
خیلییی شدیدددد تمام خونه لرزید
سلام اهواز زلزله شدید ۶ صبح
همین الان اهواز خیلیی بد لرزید
زلزله اهواز ساعت ۵ و ۵۵
اندیمشک هم زلزله شدید امد
ماهشهر زلزله نسبتا خفیفی اومد
سلام زلزله اهواز شدید مثل اینکه از دزفول بود
سلام آقا وحید اهواز الان زمین لرزه حساس کردیم،ساعت ۵ و ۵۷ دقیقه صبح
وحید جان دزفول همین الان زمین لرزه شدددد
زلزله اهواااز
از خواب پریدم کامل تخت تکون میخورد
زلزله اهواز اومد وحید کل خونه لرزید
ساعت ۰۵:۵۵
از خواب پریدم از شدت زلزله
اهواز چندبار لرزید بدون صدا
وحید جان الان اهواز زلزله ساعت ۵.۵۵
سلام زلزه اومد اهواز‌
وحید از خواب بیدارم کرد
و طولانییی بود
سلام وحید جان ساعت 5:56 دقیقه زمین لرزید ویه تکون خیلی شدید خورد خونه دزفول
سلام وحید جان ساعت ۵:۵۶ صبح زلزله فوق شدید اهواز همه چی داشت تمون میخورد
همین الان اهواز زلزله ، وحشتناک بود
سلام اهواز زمین لرزه بزرگی اومده حدود 10 15 ثانیه خونه داشت میلرزید
زلزله خیلی شدید اهواز ، ۲ بار تقریبا پشت سرهم ساعت ۵:۵۷
اهواز ساعت ۵:۵۵ خونه بد لرزید انفجار نبود انگار زلزله اومد
اهواز ساعت 5:55 دوبار زلزله اومد
آقا وحید زمین لرزه شدید اهواز در حدی که مبلا از جاشون تکون خوردن
سلام زمین لرزه اندیمشک هم حس شده
سلام شوش دانیال همین الان لرزید. انگار زلزله بود
دزفول  ساعت ۵:۵۶ صبح چند دقیقه ناجور لرزید
اهواز زلزله اومد هنوز لوسترها تکون میخوره
سلام وحید خوزستان لالی خیلی شدید زلزله اومد۵:۵۵
مسجدسلیمان هم زلزله حس شد ۵:۵۶
درود ایذه دو بار لرزید الان‌
سلام ساعت 6.55 شوش بدجور لرزید اما خیلی کوتاه ولی خیلی ترسناک بود
سلام ساعات 5:55 گتوند خوزستان زلزله احساس شد لوسترا تکون میخوردن
سلام زلزله سمت دزفول خیلیییی شدید بود یکم دیگه ادامه میداشت من خودمو از تراس پرت میدادم
اینقد طولانی بود که موقعی که بیدار شدم رفتم توی تراس هنوز قطع نشده بود توس عمرم اولین بارم بود همچین چیزی حس کرده بودم
🔄
پیام دریافتی به نقل از مرکز لرزه‌نگاری کشوری:
گزارش مقدماتی زمین‌لرزه
بزرگی: 5
محل وقوع: استان خوزستان - حوالی سالند
تاریخ و زمان وقوع به وقت محلی: 1405/04/28 05:55:21
طول جغرافیایی: 48.61
عرض جغرافیایی: 32.58
عمق زمین‌لرزه: 12 کیلومتر
نزدیک‌ترین شهرها:
23 کیلومتری سالند (خوزستان)
27 کیلومتری اندیمشک (خوزستان)
29 کیلومتری دزفول (خوزستان)
نزدیکترین مراکز استان:
103 کیلومتری خرم آباد
140 کیلومتری اهواز
📍
آمریکا هم
میگه
بزرگی زلزله ۴٬۹ بوده در عمق ۱۰ کیلومتری همونجاها:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77257" target="_blank">📅 05:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77256">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس همین الان صدای چهارتا انفجار اومد
03:33 سه تا پشت هم صدا اومد بندرعباس ولی فکر میکنم دور بود
همین الان بندر عباس صدای 4 انفجار
الان وحید جان ۳:۳۳ چهاتا انفجار شدید بندرعباس
همین الان قشم
صدای ۶ تا افجار پشت سر هم
خیلی بلندو قوی بود
کل پنجره ها لرزید
سلام ساعت۳:۳۴ صدای سه تا انفجار قوی اومد بندرعباس
سلام بندرعباس ساعت ۳ نیم صدای ۴ انفجار شنیده شد
بندرعباس ۴ تا الان زدن
#بندرعباس
28 تیر ساعت 03:33
صدای 4 انفجار سریالی،محدوده پایگاه هوایی
۴ تا انفجار سنگین در بندرعباس
بندرعباس 3:33 تقریبا سه تا صدا اومد
🔄
سه تای دیگم زد 03:35
مجدد انفجار ۳ تا در بندرعباس
دوباره زد ، شدید داره میزنه
یه صدای خیلی وحشتناک تر الان اومد۳.۳۵ بندرعباس
دوتا دیگه هم الان زد
سلام صدای ۴ انفجار به همراه لرزش از قشم
بندرعباس وحشتناک صدا انفجار میاد مشت سر هم داره میزنه
بندرعباس صدای انفجار 3.35 شدید بود
وحید قشم رو الان ساعت ۳ و ۳۴ دقیقه دو بار زدن
بندرعباس همین الان 3 انفجار جدید3:35
#بندرعباس
28 تیر ساعت 03:35
صدای 3 انفجار سریالی دوباره ،محدوده پایگاه هوایی
وحيد جان قشم هم صدا مياد
٤،٥ بار پشت سر هم
همین الان ساعت ۳:۳۶ چندتا صدای انفجار شدید در قشم
الان ۳تا افنجار دیگه اومد، کل خونه لرزید، خیلی بد بود ۳:۳۶
تسنیم ساعت ۴:۴۵
گزارش ‌خبرنگار تسنیم از بندرعباس:
🔹
براساس اعلام استانداری هرمزگان، تا این لحظه ‌بر‌اساس گزارش‌های دریافتی، هیچ‌گونه اصابت موشک یا پرتابه‌ای در بندرعباس ثبت نشده است.
🔹
در حال حاضر آرامش در منطقه برقرار بوده ‌و با وجود شنیده شدن برخی صداهای نامشخص، طبق آخرین گزارش‌ها تاکنون هیچ موردی از اصابت موشک در بندرعباس تأیید نشده است.
🔄
ساعت ۵:۳۰
صدای انفجار اومد همین الان
4 تا پشت هم
وحید الان ساعت ۵ و ۳۰ دقیقه قشم دو بار صدا انفجار شدید اومد خونه لرزید
بندرعباس الان دوتا صدای انفجار اومد ۵:۳۰
ساعت ۵:۳۱ دوتا صدا انفجار اومد بندرعباس
دو انفجار الان بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77256" target="_blank">📅 03:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77255">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پیام‌های دریافتی ۲:۱۷
درود وحید جان همین الان بهبهان اگر اشتباه نکنم سمت پالایشگاه بیدبلند رو زدن ما تو حیاط بودیم  که اون سمت آسمون سرخ شد
سلام بهبهان صدای سه تا انفجار اومد
سلام بهبهان چندین صدا اومد
صدای عبور جنگنده در بهبهان شنیده شد ولی تا این لحظه هیچ  صدای انفجاری من که ساکن شهرم نشنیده‌ام.
خبرگزاری مهر:
برخلاف فضاسازی رسانه‌های ضدانقلاب، تاکنون هیچگونه حمله و بمبارانی‌ در بهبهان صورت نگرفته است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77255" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPMK1ZpAeyHr4mXpsCTGZDonk7L2wb7bHEGZCHXFAREmCRYaONHFkW7MiZmF1124_O5aENsB4Lc46h7vSQVnqqtyF3SfIO6YxuMsiQjlElwb8HISeTEFuRlJsXpjCqtm778LadTvcfwvpR9EP2rBIltGbmz2dKzrQX_FF2m6VDAY0ZkQwddxO0wXU5mEE-0I9LapsgIm0Tj1UHtLripclU4xusmLTEGQy68uxRqNPyqvIH_FELcYYL4rRWIS8r-osGPDfpgdVUumTxIyogh4lpXMIWkpXdHHRBoumZgTpsXvAAKzpq2lWxdhtvBMiKKjv5XO-Y2NjRlpgX3SBLIrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۶ عصر به وقت شرق آمریکا [۱:۳۰ بامداد یکشنبه به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور تازه‌ای از حملات هوایی علیه ایران را آغاز کردند.
این حملات با هدف تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی انجام می‌شود که شب گذشته به نظامیان آمریکایی در اردن حمله کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77254" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uj1_ZRVsLm0Q2ImLhOEtD9ihKZRdEu1Z-aCFDbeSP7JDa98_8m0W7LiROm-7fAJiGDksus11ey2FA0I9yFXcMkwc8z4M56eEyk4M1EZPnNBmnyc5HSSs_KJWfqn7GmiL675Is3xmzeIWH_7TPg1rh70-HSCJEwNGjQx-4Fkmn0ArOCIcA5Dc-EoCNFZdnN_FhEfz9Plgdy8b0A21cU_3AU2cUeGfQb_unJ4BWnR2NIUO-jM0W-jb-4uyB-YrfT1mYxJd-ct1u5riz3ObwosuHvx7gzlia2mS9A9GZphCxYFPH_uR2yV1YDmy3EIH_TRMznd2hTdsDgVhbdUNLPD1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d99_lFgXJxc0GYm-OhZjCgjSFhK4nwWRdXOZR-Kqv1nhf6ejSUkSzTzS0OWlDC4YM-aSxoNS1Z5qMHkjAf9jz3o9CwgFIt4J770cHXxNi3FJz5-XImg_WI2FX5m3FQcy0wYdCMnuUh4LPBY2VCe6cku1hED2Z0eO85fOlz9ZoQ9hGYexZ8VtfyZwdcAIRPaI91Tm8nbUqp6ebTXRjxGd5f_EaQPv9AST9OfuX7pKs5B6mRVSZMP1VUvvDoPjyyT38BfhszkDqEsEOOY36EAq5pKENYHnky_bv6Q-jwhzEqom-Url7Hk7wRgZSyGnHvx73gNsw_Hp-gKkK2W7a0veSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری ایالات متحده، در واکنش به کشته شدن دو سرباز آمریکایی در اردن به شبکه «نیوزنیشن» گفت: «بسیار غم‌انگیز است، واقعا رویداد بسیار غم‌انگیزی است. ما از دیدن چنین چیزی متنفر هستیم. آنها در راه خدمت به کشورمان جان خود را از دست دادند.»
@
VahidOOnLine
ترامپ در بخش دیگری از این مصاحبه با مواضعی قاطع، بار دیگر تأکید کرد که «ایران نمی‌تواند و نباید سلاح هسته‌ای داشته باشد.»
او همچنین در واکنش به اظهارات مقامات جمهوری اسلامی مبنی بر تعلیق تعهدات تهران در قبال توافق موقت یک ماه پیش، با بی‌اعتنایی کامل اعلام کرد که اهمیتی به این تصمیم ایران نمی‌دهد.
پیش از این، کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه جمهوری اسلامی، شنبه ۲۷ تیر، گفت آمریکا همه تعهدات خود ذیل تفاهمنامه اسلام‌آباد را نقض کرده و ایران نیز اجرای تعهداتش را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77252" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMUFBn7sZKKZiAThI_WDVVWZVJMa3qqlV12iy-A7_UZWKHE5jyV880QJbxTj3rJZp1XrRiwxyPSyg-xTX6dv_flg32284AdZCWqYNa8SD30x7VEVDR3bfpwwzv7r-TL5yNpEdjRZNym-rZpLw09eP9uoq9GnGfuI_T8nBhFevzJqMcRiutzhGkeeVgSAxnQ3v3R8ElG4UK6QZhMOX7aGEtxYNTZ7fHmiP_sIrdaFnX-zD-JxVbHD5fruaS1PcoluTjQ_n9wbZhspuyjvHelLDUFbBxNMxh2aFdcpAJ4ozG9pA8zl7zf1zb_yzFBDXi05RTXvaHS3qpXDllf7a4OcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز به نقل از چند مقام آمریکایی نوشت حمله جمهوری اسلامی به اردن که جمعه به کشته شدن دو سرباز آمریکایی و مفقود شدن یک سرباز انجامید، چهارمین حمله به نیروهای آمریکایی در این کشور طی پنج روز گذشته بود.
به گفته این مقام‌ها، این حملات در مجموع ده‌ها سرباز آمریکایی را زخمی کرده و به تعدادی بالگرد بلک هاوک آسیب رسانده است.
این مقام‌ها گفتند حملات و خسارات ناشی از آنها نشان می‌دهد نیروهای جمهوری اسلامی همچنان ذخایر موشکی قابل توجهی دارند و در عبور از سامانه‌های دفاع هوایی آمریکا نیز ماهرتر شده‌اند.
نیویورک تایمز نوشت اهمیت اردن برای عملیات آمریکا افزایش یافته است، زیرا پنتاگون پیش و در روزهای نخست جنگ، بخشی از نیروهای خود را از بحرین، امارات متحده عربی و قطر به اردن و اسرائیل منتقل کرد.
به گفته مقام‌های آمریکایی، محدودیت‌های اعمال‌شده از سوی برخی متحدان منطقه‌ای آمریکا برای استقرار نیروها و پرواز هواپیماهای آمریکایی بر فراز خاکشان نیز نقش اردن در عملیات واشینگتن را افزایش داده است.
پنتاگون از اظهارنظر در این‌باره خودداری کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77251" target="_blank">📅 01:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeDjQirylhoaoHUdFSGUe9TdBZZcA0oMkcRTNnqxnPvSgBsfHNioN01nj_8XcDeMw9lDFCbos5KWLx9sCRFc0PfPWK8VRzuJHymVanPmSGV-RcGxZMriqi1_xeA9ttWx-_q2eoWpC4lDj5fDf28bG3opVGAR64sC1XVbzjxQKzq2dEle5QUohwVGgejTzpy43_-VYmWeh87c3oJK5LMEcwX_4Hqw8pi3OuH9J50StMtsYBfSATNP0N73hioV0zRxjuVzZ2GyzGaNp6X8hkOMPU-BtBtHbtmkVwoMJWcdcg4ZEUMncof9bXdGWunVzQ8KA6hCNWbjqet8kSudKnqaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، بامداد یکشنبه، ۲۸ تیرماه، زمین‌لرزه‌ای به بزرگی ۳.۷ حوالی سرگز در هرمزگان را لرزاند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77250" target="_blank">📅 00:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چند پیام دریافتی در ساعت ۲۲:۱۳
بندرعباس ۳ انفجار
اقا بندرعباس رو زد
۴ الی ۵ تا
زدن داداااا
بندرعباس
اقا وحید الان بندرعباس زد صدا اومد معلونم نبود کجاس
[ولی فقط همین‌ها بودند و انقدر هم صبر کردم که دیگه پیام‌های دریافتی بعد از انتشار این پست فاقد اعتبار محسوب می‌شن.]
آپدیت:
گزارش خبرنگار تسنیم از بندرعباس:
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس منتشر شد، اما مسئولان استانداری هرمزگان ضمن تایید این صداها می‌گویند هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.
🔹
از سوی دیگر برخی منابع خبری به خبرنگار تسنیم تاکید کردند احتمالا این صداها مربوط به هشدار نیروی دریایی سپاه به کشتی‌های متخلف در تنگه هرمزگان باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/77249" target="_blank">📅 22:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/77727bb200.mp4?token=nO4CXIbA5rqTJ5Rfi_tEr1uPhW0lI7IXOtNEG88Zbs-l1mVQUjW1yWa2hxFnPl8aJivvl4-r0OX1re8zTTEorCod5rde1nWXuUifiG_5u9gRCi5MXaxieriZU4KVJTPHlWmV1lVrj8xF3zLP2VNYhFlwY70LU0hLAlVfcXJXLh14f--KlcVLGsPOt_j-G7LHwtJSPpgBdTMSrlVwqUxgZotCPM87XdeOAnawUzQqxoRMKW1k41pwUbGTNXCAo9wwLt9kn6t18JVwROvo4So5mZ-cF7WcJ05OA7msMWXCt_X_SSoMKXaFT72imw-lT73m7q6_CvWBgQeKHrjjYa7ChA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/77727bb200.mp4?token=nO4CXIbA5rqTJ5Rfi_tEr1uPhW0lI7IXOtNEG88Zbs-l1mVQUjW1yWa2hxFnPl8aJivvl4-r0OX1re8zTTEorCod5rde1nWXuUifiG_5u9gRCi5MXaxieriZU4KVJTPHlWmV1lVrj8xF3zLP2VNYhFlwY70LU0hLAlVfcXJXLh14f--KlcVLGsPOt_j-G7LHwtJSPpgBdTMSrlVwqUxgZotCPM87XdeOAnawUzQqxoRMKW1k41pwUbGTNXCAo9wwLt9kn6t18JVwROvo4So5mZ-cF7WcJ05OA7msMWXCt_X_SSoMKXaFT72imw-lT73m7q6_CvWBgQeKHrjjYa7ChA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توییت، ترجمه ماشین:
این ویدیو لحظه اصابت چند موشک بالستیک ایرانی با برد متوسط تا میان‌برد به پایگاه هوایی موفق‌السلطی در اردن در طول شب را ثبت کرده است؛ حمله‌ای که دست‌کم دو نظامی آمریکایی را کشت و چند نظامی دیگر را مجروح کرد.
sentdefender
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/77248" target="_blank">📅 21:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E2HpnAbRiqEx3c0H2E87kwZJHUDmftJ-DCUqKZRYqq37lb1AjgqO_QyRJePJKPoULFzSLV4D-46Y1fySwkPvyssFkb5uX92VQPGlu-iGshkDtWbgDZWSfxbMNMdz74_923NJyJPCAs3y4qtcaQ_zN14HdCyjqVmpLS6G-u7sv-AV4LIKIC91kRoMSJprVeOwQVgVq7RMhDUBLL-hp9WfaHxbuz1WxMY415c_OwT4fDAXy6L5O6EkYCVwS4_s0dPPdmclwE_8mRxPmrMl_UidFerVXRtPRrErdczso14cfIOpReYJdkH3MocI4rr2kNqILvpQ8Z-m2WUELtAmHVuyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: دو نظامی آمریکایی کشته شدند و یک نفر مفقود است
پست سنتکام، ترجمه ماشین:
بیانیه سنتکام درباره نظامیان آمریکایی جان‌باخته و مفقودشده
تامپا، فلوریدا — در ۱۷ ژوئیه، در حالی که فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای شریک در برابر حملات موشکی بالستیک و پهپادی ایران دفاع می‌کردند، دو نظامی آمریکایی در اردن در جریان عملیات کشته شدند. همچنین، یک نظامی در حال حاضر مفقود است.
چهار نظامی آمریکایی برای دریافت خدمات پزشکی به بیمارستان‌هایی در اردن منتقل شدند. آن‌ها از آن زمان مرخص شده‌اند. سایر نیروهایی که به‌دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به خدمت بازگشته‌اند.
سنتکام از سر احترام به خانواده‌ها، تا ۲۴ ساعت پس از اطلاع‌رسانی به نزدیک‌ترین بستگان، از انتشار اطلاعات بیشتر، از جمله هویت رزمندگان جان‌باخته، خودداری خواهد کرد.
CENTCOM
پیت هگست، وزیر جنگ آمریکا، در واکنش به کشته شدن دو نظامی آمریکایی در حملات جمهوری اسلامی در اردن در شبکه ایکس نوشت: «خدا نگهدارتان، قهرمانان. فداکاری شما فقط عزم ما را راسخ‌تر می‌کند.»
پیش‌تر سنتکام خبر داد دو نظامی آمریکایی روز جمعه ۲۶ تیر در جریان مقابله با حملات موشکی و پهپادی جمهوری اسلامی در اردن کشته شدند و یک نظامی دیگر همچنان مفقود است.
سنتکام افزود چهار نظامی مجروح پس از درمان از بیمارستان مرخص شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/77247" target="_blank">📅 21:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/863eecb938.mp4?token=pKmQXrU4UyjgVkTlTG4RHqArqaHgUBLebwz-6yrU6pjeSutAQXIc_vRiSy-uIvp9U5a0JiPoNTZMZZQSWL6O_9NE4nSlAm0qMghv4dNJBtTFpvTc0G9OC_aWrRYux22L5vARE3DlMwCsGWoGRXppaSG-fFyPxnl1qB-iXHRashGodyHLgfg6PUt9BISnWJs7Gw67Abnfcde-6UK1Ck5M0-hlN5oADnT1MIiMcZ7akW5O5quabRfpJmwetUAYL6JbgoBNVBTEFREZM5_qPy-nHiufLGupmLRU76tWqnWgej6n1XDxyIZdZFYujkpkpga4Lhnt_2RN0X-fT8zbF0YIg1x5hKYFxVHxadnm3vL8x8sA_bGkoJS7XGU6IykqJwxYGdMjdFW5Fii8cXUnPu1cryxYH46Nw7mh21l3BQzor6eCKxNxenDViX6iFSrUAKLbrwfUiGV5Zh8ALQPhDn3xT4EVrbzSt7q5GQOLvwyvghSs9sCuuuI_Ius9rZIQxx3s-jpXZ9ATnE48KyrB7ZylFKymZVZgtnEP_qQfgtRLhO7KM4Cawk9a0Lnyzz4CIlmXyxPTM4j8cz0XQEZVAnKjLxJwRo8E60DTparX24ZOHeRMyQxgtwfjYFMSxRdyFI2AEb9iHFeRkbsdimmtsopKVJVwWIK3DJkxBazhaA5oeAM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/863eecb938.mp4?token=pKmQXrU4UyjgVkTlTG4RHqArqaHgUBLebwz-6yrU6pjeSutAQXIc_vRiSy-uIvp9U5a0JiPoNTZMZZQSWL6O_9NE4nSlAm0qMghv4dNJBtTFpvTc0G9OC_aWrRYux22L5vARE3DlMwCsGWoGRXppaSG-fFyPxnl1qB-iXHRashGodyHLgfg6PUt9BISnWJs7Gw67Abnfcde-6UK1Ck5M0-hlN5oADnT1MIiMcZ7akW5O5quabRfpJmwetUAYL6JbgoBNVBTEFREZM5_qPy-nHiufLGupmLRU76tWqnWgej6n1XDxyIZdZFYujkpkpga4Lhnt_2RN0X-fT8zbF0YIg1x5hKYFxVHxadnm3vL8x8sA_bGkoJS7XGU6IykqJwxYGdMjdFW5Fii8cXUnPu1cryxYH46Nw7mh21l3BQzor6eCKxNxenDViX6iFSrUAKLbrwfUiGV5Zh8ALQPhDn3xT4EVrbzSt7q5GQOLvwyvghSs9sCuuuI_Ius9rZIQxx3s-jpXZ9ATnE48KyrB7ZylFKymZVZgtnEP_qQfgtRLhO7KM4Cawk9a0Lnyzz4CIlmXyxPTM4j8cz0XQEZVAnKjLxJwRo8E60DTparX24ZOHeRMyQxgtwfjYFMSxRdyFI2AEb9iHFeRkbsdimmtsopKVJVwWIK3DJkxBazhaA5oeAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر اعلام شده جمهوری اسلامی، او با اشاره به نقض تفاهم‌نامه میان ایران و آمریکا تاکید کرد که این اقدام بار دیگر «بی‌ارزشی و نامعتبر بودن امضای رئیس‌جمهور آمریکا» را نشان داده است.
مجتبی خامنه‌ای همچنین، آمریکا را به «جنگ‌افروزی» متهم کرد و نوشت: «اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمل هزینه‌های سنگین‌تر و بی‌آبروئی بیشتر است، بداند که ملت عزیز ایران و جبهه مقاومت، درس‌های فراموش‌نشدنی برای او دارد.»
@
VahidOOnLine
متن پیام بنا بر فایل PDF منتشرشده در منابع حکومتی:
پیام رهبر معظم انقلاب درباره‌ی حماسه عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور
بسم الله الرحمن الرحیم
ملت عظیم‌الشأن و شگفتی‌ساز ایران!
سلام و درود و سپاس بر شما که با حماسه‌ی بی‌نظیر و تاریخی خود در رستاخیز بی‌سابقه‌ی بدرقه‌ی آقای شهید ایران، نصاب تازه‌ای از جلوه‌ی بعثت و اراده‌ی مستحکم هویت اسلامی ـ ایرانی را در قدرشناسی، وفاداری، بصیرت، و ابراز محبت فوق‌العاده به زعیم امت اسلامی و رهبر شهید انقلاب ثابت کردید.
گرمای دل‌های گداخته، چشمان اشکبار و عزم‌های استوار جمعیت ده‌ها میلیونی و ده‌ها کیلومتری در تهران، قم، مشهد، و سایر شهرها و روستاها، دوستان ملت ایران و مردم آزاده‌ی جهان را به تحسین و دشمنان مستکبر ملت ایران را به حیرت و سرگردانی و خشم و وحشت انداخت.
همزمان با این حماسه، نقض عهدهای مکرر شیطان بزرگ نسبت به تفاهم‌نامه امضاشده بین رئیس‌جمهوران ایران و امریکا بار دیگر این حقیقت را به همگان ثابت کرد که امضای رئیس‌جمهور امریکا چقدر بی‌ارزش و نامعتبر است و زورگویی، تمامیت‌خواهی و وحشی‌گری، اجزاء لاینفک مرام و مسلک امریکایی می‌باشد. امروز شیطان بزرگ بار دیگر چهره‌ی واقعی و بدون نقاب خود را آشکار کرده تا این تجربه‌ی تاریک از جنایت و بدعهدی، سند محکم دیگری بر دروغگویی، غیرمنطقی و غیرقابل‌اعتماد و پلید بودن امریکا باشد.
اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمل هزینه‌های سنگین‌تر و بی‌آبرویی بیشتر است، بداند که ملت عزیز ایران و جبهه‌ی مقاومت، درس‌های فراموش‌نشدنی برای او دارد که رشادت‌های رزمندگان اسلام و غیرت مردمان شجاع خطه‌ی جنوب در این روزها نمونه‌هایی از آن را نشان داده است.
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدس در همه‌ی سطوح مردم و مسئولان و در تمام عرصه‌ها برای تحقق آرمان‌های بلند انقلاب اسلامی و تأمین عزت و استقلال ایران عزیز خصوصاً در برابر دشمن جنایتکار و حیله‌گر امریکایی است. همان‌گونه که پیش از این مکرراً و مؤکداً تذکر داده شد، صیانت از وحدت و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوت‌های اجتماعی وظیفه‌ی همگانی است و البته نقش مسئولان و عناصر دلسوز و دلباخته‌ی انقلاب و امام و رهبر شهید در انسجام و یکپارچگی کشور، مهم‌تر و حساس‌تر است.
بر این اساس ملت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوه که تلاش ایشان برای رفاه و سعادت ملت، مشهود می‌باشد، همچنان برای تضمین صیانت از منافع ایران اسلامی، هوشیار و فعال در میدان خواهد بود. ممکن است کسانی با اخلاص تمام و از سر خیرخواهی، انتقاداتی نسبت به عملکرد بعضی از مسئولین داشته باشند. به نظر بنده، در عین اینکه این اهتمام و نگرانی ایشان برای نظام همچون اشخاص خودشان، سرمایه‌ی ارزشمندی به شمار می‌آید و فی‌نفسه امری مطلوب قلمداد می‌شود، این عزیزان که بعضی از ایشان از زمره‌ی پیشروان بصیرت هستند باید مراقب باشند تا این رویکرد، اولاً ظلمی را بر بی‌گناهی روا ندارد که آن خود منشأ محرومیت از برکات و عنایات می‌گردد. و ثانیاً موجب شکست در وحدت و انسجام اجتماعی نگردد؛ که با حفظ این جهات، انتقادها موجب رونق و شکوفایی امور خواهد شد.
دشمن نباید هیچ علامت ضعفی و از جمله این ضعف را از ما دریافت کند؛ که هرگاه ما این مراقبت‌ها را به طور کامل مراعات نماییم، او به ناچار رو به هزیمت خواهد گزارد.
بار دیگر از یکایک مردم عزیز که خود، صاحب عزای پدر شهید امت هستند و با وجود دشواری‌ها و برخی محدودیت‌ها و ناملایمات در رویداد عظیم بدرقه‌ی آقای شهید ایران، حماسه‌ای تاریخی خلق کردند صمیمانه قدردانی می‌کنم.
همچنین از مراجع معزز تقلید، علما، اندیشمندان و نخبگان، فعالان فرهنگی، اجتماعی و سیاسی و از اقدامات و تلاش‌های نهادهای کشوری و لشکری و نیز حضور مقامات و نمایندگان جبهه‌ی سرافراز مقاومت و نهضت‌های پرافتخار اسلامی تشکر می‌کنم. امید است همه‌ی کسانی که در این حماسه‌ی تاریخی به هر نحوی حضور و همراهی و همدلی داشته‌اند، مشمول عنایت و دعای خاص سرورمان عجل الله تعالی فرجه الشریف باشند.
سیدمجتبی حسینی خامنه‌ای
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77246" target="_blank">📅 20:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrvsXOCOt4t6kqifUnRBg-WINX3HnR6yadV4D7kUSS_h1S8LEoRFJdDaqvPG2x7yG7rF0gEmdpBBwM6FPaK6HfbpPkMgJ6Q5Ztq02lJDLa39Wjs2uB9GyvihnnL7ep3I2FApVrauemB_HbuuNmoBKOIiEXeHjK27sCValXOLOUqzJln-AqAYWx_fjImCAq40IaPS255fJk9OFRBdYCOWxHV7zbRDAJUCWSM2nDiUK7pl9pbZhwrjb4N0BokIusaIA_YLluvG8ndmEOXsX1_ce0qCpsvSx092iasBWPBz4p4eR4EdzcGOeCjtzhlfD3piUcZI8YJRWjvbLeFVrMKkig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از استانداری هرمزگان خبر دادند طی ظهر تا عصر روز شنبه چند حمله موشکی به حوالی شهر سیریک در نزدیکی تنگه هرمز انجام شده است.
استانداری هرمزگان اعلام کرد: «در ساعت ۱۲:۳۰ و ۱۶:۳۰ و ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.»
در این بیانیه آمده که «هیچ مصدوم غیرنظامی» بر اثر این حملات گزارش نشده است.
سنتکام، ستاد فرماندهی ارتش آمریکا در خاورمیانه، درباره چنین حملاتی به ایران گزارشی اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/77245" target="_blank">📅 19:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oDzExpchaeaAx45v01cK1pTX-GHt77rbdMjzSdg25ppbNP3s89Fx9zjW3aMXMuI3ohLsZQRLouKVLAPNLrx0roh41zu0UmbkxK_lBBQ50AsbdK-27fHi-6eRRfpby4IeKdnTHDyNloOV1_ayQFO-nj7diOGracGoocjz8FaQRK-MqiYkKNpbPWo6LhYpVscr-m2zJs552nMpEYBRccJ7ZbnCnTBg9MBrCKLJUhW4BibiiiTy-KZalApTebMLWI4GJ9dfL_CjJyB4qF29EbIPoETvHcT-uvVE5q8GbgJXmOfJhOl4OL-6W8im-hTIyD9dbEedsYbrORtsZiDPV_xj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FV_-JFEgNahNUZIrdvMCXKdI4Etc2f9TpYjaoUtecJqp5Q2iYTCnkqNX6Ch_yLPVecKnod13A7kfjMI9vD7sCy0MSja1oJOxo4dpgfQTUlvqysRvA_ciaAMcw2Syj6Zb4URVdoNFQIQjmdH3MX4WidHN51ghcSDmQOimT-0WnSlnj92TWC67B1wWbT61VYHbWK1Bp2aSZcyUXRgcrR7UMcps2xNG1_Kvf4skKCxnGFJ-7K-5MRayMMz3x-kgsWWWgD_zowUf3fZFt5IM_u7eKwtnN_mSzTg_89iWlzQgBczuuWUH8zC_eOIdom5UfqlWqNVH8Pl43TAjGqy2A0QzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cgvUcBIYyJtNPIuPSM025BT446ndlvQI5pkyzhxvItEGtBha6U9_A9wDKvfKlBKUPDMMAywD9Ug2maAfTxOeNLsjNTfoxdtNUY835O_rzIhWPt5lNhT-asbdEluVGZn4q9kncBAbwcmhVu_5PFmMCFo91QbBDMJ4eML6fcctnSlgsI9K-OneGdxQhsqNMDZajw9PdjsQBBihppT1YlCj_UW64k0rjXRmZBtIBxCoMEuKrLQSvu0DgjQo_zK3sejf7ZpmsBXk-bul_-G0GQmczSnGxfJ_fGy-XIFVL5lZCKhD9jBVyiD4Ex-elyO3WSqGrUwXk6nhtGc5__OI73JSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZYW_DxE7UKZYSd57OxFwBWkQxUN0JZrew-jsYyV0q-AkK3h-dXukFijkPYTNz25VwGCLjZl-uJjYAu4ACTb7L_7dBkNT3qnr1Tk95YoWQAl0YkF2-dMilA7aQ5wjURt7rY4xASuoT4KZfEAfDh11LCF2hBVxx8-l0rnT4xDAcSfROqL_NsItWspUxtRgJueJoN3BUrGvPnUO1QyYYFg07q8kjN90dNKLdgQSb1xeFqEpWdKQgMjzaTlvFGtI_lq0R1wOHS6tcCik3NWUi2pO7A8OgByDvHSxyZiG_nUjhhQXDv9g1OC-7FAljukWSQocfBRGm97M5nVZDPfNFVQteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KISJL_JBPRfJrA3R_vuqjLGnOuqbZrbEJc4gTfC4AzFQ_uQnoPrrb8f_RCo3XwRPvM4_px3nQMqq22MdRiAd6-1mfUMSNRmOcqyx6ezIf6QBwb3te8f88snn_rlK-92gOnXTLMVeTePqxblULaiPZ4Fxoi11dDztY0os2woEH73c-UuUb99p8quDBT-JgLPgW4RySgFxbWUSSp41WZxQhvc2_E7Dj3tAjAOQN4hTeF8nJ5eif81b21AEGXF5QEmCODWoQAXIaj46ROzIIx2ktxHr1xMGLEw1U1AfLXT8L0zyxUnZkbSvHGuAMbxZN6ayyXqm_DZ-KGcfhRWJRr4T4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jVPz_wolpqTcgpjFRCvHuRg7N0hXyuMt6uNWevjvisqLgGx5z-jSuZANkwUNS56QDYJN4QHJz8Shr_bVx50UQhcMJj0cJGteD9Elf07p5JdUc--cX4fMVSmb6BTskW9F04SIYIUwWJh5Gg9yqJEP8YYkKWHsAHhIbr5t21MwTgHnZ_x9xp8KUTm8T5_INiOvlmH8tjZdRXFYWYlgM4w25Gr_OigHWL72Xzc3lwKgozR-t20ev9lCmC0vYuKhTtDmivHD6es7U8xsREaBRc1VumI7DV7C5c96S3FDL_cZw8pRhJw8gdqJaYCaD-2Lf-NmjDmHQT_Wm_5XDcQ686jkjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارتش جمهوری اسلامی ایران اعلام کرد در ادامه عملیات موسوم به «صاعقه»، پایگاه‌ها و تاسیسات نظامی مرتبط با آمریکا در بحرین، کویت و اردن را با پهپادهای انتحاری هدف قرار داده است.
روابط عمومی ارتش در بیانیه‌ای مدعی شد در مرحله پانزدهم عملیات «صاعقه»، پهپادهای انتحاری «آشیانه هواپیماها، محل استقرار جنگنده‌ها و مخازن سوخت» در پایگاه شیخ عیسی بحرین را هدف قرار داده‌اند. این بیانیه همچنین از حمله به چند پل ارتباطی در بحرین خبر داده است.
ارتش جمهوری اسلامی ایران پیش‌تر نیز در بیانیه‌ای درباره مرحله چهاردهم این عملیات اعلام کرده بود که «چند پایگاه و تاسیسات نظامی آمریکا در کویت و اردن» هدف حملات پهپادی قرار گرفته‌اند.
بر اساس این ادعا، انبار مهمات نیروهای آمریکایی در اردوگاه العدیری، ساختمان‌های ستادی و انبارهای مهمات پایگاه علی‌السالم در کویت و همچنین مخازن سوخت پایگاه الازرق در اردن هدف قرار گرفته‌اند.
ارتش کویت حمله به چند مرکز نظامی و تاسیسات حیاتی این کشور را تایید کرده است.
ارتش اردن اعلام کرد سامانه‌های پدافند هوایی این کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده بودند، رهگیری و منهدم کرده‌اند. به [ادعای] مقام‌های اردنی، این حملات هیچ تلفات جانی یا خسارت مادی به دنبال نداشته است.
@
VahidHeadline
روابط عمومی سپاه پاسداران انقلاب اسلامی، روز شنبه ۲۶ تیر ماه، با صدور بیانیه‌ای اعلام کرد «اسکله پشتیبانی سوخت ناوگان آمریکا در بندر الاحمدی کویت» را هدف حملات پهپادی و موشکی قرار داده است.
بر اساس این بیانیه، در این عملیات «محل تجمع پرنده‌های جنگی» آمریکا در پایگاه شیخ عیسی و «مرکز داده‌های اطلاعاتی در بحرین با عنوان باتلکو» نیز مورد اصابت قرار گرفته‌اند.
در بخش دیگری از این اطلاعیه آمده است در جریان این حملات، «یک مرکز سیگنالی و مخابراتی آمریکا در کویت» نیز منهدم شده است. سپاه پاسداران در این گزارش بر «کنترل قدرتمندانه تنگه هرمز» تاکید کرد.
پیش از این، نیروی زمینی سپاه پاسداران در بیانیه‌ای ادعا کرده بود، مرکز پشتیبانی نیروهای زمینی آمریکا در منطقه عریفجان کویت را هدف قرار داده و این حمله منجر به کشته شدن چند نظامی در این مرکز شده است.
@
VahidOOnLine
وزارت برق، آب و انرژی‌های تجدیدپذیر کویت، روز شنبه ۲۷ تیرماه، اعلام کرد پس از حمله نیروهای مسلح جمهوری اسلامی به یک نیروگاه تولید برق و آب‌شیرین‌کن در این کشور، آتش‌سوزی در این تاسیسات رخ داده و چند واحد تولید برق در پی این حادثه از مدار خارج شده‌اند.
وزارت برق کویت روز جمعه نیز از خسارت و از کارافتادن یکی دیگر از تاسیسات تولید برق و آب این کشور در اثر حملات جمهوری اسلامی خبر داده بود.
@
VahidOOnLine
ارتش کویت در بیاینیه‌ای اعلام کرد از ساعات اولیه روز شنبه ۲۷ تیرماه، موشک‌های بالستیک و پهپادهای «متخاصم» را در حریم هوایی این کشور شناسایی کرده و آنها را رهگیری و منهدم کرده است.
سرلشکر سعود عبدالعزیز العطوان، سخنگوی وزارت دفاع کویت، در بیانیه‌ای که نیم‌روز شنبه در ایکس منتشر شد اعلام کرد «تجاوز» جمهوری اسلامی همچنان ادامه دارد و شماری از تاسیسات نظامی و امنیتی، همچنین زیرساخت‌های حیاتی و غیرنظامی این کشور را هدف قرار داده است.
به گفته این مقام کویتی، این حملات تاسیسات مربوط به بخش‌های نفت، برق و آب را هدف قرار داده و موجب آتش‌سوزی و وارد آمدن خسارت‌های گسترده به شماری از زیرساخت‌ها شده است.
ارتش کویت افزود نهادهای مسئول عملیات اطفای حریق و تعمیرات را آغاز کرده‌اند و در جریان این عملیات، شماری از نیروهای آتش‌نشانی و کارکنان بخش نفت هنگام انجام وظیفه مجروح شده‌اند و تحت درمان قرار دارند.
در این بیانیه همچنین آمده است رهگیری موشک‌ها و پهپادها باعث سقوط بقایای آنها در چند نقطه و مناطق مسکونی شده و خساراتی به اموال وارد کرده است، اما هیچ تلفات انسانی در این مناطق گزارش نشده است.
ارتش کویت در پایان تاکید کرد نیروهای مسلح این کشور با آمادگی کامل به انجام ماموریت‌های خود ادامه می‌دهند و تمامی اقدامات لازم را برای حفاظت از حاکمیت، امنیت و ثبات کشور در دستور کار دارند.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک مقام امنیتی جمهوری اسلامی نوشت اگر آمریکا به زیرساخت‌های غیرنظامی ایران حمله کند، فرودگاه‌های دبی و ابوظبی و بنادر فجیره و جبل‌علی باید فورا تخلیه شوند.
این مقام امنیتی گفت این هشدار با هدف حفظ جان شهروندان در برابر حملات متقابل جمهوری اسلامی، صادر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77239" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ppLKYwnBcV4p4clvzyCvyXRweK4IjVjyf3SAikd6EgCKstdywFRwCYORuHB48Qds7ao_gbaLZ0-dCK4C8Ak2Dp_HybnU_ohzzPNGAwPskAzBzdawGUGq70clBBRvz7sI2FE1fcFBcOV4GCA2eUUPur8YGzat86wZofwg2ydUQB4Fheow2wq90DzyTtf9SywlE1LwWVCYarEnFENZmFJYr6hsnelqGZBPVzc1BO9AB2lt4caKhRq20Mk-tPi4Hcvd0m0SiNbOsArh96Oei_x9iQA51Z-ewG3crjuP4W94iCqinlkofrdKSRwKiQMVm6Lra-a95N5JTRr8ILcnMPI1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NCQM_IwwTrYYyO0xuBzgMUecRhKDFuIQG4Y1esT_PkUDAy7weGH-zd15nmJaU-C07hYQVqGFdTlpsfxiICEDwKCoHPiH8XkCkcTrVsc07CkmJx4UOQUTNyaQ_-C6VtJquBOoZgrIPNPOesY4ewtLyyJ-wTJZdaPVSaXCA6Qh8PN09k43MNC7q6QTTnIMJRq3YhSOKEiiwrjf3FLfg3nEaY0FRay_D7IrlmXrrYEtz4C3HV2ZqvbRBxGj6Hvpk3UIoCD9QJA1JoE_b90Qs_KPKQFVpuGAeC4IRn6OfW4fGnINX9QWupQ56km1-fV1qeQC8cIrsEfiG05fvOTE0Xdz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KTEEgPvrQi4Ec0yqx8L32nY6nR30VX25KKOON1un4OmbRuWVx-tqbFXT2qClj3TuvpCIOpE3J4r4vTYli4U1f-GVmwaMjTeYiy-oGYgmb4CTF5FtKQVHiqr0Oiy35QZYchgS3azLShqkER3DTZofqnndvVdnLcbqNOgtbTQ6FtT4T2zdXB_tWk9ICjCvHAbngBEokZGAGGpSs9xPhlTrOUsYr5eGn4CIKhws1Dx4Wv3JXcSf40CQ9Lgi-OkHPn6noa9B7L-eowySBBPejUl55ItMDTRl7n196oxhil4j9qbZmCeYetl8Prws5lIjKj_LPufRFGwA8sxX9U7Xn3ZiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sW17EBh2j_gbiVZ-5IRDpS58rQTMTEoVB_feCsqe1UkQvYPkXCI9isTPjSTZC1Y7BxV5qxZmEujo0AeUEvYAxx0-Vp7OryjLYACv93m4vaDyeqP-b4qvUHFPDDgrD1AFRVlTMz5AtcKKVxPtK2-zQiMWybFODb6EKfbxMXqqQtDrCdzBKeU3haZXwiUbz58Hil1yRb_0wIVGcM88JEgAkGl_v0BLC_N-qbpWa0PB8DE_LnSI_c-K6ftpNHuf0-Y4ky4HSittoAyji9PF-Vp2IohRhgFfr7LjO4y02A_4jD-OSntDVNRcoxHM7psvvGyptXTth9HnU69TnOHOMELGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H0IZwDaY2yCJHyLRK0FhmKTOXo0LGRQ2jkMelTiZ1vl7qau6RoAo9rp66QDllNwIaRjv_pU8wVJUKK4swZYrd7R3DFVZcmdj3MaQ8SEQsQtovdsBjBEuu1Rnf2h5LW0T4RgusDZ10tfRJvJ502MvNhwHTIMzlJtRFK_FpVSvXNgCsocZYidnzOCUVb98QLFLd0Aobwb7Z6h1JJsty4MWr4ESDrzK6GvgkrG_V1dgUT-UVADfJA_q9tpgt-r4Y2l7JcIiHWnicpasuggVuyRHN3ctxc71MH4GtfFGopRdfPrFqUtB6CS8wm9IEBTMD6SNWY72uM8Qh_DCNAIB96KmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GFT77HSVxU-MQwJQDUmF8zf-2W5pjBg2OkPeV7Pu_GfVTSxH0VKcoTj0aICPqjZzcv_dJ602MS9H9t-holmSMVmUEvAHd1IlpGFRGMHP7wYQmSk5gZv9JTQgqKFXcsbWwYGcYKS1VXPWqJb3VFre9DDIoG6CwsmDp7YTiyIe5kfhFYtIIZU4_bwCOIQhASOOrU_HtC7e_WkgudAGfL1liNK_BdwAr7sjf4rqvCg_0El_LfxU9YOopuEBUatuQTpkZo9o8PrXUbU2ByvHkvgnx1xhImEE0N4MENqBlK7ttIWSk1ZXoQwEBibkbAOje1O0F3_1AMGpnbNCJmtvzI5FYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌زمان با پایان هفتمین شب حملات آمریکا به ایران، مقام‌های جمهوری اسلامی از وارد شدن خسارت به بخشی از زیرساخت‌های حمل‌ونقل، آب و برق استان هرمزگان خبر دادند؛ حملاتی که به گفته مقام‌های محلی، باعث انسداد موقت برخی مسیرهای ارتباطی و اختلال در خدمات‌رسانی شده است.
احمد کرمی‌اسد، رئیس پلیس راهور فراجا، اعلام کرد در پی حملات بامداد شنبه ۲۷ تیر و همچنین حملات چند روز گذشته، بخشی از مسیرهای خروجی استان هرمزگان به سمت استان‌های فارس و کرمان به‌طور موقت مسدود شده است.
به گفته او، پلیس راه و سازمان راهداری در حال تلاش برای بازگشایی دست‌کم یک مسیر عبوری هستند. کرمی‌اسد افزود در حال حاضر تنها یک مسیر فرعی برای تردد خودروهای سواری از بندرعباس به سمت فارس و کرمان فعال است، اما تردد ناوگان سنگین تا اطلاع ثانوی امکان‌پذیر نیست و بازگشایی کامل مسیرها به پایان عملیات ایمن‌سازی و ترمیم زیرساخت‌های آسیب‌دیده بستگی دارد.
استانداری هرمزگان نیز اعلام کرد حملات شب گذشته به چهار نقطه از محورهای ارتباطی این استان خسارت وارد کرده است. بر اساس این اطلاعیه، تونل شهید میرزایی در مسیر رفت و برگشت، پل رودخانه شور در محور بندرعباس–سیرجان و دو پل در محور سه‌راه میناب به سمت رودان هدف حمله قرار گرفته‌اند. استانداری از شهروندان خواسته است تا اطلاع ثانوی از تردد در این مسیر‌ها خودداری کنند.
هم‌زمان، معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از اصابت چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در شهرستان جاسک خبر داد و گفت در پی این حمله، آب چندین روستا قطع شده است. تاکنون گزارشی رسمی درباره میزان خسارت یا تلفات احتمالی این حمله منتشر نشده است.
خبرگزاری تسنیم، نزدیک به سپاه پاسداران، نیز از آسیب دیدن دو پل در محور بندرعباس–رودان و همچنین هدف قرار گرفتن دکل مراقبت دریایی جزیره لارک خبر داده و نوشته است که در این حملات چند نفر کشته یا زخمی شده‌اند، هرچند آمار دقیقی از تلفات ارائه نکرده است.
@
VahidHeadline
مدیرکل ارتباطات هرمزگان اعلام کرد در پی حملات دیشب آمریکا «۱۱۶ دکل مخابراتی» در این استان از مدار خارج شده و ارتباطات مخابراتی در بخش‌هایی از شمال بندرعباس و شهرستان حاجی‌آباد دچار اختلال شده است.
احد قویدل روز شنبه ۲۷ تیر با اعلام این خبر افزود در حال حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که علت آن آسیب واردشده به مسیرهای انتقال ارتباطات در محدوده تونل میرزایی است.
بر اساس این گزارش، «مسیر انتقال دیتا که با کمک فیبر نوری از بندرعباس به سمت حاجی‌آباد می‌رود، شب گذشته زمانی که به تونل میرزایی و پل رودخانه شور حمله شد، دچار مشکل شد».
@
VahidHeadline
سخنگوی وزارت بهداشت جمهوری اسلامی اعلام کرد در حملات هوایی آمریکا از ششم تا ۲۷ تیر، دست‌کم ۵۰ نفر کشته و بیش از ۵۰۰ نفر مجروح شده‌اند.
حسین کرمانپور، سخنگوی وزارت بهداشت گفت پنج زن و دو کودک و نوجوان زیر ۱۸ سال در میان جان‌باختگان این حملات قرار دارند.
به گفته او، ۳۲ زن و ۱۸ نوجوان نیز در جریان حملات مجروح شده‌اند.
سخنگوی وزارت بهداشت افزود ۳۷ نفر از مجروحان همچنان در بیمارستان‌ها بستری هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77232" target="_blank">📅 19:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77231">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lx0CSpboON55JrCCHEvMkVX3-Z88MQC-uzHi9SnHaWo5N5tczvHgbJrQvKhLu7lHY6qWQEJNwYLKP7wgcM_euKbLFnCl2d1AhHAzadf9oCy4LNriJKX45uRnxoq-x3GK_fOXbG2sbgHU_yGpwaYQl2cxxMlRmqyk0cPpXzSng8nJCayEaMaGFslV1nQrSqKTMDRKHsklPeiTPQOJUr8NAxZsd2HlGY2mUfAaEZO-2JfUIzciLltHA0w8bxjSpl6tgX3_g5zBUYOwwpXewqxT8IwyRLhB2x9KQ5cRUkq_nGLmOOaxmgwt1WsI-mbny-xoz0NgcY5hXolU2MxTA_VEHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت آموزش و پرورش اعلام کرد آزمون‌های نهایی پایه‌های یازدهم و دوازدهم در روزهای یکشنبه و دوشنبه، ۲۸ و ۲۹ تیر، در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان برگزار نخواهد شد.
این وزارتخانه روز شنبه ۲۷ تیر دلیل این تصمیم را «استمرار شرایط ناپایدار در جنوب کشور» عنوان کرد و گفت زمان جدید برگزاری این آزمون‌ها متعاقباً اعلام خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77231" target="_blank">📅 19:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cEsdmYC8Pyt9qZi9nYFUCtlP7smAdGHbrz4_K4XgiOOhM3wrJsBR3jHlI8a_aTvt5k1fM0SDz-lEXvtEC-CGX1Mlb4IuwaHYSl3DgHge8Soi5eC1vdjy7fxismgO7EXTXjCz4XHP7eWuEMEVO9ChAAbFzKTGJcz8XwBQjQgDLn-k_70AVLM-NQVdoROFHi-OGRfwb8Fv9y16ex7Oi8RvkDMeZbBx4qGV5fxX5gu3ayZxeBwdaMXzaoW9CD12b6axN2_dJSu7R3FSnAcWSVCJFUUg2qWMOCrwmPDFGE2xJkuVb2rJ5-GEokh5IXmB9bCpHH3Gacprhm0jaDgTIgmmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: پرتاب چند موشک از استان بوشهر
شنبه ۲۷ تیر حدود ساعت ۶:۳۵
Vahid
آپدیت: ساعتی بعد هم کلی پیام و تصویر از امیدیه اومده بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 482K · <a href="https://t.me/VahidOnline/77230" target="_blank">📅 06:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=BrVeeLlSOU20qKwdsydaSjjjSDtXkYgW0BhD-WSjBIh_2HCXAbWvxGJfWreDPDKX8HUug95rwSIxEXRNyVRuzeT97BOoJCUGNXxRDhdPEvOV_O433SA4e0a3eHQ7oQ43FwZp_fav2U91MhwuMjI_jXWdGiJo2MK1_Ou2Rn_F2WGUNqZ3JMPtf2gM7d9oRaQg-ghzWpVtz_5ZoNDjf4qgNLBwxlctpwxPAMfHe7MLz_Heoq3xKM1CqTEPMCB1cKO9iEZUe1abCkfbamOiGaBTCpaPmFhcGAiExt-AlR1HwV9EtOQ6Sg7OCvzPIU8DDX-sEySu0-vT7Kt0jHgP1TTiAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=BrVeeLlSOU20qKwdsydaSjjjSDtXkYgW0BhD-WSjBIh_2HCXAbWvxGJfWreDPDKX8HUug95rwSIxEXRNyVRuzeT97BOoJCUGNXxRDhdPEvOV_O433SA4e0a3eHQ7oQ43FwZp_fav2U91MhwuMjI_jXWdGiJo2MK1_Ou2Rn_F2WGUNqZ3JMPtf2gM7d9oRaQg-ghzWpVtz_5ZoNDjf4qgNLBwxlctpwxPAMfHe7MLz_Heoq3xKM1CqTEPMCB1cKO9iEZUe1abCkfbamOiGaBTCpaPmFhcGAiExt-AlR1HwV9EtOQ6Sg7OCvzPIU8DDX-sEySu0-vT7Kt0jHgP1TTiAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم با انتشار ویدیویی از محل حادثه گزارش داده است که دو پل در محور بندرعباس–رودان هدف حمله آمریکا قرار گرفته و این مسیر آسیب دیده است.
این خبرگزاری می‌گوید که در این حمله شماری کشته و تعدادی نیز زخمی شده‌اند، اما آمار دقیق تلفات و میزان خسارت هنوز اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 476K · <a href="https://t.me/VahidOnline/77229" target="_blank">📅 06:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77228">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A0-uvfE9gjmHiTce_V7R-Toq_hKR8-D740c7uEVK5hc2qysjDqtSko3rJNQ1SJ_A0im669PPRyJiEnu6O1uFLsE9yYbNv6gLw5QpMqrs_vEH9cNqusaPCF9l43h25EvXuKB4DuC9mvWxd_t5za0nMyyMrOwS9ADi4bmdiyCr7gfprXdT4t_NSGqbX3y6bgU_1cpaUeTr6FjSx9OAWiXNY_cd2p_Vs76KFtU2hzciW-KqqmLNYoNSxZF8RcDNHQ93si7oqH4NAQYd0xlpTP8_Lw4C7LaS8DKBB_lwO1zljc6UpDJKqvt44eGlXZjhoGOESdoKbsnhpBTj3ZzhwOmA5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت: نقشه «راه‌های مسدودشده» در نزدیکی تنگه هرمز
شامل دو پل و خروجی تونلی که در حملات هوایی امشب آمریکا هدف قرار گرفتند.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77228" target="_blank">📅 06:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77227">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=FoqnACHPOfNEp53F3K5W6-RgyvZP0dOyVvxYtENyitGfEU4WQT7IEGVYMjCg7i4y5bPff4nSwUimbe8Znc22_rK6F_63KJNRVw7fY1hTK8v_EBf5JsWQu6JMaXLNoXJwveqigfNMVKAVGZhNc6GQYbF2IEyxGFjWZoKI8wShsw7ZkcndTmNhfYU_IhjfTC1iCm3gJLIVUlGWFOUy56xbc730F3EfXAOiOmEFp0qoPYYWeJP7MYVzxb2IqQdQVrLcl7zM685-TwH9Z49I2mTBxllHtNQsg3RkBovmj8alFr0uPzIBNTg9FQxCKfNl0g6JJ9C0fYNj-WqApQs75kUTIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=FoqnACHPOfNEp53F3K5W6-RgyvZP0dOyVvxYtENyitGfEU4WQT7IEGVYMjCg7i4y5bPff4nSwUimbe8Znc22_rK6F_63KJNRVw7fY1hTK8v_EBf5JsWQu6JMaXLNoXJwveqigfNMVKAVGZhNc6GQYbF2IEyxGFjWZoKI8wShsw7ZkcndTmNhfYU_IhjfTC1iCm3gJLIVUlGWFOUy56xbc730F3EfXAOiOmEFp0qoPYYWeJP7MYVzxb2IqQdQVrLcl7zM685-TwH9Z49I2mTBxllHtNQsg3RkBovmj8alFr0uPzIBNTg9FQxCKfNl0g6JJ9C0fYNj-WqApQs75kUTIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین موج حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای آمریکایی در ۱۷ ژوئیه، ساعت ۹:۳۰ شب به وقت شرق آمریکا [۵ صبح به وقت تهران]، به هفتمین شب متوالی حملات علیه ایران پایان دادند.
فرماندهی مرکزی ایالات متحده (سنتکام) تأسیسات نظارتی، زیرساخت‌های لجستیکی نظامی، انبارهای زیرزمینی تسلیحات و توانمندی‌های دریایی را مورد حمله قرار داد. نیروهای آمریکایی علاوه بر دیگر تجهیزات، از جنگنده‌ها، پهپادهای هوایی و ناوهای جنگی استفاده کردند.
سنتکام به دستور فرمانده کل قوا، همچنان ایران را پاسخ‌گو می‌کند و هم‌زمان محاصره دریایی بنادر ایران را به‌طور کامل به اجرا می‌گذارد.
بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه در حال فعالیت‌اند و همچنان هوشیار، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/77227" target="_blank">📅 05:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پیام‌های دریافتی:
انفجار شدید همین الان خرم آباد
خرم آباد لرستان ۴:۵۷ بامداد صدای دو انفجار شدید
سلام وحید انفجار در خرم آباد لرستان خونه لرزید
خرم اباد دوباره صدا اومد ۴:۵۷
خرم آباد دو صداي انفجار پشت سر هم
همین الان دوتا انفجار  شدید خرم اباد
درود وحید جان خرم آباد همین الان دوتا صدای انفجار خیلی زیاد بعید میدونم اینا شلیک موشک باشه
خرم آباد دوتا صدای انفجار
سلام
داداش خرم آباد انفجار نبود
دو مرتبه صدای شلیک موشیک بود
[پیش‌تر پیام‌هایی درباره شلیک از استان بوشهر دریافت کرده بودم.
آپدیت: پس‌تر هم ساعت ۶ از داراب]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77226" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mH783LUSnHCZt-7zY_gOO2ZqNwAdHhePusT0LqdAHv5sNFr43YgN1Yr5cZkBa3hzl5imwL4gSTnjoWaGck9-RMmnMGuEsbVa6dAq-DdO5K_1RQmHmPzN0jlKEAPFnJ0VXeRNlqtnZkK-KnimvkIU8CRvNtwSUmvjoRj-d3OOZ2vEt_gPr-fpWM_6Obt2jdVZEJndjojfKIQUCvzDVLs0Xl2nnjkUmRIm57IsRV-Aned4OTK0jm6EmEeiJKzURIjAuUNbz-PGhPXy7snLddQXpGH3vD3M69OcpNDN-WdEx0rzBrfWHOXcaZ04_OJpiLK30fJClHFHN6ffJPfZr3hy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، خبرگزاری وابسته به سپاه، بامداد شنبه، در جریان حملات موشکی آمریکا به جزیره لارک، دکل مرکز کنترل ترافیک دریایی اداره بنادر و دریانوردی این جزیره هدف اصابت قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77225" target="_blank">📅 04:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77224">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9xu6FmxRW8wnhUAECg-TykrKBloLv-Y4K3MmC5XNPGhYajCtiNpz78W4yXWIQMUIfuxoy402k18FoXR-Lo7dMNSMx_OH32xA57VIVTGnSJ1HTq9I1fmbyCZfgs5LbLkY6EfHJsqUXVxM8ABk4uXBfJ4e7uhTpAI_4LCpNKw6_otYvtfU3UNKUwZdCNMXPzxtqSR4FlgHvrBBajDCEbkM8TxwPhj0gXdETnRYy8fbL2blCFeIF4FWjwrLedO-XbfCPEkOTrJV-Q0D9Gc8IfhCYjaFRLuvkZRTSGH-vu3EoIKIbcy1p4AiN7wKjhdY5bHvIC6dvcXVBKbzT0TFS4vEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است دو نفتکش پس از برخورد با مین در آبراه بین‌المللی تنگه هرمز منفجر شده‌اند.
✅
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران نادرست است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77224" target="_blank">📅 04:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77223">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیام‌های دریافتی از ۳:۵۰:
بندرعباس دوباره چهارتا انفجار شدید بود
باز داره بندرو میزنه
۴تا انفجار پشت هم
هفت تا بندر
بندرعباس کلی صدای انفجار داره میاد
سلام بندرعباس
از ۳:۴۸ تا ۳:۵۰ حدود هفت بار زدن
همین الان انفجار در قشم 3 انفجار پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77223" target="_blank">📅 03:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77222">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرنگار اکسیوس، ترجمه ماشین
:
🚨
مقام آمریکایی: ایران یک موشک بالستیک به‌سوی یک پایگاه آمریکا در عربستان سعودی شلیک کرد
🚨
چرا اهمیت دارد: این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه گذشته است.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77222" target="_blank">📅 02:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77221">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oCbnDv3WopPfvUiqnVPWmdKzavL8trMqLIdfY8piIak2sJCWWZ3gE_MgRLJsL8ArloI9bC4Kdvo-BAgCtz6O8s9vi0XKKTFC-2A5wlEJm1Nyu2amzGslJMYOS2pWG4joO6QMoKWfhZHK9pB64-zV_g-4dgBwYvFq9p0r8JG2O4L03YqFeqKj9t-k4BWSbmXmnGjIdf5S94iBTqNbbyys-ns305EHZIzM0uwwFlfqdyCZjkaLVPgSkFvJonzrUtj-pCwygBV-U8CshilodGU91rFpez6iKdrAUFIyGLtMRN3hwjEiwA9iYoKTULOGFOasiuZwMT2PUCECvf3yKrePsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی با شرح: پل جاده رودان به بندرعباس
شنبه ۲۷ تیر
Vahid
منابع حکومتی:
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب به‌سمت رودان بعد از دو راهی سرزه مورد حملۀ دشمن واقع شده است.
🔸
مردم از تردد در این مسیرها خودداری کنند. تلاش ها برای ایجاد راه کنار گذر و راه‌های جایگزین در جریان است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77221" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77220">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/daa140a498.mp4?token=pbGlOFwFfBk-upge8DtfP4hZIRNpQaG5vegFrKAHOaXjZN8ol6scMavPx3Ob3LdT7WB-2ZhmBHbCAaOQgcGivOWj3itCoNrPwC0JkZTAxpdE3fr4hoQ43G_1pquVdlzA3GMkvdnegZ5xC3V82VTuWncAXUTEIYLf5FW-jeMEvkBE_4qhq_k-XPAAHU0iSC2EhGJyniYTQl0hvAFEkPpJCeapqPkXOXwGJ4bfq1oT5c4u4zja2br7kjDU_LHLgd1wux1rL39D2anumBLwzmRn4VE1_S3KK_mLpHWTa9N8AX9R_KrQmNGKDvyGCsVm5EG0PY6TbeW0SEevvLfXD_t8EA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/daa140a498.mp4?token=pbGlOFwFfBk-upge8DtfP4hZIRNpQaG5vegFrKAHOaXjZN8ol6scMavPx3Ob3LdT7WB-2ZhmBHbCAaOQgcGivOWj3itCoNrPwC0JkZTAxpdE3fr4hoQ43G_1pquVdlzA3GMkvdnegZ5xC3V82VTuWncAXUTEIYLf5FW-jeMEvkBE_4qhq_k-XPAAHU0iSC2EhGJyniYTQl0hvAFEkPpJCeapqPkXOXwGJ4bfq1oT5c4u4zja2br7kjDU_LHLgd1wux1rL39D2anumBLwzmRn4VE1_S3KK_mLpHWTa9N8AX9R_KrQmNGKDvyGCsVm5EG0PY6TbeW0SEevvLfXD_t8EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
شلیک از خرم‌آباد و زیر ۵ دقیقه بعدش ۲ تا انفجار
وحید جان صدای دو انفجار در خرم‌آباد
زمین کامل لرزید صداش هم مثل ترکیدن بود
تو کانال استان زدن شلیک موشک نمیدونم صحت داره یا نه
خرم آباد زدن
دوتا شد دوبار انفجار ساعت ۲:۱۵ دقیقه خرم آباد
وحید جان خرم آباد ساعت 2:15 وحشتناک زدن
سلام وحید همین الان خرم اباد۲ صدای انفجار اومد
همین الان ساعت 2:15 خرم آباد دوبار صدای انفجار اومد
خرم آباد۲.۱۶دقیقه انفجار
۲ و ۱۵ خرم آباد صدا انفجار اومد
خرم اباد چند بار صدا انفجار اومد
سلام آقا ما خرم آبادیم مارو همین الان دو بار زدن صدا انفجار اومد
سلام همین الان خرم آباد صدای انفجار
سلام ساعت دو پانزده دقیقه خرم آباد صدای دو انفجار
۲:۱۶ صدای انفجار خرم آباد
خرم آباد ساعت ۲:۱۷  دوتای صدای انفجار  اومد
خرم آباد دوتا انفجار پشت سر هم ساعت ۲:۱۴ صبح
همین الان سه بار خرم اباد صدای انفجار اومد
دوتا زدن تو خرم آباد لرستان خیلی سنگین بود
سلام خرم اباد ۳تا انفجار داد ساعت ۲:۱۵صدا خیلی دور احتمالا پادگان امام علی
[ساعت ۳ هم چند پیام دیگر دریافت کردم.]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77220" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62a2ad38dd.mp4?token=WK87LnmMFxTkgqaz-6ydKwVgSkjgNIkKXx547HXAL0OrP0VvqIHNWOJjl31vyPDaY9zjx6tyJWXjP9L-Bn3q97bt0B-AeO1lTObXw-kLIJQXJyfTRiw2-KKdILHG7Pc5OWTnCLrAZdjOEaoWBtLKmCMlKg_SIDpbWxCdBt9Wqk-KT-GwsNyZwR8fJ6ZuAET8OFl76DE1kq1l7NcJc2opgL89lMQJJxO3EopuZamwOBrGJPNYtJEiqgEWJ8FbZ99kuylQqAV_pzZq5WNbUtPfmu1-q00r8dzqnwWCHt6J5lGAWysLc4j8OTssXGHaZUJQCPwLRmk-9vBGKMc6rCAb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62a2ad38dd.mp4?token=WK87LnmMFxTkgqaz-6ydKwVgSkjgNIkKXx547HXAL0OrP0VvqIHNWOJjl31vyPDaY9zjx6tyJWXjP9L-Bn3q97bt0B-AeO1lTObXw-kLIJQXJyfTRiw2-KKdILHG7Pc5OWTnCLrAZdjOEaoWBtLKmCMlKg_SIDpbWxCdBt9Wqk-KT-GwsNyZwR8fJ6ZuAET8OFl76DE1kq1l7NcJc2opgL89lMQJJxO3EopuZamwOBrGJPNYtJEiqgEWJ8FbZ99kuylQqAV_pzZq5WNbUtPfmu1-q00r8dzqnwWCHt6J5lGAWysLc4j8OTssXGHaZUJQCPwLRmk-9vBGKMc6rCAb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر پیام‌های دریافتی گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند: 'پل گلوگاه بعد گنو
#بندرعباس
و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
شنبه ۲۷ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77219" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/087c286f67.mp4?token=AbBR1N5xRKsvMf1H7PyrjySMFDlynPn_njKiKWyGVjlBRtXHcBfy7N_K0v368NmJzFDMAbApk9aIA40ozZIRfGLM5sTZNQWD8el1XuydICQYS0eb-mh3V6qRO5vSqr_rNTIlhZD7eiD1qIAjm5pdM1tRh3mQRcE1up0SR1ZrMRdKbd70IMw8f0sQ76vlh0Cy0FdMzusBjxioi37WHhg2yyiiSKTtlBNf8AcBcb-q3Vd8qVZ65kUzAwoS63s1ZkaQjyIGZcUAwEkfpkNI8h576Sd39bqpsvyWRqouwTjT6lKQoIvZXxxb5SehKsU0quApjOCcUfRoPfSt9qphydb3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/087c286f67.mp4?token=AbBR1N5xRKsvMf1H7PyrjySMFDlynPn_njKiKWyGVjlBRtXHcBfy7N_K0v368NmJzFDMAbApk9aIA40ozZIRfGLM5sTZNQWD8el1XuydICQYS0eb-mh3V6qRO5vSqr_rNTIlhZD7eiD1qIAjm5pdM1tRh3mQRcE1up0SR1ZrMRdKbd70IMw8f0sQ76vlh0Cy0FdMzusBjxioi37WHhg2yyiiSKTtlBNf8AcBcb-q3Vd8qVZ65kUzAwoS63s1ZkaQjyIGZcUAwEkfpkNI8h576Sd39bqpsvyWRqouwTjT6lKQoIvZXxxb5SehKsU0quApjOCcUfRoPfSt9qphydb3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از تبریز کلی پیام فرستادند که دو موشک شلیک شده.
و مطابق معمول از ارومیه و خمین و خرم‌آباد زنجان و داراب و... جاهای دیگری هم پیام‌های مشابه میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77218" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77217">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر سه تا
شد پنج تا صدا
بوشهر زدن الان ۲؛۳
بوشهر - دو انفجار مهیب با فاصله ی زمانی ۵ ثانیه ۲:۰۴
سومین انفجار مهیب ۲:۰۵
چهارمین انفجار در فاصله ای دورتر ۲:۰۶
سلام اقا وحید بوشهر ساعت ۲:۰۶ صدای انفجار شنیده شد
وحید جان همین الان بوشهر پایگاه زد صدای سه انفجارپشت سرهم
سلام وحید جان همین الان چغادک را زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77217" target="_blank">📅 02:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سپاه: دو  کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند
منابع حکومتی:
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
🔹
ملت قهرمان و بصیر ایران اسلامی؛
حضور شما در صحنه و حماسه آفرینی خیابانی شما، همانگونه که قائد شهید امت فرمودند سوخت موشک‌های رزمندگان اسلام و دعای شما تضمین پیروزی‌های درخشان آنهاست.
🔹
ساعتی پیش دو فروند کشتی نفتکش که با فریب سازمان‌های جاسوسی آمریکا قصد عبور از مسیر مین گذاری شده جنوب تنگه هرمز را داشتند، منفجر و دچار حریق گسترده شدند.
🔹
نیروی دریایی سپاه با قاطعیت اعلام می‌دارد تنگه هرمز به خاطر شرارت‌های ارتش کودک‌کش آمریکا به شدت ناامن و به طور کامل بسته است و تا زمانی که تجاوزات آمریکای جنایتکار پایان نیابد، امکان صدور کود شیمیایی و حتی یک قطره نفت و گاز از این منطقه وجود ندارد.
🔹
شناورها برای حفظ سرمایه و مهمتر از آن جان خود فریب نخورند و وارد مسیر مین‌گذاری شده نشوند.
و ماالنصر الا من عندالله العزیز الحکیم
پیش‌تر:
🔹
سپاه: لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77216" target="_blank">📅 01:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58eec30bb8.mov?token=aM-hagzwT9jMLtm281V21gukO3LRZdt8hFQCiAFMC4rFQFt0Cgs1WA3Tvt1lm2D1_5LP1sDEDCvgWErsECANNA7fPJMw0B-Y8R9X3XRM3PIL47WC7bKAjgq9itvZ3NheBEeV6RcXgsy2d9kgXgshcfV9lZeebt1dgRsUVATbmR4LSRoLvQSQ87hzm72exizmVitXRx76P-mYSmLLMEltWLrbqXKm_Y9HQDA4Kx7A0WOiS2IQDthcpbIRQpEu79h3iLRmKN54nw9agyH-x_n4X4eDEbDbu_ujD3UPimmVbAqlkHVNbqZOIVtWNwnNsZKGq6OyqLuphLv9YT_RqLLuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58eec30bb8.mov?token=aM-hagzwT9jMLtm281V21gukO3LRZdt8hFQCiAFMC4rFQFt0Cgs1WA3Tvt1lm2D1_5LP1sDEDCvgWErsECANNA7fPJMw0B-Y8R9X3XRM3PIL47WC7bKAjgq9itvZ3NheBEeV6RcXgsy2d9kgXgshcfV9lZeebt1dgRsUVATbmR4LSRoLvQSQ87hzm72exizmVitXRx76P-mYSmLLMEltWLrbqXKm_Y9HQDA4Kx7A0WOiS2IQDthcpbIRQpEu79h3iLRmKN54nw9agyH-x_n4X4eDEbDbu_ujD3UPimmVbAqlkHVNbqZOIVtWNwnNsZKGq6OyqLuphLv9YT_RqLLuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پیام‌ها میگن در بندرعباس صدای پرواز جنگنده و انفجار می‌شنوند.:
صدای جنگنده بندر
لرزش و صدا انتجار هم  میاد
وحید جان الان سمت بندر رو زدن
بندر عباس دوتاشو شنیدم
۴ صدای انفجار بندرعباس
سلام سه انفجار بندرعباس
صدا جنگنده هم میاد
بندر داره میزنه
سه بار پشت سر هم
4 صدای انفجار بندرعباس
ساعت ۱:۰۵ صدای انفجار بندرعباس
تا الان دو سه تا دیگه اومد
تک انفجار با صدای کم، شاید بندعباس بوده، توی قشم-طولا حس شد ساعت ۱:۰۸
صدای جنگنده بندرعباس
بندرعباس ٥ تا انفجار جنگنده خيلى پايينه
بندرعباس به شدت صدای جنگنده 1.11
ساعت 1:11  صدای جنگنده اسمان بندرعباس ارتفاع پایین
صدای جنگنده میومد بعد از ۲۰ ثانیه صدای انفجار اومد بندرعباس
سایت موشکی خورگو بندرعباس رو‌ زدن ۳تا انفجار بزرگ با جنگده
بندرعباس ساعت ۱:۰۷ صدای انفجار شنیده شد
🔄
این بار پیام‌ها رگباری بودند نه پراکنده:
بندرعباس همین الان انفجار وحشتناک
وحید جان اینجا رو وحشتناک زد بندرعباس
بندرعباس ساعت 01:16 صدای انفجار شدید
انفجار سنگین منطقه ۴ بندرعباس ۰۱:۱۶
بندرعباس دوتا انفجار شدید الان به جز دوتای قبلی
سلام شبتون بخیر آقا وحید
الان صدای انفجار بدی آمد طوری که پنجره ها لرزید
همش صدای جنگنده تو اسمانه
بندر عباس همین الان چند صدای انفجار ۱:۱۵
سلام بندرعباس همین الان صدای یه انفجار شدید خیلی نزدیک بود که همچی لرزید
😭
این شدیدترین صدایی بود که بعد از آتش بس شنیدم
زددد الان زد بندرعباس
سلام وحید جان همین الان ساعت ۱:۱۶ دقیقه ی انفجار شدید  بندرعباس نزدیک پیامبراعظم که خونه ها لرزید
سلام وحید بندرعباس ساعت ۱:۱۶ دوتا انفجار شدید صدای جنگنده هم خیلی میاد
بندرعباس اول صدای جنگنده میاد بعدش انفجار ده دقیقه پیش اینا سه تا با هم زدن چهارمی رو با فاصله ولی شدت خیلی بیشتر زدن چند دقیقه بعد دوباره صدای جنگنده و پنجمی
الانم دوباره داره صدای جنگنده میاد یه بیست سی ثانیه دیگه میزنن
بندرعباس الان بالای ده دقیقه چند جنگنده روی شهر می چرخند
🔄
همین الان ساعت ۱:۱۹ زد بندرعباس
بندرو رگباری میزنهه
برای بار نمیدونم چندم صدای انفجار
انفجار دوباره پشت هم بندر عباس
بندرعباس الان زد وحشتناک
همین الان ۱:۱۹ دوتا صدای انفجار شرق بندرعباس
زدن وحید بندرعباس ۱و ۲۰
الان دو تا صدا انفجار اومد
سلام وحید جان دوباره صدای انفجار دوتا
بندرعباس ۱:۲۰ دقیقه صدای خیلی زیاد انفجار
قشم همین الان صدا انفجار شدید اومد
سلام  وحید بندرعباس ۱:۲۰ فرودگاه انفجار بزرگ از سمت فرودگاه
بندرعباس الان ۱:۱۹ دقیقه صدای انفجار بلند اومد. قبلش هم جنگنده داشت می‌چرخید.
بندرعباس دوباره زدن
فک کنم تپه الله اکبر دوباره
خیلی شدید بود از دیشب هم بسیار بلندتر 1:16
زدن وحید بندرعباس ۱و ۲۰ پایگاه هوایی
همین الان سمت مسکن مهر طرفای بلوار هرمزو زدن صدای خیلییی شدیدی داشت خونه لرزید
سلام آقا وحید من از داراب فارس پیام میدم تو آسمون داراب هم امشب مدام صدای جنگنده میاد
من بندرعباسم صدای بدی اومد ما محدوده بهشت بندر هستیم
وحید صدای جنگنده در بندرعباس قطع نمیشه خیلی پایینه پشت سر هم صدای جنگنده
دکل مخابرات رو تپه الله اکبر رو امشب یه موشک خورد توش همین الان
برعکس دیشب که ۵تا زدن
منابع حکومتی:
استانداری هرمزگان: در ساعت ۰۱:۲۰ نقطه‌ای در بندرعباس مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77215" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77214">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3939b6f6d.mp4?token=UX38Dz8yaWZdA2e9wcNtmV5SgeYKQ5bgJbSDbxglwN6KQmLG4iZPLCtEIKuaJMYhwzWkgiJIe-XHrrDlUxDPY9zxpqPcAjzbeFTD29k1x5hYYzxCaifq_O11-EWGkPbXN9EXBGLV7DMHpZHJaHI2xIZO_i889Ze4XkwxutkqvnKqRykWwBkCVq_Hw9Y9xIKcbO7fKZF3Dk78etKPHCYqSv6XhreKiuLnyosL_z9tmGrD6Mb-e7eM893-AoF16dxIAVDDmgO3qXoWRJ9CX2lmmzvfY3AhL9Pp-qyAWrpGBs6S9ANqz-mo4TX529ouxl4kXoId2z7CvRBPjrtcNjhaRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3939b6f6d.mp4?token=UX38Dz8yaWZdA2e9wcNtmV5SgeYKQ5bgJbSDbxglwN6KQmLG4iZPLCtEIKuaJMYhwzWkgiJIe-XHrrDlUxDPY9zxpqPcAjzbeFTD29k1x5hYYzxCaifq_O11-EWGkPbXN9EXBGLV7DMHpZHJaHI2xIZO_i889Ze4XkwxutkqvnKqRykWwBkCVq_Hw9Y9xIKcbO7fKZF3Dk78etKPHCYqSv6XhreKiuLnyosL_z9tmGrD6Mb-e7eM893-AoF16dxIAVDDmgO3qXoWRJ9CX2lmmzvfY3AhL9Pp-qyAWrpGBs6S9ANqz-mo4TX529ouxl4kXoId2z7CvRBPjrtcNjhaRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: سمت نیروی هوایی
#لار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77214" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77213">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O33OTY0AS8O-l4_4vg7ksqWX567gpiHIa1roFUcTZymyh1Dfk1JRcQTDfdeLJbN0X8rZm8LlB2eQrfpg2xdYK8bLiqhBz8DgdGQXdGRONqtbEJz48etcPQ1n7RdsYmDge-a1fz5kJHGE7TFGoq75yFrNdRzQC0PN6gTea7l1tI_OljwYfJUYBoqB-XxbkxNiu98tcRlvgTsHtOU0sdm38ZvN_CbNS6pW88DJthyA1Khvjjdg-vCTaHAa_BGGgiVqULjhlpkZQXGkZmANVbTvJ13TIiMx5QM-iblv_5icQg_JdG7v9ewBrkjCtkR9av_4z0PU-9gM0BVsghQnwkH3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
۱۲:۳۰ اهواز رو زدن
صدای انفجار ولی زیاد نزدیک نبود
اهواز رو زدن 00:31
اهواز صدای انفجار ۱۲:۲۹
ساعت  ۰۰٫۳۰  اهواز  ۲ تا انفجار  پشت سر هم
منابع حکومتی:
معاون امنیتی انتظامی استانداری خوزستان: دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77213" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77212">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=pwvldNnS1NTSnAGaOEjqnUpTS7E-Dtbl9J6RFx7NrDsqxrOHZZx5QIOfNxGsgYUW_uKYY7gT6vsPDZln04CGWTXPpAc4-1H1F6kAT75m128PsyzjbrucSJ0ttE2Nuxo5pEX_cjhAkwmVUMTwAe30g4vPBad05plm7E-vO1sXWIFwqQxJrrqweSyq7-kJRtrdr7W6W3fzvNMPbUlMQQP9LPEn4PmDBFYuVeusSQXcr8-PoHmsxXjrtGHp-bl2Lgi5sOwpe8-b0LTVOURfOyJmNKdnIKHwPqnp5de_x1ikQRgh7YwXOuFl_fyCaHahk5kBrffAZZBdE7BxbQTT78Zguw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=pwvldNnS1NTSnAGaOEjqnUpTS7E-Dtbl9J6RFx7NrDsqxrOHZZx5QIOfNxGsgYUW_uKYY7gT6vsPDZln04CGWTXPpAc4-1H1F6kAT75m128PsyzjbrucSJ0ttE2Nuxo5pEX_cjhAkwmVUMTwAe30g4vPBad05plm7E-vO1sXWIFwqQxJrrqweSyq7-kJRtrdr7W6W3fzvNMPbUlMQQP9LPEn4PmDBFYuVeusSQXcr8-PoHmsxXjrtGHp-bl2Lgi5sOwpe8-b0LTVOURfOyJmNKdnIKHwPqnp5de_x1ikQRgh7YwXOuFl_fyCaHahk5kBrffAZZBdE7BxbQTT78Zguw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
وحید یزد الان 12:30صدای انفجار میاد
5 مرتبه صدا اومد
من تفت از یزد هستم
تا الان ۵ تا صدای انفجار شنیدم ولی دوره
۵ انفجار شدید پارک کوهستان یزد
یزد الان ساعت ۱۲ و نیم چندین صدای انفجار
وحید جان یزدو بد زدن چهار بار
سلام وحید دارن یزدو میزنن
وحید یزد چند تا صدای انفجار اومد ۱۲:۳۰
صدای ۵ انفجار پیاپی در یزد ۱۲:۲۹ تا ۱۲:۳۰ بامداد
من 4 تا صدا شنیدم
یزد ساعت ۱۲:۳۰
بیش از سه بار صدای انفجار اومد و زمین لرزید
وحید یزد رو زدن، ۴ تاشو من شنیدم، اخریش شدیدتر بود.
آپدیت:
منابع حکومتی:
معاون استاندار یزد: حملات آمریکا به خارج از شهر یزد بود
🔹
نیمه شب با حمله جنگنده‌های آمریکایی، صدای پنج انفجار در خارج از شهر یزد شنیده شد.
🔹
پنج موشک در حاشیه شهر اصابت داشته که تاکنون هیچ‌گونه خسارت جانی در پی نداشته است.
🔹
اکنون آرامش برقرار شده و دیگر صدای جنگنده‌های متخاصم شنیده نمی‌شود و آسمان یزد کاملاً امن است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77212" target="_blank">📅 00:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=fp1iFweeZOP7keO11NhAyLZfEl8_XeZBCSzj-DemLXl1wTTbv_qAELuOKw6TPOlOb-1wscDJDH0CUBSAElbiipm_ImwnVw5z0qEZWmuy_KTlRrpBVgAgmr9rrh28IAwWSRLFP89EPZz1j1clcnatsK83I1yQ9yQUlZ5nrHt-fGurTHtopEDV2mLbhgVkE9GzzEd2_PFVOg_NQKMKW5kd1u0h0i4NfRs-CH-g426-RldKXsD-dC0CsgqbIn5ikNkHm4iHx3cCxh7EbBzccPIMbmWRMHenEILZGkSACiNHWLnbD6Od16oE93nVKb5jgsh9WdA13LutPIvx1wHs3RfS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6f0dabd88.mp4?token=fp1iFweeZOP7keO11NhAyLZfEl8_XeZBCSzj-DemLXl1wTTbv_qAELuOKw6TPOlOb-1wscDJDH0CUBSAElbiipm_ImwnVw5z0qEZWmuy_KTlRrpBVgAgmr9rrh28IAwWSRLFP89EPZz1j1clcnatsK83I1yQ9yQUlZ5nrHt-fGurTHtopEDV2mLbhgVkE9GzzEd2_PFVOg_NQKMKW5kd1u0h0i4NfRs-CH-g426-RldKXsD-dC0CsgqbIn5ikNkHm4iHx3cCxh7EbBzccPIMbmWRMHenEILZGkSACiNHWLnbD6Od16oE93nVKb5jgsh9WdA13LutPIvx1wHs3RfS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'حمله به سایت موشکی در جاده گراش
#لار
'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77211" target="_blank">📅 00:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
پیام ساعت ۰۰:۰۷: لار داره پشت سر هم صدای انفجار میاد
سمت جاده گراش
حدود ۱۴ تا صدای انفجار
سلام اقا وحید الان لار دوبار صدای وحشتناکی اومد فک کنم سایت موشکی رو زدن
سایت موشکی لار [رو ] ‌بیشتر از ۱۰بار زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77210" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
سنتکام امروز ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ به وقت تهران]، برای هفتمین شب متوالی دور تازه‌ای از حملات علیه ایران را آغاز کرد. این حملات به دستور فرمانده کل قوا و با هدف ادامه تضعیف توانمندی‌های نظامی ایران انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/77209" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77208">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae40102b43.mp4?token=AAQlorqTCpS8b5BlKw9yCVzhFOdI3b6t4n1l_DEM5hQszVtW4TaPdYzK-8BNqt0a0QIYtyFEYqr3rJPFi2FTXQE44u3z9TfhNwexULOmWKR8ba4B3GR21FSp4M76HlDABNWcuQQBBhn5gO1s7aM-5BkzaM7GHB5Oww_lw67cwsHjT3ny4KYOJESQPUkXUhTO5ktVBs5q9A9lgrEPwb9GocE56X1nHtVn288JhvfQPPc4gOtzUpmSRJsIGIKJjHqAOFm-RiOpF2MUtNr-ySzC38ibRxm4yzzR3IlUQQSHNWOtJLMyF8HSAcGi7nKnrW5RgkB_aOXuFZP53JCkxfs9og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae40102b43.mp4?token=AAQlorqTCpS8b5BlKw9yCVzhFOdI3b6t4n1l_DEM5hQszVtW4TaPdYzK-8BNqt0a0QIYtyFEYqr3rJPFi2FTXQE44u3z9TfhNwexULOmWKR8ba4B3GR21FSp4M76HlDABNWcuQQBBhn5gO1s7aM-5BkzaM7GHB5Oww_lw67cwsHjT3ny4KYOJESQPUkXUhTO5ktVBs5q9A9lgrEPwb9GocE56X1nHtVn288JhvfQPPc4gOtzUpmSRJsIGIKJjHqAOFm-RiOpF2MUtNr-ySzC38ibRxm4yzzR3IlUQQSHNWOtJLMyF8HSAcGi7nKnrW5RgkB_aOXuFZP53JCkxfs9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، بهمن ۱۳۸۹:
حکومت وراثتی بود. یکی می‌مرد، یکی را به جای خودش معین می‌کرد. مردم هیچ نقشی نداشتند؛ می‌خواستند، نمی‌خواستند، ناچار باید قبول می‌کردند
hafezeh_tarikhi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77208" target="_blank">📅 23:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d59582925b.mp4?token=dg7Pa5YaLDc-yBP-Ro3sA7IwkH96LKItck3-FqL5NBoUJsp2pokRIDTnf_m8-indjS9PGgXIS26noVP1OxnkUAmiNBc3ZCAa44s6igeYBkl8FD4OtwUHbQEMAWAb55fwlcjMlKoIcNzrUW3KBseYfvTw5Bf0v7BkuLHQW0zD1sXZZIuB0SjBJHR_L5Qmn1Y2DPVVuWA2sNwteZqm2iQbVrFVXcbwRHXTMboxP3G7eLHmXYwsRCXZl2VSgI_wHIARZTIFY6pUp9tofLCrS9Q9msloEoGRV0ezlUsUtgg1ApAuvdGH1hVHh_4xZPSw5osqXPjajDAXWZagsdccrlSdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d59582925b.mp4?token=dg7Pa5YaLDc-yBP-Ro3sA7IwkH96LKItck3-FqL5NBoUJsp2pokRIDTnf_m8-indjS9PGgXIS26noVP1OxnkUAmiNBc3ZCAa44s6igeYBkl8FD4OtwUHbQEMAWAb55fwlcjMlKoIcNzrUW3KBseYfvTw5Bf0v7BkuLHQW0zD1sXZZIuB0SjBJHR_L5Qmn1Y2DPVVuWA2sNwteZqm2iQbVrFVXcbwRHXTMboxP3G7eLHmXYwsRCXZl2VSgI_wHIARZTIFY6pUp9tofLCrS9Q9msloEoGRV0ezlUsUtgg1ApAuvdGH1hVHh_4xZPSw5osqXPjajDAXWZagsdccrlSdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، در صدا و سیما گفت: اگر آمریکا دو سه روز دیگر به حملات خود ادامه دهند، وارد فاز تهاجم و انهدام کامل خواهیم شد و هیچ مرز سیاسی‌ای برای حملات خود نمی‌شناسیم.
او ادامه داد سیاست «هم جنگ، هم مذاکره» به طور کامل پایان یافته و اکنون راهبرد ما بر پایه بازدارندگی، مقابله به مثل قاطع و پاسخ «چشم در برابر چشم» به حملات موشکی دشمن استوار است و ما موشک در دهان دشمن می‌زنیم.
@
VahidOOnLine
مشاور نظامی رهبر جمهوری اسلامی می‌گوید هم اسماً و هم عملاً چیزی به نام تفاهم‌نامۀ اسلام‌آباد دیگر وجود ندارد.
محسن رضایی گفت که پیشبینی می‌کند که اگر مذاکرات شروع شود طرف مقابل قصد دارد «اصلاحاتی در متن ایجاد کند و در واقع تفاهم‌نامۀ جدیدی بنویسند». او در ادامه گفت که اوضاع تغییر کرده و چنین چیزی ممکن نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77207" target="_blank">📅 23:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77206">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c044eb7a7e.mp4?token=vJqZcmHUSO1Wimo7KUWZy7Zl9yMNW7bBZ5LnPHFaJIkpJ_Y3ZpYu2jS2EqEejcwXaJ9ut7o7dPH04ajHrOYPrvsMdXUVnPTan2s9nGn6_mKevF1mTZRl0G7TKGuOBbrAdZzLqwnhgJnAIFlpYLjZq-Pzu7jDVlaYpjKF6jTNFtRa8EJG8HB3G2gIyIjG9wfVaCrZBqLYo7IRBZVVe1YUVnkKET-ggD9OVs6bsa3EuNpEfe-rLO2J3bHOzUM-mU0K7aueOx9fBjiUnOA-BvkRtBnQ1NrLvoEvv_O27tdNwWb8bKP-gouBC1U70lL4dB6w0Hp5Ffx8nQSsX34LW3peZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c044eb7a7e.mp4?token=vJqZcmHUSO1Wimo7KUWZy7Zl9yMNW7bBZ5LnPHFaJIkpJ_Y3ZpYu2jS2EqEejcwXaJ9ut7o7dPH04ajHrOYPrvsMdXUVnPTan2s9nGn6_mKevF1mTZRl0G7TKGuOBbrAdZzLqwnhgJnAIFlpYLjZq-Pzu7jDVlaYpjKF6jTNFtRa8EJG8HB3G2gIyIjG9wfVaCrZBqLYo7IRBZVVe1YUVnkKET-ggD9OVs6bsa3EuNpEfe-rLO2J3bHOzUM-mU0K7aueOx9fBjiUnOA-BvkRtBnQ1NrLvoEvv_O27tdNwWb8bKP-gouBC1U70lL4dB6w0Hp5Ffx8nQSsX34LW3peZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار ویدئویی‌هایی از قرارگاه سپاه پاسداران در راسک نشان می‌دهد که در پی حمله هوایی آمریکا، سقف یک سوله بزرگ در این مجموعه به شدت آسیب دیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77206" target="_blank">📅 20:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HP400d-Kd__EfwPoWXQ2OLTdJdjcnxEnhtIZnnzKkkJ7ChDZqutRLGvf_ycJz5MELXkxVBiBFAQUauRfX-0LwVAV0B5CWBgmCOpGtszbSyRG8cRRgAd8tasEiKjkS1MIkus3RpGyFXfcaxP2_DQWKTXndTrjrd3dLxTnjH61Z6bemer_M0iFDzTVsntx9p-Ju27pR56pd2et0e8NbIwuZ_AkYbR-JYQkN0F0cVB0tK306gsl3ToOQhH0pj-sE-OBXnI0_4ubRi_X9Q33jHdjMTSmM0PmGPTa1kiM4zbWG39ugqv6N1b7pUeqcJ6BJe8nLYeHdhSbHLpih5wj-Lpzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس روز جمعه به نقل از سه مقام آمریکایی و اسرائیلی خبر داد دولت دونالد ترامپ به اسرائیل اطلاع داده که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند دیگر هواپیمای سوخت‌رسان را به این کشور اعزام می‌کند.
بر اساس این گزارش، سه‌شنبه این هفته در نشست «اتاق وضعیت» کاخ سفید، چندین طرح جدید نظامی به رئیس‌جمهور آمریکا، ارائه شد و او در حال بررسی اجرای یک «حمله گسترده» علیه ایران است؛ حمله‌ای که دامنه آن از حملات کنونی در اطراف تنگه هرمز «فراتر» خواهد رفت.
اکسیوس می‌گوید «زیرساخت‌های ایران مانند نیروگاه‌های برق، انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف دفن هرچه عمیق‌تر ذخایر اورانیوم غنی‌شده، و همچنین بمباران سایت زیرزمینی کوه کلنگ‌گزلا که گمان می‌رود یک تأسیسات هسته‌ای در حال ساخت باشد»، ازجمله گزینه‌های در حال بررسی در دولت آمریکا است.
دونالد ترامپ روز ۲۲ تیر در یک مصاحبه گفته بود که ارتش آمریکا احتمالاً به زودی به کوه کلنگ حمله خواهد کرد.
گزارش اکسیوس در عین حال یادآوری می‌کند که ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد آماده تشدید جنگ باشد تا خسارتی در حدی به ایران وارد شود تا جمهوری اسلامی تنگه هرمز را باز کند و خواسته‌های او دربارهٔ برنامه هسته‌ای ایران را بپذیرد.
در حال حاضر، ایالات متحده حدود ۳۰ فروند هواپیمای سوخت‌رسان نظامی در فرودگاه بین‌المللی بن‌گوریون در نزدیکی تل‌آویو و تقریباً همین تعداد نیز در فرودگاه رامون در جنوب اسرائیل مستقر کرده است.
مقام‌های اسرائیلی به اکسیوس گفته‌اند آمریکا قصد دارد طی روزهای آینده چند ده فروند هواپیمای سوخت‌رسان دیگر نیز به اسرائیل اعزام کند تا شمار این هواپیماها به سطحی برسد که در آغاز جنگ ۴۰ روزه وجود داشت.
به گفته این مقام‌ها، ارتش آمریکا ترجیح می‌دهد هواپیماهای سوخت‌رسان خود را از فرودگاه بن‌گوریون به پرواز درآورد، زیرا سایر پایگاه‌های هوایی منطقه در برابر حملات ایران آسیب‌پذیرتر هستند و امنیت کمتری برای هواپیماهای آمریکایی دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/77205" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3253e7746f.mp4?token=C3hwZbezglQXLcRS6OosngL0OMkzAxQC67bRjXm66F_3Lx1t0XGiohRGlGjEV0HtpI8C6nI_kdi1l1cI4R0FYaZq-jiljDbsUyyDQQl5oceJKB_YhF2Hg3sW15xV4aCr_pNcyQts4f5JU3nxcErbH6wcG6Wh7TrKF3ZKOT7W-GfoWs3wnpVCwgAP7qEcDn2un0oDqXYoz1Pq1HrJecxQlW2_zvB8vDq649sAHDw1TB2pNddlWqMwLnct7NZ2AJFCgnA8kf4wJVJXa_06NH1EkMQYrFqYxrCFKJq9TeSdj6R07C69SsH-68UtMpJKGGv3eyvKPzJL7CckJbEd0bnIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3253e7746f.mp4?token=C3hwZbezglQXLcRS6OosngL0OMkzAxQC67bRjXm66F_3Lx1t0XGiohRGlGjEV0HtpI8C6nI_kdi1l1cI4R0FYaZq-jiljDbsUyyDQQl5oceJKB_YhF2Hg3sW15xV4aCr_pNcyQts4f5JU3nxcErbH6wcG6Wh7TrKF3ZKOT7W-GfoWs3wnpVCwgAP7qEcDn2un0oDqXYoz1Pq1HrJecxQlW2_zvB8vDq649sAHDw1TB2pNddlWqMwLnct7NZ2AJFCgnA8kf4wJVJXa_06NH1EkMQYrFqYxrCFKJq9TeSdj6R07C69SsH-68UtMpJKGGv3eyvKPzJL7CckJbEd0bnIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا: برج مراقبت چابهار را منهدم کردیم چون سپاه
...
پست سنتکام ترجمه ماشین:
در ۱۶ ژوئیه، نیروهای آمریکایی برج مراقبت بندر شهید کلانتری چابهار را با موفقیت منهدم کردند. این برج بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود که سپاه پاسداران انقلاب اسلامی دهه‌ها از آن برای ردیابی و هدف قرار دادن کشتی‌های تجاری عبوری از تنگه هرمز استفاده می‌کرد.
انهدام این برج مستقیماً توانایی سپاه پاسداران برای هماهنگی حملات علیه خدمه غیرنظامی بی‌گناه را تضعیف می‌کند. افزون بر این، این حمله از آزادی کشتیرانی در آب‌های منطقه برای همه شناورها محافظت می‌کند، به‌جز کشتی‌هایی که در تلاش‌اند محاصره دریایی جاری آمریکا علیه ایران را نقض کنند.
CENTCOM
پیش‌تر پیت هگست، وزیر جنگ آمریکا،
این تصویر دریافتی
رو بدون هیچ توضیحی
توییت کرده بود
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77204" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77203">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qHFtkWMzJSAbATmLihpmiKsYibHJpgIgPE70aT_8Iwd6lGOtQ7V1-BwxQGc7NojybwDGLYLPG2tKO69aOgU3Z66sErx8j5T9CybbsmhGA-CX5uTi4WH576vUhVpxI7OzdURx4R0A-LGICeG48Pv3Jv5F_QniFrXPBQmClOWGxZEB4NjkkjeC7r5xBLT2_7yGN2PVKbP3448_D33kVeqnzAvJVEtuD74cE5lMJsCtSkYSlxcKrfkHwA49UYUdRV0h2dM7SaPCq5QckMfghTsHnozSifuI6soTi1_JaMpeHoNpUMGNShUfuqEGVlP5tfna31_8rPIINmBeGuh5_9_I-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: "پل و خط تخریب شده دیشب ایستگاه انشعاب راه‌آهن
#بندرعباس
"
هم‌زمان با حملات آمریکا در بامداد جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/77203" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n_NLqZtnjlt8dqduDqYF8lHMtR1RAmbIjvlPyLX-aTPGq8Q9boWRxoRdAJj41qqDVud_sMWyEZGFDMXByt9md7KfWkDr7FUn7gxiUJJEEnSMTEJBi5xfBC4A3W3rBQ0gi53_YFMyLgdJGKBR-OOnidRbGp7_pKHpnCy8ghNiko3b2rcCW9AS19R62DAm-V9KhNuxJ7HL97ER-Bu3gAuvQ61ENC4nzYiZemobQDbfZ3OXiN9Cy8pNjQx1aQIgoCdD2CdFSxYpMbNUIsBBJt0cjTJ2miW-UVovcw0txMH0Ys_W2TlKI7Ovcz3vrPdkrZtXeezptXkDRI84lQxskqHo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NQT94NNqTB7_i8USGUgDD1YGPIRaeooWptWcWLhk-pWhzg2bmiFyQXyOtGJvjrepc5_V8tLHJqO9B8nxEgRHsRXfGuB-YsNq6h_X2cmNQA3RtI3RliqM0A3-RYucZ12GvzJ0z63L5IRhjx9pVY9WHuzr1PRAG6TXavpLifSb5-zgRmFgddR18BZuRa65mY1_VcViHMs6ATEiLv4PB1T1V8elZSX0TWGVvfDLtFYyLNTYk-XoIYgV-h7GhkU3byPegdfHBlJXvYah394b3XY-f6NvnTXinPkOInZefWO7YgtAjZ0j6m9Asgb-vnXidXSro2iZGtuuhc6xrPy-tySDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rTZnzdM9EbHo4_Ov5Plkq2USxuKs0QB6I-pKJqfJpw9G5paMFr-O0TdPGrBM3pUB9S933CcuRK3M6lCjEvnzhslAv_A4-q5weyKrCyzJlyFPFOTe8B-LE1216slC9Gv8R_-BwbJUkzBE_BQCcMp213Lq_1AH2UnSt6_ehhB_eX54NlbBXcmlWFpfqiiUm9X9ICd1sKcsn2CjM8B-gkao6qmg4X_5J7IF6JoaFLukZPOOI6xRPTMrG47EC8gTSOODZAMmF6ZE9hsW4kotjUbVoNGgK2HUHoPpOjrt8Dpknw-EcPJQdrhujuuEAF8Jz96lPPJ58zFLsQc1hSuv5B1iLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DxgTQ8v4uMkVAK4Z9Mk__lNhCno5BHaDrCxOZ1epjmh2SaIw_EEwpiw5zh8PP6s1OMQlS82vmR1-qHztcK-z8iifeQNOLVmzSlc2UqRltScMMvJiJVIRyrxinsBXcb4-PZMF1BfPvLcR8NRz9WFDmTv-Vmhk3SrQVdsMtiAwmwYsHWHxvTp7IqcOGo1behp3mrtnAFj3ca3UcDvI-NGNZ77I10wADaneQNL9VgCZX1jQ9W5jWrRI4WRS6r3KuvjanAo9Rk-IVLGakHzBy8_eX0IqvB_AhAdTA49vQZDmO8NPkH58top-qNC-x8s_sP2F9fNnPySCarPD6LU-sopnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NQeLcpdS3QFjAaxJJQ8a3BHJ2mIunRLOwIfya99cknqqwpENcoh4NUTF5mDX2v-_m-dgUNJsoM81uK2pbN-42s34P5LZug5enm5uHMK9_pqdZHk8Y3zphNjNAhtDDKfioVHAD-SsDvuO1dDiPqHNZQ00z9L0zJgNm5IlU5efBGLTSWxQXLOyvCDhHbVX1MZ2NWHblHcuB-16zi3ORuFdXpO_5HHCzb4W3mUCQH2DB1mJzgKvlkYgvlLZYBZgmGgIa_o9bSVmnox8y1X1LtWdNCe2wwAg3jGhzyGgj5K3pof0jfQajlHOyPe4lh6gzAt1vEDdJY9z2hO92DG9XxSiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/slczZURo-k_-Y_ufgyMnw5tTA5q65g0u1qqeMBViPb4G_iVgwYAsuvjB0wHjToqKWZpUmAa0EB9C-wgm0HW3i-SHb8pqQE_b9jOgpgUWA1atpnxusP2tOqI2pNae3s2PkCtAHEmasJUDRfNCD-RXEZCGYYvoEN8jfKMY0gcyx9guu2mR0QIXwmbYJVf9UwsCaKRby-WiHL4VS09twDxTrzbIKPeV9YAov_aLwAyvnK0JMN0PlRdfQW2uD6SfHfe74tewIwgQdCWQsAfPR0gFevxgHgEEnFAX6qz8MXqs8_TCJc48l8qpV5kzYnrjXQt9FAhyEUsLPAvK3y6ChDCojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NB-3pP3cvLczmnTuJRv5MElaZEL4PU2XSu0NdzcaikBk3ZH-KTmW3F1EHj-nMYH_z2AGTwXAoVB2_JSQXmNGUDdUViilCv1cukd6shawJVk1CNCesDRZ__zky3sW0Cp_0oMUkhpSEuuE_Hv1fRA2kEECsrWSIgYdE_R4hR9iNphSAd4cM2ikTV05RaszRjX6iHPLPzwxtT-2Ya03tDqK9uHkN5cI7ckrgxpwCOrFljeuqfIWPMyKp8TGUkwK_4rIPO3_KIOE8IeLrjLQb1a620qlOKgT3c_Uv1wrJIZl57O4BuLhFB_-_6CRLymhJkybtPGjChkzDP22Bbfyo6qnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/il-AkHddwYFFEqkl7W53g8FQfmhSDAKvXp-q7TTag9A98Ovan9aCePtGq3HeUr0oE03IdYIFffLKNIvnS2ovhylpXRDVcTFpHPqFmoHDA9dfK6k6bPriyxs_-u4zYxUf6Z-dwDaKNz4SKXGDVgJAN0phrMbuz5NfJho95NlAnkJ1A9wL_9Qmu0nI8rjihhml9gH2y_xcK0UOix-ozQ1VzwBu_8e44wqIsBGGEKPAvvap1iAYPB62zjkkUUUfHlwpDjs1RJCwrqphScHBipN-XB4cgmzTEQMQoi3JUhap_SgPRgg7qxUCWLc9WwzkFnvxRlgMab1EB7aQTyD1-6KhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L0qdqX4zxZXALZLz2muix_ohe8i4bUbUschtaPJXtlcGaTkFwk_0-37CTaiakrBygf07EtsXrVibBfO6kbIjl_H9Z4YF2omRZRIDnzjqO6b9iN0RIb303DiI-SH-U03_1grCLYxi0icVxWZrxKRbQ_yYca1q6UqwlQ3eDJdFesg0adVVZmo9UhbjUtG-OQSqD6lax9-OFsLhlwtTE4_n1gjpo7DU0iQSmXRHa1Nv723sB7HR7yaumQwiRozteENUZAcqt3hE_nUmRMue1644ERuxwEQ-aV_0efGBnlo5PsxVQeSdAPm_brSEToSHmdTZgsRIkHCNyJkwxJYVlyKNng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده در منابع حکومتی با شرح:
تصاویر هوایی از حمله آمریکا‌ به پل‌های بندرخمیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/77194" target="_blank">📅 17:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77193">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: نیروهای ایرانی مدعی‌اند که به پادگان التنف در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را کشته یا اسیر کرده‌اند. نادرست است.
✅
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در منطقه کشته یا اسیر نشده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77193" target="_blank">📅 17:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuZu45Lf7njeYCn9QngBelPQp-SwLIAc34WMXzZHqoCxHbHwDvtzsofV2c61lVD4idkSvAWOpOnOkzsMOQ75RzmOJVKTYqe4zt-bdiqExaYYDL8BdT5oEuioRh5NPYjV7twonl47jNHEmoKWueZ952e9DHeybrcpT5WQWiOApieeKAA8pIb0SiOVCgFCytk34yxXebFFUdbueyZRS_JeeHShtQ9WSIyJHNGdvimTgtK-bI3HYvkp_o7-KPKVmRR0X9crYlpD3RJeLU5-f7yjlM2HlpQ8RsZmG721vFzEmN3h106UUks_08TW0KX9uO_j21-Y8VFNTMZeQZottODTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه دور تازه درگیری‌های نظامی بین ایران و آمریکا در خاورمیانه، روز جمعه ۲۶ تیر قیمت ارزهای خارجی در بازار آزاد ایران بالاتر رفت و نرخ دلار به ۱۹۱ هزار تومان رسید.
وب‌سایت‌های اعلام نرخ ارز همچنین قیمت یورو را بیش از ۲۱۸ هزار تومان نشان می‌دهند و بهای پوند انگلیس نیز از ۲۵۶ هزار تومان گذشته است.
از سوی دیگر، قیمت سکه بهار آزادی در روز جمعه ۱۸۰ میلیون تومان و سکه «طرح امامی» به ۱۸۵ میلیون تومان رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77191" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMMFCHe8C-ySqkg9wEmmHEeJLz1WCFftdxbpc_HO3c5badz_YHxXBGFMUan4f3AAkpnDo0denfRiHVgWcrwsnOZJJSviWVvp0D-D10-9JT8PXs8Ou4O4psGs4bDsVR4mdZY7J7qPuk8cIZjFDKBfljMH3uYiCv-aSLOOFz_fzy671P7CmC0GxHwTQWrBA5ZbXkvhVvhVboOEPQSTPRlH7d1OtJ4UHeHODKX1gsghiqY9krVNUS0-wbJGv95WdOAEfUPE4LU_qB7beDFyLvsWyjulg7ErIbRBN-s9vI__7vk5td4FHK2BPKqI3cyG4LclEuOVpSfiPkomaqOpWykltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت برق، آب و انرژی‌های تجدیدپذیر کویت اعلام کرد در جریان حملات جمهوری اسلامی به این کشور، یکی از نیروگاه‌های تولید برق و تاسیسات آب‌شیرین‌کن هدف قرار گرفت و در پی آن آتش‌سوزی رخ داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77190" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulMqAydM_uG0G271tkJpI2dKiEPyXnnt92APmWaEMdanT9CGe5-g20a2Anm4eIg813PcG5m3e1K-dW9-FKmCHL-2pk3PQ4vcNXGzpQkqtUYPsXY04GJuFk-Wm_PCRug5BbqvTnC6MDufJsyy8dkpTgtddJh1Q7RJJheOmMlD8xRpeoolLHvNGu213a2bu-XR7skobja1_ieqDnOJsTOX3kaR9vp4FnfuaHV8WMdoAMyrGqCvG5XcMO0usM-0JP58MXmyi9qEYqyxkF8r-aAe4735xKHKe8onC1isDEDS0UECbfCzFitaIdFbTVey8Q2Qkjp_TqSWJO6CvdvUssrrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی و امنیتی استانداری هرمزگان می‌گوید که از شب گذشته تاکنون، هشت نفر در حملات آمریکا کشته و ۱۹ نفر زخمی شده‌اند.
پیشتر وزارت بهداشت ایران اعلام کرده بود که تاکنون ۳۸ نفر در ایران در حملات آمریکا در تیرماه کشته شدند.
بنابر این آمار، در همین مدت بیش از ۴۰۰ نفر هم مجروح شدند.
دور جدید حملات آمریکا به ایران از ۱۶ تیرماه و در واکنش به هدف قرار گرفتن چند کشتی در تنگه هرمز آغاز شد؛ از آن زمان، ایران هم حملات تلافی‌جویانه‌ای را انجام داده است که می‌گوید هدفش منافع و پایگاه‌های آمریکا در کشورهای منطقه است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77189" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=D6_AYOhSNLApnk0MRevHymErJwTQ2AqTaTX7BTs5LrU-wq9AODIa9mrrJsffVpb6R6RboHOMAJAQZN2tqxeVCJG6rqMVpSYn944gcvhZ62yzIhiUphPY9wGP8ky8M6hZOfZ7-z7qjWh3tPaBKPNysSND2mG1j0vwytpsR8xfIfGV3vi0R--WlmVW9oFoX92qryRmHvOHXwElVAArnE_w50ZTC15nLJEBSyUP-mwuXg0zGB_L7tazF-JS_mCGQkufBf_lHimwPjZpLi7_FL_yPNPQoq7n5XngAjji07AtFJVXQL7CSbpoJAqZNEKTWN43iYXO7FshI-MLcZwJFOx8Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=D6_AYOhSNLApnk0MRevHymErJwTQ2AqTaTX7BTs5LrU-wq9AODIa9mrrJsffVpb6R6RboHOMAJAQZN2tqxeVCJG6rqMVpSYn944gcvhZ62yzIhiUphPY9wGP8ky8M6hZOfZ7-z7qjWh3tPaBKPNysSND2mG1j0vwytpsR8xfIfGV3vi0R--WlmVW9oFoX92qryRmHvOHXwElVAArnE_w50ZTC15nLJEBSyUP-mwuXg0zGB_L7tazF-JS_mCGQkufBf_lHimwPjZpLi7_FL_yPNPQoq7n5XngAjji07AtFJVXQL7CSbpoJAqZNEKTWN43iYXO7FshI-MLcZwJFOx8Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: پل تخریب شده در کهورستان شهرستان خمیر استان هرمزگان
بنا بر گزارش‌ها شب گذشته، پنج‌شنبه ۲۵ تیر، در حمله هوایی آمریکا هدف گرفته شده.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/77188" target="_blank">📅 08:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استانداری هرمزگان:  ۵ پل مورد اصابت قرار گرفتند
خبرگزاری فارس:
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
🔹
پل گریوه؛ مسیر بندرعباس، خمیر، لار
🔸
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
🔹
دو پل مسیر کهورستان، لار
🔸
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
🔹
پل روستای مارو شهرستان خمیر
⤴️
از مردم تقاضا می‌شود با عدم تردد در محورهای ذکر شده و مناطق مجاور آن، راه را برای تیم‌های امدادی و انتظامی باز نگه دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/77187" target="_blank">📅 05:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77185">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JjeekrlrYWytODML8QHarmuOwWXbAdIDjr7B1RA6SNmZksNNMp-eLGchsUD_z_pMnip_sHSvN6kjMm_b95zVfej7-8eTiKfpqdKWOj_XONMtY2OQ8KMOu_9tFKhSxcoxuIakUigvvhiFwMYap8Gm_RYa0-ZRYVqzIfUm9UilNV3mLwKfUFWZKSQ5yOaUCONitYv1PCalhRFK0WMjurVeJCcJ1F_zXUk_-9LD3J3tdai5FNQwAyj7TwE88CPtnXHNR10IWlRVsSlCPY0TKp7PGpta6XjWQtp0fLSgy2CZOOF6t3gAOecywNSD6Vkq_f1cX-LknsfvxFJV6wi4JxJ7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/907635e197.mp4?token=H5zWyqwp8jYeXZ1tHeSS8ve64h-6SeYql3tndwU8Qo_11DiNWNM-yTmzoGigPjXsLImWfzfWqgCzPNZ8Rqu7s1s_DOp1CotyMuxMON6Xl0KTuTMxfom2uiUX2n5M5xLrtOwHW932xHdXEJFEpxom4e5k5wcunx0psVrwIH-48cahcJh51Mj3sFU8mW78-S2DIxb7GV28Sq2BthYAXl_pwxAejaCR6QByaL1ylGb8vqqRDHo0uPldX4FpvYu58IoWSx_Jz_Lcr_6WX274eMFbAJsRY-O6eIm3NveWYC6joAQ54RjBn-8Gr2jzwmdbWLBoMAyQf6pboWp_aQsGhNfUiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/907635e197.mp4?token=H5zWyqwp8jYeXZ1tHeSS8ve64h-6SeYql3tndwU8Qo_11DiNWNM-yTmzoGigPjXsLImWfzfWqgCzPNZ8Rqu7s1s_DOp1CotyMuxMON6Xl0KTuTMxfom2uiUX2n5M5xLrtOwHW932xHdXEJFEpxom4e5k5wcunx0psVrwIH-48cahcJh51Mj3sFU8mW78-S2DIxb7GV28Sq2BthYAXl_pwxAejaCR6QByaL1ylGb8vqqRDHo0uPldX4FpvYu58IoWSx_Jz_Lcr_6WX274eMFbAJsRY-O6eIm3NveWYC6joAQ54RjBn-8Gr2jzwmdbWLBoMAyQf6pboWp_aQsGhNfUiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از 'پهپاد دیده شده در آسمان
#چابهار
'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 486K · <a href="https://t.me/VahidOnline/77185" target="_blank">📅 05:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77184">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f0b92b95e.mp4?token=aIcJKMpdx19TfhGfH0DdMV5r6byEG2YJOWWM6h4zeAz18gz5L0HG9zwYg2ndo-MeGiydCNmfPa-r39KVzDZ_s7i87PnxYQGjVRNiHxOtpKA-ZDXCYYMd6wTO_3hQ9ah56WKFu2Jo4jsz2-VGLUqJ5zwVhJWvZXf31m6kagD6A1wU2z0K14lf4HfXqrz8R3Qicr7kWFXdbgnGS_VQRgKRF3fLxjnRfRYrcHibT6G9vc13BPMeleqJpok_kel1HCj8eK3XIqIdTXlxoQ1sMGPrv3zs0NUXt2QBUovqUiazy3CkhffdhhnDM_3oMYwIDjX-bTkf9TkovlFDvZqr4o6hTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f0b92b95e.mp4?token=aIcJKMpdx19TfhGfH0DdMV5r6byEG2YJOWWM6h4zeAz18gz5L0HG9zwYg2ndo-MeGiydCNmfPa-r39KVzDZ_s7i87PnxYQGjVRNiHxOtpKA-ZDXCYYMd6wTO_3hQ9ah56WKFu2Jo4jsz2-VGLUqJ5zwVhJWvZXf31m6kagD6A1wU2z0K14lf4HfXqrz8R3Qicr7kWFXdbgnGS_VQRgKRF3fLxjnRfRYrcHibT6G9vc13BPMeleqJpok_kel1HCj8eK3XIqIdTXlxoQ1sMGPrv3zs0NUXt2QBUovqUiazy3CkhffdhhnDM_3oMYwIDjX-bTkf9TkovlFDvZqr4o6hTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا حملات جدید در ایران را با موفقیت به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) امروز ساعت ۹:۴۰ شب به وقت شرق آمریکا، تازه‌ترین موج گسترده حملات خود علیه ایران را به پایان رساند.
نیروهای آمریکایی، از جمله جنگنده‌ها، پهپادهای رزمی و ناوهای جنگی، با استفاده از مهمات هدایت‌شونده دقیق، ده‌ها موضع نظامی ایران، از جمله تأسیسات پایش ساحلی و پدافند هوایی، زیرساخت‌های لجستیکی نظامی و توانمندی‌های دریایی را مورد اصابت قرار دادند. این ششمین شب متوالی حملات آمریکا علیه ایران بود.
سنتکام به دستور فرمانده کل قوا، به تضعیف بیشتر توانمندی‌های نظامی ایران ادامه می‌دهد و این کشور را در قبال حملات اخیر به کشتی‌رانی تجاری پاسخ‌گو می‌کند.
بیش از ۵۰ هزار نیروی نظامی آمریکا در سراسر خاورمیانه در حال فعالیت‌اند و همچنان هوشیار، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77184" target="_blank">📅 05:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77183">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FazSvgcSWDFpJMVH6lGJSvGc_bvMqv9AFWEir-wqVMJYmwjLJYPgZYr23YKB0tCeTV_tlr9tB5YtQCnn2AxCh7CjS0wH7PND9VbJRKlssPgtB8YrABiKJumpyuZRK2_BvRlz9g23mIIPrlJf61U66NpuMGJxek_ZGA7M8sk1SiSqiHHOnrcGcWizGnDw0W-FCmh0N3xFjzHuyYr_s41zSy_u7iqtArdajgqVRFM5rwxcoXruJ5lQ6zmXiWZzU7JPso_xyF9SyJeVD-veCGPKJb5owGhLyI5w65dyyEgbMDMhSSjg-cvMUdfQDCjAsE2GB3WuYTgxYNBtppTc1HW3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: 'لحظه انهدام برج مراقبت دریایی چابهار'
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/77183" target="_blank">📅 05:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77182">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bv3T8CIaDOfaS0M-E1dq0keG0frTEMeNVybjt25odOblf2wO4K-zgJ-f0QozPbJ20cLOCFqyDIqNgBPwRotgIlzfwM31OVIpmTSNaSGJGXIk6Tsdqdv-dGN40pJw3lX8u1k_THRL0L3VGKruAb9s-PWFnwS2ncDIggHWeYnrF5ZlekUrqfyDvoW-EAnTIxZdB5bzl0QjNT5qYmTN5EWUNiKUf4GU397bPBWmzv7OHIfOOAwhKbn0KnGJwUzxMNTvlJo_2OwDBNrVu2ELYcZhq4aQ9Huhlie9yB8kog_CXue9MYXO4DMHP3YGJz_Wf324n8qT8ZH_n0D3hEvfRv4hfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس و پیام‌های دریافتی: در حمله اخیر آمریکا به چابهار باقی‌مانده ساختمان برج مراقبت دریایی فرو ریخت.
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77182" target="_blank">📅 05:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77178">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYAKxBk6X638JQwJycbibs2RJ6IHCFjvkJjLvG5OWnbO6bDDfljkBXhksGsCUVC79yKP_-mBsOLGbJf6jRgPSn9kBLoUi-jgBYx-xZtSEJdURhHzhChbvjo_4trwwEif651HH9FdCd6k5dw5Q8jiczsBQdaaMyflNzG8QPn43bQ_lXSeEBKBm_4dR1iNc7M5b9fc3UBJhxpQZ13cYnzPN46iKc0QCpgWpbLdDjdcEDuMqNoJ4AcOUQMVZ4jBE5HNjMPdD76ETzlQn0VBQEERq8Fz_vWJak5M_Wqc4qhzmLy10IOyPnnERis8dP2V3gT3_MheEx11V5G-5_Phzs_plQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9b8ff5804.mp4?token=YcgnHmKZVLHewwzOlf589zqRWO_CmtY9k1skx92W2nyCr8DDo-_Vn3DYlPgGIw0J1IUzWghH27UN7TYLMYs_FeiKf8LPY4ybLeMgeNn9vBol_bF8e1NrYq1gGbfKHCqsIyJuWUx5rKXV7qrRtvr46ZRjblVMQk3Tpatib7keHMP5SRanE5g3Fr3WYN25T8AuzpFV8QnWlQEc_jTpbbASRFmbnmVsrSyYd5g1HAvyZnUIUTgfPo4xcGB6dypA8E6l4dgsEJCT-7813fud6vksjGBC_3y58gorAyyw1FvC4M-3qm2wk3lixqGyST8ScWnclLaqLqLdoITIbYtgvKvUoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9b8ff5804.mp4?token=YcgnHmKZVLHewwzOlf589zqRWO_CmtY9k1skx92W2nyCr8DDo-_Vn3DYlPgGIw0J1IUzWghH27UN7TYLMYs_FeiKf8LPY4ybLeMgeNn9vBol_bF8e1NrYq1gGbfKHCqsIyJuWUx5rKXV7qrRtvr46ZRjblVMQk3Tpatib7keHMP5SRanE5g3Fr3WYN25T8AuzpFV8QnWlQEc_jTpbbASRFmbnmVsrSyYd5g1HAvyZnUIUTgfPo4xcGB6dypA8E6l4dgsEJCT-7813fud6vksjGBC_3y58gorAyyw1FvC4M-3qm2wk3lixqGyST8ScWnclLaqLqLdoITIbYtgvKvUoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: دود انفجار حمله به مکانی در چابهار
جمعه ۲۶ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77178" target="_blank">📅 04:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77177">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Moa3r4o8__tSPl9VCJF6Noc6AVTOqKaPLR4jrnZisyD6Ui3Tea4jIMELwOpne0SnSDWzKj0hkGnYb3tv7mcEFqh-Q0ThyCLOvS1CAZu7vet8MW1RWC6_JOQhN1pBYbpslNJiiIBP2yC1xm1K6JVlv8hHSSwV6gt2cBV_8D20bWrOjUR4xHz4B3NFlsJ7NSkTy54brQJoprUeIESBaUP2qUNMpSgUb3LwQ5NRXxKd54uU9x12-ywl538ArfIP9cLlFj-69oZ3rMiyOPtA7D-ml0DuXM73FayrQcjzIpinED2vF8Qg_bzQVXK1aHPS-c9VmQJkrCMn5A_U4L58AW4a1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری هرمزگان اعلام کرده حمله به پل‌های گریوه و کهورستان در بندر خمیر ۷ کشته و ۹ زخمی برجا گذاشته است.
خبرگزاری تسنیم گزارش داده که پل‌های گریوه و کهورستان که بخشی از مسیر اصلی ارتباطی بندرعباس به شیراز محسوب می‌شوند، هدف قرار گرفته‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77177" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9aE8tfIzxStJ0RbtOSZTizIcUsjm3yC7QYey2KA7JG4eXMnFgkLWtpWM4Mfmq57QdxGm3eP7nuLw6DVBkYdRvmyhzE3iJSaDkubz9EXiBDaZ0SodcsvYHo8iNOdT-LjmwS6Px__tbXV-pdkHleVee8MWc3t9Sk4GJ0w7LYyOv7_qRun1BefUb8WQhvwuS3o4DbteFt1T4omBXlgJ8vqjhsrnqiK4FeN_17ciizrfLbDgRHXVUhe_vHPZC62tSUhDVFBgwlORdR9Pz1pB4g2wFpBllFzU6xBqEX1H_h1VtLY6zPh0jF-Sy5_Ln7kHfx7GxIk1c5lRZgLBWyEX4xkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گزارش‌ها درباره دریافت پیامی از جمهوری اسلامی که در آن استیو ویتکاف و جرد کوشنر به سوءاستفاده از مذاکرات و کسب سود از اطلاعات محرمانه متهم شده بودند را تکذیب کرد و گفت هرگز چنین پیامی دریافت نکرده است.
این واکنش پس از انتشار گزارشی مطرح شد که مدعی بود جمهوری اسلامی در پی مذاکرات سوئیس، ویتکاف و کوشنر را متهم کرده بود از نوسانات بازار ۹ میلیارد دلار سود برده‌اند و خواستار اختصاص نیمی از این مبلغ، معادل ۴.۵ میلیارد دلار، به حکومت ایران شده است.
ونس این ادعاها را «کاملا بی‌اساس» خواند و گفت ویتکاف و کوشنر از اعضای مورد اعتماد تیم دونالد ترامپ، رییس‌جمهوری آمریکا، هستند و ادعای سوءاستفاده آن‌ها از اطلاعات محرمانه «مضحک» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77176" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های دریافتی:
درود وحید جان چابهار سه چهارتا موج و صدای انفجار و صدای جنگنده
۴:۳۷ دقیقه
۴:۳۸ دیقه چابهارو زد
چابهار زد
سلام وحید جان صدای دو انفجار ساعت ۴:۳۷ دقیقه در چابهار شنیده شد
چابهار ۴:۳۸ پایگاه سپاه امام علی و اسکله سپاه توسط جنگنده ای که خیلی پایین پرواز میکرد بمباران شد.
🔄
باز هم زد
دوباره زد الان ۴:۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77175" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77174">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام دریافتی 'از قطر':
ده دقیقه پیش صدا انفجار و پدافند، دوحه.
Still no threat cleared message.
آپدیت ۴:۲۳:
Security threat eliminated.
هم‌زمان از تبریز پیام‌هایی درباره شنیده شدن صدای پرتاب موشک دریافت می‌کنم. قبلش هم از شهرهای دیگری پیام مشابه فرستادند
.‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77174" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/146830ca4d.mp4?token=HdCnSbXzF_PVrhtxBPPnFhvxKdiyHlZacYrJjMvBd-wkysN6w0IfEIcVJGVYpd6b1_10h-L_iMV-qzaBZh-qIDo7mpMSmvEAxF2Wu8Jr_-wXbyyiZwk3I3GQLIYo9WieMRdqlRtcu5WtxkLv8N_m2uzyz4NOEZB-alpGbe3lGfIETIWU6AwbA2fF_pKDt1QwzEHv_xsgCkU-r4ujJlZNGUFdLYZMCBdz_80QmVH3-_MwHs8fK_Wc4wEu8PB2DiZtCbukT5LPpog5Pp2h1UUanuXiDhLDmXwNjMXTj64p-8qUR5O_sXBZimtnuMOQVPToe-9FjR8kCuG8hh0yzBuTDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/146830ca4d.mp4?token=HdCnSbXzF_PVrhtxBPPnFhvxKdiyHlZacYrJjMvBd-wkysN6w0IfEIcVJGVYpd6b1_10h-L_iMV-qzaBZh-qIDo7mpMSmvEAxF2Wu8Jr_-wXbyyiZwk3I3GQLIYo9WieMRdqlRtcu5WtxkLv8N_m2uzyz4NOEZB-alpGbe3lGfIETIWU6AwbA2fF_pKDt1QwzEHv_xsgCkU-r4ujJlZNGUFdLYZMCBdz_80QmVH3-_MwHs8fK_Wc4wEu8PB2DiZtCbukT5LPpog5Pp2h1UUanuXiDhLDmXwNjMXTj64p-8qUR5O_sXBZimtnuMOQVPToe-9FjR8kCuG8hh0yzBuTDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منابع حکومتی از
محل حمله آمریکا به پل جاده دسترسی بندرعباس – بندر خمیر و جنوب استان فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77173" target="_blank">📅 03:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bcxAill6_Gylx12iqASs8um0r4vvofGuG3CHpYU5-6cTyV8sYHhSMUtICAmEFRJ7vbzrjF_zF2aOpZoAofLd2vQoPuBc4adnneuhgrRUQ4IRLawk1ZuLS0YQsYM_PhPz6qrujUVtSCwU2f7R9anB9QGesUsaduyRYhMxVPmkG6Tuy5zkb-BSqN62M3GBq8-aXk30SGVNLEQkkipIuQ1DZGgQmEoQmHrE8MuuhwGXN5qmi2C8nH_F7uKdgi_dvUdECSX_gEUvRBNDDwzBIUW2eOorr2yPNAy8VGIdQ18pBZ8FnpwYE1pUsQvPRzPGr4ttYFiHEUYGf3woYRD6HKlg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به روزنامه وال‌استریت ژورنال گفت ارتش ایالات متحده چندین پل در ایران را هدف قرار داد تا مسیرهای تدارکاتی منتهی به بندرعباس و پایگاه دریایی واقع در تنگه هرمز را قطع کند.
آمریکا می‌گوید جمهوری اسلامی از آن پایگاه دریایی برای حمله به کشتی‌ها و نمایش قدرت استفاده می‌کند.
تلویزیون حکومتی ایران نیز گزارش داد که چندین حمله به پل‌هایی در بندرعباس و مناطق اطراف آن انجام شده و بزرگراه‌های منتهی به بندرعباس از استان‌های همجوار مسدود اعلام شده‌اند.
رئیس‌جمهوری آمریکا، سه‌شنبه ۲۳ تیر در مصاحبه‌ با شبکه فاکس‌نیوز گفته بود دامنه حملات آمریکا به جمهوری اسلامی در روزهای آینده گسترش خواهد یافت. دونالد ترامپ افزود حملات سنگین ادامه خواهد داشت و اگر جمهوری اسلامی وارد مذاکره نشود، هفته آینده نیروگاه‌های برق و پل‌های آن هدف قرار خواهند گرفت. او تصریح کرد: «تمام نیروگاه‌های برق و تمام پل‌های آن‌ها را از کار خواهیم انداخت، مگر اینکه پای میز مذاکره بیایند.»
ترامپ در آن مصاحبه همچنین تاکید کرد عملیات نظامی آمریکا علیه جمهوری اسلامی ادامه دارد و این حملات «تا زمانی که خودم بگویم کافی است» متوقف نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77172" target="_blank">📅 03:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3729a1df42.mp4?token=MzxsixkpSX8sooUZ1iaFV_Od41gYTrwaRbNW-EW3KzIDWVwGLitwEoyJ4-eimlxvju86kBU0p2nMoTJtr2TzR6aeCr1xChFe1r6HiCqBjLEBN8eukp4t9aJZpkkAMbJ0kBObxOU_IxjFKNcOlcza0rmj9iBb1Ts5kO-dRryx_EUsRECXQ5wy9FMBqhE_R6dJDM0ZfpyWIdwCCdPvPL01Um3224gg5J0vBO1yFP5UkhNRLxwMPfwZ258TRMWWyROYZ5jzOjFJa562OTkdkhhDSAe-BuTfipJhFJFO856GskwudcRSGq-FczGh6f8KHXaI6AI2scUGzmcX8U1mCP6H8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3729a1df42.mp4?token=MzxsixkpSX8sooUZ1iaFV_Od41gYTrwaRbNW-EW3KzIDWVwGLitwEoyJ4-eimlxvju86kBU0p2nMoTJtr2TzR6aeCr1xChFe1r6HiCqBjLEBN8eukp4t9aJZpkkAMbJ0kBObxOU_IxjFKNcOlcza0rmj9iBb1Ts5kO-dRryx_EUsRECXQ5wy9FMBqhE_R6dJDM0ZfpyWIdwCCdPvPL01Um3224gg5J0vBO1yFP5UkhNRLxwMPfwZ258TRMWWyROYZ5jzOjFJa562OTkdkhhDSAe-BuTfipJhFJFO856GskwudcRSGq-FczGh6f8KHXaI6AI2scUGzmcX8U1mCP6H8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
سلام موشک از شهرستان جم استان بوشهر فرستادن
سلام همین الان از جم موشک بلند شد(۲:۵۶)
۵عدد موشک از جم به سمت خلیج ۲/۵۷
سلام وحید جان از جم موشک بلند شد
سلام همین الان پرتاب موشک از جم 2:57
سلام وحیدجان الان ساعت ۲:۵۷ از جم موشک بلند شد نمیدونم به سمت کجا
همین الان ساعت ۲ و ۵۷ دقیقه موشک از جم بلند کردن
ستاد کل ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی جمهوری اسلامی هستند.
ارتش کویت همچنین اعلام کرد صدای انفجارهای شنیده‌شده ناشی از رهگیری اهداف مهاجم توسط سامانه‌های پدافندی است و از شهروندان خواست دستورالعمل‌های ایمنی صادرشده از سوی مقام‌های ذی‌ربط را رعایت کنند.
@
VahidOOnLine
پیش‌تر:
وزارت کشور بحرین اعلام کرد آژیرهای هشدار در این کشور به صدا درآمده و از شهروندان و ساکنان خواست آرامش خود را حفظ کرده و به نزدیک‌ترین محل امن بروند.
این هشدار در حالی صادر شد که پیش‌تر جمهوری اسلامی اعلام کرده بود پایگاه ناوگان پنجم آمریکا در بحرین را هدف حمله قرار داده است. مقام‌های بحرینی تاکنون درباره علت به صدا درآمدن آژیرها یا وقوع هرگونه حمله جزییات بیشتری منتشر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77171" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZWz4J6EE-wjTauzhGkVYMI2BiMgiL5pJfNGslrWHbZpMbTROcYqv55wSuKAIEUioAd_uU916fya4c2wdNeq4Wjhw0_AOaNrmYHGc4kOXGmc9d8_3r_eklPU8C3d4tkjLvGU_j5yfl3U30CiAM3dfBswOI2c-Pqn-gl-FnD90QzYTQVexQ9Ct_WiyCcIjc-ScHwbvw_4fH_heHz-3s6IYMKUjRmZwph_8-7UcPXcB_3FYfhGIDw1Qwd13F_z_xYEJpLCoac82Dn3eY04KTRrjowr78Mn8e6n0bZd8zb54O4uF3q1hwOvY5UGXq7SJApMbMCcCs2ziqJsvnkOT-qfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع حکومتی به نقل از استانداری هرمزگان:
در ساعت ۰۱:۳۰ نقاطی در حوالی بندرلنگه مورد حمله آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77170" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/033b4ebf1c.mp4?token=XY8YQL0VFMkKd5A3AsWJQfIUvnFjw-2NFTOEiNyIIIAV5GOoRUrRaFGHc6NwlzJ6TP4wBbUykS2GjQtpMHSgNy-xDSvkqlx7cziJaaSlbTeD20W5jMk_DuFA_jZhI4NDYXSqkh6yfApSB6VKAoAJgQdOI7Mh99C_8ZxMC29UuICYZ4IFJKbGjIgebEYFIC6xxJCZ0OIH3C5hVP-iGwusv9v8nAlSYMt4PgvMC0k498QZxRqFaxiyVOtgVhcEyboAzLduflSAORQZCNi-X06qzkokAbu8AVQ_xQM1pwrLszYagqMrp6AWqXMh2W5KYK2j24jEs7leXtcI_KHOwPBLfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/033b4ebf1c.mp4?token=XY8YQL0VFMkKd5A3AsWJQfIUvnFjw-2NFTOEiNyIIIAV5GOoRUrRaFGHc6NwlzJ6TP4wBbUykS2GjQtpMHSgNy-xDSvkqlx7cziJaaSlbTeD20W5jMk_DuFA_jZhI4NDYXSqkh6yfApSB6VKAoAJgQdOI7Mh99C_8ZxMC29UuICYZ4IFJKbGjIgebEYFIC6xxJCZ0OIH3C5hVP-iGwusv9v8nAlSYMt4PgvMC0k498QZxRqFaxiyVOtgVhcEyboAzLduflSAORQZCNi-X06qzkokAbu8AVQ_xQM1pwrLszYagqMrp6AWqXMh2W5KYK2j24jEs7leXtcI_KHOwPBLfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
فرماندهی مرکزی ایالات متحده تفنگداران دریایی آمریکا از یگان اعزامی یازدهم تفنگداران دریایی، ۱۶ ژوئیه در خلیج عمان برای راستی‌آزمایی، سوار نفتکش «وِن یائو» شدند.
تا امروز، نیروهای آمریکایی مسیر ۳ کشتی تجاری را که تلاش داشتند محاصره را بشکنند تغییر داده‌اند، ۱ کشتی را که از دستورات تبعیت نکرد از کار انداخته‌اند و برای اطمینان از اجرای کامل محاصره دریایی جاری آمریکا علیه ایران، وارد ۱ کشتی شده‌اند.
تنگه هرمز و آب‌های اطراف آن همچنان آزاد و باز است، به‌جز برای کشتی‌هایی که تلاش می‌کنند «دیوار فولادین» محاصره آمریکا را نقض کنند.
🇺🇸
CENTCOM
ویدیوی دیگری رو هم توییت کردند. میشه از ثانیه 00:20 ویدیوی بالا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/77169" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8860c5a306.mp4?token=Wb9P5qP0n2MEIF4cKa8VWJ5m7mIblJVBuX0fzi-XUCIs-BWtlvC8AR_yEu-y7iVQWvSUOlmcTtRABfCAcbktP_8NrhycO40mygxwH-qJWdL6GbgxMtwp4KMvw4Ywbrjf_1vJZ1xZbW2Q0ecKakiW1h1R_8s0Z7_gxEMic4wv-psY-QX_Dz1XwUYLl4f0I7eCBCyOB52bvhnqvaFVlgAwmwwUleYLjR7tcYj3gNreqeBrrfTo1-ilYBso8BDbpLCbvEFxwboPDeGxaYP2SGgOG9n_loW48qtqWl46AohwVCesgrKij6SiyuW_d2fuxM6ZDLCIMuftGPumWr2eFZH0mA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8860c5a306.mp4?token=Wb9P5qP0n2MEIF4cKa8VWJ5m7mIblJVBuX0fzi-XUCIs-BWtlvC8AR_yEu-y7iVQWvSUOlmcTtRABfCAcbktP_8NrhycO40mygxwH-qJWdL6GbgxMtwp4KMvw4Ywbrjf_1vJZ1xZbW2Q0ecKakiW1h1R_8s0Z7_gxEMic4wv-psY-QX_Dz1XwUYLl4f0I7eCBCyOB52bvhnqvaFVlgAwmwwUleYLjR7tcYj3gNreqeBrrfTo1-ilYBso8BDbpLCbvEFxwboPDeGxaYP2SGgOG9n_loW48qtqWl46AohwVCesgrKij6SiyuW_d2fuxM6ZDLCIMuftGPumWr2eFZH0mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت چند ساعت بعد: صدای چند تا از انفجارهای در ویدیوی بالا
پیام‌های دریافتی:
وحید جان همین الان بوشهر سه تا انفجار
۴ تا افنجار شدید بوشهر
بوشهر ۴ انفجار پشت سر هم ۰۰:۵۵
بوشهر سنگین دارن میزنن
سلام وحید عزیز بوشهر همین الان پنج تا انفجار رخ داد
بوشهر 00:55 صدای 4 انفجار
بوووشهررر همین حالا زدنن و دارن میزنن
همین الان بوشهر رو زدن ۲-۳تا شدید
مجدد ۴-۵تا
خیلی شد
حاجی رگبار بستن
سلام بیشتر از ده تا صدای انفجار بوشهر هنوزم دارن می‌زنن
بوشهر ۴ انفجار پشت سر هم ۰۰:۵۵
۶ تا دیگه پشت سر هم ۰۰:۵۶
بوشهر ۰۰:۵۵ بالای ۱۰ بار پشت سر هم زدن
سلام آقا وحید همین الان ۱۲.۵۵ دقیقه به بوشهر حمله ی  شدیدی شد منطقه بهمنی و من بسیار در خود ترسیده ام.‌
بوشهر صدای خیلی مهیب
۱۰انجار بوشهر الان
۵۶دقیقه
بوشهر
۱۲ تا انفجار شمردم
ساعت ۱۲.۵۵ تا ۱۲.۵۷
سلام وحید جان بوشهر ۶ بار زد خونه لرزید
بوشهر ۱۲:۵۷ چند انفجار خیلی مهیب
بوووشهررر همین حالا زدنن و دارن میزنن
بیش از هشت انفجار
همینجور پشت سر هم دارن میزنن نزدیک ۱۰ تا بود پایگاه دریایی دودش پیداست
بوشهر داره پشت هم میزنه
😭
😭
😭
😭
بوشهر خیلی صدای بدی اومد انفجار شدید بود همراه با لرزش چندین تا انفجار پشت سر هم بود
سلام وحید
حداقل ۱۲ تا انفجار پشت سر هم بوشهر
سمت پایگاه دریایی
بوشهر خیلی صدای بدی اومد انفجار شدید بود همراه با لرزش چندین تا انفجار پشت سر هم بود
سلام، صدای انفجار شدید بوشهر
ساعت ۵۵ بامداد شهر بوشهر محدوده پایگاه رو داره به شدت میکوبه شاید ده تا دوازده انفجار
سلام آقا وحید ساعت ۱۲ و ۲۶ دقیقه شهر بوشهر ۱۲ بار زدن صدای انفجار شدید بود
۱۲ تا صدای انفجار بوشهر اومد
پایگاه هوایی بود پشت هم رگباری
انفجارهای اولیه نزدیک فرودگاه بود صداش نزدیک بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77168" target="_blank">📅 00:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y7NGMbXMxYH0o1_O3lSh3it6y84vIsZSkPBn_r93g4SNGzkvPF6mq5bFsDVSsChQq_CgiIQTLP8DIVOCXnx9tpjrQdcl8LeQQ2_51jMs7ttyoPfDL_V7ZSknFEQJNMS-cbUzSVxO4UWL5mSgKouv_NebbAKo1ovURSxVtAXf7370GsmMvT-7-jAIoJancw3QW3oLWndAdI7odkvQ5dsMidFOpDuEBch2c2bHXuUE6jHzldzKPn_hKgqDWEAcatvkD3q4Ebtt6imAB3rtNptSMlO2N9Kqi6iH1RvywKjsRdZl2-bRGqqB8tewuR5VkeUJADrlqpo_YiZWhwKxCDdn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: 'پل کهورستان در شهرستان خمیر استان هرمزگان'
که گفته میشه با حمله هوایی آمریکا تخریب شده.
پنج‌شنبه ۲۵ تیر
Vahid
فارس به نقل از استانداری هرمزگان:
علاوه بر پل کهورستان، پل گریوه نیز در محورهای ارتباطی استان، مورد اصابت قرار گرفته است. ۲ نفر کشته و ۴ نفر زخمی شدند.
تسنیم:
در شهرستان خمیر به سه پل حمله شده که مهم ترین پل، متصل کننده بندرعباس به لار در استان فارس در محدوده بخش کهورستان است.
صدا و سیما:
استانداری هرمزگان اعلام کرد محور بندرعباس - خمیر - لار و محور کشار - کهورستان نیز مسدود شده است.
📍
میگن یکیش این بود:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/77167" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NkMH8U50C84G4KKW3AKed4VB9sQzhLrDBJYltDx3NFe_APVGfgVVPJBU6KWDQPt91hnPkTFThQ64GHRLuQW66JgxLWglX55BGDQWr-DlVETd0VPsNj-Ga5KgBcPjNHicwFN_KzR2RxqBV75ZHdIKy5XGj5tIfAKRtBhtQLzBOvKpVdtgzv6K9xyFEQP3zxcvd1YmSAV51Rvn67X8eFSCCDZK9-Ih-DJeQPnnBeTMXSTBHyi3sc5yneDL9epfQjCYOxvE2ljKkKCgCEK0zIo0exsRuRTO7sU7nG6dqgdPNTvXnF-x_yEqx1sawc1TDKxirBjRMjNBx_fPY1mJ7DS8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77166" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/713dc65855.mp4?token=ajPExPqypg9gj7rvZWwHthrvkC5ByH9RQUEKpaQAPOjlwHBdFryfplR-H09Xpyh7mHhxhVjWKx-mdmGakIWJ4CI5Tu8o7FmPL5ePyPsnltcBooDpdjnUi_OjDWXCMPwe-oAA63HLLWdv9PT0KXGaCEKj3DY3rlXdmMvPh6gYhw1ATGa9V6bcTuHGeFTBU9W0FQMpXhyyXfg-fJmRL5PbS7szwRGaS_l5OWkVhjrBw0oUGTsO2mNy8k29fhOVf8fQidn9JRQ8dTVwFBsjZWzyZg-ePQ4j4uTltBWXfiTBsHr_SBTnQpBNx3onQNn-q5g4zNLNtGzRzmR6OtyfsZOQKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/713dc65855.mp4?token=ajPExPqypg9gj7rvZWwHthrvkC5ByH9RQUEKpaQAPOjlwHBdFryfplR-H09Xpyh7mHhxhVjWKx-mdmGakIWJ4CI5Tu8o7FmPL5ePyPsnltcBooDpdjnUi_OjDWXCMPwe-oAA63HLLWdv9PT0KXGaCEKj3DY3rlXdmMvPh6gYhw1ATGa9V6bcTuHGeFTBU9W0FQMpXhyyXfg-fJmRL5PbS7szwRGaS_l5OWkVhjrBw0oUGTsO2mNy8k29fhOVf8fQidn9JRQ8dTVwFBsjZWzyZg-ePQ4j4uTltBWXfiTBsHr_SBTnQpBNx3onQNn-q5g4zNLNtGzRzmR6OtyfsZOQKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: یکی از پل‌های کهورستان شهرستان خمیر
منابع محلی: محور رفت و برگشت
#بندرعباس
به لار مسدود شد.
پنج‌شنبه ۲۵ تیر
Vahid
یک خودرو دیده میشه که احتمالا از روی پل سقوط کرده.
آپدیت:
محتوای ویدیوها به نقل از شاهدان عینی صدا و سیما!
تجاوز هوایی به دو پل در بندر خمیر
🔹
به گفته شاهدان عینی دو  پل حوالی روستای کهورستان و رودخانه شور شهرستان بندرخمیر مورد اصابت قرار گرفته است.
🔹
راننده یک خودرو شخصی، روی یکی از پل‌ها شهید شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77165" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dfd383428b.mp4?token=JYAm0d2yIIjPPfrRVGXjag4gdQrEbrwnhxGgl7lW2InnOq7jp20AR1hPwYk2ecmVGcdj5FUyt31bQRDf3chLTTp6EzSHPzcJEQiENbZQcNEPKRvjAekAdp0-AvMr7i7-KlT_sixwg5tjDZ7oVHyqoHYbYSOOIfDstrgRuDGfBsu53uRpFmjAg3EbtJnBi7UvUeeeddVjGqJLJA58OUAjRFGr6Fl_6uoZEB-YbzVgbH_M55izIYag9mNIvGSSwzJfBzq1-BtyHxmLEv_PzJAqk5TLoMH2C-NczDa7qx3TkJFof0DpuUZHejNqb4zUARY7ncTTb98kqp2ZndWCKGQKPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dfd383428b.mp4?token=JYAm0d2yIIjPPfrRVGXjag4gdQrEbrwnhxGgl7lW2InnOq7jp20AR1hPwYk2ecmVGcdj5FUyt31bQRDf3chLTTp6EzSHPzcJEQiENbZQcNEPKRvjAekAdp0-AvMr7i7-KlT_sixwg5tjDZ7oVHyqoHYbYSOOIfDstrgRuDGfBsu53uRpFmjAg3EbtJnBi7UvUeeeddVjGqJLJA58OUAjRFGr6Fl_6uoZEB-YbzVgbH_M55izIYag9mNIvGSSwzJfBzq1-BtyHxmLEv_PzJAqk5TLoMH2C-NczDa7qx3TkJFof0DpuUZHejNqb4zUARY7ncTTb98kqp2ZndWCKGQKPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: در کهورستان
#بندرعباس
یک پل هدف گرفته شده.
صدای ویدیو: موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
پنج‌شنبه ۲۵ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77164" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=DBFqrSrosbvO2Sg1J_UPX2u28b1TFEDIj37pJ0m3U_8uXvYFy1o4aYwD7urgnaiikRYxSgHH7-LXOsi6UViWg7Env8_dqDjynDhTrUK6Ml3VL9_e1ufuNt5v38QSsW2H3gPpYTxV9hwZgINQ9JEUHY7nbiaHSTnTb1cqPFBS5SSc4-7_LJsuZ3D-rirWin12E1diBl-ay4oV966-BRahEnpcayhqhvztnvxDpxCfKB6KCNEv1jP-5Q2NtqMRFOhgXZ_RcHhan0VXFAe92Wy60VMBwq6Hu4Xz84GQ0qgZhXSLOEWwwWfVHL-KT0tUmndHkiBoYHPTTHmUvo-Tw7jvEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=DBFqrSrosbvO2Sg1J_UPX2u28b1TFEDIj37pJ0m3U_8uXvYFy1o4aYwD7urgnaiikRYxSgHH7-LXOsi6UViWg7Env8_dqDjynDhTrUK6Ml3VL9_e1ufuNt5v38QSsW2H3gPpYTxV9hwZgINQ9JEUHY7nbiaHSTnTb1cqPFBS5SSc4-7_LJsuZ3D-rirWin12E1diBl-ay4oV966-BRahEnpcayhqhvztnvxDpxCfKB6KCNEv1jP-5Q2NtqMRFOhgXZ_RcHhan0VXFAe92Wy60VMBwq6Hu4Xz84GQ0qgZhXSLOEWwwWfVHL-KT0tUmndHkiBoYHPTTHmUvo-Tw7jvEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: کهورستان بندرعباس پل زدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77163" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77160">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vc8ddiOIkirqryiOxW2N1wI7lvRpZeQztRVPGo3rpxs9QjMRnk_ch2kF_3s56UIHdg8E9RMXvvEpGZPy5zEY4ej_PKlXM5sQ6vhCoEmeecffmh5Vlo2PJYlOH9VXRVIbO4TClvvPPuKPotQox_oNtOgqz_NXjksDPQAF0dPptRPcFEVrLa_skGVQlL86iK9UTQ_pUD_mxxcDfG3qxyu_pTmlUxCmzKfcCLf7mNJh5LLJQk29E18Vhpdiq5wgFXOutAcQNVE0PQHIMF9B-fUvlVScpjOMjvkDBMFGK86hB8U-j17Ezcom9smCiAPi3rFnLSaeLeJKJCrrUnfhXZFtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I9yASRAdLQ6ux8HQlIQiBsUuWaharh9ZF7Wa2ZMB6bcu4hCAgRrZewxv03tfeHxbOXv1coJsHvgYA7CQJ4jAiAOhy8kkoqykn_CPKJwYxSev5-t0vDBlUoug7_GliAGEwi5gDsmAAGieegw_uO6iczPJYzEyW8IIRyRgkBRl2Ebo4ouqIGXEQTyFBMPCr1aeIKf4-ZKq4Xky0rbYNizOrw3blAI6k6XvMqa8x2_1SdizXi8TOHo03ZFizmQ1pDC7hKe0b2lOcUhTUBZt-0IAq0e22BHNPB4SGqhsegZB0rsu-HeXAYJQecSTWhxe3K9u83XXFGBbBMZhIaAg7JeJOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d9ea9eedd.mp4?token=BkVXOzujkR-pK4BwWTzv4crW464g4Cl2PXkXzh7F9QLqBFbFGhKZlOw8yudEM3WFJUtaa4Hv5BL15_qoJ3NdmLY_X-b2qeEHorOsOFkrrPGBpUibOUT8vl8ZOKGd5FepSrKXElDZLr9Z9YyBBsSM7KZpCD_e_hHe5rp8UcnZ_ynUajMci13vP9zdIsGncCdySVH1YbWroHm42EYMmM1t9Ii8PLb0uUYlq46YLezxn2d4eH8aDUt-TnnoXZM12F1CG7iSBy9Tjz6PA5z97H9ONCEuFTYlJ-2dF6bk78d7y5qhWp36hP_Cr8mSwzk08KTRN4AO58qDM-uMNbE--31K3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d9ea9eedd.mp4?token=BkVXOzujkR-pK4BwWTzv4crW464g4Cl2PXkXzh7F9QLqBFbFGhKZlOw8yudEM3WFJUtaa4Hv5BL15_qoJ3NdmLY_X-b2qeEHorOsOFkrrPGBpUibOUT8vl8ZOKGd5FepSrKXElDZLr9Z9YyBBsSM7KZpCD_e_hHe5rp8UcnZ_ynUajMci13vP9zdIsGncCdySVH1YbWroHm42EYMmM1t9Ii8PLb0uUYlq46YLezxn2d4eH8aDUt-TnnoXZM12F1CG7iSBy9Tjz6PA5z97H9ONCEuFTYlJ-2dF6bk78d7y5qhWp36hP_Cr8mSwzk08KTRN4AO58qDM-uMNbE--31K3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: حمله به فرودگاه ایرانشهر در سیستان و بلوچستان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77160" target="_blank">📅 23:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77159">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام‌های دریافتی:
سلام داش ایرانشهر فرودگاهشو دوباره زدن ساعت ۲۳:۰۱
پنج دقیقه پیش دوباره فرودگاه ایرانشهرو زدن
سلام  ده دقیقه پیش فرودگاه ایرانشهر رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77159" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77158">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y8fYYtoIp2eZd5Hw337A7m9kP8NPv5dGkxUDwb9QoGVTPjpKfn_kcWehhACaSSD0FNKbUKT1ClTmzRjKtp6Dyl71TZjRFMsiq9mO2inHMxwRpI2esSP4xitbpi3WQT4yovvrHt0UfMT2xMhTjlGlOkNXmjSkgjBkeBLi9KBcoWptim3aG_8NrWNyFFE9a8CtN2m3jwb-lR81_unlMwccTT2xNpP7JR7FEY_snYfc8LvD7m6mIVXF_ZPFvEjt-GtK95LwiNmz3b0KzmgmX4eeN6f1QvhqADx7wNbjRhODFDYPhP_BgeVJG2YrdCONlfW5TF4sbfM9wpJooxXdM2Y3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم:
مصدومیت ۷ نفر در حمله دشمن آمریکایی به بندرعباس
🔹
به گزارش خبرنگار خبرگزاری تسنیم: در پی حمله دقایق پیش نیروهای متجاوز آمریکایی به محله مسکونی تپه الله اکبر در شهر بندرعباس، متأسفانه تاکنون ۷ نفر از هموطنان مجروح شده‌اند .
🔹
بلافاصله پس از وقوع این حادثه، کلیه نیروهای امدادی و درمانی دانشگاه علوم پزشکی هرمزگان در حالت آماده‌باش کامل قرار گرفته و اقدامات درمانی لازم برای مداوای مصدومین در حال انجام است.
🔹
روابط عمومی دانشگاه علوم پزشکی هرمزگان ضمن محکومیت شدید این اقدام تجاوزکارانه، از عموم مردم شریف بندرعباس می‌خواهد ضمن حفظ آرامش، اخبار را تنها از طریق مراجع رسمی و معتبر دنبال کرده و از هرگونه شایعه‌پراکنی خودداری فرمایند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77158" target="_blank">📅 23:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77157">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پیام‌های دریافتی:
‌
بندرعباس صدای انفجار شدید ۴ بار
ساعت ۱۱ شب
همین الان صدای انفجار شدید مرکز شهر بندرعباس اومد
سلاام وحید جان
بندرعباس دوتا انفجارر
شرق بندرعباس پایگاه هوایی ۲۳:۰۰ دارن میزنن
الان دو تا صدای انفجار بد آمد بندرعباس
بندرعباس دو تا انفجار صدای دومی مهیب بود ساعت ۲۳
سمت شرق بود
بندرعباس همین الان صدای انفجار
چند دقیقه قبل تر هم یه صدای انفجار اومد
بندر الان اینقدر شدید بود پنجره‌های اتاقم لرزید ۱۱:۰۱
سلام الان ۴ بار با فاصله چند ثانیه خیلی با شدت بندرعباس رو زدن (ما نزدیکای فرودگاهیم)
وحید جان سلام الان ساعت ۱۱ شب قشم هم صدای جنگنده اومد هم ۴.۵تا انفجار که خونرو لرزوند جنگنده تو اسمون میچرخه
باز هم بندرعباس صدای جنگنده خیلی واضح داره میاد دوتا صدای انفجار اومد بلافاصله برق قطع شدد صدای جنگنده اصلا قطع نمیشه
بندرعباس ساعت ۱۱ فکر کنم سمت پایگاه هوایی باشه.
وحید جان سلام ، قشم سمت دهخدا ۳ تا صدای نسبتا شدید شنیدیم.
بندر عباس همچنان داره میزنههه
صدای زیاد و لرزش
برق هم داره نوسان میده
ی مناطقی هم قطع شده
ساعت یازده شب صدای سه انفجار بندرعباس
الآن سه تا صدای انفجار بندرعباس اومد
بندر عباس تو فاصله چند دقیقه ۴، ۵ تا صدای خیلی بلند خونه لرزید ، آخریش ۱۱:۰۲ دقیقه اینا بود
سلام وحید بندرعباس اول برق اتصالی کرد بعد صدای انفجار شدید
وحید سلام دقیقا ساعت ۲۳:۰۰ صدای انفجار بندرعباس
بندرعباس ساعت ۲۳:۰۰ صدای ۴ انفجار خیلی شدید و سهمگین اومد
بندر دوباره زد. بزرگ ولی نه به بزرگی یکی دو ساعت پیش
انفجارهای امشب تو بندرعباس از شب های قبل خیلی بیشتره
واقعا ترسناک بود
به مرکز شهر و نزدیک گلشهر صداش اومد
بندر رو چند بار زد و برق هم قطع و وصل شد
وحید برق نه تنها بندر نوسان داشت بلکه چندتا از روستاهای بندر هم همینجوری نوسان و قطعی داره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77157" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77156">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
الان اهواز صدای دو تا انفجار اومد  ۱۰:۳۰
اهواز انفجار دوباره همون ۲۲:۳۱
اهواز ساعت ۱۰:۳۱ دقیقه دوتا صدای انفجار مهیب اومد
وحید جون 10:30 دو انفجار پشت هم اهواز
الان ۲۲ و۳۰ دقه صدای انفجار اومد اهواز
اهواز ساعت ۱۰:۳۰ صدای سه انفجار اومد.
اهواز طبق روال روز های قبل ساعت ۲۲:۳۰ صدای انفجار میاد
صدای سه انفجار شدید
دقت كردين همش سر يه تايمه
😭
😭
😭
😭
دیشب هم دقیقا همین ساعت ۲۲:۳۱ زدن
اهواز ساعت 10:30 زدن سه تا بود
همین الان 22:30 صدای دو انفجار مهیب در اهواز
بازم مثل دیروز راس ساعت 10.31 دقیقه اهواز رو زدن
اهواز ۲۲:۳۰، زدشون از قطعی برق هم آن‌تایم تره
اهواز صدای ۲انفجار ساعت۲۲/۳۱
همین الان اهواز صدای انفجار اومد
ساعت ۱۰/۳۰ شروع شد مثل هرشب
سلام آقا وحید دو انفجار پی در پی اهواز ساعت ۲۲:۳۱
اهواز صدای انفجار دو بار ساعت ۲۲:۳۰
سلام داش وحید اهواز ۲تا انفجار شدید الان
اهواز ساعت ۲۲:۳۱ صدای دو انفجار اومد
دیشب هم دقیقا همین ساعت شروع شد
هر شب راس ساعت ۱۰:۳۰ اهواز میزنن
امشب باز ساعت ۱۰ و نیم و دو تا انفجار شدید
سر ساعت، برنامه زمانبندی خاموشی هم اینقدر دقیق نیست وحید.
🔄
دوبااااررره
وای وحید دوباره دوتا
۲۲:۳۴ دو بار
اهواز ۲۲:۳۴ انفجار مجدد شدید
دوباره دو تا صدا پشت سر هم اهواز ۱۰:۳۵
انفجار ساعت ۲۲:۳۵ اهواز
یه انفجار دیگه 22:34 این یکی شدیدتررر بود.‌یکی دیگه هم دورتر
دوباره الان زدن ۲۲:۳۵ اهواز
اینبار شدیدتر
خیلی وحشتناک بود
سومی و چهارمی الان ساعت ۲۲:۳۵ اهواز باز روی لرزه‌ست
وحید دوتا همین الان اهواز، ساعت ۲۲:۳۵ خیلی صدا بلند بود
اهواز بعد از اون دوتای اول یکی دیگه الان زد ۲۲:۳۵
۱۰:۳۵ یه انفجار مهیب و بزرگ توی اهواز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77156" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77155">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q6zlvITq41Lxp1hHXzRZBEgJB04TjLm9LSGRc9G-R_YsZD4CVDon2Uj_sFigvmN-b1iSGFv8LZdikajlBkFVaYEkuIAwn1nFMXj7UTcayrUmvD0-ub6_qFxfSzhZxUTRPaFc2C8J4F_8k66sLPAJ0U8mA7bzHP6NiyAKoGxThym9h_UwazG7fg8i_--_RBvIj8OAZyLjsZPCI4BBTbo1gS1j3gX5vAQdOhZ90I8t3c5hfFTFTFg-P__n3PMtnFvqs3GvsN3gNjfml3AhVFH-L4jBMXgT21odclABcAeMX12LCq_Kw-17VPTCbVSJ64PQFzTIlwCxuVgDuFf_fhveuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ساعت ۲ بعدازظهر امروز به وقت شرق آمریکا [۲۱:۳۰ به وقت تهران]، نیروهای ایالات متحده برای پنجمین شب پیاپی اجرای موج تازه‌ای از حملات علیه ایران را آغاز کردند تا توانمندی‌های نظامی ایران را بیش‌ازپیش تضعیف کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77155" target="_blank">📅 22:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77154">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c552ed27a.mp4?token=lTe121xsnpEOKVuob2eQqyThVc5O6HNY8pO_4jITzcFzNGk_DCpFJcHfnCgs3ejszaK-8qYbZvuQsgPg66gyS3skOJDmseIjThEUM2piL_2uFkiEClVkRz-eL2Pr3Qs3n1b1Y10Q9YQQ40caOsvywwrVy8M_U41z3g6Qc3svAs1WEme_SuWFFZNIMLmUbcfo02ZPc65hp7UKYzg8YzU0SX99kt-TMgfpGD4Ak64M0sMxXrl3xgY4AKmGxgxkEVEXGd7JzS-KNxw4r8LzJLR8sxX0HN5StqRjDpHDoTfcoVj0cSDcVV9uUvXmzBwoZc_iSmIFS5YazzCJt6GYF4fROQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c552ed27a.mp4?token=lTe121xsnpEOKVuob2eQqyThVc5O6HNY8pO_4jITzcFzNGk_DCpFJcHfnCgs3ejszaK-8qYbZvuQsgPg66gyS3skOJDmseIjThEUM2piL_2uFkiEClVkRz-eL2Pr3Qs3n1b1Y10Q9YQQ40caOsvywwrVy8M_U41z3g6Qc3svAs1WEme_SuWFFZNIMLmUbcfo02ZPc65hp7UKYzg8YzU0SX99kt-TMgfpGD4Ak64M0sMxXrl3xgY4AKmGxgxkEVEXGd7JzS-KNxw4r8LzJLR8sxX0HN5StqRjDpHDoTfcoVj0cSDcVV9uUvXmzBwoZc_iSmIFS5YazzCJt6GYF4fROQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود از حملات امشب به بندرعباس است. @
farahmand_alipour
پیام‌های دریافتی:
سلام وحید بندرعباس ۲۱:۴۴ صدای میاد نمیدونم پدافنده یا انفجار
سلام وحید جان سه تا انفجار خیلی خیلی وحشتناک همین الان ساعت ۲۱:۴۲ بندرعباس
بندرعباسم
دارن میزنننننننن پشت هم
۹:۴۲ چندتا انفجار شدید بندرعباس
ساعت ۹ و۴۵
بندرعباس ۳ تا انفجار وحشناکک
جلوی خونمون بود
سلام وحید جان، همین الان ساعت ۲۱.۴۲ سه تا انفجار پشت سر هم بندر عباس
سلام بندرعباس ساعت 21:43‌چهارتا انفجار
بندرعباس همین الان چندتا انفجار وحشتناک رخ داد
سلام آقا وحید غرب بندرعباس منطقه ۴ ترکید ۵ تا انفجار فوق العاده شدید
3 تاانفجاربندرعباس
نیروی دریایی ارتش غرب بندرعباس
و ایستگاه رادیویی بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77154" target="_blank">📅 21:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77153">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH4KI0-o6ThV9M3k-lTCkY5K3BxFY8CiXjgS3IfM5VYhWr_yQ0UYEq5rp-pyc7P7rtClMihLfOneEa3v96srcNKHNOwWf83WU481NntOxJJsXPbGxgrxqlP47TqNvkkGYX_Jr1a-MBd5LIUUfg8bhoMzJqMGyK5jvuA2cNDBiFoJamXmNKeKyQuu2RrHrPzu16i0s2sy7_XBI42a0tRpfrje79fSP2XStgHczVKYARilzC9kp4Lh3bxPGyI6V_ybhbux7Jkds9kamGqJW_cO-EO4Vhw4TyJDxzAnp3mwqQ6K-8SUN8Ofm6G7cfUHo6g9pu7WJCfSju98GqTIoorm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس:
🔹
استانداری هرمزگان: در ساعت ۱۸:۱۰ نقطاتی در حوالی قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.
بندرعباس:
استانداری هرمزگان: در ساعت ۱۸:۲۰ و ۱۸:۴۰ نقاطی در حوالی بندر عباس مورد اصابت موشک‌های دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77153" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77149">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/puXOP0rqBfbAIfGf4ivvUeVzAfQIWt-9DO1FuT7I42ACcdUg3M0wlhv2ZcyCjQNLUNmLbLcOTDaW4ChzcpJcrme6r3LmtxdSqAYu-zsIs2sgDRBgOuP9W4snkh4d_h4YV03uxlZwOQ13eeBXAua9Lpb0oV7UIyAWpTihgBsxPHjoSj5PTthqKZl_6R5Puux4n0Xb3PwKJ_JcUN29q5FGHfY3G0GIElOCtIsjSZmbv5Fa9cV6Z65xykepQiJ_MMFt1FwpvTfpkeNMCZX8u-TPRUJUtv3z_16Y6TIsEnAeG6ZzE4xw2xkgQ359eAva-IAsUBuyZLsveLlTGoYROawb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V9HdbkeflKiWlxtAzc1Eo0iI64QizEpu8I8_EwT1Ckd2p3_jAymhVKiuaYcBsDOBLxchsYRgTSFqt0kQt5Zd8vwBtw6imWux6phQDXmGECIg_QOTFL5EDh5jXSb3XzGx3m1_X2sIuNIxR5NyPoKSrF3bJehyE-iD0uzwMmzCMvkhpYXhdz1ab4NWaldvvBZbtjc57WPsK1ixkEObycwPbpA1NuQ5Yin3mmEJxZWLJHXVTOS1sTf5_kS2-tHbCevf8cOZj50FgwyTrgb2bS2-rCZqnJaut_EjydpU7bKp3s9BK2itlOgVm-_AWbbMCJw7JlNBLjndm2tM6K7AgOKsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zn9Mbwyt6jMczEcMzrtwAji2qj-7LQNHKHdwP0aCyiOnDChhCXyKR9ALAWijespCY1Mwf2e_tBPLM65koXkHcjBezC-b2vQmQv39Ymrq5kgKk1QIG9L2-P6hqe3wDW8nTRYFS_0sq6Nhd0wZcb7B5MB9pbZzP1kWynWpIuW9nZVd5GS0reVA0ejYWMltc34A_0Ph7cMtHL9VUG3PUG75kxUr3Gz2U2IsIS9fvISrL3NyLIslj0tCOgl-OnpflXB6w-bTxgfTJ-cDDrj_K6UU-m1qy4lTbR2NOykmGeeNUNn-w3Tb3pNnPU9CqlrbOeRhufdNml5quzYo8gllhC6D3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96d56893a8.mp4?token=TWdl2OjGGka9ZfRbd5qECgVR2uGrR8lIotMAZ0PxXiYxN6-Oe3tySB94HA3uVya6N6HLs2Dm9lGCPSoZgiAtw5bMskiMnMV4uY7ENnPj5VXGv_jxg2zNtu8CK0UKWZU95uwuS9GWFA6QZxoLjrgeFCr1BQR6PGBKTs6sY88Q-rGAZHBxoO1BEJwkuFzRkmkZjsjsNWlKTXFIObtu0gvrSBLNaEVyMggC9kzx3sF05lOyCCp4DRbrIfVT2dolmp7Sr2tg0hpPHDxwfgC5oe5fDgE2nCPqTIxourLNKd0NWdzlu6OkYAYYCLfJYiAN9ChGCM5YZymRdb33maoKkIw40g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96d56893a8.mp4?token=TWdl2OjGGka9ZfRbd5qECgVR2uGrR8lIotMAZ0PxXiYxN6-Oe3tySB94HA3uVya6N6HLs2Dm9lGCPSoZgiAtw5bMskiMnMV4uY7ENnPj5VXGv_jxg2zNtu8CK0UKWZU95uwuS9GWFA6QZxoLjrgeFCr1BQR6PGBKTs6sY88Q-rGAZHBxoO1BEJwkuFzRkmkZjsjsNWlKTXFIObtu0gvrSBLNaEVyMggC9kzx3sF05lOyCCp4DRbrIfVT2dolmp7Sr2tg0hpPHDxwfgC5oe5fDgE2nCPqTIxourLNKd0NWdzlu6OkYAYYCLfJYiAN9ChGCM5YZymRdb33maoKkIw40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرستنده تصاویر: پلیس گفت اتوبوس خراب شد پیاده شد تعمیر کنه خلاص بود از ایستگاه پله سوم تا پله اول رو رفت.
آتش‌نشانی: یک اتوبوس متوقف‌شده مقابل پارک ساعی با ۵موتورسیکلت و ۲خودروی سواری برخوردکرد.
اتوبوسرانی: بدون مسافر بود و پس از عملیات امدادی و رفع نقص فنی درحال جابه‌جایی بود.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77149" target="_blank">📅 19:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77148">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e1540b68c.mp4?token=JdP1cISI4TnB26w7PLsfZMS3QyyvbFDTP3mnZFzyVV_jxPYiNQLJ7rjR1QmGqwtN4HSrhmdzuKDdQMaq5aYINf_AXbrQNmS77F7mUI1AlU_h1Yk4YDTdwcb3MyQjhe7977i03FVSHkdtpvcJx79aJEz_V4kdYuqHf4u313YU5YK_gHbMk7vKaTWdxysIxKpHRV73Vx93-GLLAroz05zwZyqI90TFt5IRUaaa6GmkEGXXbKCJXrAIKeTyV8GHyu6SkJDoxPSNLkcI5-NLUc-kzA_qhNklxJjJBDOcNF4nBoq0TIICJKcUwrmtNobUxD7U39sS1k23r4tr3tClcO2DM2SdF7eIDHW0LJN52vQ0DsEZgthLjaw2rmuyDQidw8hsNoeOI2sXNZN4SIkQTYulRUfu9cp6bSB7-BGkEHyZQUZ1KMOm26k4yKVlfMdH1qeUnP3VhJJG8XWGhEsI_gQBmPoz4XTAHnlg1UEamDZsV62w-KIg219ABOGyEcpJEh6CuHNA5bEAAW21_8CpQsjQlNv8ikUqM-an1Qssxj4wxigIf74udL6LWtQBIecGM8TLWZ-wQD9xABmALnh23CTiDviFboTA44_nNMMMDmzEWWECKSB3LIcmze5Z21d1tG_7hskSiPTvZ4L8bCHVf700M95ZZg5_NZgty5YW6V3cfCU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e1540b68c.mp4?token=JdP1cISI4TnB26w7PLsfZMS3QyyvbFDTP3mnZFzyVV_jxPYiNQLJ7rjR1QmGqwtN4HSrhmdzuKDdQMaq5aYINf_AXbrQNmS77F7mUI1AlU_h1Yk4YDTdwcb3MyQjhe7977i03FVSHkdtpvcJx79aJEz_V4kdYuqHf4u313YU5YK_gHbMk7vKaTWdxysIxKpHRV73Vx93-GLLAroz05zwZyqI90TFt5IRUaaa6GmkEGXXbKCJXrAIKeTyV8GHyu6SkJDoxPSNLkcI5-NLUc-kzA_qhNklxJjJBDOcNF4nBoq0TIICJKcUwrmtNobUxD7U39sS1k23r4tr3tClcO2DM2SdF7eIDHW0LJN52vQ0DsEZgthLjaw2rmuyDQidw8hsNoeOI2sXNZN4SIkQTYulRUfu9cp6bSB7-BGkEHyZQUZ1KMOm26k4yKVlfMdH1qeUnP3VhJJG8XWGhEsI_gQBmPoz4XTAHnlg1UEamDZsV62w-KIg219ABOGyEcpJEh6CuHNA5bEAAW21_8CpQsjQlNv8ikUqM-an1Qssxj4wxigIf74udL6LWtQBIecGM8TLWZ-wQD9xABmALnh23CTiDviFboTA44_nNMMMDmzEWWECKSB3LIcmze5Z21d1tG_7hskSiPTvZ4L8bCHVf700M95ZZg5_NZgty5YW6V3cfCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خون در ۲ ثانیه اول)
صدای ویدیو: "اتوبوس ترمز برید، هرچی موتوری بود رو زیر گرفت رفت. خیابون ولی‌عصر"
به خودروهای پلیس هم برخورد کرد.
Vahid
تهران، پنج‌شنبه ۲۵ تیر
via @
iliaen
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77148" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77147">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/71f1bffd36.mp4?token=mEUgDnlYzvyb-j926GSyaAD61xJRXtbB5n5xEvLKudBC6235MCGzgFRXItBqweE9clOmgdnmFHPmC-WA0DquEvK9ziWCvpsevZecZBrQFgeIZsCLqkl0ivyJbHCF-c0psE8XOBZk_obruSzcwSbk9nkYKYINvBngZz5iwQqPPMn7D0geJeMMfg_jD0SwVkOVZgpNngq5-db8qEUwIrxN-cEWfSdp_f33XqZ4Ji_sj2pV9BfhD5VIqK8JzHTK8t71kxbcAG_ghrH8OLCflFpxD-2YhdBEp5VYfKdtCBTdr-dxjfG3fw5p3A_Cs1DJgl-mp2JenubdGAOTIAUbZJ6kFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/71f1bffd36.mp4?token=mEUgDnlYzvyb-j926GSyaAD61xJRXtbB5n5xEvLKudBC6235MCGzgFRXItBqweE9clOmgdnmFHPmC-WA0DquEvK9ziWCvpsevZecZBrQFgeIZsCLqkl0ivyJbHCF-c0psE8XOBZk_obruSzcwSbk9nkYKYINvBngZz5iwQqPPMn7D0geJeMMfg_jD0SwVkOVZgpNngq5-db8qEUwIrxN-cEWfSdp_f33XqZ4Ji_sj2pV9BfhD5VIqK8JzHTK8t71kxbcAG_ghrH8OLCflFpxD-2YhdBEp5VYfKdtCBTdr-dxjfG3fw5p3A_Cs1DJgl-mp2JenubdGAOTIAUbZJ6kFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77147" target="_blank">📅 18:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77146">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FFLwi1b0k-ELOkA9JuPy6RkMvDx13xaOQhQri6lLXk5pYwbLpMZ3I4CkdSuNu6dVKnUovOCinfCf-V6Aj-VhQo-sNpMJZdv5m56uXsDq-ku1RHe85d_WEGg3ypuJ1Pi-ldqx_VdUIkMTeDp-DBQBurRDxDslPOjPxU69F5AzcldC3WELvQTfMNjAxtCzPQwLTv5NdcIAknpvznG2VpY8HOyL-pZm_S57rnFdeGBSIwlIUBw0g7tNrbENxm0o-JB1iQfFwGJn2rt-uDf7vaIQOMyKhgFzRxNstkD6Y6eHBbWovwGYC_vv7vO87BBYwrZjD4YHtv2bHOAVgw71LUkcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام استانداری سمنان:‌ در حملات بامداد پنج‌شنبه فرودگاه سمنان نیز هدف حمله هوایی قرار گرفته است.
محمود قدرتی، مدیرکل امنیتی و انتظامی استانداری سمنان، ادعا کرده که در این حمله یک سوله جانبی در محوطه فرودگاه هدف اصابت موشک قرار گرفت و بخشی از شیشه‌های ساختمان اصلی ترمینال نیز آسیب دید.
به گفته او، این حمله در ساعات اولیه بامداد رخ داد و تلفات جانی نداشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77146" target="_blank">📅 18:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOnjtOVChFj5adeNUK_sKdwSdXvqvNDSOlJhbZmKuJPsHqF7eIpwGj7x43AdMNJa0y75mK8MGlqoewoS8A8MJdxi9UpRzfnmGFYIxqw-B0zMhJaSUyQmVLXgdSC8TuqQels35nhioEouoLKjrYUUpz6aR65Q0AjJ6T0_9DnBZS_ILcn1ZD41hA8yqV7dWcOTaXIy-yL-85MZXV1rxrBQUqO_OAyHAEpaM04YBxlg2lmNHSdx9A3pTv9ZWJq6O35YecGnQBxUXFT9FX_3C9pWpMfrteIVOXVXaly_Koh4POKiHIGAh7QctSzGWAzd-u031LCRE8DAoxS5b8wagiAgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امنیتی به خبرگزاری فرانسه گفت که روز پنج‌شنبه ۲۵ تیرماه پهپادی به یک کشتی «حامل خودروهای آمریکایی» در نزدیکی یک ترمینال نفتی برخورد کرد. گزارش شده این کشتی از امارات متحده عربی آمده بود.
همزمان چهار منبع نفتی و امنیتی عراق به خبرگزاری رویترز گفتند که روز پنج‌شنبه بارگیری نفت خام در تمام پایانه‌های عراق پس از برخورد یک پهپاد با یک نفتکش در پایانه بصره متوقف شد.
در واکنش به این گزارش‌، سخنگوی وزارت نفت عراق با اعلام این‌که بارگیری نفت خام در پایانه‌های جنوبی عراق همچنان ادامه دارد گفت که در حال بررسی گزارش‌های مربوط به سقوط یک «شیء» نامشخص بر روی یک نفتکش هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77145" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77144">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ow5OHIV8Tfl9CKCvEKi90Dw13L2kvaHAMLmwi20xMYFJb9SJD2TTgt6B2kye6vrkpAu0eahOUU-pzpce0wI-lbtgje8eQYwAwgoc8He5yRdemhO5luEjDddoTYv2CnS_sZAmzZjET-s6ssnJk5Y058EAVWDTz6Rz23bOLZ33dAoJQ6bDNKhVHLwHVUr3BjbhnsKlOa6W1OPLbencMaDdA06MvL210e5CRXWi7rvuqDuLlLFh_f6w2Pth2NV4n2gnCQas8lNE2rGFml57jD2ys7T_QSBK-zoNOUHG36-MAmmEFsoZNtu94j2weBpEGy3SshCzBpJmCKpFwU5PnqalWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی، وزیر خارجه لبنان، می‌گوید تصمیم برای پایان‌دادن به نقش نظامی حزب‌الله در این کشور یک تصمیم حاکمیتی و مستقل لبنان بوده و پیش از توافق اصولی اخیر با اسرائیل اتخاذ شده است.
آقای رجی روز پنجنشبه ۲۵ تیر گفت که این تصمیم زمینه را برای توافقی فراهم کرد که ماه گذشته با میانجی‌گری آمریکا میان لبنان و اسرائیل حاصل شد.
او با تأکید بر این‌که لبنان «تصمیم خود را گرفته است»، گفت دیگر بازگشتی به «دوگانگی حاکمیت» وجود نخواهد داشت و جایی برای سلاح خارج از چارچوب مشروعیت دولت یا تصمیم‌گیری خارج از نهادهای رسمی کشور نیست.
رجی همچنین گفت استقرار ارتش لبنان در سراسر خاک این کشور، موضوعی جدایی‌ناپذیر از خروج کامل نیروهای اسرائیلی از همهٔ مناطق اشغالی لبنان است.
حزب‌الله که تحت حمایت جمهوری اسلامی ایران است، از سوی آمریکا یک سازمان تروریستی شناخته شده اما اتحادیه اروپا تنها شاخهٔ نظامی آن را تروریستی می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77144" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
