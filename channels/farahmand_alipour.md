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
<img src="https://cdn4.telesco.pe/file/GyrzGtBQIJjVpURtcAMX6LUspG4VzmnDizIOQie_RKHl9s3RvXIbUDWva7RL9jwmj8UnwJU7d4QP3-_amWb1lxsO7bzGRwhu8Zxu3Ck-lSlTdhQTzjOsgpAVjmqjJ02jmn7aEJGZxOMMalioEsHOz3Ww9asYyX9Pm7KEjRoMvT8fiMMW2IVFCty0bkwQ4BLvGMeVekzAh8jcvJMgptnLm8ElVeczl2anHpribJRtKOpyG-8RhyNqvo3GSQI-senNCDLavdBCX1VTrJZi4PHToeHD4Gkc_MIMVOTpynK7YBo5I0Nx8rpFMzVkJm0uFLgyXV4lAoBSHOBUhDDegODkQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 22:06:34</div>
<hr>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=sfqjqhvYJHrUzDtd16e4xmZKH0NHJR3VrgtrifbD1As3G1OeH9C6HGerHNWNJFCFqSZFZ2no7e5xIo8W_IHQWuemBYJc167IoVgbxQFJY00pE45s1u-vmLA40gSLjWEAsbOsEYl7yK5NiOqyKBwysp0fgPlkvaFWj1zuaongXRUUfMgfpgVy89yAA1Ikn2-Dsd6LbZi9cJRTBAdOpN0w8Ifmt8Fa8CZQZUJ5pT9yrO_hyqX7eex-UHk4j0jHakCLj-nvUegveYRhX4XcSrmGwzDwhgiGBUKBv0iE2uhnjPiepXeTvk0RGkvmQ4OkiUq9uUjKL1q_sZOa6PSKFEUqWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=sfqjqhvYJHrUzDtd16e4xmZKH0NHJR3VrgtrifbD1As3G1OeH9C6HGerHNWNJFCFqSZFZ2no7e5xIo8W_IHQWuemBYJc167IoVgbxQFJY00pE45s1u-vmLA40gSLjWEAsbOsEYl7yK5NiOqyKBwysp0fgPlkvaFWj1zuaongXRUUfMgfpgVy89yAA1Ikn2-Dsd6LbZi9cJRTBAdOpN0w8Ifmt8Fa8CZQZUJ5pT9yrO_hyqX7eex-UHk4j0jHakCLj-nvUegveYRhX4XcSrmGwzDwhgiGBUKBv0iE2uhnjPiepXeTvk0RGkvmQ4OkiUq9uUjKL1q_sZOa6PSKFEUqWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-2FYTo4tNQZdQjV9-gto5SwhM0Z4KjxOKs9KyHxGQ1mFJM7g2rS6NPryq1aRPVfjN3O6APqmNkIP7h1lM4KZbJHkRO6Obsnmnlsqd1xbz-Gevain3RXHz7KCPHSzen8KgesZAhTk7qtzeqqPnVxT1UiizLOnJwK1AGrf4LJdG4Wmq4wYRF3WaUBhgmRhXwlEE4aVrwSsNxG5KVVmGykqzck9W7qpgz1-lOAT9qw-Y0YFoXTWYokvHSwGVuo2AuePEMXuzcCM8mtybO7zhZBBTGHgeB6XYrtJMPCm8TxQ4Tl7ksQ91N-uEmNX5S4UO_PHAhtXOYY5gc4-aP03UU2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PchmgV0Pk6aXuN-ZVDCAogkduEMHwTwXliejClCzGghinkGUAXjyhSy-DTRnCWiYnsh5jOpD7E56-IYzfXjgD7M9VqTDJZQ_j4tPcotU37oskAIhWG3KpQFC-AV_tQk4auHK7__luKoEB2OTQgjRwCKcZTOLSSXcq2E8H5k9_tBhPh8NpbjvPfPdd0DSOH43SdE9Kx_QoJiCOcUlgvo8fOvI1QJ8_tWFh-txixRu6UQVRLxBfWamWQfbz8-U5Vhz5DNgAGhbO3VoRikaRV3GP05EAS12GQsEKsXQSd5P1LWwoO6ERld2gEjvMW2na8sBEcl0Jm6UB1gZ6LcETELg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf9AuUzZBGWHMWBK4_uVpkf08-DEgdMiEzGgZhpePCuCbzow1i4w_ZObT7Py8tunmAJ_m_QCBwa-2HjPrHg-AHCpkHGivXGSW1mdiy5u8myaZWBwgRQZ3sGy8ZPfoU2_JwA0Y8uc-Vi8DPXQDbbV4frshqi-A2wrhNRiR5k4mpprbR9jZJbh-AR6SWb_Nu_xSE3j243EGVPHv4bDjHh59QsEqLPt02_dNhhawFIpVj7qc-yHbiueSeccComI4jziZaxB9eQZFPboDkdspvgVUr3Fptc9b8G3YKhryHo0mUgzOpVGP-Jz-XFWbZsQ2e5BvkqlAzHjTclgNrmZOOwJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzg5-__0tS-5U3UwOwBgufgPSdyfkzsv5AVHjc7jLEHds9zGXbWDfeQsSPxM4qZOZO_sWOLbGvzgEyDBjTVbo7uUYMnL_2W5glcn6MucycUSKBQReRCdoyYXbzRRn2SuughsHqGXeqK--FQBto_StiqRAPkR_bsMO6qcdxkPHrCaMFzi6nQ99uYXLINnvp5fcJE1aT7QCcbz5d2awLdVh-0R04uCWNrnJqEqRl2hvDqlUKlc-24dsD4ffXO_6KVsuBPPc84A-iXxYNYYDgEDi-66X8b9BKugZGzfhfeQQteqz2cd-jlCAoxT-hm8uH0EgOgLY1HERMbhw3rBH6u8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgWGi2nrkK29-HZnRsEBwi9I1g5Id3cVvHExadPDdISuXoppw37-GEt_vIC_-VJvVy3KzfkgJ9pNqbQGaBIAlXCxJTOSjhswcjzZaQ54Qa8F0A759DEokhngaavvngcUoOqEoSWG4tdeISFVdtG3JiQNvjzinZ6TsZVw-hLntW_wgJ7-AcwPpXCy99Ihr2WaxFhe2gFPWQ9nYpsU2oCI6xfdiAnjSXH7mATPzuy0PyS-m3e54ORQcV5wtzrJXh8kZzd95zdZBbBM7cNO_fOpgzTi6pGCh_wuSlLgGRyWbWFc9XN-aj5dWENbJy_SFLfXdJGcFNQOa2l3GQvOFXzq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0G0SyujWNqYlVKFSb9AiIWOeMs7XCjoCWiCv-7plAUZZ-P-lp3qhp0G-TS04ES6RLACUySbHGPtL2iobTK9G4i_JmAkVUDM2nalGP_1kCXdC_mRaIrhAnDWpJBvPKkG3bBJo0hHpF_Hot3ID9iYSaoKPwurMzY3M-b5OGXdFQwsstc9FuMtNedzORPd42Va89NhLAzzzeWMbt0wraBZctbzNKFAZZvBb-WVcxiG4e-vVSTp7st74fHuCzsHwGRvXaOlf9pJy5wriCkJNOe1dBYRJQAqcoJTefCavhUlHJ4FLSFMtSJ_2NhzbwDQTD4290e0lUzoOKsT3IUEvTDlfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjQ7PCnJhOx8TwfAaZ3_6l7Yzh7TpgmQxNncHSckGd5COzf-k0kJxAhoUWNYR-zESKlKjJSY5X0gDx2fVTedNrMGW3GvVAQwLdFSOsZadl-zxQqzA4MGw0Nj_At0720cjrW9lnGuGfbyL2gdWPH5WJGsW7jumKNtOUyd5GbQJt08g7BCA6xtSDyXkbpJVDL_V0xakglW5lQo_vvI_Fc2GX6VyOyu-Hnm0G3kq-gKFvQ-ObUkRiOM6U4bMhNeNsMA-EEys-j-cJqpiK6nMJJrq-lfXDwz5IulQzt1q4gPtf09FZNsAkgaa8_nSIgARPtYpGIpJ_m7jh8NXU_rDrcIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/br13uVRb3SFFeaGRcVhImJ6MagK1i9dmvBlr5w6pajhUDnQJeBCT4C1rm-10f-ymKcQFs_rbUhIYGRopzlXA5e6oOiawDuKy5qOxV3SSiiBb0WX0GCqt24rUnc1NQ_-oixv8On3ye3IxGy8gvqxN38DSg_Wl-EN7gjlzAxR6UFAieA55VmzsS9v0_-qYkJPbATAzyehaEOm3jwG7jqtz-b0regKy2dGIz3DnPgdf6A4nXRXjvCFcBM0RpziWWh_w21qc365VmWcIk_ItjcYen-Rfn8eBLOhIcQI0C0gKkKzUgjR6BNDUI953ANlvFCqbmLg635rzFYTZvzh4CwDXkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vc58TESrB19SXcX22JDquOHN5mr9e_0xTLmO0xEXhTPl3TnBv1myvM6tgehgUnhwnlZGiU90S17cFbu1-OXRZTwWf976s8_DCPRxkI3Q8kGPVyKb9_j99wGZ8GUSFzSmcRZh01ncbbOnupLZa0KJeFn0j4tWo7p4V2y2A2QbvWqcAm8edlWTtVZWi1-A8BbVOcM8pVRJUfvEBr1hi-H4ZOeCGc6capNagQgs0B8sVhD9Yk_eonMNR7JVGB8wq-4QrV8cWL-6xOkt0Fd8GQn95qtKuC5mOATMQXbDgsG5z_ENMAg8nMXpTujiLsKB9_5u6anIQOFay2xcjUAHLT4gng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vc58TESrB19SXcX22JDquOHN5mr9e_0xTLmO0xEXhTPl3TnBv1myvM6tgehgUnhwnlZGiU90S17cFbu1-OXRZTwWf976s8_DCPRxkI3Q8kGPVyKb9_j99wGZ8GUSFzSmcRZh01ncbbOnupLZa0KJeFn0j4tWo7p4V2y2A2QbvWqcAm8edlWTtVZWi1-A8BbVOcM8pVRJUfvEBr1hi-H4ZOeCGc6capNagQgs0B8sVhD9Yk_eonMNR7JVGB8wq-4QrV8cWL-6xOkt0Fd8GQn95qtKuC5mOATMQXbDgsG5z_ENMAg8nMXpTujiLsKB9_5u6anIQOFay2xcjUAHLT4gng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=PiI8ZQuEEAK2i9vZU-fq2Xgl-fwbNl2gJ4Y6DOCciyteSi78Al2wTuI9ae-gD7hdjnqYzETj5R4f3EKVDLCIA5jaF9r_khJPXc_ZT5H3TrZRaVSyLA2g31dxb8SEX1oemsSktgzBSWRBrwW50DxZMzCcMMKU4CK54-Jlu-tnfKVUluSVw1Xdh8mS82DW7Aog5qqtU-DDsFr4FPcKp85J1LEdOSgT503CxllIQNDkTeDAg7JfGrPcHX9krOP31e4fkMZ7sysf64zbye2YxC05CdaPeOtQY2S98Bv3R_v3ESCARUVj7PB2xsjsS98LPgMFHyqPDfrXQbTvvqsu-pZdDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=PiI8ZQuEEAK2i9vZU-fq2Xgl-fwbNl2gJ4Y6DOCciyteSi78Al2wTuI9ae-gD7hdjnqYzETj5R4f3EKVDLCIA5jaF9r_khJPXc_ZT5H3TrZRaVSyLA2g31dxb8SEX1oemsSktgzBSWRBrwW50DxZMzCcMMKU4CK54-Jlu-tnfKVUluSVw1Xdh8mS82DW7Aog5qqtU-DDsFr4FPcKp85J1LEdOSgT503CxllIQNDkTeDAg7JfGrPcHX9krOP31e4fkMZ7sysf64zbye2YxC05CdaPeOtQY2S98Bv3R_v3ESCARUVj7PB2xsjsS98LPgMFHyqPDfrXQbTvvqsu-pZdDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyuMfEoyjh4YhZ12nVvdV111H8UmLpS8iCUCtRqDOJwS_1Qinnqcm4bG5he5AnQlbfbtGzPCALD1FdeXOk8eQhZasIhjaie4CC2fvCU9vojt3ooVEPjG8kz34Cm38Ji-ADDHhQ6Ixq3E2Yw-kegJ7unfHss2nQQIJUokBUkV7IJXrIJPlUb39jfwEoDT-84xkHf_heTCxjDRfEcKvlv2r8otI7cIx1kqJJszRtyaR5Re7l553B5YPXkpmQfZHfgr1276M4ZqkIs8jwvi1fI8LDKGiA8tEin1LZqW8QeJ-44QMIww0Y6k3fcPEZAMG8kKr3vzlSnqTFtqk7QCULi3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FIkgZ9ZunmeloGe6y83qCP-9VUn7z1rkgZ0lbEJzfG9hjMlyVLC-wGj-04ppx7eHYWbPvc29s4bQ2MnGvOuwNmARTsxsoJ2md2d4xJ5sYnOxhdaev8ZXzfyEvtgWb3REaRcIgaJEhxE6gS9teDDKjeRrl1thLrH_QAz1DhZjKIdrlKSWsq743HNaHDcL_I62xZLLtARCa1CTrLRxFhIcr-PwzQvORJuFfJ7bs1ijgLeJHSFwE2XXnJWEnxHmgJ7-iuzYbKqwsBK_hB0jRfZcEfSMNNVe57JjerAw3P4a0iDi00SDVm37rsnGxXcFJD_0Gzg25i0UaswisrzhrZQ06w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=ShnVZxmkxslZ7zchFV8EPMj9a9SnU0v4KUhUwnH5nTdsKZYC8kkHLZCvB9KLYGRTASA6MWBzftw7bOwLMN4FE_wM0urwAWhm2NUZWYiAqwdcj-NdZCwg4JKsfHgJ2bsZTErSD5tGK--LIXK-KuzV7qqj6t_QZQ-mpXw2wfi0StijRC__MsLL4aakLf5Wr5Dj0BH2lButzaddTZrSwq8EeDxVslO56PH-RYzIrkjfclSbNrYjFgjNGdzF4Ij5vvHZ5L7GlwzGvHMt8ptm58e0x1gDSAnOCc6HGgxtecSDkSd6UqC6SLMkBRYM6K5umD7nEs_fNYY-2FILHQxtiWwDGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=ShnVZxmkxslZ7zchFV8EPMj9a9SnU0v4KUhUwnH5nTdsKZYC8kkHLZCvB9KLYGRTASA6MWBzftw7bOwLMN4FE_wM0urwAWhm2NUZWYiAqwdcj-NdZCwg4JKsfHgJ2bsZTErSD5tGK--LIXK-KuzV7qqj6t_QZQ-mpXw2wfi0StijRC__MsLL4aakLf5Wr5Dj0BH2lButzaddTZrSwq8EeDxVslO56PH-RYzIrkjfclSbNrYjFgjNGdzF4Ij5vvHZ5L7GlwzGvHMt8ptm58e0x1gDSAnOCc6HGgxtecSDkSd6UqC6SLMkBRYM6K5umD7nEs_fNYY-2FILHQxtiWwDGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdrH6xB_gqYgkfyLri2Q06i4ZrBZGEotYDgRW1Mm-Uc4X6FMSYJxcXaq25WTJLkE2crRPSs9q98LscVWxT0YmotlGNGzdbCOEkvpY0dtSjxvDen2OtdRVC35YoEs0O8VqRcFS-ZGrhsQiXymeh6uvJFwKAozVIWZHUc5WIsxfzbBd7SB6UWOiF-zRdu8qpD5iOgiiW7yO-s7Par1ObFAVK25d1GmtzJ9h7HXqTxKWsszyvKlVwRbSLiZgH7oxGeM1bj4-WJMTFAZkoSa395L0p4DtXNZPQnjfc9qjoFbWM7eH2fLFKQFwXpKMDToL6JXydlsLJTFCBmiciweuA9Ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=ArlWFxNXxVjEnhavQYEoN-Q9D2oMnfYyS2WDALbGbX_haTgMalWMUDCSdJUaKQ119XjABTlSjNcCjebCuNQp9ZY0rgki3fN0OxbgYmBsYreIB1PmMaNHUnIP1-Ren77XAbUPLJSIuCDGBmErM7K1IhDTv5CtnPloI3fssz8--T524aS6tkIRj07Q3T5xYGuloCxsmEY6BB1BV-yddTW8JDwzUOagctcPZOgL1a3tMVDfW6ly257UdGp5MjabBsTvGraHkUOr8jhSAwo-CO0Ilr8Vbbzyh7tfSH3KVpGkGdKDWo7WkxDUYT6mLhnxJMwDyIteGtwdJaRTOmq8oOYC1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=ArlWFxNXxVjEnhavQYEoN-Q9D2oMnfYyS2WDALbGbX_haTgMalWMUDCSdJUaKQ119XjABTlSjNcCjebCuNQp9ZY0rgki3fN0OxbgYmBsYreIB1PmMaNHUnIP1-Ren77XAbUPLJSIuCDGBmErM7K1IhDTv5CtnPloI3fssz8--T524aS6tkIRj07Q3T5xYGuloCxsmEY6BB1BV-yddTW8JDwzUOagctcPZOgL1a3tMVDfW6ly257UdGp5MjabBsTvGraHkUOr8jhSAwo-CO0Ilr8Vbbzyh7tfSH3KVpGkGdKDWo7WkxDUYT6mLhnxJMwDyIteGtwdJaRTOmq8oOYC1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=Zqr4-eRj4ymKOiRde33m1o68wSDwgdEc3F5iJJ6yrn0VpAxfYcwY8Ltk5NNmkW_0JDIGtm2TE7HgsMe0VpXVY5qSLplrKZWErZsCKx8hV0f8onhB3iJ3ekqiV_6WfcDppzIZW3SHrPyVizDkRcnRQaMuquxAeRS3vFGQitDEOX-4NOiv8iF1RXpy-wltrbpbJ6ALH3gMkj-fNa-p-v78ffq2AEFTvGKmuHnK46EbAQy3-dKdusRrA9ZaUV1qUv6JSgSIyPRzOhStgNcSFQq5p_8D3niPV3LpTZUAQ9HIFx-P1NxA4fm6p9k9GSXVwtYQHu6G7p0Ic5ZUZaGV2sFGDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=Zqr4-eRj4ymKOiRde33m1o68wSDwgdEc3F5iJJ6yrn0VpAxfYcwY8Ltk5NNmkW_0JDIGtm2TE7HgsMe0VpXVY5qSLplrKZWErZsCKx8hV0f8onhB3iJ3ekqiV_6WfcDppzIZW3SHrPyVizDkRcnRQaMuquxAeRS3vFGQitDEOX-4NOiv8iF1RXpy-wltrbpbJ6ALH3gMkj-fNa-p-v78ffq2AEFTvGKmuHnK46EbAQy3-dKdusRrA9ZaUV1qUv6JSgSIyPRzOhStgNcSFQq5p_8D3niPV3LpTZUAQ9HIFx-P1NxA4fm6p9k9GSXVwtYQHu6G7p0Ic5ZUZaGV2sFGDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=jWX1Jsb7pCmgK4JnM55NqnVzt-dsz1ddpM-QzDjQsLCGjy4x-Krsr5HRB7GWf_9nuJrs5dQV--HePzEJ9os9mN5_kRSNy84Mirfde_oj2EAiRSljZq6LdXCR1zDducpPfuu8Dzms3ee4CRjSMQgSR5Oz29u_3Xtdm-VAhS2b2ciL55R08BNBR7rd6XUM3sVtbn-3G-jgfsscBrYr7xHCZAk8Qka5ctlmixFXwoLrFrsdkfjZI7KNZ3TNBZHNBVeq--CC033Ay4zf0-O_u0ROSTiHGUXwT11_3_GOhCd5GlHrkRjQPmuyLrlWiQ9tpTy638w6tgHN7iY5MxSOlPfxyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=jWX1Jsb7pCmgK4JnM55NqnVzt-dsz1ddpM-QzDjQsLCGjy4x-Krsr5HRB7GWf_9nuJrs5dQV--HePzEJ9os9mN5_kRSNy84Mirfde_oj2EAiRSljZq6LdXCR1zDducpPfuu8Dzms3ee4CRjSMQgSR5Oz29u_3Xtdm-VAhS2b2ciL55R08BNBR7rd6XUM3sVtbn-3G-jgfsscBrYr7xHCZAk8Qka5ctlmixFXwoLrFrsdkfjZI7KNZ3TNBZHNBVeq--CC033Ay4zf0-O_u0ROSTiHGUXwT11_3_GOhCd5GlHrkRjQPmuyLrlWiQ9tpTy638w6tgHN7iY5MxSOlPfxyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=GcATjkTHWLzO84Gfi3K3Dt2voFEE4PCpG2POPx-PeQU6Mw52sjD_xZAaD3OiXcWdaTwMFMjJtskF6uFWLMnnpd4WtMOObwNTBX52w5N0MRaM38huqpqAkHg1nXWGFY_9R3wQXkMhasqlKn9aJGtpLjcroR55-uBkAvmKYnbqnzLIulLNHy2V_icFgowOQrijWpzqlBjWZAneCo0mKeAj4ReG4JL0UWw9GOTC7wOvi8jB8onYRc8W6iEKS5amKfHG03Os9a2lG51TvKF2Zv_oz79Q1p8eSVNpp9TD4FWVzqKSmHqamVqnizX_saugT81rykbMGEMcrI8sNciN3PfkVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=GcATjkTHWLzO84Gfi3K3Dt2voFEE4PCpG2POPx-PeQU6Mw52sjD_xZAaD3OiXcWdaTwMFMjJtskF6uFWLMnnpd4WtMOObwNTBX52w5N0MRaM38huqpqAkHg1nXWGFY_9R3wQXkMhasqlKn9aJGtpLjcroR55-uBkAvmKYnbqnzLIulLNHy2V_icFgowOQrijWpzqlBjWZAneCo0mKeAj4ReG4JL0UWw9GOTC7wOvi8jB8onYRc8W6iEKS5amKfHG03Os9a2lG51TvKF2Zv_oz79Q1p8eSVNpp9TD4FWVzqKSmHqamVqnizX_saugT81rykbMGEMcrI8sNciN3PfkVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=F2k60dPHu70mMMDW5S7DVwZaAw17gbU63hFr4LMZm8SGbKh7PtT5IIwb_sls8qm5zYG-YZoiSYL_3ervA18RHCdV1do6WjIgghtq9Ox_ViZMIWi-7AETPHil6IRn_DxgH_ZJP3HxQiQkJOgtmCh9AYUmARndV9AU3f1SU0fFVWlOruFQSh2n_LeSE8ZBo74Ihz2fYT01A_ML9Avo0BnKsgd8Kbc3bk0iecWvDjoWIN_CEiahlC6Yci3tbXS_QryPcQNqn3N8oorTXbFyCjB48M2tGCfo1cL32PFHcYsP9vdc0qpxUGThLGnmTneNrK8M5zx6ybgkgkj4WpxnNivmkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=F2k60dPHu70mMMDW5S7DVwZaAw17gbU63hFr4LMZm8SGbKh7PtT5IIwb_sls8qm5zYG-YZoiSYL_3ervA18RHCdV1do6WjIgghtq9Ox_ViZMIWi-7AETPHil6IRn_DxgH_ZJP3HxQiQkJOgtmCh9AYUmARndV9AU3f1SU0fFVWlOruFQSh2n_LeSE8ZBo74Ihz2fYT01A_ML9Avo0BnKsgd8Kbc3bk0iecWvDjoWIN_CEiahlC6Yci3tbXS_QryPcQNqn3N8oorTXbFyCjB48M2tGCfo1cL32PFHcYsP9vdc0qpxUGThLGnmTneNrK8M5zx6ybgkgkj4WpxnNivmkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=ELYcQu2VL5UhUlzev7sJm40K0I87t2kDrfAYSryPQ80m0f_EJKkzxm9cuAAh4nsI_GAYMUSKuP7nh9bxb5fTRhV7iwEEGI-uyA5rw1k_24GD_dC7jFTFT_JC50g7SHPvqDe6ijFIApBwos7omi3lt14ilRZadWYbzxWzqF19jukot_VoCGhC3Nu2BOJgnSZ2GvnusDmOIo7sOJgltqUJ6DhWrT6tdjHitqJyLYrEmBGfmipXB5WxY_b0TjFB5bzdcfTsuh9RiPrQIr0XYlGa3q7JhhyEH9IqLUvQwDBrmQ5QmUJ18uMfjlZQobjYtj6sDzAwlwCbG3TLtOxZkO6KFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=ELYcQu2VL5UhUlzev7sJm40K0I87t2kDrfAYSryPQ80m0f_EJKkzxm9cuAAh4nsI_GAYMUSKuP7nh9bxb5fTRhV7iwEEGI-uyA5rw1k_24GD_dC7jFTFT_JC50g7SHPvqDe6ijFIApBwos7omi3lt14ilRZadWYbzxWzqF19jukot_VoCGhC3Nu2BOJgnSZ2GvnusDmOIo7sOJgltqUJ6DhWrT6tdjHitqJyLYrEmBGfmipXB5WxY_b0TjFB5bzdcfTsuh9RiPrQIr0XYlGa3q7JhhyEH9IqLUvQwDBrmQ5QmUJ18uMfjlZQobjYtj6sDzAwlwCbG3TLtOxZkO6KFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcVqwYXM1YhmwVHcq4DMl_K4AYycZAsrA4SFMZmj2fPhRwgzQt19RmVcZfahFytYXQ7oHomHJOtzkmde7RedgtuyecPUI24VcUs07GyDB4mnzbFSB0NzR4dm3QzjqJGL-RzqNIjjMcVlWBCNL_AiNdLSTmKDjcx3ikZO5dkjUObn0XJfJrJQhWJG1Ruf-zCBSM3pwLvhDevLODFwNc5pm2EwKEy-GCXw1zoyXH5RVGdC2Isif0jtOjEDgca8bkoHCrlG0g6OCnmD0vl1jhzdRfLBNHDK0k3elmfEx44fFORdHC859DZ55hDNtTQP4u94GyQfzArZQI60KGQGKXDs8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=WLRbW-iCLjh4Ji3WorRMIeJ0SEk61zZeIDB_QIzo2sPsng2_7-7HAZDOdSo_G0YKa9FL34KOdjcgA4vfWLxoGUnwFnkS1rXNAQCUgoWKUWqjJc1Qmqfhx12nO1yb2-R-hJ_jhiggZxg2bBwsHNCIuQYxMBD-tfmpvSiDpCPyGgyEylVvUi0CwNGiGJQpHnXu7kyaeYhVruqeihtDIyNGztqNYQ3oQE6C-LxJvaJHUZVQo_EbY0l0IdfgueEGVIvxqNFi-F_DGyCnZ9LA3HTjnBFD9mBPStiGZap3EnxCbucb62uvy4xGKEt1tjh-aqy0HeE2f2s58DWcgtJyT-vtnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=WLRbW-iCLjh4Ji3WorRMIeJ0SEk61zZeIDB_QIzo2sPsng2_7-7HAZDOdSo_G0YKa9FL34KOdjcgA4vfWLxoGUnwFnkS1rXNAQCUgoWKUWqjJc1Qmqfhx12nO1yb2-R-hJ_jhiggZxg2bBwsHNCIuQYxMBD-tfmpvSiDpCPyGgyEylVvUi0CwNGiGJQpHnXu7kyaeYhVruqeihtDIyNGztqNYQ3oQE6C-LxJvaJHUZVQo_EbY0l0IdfgueEGVIvxqNFi-F_DGyCnZ9LA3HTjnBFD9mBPStiGZap3EnxCbucb62uvy4xGKEt1tjh-aqy0HeE2f2s58DWcgtJyT-vtnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSYrQv8zOogfujMv2vOpOLaVGO2buoKQtnqbP3-Rr988Gy9rqkJgvnMF0IltNf7M4MhE7AJhjPyr4JU5CgWEf-r6BJPF9SlqcrtWsnLaG9U1f9U3wsP7xYKwC4Vt36KjU57TPI7wyoxy7y-A_XiiAT5W_wHJnP_OvDk7s01U6kE6cJhaBCdcQulPg3kcKvfldp3hQ0G6DhNAT4GPax0lOL_xNnpil1G1EifLVldP4JRi3bYBTPwPAZb7DbtIfL2YR4u6G-CGFLdf-H5ezrgvtP9y40aUA3xXyoRIeOxrTDAD3GJRh7F8kLHAhuOOjOVPTKDOPgWgaHvroqvjqoqbgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=pAJgCtsRjZZnaMdGBP6PzRlo0ZgEaEvmXUtghAmMgPuaiPZks38dG4B-ueJdBm5hOCOlmzziId6DUHly9nw5amjWru_re90ZWEECVZZ27VJv9omxDMe49Rd5E8bVX6wNvyCleCfVZCRmqrKgpGCcJioOzhgJvSTzF91y-8EETBdqjDAaLSE5Jm9d9lxE7o0aFhgqHOZM0A3UzEPOwbMkJPfn9cJjbZeD566OO2EBJOP6fB9DlZY-oBkP5llK7bodvPYfKuVWn1L5Hd5BOIfXoc6CDlUdGzey1rjvZE4wlqlEIRJ07l5Q0q1K3Y-aRxFoWN5Hqz87BQAV8k-cgPQ-OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=pAJgCtsRjZZnaMdGBP6PzRlo0ZgEaEvmXUtghAmMgPuaiPZks38dG4B-ueJdBm5hOCOlmzziId6DUHly9nw5amjWru_re90ZWEECVZZ27VJv9omxDMe49Rd5E8bVX6wNvyCleCfVZCRmqrKgpGCcJioOzhgJvSTzF91y-8EETBdqjDAaLSE5Jm9d9lxE7o0aFhgqHOZM0A3UzEPOwbMkJPfn9cJjbZeD566OO2EBJOP6fB9DlZY-oBkP5llK7bodvPYfKuVWn1L5Hd5BOIfXoc6CDlUdGzey1rjvZE4wlqlEIRJ07l5Q0q1K3Y-aRxFoWN5Hqz87BQAV8k-cgPQ-OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwmXLcIyIaZBremhTjYuUaKEv5VDgVMDve6lIuYTdJHEv2JcU7oT5ri_SqG3a2hnFEva4UhzXTjlLTLSutaa_l-E2TarZ51Dv1rxA4ezxOn-yLvSuAvxcm48VcJIA0JFL_-1AzD4TkNXJ-FypoTRQBRBc3TAeCkDQ4oDw93A9s0MxJ9r3qWMlKzeLj3-aa31xGaPXzZ5SxVf-w_EQVE63uxFU81TginSpaevJEGPqs4eGO_Y0R5-S0l9WFst_1-djj77z6H33Zdu1Dz2Y2MSQ8LVWH5REaNfdEIpqi1V2LzZSgjG5H8EuXUgThlzI5F7HCiTY9FK0E6TVW7iC_TeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiaH8qQhZesYT_dgLMhDCm1O80jzRXpjcJFxDaEf0ZhxfL7sbAzVE4Oc7HL3HG-Hvzpq_j8TihfQN9a-R8khG0CMuzXS445NSQ4VynDlS_Arsc0UAaKTh-RHB3a_C7QEzpw-mPa9JxI5yD4HqHjBjAriWylHJSHMWGeYgEot3E011SoltrZ3oPOLIS7gak5KOULKqh-9RtxqdAYKEOsAfbTvaMUs_umf4sknA8484DX1ckg5jvfZL7Sq3Sk91u-UOs7F1XeWXbduBN0RRAIf0N_IWdn1yAyvfZh7E-mw5M6ga39l1As6jRolsS3eo4hs4iWgALvOORzkUFrN64dBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zeo5rJNsfQAAh8PE2xD-QNd4yCystltD3p01fG5TVCSOwuvhiAMnZliPREWD5bdqmaj3m9OGQAmP1VlEwmHWpXxbW31Xt0WixgQFceHttroQfm6HrMLMcxWstMsKb00U27Tv82gkYVP9HW_K4eK2b9Ubr1KpkWwHdeQCEx09scoOCl9tyzFS_jdjnOZ915q6h-mDZ8GahNdrouZ8bjF3rtyBxxcw4kOJEcyejMLaDpQBMSoILh2f2Ga8X_pGZkjsaIJNotrYTkY78_YkNZPWyulEKuip0O1hsMdr_2aqrpCd7lhljdtLuPFHHaoRmKcUs_BDjkUYckVepNceZc0xuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL_4AQCGqOjPiUZZOO278902db1eTHMwI9P4B-MjUPY5qOQqGpIx1og1bvrtLOsQ-oG4ICbi51rJUmJnZfkP3Tz63t95hfATbOvnRLAlKDyP7B0T7b7bCr_byHgcmhzOpA4FYj7-_tHesboqiGGnG2KJMRtIwkcLO_OBzW5ZwuZea46LqZa58hW-ScqsodehxuF35VVPZkNvgI448QJdKOMM7h7G3nCNQY-L-a23grurYgihVrVBhdRqgqO8l1_QASdlIV58RWe6wY_NOQt2964P4nn0Ngkx80zPQCT90B46latJSCDDU3hih5n0Outhx2pXoln4gawZWpYTLFPNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j27xXG-0NY2XW-LQewZvdlTCMdtKGGkHRwsWOmTJvaNiRHeR_p1cmVeRiI9DIjk6zRrWh8IRKm6uZd0zNigy6HXq2d2lnLQM5BQKkgOoqWwzmO7kWMHIIzEyR79_aqr5LOSIPCIqDppf_U3E7UrrbwY7i-oPDn88zqZV5xCCuc39XUU3bn9GhKrGt2kgI4IMxP--PWxWVS1Im68F1MBQn185GywZAL8bYQtG3yIpfgSs_tlqWHOs78JQth64ABwo1stAktKRBqyoi2uQxXLz6JVdDaqjDWxsfo6-TPpYaguAkLRK0lhimhrdgLArLtbwLo4SK3prPKU0rtmpQtW3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsIWB2S826ZyRHV3hB0bB3RBwLw5cUNWjDtgUk0USzSFMJjvVWHEtZVBHPHoOQ1yL4vWMGxh_aE1OnPgTNcbfqP38eMqzMKi5-CXY71VvmypYQRFsTCLaD0y9EeO0YbIdHpPJsHrlehxHtky1f8tOerqu7fJGw7kg6SuGfR_9FIgeROJJFj--pHSPXs3ocfSpuBc7VD9-GAvUWgVsKdomnIZ3NVRQp6EXW8AbItimm1ooZviNxEhWYW2DOSSKjhUMwCw9yKZu3zBMLbQSElLydORJKDN02AR3x8_25DbQuX2_st_Jl3DyZu_dOs4FtBYOn4_ikuMf4K76msphGkAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ax08N9eB5bOUzJhEg_I_g4XnBZ_7pUODbykGU1vEuYI_zIolS6BfzXaMeTy6-6wMW_daOu_GpWB2YNFyDjT3AzKVcM5duDdOXwv5fhX-brQcAVMP-TPe6foAHYONoc2ZcHK4tEpjIQwJxz9BU38gc8JZ5la9XDtCoPyTnSjVhWoyZ7foqEQe4BXJSCH3uqSpybVwNvo2SZtXeQCn-0KhcBampNbJX2jgHvULy5uenrhD6g5L0KmMJkR6UgotrcdjmzGetYWR44xWcjTB8iIWzrAzRFBp5xXrfIXLfvVT81OhDG1iWebvCcPtD3ATVd1ZBBrhKkrhWGNlrnryCbXcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBeHmPLPeVhdqa3At7CrxF3xMdeO3IhCCvKdbviTRPmg8BGvCTCLBiMmP5aGqpbn--1WFU7t2tidhhIGaaTq00G8CyFwiyfVIZ2Tn1zTdHales8WyIrklHXIkBhF3evIA4ChUJcRLAVYhlJgD84D1UYKXppW4yeqgeqLgIbre3LdjoYRnftu-TZqzbWSvH4c688UeeDB6xha2BcDAK7_wLB07diBdzjH13u7SGPz_cPqXsvXUnGG8rYFV4WiLkMCmkCUsl2przhbAMHPIQJY4-LSJN365jAFTkT7P8eFHCP4_NEeGRZOdBql-5hDx1Ym4Nrfbicb9f2iGonqoSCZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=JUNX0Z6kyrl3k7zfTjObb7vLuF2FAFZPkPbJsHcOLInRSBtMeuBUTdK-nSkKfRah-hv37girBioN1em-H1fAC9cpEueJw622FI6iAn2nay3vOZThzpO-pIHQE0ltsG2X1D-xSYgPbBZ362Ivly9vfH_F5wJ5Bpmak6PePtvzrdE_W7IpGxaLXFpNzoB5N36SrYxMJTlvCvTwHVesSl8HJPDMkjOAvqeyWEoEBHGgoX6Yw4Aa__FNaV3eAa3jxgxVx_j55BcoyI9WEdHnrr_-zTltCo4podPXHeKqPCivmmT3tkdxDT3D6O-73jZi450oJbUuBDhomcgMD-oIMUH3Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=JUNX0Z6kyrl3k7zfTjObb7vLuF2FAFZPkPbJsHcOLInRSBtMeuBUTdK-nSkKfRah-hv37girBioN1em-H1fAC9cpEueJw622FI6iAn2nay3vOZThzpO-pIHQE0ltsG2X1D-xSYgPbBZ362Ivly9vfH_F5wJ5Bpmak6PePtvzrdE_W7IpGxaLXFpNzoB5N36SrYxMJTlvCvTwHVesSl8HJPDMkjOAvqeyWEoEBHGgoX6Yw4Aa__FNaV3eAa3jxgxVx_j55BcoyI9WEdHnrr_-zTltCo4podPXHeKqPCivmmT3tkdxDT3D6O-73jZi450oJbUuBDhomcgMD-oIMUH3Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX2idcJfnvEl_0P1Ei28dXYVSAjBBhNO2gmoKYpC0x9Jvhjt1dhfSkq6BWYqD25BXn4-zlwc9mXaFpXWsU2oAHjFYsHDkXWrtaCRMqjsFGrzYPZnUh0wkSQ1jHUiTdPj_6QIu5KlBj86dNX8jOWdLPU9r7sh9bFTdSSkbbFFMA1X83AEbWXEpg382egCsOTMw9sPxegmaka0d6YDIo2I3tA1AogkDyYDlS3BfvWj49YHDrCpXvkqvR28dHVYI1c_p2_oShErLQ_3yxh-0zF9nd-_758bKD3V8jzp7VfgO_gxx6c2cMyzqST2UIeeaOZeWR5Js9Rj8Bz-kSNsPEI2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDrEt9ziGjMucqF36EMgjxGiCEmyup0TdIo0E4ViwDwwp49mx53Vlb5o8-Cif_LGvT_ZfHwQEUczXP4I8iy1cewGbsIGMRBGmwqaZI-Y9KPP7vAew7io8STDMfNzernACWWJNflBbZUk2WeSfCoM8eok3MdowJcfS8F_xny-nRXmZ2J8dn4SkhHUaqYWnSk6oN3DYzRLPuZ4oOV7t44f_tSQeH9_HD65gVWbB9WJu9sQFeto5XoJ7y_i0rfp0exedTecVl92qxzfdsPow7XudgppPlKKpyjpyhkcHGQFPI_zwAhPqCR903l3QEQFthgpohnmS7WwC1X1iHfr4qTobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-pVul4GFPwB1sO2-BqQeNAYJ70S_jE0i0y625gqA-NStcAi_L5Jp_BwKi__ZZmhxQiMOdceJZDD1-J46J_4k0wc_Q7WMfUSv8A8pdVTMXIMvcDgbKTXRM62VJOR03jsP-2rNucWswQGPKAExSzJrO191MLjmVZl_kpAt-gRSNbR-OfKAjweoQmjDYqs3IhUiR13r19se9Cl10x6Lhq_qNgsq9P5v2oplwHbhToRF8XAg0ZNU1TUPWgX7cXY_OjUNc9VfyTwH1GWiufqSR7DgxOrODAoWPTbdJ-pP315iH4c6z_O42MLiFF-f-rpGtsfvj37qAuZIdtEo2H9TGCkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_r7PV58Yn2Y64Ndf5ifN97N0nQe7qBWKIJHfB7ppIvddYKNvfaCTnFz_-No8Gl-o50JF9fyROxF2bQxqWPNze0i2__XO3G7q7AKeKT7yYqsiHX_HQrtgq2AJ9zJ20xC1a7nn65Poq34eW3z8wscFP5nqPv_2FgiYjuFY1hOi1RktBy5chWkWz-JzjOPMTmw39ks4xVpIopjMeRUdbO8APBanYWp7Xkw7UASM9urE-jkZ81C4WYY2MslK0h_HSEU_Awq8fpE7Ht8UbvCLWBYtkrSlg7ww6ZvQvZQ7kjjPlxyp4k6t2Dy9hiRlshHVsLiCW74-z4z2vhhnipfXlWkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvwDTODZjrdmThs1gBWwl-7ZXJ1IARJwwl0Hjejv3y7m76ZWMy8hxq0fOBNOLA-QgbLB17tciDQ_tuDawaHqVrVJ4KyKXmsBfPiQP0LBVTu4zUVTeFyWBF_isAUZ3aN_UGlS73hZG1R3YbhSEQ6h7WPuDvi09RjFKZsZ2FgVFqezEcspdRnHG8WGoRV5h8W6i46vye3vzeODw_rrlAPSU3ZLKG5JKS7854i4Apx4f8NyEPLnmYq9GcJxGBSCPIXsfqDE6F6BbiZCFX4e9wL7u4t6T9JFGJXCrVQ1W8e3gyeeiYyLZrjHmtLSZpVI_3UXB9itq5JpqE6l58sJDcDKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=exLdRcmigjk9ylki1B1yhSYMmecS3IjkWNTGrSSMsJrJpUXXK-QjdUNb58Q8bVFxHcTgmNAPVcHcEljAPgQcsx9nCnjFISv-qABEd-Rua71_fVAxmROh_zVKSsDc0xVvasuvWFAfmmpFLe8xC1xLdWlM_5S2ivPqgGAQe6IpQWV29iINQC2onMwZ7cEgYy5dTY4VGhvDeRFg6W48Lb_ljUkNOvv1VNN4HoAQKYP4DuAvGG-Gk9uJlt3u3HuUplJSL0L9BbdD_3z4Abk5SmjjXISAcQDoDYAIY8uCk3NOIHcVXxXnrCUmZVClU1PFdsiT70dJWPu5vW7CnmhbxVFOVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=exLdRcmigjk9ylki1B1yhSYMmecS3IjkWNTGrSSMsJrJpUXXK-QjdUNb58Q8bVFxHcTgmNAPVcHcEljAPgQcsx9nCnjFISv-qABEd-Rua71_fVAxmROh_zVKSsDc0xVvasuvWFAfmmpFLe8xC1xLdWlM_5S2ivPqgGAQe6IpQWV29iINQC2onMwZ7cEgYy5dTY4VGhvDeRFg6W48Lb_ljUkNOvv1VNN4HoAQKYP4DuAvGG-Gk9uJlt3u3HuUplJSL0L9BbdD_3z4Abk5SmjjXISAcQDoDYAIY8uCk3NOIHcVXxXnrCUmZVClU1PFdsiT70dJWPu5vW7CnmhbxVFOVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X13Vc_JzgsCKHBS900xFIlR-_yMEhFZxmfLmPq0SKayRdxhYDfLoU5uHhdUac_a5vKKXdX2qCZwVS1DBiub6wHXiHPSv-sZL-7lDuAZnmPLWuDX1vKDkEdN4fwM_fzaqCGkUPnp6cScuRrYW5xVlUHBobyR7vshB1qVM_DdLrrfRW9vUURjK_2Svs7K2lSUcstruNXvZgnees4ZWekRCnCOURH6x6PaKJ-zdSyWNgbXRWzb6NNf94dJRLuhiW3vegV2bEvc975jhLL4JqdKnsDQSYl8yLdkpkcdiYhMEDy6t6h4ASqRG6yGQUf-Cj9SAwUucANv04GUjNmeI11Iwcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=TjCMzFykXa-7ysX2iCUzwmkbChgGrraoN4GBDBSglNUW68cJ5dCFsPG9EFWuExBXElyC3_Gwb9Xrp6fDTUJlE50kFuH6ajO69Atox7Yt6hLT_SU6klcuuSO8iKiNhOKEUnn-eIo5UcZyNVM0GDgUnNYFbAzDHNp97-vJQTWv6ozrqTKf18Amoxcd5dDonHs2MP1HtPWll0b4d3jniuowdYC3q72JrfrgCA8ulwK60w7J0FbiKdvxA9Ejrp1EG9VRKTJPLOTjg93LBK4jdO755DbAB7oIn2gpHGJA2Rf_su4tFhg0p0_B2NoZ-0a2DGogJwCf5LX15bx_cZyP7tMaeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=TjCMzFykXa-7ysX2iCUzwmkbChgGrraoN4GBDBSglNUW68cJ5dCFsPG9EFWuExBXElyC3_Gwb9Xrp6fDTUJlE50kFuH6ajO69Atox7Yt6hLT_SU6klcuuSO8iKiNhOKEUnn-eIo5UcZyNVM0GDgUnNYFbAzDHNp97-vJQTWv6ozrqTKf18Amoxcd5dDonHs2MP1HtPWll0b4d3jniuowdYC3q72JrfrgCA8ulwK60w7J0FbiKdvxA9Ejrp1EG9VRKTJPLOTjg93LBK4jdO755DbAB7oIn2gpHGJA2Rf_su4tFhg0p0_B2NoZ-0a2DGogJwCf5LX15bx_cZyP7tMaeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=cBjR_H83TAFEod_PfFZwRNyF9z-76C1uUbM53OuOmsEUg_gxbAg884dxJcYKoSlPDUttEOrX13k6kcfXb6mUggYGMkW7Mun101qZKixtqjDAVNGPsCAPs88HjLp0MyOOOH9il0wfOCe3kYFXc1jB4e_MmjtxGsZxx2oUoKQwu57MH8X578_HqNyhlOUoaPEBXldVCAVkH49XajUrWrkLqurQF2DkWQHuYFOFQvhg5Vh346vDPt4vtAskerU_XIRUom6ZFRcSix3j5EfTaV0meMIpJXXyUqV6hGd4Q530foWEA8DwGv1SQkX252hpRGaz-7JdAPRel13CWd46JG3xLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=cBjR_H83TAFEod_PfFZwRNyF9z-76C1uUbM53OuOmsEUg_gxbAg884dxJcYKoSlPDUttEOrX13k6kcfXb6mUggYGMkW7Mun101qZKixtqjDAVNGPsCAPs88HjLp0MyOOOH9il0wfOCe3kYFXc1jB4e_MmjtxGsZxx2oUoKQwu57MH8X578_HqNyhlOUoaPEBXldVCAVkH49XajUrWrkLqurQF2DkWQHuYFOFQvhg5Vh346vDPt4vtAskerU_XIRUom6ZFRcSix3j5EfTaV0meMIpJXXyUqV6hGd4Q530foWEA8DwGv1SQkX252hpRGaz-7JdAPRel13CWd46JG3xLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6j_pxYWZU_MgoLeShWv5L98GhD_lzusgLGn9NAyfTjoKT1AHcodxDCHY9ikn-4t-1Ikz0HsyYCkg9puX0De4OYo0KaJC8fWCiU1PE_VeB2oKIDGm0uj0wnos1tTX31BPvzLG6uS0w6k4G2qyxj0RQBMg0SkYjJDfQZfGjYyHds-jNIEgNjvldKqWXEO6s-50QJ8MbDbV_sGnKh961-TGrAOwtid4LZ2bC8uHo1ZL8ZWByJKjrRjvTrJ6IbJuycyXHU-VUzuexCpmXhWWCOb376Y2xPHNavaOOa8ReH-uJnGjnlRgUpjJphSosrHDE79xTbVZ564WtXPFigUKi02Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrVyQ509vHpo-TTg3G5kSW1ExMccTsXamUFAUQXhO5j1V6ubl2jqcZX2zGvB61-Mp0ZjNtbqdu-qrERKI67ihLLN11hKt4JBmbGC7Njfi74xb5AeYn6VwVrFWeVOPurrjNte4G47GosPImtyio8u32c-lHBDogP9WHQ6kOmUy9kou9NKP4E3UhKTqjqrgbdKBonYLCZMR6FmqigE-qeTjBZl44e05dXalMrX5d86ZKabsKRXsMCim-sn9Yzx3MzIdq-XQP7U8sdUJjVVkKPkcD0mRosYf7Y8ic31Vd7lfm5GmJZs7BWcU8IRIj-SKcgaoVXoqKlQKVDvT_JpaF4H0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=mT1EbEy6D-B90a3bAyVwA_XC_JH8C3TIfXR3PwAqkemwLqfX9-SxE5TuYqiBCn2_z6wyUX9vRA9TNhxzv2PUiTH0-LkDFSvSzfCxQot0jTzx_VI_V_H4QWp9XcXPOZCdjnnDQ8v2IGQXpxgldtdEMDLNiNjKuZ8LYtvwEKHpm4qClHhouHLIfYEr-kUfxvNL1caTls9SmTR8Fz2g9Rlbdy5g-C7YpbAPAJc_rBiEQj7gepfDULeIe3K1uF5vet1xk08IZ6oQ9Y_rBxIojytO36qxoV-bXdYawp8PE0qXQ_VIUb1_2e1ZsgWuYmUl7qavcwpjcWHJjMoA6yf8D10VeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=mT1EbEy6D-B90a3bAyVwA_XC_JH8C3TIfXR3PwAqkemwLqfX9-SxE5TuYqiBCn2_z6wyUX9vRA9TNhxzv2PUiTH0-LkDFSvSzfCxQot0jTzx_VI_V_H4QWp9XcXPOZCdjnnDQ8v2IGQXpxgldtdEMDLNiNjKuZ8LYtvwEKHpm4qClHhouHLIfYEr-kUfxvNL1caTls9SmTR8Fz2g9Rlbdy5g-C7YpbAPAJc_rBiEQj7gepfDULeIe3K1uF5vet1xk08IZ6oQ9Y_rBxIojytO36qxoV-bXdYawp8PE0qXQ_VIUb1_2e1ZsgWuYmUl7qavcwpjcWHJjMoA6yf8D10VeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVmz_mo3UKuDPL_FUzv3AptIbnTgIG7Jt82MOMBBzplhLfousCMydZcfHsftOZ3Rms2Zs94JvlwCDF0B2jNRByxPrTXmBm-XbcSOGOHK5ipO1GcDqpUiusWIQZEqiTSTIhwNyPY0C_5_Te53f_YG-gUj4XrMc_nwo3BjPIOrM3OSgxiZpgtxadJRGYJ3qRxyu_YGZAzP5ujopLdIr601vj1isOXvPDfy1rC88gHzHyzkNjbSX7AppCaKlWCDSQ7j44UupZ13ZAekLTsuMQP5IKRDjMMZScsK3MPNR2b9eLLMC7pnSOKR1VkzAjDHcHn6fb70Za70oyngxkTxvPEmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUFbVzP0l1HjwNsHEyXnx8I2GsLlh6aacbaAs5ZQYgKJBm1S70nQjzEn3ZNrYuXs7oQ6a3o7ExLcSxyFJHhAPuw8EOrUsbuGbSEk5PmmW-JB69la5IbgSM3TomQQK1M5OhPh6hyuwHoyoVahy0dnAUEln1VMlnZIOi_sYFw0Vg2PXPwOUsRIAZitfy9thGIhcwIdyMAtrkC_hN62hsAcDSWar35RIV4j_bj5Iz_2in0vjTS0gUiy7THrwpLC4UwKymsvtSK9IGkJSB7fG1d5z75IlBYSldRX7fLh7oCbz8PtmnwoMzvWD3CwGcZKyO42jKEmjI_b9i3bCmp4IPkkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgVUGbl5CQcVADfESL8-7zYVHhJE3P4ZBKbLyDDYb9qVrc_rJE-licg_RcURV0CAgLxwAf1lNChlyn4UTiMya-LVMjVOrAPHAyaM6KJAmbcHWh9GuQRFnsGyKuxJDYyWAuwK4zh24AC5gdOMm2c11ytXX6WQVO3GZI5fNDobSUj7pZfYlflGUDm_3oBpeN-D17yrIJJD0bsAc710u132KQz9Z_aaz_hsrJYqGhIFZV2KaBhZLhqlQQ1PYmTxSbEUi3eEOj8wmqI6bN5IO2lUwhNN4xB9OewnUuI_IeMudLkr7iOJJEGqJTRzKIZTRB7EnveftdNc6am9EuyZ1f5FaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQP4zx4Y5wRn6vHWXCtEIGIA3JYZay-NUcJv84HfFG6rcZuxgYjyWRv17jPLRVMtkP6IOrNMBRhVv8opAtrMPpmkQwu3zRnk0VnOw4Pe87028jDVSvPJ8eixRmTrUApO9_e98Nrmj7N8xsTxQWFSGFauYUmUEPz3GUnzdAjP0G9lu_ukOsozbLYmXf1Rhf53eCDd-yPJYx61JTSP7XFSk8DeI30ScWyYeLeZnZw0quOcHeYMXDWtJ3e0RFCY9prqrY_GGwZe3hbCwF_9OrxPASaWIIcIE4w1W8ud8qRa8sP5KvxTuLimDkeFFAbul0EbgqAw3Fyyq58zaUbFGazTNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLfYBhcDVu5317Ys1OYQGh9aq6IQDM_4Jc046A0XRwFY8sscN6i6YByB07Klf9eMl6yHcXjWxQDE2bKg5vbAjMPw0RfSA0AQqtDRxMEKDKvIcLBK9OtvORgOKTkYw6PXqNUpFwU4jdJhbrCMCaVQKsH9Uf3dRhPYbBFMacYjHlWBlaGgU06Ivtb6U18MSk-7sVqohd4AbHmQPCCgxUORtXITiOYKi1_lA7ghZ1sqmf62yUV8YhhJnk-JPAD7-wki3FfqPZm_mKMx2CATrTUWNTRwJhpMy_Mx7A9MFqPQdtZ_QipoWrcuBkt_UMnhYIRuNuNYiboiDw2MBmJfjqOXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP1pgi8Yu5KB1Ku-Hx84Q5rWvIm03VutI2WNlKenbTc2kypAWxHOhtx_SHaKlD1L9a5IHPCDkGcjJzWiwvFaeZs3NqWy4g_EPC1gXrAvvHJs8wP-OTk0YV2Ue8b-jcS_YTYczWLmTxAa8P8vgem5ROIxuJ2x1R98bLuqKer6TrIXS16qNQJuZkTDjS5AV03uu1t737xDJQgEkr7YWPp1FHQiXuyFMqapOz1QtTMl9FFeySBJ3H0Y4l6t5O8lf6VXXXKuxz5VVWvL0kWP7Sv3YTDzQyizqxjBcfyhrshvwC9BSiuHOW8eBVc1wVj4F7oCU1hLAKp5da8iDhgKtrrNfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRN4oAGpPnowuobufDQoSHkzM5rR9pDnQ6jDUkqsLNSe7bWiFnjyWY6PV2PbTdE0A9OEc8lWIHkXTrzq0VMBux2vekjizTMKdVm0y-mj1pM6JcA8MxuWR2kuV-89ggygFNxr0aADQUYK32czcIcIUM7ctUL9smXvJYSlt2FR1nCzdmGrZ1NL4QZhaOavTzXuCrfq6ogCNG5JcE98W5kuoeIFoVgF3lTxrg4SS0am3wkuQhgF8BaQa8bH4cHIzirxW5BXiNejSDLFYamI32PgQpRuBwZlI-r0M4UpwoNaB7fE9gU4CfmMnvTGoQKBCupupczQPFs4CD9xRGPa4Hz-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ9AYu1HqE8R6qb_ZUXRISLbTDQqBBHD4iHFkfQP7xXda1O8deaZC5_9X4yEoHLI1iAV5T8CIQdhsgZ2pN0qjJNvN8-BDktL1oAE9B0Zl2gASCi4lpTCamONppAJ6yG7l8wp6jr64SaZQJg0MwNbhL0dNsnQD6R761LhjEk4nM40THJ6Ln2exUxQIg5wWCnkkVLv_vDBymMw1rukXclpm1srwttMnyeW-rSOlXniSdTuLVWaPXvZmE1tVq67T_5AFGwJGxkZv-Sa3pZvfVEi976MVCUEwwB-m6TNlKFQynHhdaD1KkyrKjlqEUgBnrWGd9rqJKiKeMvNPrm2KzkM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isRb_6biarL-2Y9jjng0bDfZ1ygXoLyu4k8JeOUYArAG31vrEBKagW3KhsujgrdiGzwnCN0KPOq_sZpdZu4kODSZZtoWsTFpElApItI9nkyj4Njc1nQA9sivJJ61JttxG21EnE0xGXCYqZYJFmM_V820lekT1BOsRjMVz1NFglFYpTyi6jCXiJ90aT2U07dJrYlR-8RSNl4IHSGjjNP_pO0CyB-zAg1EzDibtGQIpRm5XBrwGE1TMPtZe6PcFtQ_KajSW4SDpt2Y3U3SpJSOZVyDJAwcbUexgmxLYouYgKLJkKJwyOXM9UFzZsx6Y7jiBglh25G_GYfba2d9aFQfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLtpulcSRKQKcW2qROZfTo-tvwcWY2vi3UykzBHOvWqRw8QcXD7dou2Zr-25d_NBJHz8gWwy-lJshokic-UWBy14gXWCyePj7XUpdDNcCBUqzxnRrg6a3otu81--BA-fBEpZT9pDbquBwHJqoQnWO28inAlB4tNZ2YQmqi_yCTqN6GbgI0xpniAxBgFkqNjquqlf_I06qwPP7vOat_czCiLtNIajhQlFkyYdkLE_ILP0V8Phj2HWfYSiC7N5S7l7ap6C7OlvSbmbuiqh_0nm_uSSvu2NfMqNEneYm-zyPKPqc_msDjqylgTVJGLZCcObEuHptZ8uvoAYd3kRXPK3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vql8ojCl7z2Y3HuXcd_Mer6ONxIZ0ly8LR4xJ6kBqPNHsY0QaS2swRsH1PJrHo1aJ-ZZY69Dz4XE7MjDflHSZgBvtIfHDvAboNV8QXI18MlrZEcsqQzXFn1o8CncD4h4C7Y4dNUnrD1JQMa1ZBUktR7nZcwEXInrUOSyUVqZbiAAv5qMc6VizqD6YoR94JZ7VUIIjZNbgSOzLFjDNHMEfplzE3z9hADtVtGd4qqhsOO6j2vY32ecdC6K35_kPdo0c05ZmF2n1D6JjlUF0NXcxdFVRBcJ4toUqbmIgce11Ga90zTIzU53qlwQvrUqmrDObHL5JQ12KIi5ysvTMXikkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=l1_ZJ1DfIgUdiO8Z0agoqVrBXufk0Pa2VvUyD_djP5mxuHbszqZaCD2IK0lDYfO7UnyUpmn7S_10EF9J1MwIlyPZ4u5Yf3MMIl55OuwArr8ilXGVQ8H4FpTyBY9qredE9rrZ-wbyCroU44VW_a-u2DrYrh4r3tsz3_i0MgGk5Z5NupeUtX_XcXY9u8KGM9VUWTWbKxVKaTdJ59lXzEb25c_zH1fgJMbGO36T4Hz0ya0Ywv4OrdXHaG91HbO99D_4Ys2cJt5Pv_MxNSYytB2muh9yp_6KFkwfNls2xw1cpUPVrQ7lpCvaGKKGzd2QdPqSauOSGWHmfylarpoYEib_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=l1_ZJ1DfIgUdiO8Z0agoqVrBXufk0Pa2VvUyD_djP5mxuHbszqZaCD2IK0lDYfO7UnyUpmn7S_10EF9J1MwIlyPZ4u5Yf3MMIl55OuwArr8ilXGVQ8H4FpTyBY9qredE9rrZ-wbyCroU44VW_a-u2DrYrh4r3tsz3_i0MgGk5Z5NupeUtX_XcXY9u8KGM9VUWTWbKxVKaTdJ59lXzEb25c_zH1fgJMbGO36T4Hz0ya0Ywv4OrdXHaG91HbO99D_4Ys2cJt5Pv_MxNSYytB2muh9yp_6KFkwfNls2xw1cpUPVrQ7lpCvaGKKGzd2QdPqSauOSGWHmfylarpoYEib_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=Q15H_caM83WMp7Pt-KRWvSXqVcCI4pcet2VVhE5UkSmEOBJXlGymqyQjH_pOCWNn1bY-1TRfjZsD334N-kdDsDTS7pUiIMoNkIFdz1myv0Xi0VEYz_twTMkFjz9zZYMxbPxsmncioP473VX60i19aM5qo3bOeOuR-whBwUqdYYl2Wb51h8XE0ydxybdIQeuaRlwCXZACgQLWqTmccMlM-YK_dr8g2nH0lh66LDmKBiqiWXJDmhEM_gzk0jZhZo0TSiHsfCUvSMFSXVqCe8HOQfTxRcru4Xdiv6KURwMC8-4t3KueUMAgLpJHCbKg22H545rUDsFGTh0CqWMqMhjXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=Q15H_caM83WMp7Pt-KRWvSXqVcCI4pcet2VVhE5UkSmEOBJXlGymqyQjH_pOCWNn1bY-1TRfjZsD334N-kdDsDTS7pUiIMoNkIFdz1myv0Xi0VEYz_twTMkFjz9zZYMxbPxsmncioP473VX60i19aM5qo3bOeOuR-whBwUqdYYl2Wb51h8XE0ydxybdIQeuaRlwCXZACgQLWqTmccMlM-YK_dr8g2nH0lh66LDmKBiqiWXJDmhEM_gzk0jZhZo0TSiHsfCUvSMFSXVqCe8HOQfTxRcru4Xdiv6KURwMC8-4t3KueUMAgLpJHCbKg22H545rUDsFGTh0CqWMqMhjXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tyb2TtMzAz1lRHD5RdYI8GrLNqF4Yku6J_xep7-AN-jy6898izGIK_lbJDqGnHQ5nS0jDz8kjvYGX3n_TaWo5J6S-WE794j1H6FGlypI_-s0aBvbuW_3CmUetuO6VG_mkREyoWQ5uKccscxiNbVOWG4HzsKKPq2IAWAmnbtzCdvoscln6_XdaP4tv0ULwyhgzx0cV7iCmeY_YxvHDINdgepchpI3mk2oEFzysnMMbKTQ17OyNTZc3HB77Q1dmcsadbSvsDu6h2FzH-b9ibxu8eUu6bi016kAeO20yrd3w_oeytIpw-KrtCFa5tzt0s_nqETakYv4zdGmYOw9SfM5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
