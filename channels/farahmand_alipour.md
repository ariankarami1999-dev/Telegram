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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 10:21:56</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRqi7Lfn_3lGj7QiqiQ_tX63UhxMLubkf4GHEN_vQrhKl46xrZcHPaOoC4VzH5cENbTIqrbK38mmnGeonjTOzPniZfk_Kk5JjqFtFnBEMIKFd698FHP3rFqYDnXnn_pCLjiFrhmOc3S60dgJkFtRB2UOb6ZugDbml9BOVBa5sKXSRR6zMNWOz7PiCwVAmZ4kuvqCFhEzDQR4uLIY4J7uhMI8Y7bVOy7YuwsF5uFABnTRVtgncdQ0nQSRBd33Zc6xpGxj6c9TZMKrNYUCmi1dlZhEK8vwjY6TYtj1gJOH2q0SZlOQSsTbqKBA06BAJmW2wCsjudviSNyO-QrgULKT2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PchmgV0Pk6aXuN-ZVDCAogkduEMHwTwXliejClCzGghinkGUAXjyhSy-DTRnCWiYnsh5jOpD7E56-IYzfXjgD7M9VqTDJZQ_j4tPcotU37oskAIhWG3KpQFC-AV_tQk4auHK7__luKoEB2OTQgjRwCKcZTOLSSXcq2E8H5k9_tBhPh8NpbjvPfPdd0DSOH43SdE9Kx_QoJiCOcUlgvo8fOvI1QJ8_tWFh-txixRu6UQVRLxBfWamWQfbz8-U5Vhz5DNgAGhbO3VoRikaRV3GP05EAS12GQsEKsXQSd5P1LWwoO6ERld2gEjvMW2na8sBEcl0Jm6UB1gZ6LcETELg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf9AuUzZBGWHMWBK4_uVpkf08-DEgdMiEzGgZhpePCuCbzow1i4w_ZObT7Py8tunmAJ_m_QCBwa-2HjPrHg-AHCpkHGivXGSW1mdiy5u8myaZWBwgRQZ3sGy8ZPfoU2_JwA0Y8uc-Vi8DPXQDbbV4frshqi-A2wrhNRiR5k4mpprbR9jZJbh-AR6SWb_Nu_xSE3j243EGVPHv4bDjHh59QsEqLPt02_dNhhawFIpVj7qc-yHbiueSeccComI4jziZaxB9eQZFPboDkdspvgVUr3Fptc9b8G3YKhryHo0mUgzOpVGP-Jz-XFWbZsQ2e5BvkqlAzHjTclgNrmZOOwJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzg5-__0tS-5U3UwOwBgufgPSdyfkzsv5AVHjc7jLEHds9zGXbWDfeQsSPxM4qZOZO_sWOLbGvzgEyDBjTVbo7uUYMnL_2W5glcn6MucycUSKBQReRCdoyYXbzRRn2SuughsHqGXeqK--FQBto_StiqRAPkR_bsMO6qcdxkPHrCaMFzi6nQ99uYXLINnvp5fcJE1aT7QCcbz5d2awLdVh-0R04uCWNrnJqEqRl2hvDqlUKlc-24dsD4ffXO_6KVsuBPPc84A-iXxYNYYDgEDi-66X8b9BKugZGzfhfeQQteqz2cd-jlCAoxT-hm8uH0EgOgLY1HERMbhw3rBH6u8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdrH6xB_gqYgkfyLri2Q06i4ZrBZGEotYDgRW1Mm-Uc4X6FMSYJxcXaq25WTJLkE2crRPSs9q98LscVWxT0YmotlGNGzdbCOEkvpY0dtSjxvDen2OtdRVC35YoEs0O8VqRcFS-ZGrhsQiXymeh6uvJFwKAozVIWZHUc5WIsxfzbBd7SB6UWOiF-zRdu8qpD5iOgiiW7yO-s7Par1ObFAVK25d1GmtzJ9h7HXqTxKWsszyvKlVwRbSLiZgH7oxGeM1bj4-WJMTFAZkoSa395L0p4DtXNZPQnjfc9qjoFbWM7eH2fLFKQFwXpKMDToL6JXydlsLJTFCBmiciweuA9Ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=o1zAccGVdl9aqscZUpDyBf_HiJGZQYh_ut_hXrBe5bgPk6ORDag_Q0E3XELj9j9-dt02wRUCMTyJbEaKshaN26YzFnBRcyBm5yZeI8Y9caUBP_rt5_XHYkHaKVgwf_cjhOMgw43pbtSQZlCXMovi-opUhBY3ajiEeZxFlInj2nxvUenlc6E-DewtJoxMEJKio2pbEBAVht0UeoEp2zay8AvuiPwbE5jpia4e_in6DPNEJG9NGXozrT1slGEb0obkXcZDNbn1AE-i1tbOHpp2t4lhapJTtMmTY5Rbz_UF7muEM1Hw5Jqyf7VqcKo2oV_D856rb8-ChD5toBP6AH_4YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=o1zAccGVdl9aqscZUpDyBf_HiJGZQYh_ut_hXrBe5bgPk6ORDag_Q0E3XELj9j9-dt02wRUCMTyJbEaKshaN26YzFnBRcyBm5yZeI8Y9caUBP_rt5_XHYkHaKVgwf_cjhOMgw43pbtSQZlCXMovi-opUhBY3ajiEeZxFlInj2nxvUenlc6E-DewtJoxMEJKio2pbEBAVht0UeoEp2zay8AvuiPwbE5jpia4e_in6DPNEJG9NGXozrT1slGEb0obkXcZDNbn1AE-i1tbOHpp2t4lhapJTtMmTY5Rbz_UF7muEM1Hw5Jqyf7VqcKo2oV_D856rb8-ChD5toBP6AH_4YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=kkWCAYT6boA63iDEFKDldjaBURJunNS7I-pqKW9Y4q2CzT2_F4GWohilE1iZC8d-IUmMBnmsIK4_OvC6sTeqf6P7IZ0Cc0XvLFQywoLFGHp_GJsxDiupxyeUEcL_lO1pAyUAmtDHkzGb6aJc0tZ5AnWp1-yakxBllN-v4MpXFx8Lj3yQ9lq-PYQwnl2PuQYy90PE6HMdU4d91Eu85PPc9wpmclKnJn7fdB4Pb-INlJ2WzYvD67j4rICGGZqhzF-P_TUaFHKsGDn5_19IiX81DXJtOhtsa5-vErMVpj5RudZx8BEPgoCJGPNupeOMvQWDE8CRFrVn-S9luTPNmEhEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=kkWCAYT6boA63iDEFKDldjaBURJunNS7I-pqKW9Y4q2CzT2_F4GWohilE1iZC8d-IUmMBnmsIK4_OvC6sTeqf6P7IZ0Cc0XvLFQywoLFGHp_GJsxDiupxyeUEcL_lO1pAyUAmtDHkzGb6aJc0tZ5AnWp1-yakxBllN-v4MpXFx8Lj3yQ9lq-PYQwnl2PuQYy90PE6HMdU4d91Eu85PPc9wpmclKnJn7fdB4Pb-INlJ2WzYvD67j4rICGGZqhzF-P_TUaFHKsGDn5_19IiX81DXJtOhtsa5-vErMVpj5RudZx8BEPgoCJGPNupeOMvQWDE8CRFrVn-S9luTPNmEhEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=I3eUuOrTV48udjSuPJXGUG1KuOFUAZ76fMmJ8_bSlFE1MkoHq_7hjp7-dCyNBalFwJrRJHWeHmqDJRZ_BfOVGTm8jn68Rqz7jAKpsBvsJZkq415auAacvrJskWZUR3LiPkuCFwIMdqqUKZkIcFJpEQgm457lpvHVKgmKOxt5lQ-lqgzLMZ9lyRVkvO36JMvT1sAumendotGim3--Ii6MxGrwaZgqU9i119NzvZeBEV0iQWyCMY9nvnIBm2IRn_tDSN0F4gNAeafZGvqYOfE70B3YdGeU7ztF486-yVBZqdhmu_Yb5cfs_EPnWUykJEYoU_60yIoI0IW5MOc_aCWGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=I3eUuOrTV48udjSuPJXGUG1KuOFUAZ76fMmJ8_bSlFE1MkoHq_7hjp7-dCyNBalFwJrRJHWeHmqDJRZ_BfOVGTm8jn68Rqz7jAKpsBvsJZkq415auAacvrJskWZUR3LiPkuCFwIMdqqUKZkIcFJpEQgm457lpvHVKgmKOxt5lQ-lqgzLMZ9lyRVkvO36JMvT1sAumendotGim3--Ii6MxGrwaZgqU9i119NzvZeBEV0iQWyCMY9nvnIBm2IRn_tDSN0F4gNAeafZGvqYOfE70B3YdGeU7ztF486-yVBZqdhmu_Yb5cfs_EPnWUykJEYoU_60yIoI0IW5MOc_aCWGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=AewfGvYs7KKb-mpBG1zc4c8PmXNkxu2LN_s0iZuOHbRbnQRlnk2dg563vY1X9PEZC26QYQAPlwcVpA1HXDFxUdvDP0Zd9uvzDA3x887qIpYm92laNANwkLGzx6jLLqr4rs8qj4aI3hjqP2e0yvvvmajjiXtPu6R326ER_orqGTVDgHMgDSy9yDaSPE2LjaYDQaExCA5Zjemsg9UkVDcoRZsW89rH7rQbgjfVhu1JTIdUdDuN6zwhA6DsB0rRbXxnpl-okamSWEsnj22_0nJHUTIICQEvc8iDfDLxXO_sfulh-O1M_fiCcyCWBzJUKUTrmJqi__kvu7swGCdNq-oyqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=AewfGvYs7KKb-mpBG1zc4c8PmXNkxu2LN_s0iZuOHbRbnQRlnk2dg563vY1X9PEZC26QYQAPlwcVpA1HXDFxUdvDP0Zd9uvzDA3x887qIpYm92laNANwkLGzx6jLLqr4rs8qj4aI3hjqP2e0yvvvmajjiXtPu6R326ER_orqGTVDgHMgDSy9yDaSPE2LjaYDQaExCA5Zjemsg9UkVDcoRZsW89rH7rQbgjfVhu1JTIdUdDuN6zwhA6DsB0rRbXxnpl-okamSWEsnj22_0nJHUTIICQEvc8iDfDLxXO_sfulh-O1M_fiCcyCWBzJUKUTrmJqi__kvu7swGCdNq-oyqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=EYTmjf45pb2UKtLdicaoBgCR_WoWfiZVxbAaOqZYRkIELm1iVnDJuUg-AH9s2noPEDqFhTY3Aog_j7dxBPugqrIBCCeNj1iQAo_ufzlyhA6aNWP8RXV-mwLHqNMjBVnlvkgQbikTk0JFGhir6utAsngxMsIcnZuJWqaaq1-3lRcUMGLze0fDTgkM2BgXcnf9JilVbbOryn6aQ7tTMf8d1yQYHfx4eUX13d94J1u-_WI88-odMq7dPoCZLRdTaYrSr2z_-DZxM2gD5Y7SDcVRwB_b8OR80cF85RRb6eJhNtk1J48_2Km8oKOZRt34Xo4jTwD3-NsxwlCuFFb1pu213w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=EYTmjf45pb2UKtLdicaoBgCR_WoWfiZVxbAaOqZYRkIELm1iVnDJuUg-AH9s2noPEDqFhTY3Aog_j7dxBPugqrIBCCeNj1iQAo_ufzlyhA6aNWP8RXV-mwLHqNMjBVnlvkgQbikTk0JFGhir6utAsngxMsIcnZuJWqaaq1-3lRcUMGLze0fDTgkM2BgXcnf9JilVbbOryn6aQ7tTMf8d1yQYHfx4eUX13d94J1u-_WI88-odMq7dPoCZLRdTaYrSr2z_-DZxM2gD5Y7SDcVRwB_b8OR80cF85RRb6eJhNtk1J48_2Km8oKOZRt34Xo4jTwD3-NsxwlCuFFb1pu213w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=vKWHhdMN93eHmLa0XxJl-IdNbA84d6pDiaNNl9KbQN6nc2ODWvgxOxGTUKwvs3nyfnhdUEzmLbg4chq6FJW8MybrjTqW3tra1HXvKUgjayLiPWi8bMPsXBvD8-ovTfPm2x8hF55JyPMEV6Sy_if6RviWnzjdeZbJeRlQ8BPJrwGf86uEtskS4srzH-rwybS8VTFtLfReO_4Bh-USxg-VwZf5zrjWYaFwd0KhTV4S82y6xJSvinVMLLZhMfdYeJ69Njz0hNOOFjFXdkxZCtIjTsPPFE8aK16pGPTXAusBTcysLxkvNy7aDfn_DuM9U3n_ZTciV3sMruswzOPjDcSXAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=vKWHhdMN93eHmLa0XxJl-IdNbA84d6pDiaNNl9KbQN6nc2ODWvgxOxGTUKwvs3nyfnhdUEzmLbg4chq6FJW8MybrjTqW3tra1HXvKUgjayLiPWi8bMPsXBvD8-ovTfPm2x8hF55JyPMEV6Sy_if6RviWnzjdeZbJeRlQ8BPJrwGf86uEtskS4srzH-rwybS8VTFtLfReO_4Bh-USxg-VwZf5zrjWYaFwd0KhTV4S82y6xJSvinVMLLZhMfdYeJ69Njz0hNOOFjFXdkxZCtIjTsPPFE8aK16pGPTXAusBTcysLxkvNy7aDfn_DuM9U3n_ZTciV3sMruswzOPjDcSXAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgvBy8stmCpqbBg9aaS4DCaS539uNoCsSk0iYCfUipdvYIBB23MxMkmWCvPD3XR0F74XYwns-buGxGim0cJ7MmpdBQP7EvTtoloFai8k-hH8sE6G71soPzKJf0aQzqOOvlTtw6KUSSFwRwLqZgPbJocuiCNCRfZb6hUScxtxhU-vpGF9GDee24QV6fRupKCc39ZzDgASnYof2W-d_Uu4Q9N5GfRzFrMpIaf9rCn3xOIU34X1yZChcUAbgxmr0RjLjJmCzALHOxJxsEBoNgSc4WRoHxyt8Gt2vbcN_2RyV09tZHQ4nA9izRS9cOkr4fLIlC17jFKn_k0mqarftjnICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=pc8iTCMEESYgiGo-hiSCeNOUbamq6rSi5SkkSIhqn5RAuW3VO-LyXoF86NXJsqQzkiUZS2qktP8fTzceg406hfCE4Qw3Ai0vsDCKg2dAyKmeK9ovMl3wyQeG4xebT0I13rtFTCDuNuw44QYig3qeay7RnMY1HN69u4F8UQSfTapuu1nsC0pkAwOed6FtM-ikKYON2ecjBQL_znLZWSE9CWUz_ctSm6EX3yJlK_AwlNCIQZ7CUH5MNrXoZAYsLGk0WQ20a73HQ7Q5FTNheIjvoHQ9OUddZScwrXU19fWg4z_kkTZ876I-YGwf7zDmceynBF_LnVSuJsru_vlkY21ZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=pc8iTCMEESYgiGo-hiSCeNOUbamq6rSi5SkkSIhqn5RAuW3VO-LyXoF86NXJsqQzkiUZS2qktP8fTzceg406hfCE4Qw3Ai0vsDCKg2dAyKmeK9ovMl3wyQeG4xebT0I13rtFTCDuNuw44QYig3qeay7RnMY1HN69u4F8UQSfTapuu1nsC0pkAwOed6FtM-ikKYON2ecjBQL_znLZWSE9CWUz_ctSm6EX3yJlK_AwlNCIQZ7CUH5MNrXoZAYsLGk0WQ20a73HQ7Q5FTNheIjvoHQ9OUddZScwrXU19fWg4z_kkTZ876I-YGwf7zDmceynBF_LnVSuJsru_vlkY21ZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHeii6r7wv-1g-Y1hQL7lSySpftqN-UjoBUdewieP87W9cVUS9POfBh40sSYY0SzfvtxFRJa3EmdUvci-aU00khEY-jmGp-_bYmQYOKA0gTIT8YfAYaL6c2lNmRY_J0hr-CzoxmNXbuanNKaOjLY5a4HaCwlLKYT81v1hDVs8voIAGErNUnE_JHnZy3P320lDqXaZ8vfue5MvPAtY_W2hHXcLk-NpWX6C9aKgXhREvPrXbsRUzrLG94UOVDbCx6IR5HvPcNi7MpZsiZaX1GYWD7I5H9D22VQT41EDs6CNW5RKhKffz1japT_oF-yH-8iNBZ6-iOQhxPEuo48MM-ugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=vp-lagswVMg-4SjIOFTO3vRU18Rd-efTtX3fbcqcOejmpTGXYOkoYQHNbPqUHNESDwubp3ny-md-bVEsaOXtGZRiW60xJxnz1LW5aGvAx6c0ztFUWYcjt3DEGaNKAF6XBbcBEwcFT1cDP6y954YXh623HQX_Ft2r8gy_5eYh66nxnV0Mm9fuKOuDlju6AphmEGi5MePwQAv2QwQHivRZENWDfVzPlt5grqvigaGJMDB3JTdTBfsY7LsPGtWgd655A1jEIU3j1SGaDaU-Dht5n_WrpshovzIpQNJXUDKI4vNzflEZLRZnQRzr7a3NxHITTluiCKKQXQ7NIQkG-hbLQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=vp-lagswVMg-4SjIOFTO3vRU18Rd-efTtX3fbcqcOejmpTGXYOkoYQHNbPqUHNESDwubp3ny-md-bVEsaOXtGZRiW60xJxnz1LW5aGvAx6c0ztFUWYcjt3DEGaNKAF6XBbcBEwcFT1cDP6y954YXh623HQX_Ft2r8gy_5eYh66nxnV0Mm9fuKOuDlju6AphmEGi5MePwQAv2QwQHivRZENWDfVzPlt5grqvigaGJMDB3JTdTBfsY7LsPGtWgd655A1jEIU3j1SGaDaU-Dht5n_WrpshovzIpQNJXUDKI4vNzflEZLRZnQRzr7a3NxHITTluiCKKQXQ7NIQkG-hbLQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndL1vfIWi2LGIcFxd8Yt8yPLZLxqs2gORdHo63wCNO-hr2ZLWrT1wzvtYPtawWMDSJvWBJMotqLwmfv6X92biApdu2CXNn0RROYGg9I5CHKqC4N-6jyv5cf--UHJ-GZ9_3PMISxjauprsd5cRLniQGrXbolTgi_ln8Uh4soNq01mURm1c5dD2YADYlzy4fMoj-3CrTcpjW_iQFsqq_xodsaDeN9ABBOZjcrGgEgF8K1YwXzgZf2zMtML0AWIAp6qEMD7nmC_Dj-HGVjSihGWxQwfjQyYzNMigFEoAg20lGRG_e7Ui4sx9FGHV-k-NiwX4vhanH-xK4uNFSad4EkF8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImLyB8ubZVLNRi2ChK4Rxgdinq6vv1CutT-SxdQmgX3-Wt1hfiSg2hJBhthGjntEHr_SL6Dvut09baKc840azfwfjd4olRBNMijRTXHogQVZieKWCNbpC2cxYfCcv5jHAf77IuEOogTjCauOAhVGEvQfATnGFqXg61d_QlL83cZtg4ZoTsZvu7ymOf0NSthfDuZ5-JFJ8Qj45LVHPAW7YVgTv91QOnUSeUuGJmPkl5c5ffgwBnk1Dyv1SCiWAlhtWYXs3xSo_qz2CCeAt6MPQXcuJMBBLQ7HvcUU236OgoPMntC_FSW1MoApkpZCm2jLYyQHb0HawoRjc4_lCsPdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3Bop31eWgSpiIcKHSixl808LgeaNQYTU-VPizBqwoY3-SenUKbq8Ae3SaX0j2cSaynqRB4K39OuDr8f00FI47UolDCSlr6HciPsTMFdpdWyiKTTfDUKvyYEuncGmUKClTn8ERRu56-9-utjpZazc_MZ83q5BmYxKYsDw7uXE6x4z7c8-CWKje865XtLLLmCNwZuS_epLWHhpnxv_26Q1Q_N3FHBpnTP3yBSoaSylddz7P-ztf_ftmceurgJb90secYrPyYCE84wSXl_CYd9iFl2WRV-CoE4ami1IBw6UUFcDIXYSqzNRIDNF1rDNM1LVTBhze3zn-5mdvRPRrxjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ66kYjEZc0eymQkfdKOufN58ADsbBCd86v7LFcHQhSTCh3hCxhyK-h-yNH1POJytxX2Hy4Gb7FmvHyZvYJa3zzCCXZQZarfjoGT6_X84Y2QdiWgfJMzMqFvx3_3bsrTaStE-PCwLMFSaGu6a7-CRsb91O7xu80yZrFGzceatVZCWCdKkklOIwt5MiTr-OXOsquChTSyqlaBr4DJFMJ99qOQxatnKeZMtRYvPXexa3rckmNchwNveDDk6fSs9D9PIs4452_W5V1USsZbfkNaZkyAeCcUyAlvHkBqD9g9DIXpCDK3rzsRoMEDs5YJkNbluMT6gLNf1yTlxySfM0TakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl0_ufbW8OIPrze_AoXiQAEDUU6eUAMCoOkRd8SMQQZjZzQCMpdCfs6AsEcONjOZY-wVhlEog-TU6kL9Wc2eshdHsEdec98av_LT58mh0dlRzsXwobIlkitby9gXNHkPLblbjAqQrOSn_bPSCAL5DR05OfgsnIEcanlli2ftsLru_LuFvBxAFyqE0u9pYHarUt4iAoNSqgOgrXAqkaq4tKQWRdoRMFygPMI0bduOp8OMZKXoIApztkvPg1NCHjdS5a9GjWS26nsjm8G6bTLw3Qw1bDdUkT56_6r0I96uceIWW5cszTKhrcj8buvF0rNpy6IU1wPW9YA--pdgSOiYGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhZwh7NOEa5xpA3062KOYfDq1jfgU9FX1O3ZXzJHwSeVgvj55ibhutwwae1BtSGQLIrza1-LABL6A5xkzxuktp9rPbXcXRsvC9B8fG0dhS8l9Z_xOCX2aWJPJb7Y5Zeo4JXDQfW8lwSVj5YfRLIfVHIF0xli8BSgPuFuK6fW_SvZQWr5m0-5et3dG0s3BcollKBPbHk7BrCAqVV5EHljXqJnNSHzCDaTIwbnk6LXiG-NYRNX7eEeQwdt3Bj6408MKvzrwKekULIx9mPWaxKOk2SuCJaf_S3ELMcwS4SyD9z3P5IswaEXXjnmnwNlfO9qr7q7QfABAG_zc1jcRKmp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb5xJ9WZ_geWawFvqEBGJrUh8GDMRyoTuBw6fUm8eHiq4sZ2Bv4p3qskXHKhNyIfV67sPVMR0JaCd_LnK-if1qrkMfN_LoGr8wBq4cKaCvd65zgw4GBCLl9NC-1BCLEizrU3QxfpGl_8SO_-_0AArcEFbGivAKmibasOdQhuVfOiy5yo__GaWyRh__o_i3ahJBrtG0uRqoEEWkcCZ4AyLeylsiPn4_fbKEGOEAB0OBjD6_v5m4bdgY1m1Xd2491cwN6yWodbZeopLxrWzocxicRpqTdRMFYDdNmoPqnBRIAWUZhmhKpfhojJoVyuR56bwcXi9uftJm6T77tWlJfTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=uFFwz5MsDK2gkfF50CyN0uSqEr07Fn4YBFp7flaGyadoUb2NO5FGKqExz8ojgvC1yaM3qZDuJgotnDg_mZNOX5wafryos0sErZKi03FYgM7TRSunCi3HtAHaOKd2LYWfMcz6vzWYTIaHy6-X38q3D56cok3Sr-RD2_7rTSlaynDwKn52kZZVq9h34z7FT_Nm1phlqneXlYF6wOsMGFhBkrIiDcx4AJQxacfnKUiA2l8NYZz8Ndg3Sj5soXpaAUxSwDEja-eHpV_F9eCd6Cq_L0UU5XYc9e2crBmeX1Olafgb1RAMOj09qPu0p8aKo2Q02VA7bb-dalG7iqegaaiGjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=uFFwz5MsDK2gkfF50CyN0uSqEr07Fn4YBFp7flaGyadoUb2NO5FGKqExz8ojgvC1yaM3qZDuJgotnDg_mZNOX5wafryos0sErZKi03FYgM7TRSunCi3HtAHaOKd2LYWfMcz6vzWYTIaHy6-X38q3D56cok3Sr-RD2_7rTSlaynDwKn52kZZVq9h34z7FT_Nm1phlqneXlYF6wOsMGFhBkrIiDcx4AJQxacfnKUiA2l8NYZz8Ndg3Sj5soXpaAUxSwDEja-eHpV_F9eCd6Cq_L0UU5XYc9e2crBmeX1Olafgb1RAMOj09qPu0p8aKo2Q02VA7bb-dalG7iqegaaiGjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3q7puYYPqOkif7boH_uKJns_XaVRw56NkVuudZER_s1NTXG5uF_Q3OfO5osyzVCDoseqryMWsnObhHCHuo246Oyjvob3ZuwA4DjhuF3diWyeJFeftgd-yWjk8QtwvmQ6m44NtNMh5tQGSQlETex08TvXnatCN49yZMhfqjh4Flm4wmrSAx7RnOiwEgLkdBOVc72INxPbeK9sq4M7tqfUfEXwLGQWUsLKoHHff3FDs9i0TP1vR0bqHvNZGJ0VjorSPS_Uv3fYNoGv7L2JRQFGtYAq_4_1n3QMR70CdJ8s0ouhynSTLIHIDUIi7wcdNB6gA3GlvGsriqTw6uvtOnyNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2PxmyGe9p_I6A1oloo2_pvLbGc97f5DUnwITGetNTZaHcTp3gFo1iATH8M8ln8Vc6RvJAuR0TU3h0HLIxxSqL9PCHx3gUt0Y-rJ7PyQ9hZWXCz22VhmamacMEDWH-vbaQfezh8dNhbGterkqcOJ6kjH63uqQT774v_EZdA_kA1ruXw18R0NNkmjjIlyi10ZjsSrWNRu8qapg67kd0WuPkHNl34G0hulMLGBrazdLSdQTn8i79whVvHzVjEKGYHV7-1K3wV0IVc8sjCofxviXvTXzSEOtrDL-gq-YD517SAHJIRYqGMOKhFt8TCfmpmoOiwjYKdHIdya3zZXTAPVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1tvB6i4QBnxWOfZoYbJ9ulew8Pl7keJWabCyv7-u3SpgrRgjxqsByGu3cAKK9hx9Dy3NfaUvmegGqt-98XAFBCid7eqLSd4OVwSZYOcTtXB3WsEpQCclUU2wvJ7AYoK19OyJnRagsrWTdt6P0eitV2zTN2t690_B6Tpcs2XUFH3G8dLEMaL71l3KQwJ70jk9LEcEsolizCscbq5viz1QcirDSTKHpbW8AizbIYHWWnsfvEns3HBF2WpymRRUeT3C1x15w8IVCiSAq7RrtCffgRpJpP2q5r6d1E48Yw3RwOprbhHrr2tazKydw1j0jlzKmt0ccEaA-VL95kAnEtPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1hgWwQXhVtS-Lck6gWdA0RyYELBUWuGsClM8-s_QXi36cbcDr9OSYSdgDylTNpNauwUwpJf8OUVs3ql3GhVTchhXBvgr_wMDk_ARNGGjWBxXWiv2pDCeUaP6jXT_rtt2n78JN0utgjY_yp6Vcb0PT263Xvhs0ErJT54FfMQALttKa4rGGc2ptePjwEIFiLwZcDlbuvKhyu9t-0H4HE_wKyzob8CTRh4VhAiBQRNuE1CY3NevDV9IfsRmWvQP6r3lr2GQ23QgLycGAJ3Gpnqv5DnzS1zHYuxpReHevNVoOM5PG45E7DpMPAb30aCYOoWMyrFsSmVWTAep1dSoOoYsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_8xSA_42xTvw9s-2vK5Co3bvIdnc_AeFYs1iQEG-SzDaGte88kiSGLh5hEXoiLFBjFXfwcmnv0WUR5X-GfJtl_whVd_uNOF7qXe27jVrZ4_X-FiHWfLix1plaeVPc_EU-nM4otHpvNQ-VWtVdVEB1nrTl0onUGZh5vUcXqPFxV1HORiXNbXTfl8NbzxUOLgm1GYHWJskqiasXUAwSyzpuBjI_Mo4W_bUi8WGnvY4bKi2ypWqN22fcZv3UUr3t4sGWxOghoY6Q59wnhOuFHOnznyrJDJr3hT6izLsUPJJwVIo1k28NwdtzCu8scAe75g380dxXHeVG9v6GNnE4TXcg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=pxeB-HZ5YcKfezkFsF8uwQfaGD8dP2b1NGj-jMSzdtb6S9AeboZLOyNVmdry2hMYpHHFji6bCHRo8mlUuMrmMz7RHZavs9bkjfpMi49iSYGfcNhTTt_cVNyqQoklNJtg4Wu_J0by5TmJrqBsoYX3qbBMrEkB7s_m1MnOyEf2gHffrdR-o_D6wRXaOVtQMCwz1XIcbNd1-cd7gaOYT3HceWyeTcLLUW8uyuKEQbpBMVLReSfLgBVCXo8zmKKPlJWOXJgkNLaWHr0uBYOoxGKWP8cg6CqTqnNy-QEa6secJpXJl_Ty7xW-B4j9gH6S1kJZ0ruZkC0jWrZuUarCma_dBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=pxeB-HZ5YcKfezkFsF8uwQfaGD8dP2b1NGj-jMSzdtb6S9AeboZLOyNVmdry2hMYpHHFji6bCHRo8mlUuMrmMz7RHZavs9bkjfpMi49iSYGfcNhTTt_cVNyqQoklNJtg4Wu_J0by5TmJrqBsoYX3qbBMrEkB7s_m1MnOyEf2gHffrdR-o_D6wRXaOVtQMCwz1XIcbNd1-cd7gaOYT3HceWyeTcLLUW8uyuKEQbpBMVLReSfLgBVCXo8zmKKPlJWOXJgkNLaWHr0uBYOoxGKWP8cg6CqTqnNy-QEa6secJpXJl_Ty7xW-B4j9gH6S1kJZ0ruZkC0jWrZuUarCma_dBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRGedMieX8bPB5kYQUMzAxMk5bAL591l_OwL27P1vcU-0M_G9swZ8LoVOsciFf8kDqq-8HyV1c7_4yqtQrmfiEZEDoRvRdyTVXuuwGJQFlJR5mmAHCYJkBlg_VNxb4wudE-jX8blrpJ8DuG5m-uzihzY_X9gt4ocJmkXWi3_W4KYDDOzor9JToJWY-H0g36KdQot-s997unRzAtAIYxv5jhgsrx7o6h3SomfG2Dq6eo7hmlI7nL2iUPp18ooX3hCVXyoZPRxQtQWIRXK_K_qlI-S9x-cUEl1AMjWYJNy8tF3zlRwAbR0LNSXFek5rQyS4CgKIZKMvAij4XyoLsQyVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=KKTUbWRojPZnwulgvbhAP6-8lRM-_iO7E9bBIm06CraaIm0n7Ymmn1j5ha-NKoDYQta2KsCjZEchxSn103jnKXdEoa40uZ2zOnty6u0G_BxBWGzxBJ5TAdcd7gLjC40t14EuWHbn9ctaTcMxiHa4EuLX-rb0Y2Yn-Sz8bxNdDe2Ul633urLpONHPtR6x7K6nRHrMRCTdZkxp-LgD3yg7k9PmbODHyIb_E9mNU1ViTB8pd-1-L8Z2Kwa9fTOwgBEeHF9GyQmsJ3-xBU9YYHrMCtVvufLYM6-tkfIrzbfVip8RctX8BfhfnN-2hxAUNVfvzJ2Eha07uYrCjH3011PQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=KKTUbWRojPZnwulgvbhAP6-8lRM-_iO7E9bBIm06CraaIm0n7Ymmn1j5ha-NKoDYQta2KsCjZEchxSn103jnKXdEoa40uZ2zOnty6u0G_BxBWGzxBJ5TAdcd7gLjC40t14EuWHbn9ctaTcMxiHa4EuLX-rb0Y2Yn-Sz8bxNdDe2Ul633urLpONHPtR6x7K6nRHrMRCTdZkxp-LgD3yg7k9PmbODHyIb_E9mNU1ViTB8pd-1-L8Z2Kwa9fTOwgBEeHF9GyQmsJ3-xBU9YYHrMCtVvufLYM6-tkfIrzbfVip8RctX8BfhfnN-2hxAUNVfvzJ2Eha07uYrCjH3011PQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=EwfNAbpfQ8eHOiMdIHZksoNpj1CVufCRjZpfb8zf2KiIyTIPFlQ17JUkdrvper0krqsDby9ekYE1udOF-zKA1pxbRKBKKYwA2siyzbfIR6n-tvpvFh59FWEer-udsBuradCkQwMWgt-LgPGkO0ip2KI_rUFm5Hg0YReEifALY4W16-smGkfHZAsZ0bW7ojTWnbjxYPslYl4VL858JI2ky5kCRmA6-mIWqJChACBaA5S_hDbbp02U2r5A1QfcaGBr8cI-SShHseUkmRYvxloLx-ZHgX_3rkOD5roMu6B89e4CxgW1u5fRqWjW68c9lmgqETXRETAYT4hQD98d24qqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=EwfNAbpfQ8eHOiMdIHZksoNpj1CVufCRjZpfb8zf2KiIyTIPFlQ17JUkdrvper0krqsDby9ekYE1udOF-zKA1pxbRKBKKYwA2siyzbfIR6n-tvpvFh59FWEer-udsBuradCkQwMWgt-LgPGkO0ip2KI_rUFm5Hg0YReEifALY4W16-smGkfHZAsZ0bW7ojTWnbjxYPslYl4VL858JI2ky5kCRmA6-mIWqJChACBaA5S_hDbbp02U2r5A1QfcaGBr8cI-SShHseUkmRYvxloLx-ZHgX_3rkOD5roMu6B89e4CxgW1u5fRqWjW68c9lmgqETXRETAYT4hQD98d24qqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccgS0GLkM_AGB17ccXSczfK4e_xtAjvsrBypV-vfbYzNyduV5yfyGXr_IRipCFYdJoz5t4MDup8eR5dgI8vYPZpdU3BQ5jAmh8gtqUjJXNpK3TV6vQ622wmAK2QPazY8cN6OTecf_5F09QDVTby0VdNYnzOK1tOcZWVPg-g-9DCH6zwbxCYZzNi3Y_QCMrYxNcFWvxeCTongMORCQbcOpgj9D4kGt87QnwfOOcAnkvrabwzQePaT5c06UmOfHXdMGeDGi7MKEL7PgoueBB1f2VmM9yYK9vCQVFsbLNBN99eMazB5aWqf9BsgMN96UyRvXPtycK-EkrM01NRxToKZ4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUss9RhhH59jtcWaAm6og_MCYKeqeBnKN1JRGTCq7-_m-LDbcrNHqf-Hehw3X7Zwr6bgCR5k4XS7W7fTUz9c9zBzNES_Qvvv3uSKUmTvhd3Tl2cw75YjWr8aEEx08dl3RoVgs7Y0dAgqZWItJ4Qz-V_RG7EI-teX57nYO0480GdauPcXh5lc5UjpekyWs0dSuNW-Hj42GGgNRTdSLnliLNmhGBwaZH9QiwNilzNLIEi-TYvkk9E47SCQ7qEufGcq5jPtZ9CuOH45sE8J1skxfOfHgtXPJl1XW8crjsX3vxFlM6jWUchMGMm2m2pHL4H7gRM23AhmDbWdE1o41QDXwg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=fvk8qJsiYsAYjf3myeo8c4dLW6YgqoQI6jjs9XH1TeaYmAcmGGrn_FLPfmFfHfDGm2CfTQwoC94OLeRRN4aAg6EkK0pFSAAQYls7DoxhNK9D2ZozPaQ8ZTEmUBDAlaRpQEVEkKDpISrUenlfkLtG28uZqrwkp1lMXaywY60XyOdgYTV2BUuLcQUP24Z1SutbipJSKWrTDm7cXjCcupIcc64_Ex7F9AsHTNdh5GLNJ3cyIGYy6uJyHn_fTGio709KCY9D-bBj9Mi2d6gKCSIEdAYd74xsnWNDHYF7RGS5QkijoyX2cxsUCv37rJzkfRZU1QEzvbDeVM0fvV_vk8loBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=fvk8qJsiYsAYjf3myeo8c4dLW6YgqoQI6jjs9XH1TeaYmAcmGGrn_FLPfmFfHfDGm2CfTQwoC94OLeRRN4aAg6EkK0pFSAAQYls7DoxhNK9D2ZozPaQ8ZTEmUBDAlaRpQEVEkKDpISrUenlfkLtG28uZqrwkp1lMXaywY60XyOdgYTV2BUuLcQUP24Z1SutbipJSKWrTDm7cXjCcupIcc64_Ex7F9AsHTNdh5GLNJ3cyIGYy6uJyHn_fTGio709KCY9D-bBj9Mi2d6gKCSIEdAYd74xsnWNDHYF7RGS5QkijoyX2cxsUCv37rJzkfRZU1QEzvbDeVM0fvV_vk8loBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrIxd9dc0aW1aK3xnBMGCQWWAKS_AJKqa1WOfNC2-hQB1EOytrZVYljHsxMD_FdsDI3OGrfGMD_aiMrpRxqbQVKt7Og4Vv5nKsDmTsRUJZGQV5hfKMXH-P3MtRUv0c0kgmrR2d1_wl3g-N_A7Od0h9EybX6PFtPOEDVniRyOW89fVLeEV1TpjwzAe7aTEQJZ6qwyv-ZvfmIWoh6LR0ai2yHl64XBI6TRbO12lDncnWFQ0wZ9OzVEv8cPFgmElEObTADF7n12678Au75mPhkvj2J1Z_TYwUczAm5Ld9kiHjbUbRY-KK6uhqJby0oCTyoaMwrlm63RT2bVCk0gEi01ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF8P8UPLDsrKH9fyzurTDZf0-wy0BnKahsAmwFdX9xoXcq5QPnvnXCCYVGPlB_uEY3t4MBOqfPFvbCtMVIxq45ks_0sbxiT807lTDmWTo9kSWUB56O3tvt1Wrbo5Uyq2GFHAvtkoBFSOpsc0rQ222xk3a6wSY2ePDBgpsEm52W8qFNDvihDuMXxe7uLGDjsgbwkB2AuxT2xt0VG6BltDyLpozCbFbRoc3Yz-pc-5cUzSfhY1xCQhrz1f7nJRWFSkfqIwMqN_DqJf3Y5aunHbW70NqjMVKYmx8i4Go7gMrA88BnszA1I0wX33E8wv4z5z9wQUIaolpZNtY9AxTroU9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foWD6JorfSsTbtrkkV-H9g8U_y0VBnjUnxg2YtaoBETabxt2PRbV618RdVTm5LsIJ2mQJE6zTfhfmFIHWD8hzZ7g-lQO6ar_5g3okn7KxDmqv1fnhnSqZ1PG6gS53oSuMgtMDPwQGQzqw-VijK90QyUNN9qAIcXw-Pcrm15A7ts0CryHFCAENClHL9_1NrcRIrwF2RnvO5tANc4K3r6PkOTTR36DZPZAty4-C0Yv8semk_DbGQBE946CP_w-HLEhhokYKZ_GE2Fcli0mQxEwptg8s8e5LvEJ3NLuMeEFKMDBekVHGmw57VobCIXnUiB7nyuxchh4Ai72GZIkd16ULA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpgqYGliaeIjmKCNizkLrFJLJoj16JbwScJTbNDWe4Cl9H8ZRQB3C_fM2EoQ6AbNZ5N4XZBgR6wpglU7lNq8gI11LW0wx4sFS0GMFr4zMmb37qu_qw099tjOgVzC24BursJzaOlnLI1ojx_1W0dRFu7lnCHAvjTutEeWi9TCmjb0RrOh9W4FoY03EDreej89bIsJxLNl57cFXGEMmOvsNUZtylFTMYJNANvZyg4o_OgeTq7ON9dkASzqyX0tMHYq0s9lGjuXe5aMD6mOvhcDh-K5xYnNAyyErH2aTNmwQqg70B2S1rqDjaDn0EBlbtIg3T3fKRaxOXD_TyYVC-dnbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5N3KMK8G1GQfqd_LiXtX0qGP-qk86JHtX2RqbZnxG8Aeh8tmJ2gV15coJ3ZQTUPuT0sFkDn_4gPwn4UPsIuIQjwL0yeKeclAFd5oKmNnBSLME8mUVVBACFkkg-3RWazbZCpiESdiL5dXwGQRl0kzE5kDgmR9oBR7O8i8BRXZkxGHS_1uMhhLmc1JJnMtEKaNa2pYSLvO-4i_4IL2d4ILpW6sZpcRHQhl-u52soFNwM2dUqlJzQQDAktMaAv6PFipZMtx_7HsMNUEgEqce41NbsXIlLBxT1-613-KlyV3TkWMhVN1C0i60fw9Dup6yqAlY3JvcddRvEmdFlMJEwWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDFl2-sOGRq6M27ZkcEViBZ_a54ZL9yAUX8p1MdDvLvMFZ43dZFSg90JalmwOCppWkTjSGnejiB0ViaakqscQwYL2plTnhGSiGcdKRV12joaG815L0sNiUHI9c-eRPjD5rvVcFVCfAUhW0SURtKJfvja_pCmRm-xExuUSCnwltwHcxJavT5jATjcHVchIyzFonRArJfiY7f_thijbIsGAzhONDwN42UmHeuN1e0A5HpqxQ0TwnlH3OQLOUkpXMZfD5wDZrSwwOSjLne2kLOXQaLhOe-EB-FjYC4972d98XnBjwPCdVG6LF-eNSiPV4qxDxtWZs1gs1mXRQNpiVrvzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0PF5wSgWdNS824d1_K99GYGkM6IHY78_1WgUQ3cbh4tjpMqbsBKLo4ibuLacuU2HHdURO8QaN6o5j241N-28YxDJsGlftgHVshUJ_OnhQF6NI0AR4I92XtIkI3MQcoCEFEljsWjlmdz8rsyLS3HHbFkNSOkm-Ww3NS33uN8eknTJ3HnQtlRVE0j0CzPjKgdy7xbysLDmNXxJ1smpim63SlrsPmNotflS_vEVAFOrsDfWHFSDwknmK9PzDjxGGL6ZkZdFW2MffKVUPuuZd9YGiCmBT7BdLjAsD_6vgx3OH2WgZLfPbdPZRM1OwWGlgRnYm00Xqy9vyLBZapxgyZyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA0jvO3XlnxQamEBYm_03ZIuht9gu1DvEi8MWpQxE8S5Q8r-ureF3SgYi98GYVIJN3tFyOXgcf1jLMV7Ro_a4A1-UnDeNS2OPuTDGCHqo34xB5UI40AJGsfwThSvW4deCZTsFguUaepnYH1n5sZv6RvSHLYGV3abgXVAcbInGRER5ggG6jj4zxNJCi9vNNfcmcgrxEpb2sieYC--w-yy-g0e6a3rS6vLRcFQfhcdRIlHvFYaGkRyC_ANCa498EB9iXLku74bWVHm2i3LwQ9y2K_fVlLJ3L0rGniaF3QjlJHSw-wzlHR-WjHCMRkt6ScBxE8h8E2kDhaOvjggd1FSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qkp2YNdebPD8Y_4G0UcZf5kpaEu_qSxP6e-hAxRDJkmeIHlBt30W5EgOzubNO8Mdwqczibagi33zqnFuRRtNUmg7_QHso56mRN66ELRAj7GMMsfVid-eJaeuU3NFGu1cWzkSpi7Q3t-VXdupNe_sPPasvGT61V7cSm05TXdIXv7iQjpv-nKW5K1mhLzM7TTzNh6bc81Z2Z_qj-XPEObofGp0JvRy15fOoWnWCR4LCvR3swkdSb3BEiU8-CkmHQ-q_c1jgZ36tl9jlUsyMBi9uk3crB7Dop1Ynt7a2k9EeQKaEsAzJNkmksuIlDV-LFdDhei4WjDwka0VY1wXm-8acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-hEqfab1_UDLDj8GxZtUxwGjxLeBp3BqGQy_PkT9bzvxzxxiKXFSZwqF0ep9rWkiP7XBFR7onSz9g-xrtqXAzsoAtLzZ6rCV00gDifg78GuAIDaj9LYxsNqO081XbR23_qPlqAY4AoCOZSXXc3DA_nMtr99qWVK9cqlx-pWlKzyNYs-I2XdqaKpuVb5g69LwmudiIzRWEcOsIXwj0BXjEvkX3vXer95JRt4L8f0xHOZHLwvZRA_ilMGnMxQl4iZsbcyZG9Brn8FdjIeRIWFt-a6--JhdcbyFmuFDwURchr9_fyyZwfwCtgy5eH8BX5EtFWBIAtCUDVW1IuMsUWxWA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=gvd_E0hFZvD118GlBH-lwk5Tpi-feGSP3rJgIkEXEdPNnL2x_DZ8gzq-Rd0eWGtWNjat0qZawA7QaztrU0vODbLGUn5nr324Nhhr-rlXxdwk24j4Hp5ee6Z0h0BMdp84vHQNQhy2T_yiwyK3jARAqC6X1y8XQzG0IcjE-E4V2Bv3JctxtNtjv-hEE8ogENENXajSMFW-QwI3OnC0F4In8hjWZ2Lcp17_ebzFSE-PJmbfEak-QS_jtX0dzdcxedKMcqZFKePnXvsQdlILdNfmNAabDNZ3m_MiTCmBd2I18MfxwCKoHrtrzx-uW-zLOwvrxfMhim_nn-BeBt771gfALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=gvd_E0hFZvD118GlBH-lwk5Tpi-feGSP3rJgIkEXEdPNnL2x_DZ8gzq-Rd0eWGtWNjat0qZawA7QaztrU0vODbLGUn5nr324Nhhr-rlXxdwk24j4Hp5ee6Z0h0BMdp84vHQNQhy2T_yiwyK3jARAqC6X1y8XQzG0IcjE-E4V2Bv3JctxtNtjv-hEE8ogENENXajSMFW-QwI3OnC0F4In8hjWZ2Lcp17_ebzFSE-PJmbfEak-QS_jtX0dzdcxedKMcqZFKePnXvsQdlILdNfmNAabDNZ3m_MiTCmBd2I18MfxwCKoHrtrzx-uW-zLOwvrxfMhim_nn-BeBt771gfALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=oD0GoapXvk8BVW4wJ05aFcAlaPMTGAemdBMrrSEQEBv5m7y4YFsFenGAWl1rDICypHQ8AHUh3tu3j-5dgLFImEppo8NSNQbl0qZoBTjydob2JbmeoKBcy4vL6Lfcx9mFENAppTltYLHeDO8cscX22_aQuswnuS78LXyTp4kHhVWM3PpylHwTFajm7_KADNh95qZpt8rt0mOlExuuupecHDnCyvzlHNO980BZ5sUj6YJBLjgyIq2EMNS41Su7mQrjyxudZTydGbT5sFffMfXob0pAOwgSWuUtpCUupQJ_Vrfs-aTkXgmaE48rJIoreHme7g3rYmpaFl8YXfdN2lI9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=oD0GoapXvk8BVW4wJ05aFcAlaPMTGAemdBMrrSEQEBv5m7y4YFsFenGAWl1rDICypHQ8AHUh3tu3j-5dgLFImEppo8NSNQbl0qZoBTjydob2JbmeoKBcy4vL6Lfcx9mFENAppTltYLHeDO8cscX22_aQuswnuS78LXyTp4kHhVWM3PpylHwTFajm7_KADNh95qZpt8rt0mOlExuuupecHDnCyvzlHNO980BZ5sUj6YJBLjgyIq2EMNS41Su7mQrjyxudZTydGbT5sFffMfXob0pAOwgSWuUtpCUupQJ_Vrfs-aTkXgmaE48rJIoreHme7g3rYmpaFl8YXfdN2lI9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHjQpK3qHed90P4bbuoj4eia3Kz91zzQuYcsNrAcLpgKR_DthYC1kuZJnLAqivncqfEo7PGb0ufTuy0OSR6S93H7xG1CDRggn_odCLEqwuZcUr_gVJali8n-P2fE5KWiXn7RJILmlJ5nRW5VPjd4oFjHpF8wXZ7AaSA95kAblfSpirKf2RE4gLvcD3weyDyoR6TSr9zaRE5c6RAnHap1Ezq9YDyVs7l4l_QONpbDrahJPTzGlXyJ9OxFTWPNMCspnqI8Bnda_rOrXIdiUQDk70WttSCiyDMRuOrWNKUT8q_O8pVYVoNVWT_7XqgInZxQnWqrm2c1IuhkqGHRTOPe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
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
