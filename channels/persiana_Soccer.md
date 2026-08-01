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
<img src="https://cdn4.telesco.pe/file/Yu8IiDtjtDBz6CJlqh-OZ8aUXrfjmQRoYRmSET3mXIxa2rCI167tw8Ef6aQF4UmU1-Bousy9mx0ZU1-PrzuNJAkTzUq-A9CajtVP_Mq-QOonHJ01_YfljT34rOWNUZ_KyNx3kUnx4jM6l3RpOcN48FkdxArvsoK-ipeebp6-Y5UI5DG4AFLVXX5d3f3yuRJSHQcedTjRGhOJa9VzW7NpFIt-ojkG2SKbcfNqfGfvGZcXcfuCysB-vEOdO-xe63Lr5-OBv_bSMfJW6ezwmxsB9c8om4gHeOqGMyfJOljS72rjNtlnN72TaCOKN9rlViywMmaaRIF0SNSV_OTREiDXTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 17:57:25</div>
<hr>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVNPF5ylIfHw6rRcCHblYkuAx1f4tdqALGOwWz-Pv8SmhtVYmHrggrtcwbx6ag1zMuxZFoYVIL3mvHjH5X9IUDKRNqrqwxrq_GZX_jMeyZUYvfQzmATi2X0F4FtToT09G4D5oDzyKehXww3uV5ogHFU2q77wD_gHMACMXveVaNkAZMKNVFbkdDC_lf6GTghalY2qdVSD_ZWjfJnnHgE1VaNEnelZPD1ggXC324BxqiilGr7dGz_aS_pv4shgdxEZQLAHlmfDyB5hiUpfy6Jc-LBz-3ezjuV3XjostusFuISOYqS-whsTfL9mSysDzopvqaUigoZLCBrpvxVQkFajBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZYYm4cxJR7EHNVX5PIwxar0KR26YhOYGgdj48kwhD0W10wIjMUX3djAlK3KREUBW3S9gNnC6-6JbWOb8nJdSTlEse-AlWyXbxroOrHs2wEHRzVVVod-TC7KdS5liAKO3_fVu610JRojFFNKe1KuDWqGhyXyjNhejnk3xXspzH7q96DyfJTN6cE5Rw24mHEFaEn-7feUxaBNdu58WzrgCFzUdlBSEjPZNt65yfe9z-SvOyp6C2-evlHQTvPSs4g7k06ddmooWd9PDneQxx4EgYg06Jw9sJ2swJN25bBdgzNwUmRIt0Qf588Vt31G4QHLrYS4QpYe0ve_0PtD7NUWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3XPZChWv2TYjxTnrvlhhZuuRH4m1HTX_CuZw12ZFwobKCO41195qaQDpYSiMFPYt0g2fHwQP-QRvTrZlXfy9kVU7wSajBvMRTqTr-HYGdYY_B8AzITX0JsuQ-EvOYYjy5bYSedcPSe0pr5csG8WOjT8NnxskyIoMkBwN4IRZfbFFW16jzHji-fOQXRTEIh6FU8AtTc9rTH7b1d9lZEwGLyL_AGz0tghN0zxSwAyTXgDL-XqW8cLaZtAqOW2kdu1Xh7r5R3UEkezwCoPdmoejbD1Uc9h_U2n-_3dL7L705pM_NZI6g8nK58CcSzaE4vr4kIcJaaI7Cc_ZiMbBrEN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufmYeDQ_5J5LhprzJyRvfl72SXFUICslBSSLJCjcmPZ62x3Mj0FsoHmDmnAhut_9bkp6Wbu-QP0oSFQy2k5HGyak7CDwcmtoReYXb3MDD4XUY-9DfdM5kkHhixJXlk9dsx9RLJw6sE28CnitjxltjqmPIGIBBZUkeEKDtcqcGSykzOCDBNAS75X1NynaUq7nkqbOvzXXMnbSw8Elqz1TVGQna-RUOISXSKqWPn2c0BCxchRfO6UKlto371SseORtAP8V1TqDsju_WtR3xsjutLij4Ifpfz0VsImgSLBr84e7aPNflifC3T8oPx0QCxS6iJGd2X_S2SVTmq3llP17vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vev9AcsSR_XTbQoOUH02RttiuAVPsvEikWkpVai-QUIV-4diZEHXMlI82RwofTZfO-5XqcFPZlKuSEstPuNePXfkKhB_6nMPRYM4hVCIKcMLe2vuVqGAeo_n2V3eV3wM__EiieOFm6A8D0LTheZMQ9sm9VMHDuJVqqTj54wgJ0Tm82CHWecbkHBWvmJPXFbFbvuEK5e5rYKwJqgnZXjxDbMp7jur6irm-4PApAZSfKw0h3ns0I9xfvxkrAo6xMOijtIBvVs1-8cAN8lh2uIlPl5v9UooyYolrZ0b1uBPKNGU0IyvYbjYfDmikFZ2inx6PyT9sdP-TmOqXrMKQ5JM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSCyDKaxOarI0GZaK4-PJx9Rz-xiuQ4BSqsi9lks1TefYoPqXKimRKuRyYvOcQu__5LAsoJ5jpI1ZKPi3OPr2OUKbCncY0ZvsXvo-GFqlU67-Z1sttEoHANHhwjx_M5swY8IFoiDVGikyfjIHyMdctw2DTjhSPsL6yHNcuuNt1wowTWe42FplNGWEuMxs0FRmV7i8LiHxthOwO8GYWvnjJCaw8NmC-GfQUEAg3ZWVm7qMYwn59mBbfMbI6rJIAN19im7UNFWz24Rj8R47xcnu4lwQhmLFaj_cXtpVMhwJmPm7rPdfBi5WO0Jq-hQP48uUclMtgNcBP3fH5bCvMcydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSbXVg47Al8IkjRVuX64CUtBIT_UmUi1Y6v4lRA3KsdyCvg5LbdPOichGJhVK4G1kwovVb-3TdFV3GKwea0sHMyGJO2hDEVZjSaY_bKj5RUZGYWtki5wzsGhHi9ic85U58arGBuIFguwvQgC27M49W8ckzDg5YrvNlKhApY5N4r1GIGz-h0-MNOECYn1cA3cpjb2nzIwKdDbFSHijcrxc9uYl6hDbY0jM6cPyBa-HePahHbx8dwfmjQAnyxIanbuPO2zxkHyiX3moahfhFN6SXNR9-AL5UtJ20ipHagGtjas6cozYoodkiO4SeZgYYxEcL_57aRHoxejW_YX3j4NYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5Kye87fZZaI48VlwD6ZHR2zbbQjH0rOZCI4xs549sG7AkwhnHMj7eJcaMOaKruKheYo2VZj_kRIi0SWRTCBFoVbxWEuihDoi7EFHF1TfLfOEuz0iV1781NgptsqYu9eu2jyZL1RNEbTtG9-SBEj007ZzTa-EG3eTGCEHB4nMpR4uKbsYeq4VNYOR_NzHS7GX2On6kg_Sz7_5LvOa4E3WWsWbsOfhFMKKovXFVnqimJRAJudMEq8AO48jRGH-AyB7-9GD1x5nGUenZCYXoRXdNzshYouvX2B4PEN-vdRXeXaY3PGtQWdLK_odKygrtcpQ87b59SFsyezBo7AHfDsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kojPwKPGswjunlkauR1LyJpQSHY859fod9vDP5utZPb4jsSGEGdPSEf0ylJuFIqkXzet87s17JbV0_vNGzl6beWAkrMYFsaqJf6fXx6hfHhurnBTxxK7Fh1WYJiJWHaEU_eWg6-uV_t2wyh6pwi8K-E2DEUUNqVcrge3CKUBzpOY5b03plUYUg6fO7QXz9pOY1Vx03pBdvtXovTWQxQPGux1fh4ema3x5uvosmUugoE7vkX5vY2p938CkKuDKmFikpvELhFdPJ4Nxb-uaMBYd78aaLHbAStHIUjgBdKiffPnst6tCts1oDETLxzY8W0NQkuwaQRmY_n-iiaKmjSpww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5mbmXMmvWGHxKi0E1RKzwlktpyCZUVOnHytEF4ToBD3jHUsi-IjCnKvYz3Pi5ysD4xruDieD29fTXKIwKGyJ-NKWBkn9nFtWXGvBs7XchA8alvlV_GihrON545R229R4H8otF7zxBCIt11HakJeXRo-r-D1VgD3m9_GfGufuir81VyZfsAQ7mlY98T8kLkSTtEiQdu0dE5UzjAX15cAy3t1ZyEx_3TRGp-oC4R0xwS5JTzUbulArT8AD2KD94kWuR-MLHg0kS8lFMOnVBqu3xrji4g-XXAxoDMZzWh-Hrr7nn1AYwA_783fW79YALlmLcmmMfFOA4CnizlmU6ReGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eezm3_wEa5GiZ-Uosk4dh8Ymk-tN4y2sAOhlVpe6Kyo6hs-byj9DyeFjPA8CeW9lqbC1emk2W0uTktiox5AQlvQgPj0kpB4O9_9g5O24tVB51pDFRrZP9NukewHzQk-DmCC4eEcRAtfKIMOpFq2CYATvwkPVslz9s_6p2bUtZrLJf3kQZFFJpdsyA3iWK9C9g1-ngfzFUhSstI8VuBCWAy03qJTDWHmcbewgUOsYxvPy5jvVyBN0aXxK-LvAvyOt9z3yr4Gd0rkEkTq8-damWQghTI82eBEAUxBWijb9udrc1FLcIeKeZB_QxYM35maLnnHIT9FGFbVu381DiL2Gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYgq0drOC_FPZJudLX6tn36gsb5_-G0t5uCaog-BbzngD2_XI2Nwm7m-LaHhe8B4B7vKZCZjVWWkaW_4IRH-4VQy6rzSuusccKx_3DH_3ExHCUChiLHQ3nYb_Pm3ARAEsNTB6TWNbKJnh98jqv1wc4GX0IB42-bhc_xbRh6P-poe0TNb_qh2u0lEvGEa4VV_0A5XOHcbbiJBo92oMrIY4ZvOvqYzEJlTFAFTVOIfi1_9MASysw4oM2M7Yx-lGLq1CHxLRJ5kRJcjFjST05GxTmvQLyTkAebQRiWpe7jhsKmATvc9B5202tLnh3uV44_1aEhlGL0CRD8rX2eeprxWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0a57Uya4TlkNos1NqnnG8B4RzA68Wy-hYRMk68jgtwVhd-2ggs9CN7EKBC41UbDrKVsHK_hkeW6SF82lc6MFzM0V91Gd3QXdV8ljhMaMfz1tuXrMfl19UQe_GObNzxR6ZmG_CAhp6DkcwO34e102bBkjvSHmdyXne2SBeJ-mxJQtmXSChDNuPhUnVKpaVyLk2ZszdXPFyZqX8ROVRWEf6BKHslaEo0vtopoi8oHXE1HfZDZvxnZMuCIf4A7uTUwiENnhl_1XmaeRdr8R8kQwPNE7gnOeQOoe-70KRDcJkFa-UlMWUNMe61__EgOQR4OgyR1b4VHdMg24_tZLllmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5gxYw8DFPf-pLB3RwsV6zCQB6qLhgEKgAbmcGjg_go-7jW6SFs7qZf7T0_spHQci6UvEY5VlfOxwB_yzOCAoTcBVAMQf7wl8MbDoInOcuM4tN2VzgnyED2_OaHZ1wDBpqzNHca5feUi2ACw_qal2lC8LTVvvuDfNkw5EWf_Ira7jTWllFrjn9mv30eXvUBXCHaW-fwPEsSJVLp1DAOrkPPwNtN9N4eJje8TpZlXTSIN4jtZ4ge7GvgYsKPliT0J7wd5dZvqgVrdCQ5Srb4kS6mSZ6kXu1FnD6V_dFTEJhbjXFKhU2JAMv3FCTk3Sm2yuKRJgTd2-taARYN69mbRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq_nTPtigzcTF_Bi5BBoJmb5YAxWL2oxitJmcvbO8uKOnqkj_ArYicPox6wdmeOVOkq2c3SUXZw4uEPqgG5wD8kMF8KWCz9P7pUa3Hin9wxSkig12D0oHSoWPq_a_M1NRENgS4INfMWRrLmKQM2U-XX7i3bheztSHv1j6v2XK8sQ58xQync4GDYBicYcWIGTqg5TDgV6YB_NezUXgcWX0ladpoFoi4U5jofXriB2ApMtHSqSuSrnSMBFh7-5XNG2oIFEI2qFNDBjUE-2pYWgnMgdb7eAacULc7AjcD9AXlzXaxcw3fnQaVgimHZlPqT0DiZnJ34EFY2y57TNJjmJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcHQeIfzsaOA4DvJ5B1u4jFbcBzezLahXc8BsAImFHIvbFufNN1A7fMEqMXb5lz14P8nEm7p9yxvLza96DKegLhncBIEzxmPETNj16A_n6eO9b_NcximpyDl7du659B2-WmjJZdoqWCQ7WeWox9Er_ymy4MzAZeeh4b2QiQQHRBYQLhKJ2V7Ro6bICBVwHJWJkljY67znirQd3rd-KXA407uunrYogSU4i7mixxHvuLx4N5iu2Iwy40qA3hTUXM-UKlBZbWG7O6s23S97pyUE2BSnOJwOdVw0LAC2mcMp5ND5hc2NamA2YdYvPHxUgS7mdMzsZO-M5JcZ6TN9cbghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cupPuKfqFkJNNGTPDruIv9JkNCa3Plg199XF9_ukvZVsHsR94p8Uwra-p_j8j81RCDhdQi3G46BnUvzeLJ8wUojBmwTiVdS618XuvnATy0MY6FBkPqbv4M9CbLO5kUlQwmMPkhZOfnKpqDnvz4GNuO2y-2tzKnRBS9nIkSR91YgbB-MGImq6L3XyHSg-77B3URjyR_4kx1fBtMp_vUqcBKweDuUmTXYTmn41vg9MpBbLS_emG-tAyftiT9geEICwCjafmV7ycChuqYpsKNyaj1wONLzUbjOvQXej-1WgU-AdcuFx-Y2TT8D3iULPyV7AyK8bvgBG84alKzqZdMwMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFcKyEByPvrUGAXrqyA-f2Hhg9dFyC8lVTVv2Sv9UbJ3JgnFaTooHZdRkjLI6d5zRabv0AP0HAUQJydoaUdfb7ztBXBAabPgsC8bOVy-Uqi4osxsEHXmGNQmiW8DGML3Mf87Ms2UjTzheDbIyTaFpdxI1MraYw-K1iwCaWLHXAcnEigId1aqFLq2eJbZNDvJaoW3ReBLKu67UNNO8rg2RU_Q_AE-fhCQw5s2pl8M81HIHXKwZ_ySrG_L8BslKD3G0GrQk0GfAGrR2Xm3WVejjn4aVVP7FosxAfQa0vLDsCnZ4so_Ts0xhSBucb9f06nqmoGxKlfW6wGcmdt1o_edGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0eEmL5r0qCN8Ne4WHQGj8utcTq19IyqEJqUX4E5pxcC4dqh7bOGGdHkd_4nGTlf9JVq9W2QjBDT-AknBtn7Wrs7TKSgKbxGSulXvh26X9oHbw_X60q_8yC04oK_PA-PM8NOjQypyluTYCQ9m2GOWEbMyLYgAkYCA0egTmx1Jh-Dh12S4wrgNrFcGBUAevT1A9DhNGgGk-6bGA2Eti7JlBHZWwEagEiwbqaavKqNNtuFAH4Uslu5JVyDvqtlwdRY25JdleSMi7eLnmJmD_GpD80MVFY_ZRxUlRFoTmbSMMeCso-uOkWsm3CiUQjAS_VnR9kLfiHanpfH_LVEbfPLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuHov7D0WEAGWpEhUiPyoNp6zInXC03SapYCuZs_1aZlgK5WN-sasRle8bVZkXdI9XS4drR8Q-vSsSJfJJVsPjfBAWTsoSYPPfUhYMnL0Mt-q7K1iWkY8NNIoFOmuXiXFTmGLtSWGg8FYZ9IenaX2UTSVRSIvSi8WaEEGvG-DIrhrbzG866GSBLfqL7d4ZaSekp0dsmJ8H0pLaFhKX0CfZ75AJXqiFzGNV77hZIRcui_v_Q8YEq9x2wRiOacSpYVC082emngI3-xq5MaWZHjWpoSO080_1O5FwMOGl2xtPuN8vJWSUaCUVNHx1KHarySO0XSmvrR7Uw36Osv1DbWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIeqjoGiiFEnmJWtXrp0KbBmMTGNcClGTzlvKskxvERDEaaF37u-q-4kBYTy9IZkWl-06YMM5CcCi-pKll2F4w-aFcrjt1DIj3B13oJEdOcaL4yZp3i9gQFfbevjbHK-VgU0w4D2Ls7i16tUyxrevz1dRUAmrw6IklfTO1L5g7k4arr4zQjpUcz2Clj7BdfjNIoumHQIzZIupkPIlYuY-2bxPm8LeSYzUvdKf77ghmitd2t0KYEwc4aWbQuGFTnGGn07dGzLnlejdH3H2xCB0LogqZRjwHGubLGqN16KtGM6E7xJIoMcGya-XqsTnZ-Fzc5If64bz0pwntVZZ2tQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtXdUlHgGWLPaMMav53mBaOzEh6LVMfYFMv4-UsV45MjDUaFIArMQPFU_PtKxNd23SnGNVAGAIYD1q2tOHbMqLRvJr2erR-WorI_RYY6dCDXAZB-oVpHN29GZR8LEv-JEaJPfHeVq-u2BcIb4mKbRnMCk5FHxCI4M6152FT6w7U_B_Ysp002lQ07bNKRYksjDOrCO3skheQpPUcsTUENAA2gpTYlRO3Fj5-YBCxZTRMbnxUjGyCpmab81rPRdIthAVMegX2SUC18xRIEwvF_lAa5phmA2vD4UIhIUIPm-fmGbLfjUAZCNKio4BjKge91wN0ObA6UDajfQvj-TJID_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26922">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja3SMauFUpFAw7hPyiHz2Cpmu9H4dCvmsxnea7-GRCFnw3oGxKmfk8XJVP5ckWuY4wk3_d4iSsTq5miEZDbew3IrGOp6FH0nZe34ezQOf7JmwWcU_oGLd8elgSWrEivjbY4shLSU20nY1ZrFs4iqKWOOSyTzKIzCRMSxx4KdkuiMBOMTtouYE2f62I-aWgmQ3GuHrWcr-DUhzxM9jjujDt6B9YlBKXjnEVDgQYvLmzVNF69EJq9zQeMh2VfuaBFXrC1BvyNb1phJ1JS2OGGqLZghkZM77Ugiw0WVMKaBIf1y7FjbWq_esvnSdkjcrZY048Nlbg2obprneAlCwm-smQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26922" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM1dyE_y1egN25fxHERYoeDPy0Us2WUEFvcGY3gnd1Ly0DW7UjDUgZ2p10YxlrbuX7VJ3Og_MeB3XQzABApnvKGX5U7C5P7Ouku-FNgWf9SAc-ACrSq4Ssxsxg574SPlFweWGzpdiL5gm9c8VjHyGXagJbAb6OGkKjMnsleQplwVXqk5js755QEk6QyEcIoz4e0sls60AkYZFU805EeOcmnU5P9j_OtWxeRwnnMozRVxaNeLP65FIUkXwY2Sohp2C2zS7jtDk5YR66jwaTK7At_3M1Cvsl7fPIzrdjdkgQzOmKOpBtuaowNYXGsFZT9blcFHkei-YQu7SK--63inlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Zpg8pOV5TqamFwASssBaZddOD6FZi6KzghcTclNIPPCm4NTA8Xbpr_x_Qi25Q5j1nypx9MNrI1GXKTfhqJ7bP_aUdZIrA5w34kh6wH0YWOh-82NuT35RL3AUU-41WO6c9AYPGIL0HJvDaizCu7QBweOT-PlpkkBh3XWV92xr0ItDiA846nkOMjbh1dwDV_0l7CRWICI59f2wzlkeTSU7Sm8p9yHyYU1EOkfsmsi-eGmVCRDjdSne5Nugde9ccScmtg84JJ7TznB0K2lXg3olyJ7lXLlGunEw_eiQyqAJF-6iqIlyfgNuHAbN5vJ9S8r4nhyIFwg6khFAhjTYZ4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3px4QhoCn0NQgV0lL113tmyxG8A5PidvKfcyiRUTsPg9rfOQclGEfmRKk82S5gsNzfqv54eeEpez5IeeByRGQP6A18EeTiA9POXeXEv4MW9suqPoK4tQpi-rZceT5_qRv0AbBRelyEE5JMAl879Wh3HWKld3TVez9LWZTxhy3mGsVKIrxJpjXhEpA4yaNkBS9LTZ1KPgP-So-lRL_49omyfdac-fgROH09zKI7kPyohm66vDAzs1eYx46e3ZeDi8MpT-FmhlxI2LLIMLXQlmcNX2bRkufyHE560xuA6WKr_P4yKu7MHtho4ktGgBuP_UbDBeOT7ollGiq4SC0lGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOCSKCUq5AwRswTPzHaLW9TfISO1e1JekS3JLEnLUqFYaqlNKnU3qrTCV3Mky9wCHWCBUI-j4cdO2RzJ127XvrTvsiT27wiFBOdpAu-iDn0oJ8OgrXPk-c69MsILzBL0Ax5uqQcW4YJo2HODary93lEoxI0g0EjhOWG1sRW6DvCplpTRt7QvDhPYu7ObtxWlLAq6b4Cc0957Z3rZ9P29evclREt_BaGiT8tKcWVjwM0qLP0jD2p2cu13z1o3IfMFsjQ1zgTp73hN4OebmM7stE6MxS_rQ87QDc1XZ-IdKOuj0Ep3mxwOVAhV4U0FI-lXPblaxvIEwxUdLdU2beLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZy_KKv8_xTw48R1cIjrXtzEuP-D4lX7UttWyPh25-FpSyLCJCOwK4d0as905NQ2_ZQNAHqOgmTuhv7cLcn_Hf5gsXtEDHPqrH_JRzTiZCeqTneWw6h0c58vJzBHo9a7tT7kJWz4zCRaqWNoWyWCYuWt6vdx0GN2_tYcmEVbNGeXxXuuQssYGTxsInyR3eBjgqtAEPM9l6bfUMPWm6_O_8-phGjVjWVHDGCz0uYlG4nuh1YcF-w6RwjvsrB5-lOPFjm94tdT-o2f44RnSjULqB2iDs0JvarXocHVQCNGWFzu7AEv2FagWt8KZq5-cts7R332pPWcyqxYcXqTbJVOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzqIoAI6tyQboPiUED7uksTaKPagHrKbkP0ky3Of4lmlNQCx1yXGE1cev9cb40Zp0fw_Nqqwe8rarPw-uUbSnrozhyZ4lm6yTyVYofveOZFvkFyvNH5VhYHUKImdP0z9C_QXYkMSZpuUJtZvHB-9fswmS8FmUFruilCWay6VQi9iuJDSGOcgjK910BsPEjzf_CbamEqIj-puHGGqQvw5J08iNzSHRGt0O2IL-DnlYhgspiO-pvQVWkaO7ohftQ8-OvhYmBggJTY3QAyrAmPoCpmpv0WV8rejI3gvO4QFd52KFZ5HsNiI7izsJ-f0xk3iARxEa-l-T1ypXIt1THAFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucd-goZn5RzXxjI0NNznZHLTTcwaHqaAkNmnlVmVLASUZ5ODX1TVB9w8HITFOgpzPnm90Sob96fnC2U1hTu413-rm8kPwuuPn4ZORMjPr6_P8Pmo2uMJGiJpyrY5kJhLgBHma-zllwgyJU0CbGEpnn-ouqQXx1fEH8rsxAJQk4XTNZT9fxX1YVflm3ykKd9tvNhlQ0CEUVcT5soxxofE-Dq2sR7JHvR0FF1jWcuAu3jr4GlDi5PjWBay8etjOskIzLWvwKMLaE8Cd-1FOeBHI7K0X4_KZh96LZHibSUDK4N3haM68GueZgORGOarx27Iwe6s_jP-Q_LmvlLngx3CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NouTR0r7ByTgxyBm-WcwnOhMC0YCwXAfSLYYckEGuJohr9W4pGdOPnM9xL3VIvbw3q6gGrozAt3c_0JlOnpDmA_4FxQsyAcaZw7wRjmzQ7zAcoqB6DVn0TmoWowANmFyIE-D97RqsADK_HiKEZz139Wsx5A6mJc5ydSrK9GQ4eBa2LO5wmh_TRvGXzOmPh33dQKi_5stvnnvj_BjBicOrXomY2hItjmMtzD5c6Cn1FiS8tL9jnyR3gQ0cpaeiSbDbko7Z0mLTRI9KOFc8EiqyVZycFuKIRosdTKCXxxOkX-Yg7vdsXB3HOeeI4NaEqA6jR4xfF-abR7CMRggJPPLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZP_YVipT_xRU8jU1DZ2ZItE2Y-46SGmrGlPEKXkp1pnTa9CHPxOH5HJtnS9TOFBAeyYMFJwOa7qg3ODv7R4UYkXPcwnMfGALsIVwh_QtGe5ldXx7ipGdmKI0tJkdCIxP7Q0U_1oXA4VxskGIMOm2qzcMNUP_Fp22lwymHVhsIb_a4rU1v6ccmbpqadeM2XqJub7QbcRg4_IxGCd2sF4S0EmHPUGAhYlE6Nv6FeRHJ_bZbH-Ol3bWXQ5EL6FpVmgsNt-UPFZk3PpyqqQJPCKNJMiBY4W2KWYUvnxtiMIo55aP5w9ViNjlcPU6NgPbNJM3mhlEXKc72Xl75hdAlPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDx_Zpevxb_8Bv0V4ASR_ZzADf-5v7GdRZ_2QBvjecruRdkjsJ2onDDxyIleT5IdYGwnZVaJVed6OuBcIRJavyqXY8OhI3T3ceJbHStY7klYU4MflKRzBLSzpJiOhyxXFOGtb28Wl7zVuepbbb6YBR47k1j4m-E4Y3XGmwfoOZ0BuNd0Yi-pSJqTQ1iQgph4VT2EX4LtEmljaQuSOX8KBGDSCNg6GYktmVLrZuTigVQDCgthW6QdlWbjjQEPVf-9K027_mkZqluTu_l0nyeGT6lvNjkFQII-MoDB5pQSFgnvmahJIKyzHqyaSkGTFTAhooPeHr26GXYGRWvvssbDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAKBkyGMQhZqFVkWvR824LmE53JHl1BRWnUj-D8UYt0nt4ysScykwIJCKViKUvmNxT3GCeF1LvfSGJtw1ucmdWLRYYStmeu_wYFAduHLHhTEYW2NSEOb8s9P9Z8MqujlXerrLbuFk_f1WkLABYlOgeAsidj8qpOAkwZp2GAK5CXpG90r6UsDPSkvvIcqLMPphBpCWw5p3ncWoS4dabPfbTg2ekUlXve6qFIM54m4VAhoFEQIrOkrm0Q6RYBIeqcslbE8aMiJs_kHr67xPHLdrhLxgwqEibrdLHS4VBat3v84aXoJtQVUOQoRXh42dRZvbpwN9ubZHR7HKnmBHrAJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1MOJrhXMW88Orxw5asXvDN_CzQOx7L4qWFwR3jziJf6w8DyA4XEKt03JDhmDzADghPnUhpMdInKaKzgLN6PViVlV6N8o-kQ8P38_Kyrh-oMwJXPgpyyzkXBbumhcqCqe4shcRWNqY5IxOHHmxPEj132HCDDNTmLse6d4ZJiGpN611EhwAjKpxJCzrluepf0ZkIZ033E6rwABoIFDV-V3ALIxSE7okBINbL220VerGTCBuWfxPpC_Ze8KZ7U0HxFeOI7NfR-BliVRpX6HyTAqbgP1fb61K0-72M7TDrODAor60Y2mcKMYD3khKR-f4_5E5UI9V5CbryDcuFGxUjbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i47RZuMlA9_Yldhyofu4Lbr5Qm_xRfZjzuoLEDj8DLJycyjjZy-5MGwhnIS6EZUAEnF0WeHg1H1G90l1OwSCkSotYLpyV0qqKAun3J0P_2RsOpiP_If8WiRz499q9K6FI_5L_HCLgRcTXGAl1ZQ1ATaN3tdUmkdUJTtsDfVucopCzD5wey0MuO7L6-uL0R64AHVREbw4cFkvPARzmz4gRJ3uLwIoIuUx9ZPCQfZRR_23jPuPF1gVLuYwbQDR28SBjB8s6R2xvVtvqLAU1eD10zOIH7W5eBXkvEtGARKVzYYNMXrhWCWT_ca1L89Pu0GWFOjUYiA8k0D-W-lR_U62hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBzZH443Fh5-dmQfHD2wn_u24skfpgIxuLYE10oHQtYT_OP-lEost3YOiYUWUK25RfeHNC1FcJMf5F7er40UP-lKcJz9GZYCwM7GmnErAHxp109i8Yf9wAQRvkUszAouMIhbpbXcVGEhL3BHihuhx6iJuMm21dqarYFdWcotOUKdWmfesNutFE7or_nk-ZXBV_YmR3FFk1TZWOtJpCXboYqx73wruHtmkonNEGH8tgY1p8j-iS76EpsWcknaZD1f1cLCYzSx4tIdj0b8j0OIB4uF-wUXy8-OfK6LrP_Yeha7-q4czZ4EQhhV-CVMlgPMECjdvmVaWaA25f6Gk6fF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXQUzvgJcYeiRNAqUc2wLmhra7-7DZHunYdYVNN6dyIWfIjZTPytSam-33nyOvEbTdEDVR-EQL2skjgFVyg8kvs3T9uw1eeZK1px0VSaJVKlR5AWMywswpbX8EQduaZvZINLM2FHk1BzD4-nG5Rco0Tk-Ow21U-wkw2trIgjMYxJsT3Uk78iLjU0kHibo56atwW64lolRlU6yzrueZvicspGeGwrD1fp9y6xF5w83EIk6rn1y-5ySjwaj6aFNeR3bJ7mRFzisrBwZQetSwW3FnO3xuoCD9fdrFJLHzi-ldB-N5Yqad4CJAVC8bcOj_LNM3vps5WT2keCE4oVRrE2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rehKqwJmAL8SAtPT8NFg4HyDwV3Do44xaHk6SJ4jYIGj4Rm4uki4RxCA_HiQKIGw5yv3crmT55EGrwTS5kCAc3jM3VWwFI5FNJZesmjbyRb3kvjSk4TTPvoi8aaiazVhxWvVrEyrNKpOJ12KW7dn7_zVuOGoSaOHUYPFkp2NtyHxgNSu8MXqjhUfb6Eed7ZMXtxBCOzJ_zGFNQkCAoRZ4khJJ1t0J3HgAi7I1WI9hClIhQVI1M6b8hdt7f5hGSf09u3qK-6fcOlNRUdQrVeaTNB2i33v479Dkrteq47K6gO2C_b9SjzYQAKoSXkvMdsX36HJQkK5ymJddhYEaXVf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq2tHdsoQOdbnKDI-vqO56-Nk6aAWc4CRf2ds3vUQTH0zg-qz9X1TzjHMUCt11xG3uPh_9WRmQcESR8HkomX1NUxWm76cQdX2nqT4d0dSryOnG-A5DodX5EoPk4HslYcX5zBdr19_br4-IfZ-jG2Gh_nMciSGXukOpkK9N5_SwcD1RFDTRY3VBxdn5LvOd9Wpvr_hZoIiW_2HVrvsIK81vqaV714DqbsWpPo0nLaoWE4i1xR9VR7f7lqwMqyaxf4Yb2aYay6IXatCKqiAx_kpXC_u85F2EpwD-rsh7NfPXJ69yzE5TdhGALM0OuSddb3bYbWWqaMS-xGt8pIBlTyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMx4w0okIQDnLB4sRMoJXt9dDLX3qFeReh9jPbC_8TVjOE8zO3InhwDzwfzTMxsZEvJ9XWYA4iDN4PyyTBuKczFFYgyFOjhgfKq4epWmgu5kBP3x4kfeOxibrjyeDrDTctVSNX2ZsVqm5-deOt_CqYDz-rpin3_YO6xb6TuNp1tJXfP2_dVxCWQRcCc22jejmDZTvgqDV6crwGu8c_M-WIUXm3cJrTyYXrjZrLwRSPOitbrh-oumcMa933UqoEvzbNH_PzRM6c1BEfaKUk_ssNEu2Lg-s8aYjaNkNEwWiLT7zGL_d-DtXrx53cJPKBEX-7VnbQE_3_lcwD1DgjSgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC6OyS18PEVpsnD8aRlccBOlcW8eM0u2VXRyWZL6T6HUBnDfIet1wn0LzEIinBeCYIK97ZeIV87Ud__KdseX4nHf-Je4M95Z8luAFqFUVH9j7ezra0SSHV_SEHhbCxweWkYFBfihwa8Akc9NP5KQTyorUV1lKyAHmFRPYwpVQl-vm9DwyFjtGCIG41yqILXUxCOH9E2bz_7FtLiGdP70V_ZdlXzSFyDY_WFIoCUPsxGxiJjT3U5VY1uQm3t1gCDPk3ZHK4gjyqwbvNFc2lh2XdE5tFi4Xy6T3F6J_fZ9CJIdrjhxSTFKZTwD49ky4uI1VwOhOLophJ9ypDkOnvexdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0Tb9gAZsK5zidfXYXQQMehNxp0ohnb6QHey5v_AOamhmnlRby0WnsYUXrsRxoZ5w9VKwla4JqVIk_NQdIzRsSEOZGxjbvQJp_gJ0odlLKVoXsXnwRMxRKdpHLQvEBq_jpz4tTXjygEKI8fEDM8Jlxg_DrBOUn96qSNs-Hf37_OMKwX5OCZ4JpzH9nn8xexsNG8sxuxYbxCcuJ94hoDsjAUsJugYdgkR15dUwa9RoVs4VBpAPUhuWaPm3KWAxZZ8USRY298CaNNsYqZjxenhNKv6cHWxfg_U6oJ704oDDvifpN1s20oY_E1b7H1fbPyPmrSIHM27PLPL65CVoVCXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=BDkP6-_y0TVjr2-9BTy61gZwH_jKxNA6muxgCqbnLgTO9ElyIE6sOdYkkLQrBELZqVycgQkzEJccWwOO4n4FrBBE1qdfB5wZQFMVAQ-2JZc9Awrf_Gwjy9Xox96MPIRHwBG8CHnTtb5LYaQpI3w-2_CtzN1JPgoLcT_S6IeTBMInGBc06IgQQff56XP7lpNeBBJ-0Fg3skS-U6kzWLFuyG3aFfjbVE7GpOKd8NUmLi9-aPnzMI6jngIHvXDQjjFyTJ0-70NtXLpz8CGQBrOK-rDDoCe_OuSu9BY4c6RGpd1ErmA9oEDWxnMyJxzfqNyqLXV02QkSp38PsVtDe5jHZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=BDkP6-_y0TVjr2-9BTy61gZwH_jKxNA6muxgCqbnLgTO9ElyIE6sOdYkkLQrBELZqVycgQkzEJccWwOO4n4FrBBE1qdfB5wZQFMVAQ-2JZc9Awrf_Gwjy9Xox96MPIRHwBG8CHnTtb5LYaQpI3w-2_CtzN1JPgoLcT_S6IeTBMInGBc06IgQQff56XP7lpNeBBJ-0Fg3skS-U6kzWLFuyG3aFfjbVE7GpOKd8NUmLi9-aPnzMI6jngIHvXDQjjFyTJ0-70NtXLpz8CGQBrOK-rDDoCe_OuSu9BY4c6RGpd1ErmA9oEDWxnMyJxzfqNyqLXV02QkSp38PsVtDe5jHZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiIitueRaLPXI8ToCzvQQ8TMS8ajDVLDjcnXqflMY3xfb2pYoHRlzxtw4jlZ7MIhIxxNzvZergPaSTM_XXVh5pMlLK4HUKb3nX4He3zZ-CH5m0m1wwgurpDn9R9tTCRw0rQYd1uyMENxFQ54qpHwk6qSIxZHNuKTz3L-qYYDAc-E_RY7i1YmYMyh-ZM3l7MdhluFdIfyZq-ZlQtgVH2-veMIXCPGzQaLOYYipIu8UqUDZdjQO8d6A1qWwdSRBxJzp9-b-NhIfcjJhBhfI5XofCKb4ggWHvcB2ltWaIF3RzvpefWCaVR2PFuZ6C-tkGlsbnKQtcui-FCbAcpSFzwnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqb6sQASDvp7jMaBbE5-qdn9Ya-zfNssL7eDtZ5py28fKLgnGe79mXJMfB4rcWMB0vOzKPJJjrGPJpxXwtSNC36IjE2mn3eKyY6ioQmsKFvxvk6kAvhdHTCNO3E2-788TRDmI_Y2kV-cF4CQUiYgLZBaA1e1fJ5hfyyUEt0f0WpAvXNQ2HVHE7_XiD5c_At6WtTJvvOUZZcvgl_9keRkn0ntqB9bZ_u8hUh0GNW2OYBpsNwPLd2rjZZdBiOhFCtvAmtVDfgkyYMnbZgbivC0RYc4TA3mEIFZuPl_Xire-nyMH08hCfBU32m2jIpoZcYfzgukl8aZduKoIDeNsKmVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I07P_gx9zImKwmv9UAwNr50ziTieVA0CtwGn2rqHboE1RHfd_scMPUWGx-9AnOVtBhDVbBY2FsyaUIsRh-0yMn7vW5zt-uikRVQsZfI8wT4A_K_1iaZ2R9FK2RuaAcKATFKSdDh3tgAEmg7fOB60mpY1-SxqFMTkE7PQHX8TNAAIWkdie_LrpX96HbUMdZc2u4F6hVQ02aVQ1fXNnNFMwhviYmm6Gkrhn7AbsHZwAQCQU9WZa25nkWGapy4UQB-QwoUaZvTHc7weEBLpQcTBTRrpVhqOd9ivY-mxL8Uk-AceQ3cfk64ITfU-agdcD6YNkDjN4asDERPPdLmr2MhsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ttpZAGKLIGNe9qgpa2wX1vdX_AN9s24D_ijf7SNeDQ0AayGNUdMZfDQiHv-T4ma9TVj8yVjWKnvN8uF2EfBMxL6bvUiRNOh2AK1Ow9UIyk8nXNys27TKUC8upQ0EO3BYteGbi3twdIglxwQA8r2cdFYKbKMBI9o0r52d2fxsMaDzEZSN2sl0Fhw420MbN4Ku9xuON_1pMoTY6ju-WBu1nJGjgwil0tayxGOFhYAmIrxh3yNcpZaHoT2M6-pgrklJUjOs_j7wRg0kxNhhj4HqF3K-ePxmUgLY1XLcxgkGMIlsZXiA_6lvbtGtYJN4bwijq_kwFs2QWcl44j-faVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgTNY3TN4UnLEekNI7ioV473V5ACcqePVq2leiMHot4fOTY3sPXaUiQyna3el4xjd5w4lqX7lFJfIeJ58r8MeDH1ttjS0y7b9C73O-ZkWNOqGkPZwnNqvbZ0Qg4H5J4HIE-tWQg_ZIx89p7h0PXn4ds26uukB20lRMlwZVLvT4CDl0DUBtYYp6uhCljRm7j3jITP7udNeBbUsxGIy35DztbiI1PIrKCNpDI4fkOF5m14yfJhkLqqiLVCLYt2pJXzxcoDSe3FIiXJi2XBgtD9PoKrvxVRjpv6aXBaC4alMW-9xty76pZiiesXTNK8zkiKVH_Z70XoIWd8f0sZ8qSjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbB8AcddGrqGalA3rWI9siQ9GIo0sdFUKHHIDgfO2IMZfUammbPK2RLN-oG8uN3opNEL_qb9bj_tlcc2UTGBPwtpkSdgknfQc6Oy34I2l55Yw8nfXPaAOFKDL_Md7VZHcTkq1zpJPoSWq0A_bU1Hkxz_OnpEu2Fvd-MfmTAN-5lyF6dLP3xyLSinPBOLh8oNq90FnmqeuJpCDhAk3OJlJz5iS08vrTRALE6s1OfRlQjjk5psqSTXvENystVHPxGdcpDMH8MPagVXrUsqGvQgoxT1IWn-C5P79tgjKkXEpYerV32zUOSS9vH6NxS5FUDxSKewZdCoe_SerxwRJjoOOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSgOyfp_0RP4LKxFyGi5h6B2kGFTkcZfYxSZ6KgfdVdvY7XylZVq9m13RfFLglWhABRZjgiIrhruUzPGEBB_q6RbVSM1VCZz1gc9uxhZVnwhw-3IpQHhJdnW7kuH1ATaAHLWXTFlC6534MsGTwFVptYAQYcB9DZ2-eGfgtoOrq837DTfeDnK8wLT2ngqi9qns2t_Zp2toIPyZ9l6TRIoGUw5m4FXBEdbx8l77ay8cv5zIxESvAFgu7_cTLEPy1QsrArRimZwDZAZ_rtVSf4QG8m0HQf7v0vGy61bmqzdkLi2lPQAq8hhYQWogz5OZpVhJumM8xddqsCvvtLPTpXamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSM4yEZ-E92JH-JeCsGU4mWcC826ibLDBlmfutyOD2W_C4TUCOrfg4iQq6d4r72lxe0XU-PDVu8fa5YLZOMytOOKKBMpSm5UxdNY3r93TcOB2XLu_VQawU9eNTP-mdFLG1MnOYtKg4dlfz5WaEzyH-A0FWPz-HpI7wbG36MW3cbrexlWYh1gTV97-15Ja0fpcmE9glcxRboflPHLyrEn2FEo_LHNZuBmmQjKA6VFxI2_z5ZuQXkWRrlWxzYNfGop_YiKsRJXPhSut1YfMwtMBny3aNaCZmjH6HlYIV44KRNpCvzGoUtKRVfzng0v-DnBn3Kpqm33iizsWtr76a_uLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOtPhJlinpV4UP3NZ2kjZhTf3C8mrtZh2b4JwMKRSZiXUIfoW5O3tJTn9GhHfBzyRC-Kp7mSY_-FUBLj_3yeg9IefhGaRosGHBIPwUxwK-lFf1Z8JC480nLaaawMlBA_SRPtWE5lX9asinLzn1RfzJEUl8ox7j-miIAR3XQsQiZlRbg5kki1Vl7WKfBz0rqht3M4LRoWSfNPV6a6ccWXocBkxnxXesw1x0whhENGF7Dsgx8Y_CSf5T7uG_qQgq8ayiwHaJjkVpr3Hp4KrN2_d5IyWwJRERXurQUXh3H-IhWyL1WtkJu5pvKL0Jc8cKK2x939lSBjacx88EuwZwNegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGi7gufici-SWwqg4RFk8IuP4yuJcdi5r-LlGYK4FMK_0joGuVe_vrBOZP8dvWol6DGp54j1XPb-wQuxtknEm2VCOVkBqWiWlC1GJr-st2jLktTH-81fB4lohHhhcs33CeUxZOhOp7D5G6L2NnrPdao8WIRQ6hnkpkB0Q2ruuUG2Gh4k5er9cxbiBfBZsfXaLr9K7rqFPgyYWn9N4JnWxjg0PtACG81YvTpD7U4LewEgpTuLCJQ1wD2V1TCBfMBq0Z8QXAJgas14NddUZa85PxisYFc383yAPxKYQsEpZbgyuGoQyvJ4gX7rkNv6RWYb-juZf2FkgGsZiupLrIGIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3GikuKy5vpTu81SljB-cxAyozKELEFmQ8f4j6-navlCxdeoykEz5wo8qCH8ZWTTKHtXuCpx-VWIVc_R5TdDM4B2GksbaJiwOsoMBzdi31H1XOjs2ZeGtvAx7-HKh6-1dNFq12o7vWc-TOtYRS9AVhCcJJWepnxHvLEuDg804yAD9SEBUKyafPsMIVeG7kLvhtg737qRgdiewV_ik4Pqils-OBDre6zD--JqYR14jLIZEb0lCWVIPp-j9GdV3XOcR3H3nESb6UrYYgzfFJdIeAo7YXCDgCny1wiZ1MMpjyBr7D3j6EvDcIFiRRN7xFibgSunZz3Pmx1rWtMUqac8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wc9pRN5rpTPnds1SGYCpZTmU7KB0J9ntphrrMbDpCNUXeEf7ECqrDWM5tX9-wiBiUazml51wVcJc3XAHvGuvTi8J1thC6pKyOMUN8enrQzpl7bcveqSzURcSXhjkcqhCty2U0vL-5lmvR4CtpXqI0s8ZbarIRS1_t03h8soekgi30ZgjW3-33cbc5CT-1abYzjzENuBrfK5Awc_VauYElvS0hcPAGNWY-XhGqGMKRZBqS1G7WBDiFYz3zr7PTUhXsGyXM-vYE3t6NdzYDHUXDrZH_WnVBqnwHGbryz7newhzdPsLzKbXsQWlsGCQesngO2KO4mJjPkmJKdLJ0xzJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzlqUrhlg7-8YE9tLKWwrPkOKwMzWZyQkZPWvUQUmrBsk-bTYfH44g68rBoipC8jCCnJ-9PN36yuafok2_w-onFdvYLwNzaEjX-nyjXiQJ4kZrjI1Ht3DJbkWUlLZ2BEM1krv_LS0R2JNjJ-eNbjroSfsJiUUPGAxLEVwIOw7uPokoY-l5fCYCXmx_9334g58xL-4zkyn1sGLySMT4Cxhi_7JnjAO2gOhpAyrEUXmV0PfLivb_2GZTb4UyfkG0HQpZrIRIfywxpjFpMMic17OsBcfaP7qCPIrkkK6FNguiqfBtfHlOvN8n6L6mmljDCsJVbwF5yrwDWClfye9hNjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=ZwFG7uIhxVHARZYffLVOyIz_ZNXWw4xbgR8pFoKgFBRYvWmZLoDuGr7gvV_VT2jbuvU2DtF2EShMfw-0WjME-Q7GfCUn4a6kMmrq4-F8GOBEOFLr86IbzGGgn6wT9lIKsDOstxPXSl1gs8n0S9CQoXa6YsNRG_JY7RINzMdMdmlhFUNBO9NN1dVHMSGJEyKBx7iA9qbD28-B1GSHoVJNcsZTxhMXIF_oHhn6-RjiVN5Hqb745dSMBGLkwB2aw8Y1Y74GUddi41MLwGb9u4hc8I0AsNHWaXxoi2GwzJ9E4CSZt07nBYR9JXt7Txd0rAp1DRooKI07o0IhIUwpG0gDpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=ZwFG7uIhxVHARZYffLVOyIz_ZNXWw4xbgR8pFoKgFBRYvWmZLoDuGr7gvV_VT2jbuvU2DtF2EShMfw-0WjME-Q7GfCUn4a6kMmrq4-F8GOBEOFLr86IbzGGgn6wT9lIKsDOstxPXSl1gs8n0S9CQoXa6YsNRG_JY7RINzMdMdmlhFUNBO9NN1dVHMSGJEyKBx7iA9qbD28-B1GSHoVJNcsZTxhMXIF_oHhn6-RjiVN5Hqb745dSMBGLkwB2aw8Y1Y74GUddi41MLwGb9u4hc8I0AsNHWaXxoi2GwzJ9E4CSZt07nBYR9JXt7Txd0rAp1DRooKI07o0IhIUwpG0gDpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=vEGyGEibBCCZ2F32iEUWKrIOTfuN76jsUanGSlfB5ECrl0JafrsfgPPKUJDzYgHeIQQGh_2mqwAU1083UXou946DL9BdFg9jcM1WIp9D9gtjkH2KdFq7zws0b-PVC86WUxGcjAe-t0liUMJ2gXWA_JyVSNNqYsJExePpVYOOQnUC8ks5Ru1GA2wAK9_7WKfSplDlnnOsEJrhpnp7IbBkcKqnrGXRtDKPMFjKxBbxaVLlqwL0kW0GWZ1iNUUXXgiG8DMeO44apQTxm63i_iinUOfYLgp6h-LPtgiUFdRgUMbmvLDGbe8CgzQEAssQqUsj28bxOpUjQtfVRI4F3ZaRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=vEGyGEibBCCZ2F32iEUWKrIOTfuN76jsUanGSlfB5ECrl0JafrsfgPPKUJDzYgHeIQQGh_2mqwAU1083UXou946DL9BdFg9jcM1WIp9D9gtjkH2KdFq7zws0b-PVC86WUxGcjAe-t0liUMJ2gXWA_JyVSNNqYsJExePpVYOOQnUC8ks5Ru1GA2wAK9_7WKfSplDlnnOsEJrhpnp7IbBkcKqnrGXRtDKPMFjKxBbxaVLlqwL0kW0GWZ1iNUUXXgiG8DMeO44apQTxm63i_iinUOfYLgp6h-LPtgiUFdRgUMbmvLDGbe8CgzQEAssQqUsj28bxOpUjQtfVRI4F3ZaRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtZyeAIJzfqAA-8CqC267qj86dNFin2qHE9br17eFxN4orTL0HNwoVJRSLzoNEs-FppfTQCH4QYCGzaRBOzUkJXnC7hxPWsfw4vyWO3ll2K1cYdKLUO-7BOtjJbqqWwY4uFri2xKBx4qiTQz1LZWXkqVqe_AzEbNkE2bjy7kKfCyxxwdbvFDM0H-lOBJvvbwCKw6T1yrgKrgXPAy7ODulbIfIXri8DNHUGEdIK8UtRa6X_fEusacMcVxZkPpxv4BJFvYqetYYijP-PJ7vkTj1Bu_AnOPkMbBPSUQGDsFyoXU6-3gDEoJpOheNfz5PwwwvFVfX1GuZKWh7-CwIrtllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKHnw-bnJa17FC84CHph3lzJQLk-JIhMNtM7Kkjwy2FUJfsYb7kpX2Jgh1B_fDx3-WwjPmk8KziJjFZncKUU_YP1WTCTqI7_hDDGgDZanRAYr77glWLYdXsTYXwGvKf5BlOUJVbn9zMkrzDjY5irAWfvNYEmQDoiu0ynfwIJgsFKhdg6XYz-PX-xgUEMf_lwayfNCd2ycahKZDnLJCzyycnYav7jqAl61Mjb9ksiJv3i-56emOpgo5AFSutgW6WASwNSSrZRg9xIFI1CuZCTvE4kIGJ2qlTbMCQ3h4k-WjzeaGhXPW_NOvgMBsqahS0jLqIZtz6kbP4UzHtNIAv6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=CojxYSyFSnbpjWnyfbVRH5PsJoTaPp-8Z2IjwQxlnuQvWWX3iMPeuSlDkLPqMEjPcb7Sia0m9kh3v-E-XRfaCeULyj-NyLnRtZrSsMVn4ON04gISHDTUpHCLPkCUdJeeSsQxQfx4CiGsXZxtse1xSxbb5rPk74eX15iY1AX25So-TelDesVX81FRL-B_F3CIU23609ceHt2j_ikkGdQdCCPt0Lhqxismf9hlYHBjJ7m67ZUlE6MSw1Dge21CEin9i3X-RSgVB3td8iuHZTW_uPLtNOg0cOZINuK1GiLXOIzT95F5_CrU2MY36b_kh8ifYr2KLvqSOWuNJ4ScPdh20A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=CojxYSyFSnbpjWnyfbVRH5PsJoTaPp-8Z2IjwQxlnuQvWWX3iMPeuSlDkLPqMEjPcb7Sia0m9kh3v-E-XRfaCeULyj-NyLnRtZrSsMVn4ON04gISHDTUpHCLPkCUdJeeSsQxQfx4CiGsXZxtse1xSxbb5rPk74eX15iY1AX25So-TelDesVX81FRL-B_F3CIU23609ceHt2j_ikkGdQdCCPt0Lhqxismf9hlYHBjJ7m67ZUlE6MSw1Dge21CEin9i3X-RSgVB3td8iuHZTW_uPLtNOg0cOZINuK1GiLXOIzT95F5_CrU2MY36b_kh8ifYr2KLvqSOWuNJ4ScPdh20A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvZ4DBfqJQA2Royw2X_wP5gSSoVnVMCr7bAiUk_3oHlzPzPXmwJKZi2ljQXyppLHLGhIYGf8IO1ZgI7ZrYj_mAcgL-VSz-aFva68QHsDu2Y1JoyDYzfiEy_nXXF-Ln9FTzDve-JufTdFOT4Uk3cjydKRJP7AzVW2_3xtuP5AzFvtdAK7fv4br6XOgAoU2I9NhUXS4jZnJAa704IcHYFWxe0Q8Tavvzix_m5Alx4V1udDxU8WPkazo82YtTUvPwXxSTKZw4zfWnVlkUzvU4ztSgMP_fb7sTveND8o-f0mQQzbzf5YT7ZYkM6NG0_NStmN7kLQ2AwbEfqf1AlHKCve_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmOhfDGKza8lM1uLh7BRojWn6jJCiJaujYqA0QWr8V67eJvlLEdrGGycyAyWwzPARQG_stfuafs6thoj9GajzffgeNF6KDgeua5es1PL4WGFPkoMHgnYAFTuhnUL_fXE35Jz3BrdtG5WyRrGfxeUL7uAGSEq3EktULi4_PGegPcx-OgFQY9_2Z0WOSBUPuXAKQUgp51NYP9DBZetrCwExstLOAzCmQCpJq08r001mQptBpP8zt6lucjsU4PBAz2X9wKdJTroOAikoMXKpAw3hN8jBdroG2cNZ8kpzfa-myL25OFeoByUUtzuoh-8PH3wQqIQptS5bpTCM5_1XOk2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=sUzqrZfgf56tS7V0BUTXilGVUnxspUzha-n53fgCDGwICRQqwOb-dIsfuK4dLdB7vWhH5YeAVa4r4rxRPwhL8G-McWbAHrPVaxFo8yber_4_UfboYMgj6t62A1RMYwQ_4SbOtL8dr6GOnIw-5QUVRcQpluT0RCSokQav83GTte6c7Uqw-VdeH8sXvWjpggtaupkc0J7zkZ_QOlyL_1yeH9LurCR1_oPQ_3d307Xy0H1men9gdqAr_wxMx6GNs9_2T2QjKZPGeaXv1bxrMG_gspYhRT5FT3X7AaW3G7qsmyehFrVBkDv_4Ew8F9QUQCZogaDOd1cezrqxCFbkh5jrAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=sUzqrZfgf56tS7V0BUTXilGVUnxspUzha-n53fgCDGwICRQqwOb-dIsfuK4dLdB7vWhH5YeAVa4r4rxRPwhL8G-McWbAHrPVaxFo8yber_4_UfboYMgj6t62A1RMYwQ_4SbOtL8dr6GOnIw-5QUVRcQpluT0RCSokQav83GTte6c7Uqw-VdeH8sXvWjpggtaupkc0J7zkZ_QOlyL_1yeH9LurCR1_oPQ_3d307Xy0H1men9gdqAr_wxMx6GNs9_2T2QjKZPGeaXv1bxrMG_gspYhRT5FT3X7AaW3G7qsmyehFrVBkDv_4Ew8F9QUQCZogaDOd1cezrqxCFbkh5jrAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFvQkFKAOYHIxnhcMCQJKjQry1KWACjqNXevaoFaiiMQlNCSji4HE3Hm5qiVoEmT-9pWQ7dmNtTE4QMO0BN-rq8MnQ6vV8VuaMT_1XBK1TnnA5SCtE0HhaomjZRuYHm_r1ynhhoSg7C02XQ9o83s8b040OznOterPyEN4cya-Preq3SkfWGVyhAh1Ek495RlG2Vok8t10SUEfRGFi3Ao2mFzKBuyPFkewYi9q5gdXMftmUGQ8aoSNHIhEfnVIeVV6YbSdIIjl_rL08o9afKc8dYjCqb60iHd3AYnZm0Wta80OQcFtk3nRkgabcvd8bnGrFiezyQMECmnuPIrRa4UTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=EAkb_1NWc4v2BBjNBs1xTxytYUYE7qYA7OmAGnGxbN1ummKGW60eJKuHR6ng8Esw7yYI_wEvz6g4BIHzR9P1zov2GG8qt2HRsSJY5yeBFmuM5XXvgOvSAGktGngaKg1v731IIwcBL55tVug31xM2fRWzY50ECS3u4begLCyNu6ekxiDD_wdMGqw57-prIv3wlnHgk8VurZvmeIGUX6JFSyJK9AaWNqTxIrpfuhXpP0P9MzfAS_SmrM6REK6UmnPVU2LHKGAsTdpah51PiP703e64Hvy5s3m1o7hfRv_v064YimBmLhO-19MH9gunEnWEGJfj6WplXnZkkAjIJ4IPbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=EAkb_1NWc4v2BBjNBs1xTxytYUYE7qYA7OmAGnGxbN1ummKGW60eJKuHR6ng8Esw7yYI_wEvz6g4BIHzR9P1zov2GG8qt2HRsSJY5yeBFmuM5XXvgOvSAGktGngaKg1v731IIwcBL55tVug31xM2fRWzY50ECS3u4begLCyNu6ekxiDD_wdMGqw57-prIv3wlnHgk8VurZvmeIGUX6JFSyJK9AaWNqTxIrpfuhXpP0P9MzfAS_SmrM6REK6UmnPVU2LHKGAsTdpah51PiP703e64Hvy5s3m1o7hfRv_v064YimBmLhO-19MH9gunEnWEGJfj6WplXnZkkAjIJ4IPbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB21pQdhA3RWfVyuSKGnZUJZ8s_S8fVh5QAiJGP0-lo4kiCpxbMKz6RAHCgGcpbuvmWXC5QpHjtOLmwptEdS847Px5qAWt4D7Pa3kYXLPMC9lnQgvsoCtUD2yXq1IbOxMXxW4R4Bv5Ae64qH-KHOS9jTiVD3j3XW0qVbTs2eEESJzuINz08dj3s-0xM6lr6B7-Rhcwu_hrQaA_3OXkMxTyzz8hjHYa6HKcVVBp3xeMv3wn2WeAkno_gyRKFQSDclj4tdq02nO8A79K6313f-cnD0ZrxBd05vmcvyIuJ9owC0UFnSozeeELoFaPIoOL0c6WoWPTWLTRarcWlj20UCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJcKRXNIoHhICO_z-hf9KwUHeVZQTA1Kxccvn7H_ebVNvM8ImbYwatycNc7_a2zilnzmfbuQ8v2ddR4iI_DXJYZrLXudJvkUeRE_NHH9ZuTQ7t-5jYeHusIL0804Yw491HVm8dOwyyKErijhFxCp9EQWh_u-imttzNxuZw0EOHAi7KUv9B5d5v5tTBJ5tdJ-CwXWkdLnJMu63aiq8RtUhBLAIcAfKOGe7tU7zDIr6m1yoNThCsZiT2fi3IR4sn7vV75_cJKhbHPucbc53X6tFo-ZJjKD5TunCbH1nWKL6xujEOnu6o0hlTPZHYSsZMCJ1oinmf-eQPN75Pcs4-en4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ji0t2X008NzAbggTeyHrrsN03_KCy7DNFtXJmjV3clc5_DbVstlg5S-aObquiNJ1gHq2-FH8mhFALE2TuLpMf7gbSasLc-iJWsF_iS-e4yZ_OuI58_kDxt9mxvE6bVGmplrI714KgkOysP9Zc3XgiZncY2BE3eilPvlUkgl2wusEI7RXdW_NT0f6cVpJ6kdla1WX-DZ707GF_9d2aTL10CMZE9MWqojkWmzZvVKFE-fpDbqe1Cqvg8IstscahQXAkE6-8kp9tDcH79oPgUZM_-KzadznNH0rw2g4gFYHkbZUsw8J-fJOuhavwUYKa33zpJYscLke7_5lv-6X3hHovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqCPbfSULoeHFT9doUxRuDXeUyspVab0pNh70emaROGtnnbC8bes30viQWRNiZvdieFpF9J2NkNQ4IiElW7oLrR7bVbYE5SpbmQ8FrLhoVFUkZuvW_UMtXCNw0RrwDsE9CCWxKzLetYwQEzJpRslhzuY9aDZ6R9MR73T3WxJyNBa-4zED5QwdC-gfncJJ6m3IXtCqMUftSg46qppUBEahuA9rKEnsTyYl1iMRfqlbuFSGNA1tSPcByturicoLVvVm5wMggyUbnHBfUP5asE7OgD7adufJkdKSj6lYt8a4V723nUGFy_MeURQKnLr_o0PS6Xrin64Y32n53G70SxK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ctsc1FzaozvY-b7i0yryuIorz3x-ZNuAxG25DSdxeo5acjZ0fMUN27ZLW-0KOmjqQ8MyJX7ZHZv-aDcYq-L3Jz8UcqrDsTpyviDhUorJ4jBnQ06XkhsQtxxZwbIOAHANhcwgPmpKlmIXRLaRfPFebbeI_55f3A8wsu1WnEsOgb_ui97E1pj98Xt0YSN2XENTTDioZLR81VZcnoKuxratPZbmc9PS8xdAH1sqqv_mpZV3r09ud9hxupq-88Gtb6-pJae6DysMci0Tjb7pyJLQYEwy-YdSpKMqQbOE6GTKLTQDp6HkzHK9puKNL5w7-wsSgrMC3PFx50e2U4_GfuztgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd_hNsaMRq3npQoKYd5OyGG9r77KE2sgfx4Rr9tKPrp0YkpemLiJFNRAzZWAs2sDjWtPsQiTsLoHlKF_74dhQPW47l93pndShSvXhOgmhL5uD9qjEl_4nYV5PlPWMLM7X9hKYJanwV-YmRiLnL0eydP7YnUG702mzauWFkyrIu1H-O1BC3G7-FVnhBMXEWhOb8bDQEaf5iYJJ3rQna9ltJe7rn-3Mw3H0cx36TGQsKZ0TAai9eHZt3GudGjVn7dQQWTMcIbi9doP8GMNvcNXQeDH9xwOczgdkI_9E0RfHOHT4DB83O59E7RIWBbyeUykEh34C48HLWzbXDovqvxAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c235EEPxPMvqB0WvJ53TvBnM89PI6MVB4PNTabTAAJVzvUPWpf6L4utzy5vc6W_qx7H5er63Zc9nW9mB_yxLsWP8JtK6CKdxeH_WyanMzViuT320-1RiB3bU6zTsBT2WWO5sfVkDPtIPGUMkMSweANIUPbqAEsQxWPHY2fFBZHO0hmeHpTOk-cTmUWtJL2Zp4kfL-mYMK4BtvGTOVmMNyu7SghP3yWNhIwC-RWg1bWaeRuReF3UQsUv6lEklBfyzQzLnRf1W7ib6nVLHt2eBXh0a8Z280TFoXzRffbuk9IT8yfJMGzrFronoahLy-1vBlUMPjHxfov5i2Wg-maNGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=vyRTevwLB-JhB69mz1WE8VsgRpa7ZamWy2IwUgPieG6nmAA2MOVHzd8JKdEYy59JsE2-y4UAdVJLuoaYFpK_oCCMrS9-xLlz9AkQVcqho6nY09K1NhjUQURAE6YOXKmiWDfv7M5WxcjdInhKtyWnLe6J_215fSVcGN6LYRQpwhuCSG8HEvAoA0lZJVaVckyVkW24wyJKfwSudKLYjACjXYH9TDQX4jR1tYScNKd3sX5sOdsZ6xklZMy_t6u8n2YEX72XAcaFRimRFbb0nuOPBlf43g8HFy-dY_a-3NjIxvFcw7dhGajd0Cy3p5hB1erDhwNSVOXNYdOWMCAvPwEPIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=vyRTevwLB-JhB69mz1WE8VsgRpa7ZamWy2IwUgPieG6nmAA2MOVHzd8JKdEYy59JsE2-y4UAdVJLuoaYFpK_oCCMrS9-xLlz9AkQVcqho6nY09K1NhjUQURAE6YOXKmiWDfv7M5WxcjdInhKtyWnLe6J_215fSVcGN6LYRQpwhuCSG8HEvAoA0lZJVaVckyVkW24wyJKfwSudKLYjACjXYH9TDQX4jR1tYScNKd3sX5sOdsZ6xklZMy_t6u8n2YEX72XAcaFRimRFbb0nuOPBlf43g8HFy-dY_a-3NjIxvFcw7dhGajd0Cy3p5hB1erDhwNSVOXNYdOWMCAvPwEPIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6viKqzfkpfAlpAZSa5m0H1_dMmqtGOAoXoGrOMWHNMkN-QIlUWAgzf2hk2Ofp40KKwWnMZQCNxOvvGPJ9p23YXQ90059YFhPPxnefH8lyHHi2GiyXgZBjP46o3vYU6SfnpQPGJ6glZSDduvYExGaPk7raNnweieUoju0P_QIoc9p-5lTzTIedvKhqgkrrpe4Td5jc_fZ06F-Gb4beUXgijpyZ512y_IDOlBNp0VOyQq4WrSo3aoEBxb01ENDly5ilN6cpu7KQoSBAtsQrZj8UF6hBlEaYtV9uANZXOq1mUzkdu-fJNvBsktqWun4G5ct7kSDWbiDu6UgE8q913J2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9aNxv4qsEPAyCgSyFaM4GU6Gm718BfAK_dahSzyGBR8KvLWVTrkEAj3eLyYPQn3HVhyLM5Ckypo8qmHCrUekW69HMVim6a0blabPKuEJXeL7i8VZWA81tDwSt8aRUPx2ob8ubSPQsHqdNDFBJw7TiwKPJr4U2SqDsJ6aFNJ1ve-9avDNTWN10VDsP4_Mqf03yX-VA5iVUcF_zf6lfZwQltranVfTZET34_jgmcmUUNOi4Okhba4gR-SghQXFhZANlOD6jsI_JYgxOB53y28WijcoDnL8wwSc_AwfkQStGK3kKstaIt5C5uVFlnk-D3F-CtkphZz_dI0WGlci95-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtW6H6rlIvDdKMQ5JnwUhkk3iT0ZYUxoiqSXQGbkDMxKnjZhd9MQX_DSN3_4zEVZzbG4RutEb4z6GcgaxTy5-komkV3vhxIisxRNVD1gj9ZQVhMpVASOC4Vx-HRe8Iz99daoL2oVqYhQVXm6po9T4G_voyzfcl2ZIWmT68TQMI5go4S6bmqik_feKoMn47rVXwq0U83uKX8hvpjM9bFAeRET6SuP4FCWe8nHknnSq8Ix9peyQqkF2RP3wNk6L1KIfpaBhSoPbABDRsBcNSSIaHPABDzy98X2Xj4qazdrbFHdwj1Ywa28GkSw4oIjcXNaSiehVsVx-AWFjwONVDgRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXbORj5w1KsbdKvhaR8mcVft4Y0uLKLrTE6FbuV05M6ueLZOT3XsITWxtfNlEkxFxetaBZW8eDeSNf5emtnP9NVjYWpExsqkbb6qZcEMqgrxUShsgWQUKmxFDDu8NFdz9OGoqeBBa4YZDou3kEnc5km53NN1Map8siSoGqSR5m-tKbkkmERxd7ZlSA0pbDsY5GTIthPXCrD7Rtg9CvpRYtoMrzhY4Id8Pf2wUoe-lFEsveqoiUwPb02ufLX1oon05N_NI-HsAY06Gv_SdLpOQywPixh5TYo3Oq-ozAN-G8Y65EZgFnaGFCdi8Rlb7_6k-g3EDagAct_RYyxNJAejWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq9MqmE_x_Mb2Bq9GfivR14GwvEn1m8Aa50-xYo0sXKu-vb9PS-KHp19EqTM01cqLH_rGBgPqeaiLMKC_aZHYsCSdwwttJEA0RRsy6AeYrrJpyZuCcEwX5KsBEAYXQ0ABn6lrj1ksTf1D0scbuPHhvkjIcnuv_TQwo3jJ_2Nb2g4aykJs_TcnGy76KJylmPIbe-ed1NbrbgoPp0vUxPigzIuDbbzhZJ0MbAbwcrsE0ghFDQZVWfTmC_tdxR44xsCROUXKIzBwXewRdM-g4k_PiQpTizCNgLdmQpGGg9_JPNngJlbzIRn--utMbpijNVtdlexi6dny-PutQDO0E_WDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_gWHnjoEpZ7wzUZW14tiHqRQ57P36Mrq3vTwwy3MRTodqDoe9Dw5AqDoH1l3ukuHpqHGPU3ESIqmtZV3pDWuScFdtj-9vNgeT7a_3rOctND4OLQYrTDytF33SX696MDAA0q1IGTZsv_FZ4MzP_uWjqB-A_gngYUFaRoMSsiuZ8BtYNp0ZYbQ68FxefRdZrY-iZg1CdMhZVYVqD6J2JJRFiDz61pubfwrZRwrlxyNT69udO56boSeYCynLhh-1WcKbvO_esuwjKoW2TjFlwijGmWfky8tma_5OZx3gaPm17U2JBjo3J0ejB4vPqETlzLkPPRhScav0OWIWogGdmUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nfu84GxbyCxSkMHW0MSmME0t4KuBAE5DcN1ssbXM7C7nEwrgyQ5JuVUuUziXzXGp9ipyZXaWNX_r6aXzA4Za1eMxdkM150bw7QowQmP9XL9E-jcaxoFCnhtt-meqte2j39s2CnE8XF1r-HCv16yn4WnFBBj85OMOlehBm6PuA3Q-QkBQHv4rbDiVhPvcKmEFrJfmgvQMzdq7W2OGImx_ip9PDeM1PB-5B0JmqdrnTawBL2Vbf_92zzH4k5hLOwgh08XGe_Hj2pkIer51ZG2d_H_VB7A3Unp9iGumLgWLbMaqP2iFFBkLxdhh5QtcSHOY2e9R0AC49Kw5s7fFRpdHaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvmYoyhWoTuONhZeb57-FnJdhJzTj3_d5PAJwBZ5bGQokbV556JkgJxiA7HTxb79iHrMZwWF-ym43eejp1Z18y-uuapibTRHweEk4KSmxfI54VOWzDQDdq-1REJuwiB15sRF1AOSzdRXf4yI9etGDme6gxarq6Fe6ldozuaQUPSjpNO2ZNqWgJy4lU760KaKu-KdVZ83-Pr1sSr4G8d-f1yrcN2X_b6NdijRJWGj9yS3YoBI-4PCds5BCVV_ARW41KkqGY1WNokL82j3O52PiXzVHW5pm-Ev32G0g_dPj4gmajBOAjcPgD6WGM_4_9Wo4jH2VFVFzQTcn4abOw1y5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqbxDMRePEo-igZj3_0A08eVV4KCh-ifm8cEydI4PbLB1zd60YzO_7FMKr4t0YJdbRKn8oilZE328HohcqEwFaDcdkDctazQ3IC_htZVi3T38t-ZSKJiYyAL1aJKErE0dVrhZ1F3xdvNTZzsu0i0LnosT_1shHVlNzZYKXnRvt_Px7l52fiFRhsAZro7_oH2Cq1TPtBFbu9ai1sf4kgxL8t42g7Kty0VLk1ptdsvj71ki_bXB_hn39OMsBKLTcioheg2jNJK1iJZIAhFN35QjAYwZRbvabbmiNguMDs5pr5VPAjnp7I9P01I2zPU37EMTsdWSFVGSiEKRJCdStetVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3bs10s5jMWhMzfOsIQBmOEie6YdLfE9KrmR08F1RaDwkC0LYjajXzGAuBPeulWlzATk7IQHwqa-aouPjtzzdkZcLSmQrFwYIOSJqD1yV6RdeAzkPNiQaS7azutG84Alxq98O03p5W7UibPjnoeNaCJaOM-SObLMedO3dLynRUaypeHoKZzb0kVg3Als_zrYPPLHDRO4U8LNz3KqT1zp8DXO11OUMcKXzM9uivI_6nKtdFMqHrQABfbBMS9drYYTJabxZCRSm7oI3oi19AC_p60mhqzndq9zxiPLMp79Ye3MFFKLQAbYKKW7M4N9U_Q7PFns_-Q7e3AFfCfVEtQViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8z3ZbMmFrHWCWl7nJHtRGKMj-6zcnki2HEvf93AYiRd9AB0l7KAWwJsRZMZcokQjJnNmqwmaLEoeDqRh2sNt7eHzWwhzxk6cCaurcfpJ5KoaVQsVA7IbPhXApuENkOba4YUJNWQFEwlJ7aparCaJxePaE1NOmcTxspjPXOHZxzOrbU89Re1j_RiAIJzfBm_He6b3Bgphz2LGgtAYpGhv4B7nDur0S-g-m5d6VYBA7HZG2sPdD4D0onyrkw_XbJsVDz1x4NDpCkhVNKcjsGIAiMAAf5p__ab2S-E4YAFihVNWZnNrRVs6VJXRxoktC8l0eiI3rVgzHwttG3refJixev8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8z3ZbMmFrHWCWl7nJHtRGKMj-6zcnki2HEvf93AYiRd9AB0l7KAWwJsRZMZcokQjJnNmqwmaLEoeDqRh2sNt7eHzWwhzxk6cCaurcfpJ5KoaVQsVA7IbPhXApuENkOba4YUJNWQFEwlJ7aparCaJxePaE1NOmcTxspjPXOHZxzOrbU89Re1j_RiAIJzfBm_He6b3Bgphz2LGgtAYpGhv4B7nDur0S-g-m5d6VYBA7HZG2sPdD4D0onyrkw_XbJsVDz1x4NDpCkhVNKcjsGIAiMAAf5p__ab2S-E4YAFihVNWZnNrRVs6VJXRxoktC8l0eiI3rVgzHwttG3refJixev8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPrtTUltNoyE7Ko7I3rHRCAuGX6mGkS7fwPZbFKFgqI4_uLPIfSNku6UAsj20LyZNvMUiemVJnMEjk2PbsmMlzpZtLFE9-xeX_j1Wnv5Jfay9nt1oXdBsMSx7URUw1s_0p9KgHjGs21X-8sv9tJAaASKwPN6iqhtZsF55Rq-jPDZkqdfaUMHTaagPSSaq4_oUi1xL3pZVpbsBGk64_7ReQg0gTyPE_hS-1lJUR4k7qEt3vtR8-yUbKIekGSmVxyalcIVADuoGZuIgpfPFi9nRPZ4B-feol8aWE9zfcogQT4-3zt7FADv9ZuDATHlEIzAbOHnbN1F4gVdd01wfrFsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcmVUa7L6D9zeMjukdvR36YHMEISqtdSZkoPKitxaPivZJLV000nnKbluRxTJKLz49Oq69eGE2z7lYd-VV75LpQaV0MQi76hwaIZyF1kQw4HBurQKMik_RLwhaCQRdlrcYXQwDF8nbX-zcS9pMDpRLUG-5l5dKLDE1ZuqSrCAtp2YMozH00l9_RuZYmx60FPNlz0W6YdGH-EcyAOmt99GdfAEOMsiL-XiMIoaY5jGv1GvgaH3HTMA6hFV1Z-mcb1djTkAtwPnN7s-P30oiaCg4H37ch3TS-Sbgd2ih8wLjrTOLveyusugFDmjm4GbWLveHZL6ZOdPFxuW4fuOU-IBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNX9GnSfBhr9MpPZA6h4tze4MlbYEkOoy-haacmLw8O81hrurfJwA8WJu07sAuK7LCQu2N9IR67t4MBvcMv3HSOd1-Tv5M07-zaUtchastIDHI87ZzbU9D_ecQQtsV5yX-084VBgAGv7a4rosnN52XJT049ejZ65aV4NSSDJUqjuOOU4Nxjras5uo7bG5GzHErKG7PfdWvVX4wEB4mgRw0EDF1bnO5CxgBAHnFuuH_Yn76BfBHJOqhkxgQ36sRsxwpqQec7WxBY7-FxDAXksIVMN2nmJyWHLj-k9IhFanKck_hDPGuQDZisVKGUJVZUHkXL1YSuGoi368ScZ7Za5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6Ikd0gGBM6xeOjbxXBs56UZfawHtr1tJyWL3RrF4cQ9Yq-i__GSlpEzy2azkceNI8pDa6Ja-fwEf99KDt2TL3z3PkSj-PHnVOEdLN5xvDo1LKg9BH8QdtTpvTFVgAEtTonGthX0197p9OfVZteOrLEMA0jJhMReIUtYz1_WWFtNoMpmw5aVl_busNFyifLneXRWWP93xwNlTzMsxcCPzqfIg1XkLm-dk9wUedTC-kc8E1toUPKOyJNeQ7tLZlf2XD67ElG0hPH9gdiKV_btzZvm0BVwF1HEm0nyMGne7Gfr4LUFUTYBaWQu0ZoPGa2OzUnyObOh2KUsNjMF9F97wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGRFQJ7WT8DGXaIvpQ2XsQTjyNyFFtQXHXWbgKv6qcqfcKtSPuYTHViKB5PZYVg0hHJSJs8QoByT3DaADgDiew6FrQArW9gbM0pVBAXwEzBRKH1a68YoEjnsU6aha6Gc3wvoIKeNRi7wEHJwNI9xOd8vnllxa92d4Ej-hwMOqTkVomgmpMaAoAwYgU63GrgKhQTh7tnPBKpPY0qJbkuepkVLu6DV6tDc6RL-3i6vw1ZcB-tSPFeo2JN9eRMq4Si-OrlgDqdpY069KvG8p_WEUiJQfNRoM9l_kkScNZIgogZ5V4y3XAXytv4bkF6LM00jir9Yhj7FEHZi0fsywmp5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grx5tH3Z_qp5zxJv2eohzZLtFH6PJm_GxbUoOEg2dEVcEMsscFHVGuC-XF3KnCa3jVRqUa5W7lh0WittjYsFqhrRxJJqql_hAf4LlemoWi47WdMcqHe1v4c4YtBT41rKgGByZ1JGhc6OBV1qo6gYze7V1UmEPgTNh1QpPafnNyn1pzLyt-bYO1e7rk9_VRKl7dwTdzG7qjvEDnAdJ9pXvyv6B6bKuuCl071yiMIx-SmMoUAMHgEXYdJ-hoX2hVopVCWAbLguQebiEn_IXWyNpYmBTusuqNZdScqMh_afQiUhO5LH9uJV4lN2x5F8OB505IA5UQtVz29QIfkaPvTuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdwtDwb6fbWkT1fdb61KFprw4WqZCKzfU9EcsWLs99pmF5sVenXFm-KYuILIf3OiL_wLxhr_fkMZYCwT-kZO2ab_VDtsWAc2hnCkeLT-uKdhm_7VGYYrjXS5U71MauohrXiGuI8-zXecAzN3yUOGxnqBhRcebCf3HAYKvdwCsICLlJkh2J9HgmfTN8TZ3EiIGgJXcj4yak_avFPV0TN1_wUH1zhv6eTOkiMj-zJmnxF4Z23bmD4ExKa-hW5yRW1t_mQrUkOIvs922wwwHaa3e5kPUtW4eQMZjkctCgf5XsaB0BWQ5YJU1FJxZOM_5yw8icLRD3nVioz4CWMtDaTEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UicHbeeMDu4aBEfVPsvbnoEg9rBqc3y-EhItzb5UA2ZQq4D0iqc7uA2vJ-m43RF7wK6zJP1nyInIiGPvyHW0q-p4VtHXW0zPFkobvA4wkOPSdcVHBt3HMxNhm1BV2Qo8wOOvJ9DWMPS0FVc40g-_LY4WKdBJD52IA2dSOty4kCqVyMlW3UJAtoQRQpxnBpOAuHXFiNxNgUjHFZOUqQzAbBqcFg50qt8TKA8HStSanXQutACGDnfo7VswSZ4Yj96wloFIwA0--bdjxIfe2Ddq-nXqiTRXCwTbHkbWm4CTWHjBSA_baPlWNfKaKbFQr27HNSHU4rL_-nOZKfohin1fgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myJOFd6QVeGj0muCxGtZ_PpVIh3ysffasaF7IP4hAhTJ4X6bYJnIC9NQ92UPpBAkTCBkmq4o4PUF9aaMO7kEXWDuHVOZCtGRGEgJGM4pVBY8qRr_bl9yOVYYMEW3_CVnAQkqItjmZ6meIkL4TDUuIQCbJ2eBrSXQ57SOqeI0g9FoKWA2vpXczUcaoXky6K5XnEzzuNmw0BU7ktH7UW9HlZevR1imS9CnIR-dvKIOGnZTsxSt1quXSOp9mEGMSqahWfRk8hpBhlLPEKaOTKOSPAFMDl_p33uoOSrAELLpPGVda6uyRZVjDc3eyB1poNCHxtfQ6Ex6uFzdLAGYOe8mDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk5CdMJ7s0kAtv8MJ6jdH8leofx4eBYfeVTIcMkGmGg5fBT8zGetopBHnWadDfoqdEAdGY0BW2UhO8OUhm0aeVj_udwlRcT1dhgZ2_WvcgLbRFGFfJpXkCZUpLDLKZVwhCe5wWg1zgiRa6BRiJFVrOpDyg5RPNzOc3giXdsTxh8En0PbQg-d4mcvnKbvWYESevxnaQ3HpWBKQsx4sbxKT4QBKaeiINDYIGNbW2mbGA-r_tsKaYGcu6YbwcVrxS6kZjoTMeU5AS3muR3bqYFocdNK53tcrgN3yEzpnpI5itet5gvH0FU03Zg-jUp2w57yT-TgXVdpRdsAK43VO4ymkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPDxRLxA-Y5HuHA2g4dBXIhdQ90vP4CEUGtH3AqU1n2ip5WwC43sAYRVPrkehd-7RSWJv-VUSO5orZ1MdldrmRDK0a251_lhlu9Dh4_N76iSDv3uBf-DGmyAzBdfE8Bbovr6uwnEYIgdmUIZu2BpaZ_1X43Zpn8PTwgvJAeScLJWxX1e65L2ak2-GaPxIzZ96GkhGBZBWGUPGk3xyF2de3z3ej6j_BFW3kJ055iNaPcsDNgCM7qkfYn1NELi2opZY7ftkxeyFOMLWzVzDH0q1AXvEPVQQN_tsOOzb-d9nwmx8NeUNsv-bUmMibjbmUi9Bl_ZpY1N9Y2uLwpZWLNacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
