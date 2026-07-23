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
<img src="https://cdn4.telesco.pe/file/XrPGZKWlPGPPA68Zo9HES1nnocbOefdvbfxUyQ81aOlyNYl3SoXtMCYwLpNa0CF4DW3PJJeE265Ag-vWB3hmBTlk9kWPbUqyzzPF7BjuR5KNWe2lf4GHSDOa2rBHDAmtr09yMQBzFyYWAaasRyNb5g3MgEaMdbE90-pUs63k1zyGVV9jwFoTL4vUtPWkwS385CX7inLUPJzSVocc7x0A30DgSvImUP1enRClkFWVDVjg-T09SCPpo4NE2dRF9w2IEYNrL8hRhkN7budGflDj5EeC0wETJajcO0fvpH74jzpYji106Qj9zcccqluAxoUl-dXWRQYMja8UiCj7WRHmcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 422K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 11:27:00</div>
<hr>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3405b1189d.mp4?token=S4SxAHBR9ByhM8UqLEfL632NOhTmhbUJPFjS5JL9yoSa6kwXPpDLtCeserNnChRTd2sCEXUSFekhIibH09xd-T36fyA_8OXlMuUFHD3ajik8TCj4jU4p4cCRBteHdcoTJW8H9-EnHArw-5cBjev1y7QeztA5bo0AevCR7JIGL_VmrkgYdpDfUdjq9Up04LUPJI-zc5ZI8WmZC90aXkpLgn4XcWLB3U3kZlB-IWzwDtxVflqTUZk-lgJG8edlKvPWuE8qFI7PR8oDKpm5QJ6gWJa4YvhMVRvsSuyFsla_udQAz5zT9LK6YYtfLelnkEL5plhwP5-n39-gtCM5dMq7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3405b1189d.mp4?token=S4SxAHBR9ByhM8UqLEfL632NOhTmhbUJPFjS5JL9yoSa6kwXPpDLtCeserNnChRTd2sCEXUSFekhIibH09xd-T36fyA_8OXlMuUFHD3ajik8TCj4jU4p4cCRBteHdcoTJW8H9-EnHArw-5cBjev1y7QeztA5bo0AevCR7JIGL_VmrkgYdpDfUdjq9Up04LUPJI-zc5ZI8WmZC90aXkpLgn4XcWLB3U3kZlB-IWzwDtxVflqTUZk-lgJG8edlKvPWuE8qFI7PR8oDKpm5QJ6gWJa4YvhMVRvsSuyFsla_udQAz5zT9LK6YYtfLelnkEL5plhwP5-n39-gtCM5dMq7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب ۲ موشک با صدای مهیب از خرم آباد لرستان  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/withyashar/19424" target="_blank">📅 11:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نفت ۹۸$
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/19423" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش انفجار ‌در ‌قطر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/19422" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urk-pRYPeRI6aFtLShKHlMDq-pvzUV0Rcq4yIy6h2nbIhnLjtAJc9-tAtItD37VfLRwy7hSWStfxXK08aJqYc16VLuEZlXuYTxjY3NUzr9_-VYzQSJdBSDDKyPf3NQvBvjTXLOdTYniF1KQNTaP_xorLsbJ4cSXhqzdNFKaj-W06TdGKYYsmwFKlSBqya4pp0eT0MLgaHFFVlvW1oYekgqRYjCbe5EE63CkVmjlkm_DeOb1vcdpmBCDWPPaNy2IrFPcsNR74P9IXm114M4v-y3976ACp5sbhKAw6EARmkbIN6_nkwcuIt2cJzxBNNFaMxH2NnHwEpwPBl1xBUo4IXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب ۲ موشک با صدای مهیب از خرم آباد لرستان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/withyashar/19421" target="_blank">📅 11:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معاون امنیتی استاندار بوشهر: شهر دشتی سه بار مورد حمله آمریکا قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/withyashar/19420" target="_blank">📅 10:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آلارم اتاق جنگ : فردا شب از نزدیکی منطقه های حساس نظامی ، تونل و پل های مهم که مسیر عبور تجهیزات نظامی هستند عبور نکنید !
⚠️
⚠️
⚠️
@WarRoom
یاشار : فردا شب ویسکی و آبجو میکس
🤒
⚔️</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/19418" target="_blank">📅 10:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Aq7sb7HCDCAcUxFjOKYQpqeQ9RcV4QRto14RHJQkfBNAqcD5znuyKOfqA449rKqz70XCMHSYUiVAqgUx6WcT-WZ2Ry93Vl8zXXX4tGBE_wEPZgzZ0pdbVYQGPKHh6KZT3lX8r8AOXSFCty4AOLQvGJd3ud498Gg1CSKpba6zE0yO5_yb1J1xHKpn_zb9-5TCIRArpt1gEt7HkkPbAK2jl9N07VJ8En-hdLqyqFiWTUfyaoZcmyY_ccwxlr_D0a_LIHsIepimEiRxWonxptq-b5vU0Lt5By_VONMOuoq7_KQvrzNXIbDCZi0-fBewSP1iP1RZYwgEoVuvR4RcAezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همانطور که در پست اینستاگرام (اتاق جنگ دروازههای جهنم) نشان دادم، هواپیماهایی که دیشب از آمریکا حرکت کرده بودند همکنون روی اروپا و نزدیک به خاورمیانه هستند.
فعالیت هواپیماهای ترابری نظامی C-17 و C-5M نیروی هوایی ایالات متحده در مسیر بین اروپا و خاورمیانه، به سطحی افزایش یافته که مدت‌هاست مشابه آن مشاهده نشده است.
منتظر یک جنگ تمام عیار باشید. دروازهها باز شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/19417" target="_blank">📅 10:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBxqh6ss5aqCj0zBRSvqyCfUoZ8_M98wKvP37jmvQA3zwNBQn6xMnDhnLfHKu-hhDHShLJwlaoVUdrWXqgzwZOyKGOgACh6FMDi69w0o48fbvM4t2ky-jLOzx7j1oa9FGP_7m-aEXxrxyasCJDC13FEMz3QaKnJAx8Rup-S6MjlFAvPSa4lEIrYzD-pcF7FA8i1YO7Kl8N1fz9MMXrozvZpwsHGh4NB7dzvNQMy9qwUvf84Tsy1Rd7rgi2m8HFTImhgsPXvKtgL9sxkUBZC_MQlsD59Br2VBekQtMQ3_MzFOhEdf2IRcmTMuw-aJCabrm20gglDBHqCtXXZ7vwkOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه امروز صبح خواهران دوقلو رومینا رحیمی و  ترانه رحیمی اعدام شدن
@WarRoom</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/19415" target="_blank">📅 10:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOudGEW5NhF47akn5c5I7J_CgeMd0eA6U6tsFR1_rkdg58Goz-07lpXqDiA1hxlA_YNUDPL2o1xdnbbB1THIWLNWfRmwSFpUHL8_GxYNYSDhpC9LP-newa_gf5wT2N1fbs1Hj-_Q6SNYHsAC4tZOxf6q9qXlp3p5YOCux0W1dUS6uductrulSe4Qnm8G1W-2JUyQ3zDsDASPN0Kc4fvbugIlKIYgKdn-K6HIHj6tB7paO--fv21RBG4_99E5Wj8RmVeK6COoPxOcIphYcnmpIjgCIdgNuz5ssgDhmSPB7mjhV2mVHn73e4hxmL8R82_XGQkMgrKjHW-mMWiuEM36Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج جدید موشکی سپاه : هم اکنون پرتاب دو موشک از خمین
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/19414" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7LTyAvUJR0c8VwuA3JzXaa6GKj8G-P9pjoXva8R-jlaMrok0fn00dOY-h1j8vvT8w8sMHsR1fXE0XsgGMr3wQ2y4Ma_xRYxCQJekFyWC6w1jfEL75c2mwoNQzItYfuvUy_zzE1SgI7ca4obQtbbbcyoU42_1raCpizI9bravMpgbIboTpi3MYI-_5_1-m_szzL-euAg-tCe7u1rRnNoK48ZRBUHhmuTXb9ob1MyfwBUm2_O8-Y2VF9DdrQ1i1mR5sT6fmFf8QF2vomcyrU79bio8uD9DjNGSJLu37ALTHjSSb-kjQ3z6HMG0peu4dZATrmwni-3FU5BhTXB6_riBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏مجله معروف ایتالیایی "اسپرسو" با نشر مقاله اخیر خود، اذعان داشت:
‏دیگر نمیشود به محمدرضا شاه پهلوی گفت «آخرین شاه ایران»
@WarRoom</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/19413" target="_blank">📅 10:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بامداد امروز، در پی حمله آمریکا، نقطه‌ای در شهرستان کیار هدف حمله هوایی قرار گرفت.
عبدالعلی ارژنگ معاون سیاسی، امنیتی و اجتماعی استاندار چهارمحال و بختیاری با تأیید این خبر اظهار کرد: این حمله در ساعات اولیه بامداد امروز رخ داده و دستگاه‌های مسئول بلافاصله در محل حاضر شده و اقدامات لازم برای بررسی ابعاد حادثه و ارزیابی خسارات احتمالی را آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/19412" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران: من آن را یک درگیری می‌نامم. ما با جمهوری اسلامی ایران درگیری داریم. آنها آنقدر ضربه می‌خورند تا معامله کنند، اما من می‌گویم که آنها آماده معامله نیستند. آنها آماهده نیستند چون بعد زیرش میزنند. اما خیلی زود آماده خواهند شد. @WarRoom</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/19411" target="_blank">📅 10:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کنگره آمریکا نسخه خود از قانون بودجه امنیت ملی سال مالی 2027 (NDAA) را تصویب کرد که شامل بندهایی برای افزایش همکاری‌های امنیتی بین ایالات متحده و اسرائیل است.
این بودجه، بیش از 750 میلیون دلار را به برنامه‌های همکاری‌های امنیتی بین دو کشور اختصاص می‌دهد، که حدود 65 میلیون دلار بیشتر از سال گذشته است، و همچنین شامل طرح‌هایی برای گسترش همکاری‌ها در زمینه فناوری‌های امنیتی می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/19410" target="_blank">📅 10:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1f97fe0f.mp4?token=QKccXNU8-BzdgROwyipA2Rp0zlXa_bgSGVrEJadkGjvO7muM-Nk_WlQkUBaTds_qRG6Rr2Ij2NV2DH-K0uLOKmowT35reDdRiJVK7ev7sEjcOI3KTCA2yYiWovxuCMXr0GpTq0aNUmLjrdf7zw12fQRFEK9l6mxiLcYowE-DmsZlUVthjrgfcGv_gY8-c_0iFmXbnCuEMwjTClOutrV7_lstpZYnhjVI_piCVrr0VpU8NjL7kMoKeSqCkpnfB6Q3XWAMsGNj5STRCXkfc_jA59dS5JDmgwqzvYRoHUK2f5Z2kRX_nzSc62yQIpc74IM5RubEpi7vyqSRjG6_bD_4PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1f97fe0f.mp4?token=QKccXNU8-BzdgROwyipA2Rp0zlXa_bgSGVrEJadkGjvO7muM-Nk_WlQkUBaTds_qRG6Rr2Ij2NV2DH-K0uLOKmowT35reDdRiJVK7ev7sEjcOI3KTCA2yYiWovxuCMXr0GpTq0aNUmLjrdf7zw12fQRFEK9l6mxiLcYowE-DmsZlUVthjrgfcGv_gY8-c_0iFmXbnCuEMwjTClOutrV7_lstpZYnhjVI_piCVrr0VpU8NjL7kMoKeSqCkpnfB6Q3XWAMsGNj5STRCXkfc_jA59dS5JDmgwqzvYRoHUK2f5Z2kRX_nzSc62yQIpc74IM5RubEpi7vyqSRjG6_bD_4PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یه دلقکی اینجوری پشت ترامپ ادا شو درمیآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/19409" target="_blank">📅 09:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI69FbJPycI64bZurgoDCS4QJ7KVR-4nfnBRgh9KNaYWqwJQ4Yh6iZfodN6SDMe2jQipT_rr-mR8k2yRZDtL7Z8D595z-XY3dgf9dK0oYkfdWr1BT7bB-pbrxQEemMbWTAOtAaHp69xfLTTZjvEJQ3uCXY7HCA4FwnmxG-KhesYiFASRyxZscfxM1FJIoKp3zIx9v7d2LokcOfa5cqahm7CrfHidrOhdj6EhLCHT1sWqcFBqbXBee6MmRBmzhAI6CmQiUzB-fDtrM05gTNSUlJvw1qveJyw7CCiaB_ob1rkdKlwyPpHrIq8acNojeSs2_nzSoVbwReJmsqL_rg3dAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏گزارش‌ها حاکی از آن است که بامداد امروز دو شناور جستجو و نجات دریایی «ناجی ۱۵» و «ناجی ۱۶» در حمله نیروی دریایی آمریکا هدف قرار گرفته و آسیب‌های سنگینی دیده‌اند. بر اساس گزارش‌های اولیه، احتمال غرق شدن هر دو شناور وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/19408" target="_blank">📅 09:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuGxwEf30Qbf68dTrp1N53C0oQBFBmzk5uAun_HnTc2Yfg3uGUV0Xesp4UjhsTa-hdtcpnj_7grKxOh-DxuNXGo1LlqzDbnA5z_hVo2qmhwllh9zNOcihvWkvRRmFSjaSwFCx_36MlIyKV3r2cELTE2PxG71KOWwGvX2tHQFtvhTnJQnOMT1AjM5YB0pzjBqg3gOugQFI_F_iiANm_JkJ_M1Nn5z0eGxmMXFHz1Wm1r4XGcGzipdi18M02eLUqPI1nEJiqifWbNeMkgbTpOQ996-bK3I8p3HdWewsDShvck9wU2f23K07IrArL8D6ngM-abYAQoy-QyoOxToPT0kAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان، با توجه به سوالات شما، حضور رادان ساعاتی قبل از حمله در شلمچه تایید شده است. ولی این که آیا هدف ترور بوده و کشته شده یا نه، هنوز مشخص نیست. در لحظه که خبری به دستم برسد، شما را در جریان خواهم قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/19407" target="_blank">📅 09:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19406">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لیست نهایی شهر هایی که دیشب مورد حملات آمریکا قرار گرفته‌اند
💥
شلمچه
💥
سیریک
💥
رامشیر
💥
بندرعباس
💥
بندر جاسک
💥
بوشهر
💥
اهواز
💥
بندر ماهشهر
💥
اندیمشک
💥
اسلام آباد غرب
💥
ابهر
💥
کرمانشاه
دوازدهمین شب و کشیده شدن حملات به غرب کشور
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/19406" target="_blank">📅 08:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گروه حوثی‌های یمن امروز پنج‌شنبه اعلام کردند دو نفتکش متعلق به عربستان سعودی را که در حال عبور از دریای سرخ بودند، با موشک و پهپاد هدف قرار داده‌اند. ساعاتی بعد، عربستان نیز اصابت پرتابه به یکی از این کشتی‌ها را تایید کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/19405" target="_blank">📅 08:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش CNN: یک مامور سازمان اطلاعاتی از تیم امنیتی معاون رئیس‌جمهور، جی-دی ونس، به دلیل افشای اطلاعات به رسانه‌ها، از سمت خود معلق شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19404" target="_blank">📅 08:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a54a3c2c.mp4?token=N92_RDZfkrLXp_5FPxa0W9SeGl-TEvn6COrjX1vuXvLrCgcZ4UzLvilV1PS9x-GdVwTR6KYJCGArp5UE-TJv4xJUw3vG3te6FDfIJFYnQKLMqvzNmPGjdnmWgFzWmI4KnqfpZbr6KPtvxgDjy-elMK4K4PtF0DV8lJ3uXH1bzAPPtBZWoDK6_H_rppzsN2-X_t7oFz6qo_TNysZefAE5kKhLuZue-zxXPmU5KTePXiJvSAXZbc_uNwDEXh_AeRINwg00Yn_1b9ESmHfIGZgOeNAunRy5J06F-WIyH6PqPOdIV3GtiJHxuOQP_AUWxO3puEhlEKlAj-wb8iM5Qti8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a54a3c2c.mp4?token=N92_RDZfkrLXp_5FPxa0W9SeGl-TEvn6COrjX1vuXvLrCgcZ4UzLvilV1PS9x-GdVwTR6KYJCGArp5UE-TJv4xJUw3vG3te6FDfIJFYnQKLMqvzNmPGjdnmWgFzWmI4KnqfpZbr6KPtvxgDjy-elMK4K4PtF0DV8lJ3uXH1bzAPPtBZWoDK6_H_rppzsN2-X_t7oFz6qo_TNysZefAE5kKhLuZue-zxXPmU5KTePXiJvSAXZbc_uNwDEXh_AeRINwg00Yn_1b9ESmHfIGZgOeNAunRy5J06F-WIyH6PqPOdIV3GtiJHxuOQP_AUWxO3puEhlEKlAj-wb8iM5Qti8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج راداری گذرگاه مرزی شلمچه
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19402" target="_blank">📅 07:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKBcukiXtvK9aASzUlJjkAXlj5VdfEPlWgr6V0oGYxQGPXu-bH63-JKR-maUGl4WiT8w55wm3QLtaAO6amsiPuqvwb3zo4gV47ERFrDiVh6OSeaVf98wQwbLgLesGA9M8aInxsM_ob2MXp42iohrABLYsApDiykpWyyT_Z-oEGA6LfJ8Ar94RZB4lx5eZPaOOvB1yyUJXFcXyiOr6mDQMUswb_4Knn6MGHGYuEmMJI846YX7BtyTnSZQVzmp7Pv7THxyQLXVUIRFdWeB3ltc28f2jzifTCWLtvbYwcFuJudnRsKIeZt3IUruzsPu68HEyNhyO9p5bDhPWTJE-AqV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: بمب‌افکن دوربرد بی ۱ آمریکا مواضع سپاه پاسداران را هدف قرار داد
‏اکسیوس به نقل از مقام‌های آمریکایی گزارش داد یک بمب‌افکن بی ۱ نیروی هوایی آمریکا روز سه‌شنبه با پرواز از پایگاهی در بریتانیا، اهدافی متعلق به گروه تروریستی سپاه پاسداران در ایران را بمباران کرده است. این نخستین استفاده آمریکا از بی ۱ از زمان ازسرگیری درگیری‌ها در ۱۲ روز گذشته است. این بمب‌افکن فراصوت توان حمل ۲۴ بمب ۹۰۰ کیلوگرمی یا ده‌ها موشک کروز را دارد و از بیشترین ظرفیت حمل مهمات در میان بمب‌افکن‌های آمریکایی برخوردار است. مقام‌های آمریکایی و اسرائیلی می‌گویند هم‌زمان با تقویت حضور نظامی آمریکا در منطقه، پرزیدنت ترامپ در حال بررسی آغاز دوباره عملیات گسترده علیه رژیم تروریستی جمهوری اسلامی طی روزهای آینده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19401" target="_blank">📅 07:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">معاون استانداری خوزستان:
در حمله موشکی آمریکا به گذرگاه مرزی شلمچه تاکنون دو نفر شهید و ۱۱ نفر مجروح شده‌اند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19400" target="_blank">📅 07:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf35d9766.mp4?token=awFuw-m-VoTFqvri0TkYqvBPFjUQmdGvnuGGcAEG6UzeHiwO0XzA1qpZI2K3zRfrvjhF_FprGd9ZYLuBojE1AhuSoYnPYkJuS-y9LWvNMRBhHTEHxvYj9I4dN3Efr1qWwYcdBGQfmSCwckmJxxEwZOiVNf5RawVcauVR_Cg3P5PhacY_DE-QquQy_G7StmuVwtfN1CafW4B6jISlEoHPeS-8_uyBmPcnZa6_IZRbVyp6oWg-2ErrRT_m7Mu7ddH5rG5lMnnfwKkT7dDFIp8jPHOTms66E7ejS4Z7R5TAqtDjrBlmJpI2L4wANHG_saCbLs1MyOSN7SUNubuVUtwYpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf35d9766.mp4?token=awFuw-m-VoTFqvri0TkYqvBPFjUQmdGvnuGGcAEG6UzeHiwO0XzA1qpZI2K3zRfrvjhF_FprGd9ZYLuBojE1AhuSoYnPYkJuS-y9LWvNMRBhHTEHxvYj9I4dN3Efr1qWwYcdBGQfmSCwckmJxxEwZOiVNf5RawVcauVR_Cg3P5PhacY_DE-QquQy_G7StmuVwtfN1CafW4B6jISlEoHPeS-8_uyBmPcnZa6_IZRbVyp6oWg-2ErrRT_m7Mu7ddH5rG5lMnnfwKkT7dDFIp8jPHOTms66E7ejS4Z7R5TAqtDjrBlmJpI2L4wANHG_saCbLs1MyOSN7SUNubuVUtwYpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰:۳۰ شب به وقت شرق آمریکا (۶ صبح به وقت تهران) در ۲۲ ژوئیه، برای دوازدهمین شب پیاپی، دور دیگری از حملات علیه ایران را به پایان رساندند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19399" target="_blank">📅 07:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19398">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حمله رژیم به کویت و اردن
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19398" target="_blank">📅 03:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19397">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19397" target="_blank">📅 02:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19396">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromrebel1</strong></div>
<div class="tg-text">ما رفتیم پشت بوی با یه فلاکس پر چای و سیگار
🤣</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19396" target="_blank">📅 02:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19395">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59327e2a3.mp4?token=T6aesOg4bRl_80asm6cbNzNPmsW4bE8q3hkVnVS4MTfsHcBrOFXLkIll3n6EUQ7DG6dZXcBVqrP0TtLrcpl_qKnWHNJn0BPwXzM34Y0YurtKQZax93Be67j0kRvNjlrFjR0pwF7DttCl3IAzQxIgco4lg5_h1gR7ostPAz3txxeDk6wSKpa242uQDJ3Ug-VQY2FJy7yhkTN49IOq5h-CExzb9Z7GZQJl0zC6S7boSVp55BE6aC-T6OalpIFoY66F-82TCq52qgQt_Sgqx7fZxoCsYEoyCQ7_5b6w0kowId6aHkESnmu7hy4jfjZQseNJVKkU2NqWPU-1tZR2Oy3iYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59327e2a3.mp4?token=T6aesOg4bRl_80asm6cbNzNPmsW4bE8q3hkVnVS4MTfsHcBrOFXLkIll3n6EUQ7DG6dZXcBVqrP0TtLrcpl_qKnWHNJn0BPwXzM34Y0YurtKQZax93Be67j0kRvNjlrFjR0pwF7DttCl3IAzQxIgco4lg5_h1gR7ostPAz3txxeDk6wSKpa242uQDJ3Ug-VQY2FJy7yhkTN49IOq5h-CExzb9Z7GZQJl0zC6S7boSVp55BE6aC-T6OalpIFoY66F-82TCq52qgQt_Sgqx7fZxoCsYEoyCQ7_5b6w0kowId6aHkESnmu7hy4jfjZQseNJVKkU2NqWPU-1tZR2Oy3iYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان لانچرها خف کرده در تونل آزاد راه اراک خرم آباد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19395" target="_blank">📅 02:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19394">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19394" target="_blank">📅 02:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19393">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7qD51calnFDJUtpx2FUFVMDLCjSDFBV_FrTlMKqMkGzhkuInKXyZwZsCDxQUWDYMYikYb_YgTtn7AuFegLyIJkAXnzUj_funo6V0glEnWqNTLq9yaLhT3JOiuxHf80sXdIyDZiFL5fel-LTkOdv1GAixsyj2GqH1gCApg3lsQUZSuJITD0-ZVmkI-4cq8KBaEqwLKXH3-Ttts3DydEc1LCcpQvjHEOkQcsevLexs-ZGwmSptxvDS3o26LdMXdjp5T7T2VpK1dhv6mmLZvTz_vq8R2OYRsokrV6GUUIb-6yGs13h7sSOGx42RJzCsAeQHsgdyglOFhZAGJzjsn39CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌های امشب مبنی بر حملات ایالات متحده به ایران تا این لحظه در مکان‌های زیر منتشر شده است:
💥
پایگاه دریایی زیارت سیریک،
💥
سیریک، استان هرمزگان
💥
رامشیر، استان خوزستان
💥
اهواز، استان خوزستان
💥
بوشهر
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19393" target="_blank">📅 02:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ادعای وال استریت ژورنال:
ارتش آمریکا در حال اعزام نیرو های عملیات ویژه، پزشک، سلاح و مهمات به خاورمیانه می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19392" target="_blank">📅 02:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19391">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فرماندار شهر بوشهر در ایران: یک نیروگاه برق روز چهارشنبه در نزدیکی نیروگاه هسته‌ای بوشهر، در جنوب این کشور، مورد اصابت موشک قرار گرفت.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19391" target="_blank">📅 02:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19390">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش انفجار بوشهر جدید
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19390" target="_blank">📅 01:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مجلس نمایندگان آمریکا بودجه 95 میلیارد دلاری تامین هزینه جنگ با ایران را با 216 رای موافق و 214 رای مخالف ، تصویب کرد.
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19389" target="_blank">📅 01:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19388">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سنتکام: امروز ساعت 5:30 بعد از ظهر به وقت شرق آمریکا، نیروهای آمریکایی با دستور فرمانده کل، حملات بیشتری رو علیه اهداف نظامی ایران آغاز کردن.  این عملیات با هدف تضعیف بیشتر توانایی ایران در تهدید ملوانان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه‌ای…</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19388" target="_blank">📅 01:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19387">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سنتکام: امروز ساعت 5:30 بعد از ظهر به وقت شرق آمریکا، نیروهای آمریکایی با دستور فرمانده کل، حملات بیشتری رو علیه اهداف نظامی ایران آغاز کردن.
این عملیات با هدف تضعیف بیشتر توانایی ایران در تهدید ملوانان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه‌ای انجام میشه.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19387" target="_blank">📅 01:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19386">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سندی محکم از قرار دادن لانچر کنار اتوبان و یک شرکت دارویی که مردم را  سپر انسانی و در خطر قرار میدهد تا در صورت حمله بگویند که آمریکا شرکتهای داروسازی و مردم را هدف قرار میدهد ، همچنین امروز هم یک ویدیو از هدف قرار گرفتن یک لانچر با پوشش استتار شده قرار دادم…</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19386" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نفطه زنی لانچر با پوشش کاه و یونجه در اتوبان قم به کاشان @WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19385" target="_blank">📅 01:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19384">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سندی محکم از قرار دادن لانچر کنار اتوبان و یک شرکت دارویی که مردم را  سپر انسانی و در خطر قرار میدهد تا در صورت حمله بگویند که آمریکا شرکتهای داروسازی و مردم را هدف قرار میدهد ، همچنین امروز هم یک ویدیو از هدف قرار گرفتن یک لانچر با پوشش استتار شده قرار دادم که شاهد عینی لانچر را به وضوح دیده بود ولی هدف حمله بعضی افراد قرار گرفتم اکنون این ویدیو سند و محکم است که رژیم این کار را از کنار اتوبانها هم انجام میدهد.
این پست را به تمامی زبانها در همه جا منتشر کنید تا به دست جامعه جهانی برسد.
https://www.instagram.com/reel/DbHEPESRguI/?igsh=ZWJjcW5qdTU0b2xv</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19384" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش انفجار بوشهررررر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19382" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سازمان دریانوردی بریتانیا:
دقایقی پیش یک نفتکش عربستان در نزدیکی این کشور مورد اصابت یک موشک قرار گرفت و آتش سوزی گسترده ای نفتکش را در بر گرفته است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19381" target="_blank">📅 00:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش انفجار رامشیر خوزستان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19380" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش انفجار دزفول
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19379" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19378">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پاسگاه سیریک رو زدند
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19378" target="_blank">📅 00:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAW3pKEhm5l4GNl4isCTaPxh56K0woeq8qFTWDJRsQ441SM1bN7lEcBxUiEoUPh1nD-g_vlIgGpQJN_xMrWNcCZHm7H15ZFtxqk0QK6WXArIpmLWDZadG6rTU6jcF3V-gT4iXPm8Hz1QkpuN9zwF0jzTEOtxxER_FnriV-ATj8N50fN45R9sGMFqqA29bT8z-gocNoUfH-Tx6_Tyk5h9SbPKu7sVoujECvwLHOQm_ML-_oY_5lVtqAjdUPu77kf23OnqMdku4jXRGPnYOJ01dffudiO6CaTIJ-4yQY9tp7yomsukhJMUuDlqFZAbGoXP_ko-00pA59xsTAzpoxIKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه ای که امشب مردم ایران منتظرند روی فلایت رادار ببینند.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19377" target="_blank">📅 00:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صداوسیما: دقایقی پیش؛ شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19376" target="_blank">📅 00:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش انفجار رامشیر خوزستان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19375" target="_blank">📅 00:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پرواز جنگنده تبریز
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19374" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دو انفجار اهواز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19373" target="_blank">📅 00:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش صدای انفجار بندر ماهشهر
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19372" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شروع شدددددد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19371" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19370">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش صدای انفجار اهواز
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19370" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19369">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">از شهر موشکی مخوف یزد موشک پرتاب شد
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19369" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19368">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسرائیل با ارسال یک پیام به هزاران نیروی پلیس خود آماده باش داد:
"با توجه به نگرانی از وخامت اوضاع امنیتی، تمام پلیس‌ها باید در دسترس و آماده برای هر سناریویی باشند، به طوری که تجهیزات شخصی آن‌ها در دسترس و آماده استفاده در صورت نیاز باشد."
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19368" target="_blank">📅 23:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19367">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حقیقت یاب سنتکام: ایران تنگه هرمز را کنترل نمی‌کند. این مسیر آبی بین‌المللی علیرغم تهدیدها و حملات سپاه پاسداران باز است. کشتی‌های تجاری همچنان با پشتیبانی نظامی ایالات متحده از تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19367" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19366">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00cad83b45.mp4?token=MtMgUrAdOebJXDq1vcHZ0NiZb3JFyQt_XUl468CmUzrVE1baNIFRTC2oIA3RyhexOApZ4yNoX4k_XFXEFrUxB3145Nz5ZXFVukeHzZnCYoSONQACNtbrn24Q6I6kWzfGOFu2qEcKTOOUhwHJpnXK0FuUcO8uasQvtFriHWdTa_VFHB8n5wJQRpgwbipblBk-oqKYvBpYWUxUU62SdWCxYvyxt5HQlONU8Am1zl3-SQtsnodV8KB_f5wBFz2qbG-pmg_aDehkznbdkiFBpltlKKVCZC_JOZLfa3DoxTdgfrZWXuluJ1OczoRuD3Fmz-of5aFtax2gkibLtmC_sAImwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00cad83b45.mp4?token=MtMgUrAdOebJXDq1vcHZ0NiZb3JFyQt_XUl468CmUzrVE1baNIFRTC2oIA3RyhexOApZ4yNoX4k_XFXEFrUxB3145Nz5ZXFVukeHzZnCYoSONQACNtbrn24Q6I6kWzfGOFu2qEcKTOOUhwHJpnXK0FuUcO8uasQvtFriHWdTa_VFHB8n5wJQRpgwbipblBk-oqKYvBpYWUxUU62SdWCxYvyxt5HQlONU8Am1zl3-SQtsnodV8KB_f5wBFz2qbG-pmg_aDehkznbdkiFBpltlKKVCZC_JOZLfa3DoxTdgfrZWXuluJ1OczoRuD3Fmz-of5aFtax2gkibLtmC_sAImwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
من آن را یک درگیری می‌نامم. ما با جمهوری اسلامی ایران درگیری داریم.
آنها آنقدر ضربه می‌خورند تا معامله کنند، اما من می‌گویم که آنها آماده معامله نیستند.
آنها آماهده نیستند چون بعد زیرش میزنند. اما خیلی زود آماده خواهند شد.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19366" target="_blank">📅 23:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19365">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">روزنامه سان : بریتانیا کارکنان سفارت خود در تهران را از ایران خارج کرده است
؛ اما نکته مهم این است که فعلاً گزارش‌ها از
تخلیه کارکنان دیپلماتیک (staff withdrawal)
صحبت می‌کنند، نه اینکه ساختمان سفارت تخلیه یا بسته شده باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19365" target="_blank">📅 23:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19364">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال ۱۲ اسرائیل: بریتانیا در پی وخامت اوضاع، در حال تخلیه شهروندانش از ایرانه.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19364" target="_blank">📅 23:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19363">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243d08a582.mp4?token=qqh1uA28DYIepxHQz4huXDxUvMv7H8tyBg_tN0cKzFPedcRG0Z3yyQ-H5HfpyuuDNeS6kM5wIWk7dbLG1lh3Kx0WXQBDQYJHfc6JQPm1sqP9CDDfYhykqTcY_MQ3l9FRdUfnhKcuSZxW-zOaOcUwRJ0G2UAEvIEwddeIRLzEVgOa4Wg0dm3HNSiGs-zQa8bfxamBXuC7KkMyx5OwPTr2uty0S6rT10wm5ErpNe56ITtKtTvEqfNQY8-_83Q6XG6TXQev1mQi58Vc12ntU4XRakRFAqESuxa7ukHQrDzq_ufgNU-6ud8GEBGcPuPP3ud6vKkOdvmmSQNkxVllyWukzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243d08a582.mp4?token=qqh1uA28DYIepxHQz4huXDxUvMv7H8tyBg_tN0cKzFPedcRG0Z3yyQ-H5HfpyuuDNeS6kM5wIWk7dbLG1lh3Kx0WXQBDQYJHfc6JQPm1sqP9CDDfYhykqTcY_MQ3l9FRdUfnhKcuSZxW-zOaOcUwRJ0G2UAEvIEwddeIRLzEVgOa4Wg0dm3HNSiGs-zQa8bfxamBXuC7KkMyx5OwPTr2uty0S6rT10wm5ErpNe56ITtKtTvEqfNQY8-_83Q6XG6TXQev1mQi58Vc12ntU4XRakRFAqESuxa7ukHQrDzq_ufgNU-6ud8GEBGcPuPP3ud6vKkOdvmmSQNkxVllyWukzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما به تنگه‌ها نیازی نداریم. ما به هیچ چیز دیگری نیاز نداریم.
ما به تنگه هرمز نیازی نداریم , ما این کار را می‌کنیم ,چون باید انجامش دهیم.
ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19363" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19362">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273ed05dc7.mp4?token=L7yzQg53q2F1yESjbl8V7YiDzof2ij-Mlm_FS79O3Ih-BlCI7FIP4t5zJNHMoHNfLmKjqKe5epZ1LbxhYgxc-qJoZbUQXLReCwDPpkRqvWu_zVSolp6tYbEhbi5WlRhWdovkif0Vs_A8smUM_zuq12r85bC1ljcs9USCR6vAgcqvBPWpsL4AFbHKzPZbho2J-ZDFqWFzN2VhTH2bzBXnPfFfi6sksUsT668hVyeL-DUmlcB-fD8odN0JyM1-98Gm28QfcKW6yP-G-Akxwq17cUz8uq6VBQuKBKB9iHXqfZeMDRN1YcBIqwvGOaxAYpdCRaHsICGr1t6tu9zLjfuLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273ed05dc7.mp4?token=L7yzQg53q2F1yESjbl8V7YiDzof2ij-Mlm_FS79O3Ih-BlCI7FIP4t5zJNHMoHNfLmKjqKe5epZ1LbxhYgxc-qJoZbUQXLReCwDPpkRqvWu_zVSolp6tYbEhbi5WlRhWdovkif0Vs_A8smUM_zuq12r85bC1ljcs9USCR6vAgcqvBPWpsL4AFbHKzPZbho2J-ZDFqWFzN2VhTH2bzBXnPfFfi6sksUsT668hVyeL-DUmlcB-fD8odN0JyM1-98Gm28QfcKW6yP-G-Akxwq17cUz8uq6VBQuKBKB9iHXqfZeMDRN1YcBIqwvGOaxAYpdCRaHsICGr1t6tu9zLjfuLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیستم دفاع هوایی مخوف c-ram در کنسولگری ایالات متحده در اربیل عراق فعال شد. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19362" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19361">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دروازه های جهنم   پیشبینی خودتون رو برام کامنت کنید کارای اداریش رو هم انجام بدید  https://www.instagram.com/reel/DbGvd4YRk8m/?igsh=cTlmeHd6bGVvYnM4</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19361" target="_blank">📅 22:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19360">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سیستم دفاع هوایی مخوف c-ram در کنسولگری ایالات متحده در اربیل عراق فعال شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19360" target="_blank">📅 22:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19359">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به گزارش خبرگزاری رویترز پهپادهای رژیم ایران تاسیسات سازمان سیا را در منطقه مورد هدف قرار دادن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19359" target="_blank">📅 22:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19358">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">۶ انفجار پهپادی اربیل عراق
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19358" target="_blank">📅 22:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19357">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG6hzr-SbwZ1RykJCgr7DdDUiL0wPLs9l81YaFpGeAgTfc17x7Jb6-aXPXo_Coo4lJ9WI5fp4u_hYAt8-gvrCrj-MvTLGnZwOexWvmLZTlOfQQai5x6H_qo0yNwPhw3194C8YD3XmDyya6APRewUYCrrrsPDrJKljbAD43wilOdBl8oKMJ4e9Ou8PhXZExpiuyyxJ9M26k8WYeyz7yZcoSwRclKUKGKmUk4szMoK-6upbZMPl3wZ0SCbtN0wwgRBATrQaQp6jBGoKX4A9AsOG-cyJ9xFO-37r-oZBt2S1JJ6LoM4Vatl2zgpZORsNH4QjUs7EX8qdrh0KvudMjNxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دروازه های جهنم
پیشبینی خودتون رو برام کامنت کنید کارای اداریش رو هم انجام بدید
https://www.instagram.com/reel/DbGvd4YRk8m/?igsh=cTlmeHd6bGVvYnM4</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19357" target="_blank">📅 22:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سیریک صدای توافق میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19356" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19355" target="_blank">📅 21:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سناتور در‌ جلسه سنا
:
مردم دیگر نمی‌دانند کدام روایت درباره جنگ را باور کنند؛ چون یک بار گفته می‌شود جنگ تمام شده و بار دیگر گفته می‌شود تمام نشده است. یک بار گفته می‌شود ظرف دو هفته اتفاقی می‌افتد و بعد می‌گویند نه، این‌طور نیست. یک بار می‌گویند دیگر موشکی نداریم و بار دیگر می‌گویند هنوز موشک داریم.
همین سردرگمی باعث شده بسیاری از مردم گیج، نگران و تحت فشار باشند و این جنگ را به‌شدت نامحبوب بدانند. چون تصمیم‌هایی را که رئیس‌جمهور می‌گیرد درک نمی‌کنند و با آن تصمیم‌ها موافق نیستند
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19354" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سد مجید گشاد زن
فرمانده هوافضا تروریستی سپاه:
به پل ها و نیروگاههای ما تعرض شود خاموشی برق متحدان و میزبانان کودک کشان قطعی است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19353" target="_blank">📅 21:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بیانیه فرماندهی نیروی دریایی تروریست سپاه(همون چرکه):
ورودی و خروجی تنگه هرمز مشخص و در کنترل قطعی ماست. مسیرهای جایگزین ، نا ایمن و خطرناک است اخطار می دهیم استفاده نشود که تبعات سنگین و غیر قابل جبرانی خواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19352" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صدای انفجار‌ در کویت
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19351" target="_blank">📅 21:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD6kSQoNX_9u5r-nnwlDnzRBcE69E3V9kx-s-NWNuZHOeKG-pzLk4T0nU1XFXEcZYhzWcje3BlaIfd-2YylXrITBI3RGqz8u7pIPWux5qIGAy7Oc0zMDQTodmVgSu-8oGsds03ccfi8cP9KgAMw60vWriAKzXfPf7kwbgwNQEsbRIfmmDk233S4CfSANBAFxpnAhjQht45DU1Arr_yYk3GpOmfL4nL9BVAbClAbu-uwyUej1oSXpjdYBdaTeAz-Or7ugZpZYS2JxC8qYs_8yiwECotvRLbY-bMN_McP0RIOdeamLH5iqi-XErnrRvQ0v4RM6fyPknDn7K14C5ei1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که ترامپ بازنشرکرد
:
به سنتکام دستور داد شده دروازه‌های جهنم را به ایران باز کنن بعد از کشته شدن نیروهای آمریکایی
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19350" target="_blank">📅 21:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19349" target="_blank">📅 21:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">موج حمله موشکی جدید رژیم
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19348" target="_blank">📅 21:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خبرگزاری کان: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19347" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy1XTP20TIUKN1QwQAbuW6JydAfiUC9o3j7EoyA2NWgSb3_6ELkhUBFSU9pMsRsQJ0ziJTZHKOe1930e20P9kor5uDXx_6Z5gyjKrovH8M5lg7M0_p1vNq5hkyH03jKjVcH_z2J86_I88fgH7g7W86HDI31d2nKmrPUyMJvR3lR4QtBMGkRlGnTCMdy0Z_i7_1wuqhXtE1TxESBeoSKlYkIm6Tj30XEzJ-JWBWyH2Pq9Yunj_fcCZT82DapYitwOSSGNWTcyAdyuwYfWTyLzqxjNx2E0mk92LzxaUkGvT2igx-ci8R2mj5VPiH6t9c0SZuKUFb34BLpBqWeET07Y6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‎سنتکام:نیروهای ایالات متحده که محاصره دریایی علیه ایران را در دریای عرب اجرا می‌کنند، طبق اعلام سنتکام (فرماندهی مرکزی ایالات متحده) تا تاریخ ۲۲ ژوئیه، ۹ فروند کشتی تجاری را تغییر مسیر داده و ۱ فروند را از کار انداخته‌اند. ناو یواس‌اس مایکل مورفی (DDG 112) عملیات را زیر نظر دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19346" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19345" target="_blank">📅 20:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حمله موشکی پهپادی رژیم به اربیل عراق
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19344" target="_blank">📅 20:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">علی‌رغم هشدارهای ایران ،بلغارستان اجازه استقرار هواپیماهای آمریکایی در خاک خود را می‌دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19343" target="_blank">📅 20:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d436f581ea.mp4?token=cWOWByfBfMTHOcL0ClacaZAvb_e5dwZzljKtZwWPax-MMEQMpU_yogYVqBprrIwhYkoFntIgimAfADl2DSNDJowYDsnWW3lNe4tQSqq3TUP31Uzb1bZyBYCRcxxoF8SVa31gp_TDZhE-msOsIkU-e6LnWDxLzyTVg1tVtHQObCEbsO6kGwUfzUzpKqVG279RoamHJjLehmRm1cipXAAV7h6Jjb4BIlaGdcBpXgET_1B_Xz3o5xj_U8zG8nnHBj3QKwR751RRjTtDMD6NgXRV0BLjI6LBVwoowiTBCEsRlqJ4rzzbyJnwxDshkJmbEmBd1dUpeh05vLJ29uyJCIQ02UWe1JtMOvuE2EF45t6jdVVOcBzi9-yAdDCuMbjx3bEOgPskJQZcEXKsElDCh2tSgWPAyxLcsCE32hyuH7M7sca7dSj1XHpMMAXjOG6o-hZh7qGkuX_QW0hn2qDdIszTc8398b8ONnJINVCYpJXSfrTcGLLbf8zSZOUOB3sIjW6zmPl0bhtN21GBqL25ZAAdl20EvbQljKXI-Q_UMyl6RahOTpGZ4S80_CX5dTDlMX6VMhmYpiPoI5iDJJE565WedYfmomOPiwHJUfXYCt2miyhH7i5-_kOMpq_D5VfZCKu66Q8xsGXjpI_u8vG0xb8ZMP3spthdn-i_bqskrA1Q-mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d436f581ea.mp4?token=cWOWByfBfMTHOcL0ClacaZAvb_e5dwZzljKtZwWPax-MMEQMpU_yogYVqBprrIwhYkoFntIgimAfADl2DSNDJowYDsnWW3lNe4tQSqq3TUP31Uzb1bZyBYCRcxxoF8SVa31gp_TDZhE-msOsIkU-e6LnWDxLzyTVg1tVtHQObCEbsO6kGwUfzUzpKqVG279RoamHJjLehmRm1cipXAAV7h6Jjb4BIlaGdcBpXgET_1B_Xz3o5xj_U8zG8nnHBj3QKwR751RRjTtDMD6NgXRV0BLjI6LBVwoowiTBCEsRlqJ4rzzbyJnwxDshkJmbEmBd1dUpeh05vLJ29uyJCIQ02UWe1JtMOvuE2EF45t6jdVVOcBzi9-yAdDCuMbjx3bEOgPskJQZcEXKsElDCh2tSgWPAyxLcsCE32hyuH7M7sca7dSj1XHpMMAXjOG6o-hZh7qGkuX_QW0hn2qDdIszTc8398b8ONnJINVCYpJXSfrTcGLLbf8zSZOUOB3sIjW6zmPl0bhtN21GBqL25ZAAdl20EvbQljKXI-Q_UMyl6RahOTpGZ4S80_CX5dTDlMX6VMhmYpiPoI5iDJJE565WedYfmomOPiwHJUfXYCt2miyhH7i5-_kOMpq_D5VfZCKu66Q8xsGXjpI_u8vG0xb8ZMP3spthdn-i_bqskrA1Q-mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو در پیامی به مناسبت نهم آو گفت اسرائیل طی سه سال گذشته با حفظ وحدت داخلی از بحران عبور کرده و به جای جنگ داخلی، در برابر دشمنان متحد شده است. او تأکید کرد که این کشور با وجود ادامه چالش‌ها به دستاوردهای مهمی رسیده و مأموریت هنوز به پایان نرسیده است. وی اعلام کرد برای تقویت وحدت داخلی، در پی تشکیل یک دولت ملی فراگیر و باثبات خواهد بود که امنیت و آینده اسرائیل را تضمین کند و افزود اختلافات انتخاباتی نباید مانع حفظ انسجام جامعه شود. او همچنین با اشاره به تجربه‌های اخیر گفت مردم اسرائیل در لحظات سخت نشان داده‌اند که بیش از آنچه تصور می‌شود متحد هستند
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19342" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ارتش آمریکا در حال انجام عملیات تخلیه تمام هواپیماهای سوخت رسان و ترابری خود از قطر می‌باشد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19341" target="_blank">📅 20:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۴ : سپاه پاسداران ایران، ایالات متحده را به حمله تروریستی «به سبک یازده سپتامبر» تهدید می‌کند.
خبرگزاری تسنیم وابسته به دولت گزارش می‌دهد که سپاه پاسداران هشدار داده است: «اگر جنگ ادامه یابد، ما عملیات پشیمان‌کننده‌ای انجام خواهیم داد که منجر به عزای ملی در آمریکا خواهد شد.»
آخرین باری که ایالات متحده برای یک حمله عزای ملی اعلام کرد، یازده سپتامبر بود.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19340" target="_blank">📅 20:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">منابع جمهوری اسلامی : رژیم ایران معتقده مهلت‌های آتش‌بس چیزی جز فرصت‌هایی برای تجدید قوا، سازماندهی نیروها و بازگشت دوباره به جنگ نیست و نمیخواد در چنین چرخه‌ای گرفتار بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19339" target="_blank">📅 19:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری رویترز: شرکت هواپیمایی کی‌ال‌ام هلند اعلام کرد تعلیق پروازهای به کشورهای خلیج فارس را تا ۶ سپتامبر تمدید خواهد کرد.
این اقدام به دلیل وضعیت بحرانی در غرب آسیا اتخاذ شده است
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19338" target="_blank">📅 19:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اکسیوس
:
شرط اصلی ترامپ برای برقراری آتش‌بس این است که ایران حملات علیه کشتی‌ها را متوقف کند و تنگه هرمز را دوباره برای کشتیرانی باز کند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19337" target="_blank">📅 19:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رسانه های عبری : آمادگی در اسرائیل ، احتمال درگیری با ایران در آخر هفته @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19336" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرنگار الجزیره:ایران ایده آتش بس موقت با آمریکا را رد کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19335" target="_blank">📅 18:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رسانه های عبری : آمادگی در اسرائیل ، احتمال درگیری با ایران در آخر هفته
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19334" target="_blank">📅 18:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aON9zb0OvOskiXPMRopiCDFPG6tL5b1JdgEJTHaKcA31oZrbBjBqcA24xRvuzg6VbrIOd99D4V5dtygZFujKr-_8xMah3meqGMrl05YeAcfgoBn7lmDZNZbJQeuyBlBtPwo9Mou1vmxlF1rA4_WsEXDFO4RWZo41eCM55NkIih4lQA0HGwTAM2DNfDFkQ2rgg4qrhHKkNR2E0GkG3D5wNVYdl4mroWbRw30PNLNM4CAGy1ID0M8PAfDV65A8u_RRU1AhqByF26QQLPDy4X-4TaH43zYj5VCdJNJ3SlmPVd7pHQ4Mhm36CwCw0RhYrLHo_6UMy4qDxUBhwA8srEqHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از خوشحالی عرزشی ها از مرگ سرباز آمریکایی در هنگام خنثی سازی خدا به کمر آنها ضربه ای زد و جان دو نفر سپاهی را به همان شکل گرفت سردار احمد احمدی و سرهنگ دوم پاسدار مصطفی جمشیدیان از نیروهای واحد تخریب لشکر ۸ زرهی نجف اشرف، در هنگام چک و خنثی سازی کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19333" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA0jxU529StCbPZggNnTcudEf9lNdNOhJi69H7WcaDfh5RpJzDLdYZLRFfei8L9sgjqs6gfj5p2xHIN80w0Cy1oXsw1Mm7EmLcdxbSTIii4R5fCVlIi8GqL_U-SJR0Wl8AqDpc6_X3pPqiTGzj1GvsIXaZGsjuf5r2-FC3RrWHCNDP95bDcQTtmjJl1zRhDRiyMfgMib9ti7GAZ3ao6uCx4C7wc7OATIhMWKOf08PkbLTUs0YKo7jVe0YZL9HGAm_T5a-ZTx99oEFF64Ng_AHD_11yJxVc065ZGRsFD89wj0jJ8Sk_sMqtDfhgjWnHayVceeZ3I11SEMbMVhnJ9Lvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک اسکادران جنگنده پنهانکار F-35 با عبور از اقیانوس، توسط دو سوختستان استقبال و کمی دیگر در انگلستان به فرود میآیند. یکی از آنها، احتمالا به علت نقص فنی یا برای نشان دادن خود به جهان و تمرین ، آلارم فرود اضطراری روشن کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19332" target="_blank">📅 18:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آکسیوس به نقل از یک مقام کاخ سفید و یک منبع اسرائیلی:
کاخ سفید و دفتر نتانیاهو در حال هماهنگی برای برگزاری دیدار احتمالی ترامپ و نتانیاهو در دفتر بیضی طی هفته آینده هستن.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19331" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfead895f.mp4?token=LOquTLfmYZxpKVUZzSU2b38ho2PfwtJLaQLO715HWoQyi3x-yacNQL0LK1YSZoooEUMnBb-o2uGMAVWn6CGiAv8zjafqyAtRlFaflfHs8KBjQCMf3Lgn2mcNrJQeLY6Dbl0j9ugrczr_i1Pgh7x-PL7A1fLhHMcypbfaavemiC8A19bmlLCY60IB40Q43mHu7OFkE8oqu6JJQv4LGN04jY7AkRxr7Hk5RAsDxOw8jtUR1XoxC7dLF-TW1rblmyDT8ZU2Hyr1iVXNAkxwliFow2MTUqxuYOJ5GulT1Z6_YCl7YlltwbVEfeujy9JRm43D84hyFt2Q3r7elGccZwpT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfead895f.mp4?token=LOquTLfmYZxpKVUZzSU2b38ho2PfwtJLaQLO715HWoQyi3x-yacNQL0LK1YSZoooEUMnBb-o2uGMAVWn6CGiAv8zjafqyAtRlFaflfHs8KBjQCMf3Lgn2mcNrJQeLY6Dbl0j9ugrczr_i1Pgh7x-PL7A1fLhHMcypbfaavemiC8A19bmlLCY60IB40Q43mHu7OFkE8oqu6JJQv4LGN04jY7AkRxr7Hk5RAsDxOw8jtUR1XoxC7dLF-TW1rblmyDT8ZU2Hyr1iVXNAkxwliFow2MTUqxuYOJ5GulT1Z6_YCl7YlltwbVEfeujy9JRm43D84hyFt2Q3r7elGccZwpT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، قرار است در مراسم انتقال رسمی پیکر سربازان آمریکایی کشته‌شده در جنگ ایران شرکت کند.
ترامپ پیش از سوار شدن به هواپیما، به خبرنگاران گفت: «جمهوری اسلامی به دلیل کشتن سربازان آمریکایی بهای سنگینی خواهد پرداخت.»
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19330" target="_blank">📅 17:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش های بسیار صدای جنگنده رامسر
@WarRoom
😁
بفرما زدم دیگه نگو</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19329" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4d4e3672.mp4?token=ZkJ16ByTjhMDc3Rab7sY-uChJqTr994gt4I_cavHiUz6BhC8Q6BBX5zJAyRhakR9gs9IccwvAB5F-eBHtUahp-UXT1p4VD3zclTWd1MRkA_9Oud1DdQOscKtxqk3GepoufDVNOgWpgSUf9bPYwO9NZQl7aNBn6h3rouwIVfSbXt4_C5USPSqKN7H-hstPhLCeFM_oTZGtNYvfUDocD3dcmDZIrEjWoxKx6Z-shUiZ922_CSUTy7KovlU9GhRhY1DBQK5kd245WcSTczpTCW0JnGBdb7cEeiy6uSl2Qs0TGJdJRxmLr0nHislbzsimFq3344GWNWPUNeISJXgTYb0Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4d4e3672.mp4?token=ZkJ16ByTjhMDc3Rab7sY-uChJqTr994gt4I_cavHiUz6BhC8Q6BBX5zJAyRhakR9gs9IccwvAB5F-eBHtUahp-UXT1p4VD3zclTWd1MRkA_9Oud1DdQOscKtxqk3GepoufDVNOgWpgSUf9bPYwO9NZQl7aNBn6h3rouwIVfSbXt4_C5USPSqKN7H-hstPhLCeFM_oTZGtNYvfUDocD3dcmDZIrEjWoxKx6Z-shUiZ922_CSUTy7KovlU9GhRhY1DBQK5kd245WcSTczpTCW0JnGBdb7cEeiy6uSl2Qs0TGJdJRxmLr0nHislbzsimFq3344GWNWPUNeISJXgTYb0Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس : بازی خطرناک تشدید درگیری؛
مقام‌های نظامی می‌گویند با نزدیک‌تر شدن حملات موشکی ایران به مناطق مرزی اسرائیل، خطر گسترش جنگ افزایش یافته است. به گفته آنها، ارتش اسرائیل در آماده‌باش کامل قرار دارد و مقام‌های تل‌آویو معتقدند تاکنون یک وضعیت بازدارندگی در برابر ایران ایجاد شده است.
بر اساس این ارزیابی، مقام‌های ایرانی نگران واکنش گسترده‌تر نیروی هوایی اسرائیل هستند، زیرا ورود مستقیم‌تر اسرائیل به درگیری می‌تواند خسارت سنگینی برای تهران به همراه داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19328" target="_blank">📅 17:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBYV2E4LmZwdkxiI1st0Bcnw3K5GJE_6dwq-9iJSH-krZs559hyFTBVJ6FgyFRF9NBr8jRKjZr8jrJhzxxADknlVPKI8Ztl2pDjg_MzOIFHunQC7amUGKHNONosy3Cb7xGZSQtjRJ9DCyILAxH48B6bCrm4UmWSaaqWrulATojZJb4HwK1R-kCULAeaoELH7lKmsOocZl4bg8n8axHX0Vpu1EYgtTTq3xhjKOBKvAQNYqLnabbxej0wFHA2cwz-fIHV5ke4pddVJ0jdJyPk3P5821BR7JqTOBOYt369NWbIT-VHATujxAjtvLNxBg5d_KC4R8-0OG1T8Zl6X_wpKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراغه الان
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19327" target="_blank">📅 16:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phO1i6Sbo_9sLcsDEys-2CUD03Hi86NpZMFf65qgtpkwGCsU5t4bW08dynqhOD6MG4pN8RBropGFHhBQ0nAX7xyVfx_vcZXuGW4hb6oNs2sJHfryNmzpHJxXrBkduNPWX3NCx5dfW0TWYNV9oUWIiFSxyF1kpoeQ5mjOypmtSUZYoGdeP_WJTSRAhag8JqgqP0laqV7nqnCgxY2j_mVviWHybTLnLHTqTgwwtPPQqDFe3VHAY72pvhW6JPP3VWurtM4sPPwBQoBTe_y2NBko6q9ztqCeyBVz4L1BYgi2Xy_aupgVwI5SnQRf4tkTCdUNVwJsnBZADG_8CAZ9FVozlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این لحظه به بعد، هر زمان که جمهوری اسلامی ایران به کشتی‌ای در تنگه هرمز شلیک کند، چه با موشک، راکت، پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه، از جمله آنهایی که در کنار یا در پایتخت تهران قرار دارند را بمباران و نابود خواهد کرد. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/19326" target="_blank">📅 16:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19325" target="_blank">📅 16:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ در‌تروث : من به پایگاه هوایی دوفر می‌روم تا از قهرمانانمان (سربازان کشته‌شده در حمله ایران) تجلیل کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19324" target="_blank">📅 16:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3pF7qGDfg-EplXQcdvnfw1CEL0v3UWJxjDFP2F1hKrGbhQ7yuOVeLhR3Ba51_up6_PMSpO7WCxpw0BMskhdtEeVMWa1KtUWOc0BSTZsIouw15Yd4NWfHnhpXM4WU4Iz9J7gaTdL0hjfQhGHsPtKtQ0vrHOyjoujwZBk7Guobd0AbSZHtqUxyOCHeC-ZphrwbtSu7R7GESrqT-3U1ByB7DVQrDKCAWG-7n3ayQRy_xjf3B3VPzdOi-Sc2iHWi_l5KHOYLnkeK0mxxWX09jNkic-tCICOm34ahBBt-qsbVIBKuroWSyRhoplu8KmFLCyC8wAXSkgEEP_4QigBLMKhvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3OxBpZe1uoHeNU2NzENDnXyvhojYBVXB8hfHfbV0SwHQndQCfZScJYnvFxELrEtw0s6C20QsyO1f3_o6_n_adv6y0KNYsf5IYTDdKKJiRtkK8P4TSaa6ZbArlRvGvHkrCatsXcffUDzEeKs8V3HRTCRJ6tI_W1Oc1aiqz6MPiEwjPcSFTEIpDh7OMhPVrB2N1TY6k-PMZ9Ov5BjBcjVnw9PA_Bhq1dE271z0GeZRfasLK0MNDyt-WAfgG4-SgxmFCPrAZsI-A1y9wgWqcFTEogDvGXNdHueTWTsn7rtYzdW3wx-KH9DGhGjpVoz2o2ev3AnNqA6ei91NeA5Jz0uyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJajh_dfHO9BdVeQpplVklHfPuFyTEVjsIBeaWOwx9YvTMstLpg-OE49ClN4MFhNsRV8hA9Z2MqEFB-aPUAS_qCmvDtM5uOVgvse26MqL3BHfjSdJ-2LeaJ_bTb28TcpjtpdaWGw4bUqa3ujRSNPPWi0niDoBaSsiVEBLU7j6yOdLhzATDGHaU0wdf876EA9cYWq94Icxp7QiTElbZAEJjkILu7uCuGMXXxXufQf4wNZZgLH6ZTyb-NNGHBUcNhHgBD6sSMQBL2pU5I_inbrZabmB84JcwS6VEIBKX9TWUJqmgcvREAqu7_2Zx78frbkEXaq2qEUqrvbpI_iqmnJTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01649fbed5.mp4?token=Qz2kcbCTzxBR0ghoJXh_YOuY4IA629TS2CvncV9RuUEP2HBgQfDpBD6t1jSVmGzuGnOfoglmhX4esGJFN_ybVm_lKRLJ0xRFQzbFZ5PYi44TTW8C9KRAkcYnItChD8JYxDej923z8H1C9i4Za7n4xGr5eWaSGp8NGoCf441PyM6Vropy-92X0BnoEyGRDMIshzd8AfQFBp7U5pJ8yV1GQxVGoWTll9cD7LAXp-TdAVA5PHdvrL_cx46dafKs3m7epgz-UKQ_5HrUoQC4QCypTk2n5Kg9bgf3MZR2snTl6rF93Tf7A71JjS_O5-uqZ7pQzsc7wzZIMuWWOyrqCMdRyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01649fbed5.mp4?token=Qz2kcbCTzxBR0ghoJXh_YOuY4IA629TS2CvncV9RuUEP2HBgQfDpBD6t1jSVmGzuGnOfoglmhX4esGJFN_ybVm_lKRLJ0xRFQzbFZ5PYi44TTW8C9KRAkcYnItChD8JYxDej923z8H1C9i4Za7n4xGr5eWaSGp8NGoCf441PyM6Vropy-92X0BnoEyGRDMIshzd8AfQFBp7U5pJ8yV1GQxVGoWTll9cD7LAXp-TdAVA5PHdvrL_cx46dafKs3m7epgz-UKQ_5HrUoQC4QCypTk2n5Kg9bgf3MZR2snTl6rF93Tf7A71JjS_O5-uqZ7pQzsc7wzZIMuWWOyrqCMdRyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشهای تایید نشده از حمله آمریکا  به پادگان همدان
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19320" target="_blank">📅 16:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رسانه های رژیم از قول منابع در سپاه : دستور مقامات ارشد سپاه برای گسترش دامنه درگیری در غرب آسیا صادر شده و ضربات در ساعات آینده به مناطق غیرمنتظره خواهد رسید
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19319" target="_blank">📅 15:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بیشترین کمکی که شما به من می‌کنید انتشار این پست است. حتما مطمئن باشید چهار پلتفرم را فالو داشته باشید
🌐
instagram.com/yashar
🌐
t.me/WarRoom
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19318" target="_blank">📅 15:36 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
