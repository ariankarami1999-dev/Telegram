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
<img src="https://cdn4.telesco.pe/file/izuuVisBsGFXo6XY0xCPAbtD0fMR4K535O32G_mpOSMHi6reHAqmzMoJhhtUh70-ID6CWxQP2ogM8_5gEZJdns4DqVU5f8izhneo1YKmNJYugG3fvUbqjW6txMPAjKNU2vazUleCFME-unKULn6-dao1XfScN5Is72UyPQLbQiAVY9RZPFiJmuapwIcu6azy5_8-WEHNwDztDcMa8HagU9qwxs6A5OhE9Ybp3U3kqJMQFcEHW2GS5ega0DEp58DzeIkF_aBBLjnBBz_FztuFAJUb9BtGgEiR7znX5ltck-ovPy65klED8nkM7ccVgf1w69eBCIi6kJzLJRdbYU_ARw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 444K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 15:06:30</div>
<hr>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=QCeSFHQh0nGMxk8ejyg55-HlSZCJnQFBRxsNnOYKyi3nYH_du_nQy-11R_bc4UxKkZnA765Yi4ywlAdEJSOMCRbLK3Ju1pAWPJo6ZMjc1jTYN9PKgZ3Ap1rz1v1Sghu7fO_QUPJ_MXHy3D2J7tJqoQDp_0m3DKsfLeOMQpDrlGXrCMgPn8_YQUSWmYxBTv9sbRBumtCuHlT9QMt3-lDYn1HQNj5cJ8EbiuFGzl8G_LhUquok4kNqavK5sDlRXnTV7sS8Nv0iaaZYOH1Dz49jXoik3oSm1iaXowlgEMVBbmrG-C8xZS-T4E7qgO5y13SzmlsMwf-TppSwynqLR98gSp-IMzqQciwKHWX9QVw0Wa3g9ErEY6SQHfZI7o6nS8YNhJxq992CyBVwPu0Di_MMnxlbYmTwCo7BqLvumGWYIl_pz2wc-xqJ_1fbHjy7DAxGOeXPKMLK0jPjkX_EaZkDkEXJGaTXcyc78L8Q4AEbN4WLZlMWsEI0TZSR6MtoltFxPO7P0GRYqk1kOX6U4nVblAcAEaVFl2MyOHPqAZY45PjO08GW87Uv86XD2O4S6QXzyS1Rohl8togL6KEtDYg6SGrd0GJhcNI9lf4U8HsQHIHHTWtvp7thRu4HUg2PQI4EXXpMG1mz1A7WSa0tqpdy7AHtddjlMQ-uDJxxS0nkqmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=QCeSFHQh0nGMxk8ejyg55-HlSZCJnQFBRxsNnOYKyi3nYH_du_nQy-11R_bc4UxKkZnA765Yi4ywlAdEJSOMCRbLK3Ju1pAWPJo6ZMjc1jTYN9PKgZ3Ap1rz1v1Sghu7fO_QUPJ_MXHy3D2J7tJqoQDp_0m3DKsfLeOMQpDrlGXrCMgPn8_YQUSWmYxBTv9sbRBumtCuHlT9QMt3-lDYn1HQNj5cJ8EbiuFGzl8G_LhUquok4kNqavK5sDlRXnTV7sS8Nv0iaaZYOH1Dz49jXoik3oSm1iaXowlgEMVBbmrG-C8xZS-T4E7qgO5y13SzmlsMwf-TppSwynqLR98gSp-IMzqQciwKHWX9QVw0Wa3g9ErEY6SQHfZI7o6nS8YNhJxq992CyBVwPu0Di_MMnxlbYmTwCo7BqLvumGWYIl_pz2wc-xqJ_1fbHjy7DAxGOeXPKMLK0jPjkX_EaZkDkEXJGaTXcyc78L8Q4AEbN4WLZlMWsEI0TZSR6MtoltFxPO7P0GRYqk1kOX6U4nVblAcAEaVFl2MyOHPqAZY45PjO08GW87Uv86XD2O4S6QXzyS1Rohl8togL6KEtDYg6SGrd0GJhcNI9lf4U8HsQHIHHTWtvp7thRu4HUg2PQI4EXXpMG1mz1A7WSa0tqpdy7AHtddjlMQ-uDJxxS0nkqmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمس آباد یک انفجار یک سمت و بک انفجار سمت دیگر !
حالا عرزشی چی میگی ؟ گاز و گوزه ؟!
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=exA5uE8-lzo9-yRmJDmNFb4j_7QGmYAyW0l-5ItkVAv1syngW0WH0eGRLVPU9M-_3hx3Ll54Q4-4m72WTctMlkSeSSHi8guDBN6LbBlp9OqFK8Jf5cIE-0NF-KHROuqwDj6B3crqTMJoeaiDIXOKvgNk6ekOVa4-K2opz-6Yca-KU75E9lZgGLCEzrocs6tmmA4q9P8Hr7H3TtUWVpjp99ntzmw44N1ZCZ5-rsw8o0nrKRmNuD_e_0JO1HDtq77fHk-5mzbFcz9E_w-8U5dIROZFLdDnq4tpE9Ikx-FwVlhL1jtx-Rfmxmyntj3vtSnBHARIpbm3UgTl4LY8TNq1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=exA5uE8-lzo9-yRmJDmNFb4j_7QGmYAyW0l-5ItkVAv1syngW0WH0eGRLVPU9M-_3hx3Ll54Q4-4m72WTctMlkSeSSHi8guDBN6LbBlp9OqFK8Jf5cIE-0NF-KHROuqwDj6B3crqTMJoeaiDIXOKvgNk6ekOVa4-K2opz-6Yca-KU75E9lZgGLCEzrocs6tmmA4q9P8Hr7H3TtUWVpjp99ntzmw44N1ZCZ5-rsw8o0nrKRmNuD_e_0JO1HDtq77fHk-5mzbFcz9E_w-8U5dIROZFLdDnq4tpE9Ikx-FwVlhL1jtx-Rfmxmyntj3vtSnBHARIpbm3UgTl4LY8TNq1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6BhMAqyf0lWz-p9j17w57N4mce19QZ1bRWfxaZEcTDOLBgaXWLXRUyA-IncXkY4Ey6hrRMB7oYLy4mYFMh1k9W7pRoP3an9irnreQkbhGdKC0K252a1XjALdDVgYVyBtlp9fZrjK14fbOu5E8Xrvt0rV7OU3EWBi445IvBV7MKHIJNZB2mZjWlHkxJC7dzg3-kDLB9eceJAEd7kCtS_p2SS6MMgiN-7522WsFuyOZPK4PlAIlorLqlKzAKhCVievHufA0DrD_NgAS6VX-1HtvKwusVAcSeN9zQE-ZrLqdkBB3RbzeUV6TTAon-xQaqfceYrmWdp6MrqA_7kQHzgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=DfyIgg99I_bCLZC0aeXk0ME2MDGzWHR19kvoLC2ENoN4ZI-JpGsVX0RSKgRktLKppYtzHxpdr_y-Vp0Olb4pTCAv0Vupch7xTTEi-dahDtRscS3FboN50CHxWGpnjIPqjhiCs1CXOqE67UFS6bwTBFAnusGvbnVkna08yjPZAEB00CW5_hcq9IMnmAXzrzw1wZDch26vGAl3SLBr2mkLqG0FO44rz1CdDFK4NMo5ohrk4aLNeb2TrPzWLiSPCNGg24rkJJwLpcmk_7CmAQdf87Gsi-12A8Vo6Vy0yhKZXyEJvYRD0qCXQ93s4Jx3QvRcZVeyb0nnqUvkAlQHzgehCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=DfyIgg99I_bCLZC0aeXk0ME2MDGzWHR19kvoLC2ENoN4ZI-JpGsVX0RSKgRktLKppYtzHxpdr_y-Vp0Olb4pTCAv0Vupch7xTTEi-dahDtRscS3FboN50CHxWGpnjIPqjhiCs1CXOqE67UFS6bwTBFAnusGvbnVkna08yjPZAEB00CW5_hcq9IMnmAXzrzw1wZDch26vGAl3SLBr2mkLqG0FO44rz1CdDFK4NMo5ohrk4aLNeb2TrPzWLiSPCNGg24rkJJwLpcmk_7CmAQdf87Gsi-12A8Vo6Vy0yhKZXyEJvYRD0qCXQ93s4Jx3QvRcZVeyb0nnqUvkAlQHzgehCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD6oEMCTWeo1WtyahdCn-1E3FdsEFugoUjTxgALeUglf4W8YBgzjPyrCNhKxernCwfpOmsPmUnzRlyFbJyZbRGvQGgi1rLwh_964o9awgqyBd0QwBKUz-L_zaMftBbnSmz5PcYlb4w6hru9asuWTFKQKyNvGE5Rcua6nQM2w_K6NlAF7voeR6jdX2RsA6c7ZypWa7BLptQdSXP6uA1YVExlK0ePPrMxDA2pyPzVWBemJy4HbALTZWE1KQAXCBS6BBFBOWYZb1uZsuIH1Nwvupfkcphlc3T4XH1oR0tpOkyW-Gkc4nC-IWxeJQNdmekh0luliOrWsGWRAoa99GIFkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=CKTotsfd86zBV149WIcqPG9Y47uR8UqiwnDxGGxJngs4ox0uTr5T10rlh4wtWt8Aa-jJmvCV4EhoyVIlUXUs1Hn9YBdL5NoEgiE_L29b-2RKVzUXY4Mu9rQNeuaFahMzSuwQIoqSStjpBU4IlydCN__CSkVlsmz0GWPNHZgmMQGRFp1f3qhWf95RApHMGhRsgIRJPj6b41k1vmX3nxNFO6pgedZZ8-7EOnrDaVMit4MYBJuZLj1J_eFtSMWtlJaj75SFGDAmdcTFr3EQiK6gMHyIuESJEqSler45te2mgZYlK_mlD1Lokl1LOlUJ4NQPD5C0cwhY9KA_-SucBjDetQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=CKTotsfd86zBV149WIcqPG9Y47uR8UqiwnDxGGxJngs4ox0uTr5T10rlh4wtWt8Aa-jJmvCV4EhoyVIlUXUs1Hn9YBdL5NoEgiE_L29b-2RKVzUXY4Mu9rQNeuaFahMzSuwQIoqSStjpBU4IlydCN__CSkVlsmz0GWPNHZgmMQGRFp1f3qhWf95RApHMGhRsgIRJPj6b41k1vmX3nxNFO6pgedZZ8-7EOnrDaVMit4MYBJuZLj1J_eFtSMWtlJaj75SFGDAmdcTFr3EQiK6gMHyIuESJEqSler45te2mgZYlK_mlD1Lokl1LOlUJ4NQPD5C0cwhY9KA_-SucBjDetQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/20467" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0HHAeyukfMq6slW0L9_QwVpL2nlmHOnIjn_ZCKhoXGoGFGysUIpfD9rbw1b4AhxGOMbsldoDt6HnudL6__qfx0ocm_Wi2uxf8Qp1xKp8vkkEzCD8dccMneU6T0BS2MaXZcwWKMJGkuKAgoswILKjS3921d16YmXInMTbnqVaAXrBDtlAQORvHWS4CWapTbgVLRY62lff_3jRaM8WvMkT3BEGaRIWvJxsFgQuOBbBRzmFO-IVCUsiw9htuVDnSyVLd3SBljXeNEPoMo7vNXOfb5u8aCv9vyv82axi4pzU7FUPytkkwOGqPh634DpJmbJHwoAAEYWFeJoxy6P-GbnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی دیگر از دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/20466" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=At6b6wKnHQKpAEzPV3Zr3uXGQnmzlsnDJlBVtwAcvkIAf7hXQX-_gj91EvfAG9g_l0imLcBeYx8MnyP144Fy6Hk6-EW_NlWRI2HUk-tOttWeFa3aTnrbZ1fqZWiOcfUxIMA1YtGU_CH9D2eptyzmS7S75WVlVSiafqhm35RAXKfxvByWs6StqVTOi-itCwT-T3fQ6koygUygDpqbBsOOFWi4CJKflHgltY_Xc_sNVrTtI_AYl2fgVdaWjQqFxww3ShjN5HCTGNUFqhsXJCmD-xiYsldgK6yCDWuiZr4b7uUG_gtyb5X37Dh5QMPs4x6aBJv8UnQUwFCTES2LHTYP3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=At6b6wKnHQKpAEzPV3Zr3uXGQnmzlsnDJlBVtwAcvkIAf7hXQX-_gj91EvfAG9g_l0imLcBeYx8MnyP144Fy6Hk6-EW_NlWRI2HUk-tOttWeFa3aTnrbZ1fqZWiOcfUxIMA1YtGU_CH9D2eptyzmS7S75WVlVSiafqhm35RAXKfxvByWs6StqVTOi-itCwT-T3fQ6koygUygDpqbBsOOFWi4CJKflHgltY_Xc_sNVrTtI_AYl2fgVdaWjQqFxww3ShjN5HCTGNUFqhsXJCmD-xiYsldgK6yCDWuiZr4b7uUG_gtyb5X37Dh5QMPs4x6aBJv8UnQUwFCTES2LHTYP3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش مردمی :
دوباره زدن
، صدای صوت موشک قشنگ شنیده میشد چند ثانیه قبل از انفجار و الان صدای جنگنده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/20465" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpN2YALnjOpCjOHvWJc3TtBdkeWZ7YtSYAhcJMD1hFo2k3bb_YqI7NKcSEDTGSE4J2vvU91vrGdOiptMmRgXL-63FHonICzhLEHJq9iJsgYJsD5GmzYXTXZcsW2f9E6tWwDkKmyei7pyMYF8YWan4wnDdECWGoDWW85-_O4k_ErUGkQIKIBr0QsFBnpX4pwuSXqTjMSwjtfe-XxG3N0n159D8vYIXOvUX-Lb9qbzlE-bGKWMwLxsGORV-3ySGLIdcLvWTDLGdwwDQf7v6nkwEXo_0TS-2vkgkSHk4FW61QR2OWmmaclgMoKVfzxpk5JQOXoYGyp9XMUTA1pLoPVSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید گزارش های مردمی تایید نشده : مورد ۱ :دو کارخانه منفجر شده مورد ۲ : کلانتری فشافویه رو زدن @WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/20464" target="_blank">📅 13:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/20463" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/20462" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه) @WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/20461" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7200405da8.mp4?token=BIvrxl54lAzxpSR51qXr6CmIvQMJqooZWrGgl_ySffEF31BTLMOZW3AodV_gFXqMDPyPLwnfQRmoL3_k3hAXCFOswCK_CJQ9vpilzl9eCXQDJjWcyuV3QZmjY-NgJj-y_XNQi2HOTacSS7GV9hMtpvHv5zQIjS1NkDcYP-dxORGy1uYpfX-7RSKOgWWdELx98nzGOLTlhT3ROrJeEN99uMwsxSfF5S0ReyBaswkLwbPMVAy1Jir-2-5w7dgQEiLiGGxMqbN6GE_q0rPg12EVLrcHRGouha4tlkms6tpqIHT2Jx-bmAQqbx3sJre5OyICEu7ufRAn2-2cya2ocQc5eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7200405da8.mp4?token=BIvrxl54lAzxpSR51qXr6CmIvQMJqooZWrGgl_ySffEF31BTLMOZW3AodV_gFXqMDPyPLwnfQRmoL3_k3hAXCFOswCK_CJQ9vpilzl9eCXQDJjWcyuV3QZmjY-NgJj-y_XNQi2HOTacSS7GV9hMtpvHv5zQIjS1NkDcYP-dxORGy1uYpfX-7RSKOgWWdELx98nzGOLTlhT3ROrJeEN99uMwsxSfF5S0ReyBaswkLwbPMVAy1Jir-2-5w7dgQEiLiGGxMqbN6GE_q0rPg12EVLrcHRGouha4tlkms6tpqIHT2Jx-bmAQqbx3sJre5OyICEu7ufRAn2-2cya2ocQc5eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه)
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/20460" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqctkpLUFjkLpH871AAtQ1SlIRSVZ2XRDSzNyjmOFoPEz6vIR-ud-BnLxv8xG2wuZmgAkJIJwdTm5M_6nC8mY97AU_-wqQvE6_vtH1kBKyIZEd2yIRat69jtOHIg4t3SCCs8DGChIeTG9tTRoz1FmFZkFD7Hr_Umop31tNaySLYDZJepeYo2uVYifxTUD5d5E9yCeLOcG65wa6rliV13S6gWeK43K0UzUztjrp6HbjI5WhgE-2jYMaJZVOGcG7qU2fWGQZsskUcRFSGhY923qqkRLKit_E50K8SrI_w47_VgpSO2330PGSNlSHGyKjpkmDLUrVXvtgp87kL6zMdPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید
گزارش های مردمی تایید نشده :
مورد ۱ :دو کارخانه منفجر شده
مورد ۲ : کلانتری فشافویه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20459" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/20458" target="_blank">📅 13:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رویترز: یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت پرتابه‌هایی قرار گرفت و یکی از ملوانان مفقود و باقی کشتی تخلیه کردند
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20457" target="_blank">📅 12:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دور جدید مذاکرات بین لبنان و اسرائیل در رم آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20456" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
@WarRoom
اتاق جنگ با یاشار : دقیقا در پست ۴ ماه پیش اتاق جنگ «نشانه» 10May به این موضوع اشاره کردم</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20455" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">روزنامه روسی Izvestia : آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20454" target="_blank">📅 10:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooK_Q-7X98GwsPZinLxDStdqddBzNDmhrzt3WnqhTJzv3ey4GvIITmeZuwRlo1rJdcunYQ1P9yaUjQsZGqQpTl_FSMBJpumssjNkjaHvXjSJ-N9j0AdqsLD28KioaEgK1ra9BF935QX7Q3F27t5VcgVZGOOXyE6HJ9Bc9czjBm9tQEHN9gVFQfvZwcgs-02UVfnp4Npcxlr6-xWIJsBUhMmeKMJ_V-UDLHHS4C_skF2RrEB2DMb2pIOL0sUfRnbiaXxpOoM1G11JHJKzmBKMrQt7wlv2Ca3BdllbgEgFsIRTPHuJ9wCNQFO3dbZQu_y6dtnkcjQD2kqyyqcCfHxAAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غزه قبل و بعد از ۷ اکتبر ۲۰۲۳
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20453" target="_blank">📅 10:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است، اما تا این لحظه اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند.      اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت. @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20452" target="_blank">📅 06:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صدایی مهیب در پایتخت یمن، صنعا، شنیده شد، و هنوز علت آن مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20451" target="_blank">📅 06:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است
، اما تا این لحظه
اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند
.
اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20450" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk1eWSf4B7w4hWwdMVruEGTesHbYE1ialvTOc8ppVKi41CkD_Qn4ExwsSXH6E6x4oAwjqjAWPcHh_0_QRs7WolLwYcpjGdfAMCyxNGBlIRwHarrPRk8bxUwGIFeW3LmzDzcg3_TRMOORG5U4XDBeuRSaGr9bJAeN5mq7tduEctZfVOB66Asjg1rBVpeDtzWktB8GS8BuYHMTegj5VyHP0yF-EBAcw4z3BXKlYHVWvnfwfoXgAQvqUTlrs7oOwrfI-9rVl4dBMwOG4W7jLTjVH0JQ6y0U29yl6cd8AiU2gMLs2HPP1AN4qWT44yZwNhnGIqxKaEVwaVAnrj04niUS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات دقیقه نودی به درخواست عربستان سعودی
@WarRoom
😁</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20449" target="_blank">📅 04:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDGoNCW8vP_SV76Nn0hEe5pypWWmP8Vs2y7rqlPzcrwk6nlzedyUnYb9X2_fZMeUndcFC0iKcfECxX2yeAQmWssxMdTwmLJb0mTIO85fEqQHaCG_zCPi9HJrf5UafjGPcNENZUwWsu37m2WKymIWYitqbiPtcutb54l0FjLIWd8e6j4gsnRxlM85mTV6h52FvZ9lA8jUikBvG3cNaR08Vzfi1LmxtBXpUSjdqeF8WqEOWe9YX-PqSBMYughy9AK87zrLvZGs4m-O0S7T9Gecr0fj48aRxxij__xCsKqDVPRbvLBIPDmur0fGHOaUNHUYzCN9rLytUoRo076Sj2qVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا : گزارشی از حادثه‌ای در ۲۰ مایل دریایی شمال شرقی الخصب، عمان دریافت کرده است.
یک کشتی باری در VHF 16 اعلام کرد که مورد اصابت یک موشک/پهپاد قرار گرفته است.
مقامات در حال بررسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20448" target="_blank">📅 03:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZYaGTfM-iYRR-2csdQyOMTqQMMtMxprqrUzaR7A-9YUvcvxiw6iZfIrc0nHNN1XSeUrEHNaXRswLFJu-8ojUiRCbBMjLrVp_HBC7e5o1rt6ODen3kirG1IRiVmNfi3s3Dib0ZvuJdBkgiiMb9nSk9G2fBoDw1XLS1EkfKk3i-Wu_Wgss86LDiz_ZINXROiXh_lD4Wf9b8AGxb_qfkP6nelQnwIRUKUnwtdeFaJvZzW5XxlWwVKs2Vyeu5No9L3Mx4YyaWh2N0Vu_cJc5W2qz2LbKmy1OIZtqpz3OTkCqANRILmZnBVBMvGWRowDgohAppHx4-DyUce6Pbn_EgeD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت هواپیمای ترابری نظامی C-17 گلوبمستر هم اکنون در مسیر آمدن به منطقه هستند!!!
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20447" target="_blank">📅 03:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال ۱۴ :مسیرهای دیپلماتیک ایران عملاً از کار افتاده‌اند.
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه، اکنون سیاست رسمی آنها است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20446" target="_blank">📅 03:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20445">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">لاکهید U2؛ شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید لباس مخصوص فشار بالا شبیه لباس فضانوردان بپوشد تا در صورت افت…</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20445" target="_blank">📅 02:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTa6thrm3yCSE4VephY-oQ54fnTomeMBndNSqbtpPHnWa38Ef7J58W_bq3PBbBcNLX6V0P_oPtTeYXqC2WD5VDAdsENLs0Z6nBMFztZQlAbrmMLyTCAW3LzyN2AVfGQbXQQj4_DpvTH7dqgWAkBAkE1Gp6rRJDAbvsFWAKox2y8_y-FJkziFsDaQ09omoQ6MeqUDMNbimeK3BKGjAmGbkEGjb3YSdLiHWivWlyufw_PItMK8Gi82WG4Qt0wc5Ctxo5jDzrkbsZqbjEKWBlq4RglUk17l8gv53hsH9VwAXTlj_fl9z-9eZ2536xROr7pt0r7sdgt-VRArPMXLnlbPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاکهید U2؛
شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید
لباس مخصوص فشار بالا شبیه لباس فضانوردان
بپوشد تا در صورت افت فشار کابین، جانش حفظ شود.
با دوربین‌ها و سامانه‌های شناسایی فوق‌پیشرفته، از صدها کیلومتر دورتر کوچک‌ترین تحرکات را زیر نظر می‌گیرد و ثبت می‌کند. با وجود گذشت بیش از هفت دهه از نخستین پروازش، یو-۲ هنوز هم یکی از ارزشمندترین چشم‌های اطلاعاتی آمریکا در مأموریت‌های فوق‌محرمانه به شمار می‌رود
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20444" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20443">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری های رژیم : شنیده شدن صدای انفجار در کویت و صدای آن از بصره عراق هم شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20443" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش پرتاب موشک از ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20442" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMI6zUPMcC-jqomKA0Mj46mpp1-MLz1QQJxIGObJMbbn7eUeq9Nf6YvoePQpy7LiHUrtw1SQ_Te81gapKrpHz3_kiU9Ij5MCi41bSU6SWDnh-7JywD1_FAKeEUTaUhTk_VfhlEUclEgoRNhs_30EyDP3E50Jpr7BWFkuEYakMaZT4yC-yMabYCRx-KQ1Iw2dUIbKrh0mr1JICoKlzu-MdShCYjw1PDaKcPjSSsGj0lEoheHtROklLJTdUehMD5wgUsjvQ9yVcwr-EzREUMJ_lbyCQ34DgLqx8Mpb-zZTXKDNDhzUquV_azH3MZ5M75W-1xvnfOiximjkUYagRnrgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت یه کاربر خارجی : اگه نقشه ایران رو برعکس کنید؛ چهره ترامپ رو میبینید!
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20441" target="_blank">📅 02:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پاکستان ادعای ترامپ درباره آغاز مذاکرات با جمهوری اسلامی را رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20440" target="_blank">📅 01:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV3Ow4QfiIsyzCegHg9Xb-T9dA411QVfz5s9gnPJycQJ9m5mhVPnHqLiIBzlBcMDecpf6zYD1lwkWLMTsGwdOE4v4h0FjHiO8QS_Mq1qSB-hrBnXhBv3PrxSudCBWY7Y5X8OSg3TvalqYUhB_WMaXNtaEaEsLGF78pjzmahZG7sLZMQk3eDcPmqU1B1jyyMs9vfUJlDUUqyyReszXLVcrz8hc2y4Ff7YV0sVz3w72zU4H-pKPxx3f5qshaE166RLpH8MSrwIvImG85c9nYllS7w7gnpoCTi9mww_qioT8MG5ZGTePWCBw4XxRoM8bOWCbrJEAygImVPP9r8U_N9gEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اسرائیلی (یدیعوت آحارونوت) : «تو ما را دیوانه کردی.»
‏ ترامپ: «من حمله خواهم کرد.» من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20439" target="_blank">📅 01:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGT4NV0wy1ZLt4sYainLNST556nWJemHxhj_kseAukCqmbpUtvivf8rWzfPVpvHasEjwMUtG8Qx_CiKrRW78Xg0tlP1XLtF4SkTj6L7vhAvHBzMS9hvZJD-02VBQlNPe3gYCQDA_vrAJ6xsJwDanzVa7aOji1yFXj66-YAJ7mafd3BNxvPc5jgy5yXRzf4cfTPqYe2IUbNdT2N-nFemPloBvdFSkhMo3IVzn5m2Rs9gjID66OgYIdIfp6E0wotQKMxFNYS4ZHg7uGWMPqmzgkZDCb3xk1nseFxiogkT6KzhnCh8tB8-vsYUNJgKxqvZ_uKRNevESlpJKDwyQHd3KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون
یک پهپاد سپا، مقر یک گروه کرد را در منطقه خبات، واقع در استان اربیل غربی عراق، مورد حمله قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20438" target="_blank">📅 01:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩ https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20437" target="_blank">📅 01:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIP1QllaazSp2pBAElFvHCZpr7KujK30QDlpjWG8kG3EEtTex6ppRhEHv0CejMOqv3G9wXO2Suv8pOlQpPJN8WglT0_r_gej3fUoSM1Jf-oGS6LcRknAyKTOXVu8-gtCqhRmi_TJhnaOsAyukSHRV6avlVxrhuix9UKLXeOhU6cQz1aZtFBSf_X6zDuNWD8rCctDcn3XnpgYn_VKPWyzcNfkNUvJgM72NzQTtufo-yPAT22e10ff8wepxWgug14VFvyPZ4Q3o2ZQds6rpp0bnqttI-V1IOQb6kF1JlSxaY9_f6HKinqsOIgVqtTnIPfGzFkdIvOODG2kVFYSM8nfCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ
اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩
https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20436" target="_blank">📅 01:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20434" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20433" target="_blank">📅 00:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=rPIjN83ge3S3eKhAwg04gSeHOjTw2XMMK299YUX3NKmSU5jiVDbfAIXqoE8Bo8tAvoiqyVO3q8aePPaOsPJzDSmH4gW6_84FqS-6B6DBpQXMC5Y9d2by4Py_GJuYx1QPBmypMOPm9uu0Jpd_VQ91sXgtLVk5m1g3cbllcKAR87RzVKd1sz9co0k915LBgeGyDd_ftWewBtl2GJ0dMdMMepP8i41eCxncV7L14jMIbIsuL73ojikXimM9dZWBO1i6T52PH6zmco3c3ZocY6YsQ1GfQ9YLKWqBlYnsyH6bTnWGij7u3OYOGypUiZHmJkEQK7Yeiq5NBgUjRXm-SadosA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=rPIjN83ge3S3eKhAwg04gSeHOjTw2XMMK299YUX3NKmSU5jiVDbfAIXqoE8Bo8tAvoiqyVO3q8aePPaOsPJzDSmH4gW6_84FqS-6B6DBpQXMC5Y9d2by4Py_GJuYx1QPBmypMOPm9uu0Jpd_VQ91sXgtLVk5m1g3cbllcKAR87RzVKd1sz9co0k915LBgeGyDd_ftWewBtl2GJ0dMdMMepP8i41eCxncV7L14jMIbIsuL73ojikXimM9dZWBO1i6T52PH6zmco3c3ZocY6YsQ1GfQ9YLKWqBlYnsyH6bTnWGij7u3OYOGypUiZHmJkEQK7Yeiq5NBgUjRXm-SadosA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ‏عراقچی در عراق
😂
(مراسم اربعین)
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20432" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانال ۱۲ اسراییل : بانک اطلاعات اسراییل برای حذف سران نظام در حال تکمیل شدن است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20431" target="_blank">📅 22:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دونالد ترامپ با «فاسد» خواندن کسانی که دست به افشای ابعاد بزرگ طرح او برای حمله به ایران زده‌اند، تأکید کرد این افراد باید زندانی شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20430" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارشگر شبکه 12 اسرائیل:
پس از 30 ساعت سکوت در نوار غزه: یک پهپاد متعلق به ارتش اسرائیل به یک خودرو در خیابان الرشید در شهر غزه حمله هدفمند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20429" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20428">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">محسن رضایی: اجازه نخواهیم داد هیچ مسیری غیر از مسیر ایران در تنگه هرمز باز شود. حتی اگر آمریکا یک ناو هواپیمابر را به مسیر غیرقانونی تنگه هرمز بیاورد، آن را هدف قرار خواهیم داد.
آماده بودیم اوکراین رو در سه نقطه بزنیم اما بعدش عذرخواهی کردن و پشیمون شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20428" target="_blank">📅 22:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20427">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: ایران از طریق افشاگری‌ها از حمله مطلع شد.اما اگر این روند ادامه پیدا می‌کرد، بسیاری از افراد در ایران باقی نمی‌ماندند.
می‌خواهم به ایران یک فرصت آخر بدهم قبل از اینکه "اقدام قاطع" را اجرا کنیم. امیدوارم آن‌ها با عقلانیت عمل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20427" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20426">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:فردا آخرین فرصت برای ایران خواهد بود.
گزارشگر: آیا ایران حاضر است به آزادی کامل تردد در این تنگه بازگردد؟
ترامپ: من اجازه نخواهم داد که آنها هزینه دریافت کنند. اگر کسی قرار است هزینه دریافت کند، ما این کار را خواهیم کرد. ما کنترل کامل را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20426" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20425">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=oQFFbPpxgNXkcEsFwi8a2VxS4M1Fs_afQ4Ubgrx1XZXfTfoMIbrytXqNKWj-HIiXG5x9b9onQbMtwfrdS0qnL-4vjyZIJJfDdp7bxxxpDX_WDZsCyrMzU2ksxBrXTnfut2IPEPCawPNZK2fwq3nfzmGoxswUuh3USmhmmeExiUoyzzXjvHet0iadnzcRGWYAOMERz3vPthW_kKX6mfFcnNZhQsSV4Mz6T0VpBpQbBBsAUiDahVpB8WlkGeqKKkCECUG0S9Azp-Cy7sJYWzCT8KMc2-94Pkxz675hprbV_Xls_9yHPrJL11GENTWCIWYZyubIzgJ5XAGR_dAtYWDZ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=oQFFbPpxgNXkcEsFwi8a2VxS4M1Fs_afQ4Ubgrx1XZXfTfoMIbrytXqNKWj-HIiXG5x9b9onQbMtwfrdS0qnL-4vjyZIJJfDdp7bxxxpDX_WDZsCyrMzU2ksxBrXTnfut2IPEPCawPNZK2fwq3nfzmGoxswUuh3USmhmmeExiUoyzzXjvHet0iadnzcRGWYAOMERz3vPthW_kKX6mfFcnNZhQsSV4Mz6T0VpBpQbBBsAUiDahVpB8WlkGeqKKkCECUG0S9Azp-Cy7sJYWzCT8KMc2-94Pkxz675hprbV_Xls_9yHPrJL11GENTWCIWYZyubIzgJ5XAGR_dAtYWDZ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مذاکرات به سرعت، به یک شکل یا دیگری، پیش خواهند رفت. موضوع خیلی پیچیده نیست.
ما قرار است فردا، به طور کامل، تنگه هرمز را باز کنیم.
سپس، درباره توانمندی‌های هسته‌ای ایران صحبت خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20425" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ درباره ایران:
"این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است."
ما دیروز قرار بود آن‌ها را به شدت مورد ضرب و شتم قرار دهیم… با قدرت بسیار زیاد… قوی‌تر از هر حمله‌ای از زمان جنگ جهانی دوم.
اما ما اکنون در حال گفتگو هستیم، این گفتگو بنا به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و سایر کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20424" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=LmPPpGM1K9LEPR289xSowll6wVcUVuKVZT9K_MRwB2HLNK-8umocvABKiqhAIan2wD7Ak5LvRF7NDYO8MpJrbTumL56921ybKTud3Wegi9F1SXMTn83v4LxhyoJ6etVoGpKOHU1HVJ-xfYdoHI4He1d0KMJ5m0zl7g9WB6rvDmCb5DH6SvoswVKCxajnbQ5IUJVGYDWhU_k3ikXg-5uV_NFSIFM3sn3sgCqQlgvLBwqK7wT-4hW1lT_TFVDthW6prNnUppDXiVOB0m-8YHKF43Gm6nMD8v7CUH3peFLpG704wCGBV2w_deXZQunMAqfcsBZTfpp3uCxsSnLI41JTkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=LmPPpGM1K9LEPR289xSowll6wVcUVuKVZT9K_MRwB2HLNK-8umocvABKiqhAIan2wD7Ak5LvRF7NDYO8MpJrbTumL56921ybKTud3Wegi9F1SXMTn83v4LxhyoJ6etVoGpKOHU1HVJ-xfYdoHI4He1d0KMJ5m0zl7g9WB6rvDmCb5DH6SvoswVKCxajnbQ5IUJVGYDWhU_k3ikXg-5uV_NFSIFM3sn3sgCqQlgvLBwqK7wT-4hW1lT_TFVDthW6prNnUppDXiVOB0m-8YHKF43Gm6nMD8v7CUH3peFLpG704wCGBV2w_deXZQunMAqfcsBZTfpp3uCxsSnLI41JTkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «از همه شما به خاطر حضورتان در اینجا متشکرم، چرا که ما گام جدید و بزرگی را برای حمایت از خانواده‌های فوق‌العاده نظامی های خود برمی‌داریم... امروز، من یک فرمان اجرایی برای ایجاد اولین کمیسیون همسران نظامی ها امضا می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20423" target="_blank">📅 21:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20422">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=et7C4Xt_dha4n5Uz4XJn9499zCMyVYstPTWlRoiCNSYAacInBkP3CIgyvV6YjibGRfG-vyuc0lsFl3hUmdi2TGp9I4UNJXFMXROgz2cnRJ7WVH1Jp59Kgflmaf7OUiCb1ip2Lz6Pom61SpSc5M1U8joYS-eDf3teFwm8YVgtM-4VY9H9_kbkwIA_KCkJI-G4umkKDjgUk7LgxLCVVOAaGm-YL8DzPzNRzjlwfn2-K7Pw1G9j6TkNCddmke9QIxgRG0KMxAReZiTOxdYj4zDWNjUUlTTRfDY2kkN-2-yANR81aZAXZLTuFW2oeasiF47aJTpwYrHNd-86DfY9va0QiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=et7C4Xt_dha4n5Uz4XJn9499zCMyVYstPTWlRoiCNSYAacInBkP3CIgyvV6YjibGRfG-vyuc0lsFl3hUmdi2TGp9I4UNJXFMXROgz2cnRJ7WVH1Jp59Kgflmaf7OUiCb1ip2Lz6Pom61SpSc5M1U8joYS-eDf3teFwm8YVgtM-4VY9H9_kbkwIA_KCkJI-G4umkKDjgUk7LgxLCVVOAaGm-YL8DzPzNRzjlwfn2-K7Pw1G9j6TkNCddmke9QIxgRG0KMxAReZiTOxdYj4zDWNjUUlTTRfDY2kkN-2-yANR81aZAXZLTuFW2oeasiF47aJTpwYrHNd-86DfY9va0QiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما اختلافاتی با ونزوئلا داشته‌ایم، و این مسائل به شکل بسیار خوبی به پایان رسیده‌اند.
و ما اختلافاتی با ایران داریم، و این اختلافات نیز به شکل بسیار خوبی، بسیار خوبی پیش می‌روند.
@WarRoom
یاشار : مثال قشنگی‌زد
🤣</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20422" target="_blank">📅 21:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=QAOXseHlMAEUW-a2bVolygGootepUYDvqEkHbRbcZaorzhQ3yiTcs4erFvWWmhbSBYxsrlVUkUZQ1dRZBneB7nAmkciN3tyj8ijUHdM6kduT3rQ-qDbMowKli3E4mmkvksKFPoitLSga41DqFcQRkeOmLPcXQ7pj7kiUcvGVfM8wrILrjDGAcQ-MS_tLnxKXB9CMLqaUdZBRw955blcH3t-JG-cWHQJ01T-6MpfMrosMAmEv5SoAzCwt4iIblok0ZY1Yc8LKpDQVNdG6uMeKhC1GuhiZXJNN4Xky86Cixxk8J10PGHOBvX4VBFN6a7Y_GOwTWZLMsRVPkXS1-LRD4KaMEABzgejOe-VhnBVsiA6M9vJPTQsu_ni0H1DdOpZ6fzVURscAKU8lSXkkWJ7_9GnuVn3lxR0NjOcRjrHcwAz3a9_10-7UHb5XDHpVfzCR4l_hf9CxSbM0ZWaiO4g5tN8ep4FZeEvYPL6rMpxpyb1UatXsepbg8BOD-MPuSmlBt5gGkVvR_tU3FRvZhVW7CsmC1b1FmngkVRnlPRdhZ0iU95_XzCIFcXHrbmQxSPAXmHDpFDQsGsywpB5O_h2BZTuNeJkpUUDBoXBvVodBkKIRJ7vlmEqmGzddmgvo9iEwv3aS-FE5W14JhzVBH1BYZCW3mijD4knc-P51-1WDNMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=QAOXseHlMAEUW-a2bVolygGootepUYDvqEkHbRbcZaorzhQ3yiTcs4erFvWWmhbSBYxsrlVUkUZQ1dRZBneB7nAmkciN3tyj8ijUHdM6kduT3rQ-qDbMowKli3E4mmkvksKFPoitLSga41DqFcQRkeOmLPcXQ7pj7kiUcvGVfM8wrILrjDGAcQ-MS_tLnxKXB9CMLqaUdZBRw955blcH3t-JG-cWHQJ01T-6MpfMrosMAmEv5SoAzCwt4iIblok0ZY1Yc8LKpDQVNdG6uMeKhC1GuhiZXJNN4Xky86Cixxk8J10PGHOBvX4VBFN6a7Y_GOwTWZLMsRVPkXS1-LRD4KaMEABzgejOe-VhnBVsiA6M9vJPTQsu_ni0H1DdOpZ6fzVURscAKU8lSXkkWJ7_9GnuVn3lxR0NjOcRjrHcwAz3a9_10-7UHb5XDHpVfzCR4l_hf9CxSbM0ZWaiO4g5tN8ep4FZeEvYPL6rMpxpyb1UatXsepbg8BOD-MPuSmlBt5gGkVvR_tU3FRvZhVW7CsmC1b1FmngkVRnlPRdhZ0iU95_XzCIFcXHrbmQxSPAXmHDpFDQsGsywpB5O_h2BZTuNeJkpUUDBoXBvVodBkKIRJ7vlmEqmGzddmgvo9iEwv3aS-FE5W14JhzVBH1BYZCW3mijD4knc-P51-1WDNMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : خاورمیانه دیگه اون خاورمیانه‌ی قدیم نیست، ایران هم تاحدودی هنوز قویه و ما دیدیم که تو درگیری‌های خلیج فارس چطور میجنگه.
ولی بنظرت چرا اونا تو یک ماه گذشته به ما حمله نکردن؟ چون میدونن که ما قوی‌تر جوابشونو میدیم.
الان یه محور شیعه‌ی تندرو هست و یه محور تندروی سُنی هم داره شکل میگیره، ولی ما با کشورهای مسلمانی متحد میشیم که اینارو قبول ندارن.
درحال حاضر اکثر ایرانی‌ها، به اسرائیل احترام میذارن.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20421" target="_blank">📅 20:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20420">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال ۱۲ اسرائیل: نتانیاهو در حال برگزاری یک جلسه امنیتی با حضور وزیر جنگ و رئیس ستاد مشترک نیروهای مسلح است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20420" target="_blank">📅 20:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20419">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=n5xi_U12Yq2SD9vRaR431HcDc-1GNlM1jhLN4pf78IIrN6F2UEb-0uCIS5NElNw-ZBof4G2d2paJq-8PXlXNqlKmLBDIZsRjWs23AS1gI18Df6nbMa3IMVQU1A4iUfltJBtxJVhUzewdrpFjoUqsVCACB0DW-GMzBDIQZY0HOTZu4ECBH2POIuAlw05vWB2y9mKwHKAk0XZ5CkvDJbX1gUz6Pj3AvVKKopA4qHXcC2mflYFRnUnZMBBePAOFmXHyPdpVlHz5aj16Ba-3t9inADoDDa44wmgcHkTnSLrOxyCSGOWFGy3HCDdbf1YVLyEnG6Lv20duv1yfbYB-YunO3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=n5xi_U12Yq2SD9vRaR431HcDc-1GNlM1jhLN4pf78IIrN6F2UEb-0uCIS5NElNw-ZBof4G2d2paJq-8PXlXNqlKmLBDIZsRjWs23AS1gI18Df6nbMa3IMVQU1A4iUfltJBtxJVhUzewdrpFjoUqsVCACB0DW-GMzBDIQZY0HOTZu4ECBH2POIuAlw05vWB2y9mKwHKAk0XZ5CkvDJbX1gUz6Pj3AvVKKopA4qHXcC2mflYFRnUnZMBBePAOFmXHyPdpVlHz5aj16Ba-3t9inADoDDa44wmgcHkTnSLrOxyCSGOWFGy3HCDdbf1YVLyEnG6Lv20duv1yfbYB-YunO3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی همچنان به اجرای دقیق محاصره اقتصادی ایران ادامه می‌دهند. تا تاریخ ۳ آگوست، سنتکام ۴۴ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20419" target="_blank">📅 20:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20418">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDUMtfLwjwmRyBx_X6XM1i4J-a-n-x6e5ZdfMVLkawXUF3xjdj8a9fm0MSuPjgtRtBuiLx--mnKCYTR14iX_uYvZjsYnAHJC1mgXKlv4PBcPyIVD9x3W-IcSDlC5GD2gXs9H9C1yPOWUdhoINmhORl7cBU5gpsitoZ0_t9t-duBfp7shZRLXqknIiPH3_nlI0yYQ0EnRIPf5eHHQ-CN43bHrdQtpORbB4mf6c5wczZ153eMGd4nNo8lQ4wO75GQuvssgcJVA28IBlNAPwEpcICXfNa2XFg4N5F-sQa1aODulgRj-ssmubkFgG8DUgeBbDk1WlNluJ1rHZ9SbB0itTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک چترباز ارتش ایالات متحده در حین اعزام به خاورمیانه، آموزش سلاح‌های سبک را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20418" target="_blank">📅 20:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20417">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مارک لوین :
من از اسرائیل حمایت می‌کنم
من از اوکراین حمایت می‌کنم
من از تایوان حمایت می‌کنم
من از مردم ایران حمایت می‌کنم
@WarRolm</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20417" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20416">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبرگزاری سی بی ای : مقامی آمریکایی اعلام کرد علی رغم ادعاهای ترامپ هیچگونه برنامه ریزی برای مذاکره با مقامات ایرانی وجود نداره
تماس ها صرفا از طریق واسطه ها جریان داره
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20416" target="_blank">📅 20:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20415">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20415" target="_blank">📅 20:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20414">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=SIOX3Yc_L_FOAVAzxygI46-NYb167NcSuF5PKnsxhsKOiwiTjL0x3V5d41ihXZRRusuqWjZh0ZDHkG4jUcpnXXVzMfqPvYGW2UR1zvg-h1W70FfxPnk0I7GJf6rJvPcAG0aKC08M_XhCSnYR-rlAzD8qCnk0qUyfXkvNuMkUziEQWGqHNpU10aBW1fzrIIaXJsZI6CajbP0g3uZ7epsP_5gy7fS_22DZIPXc42xvzeiyEj_camw3wlHipt3JCBEpZpEZO1GAX4iOL6SEpksi-fiiJyPmvBfgSXEg_XlxXEgI0T9SOtsdWBd8aS5TIKJITKDm4t2uKcXw3tMW1Keh-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=SIOX3Yc_L_FOAVAzxygI46-NYb167NcSuF5PKnsxhsKOiwiTjL0x3V5d41ihXZRRusuqWjZh0ZDHkG4jUcpnXXVzMfqPvYGW2UR1zvg-h1W70FfxPnk0I7GJf6rJvPcAG0aKC08M_XhCSnYR-rlAzD8qCnk0qUyfXkvNuMkUziEQWGqHNpU10aBW1fzrIIaXJsZI6CajbP0g3uZ7epsP_5gy7fS_22DZIPXc42xvzeiyEj_camw3wlHipt3JCBEpZpEZO1GAX4iOL6SEpksi-fiiJyPmvBfgSXEg_XlxXEgI0T9SOtsdWBd8aS5TIKJITKDm4t2uKcXw3tMW1Keh-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20414" target="_blank">📅 20:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WugiyP8IoEdIcOaz3jn6e85qYpvbMGsQApOu-crlDh-Vu-w4j9MKWBvHn32pvNG2yiZ-sZfnfHaIOllSO58eUZF68Z6qVvObhoePvuip-aqYLyvJWhWv6bovIxNbv7N54lX08Ql_Ivaij1D-_pRedX_r3wRAxhpCadLEOH1Sa8-iwqbndSx6K2exa8x9XDBtFoA322rnjiR0kThYsVmymm2-NtUNSKHW3Vs8WMUiC9FLZxB3xAeV7D1Kv-2jqZLMK5OtxClvhNwGPw3KFLsaKT8Jaee5o44dNklchDXCgU7ERzW-iWPwHSJ0wYxYZgmLtmEQuARnEvs7z7hkrp0ATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
رهبری ایران به شکلی باورنکردنی دورو و فریبکار است!
آن‌ها درخواست برگزاری جلسه می‌کنند؛ بعضی‌ها حتی می‌گویند «التماس» می‌کنند. گفت‌وگوها آغاز می‌شود و قرار است در آیندهٔ بسیار نزدیک جلسات بیشتری هم برگزار شود، اما هم‌زمان آشکارا و با افتخار ادعا می‌کنند که هیچ مذاکره‌ای در جریان نیست، هیچ موضوعی در حال بررسی نیست و فقط با «عمان» در ارتباط هستند.
@WarRoom
بعد هم طبق معمول شروع به رجزخوانی می‌کنند و می‌گویند تنگه هرمز را با قدرت در اختیار و مدیریت خود دارند؛ در حالی که این تنگه هم‌اکنون به‌طور کامل تحت کنترل نیروی دریایی ایالات متحده و «محاصره دریایی» ما قرار دارد؛ چیزی که برخی از آن با عنوان
«دیوار فولادین ایالات متحده»
یاد می‌کنند.
هیچ چیز بدون اینکه ما بخواهیم وارد ایران نمی‌شود و هیچ چیز هم وارد نخواهد شد، مگر اینکه یا
توافقی
حاصل شود یا
تسلیم کامل
صورت بگیرد.
چه ایران بخواهد این واقعیت را بپذیرد یا نه، ما در حال مذاکره برای یافتن راه‌حلی برای مشکلی هستیم که خود این کشور طی دهه‌ها به وجود آورده است.
موضوع بسیار ساده است:
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20413" target="_blank">📅 20:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20412">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک منبع ایرانی گفت که تهران پیشنهاد اخیر ایالات متحده را رد کرد و تأکید کرد که تنگه هرمز تا پایان جنگ به طور کامل بازگشایی نخواهد شد.
این منبع همچنین ادعا کرد که واشنگتن بسته شدن مسیر کشتیرانی جنوبی را پذیرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20412" target="_blank">📅 16:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20411">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20411" target="_blank">📅 16:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20410">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">لحظه نشستنش رو استورررری کردم
instagram.com/yashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20410" target="_blank">📅 16:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20409">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c929d388fd.mp4?token=glWiCH41FeUWUuzcx4mZKw0hcaJC1KaNd38VBUbC77ahFfExreVGfU3WTMfcMNCdijWpTM1SOG7cqB1F43EqYnKIwpxO3Sg52uGFjekKL8sCNwjpRJWtvfo3V9J5cI0eJqBYi7v12Kti5k_YqrI6NBIgZju87E3eikda3SJO9gINXuQMG17WifF-KffHQ-CoDrCY-AzmuOkWGHhhIY4DckW9bBOzhZ8Y6yCqwC5akVPf0p71jPyOFJdNk08_hEr2ISbIJtDdKPHcxM4z_cWr4MARzj0hCTNmBtotNrNsYM56lFL02nX022R_u4NOGup4nsInagsf7fAsfymi9lFEFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c929d388fd.mp4?token=glWiCH41FeUWUuzcx4mZKw0hcaJC1KaNd38VBUbC77ahFfExreVGfU3WTMfcMNCdijWpTM1SOG7cqB1F43EqYnKIwpxO3Sg52uGFjekKL8sCNwjpRJWtvfo3V9J5cI0eJqBYi7v12Kti5k_YqrI6NBIgZju87E3eikda3SJO9gINXuQMG17WifF-KffHQ-CoDrCY-AzmuOkWGHhhIY4DckW9bBOzhZ8Y6yCqwC5akVPf0p71jPyOFJdNk08_hEr2ISbIJtDdKPHcxM4z_cWr4MARzj0hCTNmBtotNrNsYM56lFL02nX022R_u4NOGup4nsInagsf7fAsfymi9lFEFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20409" target="_blank">📅 16:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20408">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اتاق جنگ بایاشار ، رو سفید تاریخ : ویدئوی اتاق جنگ مربوط به ۴ روز قبل از شروع جنگ ۴۰ روزه(۵اسفند)، هواپیمای ریوت جوینت از همین مبدایی که امروز پرید، یعنی میلدنهال انگلستان، و به همین مبدأ که امروز میرود یعنی جزیره خانیا در یونان، پرواز کرده بود و من به شما گفته بودم
🙌🏾
@WarRoom
I TOLD YOU
🫵</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20408" target="_blank">📅 16:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20407">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صدای ری اکشن هاااااا نمیادددددد</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20407" target="_blank">📅 16:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20406">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیج اینستاگرام رو باز پروندن ! و بازم برگردوندم !
😂
پیج دوم رو داشته باشید حتما
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20406" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20404">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1c503433.mp4?token=RBhUS1kvpINVoA_Jis_FAMen28wc1zowh8HjDi8h8r0lu3_jgaN2P_LXXfj-HKhmrV7_OCmF1m-9J3jgUYuslUT1p9LqJZQyslwpM5dIjxa9AHFhne-fse0aAaS3JQBrOOwV7azKTsVrA-b2IOZ0zV_zQXzh0kabme2aUQm5MboIUwa03_Ip1P5lr3V4iyuhSNaT_uohJdOxHWYyi73qod7yGHdLZQassWgvMDSeaQizTFxY0dPynnhVxyVVM4wJx4MF9fdg90lNv9YZL7Lof05CboUUEjkVcl5lP4nPWnlgtKdg4JH32RxBInV5ucbWel5pEqbA_0bCW9NSyE95ojdyt882tTNwk9cQZ2B0tYDZFfW1dtUfNamxb0PUnAehzPZNgxY9qsKHB7GuV0tef-ByNaQcCNdStYyjG3PTBkiCC4KcYOYc5THCVwo5OPqdbbDD11-IbYEobkufMCLipdLcvmZACcqIyAR_M65x50j9uijjkGj17NvpuxkCFHUxSkeOKlK7C_HrGwK_fR8amdLnrN_dYVl1GC8SZijeZ_iL3I2YDPlRZVF3KraZzlOv-Q460v7xAhltlpa3raHJwa_YCS2oKS6ea1cRJELaCWQD0JS6kHQhEysG3_ri-RrX2skLvPbV5nlpYgyXR93qKt48aDXbIttcG3lT3fPpAyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1c503433.mp4?token=RBhUS1kvpINVoA_Jis_FAMen28wc1zowh8HjDi8h8r0lu3_jgaN2P_LXXfj-HKhmrV7_OCmF1m-9J3jgUYuslUT1p9LqJZQyslwpM5dIjxa9AHFhne-fse0aAaS3JQBrOOwV7azKTsVrA-b2IOZ0zV_zQXzh0kabme2aUQm5MboIUwa03_Ip1P5lr3V4iyuhSNaT_uohJdOxHWYyi73qod7yGHdLZQassWgvMDSeaQizTFxY0dPynnhVxyVVM4wJx4MF9fdg90lNv9YZL7Lof05CboUUEjkVcl5lP4nPWnlgtKdg4JH32RxBInV5ucbWel5pEqbA_0bCW9NSyE95ojdyt882tTNwk9cQZ2B0tYDZFfW1dtUfNamxb0PUnAehzPZNgxY9qsKHB7GuV0tef-ByNaQcCNdStYyjG3PTBkiCC4KcYOYc5THCVwo5OPqdbbDD11-IbYEobkufMCLipdLcvmZACcqIyAR_M65x50j9uijjkGj17NvpuxkCFHUxSkeOKlK7C_HrGwK_fR8amdLnrN_dYVl1GC8SZijeZ_iL3I2YDPlRZVF3KraZzlOv-Q460v7xAhltlpa3raHJwa_YCS2oKS6ea1cRJELaCWQD0JS6kHQhEysG3_ri-RrX2skLvPbV5nlpYgyXR93qKt48aDXbIttcG3lT3fPpAyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خودش بمبی نمیندازه ولی همه بمب ها پشت سرش می آیند !
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20404" target="_blank">📅 14:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20403">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتاق جنگ با یاشار:جیمز باند.
قدرتمندترین هواپیمای جاسوسی تاریخ، ریوت جوینت، در حال ورود به منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20403" target="_blank">📅 14:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20402">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20402" target="_blank">📅 14:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20401">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e4766f60.mp4?token=dyPpCapPkBA1NGx_fb3OQ1qMqCV6vH35bm8KUEZ_i6jP15ES7i82Cj7kd6INj7Nbn2nYBJ6IscQBKc-Iigvk8K-sKw21F3U8ieWEbMj8IBrL2ye6pdNO-97q7ksESVO79jhWT0t6kxul_UamBYGYKiAYWgTn8YostfZqWppeRncdGS66bkOLGR7KQPv2Vxoxtc7E0_aQWy3uWUKvaXo2J0tgVD8QuWIDri2yCZVMauTMzt7PBT30tCoxMMJynkCmp7v47MEEq0eSi6FqFb8pRstUUKtCfNp8yXdH8srD7RXI521DlUgkO9kad8krXVCPHeM4_76zcKzWJeofSQ817w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e4766f60.mp4?token=dyPpCapPkBA1NGx_fb3OQ1qMqCV6vH35bm8KUEZ_i6jP15ES7i82Cj7kd6INj7Nbn2nYBJ6IscQBKc-Iigvk8K-sKw21F3U8ieWEbMj8IBrL2ye6pdNO-97q7ksESVO79jhWT0t6kxul_UamBYGYKiAYWgTn8YostfZqWppeRncdGS66bkOLGR7KQPv2Vxoxtc7E0_aQWy3uWUKvaXo2J0tgVD8QuWIDri2yCZVMauTMzt7PBT30tCoxMMJynkCmp7v47MEEq0eSi6FqFb8pRstUUKtCfNp8yXdH8srD7RXI521DlUgkO9kad8krXVCPHeM4_76zcKzWJeofSQ817w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده دود بزرگ و غلیظ از سمت ساوه دید از قم
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20401" target="_blank">📅 13:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20400">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رسانه های رژیم : یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه بر فراز آسمان تنگه هرمز رهگیری و مورد اصابت قرار گرفت.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20400" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20399">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بقایی: ‌در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد @WarRoom عراقچی هم امروز به کربلا میره و مملکت تعطیله</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20399" target="_blank">📅 11:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20398">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بقایی: ‌در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد
@WarRoom
عراقچی هم امروز به کربلا میره و مملکت تعطیله</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20398" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20397">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aaf651e2d.mp4?token=AbcyDXLi2woTx5Y3c8s3NdN7kjGiI77W0CTlF9PpLDsfOoyyclFjo8I6HuPqk2xv7qdmj4goKlVYtc_ZonBb8bbfa1pvBDM1VGBzN2eFU0_rOhkuN8jcR3Wt7VH36KZ5u6xLBkuK1yx-RY88zYo-uoF1AJUEW-cYm_gpmCELnwksqbtt1sg0GfhoTBZ3IxHW5Yye3_h_4lp-jirD-TWG371hRHSSnoz5_QYo1c_TqKMMBURCLT-vni8A7e4h_DQxvLtU-N-G7aV109nar7xXikwHNOkXy16vm-5yx1I26ljIP68iinNhQSD0bgV7QsvMcXsxyhIsHB7UX9mrdc6vJbqrtWx3dPFcSGfJLn31QtB9TQ21dAeO54sTGCNYv62rAytNBe7etkjilOVjylOqjunJAYGgOgXHyrz0LCSGBfJbVYHILipEmlHELxSSZ0XbydQUjnzLLYoiV_XrjLI0fgLa0QZ8AqHqfjM4zx96YAe2YluE0MeEgfwX1dmfsdzwL7FViwSm1zCoa83ZuUAKtNxKfcPSefqpiaYJYm6OEyIqp3dolMDh4qmB-K9EHOrdtXLPuGFk8B-mvB6YCHwd3BoYmZKgJ8KIg7eKD_nN7yX4Pa4UmzSSEUYGbCMgEmc6_Meds_5aAIwuLweVLIUp-cDfP1iz4wBQDuVgap6U6gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aaf651e2d.mp4?token=AbcyDXLi2woTx5Y3c8s3NdN7kjGiI77W0CTlF9PpLDsfOoyyclFjo8I6HuPqk2xv7qdmj4goKlVYtc_ZonBb8bbfa1pvBDM1VGBzN2eFU0_rOhkuN8jcR3Wt7VH36KZ5u6xLBkuK1yx-RY88zYo-uoF1AJUEW-cYm_gpmCELnwksqbtt1sg0GfhoTBZ3IxHW5Yye3_h_4lp-jirD-TWG371hRHSSnoz5_QYo1c_TqKMMBURCLT-vni8A7e4h_DQxvLtU-N-G7aV109nar7xXikwHNOkXy16vm-5yx1I26ljIP68iinNhQSD0bgV7QsvMcXsxyhIsHB7UX9mrdc6vJbqrtWx3dPFcSGfJLn31QtB9TQ21dAeO54sTGCNYv62rAytNBe7etkjilOVjylOqjunJAYGgOgXHyrz0LCSGBfJbVYHILipEmlHELxSSZ0XbydQUjnzLLYoiV_XrjLI0fgLa0QZ8AqHqfjM4zx96YAe2YluE0MeEgfwX1dmfsdzwL7FViwSm1zCoa83ZuUAKtNxKfcPSefqpiaYJYm6OEyIqp3dolMDh4qmB-K9EHOrdtXLPuGFk8B-mvB6YCHwd3BoYmZKgJ8KIg7eKD_nN7yX4Pa4UmzSSEUYGbCMgEmc6_Meds_5aAIwuLweVLIUp-cDfP1iz4wBQDuVgap6U6gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سناتور ریک اسکات: بعید می‌دانم مذاکرات با رژیم جمهوری اسلامی به نتیجه برسد
‏ریک اسکات، سناتور جمهوری‌خواه آمریکا، در گفت‌وگو با فاکس نیوز اظهار داشت که تصور نمی‌کند دور جدید مذاکرات با رژیم تروریستی جمهوری اسلامی به نتیجه برسد و معتقد است ایالات متحده در نهایت بار دیگر به حملات علیه این رژیم بازخواهد گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20397" target="_blank">📅 10:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20396">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی : ‏نیویورک پست با دو تن از رهبران میدانی انقلاب ملی شیر و‌ خورشید در داخل ایران گفت‌وگو کرده است، افرادی که با به خطر انداختن جان خود، تنها یک پیام برای جهان دارند:
‏«ما در حال آماده شدن هستیم. از خیزش دی‌ماه درس گرفتیم و مصمم‌ هستیم کاری را که آغاز کرده‌ایم، به پایان برسانیم.»
‏«ما به‌خوبی می‌دانیم با چه خطرهایی روبه‌رو هستیم، یا این رژیم می‌رود، یا ما.»
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20396" target="_blank">📅 10:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20395">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری میزان اعلام کرد که صبح امروز حکم امید بهزاد و پوریا صفوت، زندانی‌های سیاسی اجرا شد
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20395" target="_blank">📅 10:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20394">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مقام ارشد آمریکایی : هنوز به توافقی با حاکمان ایران دست نیافته‌ایم، اما تلاش‌های میانجی‌گری همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20394" target="_blank">📅 10:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20393">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">بوست کم شده داریم لول میایم پایین یه کمک کنیدد بریم بالا استیکر شاه برگرده به دوستاتون که پرکیوم دارن هم بگین
https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20393" target="_blank">📅 04:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20392">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6507572.mp4?token=SsJ4NrdtWt02u1cImlGLhAjvr8LVjnKqF2A2RgNcMdLTPf7KuRE8Zx7wg73eF2BocDam3m2KQ-ByVcan2rF2zDR3KWxpCf0OOz3hzi-BiAn7lB6NGBZRQLZ42BnL52wLohSk6qu_16OzhhXc6-grDV-yAg3cB2BRtY18KAhO-jlHezOg4RLprpzM0tGAa5nfFiTnLoNxggWN-yB1xxqLQZXjsVKyDa6IElYlSc9O7j4KU-OHW3lwpd-FD0bt6Q4OaeQ_b8fviSb050nVNZO3sGOG4j5eYYS3vmn4FfYkOjE7JK2Az1RPQHdq7-GOcOGv3GgaBxxwuhaKtqJ8HbMYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6507572.mp4?token=SsJ4NrdtWt02u1cImlGLhAjvr8LVjnKqF2A2RgNcMdLTPf7KuRE8Zx7wg73eF2BocDam3m2KQ-ByVcan2rF2zDR3KWxpCf0OOz3hzi-BiAn7lB6NGBZRQLZ42BnL52wLohSk6qu_16OzhhXc6-grDV-yAg3cB2BRtY18KAhO-jlHezOg4RLprpzM0tGAa5nfFiTnLoNxggWN-yB1xxqLQZXjsVKyDa6IElYlSc9O7j4KU-OHW3lwpd-FD0bt6Q4OaeQ_b8fviSb050nVNZO3sGOG4j5eYYS3vmn4FfYkOjE7JK2Az1RPQHdq7-GOcOGv3GgaBxxwuhaKtqJ8HbMYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو مارک لوین به ترامپ برای حمله به ایران پیشنهاد میده:
۱. تداوم توقیف دارایی‌های متعلق به ایران
۲. ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
۳. هدف‌گیری مستمر فرماندهان نظامی
۴. حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
۵. هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
۶. حمله به بانک‌ها و مراکز مالی
۷. دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20392" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20391">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عمویم پیت هگست
:
وزارت دفاع آمریکا آماده اجرای عملیات بود و همچنان نیز آماده است؛ در سطحی از آمادگی که از زمان جنگ جهانی دوم تاکنون نظیر آن را ندیده‌ایم. ما کاملاً آماده‌ایم و هر زمان لازم باشد، عملیات را آغاز خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20391" target="_blank">📅 03:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20390">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رویترز: زمین لرزه‌ای به بزرگی ۵.۴ ریشتر قاهره پایتخت مصر را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20390" target="_blank">📅 03:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20389">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20389" target="_blank">📅 03:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20388">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea3yBFbem9xmRw60FfLzj2w4eOC1n1SuJ7nGKSxLZJYvLnOnq0b2XXU7G7qnWnCqwrf5nNu0gzVo-PyiFFfe1seu1gRcrU35XX88E8hMT_rImBTI7B8_5SIoGXZPyFYam82HSdI4ucnyIUo3s0biTp3ukSgsu_37ElottED91YjPoi6DKZHRYubZCoOWEOMnptutUu29rsBs2YC2W1f-lTE4oSN9w6DNd7_-50Q_nLnc1LqbwiHNePToDb8ukx4yaFl6cdqY8lwoUbAEvDXRUjH50n9E6AJi9P71fHTyUqUKLA-8j0vGMEEjPyxDU9nVr0pm3UtPX0ssRPhro-p_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۸۴$
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20388" target="_blank">📅 02:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20387">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ دم توالت: در حال صحبت با ایرانیم و قراره از فردا بعدازظهر گفت‌وگوهای اصلی شروع بشه. امیدواریم این مذاکرات بتونه جلوی کشته شدن آدم‌های بیشتری رو بگیره @WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20387" target="_blank">📅 02:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20386">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فعالیت‌های نظامی قابل توجهی از سوی آمریکا در عربستان سعودی و خلیج فارس مشاهده می‌شود، به طوری که یک پهپاد شیلد ای آی V-BAT در حال پرواز بر فراز تنگه هرمز و یک هواپیمای E-3G Sentry بر فراز عربستان سعودی است. @WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20386" target="_blank">📅 02:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20385">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyJUtkwJ6hAwF1dgTkJskhUHqAIngtE6FRFDB9O3D4kOIyqSOB9BkrLCRLIlL000rJr-zdZwSTcY9yyK-IrUANWzzHio-_PM7Jhh5LsZCGtVz3xnAISjG_zO_1uedBgRjiwjKvpqoCGJsx-igJ_zcO0r9IPkvsAaaVcqPCYbWCWlAeYP-zqaCbRwaQeAhdDTT8k6xjQzJlXA3lyA9JW1WzVYunHskYZ1AQ7rY6buTVvZneAPRq2fqoAseRKvG8VmHm3WLE6QmqKCAnXdFSIRXRonWZmBET4bA3p37pnXuecEL6BUQQUlR2VQrAGXy4p6iWYpTLckHThPt7N0PdnZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس  https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==  کارای اداری و اد استوری رو انجام بدید کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20385" target="_blank">📅 02:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پس از آنکه ترامپ تنش‌ها با ایران را کاهش داد و احتمال توافق پدیدار شد، قیمت نفت بیش از ۶ درصد کاهش یافت همکنون به
۸۶$ رسید
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20384" target="_blank">📅 02:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28b4a7f0f.mp4?token=sH_itNOIwii8f8VHHHS1eMbPnVqN5jdbqedILMFBvSB3_k4EoLVMvvl5m5Cn7QedHvFmeOQGrUhzNGS6ViOmOIhqesbyjL0YdOvMHrLx8xvukbodQUBu7I18KHpTef8irHnVv3Lzvnwblxwe6L8fjaYDI3EEOmF6lpa0Uf5WPqyRI2K9EoMbJ-Jz0_PjM2ug60UQs43utDV8rDlWbl6pumXLbiYDXF_2OZ2WQTRndmiWdb7S1TXOsDB_SrvrQb9uvlqylnoR1AtbsT7KFF8pIvyPM3uzikChsZegywqYvCgCDJuscJUh-KIRHg3nxHBKU3CN5YuRhNGKJVThZbqqx5K8S7qy-JGbPJwi1wkGyaEKxH5Tsq-UpSW37PVyt9dx37a95CY8Pjh0VaMca7hUAh10LElgrpcHmMrulfktORCKW-1n-PQQM8cTtFPYVyocRrpyFhjNnYxXjuO2s0mLUGwd1e5bsnm1kQ1rpPnsdDqieIp4DTVhT7H30BuNDHfcjcqNwPIdFBwaa7ytcp_bHYwmo9-EEdFdFBxd4RzGsD_CnNbxOguZlZ8-7KJqKs9BnaX1ii9mms3X53kjbV_Xl6_mNkRPD4KPSDPey_m5GXOx5Yn7HsgTzwV57JsU3Et6hv0kK18eKW8ucdFiy_uPFSdEQpeitPAcYfLS34plB9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28b4a7f0f.mp4?token=sH_itNOIwii8f8VHHHS1eMbPnVqN5jdbqedILMFBvSB3_k4EoLVMvvl5m5Cn7QedHvFmeOQGrUhzNGS6ViOmOIhqesbyjL0YdOvMHrLx8xvukbodQUBu7I18KHpTef8irHnVv3Lzvnwblxwe6L8fjaYDI3EEOmF6lpa0Uf5WPqyRI2K9EoMbJ-Jz0_PjM2ug60UQs43utDV8rDlWbl6pumXLbiYDXF_2OZ2WQTRndmiWdb7S1TXOsDB_SrvrQb9uvlqylnoR1AtbsT7KFF8pIvyPM3uzikChsZegywqYvCgCDJuscJUh-KIRHg3nxHBKU3CN5YuRhNGKJVThZbqqx5K8S7qy-JGbPJwi1wkGyaEKxH5Tsq-UpSW37PVyt9dx37a95CY8Pjh0VaMca7hUAh10LElgrpcHmMrulfktORCKW-1n-PQQM8cTtFPYVyocRrpyFhjNnYxXjuO2s0mLUGwd1e5bsnm1kQ1rpPnsdDqieIp4DTVhT7H30BuNDHfcjcqNwPIdFBwaa7ytcp_bHYwmo9-EEdFdFBxd4RzGsD_CnNbxOguZlZ8-7KJqKs9BnaX1ii9mms3X53kjbV_Xl6_mNkRPD4KPSDPey_m5GXOx5Yn7HsgTzwV57JsU3Et6hv0kK18eKW8ucdFiy_uPFSdEQpeitPAcYfLS34plB9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من واقعاً دوست دارم این مسیر نتیجه بدهد؛ چون جان افراد زیادی را نجات می‌دهد و از ویرانی و نابودی گسترده جلوگیری می‌کند. صادقانه بگویم، اگر آن اتفاق می‌افتاد، سال‌های بسیار طولانی طول می‌کشید تا بتوانند خسارت‌ها را جبران کنند؛ اگر اصلاً امکان بازسازی وجود داشته باشد. حتی فکر نمی‌کنم بتوانند دوباره آن را بسازند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20383" target="_blank">📅 02:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صدای انفجار جدید همین الان در تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20382" target="_blank">📅 01:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnJ1RwpgIQhyv_Z90gTpOULjP-xKWxkaEhElaK9YSFcEKfEsEkvCeUHQNsR-i6cM86HM92knGglGz0BtHmb4vxm0IIjk8xn4SRIQJMsHKJxVob3y9rKPD0S8vKX71J8W4jF3Cp6bBn1MxyhneY2tr8J3c2t0g780cqXu2yl-9O3gZRCZ1g-JoP_Ob9S6oUWkNogm2YOYb42vCShsVlSO3xBtTQukvQaHFAAamZDIsbYWRUFPxFhwVVX7dauEejhb7zaVQhqEbL3FTi9W97i9Jp-zXlVgGg0k7XMD-9MO4cv013rxgBPNB-EwQmCxGq8J6HLKCiOw-o4abYVjPD-GxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا: گزارشی دریافت کردیم مبنی بر وقوع حادثه‌ای دریایی در فاصله 20 مایلی شمال شرقی شهر خصب در عمان. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20381" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سازمان دریایی بریتانیا: گزارشی دریافت کردیم مبنی بر وقوع حادثه‌ای دریایی در فاصله 20 مایلی شمال شرقی شهر خصب در عمان.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20380" target="_blank">📅 01:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ درباره ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست. آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20379" target="_blank">📅 01:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرنگار : شما نمی‌دانید این حملات به کجا منتهی می‌شود. منظورم این است که آیا همسایگان ایران با سیل جمعیتی که به کشورهایشان سرازیر می‌شوند، مواجه خواهند شد؟
ترامپ : یک فاجعه. اتفاقات بد زیادی ممکن است رخ دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20378" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
