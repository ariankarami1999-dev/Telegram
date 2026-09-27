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
<img src="https://cdn4.telesco.pe/file/S3wgdqW2d8hdyUXkpgTgwpjZP-vOfDuEbH7fOvdFntQX8FpAuMSmJZrQFlg-ndwR4JBpYUqQhRy8s4gE7oymxDbxBsaqeEx3a8k4bNen0v4oXqCrxSTnmqkxL8-ntpQZD-ROeSoPwB5zIoj2fTVwXFP_HEvTbtlD4oosneOI15pOJC0CJDRmX3_Xy523C1aguJRYUcaTUrwOxDCPWtHzKQDsKH37ktyTxzeqRrYc1mZpeydvDZUUvNSbKpdZwJk98ZmEkGAjIgJDgwGLMCSobLUCsDzUWvGbM8260WME-4bcpA9tcSK6wptfafPGyKz3aYVmZtgCc-pa63PVE5B8Rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-72346">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=TFAQ5-qjul784a7IK3utRH2ie51u6m6giZGDF0j8XbrNgoh1pPz2xgZdkqb3q-aSqrGuMgnmW6b37MtyULVTHrk8Nov-nMX1rz_RSLPJl9Q-Svaer6BxY5JRh7WT399-nbSZEPivAc7sg8qVjJVcdFLI5irWJJSnoScdK9e8NlSEdN7hyuKa9foMQ9220EuRzpOWKh5DPIx3IaP5lnOxuo4WDT3lv1JuI8cpZiUxIzp69-YaBzMOHezHlaYPbZNwSSWAjY2_SKa_yY6FeyPfprio1_0_ySdAlQpHyIbSwvJBzy5jm-6pqfFIcdYVoMHC_OlL6fAZtj7Nf7kjol-nWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=TFAQ5-qjul784a7IK3utRH2ie51u6m6giZGDF0j8XbrNgoh1pPz2xgZdkqb3q-aSqrGuMgnmW6b37MtyULVTHrk8Nov-nMX1rz_RSLPJl9Q-Svaer6BxY5JRh7WT399-nbSZEPivAc7sg8qVjJVcdFLI5irWJJSnoScdK9e8NlSEdN7hyuKa9foMQ9220EuRzpOWKh5DPIx3IaP5lnOxuo4WDT3lv1JuI8cpZiUxIzp69-YaBzMOHezHlaYPbZNwSSWAjY2_SKa_yY6FeyPfprio1_0_ySdAlQpHyIbSwvJBzy5jm-6pqfFIcdYVoMHC_OlL6fAZtj7Nf7kjol-nWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای ایشون در مورد مظلومیت پسرا، بیشترین لایک ۲۴ ساعت اخیر رو داشته:
پسرا از یه جایی به بعد، از بس کار دارن و به فکر آینده‌ان، حتی یادشون نمیاد که کِی تولدشونه!
ولی همینکه یکی باشه و بهشون بگه تو چقدر برام مهم و با ارزشی، اندازه هزاران کادوی میلیاردی براشون ارزش داره!
@News_Hut</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/news_hut/72346" target="_blank">📅 10:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72345">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2CGP0CT_ZgnJAuY68Bf6DpfJLDFyr0Hlq63FAlV8Y9YqCZXaTy313PZdOx3v7JDZurjaPi-vVqMUS3bLv22arBDOMFLxhFC3yj1l3EBAHMMH4FbJ9qFTUnKF1DdWa5n9m8GVHRqyugwZQF43m5hl_dZBy8kgWxzAkjTeEad6blQjdZsxHg3ec8m6hzQEZpap5VA0bnGbRolYX1yKCzRaW3T5yp3XkEHC36at0YHauQNmTgeCn_anfk40AGs6ho14Je_2vAH-xvnTeQqspgVNatE-pZUBgMeFJ4PPwZZxH_wtrNRvGRmzv9KVRps9o6INZM3lBnl6vtOGqrNmpMIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارشد نیروهای مسلح جمهوری اسلامی :
قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/news_hut/72345" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72344">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=jJEn12rOqdLjNUceTRz7sJMA9tFQ5fs8C2AjvzMkIMPA-ix7tN5JgkgbBj20dtI5Z2rivoPtMyWnuU1kTaF3HCLDWf832O03fNYDBT_ygzapo35oKR1Y0S1-YO-Ngqll4OGzncIVUQLNx0BdPwkMdpWpaAUIaTQXSU7iiIMHLcjbE4LYQ-zAZzfknaVxhWBdB7bPDIRRMwq4_0GD0tbaTinBk3MQUwSi6fxdLvyEKT2z7HvWXUSuqjevT1XTtyP_Y31gTLC5M9LpF97eeOYanOdy-YLa04owf7exOPCGyB9bGM_PYocFJDrqUtjTHhce_FBrsQfGJM1lunaniF6ezA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=jJEn12rOqdLjNUceTRz7sJMA9tFQ5fs8C2AjvzMkIMPA-ix7tN5JgkgbBj20dtI5Z2rivoPtMyWnuU1kTaF3HCLDWf832O03fNYDBT_ygzapo35oKR1Y0S1-YO-Ngqll4OGzncIVUQLNx0BdPwkMdpWpaAUIaTQXSU7iiIMHLcjbE4LYQ-zAZzfknaVxhWBdB7bPDIRRMwq4_0GD0tbaTinBk3MQUwSi6fxdLvyEKT2z7HvWXUSuqjevT1XTtyP_Y31gTLC5M9LpF97eeOYanOdy-YLa04owf7exOPCGyB9bGM_PYocFJDrqUtjTHhce_FBrsQfGJM1lunaniF6ezA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟؟
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
@News_Hut</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/news_hut/72344" target="_blank">📅 09:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72343">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjjRho10B0MqJnfCEJwI9LaxBK4_7jiEWhx9hNjw2Uk80gFHNzZHq-somvoQubUtF7m58LsKmhTJcfq1m6bAUPVaMXGT88JptMwMF7H9tIVgP7gTlQRouLTEsIcFgx8-gYSbMqmTZG79MXN7MCy0epf-qBAQFcNXsbXswLEC0nvph5JDFkOCH41ZEnJheUe2cqg1mfN4Vu7euoHcQkqLl247RP-1FG_JqVFT4x2bio_rqtRd-pTSZcw6eu0F8qqSsi8rTBto7ocSKOGnBN2X37tG9_stlEW3RR6w84tpCB6IMjKQ1WGsK7mi46v6zwpsmM1vAMFvxewho87SDnekMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال‌استریت ژورنال، دولت ترامپ فشار اقتصادی خود را بر ایران افزایش داده و از کشورها در سراسر خاورمیانه و اروپا می‌خواهد تا روابط هوایی و بانکی خود را با تهران قطع کنند.
جاناتان برک، مسئول ارشد وزارت خزانه‌داری آمریکا، این ماه از چندین کشور بازدید کرد و به شرکای تجاری ایران هشدار داد که باید بین انجام تجارت با تهران یا واشنگتن یکی را انتخاب کنند.
در پی این کمپین دیپلماتیک، عمان، امارات متحده عربی و ترکیه، پروازهای ایران را محدود کردند، در حالی که مقامات امارات، تراکنش‌های مرتبط با ایران را توسط بانک ملی مسدود کردند و ترکیه، مجوز فعالیت بانک ملت را لغو کرد.
آذربایجان و گرجستان نیز پروازهای شرکت‌های هواپیمایی ایران را محدود کرده‌اند، در حالی که بریتانیا قصد دارد معافیت‌های بانکی را که به موسسات مالی ایران اجازه فعالیت در لندن را داده بود، لغو کند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/news_hut/72343" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72342">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72342" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72342" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72341">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj56Cw4WBmRUjaS7kYngHQHCHc-ezC2RnsdlsU3AxsMCgc40kGOjnAeNqFF5SjSfGYelIytQY-2EeCB-a5L_ts6KcWNQylABb6jjTebMF-9ifJQ7wtFcHlQPlNp0pXwBEaoY6FpjJn8AL6rkrXM2K3R1hcW3ccjzjAeznnerOAtFBsXtXzYVyP9b1dkEDl6Ie0VDF1IEbL9IC1ggI1HmM1t2yaqBRx_zwWvY7hob-hOMfLksUKe3MZt7s6SZ__80TZ5UpFsG47YDqY9EZpU_PrAEgMkIh3MWqxSBnwyf2iu8kALJzr8kyGcDuScYgB3rSYlRljn1G3Fj4HAz2cO00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72341" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72340">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجار های جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72340" target="_blank">📅 01:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72339">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سپاه پاسداران:توی جنگ بعدی ناوها و ناوشکن‌های دشمن حتی توی اقیانوس هند هم امنیت نداره و قطعا هدف قرارشون میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72339" target="_blank">📅 01:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72338">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72338" target="_blank">📅 00:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72336">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ایلیا هاشمی:
ساعت در محدوده ۰۰:۱۵ الی ۰۰:۴۰ بامداد یکشنبه، چندین انفجار مهیب همراه با لرزش در محدوده تنگه هرمز شنیده شد.
تحرکات نظامیِ سواحل جنوبی هرمزگان در کنار تعداد و شدت انفجارهای امشب، نسبت به دو ماهه اخیر بی‌سابقه است و می‌تواند گسترده‌تر شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72336" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72335">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72335" target="_blank">📅 00:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72334">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی رفته نیویورک گفته اگه این هفت تا کارو بکنید تنگه رو باز می‌کنیم، اونام گفتن مرتیکه جاکش تنگه که دست خودمونه پس صیکتیر کن تا پیشنهاد بعدی
و این شد پایان این دوره از مذاکرات:
#hjAly‌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72334" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72333">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=iBP6Z7NohunVSfTHEwI0lQ1YdPpWO7-_2rCV-S40lW84MFSalr7bGwhzm-jiYMjeWXA9dRE7Cka2W48bAoI01UutBO0p_wTrC9ABJ9MlgvaZMvmJqT83h2gA9StoEJgNo53yHkR5ctVpRqo2xnpY88uYJQWSLS74vceP67wK1Lf5-SVcfBor4PFv72EBdpJ_I7maSn-Ol9YSgQBTiZdRt3mm2JSRgeQzJ_yEingFl4N2-1w0bWDfHQ8Wd_-OCBKRVQHPQjW0-91GhuV8nKSRkdcgodN1lAjcgtEmFteavCvNyP6GVPpSJfBpBXklab7pWtSeGc9b8LzGVCoTqA9hbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=iBP6Z7NohunVSfTHEwI0lQ1YdPpWO7-_2rCV-S40lW84MFSalr7bGwhzm-jiYMjeWXA9dRE7Cka2W48bAoI01UutBO0p_wTrC9ABJ9MlgvaZMvmJqT83h2gA9StoEJgNo53yHkR5ctVpRqo2xnpY88uYJQWSLS74vceP67wK1Lf5-SVcfBor4PFv72EBdpJ_I7maSn-Ol9YSgQBTiZdRt3mm2JSRgeQzJ_yEingFl4N2-1w0bWDfHQ8Wd_-OCBKRVQHPQjW0-91GhuV8nKSRkdcgodN1lAjcgtEmFteavCvNyP6GVPpSJfBpBXklab7pWtSeGc9b8LzGVCoTqA9hbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پریشب تو تهرانپارس، یه خانواده برای مریض بدحالشون با 115 تماس گرفتن تا آمبولانس بیاد و ببرتش بیمارستان؛
ولی از اونجایی که خودِ آمبولانس خراب شد، همراه‌هایِ مریض مجبور شدن تا نزدیکی‌های بیمارستان هُلش بدن:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72333" target="_blank">📅 23:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72332">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=ubXIUUCubIvv5jpHDyoMBIQwbLDMgVpFLFZ42_rKRRNnYF9bYF2HDPrIuIeTH7iH2BX5Air12H2AlHM0E4tnJNd6gUVvzad5NbJ_F6dXnVbSpA-rSbXmov0TIE5YFbD_kqih3kZ4PM-j0FNgeApXFIGMs_a16ymkjouVppKBye5JF1KdsLFUVHL556JZidWUEVxya_hbekbEdjaZZvHoYmlmG4tzIUEfIJ4_WnPjdnjgznmUkA6QbQEAPmPADwyAbzE7Vt5Po6w8uugeAMFbP5WUjOn0i9K2tSrNUV_G_3ZReDdIR0W--xOIvLgVWv2mS157aQweDE5c3M_tBDIsbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=ubXIUUCubIvv5jpHDyoMBIQwbLDMgVpFLFZ42_rKRRNnYF9bYF2HDPrIuIeTH7iH2BX5Air12H2AlHM0E4tnJNd6gUVvzad5NbJ_F6dXnVbSpA-rSbXmov0TIE5YFbD_kqih3kZ4PM-j0FNgeApXFIGMs_a16ymkjouVppKBye5JF1KdsLFUVHL556JZidWUEVxya_hbekbEdjaZZvHoYmlmG4tzIUEfIJ4_WnPjdnjgznmUkA6QbQEAPmPADwyAbzE7Vt5Po6w8uugeAMFbP5WUjOn0i9K2tSrNUV_G_3ZReDdIR0W--xOIvLgVWv2mS157aQweDE5c3M_tBDIsbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز داخل تهران اولین مرکز آموزش نظامی برای جان‌فداها افتتاح شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72332" target="_blank">📅 22:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72331">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=X6doSJD68pslBZnJjRTARlCCeuVNMPW7C7mVYpeLAY52nhKymepLPzj0BP0ET0EPSBTBmph0ZbwHyCVP_K1a6PFXYsw5YJDgbxfFRWIR_2l_LNyLTiuOLHz-Xvmofkg2Yj-OreZaJwhpszUmaNUkTJbe7oaLh6hqX6GU5ytlggCSETtqko1KyLw9Ktw2J5CXw9mYKQmPyk2Wl9jIEjka5sL3oCt_GoLTIYMPdMavv-yGcP1hwNQ1Fnw3eh5RLHYYThP8v57DNmrTK-LSatZE-j4owRxPKp3bQ8lPpWIOe21xyfPkJTUz_6H0kZ8diET08I9Wz_r7bKiHlcnSqU7rgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=X6doSJD68pslBZnJjRTARlCCeuVNMPW7C7mVYpeLAY52nhKymepLPzj0BP0ET0EPSBTBmph0ZbwHyCVP_K1a6PFXYsw5YJDgbxfFRWIR_2l_LNyLTiuOLHz-Xvmofkg2Yj-OreZaJwhpszUmaNUkTJbe7oaLh6hqX6GU5ytlggCSETtqko1KyLw9Ktw2J5CXw9mYKQmPyk2Wl9jIEjka5sL3oCt_GoLTIYMPdMavv-yGcP1hwNQ1Fnw3eh5RLHYYThP8v57DNmrTK-LSatZE-j4owRxPKp3bQ8lPpWIOe21xyfPkJTUz_6H0kZ8diET08I9Wz_r7bKiHlcnSqU7rgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرازیر شدن موج جدید افغان ها از کوه‌های صعب‌العبور به سوی خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72331" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWrqRm4-b7rZgNNrC1d_TkSQagMJJ6XLxvHM7oVrzy8If9GD8LhcjLtn9g1YdKSZQoQ0fnTy-71bf6-9y3UjRwU0BaTb7bhd_IUuuQWWjQstWMZ50ozAjaw5jnjrPP1sJXfvEQz9BlKpGOhgD_9GYQ0VPWtpP_GmgzsttSfRVPXOzJe_dvL_2tsqSEHS8tjEVAKqlTTSPhntFTz6kIB5bGSodXCHO16FyjahXl-EkJ3S5_HpqQKj4iOVfyekkx5eeQ-VK54ef2q_UjeJNY3lRBTqWFSD4rmEiF03I-bQSVlVUJTNiwNzVbp636feBTOxCnK3W4gvzwFxl3BiYu59oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=UQ0vJzfNPWhoZuZdvgxfEXiSomTTXOg2meYDSTRiPb6s9m11sYLoE7OykN24qFlPmjMCoXz1RV354YQCi8L7N3xJhhPwiJ5jMUR54Q2qJG8fSppLN3OrCH9U0frq9GwR37dK3RYq755waMhLkvnii1z6nE4T7FkgVgYQkR6WFGMiBAsb-7kEmlgh8eGHxXG4dUicNsElXqZ8nrMGTRvg9yJbV_3tRHopEMmdRopz_LK-E-0hrJ-tc9Lb-ehcHasiOCgzI3xL6xbTdigaI0aNiG5CqXV36BnFQBkNtLy0kPWsqZ8YpRkWbVysaViydhLV6mN1IamsLcdl-jjn3EtBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=UQ0vJzfNPWhoZuZdvgxfEXiSomTTXOg2meYDSTRiPb6s9m11sYLoE7OykN24qFlPmjMCoXz1RV354YQCi8L7N3xJhhPwiJ5jMUR54Q2qJG8fSppLN3OrCH9U0frq9GwR37dK3RYq755waMhLkvnii1z6nE4T7FkgVgYQkR6WFGMiBAsb-7kEmlgh8eGHxXG4dUicNsElXqZ8nrMGTRvg9yJbV_3tRHopEMmdRopz_LK-E-0hrJ-tc9Lb-ehcHasiOCgzI3xL6xbTdigaI0aNiG5CqXV36BnFQBkNtLy0kPWsqZ8YpRkWbVysaViydhLV6mN1IamsLcdl-jjn3EtBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله یه مدت به خونه صمیمی‌ترین دوستش که مامان باباش طلاق گرفته بودن، رفت و آمد داشته.
بعد از یه مدت، دختره رو بابای دوستش که ۴۷ سالش بوده کراش میزنه و مخِ بابای صمیمی‌ترین دوستشو میزنه تا باهم ازدواج کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72328" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=DwHM7C2l0F8dcamNTPVdb6M67rLDHUlOMAh4eOZjtShQE4-HTQimBKC6tWVXthElZKR6CPI6WPgOAY3ckv3ruHynkBik2OJVPgVsLxa9J8n6poc5w2NKlx4X--3wLIObeHpiuaa2NAs_1wmDEL-RJq4qcu9F-m3yn6HLXeZU3NxUw-3AonQJEG6DRCMUQGyulg5OwY42DNBpAwfh-B_zol9Wo4VjCHo-9pxIf307g6JVfJTDuRlvYp3p6CxdRrVAOj-6DHuKQgtVJPpAdf_bZ0lp9pmS7n12oBzD1ajWL7HQTWch5_OOwJ0vRQs-6-Az54VexGvPYE6RM1CXyf6hgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=DwHM7C2l0F8dcamNTPVdb6M67rLDHUlOMAh4eOZjtShQE4-HTQimBKC6tWVXthElZKR6CPI6WPgOAY3ckv3ruHynkBik2OJVPgVsLxa9J8n6poc5w2NKlx4X--3wLIObeHpiuaa2NAs_1wmDEL-RJq4qcu9F-m3yn6HLXeZU3NxUw-3AonQJEG6DRCMUQGyulg5OwY42DNBpAwfh-B_zol9Wo4VjCHo-9pxIf307g6JVfJTDuRlvYp3p6CxdRrVAOj-6DHuKQgtVJPpAdf_bZ0lp9pmS7n12oBzD1ajWL7HQTWch5_OOwJ0vRQs-6-Az54VexGvPYE6RM1CXyf6hgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه مینی رپر کوچولو و زیبا
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72326" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIkhSQ7uQVAGNQLH92H_i1wlp7DT3iCLlkWIKrrmBqebMyJqYweJVekW07r99aQWD3qAGrCkZO77YE_80d4YwsvlpBRzkJZZqX20HmrkwOlRiRwVU6qd4EMY5jNq9neU7_g0PEe2hhzSy2nSrQqqaZgjD0ZsIaVUP2aqv3S_7Zj7MMAs82hk1zFC5WKn77RhMIwvz7FNlyhHH_vjyqQa0bWYVyxv7vzvuJ2Oq0XrEZIofhagx-9naiAbtTaYEHVtK6BtnuzN4MfxJS9ajLuMqTQS6cMxn5_y7eJ27OCtNIXOZAsebMnWLG4CLVnP6Dorcm6zWX7My73GgFaS2OV8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر!
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72325" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">طبق گزارش های تایید نشده، عباس عراقچی بازگشتش به ایران تاخیر افتاده و قراره سه‌شنبه ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) از نیویورک به تهران برگرده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9470296462.mp4?token=hIEF-9kjoJY6vwqLOpI3jgfiuGKgsvX4Mv5EHdnlLoKVT4yrltJsBHzHDOu1vlvx-QiSMJddrB9olJqroUEtmCPbgiJBOE00IPt3juCetOaja4Q0WTR5brjeNq39frCCyxNs-wADDP2_HCmIDzgs-cXUN3aeeMn_nn_WENUvXPCoaX0UrhwQ18bhP4bO3OW_vM9TVgjSIWb1r2DhayclpSlqf0V4_gkOoSvlnGRG9EBNpQKpH08BamrI-eZzM7qy5guvJB4UkdQZlfANwtkVKAFfftaMTxFMBJPyHkZB7n0tzzoofJwXDoqP1L4aSMgt76dFZdxJr7QVT8kp1fQESQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9470296462.mp4?token=hIEF-9kjoJY6vwqLOpI3jgfiuGKgsvX4Mv5EHdnlLoKVT4yrltJsBHzHDOu1vlvx-QiSMJddrB9olJqroUEtmCPbgiJBOE00IPt3juCetOaja4Q0WTR5brjeNq39frCCyxNs-wADDP2_HCmIDzgs-cXUN3aeeMn_nn_WENUvXPCoaX0UrhwQ18bhP4bO3OW_vM9TVgjSIWb1r2DhayclpSlqf0V4_gkOoSvlnGRG9EBNpQKpH08BamrI-eZzM7qy5guvJB4UkdQZlfANwtkVKAFfftaMTxFMBJPyHkZB7n0tzzoofJwXDoqP1L4aSMgt76dFZdxJr7QVT8kp1fQESQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عده‌ای در فرودگاه مهرآباد و شعار علیه پزشکیان و عراقچی
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72323" target="_blank">📅 20:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=gsZVspe5EndsxTpJrI8-i55S4Zzz19_iMRoGs7WDCCkfP5xJ4nuCMooWIKGdGBGNLYR8Bbw7uE5kArscbv59Job1_GGWTO-PLjN7eryufY7xtYZLAkWnyLw_9fANdRfYvsjwp5kibQaRwDhUXRMXpRsYDcgB0PS5oKTdAr3LMryej38y0l_ubY3SkYfshUYjxlpPKG7jvD00DQDCe04fVjDQheg-b6B0IA-a3SLB_3cTCrXHk-VdARwbftQRtD_ZX-hdzK1oUZ7Vaf3b9Ms9BA4gxQVZVFI0JwJ1o_rsuafgjkrfD7zpUleynl1YrKnxCbcUGBTVkx6IjhxWTBvR2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=gsZVspe5EndsxTpJrI8-i55S4Zzz19_iMRoGs7WDCCkfP5xJ4nuCMooWIKGdGBGNLYR8Bbw7uE5kArscbv59Job1_GGWTO-PLjN7eryufY7xtYZLAkWnyLw_9fANdRfYvsjwp5kibQaRwDhUXRMXpRsYDcgB0PS5oKTdAr3LMryej38y0l_ubY3SkYfshUYjxlpPKG7jvD00DQDCe04fVjDQheg-b6B0IA-a3SLB_3cTCrXHk-VdARwbftQRtD_ZX-hdzK1oUZ7Vaf3b9Ms9BA4gxQVZVFI0JwJ1o_rsuafgjkrfD7zpUleynl1YrKnxCbcUGBTVkx6IjhxWTBvR2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از پاسخ دادن به سوال خبرنگار درباره زمان آغاز جنگ خودداری کرد.
خبرنگار:
آیا پس از انتخابات میان‌دوره‌ای به ایران حمله خواهید کرد؟
ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که در آن بلافاصله تنگه را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72322" target="_blank">📅 19:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1e0c-XkPse7477ILIgTQOwTA3NF6LKsbPXH8O7D3kcLkFIvGCHTNfgOUl1VeaHvnceqvzV1S449tqGj-PiAZXTjDQEUH1J5l_O0uI4PUCyacpu65LREyj4q-D1QwM5KzZScF4jBxRbEq0NGIysBhbZwFuWKC13N3tdqo1tfn5iMKh9bDdfjcYd09j0RQmbPV9GSwXmNuaxrCMzguWsv4nhfgScWIscmfZjSImtbMzfbUnRNgFgIqynHkpdCtdimPj5MrxFrkbe7BeYfFliIDeW5qzc0mbOXCJf4sntZfrxZ34HHYdzitnrf6aODqIloWVrv6fz_pantaD4yO0Ne8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای ترابری نظامی آمریکایی(C-40 Clipper) که بر پایه Boeing 737-700C ساخته شده و عمدتاً در اختیار نیروی دریایی آمریکا (US Navy) است در بحرین فرود آمد. مأموریت اصلی آن جابه‌جایی پرسنل و محموله‌های لجستیکی است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72321" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72320" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=mRdyusL5xwtgPK53CmkCFpB-PE7p-Wtm7npYQdJH_nYbIoFEQ4p5C0x7GBFEMRXm37qzx3Y6P_qE9vYbPptjpmJDQnv8vOF9li2eW5LDRW9aBbjQG6j9TgVRWpvNTzTvVBekZC942D6KwvhdEH_ytyw3pE2t1t_i_0LeWopTAuc-wpBx_eZRO9uFRX7XDF_agMOC_ShPgBWKPop9H_eiHI3dBDc3cWUlu7e1VWJGIy5KZ-isakyCXZS4OEpNlXGCMtewc2U_mozeumkdHGX99ncjjYCtUMe1Hm3lsUBm1nAArtkSNcGNi-ggRu0MSgLawh9X4ROjt9qat-Y9oXXl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=mRdyusL5xwtgPK53CmkCFpB-PE7p-Wtm7npYQdJH_nYbIoFEQ4p5C0x7GBFEMRXm37qzx3Y6P_qE9vYbPptjpmJDQnv8vOF9li2eW5LDRW9aBbjQG6j9TgVRWpvNTzTvVBekZC942D6KwvhdEH_ytyw3pE2t1t_i_0LeWopTAuc-wpBx_eZRO9uFRX7XDF_agMOC_ShPgBWKPop9H_eiHI3dBDc3cWUlu7e1VWJGIy5KZ-isakyCXZS4OEpNlXGCMtewc2U_mozeumkdHGX99ncjjYCtUMe1Hm3lsUBm1nAArtkSNcGNi-ggRu0MSgLawh9X4ROjt9qat-Y9oXXl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانوی گاثی که دریک براش هاپ هاپ کرد:
غذای مورد علاقه‌ام کباب کوبیده‌اس! بابای من ایرانیه و عاشق انواع کبابم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72319" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72318" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72318" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGloWVWGdSxmSgflBrKpShA5pOTuC-Xz9M0Y_UrMSCKa7Q1xGtGaXj18IpdYTUkiJUttzmU8BJQ1woowb-7auLBg5b0njGtEmYtpDVX4CNXGTXnbHtZ4mqHgfNJSAEBO3SNDhI6EbGI-MsI6iHGV_j4eOAbLprg5yCOLDWrulxjsin5wtBaRE0dkzCgr9sSt-Ls9fHWeB_zkRmD40qLEgDaTPZYMXt7X-0_J6NG4xDYOB41ND-Q8CKFaKVIzeevzziUavMeRruxly_eSY3ubt4UaILR-sMjMxW7yzFYRa8cjr83uninykWKPtjPhZ1LYlJ-yT97QTgxDbXSl43doxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72317" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=RE1VoGZ34L9ujgsA2PIZIKF6DwDHCloV2A6-q8s_rPFbhczbiX1clDF4WQ_quHWDVARgty1m6pi6xeslbSdYeIbFik2xUCAYCm3VsJI2AQq4NFd959GJS5VgvE-9KUeRnI7RZaCf9YC-8XyTbPRrVFpma2ybLJZFT8OCAclmT8h9l5X19x3YFZ4KkrRfGvd7B2eP-xsIpqa2U0gL5iAkweRVmE-7ObpJS3pdS4CaBA6aKVgeWQ_3QU4B1-QIjVIoiEx-JAYlMOeZOPCHH_anJec0lhD6SQfNu1V1WKym1JlqBOMGpZ4p5_eyuTkhoHSBrnNrrb9Hlgqi321Aol1Z4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=RE1VoGZ34L9ujgsA2PIZIKF6DwDHCloV2A6-q8s_rPFbhczbiX1clDF4WQ_quHWDVARgty1m6pi6xeslbSdYeIbFik2xUCAYCm3VsJI2AQq4NFd959GJS5VgvE-9KUeRnI7RZaCf9YC-8XyTbPRrVFpma2ybLJZFT8OCAclmT8h9l5X19x3YFZ4KkrRfGvd7B2eP-xsIpqa2U0gL5iAkweRVmE-7ObpJS3pdS4CaBA6aKVgeWQ_3QU4B1-QIjVIoiEx-JAYlMOeZOPCHH_anJec0lhD6SQfNu1V1WKym1JlqBOMGpZ4p5_eyuTkhoHSBrnNrrb9Hlgqi321Aol1Z4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده،
توی تونل رهبریشو طی میکنه
و توی تونل رهبریش به پایان میرسه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72316" target="_blank">📅 18:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9475808af6.mp4?token=HWEw7sn3Ie43Df9jaR3fLtu881zyPBOMu7zxY29_8yfM8rymnpyqX2e0fPyrEeADfFWBtcgsvqNLdEyOwyXXRHwsfXhJzOLr08RUiN0cqJjOa2uQqM84rLuDr9aX2HrswFPYWuygKb5d00W6nSmiqrTc6HcMbhOSDN811wm7HRgMpn5y5yEOzIKlMTZAFcfgsXtlk-jeSJNYLT77GFb9iZpkiJqKu0Z-DdYPoZa6Bi4-LWV9KgFvMDeMFMteMK6nM4UdMqeQwRfOsYO3aRzfu5qW68gsbfSxSGFFrthtGCKc35RYW6jjzS52kzn8acgwF40xUfRCpJPC5Kv8bBhC-jOgj9ch_9NrEwR7udi1ig68g9DGWNXB1CJkgh0Pgv2hj5wye5S_lNEfWiBaJKTTDnBPTIYDl7I1wRdn5k2fFUpV74Gxmo_IhJ9xpI-RvxCW1HcKSL7tK1ddRlWrI2p9K_7F0uJA6KP70JZpYRtmx0NZUASW9xHiyXi_aqJUmch1XeGUhH_gLETKr9fx-4CEoXa6Th7e2qWErXXYlVT8B7bQgYEbEjtY4_1Q1yMvaWL5f8kThVH3rbEQ0sYHfr4JG4LVMhb_2xhSaKQFq5awHq4VQHvCzeR-T1wFpQB0OZEdJJQgnOqk9klEKO9-gTfjeurc5P9t5Yrk-nlt3cL67WY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9475808af6.mp4?token=HWEw7sn3Ie43Df9jaR3fLtu881zyPBOMu7zxY29_8yfM8rymnpyqX2e0fPyrEeADfFWBtcgsvqNLdEyOwyXXRHwsfXhJzOLr08RUiN0cqJjOa2uQqM84rLuDr9aX2HrswFPYWuygKb5d00W6nSmiqrTc6HcMbhOSDN811wm7HRgMpn5y5yEOzIKlMTZAFcfgsXtlk-jeSJNYLT77GFb9iZpkiJqKu0Z-DdYPoZa6Bi4-LWV9KgFvMDeMFMteMK6nM4UdMqeQwRfOsYO3aRzfu5qW68gsbfSxSGFFrthtGCKc35RYW6jjzS52kzn8acgwF40xUfRCpJPC5Kv8bBhC-jOgj9ch_9NrEwR7udi1ig68g9DGWNXB1CJkgh0Pgv2hj5wye5S_lNEfWiBaJKTTDnBPTIYDl7I1wRdn5k2fFUpV74Gxmo_IhJ9xpI-RvxCW1HcKSL7tK1ddRlWrI2p9K_7F0uJA6KP70JZpYRtmx0NZUASW9xHiyXi_aqJUmch1XeGUhH_gLETKr9fx-4CEoXa6Th7e2qWErXXYlVT8B7bQgYEbEjtY4_1Q1yMvaWL5f8kThVH3rbEQ0sYHfr4JG4LVMhb_2xhSaKQFq5awHq4VQHvCzeR-T1wFpQB0OZEdJJQgnOqk9klEKO9-gTfjeurc5P9t5Yrk-nlt3cL67WY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
کاری که آن‌ها می‌خواهند انجام دهند، باز کردن فوری تنگه هرمز است. می‌دانید چرا؟ چون دارند از پا درمی‌آیند. می‌دانید چرا دارند از پا درمی‌آیند؟ چون هیچ پولی عایدشان نمی‌شود.
آن‌ها درآمدشان را از طریق تنگه هرمز به دست می‌آورند؛ بنابراین با این کار، عملاً علیه منافع خودشان عمل کردند.
آن‌ها گفتند: «بیایید تنگه را ببندیم و برای دنیا مشکل ایجاد کنیم.» اما من وارد عمل شدم و ما بزرگ‌ترین محاصره تاریخ نظامی را برقرار کردیم؛ یک دیوار فولادی.
و حالا چه شده؟ آن‌ها دیگر پولی ندارند، چون می‌خواستند تنگه را ببندند.
و من گفتم: «بسیار خب. ما آن را به روی شما می‌بندیم، اما بقیه می‌توانند از آن استفاده کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72315" target="_blank">📅 17:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=EJV5-w6c7DdSxzPSsT0H5tBnBTBieP2UjN7sPYCSqm62GkrtRP2-MBjdzFKioUnLaDHu5N8Bxp-ijV1SxJRCo77gwgaoQYawgEA4eYTbKTjA5XlVXlMzZJvYiXLzGqHGBqQT3aHcnU10IEhD2jDshBoHSP7HVz4eVKyOlOkCTnPfuNhvIyNf9sVAoMB1_F2ZoqtakQIO-pE3TpRV8WyYjNNQf855AVCEUkEcBQGNtaoccnbDL3iTVpPA4rVQY9u-y110U_dZWPtx1A2ZeBAvIGO6DMMCerkh9cu8kqaVr6FgBdhsG-NqLcGyyKKe2VTTXAFoGpmNtP0Wn_O3zh8FpzGyrKwNP0JxhP75J87GcwM9tLG9j7CUjK8YfoYTyhtVHOa-eanZj-MVXCyfiDQwBLrEy4VmATNiY2CEzRDIDeyVWQwdGx-87CSONIDPzfuEjpXAZYsx2JypedDQwVRXf_gF8CJYsGtu_6v6x7y0f2k8BwqvuFk99LhJYHMC7r9ihyLFydeicYtl-sFTYTc1Tsqr5_K5HUBXXL-mRywrqaoYZsSleTkEsh9_yiyUe9-fzT6g1B1dh_YbDjhys15fcHLW7Nag6KTTRoEWVsz-uifeLSyD2JKmNiusOt5ugAB15Og92qJiQ-NLGUX5eYJ3r8atSailD0AJPVJZL6dBAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=EJV5-w6c7DdSxzPSsT0H5tBnBTBieP2UjN7sPYCSqm62GkrtRP2-MBjdzFKioUnLaDHu5N8Bxp-ijV1SxJRCo77gwgaoQYawgEA4eYTbKTjA5XlVXlMzZJvYiXLzGqHGBqQT3aHcnU10IEhD2jDshBoHSP7HVz4eVKyOlOkCTnPfuNhvIyNf9sVAoMB1_F2ZoqtakQIO-pE3TpRV8WyYjNNQf855AVCEUkEcBQGNtaoccnbDL3iTVpPA4rVQY9u-y110U_dZWPtx1A2ZeBAvIGO6DMMCerkh9cu8kqaVr6FgBdhsG-NqLcGyyKKe2VTTXAFoGpmNtP0Wn_O3zh8FpzGyrKwNP0JxhP75J87GcwM9tLG9j7CUjK8YfoYTyhtVHOa-eanZj-MVXCyfiDQwBLrEy4VmATNiY2CEzRDIDeyVWQwdGx-87CSONIDPzfuEjpXAZYsx2JypedDQwVRXf_gF8CJYsGtu_6v6x7y0f2k8BwqvuFk99LhJYHMC7r9ihyLFydeicYtl-sFTYTc1Tsqr5_K5HUBXXL-mRywrqaoYZsSleTkEsh9_yiyUe9-fzT6g1B1dh_YbDjhys15fcHLW7Nag6KTTRoEWVsz-uifeLSyD2JKmNiusOt5ugAB15Og92qJiQ-NLGUX5eYJ3r8atSailD0AJPVJZL6dBAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که طی آن فوراً تنگه هرمز را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
می‌دانید، شما این موضوع را در «اخبار جعلی» نمی‌خوانید یا نمی‌بینید؛ اما ما داریم با قدرت تمام پیروز می‌شویم.
ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72314" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=X4AtZJ1IbPmGHnR2ghnKrM_pdudBKYs9SbD1WA7D7IoAGGW1dPz3T9vJMctY0sJwzR7z13Bw7PO20t14cyN4WRPQwuWOISLSJ13sXTd7ARBhBlvXouHenY8WubkP_o4dwb7QqeYOVSbMzxnPxQgjmezR3zHNIn8Axq8CdgX-rm3UYujAzXK8p7M0MfzYmXXt3awCB_H01Ieq0cB4jQpfGJTJ1Ael8Mv8X6nsYX4896ngkO_vDKkrVjSAgS9w_zVSaQc8qjwkgygPuV6DjrA6JzJQyxjSp6omQm1E8zQjUKpN11sd3KJkgJSy4q6KA_bkUxiR7xGol_Jhg7w6POnYAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=X4AtZJ1IbPmGHnR2ghnKrM_pdudBKYs9SbD1WA7D7IoAGGW1dPz3T9vJMctY0sJwzR7z13Bw7PO20t14cyN4WRPQwuWOISLSJ13sXTd7ARBhBlvXouHenY8WubkP_o4dwb7QqeYOVSbMzxnPxQgjmezR3zHNIn8Axq8CdgX-rm3UYujAzXK8p7M0MfzYmXXt3awCB_H01Ieq0cB4jQpfGJTJ1Ael8Mv8X6nsYX4896ngkO_vDKkrVjSAgS9w_zVSaQc8qjwkgygPuV6DjrA6JzJQyxjSp6omQm1E8zQjUKpN11sd3KJkgJSy4q6KA_bkUxiR7xGol_Jhg7w6POnYAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره طرح هفت ماده ای ارائه شده توسط ایران:
آن‌ها پیشنهادی ارائه کردند، اما من آن را رد کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72313" target="_blank">📅 17:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDlpGfEKIqyDCRJKU4cta6BtQwNPZACPICgoop0yQ9mYxcwcHhcXNxWm7vF3uIhOOjY6zzG1e39bQEEuwFdBqkCnXvEf-ZVxET4BMfDAWQ7YArwfTZ_1SCdKCaTTMTmBruq2h5KoZhMeyq0IP3pA1-AQq1pBI2r05zQ4vNxG89jBMoYOFcswwx-VkHP8TPncOZc3brMmJJgdk0AGNEariUGCWGqIU3ZN1owCtYGiPNyAMXWNeYI0aEVHe5Hlz827SxtwugHkYrHa6XMRHVpA5YnPhAZf6RX9cvBqVQFCDWJvwN3UociftbcfqFkr9v8UiNLxEmBDuuDckCvHrjIS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72312" target="_blank">📅 17:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=d0D8Cd6jt5W_fz4xO_g_1MgZufIVsvDYjloHsNK-ql5RizvhzPsf4etkoaFPhCj8G41dxQJhTFwM-HXUN9qspJW6USeoEDfsP1p4oiwamIsjFXG4l-OXn56o9rRTAEDU2tSRVNe-VkOjyzgNOsoY023B3voB9iUHx0EfUGE5k3HGWYCbdpy8MRPH4LL3_CTONzMXW0n8LnjXLxlvI1JXr3EoxQB15RXenOwWSNadrYTExskxYXGAkFm2A84WY6Ye9mMB8dyIWCMvdBoJCRL9zh81lq8IFkKKaytPazMv_5HsAYj5IoLWYWR4IvMg3LNcpfZelSQL4l1fviq0IosJmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=d0D8Cd6jt5W_fz4xO_g_1MgZufIVsvDYjloHsNK-ql5RizvhzPsf4etkoaFPhCj8G41dxQJhTFwM-HXUN9qspJW6USeoEDfsP1p4oiwamIsjFXG4l-OXn56o9rRTAEDU2tSRVNe-VkOjyzgNOsoY023B3voB9iUHx0EfUGE5k3HGWYCbdpy8MRPH4LL3_CTONzMXW0n8LnjXLxlvI1JXr3EoxQB15RXenOwWSNadrYTExskxYXGAkFm2A84WY6Ye9mMB8dyIWCMvdBoJCRL9zh81lq8IFkKKaytPazMv_5HsAYj5IoLWYWR4IvMg3LNcpfZelSQL4l1fviq0IosJmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عرزشی داره فخر میفروشه نسبت به بنزین مفتی که میگیره در حالی که بقیه مردم ایران و دنیا باید گرون تر بخرن
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72311" target="_blank">📅 17:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204024e85e.mp4?token=Vvo4s-oyajtR3ct6RhPNal-cKvbQnV82P_3IkznF_cF_hAoJEabwnJ7qYwQ1-mmajItlusFqp5igxvdgwIUG-j7LyG5xJWlEHGurn0CNJCEjCnAOfbJnf9SZy0IXbGlrYe-yIpTwDWrqwEaUE4akrmQ3FrpJBHtp3TRBfv7TMpVNGe7DL95Ca99bKJrNLdKMwgy7ELl8Rx4C8wMAyS4CnlITt-BXy1KFMHi1UnJHKRdenMmEMuPHxL1upLMCl-p9TIYoR3BB2YkYZ3-4D_tZq62RchfBvTFnXjZT_ApdOJUX9oNsn_IYlzwuFfQaLIi3QsdsaXeOLfV276_RuKzWug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204024e85e.mp4?token=Vvo4s-oyajtR3ct6RhPNal-cKvbQnV82P_3IkznF_cF_hAoJEabwnJ7qYwQ1-mmajItlusFqp5igxvdgwIUG-j7LyG5xJWlEHGurn0CNJCEjCnAOfbJnf9SZy0IXbGlrYe-yIpTwDWrqwEaUE4akrmQ3FrpJBHtp3TRBfv7TMpVNGe7DL95Ca99bKJrNLdKMwgy7ELl8Rx4C8wMAyS4CnlITt-BXy1KFMHi1UnJHKRdenMmEMuPHxL1upLMCl-p9TIYoR3BB2YkYZ3-4D_tZq62RchfBvTFnXjZT_ApdOJUX9oNsn_IYlzwuFfQaLIi3QsdsaXeOLfV276_RuKzWug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه تعداد هم وطن به مناسبت شروع سال تحصیلی لوازم تحریر جدید گرفتن پخش کردن بین بچه های محلشون
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72310" target="_blank">📅 16:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11382bd536.mp4?token=t5V9aoNG_gIfvolETmh6lCCCOunW1p6Y3IgDZORBP6OxZnZiT9TnfbFj9CU4DCZpHLx2G2KEGsXOTFfkYLTSjQL1QjY0NgiUXcWd9CvD8SfcB2JVaP58iZs21ldirm9MxHRAH20tM9YiQjh1bjdrGpQbK5_vMTVkCZaxTRCDGUXua7Y1kij6qGS3g8R42RSCtBLcq9rdrTXtMyXl6OpasTMjXgPOKiUQqm3NTaW9VWDEKwmttQ8NAE6Fzk0vHQKsp5e6vs9-ymOX4fExBQ-3YDqUa9MgI9vUIKuzXMpm6_sRE0n0YcpuFN3lrUswnFbn_N5HLcJJj7IBqPl3zp3Na442QAZvo497VNblR_jIHvV487NDl99UIiWUF0jH7j7g2yTXRnBKmTiop9E7PapikEo92v_6zDWQ1yv9QfleF09Utb495gL2d92z5-kPTrqLJFqoyiL1yaEjSnVtkMVqEVWXn5u93XYolEelrtungnQh6WRNmVjHut4I1G6v5hesyNYZO_x2K0vkiJlgxvz3qIGnUacvoNXPekMsQ_adAAAESu2fdwHMKl3AA29IR1ifqP78_0XueMO-STJBjQmV3bB8a1ZjOuoQ0dXTtLPCwNWdrb7m874Rs2GzmYCatXfqTU1AgksQSdMRb5Vp2Xh7LZaCh8prmlKGfwMiA0wfaYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11382bd536.mp4?token=t5V9aoNG_gIfvolETmh6lCCCOunW1p6Y3IgDZORBP6OxZnZiT9TnfbFj9CU4DCZpHLx2G2KEGsXOTFfkYLTSjQL1QjY0NgiUXcWd9CvD8SfcB2JVaP58iZs21ldirm9MxHRAH20tM9YiQjh1bjdrGpQbK5_vMTVkCZaxTRCDGUXua7Y1kij6qGS3g8R42RSCtBLcq9rdrTXtMyXl6OpasTMjXgPOKiUQqm3NTaW9VWDEKwmttQ8NAE6Fzk0vHQKsp5e6vs9-ymOX4fExBQ-3YDqUa9MgI9vUIKuzXMpm6_sRE0n0YcpuFN3lrUswnFbn_N5HLcJJj7IBqPl3zp3Na442QAZvo497VNblR_jIHvV487NDl99UIiWUF0jH7j7g2yTXRnBKmTiop9E7PapikEo92v_6zDWQ1yv9QfleF09Utb495gL2d92z5-kPTrqLJFqoyiL1yaEjSnVtkMVqEVWXn5u93XYolEelrtungnQh6WRNmVjHut4I1G6v5hesyNYZO_x2K0vkiJlgxvz3qIGnUacvoNXPekMsQ_adAAAESu2fdwHMKl3AA29IR1ifqP78_0XueMO-STJBjQmV3bB8a1ZjOuoQ0dXTtLPCwNWdrb7m874Rs2GzmYCatXfqTU1AgksQSdMRb5Vp2Xh7LZaCh8prmlKGfwMiA0wfaYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقایسه ارزش برگ‌های اسکناس با یک برگ دستمال‌کاغذیِ دورانداختنی
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72309" target="_blank">📅 16:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=nP52JsjbojGYbuA_4CwISBT1eZdzGIeYgbvFWLHXdkJQIwsEmQNj9twA1kaZ3a-Rf0m2eK4NMWYboxx_Y03hTckZhZdGbduPBB4YL0wnSiQpLlGdCbZxEAa_emZw1d6icyhRkI-UhIvwugeaBuAVNWB6XNT6OLzHS5Hfa3qw7V8g9kiPcQ2Y5bhAzA7TogKWlv17o0oZo402JyP9-SDwOc31bwRmkejSbn-y3sNHEo7Bm1nxo_mbGajK1d4SeGYlWoP7f8gJnQfDBSIKgywKnlasIp8zuYReEy0RdKMyjpkJuxWqBNAHBOG_h7gJMtNsdkeCAb7AeJV0stjOC1rDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=nP52JsjbojGYbuA_4CwISBT1eZdzGIeYgbvFWLHXdkJQIwsEmQNj9twA1kaZ3a-Rf0m2eK4NMWYboxx_Y03hTckZhZdGbduPBB4YL0wnSiQpLlGdCbZxEAa_emZw1d6icyhRkI-UhIvwugeaBuAVNWB6XNT6OLzHS5Hfa3qw7V8g9kiPcQ2Y5bhAzA7TogKWlv17o0oZo402JyP9-SDwOc31bwRmkejSbn-y3sNHEo7Bm1nxo_mbGajK1d4SeGYlWoP7f8gJnQfDBSIKgywKnlasIp8zuYReEy0RdKMyjpkJuxWqBNAHBOG_h7gJMtNsdkeCAb7AeJV0stjOC1rDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضخامت رنگ کوییک اسباب بازی از تولیدی کارخونه بیشتره !
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72308" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QaU522qNNNk5a9j6N1NAh_vXpmB-KoMJgtCvVbLk8uR36sgFLys0-Sa7H9-faw65YQTfOuk1tuPOH_tdriqVW0roEdgXOFAQnIgBZHibfYWUkSY2C-74UYzoYLXRdIHjE-3jkllquYU8KTNiF-565VWud_EceoyQ3yZH0QpcOvk9HkhbDmUhKLN3lu5sXQpPQj3xv5FhboikuriIneyknBPZ1ikTaJ879FGgWl3taBNywi8mkMD2P-M1ayaD0MwNtf2-FmuV55wXNgO_Nu-pN_PGIBNV3yhr4AqtYFNGDBHzJh0_V96n7jFuiFONJhpgRUR2Mh3yFKq0gD2VwvANWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=quOp5QVTlcA5maHnx6qmOYusSZwnozIcww6yJS8t4NSanR3Oyox1ChynlFuehkliBapZEZ4gJtQJY7LH_PDYnFwB-bLB6XQ0vDEeRcK053jWNAc7JI9OfCOwMwPduRfvi35QkM8WGKh-PpVZNGodXXNrPkddizL6_boXs79Bf4RpeME0eKuotHMIpZhkeZ588OviRy4l4KoiniR_ZgNiyVk1w2TZ_KLw6ExUeTEyzPYo8i7hGGrUrmg1xbPI4hGFUmOIarMBCTvz0okBT4DZgQhn355lzoewDTRS3buonQqvaGmpxaUjrVfQkI2Qq4Tflc2Do0Enk6492k2o1DgbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=quOp5QVTlcA5maHnx6qmOYusSZwnozIcww6yJS8t4NSanR3Oyox1ChynlFuehkliBapZEZ4gJtQJY7LH_PDYnFwB-bLB6XQ0vDEeRcK053jWNAc7JI9OfCOwMwPduRfvi35QkM8WGKh-PpVZNGodXXNrPkddizL6_boXs79Bf4RpeME0eKuotHMIpZhkeZ588OviRy4l4KoiniR_ZgNiyVk1w2TZ_KLw6ExUeTEyzPYo8i7hGGrUrmg1xbPI4hGFUmOIarMBCTvz0okBT4DZgQhn355lzoewDTRS3buonQqvaGmpxaUjrVfQkI2Qq4Tflc2Do0Enk6492k2o1DgbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72306" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اثر جدید ابی به یاد جان‌باختگان ۱۸ و ۱۹ دی
از او بگو به دنیا..
از او که قصه ای داشت او جشنِ زندگی بود..
سروی که قد برافراشت از اُجرتِ گلوله ..
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72305" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=V-zIkx5N1xwLob8DtmuEDx6rJIL2qJ-i0o-DCb4kZumUCRXGc6OBQ1m0eHEFGg9gFXSVR6ur2ZW9PSa_OBmnYlIRWD7CEG5QHQeOqDByacgZgbI3_a8v271i62wpRVpkLeQXnninP0muvJS5E-4bblm6vZbNe8xavyrbwij_NQb5s0JeQoyemFf05SdMS7gL5Tup7qi0QzCqVTHADbJULrj7i4_SrkY3UNXKgriG88t3SJD2vby7FaUbsa4MvfMh_-gIlJnzogTA0Eq0eXUFL53d21-TXmOBRiw6r8xGg_E8Lbv2-s7Tv05iqIqNfD1YUF-78YtG0AWyXGUxk-7YFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=V-zIkx5N1xwLob8DtmuEDx6rJIL2qJ-i0o-DCb4kZumUCRXGc6OBQ1m0eHEFGg9gFXSVR6ur2ZW9PSa_OBmnYlIRWD7CEG5QHQeOqDByacgZgbI3_a8v271i62wpRVpkLeQXnninP0muvJS5E-4bblm6vZbNe8xavyrbwij_NQb5s0JeQoyemFf05SdMS7gL5Tup7qi0QzCqVTHADbJULrj7i4_SrkY3UNXKgriG88t3SJD2vby7FaUbsa4MvfMh_-gIlJnzogTA0Eq0eXUFL53d21-TXmOBRiw6r8xGg_E8Lbv2-s7Tv05iqIqNfD1YUF-78YtG0AWyXGUxk-7YFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ در پلتفرم ایکس منتشر کرده:
در این ویدیو تصاویری از انهدام یک لانچر سپاه دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72304" target="_blank">📅 13:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش های تایید نشده از انفجار در نزدیکی جزیره خارگ/همچنین صدای انفجارهایی از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72303" target="_blank">📅 13:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc192b406.mp4?token=CfWvZJacwPP3BtdEyi64ZHQeiQwDaRxYCQuOspAAqaimXFjgIYlUfNRzx5__g328HdyasHhVfT9xYB1fkOYyk9zXlhPtwByR9rHzFeU932UrW4q7TeC4yTk2rFRCtvm_Y1zmaYdK4lMVfl_pbWt6GldjXFgC0NZgHqEYAryBmzcVriX-zTgRrYpUmKrEhFPhRpVh6p1p1s6xu2wuUXRSkdwbc01mEst6em-s1n4tZ41c2zBi6RLeErIoUF98K-t6XoOkB-zK_mBVdvo7wq78GOIY2oa1WR-jo7hUay8r_cOh7zTp3OF-m7kJNWApDLUm2PvhHlXCKIR-Pn2EZOU9qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc192b406.mp4?token=CfWvZJacwPP3BtdEyi64ZHQeiQwDaRxYCQuOspAAqaimXFjgIYlUfNRzx5__g328HdyasHhVfT9xYB1fkOYyk9zXlhPtwByR9rHzFeU932UrW4q7TeC4yTk2rFRCtvm_Y1zmaYdK4lMVfl_pbWt6GldjXFgC0NZgHqEYAryBmzcVriX-zTgRrYpUmKrEhFPhRpVh6p1p1s6xu2wuUXRSkdwbc01mEst6em-s1n4tZ41c2zBi6RLeErIoUF98K-t6XoOkB-zK_mBVdvo7wq78GOIY2oa1WR-jo7hUay8r_cOh7zTp3OF-m7kJNWApDLUm2PvhHlXCKIR-Pn2EZOU9qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی خراتیان کارشناس صداوسیما از نامه ای محرمانه که چند روز بعد از اعتراضات ۱۸و۱۹ دی از طرف جمهوری اسلامی برای دونالد ترامپ فرستاده شد می‌گوید :
ما از طریق سوئیسی‌ها، حدود دو سه روز بعد از حوادث ۱۸ و ۱۹ دی، نامه‌ای محرمانه برای ترامپ فرستادیم.
نامه به تقریر رهبر شهید بود و فکر می‌کنم آقای پزشکیان هم آن را امضا کرده بود.
متن نامه چند محور داشت و لحن آن بسیار جدی بود. در این نامه به ترامپ هشدار داده شده بود که اگر جنگ را آغاز کند، شرایط مثل گذشته نخواهد بود و ایران درخواست آتش‌بس را نخواهد پذیرفت.
تأکید شده بود که جنگ را به منطقه خواهیم کشاند، به پایگاه‌های آمریکا حملات بی‌سابقه خواهیم کرد، به نفت رحم نخواهیم کرد، مسیرهای انرژی را خواهیم بست و چه جنگ باشد و چه نباشد، به اسرائیل حمله خواهیم کرد.
رهبر شهید نیز در یکی از آخرین سخنرانی‌هایش تأکید کرده بود که این جنگ قطعاً به یک جنگ منطقه‌ای تبدیل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72302" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72301" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pa5snMcPzBSqvUdZyQjSPQgpgBqc3jqg30-ZGZA3EwNzeytkESNPCp_9rqYz-Bqirg3nhj7kETSPIvS9l09q7aNflWxI1BrMbXXxuP-G29lJ25sXHcKcO-d2NyjMwbeDg-qNTy-G0OJrXwfuPpKl1LIRKqbW9p5BDTcywErsg5haDR9Q4JiETAj3R4Nh55qWl6syDaDlvN3IwwFZo6jcHI95eu60oax57c0wxpHEwlYuPn9aNFr6p4lqhxiQW9647qGO8s8Pv-IveZCeChjBBXQTGydfaNjluHp9KDfeIKJK0sfLtyhvuQuwhYYxtqirN_aOLP5oWWJHtYZ5WE6pJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72300" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udPVuxq7XRJ0RS3HPXaui5pm3v32ym4IEYtggBkKI7No5FOHQnfGh2HAyb4qlAZROIlJpi23pRtk60DSCocdSOEFCuhyQ7OyMp3i8meEYSq2UfYr2B5DmmIwT9X6Mms55BNmeAxT0Dg-2FX-KiByhrbNRaJyakUej3xKC_5oJqiu2lbhVhjutmeLHT-9uDyZ3SpTiDJTRytmF45Gf2oVCFN0ywBeLnUwOWcIS7c_hv-6xZ3qs9JOgKLXfAdsYr_xaw2Wp0mHSSc_QbnGOvAM5JHwrvCyqb0_k9FqDToGKGfBA48XffmzPROEbSDRFjyvj9VWfyFAVrGD8dXdS4edYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M592XQDsZoZZp4UKAGTgF59kFjVRoIVgEiq0kX8rK44Am67e4nkMNvmKi0wW8m0SGDiw7kUC69XoAqOu5zIHmKg3v0zrFwfm0eaoYS-5nKXVKAUvjaFh2Wfc-cBKGQKz9VGedByjtW8jbofY3jZjYbReK9EEcJgk72ejSpqkqKv8rXiSeEr3DiFjLi38k-vQb91DNW4O6d6qxykueG5tlEPgzPnD39E46pKAFeOZOOiUePfY00JUgWXX9fkoRnLZV6MCNtspEd_QOD9UkE6MP7DdUHen3kG4ijDcCV7pTjY5OeInzy-YaUPJr_TqHHVTfhXLlfOtOdmTVG-xl94fSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exM4j0XS6wSrE442JzuVierrkPncziNc5puuwLvTviKQLkIZPf0EDN8PDVMHIW7CDBzsdqfe2TNdtY43rrg_2w6DHiKiRMY0zNzdmRfHSk-Ld9ljXSM1PJB4K1LwPf3iEo-Bv-bk-vKoqttueVLpz5pJ6MKB87VpzQ7KCNzxB9Tk8XXcIgLxoVaggaNTQRVJukOOtBaykOM3ekpc7q5evx35z2eUuOZwzL96Qpg0u5ANtyGj3PlqAkxQoHZjPA6eSB-QkSlK5n2wo0ZK3Dl6xS1qElcFQMYlj62kAZLXB4iwCAQIRBxIbIhAMFqpZqmHFdSiwvNJLjOkLH-a9Q-jZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جان فدایان ادامه دارد
ترامپ توسط جان فدایان دستگیر شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72297" target="_blank">📅 12:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=q4MFZK6iVISTiyyZ4_fPbwoEqRDfqJxrkFMjs2y37q_DWxAvM-Y0kEKyd1roFbNqSugCEobz1FpKFyYlX2PQAsfkUJumoGzGNKw4EFQ0qxj_xirsNmcSv0KhJwgTahGDUPAFa6Byjl7lQBqo5F2yqK59ecIiy7Z9NPNmcyoclkmlhxWhZno8t9RAMZVkcNTQK59ASg-r4myt1PRJ2iEBKW54UfM7wMMsDLDVPV2TBCDTQPTaAgb5cgUJ6wnM5nf_Wjy4Q2MmKN7Jvap2IDJ9zbfVLw0W8607Ax49tT4pIhhvZ4vpL3AfRezr-ryeJ8wSHT0Woq9XRElLiiCV0CSXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=q4MFZK6iVISTiyyZ4_fPbwoEqRDfqJxrkFMjs2y37q_DWxAvM-Y0kEKyd1roFbNqSugCEobz1FpKFyYlX2PQAsfkUJumoGzGNKw4EFQ0qxj_xirsNmcSv0KhJwgTahGDUPAFa6Byjl7lQBqo5F2yqK59ecIiy7Z9NPNmcyoclkmlhxWhZno8t9RAMZVkcNTQK59ASg-r4myt1PRJ2iEBKW54UfM7wMMsDLDVPV2TBCDTQPTaAgb5cgUJ6wnM5nf_Wjy4Q2MmKN7Jvap2IDJ9zbfVLw0W8607Ax49tT4pIhhvZ4vpL3AfRezr-ryeJ8wSHT0Woq9XRElLiiCV0CSXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکر کارلسون گفت که پس از تلاش برای متقاعد کردن دونالد ترامپ جهت پرهیز از جنگ با ایران، او به وی چنین پاسخ داد:
«بله، حق با توست؛ اما در نهایت همه ما می‌میریم، پس [این موضوع] اهمیتی ندارد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72296" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=ool9ZYF5TdhFoAxc_xTiqv6_E5Finwlr3T_mX2zDHYwOy2zu3dP9RWsnsjBYn8dpzo2CtXOwDQDev7VSQg3G2AeVIfZ937IsIbZHD1KDnpZxOOrp0FK5q1pGJjS29JHWwnx3ZDc232UmU_IS_qvgwpVNzD-ULf-FnCHCO2LNuNOeSbNKIy18fKvqt288pqkGWWUesL-PqNqZG9Sm5p7VSDWYRApQ9-_JAOTMN6kFoP2sJ5RoPPkIBKF9JweLt-X-psz5eaDJJG1y6ZffNp1q6lgd1A-B4IBqDUmtVaLNEenVVX-ueHLCx81sYKLbf1L4Lbzv8oF_blnGxydkDAHWMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=ool9ZYF5TdhFoAxc_xTiqv6_E5Finwlr3T_mX2zDHYwOy2zu3dP9RWsnsjBYn8dpzo2CtXOwDQDev7VSQg3G2AeVIfZ937IsIbZHD1KDnpZxOOrp0FK5q1pGJjS29JHWwnx3ZDc232UmU_IS_qvgwpVNzD-ULf-FnCHCO2LNuNOeSbNKIy18fKvqt288pqkGWWUesL-PqNqZG9Sm5p7VSDWYRApQ9-_JAOTMN6kFoP2sJ5RoPPkIBKF9JweLt-X-psz5eaDJJG1y6ZffNp1q6lgd1A-B4IBqDUmtVaLNEenVVX-ueHLCx81sYKLbf1L4Lbzv8oF_blnGxydkDAHWMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان درباره مجتبی خامنه‌ای:
مجتبی خامنه‌ای هیچ‌گونه مشکل یا چالش جسمانی خاص و مداومی ندارد.
در آخرین دیداری که بیش از هفت ساعت طول کشید، البته ما عادت نداشتیم که آن‌قدر طولانی‌مدت در حالت نشسته بمانیم.
ما زاویه و وضعیت نشستن خود را تغییر می‌دادیم، پاها را روی هم می‌انداختیم و کارهایی از این قبیل؛ اما قطعاً او از سلامت کافی برخوردار بود که بتواند پس از آن ساعات طولانی در آن وضعیت، بایستد.
از منظر پزشکی، او کاملاً سالم است. این را از زبان من به عنوان یک پزشک بشنوید و بپذیرید: او هیچ مشکلی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72295" target="_blank">📅 11:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=oeFZhRIs2bSl-NfT4wSOZReAtGImrFgFf5SKAk-LxVCZg8rwa4yoCslG0Ur5dB-gWs9Wl6C_gArsKkeAjjCk63IHVv1D7bdNwUzhfwlCBwZbb28q9eJAc7GrX_flWOkNxG5dUofrGj3y2G5eeXcVYepxCk-zDMfD74f2cUcVM_1eiIpO3k40oon9gXu8hlUdCCUaQRW_fTD0OW4t5EeRmJ252YtP8fGS03RA7sg1NqQZIYfK9PRC5YMo1ryjlwKBwDAYN0tWgXcIH7chPoo91uyuJf2Y2W9F5dSO7HfqSrGk61vMWWM9NemVlPZwIxlXo-9ay7LRRy_rw7ac7ZpFKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=oeFZhRIs2bSl-NfT4wSOZReAtGImrFgFf5SKAk-LxVCZg8rwa4yoCslG0Ur5dB-gWs9Wl6C_gArsKkeAjjCk63IHVv1D7bdNwUzhfwlCBwZbb28q9eJAc7GrX_flWOkNxG5dUofrGj3y2G5eeXcVYepxCk-zDMfD74f2cUcVM_1eiIpO3k40oon9gXu8hlUdCCUaQRW_fTD0OW4t5EeRmJ252YtP8fGS03RA7sg1NqQZIYfK9PRC5YMo1ryjlwKBwDAYN0tWgXcIH7chPoo91uyuJf2Y2W9F5dSO7HfqSrGk61vMWWM9NemVlPZwIxlXo-9ay7LRRy_rw7ac7ZpFKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا ایران بعد از امضای تفاهم‌نامه با آمریکا سه کشتی را زد و تنگه هرمز را بست؟
اینجا احمدی‌مقدم در حال توضیح دادن یکی از دلایل آن است:
نود میلیون بشکه نفت‌مان از محاصره خارج شد اما خریداری نشد.
چون ناگهان نفت زیادی عرضه شده بود، مشتری‌ها با قیمت‌های پایین می‌خواستند بخرند.
با بسته شدن تنگه، همان را با قیمت بالا فروختیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72294" target="_blank">📅 10:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtzpIYsbZ0xlNimUB9awCpiwom1anYwVgkGMRS21aVIc2QYSybwQpsIiblguAR2jp6pLdDXWOw3dOa51_xpOdGKf6eXwBb0w8Hb2MSoGFqOByBMqPxpHhgTikogDm8G2MvbQk-SwN2KzimjoBVZFmqdHlmzjcrUyQk3o06FnuutjwYyF8vt6Xmwegg85mBGjg2f4y09Qvdr8u-B6SGXnk3rLGUwC0Crf6i_k5BV_z1T0FBDbUi4osqgTVkzMRVjJOV-bkT3TTpEteMbp9xfg-nkQQ2oM08B2WXhR40rSvzkLYvCUjHDq8onzr5znSfN02j7UanwPVmFhHl0mEME4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وال‌استریت ژورنال:
به گفته مقامات آمریکایی، ترامپ پیشنهاد ایران برای برقراری آتش‌بس هفت‌روزه را رد کرده و اعلام داشته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران ایران از سر گرفته شود.
پیشنهاد ایران شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران و کاهش فشارهای اقتصادی از سوی آمریکا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72293" target="_blank">📅 10:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=MZEmynIJrUmAAYZRb6VBHF18aRawsN0oKRNR5U-Lbnlg4X5uQoC9-LT-LQs4QjJuEFul6TEbwXMgphO_yq7Ns56KHu98TR7BEvXXZr47J0ljr-hBEMkXSnOc9sUoMaA53VU-w9ObEnlgJ5Hka_nk14GnsEzSTOu5vZ1uzGqAa34y82RkKBV-Oie-ci7ArIc-OGSr3eT5LH-VHaajIo_nj-kHt0mzJl7ic1M-K8Mdwjs43a66pAAH_Mz86TVkFBOmrtiq7cWCai6sLj9l81tz2pJhWV9jH0fgQhS6w5FWAQAW4pJQZ7QER5Zl3W2gGdSCT_lLwJODQbfNOGdaq6s7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=MZEmynIJrUmAAYZRb6VBHF18aRawsN0oKRNR5U-Lbnlg4X5uQoC9-LT-LQs4QjJuEFul6TEbwXMgphO_yq7Ns56KHu98TR7BEvXXZr47J0ljr-hBEMkXSnOc9sUoMaA53VU-w9ObEnlgJ5Hka_nk14GnsEzSTOu5vZ1uzGqAa34y82RkKBV-Oie-ci7ArIc-OGSr3eT5LH-VHaajIo_nj-kHt0mzJl7ic1M-K8Mdwjs43a66pAAH_Mz86TVkFBOmrtiq7cWCai6sLj9l81tz2pJhWV9jH0fgQhS6w5FWAQAW4pJQZ7QER5Zl3W2gGdSCT_lLwJODQbfNOGdaq6s7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامبد جوان :
سانسورچی‌های صداوسیما واقعا مریض جنسی هستن
طوری که با سیبیل خانم تحریک میشدن. میگفتن سیبیل فلان مرد زنانه‌ست و تحریک کنندست.
یادمه توی یه سکانس یکی از بازیگرا میگفت «بیا بشین اینجا». میگفتن اگه یکی فقط صدا رو بشنوه ممکنه از «بشین اینجا» برداشت بدی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72292" target="_blank">📅 10:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=cGHa7es96RyuTeUAs_NerzaAUxqVf1C1ooAXGayjqvRWLMDFhA150AcVW3gxiSKfQrTZy_zH9A062C1ZHAOnAZY58PtFmca0wR58KGIjQjk-_ozNO-el1AAnriDMAFZH-LqS8_IPBJt-kW2AQ-3pMG14HCM_vjY31wUFP_46gto5c1NpDqlRWOSAPGjphPoQMuczp0dqCAKzokCD0UwBU_iSo-jEa3ilpjKJbYYiJ-juWCGdr0j-wtCvjqDPkLFj-rpPZRTgR9r6twD0jHF9YRklICMa0KV7jOfTRIukqQDGVREllz1BQhxMSzqcuLmXSrltML42gj2KLuRoQKOxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=cGHa7es96RyuTeUAs_NerzaAUxqVf1C1ooAXGayjqvRWLMDFhA150AcVW3gxiSKfQrTZy_zH9A062C1ZHAOnAZY58PtFmca0wR58KGIjQjk-_ozNO-el1AAnriDMAFZH-LqS8_IPBJt-kW2AQ-3pMG14HCM_vjY31wUFP_46gto5c1NpDqlRWOSAPGjphPoQMuczp0dqCAKzokCD0UwBU_iSo-jEa3ilpjKJbYYiJ-juWCGdr0j-wtCvjqDPkLFj-rpPZRTgR9r6twD0jHF9YRklICMa0KV7jOfTRIukqQDGVREllz1BQhxMSzqcuLmXSrltML42gj2KLuRoQKOxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72291" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7db87608.mp4?token=SFz-hHDIFvvxDNDfI9KOza_bEBxpLhQ6Kx7NFYG0aJwNisHuHqDk3tI5iV9opj45nJkPEbTzPX_n8P5ZD9gLB73wT-dua6u17PCXWfe6p3zY6unI-oQehqnPYOynB0mz7ygh_QVFdqdt7CjlPre9HIWP9tYiZ7GTJu7714yV2u6LVSKk-yhtV4W-VLDOqzJeNtgZp2r9_h_3-vIWOku_e6Idvkhb60LNFLPcUORxehYnuDpFY_WaRh-l2DGnd8TRh2lwcRzM7-Kky6VdNNTlgzLVA2vt0Fwe_OXn3gI7MXAAfO19JnNZ5yP-g-ngJCVtXDajoyogeWIShMKpU8z4qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7db87608.mp4?token=SFz-hHDIFvvxDNDfI9KOza_bEBxpLhQ6Kx7NFYG0aJwNisHuHqDk3tI5iV9opj45nJkPEbTzPX_n8P5ZD9gLB73wT-dua6u17PCXWfe6p3zY6unI-oQehqnPYOynB0mz7ygh_QVFdqdt7CjlPre9HIWP9tYiZ7GTJu7714yV2u6LVSKk-yhtV4W-VLDOqzJeNtgZp2r9_h_3-vIWOku_e6Idvkhb60LNFLPcUORxehYnuDpFY_WaRh-l2DGnd8TRh2lwcRzM7-Kky6VdNNTlgzLVA2vt0Fwe_OXn3gI7MXAAfO19JnNZ5yP-g-ngJCVtXDajoyogeWIShMKpU8z4qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احسان کاظمیون فعال اینستاگرامی، یک هفته با یک پیج فیک دخترانه با پیمان اکبری، مجری سپاهی صداوسیما توی تله انداخته!
آخرش هم باهاش تماس تصویری می‌گیره و پیمان وقتی می‌بینه طرف پسره، خشکش می‌زنه
پیمان اکبری همون مجری حکومتی بود که بابت اعدام ها از اژه‌ای تشکر کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72290" target="_blank">📅 09:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72289" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw7WAuzKK_ggU17ijYc8plg4xoTtdV71NFXD1bcKJMHchZrTtlE72pUUWp7Ha5eT61kQ_W_oZjqb2Yd36Xn_egsfhw4whDvfHP1qikC5VZfxtoX13yzAZu_oK73kILw8AXncx-qioXjQDzWB6fy__oBMkOzgUBv4kaqrp2TgEMd8a1tVS22t4dxA-Ew1rWwc91qQMSfRgFD9znevn3JWdAHDQf9I9x8VHuhkpTBLmAyjBzkFHQKCzq_yOueiR9JKCJlYnZ5XM9pvqi7juzAxgOQRsSoHxSWf4MINNu_1GfGTtUq1yjHCtUvnQMCxLmwhEVeUMv7jc7zTdpwwOy7wJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72288" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fTV9PkrxH8qJStzca-VDs-Q2qMobl2PWod8GGpUj81EJd1z6RqAvW989_Tly3X5elYZHk_yNSI-XqZe77amrIX7I7n5tLC02s_kVTXvEZ-F7viVDTwfG221MUsfC5FZV3nQvW6Kagguh8HoM0e_65UnkNmcEzAnuq-y0fR8bAwAYTt5viQGJttnS7GRV1l4qCttbYPcOMm4PWD4_k_TOcch_nHX2deqPVWv-9389zlC7VSV8_Tl37aiYBcOVezw97dSF-RGj7b1EyTkL_0aTG6XFQpABmDxLJefumXUwjAB5xF6s3WT1Ik4YsilLqaVL224-Wbxa8prkAxsn7xqVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه توی ریاضیات و بخش توابع مشکل داشتین؛
این عکس به بهترین شکل تابع f(f(x)) رو نشون میده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72287" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:   طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه. در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه. توپ در زمین آمریکاست.  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72286" target="_blank">📅 00:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=kCoTZzvf4mx7IRPw6IW4KEDAKmouZ2VGun9OaNHlDIUfVTmFZEmGDnPMuxQEQPOdpb5cC2JV8bmLfGGYbL1F52PJhe4viXsnayfwBWQYLC5BIslyZma4w7NIS4rRePuECrOhRh4oldr5eHGCXAipUmpONlD05Rf4azkaaO9J-BIty0qSSxjGXi-dxzLEWYqFJu6_bDPW-NoQ9b-rwma2Zy4UrajuxV8rbYZ8W3SR_uM9i1OzdMcAAvN9YEybcvY-ooJ3WSHC9xV4sonZKJq3Q91Ptcmtwu7EdkaXVGsDAybz3b79NAHDG3xT5JgXcXmEFPPdaIkzaUmcgKdNu9ngIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=kCoTZzvf4mx7IRPw6IW4KEDAKmouZ2VGun9OaNHlDIUfVTmFZEmGDnPMuxQEQPOdpb5cC2JV8bmLfGGYbL1F52PJhe4viXsnayfwBWQYLC5BIslyZma4w7NIS4rRePuECrOhRh4oldr5eHGCXAipUmpONlD05Rf4azkaaO9J-BIty0qSSxjGXi-dxzLEWYqFJu6_bDPW-NoQ9b-rwma2Zy4UrajuxV8rbYZ8W3SR_uM9i1OzdMcAAvN9YEybcvY-ooJ3WSHC9xV4sonZKJq3Q91Ptcmtwu7EdkaXVGsDAybz3b79NAHDG3xT5JgXcXmEFPPdaIkzaUmcgKdNu9ngIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:
طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه.
در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه.
توپ در زمین آمریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72285" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=geP37u5XHCmjd-xuhUmHSDwsRaC9FY451WmfSzQo1Ef1lMRE_Rosx7pvQHlhgzDzdY3h1OPU30bmboWkQgeRRPoN9kQwCgh5SMNzPiD886W-cg-1PtEopO__qiKcw68Q5ZyvFdwt0hFSTXhXEB72uRtaYzi9S1g0LLJGZBfqPylDEkF-kRvFg1yR7XgO6cCvwRs0sX5hp60kW-q7mIpDVQAYGa98ugiPjxFyjVbzE9As-zbmv6wPDQvJ6LPABGm3cdVR-aiEgenvRG1a-xwG6-A1bn5FP1raYTTDqvyMl5igEGVT5sWYqOcPswtyjtrUmN2P49cdbONh6GplqZtL7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=geP37u5XHCmjd-xuhUmHSDwsRaC9FY451WmfSzQo1Ef1lMRE_Rosx7pvQHlhgzDzdY3h1OPU30bmboWkQgeRRPoN9kQwCgh5SMNzPiD886W-cg-1PtEopO__qiKcw68Q5ZyvFdwt0hFSTXhXEB72uRtaYzi9S1g0LLJGZBfqPylDEkF-kRvFg1yR7XgO6cCvwRs0sX5hp60kW-q7mIpDVQAYGa98ugiPjxFyjVbzE9As-zbmv6wPDQvJ6LPABGm3cdVR-aiEgenvRG1a-xwG6-A1bn5FP1raYTTDqvyMl5igEGVT5sWYqOcPswtyjtrUmN2P49cdbONh6GplqZtL7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب‌افکن جدید «بی-۲۱ رایدر» (B-21 Raider) ایالات متحده، پرواز آزمایشی خود را بر فراز کالیفرنیا انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72284" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری فارس به نقل از یک منبع آگاه ایرانی، گزارش‌های «اکسیوس» و «الجزیره» درباره دور جدید مذاکرات ایران و آمریکا را تکذیب کرد و مدعی شد که هدف اصلی این گزارش‌ها، تأثیرگذاری بر قیمت نفت و ایجاد ثبات در بازارهاست.
این منبع همچنین ادعای الجزیره مبنی بر اعزام کارشناسان فنی ایران به نیویورک برای شرکت در مذاکرات را رد و این گزارش‌ها را نادرست توصیف کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72283" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eda15604.mp4?token=pAQFUAncovJtR-jNVHt-RCRwV1C9xKi7_7UHYK3pbHxpcWHH1nUoQpuEyqpeNTRjw0XCcSC2YbIshY3ZOLHj2NwLPZU3urfkRlfmCfXFa_bemFsEKvYMtDt0id6au6aVCKbKI9eFK-_2L0UIJ4zswcecHAwVHA7ByhB5i7Psar92iFiOFVSepo2IJLW3RyXL_zT9KzaMKmlIzkNGfWin2O9DbH3jwCjUMgOZjy_Suat3DdLVV0RX1a4G6O2LttvN8mqD5bbz5xUDaSn3nzCZa_ZFA7FVRpx1-LZ1w8UjtZpNv-4-wmTSXHt5eftZyKq_zkgx6zWcoeNttjHk_CazUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eda15604.mp4?token=pAQFUAncovJtR-jNVHt-RCRwV1C9xKi7_7UHYK3pbHxpcWHH1nUoQpuEyqpeNTRjw0XCcSC2YbIshY3ZOLHj2NwLPZU3urfkRlfmCfXFa_bemFsEKvYMtDt0id6au6aVCKbKI9eFK-_2L0UIJ4zswcecHAwVHA7ByhB5i7Psar92iFiOFVSepo2IJLW3RyXL_zT9KzaMKmlIzkNGfWin2O9DbH3jwCjUMgOZjy_Suat3DdLVV0RX1a4G6O2LttvN8mqD5bbz5xUDaSn3nzCZa_ZFA7FVRpx1-LZ1w8UjtZpNv-4-wmTSXHt5eftZyKq_zkgx6zWcoeNttjHk_CazUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال باشه چرا به یه جمع دخترونه میگن خانوادگی ولی به یه جمع پسرونه میگن مجردی:
دیروز ، رامسر به سمت جواهرده
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72282" target="_blank">📅 22:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=LUmqlM5dopYXlKABK1G4-l1BI2NadEpF8upY6ADtmGv9gMuv2r56R04u3om-TrPblFT5UNuKciz71yo94zM8qdIAoTFdiuMO4ztb3_2f54DB4pPp3NnEBze8xEm0-a8aIJZuL8asIGpjy8LojJwHewQX6Werb4FbwcNWMxiDMunGeO7LO3_hPuC9PJmD8t2rBvmu6RydtBE03Ypui8QlnyK8SrIdhDHnyt33vNBhOI0p6nx8qD75Z7cZQMo5U1aqxFIrpT4621Dg33hvvzvCatDG5j2iuLcfAq29WGk63oHW-hwM8bXM7Yvad9bXid1_Vn8DmtBILvl_B8WBFPKODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=LUmqlM5dopYXlKABK1G4-l1BI2NadEpF8upY6ADtmGv9gMuv2r56R04u3om-TrPblFT5UNuKciz71yo94zM8qdIAoTFdiuMO4ztb3_2f54DB4pPp3NnEBze8xEm0-a8aIJZuL8asIGpjy8LojJwHewQX6Werb4FbwcNWMxiDMunGeO7LO3_hPuC9PJmD8t2rBvmu6RydtBE03Ypui8QlnyK8SrIdhDHnyt33vNBhOI0p6nx8qD75Z7cZQMo5U1aqxFIrpT4621Dg33hvvzvCatDG5j2iuLcfAq29WGk63oHW-hwM8bXM7Yvad9bXid1_Vn8DmtBILvl_B8WBFPKODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روسیه در حال اتخاذ تدابیری برای محافظت از پالایشگاه‌های نفت در برابر پهپادهای اوکراینی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72281" target="_blank">📅 21:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز:
ایران حتی در صورت پذیرش پیشنهاد تهران برای بازگشایی تنگه هرمز از سوی آمریکا، هیچ‌گونه امتیازی در حوزه هسته‌ای نخواهد داد.
تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته خواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72280" target="_blank">📅 20:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=N1ApOF7RkH4Vl4at0MOUFsx1PtqpsAGVKLwDUb6rNjM_p3Avhsowx4eeUgp5-kZnk7Nin-HEMckHRZkHe6bR1MyqxeOtCxuSJr8bYopbP_z7kRmoNV2EUMt0evkkQD-oKI1Zpk2w26i0LXyKAylR93o7DKuEnesWWJMNr56HgYDm9OQ7GGwf8pIR_vOQ9t-5bTS8lxl_k_opXAWykn1I7ssDFwE5DeeGym_fjtksqmg5KMENmBj1PLycW1L9hqSkMCi4IFwMQ0J0c8WIZeF1PT5wUmpI2hvEJ7HGOFATm19p84GirJ3milE8w-BD_tpj-3zLsthqsff72PWuJtHd-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=N1ApOF7RkH4Vl4at0MOUFsx1PtqpsAGVKLwDUb6rNjM_p3Avhsowx4eeUgp5-kZnk7Nin-HEMckHRZkHe6bR1MyqxeOtCxuSJr8bYopbP_z7kRmoNV2EUMt0evkkQD-oKI1Zpk2w26i0LXyKAylR93o7DKuEnesWWJMNr56HgYDm9OQ7GGwf8pIR_vOQ9t-5bTS8lxl_k_opXAWykn1I7ssDFwE5DeeGym_fjtksqmg5KMENmBj1PLycW1L9hqSkMCi4IFwMQ0J0c8WIZeF1PT5wUmpI2hvEJ7HGOFATm19p84GirJ3milE8w-BD_tpj-3zLsthqsff72PWuJtHd-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌بی نتانیاهو یه شوخی برا میلی رئیس جمهور آرژانتین کرد و اونم یهو زد زیر خنده
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72279" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=Mwb6nD2ug3eKLk4m47N8Cu2kHs6yudB9q7aRZ8dsvg2HT5zVmm1D61yG5DsR-btVkHUW6og2DoCxcyWRtwBKN8yS68VAQT0ae7Wgrr6xq72JHLDmVfikEL4JUXINZsA85DEOeHEXP9Rgsj_Gu7IUtRFnf3AGX3sSih5CBS1tXtwcPOfEw59k5IQsEN6if6_6cZeQv9zSm_VKRQ05bibL-RpCPp6OOJ3SwnWqF_hW--txu2ms0rUPTG9jKtEStSig6ocXAKbegttitXiaH4LRCG6yIaHH-E3wbSIIf2P1wxWA6PcwEe1IpAk-6Gy7Ihpuw-ISxJQS03XcAJYx1DZtcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=Mwb6nD2ug3eKLk4m47N8Cu2kHs6yudB9q7aRZ8dsvg2HT5zVmm1D61yG5DsR-btVkHUW6og2DoCxcyWRtwBKN8yS68VAQT0ae7Wgrr6xq72JHLDmVfikEL4JUXINZsA85DEOeHEXP9Rgsj_Gu7IUtRFnf3AGX3sSih5CBS1tXtwcPOfEw59k5IQsEN6if6_6cZeQv9zSm_VKRQ05bibL-RpCPp6OOJ3SwnWqF_hW--txu2ms0rUPTG9jKtEStSig6ocXAKbegttitXiaH4LRCG6yIaHH-E3wbSIIf2P1wxWA6PcwEe1IpAk-6Gy7Ihpuw-ISxJQS03XcAJYx1DZtcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای ۲۴ و ۲۵ سپتامبر (دیروز و امروز)، افزایش فعالیت‌های ترابری ایالات متحده در ارتباط با خاورمیانه مشاهده شد که شامل هواپیماهای ترابری و پشتیبانی آمریکا—مانند مدل‌های C-17، C-5M، C-130 و KC-135می‌شد...
تدارکاتی در جریان است!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72278" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=j2oqq3txTVtno_gsE7o8zMqSW1zQhkgFaIQJsZ8PhsL43JPC_KPIvz4VZPav_v3yJI7XrccafCILYGh8ql7JpGamLsazBRwCpAGu5YK93zft17oCGXwng7Qm6gsNgwCOrO2wvlWKRtCkpdDOltqby7fWzG4wHLT2BZR8ITiPRFz13nZlmDNfzcMd4Co-mZ5PL4RJpvqXx4G4kTylGiq0rTynxc62fr1Qt5mWQM-4A8PkDxZuUdtcIsYgmboIBqN_1xpPYCy3IsCDR0MLMHihHNfYlvbTog3I7Hf0FNNWjwMmopeESHn2Jmw5m6uY8eHgJFq955i62g9I6TymJd_Ufg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=j2oqq3txTVtno_gsE7o8zMqSW1zQhkgFaIQJsZ8PhsL43JPC_KPIvz4VZPav_v3yJI7XrccafCILYGh8ql7JpGamLsazBRwCpAGu5YK93zft17oCGXwng7Qm6gsNgwCOrO2wvlWKRtCkpdDOltqby7fWzG4wHLT2BZR8ITiPRFz13nZlmDNfzcMd4Co-mZ5PL4RJpvqXx4G4kTylGiq0rTynxc62fr1Qt5mWQM-4A8PkDxZuUdtcIsYgmboIBqN_1xpPYCy3IsCDR0MLMHihHNfYlvbTog3I7Hf0FNNWjwMmopeESHn2Jmw5m6uY8eHgJFq955i62g9I6TymJd_Ufg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شی رئیس جمهور چین میگه عکس روی دیوارو ببین؛
ما خیلی برات احترام قائلیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72277" target="_blank">📅 18:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=h5_8uuaeu2Z6RT3JpVcxgMywTfoPS0n7lnjdOivyn8OwGgpADAg4DCPvIf1V825UMny5qpxuksN2hD_F4AFOvi0bAfgdB43p08EYHz5T3n1-ukn3_LKNwZb0cJfY6G8y2jvI2VbEuJkiOQiM25IM0SKtHlokS4h1insokLx71AONj9ZQh0sGxHrW6CThKucFFyE6HZ5BkUbtOIE4Xu0-S4mU6vLcQayMEIkYv9dCjkm7oGhs9V4znl82kAnc-EX2bwd9KvjMJQtL6HM2wV2k_uIMv7u95wyXasQNzrsm16CPXZCqiAXBsxzQ5JWDWbWmJKCECbaO8bIjvYl6oWo6lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=h5_8uuaeu2Z6RT3JpVcxgMywTfoPS0n7lnjdOivyn8OwGgpADAg4DCPvIf1V825UMny5qpxuksN2hD_F4AFOvi0bAfgdB43p08EYHz5T3n1-ukn3_LKNwZb0cJfY6G8y2jvI2VbEuJkiOQiM25IM0SKtHlokS4h1insokLx71AONj9ZQh0sGxHrW6CThKucFFyE6HZ5BkUbtOIE4Xu0-S4mU6vLcQayMEIkYv9dCjkm7oGhs9V4znl82kAnc-EX2bwd9KvjMJQtL6HM2wV2k_uIMv7u95wyXasQNzrsm16CPXZCqiAXBsxzQ5JWDWbWmJKCECbaO8bIjvYl6oWo6lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده با این شرح:
مردی در مشهد با انداختن 100 میلیون از امام رضا شفای همسرش رو طلب کرد ولی همسرش شفا نگرفت و درگذشت و اونم برگشت تا 100 میلیون رو پس بگیره
😑
😑
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72276" target="_blank">📅 18:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72275" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee8Z4pCqWjiqjhanBOEMiL9hPEYI9J4kfRRepjK8BoxmeavEbgiTeTXTpwKVfmPLF3hCarppIewLrow52QIT9R_ylbINMvXat-uKxaL_v6BjGV3OlUUX5osaPd8NMFr5KM-NYsgdn5mp61xxvSMqqa40c8FR6SuA3S4xo3nYi3h7hyeD3gtS1m1g2Ugmoaehvg16nnSXQBveVhgofyZ6qQty6LL1pFPf4LT6Vea8jSme1xVVwSUAZja4Bn7mStUb19MN-pDkHqd_Bd1Wq4e6sS4b8VbLD1gvzsYgFTcEk58vGtAg4ALyDobOxyBh-eF5bWP5a8O1z9lscYcMjAkBiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72274" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=Z79sHMlyZJHyb4-ivP6TiEQti7hiTgR4cg48JIRvK74b-IZxvm9zrV3_bxD9Wdh5oCdR6R3TR6wh_k7pivb0YREwOm7wRc9Q_TO9tkyu9tMO-9GcgwqfLe-4aruD_AGhAdymjnVxRiGxIObIq1uISNKDyOqLdixlqztyJPZGpmd3w7MyEdfczqJYwb38Y_QQ-AvzlF4T-jUE8MZiADFvE88Y_FJNjsYeYm1nImfg6eIXVOGjVDClHWgjiIWTE8uza0Ma4wdKM5TQg030WIuT5SynFRtT6BO1v8chbmrrwQSHf9du6K2gJF7QCKjtAuJpiGbOVnLLBeVTn-DRYCNJmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=Z79sHMlyZJHyb4-ivP6TiEQti7hiTgR4cg48JIRvK74b-IZxvm9zrV3_bxD9Wdh5oCdR6R3TR6wh_k7pivb0YREwOm7wRc9Q_TO9tkyu9tMO-9GcgwqfLe-4aruD_AGhAdymjnVxRiGxIObIq1uISNKDyOqLdixlqztyJPZGpmd3w7MyEdfczqJYwb38Y_QQ-AvzlF4T-jUE8MZiADFvE88Y_FJNjsYeYm1nImfg6eIXVOGjVDClHWgjiIWTE8uza0Ma4wdKM5TQg030WIuT5SynFRtT6BO1v8chbmrrwQSHf9du6K2gJF7QCKjtAuJpiGbOVnLLBeVTn-DRYCNJmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی گسترده در یک کشتی حامل خودرو با پرچم یونان در شمال جزیره میکونوس
این کشتی ۲۹سرنشین و نزدیک به۲۰۰دستگاه کامیون و خودرو داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72273" target="_blank">📅 17:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=JQkc7_wrhulndmc-hQgRcuJYAC1ZpYkGQ3FyCkGxJ97uF8LYP1hoVBn9JDTmSfpPqL96i0F6Elzw1d67Z6wAujC-U8nUBsgAB-hP6oxaP85CTOglCjb-M8oLtJaH-84b5l003euOo-5Ha9xLOErWRsE4dCameR_FZuSwNMu0N_xHqhbu1NsppJBp0kQd8xjjUUd5B_zCuf4yks1ywRDkeYOhIv9COYdmQS20MvOL-1y-J1v5xiWlsqkETWF4K-voe2Q6VrgGNbFgWC7HHmRAUnpESx1_xfE0UgZHNOz7M1A4Hc_NRzZIth5ZUF93GJQZ3Aoqkz196-rYs7WCMKwcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=JQkc7_wrhulndmc-hQgRcuJYAC1ZpYkGQ3FyCkGxJ97uF8LYP1hoVBn9JDTmSfpPqL96i0F6Elzw1d67Z6wAujC-U8nUBsgAB-hP6oxaP85CTOglCjb-M8oLtJaH-84b5l003euOo-5Ha9xLOErWRsE4dCameR_FZuSwNMu0N_xHqhbu1NsppJBp0kQd8xjjUUd5B_zCuf4yks1ywRDkeYOhIv9COYdmQS20MvOL-1y-J1v5xiWlsqkETWF4K-voe2Q6VrgGNbFgWC7HHmRAUnpESx1_xfE0UgZHNOz7M1A4Hc_NRzZIth5ZUF93GJQZ3Aoqkz196-rYs7WCMKwcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت اسرائیلی در سازمان ملل اسامی کشور هایی رو که حین سخنرانی بنیامین نتانیاهو سالن رو ترک کردن یادداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72272" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=Zp4AeyC_CaMVjxLtX5vOtWOV9siCPZbCpojentMWO5T6zg4OXOG_h9wJI1KicTtoWjGuYpMvoaw09Ontu3hBzTQ9zKGoeFMLfbNjHjwuQ8F-CnUzB19M3nDwEnfFc3ndPDGJBeq2IYP9HYGCVJNABRpSkm8qmcxF-B7ptTtSXSMDaQ2lxclIWUFxvjMXMIm4NFq8Mg-y3Sx3haVLyVbPCsNhOANACNB_9AFY9JQCmohRnWGla4w3sJvQk8lEDyuyigEF9AcuIf3xDZzEWj4QmpjbstM_LB8Bu4Zl4IKZ7GiOQVBBGZ4qOmIx7XX5unhN1gFdqv0L_Nm5xLVYRxxI1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=Zp4AeyC_CaMVjxLtX5vOtWOV9siCPZbCpojentMWO5T6zg4OXOG_h9wJI1KicTtoWjGuYpMvoaw09Ontu3hBzTQ9zKGoeFMLfbNjHjwuQ8F-CnUzB19M3nDwEnfFc3ndPDGJBeq2IYP9HYGCVJNABRpSkm8qmcxF-B7ptTtSXSMDaQ2lxclIWUFxvjMXMIm4NFq8Mg-y3Sx3haVLyVbPCsNhOANACNB_9AFY9JQCmohRnWGla4w3sJvQk8lEDyuyigEF9AcuIf3xDZzEWj4QmpjbstM_LB8Bu4Zl4IKZ7GiOQVBBGZ4qOmIx7XX5unhN1gFdqv0L_Nm5xLVYRxxI1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پزشک کودکان : امروز تو تهران ی دختربچه ی ۴ ساله ی بسیار زیبارو آوردن پیشمون با خون ریزی شدید واژن، معاینش کردیم و کاملا مشخص بود بهش
تجاوز
شده، از پدرش پرسیدیم میگه با واژن افتاده رو جاروبرقی درصورتی که دروغ میگفت و مادر بچه وقتی رفته بود بیرون این کودکو با پدر کودک و دوست پدرکودک تنها گذاشته بود...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72271" target="_blank">📅 16:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdIUuWU8NH4Qo2algFTKhv-By3lHzxWyaI5j3kOwr4fclcejrx43zQ0rC0nAbdxxwpOnCwbxzoCj-E9b08EuD39JwHJIfUtutTD7iR5OG4xQLO3F2AO1SJHOvz8UgHUCiAG4RlMht-arWIbkbr6_Z_L8RuxZgNs_gpX61EQqAuuNwqY9c1kJBb70zGBThHvILFZORh5xV0blqaIDHKblQczqagYzLuRgsD_fh6nsOPilDmIIbT8dvvqVN5erJKR7B0c7KRTdruEi4D1HZu9zIvQmwM125l4y_c8KWipKYxrfetcVfMjbz_K6caTyUGTkkEplWVFwNKoI59D0xhmyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=KYzV6KcqbIO5wHPQUyDcN055YSO-cOyks-CALZg94eBf-YzJKM-Z56Lq01Ik3R8oDC35x14crtr1MVDBoWnLs-HgIUqZ91sTZ3G86VujdYOXK-wRKbEOhTVFHWEE1lpoJCM79y2S_wmweb5gbgOUTqwUQGrSafkJUEPiEOj2U5yxhci-KMhNtekomy8_xr-JQSXj7RPkRAwTxxufyY2FU-k6QxpWKTxfo_0U5hgVB00CLYuwQw_J_-L0-84qwZ8k_Z7JApEjJnGQpZaYhf2z7W2iW_rfLWqN6frNBAEpsqQudkkRbSzBrbjdQqDcbc__p1Tth3gFm1hQTVFro7VNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=KYzV6KcqbIO5wHPQUyDcN055YSO-cOyks-CALZg94eBf-YzJKM-Z56Lq01Ik3R8oDC35x14crtr1MVDBoWnLs-HgIUqZ91sTZ3G86VujdYOXK-wRKbEOhTVFHWEE1lpoJCM79y2S_wmweb5gbgOUTqwUQGrSafkJUEPiEOj2U5yxhci-KMhNtekomy8_xr-JQSXj7RPkRAwTxxufyY2FU-k6QxpWKTxfo_0U5hgVB00CLYuwQw_J_-L0-84qwZ8k_Z7JApEjJnGQpZaYhf2z7W2iW_rfLWqN6frNBAEpsqQudkkRbSzBrbjdQqDcbc__p1Tth3gFm1hQTVFro7VNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای اوکراینی به چندین تأسیسات صنعتی در روسیه، از جمله پالایشگاه نفت «پرم»، کارخانه «ایسکرا» در اولیانوفسک و تأسیسات «وورونژ‌سینتزکااوچوک» در وورونژ، حمله کردند.
پالایشگاه پرم که یکی از بزرگ‌ترین پالایشگاه‌های روسیه است، در پی این حمله دچار آتش‌سوزی در واحد فرآوری «AVT-5» شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72268" target="_blank">📅 16:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که یک موشک رهگیر به سمت یک «هدف هوایی مشکوک» که بر فراز جنوب لبنان (منطقه فعالیت نیروهای اسرائیلی) شناسایی شده بود، شلیک کرده است.
ارتش در حال بررسی این حادثه است. هیچ‌گونه آژیر هشداری در شمال اسرائیل به صدا درنیامد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72267" target="_blank">📅 15:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=rpJdwMuDNxlQq1enLcvyFnqv-A0c7wtfom4wY1sc7VWqhl_iFuHlzkCAi0TkTGv7Zeu0sZyA57zNXukneI6O3im5PQZP_NrW4SNTvwWR_xRZdLTCZjJDoNV8kerZSEHf0MXHy07j7LmPCFL_xt0e8lKLbn3l5tergr_6kyWW2PYRdT7RM80ecqj6cX7bZ0vl1nyp5dOVxngWbux-FYzEn1kiOQPFaVvYA0rTsVEuD_nK1Cbx8zTtGH9fD0AGaMVLnRxoM7fGYMRp54bkHV_N3kXcWr6k6ZaVKFpSyuAbDF4Sy3TGe6HIJf6k8-Iv4_Eq0qnhbJiSXT2M5-nltxEN4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=rpJdwMuDNxlQq1enLcvyFnqv-A0c7wtfom4wY1sc7VWqhl_iFuHlzkCAi0TkTGv7Zeu0sZyA57zNXukneI6O3im5PQZP_NrW4SNTvwWR_xRZdLTCZjJDoNV8kerZSEHf0MXHy07j7LmPCFL_xt0e8lKLbn3l5tergr_6kyWW2PYRdT7RM80ecqj6cX7bZ0vl1nyp5dOVxngWbux-FYzEn1kiOQPFaVvYA0rTsVEuD_nK1Cbx8zTtGH9fD0AGaMVLnRxoM7fGYMRp54bkHV_N3kXcWr6k6ZaVKFpSyuAbDF4Sy3TGe6HIJf6k8-Iv4_Eq0qnhbJiSXT2M5-nltxEN4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از پزشکیان پرسید که میخواید بمب اتم بسازید یا نه اونم میگه نهههه نههه اصلا،
بعد بهش میگه اگه بمب اتم نمیخواید چرا اورانیوم رو بردید زیر زمین ۶۰ درصد غنی کردید؟
گفت اونو که میخوایم رقیقش کنیم! یعنی غلیظ کردید که رقیق کنید؟! بمب نمیخواید بسازید؟!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72266" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGEpMQxb00Jy3HfwWtZfj38TJVeoWCoK5EGmASKtmBmJy2AhRnky6L0F8lBW4Vq1rB9WaMN_ZakCBB_162KyGFbu3n68wwT8rKkQdgCGkqr3GVOyZ0NB6oNERTyzbMbgtQGCi0U5GzO7FalwDMmO4ZGyz3V3gjLCZ7XtpB8YlqNDCp1xzYuFz7jXgZkBBqBvZXSLLusOqDIdboswiLTJ-KO1SQpgOGEmtLys93Vivts2suhpEk1N57Kzhv1NM3Y6grby_mSI2WoLX6qN1nTb-6qQnRcQKfcKUc0c7Z-IOxWj3tpHCPK1zdIwTk3-4bdnUywzVnIbuPD6AfBzQjHP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران طرح جدید ۷ روزه‌ای را برای پایان دادن به جنگ پیشنهاد می‌کند؛
به نقل از نیویورک تایمز و به واسطه وزیر امور خارجه ایران:
• توقف کامل تمامی خصومت‌ها، از جمله در لبنان
• آزادسازی بیش از ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران توسط ایالات متحده
• لغو تحریم‌های نفتی
• پایان محاصره دریایی توسط ایالات متحده
• روز هفتم: بازگشایی تنگه هرمز
• آغاز فوری مذاکرات هسته‌ای
عباس عراقچی، وزیر امور خارجه، این چارچوب را علناً تأیید کرد اما جزئیات تمام شرایط را بیان نکرد و اظهار داشت که این طرح تا حد زیادی مشابه توافق ماه ژوئن است.
نکته مهم اینکه او نگفته است که عبور از تنگه هرمز برای همیشه رایگان خواهد بود؛ در چارچوب توافق ماه ژوئن، امکان عبور رایگان برای مدت ۶۰ روز پیش‌بینی شده بود تا در این فاصله درباره نحوه مدیریت آتی آن مذاکره شود.
ایران اعلام کرده است که آمادگی دارد این طرح را حتی پیش از موافقت واشنگتن اجرایی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72265" target="_blank">📅 14:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=uIUnrqkZCLETszmtCMatlKYO9Xoxom86_4TRQnOrCFcRn4LXqlu6GTMIOFHuY_ZGWyB4VODaXoi3H9XGd2uYKaGvZL1jB-y5KnUcbuoCDrpxgegFfBHy0UfFzZ2hULtCxgcpduvvgeJZi4V6G9yZOQgTefs4uabB26okFWWMHuHwEDWiEGixinpvYBqhL0UcptpEbRtK63OPJ22fCT2Ea_1RbqVpltPRSO9M3ZzjqxItaYo2ZGHQzeWFVfR99ZWlw72LixE2-ubf7yjawokSw9HihI6QEiFmTWVcdIqYvQdetTGiFiQLgijXYwTQInjUkzn4Nr7Pbnd3DOK0i_quHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=uIUnrqkZCLETszmtCMatlKYO9Xoxom86_4TRQnOrCFcRn4LXqlu6GTMIOFHuY_ZGWyB4VODaXoi3H9XGd2uYKaGvZL1jB-y5KnUcbuoCDrpxgegFfBHy0UfFzZ2hULtCxgcpduvvgeJZi4V6G9yZOQgTefs4uabB26okFWWMHuHwEDWiEGixinpvYBqhL0UcptpEbRtK63OPJ22fCT2Ea_1RbqVpltPRSO9M3ZzjqxItaYo2ZGHQzeWFVfR99ZWlw72LixE2-ubf7yjawokSw9HihI6QEiFmTWVcdIqYvQdetTGiFiQLgijXYwTQInjUkzn4Nr7Pbnd3DOK0i_quHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم #hjAly‌</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72264" target="_blank">📅 14:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وال استریت ژورنال:کشورهای حاشیه خلیج فارس در مورد تلاش‌ها برای از سرگیری مذاکرات ایالات متحده و ایران اختلاف نظر دارند.
عربستان سعودی و امارات متحده عربی از دولت ترامپ می‌خواهند که فشار اقتصادی و تحریم‌ها علیه تهران را حفظ کند، در حالی که قطر برای مذاکره، از جمله پیشنهاد توقف هفت روزه درگیری‌ها برای بازگشایی تنگه هرمز، تلاش می‌کند.
عربستان سعودی با اشاره به حملات به کشتیرانی خلیج فارس و اقدامات حوثی‌ها در یمن، استدلال می‌کند که ایران باید قبل از هرگونه توافقی با فشار بیشتری روبرو شود.
قطر و عمان از بازگشایی مرحله‌ای تنگه هرمز و یک راه حل دیپلماتیک حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72263" target="_blank">📅 13:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gC4RyH8ko2QbSGDdhPURZKAsxq-aA5LR7YwGyWtqZKyfT7Gl-8_UsNUTrjN109klbJJewWC90MMu9_wwxAjN2o6SSeDFxFtKjJrJMl1NFQjQSfWHr7zEs7QUGrq-LtzZdUfh0oUHcJyF5yNqfhZPoHfro3pgIWg433j7U-DhvHy0wN2EiLz_sXK9-FMmF0vD1bFDvS9NQSmG3f9S-mPKQEiN-kKo2m_Lwq1Nn4MEHN74y6B0JqtzMKzHRJW9SP8pEmkNfuWPCp1svwZsemnzRwJyjDNAj6NfyeduRcFkdM3Q8R1PKFA0r6kG6eWMByoxsA2UDPv-V4f58eI5nCHdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B35vBFg7PfZE8PKTBP3XI_mSU_Ustho4GArDeSn2Bp4zHGcNkRk0tXPOkN4Uy92hm92fcgv0_BsIsrTV1I_HD_nT4SZJocLctfgBffAkK8MRMmH3uMqV3ce8AKv1jtol4HF2_nTRjO1fnN5_-qga8uQHN_OiG43zKaDgznIIYx3AP5en-k3D3OyRWX4Oh4t__a57Ucc-xM8uzGuFFmErKgPXxZLsa_wXwFibTCFZEqqrxrTpHJQqdeBUNVZLR6r6hKpEkzkyNS7BJ-duDjNq0K7bM2ESxab8FTr2WCtz9JFQG5KdqyrQNBcr7_GzMN85AUKmBzxWOoWXwor-rp5SHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hVh0BoImjdOSRC9gxQq1Yldppc1jdutxCWs4fvb1bJlJLpufdXNx0APMrWzZDnHPh4x46zOxCvbT82HHQuofIR0N-Tdh_xRaQlCoBTVyP1wSdNVh6sRMFO5yB6DCuV0oPK4EdpazYASvRKti_gBIFiblA1rDMw32EBVp4NmxNz3ZNDEt8_GsmB5ZwkTNRpyKGqnA5h4apcrC4yhZ6ad1O4xpuDizwMz43SJMXpdG1nhIhmmQuy-WRni8o-HrrQpWDOWdKHVh8mKOFI3dpTaE_DydZn9CTHcY3ySuj2Y4A_CPxhMfMoUWN0-WZL670dVagUxLD5_f63XpLht5pLhJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FfDwk03K8GGi1Xo--4B3MKGAXsHkdCE5EKV_AcKzhtfr-wWiCXapsEVKl2WH5-_FU9Yza8UmsIHtegFz8Z04h-qRedrX8qy7iSVfH7un5aao1QsiAD5EkvcKmBD621CrJmrTuRUjkOPCLV6_qU2cwx7tyJ161WsghX1mFyDzpGdofp1Xhi9batp5ULqUXaeXYXe426CkGCy88AoNGQG-j13wn5NSJhwAObnXxegiF_l_Pva88CUnaz9bf9E6YxCtZ1E1NFVB7kkTCzXCmQtD_HriQQdgIp4-V65cjT_Pv3O5-NEOIwoHA8T6nHh_ErIhHDwSIhDZ3DmAVBziiSn-pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگولی ترین دانش‌آموز امسال معرفی شد
این دختر کوچولو به اسم
گندم
لقب کوچولو و کیوت‌ترین دانش آموز امسال رو از طرف مردم کسب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72259" target="_blank">📅 12:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72258">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72258" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72258" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72257">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkvE7BHXzIrP2t0DNaS5b1A8tqBM4MK-FegQwp7tgeNkZ4c3fl8vKv7zAqvE9wszCPn1V4BOt9906zRB8LDfmudoKlZy2p3D9B7zb7IywD9NnBw29FH628W6WvkrvPbeIHj3cQbgVa7IY3p5rGL-4h-k8Qxa-i1SWkj9h3RcyvFsUeQykOOHsd0-QEwoE00Kgg3bRaoaQ_RKZhfGea-NGIuF-a0q17H9iMsXgecCL_xDA_WzDeVUeIUIazmafhPcSW5CTKAOpuKFq4r8d3DNjPWJ57vaI8ImR8n_AXHbeA_7mFAKIhTMjS3OBBrrmfB2fGjAliozGzHbp3RFIb3EyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72257" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72256">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLb_WwjbQ-PXCFNFVbA7cT_Po5QPsjsaeFD7pGNwekP1GVMhuEaEZdnXaJXSudO8DmwS2c2u7rKiAZQJcwva7c4zxcwJh0EsL0KQgpvwO5OKZB0dJp4Q3d7AMp4fGtovhA-rC0WoE4ECgmI9G9PyjesXKp46kJA0AJwESt9_Mx7yT2YpyACWo5I_5YIzKCNXcKiyyH3XlMxMpGMVbBjyNSB0s8FQrfnztlVGSVjM85b0wJlcc1sl30B6nXaDSi6o8XKQi15A0RV1K8KEdJLgTYSPeyl93C7ydcLPRo5rqDuBUqcN-k1h8Z4SGaZyUy-IudS2g34OdwUVmOzZrXt1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
مذاکره‌کنندگان در حال بررسی توافقی مرحله‌ای هستند که بر اساس آن، تهران در ازای کاهش محاصره اقتصادی ایران توسط واشنگتن، تنگه هرمز را بازگشایی خواهد کرد.
این مذاکرات با مانعی بزرگ روبروست، زیرا هر دو طرف خواهان حفظ اهرم فشار خود هستند: ایالات متحده کنترل فشار ناشی از تحریم‌ها را در دست دارد و ایران کنترل دسترسی به یکی از مسیرهای حیاتی انرژی جهان را.
ممکن است ایران در ازای دریافت امتیازات اقتصادی، از درخواست خود برای دریافت حق ترانزیت صرف‌نظر کند، اما همچنان خواهان حفظ کنترل اجرایی بر این تنگه است. کشورهای حوزه خلیج فارس با هرگونه ترتیبی که به ایران اجازه دهد از تنگه هرمز به عنوان اهرم فشار استفاده کند، مخالف هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72256" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQBUYYKMJFn6FQ2iCfbC9OOK6k7L-3H6ZPzWISRDMe1kcsCdz3ZxjSTG2ONMZoqHkNHlqQ19oP1zttQmDzb1aCbe6FbxHMTZL-Ikbm8R1HXdRM0mTSOLNBNwMrZuorL2764lBGLSaU09flhk82sJEwz3b3y75jpwlmXu2n8VS-FZQybzPk1kK_5mvTa3Ztpdo1j9iBR9LftuDUjqR1AqjwmsfAi3k8d1G9GwE1Tkl7Ergp0sBKb7RpiA3Dff2U0caE-mAzEzMT_j8iF0kLUEI4qknGEVw2FWhQoGrzrr3EfhBVj-1u9IaCDMreeZcSqx_o8bUDiXQfY4PAZqXGuBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=YGdPaQW35ty7_Y4xPHjaR9DEik1qffHpB5B23nHwijM7DbpivTa-OJigtwi6nU7nY6bRcMQQ7Fc2IgX4JmjvXIApxv3DfcijhtlXu1o3b8M61EHNZb8yNw02LUBCBCY5KNHRSNaPLhBAdZf43Z3nVZWlwV3Y6SvC7wPaGSL4HA6wc8ULli_sjyeDiITqi18VSmp3KP0wM0Vg1pI0JKzfm3gKTvTlCl1pvFo_IoAOhK93qBWLZrRECkfsyxVx4j0tCja4TnSh_sFlxpcLRPhEYha6WeJRUm4edAEfpPVQY9z5XCqQfXXDRmiMJVm2O8GGXTgmt-eZZmwLZI2d9bpSBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=YGdPaQW35ty7_Y4xPHjaR9DEik1qffHpB5B23nHwijM7DbpivTa-OJigtwi6nU7nY6bRcMQQ7Fc2IgX4JmjvXIApxv3DfcijhtlXu1o3b8M61EHNZb8yNw02LUBCBCY5KNHRSNaPLhBAdZf43Z3nVZWlwV3Y6SvC7wPaGSL4HA6wc8ULli_sjyeDiITqi18VSmp3KP0wM0Vg1pI0JKzfm3gKTvTlCl1pvFo_IoAOhK93qBWLZrRECkfsyxVx4j0tCja4TnSh_sFlxpcLRPhEYha6WeJRUm4edAEfpPVQY9z5XCqQfXXDRmiMJVm2O8GGXTgmt-eZZmwLZI2d9bpSBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نایا:مقام‌های فرودگاه مانع سوار شدن مسافران به پرواز شرکت هواپیمایی معراج ایران از نجف به مشهد شدند. این هواپیما بدون مسافر در حال بازگشت است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72254" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=M-QUgt7YGoGXWKzkczGS6BJ8ynwvodmqQzp9_gOoN_I3er0TTAtZUVVtMV_h01SChRLf45gT22J1hAFiAdewbbo1E2HNdaMjHm9RnyUlHJpJpnlWD-EVnwV55EzHI3pSNVHIKBnlxfKvtHZJPi0oqgc_ckLy2E78b8eQdpxe_yx8y6XJIsT8lGc_Bdgrs8pKb4ulHOCbvjn3y10fp6HvbmVuzZUZkiC-hza92jEqGijKoMseKQFVlKvCv8jG4hnpVlk-YRahgmOKEG7KnI6pS0wiwZ1-gztKQFXsbtwAXA7BUOSEoW8EOgn0GDtnKC6U0hNnguhw4Pcb8iUO-zxux60ygILPXCHy2J5RHoOyna9Vm9u1IlAVJeR-ZEY9NldKoGnVD0HvREA2zNdXhbByVQ0gqkyNzDbAor--vijbcf4P15ePdtAHB3sCPvvv7UcsiVpDeMO0bncQlueOcc3at5ZiwZVHSnYrNj0_5vTRFsOAgf4U6euTLZ2ZSErNfF69r_i-20ig2jpTyvHJCyrUx2QhdWULAYEcAhUFH9gkgp1sdJicHORudYizbbNZ8Y5nlJR8_efoD3S243dv3L7NhU_-jW8izwX26o_JDyPjdKaXsX37HA6ImPhfGQcDqJwBveq5jzQ0Zyx4NQOHq_IcUsJBxAWjBF8g8f0EjOM0q0k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=M-QUgt7YGoGXWKzkczGS6BJ8ynwvodmqQzp9_gOoN_I3er0TTAtZUVVtMV_h01SChRLf45gT22J1hAFiAdewbbo1E2HNdaMjHm9RnyUlHJpJpnlWD-EVnwV55EzHI3pSNVHIKBnlxfKvtHZJPi0oqgc_ckLy2E78b8eQdpxe_yx8y6XJIsT8lGc_Bdgrs8pKb4ulHOCbvjn3y10fp6HvbmVuzZUZkiC-hza92jEqGijKoMseKQFVlKvCv8jG4hnpVlk-YRahgmOKEG7KnI6pS0wiwZ1-gztKQFXsbtwAXA7BUOSEoW8EOgn0GDtnKC6U0hNnguhw4Pcb8iUO-zxux60ygILPXCHy2J5RHoOyna9Vm9u1IlAVJeR-ZEY9NldKoGnVD0HvREA2zNdXhbByVQ0gqkyNzDbAor--vijbcf4P15ePdtAHB3sCPvvv7UcsiVpDeMO0bncQlueOcc3at5ZiwZVHSnYrNj0_5vTRFsOAgf4U6euTLZ2ZSErNfF69r_i-20ig2jpTyvHJCyrUx2QhdWULAYEcAhUFH9gkgp1sdJicHORudYizbbNZ8Y5nlJR8_efoD3S243dv3L7NhU_-jW8izwX26o_JDyPjdKaXsX37HA6ImPhfGQcDqJwBveq5jzQ0Zyx4NQOHq_IcUsJBxAWjBF8g8f0EjOM0q0k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های یکی از خبرنگارای رسانه های فارسی خارج از کشور با معاون عراقچی، کاظم غریب آبادی:
خبرنگار:
ترامپ‌ گفته میخواد جمهوری اسلامی رو نابود کنه ولی هنوز به توافق فرصت داده، فکر میکنید چقدر فرصت دارید؟
غریب آبادی:
ما با رسانه های فارسی زبان خارج از کشور که موافق مردم کشورشون نیستن مصاحبه نمیکنیم
خبرنگار:
ولی با ⁦CNN⁩ رسانه ی آمریکایی که رهبرتونو کشته مصاحبه میکنید
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72253" target="_blank">📅 10:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=giDnb6RTDUlCCTz_m3IMssK57X2kUw-unufJXPS9fz0D1UGWHqMIiCzUE4tZaVJVZhimZx2CQGONd1QqIShxKi1EG9WV_AwuvuE6eicQh1st2t3djbp2kJycS6z9opNxHbJTAzpYwugR5RbZufF-Wxh0pK1B_pUmVcrN33AWRHnR6ii76Gy4bTbFZ7ZxWkhTxg0WoW2bdEnwtnp-uh9hbeTrdUJK-O6SB07DgF0M0wRTTc7Hd1XTkvYmVSA_hydUPcZ0OsvXQOhb5c-_qT3EgbZEe-qagQStindTY0ypcOIPeI2D9mI5okNOMnZ036BR6S3bENY4ChOK__pd8lPNfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=giDnb6RTDUlCCTz_m3IMssK57X2kUw-unufJXPS9fz0D1UGWHqMIiCzUE4tZaVJVZhimZx2CQGONd1QqIShxKi1EG9WV_AwuvuE6eicQh1st2t3djbp2kJycS6z9opNxHbJTAzpYwugR5RbZufF-Wxh0pK1B_pUmVcrN33AWRHnR6ii76Gy4bTbFZ7ZxWkhTxg0WoW2bdEnwtnp-uh9hbeTrdUJK-O6SB07DgF0M0wRTTc7Hd1XTkvYmVSA_hydUPcZ0OsvXQOhb5c-_qT3EgbZEe-qagQStindTY0ypcOIPeI2D9mI5okNOMnZ036BR6S3bENY4ChOK__pd8lPNfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس سنا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق، قطعنامه‌ای را که هدف آن محدود کردن اختیارات جنگی ترامپ در قبال ایران بود، رد کرد.
چهار جمهوری‌خواه — شامل سوزان کالینز، لیزا مورکوفسکی، رند پال و تام تیلیس — در حمایت از این قطعنامه با دموکرات‌ها همراه شدند، در حالی که جان فترمن تنها دموکراتی بود که با آن مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72252" target="_blank">📅 10:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZiOkztoWER3YAe4pOjRFVVljGwUyuSS_krsvMNM-jRS14RBKefEDy1RuQfiyXqxn9JfV494UPczOCyy0TUJDXxRtCDuBAXiUR_zuIVaXz7ekYQb2ijEpHxyEyn2ahpdpz2BqSTF_FsgUIWKkp1-ZbnU0mIC17xg9f2gSoQmJFI5F_99HL-nnMyTnzqSgSlNW2372sw3TRbpICtNYkyFHqXUTmUSlw5r1lTXqzvxtxqwLZzSERmYRv18_5V7h99DJ7ALD5JmY3uZnJ4GitZ4YH4ILh0v_hzga7B22ybup0RCVyTsQ-kMuqzb435mz4Rv8LEHAQljeQFHVVL0X3Xf_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی‌ نیوز:
مسعود پزشکیان، رئیس‌جمهور ایران، اظهار داشت که تهران خواهان احیای توافق آتش‌بس خود با ایالات متحده پیش از انتخابات میان‌دوره‌ای ماه نوامبر است.
پزشکیان گفت: «ما نمی‌خواهیم کار به انتخابات میان‌دوره‌ای بکشد. ما خواهان آن هستیم که آمریکایی‌ها پیش از انتخابات میان‌دوره‌ای به تفاهم‌نامه بازگردند.»
پزشکیان همچنین اعلام کرد که ایران برای بازرسی از تأسیسات هسته‌ای خود «آمادگی دارد» و هرگونه تلاش برای ترور ترامپ یا خانواده‌اش را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72251" target="_blank">📅 09:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72250" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=GmTN7MajRmkoAWyL4VpXTuGTCWbTUjSdw8tcqLoVGqkPQeDIqoOUhm65Nagn-Oel53cRiN49d6WMUdcsRogVRqZTsX5lUF8kwC5bWLkJ7AUjKipydNaXChjWliS8WvKEl2WlJQhINUj2UkphKRLV4e5UpA27-3rcfOHhyjScZruzNy1bqg2o5B1MhsYyfyKFzKjV_Y1wGuxyIx6MNMH29YYG7FtUoEJRPTY6G-1y8d6ef2WYznGxf6hr7c_PUkB2_kUoTtOkdhtViPKMkKWlP8Onnu7CQQK3HSpTTjWKoDZlBM-qVSh_8KFIqIG5pvmVeJ9LkMT516ur7haM6p-YwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=GmTN7MajRmkoAWyL4VpXTuGTCWbTUjSdw8tcqLoVGqkPQeDIqoOUhm65Nagn-Oel53cRiN49d6WMUdcsRogVRqZTsX5lUF8kwC5bWLkJ7AUjKipydNaXChjWliS8WvKEl2WlJQhINUj2UkphKRLV4e5UpA27-3rcfOHhyjScZruzNy1bqg2o5B1MhsYyfyKFzKjV_Y1wGuxyIx6MNMH29YYG7FtUoEJRPTY6G-1y8d6ef2WYznGxf6hr7c_PUkB2_kUoTtOkdhtViPKMkKWlP8Onnu7CQQK3HSpTTjWKoDZlBM-qVSh_8KFIqIG5pvmVeJ9LkMT516ur7haM6p-YwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جناب نخست وزیر پیامتون برای مردم ایران چیه؟؟
بی‌بی نتانیاهو: ما با شما هستیم نا امید نشید
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72249" target="_blank">📅 08:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">با این جوابایی که پزشکیان به خبرنگار داد باید منتظر موج جدیدی از حملات طرفداران افراطی جمهوری اسلامی و تندرو ها به پزشکیان و دارو‌دستش باشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72248" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پزشکیان:
- انصارالله مسئول اقدامات خود است و از ما دستور نمی‌گیرد.
- ما اورانیوم غنی‌شده ۶۰ درصد را در چارچوب قوانین بین‌المللی و پیمان منع گسترش سلاح‌های هسته‌ای (NPT) واگذار خواهیم کرد.
- ما به تمامی تعهدات خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای پایبند خواهیم بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72247" target="_blank">📅 07:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=Hm4R29907ZA47XNWLaVt4Oky49ypNq0f7cz4aKIEQKC5DRsql1vwclEwAk4buSiqVz7yQE1ninbDrJ6mS7TFJktqSvtQ9xh0HRCpSusTRSxlqPQjjhaTdQl4X7II7pZmhbs0EiLNtv4lzjD0XEo-upHHIvgJvHP0x599f8r82JqHti7AJoKsmT55Jhs5mJ9EqoWDGomKfe1Eom56PZpXUc4Atypp040J24KF_xz_LSpilb1TiOHKk9n6TW1xhWwaqVxmTD0lUKlL5XPOH85xD2NNDYkto8Mr4HbFcyrt8Km0gDGAoX8XdhT24ohcrgQMEQQXEJ7qERbRYqOJpGAP_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=Hm4R29907ZA47XNWLaVt4Oky49ypNq0f7cz4aKIEQKC5DRsql1vwclEwAk4buSiqVz7yQE1ninbDrJ6mS7TFJktqSvtQ9xh0HRCpSusTRSxlqPQjjhaTdQl4X7II7pZmhbs0EiLNtv4lzjD0XEo-upHHIvgJvHP0x599f8r82JqHti7AJoKsmT55Jhs5mJ9EqoWDGomKfe1Eom56PZpXUc4Atypp040J24KF_xz_LSpilb1TiOHKk9n6TW1xhWwaqVxmTD0lUKlL5XPOH85xD2NNDYkto8Mr4HbFcyrt8Km0gDGAoX8XdhT24ohcrgQMEQQXEJ7qERbRYqOJpGAP_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز:
آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
پزشکیان:
آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72246" target="_blank">📅 07:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=p48ArVrv7S2rzpLH0TL5HaBoz8H9eTAIrJGPKsHBGAdD0pjOywrYu6jtgkrrl98P6G2d3WPYMX_mostqehBkXA4xiezsWjMbS6pee1-R9czxccMNlT37zhEDnrO1uZhQK9K2o4yr00omEDKSvsGtMVDThtWD1KSNn5sL4sk32fu8cjN-4L8W1QFTVkd6Ez8Est9OtlI2-TdlCOdrTVWAaDggy0VqB3prB3xdfrcrVli057AcL8j1YUm6SuuXGjs-SlNzUoYRDUQM0FlKDEi2_VyT5Cl79kZIP-rcqBtvlbJlvFTlrXS_u7e3Vkjzbf47-EC-v8ddjoSEVXMBbkLnApMLE65RH7QKHENL6jrKmp2e-uE0lR5-BB0jJS0azX0tzFbso28KQXTCykKaIWklVexBAr091dYgNpMPpxAmFpm6WaRZ99L5TdJfNp_o3s3hcwYCUa6SsQ21Eoc30wi26x2kN3Ze8vL82BrDZd81o3PqYdcTkl_NcAFbkmCy89xOb9Wa-B9oi4ogm_xyDM6KQDP5wszdI3twq79dcRcwnvfpU1crznCzw5Yuxs1tPMk7q-ujQk0aLinNQU3-tC3ipJNhB8ZXoTbzk6x7oHvZwZIXZBdMBH33euZBjKQUojXYcBSuIX8F_X56-TrJ0DGTI19i9af6Fa-av1HFVx5NXHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=p48ArVrv7S2rzpLH0TL5HaBoz8H9eTAIrJGPKsHBGAdD0pjOywrYu6jtgkrrl98P6G2d3WPYMX_mostqehBkXA4xiezsWjMbS6pee1-R9czxccMNlT37zhEDnrO1uZhQK9K2o4yr00omEDKSvsGtMVDThtWD1KSNn5sL4sk32fu8cjN-4L8W1QFTVkd6Ez8Est9OtlI2-TdlCOdrTVWAaDggy0VqB3prB3xdfrcrVli057AcL8j1YUm6SuuXGjs-SlNzUoYRDUQM0FlKDEi2_VyT5Cl79kZIP-rcqBtvlbJlvFTlrXS_u7e3Vkjzbf47-EC-v8ddjoSEVXMBbkLnApMLE65RH7QKHENL6jrKmp2e-uE0lR5-BB0jJS0azX0tzFbso28KQXTCykKaIWklVexBAr091dYgNpMPpxAmFpm6WaRZ99L5TdJfNp_o3s3hcwYCUa6SsQ21Eoc30wi26x2kN3Ze8vL82BrDZd81o3PqYdcTkl_NcAFbkmCy89xOb9Wa-B9oi4ogm_xyDM6KQDP5wszdI3twq79dcRcwnvfpU1crznCzw5Yuxs1tPMk7q-ujQk0aLinNQU3-tC3ipJNhB8ZXoTbzk6x7oHvZwZIXZBdMBH33euZBjKQUojXYcBSuIX8F_X56-TrJ0DGTI19i9af6Fa-av1HFVx5NXHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
خودِ آقای ترامپ اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده بود تا حکومت ایران را سرنگون کند.
اطرافیان نتانیاهو اعلام کرده بودند که نیروهایی از استان‌های کردستان و بلوچستان به مراکز کلان‌شهری نفوذ خواهند کرد تا حکومت را ساقط کنند.
آن‌ها تصور می‌کردند که این ماجرا سه روزه تمام می‌شود و حکومت سقوط می‌کند؛ اما حکومت استوار ماند و منسجم‌تر و متحدتر شد.
حتی کسانی که به دلایل گوناگون در برابر حکومت ایران ایستاده و با ما مخالف بودند، اکنون از ایران حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72245" target="_blank">📅 07:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=E0O_WUXO2oYIqPoQFXVqxuxUhWpnju3C3y5IUNnuCuUZ3vX6mS4-5RdLw4-0MkaNtOpRSD9YhCsM_Qq-Yq6J8JPbd9C4XJetAsQrr_92HeOykwJaLehwtGfwKn83cYV8XWk9Kyz17d3cz9mq6W_CzXp2FGXPx3Mr7qT-Gp3Lfr5evvjtkOb6tl7UkvvuYavG6JACkOB5xqsURRpVLLtx02LEEv80baKaJUjCUH1vDR_ogAzLavmVT2XFlkUAOPQb0sRLhUM00lKGewHogG12e23ofd15cm53zbeMcrvBlGppIT1p5EmIquHNdQp12NhIQcrHVlNiMcT92ZG5mxyEDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=E0O_WUXO2oYIqPoQFXVqxuxUhWpnju3C3y5IUNnuCuUZ3vX6mS4-5RdLw4-0MkaNtOpRSD9YhCsM_Qq-Yq6J8JPbd9C4XJetAsQrr_92HeOykwJaLehwtGfwKn83cYV8XWk9Kyz17d3cz9mq6W_CzXp2FGXPx3Mr7qT-Gp3Lfr5evvjtkOb6tl7UkvvuYavG6JACkOB5xqsURRpVLLtx02LEEv80baKaJUjCUH1vDR_ogAzLavmVT2XFlkUAOPQb0sRLhUM00lKGewHogG12e23ofd15cm53zbeMcrvBlGppIT1p5EmIquHNdQp12NhIQcrHVlNiMcT92ZG5mxyEDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما هرگز به مردم خودمان حمله نمی‌کنیم.
برت بایر (از شبکه فاکس):
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی علیه ما اقدامات تروریستی انجام داد؟ چه کسی مدارس ما را هدف قرار داد؟
بایر:
متوجه هستم، اما در روزهای ۸ و ۹ ژانویه، قطعاً نیروهای امنیتی شما شهروندان ایرانی را کشتند.
پزشکیان:
خیر اصلا اینگونه نبود.آنها تروریست هایی بودند که توسط آمریکا و موساد و کرد‌ها مسلح شده بودند.ما به مردم عادی آسیبی نزدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72244" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=dDG_kFgIaEPfg9ipRIEKIQOA7ZDrp0HK8SswFfZ6qOLW833XY45JmCS4S_ZJxM5AwbQSGpxq3TA8j1MTHB6Hw_86u2YOi7kEdkCFOEGRNUStV38QAb1VsV-ZAbsyVzHZALp41tDd_2j94jyQ1J1zYvbay-Yz2f6Ffa6LhYXHJcMB05Hh3tV6Rbpe9kduAuiwXrly11wzRoZkxwmFt1pq1B79GqUJyiAAyZNvPsYz2CwxKVMQRmM6xCl_vPKxhkzCkGSNqF3SOXcwGCBg3H5i5423fcKFtWIBk_4Lu-YTVz2kg8NxAlis7p0U7SHqy-6fbasbvKk7j_thybDh7DE2-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=dDG_kFgIaEPfg9ipRIEKIQOA7ZDrp0HK8SswFfZ6qOLW833XY45JmCS4S_ZJxM5AwbQSGpxq3TA8j1MTHB6Hw_86u2YOi7kEdkCFOEGRNUStV38QAb1VsV-ZAbsyVzHZALp41tDd_2j94jyQ1J1zYvbay-Yz2f6Ffa6LhYXHJcMB05Hh3tV6Rbpe9kduAuiwXrly11wzRoZkxwmFt1pq1B79GqUJyiAAyZNvPsYz2CwxKVMQRmM6xCl_vPKxhkzCkGSNqF3SOXcwGCBg3H5i5423fcKFtWIBk_4Lu-YTVz2kg8NxAlis7p0U7SHqy-6fbasbvKk7j_thybDh7DE2-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
رئیس‌جمهور آمریکا اعلام کرد که ما تروریست هستیم.
اما در واقعیت، همه به‌راحتی می‌توانند تشخیص دهند که ما قربانی و هدف تروریسم بوده‌ایم؛ با این حال آن‌ها می‌گویند: «نه، ما چنین کاری نکردیم.»
آن‌ها حقیقتی آشکار را انکار می‌کنند، اما در عین حال ما را به چنین اقداماتی متهم می‌سازند.
ما خواهان زندگی در صلح و آرامش در منطقه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72243" target="_blank">📅 07:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=q-Sbe5zyC_zh-swFGbJZ0Am8-wosmDm0zs46LwTG9ODbRKEC-CFVbLVJRsntYzInLgsbURVdAc3A_za9ypmulTZWVN6HgBvN4o7WG70e9O0gK3lL_LuIr2U29PJVgl2g8VPrTNyDXsZImOeX88IbFv5w2LC6fWt1_bVNU_NDZ6iIgrG5k8m4PS0-H3X71UgCtvQuHGw-pdtQhz6BrwYHGUf6XrJXo-Ut3czjdVdPw3y2mBsE54O09AmARXzzfygL79WzLt1Xcx_O9cT7GyHVU4HqzmmnlKba9cUdePMWMMpmnc1XWNZRAi0j7CjbymTqNMhrQIlqfyZXP-i7WPFsZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=q-Sbe5zyC_zh-swFGbJZ0Am8-wosmDm0zs46LwTG9ODbRKEC-CFVbLVJRsntYzInLgsbURVdAc3A_za9ypmulTZWVN6HgBvN4o7WG70e9O0gK3lL_LuIr2U29PJVgl2g8VPrTNyDXsZImOeX88IbFv5w2LC6fWt1_bVNU_NDZ6iIgrG5k8m4PS0-H3X71UgCtvQuHGw-pdtQhz6BrwYHGUf6XrJXo-Ut3czjdVdPw3y2mBsE54O09AmARXzzfygL79WzLt1Xcx_O9cT7GyHVU4HqzmmnlKba9cUdePMWMMpmnc1XWNZRAi0j7CjbymTqNMhrQIlqfyZXP-i7WPFsZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما تا آخرین لحظه به مقاومت ادامه خواهیم داد.
بله، قطعاً مشکلات اقتصادی داریم؛ اما برای بقا، از هر سختی‌ای عبور خواهیم کرد و ایستادگی خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72242" target="_blank">📅 07:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=uCvbXJ2PxNZEl53Ln5IZ3DFN0f6KNigYq_0Omnn7RDnkn74cxAa_pe6jUG_4ZcRFEFuP41IPtfQ1STz7yg3DJb1OE-vvSE_TiA46rfBVqNGEAkQtaQhTYDgu2JF5PD0zJU_238EdqdEF_gbM49tzdODLMAgHTLndGuV4qPFvDxJaqu3n-nLQ7zTJcHNVlDuMc6m4tK_S9ROLLNuxRfYFCxB5mzRs6Mmv_LYtTZDpHoMq6ZtDa6iAozqFb9JfaydHJ1e2iHOqo94Rza1xZTVlYLJKK8y2QMV_ctPER76QksAuStxsrb7Wq72dtvTgIb-WVWFs_aRsRswQClqxkmrhnAuDDLrpU-fjZ3x9dl03mmL2tMyMycBXeR-AkjSBRBMMKj8Hj3Nu6DWx9Ts8sKKBLRFLRLhmGo4TiP8Xp1nX0QK4o56ZA5W3KTkx14HLyJQK1-h20K_u4qp76zxVAAmaNKESsYM9-zCubBbmQFHWYcyyQUsdxW6kr2In6GFvtjnEB-kyVtavkxU75hqsaWzAYZ5ndQrL6cSorF48Oa-h-Ziw0_yukUMlORbGfey6Jxq3-tQh4GXRwxbrp7q2GNRtMmuHpNbJWWzpzONkTQJrZBZcLUIMskB7GFQbLdv1jBfwYZiv100v8U9MBKeUn2t0mbXmGmLjXdfNOkhd5axH40Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=uCvbXJ2PxNZEl53Ln5IZ3DFN0f6KNigYq_0Omnn7RDnkn74cxAa_pe6jUG_4ZcRFEFuP41IPtfQ1STz7yg3DJb1OE-vvSE_TiA46rfBVqNGEAkQtaQhTYDgu2JF5PD0zJU_238EdqdEF_gbM49tzdODLMAgHTLndGuV4qPFvDxJaqu3n-nLQ7zTJcHNVlDuMc6m4tK_S9ROLLNuxRfYFCxB5mzRs6Mmv_LYtTZDpHoMq6ZtDa6iAozqFb9JfaydHJ1e2iHOqo94Rza1xZTVlYLJKK8y2QMV_ctPER76QksAuStxsrb7Wq72dtvTgIb-WVWFs_aRsRswQClqxkmrhnAuDDLrpU-fjZ3x9dl03mmL2tMyMycBXeR-AkjSBRBMMKj8Hj3Nu6DWx9Ts8sKKBLRFLRLhmGo4TiP8Xp1nX0QK4o56ZA5W3KTkx14HLyJQK1-h20K_u4qp76zxVAAmaNKESsYM9-zCubBbmQFHWYcyyQUsdxW6kr2In6GFvtjnEB-kyVtavkxU75hqsaWzAYZ5ndQrL6cSorF48Oa-h-Ziw0_yukUMlORbGfey6Jxq3-tQh4GXRwxbrp7q2GNRtMmuHpNbJWWzpzONkTQJrZBZcLUIMskB7GFQbLdv1jBfwYZiv100v8U9MBKeUn2t0mbXmGmLjXdfNOkhd5axH40Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه‌ای بیاورم»، اما هدیه‌ای که آن‌ها برای ما آوردند، موشک‌های هدایت‌شونده، تسلیحات سنگین و ویرانی بود.
آنچه آن‌ها واقعاً به دنبال آن هستند، دامن زدن به وقایعی در کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72241" target="_blank">📅 07:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=XfDhG4dHWdkr1Utc_OO_bnnddQo_9rKJqDQa0ROehBklRwmq0PAG-YX1O_qCxeQvnRXQz4LinQknn83-qHI07V-BFCLuAXwAvdwksa1EjMkOrO5ntoJ0t-nGK3NFondr-hhAPweKw4fie-uv6-c-_0zCdtmxFFdsFt-rHoFmM6ekZI8u8I1pQ44Zcgkew2M8ukilHHpimMAw6D3P9wSupknlUE4dNu3FeAf7gQbr4dqZh3Y-vlL4ywBCt8qzeMdTM0e1Eh8JTjzckOfbvSxWRBSpTAheowFZq7a1dahx-LHB5W4aXb2S96I_Xu6L0G109xiNEengieOQnblv9Ly64A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=XfDhG4dHWdkr1Utc_OO_bnnddQo_9rKJqDQa0ROehBklRwmq0PAG-YX1O_qCxeQvnRXQz4LinQknn83-qHI07V-BFCLuAXwAvdwksa1EjMkOrO5ntoJ0t-nGK3NFondr-hhAPweKw4fie-uv6-c-_0zCdtmxFFdsFt-rHoFmM6ekZI8u8I1pQ44Zcgkew2M8ukilHHpimMAw6D3P9wSupknlUE4dNu3FeAf7gQbr4dqZh3Y-vlL4ywBCt8qzeMdTM0e1Eh8JTjzckOfbvSxWRBSpTAheowFZq7a1dahx-LHB5W4aXb2S96I_Xu6L0G109xiNEengieOQnblv9Ly64A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت فعلی آمریکا بخواهد در چارچوب حقوق بین‌الملل به توافق برسد، بسیار خب.
اگر نه، چه پیش از انتخابات باشد و چه پس از آن، برای ما چه تفاوتی دارد؟
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72240" target="_blank">📅 07:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=DEzNndw8HlDJykCwl1ESOEP9WCUW9qUqmO--zcjnod3wpsz6F5yyJXWbQjjJw2Ztizp3oJYbP_WA893kbD5TCX3OpO28MM39qnr7jb78qpJl7usaZ8i8X367gOY4ENASFX5_k7o6-i4p8g2y9whhBHWnWjmjLtjI4yPjd8_3EZOlQhibO9peE0WVaZhxRC4_oxI-YZ_Phpxt4I761zQFzwKVwao--1BBl7k3L1eNK91fqCgvA0wNkdDI3odpkB9HdqJv9XqcwGACCupgZW5nbc9wYGuhXIN6Lp6plIA1G8WKSATpP9DwwUB64lTT2-ZV8RT-q3gZ22AznWWAItD5nYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=DEzNndw8HlDJykCwl1ESOEP9WCUW9qUqmO--zcjnod3wpsz6F5yyJXWbQjjJw2Ztizp3oJYbP_WA893kbD5TCX3OpO28MM39qnr7jb78qpJl7usaZ8i8X367gOY4ENASFX5_k7o6-i4p8g2y9whhBHWnWjmjLtjI4yPjd8_3EZOlQhibO9peE0WVaZhxRC4_oxI-YZ_Phpxt4I761zQFzwKVwao--1BBl7k3L1eNK91fqCgvA0wNkdDI3odpkB9HdqJv9XqcwGACCupgZW5nbc9wYGuhXIN6Lp6plIA1G8WKSATpP9DwwUB64lTT2-ZV8RT-q3gZ22AznWWAItD5nYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما هرگز به دنبال جنگ نبوده‌ایم و نیستیم. من عمیقاً معتقدم که انسان‌ها نباید موجب مرگ انسان دیگری شوند.
قرار است ما موجودات برگزیده خلقت باشیم. وقتی می‌توانیم مسائل را از طریق گفتگو حل‌وفصل کنیم، نباید به کشتن یکدیگر متوسل شویم.
اما با اقداماتی که اسرائیل انجام داده، آن‌ها این جنگ را به ما تحمیل کرده‌اند.
با این حال، ما خواهان ادامه آن نیستیم. این آمریکاست که باید تصمیم بگیرد آیا می‌خواهد به این وضعیت پایان دهد یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72239" target="_blank">📅 07:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f631e90489.mp4?token=R3mfpi9ezW8X-MmWhzRPUUGxWokQa82zQklLCz51Bs-V1wsBUgV0XRRYgnZpyvUwSuYGGsiJ35w0A7ejNcA3PE2HgH3yR1-Tu4r2OFjkf3QlkucvcqtAd2FXP6AkAp6X0eymT69ynhUsvTD1qquO1mZyHqtyxJwbqFY3UmaaFTNnSgh31_wRUp-Y8IqJBC0UVIWM4OZysKYa3tJMfp2a7-KqBvnrgUH8gzOR-77KRttpghmKM8_fZD0IHYp6H4l9CeFm3UczEwDh3HuPLJr2AtrNuCWq0yyBX2C96pzfUyUXfe3TI25yAc1325erhCpijyQ_O-BaqrYWuOI0W8MQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f631e90489.mp4?token=R3mfpi9ezW8X-MmWhzRPUUGxWokQa82zQklLCz51Bs-V1wsBUgV0XRRYgnZpyvUwSuYGGsiJ35w0A7ejNcA3PE2HgH3yR1-Tu4r2OFjkf3QlkucvcqtAd2FXP6AkAp6X0eymT69ynhUsvTD1qquO1mZyHqtyxJwbqFY3UmaaFTNnSgh31_wRUp-Y8IqJBC0UVIWM4OZysKYa3tJMfp2a7-KqBvnrgUH8gzOR-77KRttpghmKM8_fZD0IHYp6H4l9CeFm3UczEwDh3HuPLJr2AtrNuCWq0yyBX2C96pzfUyUXfe3TI25yAc1325erhCpijyQ_O-BaqrYWuOI0W8MQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
یکی از مشکلاتی که با آن مواجه هستیم، مسدود بودن منابع مالی ما در چین است.
ما حتی نمی‌توانیم پول خود را از کشوری که به آن کالا صادر کرده‌ایم خارج کنیم، چه برسد به اینکه بخواهیم از آن وجوه برای پرداخت به طرفی دیگر در گوشه‌ای دیگر از جهان استفاده کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72238" target="_blank">📅 07:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=gXSYGQSELZLpCs7rU1jp73LE0zfQEpBBrDLvmrPLpxDc50EI5lg_pED74Qzx0YpnXZ4AdzXzttAmeSpDkvNC3l3QgwUJpZrgaKycWUpBQYa9YdH6VpqJ5gw4AjmFCaUmi1DLxI1gFGGONNvSitppWesxbdMPUd1MFviW6frj0ZQ-WU65M2Cboy6lcIzeoofkxMuP_3GRbDMii0VAp5LdV49oAW7AVkW3UT7E6uunsVnvOSjT4B9u_F8z0yOCBNgPS3abUGE6lNuOCHM0aqi9aT7a4KdpW0dyVw8h91Ac3GIvK_A6snQYI5vslLMiIlyVO8FmELMKmrDJ8TdTy0IdCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=gXSYGQSELZLpCs7rU1jp73LE0zfQEpBBrDLvmrPLpxDc50EI5lg_pED74Qzx0YpnXZ4AdzXzttAmeSpDkvNC3l3QgwUJpZrgaKycWUpBQYa9YdH6VpqJ5gw4AjmFCaUmi1DLxI1gFGGONNvSitppWesxbdMPUd1MFviW6frj0ZQ-WU65M2Cboy6lcIzeoofkxMuP_3GRbDMii0VAp5LdV49oAW7AVkW3UT7E6uunsVnvOSjT4B9u_F8z0yOCBNgPS3abUGE6lNuOCHM0aqi9aT7a4KdpW0dyVw8h91Ac3GIvK_A6snQYI5vslLMiIlyVO8FmELMKmrDJ8TdTy0IdCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با خبرنگار فاکس‌نیوز:
هر کس بخواهد اعتراض کند، کاملاً حق انجام این کار را دارد.
ما با بسیاری از این کارشناسان گفتگو کرده‌ایم. اما تبدیل اعتراضات به ابزاری برای تقابل (مسلح کردن معترضان)، مقوله‌ای کاملاً متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72237" target="_blank">📅 07:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72236" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMseW3WHUpFd5QQErmo1C9-2jPlzNnwaJm1vtvz0Q9zCDsZubd0C8gu5wx0QKR0EbFYtIpmCf_WdqL-7ddYHhyZBTZSOFLuFWeuE3FryKkITg3daFAl2XVtzIVtQuhuFYNc3Nx8U36XzOwOp2D9JDmWM-3j66s1CaGQSo7ULdy9fLrrLQVL7yp8ee5Ra_FxRj6zYVqWbhl4e5pkvVoPveUhfhVz3NUIj6b6oA6yjLPqvKlQYk4qR22frwilqf2apADSJBa3a0QVda_W_K0yNJUyPU2Mj5fViHWn7lI-KHRGu4WC1Em8Cn9oJDxNtBdzGmDMuuVO-D4QnqmOkPV3zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72235" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
