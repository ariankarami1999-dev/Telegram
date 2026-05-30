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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 03:24:19</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PchmgV0Pk6aXuN-ZVDCAogkduEMHwTwXliejClCzGghinkGUAXjyhSy-DTRnCWiYnsh5jOpD7E56-IYzfXjgD7M9VqTDJZQ_j4tPcotU37oskAIhWG3KpQFC-AV_tQk4auHK7__luKoEB2OTQgjRwCKcZTOLSSXcq2E8H5k9_tBhPh8NpbjvPfPdd0DSOH43SdE9Kx_QoJiCOcUlgvo8fOvI1QJ8_tWFh-txixRu6UQVRLxBfWamWQfbz8-U5Vhz5DNgAGhbO3VoRikaRV3GP05EAS12GQsEKsXQSd5P1LWwoO6ERld2gEjvMW2na8sBEcl0Jm6UB1gZ6LcETELg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf9AuUzZBGWHMWBK4_uVpkf08-DEgdMiEzGgZhpePCuCbzow1i4w_ZObT7Py8tunmAJ_m_QCBwa-2HjPrHg-AHCpkHGivXGSW1mdiy5u8myaZWBwgRQZ3sGy8ZPfoU2_JwA0Y8uc-Vi8DPXQDbbV4frshqi-A2wrhNRiR5k4mpprbR9jZJbh-AR6SWb_Nu_xSE3j243EGVPHv4bDjHh59QsEqLPt02_dNhhawFIpVj7qc-yHbiueSeccComI4jziZaxB9eQZFPboDkdspvgVUr3Fptc9b8G3YKhryHo0mUgzOpVGP-Jz-XFWbZsQ2e5BvkqlAzHjTclgNrmZOOwJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzg5-__0tS-5U3UwOwBgufgPSdyfkzsv5AVHjc7jLEHds9zGXbWDfeQsSPxM4qZOZO_sWOLbGvzgEyDBjTVbo7uUYMnL_2W5glcn6MucycUSKBQReRCdoyYXbzRRn2SuughsHqGXeqK--FQBto_StiqRAPkR_bsMO6qcdxkPHrCaMFzi6nQ99uYXLINnvp5fcJE1aT7QCcbz5d2awLdVh-0R04uCWNrnJqEqRl2hvDqlUKlc-24dsD4ffXO_6KVsuBPPc84A-iXxYNYYDgEDi-66X8b9BKugZGzfhfeQQteqz2cd-jlCAoxT-hm8uH0EgOgLY1HERMbhw3rBH6u8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdrH6xB_gqYgkfyLri2Q06i4ZrBZGEotYDgRW1Mm-Uc4X6FMSYJxcXaq25WTJLkE2crRPSs9q98LscVWxT0YmotlGNGzdbCOEkvpY0dtSjxvDen2OtdRVC35YoEs0O8VqRcFS-ZGrhsQiXymeh6uvJFwKAozVIWZHUc5WIsxfzbBd7SB6UWOiF-zRdu8qpD5iOgiiW7yO-s7Par1ObFAVK25d1GmtzJ9h7HXqTxKWsszyvKlVwRbSLiZgH7oxGeM1bj4-WJMTFAZkoSa395L0p4DtXNZPQnjfc9qjoFbWM7eH2fLFKQFwXpKMDToL6JXydlsLJTFCBmiciweuA9Ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=QbghC_d66Cbvz2YuO8ClF2rtsXFZ6MYyLeaU2DD5oT8ylRPkuxzMVcnSXCFZbL3rPFmRO7ByS1vtvCDc94nF2SIBR4A3LBNRfXfnq89ZOhXosDoVP0Keo00XUBjD69QfdgJefmNs241WWXX-63zOgHgYlSMbz-JQ2k3GWDFZ0GURBCg6lyRL1Htw4RahE8jeoXt3LzhaZXE1IkGggmkMaPih1rgoJA-ke1SyIOOdrVT1aHls0nhUGrhLvkMy6z0vszFHe4rPe_diuYpBDtP6HgmiO-wOvWdlYndePWfdy7ga7yWh894n0JH64To6YKOwno-pfTPdW1cobTzFeTKm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=QbghC_d66Cbvz2YuO8ClF2rtsXFZ6MYyLeaU2DD5oT8ylRPkuxzMVcnSXCFZbL3rPFmRO7ByS1vtvCDc94nF2SIBR4A3LBNRfXfnq89ZOhXosDoVP0Keo00XUBjD69QfdgJefmNs241WWXX-63zOgHgYlSMbz-JQ2k3GWDFZ0GURBCg6lyRL1Htw4RahE8jeoXt3LzhaZXE1IkGggmkMaPih1rgoJA-ke1SyIOOdrVT1aHls0nhUGrhLvkMy6z0vszFHe4rPe_diuYpBDtP6HgmiO-wOvWdlYndePWfdy7ga7yWh894n0JH64To6YKOwno-pfTPdW1cobTzFeTKm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=bw9b0DOCa7v05b9nT7iXzCOWzeMTfCvYhMiIL_fDHOM93Wyt3oee9Pay9atz1dn6LWLaL7lcsyrmpUWq0KajYlaiDDgvSXQsP45B99H37iB6HNZ2wo7wgZwfFnQJSySwU_-dyyYxHwIw7fKeZOri1WAc3br7y2yaCvFOrPdTsHjpFsaLHghH_rsANYkrUUHUPo9-38mK_t-zBQjRt12-ccp1QJivKeOHW4UibX1R2CjMFGqNTpcpUGv1RGxwf4lydkz1AWi3JjKFsGdHB_nl1odW0P8bsq5hYh4OCukwEppRcN0eC4Qm-cvy8PX4VKXC422iZqWV-sMkP5vhgNCkYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=bw9b0DOCa7v05b9nT7iXzCOWzeMTfCvYhMiIL_fDHOM93Wyt3oee9Pay9atz1dn6LWLaL7lcsyrmpUWq0KajYlaiDDgvSXQsP45B99H37iB6HNZ2wo7wgZwfFnQJSySwU_-dyyYxHwIw7fKeZOri1WAc3br7y2yaCvFOrPdTsHjpFsaLHghH_rsANYkrUUHUPo9-38mK_t-zBQjRt12-ccp1QJivKeOHW4UibX1R2CjMFGqNTpcpUGv1RGxwf4lydkz1AWi3JjKFsGdHB_nl1odW0P8bsq5hYh4OCukwEppRcN0eC4Qm-cvy8PX4VKXC422iZqWV-sMkP5vhgNCkYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=dd3FSY3PT-RblpJGwXK_7OO8PPFj5my8WhNQdpAZwFDNUVgVe_OQ-S8G-vt9OFTVwALVjAb1Uma5Le2Ucv6JtfjrP8d9cOiyhBbtoalzpxodNc7xd8ka_AIPn051jU_S7VYuAdRZiRliW9S-uJtIdV_k0M0ILHNw_jXsRCpfV8MigyEmAbNJcnHSae9YBp1WWbwnrw40Kk0GDAqnbcKiIbDxR2C-KTa_lJL1I9cH4rLWCpEoFNxw8qrpyjvG5Lulu5buAfbS7VbRkoJadS9J6B84uWs86ZCTsXqybRR2SX1JiBhvHvKts4u1C-YnpvHTnMBt-CYjUOdNJeJUxuKzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=dd3FSY3PT-RblpJGwXK_7OO8PPFj5my8WhNQdpAZwFDNUVgVe_OQ-S8G-vt9OFTVwALVjAb1Uma5Le2Ucv6JtfjrP8d9cOiyhBbtoalzpxodNc7xd8ka_AIPn051jU_S7VYuAdRZiRliW9S-uJtIdV_k0M0ILHNw_jXsRCpfV8MigyEmAbNJcnHSae9YBp1WWbwnrw40Kk0GDAqnbcKiIbDxR2C-KTa_lJL1I9cH4rLWCpEoFNxw8qrpyjvG5Lulu5buAfbS7VbRkoJadS9J6B84uWs86ZCTsXqybRR2SX1JiBhvHvKts4u1C-YnpvHTnMBt-CYjUOdNJeJUxuKzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=ZCgv-mz8YIiCrMwn9honZbuAWk-JeBgZQoEZLauOP-oCVE5JkgEF_cLbOh_jianBlf5ckpgIfNNqnMD1jtQIppqoNNg-gKv1bW746fpoS4nLlKBtgFywDgr9Xkc7gSjKPqY-lntq1SRT0XhulDJSw2FhAO4vxxJveS28OtkN6En7D5fecRb66IRUyShdgvbbSoY8IB0NVuMCXFz6ujTRSNLqgT_GtLtsNobFtVY7JUsRpgVXTIgyeMHdjgZ09-b7KDX6UK0BKrAwT-iF1J0T2qf66FJVCS8GXr6EEz4PccYg7P4Z_p8Pm5QIv7GaOxoeU9lMU_FeE0m2PdLvR_GRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=ZCgv-mz8YIiCrMwn9honZbuAWk-JeBgZQoEZLauOP-oCVE5JkgEF_cLbOh_jianBlf5ckpgIfNNqnMD1jtQIppqoNNg-gKv1bW746fpoS4nLlKBtgFywDgr9Xkc7gSjKPqY-lntq1SRT0XhulDJSw2FhAO4vxxJveS28OtkN6En7D5fecRb66IRUyShdgvbbSoY8IB0NVuMCXFz6ujTRSNLqgT_GtLtsNobFtVY7JUsRpgVXTIgyeMHdjgZ09-b7KDX6UK0BKrAwT-iF1J0T2qf66FJVCS8GXr6EEz4PccYg7P4Z_p8Pm5QIv7GaOxoeU9lMU_FeE0m2PdLvR_GRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=h7j5EotWdBAzQwl3xLXDL1X4rUhM5ha2Uy-Qh_fheBiZN7_dIp_ZyIBIYZO4M6NCqh7Rsv3aJpIKIeh8QGVvSjhNhZhAKjbvi2NP05VocL8MXU5C2w6CizVkVyVfX5jAK3WC4dcmq6zhWScdeHbtcBmSsGZGGMP3v9BeX2XMo0MQmEDFY9oK4F8cjCzvdLLr2bxn7sR02T6SClEbTR5tmuv7QJ1sADDktHoDb75D9EVr2nxUdK2rbYVyrJn_Bpzhvx694pD4wUk0kgPH-n4IuYgvx6bIHS76xF1J0NwBTrTU-7RTD-4TOEZYVTS5uPUof6kmJq2wxf1Cdtcvba5X5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=h7j5EotWdBAzQwl3xLXDL1X4rUhM5ha2Uy-Qh_fheBiZN7_dIp_ZyIBIYZO4M6NCqh7Rsv3aJpIKIeh8QGVvSjhNhZhAKjbvi2NP05VocL8MXU5C2w6CizVkVyVfX5jAK3WC4dcmq6zhWScdeHbtcBmSsGZGGMP3v9BeX2XMo0MQmEDFY9oK4F8cjCzvdLLr2bxn7sR02T6SClEbTR5tmuv7QJ1sADDktHoDb75D9EVr2nxUdK2rbYVyrJn_Bpzhvx694pD4wUk0kgPH-n4IuYgvx6bIHS76xF1J0NwBTrTU-7RTD-4TOEZYVTS5uPUof6kmJq2wxf1Cdtcvba5X5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAJwoKgnaEk6U_BvBMM_hwCj7gcPyQ5T6tS9rmah5hfgcR1zfH5AcFWl-Icy7bSN44gQ8Qim7Vz05YdqAEP782ifd9RIwa8Yz7rzjyAxjw5hzlk3WfrbLYANhIbIZCrXW5gqrrpLqc4i12XQWPVhtz8NBy0EUBstuLB898WTTkBtlblROi-xrk8Y8OaLAD7B8w2kg_q3cPGrXVdrWYxGl830Awjr_04NDXIfH7VxMezU59838DOGX7mkV-SDwV6dQNcBMWFSDxNffkAwx2Hb0xFJfa4RN7OCNvcn1jlP_6qq6of5VpX2Lr52RwejZz4ZJ9I-MqlOqwJmrrhCkxctIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=aR7VetrwNmUkv4TtZGKArsJeFvpjuzzmmmyAttZjjf8Lg6_LGQuQniaRsIzsscvd5beBPSOgRhGiEOKN6yD0QzGjrx0oNb0uGnF-6B3p3_z0dF5CPnrXsQhwQ5BNRoUNvoDtZjK6eQAmhePeRFXLu2cbregZHHONd_c2rrpuGF_JFG7Q0nh4m8MqC3e65s0O0Ao-TXemzsAm44dInBP3xUZ2dyO3MUU2TYLjHZD1AgXonQ6sR7kyfSr-sgqxKmwWrCDCEYs06-afzxf-MiMzLTdWuN5ZIbz_DfEWo9i1G5RP8AFv7MZFmk6yUUatwIkakwmP84nXSWbeGI7tIcu66w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=aR7VetrwNmUkv4TtZGKArsJeFvpjuzzmmmyAttZjjf8Lg6_LGQuQniaRsIzsscvd5beBPSOgRhGiEOKN6yD0QzGjrx0oNb0uGnF-6B3p3_z0dF5CPnrXsQhwQ5BNRoUNvoDtZjK6eQAmhePeRFXLu2cbregZHHONd_c2rrpuGF_JFG7Q0nh4m8MqC3e65s0O0Ao-TXemzsAm44dInBP3xUZ2dyO3MUU2TYLjHZD1AgXonQ6sR7kyfSr-sgqxKmwWrCDCEYs06-afzxf-MiMzLTdWuN5ZIbz_DfEWo9i1G5RP8AFv7MZFmk6yUUatwIkakwmP84nXSWbeGI7tIcu66w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofMQBE87J_K2B-bHAaPsrKaDXnQztmaYUsjRXkThWJWp5K2dXmyJz2NmWNdAys1N4gEDQNdnRdXKbHQKVtM0Plfmh_c40wHRlFwJHdTAn8yI0KTPC2aXsk3gb9QAhg1wQGcd-G7AR5Tdqzueu34x5hQ4m5cOzHHCHgEkmn3J0ImDKs2fB0xMVQZwBWSMWfGT0lNqiR87un8_9UmvTrvtcLo-yKjvJMvIwz2PP8PHlRBLvomFE1dET9rjT6oiZCn_oNadxOF1fGM6_eAOFcDHplvIz8_FWkJeTAYFujXQiqci5pe0kG_EQ_WE-Co5fwf11gKpo8uL2gsDzE7GcBQA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=ioJXI72xDrSnm9rjl4VAq8M4tGAhc7W9Ragg0_-JSJc1JP8acO27e5cAdXM_OmbodTpsivkVvq6xP5bhxmkdzgiU0CQHYLvkpQBOlvi_l067bNzT4fgwVAu0ppVw7iphWzKuj1ucwrjo9-G8qnqX-SzF7MhUeFnAdax6009kKCRmIVIIvD-CrLialPk3lJUwSPjMRTP7dvQzvDP0MQjDbC0BXAPv8oMsc0F6pGvZCT2S0_c-z3_05FtneLejS_RDO1RIa4OE9ESWCalkEhHOtGRCh0_OlI8gkwkWuu4zQDGJaBTCmhjBZ1XX5HolyeB7YlSCafERVWrNDzpA9q39_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=ioJXI72xDrSnm9rjl4VAq8M4tGAhc7W9Ragg0_-JSJc1JP8acO27e5cAdXM_OmbodTpsivkVvq6xP5bhxmkdzgiU0CQHYLvkpQBOlvi_l067bNzT4fgwVAu0ppVw7iphWzKuj1ucwrjo9-G8qnqX-SzF7MhUeFnAdax6009kKCRmIVIIvD-CrLialPk3lJUwSPjMRTP7dvQzvDP0MQjDbC0BXAPv8oMsc0F6pGvZCT2S0_c-z3_05FtneLejS_RDO1RIa4OE9ESWCalkEhHOtGRCh0_OlI8gkwkWuu4zQDGJaBTCmhjBZ1XX5HolyeB7YlSCafERVWrNDzpA9q39_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgNjeJSx7k2XgHajBdZmin5jtCQHBLmYx7p8u4AQ_NYYWN3So6lzryluS55yImxIzIPG-8gLDul78baUdT4Eoy614FR5zfxE59Qn-LDwpmwTsQXJoVKHs85P8Q5TSzSuZLjT8xxzDZgfdyzPCUCIAovVjn6NiUumheeBYsHUe0XvepkPK0I9J7iD0-NKBY0QKv2eit49BSUr1Qq8qfASz8AlwpMsCrMe913NHAwEkWwDhmiJx2sRYGhhScoMoBH0GPstaueEEtqRN_lRkFsSkJCxt2BNGJDN8bx2B0Cq05nXBHQjJFXxc7iVtMg_pYCuZxd-PNlfiJsFzljNn5B_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiaH8qQhZesYT_dgLMhDCm1O80jzRXpjcJFxDaEf0ZhxfL7sbAzVE4Oc7HL3HG-Hvzpq_j8TihfQN9a-R8khG0CMuzXS445NSQ4VynDlS_Arsc0UAaKTh-RHB3a_C7QEzpw-mPa9JxI5yD4HqHjBjAriWylHJSHMWGeYgEot3E011SoltrZ3oPOLIS7gak5KOULKqh-9RtxqdAYKEOsAfbTvaMUs_umf4sknA8484DX1ckg5jvfZL7Sq3Sk91u-UOs7F1XeWXbduBN0RRAIf0N_IWdn1yAyvfZh7E-mw5M6ga39l1As6jRolsS3eo4hs4iWgALvOORzkUFrN64dBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY5WlDE8ZAphSnBFvBCjEauj2Pq3Htc_W_rkWtsphOi518NPFp50DcAfSd__ZaaEhdNTgTILkrZs_aLy5tRFEyqQgXk5wqdepBUL5vI9LIsCnzqgMoQABt5GxHbO7JcVUB4n2RPhIZlBpH4iS2qrjXcz0Oe8ChEfRBP_C_DXpG-fYkYwykq5HjJZYXMJaNjXycC4f4bFmetgVOUVsLMhPf3ibGPnYDaGM1DjZwPUZjHUx2eiiMMUcjzNz6eM1KGZR3nRgW_A5Yte3Jg10EsAts0njQGoJLTDuVmrZ5rJGsKACBj_hFaCwVbYCvc1zpfd7XuX1lME_bu48SkUT3iKuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QToX9hq-vg9mDWBbHZPMSjEFQ4-CmiUpqC0lz2RzSPyINrRjm1Ajy9C4swfaGKaNEeCPm3oyIWVLmE_UVbwbPXfGk38si83_uTzYFoaiG6wtooBVzXqDYuLO0225lMePnftMWUsXSsFkdxJiyBHjPr1sOMTePOI0YTm9AhH0px_grUD1C5LsvH2FEtZgNSxlAsBVBSw63C8Gx1a00ZhXWXXq9G7EaZGi5DAY8lNK2RGTgV0UIl0qp-CDaAOfEuJ2kDlciXDI9xGdThQNOr6t-XyXZgQUuLdH7BCQRBK6jZWI2lX-x_IVo1rPJAUxQpScTnfm-pU3WkLhwm-rr7zvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j27xXG-0NY2XW-LQewZvdlTCMdtKGGkHRwsWOmTJvaNiRHeR_p1cmVeRiI9DIjk6zRrWh8IRKm6uZd0zNigy6HXq2d2lnLQM5BQKkgOoqWwzmO7kWMHIIzEyR79_aqr5LOSIPCIqDppf_U3E7UrrbwY7i-oPDn88zqZV5xCCuc39XUU3bn9GhKrGt2kgI4IMxP--PWxWVS1Im68F1MBQn185GywZAL8bYQtG3yIpfgSs_tlqWHOs78JQth64ABwo1stAktKRBqyoi2uQxXLz6JVdDaqjDWxsfo6-TPpYaguAkLRK0lhimhrdgLArLtbwLo4SK3prPKU0rtmpQtW3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsIWB2S826ZyRHV3hB0bB3RBwLw5cUNWjDtgUk0USzSFMJjvVWHEtZVBHPHoOQ1yL4vWMGxh_aE1OnPgTNcbfqP38eMqzMKi5-CXY71VvmypYQRFsTCLaD0y9EeO0YbIdHpPJsHrlehxHtky1f8tOerqu7fJGw7kg6SuGfR_9FIgeROJJFj--pHSPXs3ocfSpuBc7VD9-GAvUWgVsKdomnIZ3NVRQp6EXW8AbItimm1ooZviNxEhWYW2DOSSKjhUMwCw9yKZu3zBMLbQSElLydORJKDN02AR3x8_25DbQuX2_st_Jl3DyZu_dOs4FtBYOn4_ikuMf4K76msphGkAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPrqs_gLya85AQWP33iK0Tln9Rf2oCfIrk-pZAs1rPe27sdBlzuSQbq_NZmLfIY62k6Z1lYOMDEP9_jID5jrN51rUqkwVkthNN8ZLNDFAOVQq75byQnm5X7x3zb-59DYsUCqRsVnZkclrXUOyY5rUh5ewUd87_ld04mKRyGED9pq974fb3ujnQInMbMy_rykSb4b2XT9D-ybbHjUmwHo4BEVxHcMXjWIyZfqui27RoR-u3heZEjNKHBMh-nPUCkjebwEtGjL3rOEpDtjWlO-_y-4vcvKoqrMKUGrlvn1ZKCCx5ixXBJqm25AZOW3JP9N44oeyPNOOpDH2uhWQR21CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCk1M36j1B3CbucV26k4eNxyxoxR3UbupqtDh5qGlVhj4Hg_tup_R9qWrfd3XaNrPQ1rsG-Bf-TRws1KDfAwvLaIa5d1EuRfalgy6-3SmHrrEi505kr7vmnMB1BLZqtnlc0S-jinuKXQg95t850jdhx94zd6ywA1mFD2zVHX7Zby-Woh5tTiKdxLXE6lMmxm_SlCDyzxUXyulU9Td1CiLN2UaGoUNrdjx2U5lcAA0Y1zXdh3qzm_b6tuBgAt1nMxcuHcqe834MvrSIiBASYMesDe_iCqr3qZ5u4mAolfHvTdtbNnPyp3G_TLfFThwydV0ZURhVkdAusZUZdfQqVB5g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=SE5-KkI2Fe_VmY6sarvRvGoEVB2wo7P1b_WRflfSdW-41ciALjP-4PldrEelhQuwUGn7ScT50xAs2thQ0ycRCX7uAYTEIE7dJhSMIHU7Fr7k8Yg0kKj3tz6sraPV8rhPt2SqpxL4SBOlLFQKJBefRnsI1kl1-vCV1nA7LfN5okAVVTo6iUSfmqmUarnHt3Tm3H85IZLKQKEruh5FvwuEJvGGgC0Ypafxnx6HdnXt886aU1KX4WHGI2IKrpwYptIAlqa1jtvC-MTPJzHIsbEnylaLKbwosuu3c5OgU_MuA_nBILhFTZcC_VrSj8gxIpQDkfILaRio0lbBK84DrdmR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=SE5-KkI2Fe_VmY6sarvRvGoEVB2wo7P1b_WRflfSdW-41ciALjP-4PldrEelhQuwUGn7ScT50xAs2thQ0ycRCX7uAYTEIE7dJhSMIHU7Fr7k8Yg0kKj3tz6sraPV8rhPt2SqpxL4SBOlLFQKJBefRnsI1kl1-vCV1nA7LfN5okAVVTo6iUSfmqmUarnHt3Tm3H85IZLKQKEruh5FvwuEJvGGgC0Ypafxnx6HdnXt886aU1KX4WHGI2IKrpwYptIAlqa1jtvC-MTPJzHIsbEnylaLKbwosuu3c5OgU_MuA_nBILhFTZcC_VrSj8gxIpQDkfILaRio0lbBK84DrdmR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDrEt9ziGjMucqF36EMgjxGiCEmyup0TdIo0E4ViwDwwp49mx53Vlb5o8-Cif_LGvT_ZfHwQEUczXP4I8iy1cewGbsIGMRBGmwqaZI-Y9KPP7vAew7io8STDMfNzernACWWJNflBbZUk2WeSfCoM8eok3MdowJcfS8F_xny-nRXmZ2J8dn4SkhHUaqYWnSk6oN3DYzRLPuZ4oOV7t44f_tSQeH9_HD65gVWbB9WJu9sQFeto5XoJ7y_i0rfp0exedTecVl92qxzfdsPow7XudgppPlKKpyjpyhkcHGQFPI_zwAhPqCR903l3QEQFthgpohnmS7WwC1X1iHfr4qTobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCHHEgQdJjv0uh0YWZT-mL9T0K4Onkr0iNPZ1mg9vHv7MDh5Yf5Dt33XeWZpX2kr9sOoafvIYRn9wqYjeL_glClqMS2OdHtuAaVzTD9shuX6HO29RBcaJ5fwWL9uweh0y6JPDM0VrJR7PA0ncEKtqe_SmsZP21vMdLEMCUEYuRWuHZCACoRYOISAzXuAMf74MZDjJst0la25knT3_n8SnlkfbafQE_mZEcCKeHIhQYkmNlFN--CXryXZNLzLT7rLdzLM2_f2eL3nYgTmVN7UJDN0CGJArlL3Zo3yd22YLfgtj60gmETUL848u6Jy5srihIfvedd7U49llfC4A9SMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYA70XieNwy_KKJ2o15wipXvFd1WlOEc9w60sYDr_hjrLrx9ot_MqweFpEkvaud1sCitYqka5Kaz2VcRdPRG4Ko9kJ5RqWa-bgUUGTjuGZ8ZtUlS476lRhwwD_rSOKTUHOq-LLilPN-2fgVnmEnHJaxtG_ZGjSV1ragTYxMysSr2bcO8haVX38FL7axKSL0z9Jekid1pEF2JXvKQagQ97rX-MFpBB_IzN7PHIiRKQ5azTznLHMFGkJ5fuV2g5w6tIX8lVhWa_VsOu6CgqEgEefbTXz-aSGs93V7z8ni-CmjAvqbpNt0uPT7Yvx1Hgd6ENWL3KV7aMgrhQPmft2QEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNFAO_dj-lnKAoUrgYITkVOeiD4O3O263tc4h41YKkJ5NuzXI1D2b3ACbCpqvCCzcdxFlRhWNht7uni_bjWZBxX320fCpxruIwnESlR8iLuuk7-1UQDmdM58CvcIYjgrUS9Hj7P6ZMIySj-2sg2vayb80QskcA9CDQ36hARE2LiG4ZbnzqWprEDELYZ9xX100qxPPE2yW3Gm8Fs0aC9XtLDR8g6HyJUqAsZ97NX_g2IDGYCmY-EXaEHGT5IwyScmSPjJiYq3M0XSKNL7jee3FP_N8rSSWr3tmm8sMErpbfRlRg64eKmCLOPYvgnNMrKlE0pJSjbO7wmaetyjGrxgEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=M7rROPqJvywqgo7umDWjuvmiQMcP2gw_1Hsj5agTsweaRWP1XQ5R_5-r6C-uQOm32j2ba_lm3DVTeCRR_YE8cXtxV2DsHd3-VjAP3W1nsLJ8TdZx7jRmR0cb6Inx2P-HwBR_ll4Nu2wpElafdkmV6_BemeZbaJkz01IdzFacsalrulZIZGjX2tSWI7nz9gK9xqEssG2KITAqkIiBkRoqCjvIL1Hfi1RSkjx-w_sAlIYS7HWgQ8ml3YNo5vw_4SXUTiBLolzKXnNV4_pskxkHy85SCMUcZbXUFiIoO4l76EqD_BumCsfbg4pY2R9W8wPG3z-ukvSRgftDWDfFrQ-Y4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=M7rROPqJvywqgo7umDWjuvmiQMcP2gw_1Hsj5agTsweaRWP1XQ5R_5-r6C-uQOm32j2ba_lm3DVTeCRR_YE8cXtxV2DsHd3-VjAP3W1nsLJ8TdZx7jRmR0cb6Inx2P-HwBR_ll4Nu2wpElafdkmV6_BemeZbaJkz01IdzFacsalrulZIZGjX2tSWI7nz9gK9xqEssG2KITAqkIiBkRoqCjvIL1Hfi1RSkjx-w_sAlIYS7HWgQ8ml3YNo5vw_4SXUTiBLolzKXnNV4_pskxkHy85SCMUcZbXUFiIoO4l76EqD_BumCsfbg4pY2R9W8wPG3z-ukvSRgftDWDfFrQ-Y4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQH2ZFDU8aiIH6GUFoIQfSM-sPHQx5COSrWCEJQVBE522akM4nHMBGQaPMV14L_fpShvRYVPwPXywSIH95qw4MLns6dC1yx87S49fk2pcjkgVC2vewFWVbfTpTQDrB1ndQiOgoPvlE8pOs8ifo1JEzd_NcrfXEQht9x8KrTkP6IRao051ZTMRUe6s6h53Lg1doCrJX1eXcf3yHcCZ8zgKJT7cPqYeLalmiAW4TKR3H8HfPLN3oLIMcOnUE28ZUm9ThxPFAof0JwfvyV7XXCje_EhSqQV2e2y2dQszngS6637BQQCxDnxQdR1mChOjumpJvJx-jamGdq6Htg9cHzfUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_09624Wsy8Ip6GvUD8CFPppMim1f0umfqHFgFQaHU3tRuWrBQdiaq9myrligmm_bhhQcHe7vWohfCu02cGfuN2vmG_wmHt3rq4K51DG7-4vBi3EJ0Zao7-q46yS4oFmxSKGAoJ-Ay42uwyY-efL3Y6Pqwy3RPvHuN6r-M_pHf3QB-GookX2WKo4gg6GLgKPyc_8JOEYk_PYLj9r6gP7GWTdEHQgvaFkTF7CPYHoE6P1zpsCY3REre-oQIClMzjCWgkT-nzFjtg467LaVTOlePOFxym8zMRSjL4b0-fmlx7dblYILFpSO9T39A0UvqBqqmCpKVyiS9c2y32vnQLieA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=nWhNlTqoYWCG7d40D-iVjjghkbIEqEA5ilX_Z2tOn2TCE9nE8PeYoCNXNvcdMxx8fg1qIxQTELL_7DSJK7WWPJ38yWRlns7eGXKePY0FGKtetVm75885sR16cpwd4xKtcs3qsWJh3vXx8B_pBAvNSvKoLqYT9SEJ9Xx0pH2XdNtbOXKxojph-exslVM4r5_yYSGPib7PwWYBR0C1q-gWwCxQlYpG3skhr8SRsqPWNPc_0kbL7JmSLaLq1YIsvr05oKj73aU_NF680oYvKdgRYduZagogIPW6IYhXakKPI-D6WCBiEpIQq2xIGefszfLMrsUE43MkT2kFGhksgWJfNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=nWhNlTqoYWCG7d40D-iVjjghkbIEqEA5ilX_Z2tOn2TCE9nE8PeYoCNXNvcdMxx8fg1qIxQTELL_7DSJK7WWPJ38yWRlns7eGXKePY0FGKtetVm75885sR16cpwd4xKtcs3qsWJh3vXx8B_pBAvNSvKoLqYT9SEJ9Xx0pH2XdNtbOXKxojph-exslVM4r5_yYSGPib7PwWYBR0C1q-gWwCxQlYpG3skhr8SRsqPWNPc_0kbL7JmSLaLq1YIsvr05oKj73aU_NF680oYvKdgRYduZagogIPW6IYhXakKPI-D6WCBiEpIQq2xIGefszfLMrsUE43MkT2kFGhksgWJfNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYGfzAKaVkD9AMgoYbh7jtdbW_eIcLdVnBHV81-G27e4Et0Kix2FpxudB8-cav-JNcQ9bUhQa--JiXyCPlfnvKuDtcRHkgnXvyjrG-gt5AWOefUJTO8TuixfUhlwX9JwIh3UEt6PV9cq_lszfxsciIx2gMr7EJYox2hcWaCg3UJe_z1cyHhBNOYOW_bx_6Jf25Tf95E6CvInsicuTZuumRqSi_hmwRHfxLp0Jfgp-hTF3uS9F4N4ZPSFXC1xf3esjZQbpU5fgIFb986Ks_ZecO6b13SG2HZRInTTtu8AVCzgboK4fwEdH2fuesxChIHo6GgWH5NQBewajBZwMqXxHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to03Q9rKO5OZ9se0U8E5DE7rOEklwstlTYJJZ41zIJMQTyOKg0VreYg9olq8frTBJ5Xaxez83DQuY6mMJvOTsQzdXkiA9HreeLi_dVGOOQPADGPF6tjx9AlrbbfvBigF6X-CDxFMoNe58utSl_85ffbgY-Lhc-9K8GRxUhm7hFK-Z4hjvKKhlTiCI40egeTw2LPTg2YIbW-w_DF7TZ4ZzjVvAsD-2PJqqDtWBt1nwnyz8cUXl4yJXHOJL58FLyikb9-KK4EeSNSO9LkTH7acaKN4_98qipS2ZyuZQ6d4LDlbHnGM7Qjmv4EkBp7D4jbP1IqRYzhD-e_6gvXIYE_2Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBMyqc-hwU2r68_fiq-JO3WNIcZ5zzoh1f_9du00-EZYHD9ulJCq4XPbfzHnjsfiIDOMNx5cIYXkptpHG1ohd3DxL0zbrrX9wYS-wRWSsBraic_URm0h1mhHixFWvENoWWG_BuY7EcVrhrAMQoqIlCNrzXXMuZeL7zeWeTETd3GWR4QQae0iSgN71SDaWxl44xGib0KYDxgRpBiAFd_jFqsgyeb64NhnGfx6IdP_6ECiuPdAlVRAsCQIq8SveeuklkIPXOTV3EwQPIIg5XfqUcliR5fAYyGJ8br66Ljj1mVshss2RzLGSqe6PchH0xnZfLs_ecqJgolyoz4zYvlq5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUuXKOE0ihyjG_KJRvvWZDpqDvigJb0Z_W5xg3bmtrGRVVQix6-CyvMOLwQRJX5Yz-8mZ1VGk4I8WFyKILHiWs31Ea5OzpRNfNCy84qUmNVXjkz62gP-4MATI_JAuOHSqwqjVTUY12-gPLpkC4SLvZGgWR9AzkILFbt9UHB45bX2lqZPm-B2V3JGQXttzAnS8bCoS2y07u6eST30Kbm8jl5KTShdhK-BCzDuisKc9qvkhB4qjLt6P2zYq7JNyfn923k0Oq9g7EXDGo2ZA9xoXTWdC4pUlbLXjhFSPW57hZQ36TqSmh7CkUz50lCzDW9TE4fELs3CdO7E4o9XXTQXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJoQrU7ejoknkjZcYORKVpgxG4ORUwrUM8OVvfxcbi4z0K4xse5F3e-8Vptg0o2JtzTU7J_O5tfmyvrdD-2KYRJqlKDdJq3gIQi7N548OKC8wPOGGfvgge5Yy9UFNRLd6ZSLZFNbb7n-TxTprKAiYihJrR14Li4WPx2LIUrUAqd3a0Zakh8n8iXVCjud67ISI0QCpbouFYeYzZ6Xvdx9fXOLm7BnoArosJ0VbDRabnL4tvCfesdMBQTh3qvw0nU5II2P2aDYk0j2nmemlrKZa2KBiid3Ot49Y1mubHWVERtobSRQ-nTmjubum8aHul-ycdbedDa7GRyIeABX07L5aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLxV1UKOP1jHCsnHvG6rqdZaj0hhOugcp8W2WtNJsAP_YKlzT8Q-A-oqtQcX43GZi3Kg6rp37cRQ18u7H4ZknDXozvGiNwIr97q8Tn2icrNVTl7D5iY61zz1VDw6RwuQCBP3RtJU_JfAbYjhTbbDPWEpSueJN9cG0toq8qyqWUim0r1R4qsg9c6Prx15Y3zRnx_6f8lN6YT3-jAahm4Mq-BlKL6_VjGbuy_ElSTCgrtL7XlDMgWFtDbYtTi9RUFLbeY9s4uOUzC1QpmFgGImLho3NkRVkrtpGrZHKXBN5vm2_WYA1on6TzkZpKbsgJiCn1t3NaBZSxlDC0aT3n2PoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_u-S6z--Y_ZRGYC6YEz8Q8_W11K_P5TT8YTHW0E4528RMKTpdpZQLFIG2-3mnrkjQGLg1xjcBk8iFkwDnIi5qqh4Zi5OTkmngrXNqel4Yg3ZhDvaPjnHeyBl104fh14ZbGq3ws_83TlH1Rr32aN03MG4AesM1hvMRURJt5nJYGvUIrQpY0zf5uGD6bIoSPPbMNbrZ8V-fJ_qWMTZ_HMuM7Qa7ESw3lgUXZNLRo9ixk4QCO2g8dHDwEffCxi80ewNnbrwuMOADfO6fj-xtlUafQHbxs0P7kA1K2ZW5kVtAgKKrYJb0NdCFTnZOzC1aE2uCfe33AcKGbqAgrs4HOcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MohjOHadcApTS_RqU7fpQWJ2LqQNfd7EwlsXTZ-jw1yt3GKt4Kbq86HkVOVTRUjuqYF3k-85PIb141-AvQELuj6euiMjBwb7AjNQr9_5BJvxlKRwuE_IpBDDKj-EXAWP8yiBTG2bbADrXpF5F26T-q5mRiSHHjNKQ4tEiZZoLkyY79T5rAmsuVop3dzN5ijx5zusm1KZyqZHXdBfAY5KlwtQc4pgwkkAH35FP_32BQXzD-tu00cLBaJLkrWX74Gbu45g_E6HOHuYYfNfizt81V-p96oOF3FmNDLePPYvnt1Lz8IuMh1BMtb6H2fRmjji9Xz48flksAdIbnWQ0NCBoQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=OR5k0kPLId61cxt6Rgqy-7UMFgzo5y9vYPTAoCG2r1Uv4uBFw1qvC_xOEDYugWaH6Y-XGBRDDlzEc6xEdTg_Qd4ygLRRbeU582INzTGANQkKJsCoCzd-VKV7RInr-qA_YJnlsnh2aL9bxspKcfYWzCwATXBJvjUu4vEoPKoMVibLtp7PzZ-GiokLPQkMnniw-ZuVpbSmnxjHrHo6Fs3t-Mst44gtCg4pG8YZK6hJFcQme7VKwc8I7_ETm3PY9ZNkLnj7dtOootLy6N3OCSl66-rMdUzmXXonNh5oFT-vek4hECixllIZoeDYuc0UI9N7thYf_oKvbjGai3xrWJodLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=OR5k0kPLId61cxt6Rgqy-7UMFgzo5y9vYPTAoCG2r1Uv4uBFw1qvC_xOEDYugWaH6Y-XGBRDDlzEc6xEdTg_Qd4ygLRRbeU582INzTGANQkKJsCoCzd-VKV7RInr-qA_YJnlsnh2aL9bxspKcfYWzCwATXBJvjUu4vEoPKoMVibLtp7PzZ-GiokLPQkMnniw-ZuVpbSmnxjHrHo6Fs3t-Mst44gtCg4pG8YZK6hJFcQme7VKwc8I7_ETm3PY9ZNkLnj7dtOootLy6N3OCSl66-rMdUzmXXonNh5oFT-vek4hECixllIZoeDYuc0UI9N7thYf_oKvbjGai3xrWJodLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=Mp9JPKw14C3cngypK0gcPnIOFlTF6qu6caQLklYqyj9CmoC5Fkh9bkEjCnS-zo_J4JFQF89oWspWmMfj0wFVFL3fQaPsByMkVx2w3tfBMG0DXODZo2_bQqV-go5q9I9RAcumzTq8kuikwENFJH_Utv77ohM5HoJll4EWqBW6tfo2AMIXH_gLzhPklTtMJ610y7PTIQgw9haep4E1ytnE6w6_KNJ-FE2JWe3hmw9ApbRE6UEjkPMYkwqwmf_IWmurouFQXpwbcWom4dNQjNdNW5mIV0JD--HWyaMlx0YMd2PmXwKM-pQ0g7nhBXXpZsSHyfQ7mmfRwqyy7v6igdX-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=Mp9JPKw14C3cngypK0gcPnIOFlTF6qu6caQLklYqyj9CmoC5Fkh9bkEjCnS-zo_J4JFQF89oWspWmMfj0wFVFL3fQaPsByMkVx2w3tfBMG0DXODZo2_bQqV-go5q9I9RAcumzTq8kuikwENFJH_Utv77ohM5HoJll4EWqBW6tfo2AMIXH_gLzhPklTtMJ610y7PTIQgw9haep4E1ytnE6w6_KNJ-FE2JWe3hmw9ApbRE6UEjkPMYkwqwmf_IWmurouFQXpwbcWom4dNQjNdNW5mIV0JD--HWyaMlx0YMd2PmXwKM-pQ0g7nhBXXpZsSHyfQ7mmfRwqyy7v6igdX-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rbm8D9q1Jp3YsVnTpRjSs8DWuaC65QDUNi5aedmNwRRpgX3g9h8bP_wUbFfxI__jEMu1IVPZbFMP-_ylGNi58RN6FlrFYGpEtEJ8R3LYVvDjgjwTjSUuCnlKiB6XzPuf6YGEN8PX6X0uHdOdTaIBZ6m19yah0Bf5NNxntuWOU7iPDkucOvtTe7FfoKZY_trsApYJNmmFngTH956kEwjFlf-Ix2_PcVdw64ken4CTjsd8nZnjyhpo-A4wec3HY1YL6BaGQXjGn1TS2NREyzBYsAlkHdBWxPr4oLjbfYltCc4lLK8D9clHX2Sonc9z2V0_aL8SlHszhr1UQ7o3fO0qjg.jpg" alt="photo" loading="lazy"/></div>
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
