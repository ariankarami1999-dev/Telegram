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
<img src="https://cdn4.telesco.pe/file/Ag9bJ44kEhHJJKQTg5GoERrbNhyjLUWH58OjCMtICRpGu_8sN3B6P1KqQXXEfTdPLnxt0xtFVhWWgzkEbu2bl--c54MtttYwvAIaROR1jjLejLeF6WZl20pEydiHJw0-x3fSyr3OzMqMi6byNB5lU4iyFcp2GWUB2iJKwCbaRz4dns-M4VgzG6a2TPFM4Pcomkq0OnElZ9f9dwuc2ryRmMoys3sBMWPO2Zd_GTVyjcrPVDZ2UYfBuqtXyKHWxiIIOLBxQ7XH1kdB7ByGz0FYWN4zF4ohHz7QgMKzJ2sxrRMZlgClf8KEeXi4oNIr4QCXH2PSnLyLSCF944QNVPYC1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 421K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 01:04:23</div>
<hr>

<div class="tg-post" id="msg-19383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش‌انفجار‌ بندر ‌طبرسی
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/withyashar/19383" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19382">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش انفجار بوشهررررر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/19382" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19381">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سازمان دریانوردی بریتانیا:
دقایقی پیش یک نفتکش عربستان در نزدیکی این کشور مورد اصابت یک موشک قرار گرفت و آتش سوزی گسترده ای نفتکش را در بر گرفته است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/19381" target="_blank">📅 00:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19380">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش انفجار رامشیر خوزستان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/19380" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19379">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش انفجار دزفول
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/19379" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19378">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پاسگاه سیریک رو زدند
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/19378" target="_blank">📅 00:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19377">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAW3pKEhm5l4GNl4isCTaPxh56K0woeq8qFTWDJRsQ441SM1bN7lEcBxUiEoUPh1nD-g_vlIgGpQJN_xMrWNcCZHm7H15ZFtxqk0QK6WXArIpmLWDZadG6rTU6jcF3V-gT4iXPm8Hz1QkpuN9zwF0jzTEOtxxER_FnriV-ATj8N50fN45R9sGMFqqA29bT8z-gocNoUfH-Tx6_Tyk5h9SbPKu7sVoujECvwLHOQm_ML-_oY_5lVtqAjdUPu77kf23OnqMdku4jXRGPnYOJ01dffudiO6CaTIJ-4yQY9tp7yomsukhJMUuDlqFZAbGoXP_ko-00pA59xsTAzpoxIKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه ای که امشب مردم ایران منتظرند روی فلایت رادار ببینند.
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/19377" target="_blank">📅 00:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19376">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صداوسیما: دقایقی پیش؛ شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/19376" target="_blank">📅 00:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19375">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش انفجار رامشیر خوزستان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/19375" target="_blank">📅 00:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19374">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پرواز جنگنده تبریز
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/19374" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19373">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دو انفجار اهواز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/19373" target="_blank">📅 00:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19372">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش صدای انفجار بندر ماهشهر
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/19372" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19371">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شروع شدددددد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/19371" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19370">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش صدای انفجار اهواز
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/19370" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19369">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">از شهر موشکی مخوف یزد موشک پرتاب شد
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/19369" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19368">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اسرائیل با ارسال یک پیام به هزاران نیروی پلیس خود آماده باش داد:
"با توجه به نگرانی از وخامت اوضاع امنیتی، تمام پلیس‌ها باید در دسترس و آماده برای هر سناریویی باشند، به طوری که تجهیزات شخصی آن‌ها در دسترس و آماده استفاده در صورت نیاز باشد."
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19368" target="_blank">📅 23:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19367">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حقیقت یاب سنتکام: ایران تنگه هرمز را کنترل نمی‌کند. این مسیر آبی بین‌المللی علیرغم تهدیدها و حملات سپاه پاسداران باز است. کشتی‌های تجاری همچنان با پشتیبانی نظامی ایالات متحده از تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19367" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19366">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19366" target="_blank">📅 23:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19365">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روزنامه سان : بریتانیا کارکنان سفارت خود در تهران را از ایران خارج کرده است
؛ اما نکته مهم این است که فعلاً گزارش‌ها از
تخلیه کارکنان دیپلماتیک (staff withdrawal)
صحبت می‌کنند، نه اینکه ساختمان سفارت تخلیه یا بسته شده باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19365" target="_blank">📅 23:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19364">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال ۱۲ اسرائیل: بریتانیا در پی وخامت اوضاع، در حال تخلیه شهروندانش از ایرانه.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19364" target="_blank">📅 23:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19363">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19363" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19362">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19362" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دروازه های جهنم   پیشبینی خودتون رو برام کامنت کنید کارای اداریش رو هم انجام بدید  https://www.instagram.com/reel/DbGvd4YRk8m/?igsh=cTlmeHd6bGVvYnM4</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19361" target="_blank">📅 22:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19360">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سیستم دفاع هوایی مخوف c-ram در کنسولگری ایالات متحده در اربیل عراق فعال شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19360" target="_blank">📅 22:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19359">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به گزارش خبرگزاری رویترز پهپادهای رژیم ایران تاسیسات سازمان سیا را در منطقه مورد هدف قرار دادن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19359" target="_blank">📅 22:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19358">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۶ انفجار پهپادی اربیل عراق
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19358" target="_blank">📅 22:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19357">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG6hzr-SbwZ1RykJCgr7DdDUiL0wPLs9l81YaFpGeAgTfc17x7Jb6-aXPXo_Coo4lJ9WI5fp4u_hYAt8-gvrCrj-MvTLGnZwOexWvmLZTlOfQQai5x6H_qo0yNwPhw3194C8YD3XmDyya6APRewUYCrrrsPDrJKljbAD43wilOdBl8oKMJ4e9Ou8PhXZExpiuyyxJ9M26k8WYeyz7yZcoSwRclKUKGKmUk4szMoK-6upbZMPl3wZ0SCbtN0wwgRBATrQaQp6jBGoKX4A9AsOG-cyJ9xFO-37r-oZBt2S1JJ6LoM4Vatl2zgpZORsNH4QjUs7EX8qdrh0KvudMjNxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دروازه های جهنم
پیشبینی خودتون رو برام کامنت کنید کارای اداریش رو هم انجام بدید
https://www.instagram.com/reel/DbGvd4YRk8m/?igsh=cTlmeHd6bGVvYnM4</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19357" target="_blank">📅 22:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سیریک صدای توافق میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19356" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19355" target="_blank">📅 21:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سناتور در‌ جلسه سنا
:
مردم دیگر نمی‌دانند کدام روایت درباره جنگ را باور کنند؛ چون یک بار گفته می‌شود جنگ تمام شده و بار دیگر گفته می‌شود تمام نشده است. یک بار گفته می‌شود ظرف دو هفته اتفاقی می‌افتد و بعد می‌گویند نه، این‌طور نیست. یک بار می‌گویند دیگر موشکی نداریم و بار دیگر می‌گویند هنوز موشک داریم.
همین سردرگمی باعث شده بسیاری از مردم گیج، نگران و تحت فشار باشند و این جنگ را به‌شدت نامحبوب بدانند. چون تصمیم‌هایی را که رئیس‌جمهور می‌گیرد درک نمی‌کنند و با آن تصمیم‌ها موافق نیستند
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19354" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سد مجید گشاد زن
فرمانده هوافضا تروریستی سپاه:
به پل ها و نیروگاههای ما تعرض شود خاموشی برق متحدان و میزبانان کودک کشان قطعی است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19353" target="_blank">📅 21:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بیانیه فرماندهی نیروی دریایی تروریست سپاه(همون چرکه):
ورودی و خروجی تنگه هرمز مشخص و در کنترل قطعی ماست. مسیرهای جایگزین ، نا ایمن و خطرناک است اخطار می دهیم استفاده نشود که تبعات سنگین و غیر قابل جبرانی خواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19352" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدای انفجار‌ در کویت
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19351" target="_blank">📅 21:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx6T9xnjNYdDwiWMbr2ydGetjKh_nQa2QUsxC3nI-4ISQO3ezrRZUJPIuh0eby4LWNUlJ3bqc3z5hATlbkrOyKCEiRSc235EDWiw9aPfqrd_lnJoZ7Zh2RLUAVICV9DYhZHMxAuDQrDbuotZZzOXmT27myQTUpb0ppvgEUDALEpsuCFDDZtLiXNeo2hxWrkAuBrRckMuE3dUp3mKsbBfHB7WbXxj2BZpwj_QIv53MUwCysD3gXexr5hTf4kA2QGYZ-9Ctm-33ZOAlWbcNkDW3mLw2_KaaYJeFDkRYfe1v_K3eEqNf_tgRIXnMiDLkDOUexRUNq912ylYVgSTQADOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که ترامپ بازنشرکرد
:
به سنتکام دستور داد شده دروازه‌های جهنم را به ایران باز کنن بعد از کشته شدن نیروهای آمریکایی
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19350" target="_blank">📅 21:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19349" target="_blank">📅 21:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">موج حمله موشکی جدید رژیم
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19348" target="_blank">📅 21:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری کان: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19347" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmdhOcpDHxfR_1awcasDf1czg10G6K8JnhLZHkl66uRnNvMSWYcYP8duOpfIR46P1RxGCij2ZiCGhHiO-nfhDqJpDgS0_7mzREMyNvuEPmxrnt_ke4BBgwkrc5Lf-7p2120KK8TsjBTXEocq-oFnGCLfTf01C6OBpbCMfyGQ3nVNqpT8dVJpOpOzvsE4MJYw4-SeLG33hXmf73jIXxil50FLpWzM5szTruOPePd2hSgbsI7pNAbx8oZ0Nr2kGv9FIWwQjHu4ufkPd07P9Qtky4ygEu8FKbiLpmbknisZT9fM-OAaLkAAmh8qj8QbHG36-0rb71OITy_aLl1MgzFKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‎سنتکام:نیروهای ایالات متحده که محاصره دریایی علیه ایران را در دریای عرب اجرا می‌کنند، طبق اعلام سنتکام (فرماندهی مرکزی ایالات متحده) تا تاریخ ۲۲ ژوئیه، ۹ فروند کشتی تجاری را تغییر مسیر داده و ۱ فروند را از کار انداخته‌اند. ناو یواس‌اس مایکل مورفی (DDG 112) عملیات را زیر نظر دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19346" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19345" target="_blank">📅 20:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حمله موشکی پهپادی رژیم به اربیل عراق
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19344" target="_blank">📅 20:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">علی‌رغم هشدارهای ایران ،بلغارستان اجازه استقرار هواپیماهای آمریکایی در خاک خود را می‌دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19343" target="_blank">📅 20:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d436f581ea.mp4?token=qPLEEtFkDWrupN7lFiuP_dS8aMzXHh8TqnBCatx6gB8mJSmwzJJysEOBJdXs1xBIBZPp4gUfhgJR2sgUgVx-QpC3D9SLODvFRNlFMba6Ix5T2gBDWc0e1HwtUGwiNtvkFyL0wYSdbkXq4323kEjN6-bL1Jl522QhmMjpicljMDDsxUrEFB71L4m4Iz7OkNnxJNIuLrBDA_5-bHpNWiXMSEO8OKbBC_quKDgJoqW63zGIYQrzHiYwz52UJbR-WaxazBmMv1o2uvgCkQLl9GiOxajnypfS8nlNNSXc7bZbGfWTEfp27zf7uNURNZy9QbjfJ5keCZbRskA_iT5yZc1sG0fpPMJixz2iwYOxSOg4-cIeGuDEbCntvHhw_Dix2TzrS5AWgEl2rR0eLVIwtWIjNhsXtyp5awTdijfjLSPVcZhydIx2Dn2PNxI0lwuQPABui22wk9H8xXJSSOlFOE4CgnrlLgfJD2HCQ1RRrq-5ZPTgE4uJx7TudNgVpvFhYEgh2zzlfCTLo9lKvD0QE4oAZsIhza7jupzR-SlhWwqVleyeNO4i9sn1eSJ8iJzdRsrVG2NrFXhCXi87_o6mt1ko00XWl3pLZubPK8wXdOeZt2myeK6CTa5Ok8BAp3NtFDfJkGWGU8cgekskWyJXqL2YT60-pYeSoMin2NKC_Nudc-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d436f581ea.mp4?token=qPLEEtFkDWrupN7lFiuP_dS8aMzXHh8TqnBCatx6gB8mJSmwzJJysEOBJdXs1xBIBZPp4gUfhgJR2sgUgVx-QpC3D9SLODvFRNlFMba6Ix5T2gBDWc0e1HwtUGwiNtvkFyL0wYSdbkXq4323kEjN6-bL1Jl522QhmMjpicljMDDsxUrEFB71L4m4Iz7OkNnxJNIuLrBDA_5-bHpNWiXMSEO8OKbBC_quKDgJoqW63zGIYQrzHiYwz52UJbR-WaxazBmMv1o2uvgCkQLl9GiOxajnypfS8nlNNSXc7bZbGfWTEfp27zf7uNURNZy9QbjfJ5keCZbRskA_iT5yZc1sG0fpPMJixz2iwYOxSOg4-cIeGuDEbCntvHhw_Dix2TzrS5AWgEl2rR0eLVIwtWIjNhsXtyp5awTdijfjLSPVcZhydIx2Dn2PNxI0lwuQPABui22wk9H8xXJSSOlFOE4CgnrlLgfJD2HCQ1RRrq-5ZPTgE4uJx7TudNgVpvFhYEgh2zzlfCTLo9lKvD0QE4oAZsIhza7jupzR-SlhWwqVleyeNO4i9sn1eSJ8iJzdRsrVG2NrFXhCXi87_o6mt1ko00XWl3pLZubPK8wXdOeZt2myeK6CTa5Ok8BAp3NtFDfJkGWGU8cgekskWyJXqL2YT60-pYeSoMin2NKC_Nudc-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو در پیامی به مناسبت نهم آو گفت اسرائیل طی سه سال گذشته با حفظ وحدت داخلی از بحران عبور کرده و به جای جنگ داخلی، در برابر دشمنان متحد شده است. او تأکید کرد که این کشور با وجود ادامه چالش‌ها به دستاوردهای مهمی رسیده و مأموریت هنوز به پایان نرسیده است. وی اعلام کرد برای تقویت وحدت داخلی، در پی تشکیل یک دولت ملی فراگیر و باثبات خواهد بود که امنیت و آینده اسرائیل را تضمین کند و افزود اختلافات انتخاباتی نباید مانع حفظ انسجام جامعه شود. او همچنین با اشاره به تجربه‌های اخیر گفت مردم اسرائیل در لحظات سخت نشان داده‌اند که بیش از آنچه تصور می‌شود متحد هستند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19342" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش آمریکا در حال انجام عملیات تخلیه تمام هواپیماهای سوخت رسان و ترابری خود از قطر می‌باشد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19341" target="_blank">📅 20:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۱۴ : سپاه پاسداران ایران، ایالات متحده را به حمله تروریستی «به سبک یازده سپتامبر» تهدید می‌کند.
خبرگزاری تسنیم وابسته به دولت گزارش می‌دهد که سپاه پاسداران هشدار داده است: «اگر جنگ ادامه یابد، ما عملیات پشیمان‌کننده‌ای انجام خواهیم داد که منجر به عزای ملی در آمریکا خواهد شد.»
آخرین باری که ایالات متحده برای یک حمله عزای ملی اعلام کرد، یازده سپتامبر بود.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19340" target="_blank">📅 20:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">منابع جمهوری اسلامی : رژیم ایران معتقده مهلت‌های آتش‌بس چیزی جز فرصت‌هایی برای تجدید قوا، سازماندهی نیروها و بازگشت دوباره به جنگ نیست و نمیخواد در چنین چرخه‌ای گرفتار بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19339" target="_blank">📅 19:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرگزاری رویترز: شرکت هواپیمایی کی‌ال‌ام هلند اعلام کرد تعلیق پروازهای به کشورهای خلیج فارس را تا ۶ سپتامبر تمدید خواهد کرد.
این اقدام به دلیل وضعیت بحرانی در غرب آسیا اتخاذ شده است
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19338" target="_blank">📅 19:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اکسیوس
:
شرط اصلی ترامپ برای برقراری آتش‌بس این است که ایران حملات علیه کشتی‌ها را متوقف کند و تنگه هرمز را دوباره برای کشتیرانی باز کند
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19337" target="_blank">📅 19:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رسانه های عبری : آمادگی در اسرائیل ، احتمال درگیری با ایران در آخر هفته @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19336" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرنگار الجزیره:ایران ایده آتش بس موقت با آمریکا را رد کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19335" target="_blank">📅 18:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رسانه های عبری : آمادگی در اسرائیل ، احتمال درگیری با ایران در آخر هفته
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19334" target="_blank">📅 18:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCw8ccS7Y5vgsakC2XGW79NLhBbENuNTPW_Tln8YkQIOydBMMPTtg3ilmUBcABpJIdkJu8EycPGht-JiXk7wUC7kCq39jwwSFmkAVFgx1bWgy5balVI4zeUt6o5lnw8HzYZ6g_6otp0FI2aNi_tZGaWugNhcpNLKReQ6Nv_TzjZyNU9gCEf2eRVxvqR2Ajyu5TKH9RCcvaLdxHMnvF02asWdU-s2DvSt5rh11a1G_lROsinScQV1XxLpnnhzlIPGk6aQclkzLL6P-RVUuuO0xQktSjmyn4NeZbHDPmRMi-O5ORD0xJa5-vwnRLL9PclaXq6WSOOPeLmQXPY_GZNdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از خوشحالی عرزشی ها از مرگ سرباز آمریکایی در هنگام خنثی سازی خدا به کمر آنها ضربه ای زد و جان دو نفر سپاهی را به همان شکل گرفت سردار احمد احمدی و سرهنگ دوم پاسدار مصطفی جمشیدیان از نیروهای واحد تخریب لشکر ۸ زرهی نجف اشرف، در هنگام چک و خنثی سازی کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19333" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAEzEm8Usn45UCASqOGb8KJMZl-egIilA5B2B3crZ6NxpAbnnUfpZ-7yE2ctOqfDqRMJ4wK8lJRc74kdKYny7T7rnzFgnZJPEyApxo-cICoENyhoM4y9eKQPQxGY9ykVWPtQoWm4o65wCyJXeEjCYrVnz-1huvG9HPJw8IF0YIPh-_SHwNHMpbQOSt2_NOSVR8Z9K8xjuD4p2YXWczsBtInLTinTBpsQeQmNawMNqFMncgKDQriZKdfR5wAbedV4QbqSh9p5EdLqVV_HzrnJOB4MmszcWB_G_XuFp-iBlLDUt3dkTyFUh2aVfM0kUKpkZ_e1_IgaHwasKVfIiNvkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک اسکادران جنگنده پنهانکار F-35 با عبور از اقیانوس، توسط دو سوختستان استقبال و کمی دیگر در انگلستان به فرود میآیند. یکی از آنها، احتمالا به علت نقص فنی یا برای نشان دادن خود به جهان و تمرین ، آلارم فرود اضطراری روشن کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19332" target="_blank">📅 18:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس به نقل از یک مقام کاخ سفید و یک منبع اسرائیلی:
کاخ سفید و دفتر نتانیاهو در حال هماهنگی برای برگزاری دیدار احتمالی ترامپ و نتانیاهو در دفتر بیضی طی هفته آینده هستن.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19331" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfead895f.mp4?token=r2s2-ypRtCKVs77EfcUjHqG17r3FbS9x9Kd-ZXQuru2suMMRnM6C7pwaqvxvgMxZZS65j0s86JAhfkvL2wPDe8SpT9UMISU26gXjGKuKTGaf0icDJYpXTVime58U28odV1qZXjoKtRl7omQmh-6d6HBD5y7shSkRgCvrMvLsXSTg7MvwNzRxAkmEWehFylZn3-rZVAtbG5dzus5qDo0yI-TIUo6XKRUSMUIPvSfzr48uqTEjfCPCE_Vu-MkHoOaKGRnKMy3wMHDmW-cwCKp-ZvK8gOE34nkUCdj02McQvJ7x47sDAgwlImGKvYSwmOwfnnYG-ixemkvmAa8CvU_nHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfead895f.mp4?token=r2s2-ypRtCKVs77EfcUjHqG17r3FbS9x9Kd-ZXQuru2suMMRnM6C7pwaqvxvgMxZZS65j0s86JAhfkvL2wPDe8SpT9UMISU26gXjGKuKTGaf0icDJYpXTVime58U28odV1qZXjoKtRl7omQmh-6d6HBD5y7shSkRgCvrMvLsXSTg7MvwNzRxAkmEWehFylZn3-rZVAtbG5dzus5qDo0yI-TIUo6XKRUSMUIPvSfzr48uqTEjfCPCE_Vu-MkHoOaKGRnKMy3wMHDmW-cwCKp-ZvK8gOE34nkUCdj02McQvJ7x47sDAgwlImGKvYSwmOwfnnYG-ixemkvmAa8CvU_nHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، قرار است در مراسم انتقال رسمی پیکر سربازان آمریکایی کشته‌شده در جنگ ایران شرکت کند.
ترامپ پیش از سوار شدن به هواپیما، به خبرنگاران گفت: «جمهوری اسلامی به دلیل کشتن سربازان آمریکایی بهای سنگینی خواهد پرداخت.»
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19330" target="_blank">📅 17:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش های بسیار صدای جنگنده رامسر
@WarRoom
😁
بفرما زدم دیگه نگو</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19329" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4d4e3672.mp4?token=Y5P8IAJxeFgRMjvyb9heT1mvO8Ymun6nlbAZMOa2Wz243zDteUc9sPBnjV50j8ZYfyCQj5X8OaduBjyOP-7SNJlA-b9x7StrVEhzVYWezb6a9iZlY_rrVl9hocOwW8ndbLx0fzUpYwjsj1LWcm8ght8ia8-iKmSBBKY4VdLhyB7NcC0KM36m7tAeXzHlP9VFiF1_6XdufGQPum3C3VT3MQkkYFR4DH-cUmilkI-3SHJ7fSq_pEEwFXdp0-aDNTAo2Dkatvk72s-E0ESrergSOwfHlcbL_T3n6ANg27-cXbvbEAof2caet3NxTQm3WVo3sp3h53Ifsj-QuITHbwdqmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4d4e3672.mp4?token=Y5P8IAJxeFgRMjvyb9heT1mvO8Ymun6nlbAZMOa2Wz243zDteUc9sPBnjV50j8ZYfyCQj5X8OaduBjyOP-7SNJlA-b9x7StrVEhzVYWezb6a9iZlY_rrVl9hocOwW8ndbLx0fzUpYwjsj1LWcm8ght8ia8-iKmSBBKY4VdLhyB7NcC0KM36m7tAeXzHlP9VFiF1_6XdufGQPum3C3VT3MQkkYFR4DH-cUmilkI-3SHJ7fSq_pEEwFXdp0-aDNTAo2Dkatvk72s-E0ESrergSOwfHlcbL_T3n6ANg27-cXbvbEAof2caet3NxTQm3WVo3sp3h53Ifsj-QuITHbwdqmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس : بازی خطرناک تشدید درگیری؛
مقام‌های نظامی می‌گویند با نزدیک‌تر شدن حملات موشکی ایران به مناطق مرزی اسرائیل، خطر گسترش جنگ افزایش یافته است. به گفته آنها، ارتش اسرائیل در آماده‌باش کامل قرار دارد و مقام‌های تل‌آویو معتقدند تاکنون یک وضعیت بازدارندگی در برابر ایران ایجاد شده است.
بر اساس این ارزیابی، مقام‌های ایرانی نگران واکنش گسترده‌تر نیروی هوایی اسرائیل هستند، زیرا ورود مستقیم‌تر اسرائیل به درگیری می‌تواند خسارت سنگینی برای تهران به همراه داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19328" target="_blank">📅 17:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsvmfIZ5lJiH2VCtlVLamNT2UEMZOgziVOE4ICWf0zlekpoMLaP1Ge0v5juymGLV0IzNFeOkatuKUaq0ub1ey3VUCMsKNpwelBA2yFF6yJzJxvKAAKt5whhRN8hnDmGwcg3CjgDjjOoXtrudgiB7aW819M6Yz8uIumIc_F-DwMFfb4stdY3FCdCO1TpP5clx8amN1MFqZ0T41wUFeU1IQKEoWQqF1X42WMypjv0fHSVaawklaTCzTn1yhBmf1_JIR5Fm984TWUgl8x0uXx591mitcy_-ZdyJR53wlNE198_4vrAO6fDqsV_n-yVvv4bW9GAfdC9nH1AmHOhDTGL4Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراغه الان
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19327" target="_blank">📅 16:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svy2sUi2OBrR_Q6mJXj-qVXLWTPlrGQd2HfzZ-b96hGM8MlAf_O-yBicgFCHH7RHijwGpdmCrljFuEfrDuVFb_51UKydqRoV-yDfGROxpGvNCKOs5v3wb8aDDkeurAHLVuQTedwXjKst1a5hOfd3SAY2-bXxUH_kcy7GinjrFSzoIhugyH0ZQJzQ3FJYCVWsW53_TtT7NZSyfjP5S0ZSgvHxR4_ow3ZaWOG-nN4QOGTkqsi5RvHGWbKBfa2vY3h22Y7idd_R1vk9h8kVAPCei2qSI6Gdj8WFpGlI7Q0WtK0ZQ_47u8bD5XuWb8hROVWsP5YeU2WI_k35unl-mZZVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این لحظه به بعد، هر زمان که جمهوری اسلامی ایران به کشتی‌ای در تنگه هرمز شلیک کند، چه با موشک، راکت، پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه، از جمله آنهایی که در کنار یا در پایتخت تهران قرار دارند را بمباران و نابود خواهد کرد. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19326" target="_blank">📅 16:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19325" target="_blank">📅 16:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ در‌تروث : من به پایگاه هوایی دوفر می‌روم تا از قهرمانانمان (سربازان کشته‌شده در حمله ایران) تجلیل کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19324" target="_blank">📅 16:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8y5yzDNOT7WzNId7YLUGY_mEGCIdao5fG7np6OJneeS3-EyehOBYGXa5PTuGSfwrO8MCtjpeUy9ws3iNOGv28M2I2DVE7DxHUC24AXo23Oz62jKrivf9s_Lx2U-nU5espmYHhWyzQOwRJO6Hl7diJSXy0fIcnh3qUidp0V3eBfnywig2oJmuSd2EI2cRxaPC_kIMylDRG5yF1xaYS7vXWYMPACrQTo3fA_19JcOZKLdM4kVJ_hLY9NQUdG5L16qZsd3-hQLovQTXFSsN4YnPm0ferOKtlNcmqO1KehuEAfKDFvIT93-J1z_9RgPuTWsHmCLAorXKCxECT48oU9NbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWSNLRXcrG9s5BkuAbR4H8Vp9itV6rfwNEIYQZ9xFNerhh9F8qg4Im_mtxoLmBGcJ-FviNuHR-gNGiFQS0Kg4Xb8Id-IfEDeMo4WMq_wbs80UpoOht2EozTIBVFuiLjcA2DML0a84o0CJpAxjvCsJ-nOKcPiLv0VHk3XhB9P4HbklCssALEdPCQrOJZJY2IKoTKGiN1xNGUBRi5EW796v-8SCiMjFFhI3Da7vxpv4aKwLaLIGk5HApDDLBbxGW-sNKn5m0zO3k2L9CnDPcoHZ3Sx7p1ywJVwP1dJxAH-ibWGvYLP_yqoVv--0zgdwrvLi9bRvNoA7fCRlM3EBduUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b96zNYNZGkJLAnrHYI89gFdx2poEZHgDpBngMlFQrNtaxvRDaPcriNEa7uUua0KT2Uq76a1521scSaPQu_jx7W3_G1DpCNvBZjBenogUxVbxJMlpyATCP9LK0gA3-6FRRivpf6G2eykl63D1rxxtMuauzQQNWzk8PHxtkwoJECiGwzq8NoZYlbrkzylLnS_qRXt52vn_4aIH67AGnEZJbEcQbD4xw8mapleB0TJ3xkf0mYKGlzsixz3FuWNR0kdtLkttPc_yDkluF_HvwC38Dvu1jk2U1Vc3rMsbSj8IycqrKxNtFb2mxDepsNti8PeVmDubPdfZXSVxv2pwckNQrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01649fbed5.mp4?token=qw1sZoW1Wqq8KX-UMGzAOXxsNdUzPOH2GllBShdi1A4vGjV7eWWOIMOLkzlZnpLtb6HvhhfAIQiDij8OObP0ISShkDapXNm-IFK_d6TDgA7ANpJWkiddTvSs9laaY7q5pRJAJ6bwEOrrJPpp0YuM70LZ9TMo69I3khyvAN2CL_Gli4wzM9RbuKl-y65zx3wsbP599M7z5tus-iLxS0CcexH6yTc_GGXMeO46Svy-66KD3ia60a_JUuQR6fSlsRnU8xM2Lt3rle19Qsob30jbEijt0eGdh4WjyEd6w_1UQiArD4AeF6WiNMf8HqkX5zK30tJl_iwgTW6-tvV2PTKZ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01649fbed5.mp4?token=qw1sZoW1Wqq8KX-UMGzAOXxsNdUzPOH2GllBShdi1A4vGjV7eWWOIMOLkzlZnpLtb6HvhhfAIQiDij8OObP0ISShkDapXNm-IFK_d6TDgA7ANpJWkiddTvSs9laaY7q5pRJAJ6bwEOrrJPpp0YuM70LZ9TMo69I3khyvAN2CL_Gli4wzM9RbuKl-y65zx3wsbP599M7z5tus-iLxS0CcexH6yTc_GGXMeO46Svy-66KD3ia60a_JUuQR6fSlsRnU8xM2Lt3rle19Qsob30jbEijt0eGdh4WjyEd6w_1UQiArD4AeF6WiNMf8HqkX5zK30tJl_iwgTW6-tvV2PTKZ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشهای تایید نشده از حمله آمریکا  به پادگان همدان
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19320" target="_blank">📅 16:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه های رژیم از قول منابع در سپاه : دستور مقامات ارشد سپاه برای گسترش دامنه درگیری در غرب آسیا صادر شده و ضربات در ساعات آینده به مناطق غیرمنتظره خواهد رسید
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19319" target="_blank">📅 15:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بیشترین کمکی که شما به من می‌کنید انتشار این پست است. حتما مطمئن باشید چهار پلتفرم را فالو داشته باشید
🌐
instagram.com/yashar
🌐
t.me/WarRoom
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19318" target="_blank">📅 15:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
بیشترین کمکی که شما به من می‌کنید انتشار این پست است. حتما مطمئن باشید چهار پلتفرم را فالو داشته باشید
🌐
instagram.com/yashar
🌐
t.me/WarRoom
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19317" target="_blank">📅 15:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1db688120.mp4?token=O4YreKR0bV8epZJouGmvuRTmK1Lf_yFShKBvuNo5X32c3Oxj26QixyHj2_Q90cOhDm3aC03gnsias-CpMK6EVDKkFDIbisByLb2AIQVj9fqNCOxWxqi5lVk_HjdmjDBs-w8qYw9N5x4-sz-zI3dYoEJOiCASVpyiRwpptdAu0mFPqGDJsvfwifbYm1idpn6feZBHrRsSzkbkLj8hecTtLw-YCKPT1hKjIWyAyMvhpj26Zzm5-7Tow0-61i125qF2fBEgty0s4GhNjxpJA5iAitM1ylCTtWpC-JFZispXPhE5MCnHbrb0sNYd8PhOr38Bj5Wmh1i35xHOmoBcyYEh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1db688120.mp4?token=O4YreKR0bV8epZJouGmvuRTmK1Lf_yFShKBvuNo5X32c3Oxj26QixyHj2_Q90cOhDm3aC03gnsias-CpMK6EVDKkFDIbisByLb2AIQVj9fqNCOxWxqi5lVk_HjdmjDBs-w8qYw9N5x4-sz-zI3dYoEJOiCASVpyiRwpptdAu0mFPqGDJsvfwifbYm1idpn6feZBHrRsSzkbkLj8hecTtLw-YCKPT1hKjIWyAyMvhpj26Zzm5-7Tow0-61i125qF2fBEgty0s4GhNjxpJA5iAitM1ylCTtWpC-JFZispXPhE5MCnHbrb0sNYd8PhOr38Bj5Wmh1i35xHOmoBcyYEh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
عجب فیلمی‌ بدستم رسید</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19316" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
عجب فیلمی‌ بدستم رسید</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19315" target="_blank">📅 15:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJm9Sy2Nb-eGRj11AK1sk-xy8ZEq5YDgjoLfAg6OFRziPVLxEPtv07kKHAnHrsRRsR0Nh8P389kPqArTvvpBl_-CIhQL4P3Ov1Jd9IIc82kyAGB4ruHMWqoXSgMhRTOScz8sn7oxi-21qDLWRoEoFjk5XRZ1SXRhRbDg-6-9BwrXtZDSBtsh0BBi3XDp7qJst170f56s914laRWzOqdvw2WzcxwOvekzkhMJph4oP61HIN-2Wq5tY9VLTMTFqdEZY3Y14ikL0RQhodHYEg612o8RvAf6Ry0aE-H5a-nSEV7Mf79hI1QI1FNc8UX0vgrsYR2bhkeQ9n53s8FRI92rRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج جدید در این عکس شلیک موشک از شیراز. همچنین دوستی به ارسال عکسی که زود پاک کرد، نتوانستم سیو کنم نوشته بود: شلیک موشک از کرمانشاه به قدری قوی بود که شیشه های مغازهم داشت میشکست.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19314" target="_blank">📅 15:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عربستان از فعال شدن هشدارهای زودهنگام حمله موشکی در شهر الدمام خبر داد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19313" target="_blank">📅 15:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">موج جدید حملات رژیم به بحرین
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19312" target="_blank">📅 15:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرنگار اژدهایی : صدای ۳ انفجار در جزیره لارک و سیریک  شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19311" target="_blank">📅 14:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef1b4c242.mp4?token=WJjZ7OPAFjEi5c17QOK9dhDioPY8oK4pxdbSnGocOBMS_aSKRHSsaqHrWH3KGwPiQghLzsqZZr0U0IBiA8dFbijH2mFWFTZFGzsFyDDUkxMbf6-i7j2bs_oFa4Z9p4mUV4Oge7qS7AWlD3EQfIgtxnN5-kVSZSgii80p3SLmfhCWUvkcZldFSnKwDGkhmrEhN1Bpn05xjxMFbbggw5DveMHGuGvlvRqg5U-S42gv0ihZCKi1z9PxDiGPbqI5bjiMr7VUwww60rp6Va7mZeYh97APF3S3482LXWtd9CmcGcf-VBlUPNRvAbpxzhrmGWh5D4M3vbqa-aU8zzb5bQdBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef1b4c242.mp4?token=WJjZ7OPAFjEi5c17QOK9dhDioPY8oK4pxdbSnGocOBMS_aSKRHSsaqHrWH3KGwPiQghLzsqZZr0U0IBiA8dFbijH2mFWFTZFGzsFyDDUkxMbf6-i7j2bs_oFa4Z9p4mUV4Oge7qS7AWlD3EQfIgtxnN5-kVSZSgii80p3SLmfhCWUvkcZldFSnKwDGkhmrEhN1Bpn05xjxMFbbggw5DveMHGuGvlvRqg5U-S42gv0ihZCKi1z9PxDiGPbqI5bjiMr7VUwww60rp6Va7mZeYh97APF3S3482LXWtd9CmcGcf-VBlUPNRvAbpxzhrmGWh5D4M3vbqa-aU8zzb5bQdBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از سیریک  @WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19310" target="_blank">📅 14:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امروز صبح "مهدی خانکی" دانشجوی ۲۵ساله حقوق و از معترضان دی ماه ۱۴۰۴ اعدام شد؛
خبرگزاری میزان (وابسته یه قوه قضاییه) گفته که به دلیل همکاری با اسرائیل و آمریکا و ساخت سلاح و بمب های دست ساز، اعدام شده.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19309" target="_blank">📅 14:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8c355874.mp4?token=dXgaYf0IREZEMI3oBAr9QDkC51hyPrMCA3UCpnOEHc0_aHX3_N-Evp0QWFkg0O2RxmZ31omBCpB6Z74InXzrdg-zJ1ZdEbLiy4b39MRPOBaPwJ7YjDYMbu5uK9Gvdh1Xun2X3cqFRFSV4fUkklzD1VMp8ahK-kIBvQ3am24kwY4Xsx_MDurt9_rg4TE3OuR78CCdRmuytlBiUL4kRZpXloHYe-RgnusCDrGOWCch_fZMVrxHQXl7LAxJVR81HRrrEbjWSLxzonIg-SU-yMr6kn4UzoWmBMm2gECxMFj0FvWBXqT-ikqV8paX7nKvxlj8TeU6IKLJZk55Dd4C1mqmBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8c355874.mp4?token=dXgaYf0IREZEMI3oBAr9QDkC51hyPrMCA3UCpnOEHc0_aHX3_N-Evp0QWFkg0O2RxmZ31omBCpB6Z74InXzrdg-zJ1ZdEbLiy4b39MRPOBaPwJ7YjDYMbu5uK9Gvdh1Xun2X3cqFRFSV4fUkklzD1VMp8ahK-kIBvQ3am24kwY4Xsx_MDurt9_rg4TE3OuR78CCdRmuytlBiUL4kRZpXloHYe-RgnusCDrGOWCch_fZMVrxHQXl7LAxJVR81HRrrEbjWSLxzonIg-SU-yMr6kn4UzoWmBMm2gECxMFj0FvWBXqT-ikqV8paX7nKvxlj8TeU6IKLJZk55Dd4C1mqmBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند انفجار پی‌درپی سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19308" target="_blank">📅 14:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏کانال ۱۴ اسرائیل گزارش داد که کشورهای اطراف خلیج فارس در مورد چگونگی واکنش به رژیم اشغالگر جمهوری اسلامی اختلاف‌نظر دارند. برخی به پرزیدنت ترامپ فشار می‌آورند که به ایران حمله زمینی کند و برخی دیگر خواستار مذاکره ترامپ با ایران و اعلام آتش‌بس فوری هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19307" target="_blank">📅 13:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شبکه کان اسرائیل : جولانی اماده حمله به حزب الله می شود
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19305" target="_blank">📅 13:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وب‌‌سایت عربی ارم‌ نیوز:آمریکا به پاکستان اطلاع داده است در شرایط فعلی با آتش‌بس با ایران موافقت نخواهد کرد.
آمریکا به پاکستان اطلاع داد که برای ایجاد آتش‌بس و میانجیگری بین آمریکا و ایران اقدامی نکند، آمریکا میخواهد تمام توانمندی‌های تهاجمی سپاه رو از بین ببرد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19304" target="_blank">📅 13:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏منوچهر متکی: به محض حمله زمینی آمریکا، حمله زمینی جمهوری اسلامی به بحرین و کویت آغاز خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19303" target="_blank">📅 13:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چند انفجار پی‌درپی سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19302" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش انفجار‌ سیریک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19301" target="_blank">📅 13:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">از چه زمانی متوجه شدید جمهوری اسلامی جنایت کار است و اصلاح شدنی نیست</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19300" target="_blank">📅 13:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19299" target="_blank">📅 12:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">@WarRoom
ترکش های پرتاب شده به اسرائیل</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19298" target="_blank">📅 12:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">@WarRoom
روح و روان</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19297" target="_blank">📅 12:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKDpxwuO2cDyeYPlhEE41N4zXDuy5cqfH5KMrQrxqlqSuaET2f8i5M8cPzvrAwsImYT32Jrrc7NNBPZ0UrEiKVJvR0uAZqhor46GcxNDCWpmtwB-wh7Ww3l5b1d4J7XsdNGU53eAOgsHgFvnqJLq_a2qK5Z9drDiKPyGcnyVdsyZpO_yDGgtwop0l3ruRPBvw85-_n86gBPeRDyJuU7Fi8thrS72dcgPR8TV0zT0ax9CfJExuTkFdwUA29htmgH0LbXKx3JVTa_0cDNvysec_CYRYbEQkFvSLmUPMnyoDW3xxddQNfDd1BT2gKFQ0ORMYvcIFGdRcPFpQn8zc3rNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-rOiRLs4ekd4gpVwUuDQxorAYKZ6QCypU_JrYIVf7ei9dErBzSZPz1dC_MIKdkefxfTMgzfLMQfK9FN0L4YgG8KqIsX6goN8eeC0VfReu-UEpos3o79d9WH2O-sJJMZyUIx8ZOalN_mWrZ8JAsoPi4Vbb73sfHj1b7AQs5Db1tjMNEnxTUPYYrE435nknxAL3KFInyzzbOyazn48Luql01mI-xHXohXOZ_ZRCK53mhLV3bmyKVcU165zfc8ev2YIq84JHImaqvrFWH8Ute8jeUm471NGbvTnbBeJ_TvkIeu6eEnFUVk3cWlNfbFqA-fSUHbTyDlK7I2QMHOM1r1Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصایور جدید از انفجار‌ گاز در نارمک !
@WarRoom
که دیشب یه عده به من اومد توهین کردن !</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19295" target="_blank">📅 12:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOzfZPeMlbP7ACmYAc4Zn7D9XiDOo7qWVDRlqX9PK1-0oD7-MIN4SVMcfLsackuyuyjrYsooRGr5ZAnyNM0IDXZqOudjEYb1y55SBHddXcKnG-y3HudpIc6G2LZbnV6CnhL0WeOXGTyoBogtbZdBIvjGWCLDHU7EhhrgvWAKM_OcR7NU6Ud1TSrIMpHhlwfQAK55AEOFZdltMy734HRWrxVftbnlCwQf9Jud20zA1lbdviBUuEH7cSiz8wNzRPtaoawioNHErFiXMUjBeq4eAGfHUROVe59v_1qbXY46n-FgfsNRauUHk-h9h6n_kAxhX3RAKjS2vi0jiidJEf8YOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار : نفت به کانال مذاکرات و توافق رسید
نفت برنت به ۹۵$ رسید و هم اکنون ۹۴ معامله میشود
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19294" target="_blank">📅 12:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ارتش جمهوری اسلامی : پایگاه "الأزرق" در أردن و پایگاه "الشیخ عیسی" در بحرين را هدف قرار دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19293" target="_blank">📅 09:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتیجه جلسه دیشب : این یک جلسه بررسی و پرسش‌وپاسخ بود ، جمهوری‌خواهان عمدتاً از او حمایت کردند، اما دموکرات‌ها به‌شدت از نحوه مدیریت جنگ با ایران، هزینه‌ها و نبود شفافیت انتقاد کردند ،
هگست موفق شد از مواضع دولت دفاع کند، اما هنوز موفق به گرفتن بودجه از سنا نشده است
. روند تصویب ادامه دارد و احتمال دارد رأی‌گیری نهایی در هفته‌های آینده یا پس از بازگشت کنگره از تعطیلات انجام شود
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19292" target="_blank">📅 09:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19291" target="_blank">📅 09:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏معاون استاندار همدان اعلام کرد دیشب چند نقطه در شهرستان کبودرآهنگ هدف حمله هوایی آمریکا قرار گرفته و تاکنون جزئیاتی درباره اهداف، خسارات یا تلفات احتمالی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19290" target="_blank">📅 09:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHY8uAzTYkcVm5FiG_0Wdzr2KmFNFnL7pOtoEVaHbVQCKDTdvHCNta8Y9ZvDPwxQF0rgxc68BitzQewAZwYzVawHFmpBfOv2C8V2nTahbAYlOvyMSokAocYVuD_JqX9783INwqsv0ffXqIJj83pJ5DR0j5bnvagLWP98o8ljshVEVfHbakDkAjtkQtrN1vPZeHcbE1cCDa52vDw1Xf__KdiWe4b-O1Wr3vwpkWPBMMMUH-nGJ_4WFFf4It_sUjUzkIaEBMMy4ZnBrHXrbxnITRLNJh1jmLY-xdoYDFFxpbXmQSXVo-0uROkysrGNfkv5xPdmmyOZD3EYpu6U9EjV1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی نقاطی که گزارش انفجار ارسال شده (حتی تایید نشده)
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19289" target="_blank">📅 08:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اسپانیا ممنوعیت پرواز بر فراز حریم هوایی خود برای نیروی هوایی آمریکا را که در جنگ علیه ایران شرکت دارد، تداوم بخشید.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19288" target="_blank">📅 08:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فهرست حملات آمریکا در بامداد چهارشنبه
💥
سیریک (هرمزگان)
💥
بوشهر
💥
بهبهان (خوزستان)
💥
امیدیه (خوزستان)
💥
تبریز
💥
چابهار(سیستان و بلوچستان)
💥
کنارک (سیستان و بلوچستان)
💥
چوار (ایلام)
💥
آبدانان (ایلام)
💥
بانه (کردستان)
🚨
تهران: صدای شلیک پدافند @WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19287" target="_blank">📅 08:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630b6aa1be.mp4?token=nMC6inSgFb3CkTtpW0yr8EI61fD9ZceOhtXp0h5i6E3ABoWIf_H3w47k47kzGJshIQX9_XA9jH0_W06fj50pkjhtPS-wxPGNsNBTYxt1c1plG8gVBPKJcaq63VnPZnrSMlIZxN-Xt3qdSNoXzwk6dY15yp0mB8PWabokfejN1ecnMfIP-RJ5FJPxsHgulhz2pmKERHu2ab6opNusl_NwzhDAvy5HJw_nd-fOH0JghANpXfLdX7x9wD6pIaV8MbSEbslSV3QfmRX8CHtsV5cIu98Qc9_Gfpbmshmf62iWwFjK_qEOcoULt_EkoaR0lw-vEieLjNU3tYIyiRzGz34VwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630b6aa1be.mp4?token=nMC6inSgFb3CkTtpW0yr8EI61fD9ZceOhtXp0h5i6E3ABoWIf_H3w47k47kzGJshIQX9_XA9jH0_W06fj50pkjhtPS-wxPGNsNBTYxt1c1plG8gVBPKJcaq63VnPZnrSMlIZxN-Xt3qdSNoXzwk6dY15yp0mB8PWabokfejN1ecnMfIP-RJ5FJPxsHgulhz2pmKERHu2ab6opNusl_NwzhDAvy5HJw_nd-fOH0JghANpXfLdX7x9wD6pIaV8MbSEbslSV3QfmRX8CHtsV5cIu98Qc9_Gfpbmshmf62iWwFjK_qEOcoULt_EkoaR0lw-vEieLjNU3tYIyiRzGz34VwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو های حمله به پادگان بخردیان بهبهان
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19284" target="_blank">📅 08:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jl_z4dpcN6figfwr7bPhUcme2NWjIUVheEtcHR8K7B1NlV_NjPxsxRtgp8EJWxCO1y0TOuHpZx45bstJOD1cPR6UJHM8LGhA5DMJ5IQ3RAaDI8QHEmr7PXefD-5x78CDcjZXhm6tGbPqSyYqc1UOLb7MA7_1DaSq-nMqxq7kwc8cHOoic8WtH-f85-UulMdk7HoMAsZ6qsnqPtF8ILK0hLp0lyxD-KbrO43OQ2oK9iGTVqp5r3amNG1IM4uZI3Jirh9drhOoCkmAVyf7rv1TonAQm23DU-c6M7kkqTxxkzyienDWm_p88D7ELDIU7zOzy8zmTGlfoAN9AJd734ZWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqTSAJyFeqBVOYbK5hRH9gdpTFPOR83HrttzX5CEzZwcatjbTteNulpJLA5z4xpLQae4UlCmjnvLWKY2DZ3cG0SUYhb_OTPZsZpFat_f85-zUYcXLXK5hEB-n_CSCU1V2vw2z-cuEkhFGHDWjMvQX9OWRXAkD6rRYJXZFqyb58TzvsXL2lYzcOAPnKNfIpu165fRo2eHMs-7VQtMGVa19JDtp8iTnDxD4KSLuSusep4XknuTlFbxqdPVYNw9V7GCPK9yuFGsTbgh5zae50LoNIIL7-_RUO98yQi_TZRdNIoRMEoZvG6YUuCeBv6ry1eMxkaqfLGfErYaQGmlSLfCqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فهرست حملات آمریکا در بامداد چهارشنبه
💥
سیریک (هرمزگان)
💥
بوشهر
💥
بهبهان (خوزستان)
💥
امیدیه (خوزستان)
💥
تبریز
💥
چابهار(سیستان و بلوچستان)
💥
کنارک (سیستان و بلوچستان)
💥
چوار (ایلام)
💥
آبدانان (ایلام)
💥
بانه (کردستان)
🚨
تهران: صدای شلیک پدافند @WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19282" target="_blank">📅 08:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxrZEc4e8o84npCCsABmeqvAVXpHXCCMm1cQFKjH_7Clf8NkiDkgp2GVOyaIHBSUdQw1738P8rpIl4fB3VNS86sxzy5PS47lmydV0wTUbIHE6L_CKum8JqGY4UgurBqmhEivl3nKp7q4jSh98_ZoFyyEWed2oFw3gSXX98hvJDto60OLAJReNxwvwpZc0NabH6zM_qFEySpEnntFBuzKEaTe9rag4IPB-XmIbgkoekU2HuCdnKDRYTu2zJsIB3YI_auv8G22ieI5Ya6LDsvi6SQbcXmTNsYzb0PtsI_JU0cEq6h3JYIswdrqkdJBJYLxSRbgxBlUnT7CASFbVcNnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای ارتباطات هوایی آمریکایی مدل E-11A BACN (روتر وای‌فای در آسمان )از آمریکا به پایگاه هوایی رامشتاین آلمان رسید و احتمالاً در ادامه به پایگاه الامیر سلطان در عربستان سعودی منتقل خواهد شد، جایی که در حال حاضر بین ۴ تا ۵ فروند از همین نوع هواپیما مستقر هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19281" target="_blank">📅 08:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجار بامداد امروز در نارمک تهران یک انفجار نامشخص باعث شد میله‌ها و ورق‌های پلاستیکی به اطراف پرتاب شده و سه تا از شیشه‌های خانه های مجاور شکسته و به خودروی ام وی ام پارک شده هم خسارت جزئی وارد شود، اما حادثه مصدومی نداشت. @WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19280" target="_blank">📅 08:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجار بامداد امروز در نارمک تهران
یک انفجار نامشخص باعث شد میله‌ها و ورق‌های پلاستیکی به اطراف پرتاب شده و سه تا از شیشه‌های خانه های مجاور شکسته و به خودروی ام وی ام پارک شده هم خسارت جزئی وارد شود، اما حادثه مصدومی نداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19279" target="_blank">📅 08:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فهرست حملات آمریکا در بامداد چهارشنبه
💥
سیریک (هرمزگان)
💥
بوشهر
💥
بهبهان (خوزستان)
💥
امیدیه (خوزستان)
💥
تبریز
💥
چابهار(سیستان و بلوچستان)
💥
کنارک (سیستان و بلوچستان)
💥
چوار (ایلام)
💥
آبدانان (ایلام)
💥
بانه (کردستان)
🚨
تهران: صدای شلیک پدافند
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/19278" target="_blank">📅 08:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11cb529807.mp4?token=cAqeXLLUuxSTicvUmwkteDkks0ld_4CBVKLtsGfCogjYoRX6GBdbfyEDdPn9_AWOj-KryEQPgQka7186EOmAtYOeSis2XhyGqfJNxgPD5X1y7IV1Y5DF1U3B-RclGH_w1t45HcRlmZVpxQdXAvJRJlD0ASxRsAy6UOtqF3ujzQnrc0KmYdoaju_VUkZ0KoICkI87HIcdhUmgeDXry6LyihQ1qNaZsEw3v5Nb6EPrmdTzkUyzmYxU51vDjI3P3QPeSqv2K2U5L10ftklSSN962NYVWKenu5vd2rPBbyh851j8qkI9tbcFLvdECC8Nq3Lydb-_BuOHq_xTTDP8nR1yVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11cb529807.mp4?token=cAqeXLLUuxSTicvUmwkteDkks0ld_4CBVKLtsGfCogjYoRX6GBdbfyEDdPn9_AWOj-KryEQPgQka7186EOmAtYOeSis2XhyGqfJNxgPD5X1y7IV1Y5DF1U3B-RclGH_w1t45HcRlmZVpxQdXAvJRJlD0ASxRsAy6UOtqF3ujzQnrc0KmYdoaju_VUkZ0KoICkI87HIcdhUmgeDXry6LyihQ1qNaZsEw3v5Nb6EPrmdTzkUyzmYxU51vDjI3P3QPeSqv2K2U5L10ftklSSN962NYVWKenu5vd2rPBbyh851j8qkI9tbcFLvdECC8Nq3Lydb-_BuOHq_xTTDP8nR1yVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام :
امروز ۰۲:۳۰ بامداد
۳۱ تیر به وقت تهران حملات خود را آغاز و ۰۳:۴۵ بامداد (در ۷۵ دقیقه)
با موفقیت
یازدهمین شب متوالی حملات
علیه ایران را به پایان رساندیم.
نیروهای سنتکام
مراکز عملیات نظامی، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی ایران
را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در
تنگه هرمز
بیش از پیش تضعیف شود
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/19277" target="_blank">📅 07:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19276" target="_blank">📅 02:16 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
