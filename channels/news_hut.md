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
<img src="https://cdn4.telesco.pe/file/ohJkvxcbBl1svpoh22ptzIfbPgMl0XMzaWEmrgsnZJpNTCho_HFgis0_dxAbh3Y2ik5ra_6q4R82w0G5X_lEXfsI6FBzaDDr-iWzY98DJLGisDiRf60yITCO8Y23QuXs07LIvJNJAhJArDVCpDaUtvHmk3xm-IUlIMU6dv5z2Bj6lTU59IOBsdUAQgEpIZabcT234PBD4LTbLb0Kr5lQTqNS169P_I_l8enRSHcgAOfKXvIAHjbYmXeVVyor4C25gJhOrbN7m177UJIN8TcIgIMTu7Lcn52Nefzy8412r1EZdgBPLdI2UKl_zfvwkULqxea8V3CUxtKjJNwF7BZd6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 222K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 14:14:35</div>
<hr>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8c_sI4bhpD3XlcUC4C3Fm1ONNWynX_9FsHirWI9tlJysgPmAacUXFG0lQnhquIt66zeHGL-GeQ0IglieoMfwg2vSwAMIzPXlwXsDFUOvKFjlj41dAYUeIsWu5x7k01YX4uWNUlzYUem2ELCeJwQCE2sQIrGN3lPUed1dyqMiCpqOX4wnvtnFWoAqLouf4D0Sj60yU24vv4lPkDBPLg-f1jiNRP9RtQ_BdCOQnAUC_C7YKF4ntKSKRLhDvXKPtpoe0_ybSs9vE-ud935cazBLcHcFEABnKpVm28fTmb41fjSefm3HOGUzRFEVWNbv5kkgagXGp0yYQ_wKyLlL5NReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTFKrpLbsUTt3VrGIUzYrmTaC-3UPhAjoqG4JjvP3V9Xhi-2vOIfOA400zctzFX4-9YyztLlSb-QG4AYv9jpqTQX5vx6wcZBUkj70bQSc_zfkSaAtKquHE0sfWtR9Xgv2mXNbPJau_axV-o-eyQrTXxWL4AZ8JOFmVunYlhnrNoyIfTgmACtSyl7AbBpQXaLCooqdrbmq7HFuHsK0nY6y4ajXUNGxdoP6BHe5phIMu_2FAA-968nyloD42hTBtLGWA5A-CabnKpuS7jANdmtqLT8mGiH1wVgDeX_Bb8HQ0ucDu-lF4MvOEjf3EYOIxbAD7AWxeYbOTMbvA4dh4ZAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrQyu_9bC2V9JG69shEaRJbMN-of0J7fvIYlPWMD1wmsx0F5lvAGwcFiZkI8OaLGyHsSdSfb_g66o-0jws8e-gpIGNLwnUpgnVGV5Uv9Ir-9A3b9EJVcw1lsVjfKNONvsWaVVhmdiGOSPm7rrjjXD4ivvIG5bJwWKlqF1-1TC1z7TMbl9RfUjLzraYneSdTUXWgADd5Yn6G9ErylSk0uHqXqPW0iQS6mPRQ6xAjB46hha0ZvaW473aYzVol16gI6B6HFNvoT7G3rreWku8KNlACvyxPX0fiQV3Jx4dCJ2cynGjVb7NUwspIAofQ9IB14z5NX1WKMGbHJzMyTm357EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=P3zHPcDp4y7kSuQqpSOETteZEiaHFpapcbySd5nTztKqeJ4MioYPBYjbmA5GohWPVV-2OkZzOcaZq84mR5u89Czp6-nIbVmH9fTx9UTu9xHBdxSiCu9exf6SjCoLZR5ckH094FAfbG9VXYkWdaaOuwzvXK7T1FC7vLGtUV5L1MFfDbZ2fZaEcMQP44OJhbVLH7jrT00InYA0PpW4SGyG4oH9nnHXWCKovtQ2VGX1k4jgb-52zrQZDEXkDut1CvTqbbrGZguUa7fqxTmTj1aFvUBRaw83XRHJVVggL76yyEKPu9VVLsDv1FVMyoGZer5UgSHKCmjMNIPFJmZC-rorGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=P3zHPcDp4y7kSuQqpSOETteZEiaHFpapcbySd5nTztKqeJ4MioYPBYjbmA5GohWPVV-2OkZzOcaZq84mR5u89Czp6-nIbVmH9fTx9UTu9xHBdxSiCu9exf6SjCoLZR5ckH094FAfbG9VXYkWdaaOuwzvXK7T1FC7vLGtUV5L1MFfDbZ2fZaEcMQP44OJhbVLH7jrT00InYA0PpW4SGyG4oH9nnHXWCKovtQ2VGX1k4jgb-52zrQZDEXkDut1CvTqbbrGZguUa7fqxTmTj1aFvUBRaw83XRHJVVggL76yyEKPu9VVLsDv1FVMyoGZer5UgSHKCmjMNIPFJmZC-rorGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=l-uKTmmoTR276k9YVjapm1sgLq9iAQND-72VzMGsax5QKaEryAv4xqYl8myaHJ4RgdI-pCq31I1NXQIVKA0PFS6Qs66ix2BJlbEu_TTQ01TO5GV4P9eqssy8vR1-7Wx6ENx0Zdixtnl4TZwqniik79vrAAT5AbVzmtR8ecR7JvVNEC0ErarOK9cpWTnlBhNXIuWOkxUEsa1th-_3T8T5dTDInQMiivPpU4PPlQvnJgP-4iLYdZZyR6h9XNYu0gY1ovY-HxzFQqn1Y1O-UGV9XagOCMlMkwrmrMPwLwcIIqx88myaaahEkDIPPKS6x4Tf3By6C73qUibSq9yej2oOQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=l-uKTmmoTR276k9YVjapm1sgLq9iAQND-72VzMGsax5QKaEryAv4xqYl8myaHJ4RgdI-pCq31I1NXQIVKA0PFS6Qs66ix2BJlbEu_TTQ01TO5GV4P9eqssy8vR1-7Wx6ENx0Zdixtnl4TZwqniik79vrAAT5AbVzmtR8ecR7JvVNEC0ErarOK9cpWTnlBhNXIuWOkxUEsa1th-_3T8T5dTDInQMiivPpU4PPlQvnJgP-4iLYdZZyR6h9XNYu0gY1ovY-HxzFQqn1Y1O-UGV9XagOCMlMkwrmrMPwLwcIIqx88myaaahEkDIPPKS6x4Tf3By6C73qUibSq9yej2oOQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=OGqZUzJNCbj8f00zo8-6h4OBbdAq_htvpPBcjTbURB4IOReNWD5nQaQOYoLyqgqTfBeW50_cYF1ySOQOs9O0klPXOn1mkUIOJnNe-xC2fpXQd2N91DZrvDwZRFJUnNs-jUupUv96v658HOYn51ku78m28GzhRN_g-pFOUtLG0BVIFYvOc2CI1A3E7mecFaNP0LRI9s8D-yJlY-PV9FVWi_1fC3l5cDN3LhQEvXMg3TljyEAzVzFOziDnNaT3S7FyEcm5E5dB_vw0K4H-tHGCQeRdrF-BX7nxA2cEfXZ4Ilunpvr8ma1ocFcDcgQ7UO51S0UDXb8a8tmVV3f-w3EQow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=OGqZUzJNCbj8f00zo8-6h4OBbdAq_htvpPBcjTbURB4IOReNWD5nQaQOYoLyqgqTfBeW50_cYF1ySOQOs9O0klPXOn1mkUIOJnNe-xC2fpXQd2N91DZrvDwZRFJUnNs-jUupUv96v658HOYn51ku78m28GzhRN_g-pFOUtLG0BVIFYvOc2CI1A3E7mecFaNP0LRI9s8D-yJlY-PV9FVWi_1fC3l5cDN3LhQEvXMg3TljyEAzVzFOziDnNaT3S7FyEcm5E5dB_vw0K4H-tHGCQeRdrF-BX7nxA2cEfXZ4Ilunpvr8ma1ocFcDcgQ7UO51S0UDXb8a8tmVV3f-w3EQow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=mTyt2q_5NwuI79H5URLbLxIulv5Y2wxjPmTa5Xk6GV5zu4Tjna_DVtYk6tvT6XsgtaD7IRnfqWHxshO5wqUNxCyMGeu6yqE4peEyCElr4RjkXFMxbvTh235z6UM4FzT-BpT5LOsBmMISpDFpQXBg-Kwo-Tvi5an0zxIty1F4wzLDidF9kTsNtz10o20LmqXz_SEtKldrRsToq6wtGi8XsniNebD2YIVEU2GZi7YW14IK82qDO7eUz-e3rVyVgcl6u7RhscPYPGv9NMNSreHkkv08enNYChvaEHMGjQhpewuJzq9jQelgRdAgDpmg8fARIEfkbNk4E-K8KPX3hOiCSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=mTyt2q_5NwuI79H5URLbLxIulv5Y2wxjPmTa5Xk6GV5zu4Tjna_DVtYk6tvT6XsgtaD7IRnfqWHxshO5wqUNxCyMGeu6yqE4peEyCElr4RjkXFMxbvTh235z6UM4FzT-BpT5LOsBmMISpDFpQXBg-Kwo-Tvi5an0zxIty1F4wzLDidF9kTsNtz10o20LmqXz_SEtKldrRsToq6wtGi8XsniNebD2YIVEU2GZi7YW14IK82qDO7eUz-e3rVyVgcl6u7RhscPYPGv9NMNSreHkkv08enNYChvaEHMGjQhpewuJzq9jQelgRdAgDpmg8fARIEfkbNk4E-K8KPX3hOiCSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUqoJ4iOUxQuTDI9k3DMWqxSXpL0MHJjL1pV4eQiOz66lUWSwE1AmTCXK9Q6tB5gHtFCfxGPYj4MBdhO4FcX6TFQFSJSLt3q6vH6fSdBm0q7-Rf9KLcYVXYrMm0rJrgtSUht7kPeLLfcNTy58ng2RYM6Soteui2HhxCKOguB445Be9dVVRAkIHaqfMN_M1OvpzvavVQztecC03tmk0VMjZ0LBsOJLkuUUMUAshLzp7B21ihP4kk3ExW8KDGzjun9txMjL6hVTSpe_NOVkHgT46gWPR86zcgNN40iOb9E85Fnv4TY1tUcJrVzFNmKgqYPSThYNGIg44B1V67IUdYWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=NOoE_K6gSOZbFGFlQRl8hvZTi9Qw-43OKUbZEMtPx54VHHYdmZQminRSmKTRLrMVudwarKAuIY4Qgs2Zo1bO9ryTtFCCNUo-vN4iUibdwXCNlalBa8COcz9XNyLy1eNyeEg_F30wwTH7-0dEUCtkKZUhPpiST-M5SSQbIzzJ7r75v76vXgIh0LPJ7hQnusb_BIiz6wD1DwC6glb1bLzlBRRsO1_GZey9ZaX_Jf23DHKekVEPPHDT4wc-j2Ny_sQYhzJ7ASARVwLhlPDJNy6tbF2SIHRbem1wXYZ1YNca0JVaTdpacEwEko3N2xWuE-Xpxz-em8J9IyDNxDXkgOQK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=NOoE_K6gSOZbFGFlQRl8hvZTi9Qw-43OKUbZEMtPx54VHHYdmZQminRSmKTRLrMVudwarKAuIY4Qgs2Zo1bO9ryTtFCCNUo-vN4iUibdwXCNlalBa8COcz9XNyLy1eNyeEg_F30wwTH7-0dEUCtkKZUhPpiST-M5SSQbIzzJ7r75v76vXgIh0LPJ7hQnusb_BIiz6wD1DwC6glb1bLzlBRRsO1_GZey9ZaX_Jf23DHKekVEPPHDT4wc-j2Ny_sQYhzJ7ASARVwLhlPDJNy6tbF2SIHRbem1wXYZ1YNca0JVaTdpacEwEko3N2xWuE-Xpxz-em8J9IyDNxDXkgOQK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=hkfBz-zGtSfbvRuxM7kWiQPtZro56VDtwpUAJ4QPcC6Mntv5ymBHtXYNtQpazr1t2mivUaCdI4FRfR_GU4wiDs4RWz5XJhHHioABysseZTcIjuRzLHiagtFJNuTkVcozEz9SHWtcXJIbQPLDsONbgYqMSiY8qg33_sK7zYpY2nNk8Iic_393au1wbnJj_1Zi58NLvdccGKErMvWT7dW2mS1FxNJn94a_3pSwcvsbYW1OYvZYfnZ2jswXcR0iSy_-ZoL1IVtnH8DoT-9HBE8eKz7rH1ObfYo1OVGTL-41l8TlSSkVGrsQJ049LyaudXuVtFLdYl_WjCoXidaYPdDWzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=hkfBz-zGtSfbvRuxM7kWiQPtZro56VDtwpUAJ4QPcC6Mntv5ymBHtXYNtQpazr1t2mivUaCdI4FRfR_GU4wiDs4RWz5XJhHHioABysseZTcIjuRzLHiagtFJNuTkVcozEz9SHWtcXJIbQPLDsONbgYqMSiY8qg33_sK7zYpY2nNk8Iic_393au1wbnJj_1Zi58NLvdccGKErMvWT7dW2mS1FxNJn94a_3pSwcvsbYW1OYvZYfnZ2jswXcR0iSy_-ZoL1IVtnH8DoT-9HBE8eKz7rH1ObfYo1OVGTL-41l8TlSSkVGrsQJ049LyaudXuVtFLdYl_WjCoXidaYPdDWzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=tM3nc8jODxvczAHNyyUZbU4ecAsazZIOkSnDW_tOW_T42riGwtPYp9e7Gu67vLO0rhLtJmbUiEgcHNEPdr9-VITh6IRtXISRQDDciwOAOvOZ2UW5k3SXwrEudgk5XUtCjBeoYIcfaEl8m8lYCkAu_FwZWEStcBTMWOenpjNwytj_rYqbecCQIlPdiU-jOktn602exo6bGRe2ZZoR7ZLVkWsRK73tIjkzGetD1mtEMbKPqVjA0m1sBMpbJwp-b4Mft7PXn2PnJGQAmMNM0iByovpGeLl4a6eXhzG6AN6TYNNHProhoGzQ6i5lAXu-kM0_oOVIJ2aXtCui4KCNkWaPYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=tM3nc8jODxvczAHNyyUZbU4ecAsazZIOkSnDW_tOW_T42riGwtPYp9e7Gu67vLO0rhLtJmbUiEgcHNEPdr9-VITh6IRtXISRQDDciwOAOvOZ2UW5k3SXwrEudgk5XUtCjBeoYIcfaEl8m8lYCkAu_FwZWEStcBTMWOenpjNwytj_rYqbecCQIlPdiU-jOktn602exo6bGRe2ZZoR7ZLVkWsRK73tIjkzGetD1mtEMbKPqVjA0m1sBMpbJwp-b4Mft7PXn2PnJGQAmMNM0iByovpGeLl4a6eXhzG6AN6TYNNHProhoGzQ6i5lAXu-kM0_oOVIJ2aXtCui4KCNkWaPYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=IwrTUkyt-LyXeU_S4_zZqlbuMxhy-Z8UBt6c5tE4OlLvRMlFUJQrHlIYFemEqsqlo0F8_u0NueqPNNjG-AyXXQenx-q34eghUFIY7agZ7GJMxrL0qpufmVUcq8EoijBj79t854b-NMVP6mMCtCUqyrBiWY7QwpkTqRlmsyeb8AotVFJkzOG_J8jBAhSoXxvcK85stEqoQLky6wTa3qhzpieJlMWfjRNfyEh0IFTGQUwpF-ET-zMV4NJmWE1XNzVr7IW_jW9azdpiGs6DFBgNiM9o0xzteN64e_JeDjJE0VU_LsbE--1GSrHpFC4BlRGvrmVY6A0WO9grdC_c-RpgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=IwrTUkyt-LyXeU_S4_zZqlbuMxhy-Z8UBt6c5tE4OlLvRMlFUJQrHlIYFemEqsqlo0F8_u0NueqPNNjG-AyXXQenx-q34eghUFIY7agZ7GJMxrL0qpufmVUcq8EoijBj79t854b-NMVP6mMCtCUqyrBiWY7QwpkTqRlmsyeb8AotVFJkzOG_J8jBAhSoXxvcK85stEqoQLky6wTa3qhzpieJlMWfjRNfyEh0IFTGQUwpF-ET-zMV4NJmWE1XNzVr7IW_jW9azdpiGs6DFBgNiM9o0xzteN64e_JeDjJE0VU_LsbE--1GSrHpFC4BlRGvrmVY6A0WO9grdC_c-RpgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=b7gfrBqAKQ-Q5gaj2qefWY0zfMDE_OksJytD9fD0VaR9BcdLThEpi36m-b2tuYAXTDdXo_mT_RHNYQX5hpRzmBR7O50vJsHmxlibK8A5tj1PryaSz53leaFWRUti6n_-7ysgB_L8iU-7pElulqB6F__Lo4-KtxLXWm9dwCRx-D3t85mMF2yXha4IjSnN3uQRst8JmGQwEoF4c04Y774vO4GWrZXitbEGOLR2eiVaHynXXbohnQN58CgqdPUyeej1emoi0wKs16YHsGVkyFp0wjQ8QbDT8ykFAnEakNiXM9qAu4rQI_Pnzr3AnF7jd6VJusIYXiGbrXkXRZ2nh1LFKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=b7gfrBqAKQ-Q5gaj2qefWY0zfMDE_OksJytD9fD0VaR9BcdLThEpi36m-b2tuYAXTDdXo_mT_RHNYQX5hpRzmBR7O50vJsHmxlibK8A5tj1PryaSz53leaFWRUti6n_-7ysgB_L8iU-7pElulqB6F__Lo4-KtxLXWm9dwCRx-D3t85mMF2yXha4IjSnN3uQRst8JmGQwEoF4c04Y774vO4GWrZXitbEGOLR2eiVaHynXXbohnQN58CgqdPUyeej1emoi0wKs16YHsGVkyFp0wjQ8QbDT8ykFAnEakNiXM9qAu4rQI_Pnzr3AnF7jd6VJusIYXiGbrXkXRZ2nh1LFKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=MTHfaxlGCssuos9k2MAgOgonjB7TufQ26ifK7QgdZG3mwdetwbAFBp9-6pJUd7zrKYyCdBb9lxGSnP5T65ugzsEHEZf3Z8fYy9lSiiu6v4UbsQN6r1HfJa15NwbC4hBwwzX2R91HDfMcCc0ZDLVaspmN_Kw9F7DxSmK9VvqgK4qalHxs9JFK3ZrSF02UgtXh7jIA611aHrztaBTAKyzAuRTJCm256_IC0OYo-m5k7C9W9l0WW_TPab-EUOpcDno7KKvDddSoEsL_5bMgv5xM4YEIlw3x_oJVafKRX01fTNb4TZSd2fioYCKvOiTmVHdeD9wntEJgc6NHO-5rDsA0dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=MTHfaxlGCssuos9k2MAgOgonjB7TufQ26ifK7QgdZG3mwdetwbAFBp9-6pJUd7zrKYyCdBb9lxGSnP5T65ugzsEHEZf3Z8fYy9lSiiu6v4UbsQN6r1HfJa15NwbC4hBwwzX2R91HDfMcCc0ZDLVaspmN_Kw9F7DxSmK9VvqgK4qalHxs9JFK3ZrSF02UgtXh7jIA611aHrztaBTAKyzAuRTJCm256_IC0OYo-m5k7C9W9l0WW_TPab-EUOpcDno7KKvDddSoEsL_5bMgv5xM4YEIlw3x_oJVafKRX01fTNb4TZSd2fioYCKvOiTmVHdeD9wntEJgc6NHO-5rDsA0dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=OR6nQOY7uTzlOpYyZDyRRt3pcdv1G49NH8bwqnxTpBuXRHq19dG81T6bIQhHGkHeeIUes_CWJIqAsyLo9SS93vDfRGAXcYu1rqfoWtTPmO1gyYSBYf0vjb1bQpy2u6ziPqyDFqHhOUBUAQ8liqqFW3hcaQwv4yg4No0yfEc77Nt7L52h3F2HHzyUomq0Horihr1VwqZTXyEtdzphbB-zvNxTS-TQGQFt8lawxh1Z5H0axryJ5Z2oILzTm1sLkMZ6UAxw1Owxyw8qy9NarIElhEAHClB0-FUFX_4XdQ1_08j3iSATOIUlikj1hHWeEIgYr2T4sFZCXlfZt2dyMNkrbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=OR6nQOY7uTzlOpYyZDyRRt3pcdv1G49NH8bwqnxTpBuXRHq19dG81T6bIQhHGkHeeIUes_CWJIqAsyLo9SS93vDfRGAXcYu1rqfoWtTPmO1gyYSBYf0vjb1bQpy2u6ziPqyDFqHhOUBUAQ8liqqFW3hcaQwv4yg4No0yfEc77Nt7L52h3F2HHzyUomq0Horihr1VwqZTXyEtdzphbB-zvNxTS-TQGQFt8lawxh1Z5H0axryJ5Z2oILzTm1sLkMZ6UAxw1Owxyw8qy9NarIElhEAHClB0-FUFX_4XdQ1_08j3iSATOIUlikj1hHWeEIgYr2T4sFZCXlfZt2dyMNkrbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=SYkaDuzatfvNAxLA3tPDNdap8-5JAAEmRUMA3_0k60_OdfbwejDg614k50bqqtpouyxqwTxkf-X-q6TqkleI3o71mmrE2YlCItTUZNKm02ezU_05Z_jwGuehce0D09KHSSSFpDMcho2sTOUFBvK_jjFksmMLhydu1I2v6tj4ZfruF956mpwKhP-qt6zmjCWleIR_oRshGymKmxCVSc00eVbJzyhUUzYD3RW7zhUlvoXgh3c8vPhj5bJqjgrTqC5CjbTYUF-3bHdbnjlTCrcj30MH93m5Q4GB-We6XVZpNSXTzanATDoXf2waevS9lRIaNlNXcA8d4j3uOduCc9Mn1oTz5c2kvlNh4xWOh2wIYYuLm9koViWfktgF-LbZkuwmIxLCc6tyO9WjjS5XppFZ3bL-Lgr_yOdB-ODTudtUkx6QS9l52CkouvjLXWpMJC9bgkL7UXB1UOvGVuD4lo6qhUgXoEeWwbMqjk9TOH8ScUOVLf6_v_v5ZeTe-MLyE2mVEeLONqiP1hPvrrFJ2MS6F_v05orkmAsM4TmIlm0rX3EQkJPJ6-_06eUzr1fW88jwkpDOH0bKdaFgx2HaGGjix-7Yls4Lkn2IfaVvZr0ZOEWMHxfxBjPklNhBMFcHoIHUDaXPPZu9dzRhydIAACpqYOHxFl-Tjio8dWN3n6XJ83o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=SYkaDuzatfvNAxLA3tPDNdap8-5JAAEmRUMA3_0k60_OdfbwejDg614k50bqqtpouyxqwTxkf-X-q6TqkleI3o71mmrE2YlCItTUZNKm02ezU_05Z_jwGuehce0D09KHSSSFpDMcho2sTOUFBvK_jjFksmMLhydu1I2v6tj4ZfruF956mpwKhP-qt6zmjCWleIR_oRshGymKmxCVSc00eVbJzyhUUzYD3RW7zhUlvoXgh3c8vPhj5bJqjgrTqC5CjbTYUF-3bHdbnjlTCrcj30MH93m5Q4GB-We6XVZpNSXTzanATDoXf2waevS9lRIaNlNXcA8d4j3uOduCc9Mn1oTz5c2kvlNh4xWOh2wIYYuLm9koViWfktgF-LbZkuwmIxLCc6tyO9WjjS5XppFZ3bL-Lgr_yOdB-ODTudtUkx6QS9l52CkouvjLXWpMJC9bgkL7UXB1UOvGVuD4lo6qhUgXoEeWwbMqjk9TOH8ScUOVLf6_v_v5ZeTe-MLyE2mVEeLONqiP1hPvrrFJ2MS6F_v05orkmAsM4TmIlm0rX3EQkJPJ6-_06eUzr1fW88jwkpDOH0bKdaFgx2HaGGjix-7Yls4Lkn2IfaVvZr0ZOEWMHxfxBjPklNhBMFcHoIHUDaXPPZu9dzRhydIAACpqYOHxFl-Tjio8dWN3n6XJ83o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=GOwGETRcNY_j_zgpQrTLRL5bf8vUElgL_weQhwgsdTgl5x-rCyr8QkOhlFg0SLY7TWlschYqqVj97viky_kHKTZc27dQ7s5tq1RmNaTwB9RfgRG6uAa_8g70x5z63JzAyx0fBUdGkyQuyJTVI_4uef6S-nNn-2Ipqnk38qT9YSozeEQRxqW-pXSCG3I8hcQ-lTj-vJMy4LlFnHN4u-FY9x97zgIQJs1XW8QXs25_ztAzp5Yd6tyXD-gXo0TJrfLsn97IFh8ewfGlpeVdu5gJlQ-JNTH_-kYljJm4a4P42aInQuV7aGpRJlbJCERLeAwqLBadnfLhl9_TRRxcy9RJSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=GOwGETRcNY_j_zgpQrTLRL5bf8vUElgL_weQhwgsdTgl5x-rCyr8QkOhlFg0SLY7TWlschYqqVj97viky_kHKTZc27dQ7s5tq1RmNaTwB9RfgRG6uAa_8g70x5z63JzAyx0fBUdGkyQuyJTVI_4uef6S-nNn-2Ipqnk38qT9YSozeEQRxqW-pXSCG3I8hcQ-lTj-vJMy4LlFnHN4u-FY9x97zgIQJs1XW8QXs25_ztAzp5Yd6tyXD-gXo0TJrfLsn97IFh8ewfGlpeVdu5gJlQ-JNTH_-kYljJm4a4P42aInQuV7aGpRJlbJCERLeAwqLBadnfLhl9_TRRxcy9RJSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=nXHTT8xSUn8cl7b0bT-bFTTZjCFMm-cRaiBV-w2_g1qcSFZzaelfT6UFdIYsr_sVZJeDrqZPGXDYTrFMDNwhWbccyfLGtl6BrQ62VRsfL-5x93crJANoQW_x2QidbkyVEbVs-0LWcsN1OXfXxPKZe6dSk_seuB2_fOOUqj2Hb2cKlWIvHDaf_48Q2naxkAfejf3_dps0Kt6wcllms-0pv1Va_M_Fa96k0iqZ5aCGDpsszIjeqzoHSr3YQfdJaO-x0qgh88vic6kBySbVUCvsOvP-T5VhHtZYDfZBaAOOoO9TGBFuHOQWD_hFYHRf7WKSL6CTB5jVY4DMVuqvwtsOPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=nXHTT8xSUn8cl7b0bT-bFTTZjCFMm-cRaiBV-w2_g1qcSFZzaelfT6UFdIYsr_sVZJeDrqZPGXDYTrFMDNwhWbccyfLGtl6BrQ62VRsfL-5x93crJANoQW_x2QidbkyVEbVs-0LWcsN1OXfXxPKZe6dSk_seuB2_fOOUqj2Hb2cKlWIvHDaf_48Q2naxkAfejf3_dps0Kt6wcllms-0pv1Va_M_Fa96k0iqZ5aCGDpsszIjeqzoHSr3YQfdJaO-x0qgh88vic6kBySbVUCvsOvP-T5VhHtZYDfZBaAOOoO9TGBFuHOQWD_hFYHRf7WKSL6CTB5jVY4DMVuqvwtsOPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=cyOCrQ6mWrFHEOG_Tu0jZCGQ53Sein5g2v-mQnYzGm5IoAHDTVZrtQOsV-oFQHIZ9CdtKhe6Ht2wBoNkZ5TEUuqQMF87B7UbKso7UBlrOABDBmDdkciv4iu7UAyJ5dyk8uWgSEpjEwY4gmulQRaASlmpWJ9b2XU8wL4eBkmD1LhnGji_OZaNPrUnOCCdgs-JgGRvl1i0jYZPz80Ji1h9H5gJPhS9UK2YJ4GpxunfJFP781BZbAZlRhCxzocjt6-LfQJ_HkUhN9eflvnXPdNEKjar-rzSTaISeuUZ6-QoM9uQvDkm90B9xVMbt8SuR9oG3Sn83EUnnU-W-7VdPqwVug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=cyOCrQ6mWrFHEOG_Tu0jZCGQ53Sein5g2v-mQnYzGm5IoAHDTVZrtQOsV-oFQHIZ9CdtKhe6Ht2wBoNkZ5TEUuqQMF87B7UbKso7UBlrOABDBmDdkciv4iu7UAyJ5dyk8uWgSEpjEwY4gmulQRaASlmpWJ9b2XU8wL4eBkmD1LhnGji_OZaNPrUnOCCdgs-JgGRvl1i0jYZPz80Ji1h9H5gJPhS9UK2YJ4GpxunfJFP781BZbAZlRhCxzocjt6-LfQJ_HkUhN9eflvnXPdNEKjar-rzSTaISeuUZ6-QoM9uQvDkm90B9xVMbt8SuR9oG3Sn83EUnnU-W-7VdPqwVug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=dVpsawusysSndHpNlPtVEFnNt5K42uyTfrt5KWULx8mKWOxbnCIVoai_LnX8jE8OgZZlzDlhDTOshvupFxad8QQlambfuwv0gmXZaIUDrN9w37dg37CS2NP_p5DPFgzqYRAeDxnrJqI71yh_kNNi1VL2SOZV2q0hUgApjWgmnYtQS-gjtgw-FQMrI2SfUB_641WlcfxRAj7So_orc0Em1RL-R3rHdGvdO06xSWq3Siczjff49E-IdWazmDl9IkkYC2_LHNUaCY6_Nw2wsLdtg_XZArHWKhWGUAxrpy_6x8KMBprzVUB_vxTtoHwlObHj7mtooB7bW2S0FL9Xmr2QaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=dVpsawusysSndHpNlPtVEFnNt5K42uyTfrt5KWULx8mKWOxbnCIVoai_LnX8jE8OgZZlzDlhDTOshvupFxad8QQlambfuwv0gmXZaIUDrN9w37dg37CS2NP_p5DPFgzqYRAeDxnrJqI71yh_kNNi1VL2SOZV2q0hUgApjWgmnYtQS-gjtgw-FQMrI2SfUB_641WlcfxRAj7So_orc0Em1RL-R3rHdGvdO06xSWq3Siczjff49E-IdWazmDl9IkkYC2_LHNUaCY6_Nw2wsLdtg_XZArHWKhWGUAxrpy_6x8KMBprzVUB_vxTtoHwlObHj7mtooB7bW2S0FL9Xmr2QaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=rJQtavmh-C1JJ-zNFmIx9cw6mVdq2cr5EC1Q5vgWjPHpvc7P4tSRieP7lOru9v3yzPIwGRjMy006mXptALTnVteSLiFQLC-6ZT5rKLI2nQ6kx2kblT2fFrr2D8hfzzsY8kuqK7q1g_qusRdST2GkPdlqzWm_YGzeGPwTkH7UQCM5CYVe6f5MbJW1ZpjayipsDrCJCen7ej_fWWZ_Sn3B5mdG0xq4JN28_zCbWdoSqARTWU_8v_nogHiSM6Zec5frUpmf9VyT-VfwjlNyzVClEfytiRzuqX8fzRksE-bSpHRJkonpSdaBxi8_5wosLQzGV2irKcRRdjjMPINZ9XmANQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=rJQtavmh-C1JJ-zNFmIx9cw6mVdq2cr5EC1Q5vgWjPHpvc7P4tSRieP7lOru9v3yzPIwGRjMy006mXptALTnVteSLiFQLC-6ZT5rKLI2nQ6kx2kblT2fFrr2D8hfzzsY8kuqK7q1g_qusRdST2GkPdlqzWm_YGzeGPwTkH7UQCM5CYVe6f5MbJW1ZpjayipsDrCJCen7ej_fWWZ_Sn3B5mdG0xq4JN28_zCbWdoSqARTWU_8v_nogHiSM6Zec5frUpmf9VyT-VfwjlNyzVClEfytiRzuqX8fzRksE-bSpHRJkonpSdaBxi8_5wosLQzGV2irKcRRdjjMPINZ9XmANQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stibrGSTOxfvPKRrJHRjLXlgpxNxQV5hoAteG2YE3kBTgd5gUYjmGw9Gz6-mE6nIzJGk6-KGeUS8Cl_tTiYqLJm6eZl8FNK8bIVH8C4SvDk4vjLeCPkb47DcCj8o0x7ApsFhLwEknDbIhtSGo9ru_lbHEgE7j7r33aQrDAGveREzaRPPZqetNBujydxqLJr6CQXIM9ws3T_rVCPSRfMnXir26-ET8oycbtEvfEGfFK28UrTL1DCk2kg0bma7BGJvKZrF4xTBvcSVqlxfMRuuJYE6L_iSp5yu_RWBRr-kdQBS9OXWm6mIi-cEbNW5grOR2tENei22queb5OA6Nk1wJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahSJyDEk5E6_KlD3kNsFHKIXDWCio7DVzLYJT5W7r2yI8-ySaa0uVHvCFIG3XZf4Qnj5KtqSevl27jLxPbBSKS-VJ8wtwr2eGJA1iW4icqQ9x3qBskIcIyf5Nq4sW1FnQkU35lyw5LbIRBQrbTjSR8PM2n8Z_WXgdM8IMeVKOP5F-WgbPyh7i_I5n1KeGC6j7IaSdshT1Q2cvJvV3FURRirsJsssL1JEDZU2c6fvnHVsyUL2vtZUIkrMd2hdLFWBsR_CvUnV6mGuKbME1Q9X0BYL6epYxOmEws4GPy4hAO6qqIIIor-xKISO4NN2Du4jWd7aHS39s0Jr6qPhYmgQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9eZBc0aWhlSQO4FvLzGCi7Nu1E_HY74b6NWkk0srNMAM6HZclLZy2Gq8ANt9lTiDkXsKmvJr0A_CaSthgehdXbRXkp8PCbXq6lD3Ny4eN0-E5rYrPZKtA2AIu-vauxPjwUiv_89PQGIhhQDZIZiSXkPsFAalfzmoHoN-0TUs0wvSyrG92n39XwSBu5-rY_2ATvHaMvtcf15AZvXWa5w2yBcUNNtaijQ5mSCFtvEm8_GIYceVsdsJXBJTxYY1hejEUG_Dg_zbjZY-xunCQ6tDjPx0UB33KqDu81lw2fcuo7ICfNH_xdQu-FgOG1YXtI_Xt1rjQVMi7-vLHhKxn8seg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=uHbGR4qFoUcxKbnYEh4Twf6xc6ljN7h3_nLqPTeNly_PC9s_dgpD93XVBJG04zptWPGiLnaZ3NazecECqVsZY-WtIYZNyzsNF3Xg8U5tYBOYgFB0ZVWconT8k10JpTvrLju6iFdWLlTFtinOxZyCl9CMsEOQ2dXX0CkJEXNR6j-PM2B6AlUNsHqrByNiv7bxoKswEabSdkOQmMfJva4tiOnStg1IRy3oFnRKx2LdRa3Ui60zlhzpuAxQSsvrU2gOJysPrBRyyfGVSP_nBt38pUcqYtZ62A7vaWAHsAjY81nV1VU5QVlMSWnsKq7Y2AxcV2VeeqBJ8cu6VJCzbE1uSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=uHbGR4qFoUcxKbnYEh4Twf6xc6ljN7h3_nLqPTeNly_PC9s_dgpD93XVBJG04zptWPGiLnaZ3NazecECqVsZY-WtIYZNyzsNF3Xg8U5tYBOYgFB0ZVWconT8k10JpTvrLju6iFdWLlTFtinOxZyCl9CMsEOQ2dXX0CkJEXNR6j-PM2B6AlUNsHqrByNiv7bxoKswEabSdkOQmMfJva4tiOnStg1IRy3oFnRKx2LdRa3Ui60zlhzpuAxQSsvrU2gOJysPrBRyyfGVSP_nBt38pUcqYtZ62A7vaWAHsAjY81nV1VU5QVlMSWnsKq7Y2AxcV2VeeqBJ8cu6VJCzbE1uSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=HZ1ny79WqXqadHQO4GvfGtzVm6bgX_OnjJRYCUfF_013AZv7x5DJocAgcYlbZG27550_XD9whCpas-iT78wDa_sdUaU-_ZlcFtM5KL9xQp1nWBLUPC_nsVJdamwDbQ5mMwdDjT4pXZOEXkDppNdOxraFa8FHNRRXGSo-MEDiNpfpt7ZuELtQaVCJuT8mvgP8-atIZO2NTLuTqUzS7FNPbVsNNbwXtGTleWMgqx_aI8R-79Jd8o9CC9dYdYpTcGwL5KpyOGKtibGlYVRxLfTfTTlWQoalHAK7LwLemaGFeIouy-EtX0pe6e8AeIC7pWv6yMm7tNvDHHouHgrHVYX2OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=HZ1ny79WqXqadHQO4GvfGtzVm6bgX_OnjJRYCUfF_013AZv7x5DJocAgcYlbZG27550_XD9whCpas-iT78wDa_sdUaU-_ZlcFtM5KL9xQp1nWBLUPC_nsVJdamwDbQ5mMwdDjT4pXZOEXkDppNdOxraFa8FHNRRXGSo-MEDiNpfpt7ZuELtQaVCJuT8mvgP8-atIZO2NTLuTqUzS7FNPbVsNNbwXtGTleWMgqx_aI8R-79Jd8o9CC9dYdYpTcGwL5KpyOGKtibGlYVRxLfTfTTlWQoalHAK7LwLemaGFeIouy-EtX0pe6e8AeIC7pWv6yMm7tNvDHHouHgrHVYX2OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5MZauvipXnUV4UhKFglyERVQHtyjKZ8betousZYMgPEiyaC-ZoXkV_AgCwdo-SiQn6CNDCC0NJjt1wkKPSMFrLwhgHulZ-F-R7HVWF-673twU0ko6UTjkTD6rZVp3HDCKPxnD1vwwd-A-V6PnUQrXy-FAPlK4SDm6dAvJJ8zr3Wltzbi2nyd-c4bMpmfYEhkuT9y7kq8dfUz1JB8z_1J4JfrwSc0Wf0gr8cRRTQs9TbzWtrYZh4_6hEpLOJAg9BcR_96UmZje-fVYX0pntHTqjfvvkSzlL70RJS2JqJcPmshr6T0i87mTPt0ngCx46LuAdziCbXQbhdc50j3dJNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTFIpm-oU7auqMnDnkohQ3gQL0oI_aU-DTMYahjzBDMDb4Vh0G4PAImhSVDgAWkqdyiYma-fwUkM2hVM5lc-_DQErI7C_ZznX4Lj54Fzz0MVnbojR5HoslnCMf8Auo91vKxHMXuqQNiG9AfpZxtY0yvISD2h78BYi7TM2QDpFPMSl44DmefKE6vbvpsSd8KJ6N162jh2X0wiFqU7cC2MVoAXGCxjAMXsb9b2QPuzEC8MJFYA1ui27aLkHaxAXhd3cLGF294baG4Qc4tw4IjNoZZgQ6IotsRTPIm7fbo8IG__s0zry8hPjdKPflablcoD9n4czWry9qvttX82Xofq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=pnmVVG4KT0oKiizdxDbuhzySWfOotzHRr_oSB8zXSSGw3g585O-nOSQoKaRhWTa1PW0MCjRHB_LwkB0xICaiR-iQjcRG0T8lSWuVmKhGakXBVSX7rd6rBmyhsyPUmi5T8NworkagE017_aLRmuK6wRPiLo2tGcIWcbc-h_74OuNjJLEYw5GfBCBqh3jIodtStuuAMNJtk7quiLkWCdIdkyXesy8_MToUR4nu3ZCFUGPEQ07MCFLkdTaf60n7MyMTkf43pnR429uVegvazRovNxAbQx0FQShYuZtx8lqDckIEypGldtSCAKLF-W-ObG40nJhDMAuUVU696ujupNwW-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=pnmVVG4KT0oKiizdxDbuhzySWfOotzHRr_oSB8zXSSGw3g585O-nOSQoKaRhWTa1PW0MCjRHB_LwkB0xICaiR-iQjcRG0T8lSWuVmKhGakXBVSX7rd6rBmyhsyPUmi5T8NworkagE017_aLRmuK6wRPiLo2tGcIWcbc-h_74OuNjJLEYw5GfBCBqh3jIodtStuuAMNJtk7quiLkWCdIdkyXesy8_MToUR4nu3ZCFUGPEQ07MCFLkdTaf60n7MyMTkf43pnR429uVegvazRovNxAbQx0FQShYuZtx8lqDckIEypGldtSCAKLF-W-ObG40nJhDMAuUVU696ujupNwW-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=WsWHKlFvbq5covHZgm5KL91Uzm4SgY2m6DZg26zE-BrRJp4jF5rZG64eLmNJ7YMg-WJFR7IZbwSMqc1CkLfzOQ1gGin7K_gJqlquvcLL4NSecRgsl-D2T1KxTyd5AO4LT8i7A8ZyyuWopt57VWdm1Vgf8H2Ft4HxdxnjtfepjXmR61WbOhsQtz7Xp1Ret-CwyU6rme16ogrTSynR8W8w-HO-6xdo1ogWaoVKxj3lMIowgguTd5uNXHf0BBoncKfMMoQ9qAfRQGVEi-kbIArddZ_sZa3LfU_Yrw4Ns7smYq-viYYUmDD5FMkO9Uq5aoIrAoThMRopbqnIXhLxhpDL9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=WsWHKlFvbq5covHZgm5KL91Uzm4SgY2m6DZg26zE-BrRJp4jF5rZG64eLmNJ7YMg-WJFR7IZbwSMqc1CkLfzOQ1gGin7K_gJqlquvcLL4NSecRgsl-D2T1KxTyd5AO4LT8i7A8ZyyuWopt57VWdm1Vgf8H2Ft4HxdxnjtfepjXmR61WbOhsQtz7Xp1Ret-CwyU6rme16ogrTSynR8W8w-HO-6xdo1ogWaoVKxj3lMIowgguTd5uNXHf0BBoncKfMMoQ9qAfRQGVEi-kbIArddZ_sZa3LfU_Yrw4Ns7smYq-viYYUmDD5FMkO9Uq5aoIrAoThMRopbqnIXhLxhpDL9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=U4i5xxx-z49JyH7f2oBmg4Tw14dAM_g_kJ6fBHUh4RXmoJ5n39EmlUT-PEVBV9YcY-zqrzP8Op58weuwxWKMw8swMdXI6rfz3QgEribKefmRKWDw4Z12bXr6cFzL0vS0M2oev2pXXWXxzb1Y3qwf4-6HBGkGPJR0jp_ovl9EoR5M4RI3fGO-5XGqskeDUXeyeNk6BNxll3WYdEIQs6aLXkWaDb4X-FZNVmPIAPzSfQAEv4Ad5rEmvZueyhe8X09OGWsKwr1E5CPq-XiGddE-zZKC1Nd3tlh6cWmFq0jKL9J8MOOzeMeUfX8qjc9ExK6QmgoNJObXUvLG38uZX1Pb6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=U4i5xxx-z49JyH7f2oBmg4Tw14dAM_g_kJ6fBHUh4RXmoJ5n39EmlUT-PEVBV9YcY-zqrzP8Op58weuwxWKMw8swMdXI6rfz3QgEribKefmRKWDw4Z12bXr6cFzL0vS0M2oev2pXXWXxzb1Y3qwf4-6HBGkGPJR0jp_ovl9EoR5M4RI3fGO-5XGqskeDUXeyeNk6BNxll3WYdEIQs6aLXkWaDb4X-FZNVmPIAPzSfQAEv4Ad5rEmvZueyhe8X09OGWsKwr1E5CPq-XiGddE-zZKC1Nd3tlh6cWmFq0jKL9J8MOOzeMeUfX8qjc9ExK6QmgoNJObXUvLG38uZX1Pb6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=DVgGudyZp8ELr7WifMop4T5kK4Z5nMf1qz3l2cw93NxLmAqOTs6FE1AcaXz8R1rP4v1FdjFjDny_MbiBqOeirwToM0j3iCy_s183YhqE9qCuBWOh5Hjq4rwN41ItLgjtaIllAVKL_g8fbF70nAdeOh1jINLPiDrJUwvGmFrAAqiq5lJo_VtE5Ef5_AWrp9c_kEitb3fxYVa74QgkryDrECqQLEWefP2GOdPM617sDtZBAWn1PJGWlZRAqG_hHrFoXCM5R0xt-Lx5nSbu7JCrn6_5_qEw5VRqKHIpxWwP1ZrUUxshVwUVMwQv9OntATKSyijcHBCbdZ4kHcRcnZ8EOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=DVgGudyZp8ELr7WifMop4T5kK4Z5nMf1qz3l2cw93NxLmAqOTs6FE1AcaXz8R1rP4v1FdjFjDny_MbiBqOeirwToM0j3iCy_s183YhqE9qCuBWOh5Hjq4rwN41ItLgjtaIllAVKL_g8fbF70nAdeOh1jINLPiDrJUwvGmFrAAqiq5lJo_VtE5Ef5_AWrp9c_kEitb3fxYVa74QgkryDrECqQLEWefP2GOdPM617sDtZBAWn1PJGWlZRAqG_hHrFoXCM5R0xt-Lx5nSbu7JCrn6_5_qEw5VRqKHIpxWwP1ZrUUxshVwUVMwQv9OntATKSyijcHBCbdZ4kHcRcnZ8EOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzxNM8qssq1ooanJCFv9UPozglsS0_bmvVdIwPxGD_h4bNa34O_kdFYpa4bdQVkE3aJW6WPSzAQmPpUFfdeVshX-4EyidnBuwohkBUsyAn3puMEGHody7VD4Yhrm-lni10ta6Y86fyTtQ1wiLexwzroO1aQZdylLrlSyDb6nyOzrZTb5tyAZCuSDl_w7zOYgfogi9Zq6WwOAL2CrgLfmgYKF5Qhn3IUduAEVDsHWeJhBGCsTqUG_U9AXVRMgtTrp-rxwSQMiTpeBIIdwiwfIzlIEYlkzrZlHXL4aWb1BHpNpuutPQq9H7iIoYmc7t0WffhM26fFrTrVc2ucUqyuCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRi4pOxzcqct_4oqIbAy8VNurCl_wi4fHwFGqBbtMBZTK_pm3y-qko_EV9kUS09xFp1ehbXEL5HLloogancDE7olhvCo3cxJ1XTRo6Hqkji1uYRpKGCjGLQCBzV_1rV_6lEdBVz7kHveFPaBJpo-OmxlRDxgfNvK4eRHn7yM5MEkpEkv5Pevx30dUMK3IL05TMua-8LzW7lOa9bBY_ggh09kWZK03IyrbzNWq59aWlWi9jMcbXy0nsRykfvpcBLLVn1qHlABG69nj3II1EdSS3mGH3AoX3BQkCSp-1ru8Thkpusq-7eLIpHxbxZIj9Zlv5JiiKRKPDTN44_Cn8T7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI_6d2j_0wiqH4j_vuvq022nMaoRdC3wWQEYAF-I8EmfGVIdwJN-wxdNAWvFsS3SITEfz1zgSyFoV8iUiLI5SujdF3vsiAc_zYyI0cBby2517GKOHd-Dyvm_Z5nHLKUoqhVfgkMYSGHKZN7F3pLwNIQBnJAVHS10IO9XYePfDVGdWfvo85odiqf5r04iyXDjvxlcQSLW2Noknek8UbV-fOdxV2Eot1WLTQUS0uK9lMSVl1sJrMBCfekIDUWiXqfUUcTGeCfRJiJS5l3mXH-YHyNEQsQEKKciumKckX79MCX1NavJPT4vSSlX-kaMITZvxBPLW5miil4PMcqRHIO2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyN5V7AF3tA8BrsEFiChWXdy8yWRahq32a6s5aD6Fz-InXXvfECrmbjjS66fDzOYeIlzchd6gw9bidvt714u3Lxu-27IbuZNUbkOeUupElYks0xbjxAILKnPdbBDAVFn8tlZX3wxinpN36jFNxJ3HQp43ktd2ziV1Tz9CAZ4kB9Y985N78MDYiBkyUlb95Tjh8dzo8HTNo1EAeUtreRsp1qf3GHYHR0GntHF9AQGeef56ce3TOsqKL2EOHTlzma8KD5nTVYpqkUAAjeAZ26GmEmF5X2VZ7WIyLWmVn829nn5-sFLBjiiQtf_Kh4_YgOh4zRELpdA7s-Gh5ldZQ4DPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdnhC4759XBRu43N_YR5n6eykM8vNrnrx5PcReCi3IgJ3BsajKA3CSZNuqUayqbvxk3iPEeY9llmz4amxhP56lh-FNPsECOP2plBn-fiUFAjuNM77NuoZtyyxv_IaoCZikZMktH9DWhr8yLeKTSEhW5k5BTTHhishspiF1hHyvtlgpIFC6QI79ONt8_oK2jTGVDJ70YjUDVNhrzJcqzpcAQvJ9s1L0tJqkY6hUpRlLUpiNTAX-5gr9bHEN_R2O19S3yo98xSJXkKDJV67lcROPmZN70DG9gjSwLPAF_UGbCncqxgd8DXIqr9lOGtkPHUpJ0AmawdEi0HisoC53I2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=O4RNm2G31wZJ24O0J8nos_Mp0R_vhCBGQbduKe-eR7yeFYLy4P4dEbp2tNdJUDLC2R51m55APs15Nk0Hn0AVVvHQlzxA34nTsghrRNo6Ab_maN5iky-9SkHoh6RqwYQEZbFL05hT__FGKKL5hEtvu4EEQRzlHgNkUOSLDYLalkYJ4qVVd9KPfvJJrWAGc7z9v0hl19CmPKI2i14sztIUX3o7S7843-BJLjFDiCHXIMVsjFrvgG6mfwNtMf-RCNdTi0VtmkYrY-zQJ_wjNejskajoUlHWvFfBLuQtIgk6k50kNxulIgnZuZrSJ1T_QUMXRP5Ks0jLtMqwC0424q_mRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=O4RNm2G31wZJ24O0J8nos_Mp0R_vhCBGQbduKe-eR7yeFYLy4P4dEbp2tNdJUDLC2R51m55APs15Nk0Hn0AVVvHQlzxA34nTsghrRNo6Ab_maN5iky-9SkHoh6RqwYQEZbFL05hT__FGKKL5hEtvu4EEQRzlHgNkUOSLDYLalkYJ4qVVd9KPfvJJrWAGc7z9v0hl19CmPKI2i14sztIUX3o7S7843-BJLjFDiCHXIMVsjFrvgG6mfwNtMf-RCNdTi0VtmkYrY-zQJ_wjNejskajoUlHWvFfBLuQtIgk6k50kNxulIgnZuZrSJ1T_QUMXRP5Ks0jLtMqwC0424q_mRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=jQCA-Lt4ddKPHISFRH8ntyKjkCwjYT3icZx53EtqMhwTk8-v8oPS-ec35DLoXdJpU6W8qI1R-AEwpqH86Gr-uTSsbGpwklcrGy5d2WT0CHzcAWN_nD26BAExGth0v1L71ESlHv-LFjcZNpz1GYhaWRjCOIOt989wSLfJbfYEs_BlFjMHNsyinibQq6T6IPkp9Cl_9qXZxB1Pr67ivpA-jbY_cWcEGLyikzvnCW1nB7piZ-DdH6fRzp_KUOv5lV86XkLJ72ZOJDhz-MUxbCrAtX3mLre3SD3QyXx_iGB-uqHqO5XuWcluTgQQUgfZQJL8FA3x5vBCejbUfZzs6FKseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=jQCA-Lt4ddKPHISFRH8ntyKjkCwjYT3icZx53EtqMhwTk8-v8oPS-ec35DLoXdJpU6W8qI1R-AEwpqH86Gr-uTSsbGpwklcrGy5d2WT0CHzcAWN_nD26BAExGth0v1L71ESlHv-LFjcZNpz1GYhaWRjCOIOt989wSLfJbfYEs_BlFjMHNsyinibQq6T6IPkp9Cl_9qXZxB1Pr67ivpA-jbY_cWcEGLyikzvnCW1nB7piZ-DdH6fRzp_KUOv5lV86XkLJ72ZOJDhz-MUxbCrAtX3mLre3SD3QyXx_iGB-uqHqO5XuWcluTgQQUgfZQJL8FA3x5vBCejbUfZzs6FKseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgrmP6NfRdY0ujvurTZC2ofhW3Ty5BjPoZe3SlEl_TfPoqmuJcTsNQvdnPVa2rNFATipGfW9I1SBctcYYM0GOZnZuLukBw1n_GjtkesqIYUm_ubl9Az2-QMB8IHGE4BiuYySB359T_EMfggTwBhJrG3_YuQs9dUD2GwG4kkwIwhXSzFt8nbA4zDbBpRV34Np8KdVKZLlx4_D1_CYFI_pZgGulxQhn6toDk-7EsXyzx_64yiajdZrt-_hFYqK5YAcTBO0s1RPJhrSyrWz718eOFP_zc3AfXGiYgzybLVCgio3rjw5LTM72-r-Ie34sVqcU2rkwdkpKr5_JpF2OZp1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsV9ey1y_IwDaetBo7NK1K3Wupohuco4Lbz-TAJaxAAw-HfHq-s-2zYIrZY547ZtO_yD4hK808Q4ZD77Si81nRKNaUDIHgoZhtieK1qCyv0FMMW_936JT9UIqneuae6Nj9iLqeDiZCPUWrVN57eWlAREDMOa2EviRIlyyQLMagqAeSRzcUEwxfL0BBXSObPI40rMTdjcPWX_SBYKk0FhG0fkKDT0-sI1Th1FuGUj0lkeY_W-ehRN4s9rGPdJ8wg1eRzpK38k56biKLzUx8tsfeXaesnB7ahf1v9xE5ihGfNjiKLgsNjpnIAzjvtiGQw9YeWa9RsL8uitStow83_hug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=MbVwPeagFKILpxP3sM3ojo3at25AJYG1XSkRIhbVVwSyKFkAp8Mhi2fDVLPMjujWpK2PcBnFuetfiEwfAYSR7bUs6FHUDSIzdzkHmC6Q7AWGmkH1rZBzBBBJe33QCfiMi6mp9-ND1C80kv2gyq5XdXO8u7Xv7f258RBlsO4YTxHUcA8Kb-5enUwWkHy1xcG6anNVOxA1tEgaTs5vxGUIFAT-n0R-HYODAD68GbzvY6beTGp1j6rtIakPrVPkDgsPmkEt8eBRzw-oJG8QOUBQKmBEpdLUsF5nhR2FVZ7bDnRMn5wOK7-MLCL-NNXrPqNrOAkGs3FM_g6a0XwN9t2Kvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=MbVwPeagFKILpxP3sM3ojo3at25AJYG1XSkRIhbVVwSyKFkAp8Mhi2fDVLPMjujWpK2PcBnFuetfiEwfAYSR7bUs6FHUDSIzdzkHmC6Q7AWGmkH1rZBzBBBJe33QCfiMi6mp9-ND1C80kv2gyq5XdXO8u7Xv7f258RBlsO4YTxHUcA8Kb-5enUwWkHy1xcG6anNVOxA1tEgaTs5vxGUIFAT-n0R-HYODAD68GbzvY6beTGp1j6rtIakPrVPkDgsPmkEt8eBRzw-oJG8QOUBQKmBEpdLUsF5nhR2FVZ7bDnRMn5wOK7-MLCL-NNXrPqNrOAkGs3FM_g6a0XwN9t2Kvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=X-przmBMEh74ymp6nWvkiWjLEqiHXLIRl3Ll_mvEHK2sHLlT-_9rjF-QO6D7KNb-91SKRzMd7l3V5QqfFogn8mGJVzmExuzugY3PZda6vuLSIUJydm_kxTxn-BT4AVTu8wXIYNkBeB7R9utI6KIunrsoC1tmgOs53DFkbzWqCYkAkCwfVr66SYTK9e-WPJlNVUXnEZB0kaRECvcEAIGxo2EWQrRVtBq8siHzuGyla0CSgcmG15WSDtLuK6DBhXwEKCxtpjGzaBp8tVnqKBIwneCJNh7JPdJRbqTY4WkJvjzlH2NdH-y_14rvl3MPUK9UcpR_eLMIPSq87lU7nkFbCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=X-przmBMEh74ymp6nWvkiWjLEqiHXLIRl3Ll_mvEHK2sHLlT-_9rjF-QO6D7KNb-91SKRzMd7l3V5QqfFogn8mGJVzmExuzugY3PZda6vuLSIUJydm_kxTxn-BT4AVTu8wXIYNkBeB7R9utI6KIunrsoC1tmgOs53DFkbzWqCYkAkCwfVr66SYTK9e-WPJlNVUXnEZB0kaRECvcEAIGxo2EWQrRVtBq8siHzuGyla0CSgcmG15WSDtLuK6DBhXwEKCxtpjGzaBp8tVnqKBIwneCJNh7JPdJRbqTY4WkJvjzlH2NdH-y_14rvl3MPUK9UcpR_eLMIPSq87lU7nkFbCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=fZVlKa_-2fLEZScsdXmMB8LZw5QsUJ0orkXHnC0xRZ39yJ3Y9ShH-6W34kG8GYD2Fv2fddtcywLp3WcDdopbbM4NIerzLVzeeJCMOaAJbuAQxVCkYLDvHq5ublaSwuosckftJcC7PjDEw6VICBjyyusooeDelAFKWyPwUgQ65u7dh6y-NPolBS0rp9HViuEP1ObVDKVKrwJeCEFW_nMhXpXPZehatSQFQCzkbeGHRFtp0jF4aZ59PdrFdHaJ7m-GtI3_JyLEqZQNeMXEbxcSk7RVSfkMObsw5ouwBBuhuZyZ4vzGCJO44F0P93T5KNHToFWUe8uJZ3MPjpnZY-HLMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=fZVlKa_-2fLEZScsdXmMB8LZw5QsUJ0orkXHnC0xRZ39yJ3Y9ShH-6W34kG8GYD2Fv2fddtcywLp3WcDdopbbM4NIerzLVzeeJCMOaAJbuAQxVCkYLDvHq5ublaSwuosckftJcC7PjDEw6VICBjyyusooeDelAFKWyPwUgQ65u7dh6y-NPolBS0rp9HViuEP1ObVDKVKrwJeCEFW_nMhXpXPZehatSQFQCzkbeGHRFtp0jF4aZ59PdrFdHaJ7m-GtI3_JyLEqZQNeMXEbxcSk7RVSfkMObsw5ouwBBuhuZyZ4vzGCJO44F0P93T5KNHToFWUe8uJZ3MPjpnZY-HLMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
هم‌اکنون سپاه در بیسیم کانال ۱۶ دریایی.
“از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66488" target="_blank">📅 14:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66487">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=IB0agrUF1NYKEsBcB9Zh1QzguyVNe4qMakqrpMnP3i-DWY6Ddpmba3eFqdADiqxmH6-aBJXGb0Aq0YNOTrO87g0WTH0ufbpNf-QlIx-sdkkdwzSKqPfBQVF-3Jp_nk51wxiPlhraII4eE98LlyQcnmKnSdWABO98jVAmuzvKJOgy8bnYMDixIUs7bk9wJB7Ol1gPLmC6OGoXq0nqXfl7H7lVGT15HYkYKz3q8leBqxiYQRuBmAQNajCLgFT8EGLVpOaItAkZSt65UetPSVdQcAzyDuN3TZITF9l5bbKrecpiXO_9ILaFcDeJ-tXXDH7NEMvggNXOX_CQ0dnIujZCBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=IB0agrUF1NYKEsBcB9Zh1QzguyVNe4qMakqrpMnP3i-DWY6Ddpmba3eFqdADiqxmH6-aBJXGb0Aq0YNOTrO87g0WTH0ufbpNf-QlIx-sdkkdwzSKqPfBQVF-3Jp_nk51wxiPlhraII4eE98LlyQcnmKnSdWABO98jVAmuzvKJOgy8bnYMDixIUs7bk9wJB7Ol1gPLmC6OGoXq0nqXfl7H7lVGT15HYkYKz3q8leBqxiYQRuBmAQNajCLgFT8EGLVpOaItAkZSt65UetPSVdQcAzyDuN3TZITF9l5bbKrecpiXO_9ILaFcDeJ-tXXDH7NEMvggNXOX_CQ0dnIujZCBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=TSIhXwd6dw8vxIn-fDb9c-9TZnUYeBpyLOdCNmZoOKQLHlkUeYBtSZN8ML8EcYx9yBL25yF7o-iJWKWWRDg-jFclLGV0TGT4mWbIPZLe5_6GOqpWNNWNjXhweryjdpkP5p9o-5rFkyABUGCC13YCdUCCnrryJE5oVl_xMEf8GxYQxLoJEkhAAcAXT6vCOOk3tqRylMLu73RckB4PCxXwo_QItjehHNvAg4MaIbL_-J71TV33mlRyAK1BVS4ov0I7kM6kIbCdqxbde6Z4ciJztlL0hYnSnQ3iv4lgJit6XT9rrkUT8LAkDtqKs7pO_UE6u9kSGqneAp8UA18Lgef6XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=TSIhXwd6dw8vxIn-fDb9c-9TZnUYeBpyLOdCNmZoOKQLHlkUeYBtSZN8ML8EcYx9yBL25yF7o-iJWKWWRDg-jFclLGV0TGT4mWbIPZLe5_6GOqpWNNWNjXhweryjdpkP5p9o-5rFkyABUGCC13YCdUCCnrryJE5oVl_xMEf8GxYQxLoJEkhAAcAXT6vCOOk3tqRylMLu73RckB4PCxXwo_QItjehHNvAg4MaIbL_-J71TV33mlRyAK1BVS4ov0I7kM6kIbCdqxbde6Z4ciJztlL0hYnSnQ3iv4lgJit6XT9rrkUT8LAkDtqKs7pO_UE6u9kSGqneAp8UA18Lgef6XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=Y5TiMtAB3InrLS_qHYOuBM_t1D7InuDXzKL-IhKloiRy9uYgT_Bb1kvbdCbkGkTX-T5t8AZspQU56kwcxSYKoA-u4vQWyLF91_V8tsW4FN8cc0uWC5kpUmR25xyHl0hvBD3o0LBszvvZat76CqgDnieNijf5iqxg2NC1JvGOWdMAQgcwI6tamwBcCeRr-yVsZ7wgAhvMYsimKlR4Yzbuk-58ndupOFiYeCP8mfRvoKN7sEt8U3QrRhWecYV41QxZXLYnYCOhQjtO7uUl-SnT5ME-QQNgi1M4Km9OkVgDHFC8NlhfBKmgfJQSWe_UHhAppNGlNxYNw7fWn3uqjM-kAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=Y5TiMtAB3InrLS_qHYOuBM_t1D7InuDXzKL-IhKloiRy9uYgT_Bb1kvbdCbkGkTX-T5t8AZspQU56kwcxSYKoA-u4vQWyLF91_V8tsW4FN8cc0uWC5kpUmR25xyHl0hvBD3o0LBszvvZat76CqgDnieNijf5iqxg2NC1JvGOWdMAQgcwI6tamwBcCeRr-yVsZ7wgAhvMYsimKlR4Yzbuk-58ndupOFiYeCP8mfRvoKN7sEt8U3QrRhWecYV41QxZXLYnYCOhQjtO7uUl-SnT5ME-QQNgi1M4Km9OkVgDHFC8NlhfBKmgfJQSWe_UHhAppNGlNxYNw7fWn3uqjM-kAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=PwxqMcmzCQz7HCgBNM0Msz1JtV81LURHUvJKtvlLXHCTzxoPdeGZ7dkyXz9KYyBP001TpK6x2obb8j34egiuQoEe_JPgupt5xHXYRY3aa52Ci3YeQ3-dsuGg7b8PwnMT3ocz04QTTfIyMbjL1NPGN-PN3uswBZF2Ssx9lmwImrDKU-zFBM8_iBrrdDUrA_x1dmRMzNz5kt4EeViM1uB8iH-lSavRqyzKa3cazf10YAUHMkXaCaItXtMgidmnWW4fANzBZe0-NwZYh-ZVeZkbBRl3iAz4eW6ibev8tfBoO4fxuwKqeO2iUn8ndOm-74b2Mxcc4ocBlhhe44zf-Bxbxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=PwxqMcmzCQz7HCgBNM0Msz1JtV81LURHUvJKtvlLXHCTzxoPdeGZ7dkyXz9KYyBP001TpK6x2obb8j34egiuQoEe_JPgupt5xHXYRY3aa52Ci3YeQ3-dsuGg7b8PwnMT3ocz04QTTfIyMbjL1NPGN-PN3uswBZF2Ssx9lmwImrDKU-zFBM8_iBrrdDUrA_x1dmRMzNz5kt4EeViM1uB8iH-lSavRqyzKa3cazf10YAUHMkXaCaItXtMgidmnWW4fANzBZe0-NwZYh-ZVeZkbBRl3iAz4eW6ibev8tfBoO4fxuwKqeO2iUn8ndOm-74b2Mxcc4ocBlhhe44zf-Bxbxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=pIcGVTQYFGLLkl_gkr1mNCFYd1ZbfpFJMsScM1oNSvlvvjtFSTlmzWx87TIuW9YUdnH0wLn5wCvTZ9RamncmKwTHVhCZylNUxK25YA_-pwQNULQ_sXL_tni0wL55rQKU-kFtWy7vk9dtu7g6ebCn1hTC4z8cGyvxPTek4hlyBbMpEpJIwDAaPRaI7yZagATmQafMbig_5fRrjGx9HCvl-gmZzh3lfkTnuutt5gECO91feR8n_dGuBwmPerQ2Nc7jmnzH_dY6ArihNfNWG3Zv1zIYYONd1IEJ271clwUvyic2kZGCUUJMDI80j4W2CxcFTAEsOhhPUEN3uUjn63HQ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=pIcGVTQYFGLLkl_gkr1mNCFYd1ZbfpFJMsScM1oNSvlvvjtFSTlmzWx87TIuW9YUdnH0wLn5wCvTZ9RamncmKwTHVhCZylNUxK25YA_-pwQNULQ_sXL_tni0wL55rQKU-kFtWy7vk9dtu7g6ebCn1hTC4z8cGyvxPTek4hlyBbMpEpJIwDAaPRaI7yZagATmQafMbig_5fRrjGx9HCvl-gmZzh3lfkTnuutt5gECO91feR8n_dGuBwmPerQ2Nc7jmnzH_dY6ArihNfNWG3Zv1zIYYONd1IEJ271clwUvyic2kZGCUUJMDI80j4W2CxcFTAEsOhhPUEN3uUjn63HQ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnpDm207AEztU_1KjGnPpN0oUYiviiQFVZQFymgm62p4flm61zUKeXFoffACKCe2zkigR8NGOmMnaW7ZG2WX2Cy6gDqjcux8QMDmbZe44d0aThfmjr-cfv4dF6nMAz46nGJMih6N_OTwuIgAGRrrm0eNCb5OMufvuQTyhVCyOZyc5NIPcIRzbHfMkPWhTL0Ajo-KYYGlvI_-2XnwSh9I-x65kP_ofkcmx83br_Wc0Ga8l6zuUrGJW0arNEBp43LPU_KcA3c58oSP9BL2gl2NDk-XvtgTywF_8DGCVw07NDSjLulNdzTjMIwI7s1tzwW7-6ImYwMFBjlVXM9XOk1e-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=Kc6XEWTROsai9USrk5QvqzdZQW5hMWTPwpuPd2vLzrXgbbM7u6hnsQqSAQBuK7dEJy0dwbdNH-hsMENWCd5vJnxqB36vWCq_K501dvN-kSWNqmxjhuthRihoF6Eo2NmIjInoU1Jzw8hUl2B70M4Jppc0NdZMb_NAfyf32YrjJyHdXeOrbQipTwRd7-PyH7hzgJmXVK9jzZE4LtKWZ_Su6AnJH9MOfXYHvNxykg97XPMHpkTAkuenSOOWWySbBCAWfbb8D5cgV1Z5HU8dQY4pVxUepMfqIOdgAkwcdn5aQLx2SQcxnyoSYN5Rit5v3Ayq1hPm2zZWUpchZdaPCbIp5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=Kc6XEWTROsai9USrk5QvqzdZQW5hMWTPwpuPd2vLzrXgbbM7u6hnsQqSAQBuK7dEJy0dwbdNH-hsMENWCd5vJnxqB36vWCq_K501dvN-kSWNqmxjhuthRihoF6Eo2NmIjInoU1Jzw8hUl2B70M4Jppc0NdZMb_NAfyf32YrjJyHdXeOrbQipTwRd7-PyH7hzgJmXVK9jzZE4LtKWZ_Su6AnJH9MOfXYHvNxykg97XPMHpkTAkuenSOOWWySbBCAWfbb8D5cgV1Z5HU8dQY4pVxUepMfqIOdgAkwcdn5aQLx2SQcxnyoSYN5Rit5v3Ayq1hPm2zZWUpchZdaPCbIp5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=IqFublfKGjXg6PaDHY92QzfEPNfP7ArFvRyxooibo29Rdf9xBDLOowcwvBf0V3cmkAEqXjD20pJo-ihQfzfM-IABNE1YkP8w4yz8n2h42BfTR94eLvzjK7-JAaFjnaIIS3hry-4iU6zyB4IwD5xXubbq2SMk36UVqCYyWiBpdo9dZOAWNVNi15kHwP6gZMqpl_xgAlcjBUYbXQF4O9N_C106fNqHrfqS1NIXI7W0Cqm52MEDjcy-w8orsVBp5XgjkL6UUg5ClUZcpn7NgA3H4Il-DvpnZQ3ZmtkxQyOxDsisMTKZTEWvgwHkxL7QyfFzI3lKZTN9qGKf8qwcJoCKdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=IqFublfKGjXg6PaDHY92QzfEPNfP7ArFvRyxooibo29Rdf9xBDLOowcwvBf0V3cmkAEqXjD20pJo-ihQfzfM-IABNE1YkP8w4yz8n2h42BfTR94eLvzjK7-JAaFjnaIIS3hry-4iU6zyB4IwD5xXubbq2SMk36UVqCYyWiBpdo9dZOAWNVNi15kHwP6gZMqpl_xgAlcjBUYbXQF4O9N_C106fNqHrfqS1NIXI7W0Cqm52MEDjcy-w8orsVBp5XgjkL6UUg5ClUZcpn7NgA3H4Il-DvpnZQ3ZmtkxQyOxDsisMTKZTEWvgwHkxL7QyfFzI3lKZTN9qGKf8qwcJoCKdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر جنگ اسرائیل:«حتی اگر ترامپ چیز دیگری بگوید، هیچ‌کس نمی‌تواند به ما بگوید چه کار کنیم و ما قبلاً این را ثابت کرده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66476" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66474">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=p307DvRRgHpGVwJqi0AjkhyHTIKt7trSI6kDAS7RZQI2MNrhXMVqjDI3nQYGnvjo4nVgmgVxDnJ0jDbuEXPqsCjKXXTWW59yjoDOlF8yyRiQ5agICjWf50DnRwzJsJorx15MVnjnPZ2isxkclffJ1u2r_0f-jBCYkNp07FEBiF-uJigCNXgaI_7RNHGUcV6CJdRn6hzLSCQ2Ag1_yCCDgeeAFAxlI6HREVTqZxJLQgLOTc-rHyB3Z-EDWw8jkE7rrvj-P7SmWq2uVynPmr_zKLzfP5LJVxMpfZK-HsnVFzW--qgBG5tMeTZsSIxp7ptmWFk6m3MDFKdYQpf3UEPEkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=p307DvRRgHpGVwJqi0AjkhyHTIKt7trSI6kDAS7RZQI2MNrhXMVqjDI3nQYGnvjo4nVgmgVxDnJ0jDbuEXPqsCjKXXTWW59yjoDOlF8yyRiQ5agICjWf50DnRwzJsJorx15MVnjnPZ2isxkclffJ1u2r_0f-jBCYkNp07FEBiF-uJigCNXgaI_7RNHGUcV6CJdRn6hzLSCQ2Ag1_yCCDgeeAFAxlI6HREVTqZxJLQgLOTc-rHyB3Z-EDWw8jkE7rrvj-P7SmWq2uVynPmr_zKLzfP5LJVxMpfZK-HsnVFzW--qgBG5tMeTZsSIxp7ptmWFk6m3MDFKdYQpf3UEPEkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی شبا میری اعتراضات و روزا میری راهپیمایی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66474" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66473">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=YZKmo9Ly6twosCnnVNFk7an3Yz488nCZShrV0RNiqMb10bKbNd4vQAjNoUPpJe8PYComKreyG9alX-ecDZGyEhsk0LvhgkanSYWo5vWXtpc1sSiUCALEX6rTKvEg7Qa3k8rrIPp9ZtbuEP7k1638npX5FWtu6mO-voz8UP0RK7NBauMR5_lkL7oFMw0NQU6CTQTgKXoU5p_snC7w51oAn3KImLANL_l7VArvZtB0NlB0QbQIJgHy9yrDMME9bZW4CYE2MWAhGURQxy2JZryXrc5_c9mkZlpSODNghzh_n_BpuVEYlRfApEBdgkA15fJPLBqRHZdxU5eYlV9l6UXfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=YZKmo9Ly6twosCnnVNFk7an3Yz488nCZShrV0RNiqMb10bKbNd4vQAjNoUPpJe8PYComKreyG9alX-ecDZGyEhsk0LvhgkanSYWo5vWXtpc1sSiUCALEX6rTKvEg7Qa3k8rrIPp9ZtbuEP7k1638npX5FWtu6mO-voz8UP0RK7NBauMR5_lkL7oFMw0NQU6CTQTgKXoU5p_snC7w51oAn3KImLANL_l7VArvZtB0NlB0QbQIJgHy9yrDMME9bZW4CYE2MWAhGURQxy2JZryXrc5_c9mkZlpSODNghzh_n_BpuVEYlRfApEBdgkA15fJPLBqRHZdxU5eYlV9l6UXfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نبوغ اوکراینی ها در شکار پهباد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66473" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66469">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZ8VouAjWKu8oxyQEmsOi2eHDS-FNs5cHSdj3RGtZQ1C-_XK-TqckIM-eiqYtIpV0f1E7zHMRl3zOXnBnxrRtZMdHtEBtsOWjS4hwBADBrCqhW5nz8J5ZC2EGVGafJJjk5kVSdFVSakctcGJESCJqx79TaiqiFLbImqG2jcm11m9zAGd35JnwzfmLsAZ1gr-zh3zAWsIG78RJduQb_L-FRhkQZY4j2UEHFuZM9I_XefXZkf3r_hoCKfKe3HRucbMSavoIZwvvJuj8FuiwWmqLWLQbCl3_C6t4Hfqogp7VlTfIJxKfyAbeESo2XdHz-dQq0cHS3vLduNAaYyKEcJ1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T720apePlZlhjF771v6HlWztcp8WXbJTRHT8VZ4fk-JhxIwzTiy2EgXhpAlD2rNdtlpH4_Zb6hH-UcODVfHjzrunCZ4lCMaABZYSeGKc6G14gmnsPmD0Y0ObWqDm17Xr4uQahHA5LH9shIX6OHe5A64sAnuiXZfd-L5s94sim73jlfuV7qwQhCHTmCjxpeZWAnuzRQREWDd9ngKoj9ZexijVkAwPd5nfgScLD6EYVCrOe_dIN8Qcs4ywMYZb3iQQLGljSn3iLYLaATkBka5xNTjlNFjTeOxQI5CGJLn08LV8IR6bVD08ut9KJKQyQlEhAnQs08Sw2bEDKcnvlkVU4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTLLPgKT10bfOrmfxrOcIcQWoZhTETITL_d7VO7vE5Tqcc1VIGXADu8YfGPBtykzb2ky8BFTvz7TbwnkukUA2kyfgLwog1jenusoUZci8HGLEP97x9ucKCzGNJGSNgkUJ-BTj5DnRaMxbVP1VkhwQbvQb7TEVUlin1ajQQhadgEikLKCfRTG8uhzta_co560UwpKM6H3EkwszpgfahinP6wgnoF0_KNbfTaoMjSZHN4Bh7ury1FgYR995WR7Ps7bUhatLuLPhzJZH20Wiv3ssYetBFvAuP5ExDIWIFO57404hMIZ-aPFbyllRGcMCHGVf2O1B-8A3McAxOONg3oaRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=kWIawm6fiLPuVOoPxOV1JB48ykuIZWORKnnxYWjQof16B0IgMVNbHKrM3B1lqXxUP3icynR--L8-BrA83tylwutpeT9_AVKgsyuyr_FvbD0dXAknr1mW5XwWGOIyRt5a2DttIUSpUfsvMMNSfYoF0KJ0o0Hwlv6wyhJx7JomC5sP8H5IqQ4SFviCjJDZW2A88I7pvococF4-OkNG8_mTEm9MAobeIGm_YTUD7QE_SlD1pv5KfFGFj3i_3mneNCeMDlQw1zisCLJAWFp73vhUylyADoCe2cQnN1ZPHGCvCRXVdEfVZsgqW0DGMtZDYecHg6ZpudGje41KSpYINaveBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=kWIawm6fiLPuVOoPxOV1JB48ykuIZWORKnnxYWjQof16B0IgMVNbHKrM3B1lqXxUP3icynR--L8-BrA83tylwutpeT9_AVKgsyuyr_FvbD0dXAknr1mW5XwWGOIyRt5a2DttIUSpUfsvMMNSfYoF0KJ0o0Hwlv6wyhJx7JomC5sP8H5IqQ4SFviCjJDZW2A88I7pvococF4-OkNG8_mTEm9MAobeIGm_YTUD7QE_SlD1pv5KfFGFj3i_3mneNCeMDlQw1zisCLJAWFp73vhUylyADoCe2cQnN1ZPHGCvCRXVdEfVZsgqW0DGMtZDYecHg6ZpudGje41KSpYINaveBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به نقاط مختلف در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66469" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66468">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUeAE5MoX33nSrcMQtxEZjOBKuwwPO9fWhwPzpwW23vGfA6YJ6lLU-8rEnGM35fwTTKxaQ2bkcvIoup7nojCE3Mzt3K7QLgo4vCpIYxVIc7OG1syxEuvV14aDxYkmCKfelYOPA37kieIflIniDA5ZpjfD_6XIqcAT86sQ3OL9sQlpCH05wQS8VBGqGXAmf9Sfjul2MDR3nDK1g_REDyHV6YiyjFq5kegSlwC9Ot8uuHJCr58fA5l3nNz-MZfN6hH1Tx8qtJUzwTRMASNxt9yq2ohJ6GgOqJmF3nz-RVCvqMW1j4qSTN1FVnSojRFAo4VdJj4HAcbJzhy1_eAj5P2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت ‏مسکو، روز ۱۵۷۶م عملیات نظامی ‌ویژه ۳ روزه پوتین در اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66468" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66467">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be955089.mp4?token=DZGRqaNHhuFG4hL6jTKU4KalIXKMUgjiMsCNgs798X4ELY16Nq9aOdN3qAuCsi9YG15pG0-nYCerwT_KALg-YbQG5bIixashCjnQIQ2_ZMBfdVp82bw0fcbjBYqxSQL_kqmc29QmYBK6bN2LWPo5SRd4tGySMl0D5Kwt12M_cTxkiTsPoch5cVeXZ2hK7ul1k7LS9W3qZ96YqsWDku6DDDqHl4IL5jHhZZX0Rthe1nJ0Xr8Y7Q4LCPC4O-AYJmU11-UeEGUTfBCqGNZyWppak4_OLN7GK64KQjfwip3KJ8h-WgCMKa3hgJ2PhJOFlt6ZvRcmxQl8afNM9L1IpIQCZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be955089.mp4?token=DZGRqaNHhuFG4hL6jTKU4KalIXKMUgjiMsCNgs798X4ELY16Nq9aOdN3qAuCsi9YG15pG0-nYCerwT_KALg-YbQG5bIixashCjnQIQ2_ZMBfdVp82bw0fcbjBYqxSQL_kqmc29QmYBK6bN2LWPo5SRd4tGySMl0D5Kwt12M_cTxkiTsPoch5cVeXZ2hK7ul1k7LS9W3qZ96YqsWDku6DDDqHl4IL5jHhZZX0Rthe1nJ0Xr8Y7Q4LCPC4O-AYJmU11-UeEGUTfBCqGNZyWppak4_OLN7GK64KQjfwip3KJ8h-WgCMKa3hgJ2PhJOFlt6ZvRcmxQl8afNM9L1IpIQCZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری: شما گفته بودید که فقط تسلیم بی‌قیدوشرط را می‌خواهید. اما این تفاهم‌نامه شبیه تسلیم بی‌قیدوشرط به نظر نمی‌رسد.
ترامپ: خب، در واقع احتمالا تسلیم بی‌قیدوشرط است.
مجری: واقعا؟
ترامپ: من این‌طور فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66467" target="_blank">📅 10:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66466">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=OURJVuR6wnZoijA6gTzQrbGI-BltiXgz0MMwLajWB0P-RdyqqqxVx4jcwhywZ9qkH-tS4o1zLytBqZW3R5sGrGSej7ykPHSAcpHugRs28_KxpE2wn-ijX45aCCo2wMueOsLenflJIX7X4d-TDCIWXx4Qfd4UYnJXyYMdUJ2rTmke2EEAscCFLBDXBj6zkQwVK_9rJoRc6emeYfcYvTd5w97k1yL7psFFgbiJZ2f0nNw7qvZt1N02YxiSYg0yPzbfDk6tMu524v4jsG46KjdKrjTaW23WAsF7WSDfzouRP6ANCcyu_4gdO_mE7wB7o-LDa4wICNhTaenxodMeJ7rWYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=OURJVuR6wnZoijA6gTzQrbGI-BltiXgz0MMwLajWB0P-RdyqqqxVx4jcwhywZ9qkH-tS4o1zLytBqZW3R5sGrGSej7ykPHSAcpHugRs28_KxpE2wn-ijX45aCCo2wMueOsLenflJIX7X4d-TDCIWXx4Qfd4UYnJXyYMdUJ2rTmke2EEAscCFLBDXBj6zkQwVK_9rJoRc6emeYfcYvTd5w97k1yL7psFFgbiJZ2f0nNw7qvZt1N02YxiSYg0yPzbfDk6tMu524v4jsG46KjdKrjTaW23WAsF7WSDfzouRP6ANCcyu_4gdO_mE7wB7o-LDa4wICNhTaenxodMeJ7rWYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ به شیخ محمد بن زاید:
وقتی انقدر ثروتمند باشی، میتونی انقدر آروم صحبت کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66466" target="_blank">📅 10:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66465">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=p36LANUQr50fn_CGxfc5vMpaz9rsY9NOzH7PlBJwK5jx-FI-faHCwbbFwHY4hEh5CUkZsTo1trNvrTTa_WugfU9ZObAXBID-72y4Mc6P1Sd2I66E7I3ahbDBGUYCup9C1x4n_lQbPLDuE0tqvmuW9Egd2O9sOeA-MOyttOW6_j3MsmnytfdInTD0kHHoC4-ZR4He-KKzxbbTHCo03aXWzQmh_nxHjLxDSa5iKg0O1zjt0dqj2RC4wXF989IikSQoFQgPbxjFr1wWMGZGt38OaWxdjgCa37WkAz4gz9NCoWUWyA081Nn789rEnjM0wL5orAZuA-V0m9Nfju7lusry6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=p36LANUQr50fn_CGxfc5vMpaz9rsY9NOzH7PlBJwK5jx-FI-faHCwbbFwHY4hEh5CUkZsTo1trNvrTTa_WugfU9ZObAXBID-72y4Mc6P1Sd2I66E7I3ahbDBGUYCup9C1x4n_lQbPLDuE0tqvmuW9Egd2O9sOeA-MOyttOW6_j3MsmnytfdInTD0kHHoC4-ZR4He-KKzxbbTHCo03aXWzQmh_nxHjLxDSa5iKg0O1zjt0dqj2RC4wXF989IikSQoFQgPbxjFr1wWMGZGt38OaWxdjgCa37WkAz4gz9NCoWUWyA081Nn789rEnjM0wL5orAZuA-V0m9Nfju7lusry6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختران حاج گاسم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66465" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66461">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4-_h9qKlUIViHawzkGqnWesYPBp9qf2UzAbhAKEyX2Pt36K0vPg98qm6mmYz6Yz38fCRrtv2yyh-ZOGnzpSB3PEmyIOVj2AZ72m85aSdpoZ4pZOnVv-zESdVyiYqXtNd_ZaKCTZQPEqOOuWmDAmMGF35EjJ4l_2p1T9U8Vi4gbFA4HBmWSgHQjtzOYxcULk8esGBWNgwsYquEFJ1XfT6WX7JDxsKnRhI1x7Hqd8dMWzT5n84Xfu3vMxQXO1t-pZ0pN7g-W4LvkcCWt_gA7AqUEPmjKmKfVDgLmQ10x1nBesErbAMr7fjiQKhOx4nhP4udbx2kW7TQWYWkh3n8tACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=Uf9SpIwWtePkLRIrMeXrArTtKRbH4zYIDLqBR-otufSDqHD6ZE1EvzfyUZ8SMl0JyQHXg4Kq0pDMrbCGa8RRqUD7osKb0T5_zWjQoCnqGlaTqi-SHFoD8gfWLcRTzfPPPHirDTCZ3xe7nD5LEwUebKTASlfAwXgWx9ppFOvYPHS3N5UAWjXGJtzVHQ_yX_Y9OiQA4VkF63AQTr7YTH36je7JpvceIbGgIjcbRes2YQEPKMSKM1eCoO5r3BcYPIYjbNZmVc1ihm6O8pwL0r9QZcJqt3YMJd2gs-524PCmQ7hRiUDKxdeIrdxGWf1FY97NgJM9Rd4b3QdUtol5El5zrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=Uf9SpIwWtePkLRIrMeXrArTtKRbH4zYIDLqBR-otufSDqHD6ZE1EvzfyUZ8SMl0JyQHXg4Kq0pDMrbCGa8RRqUD7osKb0T5_zWjQoCnqGlaTqi-SHFoD8gfWLcRTzfPPPHirDTCZ3xe7nD5LEwUebKTASlfAwXgWx9ppFOvYPHS3N5UAWjXGJtzVHQ_yX_Y9OiQA4VkF63AQTr7YTH36je7JpvceIbGgIjcbRes2YQEPKMSKM1eCoO5r3BcYPIYjbNZmVc1ihm6O8pwL0r9QZcJqt3YMJd2gs-524PCmQ7hRiUDKxdeIrdxGWf1FY97NgJM9Rd4b3QdUtol5El5zrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات شبانه ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66461" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e-ExkXZz_uz1t5QjMKr-JSASW69VsgAzA4rGQeiBPgu3kjIG0Sgd2ASzTvELMhN2buMxCCS8omWMjeRnRu3Ptwkr6_kHsYI0SEPB9ztqVPUeuMUZ0d7HEY-PQYD493c1JBMD6XnAeyx8TLrj0jmVCsZmbg9bpYl0r2n17TmdckNOsImsVUhts1NwGsJUmJDBZVyL8ZxVL3wWH6dMjpN7N4K9K7KC2hnIvJyEAxp115ZM_eKwmly1474dX7Q2E9bsm897uNSdjYEEMz-OgedSmigEyuDWpRHLJgiNNqXMcs--jYUddzFmnlLGXDJyOyPk-w5zbuqlN_9flMAAnQ-y9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66457">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=vDiwOVibJYgfle4yofZdS2VPw1tHp90DR7l1jAOocvuyhZ1zJF_phb5r6GjaMuFAo1uHzhvsDFWfj9y_n6woDNsrD7zFEYezlHJ7XGakhSueOE_vwhNiVRhl37_LsOqPargwsF6lWDntB-Z01GNhOA8-sSmpbuJ-izOfooI9ot2vHR-xEXrA9mWFQCmFT9MN7nuRiwmWcAP1t_ED58w5NV4SL8bHxUIiuYZAjlV-4Z7FeiLMuYwte64snoXLr7a0o7eutXqqdJKgk8tZvCSl8SA5ofSDL6p3L4OvMdrjdpXm5Bg_zSj58ESQJiUkuWF25vJXBgBKOh2wwjLDCPXcAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=vDiwOVibJYgfle4yofZdS2VPw1tHp90DR7l1jAOocvuyhZ1zJF_phb5r6GjaMuFAo1uHzhvsDFWfj9y_n6woDNsrD7zFEYezlHJ7XGakhSueOE_vwhNiVRhl37_LsOqPargwsF6lWDntB-Z01GNhOA8-sSmpbuJ-izOfooI9ot2vHR-xEXrA9mWFQCmFT9MN7nuRiwmWcAP1t_ED58w5NV4SL8bHxUIiuYZAjlV-4Z7FeiLMuYwte64snoXLr7a0o7eutXqqdJKgk8tZvCSl8SA5ofSDL6p3L4OvMdrjdpXm5Bg_zSj58ESQJiUkuWF25vJXBgBKOh2wwjLDCPXcAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آیا در جامعه اسرائیل افرادی هستند که بخواهند ایران را به لیبی تبدیل کنند، یعنی یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالا بله.
اما نمی‌دانم که بی‌بی (نتانیاهو) چنین چیزی بخواهد.
من شخصا هیچ‌وقت چنین گفت‌وگویی با او نداشته‌ام. گفت‌وگوی جالبی هم می‌تواند باشد.
اما همین را الان می‌گویم: آیا تبدیل شدن ایران به یک «لیبی ایرانی» برای ایالات متحده آمریکا خوب است؟ قطعا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66457" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66456">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=BK0_rLcTnGwmHPxq6YjEGS1YlqNF1-lbvGmzrPIOJwUp_2HDbrOwFBb6xjxrIq5BIGN3-bpG-ATESCIV0aPiSgrX95gWsNzen0FVnELuSxmmmacCu5AWun8X5M5S1_OnypSM_94J5rh5sPXjTGfDWtDrpnR7r9PKYdkybpqgv5ENbf61t3ML13CqCTGmrknyOIRwTvnugmnDM_b4TNJ64ynxa4S8kX9NTL5ArAvgHKjy5-IVdwUersWsMPhUQ1mU038ZvQrxQ-Kc2fSEYYi3AwkOS_SyQd34VzYWCngfW-KInROKIwNnovIt2vrB8lQk4NbxiGAJGVeWgthg5nfdUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=BK0_rLcTnGwmHPxq6YjEGS1YlqNF1-lbvGmzrPIOJwUp_2HDbrOwFBb6xjxrIq5BIGN3-bpG-ATESCIV0aPiSgrX95gWsNzen0FVnELuSxmmmacCu5AWun8X5M5S1_OnypSM_94J5rh5sPXjTGfDWtDrpnR7r9PKYdkybpqgv5ENbf61t3ML13CqCTGmrknyOIRwTvnugmnDM_b4TNJ64ynxa4S8kX9NTL5ArAvgHKjy5-IVdwUersWsMPhUQ1mU038ZvQrxQ-Kc2fSEYYi3AwkOS_SyQd34VzYWCngfW-KInROKIwNnovIt2vrB8lQk4NbxiGAJGVeWgthg5nfdUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس این انتقام ما چیشد؟
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66456" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=NeyY_kTzHT6MdmnociWpqVjO9Hctcz4WTTiENXwgjkYLZAq214dtLIJBeO1McJxz6kBtja2D40UscvbNMgJAPDOqdGRfysEXt8kHRUBJ_btWWM2J7rIDmDPFGQw5uZOdRgCEpBpGyW5I9viGqBqQ8ENb_km3zKmS_TF-QXQEuwg2ObdctRKQy7MdciKfqBp5SYBkX_Pua1wVi0pJesomrU-wXJE6fX0oqFtG4jrWAfJth9RkdYXd_5-GF5DSAOt0AXwQDTZOdnjYPbGgmBh3Nfd9nyrHoePWMZMePZWVi2NuBfqN6cBVXDsAQt-dftrOH5GXnma1ebe9-2oWZh9jtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=NeyY_kTzHT6MdmnociWpqVjO9Hctcz4WTTiENXwgjkYLZAq214dtLIJBeO1McJxz6kBtja2D40UscvbNMgJAPDOqdGRfysEXt8kHRUBJ_btWWM2J7rIDmDPFGQw5uZOdRgCEpBpGyW5I9viGqBqQ8ENb_km3zKmS_TF-QXQEuwg2ObdctRKQy7MdciKfqBp5SYBkX_Pua1wVi0pJesomrU-wXJE6fX0oqFtG4jrWAfJth9RkdYXd_5-GF5DSAOt0AXwQDTZOdnjYPbGgmBh3Nfd9nyrHoePWMZMePZWVi2NuBfqN6cBVXDsAQt-dftrOH5GXnma1ebe9-2oWZh9jtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آنچه من به برخی از منتقدان این توافق که شنیده‌ام می‌گویم این است که آن‌ها می‌گویند: “خب، ایران این همه منفعت به دست خواهد آورد.”
من دوباره همان چیزی را که قبلاً گفته‌ام تکرار می‌کنم و احتمالاً مجبور خواهم بود چندین بار دیگر هم تکرارش کنم: ایران دقیقاً چه منفعتی به دست می‌آورد که قبلاً نداشت؟ پاسخ این است: هیچ چیز.
آن‌ها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتارشان را تغییر دهند. اگر رفتارشان را تغییر دهند، آن چیزی است که باید از آن استقبال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mihh19exfEzYLY8MLWuQT-c6N38cuhAY0YwYD0VDQxtgYQzhnB_lS6exTjifJ3gP-cXEaYSQe6b6AnVMJSCZXBMRh32B0XbdmAodT3Yl-n8jsL451ehxZdEcMJZy58f9gPsz3Va9-pETceHilzbtJK6r-HmRqU4NO4AVJedHAPRHYCy99KNlKuOiaTlSSmN6LG58dzKkNnzPg612gMB25VHcTajqh9CScQmoLMia5uoKpQK6zXx150cv-BJm63ons_snKxz5a6fHxk7nZxC5IS8dUOp4mTC0h7wRrVahzSJkDfd0pC-oBGVGDQzziJPN7jOsvnDyJsbcwUbEyhUXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArFM6ZAz05TKETd5Dfo3E1Uwj2XR0eREqRbgwdP7-4-SE5Ulv3Gz7oTrlJzq92CivL3jQ_5h1t2Id12EfuMMH3bUFC44AlMLpKneLkOYE5bUu00figEaauDMh6gh8qoTgkHfGhAeyqE3mm-n-NltEpQgkcjxwZpeOeZ8q_EhkxmHB_Sku4DZ6q08_I95bsPxms6zlHzsK50_wMo7m_Zden6tqOWHkhV-qBJV7cB7OzvIxDh0whOy922Kf9Gs53mkjKNLnUIhNa_Mi3muqhdbNjB2YaOE1pSmBQaSkk0lRaK4ZRQ7R4uIOZo57aJhAiiaGHayO_ubmy-F7WPpoTz-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6TCSLVUh7sBVlyUA0AQO_kvH3ZdgDhLb_Sc-GLOYoJ6xZjg9v7Bd4Mgi27-_I__hprhQ1I5PLo3z-TxMeCDyrDBCWhVQT7HkuQ8rWKzmJYsSwCcbiJTqsa99TT38j8U_7TKYBFv1jl0FCQC-YMAPNxkcQmvkoceJRSCEyz4-0n6Un-b84tcSzK-Hgf8icIio9ws5EEQ1cVumsWNuIkaF7ShOLNSIO4tnNOBo6QhfmffeqnucZpsus-3ifF3ueJJNmla_8OItkWGHyEbkVzVuuAH9mIW5mZc79tvo9xU7ij9iJeThPmEGMnc3QDgAh989SfcseyE3RZhoiOOe1zSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=T-RNmfx6wauBVpdDeg7IfJZ0RBeven1GHqLILYReXsLLQtf9fWD5LsAdERDNMWE_uUYTWQbiOvh2iDsoM2vW4xdgtwaa7ivqn_FE7OQH7EKmJAm1gMPyN8MaIfx-wPTUqa3nrvGd66aAvzKFSp6-2mIW9sa6Z8jWmN7iDuWAwE1yPt5-ijLLhtpeHgmQG8fy7eb48DutJ1G8RWbQN2kJyTpgMXB9LXc26QgMOu0Yb7OCxABlc2xsZcV65rok3CPCYwbILYCvbTa8lJtcyRWEXgY9hOqsv9bSSReW-Ma_aRXp4JeEIgpO0oITf7W0E9uDsKYKb6rOR3u9m8LPcz7dkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=T-RNmfx6wauBVpdDeg7IfJZ0RBeven1GHqLILYReXsLLQtf9fWD5LsAdERDNMWE_uUYTWQbiOvh2iDsoM2vW4xdgtwaa7ivqn_FE7OQH7EKmJAm1gMPyN8MaIfx-wPTUqa3nrvGd66aAvzKFSp6-2mIW9sa6Z8jWmN7iDuWAwE1yPt5-ijLLhtpeHgmQG8fy7eb48DutJ1G8RWbQN2kJyTpgMXB9LXc26QgMOu0Yb7OCxABlc2xsZcV65rok3CPCYwbILYCvbTa8lJtcyRWEXgY9hOqsv9bSSReW-Ma_aRXp4JeEIgpO0oITf7W0E9uDsKYKb6rOR3u9m8LPcz7dkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس در مورد اسرائیل:
در طول سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط آمریکایی‌ها ساخته شده و با پول مالیات آمریکایی‌ها هزینه شده‌اند.
مشکل اسرائیل دونالد جی ترامپ نیست و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلش رئیس جمهور ایالات متحده است، باید از خواب بیدار شود و واقعیت وضعیتی را که کشور در آن قرار دارد، ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=ThdBy_Z7_s0kMfAgYquYXsHRvsqK5cC6o3cLenCsAwknmcyaN87qNgiICxcThZwILc-iEdAPrTKICf4-P73KOELpBYjRW8rwStAn7nlCPnsY17ie9EuCRgnt1Cy0w-_vLobdC6KLBivqSF1WkbSqCHEWrlT_mxc1_U7KwAytaK6FWnUBwqkjypc4kHgEzJ_6tX5QP5uqlDf4mQHh2WI8j6ZWL9Ef7dirdWCz-CW8zCXP6Rr9CQYtMN4Vqm_eIfrwXBtRyOdL1Qh_1hq6yv01pnZPp2-yXqlzfhnmQ9w0XZzEJTVKYP5bZZHVup8tjL87ZPBtODH-XGisnhms2vbShg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=ThdBy_Z7_s0kMfAgYquYXsHRvsqK5cC6o3cLenCsAwknmcyaN87qNgiICxcThZwILc-iEdAPrTKICf4-P73KOELpBYjRW8rwStAn7nlCPnsY17ie9EuCRgnt1Cy0w-_vLobdC6KLBivqSF1WkbSqCHEWrlT_mxc1_U7KwAytaK6FWnUBwqkjypc4kHgEzJ_6tX5QP5uqlDf4mQHh2WI8j6ZWL9Ef7dirdWCz-CW8zCXP6Rr9CQYtMN4Vqm_eIfrwXBtRyOdL1Qh_1hq6yv01pnZPp2-yXqlzfhnmQ9w0XZzEJTVKYP5bZZHVup8tjL87ZPBtODH-XGisnhms2vbShg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏جی دی ونس درباره ایران:
آنچه واقعاً اینجا اتفاق افتاد این بود که ما روز یکشنبه تفاهم‌نامه را امضا کردیم. این توافق‌نامه مفاد توافق‌نامه را تثبیت کرد.
چیزی که ایرانی‌ها پیش ما آمدند و گفتند این بود: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً متوجه این موضوع نشدم - می‌خواستم متن را فوراً منتشر کنیم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «مطمئناً، باشه، تا جمعه صبر می‌کنیم.»
و سپس آنچه در روزهای دوشنبه و سه‌شنبه، در حالی که رئیس جمهور در اجلاس گروه 7 بود، اتفاق افتاد این بود که شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را به انجام این کار تشویق می‌کردند.
ما قطعاً به آنها می‌گفتیم: «ما تمایل شما را برای منتشر نشدن متن تا جمعه درک می‌کنیم، اما می‌دانید، ما در یک سیستم دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق‌نامه را ببینند. ما مطمئناً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها به این نتیجه رسیدند که رئیس جمهورشان آن را امضا کند، رئیس جمهور ما آن را امضا کند، و مهمتر از آن، شعار را تکرار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M0KMtI3cw38MJr5KQIFshoJ0sHglyUceHDZcuHKN7Zu9y7KcvW6szoGMLWC5lbWcfopN2fONY70jVy-0XcJ3uwg5bAYljmkKILmKK05Zb83mpY05mWhaqWyjElKJyJmLi7SzMo3EdckjPjc8-Us1VS8OweJRZhwBs3OWBa6yaFDsFoCeZp9mKUx5dqwfZbL-pdUiaEcypCJkX2LSFScj45iAyI6hsKzUGW5QHWuQ3k5KFbBD_Tl0XJ6d6MDpwZTF3vt3ALlrn-1JM0mIJhGGUMrmWr3-BLO010bqX2NuQfbNjc25P7WoZBf1maYfExAKzNk3Su8paoQi7Yxn8_wyEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=RW2-fEdGBft2Q-jRVf3UyKXOmC0u4RHMAmxXGU-E9I4SZERoPJvHPe5wkL2BnDROP9qZX5bzmvZOIGxIpi9rEVeRuaVcqvRosW-l5i5G02a8gDBrAbpe71owCzRtmYj3_1ws-QlvhcRbXk5lvspSO44zOYlmHymkNcgS2BXdMVGo3pi4bE8xrWWuwy19OJadGJslWNRBsFBgG4eAsEXLMFUEvCwgSM4AGZXPcX6U5rBxdYzIFghRcpXlgNd6AkYBfy477IrC00OszxqqQkAyDIj6gQJ274CoANZdSWwXag1zUS1zvfF1ZrAWoGMmjYTRpAZNlTw0dFtGr7rFhXYjyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=RW2-fEdGBft2Q-jRVf3UyKXOmC0u4RHMAmxXGU-E9I4SZERoPJvHPe5wkL2BnDROP9qZX5bzmvZOIGxIpi9rEVeRuaVcqvRosW-l5i5G02a8gDBrAbpe71owCzRtmYj3_1ws-QlvhcRbXk5lvspSO44zOYlmHymkNcgS2BXdMVGo3pi4bE8xrWWuwy19OJadGJslWNRBsFBgG4eAsEXLMFUEvCwgSM4AGZXPcX6U5rBxdYzIFghRcpXlgNd6AkYBfy477IrC00OszxqqQkAyDIj6gQJ274CoANZdSWwXag1zUS1zvfF1ZrAWoGMmjYTRpAZNlTw0dFtGr7rFhXYjyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آن‌ها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به سهم خود به تعهدمان پایبند هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqj1t8t_qDZpAaKr0UsUQa5AaDUaBHUPPnGnOahsFtcRto6pJnYT5b_JEvxR6NI5rQJic4Ee89ipmpDv9WWCbJYM4ph-2drZQ2s_wXN3A0sdwbX5MwZYREsehfAZAGX9797hsqpnkh7PnhIhxysrj19BHeGQ3AQ0bxmundzTOZqwxXObapX7r2Y8jrA_EIYm09dQjP1fJCWI7vn7AcsZLF3BThVPxjysUARFFnAntND_ZVymy1eVTmOln53qgM_7eJVTzbUfEd_ZzLsOCHuFQesccWKzfco_MyjvvC59HxwJrNvxqbjErX0Q4xT86DwFqZuPfxQafwgR2hytXCwfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN_HtAoTPMdssaOJWXZVIFtPkxifcZyddZhc2JebnWmkxQNTIJ8q4STzyzXVNWHR16r6xtcPFrVl9ArmFnfOoDATu7_GWUi5n7IOULQ9qFXg7BSBZnESd-nu5WBXcdLvMo8Oy2B4ppMODhl806Oqx7tfjBVGzEWkafykziieB9Jtr4KODq_09YAAA6s1ph5YXYLR5SkvCsMZd0q9R09-c22NmHzeNfVnqdx18rlNwKHqMtYhxJkR8kASa3bz-0vXzbAXLvA9RRlM9ymsZgdYh1pwv0gR5956VVhSgFCzusl4e6ZuX0VKn2kA2tgoO2T75aaJPap0u_T4VF4v73-qrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
