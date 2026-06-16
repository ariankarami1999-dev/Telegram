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
<img src="https://cdn4.telesco.pe/file/WUabFCjN78Ahm67FF5ERSi94Hp-kuOWL2qJgFn6S09eAhwQtmLVpXwv8VVNn7SbmS2z2OjSHSrGY_TWOiSwOrwVIj2mAty9LVSQW1SzLFOK46OFmJfLNT5HXFI_doymEOy8b06FBBWlxXpROFoi3LNWaKjlP3ygwBt9mb2dPVyAuXUnZYjnNpHLi99qTHuU7xfiaFHaTuqSXTrMohumRZWVp0iONcB--aOB3KAnVbj6q5ae22grAk6cA3MhgSchiHOGNYGWmEzT74XTbTbLT2BG_mu_Ldk5af646g2a-sHSxoiNgUC7z54VxGuhcwEXBLkYbnTTfpfVvkrbLC5ZaiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 06:23:54</div>
<hr>

<div class="tg-post" id="msg-133643">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
دو توپ دو گل برای نیوزیلند ....آقای نعمتی سلطان سوتی   پ.ن دو توپ آورده دو گل زده نیوزیلند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 396 · <a href="https://t.me/SorkhTimes/133643" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133642">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
بریم برای نیمه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/SorkhTimes/133642" target="_blank">📅 05:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133641">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
هر چی دارن باید بزارن ..راحت میشه سه امتیاز این بازی و گرفت ...تیم سختی نیست نیوزیلند ..مهمترین 45 دقیقه ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/SorkhTimes/133641" target="_blank">📅 05:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133640">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
نیمه دوم قایدی و علیپور و حسین زاده میتونن کمکمون کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/133640" target="_blank">📅 05:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133639">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
راحت و با تمرکز بیشتر میشه سه امتیاز این بازی و قشنگ گرفت ..نیوزیلند تو دفاع خیلی ضعیفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/133639" target="_blank">📅 05:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133638">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
گل اول ایران به نیوزیلند توسط رامین رضاییان در دقیقه (32)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SorkhTimes/133638" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133637">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
نیمه اول یک بر یک تمام شد ‌تو بازی که یک گل زدیم ..یک گل آفساید و یک تیرک ..و عالی بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SorkhTimes/133637" target="_blank">📅 05:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133636">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
❗️
گل تساوی و خداروشکر زدیم ...این نیوزیلند و میشه برد ...در دفاع ضعف دارن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/133636" target="_blank">📅 05:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133635">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
همچنان توپ و زمین دست ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/133635" target="_blank">📅 05:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133634">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
ما داشتیم خوب بازی میکردیم که نیوزیلند گل اول و زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SorkhTimes/133634" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133633">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
بازی و خوب شروع کردیم .و سرحال نشون داده تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SorkhTimes/133633" target="_blank">📅 04:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133632">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
❤️
کم کم بریم برای بازی تیم ملی ایران در جام جهانی 2026....انشالله تیم کشورمون ببره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/133632" target="_blank">📅 04:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133631">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVHUiGAjSSJ8Sq5cxuAUsCht1cnateYc2WGiWbuk6DvGGlgY2YVGVNOmvCzGuVUacaPUHUD2ZxoCTNS2J96WavMjuFhgSaKIKJLG1HcAcA9DmAn-CEJ0j643h8Nh0rWiMacSTV8iJz0EMqglqaXvKkk-MarwomePwMmdR56psZN9z_bCVh8sevkIqrJe1ZqtJ161OdDTyWldO02BY0aFc0iXe8sQawZcAjbYug-EJ8Zi9o5MNACZ68xOzaCok9RKIAiJ22CO5rbfP6cxzpSQmgfiLVGvym8yjvtQ0rqEujF9Z53pzRzP80QpBMNE-a-vvUppyf1vvkzLpAR1Ptr-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هم اکنون ورزشگاه مملو از تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/133631" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133630">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🤍
📸
تصاویری از هواداران ایرانی روی سکوهای استادیوم سوفای برای حمایت از تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/133630" target="_blank">📅 04:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133629">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UINYGC2WAJgAgzMbcFZS-PLpn-dzG0F9UZRhc-bzhaJPWAwSm_OAf4SM5DUVvPkkmTxKleNhJ-Tph5H-F4wrqFD8T_vT6nyFBLoF-8q48avrlxpSIPTIrmFe1xdiDgtqmgVNJA7qg0QZA2zQoBXYK7HMWC9hzumi3zDI42J3ZIQ77HcbOud35XN2f12Aq3-0NPWM3e4NbhpbzcOVNRLQ9dAX9jbteuz8HBCZL-4I1O8AkFa_LD_AZVr_52x2TGQfK2OdHLRLL4PjYAONkaEtcEN7ju4qZVzaTzTBagniKtvEdvD6xw3VJ_coYaK4ouNZXnj1OhcQ-PNQov9yiHcy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤍
📸
تصاویری از هواداران ایرانی روی سکوهای استادیوم سوفای برای حمایت از تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/133629" target="_blank">📅 04:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133628">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
جو و حواشی امشب ورزشگاه شاید صداوسیما رو مجبور به سانسورهای شدید و یا حتی قطع تصویر بکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/133628" target="_blank">📅 04:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133627">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
تیم های آسیایی تا الان عالی بودن  اگه قلعه نویی نرینه به آمار شون
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/133627" target="_blank">📅 04:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133626">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
🔻
وزیر ورزش:
🔹
در جام جهانی پرچم غیررسمی بیاورند یا شعار بدهند، سرپرست تیم مسئولیت دارد که بازی را متوقف کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/133626" target="_blank">📅 03:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133625">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
حرکت اتوبوس تیم ملی به سمت ورزشگاه سوفای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/133625" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133624">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
حرکت اتوبوس تیم ملی به سمت ورزشگاه سوفای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/133624" target="_blank">📅 03:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133623">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgsunDqCDS0cYd0DC-xAt5I1LSdE5ZaB2GFLjeK7_fe6k8eLbHvfShqTq7CyjNZiHJbLJDJhrzAAOji00wT77eSMqEfJuS6Qc1unG02p47wZrW_CdrtCnnkS8iYAgUp48yesylKpgJxURrOw0umzNl0whytN2LMYX1aku5bi-vTeEQbLf4A32k-HJkaeiGgfvUEaG97QIJFurdjzu5VSG3N9aCSzJqBk3A0NqYJ2CX24EtwiRIL9iiZaait3f2l7iYPEpFU8gBt-J7npWpeoCcFKN_jVctcmp5MZmGCf7Tg0Is7T-FF9oHOATvxCnl261BCC8ujvuKLH65MyX-r5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
گرون‌ترین ورزشگاه جهان در تسخیر ایرانی‌ها
❌
این استادیوم 70 هزار نفریه که فقط 5 هزار بلیط از نیوزیلندی‌ها فروش رفته و 65 هزار ایرانی قراره امروز بازی رو از نزدیک ببینن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SorkhTimes/133623" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133622">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8709c9d008.mp4?token=jvaQ3CBY1sTHjvmQOGyXo4-gyVJGxJFYyTrbQOdezhBTk1fc8Iog7japuoU9ZtqIFCjsq3nt6Rh9osI0lol0I4oNKt9cG8CO24v5kjyQxVd6GyYasg0ZqVuDlujWFhsmwQQ-sp0BiooUvEDxuPNFcBYXy0wzEoje7nyrDREA1d1tk_01XNBy9H9D_MP3ULRnLGJJt7xjPSAwG2QmBhRt9tMpudw6EeE9akFP5519zij1UguaIQb6ONA7oiuuddcHP6rE6jYE3TgwyiUPLErPqAbAko2qVIt0xngMqGURzOAcoJsmLjjF7xwnasqTez5dxDgVw_H3Nz8jWwOqvg8uUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8709c9d008.mp4?token=jvaQ3CBY1sTHjvmQOGyXo4-gyVJGxJFYyTrbQOdezhBTk1fc8Iog7japuoU9ZtqIFCjsq3nt6Rh9osI0lol0I4oNKt9cG8CO24v5kjyQxVd6GyYasg0ZqVuDlujWFhsmwQQ-sp0BiooUvEDxuPNFcBYXy0wzEoje7nyrDREA1d1tk_01XNBy9H9D_MP3ULRnLGJJt7xjPSAwG2QmBhRt9tMpudw6EeE9akFP5519zij1UguaIQb6ONA7oiuuddcHP6rE6jYE3TgwyiUPLErPqAbAko2qVIt0xngMqGURzOAcoJsmLjjF7xwnasqTez5dxDgVw_H3Nz8jWwOqvg8uUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرکت اتوبوس تیم ملی به سمت ورزشگاه سوفای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/133622" target="_blank">📅 02:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133621">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
جو بیرون ورزشگاه سوفی آمریکا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SorkhTimes/133621" target="_blank">📅 02:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133620">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186dc9ec7b.mp4?token=eWTlXi1GoZY0T-jMWuqs3HX9mMpLBZDDtDEMv5IxYnOEL0WA-86f9t0bqclczDPagFkzL2s0mQtEtHdcJyCAUEZjoinBNjE4d_CKaX6H70vfteVE-KnTTfiEz-KabukLpks7W0QEmFer93H8EsvzfPL1gf28y5_QVro6Exofs5wGUQrjpJObetlA9CSCCwvk23-g_C1ReYkCkUKtUGIR8rWyMld8BKXBr9fPYkvguXzjm9tk1zK9vAeJd92FDqOx7KksHuep871hsZFrk1uY2apEEJvv9ISjj2t8UrbOTKBMT2psFIUOST7YLCrIqffnRj5uEjqkTpbicrZ3BTfmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186dc9ec7b.mp4?token=eWTlXi1GoZY0T-jMWuqs3HX9mMpLBZDDtDEMv5IxYnOEL0WA-86f9t0bqclczDPagFkzL2s0mQtEtHdcJyCAUEZjoinBNjE4d_CKaX6H70vfteVE-KnTTfiEz-KabukLpks7W0QEmFer93H8EsvzfPL1gf28y5_QVro6Exofs5wGUQrjpJObetlA9CSCCwvk23-g_C1ReYkCkUKtUGIR8rWyMld8BKXBr9fPYkvguXzjm9tk1zK9vAeJd92FDqOx7KksHuep871hsZFrk1uY2apEEJvv9ISjj2t8UrbOTKBMT2psFIUOST7YLCrIqffnRj5uEjqkTpbicrZ3BTfmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
جو بیرون ورزشگاه سوفی آمریکا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/133620" target="_blank">📅 02:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133619">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
جو و حواشی امشب ورزشگاه شاید صداوسیما رو مجبور به سانسورهای شدید و یا حتی قطع تصویر بکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SorkhTimes/133619" target="_blank">📅 02:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133618">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
ورزشگاه لس آنجلس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SorkhTimes/133618" target="_blank">📅 02:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133617">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
⏱
پایان نیمه اول
🇸🇦
عربستان ۱ - ۰ اروگوئه
🇺🇾
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SorkhTimes/133617" target="_blank">📅 02:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133616">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
هلند و ژاپن مساوی کردن
✅
تا اینجای کار تیمای آسیایی خوب بوده عملکردشون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SorkhTimes/133616" target="_blank">📅 02:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133615">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4hpdgK7ALaCyED5_Ph7WkVda9hNEgvC6_Shk76mujGOihwwAi6sqZAp1AZAjRO6M0uh0ZQspg3f1Oix1R5HsP18ib3mj8R-QMY7__j8sc07rTHXk2Xi0kV6c197JXRaPmqf05g_6j5AA_ZMizKGrqAgkVCL9KyBdGIjsAgrX0220xkMQQZMPvvRE214N938QagPwUjllXVgb9ANBfJCAsSYnEhy97DU4W0k32EsTmgVlzOF_HoF_IPU-VQiIEOncGM33zmmzOm6_O47lodykSwiP98sUCmFj_3wgVQcF4f-Tqc82HCYZTCVngkE62Pe_qCyulr-u0XeZHpp5PU1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام جهانی وینکوبت ادامه دارد!
⚪️
IRAN -
⚪️
NEW ZELAND
⚫️
جام‌جهانی گروه G
⏰
سه‌شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده ۱ تیر ماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SorkhTimes/133615" target="_blank">📅 02:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133614">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
محمد سیانکی گزارشگر صدا و سیما جمهوری اسلامی راهی آمریکا شده و قرار است هر سه بازی تیم ملی را در جام جهانی گزارش کند
🫥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/133614" target="_blank">📅 02:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133613">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbRgDANqVHqMQTYbBi1-HKEYISfQh_vudJO_4buAzlqecF1C7DHswKfFIEyQw2o3RitGcZHE37PNepyARDfsebhY1Z30tSnGTNvEgmSFhb-NH-r-_qlMIlEfC9ES5nVfgh1Urqs5JkOSZaZq_n3zc6gYUEi_KQ3C96uIUKSFKGjGqPtZZLkb6k9SYHQZnl_lp7hOm63Wqav4QVpsbonLO-uQO1kH3p4ac4e51Uk4MWqVNqv5etV9bV2MNLi7ztX9TYr47ERi9bQE7uS-1D48BsU2bnogF57F1flq5CeqLi89SIdVAT7QjOvLGr4uT1D7FErUyUcuCL_K41QR5BaZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ورزشگاه لس آنجلس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SorkhTimes/133613" target="_blank">📅 02:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133612">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
جام جهانی| کیپ‌ورد نخستین شگفتی جام جهانی ٢٠٢۶ را رقم زد؛ ماتادورها پشت سد کیپ‌ورد؛ لقمه‌ای که از گلوی اسپانیا پایین نرفت
❗️
اسپانیا صفر - کیپ‌ورد صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/133612" target="_blank">📅 01:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133611">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
فوری و رسمی/هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/133611" target="_blank">📅 00:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133610">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
جام جهانی 2026؛ تساوی رقبای ایران در گام نخست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/133610" target="_blank">📅 00:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133609">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmfo2qcf_I_9E1z48dME6MyaSEYcOX2egTPoe20BJC77z2xu0r03pw0if_unO48HBKLT7HSIUlc-XDHHtTgejQ3lviTNYEDLmFRwUx9dalbEIoK_63PqxMkp8mHzNf-Jp4eKjIg9iA6xXNbA8UcG-xQKRBqH7s_lbr5sblMEzpLb8lqFYSWawMSE15CCUDMhaJGstmVaWDwjwGD8b3f62tHcjzkqBSeBWdpK5ZsGAv5iYkHsDOJ0xcfC66pIHkk_9lcJPkTNFVE6mGOMtpaxi5TqY_aoBzX9Ps8CD3EuNLK34bmoOOj49DWBXUPE7CmFY8znj9RGiJD3tBBgCyFuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی 2026؛ تساوی رقبای ایران در گام نخست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/133609" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133608">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb4BWE_ZYdeVGa1a953kmYyaN9FwtFVZesoTb4bKPnWPN-BTYHFBvvnBGxbLZ2CClD4XkHNS1iD3ieB_CdWpSy3_QEMmXinn_bfwsGNM1bAR8L-XVrfzfCiMM5ovn22vZWv_yqoqh0-hEpaSaJjwCBVCJUzfSAxOEZkrsBBuQz0xzoLm2Q0RPzDeckfiCCovCEvfZ_FV2RFGupIMQMdSspANu1NZuFQCauVRs1QFd8nO7Qf_ntcAuqBnSOpu2zeABqp8zuI1jrSfmZVcxYXfWr_ZB3kXXEAUr_L7wxIfgoUjI-qESivv8NXgDQfj2ODkTAmPMxN9ZomEAcJvDd1ImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رسانه RNZ نیوزیلند در گزارشی اعلام کرد تنها 5 هزار نیوزیلندی بلیط دیدار امشب این تیم مقابل ایران رو خریداری کردند و حدود 60 هزار صندلی دیگر استادیوم سوفی لس‌آنجلس در اختیار ایرانیان خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/133608" target="_blank">📅 23:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133607">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
🔻
وزیر ورزش:
🔹
در جام جهانی پرچم غیررسمی بیاورند یا شعار بدهند، سرپرست تیم مسئولیت دارد که بازی را متوقف کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/133607" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133606">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6241f18205.mp4?token=kH2q-SBZm_SKoBN1YorflReLN1F3g8r2StON00mpSAUlGIwBDXfmAh_62UESZ-mtw5jAriJ1A6Z2S6AzicvCagPrEvMQxtIgJLFHOCDRRfGkuEl64fGuFQW6xPm6pF7QTajNeISrbY3PeNuB3IvQKOvmourovfJtYpf5D8ShEmdPwjW5AXpVAsyxq_Mky0_Kr1xW5Ot8NbIbPlfclv6W9dxbKUbLn1QxV7GdNvvPW8gOzItwaHSZw6SVOJv3E7aRySdhChWwsur_m4ixSb8mfcNP6PhLp0vbJhHOgVbe8aRhi5imJynm9vD8a1LiGLLR3iHvqhyj2gKQTZawtjY3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6241f18205.mp4?token=kH2q-SBZm_SKoBN1YorflReLN1F3g8r2StON00mpSAUlGIwBDXfmAh_62UESZ-mtw5jAriJ1A6Z2S6AzicvCagPrEvMQxtIgJLFHOCDRRfGkuEl64fGuFQW6xPm6pF7QTajNeISrbY3PeNuB3IvQKOvmourovfJtYpf5D8ShEmdPwjW5AXpVAsyxq_Mky0_Kr1xW5Ot8NbIbPlfclv6W9dxbKUbLn1QxV7GdNvvPW8gOzItwaHSZw6SVOJv3E7aRySdhChWwsur_m4ixSb8mfcNP6PhLp0vbJhHOgVbe8aRhi5imJynm9vD8a1LiGLLR3iHvqhyj2gKQTZawtjY3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خداداد عزیزی : از طریق یکی از دوستان با پرسپولیس صحبت هایی شده، من اگه بسته بودم همینجا جلوی دوربین میگفتم بستم، هنوز قراردادی امضا نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/133606" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133605">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
خداداد عزیزی: با پرسپولیس صحبت کردم اما هنوز قراردادی بسته نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133605" target="_blank">📅 22:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133604">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
اولین بمب نقل‌وانتقالاتی با دود قرمز!
🔴
🔴
کسری طاهری بازیکن تیم روبین کازان به توافق نهایی با پرسپولیسی‌ها رسیده است و به زودی از او رونمایی می‌شود.
🔴
🔴
ستاره ۱۹ ساله فصل گذشته پیکان که البته به صورت قرضی برای این تیم به میدان می‌رفت و تحت قرارداد روبین کازان است،…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133604" target="_blank">📅 22:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133603">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
سی‌ان‌ان: ترامپ از حملات اسرائیل به لبنان به‌شدت خشمگین بود و در تماس تلفنی با نتانیاهو از الفاظ رکیک استفاده کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133603" target="_blank">📅 22:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133602">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#جام_جهانی
😀
کنداکتور آنلاین جام جهانی فوتبال امروز و بامداد فردا:
😀
اسپانیا
🆚
کیپ ورد
🇨🇻
⏱
ساعت ۱۹:۳۰
🇧🇪
بلژیک
🆚
مصر
🇪🇬
⏱
ساعت ۲۲:۳۰
🇺🇾
اروگوئه
🆚
عربستان
🇸🇦
⏱
ساعت ۱:۳۰
🇮🇷
ایران
🆚
نیوزلند
🇳🇿
⏱
ساعت ۴:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/133602" target="_blank">📅 22:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133601">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
🔴
خداداد عزیزی با حضور در باشگاه پرسپولیس قرارداد شو امضا کرد و رسماً سرپرست پرسپولیس شد / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/133601" target="_blank">📅 22:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133600">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚠️
⚠️
فوووری از ورزش سه: کسری طاهری مهاجم روبین‌کازان با پرسپولیس به توافق نهایی رسیده و بزودی از او رونمایی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133600" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133599">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341342c2ca.mp4?token=dHsKJhPBUK--W7_K1RvDtdzZ5nlkk4sZxzCOONNFL99MSf74bFyZzMcg1I0WYUvUlAWDjZtGYSeEpm2E7Tjt3reZAcIWACxG1IALcMZGFok0tu6GQdpmS1y-s6dBqCR6Xa2-T4uS6GuXTt5g34vUIzp1JBNZm4lulRXQHaVIYlUINqBrIlmFsMixo3s1Uw3sJx_QYwc8rNfR7MVM2sdgj6XqrC0jxck6MC5ZhbBJNvM0bKM56K3BpAHtA_BQReNIl9-QX-3wMlGPJbVHOhOiIwE6UQeMmihdkH_sNvMdBxrlKrvvboxQEmtVWJoCJskHXytuPsJe-vwNry2KDpRhRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341342c2ca.mp4?token=dHsKJhPBUK--W7_K1RvDtdzZ5nlkk4sZxzCOONNFL99MSf74bFyZzMcg1I0WYUvUlAWDjZtGYSeEpm2E7Tjt3reZAcIWACxG1IALcMZGFok0tu6GQdpmS1y-s6dBqCR6Xa2-T4uS6GuXTt5g34vUIzp1JBNZm4lulRXQHaVIYlUINqBrIlmFsMixo3s1Uw3sJx_QYwc8rNfR7MVM2sdgj6XqrC0jxck6MC5ZhbBJNvM0bKM56K3BpAHtA_BQReNIl9-QX-3wMlGPJbVHOhOiIwE6UQeMmihdkH_sNvMdBxrlKrvvboxQEmtVWJoCJskHXytuPsJe-vwNry2KDpRhRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو بازی آلمان و ایتالیا در لیگ ملت‌ها، لوکا پورو بازیکن ایتالیا هنگام زدن آبشار بلند میشه و میگه:
یاهووووو
😂
😂
😂
😂
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133599" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133598">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
جام جهانی| کیپ‌ورد نخستین شگفتی جام جهانی ٢٠٢۶ را رقم زد؛ ماتادورها پشت سد کیپ‌ورد؛ لقمه‌ای که از گلوی اسپانیا پایین نرفت
❗️
اسپانیا صفر - کیپ‌ورد صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/133598" target="_blank">📅 21:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133597">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📸
تصاویری از نخستین تمرین پرسپولیس با حضور اوسمار ویرا پس از بازگشت به تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133597" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133596">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
گروه H ؛ جام‌جهانی 2026
🔴
پایان نیمه اول بازی    اسپانیا
🇪🇸
0️⃣
🏆
0️⃣
🇨🇻
کیپ ورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/133596" target="_blank">📅 21:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133595">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAq-F20MrY6l5HJTIB7pVwxETgtmImLkJ_1krrfqrQMvTriJ9vUpNFNlBS6-GqLMHoOckWNe4D1Ls6jpwniA9P9cxMJiUkB-hTHzNiuBHOeXlV38ya9FHEsGi8CvI_avvEn8n9pNwdNUyRwnUn_41OricbtkBc5xOS9GBJQIhi8i533C61op3awou39lLLa9oNZWSd7aeYUIIrR98Se13AAXql2K33aZJ0fpJ4IYcyGrSSFRTbau6bSbx2_nlnshyXYUckhGHHY7Lhy1XZyfTBnFlWWIUwIy8_ZIZTgt99bI3jiEYg1CATR84fbDGR5Zhb7FfAC3rWjiJIuN-bR3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه G جام‌جهانی ۲۰۲۶
[
ایران
🇮🇷
🆚
🇳🇿
نیوزیلند
]
⏰
بامداد سه‌شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133595" target="_blank">📅 21:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133594">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📸
تصاویری از نخستین تمرین پرسپولیس با حضور اوسمار ویرا پس از بازگشت به تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133594" target="_blank">📅 21:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133593">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj65iASi8PHae4YtufuZf6AKqVHhpOuz2UPHw_L3IijD4ux515wutnZ4FB8MWE5nOX2P4iJao3nHAK1-a0AJHVVTZUHw98zfeAObRg7QrcGlmXhrGdRP3pXGftp52zEJgPu130m7J2NNTsTnnAB7E2CtrXzh8Yg_193YqtOphiz-bqMOBLvo4QI7FlsIqyn2RjwAGuWoqcLx-UHsjNj2wdlN7IRV35VNIXOET5HSitUavxiROj7bRVW7vXzOSs0SZzRzeTxEpFgIUl3V_EsXeCUGwJLmrVk8SkfFRm24FnzLRpm7r-GrBLM6n_pT3RykqhbfBuYUOpd4XYomv3RENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از نخستین تمرین پرسپولیس با حضور اوسمار ویرا پس از بازگشت به تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/133593" target="_blank">📅 20:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133592">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
❤️
امشب ساعت 4:30 صبح بازی ایران مقابل نیوزیلند برگذار میشه
🔸
بیدارید یا خواب؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/133592" target="_blank">📅 20:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133591">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#جام_جهانی
😀
کنداکتور آنلاین جام جهانی فوتبال امروز و بامداد فردا:
😀
اسپانیا
🆚
کیپ ورد
🇨🇻
⏱
ساعت ۱۹:۳۰
🇧🇪
بلژیک
🆚
مصر
🇪🇬
⏱
ساعت ۲۲:۳۰
🇺🇾
اروگوئه
🆚
عربستان
🇸🇦
⏱
ساعت ۱:۳۰
🇮🇷
ایران
🆚
نیوزلند
🇳🇿
⏱
ساعت ۴:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133591" target="_blank">📅 20:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133590">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">#شفاف_سازی
‼️
خداداد عزیزی،پژمان راهبر،رضا فیض بخش و فرزاد حبیب الهی شق کردن اسکوچیچ رو بیارن…هرچیزی گفتن بهتون کصشره شخص خداداد عزیزی پشت این موضوعه و همه میدونن ارتباط و رابطه بین این افراد نام برده چیه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/133590" target="_blank">📅 20:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133589">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtFKnJpWWj-Yy1dDlCwGcbfNl7YDzSVPATxcBjk9iCuZx98BghjF2Ji-Kik9F0t6C2yCvqLfnVa-ZQ65UknsU5Df21s7yelDRfapvhulgaRBhWv-7QkAGNYPPK7f7QsCOgsOTYFSEIe9s0NEDT-epR4EwkVs9634x8nzp4mzY2g-eZeHAioQplZKDjRefbzeALcyBguG5AN3PnU2p5l_ZAwnJ2i0pOPhNdMbtg6GdtcDEAfHEHNJQoEW5CyjR6JnsLxYm7wBWHLWdJQXP3fedqi7A5Y_nMxQPQSeVdBG5eJ67SYQr8bNHQFaVpUjMHzw6rFUwyCWz91-K1C7NNGgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
⚠️
فوووری از ورزش سه: کسری طاهری مهاجم روبین‌کازان با پرسپولیس به توافق نهایی رسیده و بزودی از او رونمایی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/133589" target="_blank">📅 20:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133588">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
🏆
مدیر برنامه کسری طاهری امروز صبح‌ و‌ عصر بامدیریت دو تیم استقلال و پرسپولیس جلسه‌ای مهم برگزار خواهد کرد تا مقصد نهایی کسریِ 19 ساله برای فصل بعد مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/133588" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133587">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
با این تفاسیر مدیرعامل و هئیت مدیره چیز خره…. از این به بعد اقای احمدی برامون تیم میبنده
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133587" target="_blank">📅 20:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133586">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">#شفاف_سازی
‼️
خداداد عزیزی،پژمان راهبر،رضا فیض بخش و فرزاد حبیب الهی شق کردن اسکوچیچ رو بیارن…هرچیزی گفتن بهتون کصشره شخص خداداد عزیزی پشت این موضوعه و همه میدونن ارتباط و رابطه بین این افراد نام برده چیه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133586" target="_blank">📅 20:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
با این تفاسیر مدیرعامل و هئیت مدیره چیز خره…. از این به بعد اقای احمدی برامون تیم میبنده
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/133585" target="_blank">📅 20:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
باشگاه پرسپولیس با خداداد عزیزی به توافقات نهایی دست یافت و بزودی از وی به عنوان جانشین پیروانی معرفی خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133584" target="_blank">📅 20:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133583">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
تیوی بیفوما امروز از دبی به استانبول میره و فردا صبح میاد تهران تا در تمرینات شرکت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133583" target="_blank">📅 18:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxT_b-Djvie6xw2wdZXIbQBKRzDJYO8URXK-iq8hJyT7o6F1NBG2u7TTyste9QS1r4aT5hmo4XPWcgMWAw5P3_aD9u_eVJTjJSX-cFgxieQp-yopxTwrbje0szyBjW_Xfjc0RCVHXQavuqjGaltW1nuNeX3SjbAh4P5pxVumdmATnEy8OQD7XZfFf57vjVkcOug6JZadrL1_TzKm2jJCDo0Ggr3Wjrn-7GfDElIAQxA-XPfmymIMlliR8y5PuB8ii-YxD-O9qMx14dCDhcWbBFMslINT3kZOaURSAAj4JWsSIxXO4zcAxdrp9LbEsPi_WUtAjxMS6ZzQLaQUrDOMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل فردوسی‌پور در برنامه خود درحال گفتگو با دین هویسن ستاره رئال‌مادرید است
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133582" target="_blank">📅 18:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
رئیس جمهور: بیش از ۹۰ درصد اعضای شعام با توافق با آمریکا همراهی کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133581" target="_blank">📅 18:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133580">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
❤️
#فوری | نیویورک تایمز:
🔸
محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، و عباس عراقچی، وزیر امور خارجه، برای امضای توافق با جی‌دی ونس، معاون رئیس‌جمهور، به ژنو سفر خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133580" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133579">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
🔴
خداداد عزیزی با حضور در باشگاه پرسپولیس قرارداد شو امضا کرد و رسماً سرپرست پرسپولیس شد / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133579" target="_blank">📅 17:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133578">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
اتفاق خاصی نیوفته خداداد طی روزای آینده با قرارداد مالی خوبی پرسپولیسی میشه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133578" target="_blank">📅 17:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133577">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
❗️
خبرگزاری فوتبالی :
🔴
🔴
اوسمار به مدیران پرسپولیس اعلام کرده برای شرکت در تورنمنت سه جانبه به ایران برگشته و برای ادامه‌ی همکاری در فصل بعد باید فکر کنه و از خانواده‌اش مشورت بگیره.
🔴
🔴
باشگاه هم به خاطر این که فصل بعد در صورت نیومدن اوسمار به مشکل نخورن؛…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133577" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133576">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
✅
اوسمار به مدیرای گفته برای فصل بعد باید فکر کنه و با خانوادش مشورت کنه و باشگاه به صورت موازی مذاکره با یه گزینه‌ی داخلی و دو گزینه‌ی خارجی رو پیگیری میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133576" target="_blank">📅 14:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133575">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1962b1668b.mp4?token=aNjRyjdG0rKx1QtbhBb0u1sEzJa5k9mQxAZHdvbp_wkD8ixWFzzweTW5-RzhcgReA2CAzzJzc5-SUZ725p8hDGiC4qVicDuUQP7Yoc3WXmEVNBFMBg5rcWmJ9uhz7XkI9XOOKb3wVAf6TrPEplqX5wgI9-N_ASVW6-hxa6NLkYZHskU-wW1Nuq98MmM1eHB4ZLd4m8e0z4mWKVcNIMR2JRkUWHeZfLW-5b3nSqGOr-sQeZwtq35hBqzl-QONc0Hw5mNFPZ1ZdKEoK1DlN27fyLv2dMrj739iI__sD5SpZrCUHAGnqsQIqxQ6EO_L6mj7gko0me-RkGmfiw8u27E5Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1962b1668b.mp4?token=aNjRyjdG0rKx1QtbhBb0u1sEzJa5k9mQxAZHdvbp_wkD8ixWFzzweTW5-RzhcgReA2CAzzJzc5-SUZ725p8hDGiC4qVicDuUQP7Yoc3WXmEVNBFMBg5rcWmJ9uhz7XkI9XOOKb3wVAf6TrPEplqX5wgI9-N_ASVW6-hxa6NLkYZHskU-wW1Nuq98MmM1eHB4ZLd4m8e0z4mWKVcNIMR2JRkUWHeZfLW-5b3nSqGOr-sQeZwtq35hBqzl-QONc0Hw5mNFPZ1ZdKEoK1DlN27fyLv2dMrj739iI__sD5SpZrCUHAGnqsQIqxQ6EO_L6mj7gko0me-RkGmfiw8u27E5Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇮🇷
ایران آماده و مصمم برای آغاز دیدارهایش در جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133575" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133574">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
تاجرنیا: شنیده‌ام پرسپولیس در بحث اسپانسر، قراردادی دارد که باید در لیگ نخبگان باشد
◻️
به تلاش‌های باشگاه پرسپولیس احترام می‌گذارم ولی برخی اقدامات تنش و مشکلات را بیشتر می‌کند و حتی باعث می‌شود انرژی نمایندگان ایران در آسیا، در آستانه شروع این مسابقات گرفته…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/133574" target="_blank">📅 13:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133573">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
درحالی که چند روزی از شروع تمرینات پرسپولیس می‌گذرد، محمدحسین صادقی همچنان در تمرینات غایب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133573" target="_blank">📅 13:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133572">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgbDK0lOd3_fEHNCRmikeeN-cKKxxkmqxmCDYYWqUIn0tvWrdAwJDFl2Qw2hXSVUFIo_ukhcv8OcVeFYWpspk-nKTPNTBkfpqJTak09v2zq_KejxM_wk4DoJyzzMDKOF74HqhcABO0WDT_SqQZ3aZhbhTGOawtlgQUacyA7Dep5tDqa113BzBPtSs9R4gog-pj4J_ZziDmYN1jFErK1gW5YMvm_jrdkvjGa_w2Y7VI8xwFOme-L1vr6cO2OJVG9NkO-x_IKtI-08635F-b4iJmobbVGfnu9V7lqxMm-th_oGF27OTheTv8PVnr3ektmoETItLPWu8rejO5mvfQpH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
درحالی که چند روزی از شروع تمرینات پرسپولیس می‌گذرد، محمدحسین صادقی همچنان در تمرینات غایب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133572" target="_blank">📅 13:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133571">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSaz6RPTqI3g1qSs7Lcg9zFWEdlWV_1jnql7r58n9PaZiDa-SlowhOftZXD0VnKEkWVhUX5NOGHE_xjwNQRL45bIkHwqlRn9UuMmw2BlvpMILG7KkzZoYiLgSPLpxA4uypS-K3QKqdTvdNn4yeMWK_l_WBbEkwv5khu5c_B2jTjBGbv4SS99t4wmig72aZHP9N2urDnSVJuaMm3nsK2my2RMFlrwFkGTFB-ybm2AuoUxgLFydGx--VpakRyxYIPaOCF3d5kTx1cVPYQ7hqyFinHZ8w6SA4x_3gfCA_2iA4Ezeua66HkQYgCI6zZDUJw61hj_XeqQI5OF6FavcnPFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه H جام‌جهانی ۲۰۲۶
[
اسپانیا
🇪🇸
🆚
🇨🇻
کیپ‌ورد
]
⏰
دوشنبه ساعت ۱۹:۳۰
🏟
استادیوم مرسدس‌بنز
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133571" target="_blank">📅 13:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133570">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
خداداد عزیزی پیگیر امور نقل و انتقالاتی پرسپولیس شده / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/133570" target="_blank">📅 13:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133569">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📊
📊
جی‌دی‌ونس: برای شرکت در مراسم توافق میرم ژنو!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133569" target="_blank">📅 13:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133568">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
امیرحسین محمودی امروز صبح برای تیم ملی مقابل تیم جوانان تیخوانا به میدون رفت و موفق شد یک پاس گل بده
🔴
علی علیپور هم موفق شده دبل کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133568" target="_blank">📅 13:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133567">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
مهدی ترابی: در گذشته زیاد آهنگای تتلو گوش میدادم و تتلیتی بودم، اسطوره ورزشیم علی دایی هستند
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/133567" target="_blank">📅 13:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133566">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwwtzYPgK17Z9_dzor362LtYnKrYypJbvcTlLImQsGQUNsXDRILDocTAq8sfsbeUZe2JoMsJ_QDn7Zl17rLe8Artp0RABgq8PaoC7eeVJzqVVV6MXIQB1nXnTxIY53_PYu8HUCYRIGhcP4HZSgizcz0VOWU8xYT2vTwHsDtKlSXp6j04KzqTWz3Xsl_ghu4ALowUY1y_VO30IjJKcEpNMwiw36C4oEhQWnObWMJ51WFEXI4s9K7HEyPooxb06wktZeFjkilqyqU7uvTuKm-j5Yq6uYw_tJDDl4zrrrhdCbC-xvyJPScuckp9A281iyvPMtIZj_UCKjpH2lIYYYlWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر به صورت رسمی برگزاری سه‌جانبه انتخابی نماینده آسیایی را پذیرفت.
‼️
اسفندیارپور قبلا اعلام کرده بود که گل‌گهر انصراف می‌دهد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133566" target="_blank">📅 13:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133565">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤍
امیر قلعه‌نویی:
می‌دانیم که ایرانیان زیادی در دهه‌های اخیر در لس‌آنجلس حضور دارند و امیدواریم که در بازی فردا در ورزشگاه به ما انرژی بدهند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133565" target="_blank">📅 13:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133564">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
براساس گزارش نیویورک‌تایمز؛
کاروان تیم ایران با ۱۰۰ افسر امنیتی و پهپادهای پیشرفته از این کاروان مراقبت شد که تقریباً ۲ برابر اسکورت تیم‌های دیگر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133564" target="_blank">📅 13:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133563">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
محمد سیانکی گزارشگر صدا و سیما جمهوری اسلامی راهی آمریکا شده و قرار است هر سه بازی تیم ملی را در جام جهانی گزارش کند
🫥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133563" target="_blank">📅 13:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133562">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQkVp7WOWkLQWLC1yXldaP4QRK_L5fsHKL5ZKuff-d-RDHy5rZGGgxLO9dlNS0QWUhxSkOWIqV8H1Xycv4HYe8I8eBZkx1PnYqih8oDuQIA1wfsAJe7MxlAgHnNzRSY9EYWoqjXLB8obZJhPlyy6J5wCJjKInAQP8t8fVt7LM9LZNtR8wjRHsFKw8_W4MIVaQBmWYP_2a5tdjoqkmqTUPd_TNe1ebwKMSI4cNWuYAEt3jzyQOZvTTYj6XFsOcs11HHN-dwbjfwkhMjy9oQOA6einUyvSwJ_KVUYkRG_5MpZ63eULRDMnVYdwJLq6E0Ss3vzgoZc3As1LSdG65zXB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
راوی ماندگار مستند ناصر حجازی درگذشت
🔴
بهروز رضوی یکی از اساتید هنر دوبله و گویندگان فراموش نشدنی رادیو و تلویزیون ساعاتی پیش چشم از جهان فرو بست و درگذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133562" target="_blank">📅 13:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133561">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
خداداد عزیزی پیگیر امور نقل و انتقالاتی پرسپولیس شده / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133561" target="_blank">📅 11:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133560">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
✅
اوسمار به مدیرای گفته برای فصل بعد باید فکر کنه و با خانوادش مشورت کنه و باشگاه به صورت موازی مذاکره با یه گزینه‌ی داخلی و دو گزینه‌ی خارجی رو پیگیری میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/133560" target="_blank">📅 11:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133559">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljDu-7Vth6ZkhOER4r02-6SSMmCvcFqoDjeWJK6cNxA2wAJ1eYmRuU3_L25w5MCHvXk5ybF2e6J7BBJUmRfjtFNXpPxY63gJDbwCyMTlWIhu43iOIJjMheJ_Y7wA-kjwFV0MjF-C82uf7OX7UX-lGSmJ7OfF5rdL5J395XTzHNVxl238xCqdWizhBZg-NkqDQc99ZjKBwiguY9oiMVKHNMaGQZdCG8Uic07TXmGRJp51sz6Ltfd6RzNSUVm3LGvKiLSkZPy-0_dGACgIzg60S7CgMGvGLP8deUYhqRfS8mN1yte_9NAZ1ojSu6UCfb5X-EIyI6MXxg67pP4wtiAhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
رده‌بندی تیم‌های لیگ ملت‌های والیبال 2026 در پایان هفته نخست
🔴
ایران در رتبه پانزدهم جدول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/133559" target="_blank">📅 11:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133558">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
❤️
امشب ساعت 4:30 صبح بازی ایران مقابل نیوزیلند برگذار میشه
🔸
بیدارید یا خواب؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133558" target="_blank">📅 11:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133557">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">#جام_جهانی
😀
کنداکتور آنلاین جام جهانی فوتبال امروز و بامداد فردا:
😀
اسپانیا
🆚
کیپ ورد
🇨🇻
⏱
ساعت ۱۹:۳۰
🇧🇪
بلژیک
🆚
مصر
🇪🇬
⏱
ساعت ۲۲:۳۰
🇺🇾
اروگوئه
🆚
عربستان
🇸🇦
⏱
ساعت ۱:۳۰
🇮🇷
ایران
🆚
نیوزلند
🇳🇿
⏱
ساعت ۴:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133557" target="_blank">📅 11:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133556">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#جام_جهانی
😀
کنداکتور آنلاین جام جهانی فوتبال امروز و بامداد فردا:
😀
اسپانیا
🆚
کیپ ورد
🇨🇻
⏱
ساعت ۱۹:۳۰
🇧🇪
بلژیک
🆚
مصر
🇪🇬
⏱
ساعت ۲۲:۳۰
🇺🇾
اروگوئه
🆚
عربستان
🇸🇦
⏱
ساعت ۱:۳۰
🇮🇷
ایران
🆚
نیوزلند
🇳🇿
⏱
ساعت ۴:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133556" target="_blank">📅 10:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133554">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
⚽️
🎙
امیر قلعه نویی سرمربی تیم ملی: برخی بدون مطالعه می گویند جام جهانی با ۴۸ تیم آسان تر شده است اما به نظر من اتفاقا سخت تر هم شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133554" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133553">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
اقا کریم از بازگشت اوسمار خیلی خوشحاله چون دیگه بهش فشار نمیارن که سرمربی بشو/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133553" target="_blank">📅 09:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133552">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⁉️
⁉️
حضور عزیزی در پرسپولیس قطعی است؛ آغاز فعالیت‌های سرپرست جدید در امور نقل‌وانتقالاتی
🕯
حضور خداداد عزیزی در پرسپولیس قطعی شده است و حتی او پیگیر برخی امورات مربوط به تیم و نقل و انتقالات نیز است.
📊
📊
عزیزی خانه خود در تهران را حدود ۱۰ روز پیش در جلسه که…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133552" target="_blank">📅 09:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133551">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
فوتبالی: چند بازیکن پرسپولیس به کریم باقری گفتن خودت مربی شو ولی اقا کریم گفته نه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/133551" target="_blank">📅 09:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133550">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
🔴
کسری طاهری:   •
⚡️
میخوام امسال قرضی برگردم لیگ ایران  •
⚡️
با پرسپولیس و استقلال مذاکره داشتم.  •
⚡️
طی چند روز آینده تصمیمم رو میگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133550" target="_blank">📅 09:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133549">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c82165294.mp4?token=VmO8lPBKi-y8jRMeVOy2GSaJC5QYKYSbRZdUXkwVb1q_6Pq5j4g7ZODVfLbUzl1ODnD0m0zPQQ5ocTUEUz6kAhy-lXcH19ipd9LksZ4O1CSvs4xHXUgRqZKmJlK9H5uAa1ne84IyapvYOUSaNCmQO8E2QffK79ALMUjj-xWNvQgXYwfVetyslJbS4iupVD6u6V5Gvn8HX_GZt3M192MaObMRYIy0lvD7Wz2EQg1yX4zwTsAK1gYSZ7aHzgy51OKzSkda67KlT90ajYtkA9-ZnaKL3KeCg1iygnG2IlvI-lHcyjRmS0UN94cE86dDVm5uiouiHqMokecb_y1veYBEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c82165294.mp4?token=VmO8lPBKi-y8jRMeVOy2GSaJC5QYKYSbRZdUXkwVb1q_6Pq5j4g7ZODVfLbUzl1ODnD0m0zPQQ5ocTUEUz6kAhy-lXcH19ipd9LksZ4O1CSvs4xHXUgRqZKmJlK9H5uAa1ne84IyapvYOUSaNCmQO8E2QffK79ALMUjj-xWNvQgXYwfVetyslJbS4iupVD6u6V5Gvn8HX_GZt3M192MaObMRYIy0lvD7Wz2EQg1yX4zwTsAK1gYSZ7aHzgy51OKzSkda67KlT90ajYtkA9-ZnaKL3KeCg1iygnG2IlvI-lHcyjRmS0UN94cE86dDVm5uiouiHqMokecb_y1veYBEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⚽️
بازدید بازیکنان ایران از ورزشگاه سوفای، میزبان دیدار با نیوزیلند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/133549" target="_blank">📅 09:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133548">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
نیویورک تایمز به نقل از مقام‌های ایرانی گزارش داد که محمدباقر قالیباف و عباس عراقچی برای امضای توافق راهی ژنو خواهند شد.
❌
به گفته این مقامات، ایران عمداً تا پس از نیمه‌شب به وقت محلی صبر کرد تا امضای توافق با سالروز تولد دونالد ترامپ هم‌زمان نشود
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133548" target="_blank">📅 08:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133547">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇵🇰
🇵🇰
🇵🇰
#فووووری شریف، نخست‌وزیر پاکستان:
🔸
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133547" target="_blank">📅 08:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
#فوری | یدیعوت آحارونوت:
🔻
نتانیاهو با درخواست ترامپ برای آتش‌‌بس و عقب‌نشینی از لبنان مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133546" target="_blank">📅 08:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLcbMBYqt8z6_szynatZfJTLYb0lrfHVjp03L-B5tOJxlo-lRUe44-nlBXbHm-WjtZxOWkeixPGixkhtPe8sVyjXBaUGSKTe8eE-1ryfRme7IxkhKLguclcbbGPY8c9HHdkhoM-5ajvptzs7-UR_voVvoWPgs64gAMyxRUckrAPoPfUNOddm3pYU4iKF5T534tLSCP7DsR9hhLIKZAm12hTLJta7DSAFqzRV895-vdz9UgRdmQ8j_rNjjV_5fS3mQkE-vlJB3Xcd_kNTCaA6QrfmYXg0QfwMvby0h2v3d8En22gs67NkC7VRnCeaCBdejErKpdKwwFbns7MP3u04QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه F جام‌جهانی ۲۰۲۶
[
سوئد
🇸🇪
🆚
🇹🇳
تونس
]
⏰
بامداد دوشنبه ساعت ۰۵:۳۰
🏟
استادیوم مونتری
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/133545" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
نتایج شب گذشته جام جهانی 2026:
🇶🇦
قطر ۱ - ۱ سوئیس
🇨🇭
🇧🇷
برزیل ۱ - ۱ مراکش
🇲🇦
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند ۱ - ۰ هائیتی
🇭🇹
🇦🇺
استرالیا ۲ - ۰ ترکیه
🇹🇷
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133544" target="_blank">📅 01:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇵🇰
🇵🇰
🇵🇰
#فووووری شریف، نخست‌وزیر پاکستان:
🔸
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133543" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
